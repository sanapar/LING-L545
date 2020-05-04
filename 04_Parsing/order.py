# Python script to collect information about relative order of object and verb in treebanks from the Universal Dependencies project.
# L-545
# Practical 04

import sys


verbobject = 0 # variable for verb-object order
objectverb = 0 # variable for object-verb order
for i in sys.stdin.readlines(): # loop through the text
    if i.startswith('#'): # ignore comments
        continue
    elif i.strip() == '': # ignore empty lines
        continue
    text = i.split('\t') # split the text by tabs
    if 'obj' in text: # if object is found in the text:
        if text[0] > text[6]: # if the object index is greater than the head index, plus 1 for verb-object
                verbobject +=1
        elif text[6] > text [0]: # if the head index is greater than the object index, plus 1 for object-verb
                objectverb += 1

if float(objectverb) < float(verbobject): # If the value for "objectverb" is less than the value for "verboject", print the relative orders:
        print ("The relative order of object-verb is: ", "{:.1f}".format(float(objectverb)/float(verbobject)))
        print ("The relative order of verb-object is: ", "{:.1f}".format(1-(float(objectverb)/float(verbobject))))
else: # Otherwise (if it is less frequent), print it the other way round (avoid negative or too high values)
        print  ("The relative order of verb-object is: ", "{:.1f}".format(float(verbobject)/float(objectverb)))
        print  ("The relative order of object-verb is: ", "{:.1f}".format(1-(float(verbobject)/float(objectverb))))
