print('WELCOME TO UNPERT BANK ATM')
def main():
    trial=3
    restart='y'
    balance=445
    while trial >= 0:
        atm_pin = int(input('Enter your 4 digit pin:'))
        if atm_pin == 1234:
            print('\nCORRECT PIN!')
            while restart not in ('n','no','N','NO'):
                print('\n-----------------------')
                print('press 1 to WITHDRAW\n')
                print('press 2 to CHECK BALANCE\n')
                print('press 3 to DEPOSIT\n')
                print('press 4 to CANCEL')
                print('-----------------------\n')
                option = int(input('What transaction do you want to perform?:'))
                if option == 1:
                    withdrawal_amount=int(input('\nHow much do you wish to withdraw?:'))
                    amount=(10,20,30,40,50)
                    if withdrawal_amount not in amount:
                        print('Invalid withdrawal amount')
                    elif withdrawal_amount in amount:
                         print(f'CONGRATS! you have successfully withdrawn ${withdrawal_amount:.2f}')
                         balance = balance - withdrawal_amount
                         print('\n------ BALANCE ------')
                         print(f'Your balance is ${balance:.2f}')
                         print('---------------------')
                         restart=input('\nWould you like to go back?:')
                         if restart in ('n','NO','No','N'):
                            break
                elif option == 2:
                    print('\n------ BALANCE ------')
                    print(f'Your balance is ${balance:.2f}')
                    print('---------------------')
                    restart=input('\nWould you like to go back?:')
                    if restart in ('n','NO','No','N'):
                       break
                elif option == 3:
                    deposit=int(input('\nHow much do you wish to deposit?:'))
                    amount=(10,20,30,40,50)
                    if deposit in amount:
                        balance=balance+deposit
                        print(f'You have successfully deposited ${deposit:.2f}')
                        print('\n------ BALANCE ------')
                        print(f'Your balance is ${balance:.2f}')
                        print('---------------------')
                        restart = input('\nWould you like to go back?:')
                        if restart in ('n', 'NO', 'No', 'N'):
                           break
                elif option == 4:
                    print('\nTransaction cancelled, please take your card')
                    break
                else:
                    print('Invalid input,select numbers between 1-4!!!')
                    restart = 'y'
        elif atm_pin != 1234:
            print('Wrong pin!')
            trial= trial-1
            if trial == 0:
                print('You have exhausted your trials')
                print('\nDO HAVE A NICE DAY!')
                break

    print('\nTHANK YOU FOR BANKING WITH US')
if __name__=='__main__':
    main()