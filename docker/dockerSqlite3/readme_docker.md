### OS-specific scripts to build and run containers
The following bash scripts simplify building the container.

| OS  | Building  | Running  |
|---|---|---|
| MacOS  		|  `sh ./build_macOS.sh` |  `sh ./run_macOS.sh` |
| Linux   	|  `sh ./build_linux.sh` | `sh ./run_linux.sh`  |
| Windows 	|  `build_win.bat` 		|  `run_win.bat` |

These files may be found in the directory, `docker/` and the builder require a copy of `Dockerfile` to run which is in the `src` directory, hence why these command should be run from the `src` directory like in the example above.


These files may be found in the main directory and the builder requires a copy of Dockerfile to run. The Dockerfile is found in the main directory and so it is recommended that the user stay in the main and enter the command, `sh ./build_macOS.sh` or similar to build a container. To run the container, type the command `sh ./run_macOS.sh`. Use an equivalent command for each OS. To run a Windows batch file, then the command can simply be entered as `build_win.bat` and then 'run_win.bat' into the Windows Command prompt.
