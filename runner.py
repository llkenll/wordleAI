from turtle import pos
from words import get_wordle_guesses, get_wordle_answers,get_wordmaster_answers
import random

def main():
    words = get_wordle_guesses()

    #words = ["brick","drift","primo","arise"]

    greenLetters = ["!"]*5
    yellowLetters = ["!"]*5
    greyLetters = list()
    

    while(True):
        
        print("Enter word")
        inputWord = input()
        print("Enter values of each letter 2 for green, 1 for yellow, 0 for grey")
        inputValue = input()

        for i in range(5):
            if int(inputValue[i]) == 0:
                greyLetters.append(inputWord[i])
        #print(parsedInput[0][1])
        # words = ["reese","like","boobs","apple","abelp", "eager"]
        # words2 = ["reese","like","boobs","apple","abelp","eager"]

        #remove words with grey letter
        need_to_remove = []
        for word in words:
            for letter in greyLetters:
                #print(word + ' '+ letter)
                if letter in word:
                    #print(word + ' '+ letter)
                    #words2.remove(word)
                    need_to_remove.append(word)
                    break
        #print(need_to_remove)

        words = [word for word in words if word not in need_to_remove]
        

        for i in range(5):
            if int(inputValue[i]) == 2:
                greenLetters[i] = inputWord[i]
        
        if len(yellowLetters) != 0:
            for i in range(5):
                if int(inputValue[i]) == 1:
                    yellowLetters[i] = inputWord[i]

        need_to_remove2 = []
        #remove words with letters in the exact position of yellow
        for word in words:
            for i in range(5):
                if yellowLetters[i] != '!':
                    if word[i] == yellowLetters[i]:
                        need_to_remove2.append(word)

        words = [word for word in words if word not in need_to_remove2]
        
        need_to_remove3 = []

        for word in words:
            for i in range(5):
                if greenLetters[i] != "!":
                    if word[i] != greenLetters[i]:
                        need_to_remove3.append(word)

        words = [word for word in words if word not in need_to_remove3]

        #sum of arise
        
        # possibleAnswer = inputWord
        # answerValue = calculateValue(inputWord, greenLetters, yellowLetters)
        possibleAnswer = ""
        answerValue = 0
        #get words by letter and position
        if len(greenLetters) != 0:
            
            for word in words:
                sum = 0
                for i in range(5):
                    if greenLetters[i] != '!':
                        if word[i] == greenLetters[i]:
                            sum+=2

                for letter in yellowLetters:
                    if letter != '!':
                        if letter in word:
                            sum+=1

                if(answerValue < sum ):
                    #print(sum)
                    answerValue = sum
                    possibleAnswer = word
                    eliminateLower(words, answerValue,greenLetters, yellowLetters)
                # elif answerValue == sum:
                #    eliminateLower(words, answerValue,greenLetters, yellowLetters)
                #    possibleAnswer = random.choice(words)
                #    print(possibleAnswer)
                #    answerValue = calculateValue(possibleAnswer, greenLetters, yellowLetters)
                   
        print(words)

        # if(possibleAnswer == ""):
        #    words = get_wordle_guesses()
        #    possibleAnswer = random.choice(words)
        #    answerValue = calculateValue(possibleAnswer, greenLetters, yellowLetters)
        print("Possible Answer is: "+ possibleAnswer)           




    
def eliminateLower(words, value, green, yellow):
    toEliminate = []

    for word in words:
        currentVal = calculateValue(word, green, yellow)
        if currentVal < value:
            toEliminate.append(word)
    
    words = [word for word in words if word not in toEliminate]


def calculateValue(word, greenLetters, yellowLetters):
    sum = 0
    for i in range(5):
        if greenLetters[i] != '!':
            if word[i] == greenLetters[i]:
                sum+=2

    for letter in yellowLetters:
        if letter != '!':
            if letter in word:
                sum+=1

    return sum


if __name__=="__main__":
    main()