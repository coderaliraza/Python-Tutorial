#take two comma separated input for user
# 1.) user's name
# 2.) a single character 

# output:- 2 print lines
# 1.) user's name length
# 2.) count the character that user inputed (bonus: case insensitive count)

# solution
# name , char = input("enter comma name and character: ").split(",")
# print(f"length of name{len(name)}")
# print(f"character you name: {name.lower().count(char.lower())}")





name , char = input("enter comma name and character: ").split(",")
print(f"length of name{len(name)}")
print(f"character count:  {name.strip().lower().count(char.strip().lower())}")