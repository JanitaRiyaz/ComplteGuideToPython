'''string is a datatye in python.
    it is basically sequence of characters that are enclose in quotes'''
    
# single quote string:
     name='janita'

# Double quote string:
     name="janita"

# triple quote string:
   name=''''janita'''

# input Function:
# input function is used to get input.
 name=input('what is your name? ')

 print(f'Good Morning {name}')

'''here name is replace with user input. f string is used to 
 concatenate diffrerent datatypes'''


#      ********String Slicing*********

name='janita'

# length=5 because indexing/numbering in python starts with zero

sl=name[index.start: index end]

sl=name[0,3]

print(sl)
# the output will be 'jan'
sl=name[:2:] 
# the skip values will set as zero by deafault.
sl=[:-1]


#           *****String Function*****

story='once upon a time there was a coder who tried to complete a git repo about python'

print(story.len())   
# gives length

print(story.endswith('coder'))

# retuen wheher there is coder and return the story till coder

print(story.count('c'))
# returns how many times letter c occurs

print(story.capitalize())
# capitalize all the words

print(story .find('tried'))
# find specificc word 

print(story.replace('janita','john'))
# replace janita with john


#          ****Escape Function****

 story='janita is a /ngood girls'

#  escpae to next line


''''          Examples           ''''

 /n  for new line
 /t for tab
 /'  for single quote
 // for backslash

