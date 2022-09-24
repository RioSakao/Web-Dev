#! /usr/bin/python3
import sys

lines = sys.stdin.readlines()

LowerList = []

for line in lines:
  LowerList.append(line.lower())

temp_token = ''
for token in LowerList:
  token = token.rstrip("\n")
  if token[0] == "a" or token[0] == "e"\
     or token[0] == "i" or token[0] == "o" or token[0] ==  "u":
    print(token + "-yay")
  else:
    for i in range(len(token)):
      temp_token += token[i]
      if token[i] == "a" or token[i] == "e"\
          or token[i] == "i" or token[i] == "o" or token[i] ==  "u":
        print(token[i:] + "-" + temp_token[:-1] + "ay")
        temp_token = ""
        break
