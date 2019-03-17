import smtplib

content="hello world"
mail=smtplib.SMTP('smtp.gmail.com')
mail.ehlo()
mail.starttls()
recipient='phoneaddicts007@gmail.com'
sender='hs475052@gmail.com'
try:
    mail.login("hs475052@gmail.com","password")
except Exception:
    print("wrong password\n see below error's")
header="To:"+recipient+'\n'+'From:' +sender+'\n'+'Subject:testing \n'
content=header+content

mail.sendmail(sender,recipient,content)
print("succesfully sent ")
mail.close()
