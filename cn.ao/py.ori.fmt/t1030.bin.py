from ScenarioHelper import *

def main():
    CreateScenaFile(
        "t1030.bin",                # FileName
        "t1030",                    # MapName
        "t1030",                    # Location
        0x0041,                     # MapIndex
        "ed7565",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x02,                       # PlaceNameNumber
        0x1A,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 65, 0, 1, 0, 2],
    )

    BuildStringList((
        "t1030",                  # 0
        "缇欧",                   # 1
        "蔡特",                   # 2
        "修利",                   # 3
        "咪西",                   # 4
        "奇幻乐园工作人员",       # 5
        "奇幻乐园工作人员",       # 6
        "游客",                   # 7
        "游客",                   # 8
        "游客",                   # 9
        "游客",                   # 10
        "游客",                   # 11
        "游客",                   # 12
        "梅尔斯",                 # 13
        "柯洛娜",                 # 14
        "利玛",                   # 15
        "职员亨克斯",             # 16
        "神狼蔡特",               # 17
        "猎兵",                   # 18
        "猎兵",                   # 19
        "猎兵",                   # 20
        "猎兵",                   # 21
        "猎兵",                   # 22
        "猎兵",                   # 23
        "猎兵",                   # 24
        "猎兵",                   # 25
        "父亲",                   # 26
        "母亲",                   # 27
        "男孩",                   # 28
        "幻兽",                   # 29
        "SE控制",                 # 30
        "bt1030",                 # 31
        "翠雀酒店方向",           # 32
        "主题公园方向",           # 33
    ))

    ATBonus("ATBonus_94", 100, 5, 0, 5, 0, 5, 0, 2, 5, 0, 0, 0, 2, 0, 0, 0)

    MonsterBattlePostion("MonsterBattlePostion_A4", 8, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_A8", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_AC", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_B0", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_B4", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_B8", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_BC", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_C0", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_C4", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_C8", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_CC", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_D0", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_D4", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_D8", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_DC", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_E0", 5, 5, 45)

    # monster count: 0

    # event battle count: 1

    BattleInfo(
        "BattleInfo_E4", 0x0042, 3, 6, 45, 3, 3, 30, 0, "bt1030", 0x00000000, 100, 0, 0, 0,
        (
            ("ms88401.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_A4", "MonsterBattlePostion_C4", "ed7454", "ed7453", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    AddCharChip((
        "chr/ch00200.itc",                   # 00
        "chr/ch02702.itc",                   # 01
        "chr/ch10100.itc",                   # 02
        "chr/ch28100.itc",                   # 03
        "chr/ch10200.itc",                   # 04
        "chr/ch44500.itc",                   # 05
        "chr/ch32300.itc",                   # 06
        "chr/ch32400.itc",                   # 07
        "chr/ch24200.itc",                   # 08
        "chr/ch24300.itc",                   # 09
        "chr/ch24600.itc",                   # 0A
        "chr/ch24700.itc",                   # 0B
        "chr/ch26200.itc",                   # 0C
        "chr/ch22700.itc",                   # 0D
        "chr/ch20700.itc",                   # 0E
        "chr/ch00000.itc",                   # 0F
        "chr/ch00000.itc",                   # 10
        "chr/ch00000.itc",                   # 11
        "chr/ch00000.itc",                   # 12
        "chr/ch00000.itc",                   # 13
        "chr/ch00000.itc",                   # 14
        "chr/ch00000.itc",                   # 15
        "chr/ch00000.itc",                   # 16
        "chr/ch00000.itc",                   # 17
        "chr/ch00000.itc",                   # 18
        "chr/ch00000.itc",                   # 19
        "chr/ch00000.itc",                   # 1A
        "chr/ch00000.itc",                   # 1B
        "chr/ch00000.itc",                   # 1C
        "chr/ch00000.itc",                   # 1D
    ))

    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   0,   0,   0,   0,   0,   3,   255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   1,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   2,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(360,     4159,    -15840,  180,  389,  0x0, 0,   4,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(-4000,   4400,    0,       180,  389,  0x0, 0,   5,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(4750,    4400,    0,       180,  389,  0x0, 0,   5,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(-13500,  4000,    -6500,   270,  389,  0x0, 0,   6,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(-13500,  4000,    -5500,   180,  389,  0x0, 0,   7,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(-6139,   4000,    -15340,  90,   389,  0x0, 0,   8,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(0,       4159,    -15840,  180,  389,  0x0, 0,   9,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(-1049,   4000,    -16770,  45,   389,  0x0, 0,   10,  0,   0,   0,   0,   13,  255,  0)
    DeclNpc(600,     4000,    -17229,  315,  389,  0x0, 0,   11,  0,   0,   0,   0,   14,  255,  0)
    DeclNpc(7699,    4000,    -1519,   135,  389,  0x0, 0,   12,  0,   0,   0,   0,   15,  255,  0)
    DeclNpc(9159,    4000,    -1759,   270,  389,  0x0, 0,   13,  0,   0,   0,   0,   16,  255,  0)
    DeclNpc(7889,    4000,    -3069,   0,    389,  0x0, 0,   14,  0,   0,   0,   0,   17,  255,  0)
    DeclNpc(-8270,   4000,    389,     180,  389,  0x0, 0,   3,   0,   0,   0,   0,   18,  255,  0)
    DeclNpc(0,       0,       0,       0,    228,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   11,  0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   11,  0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   11,  0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   11,  0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   11,  0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   11,  0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   11,  0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   11,  0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 20,  0.0,                   -28.0,                 -1.0,                  506.25,                [0.06666667014360428,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.3333333432674408,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -0.0,                  9.333333969116211,     0.20000000298023224,   1.0])
    DeclEvent(0x0000, 0, 38,  0.0,                   2.5,                   3.4000000953674316,    100.0,                 [0.09999999403953552,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.19999998807907104,   0.0,                   -0.0,                  -1.25,                 -0.6800000071525574,   1.0])

    DeclActor(-14170,  4000,    -6040,   1200,    -14170,  5500,    -6040,   0x007C, 0,  39, 0x0000)
    DeclActor(-6650,   4000,    1550,    1200,    -6650,   5500,    1550,    0x007C, 0,  40, 0x0000)

    PlaceName(10.0, 0.0, -68.0, 0x0000, 0x0000, "翠雀酒店方向")
    PlaceName(-5.0, 0.0, 20.0, 0x0000, 0x0000, "主题公园方向")

    ChipFrameInfo(1916, 0)                                       # 0

    ScpFunction((
        "Function_0_6C8",          # 00, 0
        "Function_1_778",          # 01, 1
        "Function_2_973",          # 02, 2
        "Function_3_AEE",          # 03, 3
        "Function_4_B82",          # 04, 4
        "Function_5_C23",          # 05, 5
        "Function_6_C99",          # 06, 6
        "Function_7_EF0",          # 07, 7
        "Function_8_1077",         # 08, 8
        "Function_9_1270",         # 09, 9
        "Function_10_134D",        # 0A, 10
        "Function_11_13DB",        # 0B, 11
        "Function_12_1456",        # 0C, 12
        "Function_13_14C8",        # 0D, 13
        "Function_14_1565",        # 0E, 14
        "Function_15_15E9",        # 0F, 15
        "Function_16_1722",        # 10, 16
        "Function_17_179D",        # 11, 17
        "Function_18_1826",        # 12, 18
        "Function_19_182D",        # 13, 19
        "Function_20_224F",        # 14, 20
        "Function_21_27B9",        # 15, 21
        "Function_22_27DE",        # 16, 22
        "Function_23_2C4F",        # 17, 23
        "Function_24_2C6B",        # 18, 24
        "Function_25_33FF",        # 19, 25
        "Function_26_34FE",        # 1A, 26
        "Function_27_36DF",        # 1B, 27
        "Function_28_3710",        # 1C, 28
        "Function_29_373C",        # 1D, 29
        "Function_30_3A6C",        # 1E, 30
        "Function_31_462B",        # 1F, 31
        "Function_32_4FDE",        # 20, 32
        "Function_33_5007",        # 21, 33
        "Function_34_5030",        # 22, 34
        "Function_35_5059",        # 23, 35
        "Function_36_505A",        # 24, 36
        "Function_37_505B",        # 25, 37
        "Function_38_5081",        # 26, 38
        "Function_39_5262",        # 27, 39
        "Function_40_52BE",        # 28, 40
    ))


    def Function_0_6C8(): pass

    label("Function_0_6C8")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_700"),
        (1, "loc_70C"),
        (2, "loc_718"),
        (3, "loc_724"),
        (4, "loc_730"),
        (5, "loc_73C"),
        (6, "loc_748"),
        (SWITCH_DEFAULT, "loc_754"),
    )


    label("loc_700")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_760")

    label("loc_70C")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_760")

    label("loc_718")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_760")

    label("loc_724")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_760")

    label("loc_730")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_760")

    label("loc_73C")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_760")

    label("loc_748")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_760")

    label("loc_754")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_760")

    label("loc_760")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_777")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_760")

    label("loc_777")

    Return()

    # Function_0_6C8 end

    def Function_1_778(): pass

    label("Function_1_778")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_78C")
    ClearScenarioFlags(0x22, 0)
    Event(0, 24)
    Jump("loc_7D2")

    label("loc_78C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_7A3")
    ClearScenarioFlags(0x22, 1)
    SetScenarioFlags(0x1, 1)
    Event(0, 31)
    Jump("loc_7D2")

    label("loc_7A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 2)), scpexpr(EXPR_END)), "loc_7B7")
    ClearScenarioFlags(0x22, 2)
    Event(0, 30)
    Jump("loc_7D2")

    label("loc_7B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7D2")
    SetMapFlags(0x10000000)
    Event(0, 29)

    label("loc_7D2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x86, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x86, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x86, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7F8")
    ClearChrFlags(0x17, 0x80)

    label("loc_7F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_806")
    Jump("loc_972")

    label("loc_806")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 7)), scpexpr(EXPR_END)), "loc_814")
    Jump("loc_972")

    label("loc_814")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_822")
    Jump("loc_972")

    label("loc_822")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_830")
    Jump("loc_972")

    label("loc_830")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_8B4")
    SetChrPos(0x8, -7400, 4000, -11000, 270)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x9, -6400, 4000, -10000, 180)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0xA, -8600, 4000, -11000, 90)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, -3940, 1730, -25670, 0)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x13, 0x10)
    Jump("loc_972")

    label("loc_8B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_8F6")
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 0, 1910, -25230, 0)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x13, 0x10)
    Jump("loc_972")

    label("loc_8F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_904")
    Jump("loc_972")

    label("loc_904")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_969")
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x10)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x10)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, -6040, 4000, -16340, 90)
    SetChrFlags(0x12, 0x10)
    ClearChrFlags(0x14, 0x80)
    SetChrFlags(0x14, 0x10)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    Jump("loc_972")

    label("loc_969")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_972")

    label("loc_972")

    Return()

    # Function_1_778 end

    def Function_2_973(): pass

    label("Function_2_973")

    SetMapObjFrame(0xFF, "t1030_sky", 0x1, 0x1)
    SetMapObjFrame(0xFF, "t1030_sky_y", 0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_9B1")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0xA0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x1, 1)
    Jump("loc_9C3")

    label("loc_9B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_9C3")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x233), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_9C3")

    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9DB")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_9DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9FD")
    SetMapObjFrame(0xFF, "t1030_water", 0x2, "loop_off")

    label("loc_9FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A38")
    OP_24(0x335)
    SoundDistance(0x7B, 0xFFFFFFBA, 0x109A, 0xFFFFD9E0, 0x2710, 0x186A0, 0x50, 0x0)
    SoundLoad(918)
    BeginChrThread(0x25, 3, 0, 37)
    Jump("loc_A6B")

    label("loc_A38")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_END)), "loc_A65")
    OP_24(0x335)
    SoundDistance(0x7B, 0xFFFFFFBA, 0x109A, 0xFFFFD9E0, 0x2710, 0x186A0, 0x50, 0x0)
    Jump("loc_A6B")

    label("loc_A65")

    Sound(821, 1, 40, 0)

    label("loc_A6B")

    ModifyEventFlags(0, 1, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A83")
    ModifyEventFlags(1, 1, 0x80)

    label("loc_A83")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A96")
    ModifyEventFlags(1, 1, 0x80)

    label("loc_A96")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_AA4")
    ModifyEventFlags(0, 1, 0x80)

    label("loc_AA4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_ACB")
    OP_7D(0xDC, 0xEB, 0xFF, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0xD, 0x78, 0x0)
    Jump("loc_AED")

    label("loc_ACB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 3)), scpexpr(EXPR_END)), "loc_AED")
    OP_7D(0xDC, 0xEB, 0xFF, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0xD, 0x78, 0x0)

    label("loc_AED")

    Return()

    # Function_2_973 end

    def Function_3_AEE(): pass

    label("Function_3_AEE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B00")
    Call(0, 19)
    Return()

    label("loc_B00")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_B11")
    Jump("loc_B7E")

    label("loc_B11")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_B1F")
    Jump("loc_B7E")

    label("loc_B1F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_B2D")
    Jump("loc_B7E")

    label("loc_B2D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_B3D")
    Jump("loc_B7E")

    label("loc_B3D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_B4B")
    Jump("loc_B7E")

    label("loc_B4B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_B59")
    Jump("loc_B7E")

    label("loc_B59")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_B67")
    Jump("loc_B7E")

    label("loc_B67")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_B75")
    Jump("loc_B7E")

    label("loc_B75")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_B7E")

    label("loc_B7E")

    TalkEnd(0xFE)
    Return()

    # Function_3_AEE end

    def Function_4_B82(): pass

    label("Function_4_B82")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B94")
    Call(0, 19)
    Return()

    label("loc_B94")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_BA5")
    Jump("loc_C1F")

    label("loc_BA5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_BB3")
    Jump("loc_C1F")

    label("loc_BB3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_BC1")
    Jump("loc_C1F")

    label("loc_BC1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_BEC")

    #C0001
    ChrTalk(
        0x9,
        "#01200F……咕呜呜呜……\x02",
    )

    CloseMessageWindow()
    Jump("loc_C1F")

    label("loc_BEC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_BFA")
    Jump("loc_C1F")

    label("loc_BFA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_C08")
    Jump("loc_C1F")

    label("loc_C08")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_C16")
    Jump("loc_C1F")

    label("loc_C16")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_C1F")

    label("loc_C1F")

    TalkEnd(0xFE)
    Return()

    # Function_4_B82 end

    def Function_5_C23(): pass

    label("Function_5_C23")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C35")
    Call(0, 19)
    Return()

    label("loc_C35")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_C46")
    Jump("loc_C95")

    label("loc_C46")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_C54")
    Jump("loc_C95")

    label("loc_C54")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_C62")
    Jump("loc_C95")

    label("loc_C62")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_C70")
    Jump("loc_C95")

    label("loc_C70")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_C7E")
    Jump("loc_C95")

    label("loc_C7E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_C8C")
    Jump("loc_C95")

    label("loc_C8C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_C95")

    label("loc_C95")

    TalkEnd(0xFE)
    Return()

    # Function_5_C23 end

    def Function_6_C99(): pass

    label("Function_6_C99")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_CAA")
    Jump("loc_EEC")

    label("loc_CAA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_CB8")
    Jump("loc_EEC")

    label("loc_CB8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_EEC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DB6")

    #C0002
    ChrTalk(
        0xB,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "你们好！\x01",
            "欢迎光临奇幻乐园！\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0xB,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "咪嘻嘻，要玩得开心哦～！\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x101,
        "#00002F哦哦，是咪西啊。\x02",
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x104,
        (
            "#00309F哈哈，要是把阿缇\x01",
            "也带来就好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x105,
        (
            "#10304F算啦，反正下午还要过来。\x01",
            "把最有趣的活动留到最后，\x01",
            "只会让她更加开心吧？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_EEC")

    label("loc_DB6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E99")

    #C0007
    ChrTalk(
        0xB,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "话说回来，小哥哥，\x01",
            "你是和同性朋友一起来玩的吗～？\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0xB,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "没关系的！\x01",
            "就算没有恋人，\x01",
            "也能在园内玩得很开心哟¤\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0xB,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "咪嘻嘻，要玩得开心哦～！\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x101,
        (
            "#00006F（……不知为何，\x01",
            "  反倒觉得有点悲伤了……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_EEC")

    label("loc_E99")


    #C0011
    ChrTalk(
        0xB,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "就算没有恋人，\x01",
            "也能在园内玩得很开心哟¤\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0xB,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "咪嘻嘻，要玩得开心哦～！\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EEC")

    TalkEnd(0xFE)
    Return()

    # Function_6_C99 end

    def Function_7_EF0(): pass

    label("Function_7_EF0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_F01")
    Jump("loc_1073")

    label("loc_F01")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_F90")

    #C0013
    ChrTalk(
        0xC,
        (
            "站在向导板前面的那两个孩子，\x01",
            "从刚才开始就一直在\x01",
            "兴致勃勃地讨论咪西呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0xC,
        (
            "呵呵，身为奇幻乐园的工作人员，\x01",
            "总觉得很开心呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1073")

    label("loc_F90")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_1073")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1023")

    #C0015
    ChrTalk(
        0xC,
        (
            "欢迎光临米修拉姆\x01",
            "引以为傲的主题公园。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0xC,
        (
            "我们最近新引进的\x01",
            "最新游乐设施很受欢迎。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0xC,
        "入场之后请一定不要错过哦！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1073")

    label("loc_1023")


    #C0018
    ChrTalk(
        0xC,
        (
            "主题公园\x01",
            "最近新引进的\x01",
            "最新游乐设施很受欢迎。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0xC,
        "入场之后一定不要错过哦！\x02",
    )

    CloseMessageWindow()

    label("loc_1073")

    TalkEnd(0xFE)
    Return()

    # Function_7_EF0 end

    def Function_8_1077(): pass

    label("Function_8_1077")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_1088")
    Jump("loc_126C")

    label("loc_1088")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_10E7")

    #C0020
    ChrTalk(
        0xD,
        (
            "咪西现在\x01",
            "正在主题公园内\x01",
            "闲逛呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0xD,
        (
            "如果发现了它，可以随意\x01",
            "邀请它合影哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_126C")

    label("loc_10E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_126C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1202")

    #C0022
    ChrTalk(
        0xD,
        (
            "最近，在儿童群体中\x01",
            "流行起了一种名叫\x01",
            "『踢咪西屁股』的游戏。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0xD,
        (
            "说起它的发源，多少有些恶作剧的成分在内。\x01",
            "最近还流传起了『踢到的人就会获得幸福』\x01",
            "这样的说法。\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0xD,
        (
            "呵呵，小孩子\x01",
            "请一定要\x01",
            "踢咪西一脚哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x101,
        (
            "#00006F（好、好像连工作人员\x01",
            "  都很兴奋啊……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_126C")

    label("loc_1202")


    #C0026
    ChrTalk(
        0xD,
        (
            "最近，在儿童群体中\x01",
            "流行起了一种名叫\x01",
            "『踢咪西屁股』的游戏。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0xD,
        (
            "呵呵，小孩子\x01",
            "请一定要\x01",
            "踢咪西一脚哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_126C")

    TalkEnd(0xFE)
    Return()

    # Function_8_1077 end

    def Function_9_1270(): pass

    label("Function_9_1270")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_1281")
    Jump("loc_1349")

    label("loc_1281")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_12D1")

    #C0028
    ChrTalk(
        0xE,
        "哦哦，这里就是米修拉姆奇幻乐园……！\x02",
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0xE,
        "立刻进去玩个够吧～\x02",
    )

    CloseMessageWindow()
    Jump("loc_1349")

    label("loc_12D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_1349")

    #C0030
    ChrTalk(
        0xE,
        (
            "去主题公园游玩可是件大事，\x01",
            "要好好规划。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0xE,
        (
            "为了能和女友\x01",
            "一起玩到更多的游乐设施，\x01",
            "必须得制定合理的计划。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1349")

    TalkEnd(0xFE)
    Return()

    # Function_9_1270 end

    def Function_10_134D(): pass

    label("Function_10_134D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_135E")
    Jump("loc_13D7")

    label("loc_135E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_136C")
    Jump("loc_13D7")

    label("loc_136C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_13D7")

    #C0032
    ChrTalk(
        0xF,
        (
            "真是的，何必那么麻烦，\x01",
            "赶快进去吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0xF,
        (
            "你一直考虑这种事情，\x01",
            "只会让我们的游玩时间不断减少。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13D7")

    TalkEnd(0xFE)
    Return()

    # Function_10_134D end

    def Function_11_13DB(): pass

    label("Function_11_13DB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_13EC")
    Jump("loc_1452")

    label("loc_13EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_13FA")
    Jump("loc_1452")

    label("loc_13FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_1452")

    #C0034
    ChrTalk(
        0x10,
        (
            "哦哦，那不是\x01",
            "咪西吗……！\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x10,
        (
            "好，爸爸给你们\x01",
            "拍张照片，\x01",
            "快站到它旁边去。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1452")

    TalkEnd(0xFE)
    Return()

    # Function_11_13DB end

    def Function_12_1456(): pass

    label("Function_12_1456")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_1467")
    Jump("loc_14C4")

    label("loc_1467")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_14BB")

    #C0036
    ChrTalk(
        0x11,
        (
            "咪西好像进入\x01",
            "主题公园了。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x11,
        (
            "好～既然如此，\x01",
            "妈妈来努力找到它！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14C4")

    label("loc_14BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_14C4")

    label("loc_14C4")

    TalkEnd(0xFE)
    Return()

    # Function_12_1456 end

    def Function_13_14C8(): pass

    label("Function_13_14C8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_14D9")
    Jump("loc_1561")

    label("loc_14D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_1535")

    #C0038
    ChrTalk(
        0x12,
        (
            "我今天一定要成功\x01",
            "踢到咪西～！\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x12,
        (
            "听说这样就能得到幸福了。\x01",
            "咪西好棒呀！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1561")

    label("loc_1535")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_1561")

    #C0040
    ChrTalk(
        0x12,
        (
            "哇～是咪西！\x01",
            "真正的咪西啊～！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1561")

    TalkEnd(0xFE)
    Return()

    # Function_13_14C8 end

    def Function_14_1565(): pass

    label("Function_14_1565")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_1576")
    Jump("loc_15E5")

    label("loc_1576")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_15DC")

    #C0041
    ChrTalk(
        0x13,
        (
            "不要嘛～竟然要踢咪西，\x01",
            "咪西好可怜！\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x13,
        (
            "如果只是让哥哥一个人踢的话，\x01",
            "踢我就好了！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15E5")

    label("loc_15DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_15E5")

    label("loc_15E5")

    TalkEnd(0xFE)
    Return()

    # Function_14_1565 end

    def Function_15_15E9(): pass

    label("Function_15_15E9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_15FA")
    Jump("loc_171E")

    label("loc_15FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_1608")
    Jump("loc_171E")

    label("loc_1608")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_1616")
    Jump("loc_171E")

    label("loc_1616")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_1715")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_168E")
    OP_4B(0x16, 0xFF)

    #C0043
    ChrTalk(
        0x14,
        "呼，总算到了啊。\x02",
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x14,
        (
            "好～\x01",
            "利玛、柯洛娜，\x01",
            "我们赶快入园吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x16,
        "同意～！！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    ClearChrFlags(0x14, 0x10)
    OP_4C(0x16, 0xFF)
    Jump("loc_1710")

    label("loc_168E")


    #C0046
    ChrTalk(
        0x14,
        (
            "为了彻底玩个够，\x01",
            "我买了今天\x01",
            "不限次数的套票。\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x14,
        (
            "平时一直没时间照顾家里，\x01",
            "让家人那么辛苦，\x01",
            "今天可要让利玛和柯洛娜玩个痛快。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1710")

    Jump("loc_171E")

    label("loc_1715")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_171E")

    label("loc_171E")

    TalkEnd(0xFE)
    Return()

    # Function_15_15E9 end

    def Function_16_1722(): pass

    label("Function_16_1722")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_1733")
    Jump("loc_1799")

    label("loc_1733")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_1741")
    Jump("loc_1799")

    label("loc_1741")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_174F")
    Jump("loc_1799")

    label("loc_174F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_1790")

    #C0048
    ChrTalk(
        0x15,
        (
            "主题公园内\x01",
            "都有什么呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x15,
        "呵呵，真期待。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1799")

    label("loc_1790")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_1799")

    label("loc_1799")

    TalkEnd(0xFE)
    Return()

    # Function_16_1722 end

    def Function_17_179D(): pass

    label("Function_17_179D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_17AE")
    Jump("loc_1822")

    label("loc_17AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_17BC")
    Jump("loc_1822")

    label("loc_17BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_17CA")
    Jump("loc_1822")

    label("loc_17CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_1819")

    #C0050
    ChrTalk(
        0x16,
        (
            "我今天要和爸爸妈妈\x01",
            "在主题公园玩一整天！\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x16,
        "呵呵，好期待！\x02",
    )

    CloseMessageWindow()
    Jump("loc_1822")

    label("loc_1819")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_1822")

    label("loc_1822")

    TalkEnd(0xFE)
    Return()

    # Function_17_179D end

    def Function_18_1826(): pass

    label("Function_18_1826")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_18_1826 end

    def Function_19_182D(): pass

    label("Function_19_182D")

    EventBegin(0x0)
    Fade(500)
    OP_68(-8000, 5000, -11750, 0)
    MoveCamera(315, 25, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(24500, 0)
    SetCameraDistance(24000, 1500)
    OP_4B(0x8, 0xFF)
    OP_4B(0xA, 0xFF)
    OP_93(0x8, 0xB4, 0x0)
    OP_93(0xA, 0xB4, 0x0)
    SetChrPos(0x101, -8600, 4000, -12500, 0)
    SetChrPos(0x153, -7400, 4000, -12500, 0)
    OP_6F(0x79)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1DC5")

    #C0052
    ChrTalk(
        0x153,
        "#01110F#6P嘿嘿嘿，久等啦。\x02",
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x8,
        "#00202F#11P罗伊德前辈，琪雅。\x02",
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0xA,
        "#14000F#11P……哟。\x02",
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x9,
        "#01200F#11P嗷。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 7)), scpexpr(EXPR_END)), "loc_1BC7")

    #C0056
    ChrTalk(
        0x101,
        (
            "#00009F#6P缇欧，你已经到了啊。\x02\x03",

            "#00002F刚才真是辛苦了，\x01",
            "多亏有你帮忙。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x8,
        (
            "#00211F#11P……但我多少\x01",
            "丢了些脸呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x101,
        (
            "#00006F#6P唔……真不好意思，\x01",
            "都怪我能力不足……\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x8,
        (
            "#00203F#11P不，罗伊德前辈\x01",
            "并不需要道歉。\x02\x03",

            "#00202F毕竟结果还不错，\x01",
            "就不要在意那些小事了。\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0xA,
        (
            "#04205F#5P说起来，你们刚才好像\x01",
            "去湖水浴场了吧……\x01",
            "那里发生了什么事吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x101,
        (
            "#00012F#6P没、没什么啦，哈哈哈……\x02\x03",

            "#00000F话、话说回来，\x01",
            "别人好像还没到啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x8,
        (
            "#00204F#11P嗯，我们来得\x01",
            "稍早了一些。\x02\x03",

            "#00202F我正在教导修利小姐，\x01",
            "让她明白咪西的可爱之处。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_93(0xA, 0x5A, 0x1F4)
    Sleep(500)

    #C0063
    ChrTalk(
        0xA,
        (
            "#14011F#5P不、不对，才没有那种事吧！？\x02\x03",

            "#14012F我完全没\x01",
            "觉得它可……\x02\x03",

            "#14006F喂，不要突然把话题扯回到咪西啊！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CCF")

    label("loc_1BC7")


    #C0064
    ChrTalk(
        0x101,
        (
            "#00009F#6P哟，你们先到了啊。\x02\x03",

            "#00002F不过别人\x01",
            "好像还没到吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x8,
        (
            "#00204F#11P嗯，我们来得\x01",
            "稍早了一些。\x02\x03",

            "#00202F我正在教导修利小姐，\x01",
            "让她明白咪西的可爱之处。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_93(0xA, 0x5A, 0x1F4)
    Sleep(500)

    #C0066
    ChrTalk(
        0xA,
        (
            "#14011F#5P不、不对，才没有那种事吧！？\x02\x03",

            "#14012F我完全没\x01",
            "觉得它可……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1CCF")

    OP_93(0x8, 0x10E, 0x1F4)

    #C0067
    ChrTalk(
        0x8,
        (
            "#00203F#12P休想抵赖。\x02\x03",

            "#00202F从刚才开始，我就在修利小姐的\x01",
            "身上清晰感受到了\x01",
            "对咪西感兴趣的气息。\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0xA,
        "#14011F#5P你说什么啊，哪有那种气息！？\x02",
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x153,
        "#01109F#6P嘿嘿嘿，关系真好呢。\x02",
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x101,
        (
            "#00002F#6P（嗯……要在这里\x01",
            "  等待大家吗？）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x145, 3)
    Jump("loc_1EBA")

    label("loc_1DC5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 7)), scpexpr(EXPR_END)), "loc_1E25")

    #C0071
    ChrTalk(
        0x8,
        (
            "#00202F#11P……之前真是辛苦了。\x02\x03",

            "罗伊德前辈，琪雅，\x01",
            "你们也要在这里等大家吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E61")

    label("loc_1E25")


    #C0072
    ChrTalk(
        0x8,
        (
            "#00200F#11P罗伊德前辈，琪雅，\x01",
            "你们也要在这里等大家吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E61")


    #C0073
    ChrTalk(
        0xA,
        "#14000F#11P既然来了，就陪我们一起等吧。\x02",
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x101,
        "#00002F#6P（嗯……要不要在这里等呢？）\x02",
    )

    CloseMessageWindow()

    label("loc_1EBA")

    FadeToDark(300, 0, 100)
    OP_0D()
    Sound(814, 0, 100, 0)

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【还有其它事情】\x01",      # 0
            "【在这里等大家】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (1, "loc_1F1C"),
        (0, "loc_2192"),
        (SWITCH_DEFAULT, "loc_224E"),
    )


    label("loc_1F1C")


    def lambda_1F21():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_1F21)
    Sleep(50)

    def lambda_1F31():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_1F31)
    WaitChrThread(0x8, 2)
    WaitChrThread(0xA, 2)

    #C0075
    ChrTalk(
        0x8,
        (
            "#00203F#11P那么，我再为你们二位\x01",
            "正式说明一次。\x02\x03",

            "#00201F让你们明白咪西是如何\x01",
            "利用自己的可爱，\x01",
            "为塞姆里亚大陆的和平做出贡献的……！\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x153,
        "#01105F#6P哇！\x02",
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_93(0xA, 0x5A, 0x1F4)

    #C0077
    ChrTalk(
        0xA,
        "#14011F#5P还、还要继续吗！？\x02",
    )

    CloseMessageWindow()
    OP_93(0xA, 0xB4, 0x1F4)
    Sleep(150)

    #C0078
    ChrTalk(
        0xA,
        (
            "#14007F#11P喂，你不要在一边干看着，\x01",
            "赶快制止她啊！\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0x101,
        (
            "#00006F#6P……唉，你还是放弃吧。\x02\x03",

            "#00012F只要一牵扯到咪西，\x01",
            "缇欧就停不下来了。\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0xA,
        "#14006F#11P所以已经放弃阻止了吗！？\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(24375, 1500)
    FadeToDark(1500, 0, -1)
    OP_0D()
    Sleep(500)
    SetChrName("")

    #A0081
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "不久后，购物完毕的\x01",
            "同伴们也陆续来到了\x01",
            "事先约定的集合地点。\x02\x03",

            "罗伊德等人向公园门口\x01",
            "的检票员出示了入场券，\x01",
            "进入主题公园。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    RemoveParty(0x52, 0xFF)
    StopSound(821, 1000, 40)
    StopBGM(0xFA0)
    WaitBGM()
    SetScenarioFlags(0x22, 0)
    NewScene("t1300", 0, 0, 0)
    IdleLoop()
    Jump("loc_224E")

    label("loc_2192")


    def lambda_2197():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_2197)
    Sleep(50)

    def lambda_21A7():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_21A7)
    WaitChrThread(0x8, 2)
    WaitChrThread(0xA, 2)

    #C0082
    ChrTalk(
        0x8,
        (
            "#00200F#11P已经快到集合时间了，\x01",
            "如果还有事情，就快点去办吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0xA,
        (
            "#14003F#11P哼……\x01",
            "快去快回啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_93(0x8, 0x10E, 0x0)
    OP_93(0xA, 0x5A, 0x0)
    OP_4C(0x8, 0xFF)
    OP_4C(0xA, 0xFF)
    SetChrPos(0x0, -8000, 4000, -12500, 0)
    EventEnd(0x5)
    Jump("loc_224E")

    label("loc_224E")

    Return()

    # Function_19_182D end

    def Function_20_224F(): pass

    label("Function_20_224F")

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
    OP_90(0x101, -4000, 5000, -30300, 0)
    OP_90(0x102, -4900, 5000, -31000, 0)
    OP_90(0x103, -3100, 5000, -31200, 0)
    OP_90(0x104, -4000, 5000, -32000, 0)
    ClearChrFlags(0x24, 0x80)
    OP_78(0x0, 0x24)
    OP_49()
    SetChrPos(0x24, 0, 4150, -17000, 195)
    OP_D5(0x24, 0x0, 0x2F9B8, 0x0, 0x0)
    ClearMapObjFlags(0x0, 0x4)
    OP_74(0x0, 0x1E)
    OP_71(0x0, 0xA, 0x2B, 0x0, 0x20)
    SetChrFlags(0x24, 0x8000)
    SetChrFlags(0x24, 0x1)
    OP_52(0x24, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x1D4C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x24, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_75(0x0, 0x1, 0x0)
    OP_A7(0x24, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_68(-4000, 3000, -26000, 0)
    MoveCamera(330, 20, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(17500, 0)
    FadeToBright(1000, 0)
    SetCameraDistance(16500, 2500)

    def lambda_23AA():
        OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_23AA)
    Sleep(100)

    def lambda_23C2():
        OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_23C2)
    Sleep(100)

    def lambda_23DA():
        OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_23DA)
    Sleep(100)

    def lambda_23F2():
        OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_23F2)
    WaitChrThread(0x103, 1)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0084
    ChrTalk(
        0x103,
        (
            "#00207F#6P感应到了灵压的上升！\x01",
            "大家小心！\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0x101,
        "#00010F#5P什么……！？\x02",
    )

    CloseMessageWindow()
    StopBGM(0xBB8)
    OP_68(0, 6150, -17000, 2500)
    MoveCamera(330, 20, 0, 2500)
    SetCameraDistance(15500, 2500)
    OP_6F(0x79)
    SetCameraDistance(17500, 3000)
    Sound(919, 0, 100, 0)
    BeginChrThread(0x24, 0, 0, 21)
    BlurSwitch(0x3E8, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    PlayEffect(0x0, 0xFF, 0x24, 0x0, 0, 1500, 0, 0, 0, 0, 3000, 3000, 3000, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7454", 0)
    Sleep(490)

    def lambda_2514():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x24, 2, lambda_2514)
    OP_75(0x0, 0x2, 0x3E8)
    WaitChrThread(0x24, 2)
    CancelBlur(1000)
    EndChrThread(0x24, 0x0)
    OP_6F(0x79)
    OP_68(-760, 4750, -26040, 2000)
    MoveCamera(336, 3, 0, 2000)
    OP_6E(650, 2000)
    SetCameraDistance(16870, 2000)
    Sleep(1500)
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

    #C0086
    ChrTalk(
        0x102,
        "#00110F#5P这、这是……\x02",
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x104,
        "#00307F#5P这不是出现在湿地的怪物吗！？\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_71(0x0, 0x40, 0x63, 0x0, 0x8)
    Sound(842, 0, 100, 0)
    OP_82(0x64, 0x64, 0x1F40, 0x3E8)
    BlurSwitch(0x12C, 0xBBFFFFFF, 0x0, 0x1, 0xA)
    Sleep(300)
    CancelBlur(1000)
    OP_79(0x0)
    OP_71(0x0, 0xA, 0x2B, 0x0, 0x20)
    Sleep(800)

    #C0088
    ChrTalk(
        0x103,
        (
            "#00207F#5P已经确认到了\x01",
            "上级三属性的发动……！\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0x101,
        (
            "#00007F#5P没时间发呆了！\x01",
            "开始迎击！\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x104,
        "#00301F#5P收到！\x02",
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x102,
        "#00107F#5P明白！\x02",
    )

    CloseMessageWindow()
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
    OP_71(0x0, 0xD4, 0xE4, 0x0, 0x8)
    OP_79(0x0)
    ClearChrFlags(0x24, 0x1)
    BlurSwitch(0x2BC, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    OP_68(-1850, 3450, -26400, 800)
    SetCameraDistance(13000, 750)
    Sound(809, 0, 100, 0)
    Sound(251, 0, 100, 0)
    OP_74(0x0, 0x10)
    OP_71(0x0, 0xE5, 0xF8, 0x0, 0x8)

    def lambda_277C():
        OP_9D(0xFE, 0xFFFFF6D2, 0xB40, 0xFFFFA6FA, 0x708, 0x1388)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_277C)
    Sleep(600)
    EndChrThread(0x24, 0x1)
    Battle("BattleInfo_E4", 0x0, 0x0, 0x0, 0x28, 0xFF)
    FadeToDark(0, 0, -1)
    Call(0, 22)
    Return()

    # Function_20_224F end

    def Function_21_27B9(): pass

    label("Function_21_27B9")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_27DD")
    OP_82(0x64, 0x64, 0x1F40, 0x1F4)
    Sleep(500)
    Jump("Function_21_27B9")

    label("loc_27DD")

    Return()

    # Function_21_27B9 end

    def Function_22_27DE(): pass

    label("Function_22_27DE")

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
    OP_90(0x101, -4000, 5000, -21000, 45)
    OP_90(0x102, -5000, 5000, -22000, 45)
    OP_90(0x103, -3000, 5000, -22000, 45)
    OP_90(0x104, -4000, 5000, -23000, 45)
    ClearChrFlags(0x24, 0x80)
    OP_78(0x0, 0x24)
    OP_49()
    SetChrPos(0x24, 0, 4150, -17000, 195)
    OP_D5(0x24, 0x0, 0x2F9B8, 0x0, 0x0)
    ClearMapObjFlags(0x0, 0x4)
    OP_74(0x0, 0x1E)
    OP_71(0x0, 0xA, 0x2B, 0x0, 0x20)
    SetChrFlags(0x24, 0x8000)
    SetChrFlags(0x24, 0x1)
    OP_52(0x24, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x1D4C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x24, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_75(0x0, 0x2, 0x0)
    OP_A7(0x24, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_68(0, 6150, -17000, 0)
    MoveCamera(0, 30, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(16500, 0)
    FadeToBright(1000, 0)
    MoveCamera(330, 20, 0, 3000)
    SetCameraDistance(19500, 3000)
    Sound(919, 0, 80, 0)
    Sound(842, 0, 100, 0)
    BeginChrThread(0x24, 0, 0, 21)
    BeginChrThread(0x24, 3, 0, 23)
    BlurSwitch(0x3E8, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    PlayEffect(0x0, 0x0, 0x24, 0x0, 0, 0, 0, 0, 0, 0, 2500, 2500, 2500, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    PlayEffect(0x1, 0x1, 0x24, 0x0, 0, 0, 0, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)

    def lambda_29F9():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x24, 2, lambda_29F9)
    OP_75(0x0, 0x1, 0x3E8)
    WaitChrThread(0x24, 2)
    CancelBlur(1000)
    EndChrThread(0x24, 0x3)
    EndChrThread(0x24, 0x0)
    StopEffect(0x0, 0x2)
    StopEffect(0x1, 0x2)
    OP_6F(0x79)
    OP_0D()
    SetMapObjFlags(0x0, 0x4)
    SetChrFlags(0x24, 0x80)
    Sleep(500)
    OP_68(-4000, 4400, -22000, 3000)
    MoveCamera(0, 20, 0, 3000)
    OP_6E(650, 3000)
    SetCameraDistance(15000, 3000)
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

    #C0092
    ChrTalk(
        0x104,
        (
            "#00310F#6P啧……『幻兽』为何会\x01",
            "出现在这种地方？\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x103,
        (
            "#00203F#5P不清楚……\x02\x03",

            "#00201F不过，我想应该与\x01",
            "灵压的上升有关。\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x102,
        (
            "#00106F#6P另外，也许和\x01",
            "『僧院』的情况一样，\x01",
            "与钟声存在着一定关系……\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0x101,
        (
            "#00008F#5P琪雅和亚里欧斯先生\x01",
            "在那种地方……\x02\x03",

            "#00013F总之，我们赶快进去！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_82(0xC8, 0x0, 0xBB8, 0x12C)

    #C0096
    ChrTalk(
        0x102,
        "#00107F#1K#1P嗯！\x02",
    )


    #C0097
    ChrTalk(
        0x103,
        "#00201F#1K#2P是！\x02",
    )


    #C0098
    ChrTalk(
        0x104,
        "#00307F#1K#6P好！\x02",
    )

    #Sound(2153, 255, 100, 0)    #voice#Elie
    #Sound(2249, 255, 100, 1)    #voice#Tio
    #Sound(2343, 255, 100, 2)    #voice#Randy
    OP_57(0x1)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_D7(0x20)
    OP_D7(0x21)
    SetChrPos(0x0, -4000, 4000, -19000, 0)
    OP_69(0xFF, 0x0)
    SetScenarioFlags(0x182, 6)
    OP_29(0xAD, 0x1, 0x3)
    ModifyEventFlags(0, 0, 0x80)
    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    # Function_22_27DE end

    def Function_23_2C4F(): pass

    label("Function_23_2C4F")

    OP_71(0x0, 0x157, 0x16C, 0x0, 0x8)
    OP_79(0x0)
    OP_71(0x0, 0x16D, 0x17E, 0x0, 0x20)
    Return()

    # Function_23_2C4F end

    def Function_24_2C6B(): pass

    label("Function_24_2C6B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch41950.itc", 0x1E)
    LoadChrToIndex("chr/ch41951.itc", 0x1F)
    LoadChrToIndex("chr/ch41952.itc", 0x20)
    LoadEffect(0x0, "battle/btgun00.eff")
    LoadEffect(0x1, "event/ev606_00.eff")
    SoundLoad(865)
    SoundLoad(861)
    SoundLoad(2953)
    SoundLoad(2954)
    SetChrFlags(0x101, 0x8)
    SetChrFlags(0x103, 0x8)
    SetChrFlags(0x104, 0x8)
    SetChrFlags(0x105, 0x8)
    SetChrFlags(0x109, 0x8)
    SetChrFlags(0x106, 0x8)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x1F, 0x80)
    ClearChrFlags(0x20, 0x80)
    SetChrChipByIndex(0x19, 0x1E)
    SetChrChipByIndex(0x1A, 0x1E)
    SetChrChipByIndex(0x1B, 0x1E)
    SetChrChipByIndex(0x1C, 0x1E)
    SetChrChipByIndex(0x1D, 0x1E)
    SetChrChipByIndex(0x1E, 0x1E)
    SetChrChipByIndex(0x1F, 0x1E)
    SetChrChipByIndex(0x20, 0x1E)
    SetChrSubChip(0x19, 0x0)
    SetChrSubChip(0x1A, 0x0)
    SetChrSubChip(0x1B, 0x0)
    SetChrSubChip(0x1C, 0x0)
    SetChrSubChip(0x1D, 0x0)
    SetChrSubChip(0x1E, 0x0)
    SetChrSubChip(0x1F, 0x0)
    SetChrSubChip(0x20, 0x0)
    SetChrFlags(0x19, 0x8000)
    SetChrFlags(0x1A, 0x8000)
    SetChrFlags(0x1B, 0x8000)
    SetChrFlags(0x1C, 0x8000)
    SetChrFlags(0x1D, 0x8000)
    SetChrFlags(0x1E, 0x8000)
    SetChrFlags(0x1F, 0x8000)
    SetChrFlags(0x20, 0x8000)
    SetChrPos(0x19, -2500, 0, -32000, 0)
    SetChrPos(0x1A, -3300, 0, -33500, 0)
    SetChrPos(0x1B, -4100, 0, -31500, 0)
    SetChrPos(0x1C, -4900, 0, -33000, 0)
    SetChrPos(0x1D, 2500, 0, -33500, 315)
    SetChrPos(0x1E, 3300, 0, -32000, 315)
    SetChrPos(0x1F, 4100, 0, -33000, 315)
    SetChrPos(0x20, 4900, 0, -31500, 315)
    ClearChrFlags(0x18, 0x80)
    OP_78(0x1, 0x18)
    OP_49()
    SetChrPos(0x18, 0, 4150, -17000, 180)
    OP_D5(0x18, 0x0, 0x2BF20, 0x0, 0x0)
    ClearMapObjFlags(0x1, 0x4)
    OP_74(0x1, 0x1E)
    OP_71(0x1, 0x3D, 0x64, 0x0, 0x20)
    SetChrFlags(0x18, 0x8000)
    SetChrFlags(0x18, 0x1)
    OP_52(0x18, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x1D4C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapObjFrame(0x1, "879mabuta:Layer1(43)", 0x0, 0x1)
    SetMapObjFrame(0x1, "879mabuta:Layer2(44)", 0x0, 0x1)
    OP_68(0, 8500, -17000, 0)
    MoveCamera(40, 38, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(15000, 0)
    FadeToBright(1000, 0)
    OP_68(0, 7000, -17000, 2500)
    MoveCamera(0, -3, 0, 2500)
    SetCameraDistance(24000, 2500)
    Sound(913, 0, 100, 0)
    Sound(833, 0, 100, 0)
    OP_82(0x12C, 0x12C, 0xBB8, 0xBB8)
    BlurSwitch(0x5DC, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    OP_74(0x1, 0xF)
    OP_71(0x1, 0x65, 0x8C, 0x0, 0x8)
    OP_79(0x1)
    CancelBlur(500)
    OP_71(0x1, 0x3D, 0x64, 0x0, 0x20)
    OP_6F(0x79)
    OP_0D()
    Sleep(1000)
    Fade(1000)
    SetChrPos(0x18, 0, 3900, -17000, 180)
    OP_68(0, 4550, -30000, 0)
    OP_68(0, 3550, -30000, 1500)
    MoveCamera(335, 0, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(20500, 0)
    Sleep(500)
    OP_63(0x19, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_63(0x1C, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(50)
    OP_63(0x1E, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_63(0x1B, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(50)
    OP_63(0x1F, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_63(0x1A, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(50)
    OP_63(0x1D, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_63(0x20, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    #C0099
    ChrTalk(
        0x19,
        "#5P哇啊！？\x02",
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0x1E,
        "#11P这就是报告中提到的『神狼』吗！？\x02",
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0x1A,
        (
            "#5P不要胆怯！\x01",
            "配合好，开始『狩猎』！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    SetMessageWindowPos(180, 100, -1, -1)
    OP_82(0xC8, 0x0, 0xBB8, 0x12C)
    SetChrName("众猎兵")

    #A0102
    AnonymousTalk(
        0xFF,
        "#4S是！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_82(0x0, 0x64, 0xBB8, 0x1770)
    OP_68(0, 4550, -25000, 6000)
    MoveCamera(25, 0, 0, 6000)
    BeginChrThread(0x25, 1, 0, 28)
    BeginChrThread(0x19, 3, 0, 25)
    Sleep(50)
    BeginChrThread(0x1A, 3, 0, 25)
    Sleep(50)
    BeginChrThread(0x1B, 3, 0, 25)
    Sleep(50)
    BeginChrThread(0x1C, 3, 0, 25)
    Sleep(50)
    OP_93(0x1D, 0x0, 0x0)
    BeginChrThread(0x1D, 3, 0, 25)
    Sleep(50)
    OP_93(0x1E, 0x0, 0x0)
    BeginChrThread(0x1E, 3, 0, 25)
    Sleep(50)
    OP_93(0x1F, 0x0, 0x0)
    BeginChrThread(0x1F, 3, 0, 25)
    Sleep(50)
    OP_93(0x20, 0x0, 0x0)
    BeginChrThread(0x20, 3, 0, 25)
    Sleep(1000)
    BeginChrThread(0x18, 0, 0, 26)
    OP_6F(0x79)
    Fade(500)
    SetChrPos(0x18, 0, 4150, -17000, 180)
    OP_68(-670, 8200, -20260, 0)
    MoveCamera(35, 15, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(14000, 0)
    SetCameraDistance(13000, 2000)
    Sleep(1000)
    Fade(250)
    SetMapObjFrame(0x1, "879mabuta:Layer1(43)", 0x1, 0x1)
    SetMapObjFrame(0x1, "879mabuta:Layer2(44)", 0x1, 0x1)
    OP_6F(0x79)
    OP_C9(0x0, 0x80000000)
    SetMessageWindowPos(40, 150, -1, -1)
    SetChrName("神狼蔡特")

    #A0103
    AnonymousTalk(
        0xFF,
        "#2953V#3C#4S#40W#35A嗯，斗志可嘉。\x02",
    )
    #Auto

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    SetMapObjFrame(0x1, "879mabuta:Layer1(43)", 0x0, 0x1)
    SetMapObjFrame(0x1, "879mabuta:Layer2(44)", 0x0, 0x1)
    SetCameraDistance(11500, 500)
    Sleep(1000)
    SetMessageWindowPos(20, 150, -1, -1)
    OP_82(0xC8, 0x0, 0xBB8, 0x320)
    SetChrName("神狼蔡特")

    #A0104
    AnonymousTalk(
        0xFF,
        (
            "#2954V#3C#5S#30W#40A既然如此，\x01",
            "我也不必客气了！\x02",
        )
    )
    #Auto

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x80000000)
    OP_68(0, 7500, -20000, 1000)
    MoveCamera(25, 9, 0, 1000)
    SetCameraDistance(15000, 1000)
    EndChrThread(0x25, 0x1)
    Sound(913, 0, 100, 0)
    OP_82(0x0, 0x32, 0x1388, 0x3E8)
    OP_74(0x1, 0x1E)
    OP_71(0x1, 0x1E0, 0x1EA, 0x0, 0x8)
    OP_79(0x1)
    OP_71(0x1, 0x118, 0x12C, 0x0, 0x8)
    OP_79(0x1)
    OP_6F(0x79)
    OP_82(0x1F4, 0x1F4, 0x1388, 0x1F4)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    Sleep(1)
    CancelBlur(2000)
    OP_68(0, 7500, -28000, 500)
    MoveCamera(15, 0, 0, 500)
    SetCameraDistance(22000, 500)
    ClearChrFlags(0x18, 0x1)
    Sound(251, 0, 100, 0)
    Sound(833, 0, 100, 0)
    BeginChrThread(0x18, 3, 0, 27)
    Sleep(500)
    FadeToDark(500, 0, -1)
    StopSound(861, 1000, 50)
    StopSound(865, 1000, 50)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 2)
    NewScene("t1310", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_24_2C6B end

    def Function_25_33FF(): pass

    label("Function_25_33FF")

    SetChrChipByIndex(0xFE, 0x1F)
    SetChrSubChip(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x4)
    OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x1388, 0x0)
    TurnDirection(0xFE, 0x18, 500)
    SetChrChipByIndex(0xFE, 0x20)
    SetChrSubChip(0xFE, 0x0)
    Sleep(100)

    label("loc_342D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_34FD")
    PlayEffect(0x0, 0xFF, 0xFE, 0x5, 0, 1250, 1400, 0, 0, 0, 750, 750, 750, 0xFF, 0, 0, 0, 0)
    OP_A1(0xFE, 0xFA0, 0x2, 0x2, 0x1)
    PlayEffect(0x0, 0xFF, 0xFE, 0x5, 0, 1250, 1400, 0, 0, 0, 750, 750, 750, 0xFF, 0, 0, 0, 0)
    OP_A1(0xFE, 0xFA0, 0x2, 0x2, 0x1)
    PlayEffect(0x0, 0xFF, 0xFE, 0x5, 0, 1250, 1400, 0, 0, 0, 750, 750, 750, 0xFF, 0, 0, 0, 0)
    OP_A1(0xFE, 0xFA0, 0x2, 0x2, 0x1)
    Sleep(1000)
    Jump("loc_342D")

    label("loc_34FD")

    Return()

    # Function_25_33FF end

    def Function_26_34FE(): pass

    label("Function_26_34FE")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_36DE")
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, 3620, 4000, -18000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, 380, 2970, -22580, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, -1120, 3400, -21510, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(150)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, -3740, 4000, -18570, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, -5270, 3340, -21650, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, 4550, 2940, -22640, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, -3250, 4160, -14820, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, 6190, 4000, -15970, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(150)
    Jump("Function_26_34FE")

    label("loc_36DE")

    Return()

    # Function_26_34FE end

    def Function_27_36DF(): pass

    label("Function_27_36DF")


    def lambda_36E4():
        OP_9D(0xFE, 0x0, 0x0, 0xFFFF6F78, 0xBB8, 0x7D0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_36E4)
    OP_74(0x1, 0x5)
    OP_71(0x1, 0x1EA, 0x1EF, 0x64, 0x8)
    OP_79(0x1)
    Return()

    # Function_27_36DF end

    def Function_28_3710(): pass

    label("Function_28_3710")

    Sleep(1200)
    Sound(861, 2, 60, 0)

    label("loc_3719")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_373B")
    Sound(865, 2, 60, 0)
    Sleep(1000)
    StopSound(865, 200, 50)
    Sleep(400)
    Jump("loc_3719")

    label("loc_373B")

    Return()

    # Function_28_3710 end

    def Function_29_373C(): pass

    label("Function_29_373C")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(780, 1600, -58060, 0)
    MoveCamera(315, 28, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(25500, 0)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x8000)
    SetChrFlags(0xA, 0x8000)
    SetChrFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x8000)
    SetChrFlags(0xE, 0x8000)
    SetChrFlags(0x11, 0x8000)
    SetChrFlags(0x12, 0x8000)
    SetChrFlags(0x13, 0x8000)
    SetChrPos(0x101, 600, 0, -62250, 0)
    SetChrPos(0x153, -600, 0, -62250, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x153, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_37E0():
        OP_95(0xFE, 600, 0, -57250, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_37E0)

    def lambda_37FA():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_37FA)
    Sleep(200)

    def lambda_380E():
        OP_95(0xFE, -600, 0, -57250, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x153, 1, lambda_380E)

    def lambda_3828():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x153, 2, lambda_3828)
    Sound(107, 0, 100, 0)
    SetCameraDistance(25000, 1000)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x101, 1)
    WaitChrThread(0x153, 1)
    WaitChrThread(0x101, 2)
    WaitChrThread(0x153, 2)
    OP_63(0x153, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    #Sound(3029, 255, 100, 0)    #voice#KeA

    #C0105
    ChrTalk(
        0x153,
        "#01102F哇……！\x02",
    )

    CloseMessageWindow()
    OP_68(0, 4500, -47400, 3000)
    MoveCamera(0, 0, 0, 3000)
    OP_6E(600, 3000)
    SetCameraDistance(10020, 3000)
    OP_6F(0x79)
    OP_25(0x335, 0x50)
    Fade(1000)
    PlayEffect(0x0, 0x0, 0xFF, 0x0, 0, 4250, -9800, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_68(-20, 9500, -8210, 0)
    MoveCamera(337, 10, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(27300, 0)
    OP_68(-20, 5300, -8210, 8000)
    OP_6F(0x1)
    OP_0D()
    OP_25(0x335, 0x28)
    Fade(1000)
    StopEffect(0x0, 0x0)
    OP_68(780, 1600, -58060, 0)
    MoveCamera(315, 28, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(25000, 0)
    OP_0D()

    #C0106
    ChrTalk(
        0x153,
        "#01109F#5P……罗伊德，好棒啊！！\x02",
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0x101,
        (
            "#00009F#6P嗯，连我都\x01",
            "有点兴奋呢。\x02\x03",

            "#00000F嗯……\x01",
            "说不定已经有人\x01",
            "先到了。\x02\x03",

            "我们过去看看吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0x153,
        "#01110F#5P嗯！！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x15B, 1)
    ClearMapFlags(0x10000000)
    ClearChrFlags(0x8, 0x8000)
    ClearChrFlags(0x9, 0x8000)
    ClearChrFlags(0xA, 0x8000)
    ClearChrFlags(0xC, 0x8000)
    ClearChrFlags(0xD, 0x8000)
    ClearChrFlags(0xE, 0x8000)
    ClearChrFlags(0x11, 0x8000)
    ClearChrFlags(0x12, 0x8000)
    ClearChrFlags(0x13, 0x8000)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 0, 0, -57250, 0)
    EventEnd(0x5)
    Return()

    # Function_29_373C end

    def Function_30_3A6C(): pass

    label("Function_30_3A6C")

    EventBegin(0x0)
    OP_4B(0x17, 0xFF)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-5830, 7000, -1410, 0)
    MoveCamera(306, 32, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(16500, 0)
    SetChrPos(0x101, -8720, 4000, -6130, 0)
    SetChrPos(0x102, -7550, 4000, -6410, 0)
    SetChrPos(0x103, -9480, 4000, -6890, 0)
    SetChrPos(0x104, -7960, 4000, -7290, 0)
    SetChrPos(0x109, -8800, 4000, -8240, 0)
    SetChrPos(0x105, -7400, 4000, -8240, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()

    #C0109
    ChrTalk(
        0x17,
        (
            "#11P啊啊，真是麻烦了啊。\x01",
            "按照计划表，上午也有\x01",
            "表演活动的……\x02",
        )
    )

    CloseMessageWindow()
    OP_68(-6020, 6700, -2510, 3000)
    MoveCamera(310, 29, 0, 3000)
    OP_6E(400, 3000)
    SetCameraDistance(20870, 3000)

    def lambda_3BA4():
        OP_97(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3BA4)
    Sleep(50)

    def lambda_3BC1():
        OP_97(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3BC1)
    Sleep(50)

    def lambda_3BDE():
        OP_97(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_3BDE)
    Sleep(50)

    def lambda_3BFB():
        OP_97(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3BFB)
    Sleep(50)

    def lambda_3C18():
        OP_97(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_3C18)
    Sleep(50)

    def lambda_3C35():
        OP_97(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_3C35)
    WaitChrThread(0x105, 1)
    OP_6F(0x79)

    #C0110
    ChrTalk(
        0x101,
        (
            "#00000F那个，打扰了，\x01",
            "我们是特别任务支援科的成员。\x02\x03",

            "您就是提出支援请求\x01",
            "的亨克斯先生吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x17, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0111
    ChrTalk(
        0x17,
        (
            "哦哦！哦哦！\x01",
            "你们就是特别任务支援科的人吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0x17,
        "嗯……嗯嗯……\x02",
    )

    CloseMessageWindow()
    OP_93(0x17, 0xE1, 0x1F4)
    Sleep(1000)
    OP_93(0x17, 0xB4, 0x1F4)
    Sleep(1000)

    #C0113
    ChrTalk(
        0x17,
        (
            "……好，你的体型\x01",
            "应该很合适！\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0x101,
        "#00005F体、体型……？\x02",
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0x102,
        (
            "#6P#00100F那个……如果可以，\x01",
            "能把委托的详情告诉我们吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0x17,
        (
            "啊，把这个都给忘了！\x01",
            "我可真是的……\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0x17,
        (
            "……我想你们\x01",
            "肯定知道\x01",
            "『咪西』吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0x103,
        "#00203F嗯，还算有一定了解。\x02",
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0x104,
        (
            "#6P#00306F阿缇明明是\x01",
            "狂热级别的支持者……\x02\x03",

            "#00300F说起来，住在克洛斯贝尔的人\x01",
            "几乎没有不知道\x01",
            "咪西的吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0x105,
        (
            "#6P#10300F咪西出什么\x01",
            "问题了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0x17,
        (
            "哦，其实……\x01",
            "我今天早上接到了联络。\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0x17,
        (
            "从建园时就一直\x01",
            "扮演咪西的那位工作人员\x01",
            "今天有事不能来了。\x02",
        )
    )

    CloseMessageWindow()
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
    Sleep(1000)

    #C0123
    ChrTalk(
        0x109,
        (
            "#6P#10105F有事……\x01",
            "莫非出现什么问题了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0x17,
        "听说是突然肚子疼。\x02",
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0x17,
        (
            "他去乌尔斯拉医院\x01",
            "取过药之后\x01",
            "就会赶过来……\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0x17,
        (
            "但上午的\x01",
            "活动肯定\x01",
            "赶不上了。\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0x17,
        (
            "所以……\x01",
            "希望你们穿上咪西的扮演装，\x01",
            "暂时替代工作人员扮演咪西。\x02",
        )
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0x101,
        "#00005F扮演咪西……！？\x02",
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0x104,
        (
            "#6P#00309F嘿……\x01",
            "这不是很有趣嘛。\x02\x03",

            "#00304F好，那就由我来……！\x02",
        )
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0x17,
        (
            "不行，你的身材不太符合\x01",
            "扮演装的尺寸。\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0x17,
        (
            "那位看上去\x01",
            "很正派的先生\x01",
            "倒是非常合适。\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0x101,
        "#00011F我、我吗？\x02",
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0x104,
        (
            "#6P#4S#00307F（失望！！）\x02\x03",

            "#00306F本想趁机亲近一下\x01",
            "入园游玩的女孩呢……！\x02\x03",

            "#00310F可恶的罗伊德……！\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0x101,
        "#00006F那、那个……\x02",
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0x109,
        "#6P#10112F不要为这种事情闹别扭嘛……\x02",
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0x17,
        (
            "那么……\x01",
            "你们可以接受\x01",
            "这件工作吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0x101,
        (
            "#00000F明白了，\x01",
            "我们接受。\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0x17,
        (
            "啊啊，太谢谢了。\x01",
            "那就请各位赶快跟我来……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    Sleep(2000)
    OP_64(0x103)
    TurnDirection(0x102, 0x103, 500)
    Sleep(300)

    #C0139
    ChrTalk(
        0x102,
        (
            "#12P#00105F……缇欧？\x01",
            "你怎么了？一直沉默不语……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_42B4():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_42B4)
    Sleep(50)

    def lambda_42C4():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_42C4)
    Sleep(50)

    def lambda_42D4():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_42D4)
    Sleep(300)

    #C0140
    ChrTalk(
        0x103,
        (
            "#00205F……咪西扮演装……里面的人……\x01",
            "肚子疼………取药……………\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0141
    ChrTalk(
        0x109,
        (
            "#6P#10111F（她、她的样子\x01",
            "  好像很奇怪呢……）\x02",
        )
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0x105,
        (
            "#6P#10303F（听到这种破坏幻想的\x01",
            "  幕后内情，\x01",
            "  肯定会受到不小的打击吧。）\x02",
        )
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0x101,
        (
            "#11P#00011F（说、说的也是……）\x02\x03",

            "#00012F……那、那个……缇欧？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 500)
    Sleep(300)

    #C0144
    ChrTalk(
        0x103,
        (
            "#00203F……我不要紧。\x02\x03",

            "#00201F既然是为了咪西，\x01",
            "我也很愿意帮忙。\x02",
        )
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0x104,
        "#12P#00309F哈哈，就是要有这股干劲。\x02",
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0x101,
        "#11P#00006F（真的不要紧吗……）\x02",
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0x17,
        "你们已经商量好了吧？\x02",
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0x17,
        (
            "那就请大家跟我去\x01",
            "更衣室。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4540():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_4540)
    Sleep(50)

    def lambda_4550():
        OP_93(0x102, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_4550)
    Sleep(50)

    def lambda_4560():
        OP_93(0x103, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_4560)
    Sleep(50)

    def lambda_4570():
        OP_93(0x104, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_4570)
    Sleep(50)

    def lambda_4580():
        OP_93(0x105, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_4580)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x105, 0)

    #C0149
    ChrTalk(
        0x101,
        (
            "#00012F啊……\x01",
            "是的，麻烦您带路吧。\x02",
        )
    )

    CloseMessageWindow()
    StopSound(821, 1000, 30)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(80, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0150
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "任务【主题公园的兼职】\x07\x00",
            "开始！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x176, 4)
    SetScenarioFlags(0x22, 0)
    NewScene("t1390", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_30_3A6C end

    def Function_31_462B(): pass

    label("Function_31_462B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch10200.itc", 0x1E)
    LoadChrToIndex("chr/ch45400.itc", 0x1F)
    LoadChrToIndex("chr/ch20200.itc", 0x20)
    LoadChrToIndex("chr/ch20300.itc", 0x21)
    LoadChrToIndex("chr/ch23800.itc", 0x22)
    LoadEffect(0x0, "battle/ms00109.eff")
    SoundLoad(862)
    SoundLoad(645)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x103, 0x1F)
    SetChrSubChip(0x103, 0x0)
    SetChrFlags(0x103, 0x1000)
    SetChrChipByIndex(0x21, 0x20)
    SetChrFlags(0x21, 0x8000)
    SetChrChipByIndex(0x22, 0x21)
    SetChrFlags(0x22, 0x8000)
    SetChrChipByIndex(0x23, 0x22)
    SetChrFlags(0x23, 0x8000)
    OP_52(0x23, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_68(3220, 7060, -19270, 0)
    MoveCamera(315, 20, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(19020, 0)
    SetChrPos(0x101, 360, 4160, -15840, 180)
    SetChrPos(0x103, -1060, 4140, -15840, 180)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrFlags(0x102, 0x80)
    SetChrBattleFlags(0x102, 0x8000)
    SetChrFlags(0x104, 0x80)
    SetChrBattleFlags(0x104, 0x8000)
    SetChrFlags(0x109, 0x80)
    SetChrBattleFlags(0x109, 0x8000)
    SetChrFlags(0x105, 0x80)
    SetChrBattleFlags(0x105, 0x8000)
    SetCameraDistance(17900, 3000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x10)

    #C0151
    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05206F呼……\x01",
            "终于开始了啊。\x01",
            "接下来究竟会……\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0x103,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "#05520F啊，\x01",
            "这么快就有人来了呢。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2300, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_68(3750, 7160, -21000, 5000)
    SetCameraDistance(19340, 5000)
    ClearChrFlags(0x21, 0x80)
    ClearChrFlags(0x22, 0x80)
    ClearChrFlags(0x23, 0x80)
    ClearChrFlags(0x21, 0x4)
    ClearChrFlags(0x22, 0x4)
    ClearChrFlags(0x23, 0x4)
    SetChrPos(0x21, -470, 480, -28790, 0)
    SetChrPos(0x22, 980, 480, -28800, 0)
    SetChrPos(0x23, 130, 1110, -27230, 0)

    def lambda_4832():
        OP_95(0xFE, 130, 4000, -16840, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_4832)
    Sleep(50)

    def lambda_484F():
        OP_95(0xFE, -470, 4000, -18440, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_484F)
    Sleep(50)

    def lambda_486C():
        OP_95(0xFE, 980, 4000, -18640, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_486C)
    Sleep(50)

    def lambda_4889():
        OP_95(0xFE, -7890, 4000, -16239, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_4889)
    WaitChrThread(0x103, 1)

    def lambda_48A7():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_48A7)
    WaitChrThread(0x23, 1)
    OP_6F(0x79)
    OP_63(0x23, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)

    #C0153
    ChrTalk(
        0x23,
        "哇～咪西！\x02",
    )

    CloseMessageWindow()
    OP_93(0x23, 0xB4, 0x3E8)
    Sleep(300)

    #C0154
    ChrTalk(
        0x23,
        (
            "是咪西啊！\x01",
            "这是真正的咪西吗～！？\x02",
        )
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0x21,
        "哈哈，是啊。\x02",
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0x22,
        (
            "呵呵，要是在这种地方\x01",
            "撒欢个没完，\x01",
            "可就没力气进去玩啦～\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x23, 0x0, 0x3E8)
    OP_9C(0x23, 0x0, 0x0, 0x0, 0x1F4, 0xBB8)
    OP_9C(0x23, 0x0, 0x0, 0x0, 0x1F4, 0xBB8)

    #C0157
    ChrTalk(
        0x23,
        (
            "哇哇～哇哇～！\x01",
            "咪西！咪西～！！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x23, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)

    #C0158
    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05203F（嗯、嗯嗯……\x01",
            "  在这种时候，\x01",
            "  应该说些什么呢……？）\x07\x00\x02",
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
            "咪嘻嘻，要玩得开心哦～¤\x01",      # 0
            "请去那边买门票哦～¤\x01",          # 1
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
        (0, "loc_4A8D"),
        (1, "loc_4ADC"),
        (SWITCH_DEFAULT, "loc_4B3F"),
    )


    label("loc_4A8D")

    OP_2C(0x86, 0x1)
    SetScenarioFlags(0x176, 5)

    #C0159
    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "咪嘻嘻，要玩得开心哦～¤\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0x23,
        "嗯！谢谢你，咪西～！\x02",
    )

    CloseMessageWindow()
    OP_29(0x86, 0x1, 0x1)
    Jump("loc_4B3F")

    label("loc_4ADC")


    #C0161
    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "请去那边买门票哦～¤\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x23, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0162
    ChrTalk(
        0x23,
        (
            "嗯、嗯……\x01",
            "谢谢你，咪西。\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x86, 0x1, 0x2)
    Jump("loc_4B3F")

    label("loc_4B3F")

    OP_93(0x23, 0xB4, 0x3E8)
    Sleep(300)

    #C0163
    ChrTalk(
        0x23,
        (
            "爸爸，妈妈，\x01",
            "我们赶快进去啊～\x02",
        )
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0x21,
        "哈哈，知道啦，知道啦。\x02",
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0x22,
        "今天一定要玩个痛快～\x02",
    )

    CloseMessageWindow()
    OP_68(3220, 7060, -19270, 3000)
    MoveCamera(315, 20, 0, 3000)
    OP_6E(400, 3000)
    SetCameraDistance(19020, 3000)
    BeginChrThread(0x23, 3, 0, 34)
    Sleep(50)
    BeginChrThread(0x22, 3, 0, 33)
    Sleep(50)
    BeginChrThread(0x21, 3, 0, 32)
    Sleep(50)

    def lambda_4BF0():
        TurnDirection(0xFE, 0x23, 500)
        Yield()
        Jump("loc_FFFFABCD")

    QueueWorkItem2(0x101, 1, lambda_4BF0)
    Sleep(300)

    def lambda_4C05():
        OP_95(0xFE, -1060, 4140, -15840, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_4C05)
    WaitChrThread(0x103, 1)

    def lambda_4C23():
        TurnDirection(0xFE, 0x23, 500)
        Yield()
        Jump("loc_FFFFABCD")

    QueueWorkItem2(0x103, 1, lambda_4C23)
    WaitChrThread(0x23, 3)
    WaitChrThread(0x22, 3)
    WaitChrThread(0x21, 3)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x103, 0x1)
    SetChrFlags(0x21, 0x80)
    SetChrFlags(0x22, 0x80)
    SetChrFlags(0x23, 0x80)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4DD0")

    #C0166
    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05202F呼，总算搞定了。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 500)
    Sleep(300)

    #C0167
    ChrTalk(
        0x103,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "#05524F罗伊德前辈，做得好。\x02\x03",

            "#05522F咪西的笑声\x01",
            "也学得很自然。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 500)
    Sleep(300)

    #C0168
    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05212F但、但总觉得\x01",
            "有点不好意思呢。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0x103,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "#05529F咪嘻嘻¤\x02\x03",

            "#05526F……咳咳，\x01",
            "习惯以后就\x01",
            "没什么了。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05212F没、没想到缇欧学得这么好。\x01",
            "（原来要这样笑，\x01",
            "  真是可爱啊……）\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0x103,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "#05522F就保持这种状态，继续加油吧。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4FC6")

    label("loc_4DD0")


    #C0172
    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05202F呼，总算搞定了，做得还算好吧……\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_99(0x103, 0x101, 0xFA, 0x1388, 0x0)
    PlayEffect(0x0, 0x0, 0xFF, 0x0, 360, 4300, -15840, 90, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sound(645, 0, 30, 0)
    Sound(862, 0, 50, 0)
    Sound(811, 0, 100, 0)
    OP_9B(0x1, 0x103, 0xB4, 0x3E8, 0x1388, 0x0)
    Sleep(500)
    #Sound(2030, 255, 70, 0)    #voice#Lloyd

    #C0173
    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05211F呜！？\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0x7EE)
    TurnDirection(0x101, 0x103, 500)
    Sleep(300)

    #C0174
    ChrTalk(
        0x103,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "#05531F……一点都不好。\x02\x03",

            "#05526F罗伊德前辈，咪西并不是\x01",
            "主题公园的工作人员……\x01",
            "不应该说什么『门票』吧？\x02\x03",

            "#05521F身为面带笑容，迎接大家\x01",
            "进入梦幻世界的吉祥物，\x01",
            "那种发言可是最严重的禁语。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0175
    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05206F对、对不起。\x01",
            "（好难啊……）\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0x103,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "#05526F真是的……\x01",
            "下次请认真些。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4FC6")

    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 0)
    NewScene("t1400", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_31_462B end

    def Function_32_4FDE(): pass

    label("Function_32_4FDE")

    OP_97(0x21, 0x1388, 0x0, 0x7D0, 0x7D0, 0x0)
    OP_97(0x21, 0x0, 0x0, 0x1F40, 0x7D0, 0x0)
    Return()

    # Function_32_4FDE end

    def Function_33_5007(): pass

    label("Function_33_5007")

    OP_97(0x22, 0x1388, 0x0, 0x7D0, 0x7D0, 0x0)
    OP_97(0x22, 0x0, 0x0, 0x1F40, 0x7D0, 0x0)
    Return()

    # Function_33_5007 end

    def Function_34_5030(): pass

    label("Function_34_5030")

    OP_97(0x23, 0x1388, 0x0, 0x7D0, 0x7D0, 0x0)
    OP_97(0x23, 0x0, 0x0, 0x1F40, 0x7D0, 0x0)
    Return()

    # Function_34_5030 end

    def Function_35_5059(): pass

    label("Function_35_5059")

    Return()

    # Function_35_5059 end

    def Function_36_505A(): pass

    label("Function_36_505A")

    Return()

    # Function_36_505A end

    def Function_37_505B(): pass

    label("Function_37_505B")

    Sleep(1000)

    label("loc_505E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5080")
    Sound(918, 0, 40, 0)
    Sleep(2200)
    Sound(918, 0, 30, 0)
    Sleep(5000)
    Jump("loc_505E")

    label("loc_5080")

    Return()

    # Function_37_505B end

    def Function_38_5081(): pass

    label("Function_38_5081")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_516C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5126")

    #C0177
    ChrTalk(
        0x101,
        "#00000F这边是主题公园。\x02",
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0x105,
        (
            "#10300F呵呵，下午会来这里玩的，\x01",
            "不用这么着急。\x02",
        )
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0x104,
        (
            "#00309F没错，我们现在还是\x01",
            "赶快去湖水浴场吧！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_516C")

    label("loc_5126")


    #C0180
    ChrTalk(
        0x101,
        (
            "#00000F按照预定计划，下午再来主题公园，\x01",
            "现在还是先去湖水浴场吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_516C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_524D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5209")

    #C0181
    ChrTalk(
        0x153,
        (
            "#01105F罗伊德，\x01",
            "你要先进去吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0x101,
        (
            "#00000F啊，抱歉抱歉，\x01",
            "不应该一个人先进去。\x02\x03",

            "#00004F还是等大家来了之后再一起进去吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_524D")

    label("loc_5209")


    #C0183
    ChrTalk(
        0x101,
        (
            "#00000F哦，不能一个人先进去，\x01",
            "还是等大家来了之后再一起进去吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_524D")

    OP_5A()
    SetChrPos(0x0, 0, 4400, -1250, 180)
    EventEnd(0x4)
    Return()

    # Function_38_5081 end

    def Function_39_5262(): pass

    label("Function_39_5262")

    EventBegin(0x2)
    ClearMapFlags(0x20)
    SetChrName("")

    #A0184
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "张贴着主题公园的\x01",
            "导览地图。\x02\x03",

            "广阔的公园内\x01",
            "遍布着各种各样的\x01",
            "游戏设施。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    EventEnd(0x3)
    Return()

    # Function_39_5262 end

    def Function_40_52BE(): pass

    label("Function_40_52BE")

    EventBegin(0x2)
    ClearMapFlags(0x20)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0185
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "～致前来游玩的客人～\x01\x01",
            "请勿在主题公园内打闹，\x01",
            "禁止将危险物品\x01",
            "带入园内。\x01\x01",
            "儿童需有\x01",
            "监护人的陪伴\x01",
            "方可入园。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    EventEnd(0x3)
    Return()

    # Function_40_52BE end

    SaveToFile()

Try(main)
