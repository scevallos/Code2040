import requests
import ast

# Set up constants to be used in requests
token = "e1d46e96a93e555411fd9f06333a348d"
u_in = "http://challenge.code2040.org/api/prefix"
u_out = "http://challenge.code2040.org/api/prefix/validate"

# Get dictionary from the API
r = requests.post(u_in, data={"token": token})

# Given as string object, so literal eval to make it a dict
d = ast.literal_eval(r.content)

# Store the values
p = d['prefix']
w = d['array']

# Copy over the words that do not start with the prefix
words = []
for a in w:
    if not a.startswith(p):
        words.append(a)

# Send the new array 
r2 = requests.post(u_out, json={"token" : token, "array" : words})

# Prints response
print r2.content
