from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "m1010.bin",                # FileName
        "m1010",                    # MapName
        "m1010",                    # Location
        0x006B,                     # MapIndex
        "ed7202",
        0x00080000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 26000, 0, 0, 1, 107, 0, 0, 0, 1],
    )

    BuildStringList((
        "m1010",                  # 0
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

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_B4")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    Jump("loc_B4")

    label("loc_B4")

    Return()

    # Function_1_9D end

    SaveToFile()

Try(main)
