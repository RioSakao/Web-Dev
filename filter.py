#! /usr/bin/python3
import sys

lines = sys.stdin.readlines()
for line in lines:
  tokens = line.split(", ")

for token in tokens[:-1]:
  print(token)

