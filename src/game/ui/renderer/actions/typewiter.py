# Required imports
import time
import sys
from src.game.ui.config.COLOR_MAP import COLOR_MAP
from src.game.ui.renderer.effect.corrupt import Corrupt
from src.game.ui.tools.color_tool import ColorTool
from src.core.util.helpers.usleep import usleep

CT = ColorTool()

# Updated scene data for compatibility with the improved Textwrite class
scene_1 = [
    # [message, sender, end_time_buffer, color, showsender, textspeed, is_scene_text]
    ['  SYSTEM STARTUP...', 'SYSTEM', 0.5, 'red', True, 100],
    ['  RUNNING SYSTEM DIAGNOSTICS...', 'SYSTEM', 2.0, 'red', False, 60],
    ['  READING NEURAL CONNECTION...', 'SYSTEM', 0.5, 'red', False, 60],
    ['  NEURAL_ID VALID...', '????', 0.5, 'red', True, 15],
    ['  USER INFO:\n -- USER: AF35-B391-CC47-CD42\n -- NEURAL_CONNECTION: VALID\n -- BIOMETRICS: STABLE (67%)', 'SYSTEM', 0.5, CT.text_rgb_to_ansi(COLOR_MAP['red']), True, 40],
    ['  WARNING: VITAL ERROR: BIOMETRIC_READING: DECREASING', 'SYSTEM', 0.1, 'red', False, 60],
    ['  VALIDATING BIOMETRICS...', 'SYSTEM', 1.0, 'red', False, 60],
    ['  REROUTING BACKUP...', 'SYSTEM', 2.0, 'white', False, 60],
    ['  REROUTING >> \'SAFEHOUSE.C680\'...', 'SYSTEM', 1.0, 'red', False, 60],
    ['  ESTABLISHING CONNECTION...\nCONNECTION ESTABLISHED\n&', 'SYSTEM', 2.0, 'red', False, 60],
]


# Improved Textwrite class
class Typewrite:
    def __init__(self):
        self.default_type_speed = 100
        self.type_speed = self.default_type_speed

    def write(self,
              message,
              sender='',
              end_time_buffer=0,
              color='white',
              showsender=True,
              textspeed=None,
              newline=True,
              is_scene_text=False,
              corruption_percentage=None
              ):
        """
        Writes a message with a typing animation.

        :param message: The message to be printed.
        :param sender: The sender's name to be displayed.
        :param end_time_buffer: Delay after completing the message.
        :param color: The color of the sender's name.
        :param showsender: Whether to show the sender's name.
        :param textspeed: Custom typing speed.
        :param newline: Whether to end with a newline.
        """

        if textspeed is not None:
            self.type_speed = textspeed

        if showsender and sender:
            print(f'\n[{CT.text_rgb_to_ansi(COLOR_MAP[color])}{sender}{CT.clense()}]')

        if corruption_percentage is not None:
            message = Corrupt().apply(message, corruption_percentage)

        for char in message:
            sys.stdout.write(char)
            sys.stdout.flush()

            # Adjust timing based on character
            if char in {',', '.', ';', ':', '!', '?'}:
                if is_scene_text:
                    time.sleep(0.4)
            elif char == '\n':
                if is_scene_text:
                    time.sleep(0.6)
            else:
                if is_scene_text:
                    time.sleep(1 / self.type_speed)
                else:
                    usleep(250)

        # Add buffer delay at the end
        time.sleep(end_time_buffer)

        # Reset to default typing speed
        self.type_speed = self.default_type_speed

        # Print newline if required
        if newline:
            print()

    def scene(self, scene_list):
        """
        Plays a list of scenes by calling the write method for each scene.

        :param scene_list: List of scene parameters to be passed to the write method.
        """
        for scene_params in scene_list:
            # Ensure scene_params has the necessary length and default values
            if len(scene_params) < 6:
                scene_params = scene_params + [0] * (6 - len(scene_params))

            # Unpack scene parameters for the write method
            self.write(*scene_params)


