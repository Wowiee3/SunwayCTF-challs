from flask import Flask, render_template, request, session, redirect, flash
from waitress import serve
import sqlite3
from hashlib import sha256
import os
import requests

app = Flask(__name__)
app.secret_key = os.urandom(32)
PORT = 5003

@app.route('/')
def index():
    if session:
        return redirect('/account')
    return render_template('index.html')

@app.route('/invite' ,methods=["GET", "POST"])
def invite():
    if session:
        return redirect('/account')
    if request.method == "GET":
        return render_template('invite.html')
        
    if request.method == "POST":
        url = "http://0.0.0.0:5003/"
        username = request.form['username']
        password = request.form['password']
        path = request.form['path']
        message = "Admin will consider it, still fixing the code"
        requests.get(url + path)
        return render_template('invite.html', message=message)

@app.route('/admin', methods=["GET"]) # to be completed, check if user has the secret code, if so then register the user to the shop.
def admin():
    if request.remote_addr == "127.0.0.1":
        return ""
    else:
        return "Under construction, only admins allowed"
            
@app.route('/register', methods=["GET"])
def register():
    if session:
        return redirect('/account')
    if request.remote_addr == "127.0.0.1":
        username = request.args.get("username", os.urandom(32))
        password = request.args.get("password", "fakepass")
        
        if len(password) < 1:
            return ""
        
        hashed = sha256(f'{password}'.encode('utf-8')).hexdigest()
        conn = sqlite3.connect("database.db")
        cur = conn.cursor()

        try:
            cur.execute(f"INSERT INTO users (username,password,balance) VALUES (?,?,?)",(username,hashed,50))
            conn.commit()
            cur.execute("SELECT id FROM users WHERE username = ?", (username,))
            user_id = cur.fetchone()[0]

            default_items = [
                (user_id, 1, 0),  
                (user_id, 2, 0), 
            ]

            cur.executemany("INSERT INTO userItems (user_id, item_id, quantity) VALUES (?, ?, ?)", default_items)
            conn.commit()
            conn.close()
            return ""
            
        except:
            conn.close()
            return ""
    else:
        message = "Only admins are allowed to register"
        return render_template('register.html', message=message)
    
@app.route('/login',methods=["GET","POST"])
def login():
    if session:
        return redirect('/account')
    if request.method == "GET":
        return render_template('login.html')
        
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        hashed = sha256(f'{password}'.encode('utf-8')).hexdigest()
        conn = sqlite3.connect("database.db")
        cur = conn.cursor()
        cur.execute(f"SELECT id, username, password FROM users WHERE username = ? AND password = ?", (username,hashed))
        user = cur.fetchone()

        if (user):
            session['user_id'] = user[0]
            session['username'] = user[1]
            return redirect(f'/account')
        
        else:
            message = "Invalid Username or Password"
            return render_template('login.html', message=message)

@app.route('/account')
def account():
    if not session:
        return redirect('/')
    
    username = session['username']
    user_id = session['user_id']
    conn = sqlite3.connect("database.db")
    cur = conn.cursor()

    cur.execute("""
        SELECT userItems.item_id, items.name, items.description, userItems.quantity
        FROM userItems
        JOIN items ON userItems.item_id = items.id
        WHERE userItems.user_id = ?
    """, str(user_id))

    data = cur.fetchall()

    return render_template('account.html', username=username, data=data)


@app.route('/shop')
def shop():
    if not session:
        return redirect('/')
    
    user_id = session['user_id']
    conn = sqlite3.connect("database.db")
    cur = conn.cursor()
    cur.execute(f"SELECT id, name, price FROM items")
    data= cur.fetchall()
    cur.execute(f"SELECT username, balance FROM users WHERE id = {user_id}")
    account = cur.fetchall()
    return render_template('shop.html', data=data, account=account)
        
@app.route('/purchase/<item_id>',methods=["GET","POST"])
def purchase(item_id):
    if request.method == "GET":
        if not session:
            return redirect('/')
        
        conn = sqlite3.connect("database.db")
        cur = conn.cursor()
        cur.execute(f"SELECT id, name, price FROM items WHERE id = ?" , (item_id))
        data= cur.fetchall()
        return render_template('purchase.html', data=data)

    if request.method == "POST":
        try:
            quantity = int(request.form['quantity'])
            user_id = str(session['user_id'])
            conn = sqlite3.connect("database.db")
            cur = conn.cursor()
            cur.execute(f"SELECT price FROM items WHERE id = ?", (item_id))
            item_price = cur.fetchone()[0]
            to_pay = (item_price * quantity)
            cur.execute(f"SELECT balance FROM users WHERE id = ?", (user_id))
            user_balance = cur.fetchone()[0]

            if (user_balance < to_pay):
                message = "Not enough balance"
                flash(message)
                return redirect(f'/purchase/{item_id}')

            else:
                new_balance = user_balance - to_pay
                cur.execute("UPDATE users SET balance = ? WHERE id = ?", (new_balance, user_id))
                cur.execute("UPDATE userItems SET quantity = quantity + ? WHERE user_id = ? AND item_id = ?", (quantity, user_id, item_id))
                conn.commit()
                message = f"Successfully Bought!"
                flash(message)
                return redirect('/account')

        except:
            message = "Error occured"
            flash(message)
            return redirect(f'/purchase/{item_id}')
    
@app.route('/logout')
def logout():
    session.pop('user_id', None)
    session.pop('username', None)
    return redirect('/')

if __name__ == '__main__':
    print(f"Server running at {PORT}", flush=True)
    serve(app, host='0.0.0.0', port=PORT)
