import pygetwindow as gw
import pyautogui as gui
from transaction_names import transaction_names, names_region, titles_tuple
from time import time

# print(locals().get('transaction_name').title)
print(gui.getAllTitles())


# print(gw.getWindowsWithTitle('zlpc')[0])

# zlpc = gw.getWindowsWithTitle('ZLPC')[0]
# zihp = gw.getWindowsWithTitle('In-house processing 2300')[0]
# sap_main = gw.getWindowsWithTitle('SAP Easy Access')[0]
# zlt10 = gw.getWindowsWithTitle('Stock transfer: Warehouse 270')[0]

def hotkey(image, reg, button1, button2):
    while True:
        image_location = gui.locateOnScreen(image, region=reg)
        if image_location is not None:
            gui.hotkey(button1, button2)
            gui.sleep(0.1)
            break

class Transaction:

    def _new_mode(self):

        for transaction in gui.getAllTitles():
            if transaction.startswith('ZLPC'):
                continue
            elif transaction.startswith(titles_tuple):
                temp_transaction = gui.getWindowsWithTitle(str(transaction))[0]
                temp_transaction.activate()
                print(temp_transaction)
                hotkey(transaction_names['new_mode'], (410, 30, 575, 60), 'ctrl', 'n')
                while gui.getActiveWindowTitle == temp_transaction:
                    print(gui.getActiveWindowTitle)
                    gui.sleep(0.25)
                print('test')
                if 'Information' in gui.getAllTitles():
                    dialog = gui.confirm(text='Много окошек. Закрываю одно',
                                         title='Limit of tabs',
                                         buttons=['OK', 'Cancel'])
                    if dialog == 'OK':
                        information = gw.getWindowsWithTitle('Information')[0]  # ЗАКРЫВАЕТ ВСЕ ОКНА
                        print(information)
                        gui.press('esc')
                        print(temp_transaction)
                        temp_transaction.close()
                        continue
                    else:
                        exit()
                elif gui.locateOnScreen(transaction_names['sap_easy_access'], region=names_region):
                    break

    def sap_access(self):
        try:
            trigger = False
            for transaction in gui.getAllTitles():
                if 'SAP Easy Access' in transaction:
                    sap_main = gui.getWindowsWithTitle(str(transaction))[0]
                    sap_main.activate()
                    trigger = True
                    break
            if not trigger:
                raise IndexError
        except IndexError:
            print('Seems there is no opened main SAP window')
            self._new_mode()

    def zihp(self):
        self.sap_access()
        while True:
            if gui.locateOnScreen(transaction_names['sap_easy_access'], region=names_region):
                gui.click(x=100, y=50, duration=0)
                gui.hotkey('ctrl', 'left')
                gui.hotkey('ctrl', 'delete')
                gui.write('ZIHP')
                gui.press('enter')
                break
        while True:
            if gui.locateOnScreen(transaction_names['zihp_data'], region=(0, 120, 320, 200)):
                gui.hotkey('ctrl', 'a')
                gui.press('del')
                gui.write('2300')
                gui.press('down')
                gui.write('2310')
                gui.press('down')
                gui.write('1')
                gui.press('tab')
                gui.write('5')
                gui.hotkey('shift', 'tab')
                gui.press('down', presses=5)
                gui.hotkey('ctrl', 'a')
                gui.press('space')
                gui.press('f8')
                break


# def open_transaction(transaction_name):
#     sap_main.activate()
#     if transaction_name == 'zihp':

if __name__ == '__main__':
    Transaction().zihp()
    # sap = gui.getWindowsWithTitle('SAP Easy Access')[0]
    # print(sap.title)
# while True:
#     gui.sleep(1)
#     print(gui.getActiveWindow())
