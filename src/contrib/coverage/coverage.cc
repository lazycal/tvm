#include <tvm/runtime/registry.h>
#include <memcov.hpp>

TVM_REGISTER_GLOBAL("tvm.contrib.coverage.reset")
    .set_body_typed([] { memcov::reset();});

TVM_REGISTER_GLOBAL("tvm.contrib.coverage.get_hitmap")
    .set_body_typed([] {
        TVMByteArray arr;
        arr.data = memcov::ptr();
        arr.size = memcov::get_total();
        return arr;
    });

TVM_REGISTER_GLOBAL("tvm.contrib.coverage.set_hitmap")
    .set_body_typed([] (const std::string& src) {
        char* dst = memcov::ptr();
        std::memcpy(dst, src.c_str(), src.length());
    });

TVM_REGISTER_GLOBAL("tvm.contrib.coverage.set_now")
    .set_body_typed([] (int64_t n) { memcov::set_now(n);});

TVM_REGISTER_GLOBAL("tvm.contrib.coverage.get_now")
    .set_body_typed([] () -> int64_t { return memcov::get_now();});

TVM_REGISTER_GLOBAL("tvm.contrib.coverage.set_total")
    .set_body_typed([] (int64_t t) { memcov::set_total(t);});

TVM_REGISTER_GLOBAL("tvm.contrib.coverage.get_total")
    .set_body_typed([] () -> int64_t { return memcov::get_total();});
