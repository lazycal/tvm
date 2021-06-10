include(FetchContent)
FetchContent_Declare(
  memcov
  GIT_REPOSITORY https://github.com/ganler/memcov.git
)

FetchContent_GetProperties(protobuf)

if(NOT memcov_POPULATED)
  FetchContent_Populate(memcov)
  add_subdirectory(${memcov_SOURCE_DIR} ${memcov_BINARY_DIR})
endif()

TARGET_COMPILE_OPTIONS(tvm_objs PRIVATE -fsanitize-coverage=trace-pc-guard)
TARGET_COMPILE_OPTIONS(tvm_runtime_objs PRIVATE -fsanitize-coverage=trace-pc-guard)
TARGET_LINK_LIBRARIES(tvm PRIVATE memcov)
TARGET_LINK_LIBRARIES(tvm_runtime PRIVATE memcov)
