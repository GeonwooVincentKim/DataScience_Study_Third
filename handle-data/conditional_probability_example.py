import enum, random


class Kid(enum.Enum):
    BOY = 0
    GIRL = 1

"""
def random_kid() -> Kid:
    return random.choice([Kid.BOY, Kid.GIRL])
"""
def random_kid():
    return random.choice([Kid.BOY, Kid.GIRL])


both_girls = 0
older_girl = 0
either_girl = 0

random.seed(0)

print(random_kid().value)

for _ in range(10000):
    younger = random_kid()
    older = random_kid()
    
    if older == Kid.GIRL:
        older_girl += 1
        print(older_girl)
    
    if older == Kid.GIRL and younger == Kid.GIRL:
        both_girls += 1
        print(both_girls)
        
    if older == Kid.GIRL or younger == Kid.GIRL:
        either_girl += 1

    print("Younger : {0}\nOlder : {1}".format(younger, older))
    
print("P(both | Older) : ", both_girls / older_girl)
print("P(both | either) : ", both_girls / either_girl)
