from flask import Flask, jsonify,render_template,request,redirect,url_for
import sqlite3
import req

def format_driver(plate,driver,purp,date,dest,km,):
    return "ΕΝΤΟΛΗ ΚΙΝΗΣΗΣ-: {0},Του Αρ. Κυκ/ριας:  {1},Οδηγος: {2}, Σκοπός: {3}, Προς: {4}, Χλμ: {5}".format(date, plate, driver, purp, dest, km)


app = Flask(__name__)
app.config['DEBUG'] = True
@app.route('/showdb/<string:db>')
def showdb(db):
    conn = sqlite3.connect('nonos.db')
    c = conn.cursor()
    c.execute("SELECT * FROM {0}".format(db))
    res = c.fetchall()
    return render_template('view.html', rows=res)
    #return jsonify(res)#

@app.route('/',methods=["GET","POST"])
def index():

    if request.method == "POST":
        driver = request.form['driver']
        pinakida = request.form['nuplate']
        date = request.form['date']
        scopos = request.form['purp']
        dests = request.form['dest']
        r_from = request.form['r_from']

        km_start = request.form['km_start']
        conn = sqlite3.connect('nonos.db')
        c = conn.cursor()

        c.execute("INSERT INTO routes VALUES(?,?,?,?,?,?,?,?)",(driver, pinakida, dests, date, scopos, r_from, km_start, None))
        conn.commit()
        conn.close()
        if "sms" in request.form:
            conn = sqlite3.connect('nonos.db')
            c = conn.cursor()
            c.execute("SELECT * FROM drivers where name = ?", (driver,))
            tel = c.fetchone()
            print(tel)
            tel=tel[1]
            parser = req.TokenParser()
            req.send(parser, 'doropos_entoli_kinisis@0103.syzefxis.gov.gr', 'entkin1', tel, format_driver(pinakida, driver, date, scopos, dests, km_start))
        return redirect(url_for('index'))
    else:
        conn = sqlite3.connect('nonos.db')
        c = conn.cursor()
        c.execute("SELECT * FROM drivers order by name asc ")
        drivers = c.fetchall()
        c.execute("SELECT * FROM licen order by nuplate asc")
        licens = c.fetchall()
        c.execute("SELECT * FROM scop order by purp")
        scops = c.fetchall()
        c.execute("SELECT * FROM diadromi order by dest")
        dests = c.fetchall()
        return render_template('index.html',drivers=drivers, pinakides=licens, scoposes=scops, desteses=dests)

@app.route('/adddriver',methods=["POST",])
def adddriver():
    name = request.form['name']
    telephone = request.form['telephone']
    conn = sqlite3.connect('nonos.db')
    c = conn.cursor()
    c.execute("INSERT INTO drivers VALUES(?,?)",(name, telephone))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

@app.route('/addnuplate',methods=["POST",])
def addplate():
    nuplate = request.form['nuplate']
    conn = sqlite3.connect('nonos.db')
    c = conn.cursor()
    c.execute("INSERT INTO licen VALUES(?)",(nuplate,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

@app.route('/addpurp',methods=["POST",])
def addpurp():
    purp = request.form['purp']
    conn = sqlite3.connect('nonos.db')
    c = conn.cursor()
    c.execute("INSERT INTO scop VALUES(?)",(purp,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))


@app.route('/adddest',methods=["POST",])
def adddest():
    dest = request.form['dest']
    conn = sqlite3.connect('nonos.db')
    c = conn.cursor()
    c.execute("INSERT INTO diadromi VALUES(?)",(dest,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))


@app.route('/delete',methods = ['POST'])
def delete():
    rid = request.form['rid']
    conn = sqlite3.connect('nonos.db')
    c = conn.cursor()
    c.execute("DELETE FROM routes WHERE id=?", (rid))
    conn.commit()
    conn.close()
    return redirect(url_for('showdb',db='routes'))



app.run(host="0.0.0.0")
