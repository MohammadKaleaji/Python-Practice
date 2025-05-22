printed = ['phone case', 'laptop', 'glasses']
unprinted = []

# Function to loop throw printed , pop element and append it to unprinted
def add_unprinted(printted_list, unprinted_list):
     while printted_list:
          current_item = printted_list.pop()
          print(f"The printed Item {current_item}")
          unprinted_list.append(current_item)

def show_printed(unprinted_list):
     print(f"\nThis is the list of Newly Printed Items: ")
     for item in unprinted_list:
          print(item)

add_unprinted(printed[:], unprinted) # the [:] says to python that the edits was just a copy of printed list 
show_printed(unprinted)              # and keep the original items of printed list in line 1

print(printed) #Testing [:]