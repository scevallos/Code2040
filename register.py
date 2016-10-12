import requests

def main():
	url = 'http://challenge.code2040.org/api/register'
	payload = {'token' : 'e1d46e96a93e555411fd9f06333a348d', 'github' : 'https://github.com/scevallos/Code2040'}

	response = requests.post(url, data=payload)

	print response.content

if __name__ == '__main__':
	main()