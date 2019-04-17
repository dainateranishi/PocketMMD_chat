import requests

TXT_MIMETYPE = 'text/plain'

if __name__ == "__main__":
    filename = 'bbb.txt'
    filedatabinary = open(filename, 'rb').read()
    files = {'uploadFile':(filename, filedatabinary, TXT_MIMETYPE)}

    url = 'http://localhost:3000/data/upload'
    response = requests.post(url, files=files)

    print(response.status_code)
    print(response.content)
