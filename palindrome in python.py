def palindrome(n):
   num=str(n)
   rev_num=num[::-1]
   if(num==rev_num):
      print(f"{num}  is palindrome")
   else:
      print(f"{num} is not palindrome. ")
number=input("enter a number:")
palindrome(number)
