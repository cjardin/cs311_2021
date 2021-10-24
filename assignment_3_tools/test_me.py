import argparse
import random
import os
import subprocess

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--player_a_runme_file', help='Player A runme.txt')
    parser.add_argument('--player_b_runme_file', help='Player B runme.txt')
    parser.add_argument('--iterations', help='number of iterations in game')
    args = parser.parse_args()

    players = []

    with open(args.player_a_runme_file, "r") as f:
        players.append( {"dir_name" : os.path.dirname(args.player_a_runme_file),
            "runme" : f.read().strip() , "player name" : "A",  "game_years" : 0 } )

    with open(args.player_b_runme_file, "r") as f:
        players.append( {"dir_name" : os.path.dirname(args.player_b_runme_file),
            "runme" : f.read().strip() , "player name" : "B", "game_years" : 0} )

    iterations = 100
    for i in range(2):
        p = players[i]
        p['game_years'] = 0
        p['last_move'] = "zero"
        p['current_move'] = "zero"

    for i  in range(iterations):
        for i in range(2):
            p = players[i] 
            if i == 0:
                proc = subprocess.Popen([f"{p['runme']} --init true --iterations {iterations}"], 
                        stdout=subprocess.PIPE, shell=True , cwd= p['dir_name'])
                (out, err) = proc.communicate()
           
            last_move = players[0]['last_move'] if i == 1 else players[1]['last_move']
            proc = subprocess.Popen([f"{p['runme']} --last_opponent_move {last_move}"],
                    stdout=subprocess.PIPE, shell=True , cwd= p['dir_name'])
            (out, err) = proc.communicate()
            #print(out)
            p['current_move'] = out.strip().lower().decode("utf-8")


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
        players[0]['last_move'] = players[1]['current_move'] 
        players[1]['last_move'] = players[0]['current_move']

    if players[0]['game_years'] > players[1]['game_years']:
        print(f"Player {players[1]['player name']} wins {players[1]['game_years']} < {players[0]['game_years']}")
    elif players[1]['game_years'] > players[0]['game_years']:
        print(f"Player {players[0]['player name']} wins {players[0]['game_years']} < {players[1]['game_years']}")
    else:
        print(f"Tie {players[0]['game_years']} = {players[1]['game_years']}")





