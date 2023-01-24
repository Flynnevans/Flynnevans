import sqlite3

def UpdateTable():
    # here wil will show how to update a record in the table Deprtements.

    DeptNo = int(input("Which department you want to update/ Enter Dept ID   "))
    NewPhoneNumber = input("Enter new number ")

    conn = sqlite3.connect('CompanyStaff.db')
    conn.execute('''UPDATE DEPARTMENTS  SET Telephone = ? WHERE DEp_ID = ? ''', (NewPhoneNumber, DeptNo))
    conn.commit()
    conn.close()