import pyautogui as gui
import pygetwindow as gw
import keyboard
from sys import exit
import argparse

print('start')
# gui.moveTo(x=58, y=21, duration=0) shipment
# gui.moveTo(x=58, y=21, duration=0) change
# print(gui.position())
# <Win32Window left="-8", top="-8", width="1936", height="1056", title="CCH TO x-doc 5010775587 Display: Overview">
# <Win32Window left="-8", top="-8", width="1936", height="1056", title="In-house processing 2300">


def press_the_button(button, reg=None, x=None, y=None, duration=0):
    if not x or not y:
        while True:
            button_location = gui.locateOnScreen(button, region=reg)
            print(reg)
            if button_location is not None:
                gui.click(button_location)
                gui.sleep(0.1)
                break
    else:
        while True:
            button_location = gui.locateOnScreen(button, region=reg)
            print(reg)
            if button_location is not None:
                gui.moveTo(x=x, y=y, duration=duration)
                gui.click()
                gui.sleep(0.1)
                break


class Shipment:

    def __init__(self):
        self.shipment = 'screenshots\\Shipment.png'
        self.change = 'screenshots\\Change.png'
        self.message = 'screenshots\\Message.png'
        self.output = 'screenshots\\Output.png'
        self.output_type = 'screenshots\\Output_type.png'
        self.processing = 'screenshots\\Processing.png'
        self.green = 'screenshots\\Green.png'
        self.zaby_zslr = 'screenshots\\ZABY_ZSLR.png'
        self.ship_button_pressed = False
        self.change_button_pressed = False
        self.message_button_pressed = False
        self.output_opened = False
        self.zslr_input = False
        self.print_docs_pressed = False


    def open_output(self):
        while True:
            if not self.ship_button_pressed:
                gui.sleep(0.5)
                print(gw.getActiveWindow().title)
                if gw.getActiveWindow().title.endswith('Display: Overview'):
                    shipment = gui.moveTo(x=58, y=21, duration=0)
                    gui.click(shipment)
                    self.ship_button_pressed = True
            elif self.ship_button_pressed and not self.change_button_pressed:
                change = gui.moveTo(x=55, y=65, duration=0)
                gui.click(change)
                self.change_button_pressed = True
            elif self.change_button_pressed:
                press_the_button(self.message)
                self.message_button_pressed = True
                self.output_opened = True
                break

    def zslr_inputting(self):
        if keyboard.is_pressed('ctrl+0'):
            print('key was pressed')
            self.open_output()
            while True:
                if gw.getActiveWindow().title.endswith('x-doc: Output') and self.output_opened and not self.zslr_input:
                    zslr = gui.moveTo(x=70, y=234, duration=0)
                    gui.click(zslr)
                    gui.sleep(0.25)
                    gui.write('zslr')
                    gui.write('Print output')
                    gui.press('tab', presses=3)
                    gui.write('RU')
                    gui.press('enter', presses=2, interval=0.25)
                    gui.hotkey('ctrl', 's')
                    gui.sleep(0.25)
                    gui.write('BYMSQWHL02')
                    gui.press('tab', presses=2)
                    gui.press('space')
                    gui.press('f3')
                    gui.sleep(0.25)
                    gui.hotkey('ctrl', 's')
                    self.zslr_input = True
                    print('end')
                    gui.sleep(1)
                    self.ship_button_pressed = False
                    self.change_button_pressed = False
                    self.message_button_pressed = False
                    self.output_opened = False
                    break

    def print_docs(self):
        if keyboard.is_pressed('ctrl+0'):
            print('key was pressed')
            self.zslr_inputting()
            while True:
                if self.zslr_input and not self.print_docs_pressed:
                    gui.sleep(0.25)
                    print(gw.getActiveWindow().title)
                    if gw.getActiveWindow().title.startswith('In-house processing'):
                        gui.hotkey('shift', 'f9')
                        self.print_docs_pressed = True
                elif self.print_docs_pressed:
                    # gui.sleep(0.1)
                    gui.sleep(0.1)
                    press_the_button(self.processing, reg=(20, 360, 180, 400), x=37, y=387)
                    gui.press('f8')
                    gui.sleep(0.1)
                    press_the_button(self.zaby_zslr, reg=(5, 152, 30, 220), x=16, y=208)
                    gui.hotkey('shift', 'f2')
                    gui.sleep(0.1)
                    while True:
                        if gui.locateOnScreen(self.green, region=(300, 190, 400, 225)) is not None:
                            gui.sleep(0.25)
                            gui.press('f3')
                            # gui.moveTo(x=17, y=208, duration=0)
                            # gui.click()
                            break
                    gui.sleep(0.25)
                    gui.moveTo(x=247, y=300, duration=0)
                    gui.click()
                    gui.sleep(0.1)
                    gui.press('del')
                    gui.sleep(0.1)
                    gui.press('2')
                    gui.press('f8')
                    gui.sleep(0.1)
                    self.zslr_input = False
                    self.print_docs_pressed = False
                    break


            #     gui.press('tab', interval=0.25)
            #     gui.press('space')
            #     gui.hotkey('shift', 'f2')
            #     gui.press('f3')
            #     gui.press('tab', presses=7)
            #     gui.press('2')
            #     gui.press('f8')
            #     gui.press('space')
            #     gui.hotkey('shift', 'f2')
            #     gui.press('f3', presses=2, interval=0.25)
            #     break
            # else:
            #     gui.sleep(0.25)






sh = Shipment()
while True:
    sh.print_docs()

    if keyboard.is_pressed('ctrl+9'):
        print('stop')
        exit()
# sh.print_docs()


# sh.print_docs()-
# while True:
#     gui.sleep(0.5)
#     print(gw.getActiveWindow())

# new_win = gw.getWindowsWithTitle('CCH TO x-doc 5010775587 Display: Overview')
# print()