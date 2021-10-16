
#https://github.com/chandrikadeb7/Face-Mask-Detection   ----------   for face-mask_detection model
import csv
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from tkcalendar import *
import datetime
from datetime import date
from  datetime import datetime
from tkinter import *
from tkinter.ttk import *
from numpy import *
import threading
from tkinter import messagebox
import socket
import pymysql
import pyttsx3
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model
from imutils.video import VideoStream
import numpy as np
import imutils
import cv2
import cv2 as cv
root = Tk()
root.title('Smart Monitoring Software')
class login_page(object):
    def login(self, master):
        self.master = master

        self.Top = Frame(self.master, height=1200)
        self.Top.pack(fill=X)

        self.username_entry = Entry(self.Top)
        self.username_entry.place(x=340, y=255, width=200, height=25)
        self.username_entry.insert(0, 'Enter the username')

        self.username_entry.bind('<FocusIn>', self.on_entry_click1)
        self.username_entry.bind('<FocusOut>', self.on_focusout1)

        self.password_entry = Entry(self.Top)
        self.password_entry.place(x=340, y=310, width=200, height=25)
        self.password_entry.insert(0, 'Enter the password')

        self.password_entry.bind('<FocusIn>', self.on_entry_click2)
        self.password_entry.bind('<FocusOut>', self.on_focusout2)

        self.logbtn = Button(self.Top, text="Login", width=22, command=lambda: self.login_btn_clicked())
        self.logbtn.place(x=370, y=380)

        self.admin_regitration_btn = Button(self.Top, text="Register", width=22, command=lambda: self.admin_regitration_fun())
        self.admin_regitration_btn.place(x=220, y=380)

        self.master.resizable(False, False)
        self.master.geometry("900x600+300+50")
        self.master.mainloop()

    def on_entry_click1(event, master):
        if event.username_entry.get() == 'Enter the username':
            event.username_entry.delete(0, "end")  # delete all the text in the entry
            event.username_entry.insert(0, '')  # Insert blank for user input
            # event.username_entry.config(fg='black')

    def on_focusout1(event, master):
        if event.username_entry.get() == '':
            event.username_entry.insert(0, 'Enter the username')
            # event.username_entry.config(fg='grey')

    def on_entry_click2(event, master):
        if event.password_entry.get() == 'Enter the password':
            event.password_entry.delete(0, "end")  # delete all the text in the entry
            event.password_entry.insert(0, '')  # Insert blank for user input
            # event.password_entry.config(fg='black')

    def on_focusout2(event, master):
        if event.password_entry.get() == '':
            event.password_entry.insert(0, 'Enter the password')
            # event.password_entry.config(fg='grey')

    def is_connected(self):
        try:
            socket.create_connection(("1.1.1.1", 53))
            return True
        except OSError:
            pass
        return False

    def my_message(self, my_message):
        try:
            engine = pyttsx3.init()
            rate = engine.getProperty('rate')
            engine.setProperty('rate', rate - 50)
            engine.say('{}'.format(my_message))
            engine.runAndWait()
        except:
            print('Faield to execute my_message function ! ')

    def admin_regitration_fun(self):
        self.master.destroy()
        root11 = Tk()
        root11.title('Smart Monitoring Software')
        obj11=admin_registration_page()
        obj11.admin_registration_page_fun(root11)
    def login_btn_clicked(self):
        if (self.is_connected()):
            db = pymysql.connect(host='database-1.civi8fc04a4i.us-east-2.rds.amazonaws.com'
                                 , user='admin',

            password='keshav888'
                                 )
            mycursor = db.cursor()
            sql = "use major_project"
            mycursor.execute(sql)
            sql="select * from admin_info where sequance='1'"
            mycursor.execute(sql)
            result = list(mycursor.fetchall())
            # print(result)
            username_admin = result[0][1]
            password_admin = result[0][2]

            username = self.username_entry.get()
            password = self.password_entry.get()
            if (username == username_admin and password == password_admin):
                self.master.destroy()

                root1 = Tk()
                root1.title('Smart Monitoring Software')
                obj1 = mainlist_page()
                obj1.mainlist(root1)

            else:
                messagebox.showinfo("Error", "Wrong Username/Password")
        else:
            messagebox.showinfo("Warning", "Check Internet Connection")


# In[3]:
class mainlist_page(object):
    def mainlist(self, master3):
        self.master3 = master3

        self.Top = Frame(self.master3, height=1200)
        self.Top.pack(fill=X)

        self.registerbtn = Button(self.Top, text="Register Employee Details", width=100,
                                  command=lambda: self.register_btn_clicked())
        self.registerbtn.place(x=100, y=50)

        self.masktempbtn = Button(self.Top, text="Check Mask And Attendance", width=100,
                                  command=lambda: self.masktemp_btn_clicked())
        self.masktempbtn.place(x=100, y=120)

        self.recordbtn = Button(self.Top, text="View Employee Record", width=100,
                                command=lambda: self.record_btn_clicked())
        self.recordbtn.place(x=100, y=190)

        self.backbtn = Button(self.Top, text="Back", width=22, command=lambda: self.back())
        self.backbtn.place(x=150, y=450)

        self.master3.resizable(False, False)
        self.master3.geometry("900x600+300+50")
        self.master3.mainloop()

    def back(self):
        self.master3.destroy()
        root2 = Tk()
        root2.title('Smart Monitoring Software')
        obj2 = login_page()
        obj2.login(root2)

    def register_btn_clicked(self):
        self.master3.destroy()
        root3 = Tk()
        root3.title('Smart Monitoring Software')
        obj3 = register_page()
        obj3.register(root3)

    def masktemp_btn_clicked(self):
        self.master3.destroy()
        root3 = Tk()
        root3.title('Smart Monitoring Software')
        obj3 = rfid_page()
        obj3.rfid(root3)

    def record_btn_clicked(self):
        self.master3.destroy()
        root3 = Tk()
        root3.title('Smart Monitoring Software')
        obj3 =emp_record()
        obj3.emp_record_fun(root3)


