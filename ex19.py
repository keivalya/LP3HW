def dogs_and_cats(dog_count, cat_count):
    print(f"You have {dog_count} dogs!")
    print(f"You have {cat_count} cats!")
    print(f"Man that's enough for a party!")
    print("Get a blanket.\n")

print("We can just give the functions number directly: ")
dogs_and_cats(30, 20)

print("OR, we can use variables from our script: ")
no_of_dogs = 25
no_of_cats = 15

dogs_and_cats(no_of_dogs, no_of_cats)

print("We can even do math inside too: ")
dogs_and_cats(10+30, 10+20)

print("And we can combine the two, variables and math: ")
dogs_and_cats(no_of_dogs + 100, no_of_cats + 200)
