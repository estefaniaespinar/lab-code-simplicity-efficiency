
# coding: utf-8

# In[92]:


def inicio():
    print('Welcome to this calculator!')
    print('It can add and subtract whole numbers from zero to five')


# In[93]:


def first_number():
    while True:
        a = input('Please choose your first number from 0 to 5: ')

        if a.isdigit():
            if int(a) in range(0,6):
                return int(a)
        
        else :
            print("Sorry I don't understand you, enter another number between 0 and 5: ")


# In[94]:


def signo():
    while True:
        b = input('Insert + if you want to sum the number or - if you want to rest it: ')
        
        if (b.isdigit()) == False | (b.isalpha()) == False:
            if b == '+' or b == '-':
                return b
            else:
                input("Sorry I don't understand you, enter + or - signs: ")

        else:
            print("Sorry I don't understand you, enter + or - signs: ")


# In[96]:


def second_number():
    while True:
        c = input('Please choose your second number from 0 to 5: ')
    
        if c.isdigit():
            if int(c) in range(0,6):
                return int(c)

        else :

            print("Sorry I don't understand you, enter another number between 0 and 5: ")

