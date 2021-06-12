import tvm

# Because `tvm.contrib.coverage.now` relies on tvm's registry function, so after 
# calling `reset`, the coverage will not be ZERO (but very small, e.g., 6).
reset = tvm.get_global_func("tvm.contrib.coverage.reset")

get_total = tvm.get_global_func("tvm.contrib.coverage.get_total")
get_now = tvm.get_global_func("tvm.contrib.coverage.get_now")

set_total = tvm.get_global_func("tvm.contrib.coverage.set_total")
set_now = tvm.get_global_func("tvm.contrib.coverage.set_now")

get_hitmap = tvm.get_global_func("tvm.contrib.coverage.get_hitmap")
set_hitmap = tvm.get_global_func("tvm.contrib.coverage.set_hitmap")
