#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Using variavel balance to track the values in real time

balance = 0  

#limit of withdraw

withdraw_limit = 500  

# list to register operations

transaction_history = []  

while True:
    print('Welcome! Choose an option:')
    print('1. Deposit')
    print('2. Withdraw')
    print('3. Bank Statement')
    print('4. Exit')

    choice = input('Enter your choice: ')

    if choice == '1':
        deposit_amount = float(input('Enter the amount to deposit: '))
        if deposit_amount > 0:
            balance += deposit_amount
            transaction_history.append(f'Deposit of ${deposit_amount}')
            print(f'Deposit of ${deposit_amount} successful.')
        else:
            print('Invalid deposit amount.')
    
    elif choice == '2':
        withdraw_amount = float(input('Enter the amount to withdraw: '))
        if withdraw_amount > 0 and withdraw_amount <= withdraw_limit and withdraw_amount <= balance:
            balance -= withdraw_amount
            transaction_history.append(f'Withdrawal of ${withdraw_amount}')
            print(f'Withdrawal of ${withdraw_amount} successful.')
        else:
            if withdraw_amount <= 0:
                print('Invalid withdrawal amount. Please enter a positive amount.')
            elif withdraw_amount > withdraw_limit:
                print(f'Withdrawal amount exceeds the limit of ${withdraw_limit}.')
            else:
                print('Insufficient balance.')
    
    elif choice == '3':
        print(f'Your current balance is ${balance}.')
        print('Transaction History:')
        for transaction in transaction_history:
            print(transaction)
    
    elif choice == '4':
        print('Thank you for using our banking system. Goodbye!')
        break
    
    else:
        print('Invalid choice. Please select a valid option.')


# In[ ]:





# In[ ]:




