# using the code from the code challenge
with open ("input.txt", "r") as file:
    lines = file.readlines()
    
#i'll add nnew line of numbers
modified_lines = []
for i, line in enumerate(lines, start=1):
    modified_lines.append(f"{1}: {line.strip()}\n")
    
#write modified text to output
with open("output.txt", "w") as file:
    file.writelines(modified_lines)
print("successfully created output.txt with line numbers")


#ERROR HANDLING
filename = input("Enter the filename you would want opened: ")

try: 
    with open(filename, "r") as file:
        contents = file.read()
    print("file contents:")
    print(contents)
    
except FileNotFoundError:
    print("Ërror: File not found. Please check the filename and try again.")
except PermissionError:
    print("Error: You don’t have permission to read this file.")
except Exception as e:
    print(f" An unexpected error occurred: {e}")