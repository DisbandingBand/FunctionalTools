import time
import pandas as pd
import requests

# 数据处理部分
def timeplus(time):    #垃圾算法 让上课时间加上40分钟 返回下课时间
    time_1=time[:2]
    time_2=time[2:]
    if int(time_2)+40>=60:
        time_1=str(int(time_1)+1)
        if len(str(time_1))==1:
            time_1='0'+str(time_1)
        time_2=int(time_2)+40-60
        if time_2==0:
            time_2='00'
        elif len(str(time_2))==1:
            time_2='0'+str(time_2)
        else:
            time_2=str(time_2)
        return time_1+time_2
    else:
        return time_1+str(int(time_2)+40)
    
    
#由于疫情原因学校楼层错峰下课，所以每层楼的上课时间不同，分开计算
four=['0820','0900','1010','1050','1350','1430','1540','1620','1800','1840','1920','2000','2040']
three=['0840','0920','1030','1110','1410','1450','1600','1640','1820','1900','1940','2020']
#爬取学校教务网站课表
rsp=requests.get('***************************') #链接不便展示
rsp.encoding='utf-8'
f=open('7.txt','w',encoding='utf-8')



head=['BEGIN:VCALENDAR',
'METHOD:PUBLISH',
'VERSION:2.0',
'X-WR-CALNAME:Clander',
'PRODID:-//Apple Inc.//macOS 13.4.1//EN',
'X-APPLE-CALENDAR-COLOR:#34AADC',
'X-WR-TIMEZONE:Europe/London',
'CALSCALE:GREGORIAN']
for i in head:
    f.write(i)
    f.write('\n')
time=pd.read_html(rsp.text)[0].iloc[1:,0]
id=0
for j in range(1,8):
    day=pd.read_html(rsp.text)[0].iloc[0,j]
    day_list=day[3:].split('-')
    day_str=day_list[1]+day_list[2]
    print(day_str)
    for n,i in enumerate(pd.read_html(rsp.text)[0].iloc[1:,j]):
        if pd.isna(i):
            pass
        else:
            id+=1
            if n>=4:
                n-=2
            if '3' in i:  
                start_str=three[n]
            else:
                start_str=four[n]
            f.write('BEGIN:VEVENT')
            f.write('\n')
            f.write('CREATED:20201011T104613Z')
            f.write('\n')
            f.write('UID:{}'.format(id))
            f.write('\n')
            f.write('DTEND;TZID=Asia/Shanghai:2020{}T{}'.format(day_str,timeplus(start_str)+'00'))
            f.write('\n')
            f.write('TRANSP:OPAQUE')
            f.write('\n')
            f.write('X-APPLE-TRAVEL-ADVISORY-BEHAVIOR:AUTOMATIC')
            f.write('\n')
            f.write('SUMMARY:{}'.format(i))
            f.write('\n')
            f.write('LAST-MODIFIED:20201011T104619Z')
            f.write('\n')
            f.write('DTSTAMP:20201012T104622Z')
            f.write('\n')
            f.write('DTSTART;TZID=Asia/Shanghai:2020{}T{}'.format(day_str,start_str)+'00')
            f.write('\n')
            f.write('SEQUENCE:1')
            f.write('\n')            
            f.write('BEGIN:VALARM')
            f.write('\n')
            f.write('X-WR-ALARMUID:F03864BD-41F4-40EC-BF20-1E4E7930ED92')
            f.write('\n')
            id+=1
            f.write('UID:{}'.format(id))
            f.write('\n')        
            f.write('TRIGGER:-PT30M')
            f.write('\n')
            f.write('ATTACH;VALUE=URI:Chord')
            f.write('\n')
            f.write('ACTION:AUDIO')
            f.write('\n')
            f.write('END:VALARM')
            f.write('\n')
            f.write('END:VEVENT')
            f.write('\n')
f.write('END:VCALENDAR')
f.close() 
