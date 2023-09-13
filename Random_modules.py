#python random randint method
import random
print(random.randint(2,7))#return a random no between 5 and 10 both included
#python random randrange method
print(random.randrange(4,7))#return a random no between 4(included) and 7(not included)
#python random choice method(return random element from list)
l=["mooon","hassan",56,"waqar","jumaid"]
print(random.choice(l))
# random(return a random float no between 0 and 1)
# shuffle(return a sequence of no in random order)
# uniform(return a random float no between two given parameters)
random.shuffle(l)
print(l)
r=random.random()
print(r)
e=random.uniform(3,6)
print(e)




