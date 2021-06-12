#include <tvm/runtime/registry.h>
#include <memcov.hpp>

TVM_REGISTER_GLOBAL("tvm.contrib.coverage.hitmap")
    .set_body_typed([] {
        TVMByteArray byte_arr{};
        byte_arr.data = reinterpret_cast<const char*>(memcov::ptr());
        byte_arr.size = memcov::total();
        return byte_arr;
    });

TVM_REGISTER_GLOBAL("tvm.contrib.coverage.now")
    .set_body_typed([] () -> int64_t {return memcov::now();});

TVM_REGISTER_GLOBAL("tvm.contrib.coverage.reset")
    .set_body_typed([] { memcov::reset();});

TVM_REGISTER_GLOBAL("tvm.contrib.coverage.total")
    .set_body_typed([] () -> int64_t {return memcov::total();});
