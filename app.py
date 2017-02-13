import os, json, requests
from flask import Flask,request,Response

port = int(os.getenv('PORT',8080))

app = Flask(__name__)

omnibusUrl = os.getenv('omnibus_url')

@app.route("/",methods=['POST'])
def root():
  # Get the JSON in the request
  j = request.form.to_dict()
  print 'Received a request'
  print j
  print 'Forwarding to ' + omnibusUrl + ' as application/json'
  
  # Omnibus only wants the data in 'payload', so extract this part and send
  r = requests.post(omnibusUrl, data=j['payload'], headers={'Content-Type': 'application/json'})
  print 'Status code: ' + str(r.status_code)
  resp = Response(status=r.status_code)
  print resp

  return resp

app.run(host='0.0.0.0', port=port) 
