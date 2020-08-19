# reference: http://zetcode.com/python/hashing/

class User: 
    def __init__(self, name, occupation):
        self.name = name
        self.occupation = occupation

    def __eq__(self, other):
        if not isinstance(other, User):
            return False
        return self.name == other.name and self.occupation == other.occupation
    
    def __hash__(self):
        return hash((self.name, self.occupation))

    def __str__(self):
        return f'{self.name} -> {self.occupation}'

u1 = User('John', 'SDE')
u2 = User('John', 'SDE')
users = {u1, u2}

print(len(users))
# print(hash(u1))
# print(hash(u2))

if u1 == u2:
    print('same')
    print(f'{u1} == {u2}')
else:
    print('different')

print('-' * 30)

u1.occupation = 'DE'
users = {u1, u2}
print(len(users))
if u1 == u2:
    print('same')
    print(f'{u1} == {u2}')
else:
    print('different')
    
