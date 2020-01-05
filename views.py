import requests
import re
from flask_restful import Resource, Api
from bs4 import BeautifulSoup


class Questions(Resource):
    def get(self):
        source = requests.get('https://smgis-kpi.blogspot.com/2020/01/the-list-of-questions-for-exam-on.html').text

        soup = BeautifulSoup(source, 'html')
        _main_class = soup.find('div', class_='post-body entry-content float-container')
        _content_ul = _main_class.find('ul')
        _data = _content_ul.find_all('li')
        res_data = []

        for el in _data:
            new_elem = {}
            cleaner = re.compile(r'</?li>')
            clean_string = re.sub(cleaner, '', str(el))
            new_elem['description'] = clean_string

            mapping = [('Provide ', ''), ('Compare ', ''), ('Describe ', ''), (' ', '+')]
            for k, v in mapping:
                 search_string = clean_string.replace(k, v)
            new_elem['search_name'] = search_string
            res_data.append(new_elem)

        json_view = self.get_json_view(res_data)
        return json_view

    @staticmethod
    def get_json_view(_data):
        res = {}
        for index, data in enumerate(_data):
            link = 'https://www.google.com/search?q={}'.format(data['search_name'])
            description = data['description']
            res[index] = [link, description]
        return res


class StartView(Resource):

    def get(self):
        return {'here': 'test'}

    def post(self):
        return {'hi': 'you have sent post method'}

    def put(self):
        return {'hello': 'you have sent put method'}


