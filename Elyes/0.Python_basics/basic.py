# First, create a function that concat two strings. (Just for the train)

def littleSpeech(firstWord: str, secondWord: str):
    return firstWord + secondWord

assert(littleSpeech("Hello", " World !") == "Hello World !"), "I guess he isn't alive."
# Then, count the number of characters (character frequency) in a string.

def characterFrequency(sentences: str):
    d = {}
    for i in range(len(sentences)):
        if sentences[i] in d:
            d[sentences[i]] += 1
        else:
            d[sentences[i]] = 1
    return d

characterFrequency("If you ignore both your program and yourself, you will only count your battles by your defeats. ~ Rob Tzu")

assert(characterFrequency("If you ignore both your program and yourself, you will only count your battles by your defeats. ~ Rob Tzu") == \
    {' ': 19, 'o': 12, 'y': 8, 'u': 8, 'r': 7, 'e': 5, 't': 5, 'l': 5, 'n': 4, 'b': 4, 'a': 4, 'f': 3, 's': 3, 'i': 2, 'g': 2, 'd': 2, 'I': 1,\
        'h': 1, 'p': 1, 'm': 1, ',': 1, 'w': 1, 'c': 1, '.': 1, '~': 1, 'R': 1, 'T': 1, 'z': 1}), "As this one is."
# Now the hardest task.
# Write a program that create all possible strings by using a list of letter.
# They must be returned after the operation.

def passwordMaker(letters: str):
    import itertools
    return [''.join(i) for i in list(itertools.permutations(list(letters)))]

assert("robot" in passwordMaker("tboor")), "This isn't the good password >:("


#########################2

from hashlib import blake2b

def databaseLock():
    pmFrequencies = characterFrequency("The one who excels at solving difficulties does so before they arise. ~ Rob tzu")
    letters = []

    for key, value in pmFrequencies.items():
        if value >= 4:
            letters.append(key)

    for i in passwordMaker(letters):
        if blake2b(i.encode('UTF-8')).hexdigest() == "78f1ce059586050456dfcdb88a5da760b39ad9a06f24c9bc7268830d67b9a4b65b55bd0b5ace4e8636f1de59cbb58b1fb8989fb044ba4fa4d5cd325cf5e0d7fd":
            print("Good job ! The password is '" + i + "'.")
            return

    print("Next time buddy.")

# If you succeeded, great job, you serve our society for the greatest.
databaseLock()


#########################3

def myHandmadeDivisor(nb1, nb2):
    try:
        result = nb1 / nb2
        print(result)
    except ZeroDivisionError as e:
        print(e)
    finally:
        print("program finished\n")

myHandmadeDivisor(44, 24)
myHandmadeDivisor(44, 0) # Error

###################4

def dictCounter(d1: dict, d2: dict):
    d= {}
    for i in d1.keys():
        print(i)
        d[i] = d1[i]
    for i in d2.keys():
        if i in d:
            d[i] += d2[i]
        else:
            d[i] = d2[i]
    return d

assert(dictCounter({'a': 200, 'b': 100, 'd': 100}, {'a': 150, 'c': 100, 'e': 300, 'b': 100}) ==\
{'a': 350, 'b': 200, 'c': 100, 'd': 100, 'e': 300})
print("Good job ! We don't have to count letters anymore.")