from flask import Flask, render_template, flash, request, session

import mysql.connector
import sys

app = Flask(__name__)
app.config['DEBUG']
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'


@app.route("/")
def homepage():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1travelblockdbpy')
    cur = conn.cursor()
    cur.execute("SELECT * FROM protb  ")
    data = cur.fetchall()
    return render_template('index.html', data=data)


@app.route("/Home")
def Home():
    return render_template('index.html')


@app.route("/AdminLogin")
def DoctorLogin():
    return render_template('AdminLogin.html')


@app.route("/NewTravel")
def NewTravel():
    return render_template('NewTravel.html', )


@app.route("/TravelLogin")
def TravelLogin():
    return render_template('TravelLogin.html')


@app.route("/UserLogin")
def UserLogin():
    return render_template('UserLogin.html')


@app.route("/NewUser")
def NewUser():
    return render_template('NewUser.html')

@app.route("/NewVehicle")
def NewVehicle():
    return render_template('NewVehicle.html')
@app.route("/NewProduct")
def NewProduct():
    return render_template('NewProduct.html')


@app.route("/AdminHome")
def AdminHome():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1travelblockdbpy')
    cur = conn.cursor()
    cur.execute("SELECT * FROM regtb  ")
    data = cur.fetchall()
    return render_template('AdminHome.html', data=data)


@app.route("/AProductInfo")
def AProductInfo():
    import datetime
    date = datetime.datetime.now().strftime('%Y-%m-%d')
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1travelblockdbpy')
    cur = conn.cursor()
    cur.execute("SELECT * FROM protb   ")
    data = cur.fetchall()

    return render_template('AProductInfo.html', data=data)


@app.route("/adminlogin", methods=['GET', 'POST'])
def adminlogin():
    if request.method == 'POST':
        if request.form['uname'] == 'admin' or request.form['password'] == 'admin':

            conn = mysql.connector.connect(user='root', password='', host='localhost', database='1travelblockdbpy')
            cur = conn.cursor()
            cur.execute("SELECT * FROM regtb ")
            data = cur.fetchall()
            flash("Login successfully")
            return render_template('AdminHome.html', data=data)

        else:
            flash("UserName Or Password Incorrect!")
            return render_template('AdminLogin.html')




@app.route("/TravelApproved")
def TravelApproved():

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1travelblockdbpy')
    cur = conn.cursor()
    cur.execute("SELECT * FROM traveltb where status='waiting'   ")
    data = cur.fetchall()

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1travelblockdbpy')
    cur = conn.cursor()
    cur.execute("SELECT * FROM traveltb   where status !='waiting'   ")
    data1 = cur.fetchall()

    return render_template('TravelApproved.html', data=data,data1 =data1)


@app.route("/Approved")
def Approved():
    id = request.args.get('id')
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1travelblockdbpy')
    cursor = conn.cursor()
    cursor.execute(
        "update  traveltb set status='Approved' where username='" + id + "'")
    conn.commit()
    conn.close()

    flash('Travel   info Approved Successfully!')

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1travelblockdbpy')
    cur = conn.cursor()
    cur.execute("SELECT * FROM traveltb where status='waiting'   ")
    data = cur.fetchall()

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1travelblockdbpy')
    cur = conn.cursor()
    cur.execute("SELECT * FROM traveltb   where status !='waiting'   ")
    data1 = cur.fetchall()

    return render_template('TravelApproved.html', data=data, data1=data1)



@app.route("/newtra", methods=['GET', 'POST'])
def newtra():
    if request.method == 'POST':
        name = request.form['name']
        mobile = request.form['mobile']

        email = request.form['email']

        address = request.form['address']
        Register = request.form['Register']

        uname = request.form['uname']
        password = request.form['password']

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='1travelblockdbpy')
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO traveltb VALUES ('" + name + "','" + email + "','" + mobile + "','" + address + "','" + uname + "','" + password + "','" + Register + "','waiting')")
        conn.commit()
        conn.close()
        flash('Travel Info Register Successfully')
        return render_template('NewTravel.html')




@app.route("/ARemove")
def ARemove():
    id = request.args.get('id')
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1travelblockdbpy')
    cursor = conn.cursor()
    cursor.execute(
        "delete from protb where id='" + id + "'")
    conn.commit()
    conn.close()

    flash('Product  info Remove Successfully!')

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1travelblockdbpy')
    cur = conn.cursor()
    cur.execute("SELECT * FROM protb  ")
    data = cur.fetchall()
    return render_template('AProductInfo.html', data=data)


