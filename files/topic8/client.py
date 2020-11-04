import os
import requests
import json
import time

uri = 'http://bioinf.cs.ucl.ac.uk/psipred/api/submission'

payload = {'input_data': ('prot.txt', open('input.txt', 'rb'))}
data = {'job': 'psipred',
        'submission_name': 'test',
        'email': 'daniel.buchan@ucl.ac.uk', }
print("Sending Request")
r = requests.post(uri+".json", data=data, files=payload)
response_data = json.loads(r.text)

while True:
   print("Polling result for: "+response_data['UUID'])
   result_uri = uri+"/"+response_data['UUID']
   r = requests.get(result_uri, headers={"Accept":"application/json"})
   result_data = json.loads(r.text)
   if "Complete" in result_data['state']:
       print(r.text)
       break
   else:
       time.sleep(30)
