from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t1300.bin",                # FileName
        "t1300",                    # MapName
        "t1300",                    # Location
        0x00B6,                     # MapIndex
        "ed7160",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x05,                       # PlaceNameNumber
        0x1A,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, -10000, 0, 0, 1, 182, 0, 1, 0, 2],
    )

    BuildStringList((
        "t1300",                  # 0
        "キーア",                 # 1
        "フラン",                 # 2
        "セシル",                 # 3
        "イリア",                 # 4
        "リーシャ",               # 5
        "シュリ",                 # 6
        "エリィ",                 # 7
        "ティオ",                 # 8
        "ランディ",               # 9
        "ノエル",                 # 10
        "ワジ",                   # 11
        "ツァイト",               # 12
        "みっしぃ",               # 13
        "メルスン",               # 14
        "コロナ",                 # 15
        "リマ",                   # 16
        "ＭＷＬスタッフ",         # 17
        "観光客",                 # 18
        "観光客",                 # 19
        "観光客",                 # 20
        "観光客",                 # 21
        "観光客",                 # 22
        "職員ハンクス",           # 23
        "観客",                   # 24
        "観客",                   # 25
        "観客",                   # 26
        "観客",                   # 27
        "観客",                   # 28
        "観客",                   # 29
        "観客",                   # 30
        "観客",                   # 31
        "観客",                   # 32
        "観客",                   # 33
        "みーしぇ",               # 34
        "幻獣",                   # 35
        "幻獣",                   # 36
        "幻獣",                   # 37
        "SE制御",                 # 38
        "bt1300",                 # 39
        "鏡の城方面",             # 40
        "観覧車方面",             # 41
        "ホラーコースター方面",   # 42
        "ホテル・デルフィニア方面",# 43
    ))

    ATBonus("ATBonus_64C", 100, 5, 0, 5, 0, 5, 0, 2, 5, 0, 0, 0, 2, 0, 0, 0)

    MonsterBattlePostion("MonsterBattlePostion_70C", 8, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_710", 4, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_714", 12, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_718", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_71C", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_720", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_724", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_728", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_6EC", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_6F0", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_6F4", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_6F8", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_6FC", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_700", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_704", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_708", 5, 5, 45)

    # monster count: 0

    # event battle count: 1

    BattleInfo(
        "BattleInfo_72C", 0x0042, 255, 6, 45, 3, 3, 30, 0, "bt1300", 0x00000000, 100, 0, 0, 0,
        (
            ("ms88701.dat", "ms88801.dat", "ms88801.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_70C", "MonsterBattlePostion_6EC", "ed7454", "ed7453", "ATBonus_64C"),
            (),
            (),
            (),
        )
    )

    AddCharChip((
        "chr/ch08200.itc",                   # 00
        "chr/ch08500.itc",                   # 01
        "chr/ch05200.itc",                   # 02
        "chr/ch05100.itc",                   # 03
        "chr/ch07500.itc",                   # 04
        "chr/ch10100.itc",                   # 05
        "chr/ch00100.itc",                   # 06
        "chr/ch00200.itc",                   # 07
        "chr/ch00300.itc",                   # 08
        "chr/ch02900.itc",                   # 09
        "chr/ch03000.itc",                   # 0A
        "chr/ch02710.itc",                   # 0B
        "chr/ch10200.itc",                   # 0C
        "chr/ch26200.itc",                   # 0D
        "chr/ch22700.itc",                   # 0E
        "chr/ch20700.itc",                   # 0F
        "chr/ch44500.itc",                   # 10
        "chr/ch24400.itc",                   # 11
        "chr/ch21300.itc",                   # 12
        "chr/ch20200.itc",                   # 13
        "chr/ch21900.itc",                   # 14
        "chr/ch23000.itc",                   # 15
        "apl/ch50387.itc",                   # 16
        "chr/ch00202.itc",                   # 17
        "chr/ch03002.itc",                   # 18
        "chr/ch07502.itc",                   # 19
        "chr/ch45400.itc",                   # 1A
        "chr/ch00000.itc",                   # 1B
        "chr/ch00000.itc",                   # 1C
        "chr/ch00000.itc",                   # 1D
    ))

    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   0,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   1,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   4,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   3,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   2,   0,   0,   0,   0,   13,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   5,   0,   0,   0,   0,   14,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   6,   0,   0,   0,   0,   3,   255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   7,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   8,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   9,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   10,  0,   0,   0,   0,   8,   255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   11,  0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   12,  0,   0,   0,   0,   15,  255,  0)
    DeclNpc(-4139,   0,       5000,    0,    389,  0x0, 0,   13,  0,   0,   0,   0,   16,  255,  0)
    DeclNpc(-4989,   0,       4989,    0,    389,  0x0, 0,   14,  0,   0,   0,   0,   17,  255,  0)
    DeclNpc(-4699,   0,       7539,    0,    389,  0x0, 0,   15,  0,   0,   0,   0,   18,  255,  0)
    DeclNpc(8369,    0,       5630,    225,  389,  0x0, 0,   16,  0,   0,   0,   0,   19,  255,  0)
    DeclNpc(500,     0,       -10300,  270,  389,  0x0, 0,   17,  0,   0,   0,   0,   20,  255,  0)
    DeclNpc(-500,    0,       -10300,  90,   389,  0x0, 0,   18,  0,   0,   0,   0,   21,  255,  0)
    DeclNpc(5309,    0,       6300,    180,  389,  0x0, 0,   19,  0,   0,   0,   0,   22,  255,  0)
    DeclNpc(5119,    0,       4349,    45,   389,  0x0, 0,   20,  0,   0,   0,   0,   23,  255,  0)
    DeclNpc(6190,    0,       5000,    270,  389,  0x0, 0,   21,  0,   0,   0,   0,   24,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    421,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    421,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    421,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    421,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    421,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    421,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    421,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    421,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    421,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    421,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(2029,    0,       3349,    180,  389,  0x0, 0,   26,  0,   0,   0,   255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 32,  0.0,                   -17.0,                 -1.0,                  506.25,                [0.06666667014360428,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.3333333432674408,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -0.0,                  5.6666669845581055,    0.20000000298023224,   1.0])

    DeclActor(3030,    0,       3660,    1000,    2029,    1500,    3350,    0x007E, 0,  42, 0x0000)

    PlaceName(0.0, 0.0, 30.0, 0x0000, 0x0000, "鏡の城方面")
    PlaceName(-40.0, 0.0, 10.0, 0x0000, 0x0000, "観覧車方面")
    PlaceName(60.0, 0.0, 10.0, 0x0000, 0x0000, "ホラーコースター方面")
    PlaceName(0.0, 0.0, -80.0, 0x0000, 0x0000, "ホテル・デルフィニア方面")
    PlaceName(10.0, 0.0, 10.0, 0x0000, 0x0053, "")

    ChipFrameInfo(2120, 0)                                       # 0

    ScpFunction((
        "Function_0_848",          # 00, 0
        "Function_1_900",          # 01, 1
        "Function_2_9BD",          # 02, 2
        "Function_3_D2F",          # 03, 3
        "Function_4_E25",          # 04, 4
        "Function_5_1075",         # 05, 5
        "Function_6_111D",         # 06, 6
        "Function_7_124F",         # 07, 7
        "Function_8_13C5",         # 08, 8
        "Function_9_1548",         # 09, 9
        "Function_10_1630",        # 0A, 10
        "Function_11_179C",        # 0B, 11
        "Function_12_18AA",        # 0C, 12
        "Function_13_19A6",        # 0D, 13
        "Function_14_1AB7",        # 0E, 14
        "Function_15_1B8E",        # 0F, 15
        "Function_16_20E4",        # 10, 16
        "Function_17_2178",        # 11, 17
        "Function_18_2221",        # 12, 18
        "Function_19_22E4",        # 13, 19
        "Function_20_24EB",        # 14, 20
        "Function_21_256C",        # 15, 21
        "Function_22_25B3",        # 16, 22
        "Function_23_2631",        # 17, 23
        "Function_24_26BC",        # 18, 24
        "Function_25_2706",        # 19, 25
        "Function_26_29BD",        # 1A, 26
        "Function_27_2A93",        # 1B, 27
        "Function_28_2B79",        # 1C, 28
        "Function_29_461A",        # 1D, 29
        "Function_30_4ACC",        # 1E, 30
        "Function_31_4AE3",        # 1F, 31
        "Function_32_4B55",        # 20, 32
        "Function_33_5156",        # 21, 33
        "Function_34_517B",        # 22, 34
        "Function_35_564E",        # 23, 35
        "Function_36_5681",        # 24, 36
        "Function_37_56B4",        # 25, 37
        "Function_38_56E7",        # 26, 38
        "Function_39_57EF",        # 27, 39
        "Function_40_58EB",        # 28, 40
        "Function_41_597A",        # 29, 41
        "Function_42_59B9",        # 2A, 42
        "Function_43_630A",        # 2B, 43
        "Function_44_6B25",        # 2C, 44
        "Function_45_7DA3",        # 2D, 45
        "Function_46_7DC0",        # 2E, 46
        "Function_47_7DDD",        # 2F, 47
        "Function_48_7DFA",        # 30, 48
        "Function_49_7E6D",        # 31, 49
        "Function_50_7EE0",        # 32, 50
        "Function_51_7FF4",        # 33, 51
        "Function_52_8108",        # 34, 52
        "Function_53_8127",        # 35, 53
    ))


    def Function_0_848(): pass

    label("Function_0_848")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_888"),
        (1, "loc_894"),
        (2, "loc_8A0"),
        (3, "loc_8AC"),
        (4, "loc_8B8"),
        (5, "loc_8C4"),
        (6, "loc_8D0"),
        (SWITCH_DEFAULT, "loc_8DC"),
    )


    label("loc_888")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_8E8")

    label("loc_894")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_8E8")

    label("loc_8A0")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_8E8")

    label("loc_8AC")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_8E8")

    label("loc_8B8")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_8E8")

    label("loc_8C4")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_8E8")

    label("loc_8D0")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_8E8")

    label("loc_8DC")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_8E8")

    label("loc_8E8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_8FF")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_8E8")

    label("loc_8FF")

    Return()

    # Function_0_848 end

    def Function_1_900(): pass

    label("Function_1_900")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_90E")
    Jump("loc_97C")

    label("loc_90E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 7)), scpexpr(EXPR_END)), "loc_91C")
    Jump("loc_97C")

    label("loc_91C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_92A")
    Jump("loc_97C")

    label("loc_92A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_93B")
    Call(0, 25)
    Jump("loc_97C")

    label("loc_93B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_949")
    Jump("loc_97C")

    label("loc_949")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_957")
    Jump("loc_97C")

    label("loc_957")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_965")
    Jump("loc_97C")

    label("loc_965")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_973")
    Jump("loc_97C")

    label("loc_973")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_97C")

    label("loc_97C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_990")
    ClearScenarioFlags(0x22, 0)
    Event(0, 28)
    Jump("loc_9BC")

    label("loc_990")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_9AA")
    ClearScenarioFlags(0x22, 1)
    SetScenarioFlags(0x1, 3)
    SetScenarioFlags(0x1, 4)
    Event(0, 29)
    Jump("loc_9BC")

    label("loc_9AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 2)), scpexpr(EXPR_END)), "loc_9BC")
    ClearScenarioFlags(0x22, 2)
    SetScenarioFlags(0x1, 5)
    Event(0, 44)

    label("loc_9BC")

    Return()

    # Function_1_900 end

    def Function_2_9BD(): pass

    label("Function_2_9BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_9D7")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x1, 3)
    Jump("loc_9E9")

    label("loc_9D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_9E9")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x233), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_9E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_A00")
    OP_24(0x7E)
    OP_24(0x335)
    ClearScenarioFlags(0x1, 4)
    Jump("loc_ACB")

    label("loc_A00")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_END)), "loc_A1A")
    Sound(821, 1, 60, 0)
    OP_24(0x7E)
    ClearScenarioFlags(0x1, 5)
    Jump("loc_ACB")

    label("loc_A1A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A62")
    OP_24(0x335)
    SoundDistance(0x7E, 0xFFFFB5D2, 0xBB8, 0xFFFF26F8, 0x13880, 0xC350, 0x64, 0x0)
    OP_E3(0x639C, 0xBB8, 0xFFFF26F8)
    SoundLoad(918)
    BeginChrThread(0x2D, 3, 0, 53)
    Jump("loc_ACB")

    label("loc_A62")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_END)), "loc_A9C")
    OP_24(0x335)
    SoundDistance(0x7E, 0xFFFFB5D2, 0xBB8, 0xFFFF26F8, 0x13880, 0xC350, 0x64, 0x0)
    OP_E3(0x639C, 0xBB8, 0xFFFF26F8)
    Jump("loc_ACB")

    label("loc_A9C")

    Sound(821, 1, 60, 0)
    SoundDistance(0x7E, 0xFFFFB5D2, 0xBB8, 0xFFFF26F8, 0x13880, 0xC350, 0x64, 0x0)
    OP_E3(0x639C, 0xBB8, 0xFFFF26F8)

    label("loc_ACB")

    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_AE3")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_AE3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_B8E")
    OP_7D(0xDC, 0xEB, 0xFF, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0x14, 0x1F4, 0x0)
    ClearMapObjFlags(0x8, 0x4)
    ClearMapObjFlags(0x9, 0x4)
    ClearMapObjFlags(0xA, 0x4)
    ClearMapObjFlags(0xB, 0x4)
    ClearMapObjFlags(0xC, 0x4)
    ClearMapObjFlags(0xD, 0x4)
    ClearMapObjFlags(0xE, 0x4)
    ClearMapObjFlags(0xF, 0x4)
    ClearMapObjFlags(0x10, 0x4)
    ClearMapObjFlags(0x11, 0x4)
    ClearMapObjFlags(0x12, 0x4)
    ClearMapObjFlags(0x13, 0x4)
    ClearMapObjFlags(0x14, 0x4)
    ClearMapObjFlags(0x15, 0x4)
    ClearMapObjFlags(0x16, 0x4)
    ClearMapObjFlags(0x17, 0x4)
    ClearMapObjFlags(0x18, 0x4)
    ClearMapObjFlags(0x19, 0x4)
    ClearMapObjFlags(0x1A, 0x4)
    ClearMapObjFlags(0x1B, 0x4)
    ClearMapObjFlags(0x1C, 0x4)
    ClearMapObjFlags(0x1D, 0x4)
    Jump("loc_C5E")

    label("loc_B8E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 5)), scpexpr(EXPR_END)), "loc_C39")
    OP_7D(0xDC, 0xEB, 0xFF, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0x14, 0x1F4, 0x0)
    ClearMapObjFlags(0x8, 0x4)
    ClearMapObjFlags(0x9, 0x4)
    ClearMapObjFlags(0xA, 0x4)
    ClearMapObjFlags(0xB, 0x4)
    ClearMapObjFlags(0xC, 0x4)
    ClearMapObjFlags(0xD, 0x4)
    ClearMapObjFlags(0xE, 0x4)
    ClearMapObjFlags(0xF, 0x4)
    ClearMapObjFlags(0x10, 0x4)
    ClearMapObjFlags(0x11, 0x4)
    ClearMapObjFlags(0x12, 0x4)
    ClearMapObjFlags(0x13, 0x4)
    ClearMapObjFlags(0x14, 0x4)
    ClearMapObjFlags(0x15, 0x4)
    ClearMapObjFlags(0x16, 0x4)
    ClearMapObjFlags(0x17, 0x4)
    ClearMapObjFlags(0x18, 0x4)
    ClearMapObjFlags(0x19, 0x4)
    ClearMapObjFlags(0x1A, 0x4)
    ClearMapObjFlags(0x1B, 0x4)
    ClearMapObjFlags(0x1C, 0x4)
    ClearMapObjFlags(0x1D, 0x4)
    Jump("loc_C5E")

    label("loc_C39")

    SetMapObjFrame(0xFF, "water", 0x2, "loop_off")
    SetMapObjFrame(0xFF, "back00", 0x2, "loop_off")

    label("loc_C5E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CBF")
    SetMapObjFrame(0xFF, "sky01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky_y", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sky01_y", 0x1, 0x1)
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    OP_11(0xD5, 0x8F, 0x7B, 0x26, 0x1F4, 0x0)
    Jump("loc_CE8")

    label("loc_CBF")

    SetMapObjFrame(0xFF, "sky01", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sky_y", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky01_y", 0x0, 0x1)

    label("loc_CE8")

    OP_1B(0x3, 0x0, 0x26)
    OP_1B(0x2, 0x0, 0x27)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D01")
    OP_1B(0x0, 0x0, 0x28)

    label("loc_D01")

    OP_65(0x0, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C9, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C9, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D2E")
    OP_66(0x0, 0x1)

    label("loc_D2E")

    Return()

    # Function_2_9BD end

    def Function_3_D2F(): pass

    label("Function_3_D2F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DCE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DAE")

    #C0001
    ChrTalk(
        0xE,
        (
            "#00102Fほらティオちゃん、\x01",
            "こっち向いて。\x02\x03",

            "今、ツーショット写真を\x01",
            "撮ってあげるから。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_DC9")

    label("loc_DAE")


    #C0002
    ChrTalk(
        0xE,
        "#00102Fハイ、チーズ！\x02",
    )

    CloseMessageWindow()

    label("loc_DC9")

    Jump("loc_E21")

    label("loc_DCE")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DE4")
    Jump("loc_E21")

    label("loc_DE4")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DFA")
    Jump("loc_E21")

    label("loc_DFA")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E10")
    Jump("loc_E21")

    label("loc_E10")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E21")

    label("loc_E21")

    TalkEnd(0xFE)
    Return()

    # Function_3_D2F end

    def Function_4_E25(): pass

    label("Function_4_E25")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EC9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E4B")
    Call(0, 5)
    Jump("loc_EC4")

    label("loc_E4B")


    #C0003
    ChrTalk(
        0xF,
        (
            "#00204Fわたしはついに、\x01",
            "ついにテーマパークへと\x01",
            "やってきたんですね……\x02\x03",

            "#00202F……とりあえず、\x01",
            "みっしぃと握手を……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EC4")

    Jump("loc_1071")

    label("loc_EC9")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EDF")
    Jump("loc_1071")

    label("loc_EDF")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EF5")
    Jump("loc_1071")

    label("loc_EF5")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F0B")
    Jump("loc_1071")

    label("loc_F0B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1071")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FE8")

    #C0004
    ChrTalk(
        0xF,
        (
            "#00203Fわたしたちは、夜の部までは\x01",
            "ここに居られないんですよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x101,
        (
            "#00000Fああ、夜は迎賓館の方で\x01",
            "晩餐会に呼ばれてるからな。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0xF,
        "#00206F……はあ……\x02",
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x101,
        "#00012F（残念そうだ……）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1071")

    label("loc_FE8")


    #C0008
    ChrTalk(
        0xF,
        (
            "#00200F出来るなら、夜の部の\x01",
            "みっしぃのパレードを\x01",
            "見たかったですが……\x02\x03",

            "#00206F……まあ、今度の機会に\x01",
            "とっておくしかなさそうですね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1071")

    TalkEnd(0xFE)
    Return()

    # Function_4_E25 end

    def Function_5_1075(): pass

    label("Function_5_1075")

    OP_4B(0xF, 0xFF)
    OP_4B(0x14, 0xFF)

    #C0009
    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "やっほー、お嬢ちゃん。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "みししっ、楽しんでる～？\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0xF,
        "#00201F生みっしぃ……！\x02",
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x101,
        "#00009F（はは、本当に嬉しそうだな。）\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xF, 0x10)
    ClearChrFlags(0x14, 0x10)
    SetScenarioFlags(0x0, 2)
    OP_4C(0xF, 0xFF)
    OP_4C(0x14, 0xFF)
    Return()

    # Function_5_1075 end

    def Function_6_111D(): pass

    label("Function_6_111D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11F8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11B9")

    #C0013
    ChrTalk(
        0x10,
        (
            "#00303Fさーて、さっそくナンパにでも\x01",
            "しゃれこむとすっかね。\x02\x03",

            "#00309Fさあ、俺好みのお姉様は\x01",
            "どこにいるかな～っと。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_11F3")

    label("loc_11B9")


    #C0014
    ChrTalk(
        0x10,
        (
            "#00309Fさあ、俺好みのお姉様は\x01",
            "どこにいるかな～っと。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11F3")

    Jump("loc_124B")

    label("loc_11F8")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_120E")
    Jump("loc_124B")

    label("loc_120E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1224")
    Jump("loc_124B")

    label("loc_1224")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_123A")
    Jump("loc_124B")

    label("loc_123A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_124B")

    label("loc_124B")

    TalkEnd(0xFE)
    Return()

    # Function_6_111D end

    def Function_7_124F(): pass

    label("Function_7_124F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1268")
    Jump("loc_13C1")

    label("loc_1268")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1384")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1310")

    #C0015
    ChrTalk(
        0x11,
        (
            "#10105Fそういえば、\x01",
            "みっしぃは見かけましたけど\x01",
            "妹の『みーしぇ』がいませんね。\x02\x03",

            "#10103Fうーん、どこかに\x01",
            "隠れてるんでしょうか……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_137F")

    label("loc_1310")


    #C0016
    ChrTalk(
        0x11,
        (
            "#10100Fみっしぃの妹の『みーしぇ』って\x01",
            "どこにいるんでしょうね。\x02\x03",

            "#10103Fそのうち見つけられるんでしょうか。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_137F")

    Jump("loc_13C1")

    label("loc_1384")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_139A")
    Jump("loc_13C1")

    label("loc_139A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13B0")
    Jump("loc_13C1")

    label("loc_13B0")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13C1")

    label("loc_13C1")

    TalkEnd(0xFE)
    Return()

    # Function_7_124F end

    def Function_8_13C5(): pass

    label("Function_8_13C5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13DE")
    Jump("loc_1544")

    label("loc_13DE")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1507")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_148F")

    #C0017
    ChrTalk(
        0x12,
        (
            "#10300Fさっきイリアさんが休憩所から\x01",
            "セシルさんを引っ張っていったよ。\x02\x03",

            "#10303Fフフ、あれくらい強引な方が\x01",
            "女の子を誘うには向いてそうだね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_1502")

    label("loc_148F")


    #C0018
    ChrTalk(
        0x12,
        (
            "#10300Fイリアさんくらい強引な方が\x01",
            "女の子を誘うには向いてそうだね。\x02\x03",

            "#10309Fフフ、君も頑張ってみたらどうだい？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1502")

    Jump("loc_1544")

    label("loc_1507")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_151D")
    Jump("loc_1544")

    label("loc_151D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1533")
    Jump("loc_1544")

    label("loc_1533")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1544")

    label("loc_1544")

    TalkEnd(0xFE)
    Return()

    # Function_8_13C5 end

    def Function_9_1548(): pass

    label("Function_9_1548")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1561")
    Jump("loc_162C")

    label("loc_1561")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1577")
    Jump("loc_162C")

    label("loc_1577")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_158D")
    Jump("loc_162C")

    label("loc_158D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_161B")

    #C0019
    ChrTalk(
        0x8,
        (
            "#01111Fそーだ、あとでシズクに\x01",
            "みっしぃグッズのお土産を\x01",
            "買っていってあげないとー。\x02\x03",

            "#01106Fお小遣い、足りるかなー？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_162C")

    label("loc_161B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_162C")

    label("loc_162C")

    TalkEnd(0xFE)
    Return()

    # Function_9_1548 end

    def Function_10_1630(): pass

    label("Function_10_1630")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1649")
    Jump("loc_1798")

    label("loc_1649")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_165F")
    Jump("loc_1798")

    label("loc_165F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1675")
    Jump("loc_1798")

    label("loc_1675")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1787")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_170E")

    #C0020
    ChrTalk(
        0xA,
        (
            "#05900F私の持ってるチケットも\x01",
            "半分を切ったわ。\x02\x03",

            "#05902Fふふ、みんなに付き合って\x01",
            "色々乗っているとすぐだったわね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_1782")

    label("loc_170E")


    #C0021
    ChrTalk(
        0xA,
        (
            "#05900F私の持ってるチケットも\x01",
            "半分を切ったわ。\x02\x03",

            "#05903Fそろそろ夕方になりそうだし、\x01",
            "休憩所に戻ってようかしら。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1782")

    Jump("loc_1798")

    label("loc_1787")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1798")

    label("loc_1798")

    TalkEnd(0xFE)
    Return()

    # Function_10_1630 end

    def Function_11_179C(): pass

    label("Function_11_179C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17B5")
    Jump("loc_18A6")

    label("loc_17B5")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17CB")
    Jump("loc_18A6")

    label("loc_17CB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_187F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17EE")
    Call(0, 12)
    Jump("loc_187A")

    label("loc_17EE")


    #C0022
    ChrTalk(
        0xB,
        (
            "#01705Fね、ところで何か\x01",
            "気に入ったアトラクションは\x01",
            "あったかしら？\x02\x03",

            "#01702Fスリリングなヤツを\x01",
            "ハシゴしてるんだけど、\x01",
            "オススメとかない？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_187A")

    Jump("loc_18A6")

    label("loc_187F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1895")
    Jump("loc_18A6")

    label("loc_1895")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_18A6")

    label("loc_18A6")

    TalkEnd(0xFE)
    Return()

    # Function_11_179C end

    def Function_12_18AA(): pass

    label("Function_12_18AA")

    OP_4B(0xB, 0xFF)
    OP_4B(0xC, 0xFF)
    OP_4B(0xD, 0xFF)

    #C0023
    ChrTalk(
        0xB,
        (
            "#01700Fリーシャ、シュリ。\x01",
            "あんたたちも楽しんでる？\x02\x03",

            "#01709Fアーティストにも\x01",
            "気分転換は大事なんだから、\x01",
            "今日はパーっと遊びなさいよ？\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0xC,
        "#01809Fふふ、そうですね。\x02",
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0xD,
        (
            "#14003Fフ、フン、言われなくても\x01",
            "分かってるっての。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    OP_4C(0xB, 0xFF)
    OP_4C(0xC, 0xFF)
    OP_4C(0xD, 0xFF)
    Return()

    # Function_12_18AA end

    def Function_13_19A6(): pass

    label("Function_13_19A6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_19BF")
    Jump("loc_1AB3")

    label("loc_19BF")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_19D5")
    Jump("loc_1AB3")

    label("loc_19D5")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A8C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19F8")
    Call(0, 12)
    Jump("loc_1A87")

    label("loc_19F8")


    #C0026
    ChrTalk(
        0xC,
        (
            "#01805Fそういえば、\x01",
            "ホラーコースターの近辺は\x01",
            "絶叫系が多いみたいですけど。\x02\x03",

            "#01803Fあのあたりならイリアさんが\x01",
            "好きそうなのがあるんじゃ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A87")

    Jump("loc_1AB3")

    label("loc_1A8C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1AA2")
    Jump("loc_1AB3")

    label("loc_1AA2")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1AB3")

    label("loc_1AB3")

    TalkEnd(0xFE)
    Return()

    # Function_13_19A6 end

    def Function_14_1AB7(): pass

    label("Function_14_1AB7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1AD0")
    Jump("loc_1B8A")

    label("loc_1AD0")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1AE6")
    Jump("loc_1B8A")

    label("loc_1AE6")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B63")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B09")
    Call(0, 12)
    Jump("loc_1B5E")

    label("loc_1B09")


    #C0027
    ChrTalk(
        0xD,
        (
            "#14006Fんなことより、なんだか\x01",
            "腹がへってきたよ。\x02\x03",

            "#14000F休憩所で何か食べない？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B5E")

    Jump("loc_1B8A")

    label("loc_1B63")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B79")
    Jump("loc_1B8A")

    label("loc_1B79")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B8A")

    label("loc_1B8A")

    TalkEnd(0xFE)
    Return()

    # Function_14_1AB7 end

    def Function_15_1B8E(): pass

    label("Function_15_1B8E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1C10")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1BB4")
    Call(0, 5)
    Jump("loc_1C0B")

    label("loc_1BB4")


    #C0028
    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "みししっ、\x01",
            "ワンダーランドにようこそっ☆\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "お兄さんも楽しんでってネ～！\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C0B")

    Jump("loc_20E0")

    label("loc_1C10")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1C26")
    Jump("loc_20E0")

    label("loc_1C26")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1C3C")
    Jump("loc_20E0")

    label("loc_1C3C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1FB2")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1DF5")

    #C0030
    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "みししっ、話は聞いてるよ～。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "がんばってボクの妹の\x01",
            "みーしぇを探してみてネ～☆\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "……それとも、ギブアップする？\x07\x00\x02",
        )
    )

    CloseMessageWindow()
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
            "【ギブアップしない】\x01",      # 0
            "【ギブアップする】\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1DED")

    #C0033
    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "そっか～。\x01",
            "それじゃあがんばってネ☆\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "どうしても分からなかったら、\x01",
            "ボクの方からみーしぇに\x01",
            "ギブアップを伝えるからネ～。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DF0")

    label("loc_1DED")

    Call(0, 43)

    label("loc_1DF0")

    Jump("loc_1FAD")

    label("loc_1DF5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1E83")

    #C0035
    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "みーしぇとのかくれんぼに\x01",
            "勝ったんだってネ～。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "みししっ、その景品は\x01",
            "なかなかいいものだから\x01",
            "大切にしてネ～。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1FAD")

    label("loc_1E83")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x40)"), scpexpr(EXPR_END)), "loc_1F27")

    #C0037
    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "みーしぇとの\x01",
            "かくれんぼに負けたからって\x01",
            "気を落とさないでネ～。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "思う存分アトラクションで遊んで、\x01",
            "悔しい気持ちを吹っ飛ばそうヨ～☆\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1FAD")

    label("loc_1F27")


    #C0039
    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "ねーねー、ボクにそっくりの、\x01",
            "ピンク色の女の子を見なかった？\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "ボクの妹なんだけど……\x01",
            "ん～、どこに行ったんだろうネ～？\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1FAD")

    Jump("loc_20E0")

    label("loc_1FB2")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_20E0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2063")

    #C0041
    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "みししっ、ありがと～！\x01",
            "ボク、絶対がんばるネ～！\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "夜になるまでは\x01",
            "まだちょっと時間があるから、\x01",
            "最後まで楽しんでってネ～！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x14, 0x10)
    SetScenarioFlags(0x1, 0)
    Jump("loc_20E0")

    label("loc_2063")


    #C0043
    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "ボクが一番好きなのは\x01",
            "子供たちの笑顔なんだ～。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "みししっ、ちなみに\x01",
            "二番目に好きなのは\x01",
            "でっかいメロンだヨ～。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    label("loc_20E0")

    TalkEnd(0xFE)
    Return()

    # Function_15_1B8E end

    def Function_16_20E4(): pass

    label("Function_16_20E4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_20FD")
    Jump("loc_2174")

    label("loc_20FD")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2113")
    Jump("loc_2174")

    label("loc_2113")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2129")
    Jump("loc_2174")

    label("loc_2129")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_213F")
    Jump("loc_2174")

    label("loc_213F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2174")

    #C0045
    ChrTalk(
        0xFE,
        "ああ……本当に来てよかったよ。\x02",
    )

    CloseMessageWindow()

    label("loc_2174")

    TalkEnd(0xFE)
    Return()

    # Function_16_20E4 end

    def Function_17_2178(): pass

    label("Function_17_2178")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2191")
    Jump("loc_221D")

    label("loc_2191")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_21A7")
    Jump("loc_221D")

    label("loc_21A7")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_21BD")
    Jump("loc_221D")

    label("loc_21BD")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_21D3")
    Jump("loc_221D")

    label("loc_21D3")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_221D")

    #C0046
    ChrTalk(
        0xFE,
        (
            "ふふ……見て、あなた。\x01",
            "リマがあんなに嬉しそうだわ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_221D")

    TalkEnd(0xFE)
    Return()

    # Function_17_2178 end

    def Function_18_2221(): pass

    label("Function_18_2221")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_223A")
    Jump("loc_22E0")

    label("loc_223A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2250")
    Jump("loc_22E0")

    label("loc_2250")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2266")
    Jump("loc_22E0")

    label("loc_2266")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_227C")
    Jump("loc_22E0")

    label("loc_227C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_22E0")

    #C0047
    ChrTalk(
        0xFE,
        "わーい、みっしぃ～！\x02",
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0xFE,
        (
            "リマは夜の部にはいないけど、\x01",
            "パレード頑張ってね～！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_22E0")

    TalkEnd(0xFE)
    Return()

    # Function_18_2221 end

    def Function_19_22E4(): pass

    label("Function_19_22E4")

    TalkBegin(0xFE)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_22F1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_24E7")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "話す\x01",              # 0
            "買い物をする\x01",      # 1
            "やめる\x01",            # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_234B")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_234B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_236B")
    OP_AF(0x6C)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_24E2")

    label("loc_236B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_237F")
    Jump("loc_24E2")

    label("loc_237F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2397")
    TalkEnd(0xFE)
    Return()

    label("loc_2397")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_24E2")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2457")

    #C0049
    ChrTalk(
        0x18,
        (
            "いらっしゃいませー。\x01",
            "ここではみっしぃグッズを\x01",
            "多数取り扱ってますよ～！\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x18,
        (
            "あなたもみっしぃテイルをつけて、\x01",
            "テーマパークを楽しみましょう！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_24E2")

    label("loc_2457")


    #C0051
    ChrTalk(
        0x18,
        (
            "テーマパークの思い出に\x01",
            "みっしぃグッズはいかがですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x18,
        (
            "クロスベル市に帰るまで、\x01",
            "みっしぃテイルをつけてる人も\x01",
            "意外と多いんですよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_24E2")

    Jump("loc_22F1")

    label("loc_24E7")

    TalkEnd(0xFE)
    Return()

    # Function_19_22E4 end

    def Function_20_24EB(): pass

    label("Function_20_24EB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_253D")

    #C0053
    ChrTalk(
        0xFE,
        (
            "あっちの方に新しく出来た\x01",
            "アトラクションに行こうぜ！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2568")

    label("loc_253D")


    #C0054
    ChrTalk(
        0xFE,
        (
            "折角だから夜の部まで\x01",
            "残っていこうぜ！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2568")

    TalkEnd(0xFE)
    Return()

    # Function_20_24EB end

    def Function_21_256C(): pass

    label("Function_21_256C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_259D")

    #C0055
    ChrTalk(
        0xFE,
        "次はどこにいくー？\x02",
    )

    CloseMessageWindow()
    Jump("loc_25AF")

    label("loc_259D")


    #C0056
    ChrTalk(
        0xFE,
        "もう帰るー？\x02",
    )

    CloseMessageWindow()

    label("loc_25AF")

    TalkEnd(0xFE)
    Return()

    # Function_21_256C end

    def Function_22_25B3(): pass

    label("Function_22_25B3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_262D")

    #C0057
    ChrTalk(
        0xFE,
        (
            "私たちはテーマパークの\x01",
            "年間フリーパスを持ってるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0xFE,
        "何回来ても飽きないよ、ＭＷＬは！\x02",
    )

    CloseMessageWindow()
    Jump("loc_262D")

    label("loc_262D")

    TalkEnd(0xFE)
    Return()

    # Function_22_25B3 end

    def Function_23_2631(): pass

    label("Function_23_2631")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_26B8")

    #C0059
    ChrTalk(
        0xFE,
        (
            "この子ったらみっしぃが\x01",
            "とっても大好きなのよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0xFE,
        (
            "私も何度も来ているうちに\x01",
            "すっかりハマっちゃったわ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_26B8")

    label("loc_26B8")

    TalkEnd(0xFE)
    Return()

    # Function_23_2631 end

    def Function_24_26BC(): pass

    label("Function_24_26BC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2702")

    #C0061
    ChrTalk(
        0xFE,
        (
            "買って買って～、\x01",
            "ぬいぐるみ買ってよ～！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2702")

    label("loc_2702")

    TalkEnd(0xFE)
    Return()

    # Function_24_26BC end

    def Function_25_2706(): pass

    label("Function_25_2706")

    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    SetChrFlags(0x19, 0x10)
    ClearChrFlags(0x1A, 0x80)
    SetChrFlags(0x1A, 0x10)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1D, 0x80)
    SetChrFlags(0x1D, 0x10)
    SetChrFlags(0x29, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_27C1")
    EndChrThread(0xE, 0x0)
    SetChrChipByIndex(0xE, 0x16)
    SetChrSubChip(0xE, 0x0)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, -5160, 0, 3100, 315)
    SetChrFlags(0xE, 0x10)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, -7100, 0, 4400, 315)
    SetChrFlags(0xF, 0x10)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 6000, 0, -150, 180)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x14, -8010, 0, 5260, 135)
    SetChrFlags(0x14, 0x10)
    Jump("loc_29BC")

    label("loc_27C1")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2814")
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, -9350, 0, 6350, 135)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, -7930, 200, 8240, 135)
    SetChrChipByIndex(0x12, 0x18)
    SetChrSubChip(0x12, 0x0)
    EndChrThread(0x12, 0x0)
    SetChrBattleFlags(0x12, 0x4)
    Jump("loc_29BC")

    label("loc_2814")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_287B")
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, -8320, 0, -2390, 180)
    SetChrFlags(0xB, 0x10)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, -7690, 0, -3590, 270)
    SetChrFlags(0xC, 0x10)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, -9110, 0, -3590, 90)
    SetChrFlags(0xD, 0x10)
    Jump("loc_29BC")

    label("loc_287B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_293C")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 7600, 0, -360, 0)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, -7930, 200, 8240, 135)
    SetChrChipByIndex(0xA, 0x19)
    SetChrSubChip(0xA, 0x0)
    EndChrThread(0xA, 0x0)
    SetChrBattleFlags(0xA, 0x4)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x14, 0, 0, -6210, 180)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_291C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 4)), scpexpr(EXPR_END)), "loc_290E")
    SetChrFlags(0x8, 0x80)
    Jump("loc_291C")

    label("loc_290E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 6)), scpexpr(EXPR_END)), "loc_291C")
    SetChrFlags(0xA, 0x80)

    label("loc_291C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C9, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C9, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2937")
    ClearChrFlags(0x29, 0x80)

    label("loc_2937")

    Jump("loc_29BC")

    label("loc_293C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_29BC")
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, -7930, 200, 8240, 135)
    SetChrChipByIndex(0xF, 0x17)
    SetChrSubChip(0xF, 0x0)
    EndChrThread(0xF, 0x0)
    SetChrBattleFlags(0xF, 0x4)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x14, -4700, 0, 8680, 180)
    SetChrFlags(0x14, 0x10)
    ClearChrFlags(0x15, 0x80)
    SetChrFlags(0x15, 0x10)
    ClearChrFlags(0x16, 0x80)
    SetChrFlags(0x16, 0x10)
    ClearChrFlags(0x17, 0x80)
    SetChrFlags(0x17, 0x10)
    SetChrFlags(0x1B, 0x80)
    SetChrFlags(0x1C, 0x80)
    SetChrFlags(0x1D, 0x80)

    label("loc_29BC")

    Return()

    # Function_25_2706 end

    def Function_26_29BD(): pass

    label("Function_26_29BD")

    EventBegin(0x1)

    #C0062
    ChrTalk(
        0x101,
        (
            "#0000F◆この先は大観覧車と休憩所か。\x01",
            "どこに行こうかな。\x02",
        )
    )

    CloseMessageWindow()

    Menu(
        0,
        -1,
        240,
        1,
        (
            "大観覧車へ向かう\x01",      # 0
            "休憩所へ向かう\x01",        # 1
            "やめる\x01",                # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2A48"),
        (1, "loc_2A61"),
        (SWITCH_DEFAULT, "loc_2A7A"),
    )


    label("loc_2A48")

    FadeToDark(500, 0, -1)
    OP_0D()
    NewScene("t1330", 100, 0, 0)
    IdleLoop()
    Jump("loc_2A92")

    label("loc_2A61")

    FadeToDark(500, 0, -1)
    OP_0D()
    NewScene("t1370", 100, 0, 0)
    IdleLoop()
    Jump("loc_2A92")

    label("loc_2A7A")

    SetChrPos(0x0, -11020, 0, 4080, 135)
    EventEnd(0x4)
    Jump("loc_2A92")

    label("loc_2A92")

    Return()

    # Function_26_29BD end

    def Function_27_2A93(): pass

    label("Function_27_2A93")

    EventBegin(0x1)

    #C0063
    ChrTalk(
        0x101,
        (
            "#0000F◆この先はホラーコースターと占い館か。\x01",
            "どこに行こうかな。\x02",
        )
    )

    CloseMessageWindow()

    Menu(
        0,
        -1,
        240,
        1,
        (
            "ホラーコースターへ向かう\x01",      # 0
            "占い館へ向かう\x01",                # 1
            "やめる\x01",                        # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2B2E"),
        (1, "loc_2B47"),
        (SWITCH_DEFAULT, "loc_2B60"),
    )


    label("loc_2B2E")

    FadeToDark(500, 0, -1)
    OP_0D()
    NewScene("t1350", 100, 0, 0)
    IdleLoop()
    Jump("loc_2B78")

    label("loc_2B47")

    FadeToDark(500, 0, -1)
    OP_0D()
    NewScene("t1380", 100, 0, 0)
    IdleLoop()
    Jump("loc_2B78")

    label("loc_2B60")

    SetChrPos(0x0, 10670, 0, 4280, 225)
    EventEnd(0x4)
    Jump("loc_2B78")

    label("loc_2B78")

    Return()

    # Function_27_2A93 end

    def Function_28_2B79(): pass

    label("Function_28_2B79")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_4B(0x8, 0xFF)
    OP_4B(0xF, 0xFF)
    OP_4B(0xE, 0xFF)
    OP_4B(0x10, 0xFF)
    OP_4B(0x11, 0xFF)
    OP_4B(0x12, 0xFF)
    OP_4B(0xA, 0xFF)
    OP_4B(0xB, 0xFF)
    OP_4B(0xD, 0xFF)
    OP_4B(0xC, 0xFF)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0x13, 0x80)
    LoadChrToIndex("chr/ch02702.itc", 0x1E)
    ClearChrFlags(0x8, 0x4)
    ClearChrFlags(0xF, 0x4)
    ClearChrFlags(0xE, 0x4)
    ClearChrFlags(0x10, 0x4)
    ClearChrFlags(0x11, 0x4)
    ClearChrFlags(0x12, 0x4)
    ClearChrFlags(0xA, 0x4)
    ClearChrFlags(0xB, 0x4)
    ClearChrFlags(0xD, 0x4)
    ClearChrFlags(0xC, 0x4)
    ClearChrFlags(0x9, 0x4)
    ClearChrFlags(0x13, 0x4)
    OP_90(0x101, 0, 5000, -27000, 0)
    OP_90(0x8, -1280, 5000, -27940, 0)
    OP_90(0xF, 200, 5000, -28510, 0)
    OP_90(0xE, 1130, 5000, -28360, 0)
    OP_90(0xA, -1730, 5000, -29480, 0)
    OP_90(0xB, -650, 5000, -29360, 0)
    OP_90(0xD, 580, 5000, -29850, 0)
    OP_90(0xC, 1700, 5000, -29810, 0)
    OP_90(0x11, -340, 5000, -30690, 0)
    OP_90(0x9, -1340, 5000, -30960, 0)
    OP_90(0x12, 1010, 5000, -31210, 0)
    OP_90(0x10, -850, 5000, -32340, 0)
    OP_90(0x13, 400, 5000, -32700, 0)
    OP_68(0, 1800, -24500, 0)
    MoveCamera(0, 36, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(24000, 0)
    FadeToBright(1000, 0)
    OP_68(0, 9000, -500, 9000)
    MoveCamera(0, 3, 0, 9000)
    SetCameraDistance(66000, 9000)
    PlaceName2(340, 200, "c_plac46", 0x0, 5000)

    def lambda_2D7A():
        OP_9B(0x0, 0xFE, 0x0, 0x4E20, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2D7A)

    def lambda_2D8F():
        OP_9B(0x0, 0xFE, 0x0, 0x4E20, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2D8F)
    Sleep(50)

    def lambda_2DA7():
        OP_9B(0x0, 0xFE, 0x0, 0x4E20, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_2DA7)

    def lambda_2DBC():
        OP_9B(0x0, 0xFE, 0x0, 0x4E20, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_2DBC)
    Sleep(50)

    def lambda_2DD4():
        OP_9B(0x0, 0xFE, 0x0, 0x4E20, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_2DD4)

    def lambda_2DE9():
        OP_9B(0x0, 0xFE, 0x0, 0x4E20, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_2DE9)

    def lambda_2DFE():
        OP_9B(0x0, 0xFE, 0x0, 0x4E20, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_2DFE)
    Sleep(50)

    def lambda_2E16():
        OP_9B(0x0, 0xFE, 0x0, 0x4E20, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_2E16)

    def lambda_2E2B():
        OP_9B(0x0, 0xFE, 0x0, 0x4E20, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_2E2B)

    def lambda_2E40():
        OP_9B(0x0, 0xFE, 0x0, 0x4E20, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_2E40)
    Sleep(50)

    def lambda_2E58():
        OP_9B(0x0, 0xFE, 0x0, 0x4E20, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_2E58)

    def lambda_2E6D():
        OP_9B(0x0, 0xFE, 0x0, 0x4E20, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2E6D)

    def lambda_2E82():
        OP_9B(0x0, 0xFE, 0x0, 0x4E20, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_2E82)
    OP_6F(0x79)
    Fade(1000)
    OP_68(0, 1000, 0, 0)
    OP_68(0, 1000, -8000, 5500)
    MoveCamera(0, 22, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17500, 0)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x8, 1)
    Sleep(300)
    #Sound(3033, 255, 100, 0)    #voice#KeA

    #C0064
    ChrTalk(
        0x8,
        "#01109F#15A#4Sうわあああっ……！\x02",
    )
    #Auto

    CloseMessageWindow()
    WaitChrThread(0xF, 1)
    WaitChrThread(0xE, 1)
    WaitChrThread(0x10, 1)
    WaitChrThread(0x11, 1)
    WaitChrThread(0x12, 1)
    WaitChrThread(0xA, 1)
    WaitChrThread(0xB, 1)
    WaitChrThread(0xD, 1)
    WaitChrThread(0xC, 1)
    WaitChrThread(0x9, 1)
    WaitChrThread(0x13, 1)
    SetChrFlags(0x8, 0x4)
    SetChrFlags(0xF, 0x4)
    SetChrFlags(0xE, 0x4)
    SetChrFlags(0x10, 0x4)
    SetChrFlags(0x11, 0x4)
    SetChrFlags(0x12, 0x4)
    SetChrFlags(0xA, 0x4)
    SetChrFlags(0xB, 0x4)
    SetChrFlags(0xD, 0x4)
    SetChrFlags(0xC, 0x4)
    SetChrFlags(0x9, 0x4)
    SetChrFlags(0x13, 0x4)
    SetChrChipByIndex(0x13, 0x1E)
    SetChrSubChip(0x13, 0x0)
    BeginChrThread(0x13, 3, 0, 0)
    OP_6F(0x79)
    Sleep(300)

    #C0065
    ChrTalk(
        0x101,
        "#00002FここがＭ・Ｗ・Ｌ#10Rミシュラム・ワンダーランド#……\x02",
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0xF,
        "#00203F……………………（じいぃん）\x02",
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0xD,
        "#14005F……す、すげーな……\x02",
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0xB,
        (
            "#01705Fへえ、あたしも初めてだけど\x01",
            "なかなか楽しめそうじゃない。\x02\x03",

            "#01709Fアトラクションとかも\x01",
            "結構あるのよね？\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x10,
        (
            "#00309Fま、正直１日くらいじゃ\x01",
            "回りきれないほどあるッスね。\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x12,
        (
            "#10304F今日はビーチで昼過ぎまで\x01",
            "過ごしちゃったし……\x02\x03",

            "#10302F今からだと、代表的なものを\x01",
            "中心に回った方がよさそうだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0xA,
        (
            "#05905F代表的なものというと\x01",
            "どんなものになるのかしら？\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0x9,
        (
            "#06403Fうーん、やっぱり左手に見える\x01",
            "観覧車は外せませんねー。\x02",
        )
    )

    CloseMessageWindow()
    OP_68(0, 10500, -7500, 3000)
    MoveCamera(325, 0, 0, 3000)
    OP_6E(600, 3000)
    SetCameraDistance(11000, 3000)
    OP_6F(0x79)

    #C0073
    ChrTalk(
        0x9,
        (
            "#06409Fファミリー、カップル、\x01",
            "どちらにも人気があります。\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x11,
        (
            "#10109F眺めはとにかく最高ですよ。\x02\x03",

            "#10102F最後の締めに取っておいても\x01",
            "いい場所かもしれません。\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0xB,
        "#01702Fふむふむ、なるほど。\x02",
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0xC,
        (
            "#01809Fふふっ……\x01",
            "ワクワクしてきますね。\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0xE,
        (
            "#00102F代表的なものというと……\x01",
            "中央の『城』は正にそうですね。\x02",
        )
    )

    CloseMessageWindow()
    OP_68(0, 10500, -7500, 3000)
    MoveCamera(0, 0, 0, 3000)
    OP_6E(600, 3000)
    SetCameraDistance(11000, 3000)
    OP_6F(0x79)

    #C0078
    ChrTalk(
        0xE,
        (
            "#00100F《鏡の城》──このテーマパークの\x01",
            "モニュメント的な場所だそうです。\x02\x03",

            "#00104F『願いを叶える鏡』というのが\x01",
            "最上階に置かれているらしくて……\x02\x03",

            "#00102F鐘を鳴らして鏡の前に立つと\x01",
            "願いが叶うなんて言われていますね。\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0xA,
        "#05909Fあら、ロマンチックね。\x02",
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0x10,
        (
            "#00304Fま、やっぱりカップルとか\x01",
            "ファミリーが多いッスね。\x02\x03",

            "#00300Fなにせ、その鐘を鳴らすハンドルが\x01",
            "左右に２つ付いてるくらいだし。\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0x101,
        (
            "#00011Fた、確かにそれは\x01",
            "一人で鳴らすと切なそうだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x8,
        "#01101Fねえねえ！\x02",
    )

    CloseMessageWindow()
    OP_68(0, 10500, -7500, 3000)
    MoveCamera(35, 0, 0, 3000)
    OP_6E(600, 3000)
    SetCameraDistance(11000, 3000)
    OP_6F(0x79)

    #C0083
    ChrTalk(
        0x8,
        (
            "#01110Fあっちに見えるお屋敷って\x01",
            "誰か住んでるのー？\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0xD,
        (
            "#14011Fな、なんかやたらと\x01",
            "不気味そうな屋敷だな……\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0x10,
        (
            "#00305Fありゃ俺も知らねぇな……\x01",
            "最近できたアトラクションか？\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x9,
        (
            "#06404Fええ、テーマパークでも\x01",
            "一番新しい施設みたいですねー。\x02\x03",

            "#06402F『ホラーコースター』といって\x01",
            "かなり本格的らしいですよ～？\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0xF,
        (
            "#00204Fその情報でしたら\x01",
            "わたしも調べておきました。\x02\x03",

            "#00202Fどうやら最新技術を駆使した\x01",
            "怖ろしくもエキサイティングな\x01",
            "アトラクションのようですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0xE,
        (
            "#00106Fそ、そんなものが\x01",
            "新しく出来たんだ……\x02\x03",

            "#00111F……ベルったら一言も\x01",
            "教えてくれなかったわね……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    SetChrPos(0x101, -300, 0, -7000, 180)
    SetChrPos(0x8, -1280, 0, -7940, 135)
    SetChrPos(0xF, 200, 0, -8510, 180)
    SetChrPos(0xE, 1130, 0, -8360, 225)
    SetChrPos(0xA, -1730, 0, -9280, 90)
    SetChrPos(0xB, -750, 0, -9360, 90)
    SetChrPos(0xD, 580, 0, -9850, 270)
    SetChrPos(0xC, 1700, 0, -9810, 270)
    SetChrPos(0x11, -340, 0, -10940, 0)
    SetChrPos(0x9, -1340, 0, -10960, 45)
    SetChrPos(0x12, 1010, 0, -11210, 315)
    SetChrPos(0x10, -850, 0, -12340, 0)
    SetChrPos(0x13, 400, 0, -12700, 0)
    OP_68(0, 1500, -9600, 0)
    OP_68(0, 1000, -9600, 2000)
    MoveCamera(315, 20, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15000, 0)
    OP_6F(0x79)
    OP_0D()

    #C0089
    ChrTalk(
        0xB,
        (
            "#01709Fうんうん、いいわね！\x01",
            "テンション上がってきたわ。\x02\x03",

            "#01700F他に定番は無いのかしら？\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x12,
        (
            "#10304F#6Pアトラクションじゃないけど\x01",
            "『占いの館』ってのも定番だね。\x02\x03",

            "#10300F何でも、去年入った占い師が\x01",
            "かなりの凄腕だっていう噂だよ？\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x9,
        (
            "#06403F相性占いから失せ物探しまで\x01",
            "何でもござれって話ですよねー。\x02\x03",

            "#06400Fエキゾチックで謎めいた\x01",
            "美人の占い師さんらしいです。\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0xC,
        (
            "#01805F#12Pそれは……\x01",
            "ちょっと気になりますね。\x02\x03",

            "#01808F（東方系の占術師かしら……？）\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0xF,
        (
            "#00203F……それを言うなら\x01",
            "『みっしぃ』の追っかけも\x01",
            "外せないのではないかと。\x02\x03",

            "#00201Fパークを巡回している彼を\x01",
            "追いかけていくという趣向です。\x02\x03",

            "#00207F運がよければ彼の妹である\x01",
            "『みーしぇ』というキャラにも\x01",
            "会うことが出来るとか……！\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x101,
        "#00012F#11Pそ、そうなのか。\x02",
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0x10,
        "#00301F#6Pティオすけの目がマジだぜ……\x02",
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0096
    ChrTalk(
        0xA,
        (
            "#05905Fそういえば……\x02\x03",

            "#05900F休憩できる場所というのは\x01",
            "どこかにあるのかしら？\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x11, 0x13B, 0x1F4)

    #C0097
    ChrTalk(
        0x11,
        (
            "#10105F#6Pああ、左のアーケード方面に\x01",
            "休憩所がありますよ。\x02\x03",

            "#10100Fちょっとした軽食なんかも\x01",
            "出されていたと思います。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_68(0, 1300, -9600, 1500)

    def lambda_3CB1():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3CB1)

    def lambda_3CBE():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_3CBE)
    Sleep(50)

    def lambda_3CCE():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF, 2, lambda_3CCE)

    def lambda_3CDB():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_3CDB)
    Sleep(50)

    def lambda_3CEB():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_3CEB)

    def lambda_3CF8():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_3CF8)
    Sleep(50)

    def lambda_3D08():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_3D08)

    def lambda_3D15():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_3D15)
    Sleep(50)

    def lambda_3D25():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_3D25)

    def lambda_3D32():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_3D32)
    Sleep(50)

    def lambda_3D42():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_3D42)

    def lambda_3D4F():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_3D4F)

    def lambda_3D5C():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_3D5C)
    WaitChrThread(0x101, 2)
    WaitChrThread(0x8, 2)
    WaitChrThread(0xF, 2)
    WaitChrThread(0xE, 2)
    WaitChrThread(0xA, 2)
    WaitChrThread(0xB, 2)
    WaitChrThread(0xD, 2)
    WaitChrThread(0xC, 2)
    WaitChrThread(0x11, 2)
    WaitChrThread(0x9, 2)
    WaitChrThread(0x12, 2)
    WaitChrThread(0x10, 2)
    WaitChrThread(0x13, 2)
    OP_6F(0x79)

    #C0098
    ChrTalk(
        0xA,
        (
            "#05904Fなら、そこを中心に\x01",
            "集まるといいかもしれないわね。\x02\x03",

            "#05902Fなるべく私は居るようにするから\x01",
            "みんな貧血とか、具合が悪くなったら\x01",
            "遠慮なく来てね？\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0x101,
        (
            "#00006F#11Pセシル姉、こんな時まで\x01",
            "看護師魂を発揮しなくても……\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0xE,
        "#00108F#12Pええ、さすがに申し訳ないです。\x02",
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0x10,
        (
            "#00303F#6P……しかし考えてみりゃ、\x01",
            "セシルさんに介抱してもらえる\x01",
            "絶好のチャンスってことかッ！\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0xF,
        (
            "#00211F#12Pランディさん。\x01",
            "本音は控えた方がいいかと。\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0xB,
        (
            "#01706F#11Pまあ、程々にして\x01",
            "あんたも楽しみなさいよね？\x02\x03",

            "#01702F普段遊んでないんだから\x01",
            "こんな時こそはしゃがないと！\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0xA,
        (
            "#05909Fふふ、分かったわ。\x01",
            "それじゃあお言葉に甘えて。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_68(0, 1000, -9600, 1500)
    Sleep(500)

    def lambda_4010():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4010)
    Sleep(50)

    def lambda_4020():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_4020)
    Sleep(50)

    def lambda_4030():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF, 2, lambda_4030)
    Sleep(50)

    def lambda_4040():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_4040)
    Sleep(50)

    def lambda_4050():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_4050)
    Sleep(50)

    def lambda_4060():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_4060)
    Sleep(50)

    def lambda_4070():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_4070)
    Sleep(50)

    def lambda_4080():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_4080)
    Sleep(50)

    def lambda_4090():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_4090)
    Sleep(50)

    def lambda_40A0():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_40A0)
    Sleep(50)

    def lambda_40B0():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_40B0)
    Sleep(50)

    def lambda_40C0():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_40C0)
    Sleep(50)

    def lambda_40D0():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_40D0)
    WaitChrThread(0x101, 2)
    WaitChrThread(0x8, 2)
    WaitChrThread(0xF, 2)
    WaitChrThread(0xE, 2)
    WaitChrThread(0xA, 2)
    WaitChrThread(0xB, 2)
    WaitChrThread(0xD, 2)
    WaitChrThread(0xC, 2)
    WaitChrThread(0x11, 2)
    WaitChrThread(0x9, 2)
    WaitChrThread(0x12, 2)
    WaitChrThread(0x10, 2)
    WaitChrThread(0x13, 2)
    OP_6F(0x79)

    #C0105
    ChrTalk(
        0x101,
        (
            "#00003F#11P──晩餐会があるから\x01",
            "遊べるのは夕方まで……\x02\x03",

            "#00000Fみんな、チケットを渡すから\x01",
            "ここからは自由行動にしよう。\x02\x03",

            "#00002F遊びたいアトラクションがあれば\x01",
            "それぞれ適当に組んで入る……\x02\x03",

            "そんな感じでいいかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0xE,
        "#00109F#6Pええ、いいんじゃないかしら。\x02",
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0xF,
        "#00204F#6P了解です。\x02",
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0xC,
        "#01802F#6P分かりました。\x02",
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0x10,
        "#00309F#6Pおーし、遊ぶぞ～！\x02",
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0x9,
        "#06409F#6PテンションＭＡＸですー！\x02",
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0x11,
        "#10112F#6Pあはは……\x02",
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0x12,
        "#10304F#6Pやれやれ、元気だねぇ。\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    OP_93(0x8, 0x87, 0x1F4)
    OP_9B(0x0, 0x8, 0x0, 0x1F4, 0x7D0, 0x0)

    #C0113
    ChrTalk(
        0x8,
        (
            "#01109F#5Pねえシュリ！\x01",
            "いっしょにまわろ～！？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)
    OP_93(0xD, 0x13B, 0x1F4)
    Sleep(1000)
    OP_64(0xD)

    #C0114
    ChrTalk(
        0xD,
        "#14011F#12Pだ、だから引っ張るなって！\x02",
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0xB,
        (
            "#01709F#6Pあはは、何だか\x01",
            "学生時代を思い出すわねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0xA,
        "#05909F#6Pふふ、そうね。\x02",
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0x13,
        "#01203F#6Pグルルル……ウォン。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMessageWindowPos(-1, -1, -1, -1)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0118
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x35D),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を５枚手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    AddItemNumber(0x35D, 5)
    Sleep(300)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0119
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "テーマパークでは\x01",
            "『観覧車』『鏡の城』『占いの館』\x01",
            "『ホラーコースター』の４つが楽しめます。\x02\x03",

            "それぞれ受付でパートナーを選択し、\x01",
            "チケットを１枚消費することで\x01",
            "アトラクションを楽しむ事が出来ます。\x02\x03",

            "５枚全てを使うとストーリーが進行するため\x01",
            "誰とどのアトラクションを楽しむか\x01",
            "よく考えて使用して下さい。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetChrPos(0x0, 0, 0, -6750, 0)
    SetScenarioFlags(0x145, 4)
    OP_29(0xA5, 0x1, 0x6)
    EndChrThread(0x13, 0x3)
    SetChrChipByIndex(0x13, 0xB)
    SetChrSubChip(0x13, 0x0)
    OP_49()
    OP_D7(0x1E)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0x13, 0x80)
    OP_4C(0x8, 0xFF)
    OP_4C(0xF, 0xFF)
    OP_4C(0xE, 0xFF)
    OP_4C(0x10, 0xFF)
    OP_4C(0x11, 0xFF)
    OP_4C(0x12, 0xFF)
    OP_4C(0xA, 0xFF)
    OP_4C(0xB, 0xFF)
    OP_4C(0xD, 0xFF)
    OP_4C(0xC, 0xFF)
    Call(0, 25)
    EventEnd(0x5)
    Return()

    # Function_28_2B79 end

    def Function_29_461A(): pass

    label("Function_29_461A")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis416.itp")
    OP_4B(0x8, 0xFF)
    OP_4B(0xF, 0xFF)
    OP_4B(0xE, 0xFF)
    OP_4B(0x10, 0xFF)
    OP_4B(0x11, 0xFF)
    OP_4B(0x12, 0xFF)
    OP_4B(0xA, 0xFF)
    OP_4B(0xB, 0xFF)
    OP_4B(0xD, 0xFF)
    OP_4B(0xC, 0xFF)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x8, 0x4)
    ClearChrFlags(0xF, 0x4)
    ClearChrFlags(0xE, 0x4)
    ClearChrFlags(0x10, 0x4)
    ClearChrFlags(0x11, 0x4)
    ClearChrFlags(0x12, 0x4)
    ClearChrFlags(0xA, 0x4)
    ClearChrFlags(0xB, 0x4)
    ClearChrFlags(0xD, 0x4)
    ClearChrFlags(0xC, 0x4)
    ClearChrFlags(0x9, 0x4)
    ClearChrFlags(0x13, 0x4)
    SetChrPos(0x8, 0, 0, -10000, 0)
    SetChrPos(0xF, -1000, 0, -10000, 0)
    SetChrPos(0x9, 1000, 0, -10000, 0)
    SetChrPos(0xA, -1500, 0, -11250, 0)
    SetChrPos(0xB, -500, 0, -11250, 0)
    SetChrPos(0xD, 500, 0, -11250, 0)
    SetChrPos(0xC, 1500, 0, -11250, 0)
    SetChrPos(0x11, -1000, 0, -12500, 0)
    SetChrPos(0xE, 0, 0, -12500, 0)
    SetChrPos(0x12, 1000, 0, -12500, 0)
    SetChrPos(0x10, -500, 0, -13750, 0)
    SetChrPos(0x101, 500, 0, -13750, 0)
    SetChrPos(0x13, -1500, 0, -15000, 0)
    SetChrChipByIndex(0xF, 0x7)
    SetChrFlags(0xF, 0x8000)
    OP_4B(0x14, 0xFF)
    ClearChrFlags(0x14, 0x80)
    SetChrFlags(0x14, 0x8000)
    SetChrPos(0x14, 0, 0, -7500, 180)
    OP_4B(0x18, 0xFF)
    ClearChrFlags(0x18, 0x80)
    SetChrFlags(0x18, 0x8000)
    SetChrPos(0x18, 1000, 0, -7000, 180)
    SetMapObjFrame(0xFF, "sky01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky_y", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sky01_y", 0x1, 0x1)
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    SetChrFlags(0x19, 0x80)
    SetChrFlags(0x1A, 0x80)
    SetChrName("")

    #A0120
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#30Wこうして──楽しかった時間は\x01",
            "あっという間に過ぎていった。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_68(-870, 1030, -9460, 0)
    MoveCamera(310, 24, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(18500, 0)
    PlayBGM("ed7514", 0)
    SetCameraDistance(17500, 2000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_63(0x8, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    OP_63(0x18, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    OP_63(0x9, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(500)
    OP_63(0x14, 0x0, 2300, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    OP_63(0xF, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1500)
    SetCameraDistance(25000, 15000)
    OP_68(0, 1500, -12000, 15000)
    BeginChrThread(0x101, 3, 0, 30)
    Sleep(150)
    BeginChrThread(0x10, 3, 0, 30)
    Sleep(100)
    BeginChrThread(0x13, 3, 0, 30)
    Sleep(50)
    BeginChrThread(0xE, 3, 0, 30)
    Sleep(150)
    BeginChrThread(0x11, 3, 0, 30)
    Sleep(200)
    BeginChrThread(0x12, 3, 0, 30)
    Sleep(50)
    BeginChrThread(0xB, 3, 0, 30)
    Sleep(400)
    BeginChrThread(0xA, 3, 0, 30)
    Sleep(50)
    BeginChrThread(0xD, 3, 0, 30)
    Sleep(200)
    BeginChrThread(0xC, 3, 0, 30)
    Sleep(50)
    BeginChrThread(0x8, 3, 0, 30)
    Sleep(250)
    BeginChrThread(0x9, 3, 0, 30)
    Sleep(400)
    BeginChrThread(0xF, 3, 0, 31)
    Sleep(500)
    SetChrName("")

    #A0121
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#35A#40W夜の部が始まるテーマパークを\x01",
            "後ろ髪が引かれる思いで後にし……\x02\x03",

            "#35A#40Wロイドたちは一旦ホテルに戻って\x01",
            "晩餐会のある迎賓館に行く事にした。\x07\x00\x02",
        )
    )
    #Auto

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0x1388)
    WaitBGM()
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    Sleep(2000)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    Sleep(1000)
    SetScenarioFlags(0x22, 0)
    NewScene("t100B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_29_461A end

    def Function_30_4ACC(): pass

    label("Function_30_4ACC")

    OP_93(0xFE, 0xB4, 0x1F4)
    OP_9B(0x0, 0xFE, 0x0, 0x4E20, 0x7D0, 0x0)
    Return()

    # Function_30_4ACC end

    def Function_31_4AE3(): pass

    label("Function_31_4AE3")

    OP_9B(0x1, 0xFE, 0xB4, 0x3E8, 0x3E8, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x7D0, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Sleep(300)
    OP_93(0xFE, 0xB4, 0x1F4)
    OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    OP_9B(0x1, 0xFE, 0xB4, 0x3E8, 0x3E8, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    OP_9B(0x0, 0xFE, 0x0, 0x32C8, 0x7D0, 0x0)
    Return()

    # Function_31_4AE3 end

    def Function_32_4B55(): pass

    label("Function_32_4B55")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    OP_E2(0x3)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00150.itc", 0x1F)
    LoadChrToIndex("chr/ch00250.itc", 0x20)
    LoadChrToIndex("chr/ch00350.itc", 0x21)
    LoadEffect(0x0, "battle\\cr036301.eff")
    SetChrPos(0x101, 100, 0, -21000, 0)
    SetChrPos(0x102, 800, 0, -22100, 0)
    SetChrPos(0x103, -750, 0, -21900, 0)
    SetChrPos(0x104, -100, 0, -23000, 0)
    ClearChrFlags(0x2A, 0x80)
    OP_78(0x1, 0x2A)
    OP_49()
    SetChrPos(0x2A, 0, 0, -8500, 180)
    OP_D5(0x2A, 0x0, 0x2BF20, 0x0, 0x0)
    ClearMapObjFlags(0x1, 0x4)
    OP_74(0x1, 0x1E)
    OP_71(0x1, 0xA, 0x32, 0x0, 0x20)
    SetChrFlags(0x2A, 0x8000)
    OP_75(0x1, 0x1, 0x0)
    OP_A7(0x2A, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x2B, 0x80)
    OP_78(0x2, 0x2B)
    OP_49()
    SetChrPos(0x2B, -4000, 0, -7000, 165)
    OP_D5(0x2B, 0x0, 0x28488, 0x0, 0x0)
    ClearMapObjFlags(0x2, 0x4)
    OP_74(0x2, 0x1E)
    OP_71(0x2, 0xA, 0x32, 0x0, 0x20)
    SetChrFlags(0x2B, 0x8000)
    OP_75(0x2, 0x1, 0x0)
    OP_A7(0x2B, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x2C, 0x80)
    OP_78(0x3, 0x2C)
    OP_49()
    SetChrPos(0x2C, 4000, 0, -7000, 195)
    OP_D5(0x2C, 0x0, 0x2F9B8, 0x0, 0x0)
    ClearMapObjFlags(0x3, 0x4)
    OP_74(0x3, 0x1E)
    OP_71(0x3, 0xA, 0x32, 0x0, 0x20)
    SetChrFlags(0x2C, 0x8000)
    OP_75(0x3, 0x1, 0x0)
    OP_A7(0x2C, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_68(0, 1000, 0, 0)
    MoveCamera(0, 30, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(23500, 0)
    FadeToBright(1000, 0)
    SetCameraDistance(20000, 4000)
    OP_6F(0x79)
    OP_68(0, 1000, -12000, 4500)
    MoveCamera(0, 20, 0, 4500)
    SetCameraDistance(15000, 4500)

    def lambda_4D66():
        OP_9B(0x0, 0x101, 0x0, 0x1F40, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_4D66)
    Sleep(100)

    def lambda_4D7E():
        OP_9B(0x0, 0x102, 0x0, 0x1F40, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_4D7E)
    Sleep(100)

    def lambda_4D96():
        OP_9B(0x0, 0x103, 0x0, 0x1F40, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_4D96)
    Sleep(100)

    def lambda_4DAE():
        OP_9B(0x0, 0x104, 0x0, 0x1F40, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_4DAE)
    Sleep(100)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    OP_6F(0x79)
    OP_0D()

    #C0122
    ChrTalk(
        0x101,
        "#00010F#6Pプレロマ草……！\x02",
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0x103,
        "#00201F#6Pみっしぃの花壇が……！\x02",
    )

    CloseMessageWindow()
    StopBGM(0xBB8)
    Sound(842, 0, 100, 0)
    BeginChrThread(0x2A, 0, 0, 33)
    Sleep(1000)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Sleep(300)
    Fade(1000)
    OP_68(0, 2000, -8500, 0)
    MoveCamera(30, 45, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(22500, 0)
    SetCameraDistance(17500, 4000)
    MoveCamera(0, 20, 0, 4000)
    Sleep(500)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7454", 0)
    Sleep(490)
    Sound(919, 0, 100, 0)
    BlurSwitch(0x3E8, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    PlayEffect(0x0, 0xFF, 0x2A, 0x0, 0, 1500, 0, 0, 0, 0, 3000, 3000, 3000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)

    def lambda_4F43():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x2A, 2, lambda_4F43)

    def lambda_4F54():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x2B, 2, lambda_4F54)

    def lambda_4F65():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x2C, 2, lambda_4F65)
    OP_75(0x1, 0x2, 0x3E8)
    OP_75(0x2, 0x2, 0x3E8)
    OP_75(0x3, 0x2, 0x3E8)
    WaitChrThread(0x2A, 2)
    WaitChrThread(0x2B, 2)
    WaitChrThread(0x2C, 2)
    CancelBlur(1000)
    EndChrThread(0x2A, 0x0)
    OP_6F(0x79)
    OP_68(0, 1600, -10150, 3000)
    MoveCamera(0, 14, 0, 3000)
    OP_6E(650, 3000)
    SetCameraDistance(17500, 3000)
    Sleep(1000)

    def lambda_4FD3():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFC18, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4FD3)
    Sleep(50)

    def lambda_4FEB():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFC18, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4FEB)
    Sleep(50)

    def lambda_5003():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFC18, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5003)
    Sleep(50)

    def lambda_501B():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFC18, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_501B)
    WaitChrThread(0x104, 1)
    Fade(250)
    Sound(805, 0, 100, 0)
    Sound(531, 0, 100, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x104, 0x0)
    OP_0D()
    OP_6F(0x79)

    #C0124
    ChrTalk(
        0x102,
        "#00107F#12P#N沼地に現れた……！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0125
    ChrTalk(
        0x104,
        "#00310F#6P#Nハッ、ブチのめすぞ！\x02",
    )

    CloseMessageWindow()
    OP_74(0x1, 0x14)
    OP_74(0x2, 0x14)
    OP_74(0x3, 0x14)
    OP_71(0x1, 0x5B, 0x69, 0xFA, 0x8)
    OP_71(0x2, 0x8D, 0xA0, 0xFA, 0x8)
    OP_71(0x3, 0x8D, 0xA0, 0xFA, 0x8)
    OP_79(0x1)
    OP_79(0x2)
    OP_79(0x3)
    Sound(842, 0, 100, 0)
    BlurSwitch(0x64, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    SetCameraDistance(8000, 1000)
    OP_74(0x1, 0x1E)
    OP_74(0x2, 0x1E)
    OP_74(0x3, 0x1E)
    OP_71(0x1, 0x69, 0x73, 0x0, 0x8)
    OP_71(0x2, 0xA1, 0xAA, 0x0, 0x8)
    OP_71(0x3, 0xA1, 0xAA, 0x0, 0x8)
    Sleep(500)
    Battle("BattleInfo_72C", 0x0, 0x0, 0x0, 0x28, 0xFF)
    FadeToDark(0, 0, -1)
    Call(0, 34)
    Return()

    # Function_32_4B55 end

    def Function_33_5156(): pass

    label("Function_33_5156")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_517A")
    OP_82(0x64, 0x64, 0x1F40, 0x1F4)
    Sleep(500)
    Jump("Function_33_5156")

    label("loc_517A")

    Return()

    # Function_33_5156 end

    def Function_34_517B(): pass

    label("Function_34_517B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00150.itc", 0x1F)
    LoadChrToIndex("chr/ch00250.itc", 0x20)
    LoadChrToIndex("chr/ch00350.itc", 0x21)
    LoadEffect(0x0, "battle\\bs000000.eff")
    LoadEffect(0x1, "battle\\bs000001.eff")
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x104, 0x0)
    SetChrPos(0x101, 100, 0, -13000, 0)
    SetChrPos(0x102, 800, 0, -14100, 0)
    SetChrPos(0x103, -750, 0, -13900, 0)
    SetChrPos(0x104, -100, 0, -15000, 0)
    ClearChrFlags(0x2A, 0x80)
    OP_78(0x1, 0x2A)
    OP_49()
    SetChrPos(0x2A, 0, 0, -8500, 180)
    OP_D5(0x2A, 0x0, 0x2BF20, 0x0, 0x0)
    ClearMapObjFlags(0x1, 0x4)
    OP_74(0x1, 0x1E)
    OP_71(0x1, 0xA, 0x32, 0x0, 0x20)
    SetChrFlags(0x2A, 0x8000)
    OP_75(0x1, 0x2, 0x0)
    OP_A7(0x2A, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    ClearChrFlags(0x2B, 0x80)
    OP_78(0x2, 0x2B)
    OP_49()
    SetChrPos(0x2B, -4000, 0, -7000, 165)
    OP_D5(0x2B, 0x0, 0x28488, 0x0, 0x0)
    ClearMapObjFlags(0x2, 0x4)
    OP_74(0x2, 0x1E)
    OP_71(0x2, 0xA, 0x32, 0x0, 0x20)
    SetChrFlags(0x2B, 0x8000)
    OP_75(0x2, 0x2, 0x0)
    OP_A7(0x2B, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    ClearChrFlags(0x2C, 0x80)
    OP_78(0x3, 0x2C)
    OP_49()
    SetChrPos(0x2C, 4000, 0, -7000, 195)
    OP_D5(0x2C, 0x0, 0x2F9B8, 0x0, 0x0)
    ClearMapObjFlags(0x3, 0x4)
    OP_74(0x3, 0x1E)
    OP_71(0x3, 0xA, 0x32, 0x0, 0x20)
    SetChrFlags(0x2C, 0x8000)
    OP_75(0x3, 0x2, 0x0)
    OP_A7(0x2C, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_68(0, 2000, -8500, 0)
    MoveCamera(330, 45, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(22500, 0)
    FadeToBright(1000, 0)
    MoveCamera(0, 20, 0, 4000)
    SetCameraDistance(17500, 4000)
    BeginChrThread(0x2A, 0, 0, 33)
    BeginChrThread(0x2A, 3, 0, 35)
    BeginChrThread(0x2B, 3, 0, 36)
    BeginChrThread(0x2C, 3, 0, 37)
    Sound(919, 0, 80, 0)
    Sound(842, 0, 100, 0)
    BlurSwitch(0x3E8, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    PlayEffect(0x0, 0x0, 0x2A, 0x0, 0, 0, 0, 0, 0, 0, 2500, 2500, 2500, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    PlayEffect(0x1, 0x1, 0x2A, 0x0, 0, 0, 0, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)

    def lambda_5431():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x2A, 2, lambda_5431)

    def lambda_5442():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x2B, 2, lambda_5442)

    def lambda_5453():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x2C, 2, lambda_5453)
    OP_75(0x1, 0x1, 0x3E8)
    OP_75(0x2, 0x1, 0x3E8)
    OP_75(0x3, 0x1, 0x3E8)
    WaitChrThread(0x2A, 2)
    WaitChrThread(0x2B, 2)
    WaitChrThread(0x2C, 2)
    CancelBlur(1000)
    EndChrThread(0x2A, 0x3)
    EndChrThread(0x2B, 0x3)
    EndChrThread(0x2C, 0x3)
    EndChrThread(0x2A, 0x0)
    StopEffect(0x0, 0x2)
    StopEffect(0x1, 0x2)
    OP_6F(0x79)
    OP_0D()
    SetMapObjFlags(0x1, 0x4)
    SetMapObjFlags(0x2, 0x4)
    SetMapObjFlags(0x3, 0x4)
    SetChrFlags(0x2A, 0x80)
    SetChrFlags(0x2B, 0x80)
    SetChrFlags(0x2C, 0x80)
    Sleep(500)
    OP_68(0, 1000, -11400, 3000)
    OP_6F(0x79)
    Fade(250)
    Sound(805, 0, 100, 0)
    Sound(531, 0, 100, 0)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    OP_0D()
    Sleep(300)

    #C0126
    ChrTalk(
        0x101,
        (
            "#00006F#5P……前にこの場所で\x01",
            "《結社》のカンパネルラと\x01",
            "遭遇したけど……\x02\x03",

            "#00013F考えてみればキーアも\x01",
            "ちょうどこの先で……\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0x102,
        (
            "#00108F#12Pええ……\x01",
            "本当に何があるのかしら。\x02",
        )
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0x104,
        (
            "#00303F#6P考えても仕方ねえ……\x01",
            "行ってみるしかねぇだろ。\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0x103,
        "#00201F#6Pええ、行きましょう！\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_D7(0x20)
    OP_D7(0x21)
    SetChrPos(0x0, 0, 0, -10000, 0)
    OP_69(0xFF, 0x0)
    SetScenarioFlags(0x182, 7)
    ModifyEventFlags(0, 0, 0x80)
    EventEnd(0x5)
    Return()

    # Function_34_517B end

    def Function_35_564E(): pass

    label("Function_35_564E")

    OP_74(0x1, 0xF)

    label("loc_5652")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5680")
    OP_71(0x1, 0x3D, 0x50, 0x0, 0x8)
    OP_79(0x1)
    OP_71(0x1, 0x50, 0x3D, 0x0, 0x8)
    OP_79(0x1)
    Jump("loc_5652")

    label("loc_5680")

    Return()

    # Function_35_564E end

    def Function_36_5681(): pass

    label("Function_36_5681")

    OP_74(0x2, 0xF)

    label("loc_5685")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_56B3")
    OP_71(0x2, 0x3D, 0x50, 0x0, 0x8)
    OP_79(0x2)
    OP_71(0x2, 0x50, 0x3D, 0x0, 0x8)
    OP_79(0x2)
    Jump("loc_5685")

    label("loc_56B3")

    Return()

    # Function_36_5681 end

    def Function_37_56B4(): pass

    label("Function_37_56B4")

    OP_74(0x3, 0xF)

    label("loc_56B8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_56E6")
    OP_71(0x3, 0x3D, 0x50, 0x0, 0x8)
    OP_79(0x3)
    OP_71(0x3, 0x50, 0x3D, 0x0, 0x8)
    OP_79(0x3)
    Jump("loc_56B8")

    label("loc_56E6")

    Return()

    # Function_37_56B4 end

    def Function_38_56E7(): pass

    label("Function_38_56E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_5709")
    EventBegin(0x1)
    Call(0, 41)
    SetChrPos(0x0, 10670, 0, 4280, 225)
    EventEnd(0x4)
    Return()

    label("loc_5709")

    EventBegin(0x1)
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    #A0130
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1Kどこに移動しますか？\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "ホラーコースター\x01",      # 0
            "占いの館\x01",              # 1
            "やめる\x01",                # 2
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
        (0, "loc_57A4"),
        (1, "loc_57BD"),
        (2, "loc_57D6"),
        (SWITCH_DEFAULT, "loc_57DB"),
    )


    label("loc_57A4")

    FadeToDark(500, 0, -1)
    OP_0D()
    NewScene("t1350", 100, 0, 0)
    IdleLoop()
    Jump("loc_57DB")

    label("loc_57BD")

    FadeToDark(500, 0, -1)
    OP_0D()
    NewScene("t1380", 100, 0, 0)
    IdleLoop()
    Jump("loc_57DB")

    label("loc_57D6")

    Jump("loc_57DB")

    label("loc_57DB")

    SetChrPos(0x0, 10670, 0, 4280, 225)
    EventEnd(0x4)
    Return()

    # Function_38_56E7 end

    def Function_39_57EF(): pass

    label("Function_39_57EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_5811")
    EventBegin(0x1)
    Call(0, 41)
    SetChrPos(0x0, -11020, 0, 4080, 135)
    EventEnd(0x4)
    Return()

    label("loc_5811")

    EventBegin(0x1)
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    #A0131
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1Kどこに移動しますか？\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "観覧車\x01",      # 0
            "休憩所\x01",      # 1
            "やめる\x01",      # 2
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
        (0, "loc_58A0"),
        (1, "loc_58B9"),
        (2, "loc_58D2"),
        (SWITCH_DEFAULT, "loc_58D7"),
    )


    label("loc_58A0")

    FadeToDark(500, 0, -1)
    OP_0D()
    NewScene("t1330", 100, 0, 0)
    IdleLoop()
    Jump("loc_58D7")

    label("loc_58B9")

    FadeToDark(500, 0, -1)
    OP_0D()
    NewScene("t1370", 100, 0, 0)
    IdleLoop()
    Jump("loc_58D7")

    label("loc_58D2")

    Jump("loc_58D7")

    label("loc_58D7")

    SetChrPos(0x0, -11020, 0, 4080, 135)
    EventEnd(0x4)
    Return()

    # Function_39_57EF end

    def Function_40_58EB(): pass

    label("Function_40_58EB")

    EventBegin(0x1)

    #C0132
    ChrTalk(
        0x101,
        (
            "#00000Fおっと、こっちに行くと\x01",
            "テーマパークの外に出ちゃうな。\x02\x03",

            "今日はみんなと一緒に、\x01",
            "ＭＷＬを心行くまで満喫しよう。\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, 0, 3000, -55560, 0)
    EventEnd(0x4)
    Return()

    # Function_40_58EB end

    def Function_41_597A(): pass

    label("Function_41_597A")


    #C0133
    ChrTalk(
        0x101,
        (
            "#00000F今はこっちに用はない。\x01",
            "……行くのはやめておこう。\x02",
        )
    )

    CloseMessageWindow()
    Return()

    # Function_41_597A end

    def Function_42_59B9(): pass

    label("Function_42_59B9")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(4930, 2500, 2360, 0)
    MoveCamera(323, 23, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(14940, 0)
    SetChrPos(0x101, 2160, 0, 5860, 180)
    SetChrPos(0xEF, 3750, 0, 5560, 225)
    OP_4B(0x29, 0xFF)
    FadeToBright(1000, 0)
    OP_0D()

    #C0134
    ChrTalk(
        0x101,
        "#00005Fおっと、こんなところにいたのか。\x02",
    )

    CloseMessageWindow()
    OP_9C(0x29, 0x0, 0x0, 0x0, 0x1F4, 0xBB8)
    Sleep(500)
    TurnDirection(0x29, 0x101, 500)
    OP_63(0x29, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0135
    ChrTalk(
        0x29,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "きゃっ、見つかっちゃった☆\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(4410, 2500, 5160, 0)
    MoveCamera(333, 24, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(14940, 0)
    SetChrPos(0x29, 2800, 0, 5760, 0)
    SetChrPos(0x101, 2970, 0, 8380, 180)
    SetChrPos(0xEF, 4120, 0, 7980, 180)
    FadeToBright(1000, 0)
    OP_0D()

    #C0136
    ChrTalk(
        0x29,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "むむ……あたし、\x01",
            "おにーさんを侮ってたかも。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0x29,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "２度ならず３度までも\x01",
            "あたしを見つけ出すなんて、\x01",
            "ラッキーだけじゃ無理よね、うん。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0x101,
        (
            "#00012Fい、いや～……\x01",
            "それほどでもないような気が。\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0x29,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "よぉし、こうなったらあたしも\x01",
            "本気で隠れちゃう！\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0x29,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "みししっ、次はゼッタイに\x01",
            "見つからないんだから～！\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5C67():

        label("loc_5C67")

        TurnDirection(0xFE, 0x29, 500)
        Yield()
        Jump("loc_5C67")

    QueueWorkItem2(0x101, 1, lambda_5C67)

    def lambda_5C79():

        label("loc_5C79")

        TurnDirection(0xFE, 0x29, 500)
        Yield()
        Jump("loc_5C79")

    QueueWorkItem2(0xEF, 1, lambda_5C79)
    SetChrFlags(0x29, 0x1000)
    OP_95(0x29, -550, 0, 6760, 5000, 0x0)
    OP_95(0x29, -5830, 0, 4550, 5000, 0x0)

    def lambda_5CB8():
        OP_95(0xFE, -10560, 0, 4110, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_5CB8)
    Sleep(500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x101, 0x1)
    EndChrThread(0xEF, 0x1)
    OP_68(3360, 2500, 6680, 0)
    MoveCamera(297, 28, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(12170, 0)
    SetChrPos(0x101, 1880, 0, 6910, 270)
    SetChrPos(0xEF, 2170, 0, 8550, 270)
    FadeToBright(1000, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C7, 7)), scpexpr(EXPR_END)), "loc_5DB7")

    #C0141
    ChrTalk(
        0x102,
        (
            "#00100Fふふ、なんとか２回目も\x01",
            "見つけられたわね。\x02\x03",

            "#00103F次は本気を出すとか\x01",
            "言っていたみたいだけど……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6221")

    label("loc_5DB7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 0)), scpexpr(EXPR_END)), "loc_5E29")

    #C0142
    ChrTalk(
        0x103,
        (
            "#00200Fなんとか２回目も\x01",
            "見つけられましたね。\x02\x03",

            "#00203F次は本気を出すとか\x01",
            "言っていましたけど……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6221")

    label("loc_5E29")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 1)), scpexpr(EXPR_END)), "loc_5E99")

    #C0143
    ChrTalk(
        0x104,
        (
            "#00300Fなんとか２回目も\x01",
            "見つけられたな。\x02\x03",

            "#00303F次は本気を出すとか\x01",
            "言っていたみたいだが……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6221")

    label("loc_5E99")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 2)), scpexpr(EXPR_END)), "loc_5F0F")

    #C0144
    ChrTalk(
        0x109,
        (
            "#10100Fふふ、なんとか２回目も\x01",
            "見つけられましたね！\x02\x03",

            "#10103F次は本気を出すとか\x01",
            "言ってましたけど……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6221")

    label("loc_5F0F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 3)), scpexpr(EXPR_END)), "loc_5F83")

    #C0145
    ChrTalk(
        0x105,
        (
            "#10300Fフフ、なんとか２回目も\x01",
            "見つけられたね。\x02\x03",

            "#10303F次は本気を出すとか\x01",
            "言ってたみたいだけど。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6221")

    label("loc_5F83")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 4)), scpexpr(EXPR_END)), "loc_5FFD")

    #C0146
    ChrTalk(
        0x153,
        (
            "#01109Fよーし、これで２回目も\x01",
            "みつけられたねー！\x02\x03",

            "#01111F次はホンキを出すとか\x01",
            "言ってたみたいだけどー。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6221")

    label("loc_5FFD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 5)), scpexpr(EXPR_END)), "loc_6075")

    #C0147
    ChrTalk(
        0x156,
        (
            "#06400Fふふ、なんとか２回目も\x01",
            "見つけられましたね～。\x02\x03",

            "#06403F次は本気を出すとか\x01",
            "言ってましたけど……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6221")

    label("loc_6075")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 6)), scpexpr(EXPR_END)), "loc_60E7")

    #C0148
    ChrTalk(
        0x14C,
        (
            "#05900Fふふ、なんとか２回目も\x01",
            "見つけられたわね。\x02\x03",

            "#05904F次は本気を出すとか\x01",
            "言っていたけど……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6221")

    label("loc_60E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 7)), scpexpr(EXPR_END)), "loc_6151")

    #C0149
    ChrTalk(
        0x134,
        (
            "#01700Fフフ、２回目も\x01",
            "ざっとこんなもんね。\x02\x03",

            "#01705F次は本気を出すとか\x01",
            "言ってたけど……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6221")

    label("loc_6151")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C9, 0)), scpexpr(EXPR_END)), "loc_61C7")

    #C0150
    ChrTalk(
        0x135,
        (
            "#01802Fふふ、なんとか２回目も\x01",
            "見つけられましたね。\x02\x03",

            "#01805F次は本気を出すとか\x01",
            "言ってましたけど……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6221")

    label("loc_61C7")


    #C0151
    ChrTalk(
        0x166,
        (
            "#14000Fなんとか２回目も\x01",
            "見つけられたな。\x02\x03",

            "#14006F次は本気を出すとか\x01",
            "言ってたけど……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6221")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 7)), scpexpr(EXPR_END)), "loc_6284")

    #C0152
    ChrTalk(
        0x101,
        (
            "#00006Fちょっと不安だけど、\x01",
            "探してみましょう。\x02\x03",

            "#00000F次はどこに行ったかな……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_62D5")

    label("loc_6284")


    #C0153
    ChrTalk(
        0x101,
        (
            "#00006Fちょっと不安だけど、\x01",
            "探してみよう。\x02\x03",

            "#00000F次はどこに行ったかな……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_62D5")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_29(0x7F, 0x1, 0xC)
    SetScenarioFlags(0x1C9, 4)
    OP_65(0x0, 0x1)
    SetChrFlags(0x29, 0x80)
    SetChrPos(0x0, -20, 0, 8600, 180)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_42_59B9 end

    def Function_43_630A(): pass

    label("Function_43_630A")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(1060, 2500, -8580, 0)
    MoveCamera(319, 27, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(14940, 0)
    OP_93(0x14, 0xB4, 0x0)
    SetChrPos(0x101, -510, 0, -7920, 0)
    SetChrPos(0xEF, 530, 0, -7970, 0)
    OP_4B(0x14, 0xFF)
    FadeToBright(1000, 0)
    OP_0D()

    #C0154
    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "そっか～、まあ仕方ないネ。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "みーしぇの方には\x01",
            "ボクから伝えておくヨ～。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "キミたちはそのまま\x01",
            "遊びに戻っていいからネ～。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0x101,
        "#00006Fああ、悪いけどよろしく頼むよ。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xEF, 0x101, 500)
    Sleep(300)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C7, 7)), scpexpr(EXPR_END)), "loc_64BB")

    #C0158
    ChrTalk(
        0x102,
        (
            "#00106Fまあ、見つからないんだし\x01",
            "仕方ないわよね……\x02\x03",

            "#00100Fそれじゃあ、私はそろそろ\x01",
            "行かせてもらうわね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_699B")

    label("loc_64BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 0)), scpexpr(EXPR_END)), "loc_653D")

    #C0159
    ChrTalk(
        0x103,
        (
            "#00206Fどうしても見つかりませんし\x01",
            "仕方ありませんね……\x02\x03",

            "#00200Fそれでは、私はそろそろ\x01",
            "失礼させていただきます。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_699B")

    label("loc_653D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 1)), scpexpr(EXPR_END)), "loc_65B5")

    #C0160
    ChrTalk(
        0x104,
        (
            "#00306Fま、見つからないんだし\x01",
            "仕方ないわな。\x02\x03",

            "#00300Fそんじゃ、俺はそろそろ\x01",
            "行かせてもらうとすっか。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_699B")

    label("loc_65B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 2)), scpexpr(EXPR_END)), "loc_6633")

    #C0161
    ChrTalk(
        0x109,
        (
            "#10106Fまあ、見つからないんだし\x01",
            "仕方ないですよね……\x02\x03",

            "#10100Fでは、あたしはそろそろ\x01",
            "行かせていただきます。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_699B")

    label("loc_6633")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 3)), scpexpr(EXPR_END)), "loc_66A9")

    #C0162
    ChrTalk(
        0x105,
        (
            "#10306Fまあ、見つからないんだし\x01",
            "仕方ないよね。\x02\x03",

            "#10300Fそれじゃ、僕もこの辺で\x01",
            "失礼させてもらうよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_699B")

    label("loc_66A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 4)), scpexpr(EXPR_END)), "loc_6725")

    #C0163
    ChrTalk(
        0x153,
        (
            "#01106Fぶー、せっかくだから\x01",
            "見つけたかったなー。\x02\x03",

            "#01100Fまあいいやー。\x01",
            "キーア、別のとこで遊んでくるね！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_699B")

    label("loc_6725")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 5)), scpexpr(EXPR_END)), "loc_67A9")

    #C0164
    ChrTalk(
        0x156,
        (
            "#06406Fまあ、見つかりませんし\x01",
            "仕方ないですよね～……\x02\x03",

            "#06400Fそれでは、わたしはそろそろ\x01",
            "行かせていただきます～。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_699B")

    label("loc_67A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 6)), scpexpr(EXPR_END)), "loc_6825")

    #C0165
    ChrTalk(
        0x14C,
        (
            "#05906Fまあ、見つからないんだし\x01",
            "仕方ないわよね。\x02\x03",

            "#05900Fそれじゃあ、私はそろそろ\x01",
            "行かせてもらおうかな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_699B")

    label("loc_6825")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 7)), scpexpr(EXPR_END)), "loc_68AB")

    #C0166
    ChrTalk(
        0x134,
        (
            "#01706Fう～ん、見つけたかったけど……\x01",
            "まあ仕方ないわよね。\x02\x03",

            "#01702Fそれじゃ、あたしは\x01",
            "別の場所に遊びにいこっかな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_699B")

    label("loc_68AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C9, 0)), scpexpr(EXPR_END)), "loc_692D")

    #C0167
    ChrTalk(
        0x135,
        (
            "#01806Fまあ、見つかりませんし\x01",
            "仕方なさそうですね……\x02\x03",

            "#01802Fそれでは、私はそろそろ\x01",
            "失礼させていただきますね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_699B")

    label("loc_692D")


    #C0168
    ChrTalk(
        0x166,
        (
            "#14006Fま、見つからないんだし\x01",
            "仕方ないだろ。\x02\x03",

            "#14000Fそんじゃ、オレは別のところに\x01",
            "遊びに行くとするから。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_699B")

    TurnDirection(0x101, 0xEF, 500)
    Sleep(300)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 7)), scpexpr(EXPR_END)), "loc_69D0")

    #C0169
    ChrTalk(
        0x101,
        "#00000Fええ、また後で。\x02",
    )

    CloseMessageWindow()
    Jump("loc_69EF")

    label("loc_69D0")


    #C0170
    ChrTalk(
        0x101,
        "#00000Fああ、また後でな。\x02",
    )

    CloseMessageWindow()

    label("loc_69EF")

    FadeToDark(1000, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C7, 7)), scpexpr(EXPR_END)), "loc_6A0B")
    RemoveParty(0x1, 0xFF)
    Jump("loc_6AB1")

    label("loc_6A0B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 0)), scpexpr(EXPR_END)), "loc_6A1C")
    RemoveParty(0x2, 0xFF)
    Jump("loc_6AB1")

    label("loc_6A1C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 1)), scpexpr(EXPR_END)), "loc_6A2D")
    RemoveParty(0x3, 0xFF)
    Jump("loc_6AB1")

    label("loc_6A2D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 2)), scpexpr(EXPR_END)), "loc_6A3E")
    RemoveParty(0x8, 0xFF)
    Jump("loc_6AB1")

    label("loc_6A3E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 3)), scpexpr(EXPR_END)), "loc_6A4F")
    RemoveParty(0x4, 0xFF)
    Jump("loc_6AB1")

    label("loc_6A4F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 4)), scpexpr(EXPR_END)), "loc_6A65")
    RemoveParty(0x52, 0xFF)
    ClearChrFlags(0x8, 0x80)
    Jump("loc_6AB1")

    label("loc_6A65")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 5)), scpexpr(EXPR_END)), "loc_6A76")
    RemoveParty(0x55, 0xFF)
    Jump("loc_6AB1")

    label("loc_6A76")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 6)), scpexpr(EXPR_END)), "loc_6A8C")
    RemoveParty(0x4B, 0xFF)
    ClearChrFlags(0xA, 0x80)
    Jump("loc_6AB1")

    label("loc_6A8C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 7)), scpexpr(EXPR_END)), "loc_6A9D")
    RemoveParty(0x33, 0xFF)
    Jump("loc_6AB1")

    label("loc_6A9D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C9, 0)), scpexpr(EXPR_END)), "loc_6AAE")
    RemoveParty(0x34, 0xFF)
    Jump("loc_6AB1")

    label("loc_6AAE")

    RemoveParty(0x65, 0xFF)

    label("loc_6AB1")

    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0171
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "クエスト【みーしぇの挑戦】\x07\x00",
            "に失敗した……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_29(0x7F, 0x1, 0x10)
    OP_29(0x7F, 0x4, 0x40)
    OP_65(0x0, 0x1)
    SetChrFlags(0x29, 0x80)
    SetChrPos(0x0, -30, 0, -8310, 180)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_43_630A end

    def Function_44_6B25(): pass

    label("Function_44_6B25")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch45400.itc", 0x1E)
    LoadChrToIndex("chr/ch28100.itc", 0x1F)
    LoadChrToIndex("chr/ch20600.itc", 0x20)
    LoadChrToIndex("chr/ch24500.itc", 0x21)
    LoadChrToIndex("chr/ch33000.itc", 0x22)
    LoadChrToIndex("chr/ch23700.itc", 0x23)
    LoadChrToIndex("chr/ch24400.itc", 0x24)
    LoadChrToIndex("chr/ch20700.itc", 0x25)
    LoadChrToIndex("chr/ch22200.itc", 0x26)
    LoadChrToIndex("chr/ch22100.itc", 0x27)
    LoadChrToIndex("chr/ch32300.itc", 0x28)
    LoadChrToIndex("chr/ch32400.itc", 0x29)
    LoadEffect(0x0, "event\\eva02_00.eff")
    SoundLoad(820)
    SoundLoad(819)
    SoundLoad(501)
    SoundLoad(626)
    SetChrChipByIndex(0x101, 0xC)
    SetChrSubChip(0x101, 0x0)
    SetChrFlags(0x101, 0x1000)
    SetChrFlags(0x101, 0x20)
    SetChrChipByIndex(0x103, 0x1E)
    SetChrSubChip(0x103, 0x0)
    SetChrFlags(0x103, 0x1000)
    SetChrFlags(0x103, 0x20)
    SetChrChipByIndex(0x1E, 0x1F)
    SetChrFlags(0x1E, 0x8000)
    ClearChrFlags(0x1E, 0x80)
    SetChrChipByIndex(0x1F, 0x20)
    SetChrFlags(0x1F, 0x8000)
    ClearChrFlags(0x1F, 0x80)
    SetChrChipByIndex(0x20, 0x21)
    SetChrFlags(0x20, 0x8000)
    ClearChrFlags(0x20, 0x80)
    SetChrChipByIndex(0x21, 0x22)
    SetChrFlags(0x21, 0x8000)
    ClearChrFlags(0x21, 0x80)
    SetChrChipByIndex(0x22, 0x23)
    SetChrFlags(0x22, 0x8000)
    ClearChrFlags(0x22, 0x80)
    SetChrChipByIndex(0x23, 0x24)
    SetChrFlags(0x23, 0x8000)
    ClearChrFlags(0x23, 0x80)
    SetChrChipByIndex(0x24, 0x25)
    SetChrFlags(0x24, 0x8000)
    ClearChrFlags(0x24, 0x80)
    SetChrChipByIndex(0x25, 0x26)
    SetChrFlags(0x25, 0x8000)
    ClearChrFlags(0x25, 0x80)
    SetChrChipByIndex(0x26, 0x27)
    SetChrFlags(0x26, 0x8000)
    ClearChrFlags(0x26, 0x80)
    SetChrChipByIndex(0x27, 0x28)
    SetChrFlags(0x27, 0x8000)
    ClearChrFlags(0x27, 0x80)
    SetChrChipByIndex(0x28, 0x29)
    SetChrFlags(0x28, 0x8000)
    ClearChrFlags(0x28, 0x80)
    OP_68(170, 2200, -8360, 0)
    MoveCamera(358, 25, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16680, 0)
    SetChrPos(0x101, -700, 0, -7790, 180)
    SetChrPos(0x103, 1000, 0, -7790, 180)
    SetChrPos(0x1E, 3550, 0, -7790, 180)
    SetChrPos(0x1F, 990, 0, -11190, 0)
    SetChrPos(0x20, 50, 0, -12810, 0)
    SetChrPos(0x21, -2600, 0, -10830, 0)
    SetChrPos(0x22, 3350, 0, -9980, 0)
    SetChrPos(0x23, -1650, 0, -13660, 0)
    SetChrPos(0x24, -700, 0, -10910, 0)
    SetChrPos(0x25, 2320, 0, -11400, 0)
    SetChrPos(0x26, -4090, 0, -7750, 45)
    SetChrPos(0x27, 4430, 0, -8039, 315)
    SetChrPos(0x28, 1880, 0, -13990, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0x104, 0x80)
    SetChrFlags(0x109, 0x80)
    SetChrFlags(0x105, 0x80)
    OP_68(170, 1000, -8360, 3000)
    FadeToBright(1000, 0)
    OP_6F(0x1)
    OP_0D()

    #C0172
    ChrTalk(
        0x1E,
        "皆様、お待たせしました！\x02",
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0x1E,
        (
            "これより、みっしぃ＆みーしぇの\x01",
            "ダンスショウを開始します！\x02",
        )
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0x1F,
        "ワー、みっしぃ～！\x02",
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0x20,
        "かわいー！\x02",
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05206F（……ついにダンスショウか。\x01",
            "  うう、緊張するなあ……）\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0x103,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "#05526F（大丈夫です。\x01",
            "  このダンスも毎回、\x01",
            "  アドリブらしいですし。）\x02\x03",

            "#05520F（ダンスの指針さえ\x01",
            "  決まっていれば\x01",
            "  何とかなるかと。）\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05203F（指針か……）\x02\x03",

            "#05208F（そういえば、仕事前に\x01",
            "  ダンスのマニュアルを\x01",
            "  渡されてたっけ。）\x02\x03",

            "#05201F（あれをなんとか思い出せば……）\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0x1E,
        (
            "それでは……\x01",
            "皆様も一緒にお楽しみください！\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x1E, 0x10E, 0x1F4)
    Sleep(300)

    #C0180
    ChrTalk(
        0x1E,
        (
            "みっしぃ＆みーしぇ！\x01",
            "レーッツダンシーン！！\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0xBB8)
    WaitBGM()

    #C0181
    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05201F（来た……！）\x02\x03",

            "#05207F（……いくぞティオ！！\x01",
            "  “情熱的に、そしてファンシーに！”）\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0x103,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "#05521F（了解です……！）\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    PlayBGM("ed7589", 0)
    ClearChrFlags(0x101, 0x20)
    ClearChrFlags(0x103, 0x20)
    BeginChrThread(0x101, 1, 0, 50)
    BeginChrThread(0x103, 1, 0, 51)
    Sound(819, 0, 80, 0)
    Sound(820, 0, 50, 0)
    OP_63(0x1F, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x20, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x21, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x22, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x23, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x24, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x25, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x26, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x27, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x28, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(3000)
    ClearScenarioFlags(0x1, 1)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x103, 1)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x103, 0x20)
    SetScenarioFlags(0x1, 2)
    SetScenarioFlags(0x1, 1)
    BeginChrThread(0x101, 0, 0, 45)
    BeginChrThread(0x103, 0, 0, 45)
    BeginChrThread(0x101, 2, 0, 48)
    BeginChrThread(0x103, 2, 0, 49)
    WaitChrThread(0x103, 2)
    WaitChrThread(0x101, 2)
    ClearChrFlags(0x101, 0x20)
    ClearChrFlags(0x103, 0x20)
    ClearScenarioFlags(0x1, 2)
    OP_93(0x101, 0xB4, 0x0)
    OP_93(0x103, 0xB4, 0x0)
    Sleep(200)
    BeginChrThread(0x101, 1, 0, 51)
    BeginChrThread(0x103, 1, 0, 50)
    Sound(819, 0, 80, 0)
    Sound(820, 0, 66, 0)
    OP_63(0x1F, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x20, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x21, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x22, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x23, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x24, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x25, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x26, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x27, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x28, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(3000)
    ClearScenarioFlags(0x1, 1)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x103, 1)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x103, 0x20)
    SetScenarioFlags(0x1, 2)
    SetScenarioFlags(0x1, 1)
    BeginChrThread(0x101, 0, 0, 45)
    BeginChrThread(0x103, 0, 0, 45)
    BeginChrThread(0x101, 2, 0, 49)
    BeginChrThread(0x103, 2, 0, 48)
    Sound(819, 0, 80, 0)
    Sound(820, 0, 66, 0)
    OP_63(0x1F, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x20, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x21, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x22, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x23, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x24, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x25, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x26, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x27, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x28, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(3000)
    ClearScenarioFlags(0x1, 1)
    SetScenarioFlags(0x1, 1)

    #C0183
    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05203F（ここで、最後のキメゼリフ！）\x07\x00\x02",
        )
    )

    CloseMessageWindow()
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
            "ラブイズみっしぃ☆\x01",        # 0
            "ハッピーみっしぃ☆\x01",        # 1
            "エンジョイみっしぃ☆\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_767C")
    OP_2C(0x86, 0x1)
    SetScenarioFlags(0x177, 0)

    #C0184
    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#4Sエンジョーイ、みっしぃ☆\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    ClearScenarioFlags(0x1, 2)
    SetScenarioFlags(0x1, 2)
    BeginChrThread(0x101, 0, 0, 47)
    BeginChrThread(0x103, 0, 0, 47)
    BeginChrThread(0x101, 2, 0, 52)
    BeginChrThread(0x103, 2, 0, 52)
    WaitChrThread(0x101, 2)
    WaitChrThread(0x103, 2)
    ClearScenarioFlags(0x1, 1)
    ClearScenarioFlags(0x1, 2)
    SetMessageWindowPos(-1, 140, -1, -1)
    SetChrName("観客たち")

    #A0185
    AnonymousTalk(
        0xFF,
        "#4Sエンジョーーーイ！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrName("観客たち")

    #A0186
    AnonymousTalk(
        0xFF,
        "#4Sみっしーーーーぃ☆\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sound(819, 0, 100, 0)
    Sound(820, 0, 66, 0)
    OP_63(0x1F, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x20, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x21, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x22, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x23, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x24, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x25, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x26, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x27, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x28, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)

    #C0187
    ChrTalk(
        0x103,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "#05522F（なんという連帯感……\x01",
            "  ロイドさん、さすがです！）\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7B90")

    label("loc_767C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7852")

    #C0188
    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#4Sラブイーズ、みっしぃ☆\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    ClearScenarioFlags(0x1, 2)
    SetScenarioFlags(0x1, 2)
    BeginChrThread(0x101, 0, 0, 47)
    BeginChrThread(0x103, 0, 0, 47)
    BeginChrThread(0x101, 2, 0, 52)
    BeginChrThread(0x103, 2, 0, 52)
    WaitChrThread(0x101, 2)
    WaitChrThread(0x103, 2)
    ClearScenarioFlags(0x1, 1)
    ClearScenarioFlags(0x1, 2)
    Sleep(2000)
    OP_63(0x1F, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x20, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x21, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x22, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x23, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x24, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x25, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x26, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x27, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x28, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)
    SetMessageWindowPos(-1, 140, -1, -1)
    SetChrName("観客たち")

    #A0189
    AnonymousTalk(
        0xFF,
        "#4Sラ、ラブイーーズ！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrName("観客たち")

    #A0190
    AnonymousTalk(
        0xFF,
        "#4Sみっしーーーーぃ☆\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_7A14")

    label("loc_7852")


    #C0191
    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#4Sハッピーィ、みっしぃ☆\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    ClearScenarioFlags(0x1, 2)
    SetScenarioFlags(0x1, 2)
    BeginChrThread(0x101, 0, 0, 47)
    BeginChrThread(0x103, 0, 0, 47)
    BeginChrThread(0x101, 2, 0, 52)
    BeginChrThread(0x103, 2, 0, 52)
    WaitChrThread(0x101, 2)
    WaitChrThread(0x103, 2)
    ClearScenarioFlags(0x1, 1)
    ClearScenarioFlags(0x1, 2)
    Sleep(2000)
    OP_63(0x1F, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x20, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x21, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x22, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x23, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x24, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x25, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x26, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x27, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x28, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)
    SetMessageWindowPos(-1, 140, -1, -1)
    SetChrName("観客たち")

    #A0192
    AnonymousTalk(
        0xFF,
        "#4Sハ、ハッピーーイ！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrName("観客たち")

    #A0193
    AnonymousTalk(
        0xFF,
        "#4Sみっしーーーーぃ☆\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_7A14")

    Sound(819, 0, 66, 0)
    Sound(820, 0, 50, 0)
    OP_63(0x1F, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x20, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x21, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x22, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x23, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x24, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x25, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x26, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x27, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x28, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)

    #C0194
    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05206F（……し、しまった……\x01",
            "  キメゼリフを間違えたかな？）\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0x103,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "#05526F（……ふう、最後の最後で。）\x02\x03",

            "#05531F（これは、お仕置きが必要ですね。）\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7B90")

    StopSound(821, 3000, 50)
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7C82")
    SetChrName("")

    #A0196
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ダンスショウは、ロイドたちの\x01",
            "熱の入ったダンスによって\x01",
            "大盛況のうちに終了した。\x02\x03",

            "無事踊りきったロイドは、\x01",
            "不思議な余韻に包まれつつ……\x02\x03",

            "ティオとともに\x01",
            "休憩所へと向かったのだった。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_29(0x86, 0x1, 0x7)
    Jump("loc_7D96")

    label("loc_7C82")

    SetChrName("")

    #A0197
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ダンスショウは、ロイドたちの\x01",
            "熱の入ったダンスによって\x01",
            "大盛況のうちに終了した。\x02\x03",

            "踊りきった後、ロイドは\x01",
            "ティオとともに休憩所へと\x01",
            "向かったが……\x02\x03",

            "その道中、キメゼリフを間違えた\x01",
            "お仕置きを受けるのだった。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(500)
    Sound(501, 0, 80, 0)
    Sound(815, 0, 40, 0)
    Sleep(800)
    #Sound(3319, 255, 100, 0)    #voice#Lloyd

    #C0198
    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05211F#Nあだっ！？\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_29(0x86, 0x1, 0x8)

    label("loc_7D96")

    SetScenarioFlags(0x22, 0)
    NewScene("t1370", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_44_6B25 end

    def Function_45_7DA3(): pass

    label("Function_45_7DA3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_7DBF")
    OP_52(0xFE, 0x4, (scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Sleep(100)
    Jump("Function_45_7DA3")

    label("loc_7DBF")

    Return()

    # Function_45_7DA3 end

    def Function_46_7DC0(): pass

    label("Function_46_7DC0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_7DDC")
    OP_52(0xFE, 0x4, (scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Sleep(50)
    Jump("Function_46_7DC0")

    label("loc_7DDC")

    Return()

    # Function_46_7DC0 end

    def Function_47_7DDD(): pass

    label("Function_47_7DDD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_7DF9")
    OP_52(0xFE, 0x4, (scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Sleep(33)
    Jump("Function_47_7DDD")

    label("loc_7DF9")

    Return()

    # Function_47_7DDD end

    def Function_48_7DFA(): pass

    label("Function_48_7DFA")

    OP_96(0xFE, 0xFFFFF768, 0x0, 0xFFFFE192, 0x7D0, 0x0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_9C(0xFE, 0x0, 0x0, 0x0, 0x3E8, 0xBB8)
    OP_96(0xFE, 0xFFFFFD44, 0x0, 0xFFFFE192, 0x7D0, 0x0)
    OP_96(0xFE, 0x96, 0x0, 0xFFFFDD14, 0x7D0, 0x0)
    OP_96(0xFE, 0x3E8, 0x0, 0xFFFFE192, 0x7D0, 0x0)
    Return()

    # Function_48_7DFA end

    def Function_49_7E6D(): pass

    label("Function_49_7E6D")

    OP_96(0xFE, 0x9C4, 0x0, 0xFFFFE192, 0x7D0, 0x0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_9C(0xFE, 0x0, 0x0, 0x0, 0x3E8, 0xBB8)
    OP_96(0xFE, 0x3E8, 0x0, 0xFFFFE192, 0x7D0, 0x0)
    OP_96(0xFE, 0x96, 0x0, 0xFFFFE4D0, 0x7D0, 0x0)
    OP_96(0xFE, 0xFFFFFD44, 0x0, 0xFFFFE192, 0x7D0, 0x0)
    Return()

    # Function_49_7E6D end

    def Function_50_7EE0(): pass

    label("Function_50_7EE0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_7FF3")
    OP_98(0xFE, 0x0, 0x0, 0xFFFFFE0C, 0x7D0, 0x0)
    Sleep(500)
    OP_98(0xFE, 0x0, 0x0, 0x1F4, 0x7D0, 0x0)
    Sleep(500)
    OP_98(0xFE, 0x0, 0x0, 0x1F4, 0x7D0, 0x0)
    Sleep(500)
    OP_98(0xFE, 0x0, 0x0, 0xFFFFFE0C, 0x7D0, 0x0)
    Sleep(100)
    SetScenarioFlags(0x1, 2)
    BeginChrThread(0xFE, 0, 0, 46)
    OP_9C(0xFE, 0x0, 0x0, 0x0, 0x1F4, 0xBB8)
    ClearScenarioFlags(0x1, 2)
    OP_93(0xFE, 0x10E, 0x0)
    Sleep(100)
    OP_97(0xFE, 0xFFFFFE0C, 0x0, 0x0, 0x7D0, 0x0)
    Sleep(500)
    OP_97(0xFE, 0x1F4, 0x0, 0x0, 0x7D0, 0x0)
    Sleep(500)
    OP_97(0xFE, 0x0, 0x0, 0xFFFFFE0C, 0x7D0, 0x0)
    Sleep(500)
    OP_98(0xFE, 0x0, 0x0, 0x1F4, 0x7D0, 0x0)
    SetScenarioFlags(0x1, 2)
    BeginChrThread(0xFE, 0, 0, 46)
    OP_9C(0xFE, 0x0, 0x0, 0x0, 0x1F4, 0xBB8)
    ClearScenarioFlags(0x1, 2)
    Jump("Function_50_7EE0")

    label("loc_7FF3")

    Return()

    # Function_50_7EE0 end

    def Function_51_7FF4(): pass

    label("Function_51_7FF4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_8107")
    OP_98(0xFE, 0x0, 0x0, 0xFFFFFE0C, 0x7D0, 0x0)
    Sleep(500)
    OP_98(0xFE, 0x0, 0x0, 0x1F4, 0x7D0, 0x0)
    Sleep(500)
    OP_98(0xFE, 0x0, 0x0, 0x1F4, 0x7D0, 0x0)
    Sleep(500)
    OP_98(0xFE, 0x0, 0x0, 0xFFFFFE0C, 0x7D0, 0x0)
    Sleep(100)
    SetScenarioFlags(0x1, 2)
    BeginChrThread(0xFE, 0, 0, 46)
    OP_9C(0xFE, 0x0, 0x0, 0x0, 0x1F4, 0xBB8)
    ClearScenarioFlags(0x1, 2)
    OP_93(0xFE, 0x5A, 0x0)
    Sleep(100)
    OP_97(0xFE, 0x1F4, 0x0, 0x0, 0x7D0, 0x0)
    Sleep(500)
    OP_97(0xFE, 0xFFFFFE0C, 0x0, 0x0, 0x7D0, 0x0)
    Sleep(500)
    OP_97(0xFE, 0x0, 0x0, 0xFFFFFE0C, 0x7D0, 0x0)
    Sleep(500)
    OP_98(0xFE, 0x0, 0x0, 0x1F4, 0x7D0, 0x0)
    SetScenarioFlags(0x1, 2)
    BeginChrThread(0xFE, 0, 0, 46)
    OP_9C(0xFE, 0x0, 0x0, 0x0, 0x1F4, 0xBB8)
    ClearScenarioFlags(0x1, 2)
    Jump("Function_51_7FF4")

    label("loc_8107")

    Return()

    # Function_51_7FF4 end

    def Function_52_8108(): pass

    label("Function_52_8108")

    OP_9C(0xFE, 0x0, 0x0, 0x0, 0x7D0, 0xBB8)
    OP_93(0xFE, 0xB4, 0x0)
    Return()

    # Function_52_8108 end

    def Function_53_8127(): pass

    label("Function_53_8127")

    Sleep(1000)

    label("loc_812A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_814C")
    Sound(918, 0, 50, 0)
    Sleep(2200)
    Sound(918, 0, 40, 0)
    Sleep(5000)
    Jump("loc_812A")

    label("loc_814C")

    Return()

    # Function_53_8127 end

    SaveToFile()

Try(main)
