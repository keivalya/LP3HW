from sys import argv
# Lines 1–3 use argv to get a ﬁlename
script, filename= argv

txt = open(filename)    #use a new command, open

print(f"Here's your file {filename}:") #prints a little message
print(txt.read())      #call a function on 'txt' named read
#it says “Hey txt! Do your read command with no parameters!”

print("Type the file's name: ")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())
