a=int(input("Enter a year:"))

if (a%4) == 0:
   if (a%100) == 0:
       if (a%400) == 0:
           print(a,"is a leap year")
           print("There are 366 days. You have 1 day extra to bring colour in your life.")
       else:
           print(a,"is not a leap year")
           print("There are 365 days and a century has been completed.")
   else:
       print(a,"is a leap year")
       print("There are 366 days. You have 1 day extra to bring colour in your life.")
else:
   print(a,"is not a leap year")
   print("There are 365 days.")
