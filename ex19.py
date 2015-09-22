__a__author__ = 'Jarod Jett'


def servings(cheese_count, boxes_of_crackers):
    cheeses = cheese_count % 3
    total = boxes_of_crackers / cheeses
    print "You have %s servings to distribute" % total


def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers" % boxes_of_crackers
    servings(cheese_count, boxes_of_crackers)


print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)

print "OR, we can use variables from our script and pass them to the function:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print "We can do math as arguments."
cheese_and_crackers(20 + 20, 5 + 6)

print "We can combine the last two."
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 50)