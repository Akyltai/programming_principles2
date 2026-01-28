import sys
import os

print("Python version:", sys.version)
print("Your current holder:", os.getcwd())

name = input("What's your name? ")
print("Hello, " + name + "! Your really cool guys.")

a = 15
b = 4
result = a * b
print(f"result of product {a} to {b} equel {result}")

import sys

print("Available modules:")
print(sys.builtin_module_names)

import sys

print("The path to the interpreter that executes this code:")
print(sys.executable)