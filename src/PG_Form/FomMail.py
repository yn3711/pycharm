##****************************************************************************************
##   TITLE   :  メール  / 　ビュー
##   PROJECT :
##   REMRAKS :https://sendgrid.kke.co.jp/blog/?p=12839
##****************************************************************************************
from src.PG_Business.CtlEnployee import CtlEmployee
#from flask import *
import os
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mail import Mail, Message

##////////////////////////////////////////////////
##  Class       : FomMail
##  Base        :
##  Note        :
##////////////////////////////////////////////////
class FomEMail:

    app = Flask(__name__)
    app.config['SECRET_KEY']           = 'top-secret!'
    app.config['MAIL_SERVER']          = 'smtp.sendgrid.net'
    app.config['MAIL_PORT']            = 587
    app.config['MAIL_USE_TLS']         = True
    app.config['MAIL_USERNAME']        = 'apikey'
    app.config['MAIL_PASSWORD']        = os.environ.get('SENDGRID_API_KEY')
    app.config['MAIL_DEFAULT_SENDER']  = os.environ.get('MAIL_DEFAULT_SENDER')
    mail = Mail(app)

    ##======================================================================================
    ##  'GET', 'POST'
    ## @Return:
    ## @Note:
    ##======================================================================================
    @app.route('/', methods=['GET', 'POST'])
    def index():
        if request.method == 'POST':
            recipient = request.form['recipient']
            msg = Message('Twilio SendGrid Test Email', recipients=[recipient])
            msg.body = ('Congratulations! You have sent a test email with '
                        'Twilio SendGrid!')
            msg.html = ('<h1>Twilio SendGrid Test Email</h1>'
                        '<p>Congratulations! You have sent a test email with '
                        '<b>Twilio SendGrid</b>!</p>')
            mail.send(msg)
            flash(f'A test message was sent to {recipient}.')
            return redirect(url_for('index'))
        return render_template('index_mail.html')