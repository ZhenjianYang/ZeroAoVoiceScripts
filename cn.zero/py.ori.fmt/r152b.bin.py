from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "r152b.bin",                # FileName
        "r152b",                    # MapName
        "r152b",                    # Location
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
        "r152b",                  # 0
        "克洛斯贝尔市方向",       # 1
        "乌尔斯拉医科大学方向",   # 2
        "星见之塔方向",           # 3
    ))

    PlaceName(2.0, 0.4300000071525574, 40.0, 0x0000, 0x0000, "克洛斯贝尔市方向")
    PlaceName(-59.900001525878906, 0.0, -142.27999877929688, 0x0000, 0x0000, "乌尔斯拉医科大学方向")
    PlaceName(-51.7400016784668, -1.399999976158142, -3.7799999713897705, 0x0000, 0x0000, "星见之塔方向")

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

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E8")
    OP_16(0x3, 0x2, 0x1, 0x0)

    label("loc_E8")

    Return()

    # Function_1_D9 end

    SaveToFile()

Try(main)
