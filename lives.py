""""
https://www.youtube.com/watch?v=9LQjZ3aGCuI&ab_channel=Prof.T%C3%A1ssioGon%C3%A7alves


Implemente um TAD – Tipo Abstrato de Dados (VETOR DE REGISTROS ou LISTA ENCADEADA SIMPLES) 
denominado LIVE, com os seguintes campos: título, data, hora, plataforma
 (Youtube, Instagram, etc), apresentador, artista. Para a estrutura criada, implemente as 
 seguintes operações:
a) Cadastrar uma nova LIVE, com todos os campos;
b) Pesquisar uma determinada LIVE pelo campo artista**;
c) Exibir todos os dados das LIVES cadastradas;
d) fazer um programa (em C/++ ou Python) para testar o seu TAD

"""


class live:
    titulo = ""
    data = ""
    hora = ""
    plataforma = ""
    apresentador = ""
    artista = ""

def novaLive():
    nl = live()
    nl.titulo=input("Digite o novo titulo")
    nl.data=input("Digite o novo titulo")
    nl.hora=input("Digite o novo titulo")
    nl.plataforma=input("Digite o novo titulo")
    nl.apresentador=input("Digite o novo titulo")
    nl.artista=input("Digite o novo titulo")
    return nl

def exibir(nl):
    dados = "\n "
    dados+= nl.titulo
    dados = "\n "
    dados+= nl.data
    dados = "\n "
    dados+= nl.hora
    dados = "\n "
    dados+= nl.plataforma
    dados = "\n "
    dados+= nl.apresentador
    dados = "\n "
    dados+= nl.artista
    dados = "\n "
    return dados

def procurarLivePorArtista(nl, artista):
    return nl
