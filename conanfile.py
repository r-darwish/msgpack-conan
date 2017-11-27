#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, tools
import os


class LibnameConan(ConanFile):
    name = "msgpack"
    version = "2.1.5"
    url = "https://github.com/bincrafters/conan-libname"
    description = "MessagePack implementation for C and C++"
    license = "https://raw.githubusercontent.com/msgpack/msgpack-c/master/LICENSE_1_0.txt"

    def source(self):
        source_url = "https://github.com/msgpack/msgpack-c"
        tools.get("{0}/archive/cpp-{1}.tar.gz".format(source_url, self.version))
        extracted_dir = self.name + "-c-cpp-" + self.version
        os.rename(extracted_dir, "sources")

    def package(self):
        self.copy(pattern="LICENSE_1_0.txt", src="sources")
        self.copy(pattern="*", dst="include", src="sources/include")

    def package_id(self):
        self.info.header_only()
