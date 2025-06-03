import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.scanners.ioexpander import PCF857X, PCF857XScanner
from kmk.extensions.media_keys import MediaKeys
from kmk.modules.layers import Layers
from kmk.modules.modtap import ModTap
from kmk.modules.holdtap import HoldTap
from kmk.keys import KC

keyboard = KMKKeyboard()

keyboard.extensions.append(MediaKeys())
keyboard.modules.append(Layers())
keyboard.modules.append(ModTap())
keyboard.modules.append(HoldTap())

direct_gpio_pins = [
    board.GP26, board.GP27, board.GP28, board.GP29, board.GP0,
    board.GP1, board.GP2, board.GP3, board.GP4,
]

direct_scanner = KeysScanner(
    pins=direct_gpio_pins,
    value_when_pressed=False,
    pull=True
)

ioexpander = PCF857X(i2c=board.I2C(), address=0x20)
pcf_scanner = PCF857XScanner(
    ioexpander=ioexpander,
    pins=[0, 1, 2, 3, 4, 5, 7],
    value_when_pressed=False,
)

keyboard.matrix = [direct_scanner, pcf_scanner]

keyboard.keymap = [
    [
        KC.N1,     KC.N2,    KC.N3,    KC.N4,    KC.N5,    KC.N6,    KC.N7,    KC.N8,    KC.N9,    KC.N0,
        KC.Q,      KC.W,     KC.E,     KC.R,     KC.T,     KC.Y,     KC.U,     KC.I,     KC.O,     KC.P,
        KC.A,      KC.S,     KC.D,     KC.F,     KC.G,     KC.H,     KC.J,     KC.K,     KC.L,     KC.SCLN,
        KC.Z,      KC.X,     KC.C,     KC.V,     KC.B,     KC.N,     KC.M,     KC.COMM,  KC.DOT,   KC.SLSH,
        KC.LCTL,   KC.LCMD,  KC.LALT,  KC.SPC,   KC.SPC,   KC.SPC,   KC.RALT,  KC.RCMD,  KC.LSFT,  KC.RSFT,
        KC.ESC,    KC.TAB,   KC.CAPS,  KC.MO(1), KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.MENU,  KC.RCTL,
    ],
    [
        KC.F1,     KC.F2,    KC.F3,    KC.F4,    KC.F5,    KC.F6,    KC.F7,    KC.F8,    KC.F9,    KC.F10,
        KC.TRNS,   KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.UP,    KC.TRNS,  KC.F11,
        KC.TRNS,   KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.LEFT,  KC.DOWN,  KC.RGHT,  KC.F12,
        KC.TRNS,   KC.TRNS,  KC.TRNS,  KC.VOLD,  KC.VOLU,  KC.MUTE,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,
        KC.TRNS,   KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,
        KC.GRV,    KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,
    ],
]

if __name__ == '__main__':
    keyboard.go()
