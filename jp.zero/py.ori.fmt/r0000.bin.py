from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "r0000.bin",                # FileName
        "r0000",                    # MapName
        "r0000",                    # Location
        0x005E,                     # MapIndex
        "ed7204",
        0x00000000,                 # Flags
        ("r0000", "r0000_1", "", "", "", ""),   # include
        0x04,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 5700, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 94, 0, 1, 0, 2],
    )

    BuildStringList((
        "r0000",                  # 0
        "男性",                   # 1
        "警官",                   # 2
        "バス",                   # 3
        "黒髪の女性",             # 4
        "お婆さん",               # 5
        "老人",                   # 6
        "貿易商",                 # 7
        "女性",                   # 8
        "兄",                     # 9
        "妹",                     # 10
        "父親",                   # 11
        "男の子",                 # 12
        "車00",                   # 13
        "車01",                   # 14
        "車02",                   # 15
        "車03",                   # 16
        "車04",                   # 17
        "SE制御",                 # 18
        "br0000",                 # 19
        "br0000",                 # 20
        "クロスベル市方面",       # 21
        "アルモリカ村・タングラム門方面",# 22
    ))

    ATBonus("ATBonus_5E0", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)

    Sepith("Sepith_8BCD", 5,   2,   3,   0,   0,   3,   0)
    Sepith("Sepith_8BD5", 1,   6,   0,   3,   2,   1,   1)

    MonsterBattlePostion("MonsterBattlePostion_640", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_644", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_648", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_64C", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_650", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_654", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_658", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_65C", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_6A0", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_6A4", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_6A8", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_6AC", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_6B0", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_6B4", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_6B8", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_6BC", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_620", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_624", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_628", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_62C", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_630", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_634", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_638", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_63C", 2, 13, 180)

    # monster count: 2

    BattleInfo(
        "BattleInfo_6C0", 0x0000, 8, 6, 45, 6, 1, 25, 0, "br0000", "Sepith_8BCD", 50, 50, 0, 0,
        (
            ("ms66500.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_640", "MonsterBattlePostion_6A0", "ed7400", "ed7403", "ATBonus_5E0"),
            ("ms66500.dat", "ms66500.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_620", "MonsterBattlePostion_6A0", "ed7400", "ed7403", "ATBonus_5E0"),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_730", 0x0000, 8, 6, 45, 6, 1, 25, 0, "br0000", "Sepith_8BD5", 50, 50, 0, 0,
        (
            ("ms69900.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_640", "MonsterBattlePostion_6A0", "ed7400", "ed7403", "ATBonus_5E0"),
            ("ms69900.dat", "ms69900.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_620", "MonsterBattlePostion_6A0", "ed7400", "ed7403", "ATBonus_5E0"),
            (),
            (),
        )
    )

    AddCharChip((
        "chr/ch24200.itc",                   # 00
        "chr/ch30000.itc",                   # 01
        "chr/ch00000.itc",                   # 02
        "chr/ch00000.itc",                   # 03
        "chr/ch00000.itc",                   # 04
        "chr/ch00000.itc",                   # 05
        "chr/ch00000.itc",                   # 06
        "chr/ch00000.itc",                   # 07
        "chr/ch00000.itc",                   # 08
        "chr/ch00000.itc",                   # 09
        "chr/ch00000.itc",                   # 0A
        "chr/ch00000.itc",                   # 0B
        "chr/ch00000.itc",                   # 0C
        "chr/ch00000.itc",                   # 0D
        "chr/ch00000.itc",                   # 0E
        "chr/ch00000.itc",                   # 0F
        "monster/ch66550.itc",               # 10
        "monster/ch66551.itc",               # 11
        "monster/ch69950.itc",               # 12
        "monster/ch69950.itc",               # 13
    ))

    DeclNpc(26100,   0,       -3000,   270,  405,  0x0, 0,   0,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(24799,   0,       -3000,   90,   405,  0x0, 0,   1,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclMonster(130449,  38270,   2000,    0x1010000,    "BattleInfo_6C0", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(133810,  75570,   3000,    0x1010000,    "BattleInfo_730", 0,   18,  0xFFFF, 2,  3)

    DeclActor(111510,  -2000,   78150,   1200,    111510,  -1000,   78150,   0x007C, 0,  3,  0x0000)
    DeclActor(118170,  3000,    85350,   1200,    118170,  4000,    85350,   0x007C, 0,  4,  0x0000)
    DeclActor(550,     0,       4660,    1200,    550,     1000,    4660,    0x007C, 0,  26, 0x0000)
    DeclActor(121570,  3000,    68820,   1200,    121570,  3000,    68820,   0x007C, 0,  5,  0x0000)
    DeclActor(14350,   0,       4400,    1200,    14350,   2000,    4400,    0x007C, 0,  27, 0x0000)
    DeclActor(134500,  3000,    82200,   1200,    134470,  4000,    82230,   0x007C, 0,  51, 0x0000)
    DeclActor(6200,    0,       -5000,   800,     6200,    1500,    -5000,   0x007C, 0,  13, 0x0000)
    DeclActor(2200,    0,       -5000,   800,     2200,    1500,    -5000,   0x007C, 0,  14, 0x0000)
    DeclActor(13550,   0,       -5000,   800,     13550,   1500,    -5000,   0x007C, 0,  15, 0x0000)
    DeclActor(8450,    0,       -5000,   800,     8450,    1500,    -5000,   0x007C, 0,  16, 0x0000)
    DeclActor(16950,   0,       5800,    800,     16950,   1500,    5800,    0x007C, 0,  17, 0x0000)
    DeclActor(11850,   0,       5800,    800,     11850,   1500,    5800,    0x007C, 0,  18, 0x0000)
    DeclActor(22600,   0,       -5000,   800,     22600,   1500,    -5000,   0x007C, 0,  19, 0x0000)
    DeclActor(18350,   0,       -5000,   800,     18360,   1500,    -5000,   0x007C, 0,  20, 0x0000)
    DeclActor(29400,   0,       -5000,   800,     29400,   1500,    -5000,   0x007C, 0,  21, 0x0000)
    DeclActor(24900,   0,       -5000,   800,     24900,   1500,    -5000,   0x007C, 0,  22, 0x0000)
    DeclActor(4010,    0,       6840,    1500,    4010,    1700,    6840,    0x007C, 0,  52, 0x0000)

    PlaceName(-17.0, 0.0, -7.0, 0x0000, 0x0000, "クロスベル市方面")
    PlaceName(203.0, 0.0, 27.5, 0x0000, 0x0000, "アルモリカ村・タングラム門方面")
    PlaceName(0.5899999737739563, 0.0, 4.840000152587891, 0x0000, 0x0055, "")
    PlaceName(14.899999618530273, 0.0, 6.0, 0x0000, 0x0056, "")

    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 0
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 1
    ChipFrameInfo(500, 0, [0, 1, 2, 3, 4, 5])                    # 2
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5])                   # 3

    ScpFunction((
        "Function_0_8A4",          # 00, 0
        "Function_1_95C",          # 01, 1
        "Function_2_C8F",          # 02, 2
        "Function_3_1282",         # 03, 3
        "Function_4_13CF",         # 04, 4
        "Function_5_151C",         # 05, 5
        "Function_6_1530",         # 06, 6
        "Function_7_1617",         # 07, 7
        "Function_8_1733",         # 08, 8
        "Function_9_17CB",         # 09, 9
        "Function_10_1D7D",        # 0A, 10
        "Function_11_1E6C",        # 0B, 11
        "Function_12_1EC7",        # 0C, 12
        "Function_13_1F3A",        # 0D, 13
        "Function_14_1F96",        # 0E, 14
        "Function_15_200F",        # 0F, 15
        "Function_16_206F",        # 10, 16
        "Function_17_20E8",        # 11, 17
        "Function_18_2148",        # 12, 18
        "Function_19_21C1",        # 13, 19
        "Function_20_221F",        # 14, 20
        "Function_21_2298",        # 15, 21
        "Function_22_23DA",        # 16, 22
        "Function_23_2453",        # 17, 23
        "Function_24_24C6",        # 18, 24
        "Function_25_2652",        # 19, 25
        "Function_26_288A",        # 1A, 26
        "Function_27_28FE",        # 1B, 27
        "Function_28_290C",        # 1C, 28
        "Function_29_3794",        # 1D, 29
        "Function_30_37F5",        # 1E, 30
        "Function_31_38D0",        # 1F, 31
        "Function_32_3CD2",        # 20, 32
        "Function_33_50F5",        # 21, 33
        "Function_34_5B97",        # 22, 34
        "Function_35_68EC",        # 23, 35
        "Function_36_764B",        # 24, 36
        "Function_37_83A7",        # 25, 37
        "Function_38_8416",        # 26, 38
        "Function_39_84A4",        # 27, 39
        "Function_40_853A",        # 28, 40
        "Function_41_85D0",        # 29, 41
        "Function_42_8627",        # 2A, 42
        "Function_43_867E",        # 2B, 43
        "Function_44_86D0",        # 2C, 44
        "Function_45_86EF",        # 2D, 45
        "Function_46_870E",        # 2E, 46
        "Function_47_872D",        # 2F, 47
        "Function_48_874C",        # 30, 48
        "Function_49_876B",        # 31, 49
        "Function_50_87B6",        # 32, 50
        "Function_51_87DE",        # 33, 51
        "Function_52_8B1E",        # 34, 52
    ))


    def Function_0_8A4(): pass

    label("Function_0_8A4")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_8E4"),
        (1, "loc_8F0"),
        (2, "loc_8FC"),
        (3, "loc_908"),
        (4, "loc_914"),
        (5, "loc_920"),
        (6, "loc_92C"),
        (SWITCH_DEFAULT, "loc_938"),
    )


    label("loc_8E4")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_944")

    label("loc_8F0")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_944")

    label("loc_8FC")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_944")

    label("loc_908")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_944")

    label("loc_914")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_944")

    label("loc_920")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_944")

    label("loc_92C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_944")

    label("loc_938")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_944")

    label("loc_944")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_95B")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_944")

    label("loc_95B")

    Return()

    # Function_0_8A4 end

    def Function_1_95C(): pass

    label("Function_1_95C")

    OP_D0(0x7, (scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0xF9, 4)
    SetScenarioFlags(0xFB, 4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_97A")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 31)

    label("loc_97A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_990")
    SetMapFlags(0x10000000)
    Event(0, 28)

    label("loc_990")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7E, 0)), scpexpr(EXPR_END)), "loc_99F")
    ClearScenarioFlags(0x7E, 0)
    Event(0, 8)

    label("loc_99F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7E, 1)), scpexpr(EXPR_END)), "loc_9B7")
    ClearScenarioFlags(0x7E, 1)
    OP_D0(0x1, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 10)

    label("loc_9B7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_C3E")
    ClearScenarioFlags(0x7A, 0)
    ClearScenarioFlags(0x7A, 1)
    ClearScenarioFlags(0x7A, 2)
    ClearScenarioFlags(0x7A, 3)
    ClearScenarioFlags(0x7A, 4)
    ClearScenarioFlags(0x7A, 5)
    ClearScenarioFlags(0x7A, 6)
    ClearScenarioFlags(0x7A, 7)
    ClearScenarioFlags(0x7B, 0)
    ClearScenarioFlags(0x7B, 1)
    ClearScenarioFlags(0x7B, 2)
    ClearScenarioFlags(0x7B, 3)
    ClearScenarioFlags(0x7B, 4)
    ClearScenarioFlags(0x7B, 5)
    ClearScenarioFlags(0x7B, 6)
    ClearScenarioFlags(0x7B, 7)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A1D")
    SetScenarioFlags(0x7A, 0)

    label("loc_A1D")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A33")
    SetScenarioFlags(0x7A, 1)

    label("loc_A33")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A49")
    SetScenarioFlags(0x7A, 2)

    label("loc_A49")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A5F")
    SetScenarioFlags(0x7A, 3)

    label("loc_A5F")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A75")
    SetScenarioFlags(0x7A, 4)

    label("loc_A75")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A8B")
    SetScenarioFlags(0x7A, 5)

    label("loc_A8B")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AA1")
    SetScenarioFlags(0x7A, 6)

    label("loc_AA1")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AB7")
    SetScenarioFlags(0x7A, 7)

    label("loc_AB7")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_ACD")
    SetScenarioFlags(0x7B, 0)

    label("loc_ACD")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AE3")
    SetScenarioFlags(0x7B, 1)

    label("loc_AE3")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AF9")
    SetScenarioFlags(0x7B, 2)

    label("loc_AF9")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B0F")
    SetScenarioFlags(0x7B, 3)

    label("loc_B0F")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B25")
    SetScenarioFlags(0x7B, 4)

    label("loc_B25")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B3B")
    SetScenarioFlags(0x7B, 5)

    label("loc_B3B")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B51")
    SetScenarioFlags(0x7B, 6)

    label("loc_B51")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B67")
    SetScenarioFlags(0x7B, 7)

    label("loc_B67")

    ClearScenarioFlags(0x7C, 0)
    ClearScenarioFlags(0x7C, 1)
    ClearScenarioFlags(0x7C, 2)
    ClearScenarioFlags(0x7C, 3)
    ClearScenarioFlags(0x7C, 4)
    ClearScenarioFlags(0x7C, 5)
    ClearScenarioFlags(0x7C, 6)
    ClearScenarioFlags(0x7C, 7)
    RunExpression(0x4, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BA2")
    SetScenarioFlags(0x7C, 0)
    Jump("loc_C3E")

    label("loc_BA2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BB9")
    SetScenarioFlags(0x7C, 1)
    Jump("loc_C3E")

    label("loc_BB9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BD0")
    SetScenarioFlags(0x7C, 2)
    Jump("loc_C3E")

    label("loc_BD0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BE7")
    SetScenarioFlags(0x7C, 3)
    Jump("loc_C3E")

    label("loc_BE7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BFE")
    SetScenarioFlags(0x7C, 4)
    Jump("loc_C3E")

    label("loc_BFE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C15")
    SetScenarioFlags(0x7C, 5)
    Jump("loc_C3E")

    label("loc_C15")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C2C")
    SetScenarioFlags(0x7C, 6)
    Jump("loc_C3E")

    label("loc_C2C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C3E")
    SetScenarioFlags(0x7C, 7)

    label("loc_C3E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_C4C")
    Jump("loc_C78")

    label("loc_C4C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_C78")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x17, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_C78")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x17, 0x1, 0x14)"), scpexpr(EXPR_END)), "loc_C78")
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)

    label("loc_C78")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x93, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C8E")
    Event(0, 30)

    label("loc_C8E")

    Return()

    # Function_1_95C end

    def Function_2_C8F(): pass

    label("Function_2_C8F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CA2")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_CA2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CBB")
    OP_10(0x0, 0x0)
    OP_10(0x2, 0x1)
    Jump("loc_CC1")

    label("loc_CBB")

    OP_10(0x0, 0x1)
    OP_10(0x2, 0x0)

    label("loc_CC1")

    SetChrFlags(0xA, 0x80)
    SetMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x5, 0x4)
    OP_65(0x4, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_23, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D09")
    SetMapObjFrame(0x5, "light", 0x0, 0x1)
    ClearMapObjFlags(0x5, 0x4)
    OP_66(0x4, 0x1)
    Jump("loc_D0E")

    label("loc_D09")

    OP_16(0x3, 0x3, 0x1, 0x0)

    label("loc_D0E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x100, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D21")
    OP_70(0x2, 0x0)
    Jump("loc_D25")

    label("loc_D21")

    OP_70(0x2, 0x1E)

    label("loc_D25")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x100, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D38")
    OP_70(0x3, 0x0)
    Jump("loc_D3C")

    label("loc_D38")

    OP_70(0x3, 0x1E)

    label("loc_D3C")

    OP_65(0x3, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7A, 0)), scpexpr(EXPR_END)), "loc_D99")
    LoadEffect(0x9, "event\\eva00_00.eff")
    PlayEffect(0x9, 0x9, 0xFF, 0x0, 121570, 3000, 68820, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_66(0x3, 0x1)

    label("loc_D99")

    OP_65(0x5, 0x1)
    SetMapObjFlags(0xB, 0x4)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2E, 0x1, 0x1)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2E, 0x1, 0x5)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_DBD")
    OP_66(0x5, 0x1)

    label("loc_DBD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_DCC")
    ClearMapObjFlags(0xB, 0x4)

    label("loc_DCC")

    OP_78(0x6, 0x14)
    OP_78(0x7, 0x15)
    OP_78(0x8, 0x16)
    OP_78(0x9, 0x17)
    OP_78(0xA, 0x18)
    SetMapObjFlags(0x6, 0x4)
    SetMapObjFlags(0x7, 0x4)
    SetMapObjFlags(0x8, 0x4)
    SetMapObjFlags(0x9, 0x4)
    SetMapObjFlags(0xA, 0x4)
    SetMapObjFrame(0x6, "light", 0x0, 0x1)
    SetMapObjFrame(0x7, "light", 0x0, 0x1)
    SetMapObjFrame(0x8, "light", 0x0, 0x1)
    SetMapObjFrame(0x9, "light", 0x0, 0x1)
    SetMapObjFrame(0xA, "light", 0x0, 0x1)
    SetMapObjFrame(0x6, "chukin", 0x0, 0x1)
    SetMapObjFrame(0x7, "chukin", 0x0, 0x1)
    SetMapObjFrame(0x8, "chukin", 0x0, 0x1)
    SetMapObjFrame(0x9, "chukin", 0x0, 0x1)
    SetMapObjFrame(0xA, "chukin", 0x0, 0x1)
    OP_65(0x6, 0x1)
    OP_65(0x7, 0x1)
    OP_65(0x8, 0x1)
    OP_65(0x9, 0x1)
    OP_65(0xA, 0x1)
    OP_65(0xB, 0x1)
    OP_65(0xC, 0x1)
    OP_65(0xD, 0x1)
    OP_65(0xE, 0x1)
    OP_65(0xF, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_EBB")
    Jump("loc_1281")

    label("loc_EBB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_FE8")
    ClearMapObjFlags(0x6, 0x4)
    ClearMapObjFlags(0x7, 0x4)
    ClearMapObjFlags(0x8, 0x4)
    SetChrPos(0x14, 4270, 0, -5000, 270)
    OP_D3(0x14, 0x0, 0x41EB0, 0x0, 0x0)
    SetChrPos(0x15, 10750, 0, -5000, 270)
    OP_D3(0x15, 0x0, 0x41EB0, 0x0, 0x0)
    SetChrPos(0x16, 14000, 0, 5750, 270)
    OP_D3(0x16, 0x0, 0x41EB0, 0x0, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x17, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_F8F")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x17, 0x1, 0x14)"), scpexpr(EXPR_END)), "loc_F60")
    Jump("loc_F8A")

    label("loc_F60")

    ClearMapObjFlags(0xA, 0x4)
    SetChrPos(0x18, 27500, 0, -5000, 270)
    OP_D3(0x18, 0x0, 0x41EB0, 0x0, 0x0)

    label("loc_F8A")

    Jump("loc_FE3")

    label("loc_F8F")

    ClearMapObjFlags(0x9, 0x4)
    ClearMapObjFlags(0xA, 0x4)
    SetChrPos(0x17, 20500, 0, -5000, 270)
    OP_D3(0x17, 0x0, 0x41EB0, 0x0, 0x0)
    SetChrPos(0x18, 27500, 0, -5000, 270)
    OP_D3(0x18, 0x0, 0x41EB0, 0x0, 0x0)

    label("loc_FE3")

    Jump("loc_1281")

    label("loc_FE8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_10D9")
    ClearMapObjFlags(0x6, 0x4)
    ClearMapObjFlags(0x7, 0x4)
    ClearMapObjFlags(0x8, 0x4)
    ClearMapObjFlags(0xA, 0x4)
    SetChrPos(0x14, 4270, 0, -5000, 270)
    OP_D3(0x14, 0x0, 0x41EB0, 0x0, 0x0)
    SetChrPos(0x15, 10750, 0, -5000, 270)
    OP_D3(0x15, 0x0, 0x41EB0, 0x0, 0x0)
    SetChrPos(0x16, 14000, 0, 5750, 270)
    OP_D3(0x16, 0x0, 0x41EB0, 0x0, 0x0)
    SetChrPos(0x18, 27500, 0, -5000, 270)
    OP_D3(0x18, 0x0, 0x41EB0, 0x0, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x17, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_10AA")
    Jump("loc_10D4")

    label("loc_10AA")

    ClearMapObjFlags(0x9, 0x4)
    SetChrPos(0x17, 20500, 0, -5000, 270)
    OP_D3(0x17, 0x0, 0x41EB0, 0x0, 0x0)

    label("loc_10D4")

    Jump("loc_1281")

    label("loc_10D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1281")
    ClearMapObjFlags(0x6, 0x4)
    ClearMapObjFlags(0x7, 0x4)
    ClearMapObjFlags(0x8, 0x4)
    ClearMapObjFlags(0x9, 0x4)
    ClearMapObjFlags(0xA, 0x4)
    SetChrPos(0x14, 4270, 0, -5000, 270)
    OP_D3(0x14, 0x0, 0x41EB0, 0x0, 0x0)
    SetChrPos(0x15, 10750, 0, -5000, 270)
    OP_D3(0x15, 0x0, 0x41EB0, 0x0, 0x0)
    SetChrPos(0x16, 14000, 0, 5750, 270)
    OP_D3(0x16, 0x0, 0x41EB0, 0x0, 0x0)
    SetChrPos(0x17, 20500, 0, -5000, 270)
    OP_D3(0x17, 0x0, 0x41EB0, 0x0, 0x0)
    SetChrPos(0x18, 27500, 0, -5000, 270)
    OP_D3(0x18, 0x0, 0x41EB0, 0x0, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x17, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_11C5")
    Jump("loc_1281")

    label("loc_11C5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x17, 0x1, 0x0)"), scpexpr(EXPR_END)), "loc_1281")
    OP_66(0x6, 0x1)
    OP_66(0x7, 0x1)
    OP_66(0x8, 0x1)
    OP_66(0x9, 0x1)
    OP_66(0xA, 0x1)
    OP_66(0xB, 0x1)
    OP_66(0xC, 0x1)
    OP_66(0xD, 0x1)
    OP_66(0xE, 0x1)
    OP_66(0xF, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x17, 0x1, 0xA)"), scpexpr(EXPR_END)), "loc_1215")
    SetMapObjFrame(0x6, "chukin", 0x1, 0x1)

    label("loc_1215")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x17, 0x1, 0xC)"), scpexpr(EXPR_END)), "loc_1230")
    SetMapObjFrame(0x7, "chukin", 0x1, 0x1)

    label("loc_1230")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x17, 0x1, 0xE)"), scpexpr(EXPR_END)), "loc_124B")
    SetMapObjFrame(0x8, "chukin", 0x1, 0x1)

    label("loc_124B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x17, 0x1, 0x10)"), scpexpr(EXPR_END)), "loc_1266")
    SetMapObjFrame(0x9, "chukin", 0x1, 0x1)

    label("loc_1266")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x17, 0x1, 0x12)"), scpexpr(EXPR_END)), "loc_1281")
    SetMapObjFrame(0xA, "chukin", 0x1, 0x1)

    label("loc_1281")

    Return()

    # Function_2_C8F end

    def Function_3_1282(): pass

    label("Function_3_1282")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x100, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_137E")
    Sound(14, 0, 100, 0)
    OP_71(0x2, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1F5, 1)"), scpexpr(EXPR_END)), "loc_1307")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0001
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1F5),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x100, 0)
    OP_DE(0x6, 0x0)
    Jump("loc_1379")

    label("loc_1307")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0002
    AnonymousTalk(
        0x3E7,
        (
            "宝箱には",
            scpstr(SCPSTR_CODE_ITEM, 0x1F5),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "が入っている。\x01",
            "持ち物が一杯なので、",
            scpstr(SCPSTR_CODE_ITEM, 0x1F5),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "をあきらめた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x2, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1379")

    Jump("loc_13C3")

    label("loc_137E")

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

    label("loc_13C3")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_1282 end

    def Function_4_13CF(): pass

    label("Function_4_13CF")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x100, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14CB")
    Sound(14, 0, 100, 0)
    OP_71(0x3, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x5DF, 1)"), scpexpr(EXPR_END)), "loc_1454")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0004
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x5DF),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x100, 1)
    OP_DE(0x6, 0x0)
    Jump("loc_14C6")

    label("loc_1454")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0005
    AnonymousTalk(
        0x3E7,
        (
            "宝箱には",
            scpstr(SCPSTR_CODE_ITEM, 0x5DF),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "が入っている。\x01",
            "持ち物が一杯なので、",
            scpstr(SCPSTR_CODE_ITEM, 0x5DF),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "をあきらめた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x3, 0x1E, 0x0, 0x0, 0x0)

    label("loc_14C6")

    Jump("loc_1510")

    label("loc_14CB")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0006
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

    label("loc_1510")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_13CF end

    def Function_5_151C(): pass

    label("Function_5_151C")

    TalkBegin(0xFF)
    Call(1, 0)
    ClearScenarioFlags(0x7A, 0)
    OP_65(0x3, 0x1)
    StopEffect(0x9, 0x2)
    TalkEnd(0xFF)
    Return()

    # Function_5_151C end

    def Function_6_1530(): pass

    label("Function_6_1530")

    EventBegin(0x1)
    SetMapFlags(0x8000000)

    #A0007
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "バス停がある。\x01",
            "バスで移動しますか？\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "アルモリカ村\x01",          # 0
            "タングラム門\x01",          # 1
            "停留所（三叉路）\x01",      # 2
            "やめる\x01",                # 3
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15CA")
    Call(0, 7)
    ClearMapFlags(0x8000000)
    NewScene("t0000", 0, 0, 0)
    IdleLoop()
    Jump("loc_160F")

    label("loc_15CA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15EF")
    Call(0, 7)
    ClearMapFlags(0x8000000)
    NewScene("t2500", 0, 0, 0)
    IdleLoop()
    Jump("loc_160F")

    label("loc_15EF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_160F")
    Call(0, 7)
    ClearMapFlags(0x8000000)
    NewScene("r0030", 0, 0, 0)
    IdleLoop()

    label("loc_160F")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_6_1530 end

    def Function_7_1617(): pass

    label("Function_7_1617")

    Fade(1000)
    OP_68(-620, 600, 4110, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(27000, 0)
    OP_E0(0x1)
    SetChrPos(0x0, -1000, 0, 4500, 180)
    SetChrPos(0x1, -1000, 0, 5600, 180)
    SetChrPos(0x2, -1000, 0, 6700, 180)
    SetChrPos(0x3, -1000, 0, 7800, 180)
    ClearChrFlags(0xA, 0x80)
    ClearMapObjFlags(0x0, 0x4)
    OP_78(0x0, 0xA)
    SetMapObjFrame(0x0, "light", 0x0, 0x1)
    OP_49()
    SetChrPos(0xA, 16000, 0, 0, 0)
    OP_D3(0xA, 0x0, 0x41EB0, 0x0, 0x0)
    SetMapObjFlags(0x0, 0x1000)
    OP_74(0x0, 0x1E)
    OP_0D()
    OP_71(0x0, 0x79, 0xB4, 0x0, 0x20)

    def lambda_16ED():
        OP_98(0xFE, 0xFFFFC180, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_16ED)
    Sound(466, 0, 100, 0)
    Sound(467, 0, 100, 0)
    WaitChrThread(0xA, 1)
    OP_71(0x0, 0x5B, 0x78, 0x0, 0x0)
    OP_79(0x0)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x7E, 0)
    Return()

    # Function_7_1617 end

    def Function_8_1733(): pass

    label("Function_8_1733")

    EventBegin(0x1)
    FadeToDark(0, 0, -1)
    OP_6F(0x1)
    Sleep(1)
    SetChrPos(0x0, -1000, 0, 4500, 180)
    SetChrPos(0x1, -1000, 0, 4500, 180)
    SetChrPos(0x2, -1000, 0, 4500, 180)
    SetChrPos(0x3, -1000, 0, 4500, 180)
    Sleep(1)
    OP_68(-1000, 600, 4500, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(25000, 0)
    OP_6F(0x1)
    Sleep(1)
    FadeToBright(500, 0)
    OP_0D()
    EventEnd(0x5)
    Return()

    # Function_8_1733 end

    def Function_9_17CB(): pass

    label("Function_9_17CB")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    Sound(1499, 255, 100, 0)    #voice#Noel
    Sleep(500)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_17E5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1D75")

    Menu(
        0,
        32,
        26,
        1,
        (
            "警備隊車両で移動をする\x01",      # 0
            "ここで休憩をする\x01",            # 1
            "やめる\x01",                      # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1D12")
    Sound(1500, 255, 100, 0)    #voice#Noel
    MenuCmd(0, 1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_187B")
    MenuCmd(1, 1, "★クロスベル市・中央広場")
    MenuCmd(3, 1, 0x0)
    Jump("loc_1897")

    label("loc_187B")

    MenuCmd(1, 1, "　クロスベル市・中央広場")

    label("loc_1897")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_18C9")
    MenuCmd(1, 1, "★クロスベル市・東出口")
    MenuCmd(3, 1, 0x1)
    Jump("loc_18E3")

    label("loc_18C9")

    MenuCmd(1, 1, "　クロスベル市・東出口")

    label("loc_18E3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1915")
    MenuCmd(1, 1, "★クロスベル市・西出口")
    MenuCmd(3, 1, 0x2)
    Jump("loc_192F")

    label("loc_1915")

    MenuCmd(1, 1, "　クロスベル市・西出口")

    label("loc_192F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1961")
    MenuCmd(1, 1, "★クロスベル市・南出口")
    MenuCmd(3, 1, 0x3)
    Jump("loc_197B")

    label("loc_1961")

    MenuCmd(1, 1, "　クロスベル市・南出口")

    label("loc_197B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_19AD")
    MenuCmd(1, 1, "★クロスベル市・北出口")
    MenuCmd(3, 1, 0x4)
    Jump("loc_19C7")

    label("loc_19AD")

    MenuCmd(1, 1, "　クロスベル市・北出口")

    label("loc_19C7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_19F1")
    MenuCmd(1, 1, "★タングラム門")
    MenuCmd(3, 1, 0x5)
    Jump("loc_1A03")

    label("loc_19F1")

    MenuCmd(1, 1, "　タングラム門")

    label("loc_1A03")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A2D")
    MenuCmd(1, 1, "★ベルガード門")
    MenuCmd(3, 1, 0x6)
    Jump("loc_1A3F")

    label("loc_1A2D")

    MenuCmd(1, 1, "　ベルガード門")

    label("loc_1A3F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A6D")
    MenuCmd(1, 1, "★ウルスラ医科大学")
    MenuCmd(3, 1, 0x7)
    Jump("loc_1A83")

    label("loc_1A6D")

    MenuCmd(1, 1, "　ウルスラ医科大学")

    label("loc_1A83")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1AAD")
    MenuCmd(1, 1, "★アルモリカ村")
    MenuCmd(3, 1, 0x8)
    Jump("loc_1ABF")

    label("loc_1AAD")

    MenuCmd(1, 1, "　アルモリカ村")

    label("loc_1ABF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1AEB")
    MenuCmd(1, 1, "★マインツ鉱山町")
    MenuCmd(3, 1, 0x9)
    Jump("loc_1AFF")

    label("loc_1AEB")

    MenuCmd(1, 1, "　マインツ鉱山町")

    label("loc_1AFF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B31")
    MenuCmd(1, 1, "★マインツ山道・隧道内")
    MenuCmd(3, 1, 0xA)
    Jump("loc_1B4B")

    label("loc_1B31")

    MenuCmd(1, 1, "　マインツ山道・隧道内")

    label("loc_1B4B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B71")
    MenuCmd(1, 1, "★星見の塔")
    MenuCmd(3, 1, 0xB)
    Jump("loc_1B7F")

    label("loc_1B71")

    MenuCmd(1, 1, "　星見の塔")

    label("loc_1B7F")

    MenuCmd(1, 1, "　やめる")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuCmd(2, 1, 240, 16, 1)
    MenuEnd(0x0)
    OP_60(0x1)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1D03")
    OP_60(0x0)
    Sleep(500)
    Sound(1501, 255, 100, 0)    #voice#Noel
    OP_74(0x5, 0x1E)
    OP_71(0x5, 0xF1, 0x10E, 0x0, 0x0)
    Sound(464, 0, 100, 0)
    OP_79(0x5)
    Sleep(500)
    FadeToDark(1000, 0, -1)
    Sleep(500)
    OP_0D()
    Sound(488, 0, 100, 0)
    Sleep(2500)
    SetScenarioFlags(0x7E, 1)
    SetScenarioFlags(0x7F, 6)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1C56"),
        (1, "loc_1C64"),
        (2, "loc_1C72"),
        (3, "loc_1C80"),
        (4, "loc_1C8E"),
        (5, "loc_1C9C"),
        (6, "loc_1CAA"),
        (7, "loc_1CB8"),
        (8, "loc_1CC6"),
        (9, "loc_1CD4"),
        (10, "loc_1CE2"),
        (11, "loc_1CF0"),
        (SWITCH_DEFAULT, "loc_1CFE"),
    )


    label("loc_1C56")

    NewScene("c0100", 0, 0, 0)
    IdleLoop()
    Jump("loc_1CFE")

    label("loc_1C64")

    NewScene("r0000", 0, 0, 0)
    IdleLoop()
    Jump("loc_1CFE")

    label("loc_1C72")

    NewScene("r1000", 0, 0, 0)
    IdleLoop()
    Jump("loc_1CFE")

    label("loc_1C80")

    NewScene("r1500", 0, 0, 0)
    IdleLoop()
    Jump("loc_1CFE")

    label("loc_1C8E")

    NewScene("r2000", 0, 0, 0)
    IdleLoop()
    Jump("loc_1CFE")

    label("loc_1C9C")

    NewScene("t2500", 0, 0, 0)
    IdleLoop()
    Jump("loc_1CFE")

    label("loc_1CAA")

    NewScene("t2000", 0, 0, 0)
    IdleLoop()
    Jump("loc_1CFE")

    label("loc_1CB8")

    NewScene("t1500", 0, 0, 0)
    IdleLoop()
    Jump("loc_1CFE")

    label("loc_1CC6")

    NewScene("t0000", 0, 0, 0)
    IdleLoop()
    Jump("loc_1CFE")

    label("loc_1CD4")

    NewScene("t0500", 0, 0, 0)
    IdleLoop()
    Jump("loc_1CFE")

    label("loc_1CE2")

    NewScene("r2050", 0, 0, 0)
    IdleLoop()
    Jump("loc_1CFE")

    label("loc_1CF0")

    NewScene("m1000", 0, 0, 0)
    IdleLoop()
    Jump("loc_1CFE")

    label("loc_1CFE")

    Jump("loc_1D0D")

    label("loc_1D03")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1D0D")

    Jump("loc_1D70")

    label("loc_1D12")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1D5D")
    OP_60(0x0)
    OP_57(0x0)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_5A()
    Sound(13, 0, 100, 0)
    OP_32(0xFF, 0xFE, 0x0)
    OP_6A(0x0, 0x0)
    Sleep(3500)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    Jump("loc_1D70")

    label("loc_1D5D")

    OP_60(0x0)
    OP_57(0x0)
    Sleep(500)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1D70")

    Jump("loc_17E5")

    label("loc_1D75")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_9_17CB end

    def Function_10_1D7D(): pass

    label("Function_10_1D7D")

    EventBegin(0x1)
    FadeToDark(0, 0, -1)
    OP_6F(0x1)
    Sleep(1)
    SetChrPos(0x0, 14360, 0, 2630, 180)
    SetChrPos(0x1, 14360, 0, 2630, 180)
    SetChrPos(0x2, 14360, 0, 2630, 180)
    SetChrPos(0x3, 14360, 0, 2630, 180)
    SetChrPos(0x4, 14360, 0, 2630, 180)
    SetChrPos(0x5, 14360, 0, 2630, 180)
    Sleep(1)
    OP_68(14360, 600, 2630, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(25000, 0)
    OP_6F(0x1)
    Sleep(1)
    Sound(489, 0, 100, 0)
    Sleep(2000)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1E51")
    Sound(1502, 255, 100, 0)    #voice#Noel
    Jump("loc_1E57")

    label("loc_1E51")

    Sound(1503, 255, 100, 0)    #voice#Noel

    label("loc_1E57")

    Sleep(500)
    FadeToBright(500, 0)
    OP_0D()
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_10_1D7D end

    def Function_11_1E6C(): pass

    label("Function_11_1E6C")

    TalkBegin(0xFE)

    #C0008
    ChrTalk(
        0x8,
        (
            "くそー、やはり\x01",
            "バレてしまったか……\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x8,
        (
            "記念祭なら大丈夫かと\x01",
            "思ったのに……！\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_11_1E6C end

    def Function_12_1EC7(): pass

    label("Function_12_1EC7")

    TalkBegin(0xFE)

    #C0010
    ChrTalk(
        0x9,
        (
            "ええと、１申請で\x01",
            "２台駐車なさってた方ですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x9,
        (
            "はい、こちらにサインと……\x01",
            "あとは罰金の方ですねー。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_12_1EC7 end

    def Function_13_1F3A(): pass

    label("Function_13_1F3A")

    TalkBegin(0xFF)
    SetChrName("")

    #A0012
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ヴェルヌ社製の高級車のようだ。\x02\x03",

            "車両ナンバーは『ＶＥ　４３１０』。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0xBE, 1)
    Call(0, 24)
    TalkEnd(0xFF)
    Return()

    # Function_13_1F3A end

    def Function_14_1F96(): pass

    label("Function_14_1F96")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x17, 0x1, 0xA)"), scpexpr(EXPR_END)), "loc_1FE1")
    SetChrName("")

    #A0013
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "違法駐車の警告ステッカーが\x01",
            "貼られている。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_200B")

    label("loc_1FE1")

    Call(0, 23)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_200B")
    Sleep(300)
    Sound(959, 0, 100, 0)
    SetMapObjFrame(0x6, "chukin", 0x1, 0x1)
    OP_29(0x17, 0x1, 0xA)

    label("loc_200B")

    TalkEnd(0xFF)
    Return()

    # Function_14_1F96 end

    def Function_15_200F(): pass

    label("Function_15_200F")

    TalkBegin(0xFF)
    SetChrName("")

    #A0014
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ヴェルヌ社製の導力運搬車のようだ。\x02\x03",

            "車両ナンバーは『ＥＳ　４５２１』。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0xBE, 2)
    Call(0, 24)
    TalkEnd(0xFF)
    Return()

    # Function_15_200F end

    def Function_16_206F(): pass

    label("Function_16_206F")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x17, 0x1, 0xC)"), scpexpr(EXPR_END)), "loc_20BA")
    SetChrName("")

    #A0015
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "違法駐車の警告ステッカーが\x01",
            "貼られている。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_20E4")

    label("loc_20BA")

    Call(0, 23)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_20E4")
    Sleep(300)
    Sound(959, 0, 100, 0)
    SetMapObjFrame(0x7, "chukin", 0x1, 0x1)
    OP_29(0x17, 0x1, 0xC)

    label("loc_20E4")

    TalkEnd(0xFF)
    Return()

    # Function_16_206F end

    def Function_17_20E8(): pass

    label("Function_17_20E8")

    TalkBegin(0xFF)
    SetChrName("")

    #A0016
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ヴェルヌ社製の導力運搬車のようだ。\x02\x03",

            "車両ナンバーは『ＬＡ　５８２８』。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0xBE, 3)
    Call(0, 24)
    TalkEnd(0xFF)
    Return()

    # Function_17_20E8 end

    def Function_18_2148(): pass

    label("Function_18_2148")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x17, 0x1, 0xE)"), scpexpr(EXPR_END)), "loc_2193")
    SetChrName("")

    #A0017
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "違法駐車の警告ステッカーが\x01",
            "貼られている。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_21BD")

    label("loc_2193")

    Call(0, 23)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_21BD")
    Sleep(300)
    Sound(959, 0, 100, 0)
    SetMapObjFrame(0x8, "chukin", 0x1, 0x1)
    OP_29(0x17, 0x1, 0xE)

    label("loc_21BD")

    TalkEnd(0xFF)
    Return()

    # Function_18_2148 end

    def Function_19_21C1(): pass

    label("Function_19_21C1")

    TalkBegin(0xFF)
    SetChrName("")

    #A0018
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ヴェルヌ社製の自家用車のようだ。\x02\x03",

            "車両ナンバーは『ＣＷ　６４２２』。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0xBE, 4)
    Call(0, 24)
    TalkEnd(0xFF)
    Return()

    # Function_19_21C1 end

    def Function_20_221F(): pass

    label("Function_20_221F")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x17, 0x1, 0x10)"), scpexpr(EXPR_END)), "loc_226A")
    SetChrName("")

    #A0019
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "違法駐車の警告ステッカーが\x01",
            "貼られている。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_2294")

    label("loc_226A")

    Call(0, 23)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2294")
    Sleep(300)
    Sound(959, 0, 100, 0)
    SetMapObjFrame(0x9, "chukin", 0x1, 0x1)
    OP_29(0x17, 0x1, 0x10)

    label("loc_2294")

    TalkEnd(0xFF)
    Return()

    # Function_20_221F end

    def Function_21_2298(): pass

    label("Function_21_2298")

    TalkBegin(0xFF)
    SetChrName("")

    #A0020
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ラインフォルト社製の高級車のようだ。\x02\x03",

            "車両ナンバーは『ＣＬ　１１０１』。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x17, 0x1, 0x14)"), scpexpr(EXPR_END)), "loc_233B")

    #C0021
    ChrTalk(
        0x101,
        (
            "#0001F（確か西口にも\x01",
            "  あったはずのナンバーだ……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_23D0")

    label("loc_233B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x17, 0x1, 0x13)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBC, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2354")
    Call(0, 25)
    Jump("loc_23D0")

    label("loc_2354")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x17, 0x1, 0x13)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBC, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_23C3")

    #C0022
    ChrTalk(
        0x101,
        (
            "#0005F（あれ…………？）\x02\x03",

            "#0003F（このナンバー、どこかで見た事が\x01",
            "  あるような……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_23D0")

    label("loc_23C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBC, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_23D0")
    SetScenarioFlags(0xBC, 5)

    label("loc_23D0")

    SetScenarioFlags(0xBE, 5)
    Call(0, 24)
    TalkEnd(0xFF)
    Return()

    # Function_21_2298 end

    def Function_22_23DA(): pass

    label("Function_22_23DA")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x17, 0x1, 0x12)"), scpexpr(EXPR_END)), "loc_2425")
    SetChrName("")

    #A0023
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "違法駐車の警告ステッカーが\x01",
            "貼られている。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_244F")

    label("loc_2425")

    Call(0, 23)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_244F")
    Sleep(300)
    Sound(959, 0, 100, 0)
    SetMapObjFrame(0xA, "chukin", 0x1, 0x1)
    OP_29(0x17, 0x1, 0x12)

    label("loc_244F")

    TalkEnd(0xFF)
    Return()

    # Function_22_23DA end

    def Function_23_2453(): pass

    label("Function_23_2453")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 16, -1, -1)
    SetChrName("")

    #A0024
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "警告ステッカーを貼りますか？",
            scpstr(0x18),
            scpstr(SCPSTR_CODE_ENTER),
        )
    )


    Menu(
        0,
        -1,
        150,
        1,
        (
            "【貼る】\x01",          # 0
            "【貼らない】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    Return()

    # Function_23_2453 end

    def Function_24_24C6(): pass

    label("Function_24_24C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBD, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBD, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBD, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBE, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBE, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBE, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBE, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBE, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBE, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x17, 0x1, 0x13)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2651")

    #C0025
    ChrTalk(
        0x101,
        (
            "#0000Fよし……これで\x01",
            "全車両のナンバーを\x01",
            "チェックしたかな。\x02\x03",

            "残りのステッカーを貼ってから\x01",
            "報告に戻ろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x104,
        "#0300Fうっし、そうするかね。\x02",
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x102,
        (
            "#0100F別に急ぎではないみたいだし、\x01",
            "もう一度確認しつつ戻るのも\x01",
            "いいかもしれないわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x103,
        (
            "#0200F間違って貼っていても\x01",
            "はがす事は出来ませんが……\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x101,
        (
            "#0000Fハハ……\x01",
            "まあ大丈夫だとは思うけど。\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x17, 0x1, 0x13)

    label("loc_2651")

    Return()

    # Function_24_24C6 end

    def Function_25_2652(): pass

    label("Function_25_2652")

    EventBegin(0x0)
    Fade(500)
    OP_E0(0x1)
    OP_68(31390, 600, -2940, 0)
    MoveCamera(42, 24, 0, 0)
    OP_6E(490, 0)
    SetCameraDistance(19340, 0)
    SetChrPos(0x101, 31050, 0, -4940, 270)
    SetChrPos(0x102, 32700, 0, -4120, 270)
    SetChrPos(0x103, 31500, 0, -3440, 225)
    SetChrPos(0x104, 31000, 0, -2310, 225)
    OP_0D()

    #C0030
    ChrTalk(
        0x101,
        (
            "#12P#0005F……………………？\x02\x03",

            "#0001Fこのナンバー……\x01",
            "西口にもなかったか？\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x102,
        (
            "#11P#0105Fそういえば……\x01",
            "あったかも知れないわ。\x02\x03",

            "#0100F自家用車じゃ\x01",
            "なかった気がするけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x103,
        (
            "#5P#0200F同じナンバーの車両なんて\x01",
            "本来あるはずはありませんが……\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x104,
        (
            "#5P#0303Fふむ……認可は\x01",
            "受けているナンバーだな。\x02\x03",

            "#0300Fま、一応覚えといた方が\x01",
            "いいんじゃねえか？\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x101,
        (
            "#12P#0000Fそうだな……\x01",
            "後で広域防犯課の方にも\x01",
            "報告しておこう。\x02",
        )
    )

    CloseMessageWindow()
    OP_E0(0x0)
    SetChrPos(0x0, 31050, 0, -4940, 270)
    OP_29(0x17, 0x1, 0x14)
    EventEnd(0x5)
    Return()

    # Function_25_2652 end

    def Function_26_288A(): pass

    label("Function_26_288A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_289B")
    Call(0, 6)
    Jump("loc_28FD")

    label("loc_289B")

    TalkBegin(0xFF)
    SetChrName("")

    #A0035
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "バスの停留所がある。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0036
    ChrTalk(
        0x101,
        (
            "#0006F……アルモリカ村まで\x01",
            "頑張って歩く事にしよう。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFF)

    label("loc_28FD")

    Return()

    # Function_26_288A end

    def Function_27_28FE(): pass

    label("Function_27_28FE")

    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 9)
    Return()

    # Function_27_28FE end

    def Function_28_290C(): pass

    label("Function_28_290C")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-5000, 1000, 0, 0)
    MoveCamera(36, 18, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(25000, 0)
    SetChrPos(0x101, -7100, 0, -700, 90)
    SetChrPos(0x102, -8500, 0, -700, 90)
    SetChrPos(0x103, -8500, 0, 700, 90)
    SetChrPos(0x104, -7100, 0, 700, 90)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    ClearMapObjFlags(0x0, 0x4)
    OP_78(0x0, 0xA)
    SetMapObjFrame(0x0, "light", 0x0, 0x1)
    OP_49()
    SetChrPos(0xA, 16000, 0, 6000, 0)
    OP_D3(0xA, 0x0, 0x41EB0, 0x0, 0x0)
    SetMapObjFlags(0x0, 0x1000)
    OP_74(0x0, 0x1E)
    OP_70(0x0, 0x1E)
    FadeToBright(1000, 0)

    def lambda_29EC():
        OP_97(0xFE, 0x7D0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_29EC)

    def lambda_2A06():
        OP_97(0xFE, 0x7D0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2A06)

    def lambda_2A20():
        OP_97(0xFE, 0x7D0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2A20)

    def lambda_2A3A():
        OP_97(0xFE, 0x7D0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2A3A)
    OP_0D()
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
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
    OP_68(15320, 1000, 6120, 2500)
    OP_6F(0x1)
    OP_71(0x0, 0x1F, 0x3C, 0x0, 0x0)
    Sound(463, 0, 100, 0)
    OP_79(0x0)

    #C0037
    ChrTalk(
        0x101,
        "#0011Fしまった……！\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x19, 1, 0, 29)
    OP_71(0x0, 0x3C, 0x5A, 0x0, 0x0)
    OP_79(0x0)
    OP_71(0x0, 0xB4, 0x79, 0x0, 0x20)

    def lambda_2B34():
        OP_98(0xFE, 0x3E8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_2B34)
    WaitChrThread(0xA, 1)
    Sleep(100)
    OP_68(15320, 1000, 0, 4000)
    OP_71(0x0, 0x79, 0xB4, 0x0, 0x20)

    def lambda_2B72():
        OP_9E(0xFE, 0x4268, 0x7D0, 0xFFFD40E0, 0xBB8, 0x1)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_2B72)
    WaitChrThread(0xA, 1)
    OP_71(0x0, 0x3C, 0x5A, 0x0, 0x0)
    OP_79(0x0)
    OP_71(0x0, 0x79, 0xB4, 0x0, 0x20)

    def lambda_2BAC():
        OP_98(0xFE, 0x4E20, 0x0, 0x0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_2BAC)
    WaitChrThread(0xA, 1)
    SetMapObjFlags(0x0, 0x4)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    OP_6F(0x1)
    OP_68(3200, 800, 0, 2000)

    def lambda_2BED():
        OP_97(0xFE, 0x1B58, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2BED)
    Sleep(50)

    def lambda_2C0A():
        OP_97(0xFE, 0x1B58, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2C0A)
    Sleep(50)

    def lambda_2C27():
        OP_97(0xFE, 0x1B58, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2C27)
    Sleep(50)

    def lambda_2C44():
        OP_97(0xFE, 0x1B58, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2C44)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    OP_6F(0x1)
    Sleep(500)

    #C0038
    ChrTalk(
        0x102,
        "#0106F#6P行っちゃったわね……\x02",
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x104,
        "#0306F#5Pおいおい、そりゃないぜ。\x02",
    )

    CloseMessageWindow()
    OP_93(0x104, 0xB4, 0x1F4)
    Sleep(300)

    #C0040
    ChrTalk(
        0x104,
        (
            "#0308F#5P導力バスってのは\x01",
            "どのくらい出ているんだ？\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x0, 0x1F4)
    Sleep(300)

    #C0041
    ChrTalk(
        0x101,
        (
            "#0006F#12Pう、うーん……\x01",
            "そこそこ数はあるはずだけど。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0x103, 0x0, 0x1F4)
    Sleep(500)

    def lambda_2D63():

        label("loc_2D63")

        TurnDirection(0x101, 0x103, 500)
        Yield()
        Jump("loc_2D63")

    QueueWorkItem2(0x101, 1, lambda_2D63)

    def lambda_2D75():

        label("loc_2D75")

        TurnDirection(0x102, 0x103, 500)
        Yield()
        Jump("loc_2D75")

    QueueWorkItem2(0x102, 1, lambda_2D75)

    def lambda_2D87():

        label("loc_2D87")

        TurnDirection(0x104, 0x103, 500)
        Yield()
        Jump("loc_2D87")

    QueueWorkItem2(0x104, 1, lambda_2D87)
    OP_68(1810, 800, 2340, 2000)

    def lambda_2DAA():
        OP_95(0xFE, 610, 0, 3820, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2DAA)
    WaitChrThread(0x103, 1)
    OP_6F(0x1)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x104, 0x1)

    #C0042
    ChrTalk(
        0x103,
        (
            "#0203F#6P時刻表によると……\x02\x03",

            "#0200F次の便は\x01",
            "２時間後みたいですね。\x02",
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
    Sleep(1000)

    #C0043
    ChrTalk(
        0x102,
        "#0105F#6Pそ、そんなに……？\x02",
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x104,
        (
            "#0306F#11P一日に数本しか\x01",
            "走ってないって事かよ……\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x101,
        (
            "#0006F#12P……困ったな。\x01",
            "今日中に病院くらいまでは\x01",
            "回っておきたいんだけど。\x02\x03",

            "#0008Fかといって他の場所を\x01",
            "先に回るってのもなぁ……\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x102,
        (
            "#0106F#6Pそうね……\x01",
            "捜査方針を立てたばかりだし。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x103)
    OP_93(0x103, 0xB4, 0x1F4)
    Sleep(300)

    #C0047
    ChrTalk(
        0x103,
        (
            "#0200F#5P──だったら\x01",
            "歩いて行けばいいのでは？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0048
    ChrTalk(
        0x101,
        "#0005F#12Pへっ……\x02",
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x102,
        "#0105F#6Pティオちゃん……？\x02",
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x104,
        "#0305F#2Pおいおい……マジかよ？\x02",
    )

    CloseMessageWindow()
    OP_68(1980, 800, 790, 1500)

    def lambda_3080():

        label("loc_3080")

        TurnDirection(0x101, 0x103, 500)
        Yield()
        Jump("loc_3080")

    QueueWorkItem2(0x101, 1, lambda_3080)

    def lambda_3092():

        label("loc_3092")

        TurnDirection(0x102, 0x103, 500)
        Yield()
        Jump("loc_3092")

    QueueWorkItem2(0x102, 1, lambda_3092)

    def lambda_30A4():

        label("loc_30A4")

        TurnDirection(0x104, 0x103, 500)
        Yield()
        Jump("loc_30A4")

    QueueWorkItem2(0x104, 1, lambda_30A4)

    def lambda_30B6():
        OP_95(0xFE, 500, 0, 700, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_30B6)
    WaitChrThread(0x103, 1)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x104, 0x1)

    #C0051
    ChrTalk(
        0x103,
        (
            "#0204F#5P地図で確認する限り、\x01",
            "ここからアルモリカ村まで\x01",
            "歩いて１時間半くらいの距離かと。\x02\x03",

            "#0202F次のバスで行った場合、\x01",
            "待ち時間も考えたら\x01",
            "２時間半はかかるはずです。\x02\x03",

            "歩いた方が\x01",
            "効率的ではないでしょうか……？\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x102,
        (
            "#0100F#6Pなるほど……計算ではそうなるわね。\x02\x03",

            "#0104Fたしかアルモリカ村の前には\x01",
            "田園風景が広がる石畳の道が\x01",
            "通っているはずだし……\x02\x03",

            "#0102Fハイキングがてら行ってみるのも\x01",
            "気分がいいかもしれないわね。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1500)

    #C0053
    ChrTalk(
        0x104,
        (
            "#0306F#5P（おいおい、お嬢さんたち、\x01",
            "  あんなこと言ってるぞ……？）\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x101,
        (
            "#0006F#11P（どう考えても街道を歩いたことが\x01",
            "  無いって雰囲気だよな……）\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    def lambda_335F():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_335F)
    Sleep(50)

    def lambda_336F():
        OP_93(0xFE, 0x5A, 0x12C)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_336F)
    WaitChrThread(0x102, 1)

    #C0055
    ChrTalk(
        0x102,
        "#0105F#6Pどうしたの、２人とも？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)

    #C0056
    ChrTalk(
        0x101,
        (
            "#0012F#11Pい、いや～……\x02\x03",

            "#0001Fえっと、街道には魔獣もいるけど\x01",
            "２人とも大丈夫か？\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x102,
        (
            "#0106F#6Pうーん……それを言われると。\x02\x03",

            "#0100Fでも、今までにもジオフロントに\x01",
            "何度か潜っているわけだし。\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x103,
        (
            "#0203F#6Pそれにわたしは魔導杖の\x01",
            "テストをする必要もあります。\x02\x03",

            "#0200F多少の実戦でしたら\x01",
            "むしろ望むところですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x101,
        (
            "#0006F#11Pうーん……\x02\x03",

            "#0000F──わかった。\x01",
            "そこまで言うなら歩こうか。\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x102,
        "#0100F#6Pええ、そうしましょう。\x02",
    )

    CloseMessageWindow()
    StopBGM(0x5DC)

    def lambda_355B():
        OP_93(0xFE, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_355B)
    Sleep(100)

    def lambda_356B():
        OP_93(0xFE, 0xB4, 0x190)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_356B)
    Sleep(500)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7204", 0)
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0xCC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0061
    ChrTalk(
        0x102,
        (
            "#0109F#12Pふふ、ちょっとだけ楽しみね。\x02\x03",

            "#0102Fこんな事ならお弁当でも\x01",
            "作ってくれば良かったかしら。\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)

    #C0062
    ChrTalk(
        0x103,
        (
            "#0204F#5P……確かに。\x02\x03",

            "#0202Fまあ、お昼前には\x01",
            "村に到着できるはずですから\x01",
            "ランチは向こうで頂けばいいかと。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Sleep(1000)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    OP_64(0x104)

    #C0063
    ChrTalk(
        0x101,
        (
            "#0008F#11P（……２人がへばったら\x01",
            "　俺たちでフォローしよう。）\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x104,
        "#0302F#5P（へいへい、了解。）\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetCameraDistance(25500, 1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-1070, 600, -160, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(25000, 0)
    SetChrPos(0x0, -1070, 0, -160, 90)
    SetScenarioFlags(0x60, 1)
    OP_29(0x3F, 0x1, 0x1)
    EndChrThread(0x19, 0x1)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_28_290C end

    def Function_29_3794(): pass

    label("Function_29_3794")

    Sound(470, 0, 100, 0)
    Sleep(2000)
    Sound(465, 0, 100, 0)
    Sleep(500)
    Sound(467, 0, 100, 0)
    Sleep(4500)
    Sound(469, 0, 100, 0)
    Sleep(2000)
    OP_25(0x1D5, 0x5A)
    Sleep(300)
    OP_25(0x1D5, 0x50)
    Sleep(300)
    OP_25(0x1D5, 0x46)
    Sleep(300)
    OP_25(0x1D5, 0x3C)
    Sleep(300)
    OP_25(0x1D5, 0x32)
    Sleep(300)
    OP_25(0x1D5, 0x28)
    Sleep(300)
    OP_25(0x1D5, 0x1E)
    Sleep(300)
    OP_25(0x1D5, 0x14)
    Sleep(300)
    OP_25(0x1D5, 0xA)
    Return()

    # Function_29_3794 end

    def Function_30_37F5(): pass

    label("Function_30_37F5")

    EventBegin(0x0)
    Sleep(1000)
    OP_68(920, 600, 5160, 5000)
    MoveCamera(45, 21, 0, 5000)
    OP_6E(450, 5000)
    SetCameraDistance(25000, 5000)
    OP_6F(0x79)
    Sound(828, 0, 100, 0)
    SetChrName("")

    #A0065
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "停留所の看板を調べると、\x01",
            "導力バスに乗ることができます。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #A0066
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "選択した行き先へ素早く移動することができ、\x01",
            "各地を効率的に回ることが可能です。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x93, 7)
    EventEnd(0x5)
    Return()

    # Function_30_37F5 end

    def Function_31_38D0(): pass

    label("Function_31_38D0")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E0(0x1)
    LoadChrToIndex("chr/ch07300.itc", 0x23)
    LoadChrToIndex("chr/ch24100.itc", 0x24)
    LoadChrToIndex("chr/ch20800.itc", 0x25)
    LoadChrToIndex("chr/ch33000.itc", 0x26)
    LoadChrToIndex("chr/ch24500.itc", 0x27)
    LoadChrToIndex("chr/ch21200.itc", 0x28)
    LoadChrToIndex("chr/ch21300.itc", 0x29)
    LoadChrToIndex("chr/ch21000.itc", 0x2A)
    LoadChrToIndex("chr/ch21400.itc", 0x2B)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    SetChrChipByIndex(0xB, 0x23)
    SetChrSubChip(0xB, 0x0)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    SetChrChipByIndex(0xC, 0x24)
    SetChrSubChip(0xC, 0x0)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    SetChrChipByIndex(0xD, 0x25)
    SetChrSubChip(0xD, 0x0)
    ClearChrFlags(0xE, 0x80)
    ClearChrBattleFlags(0xE, 0x8000)
    SetChrChipByIndex(0xE, 0x26)
    SetChrSubChip(0xE, 0x0)
    ClearChrFlags(0xF, 0x80)
    ClearChrBattleFlags(0xF, 0x8000)
    SetChrChipByIndex(0xF, 0x27)
    SetChrSubChip(0xF, 0x0)
    ClearChrFlags(0x10, 0x80)
    ClearChrBattleFlags(0x10, 0x8000)
    SetChrChipByIndex(0x10, 0x28)
    SetChrSubChip(0x10, 0x0)
    ClearChrFlags(0x11, 0x80)
    ClearChrBattleFlags(0x11, 0x8000)
    SetChrChipByIndex(0x11, 0x29)
    SetChrSubChip(0x11, 0x0)
    ClearChrFlags(0x12, 0x80)
    ClearChrBattleFlags(0x12, 0x8000)
    SetChrChipByIndex(0x12, 0x2A)
    SetChrSubChip(0x12, 0x0)
    ClearChrFlags(0x13, 0x80)
    ClearChrBattleFlags(0x13, 0x8000)
    SetChrChipByIndex(0x13, 0x2B)
    SetChrSubChip(0x13, 0x0)
    SetChrPos(0x101, 9700, 0, 1350, 270)
    SetChrPos(0x102, 9700, 0, 2950, 270)
    SetChrPos(0x103, 11200, 0, 1350, 270)
    SetChrPos(0x104, 11200, 0, 2950, 270)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xB, 16000, 600, 5380, 180)
    SetChrPos(0xC, 16000, 600, 5380, 180)
    SetChrPos(0xD, 16000, 600, 5380, 180)
    SetChrPos(0xE, 16000, 600, 5380, 180)
    SetChrPos(0xF, 16000, 600, 5380, 180)
    SetChrPos(0x10, 16000, 600, 5380, 180)
    SetChrPos(0x11, 16000, 600, 5380, 180)
    SetChrPos(0x12, 16000, 600, 5380, 180)
    SetChrPos(0x13, 16000, 600, 5380, 180)
    OP_A7(0xB, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xC, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xD, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xF, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x10, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x11, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x12, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x13, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    ClearMapObjFlags(0x0, 0x4)
    OP_78(0x0, 0xA)
    SetMapObjFrame(0x0, "light", 0x0, 0x1)
    OP_49()
    SetChrPos(0xA, 16000, 0, 6000, 0)
    OP_D3(0xA, 0x0, 0x41EB0, 0x0, 0x0)
    SetMapObjFlags(0x0, 0x1000)
    OP_74(0x0, 0x1E)
    OP_70(0x0, 0x1E)
    SetMapObjFlags(0x7, 0x4)
    SetMapObjFlags(0x8, 0x4)
    OP_68(16230, 600, 5720, 0)
    MoveCamera(29, 23, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(28500, 0)
    SetCameraDistance(26000, 12000)
    FadeToBright(1000, 0)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x1, 0xE)"), scpexpr(EXPR_END)), "loc_3BE3")
    Call(0, 36)
    OP_29(0x1B, 0x1, 0x14)
    Jump("loc_3C4A")

    label("loc_3BE3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x1, 0xF)"), scpexpr(EXPR_END)), "loc_3BFE")
    Call(0, 32)
    OP_29(0x1B, 0x1, 0x13)
    Jump("loc_3C4A")

    label("loc_3BFE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x1, 0x10)"), scpexpr(EXPR_END)), "loc_3C19")
    Call(0, 33)
    OP_29(0x1B, 0x1, 0x14)
    Jump("loc_3C4A")

    label("loc_3C19")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x1, 0x11)"), scpexpr(EXPR_END)), "loc_3C34")
    Call(0, 35)
    OP_29(0x1B, 0x1, 0x14)
    Jump("loc_3C4A")

    label("loc_3C34")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x1, 0x12)"), scpexpr(EXPR_END)), "loc_3C4A")
    Call(0, 34)
    OP_29(0x1B, 0x1, 0x14)

    label("loc_3C4A")

    Sleep(1500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)
    SetChrFlags(0xE, 0x80)
    SetChrBattleFlags(0xE, 0x8000)
    SetChrFlags(0xF, 0x80)
    SetChrBattleFlags(0xF, 0x8000)
    SetChrFlags(0x10, 0x80)
    SetChrBattleFlags(0x10, 0x8000)
    SetChrFlags(0x11, 0x80)
    SetChrBattleFlags(0x11, 0x8000)
    SetChrFlags(0x12, 0x80)
    SetChrBattleFlags(0x12, 0x8000)
    SetChrFlags(0x13, 0x80)
    SetChrBattleFlags(0x13, 0x8000)
    OP_49()
    OP_D5(0x23)
    OP_D5(0x24)
    OP_D5(0x25)
    OP_D5(0x26)
    OP_D5(0x27)
    OP_D5(0x28)
    OP_D5(0x29)
    OP_D5(0x2A)
    OP_D5(0x2B)
    SetScenarioFlags(0x5C, 1)
    NewScene("c100C", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_31_38D0 end

    def Function_32_3CD2(): pass

    label("Function_32_3CD2")

    BeginChrThread(0x13, 3, 0, 38)
    Sleep(750)
    BeginChrThread(0x12, 3, 0, 37)
    Sleep(4000)
    BeginChrThread(0xD, 3, 0, 41)
    Sleep(1500)
    BeginChrThread(0x10, 3, 0, 39)
    Sleep(1000)
    BeginChrThread(0x11, 3, 0, 40)
    Sleep(1500)
    BeginChrThread(0xE, 3, 0, 41)
    Sleep(1500)
    BeginChrThread(0xF, 3, 0, 42)
    Sleep(1500)
    BeginChrThread(0xB, 3, 0, 41)
    Sleep(1500)
    BeginChrThread(0xC, 3, 0, 43)
    Sleep(2500)
    OP_6F(0x10)
    Fade(500)
    OP_68(2130, 1200, 2100, 0)
    MoveCamera(317, 22, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(19910, 0)
    OP_0D()
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    WaitChrThread(0xC, 3)

    #C0067
    ChrTalk(
        0x101,
        (
            "#1P#0001F……ちょっと\x01",
            "待ってもらえますか？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_3DD3():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_3DD3)
    BeginChrThread(0x101, 3, 0, 44)
    BeginChrThread(0x102, 3, 0, 45)
    BeginChrThread(0x103, 3, 0, 46)
    BeginChrThread(0x104, 3, 0, 47)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x103, 3)
    WaitChrThread(0x104, 3)
    OP_6F(0x1)

    #C0068
    ChrTalk(
        0xC,
        (
            "#5Pおやおや、さっき国境門のほうで\x01",
            "お話しした坊やたちじゃないの。\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0xC,
        "#5P私になにかご用かしら？\x02",
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x101,
        (
            "#6P#0003F申し遅れましたが……\x02\x03",

            "#0001F俺たちは、\x01",
            "クロスベル警察・特務支援課に\x01",
            "所属している者です。\x02\x03",

            "お婆さん、あなたに……\x01",
            "任意同行をお願いします。\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0xC,
        (
            "#5P……えっ、そ、そんな……\x01",
            "私が何をしたというの？\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0xC,
        (
            "#5Pい、いくらなんでも\x01",
            "あんまりだわ……\x01",
            "こんなか弱いお年寄りに……\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0x101,
        (
            "#6P#0003F……本日、警察の情報筋から、\x01",
            "ある情報が入っていました。\x02\x03",

            "ある犯罪グループが\x01",
            "このクロスベルに\x01",
            "入国しようとしている……\x02\x03",

            "#0001F自分たちは\x01",
            "タングラム門の張込みを任され、\x01",
            "観光客を張っていたんです。\x02\x03",

            "そこに、明らかに\x01",
            "不審な発言をする人物……\x01",
            "そう、あなたが現れたんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0xC,
        "#5Pど、どういうこと……？\x02",
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0x101,
        (
            "#6P#0001Fお婆さん、あなたは\x01",
            "タングラム門の食堂で\x01",
            "不思議なことを言いました。\x02\x03",

            "#0003F『クロスベルに来たのは３年ぶり』……\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0xC,
        "#5P……そ、それがどうしたの？\x02",
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0xC,
        (
            "#5P共和国くらい離れていれば、\x01",
            "３年くらい来ないなんて\x01",
            "珍しくもなんとも……\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0x101,
        (
            "#6P#0003F……問題はその後です。\x02\x03",

            "#0001F『前に来た時に、孫とミシュラムの\x01",
            "  テーマパークで遊んだ』……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0079
    ChrTalk(
        0x102,
        "#12P#0104F……そう、そういうことだったの。\x02",
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0x104,
        (
            "#12P#0300Fなるほど、合点がいったぜ。\x01",
            "そりゃ確かにおかしい話だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0x103,
        "#12P#0200F墓穴を掘りましたね、お婆さん。\x02",
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0xC,
        (
            "#5P？　え、ええっと、\x01",
            "よく意味が……\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x101,
        (
            "#6P#0003F簡単なことです。\x02\x03",

            "あなたがクロスベルを\x01",
            "最後に訪れたという３年前……\x02\x03",

            "#0001Fミシュラム保養地に、\x01",
            "テーマパークなんて\x01",
            "できていなかったんですよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0xC,
        (
            "#5P……えっ！？\x01",
            "そ、そんなバカな……\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0xC,
        (
            "#5P……じゃなくて……\x01",
            "ええっとそれは、その……\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0xC,
        "#5P……そう、勘違いだわ！\x02",
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0xC,
        (
            "#5Pおほほ、私としたことが、\x01",
            "何かで読んだテーマパークのことを\x01",
            "自分の思い出と勘違いして……\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0x101,
        (
            "#6P#0003Fなるほど……勘違いですか。\x02\x03",

            "#0000Fそれじゃあ……\x01",
            "おばあさんの息子夫婦とやらを\x01",
            "呼んでいただきましょうか。\x02\x03",

            "警察に連絡すれば、\x01",
            "すぐに連れてきて頂けるはずです。\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0xC,
        "#5P……！！\x02",
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x101,
        (
            "#6P#0000F……できませんよね。\x01",
            "そんな人物は存在しないのだから。\x02\x03",

            "#0003F不思議な話です。\x01",
            "あったはずのないテーマパークで、\x01",
            "居るはずのないお孫さんと遊んだ……\x02\x03",

            "３年ぶりなどではなく、\x01",
            "定期的にクロスベルを訪れている\x01",
            "からこその勘違いです。\x02\x03",

            "#0001Fそう、悪どい商売を行なう為に、\x01",
            "クロスベルを訪れているからこその。\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0xC,
        (
            "#5Pわ、私、私……\x01",
            "そんなの知らないわ！\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0xC,
        (
            "#5P偽ブランド商品を売りつけるなんて、\x01",
            "そんなひどいこと……\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x102,
        (
            "#12P#0101F……お婆さん、私たちは\x01",
            "確かに偽ブランドの業者を\x01",
            "追っていましたが……\x02\x03",

            "お婆さんにその事は\x01",
            "一度も言っていないはずですよ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0094
    ChrTalk(
        0xC,
        "#5Pあ、あ、あ……\x02",
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0x104,
        (
            "#12P#0309Fははっ、古典的な手に\x01",
            "引っかかっちまったな、バーさん。\x02\x03",

            "#0300Fこれが年貢の納め時ってヤツだぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0x103,
        (
            "#12P#0200Fあなたが知るはずの無い情報を\x01",
            "喋れた理由……\x02\x03",

            "警察本部の取調室で\x01",
            "聞かせていただきましょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0xC,
        "#5P…………………………\x02",
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x101,
        (
            "#6P#0003F（これで解決……だな。）\x02\x03",

            "#0001F……お婆さん、\x01",
            "もう一度言います。\x01",
            "警察本部への任意同行を……\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0xC,
        (
            "#5P#200W……だ#200W……………………\x01",
            "………#200W……………だ……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    #N0100
    NpcTalk(
        0xC,
        "偽ブランド商",
        (
            "#5P#5S……だぁれが行くかね、\x01",
            "このクソガキどもぉぉおおお！！！\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0x101,
        "#6P#0011Fええ！！？\x02",
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x102,
        "#12P#0105Fきゃあ！！\x02",
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0x104,
        "#12P#0305Fな、なんだぁ……！？\x02",
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0x103,
        "#12P#0200F……正体を現しましたね。\x02",
    )

    CloseMessageWindow()
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    #N0105
    NpcTalk(
        0xC,
        "偽ブランド商",
        (
            "#5P#5S人様をだまくらかすような\x01",
            "マネをしおってからにぃぃぃ！\x02",
        )
    )

    CloseMessageWindow()
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    #N0106
    NpcTalk(
        0xC,
        "偽ブランド商",
        (
            "#5P#5Sそんな真似ばかりしてたらね、\x01",
            "いつか女神様から天罰が下るよッ！？\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0x103,
        (
            "#12P#0203F……よくもまぁ、\x01",
            "いけしゃあしゃあと。\x02\x03",

            "#0201F人を騙すような商売をしていたのは\x01",
            "あなたのほうでしょう。\x02",
        )
    )

    CloseMessageWindow()
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    #N0108
    NpcTalk(
        0xC,
        "偽ブランド商",
        "#5P#5Sうるさいんだよ、チビガキ！\x02",
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0x103,
        "#12P#0205Fチッ……チビガキ……！？\x02",
    )

    CloseMessageWindow()
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    #N0110
    NpcTalk(
        0xC,
        "偽ブランド商",
        (
            "#5P#5Sあーぁやだやだ！ だから\x01",
            "警察だの遊撃士だのは嫌いなんだ！\x02",
        )
    )

    CloseMessageWindow()
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    #N0111
    NpcTalk(
        0xC,
        "偽ブランド商",
        (
            "#5P#5S自分が一番正しいとでも\x01",
            "思ってるのかね、このバカチンが！\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0x101,
        (
            "#6P#0011Fと、とにかく、落ち着いてください！\x01",
            "大人しく任意同行してくれれば……\x02",
        )
    )

    CloseMessageWindow()
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    #N0113
    NpcTalk(
        0xC,
        "偽ブランド商",
        (
            "#5P#5Sお黙り小僧！\x01",
            "行かないって言ったばかりだよ！\x02",
        )
    )

    CloseMessageWindow()
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    #N0114
    NpcTalk(
        0xC,
        "偽ブランド商",
        (
            "#5P#5S何度も同じ事を\x01",
            "言わせるんじゃないよ！\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0x101,
        (
            "#6P#0006F（何度も同じ事を\x01",
            "  言わせないでくれ……！）\x02",
        )
    )

    CloseMessageWindow()

    #N0116
    NpcTalk(
        0xC,
        "偽ブランド商",
        (
            "#5Pこのアタシを\x01",
            "捕まえられるものなら……\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0x7D0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_4E78():
        OP_98(0xFE, 0xFFFFFE0C, 0x0, 0xFFFFFE0C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_4E78)
    Sleep(1000)

    def lambda_4E95():
        OP_98(0xFE, 0xFFFFFE0C, 0x0, 0x1F4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_4E95)
    Sleep(1000)
    Sleep(10)
    PlayBGM("ed7401", 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x191), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetCameraDistance(21000, 3000)

    def lambda_4ECB():
        OP_95(0xFE, -22570, 0, 2200, 10000, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_4ECB)
    Sound(250, 0, 80, 0)
    OP_82(0x0, 0x64, 0xBB8, 0xC8)
    SetMessageWindowPos(-50, 20, -1, -1)
    SetChrName("偽ブランド商")

    #A0117
    AnonymousTalk(
        0xC,
        "#5P#5S捕まえてみせなぁああ！！！\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(14, 280, 60, 3)
    WaitChrThread(0xC, 1)
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    OP_64(0x103)

    #C0118
    ChrTalk(
        0x101,
        (
            "#6P#0005F……う、ウソだろ……\x01",
            "なんてスピードだ……\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0x104,
        (
            "#12P#0306Fつーか、さっきまでの\x01",
            "上品なお婆さんキャラは\x01",
            "どこにいっちまったんだよ……\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0x103,
        "#12P#0206Fちびがき……\x02",
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0x102,
        (
            "#12P#0103Fも、もう！　呆けてる場合！？\x02\x03",

            "#0101F速く追わないと……\x01",
            "本当に逃げる気よ、アレ！\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0x101,
        (
            "#6P#0001Fそ、そうだな……\x01",
            "行くぞ、みんな！\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x101, 3, 0, 48)
    BeginChrThread(0x102, 3, 0, 48)
    BeginChrThread(0x103, 3, 0, 48)
    BeginChrThread(0x104, 3, 0, 48)
    Return()

    # Function_32_3CD2 end

    def Function_33_50F5(): pass

    label("Function_33_50F5")

    BeginChrThread(0x13, 3, 0, 38)
    Sleep(750)
    BeginChrThread(0x12, 3, 0, 37)
    Sleep(4000)
    BeginChrThread(0xD, 3, 0, 41)
    Sleep(1500)
    BeginChrThread(0x10, 3, 0, 39)
    Sleep(1000)
    BeginChrThread(0x11, 3, 0, 40)
    Sleep(1500)
    BeginChrThread(0xE, 3, 0, 41)
    Sleep(1500)
    BeginChrThread(0xF, 3, 0, 42)
    Sleep(1500)
    BeginChrThread(0xC, 3, 0, 41)
    Sleep(1500)
    BeginChrThread(0xB, 3, 0, 43)
    Sleep(2500)
    OP_6F(0x10)
    Fade(500)
    OP_68(2130, 1200, 2100, 0)
    MoveCamera(317, 22, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(19910, 0)
    OP_0D()
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    WaitChrThread(0xB, 3)

    #C0123
    ChrTalk(
        0x101,
        (
            "#1P#0001F……ちょっと\x01",
            "待ってもらえますか？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_51F6():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_51F6)
    BeginChrThread(0x101, 3, 0, 44)
    BeginChrThread(0x102, 3, 0, 45)
    BeginChrThread(0x103, 3, 0, 46)
    BeginChrThread(0x104, 3, 0, 47)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x103, 3)
    WaitChrThread(0x104, 3)
    OP_6F(0x1)

    #C0124
    ChrTalk(
        0xB,
        "#5P#3405Fあら……私に何かご用かしら？\x02",
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0x101,
        (
            "#6P#0000F申し遅れましたが……\x02\x03",

            "俺たちは、\x01",
            "クロスベル警察・特務支援課に\x01",
            "所属している者です。\x02\x03",

            "あなたに……\x01",
            "任意同行をお願いします。\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0xB,
        (
            "#5P#3403F……ふむ。\x02\x03",

            "さっきバスの中で話していた\x01",
            "偽ブランド業者とやら……\x02\x03",

            "#3400Fそれが、この私とでも言うつもりかしら？\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0x101,
        (
            "#6P#0005F……へ？\x02\x03",

            "（き、聞かれてたのか……？）\x02",
        )
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0xB,
        (
            "#5P#3403F……着眼点は悪くない。\x02\x03",

            "私はあなた達に詳しいことを\x01",
            "何一つ話さなかった……\x01",
            "疑う理由にはなりえる。\x02\x03",

            "#3401Fだけど……もっと重要な、\x01",
            "それでいて分かりやすいポイントが\x01",
            "隠されているはず。\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0x101,
        "#6P#0005F分かりやすいポイント……？\x02",
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0xB,
        (
            "#5P#3403F食堂で聞こえてきた\x01",
            "あなたたちと乗客の会話……\x01",
            "そこに不自然な点があった。\x02\x03",

            "#3401Fそれは……あの心優しそうな\x01",
            "お婆さんとの会話。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0131
    ChrTalk(
        0x102,
        (
            "#12P#0105F３年ぶりにお孫さんに会うって\x01",
            "あんなに嬉しそうにしていた……\x01",
            "あのお婆さんですか！？\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0x101,
        (
            "#6P#0005F一体、何故……？\x01",
            "あの人の話に不審な点なんて……\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0xB,
        (
            "#5P#3403F彼女との会話をよく思い出して。\x02\x03",

            "『クロスベルに来たのは３年ぶり』……\x02\x03",

            "そして……\x01",
            "『前に来た時に、孫とミシュラムの\x01",
            "  テーマパークで遊んだ』という台詞。\x02\x03",

            "#3402Fあなた達がクロスベルに住む者なら、\x01",
            "明確な矛盾点に気づけるはず。\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0x101,
        (
            "#6P#0005F……あ……！！\x02\x03",

            "そうか、そういうことだったのか……！\x02",
        )
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0x103,
        (
            "#12P#0200F……３年前のミシュラムに\x01",
            "テーマパークはありません。\x02\x03",

            "あるはずのない場所での\x01",
            "思い出を語っていた……\x02",
        )
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0x104,
        (
            "#12P#0301F……あの場で\x01",
            "一番怪しいことを言ってたのは、\x01",
            "あのバーさんってことか。\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0x102,
        (
            "#12P#0106Fこんな簡単なことに\x01",
            "気づかなかったなんて……\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0xB,
        (
            "#5P#3400F彼女が被っていた\x01",
            "『優しい老婆』の仮面に、\x01",
            "まんまと惑わされていたのでしょう。\x02\x03",

            "３年ぶりなどではなく、\x01",
            "定期的にクロスベルを訪れている\x01",
            "からこその勘違い……\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0x101,
        (
            "#6P#0003F偽ブランド業者として\x01",
            "定期的にクロスベルを訪れている……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5911():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5911)

    def lambda_591E():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_591E)

    def lambda_592B():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_592B)

    def lambda_5938():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_5938)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    #C0140
    ChrTalk(
        0x101,
        "#6P#0005F……あ、あのお婆さんは！？\x02",
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0x103,
        "#12P#0200Fおそらく今頃、東通りにいる頃かと。\x02",
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0x104,
        "#12P#0301F急がねぇと見失いそうだな。\x02",
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0x102,
        "#12P#0101Fロ、ロイド！\x02",
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0x101,
        "#6P#0001Fあ、ああ……分かってる！\x02",
    )

    CloseMessageWindow()

    def lambda_5A1D():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5A1D)

    def lambda_5A2A():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5A2A)

    def lambda_5A37():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5A37)

    def lambda_5A44():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_5A44)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    #C0145
    ChrTalk(
        0x101,
        (
            "#6P#0006Fほ、本当に申し訳ありませんでした！\x01",
            "それと……ありがとうございます！\x02\x03",

            "#0001F後で改めて謝罪させていただくので、\x01",
            "この場は……！\x02",
        )
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0xB,
        (
            "#5P#3403F構わないわ。\x02\x03",

            "今はそんなことをしている暇も\x01",
            "惜しいのではなくて？\x02",
        )
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0x101,
        (
            "#6P#0005Fあ……はい！\x02\x03",

            "#0001F行くぞ、みんな！\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(21000, 3000)

    def lambda_5B76():
        OP_93(0xFE, 0x10E, 0x64)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_5B76)
    BeginChrThread(0x101, 3, 0, 49)
    BeginChrThread(0x102, 3, 0, 49)
    BeginChrThread(0x103, 3, 0, 49)
    BeginChrThread(0x104, 3, 0, 49)
    Return()

    # Function_33_50F5 end

    def Function_34_5B97(): pass

    label("Function_34_5B97")

    BeginChrThread(0x13, 3, 0, 38)
    Sleep(750)
    BeginChrThread(0x12, 3, 0, 37)
    Sleep(4000)
    BeginChrThread(0xD, 3, 0, 41)
    Sleep(1500)
    BeginChrThread(0x10, 3, 0, 39)
    Sleep(1000)
    BeginChrThread(0x11, 3, 0, 40)
    Sleep(1500)
    BeginChrThread(0xF, 3, 0, 41)
    Sleep(1500)
    BeginChrThread(0xC, 3, 0, 42)
    Sleep(1500)
    BeginChrThread(0xB, 3, 0, 41)
    Sleep(1500)
    BeginChrThread(0xE, 3, 0, 43)
    Sleep(2500)
    OP_6F(0x10)
    Fade(500)
    OP_68(2130, 1200, 2100, 0)
    MoveCamera(317, 22, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(19910, 0)
    OP_0D()
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    WaitChrThread(0xE, 3)

    #C0148
    ChrTalk(
        0x101,
        (
            "#1P#0001F……ちょっと\x01",
            "待ってもらえますか？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_5C98():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_5C98)
    BeginChrThread(0x101, 3, 0, 44)
    BeginChrThread(0x102, 3, 0, 45)
    BeginChrThread(0x103, 3, 0, 46)
    BeginChrThread(0x104, 3, 0, 47)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x103, 3)
    WaitChrThread(0x104, 3)
    OP_6F(0x1)

    #C0149
    ChrTalk(
        0xE,
        (
            "#5Pおや、さっきタングラム門で\x01",
            "会った方々ではないですか。\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0xE,
        "#5P私に何かご用ですかな？\x02",
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0x101,
        (
            "#6P#0001F申し遅れましたが……\x02\x03",

            "俺たちは、\x01",
            "クロスベル警察・特務支援課に\x01",
            "所属している者です。\x02\x03",

            "あなたに……\x01",
            "任意同行をお願いします。\x02",
        )
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0xE,
        "#5P……け、警察！？\x02",
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0xE,
        "#5Pわ、私が一体何をしたって……\x02",
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0x101,
        (
            "#6P#0003F……これから推理をお話します。\x02\x03",

            "#0001Fいいですか、まず……\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-50, 20, -1, -1)
    SetChrName("女性の声")

    #A0155
    AnonymousTalk(
        0xB,
        "#1P──その必要はないわ。\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(14, 280, 60, 3)

    #C0156
    ChrTalk(
        0x101,
        "#6P#0005Fえ……\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, -10500, 0, 2200, 90)

    def lambda_5EA1():
        OP_95(0xFE, -800, 0, 2200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_5EA1)

    def lambda_5EBB():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_5EBB)
    WaitChrThread(0xE, 1)
    Sleep(3800)

    def lambda_5ECF():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_5ECF)

    def lambda_5EDC():
        OP_98(0xFE, 0x0, 0x0, 0x5DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_5EDC)
    WaitChrThread(0xB, 1)

    #C0157
    ChrTalk(
        0x101,
        "#6P#0005Fあ、あなたは……\x02",
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0x104,
        (
            "#12P#0305F黒髪のお姉さん！？\x01",
            "街に入っていったんじゃ……\x02",
        )
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0xB,
        (
            "#5P#3404Fええ、まあね。\x02\x03",

            "#3400Fだけど、あなた達がこの人を\x01",
            "呼び止めるのが見えて戻ってきたの。\x02",
        )
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0x103,
        "#12P#0205Fどういうことですか？\x02",
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0xB,
        (
            "#5P#3401F単刀直入に言うわ。\x02\x03",

            "さっきバスの中で話していた\x01",
            "偽ブランド業者とやら……\x02\x03",

            "#3403Fこの人は、その犯人ではない。\x02",
        )
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0x101,
        (
            "#6P#0005F……え。\x02\x03",

            "な……なんですって……！？\x02\x03",

            "（ていうか、バスでの会話を\x01",
            "  聞かれてたのか……？）\x02",
        )
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0xB,
        (
            "#5P#3403F……着眼点は悪くない。\x02\x03",

            "貿易商という彼の職業上……\x01",
            "偽ブランド業者という言葉は\x01",
            "安易に結びつきやすい。\x02\x03",

            "#3401Fだけど……もっと重要な、\x01",
            "それでいて分かりやすいポイントが\x01",
            "隠されているはず。\x02",
        )
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0x101,
        "#6P#0005F分かりやすいポイント……？\x02",
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0xB,
        (
            "#5P#3403F食堂で聞こえてきた\x01",
            "あなたたちと乗客の会話……\x01",
            "そこに不自然な点があった。\x02\x03",

            "#3401Fそれは……あの心優しそうな\x01",
            "お婆さんとの会話。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0166
    ChrTalk(
        0x102,
        (
            "#12P#0105F３年ぶりにお孫さんに会うって\x01",
            "あんなに嬉しそうにしていた……\x01",
            "あのお婆さんですか！？\x02",
        )
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0x101,
        (
            "#6P#0005F一体、何故……？\x01",
            "あの人の話に不審な点なんて……\x02",
        )
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0xB,
        (
            "#5P#3403F彼女との会話をよく思い出して。\x02\x03",

            "『クロスベルに来たのは３年ぶり』……\x02\x03",

            "そして……\x01",
            "『前に来た時に、孫とミシュラムの\x01",
            "  テーマパークで遊んだ』という台詞。\x02\x03",

            "#3402Fあなた達がクロスベルに住む者なら、\x01",
            "明確な矛盾点に気づけるはず。\x02",
        )
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0x101,
        (
            "#6P#0005F……あ……！！\x02\x03",

            "そうか、そういうことだったのか……！\x02",
        )
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0x103,
        (
            "#12P#0200F……３年前のミシュラムに\x01",
            "テーマパークはありません。\x02\x03",

            "あるはずのない場所での\x01",
            "思い出を語っていた……\x02",
        )
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0x104,
        (
            "#12P#0301F……あの場で\x01",
            "一番怪しいことを言ってたのは、\x01",
            "あのバーさんってことか。\x02",
        )
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0x102,
        (
            "#12P#0106Fこんな簡単なことに\x01",
            "気づかなかったなんて……\x02",
        )
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0xB,
        (
            "#5P#3400F彼女が被っていた\x01",
            "『優しい老婆』の仮面に、\x01",
            "まんまと惑わされていたのでしょう。\x02\x03",

            "３年ぶりなどではなく、\x01",
            "定期的にクロスベルを訪れている\x01",
            "からこその勘違い……\x02",
        )
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0x101,
        (
            "#6P#0003F偽ブランド業者として\x01",
            "定期的にクロスベルを訪れている……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_6642():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6642)

    def lambda_664F():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_664F)

    def lambda_665C():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_665C)

    def lambda_6669():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_6669)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    #C0175
    ChrTalk(
        0x101,
        "#6P#0005F……あ、あのお婆さんは！？\x02",
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0x103,
        "#12P#0200Fおそらく今頃、東通りにいる頃かと。\x02",
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0x104,
        "#12P#0301F急がねぇと見失いそうだな。\x02",
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0x102,
        "#12P#0101Fロ、ロイド！\x02",
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0x101,
        "#6P#0001Fあ、ああ……分かってる！\x02",
    )

    CloseMessageWindow()

    def lambda_674E():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_674E)

    def lambda_675B():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_675B)

    def lambda_6768():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_6768)

    def lambda_6775():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_6775)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    #C0180
    ChrTalk(
        0x101,
        (
            "#6P#0006Fほ、本当に申し訳ありませんでした！\x01",
            "大変な失礼を……\x02\x03",

            "後で改めて謝罪させていただくので、\x01",
            "この場は……！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_6807():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_6807)
    WaitChrThread(0xE, 1)

    #C0181
    ChrTalk(
        0xE,
        (
            "#5Pは、はぁ。\x01",
            "何がなんだか……？\x02",
        )
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0xB,
        (
            "#5P#3403F……今はそんなことをしている暇も\x01",
            "惜しいのではなくて？\x02",
        )
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0x101,
        (
            "#6P#0005Fあ……はい！\x02\x03",

            "#0001F行くぞ、みんな！\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(21000, 3000)

    def lambda_68BE():
        OP_93(0xFE, 0x10E, 0x64)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_68BE)

    def lambda_68CB():
        OP_93(0xFE, 0x10E, 0x64)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_68CB)
    BeginChrThread(0x101, 3, 0, 49)
    BeginChrThread(0x102, 3, 0, 49)
    BeginChrThread(0x103, 3, 0, 49)
    BeginChrThread(0x104, 3, 0, 49)
    Return()

    # Function_34_5B97 end

    def Function_35_68EC(): pass

    label("Function_35_68EC")

    BeginChrThread(0x13, 3, 0, 38)
    Sleep(750)
    BeginChrThread(0x12, 3, 0, 37)
    Sleep(4000)
    BeginChrThread(0xD, 3, 0, 41)
    Sleep(1500)
    BeginChrThread(0x10, 3, 0, 39)
    Sleep(1000)
    BeginChrThread(0x11, 3, 0, 40)
    Sleep(1500)
    BeginChrThread(0xE, 3, 0, 41)
    Sleep(1500)
    BeginChrThread(0xC, 3, 0, 42)
    Sleep(1500)
    BeginChrThread(0xB, 3, 0, 41)
    Sleep(1500)
    BeginChrThread(0xF, 3, 0, 43)
    Sleep(2500)
    OP_6F(0x10)
    Fade(500)
    OP_68(2130, 1200, 2100, 0)
    MoveCamera(317, 22, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(19910, 0)
    OP_0D()
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    WaitChrThread(0xF, 3)

    #C0184
    ChrTalk(
        0x101,
        (
            "#1P#0001F……ちょっと\x01",
            "待ってもらえますか？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xF, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_69ED():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_69ED)
    BeginChrThread(0x101, 3, 0, 44)
    BeginChrThread(0x102, 3, 0, 45)
    BeginChrThread(0x103, 3, 0, 46)
    BeginChrThread(0x104, 3, 0, 47)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x103, 3)
    WaitChrThread(0x104, 3)
    OP_6F(0x1)

    #C0185
    ChrTalk(
        0xF,
        "#5Pあら……さっきの。\x02",
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0xF,
        "#5P私に何か用でもあるの？\x02",
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0x101,
        (
            "#6P#0001F申し遅れましたが……\x02\x03",

            "俺たちは、\x01",
            "クロスベル警察・特務支援課に\x01",
            "所属している者です。\x02\x03",

            "あなたに……\x01",
            "任意同行をお願いします。\x02",
        )
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0xF,
        "#5P……はあ？\x02",
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0xF,
        (
            "#5P私が一体何をしたっていうの？\x01",
            "寝言も大概にしなさいよ！！\x02",
        )
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0x101,
        (
            "#6P#0003F……これから推理をお話します。\x02\x03",

            "#0001Fいいですか、まず……\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-50, 20, -1, -1)
    SetChrName("女性の声")

    #A0191
    AnonymousTalk(
        0xB,
        "#1P──その必要はないわ。\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(14, 280, 60, 3)

    #C0192
    ChrTalk(
        0x101,
        "#6P#0005Fえ……\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, -10500, 0, 2200, 90)

    def lambda_6BE8():
        OP_95(0xFE, -800, 0, 2200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_6BE8)

    def lambda_6C02():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_6C02)
    WaitChrThread(0xF, 1)
    Sleep(3800)

    def lambda_6C16():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_6C16)

    def lambda_6C23():
        OP_98(0xFE, 0x0, 0x0, 0x5DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 2, lambda_6C23)
    WaitChrThread(0xB, 1)

    #C0193
    ChrTalk(
        0x101,
        "#6P#0005Fあ、あなたは……\x02",
    )

    CloseMessageWindow()

    #C0194
    ChrTalk(
        0x104,
        (
            "#12P#0305F黒髪のお姉さん！？\x01",
            "街に入っていったんじゃ……\x02",
        )
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0xB,
        (
            "#5P#3404Fええ、まあね。\x02\x03",

            "#3400Fだけど、あなた達がこの人を\x01",
            "呼び止めるのが見えて戻ってきたの。\x02",
        )
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0x103,
        "#12P#0205Fどういうことですか？\x02",
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0xB,
        (
            "#5P#3401F単刀直入に言うわ。\x02\x03",

            "さっきバスの中で話していた\x01",
            "偽ブランド業者とやら……\x02\x03",

            "#3403Fこの人は、その犯人ではない。\x02",
        )
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0x101,
        (
            "#6P#0005F……え。\x02\x03",

            "な……なんですって……！？\x02\x03",

            "（ていうか、バスでの会話を\x01",
            "  聞かれてたのか……？）\x02",
        )
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0xB,
        (
            "#5P#3403F……着眼点は悪くない。\x02\x03",

            "彼女が私を怪しんでいたのを\x01",
            "他人に注意を向けるためだと考えた……\x01",
            "そんなところかしら。\x02\x03",

            "#3401Fだけど……もっと重要な、\x01",
            "それでいて分かりやすいポイントが\x01",
            "隠されているはず。\x02",
        )
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0x101,
        "#6P#0005F分かりやすいポイント……？\x02",
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0xB,
        (
            "#5P#3403F食堂で聞こえてきた\x01",
            "あなたたちと乗客の会話……\x01",
            "そこに不自然な点があった。\x02\x03",

            "#3401Fそれは……あの心優しそうな\x01",
            "お婆さんとの会話。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0202
    ChrTalk(
        0x102,
        (
            "#12P#0105F３年ぶりにお孫さんに会うって\x01",
            "あんなに嬉しそうにしていた……\x01",
            "あのお婆さんですか！？\x02",
        )
    )

    CloseMessageWindow()

    #C0203
    ChrTalk(
        0x101,
        (
            "#6P#0005F一体、何故……？\x01",
            "あの人の話に不審な点なんて……\x02",
        )
    )

    CloseMessageWindow()

    #C0204
    ChrTalk(
        0xB,
        (
            "#5P#3403F彼女との会話をよく思い出して。\x02\x03",

            "『クロスベルに来たのは３年ぶり』……\x02\x03",

            "そして……\x01",
            "『前に来た時に、孫とミシュラムの\x01",
            "  テーマパークで遊んだ』という台詞。\x02\x03",

            "#3402Fあなた達がクロスベルに住む者なら、\x01",
            "明確な矛盾点に気づけるはず。\x02",
        )
    )

    CloseMessageWindow()

    #C0205
    ChrTalk(
        0x101,
        (
            "#6P#0005F……あ……！！\x02\x03",

            "そうか、そういうことだったのか……！\x02",
        )
    )

    CloseMessageWindow()

    #C0206
    ChrTalk(
        0x103,
        (
            "#12P#0200F……３年前のミシュラムに\x01",
            "テーマパークはありません。\x02\x03",

            "あるはずのない場所での\x01",
            "思い出を語っていた……\x02",
        )
    )

    CloseMessageWindow()

    #C0207
    ChrTalk(
        0x104,
        (
            "#12P#0301F……あの場で\x01",
            "一番怪しいことを言ってたのは、\x01",
            "あのバーさんってことか。\x02",
        )
    )

    CloseMessageWindow()

    #C0208
    ChrTalk(
        0x102,
        (
            "#12P#0106Fこんな簡単なことに\x01",
            "気づかなかったなんて……\x02",
        )
    )

    CloseMessageWindow()

    #C0209
    ChrTalk(
        0xB,
        (
            "#5P#3400F彼女が被っていた\x01",
            "『優しい老婆』の仮面に、\x01",
            "まんまと惑わされていたのでしょう。\x02\x03",

            "３年ぶりなどではなく、\x01",
            "定期的にクロスベルを訪れている\x01",
            "からこその勘違い……\x02",
        )
    )

    CloseMessageWindow()

    #C0210
    ChrTalk(
        0x101,
        (
            "#6P#0003F偽ブランド業者として\x01",
            "定期的にクロスベルを訪れている……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_7391():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7391)

    def lambda_739E():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_739E)

    def lambda_73AB():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_73AB)

    def lambda_73B8():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_73B8)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    #C0211
    ChrTalk(
        0x101,
        "#6P#0005F……あ、あのお婆さんは！？\x02",
    )

    CloseMessageWindow()

    #C0212
    ChrTalk(
        0x103,
        "#12P#0200Fおそらく今頃、東通りにいる頃かと。\x02",
    )

    CloseMessageWindow()

    #C0213
    ChrTalk(
        0x104,
        "#12P#0301F急がねぇと見失いそうだな。\x02",
    )

    CloseMessageWindow()

    #C0214
    ChrTalk(
        0x102,
        "#12P#0101Fロ、ロイド！\x02",
    )

    CloseMessageWindow()

    #C0215
    ChrTalk(
        0x101,
        "#6P#0001Fあ、ああ……分かってる！\x02",
    )

    CloseMessageWindow()

    def lambda_749D():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_749D)

    def lambda_74AA():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_74AA)

    def lambda_74B7():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_74B7)

    def lambda_74C4():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_74C4)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    #C0216
    ChrTalk(
        0x101,
        (
            "#6P#0006Fほ、本当に申し訳ありませんでした！\x01",
            "大変な失礼を……\x02\x03",

            "後で改めて謝罪させていただくので、\x01",
            "この場は……！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_7556():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_7556)
    WaitChrThread(0xF, 1)

    #C0217
    ChrTalk(
        0xF,
        (
            "#5Pほ、ほんとよ！\x01",
            "とんだ無礼だわ、まったく……！\x02",
        )
    )

    CloseMessageWindow()

    #C0218
    ChrTalk(
        0xB,
        (
            "#5P#3403F……今はそんなことをしている暇も\x01",
            "惜しいのではなくて？\x02",
        )
    )

    CloseMessageWindow()

    #C0219
    ChrTalk(
        0x101,
        (
            "#6P#0005Fあ……はい！\x02\x03",

            "#0001F行くぞ、みんな！\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(21000, 3000)

    def lambda_761D():
        OP_93(0xFE, 0x10E, 0x64)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_761D)

    def lambda_762A():
        OP_93(0xFE, 0x10E, 0x64)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_762A)
    BeginChrThread(0x101, 3, 0, 49)
    BeginChrThread(0x102, 3, 0, 49)
    BeginChrThread(0x103, 3, 0, 49)
    BeginChrThread(0x104, 3, 0, 49)
    Return()

    # Function_35_68EC end

    def Function_36_764B(): pass

    label("Function_36_764B")

    BeginChrThread(0x13, 3, 0, 38)
    Sleep(750)
    BeginChrThread(0x12, 3, 0, 37)
    Sleep(4000)
    BeginChrThread(0xF, 3, 0, 41)
    Sleep(1500)
    BeginChrThread(0x10, 3, 0, 39)
    Sleep(1000)
    BeginChrThread(0x11, 3, 0, 40)
    Sleep(1500)
    BeginChrThread(0xE, 3, 0, 41)
    Sleep(1500)
    BeginChrThread(0xC, 3, 0, 42)
    Sleep(1500)
    BeginChrThread(0xB, 3, 0, 41)
    Sleep(1500)
    BeginChrThread(0xD, 3, 0, 43)
    Sleep(2500)
    OP_6F(0x10)
    Fade(500)
    OP_68(2130, 1200, 2100, 0)
    MoveCamera(317, 22, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(19910, 0)
    OP_0D()
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    WaitChrThread(0xD, 3)

    #C0220
    ChrTalk(
        0x101,
        (
            "#1P#0001F……ちょっと\x01",
            "待ってもらえますか？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_774C():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_774C)
    BeginChrThread(0x101, 3, 0, 44)
    BeginChrThread(0x102, 3, 0, 45)
    BeginChrThread(0x103, 3, 0, 46)
    BeginChrThread(0x104, 3, 0, 47)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x103, 3)
    WaitChrThread(0x104, 3)
    OP_6F(0x1)

    #C0221
    ChrTalk(
        0xD,
        "#5P…………なんじゃ。\x02",
    )

    CloseMessageWindow()

    #C0222
    ChrTalk(
        0xD,
        (
            "#5Pまた、わしを\x01",
            "からかうつもりか？\x02",
        )
    )

    CloseMessageWindow()

    #C0223
    ChrTalk(
        0x101,
        (
            "#6P#0001F申し遅れましたが……\x02\x03",

            "俺たちは、\x01",
            "クロスベル警察・特務支援課に\x01",
            "所属している者です。\x02\x03",

            "あなたに……\x01",
            "任意同行をお願いします。\x02",
        )
    )

    CloseMessageWindow()

    #C0224
    ChrTalk(
        0xD,
        "#5P……な、な、な……！\x02",
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0xD,
        (
            "#5Pば、バカにするでないぞ！\x01",
            "たちの悪い冗談を言いおって……！\x02",
        )
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0x101,
        (
            "#6P#0003F……これから推理をお話します。\x02\x03",

            "#0001Fいいですか、まず……\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-50, 20, -1, -1)
    SetChrName("女性の声")

    #A0227
    AnonymousTalk(
        0xB,
        "#1P──その必要はないわ。\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(14, 280, 60, 3)

    #C0228
    ChrTalk(
        0x101,
        "#6P#0005Fえ……\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, -10500, 0, 2200, 90)

    def lambda_795C():
        OP_95(0xFE, -800, 0, 2200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_795C)

    def lambda_7976():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_7976)
    WaitChrThread(0xD, 1)
    Sleep(3800)

    def lambda_798A():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_798A)

    def lambda_7997():
        OP_98(0xFE, 0x0, 0x0, 0x5DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_7997)
    WaitChrThread(0xB, 1)

    #C0229
    ChrTalk(
        0x101,
        "#6P#0005Fあ、あなたは……\x02",
    )

    CloseMessageWindow()

    #C0230
    ChrTalk(
        0x104,
        (
            "#12P#0305F黒髪のお姉さん！？\x01",
            "街に入っていったんじゃ……\x02",
        )
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0xB,
        (
            "#5P#3404Fええ、まあね。\x02\x03",

            "#3400Fだけど、あなた達がこの人を\x01",
            "呼び止めるのが見えて戻ってきたの。\x02",
        )
    )

    CloseMessageWindow()

    #C0232
    ChrTalk(
        0x103,
        "#12P#0205Fどういうことですか？\x02",
    )

    CloseMessageWindow()

    #C0233
    ChrTalk(
        0xB,
        (
            "#5P#3401F単刀直入に言うわ。\x02\x03",

            "さっきバスの中で話していた\x01",
            "偽ブランド業者とやら……\x02\x03",

            "#3403Fこの人は、その犯人ではない。\x02",
        )
    )

    CloseMessageWindow()

    #C0234
    ChrTalk(
        0x101,
        (
            "#6P#0005F……え。\x02\x03",

            "な……なんですって……！？\x02\x03",

            "（ていうか、バスでの会話を\x01",
            "  聞かれてたのか……？）\x02",
        )
    )

    CloseMessageWindow()

    #C0235
    ChrTalk(
        0xB,
        (
            "#5P#3403F……着眼点は悪くない。\x02\x03",

            "人とあまり話したがらない\x01",
            "彼の性格を不審に思った……\x01",
            "そんなところでしょう。\x02\x03",

            "#3401Fだけど……もっと重要な、\x01",
            "それでいて分かりやすいポイントが\x01",
            "隠されているはず。\x02",
        )
    )

    CloseMessageWindow()

    #C0236
    ChrTalk(
        0x101,
        "#6P#0005F分かりやすいポイント……？\x02",
    )

    CloseMessageWindow()

    #C0237
    ChrTalk(
        0xB,
        (
            "#5P#3403F食堂で聞こえてきた\x01",
            "あなたたちと乗客の会話……\x01",
            "そこに不自然な点があった。\x02\x03",

            "#3401Fそれは……あの心優しそうな\x01",
            "お婆さんとの会話。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0238
    ChrTalk(
        0x102,
        (
            "#12P#0105F３年ぶりにお孫さんに会うって\x01",
            "あんなに嬉しそうにしていた……\x01",
            "あのお婆さんですか！？\x02",
        )
    )

    CloseMessageWindow()

    #C0239
    ChrTalk(
        0x101,
        (
            "#6P#0005F一体、何故……？\x01",
            "あの人の話に不審な点なんて……\x02",
        )
    )

    CloseMessageWindow()

    #C0240
    ChrTalk(
        0xB,
        (
            "#5P#3403F彼女との会話をよく思い出して。\x02\x03",

            "『クロスベルに来たのは３年ぶり』……\x02\x03",

            "そして……\x01",
            "『前に来た時に、孫とミシュラムの\x01",
            "  テーマパークで遊んだ』という台詞。\x02\x03",

            "#3402Fあなた達がクロスベルに住む者なら、\x01",
            "明確な矛盾点に気づけるはず。\x02",
        )
    )

    CloseMessageWindow()

    #C0241
    ChrTalk(
        0x101,
        (
            "#6P#0005F……あ……！！\x02\x03",

            "そうか、そういうことだったのか……！\x02",
        )
    )

    CloseMessageWindow()

    #C0242
    ChrTalk(
        0x103,
        (
            "#12P#0200F……３年前のミシュラムに\x01",
            "テーマパークはありません。\x02\x03",

            "あるはずのない場所での\x01",
            "思い出を語っていた……\x02",
        )
    )

    CloseMessageWindow()

    #C0243
    ChrTalk(
        0x104,
        (
            "#12P#0301F……あの場で\x01",
            "一番怪しいことを言ってたのは、\x01",
            "あのバーさんってことか。\x02",
        )
    )

    CloseMessageWindow()

    #C0244
    ChrTalk(
        0x102,
        (
            "#12P#0106Fこんな簡単なことに\x01",
            "気づかなかったなんて……\x02",
        )
    )

    CloseMessageWindow()

    #C0245
    ChrTalk(
        0xB,
        (
            "#5P#3400F彼女が被っていた\x01",
            "『優しい老婆』の仮面に、\x01",
            "まんまと惑わされていたのでしょう。\x02\x03",

            "３年ぶりなどではなく、\x01",
            "定期的にクロスベルを訪れている\x01",
            "からこその勘違い……\x02",
        )
    )

    CloseMessageWindow()

    #C0246
    ChrTalk(
        0x101,
        (
            "#6P#0003F偽ブランド業者として\x01",
            "定期的にクロスベルを訪れている……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_80FB():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_80FB)

    def lambda_8108():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8108)

    def lambda_8115():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_8115)

    def lambda_8122():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_8122)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    #C0247
    ChrTalk(
        0x101,
        "#6P#0005F……あ、あのお婆さんは！？\x02",
    )

    CloseMessageWindow()

    #C0248
    ChrTalk(
        0x103,
        "#12P#0200Fおそらく今頃、東通りにいる頃かと。\x02",
    )

    CloseMessageWindow()

    #C0249
    ChrTalk(
        0x104,
        "#12P#0301F急がねぇと見失いそうだな。\x02",
    )

    CloseMessageWindow()

    #C0250
    ChrTalk(
        0x102,
        "#12P#0101Fロ、ロイド！\x02",
    )

    CloseMessageWindow()

    #C0251
    ChrTalk(
        0x101,
        "#6P#0001Fあ、ああ……分かってる！\x02",
    )

    CloseMessageWindow()

    def lambda_8207():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8207)

    def lambda_8214():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8214)

    def lambda_8221():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_8221)

    def lambda_822E():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_822E)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    #C0252
    ChrTalk(
        0x101,
        (
            "#6P#0006Fほ、本当に申し訳ありませんでした！\x01",
            "大変な失礼を……\x02\x03",

            "後で改めて謝罪させていただくので、\x01",
            "この場は……！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_82C0():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_82C0)
    WaitChrThread(0xD, 1)

    #C0253
    ChrTalk(
        0xD,
        "ゆ、ゆるさん、ゆるさんぞぉ……！！\x02",
    )

    CloseMessageWindow()

    #C0254
    ChrTalk(
        0xB,
        (
            "#5P#3403F……今はそんなことをしている暇も\x01",
            "惜しいのではなくて？\x02",
        )
    )

    CloseMessageWindow()

    #C0255
    ChrTalk(
        0x101,
        (
            "#6P#0005Fあ……はい！\x02\x03",

            "#0001F行くぞ、みんな！\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(21000, 3000)

    def lambda_8379():
        OP_93(0xFE, 0x10E, 0x64)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_8379)

    def lambda_8386():
        OP_93(0xFE, 0x10E, 0x64)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_8386)
    BeginChrThread(0x101, 3, 0, 49)
    BeginChrThread(0x102, 3, 0, 49)
    BeginChrThread(0x103, 3, 0, 49)
    BeginChrThread(0x104, 3, 0, 49)
    Return()

    # Function_36_764B end

    def Function_37_83A7(): pass

    label("Function_37_83A7")

    Sleep(1200)

    def lambda_83AF():
        OP_95(0xFE, 16000, 0, 2700, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_83AF)

    def lambda_83C9():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_83C9)
    WaitChrThread(0xFE, 1)
    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)

    def lambda_83F3():
        OP_95(0xFE, -12000, 0, 1200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_83F3)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_37_83A7 end

    def Function_38_8416(): pass

    label("Function_38_8416")


    def lambda_841B():
        OP_95(0xFE, 16000, 0, 1200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_841B)

    def lambda_8435():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_8435)
    WaitChrThread(0xFE, 1)

    def lambda_844A():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_844A)
    WaitChrThread(0xFE, 1)
    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(2250)

    def lambda_8470():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8470)
    WaitChrThread(0xFE, 1)

    def lambda_8481():
        OP_95(0xFE, -12000, 0, 2700, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8481)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_38_8416 end

    def Function_39_84A4(): pass

    label("Function_39_84A4")


    def lambda_84A9():
        OP_95(0xFE, 16000, 0, 1200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_84A9)

    def lambda_84C3():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_84C3)
    WaitChrThread(0xFE, 1)

    def lambda_84D8():
        OP_95(0xFE, -12000, 0, 1200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_84D8)
    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_39_84A4 end

    def Function_40_853A(): pass

    label("Function_40_853A")


    def lambda_853F():
        OP_95(0xFE, 16000, 0, 2700, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_853F)

    def lambda_8559():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_8559)
    WaitChrThread(0xFE, 1)

    def lambda_856E():
        OP_95(0xFE, -12000, 0, 2700, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_856E)
    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_40_853A end

    def Function_41_85D0(): pass

    label("Function_41_85D0")


    def lambda_85D5():
        OP_95(0xFE, 16000, 0, 2200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_85D5)

    def lambda_85EF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_85EF)
    WaitChrThread(0xFE, 1)

    def lambda_8604():
        OP_95(0xFE, -12000, 0, 2200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8604)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_41_85D0 end

    def Function_42_8627(): pass

    label("Function_42_8627")


    def lambda_862C():
        OP_95(0xFE, 16000, 0, 2700, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_862C)

    def lambda_8646():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_8646)
    WaitChrThread(0xFE, 1)

    def lambda_865B():
        OP_95(0xFE, -12000, 0, 2700, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_865B)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_42_8627 end

    def Function_43_867E(): pass

    label("Function_43_867E")


    def lambda_8683():
        OP_95(0xFE, 16000, 0, 2200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8683)

    def lambda_869D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_869D)
    WaitChrThread(0xFE, 1)

    def lambda_86B2():
        OP_95(0xFE, 0, 0, 2200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_86B2)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_43_867E end

    def Function_44_86D0(): pass

    label("Function_44_86D0")


    def lambda_86D5():
        OP_95(0xFE, 3000, 0, 1350, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_86D5)
    WaitChrThread(0x101, 1)
    Return()

    # Function_44_86D0 end

    def Function_45_86EF(): pass

    label("Function_45_86EF")


    def lambda_86F4():
        OP_95(0xFE, 3000, 0, 2950, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_86F4)
    WaitChrThread(0x102, 1)
    Return()

    # Function_45_86EF end

    def Function_46_870E(): pass

    label("Function_46_870E")


    def lambda_8713():
        OP_95(0xFE, 4500, 0, 1350, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_8713)
    WaitChrThread(0x103, 1)
    Return()

    # Function_46_870E end

    def Function_47_872D(): pass

    label("Function_47_872D")


    def lambda_8732():
        OP_95(0xFE, 4500, 0, 2950, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_8732)
    WaitChrThread(0x104, 1)
    Return()

    # Function_47_872D end

    def Function_48_874C(): pass

    label("Function_48_874C")


    def lambda_8751():
        OP_98(0xFE, 0xFFFFD8F0, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8751)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_48_874C end

    def Function_49_876B(): pass

    label("Function_49_876B")

    OP_93(0xFE, 0xB4, 0x0)

    def lambda_8777():
        OP_98(0xFE, 0x0, 0x0, 0xFFFFF8F8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8777)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x0)

    def lambda_879C():
        OP_98(0xFE, 0xFFFFD8F0, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_879C)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_49_876B end

    def Function_50_87B6(): pass

    label("Function_50_87B6")


    def lambda_87BB():
        OP_95(0xFE, -10000, 0, 3000, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_87BB)

    def lambda_87D5():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_87D5)
    Return()

    # Function_50_87B6 end

    def Function_51_87DE(): pass

    label("Function_51_87DE")

    EventBegin(0x0)
    Fade(500)
    OP_68(133180, 4800, 81440, 0)
    MoveCamera(8, 31, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(17670, 0)
    OP_E0(0x2)
    SetMapFlags(0x8000000)
    SetChrPos(0x101, 133170, 3000, 82030, 90)
    SetChrPos(0x102, 133230, 3000, 83640, 135)
    SetChrPos(0x103, 132220, 3000, 81240, 45)
    SetChrPos(0x104, 131880, 3000, 83280, 135)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8889")
    SetChrPos(0x10A, 131150, 3000, 81780, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    label("loc_8889")

    OP_0D()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0256
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x34B),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x34B, 1)

    #C0257
    ChrTalk(
        0x101,
        (
            "#12P#0000F白い花……\x01",
            "フィネルの花、だったな。\x02",
        )
    )

    CloseMessageWindow()

    #C0258
    ChrTalk(
        0x102,
        (
            "#12P#11P#0100Fクロスベル市に近い場所だし、\x01",
            "自分で摘みに来る人も\x01",
            "そこそこいるみたいよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0259
    ChrTalk(
        0x104,
        (
            "#5P#0300Fまぁ、ここならそこまで\x01",
            "強い魔獣も出ないだろうしな。\x02",
        )
    )

    CloseMessageWindow()

    #C0260
    ChrTalk(
        0x103,
        (
            "#06P#0200Fそれでも、老人や子供には\x01",
            "脅威には違いありませんけどね。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8A75")

    #C0261
    ChrTalk(
        0x101,
        "#12P#0003Fああ、そうだな。\x02",
    )

    CloseMessageWindow()

    #C0262
    ChrTalk(
        0x10A,
        (
            "#6P#0603F……花を摘んだならさっさと行くぞ。\x01",
            "モタモタしている暇はないんだ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8ABD")

    label("loc_8A75")


    #C0263
    ChrTalk(
        0x101,
        (
            "#12P#0003Fああ、そうだな。\x02\x03",

            "#0000Fよし、それじゃあ行くとしようか。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8ABD")

    OP_65(0x5, 0x1)
    OP_29(0x2E, 0x1, 0x5)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2E, 0x1, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2E, 0x1, 0x4)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2E, 0x1, 0x5)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8AEA")
    OP_29(0x2E, 0x1, 0x6)

    label("loc_8AEA")

    ClearMapFlags(0x8000000)
    OP_37()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8B0A")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)

    label("loc_8B0A")

    SetChrPos(0x0, 133170, 3000, 82030, 90)
    EventEnd(0x5)
    Return()

    # Function_51_87DE end

    def Function_52_8B1E(): pass

    label("Function_52_8B1E")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0264
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "西・クロスベル市\x01",
            "東・アルモリカ村　２７４セルジュ\x01",
            "　　タングラム門　２０６セルジュ\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_52_8B1E end

    SaveToFile()

Try(main)
