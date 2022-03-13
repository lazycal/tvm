// for flushing control of source-based coverage 
// see https://clang.llvm.org/docs/SourceBasedCodeCoverage.html#using-the-profiling-runtime-without-static-initializers

extern "C" int __llvm_profile_runtime=0;
extern "C" void __llvm_profile_initialize_file(void);
extern "C" int __llvm_profile_write_file(void);
extern "C" const char * __llvm_profile_get_filename(void);

extern "C" void wrap_llvm_profile_initialize_file() {
  __llvm_profile_initialize_file();
}

extern "C" void wrap_llvm_profile_write_file() {
  __llvm_profile_write_file();
}

extern "C" const char *wrap_llvm_profile_get_filename() {
  return __llvm_profile_get_filename();
}