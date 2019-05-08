# lists

my_list = [1,2,3,5,6]

first_number = my_list[4]

# dictionaries

my_dict = { 'a' : 1, 'b' : 45 }

how_many_a = my_dict['a']


string = 'some text'
#         012345678

# initialization, condition, incrementation
index = 0 # counter for the index into the string
while index < len(string): # loop syntax, this is where the condition goes
    print(index, string[index]) # print the string at the index
    index = index + 1 # increment the counter

# KATE
# initialization, condition, incrementation
index = 0 # counter for the index into the string
kate_dict = { }
while index < len(string): # loop syntax, this is where the condition goes
    if string[index] in kate_dict:
        kate_dict[string[index]] += 1
    else:
        kate_dict[string[index]] = 1
    index = index + 1 # increment the counter

print('Kate:', kate_dict)