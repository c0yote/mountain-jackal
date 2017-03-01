# mountain-jackal

Supporting Great Uncle Bumblefuck's effort to build a Maglocking Radial Plasma CNC cutter.

https://www.youtube.com/watch?v=IllVwt6CRJQ

## Development Environment

This section will explain how to setup the development environment for the application.

:warning: Python 3.4 is required until a bug is resolved for 3.5 or greater. :warning:

Change to the project directory and create the virtual environment:
```
virtualenv -p C:\Python34\python.exe .\.env
```

Activate the virtual environment:
```
.env\Scripts\activate.bat
```

Install the requirements:
```
pip install -r requirements.txt
```

## How to Try Algorithms

Open `control.py` and you can create scenario code for the simulator to run through by replacing the code in the `algorithm` function.

Right now it duplicates what AvE's machine is doing.

This code is hacky as fuck and was smashed out over the course of a couple hours in the middle of the night.  I can try to make it a little more robust or featureful if necessary.  Open an issue if there is a feature or change you need in order to support algorithm work.
