import os
import datetime
import shutil

# Enter your input and Output path 
input_path = "Enter your input path here"
out_path = "Enter your output path here"
temp = []
for root,dirs,files in os.walk(input_path):
    for i in files:
        temp_path = os.path.join(root,i)
        created= os.stat(temp_path).st_mtime # Getting the file modified date 
        date_=datetime.datetime.fromtimestamp(created)
        year_ = (date_.date().strftime("%Y"))
        month_ =(date_.date().strftime("%B"))
        check_path = os.path.join(out_path,year_,month_)
        
        if not os.path.exists(check_path):
            os.makedirs(check_path)
        try:
            shutil.copy(temp_path, check_path)
        except:
            temp.append(temp_path)
