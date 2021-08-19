MyName="Ashmita"
print(MyName)
#string datatype

grade= 8
print(grade)
#integer datatype

weight= 47.9
print(weight)
#float datatype

myFriends=["Anushka","Chaitali","Aditi"]
print(myFriends)
#list datatype

print(type(MyName))
print(type(grade))
print(type(weight))
print(type(myFriends))

print(len(MyName))
print(len(myFriends))

a="i love "
b="dancing"
print(a+b)

name=input( "what is your name?")
name
greeting="hello "
print(greeting+ name)

introString=input("Enter string:")
characterCount=0
wordCount=1
for i in introString:
      characterCount=characterCount+1
      if(i==' '):
            wordCount=wordCount+1
print("Number of word in the string:")
print(wordCount)
print("Number of character in the string:")
print(characterCount)