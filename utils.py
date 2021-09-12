from pathlib import Path
import json
from database import Database, Note


def extract_route(request):
    #splitted_request = request.split()
    #route = splitted_request[1]
    #route = route[1:]
    #return ''
    #return route
    return request[request.index('/')+1 : request.index('HTTP')-1]
    #return request.split()[1][1:]

def read_file(path):
    extension_list = ['.txt', '.html', '.css', '.js']
    extension = path.suffix 

    if extension in extension_list:
        with open(path,'r') as f:
            text = f.read().encode(encoding='utf-8')
            return text
    else:
        with open(path,'rb') as f:
            text = f.read()
            return text

def load_data():
    db = Database('notes')

    return db.get_all()

def load_template(template):
    filename = Path('templates') / template
    with open(filename,'r') as f:
        text = f.read()
    return text

def add_data(new_note):
    db = Database('notes')
    db.add(new_note)

def update_data(note):
    db = Database('notes')
    db.update(note)

def build_response(body='', code=200, reason='OK', headers=''):
    if headers == '':
        response = 'HTTP/1.1 ' + str(code) + ' ' + reason + '\n\n' + body
    else:
        response = 'HTTP/1.1 ' + str(code) + ' ' + reason + '\n' + headers +'\n\n' + body
    return response.encode(encoding='utf-8')

