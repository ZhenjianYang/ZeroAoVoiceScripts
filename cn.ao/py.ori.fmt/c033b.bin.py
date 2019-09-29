from ScenarioHelper import *

def main():
    CreateScenaFile(
        "c033b.bin",                # FileName
        "c033b",                    # MapName
        "c033b",                    # Location
        0x002C,                     # MapIndex
        "ed7513",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 2],
    )

    BuildStringList((
        "c033b",                  # 0
        "哈罗德",                 # 1
        "索菲亚",                 # 2
        "柯林",                   # 3
    ))

    AddCharChip((
        "chr/ch09300.itc",                   # 00
        "chr/ch09302.itc",                   # 01
        "chr/ch09400.itc",                   # 02
        "chr/ch09402.itc",                   # 03
        "chr/ch07200.itc",                   # 04
        "chr/ch07202.itc",                   # 05
    ))

    DeclNpc(-340,    0,       4409,    315,  261,  0x0, 0,   0,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(550,     0,       2039,    180,  261,  0x0, 0,   2,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(37479,   0,       3799,    180,  261,  0x0, 0,   4,   0,   0,   0,   0,   6,   255,  0)

    DeclActor(34620,   0,       7280,    1200,    34620,   1750,    7280,    0x007C, 0,  3,  0x0000)

    ChipFrameInfo(320, 0)                                        # 0

    ScpFunction((
        "Function_0_140",          # 00, 0
        "Function_1_1F0",          # 01, 1
        "Function_2_23A",          # 02, 2
        "Function_3_23B",          # 03, 3
        "Function_4_2E5",          # 04, 4
        "Function_5_438",          # 05, 5
        "Function_6_49E",          # 06, 6
    ))


    def Function_0_140(): pass

    label("Function_0_140")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_178"),
        (1, "loc_184"),
        (2, "loc_190"),
        (3, "loc_19C"),
        (4, "loc_1A8"),
        (5, "loc_1B4"),
        (6, "loc_1C0"),
        (SWITCH_DEFAULT, "loc_1CC"),
    )


    label("loc_178")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_1D8")

    label("loc_184")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_1D8")

    label("loc_190")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_1D8")

    label("loc_19C")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_1D8")

    label("loc_1A8")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_1D8")

    label("loc_1B4")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_1D8")

    label("loc_1C0")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_1D8")

    label("loc_1CC")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_1D8")

    label("loc_1D8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1EF")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_1D8")

    label("loc_1EF")

    Return()

    # Function_0_140 end

    def Function_1_1F0(): pass

    label("Function_1_1F0")

    SetChrPos(0x8, 1940, 200, 6910, 270)
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    SetChrPos(0x9, 40940, 0, -550, 180)
    SetChrFlags(0x9, 0x10)
    SetChrPos(0xA, 40930, 0, -1640, 90)
    Return()

    # Function_1_1F0 end

    def Function_2_23A(): pass

    label("Function_2_23A")

    Return()

    # Function_2_23A end

    def Function_3_23B(): pass

    label("Function_3_23B")

    SetChrName("")

    #A0001
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "摆放着车辆杂志《导力车爱好者月刊vol.1》。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 1)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x36C, 0x0)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2E1")
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0002
    AnonymousTalk(
        0xFF,
        (
            "导力车喷漆式样\x01\x07\x02",

            "『天空色彩』\x07\x00",
            "已经记下来了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    AddItemNumber(0x36C, 1)

    label("loc_2E1")

    TalkEnd(0xFF)
    Return()

    # Function_3_23B end

    def Function_4_2E5(): pass

    label("Function_4_2E5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14A, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D7")

    #C0003
    ChrTalk(
        0x8,
        "#03605F啊，是各位啊。\x02",
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x101,
        "#00000F晚上好，哈罗德先生。\x02",
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x102,
        (
            "#00104F从二层传来了很香的味道……\x01",
            "您太太正在\x01",
            "准备晚餐吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x8,
        (
            "#03600F嗯，是啊。\x01",
            "而且柯林今天\x01",
            "也在帮忙呢。\x02\x03",

            "#03609F呵呵，我刚刚\x01",
            "工作归来，\x01",
            "肚子已经饿扁了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x14A, 6)
    Jump("loc_434")

    label("loc_3D7")


    #C0007
    ChrTalk(
        0x8,
        (
            "#03600F柯林好像\x01",
            "也在帮忙做\x01",
            "今天的晚饭呢。\x02\x03",

            "#03609F呵呵，他们会做些什么呢？\x01",
            "真是期待啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_434")

    TalkEnd(0xFE)
    Return()

    # Function_4_2E5 end

    def Function_5_438(): pass

    label("Function_5_438")

    TalkBegin(0xFE)

    #C0008
    ChrTalk(
        0x9,
        (
            "#03700F接下来只要等着煮熟就好了。\x02\x03",

            "#03709F呵呵，做得很棒哦，柯林。\x01",
            "爸爸一定也会很高兴的。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_5_438 end

    def Function_6_49E(): pass

    label("Function_6_49E")

    TalkBegin(0xFE)

    #C0009
    ChrTalk(
        0xA,
        (
            "#03802F今天的晚饭\x01",
            "是咖喱哦～\x02\x03",

            "#03809F嘿嘿，\x01",
            "菜是我切的～\x01",
            "很厉害吧～？\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_6_49E end

    SaveToFile()

Try(main)
