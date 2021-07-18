import os
import subprocess
from pathlib import Path


CWD = Path(os.getcwd())
APP_DIR = CWD.joinpath('tianqi_web')


cmds = [
    f"cd {APP_DIR}",
    f"python manage.py runserver"
]

p1 = subprocess.Popen(["start", "cmd", "/k", "&&".join(cmds)], shell=True)


# from os import system; _ = system('cls')
