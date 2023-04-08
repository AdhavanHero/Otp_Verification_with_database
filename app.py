from flask import Flask, render_template,request,redirect
from flask_mail import Mail, Message
import random
import requests

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] ='Superhero8871@gmail.com'
app.config['MAIL_PASSWORD'] ='Enter Your app key'
app.config['MAIL_DEFAULT_SENDER'] ='Superhero8871@gmail.com'
app.config['MAIL_USE_TLS']=False  #SSL stands for Secure Sockets Layer, and is a protocol that protects communication over the internet
app.config['MAIL_USE_SSL']=True

mail = Mail(app)

otp=random.randint(100000, 999999)
email1 = 0
url = 'xano post url'

@app.route('/', methods=['GET', 'POST'])
def index():
     if request.method == 'POST':         # do something with the form data
          email = request.form['email']
          global email1  # Declare the variable as global to update its value
          email1 = email
          print(email1)
         

          msg = Message(subject='OTP', sender='Superhero8871@gmail.com', recipients=[email])
          msg.body = str(otp)
          mail.send(msg)
          print(msg)
          print(email)
          return redirect('/verify')
     return render_template('index.html')

@app.route('/verify',methods=['GET', 'POST'])
def verify():
    error = None
    if request.method == 'POST':
          user_otp = request.form['otp']
          #print(email1)


          if user_otp == str(otp):
              data = {'Mails': email1, "Verified": True}
              response = requests.post(url, json=data)
              return render_template('success.html')

          else:
              data = {'Mails': email1, "Verified": False}
              response = requests.post(url, json=data)
              error = "Invalid Credentials. Please try again."

    return render_template('verify.html',error=error)

if __name__ == '__main__':
    app.run()

#modern problem requiers modern solution lol
