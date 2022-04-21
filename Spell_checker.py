from textblob import TextBlob
myList=["Incorect","manago"]
correctredList=[]
for word in myList:
    correctredList.append(TextBlob(word))
print("Corrected words are = ")
for word in correctredList:
    print(word.correct(), end=" , ")