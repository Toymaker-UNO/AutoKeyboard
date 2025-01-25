import keyboard
import pyautogui
import time

class FilePlayer:
    def __init__(self):
        self.m_mappings = {}
        self.comment_flag = 0
        self.buffer = ''
        self.buffer_length = 0
        self.buffer_index = 0

    def register(self, a_key, a_file_name):
        self.m_mappings[a_key] = a_file_name
        keyboard.add_hotkey(a_key, lambda: self.type_content(a_key))

    def type_content(self, a_key):
        time.sleep(1)
        file_name = self.m_mappings[a_key]
        with open(file_name, 'r') as file:
            content = file.read()
        self.initialize(len(content))
        for char in content:
            if self.buffering(char):
                self.type_buffer()
    
    def initialize(self, a_buffer_length):
        self.comment_flag = 0
        self.buffer = ''
        self.buffer_length = a_buffer_length
        self.buffer_index = 0

    def buffering(self, a_char):
        self.buffer += a_char
        self.buffer_index += 1
        if self.buffer_index == self.buffer_length:
            return True
        if '\n' == a_char:
            return True
        if 0 == self.comment_flag :
            if '/' == a_char:
                self.comment_flag = 1
        elif 1 == self.comment_flag:
            if '/' == a_char:
                self.comment_flag = 2
            else:
                self.comment_flag = 0
        return False
    
    def type_buffer(self):
        pyautogui.typewrite(self.buffer, interval=self.get_interval())
        self.buffer = ''
        self.comment_flag = 0

    def play(self):
        print("Press 'esc' to exit.")
        keyboard.wait('esc')
            
    def get_interval(self):   #0.01 ~ 0.07
        if 2 == self.comment_flag:
            return 0.02
        return 0.06

file_player = FilePlayer()
file_player.register('F4', './02_ExampleCode.cpp')
file_player.register('F7', './03_Compile.txt')
file_player.play()