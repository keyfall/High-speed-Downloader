import os, subprocess

magnet_link = "magnet:?xt=urn:btih:C168B7AD1413C99338EAEFA9C1A0E781F27D3072"

command = 'ping google.com -n 3'
output = subprocess.check_output(command, shell=True, text=True)
print(output)
