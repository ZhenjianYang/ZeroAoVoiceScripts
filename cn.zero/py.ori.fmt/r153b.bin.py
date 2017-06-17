from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "r153b.bin",                # FileName
        "r153b",                    # MapName
        "r153b",                    # Location
        0x0060,                     # MapIndex
        "ed7200",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x03,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, -3000, 0, 5000, 0, 0, 1, 96, 0, 0, 0, 1],
    )

    BuildStringList((
        "r153b",                  # 0
        "克洛斯贝尔市方向",       # 1
        "乌尔斯拉医科大学方向",   # 2
    ))

    PlaceName(7.0, 0.0, 52.0, 0x0000, 0x0000, "克洛斯贝尔市方向")
    PlaceName(-89.0, 0.0, -115.0, 0x0000, 0x0000, "乌尔斯拉医科大学方向")
    PlaceName(-24.700000762939453, 0.0, -2.950000047683716, 0x0000, 0x0055, "")

    ScpFunction((
        "Function_0_D8",           # 00, 0
        "Function_1_D9",           # 01, 1
    ))


    def Function_0_D8(): pass

    label("Function_0_D8")

    Return()

    # Function_0_D8 end

    def Function_1_D9(): pass

    label("Function_1_D9")

    Return()

    # Function_1_D9 end

    SaveToFile()

Try(main)
