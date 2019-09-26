import sys

game = ['[]','.','.','.','a','.','.','a','.','a','.','[***]'] #index 1-13
#         0   1   2   3   4   5   6   7   8   9   10    11        12 


grasshopper = 'G'
grasshopperfood = 'G*'
nofood = '[]'
onefood = '[*]'
twofood = '[**]'
threefood = '[***]'

game.insert(1, grasshopper)

print(*game)



while True:
    command = input('> ') #WALK L, WALK R, HOP L, HOP R, PICK UP, DROP, QUIT

    while grasshopper in game:
        x= game.index(grasshopper)
        
        if command == 'WALK R':
                if game[4] == grasshopper or game[7] == grasshopper or game[9] == grasshopper:
                    print('Arrgh!! An Ant attacked you. Game over.')
                    exit()
                elif game[11] == grasshopper:
                    pass
                else:
                    x += 1
                game.remove(grasshopper)
                game.insert(x,grasshopper)
                print(*game)
                command = input('> ')

        elif command == 'WALK L':
                if game[5] == grasshopper or game[8] == grasshopper or game[10] == grasshopper:
                    print('Arrgh!! An Ant attacked you. Game over.')
                    exit()
                elif game[1] == grasshopper:
                    pass
                else:
                    x -= 1
                game.remove(grasshopper)
                game.insert(x,grasshopper)
                print(*game)
                command = input('> ')

        elif command == 'HOP R':
                if game[3] == grasshopper or game[6] == grasshopper or game[8] == grasshopper:
                            print('Arrgh!! An Ant attacked you. Game over.')
                            exit()
                elif game[4] == grasshopper or game[7] == grasshopper or game[9] == grasshopper or game[10] == grasshopper:
                    x += 1
                elif game[11] == grasshopper:
                    pass
                else:
                    x += 2
                game.remove(grasshopper)
                game.insert(x,grasshopper)
                print(*game)
                command = input('> ')  
        
        elif command == 'HOP L':
                if game[6] == grasshopper or game[9] == grasshopper or game[11] == grasshopper:
                            print('Arrgh!! An Ant attacked you. Game over.')
                            exit()
                elif game[2] == grasshopper or game[5] == grasshopper or game[8] == grasshopper or game[10] == grasshopper:
                    x -= 1
                elif game[11] == grasshopper:
                    pass
                else:
                    x -= 2
                game.remove(grasshopper)
                game.insert(x,grasshopper)
                print(*game)
                command = input('> ')  
            
        elif command == 'PICK UP':
                if game[11] == 'G':
                    if game[12] == threefood:
                        game.remove(game[12])
                        game.insert(12,twofood)
                    elif game[12] == twofood:
                        game.remove(game[12])
                        game.insert(12,onefood)
                    elif game[12] == onefood:
                        game.remove(game[12])
                        game.insert(12,nofood)
                    game.remove(grasshopper)
                    game.insert(11,grasshopperfood)
                    print(*game)
                    command = input('> ')
                    continue
                    
                elif game[11] != grasshopper:
                    print('Cannot pick up food')
                    command = input('> ')
        
        elif command == 'DROP':
                print('Cannot drop food')
                command = input('> ')
        
        elif command == 'QUIT':
            print('Goodbye Grasshopper!')
            exit()
       
        else:
            print('Invalid command')
            command = input('> ')



    while grasshopperfood in game:
        x= game.index(grasshopperfood)
        
        if command == 'WALK R':
                if game[4] == grasshopperfood or game[7] == grasshopperfood or game[9] == grasshopperfood:
                    print('Arrgh!! An Ant attacked you. Game over.')
                    exit()
                elif game[11] == grasshopperfood:
                    pass
                else:
                    x += 1
                game.remove(grasshopperfood)
                game.insert(x,grasshopperfood)
                print(*game)
                command = input('> ')

        elif command == 'WALK L':
                if game[5] == grasshopperfood or game[8] == grasshopperfood or game[10] == grasshopperfood:
                    print('Arrgh!! An Ant attacked you. Game over.')
                    exit()
                elif game[1] == grasshopperfood:
                    pass
                else:
                    x -= 1
                game.remove(grasshopperfood)
                game.insert(x,grasshopperfood)
                print(*game)
                command = input('> ')

        elif command == 'HOP R':
                if game[3] == grasshopperfood or game[6] == grasshopperfood or game[8] == grasshopperfood:
                            print('Arrgh!! An Ant attacked you. Game over.')
                            exit()
                elif game[4] == grasshopperfood or game[7] == grasshopperfood or game[9] == grasshopperfood or game[10] == grasshopperfood:
                    x += 1
                elif game[11] == grasshopperfood:
                    pass
                else:
                    x += 2
                game.remove(grasshopperfood)
                game.insert(x,grasshopperfood)
                print(*game)
                command = input('> ')  
        
        elif command == 'HOP L':
                if game[6] == grasshopperfood or game[9] == grasshopperfood or game[11] == grasshopperfood:
                            print('Arrgh!! An Ant attacked you. Game over.')
                            exit()
                elif game[2] == grasshopperfood or game[5] == grasshopperfood or game[8] == grasshopperfood or game[10] == grasshopperfood:
                    x -= 1
                elif game[11] == grasshopperfood:
                    pass
                else:
                    x -= 2
                game.remove(grasshopperfood)
                game.insert(x,grasshopperfood)
                print(*game)
                command = input('> ')  
            
        elif command == 'PICK UP':
                print('Cannot pick up food')
                command = input('> ')
        
        elif command == 'DROP':
                if game[1] == grasshopperfood:
                    if game[0] == nofood:
                        game.remove(game[0])
                        game.insert(0,onefood)
                    elif game[0] == onefood:
                        game.remove(game[0])
                        game.insert(0,twofood)
                    elif game[0] == twofood:
                        game.remove(game[0])
                        game.insert(0,threefood)
                    game.remove(grasshopperfood)
                    game.insert(1,grasshopper)
                    print(*game)
                    command = input('> ')
                    continue
                    
                elif game[1] != grasshopperfood:
                    print('Cannot drop food')
                    command = input('> ')
        
        elif command == 'QUIT':
            print('Goodbye Grasshopper!')
            exit()
       
        else:
            print('Invalid command')
            command = input('> ')

    if game[0] == threefood:
        print('Congratulations Grasshopper, you now have enough food to last the winter!')
        exit()
        