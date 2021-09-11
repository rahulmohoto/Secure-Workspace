import wifiCfg
from IoTcloud.AWS import AWS
import json
import wifiCfg
from uiflow import *
import time

GetJSONValue = None

def fun_env_core_(topic_data):
  global GetJSONValue
  GetJSONValue = json.loads(topic_data)
  pass

def getDataAWS():
  
    global GetJSONValue
    
    if str(wifiCfg.wlan_sta.isconnected()) != "True":
        wifiCfg.doConnect('Home', '01819119321')
    
    aws = AWS(things_name='AWS_CORE2', host='a25wmxf9jzsaoa-ats.iot.us-west-2.amazonaws.com', port=8883, keepalive=60, cert_file_path="/flash/res/certificate.pem.crt", private_key_path="/flash/res/private.pem.key")
    aws.subscribe(str('env/core'), fun_env_core_)
    aws.start()
      
    aws.publish(str('env/msg'),str((json.dumps(({"Tag":"Fetch_Data"})))))
    
    start = time.ticks_ms()
    while (time.ticks_ms() - start) <= 10000:
      aws.subscribe(str('env/core'), fun_env_core_)
      if GetJSONValue != None:
        break

    return GetJSONValue

# SavetoAWS()
