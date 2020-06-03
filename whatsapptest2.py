import time
import pyautogui
import subprocess
from tkinter import * 
from tkinter.filedialog import askopenfile # importing askopenfile function from filedialog class

class App:
	def main():
		global img_CBisClicked, vid_CBisClicked, doc_CBisClicked # global variables
		img_CBisClicked = False # default value will always be FALSE
		vid_CBisClicked = False # and will only be changed to TRUE
		doc_CBisClicked = False	# when the checkbox has been clicked

		# gui begins
		win = Tk()
		win.geometry("400x400")
		win.title("WhatsApp Texter")

		name = Label(win, text = "Name:")
		name.grid(row = 2, column = 2 )

		name_textb = Entry(win, bd = 5)
		name_textb.grid(row = 2, column = 4)

		msg = Label(win, text = "Message:")
		msg.grid(row = 4, column = 2 )

		msg_textb = Entry(win, bd = 5, width = "30")
		msg_textb.grid(row = 4, column = 4)

		frame = Frame(win, bd = 5, width = 100, height = 100, bg = 'light slate grey')
		frame.grid(row = 8, column = 4)
		
		def img_open_func():
			try:
				global img_file_path
				global file_img
				file = askopenfile(mode ='r', filetypes =[('All Files', '*.*')]) #---------------------------------># astrick (*), matches with any number
				# print(file) # <_io.TextIOWrapper name='C:/Pics/Nature/flower.jpg' mode='r' encoding='cp1252'>		# of characters and file extensions
				filename = file.name # file.name outputs only C:/Pics/Nature/flower.jpg
				# print('filename:  '+ filename) # outputs C:/Pics/Nature/flower.jpg
				file_address= filename.split('/') # splits the file path with blackslash as delimiter
				# print('file_address:  '+ str(file_address))
				last_index = len(file_address) - 1 # finds out the last index of the string
				# print('last_index:  '+ str(last_index))
				file_img = file_address[last_index] # finds out the actual file i.e flower.jpg     #----->important : file_img
				# print('file_img:  '+ file_img) # outputs flower.jpg
				del file_address[last_index] # removes the actual file from the string
				# print('new file_address:  '+ str(file_address)) # outputs ['C:','Pics','Nature']

				# putting back the file path except the actual file
				separator = '/' # using backslash as separator for file path
				img_file_path = separator.join(file_address)                                            #----->important : img_file_path
				print('img_file_path:  '+ img_file_path) # output will be C:/Pics/Nature
			except:
				img_file_path = '' # default value is an empty string
				pyautogui.hotkey('altleft', 'space', 'c') # closes file browser window if cancel button is pressed

		def vid_open_func():
			try:
				global vid_file_path
				global file_vid
				file = askopenfile(mode ='r', filetypes =[('All Files', '*.*')]) #---------------------------------># astrick (*), matches with any number
				# print(file) # <_io.TextIOWrapper name='C:/Pics/Nature/flower.jpg' mode='r' encoding='cp1252'>		# of characters and file extensions
				filename = file.name # file.name outputs only C:/Pics/Nature/flower.jpg
				# print('filename:  '+ filename) # outputs C:/Pics/Nature/flower.jpg
				file_address= filename.split('/') # splits the file path with blackslash as delimiter
				# print('file_address:  '+ str(file_address))
				last_index = len(file_address) - 1 # finds out the last index of the string
				# print('last_index:  '+ str(last_index))
				file_vid = file_address[last_index] # finds out the actual file i.e flower.jpg     #----->important : file_vid
				# print('file_vid:  '+ file_vid) # outputs flower.jpg
				del file_address[last_index] # removes the actual file from the string
				# print('new file_address:  '+ str(file_address)) # outputs ['C:','Pics','Nature']

				# putting back the file path except the actual file
				separator = '/' # using backslash as separator for file path
				vid_file_path = separator.join(file_address)                                            #----->important : vid_file_path
				print('vid_file_path:  '+ vid_file_path) # output will be C:/Pics/Nature
			except:
				vid_file_path = '' # default value is an empty string
				pyautogui.hotkey('altleft', 'space', 'c') # closes file browser window if cancel button is pressed

		def doc_open_func():
			try:
				global doc_file_path
				global file_doc
				file = askopenfile(mode ='r', filetypes =[('All Files', '*.*')]) #---------------------------------># astrick (*), matches with any number
				# print(file) # <_io.TextIOWrapper name='C:/Pics/Nature/flower.jpg' mode='r' encoding='cp1252'>		# of characters and file extensions
				filename = file.name # file.name outputs only C:/Pics/Nature/flower.jpg
				# print('filename:  '+ filename) # outputs C:/Pics/Nature/flower.jpg
				file_address= filename.split('/') # splits the file path with blackslash as delimiter
				# print('file_address:  '+ str(file_address))
				last_index = len(file_address) - 1 # finds out the last index of the string
				# print('last_index:  '+ str(last_index))
				file_doc = file_address[last_index] # finds out the actual file i.e flower.jpg     #----->important : file_doc
				# print('file_doc:  '+ file_doc) # outputs flower.jpg
				del file_address[last_index] # removes the actual file from the string
				# print('new file_address:  '+ str(file_address)) # outputs ['C:','Pics','Nature']

				# putting back the file path except the actual file
				separator = '/' # using backslash as separator for file path
				doc_file_path = separator.join(file_address)                                            #----->important : doc_file_path
				print('doc_file_path:  '+ doc_file_path) # output will be C:/Pics/Nature
			except:
				doc_file_path = '' # default value is an empty string
				pyautogui.hotkey('altleft', 'space', 'c') # closes file browser window if cancel button is pressed				

		def img_open_is_clicked():
			global img_file_path
			if len(img_file_path) != 0: # checks if the size of img_file_path is zero(empty) or not
				global img_CBisClicked
				img_CBisClicked = True

		def vid_open_is_clicked():
			global vid_file_path
			if len(vid_file_path) != 0: # checks if the size of img_file_path is zero(empty) or not
				global vid_CBisClicked
				vid_CBisClicked = True

		def doc_open_is_clicked():
			global doc_file_path
			if len(doc_file_path) != 0: # checks if the size of img_file_path is zero(empty) or not
				global doc_CBisClicked
				doc_CBisClicked = True					

					#-----frame contents-----#
		img = Checkbutton(frame, text = 'Add Image')
		img.grid(row = 8, column = 1)
		img_open = Button(frame, text = 'Open', command = lambda: [img_open_func(), img_open_is_clicked()])
		img_open.grid(row = 8, column = 3)                   # file browser ^^  				 # ^^ img checkbox  click counter

		vid = Checkbutton(frame, text = 'Add Video')
		vid.grid(row = 9, column = 1)
		vid_open = Button(frame, text = 'Open', command = lambda: [vid_open_func(), vid_open_is_clicked()])
		vid_open.grid(row = 9, column = 3)                   # file browser ^^  				 # ^^ vid checkbox click counter

		doc = Checkbutton(frame, text = 'Add Document')
		doc.grid(row = 10, column = 1)
		doc_open = Button(frame, text = 'Open', command = lambda: [doc_open_func(), doc_open_is_clicked()])
		doc_open.grid(row = 10, column = 3)                  # file browser ^^  				 # ^^ doc checkbox click counter
					#-----frame contents-----#

		# functions for buttons to perform
		def clear_func():
			name_textb.delete(0, 'end') # clears the textboxes
			msg_textb.delete(0, 'end') # clears the textboxes
			img_CBisClicked = False
			vid_CBisClicked = False
			doc_CBisClicked = False

		def send_func():
			receiver = name_textb.get()
			text = msg_textb.get()
			# print(receiver, text)
			win.destroy()
			subprocess.Popen(r"C:\Users\JasonPC\AppData\Local\WhatsApp\WhatsApp.exe")
			# time.sleep(0.5)
			pyautogui.hotkey('altleft', 'space', 'x') # maximises WhatsApp window
			Texter.mousecontrol(receiver, text)

		def exit_func():
			win.destroy() # closes the app

		clear_btn = Button(win, text = "Clear", command = clear_func)
		clear_btn.grid(row = 15, column = 2)

		send_btn = Button(win, text = "Send", command = send_func)
		send_btn.grid(row = 15, column = 4)

		exit_btn = Button(win, text = "Exit", command = exit_func)
		exit_btn.grid(row = 15, column = 6)

		win.mainloop()
		# gui ends

