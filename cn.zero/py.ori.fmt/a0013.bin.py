from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "a0013.bin",                # FileName
        "a0000",                    # MapName
        "a0013",                    # Location
        0x0000,                     # MapIndex
        "ed7000",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 1250, 22670, 0, 0, 1, 1, 0, 0, 0, 1],
    )

    BuildStringList((
        "a0013",                  # 0
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
