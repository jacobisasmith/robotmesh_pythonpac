
# Vex V5 controller Python API for Robot Mesh
# Copyright 2017 Robot Mesh
# Strictly for Autofill, NON-FUNCTIONAL
# Adapted 2021 Jacob Smith

# Empty marker class. Should only contain static fields
class Enum:
    pass


# Ports. This is not an enum in C++...
class Ports(Enum):
    PORT1 = 0
    PORT2 = 1
    PORT3 = 2
    PORT4 = 3
    PORT5 = 4
    PORT6 = 5
    PORT7 = 6
    PORT8 = 7
    PORT9 = 8
    PORT10 = 9
    PORT11 = 10
    PORT12 = 11
    PORT13 = 12
    PORT14 = 13
    PORT15 = 14
    PORT16 = 15
    PORT17 = 16
    PORT18 = 17
    PORT19 = 18
    PORT20 = 19
    PORT21 = 20
    PORT22 = 21


class PercentUnits(Enum):
    """A unit of percentage."""
    # A unit type that represents a value from 0% to 100%
    PCT = 0


class TimeUnits(Enum):
    """A unit of time."""
    # A unit type that represents a value of time in seconds.
    SEC = 0
    # A unit type that represents a value of time in milliseconds.
    MSEC = 1


class CurrentUnits(Enum):
    """A unit of electrical current."""
    # A unit type that represents a value of electrical current in amps.
    AMP = 0


class PowerUnits(Enum):
    """A unit of power."""
    # A unit type that represents a value of power in watts.
    WATT = 0


class TorqueUnits(Enum):
    """A unit of torque."""
    # A unit type that represents a value of torque in Newton Meters.
    NM = 0
    # A unit type that represents a value of torque in pounds per inch.
    IN_LB = 1


class RotationUnits(Enum):
    """A unit of rotation."""
    # A unit type that represents a value of rotation in degrees.
    DEG = 0
    # A unit type that represents a value of rotation in revolutions.
    REV = 1
    # A unit type that represents a value of rotation in raw data form.
    RAW = 99


class VelocityUnits(Enum):
    """A unit of velocity."""
    # A unit type that represents a value of velocity as a percentage from 0% to 100%.
    PCT = PercentUnits.PCT
    # A unit type that represents a value of velocity as rotations per minute.
    RPM = 1
    # A unit type that represents a value of velocity as volts.
    VOLT = 2


class DistanceUnits(Enum):
    """A unit of distance."""
    # A unit type that represents a value of distance in millimeters.
    MM = 0,
    # A unit type that represents a value of distance in inches.
    IN = 1,


class AnalogUnits(Enum):
    """A unit of analog units."""
    # A unit type that represents a value of analog units as a percentage from 0% to 100%.
    PCT = PercentUnits.PCT,
    # A unit type that represents a value of analog units on an 8 bit range.
    RANGE_8BIT = 1
    # A unit type that represents a value of analog units on a 10 bit range.
    RANGE_10BIT = 2
    # A unit type that represents a value of analog units on a 12 bit range.
    RANGE_12BIT = 3
    # A unit type that represents a value of analog units as megavolts.
    MV = 4


# Motor related
# -------------
class DirectionType(Enum):
    """A unit of direction."""
    # A unit type that represents a value of direction for rotating or spinning forward.
    FWD = 0
    # A unit type that represents a value of direction for rotating or spinning backward.
    REV = 1
    # Undefined unit type
    UNDEFINED = 2


class BrakeType(Enum):
    """A unit of brake mode."""
    # A unit type that represents a type of a brake mode as coast. This will cause a motor to coast after turning it off.
    COAST = 0  # kV5MotorBrakeModeCoast
    # A unit type that represents a type of a brake mode as brake. This will cause a motor to brake after turning it off.
    BRAKE = 1  # kV5MotorBrakeModeBrake
    # A unit type that represents a type of a brake mode as hold. This will cause the motor to try to hold is position after turning off.
    HOLD = 2  # kV5MotorBrakeModeHold
    # A unit type that represents a type of a brake mode as undefined.
    UNDEFINED = 3


