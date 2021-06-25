cmake_minimum_required(VERSION 3.0.0)
project(test)
add_library(FFT SHARED
    util/FFT.cpp
)
target_include_directories(FFT 
    PUBLIC
    ${PROJECT_SOURCE_DIR}/header
)

add_executable(main
    util/main.cpp
)
target_link_libraries(main
    PRIVATE
    FFT
)