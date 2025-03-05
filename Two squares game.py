#Program: Two squares game.. This game is played on a board of 4 x 4 squares. Two players take turns;
#each of them takes turn to place a rectangle (that covers two squares) on the board, covering 
#any 2 squares. Only one rectangle can be on a square. A square cannot be covered twice. The 
#last player who can place a card on the board is the winner


print("================Welcome to this program================") 
print("""**** Two squares game ***""")
print( """ This game is played on a board of 4 x 4 squares. Two players take turns;
each of them takes turn to place a rectangle (that covers two squares) on the board, covering 
any 2 squares. Only one rectangle can be on a square. A square cannot be covered twice. The 
last player who can place a card on the board is the winner""")

#Design of Game
list1 = ["ــــــــــــــــــــــ"]
list2 = ["| ", 1 ," |  ", 2 ,"  |  ", 3 ,"  |  ", 4 ," |"]
list3 = ["| ", 5 ," |  ", 6 ,"  |  ", 7 ,"  |  ", 8 ," |"]
list4 = ["| ", 9 ," | ", 10 ,"  |  ", 11 ," | ", 12 ," |"]
list5 = ["| ", 13 ,"|  ", 14 ," |  ", 15 ," | ", 16 ," |"]

list = [1,2,3,4,5,6,8,7,9,10,11,12,13,14,15,16]   #list of element which user can choose from

while True:   # print Design of Game
    print("".join(map(str,list1)))
    print("".join(map(str,list2)))
    print("".join(map(str,list1)))
    print("".join(map(str,list3)))
    print("".join(map(str,list1)))
    print("".join(map(str,list4)))
    print("".join(map(str,list1)))
    print("".join(map(str,list5)))
    print("".join(map(str,list1)))
    
#player1 is turn
    while True:                               
           try:                                                              
             number1 = int(input("""player1:  please, enter  number1: """) )       #take number and check number is intger and in correct range
             if number1 in list:
               break     
             else:
              print("""invalid number,\n """)    
           except ValueError : 
             print("""invalid: \n""")

    list.remove(number1)       #remove number2 from  list of element which user can choose from

#change value of choose number to X To disappear from the user
             
    if number1 == 1:     list2[1] = 'X'
    elif number1 == 2:   list2[3] = 'X'
    elif number1 == 3:   list2[5] = 'X'
    elif number1 == 4 :  list2[7] = 'X'
    elif number1 == 5 :  list3[1] = 'X'
    elif number1 == 6 :  list3[3] = 'X'
    elif number1 == 7 :  list3[5] = 'X'
    elif number1 == 8 :  list3[7] = 'X'
    elif number1 == 9 :  list4[1] = 'X'
    elif number1 == 10 : list4[3] = 'X'
    elif number1 == 11 : list4[5] = 'X'
    elif number1 == 12 : list4[7] = 'X'
    elif number1 == 13 : list5[1] = 'X'
    elif number1 == 14 : list5[3] = 'X'
    elif number1 == 15 : list5[5] = 'X'
    elif number1 == 16 : list5[7] = 'X'
    
    while True:        #take number2 and check number is intger and in correct range and can be make a regtangle with number1                         
           try:                                                              
             number2 = int(input("player1: please, enter  number2: ") )      
             if number2 in list:
               if number1 %4 != 0 :
                  if number2 %4 != 0 :
                     if (number2 == (number1 - 1)) or (number2 == (number1 + 1)) or (number2 == (number1 + 4)) or (number2 == (number1 - 4)) :
                        break     
                     else:
                      print("""invalid number\n""")  
                  elif number2 %4 == 0 :
                     if (number2 == (number1 + 1))  or (number2 == (number1 + 4)) or (number2 == (number1 - 4)) :
                      break     
                     else:
                      print("""invalid number \n""")
               else :
                     if number2 == number1 +1 :
                         print("""invalid number \n""") 
                     else:
                        break   
             else:
                    print("""invalid number \n""")   
           except ValueError : 
             print("""invalid,\n""")
             
    list.remove(number2)  #remove number2 from  list of element which user can choose from

    if number2 == 1:      list2[1] = 'X'
    elif number2 == 2:    list2[3] = 'X'
    elif number2 == 3:    list2[5] = 'X'
    elif number2 == 4 :   list2[7] = 'X'
    elif number2 == 5 :   list3[1] = 'X'
    elif number2 == 6 :   list3[3] = 'X'
    elif number2 == 7 :   list3[5] = 'X'
    elif number2 == 8 :   list3[7] = 'X'
    elif number2 == 9 :   list4[1] = 'X'
    elif number2 == 10 :  list4[3] = 'X'
    elif number2 == 11 :  list4[5] = 'X'
    elif number2 == 12 :  list4[7] = 'X'
    elif number2 == 13 :  list5[1] = 'X'
    elif number2 == 14 :  list5[3] = 'X'
    elif number2 == 15 :  list5[5] = 'X'
    elif number2 == 16 :  list5[7] = 'X'
    
    if list == []:   #check if player winned
            print("player2 is winning")
            print(" End Game ")
            exit() 
            
    for i in list:  #check if player winned
      if i and ((i+1) or (i-1) or (i+4) or (i-4)) in list:      
         break
      elif i in range (len(list)):
        continue    
      else:
       print("player1 is winning")
       print(" End Game ")
       exit() 

