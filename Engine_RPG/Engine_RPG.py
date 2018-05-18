#Nome:MelDol
#Versão 1.0.0
#Autor: SMR101
#Descrição: Simples Motor de Jogos com grafico de texto
class Inimigos(object): #Inimgigos do Jogo
    def orc(vida,ataque): # Vida,Ataque
             vida = vida
       	     ataque = ataque
             orc = "Orc Surgiu Vida: {0} Ataque: {1} ".format(vida,ataque)
             return orc
    def Bandido(vida,ataque): #Variaveis do Inimigo
             vida = vida
             ataque = ataque
             bandido = "Bandido Surgiu Vida: {0}  Ataque: {1} ".format(vida,ataque)
             return bandido
    def Globin(vida,ataque):
             vida = vida
             ataque = ataque
             globin = "Globin Surgiu Vida: {0}  Ataque: {1} ".format(vida,ataque)
             return globin
    def Esqueleto(vida,ataque):
             vida = vida
             ataque = ataque
             esqueleto = "Esqueleto Surgiu Vida: {0}  Ataque: {1} ".format(vida,ataque)
             return esqueleto
class Heroi(object):  #Personagem do Jogo
    def Personagem(nome,vida,forca,car,inte,moedas): #Atributos do Personagem Nome,Vida,Força,Carisma,Inteligencia,Moedas
             nome = nome
             vida = vida
             forca = forca
             car =  car
             inte = inte
             moedas = moedas
             Personagem = "Nome: {0} Vida: {1} Carisma: {2} Inteligencia: {3} Força: {4} Moedas: {5} ".format(nome,vida,car,inte,forca,moedas)
             return Personagem
class Itens(object): #Itens do Jogo
    def Adaga(dano,preco): # Atributos do Objeto Adaga Dano,Preço
        dano = dano
        preco = preco
        return "Adaga Preço: {0} Dano: {1}".format(preco,dano)
    def Espada(dano,preco):
        dano = dano
        preco = preco
        return "Espada Preço: {0} Dano: {1}".format(preco,dano)
    def Lanca(dano,preco):
        dano = dano
        preco = preco
        return "Lança Preço: {0} Dano: {1}".format(preco,dano)
    def Arco(dano,preco):
        dano = dano
        preco = preco
        return "Arco Preço: {0} Dano: {1}".format(preco,dano)
 
#Teste das Funções

