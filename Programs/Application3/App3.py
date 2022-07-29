import time
from datetime import datetime as dt


hosts_path=r"C:\Windows\Systems32\drivers\etc\hosts"
hosts_temp=r"C:\Users\caudww\OneDrive - Cambridge\Documents\GitHub\Pyton_real_world\Programs\Application3\hosts"
#r is added to show python it is a row due to key word such as \n
redirect="127.0.0.1"
website_list=["www.facebook.com","facebook.com", "dub119.mail.live.com","www.dub119.mail.live.com"]

#while loop to check if time falls between 8am and 4pm each day
#pulls each day,month and year for both set times
while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,8) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,16):
        print("Working hours...")
        with open(hosts_temp, 'r+') as file:
            content=file.read()
            print(content)
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect+" "+ website+"\n")
    else:
        print("Fun hours...")
    time.sleep(5)
