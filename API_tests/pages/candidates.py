import requests
import json

from config import url


class Candidate(object):

    def __init__(self):
        self.url = url + 'candidates'

    @property
    def get_list(self):
        return requests.get(self.url)

    def get_by_id(self, url_id):
        return requests.get(self.url+'/'+str(url_id))

    def post(self, name, position, headers={'content-type': 'application/json'}):
        data = {"name": name, "position": position}
        return requests.post(self.url, data=json.dumps(data), headers=headers)

    def delete_by_id(self, url_id):
        return requests.delete(self.url+'/'+str(url_id))

if __name__ == "__main__":
    Candidate()
