'''
Parameters
str − This is any delimeter, by default it is space.
num − this is number of lines to be made

Return Value
This method returns a list of lines.
'''

# Split a string using parameters
string_to_split.split(str=";", 3)

# Split last elements of a string
split_list = [item[::-1] for item in image_name[::-1].split(';', 5)][::-1]
