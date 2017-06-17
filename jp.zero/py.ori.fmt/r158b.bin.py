from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "r158b.bin",                # FileName
        "r158b",                    # MapName
        "r158b",                    # Location
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
        "r158b",                  # 0
        "ウルスラ間道方面",       # 1
        "星見の塔方面",           # 2
    ))

    PlaceName(35.220001220703125, 0.0, 7.400000095367432, 0x0000, 0x0000, "ウルスラ間道方面")
    PlaceName(-128.0, 0.0, -20.0, 0x0000, 0x0000, "星見の塔方面")

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

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D4")
    OP_16(0x3, 0x1, 0x1, 0x0)

    label("loc_D4")

    Return()

    # Function_1_C5 end

    SaveToFile()

Try(main)
