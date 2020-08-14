import cv2

# 1.creating a video object
video = cv2.VideoCapture(0) 
# 2. Variable
a = 0
# 3. While loop
while True:
    a = a + 1
    # 4.Create a frame object
    check, frame = video.read()
    # Converting to grayscale
    #gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    # 5.show the frame!
    cv2.imshow("Capturing",frame)
    # 6.for playing 
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
# 7. image saving
showPic = cv2.imwrite("filename.jpg",frame)
print(showPic)
# 8. shutdown the camera
video.release()
cv2.destroyAllWindows 

photo=r'H:\Program video\my projects\reader for blind\filename.jpg'
import pytesseract as tess
tess.pytesseract.tesseract_cmd = r'C:\Users\PRASAD BHOSALE\AppData\Local\Tesseract-OCR\tesseract.exe'
from PIL import Image

img = Image.open(photo)
text = tess.image_to_string(img)

print(text)




#text to speech
# Import the Gtts module for text  
# to speech conversion 
from gtts import gTTS 
  
# import Os module to start the audio file
import os 
  
mytext = text
  
# Language we want to use 
language = 'en'
  

myobj = gTTS(text=mytext, lang=language, slow=False) 
  

myobj.save("output.mp3") 
  
# Play the converted file 
os.system("start output.mp3") 
