import os
import argparse
import random
import subprocess



def run_game(player_a, player_b):
    players = [player_a, player_b]
    iterations = 100 
    for i in range(2):
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
    
            last_move = players[0]['last_move'] if i == 1 else players[1]['last_move']
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


PULL_DIR = "repos"

fork_list = []
with open("forkme.list", "r") as f:
    all_forks = f.read()
    for ffork in all_forks.split('\n'):
        parts = ffork.split()
        # example line ['@atilla20cs', 'atilla20cs', '/', 'cs311_2021']
        if len(parts) != 4:
            continue
        fork_list.append( {"github_user" : parts[1], "repo" : parts[3]} )


#clean up
os.system(f"rm -rf {PULL_DIR}")

players = []
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


#init
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
        run_game(p, pp)
        p["who_i_played_this_round"].append(pp)


good = []
bad = []
for p in players:
    if "error" in p:
        bad.append( f"{p['player']} you have a problem! {p['error']}")
    else:
        good.append(f"{p['player']} YES!!!! It worked!!!")

print("!!!!!!!!! Working !!!!!!!!!!!")
for p in good:
    print(p)

print("")
print("!!!!!!!!! NOT Working !!!!!!!!!!!")
for p in bad:
    print(p)






