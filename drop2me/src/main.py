from flask import Flask, redirect, url_for, render_template, request, session
import json
import sys
import os
from markupsafe import Markup
import random
from threading import Timer
from time import sleep

g_domain = None


public_row = '''<tr>
  <td><a href={ref}>{name}</a></td>
  <td>{size}</td>
  <td>{user}</td>
  <td>{date}</td>
</tr>'''

FILE_STORAGE_PATH="/var/www/filestorage/"

app = Flask(__name__)
app.secret_key = os.urandom(12)  # Generic key for dev purposes only

def get_random():
    n = random.randint(1000,9999)
    return n

def human_readable_size(size, decimal_places=2):
    for unit in ['B', 'KiB', 'MiB', 'GiB', 'TiB', 'PiB']:
        if size < 1024.0 or unit == 'PiB':
            break
        size /= 1024.0
    return f"{size:.{decimal_places}f} {unit}"

def get_file_size(filename):
    st = os.stat(filename)
    return st.st_size

# ======== Routing =========================================================== #
@app.route('/', methods=['GET', 'POST'])
def home():
    global g_domain
    filerow = ""

    file_arr = os.listdir(FILE_STORAGE_PATH)
    for item in file_arr:
        fsize = get_file_size(FILE_STORAGE_PATH+item)
        readable_size = human_readable_size(fsize)
        ref = 'https://{}/upload/{}'.format(g_domain, item)
        raw = public_row.format(name=item,ref=ref,size=readable_size,user="user",date="date")
        filerow = filerow + raw
    markup = Markup(filerow)
    return render_template('home.html', filecontent=markup)

def main():
    global g_domain
    g_domain = os.environ.get('WB_DOMAIN', 'drop2.me')
    app.run(debug=True, use_reloader=True, host="0.0.0.0")


# ======== Main ============================================================== #
if __name__ == "__main__":
    main()