#Leon Oram
#6-1-2015
#list of lists

players =[
    ["k1llmAchine",51,49],
    ["bob2247",5,99],
    ["hAxOr12",72,30]
    ]

print("|{0:<12}|{1:<5}|{2:<7}|".format("Name","Kills","Deaths"))
for player in players:
    print("----------------------------")
    print("|{0:<12}|{1:^5}|{2:^7}|".format(player[0],player[1],player[2]))
    
