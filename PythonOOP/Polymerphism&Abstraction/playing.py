def start_playing(cls):
    return cls.play()



class Children:

    def play(self):

        return "Children are playing"

children = Children()

print(start_playing(children))