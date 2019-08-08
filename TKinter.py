#!/usr/bin/python
from Tkinter import *
import MySQLdb

window = Tk()
txtLogin = Entry(window,width = 20)
txtPassword = Entry(window,width = 20)
txtNewLogin = Entry(window,width = 20)
txtNewPassword = Entry(window,width = 20)
txtEmail = Entry(window,width = 20)
txtName = Entry(window,width = 20)
txtLastName = Entry(window,width = 20)
txtFindMovie = Entry(window,width = 20)

isLogged = False


db = MySQLdb.connect(user = 'shopusr',
                     passwd = 'password', 
                     db = 'shop',
                     host ='127.0.0.1')
def convertTuple(tup): 
    str =  ''.join(tup) 
    return str


def signOutButtonClicked():
    isLogged = False 
    signedOutButton.destroy()
    signedOutText.destroy()
    
    
    
    
def signInButtonClicked():
    txt = "SELECT * FROM shop.users WHERE login='"+ txtLogin.get() + "'"+" AND" + " user_password='" + txtPassword.get() + "'"
    if(query.execute(txt)):
        isLogged = True
        login = txtLogin.get()
        signedOutText.grid(column = 0, row = 8,padx = 50)
        signedOutButton.grid(column = 1, row =8)
        
    else:
        print "FAILURE"
 

def signUpButtonClicked():
        checkEmail = "SELECT * FROM shop.users WHERE email='"+ txtEmail.get() + "'"
        checkLogin = "SELECT * FROM shop.users WHERE login='"+ txtLogin.get() + "'"
        if(query.execute(checkEmail)):
            print("Podany email jest juz zajety!")
        elif(query.execute(checkEmail)):
            print("Podany login jest juz zajety!")
        else:
            addQuery ="INSERT INTO shop.users (firstname, lastname, email, login, user_password) values ('" + txtName.get() + "','" + txtLastName.get() + "','" + txtEmail.get() + "','" + txtNewLogin.get()+"','"+txtNewPassword.get()+ "')"
            query.execute(addQuery)
            print(addQuery)
            db.commit()

def orderMovie():
    print("order")
    
    
    

def findMovieInDatabase():
    checkFilm = "SELECT title FROM shop.movies WHERE amount >=1 AND title='" + txtFindMovie.get() + "'"
    if(query.execute(checkFilm)):
        checkAmount = "SELECT amount FROM shop.movies WHERE title ='" + txtFindMovie.get() + "'"
        query.execute(checkAmount)
        row = query.fetchone()
        register = Label(window, text = "We found " + str(row) + " movies", font=("Arial Bold", 10))
        btn = Button(window, text = "Order", command = orderMovie) 
        btn.grid(column = 0, row = 16)
    else:
        register = Label(window, text="Sorry, not find the movie: ", font=("Arial Bold", 15))
    register.grid(column = 0, row = 15,padx = 50)

    
    
    
def showWindow():
    window.title("Welcome to online shop")
    window.geometry('1000x500')
    
def showLogin():
    lbl = Label(window, text="Username ", font=("Arial Bold", 15))
    lbl.grid(column = 0, row = 2)
    txtLogin.grid(column = 1, row = 2)
    
def showPassword():
    lbl = Label(window, text="Password ", font=("Arial Bold", 15))
    lbl.grid(column = 0, row = 5)
    txtPassword.grid(column = 1, row = 5)
    
def showNewLogin():
    lbl = Label(window, text="Username ", font=("Arial Bold", 15))
    lbl.grid(column = 5, row = 2)
    txtNewLogin.grid(column = 6, row = 2)
    
def showNewPassword():
    lbl = Label(window, text="Password ", font=("Arial Bold", 15))
    lbl.grid(column = 5, row = 6,padx = 0)
    txtNewPassword.grid(column = 6, row = 6,padx = 0)
  
def showEmail():
    lbl = Label(window, text="Email ", font=("Arial Bold", 15))
    lbl.grid(column = 5, row = 5,padx = 0)
    txtEmail.grid(column = 6, row = 5,padx = 0)

def showName():
    lbl = Label(window, text="Name ", font=("Arial Bold", 15))
    lbl.grid(column = 5, row = 7,padx = 0)
    txtName.grid(column = 6, row = 7,padx = 0)
    
def showLastName():
    lbl = Label(window, text="Lastname", font=("Arial Bold", 15))
    lbl.grid(column = 5, row = 8,padx = 0)
    txtLastName.grid(column = 6, row = 8,padx = 0)
    
def showLoginButton():
    btn = Button(window, text = "Sign in", command = signInButtonClicked) 
    btn.grid(column = 1, row = 6)
    
def showRegisterButton():
    btn = Button(window, text = "Sign up for shop", command = signUpButtonClicked) 
    btn.grid(column = 6, row = 9)
    
def showLogInOptions():
    lbl = Label(window, text="Sign in  ", font=("Arial Bold", 20))
    lbl.grid(column = 0, row = 0)
    showPassword()
    showLogin()
    showName()
    showLastName()
    showLoginButton()

def showRegisterOptions():
    register = Label(window, text="Sign up ", font=("Arial Bold", 20))
    register.grid(column = 5, row = 0,padx = 50)
    showNewLogin()
    showEmail()
    showNewPassword()
    showRegisterButton()


def findMovie():
    register = Label(window, text="Find movie: ", font=("Arial Bold", 15))
    register.grid(column = 0, row = 13,padx = 50)
    txtFindMovie.grid(column = 1, row = 13,padx = 50)
    btn = Button(window, text = "Find", command = findMovieInDatabase) 
    btn.grid(column = 1, row = 14)


signedOutText = Label(window, text="Signed in", font=("Arial Bold", 15))
signedOutButton = Button(window, text = "Sign out", command = signOutButtonClicked)

query = db.cursor()
showWindow()
showLogInOptions()
showRegisterOptions()
findMovie()

window.mainloop()
db.close()
