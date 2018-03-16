# Goto Folder

A Sublime Text 3 plugin that opens selected file or folder in your filemanager

## Installation

## Usage

### Package Control

* Open the Sublime Text Command Palette
* Select `Package Control: Install Package`
* Search for `Goto Folder`


### Git 

* Open the Sublime Text `Packages` directory with `Preferences > Browse Packages`
* From inside the `Packages` directory, clone the repository: 
```bash
$ git clone https://github.com/screamingsnake/goto-folder.git
```

### Manual

* Download a [releases](https://github.com/screamingsnake/goto-folder/releases) .zip archive
* Unzip the archive
* Change the extracted folder name to `Goto Folder`
* Open the Sublime Text `Packages` directory with `Preferences > Browse Packages`
* Copy the `Goto Folder` folder to the `Packages` directory


## Usage

You can access the command via Context menu, Sidebar, Command Palette or Shortcut. Inside a file, press <kbd>CTRL</kbd>+<kbd>SHIFT</kbd>+<kbd>O</kbd> or <kbd>CMD</kbd>+<kbd>SHIFT</kbd>+<kbd>O</kbd> on **macos** and the directory where the file is located will be opened in your default file manager.
You also can right click on a folder in your sidebar and select `Goto Folder`.   

There are two other options to run the command.
* **Command Palette**: Just press <kbd>CTRL</kbd>+<kbd>SHIFT</kbd>+<kbd>P</kbd> or <kbd>CMD</kbd>+<kbd>SHIFT</kbd>+<kbd>P</kbd> on **macos** and type `Goto Folder`. 
* **Context Menu**: Right click in your file and select `Goto Folder`

## Keybindings

These are the default keybindings. You can change it if you want a different keybinding

### macos

```json
[
	{"keys": ["super+shift+o"], "command": "go_to_folder", "args": {"file_path": "${file_path}", "open": "file_manager"}}
]
```

### Windows and Linux

```json
[
	{"keys": ["ctrl+shift+o"], "command": "go_to_folder", "args": {"file_path": "${file_path}", "open": "file_manager"}}
]
```

## License

This plugin is published under the [MIT License](https://github.com/screamingsnake/goto-folder/blob/master/LICENSE)

