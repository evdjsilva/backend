secreto = 'helena'
digitadas = []
chances = 3

while True:
  if chances <= 0:
    print('Voce perdeu')
    break
  letra = input('Digite uma letra: ')
  if len(letra) > 1:
    print('Ahh isso nao vale, apenas letras')
    continue
  digitadas.append(letra) 
  if letra in secreto:
    print(f'UHULLL, a letra "{letra}" existe na palavra secreta')
  else:
    print(f'AFFF: a letra "{letra}" não existe na palavra secreta')
    digitadas.pop()
  secreto_temporario = ''  
  for letra_secreta in secreto:
    if letra_secreta in digitadas:
      secreto_temporario += letra_secreta
    else:
      secreto_temporario += '*'
  print(secreto_temporario)
  if secreto_temporario == secreto:
    print(f'Que legal, VOCE GANHOU!! A palavra era {secreto_temporario}')
    break
  else:
    print(f' {secreto_temporario}')
  if letra not in secreto:
    chances  -= 1
  print(f'Voce tem {chances} chances.')
  print()