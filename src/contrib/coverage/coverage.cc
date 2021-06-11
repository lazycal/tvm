#include <tvm/runtime/registry.h>
#include <memcov.hpp>

TVM_REGISTER_GLOBAL("tvm.contrib.coverage.now")
    .set_body_typed([] () -> int64_t {return memcov::now();});

TVM_REGISTER_GLOBAL("tvm.contrib.coverage.reset")
    .set_body_typed([] () -> void { memcov::reset();});

TVM_REGISTER_GLOBAL("tvm.contrib.coverage.total")
    .set_body_typed([] () -> int64_t {return memcov::total();});
