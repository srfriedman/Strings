#String List Experiment
#Sarah Friedman
#9/8/17

string = ['Mississippi', 'Bookkeeper', 'Deeded', 'I love spom!  Spom is my favorite food.  Spom, spom, spom, yum']
stringCount = len(string)

replaceChar = ['i', 'e', 'e', 'om']

replaceWith = ['I', 'A', 'q', 'am']

x = 0

def replace(s, old, new):
    newStr = s.replace(old, new)
    print(newStr)

for i in range(stringCount):
    replace(string[x], replace[x], replaceWith[x])
    x = x+1
