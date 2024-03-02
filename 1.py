from PIL import Image
import pytesseract
# import pandas as pd
import json

img = Image.open('1.jpg') 
text = pytesseract.image_to_string(img)
# print(type(text))
# f = open('file.txt', 'w')
# f.writelines(text)
txt= text.replace("\n", "")
numOfDate = txt.find('Preferred start date')
numOfAccountNum = txt.find('payments to be made')
# print(numOfDate)
# print(numOfAccountNum)
useraccount_number = txt[numOfAccountNum+19: numOfAccountNum+33]
# print(useraccount_number)
preferred_start_date = txt[numOfDate+20: numOfDate+30]
# print(preferred_start_date)
data = {
    "useraccout_number": useraccount_number,
    "preferred_start_date": preferred_start_date
}

with open('data.json', 'w') as f:
    json.dump(data, f)
f = open('file.txt', 'w')
f.writelines(txt)