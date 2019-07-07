# -*- coding: utf-8 -*-

from conans import ConanFile, tools
import os


class CutlassConan(ConanFile):
    name = "cutlass"
    version = "1.3.0"
    description = "CUDA Templates for Linear Algebra Subroutines"
    topics = ("cuda", "cutlass", "deep-learning", "header-only")
    url = "https://github.com/Hopobcn/conan-cutlass"
    homepage = "https://github.com/NVIDIA/cutlass"
    author = "Hopobcn <hopobcn@gmail.com>"
    license = "BSD-3-Clause"
    no_copy_source = True

    exports = ["LICENSE.TXT"]

    _source_subfolder = "source_subfolder"

    def source(self):
        sha256 = "998657c88917ece065d2f9fc2ec977dbb5c117436b989721fc9a8b147e906ff3"
        tools.get("{0}/archive/v{1}.tar.gz".format(self.homepage, self.version))
        extracted_dir = self.name + "-" + self.version
        os.rename(extracted_dir, self._source_subfolder)

    def package(self):
        include_folder = os.path.join(self._source_subfolder, "cutlass")
        self.copy(pattern="LICENSE", dst="licenses", src=self._source_subfolder)
        self.copy(pattern="*", dst="include/cutlass", src=include_folder)

    def package_id(self):
        self.info.header_only()
