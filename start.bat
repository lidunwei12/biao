@echo off
start cmd /k "python data.py"
start cmd /k "python src/do_task.py"
start cmd /k "python server/one_server.py"
start cmd /k "python server/two_server.py"
start cmd /k "python server/three_server.py"
start cmd /k "python server/four_server.py"
