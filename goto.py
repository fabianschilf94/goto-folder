####################
# 
# Name: GoTo Folder Sublime Text 3 Plugin
# Author: Fabian Schilf (Screamingsnake)
# Version: 1.0
# Date: 2018-03
#
####################

import sublime, sublime_plugin

class GoToFolderCommand(sublime_plugin.WindowCommand):

	def run(self):

		self._path = None
		self._active_view = None


	def get_target_path(self):
		pass


	def check_target_path(self):
		pass