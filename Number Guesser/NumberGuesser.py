print("\nThe Number Guesser")

number = 1832 # Enter your number!
high = 10000 # Enter your range!

info_list = []

def numberguesser(number,high):

    guess = int(high/2)
    print(guess, "guess")
    low = 0
    i = 1

    while number != guess: # guess is incorrect
        #print(guess,"guess")
        #print("back in the loop!")
        if number == guess: # guess is correct
            info_list = [guess,i]
            return info_list
        elif number >= guess: # guess is too low
            print(guess, "guess was too low")
            i += 1
            low = guess
            guess = guess + int((high - guess)/2)
            print(guess,"new guess")
            continue # need continue or it will keep going
        elif number <= guess: # guess is too high
            print(guess, "guess was too high")
            i += 1
            high = guess
            guess = guess + int((low - guess)/2)
            print(guess,"new guess")
            continue
        
    if number == guess: # guess is correct         
            info_list = [guess,i]
            return info_list

answer_list = numberguesser(number,high)

print("\nYour Number is:", answer_list[0])
print("This took", answer_list[1], "tries.")




# print("\nYour number is", (numberguesser(number))[0])


#print("This took", (numberguesser(number))[1], "tries.")
