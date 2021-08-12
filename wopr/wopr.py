from io import StringIO
import re

print(
    """Welcome to your Madlib Game! You will be provided with a series of prompts to enter a word that satisfies the requested word type. After you've answered all the promps, we'll use your words in a special story for you.

Just a reminder:
- adjectives are descriptive words
- names should be a capitalized first name
- nouns are people, places, and things
- plural nouns are more than one of a noun
- verbs are action words
- past tense verbs are actions that took place in the past

Here we go!
"""
)


def read_template(path):
    with open(path) as text:
        contents = text.read()
        stripped_contents = contents.strip()
        return stripped_contents


def parse_template(text):
    new = tuple(re.findall(r"\{(.*?)\}", text))
    length = len(new)
    for i in range(0, length):
        if i == 0:
            print(i)
            new_text = text.replace(new[i], "")
        else:
            new_text = new_text.replace(new[i], "")
    return new_text, new


def user_prompt(words):
    print("Please type a response to the prompt and press [ENTER]")
    responses = []
    for word in words:
        responses.append(input(f"Type (a/an) {word}: "))
    return responses


def merge(strip, res):
    length = len(res)
    for i in range(0, length):
        if i == 0:
            story = strip.replace("{}", res[i], 1)
        else:
            story = story.replace("{}", res[i], 1)
    return story


def output():
    stripped, prompts = parse_template(read_template("assets/game_template.txt"))

    res = user_prompt(prompts)
    f = open("assets/madlib.txt", "w")
    f.write(merge(stripped, res))
    f.close()
    print(merge(stripped, res))


output()


# Following is working code...

# """Mad Libs"""
# """Mad Lib Intro"""

# STORY = "I the %s and %s %s have %s %s's %s sister and plan to steal her %s %s! What are a %s and backpacking %s to do? Before you can help %s, you'll have to collect the %s %s and %s %s that open up the %s worlds connected to A %s Lair. There are %s %s and %s %s in the game, along with hundreds of other goodies for you to find."

# print(
#     """Welcome to this Madlib story. You will be provided with a series of prompts to enter a word that satisfies the requested word type. After you've answered all the promps, we'll use your words in a special story for you.

# Just a reminder:
# - adjectives are descriptive words
# - names should be a capitalized first name
# - nouns are people, places, and things
# - plural nouns are more than one of a noun
# - verbs are action words
# - past tense verbs are actions that took place in the past

# Here we go!
# """
# )
# print()

# adjective1 = input("Write an adjective: ")
# adjective2 = input("Write an adjective: ")
# fName1 = input("Enter a first name: ")
# pastTenseVerb = input("Input a verb: ")
# fName2 = input("Enter a first name: ")
# adjective3 = input("Write an adjective: ")
# adjective4 = input("Write an adjective: ")
# pluralNoun1 = input("Input a plural noun: ")
# largeAnimal = input("A large animial: ")
# smallAnimal = input("A small animial: ")
# girlName = input("Enter a girl's name: ")
# adjective5 = input("Write an adjective: ")
# pluralNoun2 = input("Input a plural noun: ")
# adjective6 = input("Write an adjective: ")
# pluralNoun3 = input("Input a plural noun: ")
# number50 = input("Input a number between 1 and 50: ")
# fName3 = input("Enter a first name: ")
# number1 = input("Input a number: ")
# pluralNoun4 = input("Input a plural noun: ")
# number2 = input("Input a number: ")
# pluralNoun5 = input("Input a plural noun: ")

# print()
# print(
#     STORY
#     % (
#         adjective1,
#         adjective2,
#         fName1,
#         pastTenseVerb,
#         fName2,
#         adjective1,
#         adjective2,
#         pluralNoun1,
#         largeAnimal,
#         smallAnimal,
#         girlName,
#         adjective3,
#         pluralNoun2,
#         adjective4,
#         pluralNoun3,
#         number50,
#         fName3,
#         number1,
#         pluralNoun4,
#         number2,
#         pluralNoun5,
#     )
# )