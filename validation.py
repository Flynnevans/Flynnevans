#validation only
from datetime import datetime
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





if __name__ == "main":
    main()