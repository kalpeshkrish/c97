str1=input("enter your introduction")
print(str1)
characterCount=0
wordCount=0

for i in str1:
    characterCount=characterCount+1

    if (i==' '):
        wordCount=wordCount+1

    
print (characterCount)
print (wordCount)
