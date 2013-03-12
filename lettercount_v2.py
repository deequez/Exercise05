from sys import argv

script, filename = argv

in_file = open(filename)
text = in_file.read()

counter_list = [0]*26

for char in text:
    lower_case = char.lower()
    convert_to_ord = ord(lower_case)

    if 97 <= convert_to_ord <= 122:
        counter_list[convert_to_ord - 97] +=1

print counter_list