import os

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
        with open(f"{PULL_DIR}/{f['github_user']}/assignment3/runme.tx", "r") as runtxt:
            players.append({"player" : f"{f['github_user']}", "runtxt" : runtxt.read()})
    except:
        print(f"!!!!!!!!!!! Player {f['github_user']} did not load!!!!!!")




run_txt = ""
with open("runme.txt", "r") as f:
    run_txt = f.read().strip()

os.system(f"{run_txt} --help")





