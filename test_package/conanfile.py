#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile
import os
import sys

name     = "WafGenerator"
version  = "0.0.3"
username = os.getenv("CONAN_USERNAME", "paulobrizolara")
channel  = os.getenv("CONAN_CHANNEL", "testing")

class ExampleConanFile(ConanFile):
	build_policy = "missing"
	settings = "os", "compiler", "build_type", "arch"
	requires = (
		"%s/%s@%s/%s" % (name, version, username, channel),
		"zlib/1.2.11@conan/stable",
	)

	generators = "Waf"

	def imports(self):
		self.copy("*.dll", dst="bin", src="bin") # From bin to bin
		self.copy("*.dylib*", dst="bin", src="lib") # From lib to bin

	def build(self):
		self.run("python waf configure build -o \"%s\"" % os.getcwd() , cwd=self.source_folder)

	def test(self):
		if sys.platform == 'win32':
			exec_str = "example"
		else: exec_str = os.path.join(".", "example")
		self.run(exec_str)
