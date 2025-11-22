import random

list_of_word = ["jesus", "mosiah", "moroni", "alma", "jacob", "helaman", "nephi", "lehi", "mormon", "enos", "omni", "ether"]

secret_word = list_of_word[random.randint(1, len(list_of_word))]

print(secret_word)