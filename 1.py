from PIL import Image
import numpy as np
import pytesseract
import json


# import image and convert text
file = '1.jpg'
img = np.array(Image.open(file))
text = pytesseract.image_to_string(img)

chars_to_remove = "/\,);}{(.?!|"
text = text.replace("\n", "")
print(text)


# Detection position of target string
useraccount_num = text.find('payments to be made')
date_num = text.find('Preferred start date')
payer_particular_num = text.find('codePayer reference')
authentication_code_num = text.find(')Authorisation code')
bank_address_num = text.find('GreenlaneBranchAddress ')


# Detection of target string
useraccount_number = text[useraccount_num+19: useraccount_num+32]
preferred_start_date = text[date_num+20: date_num+30]
payer_particular = text[payer_particular_num+19:payer_particular_num+33]
authentication_code = text[authentication_code_num+20: authentication_code_num+36]
bank_address = text[bank_address_num+23:bank_address_num+69]
payer_code = text[payer_particular_num+33:payer_particular_num+41]
payer_reference = text[payer_particular_num+41:payer_particular_num+47]

# Removing characters
for char in chars_to_remove:
    authentication_code = authentication_code.replace(char, '')
    payer_particular = payer_particular.replace(char, '')

# Save as json file
data = {
    "useraccout_number": useraccount_number,
    "preferred_start_date": preferred_start_date,
    "bank_address":bank_address,
    "authentication_code":authentication_code,
    "payer_particular":payer_particular,
    "payer_code":payer_code,
    "payer_reference":payer_reference
}

with open('data.json', 'w') as f:
    json.dump(data, f)

# Save as txt file
f = open('file.txt', 'w')
f.writelines(text)

