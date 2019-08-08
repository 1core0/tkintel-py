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