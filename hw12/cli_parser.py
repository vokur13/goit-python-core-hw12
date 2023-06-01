import re


def cli_parser(commands):
    cli = []
    query = input().strip().casefold()
    for command in map(lambda command: rf"{command}", commands):
        res = re.match(command, query, flags=re.IGNORECASE)
        if res:
            cli.append(res.group())
            cli.extend(re.sub(command, "", query).split(" ")[1:])
    return cli


if __name__ == "__main__":
    pass
    # cli_parser(commands)
