import os, json
import modules
import utils
import sys

class mainclass:

    version = "1.1 production"

    def processcommand(self, cmd):

        cmds = json.loads(str(open("CONFIG/commands.json", "r").read()))

        if cmd == "help":
            utils.printseparator()
            for command in cmds:
                utils.betterprint("? "+command+" -> "+cmds[command][0])
            utils.printseparator()
        else:
            try:
                exec(cmds[cmd][1])
            except KeyError:
                pass

    def shell(self):
        while True:
            mainclass.processcommand(input(f"{utils.stylelist[2]}{utils.getRandomColor()}? "))

    def logo(self):
        print(f"""{utils.getrandomLogo()}
[{mainclass.version} by github.com/kl3sshydra]

        """)

    def main(self):
        utils.createlogs()
        utils.clearscreen()
        mainclass.logo()
        mainclass.shell()

mainclass = mainclass()
mainclass.main()