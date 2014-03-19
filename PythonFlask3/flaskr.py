# -*- coding: utf-8 -*-
"""
    Flaskr
    ~~~~~~

    A microblog example application written as Flask tutorial with
    Flask and sqlite3.

    :copyright: (c) 2014 by Armin Ronacher.
    :license: BSD, see LICENSE for more details.
"""

import os, serial, datetime
from sqlite3 import dbapi2 as sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash
#import SunCalcModule


# create our little application :)
app = Flask(__name__)

# Make the WSGI interface available at the top level so wfastcgi can get it.
#wsgi_app = app.wsgi_app

# Load default config and override config from an environment variable
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'flaskr.db'),
    DEBUG=True,
    SECRET_KEY='development key',
    USERNAME='a',
    PASSWORD='a'
))
app.config.from_envvar('FLASKR_SETTINGS', silent=True)

def connect_db():
    """Connects to the specific database."""
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv


def init_db():
    """Creates the database tables."""
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()


def get_db():
    """Opens a new database connection if there is none yet for the
    current application context.
    """
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db


@app.teardown_appcontext
def close_db(error):
    """Closes the database again at the end of the request."""
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()


@app.route('/')
def show_entries():
    db = get_db()
    cur = db.execute('select title, text from entries order by id desc')
    entries = cur.fetchall()
    datum = datetime.datetime.now()
    #datum = datum.strftime('%Y-%m-%d')      
    datum = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    #extstr = SunCalcModule.testext()
    return render_template('show_entries.html', entries=entries, datum=datum) #, extstr=extstr)


@app.route('/add', methods=['POST'])
def add_entry():
    if not session.get('logged_in'):
        abort(401)
    db = get_db()
    db.execute('insert into entries (title, text) values (?, ?)',
                 [request.form['title'], request.form['text']])
    db.commit()
    flash('New entry was successfully posted')
    return redirect(url_for('show_entries'))

@app.route('/usb', methods=['POST'])
def usbsend():
    if not session.get('logged_in'):
        abort(401)
    
    port =serial.Serial("/dev/ttyUSB1",baudrate=9600,parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE,
                bytesize=serial.EIGHTBITS,writeTimeout = 0,timeout = 10, rtscts=False,dsrdtr=False,xonxoff=False) 
    """port =serial.Serial("COM1",baudrate=9600,parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE,
                bytesize=serial.EIGHTBITS,writeTimeout = 0,timeout = 10, rtscts=False,dsrdtr=False,xonxoff=False)"""
    position=r"A0.0E45.0'\r\n"
    #A0.0E45.0' Drives in the center
    #A76.9E122.9' Max value for Azimut and Elevation -> positive angles vs. center
    #A-76.9E-32.9' Max value for Azimut and Elevation -> negative angles vs. center
    data=position
    #data=bytes([0x0c,0x80,0x09,0x00,0xf0,0xce,0x61,0x9d,0x01,0x00,0x01,0x00,0x00,0x00]) 
    port.isOpen()	
    port.write(data) 
    flash('Command sent to USB' + " " + position)
    return redirect(url_for('show_entries'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None    
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')            
            return redirect(url_for('show_entries'))
    return render_template('login.html', error=error)


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('show_entries'))


#if __name__ == '__main__':
#    init_db()
#    app.run()

#if __name__ == '__main__':
#    import os
#    host = os.environ.get('SERVER_HOST', 'localhost')
#    try:
#        port = int(os.environ.get('SERVER_PORT', '5555'))
#    except ValueError:
#        port = 5555
#    init_db()
#    app.run(host, port)



if __name__ == '__main__':
    import os
    host = os.environ.get('SERVER_HOST', '0.0.0.0')
    try:
        port = int(os.environ.get('SERVER_PORT', '80'))
    except ValueError:
        port = 80
    init_db()    
    app.run(host, port)

