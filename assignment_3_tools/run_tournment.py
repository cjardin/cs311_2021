import os
import argparse
import random
import subprocess

import sqlite3



def run_game(player_a, player_b):
    players = [player_a, player_b]
    iterations = 100 
    for i in [0,1]:
        p = players[i]
        p['game_years'] = 0 
        p['last_move'] = "zero"
        p['current_move'] = "zero"

    for i  in range(iterations):
        error = False
        for j in [0,1]:
            p = players[j] 
            if i == 0:
                proc = subprocess.Popen([f"{p['runme']} --init true --iterations {iterations}"], 
                        stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True , cwd= p['dir_name'])
                (out, err) = proc.communicate()
                
                err = err.decode("utf-8").strip()
                if len(err) != 0:
                    p['error'] = f"""Init Error .. crashed - {err}"""
                    error = True
    
            last_move = players[0]['last_move'] if j == 1 else players[1]['last_move']
            proc = subprocess.Popen([f"{p['runme']} --last_opponent_move {last_move}"],
                    stdout=subprocess.PIPE, stderr=subprocess.PIPE,  shell=True , cwd= p['dir_name'])
            (out, err) = proc.communicate()
            p['current_move'] = out.strip().lower().decode("utf-8")
            err = err.decode("utf-8").strip()
            if len(err) != 0  or p['current_move'] not in ('silent', 'confess'):
                p['error'] = f"""Invalid output "{p['current_move']}" stderr: {err} """
                error = True

        if error:
            break
        
        #score it!
        if players[0]['current_move'] == "confess" and players[1]['current_move'] == "confess":
            players[0]['game_years'] = players[0]['game_years'] + 5 
            players[1]['game_years'] = players[1]['game_years'] + 5 
        elif players[0]['current_move'] == "confess" and players[1]['current_move'] == "silent":
            players[0]['game_years'] = players[0]['game_years'] + 0 
            players[1]['game_years'] = players[1]['game_years'] + 20
        elif players[0]['current_move'] == "silent" and players[1]['current_move'] == "confess":
            players[0]['game_years'] = players[0]['game_years'] + 20
            players[1]['game_years'] = players[1]['game_years'] + 0 
        elif players[0]['current_move'] == "silent" and players[1]['current_move'] == "silent":
            players[0]['game_years'] = players[0]['game_years'] + 1 
            players[1]['game_years'] = players[1]['game_years'] + 1 
        else:
            print(players)
            print("!!!!!!!!!!!!!!!!!!!!Error!!!!!!!!!!!!!!")
        players[0]['last_move'] = players[0]['current_move'] 
        players[1]['last_move'] = players[1]['current_move']

    if players[0]['game_years'] > players[1]['game_years']:
        print(f"Player {players[1]['player']} wins {players[1]['game_years']} < {players[0]['game_years']}")
    elif players[1]['game_years'] > players[0]['game_years']:
        print(f"Player {players[0]['player']} wins {players[0]['game_years']} < {players[1]['game_years']}")
    else:
        print(f"Tie {players[0]['game_years']} = {players[1]['game_years']}")

    return (players[0]['game_years'], players[1]['game_years'], int( 'error' in  players[0]), int( 'error' in  players[1]) )


PULL_DIR = "repos"

fork_list = []
black_list = {}

with open("black.list", "r") as f:
    all_forks = f.read()
    for ffork in all_forks.split('\n'):
        parts = ffork.split()
        # example line ['@atilla20cs', 'atilla20cs', '/', 'cs311_2021']
        if len(parts) != 4:
            continue
        black_list[parts[1]] = "block"


with open("forkme.list", "r") as f:
    all_forks = f.read()
    for ffork in all_forks.split('\n'):
        parts = ffork.split()
        # example line ['@atilla20cs', 'atilla20cs', '/', 'cs311_2021']
        if len(parts) != 4:
            continue
        if parts[1] in black_list:
            continue

        fork_list.append( {"github_user" : parts[1], "repo" : parts[3]} )

#clean up
os.system(f"rm -rf {PULL_DIR}")

players = []
players_by_name = {}
#load them up
for f in fork_list:
    os.system(f"mkdir -p {PULL_DIR}/{f['github_user']}")
    exec_me = f"git clone git@github.com:{f['github_user']}/{f['repo']}.git {PULL_DIR}/{f['github_user']}"
    os.system(exec_me)

    try:
        with open(f"{PULL_DIR}/{f['github_user']}/assignment3/runme.txt", "r") as runtxt:
            players.append({"player" : f"{f['github_user']}", "runme" : runtxt.read().strip(),
                     "dir_name" : os.path.dirname(f"{PULL_DIR}/{f['github_user']}/assignment3/runme.txt")
                })
    except:
        players.append({"player": f['github_user'], "error" : "runme.txt did not load!!!!" } )
        print(f"!!!!!!!!!!! Player {f['github_user']} did not load!!!!!!")
    players_by_name[ players[-1]['player'] ] = players[-1]



#setup the db

db = sqlite3.connect('tourment.db')
cur = db.cursor()


cur.execute("create table games (player_a text, player_b text, t_round interger, player_a_years integer, player_b_years integer, player_a_error int, player_b_error int)")
db.commit()

#init
t_round = 0
while t_round < 100: #Just don't like inifinate loops 
    random.shuffle(players)
    for p in players:
        p["who_i_played_this_round"] = []
    for p in players:
        if "error" in p:
            continue
        for pp in players:
            if pp == p or "error" in pp:
                continue
            if pp in p["who_i_played_this_round"] or p in pp["who_i_played_this_round"] :
                continue 

            print(p["player"],pp["player"])
            player_a_years, player_b_years, player_a_err, player_b_err = run_game(p, pp)
            p["who_i_played_this_round"].append(pp)
            cur.execute(f"""insert into games values ('{p["player"]}', '{pp["player"]}',
                    {t_round}, {player_a_years}, {player_b_years},
                    {player_a_err} , {player_b_err} )""")
            db.commit()



    #get bad list
    bad =[]
    cur.execute(f"""select player_a from games where t_round = {t_round} and player_a_error =1
            UNION 
            select player_b from games where t_round = {t_round} and player_b_error =1 """)
    for r in cur.fetchall():
        p =  players_by_name[ r[0] ]
        bad.append( f"{p['player']} you have a problem! {p['error']}")

    #get good list
    good =[]
    cur.execute(f"""select player_a from games where t_round = {t_round} and player_a_error =0 and player_a_years <= player_b_years
            UNION
            select player_b from games where t_round = {t_round} and player_b_error =0 and player_b_years <= player_a_years """)
    for r in cur.fetchall():
        p = players_by_name[ r[0] ]
        good.append( f"{p['player']} YES!!!! It worked!!!" )


    print("!!!!!!!!! Working !!!!!!!!!!!")
    for p in good:
        print(p)

    print("")
    print("!!!!!!!!! NOT Working !!!!!!!!!!!")
    for p in bad:
        print(p)

    print("")
    print("!!!!!!!!! NOT Accepted LIST !!!!!!!!!!!")
    for p in black_list:
        print(p)


    #who moves on?
    cur.execute(f"""select player, sum(total) as total from
                (select player_b as player, sum(player_b_years) as total from games where 
                t_round = {t_round} and player_b_error =0 group by player union select player_a as player, sum(player_a_years) as total from 
                games where t_round = {t_round} and player_a_error =0 group by player) group by player order by total asc;""")
    for r in cur.fetchall():
        print(r)


    t_round += 1
    break





