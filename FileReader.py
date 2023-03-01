file = open('file.txt','r')
dict = {}
UserFile = file.read()
Wordlist = UserFile.split()

for word in Wordlist:
    dict[word] = dict.get(word,0)+1
print(dict) 
   