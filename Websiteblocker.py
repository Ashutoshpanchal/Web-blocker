import time
from datetime import datetime as dt

hosts_temp=r"C:\python\project\web_blocker\hosts"
hosts_path=r"C:\Windows\System32\drivers\etc\hosts"
redirect="127.0.0.1"
website_lists=["yahoo.com","www.yahoo.com"]

while True:
       if dt(dt.now().year,dt.now().month,dt.now().day,8)<dt.now()<dt(dt.now().year,dt.now().month,dt.now().day,10):
           #print("Working Hour...........")
          #with open(hosts_temp,"r+") as file:   
           with open(hosts_path,"r+") as file:
               content=file.read()
               print(content)
               for website in website_lists:
                      if website in content:
                          pass
                      else:
                           file.write(redirect+" "+website+"\n")
                            

       else :
            print("Fun Hour................")
           #with open(hosts_temp,"r+") as file: 
            with open(hosts_path,"r+") as file:
               content=file.readlines()
               file.seek(0)
               print(content)
               for line  in content:
                      if not any (website in line for website in website_lists):
                           file.write(line)
               file.truncate()
       time.sleep(5)
