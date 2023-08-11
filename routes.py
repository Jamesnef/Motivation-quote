from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM entries")
    entries = cursor.fetchall()
    conn.close()
    return render_template('index.html', entries=entries)

@app.route('/add_entry', methods=['POST'])    #/add_entry link with add_entry(fuction) nên post = post request = + entries vô db
def add_entry(): #def add entry = save entry
    if request.method == 'POST':  #check if method = post or ?
        content = request.form['content']  #content = databse / rqf = data submit in form from box
        conn = sqlite3.connect('database.db')  # sqlite connect database
        cursor = conn.cursor()  #worker ahhhhhhhhh *connection with db*
        cursor.execute("INSERT INTO entries (content) VALUES (?)", (content,)) 
        conn.commit()  #save permit trong db / ko có dòng này là save temp
        conn.close()  #close connection
    return redirect('/')  



if __name__ == '__main__':
    app.run(debug=True)
