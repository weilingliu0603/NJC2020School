from flask import *
from sqlite3 import *

app = Flask(__name__)

@app.route('/') #decorator for home page
def home():
       return render_template("index.html")

@app.route('/search', methods = ["POST"])
def search():
       data = request.form
       #retrieve values from webpage and store into data which is a dict 
       Name = data["name"]     
       Department = data["dept"]

       #assuming data is valid

       connection = connect("school.db") #connect database
       connection.execute("PRAGMA foreign_keys = ON;") #optional

       sql = """
       SELECT sch.Name, s.Name, s.Department, s.Contact, sch.Address
       FROM SCHOOL sch, STAFF s
       WHERE sch.Name LIKE ? AND s.Department = ?
       AND sch.SchoolCode = s.SchoolCode;
       """
       
       cursor = connection.execute(sql, ('%'+Name+'%', Department)).fetchall()
       connection.commit()
       connection.close()

       return render_template("search.html", cursor = cursor)
       
if __name__ == '__main__':
    app.run(port = 5678, debug = True)
    

#app.run(debug=True) #http://127.0.0.1:5000 default Python local host and port number
##@app.route('/about')
##def aboutpage():
##       return render_template("about.html")
##
##@app.errorhandler(404)
##def page_not_found(e):
##    # note that we set the 404 status explicitly
##    return render_template('404.html'), 404

