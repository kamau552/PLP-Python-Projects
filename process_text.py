#Read contents of input.txt
with open("input.txt", "r") as file:
    contents = file.read()
    
#count the number of words
word_count = len(contents.split())

#convert all text to uppercase
uppercase_text = contents.upper()

with open("öutput.txt", "w") as file:
    file.write(uppercase_text)
    file.write("\n\n") #space
    file.write(f"Word Count: {word_count}\n")
    
#print message
print("Successfully created output.txt with processed text and word count")