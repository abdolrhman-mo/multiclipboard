# mcb.pyw - Saves and loads pieces of text to the clipboard.
# Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
# py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
# py.exe mcb.pyw list - Loads all keywords to clipboard.

import pyperclip
import sys
import shelve

mcb = shelve.open('mcb')

if sys.argv[1].lower() == 'save':
    mcb[sys.argv[2]] = pyperclip.paste()
elif sys.argv[1].lower() == 'list':
    for itemKey, itemValue in zip(mcb.keys(), mcb.values()):
        print()
        print(f"{itemKey}: {itemValue}")
        print()
elif 'del' in sys.argv[1].lower():
    if sys.argv[2].lower() == 'all':
        mcb.clear()
    else:
        del mcb[sys.argv[2]]

elif sys.argv[1] in mcb.keys():
    pyperclip.copy(mcb[sys.argv[1]])
else:
    print(
        """
python mcb.pyw save <keyword>   - Saves clipboard to keyword.
python mcb.pyw <keyword>        - Loads keyword to clipboard.
python mcb.pyw list             - Loads all keywords to clipboard.
 
    """
    )

mcb.close()
