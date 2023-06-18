import time


class Turma:
  #criando a classe
  def __init__(self, ano, curso, turno):
    #criando o construtor da classe
    self.ano = ano
    self.curso = curso
    self.turno = turno

  
  def exibir_informacoes(self):
    atributos = ('\n', f"{'Ano:':<20}", f"{str(self.ano):>15}", '\n',
                 f"{'Curso:':<20}", f"{str(self.curso):>15}", '\n',
                 f"{'Turno:':<20}", f"{str(self.turno):>15}",)
    for ch in atributos:
      time.sleep(0.1)
      print(ch, end='', flush=True)
        
class Pessoa:
  def __init__(self, nome, idade):
    self.nome = nome
    self.idade = idade

  def exibir_pessoa(self):
    atributos = ('\n', f"{'Nome:':<20}", f"{str(self.nome):>15}", '\n',
                 f"{'Idade:':<20}", f"{str(self.idade):>15}",)
    for ch in atributos:
      time.sleep(0.1)
      print(ch, end='', flush=True)

class Professor(Pessoa):
  def __init__(self, nome, idade, identificacao):
    super().__init__(nome, idade)
    self.identificacao = identificacao


  def exibir_professor(self):
    super().exibir_pessoa()
    atributos = ('\n', f"{'Idenficação:':<20}", f"{str(self.identificacao):>15}", '\n')
    for ch in atributos:
      time.sleep(0.1)
      print(ch, end='', flush=True)

class Lider(Pessoa):
  pass
  def exibir_pessoa(self):
    return super().exibir_pessoa()

class Alunos(Pessoa):
  def __init__(self, ano, curso, turno, nome, idade, matricula, sexo):
    #reaproveitando os atributos da classe
    super().__init__(nome,idade)
    self.matricula = matricula
    self.sexo = sexo
    #relacionamento com o objeto turma
    self.turma = Turma (ano,curso,turno)
  

  def exibir_aluno(self):
    self.turma.exibir_informacoes()
    super().exibir_pessoa()
    atributos = (
      '\n',
      f"{'Matricula:':<20}",
      f"{str(self.matricula):>15}",
      '\n',
      f"{'Sexo:':<20}",
      f"{str(self.sexo):>15}",
    )
    for ch in atributos:
      time.sleep(0.1)
      print(ch, end='', flush=True)
