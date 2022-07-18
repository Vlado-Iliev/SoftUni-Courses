class User:
    def __init__(self,user_id,username):
        self.user_id = user_id
        self.username = username
        self.books = list()

    def info(self):
        return ', '.join([x for x in sorted(self.books)])

    def __str__(self):
        return f'{self.user_id}, {self.username}, {self.books}'
    