from flask import Flask, render_template, request # Function: Flask activates this as a web-app/
#render_template: find a file called index.html - grap it´s content - so that you can return it; 
# import from the flask library (=comes with a lot of functions), 
# import request variable for the flask library, gives access to http request form webbrowser bar
# with request flask parses URL, which is cat, which is david, everything behind ? flask parse and hands it back as variable to me

# sport
import os # os (operating system) gives you access to the env variables (property files) and others, where you can store secure stuff like email addresses and passwords
from cs50 import SQL # import DB: CS50 Library, SQL Library - You have to create DB on own? - Create Table "Registrans" with Columns: id (Int), name (Text not null), sport (text not null), Primary Key (id)
from flask import Flask, redirect, render_template, request  # import from flask the Flask function itself, render_template (call all templates), request, redirect (3.0.1, or other status code, location of the browser, go here instead)
from flask_mail import Mail, Message # Libray: import Mail for sending regestriant a confirmation mail

# login
#session is new, for safty reaseons, session: global variable, so I can use it everywhere, otherhand: 
# fancy enough it is tied to the current user, so even if all of us on zoom right now, using my URL, 
# each of us is getting our own copy of a variable called "session", its implemented underneath the 
# hood by way of this cookie mechanism. Each of us, when you visit my application are getting a 
# different cookie value, that cookie value is like mapping to different hanger in the closet, so my 
# data will go on that hanger, your date will go on that hanger. the hanger is going to be where all of 
# our individual data is stored, what do we wanna store, per example: user name
# session is implemented be Flask for us, in such a way that each of us as users get our own version thereof (davon, hiervon, daraus)

from flask import Flask, redirect, render_template, request, session # every user got the own copy of session, cookie identifier
from flask_session import Session # Library which enables handstamps for app(Nesselbach), reminds the browser 
#to led user on the webpage as he logged in before, also when browser tabs where closed before (see google mail), nice cookies

#search for books
from cs50 import SQL
from flask import Flask, jsonify, render_template, request

# store
from cs50 import SQL
from flask import Flask, render_template, request


app = Flask(__name__) # Flask turn the current File into an application 
#-> webapplication who listen to Browsers requests __name__ = Variable  -> refer to the name of the current file
# bunch of initalisation step to write Python code to generate emails to registrans programmatically  
# initialise the application with this Flask function using name
# lot of setting for mailserver #os.getenw = property files = privat keep it save in a other environment (variable) or file witch it not reachable from client

#@app.route("/", methods=["GET", "POST"]) # first route for form (in index.htlm); one route supports the two method=["GET"], ["POST"]
                                  # show user the form and say hello to the user as well 
                                  # What are my routs = URL / or /search, applying one function to another/ application.py = Controller
#def index(): # Funktion, Default route
    #if request.method == "GET":
       #return render_template("index.html") # world is default value, if name has no value
    # render (grap) a template called index.html, give me a variable called name(=Davide) from application.py
    # name which I want to get from the URL, name = value which plug into templates 
    # arg = argument
    # None means variable has no value
    # move name parameter (name=request.args.get("name", "world")) to greet route
    # flask render your code and forward it to the webpage, sometimes the intentations are destroyed (see right click on webpage -view), 
    # but the browser doesn´t care
    #if request.method == "POST":
        #return render_template("greet.html", name=request.form.get("first_name", "world"))

        #checking logically in my controler code: 
        # if the method came in as get (=go ahead and just display the form)
        # if the method came in as post (= go ahead and greet the user)
        # why this work: when ever you visit a webpage (google.com, harvard.edu, yale.edu), you have always been making get request
        # every request you made had the keyword get by default (in URL) in the envelope
        # get nothing to do with forms, its the default HTTP verb that´s used, whenever you just visit any URL 
        # when you using a form, you are using get as we did first or you are using post as we did second

