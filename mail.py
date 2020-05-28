import smtplib
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login("abc@gmail.com", "*********")
    # message
message1 = "accuracy is less than 90%.Try again"
    # sending the mail 
s.sendmail("abc@gmail.com", "xyz@gmail.com", message1)
    # terminating the session 
s.quit()