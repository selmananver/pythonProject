import _datetime

now=_datetime.datetime.now()
print(now.month)
print(now.strftime("%d:%m:%Y"))
x= _datetime.datetime(2020,12,4)
y= _datetime.datetime(2020,12,3)
diff =x-y
print(diff)
end =_datetime.datetime.now()
difference=end-now
print(difference)