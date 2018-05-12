# Python Screen Record

A Python script that will record your screen (without the cursor) and produce a .avi file named by your input. At the start and end of recording an audible beep is produced.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them

```
Python 3.6
numpy
opencv-python
pillow
sys
os
time
winsound

```

### Installing

A step by step series of examples that tell you have to get a development env running

```
Install all above dependencies 
```

```
Place 'capture.py' file in the directory you wish your videos to be outputted to
```
```
To run the file open your cmd terminal, navigate to the directory your 'capture.py'.
Run the command: catpture.py outputFilename

If all is going well you should here 3 beeps, your output screen should pop up and the terminal should read:
Recording!...
```

```
To stop recording, click the Capture Screen so it is the point of focus and then press escape. 
You should here 2 beeps and your terminal should read:
Recording Saved:
    Filename: outputFilename.avi
    Location: C:\path\to\file
```

## Built With

* [OpenCV](https://opencv.org/) - The web framework used

## Authors

* **Craig Grieve** - *Initial work* - [PurpleBooth](https://github.com/craigrusgrieve)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* [Extension of nikhilkumarsingh's screen_capture.py](https://gist.github.com/nikhilkumarsingh/61601e28d097ee2e4cb9542f01b901b1)
