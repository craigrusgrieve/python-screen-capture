import sys
import os
import time
import numpy as np
import cv2
from PIL import ImageGrab
import winsound


class capture:
    """
    Captures the screen and outputs a .avi file in the same file location as capture.py
    """

    def __init__(self, filename="capture", fps=25, resolution=(1366, 768)):
        """
        Sets up the video writer

        INPUTS:
        filename: (string) name of the file you want - .avi will be appended
        fps: (int) frames per second
        resolution: (tuple) screen resolution
        """

        self.fourcc = cv2.VideoWriter_fourcc(*'XVID')
        self.out = cv2.VideoWriter(
            filename + '.avi', self.fourcc, fps, resolution)
        self.fps = int(fps)
        self.filename = filename + ".avi"

    def beepStart(self):
        """ Creates a beep sequence on windows """

        winsound.Beep(1000, 300)
        time.sleep(0.3)
        winsound.Beep(1000, 300)
        time.sleep(0.3)
        winsound.Beep(1000, 1000)

    def beepEnd(self):
        """ Creates a beep sequence on windows """
        winsound.Beep(1000, 250)
        time.sleep(0.01)
        winsound.Beep(1250, 250)

    def record(self):
        """
        records screen captured frames and prepares them for output
        """

        self.beepStart()  # beeps before recording starts
        print("Recording!...")

        while True:
            img = ImageGrab.grab()  # get the screen image - excludes the cursor
            imgNp = np.array(img)  # converts image to numpy array

            # sets image to normal colors
            frame = cv2.cvtColor(imgNp, cv2.COLOR_BGR2RGB)

            # shows the screen you're recording
            cv2.imshow("Screen Capture", frame)

            self.out.write(frame)

            if cv2.waitKey(1) == 27:  # quit and save
                return True
                break
            if cv2.waitKey(1) == ord('`'):  # quit and no save
                return False
                break

    def save(self):
        """ Saves the stream to .avi file """

        self.out.release()
        cv2.destroyAllWindows()  # closes the displayed imshow()
        self.beepEnd()  # beeps after recording has ended

        """ Prints success """
        print("Recording Saved:")
        print("    Filename: {}".format(self.filename))
        print("    Location: {}".format(os.getcwd()))

    def exit(self):
        cv2.destroyAllWindows()  # closes the displayed imshow()
        self.beepEnd()  # beeps after recording has ended

        print("Recording Failed to save:")  # prints failure


if __name__ == "__main__":
    """  """
    try:
        c = capture(sys.argv[1])
        rec = c.record()

        if rec == True:
            c.save()

        if rec == False:
            c.exit()
    except IndexError:
        c = capture()
        rec = c.record()

        if rec == True:
            c.save()

        if rec == False:
            c.exit()
    except e:
        print("failed to Initialize Screen Capture... {}".format(e))
