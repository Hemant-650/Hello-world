# Practical 20: Check if string is palindrome
def is_palindrome(s):
 return s == s[::-1]
text = input("Enter string: ")

print("Palindrome:", is_palindrome(text))
print("-*-*-*-*-*-*-*-*")
