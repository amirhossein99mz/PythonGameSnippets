##
#  Check several properties of a string.
#

# Read input from the user.
message = input("Enter a string: ")

# Check each property and display a message if that property is present.
if message.isalpha():
    print("The string contains only letters.")

elif message.isdigit():
    print("The string contains only digits.")

if message.isalpha() and message.isupper():  # isupper() verifies only that all letters ar upeprcase, bbut not that all characters are letters (it ignores non-letter characters). We thus need to verify that all characters are letter (isalpha) and all letters are uppercase (isupper)
    print("The string contains only uppercase letters")

elif message.isalpha() and message.islower():  # islower() verifies only that all letters ar upeprcase, bbut not that all characters are letters (it ignores non-letter characters). We thus need to verify that all characters are letter (isalpha) and all letters are lowercase (islower)
    print("The string contains only lowercase letters")

# In the following we use 'if' rather than 'elif' because these options are not are not necessarily alternative to the previous ones (both can be true at the same time)

if message.isalnum():
    print("The string contains only letters and digits.")

if message[0].isupper():
    print("The string starts with an uppercase letter.")

if message.endswith("."):
    print("The string ends with a period.")

