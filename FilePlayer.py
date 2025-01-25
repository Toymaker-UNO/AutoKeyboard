import keyboard
import pyautogui
import time

class FilePlayer:
    def __init__(self):
        self.m_mappings = {}

    def register(self, a_key, a_file_name):
        self.m_mappings[a_key] = a_file_name
        keyboard.add_hotkey(a_key, lambda: self.type_content(a_key))

    def type_content(self, a_key):
        time.sleep(1)
        file_name = self.m_mappings[a_key]
        with open(file_name, 'r') as file:
            content = file.read()
        for char in content:
            if ' ' == char:
                time.sleep(0.1)
            if '\n' == char:
                time.sleep(0.3)
            pyautogui.typewrite(char, interval=0.0001)

    def play(self):
        print("Press 'esc' to exit.")
        keyboard.wait('esc')

file_player = FilePlayer()
file_player.register('F4', './02_ExampleCode.cpp')
file_player.register('F7', './03_Compile.txt')
file_player.play()