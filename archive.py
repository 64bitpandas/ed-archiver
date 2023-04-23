from edapi import EdAPI
import json
import pathlib
import os
import time

ed = EdAPI()

FILEPATH = os.path.dirname(os.path.realpath(__file__))

class color:
    MAGENTA = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    NC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def prettify(c):
    return f"{c['num']} {c['term']} ({c['id']})"


print(f'{color.MAGENTA}Welcome to the Ed Archiver!{color.NC}')

try:    
    ed.login()
except Exception as e:
    print(f'{color.FAIL}Authentication Error: {e}{color.NC}')
    exit(1)

print(f'\n{color.MAGENTA}Enter the ID of the course you want to archive. \nExample: 23247{color.NC}')
course_id = input('> ')

try:
    curr_threads = ed.list_threads(course_id, limit=1)
except Exception as e:
    print(f'{color.FAIL}Invalid ID: {course_id}\n{e}{color.NC}')
    exit(1)

print(f'{color.BLUE}Archiving course {course_id}{color.NC}')
offset = 1
step = 100
count = 0
posts_file = open(f"out/{course_id}.json", "w")
posts_file.write('{\n')

while curr_threads:
    for thread in curr_threads:
        posts_file.write(f"\t{json.dumps(ed.get_thread(thread['id']))},\n")
        count += 1
    curr_threads = ed.list_threads(course_id, limit=step, offset=offset)
    print(f"Read {count} posts")
    if offset > 100:
        time.sleep(30)
    offset += step

posts_file.write('}\n')
posts_file.close()

print(f"{color.GREEN}Successfully saved {count} posts to out/{course_id}.json{color.NC}")

    