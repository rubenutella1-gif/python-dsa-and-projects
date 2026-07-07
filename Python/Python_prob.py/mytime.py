import datetime
def time():
    x=datetime.datetime.now()
    print(x.year)
    print(x.strftime("%A"))
time()    