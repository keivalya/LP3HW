from sys import argv
# read WYSS section for how to run this
script, first, second, third = argv

print("The script is called:", script)
print("The first variable is:", first)
print("The second variable is:", second)
print("The third variable is:", third)


# What you should see
# WARNING! Pay attention! You have been running python scripts without command line
# arguments. If you type only python3.6 ex13.py you are doing it wrong! Pay close
# attention to how I run it. This applies any time you see argv being used.
