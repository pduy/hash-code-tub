#!/usr/bin/python

import os
from model.cache import Cache
from model.candidate import Candidate
from model.endpoint import Endpoint
from model.request import Request
from model.video import Video
from solution import find_solution, write_solution

from sys import argv

def debug(str):
    if os.getenv('DEBUG', False):
        print(str)

def intTuple(str):
    return map( int, str.split(' ') )

def parseInputs():
    script, filename = argv

    txt = open(filename)

    lines = txt.read().split('\n')

    first_line = lines[0]

    (no_videos, no_endpoints, no_requests, no_caches, cache_size) = intTuple(first_line)

    video_size = intTuple(lines[1])

    debug("Video %d" % no_videos)
    debug("Videos size : ")
    debug( video_size )

    videos = []
    for i in range(no_videos):
        videos.append(Video(i, video_size[i]))
    debug(videos)

    caches = []
    for i in range(no_caches):
        caches.append(Cache(i, cache_size))

    debug(caches)



    idx = 2

    # loop endpoint
    endpoints = []
    endpoint_id = 0
    while( no_endpoints > 0 ):
        (latency_to_dc, no_caches) = intTuple(lines[idx])
        idx = idx + 1

        latency_to_caches = dict()
        for i in range(no_caches):
            (cache_server, latency) = intTuple(lines[idx])
            latency_to_caches[cache_server] = latency
            idx = idx + 1

        en = Endpoint(endpoint_id, latency_to_caches, latency_to_dc)
        endpoints.append(en)

        endpoint_id = endpoint_id + 1
        no_endpoints = no_endpoints - 1

    debug(endpoints)

    requests = []
    while(no_requests > 0):
        (video_id, endpoint_id, reqs) = intTuple(lines[idx])


        requests.append( Request(video_id, endpoint_id, reqs) )
        idx = idx + 1
        no_requests = no_requests - 1

    debug(requests)

    idx = 2

    return (caches, endpoints, requests, videos)


def generate_candidates(requests, endpoints, videos):
    candidates = []
    for r in requests:
        ep = endpoints[r.endpoint_id]
        for cache_id in ep.cache_map.keys():
            latency_saving = ep.data_center_latency - ep.cache_map[cache_id]
            reward = r.n_requests * latency_saving / videos[r.video_id].size
            candidate = Candidate(r.video_id, r.endpoint_id, reward, cache_id)
            candidates.append(candidate)
    return candidates


def main():
    (caches, endpoints, requests, videos) = parseInputs()
    candidates = generate_candidates(requests, endpoints, videos)
    assigned_caches = find_solution(candidates, caches)
    write_solution(assigned_caches)
    # your program here


main()
