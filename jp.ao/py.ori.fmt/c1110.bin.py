from ScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "受付嬢シオン",           # 1
        "クリップ主任",           # 2
        "運送員",                 # 3
        "貿易商リゼロ",           # 4
        "市民",                   # 5
        "市民",                   # 6
        "市民",                   # 7
        "市民",                   # 8
        "ボンド",                 # 9
        "クレイユ",               # 10
        "サニータ",               # 11
        "マリー",                 # 12
        "モルス老人",             # 13
        "ロイ",                   # 14
        "アルム",                 # 15
        "エアリー",               # 16
        "マーガレット夫人",       # 17
        "クロマ",                 # 18
        "オットー",               # 19
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
        "Function_6_1647",         # 06, 6
        "Function_7_16C4",         # 07, 7
        "Function_8_1727",         # 08, 8
        "Function_9_1747",         # 09, 9
        "Function_10_175A",        # 0A, 10
        "Function_11_1984",        # 0B, 11
        "Function_12_25F4",        # 0C, 12
        "Function_13_26D1",        # 0D, 13
        "Function_14_291A",        # 0E, 14
        "Function_15_29BC",        # 0F, 15
        "Function_16_2A71",        # 10, 16
        "Function_17_2AC4",        # 11, 17
        "Function_18_2AFA",        # 12, 18
        "Function_19_2B77",        # 13, 19
        "Function_20_308E",        # 14, 20
        "Function_21_310C",        # 15, 21
        "Function_22_316A",        # 16, 22
        "Function_23_31CC",        # 17, 23
        "Function_24_3417",        # 18, 24
        "Function_25_36A9",        # 19, 25
        "Function_26_370D",        # 1A, 26
        "Function_27_374D",        # 1B, 27
        "Function_28_5170",        # 1C, 28
        "Function_29_5746",        # 1D, 29
        "Function_30_5D83",        # 1E, 30
        "Function_31_5E79",        # 1F, 31
        "Function_32_6944",        # 20, 32
        "Function_33_6D76",        # 21, 33
        "Function_34_6E84",        # 22, 34
        "Function_35_70E9",        # 23, 35
        "Function_36_7C1D",        # 24, 36
        "Function_37_7CAB",        # 25, 37
        "Function_38_7D47",        # 26, 38
        "Function_39_7F2A",        # 27, 39
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_AA8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9F5")

    #C0001
    ChrTalk(
        0x8,
        (
            "職員で手分けして、\x01",
            "戒厳令下の騒動での市民の\x01",
            "安否を確認したのですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x8,
        (
            "騒ぎに巻き込まれて\x01",
            "軽傷を負った市民十数名以外は、\x01",
            "ほとんど被害がなかったようです。\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0x8,
        (
            "治療が必要な方々への\x01",
            "救急車の手配もすみましたし……\x01",
            "ひとまずこれで安心ですね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_AA3")

    label("loc_9F5")


    #C0004
    ChrTalk(
        0x8,
        (
            "戒厳令下の騒動では、\x01",
            "軽傷を負った市民十数名以外は、\x01",
            "ほとんど被害がなかったようです。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x8,
        (
            "治療が必要な方々への\x01",
            "救急車の手配もすみましたし……\x01",
            "ひとまずこれで安心ですね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AA3")

    Jump("loc_1643")

    label("loc_AA8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_BE7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B5C")

    #C0006
    ChrTalk(
        0x8,
        (
            "現在、市民会館では\x01",
            "ご自宅に戻れない市民の方々の\x01",
            "受け入れ態勢をとっています。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x8,
        (
            "なにかお困り事などございましたら\x01",
            "ご遠慮なくお申しつけ下さいませ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_BE2")

    label("loc_B5C")


    #C0008
    ChrTalk(
        0x8,
        (
            "市民会館にも、食料品や毛布など\x01",
            "緊急時の備えがございます。\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x8,
        (
            "なにかお困り事などございましたら\x01",
            "ご遠慮なくお申しつけ下さいませ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BE2")

    Jump("loc_1643")

    label("loc_BE7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_C65")

    #C0010
    ChrTalk(
        0x8,
        (
            "万歳を唱和する声が、\x01",
            "ここにもはっきり届いてきます。\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x8,
        (
            "少し怖い気がするのは\x01",
            "どうしてなんでしょうかね……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1643")

    label("loc_C65")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_D02")

    #C0012
    ChrTalk(
        0x8,
        (
            "本日はチャリティイベントへの\x01",
            "ご来場ありがとうございます。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x8,
        (
            "ぜひ参加されたいという\x01",
            "企画等ございましたら\x01",
            "どうぞお問い合わせくださいね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1643")

    label("loc_D02")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_E8C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E36")

    #C0014
    ChrTalk(
        0x8,
        (
            "マインツを襲った武装集団について、\x01",
            "市民の皆さんから非常に多くの\x01",
            "お問い合わせを頂いているのですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x8,
        (
            "犯人や事件の目的の話になると、\x01",
            "私にはお答えようのないことなので\x01",
            "すごく困ってしまいます。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x8,
        (
            "帝国の仕業と言う方も多いのですが……\x01",
            "果たして真実はどこにあるんでしょうか？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_E87")

    label("loc_E36")


    #C0017
    ChrTalk(
        0x8,
        (
            "帝国の仕業と言う方も多いのですが……\x01",
            "果たして真実はどこにあるんでしょうか？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E87")

    Jump("loc_1643")

    label("loc_E8C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_F35")

    #C0018
    ChrTalk(
        0x8,
        (
            "只今、左手の多目的ホールにて\x01",
            "国家独立をテーマとした\x01",
            "市民フォーラムが開催中です。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x8,
        (
            "どなたでも傍聴は可能ですので\x01",
            "宜しければ、お立ち寄り下さいませ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1643")

    label("loc_F35")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_FA9")

    #C0020
    ChrTalk(
        0x8,
        (
            "そうですね、当日でも\x01",
            "傍聴自体は可能なのですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x8,
        (
            "あいにく座席の方は\x01",
            "埋まっておりまして……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1643")

    label("loc_FA9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1050")

    #C0022
    ChrTalk(
        0x8,
        (
            "いらっしゃいませ。\x01",
            "クロスベル市民会館へようこそ。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x8,
        (
            "市民会館のご利用をお考えの方は\x01",
            "まずは受付脇にある、こちらの\x01",
            "お申し込み表にご記入くださいね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1643")

    label("loc_1050")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_124C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1185")

    #C0024
    ChrTalk(
        0x8,
        (
            "国家独立の提唱を受け、\x01",
            "ここで勉強会を開きたいという\x01",
            "お問い合わせが増えておりまして。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x8,
        (
            "そんな声を受けて、市と通信社が\x01",
            "共同で明後日に市民フォーラムを\x01",
            "開催することになったんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x8,
        (
            "現在も色々と調整中ですが、\x01",
            "きっと皆さんにとって有意義な\x01",
            "フォーラムが開催できると思います。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1247")

    label("loc_1185")


    #C0027
    ChrTalk(
        0x8,
        (
            "明後日、この市民会館で\x01",
            "クロスベルの国家独立をテーマとした\x01",
            "市民フォーラムを開催する予定です。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x8,
        (
            "現在も色々と調整中ですが、\x01",
            "きっと皆さんにとって有意義な\x01",
            "フォーラムが開催できると思います。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1247")

    Jump("loc_1643")

    label("loc_124C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_12F2")

    #C0029
    ChrTalk(
        0x8,
        (
            "も、申し訳ございません。\x01",
            "以前から告示は\x01",
            "していたと思うのですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x8,
        (
            "安全保障の観点からどうしても\x01",
            "一般の方をお通しするわけには\x01",
            "いかないんです。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1643")

    label("loc_12F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_144B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13C2")

    #C0031
    ChrTalk(
        0x8,
        (
            "各国の首脳が、とうとう\x01",
            "クロスベル入りを果たしましたね。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x8,
        (
            "午後からはそれぞれで\x01",
            "行動するという話も聞きましたが……\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x8,
        (
            "皆さん、どういった\x01",
            "お時間を過ごされるんでしょうかね？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1446")

    label("loc_13C2")


    #C0034
    ChrTalk(
        0x8,
        (
            "首脳たちは、午後からはそれぞれで\x01",
            "行動するという話も聞きましたが……\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x8,
        (
            "皆さん、どういった\x01",
            "お時間を過ごされるんでしょうかね？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1446")

    Jump("loc_1643")

    label("loc_144B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_14F8")

    #C0036
    ChrTalk(
        0x8,
        (
            "通商会議とその前後の期間中は\x01",
            "市民会館のご利用を\x01",
            "ご遠慮いただいているんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x8,
        (
            "ここはオルキスタワーにも近いですし、\x01",
            "何かあったらそれこそ事ですからね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1643")

    label("loc_14F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_1637")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6A, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_158C")

    #C0038
    ChrTalk(
        0x8,
        (
            "皆さん、本日は調査の方、\x01",
            "どうもありがとうございました。\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x8,
        (
            "今後ともクロスベル市民会館を\x01",
            "何卒よろしくお願いします。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1632")

    label("loc_158C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6A, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_1632")

    #C0040
    ChrTalk(
        0x8,
        (
            "皆さんにお願いしたいのは\x01",
            "計３箇所の不審住戸、および\x01",
            "消息不明の前所有者の確認です。\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x8,
        (
            "全て確認されましたら、\x01",
            "こちらの方に報告をお願いします。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1632")

    label("loc_1632")

    Jump("loc_1643")

    label("loc_1637")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_1643")
    Call(0, 10)

    label("loc_1643")

    TalkEnd(0x8)
    Return()

    # Function_5_897 end

    def Function_6_1647(): pass

    label("Function_6_1647")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_16C0")

    #C0042
    ChrTalk(
        0xFE,
        (
            "いい物件が\x01",
            "みつかるといいですわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0xFE,
        (
            "できたら、お花がいっぱい\x01",
            "咲いている場所だと\x01",
            "いいのですけど……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16C0")

    TalkEnd(0xFE)
    Return()

    # Function_6_1647 end

    def Function_7_16C4(): pass

    label("Function_7_16C4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_1723")

    #C0044
    ChrTalk(
        0xFE,
        "大丈夫ですわ、お母様。\x02",
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0xFE,
        (
            "お父様なら、きっと良い部屋を\x01",
            "みつけてくれますわ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1723")

    TalkEnd(0xFE)
    Return()

    # Function_7_16C4 end

    def Function_8_1727(): pass

    label("Function_8_1727")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_1743")

    #C0046
    ChrTalk(
        0xFE,
        "にゃおん。\x02",
    )

    CloseMessageWindow()

    label("loc_1743")

    TalkEnd(0xFE)
    Return()

    # Function_8_1727 end

    def Function_9_1747(): pass

    label("Function_9_1747")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_1756")
    Call(0, 10)

    label("loc_1756")

    TalkEnd(0xFE)
    Return()

    # Function_9_1747 end

    def Function_10_175A(): pass

    label("Function_10_175A")

    OP_4B(0x10, 0xFF)
    OP_4B(0x8, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18BC")

    #C0047
    ChrTalk(
        0x10,
        (
            "ええ、できるだけ安い部屋を\x01",
            "探しているんですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x10,
        (
            "多少狭くてもいいので、\x01",
            "家族３人で暮らせる場所……\x01",
            "どこかないものでしょうか。\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x8,
        (
            "そうですね……\x01",
            "こういった資料もありますので、\x01",
            "確認してみてはいかがでしょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x8,
        (
            "たしか、数ヶ月前に\x01",
            "転出届けが受理された物件が\x01",
            "あったと思います。\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x10,
        (
            "ふむ、そんな物件が。\x01",
            "どれどれ……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_197B")

    label("loc_18BC")


    #C0052
    ChrTalk(
        0x10,
        (
            "ああ、それと……\x01",
            "ペット可の物件であることが\x01",
            "最低条件なんですが。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x8,
        (
            "ええ、その物件ならば\x01",
            "確かＯＫだったと思いますよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x10,
        (
            "おお、それはよかった！\x01",
            "でしたらすぐにでも\x01",
            "確認をしたいと……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_197B")

    OP_4C(0x10, 0xFF)
    OP_4C(0x8, 0xFF)
    Return()

    # Function_10_175A end

    def Function_11_1984(): pass

    label("Function_11_1984")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1B23")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A8A")

    #C0055
    ChrTalk(
        0xFE,
        (
            "今回の事件について、\x01",
            "市民に向けた公式な説明の場を\x01",
            "準備しているところです。\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0xFE,
        (
            "今後、起こりうる事態について\x01",
            "クロスベル市民たちも\x01",
            "説明を求めている事でしょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0xFE,
        (
            "各地の混乱もありますし、\x01",
            "早急に用意を進めないと\x01",
            "いけませんね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1B1E")

    label("loc_1A8A")


    #C0058
    ChrTalk(
        0xFE,
        (
            "今回の事件について、\x01",
            "市民に向けた公式な説明の場を\x01",
            "準備しているところです。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0xFE,
        (
            "各地の混乱もありますし、\x01",
            "早急に用意を進めないと\x01",
            "いけませんね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B1E")

    Jump("loc_25F0")

    label("loc_1B23")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_1CD5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C32")

    #C0060
    ChrTalk(
        0xFE,
        (
            "今回の件に関して、\x01",
            "大統領からは『戒厳令』としか\x01",
            "伝えられていませんでした。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0xFE,
        (
            "それがこのような事態……\x01",
            "備えの出来ていない方も\x01",
            "多数おられるはずです。\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0xFE,
        (
            "……今はとにかく収束を待って、\x01",
            "改めて市民たちの安全を\x01",
            "確認しなければいけませんね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1CD0")

    label("loc_1C32")


    #C0063
    ChrTalk(
        0xFE,
        (
            "このような事態……\x01",
            "備えの出来ていない方も\x01",
            "多数おられるはずです。\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0xFE,
        (
            "……今はとにかく収束を待って、\x01",
            "改めて市民たちの安全を\x01",
            "確認しなければいけませんね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1CD0")

    Jump("loc_25F0")

    label("loc_1CD5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_1DEC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D84")

    #C0065
    ChrTalk(
        0xFE,
        (
            "クロスベル独立国、\x01",
            "そして大統領の就任か……\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0xFE,
        (
            "こうなると、今後はもちろん\x01",
            "体制だって変わるだろうね。\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0xFE,
        "今日から１日１日が緊張の日々だよ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1DE7")

    label("loc_1D84")


    #C0068
    ChrTalk(
        0xFE,
        (
            "こうなると、今後はもちろん\x01",
            "体制だって変わるだろうね。\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0xFE,
        "今日から１日１日が緊張の日々だよ。\x02",
    )

    CloseMessageWindow()

    label("loc_1DE7")

    Jump("loc_25F0")

    label("loc_1DEC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1E40")

    #C0070
    ChrTalk(
        0xFE,
        (
            "さあさあ、本日は\x01",
            "チャリティイベントを\x01",
            "楽しんで行ってくださいね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_25F0")

    label("loc_1E40")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_2001")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F7A")

    #C0071
    ChrTalk(
        0xFE,
        (
            "市庁からは『目下解決に向けて\x01",
            "全力を挙げている』とだけ\x01",
            "通達を受けているんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0xFE,
        (
            "どうにも、色んなことが\x01",
            "見えなさ過ぎて、不安になるね。\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0xFE,
        (
            "ふむ、でも市の職員である僕らが\x01",
            "不安になってたんじゃ市民の皆さんは\x01",
            "もっと不安になってしまうからね。\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0xFE,
        "何とか気をしっかり持たないと。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1FFC")

    label("loc_1F7A")


    #C0075
    ChrTalk(
        0xFE,
        (
            "市の職員である僕らが\x01",
            "不安になってたんじゃ市民の皆さんは\x01",
            "もっと不安になってしまうからね。\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0xFE,
        "何とか気をしっかり持たないと。\x02",
    )

    CloseMessageWindow()

    label("loc_1FFC")

    Jump("loc_25F0")

    label("loc_2001")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2087")

    #C0077
    ChrTalk(
        0xFE,
        (
            "今の所、市民フォーラムは\x01",
            "つつがなく進行しているようだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0xFE,
        (
            "このまま、特に騒ぎが\x01",
            "起こらないことを祈っているよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_25F0")

    label("loc_2087")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_20DA")

    #C0079
    ChrTalk(
        0xFE,
        (
            "ううむ、何とかしてキーボードを\x01",
            "うまく操れるようになりたいなぁ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_25F0")

    label("loc_20DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_225C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_21BE")

    #C0080
    ChrTalk(
        0xFE,
        (
            "最近、総務二課でも\x01",
            "導力メールなるものを\x01",
            "徐々に使い始めているんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0xFE,
        (
            "この年になって\x01",
            "新しい物事に挑戦するのは\x01",
            "なかなか大変だね。\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0xFE,
        (
            "特にあのキーボードという\x01",
            "入力装置は恐ろしく難敵だよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2257")

    label("loc_21BE")


    #C0083
    ChrTalk(
        0xFE,
        (
            "あとディスプレイを見ると\x01",
            "どうにも目が疲れてくるんだよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0xFE,
        (
            "やはり紙媒体の方が……\x01",
            "ってこんなことを言っていると\x01",
            "周りから取り残されるんだろうね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2257")

    Jump("loc_25F0")

    label("loc_225C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_22FB")

    #C0085
    ChrTalk(
        0xFE,
        (
            "ここが市民会館になってから\x01",
            "忙しさが倍増した気がするね。\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0xFE,
        (
            "市民フォーラムの後には\x01",
            "住民投票の準備もあるし……\x01",
            "最近は何だか山場が続くなあ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_25F0")

    label("loc_22FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2342")

    #C0087
    ChrTalk(
        0xFE,
        (
            "えっと、彼女の言う通り\x01",
            "保安上の問題が一番でして……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_25F0")

    label("loc_2342")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_23E7")

    #C0088
    ChrTalk(
        0xFE,
        (
            "除幕式の様子は窓から\x01",
            "見させてもらったんだけど、\x01",
            "いやぁ、まさに壮観だったね。\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0xFE,
        (
            "ついに市庁が移転したんだなって、\x01",
            "ようやく実感できた気がするよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_25F0")

    label("loc_23E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2460")

    #C0090
    ChrTalk(
        0xFE,
        (
            "ええ、住民登録なら市庁に行かずとも\x01",
            "こちらで手続きできますよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0xFE,
        "１階の受付にてお申し付けください。\x02",
    )

    CloseMessageWindow()
    Jump("loc_25F0")

    label("loc_2460")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_2543")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12E, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2480")
    Call(0, 13)
    ClearChrFlags(0x9, 0x10)
    Jump("loc_253E")

    label("loc_2480")


    #C0092
    ChrTalk(
        0xFE,
        (
            "当日キャンセルの理由の大半は\x01",
            "どうやらこの雨にあるみたいでね。\x01",
            "リゼロさんが怒るのも無理はないよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0xFE,
        (
            "ふむ、例えばキャンセル料でも\x01",
            "取る仕組みにしていれば、\x01",
            "こうはならなかったのかもね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_253E")

    Jump("loc_25F0")

    label("loc_2543")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_25F0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2566")
    Call(0, 12)
    SetScenarioFlags(0x0, 1)
    ClearChrFlags(0x9, 0x10)
    Jump("loc_25F0")

    label("loc_2566")


    #C0094
    ChrTalk(
        0xFE,
        (
            "ふう、何だって移転作業の\x01",
            "事務処理が全て総務二課に\x01",
            "回ってくるかなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0xFE,
        (
            "こんなのは各自で\x01",
            "やるべきことだと思うけど……\x01",
            "ぶつぶつ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_25F0")

    TalkEnd(0xFE)
    Return()

    # Function_11_1984 end

    def Function_12_25F4(): pass

    label("Function_12_25F4")

    OP_4B(0xA, 0xFF)
    OP_4B(0x9, 0xFF)

    #C0096
    ChrTalk(
        0xA,
        (
            "えっと、それじゃ配達票の\x01",
            "確認をお願いしてもいいですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0x9,
        "ああうん、どれどれ……\x02",
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x9,
        (
            "うん、これで間違いないよ。\x01",
            "では配達の方はよろしく頼んだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0xA,
        "ええ、任せておいてください。\x02",
    )

    CloseMessageWindow()
    OP_4C(0xA, 0xFF)
    OP_4C(0x9, 0xFF)
    ClearChrFlags(0x9, 0x10)
    ClearChrFlags(0xA, 0x10)
    SetScenarioFlags(0x0, 1)
    SetScenarioFlags(0x0, 2)
    Return()

    # Function_12_25F4 end

    def Function_13_26D1(): pass

    label("Function_13_26D1")

    OP_4B(0xB, 0xFF)
    OP_4B(0x9, 0xFF)

    #C0100
    ChrTalk(
        0x9,
        (
            "そろそろセミナーの\x01",
            "開始時間ですが……\x01",
            "予定を少し遅らせますか？\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0xB,
        (
            "む、無論だよ。\x01",
            "定員の半分にも満たないんじゃ\x01",
            "始めたって意味がないからね。\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0xB,
        (
            "しかし当日キャンセルだなんて……\x01",
            "これだから素人はイヤなんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0xB,
        (
            "こんなことで、ビジネスチャンスが\x01",
            "掴めると思ったら大間違いだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0x9,
        "は、はあ……\x02",
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0xB,
        (
            "と、とにかく、\x01",
            "もう少しだけ粘らせてもらうよ。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x134, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2904")

    #C0106
    ChrTalk(
        0x102,
        (
            "#00105F（ねえ、ロイド。\x01",
            "  この人ってもしかして……）\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0x101,
        (
            "#00003F（ああ、例の教団事件の\x01",
            "  グノーシス被害者の一人だな。）\x02\x03",

            "#00000F（何だか大変そうだけど、\x01",
            "  ともかく元気そうで良かったよ。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2904")

    SetScenarioFlags(0x12E, 5)
    ClearChrFlags(0xB, 0x10)
    ClearChrFlags(0x9, 0x10)
    OP_4C(0xB, 0xFF)
    OP_4C(0x9, 0xFF)
    Return()

    # Function_13_26D1 end

    def Function_14_291A(): pass

    label("Function_14_291A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_29B8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_293D")
    Call(0, 12)
    ClearChrFlags(0xA, 0x10)
    Jump("loc_29B8")

    label("loc_293D")


    #C0108
    ChrTalk(
        0xFE,
        (
            "えっと、こっちの荷物が\x01",
            "総務一課宛てで、\x01",
            "こっちが財務課宛てか……\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0xFE,
        (
            "新市庁はすぐ近くだし、\x01",
            "さっさと運んでくるかな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_29B8")

    TalkEnd(0xFE)
    Return()

    # Function_14_291A end

    def Function_15_29BC(): pass

    label("Function_15_29BC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_2A6D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12E, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_29DF")
    Call(0, 13)
    ClearChrFlags(0xB, 0x10)
    Jump("loc_2A6D")

    label("loc_29DF")


    #C0110
    ChrTalk(
        0xFE,
        (
            "ふむむ、これでは参加費を集めても\x01",
            "施設利用料にさえ満たないじゃないか。\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0xFE,
        (
            "何としてでも、また新たに\x01",
            "元手を増やさないといけないんだが……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A6D")

    TalkEnd(0xFE)
    Return()

    # Function_15_29BC end

    def Function_16_2A71(): pass

    label("Function_16_2A71")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2AC0")

    #C0112
    ChrTalk(
        0xFE,
        (
            "あの、こちらでも住民登録の\x01",
            "手続きができると聞いたんですが……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2AC0")

    TalkEnd(0xFE)
    Return()

    # Function_16_2A71 end

    def Function_17_2AC4(): pass

    label("Function_17_2AC4")

    TalkBegin(0xFE)

    #C0113
    ChrTalk(
        0xFE,
        (
            "百貨店で働いている\x01",
            "お母さんが心配です……\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_17_2AC4 end

    def Function_18_2AFA(): pass

    label("Function_18_2AFA")

    TalkBegin(0xFE)

    #C0114
    ChrTalk(
        0xFE,
        (
            "ウムム……なんたることだ。\x01",
            "よもやこんな事態になろうとは……\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0xFE,
        (
            "ディーター大統領……\x01",
            "私は彼を信じていたのだが。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_18_2AFA end

    def Function_19_2B77(): pass

    label("Function_19_2B77")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CC, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_301C")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x84, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2F65")

    #C0116
    ChrTalk(
        0xFE,
        (
            "あら、あなたたち……\x01",
            "確か警察の人ではなかったかしら。\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0xFE,
        "その節はお世話になったわね。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2C82")

    #C0118
    ChrTalk(
        0x101,
        (
            "#00005Fあっ……もしかして、\x01",
            "ピエール副局長の奥さん……？\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0x105,
        (
            "#10302Fフフ、お久しぶりマダム。\x01",
            "市民会館に避難してたんだね？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2CF0")

    label("loc_2C82")


    #C0120
    ChrTalk(
        0x101,
        (
            "#00005Fあっ、もしかして\x01",
            "ピエール副局長の奥さん……？\x02\x03",

            "#00001Fえっと……\x01",
            "市民会館に避難していたんですか？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2CF0")


    #C0121
    ChrTalk(
        0xFE,
        (
            "ええ、そうだけど……\x01",
            "……その、主人を見なかった？\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0xFE,
        (
            "オルキスタワーに行くと言ったきり、\x01",
            "戻ってこなくってね。\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0x103,
        (
            "#00200Fいえ、見てませんが……\x02\x03",

            "副局長は、一体何をしに\x01",
            "オルキスタワーへ？\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0xFE,
        (
            "さあ……\x01",
            "私もそれは聞いていないわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0xFE,
        (
            "まったく、あの人ったら\x01",
            "こんな時に余計な心配をかけて……\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0xFE,
        (
            "帰ってきたら、\x01",
            "こっぴどく叱ってやらないと。\x02",
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
            "#00000F……とりあえず、奥さんはここで\x01",
            "待っていてください。\x02\x03",

            "もしかしたらひょっこりと\x01",
            "戻ってくるかもしれませんし。\x02",
        )
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0xFE,
        (
            "……ええ、そうするわ。\x01",
            "もし見かけたら連絡をちょうだい。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3014")

    label("loc_2F65")


    #C0129
    ChrTalk(
        0xFE,
        (
            "うちの主人が、オルキスタワーに\x01",
            "行ったきり戻ってこないのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0xFE,
        (
            "まったく、あの人ったら\x01",
            "こんな時に余計な心配をかけて……\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0xFE,
        (
            "帰ってきたら、\x01",
            "こっぴどく叱ってやらないと。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3014")

    SetScenarioFlags(0x1CC, 2)
    Jump("loc_308A")

    label("loc_301C")


    #C0132
    ChrTalk(
        0xFE,
        (
            "まったく、あの人ったら\x01",
            "こんな時に余計な心配をかけて……\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0xFE,
        (
            "帰ってきたら、\x01",
            "こっぴどく叱ってやらないと。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_308A")

    TalkEnd(0xFE)
    Return()

    # Function_19_2B77 end

    def Function_20_308E(): pass

    label("Function_20_308E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3108")

    #C0134
    ChrTalk(
        0xFE,
        (
            "ちょっと、何で\x01",
            "オルキスタワーに行けないんだよ？\x02",
        )
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0xFE,
        (
            "タワー前の広場くらい\x01",
            "自由に出入りしてもいいだろう？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3108")

    TalkEnd(0xFE)
    Return()

    # Function_20_308E end

    def Function_21_310C(): pass

    label("Function_21_310C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3166")

    #C0136
    ChrTalk(
        0xFE,
        (
            "そーそー。\x01",
            "大体そんな話、急に言われても\x01",
            "こっちは聞いてないっていうかぁ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3166")

    TalkEnd(0xFE)
    Return()

    # Function_21_310C end

    def Function_22_316A(): pass

    label("Function_22_316A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_31C8")

    #C0137
    ChrTalk(
        0xFE,
        (
            "明日行われる市民フォーラム\x01",
            "とやらに参加したいのだが……\x01",
            "まだ空席はあるかね？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_31C8")

    TalkEnd(0xFE)
    Return()

    # Function_22_316A end

    def Function_23_31CC(): pass

    label("Function_23_31CC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3214")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x199, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x199, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x199, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x199, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3206")
    Call(0, 32)
    Return()

    label("loc_3206")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x198, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3214")
    Call(0, 29)
    Return()

    label("loc_3214")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_336A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_32E8")

    #C0138
    ChrTalk(
        0xFE,
        (
            "すまんな、君たち。\x01",
            "ロイが手間をかけさせるが……\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0xFE,
        (
            "ミスコンを開けるなら、\x01",
            "市民にとっても\x01",
            "いい息抜きになるじゃろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0xFE,
        (
            "どうか、がんばって\x01",
            "参加者を集めてきてくれたまえ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_3365")

    label("loc_32E8")


    #C0141
    ChrTalk(
        0xFE,
        (
            "ミスコンを開けるなら、\x01",
            "市民にとっても\x01",
            "いい息抜きになるじゃろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0xFE,
        (
            "どうか、がんばって\x01",
            "参加者を集めてきてくれたまえ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3365")

    Jump("loc_3413")

    label("loc_336A")


    #C0143
    ChrTalk(
        0xFE,
        (
            "市民たちも息抜きできたようだし、\x01",
            "復興支援の義援金への寄付も\x01",
            "ミスコンの後は随分集まっておる。\x02",
        )
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0xFE,
        (
            "ミスコンはロイのアイデアだったが……\x01",
            "ふふ、立派になりおったわい。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3413")

    TalkEnd(0xFE)
    Return()

    # Function_23_31CC end

    def Function_24_3417(): pass

    label("Function_24_3417")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_345F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x199, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x199, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x199, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x199, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3451")
    Call(0, 32)
    Return()

    label("loc_3451")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x198, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_345F")
    Call(0, 29)
    Return()

    label("loc_345F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3638")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_35A5")

    #C0145
    ChrTalk(
        0x15,
        (
            "あんたたちには、ミスコンに\x01",
            "参加してくれる“働く女性”を\x01",
            "スカウトしてきてほしいんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0x15,
        (
            "『ウェイトレス』『職人』\x01",
            "『メイド』『シスター』……\x01",
            "この４枠でおねがいするぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0x15,
        (
            "これらの人が参加してくれれば\x01",
            "コンテスト参加者の職業の\x01",
            "バランスがよくなるだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0x15,
        "どうか、よろしく頼んだぜ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_3633")

    label("loc_35A5")


    #C0149
    ChrTalk(
        0x15,
        (
            "『ウェイトレス』『職人』\x01",
            "『メイド』『シスター』……\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0x15,
        (
            "この４枠の“働く女性”を\x01",
            "スカウトしてきてくれ。\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0x15,
        "どうか、よろしく頼んだぜ。\x02",
    )

    CloseMessageWindow()

    label("loc_3633")

    Jump("loc_36A5")

    label("loc_3638")


    #C0152
    ChrTalk(
        0x15,
        (
            "おかげさまで\x01",
            "ミスコンは大成功だ！\x02",
        )
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0x15,
        (
            "あんたたちが参加者を\x01",
            "集めてくれたおかげだ、\x01",
            "どうもありがとうな！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_36A5")

    TalkEnd(0xFE)
    Return()

    # Function_24_3417 end

    def Function_25_36A9(): pass

    label("Function_25_36A9")

    TalkBegin(0xFE)

    #C0154
    ChrTalk(
        0xFE,
        "旧市街、この住所に父さんが……\x02",
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0xFE,
        (
            "やったね、エアリー！\x01",
            "後はここへ行って会うだけだよ。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_25_36A9 end

    def Function_26_370D(): pass

    label("Function_26_370D")

    TalkBegin(0xFE)

    #C0156
    ChrTalk(
        0xFE,
        (
            "ふふ、やっと居場所が分かって\x01",
            "よかったわね、アルム㈱\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_26_370D end

    def Function_27_374D(): pass

    label("Function_27_374D")

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
            "いらっしゃいませ。\x01",
            "クロスベル市民会館へようこそ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0158
    ChrTalk(
        0x8,
        (
            "ようこそお越しくださいました。\x01",
            "特務支援課の皆さんですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0x101,
        "#12P#00000Fええ、依頼の確認に来ました。\x02",
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0x102,
        (
            "#00102F新しいメンバー共々\x01",
            "また宜しくお願いしますね。\x02",
        )
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0x105,
        "#12P#10302Fよろしくね、お姉さん。\x02",
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0x109,
        "#12P#10100F宜しくお願いします。\x02",
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0x8,
        (
            "はい、こちらこそ\x01",
            "宜しくお願い致します。\x02",
        )
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0x101,
        (
            "#12P#00006F……でも、市民会館か。\x01",
            "何だか変な感じがするな。\x02",
        )
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0x109,
        (
            "#12P#10106Fええ、この建物が\x01",
            "市庁舎じゃなくなったなんて\x01",
            "やや実感に欠けますよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0x102,
        (
            "#00104Fふふ、新しい市庁舎は\x01",
            "今度完成する新市庁ビルの中に\x01",
            "先行して入ったから……\x02\x03",

            "#00100Fでも、ここにも一応、\x01",
            "市庁舎の“出張所”は残るの。\x02\x03",

            "そういう意味では、今後も変わらず\x01",
            "お役に立ってくれると思うわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0x109,
        "#12P#10103Fなるほど、そうだったんですか。\x02",
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0x8,
        (
            "はい、この受付でも\x01",
            "各種住民手続きなどの市の窓口業務は\x01",
            "引き続き行うことになっています。\x02",
        )
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0x8,
        (
            "……ただ、その辺りの告示が\x01",
            "市民の皆さんに浸透していないのか、\x01",
            "お問い合わせが非常に多い状況で……\x02",
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
            "も、申し訳ありません。\x01",
            "皆さんには関係のない話でしたね。\x02",
        )
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0x101,
        "#12P#00012Fい、いえ……大変そうですね。\x02",
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0x105,
        (
            "#12P#10302Fフフ、でも役人の考えることって\x01",
            "つまらないよね。\x02\x03",

            "僕なら歓楽街辺りを参考に\x01",
            "“大人の社交場”にしたんだけど。\x02\x03",

            "#10309F公僕が持て成すナイトクラブ……\x01",
            "特務支援課もきっと今まで以上に\x01",
            "引っ張りだこになったと思うよ？\x02",
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
            "#12P#00006F引っ張りだこって……\x01",
            "どんな支援要請だよ。\x02\x03",

            "#00001Fっていうか、\x01",
            "そもそも公務員が夜の仕事とか\x01",
            "ありえないから。\x02",
        )
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0x109,
        (
            "#6P#10112Fあ、あはは……\x01",
            "（ちょっと想像しちゃった。）\x02",
        )
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0x102,
        (
            "#00103Fコ、コホン……\x01",
            "それよりロイド、本題を忘れてない？\x02",
        )
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0x101,
        (
            "#12P#00011Fあ、ああ、そうだな。\x02\x03",

            "#00000Fえっと、すみません。\x01",
            "支援要請についてなんですが……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0177
    ChrTalk(
        0x8,
        "は、はい、ご説明しますね。\x02",
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0x8,
        (
            "――皆さんは『居住者変更届』\x01",
            "というものをご存知でしょうか。\x02",
        )
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0x8,
        (
            "これは引越しなどで\x01",
            "居住者が変更になった際に\x01",
            "市に提出して頂く届書なのですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0x8,
        (
            "実は先ごろ、この届書に\x01",
            "不審な名前の書かれてある物が\x01",
            "見つかったのです。\x02",
        )
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0x109,
        "#12P#10105F不審な名前、ですか？\x02",
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0x8,
        (
            "ええ……正確には\x01",
            "“市に登録されていない氏名”\x01",
            "ということになりますが。\x02",
        )
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0x8,
        (
            "いくつか見つかっているのですが、\x01",
            "いずれも市の住民・法人登録には\x01",
            "一切存在しない名称でした。\x02",
        )
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0x8,
        (
            "そこで、皆さんには\x01",
            "その不審な名前で届けられた\x01",
            "住戸の実態確認と……\x02",
        )
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0x8,
        (
            "さらに念のため、\x01",
            "元の居住者の状況確認を\x01",
            "行なって頂きたいのです。\x02",
        )
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0x101,
        (
            "#12P#00001Fなるほど、つまり\x01",
            "その不審な住戸の新旧居住者を\x01",
            "確認すればいいわけですね。\x02\x03",

            "#00003F仮に何らかの犯罪に関わっていたら\x01",
            "放っておくわけにはいかないし……\x02\x03",

            "#00000F確かに、その辺りは\x01",
            "一通り調査すべきですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0x102,
        (
            "#00103Fええ、そうね。\x02\x03",

            "#00100Fただ、その不審住戸の場所は\x01",
            "当然分かると思うのですが……\x02\x03",

            "元の居住者の所在については\x01",
            "市の方で把握しているんですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0x8,
        (
            "いえ、それがお一方だけは\x01",
            "転居届けを受理しているので\x01",
            "分かるのですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0x8,
        (
            "それ以外の方については\x01",
            "一切把握できていない状況なんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0x105,
        (
            "#12P#10300Fなるほど、となると\x01",
            "捜索活動が必要というわけだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0191
    ChrTalk(
        0x109,
        (
            "#12P#10100Fでも、まずはその不審住戸と\x01",
            "所在が判明している住民の調査を\x01",
            "済ませた方が良さそうですね。\x02\x03",

            "所在不明の住民にしても、\x01",
            "調査の過程で何らかのことが\x01",
            "分かって来るでしょうし。\x02",
        )
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0x101,
        (
            "#12P#00003Fああ、そうだな。\x02\x03",

            "#00000Fちなみに、それらの\x01",
            "リストのような物はありますか？\x02",
        )
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0x8,
        (
            "はい、届書の写しを\x01",
            "用意してあるのでご確認下さい。\x02",
        )
    )

    CloseMessageWindow()

    #C0194
    ChrTalk(
        0x101,
        "#12P#00000Fお預かりします。\x02",
    )

    CloseMessageWindow()
    OP_97(0x101, 0x0, 0x0, 0x258, 0x3E8, 0x0)
    Sleep(800)
    OP_93(0x101, 0xB4, 0x1F4)
    OP_97(0x101, 0x0, 0x0, 0xFFFFFDA8, 0x3E8, 0x0)
    Sleep(50)

    def lambda_4528():
        OP_93(0x101, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4528)

    def lambda_4535():
        OP_93(0x102, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4535)

    def lambda_4542():
        OP_93(0x109, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_4542)

    def lambda_454F():
        OP_93(0x105, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_454F)
    Sleep(300)

    #C0195
    ChrTalk(
        0x101,
        (
            "#5P#00000Fふむふむ、えっと……\x01",
            "問題の住戸は全部で３箇所か。\x02\x03",

            "まず住宅街に１軒……\x01",
            "場所は、エリィなら分かるかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0x102,
        (
            "#11P#00100Fどれどれ……\x01",
            "あ、これは私の実家の隣よ。\x02\x03",

            "#00105F居住者は《ハイブラッズ》……\x01",
            "って何これ、法人名かしら？\x02\x03",

            "#00103Fここには、証券マンの\x01",
            "ボンドさん一家が\x01",
            "住んでいたはずだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0x101,
        (
            "#5P#00001Fああ、前の居住者として\x01",
            "リストにも記載されてあるな。\x02",
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
            "#5P#00003F証券マンのボンドさん……\x02\x03",

            "#00001F確か教団事件による\x01",
            "グノーシス被害者の１人だよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0x102,
        (
            "#11P#00103Fええ、間違いないわ。\x02\x03",

            "#00108F事件の後、\x01",
            "ご家族に色々あったとだけは\x01",
            "聞いていたんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0x109,
        (
            "#6P#10101Fまさか……何かのトラブルに\x01",
            "巻き込まれたのでしょうか？\x02",
        )
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0x101,
        (
            "#5P#00001F分からないけど……\x01",
            "どうやら転居届けを出したのは\x01",
            "ボンドさんみたいだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0202
    ChrTalk(
        0x105,
        (
            "#12P#10300F転居先は東通り、\x01",
            "《アカシア荘》２階。\x02\x03",

            "遊撃士協会の左隣にある\x01",
            "建物って書いてあるね。\x02",
        )
    )

    CloseMessageWindow()

    #C0203
    ChrTalk(
        0x101,
        (
            "#5P#00003F住宅街と東通りか……\x01",
            "どちらも確実に調べないとな。\x02\x03",

            "#00001F次の住戸は同じく東通り。\x01",
            "この住所は、釣公師団の本部か……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0204
    ChrTalk(
        0x101,
        "#5P#00011F――って、えぇ！？\x02",
    )

    CloseMessageWindow()

    #C0205
    ChrTalk(
        0x109,
        "#6P#10105Fど、どうかしたんですか？\x02",
    )

    CloseMessageWindow()

    #C0206
    ChrTalk(
        0x101,
        (
            "#5P#00008Fいや、居住者名が《釣皇#4Rちょうおう#倶楽部》\x01",
            "ってなってるんだけど……\x02\x03",

            "聞いたこともない団体名だと思って。\x02",
        )
    )

    CloseMessageWindow()

    #C0207
    ChrTalk(
        0x102,
        (
            "#11P#00105Fロイド、確かあなた\x01",
            "《釣公師団》の団員だったわよね？\x02\x03",

            "他のメンバーの方たちからは\x01",
            "何も聞かされていないの？\x02",
        )
    )

    CloseMessageWindow()

    #C0208
    ChrTalk(
        0x101,
        (
            "#5P#00006Fあ、ああ、最近忙しくて\x01",
            "釣りどころじゃなかったからさ。\x02\x03",

            "#00001Fそれに前居住者である\x01",
            "《釣公師団》は所在不明……\x01",
            "う～ん、まさか名前を変えたのか？\x02\x03",

            "#00003F……まあいい。\x01",
            "これもちゃんと調べるとして。\x02\x03",

            "#00001F最後の住戸は旧市街、\x01",
            "《ロータスハイツ》１階か。\x02\x03",

            "前居住者は、ガイトナー氏……\x01",
            "やはり所在不明らしい。\x02\x03",

            "そして現在の居住者は……\x01",
            "《ショーン・アルナム》。\x02\x03",

            "#00005F……あれ、この名前どこかで\x01",
            "聞いたことがあるような……？\x02",
        )
    )

    CloseMessageWindow()

    #C0209
    ChrTalk(
        0x105,
        "#12P#10304Fフフ、有名な童話の作者だね。\x02",
    )

    CloseMessageWindow()

    #C0210
    ChrTalk(
        0x101,
        "#5P#00011Fえ……？\x02",
    )

    CloseMessageWindow()

    #C0211
    ChrTalk(
        0x102,
        (
            "#11P#00103F図書館で人気の童話、\x01",
            "『マルクと深き森の魔女』を\x01",
            "書いた人ね。\x02\x03",

            "#00100Fロイドも聞き覚えあるんじゃない？\x01",
            "ほら、以前ルバーチェの\x01",
            "アジトに進入した時に……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0212
    ChrTalk(
        0x101,
        (
            "#5P#00005Fああ、そういえば扉の\x01",
            "ロック解除用のパスワードに\x01",
            "使われていたんだっけか。\x02\x03",

            "#00008Fでもまさか、そんな作家先生が\x01",
            "旧市街になんて……\x02",
        )
    )

    CloseMessageWindow()

    #C0213
    ChrTalk(
        0x102,
        (
            "#11P#00101Fええ、というよりそもそも\x01",
            "作者は既に故人だったはずよ。\x02",
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
            "#5P#00006Fそ、そうなのか……\x01",
            "何だか不安になって来たな。\x02",
        )
    )

    CloseMessageWindow()

    #C0215
    ChrTalk(
        0x105,
        (
            "#12P#10302Fフフ、他のはともかくとしても\x01",
            "これは届書を受理する時に\x01",
            "気付いて良さそうなものだよね。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x8)

    #C0216
    ChrTalk(
        0x8,
        "も、申し訳ありません。\x02",
    )

    CloseMessageWindow()

    def lambda_4F0E():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4F0E)
    Sleep(50)

    def lambda_4F1E():
        OP_93(0x102, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4F1E)
    Sleep(50)

    def lambda_4F2E():
        OP_93(0x109, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_4F2E)
    Sleep(50)

    def lambda_4F3E():
        OP_93(0x105, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_4F3E)
    Sleep(100)

    #C0217
    ChrTalk(
        0x8,
        (
            "職員一同、気を付けるように\x01",
            "心がけてはいるのですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0218
    ChrTalk(
        0x102,
        (
            "#00105Fいえ、そんな……\x01",
            "今は市庁舎も組織改革や引き継ぎで\x01",
            "かなり忙しい時期ですし。\x02",
        )
    )

    CloseMessageWindow()

    #C0219
    ChrTalk(
        0x109,
        (
            "#12P#10101Fええ、それに悪いのは何よりも\x01",
            "この届書を出した人ですよ！\x02",
        )
    )

    CloseMessageWindow()

    #C0220
    ChrTalk(
        0x8,
        "あ、ありがとうございます。\x02",
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0x101,
        (
            "#12P#00000Fまあ、というわけで\x01",
            "さっそく調査に向かいますね。\x02",
        )
    )

    CloseMessageWindow()

    #C0222
    ChrTalk(
        0x102,
        (
            "#00100F全て確認したら\x01",
            "また報告に伺いますので。\x02",
        )
    )

    CloseMessageWindow()

    #C0223
    ChrTalk(
        0x8,
        (
            "は、はい。\x01",
            "どうか宜しくお願いします。\x02",
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
            "クエスト【不審住戸の調査依頼】\x07\x00",
            "を開始した！\x02",
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

    # Function_27_374D end

    def Function_28_5170(): pass

    label("Function_28_5170")

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
            "#12P#1P皆さん。\x01",
            "不審住戸の確認の方は\x01",
            "進んでいますか？\x02",
        )
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0x101,
        (
            "#12P#00000Fはい、一通り\x01",
            "確認が終わったので\x01",
            "報告させていただきます。\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    #A0227
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "正しい居住者名を書き加えた\x01",
            "届書の写しを手渡した。\x07\x00\x02",
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
            "#12P#1Pなるほど、細かい所まで\x01",
            "よく調べていただいてますね。\x02",
        )
    )

    CloseMessageWindow()

    #C0229
    ChrTalk(
        0x8,
        (
            "#12P#1Pふむふむ、住宅街方面は共和国、\x01",
            "東通り方面は帝国の方が\x01",
            "入っていたんですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0230
    ChrTalk(
        0x8,
        "#12P#1P旧市街の方は……あら？\x02",
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0x101,
        "#12P#00005F何かありましたか？\x02",
    )

    CloseMessageWindow()

    #C0232
    ChrTalk(
        0x8,
        (
            "#12P#1Pいえ、ゲバルさんのお名前が\x01",
            "あまりに意外だったもので。\x02",
        )
    )

    CloseMessageWindow()

    #C0233
    ChrTalk(
        0x8,
        (
            "#12P#1P私もここで何度か\x01",
            "お見かけしたことがあるだけに\x01",
            "少し複雑な気分です。\x02",
        )
    )

    CloseMessageWindow()

    #C0234
    ChrTalk(
        0x8,
        (
            "#12P#1P何というかその、\x01",
            "悪いことをしていても\x01",
            "どこか憎めない人でしたので。\x02",
        )
    )

    CloseMessageWindow()

    #C0235
    ChrTalk(
        0x102,
        (
            "#00103Fええ、何となく\x01",
            "分かるような気はします。\x02",
        )
    )

    CloseMessageWindow()

    #C0236
    ChrTalk(
        0x109,
        (
            "#12P#10100F確かに良い意味でも悪い意味でも\x01",
            "分かりやすい人のようでしたね。\x02",
        )
    )

    CloseMessageWindow()

    #C0237
    ChrTalk(
        0x105,
        (
            "#12P#10304Fフフ、あれでもう少し\x01",
            "殊勝でいてくれると\x01",
            "可愛げもあるんだけどね。\x02",
        )
    )

    CloseMessageWindow()

    #C0238
    ChrTalk(
        0x8,
        "ふふ、そうかもしれませんね。\x02",
    )

    CloseMessageWindow()

    #C0239
    ChrTalk(
        0x8,
        (
            "……とにかく、調査としては\x01",
            "これ以上ない成果だと思います。\x02",
        )
    )

    CloseMessageWindow()

    #C0240
    ChrTalk(
        0x8,
        (
            "後は住民課の方で各種手続きを踏めば、\x01",
            "つつがなく処理できそうです。\x02",
        )
    )

    CloseMessageWindow()

    #C0241
    ChrTalk(
        0x8,
        (
            "本日は皆さん、\x01",
            "どうもありがとうございました。\x02",
        )
    )

    CloseMessageWindow()

    #C0242
    ChrTalk(
        0x101,
        (
            "#12P#00002Fいえ、こちらこそ\x01",
            "お役に立てたようで何よりです。\x02",
        )
    )

    CloseMessageWindow()

    #C0243
    ChrTalk(
        0x102,
        (
            "#00102Fまた、何かあったら\x01",
            "いつでも呼んでくださいね。\x02",
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
            "クエスト【不審住戸の調査依頼】\x07\x00",
            "を達成した！\x02",
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

    # Function_28_5170 end

    def Function_29_5746(): pass

    label("Function_29_5746")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x198, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5C31")
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
        "ふむ……やはり集まらんか。\x02",
    )

    CloseMessageWindow()

    #C0246
    ChrTalk(
        0x14,
        (
            "なあ、ロイよ。\x01",
            "やはりこのプログラムは\x01",
            "諦めるべきではないかのう。\x02",
        )
    )

    CloseMessageWindow()

    #C0247
    ChrTalk(
        0x15,
        "なに言ってるんだじいちゃん！\x02",
    )

    CloseMessageWindow()

    #C0248
    ChrTalk(
        0x15,
        (
            "街の皆を元気付けるための\x01",
            "チャリティイベント、\x01",
            "その目玉プログラムなんだぜ？\x02",
        )
    )

    CloseMessageWindow()

    #C0249
    ChrTalk(
        0x15,
        (
            "これをやらなくて、\x01",
            "一体何をやるって言うんだ！？\x02",
        )
    )

    CloseMessageWindow()

    #C0250
    ChrTalk(
        0x14,
        "し、しかしのう……\x02",
    )

    CloseMessageWindow()

    #C0251
    ChrTalk(
        0x101,
        (
            "#00000Fすみません、\x01",
            "お取り込みのところ\x01",
            "申し訳ないんですが……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x14, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x15, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_599F():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_599F)
    Sleep(50)
    OP_93(0x15, 0xB4, 0x1F4)

    #C0252
    ChrTalk(
        0x15,
        "あんたらは……\x02",
    )

    CloseMessageWindow()

    #C0253
    ChrTalk(
        0x14,
        "おお、よう来てくれたのう。\x02",
    )

    CloseMessageWindow()

    #C0254
    ChrTalk(
        0x14,
        (
            "今日はチャリティイベントに\x01",
            "遊びに来てくれたのかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0255
    ChrTalk(
        0x101,
        (
            "#00005Fえっと、確か商工会から\x01",
            "チャリティイベントへの協力を\x01",
            "依頼されてたんですけど……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x14, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0256
    ChrTalk(
        0x14,
        "はて、とんと覚えがないが。\x02",
    )

    CloseMessageWindow()

    #C0257
    ChrTalk(
        0x15,
        "──ああ、依頼を出したのは俺さ。\x02",
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
            "な、なぬ？\x01",
            "ロイ、お前いつの間に……\x02",
        )
    )

    CloseMessageWindow()

    #C0259
    ChrTalk(
        0x15,
        (
            "はは、実はついさっき\x01",
            "こっそり依頼を出してきたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0260
    ChrTalk(
        0x15,
        (
            "それじゃあ、\x01",
            "早速仕事の説明をしようか。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5C08():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_5C08)

    #C0261
    ChrTalk(
        0x15,
        "時間は大丈夫そうかい？\x02",
    )

    CloseMessageWindow()
    Jump("loc_5D38")

    label("loc_5C31")

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
            "早速仕事の説明を\x01",
            "したいんだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0263
    ChrTalk(
        0x15,
        "時間は大丈夫そうかい？\x02",
    )

    CloseMessageWindow()

    label("loc_5D38")

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

    # Function_29_5746 end

    def Function_30_5D83(): pass

    label("Function_30_5D83")

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
            "引き受ける\x01",      # 0
            "やめる\x01",          # 1
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
        (0, "loc_5DE5"),
        (1, "loc_5DED"),
        (SWITCH_DEFAULT, "loc_5E78"),
    )


    label("loc_5DE5")

    Call(0, 31)
    Jump("loc_5E78")

    label("loc_5DED")


    #C0264
    ChrTalk(
        0x101,
        (
            "#00006F……す、すみません。\x01",
            "今すぐはちょっと……\x02",
        )
    )

    CloseMessageWindow()

    #C0265
    ChrTalk(
        0x15,
        "そうかあ……残念だ。\x02",
    )

    CloseMessageWindow()

    #C0266
    ChrTalk(
        0x15,
        (
            "もし時間が空いたら\x01",
            "手伝ってくれると助かるよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x198, 3)
    Jump("loc_5E78")

    label("loc_5E78")

    Return()

    # Function_30_5D83 end

    def Function_31_5E79(): pass

    label("Function_31_5E79")


    #C0267
    ChrTalk(
        0x101,
        "#00000Fええ、引き受けさせていただきます。\x02",
    )

    CloseMessageWindow()

    #C0268
    ChrTalk(
        0x15,
        (
            "そうこなくっちゃ！\x01",
            "じゃあ、依頼内容を説明するぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0269
    ChrTalk(
        0x15,
        (
            "今日、この市民会館のホールで\x01",
            "チャリティイベントが開かれてるのは\x01",
            "あんたたちも知っているだろ？\x02",
        )
    )

    CloseMessageWindow()

    #C0270
    ChrTalk(
        0x15,
        (
            "今はちょうど、ピアノの演奏と\x01",
            "立食パーティが開かれてるんだが、\x01",
            "ひとつだけ問題が起きててな。\x02",
        )
    )

    CloseMessageWindow()

    #C0271
    ChrTalk(
        0x102,
        "#00105F問題……ですか？\x02",
    )

    CloseMessageWindow()

    #C0272
    ChrTalk(
        0x15,
        (
            "実は、この後に俺の企画した\x01",
            "ある目玉プログラムが行われる\x01",
            "予定だったんだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0273
    ChrTalk(
        0x15,
        (
            "参加者が集まらなくて、\x01",
            "プログラム自体が頓挫しそうなんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0274
    ChrTalk(
        0x109,
        "#10103F確か依頼にも書いてありましたね。\x02",
    )

    CloseMessageWindow()

    #C0275
    ChrTalk(
        0x105,
        (
            "#10300Fで、そのプログラムってのは\x01",
            "具体的になんなんだい？\x02",
        )
    )

    CloseMessageWindow()

    #C0276
    ChrTalk(
        0x15,
        (
            "『ミス・クロスベルコンテスト\x01",
            "    ～働く女性よ、永遠に～　』だ。\x02",
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
            "#00012Fい、いわゆる\x01",
            "ミスコンってやつですか。\x02",
        )
    )

    CloseMessageWindow()

    #C0278
    ChrTalk(
        0x104,
        "#00309Fへえ、そいつぁ楽しみだなあ。\x02",
    )

    CloseMessageWindow()

    #C0279
    ChrTalk(
        0x103,
        (
            "#00211Fサブタイトルのチープさが\x01",
            "気になるんですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0280
    ChrTalk(
        0x15,
        (
            "まあ、要するに\x01",
            "クロスベルで働く女性に\x01",
            "スポットをあてたミスコンでね。\x02",
        )
    )

    CloseMessageWindow()

    #C0281
    ChrTalk(
        0x15,
        (
            "ただ……今のところ参加者が\x01",
            "ほとんど集まってないんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0282
    ChrTalk(
        0x14,
        (
            "オファーできたのは\x01",
            "たったの３人なんじゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0283
    ChrTalk(
        0x14,
        (
            "これではさすがに\x01",
            "プログラムの体を成しておらんから、\x01",
            "中止しようかと話しておってな。\x02",
        )
    )

    CloseMessageWindow()

    #C0284
    ChrTalk(
        0x102,
        (
            "#00106Fうーん、やっぱり多くの人は\x01",
            "遠慮してしまうでしょうね。\x02",
        )
    )

    CloseMessageWindow()

    #C0285
    ChrTalk(
        0x105,
        (
            "#10302Fフフ、どうやら\x01",
            "話が見えてきたようだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0286
    ChrTalk(
        0x15,
        "お察しの通りさ。\x02",
    )

    CloseMessageWindow()

    #C0287
    ChrTalk(
        0x15,
        (
            "あんたたちには、ミスコンに\x01",
            "参加してくれる“働く女性”を\x01",
            "スカウトしてきてほしいんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0288
    ChrTalk(
        0x101,
        (
            "#00004Fなるほど……\x01",
            "依頼の概要は分かりました。\x02\x03",

            "#00000Fちなみに、参加者は現在\x01",
            "３人いるらしいですけど……\x01",
            "どんな人たちなんですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0289
    ChrTalk(
        0x15,
        (
            "えっとね、まずは\x01",
            "百貨店の受付嬢のシンシアさん。\x02",
        )
    )

    CloseMessageWindow()

    #C0290
    ChrTalk(
        0x15,
        (
            "次に、裏通りのホステス\x01",
            "アイリスさん。\x02",
        )
    )

    CloseMessageWindow()

    #C0291
    ChrTalk(
        0x15,
        (
            "そして、クロスベル警察から\x01",
            "婦警のケイトさんに\x01",
            "ＯＫをもらえてるぜ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0292
    ChrTalk(
        0x101,
        "#00012Fケイト先輩まで……\x02",
    )

    CloseMessageWindow()

    #C0293
    ChrTalk(
        0x105,
        (
            "#10304F受付嬢にホステスに婦警か。\x01",
            "フフ、中々バリエーション豊かだね。\x02\x03",

            "#10302Fあとはどんな職業の子を\x01",
            "誘ってくればいいのかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0294
    ChrTalk(
        0x15,
        "うーん、そうだな……\x02",
    )

    CloseMessageWindow()

    #C0295
    ChrTalk(
        0x15,
        (
            "『ウェイトレス』『職人』\x01",
            "『メイド』『シスター』……\x01",
            "この４枠でおねがいするぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0296
    ChrTalk(
        0x15,
        (
            "これらの人が参加してくれれば\x01",
            "コンテスト参加者の職業の\x01",
            "バランスがよくなるだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0297
    ChrTalk(
        0x15,
        (
            "……本当なら、看護師さんや\x01",
            "アルカンシェルの団員さんとかも\x01",
            "誘いたかったんだけどね。\x02",
        )
    )

    CloseMessageWindow()

    #C0298
    ChrTalk(
        0x103,
        (
            "#00203F仕方がないかと思います。\x01",
            "アルカンシェルはイリアさんの件で\x01",
            "それどころじゃないでしょうし……\x02\x03",

            "ウルスラ病院も、患者の対応で\x01",
            "手一杯なはずですから。\x02",
        )
    )

    CloseMessageWindow()

    #C0299
    ChrTalk(
        0x101,
        (
            "#00003Fそうだな……\x02\x03",

            "#00000Fよし、とにかく指針は決まったな。\x02\x03",

            "『ウェイトレス』『職人』\x01",
            "『メイド』『シスター』……\x01",
            "これらの職業の女性を探してみよう。\x02",
        )
    )

    CloseMessageWindow()

    #C0300
    ChrTalk(
        0x15,
        (
            "参加者が集まったら\x01",
            "すぐにでもイベントを\x01",
            "開始するつもりだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0301
    ChrTalk(
        0x15,
        "どうか、よろしく頼んだぜ。\x02",
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
            "クエスト【チャリティイベントへの協力】\x07\x00",
            "を開始した！\x02",
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

    # Function_31_5E79 end

    def Function_32_6944(): pass

    label("Function_32_6944")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6CE2")

    #C0303
    ChrTalk(
        0x14,
        "おお、君たちか。\x02",
    )

    CloseMessageWindow()

    #C0304
    ChrTalk(
        0x15,
        "ミスコンの参加者は集まったかい？\x02",
    )

    CloseMessageWindow()

    #C0305
    ChrTalk(
        0x15,
        (
            "頼んでいた参加枠は\x01",
            "『ウェイトレス』『職人』\x01",
            "『メイド』『シスター』の４つだが。\x02",
        )
    )

    CloseMessageWindow()

    #C0306
    ChrTalk(
        0x101,
        (
            "#00000Fええ、ちゃんと交渉してきました。\x02\x03",

            "彼女たちには、プログラムの開始前に\x01",
            "連絡をいれる手筈になってます。\x02",
        )
    )

    CloseMessageWindow()

    #C0307
    ChrTalk(
        0x15,
        "おおっ、そいつはよかった！\x02",
    )

    CloseMessageWindow()

    #C0308
    ChrTalk(
        0x15,
        (
            "こっちも、もうそろそろ\x01",
            "ピアノの演奏が終わる頃でさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0309
    ChrTalk(
        0x15,
        (
            "いやー、何とか間に合ったぜ！\x01",
            "これで何とか開催できそうだ！\x02",
        )
    )

    CloseMessageWindow()

    #C0310
    ChrTalk(
        0x102,
        "#00109Fふふ、良かったですね。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x14, 0x15, 500)

    #C0311
    ChrTalk(
        0x14,
        (
            "うむ、ロイにしては\x01",
            "色々とがんばった方じゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0312
    ChrTalk(
        0x14,
        (
            "あのやる気のない孫が\x01",
            "ようやっと成長したかと思うと\x01",
            "感慨深いものがあるのう。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x15, 0x14, 500)

    #C0313
    ChrTalk(
        0x15,
        "ちぇっ、なんだよそれ……\x02",
    )

    CloseMessageWindow()
    OP_93(0x15, 0xB4, 0x1F4)

    #C0314
    ChrTalk(
        0x15,
        (
            "ま、とにかく、\x01",
            "ミスコンが始まるんだ。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_6CB3():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_6CB3)

    #C0315
    ChrTalk(
        0x15,
        "あんたたち、準備はいいかい？\x02",
    )

    CloseMessageWindow()
    Jump("loc_6D31")

    label("loc_6CE2")


    #C0316
    ChrTalk(
        0x15,
        (
            "ま、とにかく、\x01",
            "ミスコンが始まるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0317
    ChrTalk(
        0x15,
        "あんたたちも、準備はいいかい？\x02",
    )

    CloseMessageWindow()

    label("loc_6D31")

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

    # Function_32_6944 end

    def Function_33_6D76(): pass

    label("Function_33_6D76")

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
            "準備はできている\x01",      # 0
            "まだできていない\x01",      # 1
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
        (0, "loc_6DE8"),
        (1, "loc_6DF0"),
        (SWITCH_DEFAULT, "loc_6E83"),
    )


    label("loc_6DE8")

    Call(0, 34)
    Jump("loc_6E83")

    label("loc_6DF0")


    #C0318
    ChrTalk(
        0x101,
        (
            "#00006F少し待ってもらえますか？\x01",
            "ちょっと心の準備が……\x02",
        )
    )

    CloseMessageWindow()

    #C0319
    ChrTalk(
        0x15,
        "おいおい、たのむぜ。\x02",
    )

    CloseMessageWindow()

    #C0320
    ChrTalk(
        0x15,
        (
            "じゃあ、準備ができたら\x01",
            "また声をかけてくれよな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x19A, 0)
    Jump("loc_6E83")

    label("loc_6E83")

    Return()

    # Function_33_6D76 end

    def Function_34_6E84(): pass

    label("Function_34_6E84")


    #C0321
    ChrTalk(
        0x101,
        (
            "#00000Fええ、大丈夫です。\x02\x03",

            "では、こちらからも\x01",
            "参加者たちに連絡しておきますね。\x02",
        )
    )

    CloseMessageWindow()

    #C0322
    ChrTalk(
        0x15,
        "ああ、よろしく頼むぜ。\x02",
    )

    CloseMessageWindow()

    #C0323
    ChrTalk(
        0x104,
        (
            "#00309Fいや～、いよいよだな。\x01",
            "楽しみになってきたぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0324
    ChrTalk(
        0x103,
        (
            "#00211Fランディさんは\x01",
            "本当にそればかりですね。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x14, 0x15, 500)

    #C0325
    ChrTalk(
        0x14,
        (
            "では、わしの方は\x01",
            "会場の準備に行くとしよう。\x02",
        )
    )

    CloseMessageWindow()

    #C0326
    ChrTalk(
        0x14,
        (
            "ミスコンの進行の方はロイ、\x01",
            "お前にまかせたぞ。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x15, 0x14, 500)

    #C0327
    ChrTalk(
        0x15,
        "ああ、任せてくれ爺ちゃん！\x02",
    )

    CloseMessageWindow()

    #C0328
    ChrTalk(
        0x105,
        (
            "#10302Fま、とりあえずあとは\x01",
            "成功を祈るのみだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0329
    ChrTalk(
        0x102,
        (
            "#00102Fふふ、いい機会だから\x01",
            "息抜きさせてもらいましょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0330
    ChrTalk(
        0x109,
        "#10109Fええ、そうですね！\x02",
    )

    CloseMessageWindow()

    #C0331
    ChrTalk(
        0x101,
        (
            "#00002F俺たちも早めに参加者に連絡して\x01",
            "会場入りするとしようか。\x02",
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

    # Function_34_6E84 end

    def Function_35_70E9(): pass

    label("Function_35_70E9")

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
            "おかげさまで\x01",
            "ミスコンは大成功だ！\x02",
        )
    )

    CloseMessageWindow()

    #C0333
    ChrTalk(
        0x15,
        (
            "あんたたちが参加者を\x01",
            "集めてくれたおかげだ、\x01",
            "どうもありがとうな！\x02",
        )
    )

    CloseMessageWindow()

    #C0334
    ChrTalk(
        0x101,
        "#00002Fはは、どういたしまして。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 4)), scpexpr(EXPR_END)), "loc_74E0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 1)), scpexpr(EXPR_END)), "loc_7333")

    #C0335
    ChrTalk(
        0x102,
        (
            "#00104Fふふ、私たちも\x01",
            "随分楽しめた気がします。\x02\x03",

            "#00102Fまさか特別賞をもらえるなんて\x01",
            "思いもよらなかったけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0336
    ChrTalk(
        0x109,
        (
            "#10109Fエリィさんだったら\x01",
            "当然の結果ですよ！\x02",
        )
    )

    CloseMessageWindow()

    #C0337
    ChrTalk(
        0x103,
        "#00202Fかっこよかったです。\x02",
    )

    CloseMessageWindow()
    OP_29(0x8F, 0x1, 0xE)
    Jump("loc_74DB")

    label("loc_7333")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 2)), scpexpr(EXPR_END)), "loc_7417")

    #C0338
    ChrTalk(
        0x103,
        (
            "#00204F……わたしたちも\x01",
            "結構楽しかったです。\x02\x03",

            "#00202Fまさか特別賞をもらえるなんて\x01",
            "思いませんでしたが……\x02",
        )
    )

    CloseMessageWindow()

    #C0339
    ChrTalk(
        0x102,
        (
            "#00109Fふふ、ティオちゃんだったら\x01",
            "当然の結果だと思うわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0340
    ChrTalk(
        0x109,
        (
            "#10109F本当！\x01",
            "可愛かったよ～。\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x8F, 0x1, 0xF)
    Jump("loc_74DB")

    label("loc_7417")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 3)), scpexpr(EXPR_END)), "loc_74DB")

    #C0341
    ChrTalk(
        0x109,
        (
            "#10104Fあたしたちも随分楽しめました。\x02\x03",

            "#10100Fまさか特別賞をもらえるなんて\x01",
            "予想外でしたけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0342
    ChrTalk(
        0x103,
        "#00204Fノエルさんなら当然の結果かと。\x02",
    )

    CloseMessageWindow()

    #C0343
    ChrTalk(
        0x102,
        "#00109Fとってもかっこよかったわ。\x02",
    )

    CloseMessageWindow()
    OP_29(0x8F, 0x1, 0x10)

    label("loc_74DB")

    Jump("loc_76E1")

    label("loc_74E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 1)), scpexpr(EXPR_END)), "loc_7592")

    #C0344
    ChrTalk(
        0x102,
        (
            "#00102Fふふ、私たちも\x01",
            "随分楽しめた気がします。\x02",
        )
    )

    CloseMessageWindow()

    #C0345
    ChrTalk(
        0x109,
        (
            "#10106Fエリィさんも後一歩だったと\x01",
            "思うんですけどねえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0346
    ChrTalk(
        0x103,
        (
            "#00202Fまあ、制服ではないですし\x01",
            "仕方ないかと。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_76E1")

    label("loc_7592")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 2)), scpexpr(EXPR_END)), "loc_7646")

    #C0347
    ChrTalk(
        0x103,
        (
            "#00202F……わたしたちも\x01",
            "結構楽しかったです。\x02",
        )
    )

    CloseMessageWindow()

    #C0348
    ChrTalk(
        0x102,
        (
            "#00102Fティオちゃんも後一歩だったと\x01",
            "思うんだけれどね。\x02",
        )
    )

    CloseMessageWindow()

    #C0349
    ChrTalk(
        0x109,
        (
            "#10106Fまあ、制服ではないですし\x01",
            "仕方ありませんね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_76E1")

    label("loc_7646")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 3)), scpexpr(EXPR_END)), "loc_76E1")

    #C0350
    ChrTalk(
        0x109,
        (
            "#10100Fあたしたちも\x01",
            "随分楽しめました。\x02",
        )
    )

    CloseMessageWindow()

    #C0351
    ChrTalk(
        0x103,
        (
            "#00202Fノエルさんも\x01",
            "後一歩だったと思います。\x02",
        )
    )

    CloseMessageWindow()

    #C0352
    ChrTalk(
        0x102,
        (
            "#00102Fふふ、制服ではないから\x01",
            "仕方ないけどね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_76E1")


    #C0353
    ChrTalk(
        0x14,
        (
            "市民たちも息抜きできたようだし、\x01",
            "復興支援の義援金への寄付も\x01",
            "ミスコンの後は随分集まっておる。\x02",
        )
    )

    CloseMessageWindow()

    #C0354
    ChrTalk(
        0x14,
        (
            "今日ばかりはロイの思いつきを\x01",
            "褒めてやらざるをえんな。\x02",
        )
    )

    CloseMessageWindow()

    #C0355
    ChrTalk(
        0x15,
        (
            "ちぇっ、思いつきじゃなくて\x01",
            "ナイスアイデアって言ってくれよ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0356
    ChrTalk(
        0x15,
        (
            "そうだ、せっかくだから\x01",
            "あんたたちにこれを\x01",
            "プレゼントするよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0357
    ChrTalk(
        0x15,
        (
            "今回の優勝者をイメージした\x01",
            "記念品みたいなもんだ。\x01",
            "よかったら受け取ってくれ。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x1, 0x9)"), scpexpr(EXPR_END)), "loc_78C7")
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
            "を受け取った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x76, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_7A3E")

    label("loc_78C7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x1, 0xA)"), scpexpr(EXPR_END)), "loc_7926")
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
            "を受け取った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x72, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_7A3E")

    label("loc_7926")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x1, 0xB)"), scpexpr(EXPR_END)), "loc_7985")
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
            "を受け取った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x6E, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_7A3E")

    label("loc_7985")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x1, 0xC)"), scpexpr(EXPR_END)), "loc_79E4")
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
            "を受け取った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x82, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_7A3E")

    label("loc_79E4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x1, 0xD)"), scpexpr(EXPR_END)), "loc_7A3E")
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
            "を受け取った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x66, 1)
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_7A3E")


    #C0363
    ChrTalk(
        0x101,
        (
            "#00005Fいいんですか？\x01",
            "ありがとうございます。\x02",
        )
    )

    CloseMessageWindow()

    #C0364
    ChrTalk(
        0x104,
        (
            "#00309Fハハ、何はともあれ\x01",
            "おかげさまで楽しめたぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0365
    ChrTalk(
        0x105,
        "#10302Fまたこういう機会があるといいね。\x02",
    )

    CloseMessageWindow()

    #C0366
    ChrTalk(
        0x101,
        (
            "#00004Fああ、本当だな。\x02\x03",

            "#00000F──それじゃあ、自分たちは\x01",
            "これで失礼しますね。\x02",
        )
    )

    CloseMessageWindow()

    #C0367
    ChrTalk(
        0x14,
        "うむ、ありがとうな。\x02",
    )

    CloseMessageWindow()

    #C0368
    ChrTalk(
        0x15,
        (
            "また何かあったら\x01",
            "よろしくたのむぜ！\x02",
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
            "クエスト【チャリティイベントへの協力】\x07\x00",
            "を達成した！\x02",
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

    # Function_35_70E9 end

    def Function_36_7C1D(): pass

    label("Function_36_7C1D")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0370
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "クロスベル市民会館\x01",
            "　　　応接室　　　\x07\x00\x02",
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
            "扉には鍵がかかっている。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)
    Return()

    # Function_36_7C1D end

    def Function_37_7CAB(): pass

    label("Function_37_7CAB")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0372
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "クロスベル市民会館\x01",
            "　各種施設連絡口　\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7D43")

    #C0373
    ChrTalk(
        0x101,
        (
            "#00000Fこっちに入る必要は\x01",
            "なさそうだな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_7D43")

    TalkEnd(0xFF)
    Return()

    # Function_37_7CAB end

    def Function_38_7D47(): pass

    label("Function_38_7D47")

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
            "　　　　　　　『聖者の祈り』　　　　　　　\x01",
            "　　　　　マグナス・ヘクトール作　　　　　\x01",
            "　　　　　　　　　　　　　　　　　　　\x01",
            "Ｓ１１３４、自治州創立を讃えて生み出された\x01",
            "　彫刻家マグナス・ヘクトール晩年の傑作。 　\x01",
            "　　 旧市庁舎建立後、同舎の象徴として 　　\x01",
            "　　　　長年市民に親しまれてきた。　　　　\x01",
            "　　　　　　　　　　　　　　　　　　　\x01",
            "　　　Ｓ１２０４、市庁の移転に伴い、　　　\x01",
            "　　 そのまま市民会館に引き継がれる。 　　\x07\x00\x02",
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

    # Function_38_7D47 end

    def Function_39_7F2A(): pass

    label("Function_39_7F2A")

    EventBegin(0x1)
    SetChrName("")

    #A0375
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ホールの方からは\x01",
            "白熱した論戦が聞こえてくる……\x02\x03",

            "邪魔するのはやめておこう。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, -13650, 4000, 12700, 225)
    EventEnd(0x4)
    Return()

    # Function_39_7F2A end

    SaveToFile()

Try(main)
