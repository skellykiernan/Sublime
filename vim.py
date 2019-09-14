import sublime
import sublime_plugin

import subprocess


class Open_in_vimCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        filename = self.view.file_name()

        sel  = self.view.sel()
        # the first selection that maybe iterated over, adding 1 for to ensure start line numbering from 1 rather than 0
        line_sel  = self.view.rowcol(sel[0].begin())[0] + 1
        print(line_sel)

        if filename == None:
            shell_cmd = ["C:\\Program Files (x86)\\Vim\\vim80\\gvim.exe"]
        else:
            line_sel_str = "+" + str(line_sel)
            shell_cmd = ["C:\\Program Files (x86)\\Vim\\vim80\\gvim.exe", "--remote-silent", line_sel_str, filename]

        print(shell_cmd)

        self.proc = subprocess.Popen(shell_cmd)

