# mountain-jackal

Supporting Great Uncle Bumblefuck's effort to build a Maglocking Radial Plasma CNC cutter.

[AvE's Vidjeo](https://www.youtube.com/watch?v=IllVwt6CRJQ)
[About this Sim Video](https://www.youtube.com/watch?v=w2XD-Sr_X1I)

## Screenshot

![Alt text](screenshot.png?raw=true "Screenshot")

## Basic Development Environment

1. Install Python 3.4 (Version important!)
2. Download the source.
3. Extract it to a folder.
4. Open a command prompt and change directory to the source folder.
5. Run `pip install -r requirements.txt`
6. Run `python demo.py`

## Advanced Development Environment

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

To run the simulation:
```
python demo.py
```

## How to Try Algorithms

Open `control.py` and you can create scenario code for the simulator to run through by replacing the code in the `algorithm` function.

Right now it duplicates what AvE's machine is doing.

This video explains how to use the simulation: https://www.youtube.com/watch?v=w2XD-Sr_X1I

This code is hacky as fuck and was smashed out over the course of a couple hours in the middle of the night.  I can try to make it a little more robust or featureful if necessary.  Open an issue if there is a feature or change you need in order to support algorithm work.
