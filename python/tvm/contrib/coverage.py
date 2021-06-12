import tvm
import numpy as np

total = tvm.get_global_func("tvm.contrib.coverage.total")
now = tvm.get_global_func("tvm.contrib.coverage.now")
# Because `tvm.contrib.coverage.now` relies on tvm's registry function, so after 
# calling `reset`, the coverage will not be ZERO (but very small, e.g., 6).
reset = tvm.get_global_func("tvm.contrib.coverage.reset")

_hitmap_handler = tvm.get_global_func("tvm.contrib.coverage.hitmap")
def hitmap():
    return np.frombuffer(_hitmap_handler(), dtype=np.int8, count=total()) 
