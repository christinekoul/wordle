from random_word import RandomWords

def grab_soln():
    r = RandomWords()

    # Return a single random word
    soln = r.get_random_word(hasDictionaryDef="true",minLength=5, maxLength=5, minCorpusCount=10000)
    while (soln[0].isupper() or (not soln.isalpha())):
        soln = r.get_random_word(hasDictionaryDef="true",minLength=5, maxLength=5, minCorpusCount=10000)

    return soln

def print_results(guess, results):
    # TO DO: make this prettier
    for i in range(0,5):
        print("{0} ".format(guess[i]),end='')
    print()
    for i in range(0,5):
        print("{0} ".format(results[i]),end='')
    print()

def main():
    # TO DO: let user choose length of word
    # grab a random 5 letter word
    soln = grab_soln()

    for i in range(0,6):
        # ask user for guess
        guess = input("enter guess #{0}: ".format(i+1))
        # TO DO: validate guess (length, actual word)

        # iterate through guess, tracking results (yes=2, no=0, close=1)
        results = [0,0,0,0,0]
        for i in range(0,5):
            if (guess[i] == soln[i]):
                results[i] = 2
            elif (guess[i] in soln):
                # TO DO: make this more accurate for repeated letters
                results[i] = 1
        # print results
        print_results(guess, results)

        if (not (0 in results or 1 in results)):
            print("YOU WON - CONGRATULATIONS!")
            return

    print("YOU LOST :(")

if __name__ == "__main__":
    main()
