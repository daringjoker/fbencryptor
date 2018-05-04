

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
