from ScenarioHelper import *

def main():
    CreateScenaFile(
        "m0309.bin",                # FileName
        "m0309",                    # MapName
        "m0309",                    # Location
        0x00A8,                     # MapIndex
        "ed7300",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 168, 0, 0, 0, 1],
    )

    BuildStringList((
        "m0309",                  # 0
        "新型装甲车",             # 1
        "恐怖分子·首领",         # 2
        "恐怖分子",               # 3
        "恐怖分子",               # 4
        "恐怖分子",               # 5
        "恐怖分子",               # 6
        "恐怖分子",               # 7
        "恐怖分子",               # 8
        "恐怖分子",               # 9
        "战鬼西格蒙德",           # 10
        "谢莉",                   # 11
        "猎兵加雷斯",             # 12
        "新型装甲车",             # 13
        "通讯机",                 # 14
        "剧情用魔兽",             # 15
        "剧情用魔兽",             # 16
        "剧情用魔兽",             # 17
        "剧情用魔兽",             # 18
        "猎兵",                   # 19
        "猎兵",                   # 20
        "猎兵",                   # 21
        "猎兵",                   # 22
        "猎兵",                   # 23
        "影子",                   # 24
        "SE控制",                 # 25
        "bm0320",                 # 26
        "bm0320",                 # 27
        "bm0320",                 # 28
    ))

    ATBonus("ATBonus_4D8", 100, 5, 0, 5, 0, 5, 0, 2, 5, 0, 0, 0, 2, 0, 0, 0)
    ATBonus("ATBonus_4B8", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)

    MonsterBattlePostion("MonsterBattlePostion_4F8", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_4FC", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_500", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_504", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_508", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_50C", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_510", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_514", 2, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_578", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_57C", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_580", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_584", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_588", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_58C", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_590", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_594", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_598", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_59C", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_5A0", 11, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_5A4", 6, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_5A8", 2, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_5AC", 10, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_5B0", 14, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_5B4", 8, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_5B8", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_5BC", 2, 8, 135)
    MonsterBattlePostion("MonsterBattlePostion_5C0", 4, 10, 135)
    MonsterBattlePostion("MonsterBattlePostion_5C4", 0, 9, 135)
    MonsterBattlePostion("MonsterBattlePostion_5C8", 2, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_5CC", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_5D0", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_5D4", 0, 0, 180)

    # monster count: 1

    BattleInfo(
        "BattleInfo_660", 0x0C00, 255, 6, 0, 0, 0, 0, 0, "bm0320", 0x00000000, 100, 0, 0, 0,
        (
            ("ms66100.dat", "ms66100.dat", "ms66100.dat", "ms66100.dat", "ms66100.dat", "ms66100.dat", 0, 0, "MonsterBattlePostion_4F8", "MonsterBattlePostion_578", "ed7451", "ed7453", "ATBonus_4D8"),
            (),
            (),
            (),
        )
    )

    # event battle count: 3

    BattleInfo(
        "BattleInfo_5D8", 0x0042, 3, 6, 45, 3, 3, 30, 0, "bm0320", 0x00000000, 100, 0, 0, 0,
        (
            ("ms42200.dat", "ms42200.dat", "ms42200.dat", "ms42300.dat", "ms42300.dat", "ms42300.dat", "ms42300.dat", "ms42200.dat", "MonsterBattlePostion_598", "MonsterBattlePostion_578", "ed7452", "ed7453", "ATBonus_4B8"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_61C", 0x0052, 3, 6, 45, 3, 3, 30, 0, "bm0320", 0x00000000, 100, 0, 0, 0,
        (
            ("ms88600.dat", "ms84100.dat", "ms84100.dat", "ms84300.dat", "ms84300.dat", 0, "ms84300.dat", 0, "MonsterBattlePostion_5B8", "MonsterBattlePostion_578", "ed7586", "ed7453", "ATBonus_4B8"),
            (),
            (),
            (),
        )
    )

    AddCharChip((
        "chr/ch00000.itc",                   # 00
        "chr/ch00000.itc",                   # 01
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
        "monster/ch66150.itc",               # 10
        "monster/ch66150.itc",               # 11
    ))

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
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
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
    DeclNpc(0,       0,       0,       0,    503,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclMonster(0,       0,       750,     0x185005A,    "BattleInfo_660", 0,   16,  0xFFFF, 0,  1)

    DeclEvent(0x0040, 0, 54,  0.0,                   0.0,                   -1.0,                  16.0,                  [0.125,                -0.0,                  0.0,                   0.0,                   -0.0,                  0.125,                 -0.0,                  0.0,                   0.0,                   -0.0,                  0.25,                  0.0,                   -0.0,                  -0.0,                  0.25,                  1.0])

    DeclActor(5800,    50,      398500,  1200,    5800,    1050,    398500,  0x007C, 0,  3,  0x0000)
    DeclActor(-295500, 0,       500,     1200,    -295500, 1000,    500,     0x007C, 0,  5,  0x0000)
    DeclActor(301800,  0,       19500,   1200,    301800,  1000,    19500,   0x007C, 0,  7,  0x0000)
    DeclActor(-134500, 0,       3000,    1200,    -134500, 1500,    3000,    0x007C, 0,  2,  0x0000)

    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 0
    ChipFrameInfo(1000, 0, [0, 1, 2, 3])                         # 1

    ScpFunction((
        "Function_0_79C",          # 00, 0
        "Function_1_83C",          # 01, 1
        "Function_2_B2A",          # 02, 2
        "Function_3_C0E",          # 03, 3
        "Function_4_D6E",          # 04, 4
        "Function_5_E7D",          # 05, 5
        "Function_6_FDD",          # 06, 6
        "Function_7_10EC",         # 07, 7
        "Function_8_123A",         # 08, 8
        "Function_9_1349",         # 09, 9
        "Function_10_24D2",        # 0A, 10
        "Function_11_251D",        # 0B, 11
        "Function_12_2557",        # 0C, 12
        "Function_13_2585",        # 0D, 13
        "Function_14_25B9",        # 0E, 14
        "Function_15_25E7",        # 0F, 15
        "Function_16_261B",        # 10, 16
        "Function_17_2649",        # 11, 17
        "Function_18_2683",        # 12, 18
        "Function_19_26B1",        # 13, 19
        "Function_20_26C1",        # 14, 20
        "Function_21_3621",        # 15, 21
        "Function_22_3654",        # 16, 22
        "Function_23_3693",        # 17, 23
        "Function_24_36D2",        # 18, 24
        "Function_25_3701",        # 19, 25
        "Function_26_3730",        # 1A, 26
        "Function_27_3772",        # 1B, 27
        "Function_28_37B4",        # 1C, 28
        "Function_29_37EA",        # 1D, 29
        "Function_30_383F",        # 1E, 30
        "Function_31_3894",        # 1F, 31
        "Function_32_38E9",        # 20, 32
        "Function_33_3941",        # 21, 33
        "Function_34_3989",        # 22, 34
        "Function_35_39D1",        # 23, 35
        "Function_36_3A19",        # 24, 36
        "Function_37_3A61",        # 25, 37
        "Function_38_3AA9",        # 26, 38
        "Function_39_3AF7",        # 27, 39
        "Function_40_41DC",        # 28, 40
        "Function_41_643E",        # 29, 41
        "Function_42_6B0B",        # 2A, 42
        "Function_43_6EBA",        # 2B, 43
        "Function_44_7076",        # 2C, 44
        "Function_45_70A4",        # 2D, 45
        "Function_46_70D1",        # 2E, 46
        "Function_47_70F7",        # 2F, 47
        "Function_48_713B",        # 30, 48
        "Function_49_718D",        # 31, 49
        "Function_50_71D1",        # 32, 50
        "Function_51_7223",        # 33, 51
        "Function_52_7267",        # 34, 52
        "Function_53_7286",        # 35, 53
        "Function_54_72AD",        # 36, 54
        "Function_55_76E0",        # 37, 55
    ))


    def Function_0_79C(): pass

    label("Function_0_79C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x143, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x143, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7B6")
    Event(0, 9)

    label("loc_7B6")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x68), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x143, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7D0")
    Event(0, 40)

    label("loc_7D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_7E7")
    ClearScenarioFlags(0x22, 0)
    SetScenarioFlags(0x0, 0)
    Event(0, 20)
    Jump("loc_7F6")

    label("loc_7E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_7F6")
    ClearScenarioFlags(0x22, 1)
    Event(0, 39)

    label("loc_7F6")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_ADD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_80D")
    Event(0, 4)

    label("loc_80D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_ADD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_824")
    Event(0, 6)

    label("loc_824")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_ADD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_83B")
    Event(0, 8)

    label("loc_83B")

    Return()

    # Function_0_79C end

    def Function_1_83C(): pass

    label("Function_1_83C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_868")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21C, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_863")
    ClearChrFlags(0x21, 0x80)
    ModifyEventFlags(1, 0, 0x80)
    SetChrFlags(0x21, 0x8000)

    label("loc_863")

    Jump("loc_872")

    label("loc_868")

    SetChrFlags(0x21, 0x80)
    ModifyEventFlags(0, 0, 0x80)

    label("loc_872")

    OP_52(0x21, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrBattleFlags(0x21, 0x100)
    OP_52(0x21, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x9C4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_10(0x0, 0x0)
    OP_10(0x7, 0x0)
    OP_10(0x8, 0x0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_ADD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8D4")
    SetMapObjFrame(0x3, "Null_color", 0x0, 0x1)
    SetMapObjFrame(0x3, "Null_color2", 0x1, 0x1)
    Jump("loc_8F9")

    label("loc_8D4")

    SetMapObjFrame(0x3, "Null_color", 0x1, 0x1)
    SetMapObjFrame(0x3, "Null_color2", 0x0, 0x1)

    label("loc_8F9")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_ADD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_937")
    SetMapObjFrame(0x4, "Null_color", 0x0, 0x1)
    SetMapObjFrame(0x4, "Null_color2", 0x1, 0x1)
    Jump("loc_95C")

    label("loc_937")

    SetMapObjFrame(0x4, "Null_color", 0x1, 0x1)
    SetMapObjFrame(0x4, "Null_color2", 0x0, 0x1)

    label("loc_95C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_ADD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_99A")
    SetMapObjFrame(0x5, "Null_color", 0x1, 0x1)
    SetMapObjFrame(0x5, "Null_color2", 0x0, 0x1)
    Jump("loc_9BF")

    label("loc_99A")

    SetMapObjFrame(0x5, "Null_color", 0x0, 0x1)
    SetMapObjFrame(0x5, "Null_color2", 0x1, 0x1)

    label("loc_9BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A17")
    SetMapObjFrame(0x3, "Null_color", 0x0, 0x1)
    SetMapObjFrame(0x3, "Null_color2", 0x0, 0x1)
    SetMapObjFrame(0x4, "Null_color", 0x0, 0x1)
    SetMapObjFrame(0x4, "Null_color2", 0x0, 0x1)

    label("loc_A17")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x143, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A7C")
    ClearMapObjFlags(0x9, 0x4)
    OP_78(0x9, 0x8)
    SetMapObjFlags(0x9, 0x1000)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 2000, 0, 1000, 180)
    OP_D5(0x8, 0x0, 0x222E0, 0x0, 0x0)
    OP_74(0x9, 0x1E)
    OP_71(0x9, 0x79, 0xF0, 0x0, 0x20)
    SetMapObjFrame(0x9, "mark00", 0x1, 0x1)

    label("loc_A7C")

    SetMapObjFlags(0x8, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_AD6")
    LoadEffect(0x9, "event\\ev12003.eff")
    PlayEffect(0x9, 0xFF, 0xFF, 0x0, 169200, 0, 13900, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    label("loc_AD6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x143, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B29")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x70), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_B0C")
    Sound(863, 1, 50, 0)
    Sound(864, 1, 50, 0)
    Jump("loc_B29")

    label("loc_B0C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6F), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_B29")
    OP_24(0x35F)
    OP_24(0x360)

    label("loc_B29")

    Return()

    # Function_1_83C end

    def Function_2_B2A(): pass

    label("Function_2_B2A")

    OP_F4(0x2)
    FadeToDark(300, 0, 100)

    #A0001
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "有恢复导力的装置。\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "在这里休息\x01",      # 0
            "放弃\x01",            # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BFF")
    FadeToBright(100, 0)
    Sleep(500)
    SoundLoad(13)
    OP_74(0x7, 0x1E)
    Sound(7, 0, 100, 0)
    OP_70(0x7, 0x0)
    OP_71(0x7, 0x0, 0x1E, 0x0, 0x0)
    OP_79(0x7)
    OP_71(0x7, 0x1F, 0x186, 0x0, 0x20)
    Sleep(1000)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    Sleep(700)
    Sound(13, 0, 100, 0)
    OP_0D()
    OP_32(0xFF, 0xFE, 0x0)
    OP_6A(0x0, 0x0)
    OP_31(0x1)
    Sleep(3500)
    OP_70(0x7, 0x0)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    label("loc_BFF")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_2_B2A end

    def Function_3_C0E(): pass

    label("Function_3_C0E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C20")
    Call(0, 55)
    Return()

    label("loc_C20")

    SetMapFlags(0x8000000)
    EventBegin(0x1)
    SoundLoad(144)
    SoundLoad(150)

    #A0002
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "有升降机的控制面板。\x01",
            "要操作吗？\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "是\x01",      # 0
            "否\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D66")
    Fade(500)
    SetChrPos(0x0, 5200, 50, 397000, 0)
    SetChrPos(0x1, 6200, 50, 397000, 0)
    SetChrPos(0x2, 5200, 50, 396000, 0)
    SetChrPos(0x3, 6200, 50, 396000, 0)
    OP_68(5200, 1550, 392980, 0)
    MoveCamera(24, 45, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(25000, 0)
    OP_0D()
    Sleep(500)
    Sound(144, 0, 100, 0)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(500)
    OP_71(0x3, 0xA, 0xC8, 0x0, 0x0)
    Sleep(200)
    OP_68(6000, 2000, 410000, 3800)
    MoveCamera(22, 49, 0, 3800)
    Sleep(1800)
    Sound(150, 2, 100, 0)
    Sleep(200)
    FadeToDark(500, 0, -1)
    Sleep(4000)
    StopSound(150, 1000, 100)
    Sleep(1000)
    OP_0D()
    NewScene("m0300", 101, 0, 0)
    IdleLoop()

    label("loc_D66")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_3_C0E end

    def Function_4_D6E(): pass

    label("Function_4_D6E")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(0, 0, -1)
    OP_6F(0x1)
    OP_70(0x3, 0x64)
    Sleep(1)
    OP_68(4710, 4300, 403470, 0)
    MoveCamera(23, 36, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(25000, 0)
    OP_90(0x0, 3500, 2800, 409000, 270)
    OP_90(0x1, 3500, 2800, 408000, 270)
    OP_90(0x2, 4500, 2800, 409000, 270)
    OP_90(0x3, 4500, 2800, 408000, 270)
    Sound(145, 0, 100, 0)
    OP_68(4830, 50, 394970, 3200)
    MoveCamera(45, 44, 0, 3200)
    OP_71(0x3, 0x64, 0xA, 0x0, 0x0)
    FadeToBright(500, 0)
    Sleep(3400)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(500)
    OP_79(0x3)
    OP_6F(0x1)
    Sleep(500)
    SetMapObjFrame(0x3, "Null_color", 0x1, 0x1)
    SetMapObjFrame(0x3, "Null_color2", 0x0, 0x1)
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_4_D6E end

    def Function_5_E7D(): pass

    label("Function_5_E7D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E8F")
    Call(0, 55)
    Return()

    label("loc_E8F")

    SetMapFlags(0x8000000)
    EventBegin(0x1)
    SoundLoad(144)
    SoundLoad(150)

    #A0003
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "有升降机的控制面板。\x01",
            "要操作吗？\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "是\x01",      # 0
            "否\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FD5")
    Fade(500)
    SetChrPos(0x0, -296500, 0, 0, 90)
    SetChrPos(0x1, -296500, 0, 1000, 90)
    SetChrPos(0x2, -297500, 0, 0, 90)
    SetChrPos(0x3, -297500, 0, 1000, 90)
    OP_68(-300940, 1500, 840, 0)
    MoveCamera(58, 54, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(25000, 0)
    OP_0D()
    Sleep(500)
    Sound(144, 0, 100, 0)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(500)
    OP_71(0x4, 0xA, 0xC8, 0x0, 0x0)
    Sleep(200)
    OP_68(-282200, 3500, 820, 3200)
    MoveCamera(50, 20, 0, 3200)
    Sleep(1800)
    Sound(150, 2, 100, 0)
    Sleep(200)
    FadeToDark(500, 0, -1)
    Sleep(4000)
    StopSound(150, 1000, 100)
    Sleep(1000)
    OP_0D()
    NewScene("m0301", 121, 0, 0)
    IdleLoop()

    label("loc_FD5")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_5_E7D end

    def Function_6_FDD(): pass

    label("Function_6_FDD")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(0, 0, -1)
    OP_6F(0x1)
    OP_70(0x4, 0x64)
    Sleep(1)
    OP_68(-287810, 4250, 240, 0)
    MoveCamera(70, 33, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(25000, 0)
    OP_90(0x0, -285000, 2750, -1500, 180)
    OP_90(0x1, -286000, 2750, -1500, 180)
    OP_90(0x2, -285000, 2750, -500, 180)
    OP_90(0x3, -286000, 2750, -500, 180)
    Sound(145, 0, 100, 0)
    OP_68(-299340, 1500, -3660, 3200)
    MoveCamera(32, 46, 0, 3200)
    OP_71(0x4, 0x64, 0xA, 0x0, 0x0)
    FadeToBright(500, 0)
    Sleep(3400)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(500)
    OP_79(0x4)
    OP_6F(0x1)
    Sleep(500)
    SetMapObjFrame(0x4, "Null_color", 0x1, 0x1)
    SetMapObjFrame(0x4, "Null_color2", 0x0, 0x1)
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_6_FDD end

    def Function_7_10EC(): pass

    label("Function_7_10EC")

    SetMapFlags(0x8000000)
    EventBegin(0x1)
    SoundLoad(144)
    SoundLoad(150)

    #A0004
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "有升降机的控制面板。\x01",
            "要操作吗？\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "是\x01",      # 0
            "否\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1232")
    Fade(500)
    SetChrPos(0x0, 301300, 0, 20500, 180)
    SetChrPos(0x1, 302300, 0, 20500, 180)
    SetChrPos(0x2, 301300, 0, 21500, 180)
    SetChrPos(0x3, 302300, 0, 21500, 180)
    OP_68(300400, 1500, 21470, 0)
    MoveCamera(37, 51, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(25000, 0)
    OP_0D()
    Sleep(500)
    Sound(144, 0, 100, 0)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(500)
    OP_71(0x5, 0x2F8, 0x3B6, 0x0, 0x0)
    Sleep(200)
    OP_68(301740, -1000, 14430, 3200)
    MoveCamera(33, 42, 0, 3200)
    Sleep(1800)
    Sound(150, 2, 100, 0)
    Sleep(200)
    FadeToDark(500, 0, -1)
    Sleep(4000)
    StopSound(150, 1000, 100)
    Sleep(1000)
    OP_0D()
    NewScene("m0302", 115, 0, 0)
    IdleLoop()

    label("loc_1232")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_7_10EC end

    def Function_8_123A(): pass

    label("Function_8_123A")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(0, 0, -1)
    OP_6F(0x1)
    OP_70(0x5, 0x352)
    Sleep(1)
    OP_68(299320, -1000, 7960, 0)
    MoveCamera(24, 27, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(25000, 0)
    OP_90(0x0, 299500, -2500, 9500, 270)
    OP_90(0x1, 299500, -2500, 8500, 270)
    OP_90(0x2, 300500, -2500, 9500, 270)
    OP_90(0x3, 300500, -2500, 8500, 270)
    Sound(145, 0, 100, 0)
    OP_68(299490, 1500, 24190, 3200)
    MoveCamera(60, 27, 0, 3200)
    OP_71(0x5, 0x352, 0x2F8, 0x0, 0x0)
    FadeToBright(500, 0)
    Sleep(3400)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(500)
    OP_79(0x5)
    OP_6F(0x1)
    Sleep(500)
    SetMapObjFrame(0x5, "Null_color", 0x0, 0x1)
    SetMapObjFrame(0x5, "Null_color2", 0x1, 0x1)
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_8_123A end

    def Function_9_1349(): pass

    label("Function_9_1349")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E2(0x3)
    LoadChrToIndex("chr/ch42200.itc", 0x1E)
    LoadChrToIndex("chr/ch42250.itc", 0x1F)
    LoadChrToIndex("chr/ch42251.itc", 0x20)
    LoadChrToIndex("chr/ch42300.itc", 0x21)
    LoadChrToIndex("chr/ch42350.itc", 0x22)
    LoadChrToIndex("chr/ch42351.itc", 0x23)
    LoadChrToIndex("chr/ch42352.itc", 0x24)
    LoadChrToIndex("chr/ch00050.itc", 0x25)
    LoadChrToIndex("chr/ch00051.itc", 0x26)
    LoadChrToIndex("chr/ch00150.itc", 0x27)
    LoadChrToIndex("chr/ch00151.itc", 0x28)
    LoadChrToIndex("chr/ch00250.itc", 0x29)
    LoadChrToIndex("chr/ch00251.itc", 0x2A)
    LoadChrToIndex("chr/ch00350.itc", 0x2B)
    LoadChrToIndex("chr/ch00351.itc", 0x2C)
    LoadChrToIndex("chr/ch02950.itc", 0x2D)
    LoadChrToIndex("chr/ch02951.itc", 0x2E)
    LoadChrToIndex("chr/ch03050.itc", 0x2F)
    LoadChrToIndex("chr/ch03051.itc", 0x30)
    LoadChrToIndex("apl/ch51243.itc", 0x31)
    LoadChrToIndex("apl/ch50014.itc", 0x32)
    LoadChrToIndex("chr/ch42254.itc", 0x33)
    LoadEffect(0x1, "event/ev10016.eff")
    SetChrPos(0x101, -38000, -8000, -600, 90)
    SetChrPos(0x102, -38000, -8000, 600, 90)
    SetChrPos(0x103, -39000, -8000, -1000, 90)
    SetChrPos(0x104, -39200, -8000, 1000, 90)
    SetChrPos(0x109, -40200, -8000, -600, 90)
    SetChrPos(0x105, -40200, -8000, 600, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x9, 0x31)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, 900, 0, 900, 225)
    SetChrChipByIndex(0xA, 0x1E)
    SetChrSubChip(0xA, 0x0)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)
    SetChrPos(0xA, -1700, 0, -200, 90)
    SetChrChipByIndex(0xB, 0x21)
    SetChrSubChip(0xB, 0x0)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8000)
    SetChrPos(0xB, -200, 0, -1700, 0)
    SetChrChipByIndex(0xC, 0x21)
    SetChrSubChip(0xC, 0x0)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8000)
    SetChrPos(0xC, -1200, 0, 1200, 135)
    SetChrChipByIndex(0xD, 0x21)
    SetChrSubChip(0xD, 0x0)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x8000)
    SetChrPos(0xD, 1200, 0, -1200, 315)
    SetChrChipByIndex(0xE, 0x1E)
    SetChrSubChip(0xE, 0x0)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x8000)
    SetChrPos(0xE, -1300, 0, -1300, 45)
    SetChrChipByIndex(0xF, 0x1E)
    SetChrSubChip(0xF, 0x0)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x8000)
    SetChrPos(0xF, -2600, 0, 300, 90)
    SetChrChipByIndex(0x10, 0x21)
    SetChrSubChip(0x10, 0x0)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x8000)
    SetChrPos(0x10, 300, 0, -2600, 0)
    ClearChrFlags(0x15, 0x80)
    OP_78(0x8, 0x15)
    OP_49()
    ClearMapObjFlags(0x8, 0x4)
    SetMapObjFlags(0x8, 0x1000)
    SetChrPos(0x15, 400, 150, 400, 0)
    OP_D5(0x15, 0x0, 0x36EE8, 0x0, 0x0)
    OP_68(-34500, -7100, 0, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(660, 0)
    SetCameraDistance(16500, 0)
    OP_68(-30500, -7100, 0, 4000)
    FadeToBright(2000, 0)

    def lambda_164A():
        OP_97(0x101, 0x1F40, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_164A)
    Sleep(150)

    def lambda_1667():
        OP_97(0x102, 0x1F40, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1667)
    Sleep(150)

    def lambda_1684():
        OP_97(0x103, 0x1F40, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_1684)
    Sleep(150)

    def lambda_16A1():
        OP_97(0x104, 0x1F40, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_16A1)
    Sleep(150)

    def lambda_16BE():
        OP_97(0x109, 0x1F40, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_16BE)
    Sleep(150)

    def lambda_16DB():
        OP_97(0x105, 0x1F40, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_16DB)
    Sleep(500)

    def lambda_16F8():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_16F8)
    Sleep(300)

    def lambda_170C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_170C)
    Sleep(500)

    def lambda_1720():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_1720)
    Sleep(300)

    def lambda_1734():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_1734)
    Sleep(500)

    def lambda_1748():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_1748)
    Sleep(300)

    def lambda_175C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_175C)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
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
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)

    #C0005
    ChrTalk(
        0x101,
        "#6P#00007F（那是……！）\x02",
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x103,
        (
            "#6P#00201F（看来我们总算\x01",
            "  追上了呢。）\x02",
        )
    )

    CloseMessageWindow()
    OP_68(0, 900, 0, 4000)
    MoveCamera(45, 33, 0, 4000)
    SetCameraDistance(15500, 4000)
    BeginChrThread(0x15, 3, 0, 10)
    OP_6F(0x79)
    Sound(867, 0, 100, 0)

    #C0007
    ChrTalk(
        0x9,
        "……啧，这样啊。\x02",
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x9,
        (
            "炸毁兰花塔的计划\x01",
            "最终还是失败了吗……\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0xA,
        "#3P……可恶，怎么会这样……\x02",
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0xB,
        (
            "#4P那可是杀掉可恨的\x01",
            "『铁血宰相』的大好机会啊……！\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0xE,
        (
            "#6P为了这个目的，我们甚至和\x01",
            "共和国的那些家伙联手行动……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    Sound(812, 0, 100, 0)
    EndChrThread(0x15, 0x3)
    SetChrChipByIndex(0x9, 0x1E)
    SetChrSubChip(0x9, 0x0)
    OP_0D()
    Sleep(300)
    OP_82(0x32, 0x0, 0xBB8, 0xC8)

    #C0012
    ChrTalk(
        0x9,
        "不要沮丧！同志们！\x02",
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x9,
        (
            "有很多伙伴站在我们这边！\x01",
            "不只是凯恩大公，那些家伙\x01",
            "也会再助我们一臂之力的！\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x9,
        (
            "只要我们这次能顺利逃脱，\x01",
            "今后一定还有机会——\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)
    #Sound(2090, 255, 100, 0)    #voice#Lloyd

    #N0015
    NpcTalk(
        0x101,
        "罗伊德的声音",
        "到此为止了……！\x02",
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_1B47():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_1B47)

    def lambda_1B54():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF, 2, lambda_1B54)
    Sleep(50)

    def lambda_1B64():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_1B64)

    def lambda_1B71():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_1B71)
    Sleep(50)

    def lambda_1B81():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_1B81)

    def lambda_1B8E():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_1B8E)
    Sleep(50)

    def lambda_1B9E():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_1B9E)

    def lambda_1BAB():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_1BAB)
    WaitChrThread(0x10, 2)
    Fade(500)
    OP_68(-9800, -300, -700, 0)
    MoveCamera(50, 17, 0, 0)
    OP_6E(660, 0)
    SetCameraDistance(18000, 0)
    SetChrFlags(0x15, 0x80)
    SetMapObjFlags(0x8, 0x4)
    ClearMapObjFlags(0x8, 0x1000)
    OP_68(-4800, 700, 0, 2500)
    SetCameraDistance(16000, 2500)
    SetChrChipByIndex(0x101, 0x25)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x27)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x29)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x2B)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0x2D)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0x2F)
    SetChrSubChip(0x105, 0x0)
    OP_90(0x101, -17200, 0, 0, 90)
    OP_90(0x102, -18000, 0, -1700, 90)
    OP_90(0x103, -19500, 0, 1300, 90)
    OP_90(0x104, -18000, 0, 1700, 90)
    OP_90(0x109, -19500, 0, -1300, 90)
    OP_90(0x105, -18900, 0, 0, 90)

    def lambda_1CB0():
        OP_97(0x101, 0x2710, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1CB0)
    Sleep(100)

    def lambda_1CCD():
        OP_97(0x104, 0x2710, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_1CCD)
    Sleep(100)

    def lambda_1CEA():
        OP_97(0x102, 0x2710, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1CEA)
    Sleep(100)

    def lambda_1D07():
        OP_97(0x105, 0x2710, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_1D07)
    Sleep(100)

    def lambda_1D24():
        OP_97(0x109, 0x2710, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1D24)
    Sleep(100)

    def lambda_1D41():
        OP_97(0x103, 0x2710, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_1D41)
    BeginChrThread(0x20, 1, 0, 19)
    BeginChrThread(0xF, 3, 0, 17)
    Sleep(100)
    BeginChrThread(0xA, 3, 0, 12)
    Sleep(100)
    BeginChrThread(0xE, 3, 0, 16)
    Sleep(400)
    BeginChrThread(0xB, 3, 0, 13)
    Sleep(100)
    BeginChrThread(0xC, 3, 0, 14)
    Sleep(100)
    BeginChrThread(0xD, 3, 0, 15)
    Sleep(100)
    BeginChrThread(0x10, 3, 0, 18)
    Sleep(400)
    BeginChrThread(0x9, 3, 0, 11)
    WaitChrThread(0x9, 3)

    #C0016
    ChrTalk(
        0xA,
        "#11P什么……！？\x02",
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0xE,
        "#11P是刚才那帮小鬼！？\x02",
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0xF,
        (
            "怎么可能……！\x01",
            "我们明明把来路炸毁了啊！\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x103, 0)

    #C0019
    ChrTalk(
        0x104,
        (
            "#00304F#6P不好意思，我们走了\x01",
            "其它路线，总算是追上你们了。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x103,
        (
            "#6P#00202F虽然不清楚你们\x01",
            "获得了什么样的资料，\x01",
            "但内容似乎并不太准确呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0xA,
        "#11P啧……！\x02",
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0xE,
        (
            "#11P这群可恶的小鬼……\x01",
            "到底是些什么人？\x02",
        )
    )

    CloseMessageWindow()
    Fade(250)
    Sound(802, 0, 100, 0)
    Sound(805, 0, 50, 0)
    SetChrChipByIndex(0x101, 0x32)
    SetChrSubChip(0x101, 0x0)
    Sleep(500)

    #C0023
    ChrTalk(
        0x101,
        (
            "#6P#00003F我们是克洛斯贝尔警察局·特别任务支援科的成员。\x02\x03",

            "#00013F在此以暗杀要人未遂、\x01",
            "大规模屠杀未遂等嫌疑，\x01",
            "将你们作为进行恐怖活动的现行犯逮捕！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_82(0x50, 0x0, 0xBB8, 0x12C)

    #C0024
    ChrTalk(
        0xA,
        "#11P警察……！？\x02",
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0xE,
        (
            "#11P不过是些自治州的小警察而已，\x01",
            "休想阻碍我们的大义！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0026
    ChrTalk(
        0x109,
        (
            "#6P#10107F#4S别、别开玩笑了！\x02\x03",

            "#10110F你们这些人，到底想把\x01",
            "多少无辜的人卷入其中！？\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x105,
        (
            "#6P#10306F哎呀呀，竟然还有这种人。\x02\x03",

            "#10300F一味沉浸在自己所谓的大义中，\x01",
            "完全不去顾及其它事情。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0xA,
        "#11P啧！给我闭嘴！\x02",
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0xF,
        (
            "你们这群忘却了荣耀与自尊，\x01",
            "贪恋于空虚繁荣的愚民！\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x102,
        "#6P#00108F唔……！\x02",
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x103,
        (
            "#6P#00203F……看来你们完全\x01",
            "没有反省的意思呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    StopBGM(0xFA0)
    OP_63(0x9, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Fade(250)
    Sound(805, 0, 80, 0)
    SetChrChipByIndex(0x101, 0x25)
    SetChrSubChip(0x101, 0x0)
    OP_0D()
    Sleep(1750)
    OP_64(0x9)
    Sleep(300)

    #C0032
    ChrTalk(
        0x9,
        (
            "#11P把无关人员卷入事件之中，\x01",
            "并非我们的本意。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x9,
        (
            "#11P但如果任由那个男人继续胡作非为，\x01",
            "帝国将会被搞得一团糟……\x02",
        )
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7452", 0)
    SetChrSubChip(0x9, 0x3)
    Sleep(100)
    SetChrSubChip(0x9, 0x4)
    Sound(802, 0, 100, 0)
    Sound(534, 0, 60, 0)
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0034
    ChrTalk(
        0x9,
        (
            "#11P如果有人胆敢阻挠我们的大义，\x01",
            "不管他是谁，我们也绝不会手下留情！\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x101,
        "#6P#00013F啧……！\x02",
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x104,
        (
            "#00307F多说无用！\x01",
            "直接把他们放倒吧！\x02",
        )
    )

    CloseMessageWindow()
    BlurSwitch(0x190, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    SetCameraDistance(13500, 400)

    def lambda_23A3():
        OP_98(0xFE, 0xFFFFD8F0, 0x0, 0x0, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_23A3)
    SetChrChipByIndex(0xA, 0x20)
    SetChrSubChip(0xA, 0x0)
    Sleep(30)

    def lambda_23C8():
        OP_98(0xFE, 0xFFFFD8F0, 0x0, 0x0, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_23C8)
    SetChrChipByIndex(0xE, 0x20)
    SetChrSubChip(0xE, 0x0)

    def lambda_23EA():
        OP_98(0xFE, 0xFFFFD8F0, 0x0, 0x0, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_23EA)
    SetChrChipByIndex(0xF, 0x20)
    SetChrSubChip(0xF, 0x0)
    Sleep(30)

    def lambda_240F():
        OP_98(0xFE, 0xFFFFD8F0, 0x0, 0x0, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_240F)
    SetChrChipByIndex(0xB, 0x23)
    SetChrSubChip(0xB, 0x0)

    def lambda_2431():
        OP_98(0xFE, 0xFFFFD8F0, 0x0, 0x0, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_2431)
    SetChrChipByIndex(0xD, 0x23)
    SetChrSubChip(0xD, 0x0)
    Sleep(30)

    def lambda_2456():
        OP_98(0xFE, 0xFFFFD8F0, 0x0, 0x0, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_2456)
    SetChrChipByIndex(0xC, 0x23)
    SetChrSubChip(0xC, 0x0)

    def lambda_2478():
        OP_98(0xFE, 0xFFFFD8F0, 0x0, 0x0, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_2478)
    SetChrChipByIndex(0x10, 0x23)
    SetChrSubChip(0x10, 0x0)
    Sleep(310)
    EndChrThread(0xA, 0x1)
    EndChrThread(0xE, 0x1)
    EndChrThread(0xF, 0x1)
    EndChrThread(0xB, 0x1)
    EndChrThread(0xD, 0x1)
    EndChrThread(0xC, 0x1)
    EndChrThread(0x10, 0x1)
    Battle("BattleInfo_5D8", 0x0, 0x0, 0x100, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    Call(0, 20)
    Return()

    # Function_9_1349 end

    def Function_10_24D2(): pass

    label("Function_10_24D2")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_251C")
    PlayEffect(0x1, 0xFF, 0x15, 0x1, -600, 1150, 0, 0, 0, 0, 200, 200, 200, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    Jump("Function_10_24D2")

    label("loc_251C")

    Return()

    # Function_10_24D2 end

    def Function_11_251D(): pass

    label("Function_11_251D")


    def lambda_2522():
        OP_95(0xFE, 700, 0, -500, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2522)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    Sound(531, 0, 70, 0)
    Sound(540, 0, 50, 0)
    SetChrChipByIndex(0x9, 0x33)
    SetChrSubChip(0x9, 0x0)
    Return()

    # Function_11_251D end

    def Function_12_2557(): pass

    label("Function_12_2557")


    def lambda_255C():
        OP_95(0xFE, -3000, 0, 0, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_255C)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    SetChrChipByIndex(0xA, 0x1F)
    SetChrSubChip(0xA, 0x0)
    Return()

    # Function_12_2557 end

    def Function_13_2585(): pass

    label("Function_13_2585")


    def lambda_258A():
        OP_95(0xFE, -1500, 0, 700, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_258A)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    Sound(531, 0, 100, 0)
    SetChrChipByIndex(0xB, 0x24)
    SetChrSubChip(0xB, 0x2)
    Return()

    # Function_13_2585 end

    def Function_14_25B9(): pass

    label("Function_14_25B9")


    def lambda_25BE():
        OP_95(0xFE, -900, 0, 2500, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_25BE)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    SetChrChipByIndex(0xC, 0x24)
    SetChrSubChip(0xC, 0x2)
    Return()

    # Function_14_25B9 end

    def Function_15_25E7(): pass

    label("Function_15_25E7")


    def lambda_25EC():
        OP_95(0xFE, -1500, 0, -700, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_25EC)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    Sound(531, 0, 100, 0)
    SetChrChipByIndex(0xD, 0x24)
    SetChrSubChip(0xD, 0x2)
    Return()

    # Function_15_25E7 end

    def Function_16_261B(): pass

    label("Function_16_261B")


    def lambda_2620():
        OP_95(0xFE, -2700, 0, -1900, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2620)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    SetChrChipByIndex(0xE, 0x1F)
    SetChrSubChip(0xE, 0x0)
    Return()

    # Function_16_261B end

    def Function_17_2649(): pass

    label("Function_17_2649")


    def lambda_264E():
        OP_95(0xFE, -2700, 0, 1900, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_264E)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    Sound(531, 0, 70, 0)
    Sound(540, 0, 50, 0)
    SetChrChipByIndex(0xF, 0x1F)
    SetChrSubChip(0xF, 0x0)
    Return()

    # Function_17_2649 end

    def Function_18_2683(): pass

    label("Function_18_2683")


    def lambda_2688():
        OP_95(0xFE, -900, 0, -2500, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2688)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    SetChrChipByIndex(0x10, 0x24)
    SetChrSubChip(0x10, 0x2)
    Return()

    # Function_18_2683 end

    def Function_19_26B1(): pass

    label("Function_19_26B1")

    Sleep(2000)
    Sound(531, 0, 100, 0)
    Sound(805, 0, 100, 0)
    Return()

    # Function_19_26B1 end

    def Function_20_26C1(): pass

    label("Function_20_26C1")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E2(0x3)
    LoadChrToIndex("chr/ch42200.itc", 0x1E)
    LoadChrToIndex("chr/ch42250.itc", 0x1F)
    LoadChrToIndex("chr/ch42251.itc", 0x20)
    LoadChrToIndex("chr/ch42300.itc", 0x21)
    LoadChrToIndex("chr/ch42350.itc", 0x22)
    LoadChrToIndex("chr/ch42351.itc", 0x23)
    LoadChrToIndex("chr/ch42353.itc", 0x24)
    LoadChrToIndex("chr/ch00050.itc", 0x25)
    LoadChrToIndex("chr/ch00051.itc", 0x26)
    LoadChrToIndex("chr/ch00150.itc", 0x27)
    LoadChrToIndex("chr/ch00151.itc", 0x28)
    LoadChrToIndex("chr/ch00250.itc", 0x29)
    LoadChrToIndex("chr/ch00251.itc", 0x2A)
    LoadChrToIndex("chr/ch00350.itc", 0x2B)
    LoadChrToIndex("chr/ch00351.itc", 0x2C)
    LoadChrToIndex("chr/ch02950.itc", 0x2D)
    LoadChrToIndex("chr/ch02951.itc", 0x2E)
    LoadChrToIndex("chr/ch03050.itc", 0x2F)
    LoadChrToIndex("chr/ch03051.itc", 0x30)
    LoadChrToIndex("chr/ch42253.itc", 0x31)
    LoadChrToIndex("monster/ch84150.itc", 0x32)
    LoadChrToIndex("monster/ch84350.itc", 0x33)
    LoadChrToIndex("chr/ch00056.itc", 0x34)
    LoadChrToIndex("chr/ch00156.itc", 0x35)
    LoadChrToIndex("chr/ch00256.itc", 0x36)
    LoadChrToIndex("chr/ch00356.itc", 0x37)
    LoadChrToIndex("chr/ch0295F.itc", 0x38)
    LoadChrToIndex("chr/ch0305F.itc", 0x39)
    LoadEffect(0x1, "event/ev12036.eff")
    LoadEffect(0x2, "event/eva03_01.eff")
    SoundLoad(943)
    SetChrChipByIndex(0x101, 0x25)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x27)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x29)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x2B)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0x2D)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0x2F)
    SetChrSubChip(0x105, 0x0)
    SetChrPos(0x101, -200, 0, 0, 90)
    SetChrPos(0x102, -1000, 0, -1700, 90)
    SetChrPos(0x103, -2500, 0, 1300, 90)
    SetChrPos(0x104, -1000, 0, 1700, 90)
    SetChrPos(0x109, -2500, 0, -1300, 90)
    SetChrPos(0x105, -1900, 0, 0, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrChipByIndex(0x9, 0x1F)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, 3100, 0, 0, 270)
    SetChrChipByIndex(0xA, 0x31)
    SetChrSubChip(0xA, 0x3)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)
    SetChrPos(0xA, 3600, 0, 1900, 270)
    SetChrChipByIndex(0xB, 0x24)
    SetChrSubChip(0xB, 0x3)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8000)
    SetChrPos(0xB, 7200, 0, -1300, 270)
    SetChrChipByIndex(0xC, 0x22)
    SetChrSubChip(0xC, 0x0)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8000)
    SetChrPos(0xC, 7200, 0, 1300, 270)
    SetChrChipByIndex(0xD, 0x24)
    SetChrSubChip(0xD, 0x3)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x8000)
    SetChrPos(0xD, 5200, 0, 2700, 270)
    SetChrChipByIndex(0xE, 0x31)
    SetChrSubChip(0xE, 0x3)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x8000)
    SetChrPos(0xE, 3600, 0, -1900, 270)
    SetChrChipByIndex(0xF, 0x31)
    SetChrSubChip(0xF, 0x3)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x8000)
    SetChrPos(0xF, 6200, 0, 0, 270)
    SetChrChipByIndex(0x10, 0x22)
    SetChrSubChip(0x10, 0x0)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x8000)
    SetChrPos(0x10, 5200, 0, -2700, 270)
    SetChrChipByIndex(0x16, 0x32)
    SetChrSubChip(0x16, 0x0)
    SetChrFlags(0x16, 0x8000)
    SetChrPos(0x16, 0, 0, 30000, 180)
    OP_A7(0x16, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x17, 0x32)
    SetChrSubChip(0x17, 0x0)
    SetChrFlags(0x17, 0x8000)
    SetChrPos(0x17, 0, 0, 30000, 180)
    OP_A7(0x17, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x18, 0x33)
    SetChrSubChip(0x18, 0x0)
    SetChrFlags(0x18, 0x8000)
    SetChrPos(0x18, 0, 0, 30000, 180)
    OP_A7(0x18, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x19, 0x33)
    SetChrSubChip(0x19, 0x0)
    SetChrFlags(0x19, 0x8000)
    SetChrPos(0x19, 0, 0, 30000, 180)
    OP_A7(0x19, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x14, 0x80)
    OP_78(0x6, 0x14)
    OP_49()
    SetMapObjFlags(0x6, 0x4)
    SetMapObjFlags(0x6, 0x1000)
    SetMapObjFrame(0x6, "light", 0x0, 0x1)
    SetMapObjFrame(0x6, "mark01", 0x0, 0x1)
    SetMapObjFrame(0x6, "mark00", 0x1, 0x1)
    OP_74(0x6, 0x1E)
    OP_71(0x6, 0xB5, 0xF0, 0x0, 0x20)
    SetChrPos(0x14, 0, 0, 35000, 180)
    OP_D5(0x14, 0x0, 0x2BF20, 0x0, 0x0)
    OP_68(1800, 900, 0, 0)
    MoveCamera(53, 19, 0, 0)
    OP_6E(660, 0)
    SetCameraDistance(15500, 0)
    SetCameraDistance(16500, 2000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_63(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    SetChrChipByIndex(0x9, 0x20)
    SetChrSubChip(0x9, 0x0)

    def lambda_2ADC():
        OP_96(0xFE, 0x1004, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2ADC)
    WaitChrThread(0x9, 1)
    SetChrChipByIndex(0x9, 0x1F)
    SetChrSubChip(0x9, 0x0)
    OP_64(0x9)

    def lambda_2B05():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_2B05)
    Sleep(500)

    #C0037
    ChrTalk(
        0xA,
        "这……怎么可能！？\x02",
    )

    CloseMessageWindow()

    def lambda_2B39():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_2B39)
    Sleep(500)

    #C0038
    ChrTalk(
        0xB,
        (
            "区区自治州警察，\x01",
            "居然有这种实力……！？\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x101,
        (
            "#6P#00006F或许正如你们所说，克洛斯贝尔\x01",
            "如今正在贪恋着繁荣。\x02\x03",

            "#00013F但我们并没有沉浸于其中，\x01",
            "更没有丧失自己的荣耀与自尊！\x02\x03",

            "#00007F面对着各种各样的障碍与压力……\x01",
            "我们会在承受一切的同时努力奋战，\x01",
            "并试图跨越眼前的壁障！\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x102,
        "#6P#00102F罗伊德……\x02",
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x109,
        "#6P#10100F罗伊德警官……\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0xA, 3, 0, 22)
    Sleep(200)
    BeginChrThread(0xB, 3, 0, 23)
    Sleep(200)
    BeginChrThread(0xD, 3, 0, 23)
    Sleep(200)
    Sound(540, 0, 20, 0)
    BeginChrThread(0xE, 3, 0, 22)
    Sleep(200)
    BeginChrThread(0xF, 3, 0, 22)
    Sound(531, 0, 30, 0)
    WaitChrThread(0xF, 3)
    Sleep(300)

    #C0042
    ChrTalk(
        0x9,
        (
            "#11P……似乎有些\x01",
            "小看你们了。\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x9,
        (
            "#11P好吧，我承认试图炸毁兰花塔\x01",
            "的举动的确有些过火了。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x101,
        "#6P#00000F言下之意……\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0045
    ChrTalk(
        0x9,
        (
            "#11P但是！在我们成功取下\x01",
            "『铁血宰相』的首级之前，\x01",
            "是绝不能被抓住的！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_93(0x103, 0x0, 0x1F4)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0046
    ChrTalk(
        0x103,
        "#12P#00207F各位……！\x02",
    )

    CloseMessageWindow()
    OP_93(0x104, 0x0, 0x1F4)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0047
    ChrTalk(
        0x104,
        "#00307F#11P要来了，快退后！\x02",
    )

    CloseMessageWindow()
    OP_68(0, 900, 17000, 1500)
    MoveCamera(37, 15, 0, 1500)
    SetCameraDistance(14500, 1500)

    def lambda_2E59():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2E59)
    BeginChrThread(0x9, 3, 0, 24)
    Sleep(50)

    def lambda_2E6F():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_2E6F)
    BeginChrThread(0xA, 3, 0, 24)
    Sleep(50)

    def lambda_2E85():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_2E85)
    BeginChrThread(0xE, 3, 0, 24)
    Sleep(50)

    def lambda_2E9B():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_2E9B)
    BeginChrThread(0xD, 3, 0, 25)
    BeginChrThread(0x10, 3, 0, 25)
    Sleep(50)
    BeginChrThread(0xF, 3, 0, 24)
    BeginChrThread(0xB, 3, 0, 25)
    BeginChrThread(0xC, 3, 0, 25)
    OP_6F(0x79)
    StopBGM(0x1388)
    Sound(598, 0, 50, 0)
    Sound(623, 0, 100, 0)
    PlayEffect(0x1, 0x1, 0xFF, 0x0, 0, 1000, 30000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x1, 0x2, 0xFF, 0x0, 1000, 1500, 30000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x1, 0x3, 0xFF, 0x0, -1000, 1500, 30000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    BeginChrThread(0x14, 3, 0, 21)
    Sleep(500)
    Sound(869, 0, 50, 0)
    OP_68(-2600, 900, 0, 1000)
    MoveCamera(53, 19, 0, 1000)
    SetCameraDistance(17500, 1000)
    Sleep(200)
    BeginChrThread(0x103, 3, 0, 38)
    Sleep(50)
    BeginChrThread(0x104, 3, 0, 35)
    BeginChrThread(0x105, 3, 0, 36)
    Sleep(50)
    BeginChrThread(0x101, 3, 0, 33)
    BeginChrThread(0x109, 3, 0, 37)
    Sleep(50)
    BeginChrThread(0x102, 3, 0, 34)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x14, 3)
    Sleep(500)

    #C0048
    ChrTalk(
        0x101,
        "#00007F#6P#N什么……！？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0049
    ChrTalk(
        0x109,
        "#10110F#6P#N诱、诱导飞弹！？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7586", 0)
    Fade(250)
    OP_68(0, 1000, 25000, 0)
    MoveCamera(25, 25, 21, 0)
    OP_6E(700, 0)
    SetCameraDistance(13500, 0)
    OP_68(1500, 1250, 1000, 3000)
    MoveCamera(50, 15, 11, 3000)
    SetCameraDistance(15500, 3000)
    Sound(486, 0, 100, 0)
    Sound(494, 0, 100, 0)
    ClearMapObjFlags(0x6, 0x4)
    PlayEffect(0x2, 0x4, 0x14, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0x5, 0x14, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0x6, 0x14, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_3153():
        OP_96(0xFE, 0x0, 0x0, 0x0, 0x2AF8, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_3153)
    Sleep(2500)

    def lambda_3170():
        OP_D5(0xFE, 0x0, 0x30D40, 0x0, 0x2BC)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_3170)
    OP_71(0x6, 0x5B, 0x78, 0x0, 0x0)
    Sound(487, 0, 100, 0)
    WaitChrThread(0x14, 1)
    StopEffect(0x4, 0x2)
    StopEffect(0x5, 0x2)
    StopEffect(0x6, 0x2)
    OP_82(0x64, 0x64, 0xBB8, 0x1F4)
    OP_79(0x6)
    OP_6F(0x79)
    Sleep(1000)
    Fade(500)
    OP_68(-2300, 1100, 0, 0)
    MoveCamera(50, 19, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(14500, 0)
    OP_68(-4300, 1100, 0, 1500)
    SetCameraDistance(16000, 1500)
    OP_0D()
    Sound(145, 2, 100, 0)
    OP_74(0x6, 0xF)
    OP_71(0x6, 0xF1, 0xFD, 0x0, 0x0)
    OP_79(0x6)
    OP_24(0x91)
    Sound(143, 0, 100, 0)
    OP_74(0x6, 0x1E)
    OP_6F(0x79)

    #C0050
    ChrTalk(
        0x109,
        "#6P#N#10111F啊……\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0051
    ChrTalk(
        0x102,
        "#6P#N#00101F是克洛斯贝尔警备队的……！\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0052
    ChrTalk(
        0x104,
        (
            "#00307F#6P#N你们这些混蛋……\x01",
            "到底是从哪里搞到这东西的！？\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0053
    ChrTalk(
        0xE,
        (
            "#12P哈哈，有相当能干的\x01",
            "协助者支援我们！\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0xB,
        (
            "你们就在那里\x01",
            "陪它好好玩一玩吧！\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x9,
        (
            "#6P不必再说什么了！\x01",
            "立刻撤退！\x02",
        )
    )

    CloseMessageWindow()
    Sound(943, 2, 50, 0)
    BeginChrThread(0x16, 0, 0, 28)
    BeginChrThread(0xB, 3, 0, 27)
    BeginChrThread(0xC, 3, 0, 27)
    Sleep(100)
    BeginChrThread(0xF, 3, 0, 26)
    Sleep(100)
    BeginChrThread(0xD, 3, 0, 27)
    BeginChrThread(0x10, 3, 0, 27)
    Sleep(100)
    BeginChrThread(0x9, 3, 0, 26)
    Sleep(100)
    BeginChrThread(0xA, 3, 0, 26)
    BeginChrThread(0xE, 3, 0, 26)
    WaitChrThread(0x16, 3)

    def lambda_337F():
        OP_A6(0xFE, 0x0, 0x32, 0x2EE, 0xBB8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_337F)
    Sleep(50)

    def lambda_339B():
        OP_A6(0xFE, 0x0, 0x32, 0x2EE, 0xBB8)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_339B)
    Sleep(50)

    def lambda_33B7():
        OP_A6(0xFE, 0x0, 0x32, 0x2EE, 0xBB8)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_33B7)
    Sleep(50)

    def lambda_33D3():
        OP_A6(0xFE, 0x0, 0x32, 0x2EE, 0xBB8)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_33D3)
    Sleep(50)

    def lambda_33EF():
        OP_A6(0xFE, 0x0, 0x32, 0x2EE, 0xBB8)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_33EF)
    Sleep(50)

    def lambda_340B():
        OP_A6(0xFE, 0x0, 0x32, 0x2EE, 0xBB8)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_340B)
    Sleep(250)
    Fade(250)
    Sound(805, 0, 100, 0)
    Sound(531, 0, 100, 0)
    SetChrChipByIndex(0x101, 0x25)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x27)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x29)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x2B)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0x2D)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0x2F)
    SetChrSubChip(0x105, 0x0)
    OP_0D()
    WaitChrThread(0x19, 3)

    #C0056
    ChrTalk(
        0x101,
        (
            "#6P#00010F唔……！\x01",
            "各位，还能继续战斗吗！？\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x102,
        "#6P#N#00107F嗯……应该没问题！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0058
    ChrTalk(
        0x103,
        "#00201F#6P我也能继续坚持……！\x02",
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x105,
        (
            "#6P#10304F呵呵，如果运气好，\x01",
            "说不定可以把它击毁呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x109,
        (
            "#6P#N#10107F这是相当坚固的车辆！\x01",
            "而且还具备耐魔法的性能！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0061
    ChrTalk(
        0x104,
        "#00307F#6P准备应战！找准时机攻击吧！\x02",
    )

    CloseMessageWindow()
    BlurSwitch(0x1F4, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    SetCameraDistance(14000, 500)
    Sleep(500)
    EndChrThread(0x9, 0xFF)
    EndChrThread(0xA, 0xFF)
    EndChrThread(0xB, 0xFF)
    EndChrThread(0xC, 0xFF)
    EndChrThread(0xD, 0xFF)
    EndChrThread(0xE, 0xFF)
    EndChrThread(0xF, 0xFF)
    EndChrThread(0x10, 0xFF)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x10, 0x80)
    OP_24(0x91)
    OP_24(0x3AF)
    Battle("BattleInfo_61C", 0x0, 0x0, 0x100, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x17, 0x80)
    SetChrFlags(0x18, 0x80)
    SetChrFlags(0x19, 0x80)
    Call(0, 39)
    Return()

    # Function_20_26C1 end

    def Function_21_3621(): pass

    label("Function_21_3621")

    Sleep(1500)
    OP_82(0x1F4, 0x1F4, 0xBB8, 0x3E8)
    Sound(196, 0, 100, 0)
    Sound(598, 0, 80, 0)
    Sleep(250)
    Sound(556, 0, 100, 0)
    Sound(250, 0, 100, 0)
    Sleep(750)
    Return()

    # Function_21_3621 end

    def Function_22_3654(): pass

    label("Function_22_3654")


    def lambda_3659():
        OP_A6(0xFE, 0x0, 0x32, 0x384, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3659)
    Sleep(500)
    SetChrSubChip(0xFE, 0x2)
    Sleep(80)
    SetChrSubChip(0xFE, 0x1)
    Sleep(80)
    Fade(250)
    Sound(802, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x1F)
    SetChrSubChip(0xFE, 0x0)
    OP_0D()
    Return()

    # Function_22_3654 end

    def Function_23_3693(): pass

    label("Function_23_3693")


    def lambda_3698():
        OP_A6(0xFE, 0x0, 0x32, 0x384, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3698)
    Sleep(500)
    SetChrSubChip(0xFE, 0x2)
    Sleep(80)
    SetChrSubChip(0xFE, 0x1)
    Sleep(80)
    Fade(250)
    Sound(812, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x22)
    SetChrSubChip(0xFE, 0x0)
    OP_0D()
    Return()

    # Function_23_3693 end

    def Function_24_36D2(): pass

    label("Function_24_36D2")

    SetChrChipByIndex(0xFE, 0x20)
    SetChrSubChip(0xFE, 0x0)

    def lambda_36DF():
        OP_98(0xFE, 0x7D0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_36DF)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0xFE, 0x1F)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_24_36D2 end

    def Function_25_3701(): pass

    label("Function_25_3701")

    SetChrChipByIndex(0xFE, 0x23)
    SetChrSubChip(0xFE, 0x0)

    def lambda_370E():
        OP_98(0xFE, 0x7D0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_370E)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0xFE, 0x22)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_25_3701 end

    def Function_26_3730(): pass

    label("Function_26_3730")

    OP_93(0xFE, 0x5A, 0x1F4)
    SetChrChipByIndex(0xFE, 0x20)
    SetChrSubChip(0xFE, 0x0)

    def lambda_3744():
        OP_98(0xFE, 0x9C40, 0x0, 0x0, 0x157C, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3744)
    Sleep(5000)

    def lambda_3761():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3761)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_26_3730 end

    def Function_27_3772(): pass

    label("Function_27_3772")

    OP_93(0xFE, 0x5A, 0x1F4)
    SetChrChipByIndex(0xFE, 0x23)
    SetChrSubChip(0xFE, 0x0)

    def lambda_3786():
        OP_98(0xFE, 0x9C40, 0x0, 0x0, 0x157C, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3786)
    Sleep(5000)

    def lambda_37A3():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_37A3)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_27_3772 end

    def Function_28_37B4(): pass

    label("Function_28_37B4")

    ClearChrFlags(0x16, 0x80)
    BeginChrThread(0x16, 3, 0, 29)
    Sleep(500)
    ClearChrFlags(0x18, 0x80)
    BeginChrThread(0x18, 3, 0, 31)
    Sleep(500)
    ClearChrFlags(0x17, 0x80)
    BeginChrThread(0x17, 3, 0, 30)
    Sleep(500)
    ClearChrFlags(0x19, 0x80)
    BeginChrThread(0x19, 3, 0, 32)
    Return()

    # Function_28_37B4 end

    def Function_29_37EA(): pass

    label("Function_29_37EA")


    def lambda_37EF():
        OP_96(0xFE, 0x0, 0x0, 0x2710, 0x157C, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_37EF)

    def lambda_3809():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3809)
    WaitChrThread(0xFE, 1)

    def lambda_381E():
        OP_95(0xFE, -1500, 0, 5300, 5500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_381E)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xE1, 0x1F4)
    Return()

    # Function_29_37EA end

    def Function_30_383F(): pass

    label("Function_30_383F")


    def lambda_3844():
        OP_96(0xFE, 0x0, 0x0, 0x2710, 0x157C, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3844)

    def lambda_385E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_385E)
    WaitChrThread(0xFE, 1)

    def lambda_3873():
        OP_95(0xFE, -2700, 0, 6700, 5500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3873)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xE1, 0x1F4)
    Return()

    # Function_30_383F end

    def Function_31_3894(): pass

    label("Function_31_3894")


    def lambda_3899():
        OP_96(0xFE, 0x0, 0x0, 0x2710, 0x157C, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3899)

    def lambda_38B3():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_38B3)
    WaitChrThread(0xFE, 1)

    def lambda_38C8():
        OP_95(0xFE, 400, 0, 6000, 5500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_38C8)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xE1, 0x1F4)
    Return()

    # Function_31_3894 end

    def Function_32_38E9(): pass

    label("Function_32_38E9")


    def lambda_38EE():
        OP_96(0xFE, 0x0, 0x0, 0x2710, 0x157C, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_38EE)

    def lambda_3908():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3908)
    WaitChrThread(0xFE, 1)

    def lambda_391D():
        OP_95(0xFE, -800, 0, 7400, 5500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_391D)
    WaitChrThread(0xFE, 1)
    OP_24(0x3AF)
    OP_93(0xFE, 0xE1, 0x1F4)
    Return()

    # Function_32_38E9 end

    def Function_33_3941(): pass

    label("Function_33_3941")


    def lambda_3946():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3946)
    Sleep(200)
    SetChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0x101, 0x34)
    SetChrSubChip(0x101, 0x2)

    def lambda_3963():
        OP_9C(0xFE, 0xFFFFE69C, 0x0, 0x0, 0x258, 0x7D0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3963)
    WaitChrThread(0x101, 1)
    SetChrSubChip(0x101, 0x0)
    ClearChrFlags(0xFE, 0x20)
    Return()

    # Function_33_3941 end

    def Function_34_3989(): pass

    label("Function_34_3989")


    def lambda_398E():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_398E)
    Sleep(200)
    SetChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0x102, 0x35)
    SetChrSubChip(0x102, 0x2)

    def lambda_39AB():
        OP_9C(0xFE, 0xFFFFE958, 0x0, 0xFFFFFCE0, 0x258, 0x7D0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_39AB)
    WaitChrThread(0x102, 1)
    SetChrSubChip(0x102, 0x0)
    ClearChrFlags(0xFE, 0x20)
    Return()

    # Function_34_3989 end

    def Function_35_39D1(): pass

    label("Function_35_39D1")


    def lambda_39D6():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_39D6)
    Sleep(200)
    SetChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0x104, 0x37)
    SetChrSubChip(0x104, 0x2)

    def lambda_39F3():
        OP_9C(0xFE, 0xFFFFE958, 0x0, 0x320, 0x258, 0x7D0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_39F3)
    WaitChrThread(0x104, 1)
    SetChrSubChip(0x104, 0x0)
    ClearChrFlags(0xFE, 0x20)
    Return()

    # Function_35_39D1 end

    def Function_36_3A19(): pass

    label("Function_36_3A19")


    def lambda_3A1E():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3A1E)
    Sleep(200)
    SetChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0x105, 0x39)
    SetChrSubChip(0x105, 0x2)

    def lambda_3A3B():
        OP_9C(0xFE, 0xFFFFE570, 0x0, 0x0, 0x258, 0x7D0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_3A3B)
    WaitChrThread(0x105, 1)
    SetChrSubChip(0x105, 0x0)
    ClearChrFlags(0xFE, 0x20)
    Return()

    # Function_36_3A19 end

    def Function_37_3A61(): pass

    label("Function_37_3A61")


    def lambda_3A66():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3A66)
    Sleep(200)
    SetChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0x109, 0x38)
    SetChrSubChip(0x109, 0x2)

    def lambda_3A83():
        OP_9C(0xFE, 0xFFFFEA20, 0x0, 0xFFFFFE70, 0x258, 0x7D0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_3A83)
    WaitChrThread(0x109, 1)
    SetChrSubChip(0x109, 0x0)
    ClearChrFlags(0xFE, 0x20)
    Return()

    # Function_37_3A61 end

    def Function_38_3AA9(): pass

    label("Function_38_3AA9")


    def lambda_3AAE():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_3AAE)
    Sleep(200)
    SetChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0x103, 0x36)
    SetChrSubChip(0x103, 0x2)
    Sound(809, 0, 100, 0)

    def lambda_3AD1():
        OP_9C(0xFE, 0xFFFFEA20, 0x0, 0x190, 0x258, 0x7D0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_3AD1)
    WaitChrThread(0x103, 1)
    SetChrSubChip(0x103, 0x0)
    ClearChrFlags(0xFE, 0x20)
    Return()

    # Function_38_3AA9 end

    def Function_39_3AF7(): pass

    label("Function_39_3AF7")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E2(0x3)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00150.itc", 0x1F)
    LoadChrToIndex("chr/ch00250.itc", 0x20)
    LoadChrToIndex("chr/ch00350.itc", 0x21)
    LoadChrToIndex("chr/ch02950.itc", 0x22)
    LoadChrToIndex("chr/ch03050.itc", 0x23)
    LoadEffect(0x0, "battle\\ms00103.eff ")
    SoundLoad(863)
    SoundLoad(864)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0x22)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0x23)
    SetChrSubChip(0x105, 0x0)
    SetChrPos(0x101, -4700, 0, 0, 90)
    SetChrPos(0x102, -4800, 0, -2500, 90)
    SetChrPos(0x103, -6100, 0, 1700, 90)
    SetChrPos(0x104, -4800, 0, 2500, 90)
    SetChrPos(0x109, -6100, 0, -1700, 90)
    SetChrPos(0x105, -6700, 0, 0, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrFlags(0x14, 0x80)
    SetMapObjFlags(0x6, 0x4)
    ClearMapObjFlags(0x6, 0x1000)
    SetChrFlags(0x8, 0x80)
    OP_78(0x9, 0x8)
    OP_49()
    ClearMapObjFlags(0x9, 0x4)
    SetMapObjFlags(0x9, 0x1000)
    OP_74(0x9, 0x1E)
    OP_71(0x9, 0x79, 0xF0, 0x0, 0x20)
    SetMapObjFrame(0x9, "mark00", 0x1, 0x1)
    SetChrPos(0x8, 2000, 0, 1000, 180)
    OP_D5(0x8, 0x0, 0x222E0, 0x0, 0x0)
    OP_68(1500, 2100, 500, 0)
    MoveCamera(33, 37, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(14500, 0)
    FadeToBright(1000, 0)
    OP_0D()
    SetCameraDistance(15500, 2000)
    OP_82(0x12C, 0x12C, 0xBB8, 0x5DC)
    Sound(196, 0, 100, 0)
    Sound(598, 0, 100, 0)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0xA)
    PlayEffect(0x0, 0x0, 0xFF, 0x0, 2000, 1500, 1500, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    CancelBlur(1500)
    Sleep(200)
    Sound(556, 0, 100, 0)
    Sound(200, 0, 100, 0)
    Sleep(1300)
    OP_6F(0x79)
    OP_68(-2300, 900, 0, 2000)
    MoveCamera(50, 19, 0, 2000)
    SetCameraDistance(16000, 2000)
    OP_6F(0x79)

    #C0062
    ChrTalk(
        0x101,
        "#6P#00013F很好……成功了！\x02",
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x102,
        (
            "#6P#00107F得赶快把坐在车内的\x01",
            "人救出来……！\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0064
    ChrTalk(
        0x103,
        (
            "#6P#00206F……不必，车内\x01",
            "并没有任何生命反应。\x02\x03",

            "#00201F应该是应用了\x01",
            "自动操纵系统。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0065
    ChrTalk(
        0x109,
        "#6P#N#10111F什么！？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)
    Sound(531, 0, 100, 0)
    Sound(805, 0, 100, 0)
    OP_0D()

    def lambda_3E47():
        TurnDirection(0x109, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_3E47)
    Sleep(50)

    def lambda_3E57():
        TurnDirection(0x102, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_3E57)
    Sleep(50)

    def lambda_3E67():
        TurnDirection(0x101, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3E67)
    Sleep(50)

    def lambda_3E77():
        TurnDirection(0x104, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_3E77)
    Sleep(50)

    def lambda_3E87():
        TurnDirection(0x105, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_3E87)
    Sleep(50)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x105, 0)

    #C0066
    ChrTalk(
        0x104,
        "#00306F#5P喂喂，真的假的……\x02",
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x105,
        (
            "#12P#10301F那些智能兵器也很令人在意……\x01",
            "看来有十分神秘的家伙\x01",
            "在暗中协助他们呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x5A, 0x1F4)
    Sleep(150)

    #C0068
    ChrTalk(
        0x101,
        (
            "#5P#00003F……唔，之后再说这些吧！\x02\x03",

            "#00013F我们要赶快把那些逃掉的家伙给——\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0x1770)
    Sound(863, 2, 50, 0)
    Sleep(300)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
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
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_4024():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_4024)

    def lambda_4031():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_4031)

    def lambda_403E():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_403E)

    def lambda_404B():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_404B)

    def lambda_4058():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_4058)
    OP_68(32500, 900, 0, 3000)
    OP_6F(0x79)
    MoveCamera(55, 23, 0, 4500)
    SetCameraDistance(19500, 4000)
    Sound(864, 2, 60, 0)
    OP_82(0x32, 0x32, 0xBB8, 0x1F4)
    Sleep(1500)
    OP_82(0x32, 0x32, 0xBB8, 0x1F4)
    Sleep(1500)
    OP_82(0x32, 0x32, 0xBB8, 0x1F4)
    Sleep(1500)
    OP_6F(0x79)

    #C0069
    ChrTalk(
        0x101,
        "#00010F#6P#N！？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0070
    ChrTalk(
        0x103,
        "#00210F#6P#N呜……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0071
    ChrTalk(
        0x109,
        "#10107F#6P#N这是……枪击的声音！？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0072
    ChrTalk(
        0x102,
        "#00108F#6P#N到底发生了什么事……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0073
    ChrTalk(
        0x104,
        "#00307F#6P#N……总之，赶快过去看看吧！\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrFlags(0x14, 0x80)
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_D7(0x20)
    OP_D7(0x21)
    OP_D7(0x22)
    OP_D7(0x23)
    OP_37()
    SetChrPos(0x0, -4000, 0, 0, 90)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetScenarioFlags(0x143, 7)
    OP_29(0xA4, 0x1, 0x9)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7561", 0)
    ReplaceBGM("ed7300", "ed7561")
    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    # Function_39_3AF7 end

    def Function_40_41DC(): pass

    label("Function_40_41DC")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch42300.itc", 0x1E)
    LoadChrToIndex("chr/ch42351.itc", 0x1F)
    LoadChrToIndex("chr/ch42352.itc", 0x20)
    LoadChrToIndex("chr/ch42353.itc", 0x21)
    LoadChrToIndex("chr/ch03300.itc", 0x22)
    LoadChrToIndex("chr/ch03400.itc", 0x23)
    LoadChrToIndex("chr/ch41900.itc", 0x24)
    LoadChrToIndex("chr/ch41950.itc", 0x25)
    LoadChrToIndex("chr/ch41951.itc", 0x26)
    LoadChrToIndex("chr/ch41952.itc", 0x27)
    LoadChrToIndex("apl/ch51244.itc", 0x28)
    LoadChrToIndex("apl/ch51217.itc", 0x29)
    LoadChrToIndex("apl/ch51221.itc", 0x2A)
    LoadChrToIndex("chr/ch02952.itc", 0x2B)
    LoadChrToIndex("chr/ch42253.itc", 0x2C)
    LoadChrToIndex("apl/ch51246.itc", 0x2D)
    LoadChrToIndex("apl/ch51247.itc", 0x2E)
    LoadChrToIndex("apl/ch51248.itc", 0x2F)
    LoadChrToIndex("apl/ch51249.itc", 0x30)
    LoadChrToIndex("apl/ch51250.itc", 0x31)
    LoadChrToIndex("apl/ch51251.itc", 0x32)
    LoadChrToIndex("apl/ch51252.itc", 0x33)
    LoadChrToIndex("apl/ch51253.itc", 0x34)
    LoadChrToIndex("apl/ch51254.itc", 0x35)
    LoadChrToIndex("apl/ch51219.itc", 0x36)
    LoadEffect(0x0, "event/ev12000.eff")
    LoadEffect(0x1, "battle/btgun00.eff")
    LoadEffect(0x2, "event/ev606_00.eff")
    LoadEffect(0x3, "event/eva00_00.eff")
    LoadEffect(0x4, "event/ev12002.eff")
    SoundLoad(860)
    SoundLoad(861)
    SoundLoad(2754)
    SoundLoad(2755)
    SoundLoad(4117)
    SoundLoad(3950)
    SoundLoad(3951)
    SoundLoad(3952)
    SetChrPos(0x101, 116000, 0, -700, 90)
    SetChrPos(0x102, 114900, 0, 1300, 90)
    SetChrPos(0x103, 114900, 0, -1200, 90)
    SetChrPos(0x104, 116000, 0, 600, 90)
    SetChrPos(0x109, 113800, 0, -700, 90)
    SetChrPos(0x105, 113800, 0, 600, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrChipByIndex(0x9, 0x2C)
    SetChrSubChip(0x9, 0x3)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, 171200, 0, 10000, 180)
    SetChrChipByIndex(0xA, 0x28)
    SetChrSubChip(0xA, 0x0)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)
    SetChrPos(0xA, 168700, 0, 12900, 270)
    OP_52(0xA, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xB, 0x28)
    SetChrSubChip(0xB, 0x2)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8000)
    SetChrPos(0xB, 167800, 0, 10200, 150)
    OP_52(0xB, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xC, 0x28)
    SetChrSubChip(0xC, 0x0)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8000)
    SetChrPos(0xC, 169900, 0, 11400, 170)
    OP_52(0xC, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xD, 0x28)
    SetChrSubChip(0xD, 0x1)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x8000)
    SetChrPos(0xD, 173000, 0, 10800, 305)
    OP_52(0xD, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xE, 0x28)
    SetChrSubChip(0xE, 0x1)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x8000)
    SetChrPos(0xE, 173400, 0, 12700, 90)
    OP_52(0xE, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xF, 0x28)
    SetChrSubChip(0xF, 0x3)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x8000)
    SetChrPos(0xF, 166300, 0, 12100, 90)
    OP_52(0xF, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x10, 0x1E)
    SetChrSubChip(0x10, 0x0)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x8000)
    SetChrPos(0x10, 178800, 0, 12500, 180)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x8000)
    SetChrChipByIndex(0x11, 0x22)
    SetChrSubChip(0x11, 0x0)
    SetChrPos(0x11, 170300, 0, 2300, 0)
    OP_52(0x11, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x12, 0x8000)
    SetChrChipByIndex(0x12, 0x23)
    SetChrSubChip(0x12, 0x0)
    SetChrPos(0x12, 171400, 0, 1500, 0)
    OP_52(0x12, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x13, 0x8000)
    SetChrChipByIndex(0x13, 0x24)
    SetChrSubChip(0x13, 0x0)
    SetChrPos(0x13, 169200, 0, 1100, 0)
    ClearChrFlags(0x1A, 0x80)
    SetChrFlags(0x1A, 0x8000)
    SetChrChipByIndex(0x1A, 0x27)
    SetChrSubChip(0x1A, 0x1)
    SetChrPos(0x1A, 171200, 0, 5400, 0)
    ClearChrFlags(0x1B, 0x80)
    SetChrFlags(0x1B, 0x8000)
    SetChrChipByIndex(0x1B, 0x27)
    SetChrSubChip(0x1B, 0x1)
    SetChrPos(0x1B, 167900, 0, 4800, 0)
    ClearChrFlags(0x1C, 0x80)
    SetChrFlags(0x1C, 0x8000)
    SetChrChipByIndex(0x1C, 0x27)
    SetChrSubChip(0x1C, 0x1)
    SetChrPos(0x1C, 172000, 0, 3900, 0)
    ClearChrFlags(0x1D, 0x80)
    SetChrFlags(0x1D, 0x8000)
    SetChrChipByIndex(0x1D, 0x27)
    SetChrSubChip(0x1D, 0x1)
    SetChrPos(0x1D, 169200, 0, 3700, 0)
    ClearChrFlags(0x1E, 0x80)
    SetChrFlags(0x1E, 0x8000)
    SetChrChipByIndex(0x1E, 0x27)
    SetChrSubChip(0x1E, 0x1)
    SetChrPos(0x1E, 173700, 0, 5300, 0)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 169200, 0, 13900, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x4, 0x0, 0x1A, 0x3, -100, 1100, 1150, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x4, 0x1, 0x1B, 0x3, -100, 1100, 1150, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x4, 0x2, 0x1C, 0x3, -100, 1100, 1150, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x4, 0x3, 0x1D, 0x3, -100, 1100, 1150, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x4, 0x4, 0x1E, 0x3, -100, 1100, 1150, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_68(121500, 1300, 0, 0)
    MoveCamera(35, 19, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(17500, 0)

    def lambda_4792():
        OP_97(0xFE, 0x2EE0, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_4792)
    Sleep(200)

    def lambda_47AF():
        OP_97(0x101, 0x2710, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_47AF)
    Sleep(150)

    def lambda_47CC():
        OP_97(0x102, 0x2710, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_47CC)
    Sleep(150)

    def lambda_47E9():
        OP_97(0x103, 0x2710, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_47E9)
    Sleep(150)

    def lambda_4806():
        OP_97(0x105, 0x2710, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_4806)
    Sleep(150)

    def lambda_4823():
        OP_97(0x109, 0x2710, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_4823)
    OP_68(126500, 1300, 0, 2000)
    SetCameraDistance(16500, 2000)
    BeginChrThread(0x20, 1, 0, 53)
    FadeToBright(1000, 0)
    StopBGM(0x7D0)
    WaitChrThread(0x104, 1)

    #C0074
    ChrTalk(
        0x104,
        "#5P#00305F……！\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x105, 0)

    #C0075
    ChrTalk(
        0x103,
        "#6P#00210F……啊………\x02",
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x101,
        "#00007F#6P什么——！？\x02",
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7582", 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x246), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    StopSound(863, 2000, 100)
    OP_68(146500, 1300, 0, 3000)
    Sleep(2000)
    FadeToDark(500, 0, -1)
    OP_0D()
    OP_68(169500, 900, 11500, 0)
    MoveCamera(65, 15, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(14000, 0)
    MoveCamera(50, 30, 0, 9000)
    SetCameraDistance(17000, 9000)
    FadeToBright(2000, 0)
    OP_6F(0x79)
    Fade(1000)
    OP_68(170500, 700, 9000, 0)
    MoveCamera(0, 17, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(14000, 0)
    SetCameraDistance(21000, 4000)
    OP_6F(0x79)
    Sleep(1000)
    Fade(500)
    OP_68(171160, 900, 8200, 0)
    MoveCamera(45, 17, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(19500, 0)
    BeginChrThread(0xF, 3, 0, 52)
    OP_68(171200, 900, 7200, 1500)
    OP_0D()
    OP_6F(0x79)

    def lambda_49D2():
        OP_A6(0xFE, 0x0, 0x32, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_49D2)
    Sleep(500)

    #C0077
    ChrTalk(
        0x9,
        "#5P#50W#2S……呜哇……咳咳……\x02",
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0x9,
        (
            "#5P#50W#2S『赤色星座』……\x01",
            "……你们为何会在这里……\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0x11,
        (
            "#11P#04504F这是契约中规定的工作内容。\x02\x03",

            "#04502F毁掉对空雷达的那些人\x01",
            "已经被我们送去见女神了。\x02\x03",

            "你们也安心上路吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0x9,
        "#5P#60W#2S……真………真是不甘………\x02",
    )

    CloseMessageWindow()

    def lambda_4AEA():
        OP_A6(0xFE, 0x0, 0x32, 0x2EE, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_4AEA)
    Sleep(500)
    Fade(250)
    Sound(514, 0, 100, 0)
    SetChrChipByIndex(0x9, 0x28)
    SetChrSubChip(0x9, 0x2)
    OP_52(0x9, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(1000)

    #C0081
    ChrTalk(
        0x11,
        (
            "#11P#04504F谢莉，\x01",
            "剩下那个也可以杀掉。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x12, 0x11, 500)

    #C0082
    ChrTalk(
        0x12,
        "#04602F#11P嘿嘿，真的吗？\x02",
    )

    CloseMessageWindow()

    #N0083
    NpcTalk(
        0x10,
        "声音",
        "#2S呜哇……！\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x10, 3, 0, 45)
    OP_68(178800, 1100, 9750, 3000)
    MoveCamera(13, 13, 0, 3000)
    SetCameraDistance(19000, 3000)
    OP_92(0x12, 0x2BA70, 0x1770, 0x1F4)

    def lambda_4BC9():
        OP_95(0xFE, 178800, 0, 6000, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_4BC9)
    Sleep(1000)
    BeginChrThread(0x1E, 3, 0, 44)
    WaitChrThread(0x12, 1)

    def lambda_4BF0():
        OP_95(0xFE, 178800, 0, 7000, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_4BF0)
    WaitChrThread(0x12, 1)
    OP_6F(0x79)
    SetChrChipByIndex(0x1A, 0x24)
    SetChrSubChip(0x1A, 0x0)
    SetChrPos(0x1A, 170200, 0, 5400, 90)
    SetChrChipByIndex(0x1C, 0x24)
    SetChrSubChip(0x1C, 0x0)
    SetChrPos(0x1C, 171000, 0, 3900, 90)
    Sound(859, 0, 100, 0)
    Sound(802, 0, 100, 0)
    PlayEffect(0x3, 0x0, 0x12, 0x3, 600, 1000, 100, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrFlags(0x12, 0x2)
    SetChrFlags(0x12, 0x10)
    SetChrFlags(0x12, 0x20)
    SetChrChipByIndex(0x12, 0x2D)
    SetChrSubChip(0x12, 0x0)
    Sleep(500)
    StopEffect(0x0, 0x2)
    OP_C9(0x0, 0x80000000)

    #C0084
    ChrTalk(
        0x12,
        (
            "#12P#04611F#3950V#30W呵呵，怎么啦？\x02\x03",

            "#04602F#3951V我不会让其他人插手的，\x01",
            "你不用客气，尽管放马过来吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xF6F)
    OP_C9(0x1, 0x80000000)

    #C0085
    ChrTalk(
        0x10,
        "#5P呜、呜呜……\x02",
    )

    CloseMessageWindow()
    EndChrThread(0x10, 0x3)
    Sleep(500)
    SetChrChipByIndex(0x10, 0x20)
    SetChrSubChip(0x10, 0x0)
    Sleep(100)
    Sound(531, 0, 100, 0)
    SetChrSubChip(0x10, 0x1)
    Sleep(100)
    SetChrSubChip(0x10, 0x2)
    OP_82(0xC8, 0x0, 0xBB8, 0x1F4)

    #C0086
    ChrTalk(
        0x10,
        "#4S#5P呜哇啊啊啊啊！！！\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x11, 3, 0, 42)
    BeginChrThread(0x10, 3, 0, 41)
    BeginChrThread(0x12, 3, 0, 43)
    WaitChrThread(0x10, 3)
    WaitChrThread(0x12, 3)
    Sound(859, 0, 100, 0)
    PlayEffect(0x3, 0x0, 0x12, 0x3, 300, 900, 800, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    StopEffect(0x0, 0x2)

    #C0087
    ChrTalk(
        0x10,
        "#12P啊——\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(14000, 500)
    Sleep(200)
    Sound(802, 0, 100, 0)
    SetChrSubChip(0x12, 0x1)
    OP_6F(0x79)
    OP_C9(0x0, 0x80000000)

    #C0088
    ChrTalk(
        0x12,
        (
            "#04609F#3952V#5P#40W呵呵，\x01",
            "要说再见啦——\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xF70)
    OP_57(0x0)
    OP_5A()
    OP_82(0xC8, 0x0, 0xBB8, 0x1F4)

    #C0089
    ChrTalk(
        0x104,
        "#00310F#2754V#4S#6P#N快住手！！\x02",
    )

    CloseMessageWindow()
    OP_24(0xAC2)
    OP_C9(0x1, 0x80000000)
    OP_63(0x12, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Fade(500)
    OP_68(158000, 1100, 2500, 0)
    MoveCamera(43, 21, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(15500, 0)
    SetChrChipByIndex(0x1A, 0x24)
    SetChrSubChip(0x1A, 0x0)
    SetChrChipByIndex(0x1B, 0x24)
    SetChrSubChip(0x1B, 0x0)
    SetChrChipByIndex(0x1C, 0x24)
    SetChrSubChip(0x1C, 0x0)
    SetChrChipByIndex(0x1D, 0x24)
    SetChrSubChip(0x1D, 0x0)
    SetChrChipByIndex(0x1E, 0x24)
    SetChrSubChip(0x1E, 0x0)
    SetChrPos(0x1A, 171200, 0, 5400, 0)
    SetChrPos(0x1B, 168400, 0, 4800, 0)
    SetChrPos(0x1C, 172000, 0, 3900, 0)
    SetChrPos(0x1D, 169700, 0, 3700, 0)
    SetChrPos(0x1E, 173200, 0, 5300, 0)

    def lambda_4F47():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1A, 2, lambda_4F47)

    def lambda_4F54():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1B, 2, lambda_4F54)

    def lambda_4F61():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1C, 2, lambda_4F61)

    def lambda_4F6E():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1D, 2, lambda_4F6E)

    def lambda_4F7B():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1E, 2, lambda_4F7B)
    SetChrSubChip(0x12, 0x2)
    SetChrPos(0x101, 150000, 0, 2000, 90)
    SetChrPos(0x102, 150000, 0, 4000, 90)
    SetChrPos(0x103, 150000, 0, 3800, 90)
    SetChrPos(0x104, 150000, 0, 2600, 90)
    SetChrPos(0x109, 150000, 0, 5100, 90)
    SetChrPos(0x105, 150000, 0, 4600, 90)
    OP_68(166000, 1100, 4500, 4000)
    MoveCamera(43, 16, 0, 4000)
    SetCameraDistance(16500, 4000)

    def lambda_5017():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_5017)

    def lambda_5024():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_5024)
    BeginChrThread(0x104, 3, 0, 46)
    Sleep(600)
    BeginChrThread(0x101, 3, 0, 47)
    Sleep(200)
    BeginChrThread(0x109, 3, 0, 49)

    def lambda_5049():
        OP_96(0xFE, 0x28E4C, 0x0, 0xA28, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_5049)
    Sleep(400)
    BeginChrThread(0x102, 3, 0, 48)
    Sleep(400)
    BeginChrThread(0x105, 3, 0, 50)
    Sleep(400)
    BeginChrThread(0x103, 3, 0, 51)

    def lambda_507E():
        OP_96(0xFE, 0x29234, 0x0, 0x5DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_507E)
    Sleep(1600)

    #C0090
    ChrTalk(
        0x12,
        "#04605F#12P哎呀，有人来搅局呢。\x02",
    )

    WaitChrThread(0x103, 3)
    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    WaitChrThread(0x13, 1)

    #C0091
    ChrTalk(
        0x13,
        "#11P少爷……\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x11, 1)

    #C0092
    ChrTalk(
        0x11,
        "#04504F#11P呵呵，你们来迟了。\x02",
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x104,
        (
            "#6P#00311F#30W叔叔……谢莉……\x02\x03",

            "#30W……你们怎能在这种地方……\x01",
            "做出这种事来……！\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x102,
        "#5P#00108F不……不行了……\x02",
    )

    CloseMessageWindow()

    def lambda_517B():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_517B)
    Sleep(50)

    def lambda_518B():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_518B)

    #C0095
    ChrTalk(
        0x105,
        (
            "#5P#10303F……看来所有人\x01",
            "都已经断气了。\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0x103,
        "#6P#00210F…………呜………………\x02",
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0x109,
        "#10110F#12P唔……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x11, 500)
    Sleep(300)

    #C0098
    ChrTalk(
        0x101,
        "#6P#00015F#30W……你们为何……\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    OP_82(0xC8, 0x0, 0xBB8, 0x1F4)

    #C0099
    ChrTalk(
        0x101,
        "#6P#00007F#4S为何要做出这种惨无人道的事！\x02",
    )

    CloseMessageWindow()

    def lambda_5273():
        TurnDirection(0xFE, 0x11, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_5273)

    def lambda_5280():
        TurnDirection(0xFE, 0x11, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_5280)

    #C0100
    ChrTalk(
        0x11,
        (
            "#04504F#11P我刚才不是说过了吗？这只是工作。\x02\x03",

            "处死这群对帝国宰相与皇族成员\x01",
            "心怀不轨的恐怖分子……\x02\x03",

            "#04502F这就是帝国政府此次\x01",
            "向我们交托的任务。\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0x101,
        "#6P#00011F……！？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)

    def lambda_5344():
        TurnDirection(0xFE, 0x11, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_5344)
    Sound(812, 0, 100, 0)
    Sleep(100)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)
    TurnDirection(0x105, 0x11, 500)

    #C0102
    ChrTalk(
        0x102,
        "#5P#00107F难、难道……\x02",
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0x12,
        (
            "#04609F#12P嗯，我们手上还有\x01",
            "帝国政府的正式委托书哦～\x02\x03",

            "#04611F只要有这东西，\x01",
            "你们就不能干涉我们了吧～？\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0104
    ChrTalk(
        0x109,
        "#10108F#5P这、这……！\x02",
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0x102,
        (
            "#5P#00108F自治州法第十九条第三项……\x02\x03",

            "#00110F帝国、共和国政府在克洛斯贝尔\x01",
            "拥有执行公务权……根据这条法令，\x01",
            "你们的行为是合法的……\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0x11,
        (
            "#04504F呵呵，正是如此。\x02\x03",

            "#04500F换句话说，在此次事件中，\x01",
            "我们就是帝国政府的代理人……\x02\x03",

            "也就是合法的正式处刑人。\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0x101,
        "#6P#00010F唔……！\x02",
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0x105,
        "#5P#10301F准备得真周到呢……\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    OP_82(0xC8, 0x0, 0xBB8, 0x1F4)
    OP_C9(0x0, 0x80000000)

    #C0109
    ChrTalk(
        0x104,
        "#6P#00310F#2755V#4S#13A叔叔！！\x02",
    )
    #Auto

    Sleep(500)
    OP_68(167150, 1100, 2600, 1000)
    MoveCamera(34, 19, 0, 1000)
    SetCameraDistance(14000, 1000)

    def lambda_55AA():
        OP_95(0xFE, 166800, 0, 2600, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_55AA)
    WaitChrThread(0x104, 1)
    Sound(802, 0, 100, 0)
    Fade(100)
    Sound(811, 0, 100, 0)
    SetChrFlags(0x104, 0x2)
    SetChrFlags(0x104, 0x10)
    SetChrFlags(0x104, 0x20)
    SetChrChipByIndex(0x104, 0x30)
    SetChrSubChip(0x104, 0x0)
    SetChrFlags(0x11, 0x2)
    SetChrFlags(0x11, 0x10)
    SetChrFlags(0x11, 0x20)
    SetChrChipByIndex(0x11, 0x31)
    SetChrSubChip(0x11, 0x0)

    def lambda_5607():

        label("loc_5607")

        TurnDirection(0xFE, 0x104, 500)
        Yield()
        Jump("loc_5607")

    QueueWorkItem2(0x101, 2, lambda_5607)

    def lambda_5619():

        label("loc_5619")

        TurnDirection(0xFE, 0x104, 500)
        Yield()
        Jump("loc_5619")

    QueueWorkItem2(0x102, 2, lambda_5619)

    def lambda_562B():

        label("loc_562B")

        TurnDirection(0xFE, 0x104, 500)
        Yield()
        Jump("loc_562B")

    QueueWorkItem2(0x103, 2, lambda_562B)

    def lambda_563D():

        label("loc_563D")

        TurnDirection(0xFE, 0x104, 500)
        Yield()
        Jump("loc_563D")

    QueueWorkItem2(0x109, 2, lambda_563D)

    def lambda_564F():

        label("loc_564F")

        TurnDirection(0xFE, 0x104, 500)
        Yield()
        Jump("loc_564F")

    QueueWorkItem2(0x105, 2, lambda_564F)

    def lambda_5661():

        label("loc_5661")

        TurnDirection(0xFE, 0x104, 500)
        Yield()
        Jump("loc_5661")

    QueueWorkItem2(0x13, 2, lambda_5661)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_6F(0x79)
    OP_C9(0x1, 0x80000000)

    #C0110
    ChrTalk(
        0x104,
        (
            "#6P#00307F为什么要痛下杀手！？\x01",
            "为什么要把他们都杀掉！？\x02\x03",

            "你们完全有能力在不下杀手的\x01",
            "前提下让他们丧失战斗力吧！？\x02\x03",

            "既然如此，为什么非要……！\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0x11,
        "#11P#04501F……………………………………\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(13000, 800)
    OP_57(0x0)
    OP_5A()
    Fade(300)
    Sound(802, 0, 100, 0)
    Sound(3824, 255, 100, 0)    #voice#Sigmund
    SetChrChipByIndex(0x11, 0x32)
    SetChrSubChip(0x11, 0x0)
    OP_6F(0x79)
    Sleep(150)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0xA)
    Sound(534, 0, 100, 0)
    SetChrSubChip(0x11, 0x1)
    Sleep(60)
    Sound(815, 0, 100, 0)
    SetChrSubChip(0x11, 0x2)
    OP_82(0xC8, 0xC8, 0xBB8, 0x12C)
    OP_68(165800, 1100, 2600, 500)
    SetCameraDistance(14500, 500)
    SetChrChipByIndex(0x104, 0x33)
    SetChrSubChip(0x104, 0x2)
    Sound(809, 0, 100, 0)

    def lambda_5842():
        OP_9D(0xFE, 0x28104, 0x0, 0x8FC, 0x12C, 0x5DC)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_5842)
    WaitChrThread(0x104, 1)
    Sound(862, 0, 100, 0)
    CancelBlur(0)
    SetChrChipByIndex(0x1F, 0x33)
    SetChrSubChip(0x1F, 0x0)
    SetChrPos(0x1F, 164400, -50, 2800, 0)
    OP_52(0x1F, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x1F, 0x80)
    SetChrFlags(0x1F, 0x8000)
    SetChrSubChip(0x104, 0x0)
    OP_52(0x104, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x104, 0x1)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x103, 0x2)
    EndChrThread(0x109, 0x2)
    EndChrThread(0x105, 0x2)
    EndChrThread(0x13, 0x2)

    def lambda_58F4():
        OP_A6(0xFE, 0x0, 0x32, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_58F4)
    Sleep(50)
    Sound(811, 0, 100, 0)
    Sleep(150)
    #Sound(2764, 255, 100, 0)    #voice#Randy

    #C0112
    ChrTalk(
        0x104,
        "#6P#8A呜哇……！\x02",
    )
    #Auto

    CloseMessageWindow()

    def lambda_5935():
        OP_95(0xFE, 164000, 0, 3900, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5935)
    Sleep(100)

    def lambda_5952():
        OP_95(0xFE, 162800, 0, 3000, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5952)
    WaitChrThread(0x101, 1)

    def lambda_5970():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5970)
    WaitChrThread(0x103, 1)
    TurnDirection(0x103, 0x104, 500)

    #C0113
    ChrTalk(
        0x101,
        "#00007F#5P兰迪……！\x02",
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0x109,
        "#5P#10111F前辈！\x02",
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0x103,
        "#5P#00201F兰迪前辈……！\x02",
    )

    CloseMessageWindow()
    Sound(802, 0, 100, 0)

    def lambda_59DC():
        OP_A6(0xFE, 0x0, 0x32, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_59DC)
    Sleep(500)
    SetChrSubChip(0x104, 0x1)
    Sleep(500)
    Fade(250)
    SetChrChipByIndex(0x11, 0x22)
    SetChrSubChip(0x11, 0x0)
    ClearChrFlags(0x11, 0x2)
    ClearChrFlags(0x11, 0x10)
    ClearChrFlags(0x11, 0x20)
    OP_0D()

    #C0116
    ChrTalk(
        0x11,
        (
            "#04503F#11P我已经说过了吧？\x01",
            "我们接受的任务是『处刑』。\x02\x03",

            "#04501F而且，不过是这种程度的歼灭战而已，\x01",
            "对你来说，并不是什么稀罕事吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0x104,
        "#6P#00310F………唔…………\x02",
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0x11,
        (
            "#04503F#11P归根到底，如果你们能\x01",
            "早点抓住这些家伙，也就不会演变\x01",
            "成这种结局了。\x02\x03",

            "#04502F同时还能阻止『铁血』利用这个\x01",
            "结局来达成政治上的目的。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5B53():
        TurnDirection(0x101, 0x11, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_5B53)
    Sleep(50)

    def lambda_5B63():
        TurnDirection(0x102, 0x11, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_5B63)
    Sleep(50)

    def lambda_5B73():
        TurnDirection(0x109, 0x11, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_5B73)
    Sleep(50)

    def lambda_5B83():
        TurnDirection(0x103, 0x11, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_5B83)
    Sleep(50)

    def lambda_5B93():
        TurnDirection(0x105, 0x11, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_5B93)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x105, 0)
    OP_82(0x32, 0x0, 0xBB8, 0xC8)

    #C0119
    ChrTalk(
        0x101,
        "#00007F#5P！！\x02",
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0x102,
        "#5P#N#00108F什么……难道说……？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0121
    ChrTalk(
        0x11,
        (
            "#04504F#11P呵呵，好吧，那就大发慈悲，\x01",
            "放过最后一只好了。\x02\x03",

            "#04500F谢莉，放了他。\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0x12,
        (
            "#04606F哎？真浪费啊。\x02\x03",

            "#04600F呼，算啦，反正我也\x01",
            "没什么兴趣和这种小杂鱼玩。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(174300, 1100, 7300, 0)
    MoveCamera(47, 21, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(18500, 0)
    ClearChrFlags(0x12, 0x2)
    ClearChrFlags(0x12, 0x10)
    ClearChrFlags(0x12, 0x20)
    SetChrChipByIndex(0x12, 0x23)
    SetChrSubChip(0x12, 0x0)
    SetChrChipByIndex(0x10, 0x1E)
    SetChrSubChip(0x10, 0x0)
    OP_A7(0x10, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    SetChrPos(0x10, 177000, 0, 6500, 180)

    def lambda_5D1C():

        label("loc_5D1C")

        TurnDirection(0xFE, 0x12, 500)
        Yield()
        Jump("loc_5D1C")

    QueueWorkItem2(0x109, 2, lambda_5D1C)

    def lambda_5D2E():

        label("loc_5D2E")

        TurnDirection(0xFE, 0x12, 500)
        Yield()
        Jump("loc_5D2E")

    QueueWorkItem2(0x102, 2, lambda_5D2E)

    def lambda_5D40():

        label("loc_5D40")

        TurnDirection(0xFE, 0x12, 500)
        Yield()
        Jump("loc_5D40")

    QueueWorkItem2(0x105, 2, lambda_5D40)
    OP_0D()
    OP_68(169300, 1100, 7600, 3500)
    SetCameraDistance(20500, 3500)

    def lambda_5D6D():
        OP_9E(0xFE, 0x2B368, 0x1C84, 0x15F90, 0x1388, 0x3)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_5D6D)

    def lambda_5D88():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_5D88)
    Sound(802, 0, 100, 0)
    WaitChrThread(0x10, 1)

    def lambda_5D9F():
        OP_98(0xFE, 0xFFFFE890, 0x0, 0x12C, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_5D9F)

    def lambda_5DB9():
        OP_98(0xFE, 0xFFFFE890, 0x0, 0x12C, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_5DB9)
    WaitChrThread(0x10, 1)
    WaitChrThread(0x12, 1)
    OP_52(0x10, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TurnDirection(0x10, 0x12, 0)
    SetChrChipByIndex(0x10, 0x21)
    SetChrSubChip(0x10, 0x0)
    Sound(809, 0, 100, 0)
    Sound(811, 0, 100, 0)

    def lambda_5E01():
        OP_9D(0xFE, 0x28AC8, 0x0, 0x1E14, 0x2BC, 0x7D0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_5E01)
    WaitChrThread(0x10, 1)
    Sound(862, 0, 80, 0)
    OP_82(0x64, 0x64, 0xBB8, 0x12C)
    OP_93(0x10, 0x10E, 0x0)
    SetChrChipByIndex(0x10, 0x28)
    SetChrSubChip(0x10, 0x3)
    OP_52(0x10, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x578), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x578), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(300)

    #C0123
    ChrTalk(
        0x12,
        (
            "#11P#04612F来，接住，\x01",
            "可别让他跑了哦～\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0x10, 0x2)
    SetChrFlags(0x10, 0x10)
    SetChrFlags(0x10, 0x20)
    SetChrChipByIndex(0x10, 0x34)
    SetChrSubChip(0x10, 0x0)

    def lambda_5EAF():
        OP_A6(0xFE, 0x0, 0x32, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_5EAF)

    #C0124
    ChrTalk(
        0x10,
        "#5P呜、呜啊啊……\x02",
    )

    CloseMessageWindow()

    def lambda_5EDF():
        OP_96(0xFE, 0x288D4, 0x0, 0x1964, 0x1388, 0x1)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_5EDF)
    WaitChrThread(0x109, 1)

    def lambda_5EFD():
        OP_96(0xFE, 0x28EB0, 0x0, 0x1D4C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_5EFD)
    WaitChrThread(0x109, 1)

    def lambda_5F1B():

        label("loc_5F1B")

        TurnDirection(0xFE, 0x12, 500)
        Yield()
        Jump("loc_5F1B")

    QueueWorkItem2(0x109, 2, lambda_5F1B)

    #C0125
    ChrTalk(
        0x109,
        "#6P#10110F唔……！\x02",
    )

    CloseMessageWindow()
    OP_68(165800, 1500, 2600, 2000)
    MoveCamera(34, 19, 0, 2000)
    OP_6E(650, 2000)
    SetCameraDistance(14500, 2000)
    OP_6F(0x79)

    #C0126
    ChrTalk(
        0x101,
        "#00013F#6P………………………………\x02",
    )

    CloseMessageWindow()
    OP_93(0x11, 0x2D, 0x1F4)
    Sleep(150)

    #C0127
    ChrTalk(
        0x11,
        (
            "#6P#04504F好了，我们收队吧。\x02\x03",

            "#04512F马上就能收到报酬了，\x01",
            "今晚就尽情享乐一番吧。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5FFD():
        TurnDirection(0x13, 0x11, 500)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_5FFD)
    Sleep(50)

    def lambda_600D():
        TurnDirection(0x1A, 0x11, 500)
        ExitThread()

    QueueWorkItem(0x1A, 0, lambda_600D)
    Sleep(50)

    def lambda_601D():
        TurnDirection(0x1B, 0x11, 500)
        ExitThread()

    QueueWorkItem(0x1B, 0, lambda_601D)
    Sleep(50)

    def lambda_602D():
        TurnDirection(0x1C, 0x11, 500)
        ExitThread()

    QueueWorkItem(0x1C, 0, lambda_602D)
    Sleep(50)

    def lambda_603D():
        TurnDirection(0x1D, 0x11, 500)
        ExitThread()

    QueueWorkItem(0x1D, 0, lambda_603D)
    Sleep(50)

    def lambda_604D():
        TurnDirection(0x1E, 0x11, 500)
        ExitThread()

    QueueWorkItem(0x1E, 0, lambda_604D)
    WaitChrThread(0x13, 0)
    WaitChrThread(0x1A, 0)
    WaitChrThread(0x1B, 0)
    WaitChrThread(0x1C, 0)
    WaitChrThread(0x1D, 0)
    WaitChrThread(0x1E, 0)
    Sleep(100)
    SetMessageWindowPos(300, 40, -1, -1)
    SetChrName("众猎兵")
    OP_82(0x64, 0x0, 0xBB8, 0x1F4)

    #A0128
    AnonymousTalk(
        0xFF,
        "#4S明白！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    #C0129
    ChrTalk(
        0x12,
        "#11P#N#04609F那就再见啦～！\x02",
    )

    CloseMessageWindow()
    OP_93(0x13, 0x10E, 0x1F4)

    #C0130
    ChrTalk(
        0x13,
        "#11P少爷，我们先告辞了。\x02",
    )

    CloseMessageWindow()
    OP_93(0x1B, 0x10E, 0x1F4)

    #N0131
    NpcTalk(
        0x1B,
        "猎兵扎克斯",
        (
            "#11P再见啦，\x01",
            "兰道夫队长。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_6129():

        label("loc_6129")

        TurnDirection(0xFE, 0x11, 500)
        Yield()
        Jump("loc_6129")

    QueueWorkItem2(0x101, 2, lambda_6129)

    def lambda_613B():

        label("loc_613B")

        TurnDirection(0xFE, 0x11, 500)
        Yield()
        Jump("loc_613B")

    QueueWorkItem2(0x102, 2, lambda_613B)

    def lambda_614D():

        label("loc_614D")

        TurnDirection(0xFE, 0x11, 500)
        Yield()
        Jump("loc_614D")

    QueueWorkItem2(0x103, 2, lambda_614D)

    def lambda_615F():

        label("loc_615F")

        TurnDirection(0xFE, 0x11, 500)
        Yield()
        Jump("loc_615F")

    QueueWorkItem2(0x105, 2, lambda_615F)
    OP_93(0x11, 0xB4, 0x1F4)
    OP_68(165800, 1500, -400, 5000)
    MoveCamera(23, 13, 0, 5000)

    def lambda_6194():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFCD38, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_6194)
    Sleep(1300)

    def lambda_61B1():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFCD38, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_61B1)

    def lambda_61CB():
        OP_97(0x1A, 0x0, 0x0, 0xFFFFCD38, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 0, lambda_61CB)
    Sleep(100)

    def lambda_61E8():
        OP_97(0x1B, 0x0, 0x0, 0xFFFFCD38, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1B, 0, lambda_61E8)
    Sleep(100)

    def lambda_6205():
        OP_97(0x1C, 0x0, 0x0, 0xFFFFCD38, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 0, lambda_6205)
    Sleep(100)

    def lambda_6222():
        OP_97(0x1D, 0x0, 0x0, 0xFFFFCD38, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 0, lambda_6222)
    Sleep(100)

    def lambda_623F():
        OP_97(0x1E, 0x0, 0x0, 0xFFFFCD38, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 0, lambda_623F)

    def lambda_6259():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFCD38, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_6259)
    WaitChrThread(0x11, 1)
    WaitChrThread(0x13, 1)
    WaitChrThread(0x12, 1)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x103, 0x2)
    EndChrThread(0x109, 0x2)
    EndChrThread(0x105, 0x2)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x1A, 0x80)
    SetChrFlags(0x1B, 0x80)
    SetChrFlags(0x1C, 0x80)
    SetChrFlags(0x1D, 0x80)
    SetChrFlags(0x1E, 0x80)
    OP_68(164100, 1000, 2300, 2000)
    MoveCamera(23, 23, 0, 2000)
    SetCameraDistance(14000, 2000)
    Sleep(1750)

    def lambda_62E3():
        OP_A6(0xFE, 0x0, 0x32, 0x4E2, 0xBB8)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_62E3)
    Sleep(500)
    Fade(250)
    SetChrChipByIndex(0x104, 0x36)
    SetChrSubChip(0x104, 0x3)
    SetChrFlags(0x104, 0x1)
    OP_52(0x104, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x1F, 0x80)
    OP_0D()
    Sleep(500)
    Fade(500)
    Sound(812, 0, 100, 0)
    SetChrChipByIndex(0x104, 0x35)
    SetChrSubChip(0x104, 0x0)

    def lambda_6338():
        OP_A6(0xFE, 0x0, 0x32, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_6338)
    OP_0D()
    Sleep(800)

    #C0132
    ChrTalk(
        0x104,
        (
            "#5P#00313F#60W………开什么玩笑…………\x01",
            "……我到底是为了什么……为了什么才………\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x104, 2)
    SetChrSubChip(0x104, 0x1)
    SetCameraDistance(50000, 4000)
    Sleep(500)
    OP_82(0xC8, 0x0, 0xBB8, 0xBB8)
    OP_C9(0x0, 0x80000000)
    #Sound(4117, 255, 100, 0)    #voice#Randy

    #C0133
    ChrTalk(
        0x104,
        "#5P#5S#20A#40W啊啊啊啊啊啊啊啊！！\x02",
    )
    #Auto

    Sleep(1000)
    OP_C9(0x1, 0x80000000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    ClearChrFlags(0x104, 0x2)
    ClearChrFlags(0x104, 0x10)
    ClearChrFlags(0x104, 0x20)
    OP_24(0x35C)
    OP_24(0x35D)
    Sleep(1000)
    SetScenarioFlags(0x22, 1)
    NewScene("m0200", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_40_41DC end

    def Function_41_643E(): pass

    label("Function_41_643E")

    OP_82(0x64, 0x64, 0xBB8, 0x384)

    def lambda_6454():
        OP_A6(0xFE, 0x0, 0x1E, 0x2BC, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_6454)
    PlayEffect(0x1, 0xFF, 0xFE, 0x3, 100, 1000, 900, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0xFE, 0x3, 100, 1000, 900, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0xFE, 0x3, 100, 1000, 900, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0xFE, 0x3, 100, 1000, 900, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0xFE, 0x3, 100, 1000, 900, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0xFE, 0x3, 100, 1000, 900, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0xFE, 0x3, 100, 1000, 900, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0xFE, 0x3, 100, 1000, 900, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0xFE, 0x3, 100, 1000, 900, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    OP_68(178300, 1100, 5650, 1300)
    MoveCamera(13, 13, -15, 1300)
    SetCameraDistance(19500, 1300)
    SetChrChipByIndex(0x10, 0x1F)
    SetChrSubChip(0x10, 0x0)

    def lambda_66A4():
        OP_95(0xFE, 178800, 0, 8500, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_66A4)
    WaitChrThread(0x10, 1)
    SetChrChipByIndex(0x10, 0x20)
    SetChrSubChip(0x10, 0x0)
    Sleep(100)
    SetChrSubChip(0x10, 0x1)
    Sleep(100)
    SetChrSubChip(0x10, 0x2)
    Sleep(100)
    OP_82(0x64, 0x64, 0xBB8, 0x1F4)

    def lambda_66EC():
        OP_A6(0xFE, 0x0, 0x1E, 0x190, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_66EC)
    PlayEffect(0x1, 0xFF, 0xFE, 0x3, 100, 1000, 900, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0xFE, 0x3, 100, 1000, 900, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0xFE, 0x3, 100, 1000, 900, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0xFE, 0x3, 100, 1000, 900, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0xFE, 0x3, 100, 1000, 900, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    SetChrChipByIndex(0x10, 0x1F)
    SetChrSubChip(0x10, 0x0)

    def lambda_682F():
        OP_95(0xFE, 177200, 0, 6600, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_682F)
    WaitChrThread(0x10, 1)
    SetChrChipByIndex(0x10, 0x20)
    SetChrSubChip(0x10, 0x0)
    Sleep(100)
    SetChrSubChip(0x10, 0x1)
    Sleep(100)
    SetChrSubChip(0x10, 0x2)
    Sleep(100)
    OP_82(0x64, 0x64, 0xBB8, 0x1F4)

    def lambda_6877():
        OP_A6(0xFE, 0x0, 0x1E, 0x190, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_6877)
    PlayEffect(0x1, 0xFF, 0xFE, 0x3, 100, 1000, 900, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0xFE, 0x3, 100, 1000, 900, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0xFE, 0x3, 100, 1000, 900, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0xFE, 0x3, 100, 1000, 900, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0xFE, 0x3, 100, 1000, 900, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    SetChrFlags(0xFE, 0x20)
    OP_93(0x10, 0xA0, 0x12C)
    ClearChrFlags(0xFE, 0x20)
    OP_82(0x64, 0x64, 0xBB8, 0x1F4)

    def lambda_69D4():
        OP_A6(0xFE, 0x0, 0x1E, 0x190, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_69D4)
    PlayEffect(0x1, 0xFF, 0xFE, 0x3, 100, 1000, 900, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0xFE, 0x3, 100, 1000, 900, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0xFE, 0x3, 100, 1000, 900, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0xFE, 0x3, 100, 1000, 900, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0xFE, 0x3, 100, 1000, 900, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(300)
    Return()

    # Function_41_643E end

    def Function_42_6B0B(): pass

    label("Function_42_6B0B")

    Sleep(100)
    Sound(860, 2, 100, 0)
    Sound(861, 2, 100, 0)
    PlayEffect(0x2, 0xFF, 0xFF, 0x0, 178800, 0, 7000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x2, 0xFF, 0xFF, 0x0, 178100, 0, 7500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x2, 0xFF, 0xFF, 0x0, 179200, 0, 7900, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x2, 0xFF, 0xFF, 0x0, 178600, 0, 7200, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    StopSound(860, 500, 100)
    StopSound(861, 500, 100)
    Sleep(200)
    PlayEffect(0x2, 0xFF, 0xFF, 0x0, 178200, 0, 6800, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1300)
    Sound(860, 2, 100, 0)
    Sound(861, 2, 100, 0)
    PlayEffect(0x2, 0xFF, 0xFF, 0x0, 179000, 0, 3000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x2, 0xFF, 0xFF, 0x0, 178500, 0, 3700, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x2, 0xFF, 0xFF, 0x0, 178800, 0, 3200, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    StopSound(860, 500, 100)
    StopSound(861, 500, 100)
    Sleep(800)
    Sound(860, 2, 100, 0)
    Sound(861, 2, 100, 0)
    PlayEffect(0x2, 0xFF, 0xFF, 0x0, 174500, 0, 1500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x2, 0xFF, 0xFF, 0x0, 175300, 0, 2000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x2, 0xFF, 0xFF, 0x0, 175000, 0, 2300, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x2, 0xFF, 0xFF, 0x0, 176600, 0, 1300, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x2, 0xFF, 0xFF, 0x0, 177800, 0, 1000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x2, 0xFF, 0xFF, 0x0, 178800, 0, 500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x2, 0xFF, 0xFF, 0x0, 178300, 0, 900, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    StopSound(860, 500, 100)
    StopSound(861, 500, 100)
    Return()

    # Function_42_6B0B end

    def Function_43_6EBA(): pass

    label("Function_43_6EBA")

    SetCameraDistance(20500, 500)
    ClearChrFlags(0x12, 0x2)
    ClearChrFlags(0x12, 0x10)
    SetChrChip(0x0, 0xFE, 0x1E, 0xC8)
    SetChrChipByIndex(0x12, 0x2E)
    SetChrSubChip(0x12, 0x3)
    Sound(844, 0, 100, 0)

    def lambda_6EE8():
        OP_9D(0xFE, 0x2BA70, 0x0, 0xC80, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_6EE8)
    WaitChrThread(0x12, 1)
    SetChrSubChip(0x12, 0x1)
    Sleep(100)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    SetChrSubChip(0x12, 0x0)
    Sleep(1500)
    SetChrChip(0x0, 0xFE, 0x1E, 0xC8)
    SetChrSubChip(0x12, 0x3)

    def lambda_6F2B():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_6F2B)
    Sound(844, 0, 100, 0)

    def lambda_6F3E():
        OP_9D(0xFE, 0x2A9A4, 0x0, 0x5DC, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_6F3E)
    WaitChrThread(0x12, 1)
    SetChrSubChip(0x12, 0x1)
    Sleep(200)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    SetChrSubChip(0x12, 0x0)
    Sleep(500)
    SetChrChip(0x0, 0xFE, 0x1E, 0xC8)
    SetChrSubChip(0x12, 0x3)

    def lambda_6F81():
        OP_93(0xFE, 0x154, 0x1F4)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_6F81)
    Sound(844, 0, 100, 0)

    def lambda_6F94():
        OP_9D(0xFE, 0x2BA70, 0x0, 0x1F4, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_6F94)
    WaitChrThread(0x12, 1)
    SetChrSubChip(0x12, 0x1)
    Sleep(100)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    SetChrSubChip(0x12, 0x0)
    Sleep(300)
    OP_68(177000, 1100, 7100, 1000)
    MoveCamera(27, 13, 5, 1000)
    SetCameraDistance(14500, 1000)
    SetChrChip(0x0, 0xFE, 0x1E, 0xC8)
    SetChrSubChip(0x12, 0x2)
    Sound(844, 0, 100, 0)

    def lambda_7002():
        OP_9D(0xFE, 0x2B368, 0x0, 0x1C84, 0xDAC, 0xFA0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_7002)
    Sleep(400)
    Sound(326, 0, 100, 0)
    OP_93(0x12, 0xA0, 0x0)
    SetChrSubChip(0x12, 0x3)
    WaitChrThread(0x12, 1)
    Sound(326, 0, 100, 0)
    SetChrSubChip(0x12, 0x1)
    Sleep(100)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    Fade(250)
    Sound(802, 0, 100, 0)
    SetChrFlags(0x12, 0x2)
    SetChrFlags(0x12, 0x10)
    SetChrFlags(0x12, 0x20)
    SetChrChipByIndex(0x12, 0x2F)
    SetChrSubChip(0x12, 0x0)
    OP_A7(0x10, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_0D()
    Return()

    # Function_43_6EBA end

    def Function_44_7076(): pass

    label("Function_44_7076")

    SetChrChipByIndex(0x1E, 0x24)
    SetChrSubChip(0x1E, 0x0)
    OP_93(0x1E, 0x5A, 0x1F4)

    def lambda_708A():
        OP_96(0xFE, 0x29B94, 0x0, 0x1CE8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_708A)
    WaitChrThread(0x1E, 1)
    Return()

    # Function_44_7076 end

    def Function_45_70A4(): pass

    label("Function_45_70A4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_70D0")

    def lambda_70B4():
        OP_A6(0xFE, 0x0, 0x64, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_70B4)
    Sleep(500)
    Jump("Function_45_70A4")

    label("loc_70D0")

    Return()

    # Function_45_70A4 end

    def Function_46_70D1(): pass

    label("Function_46_70D1")


    def lambda_70D6():
        OP_95(0xFE, 162900, 0, 2600, 4500, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_70D6)
    WaitChrThread(0x104, 1)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_46_70D1 end

    def Function_47_70F7(): pass

    label("Function_47_70F7")


    def lambda_70FC():
        OP_95(0xFE, 160000, 0, 2000, 4500, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_70FC)
    WaitChrThread(0x101, 1)

    def lambda_711A():
        OP_95(0xFE, 162900, 0, 4800, 4500, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_711A)
    WaitChrThread(0x101, 1)
    OP_93(0xFE, 0x87, 0x1F4)
    Return()

    # Function_47_70F7 end

    def Function_48_713B(): pass

    label("Function_48_713B")


    def lambda_7140():
        OP_95(0xFE, 160000, 0, 4000, 4500, 0x1)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7140)
    WaitChrThread(0x102, 1)

    def lambda_715E():
        OP_95(0xFE, 166600, 0, 9900, 4500, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_715E)
    WaitChrThread(0x102, 1)
    OP_93(0xFE, 0x5A, 0x1F4)
    SetChrChipByIndex(0x102, 0x29)
    SetChrSubChip(0x102, 0x0)
    Sound(812, 0, 100, 0)
    Return()

    # Function_48_713B end

    def Function_49_718D(): pass

    label("Function_49_718D")


    def lambda_7192():
        OP_95(0xFE, 159000, 0, 5100, 4500, 0x1)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_7192)
    WaitChrThread(0x109, 1)

    def lambda_71B0():
        OP_95(0xFE, 165300, 0, 7100, 4500, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_71B0)
    WaitChrThread(0x109, 1)
    OP_93(0xFE, 0x87, 0x1F4)
    Return()

    # Function_49_718D end

    def Function_50_71D1(): pass

    label("Function_50_71D1")


    def lambda_71D6():
        OP_95(0xFE, 159000, 0, 4600, 4500, 0x1)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_71D6)
    WaitChrThread(0x105, 1)

    def lambda_71F4():
        OP_95(0xFE, 165600, 0, 11400, 4500, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_71F4)
    WaitChrThread(0x105, 1)
    OP_93(0xFE, 0x5A, 0x1F4)
    SetChrChipByIndex(0x105, 0x2A)
    SetChrSubChip(0x105, 0x0)
    Sound(812, 0, 100, 0)
    Return()

    # Function_50_71D1 end

    def Function_51_7223(): pass

    label("Function_51_7223")


    def lambda_7228():
        OP_95(0xFE, 157000, 0, 3800, 4500, 0x1)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_7228)
    WaitChrThread(0x103, 1)

    def lambda_7246():
        OP_95(0xFE, 161800, 0, 6100, 4500, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_7246)
    WaitChrThread(0x103, 1)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_51_7223 end

    def Function_52_7267(): pass

    label("Function_52_7267")

    Sleep(1000)
    StopEffect(0x0, 0x2)
    Sleep(1000)
    StopEffect(0x2, 0x2)
    Sleep(1000)
    StopEffect(0x4, 0x2)
    Sleep(1000)
    StopEffect(0x1, 0x2)
    Sleep(1000)
    StopEffect(0x3, 0x2)
    Return()

    # Function_52_7267 end

    def Function_53_7286(): pass

    label("Function_53_7286")

    StopSound(864, 2000, 50)
    OP_25(0x35F, 0x3C)
    Sleep(100)
    OP_25(0x35F, 0x46)
    Sleep(100)
    OP_25(0x35F, 0x50)
    Sleep(100)
    OP_25(0x35F, 0x5A)
    Sleep(100)
    OP_25(0x35F, 0x64)
    Return()

    # Function_53_7286 end

    def Function_54_72AD(): pass

    label("Function_54_72AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21C, 7)), scpexpr(EXPR_END)), "loc_72B7")
    Return()

    label("loc_72B7")

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

    #A0134
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
        (1, "loc_7383"),
        (SWITCH_DEFAULT, "loc_739C"),
    )


    label("loc_7383")

    Sleep(500)
    OP_E2(0x2)
    OP_90(0x0, 4970, 0, 0, 90)
    EventEnd(0x5)
    Return()

    label("loc_739C")

    Battle("BattleInfo_660", 0x0, 0x0, 0x100, 0xC, 0xFF)
    OP_E2(0x2)
    EventBegin(0x1)
    OP_68(4970, 1000, 0, 0)
    OP_90(0x0, 4970, 0, 0, 90)
    OP_90(0x1, 4970, 0, 0, 90)
    OP_90(0x2, 4970, 0, 0, 90)
    OP_90(0x3, 4970, 0, 0, 90)
    OP_90(0x4, 4970, 0, 0, 90)
    OP_90(0x5, 4970, 0, 0, 90)
    OP_90(0x6, 4970, 0, 0, 90)
    OP_90(0x7, 4970, 0, 0, 90)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (2, "loc_745E"),
        (1, "loc_7463"),
        (SWITCH_DEFAULT, "loc_7466"),
    )


    label("loc_745E")

    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    label("loc_7463")

    OP_B9(0x0)
    Return()

    label("loc_7466")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(510, 0, 870, 0)
    MoveCamera(44, 39, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(13070, 0)
    SetChrFlags(0x21, 0x80)
    OP_E2(0x3)
    Sleep(400)
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0135
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "消灭了通缉魔兽！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0136
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x11),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    AddItemNumber(0x11, 1)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x101, 2500, 0, 0, 270)
    SetChrPos(0x102, -2500, 0, 0, 90)
    SetChrPos(0x103, -1200, 0, -1700, 45)
    SetChrPos(0x104, 1200, 0, -1700, 0)
    SetChrPos(0x109, -1200, 0, 1700, 180)
    SetChrPos(0x105, 1200, 0, 1700, 180)
    FadeToBright(300, 0)
    OP_0D()
    Sleep(400)

    #C0137
    ChrTalk(
        0x101,
        (
            "#00000F战术书……\x01",
            "缇欧和瓦吉应该可以学会这个战技呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0x103,
        "#00200F瓦吉先生，要试试看吗？\x02",
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0x105,
        "#10300F好啊，那就马上来试试吧。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(500)
    Sound(517, 0, 100, 0)
    AddCraft(0x2, 0x191)
    AddCraft(0x4, 0x191)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0140
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "缇欧和瓦吉习得组合战技\x01\x07\x02",

            "『Σ升天』\x07\x05",
            "。\x02",
        )
    )

    CloseMessageWindow()

    #A0141
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "两人各自消耗１００点ＣＰ，\x01",
            "便可以施展威力强大的组合技攻击。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x21C, 7)
    OP_29(0x8C, 0x4, 0x10)
    OP_29(0x8C, 0x4, 0x2)
    OP_29(0x8C, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_E2(0x2)
    ModifyEventFlags(0, 0, 0x80)
    EventEnd(0x5)
    Return()

    # Function_54_72AD end

    def Function_55_76E0(): pass

    label("Function_55_76E0")

    SetMapFlags(0x8000000)
    EventBegin(0x1)
    SetChrName("")

    #A0142
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "导力已经停止了。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x194, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7810")

    #C0143
    ChrTalk(
        0x101,
        (
            "#00003F看来已经无法\x01",
            "前往更深处了。\x02",
        )
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0x103,
        (
            "#00200F自从通商会议时发生恐怖袭击\x01",
            "事件之后，市政府就把一部分通道\x01",
            "给封锁起来了。\x02\x03",

            "#00203F这种决定很妥当，\x01",
            "可以说是理所当然的判断吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0x102,
        (
            "#00100F算啦，反正我们现在\x01",
            "也没必要去更深处，\x01",
            "还是离开这里吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x194, 4)

    label("loc_7810")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_55_76E0 end

    SaveToFile()

Try(main)
