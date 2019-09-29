from ScenarioHelper import *

def main():
    CreateScenaFile(
        "c1110.bin",                # FileName
        "c1110",                    # MapName
        "c1110",                    # Location
        0x0017,                     # MapIndex
        "ed7150",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 23, 0, 2, 0, 3],
    )

    BuildStringList((
        "c1110",                  # 0
        "接待小姐希恩",           # 1
        "库利普主任",             # 2
        "运送员",                 # 3
        "贸易商利泽罗",           # 4
        "市民",                   # 5
        "市民",                   # 6
        "市民",                   # 7
        "市民",                   # 8
        "本德",                   # 9
        "库雷优",                 # 10
        "萨妮塔",                 # 11
        "玛丽",                   # 12
        "摩尔斯老人",             # 13
        "洛依",                   # 14
        "阿鲁姆",                 # 15
        "艾娅莉",                 # 16
        "玛格丽特夫人",           # 17
        "库罗玛",                 # 18
        "奥特",                   # 19
    ))

    AddCharChip((
        "chr/ch34600.itc",                   # 00
        "chr/ch28000.itc",                   # 01
        "chr/ch23600.itc",                   # 02
        "chr/ch27800.itc",                   # 03
        "chr/ch21900.itc",                   # 04
        "chr/ch20400.itc",                   # 05
        "chr/ch21300.itc",                   # 06
        "chr/ch20800.itc",                   # 07
        "chr/ch27600.itc",                   # 08
        "chr/ch33300.itc",                   # 09
        "chr/ch34400.itc",                   # 0A
        "chr/ch39000.itc",                   # 0B
        "chr/ch00000.itc",                   # 0C
        "chr/ch21200.itc",                   # 0D
        "chr/ch46300.itc",                   # 0E
        "chr/ch46200.itc",                   # 0F
        "chr/ch44000.itc",                   # 10
        "chr/ch24900.itc",                   # 11
        "chr/ch20800.itc",                   # 12
    ))

    DeclNpc(0,       0,       7400,    180,  261,  0x0, 0,   0,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(3529,    4000,    16209,   315,  261,  0x0, 0,   1,   0,   0,   1,   0,   11,  255,  0)
    DeclNpc(2720,    4000,    17000,   90,   389,  0x0, 0,   2,   0,   0,   0,   0,   14,  255,  0)
    DeclNpc(-4429,   0,       4460,    0,    389,  0x0, 0,   3,   0,   0,   0,   0,   15,  255,  0)
    DeclNpc(-44990,  250,     14710,   180,  389,  0x0, 0,   4,   0,   0,   0,   0,   16,  255,  0)
    DeclNpc(-13510,  4000,    14529,   135,  389,  0x0, 0,   5,   0,   0,   0,   0,   20,  255,  0)
    DeclNpc(-4429,   0,       4460,    180,  389,  0x0, 0,   6,   0,   0,   0,   0,   21,  255,  0)
    DeclNpc(0,       0,       7400,    180,  389,  0x0, 0,   7,   0,   0,   0,   0,   22,  255,  0)
    DeclNpc(389,     0,       4960,    360,  389,  0x0, 0,   8,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(1879,    0,       3369,    90,   389,  0x0, 0,   9,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(3019,    0,       3369,    270,  389,  0x0, 0,   10,  0,   0,   0,   0,   7,   255,  0)
    DeclNpc(3849,    0,       3089,    270,  389,  0x0, 0,   11,  0,   0,   0,   0,   8,   255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   7,   0,   0,   0,   0,   23,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   13,  0,   0,   0,   0,   24,  255,  0)
    DeclNpc(5760,    0,       -2359,   90,   389,  0x0, 0,   14,  0,   0,   0,   0,   25,  255,  0)
    DeclNpc(6760,    0,       -2359,   270,  389,  0x0, 0,   15,  0,   0,   0,   0,   26,  255,  0)
    DeclNpc(-13510,  4000,    14529,   135,  389,  0x0, 0,   16,  0,   0,   0,   0,   19,  255,  0)
    DeclNpc(-2609,   4000,    18750,   180,  389,  0x0, 0,   17,  0,   0,   0,   0,   17,  255,  0)
    DeclNpc(-4380,   4000,    17329,   180,  389,  0x0, 0,   18,  0,   0,   0,   0,   18,  255,  0)

    DeclActor(0,       0,       6000,    1500,    0,       1500,    7460,    0x007E, 0,  4,  0x0000)
    DeclActor(0,       4000,    17600,   1500,    0,       5500,    18450,   0x007C, 0,  38, 0x0000)
    DeclActor(-8100,   4000,    19780,   1500,    -8100,   5500,    19780,   0x007C, 0,  36, 0x0000)
    DeclActor(8000,    4120,    19640,   1500,    8000,    5520,    19640,   0x007C, 0,  37, 0x0000)

    ChipFrameInfo(1060, 0)                                       # 0

    ScpFunction((
        "Function_0_424",          # 00, 0
        "Function_1_4DC",          # 01, 1
        "Function_2_507",          # 02, 2
        "Function_3_7E1",          # 03, 3
        "Function_4_893",          # 04, 4
        "Function_5_897",          # 05, 5
        "Function_6_129F",         # 06, 6
        "Function_7_12FA",         # 07, 7
        "Function_8_133F",         # 08, 8
        "Function_9_1359",         # 09, 9
        "Function_10_136C",        # 0A, 10
        "Function_11_152A",        # 0B, 11
        "Function_12_1F10",        # 0C, 12
        "Function_13_1FA9",        # 0D, 13
        "Function_14_219E",        # 0E, 14
        "Function_15_222C",        # 0F, 15
        "Function_16_22BB",        # 10, 16
        "Function_17_22FC",        # 11, 17
        "Function_18_2328",        # 12, 18
        "Function_19_2389",        # 13, 19
        "Function_20_27A0",        # 14, 20
        "Function_21_2800",        # 15, 21
        "Function_22_2846",        # 16, 22
        "Function_23_288C",        # 17, 23
        "Function_24_2A7D",        # 18, 24
        "Function_25_2C97",        # 19, 25
        "Function_26_2CF7",        # 1A, 26
        "Function_27_2D33",        # 1B, 27
        "Function_28_42D6",        # 1C, 28
        "Function_29_47D8",        # 1D, 29
        "Function_30_4D61",        # 1E, 30
        "Function_31_4E37",        # 1F, 31
        "Function_32_570C",        # 20, 32
        "Function_33_5A80",        # 21, 33
        "Function_34_5B64",        # 22, 34
        "Function_35_5D41",        # 23, 35
        "Function_36_6699",        # 24, 36
        "Function_37_6719",        # 25, 37
        "Function_38_67A9",        # 26, 38
        "Function_39_6966",        # 27, 39
    ))


    def Function_0_424(): pass

    label("Function_0_424")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_464"),
        (1, "loc_470"),
        (2, "loc_47C"),
        (3, "loc_488"),
        (4, "loc_494"),
        (5, "loc_4A0"),
        (6, "loc_4AC"),
        (SWITCH_DEFAULT, "loc_4B8"),
    )


    label("loc_464")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_4C4")

    label("loc_470")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_4C4")

    label("loc_47C")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_4C4")

    label("loc_488")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_4C4")

    label("loc_494")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_4C4")

    label("loc_4A0")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_4C4")

    label("loc_4AC")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_4C4")

    label("loc_4B8")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_4C4")

    label("loc_4C4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4DB")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_4C4")

    label("loc_4DB")

    Return()

    # Function_0_424 end

    def Function_1_4DC(): pass

    label("Function_1_4DC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_506")
    OP_94(0xFE, 0x193C, 0x3B1A, 0x672, 0x41BE, 0x3E8)
    Sleep(300)
    Jump("Function_1_4DC")

    label("loc_506")

    Return()

    # Function_1_4DC end

    def Function_2_507(): pass

    label("Function_2_507")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_515")
    Jump("loc_77C")

    label("loc_515")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_549")
    ClearChrFlags(0x18, 0x80)
    SetChrPos(0x9, 1120, 0, 5240, 315)
    BeginChrThread(0x9, 0, 0, 0)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    Jump("loc_77C")

    label("loc_549")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_557")
    Jump("loc_77C")

    label("loc_557")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_591")
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x14, 1000, 0, 5100, 90)
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x15, 2500, 0, 5100, 270)
    Jump("loc_77C")

    label("loc_591")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_5B3")
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    SetChrFlags(0x16, 0x10)
    SetChrFlags(0x17, 0x10)
    Jump("loc_77C")

    label("loc_5B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_5C1")
    Jump("loc_77C")

    label("loc_5C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_5F5")
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 390, 0, 5090, 360)
    BeginChrThread(0xF, 0, 0, 0)
    SetChrFlags(0xF, 0x10)
    SetChrFlags(0x8, 0x10)
    Jump("loc_77C")

    label("loc_5F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_603")
    Jump("loc_77C")

    label("loc_603")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_611")
    Jump("loc_77C")

    label("loc_611")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_66C")
    SetChrPos(0x9, 1880, 0, 5490, 180)
    BeginChrThread(0x9, 0, 0, 0)
    SetChrPos(0xD, 670, 0, 3710, 360)
    SetChrPos(0xE, -180, 0, 3700, 360)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0x9, 0x10)
    SetChrFlags(0x8, 0x10)
    Jump("loc_77C")

    label("loc_66C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_67A")
    Jump("loc_77C")

    label("loc_67A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_6BF")
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 2380, 4000, 15840, 90)
    SetChrPos(0x9, 3790, 4000, 15840, 270)
    BeginChrThread(0x9, 0, 0, 0)
    SetChrFlags(0xC, 0x10)
    SetChrFlags(0x9, 0x10)
    Jump("loc_77C")

    label("loc_6BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_70E")
    SetChrPos(0xB, 2380, 4000, 15840, 90)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0x9, 3790, 4000, 15840, 270)
    BeginChrThread(0x9, 0, 0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12E, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_709")
    SetChrFlags(0xB, 0x10)
    SetChrFlags(0x9, 0x10)

    label("loc_709")

    Jump("loc_77C")

    label("loc_70E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_77C")
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 2380, 4000, 15840, 90)
    BeginChrThread(0xA, 0, 0, 0)
    SetChrPos(0x9, 3790, 4000, 15840, 270)
    BeginChrThread(0x9, 0, 0, 0)
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0x9, 0x10)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x10)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x10)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x12, 0x10)
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x8, 0x10)

    label("loc_77C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_790")
    ClearScenarioFlags(0x22, 1)
    Event(0, 35)
    Jump("loc_7E0")

    label("loc_790")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 2)), scpexpr(EXPR_END)), "loc_7E0")
    ClearScenarioFlags(0x22, 2)
    SetChrPos(0x0, -13650, 4000, 12700, 45)
    SetChrPos(0x1, -13650, 4000, 12700, 45)
    SetChrPos(0x2, -13650, 4000, 12700, 45)
    SetChrPos(0x3, -13650, 4000, 12700, 45)

    label("loc_7E0")

    Return()

    # Function_2_507 end

    def Function_3_7E1(): pass

    label("Function_3_7E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7FA")
    OP_10(0x0, 0x0)
    OP_10(0x6, 0x1)
    Jump("loc_800")

    label("loc_7FA")

    OP_10(0x0, 0x1)
    OP_10(0x6, 0x0)

    label("loc_800")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_830")
    SetMapObjFrame(0xFF, "light01", 0x0, 0x1)
    Sound(128, 1, 50, 0)

    label("loc_830")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_856")
    OP_7D(0xD2, 0xD2, 0xE6, 0x0, 0x0)
    SetMapObjFrame(0xFF, "light01", 0x0, 0x1)

    label("loc_856")

    ClearMapObjFlags(0x1, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_870")
    SetMapObjFlags(0x3, 0x4)

    label("loc_870")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_892")
    SetMapObjFlags(0x3, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17B, 6)), scpexpr(EXPR_END)), "loc_892")
    OP_1B(0x2, 0x0, 0x27)

    label("loc_892")

    Return()

    # Function_3_7E1 end

    def Function_4_893(): pass

    label("Function_4_893")

    Call(0, 5)
    Return()

    # Function_4_893 end

    def Function_5_897(): pass

    label("Function_5_897")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6A, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6A, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6A, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8DF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x131, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x131, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8D1")
    Call(0, 28)
    Return()

    label("loc_8D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x131, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8DF")
    Call(0, 27)
    Return()

    label("loc_8DF")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_A56")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9CB")

    #C0001
    ChrTalk(
        0x8,
        (
            "我们这些职员分头行动，\x01",
            "确认了市民们在那场\x01",
            "戒严令骚动中的安危状况……\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x8,
        (
            "除了被卷入骚乱而身负\x01",
            "轻伤的十几名市民之外，\x01",
            "没有其他人受害。\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0x8,
        (
            "已经给需要治疗的人\x01",
            "安排好了急救车……\x01",
            "这样就可以暂时放心了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_A51")

    label("loc_9CB")


    #C0004
    ChrTalk(
        0x8,
        (
            "在戒严令骚乱中，\x01",
            "除了受轻伤的十几名市民之外，\x01",
            "没有其他人受害。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x8,
        (
            "已经给需要治疗的人\x01",
            "安排好了急救车……\x01",
            "这样就可以暂时放心了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A51")

    Jump("loc_129B")

    label("loc_A56")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_B35")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AD6")

    #C0006
    ChrTalk(
        0x8,
        (
            "市民会馆现在已经\x01",
            "做好了准备，接纳\x01",
            "无法回家的市民们。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x8,
        (
            "如果遇到了什么困难，\x01",
            "请尽管和我们说。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_B30")

    label("loc_AD6")


    #C0008
    ChrTalk(
        0x8,
        (
            "市民会馆内储备了\x01",
            "食品和毛毯等应急用物资。\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x8,
        (
            "如果遇到了什么困难，\x01",
            "请尽管和我们说。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B30")

    Jump("loc_129B")

    label("loc_B35")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_B8F")

    #C0010
    ChrTalk(
        0x8,
        (
            "在这里都能清楚地听到\x01",
            "高呼万岁的声音。\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x8,
        (
            "为什么会感到\x01",
            "有点可怕呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_129B")

    label("loc_B8F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_BE6")

    #C0012
    ChrTalk(
        0x8,
        (
            "感谢您光临\x01",
            "今日的慈善宴会。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x8,
        (
            "如果有\x01",
            "想参加的活动，\x01",
            "请尽管咨询。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_129B")

    label("loc_BE6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_CEC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CAE")

    #C0014
    ChrTalk(
        0x8,
        (
            "有许多市民前来询问\x01",
            "那个袭击玛因兹的\x01",
            "武装集团……\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x8,
        (
            "但关于犯人身份和目的，\x01",
            "我也回答不出来，\x01",
            "真是非常困扰啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x8,
        (
            "虽然有很多人说是帝国干的……\x01",
            "但真相究竟是怎样的呢？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_CE7")

    label("loc_CAE")


    #C0017
    ChrTalk(
        0x8,
        (
            "虽然有很多人说是帝国干的……\x01",
            "但真相究竟是怎样的呢？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CE7")

    Jump("loc_129B")

    label("loc_CEC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_D6D")

    #C0018
    ChrTalk(
        0x8,
        (
            "左手边的多功能大厅中，\x01",
            "正在举办以独立为主题的\x01",
            "市民座谈会。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x8,
        (
            "任何人都可以旁听，\x01",
            "如果有兴趣，不妨去听一下。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_129B")

    label("loc_D6D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_DC7")

    #C0020
    ChrTalk(
        0x8,
        (
            "不好意思，\x01",
            "已经没有空座位了。\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x8,
        (
            "但在座谈会当天也\x01",
            "可以直接入内旁听。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_129B")

    label("loc_DC7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_E30")

    #C0022
    ChrTalk(
        0x8,
        (
            "欢迎来到\x01",
            "克洛斯贝尔市民会馆。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x8,
        (
            "如果想租用市民会馆，\x01",
            "请先填好接待处旁边的\x01",
            "申请表。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_129B")

    label("loc_E30")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_FAA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F1B")

    #C0024
    ChrTalk(
        0x8,
        (
            "自从提出独立提案之后，\x01",
            "希望在这里召开学习会的\x01",
            "申请增加了不少。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x8,
        (
            "为了回应这种呼声，\x01",
            "市政府和通讯社将于后天\x01",
            "联合举办市民座谈会。\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x8,
        (
            "现在还在进行各种准备，\x01",
            "相信这一定会是一场\x01",
            "对大家都有意义的座谈会。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_FA5")

    label("loc_F1B")


    #C0027
    ChrTalk(
        0x8,
        (
            "后天将在本市民会馆举办\x01",
            "以克洛斯贝尔独立为主题的\x01",
            "市民座谈会。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x8,
        (
            "现在还在进行各种准备，\x01",
            "相信这一定会是一场\x01",
            "对大家都有意义的座谈会。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FA5")

    Jump("loc_129B")

    label("loc_FAA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1022")

    #C0029
    ChrTalk(
        0x8,
        (
            "非、非常抱歉。\x01",
            "之前已经张贴过\x01",
            "告示了……\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x8,
        (
            "从保障安全的角度来说，\x01",
            "无论如何也不能让\x01",
            "普通民众进去。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_129B")

    label("loc_1022")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_110B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10B6")

    #C0031
    ChrTalk(
        0x8,
        (
            "各国首脑终于\x01",
            "到达克洛斯贝尔了。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x8,
        (
            "听说从下午开始，\x01",
            "他们就会自由行动……\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x8,
        (
            "不知各位首脑\x01",
            "将会怎样度过那段时间。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1106")

    label("loc_10B6")


    #C0034
    ChrTalk(
        0x8,
        (
            "听说首脑们从下午开始\x01",
            "就会自由行动……\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x8,
        (
            "不知他们\x01",
            "将会怎样度过那段时间。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1106")

    Jump("loc_129B")

    label("loc_110B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_11A4")

    #C0036
    ChrTalk(
        0x8,
        (
            "在通商会议期间，\x01",
            "以及其召开前后的一段时间内，\x01",
            "市民会馆将暂时停止对外开放。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x8,
        (
            "因为这里离兰花塔很近，\x01",
            "如果发生什么事，可就不得了了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_129B")

    label("loc_11A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_128F")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6A, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_120E")

    #C0038
    ChrTalk(
        0x8,
        (
            "各位，非常感谢你们\x01",
            "今天的调查。\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x8,
        (
            "今后也请多多关照\x01",
            "克洛斯贝尔市民会馆。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_128A")

    label("loc_120E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6A, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_128A")

    #C0040
    ChrTalk(
        0x8,
        (
            "麻烦各位调查的是\x01",
            "共计三处的可疑住户，\x01",
            "以及消息不明的前住户。\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x8,
        (
            "全部确认完毕之后，\x01",
            "请再来这里报告。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_128A")

    label("loc_128A")

    Jump("loc_129B")

    label("loc_128F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_129B")
    Call(0, 10)

    label("loc_129B")

    TalkEnd(0x8)
    Return()

    # Function_5_897 end

    def Function_6_129F(): pass

    label("Function_6_129F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_12F6")

    #C0042
    ChrTalk(
        0xFE,
        (
            "希望能找到\x01",
            "好房子啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0xFE,
        (
            "如果可以，\x01",
            "希望能找个盛开着\x01",
            "鲜花的地方……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12F6")

    TalkEnd(0xFE)
    Return()

    # Function_6_129F end

    def Function_7_12FA(): pass

    label("Function_7_12FA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_133B")

    #C0044
    ChrTalk(
        0xFE,
        "没问题的，妈妈。\x02",
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0xFE,
        (
            "爸爸一定能找到\x01",
            "好房子的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_133B")

    TalkEnd(0xFE)
    Return()

    # Function_7_12FA end

    def Function_8_133F(): pass

    label("Function_8_133F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_1355")

    #C0046
    ChrTalk(
        0xFE,
        "喵。\x02",
    )

    CloseMessageWindow()

    label("loc_1355")

    TalkEnd(0xFE)
    Return()

    # Function_8_133F end

    def Function_9_1359(): pass

    label("Function_9_1359")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_1368")
    Call(0, 10)

    label("loc_1368")

    TalkEnd(0xFE)
    Return()

    # Function_9_1359 end

    def Function_10_136C(): pass

    label("Function_10_136C")

    OP_4B(0x10, 0xFF)
    OP_4B(0x8, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1488")

    #C0047
    ChrTalk(
        0x10,
        (
            "嗯，希望尽量找个\x01",
            "便宜些的房子……\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x10,
        (
            "稍微小一些也没有关系，\x01",
            "只要能住下一家三口就行了……\x01",
            "有没有这样的房子呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x8,
        (
            "这个啊……\x01",
            "这里有份资料，\x01",
            "您可以确认一下。\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x8,
        (
            "这所房屋的原住户\x01",
            "好像在几个月之前\x01",
            "办理了迁居手续。\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x10,
        (
            "唔，有这样的房子啊。\x01",
            "我看看……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1521")

    label("loc_1488")


    #C0052
    ChrTalk(
        0x10,
        (
            "啊，对了……\x01",
            "我们还有个基本要求，\x01",
            "那就是允许养宠物。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x8,
        (
            "嗯，我记得这里\x01",
            "是没问题的。\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x10,
        (
            "哦哦，那太好了！\x01",
            "既然如此，\x01",
            "我想立刻确认一下房子状况……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1521")

    OP_4C(0x10, 0xFF)
    OP_4C(0x8, 0xFF)
    Return()

    # Function_10_136C end

    def Function_11_152A(): pass

    label("Function_11_152A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1683")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1604")

    #C0055
    ChrTalk(
        0xFE,
        (
            "我们打算就此次事件\x01",
            "向市民们做个正式说明，\x01",
            "现在正在进行相关准备。\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0xFE,
        (
            "关于今后可能发生的事态，\x01",
            "克洛斯贝尔的市民们\x01",
            "急需一个说明。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0xFE,
        (
            "各地情况也都很混乱，\x01",
            "我们必须尽快准备好\x01",
            "才行啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_167E")

    label("loc_1604")


    #C0058
    ChrTalk(
        0xFE,
        (
            "我们打算就此次事件\x01",
            "向市民们做个正式说明，\x01",
            "现在正在进行相关准备。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0xFE,
        (
            "各地情况都很混乱，\x01",
            "我们必须尽快准备好\x01",
            "才行啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_167E")

    Jump("loc_1F0C")

    label("loc_1683")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_17E7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1764")

    #C0060
    ChrTalk(
        0xFE,
        (
            "关于这次的事件，\x01",
            "总统仅仅下达了一个『戒严令』，\x01",
            "其它情况只字未提。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0xFE,
        (
            "事态竟然会发展成这样……\x01",
            "一定有许多民众\x01",
            "措手不及。\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0xFE,
        (
            "……我们现在也只能等待\x01",
            "事态平息下来，然后再去\x01",
            "确认市民们的安全。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_17E2")

    label("loc_1764")


    #C0063
    ChrTalk(
        0xFE,
        (
            "事态竟然会发展成这样……\x01",
            "一定有许多民众\x01",
            "措手不及。\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0xFE,
        (
            "……我们现在也只能等待\x01",
            "事态平息下来，然后再去\x01",
            "确认市民们的安全。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17E2")

    Jump("loc_1F0C")

    label("loc_17E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_18D4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_187E")

    #C0065
    ChrTalk(
        0xFE,
        (
            "克洛斯贝尔独立国，\x01",
            "以及总统就任吗……\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0xFE,
        (
            "如此一来，体制也一定会\x01",
            "发生变化吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0xFE,
        "从今天开始，每一天都会相当紧张了。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_18CF")

    label("loc_187E")


    #C0068
    ChrTalk(
        0xFE,
        (
            "如此一来，体制也一定会\x01",
            "发生变化吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0xFE,
        "从今天开始，每一天都会相当紧张了。\x02",
    )

    CloseMessageWindow()

    label("loc_18CF")

    Jump("loc_1F0C")

    label("loc_18D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_191A")

    #C0070
    ChrTalk(
        0xFE,
        (
            "欢迎欢迎，希望大家\x01",
            "在今天的慈善宴会中\x01",
            "玩得开心哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F0C")

    label("loc_191A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_1A67")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A06")

    #C0071
    ChrTalk(
        0xFE,
        (
            "市政厅只传达给我们说\x01",
            "『当前正在竭尽全力\x01",
            "解决事态』……\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0xFE,
        (
            "但不明不白的事情实在太多，\x01",
            "真令人不安啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0xFE,
        (
            "唔，但我们这些市政职员\x01",
            "要是表现出不安的话，\x01",
            "各位市民恐怕会更加不安的。\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0xFE,
        "必须要努力调整情绪。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1A62")

    label("loc_1A06")


    #C0075
    ChrTalk(
        0xFE,
        (
            "如果我们这些市政职员\x01",
            "表现出不安，各位市民\x01",
            "恐怕会更加不安的。\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0xFE,
        "必须要努力调整情绪。\x02",
    )

    CloseMessageWindow()

    label("loc_1A62")

    Jump("loc_1F0C")

    label("loc_1A67")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1ABB")

    #C0077
    ChrTalk(
        0xFE,
        (
            "市民座谈会\x01",
            "正在顺利进行中。\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0xFE,
        (
            "希望能平稳结束，\x01",
            "不要引起骚乱。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F0C")

    label("loc_1ABB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_1AF0")

    #C0079
    ChrTalk(
        0xFE,
        (
            "唔，真想尽快熟练掌握\x01",
            "键盘操作啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F0C")

    label("loc_1AF0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1C08")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1BA0")

    #C0080
    ChrTalk(
        0xFE,
        (
            "总务二科最近\x01",
            "也逐渐开始使用\x01",
            "导力邮件了……\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0xFE,
        (
            "但人一上了年纪，\x01",
            "学习新事物\x01",
            "就会很费力。\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0xFE,
        (
            "特别是那个叫做键盘的输入装置，\x01",
            "实在是太难掌握了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1C03")

    label("loc_1BA0")


    #C0083
    ChrTalk(
        0xFE,
        (
            "另外，看屏幕久了，\x01",
            "眼睛总是会累。\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0xFE,
        (
            "还是纸质媒体更好啊……\x01",
            "不过，说这种话\x01",
            "就会落后于人了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C03")

    Jump("loc_1F0C")

    label("loc_1C08")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1C91")

    #C0085
    ChrTalk(
        0xFE,
        (
            "自从这里改为市民会馆之后，\x01",
            "工作好像比以前忙了一倍。\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0xFE,
        (
            "市民座谈会结束后，\x01",
            "还要准备居民投票……\x01",
            "最近真是大事不断啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F0C")

    label("loc_1C91")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1CD2")

    #C0087
    ChrTalk(
        0xFE,
        (
            "嗯，正如她所说，\x01",
            "安保方面的问题是第一位的……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F0C")

    label("loc_1CD2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1D51")

    #C0088
    ChrTalk(
        0xFE,
        (
            "我在窗口看到了\x01",
            "揭幕式的盛况。\x01",
            "哎呀，真是非常壮观。\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0xFE,
        (
            "市政厅正式搬到了新的场所，\x01",
            "如今才产生了这种实感呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F0C")

    label("loc_1D51")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1DBE")

    #C0090
    ChrTalk(
        0xFE,
        (
            "嗯，办理居民登记手续不用特意去市政厅，\x01",
            "在这里也可以办理。\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0xFE,
        "请您到一层的接待处登记吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1F0C")

    label("loc_1DBE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_1E75")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12E, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1DDE")
    Call(0, 13)
    ClearChrFlags(0x9, 0x10)
    Jump("loc_1E70")

    label("loc_1DDE")


    #C0092
    ChrTalk(
        0xFE,
        (
            "当天取消预约的理由\x01",
            "大多都是因为下雨，\x01",
            "也难怪利泽罗先生会生气。\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0xFE,
        (
            "唔，要是事先收取押金，\x01",
            "临时取消预定便不退回费用，\x01",
            "或许就不会变成这样了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E70")

    Jump("loc_1F0C")

    label("loc_1E75")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_1F0C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E98")
    Call(0, 12)
    SetScenarioFlags(0x0, 1)
    ClearChrFlags(0x9, 0x10)
    Jump("loc_1F0C")

    label("loc_1E98")


    #C0094
    ChrTalk(
        0xFE,
        (
            "呼，竟然把搬迁工作的\x01",
            "事务全部交给总务二科\x01",
            "来处理了。\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0xFE,
        (
            "我觉得这种事情\x01",
            "应该各自处理才对……\x01",
            "（嘀嘀咕咕）……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F0C")

    TalkEnd(0xFE)
    Return()

    # Function_11_152A end

    def Function_12_1F10(): pass

    label("Function_12_1F10")

    OP_4B(0xA, 0xFF)
    OP_4B(0x9, 0xFF)

    #C0096
    ChrTalk(
        0xA,
        (
            "嗯，请您确认一下\x01",
            "送货单好吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0x9,
        "啊，嗯，我看看……\x02",
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x9,
        (
            "嗯，没有错。\x01",
            "那就麻烦你们送货了。\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0xA,
        "嗯，请您放心吧。\x02",
    )

    CloseMessageWindow()
    OP_4C(0xA, 0xFF)
    OP_4C(0x9, 0xFF)
    ClearChrFlags(0x9, 0x10)
    ClearChrFlags(0xA, 0x10)
    SetScenarioFlags(0x0, 1)
    SetScenarioFlags(0x0, 2)
    Return()

    # Function_12_1F10 end

    def Function_13_1FA9(): pass

    label("Function_13_1FA9")

    OP_4B(0xB, 0xFF)
    OP_4B(0x9, 0xFF)

    #C0100
    ChrTalk(
        0x9,
        (
            "差不多快到\x01",
            "研讨会的开始时间了……\x01",
            "需要稍微推迟一些吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0xB,
        (
            "当、当然了，\x01",
            "连一半的人都没坐满，\x01",
            "现在开始也没有意义啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0xB,
        (
            "竟然在当天取消预定……\x01",
            "这些外行人真是让人受不了。\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0xB,
        (
            "以为凭这种不负责任的态度\x01",
            "还能抓住商机，那就大错特错了。\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0x9,
        "是、是……\x02",
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0xB,
        (
            "总、总之，\x01",
            "再等一会吧。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x134, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2188")

    #C0106
    ChrTalk(
        0x102,
        (
            "#00105F（罗伊德，\x01",
            "  这个人莫非是……）\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0x101,
        (
            "#00003F（嗯，是在教团事件中\x01",
            "  服用过『真知』的受害者之一。）\x02\x03",

            "#00000F（他好像遇到了什么麻烦事，\x01",
            "  不过精神似乎还不错，这就好。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2188")

    SetScenarioFlags(0x12E, 5)
    ClearChrFlags(0xB, 0x10)
    ClearChrFlags(0x9, 0x10)
    OP_4C(0xB, 0xFF)
    OP_4C(0x9, 0xFF)
    Return()

    # Function_13_1FA9 end

    def Function_14_219E(): pass

    label("Function_14_219E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_2228")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_21C1")
    Call(0, 12)
    ClearChrFlags(0xA, 0x10)
    Jump("loc_2228")

    label("loc_21C1")


    #C0108
    ChrTalk(
        0xFE,
        (
            "嗯，这件货物是要\x01",
            "送到总务一科的，\x01",
            "这件是要送到财务科的……\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0xFE,
        (
            "新市政厅就在附近，\x01",
            "赶快送过去吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2228")

    TalkEnd(0xFE)
    Return()

    # Function_14_219E end

    def Function_15_222C(): pass

    label("Function_15_222C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_22B7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12E, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_224F")
    Call(0, 13)
    ClearChrFlags(0xB, 0x10)
    Jump("loc_22B7")

    label("loc_224F")


    #C0110
    ChrTalk(
        0xFE,
        (
            "唔唔，这样的话，收到的参加费\x01",
            "都不够支付设施租用费啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0xFE,
        (
            "无论如何都要想办法\x01",
            "再争取到一些资金……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_22B7")

    TalkEnd(0xFE)
    Return()

    # Function_15_222C end

    def Function_16_22BB(): pass

    label("Function_16_22BB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_22F8")

    #C0112
    ChrTalk(
        0xFE,
        (
            "请问，听说在这里\x01",
            "也可以办理居民登记手续……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_22F8")

    TalkEnd(0xFE)
    Return()

    # Function_16_22BB end

    def Function_17_22FC(): pass

    label("Function_17_22FC")

    TalkBegin(0xFE)

    #C0113
    ChrTalk(
        0xFE,
        (
            "我很担心在百货店\x01",
            "工作的妈妈……\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_17_22FC end

    def Function_18_2328(): pass

    label("Function_18_2328")

    TalkBegin(0xFE)

    #C0114
    ChrTalk(
        0xFE,
        (
            "唔……怎么会这样。\x01",
            "没想到会演变成这种事态……\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0xFE,
        (
            "迪塔总统……\x01",
            "我本来还很信任他的。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_18_2328 end

    def Function_19_2389(): pass

    label("Function_19_2389")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CC, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2740")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x84, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_26AF")

    #C0116
    ChrTalk(
        0xFE,
        (
            "哎呀，你们是……\x01",
            "警察局的人啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0xFE,
        "之前真是承蒙照顾了。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_245E")

    #C0118
    ChrTalk(
        0x101,
        (
            "#00005F啊……\x01",
            "是皮埃尔副局长的夫人……？\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0x105,
        (
            "#10402F呵呵，好久不见了，夫人。\x01",
            "您在市民会馆避难啊？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_24B6")

    label("loc_245E")


    #C0120
    ChrTalk(
        0x101,
        (
            "#00005F啊……莫非是\x01",
            "皮埃尔副局长的夫人……？\x02\x03",

            "#00001F那个……\x01",
            "您在市民会馆避难啊？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_24B6")


    #C0121
    ChrTalk(
        0xFE,
        (
            "嗯，是的……\x01",
            "……请问，你们有没有见到我丈夫？\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0xFE,
        (
            "他说要去兰花塔，\x01",
            "然后就一直没有回来。\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0x103,
        (
            "#00200F不，没见到过……\x02\x03",

            "副局长要去\x01",
            "兰花塔做什么？\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0xFE,
        (
            "这个……\x01",
            "我没有问呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0xFE,
        (
            "他可真是的，在这种时期\x01",
            "还要让人操心……\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0xFE,
        (
            "等他回来以后，\x01",
            "一定要狠狠教训他一顿才行。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0127
    ChrTalk(
        0x101,
        (
            "#00000F……夫人，请您继续\x01",
            "在这里等着吧。\x02\x03",

            "说不定他突然\x01",
            "就会回来了。\x02",
        )
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0xFE,
        (
            "……嗯，我会的。\x01",
            "如果你们找到了他，就和我联络一下吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2738")

    label("loc_26AF")


    #C0129
    ChrTalk(
        0xFE,
        (
            "我丈夫去了兰花塔，\x01",
            "然后就一直没有回来。\x02",
        )
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0xFE,
        (
            "他可真是的，在这种时期\x01",
            "还要让人操心……\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0xFE,
        (
            "等他回来以后，\x01",
            "一定要狠狠教训他一顿才行。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2738")

    SetScenarioFlags(0x1CC, 2)
    Jump("loc_279C")

    label("loc_2740")


    #C0132
    ChrTalk(
        0xFE,
        (
            "他可真是的，在这种时期\x01",
            "还要让人操心……\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0xFE,
        (
            "等他回来以后，\x01",
            "一定要狠狠教训他一顿才行。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_279C")

    TalkEnd(0xFE)
    Return()

    # Function_19_2389 end

    def Function_20_27A0(): pass

    label("Function_20_27A0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_27FC")

    #C0134
    ChrTalk(
        0xFE,
        (
            "慢着，为什么\x01",
            "不让我们进兰花塔啊？\x02",
        )
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0xFE,
        (
            "至少也要让我们自由出入\x01",
            "塔前广场吧？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_27FC")

    TalkEnd(0xFE)
    Return()

    # Function_20_27A0 end

    def Function_21_2800(): pass

    label("Function_21_2800")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2842")

    #C0136
    ChrTalk(
        0xFE,
        (
            "是啊是啊！\x01",
            "突然就说禁止入内，\x01",
            "以前从没听说过啊！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2842")

    TalkEnd(0xFE)
    Return()

    # Function_21_2800 end

    def Function_22_2846(): pass

    label("Function_22_2846")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_2888")

    #C0137
    ChrTalk(
        0xFE,
        (
            "我想参加明天要举行的\x01",
            "市民座谈会……\x01",
            "还有空位吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2888")

    TalkEnd(0xFE)
    Return()

    # Function_22_2846 end

    def Function_23_288C(): pass

    label("Function_23_288C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_28D4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x199, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x199, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x199, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x199, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_28C6")
    Call(0, 32)
    Return()

    label("loc_28C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x198, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_28D4")
    Call(0, 29)
    Return()

    label("loc_28D4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_29F4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_298C")

    #C0138
    ChrTalk(
        0xFE,
        (
            "真是不好意思啊，\x01",
            "洛依给你们添麻烦了……\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0xFE,
        (
            "不过，要是能顺利举行选秀活动，\x01",
            "对市民们来说，\x01",
            "也是个放松心情的机会。\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0xFE,
        (
            "请你们努力\x01",
            "征召参加者吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_29EF")

    label("loc_298C")


    #C0141
    ChrTalk(
        0xFE,
        (
            "要是能顺利举行选秀活动，\x01",
            "对市民们来说，\x01",
            "也是个放松心情的机会。\x02",
        )
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0xFE,
        (
            "请你们努力\x01",
            "征召参加者吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_29EF")

    Jump("loc_2A79")

    label("loc_29F4")


    #C0143
    ChrTalk(
        0xFE,
        (
            "选秀活动不但让市民们\x01",
            "放松了心情，还募集到\x01",
            "不少支持复兴的捐款。\x02",
        )
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0xFE,
        (
            "说起来，选秀活动是洛依出的主意……\x01",
            "呵呵，他也算有点出息了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A79")

    TalkEnd(0xFE)
    Return()

    # Function_23_288C end

    def Function_24_2A7D(): pass

    label("Function_24_2A7D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2AC5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x199, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x199, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x199, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x199, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2AB7")
    Call(0, 32)
    Return()

    label("loc_2AB7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x198, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2AC5")
    Call(0, 29)
    Return()

    label("loc_2AC5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C40")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2BC7")

    #C0145
    ChrTalk(
        0x15,
        (
            "希望你们帮忙寻找\x01",
            "愿意参加选秀活动的\x01",
            "『职业女性』。\x02",
        )
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0x15,
        (
            "『服务员』、『技师』、\x01",
            "『女仆』、『修女』……\x01",
            "请帮忙寻找从事这四种职业的女性。\x02",
        )
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0x15,
        (
            "如果有从事这些职业的人参加，\x01",
            "参选者的职业类型\x01",
            "就比较平衡了。\x02",
        )
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0x15,
        "拜托你们啦。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_2C3B")

    label("loc_2BC7")


    #C0149
    ChrTalk(
        0x15,
        (
            "『服务员』、『技师』、\x01",
            "『女仆』、『修女』……\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0x15,
        (
            "请帮忙寻找从事这四种\x01",
            "工作的『职业女性』。\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0x15,
        "拜托你们啦。\x02",
    )

    CloseMessageWindow()

    label("loc_2C3B")

    Jump("loc_2C93")

    label("loc_2C40")


    #C0152
    ChrTalk(
        0x15,
        (
            "托你们的福，\x01",
            "选秀活动圆满成功了！\x02",
        )
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0x15,
        (
            "多亏你们\x01",
            "找到了参选者，\x01",
            "真是太谢谢啦！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C93")

    TalkEnd(0xFE)
    Return()

    # Function_24_2A7D end

    def Function_25_2C97(): pass

    label("Function_25_2C97")

    TalkBegin(0xFE)

    #C0154
    ChrTalk(
        0xFE,
        "父亲就在旧城区的这个地址……\x02",
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0xFE,
        (
            "太好了，艾娅莉！\x01",
            "接下来，我们直接过去找他就行了。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_25_2C97 end

    def Function_26_2CF7(): pass

    label("Function_26_2CF7")

    TalkBegin(0xFE)

    #C0156
    ChrTalk(
        0xFE,
        (
            "呵呵，终于知道他在哪里了。\x01",
            "真是太好了，阿鲁姆⊥\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_26_2CF7 end

    def Function_27_2D33(): pass

    label("Function_27_2D33")

    EventBegin(0x0)
    OP_4B(0x8, 0xFF)
    StopBGM(0x7D0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-190, 1300, 5510, 0)
    MoveCamera(34, 17, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(20640, 0)
    SetChrPos(0x101, -600, 0, 4700, 0)
    SetChrPos(0x102, 600, 0, 4700, 0)
    SetChrPos(0x109, -700, 0, 3600, 0)
    SetChrPos(0x105, 700, 0, 3600, 0)
    FadeToBright(1000, 0)
    OP_0D()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7111", 0)

    #C0157
    ChrTalk(
        0x8,
        (
            "欢迎来到\x01",
            "克洛斯贝尔市民会馆。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0158
    ChrTalk(
        0x8,
        (
            "是特别任务支援科的各位吧？\x01",
            "你们总算来了。\x02",
        )
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0x101,
        "#12P#00000F嗯，我们来确认委托内容。\x02",
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0x102,
        (
            "#00102F今后也请多多关照\x01",
            "加入了新成员的支援科。\x02",
        )
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0x105,
        "#12P#10302F请多关照，小姐。\x02",
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0x109,
        "#12P#10100F还请多照顾呢。\x02",
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0x8,
        (
            "好的，\x01",
            "彼此彼此。\x02",
        )
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0x101,
        (
            "#12P#00006F……话说回来，这里变成\x01",
            "市民会馆了啊，总觉得有些奇怪。\x02",
        )
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0x109,
        (
            "#12P#10106F嗯，这栋建筑\x01",
            "竟然不再是市政厅了，\x01",
            "感觉有些不真实呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0x102,
        (
            "#00104F呵呵，新市政厅\x01",
            "已经搬迁到即将\x01",
            "完工的新址了……\x02\x03",

            "#00100F不过，这里也会作为\x01",
            "市政厅的『办事处』而保留下来。\x02\x03",

            "从这个意义上说，这里今后\x01",
            "应该也会一如既往地发挥作用。\x02",
        )
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0x109,
        "#12P#10103F原来如此。\x02",
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0x8,
        (
            "是的，本接待处\x01",
            "将继续负责办理\x01",
            "居民手续等市政业务。\x02",
        )
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0x8,
        (
            "……只不过，相关告示似乎\x01",
            "还没有被市民们熟知，\x01",
            "所以现在接到了许多咨询……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_63(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x8)

    #C0170
    ChrTalk(
        0x8,
        (
            "非、非常抱歉，\x01",
            "说了些与各位毫不相干的话。\x02",
        )
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0x101,
        "#12P#00012F哪里……看来你们也很辛苦啊。\x02",
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0x105,
        (
            "#12P#10302F呵呵，话说回来，\x01",
            "官员考虑问题的方式真是无聊呢。\x02\x03",

            "换作是我的话，就会参考欢乐街一带，\x01",
            "把这里变成『成人的社交场所』。\x02\x03",

            "#10309F设立一家由市民公仆担任招待的俱乐部……\x01",
            "特别任务支援科一定会比以往\x01",
            "更加抢手的。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x8, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0173
    ChrTalk(
        0x101,
        (
            "#12P#00006F抢手……\x01",
            "那算什么支援请求啊。\x02\x03",

            "#00001F说到底，\x01",
            "要公务员从事夜间工作，\x01",
            "本身就是不可能的啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0x109,
        (
            "#6P#10112F啊、啊哈哈……\x01",
            "（我还想象了一下。）\x02",
        )
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0x102,
        (
            "#00103F咳咳……\x01",
            "罗伊德，你没有忘记正事吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0x101,
        (
            "#12P#00011F啊、哦哦，对啊。\x02\x03",

            "#00000F嗯，不好意思，\x01",
            "关于支援请求……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0177
    ChrTalk(
        0x8,
        "是、是，我这就说明。\x02",
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0x8,
        (
            "各位知道\x01",
            "『住户变更表』吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0x8,
        (
            "居民在搬家等\x01",
            "住所变迁的情况下，\x01",
            "需要向市里提交登记表……\x02",
        )
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0x8,
        (
            "我们之前发现，\x01",
            "有些登记表上\x01",
            "写着可疑的名字。\x02",
        )
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0x109,
        "#12P#10105F可疑的名字吗？\x02",
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0x8,
        (
            "嗯……准确地说，\x01",
            "也就是『没有在市里\x01",
            "登记过的名字』。\x02",
        )
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0x8,
        (
            "我们发现了数个\x01",
            "没有登记在市内的\x01",
            "『居民·公司名单』中的名字。\x02",
        )
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0x8,
        (
            "所以希望各位前去确认\x01",
            "这些登记了可疑名字的\x01",
            "住户的实际情况……\x02",
        )
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0x8,
        (
            "另外，谨慎起见，\x01",
            "最好再确认一下\x01",
            "原住户的情况。\x02",
        )
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0x101,
        (
            "#12P#00001F原来如此，也就是说，\x01",
            "要去确认一下这些可疑住所的\x01",
            "新旧居住者吧？\x02\x03",

            "#00003F不知道会不会牵扯到犯罪行为……\x01",
            "确实不能置之不理。\x02\x03",

            "#00000F的确该好好\x01",
            "调查一下。\x02",
        )
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0x102,
        (
            "#00103F嗯，是呀。\x02\x03",

            "#00100F对了，那些可疑住所的地址，\x01",
            "自然是已经确定了的……\x02\x03",

            "但说起原住户的所在地，\x01",
            "市里也有所掌握吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0x8,
        (
            "不，只有其中\x01",
            "一位办理了\x01",
            "迁居登记……\x02",
        )
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0x8,
        (
            "至于其他人的情况，\x01",
            "我们就完全不清楚了。\x02",
        )
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0x105,
        (
            "#12P#10300F是吗，这样的话，\x01",
            "就需要我们自行寻找了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0191
    ChrTalk(
        0x109,
        (
            "#12P#10100F不过，我们首先还是去调查\x01",
            "那些可疑住户和那位\x01",
            "已知去向的居民为好。\x02\x03",

            "至于不清楚去向的居民，\x01",
            "我们也许可以在\x01",
            "调查过程中查到一些信息。\x02",
        )
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0x101,
        (
            "#12P#00003F嗯，是啊。\x02\x03",

            "#00000F顺便一问，有没有\x01",
            "这些住户的列表？\x02",
        )
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0x8,
        (
            "有的，我准备了登记表的\x01",
            "副本，请确认。\x02",
        )
    )

    CloseMessageWindow()

    #C0194
    ChrTalk(
        0x101,
        "#12P#00000F好，我先收下了。\x02",
    )

    CloseMessageWindow()
    OP_97(0x101, 0x0, 0x0, 0x258, 0x3E8, 0x0)
    Sleep(800)
    OP_93(0x101, 0xB4, 0x1F4)
    OP_97(0x101, 0x0, 0x0, 0xFFFFFDA8, 0x3E8, 0x0)
    Sleep(50)

    def lambda_387E():
        OP_93(0x101, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_387E)

    def lambda_388B():
        OP_93(0x102, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_388B)

    def lambda_3898():
        OP_93(0x109, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_3898)

    def lambda_38A5():
        OP_93(0x105, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_38A5)
    Sleep(300)

    #C0195
    ChrTalk(
        0x101,
        (
            "#5P#00000F嗯……\x01",
            "有问题的住所共有三处啊。\x02\x03",

            "首先是住宅街的一处……\x01",
            "艾莉应该知道这个地址吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0x102,
        (
            "#11P#00100F我看看……\x01",
            "啊，就在我家的隔壁。\x02\x03",

            "#00105F居住者是『高贵之血』……\x01",
            "这是什么？公司名吗？\x02\x03",

            "#00103F这所房屋的居住者\x01",
            "本应是证券经理\x01",
            "本德先生一家……\x02",
        )
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0x101,
        (
            "#5P#00001F嗯，列表上也有记载，\x01",
            "他正是原居住者。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0x101)

    #C0198
    ChrTalk(
        0x101,
        (
            "#5P#00003F证券经理本德先生……\x02\x03",

            "#00001F好像是在教团事件中\x01",
            "服用过『真知』的受害者之一吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0x102,
        (
            "#11P#00103F嗯，没错。\x02\x03",

            "#00108F我只听说他们一家\x01",
            "在事件结束之后，\x01",
            "过得挺不容易……\x02",
        )
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0x109,
        (
            "#6P#10101F莫非是……被卷入\x01",
            "什么麻烦了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0x101,
        (
            "#5P#00001F不清楚……\x01",
            "看起来，提交迁居登记的\x01",
            "就是本德先生呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0202
    ChrTalk(
        0x105,
        (
            "#12P#10300F迁居地址是东街\x01",
            "『洋槐庄园』二层。\x02\x03",

            "就是邻接游击士协会左侧的\x01",
            "那座建筑。\x02",
        )
    )

    CloseMessageWindow()

    #C0203
    ChrTalk(
        0x101,
        (
            "#5P#00003F住宅街和东街吗……\x01",
            "两边都要认真调查啊。\x02\x03",

            "#00001F下一个住户也在东街，\x01",
            "这个地址好像是钓公师团……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0204
    ChrTalk(
        0x101,
        "#5P#00011F哎，什么！？\x02",
    )

    CloseMessageWindow()

    #C0205
    ChrTalk(
        0x109,
        "#6P#10105F怎、怎么了？\x02",
    )

    CloseMessageWindow()

    #C0206
    ChrTalk(
        0x101,
        (
            "#5P#00008F居、居住者一栏中写的是\x01",
            "『钓皇俱乐部』……\x02\x03",

            "从没听说过这个团体。\x02",
        )
    )

    CloseMessageWindow()

    #C0207
    ChrTalk(
        0x102,
        (
            "#11P#00105F罗伊德，你不也是\x01",
            "『钓公师团』的团员吗？\x02\x03",

            "其他成员没和你\x01",
            "说过什么吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0208
    ChrTalk(
        0x101,
        (
            "#5P#00006F嗯，最近太忙，\x01",
            "都顾不上钓鱼了。\x02\x03",

            "#00001F说起来，前居住者\x01",
            "『钓公师团』目前去向不明……\x01",
            "唔～该不会是改名字了吧？\x02\x03",

            "#00003F……总之，\x01",
            "这一处也要仔细调查。\x02\x03",

            "#00001F最后的住所在旧城区\x01",
            "『莲花公馆』的一层。\x02\x03",

            "前居住者是盖特纳……\x01",
            "目前也是去向不明。\x02\x03",

            "而现在的居住者是……\x01",
            "『肖恩·阿尔纳姆』。\x02\x03",

            "#00005F……咦，好像曾在哪里\x01",
            "听过这个名字……？\x02",
        )
    )

    CloseMessageWindow()

    #C0209
    ChrTalk(
        0x105,
        "#12P#10304F呵呵，这是一位很有名的童话作者。\x02",
    )

    CloseMessageWindow()

    #C0210
    ChrTalk(
        0x101,
        "#5P#00011F哎……？\x02",
    )

    CloseMessageWindow()

    #C0211
    ChrTalk(
        0x102,
        (
            "#11P#00103F是图书馆中大受欢迎的童话\x01",
            "《玛尔克与森林深处的魔女》的\x01",
            "作者哦。\x02\x03",

            "#00100F罗伊德不是也听说过吗？\x01",
            "你忘了吗？我们以前潜入鲁巴彻\x01",
            "据点的时候……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0212
    ChrTalk(
        0x101,
        (
            "#5P#00005F哦哦，说起来，\x01",
            "我们当时解除门锁的密码\x01",
            "中就有这个名字呢。\x02\x03",

            "#00008F但真是没想到，那位著名作家\x01",
            "竟然会住在旧城区……\x02",
        )
    )

    CloseMessageWindow()

    #C0213
    ChrTalk(
        0x102,
        (
            "#11P#00101F嗯，更重要的是，\x01",
            "那位作者应该已经去世了。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0214
    ChrTalk(
        0x101,
        (
            "#5P#00006F是、是这样吗……\x01",
            "我开始有些不安了。\x02",
        )
    )

    CloseMessageWindow()

    #C0215
    ChrTalk(
        0x105,
        (
            "#12P#10302F呵呵，其它的倒也罢了，\x01",
            "但在接收登记表的时候，\x01",
            "至少应该注意到这个啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x8)

    #C0216
    ChrTalk(
        0x8,
        "非、非常抱歉。\x02",
    )

    CloseMessageWindow()

    def lambda_40BE():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_40BE)
    Sleep(50)

    def lambda_40CE():
        OP_93(0x102, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_40CE)
    Sleep(50)

    def lambda_40DE():
        OP_93(0x109, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_40DE)
    Sleep(50)

    def lambda_40EE():
        OP_93(0x105, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_40EE)
    Sleep(100)

    #C0217
    ChrTalk(
        0x8,
        (
            "虽然我们这些职员一直\x01",
            "都很仔细，但还是……\x02",
        )
    )

    CloseMessageWindow()

    #C0218
    ChrTalk(
        0x102,
        (
            "#00105F哪里……\x01",
            "毕竟市政厅现在正面临着组织改革和事务交接，\x01",
            "处于十分繁忙的时期嘛。\x02",
        )
    )

    CloseMessageWindow()

    #C0219
    ChrTalk(
        0x109,
        (
            "#12P#10101F嗯，而且再怎么说，\x01",
            "错的也都是提交这种登记表的人呀！\x02",
        )
    )

    CloseMessageWindow()

    #C0220
    ChrTalk(
        0x8,
        "谢、谢谢各位。\x02",
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0x101,
        (
            "#12P#00000F嗯，既然如此，\x01",
            "我们就马上开始调查了。\x02",
        )
    )

    CloseMessageWindow()

    #C0222
    ChrTalk(
        0x102,
        (
            "#00100F全部确认以后，\x01",
            "会再来报告的。\x02",
        )
    )

    CloseMessageWindow()

    #C0223
    ChrTalk(
        0x8,
        (
            "好、好的，\x01",
            "那就拜托各位了。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(80, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0224
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "任务【调查可疑住户】\x07\x00",
            "开始！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_69(0xFF, 0x0)
    OP_4C(0x8, 0xFF)
    SetScenarioFlags(0x131, 4)
    OP_29(0x6A, 0x1, 0x0)
    SetChrPos(0x0, 0, 0, 4000, 180)
    StopBGM(0xBB8)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7562", 0)
    EventEnd(0x5)
    Return()

    # Function_27_2D33 end

    def Function_28_42D6(): pass

    label("Function_28_42D6")

    EventBegin(0x0)
    OP_4B(0x8, 0xFF)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-190, 1300, 5510, 0)
    MoveCamera(34, 17, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(20640, 0)
    SetChrPos(0x101, -600, 0, 4700, 0)
    SetChrPos(0x102, 600, 0, 4700, 0)
    SetChrPos(0x109, -700, 0, 3600, 0)
    SetChrPos(0x105, 700, 0, 3600, 0)
    FadeToBright(1000, 0)
    OP_0D()

    #C0225
    ChrTalk(
        0x8,
        (
            "#12P#1P各位，\x01",
            "确认可疑住户的工作\x01",
            "进展还顺利吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0x101,
        (
            "#12P#00000F嗯，已经全部\x01",
            "确认完毕，\x01",
            "所以回来报告了。\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    #A0227
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "交出了写有正确居住者姓名的\x01",
            "登记表复印件。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0228
    ChrTalk(
        0x8,
        (
            "#12P#1P原来如此，连细节\x01",
            "都调查得这么清楚啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0229
    ChrTalk(
        0x8,
        (
            "#12P#1P唔，住宅街的房屋住进了\x01",
            "共和国人，东街的房屋\x01",
            "住进了帝国人啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0230
    ChrTalk(
        0x8,
        "#12P#1P而旧城区的房屋……哎？\x02",
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0x101,
        "#12P#00005F怎么了？\x02",
    )

    CloseMessageWindow()

    #C0232
    ChrTalk(
        0x8,
        (
            "#12P#1P没什么，只是盖巴尔先生的\x01",
            "名字太让人感到意外了。\x02",
        )
    )

    CloseMessageWindow()

    #C0233
    ChrTalk(
        0x8,
        (
            "#12P#1P我在这里也曾\x01",
            "见过他很多次，\x01",
            "所以心情有点复杂。\x02",
        )
    )

    CloseMessageWindow()

    #C0234
    ChrTalk(
        0x8,
        (
            "#12P#1P该怎么说呢，\x01",
            "虽然他做过一些坏事，\x01",
            "但是又让人恨不起来。\x02",
        )
    )

    CloseMessageWindow()

    #C0235
    ChrTalk(
        0x102,
        (
            "#00103F嗯，似乎\x01",
            "可以理解。\x02",
        )
    )

    CloseMessageWindow()

    #C0236
    ChrTalk(
        0x109,
        (
            "#12P#10100F的确，无论从好的意义上来说，还是从坏的\x01",
            "意义上来说，他都是个很单纯的人呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0237
    ChrTalk(
        0x105,
        (
            "#12P#10304F呵呵，要是\x01",
            "能再正经点，\x01",
            "说不定还有些可爱之处。\x02",
        )
    )

    CloseMessageWindow()

    #C0238
    ChrTalk(
        0x8,
        "呵呵，或许正如你们所说吧。\x02",
    )

    CloseMessageWindow()

    #C0239
    ChrTalk(
        0x8,
        (
            "……总之，各位的调查成果\x01",
            "实在是非常出色。\x02",
        )
    )

    CloseMessageWindow()

    #C0240
    ChrTalk(
        0x8,
        (
            "接下来，只要交给居民科的人，办理好\x01",
            "各种手续，应该就能妥善处理好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0241
    ChrTalk(
        0x8,
        (
            "今天真是\x01",
            "太谢谢各位了。\x02",
        )
    )

    CloseMessageWindow()

    #C0242
    ChrTalk(
        0x101,
        (
            "#12P#00002F哪里，能帮上忙\x01",
            "就再好不过了。\x02",
        )
    )

    CloseMessageWindow()

    #C0243
    ChrTalk(
        0x102,
        (
            "#00102F如果以后再有什么事，\x01",
            "请随时联络我们。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0244
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "任务【调查可疑住户】\x07\x00",
            "完成！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_29(0x6A, 0x1, 0x7)
    OP_29(0x6A, 0x4, 0x10)
    OP_29(0xA1, 0x1, 0xF)
    OP_69(0xFF, 0x0)
    OP_4C(0x8, 0xFF)
    SetChrPos(0x0, 0, 0, 4000, 180)
    EventEnd(0x5)
    Return()

    # Function_28_42D6 end

    def Function_29_47D8(): pass

    label("Function_29_47D8")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x198, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4C1B")
    Fade(500)
    OP_68(1560, 1500, 3500, 0)
    MoveCamera(39, 27, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(20900, 0)
    SetChrPos(0x101, 1810, 0, 3530, 0)
    SetChrPos(0x102, 620, 0, 3130, 0)
    SetChrPos(0x104, 1610, 0, 2310, 0)
    SetChrPos(0x103, 2860, 0, 2990, 0)
    SetChrPos(0x105, 2700, 0, 1650, 0)
    SetChrPos(0x109, 570, 0, 1600, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0x14, 0xFF)
    OP_4B(0x15, 0xFF)
    OP_0D()

    #C0245
    ChrTalk(
        0x14,
        "唔……果然凑不够人啊。\x02",
    )

    CloseMessageWindow()

    #C0246
    ChrTalk(
        0x14,
        (
            "我说，洛依啊，\x01",
            "不然还是放弃\x01",
            "这项企划吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0247
    ChrTalk(
        0x15,
        "您在说什么呢，爷爷！\x02",
    )

    CloseMessageWindow()

    #C0248
    ChrTalk(
        0x15,
        (
            "在为了给市里的各位打气\x01",
            "而举办的慈善宴会中，\x01",
            "这项企划可是重头戏啊！\x02",
        )
    )

    CloseMessageWindow()

    #C0249
    ChrTalk(
        0x15,
        (
            "如果把它取消，\x01",
            "那要拿什么企划来替代啊！？\x02",
        )
    )

    CloseMessageWindow()

    #C0250
    ChrTalk(
        0x14,
        "可、可是……\x02",
    )

    CloseMessageWindow()

    #C0251
    ChrTalk(
        0x101,
        (
            "#00000F不好意思，\x01",
            "在二位忙乱之中\x01",
            "打扰了……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x14, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x15, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_49E7():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_49E7)
    Sleep(50)
    OP_93(0x15, 0xB4, 0x1F4)

    #C0252
    ChrTalk(
        0x15,
        "你们是……\x02",
    )

    CloseMessageWindow()

    #C0253
    ChrTalk(
        0x14,
        "哦哦，来得正好呢。\x02",
    )

    CloseMessageWindow()

    #C0254
    ChrTalk(
        0x14,
        (
            "今天是来参加\x01",
            "慈善宴会吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0255
    ChrTalk(
        0x101,
        (
            "#00005F哦，我们接到了工商协会\x01",
            "发来的委托，好像是让我们\x01",
            "协助慈善宴会……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x14, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0256
    ChrTalk(
        0x14,
        "咦，我没印象啊。\x02",
    )

    CloseMessageWindow()

    #C0257
    ChrTalk(
        0x15,
        "哦，发出委托的是我啦。\x02",
    )

    CloseMessageWindow()
    OP_63(0x14, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0x14, 0x15, 500)
    Sleep(500)

    #C0258
    ChrTalk(
        0x14,
        (
            "什、什么？\x01",
            "洛依，你几时……\x02",
        )
    )

    CloseMessageWindow()

    #C0259
    ChrTalk(
        0x15,
        (
            "哈哈，其实就是刚才\x01",
            "悄悄发出的。\x02",
        )
    )

    CloseMessageWindow()

    #C0260
    ChrTalk(
        0x15,
        (
            "那么，虽然有些仓促，\x01",
            "但我这就开始说明工作内容吧。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4BF6():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_4BF6)

    #C0261
    ChrTalk(
        0x15,
        "时间方面没问题吧？\x02",
    )

    CloseMessageWindow()
    Jump("loc_4D16")

    label("loc_4C1B")

    Fade(500)
    OP_68(1560, 1500, 3500, 0)
    MoveCamera(39, 27, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(20900, 0)
    SetChrPos(0x101, 1810, 0, 3530, 0)
    SetChrPos(0x102, 620, 0, 3130, 0)
    SetChrPos(0x104, 1610, 0, 2310, 0)
    SetChrPos(0x103, 2860, 0, 2990, 0)
    SetChrPos(0x105, 2700, 0, 1650, 0)
    SetChrPos(0x109, 570, 0, 1600, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0x14, 0xFF)
    OP_4B(0x15, 0xFF)
    OP_93(0x14, 0xB4, 0x0)
    OP_93(0x15, 0xB4, 0x0)
    OP_0D()

    #C0262
    ChrTalk(
        0x15,
        (
            "我想立刻说明\x01",
            "工作内容……\x02",
        )
    )

    CloseMessageWindow()

    #C0263
    ChrTalk(
        0x15,
        "时间方面没问题吧？\x02",
    )

    CloseMessageWindow()

    label("loc_4D16")

    Call(0, 30)
    OP_4C(0x14, 0xFF)
    OP_4C(0x15, 0xFF)
    OP_93(0x14, 0x5A, 0x0)
    OP_93(0x15, 0x10E, 0x0)
    BeginChrThread(0x14, 0, 0, 0)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 1750, 0, 4000, 180)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_29_47D8 end

    def Function_30_4D61(): pass

    label("Function_30_4D61")

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
        (0, "loc_4DBB"),
        (1, "loc_4DC3"),
        (SWITCH_DEFAULT, "loc_4E36"),
    )


    label("loc_4DBB")

    Call(0, 31)
    Jump("loc_4E36")

    label("loc_4DC3")


    #C0264
    ChrTalk(
        0x101,
        (
            "#00006F……对、对不起，\x01",
            "现在还不太方便……\x02",
        )
    )

    CloseMessageWindow()

    #C0265
    ChrTalk(
        0x15,
        "是吗……真遗憾。\x02",
    )

    CloseMessageWindow()

    #C0266
    ChrTalk(
        0x15,
        (
            "如果有时间了，\x01",
            "就再来帮个忙吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x198, 3)
    Jump("loc_4E36")

    label("loc_4E36")

    Return()

    # Function_30_4D61 end

    def Function_31_4E37(): pass

    label("Function_31_4E37")


    #C0267
    ChrTalk(
        0x101,
        "#00000F嗯，没问题。\x02",
    )

    CloseMessageWindow()

    #C0268
    ChrTalk(
        0x15,
        (
            "这就对了！\x01",
            "好，我来说明委托内容。\x02",
        )
    )

    CloseMessageWindow()

    #C0269
    ChrTalk(
        0x15,
        (
            "今天要在这个市民会馆的会场中\x01",
            "举办一场慈善宴会，\x01",
            "你们应该也知道吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0270
    ChrTalk(
        0x15,
        (
            "现在正在进行钢琴演奏\x01",
            "和立餐宴会，\x01",
            "但却出现了一个问题。\x02",
        )
    )

    CloseMessageWindow()

    #C0271
    ChrTalk(
        0x102,
        "#00105F问题……？\x02",
    )

    CloseMessageWindow()

    #C0272
    ChrTalk(
        0x15,
        (
            "嗯，按照预定计划，\x01",
            "接下来将要举行由我\x01",
            "企划的一项重头活动……\x02",
        )
    )

    CloseMessageWindow()

    #C0273
    ChrTalk(
        0x15,
        (
            "但由于没有征召到足够的参加者，\x01",
            "活动将面临取消。\x02",
        )
    )

    CloseMessageWindow()

    #C0274
    ChrTalk(
        0x109,
        "#10103F委托上也是这么写的。\x02",
    )

    CloseMessageWindow()

    #C0275
    ChrTalk(
        0x105,
        (
            "#10300F那么，这个活动\x01",
            "具体是什么内容？\x02",
        )
    )

    CloseMessageWindow()

    #C0276
    ChrTalk(
        0x15,
        (
            "是『克洛斯贝尔职业女性选秀活动\x01",
            "    ～劳动中的女性最美丽～』。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0277
    ChrTalk(
        0x101,
        (
            "#00012F也、也就是所谓的\x01",
            "选秀比赛吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0278
    ChrTalk(
        0x104,
        "#00309F哦，这倒挺有意思。\x02",
    )

    CloseMessageWindow()

    #C0279
    ChrTalk(
        0x103,
        (
            "#00211F但总觉得副标题\x01",
            "起得有些庸俗……\x02",
        )
    )

    CloseMessageWindow()

    #C0280
    ChrTalk(
        0x15,
        (
            "嗯，简单来说，\x01",
            "就是聚焦于克洛斯贝尔\x01",
            "职业女性的选秀活动啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0281
    ChrTalk(
        0x15,
        (
            "只是……直到现在，\x01",
            "都没有征召到几个参选者。\x02",
        )
    )

    CloseMessageWindow()

    #C0282
    ChrTalk(
        0x14,
        (
            "只有三个人\x01",
            "前来报名。\x02",
        )
    )

    CloseMessageWindow()

    #C0283
    ChrTalk(
        0x14,
        (
            "这点人数实在是\x01",
            "不足以举办活动，\x01",
            "我们正在商量是否要取消呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0284
    ChrTalk(
        0x102,
        (
            "#00106F嗯，大部分人\x01",
            "难免会迟疑吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0285
    ChrTalk(
        0x105,
        (
            "#10302F呵呵，我大概已经知道\x01",
            "你要委托我们什么了。\x02",
        )
    )

    CloseMessageWindow()

    #C0286
    ChrTalk(
        0x15,
        "嗯，正如你所想。\x02",
    )

    CloseMessageWindow()

    #C0287
    ChrTalk(
        0x15,
        (
            "希望各位帮忙\x01",
            "寻找愿意参加\x01",
            "选秀活动的『职业女性』。\x02",
        )
    )

    CloseMessageWindow()

    #C0288
    ChrTalk(
        0x101,
        (
            "#00004F原来如此……\x01",
            "我已经明白委托内容了。\x02\x03",

            "#00000F顺便一问，刚才说的\x01",
            "那三位现有参选者……\x01",
            "都是从事什么职业的人呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0289
    ChrTalk(
        0x15,
        (
            "嗯，首先是百货店的\x01",
            "接待员辛茜亚小姐。\x02",
        )
    )

    CloseMessageWindow()

    #C0290
    ChrTalk(
        0x15,
        (
            "然后是后巷的女公关\x01",
            "爱丽斯小姐。\x02",
        )
    )

    CloseMessageWindow()

    #C0291
    ChrTalk(
        0x15,
        (
            "还有克洛斯贝尔警察局的\x01",
            "女警凯特小姐\x01",
            "也答应参加了。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0292
    ChrTalk(
        0x101,
        "#00012F连凯特前辈都……\x02",
    )

    CloseMessageWindow()

    #C0293
    ChrTalk(
        0x105,
        (
            "#10304F接待小姐、女公关和女警啊。\x01",
            "呵呵，类型还挺丰富的嘛。\x02\x03",

            "#10302F接下来，还需要邀请\x01",
            "从事哪些职业的女孩呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0294
    ChrTalk(
        0x15,
        "唔，这个嘛……\x02",
    )

    CloseMessageWindow()

    #C0295
    ChrTalk(
        0x15,
        (
            "『服务员』、『技师』、\x01",
            "『女仆』、『修女』……\x01",
            "请帮忙寻找从事这四种职业的女性吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0296
    ChrTalk(
        0x15,
        (
            "如果有从事这些职业的人参加，\x01",
            "参选者的职业类型\x01",
            "就比较平衡了。\x02",
        )
    )

    CloseMessageWindow()

    #C0297
    ChrTalk(
        0x15,
        (
            "……原本还想邀请\x01",
            "护士小姐和彩虹剧团的\x01",
            "团员来参加呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0298
    ChrTalk(
        0x103,
        (
            "#00203F这恐怕是不可能的。\x01",
            "伊莉娅小姐出了那种事情，\x01",
            "彩虹剧团的各位根本顾不上这种活动……\x02\x03",

            "而乌尔斯拉医院的护士们为了照顾众多伤患，\x01",
            "应该也都忙得不可开交了。\x02",
        )
    )

    CloseMessageWindow()

    #C0299
    ChrTalk(
        0x101,
        (
            "#00003F是啊……\x02\x03",

            "#00000F好，已经确定方针了。\x02\x03",

            "『服务员』、『技师』、\x01",
            "『女仆』、『修女』……\x01",
            "我们要去寻找从事这些职业的女性。\x02",
        )
    )

    CloseMessageWindow()

    #C0300
    ChrTalk(
        0x15,
        (
            "等到参选者征集完毕后，\x01",
            "就可以马上开始\x01",
            "选秀活动了。\x02",
        )
    )

    CloseMessageWindow()

    #C0301
    ChrTalk(
        0x15,
        "拜托你们啦。\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    Sound(80, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0302
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "任务【协助慈善宴会】\x07\x00",
            "开始！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x198, 4)
    OP_29(0x8F, 0x1, 0x0)
    OP_4C(0x14, 0xFF)
    OP_4C(0x15, 0xFF)
    OP_93(0x14, 0x5A, 0x0)
    OP_93(0x15, 0x10E, 0x0)
    BeginChrThread(0x14, 0, 0, 0)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 1750, 0, 4000, 180)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_31_4E37 end

    def Function_32_570C(): pass

    label("Function_32_570C")

    EventBegin(0x0)
    Fade(500)
    OP_68(1560, 1500, 3500, 0)
    MoveCamera(39, 27, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(20900, 0)
    SetChrPos(0x101, 1810, 0, 3530, 0)
    SetChrPos(0x102, 620, 0, 3130, 0)
    SetChrPos(0x104, 1610, 0, 2310, 0)
    SetChrPos(0x103, 2860, 0, 2990, 0)
    SetChrPos(0x105, 2700, 0, 1650, 0)
    SetChrPos(0x109, 570, 0, 1600, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0x14, 0xFF)
    OP_4B(0x15, 0xFF)
    OP_93(0x14, 0xB4, 0x0)
    OP_93(0x15, 0xB4, 0x0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5A04")

    #C0303
    ChrTalk(
        0x14,
        "哦哦，是你们啊。\x02",
    )

    CloseMessageWindow()

    #C0304
    ChrTalk(
        0x15,
        "选秀活动的参选者找齐了吗？\x02",
    )

    CloseMessageWindow()

    #C0305
    ChrTalk(
        0x15,
        (
            "拜托你们征召的是从事\x01",
            "『服务员』、『技师』、『女仆』、\x01",
            "『修女』这四种工作的职业女性。\x02",
        )
    )

    CloseMessageWindow()

    #C0306
    ChrTalk(
        0x101,
        (
            "#00000F嗯，已经交涉完毕。\x02\x03",

            "在活动开始之前，\x01",
            "通知她们一声就行了。\x02",
        )
    )

    CloseMessageWindow()

    #C0307
    ChrTalk(
        0x15,
        "哦哦，那太好了！\x02",
    )

    CloseMessageWindow()

    #C0308
    ChrTalk(
        0x15,
        (
            "钢琴演奏很快\x01",
            "就要结束了。\x02",
        )
    )

    CloseMessageWindow()

    #C0309
    ChrTalk(
        0x15,
        (
            "呼，总算赶上了！\x01",
            "这样一来，终于可以举办了！\x02",
        )
    )

    CloseMessageWindow()

    #C0310
    ChrTalk(
        0x102,
        "#00109F呵呵，太好了。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x14, 0x15, 500)

    #C0311
    ChrTalk(
        0x14,
        (
            "唔，洛依这次\x01",
            "真是很努力。\x02",
        )
    )

    CloseMessageWindow()

    #C0312
    ChrTalk(
        0x14,
        (
            "一想到这个没干劲的孙子\x01",
            "终于成长起来了，\x01",
            "我就感慨良多啊。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x15, 0x14, 500)

    #C0313
    ChrTalk(
        0x15,
        "啧，什么话嘛……\x02",
    )

    CloseMessageWindow()
    OP_93(0x15, 0xB4, 0x1F4)

    #C0314
    ChrTalk(
        0x15,
        (
            "总之，\x01",
            "这就开始选秀活动吧。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_59E1():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_59E1)

    #C0315
    ChrTalk(
        0x15,
        "你们准备好了吗？\x02",
    )

    CloseMessageWindow()
    Jump("loc_5A3B")

    label("loc_5A04")


    #C0316
    ChrTalk(
        0x15,
        (
            "总之，\x01",
            "这就开始选秀活动吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0317
    ChrTalk(
        0x15,
        "你们准备好了吗？\x02",
    )

    CloseMessageWindow()

    label("loc_5A3B")

    Call(0, 33)
    OP_4C(0x14, 0xFF)
    OP_4C(0x15, 0xFF)
    OP_93(0x14, 0x5A, 0x0)
    OP_93(0x15, 0x10E, 0x0)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 1750, 0, 4000, 180)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_32_570C end

    def Function_33_5A80(): pass

    label("Function_33_5A80")

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
            "准备好了\x01",        # 0
            "还没准备好\x01",      # 1
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
        (0, "loc_5AE4"),
        (1, "loc_5AEC"),
        (SWITCH_DEFAULT, "loc_5B63"),
    )


    label("loc_5AE4")

    Call(0, 34)
    Jump("loc_5B63")

    label("loc_5AEC")


    #C0318
    ChrTalk(
        0x101,
        (
            "#00006F能再稍等一下吗？\x01",
            "还没有做好心理准备……\x02",
        )
    )

    CloseMessageWindow()

    #C0319
    ChrTalk(
        0x15,
        "喂喂，拜托快点啦。\x02",
    )

    CloseMessageWindow()

    #C0320
    ChrTalk(
        0x15,
        (
            "准备好了以后，\x01",
            "就再来找我吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x19A, 0)
    Jump("loc_5B63")

    label("loc_5B63")

    Return()

    # Function_33_5A80 end

    def Function_34_5B64(): pass

    label("Function_34_5B64")


    #C0321
    ChrTalk(
        0x101,
        (
            "#00000F嗯，没问题。\x02\x03",

            "那我们这就\x01",
            "联络参选者了。\x02",
        )
    )

    CloseMessageWindow()

    #C0322
    ChrTalk(
        0x15,
        "嗯，拜托你们啦。\x02",
    )

    CloseMessageWindow()

    #C0323
    ChrTalk(
        0x104,
        (
            "#00309F呀～终于要开始了，\x01",
            "真令人期待啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0324
    ChrTalk(
        0x103,
        (
            "#00211F兰迪前辈真是\x01",
            "很关注这件事啊。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x14, 0x15, 500)

    #C0325
    ChrTalk(
        0x14,
        (
            "好，我现在就去\x01",
            "准备会场吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0326
    ChrTalk(
        0x14,
        (
            "洛依，选秀活动\x01",
            "就交给你主持了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x15, 0x14, 500)

    #C0327
    ChrTalk(
        0x15,
        "嗯，放心交给我吧，爷爷！\x02",
    )

    CloseMessageWindow()

    #C0328
    ChrTalk(
        0x105,
        (
            "#10302F总之，先祝愿\x01",
            "这活动取得圆满成功吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0329
    ChrTalk(
        0x102,
        (
            "#00102F呵呵，机会难得，\x01",
            "就放松一下心情吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0330
    ChrTalk(
        0x109,
        "#10109F嗯，是呀！\x02",
    )

    CloseMessageWindow()

    #C0331
    ChrTalk(
        0x101,
        (
            "#00002F我们也赶快联络参选者，\x01",
            "然后进入会场吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    StopBGM(0xFA0)
    OP_0D()
    WaitBGM()
    SetScenarioFlags(0x22, 1)
    NewScene("c1120", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_34_5B64 end

    def Function_35_5D41(): pass

    label("Function_35_5D41")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(1560, 1500, 3500, 0)
    MoveCamera(39, 27, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(20900, 0)
    SetChrPos(0x101, 1810, 0, 3530, 0)
    SetChrPos(0x102, 620, 0, 3130, 0)
    SetChrPos(0x104, 1610, 0, 2310, 0)
    SetChrPos(0x103, 2860, 0, 2990, 0)
    SetChrPos(0x105, 2700, 0, 1650, 0)
    SetChrPos(0x109, 570, 0, 1600, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0x14, 0xFF)
    OP_4B(0x15, 0xFF)
    OP_93(0x14, 0xB4, 0x0)
    OP_93(0x15, 0xB4, 0x0)
    FadeToBright(1000, 0)
    OP_0D()

    #C0332
    ChrTalk(
        0x15,
        (
            "托你们的福，\x01",
            "选秀活动圆满成功！\x02",
        )
    )

    CloseMessageWindow()

    #C0333
    ChrTalk(
        0x15,
        (
            "多亏你们\x01",
            "征召到了参选者，\x01",
            "真是太谢谢啦！\x02",
        )
    )

    CloseMessageWindow()

    #C0334
    ChrTalk(
        0x101,
        "#00002F哈哈，不客气。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 4)), scpexpr(EXPR_END)), "loc_6094")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 1)), scpexpr(EXPR_END)), "loc_5F35")

    #C0335
    ChrTalk(
        0x102,
        (
            "#00104F呵呵，我们也\x01",
            "玩得很开心。\x02\x03",

            "#00102F没想到还能\x01",
            "拿到特别奖……\x02",
        )
    )

    CloseMessageWindow()

    #C0336
    ChrTalk(
        0x109,
        (
            "#10109F对艾莉小姐来说，\x01",
            "这是理所当然的结果啦！\x02",
        )
    )

    CloseMessageWindow()

    #C0337
    ChrTalk(
        0x103,
        "#00202F确实很潇洒。\x02",
    )

    CloseMessageWindow()
    OP_29(0x8F, 0x1, 0xE)
    Jump("loc_608F")

    label("loc_5F35")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 2)), scpexpr(EXPR_END)), "loc_5FE9")

    #C0338
    ChrTalk(
        0x103,
        (
            "#00204F……我们也\x01",
            "玩得很开心。\x02\x03",

            "#00202F没想到竟然\x01",
            "能拿到特别奖……\x02",
        )
    )

    CloseMessageWindow()

    #C0339
    ChrTalk(
        0x102,
        (
            "#00109F呵呵，对缇欧来说，\x01",
            "这是理所当然的结果嘛。\x02",
        )
    )

    CloseMessageWindow()

    #C0340
    ChrTalk(
        0x109,
        (
            "#10109F是啊！\x01",
            "缇欧好可爱哦～\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x8F, 0x1, 0xF)
    Jump("loc_608F")

    label("loc_5FE9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 3)), scpexpr(EXPR_END)), "loc_608F")

    #C0341
    ChrTalk(
        0x109,
        (
            "#10104F我们也玩得非常开心。\x02\x03",

            "#10100F真是完全没想到\x01",
            "能拿到特别奖呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0342
    ChrTalk(
        0x103,
        "#00204F对诺艾尔小姐来说，这是理所当然的结果。\x02",
    )

    CloseMessageWindow()

    #C0343
    ChrTalk(
        0x102,
        "#00109F确实很潇洒呢。\x02",
    )

    CloseMessageWindow()
    OP_29(0x8F, 0x1, 0x10)

    label("loc_608F")

    Jump("loc_6227")

    label("loc_6094")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 1)), scpexpr(EXPR_END)), "loc_611C")

    #C0344
    ChrTalk(
        0x102,
        (
            "#00102F呵呵，我们也\x01",
            "玩得很开心。\x02",
        )
    )

    CloseMessageWindow()

    #C0345
    ChrTalk(
        0x109,
        (
            "#10106F艾莉小姐差点\x01",
            "就能拿奖了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0346
    ChrTalk(
        0x103,
        (
            "#00202F嗯，毕竟没穿制服，\x01",
            "这也没办法。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6227")

    label("loc_611C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 2)), scpexpr(EXPR_END)), "loc_61A2")

    #C0347
    ChrTalk(
        0x103,
        (
            "#00202F……我们也\x01",
            "玩得很开心。\x02",
        )
    )

    CloseMessageWindow()

    #C0348
    ChrTalk(
        0x102,
        (
            "#00102F缇欧差点\x01",
            "就能拿奖了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0349
    ChrTalk(
        0x109,
        (
            "#10106F不过，毕竟没穿制服，\x01",
            "这也没办法啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6227")

    label("loc_61A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 3)), scpexpr(EXPR_END)), "loc_6227")

    #C0350
    ChrTalk(
        0x109,
        (
            "#10100F我们也\x01",
            "玩得非常开心。\x02",
        )
    )

    CloseMessageWindow()

    #C0351
    ChrTalk(
        0x103,
        (
            "#00202F诺艾尔小姐差点\x01",
            "就能拿奖了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0352
    ChrTalk(
        0x102,
        (
            "#00102F呵呵，毕竟没穿制服，\x01",
            "这也没办法啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6227")


    #C0353
    ChrTalk(
        0x14,
        (
            "市民们放松了心情，\x01",
            "选秀活动后还募集到了\x01",
            "不少支持复兴的捐款。\x02",
        )
    )

    CloseMessageWindow()

    #C0354
    ChrTalk(
        0x14,
        (
            "今天真是不得不表扬洛依\x01",
            "这一时兴起而想到的主意啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0355
    ChrTalk(
        0x15,
        (
            "啧，才不是一时兴起呢，\x01",
            "该说是个金点子才对。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0356
    ChrTalk(
        0x15,
        (
            "对了，机会难得，\x01",
            "就把这个\x01",
            "送给你们吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0357
    ChrTalk(
        0x15,
        (
            "也可以算是象征着\x01",
            "优胜的纪念品。\x01",
            "不介意的话，还请收下吧。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x1, 0x9)"), scpexpr(EXPR_END)), "loc_63A9")
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0358
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x76),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x76, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_6508")

    label("loc_63A9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x1, 0xA)"), scpexpr(EXPR_END)), "loc_6402")
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0359
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x72),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x72, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_6508")

    label("loc_6402")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x1, 0xB)"), scpexpr(EXPR_END)), "loc_645B")
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0360
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x6E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x6E, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_6508")

    label("loc_645B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x1, 0xC)"), scpexpr(EXPR_END)), "loc_64B4")
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0361
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x82),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x82, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_6508")

    label("loc_64B4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x1, 0xD)"), scpexpr(EXPR_END)), "loc_6508")
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0362
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x66),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x66, 1)
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_6508")


    #C0363
    ChrTalk(
        0x101,
        (
            "#00005F可以收下吗？\x01",
            "真是非常感谢。\x02",
        )
    )

    CloseMessageWindow()

    #C0364
    ChrTalk(
        0x104,
        (
            "#00309F哈哈，不管怎么说，\x01",
            "这次真是玩得很开心。\x02",
        )
    )

    CloseMessageWindow()

    #C0365
    ChrTalk(
        0x105,
        "#10302F真希望以后还有这样的活动啊。\x02",
    )

    CloseMessageWindow()

    #C0366
    ChrTalk(
        0x101,
        (
            "#00004F嗯，是啊。\x02\x03",

            "#00000F好，那我们\x01",
            "就先告辞了。\x02",
        )
    )

    CloseMessageWindow()

    #C0367
    ChrTalk(
        0x14,
        "嗯，谢谢了。\x02",
    )

    CloseMessageWindow()

    #C0368
    ChrTalk(
        0x15,
        (
            "如果以后有什么事，\x01",
            "还要再麻烦你们哦！\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0369
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "任务【协助慈善宴会】\x07\x00",
            "完成！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_29(0x8F, 0x1, 0x11)
    OP_29(0x8F, 0x4, 0x10)
    OP_4C(0x14, 0xFF)
    OP_4C(0x15, 0xFF)
    OP_93(0x14, 0x5A, 0x0)
    OP_93(0x15, 0x10E, 0x0)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 1750, 0, 4000, 180)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_35_5D41 end

    def Function_36_6699(): pass

    label("Function_36_6699")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0370
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "克洛斯贝尔市民会馆\x01",
            "　　　接待室　　　\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sound(807, 0, 100, 0)
    SetChrName("")

    #A0371
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "门上着锁。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)
    Return()

    # Function_36_6699 end

    def Function_37_6719(): pass

    label("Function_37_6719")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0372
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "克洛斯贝尔市民会馆\x01",
            "　各设施联络处　\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_67A5")

    #C0373
    ChrTalk(
        0x101,
        (
            "#00000F似乎没必要\x01",
            "进入这里啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_67A5")

    TalkEnd(0xFF)
    Return()

    # Function_37_6719 end

    def Function_38_67A9(): pass

    label("Function_38_67A9")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0374
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "　　　　　　　 『圣徒的祈祷』\x01",
            "　　　　　  马格纳斯·海克特作品\x01",
            "　　　　　　　　　　　　　　　　　　　\x01",
            "　 Ｓ１１３４，雕刻家马格纳斯·海克特为了\x01",
            " 　 庆祝自治州的创立，于晚年创作的杰作。\x01",
            "　 　 在旧市政厅建成后，作为本厅的象征\x01",
            "　　　 而长年展示于此，深受市民所喜爱。\x01",
            "　　　　　　　　　　　　　　　　　　　\x01",
            "　　　 Ｓ１２０４，市政厅转移至新场所，\x01",
            " 　  此作品继续留存在此，由市民会馆接管。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_38_67A9 end

    def Function_39_6966(): pass

    label("Function_39_6966")

    EventBegin(0x1)
    SetChrName("")

    #A0375
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "从会场方向传来了\x01",
            "激烈的论战声……\x02\x03",

            "还是不要进去打扰了。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, -13650, 4000, 12700, 225)
    EventEnd(0x4)
    Return()

    # Function_39_6966 end

    SaveToFile()

Try(main)
