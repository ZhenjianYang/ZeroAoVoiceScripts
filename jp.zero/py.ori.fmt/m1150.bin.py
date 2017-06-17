from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "m1150.bin",                # FileName
        "m1150",                    # MapName
        "m1150",                    # Location
        0x0073,                     # MapIndex
        "ed7304",
        0x00080000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, -38000, 0, 0, 0, 0, 1, 115, 0, 0, 0, 1],
    )

    BuildStringList((
        "m1150",                  # 0
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

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_C4")
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    OP_11(0xFE, 0xC2, 0xB6, 0x0, 0x104, 0x0)
    Jump("loc_C4")

    label("loc_C4")

    Return()

    # Function_1_9D end

    SaveToFile()

Try(main)
