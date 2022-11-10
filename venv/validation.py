#validation only
from datetime import datetime
import re
import postcodes_uk

# 2 or 4 or 6 or 9 or 11
# def isValid_date(day,month,year):
#     if day == (31) and month == 2





def postcodeIsValid(postcode):
    postcode = postcode.upper()
    if postcode[0] == "S" and postcode[1] == "T":
        return(postcodes_uk.validate(postcode))
    else:
        return False


#this procedure validates the length of given data such as phone numbers
#the paremeters is the data, the length set, and which type of validation
def len_validation(data,length,option):
    if option == 1:
        if len(data) != length:
            return False
        else:
            return True
    elif option == 2:
        if len(data) >= length:
            return True
        else:
            return False
    elif option == 3:
        if len(data) <= length:
            return False
        else:
            return True


#this procedure validates the range of data entered
#the parameters are te data, the highest value
def range_validation(data, high, low):
    if data >= low and data <=high:
        return True
    else:
        return False

def validate_date(date_time):
    try:
        datetime.strptime(date_time, '%d/%m/%Y %I:%M %p')
        return True
    except ValueError:
        return False



def isvalidEmail(emailad):
   pat = "^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$"
   if re.match(pat,emailad):
      return True
   return False






if __name__ == "main":
    main()