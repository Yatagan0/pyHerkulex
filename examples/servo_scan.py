"""
@package: pyHerkulex
@name: servo.py
@author: Achu Wilson (achuwilson@gmail.com), Akhil Chandran  (akhilchandran.t.r@gmail.com)
@version: 0.1

This is a python library for interfacing the Herkulex range of smart 
servo motors manufactured by Dongbu Robotics.

The library was created by Achu Wilson (mailto:achu@sastrarobotics.com) 
for the internal projects of Sastra Robotics

This free software is distributed under the GNU General Public License.
See http://www.gnu.org/licenses/gpl.html for details.

For usage of this code for  commercial purposes contact Sastra Robotics 
India Pvt. Ltd. (mailto:contact@sastrarobotics.com)




This is an example script to connect to a Herkulex bus & scan for the servos

"""

import herkulex
from herkulex import servo

#connect to the serial port
#first is the serial port, probably /dev/ttyUSB0 is=f your are using linux and e.g. COM3 if you are using Windows
#second argument is the baud rate, 115200 is teh default value
herkulex.connect("/dev/ttyUSB0",115200)

#scan for servos, it returns a tuple with servo id & model number
#optionnal argument doPrint allows to check what is happening
servos = herkulex.scan_servos(doPrint=True)

print servos