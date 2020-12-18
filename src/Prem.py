import random
#list of teams
teams = ["Arsenal", "Aston Villa", "Brighton", "Burnley", "Chelsea",
         "Crystal Palace", "Everton", "Fulham", "Leeds", "Leicester", 
         "Liverpool", "Man City", "Man Utd", "Newcastle", "Sheffield",
         "Southampton", "Spurs", "West Brom", "West Ham", "Wolves"]

def PL_Games(teams):
    game = []
    games = []
    #for all games
    for i in range(380):
        #choose teams
        x = random.choice(teams)
        y = random.choice(teams)
        #make game
        game = [x,y]
        #check if same team
        while x == y:
            y = random.choice(teams)
            game = [x,y]
            #check if game exists
            while game in games:
                y = random.choice(teams)
                game = [x,y]
        #check if game exists
        while game in games:
            x = random.choice(teams)
            y = random.choice(teams)
            game = [x,y]
            while x == y:
                y = random.choice(teams)
                game = [x,y]
        #confirm game
        games.append(game)
    #organize games
    games.sort()
    return games    

def results(games, teams):
    
    results = ["winner", "draw"]
    #rank for teams
    rank = [80,76,78,77,83,81,82,74,75,84,90,89,85,73,68,72,86,64,71,79]
    #current points for teams
    points = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    #isolate a game
    for x in games:
        gamespl = []
        #isolate teams
        teamA = x[0]
        teamB = x[1]
        #get the rank of the first team
        rankA = teams.index(teamA)
        rnkA = rank[rankA]
        #get the rank of the second team
        rankB = teams.index(teamB)
        rnkB = rank[rankB]
        #easy win
        winax = False
        winbx = False
        
        difference = 0
        chance = [0,1,2,3,4,5,6,7,8,9,10]
        #check if should be an easy win, allowing for random chance
        if rnkA > rnkB:
            difference = rnkA - rnkB
            if difference > 3:
                number = random.choice(chance)
                if number > 2:
                    winax = True
        #check if should be an easy win, allowing for random chance
        if rnkA < rnkB:
            difference = rnkA - rnkB
            if difference > 3:
                number = random.choice(chance)
                if number > 2:
                     winbx = True
        gamespl.append(teamA)
        gamespl.append(teamB)
        chc = random.choice(results)
        #add points for easy wins
        if winax == True:
            winnum = teams.index(teamA)
            points[winnum]+=3
        if winbx == True:
            winnum = teams.index(teamB)
            points[winnum]+=3
        #random winner if not an easy win
        if winax == False and winbx == False:
            if chc == "winner":
                winner = random.choice(gamespl)
                winnum = teams.index(winner)
                points[winnum]+=3
        #check for a draw        
        if chc == "draw":
            a = teams.index(teamA)
            points[a]+=1
            b = teams.index(teamB)
            points[b]+=1
    return points

def tab(teams,points):
    table = []
    #generate table
    for i in range(20):
        toadd = [teams[i], points[i]]
        table.append(toadd)
    table = sorted(table, key=lambda x: x[1], reverse=True)
    count = 0
    #make table look nice
    for team in table:
        a = team[0]
        b = team[1]
        print(str(a) + " " + str(b))
        count+=1
        if count == 4:
            print("-----------------")
        
        if count == 5:
            print("-----------------")
        if count == 17:
            print("-----------------")
    #check who gets outcomes
    win = [table[0]]
    cl = [table[0],table[1],table[2],table[3]]
    el = [table[4]]
    rel = [table[17],table[18],table[19]]
    print()
    #get outcomes
    for x in win:
        a = x[0]
        print(str(a) + " have won the premier league!")
    print()
    for x in cl:
        a = x[0]
        print(str(a) + " have qualified for the champions league!")
    print()
    for x in el:
        a = x[0]
        print(str(a) + " have qualified for the europa league!")
    print()
    for x in rel:
        a = x[0]
        print(str(a) + " have been relegated!")
#calls
games = PL_Games(teams)
points = results(games, teams)
tab(teams,points)
        






