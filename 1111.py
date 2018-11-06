import time

# time获取当前时间戳
now = time.time()    # 1533952277
print()    #毫秒级时间戳
timeArray = time.localtime(now)
print(timeArray)
timeStamp = int(time.mktime(timeArray))*1000
print(timeStamp)