# In[4]:


class register_page(object):
    def register(self, master1):
        self.master1 = master1

        self.Top = Frame(self.master1, height=1200)
        self.Top.pack(fill=X)

        self.name_lable = Label(self.Top, text="Enter Employee name", font='arial 15 bold', width=30)
        self.name_lable.place(x=50, y=100)
        self.name_lable_E = Entry(self.Top, width=20)
        self.name_lable_E.place(x=400, y=100)

        self.department_lable = Label(self.Top, text="Enter Department Name", font='arial 15 bold', width=30)
        self.department_lable.place(x=50, y=150)
        self.department_lable_E = Entry(self.Top, width=20)
        self.department_lable_E.place(x=400, y=150)

        self.id_lable = Label(self.Top, text="Enter  Employee ID", font='arial 15 bold', width=30)
        self.id_lable.place(x=50, y=200)
        self.id_lable_E = Entry(self.Top, width=20)
        self.id_lable_E.place(x=400, y=200)

        self.email_id_lable = Label(self.Top, text="Enter  Email ID", font='arial 15 bold', width=30)
        self.email_id_lable.place(x=50, y=250)
        self.email_id_lable_E = Entry(self.Top, width=20)
        self.email_id_lable_E.place(x=400, y=250)

        self.mobile_lable = Label(self.Top, text="Enter  Mobile No", font='arial 15 bold', width=30)
        self.mobile_lable.place(x=50, y=300)
        self.mobile_lable_E = Entry(self.Top, width=20)
        self.mobile_lable_E.place(x=400, y=300)

        self.rfid_lable = Label(self.Top, text="Enter/Scan RFID No", font='arial 15 bold', width=30)
        self.rfid_lable.place(x=50, y=350)
        self.rfid_lable_E = Entry(self.Top, width=20)
        self.rfid_lable_E.place(x=400, y=350)
       # self.rfidbtn = Button(self.Top, text="Scan", width=22, command=lambda: self.scan_btn_clicked())
        #self.rfidbtn.place(x=600, y=350)

        self.registerbtn = Button(self.Top, text="Register", width=22, command=lambda: self.register_btn_clicked())
        self.registerbtn.place(x=400, y=450)

        self.backbtn = Button(self.Top, text="Back", width=22, command=lambda: self.back())
        self.backbtn.place(x=100, y=500)
        t6 = threading.Thread(target=self.scan_btn_clicked)
        t6.start()

        # Toplevel.destroy()
        self.master1.resizable(False, False)
        self.master1.geometry("900x600+300+50")
        self.master1.mainloop()

    def back(self):
        self.master1.destroy()
        root2 = Tk()
        root2.title('Smart Monitoring Software')
        obj2 = mainlist_page()
        obj2.mainlist(root2)

    def my_message(self, my_message):
        try:

            engine = pyttsx3.init()
            rate = engine.getProperty('rate')
            engine.setProperty('rate', rate - 50)
            engine.say('{}'.format(my_message))
            engine.runAndWait()
        except:
            print('Faield to execute my_message function ! ')

    def scan_btn_clicked(self):
        self.i = 1
        while (1):
            k = str(self.rfid_lable_E.get())
            if (len(k) == 10 and self.i == 1):
                self.i = 0
            if (len(k) == 11):
                self.rfid_lable_E.delete(0, 10)
                self.i = 1

    def register_btn_clicked(self):
        name1 = str(self.name_lable_E.get())
        department1 = str(self.department_lable_E.get())
        id1 = str(self.id_lable_E.get())
        email1 = str(self.email_id_lable_E.get())
        mobile1 = str(self.mobile_lable_E.get())
        rfid1 = str(self.rfid_lable_E.get())
        if name1 and department1 and id1 and email1 and mobile1 and rfid1 != "":
            db = pymysql.connect(host='database-1.civi8fc04a4i.us-east-2.rds.amazonaws.com'
                                 , user='admin',
                                 password='keshav888'
                                 )
            mycursor = db.cursor()
            sql = "use major_project"
            mycursor.execute(sql)
            # print(rfid)
            # print(name)
            # print(department)
            # print(id1)
            # print(email)
            # print(mobile)
            # try:
            # print(rfid1)

            try:
                sql = "INSERT INTO  employee_details(rfid,name,department,employee_id,email_id,mobile_number) VALUES (%s, %s,%s,%s,%s,%s)"
                val = (rfid1, name1, department1, id1, email1, mobile1)
                mycursor.execute(sql, val)
                sql = "COMMIT"
                mycursor.execute(sql)
                messagebox.showerror("success", "Register successfully", icon='info')
            except:
                messagebox.showerror("Fail", "Enter Valid Data", icon='error')

                # t = threading.Thread(target=self.my_message, args=('Are you sure.... to Regiter',))
            # t.start()
        else:
            # t = threading.Thread(target=self.my_message, args=('please Fill The All Fields',))
            # t.start()
            messagebox.showerror("Error", "Fill The All Fields", icon='warning')

        # In[5]:


