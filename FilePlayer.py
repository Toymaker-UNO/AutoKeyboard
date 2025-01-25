import keyboard
import pyautogui
import time

class FilePlayer:
    def __init__(self):
        self.m_mappings = {}
        self.comment_flag = 0

    def register(self, a_key, a_file_name):
        self.m_mappings[a_key] = a_file_name
        keyboard.add_hotkey(a_key, lambda: self.type_content(a_key))

    def type_content(self, a_key):
        time.sleep(1)
        file_name = self.m_mappings[a_key]
        with open(file_name, 'r') as file:
            content = file.read()

        index = 0
        buffer=''
        length = len(content)
        for char in content:
            self.mode_set(char)
            buffer += char
            index += 1
            if index == length:
                pyautogui.typewrite(buffer, interval=self.get_interval())
                buffer = ''
                break
            if True == char.isspace():
                pyautogui.typewrite(buffer, interval=self.get_interval())
                buffer = ''
    
    def play(self):
        print("Press 'esc' to exit.")
        keyboard.wait('esc')

    def mode_set(self, char):
        if '\n' == char:
            self.comment_flag = 0
            return
        if 0 == self.comment_flag :
            if '/' == char:
                self.comment_flag = 1
                return
        elif 1 == self.comment_flag:
            if '/' == char:
                self.comment_flag = 2
                return
            else:
                self.comment_flag = 0
                return
            
    def get_interval(self):   #0.01 ~ 0.07
        if 2 == self.comment_flag:
            return 0.01
        return 0.03

file_player = FilePlayer()
file_player.register('F4', './02_ExampleCode.cpp')
file_player.register('F7', './03_Compile.txt')
file_player.play()