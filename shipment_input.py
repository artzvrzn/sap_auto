import pyautogui as gui
import pygetwindow as gw
import keyboard
from sys import exit
import logging
from windows import Transaction

logger = logging.getLogger('log')
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)


logger.debug('start')
# gui.moveTo(x=58, y=21, duration=0) shipment
# gui.moveTo(x=58, y=21, duration=0) change
# print(gui.position())
# <Win32Window left="-8", top="-8", width="1936", height="1056", title="CCH TO x-doc 5010775587 Display: Overview">
# <Win32Window left="-8", top="-8", width="1936", height="1056", title="In-house processing 2300">


def press_the_button(image, reg=None, button=None, x=None, y=None, duration=0):
    if x is None and y is None and button is None:
        while True:
            image_location = gui.locateOnScreen(image, region=reg)
            print('first')
            if image_location is not None:
                gui.click(image_location)
                gui.sleep(0.1)
                break
    elif button is None:
        while True:
            image_location = gui.locateOnScreen(image, region=reg)
            print('second')
            if image_location is not None:
                gui.moveTo(x=x, y=y, duration=duration)
                gui.click()
                gui.sleep(0.1)
                break
    elif button is not None:
        while True:
            image_location = gui.locateOnScreen(image, region=reg)
            print('third')
            if image_location is not None:
                gui.press(button)
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
        self.processing_marked = 'screenshots\\Processing_marked.png'
        self.green = 'screenshots\\Green.png'
        self.zaby_zslr = 'screenshots\\ZABY_ZSLR.png'
        self.zslr = 'screenshots\\ZSLR.png'
        self.mark = 'screenshots\\mark.png'
        self.ship_button_pressed = False
        self.change_button_pressed = False
        self.message_button_pressed = False
        self.output_opened = False
        self.zslr_input = False
        self.print_docs_pressed = False
        self.processing_1 = False
        self.processing_2 = False
        self.print_docs_status = False


    def open_output(self):
        logger.debug('open_output')
        while True:
            if not self.ship_button_pressed:
                gui.sleep(0.5)
                logger.debug('%s', gw.getActiveWindow().title)
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
        self.open_output()
        while True:
            if gw.getActiveWindow().title.endswith('x-doc: Output') and self.output_opened and not self.zslr_input:
                gui.click(x=70, y=275, duration=0) # testing parameters in zslr is here (change to 275)
                gui.sleep(0.4)
                gui.write('zslr')
                gui.press('tab')
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
                logger.debug('zslr_inputting final')
                gui.sleep(1)
                self.ship_button_pressed = False
                self.change_button_pressed = False
                self.message_button_pressed = False
                self.output_opened = False
                break

    def print_docs(self):
        # self.zslr_inputting()
        while True:
            if self.zslr_input and not self.print_docs_pressed:
                gui.sleep(0.25)
                logger.debug('%s', gw.getActiveWindow().title)
                if gw.getActiveWindow().title.startswith('In-house processing'):
                    gui.hotkey('shift', 'f9')
                    self.print_docs_pressed = True
            elif self.print_docs_pressed:
                # gui.sleep(0.1)
                gui.sleep(0.25)
                press_the_button(self.processing, reg=(20, 360, 180, 400), x=37, y=387)
                gui.press('f8')
                gui.sleep(0.1)
                press_the_button(self.zaby_zslr, reg=(5, 152, 30, 220), x=16, y=208)
                gui.hotkey('shift', 'f2')
                gui.sleep(0.1)
                press_the_button(self.green, reg=(300, 190, 400, 225), button='f3')
                press_the_button(self.processing_marked, reg=(20, 360, 180, 400), x=246, y=300)
                gui.press('del')
                gui.sleep(0.1)
                gui.press('2')
                gui.sleep(0.1)
                gui.press('f8')
                gui.sleep(0.1)
                press_the_button(self.zslr, reg=(5, 152, 30, 220), button='space')
                gui.hotkey('shift', 'f2')
                gui.sleep(0.25)
                press_the_button(self.mark, reg=(0, 1000, 50, 1060), button='esc')
                self.zslr_input = False
                self.print_docs_pressed = False
                self.print_docs_status = True
                break

    def zlpc_inputting(self):
        while True:
            if self.print_docs_status:
                if gw.getActiveWindow().title.startswith('Messages'):
                    gui.press('f3')
                elif gw.getActiveWindow().title.startswith('In-house processing'):
                    zlpc_window = gw.getWindowsWithTitle('ZLPC')[0]
                    zlpc_window.activate()
                elif gw.getActiveWindow().title.startswith('ZLPC'):
                    gui.press('f2')
                    self.print_docs_status = False
                    break
                elif keyboard.is_pressed('ctrl+='):
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




if __name__ == '__main__':

    sh = Shipment()
    tr = Transaction()

    while True:
        if keyboard.is_pressed('ctrl+8'):
            logger.debug('zslr_inputting')
            sh.zslr_inputting()
            logger.debug('stop')
        elif keyboard.is_pressed('ctrl+9'):
            logger.debug('print_docs')
            sh.print_docs()
            logger.debug('stop')
        elif keyboard.is_pressed('ctrl+0'):
            logger.debug('zslr + print_docs')
            sh.zslr_inputting()
            sh.print_docs()
            # sh.zlpc_inputting()
            logger.debug('stop')
        elif keyboard.is_pressed('ctrl+-'):
            logger.debug('exit')
            exit()
        elif keyboard.is_pressed('ctrl+7'):
            tr.zihp()
    # sh.print_docs()


    # sh.print_docs()-
    # while True:
    #     gui.sleep(0.5)
    #     print(gw.getActiveWindow())

    # new_win = gw.getWindowsWithTitle('CCH TO x-doc 5010775587 Display: Overview')
    # print()