class rfid_page(object):
    def rfid(self, master4):
        #t = Tk()
        self.master4 = master4

        self.Top = Frame(self.master4, height=1200)
        self.Top.pack(fill=X)

        self.rfid_lable = Label(self.Top, text="Enter/Scan RFID Number", font='arial 15 bold', width=30)
        self.rfid_lable.place(x=300, y=50)
        self.rfid_lable_E = Entry(self.Top, width=70)
        self.rfid_lable_E.place(x=200, y=130)

        #self.rfidbtn = Button(self.Top, text="Check", width=50, command=lambda: self.rfid_btn_clicked())
        #self.rfidbtn.place(x=300, y=180)

        #self.maskbtn = Button(self.Top, text="Check Mask Wear Or Not Wear", width=100, command=lambda: self.check_mask_present_or_not())
        #self.maskbtn.place(x=120, y=150)

        self.backbtn = Button(self.Top, text="Back", width=22, command=lambda: self.back())
        self.backbtn.place(x=150, y=450)

        #button1 = Button(t, text="Button 1", command=self.rfid_btn_clicked())
        #button1.invoke()

        #self.master4.resizable(False, False)
        #self.master4.geometry("900x600+300+50")
        #self.mainloop()
        t1 = threading.Thread(target=self.rfid_btn_clicked)
        t1.start()
        self.master4.resizable(False, False)
        self.master4.geometry('800x650+350+50')
        self.master4.mainloop()

    def my_message(self,my_message):
        try:

            engine = pyttsx3.init()
            rate = engine.getProperty('rate')
            engine.setProperty('rate', rate - 50)
            engine.say('{}'.format(my_message))
            engine.runAndWait()
        except:
            print('Faield to execute my_message function ! ')


    def rfid_btn_clicked(self):
        self.i = 1
        while (1):
            k = str(self.rfid_lable_E.get())
            if (len(k) == 10 and self.i == 1):
                self.rfid_number(k)
                print(k)
                self.i = 0
            if (len(k) >= 11):
                p=len(k)
                self.rfid_lable_E.delete(0,p-1)
                self.i = 1
    def rfid_number(self,rfid):
        db = pymysql.connect(host='database-1.civi8fc04a4i.us-east-2.rds.amazonaws.com'
                             , user='admin',
                             password='keshav888'
                             )
        mycursor = db.cursor()
        sql = "use major_project"
        mycursor.execute(sql)
        sql = "select * from employee_details"
        mycursor.execute(sql)
        result = list(mycursor.fetchall())
        flag=0
        for i in result:
            if (i[0] == rfid):
                flag=1
                break
        if(flag==0):
            t3 = threading.Thread(target=self.my_message, args=('please contact with administrator.......',))
            t3.start()
        else:
            m=self.check_mask()
            if(m==2):
                t4 = threading.Thread(target=self.my_message, args=('please connect camera with system......',))
                t4.start()
            if(m==0):
                t5 = threading.Thread(target=self.my_message, args=('please wear a mask to avoid coronavirus infection......',))
                t5.start()
            if(m==1):

                today = date.today()
                date1 = today.strftime("%m/%d/%Y")
                now1 = datetime.now()
                time1 = now1.strftime("%H:%M:%S")
                rfid1=str(rfid)

                mycursor = db.cursor()
                sql = "use major_project"
                mycursor.execute(sql)
                sql = "INSERT INTO  attendance(rfid,date,time) VALUES (%s, %s,%s)"
                val = (rfid1,date1,time1)
                mycursor.execute(sql, val)
                sql = "COMMIT"
                mycursor.execute(sql)

                t6 = threading.Thread(target=self.my_message,args=('Wellcome Your Attendance successfully Recorded.............',))
                t6.start()

    def back(self):
        self.master4.destroy()
        root3 = Tk()
        root3.title('Smart Monitoring Software')
        obj2 = mainlist_page()
        obj2.mainlist(root3)

    # mask detection

    def detect_and_predict_mask(self,frame, faceNet, maskNet):
        (h, w) = frame.shape[:2]
        blob = cv2.dnn.blobFromImage(frame, 1.0, (224, 224),
                                     (104.0, 177.0, 123.0))
        faceNet.setInput(blob)
        detections = faceNet.forward()
        faces = []
        locs = []
        preds = []
        for i in range(0, detections.shape[2]):
            confidence = detections[0, 0, i, 2]
            if confidence > 0.5:
                box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
                (startX, startY, endX, endY) = box.astype("int")
                (startX, startY) = (max(0, startX), max(0, startY))
                (endX, endY) = (min(w - 1, endX), min(h - 1, endY))
                face = frame[startY:endY, startX:endX]
                face = cv2.cvtColor(face, cv2.COLOR_BGR2RGB)
                face = cv2.resize(face, (224, 224))
                face = img_to_array(face)
                face = preprocess_input(face)
                faces.append(face)
                locs.append((startX, startY, endX, endY))
        if len(faces) > 0:
            faces = np.array(faces, dtype="float32")
            preds = maskNet.predict(faces, batch_size=32)
        return (locs, preds)

    def check_camera(self,source):
        cap = cv.VideoCapture(source)
        if cap is None or not cap.isOpened():
            return 0
        else:
            return 1
    def check_mask(self):
        prototxtPath = r"C:\project\Face-Mask-Detection-master\face_detector\deploy.prototxt"
        weightsPath = r"C:\project\Face-Mask-Detection-master\face_detector\res10_300x300_ssd_iter_140000.caffemodel"
        faceNet = cv2.dnn.readNet(prototxtPath, weightsPath)
        maskNet = load_model("C:\project\Face-Mask-Detection-master\mask_detector.model")
        vs = VideoStream(src=0).start()
        mask = 0
        camera = self.check_camera(0)
        if (camera):
            frame = vs.read()
            frame = imutils.resize(frame, width=400)
            (locs, preds) =self.detect_and_predict_mask(frame, faceNet, maskNet)
            for (box, pred) in zip(locs, preds):
                (startX, startY, endX, endY) = box
                (mask, withoutMask) = pred
                label = 1 if mask > withoutMask else 0
                return label
        else:
            return 2
