import video

class Cache:
    def __init__(self, cache_id, size, videos):
        self.id = cache_id
        self.size = size
        self.videos = videos

    def add_video(self, video):
        self.videos.append(video)

    def remove_video(self, video):
        self.videos.remove(video)

    def get_free_space(self):
        return size - sum([v.size for v in self.videos])