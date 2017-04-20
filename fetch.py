# fetch.py

import requests
import os

params = {
  'api_key': 't_H-3XReE6Bi',
}
r = requests.get(
    'https://www.parsehub.com/api/v2/projects/t3S06TF2VeSo/last_ready_run/data',
    params=params)

with open('/tmp/headlines.tmp.json', 'w') as f:
  f.write(r.text)

os.rename('/tmp/headlines.tmp.json', '/tmp/headlines.json')