#Leon Oram
#09-01-2014
#Linear Search

def inputs():
    search = input("Please enter the name to search for: ")
    search = search.lower()
    return search


def search(list_,is_in):
    found = False
    found_at = ""
    count = 0
    while not found and count < len(list_):
        if list_[count] == is_in:
            found_at = count
            found = True
        count = count+1
    return found,found_at

people=["bob","john","steve","jane",]
is_in = inputs()
found,found_at = search(people,is_in)
if found:
    print("{0} was found at index {1}".format(is_in,found_at))                          
else:
    print(is_in,"was not found")
