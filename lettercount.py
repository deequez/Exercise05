import string
received_file = raw_input("Please enter in a text file")
try:
  f = open(received_file)
except ValueError:
  print "Problem. It should be a .txt file! Try again. "
  exit() 
text = f.read()
text.lower()
f.close()

letter_dict = {}
for char in text:
  if char in letter_dict:
    count = letter_dict[char]
    count = count + 1
    letter_dict[char] = count
  else:
   count = 1
   letter_dict[char] = count

list_of_keys_random  = letter_dict.keys()
list_of_keys_random.sort()

for one_key in list_of_keys_random:
  value = letter_dict[one_key]
  print value

