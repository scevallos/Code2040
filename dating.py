import requests
import datetime
import dateutil.parser
import ast

# Set up constants, to be used in requests
token = "e1d46e96a93e555411fd9f06333a348d"
u_in = "http://challenge.code2040.org/api/dating"
u_out = "http://challenge.code2040.org/api/dating/validate"

# Asking for the datestamp & interval dictionary
r = requests.post(u_in, data={"token" : token})

# Content is a long string, convert to dictionary with literal eval
d = ast.literal_eval(r.content)

# Store each item in a variable
date = d['datestamp']
interval = d['interval']

# Convert given date from ISO 8601 to datetime object
date = dateutil.parser.parse(date)

# Convert seconds to be added to the date as datetime object
interval = datetime.timedelta(seconds=interval)

# Add them together to get elapsed time
new_date = date + interval

# Convert back from datetime object to ISO 8601
a = new_date.isoformat()

# Properly format as it was given
a = a[:len(a)-6] + "Z"

# Send back the answer
r2 = requests.post(u_out, data={"token" : token, "datestamp" : a})

print r2.content
