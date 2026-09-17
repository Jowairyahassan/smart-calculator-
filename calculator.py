# simple smart calculator 
print ("=== simple calculator ===')

       # Take numbers from user
       num1 = float(input("Enter first number: "))
       num2 = float(input("Enter second number:"))
    #choose operation 
 print("1. Add (+)")
 print("2. subtract (-)")
 choice = input('Enter choice (1 or 2): ")

    if choice == '1':
                result = num1 + num2 
                print ("The Result is:", result )
elif choice == '2':
     result = num1 - num2
print (" The Result is:", result)
else:
   print ("Invalid choice!")
  
