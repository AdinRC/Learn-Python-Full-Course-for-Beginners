
secret_word = "maulana"
guess = ""
guess_count = 0
guess_limit = 3
out_of_quesses = False

while guess != secret_word and not(out_of_quesses):
    if guess_count < guess_limit:
        guess = input("Enter guess: ")
        guess_count += 1
    else:
        out_of_quesses = True
        
if out_of_quesses:
    print ("Out of Guesses, You Lose   ") 
else:
    print("You win")