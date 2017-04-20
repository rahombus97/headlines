# headlines.py

from flask import Flask, render_template
import requests
import json

app = Flask(__name__, template_folder='.')

@app.route('/')
def homepage():
  params = {
    'api_key': 't_H-3XReE6Bi',
  }
  r = requests.get(
      'https://www.parsehub.com/api/v2/projects/t3S06TF2VeSo/last_ready_run/data',
      params=params)
  return render_template('headlines.html', headlines=json.loads(r.text)['Headlines'])

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)


"""
@app.route('/')
def homepage():
  params = {
    'api_key': '{API_KEY}',
  }
  r = requests.get(
      'https://www.parsehub.com/api/v2/projects/{PROJECT_TOKEN}/last_ready_run/data',
      params=params)
  return render_template('movies.html', movies=json.loads(r.text)['movies'])


@app.route('/')
def homepage():
  with open('/tmp/headlines.json', 'r') as f:
    return render_template('headlines.html', movies=json.loads(f.read())['Headlines'])
"""