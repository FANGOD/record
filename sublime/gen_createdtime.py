# coding: utf-8
"""
User Name: fangod@.cn
Date Time: 2020-09-02 11:22:33
File Name: gen_createdtime.py @v1.0
"""
import datetime
import sublime_plugin


class AddDateTimeStampCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        self.view.run_command("insert_snippet", {"contents": "%s" % datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")})


class AddDateStampCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        self.view.run_command("insert_snippet", {"contents": "%s" % datetime.datetime.now().strftime("%Y-%m-%d")})


class AddTimeStampCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        self.view.run_command("insert_snippet", {"contents": "%s" % datetime.datetime.now().strftime("%H:%M:%S")})
