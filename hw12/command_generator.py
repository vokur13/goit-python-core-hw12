from cli_parser import cli_parser


def command_generator(commands):
    while True:
        com = cli_parser(commands)
        if com[0] in commands and not com[0] in ["good bye", "close", "exit"]:
            yield com
        elif com[0] in commands and com[0] in ["good bye", "close", "exit"]:
            yield com
            break
        else:
            break


if __name__ == "__main__":
    pass
    # main()
