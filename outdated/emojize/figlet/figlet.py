from pyfiglet import Figlet

import sys

import random



figlet = Figlet()





if len(sys.argv) == 3:

    # Output user prompt if font name specified in command line, where first index is either '-f' or '--font' and second index is font name

    if (sys.argv[1] == '-f' or sys.argv[1] == '--font'):

        for font in figlet.getFonts():

            figlet.setFont(font=sys.argv[2])

            prompt = input('Input: ')

            print('Output:\n', figlet.renderText(prompt))

            break

    else:

        sys.exit('Invalid usage')

# Output user prompt with random font if no command line

elif len(sys.argv) < 2:

    figlet.setFont(font=random.choice(figlet.getFonts()))

    prompt = input('Input: ')

    print('Output:\n', figlet.renderText(prompt))

else:

    sys.exit('Invalid usage')