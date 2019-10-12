
import sublime
import sublime_plugin

import subprocess

# does a simple reformat, 
# via a linux server(samba) not sure it will 
# and also add a key binding, e.g. { "keys": ["ctrl+alt+f"], "command": "cformat" },
class CformatCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        filename = self.view.file_name()
        print(filename)
        shell_cmd = ["C:\\Program Files\\LLVM\\bin\\clang-format", "-i", filename]
        self.proc = subprocess.Popen(shell_cmd)
        #reloads the window, not sure if a delay will be needed, e.g. time.sleep(0.1)
        self.view.window()

        



