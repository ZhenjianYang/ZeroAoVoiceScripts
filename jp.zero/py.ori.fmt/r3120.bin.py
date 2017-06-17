from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "r3120.bin",                # FileName
        "r3120",                    # MapName
        "r3120",                    # Location
        0x0066,                     # MapIndex
        "ed7203",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, -4500, 16250, -4500, 0, 0, 1, 102, 0, 0, 0, 1],
    )

    BuildStringList((
        "r3120",                  # 0
    ))

    ScpFunction((
        "Function_0_9C",           # 00, 0
        "Function_1_9D",           # 01, 1
    ))


    def Function_0_9C(): pass

    label("Function_0_9C")

    Return()

    # Function_0_9C end

    def Function_1_9D(): pass

    label("Function_1_9D")

    Return()

    # Function_1_9D end

    SaveToFile()

Try(main)