class admin_registration_page(object):
    def admin_registration_page_fun(self,master12):
        self.master = master12
        t = threading.Thread(target=self.my_message, args=('Wellcome Admin please Complate Your Regitration',))
        t.start()
        # self.title("Admin Regitration Page In Student Attendanced System")
        self.Top1 = Frame(self.master, height=1200)
        self.Top1.pack(fill=X)

        self.text_lable = Label(self.Top1, text="Admin Registration", font='arial 19 bold', width=30)
        self.text_lable.place(x=200, y=30)
        self.text_lable_E = Entry(self.Top1, width=20)
        self.text_lable_E.place(x=400, y=100)

        self.name_lable = Label(self.Top1, text="Enter Your name", font='arial 15 bold', width=30)
        self.name_lable.place(x=70, y=100)
        self.name_lable_E = Entry(self.Top1, width=20)
        self.name_lable_E.place(x=400, y=100)

        self.Gmail_lable = Label(self.Top1, text="Enter Your Email", font='arial 15 bold',width=30)
        self.Gmail_lable.place(x=70, y=150)
        self.Gmail_lable_E = Entry(self.Top1, width=20)
        self.Gmail_lable_E.place(x=400, y=150)

        self.mobailno_lable = Label(self.Top1, text="Enter Your Mobile No", font='arial 15 bold',width=30)
        self.mobailno_lable.place(x=70, y=200)
        self.mobailno_lable_E = Entry(self.Top1, width=20)
        self.mobailno_lable_E.place(x=400, y=200)

        self.username_lable = Label(self.Top1, text="Enter Your Username", font='arial 15 bold',width=30)
        self.username_lable.place(x=70, y=250)
        self.username_lable_E = Entry(self.Top1, width=20)
        self.username_lable_E.place(x=400, y=250)

        self.password_lable = Label(self.Top1, text="Enter Password ", font='arial 15 bold', width=30)
        self.password_lable.place(x=70, y=300)
        self.password_lable_E = Entry(self.Top1, width=20)
        self.password_lable_E.place(x=400, y=300)

        self.cpassword_lable = Label(self.Top1, text="Enter Confirm Password ", font='arial 15 bold', width=30)
        self.cpassword_lable.place(x=70, y=350)
        self.cpassword_lable_E = Entry(self.Top1, width=20)
        self.cpassword_lable_E.place(x=400, y=350)

        self.pusername_lable = Label(self.Top1, text="Enter Previous Username", font='arial 15 bold',
                                     width=30)
        self.pusername_lable.place(x=70, y=400)
        self.pusername_lable_E = Entry(self.Top1, width=20)
        self.pusername_lable_E.place(x=400, y=400)

        self.admin_Button = Button(self.Top1, text="Regiter", width=50,command=lambda: self.register())
        self.admin_Button.place(x=250, y=500)

        self.backbtn = Button(self.Top1, text="Back", width=22, command=lambda: self.back())
        self.backbtn.place(x=100, y=500)

        self.master.resizable(False, False)
        self.master.geometry('800x650+350+50')
        self.master.mainloop()

    def my_message(self, my_message):
        try:

            engine = pyttsx3.init()
            rate = engine.getProperty('rate')
            engine.setProperty('rate', rate - 50)
            engine.say('{}'.format(my_message))
            engine.runAndWait()
            # rate = engine.getProperty('rate')
        except:
            print('Faield to execute my_message function ! ')

    def is_connected(self):
        try:
            socket.create_connection(("1.1.1.1", 53))
            return True
        except OSError:
            pass
        return False
    def back(self):
        self.master.destroy()
        root2 = Tk()
        root2.title('Smart Monitoring Software')
        obj2 = login_page()
        obj2.login(root2)

    def register(self):
        name1 = self.name_lable_E.get()
        username1 = self.username_lable_E.get()
        mo_no1 = self.mobailno_lable_E.get()
        email1 = self.Gmail_lable_E.get()
        password1 = self.password_lable_E.get()
        cpassword = self.cpassword_lable_E.get()
        pusername = self.pusername_lable_E.get()

        if name1 and username1 and mo_no1 and email1 and password1 and cpassword and pusername != "":
            if password1 != cpassword:
                t = threading.Thread(target=self.my_message, args=('password Not Match',))
                t.start()
                messagebox.showinfo("Error", "passaword Not Matching")
            else:
                if (self.is_connected()):
                    db = pymysql.connect(host='database-1.civi8fc04a4i.us-east-2.rds.amazonaws.com'
                                         , user='admin',

                                         password='keshav888'
                                         )
                    mycursor = db.cursor()
                    sql = "use major_project"
                    mycursor.execute(sql)
                    sql = "SELECT * FROM admin_info WHERE  sequance ='1'"
                    mycursor.execute(sql)
                    result = list(mycursor.fetchall())
                    username_admin = result[0][1]
                    if pusername != username_admin:
                        t = threading.Thread(target=self.my_message, args=('please Enter correct previous username',))
                        t.start()
                        messagebox.showinfo("Error", "previous username incorrect")
                    else:
                        string_for_mbox = "Are sure to Register"
                        t = threading.Thread(target=self.my_message, args=('Are you sure.... to Regiter',))
                        t.start()
                        ans = messagebox.askquestion("warning", string_for_mbox)
                        if ans == 'yes':
                            mycursor = db.cursor()
                            sql = "DELETE FROM admin_info WHERE  sequance = '1'"
                            mycursor.execute(sql)
                            sql = "COMMIT"
                            mycursor.execute(sql)

                            mycursor = db.cursor()
                            sequence="1"
                            sql = "INSERT INTO admin_info(sequance,username,password,name,email,mobail_no ) VALUES (%s, %s,%s,%s,%s,%s)"
                            val = (sequence,username1, password1, name1, email1, mo_no1)
                            mycursor.execute(sql, val)
                            sql = "COMMIT"
                            mycursor.execute(sql)

                            t = threading.Thread(target=self.my_message, args=('Regitration successFully completed',))
                            t.start()
                            messagebox.showinfo("success", "Register")
                else:
                    t = threading.Thread(target=self.my_message, args=('Check Internet connnection',))
                    t.start()
                    messagebox.showinfo("Error","Check Internet")
        else:
            t = threading.Thread(target=self.my_message, args=('please fill all fields',))
            t.start()
            messagebox.showinfo("warning", "please fill all fields")


