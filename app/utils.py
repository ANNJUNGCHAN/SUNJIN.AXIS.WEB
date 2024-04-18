import os
import json
from PIL import Image, ImageOps, ImageDraw

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

# 이미지를 원형으로 만드는 함수
def make_circle(img):
    mask = Image.new('L', img.size, 0)
    mask_draw = ImageDraw.Draw(mask) 
    mask_draw.ellipse((0, 0) + img.size, fill=255)
    result = ImageOps.fit(img, mask.size, centering=(0.5, 0.5))
    result.putalpha(mask)
    return result