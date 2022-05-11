#login only
namebank = []
passwordbank[]

def new_users(newname,newpassword):
    namebank = []
    passwordbank[]
    namebank.append(newname)
    passwordbank.append(newpassword)



def admin_validation(username, password):
    if username == "admin123":
        if password == ("secret123"):
            return True
        else:
            return False
    else:
        return False






def username_validation(username, password):
    if username in namebank:
        if password == passwordbank[(namebank.index(username))]:
            return True
        else:
            return False
    else:
        return False








if __name__ == "main":
    main()

