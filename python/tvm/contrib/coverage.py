from tvm._ffi.base import _LIB
import ctypes
import ctypes.util

# Because `tvm.contrib.coverage.now` relies on tvm's registry function, so after 
# calling `reset`, the coverage will not be ZERO (but very small, e.g., 6).
reset = _LIB.mcov_reset

push = _LIB.mcov_push_coverage
pop = _LIB.mcov_pop_coverage

get_total = _LIB.mcov_get_total
get_now = _LIB.mcov_get_now

set_now = _LIB.mcov_set_now
libc = ctypes.CDLL(ctypes.util.find_library('c'))
libc.free.argtypes = [ctypes.c_void_p]

_char_array = ctypes.c_char * get_total()

def get_hitmap():
    hitmap_buffer = bytearray(get_total())
    _LIB.mcov_copy_hitmap(_char_array.from_buffer(hitmap_buffer))
    return hitmap_buffer

def set_hitmap(data):
    assert len(data) == get_total()
    _LIB.mcov_set_hitmap(_char_array.from_buffer(data))

init_src_coverage = lambda: _LIB.wrap_llvm_profile_initialize_file()
write_src_coverage = lambda: _LIB.wrap_llvm_profile_write_file()

try:
    _LIB.wrap_llvm_profile_get_filename.restype = ctypes.c_void_p
except:
    pass
def get_src_coverage_filename():
    ptr = _LIB.wrap_llvm_profile_get_filename()
    result = ctypes.cast(ptr, ctypes.c_char_p).value.decode()
    libc.free(ptr)
    return result
