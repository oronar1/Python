# w - writes and erases existing contents
with open("haiku.txt", "w") as file:
    file.write("Here's one more haiku\n")
    file.write("What about the older one?\n")
    file.write("Let's go check it out")

# a - appends to end, preserving original contents
NO CONTROL OVER CURSOR
with open("haiku.txt", "a") as file:
	file.seek(0)
	file.write(":)\n")

# r+ read and write
with open("haiku.txt", "r+") as file:
	file.write(":)")
	file.seek(10)
	file.write(":(")

# r+ will not create a file if it doesn't exist
with open("hello.txt", "a") as file:
	file.write("HELLO!!!")



def statistics(file_for_stk):
    """getting statistics of fie:num of lines, num of words, num of chars """
    with open(file_for_stk,"r") as file:
        lines=file.readlines()
        
            return { "lines": len(lines),
                     "words": sum(len(line.split(" ")) for line in lines),
                    "characters": sum(len(line) for line in lines)
                    
def find_and_replace(text,word,new_word):
    """finding and replacing a word in text """
    with open(text,"r+") as file:
        text=file.read()
        new_text=text.replace(word,new_word)
        file.seek(0)
        file.write(new_text)
        file.truncate()                    