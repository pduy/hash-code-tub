class Endpoint:
    def __init__(self, endpoint_id, cache_map, data_center_latency):
        self.id = endpoint_id
        self.cache_map = cache_map
        self.data_center_latency = data_center_latency