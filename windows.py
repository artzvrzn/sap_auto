import pygetwindow as gw
import pyautogui as gui
from transaction_names import transaction_names, names_region
from time import time

# print(locals().get('transaction_name').title)
print(gw.getAllTitles())
# print(gw.getWindowsWithTitle('zlpc')[0])

# zlpc = gw.getWindowsWithTitle('ZLPC')[0]
# zihp = gw.getWindowsWithTitle('In-house processing 2300')[0]
sap_main = gw.getWindowsWithTitle('SAP Easy Access')[0]
# zlt10 = gw.getWindowsWithTitle('Stock transfer: Warehouse 270')[0]

#
# def zlpc():
#     try:
#         title = gw.getWindowsWithTitle('ZLPC')[0]
#     except IndexError:
#         pass


def open_transaction():
    sap_main.activate()
    while True:
        if gui.locateOnScreen(transaction_names['sap_easy_access'], region=names_region):
            gui.click(x=100, y=50, duration=0)
            gui.hotkey('ctrl', 'right')
            gui.hotkey('ctrl', 'left')
            gui.hotkey('ctrl', 'delete')
            gui.write('ZIHP')
            gui.press('enter')
            break

open_transaction()







