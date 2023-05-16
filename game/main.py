import random

options = ['piedra', 'papel', 'tijera']

computer_wins = 0
user_wins = 0

rounds = 1

while True:
    print('*' * 10) 
    print('Round:', rounds)
    print('*' * 10)

    print('Victorias de la maquina: ', computer_wins)
    print('Victorias del usuario: ', user_wins)

    user_input = input('piedra, papel o tijera -> ') 
    user_option = user_input.lower()

    rounds += 1

    if not user_option in options:
        print("Esa opcion no es valida")
        continue
    
    computer_option = random.choice(options)
    print('')
    print('Opcion del usuario ->', user_option)
    print('Opcion de la maquina ->', computer_option)
    print('')

    if user_option == computer_option:
        print('Empate')
    elif user_option == 'piedra':
        if computer_option == 'tijera':
            print('piedra > tijera, Usuario Gano!!!')
            user_wins += 1
        else:
            print('papel > piedra, computadora gana!')
            computer_wins += 1
    elif user_option == 'papel':
        if computer_option == 'piedra':
            print('papel > piedra, Usuario gano!!!')
            user_wins += 1
        else:
            print('tijera > papel, la computadora gano!')
            computer_wins += 1
    elif user_option == 'tijera':
        if computer_option == 'papel':
            print('tijera > papel, Usuario gano!!!')
            user_wins += 1 
        else: 
            print('Piedra > tijera, computadora gana!')
            computer_wins += 1 

    if computer_wins == 2:
        print('El ganador es la computadora')
        break
    elif user_wins == 2:
        print('Gano el usuario!')
        break



