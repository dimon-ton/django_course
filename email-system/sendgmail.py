import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def sendthai(sendto,subj="ทดสอบส่งเมลลล์",detail="สวัสดี!\nคุณสบายดีไหม?\n"):

	myemail = 'pimon.tungratogtest@gmail.com'
	mypassword = 'dmxzrerrrrxdbocw'
	receiver = sendto

	msg = MIMEMultipart('alternative')
	msg['Subject'] = subj
	msg['From'] = 'ระบบทดสอบส่งเมล'
	msg['To'] = receiver
	text = detail

	part1 = MIMEText(text, 'plain')
	msg.attach(part1)

	s = smtplib.SMTP('smtp.gmail.com:587')
	s.ehlo()
	s.starttls()

	s.login(myemail, mypassword)
	s.sendmail(myemail, receiver.split(','), msg.as_string())
	s.quit()

	print('ส่งแล้ว')

###########Start sending#############
subject = 'ลุง!! เงินผมหมดแล้วววว'

msg = '''สวัสดีครับ
ทดสอบส่งข้อความ
'''

sendthai('pimon.tungratogtest@gmail.com', subject, msg)