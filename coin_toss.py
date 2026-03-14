# FILE NAME - coin_toss.py

# NAME: Shanelle Alvarez
# DATE: March 1, 2026
# BRIEF DESCRIPTION: Coin Toss  



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience



########## ENTER YER CODE BELOW THIS LINE ##########

# Don't forget to import random!!!!!


def main():
    coin_toss()

def coin_toss():
    import random

    random_number = random.randint(1, 100)

    if random_number > 50:
         print ('===== Coin Flipper =====\nTails')
           
    else: 
        print('===== Coin Flipper =====\nHeads')

main()






########### END YER CODE ABOVE THIS LINE ###########

    



########################################
#          SAMPLE OUTPUT
########################################
'''
===== Coin Flipper =====
Heads
'''



'''
===== Coin Flipper =====
Tails
'''


########################################
#          REFLECTION QUESTIONS
########################################

'''

1. What was the hardest part of completing this lab? 



I made a mistake with my "random.randint" statement. It took a few tries to figure out the I was writing it as random.randint(1- 100) instead of (1, 100).



'''
