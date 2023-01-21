# while loop and for loop 

# x=1
# while (x<5):
#     print(x)
#     x=x+1    <--this condition is compulsory otherwise loop will never stop

# for loop 

weekdays=("mon","tue","wed","thurs","fri","sat","sun")
for i in weekdays:
    # if i=="fri":break    loop stops
     if i=="fri":continue   #skips fri 
    print(i)