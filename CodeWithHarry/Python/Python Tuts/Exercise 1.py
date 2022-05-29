"""
Create a Dictionary and take input from the user and return the meaning of the word from the dictionary
"""
dictionary = {"Set": "Well defined collection of objects",
              "Peace": "Tranquility",
              "Hate": "Intense dislike",
              "Love": "Intense like"}

word = input("Please enter a word to get the meaning: ").capitalize()
print(dictionary.get(word, "not able to find the meaning"))
