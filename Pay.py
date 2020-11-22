hours=input('Enter the Total Number of Hours ')
rate=input('Enter the rate for an hour ')
pay=float(hours)*float(rate) #We have to include float as if we multiply hrs*rate it would be strng to strng mulitplication
print('You have to pay: ', int(pay))