import os


class User(object):
    def __init__(self):
        self.username = os.environ.get("USERNAME")

    def __repr__(self):
        return self.username
