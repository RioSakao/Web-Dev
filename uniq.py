#! /usr/bin/python3
import sys

lines = sys.stdin.readlines()

Uniq = {}

for line in lines:
  Uniq[line] = 0

for key in Uniq:
  print(key, end="")
