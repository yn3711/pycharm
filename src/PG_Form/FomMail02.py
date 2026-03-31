##****************************************************************************************
##   TITLE   :  メール  / 　ビュー
##   PROJECT :
##   REMRAKS :  https://yatta47.hateblo.jp/entry/2015/04/18/232436
##****************************************************************************************

import smtplib
from email.mime.text import  MIMEText
from email.header import  Header
from email.utils import  formatdate



##////////////////////////////////////////////////
##  Class       : FomMail02
##  Base        :
##  Note        :
##////////////////////////////////////////////////
class FomEMail02:
    from_address = "sample@test.test"
    to_address   = "ynakatani3711@gmail.com"

    charset = "ISO-2022-JP"
    subject = u"メールの件名です"
    text    = u"メールの本文です"

    msg = MIMEText(text.encode(charset),"plain",charset)
    msg["Subject"] = Header(subject,charset)
    msg["From"]    = from_address
    msg["To"]      = to_address
    msg["Date"]    = formatdate(localtime=True)

    smtp = smtplib.SMTP("localhost")
    smtp.sendmail(from_address,to_address,msg.as_string())
    smtp.close()




if __name__ == "__main__":
    FomEMail02.app.run(debug=True)