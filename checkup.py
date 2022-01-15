import sys
import requests

try:
    with open(sys.argv[1], 'r') as f:
        for i in f:
            x = requests.get(i.strip())
            print('{}[{}]'.format(i.strip(), x.status_code))
except Exception as err:
    print(err)
