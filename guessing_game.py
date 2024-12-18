import random

animals = { 
    'zebra': ['I have stripes', 'I have 4 letters', 'My sound is neighing'], 
    'horse': ['I am strong and elegant', 'I have 5 letters', 'My sound is neighing'], 
    'cow': ['I give milk', 'I have 3 letters', 'My sound is mooing'], 
    'sheep': ['I am covered in wool', 'I have 5 letters'], 
    'dog': ['I am man\'s best friend', 'I have 3 letters', 'My sound is barking'], 
    'cat': ['I am independent', 'I have 3 letters', 'My sound is meowing'], 
    'parrot': ['I talk a lot', 'I have 6 letters', 'My sound is talking'], 
    'chicken': ['I lay eggs', 'I have 7 letters', 'My sound is clucking'], 
    'duck': ['I love lakes and I\'m noisy', 'I have 4 letters', 'My sound is quacking'], 
    'turkey': ['I am the main dish for Christmas', 'I have 6 letters', 'My sound is gobbling'], 
}

chosen_animal = random.choice(list(animals.keys()))

user_word = []
attempts = 3

print('\nYou have', attempts, 'attempts.\n\nGood luck!')

for _ in range(3):
    while True:
        user_input = input('\nChoose a letter to guess the chosen animal from the list: ').lower().strip()

        # Verifica se a entrada é válida (letras e tamanho correto)
        if not user_input.isalpha():
            print("\nInvalid input! Please enter letters only.")
            continue
        if len(user_input) != len(chosen_animal):
            print(f"\nPlease enter exactly {len(chosen_animal)} letters.")
            continue
        break

    for i in range(len(user_input)):
        if user_input[i] == chosen_animal[i]:
            print('\nThe letter', user_input[i], 'is correct and in the right position.')

        elif user_input[i] in chosen_animal:
            print('\nThe letter', user_input[i], 'is correct but in the wrong position.')
            
            # FIRST HINT
            first_hint = animals[chosen_animal][0]
            print('\nHINT:', first_hint)

        else:
            print('\nThe letter', user_input[i], 'is incorrect.')
            
            if len(animals[chosen_animal]) > 2:
                # SECOND HINT
                second_hint = animals[chosen_animal][1]
                print('\nHINT:', second_hint)

            if len(animals[chosen_animal]) > 3:  
                # THIRD HINT
                third_hint = animals[chosen_animal][2]
                print('\nHINT:', third_hint)

    user_word = list(user_input)

    if ''.join(user_word) == chosen_animal:
        print('\nCongratulations! You guessed the word. The word was:', chosen_animal)
        break
    else:
        attempts -= 1

        if attempts > 0:
            print('\nSorry! You were wrong.\nTry again.')
            print('\nYou still have', attempts, 'attempts left.')
        else:
            print('\nGame over! The correct word was:', chosen_animal)
            break
