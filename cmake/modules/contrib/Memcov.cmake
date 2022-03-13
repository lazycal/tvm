if(USE_COV)
    include(FetchContent)
    FetchContent_Declare(
      memcov
      GIT_REPOSITORY https://github.com/ganler/memcov.git
    )

    FetchContent_GetProperties(memcov)

    if(NOT memcov_POPULATED)
      FetchContent_Populate(memcov)
      add_subdirectory(${memcov_SOURCE_DIR} ${memcov_BINARY_DIR})
    endif()

    list(APPEND TVM_LINKER_LIBS memcov)
    list(APPEND TVM_RUNTIME_LINKER_LIBS memcov)

endif()
if(USE_ASTCOV)
    tvm_file_glob(GLOB SOURCECOV_CONTRIB_SRC src/contrib/source_cov.cc)
    list(APPEND COMPILER_SRCS ${SOURCECOV_CONTRIB_SRC})
endif()