#Print development in game form
       
    print("".join(map(str,list1)))
    print("".join(map(str,list2)))
    print("".join(map(str,list1)))
    print("".join(map(str,list3)))
    print("".join(map(str,list1)))
    print("".join(map(str,list4)))
    print("".join(map(str,list1)))
    print("".join(map(str,list5)))
    print("".join(map(str,list1)))

#player2 is turn
    while True:                               
           try:                                                              
             number1 = int(input("""player2: please, enter  number1: """) )       #check number is intger and in correct range
             if number1 in list:
               break     
             else:
              print("""invalid number, \n""")    
           except ValueError : 
             print("""invalid: \n""")
    list.remove(number1)

    if number1 == 1:     list2[1] = 'X'
    elif number1 == 2:   list2[3] = 'X'
    elif number1 == 3:   list2[5] = 'X'
    elif number1 == 4 :  list2[7] = 'X'
    elif number1 == 5 :  list3[1] = 'X'
    elif number1 == 6 :  list3[3] = 'X'
    elif number1 == 7 :  list3[5] = 'X'
    elif number1 == 8 :  list3[7] = 'X'
    elif number1 == 9 :  list4[1] = 'X'
    elif number1 == 10 : list4[3] = 'X'
    elif number1 == 11 : list4[5] = 'X'
    elif number1 == 12 : list4[7] = 'X'
    elif number1 == 13 : list5[1] = 'X'
    elif number1 == 14 : list5[3] = 'X'
    elif number1 == 15 : list5[5] = 'X'
    elif number1 == 16 : list5[7] = 'X'
    
    while True:                               
           try:                                                              
             number2 = int(input("player2: please, enter  number2: ") )       #check number is intger and in correct range
             if number2 in list:
               if number1 % 4 != 0 :
                  if number2 % 4 != 0 :
                     if (number2 == (number1 - 1)) or (number2 == (number1 + 1)) or (number2 == (number1 + 4)) or (number2 == (number1 - 4)) :
                        break     
                     else:
                      print("""invalid number\n""")  
                  elif number2 % 4 == 0 :
                     if (number2 == (number1 + 1))  or (number2 == (number1 + 4)) or (number2 == (number1 - 4)) :
                      break     
                     else:
                      print("""invalid number \n""")
               else :
                     if number2 == number1 + 1 :
                         print("""invalid number \n""") 
                     else:
                        break   
             else:
                    print("""invalid number \n""")   
           except ValueError : 
             print("""invalid,\n""")
   
             
    list.remove(number2)

    if number2 == 1:     list2[1] = 'X'
    elif number2 == 2:   list2[3] = 'X'
    elif number2 == 3:   list2[5] = 'X'
    elif number2 == 4 :  list2[7] = 'X'
    elif number2 == 5 :  list3[1] = 'X'
    elif number2 == 6 :  list3[3] = 'X'
    elif number2 == 7 :  list3[5] = 'X'
    elif number2 == 8 :  list3[7] = 'X'
    elif number2 == 9 :  list4[1] = 'X'
    elif number2 == 10 : list4[3] = 'X'
    elif number2 == 11 : list4[5] = 'X'
    elif number2 == 12 : list4[7] = 'X'
    elif number2 == 13 : list5[1] = 'X'
    elif number2 == 14 : list5[3] = 'X'
    elif number2 == 15 : list5[5] = 'X'
    elif number2 == 16 : list5[7] = 'X'
    
    if list == []:
            print("player2 is winning")
            print(" End Game ")
            exit() 

    for i in list:
       if i and ((i + 1) or (i - 1) or (i + 4) or (i - 4)) in list:      
           break    
       
       elif i in range (len(list)):
          continue     
       else:
         print("player2 is winning")
         print(" End Game ")
         exit() 