class GearSetting(Enum):
    """A unit of gear settings"""
    # A unit type that represents a type of gear setting for the stock gears (red). The red gears have a max rpm of 100.
    RATIO36_1 = 0  # kMotorGearSet_36
    # A unit type that represents a type of gear setting for upgraded gears (green). The green gears have a max rpm of 200.
    RATIO18_1 = 1  # kMotorGearSet_18
    # A unit type that represents a type of gear setting for upgraded gears (blue). The blue gears have a max rpm of 600.
    RATIO6_1 = 2  # kMotorGearSet_06


# Brain/LCD related
# -----------------
class Font(Enum):
    """A unit of font type."""
    # A unit type that represents a type of font as mono20.
    MONO_20 = 0
    # A unit type that represents a type of font as mono30.
    MONO_30 = 1
    # A unit type that represents a type of font as mono40.
    MONO_40 = 2
    # A unit type that represents a type of font as mono60.
    MONO_60 = 3

    # A unit type that represents a type of font as prop20.
    PROP_20 = 4
    # A unit type that represents a type of font as prop30.
    PROP_30 = 5
    # A unit type that represents a type of font as prop40.
    PROP_40 = 6
    # A unit type that represents a type of font as prop60.
    PROP_60 = 7

    # not in spec
    # A unit type that represents a type of font as mono15.
    MONO_15 = 8
    # A unit type that represents a type of font as mono12.
    MONO_12 = 9


# Not in use -- the user can configure ports
# by cereating TriDevice derived classes
# class TriportType(Enum):
#    ANALOG_INPUT = 0
#    ANALOG_OUTPUT = 1
#    DIGITAL_INPUT = 2
#    DIGITAL_OUTPUT = 3
#    BUTTON = 4
#    POTENTIOMETER = 5
#    LINE_SENSOR = 6
#    LIGHT_SENSOR = 7
#    GYRO = 8
#    ACCELEROMETER = 9
#    MOTOR = 10
#    SERVO = 11
#    QUAD_ENCODER = 12
#    SONAR = 13
#    MOTOR_S = 14

class ControllerType(Enum):
    PRIMARY = 0  # kControllerMaster
    PARTNER = 1  # kControllerPartner


# corresponds to V5_DeviceType in v5_apitypes.h
class V5DeviceType(Enum):
    NO_SENSOR = 0
    MOTOR = 2
    LED = 3
    ABS_ENC = 4
    BUMPER = 5
    IMU = 6
    RANGE = 7
    RADIO = 8
    TETHER = 9
    BRAIN = 10
    VISION = 11
    ADI = 12
    GYRO = 0x46
    SONAR = 0x47
    GENERIC = 128
    GENERIC_SERIAL = 129
    UNDEFINED = 255


class Color:
    # Re-implementing in Python instead of wrapping vex::color
    # to avoid exceeding the 255 object limit on linked objects

    # Creates a color using a 0xRRGGBB color value.

    @staticmethod
    def set_rgb(r, g, b):
        pass

    @staticmethod
    def set_value(color_value):
        # in C++ this is color::rgb(int32_t), but Python has no overloads
        pass

    # Creates a color using hue, saturation, and brightness values.
    # An integer from 0 to 360 that represents the hue of the color.
    # A double from 0.0 to 1.0 that represents the saturation of the color.
    # A double from 0.0 to 1.0 that represents the brightness of the color.
    # Returns a reference to a color.
    @staticmethod
    def set_hsv(hue, saturation, value):
        pass

    # Creates a color using a hex web color string "#rgb" or "#rrggbb".
    # olor A web color value that defines a specific color.
    # Returns a reference to a color.
    @staticmethod
    def set_web(web_color_str):
        pass

    # Gets the 0xRRGGBB color value
    @staticmethod
    def value():
        # named rgb in python, but analogous to .set_value(v),
        # since rgb setter is an overload
        pass

    # Gets the state of the color's transparency.
    # Returns true if the color is transparent.
    @staticmethod
    def is_transparent():
        pass

    # creator methods, not in C++
    @staticmethod
    def from_rgb(r, g, b):
        col = 0
        col.set_rgb(r, g, b)
        return col

    @staticmethod
    def from_hsv(h, s, v):
        col = 0
        col.set_hsv(h, s, v)
        return col

    @staticmethod
    def from_web(web_color_str):
        col = 0
        col.set_web(web_color_str)
        return col

    # helpers
    @staticmethod
    def _hsv_to_rgb(hue, saturation, value):
        return 0

    @staticmethod
    def _web_to_rgb(web_color_str):
        return 0

    # predefined colors
    BLACK = None
    WHITE = None
    RED = None
    GREEN = None
    BLUE = None
    YELLOW = None
    ORANGE = None
    PURPLE = None
    CYAN = None
    TRANSPARENT = None


