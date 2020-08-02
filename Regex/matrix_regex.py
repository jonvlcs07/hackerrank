#!/usr/bin/env python3
import re

test = ["7 3\nTsi\nh%x\ni #\nsM \n$a \n#t%\nir!"]

# print(test[0])
n = int(input()[0])
first_multiple_input = []

for i in range(n):
    first_multiple_input.append(input())

print(first_multiple_input)

text = ""
for i in range(len(first_multiple_input[0])):
    for line in first_multiple_input:
        text += line[i]

print(text)

text = re.sub(r'(?<=\w)(\W+)(?=\w)', " ", text)

print(text)