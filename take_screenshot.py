import pyautogui
import subprocess


def take_screenshot_and_open_paint():
    # Take a screenshot
    pyautogui.hotkey('win', 'shiftleft', 's')

    # Launch paint
    subprocess.Popen('mspaint')


if __name__ == "__main__":
    take_screenshot_and_open_paint()