@app.route("/emplogin", methods=['GET', 'POST'])
def emplogin():
    if request.method == 'POST':
        username = request.form['uname']
        password = request.form['password']
        session['ename'] = request.form['uname']

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='1travelblockdbpy')
        cursor = conn.cursor()
        cursor.execute("SELECT * from traveltb where username='" + username + "' and Password='" + password + "'")
        data = cursor.fetchone()
        if data is None:

            flash('Username or Password is wrong')
            return render_template('ManufacturerLogin.html', data=data)
        else:

            status = data[7]
            if status == "Approved":
                conn = mysql.connector.connect(user='root', password='', host='localhost', database='1travelblockdbpy')
                cur = conn.cursor()
                cur.execute(
                    "SELECT * FROM traveltb where username='" + username + "' and Password='" + password + "'")
                data = cur.fetchall()
                flash("Login successfully")
                return render_template('TravelHome.html', data=data)
            else:
                flash('Approved Waiting For Admin')
                return render_template('TravelLogin.html', data=data)


@app.route("/TravelHome")
def TravelHome():
    username = session['ename']
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1travelblockdbpy')
    # cursor = conn.cursor()
    cur = conn.cursor()
    cur.execute("SELECT * FROM traveltb where username='" + username + "' ")
    data = cur.fetchall()
    return render_template('TravelHome.html', data=data)



import hmac
import hashlib
import binascii


def create_sha256_signature(key, message):
    byte_key = binascii.unhexlify(key)
    message = message.encode()
    return hmac.new(byte_key, message, hashlib.sha256).hexdigest().upper()


@app.route("/newproduct", methods=['GET', 'POST'])
def newproduct():
    if request.method == 'POST':
        import datetime
        date = datetime.datetime.now().strftime('%Y-%m-%d')
        print(date)
        tname = session['ename']
        vno = request.form['vno']
        ptype = request.form['ptype']
        price = request.form['price']
        qty = request.form['qty']
        info = request.form['info']
        gst = request.form['gst']
        source = request.form['source']
        destination = request.form['destination']

        import random
        file = request.files['file']
        fnew = random.randint(1111, 9999)
        savename = str(fnew) + ".png"
        file.save("static/upload/" + savename)

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='1travelblockdbpy')
        cursor = conn.cursor()
        cursor.execute("SELECT  *  FROM protb ")
        data = cursor.fetchone()

        if data:

            conn1 = mysql.connector.connect(user='root', password='', host='localhost', database='1travelblockdbpy')
            cursor1 = conn1.cursor()
            cursor1.execute("select max(id) from protb")
            da = cursor1.fetchone()
            if da:
                d = da[0]
                print(d)

            conn = mysql.connector.connect(user='root', password='', host='localhost', database='1travelblockdbpy')
            cursor = conn.cursor()
            cursor.execute("SELECT  *  FROM protb where  id ='" + str(d) + "'   ")
            data = cursor.fetchone()
            if data:
                hash1 = data[12]
                num1 = random.randrange(1111, 9999)
                hash2 = create_sha256_signature("E49756B4C8FAB4E48222A3E7F3B97CC3", str(num1))
                conn = mysql.connector.connect(user='root', password='', host='localhost', database='1travelblockdbpy')
                cursor = conn.cursor()
                cursor.execute(
                    "INSERT INTO  protb VALUES ('','" + vno + "','" + ptype + "','" + price + "','" + qty + "','" + info + "','" + date
                    + "','" + savename + "','" + gst + "','" + source + "','" + destination + "','"+ hash1 +"','"+ hash2+"','"+ tname +"')")
                conn.commit()
                conn.close()
        else:

            hash1 = '0'
            num1 = random.randrange(1111, 9999)
            hash2 = create_sha256_signature("E49756B4C8FAB4E48222A3E7F3B97CC3", str(num1))
            conn = mysql.connector.connect(user='root', password='', host='localhost', database='1travelblockdbpy')
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO  protb VALUES ('','" + vno + "','" + ptype + "','" + price + "','" + qty + "','" + info + "','" + date
                + "','" + savename + "','" + gst + "','" + source + "','" + destination + "','"+ hash1 +"','"+ hash2 +"','"+ tname +"')")
            conn.commit()
            conn.close()

    flash('Vehicle Register successfully')
    return render_template('NewVehicle.html')


