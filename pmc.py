# coding: utf-8
# Wrote by Sanix-darker
#
import pymemcache
import argparse

Client = pymemcache.client.base.Client
ArgumentParser = argparse.ArgumentParser

# Initialize the arguments
# Example seting a value : python pmc.py -i 127.0.0.1 -s test -v value -x 100
# Example getting value : python pmc.py -i 127.0.0.1 -g test
prs = ArgumentParser()
prs.add_argument('-i', '--ip', help='The memcache ip address', type=str, default="localhost")
prs.add_argument('-p', '--port', help='The default port where the memcache is running', type=int, default=11211)
prs.add_argument('-g', '--get', help='Give the key of what you want', type=str)
prs.add_argument('-s', '--set', help='Set the key of what you want to save', type=str)
prs.add_argument('-v', '--val', help='Set the value of what you want to save in the key', type=str, default="")
prs.add_argument('-x', '--exp', help='Set the expiration time in seconds for the key', type=int, default=0)
prs = prs.parse_args()

try:
    client = Client((prs.ip, prs.port))
    if (prs.set != None):
        client.set("".join(prs.set.replace("\n", "").split()), prs.val, prs.exp)
        print("SET: ",prs.set, ":", prs.val, prs.exp)
    else:
        if (prs.get != None):
            print(client.get(prs.get).decode("utf-8"))
except Exception as es: print("ERROR: ", es)
