def get(c, f = 0):
    colors = {
        "reset"  : "0",
        "red"    : "31",
        "green"  : "32",
        "yellow" : "33",
        "blue"   : "34",
        "purple" : "35",
        "cyan"   : "36",
        "white"  : "37"
    }
    if colors.get("%s" % c) != None and (f >= 0 and f <= 5):
        return ("\033[%s;%sm" % (f, colors.get("%s" % c)))
    return (None)