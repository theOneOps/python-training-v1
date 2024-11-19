from smtplib import SMTP

my_email = "medewoubillgate@gmail.com"
password = "BIAHere@/8_"
send_to = "treedryck818@gmail.com"

with SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs=send_to,
        msg="subject:First test with python\n\nHola Bill, como estas ? muy bien y tu..._ bien gracias. :) "
    )
