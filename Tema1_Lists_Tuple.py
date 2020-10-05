# Requirements: 
# • Have at least 400 articles in the shop 
# • Have at least four types of articles (shirt, scarf, glove, heat) 
# • Have at least five sizes (S M L XL XXL) for each type of article 
# • To be able to sell the latest article that was added to the shop
# • To be able to sell any item that is in the shop 
# • To restock the shop with new items

article = ('shirt', 'scarf', 'glove', 'heat')
size = ('S', 'M', 'L', 'XL', 'XXL')
my_shop = [('shirt', 'S'), ('shirt', 'M'), ('glove', 'S')]
my_shop = [(article, size)]
print(f'my_shop has these articles {article} the following sizes {size}')

my_shop.pop(-1)

new_item = ('heat','XL')
my_shop.append(new_item)

toSellItem = input("Please choose the item to sell ")
my_shop.remove(toSellItem)

toSellIndex = input("Please choose the index to sell ")
my_shop.pop(toSellIndex)


#1. Write a python code to remove an element from a tuple.

my_tuple = "red", 3, "black", "green", "orange", "white", "blue", "violet", "purple"
print(my_tuple)
my_tuple = my_tuple[:3] + my_tuple[4:]
print(my_tuple)
my_list = list(my_tuple) 
my_list.remove("purple") 
my_tuple = tuple(my_list)
print(my_tuple)

#2. Replace the last element in the list with the string 'last'
using list comprehension and tuples

my_list = ['red','blue','white','yellow','black','purple','pink']
print("The original list is : " + str(my_list)) 
result = ['last' if my_list[-1]==sub else sub for sub in my_list]

print("The tuple after replacement is : " + str(result))


#3. Extract only the strings from the following list using list comprehension :
slist = ['I', 'am', 1, 'list', 'of', 5, 'strings']
result = [char for char in slist if str(char).isdigit() == False]

#4. Generate a 3 by 3 matrix that contains 'X' on the main diagonal and '_' in the rest.
n, m = 3, 3;
Matrix = [['_' if i == j else 'X' for i in range(n)] for j in range(m)]
print(Matrix)

