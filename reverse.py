import requests

def main():

	# Setup url to request, save token for easier access, and payload to send with requests
	url = "http://challenge.code2040.org/api/reverse"
	token = "e1d46e96a93e555411fd9f06333a348d"
	payload = {"token" : token}

	# Get word to reverse
	response = requests.post(url, data=payload)
	word = response.content

	# Reverse the word
	rev = word[::-1]

	# Update url and data with reversed word
	url = "http://challenge.code2040.org/api/reverse/validate"
	payload = {"token" : token, "string" : rev}

	# Send it back to the API
	response = requests.post(url, data=payload)

	# Are we good?
	print response.content


if __name__ == '__main__':
	main()