class Texter():
	              #-----Attachment controls-----#
	def send_file():
		# pyautogui.moveTo(1830, 870) # moves cursor to green send button
		pyautogui.click(1830, 870) # clicks on the green send button

	def openfilewindow(file_item, file_path):
		# pyautogui.moveTo(400, 60) # moves cursor to file address bar
		pyautogui.click(400, 60) # clicks on file search bar
		pyautogui.typewrite(file_path, 0.15)
		pyautogui.press('enter') # stimulates ENTER key press

		# pyautogui.moveTo(235, 953) # moves cursor to file search bar
		pyautogui.click(235, 953) # clicks on file search bar
		pyautogui.typewrite(file_item, 0.15)

		# pyautogui.moveTo(1700, 990) # moves cursor to Open button
		pyautogui.click(1700, 990) # clicks on Open button
		time.sleep(2) # lets the file load 
		Texter.send_file()

	def img_func():
		# pyautogui.moveTo(1815, 69) # moves cursor to attach button
		pyautogui.click(1815, 69) # clicks on attach button
		time.sleep(0.5)
		pyautogui.click(1815, 160) # clicks on image button
		time.sleep(0.5)
		pyautogui.hotkey('altleft', 'space', 'x') # maximises file browser window
		Texter.openfilewindow(file_img, img_file_path)

	def vid_func():
		# pyautogui.moveTo(1815, 69) # moves cursor to attach button
		pyautogui.click(1815, 69) # clicks on attach button
		time.sleep(0.5)
		pyautogui.click(1815, 160) # clicks on video button
		time.sleep(0.5)
		pyautogui.hotkey('altleft', 'space', 'x') # maximises file browser window
		Texter.openfilewindow(file_vid, vid_file_path)

	def doc_func():
		# pyautogui.moveTo(1815, 69) # moves cursor to attach button
		pyautogui.click(1815, 69) # clicks on attach button
		time.sleep(0.5)
		pyautogui.click(1815, 335) # clicks on document button
		time.sleep(0.5)
		pyautogui.hotkey('altleft', 'space', 'x') # maximises file browser window
		Texter.openfilewindow(file_doc, doc_file_path)	
                   #-----Attachment controls-----#

	def keyboardcontrol(content):
		pyautogui.typewrite(content, 0.25)

	def mousecontrol(receiver, text):
		receiver = receiver
		text = text
		time.sleep(15) # waits for WhatsApp to load
		# pyautogui.moveTo(97, 134, duration = 0.25) # moves cursor to search bar
		pyautogui.click(97, 134) # clicks on search bar
		Texter.keyboardcontrol(receiver) # sends name

		# pyautogui.moveTo(118, 295, duration = 0.25) # moves cursor to search result
		pyautogui.click(118, 295) # clicks on search result

		# pyautogui.moveTo(680, 990, duration = 0.25) # moves cursor to message bar
		pyautogui.click(680, 990) # clicks on message bar
		Texter.keyboardcontrol(text) # types text

		# pyautogui.moveTo(1886, 996, duration = 0.25) # moves cursor to send button
		pyautogui.click(1886, 996) # clicks on send button

		if img_CBisClicked == True: # checks if img checkbox was clicked
			Texter.img_func()
		if vid_CBisClicked == True: # checks if vid checkbox was clicked
			Texter.vid_func()
		if doc_CBisClicked == True: # checks if doc checkbox was clicked
			Texter.doc_func()
		else:
			pass # do nothing
			
if __name__ == '__main__':                   #-----------> program execution starts here 
	img_file_path = '' # global variable
	vid_file_path = '' # global variable
	doc_file_path = '' # global variable
	file_img = '' # global variable
	file_vid = '' # global variable
	file_doc = '' # global variable
	App.main()