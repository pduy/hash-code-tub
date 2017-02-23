class Video:
    def __init__(self, id, size):
        self.id = id
        self.size = size
    
    def __str__(self):
        return "{ video id = " + str(self.id) + " , " + \
               "video size = " + str(self.size) + "}"

    def __repr__(self):
        return "{ video id = " + str(self.id) + " , " + \
                 "video size = " + str(self.size) + "}"