class emp_record(object):
    def emp_record_fun(self, master):
        self.master = master

        self.Top1 = Frame(self.master, height=1200)
        self.Top1.pack(fill=X)

        self.backbtn1 = Button(self.Top1, text="Single Employee Record", width=80, command=lambda: self.fun1())
        self.backbtn1.place(x=150, y=50)

        self.backbtn1 = Button(self.Top1, text="Multiple Employees  Record", width=80, command=lambda: self.fun2())
        self.backbtn1.place(x=150, y=150)

        self.backbtn = Button(self.Top1, text="Back", width=22, command=lambda: self.back())
        self.backbtn.place(x=150, y=450)

        master.geometry("800x650+350+50")
        master.resizable(False, False)
        master.mainloop()

    def back(self):
        self.master.destroy()
        root41 = Tk()
        root41.title('Smart Monitoring Software')
        obj4 = mainlist_page()
        obj4.mainlist(root41)

    def fun1(self):
        self.master.destroy()
        root31 = Tk()
        root31.title('Smart Monitoring Software')
        obj21 = single_emp()
        obj21.single_emp_fun(root31)

    def fun2(self):
        self.master.destroy()
        root31 = Tk()
        root31.title('Smart Monitoring Software')
        obj21 = multiple_emp()
        obj21.multiple_emp_fun(root31)


