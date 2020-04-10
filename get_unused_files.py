import os
import datetime
current_date= datetime.datetime.now()
current_month = current_date.month
for dirpath, dirname, filename in os.walk('/Users/shrishtisharma/Documents'):
    try:
        os.chdir(dirpath)
        for i in filename:
            current_mod_date = datetime.datetime.fromtimestamp(os.stat(i).st_mtime)
            current_mod_month = current_mod_date.month
            if current_mod_month < current_month:
                print(i)
    except:
        pass


