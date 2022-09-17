
while True:
    
    print('Welcome to the Flarsheim Guesser!')
    print()
    print('Please think of a number between and including 1 and 100.')
    print()


    num_1 = 1
    num_2 = 2
    num_3 = 3

    while num_1 > 0:
    
        num_1 = int(input('What is the remainder when your number is divieded by 3 ?'))
    
        if num_1 >= 3:
            print('The value entered must be less than 3')
            
        elif num_1 < 0:
        
            print('The value entered must be 0 or greater')

        else:
            num_1 = 5
            break 
        
        
    while num_2 > 0:
    
        num_2 = int(input('What is the remainder when your number is divieded by 5 ?'))
    
        if num_2 >= 3:
            print('The value entered must be less than 3')
        
        elif num_1 > 0:
            print('The value entered must be 0 or greater')
            

        else:
            num_2 = -1
            break

    while num_3 > 0:
    
        num_3 = int(input('What is the remainder when your number is divieded by 7 ?'))
    
        if num_3 >= 3:
            print('The value entered must be less than 3')
        
        elif num_3 > 0:
            print('The value entered must be 0 or greater')

        else:
            num_3 = -1
            break
    
        
    break

game = True
while game:
    num = int(input('Do you want to play again? Y to continue, N to quit ==>'))
    if num == Y:
        print('Y')
            
    elif num == N:
        print('N')
        
        game = false 


        
        
print()
       


        
while num_1 != num_2:
    print(num_1 / 3)
    num_1 += num_1


#finishing the loop example 
    game = true
    while game:

        num = int(input(''))
        if num --5:
            print('')
            game = false 
        
    