# Static fields refer to the class, must initialize after the class
Color.BLACK = 0x000000
Color.WHITE = 0xFFFFFF
Color.RED = 0xFF0000
Color.GREEN = 0x00FF00
Color.BLUE = 0x0000FF
Color.YELLOW = 0xFFFF00
Color.ORANGE = 0xFFA500
Color.PURPLE = 0xFF00FF
Color.CYAN = 0x00FFFF
Color.TRANSPARENT = -1  # special case


# Abstract class
class Device:

    def __init__(index=None):
        pass

    # Get the device type
    # V5DeviceType enum value
    @staticmethod
    def type():
        return 0

    # called by the C++ ctor, seems internal
    # void init( int32_t index );

    # Gets the status of what is installed
    # Returns a true Boolean if the triport is installed. Returns a false Boolean if the triport is not installed.
    @staticmethod
    def installed():
        pass

    @staticmethod
    def value():
        return 0


class Devices:

    def __init__():
        pass

    @staticmethod
    def get(index):
        return None

    # Get the V5 device type plugged into a specific port.
    # index Specifies the index to look at for the device.
    # Returns a V5DeviceType enum value.
    @staticmethod
    def type(index):
        return 0

    # Gets the number of VEX devices that are plugged in.
    # Returns an integer that represent the number of vex devices
    @staticmethod
    def number():
        return 0

    # Gets the number of specified devices that are plugged into the V5.
    # type The type of device to look for on the V5.
    # Returns an integer that represents the number of a specific vex devices set by the parameter.
    @staticmethod
    def number_of(type):
        return 0


