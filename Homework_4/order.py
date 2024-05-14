import requests
import json

device_name = "SAN-5988 Test Device"
devices_names = []
for i in range(10):
  devices_names.append(device_name + "_" + str(i+1))

device_Eui = "fa43b8fffe00035"
devices_Euis = []
for i in range(len(devices_names)):
  devices_Euis.append(device_Eui + str(i))
#print(devices_Euis)

new_name = "CODE updated"
new_names =[]
for i in range(len(devices_names)):
  new_names.append(devices_names[i] + " " + new_name)
#print(new_names)

device_url = "https://chirpstack-api.iotserv.ru/api/devices/"
devices_urls = []
for i in range(len(devices_names)):
  devices_urls.append(device_url + devices_Euis[i])
#print(devices_urls)


def create_device(d_name, eui):
    applicationId = "22581d62-7777-429a-b816-12bf56f35f6e"
    description = d_name
    devEui = eui
    deviceProfileId ="29d26ba4-2bf0-452e-9341-2671f442c7da"
    isDisabled = False
    joinEui = "0000000000000000"
    name = d_name
    skipFcntChec = False

    url = "https://chirpstack-api.iotserv.ru/api/devices"
    payload = json.dumps({
      "device": {"applicationId": applicationId,
                "description": description,
                "devEui": devEui,
                "deviceProfileId": deviceProfileId,
                "isDisabled": isDisabled,
                "joinEui": joinEui,
                "name": name,
                "skipFcntCheck": skipFcntChec}
    })
    headers = {
      'Content-Type': 'application/json',
      'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJjaGlycHN0YWNrIiwiaXNzIjoiY2hpcnBzdGFjayIsInN1YiI6IjY2MWQ1MTk3LTE2ZTAtNDBkZi1hZDk3LTJlYzgwM2QzZTllZCIsInR5cCI6ImtleSJ9.x5FnyRtUcrIqpYOYP_tiyCqAbews4L67kQmtv9HBTRI'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)
    return response

def delete_devices(urls):
   
  payload = {}
  headers = {
    'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJjaGlycHN0YWNrIiwiaXNzIjoiY2hpcnBzdGFjayIsInN1YiI6IjY2MWQ1MTk3LTE2ZTAtNDBkZi1hZDk3LTJlYzgwM2QzZTllZCIsInR5cCI6ImtleSJ9.x5FnyRtUcrIqpYOYP_tiyCqAbews4L67kQmtv9HBTRI'
  }

  response = requests.request("DELETE", url, headers=headers, data=payload)

  print(response.text)
  return response   

def change_names(names, urls):

  url = urls[i]
  payload = json.dumps({
    "device": {
      "applicationId": "22581d62-7777-429a-b816-12bf56f35f6e",
      "deviceProfileId": "29d26ba4-2bf0-452e-9341-2671f442c7da",
      "name": names
      }
  })
  headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJjaGlycHN0YWNrIiwiaXNzIjoiY2hpcnBzdGFjayIsInN1YiI6IjY2MWQ1MTk3LTE2ZTAtNDBkZi1hZDk3LTJlYzgwM2QzZTllZCIsInR5cCI6ImtleSJ9.x5FnyRtUcrIqpYOYP_tiyCqAbews4L67kQmtv9HBTRI'
  }

  response = requests.request("PUT", url, headers=headers, data=payload)

  print(response.text)
  return response

def device_info():
  
  url = "https://chirpstack-api.iotserv.ru/api/devices?limit=11&applicationId=22581d62-7777-429a-b816-12bf56f35f6e"
  payload = {}
  headers = {
    'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJjaGlycHN0YWNrIiwiaXNzIjoiY2hpcnBzdGFjayIsInN1YiI6IjY2MWQ1MTk3LTE2ZTAtNDBkZi1hZDk3LTJlYzgwM2QzZTllZCIsInR5cCI6ImtleSJ9.x5FnyRtUcrIqpYOYP_tiyCqAbews4L67kQmtv9HBTRI'
  }

  response = requests.request("GET", url, headers=headers, data=payload)

  print(response.text)
  return response  

dev_name = devices_names[0]
eui = devices_Euis[0]
url = devices_urls[0]
n_name = new_names[0]
for i in range(len(devices_names)):
    dev_name = devices_names[i]
    eui = devices_Euis[i]
    url = devices_urls[i]
    n_name = new_names[i]
    #create_device(dev_name, eui)
    delete_devices(devices_urls)
    #change_names(n_name, devices_urls)
device_info()
