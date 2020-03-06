from flask import Flask,render_template, request
from flask_mysqldb import MySQL
import os
app = Flask(__name__)





app.config["MYSQL_HOST"] = os.environ['MYSQL']
app.config["MYSQL_USER"] = os.environ['USER']
app.config["MYSQL_PASSWORD"] = os.environ['PASSWORD']
app.config["MYSQL_DB"] = os.environ['DATABASE']

mysql = MySQL(app)

@app.route('/' , methods=['GET', 'POST'])
def home():

    
    info = []
    if request.method == "POST":   
        
        details=request.form
        Top_Description=details['tname']
        Top_Size=details['tsize']
        Top_Colour=details['tc']
        WARDROBE_ID = details['wid']
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM tops")
        cur.execute("INSERT INTO tops (Top_Description, Top_Size, Top_Colour,WARDROBE_ID) VALUES (%s, %s, %s ,%s)", (Top_Description, Top_Size, Top_Colour,WARDROBE_ID))
        mysql.connection.commit()
        rows = cur.fetchall()
        cur.close()

        
        for row in rows:
            info.append(row)
        print(info)
    
        return render_template("index.html" , title="Home", info1=info)

    else:
        
        return render_template("index.html" , title="Home", info1=info)


if __name__ == "__main__":
    app.run('0.0.0.0',debug=True)
