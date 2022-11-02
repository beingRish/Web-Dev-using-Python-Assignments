# 3. Write a Python script to read the above created file ‘myfile.txt’ and display content on the console.

with open('myfile.txt', 'r') as f:
    content = f.read()
    print(content)
