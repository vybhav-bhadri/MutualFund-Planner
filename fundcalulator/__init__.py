from flask import Flask
from flask_wtf.csrf import CSRFProtect

app=Flask(__name__)

# csrf = CSRFProtect(app)
#<!-- <input type="hidden" name="csrf_token" value="{{ csrf_token() }}"/> -->

app.config['SECRET_KEY']='6e9ad540bfd3c08814f6b51f44150875'
# app.config['SESSION_COOKIE_SECURE'] = False

from fundcalulator import routes