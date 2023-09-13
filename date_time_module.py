import datetime
x=datetime.datetime.now()#show current date and time
s=datetime.datetime(2018,6,7)#arrange in order
print(x)
print(s)
#strftime
# %b(month name short version)
# %B(month name fuul version)
# %m(month as a no integer)
# %y(year short version)
# %Y(yeat full version)
# %H(hour in 24 cycle))
# %I(hours in 12 cycle)
# %M(minutes)
# %p(am / pm)
x=datetime.datetime.now()
s=x.strftime("%Y")
y=x.strftime("%B")
print(x)
print(s)
print(y)