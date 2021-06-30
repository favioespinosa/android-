import uiautomator2 as u2
from time import sleep
import time
import hashlib
class Phone_emulator:
	def __init__(self,phone,ident):
		self.phone = phone
		str2hash=str(phone)
		str2hash=hashlib.md5(str2hash.encode())
		self.name=str(str2hash.hexdigest())
		self.ident=ident
		self.d = u2.connect_usb(ident)

	def add_contact(self):
		self.d.press("home")
		self.d(text="Phone").click()
		self.d(text="Contacts").click()
		self.d(text="Create new contact").click()
		self.d(text="First name").set_text(self.name)
		self.d(text="Phone").set_text(self.phone)
		self.d(text="SAVE").click()

	def go_whats(self):
		self.d.press("home")
		self.d(text="WhatsApp").click()
		self.d(resourceId="com.whatsapp:id/menuitem_search").click()
		self.d(resourceId="com.whatsapp:id/search_input").set_text(self.name)
		if self.d(resourceId="com.whatsapp:id/contact_photo").count==0:
			self.d.press("back")
			self.d.press("back")
			self.d.press("back")
			self.d.press("back")
			return -1
		self.d(resourceId="com.whatsapp:id/contact_photo").click()
		self.d(text=self.name).click()
		sleep(1)
		self.d.screenshot(self.name+".jpg")
		self.d.press("back")
		self.d.press("back")
		self.d.press("back")
		self.d.press("back")
		return 0
			
start=time.time()
w=Phone_emulator("+79858907963","emulator-5554")
w.add_contact()
if not w.go_whats():
	print("Has it")
fin=time.time()
print(fin-start)