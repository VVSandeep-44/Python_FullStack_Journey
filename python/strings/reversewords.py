
'''
take a statement. print words in the reverse order. eg: "palle tech pvt ltd" . output : ltd pvt tech palle. student can use split() function 
'''
statement = "palle tech pvt ltd"
words = statement.split()
for i in range(len(words)-1, -1, -1):
    print(words[i], end=" ")
