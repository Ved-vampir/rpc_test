#!/usr/bin/env python

import json

with open("json_stat", "r") as f:
    results = json.load(f)

avg = {}

for rpc, lst in results.items():
    avg[rpc] = {}
    for tp, dts in lst.items():
        avg[rpc][tp] = {}
        for dt, vals in dts.items():
            avg[rpc][tp][dt] = 0
            for v in vals:
                
                avg[rpc][tp][dt] += v
            avg[rpc][tp][dt] /= len(vals)

with open("json_stat_avg", "w") as f:
    json.dump(avg, f, indent=4)

