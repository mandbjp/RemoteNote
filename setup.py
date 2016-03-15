# -*- coding: utf-8 -*-
from distutils.core import setup
import py2exe

# @see http://shrkw.hatenablog.com/entry/20080825/py2exe_with_tkinter

option = {
    "compressed"    :    1,
    "optimize"      :    2,
    "bundle_files"  :    1
}

setup(
    options = {
        "py2exe"    :    option
    },

    windows = [
        {
            "script": "main.py",
            # "icon_resources": [(1, "py.ico")]
        }
    ],
    zipfile=None
)
