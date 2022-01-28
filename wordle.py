from random_word import RandomWords

def grab_soln(length):
    r = RandomWords()

    # Return a single random word
    soln = r.get_random_word(hasDictionaryDef="true",minLength=length, maxLength=length, minCorpusCount=10000)
    while (soln[0].isupper() or (not soln.isalpha())):
        soln = r.get_random_word(hasDictionaryDef="true",minLength=length, maxLength=length, minCorpusCount=10000)

    return soln

def print_results(guess, results):
    # TO DO: make this prettier
    for letter in guess:
        print("{0} ".format(letter),end='')
    print()
    for result in results:
        print("{0} ".format(result),end='')
    print()

def main():
    # TO DO: let user choose length of word
    length = int(input("enter length of word: "))
    # grab a random 5 letter word
    soln = grab_soln(length)

    for i in range(0,5):
        # ask user for guess
        guess = input("enter guess #{0}: ".format(i+1))
        # TO DO: validate guess (length, actual word)

        # iterate through guess, tracking results (yes=2, no=0, close=1)
        results = [0] * length
        for i in range(0,length):
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

    print("YOU LOST - THE SOLUTION WAS {0}".format(soln))

if __name__ == "__main__":
    main()
