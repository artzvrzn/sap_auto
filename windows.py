import pygetwindow as gw
import pyautogui as gui
from transaction_names import transaction_names, names_region, titles_list
from time import time

# print(locals().get('transaction_name').title)
print(gw.getAllTitles())
# print(gw.getWindowsWithTitle('zlpc')[0])

# zlpc = gw.getWindowsWithTitle('ZLPC')[0]
# zihp = gw.getWindowsWithTitle('In-house processing 2300')[0]
# sap_main = gw.getWindowsWithTitle('SAP Easy Access')[0]
# zlt10 = gw.getWindowsWithTitle('Stock transfer: Warehouse 270')[0]


class Transaction:

    def sap_access(self):
        try:
            sap_main = gw.getWindowsWithTitle('SAP Easy Access')[0]
            sap_main.activate()
        except IndexError:
            print('Seems there is no opened main SAP window')
            for transaction in titles_list:
                if transaction == 'ZLPC':
                    continue
                elif transaction in gw.getAllTitles():
                    temp_transaction = gw.getWindowsWithTitle(f'{transaction}')[0]
                    temp_transaction.activate()
                    while True:
                        gui.locateOnScreen(transaction_names['new_mode'], region=(410, 30, 575, 60))
                        gui.hotkey('ctrl', 'n')
                        gui.locateOnScreen(transaction_names['sap_easy_access'], region=names_region)
                        break

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
                gui.press('down', presses=2)
                gui.write('1')
                gui.press('tab')
                gui.write('5')
                gui.hotkey('shift', 'tab')
                gui.press('down', presses=4)
                gui.hotkey('ctrl', 'a')
                gui.press('space')
                gui.press('f8')
                break


# def open_transaction(transaction_name):
#     sap_main.activate()
#     if transaction_name == 'zihp':


# Transaction().zihp()
while True:
    gui.sleep(1)
    print(gw.getActiveWindow())






