
# ^ String Methods
data = " File: report.txt"
# ! .strip() - removes whitespaces at the beginning or at the end of the string
print(data.strip())

# ! .startswith() - identifies whether a string starts with a particular value and gives boolean result based on it.
print(data.startswith(" "))

# ! .endswith() - identifies whether a string ends with a particular value and gives boolean result based on it.
print(data.endswith(".txt"))

# ! .find() - finds if the particular value exists in the string, if yes returns it's index else returns -1
print(data.find("friend")) #* -1
print(data.find("txt")) #* 14

a = "A friend in need is a friend indeed"
# ! .replace() - finds if the particular value exists in the string and then replace it with the different value, if value not found it prints the same string
print(a.replace("friend", "brother"))

# ! .split() - splits a string into list
b = 'apple banana mango'
print(b.split())