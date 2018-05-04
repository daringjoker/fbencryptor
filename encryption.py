from random import randint

class encryptionHandle:
    tokenSeed=""
    def encrypt(self,message):
        sentence = ""
        for letter in list(message):
            if letter.isdigit:
            if letter == " ":
                word = "."
            elif letter == ".":
                word = "\n"
            else:
                word = self.getwrd(letter, 3)
            sentence = sentence + " " + word
        return sentence


    def getwrd(self,letter,n):
        rword=randint(1,1000)
        wcount= 0
        with open("1.1million word list.txt", 'r') as rfile:
            while(wcount!=rword):
                word=rfile.readline()
                if (len(word)>n+1):
                    if(word[n] == letter):
                        wcount+=1
            return word[:-1]






message=input("enter the message   ")
sentence=encrypt(message)
print(sentence)
print(decrypt(sentence))
