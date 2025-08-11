# import modules
import emoji

# Prompt the user for emojize
emojize = input("Input: ")

print("Output: ", emoji.emojize(emojize, language='alias'))
