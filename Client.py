from dataclasses import dataclass
import requests
from datetime import datetime

DEFAULT_BASE_URL = "http://127.0.0.1:5000/"


@dataclass
class Status:
    status: str
    filename: str
    timestamp: datetime
    explanation: str

    def is_done(self):
        return self.status == 'done'


class WebClient:
    def __init__(self, base_url=DEFAULT_BASE_URL):
        self.base_url = base_url.rstrip('/')

    def upload(self, file_path):
        url = f'{self.base_url}/submit'
        files = {'file': open(file_path, 'rb')}
        response = requests.post(url, files=files)
        response.raise_for_status()
        json_data = response.json()
        uid = json_data.get('uid')
        return uid

    def status(self, uid):
        url = f'{self.base_url}/status/{uid}'
        response = requests.get(url)
        response.raise_for_status()
        json_data = response.json()
        status = json_data.get('status')
        filename = json_data.get('filename')
        timestamp = json_data.get('timestamp')
        explanation = json_data.get('explanation')
        return Status(status, filename, timestamp, explanation)

# import requests
# from datetime import datetime
#
#
# class Status:
#     def __init__(self, status, filename, timestamp, explanation):
#         self.status = status
#         self.filename = filename
#         self.timestamp = datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S')
#         self.explanation = explanation
#
#     def is_done(self):
#         return self.status == 'done'
#
#
# class WebAppClient:
#     def __init__(self, base_url):
#         self.base_url = base_url
#
#     def upload(self, file_path):
#         url = f"{self.base_url}/submit"
#         files = {'file': open(file_path, 'rb')}
#         response = requests.post(url, files=files)
#
#         if response.status_code != 200:
#             raise Exception(f"Upload failed with status code {response.status_code}")
#
#         data = response.json()
#         uid = data['uid']
#         return uid
#
#     def status(self, uid):
#         url = f"{self.base_url}/status"
#         params = {'uid': uid}
#         response = requests.get(url, params=params)
#
#         if response.status_code != 200:
#             raise Exception(f"Status request failed with status code {response.status_code}")
#
#         data = response.json()
#         status = data['status']
#         filename = data['filename']
#         timestamp = data['timestamp']
#         explanation = data['explanation']
#
#         status_obj = Status(status, filename, timestamp, explanation)
#         return status_obj
