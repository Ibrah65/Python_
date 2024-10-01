def is_palindrome(string):
    cleaned_string = ''.join(char.lower() for char in string if char.isalnum())
    
    return cleaned_string == cleaned_string[::-1]

input_string = input("Enter a word or phrase: ")
if is_palindrome(input_string):
    print(f"'{input_string}' is a palindrome.")
else:
    print(f"'{input_string}' is not a palindrome.")
#Line 2 explains the concept of case-sensitivity an instance could be "Dad" as such would
# not be recognised as palindrome because the string "Dad" isn't the same as "daD" when reversed.