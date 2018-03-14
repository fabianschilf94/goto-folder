import sublime, sublime_plugin

class GoToFolderTestCommand(sublime_plugin.WindowCommand):

	def run(self, **kwargs):
		self.path = None
		self.active_view = None
		self.shell = None

		self.settings = sublime.load_settings("gotofolder.sublime-settings")

		if self.settings.get("shell_path"):
			self.shell = self.settings.get("shell_path")

		if kwargs["open"] == "explorer":
			self.open_in_explorer()
		elif kwargs["open"] == "shell":
			self.open_in_shell()


	def get_target_path(self):
		pass


	def check_target_path(self):
		pass


	def open_in_explorer(self):
		pass


	def open_in_shell(self):
		pass