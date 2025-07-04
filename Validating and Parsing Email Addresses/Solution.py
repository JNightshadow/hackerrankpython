import email.utils
import re
n = int(input())
for i in range(n):
    addr = input()
    addrCheck = email.utils.parseaddr(addr) 
    if(re.match(r'^[a-zA-Z]+[a-zA-Z-\._0-9]*@[a-zA-Z]+\.[a-zA-Z]{1,3}$',addrCheck[1])):
        print(addr)
