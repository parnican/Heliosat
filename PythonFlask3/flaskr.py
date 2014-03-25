# -*- coding: utf-8 -*-
"""
    Flaskr
    ~~~~~~

    A microblog example application written as Flask tutorial with
    Flask and sqlite3.

    :copyright: (c) 2014 by Armin Ronacher.
    :license: BSD, see LICENSE for more details.
"""

import os, serial, datetime, Pysolar, re
from sqlite3 import dbapi2 as sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash, redirect
#import SunCalcModule


#for redirect
#reg_b = re.compile(r"(android|bb\\d+|meego).+mobile|avantgo|bada\\/|blackberry|blazer|compal|elaine|fennec|hiptop|iemobile|ip(hone|od)|iris|kindle|lge |maemo|midp|mmp|mobile.+firefox|netfront|opera m(ob|in)i|palm( os)?|phone|p(ixi|re)\\/|plucker|pocket|psp|series(4|6)0|symbian|treo|up\\.(browser|link)|vodafone|wap|windows (ce|phone)|xda|xiino", re.I|re.M)
#reg_v = re.compile(r"1207|6310|6590|3gso|4thp|50[1-6]i|770s|802s|a wa|abac|ac(er|oo|s\\-)|ai(ko|rn)|al(av|ca|co)|amoi|an(ex|ny|yw)|aptu|ar(ch|go)|as(te|us)|attw|au(di|\\-m|r |s )|avan|be(ck|ll|nq)|bi(lb|rd)|bl(ac|az)|br(e|v)w|bumb|bw\\-(n|u)|c55\\/|capi|ccwa|cdm\\-|cell|chtm|cldc|cmd\\-|co(mp|nd)|craw|da(it|ll|ng)|dbte|dc\\-s|devi|dica|dmob|do(c|p)o|ds(12|\\-d)|el(49|ai)|em(l2|ul)|er(ic|k0)|esl8|ez([4-7]0|os|wa|ze)|fetc|fly(\\-|_)|g1 u|g560|gene|gf\\-5|g\\-mo|go(\\.w|od)|gr(ad|un)|haie|hcit|hd\\-(m|p|t)|hei\\-|hi(pt|ta)|hp( i|ip)|hs\\-c|ht(c(\\-| |_|a|g|p|s|t)|tp)|hu(aw|tc)|i\\-(20|go|ma)|i230|iac( |\\-|\\/)|ibro|idea|ig01|ikom|im1k|inno|ipaq|iris|ja(t|v)a|jbro|jemu|jigs|kddi|keji|kgt( |\\/)|klon|kpt |kwc\\-|kyo(c|k)|le(no|xi)|lg( g|\\/(k|l|u)|50|54|\\-[a-w])|libw|lynx|m1\\-w|m3ga|m50\\/|ma(te|ui|xo)|mc(01|21|ca)|m\\-cr|me(rc|ri)|mi(o8|oa|ts)|mmef|mo(01|02|bi|de|do|t(\\-| |o|v)|zz)|mt(50|p1|v )|mwbp|mywa|n10[0-2]|n20[2-3]|n30(0|2)|n50(0|2|5)|n7(0(0|1)|10)|ne((c|m)\\-|on|tf|wf|wg|wt)|nok(6|i)|nzph|o2im|op(ti|wv)|oran|owg1|p800|pan(a|d|t)|pdxg|pg(13|\\-([1-8]|c))|phil|pire|pl(ay|uc)|pn\\-2|po(ck|rt|se)|prox|psio|pt\\-g|qa\\-a|qc(07|12|21|32|60|\\-[2-7]|i\\-)|qtek|r380|r600|raks|rim9|ro(ve|zo)|s55\\/|sa(ge|ma|mm|ms|ny|va)|sc(01|h\\-|oo|p\\-)|sdk\\/|se(c(\\-|0|1)|47|mc|nd|ri)|sgh\\-|shar|sie(\\-|m)|sk\\-0|sl(45|id)|sm(al|ar|b3|it|t5)|so(ft|ny)|sp(01|h\\-|v\\-|v )|sy(01|mb)|t2(18|50)|t6(00|10|18)|ta(gt|lk)|tcl\\-|tdg\\-|tel(i|m)|tim\\-|t\\-mo|to(pl|sh)|ts(70|m\\-|m3|m5)|tx\\-9|up(\\.b|g1|si)|utst|v400|v750|veri|vi(rg|te)|vk(40|5[0-3]|\\-v)|vm40|voda|vulc|vx(52|53|60|61|70|80|81|83|85|98)|w3c(\\-| )|webc|whit|wi(g |nc|nw)|wmlb|wonu|x700|yas\\-|your|zeto|zte\\-", re.I|re.M)


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
    #datum = datetime.datetime.now()
    #datum = datum.strftime('%Y-%m-%d')      
    #d = datetime.datetime.now() # create a datetime object for now
    #https://github.com/pingswept/pysolar/wiki/examples
    #datum = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M")) + str('Alt: ') + str(Pysolar.GetAltitude(48.203424, 17.298552, d)) + str(' Azimut: ') + str(Pysolar.GetAzimuth(48.203424, 17.298552, d))
    #extstr = SunCalcModule.testext()
    #return render_template('show_entries.html', entries=entries) #, extstr=extstr)
    #return render_template('index.html', entries=entries) #, extstr=extstr)
    return render_template('main.html')

@app.route('/mobile')
def openmobilepage():  
    return render_template('jq.html')

@app.route('/main')
def main():  
    return render_template('main.html')

@app.route('/coordinates')
def coordinates():  
    return render_template('coordinates.html')

@app.route('/panel')
def panelpage():  
    return render_template('panel.html')


#def process_request(self, request):
#    request.mobile = False
#    if request.META.has_key('HTTP_USER_AGENT'):
#        user_agent = request.META['HTTP_USER_AGENT']
#        b = reg_b.search(user_agent)
#        v = reg_v.search(user_agent[0:4])
#    if b or v:
#       return HttpResponseRedirect("http://detectmobilebrowser.com/mobile")




@app.route('/SunCalc', methods=['POST'])
def SunCalc():
    if not session.get('logged_in'):
        abort(401)    
    d = datetime.datetime.now() # create a datetime object for now
    mydate = request.form['MyDatetime']
    timezone = request.form['tmz']
    #https://github.com/pingswept/pysolar/wiki/examples
    datum = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M")) + str('Alt: ') + str(Pysolar.GetAltitude(48.203424, 17.298552, d)) + str(' Azimut: ') + str(Pysolar.GetAzimuth(48.203424, 17.298552, d))
    flash(timezone + mydate)
    #return redirect(url_for('show_entries'))
    return render_template('show_entries.html', datum=datum) #, extstr=extstr)



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
    return render_template('main.html', error=error)


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
    #process_request()
    init_db()    
    app.run(host, port)

