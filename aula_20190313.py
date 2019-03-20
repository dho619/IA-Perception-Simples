def soma(amostra,peso):
	v_total = 0
	for i,p in enumerate(peso):
		v_total += p * amostra[i]
	return v_total

def ativacao(valor):
	if valor >= 0:
		return 1
	else:
		return 0

def erro(amostra, v_saida):
	return amostra[-1] - v_saida

def correcao(tx, erro, peso, v_entrada):
    for i,p in enumerate(peso):
        peso[i] = p+(tx*erro*v_entrada[i])

    return peso
"""			  0	    1
			Animal	  Planta

1- Faz Fotossintese?	0	  1
2- Eh carnivaro?	1	  0
3- Eh herbivaro?	1	  0
4- Tem raiz?		0	  1
5- Tem patas?		1  	  0
6- Tem frutos?		0	  1
7- Tem folhas?		0	  1
8- Respira?		1	  1
"""

ds = [	#b 1 2 3 4 5 6 7 8 s
	[1,0,1,0,0,1,0,0,1,0], #Cachorro
	[1,0,0,1,0,1,0,0,1,0], #Cavalo
	[1,1,0,0,1,0,0,1,1,1], #Rosa
	[1,1,0,0,1,0,1,1,1,1], #Mangueira
	[1,0,1,0,0,1,0,0,1,0], #Gato
	[1,1,0,0,1,0,0,1,1,1], #Eucalipto
	[1,1,0,0,1,0,0,1,1,1], #Bananeira
	[1,1,1,0,1,0,0,1,1,1], #Dioneia
	[1,0,1,0,0,0,0,0,1,0], #Cobra
	[1,0,1,0,0,1,0,0,1,0]  #Tartaruga
	]
    #b  1  2 3 4  5  6  7  8
w = [1,0.5,1,1,1,0.5,1,0.5,1]
tx = 0.5
count = 0

while True:
    f_ok = 0
    count += 1
    print("Rodada {}: \n".format(count))
    print("Pesos sao: ", w)
    for a in ds:
        v_soma = soma(a,w)
        v_saida = ativacao(v_soma)
        v_erro = erro(a,v_saida)

        if v_erro != 0:
            w = correcao(tx, v_erro, w, a)
            f_ok += 1
	
    if f_ok == 0:
        break

print("Rede treinada!")

print("Pesos sao: ", w)
