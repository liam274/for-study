def main():
    import os
    import re
    USER_PATH="user.txt"
    DICT=re.compile("\\{([\"']*(.*)[\"']*( )*:( )*[\"'](.*)[\"'])*(,)*( )*\\}")
    def signup(us,psw):
        with open(USER_PATH,"a+") as file:
            file.write(str({us:psw}))
        return True
    def login():
        with open(USER_PATH,"r") as file:
            
