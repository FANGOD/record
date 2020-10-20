#! python
# coding: utf-8
"""
User Name: fangod@cn
Date Time: 2020-10-14 15:39:31
File Name: cbg.py @v1.0
"""
import os
import sys
import platform
try:
    import commentjson as json
except ImportError:
    try:
        import pip
        pip.main(['install', 'commentjson', '--user'])
    except:
        from pip._internal import main
        main.main(['install', 'commentjson', '--user'])
    import commentjson as json


config_list = [
    "fontFace", "fontWeight", "antialiasingMode", "cursorShape", "cursorColor", "colorScheme", "useAcrylic", "acrylicOpacity",
    "scrollbarState", "historySize"
]


class bcolors:
    HEADER = '\033[95m'
    RED = '\033[0;31m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def main(keyword=None):
    if platform.platform().startswith("Windows"):
        select_terminal = 1
        bg_imgs = [os.path.join("d:/BGI/", i) for i in os.listdir("d:/BGI/") if i.endswith(".jpg") or i.endswith(".png")]
        settings_path = "c:/Users/fangod/AppData/Local/Packages/Microsoft.WindowsTerminal_8wekyb3d8bbwe/LocalState/settings.json"
    elif platform.platform().startswith("Linux"):
        select_terminal = 0
        bg_imgs = [os.path.join("d:/BGI/", i) for i in os.listdir("/mnt/d/BGI/") if i.endswith(".jpg") or i.endswith(".png")]
        settings_path = "/mnt/c/Users/fangod/AppData/Local/Packages/Microsoft.WindowsTerminal_8wekyb3d8bbwe/LocalState/settings.json"

    with open(settings_path) as jf:
        settings = json.load(jf)

    ux = settings["profiles"]["list"][select_terminal]

    if keyword and keyword.split("=")[0] in config_list:
        print(bcolors.HEADER + "Default config before change:" + bcolors.ENDC)
        print(bcolors.OKGREEN + "\tfontFace: " + bcolors.OKBLUE + "{}".format(ux.get("fontFace", "Cascadia Mono")))
        print(bcolors.OKCYAN + "\t\taccept: " + bcolors.WARNING + "Cascadia Mono, ...")
        print(bcolors.OKGREEN + "\tfontWeight: " + bcolors.OKBLUE + "{}".format(ux.get("fontWeight", "normal")))
        print(bcolors.OKCYAN + "\t\taccept: " + bcolors.WARNING + "normal, thin, extra-light, light, semi-light, medium, semi-bold, bold, extra-bold, black, extra-black")
        print(bcolors.OKGREEN + "\tantialiasingMode: " + bcolors.OKBLUE + "{}".format(ux.get("antialiasingMode", "grayscale")))
        print(bcolors.OKCYAN + "\t\taccept: " + bcolors.WARNING + "grayscale, cleartype, aliased")
        print(bcolors.OKGREEN + "\tcursorShape: " + bcolors.OKBLUE + "{}".format(ux.get("cursorShape", "bar")))
        print(bcolors.OKCYAN + "\t\taccept: " + bcolors.WARNING + "bar, vintage, underscore, filledBox, emptyBox")
        print(bcolors.OKGREEN + "\tcursorColor: " + bcolors.OKBLUE + "{}".format(ux.get("cursorColor")))
        print(bcolors.OKCYAN + "\t\taccept: " + bcolors.WARNING + "#rgb, #rrggbb")
        print(bcolors.OKGREEN + "\tcolorScheme: " + bcolors.OKBLUE + "{}".format(ux.get("colorScheme")))
        print(bcolors.OKCYAN + "\t\taccept: " + bcolors.WARNING + "Campbell, userset")
        print(bcolors.OKGREEN + "\tuseAcrylic: " + bcolors.OKBLUE + "{}".format(ux.get("useAcrylic", False)))
        print(bcolors.OKCYAN + "\t\taccept: " + bcolors.WARNING + "False, True")
        print(bcolors.OKGREEN + "\tacrylicOpacity: " + bcolors.OKBLUE + "{}".format(ux.get("acrylicOpacity", 0.5)))
        print(bcolors.OKCYAN + "\t\taccept: " + bcolors.WARNING + "float(0) - float(1)")
        print(bcolors.OKGREEN + "\tscrollbarState: " + bcolors.OKBLUE + "{}".format(ux.get("scrollbarState", None)))
        print(bcolors.OKCYAN + "\t\taccept: " + bcolors.WARNING + "visible, hidden")
        print(bcolors.OKGREEN + "\thistorySize: " + bcolors.OKBLUE + "{}".format(ux.get("historySize", 9001)))
        print(bcolors.OKCYAN + "\t\taccept: " + bcolors.WARNING + "int")

    # ssh1
    u4 = settings["profiles"]["list"][3]
    # ssh2
    u5 = settings["profiles"]["list"][4]

    ux = change_unit(ux, keyword, bg_imgs)

    if select_terminal == 0:
        u4 = change_unit(u4, keyword, bg_imgs)
        u5 = change_unit(u5, keyword, bg_imgs)

    print(bcolors.OKGREEN + u"\nplatform:            \t{}".format(platform.platform()))
    print(u"name:                  \t{}".format(ux["name"]))
    print(u"backgroundImage:       \t{}".format(ux.get('backgroundImage')))
    print(u"backgroundImageOpacity:\t{}\n".format(ux["backgroundImageOpacity"]) + bcolors.ENDC)

    if keyword == "df":
        import pandas as pd
        data = [settings["profiles"]["list"][i] for i in [0, 1, 3, 4]]
        df = pd.DataFrame(data).set_index("name").T
        print(bcolors.OKGREEN + "{}".format(df.head(100)))
        print(bcolors.ENDC)

    with open(settings_path, "w") as jf:
        json.dump(settings, jf, indent=4)


def change_unit(unit, keyword, bg_imgs):
    value = 0.10
    if keyword and "=" in keyword:
        keyword, value = keyword.split("=")

    if "backgroundImage" not in unit:
        unit["backgroundImage"] = bg_imgs[0]

    if keyword in config_list:
        print(bcolors.RED + "\nOpen comments when need change config. Maybe it's not safe." + bcolors.BOLD)
        # if value.isdigit():
        #     value = int(value)
        # unit[keyword] = value
    else:
        if keyword in ["up", "u", "A", "a"]:
            unit["backgroundImageOpacity"] += float(value)
        elif keyword in ["down", "d", "do", "B", "b"]:
            unit["backgroundImageOpacity"] -= float(value)
        elif keyword in ["None", "none", "n", "N", "no", "No", "NONE"]:
            del unit["backgroundImage"]
        else:
            try:
                xid = (bg_imgs.index(unit["backgroundImage"]) + 1) % len(bg_imgs)
                unit["backgroundImage"] = bg_imgs[xid]
            except:
                del unit["backgroundImage"]

        if unit["backgroundImageOpacity"] > 1:
            unit["backgroundImageOpacity"] = 1
        if unit["backgroundImageOpacity"] < 0:
            unit["backgroundImageOpacity"] = 0

    print(bcolors.OKGREEN + "Change: " + unit["name"] + bcolors.ENDC)
    return unit


if __name__ == '__main__':
    try:
        keyword = sys.argv[1]
    except:
        keyword = None
    main(keyword)
