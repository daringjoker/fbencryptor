from random import randint

class encryptionHandle:
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


class decryptionHandle:
    def decrypt(self,message):
        realmsg=""
        for word in message.lstrip(" ").split(" "):
            if word=="." : letter=" "
            elif word=="\n": letter=". "
            else :letter=self.getletter(word,3)
            realmsg=realmsg+letter
        return realmsg

    def getletter(self,word,n):
        return word[n]





message=input("enter the message   ")
sentence=encrypt(message)
print(sentence)
print(decrypt(sentence))