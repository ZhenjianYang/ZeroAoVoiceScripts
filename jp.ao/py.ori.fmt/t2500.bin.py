from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t2500.bin",                # FileName
        "t2500",                    # MapName
        "t2500",                    # Location
        0x005A,                     # MapIndex
        "ed7126",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x03,                       # PlaceNameNumber
        0x1B,                       # PreInitFunctionIndex
        b'\x00\xff\x01',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, -25330, 0, -250, 0, 0, 1, 90, 0, 2, 0, 3],
    )

    BuildStringList((
        "t2500",                  # 0
        "ノウェ隊員",             # 1
        "ダイモン隊員",           # 2
        "ギャリソン隊員",         # 3
        "バレル隊員",             # 4
        "チルル",                 # 5
        "ユーリ",                 # 6
        "サイクス",               # 7
        "レジー",                 # 8
        "バス",                   # 9
        "列車",                   # 10
        "特務支援車",             # 11
        "運搬車",                 # 12
        "ダグラス副司令",         # 13
        "オリバー隊員",           # 14
        "ジャック隊員",           # 15
        "アレクセイ隊員",         # 16
        "ミンネス",               # 17
        "bt2500",                 # 18
        "bt2500",                 # 19
        "bt2500",                 # 20
        "東クロスベル街道",       # 21
    ))

    ATBonus("ATBonus_3B0", 100, 5, 0, 5, 0, 5, 0, 2, 5, 0, 0, 0, 2, 0, 0, 0)

    MonsterBattlePostion("MonsterBattlePostion_470", 8, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_474", 6, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_478", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_47C", 3, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_480", 13, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_484", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_488", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_48C", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_450", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_454", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_458", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_45C", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_460", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_464", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_468", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_46C", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_490", 8, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_494", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_498", 5, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_49C", 11, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_4A0", 3, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_4A4", 13, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_4A8", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_4AC", 0, 0, 180)

    # monster count: 0

    # event battle count: 3

    BattleInfo(
        "BattleInfo_4B0", 0x0002, 255, 6, 45, 3, 3, 30, 0, "bt2500", 0x00000000, 100, 0, 0, 0,
        (
            ("ms31300.dat", "ms31300.dat", "ms31300.dat", "ms31200.dat", "ms31200.dat", 0, 0, 0, "MonsterBattlePostion_470", "MonsterBattlePostion_450", "ed7451", "ed7453", "ATBonus_3B0"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_4F4", 0x0002, 255, 6, 45, 3, 3, 30, 0, "bt2500", 0x00000000, 100, 0, 0, 0,
        (
            ("ms31300.dat", "ms31300.dat", "ms31300.dat", "ms31200.dat", "ms31200.dat", 0, 0, 0, "MonsterBattlePostion_470", "MonsterBattlePostion_450", "ed7451", "ed7453", "ATBonus_3B0"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_538", 0x0022, 255, 6, 45, 3, 3, 30, 0, "bt2500", 0x00000000, 100, 0, 0, 0,
        (
            ("ms44900.dat", "ms31300.dat", "ms31300.dat", "ms31300.dat", "ms31200.dat", "ms31200.dat", 0, 0, "MonsterBattlePostion_490", "MonsterBattlePostion_450", "ed7452", "ed7453", "ATBonus_3B0"),
            (),
            (),
            (),
        )
    )

    AddCharChip((
        "chr/ch31200.itc",                   # 00
        "chr/ch31300.itc",                   # 01
        "chr/ch20500.itc",                   # 02
        "chr/ch44100.itc",                   # 03
        "chr/ch47500.itc",                   # 04
        "chr/ch23600.itc",                   # 05
        "chr/ch41400.itc",                   # 06
        "chr/ch41500.itc",                   # 07
    ))

    DeclNpc(-22430,  0,       4730,    270,  261,  0x0, 0,   0,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(-22239,  0,       -5489,   270,  261,  0x0, 0,   1,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(13659,   10000,   2849,    90,   261,  0x0, 0,   0,   0,   0,   0,   0,   15,  255,  0)
    DeclNpc(13859,   10000,   -2640,   90,   261,  0x0, 0,   1,   0,   0,   0,   0,   16,  255,  0)
    DeclNpc(-35549,  0,       -3299,   270,  389,  0x0, 0,   2,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(-38659,  0,       -3250,   90,   389,  0x0, 0,   3,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(-37299,  0,       -1419,   135,  389,  0x0, 0,   4,   0,   0,   0,   0,   13,  255,  0)
    DeclNpc(-38250,  0,       -4769,   45,   389,  0x0, 0,   5,   0,   0,   0,   0,   14,  255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclActor(-31150,  0,       27650,   1200,    -31150,  1000,    27650,   0x007C, 0,  18, 0x0000)
    DeclActor(-8000,   1500,    -37500,  1200,    -8000,   2500,    -37500,  0x007C, 0,  4,  0x0000)
    DeclActor(-38370,  0,       3120,    1200,    -38370,  2000,    3120,    0x007C, 0,  17, 0x0000)
    DeclActor(-37890,  0,       4410,    1200,    -37890,  2000,    4410,    0x007C, 0,  17, 0x0000)
    DeclActor(-18980,  200,     -11720,  1200,    -18980,  1700,    -11720,  0x007C, 0,  36, 0x0000)

    PlaceName(-71.0, 0.0, -8.0, 0x0000, 0x0000, "東クロスベル街道")
    PlaceName(-5.25, 0.0, -2.5, 0x0000, 0x0052, "")
    PlaceName(-30.950000762939453, 0.0, 28.100000381469727, 0x0000, 0x0055, "")

    ChipFrameInfo(1552, 0)                                       # 0

    ScpFunction((
        "Function_0_610",          # 00, 0
        "Function_1_6C8",          # 01, 1
        "Function_2_721",          # 02, 2
        "Function_3_D7D",          # 03, 3
        "Function_4_106D",         # 04, 4
        "Function_5_11BE",         # 05, 5
        "Function_6_12AE",         # 06, 6
        "Function_7_13DB",         # 07, 7
        "Function_8_142C",         # 08, 8
        "Function_9_14C0",         # 09, 9
        "Function_10_21AE",        # 0A, 10
        "Function_11_2DA5",        # 0B, 11
        "Function_12_2EC6",        # 0C, 12
        "Function_13_2FF1",        # 0D, 13
        "Function_14_3101",        # 0E, 14
        "Function_15_3210",        # 0F, 15
        "Function_16_3C98",        # 10, 16
        "Function_17_4818",        # 11, 17
        "Function_18_4B5B",        # 12, 18
        "Function_19_4BA7",        # 13, 19
        "Function_20_4D40",        # 14, 20
        "Function_21_598F",        # 15, 21
        "Function_22_599F",        # 16, 22
        "Function_23_59B2",        # 17, 23
        "Function_24_59C5",        # 18, 24
        "Function_25_59D8",        # 19, 25
        "Function_26_59EB",        # 1A, 26
        "Function_27_6204",        # 1B, 27
        "Function_28_638B",        # 1C, 28
        "Function_29_6B3F",        # 1D, 29
        "Function_30_726C",        # 1E, 30
        "Function_31_78B5",        # 1F, 31
        "Function_32_7EFA",        # 20, 32
        "Function_33_82A0",        # 21, 33
        "Function_34_85EE",        # 22, 34
        "Function_35_9627",        # 23, 35
        "Function_36_968C",        # 24, 36
    ))


    def Function_0_610(): pass

    label("Function_0_610")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_650"),
        (1, "loc_65C"),
        (2, "loc_668"),
        (3, "loc_674"),
        (4, "loc_680"),
        (5, "loc_68C"),
        (6, "loc_698"),
        (SWITCH_DEFAULT, "loc_6A4"),
    )


    label("loc_650")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_6B0")

    label("loc_65C")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_6B0")

    label("loc_668")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_6B0")

    label("loc_674")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_6B0")

    label("loc_680")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_6B0")

    label("loc_68C")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_6B0")

    label("loc_698")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_6B0")

    label("loc_6A4")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_6B0")

    label("loc_6B0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6C7")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_6B0")

    label("loc_6C7")

    Return()

    # Function_0_610 end

    def Function_1_6C8(): pass

    label("Function_1_6C8")

    SetMapObjFlags(0x2, 0x2000000)
    SetMapObjFlags(0x3, 0x2000000)
    SetMapObjFlags(0x9, 0x2000000)
    SetMapObjFlags(0xA, 0x2000000)
    SetMapObjFlags(0x8, 0x2000000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_705")
    ClearMapObjFlags(0x9, 0x2000000)
    ClearMapObjFlags(0xA, 0x2000000)
    Jump("loc_711")

    label("loc_705")

    ClearMapObjFlags(0x2, 0x2000000)
    ClearMapObjFlags(0x3, 0x2000000)

    label("loc_711")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_720")
    ClearMapObjFlags(0x8, 0x2000000)

    label("loc_720")

    Return()

    # Function_1_6C8 end

    def Function_2_721(): pass

    label("Function_2_721")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_74E")
    SetChrChipByIndex(0x8, 0x6)
    SetChrChipByIndex(0x9, 0x7)
    SetChrChipByIndex(0xA, 0x6)
    SetChrChipByIndex(0xB, 0x7)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)

    label("loc_74E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BF2")
    ClearScenarioFlags(0x38, 0)
    ClearScenarioFlags(0x38, 1)
    ClearScenarioFlags(0x38, 2)
    ClearScenarioFlags(0x38, 3)
    ClearScenarioFlags(0x38, 4)
    ClearScenarioFlags(0x38, 5)
    ClearScenarioFlags(0x38, 6)
    ClearScenarioFlags(0x38, 7)
    ClearScenarioFlags(0x39, 0)
    ClearScenarioFlags(0x39, 1)
    ClearScenarioFlags(0x39, 2)
    ClearScenarioFlags(0x39, 3)
    ClearScenarioFlags(0x39, 4)
    ClearScenarioFlags(0x39, 5)
    ClearScenarioFlags(0x39, 6)
    ClearScenarioFlags(0x39, 7)
    ClearScenarioFlags(0x3A, 0)
    ClearScenarioFlags(0x3A, 1)
    ClearScenarioFlags(0x3A, 2)
    ClearScenarioFlags(0x3A, 3)
    ClearScenarioFlags(0x3A, 4)
    ClearScenarioFlags(0x3A, 5)
    ClearScenarioFlags(0x3A, 6)
    ClearScenarioFlags(0x3A, 7)
    ClearScenarioFlags(0x3B, 0)
    ClearScenarioFlags(0x3B, 1)
    ClearScenarioFlags(0x3B, 2)
    ClearScenarioFlags(0x3B, 3)
    ClearScenarioFlags(0x3B, 4)
    ClearScenarioFlags(0x3B, 5)
    ClearScenarioFlags(0x3B, 6)
    ClearScenarioFlags(0x3B, 7)
    ClearScenarioFlags(0x3D, 5)
    ClearScenarioFlags(0x3D, 6)
    ClearScenarioFlags(0x3D, 7)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7DB")
    SetScenarioFlags(0x38, 0)

    label("loc_7DB")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7F1")
    SetScenarioFlags(0x38, 1)

    label("loc_7F1")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_807")
    SetScenarioFlags(0x38, 2)

    label("loc_807")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_81D")
    SetScenarioFlags(0x38, 3)

    label("loc_81D")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_833")
    SetScenarioFlags(0x38, 4)

    label("loc_833")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_849")
    SetScenarioFlags(0x38, 5)

    label("loc_849")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_85F")
    SetScenarioFlags(0x38, 6)

    label("loc_85F")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_875")
    SetScenarioFlags(0x38, 7)

    label("loc_875")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_88B")
    SetScenarioFlags(0x39, 0)

    label("loc_88B")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8A1")
    SetScenarioFlags(0x39, 1)

    label("loc_8A1")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8B7")
    SetScenarioFlags(0x39, 2)

    label("loc_8B7")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8CD")
    SetScenarioFlags(0x39, 3)

    label("loc_8CD")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8E3")
    SetScenarioFlags(0x39, 4)

    label("loc_8E3")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8F9")
    SetScenarioFlags(0x39, 5)

    label("loc_8F9")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_90F")
    SetScenarioFlags(0x39, 6)

    label("loc_90F")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_925")
    SetScenarioFlags(0x39, 7)

    label("loc_925")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_93B")
    SetScenarioFlags(0x3A, 0)

    label("loc_93B")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_951")
    SetScenarioFlags(0x3A, 1)

    label("loc_951")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_967")
    SetScenarioFlags(0x3A, 2)

    label("loc_967")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_97D")
    SetScenarioFlags(0x3A, 3)

    label("loc_97D")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_993")
    SetScenarioFlags(0x3A, 4)

    label("loc_993")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9A9")
    SetScenarioFlags(0x3A, 5)

    label("loc_9A9")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9BF")
    SetScenarioFlags(0x3A, 6)

    label("loc_9BF")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9D5")
    SetScenarioFlags(0x3A, 7)

    label("loc_9D5")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9EB")
    SetScenarioFlags(0x3B, 0)

    label("loc_9EB")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A01")
    SetScenarioFlags(0x3B, 1)

    label("loc_A01")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A17")
    SetScenarioFlags(0x3B, 2)

    label("loc_A17")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A2D")
    SetScenarioFlags(0x3B, 3)

    label("loc_A2D")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A43")
    SetScenarioFlags(0x3B, 4)

    label("loc_A43")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A59")
    SetScenarioFlags(0x3B, 5)

    label("loc_A59")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A6F")
    SetScenarioFlags(0x3B, 6)

    label("loc_A6F")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A85")
    SetScenarioFlags(0x3B, 7)

    label("loc_A85")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A9B")
    SetScenarioFlags(0x3D, 5)

    label("loc_A9B")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AB1")
    SetScenarioFlags(0x3D, 6)

    label("loc_AB1")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AC7")
    SetScenarioFlags(0x3D, 7)

    label("loc_AC7")

    ClearScenarioFlags(0x3C, 0)
    ClearScenarioFlags(0x3C, 1)
    ClearScenarioFlags(0x3C, 2)
    ClearScenarioFlags(0x3C, 3)
    ClearScenarioFlags(0x3C, 4)
    ClearScenarioFlags(0x3C, 5)
    ClearScenarioFlags(0x3C, 6)
    ClearScenarioFlags(0x3C, 7)
    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B02")
    SetScenarioFlags(0x3C, 0)
    Jump("loc_BF2")

    label("loc_B02")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B25")
    SetScenarioFlags(0x3C, 1)
    Jump("loc_BF2")

    label("loc_B25")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B48")
    SetScenarioFlags(0x3C, 2)
    Jump("loc_BF2")

    label("loc_B48")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B6B")
    SetScenarioFlags(0x3C, 3)
    Jump("loc_BF2")

    label("loc_B6B")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B8E")
    SetScenarioFlags(0x3C, 4)
    Jump("loc_BF2")

    label("loc_B8E")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BB1")
    SetScenarioFlags(0x3C, 5)
    Jump("loc_BF2")

    label("loc_BB1")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BD4")
    SetScenarioFlags(0x3C, 6)
    Jump("loc_BF2")

    label("loc_BD4")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BF2")
    SetScenarioFlags(0x3C, 7)

    label("loc_BF2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x35, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C08")
    OP_50(0x1E, (scpexpr(EXPR_PUSH_LONG, 0x1B), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_C08")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C3A")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C3A")
    SetChrPos(0x0, -38590, 0, 1950, 180)
    OP_31(0x1)
    OP_69(0xFF, 0x0)
    Event(0, 8)

    label("loc_C3A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_END)), "loc_C6D")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C6D")
    SetChrPos(0x0, -37890, 0, 4410, 180)
    OP_31(0x1)
    OP_69(0xFF, 0x0)
    ClearMapFlags(0x8000000)

    label("loc_C6D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3E, 0)), scpexpr(EXPR_END)), "loc_CBB")
    ClearScenarioFlags(0x3E, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C9D")
    Event(0, 33)
    Jump("loc_CBB")

    label("loc_C9D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CB, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CB8")
    Event(0, 26)
    Jump("loc_CBB")

    label("loc_CB8")

    Event(0, 7)

    label("loc_CBB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_CCF")
    ClearScenarioFlags(0x22, 0)
    Event(0, 19)
    Jump("loc_CDE")

    label("loc_CCF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_CDE")
    ClearScenarioFlags(0x22, 1)
    Event(0, 27)

    label("loc_CDE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 1)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6F, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D02")
    Event(0, 20)
    Jump("loc_D7C")

    label("loc_D02")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D4A")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D34")
    Event(0, 34)
    Jump("loc_D45")

    label("loc_D34")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D45")
    Event(0, 32)

    label("loc_D45")

    Jump("loc_D7C")

    label("loc_D4A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CB, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D7C")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_D7C")
    SetMapFlags(0x10000000)
    Event(0, 26)

    label("loc_D7C")

    Return()

    # Function_2_721 end

    def Function_3_D7D(): pass

    label("Function_3_D7D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D99")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x97), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_DAB")

    label("loc_D99")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 3)), scpexpr(EXPR_END)), "loc_DAB")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x236), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_DAB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_E2F")
    LoadEffect(0x9, "map/mprain00.eff")
    PlayEffect(0x9, 0x7, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 1000)
    OP_7D(0xB4, 0xB4, 0xB4, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0xD, 0xE6, 0x0)
    Sound(128, 1, 100, 0)

    label("loc_E2F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_END)), "loc_E46")
    OP_7D(0xDC, 0xEB, 0xFF, 0x0, 0x0)
    Jump("loc_E46")

    label("loc_E46")

    MiniGame(0x2F, 0x2, 0x3, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    SetChrFlags(0x10, 0x80)
    SetMapObjFlags(0x4, 0x4)
    SetMapObjFlags(0x8, 0x4)
    SetMapObjFlags(0x9, 0x4)
    SetMapObjFlags(0xA, 0x4)
    SetMapObjFlags(0x2, 0x4)
    SetMapObjFlags(0x3, 0x4)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_ECA")
    ClearMapObjFlags(0x9, 0x4)
    ClearMapObjFlags(0xA, 0x4)
    SetMapObjFrame(0x9, "light", 0x0, 0x1)
    SetMapObjFrame(0xA, "light", 0x0, 0x1)
    Jump("loc_EF0")

    label("loc_ECA")

    ClearMapObjFlags(0x2, 0x4)
    ClearMapObjFlags(0x3, 0x4)
    SetMapObjFrame(0x2, "light", 0x0, 0x1)
    SetMapObjFrame(0x3, "light", 0x0, 0x1)

    label("loc_EF0")

    SetMapObjFrame(0xFF, "sky00", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sky01", 0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1ED, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F1D")
    OP_70(0x5, 0x0)
    Jump("loc_F21")

    label("loc_F1D")

    OP_70(0x5, 0x1E)

    label("loc_F21")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_FC8")
    ClearMapObjFlags(0x6, 0x4)
    SetMapObjFrame(0x6, "light", 0x0, 0x1)
    SetMapObjFlags(0x6, 0x1000)
    OP_78(0x6, 0x12)
    SetChrPos(0x12, -50500, 0, 0, 90)
    OP_D5(0x12, 0x0, 0x15F90, 0x0, 0x0)
    ClearMapObjFlags(0xB, 0x4)
    SetMapObjFrame(0xB, "light", 0x0, 0x1)
    SetMapObjFlags(0xB, 0x1000)
    OP_78(0xB, 0x13)
    SetChrPos(0x13, -22290, 0, -12240, 0)
    OP_D5(0x13, 0x0, 0x0, 0x0, 0x0)

    label("loc_FC8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_1021")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1000")
    SetMapObjFrame(0x9, "mark00", 0x0, 0x1)
    SetMapObjFrame(0xA, "mark00", 0x0, 0x1)
    Jump("loc_101C")

    label("loc_1000")

    SetMapObjFrame(0x2, "mark00", 0x0, 0x1)
    SetMapObjFrame(0x3, "mark00", 0x0, 0x1)

    label("loc_101C")

    Jump("loc_106C")

    label("loc_1021")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1050")
    SetMapObjFrame(0x9, "mark01", 0x0, 0x1)
    SetMapObjFrame(0xA, "mark01", 0x0, 0x1)
    Jump("loc_106C")

    label("loc_1050")

    SetMapObjFrame(0x2, "mark01", 0x0, 0x1)
    SetMapObjFrame(0x3, "mark01", 0x0, 0x1)

    label("loc_106C")

    Return()

    # Function_3_D7D end

    def Function_4_106D(): pass

    label("Function_4_106D")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1ED, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_116D")
    Sound(14, 0, 100, 0)
    OP_74(0x5, 0x1E)
    OP_71(0x5, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x646, 1)"), scpexpr(EXPR_END)), "loc_10F6")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0001
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x646),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1ED, 7)
    OP_E0(0x5, 0x0)
    Jump("loc_1168")

    label("loc_10F6")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0002
    AnonymousTalk(
        0x3E7,
        (
            "宝箱には",
            scpstr(SCPSTR_CODE_ITEM, 0x646),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "が入っている。\x01",
            "持ち物が一杯なので、",
            scpstr(SCPSTR_CODE_ITEM, 0x646),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "をあきらめた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x5, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1168")

    Jump("loc_11B2")

    label("loc_116D")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0003
    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "宝箱には何も入っていない。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_11B2")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_106D end

    def Function_5_11BE(): pass

    label("Function_5_11BE")

    EventBegin(0x2)
    SetMapFlags(0x8000000)

    #A0004
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1Kバス停がある。\x01",
            "バスで移動しますか？\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "クロスベル市東口\x01",      # 0
            "アルモリカ村\x01",          # 1
            "停留所（三叉路）\x01",      # 2
            "やめる\x01",                # 3
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1261")
    Call(0, 6)
    ClearMapFlags(0x8000000)
    NewScene("r0000", 0, 0, 0)
    IdleLoop()
    Jump("loc_12A6")

    label("loc_1261")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1286")
    Call(0, 6)
    ClearMapFlags(0x8000000)
    NewScene("t0000", 0, 0, 0)
    IdleLoop()
    Jump("loc_12A6")

    label("loc_1286")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12A6")
    Call(0, 6)
    ClearMapFlags(0x8000000)
    NewScene("r0030", 0, 0, 0)
    IdleLoop()

    label("loc_12A6")

    ClearMapFlags(0x8000000)
    EventEnd(0x3)
    Return()

    # Function_5_11BE end

    def Function_6_12AE(): pass

    label("Function_6_12AE")

    ClearMapFlags(0x1)
    SetEventSkip(0x0, "loc_13D7")
    Fade(500)
    OP_68(-27530, 1000, 24550, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(570, 0)
    SetCameraDistance(24000, 0)
    OP_E2(0x1)
    SetChrPos(0x0, -32119, 0, 25500, 90)
    SetChrPos(0x1, -32119, 0, 24000, 90)
    SetChrPos(0x2, -32119, 0, 22500, 90)
    SetChrPos(0x3, -32119, 0, 21000, 90)
    ClearChrFlags(0x10, 0x80)
    ClearMapObjFlags(0x4, 0x4)
    OP_78(0x4, 0x10)
    SetMapObjFrame(0x4, "light", 0x0, 0x1)
    OP_49()
    SetChrPos(0x10, -27000, 0, 11850, 0)
    OP_D5(0x10, 0x0, 0x1F4, 0x0, 0x0)
    SetMapObjFlags(0x4, 0x1000)
    OP_74(0x4, 0x1E)
    OP_71(0x4, 0x79, 0xB4, 0x0, 0x20)

    def lambda_138E():
        OP_98(0xFE, 0x0, 0x0, 0x2EE0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_138E)
    OP_0D()
    Sound(466, 0, 100, 0)
    Sound(467, 0, 100, 0)
    WaitChrThread(0x10, 1)
    OP_71(0x4, 0x5B, 0x78, 0x0, 0x0)
    OP_79(0x4)
    Sleep(300)
    FadeToDark(500, 0, -1)
    OP_0D()
    SetEventSkip(0x1, 0x0)

    label("loc_13D7")

    SetScenarioFlags(0x3E, 0)
    Return()

    # Function_6_12AE end

    def Function_7_13DB(): pass

    label("Function_7_13DB")

    EventBegin(0x1)
    FadeToDark(0, 0, -1)
    OP_0D()
    SetChrPos(0x0, -31260, 0, 26050, 90)
    OP_31(0x1)
    OP_68(-31260, 1000, 26050, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(23500, 0)
    EventEnd(0x5)
    Return()

    # Function_7_13DB end

    def Function_8_142C(): pass

    label("Function_8_142C")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(0, 0, -1)
    Sleep(100)
    Sound(459, 0, 100, 0)
    Sleep(2000)
    StopSound(459, 1000, 100)
    Sound(492, 0, 70, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 2)), scpexpr(EXPR_END)), "loc_1487")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_147C")
    Sound(2502, 255, 100, 0)    #voice#Noel
    Jump("loc_1482")

    label("loc_147C")

    Sound(2503, 255, 100, 0)    #voice#Noel

    label("loc_1482")

    Jump("loc_14AB")

    label("loc_1487")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_14A5")
    Sound(3347, 255, 100, 0)    #voice#Lloyd
    Jump("loc_14AB")

    label("loc_14A5")

    Sound(3348, 255, 100, 0)    #voice#Lloyd

    label("loc_14AB")

    Sleep(500)
    FadeToBright(500, 0)
    OP_0D()
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_8_142C end

    def Function_9_14C0(): pass

    label("Function_9_14C0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_16BE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_162F")
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #N0005
    NpcTalk(
        0x8,
        "兵士ノウェ",
        (
            "お、おまえたちは……！\x01",
            "……って、もう捕まえる必要も\x01",
            "ないんだったか。\x02",
        )
    )

    CloseMessageWindow()

    #N0006
    NpcTalk(
        0x8,
        "兵士ノウェ",
        (
            "はあ、結局僕たち国防軍も\x01",
            "何をしたかったんだろうな。\x02",
        )
    )

    CloseMessageWindow()

    #N0007
    NpcTalk(
        0x8,
        "兵士ノウェ",
        (
            "不遇だった警備隊も、\x01",
            "ようやく誇りを持てた。\x01",
            "そんな気がしていたのに……\x02",
        )
    )

    CloseMessageWindow()

    #N0008
    NpcTalk(
        0x8,
        "兵士ノウェ",
        (
            "なんだか長い長い夢を\x01",
            "見せられていたような気がするよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_16B9")

    label("loc_162F")


    #N0009
    NpcTalk(
        0x8,
        "兵士ノウェ",
        (
            "……結局、僕たち国防軍も\x01",
            "何をしたかったんだろうな。\x02",
        )
    )

    CloseMessageWindow()

    #N0010
    NpcTalk(
        0x8,
        "兵士ノウェ",
        (
            "なんだか長い長い夢を\x01",
            "見せられていたような気がするよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16B9")

    Jump("loc_21AA")

    label("loc_16BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1829")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17A8")

    #C0011
    ChrTalk(
        0x8,
        (
            "ウルスラ病院に入院した隊員たちは、\x01",
            "みんな予断を許さない状況らしい。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x8,
        (
            "……いや、彼らは運がいい方だ。\x01",
            "山道で犠牲となった仲間たちは……\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x8,
        (
            "普段、温和な僕だけど……\x01",
            "今回ばかりは怒りを抑えきれないな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1824")

    label("loc_17A8")


    #C0014
    ChrTalk(
        0x8,
        (
            "普段、温和な僕だけど……\x01",
            "今回ばかりは怒りを抑えきれないな。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x8,
        (
            "赤い星座……この借りは\x01",
            "いつか絶対に、返してみせるよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1824")

    Jump("loc_21AA")

    label("loc_1829")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_19B0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1919")

    #C0016
    ChrTalk(
        0x8,
        (
            "昨日の西クロスベル街道での事故は、\x01",
            "かなりの影響が予想されてた。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x8,
        (
            "もし復旧が済んでなかったら、\x01",
            "帝国や共和国に横槍を入れられて\x01",
            "住民投票どころじゃなかったろうね。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x8,
        "復旧にあたった部隊に賞賛を送りたいよ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_19AB")

    label("loc_1919")


    #C0019
    ChrTalk(
        0x8,
        (
            "事故の復旧が済んでなかったら、\x01",
            "帝国や共和国に横槍を入れられて\x01",
            "住民投票どころじゃなかったろうね。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x8,
        "復旧にあたった部隊に賞賛を送りたいよ。\x02",
    )

    CloseMessageWindow()

    label("loc_19AB")

    Jump("loc_21AA")

    label("loc_19B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1B48")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1AA6")

    #C0021
    ChrTalk(
        0x8,
        (
            "クロスベル自治州は、\x01",
            "帝国と共和国にあわせて\x01",
            "１０％もの税収を納めている。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x8,
        (
            "国家独立によって\x01",
            "制度が撤廃されれば、\x01",
            "かなりの予算が浮くだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x8,
        (
            "そうなれば、警備隊の強化なんかは\x01",
            "真っ先に行われるんじゃないかな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1B43")

    label("loc_1AA6")


    #C0024
    ChrTalk(
        0x8,
        (
            "独立によって１０％の税収を\x01",
            "収める制度が撤廃されれば、\x01",
            "かなりの予算が浮くだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x8,
        (
            "そうなれば、警備隊の強化なんかは\x01",
            "真っ先に行われるんじゃないかな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B43")

    Jump("loc_21AA")

    label("loc_1B48")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1CBB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C31")

    #C0026
    ChrTalk(
        0x8,
        (
            "クロスベル自治州は、\x01",
            "帝国と共和国に挟まれた\x01",
            "地形に存在する。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x8,
        (
            "つまり、あの独立提唱は\x01",
            "対立する相手の真っ只中で\x01",
            "宣言されたに等しいわけだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x8,
        (
            "そう考えると、\x01",
            "市長も思い切ったことを\x01",
            "したものだよね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1CB6")

    label("loc_1C31")


    #C0029
    ChrTalk(
        0x8,
        (
            "通商会議での独立提唱は\x01",
            "対立する相手の真っ只中で\x01",
            "宣言されたに等しいわけだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x8,
        (
            "いやあ、市長も思い切ったことを\x01",
            "したものだよね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1CB6")

    Jump("loc_21AA")

    label("loc_1CBB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1E64")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1DBF")

    #C0031
    ChrTalk(
        0x8,
        (
            "共和国のテロリストが\x01",
            "クロスベル入りする……\x01",
            "なんていう情報があるらしい。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x8,
        (
            "テロだなんて穏やかじゃないよ。\x01",
            "自分の主張を通したいなら、\x01",
            "もっと他の方法を考えるべきで……\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x8,
        (
            "……っと、まあこんな事を言っても\x01",
            "仕方ないんだけどね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1E5F")

    label("loc_1DBF")


    #C0034
    ChrTalk(
        0x8,
        (
            "共和国のテロリストが\x01",
            "クロスベル入りする……\x01",
            "なんていう情報があるらしい。\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x8,
        (
            "テロ行為については\x01",
            "色々と思う事はあるけど……\x01",
            "ひとまず警備に専念しなきゃな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E5F")

    Jump("loc_21AA")

    label("loc_1E64")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1FC4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F30")

    #C0036
    ChrTalk(
        0x8,
        (
            "今朝、ロックスミス大統領の\x01",
            "白いリムジンが通っていってね。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x8,
        (
            "出迎えやら交通規制やらで、\x01",
            "なかなかに忙しかったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x8,
        (
            "ＶＩＰの入国というのは、\x01",
            "やはり気を使ってしまうな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1FBF")

    label("loc_1F30")


    #C0039
    ChrTalk(
        0x8,
        (
            "今朝は、ロックスミス大統領の\x01",
            "出迎えやら交通規制やらで、\x01",
            "なかなかに忙しかったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x8,
        (
            "ＶＩＰの入国というのは、\x01",
            "やはり気を使ってしまうな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1FBF")

    Jump("loc_21AA")

    label("loc_1FC4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_21AA")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6F, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2057")

    #C0041
    ChrTalk(
        0x8,
        (
            "いや～、おかげさまで\x01",
            "いい演習になったよ。\x01",
            "君たちもなかなかやるね。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x8,
        (
            "また機会があったら\x01",
            "手合わせをお願いするよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21AA")

    label("loc_2057")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2125")

    #C0043
    ChrTalk(
        0x8,
        (
            "新しくタングラム門に赴任した\x01",
            "ダグラス副司令は、\x01",
            "なかなか気さくな人でね。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x8,
        (
            "あえて例えるなら、\x01",
            "頼れるみんなのアニキって感じかな。\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x8,
        (
            "……仕事となると\x01",
            "鬼のように厳しくなるけどね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_21AA")

    label("loc_2125")


    #C0046
    ChrTalk(
        0x8,
        (
            "ダグラス副司令は、\x01",
            "なかなか気さくな人でね。\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x8,
        (
            "あえて例えるなら、\x01",
            "頼れるみんなのアニキって感じさ。\x01",
            "……仕事では厳しいけどね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_21AA")

    TalkEnd(0xFE)
    Return()

    # Function_9_14C0 end

    def Function_10_21AE(): pass

    label("Function_10_21AE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2399")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22D0")

    #N0048
    NpcTalk(
        0x9,
        "兵士ダイモン",
        (
            "あの青白い大樹の出現もあって、\x01",
            "共和国軍は今のところ\x01",
            "様子見の姿勢でいるようだが……\x02",
        )
    )

    CloseMessageWindow()

    #N0049
    NpcTalk(
        0x9,
        "兵士ダイモン",
        (
            "結界と《神機》を失った今、\x01",
            "油断は禁物だろう。\x02",
        )
    )

    CloseMessageWindow()

    #N0050
    NpcTalk(
        0x9,
        "兵士ダイモン",
        (
            "今のクロスベルを守れるのは\x01",
            "俺たち国防軍だけだ。\x01",
            "厳重に警戒せねばなるまいな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2394")

    label("loc_22D0")


    #N0051
    NpcTalk(
        0x9,
        "兵士ダイモン",
        (
            "あの青白い大樹の出現もあって、\x01",
            "共和国軍は今のところ\x01",
            "様子見の姿勢でいるようだが……\x02",
        )
    )

    CloseMessageWindow()

    #N0052
    NpcTalk(
        0x9,
        "兵士ダイモン",
        (
            "今のクロスベルを守れるのは\x01",
            "俺たち国防軍だけだ。\x01",
            "厳重に警戒せねばなるまいな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2394")

    Jump("loc_2DA1")

    label("loc_2399")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2539")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_24A0")

    #C0053
    ChrTalk(
        0x9,
        (
            "クロスベル市の襲撃を防げなかったのは、\x01",
            "我々警備隊の明らかな失態だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x9,
        (
            "マインツの占領事件のために\x01",
            "戦力を削られていたが……\x01",
            "そんなことは言い訳にはならん。\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x9,
        (
            "治安維持を預かる組織として……\x01",
            "色々と見直されるべきなのかもしれんな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2534")

    label("loc_24A0")


    #C0056
    ChrTalk(
        0x9,
        (
            "クロスベル市の襲撃を防げなかったのは、\x01",
            "我々警備隊の明らかな失態だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x9,
        (
            "治安維持を預かる組織として……\x01",
            "色々と見直されるべきなのかもしれんな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2534")

    Jump("loc_2DA1")

    label("loc_2539")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_25C1")

    #C0058
    ChrTalk(
        0x9,
        (
            "さっき男の遊撃士が\x01",
            "聞き込みをしていったが……\x01",
            "女性遊撃士が行方不明らしいな。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x9,
        "ふむ……何事もなければいいのだが。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2DA1")

    label("loc_25C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2663")

    #C0060
    ChrTalk(
        0x9,
        (
            "遊撃士たちも、\x01",
            "《幻獣》を追って様々な場所を\x01",
            "探索しているようだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x9,
        (
            "彼らは我々では入り込めない\x01",
            "奥地の方にも詳しいからな。\x01",
            "頼もしい連中だよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DA1")

    label("loc_2663")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_27B6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2758")

    #C0062
    ChrTalk(
        0x9,
        (
            "もし《幻獣》が外国人を\x01",
            "傷つけるようなことがあれば、\x01",
            "２大国は必ずそれを利用するだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x9,
        (
            "国境の緊張状態にもストレートに\x01",
            "絡んでくる以上、決して警備隊も\x01",
            "見過ごせる問題ではないんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x9,
        "調査はよろしく頼んだぞ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_27B1")

    label("loc_2758")


    #C0065
    ChrTalk(
        0x9,
        (
            "幻獣の問題は、決して警備隊も\x01",
            "見過ごせるものではない。\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x9,
        "調査はよろしく頼んだぞ。\x02",
    )

    CloseMessageWindow()

    label("loc_27B1")

    Jump("loc_2DA1")

    label("loc_27B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_284E")

    #C0067
    ChrTalk(
        0x9,
        (
            "テロリストに関しては、\x01",
            "我々も総力を挙げて\x01",
            "警戒に当たっている。\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x9,
        (
            "警備隊のメンツにかけて、\x01",
            "その侵入を必ずや\x01",
            "防いでみせなければな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DA1")

    label("loc_284E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_28D7")

    #C0069
    ChrTalk(
        0x9,
        (
            "ロックスミス大統領は、\x01",
            "庶民派として共和国民に\x01",
            "支持されているという。\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x9,
        (
            "果たして、実際は\x01",
            "いかなる人物なのだろうな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DA1")

    label("loc_28D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2DA1")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6F, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_299B")

    #C0071
    ChrTalk(
        0x9,
        (
            "ノエル曹長がいるとはいえ、\x01",
            "ダグラス副司令とあそこまでの\x01",
            "善戦を繰り広げるとは……\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0x9,
        (
            "さすがは教団事件の立役者、\x01",
            "特務支援課という所か。\x01",
            "正直、感服させてもらったぞ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DA1")

    label("loc_299B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14F, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C48")

    #C0073
    ChrTalk(
        0x9,
        (
            "ノエル曹長、お疲れ様です！\x01",
            "……………………………………\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x109,
        (
            "#10100Fお疲れ様です、ダイモンさん。\x01",
            "……えっと、どうかしましたか？\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0x9,
        (
            "……ふむ、なんというか……\x01",
            "警備隊の制服を着ていない曹長も、\x01",
            "なんだか新鮮だと思いまして。\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x109,
        (
            "#10105Fああ、そういえばこの格好で\x01",
            "タングラム門をうろつくのは\x01",
            "初めてかも……\x02\x03",

            "#10112Fすみません、ちょっと\x01",
            "配慮が足りなかったですかね。\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0x9,
        (
            "い、いえ。\x01",
            "大変よろしいかと……\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0x104,
        (
            "#00300Fはは～あ、さては……\x01",
            "ノエルの見慣れない格好に\x01",
            "ときめいちまったか？\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0x109,
        "#10105Fへっ！？\x02",
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0x9,
        (
            "い、いや、その。\x01",
            "決してそういうアレでは。\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0x9,
        (
            "……し、失礼しました。\x01",
            "忘れてください、曹長。\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x109,
        (
            "#10106F（ラ、ランディ先輩ったら。\x01",
            "  恥ずかしいなあもう……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x14F, 7)
    Jump("loc_2DA1")

    label("loc_2C48")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D24")

    #C0083
    ChrTalk(
        0x9,
        (
            "……正直、服装の違いくらいで\x01",
            "動揺しすぎましたな。\x01",
            "私も修行が足りません。\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x9,
        (
            "大変失礼しました。\x01",
            "曹長、忘れてください。\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0x109,
        "#10106Fは、はあ……\x02",
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x101,
        (
            "#00006F（修行とか、\x01",
            "  そんな問題なのか……？）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2DA1")

    label("loc_2D24")


    #C0087
    ChrTalk(
        0x9,
        (
            "……正直、服装の違いくらいで\x01",
            "動揺しすぎましたな。\x01",
            "私も修行が足りません。\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0x9,
        (
            "大変失礼しました。\x01",
            "曹長、忘れてください。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2DA1")

    TalkEnd(0xFE)
    Return()

    # Function_10_21AE end

    def Function_11_2DA5(): pass

    label("Function_11_2DA5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2EC2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E5D")

    #C0089
    ChrTalk(
        0xC,
        "この人たち、街の東口で会ってね。\x02",
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0xC,
        (
            "私と一緒にタングラム門に\x01",
            "行きたいっていうから\x01",
            "護衛代わりに連れてきたのに……\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0xC,
        "……正直、役立たずだったね。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_2EC2")

    label("loc_2E5D")


    #C0092
    ChrTalk(
        0xC,
        (
            "それにしても、街道を歩くのは\x01",
            "なかなかスリリングだった。\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0xC,
        "このままアルモリカ村に行こうかな。\x02",
    )

    CloseMessageWindow()

    label("loc_2EC2")

    TalkEnd(0xFE)
    Return()

    # Function_11_2DA5 end

    def Function_12_2EC6(): pass

    label("Function_12_2EC6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2FED")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F91")

    #C0094
    ChrTalk(
        0xD,
        (
            "はあ、はあ……\x01",
            "途中で幻獣に遭遇した時は\x01",
            "どうなる事かと思ったが……\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0xD,
        (
            "……と、とにかく辿りついたんだ。\x01",
            "あとは共和国に帰るだけ……\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0xD,
        "ほ、本当に帰れるんだろうな……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_2FED")

    label("loc_2F91")


    #C0097
    ChrTalk(
        0xD,
        (
            "ここまでの仕打ちは\x01",
            "生まれて初めてだぞ……\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0xD,
        (
            "ほ、本当に共和国に\x01",
            "帰れるんだろうな……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2FED")

    TalkEnd(0xFE)
    Return()

    # Function_12_2EC6 end

    def Function_13_2FF1(): pass

    label("Function_13_2FF1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_30FD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_30AB")

    #C0099
    ChrTalk(
        0xE,
        (
            "ぜえ、ぜえ……\x01",
            "て、てっきり安全な道でも\x01",
            "知ってるとばかり思ってたが……\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0xE,
        (
            "まさか、普通に街道を\x01",
            "マラソンするハメになるとは……\x01",
            "し、死ぬかと思った……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_30FD")

    label("loc_30AB")


    #C0101
    ChrTalk(
        0xE,
        (
            "うう、何で俺たちが\x01",
            "こんな目に……\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0xE,
        (
            "クロスベルなんて\x01",
            "もうコリゴリだぜ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_30FD")

    TalkEnd(0xFE)
    Return()

    # Function_13_2FF1 end

    def Function_14_3101(): pass

    label("Function_14_3101")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_320C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_31D5")

    #C0103
    ChrTalk(
        0xF,
        (
            "せっかく結界が解けたのに、\x01",
            "クルマが手に入らなくてさ……\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0xF,
        (
            "偶然会った彼女に\x01",
            "案内してもらったら、\x01",
            "こんなしんどい事に……\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0xF,
        (
            "や、やっぱりヒッチハイクでも\x01",
            "すればよかったよ……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_320C")

    label("loc_31D5")


    #C0106
    ChrTalk(
        0xF,
        (
            "や、やっぱりヒッチハイクでも\x01",
            "すればよかったよ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_320C")

    TalkEnd(0xFE)
    Return()

    # Function_14_3101 end

    def Function_15_3210(): pass

    label("Function_15_3210")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_33C0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_331D")

    #N0107
    NpcTalk(
        0xA,
        "兵士ギャリソン",
        (
            "副司令の指示で、\x01",
            "共和国方面の警戒を\x01",
            "続けちゃいるけど……\x02",
        )
    )

    CloseMessageWindow()

    #N0108
    NpcTalk(
        0xA,
        "兵士ギャリソン",
        (
            "以前、２大国の軍を撃退できたのは\x01",
            "《神機》の力あってこそだった。\x02",
        )
    )

    CloseMessageWindow()

    #N0109
    NpcTalk(
        0xA,
        "兵士ギャリソン",
        (
            "今度また侵攻してきたら……\x01",
            "多分、止めようがないだろうね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_33BB")

    label("loc_331D")


    #N0110
    NpcTalk(
        0xA,
        "兵士ギャリソン",
        (
            "以前軍を撃退できたのは\x01",
            "神機の力あってこそだった。\x02",
        )
    )

    CloseMessageWindow()

    #N0111
    NpcTalk(
        0xA,
        "兵士ギャリソン",
        (
            "今度また共和国軍が侵攻してきたら……\x01",
            "多分、止めようがないだろうね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_33BB")

    Jump("loc_3C94")

    label("loc_33C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3533")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_34AA")

    #C0112
    ChrTalk(
        0xA,
        (
            "猟兵団から甚大な被害を受けて、\x01",
            "警備隊はボロボロになってしまった。\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0xA,
        (
            "あんな連中とまた戦えと言われたら、\x01",
            "俺は正直、逃げてしまいたくなるよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0xA,
        (
            "これから一体、俺たちは\x01",
            "どうしていくべきなんだろうか……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_352E")

    label("loc_34AA")


    #C0115
    ChrTalk(
        0xA,
        (
            "猟兵団とまた戦えと言われたら、\x01",
            "俺は正直、逃げてしまいたくなるよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0xA,
        (
            "これから一体、俺たちは\x01",
            "どうしていくべきなんだろうか……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_352E")

    Jump("loc_3C94")

    label("loc_3533")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3648")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_35D2")

    #C0117
    ChrTalk(
        0xA,
        "……ぶえっくしっ！！\x02",
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0xA,
        (
            "……ちょっと体を\x01",
            "冷やしちゃったかな。\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0xA,
        (
            "風邪を引いたりしてもなんだし\x01",
            "ちょっと休憩してくるかな……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3643")

    label("loc_35D2")


    #C0120
    ChrTalk(
        0xA,
        (
            "ちょっと体を\x01",
            "冷やしちゃったし、\x01",
            "食堂で一服してくるか……\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0xA,
        (
            "この緊張状態の中、\x01",
            "体調を崩してもなんだしね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3643")

    Jump("loc_3C94")

    label("loc_3648")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_37DA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3744")

    #C0122
    ChrTalk(
        0xA,
        (
            "今、タングラム丘陵は\x01",
            "クロスベルと共和国、どちらの領土か\x01",
            "曖昧な状態になっているんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0xA,
        (
            "現在、事実上は共和国が保有している\x01",
            "ことになってるけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0xA,
        (
            "クロスベルが独立、\x01",
            "なんてことになれば……\x01",
            "しばらくは揉めそうだな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_37D5")

    label("loc_3744")


    #C0125
    ChrTalk(
        0xA,
        (
            "今、タングラム丘陵は\x01",
            "クロスベルと共和国、どちらの領土か\x01",
            "曖昧な状態になっているんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0xA,
        (
            "独立が実現したとしても、\x01",
            "しばらくは揉めそうだな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_37D5")

    Jump("loc_3C94")

    label("loc_37DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_393B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_38B8")

    #C0127
    ChrTalk(
        0xA,
        (
            "住民投票の日が近づくにつれ、\x01",
            "圧力も日増しに強くなって来てるな。\x02",
        )
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0xA,
        (
            "共和国民も、クロスベルの独立には\x01",
            "反対の意を示しているらしい。\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0xA,
        (
            "あまり露骨な運動や政策に\x01",
            "発展しないことを祈りたいね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3936")

    label("loc_38B8")


    #C0130
    ChrTalk(
        0xA,
        (
            "共和国民も、クロスベルの独立には\x01",
            "反対の意を示しているらしい。\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0xA,
        (
            "あまり露骨な運動や政策に\x01",
            "発展しないことを祈りたいね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3936")

    Jump("loc_3C94")

    label("loc_393B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3ADC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A33")

    #C0132
    ChrTalk(
        0xA,
        (
            "タングラム丘陵は\x01",
            "見ての通り見晴らしがいいし、\x01",
            "監視用の施設もある。\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0xA,
        (
            "向かってくる飛行艇や車があれば\x01",
            "すぐに分かるはずさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0xA,
        (
            "無論、そう簡単な話じゃないけど……\x01",
            "大丈夫、テロリストなんか\x01",
            "絶対に入れさせやしないよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3AD7")

    label("loc_3A33")


    #C0135
    ChrTalk(
        0xA,
        (
            "タングラム丘陵は\x01",
            "見ての通り見晴らしがいいし、\x01",
            "監視用の施設もある。\x02",
        )
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0xA,
        (
            "無論、そう簡単な話じゃないけど……\x01",
            "大丈夫、テロリストなんか\x01",
            "絶対に入れさせやしないよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3AD7")

    Jump("loc_3C94")

    label("loc_3ADC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3B7A")

    #C0137
    ChrTalk(
        0xA,
        (
            "ロックスミス大統領のリムジンは、\x01",
            "何台もの護衛の車に守られていてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0xA,
        (
            "さすがは共和国を統治する大統領……\x01",
            "あの光景はまさに壮観だったよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C94")

    label("loc_3B7A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3C94")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3C33")

    #C0139
    ChrTalk(
        0xA,
        (
            "一面に広がるタングラム丘陵……\x01",
            "とてもいい眺めだよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0xA,
        (
            "歴史上、何度も紛争の舞台に\x01",
            "なったと言われているけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0xA,
        "俺はこの景色、なかなか好きだよ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3C94")

    label("loc_3C33")


    #C0142
    ChrTalk(
        0xA,
        (
            "一面に広がるタングラム丘陵……\x01",
            "とてもいい眺めだよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0xA,
        "俺はこの景色、なかなか好きだよ。\x02",
    )

    CloseMessageWindow()

    label("loc_3C94")

    TalkEnd(0xFE)
    Return()

    # Function_15_3210 end

    def Function_16_3C98(): pass

    label("Function_16_3C98")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3E27")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D8B")

    #N0144
    NpcTalk(
        0xB,
        "兵士バレル",
        (
            "あの得体の知れない樹木……\x01",
            "きっとクロスベル全土から\x01",
            "見えてるはずだ。\x02",
        )
    )

    CloseMessageWindow()

    #N0145
    NpcTalk(
        0xB,
        "兵士バレル",
        (
            "あんなもんが突然現れるなんて、\x01",
            "絶対に普通じゃない。\x02",
        )
    )

    CloseMessageWindow()

    #N0146
    NpcTalk(
        0xB,
        "兵士バレル",
        (
            "クロスベルは一体\x01",
            "どうなっちまうんだろう……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3E22")

    label("loc_3D8B")


    #N0147
    NpcTalk(
        0xB,
        "兵士バレル",
        (
            "得体の知れない樹木……\x01",
            "あんなもんが突然現れるなんて、\x01",
            "絶対に普通じゃない。\x02",
        )
    )

    CloseMessageWindow()

    #N0148
    NpcTalk(
        0xB,
        "兵士バレル",
        (
            "ベルガード門にいる\x01",
            "ブルードは大丈夫かな……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3E22")

    Jump("loc_4814")

    label("loc_3E27")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3F9C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F1E")

    #C0149
    ChrTalk(
        0xB,
        (
            "ベルガード門にいる\x01",
            "幼馴染のブルードは\x01",
            "無事だったみたいだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0xB,
        (
            "……だけど、安心はできない。\x01",
            "警備隊が失ったものは\x01",
            "やっぱりデカいからな。\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0xB,
        (
            "正直言って、これから\x01",
            "どうなっていくか怖いけど……\x01",
            "覚悟するしかねえよな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3F97")

    label("loc_3F1E")


    #C0152
    ChrTalk(
        0xB,
        (
            "警備隊が失ったものは\x01",
            "やっぱりデカい。\x02",
        )
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0xB,
        (
            "正直言って、これから\x01",
            "どうなっていくか怖いけど……\x01",
            "覚悟するしかねえよな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3F97")

    Jump("loc_4814")

    label("loc_3F9C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_4106")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_408B")

    #C0154
    ChrTalk(
        0xB,
        (
            "今日はレーダー施設の方が\x01",
            "フル稼働で働いてるみたいだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0xB,
        (
            "雨が降ってると、\x01",
            "空の状況も目視じゃ分かりにくい。\x01",
            "警備上かなり重宝してるぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0xB,
        (
            "通商会議のときは壊されちまったが、\x01",
            "ちゃんと役立ってくれてんのさ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4101")

    label("loc_408B")


    #C0157
    ChrTalk(
        0xB,
        (
            "レーダー施設は\x01",
            "警備上かなり重宝してるぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0xB,
        (
            "通商会議のときは壊されちまったが、\x01",
            "ちゃんと役立ってくれてんのさ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4101")

    Jump("loc_4814")

    label("loc_4106")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_4181")

    #C0159
    ChrTalk(
        0xB,
        (
            "ダグラス副司令は気さくだが、\x01",
            "あれでかなりクールなお人なんだよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0xB,
        "俺もあれくらいになれたらなあ……\x02",
    )

    CloseMessageWindow()
    Jump("loc_4814")

    label("loc_4181")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_434B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4299")

    #C0161
    ChrTalk(
        0xB,
        (
            "幻獣ってのは、\x01",
            "以前《月の僧院》に出た幽霊みたいな\x01",
            "得体の知れないもんらしいな。\x02",
        )
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0xB,
        (
            "単に外見が怖いくらいならいいが、\x01",
            "正体そのものが分からないってのは\x01",
            "不気味な恐怖があるよ……\x02",
        )
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0xB,
        (
            "もし鉢合わせすることがあっても、\x01",
            "また気を失わないようにしないとな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4346")

    label("loc_4299")


    #C0164
    ChrTalk(
        0xB,
        (
            "以前《月の僧院》に出た幽霊を\x01",
            "調査しに行ったときは、\x01",
            "アワくってぶっ倒れちまったんだよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0xB,
        (
            "もし幻獣と鉢合わせすることがあっても、\x01",
            "また気を失わないようにしないとな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4346")

    Jump("loc_4814")

    label("loc_434B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_44C6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_442D")

    #C0166
    ChrTalk(
        0xB,
        (
            "警察の情報じゃテロリストが\x01",
            "現れる可能性が高いらしい。\x02",
        )
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0xB,
        (
            "そんな危ないヤツらと\x01",
            "やりあったりするなんて\x01",
            "正直、ゴメンだぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0xB,
        (
            "ああ、空の女神様。\x01",
            "どうか今日という日が\x01",
            "平和に終わりますように……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_44C1")

    label("loc_442D")


    #C0169
    ChrTalk(
        0xB,
        (
            "テロリストなんて危ない奴らと\x01",
            "やりあったりするなんて\x01",
            "正直、ゴメンだぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0xB,
        (
            "ああ、空の女神様。\x01",
            "どうか今日という日が\x01",
            "平和に終わりますように……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_44C1")

    Jump("loc_4814")

    label("loc_44C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_4694")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_45E8")

    #C0171
    ChrTalk(
        0xB,
        (
            "大統領のリムジンの迎え入れなんて、\x01",
            "正直、緊張しちまったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0xB,
        (
            "俺ってビビリだからな～……\x01",
            "敬礼のときも、なんかポーズが\x01",
            "おかしくなっちまった気がするぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0xB,
        (
            "ま、大統領閣下は俺みたいな\x01",
            "一兵卒なんて気にしてないだろうが……\x01",
            "それでも充分プレッシャーだったよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_468F")

    label("loc_45E8")


    #C0174
    ChrTalk(
        0xB,
        (
            "大統領のリムジンの迎え入れなんて\x01",
            "正直、緊張しちまったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0xB,
        (
            "ま、大統領閣下は俺みたいな\x01",
            "一兵卒なんて気にしてないだろうが……\x01",
            "それでも充分プレッシャーだったよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_468F")

    Jump("loc_4814")

    label("loc_4694")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_4814")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_477D")

    #C0176
    ChrTalk(
        0xB,
        (
            "帝国方面のベルガード門には、\x01",
            "ブルードって幼馴染がいるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0xB,
        (
            "この間、あいつから\x01",
            "リハビリ訓練が無事に\x01",
            "終了したって聞いてさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0xB,
        (
            "いや～、一時は心配したけど……\x01",
            "完全に回復できたみたいで安心したぜ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4814")

    label("loc_477D")


    #C0179
    ChrTalk(
        0xB,
        (
            "この間、幼馴染のブルードから\x01",
            "リハビリ訓練が無事に\x01",
            "終了したって聞いてさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0xB,
        (
            "いや～、一時は心配したけど……\x01",
            "完全に回復できたみたいで安心したぜ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4814")

    TalkEnd(0xFE)
    Return()

    # Function_16_3C98 end

    def Function_17_4818(): pass

    label("Function_17_4818")

    SetMapFlags(0x80)
    SetMapFlags(0x8000000)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x31, 2)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_484A")
    SetScenarioFlags(0x31, 2)

    label("loc_484A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4890")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 2)), scpexpr(EXPR_END)), "loc_488A")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_487F")
    Sound(2499, 255, 100, 0)    #voice#Noel
    Jump("loc_4885")

    label("loc_487F")

    Sound(3537, 255, 100, 0)    #voice#Noel

    label("loc_4885")

    Jump("loc_4890")

    label("loc_488A")

    Sound(3344, 255, 100, 0)    #voice#Lloyd

    label("loc_4890")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4B4D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_END)), "loc_4909")
    MenuCmd(0, 0)
    MenuCmd(1, 0, "メルカバに乗り込む")
    MenuCmd(1, 0, "やめる")
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_48E9"),
        (SWITCH_DEFAULT, "loc_48FA"),
    )


    label("loc_48E9")

    SetScenarioFlags(0x22, 0)
    NewScene("e3020", 0, 0, 0)
    IdleLoop()
    Jump("loc_4904")

    label("loc_48FA")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4904")

    Jump("loc_4B48")

    label("loc_4909")

    MenuCmd(0, 0)
    MenuCmd(1, 0, "導力車で移動する")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_493D")
    MenuCmd(1, 0, "導力車で休憩する")

    label("loc_493D")

    MenuCmd(1, 0, "やめる")
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_4971"),
        (1, "loc_4A75"),
        (2, "loc_4B06"),
        (SWITCH_DEFAULT, "loc_4B3E"),
    )


    label("loc_4971")

    SetMapObjFrame(0x6, "light", 0x0, 0x1)
    OP_74(0x6, 0x1E)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_49A2")
    OP_70(0x6, 0x12C)
    OP_71(0x6, 0x12C, 0x14A, 0x0, 0x0)
    Jump("loc_49B2")

    label("loc_49A2")

    OP_70(0x6, 0xF0)
    OP_71(0x6, 0xF0, 0x10E, 0x0, 0x0)

    label("loc_49B2")

    Sound(462, 0, 100, 0)
    SoundLoad(2500)
    SoundLoad(3538)
    SoundLoad(3345)
    Sleep(700)
    FadeToDark(300, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x2E, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4A08")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4A08")

    FadeToDark(0, 0, -1)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D4, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4A2B")
    Sound(461, 0, 100, 0)

    label("loc_4A2B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4A4B")
    OP_70(0x6, 0x14A)
    OP_71(0x6, 0x14A, 0x12C, 0x0, 0x0)
    Jump("loc_4A5B")

    label("loc_4A4B")

    OP_70(0x6, 0x10E)
    OP_71(0x6, 0x10E, 0xF0, 0x0, 0x0)

    label("loc_4A5B")

    Sleep(1000)
    OP_0D()
    SetMapObjFrame(0x6, "light", 0x1, 0x1)
    OP_70(0x6, 0x0)
    Jump("loc_4890")

    label("loc_4A75")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_4AE7")
    OP_57(0x0)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_5A()
    Sound(13, 0, 100, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 0)), scpexpr(EXPR_END)), "loc_4AAA")
    OP_32(0xFF, 0xFF, 0x0)
    Jump("loc_4AC2")

    label("loc_4AAA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_4ABD")
    OP_32(0xFF, 0xFE, 0x0)
    Jump("loc_4AC2")

    label("loc_4ABD")

    OP_32(0xFF, 0xFA, 0x0)

    label("loc_4AC2")

    OP_6A(0x0, 0x0)
    Sleep(3500)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4B01")

    label("loc_4AE7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_4AF7")
    OP_AF(0xFB)
    Jump("loc_4B01")

    label("loc_4AF7")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4B01")

    Jump("loc_4B48")

    label("loc_4B06")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4B1F")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4B39")

    label("loc_4B1F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_4B2F")
    OP_AF(0xFB)
    Jump("loc_4B39")

    label("loc_4B2F")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4B39")

    Jump("loc_4B48")

    label("loc_4B3E")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4B48")

    Jump("loc_4890")

    label("loc_4B4D")

    ClearMapFlags(0x8000000)
    OP_60(0x0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    # Function_17_4818 end

    def Function_18_4B5B(): pass

    label("Function_18_4B5B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_4BA3")
    EventBegin(0x2)
    ClearMapFlags(0x20)
    SetChrName("")

    #A0181
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "導力バスは運行を見合わせているようだ。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    EventEnd(0x3)
    Return()

    label("loc_4BA3")

    Call(0, 5)
    Return()

    # Function_18_4B5B end

    def Function_19_4BA7(): pass

    label("Function_19_4BA7")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x101, -45000, 0, 11000, 0)
    SetChrPos(0x109, -45000, 0, 11000, 0)
    OP_78(0x8, 0x11)
    OP_49()
    SetChrPos(0x11, 20000, -10000, -39000, 0)
    OP_D5(0x11, 0x0, 0x41EB0, 0x0, 0x0)
    SetMapObjFlags(0x8, 0x1000)
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    OP_11(0xCC, 0xA3, 0x6A, 0x26, 0xE6, 0x0)
    SetMapObjFrame(0xFF, "sky00", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky01", 0x1, 0x1)
    OP_68(-15000, 1500, 0, 0)
    MoveCamera(50, 17, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(44000, 0)
    OP_68(-20000, -6000, -30000, 10000)
    FadeToBright(2000, 0)
    OP_0D()
    PlaceName2(340, 200, "c_plac19", 0x0, 0)
    OP_6F(0x79)
    Fade(500)
    OP_68(-20000, -7500, -39000, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(750, 0)
    SetCameraDistance(18000, 0)
    OP_68(-40000, -7500, -39000, 6000)
    MoveCamera(45, 15, 0, 6000)
    SetCameraDistance(33000, 6000)
    Sound(455, 0, 100, 0)
    ClearMapObjFlags(0x8, 0x4)
    OP_82(0x64, 0x0, 0xBB8, 0x1B58)

    def lambda_4D0D():
        OP_96(0xFE, 0xFFFE2B40, 0xFFFFD8F0, 0xFFFF67A8, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_4D0D)
    OP_6F(0x79)
    FadeToDark(2000, 0, -1)
    OP_0D()
    EndChrThread(0x11, 0x1)
    SetScenarioFlags(0x22, 0)
    NewScene("e0410", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_19_4BA7 end

    def Function_20_4D40(): pass

    label("Function_20_4D40")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50011.itc", 0x1E)
    SoundLoad(803)
    CreatePortrait(0, 180, 0, 436, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis007.itp")
    SetChrPos(0x101, -18420, 0, 290, 270)
    SetChrPos(0x102, -17710, 0, -820, 270)
    SetChrPos(0x104, -17010, 0, 1050, 270)
    SetChrPos(0x109, -15460, 0, 420, 270)
    SetChrPos(0x105, -15120, 0, -1000, 270)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_68(-16000, 1000, 0, 0)
    MoveCamera(34, 33, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(21210, 0)
    OP_68(-28490, 1000, 340, 6000)
    BeginChrThread(0x101, 0, 0, 21)
    BeginChrThread(0x102, 0, 0, 22)
    BeginChrThread(0x104, 0, 0, 23)
    BeginChrThread(0x105, 0, 0, 24)
    BeginChrThread(0x109, 0, 0, 25)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(4500)
    Sound(803, 2, 100, 0)
    Sleep(500)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    WaitChrThread(0x101, 0)
    Fade(250)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    Sound(802, 0, 100, 0)
    Sleep(500)

    #C0182
    ChrTalk(
        0x101,
        "#00005F#5Pおっと……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 0)

    def lambda_4EB2():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_4EB2)

    #C0183
    ChrTalk(
        0x102,
        "#00105F#12P他の部署からの連絡かしら？\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x1)
    OP_24(0x323)
    Sound(804, 0, 100, 0)
    Sleep(300)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    FadeToDark(500, 0, 100)
    OP_0D()
    OP_CC(0x0, 0x0, 0x3)
    #Sound(2084, 255, 100, 0)    #voice#Lloyd
    SetMessageWindowPos(90, 130, -1, -1)

    #A0184
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00000F#30Wはい、特務支援課、\x01",
            "ロイド・バニングスです。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("逞しい声")

    #A0185
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ウフフっ……\x01",
            "アタシよ、アタシ。\x02\x03",

            "誰だか判るかしら？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    SetMessageWindowPos(90, 130, -1, -1)

    #A0186
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00012Fミシェルさん……\x01",
            "えっと、どうしたんですか？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("ミシェルの声")

    #A0187
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ウフフ、一発で判るなんて\x01",
            "なかなか冴えてるじゃない。\x02\x03",

            "それとも愛のなせる業かしら？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0188
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00006Fいえ、ミシェルさん以外に\x01",
            "該当者が思いつかなかっただけで。\x02\x03",

            "#00000Fひょっとして、そちらに伺ってる\x01",
            "キーアのことですか？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("ミシェルの声")

    #A0189
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "あ、それなんだけど。\x02\x03",

            "あの子、シズクちゃんを連れて\x01",
            "港湾区に遊びに行っちゃったわ。\x02\x03",

            "ツァイトだったかしら？\x01",
            "あの警察犬が一緒だったから\x01",
            "大丈夫だとは思うんだけど。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0190
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00002Fああ、ツァイトが一緒なら\x01",
            "何の心配もいらないと思います。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("ミシェルの声")

    #A0191
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "あら、やっぱり？\x02\x03",

            "話は聞いていたけど、\x01",
            "カレ、すっごく貫禄があるわね。\x02\x03",

            "さすが伝説の《神狼》と\x01",
            "言われてるだけはあるじゃない？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0192
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00004Fハハ……さすがに伝説の狼とは\x01",
            "別物だとは思いますけど。\x02\x03",

            "#00005Fあ、わざわざその事を\x01",
            "知らせてくれたんですか？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("ミシェルの声")

    #A0193
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ううん、こちらが本題なんだけど。\x02\x03",

            "実は、アリオスがアナタたちと\x01",
            "情報交換がしたいらしいのよ。\x02\x03",

            "夕方くらいに戻って来るんだけど\x01",
            "何とか時間が取れないかしら？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0194
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00000F夕方ですか……\x01",
            "それだったら大丈夫かと。\x02\x03",

            "情報交換ということは、\x01",
            "やはり通商会議についてですか？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("ミシェルの声")

    #A0195
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "それもあるけど……\x01",
            "《黒月》と《赤い星座》に関してね。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    SetMessageWindowPos(90, 130, -1, -1)

    #A0196
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00003F……判りました。\x02\x03",

            "#00001F一通り用事を済ませたら\x01",
            "そちらに伺います。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("ミシェルの声")

    #A0197
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ええ、待ってるわ。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    OP_CC(0x0, 0x0, 0x3)
    SetChrSubChip(0x101, 0x0)
    Sound(804, 0, 100, 0)

    #C0198
    ChrTalk(
        0x102,
        (
            "#00100F#12P遊撃士協会の\x01",
            "ミシェルさんからみたいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0x104,
        "#00305F#11P何かあったのかよ？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    ClearChrFlags(0x101, 0x20)
    ClearChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    Sound(802, 0, 100, 0)
    OP_0D()
    OP_93(0x101, 0x5A, 0x1F4)

    #C0200
    ChrTalk(
        0x101,
        "#00006F#5Pいや、情報交換の申し出さ。\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    #A0201
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ロイドはミシェルの用件について\x01",
            "他のメンバーに説明した。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0202
    ChrTalk(
        0x104,
        (
            "#00303F#11P《黒月》と《赤い星座》か……\x02\x03",

            "#00301F確かにアリオスのオッサンなら\x01",
            "自治州外の情報にも詳しそうだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0203
    ChrTalk(
        0x105,
        (
            "#10304F#11Pフフ、渡りに舟かもしれないね。\x02\x03",

            "#10300Fそれじゃあ今から\x01",
            "クロスベル市に戻るのかい？\x02",
        )
    )

    CloseMessageWindow()

    #C0204
    ChrTalk(
        0x101,
        (
            "#00000F#5Pいや、アリオスさんが\x01",
            "戻ってくるのは夕方らしい。\x02\x03",

            "それまでは、こちらの用事を\x01",
            "済ませていても大丈夫だろう。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14F, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14F, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x149, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_588E")

    #C0205
    ChrTalk(
        0x102,
        (
            "#00104F#12P《赤い星座》の情報は\x01",
            "一通り集められたけど……\x02\x03",

            "#00102Fせっかく車があるから\x01",
            "まだ色々回っても良さそうね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_590A")

    label("loc_588E")


    #C0206
    ChrTalk(
        0x102,
        (
            "#00103F#12P《赤い星座》の情報も\x01",
            "それほど集まっていないし……\x02\x03",

            "#00100Fせっかく車があるから\x01",
            "色々回ってみても良さそうね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_590A")


    #C0207
    ChrTalk(
        0x109,
        (
            "#10100F#11Pそれでは、用事を済ませたら\x01",
            "東通りのギルドに行きましょう。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_CC(0x1, 0xFF, 0x0)
    OP_D7(0x1E)
    SetChrPos(0x0, -29000, 0, -250, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetScenarioFlags(0x140, 2)
    OP_29(0xA3, 0x1, 0x6)
    OP_24(0x323)
    EventEnd(0x5)
    Return()

    # Function_20_4D40 end

    def Function_21_598F(): pass

    label("Function_21_598F")

    OP_9B(0x0, 0xFE, 0x0, 0x2EE0, 0x7D0, 0x0)
    Return()

    # Function_21_598F end

    def Function_22_599F(): pass

    label("Function_22_599F")

    Sleep(50)
    OP_9B(0x0, 0xFE, 0x0, 0x2EE0, 0x7D0, 0x0)
    Return()

    # Function_22_599F end

    def Function_23_59B2(): pass

    label("Function_23_59B2")

    Sleep(100)
    OP_9B(0x0, 0xFE, 0x0, 0x2EE0, 0x7D0, 0x0)
    Return()

    # Function_23_59B2 end

    def Function_24_59C5(): pass

    label("Function_24_59C5")

    Sleep(150)
    OP_9B(0x0, 0xFE, 0x0, 0x2EE0, 0x7D0, 0x0)
    Return()

    # Function_24_59C5 end

    def Function_25_59D8(): pass

    label("Function_25_59D8")

    Sleep(200)
    OP_9B(0x0, 0xFE, 0x0, 0x2EE0, 0x7D0, 0x0)
    Return()

    # Function_25_59D8 end

    def Function_26_59EB(): pass

    label("Function_26_59EB")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-19190, 1000, -11460, 0)
    MoveCamera(69, 23, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(15590, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetMapObjFlags(0x6, 0x4)
    SetCameraDistance(17960, 3000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x10)
    Sleep(1000)
    OP_68(-22700, 2480, 50, 7000)
    MoveCamera(75, 17, 0, 7000)
    OP_6E(510, 7000)
    SetCameraDistance(42860, 7000)
    PlaceName2(340, 200, "c_plac19", 0x0, 4000)
    OP_6F(0x79)
    Sleep(3000)
    OP_68(-46580, 2500, -1750, 4000)
    MoveCamera(48, 28, 0, 4000)
    OP_6E(510, 4000)
    SetCameraDistance(22180, 4000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5C8F")
    Sleep(2500)
    SetChrPos(0x101, -53200, 0, 220, 90)
    SetChrPos(0x102, -54130, 0, -950, 90)
    SetChrPos(0x104, -54120, 0, 1520, 90)
    SetChrPos(0x109, -55800, 0, 1010, 90)
    SetChrPos(0x105, -56000, 0, -620, 90)

    def lambda_5B61():
        OP_97(0xFE, 0x1F40, 0x0, 0x0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5B61)

    def lambda_5B7B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5B7B)
    Sleep(100)

    def lambda_5B8F():
        OP_97(0xFE, 0x1F40, 0x0, 0x0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5B8F)

    def lambda_5BA9():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_5BA9)
    Sleep(120)

    def lambda_5BBD():
        OP_97(0xFE, 0x1F40, 0x0, 0x0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_5BBD)

    def lambda_5BD7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_5BD7)
    Sleep(90)

    def lambda_5BEB():
        OP_97(0xFE, 0x1F40, 0x0, 0x0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_5BEB)

    def lambda_5C05():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_5C05)
    Sleep(100)

    def lambda_5C19():
        OP_97(0xFE, 0x1F40, 0x0, 0x0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_5C19)

    def lambda_5C33():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_5C33)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x109, 1)
    WaitChrThread(0x105, 1)
    Fade(500)
    OP_68(-47890, 2500, -1790, 0)
    MoveCamera(48, 28, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(16180, 0)
    OP_0D()
    Sleep(1000)
    Jump("loc_5FDF")

    label("loc_5C8F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5E54")
    ClearChrFlags(0x12, 0x80)
    OP_78(0x6, 0x12)
    OP_49()
    SetChrPos(0x12, -58640, 0, 540, 90)
    OP_D5(0x12, 0x0, 0x15F90, 0x0, 0x0)
    ClearMapObjFlags(0x6, 0x4)
    SetMapObjFlags(0x6, 0x1000)
    SetMapObjFrame(0x6, "light", 0x0, 0x1)
    OP_74(0x6, 0x1E)
    OP_0D()
    OP_49()
    SetMapObjFlags(0x6, 0x1000)
    OP_74(0x6, 0x1E)
    OP_71(0x6, 0x79, 0xB4, 0x0, 0x20)
    Sleep(2200)

    def lambda_5D08():
        OP_95(0xFE, -37480, 0, 280, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_5D08)
    Sleep(1000)
    Sound(459, 0, 100, 0)
    Sleep(2500)
    Sound(492, 0, 100, 0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x12, 0x1)
    SetChrPos(0x12, -37890, 0, 4410, 270)
    OP_D5(0x12, 0x0, 0x41EB0, 0x0, 0x0)
    OP_71(0x6, 0x0, 0x0, 0x0, 0x0)
    OP_79(0x6)
    SetMapObjFlags(0x6, 0x2)
    OP_66(0x2, 0x1)
    Sleep(1)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrPos(0x101, -38290, 0, 910, 180)
    SetChrPos(0x102, -36930, 0, 0, 225)
    SetChrPos(0x104, -37690, 0, -2260, 315)
    SetChrPos(0x109, -40170, 0, -730, 90)
    SetChrPos(0x105, -39670, 0, -2360, 45)
    OP_68(-38040, 800, -240, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(19090, 0)
    Sleep(200)
    FadeToBright(500, 0)
    OP_0D()
    Jump("loc_5FDF")

    label("loc_5E54")

    ClearChrFlags(0x10, 0x80)
    ClearMapObjFlags(0x4, 0x4)
    ClearMapObjFlags(0x4, 0x2)
    OP_78(0x4, 0x10)
    SetMapObjFrame(0x4, "light", 0x0, 0x1)
    OP_49()
    SetChrPos(0x10, -58640, 0, 540, 90)
    OP_D5(0x10, 0x0, 0x15F90, 0x0, 0x0)
    SetMapObjFlags(0x4, 0x1000)
    OP_74(0x4, 0x1E)
    OP_49()
    SetMapObjFlags(0x4, 0x1000)
    OP_74(0x4, 0x1E)
    OP_71(0x4, 0x79, 0xB4, 0x0, 0x20)
    Sleep(1700)
    Sound(473, 0, 100, 0)
    Sleep(500)

    def lambda_5ECD():
        OP_95(0xFE, -37480, 0, 280, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_5ECD)
    Sleep(1000)
    Sound(467, 0, 100, 0)
    Sleep(3500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x10, 0x1)
    SetChrFlags(0x10, 0x80)
    SetMapObjFlags(0x4, 0x4)
    Sleep(1)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrPos(0x101, -30230, 0, 25140, 180)
    SetChrPos(0x102, -28930, 0, 24240, 270)
    SetChrPos(0x104, -29240, 0, 22400, 315)
    SetChrPos(0x105, -32100, 0, 22120, 45)
    SetChrPos(0x109, -31780, 0, 24260, 135)
    OP_68(-31080, 1300, 23140, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(18570, 0)
    Sleep(1)
    Sleep(200)
    FadeToBright(500, 0)
    OP_0D()

    label("loc_5FDF")


    #C0208
    ChrTalk(
        0x101,
        "#00000Fさて、タングラム門に着いたな。\x02",
    )

    CloseMessageWindow()

    #C0209
    ChrTalk(
        0x105,
        (
            "#12P#10300F確か、支援課への出向前に\x01",
            "ノエルが勤めていた門だっけ？\x02",
        )
    )

    CloseMessageWindow()

    #C0210
    ChrTalk(
        0x109,
        (
            "#10100Fうん、そうだよ。\x02\x03",

            "こちら側は共和国方面を\x01",
            "警備している国境門になるね。\x02",
        )
    )

    CloseMessageWindow()

    #C0211
    ChrTalk(
        0x102,
        (
            "#00100F今は新しくダグラス副司令という方が\x01",
            "指揮をとってらっしゃるのよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0212
    ChrTalk(
        0x104,
        (
            "#00300Fダグラスの兄さんか……\x01",
            "俺も会うのは久しぶりだぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0213
    ChrTalk(
        0x101,
        (
            "#00000F緊急度の高そうな\x01",
            "支援要請も入っていたし……\x02\x03",

            "さっそく２階の副司令室を\x01",
            "訪ねてみようか。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetScenarioFlags(0x1CB, 2)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_61B9")
    SetChrPos(0x0, -49550, 0, -310, 90)
    Jump("loc_61EE")

    label("loc_61B9")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_61DD")
    SetChrPos(0x0, -35570, 0, 510, 90)
    Jump("loc_61EE")

    label("loc_61DD")

    SetChrPos(0x0, -30310, 0, 21020, 180)

    label("loc_61EE")

    OP_69(0xFF, 0x0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_26_59EB end

    def Function_27_6204(): pass

    label("Function_27_6204")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00150.itc", 0x1F)
    LoadChrToIndex("chr/ch00350.itc", 0x20)
    LoadChrToIndex("chr/ch02950.itc", 0x21)
    LoadChrToIndex("chr/ch03050.itc", 0x22)
    LoadChrToIndex("chr/ch44900.itc", 0x28)
    LoadChrToIndex("chr/ch31200.itc", 0x29)
    LoadChrToIndex("chr/ch31300.itc", 0x2A)
    LoadChrToIndex("chr/ch31250.itc", 0x2B)
    LoadChrToIndex("chr/ch31350.itc", 0x2C)
    LoadChrToIndex("chr/ch31253.itc", 0x2D)
    LoadChrToIndex("chr/ch31353.itc", 0x2E)
    Call(0, 28)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00150.itc", 0x1F)
    LoadChrToIndex("chr/ch00350.itc", 0x20)
    LoadChrToIndex("chr/ch02950.itc", 0x21)
    LoadChrToIndex("chr/ch03050.itc", 0x22)
    LoadChrToIndex("chr/ch44900.itc", 0x28)
    LoadChrToIndex("chr/ch31200.itc", 0x29)
    LoadChrToIndex("chr/ch31300.itc", 0x2A)
    LoadChrToIndex("chr/ch31250.itc", 0x2B)
    LoadChrToIndex("chr/ch31350.itc", 0x2C)
    LoadChrToIndex("chr/ch31253.itc", 0x2D)
    LoadChrToIndex("chr/ch31353.itc", 0x2E)
    Call(0, 29)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00150.itc", 0x1F)
    LoadChrToIndex("chr/ch00350.itc", 0x20)
    LoadChrToIndex("chr/ch02950.itc", 0x21)
    LoadChrToIndex("chr/ch03050.itc", 0x22)
    LoadChrToIndex("chr/ch00053.itc", 0x23)
    LoadChrToIndex("chr/ch00153.itc", 0x24)
    LoadChrToIndex("chr/ch00353.itc", 0x25)
    LoadChrToIndex("chr/ch02953.itc", 0x26)
    LoadChrToIndex("chr/ch03053.itc", 0x27)
    LoadChrToIndex("chr/ch44900.itc", 0x28)
    LoadChrToIndex("chr/ch31200.itc", 0x29)
    LoadChrToIndex("chr/ch31300.itc", 0x2A)
    LoadChrToIndex("chr/ch31250.itc", 0x2B)
    LoadChrToIndex("chr/ch31350.itc", 0x2C)
    LoadChrToIndex("chr/ch31253.itc", 0x2D)
    LoadChrToIndex("chr/ch31353.itc", 0x2E)
    LoadChrToIndex("chr/ch44950.itc", 0x2F)
    Call(0, 30)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00150.itc", 0x1F)
    LoadChrToIndex("chr/ch00350.itc", 0x20)
    LoadChrToIndex("chr/ch02950.itc", 0x21)
    LoadChrToIndex("chr/ch03050.itc", 0x22)
    LoadChrToIndex("chr/ch00053.itc", 0x23)
    LoadChrToIndex("chr/ch00153.itc", 0x24)
    LoadChrToIndex("chr/ch00353.itc", 0x25)
    LoadChrToIndex("chr/ch02953.itc", 0x26)
    LoadChrToIndex("chr/ch03053.itc", 0x27)
    LoadChrToIndex("chr/ch44900.itc", 0x28)
    LoadChrToIndex("chr/ch31200.itc", 0x29)
    LoadChrToIndex("chr/ch31300.itc", 0x2A)
    LoadChrToIndex("chr/ch31250.itc", 0x2B)
    LoadChrToIndex("chr/ch31350.itc", 0x2C)
    LoadChrToIndex("chr/ch31253.itc", 0x2D)
    LoadChrToIndex("chr/ch31353.itc", 0x2E)
    LoadChrToIndex("chr/ch44950.itc", 0x2F)
    LoadChrToIndex("chr/ch44953.itc", 0x30)
    Call(0, 31)
    Return()

    # Function_27_6204 end

    def Function_28_638B(): pass

    label("Function_28_638B")

    EventBegin(0x0)
    OP_68(-22750, 3100, 20090, 0)
    MoveCamera(51, 19, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(19040, 0)
    ClearChrFlags(0x14, 0x80)
    ClearChrBattleFlags(0x14, 0x8000)
    SetChrChipByIndex(0x14, 0x28)
    SetChrSubChip(0x14, 0x0)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    SetChrChipByIndex(0x8, 0x29)
    SetChrSubChip(0x8, 0x0)
    OP_4B(0x8, 0xFF)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    SetChrChipByIndex(0x9, 0x2A)
    SetChrSubChip(0x9, 0x0)
    OP_4B(0x9, 0xFF)
    ClearChrFlags(0x15, 0x80)
    ClearChrBattleFlags(0x15, 0x8000)
    SetChrChipByIndex(0x15, 0x2A)
    SetChrSubChip(0x15, 0x0)
    OP_4B(0x15, 0xFF)
    ClearChrFlags(0x16, 0x80)
    ClearChrBattleFlags(0x16, 0x8000)
    SetChrChipByIndex(0x16, 0x29)
    SetChrSubChip(0x16, 0x0)
    OP_4B(0x16, 0xFF)
    ClearChrFlags(0x17, 0x80)
    ClearChrBattleFlags(0x17, 0x8000)
    SetChrChipByIndex(0x17, 0x2A)
    SetChrSubChip(0x17, 0x0)
    OP_4B(0x17, 0xFF)
    SetChrPos(0x14, -16500, 0, 21500, 270)
    SetChrPos(0x101, -22000, 0, 19000, 0)
    SetChrPos(0x102, -23000, 0, 17700, 0)
    SetChrPos(0x109, -20000, 0, 19000, 0)
    SetChrPos(0x104, -21000, 0, 17200, 0)
    SetChrPos(0x105, -19000, 0, 17700, 0)
    SetChrPos(0x8, -19500, 0, 26000, 180)
    SetChrPos(0x9, -20500, 0, 25500, 180)
    SetChrPos(0x15, -21500, 0, 25500, 180)
    SetChrPos(0x16, -23500, 0, 26000, 180)
    SetChrPos(0x17, -22500, 0, 25500, 180)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_68(-22750, 2100, 20090, 3000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)

    #C0214
    ChrTalk(
        0x14,
        (
            "#11Pそれではこれより、\x01",
            "《ダグラス式演習プログラム》を\x01",
            "開始する。\x02",
        )
    )

    CloseMessageWindow()

    #C0215
    ChrTalk(
        0x14,
        "#11P双方、準備はいいな？\x02",
    )

    CloseMessageWindow()

    #C0216
    ChrTalk(
        0x9,
        (
            "#5Pダイモン隊員以下５名、\x01",
            "準備完了しております。\x02",
        )
    )

    CloseMessageWindow()

    #C0217
    ChrTalk(
        0x101,
        "#12P#00000F特務支援課も、同じく。\x02",
    )

    CloseMessageWindow()

    #C0218
    ChrTalk(
        0x14,
        "#11Pよし。\x02",
    )

    CloseMessageWindow()

    #C0219
    ChrTalk(
        0x14,
        (
            "#11Pなお、これから行う戦闘では、\x01",
            "特務支援課チームの\x01",
            "アーツの使用を一切禁止する。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_66B2():
        TurnDirection(0xFE, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_66B2)
    Sleep(50)

    def lambda_66C2():
        TurnDirection(0xFE, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_66C2)
    Sleep(50)

    def lambda_66D2():
        TurnDirection(0xFE, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_66D2)
    Sleep(50)

    def lambda_66E2():
        TurnDirection(0xFE, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_66E2)
    Sleep(50)

    def lambda_66F2():
        TurnDirection(0xFE, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_66F2)
    Sleep(300)

    #C0220
    ChrTalk(
        0x101,
        (
            "#6P#00005Fちょ……\x01",
            "ちょっと待ってください！\x02\x03",

            "#00001Fこちらだけアーツなしなんて、\x01",
            "さすがに不利すぎるんじゃ……\x02",
        )
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0x104,
        (
            "#12P#00303Fなるほどな、これが噂の\x01",
            "《ダグラス式》の一つってわけか。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x14, 0x109, 500)
    Sleep(300)

    #C0222
    ChrTalk(
        0x14,
        "#11Pその通り。\x02",
    )

    CloseMessageWindow()

    #C0223
    ChrTalk(
        0x14,
        (
            "#11Pこの演習プログラムは、\x01",
            "様々な不利な条件を踏まえて\x01",
            "どう戦うかを試すものだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0224
    ChrTalk(
        0x14,
        (
            "#11Pそうすることで、\x01",
            "様々な状況に対応する力を\x01",
            "高めるのが狙いなのさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0x105,
        (
            "#12P#10304Fなるほど、『鬼』の名は\x01",
            "伊達じゃないってことだ。\x02\x03",

            "#10302Fフフ……\x01",
            "面白くなってきたじゃないか。\x02",
        )
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0x102,
        (
            "#12P#N#00106Fふぅ……\x01",
            "やるしかないみたいね。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    def lambda_691A():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_691A)
    Sleep(50)

    def lambda_692A():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_692A)
    Sleep(50)

    def lambda_693A():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_693A)
    Sleep(50)

    def lambda_694A():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_694A)
    Sleep(50)

    def lambda_695A():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_695A)
    Sleep(300)

    #C0227
    ChrTalk(
        0x14,
        "#11P話はついたようだな？\x02",
    )

    CloseMessageWindow()
    StopBGM(0xBB8)
    OP_93(0x14, 0x10E, 0x1F4)
    Sleep(300)

    #C0228
    ChrTalk(
        0x14,
        (
            "#4S#11Pそれでは……\x01",
            "全員、構えをとれ！\x02",
        )
    )

    CloseMessageWindow()

    #N0229
    NpcTalk(
        0x9,
        "隊員たち",
        "#5P#4S#Nはっ！！\x02",
    )

    CloseMessageWindow()
    OP_5A()
    SetCameraDistance(16200, 700)
    OP_68(-22750, 1500, 20090, 700)
    Fade(500)
    Sound(805, 0, 100, 0)
    Sound(531, 0, 100, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x104, 0x20)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0x21)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0x22)
    SetChrSubChip(0x105, 0x0)
    SetChrChipByIndex(0x8, 0x2B)
    SetChrSubChip(0x8, 0x0)
    SetChrChipByIndex(0x9, 0x2C)
    SetChrSubChip(0x9, 0x0)
    SetChrChipByIndex(0x15, 0x2C)
    SetChrSubChip(0x15, 0x0)
    SetChrChipByIndex(0x16, 0x2B)
    SetChrSubChip(0x16, 0x0)
    SetChrChipByIndex(0x17, 0x2C)
    SetChrSubChip(0x17, 0x0)
    OP_0D()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7451", 0)
    OP_6F(0x79)

    #C0230
    ChrTalk(
        0x101,
        (
            "#12P#00003F相手は戦闘のプロ、警備隊員……\x01",
            "しかもアーツは使えない、か。\x02\x03",

            "#00007Fみんな、油断するな！\x01",
            "絶対に活路は見出せるはずだ！\x02",
        )
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0x109,
        "#12P#10101Fりょ、了解です！\x02",
    )

    CloseMessageWindow()

    #C0232
    ChrTalk(
        0x14,
        "#5S#11P……始めッ！\x02",
    )

    CloseMessageWindow()
    Battle("BattleInfo_4B0", 0x0, 0x0, 0x0, 0xF, 0xFF)
    FadeToDark(0, 0, -1)
    Return()

    # Function_28_638B end

    def Function_29_6B3F(): pass

    label("Function_29_6B3F")

    EventBegin(0x0)
    OP_68(-22750, 2100, 20090, 0)
    MoveCamera(51, 19, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(19040, 0)
    SetChrPos(0x101, -22000, 0, 19000, 0)
    SetChrPos(0x102, -23000, 0, 17700, 0)
    SetChrPos(0x109, -20000, 0, 19000, 0)
    SetChrPos(0x104, -21000, 0, 17200, 0)
    SetChrPos(0x105, -19000, 0, 17700, 0)
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
    SetChrChipByIndex(0x8, 0x2D)
    SetChrSubChip(0x8, 0x3)
    SetChrChipByIndex(0x9, 0x2E)
    SetChrSubChip(0x9, 0x3)
    SetChrChipByIndex(0x15, 0x2E)
    SetChrSubChip(0x15, 0x3)
    SetChrChipByIndex(0x16, 0x2D)
    SetChrSubChip(0x16, 0x3)
    SetChrChipByIndex(0x17, 0x2E)
    SetChrSubChip(0x17, 0x3)
    FadeToBright(1000, 0)
    OP_0D()

    #C0233
    ChrTalk(
        0x14,
        "#11Pよぉし、そこまで！\x02",
    )

    CloseMessageWindow()

    #C0234
    ChrTalk(
        0x15,
        "いつつ……やるねえ。\x02",
    )

    CloseMessageWindow()

    #C0235
    ChrTalk(
        0x16,
        (
            "アーツの使用を\x01",
            "禁止されているのに……\x01",
            "さすがでありますッ！\x02",
        )
    )

    CloseMessageWindow()

    #C0236
    ChrTalk(
        0x105,
        "#12P#10302Fなんとかなったみたいだね。\x02",
    )

    CloseMessageWindow()

    #C0237
    ChrTalk(
        0x101,
        (
            "#12P#00001Fアーツが使えない状況は\x01",
            "戦闘中に何度か体験した\x01",
            "ことがあるけど……\x02\x03",

            "#00006F今回みたいに最初から\x01",
            "使えないっていうのは\x01",
            "なかなか大変だな。\x02",
        )
    )

    CloseMessageWindow()

    #C0238
    ChrTalk(
        0x102,
        (
            "#12P#N#00106F１年ちょっと前の、\x01",
            "リベールの導力停止現象のときも\x01",
            "こんな感じだったのかしら……\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0239
    ChrTalk(
        0x14,
        (
            "#11P《ダグラス式》第１段階は\x01",
            "危なげなく突破できたようだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0240
    ChrTalk(
        0x14,
        (
            "#11Pそれでは続けて、第２段階……\x01",
            "今度は戦技#4Rクラフト#の使用を\x01",
            "禁止した上で戦ってもらうぞ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_6EE6():
        TurnDirection(0xFE, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6EE6)
    Sleep(50)

    def lambda_6EF6():
        TurnDirection(0xFE, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_6EF6)
    Sleep(50)

    def lambda_6F06():
        TurnDirection(0xFE, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6F06)
    Sleep(50)

    def lambda_6F16():
        TurnDirection(0xFE, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_6F16)
    Sleep(50)

    def lambda_6F26():
        TurnDirection(0xFE, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_6F26)
    Sleep(300)

    #C0241
    ChrTalk(
        0x104,
        (
            "#12P#00306Fおいおい、まだやんのかよ！？\x02\x03",

            "#00301Fしかも戦技#4Rクラフト#を禁止だぁ！？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x14, 0x109, 500)
    Sleep(500)

    #C0242
    ChrTalk(
        0x14,
        (
            "#11Pなぁに、お前たちだったら\x01",
            "何とかなるだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0243
    ChrTalk(
        0x14,
        (
            "#11Pいい経験だと思って\x01",
            "一丁、やってみるといい。\x02",
        )
    )

    CloseMessageWindow()

    #C0244
    ChrTalk(
        0x109,
        (
            "#12P#10106F副司令……\x01",
            "キビしすぎです……\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x14, 0x10E, 0x1F4)
    Sleep(500)

    #C0245
    ChrTalk(
        0x14,
        (
            "#4S#11Pよし、警備隊員起立！\x01",
            "双方、戦闘態勢に入れ！\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0xBB8)

    def lambda_7079():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7079)
    Sleep(50)

    def lambda_7089():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_7089)
    Sleep(50)

    def lambda_7099():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7099)
    Sleep(50)

    def lambda_70A9():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_70A9)
    Sleep(50)

    def lambda_70B9():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_70B9)
    Sleep(300)
    Fade(500)
    Sound(802, 0, 100, 0)
    SetChrChipByIndex(0x8, 0x29)
    SetChrSubChip(0x8, 0x0)
    SetChrChipByIndex(0x9, 0x2A)
    SetChrSubChip(0x9, 0x0)
    SetChrChipByIndex(0x15, 0x2A)
    SetChrSubChip(0x15, 0x0)
    SetChrChipByIndex(0x16, 0x29)
    SetChrSubChip(0x16, 0x0)
    SetChrChipByIndex(0x17, 0x2A)
    SetChrSubChip(0x17, 0x0)
    OP_0D()

    #N0246
    NpcTalk(
        0x9,
        "隊員たち",
        "#4S#Nハッ！！\x02",
    )

    CloseMessageWindow()
    OP_5A()
    SetCameraDistance(16200, 700)
    OP_68(-22750, 1500, 20090, 700)
    Fade(500)
    Sound(805, 0, 100, 0)
    Sound(531, 0, 100, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x104, 0x20)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0x21)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0x22)
    SetChrSubChip(0x105, 0x0)
    SetChrChipByIndex(0x8, 0x2B)
    SetChrSubChip(0x8, 0x0)
    SetChrChipByIndex(0x9, 0x2C)
    SetChrSubChip(0x9, 0x0)
    SetChrChipByIndex(0x15, 0x2C)
    SetChrSubChip(0x15, 0x0)
    SetChrChipByIndex(0x16, 0x2B)
    SetChrSubChip(0x16, 0x0)
    SetChrChipByIndex(0x17, 0x2C)
    SetChrSubChip(0x17, 0x0)
    OP_0D()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7451", 0)
    OP_6F(0x79)

    #C0247
    ChrTalk(
        0x101,
        (
            "#12P#00003Fくっ……\x01",
            "戦技#4Rクラフト#を使えないのは\x01",
            "正直つらいけど……\x02\x03",

            "#00007Fなんとか、\x01",
            "アーツと通常攻撃を\x01",
            "駆使して戦うぞ！\x02",
        )
    )

    CloseMessageWindow()

    #C0248
    ChrTalk(
        0x102,
        "#12P#00101F……ええ！\x02",
    )

    CloseMessageWindow()

    #C0249
    ChrTalk(
        0x14,
        "#5S#11P……始めッ！\x02",
    )

    CloseMessageWindow()
    Battle("BattleInfo_4F4", 0x0, 0x0, 0x0, 0x10, 0xFF)
    FadeToDark(0, 0, -1)
    Return()

    # Function_29_6B3F end

    def Function_30_726C(): pass

    label("Function_30_726C")

    EventBegin(0x0)
    OP_68(-22750, 2100, 20090, 0)
    MoveCamera(51, 19, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(19040, 0)
    SetChrPos(0x101, -22000, 0, 19000, 0)
    SetChrPos(0x102, -23000, 0, 17700, 0)
    SetChrPos(0x109, -20000, 0, 19000, 0)
    SetChrPos(0x104, -21000, 0, 17200, 0)
    SetChrPos(0x105, -19000, 0, 17700, 0)
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
    SetChrChipByIndex(0x8, 0x2D)
    SetChrSubChip(0x8, 0x3)
    SetChrChipByIndex(0x9, 0x2E)
    SetChrSubChip(0x9, 0x3)
    SetChrChipByIndex(0x15, 0x2E)
    SetChrSubChip(0x15, 0x3)
    SetChrChipByIndex(0x16, 0x2D)
    SetChrSubChip(0x16, 0x3)
    SetChrChipByIndex(0x17, 0x2E)
    SetChrSubChip(0x17, 0x3)
    OP_0D()
    FadeToBright(1000, 0)
    OP_0D()

    #C0250
    ChrTalk(
        0x14,
        "#11Pうむ、そこまで！\x02",
    )

    CloseMessageWindow()

    #C0251
    ChrTalk(
        0x8,
        "くはー、マジかよ……\x02",
    )

    CloseMessageWindow()

    #C0252
    ChrTalk(
        0x17,
        "まさか、ここまでやるとはな。\x02",
    )

    CloseMessageWindow()

    #C0253
    ChrTalk(
        0x109,
        (
            "#12P#10106Fふぅ……\x01",
            "さすがに辛かったですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0254
    ChrTalk(
        0x101,
        (
            "#12P#00000Fああ……\x01",
            "戦技#4Rクラフト#がどれだけ戦いにおいて\x01",
            "重要だったか分かるな。\x02",
        )
    )

    CloseMessageWindow()

    #C0255
    ChrTalk(
        0x104,
        (
            "#12P#00304Fま、何とかなったようだし\x01",
            "いいじゃねぇか。\x02\x03",

            "#00301Fどーよ、これで文句ねえだろ！\x02",
        )
    )

    CloseMessageWindow()

    #C0256
    ChrTalk(
        0x14,
        (
            "#11Pフフ、なるほどな。\x01",
            "確かによく育ってる\x01",
            "みたいじゃないか。\x02",
        )
    )

    CloseMessageWindow()

    #C0257
    ChrTalk(
        0x14,
        (
            "#11Pそれならば……\x01",
            "《ダグラス式》第３段階に\x01",
            "移らせてもらおうか！\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0xFA0)
    OP_68(-22750, 1300, 20090, 1000)
    MoveCamera(51, 19, 0, 1000)
    OP_6E(510, 1000)
    SetCameraDistance(16320, 1000)
    Sound(809, 0, 70, 0)
    OP_9D(0x14, 0xFFFFACE0, 0x0, 0x5DFC, 0x7D0, 0x1388)
    TurnDirection(0x14, 0x101, 500)
    Sleep(500)
    WaitChrThread(0x14, 1)
    Fade(500)
    Sound(805, 0, 100, 0)
    SetChrChipByIndex(0x14, 0x2F)
    SetChrSubChip(0x14, 0x0)
    OP_0D()

    #C0258
    ChrTalk(
        0x14,
        (
            "#5S#5P警備隊員、起立！\x01",
            "最終訓練へと移行する！\x02",
        )
    )

    CloseMessageWindow()

    #N0259
    NpcTalk(
        0x9,
        "隊員たち",
        "#5S#Nはっ！\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    Sound(805, 0, 100, 0)
    Sound(531, 0, 100, 0)
    Sound(802, 0, 100, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x104, 0x20)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0x21)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0x22)
    SetChrSubChip(0x105, 0x0)
    SetChrChipByIndex(0x8, 0x2B)
    SetChrSubChip(0x8, 0x0)
    SetChrChipByIndex(0x9, 0x2C)
    SetChrSubChip(0x9, 0x0)
    SetChrChipByIndex(0x15, 0x2C)
    SetChrSubChip(0x15, 0x0)
    SetChrChipByIndex(0x16, 0x2B)
    SetChrSubChip(0x16, 0x0)
    SetChrChipByIndex(0x17, 0x2C)
    SetChrSubChip(0x17, 0x0)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0260
    ChrTalk(
        0x102,
        "#12P#00101Fこれは……！\x02",
    )

    CloseMessageWindow()

    #C0261
    ChrTalk(
        0x105,
        (
            "#12P#10302Fふぅん……\x01",
            "話に聞いていたとおり、\x01",
            "デキるみたいだね。\x02",
        )
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7452", 0)

    #C0262
    ChrTalk(
        0x101,
        (
            "#12P#00003F《鬼のダグラス》……\x01",
            "警備隊Ｎｏ．１の実力は\x01",
            "伊達じゃないはずだ。\x02\x03",

            "#00007F皆、一瞬たりとも\x01",
            "油断するんじゃないぞ！\x02",
        )
    )

    CloseMessageWindow()

    #C0263
    ChrTalk(
        0x14,
        (
            "#5Pはっはっは、\x01",
            "なかなかリーダーも\x01",
            "板についてるみたいだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0264
    ChrTalk(
        0x14,
        (
            "#5P……では、今までの演習の\x01",
            "総決算といこうじゃないか。\x02",
        )
    )

    CloseMessageWindow()

    #C0265
    ChrTalk(
        0x14,
        (
            "#5S#5Pこの俺を……\x01",
            "全力で打ち倒してみろ！\x02",
        )
    )

    CloseMessageWindow()

    #C0266
    ChrTalk(
        0x104,
        "#12P#00301Fへっ、望むところだぜ！\x02",
    )

    CloseMessageWindow()

    #C0267
    ChrTalk(
        0x109,
        "#12P#10107F行きます！\x02",
    )

    CloseMessageWindow()
    Battle("BattleInfo_538", 0x0, 0x0, 0x100, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    Return()

    # Function_30_726C end

    def Function_31_78B5(): pass

    label("Function_31_78B5")

    EventBegin(0x0)
    OP_68(-22750, 1500, 20090, 0)
    MoveCamera(49, 19, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(16320, 0)
    SetChrPos(0x101, -22000, 0, 19000, 0)
    SetChrPos(0x102, -23000, 0, 17700, 0)
    SetChrPos(0x109, -20000, 0, 19000, 0)
    SetChrPos(0x104, -21000, 0, 17200, 0)
    SetChrPos(0x105, -19000, 0, 17700, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7BAD")
    OP_2C(0x6F, 0x1)
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
    SetChrChipByIndex(0x8, 0x2D)
    SetChrSubChip(0x8, 0x3)
    SetChrChipByIndex(0x9, 0x2E)
    SetChrSubChip(0x9, 0x3)
    SetChrChipByIndex(0x15, 0x2E)
    SetChrSubChip(0x15, 0x3)
    SetChrChipByIndex(0x16, 0x2D)
    SetChrSubChip(0x16, 0x3)
    SetChrChipByIndex(0x17, 0x2E)
    SetChrSubChip(0x17, 0x3)
    SetChrChipByIndex(0x14, 0x30)
    SetChrSubChip(0x14, 0x3)
    FadeToBright(1000, 0)
    OP_0D()

    #C0268
    ChrTalk(
        0x101,
        "#12P#00002Fや、やった……！\x02",
    )

    CloseMessageWindow()

    #C0269
    ChrTalk(
        0x9,
        (
            "#5Pバ、バカな……\x01",
            "まさか副司令が……！？\x02",
        )
    )

    CloseMessageWindow()

    #C0270
    ChrTalk(
        0x14,
        (
            "#5Pフッ……なかなか\x01",
            "やるじゃないか。\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    Sound(802, 0, 100, 0)
    SetChrChipByIndex(0x14, 0x28)
    SetChrSubChip(0x14, 0x0)
    OP_0D()

    #C0271
    ChrTalk(
        0x104,
        (
            "#12P#00305F……ぜんぜん\x01",
            "効いてないみてえだな。\x02\x03",

            "#00306Fちっ、あいかわらず\x01",
            "タフというかなんというか。\x02",
        )
    )

    CloseMessageWindow()

    #C0272
    ChrTalk(
        0x14,
        "#5Pいや、効いてないことはないさ。\x02",
    )

    CloseMessageWindow()

    #C0273
    ChrTalk(
        0x14,
        (
            "#5P昔から、体力があるのが\x01",
            "唯一の取り柄ってだけさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0274
    ChrTalk(
        0x102,
        "#12P#00109Fご、ご謙遜を……\x02",
    )

    CloseMessageWindow()

    #C0275
    ChrTalk(
        0x109,
        "#12P#10106Fさすがです、副司令。\x02",
    )

    CloseMessageWindow()

    #C0276
    ChrTalk(
        0x105,
        "#12P#10306Fやれやれ、脱帽だね。\x02",
    )

    CloseMessageWindow()

    #C0277
    ChrTalk(
        0x14,
        (
            "#5Pいよぉし、ひとまず演習は\x01",
            "これで終わりだ。\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x6F, 0x1, 0x2)
    Jump("loc_7D96")

    label("loc_7BAD")

    SetChrChipByIndex(0x101, 0x23)
    SetChrSubChip(0x101, 0x3)
    SetChrChipByIndex(0x102, 0x24)
    SetChrSubChip(0x102, 0x3)
    SetChrChipByIndex(0x104, 0x25)
    SetChrSubChip(0x104, 0x3)
    SetChrChipByIndex(0x109, 0x26)
    SetChrSubChip(0x109, 0x3)
    SetChrChipByIndex(0x105, 0x27)
    SetChrSubChip(0x105, 0x3)
    FadeToBright(1000, 0)
    OP_0D()

    #C0278
    ChrTalk(
        0x101,
        (
            "#12P#00003Fくっ……！\x01",
            "届かなかったか……\x02",
        )
    )

    CloseMessageWindow()

    #C0279
    ChrTalk(
        0x102,
        (
            "#12P#N#00106Fアーツと戦技#4Rクラフト#があっても\x01",
            "勝てないなんて……\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0280
    ChrTalk(
        0x104,
        (
            "#12P#00301Fちっ、いい歳して\x01",
            "はりきりやがって。\x02",
        )
    )

    CloseMessageWindow()

    #C0281
    ChrTalk(
        0x14,
        (
            "#5Pフフ、俺もまだまだ\x01",
            "現役だってことだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0282
    ChrTalk(
        0x14,
        (
            "#5Pお前たちもなかなか\x01",
            "がんばっていたとは思うがな。\x02",
        )
    )

    CloseMessageWindow()

    #C0283
    ChrTalk(
        0x109,
        "#12P#10106F完敗ですね……\x02",
    )

    CloseMessageWindow()

    #C0284
    ChrTalk(
        0x105,
        (
            "#12P#10304Fさすがは警備隊の\x01",
            "副司令ってところかな。\x02",
        )
    )

    CloseMessageWindow()

    #C0285
    ChrTalk(
        0x14,
        (
            "#5Pいよぉし、ひとまず演習は\x01",
            "これで終わりだ。\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    Sound(805, 0, 100, 0)
    SetChrChipByIndex(0x14, 0x28)
    SetChrSubChip(0x14, 0x0)
    OP_0D()
    OP_29(0x6F, 0x1, 0x3)
    SetScenarioFlags(0x1, 0)

    label("loc_7D96")

    TurnDirection(0x14, 0x9, 500)
    Sleep(300)

    #C0286
    ChrTalk(
        0x14,
        (
            "#11P各員、持ち場にもどって\x01",
            "各々の仕事を再開するように。\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_7DFF")
    Sound(805, 0, 100, 0)
    Sound(802, 0, 100, 0)
    ClearScenarioFlags(0x1, 0)
    Jump("loc_7E05")

    label("loc_7DFF")

    Sound(802, 0, 100, 0)

    label("loc_7E05")

    SetChrChipByIndex(0x8, 0x29)
    SetChrSubChip(0x8, 0x0)
    SetChrChipByIndex(0x9, 0x2A)
    SetChrSubChip(0x9, 0x0)
    SetChrChipByIndex(0x15, 0x2A)
    SetChrSubChip(0x15, 0x0)
    SetChrChipByIndex(0x16, 0x29)
    SetChrSubChip(0x16, 0x0)
    SetChrChipByIndex(0x17, 0x2A)
    SetChrSubChip(0x17, 0x0)
    OP_0D()

    #N0287
    NpcTalk(
        0x9,
        "隊員たち",
        "#4S#Nハッ！\x02",
    )

    CloseMessageWindow()
    OP_5A()
    TurnDirection(0x14, 0x101, 500)
    Sleep(300)

    #C0288
    ChrTalk(
        0x14,
        (
            "#5Pお前たちも、\x01",
            "ご苦労だったな。\x02",
        )
    )

    CloseMessageWindow()

    #C0289
    ChrTalk(
        0x14,
        (
            "#5P立ち話もなんだし、\x01",
            "一旦司令室のほうに\x01",
            "戻るとしようか。\x02",
        )
    )

    CloseMessageWindow()

    #C0290
    ChrTalk(
        0x101,
        "#12P#00000Fは、はい。\x02",
    )

    CloseMessageWindow()
    OP_5A()
    FadeToBright(1000, 0)
    OP_0D()
    OP_32(0xFF, 0xFE, 0x0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetScenarioFlags(0x22, 0)
    NewScene("t2520", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_31_78B5 end

    def Function_32_7EFA(): pass

    label("Function_32_7EFA")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-41990, 1000, 10, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(20150, 0)
    SetChrPos(0x101, -49500, 0, 0, 90)
    SetChrPos(0x102, -49500, 0, -1200, 90)
    SetChrPos(0x104, -49500, 0, 1200, 90)
    SetChrPos(0x109, -50500, 0, 0, 90)
    SetChrPos(0x103, -50500, 0, -1200, 90)
    SetChrPos(0x105, -50500, 0, 1200, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)

    def lambda_7FB3():
        OP_95(0x101, -42000, 0, 0, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7FB3)
    Sleep(30)

    def lambda_7FD0():
        OP_95(0x102, -42500, 0, -1200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7FD0)
    Sleep(40)

    def lambda_7FED():
        OP_95(0x104, -42500, 0, 1200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_7FED)
    Sleep(800)

    def lambda_800A():
        OP_95(0x109, -44100, 0, 0, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_800A)
    Sleep(30)

    def lambda_8027():
        OP_95(0x103, -43800, 0, -1200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_8027)
    Sleep(10)

    def lambda_8044():
        OP_95(0x105, -43800, 0, 1200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_8044)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x109, 1)
    WaitChrThread(0x105, 1)

    #C0291
    ChrTalk(
        0x101,
        (
            "#00000Fさてと……\x01",
            "黒い運搬車は来ているかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0292
    ChrTalk(
        0x103,
        "#00200F屋外には見当たりませんが……\x02",
    )

    CloseMessageWindow()

    #C0293
    ChrTalk(
        0x102,
        (
            "#00103Fもしかしたら、既に中で\x01",
            "出国手続きをしているのかも\x01",
            "しれないわね……\x02",
        )
    )

    CloseMessageWindow()

    #C0294
    ChrTalk(
        0x105,
        (
            "#10300Fその可能性はありそうだね。\x01",
            "来るのに少し時間がかかっちゃったし……\x02",
        )
    )

    CloseMessageWindow()

    #C0295
    ChrTalk(
        0x109,
        "#10101Fい、急いで確認してみましょう！\x02",
    )

    CloseMessageWindow()

    #C0296
    ChrTalk(
        0x104,
        "#00306Fやれやれ、間に合えばいいが……\x02",
    )

    CloseMessageWindow()

    def lambda_81CE():
        OP_95(0x101, -25000, 0, 0, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_81CE)
    Sleep(30)

    def lambda_81EB():
        OP_95(0x102, -25500, 0, -1200, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_81EB)
    Sleep(40)

    def lambda_8208():
        OP_95(0x104, -25500, 0, 1200, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_8208)
    Sleep(30)

    def lambda_8225():
        OP_95(0x109, -25100, 0, 0, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_8225)
    Sleep(30)

    def lambda_8242():
        OP_95(0x103, -25800, 0, -1200, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_8242)
    Sleep(10)

    def lambda_825F():
        OP_95(0x105, -25800, 0, 1200, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_825F)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_29(0x93, 0x1, 0x3)
    SetScenarioFlags(0x22, 1)
    NewScene("t2510", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_32_7EFA end

    def Function_33_82A0(): pass

    label("Function_33_82A0")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-31240, 1000, 24480, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(20150, 0)
    SetChrPos(0x101, -31060, 0, 25800, 180)
    SetChrPos(0x102, -29790, 0, 24750, 270)
    SetChrPos(0x104, -29830, 0, 23100, 270)
    SetChrPos(0x109, -31200, 0, 21720, 0)
    SetChrPos(0x103, -32330, 0, 23100, 90)
    SetChrPos(0x105, -32330, 0, 24750, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()

    #C0297
    ChrTalk(
        0x101,
        (
            "#00000Fさてと……\x01",
            "黒い運搬車は来ているかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0298
    ChrTalk(
        0x103,
        "#00200F屋外には見当たりませんが……\x02",
    )

    CloseMessageWindow()

    #C0299
    ChrTalk(
        0x102,
        (
            "#00103Fもしかしたら、既に中で\x01",
            "出国手続きをしているのかも\x01",
            "しれないわね……\x02",
        )
    )

    CloseMessageWindow()

    #C0300
    ChrTalk(
        0x105,
        (
            "#10300Fその可能性はありそうだね。\x01",
            "バスの待ち時間で少し\x01",
            "手間取っちゃったし……\x02",
        )
    )

    CloseMessageWindow()

    #C0301
    ChrTalk(
        0x109,
        "#10101Fい、急いで確認してみましょう！\x02",
    )

    CloseMessageWindow()

    #C0302
    ChrTalk(
        0x104,
        "#00306Fやれやれ、間に合えばいいが……\x02",
    )

    CloseMessageWindow()

    def lambda_84B6():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_84B6)
    Sleep(30)

    def lambda_84C6():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_84C6)
    Sleep(40)

    def lambda_84D6():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_84D6)
    Sleep(30)

    def lambda_84E6():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_84E6)
    Sleep(30)

    def lambda_84F6():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_84F6)
    Sleep(10)

    def lambda_8506():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_8506)
    WaitChrThread(0x109, 2)

    def lambda_8517():
        OP_95(0x109, -25100, 0, 0, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_8517)
    WaitChrThread(0x104, 2)

    def lambda_8535():
        OP_95(0x104, -25500, 0, 1200, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_8535)
    WaitChrThread(0x103, 2)

    def lambda_8553():
        OP_95(0x103, -25800, 0, -1200, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_8553)
    WaitChrThread(0x102, 2)

    def lambda_8571():
        OP_95(0x102, -25500, 0, -1200, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8571)
    WaitChrThread(0x105, 2)

    def lambda_858F():
        OP_95(0x105, -25800, 0, 1200, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_858F)
    WaitChrThread(0x101, 2)

    def lambda_85AD():
        OP_95(0x101, -25000, 0, 0, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_85AD)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_29(0x93, 0x1, 0x4)
    SetScenarioFlags(0x22, 1)
    NewScene("t2510", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_33_82A0 end

    def Function_34_85EE(): pass

    label("Function_34_85EE")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearMapFlags(0x8000000)
    OP_68(-41990, 1000, 10, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(20150, 0)
    LoadChrToIndex("chr/ch45200.itc", 0x1E)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    SetChrFlags(0x4, 0x80)
    SetChrFlags(0x5, 0x80)
    SetChrPos(0x101, -35000, 0, 0, 0)
    SetChrPos(0x102, -35000, 0, 0, 0)
    SetChrFlags(0x9, 0x80)
    Sound(459, 0, 100, 0)
    OP_74(0x6, 0x1E)
    OP_71(0x6, 0x79, 0xB4, 0x1, 0x20)

    def lambda_86A7():
        OP_96(0x12, 0xFFFF5BF0, 0x0, 0x0, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_86A7)
    FadeToBright(1000, 0)
    OP_0D()
    Sound(492, 0, 100, 0)
    WaitChrThread(0x12, 1)
    OP_71(0x6, 0x5B, 0x78, 0x1, 0x8)
    StopSound(459, 1000, 90)
    Sleep(1000)

    #C0303
    ChrTalk(
        0x101,
        "#00005Fあれは……！\x02",
    )

    CloseMessageWindow()

    #C0304
    ChrTalk(
        0x102,
        "#00101Fどうやら、見つかったみたいね。\x02",
    )

    CloseMessageWindow()
    Fade(500)
    OP_68(-24420, 1000, -11490, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(21210, 0)
    ClearChrFlags(0x0, 0x80)
    ClearChrFlags(0x1, 0x80)
    ClearChrFlags(0x2, 0x80)
    ClearChrFlags(0x3, 0x80)
    ClearChrFlags(0x4, 0x80)
    ClearChrFlags(0x5, 0x80)
    SetChrPos(0x101, -32250, 0, -8230, 135)
    SetChrPos(0x102, -31980, 0, -6900, 135)
    SetChrPos(0x103, -31690, 0, -9430, 135)
    SetChrPos(0x104, -33590, 0, -6950, 135)
    SetChrPos(0x105, -33500, 0, -5480, 135)
    SetChrPos(0x109, -33500, 0, -7110, 135)
    SetChrChipByIndex(0x18, 0x1E)
    SetChrSubChip(0x18, 0x0)
    ClearChrFlags(0x18, 0x80)
    SetChrFlags(0x18, 0x4)
    SetChrPos(0x18, -24460, 0, -11450, 90)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_88BC")

    #C0305
    ChrTalk(
        0x18,
        (
            "クク……\x01",
            "ここまでくれば安心でしょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0306
    ChrTalk(
        0x18,
        (
            "あとはこの医療物資を\x01",
            "共和国方面で売りさばけばいい。\x02",
        )
    )

    CloseMessageWindow()

    #C0307
    ChrTalk(
        0x18,
        (
            "レミフェリア製の医療物資……\x01",
            "そこそこいいミラになるでしょう。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8984")

    label("loc_88BC")


    #N0308
    NpcTalk(
        0x18,
        "商人風の男",
        (
            "クク……\x01",
            "ここまでくれば安心でしょう。\x02",
        )
    )

    CloseMessageWindow()

    #N0309
    NpcTalk(
        0x18,
        "商人風の男",
        (
            "あとはこの医療物資を\x01",
            "共和国方面で売りさばけばいい。\x02",
        )
    )

    CloseMessageWindow()

    #N0310
    NpcTalk(
        0x18,
        "商人風の男",
        (
            "レミフェリア製の医療物資……\x01",
            "そこそこいいミラになるでしょう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8984")


    #C0311
    ChrTalk(
        0x101,
        "#00007F──そうはさせない！\x02",
    )

    CloseMessageWindow()
    OP_63(0x18, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_68(-25430, 1000, -10970, 3000)
    MoveCamera(42, 28, 0, 3000)
    OP_6E(510, 3000)
    SetCameraDistance(21210, 3000)

    def lambda_89F0():
        OP_95(0x101, -26500, 0, -11450, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_89F0)

    def lambda_8A0A():
        OP_95(0x102, -26230, 0, -10150, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8A0A)

    def lambda_8A24():
        OP_95(0x103, -26500, 0, -12750, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_8A24)

    def lambda_8A3E():
        OP_95(0x104, -27950, 0, -11450, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_8A3E)

    def lambda_8A58():
        OP_95(0x105, -27550, 0, -10200, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_8A58)

    def lambda_8A72():
        OP_95(0x109, -27550, 0, -12750, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_8A72)
    WaitChrThread(0x101, 1)

    def lambda_8A90():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_8A90)
    WaitChrThread(0x102, 1)

    def lambda_8AA1():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_8AA1)
    WaitChrThread(0x103, 1)

    def lambda_8AB2():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_8AB2)
    WaitChrThread(0x104, 1)

    def lambda_8AC3():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_8AC3)
    WaitChrThread(0x105, 1)

    def lambda_8AD4():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_8AD4)
    WaitChrThread(0x109, 1)

    def lambda_8AE5():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_8AE5)
    OP_93(0x18, 0x10E, 0x1F4)
    WaitChrThread(0x109, 2)
    OP_6F(0x79)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_8E2B")

    #C0312
    ChrTalk(
        0x18,
        "貴様たちは……！！\x02",
    )

    CloseMessageWindow()

    #C0313
    ChrTalk(
        0x101,
        (
            "#00001Fミンネス……\x01",
            "うすうす気づいていたが、\x01",
            "貴方だったんだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0314
    ChrTalk(
        0x102,
        (
            "#00103F貴方には、空港で医療物資を\x01",
            "騙し取った容疑がかかっています。\x02\x03",

            "#00101F申し訳ありませんが、\x01",
            "積荷を見せていただいても……？\x02",
        )
    )

    CloseMessageWindow()

    #C0315
    ChrTalk(
        0x18,
        (
            "……フン、急いでいたせいで\x01",
            "仕事が粗すぎましたか。\x02",
        )
    )

    CloseMessageWindow()

    #C0316
    ChrTalk(
        0x105,
        (
            "#10302Fフフ、確かに。\x01",
            "アルモリカ村で会った頃に比べて\x01",
            "随分精彩を欠いた手口だよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0317
    ChrTalk(
        0x18,
        (
            "……こっちは貴様たちのせいで\x01",
            "アルモリカ村での仕事に失敗し、\x01",
            "指名手配までされる身の上……\x02",
        )
    )

    CloseMessageWindow()

    #C0318
    ChrTalk(
        0x18,
        (
            "このくらいの\x01",
            "小遣い稼ぎでもしなければ\x01",
            "商売上がったりなのですよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0319
    ChrTalk(
        0x104,
        (
            "#00303Fハッ……もうひとつ\x01",
            "でけえ理由があるだろうが。\x02\x03",

            "#00301Fあんたが《赤い星座》の\x01",
            "御用商人か資金調達係なのは\x01",
            "分かってるからな。\x02\x03",

            "連中がクロスベルであんなことを\x01",
            "やらかしちまったから、\x01",
            "留まってられなくなったんだろう？\x02",
        )
    )

    CloseMessageWindow()

    #C0320
    ChrTalk(
        0x18,
        "……フフ、ご想像にお任せしますよ。\x02",
    )

    CloseMessageWindow()
    OP_29(0x93, 0x1, 0x5)
    Jump("loc_9171")

    label("loc_8E2B")


    #N0321
    NpcTalk(
        0x18,
        "商人風の男",
        "おや、あなた方は……？\x02",
    )

    CloseMessageWindow()

    #C0322
    ChrTalk(
        0x101,
        (
            "#00001F俺たちは、クロスベル警察、\x01",
            "特務支援課の者です。\x02\x03",

            "申し訳ありませんが……\x01",
            "名前と身分を\x01",
            "明かしていただけますか？\x02",
        )
    )

    CloseMessageWindow()

    #N0323
    NpcTalk(
        0x18,
        "商人風の男",
        (
            "ふむ……警察の方でしたか。\x01",
            "これは失礼致しました。\x02",
        )
    )

    CloseMessageWindow()

    #N0324
    NpcTalk(
        0x18,
        "商人風の男",
        (
            "私の名はミンネス……\x01",
            "帝国出身のしがない商人です。\x02",
        )
    )

    CloseMessageWindow()

    #C0325
    ChrTalk(
        0x18,
        (
            "今から、共和国の方へ\x01",
            "取引きに出かける所なのですが……\x01",
            "私に何かご用でしょうか？\x02",
        )
    )

    CloseMessageWindow()

    #C0326
    ChrTalk(
        0x104,
        "#00306Fやれやれ、シレっとしやがって。\x02",
    )

    CloseMessageWindow()

    #C0327
    ChrTalk(
        0x102,
        (
            "#00103F貴方には、空港で医療物資を\x01",
            "騙し取った容疑がかかっています。\x02\x03",

            "#00101F申し訳ありませんが、\x01",
            "積荷を見せていただいても……？\x02",
        )
    )

    CloseMessageWindow()

    #C0328
    ChrTalk(
        0x18,
        (
            "ふむ、確かにこの運搬車には\x01",
            "医療物資を積んでいますが……\x02",
        )
    )

    CloseMessageWindow()

    #C0329
    ChrTalk(
        0x18,
        "これはもともと私の荷物ですよ？\x02",
    )

    CloseMessageWindow()

    #C0330
    ChrTalk(
        0x18,
        (
            "それとも、私が騙し取ったいう\x01",
            "証拠でもおありですかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0331
    ChrTalk(
        0x105,
        (
            "#10304Fフフ、シラを切れるとでも\x01",
            "思ってるのかな。\x02\x03",

            "#10302Fリカルドさんに確認をとれば\x01",
            "流石に言い逃れできないと思うけど。\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x93, 0x1, 0x6)

    label("loc_9171")


    #C0332
    ChrTalk(
        0x103,
        (
            "#00203F……時間が惜しいです。\x01",
            "強制的に連行してしまいましょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0333
    ChrTalk(
        0x101,
        "#00001Fああ……そうするしかなさそうだ。\x02",
    )

    CloseMessageWindow()

    #C0334
    ChrTalk(
        0x18,
        (
            "おお、怖い怖い。\x01",
            "なんて野蛮な連中だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0335
    ChrTalk(
        0x18,
        (
            "それならば……\x01",
            "私も逃げるしかなさそうですね。\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0x7D0)
    Sound(464, 0, 100, 0)
    OP_74(0xB, 0x1E)
    OP_71(0xB, 0x1, 0x3C, 0x1, 0x8)
    OP_93(0x18, 0x10E, 0x1F4)
    Sleep(500)

    def lambda_926A():
        OP_95(0x18, -23800, 0, -11450, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_926A)
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
    WaitChrThread(0x18, 1)
    Sound(463, 0, 100, 0)

    def lambda_9324():
        OP_A7(0x18, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_9324)
    OP_95(0x18, -23000, 600, -11450, 2000, 0x0)

    #C0336
    ChrTalk(
        0x101,
        "#00007F#11Aま、待てッ……！\x02",
    )
    #Auto

    Sound(470, 0, 70, 0)
    OP_74(0xB, 0x3C)
    OP_71(0xB, 0x3C, 0x5A, 0x0, 0x0)
    Sleep(1000)
    Sound(493, 0, 100, 0)
    Sound(494, 0, 100, 0)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7507", 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x1FB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_74(0xB, 0x1E)
    OP_71(0xB, 0x79, 0xB4, 0x1, 0x20)
    BeginChrThread(0x13, 1, 0, 35)
    Sleep(800)
    OP_57(0x0)
    OP_5A()

    def lambda_93BB():
        OP_95(0x101, -23500, 0, -11450, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_93BB)

    def lambda_93D5():
        OP_95(0x102, -23230, 0, -10150, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_93D5)

    def lambda_93EF():
        OP_95(0x103, -23500, 0, -12750, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_93EF)

    def lambda_9409():
        OP_95(0x104, -24950, 0, -11450, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_9409)

    def lambda_9423():
        OP_95(0x105, -24550, 0, -10200, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_9423)

    def lambda_943D():
        OP_95(0x109, -24550, 0, -12750, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_943D)
    WaitChrThread(0x109, 1)

    def lambda_945B():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_945B)

    def lambda_9468():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_9468)

    def lambda_9475():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_9475)

    def lambda_9482():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_9482)

    def lambda_948F():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_948F)

    def lambda_949C():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_949C)
    Sleep(500)

    #C0337
    ChrTalk(
        0x109,
        (
            "#10107Fロイドさん、\x01",
            "こちらも導力車で追いましょう！\x02",
        )
    )

    CloseMessageWindow()

    #C0338
    ChrTalk(
        0x101,
        "#00001Fああ……！\x02",
    )

    CloseMessageWindow()

    def lambda_94FB():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_94FB)
    Sleep(50)

    def lambda_950B():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_950B)
    Sleep(50)

    def lambda_951B():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_951B)
    Sleep(50)

    def lambda_952B():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_952B)
    Sleep(50)

    def lambda_953B():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_953B)
    Sleep(50)

    def lambda_954B():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_954B)
    WaitChrThread(0x101, 1)

    def lambda_955C():
        OP_95(0x101, -32250, 0, -8230, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_955C)
    WaitChrThread(0x102, 1)

    def lambda_957A():
        OP_95(0x102, -31980, 0, -6900, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_957A)
    WaitChrThread(0x103, 1)

    def lambda_9598():
        OP_95(0x103, -31690, 0, -9430, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_9598)
    WaitChrThread(0x104, 1)

    def lambda_95B6():
        OP_95(0x104, -33590, 0, -6950, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_95B6)
    WaitChrThread(0x105, 1)

    def lambda_95D4():
        OP_95(0x105, -33500, 0, -5480, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_95D4)
    WaitChrThread(0x109, 1)

    def lambda_95F2():
        OP_95(0x109, -33500, 0, -9430, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_95F2)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    ClearChrFlags(0x9, 0x80)
    SetScenarioFlags(0x22, 0)
    NewScene("t2510", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_34_85EE end

    def Function_35_9627(): pass

    label("Function_35_9627")

    SetChrPos(0xFE, -22290, 0, -12240, 0)
    OP_9F(0x0, 0xFE)
    OP_9F(0x1, -24290, 0, -4000)
    OP_9F(0x1, -23290, 0, -2000)
    OP_9F(0x1, -21000, 0, 0)
    OP_9F(0x1, -18290, 0, 0)
    OP_9F(0x1, 290, 0, 0)
    OP_9F(0x2, 0xFE, 6500, 0x6)
    Return()

    # Function_35_9627 end

    def Function_36_968C(): pass

    label("Function_36_968C")

    EventBegin(0x2)
    ClearMapFlags(0x20)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0339
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "カルバード共和国方面国境\x01",
            "    『タングラム門』\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    EventEnd(0x3)
    Return()

    # Function_36_968C end

    SaveToFile()

Try(main)
