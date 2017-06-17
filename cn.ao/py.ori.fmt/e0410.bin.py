from ScenarioHelper import *

def main():
    CreateScenaFile(
        "e0410.bin",                # FileName
        "e0410",                    # MapName
        "e0410",                    # Location
        0x00A0,                     # MapIndex
        "ed7000",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0xFF,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 270, 1, 160, 0, 1, 0, 2],
    )

    BuildStringList((
        "e0410",                  # 0
        "老人",                   # 1
        "商人",                   # 2
        "父亲",                   # 3
        "女孩",                   # 4
        "青年",                   # 5
        "妹妹",                   # 6
        "哥哥",                   # 7
        "护卫",                   # 8
        "秦",                     # 9
        "女孩",                   # 10
        "夫人",                   # 11
        "防护栏",                 # 12
        "假人",                   # 13
        "乘客",                   # 14
        "乘客",                   # 15
        "乘客",                   # 16
        "乘客",                   # 17
        "乘客",                   # 18
        "乘客",                   # 19
        "乘客",                   # 20
        "乘客",                   # 21
        "乘客",                   # 22
        "乘客",                   # 23
        "乘客",                   # 24
        "乘客",                   # 25
        "猎兵",                   # 26
        "猎兵",                   # 27
        "猎兵",                   # 28
        "猎兵",                   # 29
        "猎兵",                   # 30
        "猎兵",                   # 31
        "雾香",                   # 32
        "雷克特",                 # 33
        "假货商",                 # 34
        "共和国恐怖分子",         # 35
        "共和国恐怖分子",         # 36
        "共和国恐怖分子",         # 37
        "黑月成员",               # 38
        "黑月成员",               # 39
    ))

    AddCharChip((
        "chr/ch20802.itc",                   # 00
        "chr/ch21802.itc",                   # 01
        "chr/ch21002.itc",                   # 02
        "chr/ch22302.itc",                   # 03
        "chr/ch22802.itc",                   # 04
        "chr/ch22102.itc",                   # 05
        "chr/ch22002.itc",                   # 06
        "chr/ch47602.itc",                   # 07
        "chr/ch45000.itc",                   # 08
        "chr/ch44202.itc",                   # 09
        "chr/ch21902.itc",                   # 0A
    ))

    DeclNpc(2200,    150,     5739,    180,  421,  0x0, 0,   0,   0,   255, 255, 0,   3,   255,  0)
    DeclNpc(-2259,   150,     1700,    0,    421,  0x0, 0,   1,   0,   255, 255, 0,   4,   255,  0)
    DeclNpc(1769,    150,     699,     180,  421,  0x0, 0,   2,   0,   255, 255, 0,   5,   255,  0)
    DeclNpc(2849,    150,     699,     180,  421,  0x0, 0,   3,   0,   255, 255, 0,   6,   255,  0)
    DeclNpc(-2250,   150,     -1750,   180,  421,  0x0, 0,   4,   0,   255, 255, 0,   7,   255,  0)
    DeclNpc(2200,    150,     3230,    180,  421,  0x0, 0,   5,   0,   255, 255, 0,   8,   255,  0)
    DeclNpc(2220,    150,     1730,    0,    421,  0x0, 0,   6,   0,   255, 255, 0,   9,   255,  0)
    DeclNpc(-1740,   150,     709,     180,  421,  0x0, 0,   7,   0,   255, 255, 0,   10,  255,  0)
    DeclNpc(-3089,   0,       19,      270,  389,  0x0, 0,   8,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(2279,    150,     -1759,   180,  421,  0x0, 0,   9,   0,   255, 255, 0,   12,  255,  0)
    DeclNpc(-2200,   150,     -3250,   0,    421,  0x0, 0,   10,  0,   255, 255, 0,   13,  255,  0)
    DeclNpc(0,       0,       0,       0,    421,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    421,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
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
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 35,  0.0,                   10.5,                  0.0,                   4.0,                   [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -0.0,                  -5.25,                 -0.0,                  1.0])
    DeclEvent(0x0000, 0, 36,  0.0,                   -10.0,                 0.0,                   4.0,                   [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -0.0,                  5.0,                   -0.0,                  1.0])
    DeclEvent(0x0000, 0, 44,  0.0,                   0.0,                   0.0,                   0.0,                   [1.0,                  0.0,                   0.0,                   0.0,                   0.0,                   1.0,                   0.0,                   0.0,                   0.0,                   0.0,                   1.0,                   0.0,                   0.0,                   0.0,                   0.0,                   1.0])
    DeclEvent(0x0000, 0, 19,  0.0,                   9.199999809265137,     0.0,                   4.0,                   [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -0.0,                  -4.599999904632568,    -0.0,                  1.0])
    DeclEvent(0x0000, 0, 20,  3.5,                   -7.849999904632568,    0.0,                   6.25,                  [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.3999999761581421,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.19999998807907104,   0.0,                   -1.75,                 3.1399998664855957,    -0.0,                  1.0])
    DeclEvent(0x0000, 0, 21,  3.5,                   7.849999904632568,     0.0,                   6.25,                  [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.3999999761581421,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.19999998807907104,   0.0,                   -1.75,                 -3.1399998664855957,   -0.0,                  1.0])

    ChipFrameInfo(2304, 0)                                       # 0

    ScpFunction((
        "Function_0_900",          # 00, 0
        "Function_1_9B8",          # 01, 1
        "Function_2_ADF",          # 02, 2
        "Function_3_C65",          # 03, 3
        "Function_4_CDB",          # 04, 4
        "Function_5_D54",          # 05, 5
        "Function_6_DE8",          # 06, 6
        "Function_7_E47",          # 07, 7
        "Function_8_EAE",          # 08, 8
        "Function_9_EFB",          # 09, 9
        "Function_10_F49",         # 0A, 10
        "Function_11_1036",        # 0B, 11
        "Function_12_110C",        # 0C, 12
        "Function_13_118B",        # 0D, 13
        "Function_14_11E4",        # 0E, 14
        "Function_15_1F61",        # 0F, 15
        "Function_16_1F9A",        # 10, 16
        "Function_17_3F98",        # 11, 17
        "Function_18_473B",        # 12, 18
        "Function_19_49C6",        # 13, 19
        "Function_20_4A86",        # 14, 20
        "Function_21_4ACF",        # 15, 21
        "Function_22_4B18",        # 16, 22
        "Function_23_4F74",        # 17, 23
        "Function_24_5437",        # 18, 24
        "Function_25_58A0",        # 19, 25
        "Function_26_5E4D",        # 1A, 26
        "Function_27_5E56",        # 1B, 27
        "Function_28_62FB",        # 1C, 28
        "Function_29_667E",        # 1D, 29
        "Function_30_73E8",        # 1E, 30
        "Function_31_7C57",        # 1F, 31
        "Function_32_8024",        # 20, 32
        "Function_33_8E25",        # 21, 33
        "Function_34_9059",        # 22, 34
        "Function_35_ACD8",        # 23, 35
        "Function_36_AD22",        # 24, 36
        "Function_37_AD6C",        # 25, 37
        "Function_38_ADA3",        # 26, 38
        "Function_39_ADDD",        # 27, 39
        "Function_40_AE17",        # 28, 40
        "Function_41_AE51",        # 29, 41
        "Function_42_AE8B",        # 2A, 42
        "Function_43_AEC5",        # 2B, 43
        "Function_44_D1AC",        # 2C, 44
        "Function_45_EC50",        # 2D, 45
        "Function_46_ECAC",        # 2E, 46
        "Function_47_ED02",        # 2F, 47
        "Function_48_ED3C",        # 30, 48
        "Function_49_ED93",        # 31, 49
        "Function_50_EDEA",        # 32, 50
    ))


    def Function_0_900(): pass

    label("Function_0_900")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_940"),
        (1, "loc_94C"),
        (2, "loc_958"),
        (3, "loc_964"),
        (4, "loc_970"),
        (5, "loc_97C"),
        (6, "loc_988"),
        (SWITCH_DEFAULT, "loc_994"),
    )


    label("loc_940")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_9A0")

    label("loc_94C")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_9A0")

    label("loc_958")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_9A0")

    label("loc_964")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_9A0")

    label("loc_970")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_9A0")

    label("loc_97C")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_9A0")

    label("loc_988")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_9A0")

    label("loc_994")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_9A0")

    label("loc_9A0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_9B7")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_9A0")

    label("loc_9B7")

    Return()

    # Function_0_900 end

    def Function_1_9B8(): pass

    label("Function_1_9B8")

    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    SetChrChipByIndex(0x9, 0x1)
    SetChrSubChip(0x9, 0x0)
    EndChrThread(0x9, 0x0)
    SetChrBattleFlags(0x9, 0x4)
    SetChrChipByIndex(0xA, 0x2)
    SetChrSubChip(0xA, 0x0)
    EndChrThread(0xA, 0x0)
    SetChrBattleFlags(0xA, 0x4)
    SetChrChipByIndex(0xB, 0x3)
    SetChrSubChip(0xB, 0x0)
    EndChrThread(0xB, 0x0)
    SetChrBattleFlags(0xB, 0x4)
    SetChrChipByIndex(0xC, 0x4)
    SetChrSubChip(0xC, 0x0)
    EndChrThread(0xC, 0x0)
    SetChrBattleFlags(0xC, 0x4)
    SetChrChipByIndex(0xD, 0x5)
    SetChrSubChip(0xD, 0x0)
    EndChrThread(0xD, 0x0)
    SetChrBattleFlags(0xD, 0x4)
    SetChrChipByIndex(0xE, 0x6)
    SetChrSubChip(0xE, 0x0)
    EndChrThread(0xE, 0x0)
    SetChrBattleFlags(0xE, 0x4)
    SetChrChipByIndex(0xF, 0x7)
    SetChrSubChip(0xF, 0x0)
    EndChrThread(0xF, 0x0)
    SetChrBattleFlags(0xF, 0x4)
    SetChrChipByIndex(0x11, 0x9)
    SetChrSubChip(0x11, 0x0)
    EndChrThread(0x11, 0x0)
    SetChrBattleFlags(0x11, 0x4)
    SetChrChipByIndex(0x12, 0xA)
    SetChrSubChip(0x12, 0x0)
    EndChrThread(0x12, 0x0)
    SetChrBattleFlags(0x12, 0x4)
    SetChrSubChip(0x11, 0x1)
    SetChrFlags(0x11, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_A7F")
    ClearScenarioFlags(0x22, 0)
    Event(0, 14)
    Jump("loc_ADE")

    label("loc_A7F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_A93")
    ClearScenarioFlags(0x22, 1)
    Event(0, 16)
    Jump("loc_ADE")

    label("loc_A93")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 2)), scpexpr(EXPR_END)), "loc_AA7")
    ClearScenarioFlags(0x22, 2)
    Event(0, 17)
    Jump("loc_ADE")

    label("loc_AA7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 3)), scpexpr(EXPR_END)), "loc_ABB")
    ClearScenarioFlags(0x22, 3)
    Event(0, 18)
    Jump("loc_ADE")

    label("loc_ABB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 4)), scpexpr(EXPR_END)), "loc_ACF")
    ClearScenarioFlags(0x22, 4)
    Event(0, 43)
    Jump("loc_ADE")

    label("loc_ACF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 5)), scpexpr(EXPR_END)), "loc_ADE")
    ClearScenarioFlags(0x22, 5)
    Event(0, 44)

    label("loc_ADE")

    Return()

    # Function_1_9B8 end

    def Function_2_ADF(): pass

    label("Function_2_ADF")

    ClearMapObjFlags(0x0, 0x10)
    ClearMapObjFlags(0x1, 0x10)
    ModifyEventFlags(0, 0, 0x80)
    ModifyEventFlags(0, 1, 0x80)
    ModifyEventFlags(0, 3, 0x80)
    ModifyEventFlags(0, 4, 0x80)
    ModifyEventFlags(0, 5, 0x80)
    SetMapObjFlags(0x6, 0x4)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x79, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x79, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_2A(0x79, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C26")
    ModifyEventFlags(1, 0, 0x80)
    ModifyEventFlags(1, 1, 0x80)
    ModifyEventFlags(1, 4, 0x80)
    ModifyEventFlags(1, 5, 0x80)
    ModifyEventFlags(1, 3, 0x80)
    SetMapObjFlags(0x2, 0x10)
    OP_70(0x2, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x156, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BC8")
    ModifyEventFlags(1, 0, 0x80)
    ModifyEventFlags(0, 1, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x158, 6)), scpexpr(EXPR_END)), "loc_B6B")
    ModifyEventFlags(0, 3, 0x80)

    label("loc_B6B")

    OP_78(0x3, 0x13)
    SetChrPos(0x13, 0, 0, -9450, 0)
    ClearMapObjFlags(0x3, 0x4)
    SetMapObjFlags(0x3, 0x2)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    Jump("loc_C21")

    label("loc_BC8")

    ModifyEventFlags(0, 0, 0x80)
    ModifyEventFlags(1, 1, 0x80)
    ClearMapObjFlags(0x2, 0x10)
    SetMapObjFlags(0x2, 0x2)
    SetMapObjFlags(0x3, 0x4)
    ClearMapObjFlags(0x3, 0x2)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)

    label("loc_C21")

    Jump("loc_C64")

    label("loc_C26")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x81, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x81, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x81, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C64")
    SetMapObjFlags(0x2, 0x10)
    BeginChrThread(0x13, 3, 0, 15)
    SetMapObjFlags(0x4, 0x4)
    OP_74(0x5, 0x2D)
    OP_71(0x5, 0xF0, 0x0, 0x0, 0x20)

    label("loc_C64")

    Return()

    # Function_2_ADF end

    def Function_3_C65(): pass

    label("Function_3_C65")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 1)), scpexpr(EXPR_END)), "loc_CBC")

    #C0001
    ChrTalk(
        0xFE,
        (
            "对、对不起，\x01",
            "能不能再等一下？\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0xFE,
        (
            "我真的买了票，\x01",
            "一定能找到的！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CD7")

    label("loc_CBC")

    Call(0, 25)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CD7")
    Call(0, 26)

    label("loc_CD7")

    TalkEnd(0xFE)
    Return()

    # Function_3_C65 end

    def Function_4_CDB(): pass

    label("Function_4_CDB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 2)), scpexpr(EXPR_END)), "loc_D35")

    #C0003
    ChrTalk(
        0xFE,
        (
            "这次的谈判要是能谈成，\x01",
            "绝对可以大赚一笔！\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0xFE,
        "哼哼，真是期待死了！\x02",
    )

    CloseMessageWindow()
    Jump("loc_D50")

    label("loc_D35")

    Call(0, 24)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D50")
    Call(0, 26)

    label("loc_D50")

    TalkEnd(0xFE)
    Return()

    # Function_4_CDB end

    def Function_5_D54(): pass

    label("Function_5_D54")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 3)), scpexpr(EXPR_END)), "loc_DCC")
    TalkBegin(0xFE)

    #C0005
    ChrTalk(
        0xFE,
        (
            "我们今天要回\x01",
            "共和国的\x01",
            "老家。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0xFE,
        (
            "我女儿很快就能见到\x01",
            "久别多时的爷爷和奶奶了，\x01",
            "她好像很高兴呢。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Jump("loc_DE7")

    label("loc_DCC")

    Call(0, 23)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_DE7")
    Call(0, 26)

    label("loc_DE7")

    Return()

    # Function_5_D54 end

    def Function_6_DE8(): pass

    label("Function_6_DE8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 3)), scpexpr(EXPR_END)), "loc_E2B")
    TalkBegin(0xFE)

    #C0007
    ChrTalk(
        0xFE,
        (
            "爷爷，奶奶，我马上\x01",
            "就去找你们了，等我哦¤\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Jump("loc_E46")

    label("loc_E2B")

    Call(0, 23)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E46")
    Call(0, 26)

    label("loc_E46")

    Return()

    # Function_6_DE8 end

    def Function_7_E47(): pass

    label("Function_7_E47")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 4)), scpexpr(EXPR_END)), "loc_E92")
    TalkBegin(0xFE)

    #C0008
    ChrTalk(
        0xFE,
        (
            "我要回故乡\x01",
            "奥雷德了。\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0xFE,
        "……妈妈不会有事吧……\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Jump("loc_EAD")

    label("loc_E92")

    Call(0, 22)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_EAD")
    Call(0, 26)

    label("loc_EAD")

    Return()

    # Function_7_E47 end

    def Function_8_EAE(): pass

    label("Function_8_EAE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 5)), scpexpr(EXPR_END)), "loc_EDF")
    TalkBegin(0xFE)

    #C0010
    ChrTalk(
        0xFE,
        (
            "真是的，我不管\x01",
            "哥哥了！\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Jump("loc_EFA")

    label("loc_EDF")

    Call(0, 30)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CB, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_EFA")
    Call(0, 31)

    label("loc_EFA")

    Return()

    # Function_8_EAE end

    def Function_9_EFB(): pass

    label("Function_9_EFB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 5)), scpexpr(EXPR_END)), "loc_F2D")
    TalkBegin(0xFE)

    #C0011
    ChrTalk(
        0xFE,
        "哼，真是个不可爱的妹妹。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Jump("loc_F48")

    label("loc_F2D")

    Call(0, 30)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CB, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F48")
    Call(0, 31)

    label("loc_F48")

    Return()

    # Function_9_EFB end

    def Function_10_F49(): pass

    label("Function_10_F49")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 6)), scpexpr(EXPR_END)), "loc_101A")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_FC9")

    #C0012
    ChrTalk(
        0xFE,
        (
            "呵呵，秦少爷似乎\x01",
            "在这次的旅行中获得了\x01",
            "很有意义的经验呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0xFE,
        (
            "这都是托了各位的福。\x01",
            "十分感谢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1012")

    label("loc_FC9")


    #C0014
    ChrTalk(
        0xFE,
        (
            "今天真是晴朗\x01",
            "的好天气啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0xFE,
        "呵呵，这样的天气最适合坐列车出行了。\x02",
    )

    CloseMessageWindow()

    label("loc_1012")

    TalkEnd(0xFE)
    Jump("loc_1035")

    label("loc_101A")

    Call(0, 29)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CB, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1035")
    Call(0, 31)

    label("loc_1035")

    Return()

    # Function_10_F49 end

    def Function_11_1036(): pass

    label("Function_11_1036")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 6)), scpexpr(EXPR_END)), "loc_10F0")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_10A1")

    #C0016
    ChrTalk(
        0xFE,
        (
            "总之，\x01",
            "我有朝一日一定\x01",
            "还会来克洛斯贝尔的。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0xFE,
        "……在那之前，就暂别了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_10E8")

    label("loc_10A1")


    #N0018
    NpcTalk(
        0xFE,
        "男孩",
        "怎么，还有事吗？\x02",
    )

    CloseMessageWindow()

    #N0019
    NpcTalk(
        0xFE,
        "男孩",
        (
            "哼，我很忙的，\x01",
            "不要随便和我说话。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10E8")

    TalkEnd(0xFE)
    Jump("loc_110B")

    label("loc_10F0")

    Call(0, 29)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CB, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_110B")
    Call(0, 31)

    label("loc_110B")

    Return()

    # Function_11_1036 end

    def Function_12_110C(): pass

    label("Function_12_110C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 7)), scpexpr(EXPR_END)), "loc_116C")

    #C0020
    ChrTalk(
        0xFE,
        (
            "（嘀嘀咕咕）……\x01",
            "距离发车还有几分钟？\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0xFE,
        "啊啊，真是让人依依不舍啊……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_1187")

    label("loc_116C")

    Call(0, 28)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CB, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1187")
    Call(0, 31)

    label("loc_1187")

    TalkEnd(0xFE)
    Return()

    # Function_12_110C end

    def Function_13_118B(): pass

    label("Function_13_118B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CB, 0)), scpexpr(EXPR_END)), "loc_11C5")

    #C0022
    ChrTalk(
        0xFE,
        (
            "干什么？已经没事了吧？\x01",
            "那就快走吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11E0")

    label("loc_11C5")

    Call(0, 27)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CB, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_11E0")
    Call(0, 31)

    label("loc_11E0")

    TalkEnd(0xFE)
    Return()

    # Function_13_118B end

    def Function_14_11E4(): pass

    label("Function_14_11E4")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch02902.itc", 0x1F)
    LoadChrToIndex("chr/ch24202.itc", 0x20)
    LoadChrToIndex("chr/ch24402.itc", 0x21)
    LoadChrToIndex("chr/ch24502.itc", 0x22)
    LoadChrToIndex("chr/ch27602.itc", 0x23)
    LoadChrToIndex("chr/ch33102.itc", 0x24)
    LoadChrToIndex("chr/ch33202.itc", 0x25)
    LoadChrToIndex("chr/ch32302.itc", 0x26)
    LoadChrToIndex("chr/ch22302.itc", 0x27)
    LoadChrToIndex("chr/ch21802.itc", 0x28)
    SoundLoad(450)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis008.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu10100.itp")
    SetChrFlags(0x101, 0x4)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrPos(0x101, -2000, 150, -750, 0)
    SetChrFlags(0x109, 0x4)
    SetChrChipByIndex(0x109, 0x1F)
    SetChrSubChip(0x109, 0x0)
    SetChrPos(0x109, -2000, 150, 750, 180)
    SetChrChipByIndex(0x15, 0x20)
    SetChrSubChip(0x15, 0x0)
    ClearChrFlags(0x15, 0x80)
    SetChrFlags(0x15, 0x8000)
    SetChrPos(0x15, -2600, 150, 3300, 180)
    SetChrChipByIndex(0x16, 0x21)
    SetChrSubChip(0x16, 0x1)
    ClearChrFlags(0x16, 0x80)
    SetChrFlags(0x16, 0x8000)
    SetChrPos(0x16, -1600, 150, -3300, 0)
    SetChrChipByIndex(0x17, 0x22)
    SetChrSubChip(0x17, 0x2)
    ClearChrFlags(0x17, 0x80)
    SetChrFlags(0x17, 0x8000)
    SetChrPos(0x17, -2600, 150, -3300, 0)
    SetChrChipByIndex(0x18, 0x23)
    SetChrSubChip(0x18, 0x0)
    ClearChrFlags(0x18, 0x80)
    SetChrFlags(0x18, 0x8000)
    SetChrPos(0x18, 2600, 150, 750, 180)
    SetChrChipByIndex(0x19, 0x24)
    SetChrSubChip(0x19, 0x0)
    ClearChrFlags(0x19, 0x80)
    SetChrFlags(0x19, 0x8000)
    SetChrPos(0x19, 1800, 150, 1800, 0)
    SetChrChipByIndex(0x1A, 0x25)
    SetChrSubChip(0x1A, 0x0)
    ClearChrFlags(0x1A, 0x80)
    SetChrFlags(0x1A, 0x8000)
    SetChrPos(0x1A, 1800, 150, 3300, 180)
    SetChrChipByIndex(0x1B, 0x26)
    SetChrSubChip(0x1B, 0x0)
    ClearChrFlags(0x1B, 0x80)
    SetChrFlags(0x1B, 0x8000)
    SetChrPos(0x1B, -1600, 150, 4350, 0)
    SetChrChipByIndex(0x1C, 0x27)
    SetChrSubChip(0x1C, 0x2)
    ClearChrFlags(0x1C, 0x80)
    SetChrFlags(0x1C, 0x8000)
    SetChrPos(0x1C, 2600, 150, -4350, 180)
    SetChrChipByIndex(0x1D, 0x28)
    SetChrSubChip(0x1D, 0x0)
    ClearChrFlags(0x1D, 0x80)
    SetChrFlags(0x1D, 0x8000)
    SetChrPos(0x1D, 1600, 150, -4350, 180)
    SetMapObjFlags(0x4, 0x4)
    OP_74(0x5, 0x2D)
    OP_71(0x5, 0x0, 0xF0, 0x0, 0x20)
    BeginChrThread(0x101, 3, 0, 15)
    OP_68(0, 900, -1000, 0)
    MoveCamera(312, 17, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(19000, 0)
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    Sound(450, 2, 100, 0)
    SetCameraDistance(16500, 5000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)
    Fade(500)
    OP_68(-2300, 900, 350, 0)
    MoveCamera(300, 17, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(20000, 0)
    OP_0D()
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    SetChrName("诺艾尔上士")

    #A0023
    AnonymousTalk(
        0xFF,
        (
            "呼……总算顺利完成了任务，\x01",
            "真是太好了。\x02\x03",

            "老实说，我一直害怕\x01",
            "自己会拖大家的后腿呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)

    #C0024
    ChrTalk(
        0x101,
        (
            "#6P#00002F哈哈，真是不必要的担心。\x02\x03",

            "#00004F索妮亚司令正是因为\x01",
            "信任上士你的能力，\x01",
            "才会推荐你过来。\x02\x03",

            "#00000F总之，今后就请\x01",
            "多多指教吧。\x02",
        )
    )

    CloseMessageWindow()

    #N0025
    NpcTalk(
        0x109,
        "诺艾尔上士",
        (
            "#10109F#11P是，请多指教！\x02\x03",

            "#10105F……啊，不过……罗伊德警官，\x01",
            "有件事情想和你商量一下。\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x101,
        "#6P#00005F嗯？\x02",
    )

    CloseMessageWindow()

    #N0027
    NpcTalk(
        0x109,
        "诺艾尔上士",
        (
            "#10106F#11P今后的这段时间，\x01",
            "我就要正式接受各位的照顾了……\x02\x03",

            "#10102F而且我也没有穿着军服，\x01",
            "所以称呼『上士』这个军衔就有点……\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x101,
        (
            "#6P#00011F啊，说的也是啊。\x02\x03",

            "#00000F那应该怎么称呼呢？\x01",
            "直呼名字可以吗？\x02",
        )
    )

    CloseMessageWindow()

    #N0029
    NpcTalk(
        0x109,
        "诺艾尔上士",
        "#10109F#11P嗯，当然。\x02",
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x101,
        (
            "#6P#00009F那好，诺艾尔，\x01",
            "今后就请多指教了。\x02\x03",

            "#00002F对了，不介意的话，\x01",
            "你以后也随意些吧。\x02\x03",

            "我们年纪相当，又是同事，\x01",
            "没必要太过客气。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x109, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0031
    ChrTalk(
        0x109,
        (
            "#10111F#11P哎哎！？\x01",
            "要我对罗伊德警官随意吗！？\x02\x03",

            "#10106F………………………………\x01",
            "不行不行，那可不行！\x02\x03",

            "#10101F我在警察局还是个新人，\x01",
            "而且只是见习身份而已！\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x101,
        (
            "#6P#00011F不不，没必要\x01",
            "这么拘泥啦……\x02\x03",

            "#00000F艾莉、兰迪他们彼此之间说话都很随便的，\x01",
            "并不在意年龄大小。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x109,
        (
            "#10106F#11P可是，那个……\x01",
            "这还是和天性有关吧……\x02\x03",

            "一旦养成习惯，\x01",
            "好像就很难再改变了……\x02\x03",

            "#10101F不过，既然罗伊德警官都这么说了，\x01",
            "我一定会努力改掉说敬语的习惯！\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x101,
        (
            "#6P#00012F这、这个，\x01",
            "也不用太勉强哦。\x02\x03",

            "#00002F哈哈……\x01",
            "你骨子里就很严谨守矩呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x109,
        (
            "#10109F#11P哈哈……\x01",
            "这说不定是受了父亲的影响吧。\x02\x03",

            "#10100F父亲是个很严厉的人，我和芙兰\x01",
            "从小就接受他的严格教育。\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x101,
        "#6P#00002F原来是受父亲影响啊。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0037
    ChrTalk(
        0x101,
        (
            "#6P#00005F哎，说起来，虽然见过你们\x01",
            "的母亲几次，不过……？\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x109,
        (
            "#10104F#11P父亲……\x01",
            "在十年前左右离世了。\x02\x03",

            "#10100F他是克洛斯贝尔警备队的一员，\x01",
            "在某次任务中……亡于事故。\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x101,
        (
            "#6P#00006F……是吗，\x01",
            "抱歉，问到你的伤心事了。\x02\x03",

            "#00001F莫非……\x01",
            "你决定加入警备队也是因为……？\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x109,
        (
            "#10105F#11P该怎么说呢……\x01",
            "也没有特别明确的想法。\x02\x03",

            "#10104F不过，也许正如你所说，\x01",
            "我大概和父亲一样，\x01",
            "也想守护克洛斯贝尔这片土地。\x02\x03",

            "#10100F从这种意义上说，虽然所在职场不同，\x01",
            "但芙兰说不定也和我一样呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x101,
        "#6P#00002F是吗……\x02",
    )

    CloseMessageWindow()
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(1000)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(300)

    #C0042
    ChrTalk(
        0x101,
        "#6P#00008F………………………………………\x02",
    )

    CloseMessageWindow()
    OP_63(0x109, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0043
    ChrTalk(
        0x109,
        "#10105F#11P罗伊德警官？\x02",
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x101,
        (
            "#6P#00004F抱歉，没什么。\x02\x03",

            "#00002F话说回来，你能加入，\x01",
            "真是帮了我们大忙呢。\x02\x03",

            "现在的人手明显不足。\x01",
            "而且，老实说……真是预测不到\x01",
            "今后将会发生什么呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x109,
        (
            "#10112F#11P啊哈哈，得到如此期待，\x01",
            "真是荣幸……\x02\x03",

            "#10102F不过，黑手党覆灭之后，\x01",
            "市内的治安应该得到了改善吧？\x02\x03",

            "虽然『黑月』还在，\x01",
            "但他们似乎并没有太过显眼的行为。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x101,
        (
            "#6P#00006F……这只是表面现象而已。\x02\x03",

            "#00008F从某种角度来看，\x01",
            "『鲁巴彻』这个组织\x01",
            "其实也发挥了一定的作用。\x02\x03",

            "#00001F其作用就是维护克洛斯贝尔的治安。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopSound(450, 1000, 100)
    Sleep(1000)
    OP_CC(0x1, 0xFF, 0x0)
    SetScenarioFlags(0x22, 1)
    NewScene("r0040", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_14_11E4 end

    def Function_15_1F61(): pass

    label("Function_15_1F61")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1F99")
    OP_82(0xA, 0xA, 0x5DC, 0x2EE)
    Sleep(3500)
    OP_82(0xA, 0xA, 0x4B0, 0x1F4)
    Sleep(3500)
    Jump("Function_15_1F61")

    label("loc_1F99")

    Return()

    # Function_15_1F61 end

    def Function_16_1F9A(): pass

    label("Function_16_1F9A")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_20A3")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "◆在前作中取得了成就：与艾莉的羁绊\x01",      # 0
            "◆在前作中取得了成就：与缇欧的羁绊\x01",      # 1
            "◆在前作中取得了成就：与兰迪的羁绊\x01",      # 2
            "◆在前作中取得了全员的羁绊成就\x01",          # 3
            "◆不变更\x01",                                # 4
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2078"),
        (1, "loc_2080"),
        (2, "loc_2088"),
        (3, "loc_2090"),
        (4, "loc_209E"),
        (SWITCH_DEFAULT, "loc_209E"),
    )


    label("loc_2078")

    SetScenarioFlags(0x25, 3)
    Jump("loc_20A3")

    label("loc_2080")

    SetScenarioFlags(0x25, 4)
    Jump("loc_20A3")

    label("loc_2088")

    SetScenarioFlags(0x25, 5)
    Jump("loc_20A3")

    label("loc_2090")

    SetScenarioFlags(0x25, 3)
    SetScenarioFlags(0x25, 4)
    SetScenarioFlags(0x25, 5)
    Jump("loc_20A3")

    label("loc_209E")

    Jump("loc_20A3")

    label("loc_20A3")

    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch02902.itc", 0x1F)
    LoadChrToIndex("chr/ch24202.itc", 0x20)
    LoadChrToIndex("chr/ch24402.itc", 0x21)
    LoadChrToIndex("chr/ch24502.itc", 0x22)
    LoadChrToIndex("chr/ch27602.itc", 0x23)
    LoadChrToIndex("chr/ch33102.itc", 0x24)
    LoadChrToIndex("chr/ch33202.itc", 0x25)
    LoadChrToIndex("chr/ch32302.itc", 0x26)
    LoadChrToIndex("chr/ch22302.itc", 0x27)
    LoadChrToIndex("chr/ch21802.itc", 0x28)
    LoadChrToIndex("apl/ch51029.itc", 0x29)
    SoundLoad(450)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis229.itp")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x121, 2)
    ClearScenarioFlags(0x121, 3)
    ClearScenarioFlags(0x121, 4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 3)), scpexpr(EXPR_END)), "loc_2170")
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis224.itp")
    RunExpression(0x3, (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2170")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 4)), scpexpr(EXPR_END)), "loc_21B3")
    CreatePortrait(2, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis225.itp")
    RunExpression(0x3, (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_21B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 5)), scpexpr(EXPR_END)), "loc_21F6")
    CreatePortrait(3, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis226.itp")
    RunExpression(0x3, (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_21F6")

    SetChrFlags(0x101, 0x4)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrPos(0x101, -2000, 150, -750, 0)
    SetChrFlags(0x109, 0x4)
    SetChrChipByIndex(0x109, 0x1F)
    SetChrSubChip(0x109, 0x0)
    SetChrPos(0x109, -2000, 150, 750, 180)
    SetChrChipByIndex(0x15, 0x20)
    SetChrSubChip(0x15, 0x0)
    ClearChrFlags(0x15, 0x80)
    SetChrFlags(0x15, 0x8000)
    SetChrPos(0x15, -2600, 150, 3300, 180)
    SetChrChipByIndex(0x16, 0x21)
    SetChrSubChip(0x16, 0x1)
    ClearChrFlags(0x16, 0x80)
    SetChrFlags(0x16, 0x8000)
    SetChrPos(0x16, -1600, 150, -3300, 0)
    SetChrChipByIndex(0x17, 0x22)
    SetChrSubChip(0x17, 0x2)
    ClearChrFlags(0x17, 0x80)
    SetChrFlags(0x17, 0x8000)
    SetChrPos(0x17, -2600, 150, -3300, 0)
    SetChrChipByIndex(0x18, 0x23)
    SetChrSubChip(0x18, 0x0)
    ClearChrFlags(0x18, 0x80)
    SetChrFlags(0x18, 0x8000)
    SetChrPos(0x18, 2600, 150, 750, 180)
    SetChrChipByIndex(0x19, 0x24)
    SetChrSubChip(0x19, 0x0)
    ClearChrFlags(0x19, 0x80)
    SetChrFlags(0x19, 0x8000)
    SetChrPos(0x19, 1800, 150, 1800, 0)
    SetChrChipByIndex(0x1A, 0x25)
    SetChrSubChip(0x1A, 0x0)
    ClearChrFlags(0x1A, 0x80)
    SetChrFlags(0x1A, 0x8000)
    SetChrPos(0x1A, 1800, 150, 3300, 180)
    SetChrChipByIndex(0x1B, 0x26)
    SetChrSubChip(0x1B, 0x0)
    ClearChrFlags(0x1B, 0x80)
    SetChrFlags(0x1B, 0x8000)
    SetChrPos(0x1B, -1600, 150, 4350, 0)
    SetChrChipByIndex(0x1C, 0x27)
    SetChrSubChip(0x1C, 0x2)
    ClearChrFlags(0x1C, 0x80)
    SetChrFlags(0x1C, 0x8000)
    SetChrPos(0x1C, 2600, 150, -4350, 180)
    SetChrChipByIndex(0x1D, 0x28)
    SetChrSubChip(0x1D, 0x0)
    ClearChrFlags(0x1D, 0x80)
    SetChrFlags(0x1D, 0x8000)
    SetChrPos(0x1D, 1600, 150, -4350, 180)
    SetMapObjFlags(0x4, 0x4)
    OP_74(0x5, 0x2D)
    OP_71(0x5, 0x0, 0xF0, 0x0, 0x20)
    BeginChrThread(0x101, 3, 0, 15)
    OP_68(-3500, 500, 0, 0)
    MoveCamera(270, 19, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(15500, 0)
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    Sound(450, 2, 100, 0)
    FadeToBright(1000, 0)
    OP_0D()

    #C0047
    ChrTalk(
        0x109,
        (
            "#10105F黑手党维护\x01",
            "克洛斯贝尔的治安……？\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x101,
        (
            "#00006F嗯，单从结果来看，正是如此。\x02\x03",

            "#00001F……想想克洛斯贝尔\x01",
            "的特殊状况吧。\x02\x03",

            "虽说拥有自治权，\x01",
            "但并非独立国家，\x01",
            "要时常受到两大国的干涉。\x02\x03",

            "取缔犯罪行为的法律充满漏洞，\x01",
            "入境限制也几乎为零……\x02\x03",

            "#00003F在这种情况下，\x01",
            "黑月或其它犯罪组织，以及恐怖分子\x01",
            "本应在这里四处横行才对。\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x109,
        (
            "#10101F啊……\x02\x03",

            "……也就是说，至今为止，\x01",
            "一直是鲁巴彻在抑制他们？\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x101,
        (
            "#00008F我虽然不愿意承认……\x01",
            "但无法否认，单从结果来看，\x01",
            "他们在一定程度上稳定了地下社会的秩序。\x02\x03",

            "#00006F……在毫无征兆的情况下，\x01",
            "鲁巴彻便被卷入到了『教团』所引发的灾难中，\x01",
            "从此消失灭亡……\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x109,
        "#10108F这就导致各势力之间的平衡被打破了吗……\x02",
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x101,
        (
            "#00003F嗯……\x01",
            "帝国派和共和国派议员\x01",
            "的失势也是一样。\x02\x03",

            "由于失去了代言人，\x01",
            "反而有可能会使两大国\x01",
            "比以往更加露骨地施加压力。\x02\x03",

            "#00013F我想，正是因为如此，\x01",
            "新市长才会期待我们支援科的表现。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x109,
        (
            "#10104F原来如此……\x01",
            "我总算明白了。\x02\x03",

            "#10100F艾莉小姐、兰迪前辈，\x01",
            "还有缇欧暂时离队，\x01",
            "也是由于这个原因吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x101,
        (
            "#00004F嗯，为了应对今后的新局面，\x01",
            "要尽可能与各界合作，\x01",
            "从而保证更进一步的活动能力。\x02\x03",

            "我也在一科研修了一段时间，\x01",
            "学到了不少东西……\x02\x03",

            "#00002F另外，由于人手不足，\x01",
            "所以邀请了新成员作为战力。\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x109,
        (
            "#10109F呵呵……\x01",
            "能被大家邀请，真是倍感光荣。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(-2300, 900, -150, 0)
    MoveCamera(240, 17, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(20000, 0)
    OP_0D()

    #C0056
    ChrTalk(
        0x109,
        "#12P#10105F不过，说起来……\x02",
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x101,
        "#00000F#5P嗯，怎么了？\x02",
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x109,
        (
            "#12P#10100F另一名新成员，\x01",
            "就是之前曾经见到过的『那个人』吧？\x02\x03",

            "老实说，我真是有点意外，\x01",
            "这中间究竟发生过什么呢？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0059
    ChrTalk(
        0x101,
        (
            "#00011F#5P哦，你是说『他』啊。\x02\x03",

            "#00006F就在我们刚开始\x01",
            "寻找人手的时候，\x01",
            "他就前来拜访了。\x02\x03",

            "他有新市长的\x01",
            "推荐信，\x01",
            "我们也没办法拒绝。\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x109,
        "#12P#10111F市、市长的推荐信吗？\x02",
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x101,
        (
            "#00001F#5P嗯，他向市长索要的，\x01",
            "作为在ＩＢＣ大楼的那次危机中\x01",
            "出手帮忙的谢礼。\x02\x03",

            "#00006F……也不知道他是从哪里\x01",
            "听说特别任务支援科\x01",
            "在征召新成员的。\x02\x03",

            "据他本人说，想加入的原因\x01",
            "就是『好像会很有趣』……\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x109,
        (
            "#12P#10108F那个……\x01",
            "真的没问题吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x101,
        (
            "#00012F#5P应、应该没问题吧……\x01",
            "毕竟不是什么坏人。\x02\x03",

            "#00002F虽然他的经历不详，\x01",
            "对地下社会有很深的了解，\x01",
            "又身兼男公关一职……\x02\x03",

            "#00006F……说着说着，\x01",
            "好像连我都有些不安了。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x109, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(400)
    Sound(2496, 255, 100, 0)    #voice#Noel
    Sleep(800)

    #C0064
    ChrTalk(
        0x109,
        (
            "#12P#10112F不、不用担心。\x02\x03",

            "#10102F虽然他说话刻薄，爱挖苦人，\x01",
            "但应该不是个坏孩子……\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x101,
        (
            "#00012F#5P哈哈……\x01",
            "你能这么说，我也放心了。\x02\x03",

            "#00002F老实说，我一直都\x01",
            "怕你和他合不来呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x109,
        (
            "#12P#10106F唔、唔……\x01",
            "虽然我确实被他\x01",
            "戏弄过……\x02\x03",

            "#10100F不过，\x01",
            "他好像还是更喜欢\x01",
            "欺负罗伊德警官呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x101,
        (
            "#00006F#5P呜……\x01",
            "饶了我吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x109,
        (
            "#12P#10112F哈哈哈……\x01",
            "（其实芙兰倒是觉得很有趣呢，\x01",
            "  不过，还是不说为好吧？）\x02",
        )
    )

    CloseMessageWindow()
    Sound(800, 0, 100, 0)
    Sleep(500)
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("乘务员的声音")

    #A0069
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "各位乘客请注意。\x02",
        )
    )

    CloseMessageWindow()

    #A0070
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "列车即将到达克洛斯贝尔自治州\x01",
            "的克洛斯贝尔市。\x02",
        )
    )

    CloseMessageWindow()

    #A0071
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "需要乘坐定期飞船\x01",
            "前往利贝尔、雷米菲利亚等地的\x01",
            "乘客请准备下车换乘。\x02",
        )
    )

    CloseMessageWindow()

    #A0072
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "另外，遵照大陆铁道公司规章，\x01",
            "本列车将会在克洛斯贝尔站\x01",
            "停车大约３０分钟。\x02",
        )
    )

    CloseMessageWindow()

    #A0073
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "准备前往埃雷波尼亚的乘客，\x01",
            "请填写入境申请书，\x01",
            "提交给安检官。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sleep(150)

    #C0074
    ChrTalk(
        0x101,
        (
            "#00002F#5P哈哈，只坐一站而已，\x01",
            "真是转眼之间就到了。\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0x109,
        (
            "#12P#10104F嗯……\x02\x03",

            "#10102F话说回来，离开克洛斯贝尔数日，\x01",
            "还真是很怀念呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x101,
        "#00002F#5P是啊……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetCameraDistance(19500, 1500)
    Fade(250)
    SetChrChipByIndex(0x101, 0x29)
    SetChrSubChip(0x101, 0x0)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x2)
    SetChrFlags(0x101, 0x10)
    OP_0D()
    Sleep(1000)
    Sound(802, 0, 100, 0)
    SetChrSubChip(0x101, 0x1)
    Sleep(500)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(1000)
    SetMessageWindowPos(80, 200, -1, -1)

    #A0077
    AnonymousTalk(
        0x101,
        (
            "#00004F#5P（……距离全员团聚，\x01",
            "  可能还需要一段时间……）\x02\x03",

            "#00002F（希望琪雅不要\x01",
            "  感到太寂寞。）\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(300)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_31AA")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    #A0078
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1K教团事件的那一晚，在ＩＢＣ大楼的十六层和谁谈话了？\x07\x00\x02",
        )
    )

    MenuCmd(0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 3)), scpexpr(EXPR_END)), "loc_30F2")
    MenuCmd(1, 0, "【艾莉】")

    label("loc_30F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 4)), scpexpr(EXPR_END)), "loc_3107")
    MenuCmd(1, 0, "【缇欧】")

    label("loc_3107")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 5)), scpexpr(EXPR_END)), "loc_311C")
    MenuCmd(1, 0, "【兰迪】")

    label("loc_311C")

    MenuCmd(2, 0, -1, 100, 0)
    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_315A"),
        (1, "loc_3173"),
        (2, "loc_319D"),
        (SWITCH_DEFAULT, "loc_31A5"),
    )


    label("loc_315A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 3)), scpexpr(EXPR_END)), "loc_316B")
    SetScenarioFlags(0x121, 2)
    Jump("loc_316E")

    label("loc_316B")

    SetScenarioFlags(0x121, 3)

    label("loc_316E")

    Jump("loc_31A5")

    label("loc_3173")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 3)), scpexpr(EXPR_END)), "loc_3195")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 4)), scpexpr(EXPR_END)), "loc_318D")
    SetScenarioFlags(0x121, 3)
    Jump("loc_3190")

    label("loc_318D")

    SetScenarioFlags(0x121, 4)

    label("loc_3190")

    Jump("loc_3198")

    label("loc_3195")

    SetScenarioFlags(0x121, 4)

    label("loc_3198")

    Jump("loc_31A5")

    label("loc_319D")

    SetScenarioFlags(0x121, 4)
    Jump("loc_31A5")

    label("loc_31A5")

    Jump("loc_31D8")

    label("loc_31AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 3)), scpexpr(EXPR_END)), "loc_31BB")
    SetScenarioFlags(0x121, 2)
    Jump("loc_31D8")

    label("loc_31BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 4)), scpexpr(EXPR_END)), "loc_31CC")
    SetScenarioFlags(0x121, 3)
    Jump("loc_31D8")

    label("loc_31CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 5)), scpexpr(EXPR_END)), "loc_31D8")
    SetScenarioFlags(0x121, 4)

    label("loc_31D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x121, 2)), scpexpr(EXPR_END)), "loc_35FC")
    Sleep(300)

    #C0079
    ChrTalk(
        0x101,
        "#00004F#5P（而且……）\x02",
    )

    CloseMessageWindow()
    VolumeBGM(0x46, 0x3E8)
    OP_25(0x1C2, 0x3C)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    Sleep(300)
    OP_4B(0x101, 0x3)
    SetChrSubChip(0x101, 0x1)
    OP_68(-2700, 900, 2040, 0)

    #N0080
    NpcTalk(
        0x15,
        "艾莉",
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#00112F#N#11P……那、那个……\x01",
            "我先回去找贝尔啦。\x02\x03",

            "#00113F或许还能帮\x01",
            "迪塔叔叔他们做些\x01",
            "什么事呢……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(80, 160, -1, -1)

    #A0081
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#00004F啊，好的……\x01",
            "我也趁现在去进行补给，\x01",
            "顺便检查一下装备吧。\x02\x03",

            "#00002F……一会见。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #N0082
    NpcTalk(
        0x15,
        "艾莉",
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#00102F#N#11P嗯……\x02\x03",

            "#00113F……那个……刚才做到一半的事，\x01",
            "等到把全部事情都解决之后再……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(80, 160, -1, -1)

    #A0083
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#00005F哎？\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #N0084
    NpcTalk(
        0x15,
        "艾莉",
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#00112F#N#11P没、没什么啦。\x02\x03",

            "#00109F那、那么，一会见哦！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_68(-2300, 900, -150, 0)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_4C(0x101, 0x3)
    VolumeBGM(0x64, 0x3E8)
    OP_25(0x1C2, 0x64)
    Sleep(300)

    #C0085
    ChrTalk(
        0x101,
        (
            "#00004F#5P（……自那之后，我们都很忙，\x01",
            "  一直都没有取得实质性进展……）\x02\x03",

            "（等艾莉回来以后，\x01",
            "  无论如何也要把当时没做完的事情……）\x02\x03",

            "#00011F（不对不对！哪有什么没做完的事情！\x01",
            "  不能再胡思乱想了……）\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x109,
        "#12P#10100F……罗伊德警官？\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_63(0x101, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    ClearChrFlags(0x101, 0x20)
    ClearChrFlags(0x101, 0x2)
    ClearChrFlags(0x101, 0x10)

    #C0087
    ChrTalk(
        0x101,
        (
            "#00011F#5P啊啊，没什么！\x02\x03",

            "#00012F话说回来，还真是有些累啊！\x01",
            "真想赶快回支援科，坐在沙发上休息一下！\x02",
        )
    )

    CloseMessageWindow()
    OP_64(0x101)

    #C0088
    ChrTalk(
        0x109,
        "#12P#10105F（罗伊德警官的反应好奇怪……）\x02",
    )

    CloseMessageWindow()
    Jump("loc_3F1D")

    label("loc_35FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x121, 3)), scpexpr(EXPR_END)), "loc_3A34")
    Sleep(300)

    #C0089
    ChrTalk(
        0x101,
        "#00004F#5P（而且……）\x02",
    )

    CloseMessageWindow()
    VolumeBGM(0x46, 0x3E8)
    OP_25(0x1C2, 0x3C)
    OP_CB(0x2, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    Sleep(300)
    OP_4B(0x101, 0x3)
    SetChrSubChip(0x101, 0x1)
    OP_68(-2700, 900, 2040, 0)

    #N0090
    NpcTalk(
        0x15,
        "缇欧",
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#00204F#N#11P……米修拉姆的主题公园。\x02\x03",

            "如果能顺利解决此次骚乱，\x01",
            "请带我去那里玩吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(80, 160, -1, -1)

    #A0091
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#00011F哎……\x01",
            "那样就行了吗！？\x02\x03",

            "#00001F不，可是……\x01",
            "还是做个更加正式些\x01",
            "的约定比较好吧？\x02\x03",

            "比如说，当缇欧遇到困难时，\x01",
            "无论如何我都要马上赶去帮忙之类的。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #N0092
    NpcTalk(
        0x15,
        "缇欧",
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#00204F#N#11P不，这样就够了。\x02\x03",

            "#00208F而且，如果不解决此次事件，\x01",
            "这个约定也等同于无法履行……\x02\x03",

            "#00202F从这层意义上来说，\x01",
            "也已经算是个非常正式的约定了吧。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_68(-2300, 900, -150, 0)
    OP_CB(0x2, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    OP_4C(0x101, 0x3)
    VolumeBGM(0x64, 0x3E8)
    OP_25(0x1C2, 0x64)
    Sleep(300)

    #C0093
    ChrTalk(
        0x101,
        (
            "#00004F#5P（……自那之后，我们都很忙，\x01",
            "  直到现在也没能去玩……）\x02\x03",

            "（等缇欧回来以后，\x01",
            "  一定要履行那时的约定。）\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x109,
        "#12P#10105F……罗伊德警官？\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Fade(250)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    ClearChrFlags(0x101, 0x20)
    ClearChrFlags(0x101, 0x2)
    ClearChrFlags(0x101, 0x10)
    OP_0D()

    #C0095
    ChrTalk(
        0x101,
        (
            "#00005F#5P啊啊，抱歉。\x02\x03",

            "#00000F……对了，诺艾尔，\x01",
            "你去过主题公园吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0x109,
        (
            "#12P#10102F米修拉姆的主题公园吗？\x01",
            "嗯，以前和芙兰去过一次。\x02\x03",

            "#10109F公园里的表演非常有意思，\x01",
            "咪西也很可爱呢～！\x02",
        )
    )

    CloseMessageWindow()
    Sound(822, 0, 100, 0)
    OP_63(0x109, 0x12C, 1300, 0x36, 0x39, 0xFA, 0x0)
    Sleep(1000)

    #C0097
    ChrTalk(
        0x101,
        (
            "#00012F#5P是、是吗……\x01",
            "（咪西真受欢迎啊。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3F1D")

    label("loc_3A34")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x121, 4)), scpexpr(EXPR_END)), "loc_3F1D")
    Sleep(300)

    #C0098
    ChrTalk(
        0x101,
        "#00004F#5P（而且……）\x02",
    )

    CloseMessageWindow()
    VolumeBGM(0x46, 0x3E8)
    OP_25(0x1C2, 0x3C)
    OP_CB(0x3, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x3, 0x3)
    Sleep(300)
    OP_4B(0x101, 0x3)
    SetChrSubChip(0x101, 0x1)
    OP_68(-2700, 900, 2040, 0)

    #N0099
    NpcTalk(
        0x15,
        "兰迪",
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#00303F#N#11P警备队要是真的攻过来，\x01",
            "战到最后的应该是我们吧。\x02\x03",

            "#00300F我可不想让大小姐和阿缇\x01",
            "做出太过逞强的事啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0100
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#00004F……嗯，我明白的。\x02\x03",

            "#00000F无论如何，我和兰迪也要阻止他们，\x01",
            "绝对不能让他们迈进这里半步。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(200, 50, -1, -1)
    SetChrName("兰迪")

    #N0101
    NpcTalk(
        0x15,
        "兰迪",
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#00302F#N#11P就是这样。\x02\x03",

            "#00309F我的背后就托付给你啦，搭档。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0102
    AnonymousTalk(
        0x101,
        (
            scpstr(0xD),
            "#00005F啊……\x02\x03",

            "#00002F明白了！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_68(-2300, 900, -150, 0)
    OP_CB(0x3, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x3, 0x3)
    OP_4C(0x101, 0x3)
    VolumeBGM(0x64, 0x3E8)
    OP_25(0x1C2, 0x64)
    Sleep(300)

    #C0103
    ChrTalk(
        0x101,
        (
            "#00008F#5P（搭档吗……）\x02\x03",

            "#00003F（老实说，身为男人，\x01",
            "  我还没有和兰迪并肩而立的能力。）\x02\x03",

            "#00000F（为了能成为真正合格的搭档，\x01",
            "  我必须要更加努力……）\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0x109,
        "#12P#10105F……罗伊德警官？\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Fade(250)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    ClearChrFlags(0x101, 0x20)
    ClearChrFlags(0x101, 0x2)
    ClearChrFlags(0x101, 0x10)
    OP_0D()

    #C0105
    ChrTalk(
        0x101,
        (
            "#00005F#5P啊，抱歉。\x02\x03",

            "#00000F对了，在你眼里，\x01",
            "兰迪是个什么样的人？\x02\x03",

            "并不是担任警察工作的兰迪，\x01",
            "主要还是指警备队时代的他……\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0x109,
        (
            "#12P#10105F兰迪前辈吗？\x02\x03",

            "#10104F这个嘛……\x01",
            "第一感觉就是超乎寻常的强吧。\x02\x03",

            "#10100F个人战斗能力自然不用说，\x01",
            "听说他带队作战的战术\x01",
            "也相当厉害……\x02\x03",

            "现在应该也在复健训练中\x01",
            "大展身手吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0x101,
        (
            "#00002F#5P是吗……\x02\x03",

            "#00008F（……说起来，\x01",
            "  兰迪说过，在这次的训练中\x01",
            "  将会使用来复枪……）\x02\x03",

            "（猎兵时代的往事……\x01",
            "  是不是已经抛开一些了呢……？）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3F1D")

    OP_68(-2300, 1400, -150, 2000)
    FadeToDark(2000, 0, -1)
    Sleep(1000)
    StopSound(450, 1000, 100)
    OP_0D()
    OP_6F(0x79)
    OP_C9(0x0, 0x10)
    FadeToBright(0, 0)
    OP_0D()
    PlayMovie(0x0, "ed72_01.pmf", 0x235, 0x1)
    Sleep(1000)
    OP_57(0x2)
    PlayMovie(0x1, "", 0x0, 0x0)
    StopBGM(0xFA0)
    WaitBGM()
    OP_CC(0x1, 0xFF, 0x0)
    OP_C9(0x1, 0x10)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x22, 0)
    NewScene("c0800", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_16_1F9A end

    def Function_17_3F98(): pass

    label("Function_17_3F98")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x101, 0x8)
    SetChrFlags(0x102, 0x8)
    SetChrFlags(0x109, 0x8)
    SetChrFlags(0x105, 0x8)
    SoundLoad(450)
    LoadChrToIndex("chr/ch24202.itc", 0x1E)
    LoadChrToIndex("chr/ch24402.itc", 0x1F)
    LoadChrToIndex("chr/ch24502.itc", 0x20)
    LoadChrToIndex("chr/ch24102.itc", 0x21)
    LoadChrToIndex("chr/ch24002.itc", 0x22)
    LoadChrToIndex("chr/ch27602.itc", 0x23)
    LoadChrToIndex("chr/ch27802.itc", 0x24)
    LoadChrToIndex("chr/ch27702.itc", 0x25)
    LoadChrToIndex("chr/ch27902.itc", 0x26)
    LoadChrToIndex("chr/ch33102.itc", 0x27)
    LoadChrToIndex("chr/ch23502.itc", 0x28)
    LoadChrToIndex("chr/ch33202.itc", 0x29)
    LoadChrToIndex("chr/ch33002.itc", 0x2A)
    LoadChrToIndex("chr/ch20402.itc", 0x2B)
    LoadChrToIndex("chr/ch20502.itc", 0x2C)
    LoadChrToIndex("chr/ch21302.itc", 0x2D)
    LoadChrToIndex("chr/ch32402.itc", 0x2E)
    LoadChrToIndex("chr/ch32302.itc", 0x2F)
    LoadChrToIndex("chr/ch32202.itc", 0x30)
    LoadChrToIndex("chr/ch22302.itc", 0x31)
    LoadChrToIndex("chr/ch21802.itc", 0x32)
    LoadChrToIndex("chr/ch22002.itc", 0x33)
    LoadChrToIndex("chr/ch22102.itc", 0x34)
    LoadChrToIndex("chr/ch21902.itc", 0x35)
    LoadChrToIndex("chr/ch42802.itc", 0x3C)
    LoadChrToIndex("chr/ch42902.itc", 0x3D)
    LoadChrToIndex("chr/ch43002.itc", 0x3E)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x1E, 0x80)
    SetChrFlags(0x15, 0x8000)
    SetChrFlags(0x16, 0x8000)
    SetChrFlags(0x17, 0x8000)
    SetChrFlags(0x18, 0x8000)
    SetChrFlags(0x19, 0x8000)
    SetChrFlags(0x1A, 0x8000)
    SetChrFlags(0x1B, 0x8000)
    SetChrFlags(0x1C, 0x8000)
    SetChrFlags(0x1D, 0x8000)
    SetChrFlags(0x1E, 0x8000)
    ClearChrFlags(0x21, 0x80)
    ClearChrFlags(0x22, 0x80)
    ClearChrFlags(0x23, 0x80)
    SetChrFlags(0x21, 0x8000)
    SetChrFlags(0x22, 0x8000)
    SetChrFlags(0x23, 0x8000)
    SetMapObjFlags(0x4, 0x4)
    OP_74(0x5, 0x2D)
    OP_71(0x5, 0xF0, 0x0, 0x0, 0x20)
    BeginChrThread(0x101, 3, 0, 15)
    Sound(450, 2, 100, 0)
    OP_68(0, 900, 7000, 0)
    MoveCamera(303, 24, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(14000, 0)
    SetChrPos(0x15, -2600, 150, -4350, 180)
    SetChrPos(0x16, -2600, 150, -750, 0)
    SetChrPos(0x17, -2600, 150, 650, 180)
    SetChrPos(0x18, -2600, 150, 4350, 0)
    SetChrPos(0x19, -1600, 150, -4350, 180)
    SetChrPos(0x1A, -1600, 150, 3150, 180)
    SetChrPos(0x1B, 1800, 150, -1800, 180)
    SetChrPos(0x1C, 1800, 150, 3150, 180)
    SetChrPos(0x1D, 2800, 150, 650, 180)
    SetChrPos(0x1E, 2800, 150, 3150, 180)
    SetChrChipByIndex(0x15, 0x21)
    SetChrSubChip(0x15, 0x0)
    SetChrChipByIndex(0x16, 0x33)
    SetChrSubChip(0x16, 0x0)
    SetChrChipByIndex(0x17, 0x24)
    SetChrSubChip(0x17, 0x0)
    SetChrChipByIndex(0x18, 0x2B)
    SetChrSubChip(0x18, 0x0)
    SetChrChipByIndex(0x19, 0x2D)
    SetChrSubChip(0x19, 0x0)
    SetChrChipByIndex(0x1A, 0x20)
    SetChrSubChip(0x1A, 0x0)
    SetChrChipByIndex(0x1B, 0x23)
    SetChrSubChip(0x1B, 0x0)
    SetChrChipByIndex(0x1C, 0x29)
    SetChrSubChip(0x1C, 0x0)
    SetChrChipByIndex(0x1D, 0x28)
    SetChrSubChip(0x1D, 0x0)
    SetChrChipByIndex(0x1E, 0x25)
    SetChrSubChip(0x1E, 0x0)
    SetChrPos(0x21, -1600, 150, -1800, 180)
    SetChrPos(0x22, 1800, 150, 4350, 0)
    SetChrPos(0x23, 2800, 150, 4350, 0)
    SetChrChipByIndex(0x21, 0x3E)
    SetChrSubChip(0x21, 0x0)
    SetChrChipByIndex(0x22, 0x3E)
    SetChrSubChip(0x22, 0x0)
    SetChrChipByIndex(0x23, 0x3E)
    SetChrSubChip(0x23, 0x0)
    FadeToBright(1000, 0)
    OP_68(0, 900, -5000, 7000)
    OP_0D()
    Sleep(3500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(0, 900, 7000, 0)
    SetChrPos(0x15, -2600, 150, -4350, 180)
    SetChrPos(0x16, -1600, 150, -1800, 180)
    SetChrPos(0x17, -1600, 150, 1800, 0)
    SetChrPos(0x18, -1600, 150, 5650, 180)
    SetChrPos(0x19, 1800, 150, -4350, 180)
    SetChrPos(0x1A, 1800, 150, -1800, 180)
    SetChrPos(0x1B, 2800, 150, -1800, 180)
    SetChrPos(0x1C, 2800, 150, 650, 180)
    SetChrPos(0x1D, 2800, 150, 4350, 0)
    SetChrPos(0x1E, 2800, 150, 5650, 180)
    SetChrChipByIndex(0x15, 0x28)
    SetChrSubChip(0x15, 0x0)
    SetChrChipByIndex(0x16, 0x27)
    SetChrSubChip(0x16, 0x0)
    SetChrChipByIndex(0x17, 0x31)
    SetChrSubChip(0x17, 0x0)
    SetChrChipByIndex(0x18, 0x22)
    SetChrSubChip(0x18, 0x0)
    SetChrChipByIndex(0x19, 0x2F)
    SetChrSubChip(0x19, 0x0)
    SetChrChipByIndex(0x1A, 0x26)
    SetChrSubChip(0x1A, 0x0)
    SetChrChipByIndex(0x1B, 0x2B)
    SetChrSubChip(0x1B, 0x0)
    SetChrChipByIndex(0x1C, 0x34)
    SetChrSubChip(0x1C, 0x0)
    SetChrChipByIndex(0x1D, 0x1E)
    SetChrSubChip(0x1D, 0x0)
    SetChrChipByIndex(0x1E, 0x1F)
    SetChrSubChip(0x1E, 0x0)
    SetChrPos(0x21, -2600, 150, 650, 180)
    SetChrPos(0x22, -1600, 150, -750, 0)
    SetChrPos(0x23, 1800, 150, 3150, 180)
    SetChrChipByIndex(0x21, 0x3E)
    SetChrSubChip(0x21, 0x0)
    SetChrChipByIndex(0x22, 0x3E)
    SetChrSubChip(0x22, 0x0)
    SetChrChipByIndex(0x23, 0x3C)
    SetChrSubChip(0x23, 0x0)
    FadeToBright(1000, 0)
    OP_68(0, 900, -5000, 7000)
    OP_0D()
    Sleep(3500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(0, 900, 7000, 0)
    SetChrPos(0x15, -2600, 150, -3150, 0)
    SetChrPos(0x16, -2600, 150, -1800, 180)
    SetChrPos(0x17, -2600, 150, 4350, 0)
    SetChrPos(0x18, -1600, 150, -4350, 180)
    SetChrPos(0x19, -1600, 150, 650, 180)
    SetChrPos(0x1A, -1600, 150, 4350, 0)
    SetChrPos(0x1B, 1800, 150, -1800, 180)
    SetChrPos(0x1C, 1800, 150, -750, 0)
    SetChrPos(0x1D, 1800, 150, 3150, 180)
    SetChrPos(0x1E, 2800, 150, 1800, 0)
    SetChrChipByIndex(0x15, 0x27)
    SetChrSubChip(0x15, 0x0)
    SetChrChipByIndex(0x16, 0x2B)
    SetChrSubChip(0x16, 0x0)
    SetChrChipByIndex(0x17, 0x2D)
    SetChrSubChip(0x17, 0x0)
    SetChrChipByIndex(0x18, 0x2F)
    SetChrSubChip(0x18, 0x0)
    SetChrChipByIndex(0x19, 0x21)
    SetChrSubChip(0x19, 0x0)
    SetChrChipByIndex(0x1A, 0x35)
    SetChrSubChip(0x1A, 0x0)
    SetChrChipByIndex(0x1B, 0x30)
    SetChrSubChip(0x1B, 0x0)
    SetChrChipByIndex(0x1C, 0x22)
    SetChrSubChip(0x1C, 0x0)
    SetChrChipByIndex(0x1D, 0x25)
    SetChrSubChip(0x1D, 0x0)
    SetChrChipByIndex(0x1E, 0x2C)
    SetChrSubChip(0x1E, 0x0)
    SetChrPos(0x21, 1800, 150, 5650, 180)
    SetChrPos(0x22, 2800, 150, -4350, 180)
    SetChrPos(0x23, 2800, 150, 5650, 180)
    SetChrChipByIndex(0x21, 0x3E)
    SetChrSubChip(0x21, 0x0)
    SetChrChipByIndex(0x22, 0x3E)
    SetChrSubChip(0x22, 0x0)
    SetChrChipByIndex(0x23, 0x3E)
    SetChrSubChip(0x23, 0x0)
    FadeToBright(1000, 0)
    OP_68(0, 900, -5000, 7000)
    OP_0D()
    Sleep(3500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(0, 900, 7000, 0)
    SetChrPos(0x15, -2600, 150, -750, 0)
    SetChrPos(0x16, -2600, 150, 5650, 180)
    SetChrPos(0x17, -1600, 150, -3150, 0)
    SetChrPos(0x18, -1600, 150, 650, 180)
    SetChrPos(0x19, -1600, 150, 5650, 180)
    SetChrPos(0x1A, 1800, 150, -4350, 180)
    SetChrPos(0x1B, 1800, 150, 4350, 0)
    SetChrPos(0x1C, 2800, 150, -5650, 0)
    SetChrPos(0x1D, 2800, 150, -750, 0)
    SetChrPos(0x1E, 2800, 150, 650, 180)
    SetChrChipByIndex(0x15, 0x1E)
    SetChrSubChip(0x15, 0x0)
    SetChrChipByIndex(0x16, 0x1E)
    SetChrSubChip(0x16, 0x0)
    SetChrChipByIndex(0x17, 0x21)
    SetChrSubChip(0x17, 0x0)
    SetChrChipByIndex(0x18, 0x23)
    SetChrSubChip(0x18, 0x0)
    SetChrChipByIndex(0x19, 0x28)
    SetChrSubChip(0x19, 0x0)
    SetChrChipByIndex(0x1A, 0x1F)
    SetChrSubChip(0x1A, 0x0)
    SetChrChipByIndex(0x1B, 0x30)
    SetChrSubChip(0x1B, 0x0)
    SetChrChipByIndex(0x1C, 0x2E)
    SetChrSubChip(0x1C, 0x0)
    SetChrChipByIndex(0x1D, 0x26)
    SetChrSubChip(0x1D, 0x0)
    SetChrChipByIndex(0x1E, 0x35)
    SetChrSubChip(0x1E, 0x0)
    SetChrPos(0x21, -2600, 150, 1800, 0)
    SetChrPos(0x22, -2600, 150, 3150, 180)
    SetChrPos(0x23, 1800, 150, -1800, 180)
    SetChrChipByIndex(0x21, 0x3E)
    SetChrSubChip(0x21, 0x0)
    SetChrChipByIndex(0x22, 0x3E)
    SetChrSubChip(0x22, 0x0)
    SetChrChipByIndex(0x23, 0x3D)
    SetChrSubChip(0x23, 0x0)
    FadeToBright(1000, 0)
    OP_68(0, 900, -5000, 7000)
    OP_0D()
    Sleep(3500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopSound(450, 1000, 100)
    Sleep(1000)
    SetScenarioFlags(0x22, 0)
    NewScene("r1020", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_17_3F98 end

    def Function_18_473B(): pass

    label("Function_18_473B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearScenarioFlags(0x156, 7)
    OP_68(270, 1000, -8380, 0)
    MoveCamera(315, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(20000, 0)
    SetChrPos(0x0, -570, 0, -8020, 0)
    SetChrPos(0x1, 990, 0, -8210, 0)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    FadeToBright(1000, 0)
    OP_0D()

    #C0108
    ChrTalk(
        0x101,
        (
            "#00004F好，我们负责的是\x01",
            "后面的两节车厢。\x02\x03",

            "#00001F乘客的数量……\x01",
            "好像很多呢。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_487E")

    #C0109
    ChrTalk(
        0x102,
        (
            "#00100F是啊，总之，\x01",
            "我们就一个一个地仔细检查吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x79, 0x1, 0x0)
    Jump("loc_49BF")

    label("loc_487E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_48D3")

    #C0110
    ChrTalk(
        0x103,
        (
            "#00200F是啊，我们就从头到尾，\x01",
            "按顺序仔细检查一遍吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x79, 0x1, 0x1)
    Jump("loc_49BF")

    label("loc_48D3")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4920")

    #C0111
    ChrTalk(
        0x104,
        (
            "#00304F嗯，那就只能从头开始\x01",
            "一个一个检查了。\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x79, 0x1, 0x2)
    Jump("loc_49BF")

    label("loc_4920")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_496F")

    #C0112
    ChrTalk(
        0x109,
        (
            "#10100F是的，既然如此，\x01",
            "我们就仔细完成检查吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x79, 0x1, 0x3)
    Jump("loc_49BF")

    label("loc_496F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_49BF")

    #C0113
    ChrTalk(
        0x105,
        (
            "#10300F呼，看样子，也只能\x01",
            "从头到尾，完整检查一遍了。\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x79, 0x1, 0x4)

    label("loc_49BF")

    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_18_473B end

    def Function_19_49C6(): pass

    label("Function_19_49C6")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x156, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4A25")

    #C0114
    ChrTalk(
        0x101,
        (
            "#00003F……往这边走就是第三节车厢了，\x01",
            "先把第四节车厢的所有乘客检查完吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4A6F")

    label("loc_4A25")


    #C0115
    ChrTalk(
        0x101,
        (
            "#00003F……前面的车厢不是我们负责的，\x01",
            "还是专心检查自己负责的部分吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4A6F")

    Sleep(50)
    SetChrPos(0x0, -10, 0, 7470, 180)
    EventEnd(0x4)
    Return()

    # Function_19_49C6 end

    def Function_20_4A86(): pass

    label("Function_20_4A86")

    EventBegin(0x1)

    #C0116
    ChrTalk(
        0x101,
        (
            "#00003F……安检还没有完成，\x01",
            "不能离开列车。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, 2000, 0, -7850, 270)
    EventEnd(0x4)
    Return()

    # Function_20_4A86 end

    def Function_21_4ACF(): pass

    label("Function_21_4ACF")

    EventBegin(0x1)

    #C0117
    ChrTalk(
        0x101,
        (
            "#00003F……安检还没有完成，\x01",
            "不能离开列车。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, 2000, 0, 7850, 270)
    EventEnd(0x4)
    Return()

    # Function_21_4ACF end

    def Function_22_4B18(): pass

    label("Function_22_4B18")

    EventBegin(0x0)
    Fade(500)
    OP_68(-2120, 1000, -1250, 0)
    MoveCamera(315, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(20000, 0)
    SetChrPos(0x0, -500, 0, -2100, 270)
    SetChrPos(0x1, -500, 0, -3080, 315)
    OP_0D()

    #C0118
    ChrTalk(
        0x101,
        (
            "#00000F打扰一下，\x01",
            "我们是代理安检官。\x02\x03",

            "不好意思，\x01",
            "能否让我确认一下您的\x01",
            "随身行李和入境申请书呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0xC,
        "……妈妈…………\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4C2B")

    #C0120
    ChrTalk(
        0x102,
        (
            "#00105F（看样子，\x01",
            "  他好像没听见呢。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4D27")

    label("loc_4C2B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4C6C")

    #C0121
    ChrTalk(
        0x103,
        (
            "#00205F（看样子，\x01",
            "  他好像没听到呢。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4D27")

    label("loc_4C6C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4CA2")

    #C0122
    ChrTalk(
        0x104,
        "#00305F（唔，他没听到啊。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_4D27")

    label("loc_4CA2")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4CE3")

    #C0123
    ChrTalk(
        0x109,
        (
            "#10105F（那个……\x01",
            "  他好像没听见呢。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4D27")

    label("loc_4CE3")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4D27")

    #C0124
    ChrTalk(
        0x105,
        (
            "#10302F（呵呵，看起来，\x01",
            "  他好像是没听见啊。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4D27")


    #C0125
    ChrTalk(
        0x101,
        "#00006F#4S那个……打扰了！\x02",
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xC, 0x10)
    TurnDirection(0xC, 0x0, 0)
    OP_52(0xC, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4DED")
    Jump("loc_4E37")

    label("loc_4DED")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4E0D")
    OP_52(0xC, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4E37")

    label("loc_4E0D")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4E2D")
    OP_52(0xC, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4E37")

    label("loc_4E2D")

    OP_52(0xC, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4E37")

    OP_52(0xC, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xC, 0x10)

    #C0126
    ChrTalk(
        0xC,
        "哎，啊啊……抱歉。\x02",
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0xC,
        "我有点走神了。\x02",
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0xC,
        (
            "那个……你们是负责安检的人员吧？\x01",
            "麻烦你们检查吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0x101,
        "#00000F好的，那我现在就开始检查。\x02",
    )

    CloseMessageWindow()
    FadeToDark(500, 0, -1)
    OP_0D()
    Sleep(1000)
    FadeToBright(500, 0)
    OP_0D()

    #C0130
    ChrTalk(
        0x101,
        (
            "#00004F已经确认了您的\x01",
            "随身行李和入境申请书……\x01",
            "非常感谢您的配合。\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0xC,
        "啊，哪里，不用客气。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1CA, 4)
    OP_29(0x79, 0x1, 0x5)
    ClearChrFlags(0xC, 0x10)
    SetChrSubChip(0xC, 0x0)
    EventEnd(0x5)
    Return()

    # Function_22_4B18 end

    def Function_23_4F74(): pass

    label("Function_23_4F74")

    EventBegin(0x0)
    Fade(500)
    OP_68(1540, 1000, 90, 0)
    MoveCamera(315, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(20000, 0)
    SetChrPos(0x0, 500, 0, 440, 90)
    SetChrPos(0x1, 500, 0, -530, 90)
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xA, 0x10)
    TurnDirection(0xA, 0x0, 0)
    OP_52(0xA, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_505C")
    Jump("loc_50A6")

    label("loc_505C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_507C")
    OP_52(0xA, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_50A6")

    label("loc_507C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_509C")
    OP_52(0xA, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_50A6")

    label("loc_509C")

    OP_52(0xA, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_50A6")

    OP_52(0xA, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xA, 0x10)
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xB, 0x10)
    TurnDirection(0xB, 0x0, 0)
    OP_52(0xB, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_515C")
    Jump("loc_51A6")

    label("loc_515C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_517C")
    OP_52(0xB, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_51A6")

    label("loc_517C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_519C")
    OP_52(0xB, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_51A6")

    label("loc_519C")

    OP_52(0xB, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_51A6")

    OP_52(0xB, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xB, 0x10)
    OP_0D()

    #C0132
    ChrTalk(
        0x101,
        (
            "#00000F打扰一下，我们是代理安检官。\x02\x03",

            "不好意思，\x01",
            "能否让我确认一下二位的\x01",
            "随身行李和入境申请书呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0xA,
        "哦，当然没问题。\x02",
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0xB,
        (
            "安检～安检～¤\x01",
            "大哥哥，麻烦你们啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0x101,
        (
            "#00009F哈哈，那我就马上\x01",
            "开始检查了。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(500, 0, -1)
    OP_0D()
    Sleep(1000)
    FadeToBright(500, 0)
    OP_0D()

    #C0136
    ChrTalk(
        0x101,
        (
            "#00004F已经确认了二位的\x01",
            "随身行李和入境申请书……\x01",
            "非常感谢你们的配合。\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0xA,
        (
            "哪里，\x01",
            "这是应该的。\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0xB,
        (
            "大哥哥，\x01",
            "你们工作辛苦啦☆\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5363")

    #C0139
    ChrTalk(
        0x102,
        "#00102F呵呵，谢谢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_5419")

    label("loc_5363")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5394")

    #C0140
    ChrTalk(
        0x103,
        (
            "#00202F呵呵，\x01",
            "谢谢了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5419")

    label("loc_5394")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_53C2")

    #C0141
    ChrTalk(
        0x104,
        "#00309F哈哈，谢啦。\x02",
    )

    CloseMessageWindow()
    Jump("loc_5419")

    label("loc_53C2")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_53F0")

    #C0142
    ChrTalk(
        0x109,
        "#10109F呵呵，谢啦。\x02",
    )

    CloseMessageWindow()
    Jump("loc_5419")

    label("loc_53F0")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5419")

    #C0143
    ChrTalk(
        0x105,
        "#10309F呵呵，谢谢。\x02",
    )

    CloseMessageWindow()

    label("loc_5419")

    SetScenarioFlags(0x1CA, 3)
    OP_29(0x79, 0x1, 0x6)
    ClearChrFlags(0xA, 0x10)
    ClearChrFlags(0xB, 0x10)
    SetChrSubChip(0xA, 0x0)
    SetChrSubChip(0xB, 0x0)
    EventEnd(0x5)
    Return()

    # Function_23_4F74 end

    def Function_24_5437(): pass

    label("Function_24_5437")

    EventBegin(0x0)
    Fade(500)
    OP_68(-1090, 1000, 2420, 0)
    MoveCamera(315, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(20000, 0)
    SetChrPos(0x0, -470, 0, 2090, 270)
    SetChrPos(0x1, -470, 0, 3000, 225)
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x9, 0x10)
    TurnDirection(0x9, 0x0, 0)
    OP_52(0x9, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_551F")
    Jump("loc_5569")

    label("loc_551F")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_553F")
    OP_52(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5569")

    label("loc_553F")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_555F")
    OP_52(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5569")

    label("loc_555F")

    OP_52(0x9, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5569")

    OP_52(0x9, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x9, 0x10)
    OP_0D()

    #C0144
    ChrTalk(
        0x101,
        (
            "#00000F打扰一下，\x01",
            "我们是代理安检官。\x02\x03",

            "不好意思，\x01",
            "能否让我确认一下您的\x01",
            "随身行李和入境申请书呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0x9,
        "呵呵，等着你呢！\x02",
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0x9,
        "好了，请确认吧！\x02",
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0x101,
        "#00005F好、好的……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_566C")

    #C0148
    ChrTalk(
        0x102,
        "#00105F（情绪真高涨啊。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_5747")

    label("loc_566C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_56A0")

    #C0149
    ChrTalk(
        0x103,
        "#00200F（情绪真高涨呢。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_5747")

    label("loc_56A0")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_56D6")

    #C0150
    ChrTalk(
        0x104,
        "#00306F（情绪可真高涨啊。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_5747")

    label("loc_56D6")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5710")

    #C0151
    ChrTalk(
        0x109,
        "#10105F（情绪高涨得不正常呢。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_5747")

    label("loc_5710")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5747")

    #C0152
    ChrTalk(
        0x105,
        "#10303F（呵呵，情绪相当高涨呢。）\x02",
    )

    CloseMessageWindow()

    label("loc_5747")

    FadeToDark(500, 0, -1)
    OP_0D()
    Sleep(1000)
    FadeToBright(500, 0)
    OP_0D()

    #C0153
    ChrTalk(
        0x101,
        (
            "#00004F已经确认了您的\x01",
            "随身行李和入境申请书……\x01",
            "非常感谢您的配合。\x02",
        )
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0x9,
        (
            "呵呵呵，你也看到了吧？\x01",
            "这一大捆合同！\x02",
        )
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0x9,
        (
            "其实我正要去谈\x01",
            "一宗大生意呢！\x02",
        )
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0x9,
        (
            "只要能谈成，绝对可以大赚一笔！\x01",
            "哎呀呀，真是太期待了！\x02",
        )
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0x101,
        (
            "#00012F是、是吗……\x01",
            "希望您谈判顺利。\x02\x03",

            "#00003F（原来如此，这就是情绪高涨的\x01",
            "  原因啊。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1CA, 2)
    OP_29(0x79, 0x1, 0x7)
    ClearChrFlags(0x9, 0x10)
    SetChrSubChip(0x9, 0x0)
    EventEnd(0x5)
    Return()

    # Function_24_5437 end

    def Function_25_58A0(): pass

    label("Function_25_58A0")

    EventBegin(0x0)
    Fade(500)
    OP_68(570, 1000, 5250, 0)
    MoveCamera(315, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(20000, 0)
    SetChrPos(0x0, 500, 0, 5450, 90)
    SetChrPos(0x1, 500, 0, 4450, 90)
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x8, 0x10)
    TurnDirection(0x8, 0x0, 0)
    OP_52(0x8, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5988")
    Jump("loc_59D2")

    label("loc_5988")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_59A8")
    OP_52(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_59D2")

    label("loc_59A8")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_59C8")
    OP_52(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_59D2")

    label("loc_59C8")

    OP_52(0x8, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_59D2")

    OP_52(0x8, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x8, 0x10)
    OP_0D()

    #C0158
    ChrTalk(
        0x101,
        (
            "#00000F打扰一下，我们是代理安检官。\x02\x03",

            "不好意思，\x01",
            "能否让我确认一下您的\x01",
            "随身行李和入境申请书呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0x8,
        "哦，当然可以。\x02",
    )

    CloseMessageWindow()
    FadeToDark(500, 0, -1)
    OP_0D()
    Sleep(1000)
    FadeToBright(500, 0)
    OP_0D()

    #C0160
    ChrTalk(
        0x101,
        (
            "#00004F已经确认了您的\x01",
            "随身行李和入境申请书……\x02\x03",

            "#00001F可是……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0161
    ChrTalk(
        0x8,
        "嗯？怎么了？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5B51")

    #C0162
    ChrTalk(
        0x102,
        (
            "#00101F在您的行李中\x01",
            "并没有看到\x01",
            "车票啊。\x02\x03",

            "您还记得放在什么地方了吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5CB1")

    label("loc_5B51")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5BA7")

    #C0163
    ChrTalk(
        0x103,
        (
            "#00201F在您的行李中\x01",
            "没有发现\x01",
            "车票。\x02\x03",

            "记得放在什么地方了吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5CB1")

    label("loc_5BA7")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5BFF")

    #C0164
    ChrTalk(
        0x104,
        (
            "#00301F哦，在您的行李中\x01",
            "没有看到\x01",
            "车票。\x02\x03",

            "还记得放到哪里了吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5CB1")

    label("loc_5BFF")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5C55")

    #C0165
    ChrTalk(
        0x109,
        (
            "#10101F我们在您的行李中\x01",
            "没有找到\x01",
            "车票。\x02\x03",

            "您放在什么地方了？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5CB1")

    label("loc_5C55")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5CB1")

    #C0166
    ChrTalk(
        0x105,
        (
            "#10304F我们在您的行李中\x01",
            "没有看到\x01",
            "车票哦。\x02\x03",

            "#10302F还记得放到哪里了吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5CB1")

    OP_63(0x8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0167
    ChrTalk(
        0x8,
        "没、没有车票！？\x02",
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0x8,
        (
            "不可能啊，\x01",
            "我明明仔细收在包里了……！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x8)
    Sleep(1000)
    OP_63(0x8, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x8)

    #C0169
    ChrTalk(
        0x8,
        "……没有、没有、怎么都找不到！\x02",
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0x8,
        "是在衣服的口袋里吗？不对，可是……\x02",
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0x8,
        (
            "对、对不起，\x01",
            "再等我一下吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0x8,
        (
            "我真的有票，\x01",
            "一定能找到的！\x02",
        )
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0x101,
        (
            "#00005F好、好的……\x01",
            "那我们稍后再来找您。\x02\x03",

            "#00003F（没办法，先去检查其他乘客，\x01",
            "  稍后再回来一趟吧。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1CA, 1)
    OP_29(0x79, 0x1, 0x8)
    ClearChrFlags(0x8, 0x10)
    SetChrSubChip(0x8, 0x0)
    EventEnd(0x5)
    Return()

    # Function_25_58A0 end

    def Function_26_5E4D(): pass

    label("Function_26_5E4D")

    ModifyEventFlags(0, 3, 0x80)
    SetScenarioFlags(0x158, 6)
    Return()

    # Function_26_5E4D end

    def Function_27_5E56(): pass

    label("Function_27_5E56")

    EventBegin(0x0)
    Fade(500)
    OP_68(-1900, 1000, -1610, 0)
    MoveCamera(315, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(20000, 0)
    SetChrPos(0x0, -520, 0, -3000, 270)
    SetChrPos(0x1, -520, 0, -2100, 270)
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x12, 0x10)
    TurnDirection(0x12, 0x0, 0)
    OP_52(0x12, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5F3E")
    Jump("loc_5F88")

    label("loc_5F3E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5F5E")
    OP_52(0x12, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5F88")

    label("loc_5F5E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5F7E")
    OP_52(0x12, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5F88")

    label("loc_5F7E")

    OP_52(0x12, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5F88")

    OP_52(0x12, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x12, 0x10)
    OP_0D()

    #C0174
    ChrTalk(
        0x101,
        (
            "#00000F打扰一下，\x01",
            "我们是代理安检官。\x02\x03",

            "不好意思，\x01",
            "能否让我确认一下您的\x01",
            "随身行李和入境申请书呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0x12,
        (
            "哼，话倒是说得客气，\x01",
            "但我根本就没有拒绝的权利吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0x12,
        (
            "既然如此，那就不要\x01",
            "一个一个地问，\x01",
            "赶快把工作完成就是了。\x02",
        )
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0x101,
        "#00006F好的，真抱歉。\x02",
    )

    CloseMessageWindow()
    FadeToDark(500, 0, -1)
    OP_0D()
    Sleep(1000)
    FadeToBright(500, 0)
    OP_0D()

    #C0178
    ChrTalk(
        0x101,
        (
            "#00004F已经确认了您的\x01",
            "随身行李和入境申请书……\x01",
            "非常感谢您的配合。\x02",
        )
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0x12,
        (
            "……哼，我都说过了，\x01",
            "这种客套话是多余的。\x02",
        )
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0x12,
        (
            "没别的事了吧？\x01",
            "那就赶快走吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0x101,
        "#00005F好、好的，打扰您了。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_61BF")

    #C0182
    ChrTalk(
        0x102,
        (
            "#00106F（呼，这项工作真是很\x01",
            "  磨练人的意志啊。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_62E5")

    label("loc_61BF")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6208")

    #C0183
    ChrTalk(
        0x103,
        (
            "#00206F（呼……\x01",
            "  这个工作很磨练人的意志呢。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_62E5")

    label("loc_6208")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6251")

    #C0184
    ChrTalk(
        0x104,
        (
            "#00306F（呼，这个工作也很\x01",
            "  磨练人的意志啊。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_62E5")

    label("loc_6251")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6298")

    #C0185
    ChrTalk(
        0x109,
        (
            "#10106F（呼，真是个很考验\x01",
            "  意志的工作啊。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_62E5")

    label("loc_6298")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_62E5")

    #C0186
    ChrTalk(
        0x105,
        (
            "#10304F（呵呵，安检官\x01",
            "  也是一份很有压力的\x01",
            "  工作啊。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_62E5")

    OP_5A()
    SetScenarioFlags(0x1CB, 0)
    OP_29(0x79, 0x1, 0x9)
    ClearChrFlags(0x12, 0x10)
    SetChrSubChip(0x12, 0x0)
    EventEnd(0x5)
    Return()

    # Function_27_5E56 end

    def Function_28_62FB(): pass

    label("Function_28_62FB")

    EventBegin(0x0)
    Fade(500)
    OP_68(1240, 1000, -2420, 0)
    MoveCamera(315, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(20000, 0)
    SetChrPos(0x0, 490, 0, -1970, 90)
    SetChrPos(0x1, 490, 0, -3000, 90)
    OP_0D()

    #C0187
    ChrTalk(
        0x11,
        (
            "呵呵呵，\x01",
            "『艾森古拉夫号』\x01",
            "果然和其它列车完全不同啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0x11,
        (
            "（流口水）……\x01",
            "噢，不行不行。\x02",
        )
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0x101,
        (
            "#00006F（在、在流口水……？）\x02\x03",

            "#00000F不好意思，\x01",
            "我们是代理安检官……\x02",
        )
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0x11,
        (
            "啊，我正在观察列车，\x01",
            "忙得很。\x02",
        )
    )

    CloseMessageWindow()

    #C0191
    ChrTalk(
        0x11,
        (
            "申请书就放在包里，\x01",
            "不用客气，自己去翻吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0x101,
        (
            "#00003F知、知道了，\x01",
            "既然您都这么说了……\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(500, 0, -1)
    OP_0D()
    Sleep(1000)
    FadeToBright(500, 0)
    OP_0D()

    #C0193
    ChrTalk(
        0x101,
        (
            "#00004F已经确认了您的\x01",
            "随身行李和入境申请书……\x01",
            "非常感谢您的配合。\x02",
        )
    )

    CloseMessageWindow()

    #C0194
    ChrTalk(
        0x11,
        (
            "（嘀嘀咕咕）……\x01",
            "距离发车还有几分钟？\x02",
        )
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0x11,
        "啊啊，真是让人依依不舍啊……！\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_656E")

    #C0196
    ChrTalk(
        0x102,
        (
            "#00103F（……精、精神真是\x01",
            "  相当集中啊。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6671")

    label("loc_656E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_65BB")

    #C0197
    ChrTalk(
        0x103,
        (
            "#00203F（……直到最后，\x01",
            "  她也没有转过一次头呢。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6671")

    label("loc_65BB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_65F3")

    #C0198
    ChrTalk(
        0x104,
        "#00306F（……完全没在听呢。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_6671")

    label("loc_65F3")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_663A")

    #C0199
    ChrTalk(
        0x109,
        (
            "#10106F（……这个人真是相当\x01",
            "  喜欢列车啊。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6671")

    label("loc_663A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6671")

    #C0200
    ChrTalk(
        0x105,
        "#10302F（呵呵，她根本没听到呢。）\x02",
    )

    CloseMessageWindow()

    label("loc_6671")

    OP_5A()
    SetScenarioFlags(0x1CA, 7)
    OP_29(0x79, 0x1, 0xA)
    EventEnd(0x5)
    Return()

    # Function_28_62FB end

    def Function_29_667E(): pass

    label("Function_29_667E")

    EventBegin(0x0)
    Fade(500)
    OP_68(-1170, 1000, -100, 0)
    MoveCamera(324, 28, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18000, 0)
    SetChrPos(0x0, -530, 0, 410, 270)
    SetChrPos(0x1, -530, 0, -410, 270)
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xF, 0x10)
    TurnDirection(0xF, 0x0, 0)
    OP_52(0xF, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_6766")
    Jump("loc_67B0")

    label("loc_6766")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_6786")
    OP_52(0xF, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_67B0")

    label("loc_6786")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_67A6")
    OP_52(0xF, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_67B0")

    label("loc_67A6")

    OP_52(0xF, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_67B0")

    OP_52(0xF, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xF, 0x10)
    OP_0D()

    #C0201
    ChrTalk(
        0x101,
        "#00000F不好意思，我们是代理安检官……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0202
    ChrTalk(
        0x101,
        (
            "#00005F（这身衣服……\x01",
            "  莫非他们是『黑月』的成员吗？）\x02",
        )
    )

    CloseMessageWindow()

    #C0203
    ChrTalk(
        0xF,
        "唔，有什么问题吗？\x02",
    )

    CloseMessageWindow()
    OP_4B(0x10, 0xFF)
    Sleep(300)
    OP_93(0x10, 0x5A, 0x1F4)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_6DB8")
    OP_29(0x79, 0x1, 0xB)

    #C0204
    ChrTalk(
        0x10,
        "嗯？有什么事吗？\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x10, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0205
    ChrTalk(
        0x101,
        "#00011F哎，秦？\x02",
    )

    CloseMessageWindow()

    #C0206
    ChrTalk(
        0x10,
        (
            "啊，你是特别\x01",
            "任务支援科的……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_695D")

    #C0207
    ChrTalk(
        0x10,
        (
            "而且竟然连艾莉姐姐\x01",
            "也在一起！\x02",
        )
    )

    CloseMessageWindow()

    #C0208
    ChrTalk(
        0x102,
        "#00102F呵呵，你好啊，秦。\x02",
    )

    CloseMessageWindow()

    label("loc_695D")


    #C0209
    ChrTalk(
        0x10,
        (
            "你们在这里\x01",
            "干什么呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0210
    ChrTalk(
        0x101,
        (
            "#00000F哦，这是特别任务支援科的工作，\x01",
            "要协助完成列车上的安检。\x02\x03",

            "所以需要确认一下各位的\x01",
            "随身行李与入境申请书……\x02",
        )
    )

    CloseMessageWindow()

    #C0211
    ChrTalk(
        0x10,
        (
            "原来如此，支援科\x01",
            "还要做这种工作啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0212
    ChrTalk(
        0x10,
        (
            "知道了，既然如此，\x01",
            "就赶快来检查吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(500, 0, -1)
    OP_0D()
    Sleep(1000)
    FadeToBright(500, 0)
    OP_0D()

    #C0213
    ChrTalk(
        0x101,
        (
            "#00004F好，\x01",
            "已经确认过二位的\x01",
            "行李和入境申请书了。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6B30")

    #C0214
    ChrTalk(
        0x102,
        "#00100F谢谢你们的配合哦。\x02",
    )

    CloseMessageWindow()

    #C0215
    ChrTalk(
        0x10,
        (
            "呵呵，为了大姐姐，\x01",
            "这不算什么。\x02",
        )
    )

    CloseMessageWindow()

    #C0216
    ChrTalk(
        0x10,
        "有朝一日，我们一定还要再见面啊！\x02",
    )

    CloseMessageWindow()

    #C0217
    ChrTalk(
        0x102,
        "#00109F嗯，我很期待那一天呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_6DB3")

    label("loc_6B30")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6C34")

    #C0218
    ChrTalk(
        0x103,
        "#00200F非常感谢二位的配合。\x02",
    )

    CloseMessageWindow()

    #C0219
    ChrTalk(
        0x10,
        (
            "（唔，原来支援科\x01",
            "  还有这样的少女啊。）\x02",
        )
    )

    CloseMessageWindow()

    #C0220
    ChrTalk(
        0x103,
        "#00200F……我的脸上有什么东西吗？\x02",
    )

    CloseMessageWindow()
    OP_63(0x10, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_63(0x10, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x10)

    #C0221
    ChrTalk(
        0x10,
        "啊、不不，什么都没有！\x02",
    )

    CloseMessageWindow()

    #C0222
    ChrTalk(
        0x10,
        "那就再见吧。\x02",
    )

    CloseMessageWindow()

    #C0223
    ChrTalk(
        0x101,
        "#00009F嗯，秦也要保重啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_6DB3")

    label("loc_6C34")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6CB6")

    #C0224
    ChrTalk(
        0x104,
        "#00300F多谢二位的配合。\x02",
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0x10,
        (
            "哼，这只是我们\x01",
            "应该做的。\x02",
        )
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0x10,
        "那就再见吧。\x02",
    )

    CloseMessageWindow()

    #C0227
    ChrTalk(
        0x101,
        "#00009F嗯，秦也要保重啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_6DB3")

    label("loc_6CB6")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6D3A")

    #C0228
    ChrTalk(
        0x109,
        "#10100F多谢二位的配合哦。\x02",
    )

    CloseMessageWindow()

    #C0229
    ChrTalk(
        0x10,
        (
            "哼，这只是我们\x01",
            "应该做的。\x02",
        )
    )

    CloseMessageWindow()

    #C0230
    ChrTalk(
        0x10,
        "那就再见吧。\x02",
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0x101,
        "#00009F嗯，秦也要保重啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_6DB3")

    label("loc_6D3A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6DB3")

    #C0232
    ChrTalk(
        0x105,
        "#10300F多谢配合了。\x02",
    )

    CloseMessageWindow()

    #C0233
    ChrTalk(
        0x10,
        (
            "哼，这只是我们\x01",
            "应该做的。\x02",
        )
    )

    CloseMessageWindow()

    #C0234
    ChrTalk(
        0x10,
        "那就再见吧。\x02",
    )

    CloseMessageWindow()

    #C0235
    ChrTalk(
        0x101,
        "#00009F嗯，秦也要保重啊。\x02",
    )

    CloseMessageWindow()

    label("loc_6DB3")

    Jump("loc_73CD")

    label("loc_6DB8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_708D")
    OP_29(0x79, 0x1, 0xB)

    #C0236
    ChrTalk(
        0x10,
        "嗯？有什么事吗？\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x10, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0237
    ChrTalk(
        0x101,
        "#00005F那个，你不是黑月的……？\x02",
    )

    CloseMessageWindow()

    #C0238
    ChrTalk(
        0x10,
        (
            "啊，你是特别\x01",
            "任务支援科的……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6EE6")

    #C0239
    ChrTalk(
        0x10,
        (
            "而且竟然连艾莉姐姐\x01",
            "也在一起！\x02",
        )
    )

    CloseMessageWindow()

    #C0240
    ChrTalk(
        0x102,
        "#00102F呵呵，你好啊，秦。\x02",
    )

    CloseMessageWindow()

    #C0241
    ChrTalk(
        0x10,
        "啊……嗯嗯……\x02",
    )

    CloseMessageWindow()

    #C0242
    ChrTalk(
        0x10,
        "对了，你们在这里干什么呢？\x02",
    )

    CloseMessageWindow()
    Jump("loc_6F00")

    label("loc_6EE6")


    #C0243
    ChrTalk(
        0x10,
        "你们在这里干什么呢？\x02",
    )

    CloseMessageWindow()

    label("loc_6F00")


    #C0244
    ChrTalk(
        0x101,
        (
            "#00000F哦，这是特别任务支援科的工作，\x01",
            "要协助完成列车上的安检。\x02\x03",

            "所以需要确认一下二位的\x01",
            "随身行李与入境申请书……\x02",
        )
    )

    CloseMessageWindow()

    #C0245
    ChrTalk(
        0x10,
        (
            "原来如此，支援科\x01",
            "还要做这种工作啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0246
    ChrTalk(
        0x10,
        (
            "知道了，既然如此，\x01",
            "就赶快来检查吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(500, 0, -1)
    OP_0D()
    Sleep(1000)
    FadeToBright(500, 0)
    OP_0D()

    #C0247
    ChrTalk(
        0x101,
        (
            "#00004F好，\x01",
            "已经确认过二位的\x01",
            "行李和入境申请书了。\x02\x03",

            "多谢配合哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0248
    ChrTalk(
        0x10,
        (
            "哼，这只是我们\x01",
            "应该做的。\x02",
        )
    )

    CloseMessageWindow()

    #C0249
    ChrTalk(
        0x10,
        "既然已经没事了，就赶快走吧。\x02",
    )

    CloseMessageWindow()

    #C0250
    ChrTalk(
        0x101,
        "#00006F啊……嗯嗯……打扰了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_73CD")

    label("loc_708D")


    #N0251
    NpcTalk(
        0x10,
        "男孩",
        "嗯？有什么事吗？\x02",
    )

    CloseMessageWindow()
    OP_29(0x79, 0x1, 0xC)

    #C0252
    ChrTalk(
        0x101,
        (
            "#00000F打扰一下，我们是代理安检官。\x02\x03",

            "不好意思，\x01",
            "能否让我确认一下二位的\x01",
            "随身行李和入境申请书呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0253
    ChrTalk(
        0xF,
        "嗯，当然可以。\x02",
    )

    CloseMessageWindow()

    #N0254
    NpcTalk(
        0x10,
        "男孩",
        "哦，不过动作可要麻利些。\x02",
    )

    CloseMessageWindow()

    #C0255
    ChrTalk(
        0x101,
        "#00006F知、知道了……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_71BE")

    #C0256
    ChrTalk(
        0x102,
        (
            "#00105F（这孩子也和黑月有什么关系吗？\x01",
            "  态度真是很傲慢啊……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_731D")

    label("loc_71BE")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7217")

    #C0257
    ChrTalk(
        0x103,
        (
            "#00205F（这孩子也和黑月有什么关系吗？\x01",
            "  态度真是很傲慢呢……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_731D")

    label("loc_7217")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7270")

    #C0258
    ChrTalk(
        0x104,
        (
            "#00303F（这小鬼也和黑月有什么关系吗？\x01",
            "  态度怎么这么傲慢……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_731D")

    label("loc_7270")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_72C9")

    #C0259
    ChrTalk(
        0x109,
        (
            "#10105F（这孩子也和黑月有什么关系吗？\x01",
            "  态度真是很傲慢啊……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_731D")

    label("loc_72C9")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_731D")

    #C0260
    ChrTalk(
        0x105,
        (
            "#10304F（这孩子也和黑月有什么关系吗？\x01",
            "  态度真是相当傲慢……）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_731D")

    FadeToDark(500, 0, -1)
    OP_0D()
    Sleep(1000)
    FadeToBright(500, 0)
    OP_0D()

    #C0261
    ChrTalk(
        0x101,
        (
            "#00004F已经确认过二位的\x01",
            "行李和入境申请书了，\x01",
            "多谢配合。\x02",
        )
    )

    CloseMessageWindow()

    #C0262
    ChrTalk(
        0xF,
        "哪里，不用客气。\x02",
    )

    CloseMessageWindow()

    #N0263
    NpcTalk(
        0x10,
        "男孩",
        (
            "哼，既然已经没事了，\x01",
            "就赶快走吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0264
    ChrTalk(
        0x101,
        "#00006F啊……嗯……\x02",
    )

    CloseMessageWindow()

    label("loc_73CD")

    OP_5A()
    SetScenarioFlags(0x1CA, 6)
    OP_4C(0x10, 0xFF)
    OP_93(0x10, 0x10E, 0x0)
    ClearChrFlags(0xF, 0x10)
    SetChrSubChip(0xF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_29_667E end

    def Function_30_73E8(): pass

    label("Function_30_73E8")

    EventBegin(0x0)
    Fade(500)
    OP_68(1640, 1000, 2570, 0)
    MoveCamera(315, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(20000, 0)
    SetChrPos(0x0, 520, 0, 2930, 90)
    SetChrPos(0x1, 520, 0, 2090, 90)
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xD, 0x10)
    TurnDirection(0xD, 0x0, 0)
    OP_52(0xD, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_74D0")
    Jump("loc_751A")

    label("loc_74D0")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_74F0")
    OP_52(0xD, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_751A")

    label("loc_74F0")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7510")
    OP_52(0xD, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_751A")

    label("loc_7510")

    OP_52(0xD, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_751A")

    OP_52(0xD, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xD, 0x10)
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xE, 0x10)
    TurnDirection(0xE, 0x0, 0)
    OP_52(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_75D0")
    Jump("loc_761A")

    label("loc_75D0")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_75F0")
    OP_52(0xE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_761A")

    label("loc_75F0")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7610")
    OP_52(0xE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_761A")

    label("loc_7610")

    OP_52(0xE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_761A")

    OP_52(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xE, 0x10)
    OP_0D()

    #C0265
    ChrTalk(
        0x101,
        (
            "#00000F打扰一下，我们是代理安检官。\x02\x03",

            "不好意思，\x01",
            "能否让我确认一下二位的\x01",
            "随身行李和入境申请书呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0266
    ChrTalk(
        0xD,
        (
            "哎，为什么非要接受\x01",
            "这种检查啊？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xE)
    SetChrSubChip(0xE, 0x0)

    #C0267
    ChrTalk(
        0xE,
        (
            "喂！\x01",
            "怎么可以对安检官先生说这种话！\x02",
        )
    )

    CloseMessageWindow()
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xE, 0x10)
    TurnDirection(0xE, 0x0, 0)
    OP_52(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_77A0")
    Jump("loc_77EA")

    label("loc_77A0")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_77C0")
    OP_52(0xE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_77EA")

    label("loc_77C0")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_77E0")
    OP_52(0xE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_77EA")

    label("loc_77E0")

    OP_52(0xE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_77EA")

    OP_52(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xE, 0x10)

    #C0268
    ChrTalk(
        0xE,
        (
            "对不起，\x01",
            "我的妹妹太没礼貌了。\x02",
        )
    )

    CloseMessageWindow()

    #C0269
    ChrTalk(
        0xE,
        (
            "她就是个笨蛋，\x01",
            "还请多多原谅。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 1700, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    SetChrSubChip(0xD, 0x0)

    #C0270
    ChrTalk(
        0xD,
        (
            "你说什么！？谁是笨蛋啊！\x01",
            "哥哥才是笨蛋呢！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0271
    ChrTalk(
        0x101,
        "#00006F（那个……我们可以开始检查了吗？）\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_793B")

    #C0272
    ChrTalk(
        0x102,
        "#00100F（嗯，我觉得可以。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_7A10")

    label("loc_793B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_796F")

    #C0273
    ChrTalk(
        0x103,
        "#00200F（嗯，我看可以。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_7A10")

    label("loc_796F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_79A5")

    #C0274
    ChrTalk(
        0x104,
        "#00300F（嗯，我看没问题。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_7A10")

    label("loc_79A5")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_79DD")

    #C0275
    ChrTalk(
        0x109,
        "#10100F（是的，我认为可以。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_7A10")

    label("loc_79DD")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7A10")

    #C0276
    ChrTalk(
        0x105,
        "#10300F（呵呵，我想没问题。）\x02",
    )

    CloseMessageWindow()

    label("loc_7A10")

    FadeToDark(500, 0, -1)
    OP_0D()
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xD, 0x10)
    TurnDirection(0xD, 0x0, 0)
    OP_52(0xD, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_7AAC")
    Jump("loc_7AF6")

    label("loc_7AAC")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_7ACC")
    OP_52(0xD, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7AF6")

    label("loc_7ACC")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7AEC")
    OP_52(0xD, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7AF6")

    label("loc_7AEC")

    OP_52(0xD, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7AF6")

    OP_52(0xD, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xD, 0x10)
    Sleep(1000)
    FadeToBright(500, 0)
    OP_0D()

    #C0277
    ChrTalk(
        0x101,
        (
            "#00004F已经确认过二位的\x01",
            "行李和入境申请书了。\x01",
            "多谢配合。\x02",
        )
    )

    CloseMessageWindow()

    #C0278
    ChrTalk(
        0xE,
        (
            "哪里哪里，我妹妹给你们添麻烦了，\x01",
            "实在抱歉。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 1700, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    SetChrSubChip(0xD, 0x0)

    #C0279
    ChrTalk(
        0xD,
        (
            "这叫什么话！说起来，\x01",
            "哥哥你才……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0280
    ChrTalk(
        0x101,
        "#00003F（我们还是早点离开为好啊。）\x02",
    )

    CloseMessageWindow()
    OP_5A()
    SetScenarioFlags(0x1CA, 5)
    OP_29(0x79, 0x1, 0xD)
    ClearChrFlags(0xD, 0x10)
    ClearChrFlags(0xE, 0x10)
    SetChrSubChip(0xD, 0x0)
    SetChrSubChip(0xE, 0x0)
    EventEnd(0x5)
    Return()

    # Function_30_73E8 end

    def Function_31_7C57(): pass

    label("Function_31_7C57")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(270, 1000, -8380, 0)
    MoveCamera(315, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(20000, 0)
    SetChrPos(0x0, -570, 0, -8020, 90)
    SetChrPos(0x1, 990, 0, -8210, 270)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8)
    SetChrPos(0x8, 770, 0, -16190, 0)
    FadeToBright(1000, 0)
    OP_0D()

    #C0281
    ChrTalk(
        0x101,
        "#00000F好，已经全部检查完毕了。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7D4C")

    #C0282
    ChrTalk(
        0x102,
        (
            "#00105F对了，还没去检查\x01",
            "四号车厢那个老爷爷的\x01",
            "票呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7E87")

    label("loc_7D4C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7D9C")

    #C0283
    ChrTalk(
        0x103,
        (
            "#00205F对了，还没去检查\x01",
            "四号车厢那个老爷爷的\x01",
            "车票呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7E87")

    label("loc_7D9C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7DEC")

    #C0284
    ChrTalk(
        0x104,
        (
            "#00305F对了，还没去检查\x01",
            "四号车厢那个老爷爷的\x01",
            "车票呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7E87")

    label("loc_7DEC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7E3C")

    #C0285
    ChrTalk(
        0x109,
        (
            "#10105F对了，还没去检查\x01",
            "四号车厢那个老爷爷的\x01",
            "车票呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7E87")

    label("loc_7E3C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7E87")

    #C0286
    ChrTalk(
        0x105,
        (
            "#10305F对了，还没去检查\x01",
            "四号车厢那个老爷爷的\x01",
            "车票呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7E87")


    #C0287
    ChrTalk(
        0x101,
        (
            "#00003F哦，是啊，\x01",
            "那我们现在就回去检……\x02",
        )
    )

    CloseMessageWindow()
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    #C0288
    ChrTalk(
        0x8,
        "把、把我的票还给我！\x02",
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7F3D")

    #C0289
    ChrTalk(
        0x102,
        "#00101F罗伊德！\x02",
    )

    CloseMessageWindow()
    Jump("loc_7FE8")

    label("loc_7F3D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7F6B")

    #C0290
    ChrTalk(
        0x103,
        "#00201F罗伊德前辈！\x02",
    )

    CloseMessageWindow()
    Jump("loc_7FE8")

    label("loc_7F6B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7F95")

    #C0291
    ChrTalk(
        0x104,
        "#00301F罗伊德！\x02",
    )

    CloseMessageWindow()
    Jump("loc_7FE8")

    label("loc_7F95")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7FC3")

    #C0292
    ChrTalk(
        0x109,
        "#10101F罗伊德警官！\x02",
    )

    CloseMessageWindow()
    Jump("loc_7FE8")

    label("loc_7FC3")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7FE8")

    #C0293
    ChrTalk(
        0x105,
        "#10301F罗伊德！\x02",
    )

    CloseMessageWindow()

    label("loc_7FE8")


    #C0294
    ChrTalk(
        0x101,
        "#00000F嗯，我们赶快过去！\x02",
    )

    CloseMessageWindow()
    Call(0, 32)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_801E")
    Call(0, 34)
    Jump("loc_8021")

    label("loc_801E")

    Call(0, 33)

    label("loc_8021")

    EventEnd(0x5)
    Return()

    # Function_31_7C57 end

    def Function_32_8024(): pass

    label("Function_32_8024")

    FadeToDark(1000, 0, -1)
    OP_0D()
    ClearScenarioFlags(0x156, 7)
    Call(0, 2)
    LoadChrToIndex("chr/ch20800.itc", 0x1E)
    LoadChrToIndex("chr/ch21800.itc", 0x1F)
    LoadChrToIndex("chr/ch21000.itc", 0x20)
    LoadChrToIndex("chr/ch22300.itc", 0x21)
    LoadChrToIndex("chr/ch22800.itc", 0x22)
    LoadChrToIndex("chr/ch47600.itc", 0x23)
    ClearChrFlags(0x8, 0x8)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    ClearChrBattleFlags(0x8, 0x4)
    ClearChrFlags(0x8, 0x20)
    SetChrChipByIndex(0x9, 0x1F)
    SetChrSubChip(0x9, 0x0)
    ClearChrBattleFlags(0x9, 0x4)
    ClearChrFlags(0x9, 0x20)
    SetChrChipByIndex(0xA, 0x20)
    SetChrSubChip(0xA, 0x0)
    ClearChrBattleFlags(0xA, 0x4)
    ClearChrFlags(0xA, 0x20)
    SetChrChipByIndex(0xB, 0x21)
    SetChrSubChip(0xB, 0x0)
    ClearChrBattleFlags(0xB, 0x4)
    ClearChrFlags(0xB, 0x20)
    SetChrChipByIndex(0xC, 0x22)
    SetChrSubChip(0xC, 0x0)
    ClearChrBattleFlags(0xC, 0x4)
    ClearChrFlags(0xC, 0x20)
    SetChrChipByIndex(0xF, 0x23)
    SetChrSubChip(0xF, 0x0)
    ClearChrBattleFlags(0xF, 0x4)
    ClearChrFlags(0xF, 0x20)
    SetChrPos(0x8, -50, 0, 1590, 180)
    SetChrPos(0x9, -550, 0, -250, 0)
    SetChrPos(0xC, 670, 0, -180, 0)
    SetChrPos(0xA, -1670, 0, -2540, 45)
    SetChrPos(0xB, -2540, 0, -2720, 90)
    SetChrPos(0x101, 460, 0, 7860, 180)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8156")
    SetChrPos(0x102, -480, 0, 8210, 180)
    Jump("loc_81E9")

    label("loc_8156")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_817C")
    SetChrPos(0x103, -480, 0, 8210, 180)
    Jump("loc_81E9")

    label("loc_817C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_81A2")
    SetChrPos(0x104, -480, 0, 8210, 180)
    Jump("loc_81E9")

    label("loc_81A2")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_81C8")
    SetChrPos(0x109, -480, 0, 8210, 180)
    Jump("loc_81E9")

    label("loc_81C8")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_81E9")
    SetChrPos(0x105, -480, 0, 8210, 180)

    label("loc_81E9")

    OP_68(120, 1000, 220, 0)
    MoveCamera(315, 27, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17500, 0)
    FadeToBright(1000, 0)
    OP_0D()

    #C0295
    ChrTalk(
        0x8,
        (
            "我说过了，肯定就是你们两个\x01",
            "之中的一个人干的！\x02",
        )
    )

    CloseMessageWindow()

    #C0296
    ChrTalk(
        0x8,
        (
            "快说！到底是谁！\x01",
            "赶快坦白吧！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(1000)

    def lambda_827F():
        OP_95(0x101, 460, 0, 3200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_827F)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_82C3")

    def lambda_82A9():
        OP_95(0x102, -480, 0, 3600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_82A9)
    Jump("loc_837A")

    label("loc_82C3")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_82F2")

    def lambda_82D8():
        OP_95(0x103, -480, 0, 3600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_82D8)
    Jump("loc_837A")

    label("loc_82F2")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8321")

    def lambda_8307():
        OP_95(0x104, -480, 0, 3600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_8307)
    Jump("loc_837A")

    label("loc_8321")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8350")

    def lambda_8336():
        OP_95(0x109, -480, 0, 3600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_8336)
    Jump("loc_837A")

    label("loc_8350")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_837A")

    def lambda_8365():
        OP_95(0x105, -480, 0, 3600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_8365)

    label("loc_837A")

    OP_68(70, 1000, 2830, 3000)
    MoveCamera(315, 25, 0, 3000)
    OP_6E(500, 3000)
    SetCameraDistance(16500, 3000)
    OP_6F(0x79)

    #C0297
    ChrTalk(
        0x101,
        "#00005F请问……发生什么事了？\x02",
    )

    CloseMessageWindow()

    #C0298
    ChrTalk(
        0xC,
        "啊，是刚才的安检官啊。\x02",
    )

    CloseMessageWindow()

    #C0299
    ChrTalk(
        0x9,
        (
            "这个老头子\x01",
            "想耍赖讹人！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0300
    ChrTalk(
        0x8,
        (
            "你说什么！？\x01",
            "你这厚颜无耻的家伙！\x02",
        )
    )

    CloseMessageWindow()

    #C0301
    ChrTalk(
        0x101,
        "#00011F请、请冷静些！\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_84AA")

    #C0302
    ChrTalk(
        0x102,
        (
            "#00101F那个……先把事情的经过\x01",
            "告诉我们如何？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_85C5")

    label("loc_84AA")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_84F3")

    #C0303
    ChrTalk(
        0x103,
        (
            "#00200F那个……可以先把事情的经过\x01",
            "告诉我们吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_85C5")

    label("loc_84F3")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_853A")

    #C0304
    ChrTalk(
        0x104,
        (
            "#00303F总之，还是先把\x01",
            "事情的经过告诉我们吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_85C5")

    label("loc_853A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8583")

    #C0305
    ChrTalk(
        0x109,
        (
            "#10101F总之，首先还是把\x01",
            "事情的经过告诉我们吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_85C5")

    label("loc_8583")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_85C5")

    #C0306
    ChrTalk(
        0x105,
        (
            "#10304F总之，先把事情的经过\x01",
            "说给我们听听吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_85C5")

    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x101, 550, 0, 1100, 180)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8607")
    SetChrPos(0x102, -540, 0, 1100, 180)
    Jump("loc_869A")

    label("loc_8607")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_862D")
    SetChrPos(0x103, -540, 0, 1100, 180)
    Jump("loc_869A")

    label("loc_862D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8653")
    SetChrPos(0x104, -540, 0, 1100, 180)
    Jump("loc_869A")

    label("loc_8653")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8679")
    SetChrPos(0x109, -540, 0, 1100, 180)
    Jump("loc_869A")

    label("loc_8679")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_869A")
    SetChrPos(0x105, -540, 0, 1100, 180)

    label("loc_869A")

    SetChrPos(0x8, -1580, 0, -60, 90)
    SetChrPos(0x9, -550, 0, -1300, 0)
    SetChrPos(0xC, 540, 0, -1300, 0)
    OP_68(-1060, 1000, 820, 0)
    MoveCamera(307, 26, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18110, 0)
    FadeToBright(1000, 0)
    OP_0D()

    #C0307
    ChrTalk(
        0x101,
        (
            "#00003F原来如此，老爷爷\x01",
            "买的车票是开往奥雷德自治州的，\x01",
            "而且是四号车厢的票……\x02\x03",

            "而持有这种车票的人，\x01",
            "在整节车厢中只有他们两人……\x02\x03",

            "#00001F也就是说，在他们两人之中，\x01",
            "可能有其中一人偷了您的票。\x01",
            "是这样吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0308
    ChrTalk(
        0x8,
        "嗯，正是如此。\x02",
    )

    CloseMessageWindow()

    #C0309
    ChrTalk(
        0x8,
        (
            "总之，\x01",
            "我拿着车票进站\x01",
            "是不争的事实。\x02",
        )
    )

    CloseMessageWindow()

    #C0310
    ChrTalk(
        0x8,
        (
            "在这么短的时间之内，\x01",
            "我的票不可能无缘无故地消失。\x02",
        )
    )

    CloseMessageWindow()

    #C0311
    ChrTalk(
        0x8,
        (
            "所以说，肯定是\x01",
            "被人偷走了。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0312
    ChrTalk(
        0x101,
        (
            "#00006F嗯……我认为不能这么简单\x01",
            "就妄下断言……\x02",
        )
    )

    CloseMessageWindow()

    #C0313
    ChrTalk(
        0x9,
        (
            "没关系、没关系，\x01",
            "不用客气，继续说啊！\x02",
        )
    )

    CloseMessageWindow()

    #C0314
    ChrTalk(
        0x9,
        "明明就是老年痴呆，自己弄丢了而已！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x9, 500)

    #C0315
    ChrTalk(
        0x8,
        "你还敢说……！\x02",
    )

    CloseMessageWindow()

    #C0316
    ChrTalk(
        0x101,
        (
            "#00006F好了，\x01",
            "二位都先冷静一下吧。\x02\x03",

            "#00001F不管怎么说，\x01",
            "如果光是这样感情用事，\x01",
            "是无法解决纠纷的。\x02\x03",

            "#00003F所以，希望持有车票的二位\x01",
            "能接受我的简单询问。\x02\x03",

            "#00001F你们前往目的地的理由是什么？\x01",
            "至少可以回答我\x01",
            "这个问题吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0317
    ChrTalk(
        0xC,
        "前、前往目的地的理由？\x02",
    )

    CloseMessageWindow()

    #C0318
    ChrTalk(
        0x9,
        (
            "哼，这种问题能\x01",
            "证明我的清白吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0319
    ChrTalk(
        0x101,
        (
            "#00000F是的，假如车票是偷来的，\x01",
            "那车票上的目的地\x01",
            "就有可能并不是犯人想去的地方。\x02\x03",

            "#00004F在这种情况下，\x01",
            "犯人说不定会露出什么破绽。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8B4D")

    #C0320
    ChrTalk(
        0x102,
        (
            "#00105F原来如此，\x01",
            "确实有这种可能性呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8C4C")

    label("loc_8B4D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8B8E")

    #C0321
    ChrTalk(
        0x103,
        (
            "#00203F原来如此，\x01",
            "确实有这种可能性呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8C4C")

    label("loc_8B8E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8BCF")

    #C0322
    ChrTalk(
        0x104,
        (
            "#00305F原来如此，\x01",
            "确实有这种可能性呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8C4C")

    label("loc_8BCF")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8C10")

    #C0323
    ChrTalk(
        0x109,
        (
            "#10105F原来如此，\x01",
            "确实有那种可能性呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8C4C")

    label("loc_8C10")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8C4C")

    #C0324
    ChrTalk(
        0x105,
        (
            "#10302F原来如此，\x01",
            "确实有那种可能性呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8C4C")


    #C0325
    ChrTalk(
        0x8,
        (
            "嗯，那就事不宜迟。\x01",
            "好了，赶快回答吧！\x02",
        )
    )

    CloseMessageWindow()

    #C0326
    ChrTalk(
        0x9,
        "哼，这种小问题自然无妨。\x02",
    )

    CloseMessageWindow()

    #C0327
    ChrTalk(
        0x9,
        (
            "我是个商人，\x01",
            "要去奥雷德签订一份\x01",
            "重要的合同。\x02",
        )
    )

    CloseMessageWindow()

    #C0328
    ChrTalk(
        0x9,
        (
            "请看，这就是合同。\x01",
            "交易对象是位于奥雷德自治州的\x01",
            "『流星商会』。\x02",
        )
    )

    CloseMessageWindow()

    #C0329
    ChrTalk(
        0x9,
        (
            "像我这样的人会偷车票，\x01",
            "简直就是开玩笑吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0330
    ChrTalk(
        0x8,
        "唔、唔唔唔……\x02",
    )

    CloseMessageWindow()

    #C0331
    ChrTalk(
        0x101,
        (
            "#00003F……原来如此。\x02\x03",

            "#00001F那么，你呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0332
    ChrTalk(
        0xC,
        (
            "哎，这个……我的故乡\x01",
            "就是奥雷德自治州。\x02",
        )
    )

    CloseMessageWindow()

    #C0333
    ChrTalk(
        0xC,
        "……回老家是不是不能算理由？\x02",
    )

    CloseMessageWindow()

    #C0334
    ChrTalk(
        0x101,
        (
            "#00003F哪里，没有的事……\x02\x03",

            "#00008F（唔～光凭这些线索，\x01",
            "  实在是无法做出判断啊。）\x02",
        )
    )

    CloseMessageWindow()
    Return()

    # Function_32_8024 end

    def Function_33_8E25(): pass

    label("Function_33_8E25")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8E74")

    #C0335
    ChrTalk(
        0x102,
        (
            "#00103F（……看样子，我们能做的\x01",
            "  也只有这么多了。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8FA5")

    label("loc_8E74")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8EC1")

    #C0336
    ChrTalk(
        0x103,
        (
            "#00203F（……看样子，我们能做的\x01",
            "  也只有这些了。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8FA5")

    label("loc_8EC1")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8F0E")

    #C0337
    ChrTalk(
        0x104,
        (
            "#00303F（……看样子，我们能做的\x01",
            "  也只有这些啦。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8FA5")

    label("loc_8F0E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8F5B")

    #C0338
    ChrTalk(
        0x109,
        (
            "#10103F（……看样子，我们能做的\x01",
            "  也只有这些了。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8FA5")

    label("loc_8F5B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8FA5")

    #C0339
    ChrTalk(
        0x105,
        (
            "#10303F（……看样子，我们能做的\x01",
            "  也只有这些了啊。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8FA5")


    #C0340
    ChrTalk(
        0x101,
        (
            "#00003F（是啊……\x01",
            "  接下来，也只能去向\x01",
            "  正式安检官马洛先生报告了。）\x02\x03",

            "#00000F那个……请各位在这里\x01",
            "稍等片刻，\x02\x03",

            "我们现在就去把上级叫来。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x22, 3)
    NewScene("c0800", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_33_8E25 end

    def Function_34_9059(): pass

    label("Function_34_9059")

    Sleep(1000)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    OP_4B(0x10, 0x0)
    SetChrPos(0x10, 460, 0, 9210, 180)
    SetChrPos(0xF, -480, 0, 9860, 180)
    OP_A7(0x10, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xF, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    Sound(100, 0, 100, 0)
    OP_71(0x2, 0x0, 0x5, 0x1, 0x8)
    Sleep(1000)

    #C0341
    ChrTalk(
        0x10,
        (
            "哈哈，有意思。\x01",
            "这节车厢里有个骗子啊！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_910E():
        OP_93(0x0, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_910E)

    def lambda_911B():
        OP_93(0x1, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_911B)
    OP_68(460, 1000, 5040, 3000)
    MoveCamera(315, 25, 0, 3000)
    OP_6E(500, 3000)
    SetCameraDistance(16210, 3000)

    def lambda_9156():
        OP_95(0x10, 460, 0, 5470, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_9156)

    def lambda_9170():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_9170)

    def lambda_9181():
        OP_95(0xF, -480, 0, 5970, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_9181)

    def lambda_919B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF, 2, lambda_919B)
    Sleep(2000)
    Sound(100, 0, 100, 0)
    OP_71(0x2, 0x5, 0x0, 0x1, 0x8)
    OP_6F(0x79)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_92CA")

    #C0342
    ChrTalk(
        0x101,
        (
            "#00005F秦？\x02\x03",

            "#00001F等、等一下。\x01",
            "按照规定，在安检过程中\x01",
            "是不能移动到其它车厢的。\x02",
        )
    )

    CloseMessageWindow()

    #C0343
    ChrTalk(
        0x10,
        (
            "哼，安检工作已经\x01",
            "告一段落了吧？\x01",
            "这点小事就稍微通融一下吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0344
    ChrTalk(
        0x101,
        (
            "#00006F这……可是……\x01",
            "呼，算了。\x02",
        )
    )

    CloseMessageWindow()

    #C0345
    ChrTalk(
        0x10,
        (
            "看样子，事情的发展\x01",
            "似乎很有趣啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0346
    ChrTalk(
        0x10,
        "让我也加入好了！\x02",
    )

    CloseMessageWindow()
    Jump("loc_9318")

    label("loc_92CA")


    #C0347
    ChrTalk(
        0x101,
        "#00005F秦？\x02",
    )

    CloseMessageWindow()

    #C0348
    ChrTalk(
        0x10,
        (
            "呵呵，事情的发展\x01",
            "似乎很有趣啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0349
    ChrTalk(
        0x10,
        "让我也加入好了！\x02",
    )

    CloseMessageWindow()

    label("loc_9318")


    #C0350
    ChrTalk(
        0x101,
        "#00005F加、加入……\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    Fade(1000)
    OP_68(-470, 1000, 1440, 0)
    MoveCamera(307, 26, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17200, 0)
    SetChrPos(0x101, -550, 0, 1100, 90)
    SetChrPos(0x10, 540, 0, 1100, 180)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_93AF")
    SetChrPos(0x102, -540, 0, 2100, 135)
    Jump("loc_9442")

    label("loc_93AF")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_93D5")
    SetChrPos(0x103, -540, 0, 2100, 135)
    Jump("loc_9442")

    label("loc_93D5")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_93FB")
    SetChrPos(0x104, -540, 0, 2100, 135)
    Jump("loc_9442")

    label("loc_93FB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9421")
    SetChrPos(0x109, -540, 0, 2100, 135)
    Jump("loc_9442")

    label("loc_9421")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9442")
    SetChrPos(0x105, -540, 0, 2100, 135)

    label("loc_9442")

    SetChrPos(0xF, 540, 0, 2500, 180)
    OP_93(0x8, 0x5A, 0x0)
    OP_0D()

    #C0351
    ChrTalk(
        0x101,
        (
            "#00001F……那个，你刚才说的骗子\x01",
            "究竟是指谁呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0352
    ChrTalk(
        0x10,
        (
            "哦，首先还得请\x01",
            "那位商人来回答我的问题。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_94C1():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_94C1)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_94EB")

    def lambda_94DE():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_94DE)
    Jump("loc_956E")

    label("loc_94EB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_950D")

    def lambda_9500():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_9500)
    Jump("loc_956E")

    label("loc_950D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_952F")

    def lambda_9522():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_9522)
    Jump("loc_956E")

    label("loc_952F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9551")

    def lambda_9544():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_9544)
    Jump("loc_956E")

    label("loc_9551")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_956E")

    def lambda_9566():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_9566)

    label("loc_956E")


    #C0353
    ChrTalk(
        0x10,
        (
            "要和『流星商会』做交易，\x01",
            "你刚才是这么说的吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0354
    ChrTalk(
        0x10,
        "交易的具体内容是什么？\x02",
    )

    CloseMessageWindow()

    #C0355
    ChrTalk(
        0x9,
        (
            "呼，我为什么要陪\x01",
            "这种小孩子做游戏……\x02",
        )
    )

    CloseMessageWindow()

    #C0356
    ChrTalk(
        0x9,
        (
            "告诉你也没关系，\x01",
            "我要去采购奥雷德自治州\x01",
            "出产的稀有蔬菜和香料。\x02",
        )
    )

    CloseMessageWindow()

    #C0357
    ChrTalk(
        0x9,
        "说起奥雷德，那可是个以农业而闻名的地方。\x02",
    )

    CloseMessageWindow()

    #C0358
    ChrTalk(
        0x9,
        (
            "而『流星商会』正是\x01",
            "控制着共和国东方人街的\x01",
            "组织——『黑月』的关联公司。\x02",
        )
    )

    CloseMessageWindow()

    #C0359
    ChrTalk(
        0x9,
        "……如何？已经没有怀疑余地了吧？\x02",
    )

    CloseMessageWindow()

    #C0360
    ChrTalk(
        0x10,
        (
            "呵呵，正如你所说，\x01",
            "奥雷德自治州确实有个『流星商会』。\x02",
        )
    )

    CloseMessageWindow()

    #C0361
    ChrTalk(
        0x10,
        (
            "但不巧得很，\x01",
            "『流星商会』正在巩固\x01",
            "自己在自治州内的立足点。\x02",
        )
    )

    CloseMessageWindow()

    #C0362
    ChrTalk(
        0x10,
        (
            "还没有发展到\x01",
            "和外部人士\x01",
            "交易的阶段哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0363
    ChrTalk(
        0x9,
        (
            "什么？\x01",
            "你为什么会知道那种事情？\x02",
        )
    )

    CloseMessageWindow()

    #C0364
    ChrTalk(
        0x10,
        "这个嘛……还是你来告诉他好了。\x02",
    )

    CloseMessageWindow()
    StopBGM(0xBB8)

    #C0365
    ChrTalk(
        0xF,
        "嗯，交给我吧。\x02",
    )

    CloseMessageWindow()

    #C0366
    ChrTalk(
        0xF,
        (
            "你这混蛋，我从刚才开始\x01",
            "就一直在忍耐了！\x01",
            "你竟敢对小少爷如此无礼！\x02",
        )
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7114", 0)
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    #C0367
    ChrTalk(
        0xF,
        (
            "#5S你给我老实一点！\x01",
            "这位可是『黑月』长老的\x01",
            "孙子秦少爷！#3S\x02",
        )
    )

    CloseMessageWindow()

    #C0368
    ChrTalk(
        0x9,
        "长老的孙子～？开玩笑吧……\x02",
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0369
    ChrTalk(
        0x9,
        (
            "你、你穿的那套衣服……\x01",
            "我好像确实曾在哪里见过。\x02",
        )
    )

    CloseMessageWindow()

    #C0370
    ChrTalk(
        0x9,
        "怎、怎么会……难道真的是……\x02",
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x9)

    #C0371
    ChrTalk(
        0x10,
        "呵呵，看来你总算是明白了。\x02",
    )

    CloseMessageWindow()

    #C0372
    ChrTalk(
        0x10,
        "顺便问一下，你真正的目的是什么？\x02",
    )

    CloseMessageWindow()

    #C0373
    ChrTalk(
        0x9,
        "这、这个……\x02",
    )

    CloseMessageWindow()

    #C0374
    ChrTalk(
        0x10,
        (
            "哼，算了。\x01",
            "你稍后就去办公室\x01",
            "向安检官坦白一切吧。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_99FB")

    #C0375
    ChrTalk(
        0x102,
        "#00103F（……秦……干得好啊。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_9AEC")

    label("loc_99FB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9A39")

    #C0376
    ChrTalk(
        0x103,
        "#00203F（……这孩子……很厉害呢。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_9AEC")

    label("loc_9A39")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9A77")

    #C0377
    ChrTalk(
        0x104,
        "#00303F（……秦这家伙，很能干啊。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_9AEC")

    label("loc_9A77")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9AAF")

    #C0378
    ChrTalk(
        0x109,
        "#10105F（……好厉害啊，秦。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_9AEC")

    label("loc_9AAF")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9AEC")

    #C0379
    ChrTalk(
        0x105,
        "#10304F（呵呵，真是个了不起的孩子啊。）\x02",
    )

    CloseMessageWindow()

    label("loc_9AEC")


    #C0380
    ChrTalk(
        0x101,
        (
            "#00003F（嗯，该怎么说呢，\x01",
            "  真是威严十足啊。）\x02",
        )
    )

    CloseMessageWindow()

    #C0381
    ChrTalk(
        0x10,
        "好了，下一个是你。\x02",
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0382
    ChrTalk(
        0x101,
        "#00005F秦……？\x02",
    )

    CloseMessageWindow()

    #C0383
    ChrTalk(
        0xC,
        "我、我吗？\x02",
    )

    CloseMessageWindow()

    #C0384
    ChrTalk(
        0xC,
        (
            "犯人不就是那个\x01",
            "说谎的男人吗……\x02",
        )
    )

    CloseMessageWindow()

    #C0385
    ChrTalk(
        0x10,
        "哼，谁说过那种话了？\x02",
    )

    CloseMessageWindow()

    #C0386
    ChrTalk(
        0x10,
        (
            "你也要回答几个问题，\x01",
            "你是出身于\x01",
            "奥雷德自治州的吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0387
    ChrTalk(
        0xC,
        (
            "是、是的……\x01",
            "我这次是想回故乡……\x02",
        )
    )

    CloseMessageWindow()

    #C0388
    ChrTalk(
        0x10,
        "嗯，既然如此，这个问题你肯定能答上来。\x02",
    )

    CloseMessageWindow()

    #C0389
    ChrTalk(
        0x10,
        (
            "奥雷德自治州不仅农业发达，\x01",
            "还是个以自然秘境而闻名的地方。\x02",
        )
    )

    CloseMessageWindow()

    #C0390
    ChrTalk(
        0x10,
        (
            "自治州内遍布着很多温泉……\x01",
            "请问以下三个温泉，哪个位于奥雷德自治州？\x02",
        )
    )

    CloseMessageWindow()

    #C0391
    ChrTalk(
        0x10,
        (
            "一，艾尔摩温泉\x01",
            "二，帕鲁姆温泉\x01",
            "三，奥雷德温泉。\x02",
        )
    )

    CloseMessageWindow()

    #C0392
    ChrTalk(
        0x10,
        "好了，快回答。\x02",
    )

    CloseMessageWindow()

    #C0393
    ChrTalk(
        0xC,
        "啊……？\x02",
    )

    CloseMessageWindow()

    #C0394
    ChrTalk(
        0xC,
        (
            "这、这个……\x01",
            "那、那当然是三——\x01",
            "奥雷德温泉嘛。\x02",
        )
    )

    CloseMessageWindow()

    #C0395
    ChrTalk(
        0x10,
        (
            "……是吗。\x01",
            "呵呵……哈哈哈哈。\x02",
        )
    )

    CloseMessageWindow()

    #C0396
    ChrTalk(
        0x101,
        "#00005F怎、怎么回事？\x02",
    )

    CloseMessageWindow()

    #C0397
    ChrTalk(
        0x10,
        (
            "你觉得我只是个小孩子，\x01",
            "所以就小看我吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0398
    ChrTalk(
        0x10,
        "奥雷德温泉～？\x02",
    )

    CloseMessageWindow()

    #C0399
    ChrTalk(
        0x10,
        (
            "这么老套的陷阱也能让你上当啊，\x01",
            "其实根本就没有以自治州的名字\x01",
            "命名的温泉。\x02",
        )
    )

    CloseMessageWindow()

    #C0400
    ChrTalk(
        0x10,
        (
            "如果你真的是奥雷德自治州的人，\x01",
            "就应该这么回答——\x01",
            "『其中没有正确答案』。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0401
    ChrTalk(
        0xC,
        "哎……\x02",
    )

    CloseMessageWindow()

    #C0402
    ChrTalk(
        0x10,
        (
            "哼哼，还要我继续\x01",
            "提出问题吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0403
    ChrTalk(
        0x10,
        (
            "那样的话，你只会\x01",
            "露出更多的马脚哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0404
    ChrTalk(
        0x10,
        "好了，你真正的老家是哪里？\x02",
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xC)

    #C0405
    ChrTalk(
        0xC,
        "哎，那、那个……\x02",
    )

    CloseMessageWindow()

    #C0406
    ChrTalk(
        0xC,
        (
            "我只是觉得没有必要\x01",
            "特意说明而已，\x01",
            "其实我的老家是共和国。\x02",
        )
    )

    CloseMessageWindow()

    #C0407
    ChrTalk(
        0xC,
        (
            "但我现在的家真的在奥雷德……\x01",
            "请、请相信我！\x02",
        )
    )

    CloseMessageWindow()

    #C0408
    ChrTalk(
        0x10,
        "哼，是吗。\x02",
    )

    CloseMessageWindow()
    StopBGM(0xBB8)
    TurnDirection(0x10, 0x101, 500)

    #C0409
    ChrTalk(
        0x10,
        (
            "那么，\x01",
            "特别任务支援科的二位怎么想？\x02",
        )
    )

    CloseMessageWindow()

    #C0410
    ChrTalk(
        0x10,
        (
            "具体内容暂且不说，现在至少可以\x01",
            "确定他们两个人都在说谎……\x02",
        )
    )

    CloseMessageWindow()

    #C0411
    ChrTalk(
        0x10,
        "偷票的小偷究竟是谁呢？\x02",
    )

    CloseMessageWindow()

    #C0412
    ChrTalk(
        0x101,
        "#00003F啊……嗯……这个嘛……\x02",
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7111", 0)
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    #A0413
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1K商人与青年，谁更有可能\x01",
            "是偷票的小偷呢？\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "商人\x01",      # 0
            "青年\x01",      # 1
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
        (0, "loc_A135"),
        (1, "loc_A31D"),
        (SWITCH_DEFAULT, "loc_A44D"),
    )


    label("loc_A135")

    OP_2C(0x79, 0x1)

    #C0414
    ChrTalk(
        0x101,
        (
            "#00003F应该是商人吧？\x02\x03",

            "#00000F他好像隐瞒了\x01",
            "不少事情……\x02",
        )
    )

    CloseMessageWindow()

    #C0415
    ChrTalk(
        0x10,
        (
            "喂，我说你……\x01",
            "不要让我失望啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0416
    ChrTalk(
        0x10,
        "你真的用心思考过吗？\x02",
    )

    CloseMessageWindow()

    #C0417
    ChrTalk(
        0x101,
        (
            "#00006F啊、啊啊……抱歉。\x02\x03",

            "#00008F……对了，在这种情况下，\x01",
            "应该用排除法来思考。\x02\x03",

            "#00001F商人向我们出示了\x01",
            "虚假的合同……\x02\x03",

            "虽然不清楚他的具体目的，\x01",
            "但特意准备了这种东西，\x01",
            "显然是有备而来。\x02\x03",

            "#00003F既然做了如此周到的准备，\x01",
            "再去做偷票这种小勾当\x01",
            "就很奇怪了。\x02\x03",

            "因为旅途中\x01",
            "随时可以下车，\x01",
            "所以犯人不一定是要去奥雷德……\x02\x03",

            "#00001F也就是说……\x01",
            "犯人其实是你吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A44D")

    label("loc_A31D")

    OP_2C(0x79, 0x2)

    #C0418
    ChrTalk(
        0x101,
        (
            "#00003F是这位青年。\x02\x03",

            "#00001F商人向我们出示了\x01",
            "虚假的合同……\x02\x03",

            "虽然不清楚他的具体目的，\x01",
            "但特意准备了这种东西，\x01",
            "显然是有备而来。\x02\x03",

            "#00003F既然做了如此周到的准备，\x01",
            "再去做偷票这种小勾当\x01",
            "就很奇怪了。\x02\x03",

            "因为旅途中\x01",
            "随时可以下车，\x01",
            "所以犯人不一定是要去奥雷德……\x02\x03",

            "#00001F也就是说……\x01",
            "犯人其实是你吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A44D")

    label("loc_A44D")


    #C0419
    ChrTalk(
        0xC,
        "呜、呜呜呜……\x02",
    )

    CloseMessageWindow()

    #C0420
    ChrTalk(
        0x10,
        "嗯，算是合格吧。\x02",
    )

    CloseMessageWindow()
    OP_93(0x10, 0xB4, 0x1F4)

    #C0421
    ChrTalk(
        0x10,
        (
            "喂，你就算继续\x01",
            "嘴硬下去，\x01",
            "也无法隐瞒事实了。\x02",
        )
    )

    CloseMessageWindow()

    #C0422
    ChrTalk(
        0x10,
        (
            "如果是个男人，\x01",
            "就趁现在赶快坦白吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0423
    ChrTalk(
        0xC,
        "#5S请、请放过我吧！#3S\x02",
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_A593():
        TurnDirection(0xFE, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_A593)
    Sleep(50)

    def lambda_A5A3():
        TurnDirection(0xFE, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_A5A3)
    Sleep(300)

    #C0424
    ChrTalk(
        0x8,
        "什、什么！\x02",
    )

    CloseMessageWindow()

    #C0425
    ChrTalk(
        0x10,
        "喂，你……\x02",
    )

    CloseMessageWindow()

    #C0426
    ChrTalk(
        0xC,
        (
            "我、我的妈妈被送到了\x01",
            "共和国的医院。\x02",
        )
    )

    CloseMessageWindow()

    #C0427
    ChrTalk(
        0xC,
        (
            "所以我无论如何也要\x01",
            "尽快赶往医院！\x02",
        )
    )

    CloseMessageWindow()

    #C0428
    ChrTalk(
        0x101,
        "#00006F这、这个……\x02",
    )

    CloseMessageWindow()

    #C0429
    ChrTalk(
        0x10,
        "你说得太过突然，我一时听不太明白。\x02",
    )

    CloseMessageWindow()

    #C0430
    ChrTalk(
        0x10,
        "总之，先把情况说清楚吧。\x02",
    )

    CloseMessageWindow()

    #C0431
    ChrTalk(
        0xC,
        "是、是的……\x02",
    )

    CloseMessageWindow()

    #C0432
    ChrTalk(
        0xC,
        (
            "其实我是个以考入乌尔斯拉\x01",
            "医科大学为目标的学生……\x01",
            "不过家境十分贫困……\x02",
        )
    )

    CloseMessageWindow()

    #C0433
    ChrTalk(
        0xC,
        (
            "妈妈倾尽一切，\x01",
            "把我送到了克洛斯贝尔……\x01",
            "我一边打工，一边学习。\x02",
        )
    )

    CloseMessageWindow()

    #C0434
    ChrTalk(
        0xC,
        (
            "就在不久前，\x01",
            "我突然接到了\x01",
            "妈妈病倒的消息……所以就……\x02",
        )
    )

    CloseMessageWindow()

    #C0435
    ChrTalk(
        0x10,
        (
            "你想去探望母亲，\x01",
            "但因为没钱，所以就偷了别人的车票。\x01",
            "是这样吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0436
    ChrTalk(
        0xC,
        (
            "是、是的……\x01",
            "这真的不是在说谎！\x02",
        )
    )

    CloseMessageWindow()

    #C0437
    ChrTalk(
        0xC,
        "如果再这么拖下去，我妈妈就……\x02",
    )

    CloseMessageWindow()

    #C0438
    ChrTalk(
        0x101,
        (
            "#00003F唔～就算是这样，\x01",
            "我们也不能对偷窃行为……\x02",
        )
    )

    CloseMessageWindow()

    #C0439
    ChrTalk(
        0x10,
        "好吧，费用就由我来出。\x02",
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xF, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_A8BA():
        TurnDirection(0xFE, 0x10, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A8BA)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A8E4")

    def lambda_A8D7():
        TurnDirection(0xFE, 0x10, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A8D7)
    Jump("loc_A967")

    label("loc_A8E4")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A906")

    def lambda_A8F9():
        TurnDirection(0xFE, 0x10, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_A8F9)
    Jump("loc_A967")

    label("loc_A906")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A928")

    def lambda_A91B():
        TurnDirection(0xFE, 0x10, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_A91B)
    Jump("loc_A967")

    label("loc_A928")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A94A")

    def lambda_A93D():
        TurnDirection(0xFE, 0x10, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_A93D)
    Jump("loc_A967")

    label("loc_A94A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A967")

    def lambda_A95F():
        TurnDirection(0xFE, 0x10, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_A95F)

    label("loc_A967")


    def lambda_A96C():
        TurnDirection(0xFE, 0x10, 500)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_A96C)
    Sleep(50)

    def lambda_A97C():
        TurnDirection(0xFE, 0x10, 500)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_A97C)
    Sleep(300)

    #C0440
    ChrTalk(
        0xC,
        "哎……？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A9BF")

    #C0441
    ChrTalk(
        0x102,
        "#00105F秦……？\x02",
    )

    CloseMessageWindow()
    Jump("loc_AA64")

    label("loc_A9BF")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A9EB")

    #C0442
    ChrTalk(
        0x103,
        "#00205F你这是……\x02",
    )

    CloseMessageWindow()
    Jump("loc_AA64")

    label("loc_A9EB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AA17")

    #C0443
    ChrTalk(
        0x104,
        "#00305F喂、喂……\x02",
    )

    CloseMessageWindow()
    Jump("loc_AA64")

    label("loc_AA17")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AA41")

    #C0444
    ChrTalk(
        0x109,
        "#10105F那个……\x02",
    )

    CloseMessageWindow()
    Jump("loc_AA64")

    label("loc_AA41")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AA64")

    #C0445
    ChrTalk(
        0x105,
        "#10305F哎……\x02",
    )

    CloseMessageWindow()

    label("loc_AA64")

    TurnDirection(0x10, 0x8, 500)

    #C0446
    ChrTalk(
        0x10,
        (
            "老人家，您的车票\x01",
            "就由我来偿还。\x02",
        )
    )

    CloseMessageWindow()

    #C0447
    ChrTalk(
        0x10,
        (
            "您能否网开一面，\x01",
            "就此放过他呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0448
    ChrTalk(
        0x8,
        (
            "算、算了，只要能把票还回来，\x01",
            "我也不想牵扯更多纠纷……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10, 0xC, 500)

    #C0449
    ChrTalk(
        0x10,
        "还有，你。\x02",
    )

    CloseMessageWindow()

    #C0450
    ChrTalk(
        0xC,
        "是、是的……\x02",
    )

    CloseMessageWindow()

    #C0451
    ChrTalk(
        0x10,
        "难道你想靠偷来的车票去探望母亲吗？\x02",
    )

    CloseMessageWindow()

    #C0452
    ChrTalk(
        0x10,
        (
            "如果你母亲知道了，又会怎么想？\x01",
            "你认为她会高兴吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0453
    ChrTalk(
        0xC,
        "这、这个……\x02",
    )

    CloseMessageWindow()

    #C0454
    ChrTalk(
        0x10,
        (
            "听好，虽然这次我替你出钱，\x01",
            "但并不是赠送，\x01",
            "仅仅是暂借而已。\x02",
        )
    )

    CloseMessageWindow()

    #C0455
    ChrTalk(
        0x10,
        (
            "虽然还款时间并无限制，\x01",
            "但是你必须要还。\x02",
        )
    )

    CloseMessageWindow()

    #C0456
    ChrTalk(
        0xC,
        (
            "呜呜，对不起……\x01",
            "谢谢你。\x02",
        )
    )

    CloseMessageWindow()

    #C0457
    ChrTalk(
        0xC,
        "我一定会把钱还上的。\x02",
    )

    CloseMessageWindow()

    #C0458
    ChrTalk(
        0x10,
        "嗯，一言为定。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x10, 0x101, 500)

    #C0459
    ChrTalk(
        0x10,
        (
            "事情就是这样，\x01",
            "接下来，就去把安检官叫来吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0460
    ChrTalk(
        0x10,
        "由我来说明事情的经过。\x02",
    )

    CloseMessageWindow()

    #C0461
    ChrTalk(
        0x101,
        "#00005F啊……嗯……\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x22, 4)
    NewScene("c0800", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_34_9059 end

    def Function_35_ACD8(): pass

    label("Function_35_ACD8")

    EventBegin(0x1)
    SetScenarioFlags(0x156, 7)
    Call(0, 2)
    SetChrPos(0x0, 100, 0, -8640, 0)
    OP_68(100, 1000, -8640, 0)
    MoveCamera(315, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(20000, 0)
    EventEnd(0x4)
    Return()

    # Function_35_ACD8 end

    def Function_36_AD22(): pass

    label("Function_36_AD22")

    EventBegin(0x1)
    ClearScenarioFlags(0x156, 7)
    Call(0, 2)
    SetChrPos(0x0, 90, 0, 8340, 180)
    OP_68(90, 1000, 8340, 0)
    MoveCamera(315, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(20000, 0)
    EventEnd(0x4)
    Return()

    # Function_36_AD22 end

    def Function_37_AD6C(): pass

    label("Function_37_AD6C")

    SetChrPos(0xFE, -400, 0, -4300, 0)

    def lambda_AD82():
        OP_95(0xFE, -400, 0, 2700, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_AD82)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_37_AD6C end

    def Function_38_ADA3(): pass

    label("Function_38_ADA3")

    SetChrPos(0xFE, -400, 0, -5500, 0)
    Sleep(50)

    def lambda_ADBC():
        OP_95(0xFE, -400, 0, 1500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_ADBC)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x13B, 0x1F4)
    Return()

    # Function_38_ADA3 end

    def Function_39_ADDD(): pass

    label("Function_39_ADDD")

    SetChrPos(0xFE, 400, 0, -4600, 0)
    Sleep(50)

    def lambda_ADF6():
        OP_95(0xFE, 400, 0, 3900, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_ADF6)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_39_ADDD end

    def Function_40_AE17(): pass

    label("Function_40_AE17")

    SetChrPos(0xFE, 400, 0, -5600, 0)
    Sleep(100)

    def lambda_AE30():
        OP_95(0xFE, 400, 0, 2900, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_AE30)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_40_AE17 end

    def Function_41_AE51(): pass

    label("Function_41_AE51")

    SetChrPos(0xFE, 400, 0, -6600, 0)
    Sleep(50)

    def lambda_AE6A():
        OP_95(0xFE, 500, 0, 1500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_AE6A)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_41_AE51 end

    def Function_42_AE8B(): pass

    label("Function_42_AE8B")

    SetChrPos(0xFE, 400, 0, -7700, 0)
    Sleep(100)

    def lambda_AEA4():
        OP_95(0xFE, 400, 0, 400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_AEA4)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x13B, 0x1F4)
    Return()

    # Function_42_AE8B end

    def Function_43_AEC5(): pass

    label("Function_43_AEC5")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_7D(0xC8, 0xC8, 0xFF, 0x0, 0x0)
    LoadChrToIndex("chr/ch07302.itc", 0x1E)
    LoadChrToIndex("chr/ch12402.itc", 0x1F)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis236.itp")
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis237.itp")
    CreatePortrait(2, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu03400.itp")
    CreatePortrait(3, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu11500.itp")
    OP_68(-2000, 1000, 2550, 0)
    MoveCamera(315, 21, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(16500, 0)
    SetChrPos(0x101, 1400, 0, -7500, 315)
    SetChrPos(0x102, 1400, 0, -8500, 315)
    SetChrPos(0x103, 2300, 0, -8500, 315)
    SetChrPos(0x104, 2300, 0, -7500, 315)
    SetChrPos(0xF4, 3200, 0, -8500, 315)
    SetChrPos(0xF5, 3200, 0, -7500, 315)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrChipByIndex(0x27, 0x1E)
    SetChrSubChip(0x27, 0x0)
    ClearChrFlags(0x27, 0x80)
    SetChrFlags(0x27, 0x8000)
    SetChrPos(0x27, -2100, 150, 1800, 0)
    SetChrChipByIndex(0x28, 0x1F)
    SetChrSubChip(0x28, 0x0)
    ClearChrFlags(0x28, 0x80)
    SetChrFlags(0x28, 0x8000)
    SetChrPos(0x28, -2100, 150, 3300, 180)
    PlayBGM("ed7302", 0)
    SetCameraDistance(17000, 1500)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    SetChrSubChip(0x27, 0x2)
    Sleep(300)

    #C0462
    ChrTalk(
        0x27,
        "#5P#03402F你们来了啊。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x28, 0x1)

    #C0463
    ChrTalk(
        0x28,
        "#11P#11509F哟，好久不见啊。\x02",
    )

    CloseMessageWindow()
    OP_68(1000, 1000, -6000, 2000)
    MoveCamera(323, 21, 0, 2000)
    SetCameraDistance(18000, 2000)
    OP_6F(0x79)

    #C0464
    ChrTalk(
        0x101,
        "#6P#00006F……好久不见。\x02",
    )

    CloseMessageWindow()

    #C0465
    ChrTalk(
        0x103,
        (
            "#6P#00200F原来如此，是使用列车的通讯器\x01",
            "来和支援科车辆联络的啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0466
    ChrTalk(
        0x27,
        "#03404F#6P正是。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(-1470, 1000, 2540, 0)
    MoveCamera(306, 21, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(16650, 0)
    SetCameraDistance(16149, 3000)
    BeginChrThread(0x101, 3, 0, 37)
    BeginChrThread(0x102, 3, 0, 38)
    BeginChrThread(0x104, 3, 0, 39)
    BeginChrThread(0x103, 3, 0, 40)
    BeginChrThread(0xF4, 3, 0, 41)
    BeginChrThread(0xF5, 3, 0, 42)
    WaitChrThread(0xF5, 3)
    OP_6F(0x79)
    OP_CB(0x2, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x2, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    OP_CC(0x0, 0x2, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B2B4")

    #A0467
    AnonymousTalk(
        0x27,
        (
            "呵呵……仔细一看，\x01",
            "还真是强者云集啊。\x02\x03",

            "国防军最杰出的年轻少尉和星杯骑士团的\x01",
            "守护骑士竟然也和你们在一起。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B54B")

    label("loc_B2B4")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B33A")

    #A0468
    AnonymousTalk(
        0x27,
        (
            "呵呵……仔细一看，\x01",
            "还真是强者云集啊。\x02\x03",

            "国防军最杰出的年轻少尉和传说中的\x01",
            "刺客竟然也和你们在一起。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B54B")

    label("loc_B33A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B3C4")

    #A0469
    AnonymousTalk(
        0x27,
        (
            "呵呵……仔细一看，\x01",
            "还真是强者云集啊。\x02\x03",

            "国防军最杰出的年轻少尉和一科的\x01",
            "主任搜查官竟然也和你们在一起。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B54B")

    label("loc_B3C4")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B448")

    #A0470
    AnonymousTalk(
        0x27,
        (
            "呵呵……仔细一看，\x01",
            "还真是强者云集啊。\x02\x03",

            "星杯骑士团的守护骑士和传说中的\x01",
            "刺客竟然也和你们在一起。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B54B")

    label("loc_B448")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B4D0")

    #A0471
    AnonymousTalk(
        0x27,
        (
            "呵呵……仔细一看，\x01",
            "还真是强者云集啊。\x02\x03",

            "一科的主任搜查官和星杯骑士团的\x01",
            "守护骑士竟然也和你们在一起。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B54B")

    label("loc_B4D0")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B54B")

    #A0472
    AnonymousTalk(
        0x27,
        (
            "呵呵……仔细一看，\x01",
            "还真是强者云集啊。\x02\x03",

            "一科的主任搜查官和传说中的\x01",
            "刺客竟然也和你们在一起。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B54B")

    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x2, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x2, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    OP_CC(0x0, 0x2, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B5D0")

    #C0473
    ChrTalk(
        0x109,
        (
            "#6P#10103F……不好意思，我已经再次被\x01",
            "借调到了支援科。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B5D0")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B60D")

    #C0474
    ChrTalk(
        0x105,
        (
            "#6P#10402F你们果然掌握到了\x01",
            "我的身份啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B60D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B645")

    #C0475
    ChrTalk(
        0x106,
        "#6P#10701F………………………………\x02",
    )

    CloseMessageWindow()

    label("loc_B645")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B682")

    #C0476
    ChrTalk(
        0x10A,
        (
            "#6P#00603F哼……社交辞令\x01",
            "就到此为止吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B682")


    #C0477
    ChrTalk(
        0x102,
        (
            "#6P#00106F真没想到\x01",
            "你们还留在\x01",
            "克洛斯贝尔。\x02\x03",

            "#00101F自那次之后，你们一直都在市里？\x02",
        )
    )

    CloseMessageWindow()
    OP_CB(0x3, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x3, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x3, 0x3)
    OP_CC(0x0, 0x3, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0478
    AnonymousTalk(
        0x28,
        (
            "嗯，因为有很多事情\x01",
            "需要调查～\x02\x03",

            "不过，好像总算可以\x01",
            "回埃雷波尼亚了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x3, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x3, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    Sleep(300)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0xF4, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xF5, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    CreatePortrait(2, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis238.itp")
    CreatePortrait(3, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis291.itp")
    CreatePortrait(4, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis292.itp")

    #C0479
    ChrTalk(
        0x101,
        "#00011F#12P调查……？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BF, 3)), scpexpr(EXPR_END)), "loc_BA9A")

    #C0480
    ChrTalk(
        0x28,
        (
            "#11504F顺便一说，除了我们之外，\x01",
            "利贝尔的相关人员\x01",
            "也在行动……\x02\x03",

            "#11500F莫非你们已经知道了？\x02",
        )
    )

    CloseMessageWindow()

    #C0481
    ChrTalk(
        0x101,
        (
            "#00005F嗯……是Ｒ＆Ａ调查所的\x01",
            "雷因兹先生吧？\x02\x03",

            "#00001F难道你们与他有合作关系？\x02",
        )
    )

    CloseMessageWindow()

    #C0482
    ChrTalk(
        0x27,
        (
            "#03404F#5P嗯，在这次的事件中，\x01",
            "相互交换过一些情报。\x02\x03",

            "#03402F身为民间的调查公司，\x01",
            "他们拥有很优秀的情报网。\x02",
        )
    )

    CloseMessageWindow()

    #C0483
    ChrTalk(
        0x28,
        (
            "#11504F哈，但民间公司毕竟人手不足，\x01",
            "需要常年奔波在各地，\x01",
            "似乎很辛苦呢～\x02",
        )
    )

    CloseMessageWindow()

    #C0484
    ChrTalk(
        0x104,
        (
            "#00306F#12P那些事情暂且不提……\x02\x03",

            "#00301F听说『铁血宰相』遭到了枪击，\x01",
            "目前下落不明。\x02\x03",

            "你却在这种地方闲扯，没问题吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BB07")

    label("loc_BA9A")


    #C0485
    ChrTalk(
        0x104,
        (
            "#00306F#12P话说回来，听说『铁血宰相』遭到了枪击，\x01",
            "目前下落不明。\x02\x03",

            "#00301F你却在这种地方闲扯，没问题吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BB07")


    #C0486
    ChrTalk(
        0x28,
        (
            "#11505F哦……\x01",
            "你是说吉利亚斯大叔啊。\x02\x03",

            "#11506F我就算立刻赶回去，\x01",
            "也起不到什么作用了。\x02\x03",

            "#11510F而且，对那大叔而言，\x01",
            "无论是自己的遭遇，还是克洛斯贝尔的事态，\x01",
            "应该都处在事先预想的局面之内。\x02",
        )
    )

    CloseMessageWindow()
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
    OP_63(0xF4, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xF5, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0487
    ChrTalk(
        0x102,
        "#6P#00105F哎……！？\x02",
    )

    CloseMessageWindow()

    #C0488
    ChrTalk(
        0x101,
        (
            "#00007F#12P预想的局面……\x01",
            "莫非连自己会遭到枪击都……！？\x02",
        )
    )

    CloseMessageWindow()

    #C0489
    ChrTalk(
        0x103,
        (
            "#12P#00201F克洛斯贝尔的事态……\x01",
            "就是指这次的事件吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0490
    ChrTalk(
        0x28,
        (
            "#11501F对那个大叔来说，\x01",
            "一切都是游戏盘上的『棋子』。\x02\x03",

            "#11503F克洛斯贝尔取得至宝之后，\x01",
            "不仅会宣布独立，还会企图\x01",
            "支配整个大陆……\x02\x03",

            "贵族势力利用帝国军遭受反击的机会，\x01",
            "趁机占领帝都……\x02\x03",

            "#11508F其结果就是，由于自己遭到\x01",
            "枪击，身负重伤而濒死，\x01",
            "使帝国从此陷入内战……\x02\x03",

            "尽管如此，由于有克洛斯贝尔这道\x01",
            "坚不可摧的『壁障』阻隔在其中，\x01",
            "共和国也无法趁机发动侵攻。\x02\x03",

            "#11500F对那大叔来说，\x01",
            "这一切应该都是预料之中的发展。\x02",
        )
    )

    CloseMessageWindow()

    #C0491
    ChrTalk(
        0x101,
        "#00010F#12P……呜…………\x02",
    )

    CloseMessageWindow()

    #C0492
    ChrTalk(
        0x102,
        "#6P#00108F怎、怎么会……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_BEFE")

    #C0493
    ChrTalk(
        0x105,
        "#6P#10401F……真是个怪物呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_BF67")

    label("loc_BEFE")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_BF3B")

    #C0494
    ChrTalk(
        0x10A,
        "#6P#00610F竟然有那么可怕的怪物……\x02",
    )

    CloseMessageWindow()
    Jump("loc_BF67")

    label("loc_BF3B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_BF67")

    #C0495
    ChrTalk(
        0x106,
        "#6P#10703F……怪物……\x02",
    )

    CloseMessageWindow()

    label("loc_BF67")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_BF9C")

    #C0496
    ChrTalk(
        0x109,
        "#6P#10110F难、难以置信……\x02",
    )

    CloseMessageWindow()
    Jump("loc_C015")

    label("loc_BF9C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_BFDA")

    #C0497
    ChrTalk(
        0x106,
        (
            "#6P#10703F……真是有些\x01",
            "难以相信……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C015")

    label("loc_BFDA")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C015")

    #C0498
    ChrTalk(
        0x10A,
        (
            "#6P#00610F一时真是难以\x01",
            "彻底消化啊……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C015")


    #C0499
    ChrTalk(
        0x27,
        (
            "#03401F#5P『结社』似乎也在\x01",
            "帝国展开了行动……\x02\x03",

            "但真正可怕的\x01",
            "可能还是『铁血宰相』哦。\x02\x03",

            "#03403F把自己都当作『棋子』来利用，\x01",
            "从而造就出波涛汹涌的动荡时代……\x02\x03",

            "#03401F真不愧是一代人杰——不，该说是怪物才对。\x02",
        )
    )

    CloseMessageWindow()

    #C0500
    ChrTalk(
        0x101,
        "#00008F#12P…………………………………\x02",
    )

    CloseMessageWindow()

    #C0501
    ChrTalk(
        0x104,
        (
            "#00306F#12P早就知道他是个危险的大叔，\x01",
            "但没想到会可怕到这种程度……\x02",
        )
    )

    CloseMessageWindow()

    #C0502
    ChrTalk(
        0x102,
        (
            "#6P#00101F……迪塔总统\x01",
            "察觉到这一点了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0503
    ChrTalk(
        0x27,
        (
            "#03405F#5P那就不清楚了。\x02\x03",

            "#03403F这样说可能有些失礼……\x01",
            "迪塔·库罗伊斯这个人物，\x01",
            "演说的煽动性确实是超一流的。\x02\x03",

            "#03401F但是，作为一个政治家……\x01",
            "他的手腕就实在是让人抱有疑问了。\x02\x03",

            "从某种意义上说，他只会用商人的观点\x01",
            "来处理政治问题。\x02",
        )
    )

    CloseMessageWindow()

    #C0504
    ChrTalk(
        0x101,
        "#00005F#12P这……\x02",
    )

    CloseMessageWindow()

    #C0505
    ChrTalk(
        0x102,
        "#6P#00108F…………………………………\x02",
    )

    CloseMessageWindow()

    #C0506
    ChrTalk(
        0x27,
        (
            "#03404F#5P他骨子里毕竟\x01",
            "还是个银行家嘛。\x02\x03",

            "#03402F至于『库罗伊斯家族』的使命，\x01",
            "他好像也是全权交给女儿来负责的。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xF4, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xF5, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0507
    ChrTalk(
        0x103,
        "#12P#00205F这……\x02",
    )

    CloseMessageWindow()

    #C0508
    ChrTalk(
        0x101,
        "#00001F#12P……你们已经知道了啊。\x02",
    )

    CloseMessageWindow()

    #C0509
    ChrTalk(
        0x28,
        (
            "#11504F嗯，我们也有我们\x01",
            "的情报渠道。\x02\x03",

            "#11508F你们在那场竞拍会上\x01",
            "救出的那个小鬼头……\x02\x03",

            "#11501F化为『核心』，使『至宝』\x01",
            "诞生的事情经过，\x01",
            "我们也已经有了大体把握。\x02",
        )
    )

    CloseMessageWindow()

    #C0510
    ChrTalk(
        0x101,
        "#00003F#12P………………………………\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C51B")

    #C0511
    ChrTalk(
        0x105,
        (
            "#6P#10408F哎呀呀……\x01",
            "世俗势力竟然能\x01",
            "掌握到这种程度的机密。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C51B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C566")

    #C0512
    ChrTalk(
        0x10A,
        (
            "#6P#00603F真不愧是帝国军情报部\x01",
            "和洛克史密斯机关啊……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C566")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C58C")

    #C0513
    ChrTalk(
        0x109,
        "#6P#10101F唔……\x02",
    )

    CloseMessageWindow()

    label("loc_C58C")


    #C0514
    ChrTalk(
        0x27,
        (
            "#03400F#5P请不要误会……\x01",
            "我和他都只是\x01",
            "情报界的人员而已。\x02\x03",

            "以个人的立场来说，\x01",
            "对『至宝』从没有过\x01",
            "任何企图。\x02\x03",

            "#03403F不过，这场事件可以说是\x01",
            "使整个大陆陷入混乱的原因……\x02\x03",

            "#03401F我们只是想知道引发这场事件\x01",
            "的『真正幕后黑手』是谁而已。\x02",
        )
    )

    CloseMessageWindow()

    #C0515
    ChrTalk(
        0x101,
        "#00005F#12P……！？\x02",
    )

    CloseMessageWindow()

    #C0516
    ChrTalk(
        0x102,
        "#6P#00101F真正……幕后黑手！？\x02",
    )

    CloseMessageWindow()

    #C0517
    ChrTalk(
        0x27,
        (
            "#03404F#5P正如之前所说，\x01",
            "迪塔总统只是在商业\x01",
            "领域中很强大而已。\x02\x03",

            "玛丽亚贝尔小姐虽然深不可测，\x01",
            "但相比政治活动，主要还是\x01",
            "负责魔导技术方面的事项。\x02\x03",

            "#03400F至于『风之剑圣』……\x01",
            "如果说是幕后黑手，他未免也太过\x01",
            "自律与禁欲了。\x02",
        )
    )

    CloseMessageWindow()

    #C0518
    ChrTalk(
        0x28,
        (
            "#11501F吉利亚斯大叔也好，\x01",
            "『结社』也好……\x02\x03",

            "只是利用了克洛斯贝尔如今的状况，\x01",
            "或在利害一致的情况下提供了协助，\x01",
            "但都并非导致此次事件的主谋。\x02\x03",

            "#11503F幕后应该存在着一名真正的主谋。\x02\x03",

            "#11508F那个人对政治、经济、历史、国际形势……\x02\x03",

            "库罗伊斯家族、Ｄ∴Ｇ教团，\x01",
            "乃至『结社』的动向均有掌握。\x02\x03",

            "#11501F他掌控着各方面\x01",
            "的动向，最终造就了\x01",
            "如今的局面。\x02",
        )
    )

    CloseMessageWindow()

    #C0519
    ChrTalk(
        0x104,
        "#00306F#12P喂喂……真的假的？\x02",
    )

    CloseMessageWindow()

    #C0520
    ChrTalk(
        0x102,
        (
            "#6P#00108F虽然有些\x01",
            "阴谋论的感觉，但……\x02",
        )
    )

    CloseMessageWindow()

    #C0521
    ChrTalk(
        0x103,
        (
            "#12P#00203F的确……总觉得拼图中\x01",
            "还缺少一块碎片。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BE, 0)), scpexpr(EXPR_END)), "loc_CA8D")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(1000)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x0, 0x0, 0x0)
    Sleep(1000)
    OP_CB(0x2, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x0, 0x0, 0x0)
    Sleep(1000)
    OP_CB(0x3, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x3, 0x3)
    OP_CB(0x2, 0x3, 0xFFFFFF, 0x0, 0x0, 0x0)
    Sleep(1000)
    OP_CB(0x4, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x4, 0x3)
    OP_CB(0x3, 0x3, 0xFFFFFF, 0x0, 0x0, 0x0)
    Sleep(1000)
    OP_CB(0x4, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x4, 0x3)
    Sleep(300)

    #C0522
    ChrTalk(
        0x101,
        "#00013F#11P（………难道…………）\x02",
    )

    CloseMessageWindow()
    Jump("loc_CAEC")

    label("loc_CA8D")


    #C0523
    ChrTalk(
        0x101,
        "#00008F#11P（究竟会是谁……？）\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_CAEC")

    #C0524
    ChrTalk(
        0x10A,
        "#00608F#6P#30W（……难道……不……）\x02",
    )

    CloseMessageWindow()

    label("loc_CAEC")

    Sleep(500)

    #C0525
    ChrTalk(
        0x27,
        (
            "#03404F#5P算了，虽然之前还想过\x01",
            "能否在这个问题上取得进展……\x02\x03",

            "但看来你们也没有什么确凿证据，\x01",
            "就先这样吧。\x02\x03",

            "#03402F时间紧迫，现在就来说说\x01",
            "另一件事情吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0526
    ChrTalk(
        0x101,
        "#00005F#12P另一件事情……？\x02",
    )

    CloseMessageWindow()

    #C0527
    ChrTalk(
        0x28,
        (
            "#11504F嗯，很简单。\x02\x03",

            "#11507F我们准备参与\x01",
            "『攻占兰花塔作战』！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xF4, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xF5, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_82(0x32, 0x0, 0x7D0, 0xC8)

    #C0528
    ChrTalk(
        0x101,
        "#00011F#12P哎哎！？\x02",
    )

    CloseMessageWindow()

    #C0529
    ChrTalk(
        0x104,
        (
            "#00307F#12P喂喂，\x01",
            "这也太过突然了吧！？\x02",
        )
    )

    CloseMessageWindow()

    #C0530
    ChrTalk(
        0x27,
        (
            "#03404F#5P既然已经了解了事件概要，\x01",
            "本没有继续留在\x01",
            "克洛斯贝尔的必要了……\x02\x03",

            "但如果就这样一走了之，\x01",
            "多少会有些寝食难安呢。\x02\x03",

            "#03400F克洛斯贝尔今后会有怎样的发展，\x01",
            "还要看你们的努力……\x02\x03",

            "但如果长期陷入这种胶着状态，\x01",
            "我们也是很伤脑筋的。\x02",
        )
    )

    CloseMessageWindow()

    #C0531
    ChrTalk(
        0x28,
        (
            "#11504F在『波波碰！』即将过关的时候\x01",
            "突然放弃，感觉肯定会很不痛快。\x02\x03",

            "#11502F现在的情况也是一样。\x02",
        )
    )

    CloseMessageWindow()

    #C0532
    ChrTalk(
        0x102,
        "#6P#00109F就算你这么说……\x02",
    )

    CloseMessageWindow()

    #C0533
    ChrTalk(
        0x103,
        (
            "#12P#00211F……话说回来，\x01",
            "你是什么时候得到\x01",
            "『波波碰！』的账号的？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_CEEE")

    #C0534
    ChrTalk(
        0x105,
        (
            "#6P#10404F不管怎么说，如果战力增加，\x01",
            "作战的成功率也会提升呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CF9F")

    label("loc_CEEE")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_CF4A")

    #C0535
    ChrTalk(
        0x10A,
        (
            "#6P#00606F不管怎么说，如果战力增加，\x01",
            "作战成功率确实会有所提升……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CF9F")

    label("loc_CF4A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_CF9F")

    #C0536
    ChrTalk(
        0x106,
        (
            "#6P#10703F不管怎么说，如果战力增加，\x01",
            "作战的成功率应该也会提升。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CF9F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_CFF1")

    #C0537
    ChrTalk(
        0x109,
        (
            "#6P#10108F虽然心情有些复杂……\x01",
            "但我们还是考虑一下为好。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D07A")

    label("loc_CFF1")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D037")

    #C0538
    ChrTalk(
        0x106,
        (
            "#6P#10708F还是去和科长先生\x01",
            "商量一下为好呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D07A")

    label("loc_D037")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D07A")

    #C0539
    ChrTalk(
        0x10A,
        (
            "#6P#00601F还是去和赛尔盖长官\x01",
            "商谈一下为好啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D07A")


    #C0540
    ChrTalk(
        0x101,
        (
            "#00006F#12P……明白了。\x02\x03",

            "#00000F这就带二位去我们的据点，\x01",
            "请跟我们来。\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(16650, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    StopBGM(0xFA0)
    WaitBGM()
    SetChrName("")

    #A0541
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "之后，罗伊德等人向赛尔盖科长\x01",
            "介绍了雾香和雷克特……\x02\x03",

            "双方交换情报之后，\x01",
            "决定联手作战。\x02\x03",

            "随后，罗伯兹主任\x01",
            "向兰花塔发起的\x01",
            "网络入侵获得成功……\x02\x03",

            "『攻占兰花塔作战』\x01",
            "随即开始。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CC(0x1, 0xFF, 0x0)
    SetScenarioFlags(0x22, 2)
    NewScene("c1100", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_43_AEC5 end

    def Function_44_D1AC(): pass

    label("Function_44_D1AC")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    SetChrChipByIndex(0x15, 0x4)
    SetChrSubChip(0x15, 0x0)
    EndChrThread(0x15, 0x0)
    SetChrBattleFlags(0x15, 0x4)
    SetChrPos(0x15, -1900, 150, 3200, 180)
    SetChrSubChip(0x15, 0x1)
    SetChrChipByIndex(0x16, 0x6)
    SetChrSubChip(0x16, 0x0)
    EndChrThread(0x16, 0x0)
    SetChrBattleFlags(0x16, 0x4)
    SetChrPos(0x16, -1900, 150, 1700, 0)
    SetChrSubChip(0x16, 0x2)
    SetChrChipByIndex(0x17, 0x0)
    SetChrSubChip(0x17, 0x0)
    EndChrThread(0x17, 0x0)
    SetChrBattleFlags(0x17, 0x4)
    SetChrPos(0x17, -2230, 150, -3170, 0)
    SetChrChipByIndex(0x18, 0xA)
    SetChrSubChip(0x18, 0x0)
    EndChrThread(0x18, 0x0)
    SetChrBattleFlags(0x18, 0x4)
    SetChrPos(0x18, 2240, 150, -1750, 180)
    SetChrChipByIndex(0x19, 0x1)
    SetChrSubChip(0x19, 0x0)
    EndChrThread(0x19, 0x0)
    SetChrBattleFlags(0x19, 0x4)
    SetChrPos(0x19, 2200, 150, 5740, 180)
    LoadChrToIndex("chr/ch24100.itc", 0x1E)
    SetMapObjFlags(0x3, 0x4)
    ClearMapObjFlags(0x3, 0x2)
    OP_68(-110, 1000, 2300, 0)
    MoveCamera(315, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(16290, 0)
    SetChrPos(0x101, -420, 0, -6700, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D2FA")
    SetChrPos(0x102, 280, 0, -7500, 0)
    Jump("loc_D38D")

    label("loc_D2FA")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D320")
    SetChrPos(0x103, 280, 0, -7500, 0)
    Jump("loc_D38D")

    label("loc_D320")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D346")
    SetChrPos(0x104, 280, 0, -7500, 0)
    Jump("loc_D38D")

    label("loc_D346")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D36C")
    SetChrPos(0x109, 280, 0, -7500, 0)
    Jump("loc_D38D")

    label("loc_D36C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D38D")
    SetChrPos(0x105, 280, 0, -7500, 0)

    label("loc_D38D")

    SetChrPos(0x1A1, -90, 0, -8180, 0)
    SetChrChipByIndex(0x29, 0x1E)
    SetChrSubChip(0x29, 0x0)
    ClearChrFlags(0x29, 0x80)
    SetChrFlags(0x29, 0x8000)
    SetChrPos(0x29, -40, 0, -3180, 0)

    def lambda_D3C6():
        OP_95(0x29, -40, 0, 1990, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_D3C6)
    SoundLoad(450)
    Sound(450, 2, 100, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(1000)

    #C0542
    ChrTalk(
        0x15,
        (
            "你、你看啊，那个老婆婆……\x01",
            "是从上面跳下来的。\x02",
        )
    )

    CloseMessageWindow()

    #C0543
    ChrTalk(
        0x16,
        (
            "唔……\x01",
            "那个人究竟是干什么的啊？\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x29, 1)
    OP_63(0x29, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    OP_93(0x29, 0x10E, 0x1F4)
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    #C0544
    ChrTalk(
        0x29,
        (
            "#5S吵死了！闭嘴！\x01",
            "不要大惊小怪的！！#3S\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0x16, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x15)
    OP_64(0x16)

    #C0545
    ChrTalk(
        0x16,
        "哇哇！？\x02",
    )

    CloseMessageWindow()

    #C0546
    ChrTalk(
        0x15,
        "好、好可怕……！\x02",
    )

    CloseMessageWindow()

    #C0547
    ChrTalk(
        0x101,
        "#00007F在这里！！\x02",
    )

    CloseMessageWindow()
    OP_63(0x29, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_68(-290, 1000, 500, 2000)
    MoveCamera(315, 25, 0, 2000)
    OP_6E(500, 2000)
    SetCameraDistance(17960, 2000)
    OP_93(0x29, 0xB4, 0x1F4)

    def lambda_D56A():
        OP_95(0xFE, -420, 0, 150, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_D56A)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D5AE")

    def lambda_D594():
        OP_95(0xFE, 280, 0, -850, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_D594)
    Jump("loc_D665")

    label("loc_D5AE")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D5DD")

    def lambda_D5C3():
        OP_95(0xFE, 280, 0, -850, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_D5C3)
    Jump("loc_D665")

    label("loc_D5DD")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D60C")

    def lambda_D5F2():
        OP_95(0xFE, 280, 0, -850, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_D5F2)
    Jump("loc_D665")

    label("loc_D60C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D63B")

    def lambda_D621():
        OP_95(0xFE, 280, 0, -850, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_D621)
    Jump("loc_D665")

    label("loc_D63B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D665")

    def lambda_D650():
        OP_95(0xFE, 280, 0, -850, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_D650)

    label("loc_D665")


    def lambda_D66A():
        OP_95(0xFE, -90, 0, -1650, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x1A1, 1, lambda_D66A)
    WaitChrThread(0x1A1, 1)

    #C0548
    ChrTalk(
        0x29,
        "什么……！！\x02",
    )

    CloseMessageWindow()
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    #C0549
    ChrTalk(
        0x29,
        "#5S竟然如此纠缠不清！#3S\x02",
    )

    CloseMessageWindow()
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    #C0550
    ChrTalk(
        0x29,
        "#5S你们可真是不见棺材不落泪啊！#3S\x02",
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1A1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D7B9")

    #C0551
    ChrTalk(
        0x102,
        (
            "#00106F那应该是我们\x01",
            "要说的台词……\x02\x03",

            "#00101F……你已经无处可逃了，\x01",
            "请老老实实地投降吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D98A")

    label("loc_D7B9")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D822")

    #C0552
    ChrTalk(
        0x103,
        (
            "#00206F把这句话原封不动地\x01",
            "还给你。\x02\x03",

            "#00200F你已经无处可逃了……\x01",
            "请放弃抵抗吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D98A")

    label("loc_D822")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D890")

    #C0553
    ChrTalk(
        0x104,
        (
            "#00306F那应该是我们的台词啊。\x02\x03",

            "#00302F喂，你已经无处可逃了吧？\x01",
            "该到算总帐的时候了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D98A")

    label("loc_D890")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D910")

    #C0554
    ChrTalk(
        0x109,
        (
            "#10106F那、那好像是我们\x01",
            "该说的台词吧……\x02\x03",

            "#10101F……总之，\x01",
            "你已经不可能逃跑了。\x01",
            "请老老实实地投降吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D98A")

    label("loc_D910")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D98A")

    #C0555
    ChrTalk(
        0x105,
        (
            "#10306F哎呀呀，真是唯独不想\x01",
            "被你这样说啊，夫人。\x02\x03",

            "#10302F为了你自身考虑，\x01",
            "我认为还是老实投降为好……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D98A")


    #C0556
    ChrTalk(
        0x1A1,
        (
            "说、说的没错！\x01",
            "赶快放弃抵抗吧～！\x02",
        )
    )

    CloseMessageWindow()

    #C0557
    ChrTalk(
        0x29,
        (
            "哈……\x01",
            "我还以为你们想说什么，原来只是这些……\x02",
        )
    )

    CloseMessageWindow()

    #C0558
    ChrTalk(
        0x29,
        "你们给我记清楚！\x02",
    )

    CloseMessageWindow()

    #C0559
    ChrTalk(
        0x29,
        (
            "只要这个大陆还存在……\x01",
            "我就永远不会有\x01",
            "无处可逃的时候！\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x29, 0x0, 0x1F4)
    OP_95(0x29, 0, 0, 8290, 4000, 0x0)
    Sound(100, 0, 100, 0)
    ClearMapObjFlags(0x2, 0x10)
    OP_71(0x2, 0x0, 0x5, 0x1, 0x8)
    Sleep(200)

    def lambda_DA71():
        OP_95(0xFE, -10, 0, 10140, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_DA71)
    Sleep(200)

    def lambda_DA8E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x29, 2, lambda_DA8E)
    Sleep(1000)

    #C0560
    ChrTalk(
        0x101,
        (
            "#00006F可、可恶……\x01",
            "听不懂她在说什么……！\x02\x03",

            "#00007F总之，我们快追吧！\x02",
        )
    )

    CloseMessageWindow()

    #C0561
    ChrTalk(
        0x1A1,
        "站住～～～～～～！\x02",
    )

    CloseMessageWindow()

    def lambda_DB05():
        OP_95(0xFE, -420, 0, 10450, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_DB05)
    Sleep(100)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_DB4C")

    def lambda_DB32():
        OP_95(0xFE, 280, 0, 10250, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_DB32)
    Jump("loc_DC03")

    label("loc_DB4C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_DB7B")

    def lambda_DB61():
        OP_95(0xFE, 280, 0, 10250, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_DB61)
    Jump("loc_DC03")

    label("loc_DB7B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_DBAA")

    def lambda_DB90():
        OP_95(0xFE, 280, 0, 10250, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_DB90)
    Jump("loc_DC03")

    label("loc_DBAA")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_DBD9")

    def lambda_DBBF():
        OP_95(0xFE, 280, 0, 10250, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_DBBF)
    Jump("loc_DC03")

    label("loc_DBD9")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_DC03")

    def lambda_DBEE():
        OP_95(0xFE, 280, 0, 10250, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_DBEE)

    label("loc_DC03")

    Sleep(100)

    def lambda_DC0B():
        OP_95(0xFE, -90, 0, 10050, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x1A1, 1, lambda_DC0B)
    Sleep(500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_71(0x2, 0x0, 0x0, 0x1, 0x8)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x17, 0x80)
    SetChrFlags(0x18, 0x80)
    SetChrFlags(0x19, 0x80)
    LoadChrToIndex("chr/ch20400.itc", 0x1F)
    LoadChrToIndex("chr/ch20402.itc", 0x20)
    LoadChrToIndex("chr/ch22800.itc", 0x21)
    LoadChrToIndex("chr/ch22802.itc", 0x22)
    LoadChrToIndex("chr/ch24400.itc", 0x23)
    LoadChrToIndex("chr/ch24402.itc", 0x24)
    LoadChrToIndex("chr/ch12500.itc", 0x25)
    LoadChrToIndex("chr/ch12553.itc", 0x26)
    LoadChrToIndex("chr/ch31500.itc", 0x27)
    LoadChrToIndex("chr/ch31553.itc", 0x28)
    OP_68(-1580, 1000, 2240, 0)
    MoveCamera(310, 27, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(16290, 0)
    EndChrThread(0x0, 0x1)
    EndChrThread(0x1, 0x1)
    EndChrThread(0x1A1, 0x1)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x1A1, 0x80)
    OP_A7(0x0, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x1, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x1A1, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    SetChrPos(0x101, -230, 0, -4950, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_DD30")
    SetChrPos(0x102, 130, 0, -6140, 0)
    Jump("loc_DDC3")

    label("loc_DD30")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_DD56")
    SetChrPos(0x103, 130, 0, -6140, 0)
    Jump("loc_DDC3")

    label("loc_DD56")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_DD7C")
    SetChrPos(0x104, 130, 0, -6140, 0)
    Jump("loc_DDC3")

    label("loc_DD7C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_DDA2")
    SetChrPos(0x109, 130, 0, -6140, 0)
    Jump("loc_DDC3")

    label("loc_DDA2")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_DDC3")
    SetChrPos(0x105, 130, 0, -6140, 0)

    label("loc_DDC3")

    SetChrPos(0x1A1, -40, 0, -7350, 0)
    SetChrChipByIndex(0x2A, 0x20)
    SetChrSubChip(0x2A, 0x0)
    EndChrThread(0x2A, 0x0)
    SetChrBattleFlags(0x2A, 0x4)
    ClearChrFlags(0x2A, 0x80)
    SetChrFlags(0x2A, 0x8000)
    SetChrPos(0x2A, -2800, 150, 3210, 180)
    SetChrChipByIndex(0x2B, 0x22)
    SetChrSubChip(0x2B, 0x0)
    EndChrThread(0x2B, 0x0)
    SetChrBattleFlags(0x2B, 0x4)
    ClearChrFlags(0x2B, 0x80)
    SetChrFlags(0x2B, 0x8000)
    SetChrPos(0x2B, -1730, 150, 3210, 180)
    SetChrChipByIndex(0x2C, 0x24)
    SetChrSubChip(0x2C, 0x0)
    EndChrThread(0x2C, 0x0)
    SetChrBattleFlags(0x2C, 0x4)
    ClearChrFlags(0x2C, 0x80)
    SetChrFlags(0x2C, 0x8000)
    SetChrPos(0x2C, -2290, 150, 1730, 0)
    SetChrChipByIndex(0x2D, 0x25)
    ClearChrFlags(0x2D, 0x80)
    SetChrFlags(0x2D, 0x8000)
    SetChrPos(0x2D, 460, 0, 9210, 180)
    OP_A7(0x2D, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x2E, 0x27)
    ClearChrFlags(0x2E, 0x80)
    SetChrFlags(0x2E, 0x8000)
    SetChrPos(0x2E, -480, 0, 9860, 180)
    OP_A7(0x2E, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x29, 0x80)
    SetChrPos(0x29, -10, 0, -6170, 0)
    OP_A7(0x29, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    FadeToBright(1000, 0)
    OP_0D()

    #N0562
    NpcTalk(
        0x2A,
        "男人",
        (
            "列车已经发车了……\x01",
            "总算可以松一口气了啊。\x02",
        )
    )

    CloseMessageWindow()

    #N0563
    NpcTalk(
        0x2B,
        "男人",
        (
            "嗯……\x01",
            "要和克洛斯贝尔说再见了。\x02",
        )
    )

    CloseMessageWindow()

    #N0564
    NpcTalk(
        0x2B,
        "男人",
        (
            "老实说，真是对不住那些\x01",
            "被黑月捕获的同伴……\x02",
        )
    )

    CloseMessageWindow()

    #N0565
    NpcTalk(
        0x2C,
        "男人",
        (
            "没办法，这说明我们这次的\x01",
            "准备工作做得不够。\x02",
        )
    )

    CloseMessageWindow()

    #N0566
    NpcTalk(
        0x2C,
        "男人",
        (
            "总有一天，要将\x01",
            "那些家伙全部制裁……\x02",
        )
    )

    CloseMessageWindow()

    #N0567
    NpcTalk(
        0x2D,
        "男人的声音",
        (
            "哦……？你们聊的话题\x01",
            "好像很有趣啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x2A, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x2B, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x2C, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Sound(100, 0, 100, 0)
    OP_71(0x2, 0x0, 0x5, 0x1, 0x8)
    Sleep(500)

    def lambda_E06E():
        OP_95(0xFE, 30, 0, 1880, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x2D, 1, lambda_E06E)

    def lambda_E088():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2D, 2, lambda_E088)
    Sleep(600)

    def lambda_E09C():
        OP_95(0xFE, -110, 0, 2990, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x2E, 1, lambda_E09C)

    def lambda_E0B6():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2E, 2, lambda_E0B6)
    WaitChrThread(0x2D, 1)
    OP_93(0x2D, 0x10E, 0x12C)
    WaitChrThread(0x2E, 1)
    OP_93(0x2E, 0x10E, 0x1F4)
    SetChrSubChip(0x2A, 0x1)
    SetChrSubChip(0x2B, 0x1)
    SetChrSubChip(0x2C, 0x2)

    #N0568
    NpcTalk(
        0x2A,
        "男人",
        (
            "啊……啊啊……\x01",
            "你们是……\x02",
        )
    )

    CloseMessageWindow()

    #N0569
    NpcTalk(
        0x2B,
        "男人",
        "黑月……！？\x02",
    )

    CloseMessageWindow()

    #N0570
    NpcTalk(
        0x2C,
        "男人",
        (
            "可、可恶……\x01",
            "被追踪到了吗……！\x02",
        )
    )

    CloseMessageWindow()

    #C0571
    ChrTalk(
        0x2D,
        (
            "曹先生自然没理由\x01",
            "放过你们。\x02",
        )
    )

    CloseMessageWindow()

    #C0572
    ChrTalk(
        0x2D,
        (
            "反东方移民政策主义的各位……\x01",
            "请随我们一起来吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0573
    ChrTalk(
        0x2E,
        (
            "到达阿尔泰尔市之后，\x01",
            "我们就一起换乘\x01",
            "前往克洛斯贝尔的列车吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0574
    ChrTalk(
        0x2A,
        "万、万事皆休了吗……\x02",
    )

    CloseMessageWindow()

    #N0575
    NpcTalk(
        0x29,
        "老婆婆的声音",
        "小鬼，别挡道！\x02",
    )

    CloseMessageWindow()
    OP_63(0x2D, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x2E, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x2A, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x2B, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x2C, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    def lambda_E2A8():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2D, 1, lambda_E2A8)
    Sleep(50)

    def lambda_E2B8():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2E, 1, lambda_E2B8)

    #C0576
    ChrTalk(
        0x2D,
        "哎……\x02",
    )

    CloseMessageWindow()

    def lambda_E2D1():
        OP_95(0xFE, 10, 0, 2460, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_E2D1)
    Sleep(1850)
    Sound(811, 0, 100, 0)
    Sound(815, 0, 50, 0)
    Sound(833, 0, 20, 0)
    BeginChrThread(0x2D, 1, 0, 45)
    WaitChrThread(0x29, 1)
    Sound(811, 0, 100, 0)
    Sound(815, 0, 40, 0)
    BeginChrThread(0x2E, 1, 0, 46)
    WaitChrThread(0x2E, 1)

    #C0577
    ChrTalk(
        0x2D,
        "哇啊！\x02",
    )

    CloseMessageWindow()

    #C0578
    ChrTalk(
        0x2E,
        "呃呃！\x02",
    )

    CloseMessageWindow()

    #C0579
    ChrTalk(
        0x29,
        (
            "疼死了……\x01",
            "这两个蠢货，\x01",
            "我不是让你们闪开吗！？\x02",
        )
    )

    CloseMessageWindow()

    #C0580
    ChrTalk(
        0x29,
        (
            "我现在可不能止步在\x01",
            "这种地方！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x2A, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x2B, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x2C, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x2A)
    OP_64(0x2B)
    OP_64(0x2C)

    #C0581
    ChrTalk(
        0x2C,
        "（那、那个……）\x02",
    )

    CloseMessageWindow()

    #C0582
    ChrTalk(
        0x2A,
        "（这老婆婆是怎么回事啊？）\x02",
    )

    CloseMessageWindow()
    OP_63(0x29, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0x29, 0x10E, 0x1F4)

    #C0583
    ChrTalk(
        0x29,
        "……嗯～？\x02",
    )

    CloseMessageWindow()

    #C0584
    ChrTalk(
        0x29,
        (
            "你们几个，莫非……\x01",
            "正在被他们追赶吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0585
    ChrTalk(
        0x2B,
        (
            "啊，是的……\x01",
            "多亏您救了我们。\x02",
        )
    )

    CloseMessageWindow()

    #C0586
    ChrTalk(
        0x2C,
        "您是我们的恩人啊！\x02",
    )

    CloseMessageWindow()

    #C0587
    ChrTalk(
        0x29,
        "哼，虽然不清楚发生了什么事……\x02",
    )

    CloseMessageWindow()

    #C0588
    ChrTalk(
        0x29,
        (
            "……但为了对抗他们，\x01",
            "哪怕多一个同伴也是好的。\x02",
        )
    )

    CloseMessageWindow()
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    #C0589
    ChrTalk(
        0x29,
        (
            "#5S你们几个！\x01",
            "要是知道感恩的话，\x01",
            "就跟我一起来吧！#3S\x02",
        )
    )

    CloseMessageWindow()
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    #C0590
    ChrTalk(
        0x29,
        (
            "#5S如果一切顺利，\x01",
            "说不定你们也可以\x01",
            "顺利逃脱！#3S\x02",
        )
    )

    CloseMessageWindow()

    #C0591
    ChrTalk(
        0x2A,
        "哎、哎哎……！？\x02",
    )

    CloseMessageWindow()

    #C0592
    ChrTalk(
        0x2B,
        "真的吗……！？\x02",
    )

    CloseMessageWindow()

    #C0593
    ChrTalk(
        0x29,
        "好啦！别再磨磨蹭蹭的！\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("共和国恐怖分子")

    #A0594
    AnonymousTalk(
        0xFF,
        "知、知道了！！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_93(0x29, 0x0, 0x1F4)
    BeginChrThread(0x29, 1, 0, 47)
    Sleep(200)
    BeginChrThread(0x2B, 1, 0, 49)
    Sleep(600)
    BeginChrThread(0x2C, 1, 0, 50)
    Sleep(600)
    BeginChrThread(0x2A, 1, 0, 48)
    Sleep(3000)
    ClearChrFlags(0x0, 0x80)
    ClearChrFlags(0x1, 0x80)
    ClearChrFlags(0x1A1, 0x80)
    BeginChrThread(0x101, 1, 0, 47)
    Sleep(300)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E65A")
    BeginChrThread(0x102, 1, 0, 47)
    Jump("loc_E6C1")

    label("loc_E65A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E675")
    BeginChrThread(0x103, 1, 0, 47)
    Jump("loc_E6C1")

    label("loc_E675")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E690")
    BeginChrThread(0x104, 1, 0, 47)
    Jump("loc_E6C1")

    label("loc_E690")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E6AB")
    BeginChrThread(0x109, 1, 0, 47)
    Jump("loc_E6C1")

    label("loc_E6AB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E6C1")
    BeginChrThread(0x105, 1, 0, 47)

    label("loc_E6C1")

    Sleep(300)
    BeginChrThread(0x1A1, 1, 0, 47)
    Sleep(2000)

    #C0595
    ChrTalk(
        0x1A1,
        "#7A慢、慢着～！！\x02",
    )
    #Auto

    WaitChrThread(0x1A1, 1)
    OP_57(0x0)
    OP_5A()
    Sleep(700)

    #C0596
    ChrTalk(
        0x2E,
        "唔……\x02",
    )

    CloseMessageWindow()

    #C0597
    ChrTalk(
        0x2D,
        "究、究竟发生了什么事……\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrFlags(0x2D, 0x80)
    SetChrFlags(0x2E, 0x80)
    OP_71(0x2, 0x0, 0x0, 0x1, 0x8)
    OP_78(0x6, 0x14)
    SetChrPos(0x14, -1000, 0, 7800, 90)
    ClearMapObjFlags(0x6, 0x4)
    OP_78(0x3, 0x13)
    SetChrPos(0x13, 0, 0, 8800, 0)
    ClearMapObjFlags(0x3, 0x4)
    SetMapObjFlags(0x3, 0x2)
    OP_68(100, 1000, -6850, 0)
    MoveCamera(315, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(20000, 0)
    OP_A7(0x0, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x1, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x1A1, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    SetChrPos(0x101, -20, 0, -7440, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E7FA")
    SetChrPos(0x102, -650, 0, -8160, 0)
    Jump("loc_E88D")

    label("loc_E7FA")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E820")
    SetChrPos(0x103, -650, 0, -8160, 0)
    Jump("loc_E88D")

    label("loc_E820")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E846")
    SetChrPos(0x104, -650, 0, -8160, 0)
    Jump("loc_E88D")

    label("loc_E846")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E86C")
    SetChrPos(0x109, -650, 0, -8160, 0)
    Jump("loc_E88D")

    label("loc_E86C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E88D")
    SetChrPos(0x105, -650, 0, -8160, 0)

    label("loc_E88D")

    SetChrPos(0x1A1, 550, 0, -8490, 0)
    SetChrFlags(0x29, 0x80)
    SetChrFlags(0x2A, 0x80)
    SetChrFlags(0x2B, 0x80)
    SetChrFlags(0x2C, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    SetChrChipByIndex(0x15, 0x6)
    SetChrSubChip(0x15, 0x0)
    EndChrThread(0x15, 0x0)
    SetChrBattleFlags(0x15, 0x4)
    SetChrPos(0x15, 2210, 150, -3270, 0)
    SetChrChipByIndex(0x16, 0x5)
    SetChrSubChip(0x16, 0x0)
    EndChrThread(0x16, 0x0)
    SetChrBattleFlags(0x16, 0x4)
    SetChrPos(0x16, 2210, 150, -1710, 180)
    SetChrChipByIndex(0x17, 0x0)
    SetChrSubChip(0x17, 0x0)
    EndChrThread(0x17, 0x0)
    SetChrBattleFlags(0x17, 0x4)
    SetChrPos(0x17, -2240, 0, -750, 0)
    SetChrChipByIndex(0x18, 0xA)
    SetChrSubChip(0x18, 0x0)
    EndChrThread(0x18, 0x0)
    SetChrBattleFlags(0x18, 0x4)
    SetChrPos(0x18, -2240, 0, 3210, 180)
    SetChrChipByIndex(0x19, 0x9)
    SetChrSubChip(0x19, 0x0)
    EndChrThread(0x19, 0x0)
    SetChrBattleFlags(0x19, 0x4)
    SetChrPos(0x19, 2340, 0, 5690, 180)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)
    OP_68(-1640, 1000, 8480, 3000)
    MoveCamera(315, 25, 0, 3000)
    OP_6E(500, 3000)
    SetCameraDistance(20000, 3000)
    OP_6F(0x79)
    Sleep(1000)
    Fade(500)
    OP_68(20, 1000, -6050, 0)
    MoveCamera(315, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(16210, 0)
    OP_0D()

    #C0598
    ChrTalk(
        0x1A1,
        "呼、呼……\x02",
    )

    CloseMessageWindow()

    #C0599
    ChrTalk(
        0x1A1,
        (
            "好、好像又爬到\x01",
            "车顶去了啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0600
    ChrTalk(
        0x101,
        (
            "#00003F而且好像\x01",
            "还带着什么人\x01",
            "一起上去了……\x02\x03",

            "#00001F莫非有同伴\x01",
            "潜伏在车内吗！？\x02",
        )
    )

    CloseMessageWindow()

    #C0601
    ChrTalk(
        0x1A1,
        (
            "不、不可能吧……\x01",
            "她的手下早就被我们\x01",
            "全部逮捕了啊～！\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_EAE8")

    #C0602
    ChrTalk(
        0x102,
        (
            "#00101F总、总之……\x01",
            "赶快追上去吧！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EC00")

    label("loc_EAE8")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_EB21")

    #C0603
    ChrTalk(
        0x103,
        (
            "#00201F总之……\x01",
            "赶快追上去吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EC00")

    label("loc_EB21")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_EB70")

    #C0604
    ChrTalk(
        0x104,
        (
            "#00301F啧，虽然不知道是怎么回事……\x01",
            "但赶快追上去吧！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EC00")

    label("loc_EB70")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_EBBF")

    #C0605
    ChrTalk(
        0x109,
        (
            "#10101F虽、虽然不清楚是怎么回事……\x01",
            "但赶快追上去吧！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EC00")

    label("loc_EBBF")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_EC00")

    #C0606
    ChrTalk(
        0x105,
        (
            "#10302F总之，\x01",
            "先别管这些了，\x01",
            "赶快追上去吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EC00")


    #C0607
    ChrTalk(
        0x101,
        (
            "#00003F说、说的没错。\x02\x03",

            "#00001F好，继续追击！\x02",
        )
    )

    CloseMessageWindow()
    StopSound(451, 1000, 100)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 1)
    NewScene("e4800", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_44_D1AC end

    def Function_45_EC50(): pass

    label("Function_45_EC50")

    OP_93(0xFE, 0x10E, 0x0)
    OP_82(0xC8, 0x12C, 0xBB8, 0x190)
    Fade(500)
    SetChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0x26)
    SetChrSubChip(0xFE, 0x0)
    OP_96(0xFE, 0x4BA, 0x0, 0x99C, 0x1388, 0x0)
    OP_A6(0xFE, 0x1E, 0xA, 0x190, 0x1F4)
    SetChrSubChip(0xFE, 0x1)
    Sound(514, 0, 60, 0)
    Return()

    # Function_45_EC50 end

    def Function_46_ECAC(): pass

    label("Function_46_ECAC")

    OP_93(0xFE, 0xB4, 0x0)
    OP_82(0xC8, 0x12C, 0xBB8, 0x190)
    Fade(500)
    SetChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0x28)
    SetChrSubChip(0xFE, 0x0)
    OP_96(0xFE, 0xFFFFFC22, 0x0, 0x13CE, 0x1388, 0x0)
    OP_A6(0xFE, 0x1E, 0xA, 0x190, 0x1F4)
    SetChrSubChip(0xFE, 0x1)
    Return()

    # Function_46_ECAC end

    def Function_47_ED02(): pass

    label("Function_47_ED02")

    OP_95(0xFE, 0, 0, 8350, 4000, 0x0)

    def lambda_ED1B():
        OP_95(0xFE, 0, 0, 10000, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_ED1B)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
    Return()

    # Function_47_ED02 end

    def Function_48_ED3C(): pass

    label("Function_48_ED3C")

    Fade(500)
    Sound(812, 0, 100, 0)
    ClearChrFlags(0xFE, 0x4)
    ClearChrBattleFlags(0xFE, 0x4)
    SetChrChipByIndex(0xFE, 0x1F)
    SetChrSubChip(0xFE, 0x0)
    SetChrPos(0xFE, -2790, 0, 2570, 180)
    OP_93(0xFE, 0x5A, 0x1F4)
    OP_95(0xFE, -230, 0, 2530, 4000, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    BeginChrThread(0xFE, 2, 0, 47)
    Return()

    # Function_48_ED3C end

    def Function_49_ED93(): pass

    label("Function_49_ED93")

    Fade(500)
    Sound(812, 0, 100, 0)
    ClearChrFlags(0xFE, 0x4)
    ClearChrBattleFlags(0xFE, 0x4)
    SetChrChipByIndex(0xFE, 0x21)
    SetChrSubChip(0xFE, 0x0)
    SetChrPos(0xFE, -1720, 0, 2580, 180)
    OP_93(0xFE, 0x5A, 0x1F4)
    OP_95(0xFE, -230, 0, 2530, 4000, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    BeginChrThread(0xFE, 2, 0, 47)
    Return()

    # Function_49_ED93 end

    def Function_50_EDEA(): pass

    label("Function_50_EDEA")

    Fade(500)
    Sound(812, 0, 100, 0)
    ClearChrFlags(0xFE, 0x4)
    ClearChrBattleFlags(0xFE, 0x4)
    SetChrChipByIndex(0xFE, 0x23)
    SetChrSubChip(0xFE, 0x0)
    SetChrPos(0xFE, -2280, 0, 2400, 0)
    OP_93(0xFE, 0x5A, 0x1F4)
    OP_95(0xFE, -230, 0, 2530, 4000, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    BeginChrThread(0xFE, 2, 0, 47)
    Return()

    # Function_50_EDEA end

    SaveToFile()

Try(main)
