#mainFaceGen.py

#This program currently takes in and organizes the picture files (of facial features) in a folder
#Prompts the user for an emotion (currently: angry, happy or neutral)
#Creates a randomly generated face based on the available options for that emotion

import Image #to work with the images
import os  #for use in reading in the names from the folder
import random 


###########################################
#Bring in and organize pictures by emotion#
###########################################

#Get all items in the folder as a list of strings - 
filenames = os.listdir("FILEPATH")
#print filenames

#initialize Lists of emotions with picture filenames
noses = []
angry_mouths = []
angry_eyes = []
happy_mouths = []
happy_eyes = []
neutral_mouths = []
neutral_eyes = []

#separate filenames into appropriate lists
for filename in filenames:
    if "nose" in filename:
        noses = noses+[filename]
    if "angry" in filename:
        if "mouth" in filename:
            angry_mouths = angry_mouths+[filename]
        if "eye" in filename:
            angry_eyes = angry_eyes+[filename]
    if "neutral" in filename:
        if "mouth" in filename:
            neutral_mouths = neutral_mouths+[filename]
        if "eye" in filename: #neutral eyes work for happy faces too
            neutral_eyes = neutral_eyes+[filename]
            happy_eyes = happy_eyes+[filename]
    if "happy" in filename:
        if "mouth" in filename:
            happy_mouths = happy_mouths+[filename]
        if "eye" in filename:
            happy_eyes = happy_eyes+[filename]

  

##################################################
#Ask user what emotion they would like to display#
##################################################

chosen_emotion = raw_input("Choose an emotion: angry, happy, neutral\n")


########################################################
#Generate face based on user input and random selection#
########################################################

#Function with input of chosen emotion that creates and returns the finished picture
def face_painter(emotion):
    
    #Create empty canvas to place the picture on
    canvas = Image.new("RGB",(500,500),"white") 
    
    #choose random filenames from the list for that emotion
    chosen_nose = noses[random.randrange(0,(len(noses)))]
    if emotion == "angry":
        chosen_eye1 = angry_eyes[random.randrange(0,(len(angry_eyes)))]
        chosen_mouth = angry_mouths[random.randrange(0,(len(angry_mouths)))]
    if emotion == "happy":
        chosen_eye1 = happy_eyes[random.randrange(0,(len(happy_eyes)))]
        chosen_mouth = happy_mouths[random.randrange(0,(len(happy_mouths)))]
    if emotion == "neutral":
        chosen_eye1 = neutral_eyes[random.randrange(0,(len(neutral_eyes)))]
        chosen_mouth = neutral_mouths[random.randrange(0,(len(neutral_mouths)))]
   
    #Create Picture
    nose = Image.open(chosen_nose)
    eye = Image.open(chosen_eye1)
    eye2 = eye.transpose(Image.FLIP_LEFT_RIGHT) # so we only need one eye drawing
    mouth = Image.open(chosen_mouth)
    canvas.paste(nose,(200,200))
    canvas.paste(mouth,(100,300))
    canvas.paste(eye,(100,100))
    canvas.paste(eye2,(300,100))
    
    return canvas
   

#Calls face generating function
final_pic = face_painter(chosen_emotion)

#shows picture
final_pic.show()

##################################################################
#Additional Function to create and display a lot of faces at once#
##################################################################
"""

test_emotions = ["happy","angry","neutral"]
test_canvas = Image.new("RGB",(2000,2000),"white") 

#size of thumbnail
thumb_size = 100, 100

#scroll through coordinates of canvas by size of thumbnail square and create a list of coordinates for pasting the thumbnails onto the canvas
coordinates = []
for x in range(0,test_canvas.size[0],thumb_size[1]): #range = (start,end,increase by amount)
    for y in range(0,test_canvas.size[1],thumb_size[1]):
        coordinates = coordinates + [[x,y]]
        
#create thumnails for faces built from randomly selected emotions 
#paste on canvas by scrolling through list of coordinates
for coor in coordinates:
    rand_emotion = test_emotions[random.randrange(len(test_emotions))] 
    test_pic = face_painter(rand_emotion)
    test_pic.thumbnail(thumb_size,Image.ANTIALIAS)
    test_canvas.paste(test_pic,tuple(coor))

#show canvas with pictures
test_canvas.show()
#save file to current folder
test_canvas.save("faces","JPEG")
"""
