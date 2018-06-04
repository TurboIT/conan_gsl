from conans import ConanFile, CMake, tools


class GslConan(ConanFile):
    name = "GSL"
    version = "2.0"
    license = "MIT License"
    url = "https://github.com/audiocard/conan_gsl.git"
    description = "The Guideline Support Library (GSL) for C++."
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    generators = "cmake"
    export_sources="include/*"
    no_copy_source = "true"

    def source(self):
        self.run("git clone https://github.com/audiocard/GSL.git")
        self.run("cd GSL && git checkout master")
        # This small hack might be useful to guarantee proper /MT /MD linkage
        # in MSVC if the packaged project doesn't have variables to set it
        # properly
        tools.replace_in_file("GSL/CMakeLists.txt", "project(GSL CXX)",
                              '''PROJECT(GSL CXX)
include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()''')

    def build(self):
        cmake = CMake(self)
        cmake.verbose = True
        cmake.configure(source_folder="GSL")
        cmake.build()

    def package(self):
        self.copy(pattern="*", dst="include", src="GSL/include")

