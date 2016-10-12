import requests
import ast

def main():
	token = "e1d46e96a93e555411fd9f06333a348d"
	url = "http://challenge.code2040.org/api/prefix"
	payload = {"token" : token}

	response = requests.post(url, data=payload)

	d = ast.literal_eval(response.content)

	pre = d['prefix']
	words = d['array']

	words_no_pre = []
	print pre
	print words
	for w in words:
		if not w.startswith(pre):
			words_no_pre.append(w)
	print words_no_pre
	url = "http://challenge.code2040.org/api/prefix/validate"
	payload = {"token" : token, "array" : words_no_pre}

	response = requests.post(url, data=payload)
	print response.content


if __name__ == '__main__':
	main()