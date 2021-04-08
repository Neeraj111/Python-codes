BLACK = '\u001b[30m'
RED = '\u001b[31m'
GREEN = '\u001b[32m'
YELLOW = '\u001b[33m'
BLUE = '\u001b[34m'
MAGENTA = '\u001b[35m'
CYAN = '\u001b[36m'
WHITE = '\u001b[37m'
RESET = '\u001b[0m'

BOLD = '\u001b[1m'
UNDERLINE = '\u001b[4m'
REVERSE = '\u001b[7m'


def color_print(text: str, *effects: str) -> None:
    """
    print 'text' using the ANSI sequences to change color, etc

    :param text: the text to print.
    :param effects: the effect we want. one of the constants defined at
                   the start of this module.
    """
    effects_string = "".join(effects)
    output_string = "{}{}{}".format(effects_string, text, RESET) 
    print(output_string)

color_print("hello cyan", CYAN)
 
color_print("helo reversed blue", BLUE, REVERSE)  
color_print("helo blue", BLUE) 
color_print("helo reversed and underline blue", BLUE,REVERSE,UNDERLINE)  
color_print("helo bold blue", BLUE, BOLD)  
print("YBHJWECGJ IHCEWBCHJ IBCJWHBCH")
color_print("HELLO YELLOW", YELLOW)               