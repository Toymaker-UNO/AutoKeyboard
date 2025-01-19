import keyboard
import pyautogui

class FilePlayer:
    def __init__(self):
        self.m_mappings = {}

    def register(self, a_key, a_file_name):
        with open(a_file_name, 'r') as file:
            content = file.read()
        self.m_mappings[a_key] = (content)
        keyboard.add_hotkey(a_key, lambda: self.type_content(a_key))

    def type_content(self, a_key):
        content = self.m_mappings[a_key]
        for char in content:
            pyautogui.typewrite(char, interval=0.0001)

        #words = content.split()
        #for word in words:
        #    pyautogui.typewrite(word + ' ', interval=0.01)

    def play(self):
        print("Press 'esc' to exit.")
        keyboard.wait('esc')

file_player = FilePlayer()
file_player.register('F4', './01_URL.txt')
file_player.register('F6', './02_ExampleCode.cpp')
file_player.play()