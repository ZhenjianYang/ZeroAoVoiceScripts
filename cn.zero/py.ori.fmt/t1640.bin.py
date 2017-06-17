from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "t1640.bin",                # FileName
        "t1640",                    # MapName
        "t1640",                    # Location
        0x0057,                     # MapIndex
        "ed7123",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 87, 0, 1, 0, 2],
    )

    BuildStringList((
        "t1640",                  # 0
        "伊姆兹",                 # 1
        "夏鲁鲁",                 # 2
        "弗罗伦斯",               # 3
    ))

    AddCharChip((
        "chr/ch29400.itc",                   # 00
    ))

    DeclNpc(108069,  0,       4539,    258,  261,  0x0, 0,   0,   0,   0,   0,   0,   3,   255,  0)
    DeclNpc(103480,  0,       55840,   90,   261,  0x0, 0,   0,   0,   0,   0,   0,   3,   255,  0)
    DeclNpc(-54110,  0,       95160,   0,    261,  0x0, 0,   0,   0,   0,   0,   0,   3,   255,  0)

    ScpFunction((
        "Function_0_FC",           # 00, 0
        "Function_1_1B4",          # 01, 1
        "Function_2_1B5",          # 02, 2
        "Function_3_1B6",          # 03, 3
    ))


    def Function_0_FC(): pass

    label("Function_0_FC")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_13C"),
        (1, "loc_148"),
        (2, "loc_154"),
        (3, "loc_160"),
        (4, "loc_16C"),
        (5, "loc_178"),
        (6, "loc_184"),
        (SWITCH_DEFAULT, "loc_190"),
    )


    label("loc_13C")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_19C")

    label("loc_148")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_19C")

    label("loc_154")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_19C")

    label("loc_160")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_19C")

    label("loc_16C")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_19C")

    label("loc_178")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_19C")

    label("loc_184")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_19C")

    label("loc_190")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_19C")

    label("loc_19C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1B3")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_19C")

    label("loc_1B3")

    Return()

    # Function_0_FC end

    def Function_1_1B4(): pass

    label("Function_1_1B4")

    Return()

    # Function_1_1B4 end

    def Function_2_1B5(): pass

    label("Function_2_1B5")

    Return()

    # Function_2_1B5 end

    def Function_3_1B6(): pass

    label("Function_3_1B6")

    TalkBegin(0xFE)

    #C0001
    ChrTalk(
        0xFE,
        "外科！外科！\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_3_1B6 end

    SaveToFile()

Try(main)
