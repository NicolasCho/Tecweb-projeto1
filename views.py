from utils import load_data, load_template, add_data, build_response
import urllib.parse
from database import Database, Note

def index(request):
    # A string de request sempre começa com o tipo da requisição (ex: GET, POST)
    if request.startswith('POST'):
        
        request = request.replace('\r', '')  # Remove caracteres indesejados
        # Cabeçalho e corpo estão sempre separados por duas quebras de linha
        partes = request.split('\n\n')
        corpo = partes[1]
        params = {}
        # Preencha o dicionário params com as informações do corpo da requisição
        # O dicionário conterá dois valores, o título e a descrição.
        # Posteriormente pode ser interessante criar uma função que recebe a
        # requisição e devolve os parâmetros para desacoplar esta lógica.
        # Dica: use o método split da string e a função unquote_plus
        for chave_valor in corpo.split('&'):
            # AQUI É COM VOCÊ
            separado = chave_valor.split('=')
            chave = separado[0]
            valor = urllib.parse.unquote_plus(separado[1])

            params[chave] = valor
        
        note = Note(title=params['titulo'], content=params['detalhes'])
        
        # ADICIONANDO A NOTA NO BANCO DE DADOS
        add_data(note)

        return build_response(code=303, reason='See Other', headers='Location: /')
    
    else:
        note_template = load_template('components/note.html')
        db_notes = load_data()
        notes_li = [
            note_template.format(id = dados.id, title = dados.title, details = dados.content)
            for dados in db_notes
        ]
        notes = '\n'.join(notes_li)

        corpo = load_template('index.html').format(notes=notes)
        return build_response(body=corpo) 
    