from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t1130.bin",                # FileName
        "t1130",                    # MapName
        "t1130",                    # Location
        0x0049,                     # MapIndex
        "ed7125",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 73, 0, 0, 0, 1],
    )

    BuildStringList((
        "t1130",                  # 0
    ))

    AddCharChip((
        "chr/ch25600.itc",                   # 00
        "chr/ch25700.itc",                   # 01
    ))

    ScpFunction((
        "Function_0_A4",           # 00, 0
        "Function_1_A5",           # 01, 1
    ))


    def Function_0_A4(): pass

    label("Function_0_A4")

    Return()

    # Function_0_A4 end

    def Function_1_A5(): pass

    label("Function_1_A5")

    Return()

    # Function_1_A5 end

    SaveToFile()

Try(main)