# delete /greet route, bc of redundancy,
@app.route("/greet", methods=["POST"]) #second route is greet route, methods=["GET"] is default, read users input in textfield and send it to webpage, for: one form (index.html) could send data to this route instead
def greet(): #function, who wil be called, when the user visits /greet, naming should be easy, that is why we call the funktion=route=greet
    return render_template("greet.html", first_name=request.args.get("first_name", "world")) #get funktion, return index.html on webpage, "TODO" return TODO on webpage
    # grap a template called greet.html and give me a variable called name or default world from greet.html
    # first_name = parameter that I passing in to my template, let me get the first_name http parameter 
    # "first_name" = http parameter that I am grapping from the URL
    # .args.get = refers to the arguments in the URL
    # if you send e-mail addresses, passwords, credit card data otherwise get

    #return render_template("greet.html", first_name=request.form.get("first_name", "world"))
    # methods=["POST"] form.get don´t remember what I typed in a from like credit cart number, Name

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        return render_template("greet.html", name=request.form.get("name", "world"))
    return render_template("index.html")


# sports

app.config["MAIL_DEFAULT_SENDER"] = os.getenv("MAIL_DEFAULT_SENDER") # Default Sender revers to default email address, or =my email= kati.rupp@...; getenv is variable is defind elsewhere in IDE or Linux system 
app.config["MAIL_PASSWORD"] = os.getenv("MAIL_PASSWORD") #lots of settings for mail server, password should also not shown, thats why we also grap it from the other env
app.config["MAIL_PORT"] = 587 #gmail let you send email on TCP Port 587
app.config["MAIL_SERVER"] = "smtp.gmail.com" #you will find that on googles documentation
app.config["MAIL_USE_TLS"] = True # TLS is a typ of encryption, enable with TRUE
app.config["MAIL_USERNAME"] = os.getenv("MAIL_USERNAME") # i dont know what user name they are taking, thats we grap this also from the env, best practise is storing secure information in env variables, not only for try out reasons use private passwords, you will send it to the server, if you run the code
mail = Mail(app) # mail variable, passing copy flask applications (=app) to a function called Mail

#REGISTRANTS = # store our registrants in a dictionary with a global CONSTANT, store name of Registrant and sport to have in computers` memory a list of all the vaild registration
# instead of the dictionary we can use a DB to store the data
#db = SQL("sqlite:///froshims.db") # Registrants go to SQL database

#in sqlite shema: CREATE TABLE registrans (id  INTEGER, name TEXT NOT NULL, sport TEXT NOT NULL, PRIMARY KEY(id))



SPORTS = [        # Variable, Capital Letters global Constant, create a list
    "Dodgeball",
    "Flag Football",
    "Soccer",
    "Volleyball",
    "Ultimate Frisbee", 
]

@app.route("/")
def index():
    return render_template("index.html", sports=SPORTS) #render a template called index.html/ Variable sports have the Value of the global Constant SPORTS, which is a list put in index template

@app.route("/register", methods=["POST"])
def register():
    email = request.form.get("email") # get users email from the form, variable name/email, actually register the registrants, not only saying it on html, activly store on server the data (name of registrants   )
    if not email:
        return render_template("error.html", message="Missing email")

    sport = request.form.get("sport") # variable sports, actually register the registrants, not only saying it on html, activly store on server the data (sport of registrants)
    if not sport:
        return render_template("error.html", message="Missing sport")

    if sport not in SPORTS: # if variable sport not in global constant SPORTS
        return render_template("error.html", message="Invalid sport") # manually typed in, sport is not on server (not in global variable, not in list)

    #REGISTRANTS[name] = sport  # keys and values, name to index into the Python dictionray and setting the value equal to sport computers memory recall using by way of this global variable called REGISTRANTS (all caps to make clear that it is a global variable) - successful restistration - register the user, i want to remember, that the registrant is registered for a given sport in the computer memory - with name and sport

    # return render_template("registrants.html", registrants=REGISTRANTS) # like with the sports variable, providing my registrants.html (template) with a variable called registrants setting it equal to the value of that global variable thereby giving my template access to that dictionary, ability to save all these registrants to a global variable

    #if not request.form.get("name") or request.form.get("sport") not in SPORTS:  # Error checking, Type Name and Sport, Sport must be in Constant SPORT (=list), if not template failure will appear
        #return render_template("failure.html") # give a failure, if typed in no name or sports
    #return
    #  render_template("success.html") #presume the registration would be succesful
