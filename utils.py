from models import Pessoas

def insere():
    pessoa = Pessoas(nome='Araujo', idade=59)
    print(pessoa)
    pessoa.save()

def consulta():
    pessoas = Pessoas.query.all()
    print(pessoas)
    pessoa = Pessoas.query.filter_by(nome='Modesto').first()
    print(pessoa.idade)

def altera():
    pessoa =Pessoas.query.filter_by(nome='Araujo').first()
    pessoa.nome = 'Carlos'
    pessoa.save()

def exclui():
    pessoa = Pessoas.query.filter_by(nome='Araujo').first()
    pessoa.delete()

if __name__ == '__main__':
   # insere()
   #altera()
   exclui()
   consulta()
   