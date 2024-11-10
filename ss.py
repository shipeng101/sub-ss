import requests
import random
import string
import json
import warnings

warnings.filterwarnings("ignore")

host = "api.fenghuolun.xyz"
tg = "https://t.me/MFJD666"

def generate_random_alpha_string(length=6):
    letters = string.ascii_letters + string.digits
    return "".join(random.choices(letters, k=length))

email = f"{generate_random_alpha_string()}@gmail.com"
password = f"{generate_random_alpha_string(10)}"

register_url = f'https://{host}/api/v1/passport/auth/register'
register_data = {
    "email": email,
    "password": password,
    "invite_code": "pXdFSnIH",
    "email_code": "pXdFSnIH"
}

register_response = requests.post(register_url, data=register_data, verify=False)
if register_response.status_code == 200:
    register_json = register_response.json()
    print("机场:https://" + host)
    print("账号: " + email)
    print("密码: " + password)


    auth_data = register_json.get('data', {}).get('auth_data')
    if auth_data:
        login_url = f'https://{host}/api/v1/passport/auth/login'
        login_data = {
            "email": email,
            "password": password
        }
        headers = {
            "authorization": f'{auth_data}',
            "Referer": f'https://{host}/',
            "Host": f'{host}'
        }

        login_response = requests.post(login_url, data=login_data, headers=headers, verify=False)
        if login_response.status_code == 200:
            login_json = login_response.json()
            auth_data = login_json.get('data', {}).get('auth_data')
            token = login_json.get('data', {}).get('token')

            if auth_data:
                subscribe_url = f'https://{host}/api/v1/client/subscribe?token={token}'
                print("\n关注TG频道获取更多资源:" + tg)
                print("订阅地址:\n" + subscribe_url)
            else:
                print('无法提取新的auth_data。')
        else:
            print('登录失败，状态码：', login_response.status_code)
            print(login_response.text)
    else:
        print('无法提取注册时的auth_data。')
else:
    print('注册失败，状态码：', register_response.status_code)
    print(register_response.text)