class Motor(Device):
    # Creates a new motor object on the port specified.
    # index The port index for this motor. The index is zero based.
    # gears Sets the gears setting for the new motor object.
    # reverse Sets the reverse flag for the new motor object.
    def __init__(index, gearSetting=GearSetting.RATIO36_1, reverse=False):

        pass

    # Use this function to reverse setting for the motor.
    # value If set to true, the motor will spin in the reversed direction.
    @staticmethod
    def set_reversed(isReversed):

        pass

    # Sets the velocity of the motor based on the parameters set in the command.
    # This command will not run the motor.  Any subsequent call that does not contain a
    # specified motor velocity will use this value.
    # velocity Set the amount of velocity that the motor should use.
    # units Set what the motor should treat the previous velocity value as.
    @staticmethod
    def set_velocity(velocity, velocityUnits=VelocityUnits.PCT):

        pass

    # Sets the stopping mode of the motor by passing a brake mode as a parameter.
    # mode The stopping mode can be set to coast, brake, or hold.
    @staticmethod
    def set_stopping(brakeType):
        pass

    # Resets the motor's encoder to the value of zero.
    @staticmethod
    def reset_rotation():
        pass

    # Sets the value of the motor's encoder to the value specified in the parameter.
    # value The value of what you want the motor's encoder to be set to.
    # units A rotational unit type that defines how the previous value should be treated as.
    @staticmethod
    def set_rotation(value, rotationUnits=RotationUnits.DEG):
        pass

    # Sets the timeout for the motor. If the motor does not reach its' commanded position prior to the completion of the timeout, the motor will turn off.
    # time The value of the time out expiration.
    # units A time unit that defines how to treat the previous value.
    @staticmethod
    def set_timeout(time, timeUnits=TimeUnits.SEC):
        pass

    # Return the timeout for the motor.
    @staticmethod
    def timeout(timeUnits=TimeUnits.SEC):
        return 0

    # Actions
    # -------

    # Turns on the motor and spins it in a specified direction and velocity (if specified).
    # dir Spin the motor forward by passing FWD, or spin the motor backward by passing REV.
    # velocity Set the amount of velocity that the motor should use. Optional.
    # units Set what the motor should treat the previous velocity value as. Optional.
    @staticmethod
    def spin(directionType, velocity=None, velocityUnits=VelocityUnits.PCT):
        pass

    # Turns on the motor and spins it to an absolute target rotation value at a specified velocity.
    # rotation The motor encoder's target rotation value
    # units A rotational unit type that defines how the previous value should be treated as.
    # velocity Set the amount of velocity that the motor should use.
    # units_v Set what the motor should treat the previous velocity value as.
    # bWaitForCompletition (Optional) If true, your program will wait until the motor reaches the target rotational value. If false, the program will continue after calling this function. By default, this parameter is true.
    # Returns a Boolean that signifies when the motor has reached the target rotation value.
    @staticmethod
    def rotate_to(rotation, rotationUnits=RotationUnits.DEG, velocity=None, velocityUnits=VelocityUnits.PCT):
        pass

    @staticmethod
    def _rotate_wait(waitForCompletion):
        pass

    @staticmethod
    def _on_rotate_done(done):
        pass

    @staticmethod
    def _rotate_to(rotation, rotationUnits=RotationUnits.DEG, velocity=None, velocityUnits=VelocityUnits.PCT):
        return False

    # Turns on the motor and spins it to a relative target rotation value at a specified velocity.
    # rotation The motor encoder's target rotation value
    # units A rotational unit type that defines how the previous value should be treated as.
    # velocity Set the amount of velocity that the motor should use.
    # units_v Set what the motor should treat the previous velocity value as.
    # bWaitForCompletition (Optional) If true, your program will wait until the motor reaches the target rotational value. If false, the program will continue after calling this function. By default, this parameter is true.
    # Returns a Boolean that signifies when the motor has reached the target rotation value.
    @staticmethod
    def rotate_for(rotation, rotationUnits=RotationUnits.DEG, velocity=None, velocityUnits=VelocityUnits.PCT,
                   waitForCompletion=True):
        pass

    @staticmethod
    def _rotate_for(rotation, rotationUnits=RotationUnits.DEG, velocity=None, velocityUnits=VelocityUnits.PCT,
                    waitForCompletion=True):

        return False

    # Turns on the motor and spins it to a relative target time value at a specified velocity.
    # time The value of time that the motor should spin for.
    # units A time unit that defines how to treat the previous value.
    # velocity Set the amount of velocity that the motor should use.
    # units_v Set what the motor should treat the previous velocity value as.
    # Returns a Boolean that signifies when the motor has reached the target time value.
    @staticmethod
    def rotate_for_time(time, timeUnits=TimeUnits.SEC, velocity=None, velocityUnits=VelocityUnits.PCT):
        pass

    # Starts spinning a motor to an absolute target rotation but does not wait for the motor to reach that target.
    # rotation This is the motor encoder's target rotation value
    # units This is a rotational unit type that defines how the previous value should be treated as.
    # velocity Set the amount of velocity that the motor should use.
    # Set what the motor should treat the previous velocity value as.
    @staticmethod
    def start_rotate_to(rotation, rotationUnits=RotationUnits.DEG, velocity=None,
                        velocityUnits=VelocityUnits.PCT):
        pass

    # Starts spinning a motor to a relative target rotation but does not wait for the motor to reach that target.
    # This is the motor encoder's target rotation value
    # This is a rotational unit type that defines how the previous value should be treated as.
    # Set the amount of velocity that the motor should use.
    # Set what the motor should treat the previous velocity value as.
    @staticmethod
    def start_rotate_for(rotation, rotationUnits=RotationUnits.DEG, velocity=None,
                         velocityUnits=VelocityUnits.PCT):
        pass

    # Checks to see if the motor is spinning.
    # Returns a true Boolean if the motor is on and is running. Returns a false Boolean if the motor is off or braking.
    @staticmethod
    def is_spinning():
        pass

    # Determines if the motor is done with its action.
    # If the function returns true, then the motor is done with the action.
    @staticmethod
    def is_done():

        return False

    # Stops the motor using a specified brake mode (or default mode if not specified).
    @staticmethod
    def stop(brakeType=None):
        pass

    # Sets the max torque of the motor.
    # value The value that the motor's max torque should be set to.
    # units The type of torque units that defines how to treat the previous value.
    # BUG: should it be TorqueUnits?
    @staticmethod
    def set_max_torque(maxTorque, torqueUnits=PercentUnits.PCT):
        pass

    # Gets which direction the motor is spinning.
    # Returns an integer that represents the direction that the motor is spinning.
    @staticmethod
    def direction():
        return 0

    # Gets the current rotation  of the motor's encoder.
    # units Defines what the unity type of the value of rotation  that is returned.
    # Returns a double that represents the current rotation of the motor in the units defined in the parameter.
    @staticmethod
    def rotation(rotationUnits=RotationUnits.DEG):
        return 0

    # Gets the current velocity of the motor.
    # units Defines the unit type of the velocity value returned.
    # Returns a double that represents the current velocity of the motor in the units defined in the parameter.
    @staticmethod
    def velocity(velocityUnits=VelocityUnits.PCT):
        return 0

    # Gets the electrical current of the motor.
    # currentUnits Defines the unit type of the electrical current value that is returned.
    # Returns a double that represents the electrical current of the motor in the units defined in the parameter.
    @staticmethod
    def current(currentUnits=CurrentUnits.AMP):
        return 0

    # Gets the power of the motor.
    # powerUnits
    # Returns a double that represents the power of the motor in the units defined in the parameter.
    @staticmethod
    def power(powerUnits=PowerUnits.WATT):
        return 0

    # Gets the torque of the motor.
    # torqueUnits Defines the unit type of torque to be returned.
    # Returns a double that represents the torque of the motor in the units defined in the parameter.
    @staticmethod
    def torque(torqueUnits=TorqueUnits.NM):
        return 0.0

    # Gets the efficiency of the motor.
    # units Defines the unit type of the efficiency value to be returned.
    # Returns the efficiency of the motor in the units defined in the parameter.
    @staticmethod
    def efficiency(percentUnits=PercentUnits.PCT):
        return 0.0

    # Gets the temperature  of the motor.
    # units Defines the unit type of the temperature value to be returned.
    # Returns the temperature of the motor in the units defined in the parameter.
    # BUG in C++ API: using PercentUnits
    @staticmethod
    def temperature(percentUnits=PercentUnits.PCT):
        return 0.0


