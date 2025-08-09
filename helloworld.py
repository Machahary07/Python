#WAP in python to create a dictionary that contains information about books
# books = {1:{"Author":"Neelashree","Name":"Life","Price":"₹400"},
        #  2:{"Author":"Jeu","Name":"Code","Price":"₹300"}}
# print(books)

# WAP in python to create a dictionary that contains information about books

# books = {
    # 1: {"Author": "Neelashree", "Name": "Life", "Price": "₹400"},
    # 2: {"Author": "Jeu", "Name": "Code", "Price": "₹300"}
# }
# 
# print(books)

# WAP in python to create a dictionary that contains information about books

books = {
    1: {"Author": "Neelashree", "Name": "Life", "Price": "₹400"},
    2: {"Author": "Jeu", "Name": "Code", "Price": "₹300"}
}

# Nicely formatted output
for book_id, details in books.items():
    print(f"Book ID: {book_id}")
    print(f"Author : {details['Author']}")
    print(f"Name   : {details['Name']}")
    print(f"Price  : {details['Price']}\n")