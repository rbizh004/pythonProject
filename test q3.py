path= r'C:\Users\zheka\PycharmProjects\pythonProject\my_text.txt'

with open(path) as f:
    lines=[x.strip() for x in f]
    lines=[x.replace(" ", " ").replace("\t", " ").replace("\n", " ") for x in lines]
print(lines)