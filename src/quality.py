from lib import status
from lib import color

def get(str):
    quality = None

    try:
        quality = str.split("setVideoUrlHigh")[1]
        print("%s Quality: %sHIGH%s" % (status.get("info"), color.get("green", 1), color.get("reset")))
    except:
        try:
            quality = str.split("setVideoUrlLow")[1]
            print("%s Quality: %sLOW%s" % (status.get("info"), color.get("green", 1), color.get("reset")))
        except:
            print("%sNo download found%s" % (color.get("red", 1), color.get("reset")))
            return (84)
    return (quality)