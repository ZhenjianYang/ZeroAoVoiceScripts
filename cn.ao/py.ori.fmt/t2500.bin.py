from ScenarioHelper import *

def main():
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
        "诺威队员",               # 1
        "戴蒙队员",               # 2
        "加利森队员",             # 3
        "巴雷尔队员",             # 4
        "琪露露",                 # 5
        "尤利",                   # 6
        "塞克斯",                 # 7
        "瑞吉",                   # 8
        "巴士",                   # 9
        "列车",                   # 10
        "特别任务支援车辆",       # 11
        "运输车",                 # 12
        "道格拉斯副司令",         # 13
        "奥利弗队员",             # 14
        "杰克队员",               # 15
        "阿雷库瑟队员",           # 16
        "敏涅斯",                 # 17
        "bt2500",                 # 18
        "bt2500",                 # 19
        "bt2500",                 # 20
        "东克洛斯贝尔街道",       # 21
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

    PlaceName(-71.0, 0.0, -8.0, 0x0000, 0x0000, "东克洛斯贝尔街道")
    PlaceName(-5.25, 0.0, -2.5, 0x0000, 0x0052, "")
    PlaceName(-30.950000762939453, 0.0, 28.100000381469727, 0x0000, 0x0055, "")

    ChipFrameInfo(1552, 0)                                       # 0

    ScpFunction((
        "Function_0_610",          # 00, 0
        "Function_1_6C8",          # 01, 1
        "Function_2_721",          # 02, 2
        "Function_3_D7D",          # 03, 3
        "Function_4_106D",         # 04, 4
        "Function_5_11A8",         # 05, 5
        "Function_6_1296",         # 06, 6
        "Function_7_13C3",         # 07, 7
        "Function_8_1414",         # 08, 8
        "Function_9_14A8",         # 09, 9
        "Function_10_1FF4",        # 0A, 10
        "Function_11_2A75",        # 0B, 11
        "Function_12_2B8E",        # 0C, 12
        "Function_13_2CAF",        # 0D, 13
        "Function_14_2D9F",        # 0E, 14
        "Function_15_2E92",        # 0F, 15
        "Function_16_3772",        # 10, 16
        "Function_17_4112",        # 11, 17
        "Function_18_443F",        # 12, 18
        "Function_19_4479",        # 13, 19
        "Function_20_4612",        # 14, 20
        "Function_21_50F7",        # 15, 21
        "Function_22_5107",        # 16, 22
        "Function_23_511A",        # 17, 23
        "Function_24_512D",        # 18, 24
        "Function_25_5140",        # 19, 25
        "Function_26_5153",        # 1A, 26
        "Function_27_5920",        # 1B, 27
        "Function_28_5AA7",        # 1C, 28
        "Function_29_61D5",        # 1D, 29
        "Function_30_6890",        # 1E, 30
        "Function_31_6E49",        # 1F, 31
        "Function_32_73EE",        # 20, 32
        "Function_33_774E",        # 21, 33
        "Function_34_7A5A",        # 22, 34
        "Function_35_8923",        # 23, 35
        "Function_36_8988",        # 24, 36
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1ED, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_115F")
    Sound(14, 0, 100, 0)
    OP_74(0x5, 0x1E)
    OP_71(0x5, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('弹簧跑鞋', 1)"), scpexpr(EXPR_END)), "loc_10F0")
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
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1ED, 7)
    OP_E0(0x5, 0x0)
    Jump("loc_115A")

    label("loc_10F0")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0002
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, 0x646),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多，",
            scpstr(SCPSTR_CODE_ITEM, 0x646),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x5, 0x1E, 0x0, 0x0, 0x0)

    label("loc_115A")

    Jump("loc_119C")

    label("loc_115F")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0003
    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "宝箱里什么都没有。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_119C")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_106D end

    def Function_5_11A8(): pass

    label("Function_5_11A8")

    EventBegin(0x2)
    SetMapFlags(0x8000000)

    #A0004
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1K有一个巴士车站。\x01",
            "要乘坐巴士吗？\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "克洛斯贝尔市·东出口\x01",      # 0
            "阿尔摩利卡村\x01",              # 1
            "停靠站（三岔路）\x01",          # 2
            "放弃\x01",                      # 3
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1249")
    Call(0, 6)
    ClearMapFlags(0x8000000)
    NewScene("r0000", 0, 0, 0)
    IdleLoop()
    Jump("loc_128E")

    label("loc_1249")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_126E")
    Call(0, 6)
    ClearMapFlags(0x8000000)
    NewScene("t0000", 0, 0, 0)
    IdleLoop()
    Jump("loc_128E")

    label("loc_126E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_128E")
    Call(0, 6)
    ClearMapFlags(0x8000000)
    NewScene("r0030", 0, 0, 0)
    IdleLoop()

    label("loc_128E")

    ClearMapFlags(0x8000000)
    EventEnd(0x3)
    Return()

    # Function_5_11A8 end

    def Function_6_1296(): pass

    label("Function_6_1296")

    ClearMapFlags(0x1)
    SetEventSkip(0x0, "loc_13BF")
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

    def lambda_1376():
        OP_98(0xFE, 0x0, 0x0, 0x2EE0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_1376)
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

    label("loc_13BF")

    SetScenarioFlags(0x3E, 0)
    Return()

    # Function_6_1296 end

    def Function_7_13C3(): pass

    label("Function_7_13C3")

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

    # Function_7_13C3 end

    def Function_8_1414(): pass

    label("Function_8_1414")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(0, 0, -1)
    Sleep(100)
    Sound(459, 0, 100, 0)
    Sleep(2000)
    StopSound(459, 1000, 100)
    Sound(492, 0, 70, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 2)), scpexpr(EXPR_END)), "loc_146F")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1464")
    Sound(2502, 255, 100, 0)    #voice#Noel
    Jump("loc_146A")

    label("loc_1464")

    Sound(2503, 255, 100, 0)    #voice#Noel

    label("loc_146A")

    Jump("loc_1493")

    label("loc_146F")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_148D")
    Sound(3347, 255, 100, 0)    #voice#Lloyd
    Jump("loc_1493")

    label("loc_148D")

    Sound(3348, 255, 100, 0)    #voice#Lloyd

    label("loc_1493")

    Sleep(500)
    FadeToBright(500, 0)
    OP_0D()
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_8_1414 end

    def Function_9_14A8(): pass

    label("Function_9_14A8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_166A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15F3")
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #N0005
    NpcTalk(
        0x8,
        "士兵诺威",
        (
            "你、你们是……！？\x01",
            "……唔，说起来，现在好像已经\x01",
            "没必要再逮捕你们了。\x02",
        )
    )

    CloseMessageWindow()

    #N0006
    NpcTalk(
        0x8,
        "士兵诺威",
        (
            "唉，如今想想，我们国防军\x01",
            "到底在做什么呢？\x02",
        )
    )

    CloseMessageWindow()

    #N0007
    NpcTalk(
        0x8,
        "士兵诺威",
        (
            "我当时还很高兴，\x01",
            "以为一直不得志的警备队\x01",
            "终于也有出头之日了……\x02",
        )
    )

    CloseMessageWindow()

    #N0008
    NpcTalk(
        0x8,
        "士兵诺威",
        (
            "总觉得这段时间就像是\x01",
            "做了一场很长很长的梦。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1665")

    label("loc_15F3")


    #N0009
    NpcTalk(
        0x8,
        "士兵诺威",
        (
            "……如今想想，我们国防军\x01",
            "到底在做什么呢？\x02",
        )
    )

    CloseMessageWindow()

    #N0010
    NpcTalk(
        0x8,
        "士兵诺威",
        (
            "总觉得这段时间就像是\x01",
            "做了一场很长很长的梦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1665")

    Jump("loc_1FF0")

    label("loc_166A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_17B5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1740")

    #C0011
    ChrTalk(
        0x8,
        (
            "被送进乌尔斯拉医院的队员们，\x01",
            "情况都不容乐观。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x8,
        (
            "……但相比之下，他们的运气还算不错了。\x01",
            "想想那些牺牲在山道上的同伴们……\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x8,
        (
            "我平时一向性情温和……\x01",
            "但这次真是无法抑制心中的怒火。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_17B0")

    label("loc_1740")


    #C0014
    ChrTalk(
        0x8,
        (
            "我平时一向性情温和……\x01",
            "但这次真是无法抑制心中的怒火。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x8,
        (
            "赤色星座……我总有一天\x01",
            "会让你们为此付出代价的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17B0")

    Jump("loc_1FF0")

    label("loc_17B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1904")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1881")

    #C0016
    ChrTalk(
        0x8,
        (
            "大家当时都认为昨天那起事故\x01",
            "会造成很大的影响。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x8,
        (
            "毕竟要是没能及时修复，\x01",
            "帝国和共和国一定会强行介入，\x01",
            "居民投票活动多半也就无法举行了。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x8,
        "真该感谢负责修复铁道的部队啊。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_18FF")

    label("loc_1881")


    #C0019
    ChrTalk(
        0x8,
        (
            "要是没能及时修复铁道，\x01",
            "帝国和共和国一定会强行介入，\x01",
            "居民投票活动多半也就无法举行了。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x8,
        "真该感谢负责修复铁道的部队啊。\x02",
    )

    CloseMessageWindow()

    label("loc_18FF")

    Jump("loc_1FF0")

    label("loc_1904")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1A36")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19BE")

    #C0021
    ChrTalk(
        0x8,
        (
            "克洛斯贝尔自治州\x01",
            "要向帝国和共和国\x01",
            "缴纳合计１０％的税收。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x8,
        (
            "如果独立之后\x01",
            "能废除那项制度，\x01",
            "就可以省下不少预算。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x8,
        (
            "到时候，应该首先\x01",
            "就会强化警备队吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1A31")

    label("loc_19BE")


    #C0024
    ChrTalk(
        0x8,
        (
            "如果独立之后能废除那个\x01",
            "缴纳合计１０％税收的制度，\x01",
            "就能省下不少预算。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x8,
        (
            "到时候，应该首先\x01",
            "就会强化警备队吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A31")

    Jump("loc_1FF0")

    label("loc_1A36")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1B91")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B0F")

    #C0026
    ChrTalk(
        0x8,
        (
            "从地理位置上来看，\x01",
            "克洛斯贝尔自治州被\x01",
            "帝国和共和国夹在中间。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x8,
        (
            "也就是说，那项独立提案\x01",
            "是在两股与我们对立势力的\x01",
            "正中央发表的。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x8,
        (
            "考虑到这一点，\x01",
            "不得不说市长这次的\x01",
            "举动相当大胆啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1B8C")

    label("loc_1B0F")


    #C0029
    ChrTalk(
        0x8,
        (
            "通商会议上的那项独立提案，\x01",
            "是在两股与我们对立势力的\x01",
            "正中央发表的。\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x8,
        (
            "哎呀，不得不说，市长这次的\x01",
            "举动真是相当大胆啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B8C")

    Jump("loc_1FF0")

    label("loc_1B91")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1D08")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C6D")

    #C0031
    ChrTalk(
        0x8,
        (
            "我们得到情报，\x01",
            "据说共和国的恐怖分子\x01",
            "将会潜入克洛斯贝尔……\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x8,
        (
            "恐怖活动可真是吓人啊，\x01",
            "就算想让自己的主张得到他人的认同，\x01",
            "也应该采用其它方法嘛……\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x8,
        (
            "……不过，现在说\x01",
            "这种话也无济于事。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1D03")

    label("loc_1C6D")


    #C0034
    ChrTalk(
        0x8,
        (
            "我们得到情报，\x01",
            "据说共和国的恐怖分子\x01",
            "将会潜入克洛斯贝尔……\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x8,
        (
            "我们也预想了不少针对\x01",
            "恐怖活动的预防措施……\x01",
            "但首先还是要集中精神，做好警备工作。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D03")

    Jump("loc_1FF0")

    label("loc_1D08")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1E28")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1DB8")

    #C0036
    ChrTalk(
        0x8,
        (
            "今天早上，洛克史密斯总统的\x01",
            "白色轿车从这里经过了。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x8,
        (
            "既要迎接总统，又要进行\x01",
            "交通管制，实在是非常忙碌。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x8,
        (
            "首脑来访这等大事\x01",
            "果然很受重视啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1E23")

    label("loc_1DB8")


    #C0039
    ChrTalk(
        0x8,
        (
            "今早要迎接洛克史密斯总统，\x01",
            "还要进行交通管制，\x01",
            "实在是非常忙碌。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x8,
        (
            "首脑来访这等大事\x01",
            "果然很受重视啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E23")

    Jump("loc_1FF0")

    label("loc_1E28")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1FF0")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6F, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1EBB")

    #C0041
    ChrTalk(
        0x8,
        (
            "哎呀～多亏各位前来帮忙，\x01",
            "这场演习的效果非常不错，\x01",
            "你们干得很出色啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x8,
        (
            "如果下次还有机会，\x01",
            "希望能与你们再次切磋。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1FF0")

    label("loc_1EBB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F71")

    #C0043
    ChrTalk(
        0x8,
        (
            "刚到唐古拉姆门就任的\x01",
            "道格拉斯副司令真是个\x01",
            "率直爽朗的人。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x8,
        (
            "如果要我形容的话，\x01",
            "他就像是个可靠的大众兄长。\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x8,
        (
            "……但只要牵扯到工作，\x01",
            "他就会严厉得像鬼一样。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1FF0")

    label("loc_1F71")


    #C0046
    ChrTalk(
        0x8,
        (
            "道格拉斯副司令\x01",
            "真是个率直爽朗的人啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x8,
        (
            "如果要我形容的话，\x01",
            "他就像是个可靠的大众兄长。\x01",
            "……但他对工作的要求却十分严格。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1FF0")

    TalkEnd(0xFE)
    Return()

    # Function_9_14A8 end

    def Function_10_1FF4(): pass

    label("Function_10_1FF4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_219B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_20F8")

    #N0048
    NpcTalk(
        0x9,
        "士兵戴蒙",
        (
            "因为那棵蓝白色大树的出现，\x01",
            "共和国军也暂时按兵不动，\x01",
            "静观其变……\x02",
        )
    )

    CloseMessageWindow()

    #N0049
    NpcTalk(
        0x9,
        "士兵戴蒙",
        (
            "但我们如今已经失去了结界和『神机』，\x01",
            "所以绝不能放松警惕。\x02",
        )
    )

    CloseMessageWindow()

    #N0050
    NpcTalk(
        0x9,
        "士兵戴蒙",
        (
            "现在能保卫克洛斯贝尔的\x01",
            "也只有我们国防军了。\x01",
            "必须得严加警戒才行。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2196")

    label("loc_20F8")


    #N0051
    NpcTalk(
        0x9,
        "士兵戴蒙",
        (
            "因为那棵蓝白色大树的出现，\x01",
            "共和国军也暂时按兵不动，\x01",
            "静观其变……\x02",
        )
    )

    CloseMessageWindow()

    #N0052
    NpcTalk(
        0x9,
        "士兵戴蒙",
        (
            "现在能保卫克洛斯贝尔的\x01",
            "也只有我们国防军了。\x01",
            "必须得严加警戒才行。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2196")

    Jump("loc_2A71")

    label("loc_219B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2301")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_227E")

    #C0053
    ChrTalk(
        0x9,
        (
            "没能防范克洛斯贝尔市遇袭事件，\x01",
            "显然属于我们警备队的失误。\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x9,
        (
            "虽说之前的玛因兹事件\x01",
            "使我们的战斗力严重削弱……\x01",
            "但这并不能成为借口。\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x9,
        (
            "警备队作为维护治安的组织……\x01",
            "恐怕必须得好好检讨一下才行。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_22FC")

    label("loc_227E")


    #C0056
    ChrTalk(
        0x9,
        (
            "没能防范克洛斯贝尔市遇袭事件，\x01",
            "显然属于我们警备队的失误。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x9,
        (
            "警备队作为维护治安的组织……\x01",
            "恐怕必须得好好检讨一下才行。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_22FC")

    Jump("loc_2A71")

    label("loc_2301")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_236F")

    #C0058
    ChrTalk(
        0x9,
        (
            "刚刚有位男性游击士\x01",
            "问了我几个问题……\x01",
            "据说有女游击士失踪了。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x9,
        "唔……希望别出什么意外。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2A71")

    label("loc_236F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_23FF")

    #C0060
    ChrTalk(
        0x9,
        (
            "游击士们似乎正在\x01",
            "各处调查探索，\x01",
            "寻找『幻兽』的踪迹。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x9,
        (
            "有些连我们极少涉足的腹地，\x01",
            "他们都了如指掌。\x01",
            "真是一群可靠的家伙啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A71")

    label("loc_23FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2502")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_24B8")

    #C0062
    ChrTalk(
        0x9,
        (
            "万一『幻兽』伤到了\x01",
            "外国人，两大国一定\x01",
            "会以此为借口而发难。\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x9,
        (
            "这可直接关系到边境的\x01",
            "局势，所以我们警备队\x01",
            "也很重视这个问题。\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x9,
        "调查工作就拜托各位了。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_24FD")

    label("loc_24B8")


    #C0065
    ChrTalk(
        0x9,
        (
            "我们警备队也很重视\x01",
            "有关幻兽的问题。\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x9,
        "调查方面就拜托各位了。\x02",
    )

    CloseMessageWindow()

    label("loc_24FD")

    Jump("loc_2A71")

    label("loc_2502")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2580")

    #C0067
    ChrTalk(
        0x9,
        (
            "关于恐怖分子的问题，\x01",
            "我们正在全力\x01",
            "警戒中。\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x9,
        (
            "赌上警备队的荣耀，\x01",
            "我们一定要成功阻止\x01",
            "那帮恐怖分子的入侵。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A71")

    label("loc_2580")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_25EF")

    #C0069
    ChrTalk(
        0x9,
        (
            "听说洛克史密斯总统\x01",
            "作为庶民派代表，\x01",
            "广受共和国人民的爱戴。\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x9,
        (
            "他究竟是位\x01",
            "什么样的人物呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A71")

    label("loc_25EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2A71")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6F, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_26AF")

    #C0071
    ChrTalk(
        0x9,
        (
            "虽说有诺艾尔上士助阵，\x01",
            "但真没想到你们能与道格拉斯\x01",
            "副司令抗衡到如此程度……\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0x9,
        (
            "特别任务支援科确实不愧是\x01",
            "解决了教团事件的大功臣啊。\x01",
            "老实说，实在是让我敬佩不已。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A71")

    label("loc_26AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14F, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2916")

    #C0073
    ChrTalk(
        0x9,
        (
            "诺艾尔上士，您辛苦了！\x01",
            "……………………………………\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x109,
        (
            "#10100F戴蒙，你也辛苦了。\x01",
            "……请问，有什么问题吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0x9,
        (
            "……唔，该怎么说呢……\x01",
            "没有穿着警备队制服的上士，\x01",
            "看起来还真有些新鲜啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x109,
        (
            "#10105F啊，说起来，\x01",
            "我好像还是第一次穿成这样\x01",
            "出现在唐古拉姆门……\x02\x03",

            "#10112F真抱歉，\x01",
            "是我考虑不周。\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0x9,
        (
            "没、没这回事。\x01",
            "这身衣服很好看啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0x104,
        (
            "#00300F哈哈～难道……\x01",
            "你是因为从没看过诺艾尔这幅打扮，\x01",
            "所以感到心跳加速了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0x109,
        "#10105F咦！？\x02",
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0x9,
        (
            "不、不是的，那个……\x01",
            "我绝对没有那个意思。\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0x9,
        (
            "……是、是我失礼了，\x01",
            "上士，请您忘了这件事吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x109,
        (
            "#10106F（兰、兰迪前辈真是的，\x01",
            "  这也太让人难为情了……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x14F, 7)
    Jump("loc_2A71")

    label("loc_2916")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_29EE")

    #C0083
    ChrTalk(
        0x9,
        (
            "……只不过是换了套衣服而已，\x01",
            "我未免也太大惊小怪了，\x01",
            "看来我的修行还远远不够啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x9,
        (
            "实在是太失礼了，\x01",
            "上士，请您忘了这件事吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0x109,
        "#10106F好、好的……\x02",
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x101,
        (
            "#00006F（这是修行的\x01",
            "  问题吗……？）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2A71")

    label("loc_29EE")


    #C0087
    ChrTalk(
        0x9,
        (
            "……只不过是换了套衣服而已，\x01",
            "我未免也太大惊小怪了，\x01",
            "看来我的修行还远远不够啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0x9,
        (
            "实在是太失礼了，\x01",
            "上士，请您忘了这件事吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A71")

    TalkEnd(0xFE)
    Return()

    # Function_10_1FF4 end

    def Function_11_2A75(): pass

    label("Function_11_2A75")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2B8A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B2B")

    #C0089
    ChrTalk(
        0xC,
        "我是在城市东出口遇到这些人的。\x02",
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0xC,
        (
            "他们说想和我一起前往\x01",
            "唐古拉姆门，所以我就\x01",
            "把他们当作护卫带过来了……\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0xC,
        "……但老实说，他们完全没派上用场啊。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_2B8A")

    label("loc_2B2B")


    #C0092
    ChrTalk(
        0xC,
        (
            "话说回来，走在野外，\x01",
            "还真让人毛骨悚然。\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0xC,
        "还要按照原定计划，继续前往阿尔摩利卡村吗……\x02",
    )

    CloseMessageWindow()

    label("loc_2B8A")

    TalkEnd(0xFE)
    Return()

    # Function_11_2A75 end

    def Function_12_2B8E(): pass

    label("Function_12_2B8E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2CAB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C5B")

    #C0094
    ChrTalk(
        0xD,
        (
            "呼……呼……\x01",
            "在途中遇到幻兽时，\x01",
            "我真是完全不知所措了……\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0xD,
        (
            "……不、不过总算是平安抵达这里了。\x01",
            "接下来，就只剩下返回共和国的那段路了……\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0xD,
        "我、我能不能平安回去呢……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_2CAB")

    label("loc_2C5B")


    #C0097
    ChrTalk(
        0xD,
        (
            "我这辈子还是第一次\x01",
            "遇到这种事……\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0xD,
        (
            "不、不知还能不能平安\x01",
            "回到共和国……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2CAB")

    TalkEnd(0xFE)
    Return()

    # Function_12_2B8E end

    def Function_13_2CAF(): pass

    label("Function_13_2CAF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2D9B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D4F")

    #C0099
    ChrTalk(
        0xE,
        (
            "呼……呼……\x01",
            "我本以为这个女孩\x01",
            "肯定知道安全的道路……\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0xE,
        (
            "没想到竟然让我们在\x01",
            "野外跑了次马拉松……\x01",
            "我、我还以为自己死定了……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_2D9B")

    label("loc_2D4F")


    #C0101
    ChrTalk(
        0xE,
        (
            "呜呜，为什么我们会\x01",
            "遇到这种事啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0xE,
        (
            "我再也不要来\x01",
            "克洛斯贝尔了……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D9B")

    TalkEnd(0xFE)
    Return()

    # Function_13_2CAF end

    def Function_14_2D9F(): pass

    label("Function_14_2D9F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2E8E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E65")

    #C0103
    ChrTalk(
        0xF,
        (
            "好不容易才等到结界消失，\x01",
            "却弄不到导力车……\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0xF,
        (
            "没办法，只好让偶然遇到的\x01",
            "这个女孩给我们带路，\x01",
            "结果却又吃了好一番苦头……\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0xF,
        (
            "早、早知如此，\x01",
            "还不如搭个便车呢……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_2E8E")

    label("loc_2E65")


    #C0106
    ChrTalk(
        0xF,
        (
            "早、早知如此，\x01",
            "还不如搭个便车呢……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E8E")

    TalkEnd(0xFE)
    Return()

    # Function_14_2D9F end

    def Function_15_2E92(): pass

    label("Function_15_2E92")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3016")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F83")

    #N0107
    NpcTalk(
        0xA,
        "士兵加利森",
        (
            "根据副司令的指示，\x01",
            "我们将继续对共和国\x01",
            "保持警戒……\x02",
        )
    )

    CloseMessageWindow()

    #N0108
    NpcTalk(
        0xA,
        "士兵加利森",
        (
            "但是，以前能够击退两大国的军队，\x01",
            "全是倚仗『神机』的力量。\x02",
        )
    )

    CloseMessageWindow()

    #N0109
    NpcTalk(
        0xA,
        "士兵加利森",
        (
            "如果他们现在再次发动侵攻……\x01",
            "我们恐怕就抵挡不住了吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3011")

    label("loc_2F83")


    #N0110
    NpcTalk(
        0xA,
        "士兵加利森",
        (
            "以前能够击退两大国的军队，\x01",
            "全是倚仗『神机』的力量。\x02",
        )
    )

    CloseMessageWindow()

    #N0111
    NpcTalk(
        0xA,
        "士兵加利森",
        (
            "如果共和国军现在再次发动侵攻……\x01",
            "我们恐怕就抵挡不住了吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3011")

    Jump("loc_376E")

    label("loc_3016")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3153")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_30E0")

    #C0112
    ChrTalk(
        0xA,
        (
            "警备队在与猎兵团的战斗中损伤惨重，\x01",
            "如今已经有些溃不成军。\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0xA,
        (
            "老实说，如果再让我去和那些家伙交战，\x01",
            "我大概就会产生临阵脱逃的想法了。\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0xA,
        (
            "我们今后究竟该\x01",
            "怎么办才好呢……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_314E")

    label("loc_30E0")


    #C0115
    ChrTalk(
        0xA,
        (
            "老实说，如果再让我去和猎兵团交战，\x01",
            "我大概就会产生临阵脱逃的想法了。\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0xA,
        (
            "我们今后究竟该\x01",
            "怎么办才好呢……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_314E")

    Jump("loc_376E")

    label("loc_3153")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_323C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_31CE")

    #C0117
    ChrTalk(
        0xA,
        "……啊嚏！！\x02",
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0xA,
        (
            "……身体有些\x01",
            "发冷呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0xA,
        (
            "要是患上感冒可就麻烦了，\x01",
            "干脆去休息一下吧……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3237")

    label("loc_31CE")


    #C0120
    ChrTalk(
        0xA,
        (
            "身体有些\x01",
            "发冷呢。\x01",
            "去食堂稍微休息一下吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0xA,
        (
            "毕竟现在正处于紧张状态，\x01",
            "在这种时候搞坏身体就糟了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3237")

    Jump("loc_376E")

    label("loc_323C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_337E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3300")

    #C0122
    ChrTalk(
        0xA,
        (
            "如今还没有明确唐古拉姆丘陵\x01",
            "到底属于克洛斯贝尔，\x01",
            "还是属于共和国。\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0xA,
        (
            "但实际上还是\x01",
            "由共和国统治……\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0xA,
        (
            "要是克洛斯贝尔\x01",
            "真的能实现独立……\x01",
            "恐怕会出现一番争夺战吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3379")

    label("loc_3300")


    #C0125
    ChrTalk(
        0xA,
        (
            "如今还没有明确唐古拉姆丘陵\x01",
            "到底属于克洛斯贝尔，\x01",
            "还是属于共和国。\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0xA,
        (
            "就算真的能实现独立，\x01",
            "恐怕也会出现一番争夺战。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3379")

    Jump("loc_376E")

    label("loc_337E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_347D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3420")

    #C0127
    ChrTalk(
        0xA,
        (
            "随着居民投票日渐渐临近，\x01",
            "压力也逐日增强。\x02",
        )
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0xA,
        (
            "听说共和国的国民强烈反对\x01",
            "克洛斯贝尔独立。\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0xA,
        (
            "千万不要出现\x01",
            "太过火的运动或政策啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3478")

    label("loc_3420")


    #C0130
    ChrTalk(
        0xA,
        (
            "听说共和国的国民强烈反对\x01",
            "克洛斯贝尔独立。\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0xA,
        (
            "千万不要出现\x01",
            "太过火的运动或政策啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3478")

    Jump("loc_376E")

    label("loc_347D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3606")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3563")

    #C0132
    ChrTalk(
        0xA,
        (
            "如你所见，唐古拉姆丘陵\x01",
            "十分适合远眺，\x01",
            "而且这里还备有监视用设施。\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0xA,
        (
            "如果有飞艇或车辆过来，\x01",
            "马上就能看到了。\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0xA,
        (
            "当然了，实际上并没有这么简单……\x01",
            "但请放心，我们绝不会让\x01",
            "恐怖分子进入克洛斯贝尔的。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3601")

    label("loc_3563")


    #C0135
    ChrTalk(
        0xA,
        (
            "如你所见，唐古拉姆丘陵\x01",
            "十分适合远眺，\x01",
            "而且这里还备有监视用设施。\x02",
        )
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0xA,
        (
            "当然了，实际上并没有这么简单……\x01",
            "但请放心，我们绝不会让\x01",
            "恐怖分子进入克洛斯贝尔的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3601")

    Jump("loc_376E")

    label("loc_3606")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3680")

    #C0137
    ChrTalk(
        0xA,
        (
            "洛克史密斯总统的轿车\x01",
            "被好几辆护卫车簇拥着。\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0xA,
        (
            "真不愧是统治共和国的总统啊……\x01",
            "那副场面真是太壮观了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_376E")

    label("loc_3680")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_376E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_371D")

    #C0139
    ChrTalk(
        0xA,
        (
            "一望无际的唐古拉姆丘陵……\x01",
            "这风景十分漂亮吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0xA,
        (
            "虽说此地在历史之中多次\x01",
            "成为纷争的舞台……\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0xA,
        "可我真的很喜欢这副景色呢。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_376E")

    label("loc_371D")


    #C0142
    ChrTalk(
        0xA,
        (
            "一望无际的唐古拉姆丘陵……\x01",
            "这风景十分漂亮吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0xA,
        "我真的很喜欢这副景色呢。\x02",
    )

    CloseMessageWindow()

    label("loc_376E")

    TalkEnd(0xFE)
    Return()

    # Function_15_2E92 end

    def Function_16_3772(): pass

    label("Function_16_3772")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_38D1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_384F")

    #N0144
    NpcTalk(
        0xB,
        "士兵巴雷尔",
        (
            "无论身处克洛斯贝尔的哪个地区，\x01",
            "应该都能清楚地看到\x01",
            "那棵神秘的树木……\x02",
        )
    )

    CloseMessageWindow()

    #N0145
    NpcTalk(
        0xB,
        "士兵巴雷尔",
        (
            "突然冒出那种东西，\x01",
            "这事情绝对不同寻常。\x02",
        )
    )

    CloseMessageWindow()

    #N0146
    NpcTalk(
        0xB,
        "士兵巴雷尔",
        (
            "克洛斯贝尔到底\x01",
            "会变成什么样呢……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_38CC")

    label("loc_384F")


    #N0147
    NpcTalk(
        0xB,
        "士兵巴雷尔",
        (
            "突然冒出那棵\x01",
            "神秘的树木……\x01",
            "这事情绝对不同寻常。\x02",
        )
    )

    CloseMessageWindow()

    #N0148
    NpcTalk(
        0xB,
        "士兵巴雷尔",
        (
            "不知身在贝尔加德门的布鲁德\x01",
            "现在是否平安……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_38CC")

    Jump("loc_410E")

    label("loc_38D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3A2A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_39B2")

    #C0149
    ChrTalk(
        0xB,
        (
            "听说我那在贝尔加德门\x01",
            "任职的儿时好友\x01",
            "布鲁德平安无事。\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0xB,
        (
            "……但还是不能放下心来。\x01",
            "警备队失去的东西\x01",
            "实在是太过沉重了。\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0xB,
        (
            "老实说，我对未知的前路\x01",
            "感到十分恐惧……\x01",
            "但现在也只能做好心理准备了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3A25")

    label("loc_39B2")


    #C0152
    ChrTalk(
        0xB,
        (
            "警备队失去的东西\x01",
            "实在是太过沉重了。\x02",
        )
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0xB,
        (
            "老实说，我对未知的前路\x01",
            "感到十分恐惧……\x01",
            "但现在也只能做好心理准备了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3A25")

    Jump("loc_410E")

    label("loc_3A2A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3B56")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3AEF")

    #C0154
    ChrTalk(
        0xB,
        (
            "雷达设施将在今天全天\x01",
            "持续运作。\x02",
        )
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0xB,
        (
            "在下雨天，\x01",
            "很难凭肉眼把握空中状况，\x01",
            "对于警备工作而言，雷达是十分重要的。\x02",
        )
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0xB,
        (
            "虽说在通商会议时曾被破坏，\x01",
            "但它一定会派上用场的。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3B51")

    label("loc_3AEF")


    #C0157
    ChrTalk(
        0xB,
        (
            "对于警备工作而言，\x01",
            "雷达是十分重要的。\x02",
        )
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0xB,
        (
            "虽说在通商会议时曾被破坏，\x01",
            "但它一定会派上用场的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3B51")

    Jump("loc_410E")

    label("loc_3B56")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3BC9")

    #C0159
    ChrTalk(
        0xB,
        (
            "道格拉斯副司令虽然率直爽朗，\x01",
            "但实际上却是个十分冷静的人。\x02",
        )
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0xB,
        "真希望我也能成为像他那样的人……\x02",
    )

    CloseMessageWindow()
    Jump("loc_410E")

    label("loc_3BC9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3D27")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3CAD")

    #C0161
    ChrTalk(
        0xB,
        (
            "听说所谓的幻兽，类似于以前\x01",
            "曾在『月之僧院』出现的那些\x01",
            "幽灵般的不明怪物。\x02",
        )
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0xB,
        (
            "单是外表可怕倒没什么，\x01",
            "但来历完全不明，\x01",
            "实在是让人毛骨悚然……\x02",
        )
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0xB,
        (
            "今后如果碰上幻兽，\x01",
            "我可得注意一些，不能再昏倒了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3D22")

    label("loc_3CAD")


    #C0164
    ChrTalk(
        0xB,
        (
            "以前去调查\x01",
            "『月之僧院』出现的幽灵时，\x01",
            "我被吓得昏了过去。\x02",
        )
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0xB,
        (
            "今后如果碰上幻兽，\x01",
            "我可得注意一些，不能再昏倒了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3D22")

    Jump("loc_410E")

    label("loc_3D27")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3E4E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3DDD")

    #C0166
    ChrTalk(
        0xB,
        (
            "根据警察提供的情报，\x01",
            "恐怖分子出现的可能性很高。\x02",
        )
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0xB,
        (
            "说实话，我可\x01",
            "不想对上那种\x01",
            "危险的家伙啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0xB,
        (
            "啊啊，空之女神啊，\x01",
            "请您保佑今天\x01",
            "也能和平地结束……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3E49")

    label("loc_3DDD")


    #C0169
    ChrTalk(
        0xB,
        (
            "说实话，我可\x01",
            "不想对上恐怖分子\x01",
            "那种危险的家伙。\x02",
        )
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0xB,
        (
            "啊啊，空之女神啊，\x01",
            "请您保佑今天\x01",
            "也能和平地结束……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3E49")

    Jump("loc_410E")

    label("loc_3E4E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3FA2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F20")

    #C0171
    ChrTalk(
        0xB,
        (
            "迎接总统的座驾时，\x01",
            "我真是紧张得不得了。\x02",
        )
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0xB,
        (
            "我可是很胆小的……\x01",
            "总觉得连敬礼时的\x01",
            "动作都有些走样。\x02",
        )
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0xB,
        (
            "不过，总统阁下肯定不会\x01",
            "注意到我这种小兵吧……\x01",
            "话虽如此，可压力还是很大啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3F9D")

    label("loc_3F20")


    #C0174
    ChrTalk(
        0xB,
        (
            "迎接总统的座驾时，\x01",
            "我真是紧张得不得了。\x02",
        )
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0xB,
        (
            "不过，总统阁下肯定不会\x01",
            "注意到我这种小兵吧……\x01",
            "虽说如此，可压力还是很大啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3F9D")

    Jump("loc_410E")

    label("loc_3FA2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_410E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_407B")

    #C0176
    ChrTalk(
        0xB,
        (
            "我的儿时好友布鲁德就在\x01",
            "帝国方向的贝尔加德门执勤。\x02",
        )
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0xB,
        (
            "前段时间，那家伙告诉我，\x01",
            "他总算成功结束了\x01",
            "复健训练。\x02",
        )
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0xB,
        (
            "哎呀～之前我担心了好一阵……\x01",
            "现在他终于完全恢复了，我也总算松了一口气。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_410E")

    label("loc_407B")


    #C0179
    ChrTalk(
        0xB,
        (
            "前段时间，我的儿时好友布鲁德\x01",
            "告诉我，他总算成功结束了\x01",
            "复健训练。\x02",
        )
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0xB,
        (
            "哎呀～之前我担心了好一阵……\x01",
            "现在他终于完全恢复了，我也总算松了一口气。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_410E")

    TalkEnd(0xFE)
    Return()

    # Function_16_3772 end

    def Function_17_4112(): pass

    label("Function_17_4112")

    SetMapFlags(0x80)
    SetMapFlags(0x8000000)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x31, 2)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4144")
    SetScenarioFlags(0x31, 2)

    label("loc_4144")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_418A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 2)), scpexpr(EXPR_END)), "loc_4184")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4179")
    Sound(2499, 255, 100, 0)    #voice#Noel
    Jump("loc_417F")

    label("loc_4179")

    Sound(3537, 255, 100, 0)    #voice#Noel

    label("loc_417F")

    Jump("loc_418A")

    label("loc_4184")

    Sound(3344, 255, 100, 0)    #voice#Lloyd

    label("loc_418A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4431")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_END)), "loc_41FB")
    MenuCmd(0, 0)
    MenuCmd(1, 0, "登上梅尔卡瓦")
    MenuCmd(1, 0, "放弃")
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_41DB"),
        (SWITCH_DEFAULT, "loc_41EC"),
    )


    label("loc_41DB")

    SetScenarioFlags(0x22, 0)
    NewScene("e3020", 0, 0, 0)
    IdleLoop()
    Jump("loc_41F6")

    label("loc_41EC")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_41F6")

    Jump("loc_442C")

    label("loc_41FB")

    MenuCmd(0, 0)
    MenuCmd(1, 0, "驾驶导力车移动")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_422B")
    MenuCmd(1, 0, "在导力车中休息")

    label("loc_422B")

    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_4255"),
        (1, "loc_4359"),
        (2, "loc_43EA"),
        (SWITCH_DEFAULT, "loc_4422"),
    )


    label("loc_4255")

    SetMapObjFrame(0x6, "light", 0x0, 0x1)
    OP_74(0x6, 0x1E)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4286")
    OP_70(0x6, 0x12C)
    OP_71(0x6, 0x12C, 0x14A, 0x0, 0x0)
    Jump("loc_4296")

    label("loc_4286")

    OP_70(0x6, 0xF0)
    OP_71(0x6, 0xF0, 0x10E, 0x0, 0x0)

    label("loc_4296")

    Sound(462, 0, 100, 0)
    SoundLoad(2500)
    SoundLoad(3538)
    SoundLoad(3345)
    Sleep(700)
    FadeToDark(300, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x2E, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_42EC")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_42EC")

    FadeToDark(0, 0, -1)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D4, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_430F")
    Sound(461, 0, 100, 0)

    label("loc_430F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_432F")
    OP_70(0x6, 0x14A)
    OP_71(0x6, 0x14A, 0x12C, 0x0, 0x0)
    Jump("loc_433F")

    label("loc_432F")

    OP_70(0x6, 0x10E)
    OP_71(0x6, 0x10E, 0xF0, 0x0, 0x0)

    label("loc_433F")

    Sleep(1000)
    OP_0D()
    SetMapObjFrame(0x6, "light", 0x1, 0x1)
    OP_70(0x6, 0x0)
    Jump("loc_418A")

    label("loc_4359")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_43CB")
    OP_57(0x0)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_5A()
    Sound(13, 0, 100, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 0)), scpexpr(EXPR_END)), "loc_438E")
    OP_32(0xFF, 0xFF, 0x0)
    Jump("loc_43A6")

    label("loc_438E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_43A1")
    OP_32(0xFF, 0xFE, 0x0)
    Jump("loc_43A6")

    label("loc_43A1")

    OP_32(0xFF, 0xFA, 0x0)

    label("loc_43A6")

    OP_6A(0x0, 0x0)
    Sleep(3500)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_43E5")

    label("loc_43CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_43DB")
    OP_AF(0xFB)
    Jump("loc_43E5")

    label("loc_43DB")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_43E5")

    Jump("loc_442C")

    label("loc_43EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4403")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_441D")

    label("loc_4403")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_4413")
    OP_AF(0xFB)
    Jump("loc_441D")

    label("loc_4413")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_441D")

    Jump("loc_442C")

    label("loc_4422")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_442C")

    Jump("loc_418A")

    label("loc_4431")

    ClearMapFlags(0x8000000)
    OP_60(0x0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    # Function_17_4112 end

    def Function_18_443F(): pass

    label("Function_18_443F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_4475")
    EventBegin(0x2)
    ClearMapFlags(0x20)
    SetChrName("")

    #A0181
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "导力巴士已经停运了。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    EventEnd(0x3)
    Return()

    label("loc_4475")

    Call(0, 5)
    Return()

    # Function_18_443F end

    def Function_19_4479(): pass

    label("Function_19_4479")

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

    def lambda_45DF():
        OP_96(0xFE, 0xFFFE2B40, 0xFFFFD8F0, 0xFFFF67A8, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_45DF)
    OP_6F(0x79)
    FadeToDark(2000, 0, -1)
    OP_0D()
    EndChrThread(0x11, 0x1)
    SetScenarioFlags(0x22, 0)
    NewScene("e0410", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_19_4479 end

    def Function_20_4612(): pass

    label("Function_20_4612")

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
        "#00005F#5P哦……？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 0)

    def lambda_4782():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_4782)

    #C0183
    ChrTalk(
        0x102,
        "#00105F#12P是其它部门打来的吗？\x02",
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
            "#00000F#30W您好，我是特别任务支援科的\x01",
            "罗伊德·班宁斯。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("嘹亮的声音")

    #A0185
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "哦呵呵……\x01",
            "是我啦，是我。\x02\x03",

            "猜到人家是谁了吗？\x02",
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
            "#00012F米歇尔先生……\x01",
            "那个……有什么事吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("米歇尔的声音")

    #A0187
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "哦呵呵，竟然一下就猜出来了，\x01",
            "挺机灵的嘛。\x02\x03",

            "还是说，这是因为爱呢？\x02",
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
            "#00006F不，只是除了米歇尔先生之外，\x01",
            "没有别人会这样说话而已。\x02\x03",

            "#00000F莫非事情和去协会\x01",
            "打搅的琪雅有关？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("米歇尔的声音")

    #A0189
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "哦，你说那孩子啊。\x02\x03",

            "她带着小滴\x01",
            "去港湾区玩了。\x02\x03",

            "那条警犬……是叫蔡特吧？\x01",
            "它也一起去了，\x01",
            "我想应该没问题的。\x02",
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
            "#00002F嗯，有蔡特同行，\x01",
            "应该就不用担心了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("米歇尔的声音")

    #A0191
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "哎呀，果然是这样吗？\x02\x03",

            "久闻大名，\x01",
            "它确实威风凛凛呢。\x02\x03",

            "不愧是传说中的\x01",
            "『神狼』啊。\x02",
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
            "#00004F哈哈……我想它终究不是\x01",
            "传说中的那匹狼吧。\x02\x03",

            "#00005F啊，您是特意通知\x01",
            "我们这件事的吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("米歇尔的声音")

    #A0193
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "不，接下来才是正题。\x02\x03",

            "其实是亚里欧斯想和你们\x01",
            "交换情报啦。\x02\x03",

            "他大概会在傍晚时分回来，\x01",
            "你们能不能抽点时间过来？\x02",
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
            "#00000F傍晚吗……\x01",
            "应该没问题。\x02\x03",

            "说到交换情报，\x01",
            "当然是关于通商会议的吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("米歇尔的声音")

    #A0195
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "也有这方面的内容……\x01",
            "但主要还是关于『黑月』和『赤色星座』的情报。\x02",
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
            "#00003F……明白了。\x02\x03",

            "#00001F我们把手头的事情处理完以后，\x01",
            "就会前去拜访的。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("米歇尔的声音")

    #A0197
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "嗯，等你们哦。\x07\x00\x02",
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
            "#00100F#12P好像是游击士协会的\x01",
            "米歇尔先生啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0x104,
        "#00305F#11P出什么事了吗？\x02",
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
        "#00006F#5P没有，只是要和我们交换情报。\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    #A0201
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "罗伊德向其他成员\x01",
            "说明了米歇尔的提议。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0202
    ChrTalk(
        0x104,
        (
            "#00303F#11P『黑月』和『赤色星座』吗……\x02\x03",

            "#00301F的确，亚里欧斯那大叔对自治州外的\x01",
            "情报应该也了解得很清楚。\x02",
        )
    )

    CloseMessageWindow()

    #C0203
    ChrTalk(
        0x105,
        (
            "#10304F#11P呵呵，说不定正是及时雨呢。\x02\x03",

            "#10300F那么，我们现在就\x01",
            "回克洛斯贝尔市吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0204
    ChrTalk(
        0x101,
        (
            "#00000F#5P不，亚里欧斯先生\x01",
            "要到傍晚才能回去。\x02\x03",

            "在那之前，我们先把\x01",
            "自己的工作完成吧。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14F, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14F, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x149, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5008")

    #C0205
    ChrTalk(
        0x102,
        (
            "#00104F#12P虽说已经收集到了不少\x01",
            "有关『赤色星座』的情报……\x02\x03",

            "#00102F但我们难得有了导力车，\x01",
            "再四处转转也不错。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_507A")

    label("loc_5008")


    #C0206
    ChrTalk(
        0x102,
        (
            "#00103F#12P目前还没有收集到多少\x01",
            "有关『赤色星座』的情报……\x02\x03",

            "#00100F我们难得有了导力车，\x01",
            "还是再四处转转为好。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_507A")


    #C0207
    ChrTalk(
        0x109,
        (
            "#10100F#11P好，把手头的事情办完之后，\x01",
            "我们就去东街的协会吧。\x02",
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

    # Function_20_4612 end

    def Function_21_50F7(): pass

    label("Function_21_50F7")

    OP_9B(0x0, 0xFE, 0x0, 0x2EE0, 0x7D0, 0x0)
    Return()

    # Function_21_50F7 end

    def Function_22_5107(): pass

    label("Function_22_5107")

    Sleep(50)
    OP_9B(0x0, 0xFE, 0x0, 0x2EE0, 0x7D0, 0x0)
    Return()

    # Function_22_5107 end

    def Function_23_511A(): pass

    label("Function_23_511A")

    Sleep(100)
    OP_9B(0x0, 0xFE, 0x0, 0x2EE0, 0x7D0, 0x0)
    Return()

    # Function_23_511A end

    def Function_24_512D(): pass

    label("Function_24_512D")

    Sleep(150)
    OP_9B(0x0, 0xFE, 0x0, 0x2EE0, 0x7D0, 0x0)
    Return()

    # Function_24_512D end

    def Function_25_5140(): pass

    label("Function_25_5140")

    Sleep(200)
    OP_9B(0x0, 0xFE, 0x0, 0x2EE0, 0x7D0, 0x0)
    Return()

    # Function_25_5140 end

    def Function_26_5153(): pass

    label("Function_26_5153")

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
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_53F7")
    Sleep(2500)
    SetChrPos(0x101, -53200, 0, 220, 90)
    SetChrPos(0x102, -54130, 0, -950, 90)
    SetChrPos(0x104, -54120, 0, 1520, 90)
    SetChrPos(0x109, -55800, 0, 1010, 90)
    SetChrPos(0x105, -56000, 0, -620, 90)

    def lambda_52C9():
        OP_97(0xFE, 0x1F40, 0x0, 0x0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_52C9)

    def lambda_52E3():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_52E3)
    Sleep(100)

    def lambda_52F7():
        OP_97(0xFE, 0x1F40, 0x0, 0x0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_52F7)

    def lambda_5311():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_5311)
    Sleep(120)

    def lambda_5325():
        OP_97(0xFE, 0x1F40, 0x0, 0x0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_5325)

    def lambda_533F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_533F)
    Sleep(90)

    def lambda_5353():
        OP_97(0xFE, 0x1F40, 0x0, 0x0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_5353)

    def lambda_536D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_536D)
    Sleep(100)

    def lambda_5381():
        OP_97(0xFE, 0x1F40, 0x0, 0x0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_5381)

    def lambda_539B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_539B)
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
    Jump("loc_5747")

    label("loc_53F7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_55BC")
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

    def lambda_5470():
        OP_95(0xFE, -37480, 0, 280, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_5470)
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
    Jump("loc_5747")

    label("loc_55BC")

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

    def lambda_5635():
        OP_95(0xFE, -37480, 0, 280, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_5635)
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

    label("loc_5747")


    #C0208
    ChrTalk(
        0x101,
        "#00000F抵达唐古拉姆门了啊。\x02",
    )

    CloseMessageWindow()

    #C0209
    ChrTalk(
        0x105,
        (
            "#12P#10300F我记得诺艾尔外派到支援科之前，\x01",
            "就是在这里执勤的吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0210
    ChrTalk(
        0x109,
        (
            "#10100F嗯，是的。\x02\x03",

            "这里是负责警戒\x01",
            "共和国方向的边境大门。\x02",
        )
    )

    CloseMessageWindow()

    #C0211
    ChrTalk(
        0x102,
        (
            "#00100F这里现在是由新上任的道格拉斯副司令\x01",
            "全权负责指挥吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0212
    ChrTalk(
        0x104,
        (
            "#00300F道格拉斯老兄啊……\x01",
            "我跟他也好久不见了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0213
    ChrTalk(
        0x101,
        (
            "#00000F这里的支援请求\x01",
            "似乎很紧急……\x02\x03",

            "我们赶快到二楼的\x01",
            "副司令室看看吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetScenarioFlags(0x1CB, 2)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_58D5")
    SetChrPos(0x0, -49550, 0, -310, 90)
    Jump("loc_590A")

    label("loc_58D5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_58F9")
    SetChrPos(0x0, -35570, 0, 510, 90)
    Jump("loc_590A")

    label("loc_58F9")

    SetChrPos(0x0, -30310, 0, 21020, 180)

    label("loc_590A")

    OP_69(0xFF, 0x0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_26_5153 end

    def Function_27_5920(): pass

    label("Function_27_5920")

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

    # Function_27_5920 end

    def Function_28_5AA7(): pass

    label("Function_28_5AA7")

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
            "#11P好，\x01",
            "现在就开始进行\x01",
            "『道格拉斯式训练』。\x02",
        )
    )

    CloseMessageWindow()

    #C0215
    ChrTalk(
        0x14,
        "#11P双方都做好准备了吗？\x02",
    )

    CloseMessageWindow()

    #C0216
    ChrTalk(
        0x9,
        (
            "#5P戴蒙及其他四名队员\x01",
            "准备完毕。\x02",
        )
    )

    CloseMessageWindow()

    #C0217
    ChrTalk(
        0x101,
        "#12P#00000F特别任务支援科也已做好准备。\x02",
    )

    CloseMessageWindow()

    #C0218
    ChrTalk(
        0x14,
        "#11P很好。\x02",
    )

    CloseMessageWindow()

    #C0219
    ChrTalk(
        0x14,
        (
            "#11P在接下来的战斗中，\x01",
            "特别任务支援科\x01",
            "禁止使用任何魔法。\x02",
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

    def lambda_5D98():
        TurnDirection(0xFE, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5D98)
    Sleep(50)

    def lambda_5DA8():
        TurnDirection(0xFE, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_5DA8)
    Sleep(50)

    def lambda_5DB8():
        TurnDirection(0xFE, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5DB8)
    Sleep(50)

    def lambda_5DC8():
        TurnDirection(0xFE, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_5DC8)
    Sleep(50)

    def lambda_5DD8():
        TurnDirection(0xFE, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_5DD8)
    Sleep(300)

    #C0220
    ChrTalk(
        0x101,
        (
            "#6P#00005F请……\x01",
            "请等一下！\x02\x03",

            "#00001F只禁止我们一方使用魔法，\x01",
            "我们的状况未免也太不利了吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0x104,
        (
            "#12P#00303F原来如此，这就是传闻中的\x01",
            "『道格拉斯式训练法』之一吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x14, 0x109, 500)
    Sleep(300)

    #C0222
    ChrTalk(
        0x14,
        "#11P没错。\x02",
    )

    CloseMessageWindow()

    #C0223
    ChrTalk(
        0x14,
        (
            "#11P这套演习方案就是\x01",
            "要让训练者尝试在\x01",
            "各种不利条件下战斗。\x02",
        )
    )

    CloseMessageWindow()

    #C0224
    ChrTalk(
        0x14,
        (
            "#11P通过这种方式\x01",
            "来提高受训者在面对\x01",
            "各种突发状况时的应对能力。\x02",
        )
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0x105,
        (
            "#12P#10304F原来如此，真不愧是被\x01",
            "称为『鬼』的人物啊。\x02\x03",

            "#10302F呵呵……\x01",
            "这不是挺有趣的嘛。\x02",
        )
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0x102,
        (
            "#12P#N#00106F呼……\x01",
            "看来也只能尽力而为了。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    def lambda_5FBC():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5FBC)
    Sleep(50)

    def lambda_5FCC():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_5FCC)
    Sleep(50)

    def lambda_5FDC():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5FDC)
    Sleep(50)

    def lambda_5FEC():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_5FEC)
    Sleep(50)

    def lambda_5FFC():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_5FFC)
    Sleep(300)

    #C0227
    ChrTalk(
        0x14,
        "#11P看来你们已经明白了啊。\x02",
    )

    CloseMessageWindow()
    StopBGM(0xBB8)
    OP_93(0x14, 0x10E, 0x1F4)
    Sleep(300)

    #C0228
    ChrTalk(
        0x14,
        (
            "#4S#11P那么……\x01",
            "全员做好准备！\x02",
        )
    )

    CloseMessageWindow()

    #N0229
    NpcTalk(
        0x9,
        "队员们",
        "#5P#4S#N遵命！！\x02",
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
            "#12P#00003F对手是警备队员，战斗的专家……\x01",
            "而且我们还不能使用魔法……\x02\x03",

            "#00007F各位，千万别大意！\x01",
            "在战斗中一定能找到取胜的方法！\x02",
        )
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0x109,
        "#12P#10101F明、明白了！\x02",
    )

    CloseMessageWindow()

    #C0232
    ChrTalk(
        0x14,
        "#5S#11P……训练开始！\x02",
    )

    CloseMessageWindow()
    Battle("BattleInfo_4B0", 0x0, 0x0, 0x0, 0xF, 0xFF)
    FadeToDark(0, 0, -1)
    Return()

    # Function_28_5AA7 end

    def Function_29_61D5(): pass

    label("Function_29_61D5")

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
        "#11P好！到此结束！\x02",
    )

    CloseMessageWindow()

    #C0234
    ChrTalk(
        0x15,
        "痛痛痛……真强啊。\x02",
    )

    CloseMessageWindow()

    #C0235
    ChrTalk(
        0x16,
        (
            "在禁止使用魔法的\x01",
            "情况下竟然还能……\x01",
            "果然名不虚传啊！\x02",
        )
    )

    CloseMessageWindow()

    #C0236
    ChrTalk(
        0x105,
        "#12P#10302F总算取胜了。\x02",
    )

    CloseMessageWindow()

    #C0237
    ChrTalk(
        0x101,
        (
            "#12P#00001F我们在战斗中\x01",
            "曾经多次经历过\x01",
            "无法使用魔法的状况……\x02\x03",

            "#00006F但像这次这样，\x01",
            "从一开始就不能使用，\x01",
            "还真是很棘手啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0238
    ChrTalk(
        0x102,
        (
            "#12P#N#00106F大约一年前，利贝尔出现\x01",
            "导力停止现象的时候，\x01",
            "大概也是这种感觉吧……\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0239
    ChrTalk(
        0x14,
        (
            "#11P看来你们已经顺利突破了\x01",
            "『道格拉斯式训练』的第一阶段。\x02",
        )
    )

    CloseMessageWindow()

    #C0240
    ChrTalk(
        0x14,
        (
            "#11P那我们就继续进行第二阶段……\x01",
            "在接下来的战斗中，\x01",
            "将禁止你们使用战技。\x02",
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

    def lambda_652A():
        TurnDirection(0xFE, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_652A)
    Sleep(50)

    def lambda_653A():
        TurnDirection(0xFE, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_653A)
    Sleep(50)

    def lambda_654A():
        TurnDirection(0xFE, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_654A)
    Sleep(50)

    def lambda_655A():
        TurnDirection(0xFE, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_655A)
    Sleep(50)

    def lambda_656A():
        TurnDirection(0xFE, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_656A)
    Sleep(300)

    #C0241
    ChrTalk(
        0x104,
        (
            "#12P#00306F喂喂，还要继续吗！？\x02\x03",

            "#00301F而且还要禁止我们使用战技！？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x14, 0x109, 500)
    Sleep(500)

    #C0242
    ChrTalk(
        0x14,
        (
            "#11P这不算什么，凭你们的实力，\x01",
            "肯定可以撑过去。\x02",
        )
    )

    CloseMessageWindow()

    #C0243
    ChrTalk(
        0x14,
        (
            "#11P把它当作一次难得的经历，\x01",
            "试试看吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0244
    ChrTalk(
        0x109,
        (
            "#12P#10106F副司令……\x01",
            "这也太难为人了……\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x14, 0x10E, 0x1F4)
    Sleep(500)

    #C0245
    ChrTalk(
        0x14,
        (
            "#4S#11P好了，警备队员，全体起立！\x01",
            "双方马上做好战斗准备！\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0xBB8)

    def lambda_66AB():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_66AB)
    Sleep(50)

    def lambda_66BB():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_66BB)
    Sleep(50)

    def lambda_66CB():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_66CB)
    Sleep(50)

    def lambda_66DB():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_66DB)
    Sleep(50)

    def lambda_66EB():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_66EB)
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
        "队员们",
        "#4S#N明白！！\x02",
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
            "#12P#00003F唔……\x01",
            "无法使用战技，\x01",
            "在战斗中必定会十分艰难……\x02\x03",

            "#00007F总之，尽量以魔法\x01",
            "和普通攻击为主\x01",
            "去战斗吧！\x02",
        )
    )

    CloseMessageWindow()

    #C0248
    ChrTalk(
        0x102,
        "#12P#00101F……好的！\x02",
    )

    CloseMessageWindow()

    #C0249
    ChrTalk(
        0x14,
        "#5S#11P……训练开始！\x02",
    )

    CloseMessageWindow()
    Battle("BattleInfo_4F4", 0x0, 0x0, 0x0, 0x10, 0xFF)
    FadeToDark(0, 0, -1)
    Return()

    # Function_29_61D5 end

    def Function_30_6890(): pass

    label("Function_30_6890")

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
        "#11P唔，到此结束！\x02",
    )

    CloseMessageWindow()

    #C0251
    ChrTalk(
        0x8,
        "呜，不会吧……\x02",
    )

    CloseMessageWindow()

    #C0252
    ChrTalk(
        0x17,
        "没想到你们强到这种地步。\x02",
    )

    CloseMessageWindow()

    #C0253
    ChrTalk(
        0x109,
        (
            "#12P#10106F呼……\x01",
            "还真是艰难啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0254
    ChrTalk(
        0x101,
        (
            "#12P#00000F是啊……\x01",
            "让人深刻体会到战技在\x01",
            "战斗中到底有多么重要了。\x02",
        )
    )

    CloseMessageWindow()

    #C0255
    ChrTalk(
        0x104,
        (
            "#12P#00304F不过，总算是撑下来了，\x01",
            "结果还算不错。\x02\x03",

            "#00301F如何？这下你就无话可说了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0256
    ChrTalk(
        0x14,
        (
            "#11P呵呵，原来如此。\x01",
            "看来你们确实\x01",
            "成长了不少。\x02",
        )
    )

    CloseMessageWindow()

    #C0257
    ChrTalk(
        0x14,
        (
            "#11P既然如此……\x01",
            "我们就进入『道格拉斯式训练』的\x01",
            "第三阶段吧！\x02",
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
            "#5S#5P警备队员，全体起立！\x01",
            "接下来开始最终训练！\x02",
        )
    )

    CloseMessageWindow()

    #N0259
    NpcTalk(
        0x9,
        "队员们",
        "#5S#N是！\x02",
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
        "#12P#00101F这是……！\x02",
    )

    CloseMessageWindow()

    #C0261
    ChrTalk(
        0x105,
        (
            "#12P#10302F嘿……\x01",
            "似乎正如传言所说，\x01",
            "是个相当厉害的强者呢。\x02",
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
            "#12P#00003F『鬼之道格拉斯』……\x01",
            "警备队的首席强者\x01",
            "可不是浪得虚名的。\x02\x03",

            "#00007F各位，打起精神！\x01",
            "瞬间都不能放松！\x02",
        )
    )

    CloseMessageWindow()

    #C0263
    ChrTalk(
        0x14,
        (
            "#5P哈哈哈！\x01",
            "很有队长的\x01",
            "样子嘛。\x02",
        )
    )

    CloseMessageWindow()

    #C0264
    ChrTalk(
        0x14,
        (
            "#5P……这场演习算是\x01",
            "前面两场的总结。\x02",
        )
    )

    CloseMessageWindow()

    #C0265
    ChrTalk(
        0x14,
        (
            "#5S#5P你们就全力以赴……\x01",
            "试着打倒我吧！\x02",
        )
    )

    CloseMessageWindow()

    #C0266
    ChrTalk(
        0x104,
        "#12P#00301F嘿，正有此意！\x02",
    )

    CloseMessageWindow()

    #C0267
    ChrTalk(
        0x109,
        "#12P#10107F上吧！\x02",
    )

    CloseMessageWindow()
    Battle("BattleInfo_538", 0x0, 0x0, 0x100, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    Return()

    # Function_30_6890 end

    def Function_31_6E49(): pass

    label("Function_31_6E49")

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
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7103")
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
        "#12P#00002F成、成功了……！\x02",
    )

    CloseMessageWindow()

    #C0269
    ChrTalk(
        0x9,
        (
            "#5P怎、怎么可能……\x01",
            "副司令居然会……！？\x02",
        )
    )

    CloseMessageWindow()

    #C0270
    ChrTalk(
        0x14,
        (
            "#5P呵呵……还挺\x01",
            "能干的嘛。\x02",
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
            "#12P#00305F……看来我们的攻击\x01",
            "完全没有奏效啊。\x02\x03",

            "#00306F啧，还是老样子，\x01",
            "结实得不像话呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0272
    ChrTalk(
        0x14,
        "#5P不，你们的攻击还是有效的。\x02",
    )

    CloseMessageWindow()

    #C0273
    ChrTalk(
        0x14,
        (
            "#5P但体力充沛一直\x01",
            "都是我唯一的优点。\x02",
        )
    )

    CloseMessageWindow()

    #C0274
    ChrTalk(
        0x102,
        "#12P#00109F您、您太谦虚了……\x02",
    )

    CloseMessageWindow()

    #C0275
    ChrTalk(
        0x109,
        "#12P#10106F副司令，您果然厉害。\x02",
    )

    CloseMessageWindow()

    #C0276
    ChrTalk(
        0x105,
        "#12P#10306F哎呀呀，甘拜下风。\x02",
    )

    CloseMessageWindow()

    #C0277
    ChrTalk(
        0x14,
        (
            "#5P好，\x01",
            "演习到此结束。\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x6F, 0x1, 0x2)
    Jump("loc_72B4")

    label("loc_7103")

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
            "#12P#00003F唔……！\x01",
            "我们的实力还是不足吗……\x02",
        )
    )

    CloseMessageWindow()

    #C0279
    ChrTalk(
        0x102,
        (
            "#12P#N#00106F已经用上了魔法和战技，\x01",
            "竟然还是赢不了他……\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0280
    ChrTalk(
        0x104,
        (
            "#12P#00301F啧，年纪也不小了，\x01",
            "却还是这么精力充沛。\x02",
        )
    )

    CloseMessageWindow()

    #C0281
    ChrTalk(
        0x14,
        (
            "#5P呵呵，我毕竟也是\x01",
            "现役警备队员啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0282
    ChrTalk(
        0x14,
        (
            "#5P话说回来，我觉得\x01",
            "你们已经很努力了。\x02",
        )
    )

    CloseMessageWindow()

    #C0283
    ChrTalk(
        0x109,
        "#12P#10106F真是惨败啊……\x02",
    )

    CloseMessageWindow()

    #C0284
    ChrTalk(
        0x105,
        (
            "#12P#10304F不愧是警备队的\x01",
            "副司令。\x02",
        )
    )

    CloseMessageWindow()

    #C0285
    ChrTalk(
        0x14,
        (
            "#5P好，\x01",
            "演习到此结束。\x02",
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

    label("loc_72B4")

    TurnDirection(0x14, 0x9, 500)
    Sleep(300)

    #C0286
    ChrTalk(
        0x14,
        (
            "#11P全体成员，返回工作岗位，\x01",
            "继续自己的工作吧。\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_7315")
    Sound(805, 0, 100, 0)
    Sound(802, 0, 100, 0)
    ClearScenarioFlags(0x1, 0)
    Jump("loc_731B")

    label("loc_7315")

    Sound(802, 0, 100, 0)

    label("loc_731B")

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
        "队员们",
        "#4S#N遵命！\x02",
    )

    CloseMessageWindow()
    OP_5A()
    TurnDirection(0x14, 0x101, 500)
    Sleep(300)

    #C0288
    ChrTalk(
        0x14,
        (
            "#5P诸位也\x01",
            "辛苦了。\x02",
        )
    )

    CloseMessageWindow()

    #C0289
    ChrTalk(
        0x14,
        (
            "#5P站着聊不太合适，\x01",
            "我们先回\x01",
            "司令室吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0290
    ChrTalk(
        0x101,
        "#12P#00000F好、好的。\x02",
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

    # Function_31_6E49 end

    def Function_32_73EE(): pass

    label("Function_32_73EE")

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

    def lambda_74A7():
        OP_95(0x101, -42000, 0, 0, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_74A7)
    Sleep(30)

    def lambda_74C4():
        OP_95(0x102, -42500, 0, -1200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_74C4)
    Sleep(40)

    def lambda_74E1():
        OP_95(0x104, -42500, 0, 1200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_74E1)
    Sleep(800)

    def lambda_74FE():
        OP_95(0x109, -44100, 0, 0, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_74FE)
    Sleep(30)

    def lambda_751B():
        OP_95(0x103, -43800, 0, -1200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_751B)
    Sleep(10)

    def lambda_7538():
        OP_95(0x105, -43800, 0, 1200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_7538)
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
            "#00000F嗯……\x01",
            "黑色运输车应该已经到了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0292
    ChrTalk(
        0x103,
        "#00200F但并没有看到那辆车啊……\x02",
    )

    CloseMessageWindow()

    #C0293
    ChrTalk(
        0x102,
        (
            "#00103F说不定他正在\x01",
            "里面办理\x01",
            "出境手续呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0294
    ChrTalk(
        0x105,
        (
            "#10300F有这个可能，但我们已经在路上\x01",
            "花费了一些时间……\x02",
        )
    )

    CloseMessageWindow()

    #C0295
    ChrTalk(
        0x109,
        "#10101F赶、赶快进去确认一下吧！\x02",
    )

    CloseMessageWindow()

    #C0296
    ChrTalk(
        0x104,
        "#00306F哎呀呀，希望能赶上……\x02",
    )

    CloseMessageWindow()

    def lambda_767C():
        OP_95(0x101, -25000, 0, 0, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_767C)
    Sleep(30)

    def lambda_7699():
        OP_95(0x102, -25500, 0, -1200, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7699)
    Sleep(40)

    def lambda_76B6():
        OP_95(0x104, -25500, 0, 1200, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_76B6)
    Sleep(30)

    def lambda_76D3():
        OP_95(0x109, -25100, 0, 0, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_76D3)
    Sleep(30)

    def lambda_76F0():
        OP_95(0x103, -25800, 0, -1200, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_76F0)
    Sleep(10)

    def lambda_770D():
        OP_95(0x105, -25800, 0, 1200, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_770D)
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

    # Function_32_73EE end

    def Function_33_774E(): pass

    label("Function_33_774E")

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
            "#00000F嗯……\x01",
            "黑色运输车应该已经到了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0298
    ChrTalk(
        0x103,
        "#00200F但并没有看到那辆车啊……\x02",
    )

    CloseMessageWindow()

    #C0299
    ChrTalk(
        0x102,
        (
            "#00103F说不定他正在\x01",
            "里面办理\x01",
            "出境手续呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0300
    ChrTalk(
        0x105,
        (
            "#10300F有这个可能，\x01",
            "但我们在等巴士的时候\x01",
            "已经花费了一些时间……\x02",
        )
    )

    CloseMessageWindow()

    #C0301
    ChrTalk(
        0x109,
        "#10101F赶、赶快进去确认一下吧！\x02",
    )

    CloseMessageWindow()

    #C0302
    ChrTalk(
        0x104,
        "#00306F哎呀呀，希望能赶上……\x02",
    )

    CloseMessageWindow()

    def lambda_7922():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_7922)
    Sleep(30)

    def lambda_7932():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_7932)
    Sleep(40)

    def lambda_7942():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_7942)
    Sleep(30)

    def lambda_7952():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_7952)
    Sleep(30)

    def lambda_7962():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_7962)
    Sleep(10)

    def lambda_7972():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_7972)
    WaitChrThread(0x109, 2)

    def lambda_7983():
        OP_95(0x109, -25100, 0, 0, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_7983)
    WaitChrThread(0x104, 2)

    def lambda_79A1():
        OP_95(0x104, -25500, 0, 1200, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_79A1)
    WaitChrThread(0x103, 2)

    def lambda_79BF():
        OP_95(0x103, -25800, 0, -1200, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_79BF)
    WaitChrThread(0x102, 2)

    def lambda_79DD():
        OP_95(0x102, -25500, 0, -1200, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_79DD)
    WaitChrThread(0x105, 2)

    def lambda_79FB():
        OP_95(0x105, -25800, 0, 1200, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_79FB)
    WaitChrThread(0x101, 2)

    def lambda_7A19():
        OP_95(0x101, -25000, 0, 0, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7A19)
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

    # Function_33_774E end

    def Function_34_7A5A(): pass

    label("Function_34_7A5A")

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

    def lambda_7B13():
        OP_96(0x12, 0xFFFF5BF0, 0x0, 0x0, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_7B13)
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
        "#00005F那是……！\x02",
    )

    CloseMessageWindow()

    #C0304
    ChrTalk(
        0x102,
        "#00101F发现了呢。\x02",
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
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_7D00")

    #C0305
    ChrTalk(
        0x18,
        (
            "呵呵……\x01",
            "来到这里就可以安心了。\x02",
        )
    )

    CloseMessageWindow()

    #C0306
    ChrTalk(
        0x18,
        (
            "接下来，只要把这些医疗物资\x01",
            "运到共和国卖掉就可以了。\x02",
        )
    )

    CloseMessageWindow()

    #C0307
    ChrTalk(
        0x18,
        (
            "雷米菲利亚制造的医疗物资……\x01",
            "应该能卖个好价钱吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7DC2")

    label("loc_7D00")


    #N0308
    NpcTalk(
        0x18,
        "商人装扮的男人",
        (
            "呵呵……\x01",
            "来到这里就可以安心了。\x02",
        )
    )

    CloseMessageWindow()

    #N0309
    NpcTalk(
        0x18,
        "商人装扮的男人",
        (
            "接下来，只要把这些医疗物资\x01",
            "运到共和国卖掉就可以了。\x02",
        )
    )

    CloseMessageWindow()

    #N0310
    NpcTalk(
        0x18,
        "商人装扮的男人",
        (
            "雷米菲利亚制造的医疗物资……\x01",
            "应该能卖个好价钱吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7DC2")


    #C0311
    ChrTalk(
        0x101,
        "#00007F休想得逞！\x02",
    )

    CloseMessageWindow()
    OP_63(0x18, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_68(-25430, 1000, -10970, 3000)
    MoveCamera(42, 28, 0, 3000)
    OP_6E(510, 3000)
    SetCameraDistance(21210, 3000)

    def lambda_7E24():
        OP_95(0x101, -26500, 0, -11450, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7E24)

    def lambda_7E3E():
        OP_95(0x102, -26230, 0, -10150, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7E3E)

    def lambda_7E58():
        OP_95(0x103, -26500, 0, -12750, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_7E58)

    def lambda_7E72():
        OP_95(0x104, -27950, 0, -11450, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_7E72)

    def lambda_7E8C():
        OP_95(0x105, -27550, 0, -10200, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_7E8C)

    def lambda_7EA6():
        OP_95(0x109, -27550, 0, -12750, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_7EA6)
    WaitChrThread(0x101, 1)

    def lambda_7EC4():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_7EC4)
    WaitChrThread(0x102, 1)

    def lambda_7ED5():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_7ED5)
    WaitChrThread(0x103, 1)

    def lambda_7EE6():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_7EE6)
    WaitChrThread(0x104, 1)

    def lambda_7EF7():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_7EF7)
    WaitChrThread(0x105, 1)

    def lambda_7F08():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_7F08)
    WaitChrThread(0x109, 1)

    def lambda_7F19():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_7F19)
    OP_93(0x18, 0x10E, 0x1F4)
    WaitChrThread(0x109, 2)
    OP_6F(0x79)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_81E9")

    #C0312
    ChrTalk(
        0x18,
        "你们是……！！\x02",
    )

    CloseMessageWindow()

    #C0313
    ChrTalk(
        0x101,
        (
            "#00001F敏涅斯……\x01",
            "其实我已经隐约察觉到了，\x01",
            "但没想到真的是你。\x02",
        )
    )

    CloseMessageWindow()

    #C0314
    ChrTalk(
        0x102,
        (
            "#00103F您涉嫌在空港\x01",
            "骗取医疗物资。\x02\x03",

            "#00101F不好意思，可以让我们\x01",
            "检查一下您车上的货物吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0315
    ChrTalk(
        0x18,
        (
            "……哼，看来是因为心急，\x01",
            "这次的行事手段好像太过草率了。\x02",
        )
    )

    CloseMessageWindow()

    #C0316
    ChrTalk(
        0x105,
        (
            "#10302F呵呵，确实如此。\x01",
            "与在阿尔摩利卡村的那次相比，\x01",
            "这次的手段实在是欠缺精彩呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0317
    ChrTalk(
        0x18,
        (
            "……都怪你们多管闲事，\x01",
            "使我在阿尔摩利卡村的行动失败，\x01",
            "而且还成为通缉犯……\x02",
        )
    )

    CloseMessageWindow()

    #C0318
    ChrTalk(
        0x18,
        (
            "如果不靠这种方式\x01",
            "赚点小钱，\x01",
            "生意可就没法做下去了。\x02",
        )
    )

    CloseMessageWindow()

    #C0319
    ChrTalk(
        0x104,
        (
            "#00303F哼……你还有另一个\x01",
            "更重要的理由吧？\x02\x03",

            "#00301F我们已经知道了，\x01",
            "你就是『赤色星座』的\x01",
            "专属商人或资金周转人。\x02\x03",

            "那些家伙在克洛斯贝尔\x01",
            "干了那种事，所以你也\x01",
            "没法继续待下去了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0320
    ChrTalk(
        0x18,
        "……呵呵，随你们想象吧。\x02",
    )

    CloseMessageWindow()
    OP_29(0x93, 0x1, 0x5)
    Jump("loc_84A3")

    label("loc_81E9")


    #N0321
    NpcTalk(
        0x18,
        "商人装扮的男人",
        "哎呀，几位是……？\x02",
    )

    CloseMessageWindow()

    #C0322
    ChrTalk(
        0x101,
        (
            "#00001F我们是克洛斯贝尔警察局\x01",
            "特别任务支援科的成员。\x02\x03",

            "不好意思……\x01",
            "您可以报上自己的\x01",
            "姓名与身份吗？\x02",
        )
    )

    CloseMessageWindow()

    #N0323
    NpcTalk(
        0x18,
        "商人装扮的男人",
        (
            "唔……原来各位是警察啊，\x01",
            "这可真是失礼了。\x02",
        )
    )

    CloseMessageWindow()

    #N0324
    NpcTalk(
        0x18,
        "商人装扮的男人",
        (
            "我的名字是敏涅斯……\x01",
            "只是个不值一提的帝国商人。\x02",
        )
    )

    CloseMessageWindow()

    #C0325
    ChrTalk(
        0x18,
        (
            "现在正打算前往\x01",
            "共和国商谈生意……\x01",
            "各位找我有什么事吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0326
    ChrTalk(
        0x104,
        "#00306F哎呀呀，装得还真是像模像样。\x02",
    )

    CloseMessageWindow()

    #C0327
    ChrTalk(
        0x102,
        (
            "#00103F您涉嫌在空港\x01",
            "骗取医疗物资。\x02\x03",

            "#00101F不好意思，可以让我们\x01",
            "检查一下您车上的货物吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0328
    ChrTalk(
        0x18,
        (
            "唔，这辆运输车上装载的\x01",
            "确实是医疗物资……\x02",
        )
    )

    CloseMessageWindow()

    #C0329
    ChrTalk(
        0x18,
        "但这全都是我自己的货物哦。\x02",
    )

    CloseMessageWindow()

    #C0330
    ChrTalk(
        0x18,
        (
            "莫非各位找到了\x01",
            "我骗取医疗物资的证据？\x02",
        )
    )

    CloseMessageWindow()

    #C0331
    ChrTalk(
        0x105,
        (
            "#10304F呵呵，你是想\x01",
            "装傻到底吗？\x02\x03",

            "#10302F我们只要去找利卡尔德先生对质一下，\x01",
            "你就再也无法抵赖了。\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x93, 0x1, 0x6)

    label("loc_84A3")


    #C0332
    ChrTalk(
        0x103,
        (
            "#00203F……时间宝贵，\x01",
            "我们强行把他带走吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0333
    ChrTalk(
        0x101,
        "#00001F是啊……看来也只能这么办了。\x02",
    )

    CloseMessageWindow()

    #C0334
    ChrTalk(
        0x18,
        (
            "哎呀，好可怕。\x01",
            "多么野蛮的一群人啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0335
    ChrTalk(
        0x18,
        (
            "既然如此……\x01",
            "我也只能赶紧开溜了。\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0x7D0)
    Sound(464, 0, 100, 0)
    OP_74(0xB, 0x1E)
    OP_71(0xB, 0x1, 0x3C, 0x1, 0x8)
    OP_93(0x18, 0x10E, 0x1F4)
    Sleep(500)

    def lambda_8576():
        OP_95(0x18, -23800, 0, -11450, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_8576)
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

    def lambda_8630():
        OP_A7(0x18, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_8630)
    OP_95(0x18, -23000, 600, -11450, 2000, 0x0)

    #C0336
    ChrTalk(
        0x101,
        "#00007F#11A等、等等……！\x02",
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

    def lambda_86C5():
        OP_95(0x101, -23500, 0, -11450, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_86C5)

    def lambda_86DF():
        OP_95(0x102, -23230, 0, -10150, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_86DF)

    def lambda_86F9():
        OP_95(0x103, -23500, 0, -12750, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_86F9)

    def lambda_8713():
        OP_95(0x104, -24950, 0, -11450, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_8713)

    def lambda_872D():
        OP_95(0x105, -24550, 0, -10200, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_872D)

    def lambda_8747():
        OP_95(0x109, -24550, 0, -12750, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_8747)
    WaitChrThread(0x109, 1)

    def lambda_8765():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_8765)

    def lambda_8772():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_8772)

    def lambda_877F():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_877F)

    def lambda_878C():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_878C)

    def lambda_8799():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_8799)

    def lambda_87A6():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_87A6)
    Sleep(500)

    #C0337
    ChrTalk(
        0x109,
        (
            "#10107F罗伊德警官，\x01",
            "我们驾车追上去吧！\x02",
        )
    )

    CloseMessageWindow()

    #C0338
    ChrTalk(
        0x101,
        "#00001F嗯……！\x02",
    )

    CloseMessageWindow()

    def lambda_87F7():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_87F7)
    Sleep(50)

    def lambda_8807():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_8807)
    Sleep(50)

    def lambda_8817():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_8817)
    Sleep(50)

    def lambda_8827():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_8827)
    Sleep(50)

    def lambda_8837():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_8837)
    Sleep(50)

    def lambda_8847():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_8847)
    WaitChrThread(0x101, 1)

    def lambda_8858():
        OP_95(0x101, -32250, 0, -8230, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8858)
    WaitChrThread(0x102, 1)

    def lambda_8876():
        OP_95(0x102, -31980, 0, -6900, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8876)
    WaitChrThread(0x103, 1)

    def lambda_8894():
        OP_95(0x103, -31690, 0, -9430, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_8894)
    WaitChrThread(0x104, 1)

    def lambda_88B2():
        OP_95(0x104, -33590, 0, -6950, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_88B2)
    WaitChrThread(0x105, 1)

    def lambda_88D0():
        OP_95(0x105, -33500, 0, -5480, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_88D0)
    WaitChrThread(0x109, 1)

    def lambda_88EE():
        OP_95(0x109, -33500, 0, -9430, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_88EE)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    ClearChrFlags(0x9, 0x80)
    SetScenarioFlags(0x22, 0)
    NewScene("t2510", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_34_7A5A end

    def Function_35_8923(): pass

    label("Function_35_8923")

    SetChrPos(0xFE, -22290, 0, -12240, 0)
    OP_9F(0x0, 0xFE)
    OP_9F(0x1, -24290, 0, -4000)
    OP_9F(0x1, -23290, 0, -2000)
    OP_9F(0x1, -21000, 0, 0)
    OP_9F(0x1, -18290, 0, 0)
    OP_9F(0x1, 290, 0, 0)
    OP_9F(0x2, 0xFE, 6500, 0x6)
    Return()

    # Function_35_8923 end

    def Function_36_8988(): pass

    label("Function_36_8988")

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
            "卡尔瓦德共和国方向边境\x01",
            "    『唐古拉姆门』\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    EventEnd(0x3)
    Return()

    # Function_36_8988 end

    SaveToFile()

Try(main)
