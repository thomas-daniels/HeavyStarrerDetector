from ChatExchange.chatexchange.client import *
from ChatExchange.chatexchange.events import *
from datetime import datetime
import getpass

messages = [
"$ping I'm a bot that detects people who star many at a short period. I saw that you starred 3 messages in less than a minute. Please see the pinned message on the starwall. (I'm sorry if you were starring legitimately)",
"http://chat.stackoverflow.com/transcript/message/20549798#20549798"
]
starrers = []
host = raw_input("Host: ")
room_number = int(raw_input("Room number: "))
email = raw_input("Email address: ")
password = getpass.getpass("Password: ")

c = Client(host)
c.login(email, password)
r = c.get_room(room_number)

def purge():
    curr_date = datetime.utcnow()
    for s in starrers:
        diff = curr_date - s[1]
        tsec = diff.total_seconds()
        if tsec > 60:
            starrers.remove(s)

def remove_user_from_list(id):
    for s in starrers:
        if s[0] == id:
            starrers.remove(s)

def check():
    msgs_starred_in_one_minute = {}
    heavy_starrers = []
    curr_date = datetime.utcnow()
    for s in starrers:
        if not s[0] in msgs_starred_in_one_minute:
            msgs_starred_in_one_minute[s[0]] = 0
        diff = curr_date - s[1]
        tsec = diff.total_seconds()
        if tsec <= 60:
            curr_val = msgs_starred_in_one_minute[s[0]]
            msgs_starred_in_one_minute[s[0]] = curr_val + 1
    for ms in msgs_starred_in_one_minute:
        if msgs_starred_in_one_minute[ms] >= 3:
            heavy_starrers.append(ms)
    return heavy_starrers

def on_event(event, client):
    if not isinstance(event, MessageStarred):
        return
    curr_date = datetime.utcnow()
    starrers.append((event.user.id, curr_date))
    purge()
    detected = check()
    if len(detected) > 0:
        for hs in detected:
            usr = c.get_user(hs)
            uname = usr.name
            print("Heavy starrer detected: " + uname)
            for m in messages:
                msg_to_post = m.replace("$ping", "@" + uname).replace("$user", uname)
                r.send_message(msg_to_post)
            remove_user_from_list(hs)

r.join()
r.watch_socket(on_event)

running = True
while running:
    cmd = raw_input("<< ")
    if cmd == "stop":
        c.logout()
        running = False