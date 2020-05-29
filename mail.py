import smtplib
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login("anand31798@gmail.com", "3179724774937007")
    # message
message1 = "accuracy is less than 90%.Try again"
    # sending the mail 
s.sendmail("anand31798@gmail.com", "1706298@kiit.ac.in", message1)
    # terminating the session 
s.quit()