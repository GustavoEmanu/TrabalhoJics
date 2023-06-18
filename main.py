#2 Informática Vespertino 
#Alunos: Beatriz Carvalho; Gustavo Emanuel Pereira Prestes; Maria Eduarda de Sá Coreas; Yuri kelwin da Silva Ramalho 
#iniciar_sistema
from inicio import *
from cadastrar import *
import os
import time
import itertools
import random

###Yuri

opcao = 0

while opcao != 2:
  exibir_tela_inicial()
  opcao = int(input("Selecione uma opção: "))

  if opcao == 1:
    time.sleep(2)
    os.system('cls')
    iniciar_jogo()
    time.sleep(2)
    os.system('cls')
    break

  elif opcao == 2:
    print("Saindo...")
    exit()
  else:
    print("Opção inválida. Por favor, selecione novamente.")
#iniciar_sistema

#ano, curso, turno
jogador = []
#Criar uma lista gerla para armazenar todas as turmas para o seteamento e o chaveamento
turmas_cadastradas = int(input('Quantas turmas serão cadastradas?'))
os.system('cls')

turmas = []

for x in range(turmas_cadastradas):
  print("\nCadastrar turmas de handebol:\n")
  ano = int(input("Digite o ano da turma: "))
  curso = input("Digite o curso da turma: ").upper()
  turno = input("Digite o turno da turma: ").upper()
  Turma1 = Turma(ano, curso, turno)
  os.system('cls')
  turmas.append(Turma1)

  print(f"DADOS DA TURMA {x+1}°")
  Turma.exibir_informacoes(Turma1)
  time.sleep(2)
  os.system('cls')

###Yuri

  print("Cadastrar equipes do handebol:\n")

###Gustavo

  qtnd_alunos = int(input("Quantos alunos serão cadastrados?"))
  os.system('cls')

  for x in range(qtnd_alunos):
    print(f"ALUNO {x+1}°\n")
    nome = input("Digite o nome do aluno: ").upper()
    idade = int(input("Digite a idade do aluno: "))
    matricula = int(input("Digite a matricula do aluno: "))
    sexo = input("Digite o sexo do aluno: ").upper()
    os.system('cls')

    jogadores = Alunos(ano, curso, turno, nome, idade, matricula,
                                    sexo)
    jogador.append(jogadores)

  os.system('cls')

print("DADOS DAS EQUIPES:\n")
for jogadores in jogador:
  jogadores.exibir_aluno()
  print()
  print()

###Gustavo

time.sleep(1)
os.system('cls')
print("DADOS DE TODAS AS TURMAS:\n")
for Turma1 in turmas:
  Turma1.exibir_informacoes()
  print()
time.sleep(1)
os.system('cls')

"""random.shuffle(turmas)

# Gerar chaves de jogos
chaves = []
for i in range(0, len(turmas), 2):
  turma1 = turmas[i]
  if i + 1 < len(turmas):
    turma2 = turmas[i + 1]
    chaves.append((turma1, turma2))
  else:
    chaves.append((turma1, ))

print("CHAVES DE JOGOS:\n")
for i, chave in enumerate(chaves):
  print(f"Chave {i+1}:")
  for turma in chave:
    turma.exibir_informacoes()
  print()
"""