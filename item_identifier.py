#identify items based on a couple of key words

#item = [list of keywords that define item]

crocs = ["lightweight", "waterproof", "comfort", "versatile"]
sweater = ["cozy", "over-sized", "chunky", "plush"]
phone = ["small", "hand-held", "did he", "useful"]


item_input = input("Keywords that closely defines your desired product: ")

if item_input in crocs:
    print("You want crocs! Prices for crocs go around $30 - $50 on Amazon.")
elif item_input in sweater:
    print("You want a sweater(s)! Prices for sweater go around $20 - $40 on Amazon.")
elif item_input in phone:
    print("You want a phone(s)! Prices for phones go around $1 - $99999999990 on Amazon.")
else:
    print("try again!")