@app.route("/EVehicleInfo")
def EVehicleInfo():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1travelblockdbpy')

    cur = conn.cursor()
    cur.execute("SELECT * FROM protb  ")
    data = cur.fetchall()
    return render_template('EVehicleInfo.html', data=data)


@app.route("/ERemove")
def ERemove():
    id = request.args.get('id')
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1travelblockdbpy')
    cursor = conn.cursor()
    cursor.execute(
        "delete from protb where id='" + id + "'")
    conn.commit()
    conn.close()

    flash('Vehicle  info Remove Successfully!')

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1travelblockdbpy')
    cur = conn.cursor()
    cur.execute("SELECT * FROM protb  ")
    data = cur.fetchall()
    return render_template('EVehicleInfo.html', data=data)


@app.route("/newuser", methods=['GET', 'POST'])
def newuser():
    if request.method == 'POST':
        name = request.form['name']
        gender = request.form['gender']
        mobile = request.form['mobile']

        email = request.form['email']

        address = request.form['address']

        uname = request.form['uname']
        password = request.form['password']

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='1travelblockdbpy')
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO regtb VALUES ('" + name + "','" + email + "','" + mobile + "','" + address + "','" + uname + "','" + password + "','" + gender + "')")
        conn.commit()
        conn.close()
        flash('User Register successfully')

    return render_template('UserLogin.html')


@app.route("/userlogin", methods=['GET', 'POST'])
def userlogin():
    if request.method == 'POST':
        username = request.form['uname']
        password = request.form['password']
        session['uname'] = request.form['uname']

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='1travelblockdbpy')
        cursor = conn.cursor()
        cursor.execute("SELECT * from regtb where username='" + username + "' and Password='" + password + "'")
        data = cursor.fetchone()
        if data is None:

            flash('Username or Password is wrong')
            return render_template('UserLogin.html')
        else:

            conn = mysql.connector.connect(user='root', password='', host='localhost', database='1travelblockdbpy')
            cur = conn.cursor()
            cur.execute("SELECT * FROM regtb where username='" + username + "' and Password='" + password + "'")
            data = cur.fetchall()
            flash("Login successfully")

            return render_template('UserHome.html', data=data)


@app.route("/Search")
def Search():
    import datetime
    date = datetime.datetime.now().strftime('%Y-%m-%d')
    print(date)
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1travelblockdbpy')
    cur = conn.cursor()
    cur.execute("SELECT * FROM protb ")
    data = cur.fetchall()

    return render_template('Search.html', data=data)


@app.route("/search", methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        source = request.form['source']
        destination = request.form['destination']

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='1travelblockdbpy')
        cur = conn.cursor()
        cur.execute("SELECT * FROM protb where  source ='" + source + "' and destination='"+  destination +"' ")
        data = cur.fetchall()

        return render_template('Search.html', data=data)





@app.route("/UserHome")
def UserHome():
    uname = session['uname']

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1travelblockdbpy')
    # cursor = conn.cursor()
    cur = conn.cursor()
    cur.execute("SELECT * FROM  regtb where username='" + uname + "'  ")
    data = cur.fetchall()

    return render_template('UserHome.html', data=data)


@app.route("/Add")
def Add():
    id = request.args.get('id')
    session['pid'] = id
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1travelblockdbpy')
    cur = conn.cursor()
    cur.execute("SELECT * FROM protb  where id='" + id + "' ")
    data = cur.fetchall()
    return render_template('AddCart.html', data=data)


@app.route("/add")
def add():
    flash('Please Login!')
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1travelblockdbpy')
    cur = conn.cursor()
    cur.execute("SELECT * FROM protb   ")
    data = cur.fetchall()
    return render_template('index.html', data=data)


