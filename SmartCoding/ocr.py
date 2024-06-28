from PIL import Image
import pytesseract
from gtts import gTTS
from playsound import playsound

image_path = r"OCR\newspaper.png"
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

text = pytesseract.image_to_string(Image.open(image_path), lang="kor")
print(text)

with open(r"OCR\outfile.txt","w",encoding="utf8") as f:
    f.write(text)
    tts = gTTS(text=text,lang='ko')
tts.save("hi.mp3")
playsound("hi.mp3")