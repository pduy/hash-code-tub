class Candidate:
    def __init__(self, video_id, endpoint_id, reward, cache_id):
        self.video_id = video_id
        self.endpoint_id = endpoint_id
        self.reward = reward
        self.cache_id = cache_id

    def __str__(self):
        return "video id = " + self.video_id + "\n" \
                "endpoint_id = " + self.endpoint_id + "\n" \
                "reward = " + self.reward + "\n" \
                "cache id = " + self.cache_id