class single_emp(object):
    def single_emp_fun(self, master13):
        self.master13 = master13
        self.Top = Frame(self.master13, height=1200)
        self.Top.pack(fill=X)
        self.rfid_lable = Label(self.Top, text="Enter/Scan RFID No :", font='arial 12 bold', width=30)
        self.rfid_lable.place(x=70, y=150)
        self.rfid_lable_E = Entry(self.Top, width=30)
        self.rfid_lable_E.place(x=350, y=150)

        self.date1_lable = Label(self.Top, text="Enter Date from      :", font='arial 12 bold', width=30)
        self.date1_lable.place(x=70, y=200)
        self.date1_lable_E = Entry(self.Top, width=20)
        self.date1_lable_E.place(x=350, y=200)
        self.enter_date1 = Button(self.Top, text="date", width=22, command=lambda: self.emp_date12())
        self.enter_date1.place(x=530, y=200)

        self.date2_lable = Label(self.Top, text="Enter Date To         :", font='arial 12 bold', width=30)
        self.date2_lable.place(x=70, y=250)
        self.date2_lable_E = Entry(self.Top, width=20)
        self.date2_lable_E.place(x=350, y=250)
        self.enter_date2 = Button(self.Top, text="Date", width=22, command=lambda: self.emp_date12())
        self.enter_date2.place(x=530, y=250)

        self.record_btn = Button(self.Top, text="Get Record", width=22, command=lambda: self.get_record())
        self.record_btn.place(x=330, y=400)

        self.backbtn = Button(self.Top, text="Back", width=22, command=lambda: self.back())
        self.backbtn.place(x=150, y=450)

        self.master13.resizable(False, False)
        self.master13.geometry('800x650+350+50')
        self.master13.mainloop()

    def get_record(self):
        today = date.today()
        today = today.strftime("%m/%d/%Y")
        today = str(today)
        # print(today)
        rfid = self.rfid_lable_E.get()
        db = pymysql.connect(host='database-1.civi8fc04a4i.us-east-2.rds.amazonaws.com'
                             , user='admin',
                             password='keshav888'
                             )
        mycursor = db.cursor()
        sql = "use major_project"
        mycursor.execute(sql)
        sql = "select * from employee_details"
        mycursor.execute(sql)
        result = list(mycursor.fetchall())
        flag12 = 0
        for i in result:
            if (i[0] == rfid):
                flag12 = 1
                break
        if (flag12 == 0):
            t = threading.Thread(target=self.my_message, args=('please Enter Valid data',))
            t.start()
            messagebox.showerror("Fail", "Enter Valid RFID number", icon='error')
        else:
            date1 = str(self.date1_lable_E.get())
            date2 = str(self.date2_lable_E.get())
            p1 = int(date1[6] + date1[7] + date1[8] + date1[9])
            p2 = int(date2[6] + date2[7] + date2[8] + date2[9])
            today_year = int(today[6] + today[7] + today[8] + today[9])
            today_month = int(today[0] + today[1])
            today_day = int(today[3] + today[4])
            if (p2 >= p1 and p2 <= today_year):
                p1 = int(date1[3] + date1[4])
                p2 = int(date2[3] + date2[4])
                if (p2 >= p1 and p2 <= today_day):
                    p1 = int(date1[0] + date1[1])
                    p2 = int(date2[0] + date2[1])
                    if (p2 > p1 and p2 <= today_month):
                        t = threading.Thread(target=self.my_message,
                                             args=('Are you want to share record to email Address also',))
                        t.start()
                        ans = messagebox.askquestion("warning", "Are you want to share record to email Address also")
                        if ans == 'yes':
                            db = pymysql.connect(host='database-1.civi8fc04a4i.us-east-2.rds.amazonaws.com'
                                                 , user='admin',
                                                 password='keshav888'
                                                 )
                            mycursor = db.cursor()
                            sql = "use major_project"
                            mycursor.execute(sql)
                            sql = "select * from attendance where date>%s and date<=%s"
                            val = (date1, date2)
                            mycursor.execute(sql, val)
                            result = list(mycursor.fetchall())
                            result1 = []
                            for i in result:
                                result1.append(list(i))
                            # print(result1)
                            fields = ['RFID No', 'Date', 'Time']
                            rows = result1
                            # file_no12 = 1
                            # path = 'C:\Emp Record\\' + "file" + str(file_no12) + ".csv"
                            path = 'C:\Emp Record\\' + "emp_record.csv"
                            # print(path)
                            with open(path, 'w') as f:
                                write = csv.writer(f)
                                write.writerow(fields)
                                write.writerows(rows)

                            sql = "select * from admin_info"
                            mycursor.execute(sql)
                            result = list(mycursor.fetchall())
                            admin_email_id = (result[0][4])
                            if (self.mailsent(admin_email_id) == 1):
                                t = threading.Thread(target=self.my_message, args=(
                                    'record successfully save and Successfully sent to email address',))
                                t.start()
                                messagebox.showinfo("Success", "Record Successfully Save and email sent ")
                            else:
                                messagebox.showerror("Fail", "Try again", icon='error')



                        else:
                            db = pymysql.connect(host='database-1.civi8fc04a4i.us-east-2.rds.amazonaws.com'
                                                 , user='admin',
                                                 password='keshav888'
                                                 )
                            mycursor = db.cursor()
                            sql = "use major_project"
                            mycursor.execute(sql)
                            sql = "select * from attendance where date>%s and date<=%s"
                            val = (date1, date2)
                            mycursor.execute(sql, val)
                            result = list(mycursor.fetchall())
                            result1 = []
                            for i in result:
                                result1.append(list(i))
                            # print(result1)
                            fields = ['RFID No', 'Date', 'Time']
                            rows = result1
                            file_no12 = 1
                            path = 'C:\Emp Record\\' + "file" + str(file_no12) + ".csv"
                            # print(path)
                            with open(path, 'w') as f:
                                write = csv.writer(f)
                                write.writerow(fields)
                                write.writerows(rows)
                            t = threading.Thread(target=self.my_message, args=('record successfully save',))
                            t.start()
                            messagebox.showinfo("Success", "Record Successfully Save")

                    else:
                        messagebox.showerror("Fail", "Enter Valid Date", icon='error')
                else:
                    messagebox.showerror("Fail", "Enter Valid Date", icon='error')
            else:
                messagebox.showerror("Fail", "Enter Valid Date", icon='error')

    def mailsent(self, email_admin):
        internet = self.is_internet_available()
        if (internet):
            fromaddr = "iotsmartattendance@gmail.com"
            toaddr = "shindekeshav37@gmail.com"
            msg = MIMEMultipart()

            msg['From'] = "iotsmartattendance@gmail.com"
            msg['To'] = email_admin

            # storing the subject
            msg['Subject'] = "Employee record from smart monitoring system"

            body = "Dear Admin, " \
                   "This is the Employee record file"
            msg.attach(MIMEText(body, 'plain'))
            filename = "file1.csv"

            attachment = open("C:\Emp Record\\emp_record.csv", "rb")

            p = MIMEBase('application', 'octet-stream')
            p.set_payload((attachment).read())
            encoders.encode_base64(p)
            p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
            msg.attach(p)
            s = smtplib.SMTP('smtp.gmail.com', 587)
            s.starttls()
            s.login("iotsmartattendance@gmail.com", "Project@888")
            text = msg.as_string()
            s.sendmail(fromaddr, toaddr, text)
            s.quit()
            return 1
        else:
            t = threading.Thread(target=self.my_message, args=('please check the internet connection',))
            t.start()
            messagebox.showinfo("Warnnig", "Internet connection not available")
            return 0

    def is_internet_available(self):
        try:
            socket.create_connection(("1.1.1.1", 53))
            return 1
        except OSError:
            pass
        return 0

    def my_message(self, my_message):
        try:

            engine = pyttsx3.init()
            rate = engine.getProperty('rate')
            engine.setProperty('rate', rate - 50)
            engine.say('{}'.format(my_message))
            engine.runAndWait()
            # rate = engine.getProperty('rate')
        except:
            print('Faield to execute my_message function ! ')

    def emp_date12(self):
        root3 = Tk()
        root3.title('Smart Monitoring Software')
        obj2 = emp_date()
        obj2.emp_date_fun(root3)

    def back(self):
        self.master13.destroy()
        root3 = Tk()
        root3.title('Smart Monitoring Software')
        obj2 = emp_record()
        obj2.emp_record_fun(root3)


