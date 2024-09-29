#! /usr/bin/env python3
"""Hello World Multi Linguas.

Dependendo da linguam configurada no ambiente 
o programa exibe a mensagem correspondente.

Usage: 
Tenha a variavel LANG devidamente configurada ex:
    export LANG=pt_BR

Execution:
    python3 hello.py
    ./hello.py 
"""

__version__ = "0.0.1" #Dunder
__author__ = "Lucas"
__license__ = "Unlicense"

import os

current_language = os.getenv("LANG", "en_US").split(".")[0]


msg = "Hello, World!"

if current_language == "pt_BR":
    msg = "Ola, Mundo!"
elif current_language == "it_IT":
    msg = "Ciao, Mondo!"
        
print(msg)

