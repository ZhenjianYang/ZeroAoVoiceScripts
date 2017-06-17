from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "a0005.bin",                # FileName
        "a0000",                    # MapName
        "a0005",                    # Location
        0x0001,                     # MapIndex
        "ed7000",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1],
    )

    BuildStringList((
        "a0005",                  # 0
    ))

    ScpFunction((
        "Function_0_A4",           # 00, 0
        "Function_1_A8",           # 01, 1
        "Function_2_A9",           # 02, 2
        "Function_3_11C",          # 03, 3
    ))


    def Function_0_A4(): pass

    label("Function_0_A4")

    Event(0, 2)
    Return()

    # Function_0_A4 end

    def Function_1_A8(): pass

    label("Function_1_A8")

    Return()

    # Function_1_A8 end

    def Function_2_A9(): pass

    label("Function_2_A9")

    SetMapFlags(0x80)
    ClearMapFlags(0x1)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_BD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10B")
    MenuCmd(0, 0)
    MenuCmd(1, 0, "大型船")
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_F4"),
        (SWITCH_DEFAULT, "loc_FC"),
    )


    label("loc_F4")

    Call(0, 3)
    Jump("loc_106")

    label("loc_FC")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_106")

    Jump("loc_BD")

    label("loc_10B")

    OP_60(0x0)
    OP_57(0x0)
    OP_DB()
    ClearMapFlags(0x80)
    SetMapFlags(0x1)
    Return()

    # Function_2_A9 end

    def Function_3_11C(): pass

    label("Function_3_11C")

    OP_68(-10650, 0, 22010, 0)
    MoveCamera(45, 17, 0, 0)
    OP_6E(260, 0)
    SetCameraDistance(83000, 0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_154")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_250")
    MenuCmd(0, 1)
    MenuCmd(1, 1, "wave00")
    MenuCmd(1, 1, "open 1-30")
    MenuCmd(1, 1, "close 31-57")
    MenuCmd(1, 1, "go 61-90")
    MenuCmd(1, 1, "stop 91-120")
    MenuCmd(1, 1, "lowspd 121-180")
    MenuCmd(1, 1, "hispd  175-233")
    MenuCmd(1, 1, "openclose 234-233")
    MenuCmd(2, 1, -1, -1, 1)
    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_213"),
        (1, "loc_218"),
        (2, "loc_232"),
        (3, "loc_237"),
        (4, "loc_23C"),
        (SWITCH_DEFAULT, "loc_241"),
    )


    label("loc_213")

    Jump("loc_24B")

    label("loc_218")

    OP_71(0x5, 0x1, 0x1E, 0x0, 0x0)
    SetMapObjFlags(0x5, 0x20)
    OP_79(0x5)
    Jump("loc_24B")

    label("loc_232")

    Jump("loc_24B")

    label("loc_237")

    Jump("loc_24B")

    label("loc_23C")

    Jump("loc_24B")

    label("loc_241")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_24B")

    Jump("loc_154")

    label("loc_250")

    OP_60(0x1)
    OP_57(0x0)
    OP_DB()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_3_11C end

    SaveToFile()

Try(main)
