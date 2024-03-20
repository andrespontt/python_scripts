import os
import requests

os.environ['HTTP_PROXY'] = 'http://localhost:8080'
os.environ['HTTPS_PROXY'] = 'http://localhost:8080'

response = requests.get('https://github.com', verify=False)
