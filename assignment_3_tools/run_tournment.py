import os


fork_list = []
with open("forkme.list", "r") as f:
    all_forks = f.read()
    for ffork in all_forks.split('\n'):
        print(ffork.split())


run_txt = ""
with open("runme.txt", "r") as f:
    run_txt = f.read()

print(run_txt)
os.system(run_txt)





