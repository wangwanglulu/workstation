import requests     
    
KEY = '' # 这里填拿到的key    
    
def get_response(msg):    
    apiUrl = 'http://www.tuling123.com/openapi/api'    
    data = {    
        'key'    : KEY,    
        'info'   : msg,    
        'userid' : '', #这里填你的id    
    }    
    try:    
        r = requests.post(apiUrl, data=data).json()    
        return r.get('text')    
    except:    
        return None
print(get_response('你好'))