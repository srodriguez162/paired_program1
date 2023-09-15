# Christopher Barragan, Santiago Rodriguez
# String Methods Practice #1
# Print the following text in uppercase, using the specific string method:
# "Especially in electronic communications, writing in all caps is equivalent to yelling."
sentence = "Especially in electronic communications, writing in all caps is equivalent to yelling."

print(sentence.upper())
print("hello")
# String Methods Practice #2
# Join the following list into a string, separating each item with a space. Use the appropriate list/string method, and display the result.
word_list = ["Simple","is","better","than","complex."]
word_list2 = " ".join(word_list)
print(word_list2)
print("hello world")
# String Methods Practice #3
# Replace in the following sentence:
# "If the implementation is hard to explain, it might be a bad idea."
# the following pairs of words:
# "hard" --> "easy"
# "bad" --> "good"
# and display the sentence with both words modified.

sentence2 = "If the implementation is hard to explain, it might be a bad idea."
result = sentence2.replace("hard", "easy")
result2 = result.replace("bad", "good")
print(result2)
#################################string properties################################

# String Properties Practice #1
# Concatenate the text "Repetition" 15 times and display the result on the screen.
# Luckily, you know that strings are multipliable and you can do this activity in a simple and elegant way.
word = "repetition "
print(word * 15)
# String Properties Practice #2
# Check if the word "beach" is not found in the following haiku. You should print the boolean.
# "Whitecaps on the bay:
# A broken signboard banging
# In the April wind."
# — Richard Wright, collected in Haiku: This Other World, 1998
haiku = "Whitecaps on the bay: A broken signboard banging In the April wind. - Richard Wright, collected in Haiku: This Other World, 1998" 
print(haiku.find("beach"))

# String Properties Practice #3
# Check the Python Documentation to find the description of the len() function. Then, display on the screen the length (in number of characters) of the word electroencephalographist.
longWord = "electroencephalographist"
print(len(longWord))