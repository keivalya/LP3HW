from sys import argv
script, filename = argv

print(f"We are going to erase {filename}.")
print("If you don't want that, press CTRL-C (^C)")
print("If you do want that, hit RETURN")

input("?")

print("Opening the file...")
target = open(filename,'w')#use 'w' then you’re saying“open this ﬁle in ‘write’mode,”
                            #'r' for “read,” 'a' for “append,”
print("Truncating the file. Goodbye!")
target.truncate()       #something new. "It erases file's content"

print("Now I am going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And finally we close it.")
target.close()
