#!/usr/bin/env python3
import re

def validate_card(string):
    
    if '-' in string:
        if not re.match(r'^[456]\d{3}\-\d{4}\-\d{4}\-\d{4}$', string):
            return 'Invalid'
    else:
        if not re.match(r'^[456]\d{3}\d{4}\d{4}\d{4}$', string):
            return 'Invalid'
    
    temp_string = string.replace('-','') #modificar isso depois
    if any([re.match(r'(\d)\1{3}', temp_string[i:i+4])
             for i in range(len(temp_string)-3)]):
        return 'Invalid' 
    return 'Valid'

for _ in range(int(input().strip())):
    print(validate_card(input().strip()))

