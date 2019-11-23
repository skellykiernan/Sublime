import sublime
import sublime_plugin

import subprocess


class Open_in_vimCommand(sublime_plugin.TextCommand): 
    def __init__(self, view):
        # At moment must be set 
        settings = sublime.load_settings('DerekPlugins.sublime-settings')
        self.gvim_path = settings.get('gvim_path')

        # Note I have overwritten a constuctor this works not sure why, change settings
        self.view = view

    def run(self, edit):
        filename = self.view.file_name()

        sel  = self.view.sel()
        # the first selection that maybe iterated over, adding 1 for to ensure start line numbering from 1 rather than 0
        line_sel  = self.view.rowcol(sel[0].begin())[0] + 1

        if filename == None:
            shell_cmd = [self.gvim_path]
        else:
            line_sel_str = "+" + str(line_sel)
            shell_cmd = [self.gvim_path, "--remote-silent", line_sel_str, filename]

        print(shell_cmd)

        self.proc = subprocess.Popen(shell_cmd)

