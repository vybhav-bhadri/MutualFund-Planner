from flask import Flask

app=Flask(__name__)

app.config['SECRET_KEY']='36e47e82246707aa45b6e668a89605a6'

from fundcalulator import routes