@app.route("/addcart", methods=['GET', 'POST'])
def addcart():
    if request.method == 'POST':
        import datetime
        date = datetime.datetime.now().strftime('%Y-%m-%d')

        pid = session['pid']
        uname = session['uname']
        qty = request.form['qty']

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='1travelblockdbpy')
        cursor = conn.cursor()
        cursor.execute("SELECT  *  FROM protb  where  id='" + pid + "'")
        data = cursor.fetchone()

        if data:
            ProductName = data[1]
            Producttype = data[2]
            price = data[3]
            gst = data[8]
            cQty = data[4]

            Image = data[7]

        else:
            return 'No Record Found!'

        tprice = float(price) * float(qty)

        clqty = float(cQty) - float(qty)

        if clqty < 0:

            flash('Low  Product ')

            conn = mysql.connector.connect(user='root', password='', host='localhost', database='1travelblockdbpy')
            cur = conn.cursor()
            cur.execute("SELECT * FROM protb  where id='" + pid + "' ")
            data = cur.fetchall()
            return render_template('AddCart.html', data=data)

        else:

            conn = mysql.connector.connect(user='root', password='', host='localhost', database='1travelblockdbpy')
            cursor = conn.cursor()
            cursor.execute(
                "update protb set Qty='" + str(clqty) + "' where id='" + pid + "' ")
            conn.commit()
            conn.close()

            gstamount = (float(gst) / 100) * float(tprice)

            payamt = gstamount + tprice

            conn = mysql.connector.connect(user='root', password='', host='localhost', database='1travelblockdbpy')
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO carttb VALUES ('','" + uname + "','" + ProductName + "','" + Producttype + "','" + str(
                    price) + "','" + str(qty) + "','" + str(payamt) + "','" +
                Image + "','" + date + "','0','','" + gst + "')")
            conn.commit()
            conn.close()

            flash('Book   Successfully')

            conn = mysql.connector.connect(user='root', password='', host='localhost', database='1travelblockdbpy')
            cur = conn.cursor()
            cur.execute("SELECT * FROM protb  where id='" + pid + "' ")
            data = cur.fetchall()
            return render_template('AddCart.html', data=data)


@app.route("/Cart")
def Cart():
    uname = session['uname']
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1travelblockdbpy')
    cur = conn.cursor()
    cur.execute("SELECT * FROM  carttb where UserName='" + uname + "' and Status='0' ")
    data = cur.fetchall()

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1travelblockdbpy')
    cursor = conn.cursor()
    cursor.execute(
        "SELECT  sum(Qty) as qty ,sum(Tprice) as Tprice   FROM  carttb where UserName='" + uname + "' and Status='0' ")
    data1 = cursor.fetchone()
    if data1:
        tqty = data1[0]
        tprice = data1[1]
    else:
        return 'No Record Found!'

    return render_template('Cart.html', data=data, tqty=tqty, tprice=tprice)


@app.route("/RemoveCart")
def RemoveCart():
    id = request.args.get('id')

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1travelblockdbpy')
    cursor = conn.cursor()
    cursor.execute("SELECT  *  FROM carttb  where  id='" + id + "'")
    data1 = cursor.fetchone()

    if data1:
        ProductName = data1[2]
        cQty1 = data1[5]

    else:
        return 'No Record Found!'

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1travelblockdbpy')
    cursor = conn.cursor()
    cursor.execute("SELECT  *  FROM protb  where  ProductName='" + ProductName + "'")
    data2 = cursor.fetchone()

    if data2:
        cQty = data2[4]

    else:
        return 'No Record Found!'

    total = float(cQty1) + float(cQty)

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1travelblockdbpy')
    cursor = conn.cursor()
    cursor.execute(
        "update protb set Qty='" + str(total) + "' where  ProductName='" + ProductName + "' ")
    conn.commit()
    conn.close()

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1travelblockdbpy')
    cursor = conn.cursor()
    cursor.execute(
        "delete from carttb where id='" + id + "'")
    conn.commit()
    conn.close()

    flash('Product Remove Successfully!')

    uname = session['uname']
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1travelblockdbpy')
    cur = conn.cursor()
    cur.execute("SELECT * FROM  carttb where UserName='" + uname + "' and Status='0' ")
    data = cur.fetchall()

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1travelblockdbpy')
    cursor = conn.cursor()
    cursor.execute(
        "SELECT  sum(Qty) as qty ,sum(Tprice) as Tprice   FROM  carttb where UserName='" + uname + "' and Status='0' ")
    data1 = cursor.fetchone()
    if data1:
        tqty = data1[0]
        tprice = data1[1]

    return render_template('Cart.html', data=data, tqty=tqty, tprice=tprice)