# register registrans
   # db.execute("INSERT INTO registrants (name, sport) VALUES(?, ?)", name, sport) #insert name and sport in db

    message = Message("You are registered!", recipients=[email])  # send this to massage is variable, Massage is feature imported at the top of here, second Argument recipient
    mail.send(message) # dynamic generated emails to gmail, if you registered

    return render_template("succes.html")
    #return redirect("/registrants") # redirect the user to /registrants html, so that the registrants see themself and others; URL .../registrans


#@app.route("/registrants") # iterrating over table row of registrans
#def registrants():
    #registrants = db.execute("SELECT * FROM registrants") # getting back tablerows, each row is a dictonary of columns and he values there are in # query, access to all registrants from DB, registrans getting back rows of data
   # return render_template("registrants.html", registrants=registrants)  # name of variable = name want to use in template; return registrants from html, before =REGISTRANTS from veriable

# fully fledged web application, own db with sqlite, own templates dynamically generating a table on registrants template, beautify with some css or bootstrap


# Login

# some lines for documentation to configure flask_session (application)
app.config ["SESSION_PERMANENT"] = False # specificly only to library called Flask session
app.config ["SESSION_TYPE"] = "filesystem" # alternative of DB using, configure flask session use the file system (fancy for =hard drive of computer or own IDE account)
Session(app) # only boilerplate (Textbausteine), 3 lines copied from documentation for the library flask_session

# To use the flask_session Library (same for Mail Library) we need another file "requirements"
# for installation of the packages in the whole (pip)

@app.route("/")
def index():
    if not session.get("name"): # if there is no name in the session
        return redirect("/login") # send user to login
    return render_template("index.html") # otherwise go ahead and render the tmp index.html, route with funktion "index", which opens by default template "index.html"


@app.route("/login", methods=["GET", "POST"]) # POST for privacy, GET render template index, login as needed
def login():
    if request.method == "POST":  # from login form
        # Remember that user logged in
        # name = request.form.get("name") # I wanna store users name in a session, as soon we have the handstamp, it´s like a coat check (Garderrobenmarke) too, like a identifier (=number)
        # same as in ther world of webbrowsers, when you get a unique cookie (giving you a coat number), where all the code can go,
        # especially for variables, we want to remeber
        # Thanks to Flask we have access to, but really thanks to http, we have acces to this special Variable called "session" (Library see on import above) 
        # Redirect user to /
        # session ["name"] = name # use this session as dictionary in Python, add users name as "name" 
        # browser represents name of cookie, that why browser remembers me no matter if I close the tab, or log out
        # easier
        # put users name in session 
        session["name"] = request.form.get("name") # "name" = users name, put the usersname in a session (special coat hanger = identifier), the key of ["name"] and value (request.form.get("name")) of whatever the user logged
        return redirect("/")
    return render_template("login.html") # same for login route

@app.route("/logout")
def logout():
    session ["name"] = None # forget the the user logged in - simplest version= just change users name to "None"
    return redirect("/")
     

# search for books

#db = SQL("sqlite:///shows.db")

#connect postgres DB - not for Cloud PostgreSQL?
DB_HOST = ""
DB_NAME = ""
DB_USER = ""
DB_PASS = ""

import psycopg2
import psycopg2.extras

conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)

# cursor (cur) allows you to execute statements, using cursor() method on connection (conn)
#cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

# execute statements like create statements insert, select (sql statements)
# create a table 
# call the cursor and the execute methode on cursor, table name: student (2 columns: id, name)
#cur.execute("CREATE TABLE student (id SERIAL PRIMARY KEY, name VARCHAR);")

