from ScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "ペーター",               # 1
        "コパン",                 # 2
        "セルダン支部長",         # 3
        "レイクロードⅢ世",       # 4
        "竜宮カグヤ",             # 5
        "フィッシャー団長",       # 6
        "幻獣",                   # 7
        "幻獣",                   # 8
        "幻獣",                   # 9
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
        "Function_4_1346",         # 04, 4
        "Function_5_1E14",         # 05, 5
        "Function_6_23A3",         # 06, 6
        "Function_7_2463",         # 07, 7
        "Function_8_25E2",         # 08, 8
        "Function_9_26A7",         # 09, 9
        "Function_10_2755",        # 0A, 10
        "Function_11_286B",        # 0B, 11
        "Function_12_293F",        # 0C, 12
        "Function_13_2979",        # 0D, 13
        "Function_14_2CBC",        # 0E, 14
        "Function_15_2D50",        # 0F, 15
        "Function_16_2F23",        # 10, 16
        "Function_17_36C0",        # 11, 17
        "Function_18_3B25",        # 12, 18
        "Function_19_43B0",        # 13, 19
        "Function_20_5684",        # 14, 20
        "Function_21_5975",        # 15, 21
        "Function_22_641D",        # 16, 22
        "Function_23_6FF8",        # 17, 23
        "Function_24_7706",        # 18, 24
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

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1342")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1138")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_118C")

    label("loc_1138")

    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "話をする\x01",          # 0
            "買い物をする\x01",      # 1
            "やめる\x01",            # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_118C")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jump("loc_118C")

    label("loc_118C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11BC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x190, 5)), scpexpr(EXPR_END)), "loc_11AB")
    OP_AF(0x37)
    Jump("loc_11AD")

    label("loc_11AB")

    OP_AF(0x36)

    label("loc_11AD")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_133D")

    label("loc_11BC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_133D")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_12CD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11F0")
    Call(0, 7)
    Jump("loc_12BE")

    label("loc_11F0")


    #C0001
    ChrTalk(
        0xA,
        (
            "しかし……この小屋で\x01",
            "１ヶ月近くも生活するなんて\x01",
            "本当にたくましい連中だなァ。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0xA,
        (
            "どうやら干物を作ったり、\x01",
            "食べられる野草なんかを採って\x01",
            "凌いでたみてえだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0xA,
        "まったく、見上げた根性してやがるぜ。\x02",
    )

    CloseMessageWindow()

    label("loc_12BE")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_133D")

    label("loc_12CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_133D")
    TurnDirection(0xFE, 0x101, 0)

    #C0004
    ChrTalk(
        0xFE,
        "ロイド団員、気を付けてな。\x02",
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0xFE,
        (
            "俺たちはここで\x01",
            "待たせてもらうから、\x01",
            "幻獣のことは任せたぞ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_133D")

    Jump("loc_1111")

    label("loc_1342")

    TalkEnd(0xFE)
    Return()

    # Function_3_1104 end

    def Function_4_1346(): pass

    label("Function_4_1346")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x191, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x190, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_137F")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x344, 0x0)"), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x345, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x346, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x347, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_137F")
    Call(0, 23)
    Return()

    label("loc_137F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1740")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x344, 0x0)"), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x345, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x346, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x347, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_13B3")
    Jump("loc_1740")

    label("loc_13B3")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x344, 0x0)"), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x345, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x346, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x347, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1740")
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x8, 0x101, 500)

    #C0006
    ChrTalk(
        0xFE,
        "ロイド君、それは……\x02",
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x101,
        (
            "#00004Fええ、間違いなく釣具の\x01",
            "パーツだと思うんですけど、\x01",
            "すごく綺麗ですよね。\x02\x03",

            "#00000F四天王から取り返した釣り場で\x01",
            "珍しい魚を釣ったんですけど……\x01",
            "その魚が吐き出したんですよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0xFE,
        "……間違いありません。\x02",
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0xFE,
        (
            "それはかつて、旅の凄腕釣師が\x01",
            "使っていた伝説の釣具のパーツです。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0xFE,
        (
            "彼がクロスベルを去る時、\x01",
            "この地に封印されたと\x01",
            "聞いていましたが……\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0xFE,
        (
            "まさか、\x01",
            "このような形で見つかるとは！\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x101,
        (
            "#00005Fそ、そんなに\x01",
            "凄いものだったんですか……\x02\x03",

            "#00003Fでもどうしましょう。\x01",
            "なら、その人に返した方が……\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0xFE,
        "いえ、その必要はありません。\x02",
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0xFE,
        (
            "……なぜなら彼は言いました。\x01",
            "その釣具は見つけた者が使えと。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0xFE,
        (
            "ロイド君、\x01",
            "パーツは全部で４つあります。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0xFE,
        (
            "その全てを手に入れたら\x01",
            "どうか私のところへ来て下さい。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0xFE,
        (
            "私ならそのパーツを\x01",
            "組み上げることができます。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x101,
        (
            "#00012Fな、なるほど……\x01",
            "分かりました、覚えておきます。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    SetScenarioFlags(0x1C0, 1)
    TalkEnd(0xFE)
    Return()

    label("loc_1740")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_17C7")
    TurnDirection(0xFE, 0x101, 0)

    #C0019
    ChrTalk(
        0xFE,
        (
            "かつて封印された伝説の釣具が\x01",
            "このような時に現れるとは……\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0xFE,
        (
            "ふむ、ロイド君。\x01",
            "これは運命かもしれませんよ？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E10")

    label("loc_17C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_17D5")
    Jump("loc_1E10")

    label("loc_17D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_19B0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x191, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1907")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x190, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_189F")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x344, 0x0)"), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x345, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x346, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x347, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1814")
    Jump("loc_189A")

    label("loc_1814")


    #C0021
    ChrTalk(
        0xFE,
        (
            "いやぁ、あのお方に会えるなんて\x01",
            "楽しみで仕方がありませんねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0xFE,
        (
            "うふふ、釣皇倶楽部の皆さん、\x01",
            "笑っていられるのも今の内ですよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_189A")

    Jump("loc_1902")

    label("loc_189F")

    TurnDirection(0xFE, 0x101, 0)

    #C0023
    ChrTalk(
        0xFE,
        (
            "ロイド君、そのアクアルーラーで\x01",
            "レイクロードを打ち破って下さい！\x01",
            "――お願いしましたよ！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1902")

    Jump("loc_19AB")

    label("loc_1907")

    TurnDirection(0xFE, 0x101, 0)

    #C0024
    ChrTalk(
        0xFE,
        (
            "《釣皇スレイヤー》ロイド師。\x01",
            "この度は本当に素晴らしい\x01",
            "活躍をありがとうございました。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0xFE,
        (
            "うふふ、今回の爆釣勝負は、\x01",
            "末代まで語り継がせてもらいますよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19AB")

    Jump("loc_1E10")

    label("loc_19B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_19BE")
    Jump("loc_1E10")

    label("loc_19BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_19CC")
    Jump("loc_1E10")

    label("loc_19CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_19DA")
    Jump("loc_1E10")

    label("loc_19DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1A54")

    #C0026
    ChrTalk(
        0xFE,
        (
            "支部長やコパン君が\x01",
            "何度挑んでも勝てないなんて……\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0xFE,
        (
            "まるで、悪い夢でも\x01",
            "見させられている気分ですよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E10")

    label("loc_1A54")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1C1E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17A, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1AE8")

    #C0028
    ChrTalk(
        0xFE,
        (
            "皆さんが来てくれて、\x01",
            "心の底からホッとしましたよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0xFE,
        (
            "昨日からいつ襲ってくるのかと、\x01",
            "不安でたまりませんでしたからね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C19")

    label("loc_1AE8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1BA7")

    #C0030
    ChrTalk(
        0xFE,
        (
            "さて、私もぼちぼち修行を\x01",
            "再開するとしましょうかね。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0xFE,
        (
            "まだ四天王を誰１人として\x01",
            "倒せていないのは私だけ……\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0xFE,
        (
            "そろそろ、本気を出して\x01",
            "汚名を返上させてもらいますよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1C19")

    label("loc_1BA7")


    #C0033
    ChrTalk(
        0xFE,
        (
            "まだ四天王を誰１人として\x01",
            "倒せていないのは私だけ……\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0xFE,
        (
            "そろそろ、本気を出して\x01",
            "汚名返上させてもらいますよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C19")

    Jump("loc_1E10")

    label("loc_1C1E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1CBC")

    #C0035
    ChrTalk(
        0xFE,
        (
            "コパン君……\x01",
            "あの幻のノーブルカルプを\x01",
            "よくもあれだけ釣れますねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0xFE,
        (
            "ふむむ、早くも\x01",
            "修行の成果というわけですか。\x01",
            "私も負けられませんよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E10")

    label("loc_1CBC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1D64")

    #C0037
    ChrTalk(
        0xFE,
        (
            "さてと、私も少しは\x01",
            "皆さんのお役に立てるよう\x01",
            "腕を磨くとしましょうか。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0xFE,
        (
            "せめて『生業釣り師』クラスに\x01",
            "ならないと、サバイバルも\x01",
            "できませんからねぇ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E10")

    label("loc_1D64")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1DF9")

    #C0039
    ChrTalk(
        0xFE,
        (
            "釣公師団の看板……\x01",
            "何としても再び元の事務所に\x01",
            "掲げないといけませんねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0xFE,
        (
            "このままでは、我らが団長にも\x01",
            "申し訳が立ちませんよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E10")

    label("loc_1DF9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_1E07")
    Jump("loc_1E10")

    label("loc_1E07")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_1E10")

    label("loc_1E10")

    TalkEnd(0xFE)
    Return()

    # Function_4_1346 end

    def Function_5_1E14(): pass

    label("Function_5_1E14")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_1E25")
    Jump("loc_239F")

    label("loc_1E25")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1F04")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x191, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1EA7")

    #C0041
    ChrTalk(
        0xFE,
        (
            "釣公師団の\x01",
            "リーサルウエポンッスか……\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0xFE,
        (
            "俺も会ったことはないんスけど、\x01",
            "一体どんな人なんスかね～。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1EFF")

    label("loc_1EA7")


    #C0043
    ChrTalk(
        0xFE,
        (
            "よ～し、\x01",
            "オレも負けてられないッスよ！\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0xFE,
        (
            "いつか必ず、\x01",
            "釣皇倶楽部にリベンジッス！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1EFF")

    Jump("loc_239F")

    label("loc_1F04")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_1F12")
    Jump("loc_239F")

    label("loc_1F12")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1F76")

    #C0045
    ChrTalk(
        0xFE,
        (
            "自分はもっと……\x01",
            "もっとやれるはずなんス！\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0xFE,
        (
            "悔しい……\x01",
            "ホントに悔しいッスよ！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_239F")

    label("loc_1F76")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_1F84")
    Jump("loc_239F")

    label("loc_1F84")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2008")

    #C0047
    ChrTalk(
        0xFE,
        (
            "うう～、自分はなぜ何度挑戦しても\x01",
            "《竜宮》に勝てないんスか！\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0xFE,
        (
            "オレの何が……\x01",
            "いったい何が悪いというんスか！？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_239F")

    label("loc_2008")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_20E3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17A, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2094")

    #C0049
    ChrTalk(
        0xFE,
        (
            "それにしてもあの化物、\x01",
            "見れば見るほど不気味なんスよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0xFE,
        (
            "おまけにデカイし……\x01",
            "もうカンベンして欲しいッス。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20DE")

    label("loc_2094")


    #C0051
    ChrTalk(
        0xFE,
        "さあ、遅れた分を取り戻すッスよ～。\x02",
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0xFE,
        "目指せ、『竜宮キラー』ッス！\x02",
    )

    CloseMessageWindow()

    label("loc_20DE")

    Jump("loc_239F")

    label("loc_20E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2219")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_219F")

    #C0053
    ChrTalk(
        0xFE,
        (
            "うおっ、またノーブルカルプを\x01",
            "釣ってしまったッス。\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0xFE,
        (
            "クロスベルでは相当な\x01",
            "レア魚のはずなんスけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0xFE,
        (
            "う～ん、やっぱり何かが\x01",
            "おかしい気がするッスね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2214")

    label("loc_219F")


    #C0056
    ChrTalk(
        0xFE,
        (
            "ノーブルカルプ、\x01",
            "何か以前と比べて\x01",
            "数が増えたっぽい気が……\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0xFE,
        (
            "クロスベルの生態系に\x01",
            "何かが起こってるんスかね？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2214")

    Jump("loc_239F")

    label("loc_2219")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2330")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22D4")

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
            "今日もまずはエサを付ける前に、\x01",
            "ロッドの素振り１０００回からッス！\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0xFE,
        (
            "この特訓、けっこう\x01",
            "腕力が鍛えられていいんスよ～！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_232B")

    label("loc_22D4")


    #C0061
    ChrTalk(
        0xFE,
        (
            "努力を怠る者に\x01",
            "女神は微笑まないッスからね～！\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0xFE,
        "釣師は日々、精進あるのみッス！\x02",
    )

    CloseMessageWindow()

    label("loc_232B")

    Jump("loc_239F")

    label("loc_2330")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2388")

    #C0063
    ChrTalk(
        0xFE,
        "さあ、さっそく釣りの修行開始ッス。\x02",
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0xFE,
        "今に見てろ、釣皇倶楽部ッス！\x02",
    )

    CloseMessageWindow()
    Jump("loc_239F")

    label("loc_2388")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_2396")
    Jump("loc_239F")

    label("loc_2396")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_239F")

    label("loc_239F")

    TalkEnd(0xFE)
    Return()

    # Function_5_1E14 end

    def Function_6_23A3(): pass

    label("Function_6_23A3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_243A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_23C1")
    Call(0, 7)
    Jump("loc_2435")

    label("loc_23C1")


    #C0065
    ChrTalk(
        0xB,
        (
            "くそっ、俺は敵だというのに\x01",
            "何故こいつはこんなにも\x01",
            "フレンドリーなのだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0xB,
        "こんな珍現象、認めてたまるものか！\x02",
    )

    CloseMessageWindow()

    label("loc_2435")

    Jump("loc_245F")

    label("loc_243A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_2448")
    Jump("loc_245F")

    label("loc_2448")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_END)), "loc_2456")
    Jump("loc_245F")

    label("loc_2456")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_245F")

    label("loc_245F")

    TalkEnd(0xFE)
    Return()

    # Function_6_23A3 end

    def Function_7_2463(): pass

    label("Function_7_2463")

    OP_4B(0xB, 0xFF)
    OP_4B(0xA, 0xFF)

    #C0067
    ChrTalk(
        0xA,
        (
            "まさかレイクロード、\x01",
            "アンタがここにいるとはなァ。\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0xB,
        (
            "フン、ここを使っていいと\x01",
            "言ったのは貴様だろう。\x01",
            "……文句は言わせんぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0xA,
        "もちろんだ、そういう約束だしな。\x02",
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0xA,
        (
            "だが、ここでは不便も多いだろう。\x01",
            "いつでも支部の方に来てくれたって\x01",
            "いいんだからな？\x02",
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
            "フ、フンッ……\x01",
            "俺たちは貴様らに気遣われるほど\x01",
            "落ちぶれてはいない。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    ClearChrFlags(0xB, 0x10)
    ClearChrFlags(0xA, 0x10)
    OP_4C(0xB, 0xFF)
    OP_4C(0xA, 0xFF)
    Return()

    # Function_7_2463 end

    def Function_8_25E2(): pass

    label("Function_8_25E2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_267E")

    #C0072
    ChrTalk(
        0xC,
        (
            "ふぅ……忘れていましたけど\x01",
            "この小屋はあのセルダンという男が\x01",
            "借りているんでしたわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0xC,
        (
            "せっかくの２人の時間を……\x01",
            "許すまじですわ！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_26A3")

    label("loc_267E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_268C")
    Jump("loc_26A3")

    label("loc_268C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_END)), "loc_269A")
    Jump("loc_26A3")

    label("loc_269A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_26A3")

    label("loc_26A3")

    TalkEnd(0xFE)
    Return()

    # Function_8_25E2 end

    def Function_9_26A7(): pass

    label("Function_9_26A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 4)), scpexpr(EXPR_END)), "loc_26D3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 6)), scpexpr(EXPR_END)), "loc_26C1")
    Call(0, 20)
    Jump("loc_26CE")

    label("loc_26C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_26CE")
    Call(0, 19)

    label("loc_26CE")

    Jump("loc_2754")

    label("loc_26D3")

    EventBegin(0x2)
    SetChrName("")

    #A0074
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "蒼い花が咲いている。\x07\x00\x02",
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
            "#00000F（なんていうか、綺麗な花だな。\x01",
            "  淡く輝いているみたいだけど……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x168, 4)
    EventEnd(0x3)

    label("loc_2754")

    Return()

    # Function_9_26A7 end

    def Function_10_2755(): pass

    label("Function_10_2755")

    EventBegin(0x1)

    #C0076
    ChrTalk(
        0x101,
        (
            "#00003F（これで幻獣は２体とも\x01",
            "  倒したわけだけど……\x01",
            "  なにかが気になるな。）\x02\x03",

            "#00000Fみんな、ちょっと現場を\x01",
            "改めて調べ直してもいいかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0x102,
        (
            "#00100F確かに、ここでするべきことは\x01",
            "まだありそうな気もするわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0x103,
        "#00200Fでは、早速戻って調べましょう。\x02",
    )

    CloseMessageWindow()
    SetChrPos(0x0, 91500, 0, 0, 90)
    EventEnd(0x4)
    Return()

    # Function_10_2755 end

    def Function_11_286B(): pass

    label("Function_11_286B")

    EventBegin(0x1)
    #Sound(2094, 255, 100, 0)    #voice#Lloyd

    #C0079
    ChrTalk(
        0x101,
        "#0000Fここなら釣れそうだな。\x02",
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
            "釣りをしますか？\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "釣りをする\x01",      # 0
            "やめる\x01",          # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    OP_6F(0x1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_293A")
    OP_E2(0x2)
    MiniGame(0x6, 0x18, 0x73D2, 0x0, 0xD2, 0x5A, 0x933A, 0xFFFFFC18, 0x76C)

    label("loc_293A")

    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    # Function_11_286B end

    def Function_12_293F(): pass

    label("Function_12_293F")

    TalkBegin(0xFF)
    Sound(807, 0, 100, 0)
    SetChrName("")

    #A0081
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "扉には固く鍵が掛けられている。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)
    Return()

    # Function_12_293F end

    def Function_13_2979(): pass

    label("Function_13_2979")

    SetMapFlags(0x80)
    SetMapFlags(0x8000000)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x31, 2)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_29AB")
    SetScenarioFlags(0x31, 2)

    label("loc_29AB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_29F1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 2)), scpexpr(EXPR_END)), "loc_29EB")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_29E0")
    Sound(2499, 255, 100, 0)    #voice#Noel
    Jump("loc_29E6")

    label("loc_29E0")

    Sound(3537, 255, 100, 0)    #voice#Noel

    label("loc_29E6")

    Jump("loc_29F1")

    label("loc_29EB")

    Sound(3344, 255, 100, 0)    #voice#Lloyd

    label("loc_29F1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2CAE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_END)), "loc_2A6A")
    MenuCmd(0, 0)
    MenuCmd(1, 0, "メルカバに乗り込む")
    MenuCmd(1, 0, "やめる")
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2A4A"),
        (SWITCH_DEFAULT, "loc_2A5B"),
    )


    label("loc_2A4A")

    SetScenarioFlags(0x22, 0)
    NewScene("e3020", 0, 0, 0)
    IdleLoop()
    Jump("loc_2A65")

    label("loc_2A5B")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2A65")

    Jump("loc_2CA9")

    label("loc_2A6A")

    MenuCmd(0, 0)
    MenuCmd(1, 0, "導力車で移動する")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_2A9E")
    MenuCmd(1, 0, "導力車で休憩する")

    label("loc_2A9E")

    MenuCmd(1, 0, "やめる")
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2AD2"),
        (1, "loc_2BD6"),
        (2, "loc_2C67"),
        (SWITCH_DEFAULT, "loc_2C9F"),
    )


    label("loc_2AD2")

    SetMapObjFrame(0x8, "light", 0x0, 0x1)
    OP_74(0x8, 0x1E)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2B03")
    OP_70(0x8, 0x12C)
    OP_71(0x8, 0x12C, 0x14A, 0x0, 0x0)
    Jump("loc_2B13")

    label("loc_2B03")

    OP_70(0x8, 0xF0)
    OP_71(0x8, 0xF0, 0x10E, 0x0, 0x0)

    label("loc_2B13")

    Sound(462, 0, 100, 0)
    SoundLoad(2500)
    SoundLoad(3538)
    SoundLoad(3345)
    Sleep(700)
    FadeToDark(300, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x2E, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B69")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2B69")

    FadeToDark(0, 0, -1)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D4, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B8C")
    Sound(461, 0, 100, 0)

    label("loc_2B8C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2BAC")
    OP_70(0x8, 0x14A)
    OP_71(0x8, 0x14A, 0x12C, 0x0, 0x0)
    Jump("loc_2BBC")

    label("loc_2BAC")

    OP_70(0x8, 0x10E)
    OP_71(0x8, 0x10E, 0xF0, 0x0, 0x0)

    label("loc_2BBC")

    Sleep(1000)
    OP_0D()
    SetMapObjFrame(0x8, "light", 0x1, 0x1)
    OP_70(0x8, 0x0)
    Jump("loc_29F1")

    label("loc_2BD6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_2C48")
    OP_57(0x0)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_5A()
    Sound(13, 0, 100, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 0)), scpexpr(EXPR_END)), "loc_2C0B")
    OP_32(0xFF, 0xFF, 0x0)
    Jump("loc_2C23")

    label("loc_2C0B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_2C1E")
    OP_32(0xFF, 0xFE, 0x0)
    Jump("loc_2C23")

    label("loc_2C1E")

    OP_32(0xFF, 0xFA, 0x0)

    label("loc_2C23")

    OP_6A(0x0, 0x0)
    Sleep(3500)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2C62")

    label("loc_2C48")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_2C58")
    OP_AF(0xFB)
    Jump("loc_2C62")

    label("loc_2C58")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2C62")

    Jump("loc_2CA9")

    label("loc_2C67")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C80")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2C9A")

    label("loc_2C80")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_2C90")
    OP_AF(0xFB)
    Jump("loc_2C9A")

    label("loc_2C90")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2C9A")

    Jump("loc_2CA9")

    label("loc_2C9F")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2CA9")

    Jump("loc_29F1")

    label("loc_2CAE")

    ClearMapFlags(0x8000000)
    OP_60(0x0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    # Function_13_2979 end

    def Function_14_2CBC(): pass

    label("Function_14_2CBC")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(0, 0, -1)
    Sleep(100)
    Sound(459, 0, 100, 0)
    Sleep(2000)
    StopSound(459, 1000, 100)
    Sound(492, 0, 70, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 2)), scpexpr(EXPR_END)), "loc_2D17")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2D0C")
    Sound(2502, 255, 100, 0)    #voice#Noel
    Jump("loc_2D12")

    label("loc_2D0C")

    Sound(2503, 255, 100, 0)    #voice#Noel

    label("loc_2D12")

    Jump("loc_2D3B")

    label("loc_2D17")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2D35")
    Sound(3347, 255, 100, 0)    #voice#Lloyd
    Jump("loc_2D3B")

    label("loc_2D35")

    Sound(3348, 255, 100, 0)    #voice#Lloyd

    label("loc_2D3B")

    Sleep(500)
    FadeToBright(500, 0)
    OP_0D()
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_14_2CBC end

    def Function_15_2D50(): pass

    label("Function_15_2D50")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_2D5A")
    Return()

    label("loc_2D5A")

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
            "大型の魔獣が徘徊#4Rはいかい#している。\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【退治する】\x01",      # 0
            "【やめる】\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (1, "loc_2E3C"),
        (SWITCH_DEFAULT, "loc_2E55"),
    )


    label("loc_2E3C")

    Sleep(500)
    OP_E2(0x2)
    OP_90(0x0, 106900, 0, 4400, 90)
    EventEnd(0x5)
    Return()

    label("loc_2E55")

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
        (2, "loc_2F17"),
        (1, "loc_2F1C"),
        (SWITCH_DEFAULT, "loc_2F1F"),
    )


    label("loc_2F17")

    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    label("loc_2F1C")

    OP_B9(0x0)
    Return()

    label("loc_2F1F")

    Call(0, 18)
    Return()

    # Function_15_2D50 end

    def Function_16_2F23(): pass

    label("Function_16_2F23")

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

    def lambda_300F():
        OP_9B(0x0, 0x101, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_300F)
    Sleep(0)

    def lambda_3027():
        OP_9B(0x0, 0x102, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_3027)
    Sleep(0)

    def lambda_303F():
        OP_9B(0x0, 0x103, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_303F)
    Sleep(0)

    def lambda_3057():
        OP_9B(0x0, 0x104, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_3057)
    Sleep(0)

    def lambda_306F():
        OP_9B(0x0, 0x109, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_306F)
    Sleep(0)

    def lambda_3087():
        OP_9B(0x0, 0x105, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_3087)
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_31A0")

    #C0083
    ChrTalk(
        0x109,
        "#10111F#6P（あ……！）\x02",
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x101,
        "#00013F#5P（あれが《幻獣》か……！）\x02",
    )

    CloseMessageWindow()
    Jump("loc_31DE")

    label("loc_31A0")


    #C0085
    ChrTalk(
        0x105,
        "#10305F#6P（おっと……）\x02",
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x101,
        "#00013F#5P（いたか……！）\x02",
    )

    CloseMessageWindow()

    label("loc_31DE")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_34EC")

    #C0087
    ChrTalk(
        0x104,
        (
            "#00303F#9P（報告通り、結構デケェな……）\x02\x03",

            "#00301F（ティオすけ、場の歪みはどうだ？）\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0x103,
        (
            "#00203F#9P（時・空・幻……\x01",
            "  上位三属性の発現を確認しました。）\x02\x03",

            "#00201F（今のところ原因は不明です。）\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0x102,
        "#00108F#9P（そう……）\x02",
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

    def lambda_33A3():
        TurnDirection(0x101, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_33A3)
    Sleep(0)

    def lambda_33B3():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_33B3)
    Sleep(0)

    def lambda_33C3():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_33C3)
    Sleep(0)

    def lambda_33D3():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_33D3)
    Sleep(0)

    def lambda_33E3():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_33E3)
    Sleep(0)

    def lambda_33F3():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_33F3)
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
            "#10301F#6P（それで……\x01",
            "  結局どうするんだい？）\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x101,
        (
            "#00003F#11P（警備隊の報告では\x01",
            "  かなり危険なタイプみたいだ……）\x02\x03",

            "#00013F（退治するなら慎重に仕掛けよう。）\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0x109,
        "#10101F#12P（了解しました……！）\x02",
    )

    CloseMessageWindow()
    Jump("loc_3685")

    label("loc_34EC")


    #C0093
    ChrTalk(
        0x102,
        (
            "#00101F#9P（ティオちゃん……\x01",
            "  場の歪みの方はどう？）\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x103,
        (
            "#00203F#9P（同じく上位三属性の発現を確認……）\x02\x03",

            "#00201F（やはり原因は不明です。）\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0x104,
        "#00306F#9P（やっぱりか……）\x02",
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0x105,
        (
            "#10308F#9P（どうやら幻獣そのものが\x01",
            "  原因じゃなさそうだけど……）\x02",
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
            "#10101F#6P（ロイドさん……\x01",
            "  さっそく仕掛けますか？）\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x101,
        "#00013F#5P（ああ、慎重に行こう……！）\x02",
    )

    CloseMessageWindow()

    label("loc_3685")

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

    # Function_16_2F23 end

    def Function_17_36C0(): pass

    label("Function_17_36C0")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x168, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A73")
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
    Jump("loc_3A8D")

    label("loc_3A73")

    OP_75(0x6, 0x2, 0x0)
    OP_75(0x7, 0x2, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)

    label("loc_3A8D")

    Battle("BattleInfo_4EC", 0x0, 0x0, 0x0, 0x28, 0xFF)
    FadeToDark(0, 0, -1)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x10, 0x80)
    SetMapObjFlags(0x6, 0x4)
    SetMapObjFlags(0x7, 0x4)
    SetScenarioFlags(0x168, 1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3B21")
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
    Jump("loc_3B24")

    label("loc_3B21")

    Call(0, 18)

    label("loc_3B24")

    Return()

    # Function_17_36C0 end

    def Function_18_3B25(): pass

    label("Function_18_3B25")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3EF5")

    #C0099
    ChrTalk(
        0x101,
        (
            "#00006F#5Pくっ……\x01",
            "さすがに手強かったな。\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0x102,
        (
            "#00108F#6Pそれにやっぱり……\x01",
            "不思議な消え方をしたわね。\x02",
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

    def lambda_3D50():
        TurnDirection(0x101, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3D50)
    Sleep(50)

    def lambda_3D60():
        TurnDirection(0x102, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_3D60)
    Sleep(50)

    def lambda_3D70():
        TurnDirection(0x103, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_3D70)
    Sleep(50)

    def lambda_3D80():
        TurnDirection(0x104, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_3D80)
    Sleep(50)

    def lambda_3D90():
        TurnDirection(0x109, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_3D90)
    Sleep(50)

    def lambda_3DA0():
        TurnDirection(0x105, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_3DA0)
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
            "#10108F#12Pティオちゃん。\x01",
            "“場の歪み”の方は？\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x103,
        (
            "#00206F#6P……駄目です。\x01",
            "上位三属性が働いたままです。\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0x104,
        (
            "#00301F#5Pったく……\x01",
            "いったい何が原因なんだ？\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0x105,
        (
            "#10303F#11Pどうやら《幻獣》そのものが\x01",
            "原因じゃなさそうだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0x101,
        (
            "#00013F#11P……やっぱりもう一方も\x01",
            "当たってみる必要がありそうだな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_430C")

    label("loc_3EF5")


    #C0106
    ChrTalk(
        0x105,
        (
            "#10306F#6Pやれやれ……\x01",
            "こっちの方も手強かったね。\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0x109,
        "#10101F#6Pでも、消え方は同じ……\x02",
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

    def lambda_3F99():
        TurnDirection(0x101, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3F99)
    Sleep(50)

    def lambda_3FA9():
        TurnDirection(0x102, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_3FA9)
    Sleep(50)

    def lambda_3FB9():
        TurnDirection(0x103, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_3FB9)
    Sleep(50)

    def lambda_3FC9():
        TurnDirection(0x104, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_3FC9)
    Sleep(50)

    def lambda_3FD9():
        TurnDirection(0x109, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_3FD9)
    Sleep(50)

    def lambda_3FE9():
        TurnDirection(0x105, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_3FE9)
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
            "#00301F#5Pやっぱり“場の歪み”ってのは\x01",
            "続いたままかよ？\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0x103,
        (
            "#00203F#6Pそうですね……\x02\x03",

            "#00201Fただ、何か具体的な原因が\x01",
            "ありそうな気はします。\x02",
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
            "#00005F#11P具体的な原因……\x01",
            "たとえばどんな？\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0x103,
        (
            "#00206F#6P……その……\x01",
            "先ほどからわたしの感覚が\x01",
            "“歪み”に撹乱されていて……\x02\x03",

            "#00200Fむしろ、皆さんの方が原因を\x01",
            "見つけられるかもしれません。\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0x102,
        "#00105F#5Pそ、そう？\x02",
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0x101,
        (
            "#00003F#11Pよし……\x01",
            "この付近を捜索してみよう。\x02\x03",

            "#00000F“場の歪み”をもたらしているものが\x01",
            "必ずあるはずだ。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_424C():
        TurnDirection(0x101, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_424C)
    Sleep(50)

    def lambda_425C():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_425C)
    Sleep(50)

    def lambda_426C():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_426C)
    Sleep(50)

    def lambda_427C():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_427C)
    Sleep(50)

    def lambda_428C():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_428C)
    Sleep(50)

    def lambda_429C():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_429C)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)

    #C0114
    ChrTalk(
        0x109,
        "#10100F#6P了解しました！\x02",
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0x104,
        "#00300F#5P手当たり次第、探してみっか！\x02",
    )

    CloseMessageWindow()
    OP_29(0xA6, 0x1, 0x3)

    label("loc_430C")

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
            "東クロスベル街道方面の幻獣を倒した！\x07\x00\x02",
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_43A0")
    ModifyEventFlags(1, 3, 0x80)

    label("loc_43A0")

    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_D7(0x20)
    OP_D7(0x21)
    OP_D7(0x22)
    OP_D7(0x23)
    OP_37()
    EventEnd(0x5)
    Return()

    # Function_18_3B25 end

    def Function_19_43B0(): pass

    label("Function_19_43B0")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4791")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    Sleep(300)

    #A0117
    AnonymousTalk(
        0x101,
        "#00005Fこの花は……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x168, 3)), scpexpr(EXPR_END)), "loc_45BF")

    #A0118
    AnonymousTalk(
        0x102,
        (
            "#00108F確か、ウルスラ間道方面の\x01",
            "岸辺でも咲いていたような……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0119
    AnonymousTalk(
        0x104,
        "#00305Fああ、そういや見かけたな。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_4663")

    label("loc_45BF")


    #A0120
    AnonymousTalk(
        0x105,
        (
            "#10302F確か、ウルスラ間道方面の\x01",
            "岸辺でも咲いていなかったっけ？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0121
    AnonymousTalk(
        0x101,
        "#00011Fそ、そうだったか？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0122
    AnonymousTalk(
        0x102,
        (
            "#00108Fええ、確かに私も\x01",
            "見たような気がするけど……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_4663")


    #A0123
    AnonymousTalk(
        0x109,
        (
            "#10109Fすごく綺麗な花ですね……\x02\x03",

            "#10102F……見たことがありませんけど\x01",
            "なんていう名前なんでしょうか？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0124
    AnonymousTalk(
        0x101,
        "#00001Fうーん……\x02",
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
            "#00003F#11P（……まさかとは思うけど……）\x02\x03",

            "#00001F（いや、試す価値はあるか？）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x161, 2)
    OP_29(0xA6, 0x1, 0x4)
    Jump("loc_4847")

    label("loc_4791")

    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    Sleep(300)

    #A0126
    AnonymousTalk(
        0x101,
        (
            "#00003F#11P（……まさかとは思うけど……）\x02\x03",

            "#00001F（いや、試す価値はあるか？）\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    label("loc_4847")

    FadeToDark(300, 0, 100)
    OP_0D()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "蒼い花を摘んでみる\x01",      # 0
            "止めておく\x01",              # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_489F"),
        (1, "loc_5644"),
        (SWITCH_DEFAULT, "loc_5683"),
    )


    label("loc_489F")

    OP_9B(0x0, 0x101, 0x0, 0x2EE, 0x3E8, 0x0)
    Fade(250)
    Sound(802, 0, 100, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    OP_0D()

    #C0127
    ChrTalk(
        0x102,
        "#00105Fロイド……？\x02",
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0x105,
        (
            "#10305F#6Pなに、その花を\x01",
            "摘んでいくつもりかい？\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0x101,
        (
            "#00003F#11Pああ……\x01",
            "ちょっと可哀想だけど──\x02",
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
        "#00301F#5Pな、なんだ！？\x02",
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0x103,
        "#00205F#12Pこれは……！\x02",
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0x101,
        "#00001F#11Pくっ……！\x02",
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
        "#10111F#5Pい、今のは……\x02",
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0x102,
        "#00108F何か空間が揺らいだような……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x103, 500)

    #C0136
    ChrTalk(
        0x105,
        (
            "#10308F#6P……ティオ。\x01",
            "“場の歪み”の方は？\x02",
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
            "#00203F#12P……上位三属性の\x01",
            "気配が消滅しました。\x02\x03",

            "#00201F既にこの一帯に\x01",
            "異常は感じられません。\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0x101,
        "#00006F#11Pそうか……\x02",
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0x104,
        (
            "#00305F#5Pちょ、ちょっと待て。\x02\x03",

            "#00307Fまさかその蒼い花が\x01",
            "異常を引き起こしてたのかよ！？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 500)

    #C0140
    ChrTalk(
        0x105,
        (
            "#10304F#6Pまあ、そういう事だろうね。\x02\x03",

            "#10300F……そのちっぽけな花程度に\x01",
            "そんな力があるとも思えないけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0x102,
        "#00101Fし、信じられない……\x02",
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0x109,
        (
            "#10101F#5Pい、いったい\x01",
            "どういう花なんでしょうか？\x02",
        )
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0x103,
        (
            "#00206F#12P……もう、その花からは\x01",
            "おかしな気配は感じませんが……\x02\x03",

            "#00200Fとりあえずどこかで\x01",
            "調べてもらった方がいいのでは？\x02",
        )
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0x101,
        (
            "#00008F#11Pそうだな……\x02\x03",

            "#00003F……医科大学あたりも\x01",
            "ちょっと専門が違うだろうし。\x02",
        )
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0x102,
        (
            "#00100Fと、とにかく失くさないよう\x01",
            "保管しておきましょう。\x02\x03",

            "心当たりが見つかったら\x01",
            "調べてもらえばいいじゃない？\x02",
        )
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0x101,
        "#00006F#11Pああ、そうするか。\x02",
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
        "#10303F#6P……ふむ………\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    def lambda_5025():
        TurnDirection(0x101, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_5025)
    Sleep(50)

    def lambda_5035():
        TurnDirection(0x102, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_5035)
    Sleep(50)

    def lambda_5045():
        TurnDirection(0x103, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_5045)
    Sleep(50)

    def lambda_5055():
        TurnDirection(0x104, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_5055)
    Sleep(50)

    def lambda_5065():
        TurnDirection(0x109, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_5065)
    Sleep(50)

    def lambda_5075():
        TurnDirection(0x105, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_5075)
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
        "#00005F#11Pワジ……？\x02",
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0x109,
        "#10101F#5P何か心当たりでもあるの？\x02",
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0x105,
        (
            "#10303F#6Pいや……\x01",
            "僕のウロ覚えかもしれないけど。\x02\x03",

            "#10301F教会の聖典に、不思議な蒼い花の\x01",
            "言い伝えがあった気がする。\x02",
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
        "#00011F#11Pえっ……！？\x02",
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0x104,
        "#00305F#5Pおいおい、マジかよ！？\x02",
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0x105,
        (
            "#10306F#6Pいや、大分前に流し読みした時に\x01",
            "見かけた気がするんだけど……\x02\x03",

            "#10300Fエリィとか心当たりはないかい？\x02",
        )
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0x102,
        (
            "#00112F#11P私もさすがに聖典の全てに\x01",
            "目は通していないけど……\x02\x03",

            "#00103F……でも、確かに\x01",
            "そんな下りを読んだ気がするわ。\x02\x03",

            "#00108F不思議な力を持っているという\x01",
            "『蒼き花』の言い伝えを……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x102, 500)

    #C0155
    ChrTalk(
        0x109,
        (
            "#10111F#6Pそ、それって……\x01",
            "ビンゴなんじゃないですか？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 500)

    #C0156
    ChrTalk(
        0x103,
        (
            "#00201F#12P少なくとも教会関係者に\x01",
            "確認する価値はありそうです。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_53D6():
        TurnDirection(0x101, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_53D6)
    Sleep(50)

    def lambda_53E6():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_53E6)
    Sleep(50)

    def lambda_53F6():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_53F6)
    Sleep(50)

    def lambda_5406():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_5406)
    Sleep(50)

    def lambda_5416():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_5416)
    Sleep(50)

    def lambda_5426():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_5426)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7C, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_54E4")

    #C0157
    ChrTalk(
        0x101,
        (
            "#00003F#11P……そうだな。\x02\x03",

            "#00000Fマーブル先生かリースさんの\x01",
            "どちらかに相談してみるか。\x02",
        )
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0x102,
        (
            "#00104Fそうね……\x01",
            "どちらも適任だと思うわ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5593")

    label("loc_54E4")


    #C0159
    ChrTalk(
        0x101,
        (
            "#00003F#11P……そうだな。\x02\x03",

            "#00000Fやっぱりマーブル先生が\x01",
            "一番相談しやすいかもしれない。\x02",
        )
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0x102,
        (
            "#00104Fええ、適任だと思うわ。\x02\x03",

            "#00108F（“彼女”にも相談できそうだけど……）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5593")


    #C0161
    ChrTalk(
        0x104,
        (
            "#00300F#5Pおーし、そんじゃあ\x01",
            "クロスベル大聖堂に向かうか！\x02",
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
    Jump("loc_5683")

    label("loc_5644")

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
    Jump("loc_5683")

    label("loc_5683")

    Return()

    # Function_19_43B0 end

    def Function_20_5684(): pass

    label("Function_20_5684")

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
            "#10100Fそ、そういえば……\x02\x03",

            "こっちの花も\x01",
            "摘んだ方がいいんでしょうか？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0163
    AnonymousTalk(
        0x101,
        (
            "#00000Fいや……\x01",
            "こちらの方は様子を見よう。\x02\x03",

            "ひょっとしたら貴重な\x01",
            "サンプルになるかもしれない。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0164
    AnonymousTalk(
        0x103,
        (
            "#00200F……確かに。\x01",
            "摘んだら力を失うみたいですし。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0165
    AnonymousTalk(
        0x102,
        (
            "#00100Fでも……また幻獣が現れたら\x01",
            "摘むしかないかもしれないわね。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0166
    AnonymousTalk(
        0x104,
        "#00300Fま、そん時はそん時だ。\x02",
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

    # Function_20_5684 end

    def Function_21_5975(): pass

    label("Function_21_5975")

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
            "う～ん、しかし\x01",
            "気味の悪い魔獣ですねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0x9,
        (
            "#6Pあ、あんなのがこっちに来たら\x01",
            "ひとたまりもないッスよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0xA,
        (
            "ああ、そうなったら\x01",
            "速攻で避難しないとなァ。\x02",
        )
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0xA,
        (
            "だが、とりあえず今は\x01",
            "警備隊が来るのを待って……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0171
    ChrTalk(
        0xA,
        "おお、君は……ロイド団員！\x02",
    )

    CloseMessageWindow()
    OP_68(37180, 1400, -14790, 4000)
    MoveCamera(33, 33, 0, 4000)
    OP_6E(600, 4000)
    SetCameraDistance(14430, 4000)

    def lambda_5B21():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_5B21)

    def lambda_5B2E():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_5B2E)
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

    def lambda_5BBC():
        OP_95(0xFE, 36720, 0, -14030, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5BBC)
    Sleep(300)

    def lambda_5BD9():
        OP_95(0xFE, 36720, 0, -15170, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5BD9)
    Sleep(300)

    def lambda_5BF6():
        OP_95(0xFE, 35680, 0, -13860, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5BF6)
    Sleep(300)

    def lambda_5C13():
        OP_95(0xFE, 35680, 0, -15050, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_5C13)
    Sleep(300)

    def lambda_5C30():
        OP_95(0xFE, 34560, 0, -13930, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_5C30)
    Sleep(300)

    def lambda_5C4D():
        OP_95(0xFE, 34700, 0, -14930, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_5C4D)
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
            "#6P#00003Fお久しぶりです、セルダン支部長。\x02\x03",

            "#00001Fこちらの方に不可思議な大型魔獣、\x01",
            "《幻獣》が現れたと聞いたのですが。\x02",
        )
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0xA,
        (
            "《幻獣》……\x01",
            "ふむ、言い得て妙な表現だなァ。\x02",
        )
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0xA,
        (
            "ああ、実はその《幻獣》とやらが\x01",
            "昨日の夕方、突如沼地の奥に現れてな。\x02",
        )
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0xA,
        (
            "俺たちの方で警備隊に\x01",
            "連絡を入れさせてもらったんだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0x8,
        (
            "#11Pもしかして、\x01",
            "ロイド君たち特務支援課が\x01",
            "対処に来てくれたのですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0x102,
        (
            "#6P#00103Fはい、警備隊から依頼を受けて。\x02\x03",

            "#00101F詳しい状況を\x01",
            "聞かせてもらえますか？\x02",
        )
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0xA,
        (
            "ああ、さっきも言った通り\x01",
            "最初に確認したのは\x01",
            "昨日の夕方のことなんだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0xA,
        (
            "本当に何の前触れもなく、\x01",
            "急に奇妙な鳴き声のようなものが\x01",
            "聴こえて来てなァ。\x02",
        )
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0x9,
        (
            "#12Pずっと封鎖していた沼地の奥の方に\x01",
            "怪しい影がちらついたんで……\x02",
        )
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0x9,
        "#12Pみんなで、慎重に近づいたんスよ。\x02",
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0x8,
        (
            "#11Pそしたら、その不可思議な\x01",
            "《幻獣》とやらを見つけましてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0x8,
        (
            "#11Pそれで、慌てて警備隊に\x01",
            "報告させてもらったんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0xA,
        (
            "俺たちはすぐに逃げようと\x01",
            "思ったんだが……《幻獣》は\x01",
            "その場から動く気配がなくてなァ。\x02",
        )
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0xA,
        (
            "とりあえず、昨日から交代で\x01",
            "見張りを立てて様子を見ていたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0x103,
        "#6P#00203F……それはお疲れ様でした。\x02",
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0x109,
        (
            "#6P#10101F見張っている間、何か\x01",
            "変わったことはありましたか？\x02",
        )
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0xA,
        (
            "いや、それがまた\x01",
            "不気味なほどに何もなくてなァ。\x02",
        )
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0xA,
        (
            "遠巻きながらも敵意めいた\x01",
            "意志のようなものは感じるんだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0x9,
        (
            "#12Pなんつうか……\x01",
            "動かないんじゃなく動けないって\x01",
            "感じにも見えるッスよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0191
    ChrTalk(
        0x9,
        (
            "#12P詳しいことは\x01",
            "よく分からないッスけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0x105,
        (
            "#6P#10303Fなるほど、突如現れて\x01",
            "更にその場を離れない、か……\x02",
        )
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0x104,
        (
            "#6P#00301Fなんつうか、明らかに\x01",
            "“場の歪み”ってヤツに\x01",
            "関係してそうだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0194
    ChrTalk(
        0x101,
        (
            "#6P#00003Fああ、間違いないだろう。\x02\x03",

            "#00013Fそれじゃ、セルダン支部長。\x01",
            "早速この奥に行きたいんですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0xA,
        (
            "ああ、ヤツを\x01",
            "退治してくれるんだったな。\x02",
        )
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0xA,
        "今、鍵を開けよう。\x02",
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
            "さあ、これで大丈夫だ。\x01",
            "後はよろしく頼んだぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0x101,
        "#6P#00000Fはい、分かりました。\x02",
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

    # Function_21_5975 end

    def Function_22_641D(): pass

    label("Function_22_641D")

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
            "#6Pおお、ロイド団員。\x01",
            "《幻獣》は退治できたのかい？\x02",
        )
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0x101,
        (
            "#00006F#11Pええ、何とか。\x02\x03",

            "#00000F注意は必要だと思いますが、\x01",
            "多分しばらくは再び現れることも\x01",
            "ないと思います。\x02",
        )
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0x9,
        (
            "#5Pマジッスか……\x01",
            "それはよかったッス。\x02",
        )
    )

    CloseMessageWindow()

    #C0202
    ChrTalk(
        0x8,
        (
            "#6Pふふ、これでまた釣りに\x01",
            "専念することができますね。\x02",
        )
    )

    CloseMessageWindow()

    #C0203
    ChrTalk(
        0xA,
        "#6Pああ、本当に助かったぜ。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 0)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_695D")

    #C0204
    ChrTalk(
        0x8,
        "#6Pそうそう、それからロイド君。\x02",
    )

    CloseMessageWindow()

    #C0205
    ChrTalk(
        0x8,
        (
            "#6Pお礼と言ってはなんですが、\x01",
            "これを受け取ってくれませんか。\x02",
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
            "を受け取った。\x02",
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
        "#00005F#11Pこれは……新しい釣竿ですか？\x02",
    )

    CloseMessageWindow()

    #C0208
    ChrTalk(
        0x8,
        (
            "#6Pええ、対・釣皇倶楽部用に\x01",
            "私が組み上げたロッドなんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0209
    ChrTalk(
        0x8,
        (
            "#6Pこれがあれば、より大型の魚を\x01",
            "釣ることが可能になるはずです。\x02",
        )
    )

    CloseMessageWindow()

    #C0210
    ChrTalk(
        0x101,
        "#00002F#11Pペーターさんがこれを……\x02",
    )

    CloseMessageWindow()

    #C0211
    ChrTalk(
        0xA,
        (
            "#6Pはは、こう見えてペーターは\x01",
            "道具いじりが得意でなァ。\x02",
        )
    )

    CloseMessageWindow()

    #C0212
    ChrTalk(
        0xA,
        (
            "#6Pたまにこうやって、\x01",
            "既製品を改造したりして\x01",
            "新しい釣具を作ったりするんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0213
    ChrTalk(
        0x9,
        (
            "#5Pへへ、これで釣りの腕前が\x01",
            "からっきしってんだから、\x01",
            "何とも不思議な話ッスよね～。\x02",
        )
    )

    CloseMessageWindow()

    #C0214
    ChrTalk(
        0x8,
        (
            "#6Pそこ、コパン君。\x01",
            "余計な事を言わないように。\x02",
        )
    )

    CloseMessageWindow()

    #C0215
    ChrTalk(
        0x101,
        (
            "#00012F#11Pあはは……\x02\x03",

            "#00000Fでも本当に、こんな良い物を\x01",
            "ありがとうございます。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6F91")

    label("loc_695D")


    #C0216
    ChrTalk(
        0xA,
        "#6Pそうだ、ロイド団員。\x02",
    )

    CloseMessageWindow()

    #C0217
    ChrTalk(
        0xA,
        (
            "#6P君には伝えていなかったが、\x01",
            "釣皇倶楽部との《爆釣#4Rばくちょう#勝負》について\x01",
            "説明しておきたいんだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0218
    ChrTalk(
        0x101,
        "#00011F#11Pば、《爆釣勝負》ですか……？\x02",
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
            "#00003F#11Pなるほど、釣皇倶楽部の\x01",
            "メンバー５人と《爆釣勝負》……\x02\x03",

            "勝てば事務所と釣り場の自由を\x01",
            "取り戻すことができ……\x02\x03",

            "#00001F負ければ相手の言うがまま、ですか。\x02",
        )
    )

    CloseMessageWindow()

    #C0220
    ChrTalk(
        0xA,
        "#6Pああ、そういうことだ。\x02",
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0xA,
        (
            "#6Pまあ、とりあえず\x01",
            "勝負の方は俺たちの方で\x01",
            "何とかするつもりだからな。\x02",
        )
    )

    CloseMessageWindow()

    #C0222
    ChrTalk(
        0xA,
        (
            "#6Pロイド団員は本業の方が\x01",
            "忙しいだろうから、\x01",
            "気に留める程度で構わないぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0223
    ChrTalk(
        0x101,
        "#00000F#11Pええ、分かりました。\x02",
    )

    CloseMessageWindow()

    #C0224
    ChrTalk(
        0x8,
        "#6Pそうそう、それからロイド君。\x02",
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0x8,
        (
            "#6Pお礼と言ってはなんですが、\x01",
            "これを受け取ってくれませんか。\x02",
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
            "を受け取った。\x02",
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
        "#00005F#11Pこれは……新しい釣竿ですか？\x02",
    )

    CloseMessageWindow()

    #C0228
    ChrTalk(
        0x8,
        (
            "#6Pええ、対・釣皇倶楽部用に\x01",
            "私が組み上げたロッドなんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0229
    ChrTalk(
        0x8,
        (
            "#6Pこれがあれば、より大型の魚を\x01",
            "釣ることが可能になるはずです。\x02",
        )
    )

    CloseMessageWindow()

    #C0230
    ChrTalk(
        0x101,
        "#00002F#11Pペーターさんがこれを……\x02",
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0xA,
        (
            "#6Pはは、こう見えてペーターは\x01",
            "道具いじりが得意でなァ。\x02",
        )
    )

    CloseMessageWindow()

    #C0232
    ChrTalk(
        0xA,
        (
            "#6Pたまにこうやって、\x01",
            "既製品を改造したりして\x01",
            "新しい釣具を作ったりするんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0233
    ChrTalk(
        0x9,
        (
            "#5Pへへ、これで釣りの腕前が\x01",
            "からっきしってんだから、\x01",
            "何とも不思議な話ッスよね～。\x02",
        )
    )

    CloseMessageWindow()

    #C0234
    ChrTalk(
        0x8,
        (
            "#6Pそこ、コパン君。\x01",
            "余計な事を言わないように。\x02",
        )
    )

    CloseMessageWindow()

    #C0235
    ChrTalk(
        0x101,
        (
            "#00012F#11Pあはは……\x02\x03",

            "#00000Fでも本当に、こんな良い物を\x01",
            "ありがとうございます。\x02",
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
            "釣皇倶楽部のメンバーに、\x01",
            "《爆釣勝負》を挑めるようになりました。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #A0237
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "勝負についての詳しい内容は、\x01",
            "『東通りの釣皇倶楽部』にいる\x01",
            "受付嬢セイラームから聞く事ができます。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x1C0, 0)

    label("loc_6F91")

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

    # Function_22_641D end

    def Function_23_6FF8(): pass

    label("Function_23_6FF8")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 1)), scpexpr(EXPR_END)), "loc_7163")
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x8, 0x101, 500)

    #C0238
    ChrTalk(
        0x8,
        (
            "ロイド君、ついに\x01",
            "全てのパーツを揃えたんですね！\x02",
        )
    )

    CloseMessageWindow()

    #C0239
    ChrTalk(
        0x101,
        "#00002Fええ、何とか集めて来ました。\x02",
    )

    CloseMessageWindow()

    #C0240
    ChrTalk(
        0x8,
        (
            "ふむ、ではさっそく\x01",
            "組み上げてみましょう。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7497")

    label("loc_7163")

    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x8, 0x101, 500)

    #C0241
    ChrTalk(
        0x8,
        "ロイド君、それは……\x02",
    )

    CloseMessageWindow()

    #C0242
    ChrTalk(
        0x101,
        (
            "#00004Fええ、間違いなく釣具の\x01",
            "パーツだと思うんですけど、\x01",
            "すごく綺麗ですよね。\x02\x03",

            "#00000F四天王から取り返した釣り場で\x01",
            "珍しい魚を釣ったんですけど……\x01",
            "その魚が吐き出したんですよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0243
    ChrTalk(
        0x8,
        "……間違いありません。\x02",
    )

    CloseMessageWindow()

    #C0244
    ChrTalk(
        0x8,
        (
            "それはかつて、旅の凄腕釣師が\x01",
            "使っていた伝説の釣具のパーツです。\x02",
        )
    )

    CloseMessageWindow()

    #C0245
    ChrTalk(
        0x8,
        (
            "彼がクロスベルを去る時、\x01",
            "この地に封印されたと\x01",
            "聞いていましたが……\x02",
        )
    )

    CloseMessageWindow()

    #C0246
    ChrTalk(
        0x8,
        (
            "まさか、\x01",
            "このような形で見つかるとは！\x02",
        )
    )

    CloseMessageWindow()

    #C0247
    ChrTalk(
        0x101,
        (
            "#00005Fそ、そんなに\x01",
            "凄いものだったんですか……\x02\x03",

            "#00003Fでもどうしましょう。\x01",
            "なら、その人に返した方が……\x02",
        )
    )

    CloseMessageWindow()

    #C0248
    ChrTalk(
        0x8,
        "いえ、その必要はありません。\x02",
    )

    CloseMessageWindow()

    #C0249
    ChrTalk(
        0x8,
        (
            "……なぜなら彼は言いました。\x01",
            "その釣具は見つけた者が使えと。\x02",
        )
    )

    CloseMessageWindow()

    #C0250
    ChrTalk(
        0x8,
        (
            "そして、そのパーツは全部で４つ……\x01",
            "ってもう揃っているじゃないですか。\x02",
        )
    )

    CloseMessageWindow()

    #C0251
    ChrTalk(
        0x8,
        (
            "では、さっそく組み上げてみましょう。\x01",
            "いいですね、ロイドさん？\x02",
        )
    )

    CloseMessageWindow()

    #C0252
    ChrTalk(
        0x101,
        "#00005Fは、はい。\x02",
    )

    CloseMessageWindow()

    label("loc_7497")

    FadeToDark(1000, 0, -1)
    OP_0D()
    FadeToBright(1000, 0)
    OP_0D()

    #C0253
    ChrTalk(
        0x8,
        (
            "おお、美しい。\x01",
            "これが伝説の……\x02",
        )
    )

    CloseMessageWindow()

    #C0254
    ChrTalk(
        0x101,
        (
            "#00004F確かに……こうして組みあがると\x01",
            "物凄く綺麗でカッコイイですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0255
    ChrTalk(
        0x8,
        (
            "ふむ、ではロイド君。\x01",
            "しっかりと受け取って下さい。\x02",
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
            "を受け取った。\x02",
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
        "#00005Fお、俺が使っていいんですか？\x02",
    )

    CloseMessageWindow()

    #C0258
    ChrTalk(
        0x8,
        (
            "うふふ、何を言うんですか。\x01",
            "ロイド君が見つけたんですから当然です。\x02",
        )
    )

    CloseMessageWindow()

    #C0259
    ChrTalk(
        0x8,
        (
            "ロイド君はどうやら\x01",
            "釣傑四天王も全て倒したようですし……\x02",
        )
    )

    CloseMessageWindow()

    #C0260
    ChrTalk(
        0x8,
        (
            "そのロッドを存分に振るって\x01",
            "残るレイクロードを倒して来て下さい！\x02",
        )
    )

    CloseMessageWindow()

    #C0261
    ChrTalk(
        0x101,
        "#00000Fは、はい……分かりました！\x02",
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

    # Function_23_6FF8 end

    def Function_24_7706(): pass

    label("Function_24_7706")

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
            "ロイド団員……\x01",
            "いや、《釣皇スレイヤー》ロイド師。\x02",
        )
    )

    CloseMessageWindow()

    #C0263
    ChrTalk(
        0xA,
        (
            "今回は本当にありがとう。\x01",
            "いくら感謝しても足りないくらいだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0264
    ChrTalk(
        0x9,
        "マジすごいッスよ、ロイド師！\x02",
    )

    CloseMessageWindow()

    #C0265
    ChrTalk(
        0xD,
        (
            "ふむ、釣公師団・クロスベル支部が\x01",
            "若人の手によって守られたことは\x01",
            "誠に喜ばしく誇らしい限りなのである。\x02",
        )
    )

    CloseMessageWindow()

    #C0266
    ChrTalk(
        0x8,
        (
            "うふふ、今回の爆釣勝負は、\x01",
            "末代まで語り継がせてもらいますよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0267
    ChrTalk(
        0x101,
        "#00006Fそ、そんな、大げさですから。\x02",
    )

    CloseMessageWindow()
    OP_68(2190, 1200, -8070, 2000)
    OP_6F(0x79)

    #C0268
    ChrTalk(
        0x102,
        "#00102F（う～ん、すごい称えられようね。）\x02",
    )

    CloseMessageWindow()

    #C0269
    ChrTalk(
        0x109,
        (
            "#10103F（何だかよく分かりませんけど……\x01",
            "  まさに英雄って感じですね。）\x02",
        )
    )

    CloseMessageWindow()

    #C0270
    ChrTalk(
        0x103,
        (
            "#00200F（《釣皇スレイヤー》……\x01",
            "  少しだけカッコイイかもです。）\x02",
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

    # Function_24_7706 end

    SaveToFile()

Try(main)
