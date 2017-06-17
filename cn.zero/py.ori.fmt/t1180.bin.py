from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "t1180.bin",                # FileName
        "t1180",                    # MapName
        "t1180",                    # Location
        0x004A,                     # MapIndex
        "ed7125",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 74, 0, 1, 0, 2],
    )

    BuildStringList((
        "t1180",                  # 0
    ))

    ScpFunction((
        "Function_0_A0",           # 00, 0
        "Function_1_158",          # 01, 1
        "Function_2_159",          # 02, 2
    ))


    def Function_0_A0(): pass

    label("Function_0_A0")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_E0"),
        (1, "loc_EC"),
        (2, "loc_F8"),
        (3, "loc_104"),
        (4, "loc_110"),
        (5, "loc_11C"),
        (6, "loc_128"),
        (SWITCH_DEFAULT, "loc_134"),
    )


    label("loc_E0")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_140")

    label("loc_EC")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_140")

    label("loc_F8")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_140")

    label("loc_104")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_140")

    label("loc_110")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_140")

    label("loc_11C")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_140")

    label("loc_128")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_140")

    label("loc_134")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_140")

    label("loc_140")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_157")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_140")

    label("loc_157")

    Return()

    # Function_0_A0 end

    def Function_1_158(): pass

    label("Function_1_158")

    Return()

    # Function_1_158 end

    def Function_2_159(): pass

    label("Function_2_159")

    Return()

    # Function_2_159 end

    SaveToFile()

Try(main)
