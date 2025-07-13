from datetime import datetime
import time_utils
import time

now = time_utils.get_current_time()
now_time = time.localtime(now)
date_str = time_utils.format_datetime(now_time)

print(date_str)


#t = datetime.now()

#print(t.strftime("%d.%m.%Y, %H:%M:%S"))