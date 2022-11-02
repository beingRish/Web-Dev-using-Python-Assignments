# 7. Write a python script to determine whether a string contains a specific substring.
s = input("Enter a string:")
ss = input("Enter a substring:")
if s.index(ss):
    print("Yes, The String contains that Substring at", s.index(ss))
else:
    print("No, The String does not contain that Substring.")
