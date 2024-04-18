import os
import json

def Load_Private_Info(SETTING_PATH) :
    
    # JSON 불러오기
    with open(os.path.join(SETTING_PATH), 'r') as f :
        json_data = json.load(f)
        
        host=json_data['host']
        port = json_data['port']
        user=json_data['user']
        password=json_data['password']
        db=json_data['DB']
        
    return host, port, user, password, db