class VisionObject:  # C++ vex::vision::object
    # NOT linked to an underlying C++ object, for easy access to fields and to avoid Python allocations

    # Creates a new vision object object with all properties set to default values.
    def __init__():
        pass
        # setting attributes here so they can be documented (see PEP 258 Attribute Docstrings)

    @staticmethod
    def id():
        pass

    @staticmethod
    def originX(origin):
        pass

    @staticmethod
    def originY(origin):
        pass

    @staticmethod
    def centerX(center):
        pass

    @staticmethod
    def centerY(center):
        pass

    @staticmethod
    def width(width):
        pass

    @staticmethod
    def height(height):
        pass

    @staticmethod
    def angle(angle):
        pass

    @staticmethod
    def exsists():
        pass

    # Inverts the anlge for this object.
    @staticmethod
    def flip_angle():
        pass

    # Sets all properties for this object to defualt values.
    class clear:

        def __init__():
            pass

        @staticmethod
        def id():
            pass

        @staticmethod
        def originX(origin):
            pass

        @staticmethod
        def originY(origin):
            pass

        @staticmethod
        def centerX(center):
            pass

        @staticmethod
        def centerY(center):
            pass

        @staticmethod
        def width(width):
            pass

        @staticmethod
        def height(height):
            pass

        @staticmethod
        def angle(angle):
            pass

        @staticmethod
        def exsists():
            pass


class VisionSignature:  # C++ vex::vision::signature
    # why is the "rgb" field skipped in the C++ ctor???
    # def __init__(id, , range, type):
    @staticmethod
    def __init__(id, uMin, uMax, uMean, vMin, vMax, vMean, range, type):
        pass


class VisionMode(Enum):  # C++ vex::vision::tMode
    OBJECT_DETECT = 0  # kVisionModeNormal
    MIXED_DETECT = 1  # kVisionTypeColorCode
    LINE_DETECT = 2  # kVisionModeLineDetect
    TEST = 3  # kVisionTypeTest


class VisionWbMode(Enum):  # C++ vex::vision::tWbMode
    AUTOMATIC = 0  # kVisionWBNormal
    START = 1  # kVisionWBStart
    MANUAL = 2  # kVisionWBManual


class VisionLedMode(Enum):  # C++ vex::vision::tLedMode
    AUTOMATIC = 0  # kVisionLedModeAuto
    MANUAL = 1  # kVisionLedModeManual


class VisionWifiMode(Enum):  # C++ vex::vision:tWifiMode
    OFF = 0  # kVisionWifiModeOff
    ON = 1  # kVisionWifiModeOn


