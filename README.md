# Sublime

# SkelsPlugin
  - call the following programs
     + clang-format
     + vim
# Other useful items sublime
## Packages 
  - CMake
  - Copy as HTML
  - FileSystem Autocompletion
  - MarkdownPreview
  - Package Control
  - SmartMarkdown
  - Table Editor
  - Therme Spacegray


## smartdown smart_floding
```json
	// For Markdowns this seems to allow SmartMarkdown do smart folding on all headers in SublimeText4
	// Ctrl as the for Table editor
	{ "keys": ["ctrl+tab"], "command": "smart_folding", "context":
		[
			{ "key": "selector", "operator": "equal", "operand": "text.html.markdown" }
		]
	},
```
