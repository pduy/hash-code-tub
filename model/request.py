class Request:
    def __init__(self, video_id, endpoint_id, n_requests):
        self.video_id = video_id
        self.endpoint_id = endpoint_id
        self.n_requests = n_requests

    def __str__(self):
        return "video id = " + self.video_id + "\n" \
                "endpoint_id = " + self.endpoint_id + "\n" \
                "n_requests = " + self.n_requests