from ScenarioHelper import *

def main():
    CreateScenaFile(
        "r0200.bin",                # FileName
        "r0200",                    # MapName
        "r0200",                    # Location
        0x00A5,                     # MapIndex
        "ed7121",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x34,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 460, 0, 34470, 180, 0, 1, 1, 0, 1, 0, 2],
    )

    BuildStringList((
        "r0200",                  # 0
        "彼德",                   # 1
        "克潘",                   # 2
        "赛尔丹分部长",           # 3
        "雷克罗德Ⅲ世",           # 4
        "『龙宫』辉夜",           # 5
        "费瑟尔团长",             # 6
        "幻兽",                   # 7
        "幻兽",                   # 8
        "幻兽",                   # 9
        "br0200",                 # 10
    ))

    ATBonus("ATBonus_40C", 100, 5, 0, 5, 0, 5, 0, 2, 5, 0, 0, 0, 2, 0, 0, 0)

    MonsterBattlePostion("MonsterBattlePostion_4CC", 8, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_4D0", 3, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_4D4", 13, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_4D8", 2, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_4DC", 14, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_4E0", 2, 8, 135)
    MonsterBattlePostion("MonsterBattlePostion_4E4", 14, 8, 225)
    MonsterBattlePostion("MonsterBattlePostion_4E8", 0, 0, 180)

    # monster count: 0

    # event battle count: 2

    BattleInfo(
        "BattleInfo_4EC", 0x0042, 255, 6, 45, 10, 1, 30, 0, "br0200", 0x00000000, 100, 0, 0, 0,
        (
            ("ms88700.dat", "ms88800.dat", "ms88800.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_4CC", "MonsterBattlePostion_4CC", "ed7454", "ed7453", "ATBonus_40C"),
            (),
            (),
            (),
        )
    )

    AddCharChip((
        "chr/ch24200.itc",                   # 00
        "chr/ch23600.itc",                   # 01
        "chr/ch32200.itc",                   # 02
        "apl/ch50166.itc",                   # 03
        "chr/ch45600.itc",                   # 04
        "apl/ch51009.itc",                   # 05
    ))

    DeclNpc(17129,   0,       -10449,  0,    261,  0x0, 0,   0,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(28979,   0,       4010,    0,    277,  0x0, 0,   3,   0,   255, 255, 0,   5,   255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   2,   0,   0,   0,   0,   3,   255,  0)
    DeclNpc(17819,   0,       -10109,  270,  389,  0x0, 0,   4,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(29600,   9,       1799,    90,   407,  0x0, 0,   5,   0,   255, 255, 0,   8,   255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 16,  92.0,                  0.0,                   0.0,                   256.0,                 [0.25,                 -0.0,                  0.0,                   0.0,                   -0.0,                  0.125,                 -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -23.0,                 -0.0,                  -0.0,                  1.0])
    DeclEvent(0x0040, 0, 17,  113.4000015258789,     3.7699999809265137,    0.0,                   14.0625,               [0.13333334028720856,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.13333334028720856,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.10000000149011612,   0.0,                   -15.120000839233398,   -0.502666711807251,    -0.0,                  1.0])
    DeclEvent(0x0000, 0, 21,  24.670000076293945,    -12.6899995803833,     -0.5,                  4.0,                   [-0.17677687108516693, 0.7071061134338379,    0.0,                   0.0,                   -0.17677652835845947,  -0.7071074843406677,   0.0,                   0.0,                   0.0,                   -0.0,                  0.5,                   0.0,                   2.1177914142608643,    -26.41750144958496,    0.25,                  1.0])
    DeclEvent(0x0000, 0, 10,  88.0,                  0.6000000238418579,    0.0,                   256.0,                 [0.25,                 -0.0,                  0.0,                   0.0,                   -0.0,                  0.125,                 -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -22.0,                 -0.07500000298023224,  -0.0,                  1.0])

    DeclActor(119750,  0,       2850,    2000,    119750,  1000,    2850,    0x007C, 0,  9,  0x0000)
    DeclActor(29650,   0,       210,     1200,    37690,   -1000,   1900,    0x007C, 0,  11, 0x0000)
    DeclActor(39850,   0,       -14060,  1000,    39850,   1000,    -14060,  0x007C, 0,  12, 0x0000)
    DeclActor(-4059,   0,       -1690,   1500,    -4059,   2000,    -1690,   0x007C, 0,  13, 0x0000)
    DeclActor(102780,  0,       1670,    1500,    102780,  2000,    1670,    0x007C, 0,  13, 0x0000)

    ChipFrameInfo(1428, 0)                                       # 0

    ScpFunction((
        "Function_0_594",          # 00, 0
        "Function_1_644",          # 01, 1
        "Function_2_D8C",          # 02, 2
        "Function_3_1104",         # 03, 3
        "Function_4_1324",         # 04, 4
        "Function_5_1C6E",         # 05, 5
        "Function_6_2135",         # 06, 6
        "Function_7_21DF",         # 07, 7
        "Function_8_232A",         # 08, 8
        "Function_9_23D7",         # 09, 9
        "Function_10_2475",        # 0A, 10
        "Function_11_2563",        # 0B, 11
        "Function_12_262B",        # 0C, 12
        "Function_13_2659",        # 0D, 13
        "Function_14_2986",        # 0E, 14
        "Function_15_2A1A",        # 0F, 15
        "Function_16_2BD7",        # 10, 16
        "Function_17_3348",        # 11, 17
        "Function_18_37AD",        # 12, 18
        "Function_19_3FAE",        # 13, 19
        "Function_20_50EA",        # 14, 20
        "Function_21_53AF",        # 15, 21
        "Function_22_5D39",        # 16, 22
        "Function_23_676C",        # 17, 23
        "Function_24_6DA0",        # 18, 24
    ))


    def Function_0_594(): pass

    label("Function_0_594")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_5CC"),
        (1, "loc_5D8"),
        (2, "loc_5E4"),
        (3, "loc_5F0"),
        (4, "loc_5FC"),
        (5, "loc_608"),
        (6, "loc_614"),
        (SWITCH_DEFAULT, "loc_620"),
    )


    label("loc_5CC")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_62C")

    label("loc_5D8")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_62C")

    label("loc_5E4")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_62C")

    label("loc_5F0")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_62C")

    label("loc_5FC")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_62C")

    label("loc_608")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_62C")

    label("loc_614")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_62C")

    label("loc_620")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_62C")

    label("loc_62C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_643")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_62C")

    label("loc_643")

    Return()

    # Function_0_594 end

    def Function_1_644(): pass

    label("Function_1_644")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AE8")
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
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6D1")
    SetScenarioFlags(0x38, 0)

    label("loc_6D1")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6E7")
    SetScenarioFlags(0x38, 1)

    label("loc_6E7")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6FD")
    SetScenarioFlags(0x38, 2)

    label("loc_6FD")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_713")
    SetScenarioFlags(0x38, 3)

    label("loc_713")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_729")
    SetScenarioFlags(0x38, 4)

    label("loc_729")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_73F")
    SetScenarioFlags(0x38, 5)

    label("loc_73F")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_755")
    SetScenarioFlags(0x38, 6)

    label("loc_755")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_76B")
    SetScenarioFlags(0x38, 7)

    label("loc_76B")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_781")
    SetScenarioFlags(0x39, 0)

    label("loc_781")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_797")
    SetScenarioFlags(0x39, 1)

    label("loc_797")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7AD")
    SetScenarioFlags(0x39, 2)

    label("loc_7AD")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7C3")
    SetScenarioFlags(0x39, 3)

    label("loc_7C3")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7D9")
    SetScenarioFlags(0x39, 4)

    label("loc_7D9")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7EF")
    SetScenarioFlags(0x39, 5)

    label("loc_7EF")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_805")
    SetScenarioFlags(0x39, 6)

    label("loc_805")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_81B")
    SetScenarioFlags(0x39, 7)

    label("loc_81B")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_831")
    SetScenarioFlags(0x3A, 0)

    label("loc_831")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_847")
    SetScenarioFlags(0x3A, 1)

    label("loc_847")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_85D")
    SetScenarioFlags(0x3A, 2)

    label("loc_85D")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_873")
    SetScenarioFlags(0x3A, 3)

    label("loc_873")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_889")
    SetScenarioFlags(0x3A, 4)

    label("loc_889")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_89F")
    SetScenarioFlags(0x3A, 5)

    label("loc_89F")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8B5")
    SetScenarioFlags(0x3A, 6)

    label("loc_8B5")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8CB")
    SetScenarioFlags(0x3A, 7)

    label("loc_8CB")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8E1")
    SetScenarioFlags(0x3B, 0)

    label("loc_8E1")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8F7")
    SetScenarioFlags(0x3B, 1)

    label("loc_8F7")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_90D")
    SetScenarioFlags(0x3B, 2)

    label("loc_90D")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_923")
    SetScenarioFlags(0x3B, 3)

    label("loc_923")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_939")
    SetScenarioFlags(0x3B, 4)

    label("loc_939")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_94F")
    SetScenarioFlags(0x3B, 5)

    label("loc_94F")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_965")
    SetScenarioFlags(0x3B, 6)

    label("loc_965")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_97B")
    SetScenarioFlags(0x3B, 7)

    label("loc_97B")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_991")
    SetScenarioFlags(0x3D, 5)

    label("loc_991")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9A7")
    SetScenarioFlags(0x3D, 6)

    label("loc_9A7")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9BD")
    SetScenarioFlags(0x3D, 7)

    label("loc_9BD")

    ClearScenarioFlags(0x3C, 0)
    ClearScenarioFlags(0x3C, 1)
    ClearScenarioFlags(0x3C, 2)
    ClearScenarioFlags(0x3C, 3)
    ClearScenarioFlags(0x3C, 4)
    ClearScenarioFlags(0x3C, 5)
    ClearScenarioFlags(0x3C, 6)
    ClearScenarioFlags(0x3C, 7)
    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9F8")
    SetScenarioFlags(0x3C, 0)
    Jump("loc_AE8")

    label("loc_9F8")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A1B")
    SetScenarioFlags(0x3C, 1)
    Jump("loc_AE8")

    label("loc_A1B")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A3E")
    SetScenarioFlags(0x3C, 2)
    Jump("loc_AE8")

    label("loc_A3E")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A61")
    SetScenarioFlags(0x3C, 3)
    Jump("loc_AE8")

    label("loc_A61")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A84")
    SetScenarioFlags(0x3C, 4)
    Jump("loc_AE8")

    label("loc_A84")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AA7")
    SetScenarioFlags(0x3C, 5)
    Jump("loc_AE8")

    label("loc_AA7")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_ACA")
    SetScenarioFlags(0x3C, 6)
    Jump("loc_AE8")

    label("loc_ACA")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AE8")
    SetScenarioFlags(0x3C, 7)

    label("loc_AE8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2F, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_AFE")
    OP_50(0x1E, (scpexpr(EXPR_PUSH_LONG, 0x34), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_AFE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B30")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B30")
    SetChrPos(0x0, -2090, 0, -1280, 89)
    OP_31(0x1)
    OP_69(0xFF, 0x0)
    Event(0, 14)

    label("loc_B30")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_END)), "loc_B63")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B63")
    SetChrPos(0x0, 102780, 0, 1670, 270)
    OP_31(0x1)
    OP_69(0xFF, 0x0)
    ClearMapFlags(0x8000000)

    label("loc_B63")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_BAF")
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 16430, 0, -10160, 90)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B9B")
    SetChrFlags(0xB, 0x10)
    SetChrFlags(0xA, 0x10)

    label("loc_B9B")

    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    Jump("loc_D4E")

    label("loc_BAF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_BC7")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    Jump("loc_D4E")

    label("loc_BC7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_BD5")
    Jump("loc_D4E")

    label("loc_BD5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_BE3")
    Jump("loc_D4E")

    label("loc_BE3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_BF6")
    SetChrFlags(0x8, 0x80)
    Jump("loc_D4E")

    label("loc_BF6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_C04")
    Jump("loc_D4E")

    label("loc_C04")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_C12")
    Jump("loc_D4E")

    label("loc_C12")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_CCF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17A, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C75")
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 39460, 0, -14300, 270)
    SetChrPos(0x8, 38260, 0, -13900, 135)
    SetChrChipByIndex(0x9, 0x1)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x10)
    SetChrPos(0x9, 38260, 0, -15100, 45)
    BeginChrThread(0x9, 0, 0, 0)
    Jump("loc_CCA")

    label("loc_C75")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17A, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CCA")
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 34370, 0, -14100, 225)
    SetChrPos(0x8, 33010, 0, -14380, 90)
    SetChrChipByIndex(0x9, 0x1)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x10)
    SetChrPos(0x9, 33520, 0, -15630, 0)
    BeginChrThread(0x9, 0, 0, 0)

    label("loc_CCA")

    Jump("loc_D4E")

    label("loc_CCF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_CDD")
    Jump("loc_D4E")

    label("loc_CDD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_CEB")
    Jump("loc_D4E")

    label("loc_CEB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_D23")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D0D")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    Jump("loc_D1E")

    label("loc_D0D")

    SetChrPos(0x8, 7910, 0, -5530, 90)

    label("loc_D1E")

    Jump("loc_D4E")

    label("loc_D23")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_D3B")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    Jump("loc_D4E")

    label("loc_D3B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_D4E")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)

    label("loc_D4E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_D62")
    ClearScenarioFlags(0x22, 0)
    Event(0, 18)
    Jump("loc_D71")

    label("loc_D62")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_D71")
    ClearScenarioFlags(0x22, 1)
    Event(0, 24)

    label("loc_D71")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17A, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D8B")
    Event(0, 22)

    label("loc_D8B")

    Return()

    # Function_1_644 end

    def Function_2_D8C(): pass

    label("Function_2_D8C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_END)), "loc_DA3")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0xFB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_DF6")

    label("loc_DA3")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_DCD")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x23D), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_DF6")

    label("loc_DCD")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_DF6")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x79), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_DF6")

    SoundDistance(0x7B, 0x230A, 0x0, 0xFFFF7356, 0x3A98, 0xC350, 0x64, 0x0)
    OP_E3(0x73AA, 0x96, 0xFFFFE840)
    OP_E3(0x1DC9A, 0x0, 0x4A38)
    LoadEffect(0xF, "eff\\mgm03_02.eff")
    PlayEffect(0xF, 0x8, 0xFF, 0x0, 37690, -1000, 1900, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_F16")
    LoadEffect(0x9, "map/mprain00.eff")
    PlayEffect(0x9, 0x7, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 1000)
    SetMapObjFrame(0xFF, "sky", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x0, 0x1)
    OP_7D(0xB4, 0xB4, 0xB4, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0xD, 0x78, 0x0)
    Sound(128, 1, 100, 0)
    Jump("loc_F2E")

    label("loc_F16")

    SetMapObjFrame(0xFF, "sky1", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky2", 0x0, 0x1)

    label("loc_F2E")

    SetMapObjFlags(0x2, 0x4)
    SetMapObjFlags(0x9, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_END)), "loc_F6E")
    SetMapObjFrame(0xFF, "sky", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x0, 0x1)
    OP_7D(0xDC, 0xEB, 0xFF, 0x0, 0x0)
    ClearMapObjFlags(0x9, 0x4)
    Jump("loc_FA1")

    label("loc_F6E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 3)), scpexpr(EXPR_END)), "loc_F92")
    ClearMapObjFlags(0x2, 0x4)
    SetMapObjFrame(0x2, "flower04", 0x0, 0x1)
    Jump("loc_FA1")

    label("loc_F92")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_FA1")
    ClearMapObjFlags(0x2, 0x4)

    label("loc_FA1")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_FC2")
    SetMapObjFrame(0xFF, "turi00", 0x0, 0x1)
    Jump("loc_FD0")

    label("loc_FC2")

    SetMapObjFrame(0xFF, "turi01", 0x0, 0x1)

    label("loc_FD0")

    MiniGame(0x2F, 0x3, 0x4, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_100A")
    ClearMapFlags(0x2000)
    Jump("loc_100F")

    label("loc_100A")

    SetMapFlags(0x2000)

    label("loc_100F")

    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1027")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_1027")

    ModifyEventFlags(0, 2, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17A, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1044")
    ModifyEventFlags(1, 2, 0x80)

    label("loc_1044")

    OP_65(0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_105F")
    OP_66(0x0, 0x1)

    label("loc_105F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 1)), scpexpr(EXPR_END)), "loc_1089")
    SetChrFlags(0xE, 0x80)
    SetMapObjFlags(0x5, 0x4)
    SetMapObjFlags(0x6, 0x4)
    SetMapObjFlags(0x7, 0x4)
    ModifyEventFlags(0, 1, 0x80)
    Jump("loc_10BC")

    label("loc_1089")

    ClearChrFlags(0xE, 0x80)
    ClearMapObjFlags(0x5, 0x4)
    OP_78(0x5, 0xE)
    SetMapObjFlags(0x6, 0x4)
    SetMapObjFlags(0x7, 0x4)
    SetChrPos(0xE, 113400, 0, 3770, 180)
    OP_93(0xE, 0x10E, 0x0)

    label("loc_10BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17A, 0)), scpexpr(EXPR_END)), "loc_10D8")
    ClearMapObjFlags(0x0, 0x10)
    OP_70(0x0, 0xA)
    OP_65(0x2, 0x1)
    Jump("loc_10E2")

    label("loc_10D8")

    ClearMapObjFlags(0x0, 0x10)
    OP_66(0x2, 0x1)

    label("loc_10E2")

    ModifyEventFlags(0, 3, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1103")
    ModifyEventFlags(1, 3, 0x80)

    label("loc_1103")

    Return()

    # Function_2_D8C end

    def Function_3_1104(): pass

    label("Function_3_1104")

    TalkBegin(0xFE)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1111")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1320")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1138")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_117E")

    label("loc_1138")

    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "对话\x01",      # 0
            "购物\x01",      # 1
            "放弃\x01",      # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_117E")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jump("loc_117E")

    label("loc_117E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11AE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x190, 5)), scpexpr(EXPR_END)), "loc_119D")
    OP_AF(0x37)
    Jump("loc_119F")

    label("loc_119D")

    OP_AF(0x36)

    label("loc_119F")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_131B")

    label("loc_11AE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_131B")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_12AF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11E2")
    Call(0, 7)
    Jump("loc_12A0")

    label("loc_11E2")


    #C0001
    ChrTalk(
        0xA,
        (
            "话说回来……居然在这种小屋里\x01",
            "生活了将近一个月，\x01",
            "意志还真是坚强啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0xA,
        (
            "看来他们平时都是靠晒鱼干、\x01",
            "采摘可食用野草等手段\x01",
            "来解决温饱问题的……\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0xA,
        "真是的，这种毅力真是让人不得不敬佩啊。\x02",
    )

    CloseMessageWindow()

    label("loc_12A0")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_131B")

    label("loc_12AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_131B")
    TurnDirection(0xFE, 0x101, 0)

    #C0004
    ChrTalk(
        0xFE,
        "罗伊德团员，你们可要小心点哦。\x02",
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0xFE,
        (
            "我们会在这里\x01",
            "等着各位的，\x01",
            "幻兽的问题就交给你们了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_131B")

    Jump("loc_1111")

    label("loc_1320")

    TalkEnd(0xFE)
    Return()

    # Function_3_1104 end

    def Function_4_1324(): pass

    label("Function_4_1324")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x191, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x190, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_135D")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x344, 0x0)"), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x344, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x344, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x344, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_135D")
    Call(0, 23)
    Return()

    label("loc_135D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1698")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x344, 0x0)"), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x344, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x344, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x344, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1391")
    Jump("loc_1698")

    label("loc_1391")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x344, 0x0)"), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x344, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x344, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x344, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1698")
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x8, 0x101, 500)

    #C0006
    ChrTalk(
        0xFE,
        "罗伊德，这是……\x02",
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x101,
        (
            "#00004F嗯，我想应该\x01",
            "是钓具的部件，\x01",
            "还真是漂亮呢。\x02\x03",

            "#00000F我在从四天王手中夺回的垂钓场所\x01",
            "钓到了很罕见的鱼……\x01",
            "这就是那条鱼吐出来的。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0xFE,
        "……不会有错的。\x02",
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0xFE,
        (
            "这就是过去某位飘泊的钓鱼大师\x01",
            "所使用过的传说钓具的部件。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0xFE,
        (
            "听说他在离开克洛斯贝尔的时候，\x01",
            "将这套钓具\x01",
            "封存在了这片土地上……\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0xFE,
        (
            "没想到……竟然会以\x01",
            "这样的形式再现于世！\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x101,
        (
            "#00005F是、是那么\x01",
            "珍贵的东西吗……\x02\x03",

            "#00003F那该怎么办呢？\x01",
            "还是交还给那个人为好吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0xFE,
        "不，没有那个必要。\x02",
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0xFE,
        (
            "……因为他曾经说过，\x01",
            "这套钓具就送给找到它的人使用。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0xFE,
        (
            "罗伊德，\x01",
            "这套钓具的部件共有四个。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0xFE,
        (
            "如果你获得了所有部件，\x01",
            "请务必拿到我这里来。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0xFE,
        (
            "我应该可以把那些部件\x01",
            "重新组合起来。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x101,
        (
            "#00012F原、原来如此……\x01",
            "明白了，我会留心的。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    SetScenarioFlags(0x1C0, 1)
    TalkEnd(0xFE)
    Return()

    label("loc_1698")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1707")
    TurnDirection(0xFE, 0x101, 0)

    #C0019
    ChrTalk(
        0xFE,
        (
            "已被封存多年的传说钓具\x01",
            "居然会在这种时候出现……\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0xFE,
        (
            "唔，罗伊德，\x01",
            "也许这就是命运吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C6A")

    label("loc_1707")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_1715")
    Jump("loc_1C6A")

    label("loc_1715")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_18BC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x191, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1839")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x190, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17E9")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x344, 0x0)"), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x344, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x344, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x344, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1754")
    Jump("loc_17E4")

    label("loc_1754")


    #C0021
    ChrTalk(
        0xFE,
        (
            "哎呀，居然能见到那位传说中的人物，\x01",
            "我兴奋得简直有些不知所措。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0xFE,
        (
            "呵呵呵，钓皇俱乐部的各位啊，\x01",
            "要得意就趁现在吧，你们马上就要笑不出来了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17E4")

    Jump("loc_1834")

    label("loc_17E9")

    TurnDirection(0xFE, 0x101, 0)

    #C0023
    ChrTalk(
        0xFE,
        (
            "罗伊德，用那把水中支配者\x01",
            "把雷克罗德彻底打败吧！\x01",
            "……拜托你了！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1834")

    Jump("loc_18B7")

    label("loc_1839")

    TurnDirection(0xFE, 0x101, 0)

    #C0024
    ChrTalk(
        0xFE,
        (
            "『钓皇杀手』罗伊德大师，\x01",
            "你这次的表现非常出色，\x01",
            "请容我在此表示感谢。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0xFE,
        (
            "呵呵呵，这场爆钓比赛\x01",
            "一定会名流千古的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18B7")

    Jump("loc_1C6A")

    label("loc_18BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_18CA")
    Jump("loc_1C6A")

    label("loc_18CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_18D8")
    Jump("loc_1C6A")

    label("loc_18D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_18E6")
    Jump("loc_1C6A")

    label("loc_18E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1946")

    #C0026
    ChrTalk(
        0xFE,
        (
            "分部长和克潘挑战了那么多次，\x01",
            "竟然还是赢不了……\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0xFE,
        (
            "简直就像在做\x01",
            "噩梦一样。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C6A")

    label("loc_1946")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1AD2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17A, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19D0")

    #C0028
    ChrTalk(
        0xFE,
        (
            "各位能来这里，\x01",
            "真是让我发自内心地松了一口气。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0xFE,
        (
            "我从昨天开始就一直在担心，\x01",
            "怕那东西什么时候突然过来袭击。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1ACD")

    label("loc_19D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A67")

    #C0030
    ChrTalk(
        0xFE,
        (
            "好，我要开始\x01",
            "继续修行了。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0xFE,
        (
            "到现在为止，还没能战胜四天王中\x01",
            "任意一人的就只有我了……\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0xFE,
        (
            "差不多也该认真起来，\x01",
            "洗去这污名了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1ACD")

    label("loc_1A67")


    #C0033
    ChrTalk(
        0xFE,
        (
            "到现在为止，还没能战胜四天王中\x01",
            "任意一人的就只有我了……\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0xFE,
        (
            "差不多也该认真起来，\x01",
            "洗去这污名了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1ACD")

    Jump("loc_1C6A")

    label("loc_1AD2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1B42")

    #C0035
    ChrTalk(
        0xFE,
        (
            "克潘……\x01",
            "竟然钓到了那么多\x01",
            "梦幻之鱼锦鲤。\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0xFE,
        (
            "唔，这就是努力\x01",
            "修行的成果啊。\x01",
            "我也不能输给他。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C6A")

    label("loc_1B42")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1BD6")

    #C0037
    ChrTalk(
        0xFE,
        (
            "好……为了派上一点用场，\x01",
            "我也要好好磨练\x01",
            "自己的钓技。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0xFE,
        (
            "至少也得达到『专业钓师』的\x01",
            "级别才行，不然都没法在这种\x01",
            "野外环境下生存。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C6A")

    label("loc_1BD6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1C53")

    #C0039
    ChrTalk(
        0xFE,
        (
            "无论如何……\x01",
            "我们也要把钓公师团的招牌\x01",
            "重新挂到原事务所的门外。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0xFE,
        (
            "如果再这样下去，\x01",
            "我们就没脸见团长了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C6A")

    label("loc_1C53")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_1C61")
    Jump("loc_1C6A")

    label("loc_1C61")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_1C6A")

    label("loc_1C6A")

    TalkEnd(0xFE)
    Return()

    # Function_4_1324 end

    def Function_5_1C6E(): pass

    label("Function_5_1C6E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_1C7F")
    Jump("loc_2131")

    label("loc_1C7F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1D38")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x191, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CE5")

    #C0041
    ChrTalk(
        0xFE,
        (
            "钓公师团的\x01",
            "超级秘密武器吗……\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0xFE,
        (
            "我还没见过呢，\x01",
            "到底是个什么样的人呢～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D33")

    label("loc_1CE5")


    #C0043
    ChrTalk(
        0xFE,
        (
            "好～\x01",
            "我也绝不能输的说！\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0xFE,
        (
            "总有一天，\x01",
            "要向钓皇俱乐部报那一箭之仇的说！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D33")

    Jump("loc_2131")

    label("loc_1D38")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_1D46")
    Jump("loc_2131")

    label("loc_1D46")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1D9E")

    #C0045
    ChrTalk(
        0xFE,
        (
            "我应该……\x01",
            "应该能变得更强的说！\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0xFE,
        (
            "好不甘心……\x01",
            "真的好不甘心的说！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2131")

    label("loc_1D9E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_1DAC")
    Jump("loc_2131")

    label("loc_1DAC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1E1E")

    #C0047
    ChrTalk(
        0xFE,
        (
            "呜呜……不管挑战多少次，\x01",
            "我也赢不了『龙宫』的说！\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0xFE,
        (
            "我到底……\x01",
            "到底什么地方做得不对的说！？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2131")

    label("loc_1E1E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1EE1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17A, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E92")

    #C0049
    ChrTalk(
        0xFE,
        (
            "话说回来，那只怪物\x01",
            "真是越看越诡异的说。\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0xFE,
        (
            "而且体型还那么巨大……\x01",
            "真是的，饶了我吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1EDC")

    label("loc_1E92")


    #C0051
    ChrTalk(
        0xFE,
        "好，我得把耽误的修行给补回来的说～\x02",
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0xFE,
        "我的目标是『龙宫杀手』的说！\x02",
    )

    CloseMessageWindow()

    label("loc_1EDC")

    Jump("loc_2131")

    label("loc_1EE1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1FCD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F69")

    #C0053
    ChrTalk(
        0xFE,
        (
            "哇，又钓到了\x01",
            "锦鲤的说。\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0xFE,
        (
            "这种鱼在克洛斯贝尔\x01",
            "应该相当罕见的说……\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0xFE,
        (
            "唔～但总觉得\x01",
            "有点不对劲的说。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1FC8")

    label("loc_1F69")


    #C0056
    ChrTalk(
        0xFE,
        (
            "和以前相比，\x01",
            "锦鲤的数量\x01",
            "似乎变多了……\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0xFE,
        (
            "难道克洛斯贝尔的生态环境\x01",
            "出现了什么问题的说？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1FC8")

    Jump("loc_2131")

    label("loc_1FCD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_20CA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2074")

    #C0058
    ChrTalk(
        0xFE,
        "２１３、２１４、２１５……！\x02",
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0xFE,
        (
            "今天也一样，在挂上鱼饵之前，\x01",
            "要先练习空挥钓竿一千次的说！\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0xFE,
        (
            "这项特训很锻炼腕力，\x01",
            "十分不错的说～！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_20C5")

    label("loc_2074")


    #C0061
    ChrTalk(
        0xFE,
        (
            "女神不会对懒惰者\x01",
            "展露微笑的说～！\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0xFE,
        "钓师就得每日坚持不懈地磨练自己的说！\x02",
    )

    CloseMessageWindow()

    label("loc_20C5")

    Jump("loc_2131")

    label("loc_20CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_211A")

    #C0063
    ChrTalk(
        0xFE,
        "好，赶快开始修行钓技的说。\x02",
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0xFE,
        "你们就等着瞧吧，钓皇俱乐部！\x02",
    )

    CloseMessageWindow()
    Jump("loc_2131")

    label("loc_211A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_2128")
    Jump("loc_2131")

    label("loc_2128")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_2131")

    label("loc_2131")

    TalkEnd(0xFE)
    Return()

    # Function_5_1C6E end

    def Function_6_2135(): pass

    label("Function_6_2135")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_21B6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2153")
    Call(0, 7)
    Jump("loc_21B1")

    label("loc_2153")


    #C0065
    ChrTalk(
        0xB,
        (
            "可恶，我明明是他们的敌人，\x01",
            "他为何却表现得\x01",
            "如此友好。\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0xB,
        "我才不会接受这种反常的对待呢！\x02",
    )

    CloseMessageWindow()

    label("loc_21B1")

    Jump("loc_21DB")

    label("loc_21B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_21C4")
    Jump("loc_21DB")

    label("loc_21C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_END)), "loc_21D2")
    Jump("loc_21DB")

    label("loc_21D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_21DB")

    label("loc_21DB")

    TalkEnd(0xFE)
    Return()

    # Function_6_2135 end

    def Function_7_21DF(): pass

    label("Function_7_21DF")

    OP_4B(0xB, 0xFF)
    OP_4B(0xA, 0xFF)

    #C0067
    ChrTalk(
        0xA,
        (
            "雷克罗德，没想到\x01",
            "你居然在这里啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0xB,
        (
            "哼，我们有权随意使用这个小屋，\x01",
            "这可是你自己说的，\x01",
            "现在可别再诸多怨言哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0xA,
        "当然不会，原本就是这样约定的。\x02",
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0xA,
        (
            "但在这里会有诸多不便吧？\x01",
            "如果有需要，你们随时\x01",
            "都可以到分部来哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xB)

    #C0071
    ChrTalk(
        0xB,
        (
            "哼、哼……\x01",
            "我们还没有落魄到需要\x01",
            "你们同情的程度。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    ClearChrFlags(0xB, 0x10)
    ClearChrFlags(0xA, 0x10)
    OP_4C(0xB, 0xFF)
    OP_4C(0xA, 0xFF)
    Return()

    # Function_7_21DF end

    def Function_8_232A(): pass

    label("Function_8_232A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_23AE")

    #C0072
    ChrTalk(
        0xC,
        (
            "唉……我差点忘了，\x01",
            "这个小屋是那个叫赛尔丹的\x01",
            "男人借给我们的。\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0xC,
        (
            "难得的二人世界被破坏了……\x01",
            "实在是无法原谅！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_23D3")

    label("loc_23AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_23BC")
    Jump("loc_23D3")

    label("loc_23BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_END)), "loc_23CA")
    Jump("loc_23D3")

    label("loc_23CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_23D3")

    label("loc_23D3")

    TalkEnd(0xFE)
    Return()

    # Function_8_232A end

    def Function_9_23D7(): pass

    label("Function_9_23D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 4)), scpexpr(EXPR_END)), "loc_2403")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 6)), scpexpr(EXPR_END)), "loc_23F1")
    Call(0, 20)
    Jump("loc_23FE")

    label("loc_23F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_23FE")
    Call(0, 19)

    label("loc_23FE")

    Jump("loc_2474")

    label("loc_2403")

    EventBegin(0x2)
    SetChrName("")

    #A0074
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "蓝花在地上绽放。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    #C0075
    ChrTalk(
        0x101,
        (
            "#00000F（哦，这花可真漂亮啊，\x01",
            "  还散发着一层淡淡的晕光……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x168, 4)
    EventEnd(0x3)

    label("loc_2474")

    Return()

    # Function_9_23D7 end

    def Function_10_2475(): pass

    label("Function_10_2475")

    EventBegin(0x1)

    #C0076
    ChrTalk(
        0x101,
        (
            "#00003F（虽然已经把两个地点的\x01",
            "  幻兽都消灭了……\x01",
            "  但总觉得有点不对劲。）\x02\x03",

            "#00000F各位，我们不如再去\x01",
            "调查一下现场吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0x102,
        (
            "#00100F说的也是，总觉得还有\x01",
            "值得调查的地方呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0x103,
        "#00200F那就赶快回去，再调查一下吧。\x02",
    )

    CloseMessageWindow()
    SetChrPos(0x0, 91500, 0, 0, 90)
    EventEnd(0x4)
    Return()

    # Function_10_2475 end

    def Function_11_2563(): pass

    label("Function_11_2563")

    EventBegin(0x1)
    #Sound(2094, 255, 100, 0)    #voice#Lloyd

    #C0079
    ChrTalk(
        0x101,
        "#0000F在这里似乎可以钓到鱼呢。\x02",
    )

    CloseMessageWindow()
    OP_68(32130, 1200, -50, 1500)
    MoveCamera(25, 31, 0, 1500)
    OP_6E(600, 1500)
    SetCameraDistance(20500, 1500)
    Sleep(1000)
    SetChrName("")

    #A0080
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "要钓鱼吗？\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "钓鱼\x01",      # 0
            "放弃\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    OP_6F(0x1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2626")
    OP_E2(0x2)
    MiniGame(0x6, 0x18, 0x73D2, 0x0, 0xD2, 0x5A, 0x933A, 0xFFFFFC18, 0x76C)

    label("loc_2626")

    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    # Function_11_2563 end

    def Function_12_262B(): pass

    label("Function_12_262B")

    TalkBegin(0xFF)
    Sound(807, 0, 100, 0)
    SetChrName("")

    #A0081
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "门上挂着坚固的锁。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)
    Return()

    # Function_12_262B end

    def Function_13_2659(): pass

    label("Function_13_2659")

    SetMapFlags(0x80)
    SetMapFlags(0x8000000)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x31, 2)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_268B")
    SetScenarioFlags(0x31, 2)

    label("loc_268B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_26D1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 2)), scpexpr(EXPR_END)), "loc_26CB")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_26C0")
    Sound(2499, 255, 100, 0)    #voice#Noel
    Jump("loc_26C6")

    label("loc_26C0")

    Sound(3537, 255, 100, 0)    #voice#Noel

    label("loc_26C6")

    Jump("loc_26D1")

    label("loc_26CB")

    Sound(3344, 255, 100, 0)    #voice#Lloyd

    label("loc_26D1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2978")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_END)), "loc_2742")
    MenuCmd(0, 0)
    MenuCmd(1, 0, "登上梅尔卡瓦")
    MenuCmd(1, 0, "放弃")
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2722"),
        (SWITCH_DEFAULT, "loc_2733"),
    )


    label("loc_2722")

    SetScenarioFlags(0x22, 0)
    NewScene("e3020", 0, 0, 0)
    IdleLoop()
    Jump("loc_273D")

    label("loc_2733")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_273D")

    Jump("loc_2973")

    label("loc_2742")

    MenuCmd(0, 0)
    MenuCmd(1, 0, "驾驶导力车移动")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_2772")
    MenuCmd(1, 0, "在导力车中休息")

    label("loc_2772")

    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_279C"),
        (1, "loc_28A0"),
        (2, "loc_2931"),
        (SWITCH_DEFAULT, "loc_2969"),
    )


    label("loc_279C")

    SetMapObjFrame(0x8, "light", 0x0, 0x1)
    OP_74(0x8, 0x1E)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_27CD")
    OP_70(0x8, 0x12C)
    OP_71(0x8, 0x12C, 0x14A, 0x0, 0x0)
    Jump("loc_27DD")

    label("loc_27CD")

    OP_70(0x8, 0xF0)
    OP_71(0x8, 0xF0, 0x10E, 0x0, 0x0)

    label("loc_27DD")

    Sound(462, 0, 100, 0)
    SoundLoad(2500)
    SoundLoad(3538)
    SoundLoad(3345)
    Sleep(700)
    FadeToDark(300, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x2E, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2833")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2833")

    FadeToDark(0, 0, -1)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D4, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2856")
    Sound(461, 0, 100, 0)

    label("loc_2856")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2876")
    OP_70(0x8, 0x14A)
    OP_71(0x8, 0x14A, 0x12C, 0x0, 0x0)
    Jump("loc_2886")

    label("loc_2876")

    OP_70(0x8, 0x10E)
    OP_71(0x8, 0x10E, 0xF0, 0x0, 0x0)

    label("loc_2886")

    Sleep(1000)
    OP_0D()
    SetMapObjFrame(0x8, "light", 0x1, 0x1)
    OP_70(0x8, 0x0)
    Jump("loc_26D1")

    label("loc_28A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_2912")
    OP_57(0x0)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_5A()
    Sound(13, 0, 100, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 0)), scpexpr(EXPR_END)), "loc_28D5")
    OP_32(0xFF, 0xFF, 0x0)
    Jump("loc_28ED")

    label("loc_28D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_28E8")
    OP_32(0xFF, 0xFE, 0x0)
    Jump("loc_28ED")

    label("loc_28E8")

    OP_32(0xFF, 0xFA, 0x0)

    label("loc_28ED")

    OP_6A(0x0, 0x0)
    Sleep(3500)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_292C")

    label("loc_2912")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_2922")
    OP_AF(0xFB)
    Jump("loc_292C")

    label("loc_2922")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_292C")

    Jump("loc_2973")

    label("loc_2931")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_294A")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2964")

    label("loc_294A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_295A")
    OP_AF(0xFB)
    Jump("loc_2964")

    label("loc_295A")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2964")

    Jump("loc_2973")

    label("loc_2969")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2973")

    Jump("loc_26D1")

    label("loc_2978")

    ClearMapFlags(0x8000000)
    OP_60(0x0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    # Function_13_2659 end

    def Function_14_2986(): pass

    label("Function_14_2986")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(0, 0, -1)
    Sleep(100)
    Sound(459, 0, 100, 0)
    Sleep(2000)
    StopSound(459, 1000, 100)
    Sound(492, 0, 70, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 2)), scpexpr(EXPR_END)), "loc_29E1")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_29D6")
    Sound(2502, 255, 100, 0)    #voice#Noel
    Jump("loc_29DC")

    label("loc_29D6")

    Sound(2503, 255, 100, 0)    #voice#Noel

    label("loc_29DC")

    Jump("loc_2A05")

    label("loc_29E1")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_29FF")
    Sound(3347, 255, 100, 0)    #voice#Lloyd
    Jump("loc_2A05")

    label("loc_29FF")

    Sound(3348, 255, 100, 0)    #voice#Lloyd

    label("loc_2A05")

    Sleep(500)
    FadeToBright(500, 0)
    OP_0D()
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_14_2986 end

    def Function_15_2A1A(): pass

    label("Function_15_2A1A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_2A24")
    Return()

    label("loc_2A24")

    EventBegin(0x1)
    OP_52(0x0, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x3, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x4, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x5, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x6, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x7, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrSubChip(0x0, 0x0)
    SetChrSubChip(0x1, 0x0)
    SetChrSubChip(0x2, 0x0)
    SetChrSubChip(0x3, 0x0)
    SetChrSubChip(0x4, 0x0)
    SetChrSubChip(0x5, 0x0)
    SetChrSubChip(0x6, 0x0)
    SetChrSubChip(0x7, 0x0)
    SetChrName("")

    #A0082
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "大型魔兽正在四处游荡。\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【消灭】\x01",      # 0
            "【放弃】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (1, "loc_2AF0"),
        (SWITCH_DEFAULT, "loc_2B09"),
    )


    label("loc_2AF0")

    Sleep(500)
    OP_E2(0x2)
    OP_90(0x0, 106900, 0, 4400, 90)
    EventEnd(0x5)
    Return()

    label("loc_2B09")

    Battle("BattleInfo_4EC", 0x0, 0x0, 0x100, 0xC, 0xFF)
    OP_E2(0x2)
    EventBegin(0x1)
    OP_68(106900, 1000, 4400, 0)
    OP_90(0x0, 106900, 0, 4400, 90)
    OP_90(0x1, 106900, 0, 4400, 90)
    OP_90(0x2, 106900, 0, 4400, 90)
    OP_90(0x3, 106900, 0, 4400, 90)
    OP_90(0x4, 106900, 0, 4400, 90)
    OP_90(0x5, 106900, 0, 4400, 90)
    OP_90(0x6, 106900, 0, 4400, 90)
    OP_90(0x7, 106900, 0, 4400, 90)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (2, "loc_2BCB"),
        (1, "loc_2BD0"),
        (SWITCH_DEFAULT, "loc_2BD3"),
    )


    label("loc_2BCB")

    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    label("loc_2BD0")

    OP_B9(0x0)
    Return()

    label("loc_2BD3")

    Call(0, 18)
    Return()

    # Function_15_2A1A end

    def Function_16_2BD7(): pass

    label("Function_16_2BD7")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    OP_68(90650, 1000, 0, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18500, 0)
    OP_68(91800, 1100, 0, 1300)
    SetChrPos(0x101, 92650, 0, 0, 90)
    SetChrPos(0x102, 92200, 0, 900, 90)
    SetChrPos(0x103, 91050, 0, 900, 90)
    SetChrPos(0x104, 90750, 0, 1900, 90)
    SetChrPos(0x109, 91300, 0, -900, 90)
    SetChrPos(0x105, 90300, 0, -500, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    StopBGM(0xFA0)
    FadeToBright(1000, 0)

    def lambda_2CC3():
        OP_9B(0x0, 0x101, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2CC3)
    Sleep(0)

    def lambda_2CDB():
        OP_9B(0x0, 0x102, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_2CDB)
    Sleep(0)

    def lambda_2CF3():
        OP_9B(0x0, 0x103, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_2CF3)
    Sleep(0)

    def lambda_2D0B():
        OP_9B(0x0, 0x104, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_2D0B)
    Sleep(0)

    def lambda_2D23():
        OP_9B(0x0, 0x109, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_2D23)
    Sleep(0)

    def lambda_2D3B():
        OP_9B(0x0, 0x105, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_2D3B)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    OP_0D()
    OP_6F(0x79)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E54")

    #C0083
    ChrTalk(
        0x109,
        "#10111F#6P（啊……！）\x02",
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x101,
        "#00013F#5P（那就是『幻兽』吗……！）\x02",
    )

    CloseMessageWindow()
    Jump("loc_2E8E")

    label("loc_2E54")


    #C0085
    ChrTalk(
        0x105,
        "#10305F#6P（哦……）\x02",
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x101,
        "#00013F#5P（在这里啊……）\x02",
    )

    CloseMessageWindow()

    label("loc_2E8E")

    WaitBGM()
    Sleep(10)
    PlayBGM("ed7573", 0)
    OP_68(114100, 1600, 4200, 3000)
    MoveCamera(55, 12, 0, 3000)
    OP_6E(700, 3000)
    SetCameraDistance(17580, 4000)
    OP_6F(0x79)
    Fade(500)
    OP_68(115110, 1200, 5490, 0)
    MoveCamera(38, 33, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(19330, 0)
    OP_68(115110, 1200, 3580, 5000)
    MoveCamera(90, 16, 0, 5000)
    OP_6E(600, 5000)
    SetCameraDistance(19330, 5000)
    OP_6F(0x79)
    Sleep(300)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3186")

    #C0087
    ChrTalk(
        0x104,
        (
            "#00303F#9P（和报告中提到的一样，相当巨大呢……）\x02\x03",

            "#00301F（阿缇，力场扭曲了吗？）\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0x103,
        (
            "#00203F#9P（时、空、幻……\x01",
            "  这里确实出现了上级三属性。）\x02\x03",

            "#00201F（目前还不清楚发生此现象的原因。）\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0x102,
        "#00108F#9P（是吗……）\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(91800, 1100, 0, 0)
    MoveCamera(45, 26, 0, 0)
    SetCameraDistance(18500, 0)
    OP_6E(500, 0)
    OP_0D()

    def lambda_304F():
        TurnDirection(0x101, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_304F)
    Sleep(0)

    def lambda_305F():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_305F)
    Sleep(0)

    def lambda_306F():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_306F)
    Sleep(0)

    def lambda_307F():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_307F)
    Sleep(0)

    def lambda_308F():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_308F)
    Sleep(0)

    def lambda_309F():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_309F)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    OP_93(0x101, 0x10E, 0x1F4)

    #C0090
    ChrTalk(
        0x105,
        (
            "#10301F#6P（那么……\x01",
            "  我们该怎么办？）\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x101,
        (
            "#00003F#11P（根据警备队的报告来看，\x01",
            "  是相当危险的类型呢……）\x02\x03",

            "#00013F（消灭它的时候一定要多加小心。）\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0x109,
        "#10101F#12P（明白了……！）\x02",
    )

    CloseMessageWindow()
    Jump("loc_330D")

    label("loc_3186")


    #C0093
    ChrTalk(
        0x102,
        (
            "#00101F#9P（缇欧……\x01",
            "  力场的扭曲情况如何？）\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x103,
        (
            "#00203F#9P（这里也出现了上级三属性……）\x02\x03",

            "#00201F（发生此现象的原因仍旧不明。）\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0x104,
        "#00306F#9P（果然如此……）\x02",
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0x105,
        (
            "#10308F#9P（但幻兽似乎并不是\x01",
            "  引发此现象的原因呢……）\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(91800, 1100, 0, 0)
    MoveCamera(45, 26, 0, 0)
    SetCameraDistance(18500, 0)
    OP_6E(500, 0)
    OP_0D()

    #C0097
    ChrTalk(
        0x109,
        (
            "#10101F#6P（罗伊德警官……\x01",
            "  要马上动手把它消灭吗？）\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x101,
        "#00013F#5P（嗯，大家一定要小心行事……！）\x02",
    )

    CloseMessageWindow()

    label("loc_330D")

    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, 92650, 0, 0, 90)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetScenarioFlags(0x161, 0)
    ModifyEventFlags(0, 0, 0x80)
    EventEnd(0x5)
    Return()

    # Function_16_2BD7 end

    def Function_17_3348(): pass

    label("Function_17_3348")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00150.itc", 0x1F)
    LoadChrToIndex("chr/ch00250.itc", 0x20)
    LoadChrToIndex("chr/ch00350.itc", 0x21)
    LoadChrToIndex("chr/ch02950.itc", 0x22)
    LoadChrToIndex("chr/ch03050.itc", 0x23)
    LoadEffect(0x0, "battle\\cr036301.eff")
    ClearChrFlags(0xF, 0x80)
    OP_78(0x6, 0xF)
    OP_49()
    SetChrPos(0xF, 111300, 0, 9000, 225)
    OP_D5(0xF, 0x0, 0x36EE8, 0x0, 0x0)
    ClearMapObjFlags(0x6, 0x4)
    SetMapObjFlags(0x6, 0x1000)
    OP_75(0x6, 0x1, 0x0)
    ClearChrFlags(0x10, 0x80)
    OP_78(0x7, 0x10)
    OP_49()
    SetChrPos(0x10, 111300, 0, -1000, 315)
    OP_D5(0x10, 0x0, 0x4CE78, 0x0, 0x0)
    ClearMapObjFlags(0x7, 0x4)
    SetMapObjFlags(0x7, 0x1000)
    OP_75(0x7, 0x1, 0x0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrChipByIndex(0x103, 0x20)
    SetChrChipByIndex(0x104, 0x21)
    SetChrChipByIndex(0x109, 0x22)
    SetChrChipByIndex(0x105, 0x23)
    SetChrSubChip(0x101, 0x0)
    SetChrSubChip(0x102, 0x0)
    SetChrSubChip(0x103, 0x0)
    SetChrSubChip(0x104, 0x0)
    SetChrSubChip(0x109, 0x0)
    SetChrSubChip(0x105, 0x0)
    SetChrPos(0x101, 106800, 0, 3750, 90)
    SetChrPos(0x102, 105500, 0, 4400, 90)
    SetChrPos(0x103, 104050, 0, 3550, 90)
    SetChrPos(0x104, 106600, 0, 4900, 90)
    SetChrPos(0x109, 105600, 0, 3000, 90)
    SetChrPos(0x105, 106500, 0, 2400, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0xE, 113400, 0, 3750, 180)
    OP_68(110400, 1000, 3750, 0)
    MoveCamera(90, 20, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(23000, 0)
    OP_68(113400, 1000, 3750, 3000)
    SetCameraDistance(26000, 3000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x168, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_36FB")
    FadeToBright(1000, 0)
    OP_0D()
    BlurSwitch(0x3E8, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    Sound(919, 0, 100, 0)
    PlayEffect(0x0, 0xFF, 0xF, 0x0, 0, 1500, 0, 0, 0, 0, 3000, 3000, 3000, 0xFF, 0, 0, 0, 500)
    PlayEffect(0x0, 0xFF, 0x10, 0x0, 0, 1500, 0, 0, 0, 0, 3000, 3000, 3000, 0xFF, 0, 0, 0, 500)
    Sleep(1000)
    OP_75(0x6, 0x2, 0x3E8)
    OP_75(0x7, 0x2, 0x3E8)
    CancelBlur(1000)
    Sleep(1000)
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
    OP_6F(0x79)
    Sleep(500)
    OP_74(0x5, 0x14)
    OP_74(0x6, 0x14)
    OP_74(0x7, 0x14)
    OP_71(0x5, 0x5B, 0x69, 0xFA, 0x8)
    OP_71(0x6, 0x8D, 0xA0, 0xFA, 0x8)
    OP_71(0x7, 0x8D, 0xA0, 0xFA, 0x8)
    OP_79(0x5)
    OP_79(0x6)
    OP_79(0x7)
    Sound(842, 0, 100, 0)
    BlurSwitch(0x64, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    SetCameraDistance(22500, 1000)
    OP_74(0x5, 0x1E)
    OP_74(0x6, 0x1E)
    OP_74(0x7, 0x1E)
    OP_71(0x5, 0x69, 0x73, 0x0, 0x8)
    OP_71(0x6, 0xA1, 0xAA, 0x0, 0x8)
    OP_71(0x7, 0xA1, 0xAA, 0x0, 0x8)
    Sleep(500)
    Jump("loc_3715")

    label("loc_36FB")

    OP_75(0x6, 0x2, 0x0)
    OP_75(0x7, 0x2, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)

    label("loc_3715")

    Battle("BattleInfo_4EC", 0x0, 0x0, 0x0, 0x28, 0xFF)
    FadeToDark(0, 0, -1)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x10, 0x80)
    SetMapObjFlags(0x6, 0x4)
    SetMapObjFlags(0x7, 0x4)
    SetScenarioFlags(0x168, 1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_37A9")
    SetChrChipByIndex(0x0, 0xFF)
    SetChrChipByIndex(0x1, 0xFF)
    SetChrChipByIndex(0x2, 0xFF)
    SetChrChipByIndex(0x3, 0xFF)
    SetChrSubChip(0x0, 0x0)
    SetChrSubChip(0x1, 0x0)
    SetChrSubChip(0x2, 0x0)
    SetChrSubChip(0x3, 0x0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_49()
    OP_37()
    Sleep(500)
    OP_E2(0x2)
    OP_90(0x0, 106900, 0, 4400, 90)
    EventEnd(0x5)
    Jump("loc_37AC")

    label("loc_37A9")

    Call(0, 18)

    label("loc_37AC")

    Return()

    # Function_17_3348 end

    def Function_18_37AD(): pass

    label("Function_18_37AD")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00150.itc", 0x1F)
    LoadChrToIndex("chr/ch00250.itc", 0x20)
    LoadChrToIndex("chr/ch00350.itc", 0x21)
    LoadChrToIndex("chr/ch02950.itc", 0x22)
    LoadChrToIndex("chr/ch03050.itc", 0x23)
    OP_68(114100, 1600, 4200, 0)
    MoveCamera(50, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(20500, 0)
    OP_68(108700, 1300, 3200, 3000)
    MoveCamera(45, 25, 0, 3000)
    OP_6E(500, 3000)
    SetCameraDistance(17100, 3000)
    SetChrPos(0x101, 109900, 0, 3750, 90)
    SetChrPos(0x102, 108500, 0, 4700, 90)
    SetChrPos(0x103, 107050, 0, 3550, 90)
    SetChrPos(0x104, 109600, 0, 4900, 90)
    SetChrPos(0x109, 108600, 0, 3200, 90)
    SetChrPos(0x105, 109500, 0, 2400, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrChipByIndex(0x103, 0x20)
    SetChrChipByIndex(0x104, 0x21)
    SetChrChipByIndex(0x109, 0x22)
    SetChrChipByIndex(0x105, 0x23)
    SetChrSubChip(0x101, 0x0)
    SetChrSubChip(0x102, 0x0)
    SetChrSubChip(0x103, 0x0)
    SetChrSubChip(0x104, 0x0)
    SetChrSubChip(0x109, 0x0)
    SetChrSubChip(0x105, 0x0)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x10, 0x80)
    SetMapObjFlags(0x5, 0x4)
    SetMapObjFlags(0x6, 0x4)
    SetMapObjFlags(0x7, 0x4)
    ModifyEventFlags(0, 1, 0x80)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    OP_29(0xA6, 0x1, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B47")

    #C0099
    ChrTalk(
        0x101,
        (
            "#00006F#5P唔……！\x01",
            "真是相当难对付啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0x102,
        (
            "#00108F#6P而且，果然还是一样……\x01",
            "以不可思议的方式消失了。\x02",
        )
    )

    CloseMessageWindow()
    Fade(250)
    Sound(531, 0, 100, 0)
    Sound(805, 0, 100, 0)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrSubChip(0x102, 0x0)
    SetChrSubChip(0x103, 0x0)
    SetChrSubChip(0x104, 0x0)
    SetChrSubChip(0x109, 0x0)
    SetChrSubChip(0x105, 0x0)
    OP_0D()

    def lambda_39D6():
        TurnDirection(0x101, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_39D6)
    Sleep(50)

    def lambda_39E6():
        TurnDirection(0x102, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_39E6)
    Sleep(50)

    def lambda_39F6():
        TurnDirection(0x103, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_39F6)
    Sleep(50)

    def lambda_3A06():
        TurnDirection(0x104, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_3A06)
    Sleep(50)

    def lambda_3A16():
        TurnDirection(0x109, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_3A16)
    Sleep(50)

    def lambda_3A26():
        TurnDirection(0x105, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_3A26)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)

    #C0101
    ChrTalk(
        0x109,
        (
            "#10108F#12P缇欧，\x01",
            "『力场扭曲』的情况如何了？\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x103,
        (
            "#00206F#6P……还没消失，\x01",
            "上级三属性仍然存在。\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0x104,
        (
            "#00301F#5P真是的……\x01",
            "到底是什么原因啊？\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0x105,
        (
            "#10303F#11P看来『幻兽』并不是\x01",
            "引发力场扭曲的原因……\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0x101,
        (
            "#00013F#11P……有必要去\x01",
            "调查另一头幻兽呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3F10")

    label("loc_3B47")


    #C0106
    ChrTalk(
        0x105,
        (
            "#10306F#6P哎呀呀……\x01",
            "这头幻兽也很难对付。\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0x109,
        "#10101F#6P而且消失的方式和之前那头一样……\x02",
    )

    CloseMessageWindow()
    Fade(250)
    Sound(531, 0, 100, 0)
    Sound(805, 0, 100, 0)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrSubChip(0x102, 0x0)
    SetChrSubChip(0x103, 0x0)
    SetChrSubChip(0x104, 0x0)
    SetChrSubChip(0x109, 0x0)
    SetChrSubChip(0x105, 0x0)
    OP_0D()

    def lambda_3BED():
        TurnDirection(0x101, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3BED)
    Sleep(50)

    def lambda_3BFD():
        TurnDirection(0x102, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_3BFD)
    Sleep(50)

    def lambda_3C0D():
        TurnDirection(0x103, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_3C0D)
    Sleep(50)

    def lambda_3C1D():
        TurnDirection(0x104, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_3C1D)
    Sleep(50)

    def lambda_3C2D():
        TurnDirection(0x109, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_3C2D)
    Sleep(50)

    def lambda_3C3D():
        TurnDirection(0x105, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_3C3D)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)

    #C0108
    ChrTalk(
        0x104,
        (
            "#00301F#5P所谓的『力场扭曲』现象\x01",
            "还是没有消失吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0x103,
        (
            "#00203F#6P是啊……\x02\x03",

            "#00201F我认为应该存在某些\x01",
            "具体原因。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0110
    ChrTalk(
        0x101,
        (
            "#00005F#11P具体原因……？\x01",
            "比如说呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0x103,
        (
            "#00206F#6P……这个嘛……\x01",
            "从刚才开始，我的感觉就\x01",
            "一直被『扭曲』所干扰……\x02\x03",

            "#00200F各位说不定能在我\x01",
            "之前发现原因呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0x102,
        "#00105F#5P是、是吗？\x02",
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0x101,
        (
            "#00003F#11P好……\x01",
            "那我们就在这里搜索一圈吧。\x02\x03",

            "#00000F这附近肯定存在着某种可以引发\x01",
            "『力场扭曲』现象的东西。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3E60():
        TurnDirection(0x101, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3E60)
    Sleep(50)

    def lambda_3E70():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_3E70)
    Sleep(50)

    def lambda_3E80():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_3E80)
    Sleep(50)

    def lambda_3E90():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_3E90)
    Sleep(50)

    def lambda_3EA0():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_3EA0)
    Sleep(50)

    def lambda_3EB0():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_3EB0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)

    #C0114
    ChrTalk(
        0x109,
        "#10100F#6P明白了！\x02",
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0x104,
        "#00300F#5P那就四处找找看吧！\x02",
    )

    CloseMessageWindow()
    OP_29(0xA6, 0x1, 0x3)

    label("loc_3F10")

    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0116
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "消灭了东克洛斯贝尔街道的幻兽！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetChrPos(0x0, 109900, 0, 3750, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetScenarioFlags(0x161, 1)
    OP_66(0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3F9E")
    ModifyEventFlags(1, 3, 0x80)

    label("loc_3F9E")

    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_D7(0x20)
    OP_D7(0x21)
    OP_D7(0x22)
    OP_D7(0x23)
    OP_37()
    EventEnd(0x5)
    Return()

    # Function_18_37AD end

    def Function_19_3FAE(): pass

    label("Function_19_3FAE")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    LoadChrToIndex("apl/ch51216.itc", 0x1E)
    SoundLoad(961)
    SoundLoad(825)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis252.itp")
    LoadEffect(0x0, "event/ev14005.eff")
    LoadEffect(0x1, "event/ev14007.eff")
    SetChrPos(0x101, 121050, 0, 2350, 270)
    SetChrPos(0x102, 121150, 0, 3550, 225)
    SetChrPos(0x103, 120660, 0, 1200, 315)
    SetChrPos(0x104, 120950, 0, 4650, 225)
    SetChrPos(0x109, 119650, 0, 4150, 180)
    SetChrPos(0x105, 118100, 0, 3000, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_68(120250, 1100, 2500, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19000, 0)
    SetCameraDistance(18500, 1000)
    FadeToBright(1000, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4327")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    Sleep(300)

    #A0117
    AnonymousTalk(
        0x101,
        "#00005F这花是……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x168, 3)), scpexpr(EXPR_END)), "loc_41AF")

    #A0118
    AnonymousTalk(
        0x102,
        (
            "#00108F我记得乌尔斯拉间道的\x01",
            "岸边也开着这种花呢……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0119
    AnonymousTalk(
        0x104,
        "#00305F是啊，确实见到过这种花。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_422B")

    label("loc_41AF")


    #A0120
    AnonymousTalk(
        0x105,
        (
            "#10302F乌尔斯拉间道的岸边\x01",
            "好像也开着这种花吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0121
    AnonymousTalk(
        0x101,
        "#00011F有、有这回事吗？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0122
    AnonymousTalk(
        0x102,
        (
            "#00108F嗯，\x01",
            "我也有些印象……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_422B")


    #A0123
    AnonymousTalk(
        0x109,
        (
            "#10109F好漂亮的花啊……\x02\x03",

            "#10102F……以前从没见过这种花，\x01",
            "它的名字是什么呢？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0124
    AnonymousTalk(
        0x101,
        "#00001F唔……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    #C0125
    ChrTalk(
        0x101,
        (
            "#00003F#11P（……难道……）\x02\x03",

            "#00001F（嗯，姑且一试吧。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x161, 2)
    OP_29(0xA6, 0x1, 0x4)
    Jump("loc_43C7")

    label("loc_4327")

    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    Sleep(300)

    #A0126
    AnonymousTalk(
        0x101,
        (
            "#00003F#11P（……难道……）\x02\x03",

            "#00001F（嗯，姑且一试吧。）\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    label("loc_43C7")

    FadeToDark(300, 0, 100)
    OP_0D()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "摘下蓝花\x01",      # 0
            "放弃\x01",          # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_440F"),
        (1, "loc_50AA"),
        (SWITCH_DEFAULT, "loc_50E9"),
    )


    label("loc_440F")

    OP_9B(0x0, 0x101, 0x0, 0x2EE, 0x3E8, 0x0)
    Fade(250)
    Sound(802, 0, 100, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    OP_0D()

    #C0127
    ChrTalk(
        0x102,
        "#00105F罗伊德……？\x02",
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0x105,
        (
            "#10305F#6P怎么？你想把\x01",
            "这朵花摘下来吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0x101,
        (
            "#00003F#11P是啊……\x01",
            "虽说有点残忍……\x02",
        )
    )

    CloseMessageWindow()
    Sound(929, 0, 40, 0)
    Sound(828, 2, 30, 0)
    PlayEffect(0x0, 0x0, 0xFF, 0x0, 119770, 600, 2910, 0, 0, 0, 750, 750, 750, 0xFF, 0, 0, 0, 0)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0130
    ChrTalk(
        0x104,
        "#00301F#5P怎、怎么回事！？\x02",
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0x103,
        "#00205F#12P这是……！\x02",
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0x101,
        "#00001F#11P唔……！\x02",
    )

    CloseMessageWindow()
    SetMapObjFrame(0x2, "flower04", 0x0, 0x1)
    StopEffect(0x0, 0x2)
    Fade(250)
    Sound(802, 0, 100, 0)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    Sound(961, 2, 70, 0)
    Sound(233, 0, 100, 0)
    Sound(929, 0, 60, 0)
    PlayEffect(0x1, 0x1, 0x101, 0x3, 0, 1050, 500, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    OP_0D()
    OP_7D(0xD7, 0xFF, 0xFF, 0x0, 0x5DC)
    OP_11(0x7B, 0xB4, 0xD5, 0x1E, 0xB4, 0x5DC)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0xF)
    MoveCamera(45, 23, 10, 3000)
    SetCameraDistance(12000, 3000)
    OP_6E(1000, 3000)
    Sleep(2500)
    Sound(829, 0, 100, 0)
    StopSound(961, 2000, 60)
    StopSound(828, 2000, 20)
    FadeToDark(500, 16777215, -1)
    Sleep(800)
    FadeToBright(300, 16777215)
    CancelBlur(300)
    OP_7D(0xFF, 0xFF, 0xFF, 0x0, 0x32)
    OP_11(0xA7, 0xDD, 0xFE, 0x1E, 0xB4, 0x32)
    MoveCamera(45, 21, 0, 50)
    SetCameraDistance(18500, 50)
    OP_6E(500, 50)
    StopEffect(0x1, 0x2)
    Sleep(500)
    OP_6F(0x79)
    StopBGM(0x1770)

    #C0133
    ChrTalk(
        0x101,
        "#00013F#11P………………………………\x02",
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0x109,
        "#10111F#5P刚、刚才那是……\x02",
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0x102,
        "#00108F空间似乎晃动了一下呢……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x103, 500)

    #C0136
    ChrTalk(
        0x105,
        (
            "#10308F#6P……缇欧，\x01",
            "『力场扭曲』的情况如何了？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x103)

    #C0137
    ChrTalk(
        0x103,
        (
            "#00203F#12P……上级三属性的\x01",
            "气息完全消失了。\x02\x03",

            "#00201F在这一带已经感知不到\x01",
            "任何异常了。\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0x101,
        "#00006F#11P是吗……\x02",
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0x104,
        (
            "#00305F#5P等、等等。\x02\x03",

            "#00307F难道就是这种蓝花\x01",
            "引起了异常现象吗！？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 500)

    #C0140
    ChrTalk(
        0x105,
        (
            "#10304F#6P目前看来，正是如此。\x02\x03",

            "#10300F虽然我也很难相信\x01",
            "小小一朵花就有如此力量……\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0x102,
        "#00101F真、真不敢相信……\x02",
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0x109,
        (
            "#10101F#5P这、这到底是\x01",
            "什么花啊？\x02",
        )
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0x103,
        (
            "#00206F#12P……现在已经无法从这朵花上\x01",
            "感知到奇怪的气息了……\x02\x03",

            "#00200F不管怎么说，还是找个地方\x01",
            "调查一下这种花为好吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0x101,
        (
            "#00008F#11P说的也是……\x02\x03",

            "#00003F……但医科大学好像\x01",
            "和这种事情挂不上钩。\x02",
        )
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0x102,
        (
            "#00100F总、总之，一定要把它小心收好，\x01",
            "注意别弄丢了。\x02\x03",

            "以后要是想到了适合咨询的地方，\x01",
            "再继续调查就是了。\x02",
        )
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0x101,
        "#00006F#11P嗯，就这么办吧。\x02",
    )

    CloseMessageWindow()
    OP_9B(0x1, 0x101, 0xB4, 0x2EE, 0x3E8, 0x0)
    OP_63(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1200)
    OP_64(0x105)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7516", 0)

    #C0147
    ChrTalk(
        0x105,
        "#10303F#6P……唔………\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    def lambda_4B23():
        TurnDirection(0x101, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_4B23)
    Sleep(50)

    def lambda_4B33():
        TurnDirection(0x102, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_4B33)
    Sleep(50)

    def lambda_4B43():
        TurnDirection(0x103, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_4B43)
    Sleep(50)

    def lambda_4B53():
        TurnDirection(0x104, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_4B53)
    Sleep(50)

    def lambda_4B63():
        TurnDirection(0x109, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_4B63)
    Sleep(50)

    def lambda_4B73():
        TurnDirection(0x105, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_4B73)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    Sleep(1000)

    #C0148
    ChrTalk(
        0x101,
        "#00005F#11P瓦吉……？\x02",
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0x109,
        "#10101F#5P莫非你有什么头绪吗？\x02",
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0x105,
        (
            "#10303F#6P这个嘛……\x01",
            "说不定只是我记错了。\x02\x03",

            "#10301F印象中，似乎曾在教会的圣典中\x01",
            "看过一个有关奇异蓝花的传说。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0151
    ChrTalk(
        0x101,
        "#00011F#11P咦……！？\x02",
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0x104,
        "#00305F#5P喂喂，你是说真的吗！？\x02",
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0x105,
        (
            "#10306F#6P这个嘛，毕竟是很久以前看到的了，\x01",
            "而且只是随便扫了一眼……\x02\x03",

            "#10300F艾莉，你有没有什么印象？\x02",
        )
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0x102,
        (
            "#00112F#11P我也不可能把\x01",
            "所有圣典看遍啊……\x02\x03",

            "#00103F……不过，好像确实\x01",
            "看过类似的记载。\x02\x03",

            "#00108F关于拥有奇异力量的\x01",
            "『蓝花』的传说……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x102, 500)

    #C0155
    ChrTalk(
        0x109,
        (
            "#10111F#6P那、那应该……\x01",
            "就没错了吧？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 500)

    #C0156
    ChrTalk(
        0x103,
        (
            "#00201F#12P看来有必要去向\x01",
            "教会的人员确认一下呢。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4E70():
        TurnDirection(0x101, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_4E70)
    Sleep(50)

    def lambda_4E80():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_4E80)
    Sleep(50)

    def lambda_4E90():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_4E90)
    Sleep(50)

    def lambda_4EA0():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_4EA0)
    Sleep(50)

    def lambda_4EB0():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_4EB0)
    Sleep(50)

    def lambda_4EC0():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_4EC0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7C, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_4F6A")

    #C0157
    ChrTalk(
        0x101,
        (
            "#00003F#11P……是啊。\x02\x03",

            "#00000F那我们就去找玛布尔老师\x01",
            "或莉丝小姐问问看吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0x102,
        (
            "#00104F说的也是……\x01",
            "这两人都很适合。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5003")

    label("loc_4F6A")


    #C0159
    ChrTalk(
        0x101,
        (
            "#00003F#11P……是啊。\x02\x03",

            "#00000F最适合的咨询对象\x01",
            "显然还是玛布尔老师吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0x102,
        (
            "#00104F嗯，我也这样想。\x02\x03",

            "#00108F（不过，其实也可以找『她』咨询一下……）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5003")


    #C0161
    ChrTalk(
        0x104,
        (
            "#00300F#5P好～那我们这就去\x01",
            "克洛斯贝尔大圣堂吧！\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_CC(0x1, 0xFF, 0x0)
    OP_D7(0x1E)
    OP_49()
    OP_37()
    SetChrPos(0x0, 121050, 0, 2350, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    AddItemNumber(0x333, 1)
    SetScenarioFlags(0x161, 3)
    OP_29(0xA6, 0x1, 0x5)
    OP_65(0x0, 0x1)
    ModifyEventFlags(0, 3, 0x80)
    StopBGM(0xFA0)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7121", 0)
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x79), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_24(0x3C1)
    OP_24(0x33C)
    EventEnd(0x5)
    Jump("loc_50E9")

    label("loc_50AA")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_CC(0x1, 0xFF, 0x0)
    OP_D7(0x1E)
    OP_49()
    OP_37()
    SetChrPos(0x0, 121050, 0, 2350, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Jump("loc_50E9")

    label("loc_50E9")

    Return()

    # Function_19_3FAE end

    def Function_20_50EA(): pass

    label("Function_20_50EA")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis252.itp")
    OP_68(120250, 1000, 2500, 0)
    MoveCamera(45, 23, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18500, 0)
    SetChrPos(0x101, 121050, 0, 2350, 270)
    SetChrPos(0x102, 121150, 0, 3550, 225)
    SetChrPos(0x103, 120660, 0, 1200, 315)
    SetChrPos(0x104, 120950, 0, 4650, 225)
    SetChrPos(0x109, 119650, 0, 4150, 180)
    SetChrPos(0x105, 118100, 0, 3000, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    #A0162
    AnonymousTalk(
        0x109,
        (
            "#10100F对、对了……\x02\x03",

            "是不是应该把这里的花\x01",
            "也一并摘掉呢？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0163
    AnonymousTalk(
        0x101,
        (
            "#00000F不了……\x01",
            "这里的花就先留着吧。\x02\x03",

            "说不定会成为\x01",
            "珍贵的样品。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0164
    AnonymousTalk(
        0x103,
        (
            "#00200F……说的也是。\x01",
            "毕竟摘下之后，它的力量就会随之消失。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0165
    AnonymousTalk(
        0x102,
        (
            "#00100F不过……如果幻兽再次出现，\x01",
            "可就不得不把它摘掉了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0166
    AnonymousTalk(
        0x104,
        "#00300F嗯，那就到时再说吧。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_CC(0x1, 0xFF, 0x0)
    SetChrPos(0x0, 121050, 0, 2350, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetScenarioFlags(0x161, 4)
    EventEnd(0x5)
    Return()

    # Function_20_50EA end

    def Function_21_53AF(): pass

    label("Function_21_53AF")

    EventBegin(0x0)
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_68(37740, 1200, -14770, 3000)
    SetCameraDistance(17000, 3000)
    OP_6F(0x79)
    Fade(500)
    OP_4B(0xA, 0xFF)
    OP_4B(0x8, 0xFF)
    OP_4B(0x9, 0xFF)
    OP_68(38230, 1200, -14840, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(14580, 0)
    OP_0D()

    #C0167
    ChrTalk(
        0x8,
        (
            "唔～真是相当\x01",
            "诡异的魔兽啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0x9,
        (
            "#6P如、如果那种怪物跑到这边，\x01",
            "我们恐怕连半秒都撑不住啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0xA,
        (
            "是啊，要是真的发生那种情况，\x01",
            "就必须迅速去避难了。\x02",
        )
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0xA,
        (
            "不过，现在还是先在这里\x01",
            "等警备队的人来吧……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0171
    ChrTalk(
        0xA,
        "哦哦，你是……罗伊德团员！\x02",
    )

    CloseMessageWindow()
    OP_68(37180, 1400, -14790, 4000)
    MoveCamera(33, 33, 0, 4000)
    OP_6E(600, 4000)
    SetCameraDistance(14430, 4000)

    def lambda_5551():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_5551)

    def lambda_555E():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_555E)
    OP_93(0x9, 0x10E, 0x1F4)
    SetChrPos(0x101, 28250, 0, -15760, 90)
    SetChrPos(0x102, 28250, 0, -15760, 90)
    SetChrPos(0x103, 28250, 0, -15760, 90)
    SetChrPos(0x104, 28250, 0, -15760, 90)
    SetChrPos(0x109, 28250, 0, -15760, 90)
    SetChrPos(0x105, 28250, 0, -15760, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)

    def lambda_55EC():
        OP_95(0xFE, 36720, 0, -14030, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_55EC)
    Sleep(300)

    def lambda_5609():
        OP_95(0xFE, 36720, 0, -15170, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5609)
    Sleep(300)

    def lambda_5626():
        OP_95(0xFE, 35680, 0, -13860, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5626)
    Sleep(300)

    def lambda_5643():
        OP_95(0xFE, 35680, 0, -15050, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_5643)
    Sleep(300)

    def lambda_5660():
        OP_95(0xFE, 34560, 0, -13930, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_5660)
    Sleep(300)

    def lambda_567D():
        OP_95(0xFE, 34700, 0, -14930, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_567D)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x109, 1)
    WaitChrThread(0x105, 1)

    #C0172
    ChrTalk(
        0x101,
        (
            "#6P#00003F好久不见了，赛尔丹分部长。\x02\x03",

            "#00001F听说这里出现了不可思议的\x01",
            "大型魔兽——『幻兽』？\x02",
        )
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0xA,
        (
            "『幻兽』……\x01",
            "嗯，这名称十分贴切呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0xA,
        (
            "没错，就在昨天傍晚，那头所谓的『幻兽』\x01",
            "突然出现在了沼泽地带的深处。\x02",
        )
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0xA,
        (
            "我们立刻就\x01",
            "联络了警备队……\x02",
        )
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0x8,
        (
            "#11P难道说……\x01",
            "你们特别任务支援科就是来\x01",
            "处理这件事的吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0x102,
        (
            "#6P#00103F是的，我们接受了警备队的任务。\x02\x03",

            "#00101F您可以向我们\x01",
            "描述一下详细状况吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0xA,
        (
            "没问题，正如我刚才所说，\x01",
            "最初发现那东西，\x01",
            "是在昨天的傍晚时分……\x02",
        )
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0xA,
        (
            "当时真的是毫无预兆，\x01",
            "突然就听到了\x01",
            "奇怪的鸣叫声。\x02",
        )
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0x9,
        (
            "#12P在一直封锁着的沼泽地带深处，\x01",
            "隐约能看到奇怪的黑影……\x02",
        )
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0x9,
        "#12P大家一起小心翼翼地接近黑影。\x02",
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0x8,
        (
            "#11P然后就发现了那头\x01",
            "不可思议的『幻兽』。\x02",
        )
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0x8,
        (
            "#11P我们急忙向警备队\x01",
            "报告了这件事。\x02",
        )
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0xA,
        (
            "报告之后，我们本打算马上逃离\x01",
            "这个地方……但『幻兽』完全\x01",
            "没有离开那个地方的意思。\x02",
        )
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0xA,
        (
            "于是从昨天起，我们就\x01",
            "轮班监视它的情况。\x02",
        )
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0x103,
        "#6P#00203F……真是辛苦各位了。\x02",
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0x109,
        (
            "#6P#10101F在监视期间内，\x01",
            "有没有发生什么奇怪的情况呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0xA,
        (
            "不，完全没有，\x01",
            "但这反而更让人毛骨悚然。\x02",
        )
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0xA,
        (
            "即使站在远处观察，我们也能感觉到\x01",
            "它那带有敌意的意志与气息……\x02",
        )
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0x9,
        (
            "#12P该怎么形容呢……\x01",
            "我感觉它应该不是不想动，\x01",
            "而是动不了的说。\x02",
        )
    )

    CloseMessageWindow()

    #C0191
    ChrTalk(
        0x9,
        (
            "#12P虽然我也搞不懂\x01",
            "具体原因的说……\x02",
        )
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0x105,
        (
            "#6P#10303F原来如此，突然出现，\x01",
            "而且无法离开那个地方吗……\x02",
        )
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0x104,
        (
            "#6P#00301F嗯……看来明显与\x01",
            "那个『力场扭曲』现象\x01",
            "有关啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0194
    ChrTalk(
        0x101,
        (
            "#6P#00003F嗯，应该没错。\x02\x03",

            "#00013F那么……赛尔丹分部长，\x01",
            "我们想尽快前往沼泽地带的深处……\x02",
        )
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0xA,
        (
            "哦哦，你们要去\x01",
            "消灭那家伙吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0xA,
        "我这就把锁打开。\x02",
    )

    CloseMessageWindow()
    OP_93(0xA, 0x5A, 0x1F4)
    Sound(806, 0, 100, 0)
    Sleep(1000)
    Sound(103, 0, 100, 0)
    OP_71(0x0, 0x0, 0xA, 0x0, 0x0)
    OP_79(0x0)
    OP_93(0xA, 0x10E, 0x1F4)

    #C0197
    ChrTalk(
        0xA,
        (
            "好了，你们可以进去了。\x01",
            "接下来就拜托大家啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0x101,
        "#6P#00000F嗯，我明白了。\x02",
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0xA, 34370, 0, -14100, 225)
    SetChrPos(0x8, 33010, 0, -14380, 90)
    SetChrPos(0x9, 33520, 0, -15630, 0)
    ClearChrFlags(0x9, 0x10)
    OP_65(0x2, 0x1)
    ModifyEventFlags(0, 2, 0x80)
    SetScenarioFlags(0x17A, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x0, 37160, 0, -14440, 90)
    OP_69(0xFF, 0x0)
    OP_4C(0xA, 0xFF)
    OP_4C(0x8, 0xFF)
    OP_4C(0x9, 0xFF)
    EventEnd(0x5)
    Return()

    # Function_21_53AF end

    def Function_22_5D39(): pass

    label("Function_22_5D39")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_4B(0xA, 0xFF)
    OP_4B(0x8, 0xFF)
    EndChrThread(0x9, 0x0)
    OP_68(35180, 1200, -14020, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17000, 0)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 34070, 0, -14520, 90)
    SetChrPos(0x8, 34270, 0, -15520, 90)
    SetChrPos(0x9, 34070, 0, -13320, 90)
    SetChrPos(0x101, 35460, 0, -14310, 270)
    SetChrPos(0x102, 35500, 0, -15390, 270)
    SetChrPos(0x104, 36590, 0, -15670, 270)
    SetChrPos(0x109, 36590, 0, -14070, 270)
    SetChrPos(0x103, 37600, 0, -15500, 270)
    SetChrPos(0x105, 37650, 0, -14100, 270)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()

    #C0199
    ChrTalk(
        0xA,
        (
            "#6P哦哦，罗伊德团员，\x01",
            "你们成功消灭那头『幻兽』了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0x101,
        (
            "#00006F#11P是的，总算解决掉了。\x02\x03",

            "#00000F虽然还要继续保持警惕，\x01",
            "但我认为它应该不会在\x01",
            "短时间之内再次出现了。\x02",
        )
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0x9,
        (
            "#5P真的吗……\x01",
            "那真是可喜可贺的说。\x02",
        )
    )

    CloseMessageWindow()

    #C0202
    ChrTalk(
        0x8,
        (
            "#6P呵呵，这下我们又能\x01",
            "专心钓鱼了。\x02",
        )
    )

    CloseMessageWindow()

    #C0203
    ChrTalk(
        0xA,
        "#6P是啊，真是多亏各位相助。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 0)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_61CF")

    #C0204
    ChrTalk(
        0x8,
        "#6P对了，罗伊德。\x02",
    )

    CloseMessageWindow()

    #C0205
    ChrTalk(
        0x8,
        (
            "#6P这也算不上是什么谢礼，\x01",
            "你可以收下吗？\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0206
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x17),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x17, 1)
    SetMessageWindowPos(14, 280, 60, 3)

    #C0207
    ChrTalk(
        0x101,
        "#00005F#11P这是……新钓竿吗？\x02",
    )

    CloseMessageWindow()

    #C0208
    ChrTalk(
        0x8,
        (
            "#6P没错，是我为了对抗钓皇俱乐部\x01",
            "而专门特制的钓竿。\x02",
        )
    )

    CloseMessageWindow()

    #C0209
    ChrTalk(
        0x8,
        (
            "#6P有了它，应该就能钓起\x01",
            "更大型的鱼类了。\x02",
        )
    )

    CloseMessageWindow()

    #C0210
    ChrTalk(
        0x101,
        "#00002F#11P这是彼德先生制作的……？\x02",
    )

    CloseMessageWindow()

    #C0211
    ChrTalk(
        0xA,
        (
            "#6P哈哈，别看彼德这个样子，\x01",
            "他在制造工具这方面还是很有一手的。\x02",
        )
    )

    CloseMessageWindow()

    #C0212
    ChrTalk(
        0xA,
        (
            "#6P偶尔也会像这次一样，\x01",
            "改造现有的成品，\x01",
            "制作出全新的钓具。\x02",
        )
    )

    CloseMessageWindow()

    #C0213
    ChrTalk(
        0x9,
        (
            "#5P呵呵，但他的钓技\x01",
            "却根本上不了台面，\x01",
            "真是不可思议的说～\x02",
        )
    )

    CloseMessageWindow()

    #C0214
    ChrTalk(
        0x8,
        (
            "#6P喂喂，克潘，\x01",
            "别说这些没用的话。\x02",
        )
    )

    CloseMessageWindow()

    #C0215
    ChrTalk(
        0x101,
        (
            "#00012F#11P哈哈……\x02\x03",

            "#00000F多谢您送给我\x01",
            "这么好的东西。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6705")

    label("loc_61CF")


    #C0216
    ChrTalk(
        0xA,
        "#6P对了，罗伊德团员。\x02",
    )

    CloseMessageWindow()

    #C0217
    ChrTalk(
        0xA,
        (
            "#6P有件事情我还没跟你提过，\x01",
            "我想趁现在向你说明一下我们和\x01",
            "钓皇俱乐部之间的『爆钓比赛』……\x02",
        )
    )

    CloseMessageWindow()

    #C0218
    ChrTalk(
        0x101,
        "#00011F#11P『爆钓比赛』……？\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    FadeToBright(1000, 0)
    OP_0D()

    #C0219
    ChrTalk(
        0x101,
        (
            "#00003F#11P原来如此，与钓皇俱乐部的\x01",
            "五名成员进行『爆钓比赛』……\x02\x03",

            "只要战胜他们，就能夺回事务所和\x01",
            "垂钓场所的自由使用权……\x02\x03",

            "#00001F但如果无法取胜，就要服从对方的规定吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0220
    ChrTalk(
        0xA,
        "#6P嗯，就是这样。\x02",
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0xA,
        (
            "#6P关于这场比赛，\x01",
            "我们几个会\x01",
            "努力挑战的。\x02",
        )
    )

    CloseMessageWindow()

    #C0222
    ChrTalk(
        0xA,
        (
            "#6P罗伊德团员，\x01",
            "你的本职工作应该很忙，\x01",
            "就不用太过挂心了。\x02",
        )
    )

    CloseMessageWindow()

    #C0223
    ChrTalk(
        0x101,
        "#00000F#11P嗯，我明白了。\x02",
    )

    CloseMessageWindow()

    #C0224
    ChrTalk(
        0x8,
        "#6P对了，罗伊德。\x02",
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0x8,
        (
            "#6P这也说不上是什么谢礼，\x01",
            "你可以收下吗？\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0226
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x17),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x17, 1)
    SetMessageWindowPos(14, 280, 60, 3)

    #C0227
    ChrTalk(
        0x101,
        "#00005F#11P这是……新钓竿吗？\x02",
    )

    CloseMessageWindow()

    #C0228
    ChrTalk(
        0x8,
        (
            "#6P没错，是我为了对抗钓皇俱乐部\x01",
            "而专门特制的钓竿。\x02",
        )
    )

    CloseMessageWindow()

    #C0229
    ChrTalk(
        0x8,
        (
            "#6P有了它，应该就能钓起\x01",
            "更大型的鱼类了。\x02",
        )
    )

    CloseMessageWindow()

    #C0230
    ChrTalk(
        0x101,
        "#00002F#11P这是彼德先生制作的……？\x02",
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0xA,
        (
            "#6P哈哈，别看彼德这个样子，\x01",
            "他在制造工具这方面还是很有一手的。\x02",
        )
    )

    CloseMessageWindow()

    #C0232
    ChrTalk(
        0xA,
        (
            "#6P偶尔也会像这次一样，\x01",
            "改造现有的成品，\x01",
            "制作出全新的钓具。\x02",
        )
    )

    CloseMessageWindow()

    #C0233
    ChrTalk(
        0x9,
        (
            "#5P呵呵，但他的钓技\x01",
            "却根本上不了台面，\x01",
            "真是不可思议的说～\x02",
        )
    )

    CloseMessageWindow()

    #C0234
    ChrTalk(
        0x8,
        (
            "#6P喂喂，克潘，\x01",
            "别说这些没用的话。\x02",
        )
    )

    CloseMessageWindow()

    #C0235
    ChrTalk(
        0x101,
        (
            "#00012F#11P哈哈……\x02\x03",

            "#00000F多谢您送给我\x01",
            "这么好的东西。\x02",
        )
    )

    CloseMessageWindow()
    Sound(814, 0, 100, 0)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0236
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "从现在开始，可以向钓皇俱乐部成员发起挑战，\x01",
            "展开『爆钓比赛』了。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #A0237
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "关于比赛的详细规则，\x01",
            "可以向东街『钓皇俱乐部』的\x01",
            "接待小姐塞拉姆咨询。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x1C0, 0)

    label("loc_6705")

    SetScenarioFlags(0x17A, 1)
    SetChrPos(0x8, 17130, 0, -10450, 0)
    SetChrPos(0x9, 28980, 0, 4010, 0)
    SetChrChipByIndex(0x9, 0x3)
    SetChrSubChip(0x9, 0x0)
    SetChrFlags(0x9, 0x10)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x0, 36380, 0, -14420, 270)
    OP_69(0xFF, 0x0)
    OP_4C(0x8, 0xFF)
    EventEnd(0x5)
    Return()

    # Function_22_5D39 end

    def Function_23_676C(): pass

    label("Function_23_676C")

    EventBegin(0x0)
    OP_4B(0x8, 0xFF)
    Fade(500)
    OP_68(17140, 1200, -10530, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17000, 0)
    SetChrPos(0x101, 16630, 0, -11900, 0)
    SetChrPos(0x102, 17690, 0, -11920, 0)
    SetChrPos(0x103, 16680, 0, -12920, 0)
    SetChrPos(0x104, 17680, 0, -12920, 0)
    SetChrPos(0x109, 16670, 250, -13920, 0)
    SetChrPos(0x105, 17670, 0, -13920, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 1)), scpexpr(EXPR_END)), "loc_68BD")
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x8, 0x101, 500)

    #C0238
    ChrTalk(
        0x8,
        (
            "罗伊德，你终于把\x01",
            "所有部件集齐了啊！\x02",
        )
    )

    CloseMessageWindow()

    #C0239
    ChrTalk(
        0x101,
        "#00002F是的，总算是全部收集到了。\x02",
    )

    CloseMessageWindow()

    #C0240
    ChrTalk(
        0x8,
        (
            "嗯，我马上就给你\x01",
            "组装起来吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6B71")

    label("loc_68BD")

    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x8, 0x101, 500)

    #C0241
    ChrTalk(
        0x8,
        "罗伊德，这是……\x02",
    )

    CloseMessageWindow()

    #C0242
    ChrTalk(
        0x101,
        (
            "#00004F哦，我想应该\x01",
            "是钓具的部件，\x01",
            "还真漂亮呢。\x02\x03",

            "#00000F我在从四天王手中夺回的垂钓场所\x01",
            "钓到了很罕见的鱼……\x01",
            "这就是那条鱼吐出来的。\x02",
        )
    )

    CloseMessageWindow()

    #C0243
    ChrTalk(
        0x8,
        "……不会有错的。\x02",
    )

    CloseMessageWindow()

    #C0244
    ChrTalk(
        0x8,
        (
            "这就是过去某位飘泊的钓鱼大师\x01",
            "所使用过的传说钓具的部件。\x02",
        )
    )

    CloseMessageWindow()

    #C0245
    ChrTalk(
        0x8,
        (
            "听说他在离开克洛斯贝尔的时候，\x01",
            "将这套钓具\x01",
            "封存在了这片土地上……\x02",
        )
    )

    CloseMessageWindow()

    #C0246
    ChrTalk(
        0x8,
        (
            "没想到……竟然会以\x01",
            "这样的形式再现于世！\x02",
        )
    )

    CloseMessageWindow()

    #C0247
    ChrTalk(
        0x101,
        (
            "#00005F是、是那么\x01",
            "珍贵的东西吗……\x02\x03",

            "#00003F那该怎么办呢？\x01",
            "还是交还给那个人为好吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0248
    ChrTalk(
        0x8,
        "不，没有那个必要。\x02",
    )

    CloseMessageWindow()

    #C0249
    ChrTalk(
        0x8,
        (
            "……因为他曾经说过，\x01",
            "这套钓具就送给找到它的人使用。\x02",
        )
    )

    CloseMessageWindow()

    #C0250
    ChrTalk(
        0x8,
        (
            "另外，这套钓具共有四个部件……\x01",
            "咦？原来你已经集齐了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0251
    ChrTalk(
        0x8,
        (
            "那我这就给你把钓具组装起来吧。\x01",
            "可以吗？罗伊德。\x02",
        )
    )

    CloseMessageWindow()

    #C0252
    ChrTalk(
        0x101,
        "#00005F好、好的。\x02",
    )

    CloseMessageWindow()

    label("loc_6B71")

    FadeToDark(1000, 0, -1)
    OP_0D()
    FadeToBright(1000, 0)
    OP_0D()

    #C0253
    ChrTalk(
        0x8,
        (
            "哦哦，太美了。\x01",
            "这就是传说中的……\x02",
        )
    )

    CloseMessageWindow()

    #C0254
    ChrTalk(
        0x101,
        (
            "#00004F嗯……把它们组装起来一看，\x01",
            "确实漂亮又帅气呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0255
    ChrTalk(
        0x8,
        (
            "那么，罗伊德，\x01",
            "请你小心收好它吧。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0256
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x18),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x18, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    SubItemNumber(0x344, 1)
    SubItemNumber(0x345, 1)
    SubItemNumber(0x346, 1)
    SubItemNumber(0x347, 1)

    #C0257
    ChrTalk(
        0x101,
        "#00005F这、这件钓具可以由我来使用吗？\x02",
    )

    CloseMessageWindow()

    #C0258
    ChrTalk(
        0x8,
        (
            "呵呵呵，这叫什么话。\x01",
            "这是你找到的啊，自然归你所有。\x02",
        )
    )

    CloseMessageWindow()

    #C0259
    ChrTalk(
        0x8,
        (
            "而且，看来你已经\x01",
            "把钓杰四天王全部打倒了……\x02",
        )
    )

    CloseMessageWindow()

    #C0260
    ChrTalk(
        0x8,
        (
            "接下来，就用力挥舞那把钓竿，\x01",
            "一鼓作气把最后的雷克罗德也打倒吧！\x02",
        )
    )

    CloseMessageWindow()

    #C0261
    ChrTalk(
        0x101,
        "#00000F好、好的……我明白了！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x190, 6)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x0, 17060, 0, -12510, 0)
    OP_69(0xFF, 0x0)
    OP_93(0x8, 0x0, 0x0)
    OP_4C(0x8, 0xFF)
    EventEnd(0x5)
    Return()

    # Function_23_676C end

    def Function_24_6DA0(): pass

    label("Function_24_6DA0")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch46100.itc", 0x1E)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)
    SetChrPos(0xA, 5250, 10, -7750, 270)
    SetChrChipByIndex(0xD, 0x1E)
    SetChrSubChip(0xD, 0x0)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x8000)
    SetChrPos(0xD, 5250, 10, -8950, 270)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 6450, 10, -7550, 270)
    SetChrChipByIndex(0x9, 0x1)
    SetChrSubChip(0x9, 0x0)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, 6450, 10, -9150, 270)
    OP_4B(0xA, 0xFF)
    OP_4B(0x8, 0xFF)
    OP_4B(0x9, 0xFF)
    OP_68(3810, 2200, -8500, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17000, 0)
    SetChrPos(0x101, 3250, 10, -8350, 90)
    SetChrPos(0x102, 1270, 0, -8270, 90)
    SetChrPos(0x103, 1220, 0, -9350, 90)
    SetChrPos(0x104, 1120, 0, -7380, 90)
    SetChrPos(0x109, -70, 0, -8850, 90)
    SetChrPos(0x105, -610, 0, -7900, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_68(3810, 1200, -8500, 3000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x1)

    #C0262
    ChrTalk(
        0xA,
        (
            "罗伊德团员……\x01",
            "不对，是『钓皇杀手』罗伊德大师。\x02",
        )
    )

    CloseMessageWindow()

    #C0263
    ChrTalk(
        0xA,
        (
            "这次真是太感谢你了，\x01",
            "用语言都不足以表达我的谢意。\x02",
        )
    )

    CloseMessageWindow()

    #C0264
    ChrTalk(
        0x9,
        "你实在太厉害了，罗伊德大师！\x02",
    )

    CloseMessageWindow()

    #C0265
    ChrTalk(
        0xD,
        (
            "嗯，能由年轻人亲手保护我们的\x01",
            "钓公师团·克洛斯贝尔分部，\x01",
            "实在是一件值得高兴，令人自豪的事情。\x02",
        )
    )

    CloseMessageWindow()

    #C0266
    ChrTalk(
        0x8,
        (
            "呵呵呵，这场爆钓比赛\x01",
            "一定会名流千古的。\x02",
        )
    )

    CloseMessageWindow()

    #C0267
    ChrTalk(
        0x101,
        "#00006F过、过奖了、没那么夸张啦。\x02",
    )

    CloseMessageWindow()
    OP_68(2190, 1200, -8070, 2000)
    OP_6F(0x79)

    #C0268
    ChrTalk(
        0x102,
        "#00102F（唔～被一个劲地赞扬呢。）\x02",
    )

    CloseMessageWindow()

    #C0269
    ChrTalk(
        0x109,
        (
            "#10103F（虽然不太明白……\x01",
            "  但感觉就像英雄一样呢。）\x02",
        )
    )

    CloseMessageWindow()

    #C0270
    ChrTalk(
        0x103,
        (
            "#00200F（『钓皇杀手』……\x01",
            "  听起来还挺帅气的。）\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x191, 1)
    ClearChrFlags(0x8, 0x8000)
    ClearChrFlags(0x9, 0x8000)
    SetChrPos(0x8, 17130, 0, -10450, 0)
    SetChrPos(0x9, 28980, 0, 4010, 0)
    OP_4C(0x8, 0xFF)
    OP_4C(0x9, 0xFF)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrChipByIndex(0x9, 0x3)
    SetChrSubChip(0x9, 0x0)
    OP_49()
    OP_D7(0x1E)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 3250, 10, -8350, 90)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_24_6DA0 end

    SaveToFile()

Try(main)
