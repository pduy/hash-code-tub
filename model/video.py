class Video:
    def __init__(self, id, size):
        self.id = id
        self.size = size
    
    def __str__(self):
        return "video id = " + self.id + "\n" \
                "video size = " + self.size