class VisionCode:  # C++ vex::vision::code
    # wrap a C++ object... but be prepared to hit a 255 object limit?
    @staticmethod
    def __init__(ids_or_signatures):
        pass


class Vision(Device):
    _MAX_OBJECTS = 16  # C++ VISION_MAX_OBJECTS

    # _DEFAULT_SNAPSHOT_OBJECTS = 8 # C++ VISION_DEFAULT_SNAPSHOT_OBJECTS

    # Creates a new vision object on the port specified. Sets the brightness setting and all of the vision objects settings.
    #  index The port index for this vision. The index is zero based.
    #  bright The vision sensor brightness seting. Values are 0 to 100%
    #  sigs List of signature objects used to setup the detection signatures for this sensor.
    @staticmethod
    def __init__(index, brigthness=None, signatures=None):
        pass

    @staticmethod
    def object_count():
        pass

    @staticmethod
    def _init_core(index, brigthness, signatures):
        pass

    # in superclass: value() -- returns an int

    #  Takes a data sample from the vision sensor.
    #  id_or_sig_or_code The ID or VisionCode or VisionSignature of the object to look for.
    #  count the amount of objects to look for. The largest of the object will be returned. Optional.
    #  Returns the number of objects found from the ID passed in the parameter.
    @staticmethod
    def take_snapshot(id_or_sig_or_code, count=None):
        return 0

    @staticmethod
    def set_signature(signature):
        return False

    @staticmethod
    def get_signature(id, r_signature):
        return False

    @staticmethod
    def set_mode(visionMode):
        return False

    #  VisionMode enum value
    @staticmethod
    def get_mode():
        return 0

    @staticmethod
    def set_brightness(percent):
        return False

    #  percent brightness 0-100
    @staticmethod
    def get_brigthness():
        return 0

    @staticmethod
    def set_white_balance_mode(visionWbMode):
        return False

    #  VisionWbMode enum value
    @staticmethod
    def get_white_balance_mode():
        return 0

    # set a 0xRRGGBB color
    @staticmethod
    def set_white_balance_values(color):
        return False

    #  a 0xRRGGBB number representing the color
    @staticmethod
    def get_white_balance_values():
        return 0

    # Changes the mode of the LED on the vision sensor.
    #  mode The LED mode. Automatic mode will cause the LED color to be controlled by the vision sensor firmware. Manual mode allows the LED color to be controlled by the user program.
    #  Returns true if setting was succesfully saved.
    @staticmethod
    def set_led_mode(visionLedMode):
        return False

    # Gets the mode of the LED from the vision sensor.
    #  Returns a VisionLedMode enum value that represents the current mode of the vision sensor LED.
    @staticmethod
    def get_led_mode():
        return 0

    # Changes the brightness of the LED on the vision sensor when LED is set to manual mode.
    #  percent A percentage of total brightness of the vision sensor LED when in manual mode. Values are 0 to 100. 0 = LED off
    #  Returns true if setting was succesfully saved.
    @staticmethod
    def set_led_brightness(percent):
        return False

    # Gets the brightness of the LED from the vision sensor.
    #  Returns a value between 0 and 100 that represents the current brightness of the vision sensor LED.
    @staticmethod
    def get_led_brightness():
        return 0

    # Changes the color of the LED on the vision sensor when LED is set to manual mode.
    #  red A value from 0 to 255 the represents the intensity of the red color of the LED.
    #  green A value from 0 to 255 the represents the intensity of the green color of the LED.
    #  blue A value from 0 to 255 the represents the intensity of the blue color of the LED.
    #  Returns true if setting was succesfully saved.
    @staticmethod
    def set_led_color(red, green, blue):
        return False

    # Gets the color of the LED from the vision sensor.
    #  a 0xRRGGBB number representing the color
    @staticmethod
    def get_led_color():
        return 0

    @staticmethod
    def set_wifi_mode(visionWifiMode):
        return False

    #  VisionWifiMode enum value
    @staticmethod
    def get_wifi_mode():
        return 0


class ControllerButton:
    #  Use the button class to get values from the controller's buttons.
    @staticmethod
    def __init__(parent, id):
        pass

    # Not implementing -- no callback support
    # def pressed(callback):
    # def released(callback):

    # Gets the staus of a button
    #  Returns a Boolean value based on the pressed states of the button.
    #         If the button is pressed it will return True.
    @staticmethod
    def pressing():
        return False


