####################
# 
# Name: GoTo Folder Sublime Text 3 Plugin
# Author: Fabian Schilf (Screamingsnake)
# Version: 1.0
# Date: 2018-03
#
####################

import sublime, sublime_plugin, os

class GoToFolderCommand(sublime_plugin.WindowCommand):

	def run(self, **kwargs):

		# setting global vars
		self.args = sublime.load_settings("gotofolder.sublime-settings")
		self.folder = self.window.extract_variables()["file_path"]
		self.shell = None

		# check if custom shell is set

		# | added if shell issue is fixed | 
		# if self.args.get("shell_path"):
		# 	self.shell = self.args.get("shell_path")

		# check if sidebar was clicked
		if "paths" in kwargs:
			self.folder = kwargs["paths"][0]
		
		# open folder in file manager
		if kwargs["open"] == "file_manager":
			self.open_in_file_manager()

		# open folder in default shell or given shell in settings
		if kwargs["open"] == "shell":
			self.open_in_shell()

		


	def open_in_file_manager(self):
		if os.path.isdir(self.folder):
			self.window.run_command("open_dir", {"dir": self.folder})
		else:
			sublime.error_message("Could not find {}".format(self.folder))


	def open_in_shell(self):
		pass