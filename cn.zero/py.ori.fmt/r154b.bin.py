from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "r154b.bin",                # FileName
        "r154b",                    # MapName
        "r154b",                    # Location
        0x0060,                     # MapIndex
        "ed7200",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x02,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, -3000, 0, 5000, 0, 0, 1, 96, 0, 0, 0, 1],
    )

    BuildStringList((
        "r154b",                  # 0
        "克洛斯贝尔市方向",       # 1
        "乌尔斯拉医科大学方向",   # 2
    ))

    PlaceName(27.450000762939453, 0.0, 1.25, 0x0000, 0x0000, "克洛斯贝尔市方向")
    PlaceName(26.0, 0.0, -92.0, 0x0000, 0x0000, "乌尔斯拉医科大学方向")

    ScpFunction((
        "Function_0_C4",           # 00, 0
        "Function_1_C5",           # 01, 1
    ))


    def Function_0_C4(): pass

    label("Function_0_C4")

    Return()

    # Function_0_C4 end

    def Function_1_C5(): pass

    label("Function_1_C5")

    Return()

    # Function_1_C5 end

    SaveToFile()

Try(main)
