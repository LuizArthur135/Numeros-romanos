# Codigo feito por Marcelo

decimais=[1000,900,500,400,100,90,50,40,10,9,5,4,1]
dict={1:"I",4:"IV",5:"V",9:"IX",10:"X",40:"XL",50:"L",90:"XC",100:"C",400:"CD",500:"D",900:"CM",1000:"M"}
result=[]


def decimal_to_roman(numero):
	for i in range(0,len(decimais)):
		if numero in decimais:
			numero_romano=dict[numero]
			resto=0
			break
		if numero>decimais[i]:
			quociente=numero//decimais[i] # Inteiro da divisão
			resto=numero%decimais[i] # Resto da divisão
			numero_romano=dict[decimais[i]]*quociente # Repete o numero romano de acordo com o inteiro da divisão  
			break
	result.append(numero_romano)
	if resto==0:
		pass
	else:
		decimal_to_roman(resto)
	return "".join(result)

print(f'Aqui esta o número em romano: {decimal_to_roman(333)}')