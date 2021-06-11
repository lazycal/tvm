import tvm

total = tvm.get_global_func("tvm.contrib.coverage.total")
now = tvm.get_global_func("tvm.contrib.coverage.now")
# Because `tvm.contrib.coverage.now` relies on tvm's registry function, so after 
# calling `reset`, the coverage will not be ZERO (but very small, e.g., 6).
reset = tvm.get_global_func("tvm.contrib.coverage.reset")
