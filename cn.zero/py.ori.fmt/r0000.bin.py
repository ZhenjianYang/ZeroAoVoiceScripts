from ZeroScenarioHelper import *

def main():
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
        "巴士",                   # 3
        "黑发女性",               # 4
        "老婆婆",                 # 5
        "老人",                   # 6
        "贸易商",                 # 7
        "女性",                   # 8
        "哥哥",                   # 9
        "妹妹",                   # 10
        "父亲",                   # 11
        "男孩",                   # 12
        "车00",                   # 13
        "车01",                   # 14
        "车02",                   # 15
        "车03",                   # 16
        "车04",                   # 17
        "SE控制",                 # 18
        "br0000",                 # 19
        "br0000",                 # 20
        "克洛斯贝尔市方向",       # 21
        "阿尔摩利卡村·唐古拉姆门方向",# 22
    ))

    ATBonus("ATBonus_5E0", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)

    Sepith("Sepith_8004", 5,   2,   3,   0,   0,   3,   0)
    Sepith("Sepith_800C", 1,   6,   0,   3,   2,   1,   1)

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
        "BattleInfo_6C0", 0x0000, 8, 6, 45, 6, 1, 25, 0, "br0000", "Sepith_8004", 50, 50, 0, 0,
        (
            ("ms66500.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_640", "MonsterBattlePostion_6A0", "ed7400", "ed7403", "ATBonus_5E0"),
            ("ms66500.dat", "ms66500.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_620", "MonsterBattlePostion_6A0", "ed7400", "ed7403", "ATBonus_5E0"),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_730", 0x0000, 8, 6, 45, 6, 1, 25, 0, "br0000", "Sepith_800C", 50, 50, 0, 0,
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

    PlaceName(-17.0, 0.0, -7.0, 0x0000, 0x0000, "克洛斯贝尔市方向")
    PlaceName(203.0, 0.0, 27.5, 0x0000, 0x0000, "阿尔摩利卡村·唐古拉姆门方向")
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
        "Function_4_13B8",         # 04, 4
        "Function_5_14EE",         # 05, 5
        "Function_6_1502",         # 06, 6
        "Function_7_15E1",         # 07, 7
        "Function_8_16FD",         # 08, 8
        "Function_9_1795",         # 09, 9
        "Function_10_1D19",        # 0A, 10
        "Function_11_1E08",        # 0B, 11
        "Function_12_1E5B",        # 0C, 12
        "Function_13_1EBA",        # 0D, 13
        "Function_14_1F12",        # 0E, 14
        "Function_15_1F7F",        # 0F, 15
        "Function_16_1FDB",        # 10, 16
        "Function_17_2048",        # 11, 17
        "Function_18_20A4",        # 12, 18
        "Function_19_2111",        # 13, 19
        "Function_20_2169",        # 14, 20
        "Function_21_21D6",        # 15, 21
        "Function_22_2306",        # 16, 22
        "Function_23_2373",        # 17, 23
        "Function_24_23D4",        # 18, 24
        "Function_25_250E",        # 19, 25
        "Function_26_270C",        # 1A, 26
        "Function_27_2774",        # 1B, 27
        "Function_28_2782",        # 1C, 28
        "Function_29_34E3",        # 1D, 29
        "Function_30_3544",        # 1E, 30
        "Function_31_35FB",        # 1F, 31
        "Function_32_39FD",        # 20, 32
        "Function_33_4B65",        # 21, 33
        "Function_34_54B1",        # 22, 34
        "Function_35_607E",        # 23, 35
        "Function_36_6C6F",        # 24, 36
        "Function_37_7844",        # 25, 37
        "Function_38_78B3",        # 26, 38
        "Function_39_7941",        # 27, 39
        "Function_40_79D7",        # 28, 40
        "Function_41_7A6D",        # 29, 41
        "Function_42_7AC4",        # 2A, 42
        "Function_43_7B1B",        # 2B, 43
        "Function_44_7B6D",        # 2C, 44
        "Function_45_7B8C",        # 2D, 45
        "Function_46_7BAB",        # 2E, 46
        "Function_47_7BCA",        # 2F, 47
        "Function_48_7BE9",        # 30, 48
        "Function_49_7C08",        # 31, 49
        "Function_50_7C53",        # 32, 50
        "Function_51_7C7B",        # 33, 51
        "Function_52_7F59",        # 34, 52
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x100, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_136F")
    Sound(14, 0, 100, 0)
    OP_71(0x2, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1F5, 1)"), scpexpr(EXPR_END)), "loc_1301")
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
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x100, 0)
    OP_DE(0x6, 0x0)
    Jump("loc_136A")

    label("loc_1301")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0002
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, 0x1F5),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多,",
            scpstr(SCPSTR_CODE_ITEM, 0x1F5),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x2, 0x1E, 0x0, 0x0, 0x0)

    label("loc_136A")

    Jump("loc_13AC")

    label("loc_136F")

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

    label("loc_13AC")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_1282 end

    def Function_4_13B8(): pass

    label("Function_4_13B8")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x100, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14A5")
    Sound(14, 0, 100, 0)
    OP_71(0x3, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x5DF, 1)"), scpexpr(EXPR_END)), "loc_1437")
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
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x100, 1)
    OP_DE(0x6, 0x0)
    Jump("loc_14A0")

    label("loc_1437")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0005
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, 0x5DF),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多,",
            scpstr(SCPSTR_CODE_ITEM, 0x5DF),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x3, 0x1E, 0x0, 0x0, 0x0)

    label("loc_14A0")

    Jump("loc_14E2")

    label("loc_14A5")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0006
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

    label("loc_14E2")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_13B8 end

    def Function_5_14EE(): pass

    label("Function_5_14EE")

    TalkBegin(0xFF)
    Call(1, 0)
    ClearScenarioFlags(0x7A, 0)
    OP_65(0x3, 0x1)
    StopEffect(0x9, 0x2)
    TalkEnd(0xFF)
    Return()

    # Function_5_14EE end

    def Function_6_1502(): pass

    label("Function_6_1502")

    EventBegin(0x1)
    SetMapFlags(0x8000000)

    #A0007
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "有一个巴士车站。\x01",
            "要乘坐巴士吗？\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "阿尔摩利卡村\x01",          # 0
            "唐古拉姆门\x01",            # 1
            "停靠站（三岔路）\x01",      # 2
            "放弃\x01",                  # 3
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1594")
    Call(0, 7)
    ClearMapFlags(0x8000000)
    NewScene("t0000", 0, 0, 0)
    IdleLoop()
    Jump("loc_15D9")

    label("loc_1594")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15B9")
    Call(0, 7)
    ClearMapFlags(0x8000000)
    NewScene("t2500", 0, 0, 0)
    IdleLoop()
    Jump("loc_15D9")

    label("loc_15B9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15D9")
    Call(0, 7)
    ClearMapFlags(0x8000000)
    NewScene("r0030", 0, 0, 0)
    IdleLoop()

    label("loc_15D9")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_6_1502 end

    def Function_7_15E1(): pass

    label("Function_7_15E1")

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

    def lambda_16B7():
        OP_98(0xFE, 0xFFFFC180, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_16B7)
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

    # Function_7_15E1 end

    def Function_8_16FD(): pass

    label("Function_8_16FD")

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

    # Function_8_16FD end

    def Function_9_1795(): pass

    label("Function_9_1795")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    Sound(1499, 255, 100, 0)    #voice#Noel
    Sleep(500)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_17AF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1D11")

    Menu(
        0,
        32,
        26,
        1,
        (
            "使用警备队车辆进行移动\x01",      # 0
            "在此处休息\x01",                  # 1
            "放弃\x01",                        # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1CAE")
    Sound(1500, 255, 100, 0)    #voice#Noel
    MenuCmd(0, 1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_183B")
    MenuCmd(1, 1, "★克洛斯贝尔·中央广场")
    MenuCmd(3, 1, 0x0)
    Jump("loc_1855")

    label("loc_183B")

    MenuCmd(1, 1, "　克洛斯贝尔·中央广场")

    label("loc_1855")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1885")
    MenuCmd(1, 1, "★克洛斯贝尔·东出口")
    MenuCmd(3, 1, 0x1)
    Jump("loc_189D")

    label("loc_1885")

    MenuCmd(1, 1, "　克洛斯贝尔·东出口")

    label("loc_189D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_18CD")
    MenuCmd(1, 1, "★克洛斯贝尔·西出口")
    MenuCmd(3, 1, 0x2)
    Jump("loc_18E5")

    label("loc_18CD")

    MenuCmd(1, 1, "　克洛斯贝尔·西出口")

    label("loc_18E5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1915")
    MenuCmd(1, 1, "★克洛斯贝尔·南出口")
    MenuCmd(3, 1, 0x3)
    Jump("loc_192D")

    label("loc_1915")

    MenuCmd(1, 1, "　克洛斯贝尔·南出口")

    label("loc_192D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_195D")
    MenuCmd(1, 1, "★克洛斯贝尔·北出口")
    MenuCmd(3, 1, 0x4)
    Jump("loc_1975")

    label("loc_195D")

    MenuCmd(1, 1, "　克洛斯贝尔·北出口")

    label("loc_1975")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_199D")
    MenuCmd(1, 1, "★唐古拉姆门")
    MenuCmd(3, 1, 0x5)
    Jump("loc_19AD")

    label("loc_199D")

    MenuCmd(1, 1, "　唐古拉姆门")

    label("loc_19AD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_19D5")
    MenuCmd(1, 1, "★贝尔加德门")
    MenuCmd(3, 1, 0x6)
    Jump("loc_19E5")

    label("loc_19D5")

    MenuCmd(1, 1, "　贝尔加德门")

    label("loc_19E5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A13")
    MenuCmd(1, 1, "★乌尔斯拉医科大学")
    MenuCmd(3, 1, 0x7)
    Jump("loc_1A29")

    label("loc_1A13")

    MenuCmd(1, 1, "　乌尔斯拉医科大学")

    label("loc_1A29")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A53")
    MenuCmd(1, 1, "★阿尔摩利卡村")
    MenuCmd(3, 1, 0x8)
    Jump("loc_1A65")

    label("loc_1A53")

    MenuCmd(1, 1, "　阿尔摩利卡村")

    label("loc_1A65")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A8F")
    MenuCmd(1, 1, "★矿山镇玛因兹")
    MenuCmd(3, 1, 0x9)
    Jump("loc_1AA1")

    label("loc_1A8F")

    MenuCmd(1, 1, "　矿山镇玛因兹")

    label("loc_1AA1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1AD1")
    MenuCmd(1, 1, "★玛因兹山道·隧道内")
    MenuCmd(3, 1, 0xA)
    Jump("loc_1AE9")

    label("loc_1AD1")

    MenuCmd(1, 1, "　玛因兹山道·隧道内")

    label("loc_1AE9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B0F")
    MenuCmd(1, 1, "★星见之塔")
    MenuCmd(3, 1, 0xB)
    Jump("loc_1B1D")

    label("loc_1B0F")

    MenuCmd(1, 1, "　星见之塔")

    label("loc_1B1D")

    MenuCmd(1, 1, "　放弃")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuCmd(2, 1, 240, 16, 1)
    MenuEnd(0x0)
    OP_60(0x1)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1C9F")
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
        (0, "loc_1BF2"),
        (1, "loc_1C00"),
        (2, "loc_1C0E"),
        (3, "loc_1C1C"),
        (4, "loc_1C2A"),
        (5, "loc_1C38"),
        (6, "loc_1C46"),
        (7, "loc_1C54"),
        (8, "loc_1C62"),
        (9, "loc_1C70"),
        (10, "loc_1C7E"),
        (11, "loc_1C8C"),
        (SWITCH_DEFAULT, "loc_1C9A"),
    )


    label("loc_1BF2")

    NewScene("c0100", 0, 0, 0)
    IdleLoop()
    Jump("loc_1C9A")

    label("loc_1C00")

    NewScene("r0000", 0, 0, 0)
    IdleLoop()
    Jump("loc_1C9A")

    label("loc_1C0E")

    NewScene("r1000", 0, 0, 0)
    IdleLoop()
    Jump("loc_1C9A")

    label("loc_1C1C")

    NewScene("r1500", 0, 0, 0)
    IdleLoop()
    Jump("loc_1C9A")

    label("loc_1C2A")

    NewScene("r2000", 0, 0, 0)
    IdleLoop()
    Jump("loc_1C9A")

    label("loc_1C38")

    NewScene("t2500", 0, 0, 0)
    IdleLoop()
    Jump("loc_1C9A")

    label("loc_1C46")

    NewScene("t2000", 0, 0, 0)
    IdleLoop()
    Jump("loc_1C9A")

    label("loc_1C54")

    NewScene("t1500", 0, 0, 0)
    IdleLoop()
    Jump("loc_1C9A")

    label("loc_1C62")

    NewScene("t0000", 0, 0, 0)
    IdleLoop()
    Jump("loc_1C9A")

    label("loc_1C70")

    NewScene("t0500", 0, 0, 0)
    IdleLoop()
    Jump("loc_1C9A")

    label("loc_1C7E")

    NewScene("r2050", 0, 0, 0)
    IdleLoop()
    Jump("loc_1C9A")

    label("loc_1C8C")

    NewScene("m1000", 0, 0, 0)
    IdleLoop()
    Jump("loc_1C9A")

    label("loc_1C9A")

    Jump("loc_1CA9")

    label("loc_1C9F")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1CA9")

    Jump("loc_1D0C")

    label("loc_1CAE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1CF9")
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
    Jump("loc_1D0C")

    label("loc_1CF9")

    OP_60(0x0)
    OP_57(0x0)
    Sleep(500)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1D0C")

    Jump("loc_17AF")

    label("loc_1D11")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_9_1795 end

    def Function_10_1D19(): pass

    label("Function_10_1D19")

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
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1DED")
    Sound(1502, 255, 100, 0)    #voice#Noel
    Jump("loc_1DF3")

    label("loc_1DED")

    Sound(1503, 255, 100, 0)    #voice#Noel

    label("loc_1DF3")

    Sleep(500)
    FadeToBright(500, 0)
    OP_0D()
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_10_1D19 end

    def Function_11_1E08(): pass

    label("Function_11_1E08")

    TalkBegin(0xFE)

    #C0008
    ChrTalk(
        0x8,
        (
            "可恶～还是\x01",
            "被发现了吗……\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x8,
        (
            "还以为在纪念庆典期间\x01",
            "就不会有事呢……！\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_11_1E08 end

    def Function_12_1E5B(): pass

    label("Function_12_1E5B")

    TalkBegin(0xFE)

    #C0010
    ChrTalk(
        0x9,
        (
            "嗯，您就是用一封申请书\x01",
            "停了两辆车的先生吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x9,
        (
            "来，请在这里签名……\x01",
            "并交纳罚金～\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_12_1E5B end

    def Function_13_1EBA(): pass

    label("Function_13_1EBA")

    TalkBegin(0xFF)
    SetChrName("")

    #A0012
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "似乎是乌尔努公司制造的高级车。\x02\x03",

            "车牌号码是『ＶＥ　４３１０』。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0xBE, 1)
    Call(0, 24)
    TalkEnd(0xFF)
    Return()

    # Function_13_1EBA end

    def Function_14_1F12(): pass

    label("Function_14_1F12")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x17, 0x1, 0xA)"), scpexpr(EXPR_END)), "loc_1F51")
    SetChrName("")

    #A0013
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "车上贴着违章停车的\x01",
            "警告标志。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_1F7B")

    label("loc_1F51")

    Call(0, 23)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F7B")
    Sleep(300)
    Sound(959, 0, 100, 0)
    SetMapObjFrame(0x6, "chukin", 0x1, 0x1)
    OP_29(0x17, 0x1, 0xA)

    label("loc_1F7B")

    TalkEnd(0xFF)
    Return()

    # Function_14_1F12 end

    def Function_15_1F7F(): pass

    label("Function_15_1F7F")

    TalkBegin(0xFF)
    SetChrName("")

    #A0014
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "似乎是乌尔努公司制造的导力搬运车。\x02\x03",

            "车牌号码是『ＥＳ　４５２１』。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0xBE, 2)
    Call(0, 24)
    TalkEnd(0xFF)
    Return()

    # Function_15_1F7F end

    def Function_16_1FDB(): pass

    label("Function_16_1FDB")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x17, 0x1, 0xC)"), scpexpr(EXPR_END)), "loc_201A")
    SetChrName("")

    #A0015
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "车上贴着违章停车的\x01",
            "警告标志。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_2044")

    label("loc_201A")

    Call(0, 23)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2044")
    Sleep(300)
    Sound(959, 0, 100, 0)
    SetMapObjFrame(0x7, "chukin", 0x1, 0x1)
    OP_29(0x17, 0x1, 0xC)

    label("loc_2044")

    TalkEnd(0xFF)
    Return()

    # Function_16_1FDB end

    def Function_17_2048(): pass

    label("Function_17_2048")

    TalkBegin(0xFF)
    SetChrName("")

    #A0016
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "似乎是乌尔努公司制造的导力搬运车。\x02\x03",

            "车牌号码是『ＬＡ　５８２８』。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0xBE, 3)
    Call(0, 24)
    TalkEnd(0xFF)
    Return()

    # Function_17_2048 end

    def Function_18_20A4(): pass

    label("Function_18_20A4")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x17, 0x1, 0xE)"), scpexpr(EXPR_END)), "loc_20E3")
    SetChrName("")

    #A0017
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "车上贴着违章停车的\x01",
            "警告标志。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_210D")

    label("loc_20E3")

    Call(0, 23)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_210D")
    Sleep(300)
    Sound(959, 0, 100, 0)
    SetMapObjFrame(0x8, "chukin", 0x1, 0x1)
    OP_29(0x17, 0x1, 0xE)

    label("loc_210D")

    TalkEnd(0xFF)
    Return()

    # Function_18_20A4 end

    def Function_19_2111(): pass

    label("Function_19_2111")

    TalkBegin(0xFF)
    SetChrName("")

    #A0018
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "似乎是乌尔努公司制造的家用车。\x02\x03",

            "车牌号码是『ＣＷ　６４２２』。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0xBE, 4)
    Call(0, 24)
    TalkEnd(0xFF)
    Return()

    # Function_19_2111 end

    def Function_20_2169(): pass

    label("Function_20_2169")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x17, 0x1, 0x10)"), scpexpr(EXPR_END)), "loc_21A8")
    SetChrName("")

    #A0019
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "车上贴着违章停车的\x01",
            "警告标志。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_21D2")

    label("loc_21A8")

    Call(0, 23)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_21D2")
    Sleep(300)
    Sound(959, 0, 100, 0)
    SetMapObjFrame(0x9, "chukin", 0x1, 0x1)
    OP_29(0x17, 0x1, 0x10)

    label("loc_21D2")

    TalkEnd(0xFF)
    Return()

    # Function_20_2169 end

    def Function_21_21D6(): pass

    label("Function_21_21D6")

    TalkBegin(0xFF)
    SetChrName("")

    #A0020
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "似乎是莱恩福尔特公司制造的高级车。\x02\x03",

            "车牌号码是『ＣＬ　１１０１』。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x17, 0x1, 0x14)"), scpexpr(EXPR_END)), "loc_2275")

    #C0021
    ChrTalk(
        0x101,
        (
            "#0001F（记得这个车牌号码\x01",
            "  在西出口那边也出现过……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_22FC")

    label("loc_2275")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x17, 0x1, 0x13)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBC, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_228E")
    Call(0, 25)
    Jump("loc_22FC")

    label("loc_228E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x17, 0x1, 0x13)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBC, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_22EF")

    #C0022
    ChrTalk(
        0x101,
        (
            "#0005F（咦…………？）\x02\x03",

            "#0003F（这个号码，好像在哪里\x01",
            "  看到过呢……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_22FC")

    label("loc_22EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBC, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22FC")
    SetScenarioFlags(0xBC, 5)

    label("loc_22FC")

    SetScenarioFlags(0xBE, 5)
    Call(0, 24)
    TalkEnd(0xFF)
    Return()

    # Function_21_21D6 end

    def Function_22_2306(): pass

    label("Function_22_2306")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x17, 0x1, 0x12)"), scpexpr(EXPR_END)), "loc_2345")
    SetChrName("")

    #A0023
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "车上贴着违章停车的\x01",
            "警告标志。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_236F")

    label("loc_2345")

    Call(0, 23)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_236F")
    Sleep(300)
    Sound(959, 0, 100, 0)
    SetMapObjFrame(0xA, "chukin", 0x1, 0x1)
    OP_29(0x17, 0x1, 0x12)

    label("loc_236F")

    TalkEnd(0xFF)
    Return()

    # Function_22_2306 end

    def Function_23_2373(): pass

    label("Function_23_2373")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 16, -1, -1)
    SetChrName("")

    #A0024
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "要贴警告标志吗？",
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
            "【贴】\x01",        # 0
            "【不贴】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    Return()

    # Function_23_2373 end

    def Function_24_23D4(): pass

    label("Function_24_23D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBD, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBD, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBD, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBE, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBE, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBE, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBE, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBE, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBE, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x17, 0x1, 0x13)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_250D")

    #C0025
    ChrTalk(
        0x101,
        (
            "#0000F好……这样一来，\x01",
            "所有车辆的号码\x01",
            "都检查过了吧。\x02\x03",

            "把剩下的标志贴完，\x01",
            "就回去报告吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x104,
        "#0300F好，就这样吧。\x02",
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x102,
        (
            "#0100F反正也不急，\x01",
            "回去之前还是\x01",
            "确认一遍比较好吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x103,
        (
            "#0200F但就算贴错了，\x01",
            "也没法再撕掉……\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x101,
        (
            "#0000F哈哈……\x01",
            "我想应该没问题吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x17, 0x1, 0x13)

    label("loc_250D")

    Return()

    # Function_24_23D4 end

    def Function_25_250E(): pass

    label("Function_25_250E")

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

            "#0001F这个号码……\x01",
            "在西出口好像也出现过吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x102,
        (
            "#11P#0105F这么说来……\x01",
            "似乎还真的有印象呢。\x02\x03",

            "#0100F但那边的好像\x01",
            "并不是家用车。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x103,
        (
            "#5P#0200F牌号相同的车辆，\x01",
            "本来应该不可能出现的……\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x104,
        (
            "#5P#0303F唔……这是个得到过许可\x01",
            "的车号啊。\x02\x03",

            "#0300F嗯，姑且还是记下来\x01",
            "为好吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x101,
        (
            "#12P#0000F也是……\x01",
            "稍后再向公共安全科\x01",
            "的人汇报吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_E0(0x0)
    SetChrPos(0x0, 31050, 0, -4940, 270)
    OP_29(0x17, 0x1, 0x14)
    EventEnd(0x5)
    Return()

    # Function_25_250E end

    def Function_26_270C(): pass

    label("Function_26_270C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_271D")
    Call(0, 6)
    Jump("loc_2773")

    label("loc_271D")

    TalkBegin(0xFF)
    SetChrName("")

    #A0035
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "有一个巴士停靠站。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0036
    ChrTalk(
        0x101,
        (
            "#0006F……还是努力\x01",
            "步行去阿尔摩利卡村吧。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFF)

    label("loc_2773")

    Return()

    # Function_26_270C end

    def Function_27_2774(): pass

    label("Function_27_2774")

    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 9)
    Return()

    # Function_27_2774 end

    def Function_28_2782(): pass

    label("Function_28_2782")

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

    def lambda_2862():
        OP_97(0xFE, 0x7D0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2862)

    def lambda_287C():
        OP_97(0xFE, 0x7D0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_287C)

    def lambda_2896():
        OP_97(0xFE, 0x7D0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2896)

    def lambda_28B0():
        OP_97(0xFE, 0x7D0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_28B0)
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
        "#0011F糟了……！\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x19, 1, 0, 29)
    OP_71(0x0, 0x3C, 0x5A, 0x0, 0x0)
    OP_79(0x0)
    OP_71(0x0, 0xB4, 0x79, 0x0, 0x20)

    def lambda_29A6():
        OP_98(0xFE, 0x3E8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_29A6)
    WaitChrThread(0xA, 1)
    Sleep(100)
    OP_68(15320, 1000, 0, 4000)
    OP_71(0x0, 0x79, 0xB4, 0x0, 0x20)

    def lambda_29E4():
        OP_9E(0xFE, 0x4268, 0x7D0, 0xFFFD40E0, 0xBB8, 0x1)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_29E4)
    WaitChrThread(0xA, 1)
    OP_71(0x0, 0x3C, 0x5A, 0x0, 0x0)
    OP_79(0x0)
    OP_71(0x0, 0x79, 0xB4, 0x0, 0x20)

    def lambda_2A1E():
        OP_98(0xFE, 0x4E20, 0x0, 0x0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_2A1E)
    WaitChrThread(0xA, 1)
    SetMapObjFlags(0x0, 0x4)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    OP_6F(0x1)
    OP_68(3200, 800, 0, 2000)

    def lambda_2A5F():
        OP_97(0xFE, 0x1B58, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2A5F)
    Sleep(50)

    def lambda_2A7C():
        OP_97(0xFE, 0x1B58, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2A7C)
    Sleep(50)

    def lambda_2A99():
        OP_97(0xFE, 0x1B58, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2A99)
    Sleep(50)

    def lambda_2AB6():
        OP_97(0xFE, 0x1B58, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2AB6)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    OP_6F(0x1)
    Sleep(500)

    #C0038
    ChrTalk(
        0x102,
        "#0106F#6P走掉了……\x02",
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x104,
        "#0306F#5P喂喂，不是吧。\x02",
    )

    CloseMessageWindow()
    OP_93(0x104, 0xB4, 0x1F4)
    Sleep(300)

    #C0040
    ChrTalk(
        0x104,
        (
            "#0308F#5P导力巴士\x01",
            "有多少班啊？\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x0, 0x1F4)
    Sleep(300)

    #C0041
    ChrTalk(
        0x101,
        (
            "#0006F#12P嗯，这个～……\x01",
            "应该还挺多的。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0x103, 0x0, 0x1F4)
    Sleep(500)

    def lambda_2B9F():

        label("loc_2B9F")

        TurnDirection(0x101, 0x103, 500)
        Yield()
        Jump("loc_2B9F")

    QueueWorkItem2(0x101, 1, lambda_2B9F)

    def lambda_2BB1():

        label("loc_2BB1")

        TurnDirection(0x102, 0x103, 500)
        Yield()
        Jump("loc_2BB1")

    QueueWorkItem2(0x102, 1, lambda_2BB1)

    def lambda_2BC3():

        label("loc_2BC3")

        TurnDirection(0x104, 0x103, 500)
        Yield()
        Jump("loc_2BC3")

    QueueWorkItem2(0x104, 1, lambda_2BC3)
    OP_68(1810, 800, 2340, 2000)

    def lambda_2BE6():
        OP_95(0xFE, 610, 0, 3820, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2BE6)
    WaitChrThread(0x103, 1)
    OP_6F(0x1)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x104, 0x1)

    #C0042
    ChrTalk(
        0x103,
        (
            "#0203F#6P根据时刻表……\x02\x03",

            "#0200F下一班车\x01",
            "好像是两小时后来呢。\x02",
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
        "#0105F#6P那、那么久……？\x02",
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x104,
        (
            "#0306F#11P这么说，一天内也只有\x01",
            "区区几班啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x101,
        (
            "#0006F#12P……伤脑筋呢。\x01",
            "本想在今天至少去一趟医院的，\x01",
            "这样也许就来不及了。\x02\x03",

            "#0008F可是，改变原定计划，\x01",
            "先去医院似乎也不太好……\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x102,
        (
            "#0106F#6P是呀……\x01",
            "我们刚刚才决定了调查方针呢。\x02",
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
            "#0200F#5P──既然如此，\x01",
            "走过去不就好了？\x02",
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
        "#0005F#12P哎……\x02",
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x102,
        "#0105F#6P缇欧……？\x02",
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x104,
        "#0305F#2P喂喂……真的假的？\x02",
    )

    CloseMessageWindow()
    OP_68(1980, 800, 790, 1500)

    def lambda_2E9A():

        label("loc_2E9A")

        TurnDirection(0x101, 0x103, 500)
        Yield()
        Jump("loc_2E9A")

    QueueWorkItem2(0x101, 1, lambda_2E9A)

    def lambda_2EAC():

        label("loc_2EAC")

        TurnDirection(0x102, 0x103, 500)
        Yield()
        Jump("loc_2EAC")

    QueueWorkItem2(0x102, 1, lambda_2EAC)

    def lambda_2EBE():

        label("loc_2EBE")

        TurnDirection(0x104, 0x103, 500)
        Yield()
        Jump("loc_2EBE")

    QueueWorkItem2(0x104, 1, lambda_2EBE)

    def lambda_2ED0():
        OP_95(0xFE, 500, 0, 700, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2ED0)
    WaitChrThread(0x103, 1)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x104, 0x1)

    #C0051
    ChrTalk(
        0x103,
        (
            "#0204F#5P从地图上来看，\x01",
            "从这里到阿尔摩利卡村\x01",
            "步行大约需要一个半小时。\x02\x03",

            "#0202F如果乘坐下一班巴士去，\x01",
            "加上等车时间，\x01",
            "应该要两个半小时。\x02\x03",

            "相比之下，步行的话\x01",
            "不是更有效率吗……？\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x102,
        (
            "#0100F#6P原来如此……计算起来确实是这样呢。\x02\x03",

            "#0104F我听说，在阿尔摩利卡村前，\x01",
            "有一条满眼田园风光的\x01",
            "石板路……\x02\x03",

            "#0102F就当是一次远足，\x01",
            "说不定也很惬意呢。\x02",
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
            "#0306F#5P（喂喂，小姐们\x01",
            "   竟然敢这样说啊……）\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x101,
        (
            "#0006F#11P（不管怎么想，明显也都是\x01",
            "  从没在郊外长途跋涉过呢……）\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    def lambda_3116():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3116)
    Sleep(50)

    def lambda_3126():
        OP_93(0xFE, 0x5A, 0x12C)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_3126)
    WaitChrThread(0x102, 1)

    #C0055
    ChrTalk(
        0x102,
        "#0105F#6P你们两个怎么了？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)

    #C0056
    ChrTalk(
        0x101,
        (
            "#0012F#11P不，没什么～……\x02\x03",

            "#0001F那个，郊外还有魔兽徘徊，\x01",
            "你们两个没问题吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x102,
        (
            "#0106F#6P嗯～……这么说来，魔兽也是个问题呢。\x02\x03",

            "#0100F不过，我们之前也潜入过\x01",
            "地下空间好几次了，应该没问题。\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x103,
        (
            "#0203F#6P而且我也需要\x01",
            "测试魔导杖。\x02\x03",

            "#0200F适当的实战\x01",
            "正是求之不得的……\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x101,
        (
            "#0006F#11P嗯～……\x02\x03",

            "#0000F──好吧。\x01",
            "既然你们都这么说了，那就走过去吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x102,
        "#0100F#6P嗯，走吧。\x02",
    )

    CloseMessageWindow()
    StopBGM(0x5DC)

    def lambda_32D8():
        OP_93(0xFE, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_32D8)
    Sleep(100)

    def lambda_32E8():
        OP_93(0xFE, 0xB4, 0x190)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_32E8)
    Sleep(500)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7204", 0)
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0xCC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0061
    ChrTalk(
        0x102,
        (
            "#0109F#12P呵呵，真有点期待呢。\x02\x03",

            "#0102F早知道这样的话，\x01",
            "事先做个便当带来就好了。\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)

    #C0062
    ChrTalk(
        0x103,
        (
            "#0204F#5P……的确。\x02\x03",

            "#0202F不过，中午之前\x01",
            "应该能到达村子，\x01",
            "午饭就在那边吃好了。\x02",
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
            "#0008F#11P（……她们两个要是\x01",
            "　累了的话，就由我们负责支援吧。）\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x104,
        "#0302F#5P（是是，明白。）\x02",
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

    # Function_28_2782 end

    def Function_29_34E3(): pass

    label("Function_29_34E3")

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

    # Function_29_34E3 end

    def Function_30_3544(): pass

    label("Function_30_3544")

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
            "调查停靠站的告示牌后，\x01",
            "就能乘坐导力巴士。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #A0066
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "进而便可迅速移动至所选目的地，\x01",
            "以更高的效率来往于各处。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x93, 7)
    EventEnd(0x5)
    Return()

    # Function_30_3544 end

    def Function_31_35FB(): pass

    label("Function_31_35FB")

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
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x1, 0xE)"), scpexpr(EXPR_END)), "loc_390E")
    Call(0, 36)
    OP_29(0x1B, 0x1, 0x14)
    Jump("loc_3975")

    label("loc_390E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x1, 0xF)"), scpexpr(EXPR_END)), "loc_3929")
    Call(0, 32)
    OP_29(0x1B, 0x1, 0x13)
    Jump("loc_3975")

    label("loc_3929")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x1, 0x10)"), scpexpr(EXPR_END)), "loc_3944")
    Call(0, 33)
    OP_29(0x1B, 0x1, 0x14)
    Jump("loc_3975")

    label("loc_3944")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x1, 0x11)"), scpexpr(EXPR_END)), "loc_395F")
    Call(0, 35)
    OP_29(0x1B, 0x1, 0x14)
    Jump("loc_3975")

    label("loc_395F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x1, 0x12)"), scpexpr(EXPR_END)), "loc_3975")
    Call(0, 34)
    OP_29(0x1B, 0x1, 0x14)

    label("loc_3975")

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

    # Function_31_35FB end

    def Function_32_39FD(): pass

    label("Function_32_39FD")

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
            "#1P#0001F……请您\x01",
            "稍等一下好吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_3AF4():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_3AF4)
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
            "#5P哎呀哎呀，这不是刚才\x01",
            "在国境门那边聊过天的孩子们嘛。\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0xC,
        "#5P找我有什么事吗？\x02",
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x101,
        (
            "#6P#0003F抱歉，还没做自我介绍……\x02\x03",

            "#0001F我们是\x01",
            "克洛斯贝尔警察局·特别任务\x01",
            "支援科的成员。\x02\x03",

            "老婆婆，麻烦您……\x01",
            "跟我们走一趟吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0xC,
        (
            "#5P……哎，怎、怎么会……\x01",
            "我做了什么啊？\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0xC,
        (
            "#5P再、再怎么说，\x01",
            "这也太过分了……\x01",
            "让我这样身体虚弱的老人家……\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0x101,
        (
            "#6P#0003F……今日，根据警察局的情报来源，\x01",
            "我们得知了这样一条消息。\x02\x03",

            "某个犯罪集团\x01",
            "企图潜入\x01",
            "克洛斯贝尔……\x02\x03",

            "#0001F我们接到任务，\x01",
            "其内容是赶往唐古拉姆门盯梢，\x01",
            "观察众游客。\x02\x03",

            "而其中有个人\x01",
            "说出了明显很可疑的话……\x01",
            "没错，那就是您。\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0xC,
        "#5P什、什么意思……？\x02",
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0x101,
        (
            "#6P#0001F老婆婆，您在\x01",
            "唐古拉姆门的食堂\x01",
            "说了很奇怪的话。\x02\x03",

            "#0003F『三年没来克洛斯贝尔了』……\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0xC,
        "#5P……那、那有什么问题？\x02",
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0xC,
        (
            "#5P住在共和国那么远的地方，\x01",
            "三年没来也\x01",
            "没什么好奇怪的……\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0x101,
        (
            "#6P#0003F……问题还在后面。\x02\x03",

            "#0001F『之前来的时候，带孙子去\x01",
            "  米修拉姆的主题公园玩过』……\x02",
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
        "#12P#0104F……对，就是这样。\x02",
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0x104,
        (
            "#12P#0300F原来如此，我明白了。\x01",
            "这话的确是充满疑点呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0x103,
        "#12P#0200F您自掘坟墓了呢，老婆婆。\x02",
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0xC,
        (
            "#5P哎？呃，那个……\x01",
            "我不太懂你们的意思……\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x101,
        (
            "#6P#0003F很简单。\x02\x03",

            "您说自己最后一次到访\x01",
            "克洛斯贝尔是在三年前……\x02\x03",

            "#0001F但米修拉姆疗养地的\x01",
            "主题公园在那时\x01",
            "还没有建成呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0xC,
        (
            "#5P……哎！？\x01",
            "这、这不可能……\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0xC,
        (
            "#5P……不……\x01",
            "呃，那是，那个……\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0xC,
        "#5P……对，是我弄错了！\x02",
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0xC,
        (
            "#5P呵呵，我可真是的，\x01",
            "把在别处看到的主题公园的报道\x01",
            "错当成了自己的回忆……\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0x101,
        (
            "#6P#0003F原来如此……是弄错了吗。\x02\x03",

            "#0000F那么……\x01",
            "能麻烦您把令郎夫妇\x01",
            "叫来吗？\x02\x03",

            "只要联络警察的话，\x01",
            "应该马上就能把他们找来了。\x02",
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
            "#6P#0000F……办不到吧，\x01",
            "因为那些人物根本就不存在。\x02\x03",

            "#0003F真是不可思议。\x01",
            "在不存在的主题公园里，\x01",
            "和不存在的孙子游玩……\x02\x03",

            "您并不是三年没来，\x01",
            "而正是因为定期到访克洛斯贝尔，\x01",
            "所以才会弄错的吧。\x02\x03",

            "#0001F没错，正是为了非法行商，\x01",
            "定期到访克洛斯贝尔，所以才会如此。\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0xC,
        (
            "#5P我、我、我……\x01",
            "我不知道你在说什么！\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0xC,
        (
            "#5P什么贩卖假冒的名牌商品……\x01",
            "那种过分的事我才不会……\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x102,
        (
            "#12P#0101F……老婆婆，我们\x01",
            "的确是在追查\x01",
            "假货商……\x02\x03",

            "但是这件事好像\x01",
            "一次也没对您说过啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0094
    ChrTalk(
        0xC,
        "#5P啊、啊、啊……\x02",
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0x104,
        (
            "#12P#0309F哈哈，这么老套的陷阱\x01",
            "也能让您上钩啊，老婆婆。\x02\x03",

            "#0300F该到算总账的时候啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0x103,
        (
            "#12P#0200F您为什么会说出\x01",
            "本不可能知道的信息……\x02\x03",

            "请到警察局总部\x01",
            "的笔录室中慢慢解释吧。\x02",
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
            "#6P#0003F（这样就解决了吧……）\x02\x03",

            "#0001F……老婆婆，\x01",
            "我再说一遍，\x01",
            "请跟我们到警察局总部走一趟……\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0xC,
        (
            "#5P#200W……谁#200W……………………\x01",
            "…………#200W…………谁……\x02",
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
        "假货商",
        (
            "#5P#5S……谁要跟你们走啊，\x01",
            "这群臭小鬼！！！\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0x101,
        "#6P#0011F哎！！？\x02",
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x102,
        "#12P#0105F呀！！\x02",
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0x104,
        "#12P#0305F怎、怎么回事……！？\x02",
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0x103,
        "#12P#0200F……原形毕露了呢。\x02",
    )

    CloseMessageWindow()
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    #N0105
    NpcTalk(
        0xC,
        "假货商",
        (
            "#5P#5S竟敢搞这种引人上钩的\x01",
            "骗子把戏！\x02",
        )
    )

    CloseMessageWindow()
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    #N0106
    NpcTalk(
        0xC,
        "假货商",
        (
            "#5P#5S你们做这种缺德事，\x01",
            "总有一天会遭到女神的天谴啊！\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0x103,
        (
            "#12P#0203F……竟然说出这种\x01",
            "恬不知耻的话。\x02\x03",

            "#0201F做着骗人买卖的\x01",
            "不正是您吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    #N0108
    NpcTalk(
        0xC,
        "假货商",
        "#5P#5S吵死了，你这个矮冬瓜！\x02",
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0x103,
        "#12P#0205F矮……矮冬瓜……！？\x02",
    )

    CloseMessageWindow()
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    #N0110
    NpcTalk(
        0xC,
        "假货商",
        (
            "#5P#5S啊啊～讨厌讨厌！所以说\x01",
            "我最讨厌警察、游击士这群人了！\x02",
        )
    )

    CloseMessageWindow()
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    #N0111
    NpcTalk(
        0xC,
        "假货商",
        (
            "#5P#5S你们以为自己永远\x01",
            "都是正确的吗，呆瓜们！\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0x101,
        (
            "#6P#0011F总、总而言之，请您先镇定一点！\x01",
            "只要老老实实跟我们走……\x02",
        )
    )

    CloseMessageWindow()
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    #N0113
    NpcTalk(
        0xC,
        "假货商",
        (
            "#5P#5S闭嘴，小子！\x01",
            "我都说过不去了！\x02",
        )
    )

    CloseMessageWindow()
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    #N0114
    NpcTalk(
        0xC,
        "假货商",
        (
            "#5P#5S同样的话，\x01",
            "不要让我重复很多遍！\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0x101,
        (
            "#6P#0006F（同样的话，\x01",
            "  您也不要让我重复很多遍啊……！）\x02",
        )
    )

    CloseMessageWindow()

    #N0116
    NpcTalk(
        0xC,
        "假货商",
        (
            "#5P要是你有本事\x01",
            "抓到我的话……\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0x7D0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_490E():
        OP_98(0xFE, 0xFFFFFE0C, 0x0, 0xFFFFFE0C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_490E)
    Sleep(1000)

    def lambda_492B():
        OP_98(0xFE, 0xFFFFFE0C, 0x0, 0x1F4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_492B)
    Sleep(1000)
    Sleep(10)
    PlayBGM("ed7401", 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x191), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetCameraDistance(21000, 3000)

    def lambda_4961():
        OP_95(0xFE, -22570, 0, 2200, 10000, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_4961)
    Sound(250, 0, 80, 0)
    OP_82(0x0, 0x64, 0xBB8, 0xC8)
    SetMessageWindowPos(-50, 20, -1, -1)
    SetChrName("假货商")

    #A0117
    AnonymousTalk(
        0xC,
        "#5P#5S就来抓抓看啊！！！\x02",
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
            "#6P#0005F……不、不是吧……\x01",
            "这是什么速度啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0x104,
        (
            "#12P#0306F我说～之前那副\x01",
            "慈祥优雅的老婆婆的面具\x01",
            "都扔到哪里去了啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0x103,
        "#12P#0206F矮冬瓜……\x02",
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0x102,
        (
            "#12P#0103F好、好啦！你们还有空发呆！？\x02\x03",

            "#0101F再不赶快追上去……\x01",
            "就真要被她逃掉了啊！\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0x101,
        (
            "#6P#0001F说、说得对啊……\x01",
            "赶快追吧，各位！\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x101, 3, 0, 48)
    BeginChrThread(0x102, 3, 0, 48)
    BeginChrThread(0x103, 3, 0, 48)
    BeginChrThread(0x104, 3, 0, 48)
    Return()

    # Function_32_39FD end

    def Function_33_4B65(): pass

    label("Function_33_4B65")

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
            "#1P#0001F……请您\x01",
            "稍等一下好吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_4C5C():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_4C5C)
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
        "#5P#3405F哎呀……找我有什么事吗？\x02",
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0x101,
        (
            "#6P#0000F抱歉，还没自我介绍……\x02\x03",

            "我们是\x01",
            "克洛斯贝尔警察局·特别任务支援科\x01",
            "的成员。\x02\x03",

            "麻烦您……\x01",
            "跟我们走一趟吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0xB,
        (
            "#5P#3403F……唔。\x02\x03",

            "刚才你们在巴士里说\x01",
            "假货贩子什么的……\x02\x03",

            "#3400F莫非以为是我吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0x101,
        (
            "#6P#0005F……哎？\x02\x03",

            "（听、听到了吗……？）\x02",
        )
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0xB,
        (
            "#5P#3403F……着眼点倒是不错。\x02\x03",

            "我没有对你们\x01",
            "透露任何有关自身的详情……\x01",
            "这的确可以作为怀疑的理由。\x02\x03",

            "#3401F但是……应该还有条\x01",
            "更重要，而且更明显的线索，\x01",
            "而你们却没有发现。\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0x101,
        "#6P#0005F明显的线索……？\x02",
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0xB,
        (
            "#5P#3403F我在食堂听到了\x01",
            "你们和乘客们的对话……\x01",
            "其中有个不自然的地方。\x02\x03",

            "#3401F那就是……那位看似慈祥的\x01",
            "老婆婆所说的话。\x02",
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
            "#12P#0105F快要见到阔别三年的孙子，\x01",
            "看起来非常开心的……\x01",
            "那位老婆婆吗！？\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0x101,
        (
            "#6P#0005F到底从何说起……？\x01",
            "那个人说的话里，没有什么可疑的地方啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0xB,
        (
            "#5P#3403F仔细想想她说过的话。\x02\x03",

            "『三年没来克洛斯贝尔了』……\x02\x03",

            "以及……\x01",
            "『之前来的时候，带孙子去\x01",
            "  米修拉姆的主题公园玩过』这两句话。\x02\x03",

            "#3402F如果你们是克洛斯贝尔的居民，\x01",
            "应该能发现其中的明显矛盾。\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0x101,
        (
            "#6P#0005F……啊……！！\x02\x03",

            "对了，原来如此啊……！\x02",
        )
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0x103,
        (
            "#12P#0200F……三年前的米修拉姆\x01",
            "还没有主题公园。\x02\x03",

            "她回忆中的地方\x01",
            "根本就不存在……\x02",
        )
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0x104,
        (
            "#12P#0301F……这么说，在场众人中，\x01",
            "说话最可疑的就是\x01",
            "那位老婆婆吗。\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0x102,
        (
            "#12P#0106F这么明显的破绽，\x01",
            "我们竟然没有注意到……\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0xB,
        (
            "#5P#3400F被她戴着的那副\x01",
            "『慈祥老婆婆』的面具\x01",
            "彻底欺骗了吧。\x02\x03",

            "她不是三年没来，\x01",
            "而正是因为定期到访克洛斯贝尔，\x01",
            "所以才会犯下这种失误……\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0x101,
        (
            "#6P#0003F身为假货贩子，\x01",
            "定期到访克洛斯贝尔……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5271():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5271)

    def lambda_527E():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_527E)

    def lambda_528B():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_528B)

    def lambda_5298():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_5298)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    #C0140
    ChrTalk(
        0x101,
        "#6P#0005F……那、那位老婆婆吗！？\x02",
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0x103,
        "#12P#0200F她现在恐怕已经到东街了。\x02",
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0x104,
        "#12P#0301F不赶快追上去的话，可能会跟丢啊。\x02",
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0x102,
        "#12P#0101F罗、罗伊德！\x02",
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0x101,
        "#6P#0001F啊……我明白！\x02",
    )

    CloseMessageWindow()

    def lambda_536D():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_536D)

    def lambda_537A():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_537A)

    def lambda_5387():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5387)

    def lambda_5394():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_5394)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    #C0145
    ChrTalk(
        0x101,
        (
            "#6P#0006F真、真是太对不起您了！\x01",
            "还有……非常感谢！\x02\x03",

            "#0001F稍后我们会再次向您谢罪的，\x01",
            "所以现在就先……！\x02",
        )
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0xB,
        (
            "#5P#3403F没关系的。\x02\x03",

            "你们现在可没有\x01",
            "慢慢道歉的空闲吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0x101,
        (
            "#6P#0005F啊……是！\x02\x03",

            "#0001F快追，各位！\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(21000, 3000)

    def lambda_5490():
        OP_93(0xFE, 0x10E, 0x64)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_5490)
    BeginChrThread(0x101, 3, 0, 49)
    BeginChrThread(0x102, 3, 0, 49)
    BeginChrThread(0x103, 3, 0, 49)
    BeginChrThread(0x104, 3, 0, 49)
    Return()

    # Function_33_4B65 end

    def Function_34_54B1(): pass

    label("Function_34_54B1")

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
            "#1P#0001F……请您\x01",
            "稍等一下好吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_55A8():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_55A8)
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
            "#5P哎呀，这不是刚才在\x01",
            "唐古拉姆门见过的几位嘛。\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0xE,
        "#5P找我有什么事吗？\x02",
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0x101,
        (
            "#6P#0001F抱歉，还没做自我介绍……\x02\x03",

            "我们是\x01",
            "克洛斯贝尔警察局·特别任务支援科\x01",
            "的成员。\x02\x03",

            "麻烦您……\x01",
            "跟我们走一趟吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0xE,
        "#5P……警、警察！？\x02",
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0xE,
        "#5P我、我到底做了什么……\x02",
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0x101,
        (
            "#6P#0003F……现在就告诉您我们的推理。\x02\x03",

            "#0001F您听好，首先……\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-50, 20, -1, -1)
    SetChrName("女性的声音")

    #A0155
    AnonymousTalk(
        0xB,
        "#1P──没有那个必要。\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(14, 280, 60, 3)

    #C0156
    ChrTalk(
        0x101,
        "#6P#0005F哎……？\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, -10500, 0, 2200, 90)

    def lambda_5783():
        OP_95(0xFE, -800, 0, 2200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_5783)

    def lambda_579D():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_579D)
    WaitChrThread(0xE, 1)
    Sleep(3800)

    def lambda_57B1():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_57B1)

    def lambda_57BE():
        OP_98(0xFE, 0x0, 0x0, 0x5DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_57BE)
    WaitChrThread(0xB, 1)

    #C0157
    ChrTalk(
        0x101,
        "#6P#0005F您、您是……\x02",
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0x104,
        (
            "#12P#0305F黑发的姐姐！？\x01",
            "你不是已经进入市里了吗……\x02",
        )
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0xB,
        (
            "#5P#3404F嗯，是啊。\x02\x03",

            "#3400F不过，看到你们叫住\x01",
            "这个人，就掉头回来了。\x02",
        )
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0x103,
        "#12P#0205F这是怎么回事？\x02",
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0xB,
        (
            "#5P#3401F我就直截了当地说吧。\x02\x03",

            "刚才你们在巴士里说的\x01",
            "假货贩子什么的……\x02\x03",

            "#3403F犯人并不是这个人。\x02",
        )
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0x101,
        (
            "#6P#0005F……哎？\x02\x03",

            "您……您说什么……！？\x02\x03",

            "（话说，巴士里的对话\x01",
            "  都被她听到了吗……？）\x02",
        )
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0xB,
        (
            "#5P#3403F……着眼点倒是不错。\x02\x03",

            "他的职业是贸易商……\x01",
            "很容易和假货贩子\x01",
            "这个词联系起来。\x02\x03",

            "#3401F但是……应该还有条\x01",
            "更重要，而且更明显的线索，\x01",
            "而你们却没有发现。\x02",
        )
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0x101,
        "#6P#0005F明显的线索……？\x02",
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0xB,
        (
            "#5P#3403F我在食堂听到了\x01",
            "你们和乘客们的对话……\x01",
            "其中有个不自然的地方。\x02\x03",

            "#3401F那就是……那位看似慈祥的\x01",
            "老婆婆所说的话。\x02",
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
            "#12P#0105F快要见到阔别三年的孙子，\x01",
            "看起来非常开心的……\x01",
            "那位老婆婆吗！？\x02",
        )
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0x101,
        (
            "#6P#0005F到底从何说起……？\x01",
            "那个人说的话里，没有什么可疑的地方啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0xB,
        (
            "#5P#3403F仔细想想她说的话。\x02\x03",

            "『三年没来克洛斯贝尔了』……\x02\x03",

            "以及……\x01",
            "『之前来的时候，带孙子去\x01",
            "  米修拉姆的主题公园玩过』这两句话。\x02\x03",

            "#3402F如果你们是克洛斯贝尔的居民，\x01",
            "应该能发现其中的明显矛盾。\x02",
        )
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0x101,
        (
            "#6P#0005F……啊……！！\x02\x03",

            "对了，原来如此啊……！\x02",
        )
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0x103,
        (
            "#12P#0200F……三年前的米修拉姆\x01",
            "还没有主题公园。\x02\x03",

            "她回忆中的地方\x01",
            "根本就不存在……\x02",
        )
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0x104,
        (
            "#12P#0301F……这么说，在场众人中，\x01",
            "说话最可疑的就是\x01",
            "那位婆婆吗。\x02",
        )
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0x102,
        (
            "#12P#0106F这么明显的破绽，\x01",
            "我们竟然没有注意到……\x02",
        )
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0xB,
        (
            "#5P#3400F被她戴着的那副\x01",
            "『慈祥老婆婆』的面具\x01",
            "彻底欺骗了吧。\x02\x03",

            "她不是三年没来，\x01",
            "而正是因为定期到访克洛斯贝尔，\x01",
            "所以才会犯下这种失误……\x02",
        )
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0x101,
        (
            "#6P#0003F身为假货贩子\x01",
            "定期到访克洛斯贝尔……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5E08():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5E08)

    def lambda_5E15():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5E15)

    def lambda_5E22():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5E22)

    def lambda_5E2F():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_5E2F)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    #C0175
    ChrTalk(
        0x101,
        "#6P#0005F……那、那位老婆婆吗！？\x02",
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0x103,
        "#12P#0200F她现在恐怕已经到东街了。\x02",
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0x104,
        "#12P#0301F不赶快追上去的话，可能会跟丢啊。\x02",
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0x102,
        "#12P#0101F罗、罗伊德！\x02",
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0x101,
        "#6P#0001F啊……我明白！\x02",
    )

    CloseMessageWindow()

    def lambda_5F04():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5F04)

    def lambda_5F11():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5F11)

    def lambda_5F1E():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5F1E)

    def lambda_5F2B():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_5F2B)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    #C0180
    ChrTalk(
        0x101,
        (
            "#6P#0006F真、真是太对不起您了！\x01",
            "我们太失礼了……\x02\x03",

            "稍后我们会再次向您谢罪的，\x01",
            "所以现在就先……！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5FAD():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_5FAD)
    WaitChrThread(0xE, 1)

    #C0181
    ChrTalk(
        0xE,
        (
            "#5P哦，哦。\x01",
            "我是完全一头雾水啦……\x02",
        )
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0xB,
        (
            "#5P#3403F……你们现在可没有\x01",
            "慢慢道歉的空闲吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0x101,
        (
            "#6P#0005F啊……是！\x02\x03",

            "#0001F快追，各位！\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(21000, 3000)

    def lambda_6050():
        OP_93(0xFE, 0x10E, 0x64)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_6050)

    def lambda_605D():
        OP_93(0xFE, 0x10E, 0x64)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_605D)
    BeginChrThread(0x101, 3, 0, 49)
    BeginChrThread(0x102, 3, 0, 49)
    BeginChrThread(0x103, 3, 0, 49)
    BeginChrThread(0x104, 3, 0, 49)
    Return()

    # Function_34_54B1 end

    def Function_35_607E(): pass

    label("Function_35_607E")

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
            "#1P#0001F……请您\x01",
            "稍等一下好吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xF, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_6175():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_6175)
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
        "#5P哎呀……是刚才的……\x02",
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0xF,
        "#5P找我有什么事吗？\x02",
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0x101,
        (
            "#6P#0001F抱歉，还没做自我介绍……\x02\x03",

            "我们是\x01",
            "克洛斯贝尔警察局·特别任务支援科\x01",
            "的成员。\x02\x03",

            "麻烦您……\x01",
            "跟我们走一趟吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0xF,
        "#5P……啊？\x02",
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0xF,
        (
            "#5P我到底做了什么啊？\x01",
            "梦话也要等睡着了以后再说吧！！\x02",
        )
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0x101,
        (
            "#6P#0003F……现在就告诉您我们的推理。\x02\x03",

            "#0001F您听好，首先……\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-50, 20, -1, -1)
    SetChrName("女性的声音")

    #A0191
    AnonymousTalk(
        0xB,
        "#1P──没有那个必要。\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(14, 280, 60, 3)

    #C0192
    ChrTalk(
        0x101,
        "#6P#0005F哎……？\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, -10500, 0, 2200, 90)

    def lambda_634C():
        OP_95(0xFE, -800, 0, 2200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_634C)

    def lambda_6366():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_6366)
    WaitChrThread(0xF, 1)
    Sleep(3800)

    def lambda_637A():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_637A)

    def lambda_6387():
        OP_98(0xFE, 0x0, 0x0, 0x5DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 2, lambda_6387)
    WaitChrThread(0xB, 1)

    #C0193
    ChrTalk(
        0x101,
        "#6P#0005F您、您是……\x02",
    )

    CloseMessageWindow()

    #C0194
    ChrTalk(
        0x104,
        (
            "#12P#0305F黑发的姐姐！？\x01",
            "你不是已经进入市内了吗……\x02",
        )
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0xB,
        (
            "#5P#3404F嗯，是啊。\x02\x03",

            "#3400F不过，看到你们叫住\x01",
            "这个人，就掉头回来了。\x02",
        )
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0x103,
        "#12P#0205F这是怎么回事？\x02",
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0xB,
        (
            "#5P#3401F我就直截了当地说吧。\x02\x03",

            "刚才你们在巴士里说的\x01",
            "假货贩子什么的……\x02\x03",

            "#3403F犯人并不是这个人。\x02",
        )
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0x101,
        (
            "#6P#0005F……哎？\x02\x03",

            "您……您说什么……！？\x02\x03",

            "（话说，巴士里的对话\x01",
            "  都被她听到了吗……？）\x02",
        )
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0xB,
        (
            "#5P#3403F……着眼点倒是不错。\x02\x03",

            "她说我很可疑，可以将这种做法当成\x01",
            "是在试图将你们的注意力转向他人……\x01",
            "你们大概是这样想的吧。\x02\x03",

            "#3401F但是……应该还有条\x01",
            "更重要，而且更明显的线索，\x01",
            "而你们却没有发现。\x02",
        )
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0x101,
        "#6P#0005F明显的线索……？\x02",
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0xB,
        (
            "#5P#3403F我在食堂听到了\x01",
            "你们和乘客们的对话……\x01",
            "其中有个不自然的地方。\x02\x03",

            "#3401F那就是……那位看似慈祥的\x01",
            "老婆婆所说的话。\x02",
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
            "#12P#0105F快要见到阔别三年的孙子，\x01",
            "看起来非常开心的……\x01",
            "那位老婆婆吗！？\x02",
        )
    )

    CloseMessageWindow()

    #C0203
    ChrTalk(
        0x101,
        (
            "#6P#0005F到底从何说起……？\x01",
            "那个人说的话里，没有什么可疑的地方啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0204
    ChrTalk(
        0xB,
        (
            "#5P#3403F仔细想想她说的话。\x02\x03",

            "『三年没来克洛斯贝尔了』……\x02\x03",

            "以及……\x01",
            "『之前来的时候，带孙子去\x01",
            "  米修拉姆的主题公园玩过』这两句话。\x02\x03",

            "#3402F如果你们是克洛斯贝尔的居民，\x01",
            "应该能发现其中的明显矛盾。\x02",
        )
    )

    CloseMessageWindow()

    #C0205
    ChrTalk(
        0x101,
        (
            "#6P#0005F……啊……！！\x02\x03",

            "对了，原来如此啊……！\x02",
        )
    )

    CloseMessageWindow()

    #C0206
    ChrTalk(
        0x103,
        (
            "#12P#0200F……三年前的米修拉姆\x01",
            "还没有主题公园。\x02\x03",

            "她回忆中的地方\x01",
            "根本就不存在……\x02",
        )
    )

    CloseMessageWindow()

    #C0207
    ChrTalk(
        0x104,
        (
            "#12P#0301F……这么说，在场众人中，\x01",
            "说话最可疑的就是\x01",
            "那位婆婆吗。\x02",
        )
    )

    CloseMessageWindow()

    #C0208
    ChrTalk(
        0x102,
        (
            "#12P#0106F这么明显的破绽，\x01",
            "我们竟然没有注意到……\x02",
        )
    )

    CloseMessageWindow()

    #C0209
    ChrTalk(
        0xB,
        (
            "#5P#3400F被她戴着的那副\x01",
            "『慈祥老婆婆』的面具\x01",
            "彻底欺骗了吧。\x02\x03",

            "不是三年没来，\x01",
            "而正是因为定期到访克洛斯贝尔，\x01",
            "所以才会出现这样的差错……\x02",
        )
    )

    CloseMessageWindow()

    #C0210
    ChrTalk(
        0x101,
        (
            "#6P#0003F身为假货贩子\x01",
            "定期到访克洛斯贝尔……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_69F5():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_69F5)

    def lambda_6A02():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6A02)

    def lambda_6A0F():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_6A0F)

    def lambda_6A1C():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_6A1C)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    #C0211
    ChrTalk(
        0x101,
        "#6P#0005F……那、那位老婆婆吗！？\x02",
    )

    CloseMessageWindow()

    #C0212
    ChrTalk(
        0x103,
        "#12P#0200F她现在恐怕已经到东街了。\x02",
    )

    CloseMessageWindow()

    #C0213
    ChrTalk(
        0x104,
        "#12P#0301F不赶快追上去的话，可能会跟丢啊。\x02",
    )

    CloseMessageWindow()

    #C0214
    ChrTalk(
        0x102,
        "#12P#0101F罗、罗伊德！\x02",
    )

    CloseMessageWindow()

    #C0215
    ChrTalk(
        0x101,
        "#6P#0001F啊……我明白！\x02",
    )

    CloseMessageWindow()

    def lambda_6AF1():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6AF1)

    def lambda_6AFE():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6AFE)

    def lambda_6B0B():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_6B0B)

    def lambda_6B18():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_6B18)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    #C0216
    ChrTalk(
        0x101,
        (
            "#6P#0006F真、真是太对不起您了！\x01",
            "我们太失礼了……\x02\x03",

            "稍后我们会再次向您谢罪的，\x01",
            "所以现在就先……！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_6B9A():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_6B9A)
    WaitChrThread(0xF, 1)

    #C0217
    ChrTalk(
        0xF,
        (
            "#5P就、就是嘛！\x01",
            "太无礼了，真是的……！\x02",
        )
    )

    CloseMessageWindow()

    #C0218
    ChrTalk(
        0xB,
        (
            "#5P#3403F……你们现在可没有\x01",
            "慢慢道歉的空闲吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0219
    ChrTalk(
        0x101,
        (
            "#6P#0005F啊……是！\x02\x03",

            "#0001F快追，各位！\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(21000, 3000)

    def lambda_6C41():
        OP_93(0xFE, 0x10E, 0x64)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_6C41)

    def lambda_6C4E():
        OP_93(0xFE, 0x10E, 0x64)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_6C4E)
    BeginChrThread(0x101, 3, 0, 49)
    BeginChrThread(0x102, 3, 0, 49)
    BeginChrThread(0x103, 3, 0, 49)
    BeginChrThread(0x104, 3, 0, 49)
    Return()

    # Function_35_607E end

    def Function_36_6C6F(): pass

    label("Function_36_6C6F")

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
            "#1P#0001F……请您\x01",
            "稍等一下好吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_6D66():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_6D66)
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
        "#5P…………怎么了？\x02",
    )

    CloseMessageWindow()

    #C0222
    ChrTalk(
        0xD,
        (
            "#5P又打算\x01",
            "耍弄我吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0223
    ChrTalk(
        0x101,
        (
            "#6P#0001F抱歉，还没做自我介绍……\x02\x03",

            "我们是\x01",
            "克洛斯贝尔警察局·特别任务支援科\x01",
            "的成员。\x02\x03",

            "麻烦您……\x01",
            "跟我们走一趟吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0224
    ChrTalk(
        0xD,
        "#5P……什、什、什么……！\x02",
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0xD,
        (
            "#5P别、别把我当傻瓜！\x01",
            "竟然开这种恶劣的玩笑……！\x02",
        )
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0x101,
        (
            "#6P#0003……现在就告诉您我们的推理。\x02\x03",

            "#0001F您听好，首先……\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-50, 20, -1, -1)
    SetChrName("女性的声音")

    #A0227
    AnonymousTalk(
        0xB,
        "#1P──没有那个必要。\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(14, 280, 60, 3)

    #C0228
    ChrTalk(
        0x101,
        "#6P#0005F哎……？\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, -10500, 0, 2200, 90)

    def lambda_6F43():
        OP_95(0xFE, -800, 0, 2200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_6F43)

    def lambda_6F5D():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_6F5D)
    WaitChrThread(0xD, 1)
    Sleep(3800)

    def lambda_6F71():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_6F71)

    def lambda_6F7E():
        OP_98(0xFE, 0x0, 0x0, 0x5DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_6F7E)
    WaitChrThread(0xB, 1)

    #C0229
    ChrTalk(
        0x101,
        "#6P#0005F您、您是……\x02",
    )

    CloseMessageWindow()

    #C0230
    ChrTalk(
        0x104,
        (
            "#12P#0305F黑发的姐姐！？\x01",
            "你不是已经进入市里了吗……\x02",
        )
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0xB,
        (
            "#5P#3404F嗯，是啊。\x02\x03",

            "#3400F不过，看到你们叫住\x01",
            "这个人，就掉头回来了。\x02",
        )
    )

    CloseMessageWindow()

    #C0232
    ChrTalk(
        0x103,
        "#12P#0205F这是怎么回事？\x02",
    )

    CloseMessageWindow()

    #C0233
    ChrTalk(
        0xB,
        (
            "#5P#3401F我就直截了当地说吧。\x02\x03",

            "刚才你们在巴士里说的\x01",
            "假货贩子什么的……\x02\x03",

            "#3403F犯人并不是这个人。\x02",
        )
    )

    CloseMessageWindow()

    #C0234
    ChrTalk(
        0x101,
        (
            "#6P#0005F……哎？\x02\x03",

            "您……您说什么……！？\x02\x03",

            "（话说，巴士里的对话\x01",
            "  都被她听到了吗……？）\x02",
        )
    )

    CloseMessageWindow()

    #C0235
    ChrTalk(
        0xB,
        (
            "#5P#3403F……着眼点倒是不错。\x02\x03",

            "因为不太爱和别人说话，\x01",
            "所以他的性格很可疑……\x01",
            "你们是这样想的吧。\x02\x03",

            "#3401F但是……应该还有条\x01",
            "更重要，而且更明显的线索，\x01",
            "而你们却没有发现。\x02",
        )
    )

    CloseMessageWindow()

    #C0236
    ChrTalk(
        0x101,
        "#6P#0005F明显的线索……？\x02",
    )

    CloseMessageWindow()

    #C0237
    ChrTalk(
        0xB,
        (
            "#5P#3403F我在食堂听到了\x01",
            "你们和乘客们的对话……\x01",
            "其中有个不自然的地方。\x02\x03",

            "#3401F那就是……那位看似慈祥的\x01",
            "老婆婆说的话。\x02",
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
            "#12P#0105F快要见到阔别三年的孙子，\x01",
            "看起来非常开心的……\x01",
            "那位老婆婆吗！？\x02",
        )
    )

    CloseMessageWindow()

    #C0239
    ChrTalk(
        0x101,
        (
            "#6P#0005F到底从何说起……？\x01",
            "那个人说的话里，没有什么可疑的地方啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0240
    ChrTalk(
        0xB,
        (
            "#5P#3403F仔细想想她说的话。\x02\x03",

            "『三年没来克洛斯贝尔了』……\x02\x03",

            "以及……\x01",
            "『之前来的时候，带孙子去\x01",
            "  米修拉姆的主题公园玩过』这两句话。\x02\x03",

            "#3402F如果你们是克洛斯贝尔的居民，\x01",
            "应该能发现其中的明显矛盾。\x02",
        )
    )

    CloseMessageWindow()

    #C0241
    ChrTalk(
        0x101,
        (
            "#6P#0005F……啊……！！\x02\x03",

            "对了，原来如此啊……！\x02",
        )
    )

    CloseMessageWindow()

    #C0242
    ChrTalk(
        0x103,
        (
            "#12P#0200F……三年前的米修拉姆\x01",
            "还没有主题公园。\x02\x03",

            "她回忆中的地方\x01",
            "根本就不存在……\x02",
        )
    )

    CloseMessageWindow()

    #C0243
    ChrTalk(
        0x104,
        (
            "#12P#0301F……这么说，在场众人中，\x01",
            "说话最可疑的就是\x01",
            "那位婆婆吗。\x02",
        )
    )

    CloseMessageWindow()

    #C0244
    ChrTalk(
        0x102,
        (
            "#12P#0106F这么明显的破绽，\x01",
            "我们竟然没有注意到……\x02",
        )
    )

    CloseMessageWindow()

    #C0245
    ChrTalk(
        0xB,
        (
            "#5P#3400F被她戴着的那副\x01",
            "『慈祥老婆婆』的面具\x01",
            "彻底欺骗了吧。\x02\x03",

            "她不是三年没来，\x01",
            "而正是因为定期到访克洛斯贝尔，\x01",
            "所以才会犯下这种失误……\x02",
        )
    )

    CloseMessageWindow()

    #C0246
    ChrTalk(
        0x101,
        (
            "#6P#0003F身为假货贩子\x01",
            "定期到访克洛斯贝尔……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_75D0():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_75D0)

    def lambda_75DD():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_75DD)

    def lambda_75EA():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_75EA)

    def lambda_75F7():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_75F7)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    #C0247
    ChrTalk(
        0x101,
        "#6P#0005F……那、那位老婆婆吗！？\x02",
    )

    CloseMessageWindow()

    #C0248
    ChrTalk(
        0x103,
        "#12P#0200F她现在恐怕已经到东街了。\x02",
    )

    CloseMessageWindow()

    #C0249
    ChrTalk(
        0x104,
        "#12P#0301F不赶快追上去的话，可能会跟丢啊。\x02",
    )

    CloseMessageWindow()

    #C0250
    ChrTalk(
        0x102,
        "#12P#0101F罗、罗伊德！\x02",
    )

    CloseMessageWindow()

    #C0251
    ChrTalk(
        0x101,
        "#6P#0001F啊……我明白！\x02",
    )

    CloseMessageWindow()

    def lambda_76CC():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_76CC)

    def lambda_76D9():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_76D9)

    def lambda_76E6():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_76E6)

    def lambda_76F3():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_76F3)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    #C0252
    ChrTalk(
        0x101,
        (
            "#6P#0006F真、真是太对不起您了！\x01",
            "我们太失礼了……\x02\x03",

            "稍后我们会再次向您谢罪的，\x01",
            "所以现在就先……！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_7775():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_7775)
    WaitChrThread(0xD, 1)

    #C0253
    ChrTalk(
        0xD,
        "不、不可原谅，不可原谅啊……！！\x02",
    )

    CloseMessageWindow()

    #C0254
    ChrTalk(
        0xB,
        (
            "#5P#3403F……你们现在可没有\x01",
            "慢慢道歉的空闲吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0255
    ChrTalk(
        0x101,
        (
            "#6P#0005F啊……是！\x02\x03",

            "#0001F快追，各位！\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(21000, 3000)

    def lambda_7816():
        OP_93(0xFE, 0x10E, 0x64)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_7816)

    def lambda_7823():
        OP_93(0xFE, 0x10E, 0x64)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_7823)
    BeginChrThread(0x101, 3, 0, 49)
    BeginChrThread(0x102, 3, 0, 49)
    BeginChrThread(0x103, 3, 0, 49)
    BeginChrThread(0x104, 3, 0, 49)
    Return()

    # Function_36_6C6F end

    def Function_37_7844(): pass

    label("Function_37_7844")

    Sleep(1200)

    def lambda_784C():
        OP_95(0xFE, 16000, 0, 2700, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_784C)

    def lambda_7866():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_7866)
    WaitChrThread(0xFE, 1)
    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)

    def lambda_7890():
        OP_95(0xFE, -12000, 0, 1200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7890)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_37_7844 end

    def Function_38_78B3(): pass

    label("Function_38_78B3")


    def lambda_78B8():
        OP_95(0xFE, 16000, 0, 1200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_78B8)

    def lambda_78D2():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_78D2)
    WaitChrThread(0xFE, 1)

    def lambda_78E7():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_78E7)
    WaitChrThread(0xFE, 1)
    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(2250)

    def lambda_790D():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_790D)
    WaitChrThread(0xFE, 1)

    def lambda_791E():
        OP_95(0xFE, -12000, 0, 2700, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_791E)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_38_78B3 end

    def Function_39_7941(): pass

    label("Function_39_7941")


    def lambda_7946():
        OP_95(0xFE, 16000, 0, 1200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7946)

    def lambda_7960():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_7960)
    WaitChrThread(0xFE, 1)

    def lambda_7975():
        OP_95(0xFE, -12000, 0, 1200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7975)
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

    # Function_39_7941 end

    def Function_40_79D7(): pass

    label("Function_40_79D7")


    def lambda_79DC():
        OP_95(0xFE, 16000, 0, 2700, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_79DC)

    def lambda_79F6():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_79F6)
    WaitChrThread(0xFE, 1)

    def lambda_7A0B():
        OP_95(0xFE, -12000, 0, 2700, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7A0B)
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

    # Function_40_79D7 end

    def Function_41_7A6D(): pass

    label("Function_41_7A6D")


    def lambda_7A72():
        OP_95(0xFE, 16000, 0, 2200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7A72)

    def lambda_7A8C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_7A8C)
    WaitChrThread(0xFE, 1)

    def lambda_7AA1():
        OP_95(0xFE, -12000, 0, 2200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7AA1)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_41_7A6D end

    def Function_42_7AC4(): pass

    label("Function_42_7AC4")


    def lambda_7AC9():
        OP_95(0xFE, 16000, 0, 2700, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7AC9)

    def lambda_7AE3():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_7AE3)
    WaitChrThread(0xFE, 1)

    def lambda_7AF8():
        OP_95(0xFE, -12000, 0, 2700, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7AF8)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_42_7AC4 end

    def Function_43_7B1B(): pass

    label("Function_43_7B1B")


    def lambda_7B20():
        OP_95(0xFE, 16000, 0, 2200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7B20)

    def lambda_7B3A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_7B3A)
    WaitChrThread(0xFE, 1)

    def lambda_7B4F():
        OP_95(0xFE, 0, 0, 2200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7B4F)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_43_7B1B end

    def Function_44_7B6D(): pass

    label("Function_44_7B6D")


    def lambda_7B72():
        OP_95(0xFE, 3000, 0, 1350, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7B72)
    WaitChrThread(0x101, 1)
    Return()

    # Function_44_7B6D end

    def Function_45_7B8C(): pass

    label("Function_45_7B8C")


    def lambda_7B91():
        OP_95(0xFE, 3000, 0, 2950, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7B91)
    WaitChrThread(0x102, 1)
    Return()

    # Function_45_7B8C end

    def Function_46_7BAB(): pass

    label("Function_46_7BAB")


    def lambda_7BB0():
        OP_95(0xFE, 4500, 0, 1350, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_7BB0)
    WaitChrThread(0x103, 1)
    Return()

    # Function_46_7BAB end

    def Function_47_7BCA(): pass

    label("Function_47_7BCA")


    def lambda_7BCF():
        OP_95(0xFE, 4500, 0, 2950, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_7BCF)
    WaitChrThread(0x104, 1)
    Return()

    # Function_47_7BCA end

    def Function_48_7BE9(): pass

    label("Function_48_7BE9")


    def lambda_7BEE():
        OP_98(0xFE, 0xFFFFD8F0, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7BEE)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_48_7BE9 end

    def Function_49_7C08(): pass

    label("Function_49_7C08")

    OP_93(0xFE, 0xB4, 0x0)

    def lambda_7C14():
        OP_98(0xFE, 0x0, 0x0, 0xFFFFF8F8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7C14)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x0)

    def lambda_7C39():
        OP_98(0xFE, 0xFFFFD8F0, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7C39)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_49_7C08 end

    def Function_50_7C53(): pass

    label("Function_50_7C53")


    def lambda_7C58():
        OP_95(0xFE, -10000, 0, 3000, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7C58)

    def lambda_7C72():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7C72)
    Return()

    # Function_50_7C53 end

    def Function_51_7C7B(): pass

    label("Function_51_7C7B")

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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7D26")
    SetChrPos(0x10A, 131150, 3000, 81780, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    label("loc_7D26")

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
            "获得了。\x02",
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
            "#12P#0000F白色的花……\x01",
            "是菲奈尔之花吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0258
    ChrTalk(
        0x102,
        (
            "#12P#11P#0100F这里离克洛斯贝尔市很近，\x01",
            "自己来摘的人\x01",
            "似乎也有不少哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0259
    ChrTalk(
        0x104,
        (
            "#5P#0300F嗯，这里的话，应该\x01",
            "也不会出现太强的魔兽吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0260
    ChrTalk(
        0x103,
        (
            "#06P#0200F即使如此，对老人和孩子\x01",
            "肯定也是有威胁的。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7EC8")

    #C0261
    ChrTalk(
        0x101,
        "#12P#0003F嗯，是啊。\x02",
    )

    CloseMessageWindow()

    #C0262
    ChrTalk(
        0x10A,
        (
            "#6P#0603F……花都摘到了，那就快点走吧，\x01",
            "没工夫磨磨蹭蹭了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7EF8")

    label("loc_7EC8")


    #C0263
    ChrTalk(
        0x101,
        (
            "#12P#0003F嗯，是啊。\x02\x03",

            "#0000F好，那就走吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7EF8")

    OP_65(0x5, 0x1)
    OP_29(0x2E, 0x1, 0x5)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2E, 0x1, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2E, 0x1, 0x4)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2E, 0x1, 0x5)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7F25")
    OP_29(0x2E, 0x1, 0x6)

    label("loc_7F25")

    ClearMapFlags(0x8000000)
    OP_37()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7F45")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)

    label("loc_7F45")

    SetChrPos(0x0, 133170, 3000, 82030, 90)
    EventEnd(0x5)
    Return()

    # Function_51_7C7B end

    def Function_52_7F59(): pass

    label("Function_52_7F59")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0264
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "西·克洛斯贝尔市\x01",
            "东·阿尔摩利卡村　２７４赛尔矩\x01",
            "　　　唐古拉姆门　２０６赛尔矩\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_52_7F59 end

    SaveToFile()

Try(main)
