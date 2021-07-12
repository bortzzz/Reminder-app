from datetime import datetime, timedelta  
import keyboard, os
from playsound import playsound
def popupmsg():
	playsound('alrt2.mp3')
	os.system("alrt.vbs")
    
print('NOTED : This app use 24-hour military time, You will heard a sound and a box will popup when reminder is triggered.')
while True:
	
	cus1=input('Select Mode (hr & mn) :')
	if cus1 == 'hr':
		hr = input('Please Enter Hour As Number (01-24):')
		minute = input('Please Enter Minute As Number (01-60):')
		if len(hr) == 1:
			hr = "0"+hr
		if len(minute) == 1:
			minute = "0"+ minute
		hrINT = int(hr)
		minuteINT = int(minute)
		print('\n*press "f12" to cancel*\n')
		while True:
			ini_time_for_now = datetime.now()  
				
			
			print (f"Time : {str(ini_time_for_now)}",end='\r')  
			if (ini_time_for_now.hour == hrINT) and (ini_time_for_now.minute == minuteINT):
				os.system('cls')
				popupmsg()
				break
			if keyboard.is_pressed('f12'):
				os.system('cls')
				print('Cancelled ~')
				break
	if cus1=='mn':
		mns = input('Please Enter Minute As Number (01-60) :')
		secs = input('Please Enter Second As Number (01-60) :')
		if len(mns) == 1:
			mns = "0"+mns
		if len(secs) == 1:
			secs = "0"+ secs
		msINT = int(mns)
		secsINT = int(secs)
		print('\n*press "f12" to cancel*\n')
		while True:
			ini_time_for_now = datetime.now()  
				
			
			print (f"Time : {str(ini_time_for_now)}",end='\r') 
				
			
			if (ini_time_for_now.minute == msINT) and (ini_time_for_now.second == secsINT):
				os.system('cls')
				popupmsg()
				break
			if keyboard.is_pressed('f12'):
				os.system('cls')
				print('Cancelled ~')
				break 
