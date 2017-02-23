#!/usr/bin/env python 

def find_solution(candidates, caches, videos):
    candidates.sort(key=lambda x: x.reward, reverse=True)
    number_of_caches = len(caches)
    total_reward = 0
    total_reward_original = 0
    full_caches = set()
    fulfilled_requests = set()
    for c in candidates:
        if not candidate_id(c) in fulfilled_requests:
            is_full = caches[c.cache_id].add_video(videos[c.video_id])
            if is_full:
                full_caches.add(c.cache_id)
                if len(full_caches) == number_of_caches:
                    break
            else:
                total_reward += c.reward
                total_reward_original += c.reward * videos[c.video_id].size
                fulfilled_requests.add(candidate_id(c))


    print "Total reward: " + str(total_reward)
    print "Total reward original: " + str(total_reward_original)
    return caches

def candidate_id(candidate):
    return str(candidate.video_id) + "-" + str(candidate.endpoint_id)

def write_solution(caches):
    lines = []
    for c in caches:
        if not len(c.videos) == 0:
            ids = [str(c.id)] + [str(v.id) for v in c.videos]
            line = " ".join(ids) + "\n"
            lines.append(line)
    lines = [str(len(lines)) + "\n"] + lines
    with open("result.txt", "w+") as f:
        f.writelines(lines)