# Annthony should be in the table of db
#cur.execute("INSERT INTO student (name) VALUES(%s)", ("Anthony"))

# See all students in table of db 
#cur.execute("SELECT * FROM student;")

# View all students in Terminal
#print (cur.fetchall())

# automatically commit for us and print all students and avoid close on cursor (below)
with conn:
    with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:

        cur.execute("SELECT * FROM student;")
        print (cur.fetchall())
        # View only one student - Tupel
        # cur.execute("SELECT * FROM student WHERE id = %s;", (1,))
        # print(cur.fetchone()["name"])

        #cur.execute("INSERT INTO student (name) VALUES(%s)", ("Anthony",))


# commit methode will save anything what we run in execute
# conn.commit()

# cur.close()

conn.close()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/search")
def search():
    shows = db.execute("SELECT * FROM shows WHERE title LIKE ?", "%" + request.args.get("q") + "%") # request.args.get("q") is users search, per exp. alle movies/shows with "office" in the name, "%" = sql wildcard placeholders - zero or more characters to the left and right - thats why we getting matches with "office" at the beginning, middle and end of the  word
    #return render_template("search.html", shows=shows)
    return jsonify(shows) # json: javaScript Object Notation, standatised format for transmitting data between servers and browsers, using a very lightweight text format/ jsonify: Flask function that takes a Python list or dictionary and converts it into json format
    # returning the jsonification of the shows variable, which recall is just the rows that came back from db.exe, dictionary = object in javaScript
    # browser convert json file (only text, , [], {}) into html
    # js mutate or change dom - the document object model - the tree in memory, with js you add more nodes to that tree


# IDs, title of tv shows
# Terminal
# sqlite .schema
# CREATE TABLE shows (id INTEGER, title TEXT NOT NULL, PRIMARY KEY(id))
# infromation is send of web using python and javaScript

# store
# Configure app
app = Flask(__name__)

# Connect to database
db = SQL("sqlite:///store.db")

# Configure sessions
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app) 

@app.route("/")
def index():
    books = db.execute("SELECT * FROM books") #table "books" in db, we selecting * from books, to get me all the books
    return render_template("books.html", books=books) # rendering tamplate "books.html" and we passing in those books


@app.route("/cart", methods=["GET", "POST"])
def cart():

     # Ensure cart exists
    if "cart" not in session: # sessions run on the server
        session["cart"] = [] # initialise it to an empty list, so you can remeber what´s in your cart, same goes on on amazon

    # POST
    if request.method == "POST":
        id = request.form.get("id") # adding the ID to the books...
        if id:
            session["cart"].append(id) #...to my sessions cart key
        return redirect("/cart")

    # GET
    books = db.execute("SELECT * FROM books WHERE id IN (?)", session["cart"]) # WHERE the id of the book is IN (?) list of the books, list coming from session["cart"], using the session to store what we will call a shopping cart (Warenkorb), implemented via cookies underneath the hood, to give us the illusion of user specific variables, dictionaries, where you can store anything you want in there, so it looks like the session cart key is going to have a value equal to the IDs of a whole bunch of books/ (befor: use session to store everybodys name on a per user basis)
    return render_template("cart.html", books=books) # rendering cart.html template passing in the books from the database

# How do they go into the session?
# if the user submits the form to the cart -> if request.method == "POST":
# if the user posts to (/"cart") like i´m going to get the id that they´ve typed in, maybe if there is a id -> id = request.form.get("id")
# if id: and is there is in fact an ID and it´s not none
# session ["cart"].append(id): we appentthe cart, the ID of the book
# return redirect ("/cart"): redirect user to ("/cart")
        
# Terminal:
# open sqlite .schema
# CREATE TABLE books (id INTEGER, title TEXT NOT NULL, PRIMARY KEY(id));
# SELCT * FROM books;
# 1 Harry Potter and the Sorcrer's Stone
# ...