class ControllerAxis:
    # Use the axis class to get axis values from the controllers joystick.
    @staticmethod
    def __init__(parent, id):
        pass

    # Not implementing -- needs callback support
    # def changed(callback):

    # Gets the value of the axis.
    #  Returns an integer that represents the value of the axis.
    @staticmethod
    def value():
        return 0

    # Gets the position of the axis.
    #  Returns an integer that represents the position of the axis as defined by the unit in the parameter.
    #  units The type of unit that should be returned.
    @staticmethod
    def position(percentUnits=PercentUnits.PCT):
        return 0


class ControllerLcd:
    # Use the lcd class to write to the controller's LCD screen.
    @staticmethod
    def __init__(parent):
        pass

    # Sets the cursor to the row and column number set in the parameters.
    #  row Sets the row number for where the cursor is placed.
    #  col Sets the column number for where the cursor is placed.
    @staticmethod
    def set_cursor(row, col):
        pass

    # Rumbles the controller by a patteren defined by the parameter. Dots equal short while dashes equal long.
    #  str A string that consists of dots and dashes that represent the rumble patteren.
    @staticmethod
    def rumble(rumblePattern):
        pass

    # Print a string to the screen at the cursor location
    #  text object to print, usually a string.
    #        For multiple arguments, use format like "x: %g y: %g" % (x, y) -> "x: 123 y: 456"
    #        Supported format flags are %g (all) %x (hex) %d (int) %f (float)
    @staticmethod
    def print_(text, new_line=True):  # "print" is a Python keyword, and printf implies format string...
        pass

    @staticmethod
    def set_pen_color(color):
        pass

    # Sets the color of the pen to a specified color.
    # hue An integer that represents the hue of the color.
    @staticmethod
    def set_pen_color_hue(hue):
        pass

    # Sets the background fill color of the LCD screen to the specified color.
    # color A color unit where colors can be defined as names.
    @staticmethod
    def set_fill_color(color):
        pass

    @staticmethod
    def set_fill_color_hue(color):
        pass


