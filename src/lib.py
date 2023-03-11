import os
import requests
from dotenv import load_dotenv
load_dotenv()

def get_ip_info(addr):
    api_key = os.environ.get('API_KEY')
    url = f"http://api.ipstack.com/{ addr }?access_key={ api_key }"

    data = requests.get(url)
    print(data.content)