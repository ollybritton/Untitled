from sys import stdout

class Colors:
    PINK = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    END = '\033[0m'

pink = Colors.PINK
blue = Colors.BLUE
green = Colors.GREEN
yellow = Colors.YELLOW
red = Colors.RED
end = Colors.END

def display(string, color = green, end = '\r\n'):
    if color:
        stdout.write("%s%s%s" % (
            color,
            string,
            Colors.END
        ))
    else:
        stdout.write(string)
    if end:
        stdout.write("\n")
