# shhh these arent "real" tests

from character import Character
from character import Hero
from character import Monster

# Character can be instantiated with name and avatar
arya = Character("Arya Stark", "arya.png")
jon = Character("Jon Snow", "jon.png")

print(arya.name, arya.avatar)
print(jon.name, jon.avatar)

# After adding 2 items to inventory
# length of inventory should == 2

arya.inventory.append('Needle')
arya.inventory.append('mask')

print(len(arya.inventory))

# arya should have a `greet` method
# and when I call with `arya.greet(jon)`, it should return
# "Hello Jon Snow, I am Arya Stark. I am awesome"
print(arya.greet(jon))

# arya should have a `greet` method
# and when I call with `arya.greet()`, it should return
# "Hello, I am Arya Stark. I am awesome"
print(arya.greet())

# I should be able to create a hero instance
bronn = Hero("Bronn of the Blackwater", "bronn.png")

# Hero should be able to greet Character
print(bronn.greet(arya))
print(jon.greet(bronn))

# should be able to create a monster instance
walker = Monster()

# Monster and Hero should be able to greet eachother
print(walker.greet(bronn))
print(bronn.greet(walker))

# Monster should be able to growl at nothing or at someone
print(walker.rawr())
print(walker.rawr(jon))

# expect Jon to say eek when encountering Monster
print(bronn.greet(walker))
print(bronn.greet(jon))