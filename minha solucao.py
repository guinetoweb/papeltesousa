
#minha resposta de fazer
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

numero = int(input("escolha \n 0.pedra \n 1.papel \n 2.tesoura "))

randomN= random.randint(0,2)

if numero ==0 and randomN==1:
    print(rock)
    print(paper)
    print("Voce venceu pedra x papel")
elif numero==1 and randomN==2:
    print(paper)
    print(scissors)
    print("Voce perdeu papel x tesoura")
elif numero ==2 and randomN==0:
    print(scissors)
    print(rock)
    print("voce perdeu tesoura x pedra")
elif numero==1 and random==0:
    print(paper)
    print(rock)
    print("voce ganhou papel x tesoura")
elif numero ==2 and randomN==1:
    print(scissors)
    print(paper)
    print("voce ganhou tesoura x papel ")
elif numero ==0 and randomN==2:
    print(rock)
    print(scissors)
    print("voce perdeu pedra x tesoura")
else:
    print("deu empate")