import hashlib
import os
import base64

with open("password.lst", "r") as f: #abrir aquivo
    temp = f.read().splitlines() #ler o arquivo e dividir em linhas
    for each_element in temp: #para cada palavra em uma linha
        result = hashlib.md5(each_element.encode("utf-8")).hexdigest()
        base = base64.b64encode(result.encode())
        sha = hashlib.sha1(base).hexdigest()
    
        if sha == "806825f0827b628e81620f0d83922fb2c52c7136":
            print (each_element)
            break
