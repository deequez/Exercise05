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
print text
text.replace(' ','')
text.strip()
l = sorted(text)


alphabet = 'abcdefghijklmnopqrstuvwxyz'
for char in alphabet:
  if char not in l:
    count = 0
  else:
    count = 0
    for item in l:
      if item == char:
        count += 1    
  print '%r' % (count)