class multiple_emp(object):
    def multiple_emp_fun(self, master14):
        self.master14 = master14
        self.Top = Frame(self.master14, height=1200)
        self.Top.pack(fill=X)
        self.date1_lable = Label(self.Top, text="Enter Date from      :", font='arial 12 bold', width=30)
        self.date1_lable.place(x=70, y=150)
        self.date1_lable_E = Entry(self.Top, width=20)
        self.date1_lable_E.place(x=350, y=150)
        self.enter_date1 = Button(self.Top, text="date", width=22, command=lambda: self.emp_date12())
        self.enter_date1.place(x=530, y=150)

        self.date2_lable = Label(self.Top, text="Enter Date To         :", font='arial 12 bold', width=30)
        self.date2_lable.place(x=70, y=250)
        self.date2_lable_E = Entry(self.Top, width=20)
        self.date2_lable_E.place(x=350, y=250)
        self.enter_date2 = Button(self.Top, text="Date", width=22, command=lambda: self.emp_date12())
        self.enter_date2.place(x=530, y=250)

        self.record_btn = Button(self.Top, text="Get Record", width=22, command=lambda: self.get_record())
        self.record_btn.place(x=330, y=400)

        self.backbtn = Button(self.Top, text="Back", width=22, command=lambda: self.back())
        self.backbtn.place(x=150, y=450)

        self.master14.resizable(False, False)
        self.master14.geometry('800x650+350+50')
        self.master14.mainloop()

    def emp_date12(self):
        root3 = Tk()
        root3.title('Smart Monitoring Software')
        obj2 = emp_date()
        obj2.emp_date_fun(root3)

    def get_record(self):
        today = date.today()
        today = today.strftime("%m/%d/%Y")
        print(today)
        today = str(today)
        date1 = str(self.date1_lable_E.get())
        date2 = str(self.date2_lable_E.get())
        p1 = int(date1[6] + date1[7] + date1[8] + date1[9])
        p2 = int(date2[6] + date2[7] + date2[8] + date2[9])
        today_year = int(today[6] + today[7] + today[8] + today[9])
        today_month = int(today[0] + today[1])
        today_day = int(today[3] + today[4])
        if (p2 >= p1 and p2 <= today_year):
            p1 = int(date1[3] + date1[4])
            p2 = int(date2[3] + date2[4])
            if (p2 >= p1 and p2 <= today_day):
                p1 = int(date1[0] + date1[1])
                p2 = int(date2[0] + date2[1])
                if (p2 > p1 and p2 <= today_month):
                    t = threading.Thread(target=self.my_message,
                                         args=('Are you want to share record to email Address also',))
                    t.start()
                    ans = messagebox.askquestion("warning", "Are you want to share record to email Address also")
                    if ans == 'yes':
                        db = pymysql.connect(host='database-1.civi8fc04a4i.us-east-2.rds.amazonaws.com'
                                             , user='admin',
                                             password='keshav888'
                                             )
                        mycursor = db.cursor()
                        sql = "use major_project"
                        mycursor.execute(sql)
                        sql = "select * from attendance where date>%s and date<=%s"
                        val = (date1, date2)
                        mycursor.execute(sql, val)
                        result = list(mycursor.fetchall())
                        result1 = []
                        for i in result:
                            result1.append(list(i))
                        # print(result1)
                        fields = ['RFID No', 'Date', 'Time']
                        rows = result1
                        # file_no12 = 1
                        # path = 'C:\Emp Record\\' + "file" + str(file_no12) + ".csv"
                        path = 'C:\Emp Record\\' + "emp_record.csv"
                        # print(path)
                        with open(path, 'w') as f:
                            write = csv.writer(f)
                            write.writerow(fields)
                            write.writerows(rows)

                        sql = "select * from admin_info"
                        mycursor.execute(sql)
                        result = list(mycursor.fetchall())
                        admin_email_id = (result[0][4])
                        if (self.mailsent(admin_email_id) == 1):
                            t = threading.Thread(target=self.my_message, args=(
                                'record successfully save and Successfully sent to email address',))
                            t.start()
                            messagebox.showinfo("Success", "Record Successfully Save and email sent ")
                        else:
                            messagebox.showerror("Fail", "Try again", icon='error')



                    else:
                        db = pymysql.connect(host='database-1.civi8fc04a4i.us-east-2.rds.amazonaws.com'
                                             , user='admin',
                                             password='keshav888'
                                             )
                        mycursor = db.cursor()
                        sql = "use major_project"
                        mycursor.execute(sql)
                        sql = "select * from attendance where date>%s and date<=%s"
                        val = (date1, date2)
                        mycursor.execute(sql, val)
                        result = list(mycursor.fetchall())
                        result1 = []
                        for i in result:
                            result1.append(list(i))
                        # print(result1)
                        fields = ['RFID No', 'Date', 'Time']
                        rows = result1
                        file_no12 = 1
                        path = 'C:\Emp Record\\' + "file" + str(file_no12) + ".csv"
                        # print(path)
                        with open(path, 'w') as f:
                            write = csv.writer(f)
                            write.writerow(fields)
                            write.writerows(rows)
                        t = threading.Thread(target=self.my_message, args=('record successfully save',))
                        t.start()
                        messagebox.showinfo("Success", "Record Successfully Save")

                else:
                    messagebox.showerror("Fail", "Enter Valid Date", icon='error')
            else:
                messagebox.showerror("Fail", "Enter Valid Date", icon='error')
        else:
            messagebox.showerror("Fail", "Enter Valid Date", icon='error')

    def my_message(self, my_message):
        try:

            engine = pyttsx3.init()
            rate = engine.getProperty('rate')
            engine.setProperty('rate', rate - 50)
            engine.say('{}'.format(my_message))
            engine.runAndWait()
            # rate = engine.getProperty('rate')
        except:
            print('Faield to execute my_message function ! ')

    def mailsent(self, email_admin):
        internet = self.is_internet_available()
        if (internet):
            fromaddr = "iotsmartattendance@gmail.com"
            toaddr = "shindekeshav37@gmail.com"
            msg = MIMEMultipart()

            msg['From'] = "iotsmartattendance@gmail.com"
            msg['To'] = email_admin

            # storing the subject
            msg['Subject'] = "Employee record from smart monitoring system"

            body = "Dear Admin, " \
                   "This is the Employee record file"
            msg.attach(MIMEText(body, 'plain'))
            filename = "file1.csv"

            attachment = open("C:\Emp Record\\emp_record.csv", "rb")

            p = MIMEBase('application', 'octet-stream')
            p.set_payload((attachment).read())
            encoders.encode_base64(p)
            p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
            msg.attach(p)
            s = smtplib.SMTP('smtp.gmail.com', 587)
            s.starttls()
            s.login("iotsmartattendance@gmail.com", "Project@888")
            text = msg.as_string()
            s.sendmail(fromaddr, toaddr, text)
            s.quit()
            return 1
        else:
            t = threading.Thread(target=self.my_message, args=('please check the internet connection',))
            t.start()
            messagebox.showinfo("Warnnig", "Internet connection not available")
            return 0

    def is_internet_available(self):
        try:
            socket.create_connection(("1.1.1.1", 53))
            return 1
        except OSError:
            pass
        return 0

    def emp_date12(self):
        root3 = Tk()
        root3.title('Smart Monitoring Software')
        obj2 = emp_date()
        obj2.emp_date_fun(root3)

    def back(self):
        self.master14.destroy()
        root3 = Tk()
        root3.title('Smart Monitoring Software')
        obj2 = emp_record()
        obj2.emp_record_fun(root3)


class emp_date(object):
    def emp_date_fun(self, master):
        self.master14 = master
        Top = Frame(self.master14, height=1200)
        Top.pack(fill=X)
        cal = Calendar(Top, selectmode="day", year=2021, month=3, day=3)
        cal.pack(pady=20)

        # Define Function to select the date
        def get_date():
            print(cal.get_date())
            self.master14.destroy()

        # Create a button to pick the date from the calendar
        button = Button(Top, text="Select the Date", command=get_date)
        button.pack(pady=20)

        # Create Label for displaying selected Date
        label = Label(Top, text="")
        label.pack(pady=20)

        self.master14.resizable(False, False)
        self.master14.geometry('300x300+750+220')
        self.master14.mainloop()
obj = login_page()
obj.login(root)
