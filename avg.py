#!/usr/bin/env python

import json

with open("json_stat", "r") as f:
    results = json.loads(f)

avg = {}

for rpc, lst in results.items():
    avg[rpc] = {}
    for tp, vals in lst.items():
        avg[rpc][tp] = 0
        for v in vals:
            avg[rpc][tp] += v
        avg[rpc][tp] /= len(vals)

print avg
