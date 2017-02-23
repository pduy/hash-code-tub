class Candidate:
    def __init__(self, video_id, endpoint_id, reward, cache_id):
        self.video_id = video_id
        self.endpoint_id = endpoint_id
        self.reward = reward
        self.cache_id = cache_id

    def __str__(self):
        return "{video id = " +     str(self.video_id) + "," \
                "endpoint_id = " +  str(self.endpoint_id) + "," \
                "reward = " +       str(self.reward) + "," \
                "cache id = " +     str(self.cache_id) + "}"

    def __repr__(self):
        return "{video id = " +     str(self.video_id) + "," \
                "endpoint_id = " +  str(self.endpoint_id) + "," \
                "reward = " +       str(self.reward) + "," \
                "cache id = " +     str(self.cache_id) + "}"
