if(USE_COV)
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

    include_directories(${memcov_SOURCE_DIR}/include)

    list(APPEND COMPILER_SRCS ${CMAKE_CURRENT_SOURCE_DIR}/src/contrib/coverage/coverage.cc)
    list(APPEND TVM_LINKER_LIBS memcov)
    list(APPEND TVM_RUNTIME_LINKER_LIBS memcov)
endif()