import wifiCfg
from IoTcloud.AWS import AWS
import json
import wifiCfg
from uiflow import *

def SavetoAWS(Dictionary):
    
    if str(wifiCfg.wlan_sta.isconnected()) != "True":
        wifiCfg.doConnect('Home', '01819119321')
    
    aws = AWS(things_name='AWS_CORE2', host='a25wmxf9jzsaoa-ats.iot.us-west-2.amazonaws.com', port=8883, keepalive=60, cert_file_path="/flash/res/certificate.pem.crt", private_key_path="/flash/res/private.pem.key")
    aws.start()
      
    aws.publish(str('env/msg'),str((json.dumps((Dictionary)))))

    wait(2)

def EditonAWS(Dictionary):

    if str(wifiCfg.wlan_sta.isconnected()) != "True":
        wifiCfg.doConnect('Home', '01819119321')
    
    aws = AWS(things_name='AWS_CORE2', host='a25wmxf9jzsaoa-ats.iot.us-west-2.amazonaws.com', port=8883, keepalive=60, cert_file_path="/flash/res/certificate.pem.crt", private_key_path="/flash/res/private.pem.key")
    aws.start()
      
    aws.publish(str('env/msg'),str((json.dumps((Dictionary)))))

    wait(2)
