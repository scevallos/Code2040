import requests
import ast

def main():
	# Set up url and token
	token = "e1d46e96a93e555411fd9f06333a348d"
	url = "http://challenge.code2040.org/api/haystack"
	payload = {"token" : token}

	# Get the needle & haystack dictionary
	response = requests.post(url, data=payload)

	d = ast.literal_eval(response.content)

	words = d['haystack']
	look = d['needle']

	for i in range(0, len(words)):
		if look == words[i]:
			index = i

	# Send back the index
	url = "http://challenge.code2040.org/api/haystack/validate"
	payload = {"token" : token, "needle" : index}

	response = requests.post(url, data=payload)

	print response.content

if __name__ == '__main__':
	main()