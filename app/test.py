import pymysql as MySQLdb
import cv2
import time
from flask import Flask, render_template, Response
from camera import VideoCamera
from threading import Thread, Lock


mutex=Lock()
fr=0
obj=0
cursor=''
con=''
check=True
fc=[]
def check_db():
    global check
    global cursor
    global con
    while check:
        try:
            con=MySQLdb.connect(host="db",port=3306,user="surya",password="admin",database='BOOKINFO')
            cursor=con.cursor()
            cursor.execute('CREATE TABLE IF NOT EXISTS faces(time datetime,count int);')
            con.commit()
            cursor.execute("INSERT INTO faces(time,count) VALUES (NOW(),5);")
            con.commit()
            print("connected to db successfully")
            check=False
        except:
            print("no db connection")
            time.sleep(10)
            pass

app = Flask(__name__)
@app.route('/')
def index():
    # rendering webpage
    return render_template('index.html')


def insert_to_db(q,c):
    global mutex
    global cursor
    global con
    mutex.acquire()
    print(c)
    cursor.execute(q,(int(c)))
    con.commit()
    mutex.release()
    
def gen(camera):
    global check
    global fc
    while not check:
        #get camera frame
        frame,l= camera.get_frame()
        sql = "INSERT INTO `faces` (`time`,`count`) VALUES (NOW(),%s)"
        if l>0:
            th=Thread(target=insert_to_db,args=(sql,l))
            th.start()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
@app.route('/video_feed')
def video_feed():
    global obj
    if obj==0:
        obj=VideoCamera()
    return Response(gen(obj),
                    mimetype='multipart/x-mixed-replace; boundary=frame')
if __name__ == '__main__':
    # defining server ip address and port
    check_db()
    app.run(host='0.0.0.0',port='5000', debug=True)

