#!/usr/bin/env python
# -*- coding: utf-8 -*-

import ctypes


def key_click(code):
    key_down(code)
    key_up(code)


def key_down(code):
    ctypes.windll.user32.keybd_event(code, 0, 0, 0)
    return


def key_up(code):
    ctypes.windll.user32.keybd_event(code, 0, 0x2, 0)
    return

VK_BACK = 0x08  # BackSpace (8)
VK_TAB = 0x09  # Tab (9)
VK_CLEAR = 0x0C  # Clear (12)
VK_RETURN = 0x0D  # Enter (13)
VK_SHIFT = 0x10  # Shift (16)
VK_CONTROL = 0x11  # Ctrl (17)
VK_MENU = 0x12  # Alt (18)
VK_PAUSE = 0x13  # Pause (19)
VK_CAPITAL = 0x14  # Shift+CapsLock (20)
VK_ESCAPE = 0x1B  # Esc (27)
VK_NONCONVERT = 0x1D  # 無変換 (29)
VK_SPACE = 0x20  # Space (32)
VK_PRIOR = 0x21  # PageUp (33)
VK_NEXT = 0x22  # PageDown (34)
VK_END = 0x23  # End (35)
VK_HOME = 0x24  # Home (36)
VK_LEFT = 0x25  # ← (37)
VK_UP = 0x26  # ↑ (38)
VK_RIGHT = 0x27  # → (39)
VK_DOWN = 0x28  # ↓ (40)
VK_SNAPSHOT = 0x2C  # PrintScreen (44)
VK_INSERT = 0x2D  # Insert (45)
VK_DELETE = 0x2E  # Delete (46)
VK_0 = 0x30  # 0 (48)
VK_1 = 0x31  # 1 (49)
VK_2 = 0x32  # 2 (50)
VK_3 = 0x33  # 3 (51)
VK_4 = 0x34  # 4 (52)
VK_5 = 0x35  # 5 (53)
VK_6 = 0x36  # 6 (54)
VK_7 = 0x37  # 7 (55)
VK_8 = 0x38  # 8 (56)
VK_9 = 0x39  # 9 (57)
VK_A = 0x41  # A (65)
VK_B = 0x42  # B (66)
VK_C = 0x43  # C (67)
VK_D = 0x44  # D (68)
VK_E = 0x45  # E (69)
VK_F = 0x46  # F (70)
VK_G = 0x47  # G (71)
VK_H = 0x48  # H (72)
VK_I = 0x49  # I (73)
VK_J = 0x4A  # J (74)
VK_K = 0x4B  # K (75)
VK_L = 0x4C  # L (76)
VK_M = 0x4D  # M (77)
VK_N = 0x4E  # N (78)
VK_O = 0x4F  # O (79)
VK_P = 0x50  # P (80)
VK_Q = 0x51  # Q (81)
VK_R = 0x52  # R (82)
VK_S = 0x53  # S (83)
VK_T = 0x54  # T (84)
VK_U = 0x55  # U (85)
VK_V = 0x56  # V (86)
VK_W = 0x57  # W (87)
VK_X = 0x58  # X (88)
VK_Y = 0x59  # Y (89)
VK_Z = 0x5A  # Z (90)
VK_LWIN = 0x5B  # 左Windows (91)
VK_RWIN = 0x5C  # 右Windows (92)
VK_APPS = 0x5D  # ApplicationMenu (93)
VK_NUMPAD0 = 0x60  # 0 (96)
VK_NUMPAD1 = 0x61  # 1 (97)
VK_NUMPAD2 = 0x62  # 2 (98)
VK_NUMPAD3 = 0x63  # 3 (99)
VK_NUMPAD4 = 0x64  # 4 (100)
VK_NUMPAD5 = 0x65  # 5 (101)
VK_NUMPAD6 = 0x66  # 6 (102)
VK_NUMPAD7 = 0x67  # 7 (103)
VK_NUMPAD8 = 0x68  # 8 (104)
VK_NUMPAD9 = 0x69  # 9 (105)
VK_MULTIPLY = 0x6A  # * (106)
VK_ADD = 0x6B  # + (107)
VK_SUBTRACT = 0x6D  # - (109)
VK_DECIMAL = 0x6E  # . (110)
VK_DIVIDE = 0x6F  # / (111)
VK_F1 = 0x70  # F1 (112)
VK_F2 = 0x71  # F2 (113)
VK_F3 = 0x72  # F3 (114)
VK_F4 = 0x73  # F4 (115)
VK_F5 = 0x74  # F5 (116)
VK_F6 = 0x75  # F6 (117)
VK_F7 = 0x76  # F7 (118)
VK_F8 = 0x77  # F8 (119)
VK_F9 = 0x78  # F9 (120)
VK_F10 = 0x79  # F10 (121)
VK_F11 = 0x7A  # F11 (122)
VK_F12 = 0x7B  # F12 (123)
VK_NUMLOCK = 0x90  # NumLock (144)
VK_SCROLL = 0x91  # ScrollLock (145)
VK_COLONGE = 0xBA  # : (186)
VK_SEMICOLONGE = 0xBB  # ; (187)
VK_COMMA = 0xBC  # , (188)
VK_HYPHEN = 0xBD  # - (189)
VK_DOT = 0xBE  # . (190)
VK_SLASH = 0xBF  # / (191)
VK_ATMARK = 0xC0  # @ (192)
VK_LEFT_SQUARE_BRACKET = 0xDB  # [ (219)
VK_BACKSLASH = 0xDC  # \ (220)
VK_RIGHT_SQUARE_BRACKET = 0xDD  # ] (221)
VK_HAT = 0xDE  # ^ (222)
VK_BACKSLASH2 = 0xE2  # \ (226)
VK_HANKAKU_ZENKAKU = 0xE5  # 半角/全角 (229)
VK_MAEKOUHO = 0xE5  # 前候補 (229)
VK_CAPSLOCK = 0xF0  # CapsLock (240)
VK_KANA = 0xF2  # カタカナひらがな (242)

VK_ALT = VK_MENU
VK_PRINTSCREEN = VK_SNAPSHOT