from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "r150b.bin",                # FileName
        "r150b",                    # MapName
        "r150b",                    # Location
        0x0060,                     # MapIndex
        "ed7200",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x04,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, -9000, 0, 0, 1, 96, 0, 0, 0, 1],
    )

    BuildStringList((
        "r150b",                  # 0
        "克洛斯贝尔市方向",       # 1
        "乌尔斯拉医科大学方向",   # 2
        "克洛斯贝尔空港方向",     # 3
    ))

    PlaceName(2.0, 0.0, 20.0, 0x0000, 0x0000, "克洛斯贝尔市方向")
    PlaceName(-27.0, 0.0, -159.0, 0x0000, 0x0000, "乌尔斯拉医科大学方向")
    PlaceName(45.0, 0.0, -24.0, 0x0000, 0x0000, "克洛斯贝尔空港方向")
    PlaceName(-10.649999618530273, 0.0, -11.800000190734863, 0x0000, 0x0055, "")

    ScpFunction((
        "Function_0_EC",           # 00, 0
        "Function_1_ED",           # 01, 1
    ))


    def Function_0_EC(): pass

    label("Function_0_EC")

    Return()

    # Function_0_EC end

    def Function_1_ED(): pass

    label("Function_1_ED")

    Return()

    # Function_1_ED end

    SaveToFile()

Try(main)
