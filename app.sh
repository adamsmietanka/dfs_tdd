if [ -z "$1" ]; then >&2 echo Please provide a .txt file as an argument; else python main.py "$1"; fi