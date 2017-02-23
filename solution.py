#!/usr/bin/env python 

def find_solution(candidates, caches):
    candidates.sort(key=lambda x: x.reward, reverse=True)
    number_of_caches = len(caches)
    total_reward = 0
    full_caches = set()
    for c in candidates:
        is_full = caches[c.cache_id].add(c.video)
        if is_full:
            full_caches.add(c.cache_id)
            if len(full_caches) == number_of_caches:
                break
        else:
            total_reward += c.reward

    print "Total reward: " + str(total_reward)
    return caches

def write_solution(caches):
    lines = []
    for c in caches:
        if not len(c.videos) == 0:
            ids = [str(c.id)] + [str(v.id) for v in c.videos]
            line = " ".join(ids) + "\n"
            lines.append(line)

    with open("result.txt", "a") as f:
        f.writelines(lines)