from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t1340.bin",                # FileName
        "t1340",                    # MapName
        "t1340",                    # Location
        0x00B7,                     # MapIndex
        "ed7160",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x1A,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 183, 0, 0, 0, 1],
    )

    BuildStringList((
        "t1340",                  # 0
    ))

    ChipFrameInfo(156, 0)                                        # 0

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

    Sound(148, 1, 100, 0)
    Return()

    # Function_1_9D end

    SaveToFile()

Try(main)
