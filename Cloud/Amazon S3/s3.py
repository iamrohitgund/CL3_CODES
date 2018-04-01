import Tkinter 
from Tkinter import *
import subprocess
import tkMessageBox
from subprocess import call
top = Tkinter.Tk()
def main():
	l1=Tkinter.Label(top,text="Click on a button to perform an operation:",height=3, width=34,fg="white",bg="black").pack()
	m6=Tkinter.Button(top, text ="View List of Buckets", command = view,height=2, width=20)
	m6.pack()
	m1=Tkinter.Button(top, text ="Create a Bucket", command = create,height=2, width=20)
	m1.pack()
	m7=Tkinter.Button(top, text ="View contents of a Bucket", command = contents,height=2, width=20)
	m7.pack()
	m4=Tkinter.Button(top, text ="Upload a File", command = upload,height=2, width=20)
	m4.pack()
	m3=Tkinter.Button(top, text ="Download a File", command = download,height=2, width=20)
	m3.pack()
	m5=Tkinter.Button(top, text ="Delete a File", command = delete2,height=2, width=20)
	m5.pack()
	m2=Tkinter.Button(top, text ="Delete a Bucket", command = delete1,height=2, width=20)
	m2.pack()
	m8=Tkinter.Button(top, text ="Exit", command = done,height=2, width=20)
	m8.pack()
	top.title("Menu")
	top.configure(bg='white')
	top.minsize(width=333, height=333)
	top.mainloop()
	
def back(t):
	t.destroy()
	
def create():
	 top1 = Toplevel()
	 top1.minsize(width=333, height=200)
	 top1.title('Create a bucket')
	 top1.focus_set()
	 lable=Tkinter.Label(top1,text="Enter name of bucket to be created:",height=2, width=30).pack()
	 E1=Tkinter.Entry(top1)
	 E1.pack()
	 B1 = Tkinter.Button(top1, text ="Continue", command = lambda:createBuck(top1,E1.get()),height=2, width=20) #lambda used when a func is called from a func and not from main
	 B1.pack()
	 B2 = Tkinter.Button(top1, text ="Back", command = lambda:back(top1),height=2, width=20)
	 B2.pack()

def createBuck(t,src):
	cmd="aws s3api create-bucket --bucket %s --region us-west-2"%(src)
	x = subprocess.check_output(cmd.split())
	t.destroy()
	tkMessageBox.showinfo( "Message", x)
	
def delete1():
	 top1 = Toplevel()
	 top1.minsize(width=333, height=200)
	 top1.title('Delete a bucket')
	 top1.focus_set()
	 lable=Tkinter.Label(top1,text="Enter name of bucket to be deleted:",height=2, width=30).pack()
	 E1=Tkinter.Entry(top1)
	 E1.pack()
	 B1 = Tkinter.Button(top1, text ="Continue", command = lambda:deleteBuck(top1,E1.get()),height=2, width=20)
	 B1.pack()
	 B2 = Tkinter.Button(top1, text ="Back", command = lambda:back(top1),height=2, width=20)
	 B2.pack()

def deleteBuck(t,src):
	cmd="aws s3api delete-bucket --bucket %s --region us-west-2"%(src)
	x = subprocess.check_output(cmd.split())
	cmd="aws s3 ls"
	x = subprocess.check_output(cmd.split())
	t.destroy()
	tkMessageBox.showinfo( "List of Buckets", x)
		 
def download():
	top1 = Toplevel()
	top1.minsize(width=333, height=200)
	top1.title('Download a file')
	top1.focus_set()
	lable=Tkinter.Label(top1,text="Enter path of file to be downloaded:",height=2, width=30).pack()
	E1=Tkinter.Entry(top1)
	E1.pack()
	lable1=Tkinter.Label(top1,text="Enter destination path:",height=2, width=20).pack()
	E2=Tkinter.Entry(top1)
	E2.pack()
	B1 = Tkinter.Button(top1, text ="Continue", command = lambda:downloadF(top1,E1.get(),E2.get()),height=2, width=20)
	B1.pack()
	B2 = Tkinter.Button(top1, text ="Back", command = lambda:back(top1),height=2, width=20)
	B2.pack()
 
def downloadF(t,src,dest):
	cmd="aws s3 cp s3:/%s %s"%(src,dest)
	x = subprocess.check_output(cmd.split())
	t.destroy()
	tkMessageBox.showinfo( "Message", x)
	
def upload():
	top1 = Toplevel()
	top1.minsize(width=333, height=200)
	top1.title('Upload a file')
	top1.focus_set()
	lable=Tkinter.Label(top1,text="Enter path of file to be uploaded:",height=2, width=30).pack()
	E1=Tkinter.Entry(top1)
	E1.pack()
	lable1=Tkinter.Label(top1,text="Enter destination path:",height=2, width=20).pack()
	E2=Tkinter.Entry(top1)
	E2.pack()
	B1 = Tkinter.Button(top1, text ="Continue", command = lambda:uploadF(top1,E1.get(),E2.get()),height=2, width=20)
	B1.pack()
	B2 = Tkinter.Button(top1, text ="Back", command = lambda:back(top1),height=2, width=20)
	B2.pack()
	
def uploadF(t,src,dest):
	cmd="aws s3 cp %s s3:/%s"%(src,dest)
	x = subprocess.check_output(cmd.split())
	t.destroy()
	tkMessageBox.showinfo( "Message", x)
	
def delete2():
	top1 = Toplevel()
	top1.minsize(width=333, height=200)
	top1.title('Delete a file')
	top1.focus_set()
	lable=Tkinter.Label(top1,text="Enter file path to be deleted:",height=2, width=30).pack()
	E1=Tkinter.Entry(top1)
	E1.pack()
	B1 = Tkinter.Button(top1, text ="Continue", command = lambda:deleteF(top1,E1.get()),height=2, width=20)
	B1.pack()
	B2 = Tkinter.Button(top1, text ="Back", command = lambda:back(top1),height=2, width=20)
	B2.pack()
	 
def deleteF(t,src):
	cmd="aws s3 rm s3:/%s"%(src)
	x = subprocess.check_output(cmd.split())
	t.destroy()
	tkMessageBox.showinfo( "Message", x)
	
def view():
	cmd="aws s3 ls"
	x = subprocess.check_output(cmd.split())
	tkMessageBox.showinfo( "List of Buckets", x)
	
def contents():
	top1 = Toplevel()
	top1.minsize(width=333, height=200)
	top1.title('Contents of a bucket')
	top1.focus_set()
	lable=Tkinter.Label(top1,text="Enter Bucket name:",height=2, width=20).pack()
	E1=Tkinter.Entry(top1)
	E1.pack()
	B1 = Tkinter.Button(top1, text ="Continue", command = lambda:viewBuck(top1,E1.get()),height=2, width=20)
	B1.pack()
	B2 = Tkinter.Button(top1, text ="Back", command = lambda:back(top1),height=2, width=20)
	B2.pack()

def viewBuck(t,src):
	cmd="aws s3 ls %s"%src
	x = subprocess.check_output(cmd.split())
	t.destroy()
	tkMessageBox.showinfo( "Contents of the Bucket", x)
	 
def done():
	top.destroy()
	
if __name__ == '__main__': main()
