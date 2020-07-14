'''if 2 > 4:
  print('Hello, Django girls!')
else:  
    print('Hello, Django girls 2!')

print('*'*22)

nome = 'Roberta'
if nome == 'Sarita':
    print('Olá Sarita')
elif nome == 'Ana':
    print('Olá Ana')
else:
    print('Olá Roberta')


volume = 18
if volume < 20: 
    print("Está um pouco baixo")
elif 20 <= volume < 40: 
    print("Está bom para música ambiente")
elif 40 <= volume < 60: 
    print("Perfeito, posso ouvir todos os detalhes")
elif 60 <= volume < 80: 
    print("Ótimo para festas!")
elif 80 <= volume < 100: 
    print("Está muito alto!")
else: 
    print("Meus ouvidos doem! :(")

#Mudar o volume se estiver muito alto ou muito baixo
if volume < 20 or volume > 80:
   
    print('Bem melhor agora!')'''

def saudacao(name):
    print('Olá, '+ name +'!')
    
#laços
garotas = ['Geovana', 'Débora', 'Camila', 'Isabelle', 'Roberta']
for name in garotas:
    saudacao(name)
    print('Próxima')