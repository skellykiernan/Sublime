
import sublime
import sublime_plugin

import subprocess

# does a simple reformat if a .clang_format file is present and the current file is saved
# and also add a key binding, e.g. { "keys": ["ctrl+alt+f"], "command": "cformat" },
class CformatCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        filename = self.view.file_name()
        print(filename)
        shell_cmd = ["C:\\Program Files\\LLVM\\bin\\clang-format", "-i", filename]
        # hoping the wait will till file is written where requesting the window loads the saved file
        # if on a netwrok drive likely to be a noticable delay
        self.proc = subprocess.Popen(shell_cmd, shell=True).wait()
        self.view.window()





