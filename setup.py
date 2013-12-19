#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from distutils.core import setup

setup(
        name = "show-my-ip",
        version = "0.0.1",
        description = "Simple utility to show your local and global IP.",
        author = "Malte Bublitz",
        author_email = "malte70@malte-bublitz.de",
        url = "https://github.com/malte70/show-my-ip",
        packages = ["show_my_ip"],
        scripts = ["bin/show-my-ip"]
        )
