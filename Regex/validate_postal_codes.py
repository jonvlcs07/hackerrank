#!/usr/bin/env python3

import re

tests = ['110000', '123456',
         '111110000']

def regex_integer_in_range(number):
    
    p = r'^[1-9][0-9]{5}$'
    match =  re.match(p, number)
    return match

def regex_alternating_repetitive_digit_pair(number):

    p = r'(\d)(?=.\1)'
    alternating_digits = len(re.findall(p, number))
    return alternating_digits


def validate_postal_code(number):

    valid = (bool(regex_integer_in_range(number))
             and
             (regex_alternating_repetitive_digit_pair(number) < 2))
    return valid

for _ in range(int(input().strip())):
    print(validate_postal_code(input().strip()))

print("Testes de validação de numeros permitidos")
for i in tests:
    print(regex_integer_in_range(i))

print("Testes de validação de digitos repetidos que se alternam")
for i in tests:
    print(regex_alternating_repetitive_digit_pair(i))

print("Testes de validação dos códigos")
for i in tests:
    print(validate_postal_code(i))




