print("Starting")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.matrix import DiodeOrientation
from kmk.handlers.sequences import send_string, simple_key_sequence
from kmk.modules.layers import Layers
from kmk.modules.encoder import EncoderHandler
from kmk.modules.tapdance import TapDance
from kmk.extensions.RGB import RGB
from midi import Midi


# KEYTBOARD SETUP
layers = Layers()
keyboard = KMKKeyboard()
encoders = EncoderHandler()
tapdance = TapDance()
tapdance.tap_time = 250
keyboard.modules = [layers, encoders, tapdance]

# SWITCH MATRIX
keyboard.col_pins = (board.GP3, board.GP4, board.GP5, board.GP6) #列引脚
keyboard.row_pins = (board.GP7, board.GP8, board.GP9)           #行引脚
keyboard.diode_orientation = DiodeOrientation.COL2ROW        #行引脚会被拉低，而与该按键相连的列引脚会被拉高。

# ENCODERS
encoders.pins = ((board.A2, board.A1, board.A0, False), (board.GP21, board.GP20, board.GP19, False),)

# EXTENSIONS
rgb_ext = RGB(pixel_pin = board.GP18, num_pixels=4, hue_default=100)
midi_ext = Midi()
keyboard.extensions.append(rgb_ext)
keyboard.extensions.append(midi_ext)
keyboard.debug_enabled = False

# MACROS ROW 1
# GIT = simple_key_sequence([KC.LWIN(KC.X),KC.MACRO_SLEEP_MS(200),(KC.I), KC.MACRO_SLEEP_MS(1000),send_string('start https://github.com'), KC.ENTER])
SAVE = simple_key_sequence([KC.LCTRL(KC.S)])
project_left = simple_key_sequence([KC.LALT(KC.LEFT)])
project_right = simple_key_sequence([KC.LALT(KC.RIGHT)])
CODE_down = simple_key_sequence([KC.LCTRL(KC.LSHIFT(KC.DOWN))])

# MACROS ROW 2
cancel =simple_key_sequence([KC.LCTRL(KC.Z)])
BROWSER = simple_key_sequence([KC.LCMD(KC.LALT(KC.LSFT(KC.T))), KC.MACRO_SLEEP_MS(1000), KC.LCTRL(KC.U), send_string('start https://ocrism.studio'), KC.ENTER])
CODE_left = simple_key_sequence([KC.LCTRL(KC.LBRACKET)])
CODE_right = simple_key_sequence([KC.LCTRL(KC.RBRACKET)])
CODE_UP = simple_key_sequence([KC.LCTRL(KC.LSHIFT(KC.UP))])

# MACROS ROW 3
TERMINAL = simple_key_sequence([KC.LCMD(KC.LALT(KC.LSFT(KC.T))), KC.LCTRL(KC.U)])
cancel =simple_key_sequence([KC.LCTRL(KC.Z)])
head_wenjian=simple_key_sequence([send_string('#include <iostream>'), KC.ENTER,send_string('#include <vector>'),KC.ENTER,send_string('using namespace std;'), KC.ENTER])
FORCE_QUIT = simple_key_sequence([KC.LCMD(KC.LALT(KC.ESCAPE))])
MUTE = KC.MUTE(send_string('start https://ocrism.studio'), KC.ENTER)
LOCK = simple_key_sequence([KC.LCTRL(KC.LCMD(KC.Q)), KC.MACRO_SLEEP_MS(400), KC.ESCAPE])


_______ = KC.TRNS
xxxxxxx = KC.NO

# LAYER SWITCHING TAP DANCE
TD_LYRS = KC.TD(LOCK, KC.MO(1), xxxxxxx, KC.TO(2))
MIDI_OUT = KC.TD(KC.MIDI(70), xxxxxxx, xxxxxxx, KC.TO(0))

# array of default MIDI notes
# midi_notes = [60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75]

# KEYMAPS

keyboard.keymap = [
    # MACROS
    [
        TERMINAL,   FORCE_QUIT,     KC.MUTE,    TD_LYRS,
        head_wenjian,    CODE_left,          CODE_right,    CODE_UP,
        SAVE,    project_left,       project_right,     CODE_down,
    ],
    # RGB CTL
    [
        xxxxxxx,    xxxxxxx,            xxxxxxx,                xxxxxxx,
        xxxxxxx,    KC.RGB_MODE_SWIRL,  KC.RGB_MODE_KNIGHT,     KC.RGB_MODE_BREATHE_RAINBOW,
        xxxxxxx,    KC.RGB_MODE_PLAIN,  KC.RGB_MODE_BREATHE,    KC.RGB_MODE_RAINBOW,
    ],
    # MIDI
    [
        KC.MIDI(30),    KC.MIDI(69),      KC.MIDI(70),       MIDI_OUT,
        KC.MIDI(67),    KC.MIDI(66),      KC.MIDI(65),       KC.MIDI(64),
        KC.MIDI(60),    KC.MIDI(61),      KC.MIDI(62),       KC.MIDI(63),
    ]
]

encoders.map = [    ((KC.VOLD, KC.VOLU, KC.MUTE),           (KC.RGB_VAD,    KC.RGB_VAI,     KC.RGB_TOG)),   # MACROS
                    ((KC.RGB_AND, KC.RGB_ANI, xxxxxxx),     (KC.RGB_HUD,    KC.RGB_HUI,     _______   )),   # RGB CTL
                    ((KC.VOLD, KC.VOLU, KC.MUTE),           (KC.RGB_VAD,    KC.RGB_VAI,     KC.RGB_TOG)),   # MIDI
                ]


if __name__ == '__main__':
    keyboard.go()