class Brain:
    @staticmethod
    def __init__():
        pass

    class battery:

        @staticmethod
        def capacity(percentUnits):
            pass

        @staticmethod
        def voltage(voltageUntis):
            pass

        @staticmethod
        def current(currentUnits):
            pass

        @staticmethod
        def temperature(temperatureUnits):
            pass

    def installed():
        pass

    class screen:
        def __init__():
            pass

        #  Use the LCD class to write or draw to the LCD.
        # Sets the cursor to the row and column number set in the parameters.
        #  row Sets the row number for where the cursor is placed.
        #  col Sets the column number for where the cursor is placed.
        @staticmethod
        def set_cursor(row, col):
            pass

        # Sets the font type to be displayed on the LCD that is determined by the parameter.
        #  font Font enum value.
        @staticmethod
        def set_font(font):
            pass

        # Sets the pen width to the determined by the parameter set in the command.
        #  width The width of the pen when drawing. A larger width equals a wider pen stroke.
        @staticmethod
        def set_pen_width(width):
            pass

        #  Sets the origin of the LCD screen to the parameters defined in the function.
        #  x The x location of the origin.
        #  y The y location of the origin.
        @staticmethod
        def set_origin(x, y):
            pass

        # An integer type represents the a column on the LCD screen.
        #  Returns an integer that represents the a column on the LCD screen.
        @staticmethod
        def column():
            return 0

        # An integer type represents the a row on the LCD screen.
        #  Returns an integer that represents the a row on the LCD screen.
        @staticmethod
        def row():
            return 0

        # Sets the color of the pen to a specified color.
        # color 0xRRGGBB color, Color enum value or a string
        @staticmethod
        def set_pen_color(color):
            pass

        # Sets the color of the pen to a specified color.
        #  hue An integer that represents the hue of the color.
        @staticmethod
        def set_pen_color_hue(hue):
            pass

        # Sets the background fill color of the LCD screen to the specified color.
        # color A color unit where colors can be defined as names.
        @staticmethod
        def set_fill_color(color):
            pass

        @staticmethod
        def set_fill_color_hue(color):
            pass

        # Prints a string at an x, y location with the ability to be transparent.
        # x The x location of where the print should start
        # y The y location of where the print should start
        # bOpaque If set to false, the print will be transparent.
        # text object to print, usually a string.
        @staticmethod
        def print_at(x, y, opaque, text):
            pass

        # Clears the whole LCD to a default color or otherwise specified color.
        # color A color unit where colors can be defined as names.
        @staticmethod
        def clear_screen(color=None):
            pass

        # Clears the whole LCD to a default color or otherwise specified color.
        # hue An integer that represents the hue of the color.
        @staticmethod
        def clear_screen_hue(hue):
            pass

        # Clears the specified line and sets it to a specified color.
        # number An integer that sets the line that is to be cleared.
        # color A color unit where colors can be defined as names.
        @staticmethod
        def clear_line(number=None, color=None):
            pass

        @staticmethod
        def clear_line_hue(number, hue):
            pass

        # Clears the rest of the line from where the cursor is located and then moves the cursor to the beginning of the next line.
        @staticmethod
        def new_line():
            pass

        # Draws a single pixel to the LCD screen in the specified x and y location.
        # x The x location of where to draw the pixel.
        # y The y location of where to draw the pixel.
        @staticmethod
        def draw_pixel(x, y):
            pass

        # Draws a line connecting the two specified points in the parameters.
        # x1 The x location of the first point.
        # y1 The y location of the first point.
        # x2 The x location of the second point.
        # y2 The y location of the second point.
        @staticmethod
        def draw_line(x1, y1, x2, y2):
            pass

        # Draws a rectangle using the specified points and attributes set in the parameters. Fills the rectangle with a default color unless specified.
        # x The top left x location of the rectangle.
        # y The top left y location of the rectangle.
        # width The width of the rectangle.
        # height The height of the rectangle.
        # color
        @staticmethod
        def draw_rectangle(x, y, width, height, color=None):
            pass

        @staticmethod
        def draw_rectangle_hue(x, y, width, height, hue):
            pass

        # Draws a circle using the specified points and attributes set in the parameters. Fills the circle with a default color unless specified.
        # x The central x location of the circle.
        # y The central y location of the circle.
        # radius Sets the redius of the circle to be drawn on the LCD.
        @staticmethod
        def draw_circle(x, y, radius, color=None):
            pass

        @staticmethod
        def draw_circle_hue(x, y, radius, hue):
            pass

        # Not implementing -- no callback support
        # def pressed(, callback):
        # def released(, callback):

        # Gets the x location of the pen.
        # Returns an integer that represents the x location of the pen.
        @staticmethod
        def x_position():
            return 0

        # Gets the y location of the pen.
        #  Returns an integer that represents the y location of the pen.
        @staticmethod
        def y_position():
            return 0

        # Gets the pressed status of the LCD.
        # Returns a Boolean based on the state of a button. If the button is pressed, the Boolean will be true, if the button is released, the Boolean will be false.
        @staticmethod
        def pressing():
            return False

        # Switches to double buffering or renders back buffer to screen.
        @staticmethod
        def render(vsync_wait=True, run_schedule=True):
            return False

    class sdcard:
        @staticmethod
        def appendfile(filename, buffer):
            pass

        @staticmethod
        def filesize(filename):
            pass

        @staticmethod
        def is_inserted():
            pass

        @staticmethod
        def load_to_bytearray(filename, size):
            pass

        @staticmethod
        def load_to_string(filename, size):
            pass

        @staticmethod
        def loadfile(filename, buffer):
            pass

        @staticmethod
        def savefile(filename, buffer):
            pass

    class serial:

        @staticmethod
        def has_data():
            pass

        @staticmethod
        def read(buffer):
            pass

        @staticmethod
        def write(data, null_terminate_string):
            pass

    class three_wire_port:

        @staticmethod
        def a():
            pass

        @staticmethod
        def b():
            pass

        @staticmethod
        def c():
            pass

        @staticmethod
        def d():
            pass

        @staticmethod
        def e():
            pass

        @staticmethod
        def f():
            pass

        @staticmethod
        def g():
            pass

        @staticmethod
        def h():
            pass

        @staticmethod
        def installed():
            pass

        @staticmethod
        def port():
            pass

        @staticmethod
        def type():
            pass

        @staticmethod
        def value():
            pass

    class timer:

        @staticmethod
        def clear():
            pass

        @staticmethod
        def system():
            pass

        @staticmethod
        def time(timeUnits):
            pass

    @staticmethod
    def type():
        pass

    @staticmethod
    def value():
        pass