@app.route("/payment", methods=['GET', 'POST'])
def payment():
    if request.method == 'POST':
        import datetime
        date = datetime.datetime.now().strftime('%Y-%m-%d')
        uname = session['uname']
        cname = request.form['cname']
        Cardno = request.form['cno']
        Cvno = request.form['cvno']

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='1travelblockdbpy')
        cursor = conn.cursor()
        cursor.execute(
            "SELECT  sum(Qty) as qty ,sum(Tprice) as Tprice   FROM  carttb where UserName='" + uname + "' and Status='0' ")
        data1 = cursor.fetchone()
        if data1:
            tqty = data1[0]
            tprice = data1[1]

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='1travelblockdbpy')
        cursor = conn.cursor()
        cursor.execute(
            "SELECT  count(*) As count  FROM booktb ")
        data = cursor.fetchone()
        if data:
            bookno = data[0]
            print(bookno)

            if bookno == 'Null' or bookno == 0:
                bookno = 1
            else:
                bookno += 1

        else:
            return 'Incorrect username / password !'

        bookno = 'BOOKID' + str(bookno)

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='1travelblockdbpy')
        cursor = conn.cursor()
        cursor.execute(
            "update   carttb set status='1',Bookid='" + bookno + "' where UserName='" + uname + "' and Status='0' ")
        conn.commit()
        conn.close()

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='1travelblockdbpy')
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO booktb VALUES ('','" + uname + "','" + bookno + "','" + str(tqty) + "','" + str(
                tprice) + "','" + cname + "','" + Cardno + "','" + Cvno + "','" + date + "')")
        conn.commit()
        conn.close()

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='1travelblockdbpy')
        cur = conn.cursor()
        cur.execute("SELECT * FROM  carttb where UserName='" + uname + "' and Status='1' ")
        data1 = cur.fetchall()

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='1travelblockdbpy')
        cur = conn.cursor()
        cur.execute("SELECT * FROM  booktb where username='" + uname + "'")
        data2 = cur.fetchall()

    return render_template('UserBook.html', data1=data1, data2=data2)


@app.route("/BookInfo")
def BookInfo():
    uname = session['uname']

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1travelblockdbpy')
    cur = conn.cursor()
    cur.execute("SELECT * FROM  carttb where UserName='" + uname + "' and Status='1' ")
    data1 = cur.fetchall()

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1travelblockdbpy')
    cur = conn.cursor()
    cur.execute("SELECT * FROM  booktb where username='" + uname + "'")
    data2 = cur.fetchall()

    return render_template('UserBook.html', data1=data1, data2=data2)


@app.route("/ASalesInfo")
def ASalesInfo():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1travelblockdbpy')
    cur = conn.cursor()
    cur.execute("SELECT * FROM  carttb where Status='1' ")
    data1 = cur.fetchall()

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1travelblockdbpy')
    cur = conn.cursor()
    cur.execute("SELECT * FROM  booktb ")
    data2 = cur.fetchall()

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1travelblockdbpy')
    cur = conn.cursor()
    cur.execute("SELECT distinct username FROM  booktb ")
    data = cur.fetchall()

    return render_template('ASalesInfo.html', data1=data1, data2=data2, data=data)


@app.route("/EBookInfo")
def EBookInfo():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1travelblockdbpy')
    cur = conn.cursor()
    cur.execute("SELECT * FROM  carttb where  Status='1' ")
    data1 = cur.fetchall()

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1travelblockdbpy')
    cur = conn.cursor()
    cur.execute("SELECT * FROM  booktb")
    data2 = cur.fetchall()

    return render_template('EBookInfo.html', data1=data1, data2=data2)


@app.route("/asale", methods=['GET', 'POST'])
def asale():
    if request.method == 'POST':
        uname = request.form['username']

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='1travelblockdbpy')
        cur = conn.cursor()
        cur.execute("SELECT * FROM  carttb where UserName='" + uname + "' and Status='1' ")
        data1 = cur.fetchall()

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='1travelblockdbpy')
        cur = conn.cursor()
        cur.execute("SELECT * FROM  booktb where username='" + uname + "'")
        data2 = cur.fetchall()

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='1travelblockdbpy')
        cur = conn.cursor()
        cur.execute("SELECT distinct username FROM  booktb ")
        data = cur.fetchall()

        return render_template('ASalesInfo.html', data1=data1, data2=data2, data=data)


@app.route("/Update")
def Update():
    uid = request.args.get('uid')
    session["uid"] = uid

    return render_template('Update.html')


@app.route("/update", methods=['GET', 'POST'])
def update():
    if request.method == 'POST':
        price = request.form['price']
        Qty = request.form['qty']
        date = request.form['date']
        mdate = request.form['date']

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='1travelblockdbpy')
        cursor = conn.cursor()
        cursor.execute(
            "update protb set price='" + price + "',Qty='" + Qty + "',exdate='" + date + "',Mdate ='" + mdate + "' where id='" +
            session[
                'uid'] + "' ")
        conn.commit()
        conn.close()

        flash('Product Info Update')

        return render_template('AProductInfo.html')


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
