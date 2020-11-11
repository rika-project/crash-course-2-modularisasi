import requests

url = 'https://detik.com'

try:
    response = requests.get(url)
    if response == 200 :
        print(f'Succes! Response = {response}')
        print(f'Content {response.text}')
    else :
        print(f'Sorry ada kesalahan request {response.status_code}')
except Exception as e :
    print(f'There is an error {e}')
print('Program Ended')
