import random

# ::METHODS OF RANDOM MODULE ARE::
#random() # start stop step #start is 0 by default
# randrange()
# choice()
# choices()
#seed()
#shuffle()
#sample()

random.randrange(100) 
number1=random.random() # from 0.0 to 1.0
print(number1)
random.randint(1,6) # from 1 to 6
random.choice("bharat") # gives a letter these 6 letters


numbers = [1,2,3,4,5,6]
random.shuffle(numbers


)
random.choice(numbers)



fruits = ["banana", "apple", "mango"]
random.choice(fruits)

random.seed(100) #  Reproduce same set of output again and again

#random.sample(set , selection)
random.sample (numbers,3)

list1 =[1,2,3,4,5,6,7,8,9,10]
random.sample(list1,3)

list1 =[1,2,3,4,5,6,7,8,9,10]
random.choices(list1,k=2)


list1 =[1,2,3,4,5,6,7,8,9,10]
random.sample(list1,k=5)

#choices contain duplicates
#sample() contain no duplicates