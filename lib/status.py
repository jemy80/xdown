from lib import color

def get(s):
    statuses = {
        "working" : "%s----%s" % (color.get("cyan", 1),   color.get("reset")),
        "input"   : " %s ~>%s" % (color.get("yellow", 1), color.get("reset")),
        "ko"      : "%s KO %s" % (color.get("red", 1),    color.get("reset")),
        "ok"      : "%s OK %s" % (color.get("green", 1),  color.get("reset")),
        "info"    : "%s ?? %s" % (color.get("purple", 1), color.get("reset")),
        "found"   : "%s####%s" % (color.get("yellow", 1), color.get("reset")),
        "error"   : " %s E: %s " % (color.get("red", 1),    color.get("reset"))
    }
    return (statuses.get("%s" % s))