"""Modification des styles."""

from colorama import Back, Fore, Style, deinit, init

init()

print(Fore.RED + Style.NORMAL + 'Un texte rouge')
print(Back.WHITE + 'Avec un fond blanc')
print(Style.BRIGHT + 'Plus lumineux !')
print(Style.RESET_ALL + 'Retour à la normale')

deinit()
