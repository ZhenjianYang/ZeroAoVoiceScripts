from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "t1620.bin",                # FileName
        "t1620",                    # MapName
        "t1620",                    # Location
        0x0055,                     # MapIndex
        "ed7123",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 85, 0, 1, 0, 2],
    )

    BuildStringList((
        "t1620",                  # 0
    ))

    AddCharChip((
        "chr/ch29400.itc",                   # 00
        "chr/ch29200.itc",                   # 01
    ))

    DeclActor(-3000,   0,       64599,   1000,    -3000,   1200,    64599,   0x007C, 0,  5,  0x0000)
    DeclActor(-880,    0,       62400,   1000,    -880,    1200,    62400,   0x007C, 0,  6,  0x0000)
    DeclActor(-880,    0,       58300,   1000,    -880,    1200,    58300,   0x007C, 0,  7,  0x0000)
    DeclActor(880,     0,       58300,   1000,    880,     1200,    58300,   0x007C, 0,  8,  0x0000)
    DeclActor(880,     0,       62400,   1000,    880,     1200,    62400,   0x007C, 0,  9,  0x0000)
    DeclActor(3000,    0,       64599,   1000,    3000,    1200,    64599,   0x007C, 0,  10, 0x0000)
    DeclActor(5100,    0,       62400,   1000,    5100,    1200,    62400,   0x007C, 0,  4,  0x0000)
    DeclActor(5100,    0,       58300,   1000,    5100,    1200,    58300,   0x007C, 0,  11, 0x0000)
    DeclActor(6940,    0,       58300,   1000,    6940,    1200,    58300,   0x007C, 0,  12, 0x0000)
    DeclActor(6940,    0,       62400,   1000,    6940,    1200,    62400,   0x007C, 0,  13, 0x0000)
    DeclActor(9000,    0,       64599,   1000,    9000,    1200,    64599,   0x007C, 0,  14, 0x0000)
    DeclActor(11500,   0,       62400,   1000,    11500,   1200,    62400,   0x007C, 0,  15, 0x0000)
    DeclActor(11500,   0,       55800,   1000,    11500,   1200,    55800,   0x007C, 0,  16, 0x0000)

    ScpFunction((
        "Function_0_2B8",          # 00, 0
        "Function_1_370",          # 01, 1
        "Function_2_393",          # 02, 2
        "Function_3_3B0",          # 03, 3
        "Function_4_785",          # 04, 4
        "Function_5_B6A",          # 05, 5
        "Function_6_C10",          # 06, 6
        "Function_7_CB6",          # 07, 7
        "Function_8_D5C",          # 08, 8
        "Function_9_E02",          # 09, 9
        "Function_10_EA8",         # 0A, 10
        "Function_11_F4E",         # 0B, 11
        "Function_12_FF4",         # 0C, 12
        "Function_13_109A",        # 0D, 13
        "Function_14_1140",        # 0E, 14
        "Function_15_11E6",        # 0F, 15
        "Function_16_128C",        # 10, 16
        "Function_17_1332",        # 11, 17
    ))


    def Function_0_2B8(): pass

    label("Function_0_2B8")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_2F8"),
        (1, "loc_304"),
        (2, "loc_310"),
        (3, "loc_31C"),
        (4, "loc_328"),
        (5, "loc_334"),
        (6, "loc_340"),
        (SWITCH_DEFAULT, "loc_34C"),
    )


    label("loc_2F8")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_358")

    label("loc_304")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_358")

    label("loc_310")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_358")

    label("loc_31C")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_358")

    label("loc_328")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_358")

    label("loc_334")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_358")

    label("loc_340")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_358")

    label("loc_34C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_358")

    label("loc_358")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_36F")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_358")

    label("loc_36F")

    Return()

    # Function_0_2B8 end

    def Function_1_370(): pass

    label("Function_1_370")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x72), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0x8)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0x9)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_392")
    Event(0, 3)

    label("loc_392")

    Return()

    # Function_1_370 end

    def Function_2_393(): pass

    label("Function_2_393")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3AA")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)

    label("loc_3AA")

    OP_1B(0xE, 0x0, 0x11)
    Return()

    # Function_2_393 end

    def Function_3_3B0(): pass

    label("Function_3_3B0")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(250, 1000, 52660, 0)
    MoveCamera(45, 28, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(20000, 0)
    SetChrPos(0x101, 0, 0, 52500, 0)
    SetChrPos(0x102, 1200, 0, 52500, 0)
    SetChrPos(0x103, 0, 0, 51300, 0)
    SetChrPos(0x104, 1200, 0, 51300, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_45E")
    SetChrPos(0x109, -1200, 0, 51900, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    Jump("loc_489")

    label("loc_45E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_489")
    SetChrPos(0x10A, -1200, 0, 51900, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    label("loc_489")

    FadeToBright(500, 0)
    OP_0D()

    #C0001
    ChrTalk(
        0x101,
        (
            "#12P#0000F这里就是资料室吗……\x02\x03",

            "芙萝拉小姐好像是\x01",
            "不小心将逾期未还的书籍\x01",
            "放到这里的书架上了啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_68(2900, 1000, 60120, 4000)
    MoveCamera(45, 19, 0, 4000)
    OP_6E(440, 4000)
    SetCameraDistance(28640, 4000)
    OP_6F(0x79)
    Fade(500)
    OP_68(250, 1000, 52660, 0)
    MoveCamera(45, 28, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(20000, 0)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5E3")
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_5E3")

    Sleep(1000)

    #C0002
    ChrTalk(
        0x101,
        (
            "#12P#0006F嗯，是啊……\x01",
            "这么一看，数量还真是不少。\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0x102,
        (
            "#12P#0106F是啊……\x01",
            "确实是个累人的差事呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x103,
        "#12P#0200F真麻烦。\x02",
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x104,
        (
            "#12P#0300F算了，现在只有一本不漏地\x01",
            "仔细调查了。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x101,
        (
            "#12P#0000F是啊……\x01",
            "虽然很辛苦，但还是耐心一点，\x01",
            "认真找找看吧。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_70F")

    #C0007
    ChrTalk(
        0x109,
        "#6P#0501F我也来帮忙吧！\x02",
    )

    CloseMessageWindow()
    Jump("loc_746")

    label("loc_70F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_746")

    #C0008
    ChrTalk(
        0x10A,
        "#6P#0603F………………………………\x02",
    )

    CloseMessageWindow()

    label("loc_746")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_76B")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)

    label("loc_76B")

    SetChrPos(0x0, 0, 0, 52500, 0)
    OP_29(0x28, 0x1, 0x9)
    EventEnd(0x5)
    Return()

    # Function_3_3B0 end

    def Function_4_785(): pass

    label("Function_4_785")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0009
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '有效利用五分钟的零散时间'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber('有效利用五分钟的零散时间', 1)
    EventBegin(0x0)
    Fade(500)
    OP_68(4520, 1000, 62040, 0)
    MoveCamera(54, 30, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(19850, 0)
    SetChrPos(0x101, 4140, 0, 61890, 90)
    SetChrPos(0x102, 3110, 0, 62550, 90)
    SetChrPos(0x103, 2910, 0, 60910, 45)
    SetChrPos(0x104, 4100, 0, 63510, 135)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_879")
    SetChrPos(0x109, 4030, 0, 60190, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    Jump("loc_8A4")

    label("loc_879")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8A4")
    SetChrPos(0x10A, 4030, 0, 60190, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    label("loc_8A4")

    OP_0D()

    #C0010
    ChrTalk(
        0x101,
        (
            "#5P#0005F啊，难道这本就是……！\x02\x03",

            "#0000F嗯，盖有图书馆的印章。\x01",
            "没错，应该就是芙萝拉小姐\x01",
            "从图书馆借的书了。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_942")

    #C0011
    ChrTalk(
        0x109,
        "#12P#0500F太好了，各位！\x02",
    )

    CloseMessageWindow()

    label("loc_942")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_9AA")

    #C0012
    ChrTalk(
        0x102,
        "#6P#0106F终、终于找到了啊……\x02",
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x103,
        (
            "#12P#0211F……我都快要\x01",
            "厌恶书架这种东西了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A61")

    label("loc_9AA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_A04")

    #C0014
    ChrTalk(
        0x102,
        (
            "#6P#0100F总算找到了，\x01",
            "太好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x103,
        "#12P#0206F……我都有点累了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_A61")

    label("loc_A04")


    #C0016
    ChrTalk(
        0x102,
        (
            "#6P#0100F这么快就能找到，\x01",
            "真幸运啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x103,
        (
            "#12P#0203F不用展开地毯式搜索，\x01",
            "实在是万幸呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A61")


    #C0018
    ChrTalk(
        0x104,
        (
            "#5P#0300F不管怎么说，\x01",
            "总算是找到了啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x10E, 0x1F4)

    #C0019
    ChrTalk(
        0x101,
        (
            "#0000F嗯，\x01",
            "我们也差不多该离开这里啦。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B08")

    #C0020
    ChrTalk(
        0x10A,
        (
            "#12P#0606F（真是的，竟然在这种地方\x01",
            "　浪费时间……）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B08")

    OP_29(0x28, 0x1, 0xA)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0x5)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0x7)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0xA)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B31")
    OP_29(0x28, 0x1, 0x1F)

    label("loc_B31")

    FadeToBright(500, 0)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_B60")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)

    label("loc_B60")

    NewScene("t1600", 104, 0, 0)
    IdleLoop()
    Return()

    # Function_4_785 end

    def Function_5_B6A(): pass

    label("Function_5_B6A")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BE3")
    SetChrName("")

    #A0021
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "把书架上的书籍\x01",
            "全部调查了一遍。\x02\x03",

            "……这个书架上\x01",
            "好像没有芙萝拉\x01",
            "逾期未还的书。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x0, 0)
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_C0C")

    label("loc_BE3")

    SetChrName("")

    #A0022
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "这个书架上没有逾期未还的书。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_C0C")

    TalkEnd(0xFF)
    Return()

    # Function_5_B6A end

    def Function_6_C10(): pass

    label("Function_6_C10")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C89")
    SetChrName("")

    #A0023
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "把书架上的书籍\x01",
            "全部调查了一遍。\x02\x03",

            "……这个书架上\x01",
            "好像没有芙萝拉\x01",
            "逾期未还的书。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x0, 1)
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_CB2")

    label("loc_C89")

    SetChrName("")

    #A0024
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "这个书架上没有逾期未还的书。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_CB2")

    TalkEnd(0xFF)
    Return()

    # Function_6_C10 end

    def Function_7_CB6(): pass

    label("Function_7_CB6")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D2F")
    SetChrName("")

    #A0025
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "把书架上的书籍\x01",
            "全部调查了一遍。\x02\x03",

            "……这个书架上\x01",
            "好像没有芙萝拉\x01",
            "逾期未还的书。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x0, 2)
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_D58")

    label("loc_D2F")

    SetChrName("")

    #A0026
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "这个书架上没有逾期未还的书。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_D58")

    TalkEnd(0xFF)
    Return()

    # Function_7_CB6 end

    def Function_8_D5C(): pass

    label("Function_8_D5C")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DD5")
    SetChrName("")

    #A0027
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "把书架上的书籍\x01",
            "全部调查了一遍。\x02\x03",

            "……这个书架上\x01",
            "好像没有芙萝拉\x01",
            "逾期未还的书。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x0, 3)
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_DFE")

    label("loc_DD5")

    SetChrName("")

    #A0028
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "这个书架上没有逾期未还的书。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_DFE")

    TalkEnd(0xFF)
    Return()

    # Function_8_D5C end

    def Function_9_E02(): pass

    label("Function_9_E02")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E7B")
    SetChrName("")

    #A0029
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "把书架上的书籍\x01",
            "全部调查了一遍。\x02\x03",

            "……这个书架上\x01",
            "好像没有芙萝拉\x01",
            "逾期未还的书。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x0, 4)
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_EA4")

    label("loc_E7B")

    SetChrName("")

    #A0030
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "这个书架上没有逾期未还的书。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_EA4")

    TalkEnd(0xFF)
    Return()

    # Function_9_E02 end

    def Function_10_EA8(): pass

    label("Function_10_EA8")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F21")
    SetChrName("")

    #A0031
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "把书架上的书籍\x01",
            "全部调查了一遍。\x02\x03",

            "……这个书架上\x01",
            "好像没有芙萝拉\x01",
            "逾期未还的书。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x0, 5)
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_F4A")

    label("loc_F21")

    SetChrName("")

    #A0032
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "这个书架上没有逾期未还的书。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_F4A")

    TalkEnd(0xFF)
    Return()

    # Function_10_EA8 end

    def Function_11_F4E(): pass

    label("Function_11_F4E")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FC7")
    SetChrName("")

    #A0033
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "把书架上的书籍\x01",
            "全部调查了一遍。\x02\x03",

            "……这个书架上\x01",
            "好像没有芙萝拉\x01",
            "逾期未还的书。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x0, 6)
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_FF0")

    label("loc_FC7")

    SetChrName("")

    #A0034
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "这个书架上没有逾期未还的书。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_FF0")

    TalkEnd(0xFF)
    Return()

    # Function_11_F4E end

    def Function_12_FF4(): pass

    label("Function_12_FF4")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_106D")
    SetChrName("")

    #A0035
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "把书架上的书籍\x01",
            "全部调查了一遍。\x02\x03",

            "……这个书架上\x01",
            "好像没有芙萝拉\x01",
            "逾期未还的书。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x0, 7)
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_1096")

    label("loc_106D")

    SetChrName("")

    #A0036
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "这个书架上没有逾期未还的书。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_1096")

    TalkEnd(0xFF)
    Return()

    # Function_12_FF4 end

    def Function_13_109A(): pass

    label("Function_13_109A")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1113")
    SetChrName("")

    #A0037
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "把书架上的书籍\x01",
            "全部调查了一遍。\x02\x03",

            "……这个书架上\x01",
            "好像没有芙萝拉\x01",
            "逾期未还的书。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x1, 0)
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_113C")

    label("loc_1113")

    SetChrName("")

    #A0038
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "这个书架上没有逾期未还的书。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_113C")

    TalkEnd(0xFF)
    Return()

    # Function_13_109A end

    def Function_14_1140(): pass

    label("Function_14_1140")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11B9")
    SetChrName("")

    #A0039
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "把书架上的书籍\x01",
            "全部调查了一遍。\x02\x03",

            "……这个书架上\x01",
            "好像没有芙萝拉\x01",
            "逾期未还的书。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x1, 1)
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_11E2")

    label("loc_11B9")

    SetChrName("")

    #A0040
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "这个书架上没有逾期未还的书。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_11E2")

    TalkEnd(0xFF)
    Return()

    # Function_14_1140 end

    def Function_15_11E6(): pass

    label("Function_15_11E6")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_125F")
    SetChrName("")

    #A0041
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "把书架上的书籍\x01",
            "全部调查了一遍。\x02\x03",

            "……这个书架上\x01",
            "好像没有芙萝拉\x01",
            "逾期未还的书。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x1, 2)
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_1288")

    label("loc_125F")

    SetChrName("")

    #A0042
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "这个书架上没有逾期未还的书。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_1288")

    TalkEnd(0xFF)
    Return()

    # Function_15_11E6 end

    def Function_16_128C(): pass

    label("Function_16_128C")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1305")
    SetChrName("")

    #A0043
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "把书架上的书籍\x01",
            "全部调查了一遍。\x02\x03",

            "……这个书架上\x01",
            "好像没有芙萝拉\x01",
            "逾期未还的书。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x1, 3)
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_132E")

    label("loc_1305")

    SetChrName("")

    #A0044
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "这个书架上没有逾期未还的书。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_132E")

    TalkEnd(0xFF)
    Return()

    # Function_16_128C end

    def Function_17_1332(): pass

    label("Function_17_1332")

    EventBegin(0x1)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuCmd(0, 0)
    MenuCmd(1, 0, "【离开研究楼】")
    FadeToDark(300, 0, 100)
    OP_0D()
    MenuCmd(1, 0, "放弃")
    MenuCmd(2, 0, -1, -1, 0)
    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_139A"),
        (1, "loc_13A9"),
        (2, "loc_13D6"),
        (SWITCH_DEFAULT, "loc_13E5"),
    )


    label("loc_139A")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_13E5")

    label("loc_13A9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13C7")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_13D1")

    label("loc_13C7")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_13D1")

    Jump("loc_13E5")

    label("loc_13D6")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_13E5")

    label("loc_13E5")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_END)),
        (0, "loc_1401"),
        (1, "loc_150E"),
        (2, "loc_1529"),
        (SWITCH_DEFAULT, "loc_1544"),
    )


    label("loc_1401")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_14B5")

    #C0045
    ChrTalk(
        0x101,
        (
            "#0005F对了……不能保证\x01",
            "约西亚姆医生是否在研究楼中，\x01",
            "还是先去接待处确认一下吧。\x02\x03",

            "#0000F而且，那里也不是无关人员\x01",
            "可以随意进去的地方。\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, 0, 0, 50500, 0)
    EventEnd(0x4)
    Jump("loc_1544")

    label("loc_14B5")

    FadeToDark(1000, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_14DF")
    SetScenarioFlags(0x5C, 0)
    NewScene("t1650", 101, 0, 0)
    IdleLoop()
    Jump("loc_1509")

    label("loc_14DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_14FE")
    SetScenarioFlags(0x5C, 1)
    NewScene("t1650", 101, 0, 0)
    IdleLoop()
    Jump("loc_1509")

    label("loc_14FE")

    EventEnd(0x5)
    NewScene("t1650", 101, 0, 0)
    IdleLoop()

    label("loc_1509")

    Jump("loc_1544")

    label("loc_150E")

    FadeToDark(1000, 0, -1)
    OP_0D()
    EventEnd(0x5)
    NewScene("t1600", 104, 0, 0)
    IdleLoop()
    Jump("loc_1544")

    label("loc_1529")

    Sleep(50)
    SetChrPos(0x0, 0, 0, 50500, 0)
    EventEnd(0x4)
    Jump("loc_1544")

    label("loc_1544")

    Return()

    # Function_17_1332 end

    SaveToFile()

Try(main)
