cmake_minimum_required(VERSION 3.7)

project(dde-manual-content)

#manual
install(DIRECTORY ${CMAKE_SOURCE_DIR}/src/assets/dde DESTINATION /usr/share/deepin-manual/manual-assets/system/dde/)
