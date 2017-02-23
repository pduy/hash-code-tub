class Endpoint:
    def __init__(self, endpoint_id, cache_map, data_center_latency):
        self.id = endpoint_id
        self.cache_map = cache_map
        self.data_center_latency = data_center_latency

    def __str__(self):
        return "endpoint id = " + self.endpoint_id + "\n" \
                "cache_map = " + str(self.cache_map) + "\n" \
                "data_center_latency = " + self.data_center_latency
