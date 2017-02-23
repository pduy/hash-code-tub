import video

class Cache:
    def __init__(self, cache_id, size, videos=[]):
        self.id = cache_id
        self.size = size
        self.videos = videos
        self.isModified = False

        if len(videos) == 0:
            self.freespace = size
        else:
            self.freespace = self.get_free_space()

    def add_video(self, video):
        if self.get_free_space() > video.size:
            if video.id not in [v.id for v in self.videos]:
                self.videos.append(video)
                self.isModified = True
            return True
        else:
            return False

    #TODO: check video id instead
    #def remove_video(self, video):
    #    self.videos.remove(video)
    #    self.isModified = True

    def get_free_space(self):
        if self.isModified:
            self.freespace  = self.size - sum([v.size for v in self.videos])
            self.isModified = False

        return self.freespace

    def __str__(self):
        return "{ cache id = " + str(self.id) + "," \
                "size = " +      str(self.size) + "," \
                "videos = " + [str(v) for v in self.videos] + "}"

    def __repr__(self):
        return "{ cache id = " + str(self.id) + "," \
                "size = " +      str(self.size) + "," \
                "videos = " + str([str(v) for v in self.videos]) + "}"
