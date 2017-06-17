from ScenarioHelper import *

def main():
    CreateScenaFile(
        "t3510.bin",                # FileName
        "t3510",                    # MapName
        "t3510",                    # Location
        0x005C,                     # MapIndex
        "ed7150",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\x01',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 92, 0, 2, 0, 3],
    )

    BuildStringList((
        "t3510",                  # 0
        "接待小姐玛尔卡娜",       # 1
        "接待员托马斯",           # 2
        "利卡尔德",               # 3
        "游客",                   # 4
        "游客",                   # 5
        "游客",                   # 6
        "市民",                   # 7
        "市民",                   # 8
        "男孩",                   # 9
        "运送员阿伦",             # 10
        "比利",                   # 11
        "女性士官",               # 12
        "飞艇",                   # 13
        "警官",                   # 14
        "警官",                   # 15
        "格蕾丝",                 # 16
        "雷因兹",                 # 17
        "记者诺蒂亚",             # 18
        "记者",                   # 19
        "记者",                   # 20
        "记者",                   # 21
        "记者",                   # 22
    ))

    AddCharChip((
        "chr/ch10500.itc",                   # 00
        "chr/ch23600.itc",                   # 01
        "chr/ch26000.itc",                   # 02
        "chr/ch28200.itc",                   # 03
        "chr/ch28100.itc",                   # 04
        "chr/ch22000.itc",                   # 05
        "chr/ch22100.itc",                   # 06
        "chr/ch21800.itc",                   # 07
        "chr/ch20200.itc",                   # 08
        "chr/ch20302.itc",                   # 09
        "chr/ch34202.itc",                   # 0A
    ))

    DeclNpc(-10220,  150,     2849,    90,   261,  0x0, 0,   3,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(-8350,   150,     6730,    135,  261,  0x0, 0,   4,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(6679,    0,       5530,    180,  261,  0x0, 0,   2,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(-11300,  5000,    4760,    270,  389,  0x0, 0,   5,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(-10729,  5000,    5769,    225,  389,  0x0, 0,   6,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(-1039,   5000,    13960,   315,  389,  0x0, 0,   7,   0,   0,   0,   0,   13,  255,  0)
    DeclNpc(-5679,   0,       -2539,   225,  389,  0x0, 0,   8,   0,   0,   0,   0,   14,  255,  0)
    DeclNpc(-10319,  5199,    8109,    45,   389,  0x0, 0,   9,   0,   255, 255, 0,   15,  255,  0)
    DeclNpc(-8869,   5199,    10039,   225,  389,  0x0, 0,   10,  0,   255, 255, 0,   16,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   0,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   1,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 18,  0.25999999046325684,   7.989999771118164,     0.0,                   36.0,                  [0.1666666716337204,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.3333333432674408,    0.0,                   -0.04333333298563957,  -3.994999885559082,    -0.0,                  1.0])

    DeclActor(-8690,   0,       2530,    1000,    -10220,  1600,    2850,    0x007E, 0,  7,  0x0000)
    DeclActor(-7210,   0,       5680,    1000,    -8350,   1600,    6730,    0x007E, 0,  9,  0x0000)
    DeclActor(-7590,   0,       -2440,   1200,    -7590,   1500,    -2440,   0x007C, 0,  17, 0x0000)

    ChipFrameInfo(1136, 0)                                       # 0

    ScpFunction((
        "Function_0_470",          # 00, 0
        "Function_1_520",          # 01, 1
        "Function_2_56D",          # 02, 2
        "Function_3_6EA",          # 03, 3
        "Function_4_75D",          # 04, 4
        "Function_5_9F8",          # 05, 5
        "Function_6_AA7",          # 06, 6
        "Function_7_F2D",          # 07, 7
        "Function_8_F31",          # 08, 8
        "Function_9_12EA",         # 09, 9
        "Function_10_12EE",        # 0A, 10
        "Function_11_16DC",        # 0B, 11
        "Function_12_173F",        # 0C, 12
        "Function_13_17C7",        # 0D, 13
        "Function_14_184B",        # 0E, 14
        "Function_15_18C8",        # 0F, 15
        "Function_16_1937",        # 10, 16
        "Function_17_1988",        # 11, 17
        "Function_18_1A53",        # 12, 18
        "Function_19_1B54",        # 13, 19
        "Function_20_1D3A",        # 14, 20
        "Function_21_1DF3",        # 15, 21
        "Function_22_2702",        # 16, 22
        "Function_23_291C",        # 17, 23
        "Function_24_2A64",        # 18, 24
        "Function_25_2B50",        # 19, 25
        "Function_26_3367",        # 1A, 26
        "Function_27_37F5",        # 1B, 27
        "Function_28_3F40",        # 1C, 28
        "Function_29_40C2",        # 1D, 29
        "Function_30_41E0",        # 1E, 30
    ))


    def Function_0_470(): pass

    label("Function_0_470")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_4A8"),
        (1, "loc_4B4"),
        (2, "loc_4C0"),
        (3, "loc_4CC"),
        (4, "loc_4D8"),
        (5, "loc_4E4"),
        (6, "loc_4F0"),
        (SWITCH_DEFAULT, "loc_4FC"),
    )


    label("loc_4A8")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_508")

    label("loc_4B4")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_508")

    label("loc_4C0")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_508")

    label("loc_4CC")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_508")

    label("loc_4D8")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_508")

    label("loc_4E4")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_508")

    label("loc_4F0")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_508")

    label("loc_4FC")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_508")

    label("loc_508")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_51F")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_508")

    label("loc_51F")

    Return()

    # Function_0_470 end

    def Function_1_520(): pass

    label("Function_1_520")

    SetMapObjFlags(0x0, 0x2000000)
    SetMapObjFlags(0x2, 0x2000000)
    SetMapObjFlags(0x5, 0x2000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_546")
    ClearMapObjFlags(0x5, 0x2000000)
    Jump("loc_555")

    label("loc_546")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_555")
    ClearMapObjFlags(0x5, 0x2000000)

    label("loc_555")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x85, 0x0, 0x2)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_56C")
    ClearMapObjFlags(0x0, 0x2000000)

    label("loc_56C")

    Return()

    # Function_1_520 end

    def Function_2_56D(): pass

    label("Function_2_56D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x85, 0x0, 0x2)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_594")
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 6600, 0, -3500, 180)

    label("loc_594")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_5D5")
    SetChrPos(0x8, 0, 0, -5500, 90)
    SetChrPos(0x9, 1500, 0, -5500, 270)
    SetChrPos(0xA, 340, 0, 6490, 180)
    Jump("loc_6A7")

    label("loc_5D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_5E3")
    Jump("loc_6A7")

    label("loc_5E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_5F1")
    Jump("loc_6A7")

    label("loc_5F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_66E")
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    SetChrChipByIndex(0xF, 0x9)
    SetChrSubChip(0xF, 0x0)
    EndChrThread(0xF, 0x0)
    SetChrBattleFlags(0xF, 0x4)
    SetChrChipByIndex(0x10, 0xA)
    SetChrSubChip(0x10, 0x0)
    EndChrThread(0x10, 0x0)
    SetChrBattleFlags(0x10, 0x4)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_669")
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, 5480, 0, 5530, 90)
    TurnDirection(0xA, 0x12, 0)

    label("loc_669")

    Jump("loc_6A7")

    label("loc_66E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_67C")
    Jump("loc_6A7")

    label("loc_67C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_69E")
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xB, 0x10)
    Jump("loc_6A7")

    label("loc_69E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_6A7")

    label("loc_6A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_6BE")
    ClearScenarioFlags(0x22, 0)
    SetScenarioFlags(0x0, 4)
    Event(0, 19)
    Jump("loc_6E9")

    label("loc_6BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_6D5")
    ClearScenarioFlags(0x22, 1)
    SetScenarioFlags(0x0, 4)
    Event(0, 21)
    Jump("loc_6E9")

    label("loc_6D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 2)), scpexpr(EXPR_END)), "loc_6E9")
    ClearScenarioFlags(0x22, 2)
    SetMapFlags(0x10000000)
    Event(0, 26)

    label("loc_6E9")

    Return()

    # Function_2_56D end

    def Function_3_6EA(): pass

    label("Function_3_6EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_6FE")
    OP_24(0x86)
    ClearScenarioFlags(0x0, 4)
    Jump("loc_71A")

    label("loc_6FE")

    SoundDistance(0x86, 0x16D0, 0x0, 0x259E, 0x1388, 0x30D40, 0x64, 0x0)

    label("loc_71A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_72B")
    OP_65(0x0, 0x1)
    OP_65(0x1, 0x1)

    label("loc_72B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_745")
    ModifyEventFlags(0, 0, 0x80)
    ClearMapObjFlags(0x3, 0x10)
    ClearMapObjFlags(0x4, 0x10)

    label("loc_745")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x85, 0x0, 0x2)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_75C")
    ClearMapObjFlags(0x0, 0x4)

    label("loc_75C")

    Return()

    # Function_3_6EA end

    def Function_4_75D(): pass

    label("Function_4_75D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x85, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x85, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x85, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x175, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_795")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x175, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_791")
    Call(0, 22)
    Return()

    label("loc_791")

    Call(0, 23)
    Return()

    label("loc_795")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x85, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_91C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8A2")

    #C0001
    ChrTalk(
        0xFE,
        (
            "请按顺序前往送错包裹\x01",
            "的地点，并用正确的\x01",
            "包裹交换。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0xFE,
        (
            "先去玛因兹，然后是乌尔斯拉医院，\x01",
            "最后去住宅街的民宅就行了。\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0xFE,
        (
            "住宅街民宅的具体地址\x01",
            "写在送货单上，\x01",
            "去之前先查看一下吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0xFE,
        "不好意思啊，这件差事实在是很麻烦，拜托你们了。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_917")

    label("loc_8A2")


    #C0005
    ChrTalk(
        0xFE,
        (
            "先去玛因兹，然后是乌尔斯拉医院，\x01",
            "最后去住宅街的民宅就行了。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0xFE,
        "不好意思啊，这件差事实在是很麻烦，拜托你们了。\x02",
    )

    CloseMessageWindow()

    label("loc_917")

    Jump("loc_9F4")

    label("loc_91C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9A0")

    #C0007
    ChrTalk(
        0xFE,
        "辛苦啦，多亏了你们，真是帮大忙了。\x02",
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0xFE,
        "好～顺利解决了，得赶快向老大……\x02",
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0xFE,
        "不对，得赶快去向经理报告才行。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_9F4")

    label("loc_9A0")


    #C0010
    ChrTalk(
        0xFE,
        "辛苦啦，多亏你们帮忙，总算得救了。\x02",
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0xFE,
        "如果以后再有什么事，还要请你们帮忙哦。\x02",
    )

    CloseMessageWindow()

    label("loc_9F4")

    TalkEnd(0xFE)
    Return()

    # Function_4_75D end

    def Function_5_9F8(): pass

    label("Function_5_9F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A3B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19B, 6)), scpexpr(EXPR_END)), "loc_A37")
    Call(0, 28)
    Jump("loc_A3A")

    label("loc_A37")

    Call(0, 27)

    label("loc_A3A")

    Return()

    label("loc_A3B")

    TalkBegin(0x12)

    #C0012
    ChrTalk(
        0xFE,
        (
            "竟然在克洛斯贝尔陷入这种\x01",
            "困境的时候骗取医疗物资……\x01",
            "绝对不能饶恕。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0xFE,
        (
            "你们一定要\x01",
            "抓到犯人啊！\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x12)
    Return()

    # Function_5_9F8 end

    def Function_6_AA7(): pass

    label("Function_6_AA7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_AEA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19B, 6)), scpexpr(EXPR_END)), "loc_AE6")
    Call(0, 28)
    Jump("loc_AE9")

    label("loc_AE6")

    Call(0, 27)

    label("loc_AE9")

    Return()

    label("loc_AEA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_B54")

    #C0014
    ChrTalk(
        0xA,
        (
            "警察刚才来这里了，\x01",
            "现在好像正在飞艇坪调查猎兵的痕迹。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0xA,
        "不好意思，前方禁止入内。\x02",
    )

    CloseMessageWindow()
    Jump("loc_F29")

    label("loc_B54")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_B62")
    Jump("loc_F29")

    label("loc_B62")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_B70")
    Jump("loc_F29")

    label("loc_B70")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_E26")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_CC3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C3C")

    #C0016
    ChrTalk(
        0xFE,
        (
            "你们漂亮地夺回了\x01",
            "医疗物资啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0xFE,
        (
            "我刚才接到了乌尔斯拉医院\x01",
            "的联络，听说货物已经送到了，\x01",
            "总算是松了一口气。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0xFE,
        (
            "今后一定要更加仔细，\x01",
            "避免这样的事情\x01",
            "再次发生。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_CBE")

    label("loc_C3C")


    #C0019
    ChrTalk(
        0xFE,
        (
            "我刚才接到了乌尔斯拉医院\x01",
            "的联络，听说货物已经送到了，\x01",
            "总算是松了一口气。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0xFE,
        (
            "今后一定要更加仔细，\x01",
            "避免这样的事情\x01",
            "再次发生。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CBE")

    Jump("loc_E21")

    label("loc_CC3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x40)"), scpexpr(EXPR_END)), "loc_DC7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D74")

    #C0021
    ChrTalk(
        0xFE,
        (
            "……医疗物资最后还是\x01",
            "被骗子带走了。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0xFE,
        (
            "别难过，这并不是你们的错。\x01",
            "都怪我不好，竟然糊里糊涂地被他骗过了。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0xFE,
        (
            "今后必须要更加\x01",
            "仔细才行啊……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_DC2")

    label("loc_D74")


    #C0024
    ChrTalk(
        0xFE,
        (
            "……医疗物资最后还是\x01",
            "被骗子带走了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0xFE,
        (
            "今后必须要更加\x01",
            "仔细才行啊……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DC2")

    Jump("loc_E21")

    label("loc_DC7")


    #C0026
    ChrTalk(
        0xFE,
        (
            "竟然被伪造的文件欺骗了……\x01",
            "可恶，这都怪我啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0xFE,
        (
            "稍后必须要和\x01",
            "乌尔斯拉医院联络……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E21")

    Jump("loc_F29")

    label("loc_E26")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_F29")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EC9")

    #C0028
    ChrTalk(
        0xFE,
        (
            "卡普亚特急便的那些家伙\x01",
            "来空港越来越频繁了。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0xFE,
        (
            "听说他们是一家民营的运输公司，\x01",
            "业绩一直在飞速提升。\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0xFE,
        "哎呀呀，经营得真不错呢。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_F29")

    label("loc_EC9")


    #C0031
    ChrTalk(
        0xFE,
        (
            "听说卡普亚特急便\x01",
            "是一家民营的运输公司，\x01",
            "业绩一直在飞速提升。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0xFE,
        "哎呀呀，经营得真不错呢。\x02",
    )

    CloseMessageWindow()

    label("loc_F29")

    TalkEnd(0xFE)
    Return()

    # Function_6_AA7 end

    def Function_7_F2D(): pass

    label("Function_7_F2D")

    Call(0, 8)
    Return()

    # Function_7_F2D end

    def Function_8_F31(): pass

    label("Function_8_F31")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1047")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FE8")

    #C0033
    ChrTalk(
        0x8,
        (
            "猎兵和徘徊在市里的怪物都消失了，\x01",
            "我总算可以返回职场……\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x8,
        (
            "但航空件现在全都不能发，\x01",
            "今后该怎么办才好呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x8,
        (
            "我们还能回到之前的\x01",
            "正常生活吗……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1042")

    label("loc_FE8")


    #C0036
    ChrTalk(
        0x8,
        (
            "航空件现在全都不能发，\x01",
            "今后该怎么办才好呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x8,
        (
            "我们还能回到之前的\x01",
            "正常生活吗……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1042")

    Jump("loc_12E6")

    label("loc_1047")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1191")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1117")

    #C0038
    ChrTalk(
        0x8,
        (
            "利贝尔和雷米菲利亚\x01",
            "都对克洛斯贝尔这次的\x01",
            "复兴活动提供了很大支援。\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x8,
        (
            "他们筹集了援助金与物资，\x01",
            "使重建作业的状况很快就\x01",
            "趋于平稳。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x8,
        (
            "身为克洛斯贝尔的居民，\x01",
            "真是非常感激他们。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_118C")

    label("loc_1117")


    #C0041
    ChrTalk(
        0x8,
        (
            "利贝尔和雷米菲利亚\x01",
            "都对克洛斯贝尔这次的\x01",
            "复兴活动提供了很大支援。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x8,
        (
            "身为克洛斯贝尔的居民，\x01",
            "真是非常感激他们。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_118C")

    Jump("loc_12E6")

    label("loc_1191")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_12E6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1260")

    #C0043
    ChrTalk(
        0x8,
        (
            "独立提案发表之后，\x01",
            "似乎有客人对\x01",
            "克洛斯贝尔的情势感到不安。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x8,
        (
            "不少客人都将\x01",
            "来此旅行的计划\x01",
            "临时取消了。\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x8,
        (
            "虽然也能理解，\x01",
            "但站在克洛斯贝尔居民的立场来看，\x01",
            "真是有点失落呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_12E6")

    label("loc_1260")


    #C0046
    ChrTalk(
        0x8,
        (
            "独立提案发表之后，\x01",
            "似乎有客人对\x01",
            "克洛斯贝尔的情势感到不安。\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x8,
        (
            "虽然也能理解，\x01",
            "但站在克洛斯贝尔居民的立场来看，\x01",
            "真是有点失落呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12E6")

    TalkEnd(0x8)
    Return()

    # Function_8_F31 end

    def Function_9_12EA(): pass

    label("Function_9_12EA")

    Call(0, 10)
    Return()

    # Function_9_12EA end

    def Function_10_12EE(): pass

    label("Function_10_12EE")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_141E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13DE")

    #C0048
    ChrTalk(
        0x9,
        (
            "独立宣言发表之后，\x01",
            "这个空港便成为迎击\x01",
            "两大国入侵势力的据点了。\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x9,
        (
            "据说当时袭击城市的\x01",
            "那些猎兵曾作为总统的\x01",
            "私人部队驻守在此。\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x9,
        (
            "……该说什么好呢。\x01",
            "相信了总统的话，并赞成独立的我们，\x01",
            "现在该作何感想……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1419")

    label("loc_13DE")


    #C0051
    ChrTalk(
        0x9,
        (
            "相信了总统的话，并赞成独立的我们，\x01",
            "现在该作何感想……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1419")

    Jump("loc_16D8")

    label("loc_141E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_156E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14EF")

    #C0052
    ChrTalk(
        0x9,
        (
            "听说克洛斯贝尔\x01",
            "遭受袭击的那起事件\x01",
            "是帝国策动的阴谋。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x9,
        (
            "虽然并没有确凿证据……\x01",
            "但毕竟\x01",
            "无风不起浪。\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x9,
        (
            "从帝国长久以来的做法手段来看，\x01",
            "让人不能不觉得\x01",
            "那种传闻很可能是真的……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1569")

    label("loc_14EF")


    #C0055
    ChrTalk(
        0x9,
        (
            "听说克洛斯贝尔\x01",
            "遭受袭击的那起事件\x01",
            "是帝国策动的阴谋。\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x9,
        (
            "虽然并没有确凿证据，\x01",
            "但总让人觉得\x01",
            "那种传闻很可能是真的……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1569")

    Jump("loc_16D8")

    label("loc_156E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_16D8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_164D")

    #C0057
    ChrTalk(
        0x9,
        (
            "这里是出入境手续办理处，\x01",
            "行李的托运也可以在此办理。\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x9,
        (
            "『卡普亚特急便』的人正好在这里，\x01",
            "如果想寄包裹到国外，\x01",
            "就去找他们如何？\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x9,
        (
            "听说他们的运送速度比一般空运更快，\x01",
            "所以广受顾客的好评呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_16D8")

    label("loc_164D")


    #C0060
    ChrTalk(
        0x9,
        (
            "『卡普亚特急便』的人正好在这里，\x01",
            "如果想寄包裹到国外，\x01",
            "就去找他们如何？\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x9,
        (
            "听说他们的运送速度比一般空运更快，\x01",
            "所以广受顾客的好评呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16D8")

    TalkEnd(0x9)
    Return()

    # Function_10_12EE end

    def Function_11_16DC(): pass

    label("Function_11_16DC")

    TalkBegin(0xFE)

    #C0062
    ChrTalk(
        0xFE,
        (
            "哦哦～看啊看啊！\x01",
            "可以看到飞船起飞呢！\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0xFE,
        (
            "亲爱的，你也来看看啊！\x01",
            "这真是太让人兴奋了！\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_11_16DC end

    def Function_12_173F(): pass

    label("Function_12_173F")

    TalkBegin(0xFE)

    #C0064
    ChrTalk(
        0xFE,
        (
            "呼，男人可真是的，\x01",
            "不管多大都是个孩子呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0xFE,
        (
            "不过，那么大的东西竟然能\x01",
            "飞在空中，确实是很惊人的技术。\x01",
            "这倒是不得不佩服啊。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_12_173F end

    def Function_13_17C7(): pass

    label("Function_13_17C7")

    TalkBegin(0xFE)

    #C0066
    ChrTalk(
        0xFE,
        (
            "啊，那艘绿色的飞艇\x01",
            "好像和客船不同呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0xFE,
        (
            "看起来好像是莱恩福尔特公司\x01",
            "制造的旧式高速飞艇……\x01",
            "大概是某个贵族的所有物吧。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_13_17C7 end

    def Function_14_184B(): pass

    label("Function_14_184B")

    TalkBegin(0xFE)

    #C0068
    ChrTalk(
        0xFE,
        (
            "城市的复兴工作已经告一段落，\x01",
            "我想和家人们去\x01",
            "外国暂避一段时间。\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0xFE,
        (
            "我的老家在\x01",
            "雷米菲利亚地区，\x01",
            "那里一定很安全。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_14_184B end

    def Function_15_18C8(): pass

    label("Function_15_18C8")

    TalkBegin(0xFE)

    #C0070
    ChrTalk(
        0xFE,
        (
            "呼，老公突然要带我们返乡，\x01",
            "我真是吃了一惊……\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0xFE,
        (
            "不过他的话确实有一定道理。\x01",
            "最近好像很不太平……\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_15_18C8 end

    def Function_16_1937(): pass

    label("Function_16_1937")

    TalkBegin(0xFE)

    #C0072
    ChrTalk(
        0xFE,
        (
            "我们这就要坐飞船啦～\x01",
            "嘿嘿嘿，好期待～\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0xFE,
        (
            "一定要在天上\x01",
            "拍很多照片。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_16_1937 end

    def Function_17_1988(): pass

    label("Function_17_1988")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_19F4")

    #A0074
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "欢迎来到克洛斯贝尔独立国！\x01",
            "如有住宿需求，\x01",
            "请前往『千禧酒店』！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A3A")

    label("loc_19F4")


    #A0075
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "欢迎来到克洛斯贝尔自治州！\x01",
            "如有住宿需求，\x01",
            "请前往『千禧酒店』！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A3A")

    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_17_1988 end

    def Function_18_1A53(): pass

    label("Function_18_1A53")

    EventBegin(0x1)
    OP_4B(0xA, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_1AC0")

    #C0076
    ChrTalk(
        0xA,
        (
            "警察刚才来这里了，\x01",
            "现在好像正在飞艇坪调查猎兵的痕迹。\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0xA,
        "不好意思，前方禁止入内。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1B05")

    label("loc_1AC0")

    TurnDirection(0xA, 0x0, 500)

    #C0078
    ChrTalk(
        0xA,
        (
            "啊……\x01",
            "那边是登船口哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0xA,
        (
            "如果没有票，\x01",
            "是无法进入的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B05")

    Sleep(50)
    SetChrPos(0x0, 960, 0, 5140, 180)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1B46")
    TurnDirection(0xA, 0x12, 0)
    Jump("loc_1B4D")

    label("loc_1B46")

    OP_93(0xA, 0xB4, 0x0)

    label("loc_1B4D")

    OP_4C(0xA, 0xFF)
    EventEnd(0x4)
    Return()

    # Function_18_1A53 end

    def Function_19_1B54(): pass

    label("Function_19_1B54")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch06000.itc", 0x1E)
    LoadChrToIndex("apl/ch50314.itc", 0x1F)
    LoadChrToIndex("chr/ch47900.itc", 0x20)
    LoadChrToIndex("chr/ch27400.itc", 0x21)
    LoadChrToIndex("chr/ch27800.itc", 0x22)
    LoadChrToIndex("chr/ch27900.itc", 0x23)
    LoadChrToIndex("chr/ch27600.itc", 0x24)
    LoadEffect(0x0, "event/eva02_00.eff")
    SetChrChipByIndex(0x17, 0x1E)
    SetChrSubChip(0x17, 0x0)
    ClearChrFlags(0x17, 0x80)
    SetChrFlags(0x17, 0x8000)
    SetChrChipByIndex(0x18, 0x1F)
    SetChrSubChip(0x18, 0x0)
    ClearChrFlags(0x18, 0x80)
    SetChrFlags(0x18, 0x8000)
    SetChrChipByIndex(0x19, 0x20)
    SetChrSubChip(0x19, 0x0)
    ClearChrFlags(0x19, 0x80)
    SetChrFlags(0x19, 0x8000)
    SetChrChipByIndex(0x1A, 0x21)
    SetChrSubChip(0x1A, 0x0)
    ClearChrFlags(0x1A, 0x80)
    SetChrFlags(0x1A, 0x8000)
    SetChrChipByIndex(0x1B, 0x22)
    SetChrSubChip(0x1B, 0x0)
    ClearChrFlags(0x1B, 0x80)
    SetChrFlags(0x1B, 0x8000)
    SetChrChipByIndex(0x1C, 0x23)
    SetChrSubChip(0x1C, 0x0)
    ClearChrFlags(0x1C, 0x80)
    SetChrFlags(0x1C, 0x8000)
    SetChrChipByIndex(0x1D, 0x24)
    SetChrSubChip(0x1D, 0x0)
    ClearChrFlags(0x1D, 0x80)
    SetChrFlags(0x1D, 0x8000)
    SetMapObjFlags(0x5, 0x1000)
    ClearMapObjFlags(0x5, 0x4)
    SetChrFlags(0x0, 0x80)
    SetChrBattleFlags(0x0, 0x8000)
    SetChrFlags(0x1, 0x80)
    SetChrBattleFlags(0x1, 0x8000)
    SetChrFlags(0x2, 0x80)
    SetChrBattleFlags(0x2, 0x8000)
    SetChrFlags(0x3, 0x80)
    SetChrBattleFlags(0x3, 0x8000)
    SetChrPos(0x17, -1450, 5000, 13350, 0)
    SetChrPos(0x18, -900, 5000, 13950, 0)
    SetChrPos(0x19, 3000, 5000, 13450, 0)
    SetChrPos(0x1A, 1150, 5000, 13950, 0)
    SetChrPos(0x1B, -3150, 5000, 13350, 45)
    SetChrPos(0x1C, 1550, 5000, 12500, 0)
    SetChrPos(0x1D, 4700, 5000, 13000, 0)
    BeginChrThread(0x18, 3, 0, 20)
    OP_68(1000, 8000, 13250, 0)
    MoveCamera(315, 15, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(37800, 0)
    OP_68(1000, 6000, 13250, 5000)
    SetCameraDistance(35800, 5000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 5)
    NewScene("c0100", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_19_1B54 end

    def Function_20_1D3A(): pass

    label("Function_20_1D3A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1DF2")
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1D68")
    Sleep(500)
    Jump("loc_1DB0")

    label("loc_1D68")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x28), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1D7F")
    Sleep(1000)
    Jump("loc_1DB0")

    label("loc_1D7F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3C), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1D96")
    Sleep(1500)
    Jump("loc_1DB0")

    label("loc_1D96")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x50), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1DAD")
    Sleep(2000)
    Jump("loc_1DB0")

    label("loc_1DAD")

    Sleep(2500)

    label("loc_1DB0")

    PlayEffect(0x0, 0xFF, 0xFE, 0x3, 0, 1200, 400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(810, 0, 80, 0)
    Jump("Function_20_1D3A")

    label("loc_1DF2")

    Return()

    # Function_20_1D3A end

    def Function_21_1DF3(): pass

    label("Function_21_1DF3")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch11200.itc", 0x1E)
    LoadChrToIndex("chr/ch00102.itc", 0x20)
    LoadChrToIndex("chr/ch02902.itc", 0x22)
    LoadChrToIndex("apl/ch51212.itc", 0x24)
    LoadChrToIndex("chr/ch30000.itc", 0x25)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu07100.itp")
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis416.itp")
    SetChrChipByIndex(0x102, 0x20)
    SetChrSubChip(0x102, 0x1)
    SetChrChipByIndex(0x109, 0x22)
    SetChrSubChip(0x109, 0x2)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x109, 0x4)
    SetChrPos(0x101, 3000, 5000, 11400, 0)
    SetChrPos(0x102, 2700, 5100, 13000, 90)
    SetChrPos(0x104, 4500, 5000, 10600, 0)
    SetChrPos(0x109, 4800, 5100, 12300, 270)
    SetChrPos(0x105, 3300, 5000, 10100, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrChipByIndex(0x13, 0x1E)
    SetChrSubChip(0x13, 0x0)
    SetChrFlags(0x13, 0x8000)
    SetChrPos(0x13, -8300, 5000, 6700, 90)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x8000)
    SetChrFlags(0xA, 0x8000)
    SetChrChipByIndex(0x15, 0x25)
    SetChrSubChip(0x15, 0x0)
    ClearChrFlags(0x15, 0x80)
    SetChrFlags(0x15, 0x8000)
    SetChrPos(0x15, -4300, 0, -6800, 45)
    BeginChrThread(0x15, 0, 0, 0)
    SetChrChipByIndex(0x16, 0x25)
    SetChrSubChip(0x16, 0x0)
    ClearChrFlags(0x16, 0x80)
    SetChrFlags(0x16, 0x8000)
    SetChrPos(0x16, -3700, 0, 6600, 180)
    BeginChrThread(0x16, 0, 0, 0)
    ClearChrFlags(0x14, 0x80)
    OP_78(0x5, 0x14)
    OP_49()
    SetChrPos(0x14, -7700, 0, 29900, 270)
    OP_D5(0x14, 0x0, 0x41EB0, 0x0, 0x0)
    SetMapObjFlags(0x5, 0x1000)
    ClearMapObjFlags(0x5, 0x4)
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    OP_11(0xE4, 0xA9, 0x9D, 0x32, 0xBE, 0x0)
    OP_68(0, 2000, 0, 0)
    MoveCamera(330, 17, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(30000, 0)
    OP_68(0, 7500, 0, 9000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)
    Sleep(300)
    Fade(500)
    OP_68(4300, 6500, 12000, 0)
    MoveCamera(330, 20, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(22000, 0)
    SetCameraDistance(20500, 2000)
    OP_6F(0x79)

    #C0080
    ChrTalk(
        0x109,
        (
            "#6P#10102F利贝尔王国的高速巡洋舰\x01",
            "『埃尔赛尤号』……\x02\x03",

            "#10109F啊……\x01",
            "确实是艘很棒的飞船呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0x102,
        (
            "#00104F#6P使蔡斯中央工房名震天下的\x01",
            "世界最高速飞船……\x02\x03",

            "#00100F据说至今仍在不断刷新自己保持的速度记录，\x01",
            "遥遥领先于其它飞船。\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x104,
        (
            "#6P#00309F利贝尔的公主殿下就是乘坐它\x01",
            "抵达克洛斯贝尔的啊。\x02\x03",

            "#00302F记得是科洛蒂娅公主殿下吧？\x01",
            "感觉是个非常高贵的人呢。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 500)

    #C0083
    ChrTalk(
        0x101,
        (
            "#00004F#5P准确地说，并不是『公主』，\x01",
            "而是『王太女』。\x02\x03",

            "#00000F也就是利贝尔王国\x01",
            "下一任的女王陛下。\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x104,
        (
            "#6P#00305F哈～原来如此。\x02\x03",

            "#00301F把我们叫到这里的……\x01",
            "该不会就是她本人吧？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x102, 0x2)
    Sleep(300)

    #C0085
    ChrTalk(
        0x102,
        (
            "#5P#00106F唔……\x01",
            "这就实在猜不到了。\x02\x03",

            "#00108F如果去问问贝尔，\x01",
            "倒是可以了解到殿下\x01",
            "的行程安排表……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x105, 0x13, 500)

    def lambda_22F4():

        label("loc_22F4")

        TurnDirection(0xFE, 0x13, 500)
        Yield()
        Jump("loc_22F4")

    QueueWorkItem2(0x105, 2, lambda_22F4)

    #C0086
    ChrTalk(
        0x105,
        (
            "#11P#10302F呵呵……\x01",
            "好像已经没有那个必要了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 500)

    #C0087
    ChrTalk(
        0x101,
        "#5P#00005F哎？\x02",
    )

    CloseMessageWindow()
    Sleep(150)
    ClearChrFlags(0x13, 0x80)

    #N0088
    NpcTalk(
        0x13,
        "正气凛然的声音",
        (
            "让你们久等了，\x01",
            "是特别任务支援科的诸位吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_23E7():

        label("loc_23E7")

        TurnDirection(0xFE, 0x13, 500)
        Yield()
        Jump("loc_23E7")

    QueueWorkItem2(0x101, 2, lambda_23E7)
    Sleep(50)

    def lambda_23FC():

        label("loc_23FC")

        TurnDirection(0xFE, 0x13, 500)
        Yield()
        Jump("loc_23FC")

    QueueWorkItem2(0x104, 2, lambda_23FC)
    Sleep(100)
    SetChrSubChip(0x109, 0x1)
    Sleep(300)
    Fade(500)
    OP_68(-7500, 6100, 7000, 0)
    MoveCamera(336, 19, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(20500, 0)
    OP_68(1800, 6100, 11300, 5500)
    MoveCamera(321, 19, 0, 5500)

    def lambda_2467():
        OP_95(0xFE, -4300, 5000, 10000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_2467)
    WaitChrThread(0x13, 1)

    def lambda_2485():
        OP_95(0xFE, 1000, 5000, 11000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_2485)
    WaitChrThread(0x13, 1)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x104, 0x2)
    EndChrThread(0x105, 0x2)
    OP_6F(0x79)

    #C0089
    ChrTalk(
        0x101,
        "#00011F啊……\x02",
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x109,
        "#12P#10101F！！\x02",
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x102,
        "#00102F果、果然……\x02",
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0x104,
        (
            "#12P#00305F哦哦，是刚才让大小姐\x01",
            "和诺艾尔激动热议的……\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x13,
        (
            "#07105F#5P……？\x02\x03",

            "#07104F哦，真是失敬了，\x01",
            "我们曾在揭幕式上见过一面吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetCameraDistance(20000, 300)
    Sound(802, 0, 100, 0)
    SetChrChipByIndex(0x13, 0x24)
    SetChrSubChip(0x13, 0x0)
    OP_6F(0x79)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0094
    AnonymousTalk(
        0x13,
        (
            "抱歉，自我介绍做得太迟了。\x01",
            "我是利贝尔王国军·王室亲卫队的\x01",
            "尤莉亚·舒华兹准校。\x02\x03",

            "奉科洛蒂娅殿下的命令，\x01",
            "前来带各位进入\x01",
            "『埃尔赛尤』。\x02\x03",

            "请大家跟我来。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    SetCameraDistance(20500, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x102, 0x4)
    ClearChrFlags(0x104, 0x4)
    ClearChrFlags(0x109, 0x4)
    ClearChrFlags(0x105, 0x4)
    OP_CC(0x1, 0xFF, 0x0)
    Sleep(500)
    SetScenarioFlags(0x22, 1)
    NewScene("t3520", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_21_1DF3 end

    def Function_22_2702(): pass

    label("Function_22_2702")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(6860, 1250, -5300, 0)
    MoveCamera(315, 27, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(36000, 0)
    SetChrPos(0x101, 6000, 0, -4790, 0)
    SetChrPos(0x102, 7200, 0, -4850, 0)
    SetChrPos(0x103, 5430, 0, -5620, 0)
    SetChrPos(0x104, 6910, 0, -5920, 0)
    SetChrPos(0x109, 7600, 0, -6670, 0)
    SetChrPos(0x105, 6280, 0, -6960, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0x11, 0xFF)
    FadeToBright(1000, 0)
    OP_0D()

    #C0095
    ChrTalk(
        0x101,
        (
            "#00000F不好意思，请问您是\x01",
            "卡普亚特急便的职员吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0x11,
        (
            "啊，是的……\x01",
            "你们是？\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0x101,
        (
            "#00000F我们是克洛斯贝尔警察局\x01",
            "特别任务支援科的成员。\x02\x03",

            "前来向您确认\x01",
            "委托的情况。\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x11,
        "哦哦，是你们啊！\x02",
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0x11,
        (
            "哎呀呀，太感谢了。\x01",
            "我正发愁，不知该怎么办才好呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0x11,
        (
            "这件委托也许会比较耗时间，\x01",
            "你们可以接受吗？\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 24)
    OP_4C(0x11, 0xFF)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 6600, 0, -5000, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_22_2702 end

    def Function_23_291C(): pass

    label("Function_23_291C")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(6860, 1250, -5300, 0)
    MoveCamera(315, 27, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(36000, 0)
    SetChrPos(0x101, 6000, 0, -4790, 0)
    SetChrPos(0x102, 7200, 0, -4850, 0)
    SetChrPos(0x103, 5430, 0, -5620, 0)
    SetChrPos(0x104, 6910, 0, -5920, 0)
    SetChrPos(0x109, 7600, 0, -6670, 0)
    SetChrPos(0x105, 6280, 0, -6960, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0x11, 0xFF)
    FadeToBright(1000, 0)
    OP_0D()

    #C0101
    ChrTalk(
        0x11,
        (
            "哦，莫非现在\x01",
            "已经有空了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x11,
        (
            "这件委托也许会比较耗时间，\x01",
            "你们可以接受吗？\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 24)
    OP_4C(0x11, 0xFF)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 6600, 0, -5000, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_23_291C end

    def Function_24_2A64(): pass

    label("Function_24_2A64")

    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【接受】\x01",      # 0
            "【放弃】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2AC6"),
        (1, "loc_2ACE"),
        (SWITCH_DEFAULT, "loc_2B4F"),
    )


    label("loc_2AC6")

    Call(0, 25)
    Jump("loc_2B4F")

    label("loc_2ACE")


    #C0103
    ChrTalk(
        0x101,
        (
            "#00006F抱歉，我们现在\x01",
            "实在是没空……\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0x11,
        (
            "啊，这样啊？\x01",
            "真没办法……\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0x11,
        (
            "那就等你们有空之后\x01",
            "再来找我吧！\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x175, 4)
    Jump("loc_2B4F")

    label("loc_2B4F")

    Return()

    # Function_24_2A64 end

    def Function_25_2B50(): pass

    label("Function_25_2B50")


    #C0106
    ChrTalk(
        0x101,
        "#00000F嗯，没问题。\x02",
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0x104,
        (
            "#00300F好像是发错了\x01",
            "什么货物吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0x11,
        "嗯，是的。\x02",
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0x11,
        (
            "我们飞行于整个大陆，\x01",
            "将邮寄的货物发送到\x01",
            "各个地区……\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0x11,
        (
            "但这次却把\x01",
            "货物送错了。\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0x11,
        (
            "因为搞乱了送货单，\x01",
            "导致好几件货物\x01",
            "被送到了错误的地址。\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0x102,
        "#00105F呼……那可真是很麻烦呢。\x02",
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0x103,
        (
            "#00206F搞错送货单这种事情\x01",
            "实在少见……\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0x11,
        (
            "不不，我们的经理\x01",
            "是个非常粗枝大叶的人。\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0x11,
        (
            "以前也曾多次\x01",
            "出现过这样的事。\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0x11,
        (
            "在最夸张的时候，\x01",
            "甚至还会把朋友寄给他的信\x01",
            "当成送货单，贴在包裹上……\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0x109,
        (
            "#10109F啊哈哈……\x01",
            "真是个很粗心\x01",
            "的人呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0x11,
        (
            "嗯，不过也是个很值得尊敬的人。\x01",
            "是他收留了\x01",
            "无家可归的我们……\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0x11,
        (
            "……咳咳，抱歉，\x01",
            "把话扯远了。\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0x11,
        (
            "简要来说，就是想委托你们\x01",
            "将送错的货物重新配送。\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0x11,
        (
            "我们把货物运到自治州之后，\x01",
            "就会交给本地的运送公司了，\x01",
            "所以对这里的格局不是很熟。\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0x105,
        (
            "#10304F原来如此，\x01",
            "我明白了。\x02\x03",

            "#10302F误发货物如今所在的场所，\x01",
            "你们已经有所掌握了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0x11,
        (
            "嗯，之前已经\x01",
            "核实过了……\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0x11,
        (
            "应该发到乌尔斯拉医院的货物，\x01",
            "现在已经发到了玛因兹的『红砖亭』。\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0x11,
        (
            "而误发到乌尔斯拉医院的\x01",
            "那件货物，本应发送到市内\x01",
            "住宅街的某处民宅。\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0x11,
        (
            "请你们去这些地方收回\x01",
            "发错的货物，并重新配发到\x01",
            "正确的收货地址。\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0x11,
        (
            "……情况就是这样，\x01",
            "请把这个拿去吧。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0128
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '易碎品的小包裹'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('易碎品的小包裹', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0129
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '发往住宅街的送货单'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('发往住宅街的送货单', 1)
    SetMessageWindowPos(14, 280, 60, 3)

    #C0130
    ChrTalk(
        0x101,
        (
            "#00000F这就是应该\x01",
            "送到『红砖亭』\x01",
            "的货物吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0x103,
        (
            "#00200F这张送货单，本来应该贴在\x01",
            "发往医院的那件货物上？\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0x11,
        "嗯，正是。\x02",
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0x11,
        (
            "你们先把这件\x01",
            "货物送到\x01",
            "『红砖亭』吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0x11,
        (
            "然后再把应该送到\x01",
            "乌尔斯拉医院的货物\x01",
            "取回去，接下来……\x02",
        )
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0x11,
        (
            "……唔，说着说着，\x01",
            "连我自己都搞不清楚了。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0136
    ChrTalk(
        0x101,
        (
            "#00003F总、总之……\x01",
            "我们只要按顺序\x01",
            "去交换货物就行了。\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0x11,
        "嗯，没错。\x02",
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0x11,
        (
            "这件委托确实很麻烦，\x01",
            "不好意思，拜托你们了。\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0x101,
        (
            "#00004F好，明白了。\x02\x03",

            "#00000F……那我们就\x01",
            "赶快去玛因兹的\x01",
            "『红砖亭』吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0x104,
        (
            "#00306F哎呀呀，\x01",
            "好像会很累人啊。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    Sound(80, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0141
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "任务【重发误送包裹】\x07\x00",
            "开始！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x175, 5)
    OP_29(0x85, 0x1, 0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_4C(0x11, 0xFF)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 6600, 0, -5000, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_25_2B50 end

    def Function_26_3367(): pass

    label("Function_26_3367")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(6860, 2500, -5300, 0)
    MoveCamera(315, 27, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(36000, 0)
    SetChrPos(0x101, 6000, 0, -4790, 0)
    SetChrPos(0x102, 7200, 0, -4850, 0)
    SetChrPos(0x103, 5430, 0, -5620, 0)
    SetChrPos(0x104, 6910, 0, -5920, 0)
    SetChrPos(0x109, 7600, 0, -6670, 0)
    SetChrPos(0x105, 6280, 0, -6960, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0x11, 0xFF)
    OP_68(6860, 1250, -5300, 3000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x1)

    #C0142
    ChrTalk(
        0x11,
        (
            "哦，你们已经把货物\x01",
            "送到正确的地址了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0x11,
        (
            "嘿，真是帮大忙啦。\x01",
            "非常感谢你们，支援科的各位。\x02",
        )
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0x101,
        "#00000F不用客气。\x02",
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0x11,
        "话说回来……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x11, 0x102, 500)
    Sleep(300)

    #C0146
    ChrTalk(
        0x11,
        (
            "这位小姐的脸色\x01",
            "好像很不好啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0x102,
        (
            "#00106F#1S（全身发抖）……\x01",
            "我竟然和幽灵说了话……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0148
    ChrTalk(
        0x105,
        "#10309F呵呵，好像受了很强烈的刺激呢。\x02",
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0x109,
        "#10106F我能理解她的心情……\x02",
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0x104,
        "#00300F算啦，过一阵子就会恢复了。\x02",
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0x101,
        (
            "#00012F嗯，那个……\x01",
            "情况就是这样，\x01",
            "请不必在意。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x11, 0xB4, 0x1F4)
    Sleep(300)

    #C0152
    ChrTalk(
        0x11,
        (
            "是吗？\x01",
            "也罢……\x02",
        )
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0x11,
        (
            "那我这就\x01",
            "告辞啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0x11,
        (
            "如果以后再遇到什么事情，\x01",
            "还请各位多帮忙哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0x101,
        "#00000F嗯，没问题。\x02",
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0x103,
        "#00200F随时欢迎。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_3743")
    TurnDirection(0x101, 0x104, 500)
    Sleep(300)

    #C0157
    ChrTalk(
        0x101,
        (
            "#00000F……好，接下来，\x01",
            "我们赶快去西克洛斯贝尔街道\x01",
            "的脱轨事故现场吧！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3743")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_57(0x0)
    OP_5A()
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0158
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "任务【重发误送包裹】\x07\x00",
            "完成！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_29(0x85, 0x1, 0x5)
    OP_29(0x85, 0x1, 0x6)
    OP_29(0x85, 0x4, 0x10)
    SubItemNumber('发往住宅街的送货单', 1)
    OP_4C(0x11, 0xFF)
    ClearMapFlags(0x10000000)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_37DD")
    EventEnd(0x5)
    NewScene("c0000", 103, 0, 0)
    IdleLoop()
    Jump("loc_37F4")

    label("loc_37DD")

    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 6600, 0, -5000, 0)
    EventEnd(0x5)

    label("loc_37F4")

    Return()

    # Function_26_3367 end

    def Function_27_37F5(): pass

    label("Function_27_37F5")

    EventBegin(0x0)
    Fade(500)
    OP_68(5810, 1250, 4500, 0)
    MoveCamera(315, 27, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(32500, 0)
    SetChrPos(0x101, 5480, 0, 4000, 0)
    SetChrPos(0x102, 6680, 0, 4000, 0)
    SetChrPos(0x104, 5480, 0, 2800, 0)
    SetChrPos(0x103, 6580, 0, 2800, 0)
    SetChrPos(0x105, 5480, 0, 1600, 0)
    SetChrPos(0x109, 6680, 0, 1600, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0x12, 0xFF)
    OP_4B(0xA, 0xFF)
    OP_0D()

    #C0159
    ChrTalk(
        0x12,
        "呼，到底该怎么办才好……\x02",
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0xA,
        (
            "要是我当时再稍微谨慎些，\x01",
            "就不会发生这种事了……\x02",
        )
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0x101,
        (
            "#00005F那个……\x01",
            "请问发生什么事了？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x12, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_3954():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_3954)
    Sleep(10)

    def lambda_3964():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_3964)
    WaitChrThread(0xA, 2)
    Sleep(500)

    #C0162
    ChrTalk(
        0x12,
        (
            "哦哦，你们是特别任务支援科的……\x01",
            "我们遇到了一件大麻烦呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0x12,
        (
            "我今天原本要把从雷米菲利亚\x01",
            "发来的医疗物资送到\x01",
            "乌尔斯拉医院……\x02",
        )
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0x12,
        (
            "但有个身份不明的家伙\x01",
            "却把医疗物资给骗走了。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0165
    ChrTalk(
        0x102,
        "#00105F把医疗物资骗走了……！？\x02",
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0xA,
        (
            "嗯……就在刚才，\x01",
            "有个自称运输公司职员\x01",
            "的男人来找我。\x02",
        )
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0xA,
        (
            "他说『莱姆斯运输公司的人来不了了，\x01",
            "我来代替他们运送物资』……\x01",
            "理由编得真是像模像样。\x02",
        )
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0xA,
        (
            "我看他完全不像是骗人的，\x01",
            "于是二话没说，马上就把\x01",
            "货物交给他了。\x02",
        )
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0x12,
        (
            "可是我们公司根本就没有\x01",
            "发出过那样的委托书。\x02",
        )
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0x12,
        (
            "我们两个谈了一阵之后，\x01",
            "才意识到货物是被骗走了。\x02",
        )
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0x103,
        (
            "#00203F嗯……也就是说，\x01",
            "那封委托书是伪造的啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0x105,
        (
            "#10301F话说回来，在这种非常时期，\x01",
            "竟然还要骗取医疗物资，\x01",
            "真是个相当恶劣的家伙啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0x109,
        (
            "#10108F那起袭击事件使\x01",
            "很多受害者负伤住院……\x02",
        )
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0x104,
        (
            "#00303F如果在暗地里将\x01",
            "那些医疗物资销售出去，\x01",
            "自然能赚到不少钱呢。\x02\x03",

            "#00301F也就是说，犯人是个为了\x01",
            "赚钱而趁火打劫的奸诈之人。\x02",
        )
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0x102,
        "#00101F好、好过分……\x02",
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0x12,
        "真是伤脑筋啊……\x02",
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0x12,
        (
            "乌尔斯拉医院的人\x01",
            "现在仍在等待\x01",
            "物资送达呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0xA,
        (
            "唉，这都怪我啊……\x01",
            "至少应该先和莱姆斯\x01",
            "运输公司的人确认一下……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x12, 0xA, 500)

    #C0179
    ChrTalk(
        0x12,
        (
            "不……这并不是你的错。\x01",
            "不管怎么说，错的也都是那个\x01",
            "骗取货物的家伙。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x12, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x12, 0x101, 500)

    #C0180
    ChrTalk(
        0x12,
        (
            "对了……你们几位，\x01",
            "能不能帮忙抓捕那个\x01",
            "骗取医疗物资的犯人呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0x12,
        (
            "为了乌尔斯拉医院中的\x01",
            "各位住院患者，\x01",
            "请你们一定要想办法抓到他啊。\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 29)
    OP_4C(0x12, 0xFF)
    OP_4C(0xA, 0xFF)
    TurnDirection(0x12, 0xA, 0)
    TurnDirection(0xA, 0x12, 0)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 6080, 0, 4000, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_27_37F5 end

    def Function_28_3F40(): pass

    label("Function_28_3F40")

    EventBegin(0x0)
    Fade(500)
    OP_68(5810, 1250, 4500, 0)
    MoveCamera(315, 27, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(32500, 0)
    SetChrPos(0x101, 5480, 0, 4000, 0)
    SetChrPos(0x102, 6680, 0, 4000, 0)
    SetChrPos(0x104, 5480, 0, 2800, 0)
    SetChrPos(0x103, 6580, 0, 2800, 0)
    SetChrPos(0x105, 5480, 0, 1600, 0)
    SetChrPos(0x109, 6680, 0, 1600, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0x12, 0xFF)
    OP_4B(0xA, 0xFF)
    OP_93(0x12, 0xB4, 0x0)
    OP_93(0xA, 0xB4, 0x0)
    OP_0D()

    #C0182
    ChrTalk(
        0x12,
        (
            "你们能否帮忙抓捕那个\x01",
            "骗取医疗物资的犯人呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0x12,
        (
            "为了乌尔斯拉医院中的\x01",
            "各位住院患者，\x01",
            "请你们一定要想办法抓到他啊。\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 29)
    OP_4C(0x12, 0xFF)
    OP_4C(0xA, 0xFF)
    TurnDirection(0x12, 0xA, 0)
    TurnDirection(0xA, 0x12, 0)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 6080, 0, 4000, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_28_3F40 end

    def Function_29_40C2(): pass

    label("Function_29_40C2")

    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "接受\x01",      # 0
            "放弃\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_411C"),
        (1, "loc_4124"),
        (SWITCH_DEFAULT, "loc_41DF"),
    )


    label("loc_411C")

    Call(0, 30)
    Jump("loc_41DF")

    label("loc_4124")


    #C0184
    ChrTalk(
        0x101,
        (
            "#00003F抱歉……\x01",
            "我们现在还有无法推脱的工作在身。\x02",
        )
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0xA,
        (
            "是、是吗……\x01",
            "那就没办法了……\x02",
        )
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0x12,
        (
            "如果你们稍后有空了，\x01",
            "就请再来找我吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0x12,
        (
            "我能拜托的人只有你们了，\x01",
            "请一定要帮忙啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x19B, 6)
    Jump("loc_41DF")

    label("loc_41DF")

    Return()

    # Function_29_40C2 end

    def Function_30_41E0(): pass

    label("Function_30_41E0")


    #C0188
    ChrTalk(
        0x101,
        (
            "#00003F……犯人似乎并没有\x01",
            "离开太久……\x01",
            "如果动作迅速，说不定还来得及。\x02\x03",

            "#00000F这件事情就交给我们吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0xA,
        "哦哦……太感谢了！\x02",
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0x102,
        (
            "#00103F不过，既然犯人已经得手了，\x01",
            "应该会立刻逃走……\x01",
            "我们还是尽快行动为好。\x02\x03",

            "#00101F有没有什么可以推测出\x01",
            "犯人去向的线索呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0191
    ChrTalk(
        0x12,
        (
            "这个嘛……\x01",
            "我毕竟没有亲眼见到犯人，\x01",
            "什么都提供不了。\x02",
        )
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0xA,
        (
            "说起来……\x01",
            "那个男人好像驾驶着莱恩福尔特公司\x01",
            "制造的黑色运输车。\x02",
        )
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0xA,
        (
            "看起来像是个\x01",
            "打扮讲究的帝国人，说不定……\x02",
        )
    )

    CloseMessageWindow()

    #C0194
    ChrTalk(
        0x104,
        (
            "#00301F很有可能驾驶着\x01",
            "运输车，逃往\x01",
            "帝国方向了。\x02",
        )
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0x109,
        (
            "#10103F如果是这样的话，\x01",
            "他现在大概已经抵达\x01",
            "贝尔加德门附近了。\x02\x03",

            "#10101F谨慎起见，我们在追寻途中，\x01",
            "最好也向运输车所经道路上的\x01",
            "人们询问一下……\x02",
        )
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0x105,
        (
            "#10306F嗯，但我们可不能\x01",
            "太过慢条斯理。\x02",
        )
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0x101,
        (
            "#00003F总之……\x01",
            "先追上去再说吧。\x02\x03",

            "#00001F比利先生，请你们二位\x01",
            "在这里等待我们的联络。\x02",
        )
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0x12,
        "嗯，知道了。\x02",
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0xA,
        "拜托啦，各位！\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    Sound(80, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0200
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "任务【寻找医疗物资】\x07\x00",
            "开始！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_29(0x93, 0x4, 0x2)
    OP_29(0x93, 0x1, 0x0)
    Return()

    # Function_30_41E0 end

    SaveToFile()

Try(main)
