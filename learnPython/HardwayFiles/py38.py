ten_things = "apples oranges crows telephones light sugar"

print("Wait, there are not 10 things in that list, let's fix that")

stuff = ten_things.split(" ")
more_stuff = ["day", "night", "song", "frisbee", "corn", "banana", "girl", "boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print("adding: ", next_one)
    stuff.append(next_one)
    print("there are %d items now." % (len(stuff)))

print("There we go:", stuff)

print("let's do some things with stuff")

print(stuff[1])
print(stuff[-1])
print(stuff.pop())
print("'" * 5)
print(" ".join(stuff))
print("#".join(stuff[3:5]))
