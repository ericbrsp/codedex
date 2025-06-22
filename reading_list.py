
''' 
List Method	Description:
.append()	Add an item to the end of the list
.clear()	Remove all items from the list
.copy()	Return a shallow copy of the list
.count()	Return the number of times the value appears in the list
.extend()	Appends another list to the current list by extending it
.index()	Returns the index of a value inside the list
.insert()	Insert an item at a specified position in the list
.pop()	Remove an item from a specified position in the list
.remove()	Remove an item from the list based on the value of the item
.reverse()	Reverses the list in place
.sort()	Sorts the list in place
'''


list_books = ['Harry Potter',
'1984',
'The Fault in Our Stars',
'The Mom Test',
'Life in Code',
]

list_books.append('Pachinko')
list_books.remove('The Fault in Our Stars')

#também remove, porém tem que apontar a posição a ser removida:
list_books.pop(1)

print(list_books)
