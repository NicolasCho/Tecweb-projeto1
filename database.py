import sqlite3
from dataclasses import dataclass

@dataclass
class Note:
    id: int = None
    title: str = None
    content: str = ''

class Database:
    def __init__(self, name):
        self.conn = sqlite3.connect(name+'.db')
        self.conn.execute('CREATE TABLE IF NOT EXISTS note (id INTEGER PRIMARY KEY, title TEXT, content TEXT NOT NULL);')

    def add(self, note):
        self.conn.execute("INSERT INTO note (title,content) VALUES ('{}','{}');".format(note.title,note.content))
        self.conn.commit()

    def get_all(self):
        cursor = self.conn.execute("SELECT id, title, content FROM note")
        
        note_list = []
        for linha in cursor:
            note = Note(id = linha[0], title = linha[1], content = linha[2])
            note_list.append(note)
        return note_list

    def update(self, entry):
        self.conn.execute("UPDATE note SET title = '{}', content = '{}' WHERE id = {};".format(entry.title, entry.content, entry.id))
        self.conn.commit()
    
    def delete(self, note_id):
        self.conn.execute("DELETE FROM note WHERE id = {};".format(note_id))
        self.conn.commit()