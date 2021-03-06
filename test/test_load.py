#!/usr/bin/python

import rabinpoly

lib = rabinpoly

window_size = 32
min_segment_size = 1024
avg_segment_size = 8192
max_segment_size = 65536

rp = lib.rp_new(window_size, avg_segment_size, min_segment_size, 
        max_segment_size, 1024*128)
assert rp.contents.window_size == window_size
assert rp.contents.T[1] == 13827942727904890243

# from guppy import hpy; hp=hpy()
# print hp.heap()
lib.rp_free(rp)
# print hp.heap()
