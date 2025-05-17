cmake_minimum_required(VERSION 3.10)
project(GrayscaleImageProcessing)

set(CMAKE_CXX_STANDARD 17)

include_directories(include)

add_subdirectory(external/googletest)

enable_testing()

set(IMAGE_PROCESSING_LIB_PATH ${CMAKE_SOURCE_DIR}/lib/libimage_processing.a)
add_library(image_processing STATIC IMPORTED)
set_target_properties(image_processing PROPERTIES IMPORTED_LOCATION ${IMAGE_PROCESSING_LIB_PATH})

add_executable(test_grayscale test/test_image_processing.cpp)
add_executable(convert_grayscale src/main.cpp)
target_link_libraries(test_grayscale image_processing gtest_main)
target_link_libraries(convert_grayscale image_processing)

include(GoogleTest)
gtest_discover_tests(test_grayscale)
