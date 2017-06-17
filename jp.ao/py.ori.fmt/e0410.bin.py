from ScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "父",                     # 3
        "女の子",                 # 4
        "青年",                   # 5
        "妹",                     # 6
        "兄",                     # 7
        "御守役",                 # 8
        "シン",                   # 9
        "娘",                     # 10
        "婦人",                   # 11
        "ロープ",                 # 12
        "ダミー",                 # 13
        "乗客",                   # 14
        "乗客",                   # 15
        "乗客",                   # 16
        "乗客",                   # 17
        "乗客",                   # 18
        "乗客",                   # 19
        "乗客",                   # 20
        "乗客",                   # 21
        "乗客",                   # 22
        "乗客",                   # 23
        "乗客",                   # 24
        "乗客",                   # 25
        "猟兵",                   # 26
        "猟兵",                   # 27
        "猟兵",                   # 28
        "猟兵",                   # 29
        "猟兵",                   # 30
        "猟兵",                   # 31
        "キリカ",                 # 32
        "レクター",               # 33
        "偽ブランド商",           # 34
        "共和国系テロリスト",     # 35
        "共和国系テロリスト",     # 36
        "共和国系テロリスト",     # 37
        "黒月構成員",             # 38
        "黒月構成員",             # 39
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
        "Function_4_D09",          # 04, 4
        "Function_5_D8E",          # 05, 5
        "Function_6_E3E",          # 06, 6
        "Function_7_EAF",          # 07, 7
        "Function_8_F2C",          # 08, 8
        "Function_9_F91",          # 09, 9
        "Function_10_FE5",         # 0A, 10
        "Function_11_1104",        # 0B, 11
        "Function_12_1216",        # 0C, 12
        "Function_13_129B",        # 0D, 13
        "Function_14_1310",        # 0E, 14
        "Function_15_2223",        # 0F, 15
        "Function_16_225C",        # 10, 16
        "Function_17_45B8",        # 11, 17
        "Function_18_4D5B",        # 12, 18
        "Function_19_5028",        # 13, 19
        "Function_20_50E4",        # 14, 20
        "Function_21_5149",        # 15, 21
        "Function_22_51AE",        # 16, 22
        "Function_23_5680",        # 17, 23
        "Function_24_5BD9",        # 18, 24
        "Function_25_60E4",        # 19, 25
        "Function_26_67A1",        # 1A, 26
        "Function_27_67AA",        # 1B, 27
        "Function_28_6CCD",        # 1C, 28
        "Function_29_70C8",        # 1D, 29
        "Function_30_8006",        # 1E, 30
        "Function_31_88EB",        # 1F, 31
        "Function_32_8D66",        # 20, 32
        "Function_33_9D47",        # 21, 33
        "Function_34_9FF7",        # 22, 34
        "Function_35_BF66",        # 23, 35
        "Function_36_BFB0",        # 24, 36
        "Function_37_BFFA",        # 25, 37
        "Function_38_C031",        # 26, 38
        "Function_39_C06B",        # 27, 39
        "Function_40_C0A5",        # 28, 40
        "Function_41_C0DF",        # 29, 41
        "Function_42_C119",        # 2A, 42
        "Function_43_C153",        # 2B, 43
        "Function_44_E84A",        # 2C, 44
        "Function_45_104C2",       # 2D, 45
        "Function_46_1051E",       # 2E, 46
        "Function_47_10574",       # 2F, 47
        "Function_48_105AE",       # 30, 48
        "Function_49_10605",       # 31, 49
        "Function_50_1065C",       # 32, 50
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 1)), scpexpr(EXPR_END)), "loc_CEA")

    #C0001
    ChrTalk(
        0xFE,
        (
            "す、すまんが、\x01",
            "ちょっと待っていてくれんか。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0xFE,
        (
            "チケットは絶対にあるはずじゃ。\x01",
            "必ず探し出してみせるからのう！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D05")

    label("loc_CEA")

    Call(0, 25)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D05")
    Call(0, 26)

    label("loc_D05")

    TalkEnd(0xFE)
    Return()

    # Function_3_C65 end

    def Function_4_D09(): pass

    label("Function_4_D09")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 2)), scpexpr(EXPR_END)), "loc_D6F")

    #C0003
    ChrTalk(
        0xFE,
        (
            "今回の商談がまとまれば\x01",
            "大もうけ間違いナシだ！\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0xFE,
        "むふふ、楽しみで仕方ないよ！\x02",
    )

    CloseMessageWindow()
    Jump("loc_D8A")

    label("loc_D6F")

    Call(0, 24)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D8A")
    Call(0, 26)

    label("loc_D8A")

    TalkEnd(0xFE)
    Return()

    # Function_4_D09 end

    def Function_5_D8E(): pass

    label("Function_5_D8E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 3)), scpexpr(EXPR_END)), "loc_E22")
    TalkBegin(0xFE)

    #C0005
    ChrTalk(
        0xFE,
        (
            "今日はこれから\x01",
            "共和国にある実家の方に\x01",
            "里帰りするんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0xFE,
        (
            "娘も久しぶりに\x01",
            "祖父母に会えるとあって\x01",
            "すごく嬉しいみたいだね。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Jump("loc_E3D")

    label("loc_E22")

    Call(0, 23)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E3D")
    Call(0, 26)

    label("loc_E3D")

    Return()

    # Function_5_D8E end

    def Function_6_E3E(): pass

    label("Function_6_E3E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 3)), scpexpr(EXPR_END)), "loc_E93")
    TalkBegin(0xFE)

    #C0007
    ChrTalk(
        0xFE,
        (
            "おじいちゃん、おばあちゃん、\x01",
            "いまから行くからまっててねー♪\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Jump("loc_EAE")

    label("loc_E93")

    Call(0, 23)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_EAE")
    Call(0, 26)

    label("loc_EAE")

    Return()

    # Function_6_E3E end

    def Function_7_EAF(): pass

    label("Function_7_EAF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 4)), scpexpr(EXPR_END)), "loc_F10")
    TalkBegin(0xFE)

    #C0008
    ChrTalk(
        0xFE,
        (
            "僕はこれから、\x01",
            "故郷のオレドに帰るんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0xFE,
        "……母さんは元気かなぁ。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Jump("loc_F2B")

    label("loc_F10")

    Call(0, 22)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F2B")
    Call(0, 26)

    label("loc_F2B")

    Return()

    # Function_7_EAF end

    def Function_8_F2C(): pass

    label("Function_8_F2C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 5)), scpexpr(EXPR_END)), "loc_F75")
    TalkBegin(0xFE)

    #C0010
    ChrTalk(
        0xFE,
        (
            "もう、お兄ちゃんのことなんか\x01",
            "知らないんだから！\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Jump("loc_F90")

    label("loc_F75")

    Call(0, 30)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CB, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F90")
    Call(0, 31)

    label("loc_F90")

    Return()

    # Function_8_F2C end

    def Function_9_F91(): pass

    label("Function_9_F91")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 5)), scpexpr(EXPR_END)), "loc_FC9")
    TalkBegin(0xFE)

    #C0011
    ChrTalk(
        0xFE,
        "ふぅ、ほんと可愛くない妹だな。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Jump("loc_FE4")

    label("loc_FC9")

    Call(0, 30)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CB, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_FE4")
    Call(0, 31)

    label("loc_FE4")

    Return()

    # Function_9_F91 end

    def Function_10_FE5(): pass

    label("Function_10_FE5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 6)), scpexpr(EXPR_END)), "loc_10E8")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1095")

    #C0012
    ChrTalk(
        0xFE,
        (
            "ふふ、どうやら今回の旅は\x01",
            "シン様にとってかなり有意義な\x01",
            "ものになったようですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0xFE,
        (
            "これも皆さんのおかげです。\x01",
            "どうもありがとうございました。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10E0")

    label("loc_1095")


    #C0014
    ChrTalk(
        0xFE,
        (
            "ふむ、今日は朗らかで\x01",
            "いい天気ですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0xFE,
        "ふふ、絶好の列車日和です。\x02",
    )

    CloseMessageWindow()

    label("loc_10E0")

    TalkEnd(0xFE)
    Jump("loc_1103")

    label("loc_10E8")

    Call(0, 29)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CB, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1103")
    Call(0, 31)

    label("loc_1103")

    Return()

    # Function_10_FE5 end

    def Function_11_1104(): pass

    label("Function_11_1104")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 6)), scpexpr(EXPR_END)), "loc_11FA")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1181")

    #C0016
    ChrTalk(
        0xFE,
        (
            "とりあえず、\x01",
            "ボクはいつかまたきっと\x01",
            "クロスベルに来るからな。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0xFE,
        "……その時までさらばだ。\x02",
    )

    CloseMessageWindow()
    Jump("loc_11F2")

    label("loc_1181")


    #N0018
    NpcTalk(
        0xFE,
        "男の子",
        "なんだ、まだ何か用があるのか？\x02",
    )

    CloseMessageWindow()

    #N0019
    NpcTalk(
        0xFE,
        "男の子",
        (
            "フンッ、ボクは忙しいんだ。\x01",
            "むやみに声をかけるんじゃない。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11F2")

    TalkEnd(0xFE)
    Jump("loc_1215")

    label("loc_11FA")

    Call(0, 29)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CB, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1215")
    Call(0, 31)

    label("loc_1215")

    Return()

    # Function_11_1104 end

    def Function_12_1216(): pass

    label("Function_12_1216")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 7)), scpexpr(EXPR_END)), "loc_127C")

    #C0020
    ChrTalk(
        0xFE,
        (
            "ぶつぶつ……\x01",
            "出発まであと何分くらいかしら？\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0xFE,
        "ああん、名残惜しいわねっ……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_1297")

    label("loc_127C")

    Call(0, 28)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CB, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1297")
    Call(0, 31)

    label("loc_1297")

    TalkEnd(0xFE)
    Return()

    # Function_12_1216 end

    def Function_13_129B(): pass

    label("Function_13_129B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CB, 0)), scpexpr(EXPR_END)), "loc_12F1")

    #C0022
    ChrTalk(
        0xFE,
        (
            "なによ、もう用事はないんでしょ？\x01",
            "だったら早く行ってちょうだい。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_130C")

    label("loc_12F1")

    Call(0, 27)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CB, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_130C")
    Call(0, 31)

    label("loc_130C")

    TalkEnd(0xFE)
    Return()

    # Function_13_129B end

    def Function_14_1310(): pass

    label("Function_14_1310")

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
    SetChrName("ノエル曹長")

    #A0023
    AnonymousTalk(
        0xFF,
        (
            "ふう……でも無事に\x01",
            "任務が片付いてよかったです。\x02\x03",

            "正直、足を引っ張ってしまうんじゃ\x01",
            "ないかとヒヤヒヤしました。\x02",
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
            "#6P#00002Fはは、心配性だなぁ。\x02\x03",

            "#00004Fソーニャ司令だって\x01",
            "曹長に見込みがあると思ったから\x01",
            "推薦したんだろうし。\x02\x03",

            "#00000Fとにかく、これからは\x01",
            "改めてよろしくお願いするよ。\x02",
        )
    )

    CloseMessageWindow()

    #N0025
    NpcTalk(
        0x109,
        "ノエル曹長",
        (
            "#10109F#11Pはい、こちらこそ！\x02\x03",

            "#10105F……あ、でも、ロイドさん。\x01",
            "ちょっと宜しいでしょうか？\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x101,
        "#6P#00005Fん？\x02",
    )

    CloseMessageWindow()

    #N0027
    NpcTalk(
        0x109,
        "ノエル曹長",
        (
            "#10106F#11P一応、これからしばらくの間、\x01",
            "正式にお世話になるわけですし……\x02\x03",

            "#10102F軍服も着てないわけですから\x01",
            "その“曹長”というのはちょっと……\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x101,
        (
            "#6P#00011Fあ、ああ、それもそうか。\x02\x03",

            "#00000Fでもどうしよう？\x01",
            "呼び捨てでも構わないかな？\x02",
        )
    )

    CloseMessageWindow()

    #N0029
    NpcTalk(
        0x109,
        "ノエル曹長",
        "#10109F#11Pええ、それでお願いします。\x02",
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x101,
        (
            "#6P#00009Fそれじゃあノエル──\x01",
            "改めてよろしくお願いするよ。\x02\x03",

            "#00002Fそうだ、そっちもよかったら\x01",
            "もっとフランクに行ってくれ。\x02\x03",

            "同い年だし、同僚なんだから\x01",
            "気を使わないで欲しいんだ。\x02",
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
            "#10111F#11Pええっ！？\x01",
            "あたしがロイドさんのことを！？\x02\x03",

            "#10106F………………………………\x01",
            "無理無理、そんなの無理ですよ！\x02\x03",

            "#10101Fあくまで警察官としては新米ですし、\x01",
            "勉強させてもらう身分なんですから！\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x101,
        (
            "#6P#00011Fいや、そんなに堅苦しく\x01",
            "考えることないと思うけど……\x02\x03",

            "#00000Fエリィとランディだって\x01",
            "歳の差関係なくタメ口だしさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x109,
        (
            "#10106F#11Pいや、その……\x01",
            "何というか性分みたいで……\x02\x03",

            "一度そう思い込んじゃうと\x01",
            "なかなか変えられないというか……\x02\x03",

            "#10101Fでも、ロイドさんがそう仰るなら\x01",
            "何とか努力してタメ口を──！\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x101,
        (
            "#6P#00012Fい、いや。\x01",
            "別に無理はしなくていいから。\x02\x03",

            "#00002Fはは……\x01",
            "根っからの体育会気質なんだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x109,
        (
            "#10109F#11Pあはは……\x01",
            "父の影響かもしれませんね。\x02\x03",

            "#10100F厳しい人で、あたしもフランも\x01",
            "小さい頃に躾けられましたから。\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x101,
        "#6P#00002Fへえ、お父さんの。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0037
    ChrTalk(
        0x101,
        (
            "#6P#00005Fあれ、君たちのお母さんには\x01",
            "何度か会ったことがあるけど……？\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x109,
        (
            "#10104F#11P父は……\x01",
            "１０年ほど前に亡くなりました。\x02\x03",

            "#10100Fクロスベル警備隊に所属していて、\x01",
            "その、任務中の事故で。\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x101,
        (
            "#6P#00006F………そっか。\x01",
            "悪いことを聞いちゃったな。\x02\x03",

            "#00001Fひょっとして……\x01",
            "君が警備隊に入ったのも？\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x109,
        (
            "#10105F#11Pどうでしょう……？\x01",
            "あまり自覚した事は無いですけど。\x02\x03",

            "#10104Fでも、父と同じように\x01",
            "クロスベルという地を守りたかったのは\x01",
            "確かかもしれません。\x02\x03",

            "#10100Fその意味では、所属は違っても\x01",
            "フランも同じなのかもしれませんね。\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x101,
        "#6P#00002Fそっか……\x02",
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
        "#10105F#11Pロイドさん？\x02",
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x101,
        (
            "#6P#00004Fごめん、何でもない。\x02\x03",

            "#00002F──でも、君が来てくれて\x01",
            "こちらは本当に助かったよ。\x02\x03",

            "人手が足りないってのもあるけど\x01",
            "……この先、何が起きるのか\x01",
            "正直予想できないくらいだからさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x109,
        (
            "#10112F#11Pあはは、そう言ってもらえると\x01",
            "光栄ですけど……\x02\x03",

            "#10102Fでも、マフィアがいなくなって\x01",
            "市内の治安も改善されたんですよね？\x02\x03",

            "『黒月#4Rヘイユエ#』は残っていますけど\x01",
            "目立った動きは無いみたいですし。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x101,
        (
            "#6P#00006F……表面的にはね。\x02\x03",

            "#00008Fただ、一つ言えるのは\x01",
            "《ルバーチェ》という組織が\x01",
            "一定の役割を果たしていた事だ。\x02\x03",

            "#00001Fクロスベルの治安を守る意味でね。\x02",
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

    # Function_14_1310 end

    def Function_15_2223(): pass

    label("Function_15_2223")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_225B")
    OP_82(0xA, 0xA, 0x5DC, 0x2EE)
    Sleep(3500)
    OP_82(0xA, 0xA, 0x4B0, 0x1F4)
    Sleep(3500)
    Jump("Function_15_2223")

    label("loc_225B")

    Return()

    # Function_15_2223 end

    def Function_16_225C(): pass

    label("Function_16_225C")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2351")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "◆前編実績エリィとの絆達成済\x01",      # 0
            "◆前編実績ティオとの絆達成済\x01",      # 1
            "◆前編実績ランディの絆達成済\x01",      # 2
            "◆前編実績全員の絆達成済\x01",          # 3
            "◆変更しない\x01",                      # 4
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2326"),
        (1, "loc_232E"),
        (2, "loc_2336"),
        (3, "loc_233E"),
        (4, "loc_234C"),
        (SWITCH_DEFAULT, "loc_234C"),
    )


    label("loc_2326")

    SetScenarioFlags(0x25, 3)
    Jump("loc_2351")

    label("loc_232E")

    SetScenarioFlags(0x25, 4)
    Jump("loc_2351")

    label("loc_2336")

    SetScenarioFlags(0x25, 5)
    Jump("loc_2351")

    label("loc_233E")

    SetScenarioFlags(0x25, 3)
    SetScenarioFlags(0x25, 4)
    SetScenarioFlags(0x25, 5)
    Jump("loc_2351")

    label("loc_234C")

    Jump("loc_2351")

    label("loc_2351")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 3)), scpexpr(EXPR_END)), "loc_241E")
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis224.itp")
    RunExpression(0x3, (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_241E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 4)), scpexpr(EXPR_END)), "loc_2461")
    CreatePortrait(2, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis225.itp")
    RunExpression(0x3, (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2461")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 5)), scpexpr(EXPR_END)), "loc_24A4")
    CreatePortrait(3, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis226.itp")
    RunExpression(0x3, (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_24A4")

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
            "#10105Fマフィアがクロスベルの\x01",
            "治安を守っていた……？\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x101,
        (
            "#00006Fまあ、結果的にだけどね。\x02\x03",

            "#00001F……クロスベルの置かれている\x01",
            "特殊な状況を考えてみてくれ。\x02\x03",

            "自治権はあっても\x01",
            "国家としては独立しておらず、\x01",
            "２大国の干渉を常に受けている。\x02\x03",

            "犯罪を取り締まる法律は穴だらけで\x01",
            "入国規制もほとんどない……\x02\x03",

            "#00003F本来なら、黒月どころか\x01",
            "他の犯罪組織やテロリストなんかが\x01",
            "跋扈#4Rばっこ#してもおかしくない場所なんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x109,
        (
            "#10101Fあ……\x02\x03",

            "……それじゃあ今までは\x01",
            "ルバーチェがそれを抑える役割を？\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x101,
        (
            "#00008F認めたくはないけど……\x01",
            "結果的に一定の秩序を裏社会に\x01",
            "もたらしていたのは否定できない。\x02\x03",

            "#00006F……それが何の前触れもなく\x01",
            "《教団》という災厄に巻き込まれる形で\x01",
            "消滅してしまった……\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x109,
        "#10108Fパワーバランスの崩壊、ですか。\x02",
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x101,
        (
            "#00003Fああ……\x01",
            "帝国派と共和国派の議員たちが\x01",
            "失脚したのも同じことが言える。\x02\x03",

            "代弁者が居なくなったことで\x01",
            "逆に両国からの圧力が今まで以上に\x01",
            "露骨になる可能性は高いだろう。\x02\x03",

            "#00013F──だからこそ新市長は\x01",
            "支援課#6Rオレたち#に期待してるんだと思う。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x109,
        (
            "#10104Fなるほど……\x01",
            "ようやく納得しました。\x02\x03",

            "#10100Fエリィさんやランディ先輩、\x01",
            "ティオちゃんが一時的に離れたのも\x01",
            "それが理由だったんですね？\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x101,
        (
            "#00004Fああ、新たな局面を前に\x01",
            "可能な限り各方面と連携して\x01",
            "より高度な活動が出来るようにする。\x02\x03",

            "俺も一課で研修させてもらって\x01",
            "色々なことを叩き込まれたし……\x02\x03",

            "#00002F更に、人手が足りなかったから\x01",
            "新たな戦力も要請したってわけさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x109,
        (
            "#10109Fふふっ……\x01",
            "呼んでいただけて光栄です。\x02",
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
        "#12P#10105Fでも、そういえば……\x02",
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x101,
        "#00000F#5Pん、どうしたんだ？\x02",
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x109,
        (
            "#12P#10100Fもう一人の新メンバーって\x01",
            "前に会った“彼”ですよね？\x02\x03",

            "正直、意外だったんですけど\x01",
            "どういう経緯なんですか？\x02",
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
            "#00011F#5Pああ──“彼”ね。\x02\x03",

            "#00006Fいや、新しい人手を\x01",
            "俺たちが探し始めた矢先に\x01",
            "こちらを訪ねて来てさ。\x02\x03",

            "新市長からの推薦なんかも\x01",
            "取り付けてきたから\x01",
            "断るに断れなかったんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x109,
        "#12P#10111Fし、市長の推薦ですか？\x02",
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x101,
        (
            "#00001F#5Pああ、ＩＢＣビルの危機に\x01",
            "力を貸した謝礼と引き換えに\x01",
            "推薦状を貰ったらしい。\x02\x03",

            "#00006F……そもそも特務支援課が\x01",
            "新規メンバーを探してるなんて\x01",
            "どこで聞きつけたのやら。\x02\x03",

            "本人は『面白そうだから』とか\x01",
            "しれっと言ってたけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x109,
        (
            "#12P#10108Fえっと……\x01",
            "それって大丈夫なんですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x101,
        (
            "#00012F#5Pま、まあ……\x01",
            "悪いヤツじゃないのは確かだよ。\x02\x03",

            "#00002Fそりゃあ、経歴不詳だったり、\x01",
            "裏社会にやたらと詳しかったり、\x01",
            "ホストなんかもやってるけど。\x02\x03",

            "#00006F……何だか言ってて\x01",
            "だんだん不安になってきたな。\x02",
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
            "#12P#10112Fだ、大丈夫ですよ。\x02\x03",

            "#10102F確かに皮肉屋で口は悪いけど\x01",
            "悪い子じゃなさそうでしたし……\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x101,
        (
            "#00012F#5Pはは……\x01",
            "そう言ってくれると助かるよ。\x02\x03",

            "#00002F正直、君とはソリが\x01",
            "合わないかと思ったからさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x109,
        (
            "#12P#10106Fう、うーん……\x01",
            "確かにあたしもからかわれたり\x01",
            "しましたけど……\x02\x03",

            "#10100Fどちらかというと\x01",
            "ロイドさんをいじる方が\x01",
            "彼には楽しいみたいですし。\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x101,
        (
            "#00006F#5Pうぐっ……\x01",
            "勘弁して欲しいんだけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x109,
        (
            "#12P#10112Fあはは……\x01",
            "（フランが騒いでたとか\x01",
            "  言わない方がいいのかな？）\x02",
        )
    )

    CloseMessageWindow()
    Sound(800, 0, 100, 0)
    Sleep(500)
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("車掌の声")

    #A0069
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "──乗客の皆様にお伝えします。\x02",
        )
    )

    CloseMessageWindow()

    #A0070
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "まもなく、クロスベル自治州、\x01",
            "クロスベル市に到着いたします。\x02",
        )
    )

    CloseMessageWindow()

    #A0071
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "リベール、レミフェリア各方面への\x01",
            "定期飛行船をご利用のお客様は\x01",
            "お乗換えください。\x02",
        )
    )

    CloseMessageWindow()

    #A0072
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "なお、大陸鉄道公社規約に基づき、\x01",
            "当列車はクロスベル駅にて\x01",
            "３０分ほど停車させていただきます。\x02",
        )
    )

    CloseMessageWindow()

    #A0073
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "エレボニア方面に向かわれる方は\x01",
            "入国申請書をご記入の上、\x01",
            "臨検官への提出をお願いいたします。\x07\x00\x02",
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
            "#00002F#5Pはは、一駅だけだから\x01",
            "あっという間だったな。\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0x109,
        (
            "#12P#10104Fええ……\x02\x03",

            "#10102Fそれでも数日、留守にしていると\x01",
            "何だか懐かしい感じがしますね。\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x101,
        "#00002F#5Pそうだな……\x02",
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
            "#00004F#5P（……全員が揃うのは\x01",
            "  もうちょっとしてからか……）\x02\x03",

            "#00002F（キーア……\x01",
            "  寂しがってないといいけど。）\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(300)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3694")
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
            "#1K教団事件の夜、ＩＢＣビル１６Ｆで誰と話した？\x07\x00\x02",
        )
    )

    MenuCmd(0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 3)), scpexpr(EXPR_END)), "loc_35D6")
    MenuCmd(1, 0, "【エリィ】")

    label("loc_35D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 4)), scpexpr(EXPR_END)), "loc_35ED")
    MenuCmd(1, 0, "【ティオ】")

    label("loc_35ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 5)), scpexpr(EXPR_END)), "loc_3606")
    MenuCmd(1, 0, "【ランディ】")

    label("loc_3606")

    MenuCmd(2, 0, -1, 100, 0)
    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3644"),
        (1, "loc_365D"),
        (2, "loc_3687"),
        (SWITCH_DEFAULT, "loc_368F"),
    )


    label("loc_3644")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 3)), scpexpr(EXPR_END)), "loc_3655")
    SetScenarioFlags(0x121, 2)
    Jump("loc_3658")

    label("loc_3655")

    SetScenarioFlags(0x121, 3)

    label("loc_3658")

    Jump("loc_368F")

    label("loc_365D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 3)), scpexpr(EXPR_END)), "loc_367F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 4)), scpexpr(EXPR_END)), "loc_3677")
    SetScenarioFlags(0x121, 3)
    Jump("loc_367A")

    label("loc_3677")

    SetScenarioFlags(0x121, 4)

    label("loc_367A")

    Jump("loc_3682")

    label("loc_367F")

    SetScenarioFlags(0x121, 4)

    label("loc_3682")

    Jump("loc_368F")

    label("loc_3687")

    SetScenarioFlags(0x121, 4)
    Jump("loc_368F")

    label("loc_368F")

    Jump("loc_36C2")

    label("loc_3694")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 3)), scpexpr(EXPR_END)), "loc_36A5")
    SetScenarioFlags(0x121, 2)
    Jump("loc_36C2")

    label("loc_36A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 4)), scpexpr(EXPR_END)), "loc_36B6")
    SetScenarioFlags(0x121, 3)
    Jump("loc_36C2")

    label("loc_36B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 5)), scpexpr(EXPR_END)), "loc_36C2")
    SetScenarioFlags(0x121, 4)

    label("loc_36C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x121, 2)), scpexpr(EXPR_END)), "loc_3B20")
    Sleep(300)

    #C0079
    ChrTalk(
        0x101,
        "#00004F#5P（それに……）\x02",
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
        "エリィ",
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#00112F#N#11P……え、えっと……\x01",
            "私、ベルの所に戻るわね。\x02\x03",

            "#00113F何かおじさまたちに\x01",
            "協力できることがあるかも\x01",
            "しれないから……\x02",
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
            "#00004Fあ、ああ……\x01",
            "俺も今のうちに補給と\x01",
            "装備の確認をしてくるよ。\x02\x03",

            "#00002F……また、後でな。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #N0082
    NpcTalk(
        0x15,
        "エリィ",
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#00102F#N#11Pええ……\x02\x03",

            "#00113F……その、さっきの続きは、\x01",
            "ぜんぶ解決した後にでも……\x02",
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
            "#00005Fえ。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #N0084
    NpcTalk(
        0x15,
        "エリィ",
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#00112F#N#11Pな、なんでもないっ。\x02\x03",

            "#00109Fそ、それじゃあまた後でね！\x07\x00\x02",
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
            "#00004F#5P（……あれからお互い忙しくて\x01",
            "  あんまり進展してないけど……）\x02\x03",

            "（エリィが戻ってきたら\x01",
            "  何とかしてあの時の続きを──）\x02\x03",

            "#00011F（いやいや、続きじゃないだろ！\x01",
            "  もっと真面目に考えないと……）\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x109,
        "#12P#10100F……ロイドさん？\x02",
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
            "#00011F#5Pいやその、何でもないんだ！\x02\x03",

            "#00012Fそれにしても疲れたなぁ！\x01",
            "早く支援課のソファで休みたいよ！\x02",
        )
    )

    CloseMessageWindow()
    OP_64(0x101)

    #C0088
    ChrTalk(
        0x109,
        "#12P#10105F（ロイドさんの反応が怪しい……）\x02",
    )

    CloseMessageWindow()
    Jump("loc_453D")

    label("loc_3B20")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x121, 3)), scpexpr(EXPR_END)), "loc_3FC6")
    Sleep(300)

    #C0089
    ChrTalk(
        0x101,
        "#00004F#5P（それに……）\x02",
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
        "ティオ",
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#00204F#N#11P……ミシュラムのテーマパーク。\x02\x03",

            "この騒ぎが無事解決したら\x01",
            "あそこに連れて行ってください。\x02",
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
            "#00011Fええっ……\x01",
            "そんなのでいいのか！？\x02\x03",

            "#00001Fいや、でも……\x01",
            "もうちょっとこうシリアスな\x01",
            "約束の方がいいんじゃないか？\x02\x03",

            "ティオが困った時には\x01",
            "何があっても助けに行くとか。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #N0092
    NpcTalk(
        0x15,
        "ティオ",
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#00204F#N#11Pいえ、これで十分です。\x02\x03",

            "#00208Fそれに、この事態を解決しないと\x01",
            "この約束も果たされない……\x02\x03",

            "#00202Fその意味では十分、\x01",
            "シリアスなのではないかと。\x07\x00\x02",
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
            "#00004F#5P（……あれからお互い忙しくて\x01",
            "  まだ遊びに行けてないけど……）\x02\x03",

            "（ティオが戻ってきたら\x01",
            "  絶対にあの約束を守らないと。）\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x109,
        "#12P#10105F……ロイドさん？\x02",
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
            "#00005F#5Pああ、ごめん。\x02\x03",

            "#00000F……そういえばノエルって\x01",
            "テーマパークに行った事はある？\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0x109,
        (
            "#12P#10102Fミシュラムですか？\x01",
            "ええ、前にフランと一度だけ。\x02\x03",

            "#10109Fアトラクションも面白いんですけど\x01",
            "みっしぃが可愛いんですよね～！\x02",
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
            "#00012F#5Pそ、そっか……\x01",
            "（大人気だな、みっしぃ。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_453D")

    label("loc_3FC6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x121, 4)), scpexpr(EXPR_END)), "loc_453D")
    Sleep(300)

    #C0098
    ChrTalk(
        0x101,
        "#00004F#5P（それに……）\x02",
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
        "ランディ",
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#00303F#N#11P──警備隊が押し寄せたら\x01",
            "最後まで動けるのは俺らだろう。\x02\x03",

            "#00300Fお嬢やティオすけには\x01",
            "あんま無茶させたくないしな。\x02",
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
            "#00004F……ああ、分かってる。\x02\x03",

            "#00000F俺とランディの２人で\x01",
            "何とか喰い止める必要があるな。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(200, 50, -1, -1)
    SetChrName("ランディ")

    #N0101
    NpcTalk(
        0x15,
        "ランディ",
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#00302F#N#11Pそういう事だ。\x02\x03",

            "#00309F背中は任せたぜ──相棒。\x07\x00\x02",
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
            "#00005Fあ……\x02\x03",

            "#00002F──了解！\x07\x00\x02",
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
            "#00008F#5P（相棒か……）\x02\x03",

            "#00003F（正直、まだ男として釣り合いが\x01",
            "  取れているとは思えないんだよな。）\x02\x03",

            "#00000F（本当に肩を並べられるよう\x01",
            "  もっと俺も頑張らないと……）\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0x109,
        "#12P#10105F……ロイドさん？\x02",
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
            "#00005F#5Pああ、ごめん。\x02\x03",

            "#00000Fそういえば、ノエルの目から見て\x01",
            "ランディってどうなのかな？\x02\x03",

            "警察官というより、\x01",
            "警備隊員としてなんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0x109,
        (
            "#12P#10105Fランディ先輩ですか？\x02\x03",

            "#10104Fそうですね……\x01",
            "やっぱり規格外な感じがしますね。\x02\x03",

            "#10100F個人の戦闘力はもちろんですけど、\x01",
            "部隊レベルの戦術なんかも\x01",
            "相当凄いって聞いていますし……\x02\x03",

            "今やっているリハビリ訓練でも\x01",
            "かなり飛ばしているみたいですよ？\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0x101,
        (
            "#00002F#5Pそっか……\x02\x03",

            "#00008F（……そういえばランディ、\x01",
            "  今回の訓練でライフルを\x01",
            "  使うとか言ってたけど……）\x02\x03",

            "（少しは猟兵時代のことを\x01",
            "  吹っ切れたのかな……？）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_453D")

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

    # Function_16_225C end

    def Function_17_45B8(): pass

    label("Function_17_45B8")

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

    # Function_17_45B8 end

    def Function_18_4D5B(): pass

    label("Function_18_4D5B")

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
            "#00004Fさてと、俺たちの担当は\x01",
            "後ろ半分の２両だ。\x02\x03",

            "#00001F乗客は……\x01",
            "結構いるみたいだな。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4EBC")

    #C0109
    ChrTalk(
        0x102,
        (
            "#00100Fみたいね、とにかく一人一人\x01",
            "確実にチェックして行きましょう。\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x79, 0x1, 0x0)
    Jump("loc_5021")

    label("loc_4EBC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4F1F")

    #C0110
    ChrTalk(
        0x103,
        (
            "#00200Fですね、とにかく端から順番に\x01",
            "確実に終わらせて行きましょう。\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x79, 0x1, 0x1)
    Jump("loc_5021")

    label("loc_4F1F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4F74")

    #C0111
    ChrTalk(
        0x104,
        (
            "#00304Fま、とにかく\x01",
            "片っ端から当たってくしかねえな。\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x79, 0x1, 0x2)
    Jump("loc_5021")

    label("loc_4F74")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4FCD")

    #C0112
    ChrTalk(
        0x109,
        (
            "#10100Fはい、とにかく確実に\x01",
            "チェックを終わらせましょう。\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x79, 0x1, 0x3)
    Jump("loc_5021")

    label("loc_4FCD")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5021")

    #C0113
    ChrTalk(
        0x105,
        (
            "#10300Fふぅ、とにかく端から\x01",
            "潰していくしかなさそうだね。\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x79, 0x1, 0x4)

    label("loc_5021")

    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_18_4D5B end

    def Function_19_5028(): pass

    label("Function_19_5028")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x156, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5081")

    #C0114
    ChrTalk(
        0x101,
        (
            "#00003F……こっちは３両目だな。\x01",
            "まずは４両目の乗客を全員調べよう。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_50CD")

    label("loc_5081")


    #C0115
    ChrTalk(
        0x101,
        (
            "#00003F……前の車両は俺たちの担当外だ。\x01",
            "今は持ち場の臨検に集中しよう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_50CD")

    Sleep(50)
    SetChrPos(0x0, -10, 0, 7470, 180)
    EventEnd(0x4)
    Return()

    # Function_19_5028 end

    def Function_20_50E4(): pass

    label("Function_20_50E4")

    EventBegin(0x1)

    #C0116
    ChrTalk(
        0x101,
        (
            "#00003F……まだ臨検は終わっていない。\x01",
            "列車から出るわけにはいかないな。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, 2000, 0, -7850, 270)
    EventEnd(0x4)
    Return()

    # Function_20_50E4 end

    def Function_21_5149(): pass

    label("Function_21_5149")

    EventBegin(0x1)

    #C0117
    ChrTalk(
        0x101,
        (
            "#00003F……まだ臨検は終わっていない。\x01",
            "列車から出るわけにはいかないな。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, 2000, 0, 7850, 270)
    EventEnd(0x4)
    Return()

    # Function_21_5149 end

    def Function_22_51AE(): pass

    label("Function_22_51AE")

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
            "#00000Fすみません、\x01",
            "臨検官補佐の者です。\x02\x03",

            "お手数ですが、\x01",
            "手荷物と入国申請書を\x01",
            "確認させていただけますか？\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0xC,
        "……母さん…………\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_52D9")

    #C0120
    ChrTalk(
        0x102,
        (
            "#00105F（どうやら、\x01",
            "  声が届いていないみたいね。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5401")

    label("loc_52D9")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5328")

    #C0121
    ChrTalk(
        0x103,
        (
            "#00205F（どうやら、\x01",
            "  声が届いていないようですね。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5401")

    label("loc_5328")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5366")

    #C0122
    ChrTalk(
        0x104,
        "#00305F（ふむ、耳に入ってねえな。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_5401")

    label("loc_5366")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_53B5")

    #C0123
    ChrTalk(
        0x109,
        (
            "#10105F（えっと……\x01",
            "  声が届いていないようですね。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5401")

    label("loc_53B5")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5401")

    #C0124
    ChrTalk(
        0x105,
        (
            "#10302F（フフ、どうやら\x01",
            "  聞こえていないみたいだね。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5401")


    #C0125
    ChrTalk(
        0x101,
        "#00006F#4Sあの、すみません――\x02",
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
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_54CB")
    Jump("loc_5515")

    label("loc_54CB")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_54EB")
    OP_52(0xC, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5515")

    label("loc_54EB")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_550B")
    OP_52(0xC, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5515")

    label("loc_550B")

    OP_52(0xC, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5515")

    OP_52(0xC, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xC, 0x10)

    #C0126
    ChrTalk(
        0xC,
        "え、ああ……ごめんなさい。\x02",
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0xC,
        "ちょっとボーッとしてました。\x02",
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0xC,
        (
            "えっと、臨検の人ですね？\x01",
            "チェックの方、お願いします。\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0x101,
        "#00000Fはい、ではさっそく――\x02",
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
            "#00004F――手荷物、入国申請書ともに\x01",
            "確認できました。\x01",
            "ご協力ありがとうございます。\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0xC,
        "ああいえ、どういたしまして。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1CA, 4)
    OP_29(0x79, 0x1, 0x5)
    ClearChrFlags(0xC, 0x10)
    SetChrSubChip(0xC, 0x0)
    EventEnd(0x5)
    Return()

    # Function_22_51AE end

    def Function_23_5680(): pass

    label("Function_23_5680")

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
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5768")
    Jump("loc_57B2")

    label("loc_5768")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5788")
    OP_52(0xA, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_57B2")

    label("loc_5788")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_57A8")
    OP_52(0xA, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_57B2")

    label("loc_57A8")

    OP_52(0xA, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_57B2")

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
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5868")
    Jump("loc_58B2")

    label("loc_5868")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5888")
    OP_52(0xB, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_58B2")

    label("loc_5888")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_58A8")
    OP_52(0xB, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_58B2")

    label("loc_58A8")

    OP_52(0xB, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_58B2")

    OP_52(0xB, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xB, 0x10)
    OP_0D()

    #C0132
    ChrTalk(
        0x101,
        (
            "#00000Fえっと、臨検官補佐の者です。\x02\x03",

            "お手数ですが、\x01",
            "手荷物と入国申請書を\x01",
            "確認させていただけますか？\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0xA,
        "ああ、もちろんだとも。\x02",
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0xB,
        (
            "リンケン、リンケン♪\x01",
            "お兄ちゃんたち、よろしくね。\x02",
        )
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0x101,
        (
            "#00009Fはは、それじゃ\x01",
            "さっそく調べさせてもらうよ。\x02",
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
            "#00004F――手荷物、入国申請書ともに\x01",
            "確認できました。\x01",
            "ご協力ありがとうございます。\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0xA,
        (
            "いやなんの、\x01",
            "当たり前のことだからね。\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0xB,
        (
            "お兄ちゃんたち、\x01",
            "お仕事おつかれさまー☆\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5ACD")

    #C0139
    ChrTalk(
        0x102,
        "#00102Fふふ、どうもありがとう。\x02",
    )

    CloseMessageWindow()
    Jump("loc_5BBB")

    label("loc_5ACD")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5B12")

    #C0140
    ChrTalk(
        0x103,
        (
            "#00202Fふふ、どうも\x01",
            "ありがとうございます。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5BBB")

    label("loc_5B12")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5B4C")

    #C0141
    ChrTalk(
        0x104,
        "#00309Fはは、どうもありがとな。\x02",
    )

    CloseMessageWindow()
    Jump("loc_5BBB")

    label("loc_5B4C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5B86")

    #C0142
    ChrTalk(
        0x109,
        "#10109Fふふ、どうもありがとね。\x02",
    )

    CloseMessageWindow()
    Jump("loc_5BBB")

    label("loc_5B86")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5BBB")

    #C0143
    ChrTalk(
        0x105,
        "#10309Fフフ、どうもありがとう。\x02",
    )

    CloseMessageWindow()

    label("loc_5BBB")

    SetScenarioFlags(0x1CA, 3)
    OP_29(0x79, 0x1, 0x6)
    ClearChrFlags(0xA, 0x10)
    ClearChrFlags(0xB, 0x10)
    SetChrSubChip(0xA, 0x0)
    SetChrSubChip(0xB, 0x0)
    EventEnd(0x5)
    Return()

    # Function_23_5680 end

    def Function_24_5BD9(): pass

    label("Function_24_5BD9")

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
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5CC1")
    Jump("loc_5D0B")

    label("loc_5CC1")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5CE1")
    OP_52(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5D0B")

    label("loc_5CE1")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5D01")
    OP_52(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5D0B")

    label("loc_5D01")

    OP_52(0x9, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5D0B")

    OP_52(0x9, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x9, 0x10)
    OP_0D()

    #C0144
    ChrTalk(
        0x101,
        (
            "#00000F失礼します、\x01",
            "臨検官補佐の者です。\x02\x03",

            "お手数ですが、\x01",
            "手荷物と入国申請書を\x01",
            "確認させていただけますか？\x02",
        )
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0x9,
        "ふふ、待っていたよ！\x02",
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0x9,
        "さあどうぞ確認してくれたまえ！\x02",
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0x101,
        "#00005Fは、はぁ……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5E38")

    #C0148
    ChrTalk(
        0x102,
        "#00105F（やけにテンションが高いわね。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_5F3F")

    label("loc_5E38")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5E7C")

    #C0149
    ChrTalk(
        0x103,
        "#00200F（やけにテンションが高いですね。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_5F3F")

    label("loc_5E7C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5EBE")

    #C0150
    ChrTalk(
        0x104,
        "#00306F（やたらとテンションが高えな。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_5F3F")

    label("loc_5EBE")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5F00")

    #C0151
    ChrTalk(
        0x109,
        "#10105F（妙にテンションが高いですね。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_5F3F")

    label("loc_5F00")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5F3F")

    #C0152
    ChrTalk(
        0x105,
        "#10303F（フフ、随分テンションが高いね。）\x02",
    )

    CloseMessageWindow()

    label("loc_5F3F")

    FadeToDark(500, 0, -1)
    OP_0D()
    Sleep(1000)
    FadeToBright(500, 0)
    OP_0D()

    #C0153
    ChrTalk(
        0x101,
        (
            "#00004F――手荷物、入国申請書ともに\x01",
            "確認できました。\x01",
            "ご協力ありがとうございます。\x02",
        )
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0x9,
        (
            "むふふ、君も見ただろう？\x01",
            "この契約書の束を！\x02",
        )
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0x9,
        (
            "実は、私はこれから\x01",
            "とある大きな商談に向かう所でね！\x02",
        )
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0x9,
        (
            "それがまとまれば大もうけは確実――\x01",
            "いやぁ、楽しみで仕方ないよ！\x02",
        )
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0x101,
        (
            "#00012Fそ、そうですか……\x01",
            "うまく行くといいですね。\x02\x03",

            "#00003F（なるほど、このテンションは\x01",
            "  そういう理由か。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1CA, 2)
    OP_29(0x79, 0x1, 0x7)
    ClearChrFlags(0x9, 0x10)
    SetChrSubChip(0x9, 0x0)
    EventEnd(0x5)
    Return()

    # Function_24_5BD9 end

    def Function_25_60E4(): pass

    label("Function_25_60E4")

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
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_61CC")
    Jump("loc_6216")

    label("loc_61CC")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_61EC")
    OP_52(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6216")

    label("loc_61EC")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_620C")
    OP_52(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6216")

    label("loc_620C")

    OP_52(0x8, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6216")

    OP_52(0x8, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x8, 0x10)
    OP_0D()

    #C0158
    ChrTalk(
        0x101,
        (
            "#00000Fあの、臨検官補佐の者です。\x02\x03",

            "お手数ですが、\x01",
            "手荷物と入国申請書を\x01",
            "確認させていただけますか？\x02",
        )
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0x8,
        "ああ、もちろん構わんぞい。\x02",
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
            "#00004F――手荷物、入国申請書ともに\x01",
            "確認できました。\x02\x03",

            "#00001Fですが……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0161
    ChrTalk(
        0x8,
        "ん？　なんじゃ？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_63D1")

    #C0162
    ChrTalk(
        0x102,
        (
            "#00101Fはい、どうやら\x01",
            "手荷物の中に乗車チケットが\x01",
            "なかったようなのですが。\x02\x03",

            "心当たりはおありですか？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_65C5")

    label("loc_63D1")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6453")

    #C0163
    ChrTalk(
        0x103,
        (
            "#00201Fはい、どうやら\x01",
            "手荷物の中に乗車チケットが\x01",
            "なかったようなのですが。\x02\x03",

            "心当たりはおありでしょうか？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_65C5")

    label("loc_6453")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_64CF")

    #C0164
    ChrTalk(
        0x104,
        (
            "#00301Fああ、どうやら\x01",
            "手荷物の中に乗車チケットが\x01",
            "なかったみたいなんだが。\x02\x03",

            "心当たりはないッスか？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_65C5")

    label("loc_64CF")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_654B")

    #C0165
    ChrTalk(
        0x109,
        (
            "#10101Fはい、どうやら\x01",
            "手荷物の中に乗車チケットが\x01",
            "見当たらないのですが。\x02\x03",

            "心当たりはありますかね？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_65C5")

    label("loc_654B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_65C5")

    #C0166
    ChrTalk(
        0x105,
        (
            "#10304Fああ、どうやら\x01",
            "手荷物の中に乗車チケットが\x01",
            "ないみたいなんだけど。\x02\x03",

            "#10302F心当たりはあるかい？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_65C5")

    OP_63(0x8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0167
    ChrTalk(
        0x8,
        "チ、チケットがないじゃと！？\x02",
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0x8,
        (
            "そんなはずはない、\x01",
            "ちゃんとカバンの中に――\x02",
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
        "……ない、ない、どこにもない！\x02",
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0x8,
        "服のポケットか？　いやしかし――\x02",
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0x8,
        (
            "す、すまんが、\x01",
            "ちょっと待っていてくれんか。\x02",
        )
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0x8,
        (
            "絶対にあるはずなんじゃ。\x01",
            "必ず探し出してみせるからの！\x02",
        )
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0x101,
        (
            "#00005Fは、はい……\x01",
            "ではまた改めて伺います。\x02\x03",

            "#00003F（仕方ない、この人は\x01",
            "  後回しにして臨検を続けるか。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1CA, 1)
    OP_29(0x79, 0x1, 0x8)
    ClearChrFlags(0x8, 0x10)
    SetChrSubChip(0x8, 0x0)
    EventEnd(0x5)
    Return()

    # Function_25_60E4 end

    def Function_26_67A1(): pass

    label("Function_26_67A1")

    ModifyEventFlags(0, 3, 0x80)
    SetScenarioFlags(0x158, 6)
    Return()

    # Function_26_67A1 end

    def Function_27_67AA(): pass

    label("Function_27_67AA")

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
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_6892")
    Jump("loc_68DC")

    label("loc_6892")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_68B2")
    OP_52(0x12, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_68DC")

    label("loc_68B2")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_68D2")
    OP_52(0x12, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_68DC")

    label("loc_68D2")

    OP_52(0x12, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_68DC")

    OP_52(0x12, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x12, 0x10)
    OP_0D()

    #C0174
    ChrTalk(
        0x101,
        (
            "#00000F失礼します、\x01",
            "臨検官補佐の者です。\x02\x03",

            "お手数ですが、\x01",
            "手荷物と入国申請書を\x01",
            "確認させていただけますか？\x02",
        )
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0x12,
        (
            "ふぅ、そんなこと言って\x01",
            "私に断る権利なんてないんでしょ？\x02",
        )
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0x12,
        (
            "だったら、いちいち\x01",
            "確認なんて取らないで\x01",
            "早く済ませてくださるかしら。\x02",
        )
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0x101,
        "#00006Fはぁ、すみません。\x02",
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
            "#00004F――手荷物、入国申請書ともに\x01",
            "確認できました。\x01",
            "ご協力ありがとうございます。\x02",
        )
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0x12,
        (
            "……ふぅ、だから\x01",
            "そのお礼の言葉もいらないのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0x12,
        (
            "用事はもうないんでしょ？\x01",
            "だったら早く行ってちょうだい。\x02",
        )
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0x101,
        "#00005Fえ、ええ、失礼します。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6B6B")

    #C0182
    ChrTalk(
        0x102,
        (
            "#00106F（ふう、この仕事は\x01",
            "  なかなか神経を使うわね。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6CB7")

    label("loc_6B6B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6BB8")

    #C0183
    ChrTalk(
        0x103,
        (
            "#00206F（ふぅ……\x01",
            "  この仕事は神経を使いますね。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6CB7")

    label("loc_6BB8")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6C09")

    #C0184
    ChrTalk(
        0x104,
        (
            "#00306F（ふぅ、この仕事も\x01",
            "  なかなか神経を使うのな。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6CB7")

    label("loc_6C09")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6C5A")

    #C0185
    ChrTalk(
        0x109,
        (
            "#10106F（ふぅ、なかなか\x01",
            "  神経を使う仕事かもですね。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6CB7")

    label("loc_6C5A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6CB7")

    #C0186
    ChrTalk(
        0x105,
        (
            "#10304F（フフ、臨検官ってのも\x01",
            "  なかなかストレスの\x01",
            "  溜まる仕事だね。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6CB7")

    OP_5A()
    SetScenarioFlags(0x1CB, 0)
    OP_29(0x79, 0x1, 0x9)
    ClearChrFlags(0x12, 0x10)
    SetChrSubChip(0x12, 0x0)
    EventEnd(0x5)
    Return()

    # Function_27_67AA end

    def Function_28_6CCD(): pass

    label("Function_28_6CCD")

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
            "うふふ、やっぱり\x01",
            "《アイゼングラーフ号》は\x01",
            "他の列車とは格が違うわぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0x11,
        (
            "じゅるり……\x01",
            "おっと、いけないいけない。\x02",
        )
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0x101,
        (
            "#00006F（よ、よだれ……？）\x02\x03",

            "#00000Fすみません、\x01",
            "臨検官補佐の者ですが。\x02",
        )
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0x11,
        (
            "あー、アタシいま\x01",
            "列車ウォッチングに忙しいの。\x02",
        )
    )

    CloseMessageWindow()

    #C0191
    ChrTalk(
        0x11,
        (
            "申請書ならカバンに入ってるから、\x01",
            "気兼ねなく臨検しちゃっていいわよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0x101,
        (
            "#00003Fわ、分かりました。\x01",
            "そういうことなら……\x02",
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
            "#00004F――手荷物、入国申請書ともに\x01",
            "確認できました。\x01",
            "ご協力ありがとうございます。\x02",
        )
    )

    CloseMessageWindow()

    #C0194
    ChrTalk(
        0x11,
        (
            "ぶつぶつ……\x01",
            "出発まであと何分くらいかしら？\x02",
        )
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0x11,
        "ああん、名残惜しいわねっ……！\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6FA8")

    #C0196
    ChrTalk(
        0x102,
        (
            "#00103F（……ず、随分\x01",
            "  集中しているみたいね。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_70BB")

    label("loc_6FA8")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6FFD")

    #C0197
    ChrTalk(
        0x103,
        (
            "#00203F（……とうとう、\x01",
            "  一度も振り向きませんでしたね。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_70BB")

    label("loc_6FFD")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7039")

    #C0198
    ChrTalk(
        0x104,
        "#00306F（……聞いちゃいねえな。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_70BB")

    label("loc_7039")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7082")

    #C0199
    ChrTalk(
        0x109,
        (
            "#10106F（……相当、\x01",
            "  列車が好きなんですね。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_70BB")

    label("loc_7082")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_70BB")

    #C0200
    ChrTalk(
        0x105,
        "#10302F（フフ、聞いちゃいないね。）\x02",
    )

    CloseMessageWindow()

    label("loc_70BB")

    OP_5A()
    SetScenarioFlags(0x1CA, 7)
    OP_29(0x79, 0x1, 0xA)
    EventEnd(0x5)
    Return()

    # Function_28_6CCD end

    def Function_29_70C8(): pass

    label("Function_29_70C8")

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
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_71B0")
    Jump("loc_71FA")

    label("loc_71B0")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_71D0")
    OP_52(0xF, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_71FA")

    label("loc_71D0")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_71F0")
    OP_52(0xF, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_71FA")

    label("loc_71F0")

    OP_52(0xF, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_71FA")

    OP_52(0xF, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xF, 0x10)
    OP_0D()

    #C0201
    ChrTalk(
        0x101,
        "#00000Fえっと、臨検官補佐の者ですが……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0202
    ChrTalk(
        0x101,
        (
            "#00005F（このスーツは……\x01",
            "  もしかして『黒月』の社員か？）\x02",
        )
    )

    CloseMessageWindow()

    #C0203
    ChrTalk(
        0xF,
        "ふむ、なにか問題でも？\x02",
    )

    CloseMessageWindow()
    OP_4B(0x10, 0xFF)
    Sleep(300)
    OP_93(0x10, 0x5A, 0x1F4)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_78E2")
    OP_29(0x79, 0x1, 0xB)

    #C0204
    ChrTalk(
        0x10,
        "ん？　どうかしたか？\x02",
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
        "#00011F――って、シン？\x02",
    )

    CloseMessageWindow()

    #C0206
    ChrTalk(
        0x10,
        (
            "――そういうお前は、\x01",
            "特務支援課の！\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_73D3")

    #C0207
    ChrTalk(
        0x10,
        (
            "それに、エリィお姉さんまで\x01",
            "一緒とは！\x02",
        )
    )

    CloseMessageWindow()

    #C0208
    ChrTalk(
        0x102,
        "#00102Fふふ、こんにちは、シン君。\x02",
    )

    CloseMessageWindow()

    label("loc_73D3")


    #C0209
    ChrTalk(
        0x10,
        (
            "だが、こんなところで\x01",
            "いったい何をしているんだ？\x02",
        )
    )

    CloseMessageWindow()

    #C0210
    ChrTalk(
        0x101,
        (
            "#00000Fああ、特務支援課の仕事で\x01",
            "臨検官の仕事を手伝っているんだ。\x02\x03",

            "だから手荷物と入国申請書を\x01",
            "確認したいんだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0211
    ChrTalk(
        0x10,
        (
            "なるほど、支援課ってのは\x01",
            "そんな仕事もするんだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0212
    ChrTalk(
        0x10,
        (
            "まあいい、そういうことなら\x01",
            "早く済ませてくれ。\x02",
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
            "#00004F――よし。\x01",
            "手荷物、入国申請書ともに\x01",
            "確認完了だ。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_75F6")

    #C0214
    ChrTalk(
        0x102,
        "#00100F協力してくれてありがとうね。\x02",
    )

    CloseMessageWindow()

    #C0215
    ChrTalk(
        0x10,
        (
            "ふふ、お姉さんのためなら\x01",
            "これくらい。\x02",
        )
    )

    CloseMessageWindow()

    #C0216
    ChrTalk(
        0x10,
        "いつか必ずまたお会いしましょうね！\x02",
    )

    CloseMessageWindow()

    #C0217
    ChrTalk(
        0x102,
        "#00109Fええ、楽しみにしてるわね。\x02",
    )

    CloseMessageWindow()
    Jump("loc_78DD")

    label("loc_75F6")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_770E")

    #C0218
    ChrTalk(
        0x103,
        "#00200Fご協力ありがとうございます。\x02",
    )

    CloseMessageWindow()

    #C0219
    ChrTalk(
        0x10,
        (
            "（フム、支援課には\x01",
            "  こんな少女もいるんだな。）\x02",
        )
    )

    CloseMessageWindow()

    #C0220
    ChrTalk(
        0x103,
        "#00200F……わたしの顔に何か？\x02",
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
        "い、いや、何でもない！\x02",
    )

    CloseMessageWindow()

    #C0222
    ChrTalk(
        0x10,
        "――ではまたな。\x02",
    )

    CloseMessageWindow()

    #C0223
    ChrTalk(
        0x101,
        "#00009Fああ、シンも元気でな。\x02",
    )

    CloseMessageWindow()
    Jump("loc_78DD")

    label("loc_770E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_77AC")

    #C0224
    ChrTalk(
        0x104,
        "#00300F協力してくれてありがとな。\x02",
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0x10,
        (
            "フン、別に当然のことを\x01",
            "しただけだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0x10,
        "――ではまたな。\x02",
    )

    CloseMessageWindow()

    #C0227
    ChrTalk(
        0x101,
        "#00009Fああ、シンも元気でな。\x02",
    )

    CloseMessageWindow()
    Jump("loc_78DD")

    label("loc_77AC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_784A")

    #C0228
    ChrTalk(
        0x109,
        "#10100F協力してくれてありがとね。\x02",
    )

    CloseMessageWindow()

    #C0229
    ChrTalk(
        0x10,
        (
            "フン、別に当然のことを\x01",
            "しただけだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0230
    ChrTalk(
        0x10,
        "――ではまたな。\x02",
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0x101,
        "#00009Fああ、シンも元気でな。\x02",
    )

    CloseMessageWindow()
    Jump("loc_78DD")

    label("loc_784A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_78DD")

    #C0232
    ChrTalk(
        0x105,
        "#10300Fご協力に感謝するよ。\x02",
    )

    CloseMessageWindow()

    #C0233
    ChrTalk(
        0x10,
        (
            "フン、別に当然のことを\x01",
            "しただけだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0234
    ChrTalk(
        0x10,
        "――ではまたな。\x02",
    )

    CloseMessageWindow()

    #C0235
    ChrTalk(
        0x101,
        "#00009Fああ、シンも元気でな。\x02",
    )

    CloseMessageWindow()

    label("loc_78DD")

    Jump("loc_7FEB")

    label("loc_78E2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_7C0D")
    OP_29(0x79, 0x1, 0xB)

    #C0236
    ChrTalk(
        0x10,
        "ん？　どうかしたか？\x02",
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
        "#00005F――って、君は黒月の？\x02",
    )

    CloseMessageWindow()

    #C0238
    ChrTalk(
        0x10,
        (
            "――そういうお前は、\x01",
            "特務支援課の！\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7A26")

    #C0239
    ChrTalk(
        0x10,
        (
            "それに、エリィお姉さんまで\x01",
            "一緒とは！\x02",
        )
    )

    CloseMessageWindow()

    #C0240
    ChrTalk(
        0x102,
        "#00102Fふふ、こんにちは、シン君。\x02",
    )

    CloseMessageWindow()

    #C0241
    ChrTalk(
        0x10,
        "え、ええ……\x02",
    )

    CloseMessageWindow()

    #C0242
    ChrTalk(
        0x10,
        "で、一体なにをしてるんだ？\x02",
    )

    CloseMessageWindow()
    Jump("loc_7A48")

    label("loc_7A26")


    #C0243
    ChrTalk(
        0x10,
        "だが、一体なにをしてるんだ？\x02",
    )

    CloseMessageWindow()

    label("loc_7A48")


    #C0244
    ChrTalk(
        0x101,
        (
            "#00000Fああ、特務支援課の仕事で\x01",
            "臨検官の仕事を手伝っているんだ。\x02\x03",

            "だから手荷物と入国申請書を\x01",
            "確認したいんだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0245
    ChrTalk(
        0x10,
        (
            "なるほど、支援課ってのは\x01",
            "そんな仕事もするんだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0246
    ChrTalk(
        0x10,
        (
            "まあいい、そういうことなら\x01",
            "早く済ませてくれ。\x02",
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
            "#00004F――よし。\x01",
            "手荷物、入国申請書ともに\x01",
            "確認完了だ。\x02\x03",

            "協力してくれてありがとな。\x02",
        )
    )

    CloseMessageWindow()

    #C0248
    ChrTalk(
        0x10,
        (
            "フン、別に当然のことを\x01",
            "しただけだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0249
    ChrTalk(
        0x10,
        "用が済んだらさっさと行け。\x02",
    )

    CloseMessageWindow()

    #C0250
    ChrTalk(
        0x101,
        "#00006Fあ、ああ……失礼するよ。\x02",
    )

    CloseMessageWindow()
    Jump("loc_7FEB")

    label("loc_7C0D")


    #N0251
    NpcTalk(
        0x10,
        "男の子",
        "ん？　どうかしたか？\x02",
    )

    CloseMessageWindow()
    OP_29(0x79, 0x1, 0xC)

    #C0252
    ChrTalk(
        0x101,
        (
            "#00000Fえっと、臨検官補佐の者です。\x02\x03",

            "お手数ですが、\x01",
            "手荷物と入国申請書を\x01",
            "確認させていただけますか？\x02",
        )
    )

    CloseMessageWindow()

    #C0253
    ChrTalk(
        0xF,
        "ええ、もちろん構いませんよ。\x02",
    )

    CloseMessageWindow()

    #N0254
    NpcTalk(
        0x10,
        "男の子",
        "あー、ただしさっさと済ませろよ。\x02",
    )

    CloseMessageWindow()

    #C0255
    ChrTalk(
        0x101,
        "#00006Fは、はぁ……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7D6C")

    #C0256
    ChrTalk(
        0x102,
        (
            "#00105F（この子も黒月の関係者なのかしら？\x01",
            "  何やら態度が随分大きいけど……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7F0D")

    label("loc_7D6C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7DD5")

    #C0257
    ChrTalk(
        0x103,
        (
            "#00205F（この子も黒月の関係者でしょうか？\x01",
            "  随分、態度が大きいようですが……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7F0D")

    label("loc_7DD5")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7E3E")

    #C0258
    ChrTalk(
        0x104,
        (
            "#00303F（この小僧も黒月の関係者なのか？\x01",
            "  なんか、やたらと態度がでけえが……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7F0D")

    label("loc_7E3E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7EAB")

    #C0259
    ChrTalk(
        0x109,
        (
            "#10105F（この子も黒月の関係者なんですかね？\x01",
            "  随分、態度が大きいみたいですが……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7F0D")

    label("loc_7EAB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7F0D")

    #C0260
    ChrTalk(
        0x105,
        (
            "#10304F（この子も黒月の関係者なのかな？\x01",
            "  随分、態度が大きいようだけど……）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7F0D")

    FadeToDark(500, 0, -1)
    OP_0D()
    Sleep(1000)
    FadeToBright(500, 0)
    OP_0D()

    #C0261
    ChrTalk(
        0x101,
        (
            "#00004F――手荷物、入国申請書ともに\x01",
            "確認できました。\x01",
            "ご協力ありがとうございます。\x02",
        )
    )

    CloseMessageWindow()

    #C0262
    ChrTalk(
        0xF,
        "ああいえ、どうしたしまして。\x02",
    )

    CloseMessageWindow()

    #N0263
    NpcTalk(
        0x10,
        "男の子",
        (
            "フン、用が済んだら\x01",
            "さっさと行くんだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0264
    ChrTalk(
        0x101,
        "#00006Fあ、ああ……\x02",
    )

    CloseMessageWindow()

    label("loc_7FEB")

    OP_5A()
    SetScenarioFlags(0x1CA, 6)
    OP_4C(0x10, 0xFF)
    OP_93(0x10, 0x10E, 0x0)
    ClearChrFlags(0xF, 0x10)
    SetChrSubChip(0xF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_29_70C8 end

    def Function_30_8006(): pass

    label("Function_30_8006")

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
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_80EE")
    Jump("loc_8138")

    label("loc_80EE")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_810E")
    OP_52(0xD, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8138")

    label("loc_810E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_812E")
    OP_52(0xD, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8138")

    label("loc_812E")

    OP_52(0xD, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_8138")

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
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_81EE")
    Jump("loc_8238")

    label("loc_81EE")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_820E")
    OP_52(0xE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8238")

    label("loc_820E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_822E")
    OP_52(0xE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8238")

    label("loc_822E")

    OP_52(0xE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_8238")

    OP_52(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xE, 0x10)
    OP_0D()

    #C0265
    ChrTalk(
        0x101,
        (
            "#00000Fあの、臨検官補佐の者です。\x02\x03",

            "お手数ですが、\x01",
            "手荷物と入国申請書を\x01",
            "確認させていただけますか？\x02",
        )
    )

    CloseMessageWindow()

    #C0266
    ChrTalk(
        0xD,
        (
            "え、なんでそんなことを\x01",
            "させなきゃいけないの？\x02",
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
            "お、おい――\x01",
            "臨検官さんに何言ってんだよ！\x02",
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
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_83D4")
    Jump("loc_841E")

    label("loc_83D4")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_83F4")
    OP_52(0xE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_841E")

    label("loc_83F4")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8414")
    OP_52(0xE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_841E")

    label("loc_8414")

    OP_52(0xE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_841E")

    OP_52(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xE, 0x10)

    #C0268
    ChrTalk(
        0xE,
        (
            "すみません、\x01",
            "うちの妹がとんだ無礼を。\x02",
        )
    )

    CloseMessageWindow()

    #C0269
    ChrTalk(
        0xE,
        (
            "こいつほんとバカなんで\x01",
            "許してやってください。\x02",
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
            "バカとは何よ、バカとは！\x01",
            "だいたいお兄ちゃんは――\x02",
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
        "#00006F（えっと、始めていいんだよな？）\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8591")

    #C0272
    ChrTalk(
        0x102,
        "#00100F（ええ、だと思うわよ。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_8672")

    label("loc_8591")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_85CB")

    #C0273
    ChrTalk(
        0x103,
        "#00200F（ええ、だと思います。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_8672")

    label("loc_85CB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8603")

    #C0274
    ChrTalk(
        0x104,
        "#00300F（ああ、だと思うぜ。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_8672")

    label("loc_8603")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_863D")

    #C0275
    ChrTalk(
        0x109,
        "#10100F（はい、だと思います。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_8672")

    label("loc_863D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8672")

    #C0276
    ChrTalk(
        0x105,
        "#10300F（フフ、だと思うけど。）\x02",
    )

    CloseMessageWindow()

    label("loc_8672")

    FadeToDark(500, 0, -1)
    OP_0D()
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xD, 0x10)
    TurnDirection(0xD, 0x0, 0)
    OP_52(0xD, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_870E")
    Jump("loc_8758")

    label("loc_870E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_872E")
    OP_52(0xD, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8758")

    label("loc_872E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_874E")
    OP_52(0xD, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8758")

    label("loc_874E")

    OP_52(0xD, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_8758")

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
            "#00004F――手荷物、入国申請書ともに\x01",
            "確認できました。\x01",
            "ご協力ありがとうございます。\x02",
        )
    )

    CloseMessageWindow()

    #C0278
    ChrTalk(
        0xE,
        (
            "いえいえ、こちらこそ\x01",
            "妹がご面倒をおかけしました。\x02",
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
            "なにそれ、それを言うなら\x01",
            "お兄ちゃんの方が――\x02",
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
        "#00003F（早く退散した方が良さそうだな。）\x02",
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

    # Function_30_8006 end

    def Function_31_88EB(): pass

    label("Function_31_88EB")

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
        "#00000Fさてと、これで全員確認したか。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8A02")

    #C0282
    ChrTalk(
        0x102,
        (
            "#00105Fそういえば、４両目の\x01",
            "おじいさんのチケットを\x01",
            "まだ確認していなかったわね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8BA1")

    label("loc_8A02")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8A6E")

    #C0283
    ChrTalk(
        0x103,
        (
            "#00205Fそういえば、４両目の\x01",
            "おじいさんのチケットを\x01",
            "まだ確認していませんでしたね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8BA1")

    label("loc_8A6E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8AD2")

    #C0284
    ChrTalk(
        0x104,
        (
            "#00305Fそういえば、４両目の\x01",
            "じいさんのチケットを\x01",
            "まだ確認してなかったな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8BA1")

    label("loc_8AD2")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8B3E")

    #C0285
    ChrTalk(
        0x109,
        (
            "#10105Fそういえば、４両目の\x01",
            "おじいさんのチケットを\x01",
            "まだ確認していませんでしたね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8BA1")

    label("loc_8B3E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8BA1")

    #C0286
    ChrTalk(
        0x105,
        (
            "#10305Fそういえば、４両目の\x01",
            "おじいさんのチケットを\x01",
            "まだ確認していなかったね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8BA1")


    #C0287
    ChrTalk(
        0x101,
        (
            "#00003Fそうだな、じゃあ\x01",
            "さっそく確認しに戻――\x02",
        )
    )

    CloseMessageWindow()
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    #C0288
    ChrTalk(
        0x8,
        "――わ、わしのチケットを返せ！\x02",
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8C6B")

    #C0289
    ChrTalk(
        0x102,
        "#00101F――ロイド！\x02",
    )

    CloseMessageWindow()
    Jump("loc_8D26")

    label("loc_8C6B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8C9D")

    #C0290
    ChrTalk(
        0x103,
        "#00201F――ロイドさん！\x02",
    )

    CloseMessageWindow()
    Jump("loc_8D26")

    label("loc_8C9D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8CCB")

    #C0291
    ChrTalk(
        0x104,
        "#00301F――ロイド！\x02",
    )

    CloseMessageWindow()
    Jump("loc_8D26")

    label("loc_8CCB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8CFD")

    #C0292
    ChrTalk(
        0x109,
        "#10101F――ロイドさん！\x02",
    )

    CloseMessageWindow()
    Jump("loc_8D26")

    label("loc_8CFD")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8D26")

    #C0293
    ChrTalk(
        0x105,
        "#10301F――ロイド！\x02",
    )

    CloseMessageWindow()

    label("loc_8D26")


    #C0294
    ChrTalk(
        0x101,
        "#00000Fああ、すぐに向かおう！\x02",
    )

    CloseMessageWindow()
    Call(0, 32)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_8D60")
    Call(0, 34)
    Jump("loc_8D63")

    label("loc_8D60")

    Call(0, 33)

    label("loc_8D63")

    EventEnd(0x5)
    Return()

    # Function_31_88EB end

    def Function_32_8D66(): pass

    label("Function_32_8D66")

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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8E98")
    SetChrPos(0x102, -480, 0, 8210, 180)
    Jump("loc_8F2B")

    label("loc_8E98")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8EBE")
    SetChrPos(0x103, -480, 0, 8210, 180)
    Jump("loc_8F2B")

    label("loc_8EBE")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8EE4")
    SetChrPos(0x104, -480, 0, 8210, 180)
    Jump("loc_8F2B")

    label("loc_8EE4")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8F0A")
    SetChrPos(0x109, -480, 0, 8210, 180)
    Jump("loc_8F2B")

    label("loc_8F0A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8F2B")
    SetChrPos(0x105, -480, 0, 8210, 180)

    label("loc_8F2B")

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
            "だから、お前ら２人のどちらかに\x01",
            "決まっておると言っておるんじゃ！\x02",
        )
    )

    CloseMessageWindow()

    #C0296
    ChrTalk(
        0x8,
        (
            "さあ、どっちだ！\x01",
            "さっさと白状するがいい！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(1000)

    def lambda_8FDF():
        OP_95(0x101, 460, 0, 3200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8FDF)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9023")

    def lambda_9009():
        OP_95(0x102, -480, 0, 3600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_9009)
    Jump("loc_90DA")

    label("loc_9023")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9052")

    def lambda_9038():
        OP_95(0x103, -480, 0, 3600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_9038)
    Jump("loc_90DA")

    label("loc_9052")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9081")

    def lambda_9067():
        OP_95(0x104, -480, 0, 3600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_9067)
    Jump("loc_90DA")

    label("loc_9081")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_90B0")

    def lambda_9096():
        OP_95(0x109, -480, 0, 3600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_9096)
    Jump("loc_90DA")

    label("loc_90B0")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_90DA")

    def lambda_90C5():
        OP_95(0x105, -480, 0, 3600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_90C5)

    label("loc_90DA")

    OP_68(70, 1000, 2830, 3000)
    MoveCamera(315, 25, 0, 3000)
    OP_6E(500, 3000)
    SetCameraDistance(16500, 3000)
    OP_6F(0x79)

    #C0297
    ChrTalk(
        0x101,
        "#00005Fあの、何があったんですか？\x02",
    )

    CloseMessageWindow()

    #C0298
    ChrTalk(
        0xC,
        "あ、さっきの臨検官の人。\x02",
    )

    CloseMessageWindow()

    #C0299
    ChrTalk(
        0x9,
        (
            "どうもこうも、\x01",
            "この老人がイチャモンを――\x02",
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
            "何を――\x01",
            "よくもヌケヌケと！\x02",
        )
    )

    CloseMessageWindow()

    #C0301
    ChrTalk(
        0x101,
        "#00011Fお、落ち着いてください！\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_922E")

    #C0302
    ChrTalk(
        0x102,
        (
            "#00101Fあの、まずは話を\x01",
            "聞かせてもらっていいですか？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9365")

    label("loc_922E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_927D")

    #C0303
    ChrTalk(
        0x103,
        (
            "#00200Fあの、まずは話を\x01",
            "聞いてもよろしいでしょうか？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9365")

    label("loc_927D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_92CC")

    #C0304
    ChrTalk(
        0x104,
        (
            "#00303Fとりあえず、まずは\x01",
            "話を聞かせちゃくれねえか？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9365")

    label("loc_92CC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_931D")

    #C0305
    ChrTalk(
        0x109,
        (
            "#10101Fとりあえず、まずは\x01",
            "話を聞かせてもらえませんか？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9365")

    label("loc_931D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9365")

    #C0306
    ChrTalk(
        0x105,
        (
            "#10304Fとにかく、まずは\x01",
            "話を聞かせてもらえるかな？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9365")

    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x101, 550, 0, 1100, 180)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_93A7")
    SetChrPos(0x102, -540, 0, 1100, 180)
    Jump("loc_943A")

    label("loc_93A7")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_93CD")
    SetChrPos(0x103, -540, 0, 1100, 180)
    Jump("loc_943A")

    label("loc_93CD")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_93F3")
    SetChrPos(0x104, -540, 0, 1100, 180)
    Jump("loc_943A")

    label("loc_93F3")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9419")
    SetChrPos(0x109, -540, 0, 1100, 180)
    Jump("loc_943A")

    label("loc_9419")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_943A")
    SetChrPos(0x105, -540, 0, 1100, 180)

    label("loc_943A")

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
            "#00003Fなるほど、おじいさんが\x01",
            "購入したチケットは４両目指定の\x01",
            "オレド自治州行き……\x02\x03",

            "そして、それと全く同じチケットを\x01",
            "持っている人がこの車両に２人いた……\x02\x03",

            "#00001Fつまり、その２人のどちらかが\x01",
            "チケットを盗んだ可能性がある――\x01",
            "そう言いたいわけですね？\x02",
        )
    )

    CloseMessageWindow()

    #C0308
    ChrTalk(
        0x8,
        "ああ、その通りじゃ。\x02",
    )

    CloseMessageWindow()

    #C0309
    ChrTalk(
        0x8,
        (
            "――とにかく、わしが\x01",
            "チケットを持ってホームに\x01",
            "入ったことは紛れもない事実。\x02",
        )
    )

    CloseMessageWindow()

    #C0310
    ChrTalk(
        0x8,
        (
            "そして、この短い時間の間に\x01",
            "チケットをなくすわけがない！\x02",
        )
    )

    CloseMessageWindow()

    #C0311
    ChrTalk(
        0x8,
        (
            "それこそ、盗難の被害にでも\x01",
            "遭わん限りな。\x02",
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
            "#00006Fえっと、流石に断定は\x01",
            "できないと思いますが……\x02",
        )
    )

    CloseMessageWindow()

    #C0313
    ChrTalk(
        0x9,
        (
            "いいぞいいぞ、\x01",
            "もっと遠慮なく言ってやれ！\x02",
        )
    )

    CloseMessageWindow()

    #C0314
    ChrTalk(
        0x9,
        "あんたがボケてるだけだってな！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x9, 500)

    #C0315
    ChrTalk(
        0x8,
        "貴様、まだ言うか……！\x02",
    )

    CloseMessageWindow()

    #C0316
    ChrTalk(
        0x101,
        (
            "#00006Fとりあえず――\x01",
            "お２人とも落ち着いてください。\x02\x03",

            "#00001Fとにかく、\x01",
            "感情をぶつけ合うだけでは\x01",
            "収まるものも収まりません。\x02\x03",

            "#00003Fなので、チケットを持つお２人に\x01",
            "軽く質問させてください。\x02\x03",

            "#00001F目的地を目指す理由――\x01",
            "最低限それだけ\x01",
            "聞かせていただけますか？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0317
    ChrTalk(
        0xC,
        "も、目的地を目指す理由？\x02",
    )

    CloseMessageWindow()

    #C0318
    ChrTalk(
        0x9,
        (
            "フン、それで\x01",
            "潔白を証明できるのかね？\x02",
        )
    )

    CloseMessageWindow()

    #C0319
    ChrTalk(
        0x101,
        (
            "#00000Fええ、仮にチケットが本当に\x01",
            "盗難物だとしたら犯人にとって\x01",
            "希望の目的地でない可能性があります。\x02\x03",

            "#00004Fその場合、犯人なら\x01",
            "何らかのボロを出すかもしれません。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_99C3")

    #C0320
    ChrTalk(
        0x102,
        (
            "#00105Fなるほど、\x01",
            "確かにその可能性はあるわね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9AE2")

    label("loc_99C3")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9A0E")

    #C0321
    ChrTalk(
        0x103,
        (
            "#00203Fなるほど、\x01",
            "確かにその可能性はありますね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9AE2")

    label("loc_9A0E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9A55")

    #C0322
    ChrTalk(
        0x104,
        (
            "#00305Fなるほど、\x01",
            "確かにその可能性はあるな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9AE2")

    label("loc_9A55")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9AA0")

    #C0323
    ChrTalk(
        0x109,
        (
            "#10105Fなるほど、\x01",
            "確かにその可能性はありますね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9AE2")

    label("loc_9AA0")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9AE2")

    #C0324
    ChrTalk(
        0x105,
        (
            "#10302Fなるほど、\x01",
            "確かにその可能性はあるね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9AE2")


    #C0325
    ChrTalk(
        0x8,
        (
            "ふむ、なら善は急げじゃな。\x01",
            "ほれっ、さっさと答えるんじゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0326
    ChrTalk(
        0x9,
        "フン、そのくらいお安い御用だ。\x02",
    )

    CloseMessageWindow()

    #C0327
    ChrTalk(
        0x9,
        (
            "私は商人でね。\x01",
            "これからオレド自治州で\x01",
            "大事な契約があるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0328
    ChrTalk(
        0x9,
        (
            "ちなみにこれが契約書――\x01",
            "取り引き先はオレドにある\x01",
            "《流星#4Rりゅうしん#商会》だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0329
    ChrTalk(
        0x9,
        (
            "そんな人間がチケットを盗むなんて、\x01",
            "セコイことをするわけがないだろう？\x02",
        )
    )

    CloseMessageWindow()

    #C0330
    ChrTalk(
        0x8,
        "ぐ、ぐぬぬ……\x02",
    )

    CloseMessageWindow()

    #C0331
    ChrTalk(
        0x101,
        (
            "#00003F……なるほど。\x02\x03",

            "#00001Fちなみにあなたの方は？\x02",
        )
    )

    CloseMessageWindow()

    #C0332
    ChrTalk(
        0xC,
        (
            "え、えっと、僕は\x01",
            "オレド自治州が故郷なんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0333
    ChrTalk(
        0xC,
        "……里帰りは理由になりませんかね？\x02",
    )

    CloseMessageWindow()

    #C0334
    ChrTalk(
        0x101,
        (
            "#00003Fいえ、そんなことは……\x02\x03",

            "#00008F（う～ん、とりあえず聞いてはみたものの\x01",
            "  これだけじゃ判断が付かないな。）\x02",
        )
    )

    CloseMessageWindow()
    Return()

    # Function_32_8D66 end

    def Function_33_9D47(): pass

    label("Function_33_9D47")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9DA2")

    #C0335
    ChrTalk(
        0x102,
        (
            "#00103F（……どうやら、私たちに\x01",
            "  できるのはここまでみたいね。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9F1D")

    label("loc_9DA2")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9E05")

    #C0336
    ChrTalk(
        0x103,
        (
            "#00203F（……どうやら、わたしたちに\x01",
            "  できるのはここまでのようですね。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9F1D")

    label("loc_9E05")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9E62")

    #C0337
    ChrTalk(
        0x104,
        (
            "#00303F（……どうやら、俺たちに\x01",
            "  できるのはここまでみたいだな。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9F1D")

    label("loc_9E62")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9EC5")

    #C0338
    ChrTalk(
        0x109,
        (
            "#10103F（……どうやら、あたしたちに\x01",
            "  できるのはここまでみたいですね。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9F1D")

    label("loc_9EC5")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9F1D")

    #C0339
    ChrTalk(
        0x105,
        (
            "#10303F（……どうやら、僕たちに\x01",
            "  できるのはここまでみたいだね。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9F1D")


    #C0340
    ChrTalk(
        0x101,
        (
            "#00003F（そうだな……\x01",
            "  あとは本職のマーロウさんに\x01",
            "  報告するしかなさそうだ。）\x02\x03",

            "#00000Fあの、皆さんはしばらく\x01",
            "この場に待機していてください。\x02\x03",

            "今、上の者を呼んで来ますので。\x02",
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

    # Function_33_9D47 end

    def Function_34_9FF7(): pass

    label("Function_34_9FF7")

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
            "はは、面白い。\x01",
            "この車両にはウソツキがいるぞ！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_A0B4():
        OP_93(0x0, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_A0B4)

    def lambda_A0C1():
        OP_93(0x1, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_A0C1)
    OP_68(460, 1000, 5040, 3000)
    MoveCamera(315, 25, 0, 3000)
    OP_6E(500, 3000)
    SetCameraDistance(16210, 3000)

    def lambda_A0FC():
        OP_95(0x10, 460, 0, 5470, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_A0FC)

    def lambda_A116():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_A116)

    def lambda_A127():
        OP_95(0xF, -480, 0, 5970, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_A127)

    def lambda_A141():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF, 2, lambda_A141)
    Sleep(2000)
    Sound(100, 0, 100, 0)
    OP_71(0x2, 0x5, 0x0, 0x1, 0x8)
    OP_6F(0x79)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_A2AA")

    #C0342
    ChrTalk(
        0x101,
        (
            "#00005F――シン？\x02\x03",

            "#00001Fちょ、ちょっと待てくれ。\x01",
            "臨検中は車両を移動しては\x01",
            "いけないって決まりが――\x02",
        )
    )

    CloseMessageWindow()

    #C0343
    ChrTalk(
        0x10,
        (
            "フン、既に臨検は\x01",
            "一通り済んでるんだろ？\x01",
            "それくらい融通を利かせろ。\x02",
        )
    )

    CloseMessageWindow()

    #C0344
    ChrTalk(
        0x101,
        (
            "#00006Fいやでも……\x01",
            "はぁ、まあいいか。\x02",
        )
    )

    CloseMessageWindow()

    #C0345
    ChrTalk(
        0x10,
        (
            "とりあえず、なんか面白いことに\x01",
            "なっているみたいだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0346
    ChrTalk(
        0x10,
        "ボクも参加してやるぞ！\x02",
    )

    CloseMessageWindow()
    Jump("loc_A312")

    label("loc_A2AA")


    #C0347
    ChrTalk(
        0x101,
        "#00005F――シン？\x02",
    )

    CloseMessageWindow()

    #C0348
    ChrTalk(
        0x10,
        (
            "フフ、なんか面白いことに\x01",
            "なっているみたいだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0349
    ChrTalk(
        0x10,
        "ボクも参加してやるぞ！\x02",
    )

    CloseMessageWindow()

    label("loc_A312")


    #C0350
    ChrTalk(
        0x101,
        "#00005Fさ、参加って……\x02",
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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A3AD")
    SetChrPos(0x102, -540, 0, 2100, 135)
    Jump("loc_A440")

    label("loc_A3AD")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A3D3")
    SetChrPos(0x103, -540, 0, 2100, 135)
    Jump("loc_A440")

    label("loc_A3D3")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A3F9")
    SetChrPos(0x104, -540, 0, 2100, 135)
    Jump("loc_A440")

    label("loc_A3F9")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A41F")
    SetChrPos(0x109, -540, 0, 2100, 135)
    Jump("loc_A440")

    label("loc_A41F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A440")
    SetChrPos(0x105, -540, 0, 2100, 135)

    label("loc_A440")

    SetChrPos(0xF, 540, 0, 2500, 180)
    OP_93(0x8, 0x5A, 0x0)
    OP_0D()

    #C0351
    ChrTalk(
        0x101,
        (
            "#00001F……で、ウソツキってのは\x01",
            "一体どういうことなんだ？\x02",
        )
    )

    CloseMessageWindow()

    #C0352
    ChrTalk(
        0x10,
        (
            "ああ、ではまずは\x01",
            "そこの商人に答えてもらおう。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_A4CF():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A4CF)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A4F9")

    def lambda_A4EC():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A4EC)
    Jump("loc_A57C")

    label("loc_A4F9")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A51B")

    def lambda_A50E():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_A50E)
    Jump("loc_A57C")

    label("loc_A51B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A53D")

    def lambda_A530():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_A530)
    Jump("loc_A57C")

    label("loc_A53D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A55F")

    def lambda_A552():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_A552)
    Jump("loc_A57C")

    label("loc_A55F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A57C")

    def lambda_A574():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_A574)

    label("loc_A57C")


    #C0353
    ChrTalk(
        0x10,
        (
            "お前――さっき《流星商会》と\x01",
            "取り引きがあるって言ってたな？\x02",
        )
    )

    CloseMessageWindow()

    #C0354
    ChrTalk(
        0x10,
        "具体的にはどんな内容だ？\x02",
    )

    CloseMessageWindow()

    #C0355
    ChrTalk(
        0x9,
        (
            "はぁ、なんで私が\x01",
            "こんな子供のお遊戯に……\x02",
        )
    )

    CloseMessageWindow()

    #C0356
    ChrTalk(
        0x9,
        (
            "ああ、取り引きというのは\x01",
            "オレド自治州の珍しい野菜や\x01",
            "香辛料の買い付けだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0357
    ChrTalk(
        0x9,
        "オレドと言えば農業の盛んな場所――\x02",
    )

    CloseMessageWindow()

    #C0358
    ChrTalk(
        0x9,
        (
            "それに《流星商会》は\x01",
            "共和国の東方人街を取り仕切る\x01",
            "《黒月グループ》の系列会社――\x02",
        )
    )

    CloseMessageWindow()

    #C0359
    ChrTalk(
        0x9,
        "……疑う余地はないと思うんだが？\x02",
    )

    CloseMessageWindow()

    #C0360
    ChrTalk(
        0x10,
        (
            "フフ、キサマの言う通り確かに\x01",
            "オレドには《流星商会》がある。\x02",
        )
    )

    CloseMessageWindow()

    #C0361
    ChrTalk(
        0x10,
        (
            "だがあいにく――\x01",
            "まだまだ自治州内での足場を\x01",
            "かためている最中でな。\x02",
        )
    )

    CloseMessageWindow()

    #C0362
    ChrTalk(
        0x10,
        (
            "とても外部の人間と\x01",
            "取り引きなんてできるような\x01",
            "段階にはないぞ？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0363
    ChrTalk(
        0x9,
        (
            "なんだと？\x01",
            "なんでそんなことが分かるんだ？\x02",
        )
    )

    CloseMessageWindow()

    #C0364
    ChrTalk(
        0x10,
        "だってさ――どうする？\x02",
    )

    CloseMessageWindow()
    StopBGM(0xBB8)

    #C0365
    ChrTalk(
        0xF,
        "――ええ、お任せを。\x02",
    )

    CloseMessageWindow()

    #C0366
    ChrTalk(
        0xF,
        (
            "貴様、さっきから黙って\x01",
            "聞いていれば坊ちゃまに\x01",
            "対して失礼極まりない――！\x02",
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
            "#5Sええい、控えおろう――\x01",
            "この方は《黒月》長老のご令孫、\x01",
            "シン様にあらせられるぞ！#3S\x02",
        )
    )

    CloseMessageWindow()

    #C0368
    ChrTalk(
        0x9,
        "長老の孫～？　そんな冗談が……\x02",
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0369
    ChrTalk(
        0x9,
        (
            "あ、あんたが着ているスーツ……\x01",
            "確かに見覚えがある。\x02",
        )
    )

    CloseMessageWindow()

    #C0370
    ChrTalk(
        0x9,
        "そ、そんな……まさか本当に……\x02",
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x9)

    #C0371
    ChrTalk(
        0x10,
        "フフ、ようやく理解できたか？\x02",
    )

    CloseMessageWindow()

    #C0372
    ChrTalk(
        0x10,
        "ちなみに本当の目的はなんだ？\x02",
    )

    CloseMessageWindow()

    #C0373
    ChrTalk(
        0x9,
        "そ、それは……\x02",
    )

    CloseMessageWindow()

    #C0374
    ChrTalk(
        0x10,
        (
            "フン、まあいい。\x01",
            "あとで別室に行って\x01",
            "臨検官にすべてを話すんだな。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AA97")

    #C0375
    ChrTalk(
        0x102,
        "#00103F（……シン君、やるわね。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_AB96")

    label("loc_AA97")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AAD7")

    #C0376
    ChrTalk(
        0x103,
        "#00203F（……この子、すごいですね。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_AB96")

    label("loc_AAD7")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AB19")

    #C0377
    ChrTalk(
        0x104,
        "#00303F（……シンの奴、やりやがるな。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_AB96")

    label("loc_AB19")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AB59")

    #C0378
    ChrTalk(
        0x109,
        "#10105F（……すごいですね、シン君。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_AB96")

    label("loc_AB59")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AB96")

    #C0379
    ChrTalk(
        0x105,
        "#10304F（フフ、大したタマじゃないか。）\x02",
    )

    CloseMessageWindow()

    label("loc_AB96")


    #C0380
    ChrTalk(
        0x101,
        (
            "#00003F（ああ、なんていうか\x01",
            "  貫禄十分だな。）\x02",
        )
    )

    CloseMessageWindow()

    #C0381
    ChrTalk(
        0x10,
        "――で、次はお前だ。\x02",
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0382
    ChrTalk(
        0x101,
        "#00005Fシン……？\x02",
    )

    CloseMessageWindow()

    #C0383
    ChrTalk(
        0xC,
        "ぼ、僕ですか？\x02",
    )

    CloseMessageWindow()

    #C0384
    ChrTalk(
        0xC,
        (
            "犯人は嘘を付いていた\x01",
            "その男なんじゃ……\x02",
        )
    )

    CloseMessageWindow()

    #C0385
    ChrTalk(
        0x10,
        "フンッ、誰がそんなことを言った？\x02",
    )

    CloseMessageWindow()

    #C0386
    ChrTalk(
        0x10,
        (
            "ちょっとお前にも\x01",
            "聞いてみたいことがあってな。\x01",
            "確かオレドの出身なんだよな？\x02",
        )
    )

    CloseMessageWindow()

    #C0387
    ChrTalk(
        0xC,
        (
            "は、はい……\x01",
            "これから里帰りに……\x02",
        )
    )

    CloseMessageWindow()

    #C0388
    ChrTalk(
        0x10,
        "フム、ならこれは当然分かるな。\x02",
    )

    CloseMessageWindow()

    #C0389
    ChrTalk(
        0x10,
        (
            "オレド自治州は農業の他にも\x01",
            "秘境で有名な場所――\x02",
        )
    )

    CloseMessageWindow()

    #C0390
    ChrTalk(
        0x10,
        (
            "温泉なんてものも数多くあるが……\x01",
            "次の内、オレドにある温泉はどれだ？\x02",
        )
    )

    CloseMessageWindow()

    #C0391
    ChrTalk(
        0x10,
        (
            "①エルモ温泉\x01",
            "②パルム温泉\x01",
            "③オレド温泉。\x02",
        )
    )

    CloseMessageWindow()

    #C0392
    ChrTalk(
        0x10,
        "――さあ、答えろ。\x02",
    )

    CloseMessageWindow()

    #C0393
    ChrTalk(
        0xC,
        "はぁ……？\x02",
    )

    CloseMessageWindow()

    #C0394
    ChrTalk(
        0xC,
        (
            "え、ええと……\x01",
            "そんなの、③のオレド温泉に\x01",
            "決まってるじゃないですか。\x02",
        )
    )

    CloseMessageWindow()

    #C0395
    ChrTalk(
        0x10,
        (
            "……そうか。\x01",
            "フフ……フハハッ。\x02",
        )
    )

    CloseMessageWindow()

    #C0396
    ChrTalk(
        0x101,
        "#00005Fど、どういうことだ？\x02",
    )

    CloseMessageWindow()

    #C0397
    ChrTalk(
        0x10,
        (
            "お前、ボクを\x01",
            "コドモだと思って侮っただろ？\x02",
        )
    )

    CloseMessageWindow()

    #C0398
    ChrTalk(
        0x10,
        "オレド温泉～？\x02",
    )

    CloseMessageWindow()

    #C0399
    ChrTalk(
        0x10,
        (
            "そんなベタというか、\x01",
            "自治州そのものの名前が付いた\x01",
            "温泉なんてないぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0400
    ChrTalk(
        0x10,
        (
            "本当にオレドの人間なら\x01",
            "こう答えただろうな。\x01",
            "『その中に答えはない』って。\x02",
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
        "え……\x02",
    )

    CloseMessageWindow()

    #C0402
    ChrTalk(
        0x10,
        (
            "フフン、さらに\x01",
            "問題を出してやろうか？\x02",
        )
    )

    CloseMessageWindow()

    #C0403
    ChrTalk(
        0x10,
        (
            "もっとも、ボロが\x01",
            "次々出るだけだと思うがな。\x02",
        )
    )

    CloseMessageWindow()

    #C0404
    ChrTalk(
        0x10,
        "で、お前は本当はどこの出身なんだ？\x02",
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xC)

    #C0405
    ChrTalk(
        0xC,
        "え、ええっとそれは……\x02",
    )

    CloseMessageWindow()

    #C0406
    ChrTalk(
        0xC,
        (
            "あの、わざわざ言うことも\x01",
            "ないと思っていましたが、\x01",
            "実は僕、共和国出身なんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0407
    ChrTalk(
        0xC,
        (
            "でも今はオレドに家があって……\x01",
            "し、信じてください！\x02",
        )
    )

    CloseMessageWindow()

    #C0408
    ChrTalk(
        0x10,
        "フン、どうだかな。\x02",
    )

    CloseMessageWindow()
    StopBGM(0xBB8)
    TurnDirection(0x10, 0x101, 500)

    #C0409
    ChrTalk(
        0x10,
        (
            "――で、\x01",
            "特務支援課としてはどう見る？\x02",
        )
    )

    CloseMessageWindow()

    #C0410
    ChrTalk(
        0x10,
        (
            "内容はともかく、２人とも\x01",
            "ウソツキということが分かったが……\x02",
        )
    )

    CloseMessageWindow()

    #C0411
    ChrTalk(
        0x10,
        "チケット泥棒はどっちだ？\x02",
    )

    CloseMessageWindow()

    #C0412
    ChrTalk(
        0x101,
        "#00003Fあ、ああ……そうだな。\x02",
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
            "#1K商人と青年、チケット泥棒の\x01",
            "可能性が高いのは？\x07\x00\x02",
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
        (0, "loc_B26D"),
        (1, "loc_B48F"),
        (SWITCH_DEFAULT, "loc_B5D7"),
    )


    label("loc_B26D")

    OP_2C(0x79, 0x1)

    #C0414
    ChrTalk(
        0x101,
        (
            "#00003F商人さんの方かな。\x02\x03",

            "#00000Fこの人の方が、\x01",
            "色々と隠し事も多そうだし……\x02",
        )
    )

    CloseMessageWindow()

    #C0415
    ChrTalk(
        0x10,
        (
            "おい、お前……\x01",
            "ボクを失望させるなよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0416
    ChrTalk(
        0x10,
        "本当に真面目に考えてるのか？\x02",
    )

    CloseMessageWindow()

    #C0417
    ChrTalk(
        0x101,
        (
            "#00006Fあ、ああ……すまない。\x02\x03",

            "#00008F……そうか、ここは\x01",
            "消去法で考えるべきだな。\x02\x03",

            "#00001F商人さんが見せてくれた\x01",
            "架空の契約書……\x02\x03",

            "目的は分からないけど、\x01",
            "わざわざこんなものを\x01",
            "ご丁寧に用意してるんだ。\x02\x03",

            "#00003Fチケット泥棒なんて\x01",
            "軽犯罪を犯すというのも\x01",
            "不自然な印象だ。\x02\x03",

            "たとえ目的地が\x01",
            "オレドじゃなくても\x01",
            "途中下車だって可能だし……\x02\x03",

            "#00001Fとなると……\x01",
            "犯人はあなたですね？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B5D7")

    label("loc_B48F")

    OP_2C(0x79, 0x2)

    #C0418
    ChrTalk(
        0x101,
        (
            "#00003Fこっちの彼かな。\x02\x03",

            "#00001F商人さんが見せてくれた\x01",
            "架空の契約書……\x02\x03",

            "目的は分からないけど、\x01",
            "わざわざこんなものを\x01",
            "ご丁寧に用意してるんだ。\x02\x03",

            "#00003Fチケット泥棒なんて\x01",
            "軽犯罪を犯すというのも\x01",
            "不自然な印象だ。\x02\x03",

            "たとえ目的地が\x01",
            "オレドじゃなくても\x01",
            "途中下車だって可能だし……\x02\x03",

            "#00001Fとなると……\x01",
            "犯人はあなたですね？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B5D7")

    label("loc_B5D7")


    #C0419
    ChrTalk(
        0xC,
        "う、ううう……\x02",
    )

    CloseMessageWindow()

    #C0420
    ChrTalk(
        0x10,
        "フム、まあ合格点だな。\x02",
    )

    CloseMessageWindow()
    OP_93(0x10, 0xB4, 0x1F4)

    #C0421
    ChrTalk(
        0x10,
        (
            "おい、お前\x01",
            "これ以上しらを切っても\x01",
            "隠し通せることじゃないぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0422
    ChrTalk(
        0x10,
        (
            "オトコならこの場で\x01",
            "正直に白状してみせろ。\x02",
        )
    )

    CloseMessageWindow()

    #C0423
    ChrTalk(
        0xC,
        "#5Sみ、見逃してください！#3S\x02",
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

    def lambda_B73F():
        TurnDirection(0xFE, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_B73F)
    Sleep(50)

    def lambda_B74F():
        TurnDirection(0xFE, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_B74F)
    Sleep(300)

    #C0424
    ChrTalk(
        0x8,
        "な、なんじゃと！\x02",
    )

    CloseMessageWindow()

    #C0425
    ChrTalk(
        0x10,
        "おい、お前――\x02",
    )

    CloseMessageWindow()

    #C0426
    ChrTalk(
        0xC,
        (
            "は、母親が共和国の\x01",
            "病院に運ばれたんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0427
    ChrTalk(
        0xC,
        (
            "だからどうしても\x01",
            "病院に急がないと――！\x02",
        )
    )

    CloseMessageWindow()

    #C0428
    ChrTalk(
        0x101,
        "#00006Fえ、えっと……\x02",
    )

    CloseMessageWindow()

    #C0429
    ChrTalk(
        0x10,
        "いきなりでワケが分からん。\x02",
    )

    CloseMessageWindow()

    #C0430
    ChrTalk(
        0x10,
        "ともかく事情を聞かせてみろ。\x02",
    )

    CloseMessageWindow()

    #C0431
    ChrTalk(
        0xC,
        "は、はい……\x02",
    )

    CloseMessageWindow()

    #C0432
    ChrTalk(
        0xC,
        (
            "実は僕、ウルスラ医大を\x01",
            "目指している学生でして……\x01",
            "でも実家は貧しい家庭で……\x02",
        )
    )

    CloseMessageWindow()

    #C0433
    ChrTalk(
        0xC,
        (
            "母親に無理をしてもらってまで\x01",
            "クロスベルに送り出してもらって……\x01",
            "バイトをしながら勉強してるんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0434
    ChrTalk(
        0xC,
        (
            "そんな中で、\x01",
            "突然母親が倒れたって\x01",
            "報せが入って……それで……\x02",
        )
    )

    CloseMessageWindow()

    #C0435
    ChrTalk(
        0x10,
        (
            "――見舞いに行きたいが、\x01",
            "ミラがないのでチケットを盗んだ。\x01",
            "そういうことか？\x02",
        )
    )

    CloseMessageWindow()

    #C0436
    ChrTalk(
        0xC,
        (
            "は、はい……\x01",
            "これは嘘じゃありません！\x02",
        )
    )

    CloseMessageWindow()

    #C0437
    ChrTalk(
        0xC,
        "今こうしている間にも母親は――\x02",
    )

    CloseMessageWindow()

    #C0438
    ChrTalk(
        0x101,
        (
            "#00003Fう～ん、かといって\x01",
            "窃盗を見逃すわけには……\x02",
        )
    )

    CloseMessageWindow()

    #C0439
    ChrTalk(
        0x10,
        "よしっ、ボクがミラを出してやる。\x02",
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

    def lambda_BAC8():
        TurnDirection(0xFE, 0x10, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_BAC8)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_BAF2")

    def lambda_BAE5():
        TurnDirection(0xFE, 0x10, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_BAE5)
    Jump("loc_BB75")

    label("loc_BAF2")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_BB14")

    def lambda_BB07():
        TurnDirection(0xFE, 0x10, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_BB07)
    Jump("loc_BB75")

    label("loc_BB14")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_BB36")

    def lambda_BB29():
        TurnDirection(0xFE, 0x10, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_BB29)
    Jump("loc_BB75")

    label("loc_BB36")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_BB58")

    def lambda_BB4B():
        TurnDirection(0xFE, 0x10, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_BB4B)
    Jump("loc_BB75")

    label("loc_BB58")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_BB75")

    def lambda_BB6D():
        TurnDirection(0xFE, 0x10, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_BB6D)

    label("loc_BB75")


    def lambda_BB7A():
        TurnDirection(0xFE, 0x10, 500)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_BB7A)
    Sleep(50)

    def lambda_BB8A():
        TurnDirection(0xFE, 0x10, 500)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_BB8A)
    Sleep(300)

    #C0440
    ChrTalk(
        0xC,
        "え……？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_BBD1")

    #C0441
    ChrTalk(
        0x102,
        "#00105Fシン君……？\x02",
    )

    CloseMessageWindow()
    Jump("loc_BC7C")

    label("loc_BBD1")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_BBFD")

    #C0442
    ChrTalk(
        0x103,
        "#00205Fそれは……\x02",
    )

    CloseMessageWindow()
    Jump("loc_BC7C")

    label("loc_BBFD")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_BC2B")

    #C0443
    ChrTalk(
        0x104,
        "#00305Fお、おい……\x02",
    )

    CloseMessageWindow()
    Jump("loc_BC7C")

    label("loc_BC2B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_BC57")

    #C0444
    ChrTalk(
        0x109,
        "#10105Fええと……\x02",
    )

    CloseMessageWindow()
    Jump("loc_BC7C")

    label("loc_BC57")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_BC7C")

    #C0445
    ChrTalk(
        0x105,
        "#10305Fへえ……\x02",
    )

    CloseMessageWindow()

    label("loc_BC7C")

    TurnDirection(0x10, 0x8, 500)

    #C0446
    ChrTalk(
        0x10,
        (
            "ご老人、あなたのチケットは\x01",
            "ボクが責任を持って返させる。\x02",
        )
    )

    CloseMessageWindow()

    #C0447
    ChrTalk(
        0x10,
        (
            "それで、どうか\x01",
            "ホコを収めてはくれまいか？\x02",
        )
    )

    CloseMessageWindow()

    #C0448
    ChrTalk(
        0x8,
        (
            "ま、まあチケットが返ってくるなら\x01",
            "わしは別に事を荒立てる気がないが……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10, 0xC, 500)

    #C0449
    ChrTalk(
        0x10,
        "そしてお前――\x02",
    )

    CloseMessageWindow()

    #C0450
    ChrTalk(
        0xC,
        "は、はい……\x02",
    )

    CloseMessageWindow()

    #C0451
    ChrTalk(
        0x10,
        "盗んだチケットで見舞いだ？\x02",
    )

    CloseMessageWindow()

    #C0452
    ChrTalk(
        0x10,
        (
            "もし母親がそれを知ったらどうだ。\x01",
            "喜んでくれるとでも思うのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0453
    ChrTalk(
        0xC,
        "そ、それは……\x02",
    )

    CloseMessageWindow()

    #C0454
    ChrTalk(
        0x10,
        (
            "いいか、ミラは出してやるが\x01",
            "これは譲渡ではない――\x01",
            "あくまで貸しだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0455
    ChrTalk(
        0x10,
        (
            "期限は定めないが、\x01",
            "必ず返してもらうからな。\x02",
        )
    )

    CloseMessageWindow()

    #C0456
    ChrTalk(
        0xC,
        (
            "うう、すみません……\x01",
            "ありがとうございます。\x02",
        )
    )

    CloseMessageWindow()

    #C0457
    ChrTalk(
        0xC,
        "必ず、必ずお返しします。\x02",
    )

    CloseMessageWindow()

    #C0458
    ChrTalk(
        0x10,
        "フム、約束は守ってもらうぞ。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x10, 0x101, 500)

    #C0459
    ChrTalk(
        0x10,
        (
            "そういうわけで、\x01",
            "あとは本職の臨検官を呼んで来い。\x02",
        )
    )

    CloseMessageWindow()

    #C0460
    ChrTalk(
        0x10,
        "事情はボクが説明してやる。\x02",
    )

    CloseMessageWindow()

    #C0461
    ChrTalk(
        0x101,
        "#00005Fあ、ああ……\x02",
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

    # Function_34_9FF7 end

    def Function_35_BF66(): pass

    label("Function_35_BF66")

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

    # Function_35_BF66 end

    def Function_36_BFB0(): pass

    label("Function_36_BFB0")

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

    # Function_36_BFB0 end

    def Function_37_BFFA(): pass

    label("Function_37_BFFA")

    SetChrPos(0xFE, -400, 0, -4300, 0)

    def lambda_C010():
        OP_95(0xFE, -400, 0, 2700, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_C010)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_37_BFFA end

    def Function_38_C031(): pass

    label("Function_38_C031")

    SetChrPos(0xFE, -400, 0, -5500, 0)
    Sleep(50)

    def lambda_C04A():
        OP_95(0xFE, -400, 0, 1500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_C04A)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x13B, 0x1F4)
    Return()

    # Function_38_C031 end

    def Function_39_C06B(): pass

    label("Function_39_C06B")

    SetChrPos(0xFE, 400, 0, -4600, 0)
    Sleep(50)

    def lambda_C084():
        OP_95(0xFE, 400, 0, 3900, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_C084)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_39_C06B end

    def Function_40_C0A5(): pass

    label("Function_40_C0A5")

    SetChrPos(0xFE, 400, 0, -5600, 0)
    Sleep(100)

    def lambda_C0BE():
        OP_95(0xFE, 400, 0, 2900, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_C0BE)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_40_C0A5 end

    def Function_41_C0DF(): pass

    label("Function_41_C0DF")

    SetChrPos(0xFE, 400, 0, -6600, 0)
    Sleep(50)

    def lambda_C0F8():
        OP_95(0xFE, 500, 0, 1500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_C0F8)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_41_C0DF end

    def Function_42_C119(): pass

    label("Function_42_C119")

    SetChrPos(0xFE, 400, 0, -7700, 0)
    Sleep(100)

    def lambda_C132():
        OP_95(0xFE, 400, 0, 400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_C132)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x13B, 0x1F4)
    Return()

    # Function_42_C119 end

    def Function_43_C153(): pass

    label("Function_43_C153")

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
        "#5P#03402F──来たわね。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x28, 0x1)

    #C0463
    ChrTalk(
        0x28,
        "#11P#11509Fよ、久しぶりだな。\x02",
    )

    CloseMessageWindow()
    OP_68(1000, 1000, -6000, 2000)
    MoveCamera(323, 21, 0, 2000)
    SetCameraDistance(18000, 2000)
    OP_6F(0x79)

    #C0464
    ChrTalk(
        0x101,
        "#6P#00006F……ご無沙汰しています。\x02",
    )

    CloseMessageWindow()

    #C0465
    ChrTalk(
        0x103,
        (
            "#6P#00200Fなるほど、列車の通信器から\x01",
            "支援課の車に連絡したんですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0466
    ChrTalk(
        0x27,
        "#03404F#6Pご明察。\x02",
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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C558")

    #A0467
    AnonymousTalk(
        0x27,
        (
            "フフ……改めて見ると\x01",
            "錚々#4Rそうそう#たる顔触れね。\x02\x03",

            "国防軍きっての若手少尉と\x01",
            "星杯の守護騎士が一緒なんて。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C805")

    label("loc_C558")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C5E4")

    #A0468
    AnonymousTalk(
        0x27,
        (
            "フフ……改めて見ると\x01",
            "錚々#4Rそうそう#たる顔触れね。\x02\x03",

            "国防軍きっての若手少尉と\x01",
            "伝説の凶手が一緒なんて。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C805")

    label("loc_C5E4")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C676")

    #A0469
    AnonymousTalk(
        0x27,
        (
            "フフ……改めて見ると\x01",
            "錚々#4Rそうそう#たる顔触れね。\x02\x03",

            "国防軍きっての若手少尉と\x01",
            "一課の主任捜査官が一緒なんて。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C805")

    label("loc_C676")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C6FA")

    #A0470
    AnonymousTalk(
        0x27,
        (
            "フフ……改めて見ると\x01",
            "錚々#4Rそうそう#たる顔触れね。\x02\x03",

            "星杯の守護騎士と\x01",
            "伝説の凶手が一緒なんて。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C805")

    label("loc_C6FA")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C784")

    #A0471
    AnonymousTalk(
        0x27,
        (
            "フフ……改めて見ると\x01",
            "錚々#4Rそうそう#たる顔触れね。\x02\x03",

            "一課の主任捜査官と\x01",
            "星杯の守護騎士が一緒なんて。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C805")

    label("loc_C784")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C805")

    #A0472
    AnonymousTalk(
        0x27,
        (
            "フフ……改めて見ると\x01",
            "錚々#4Rそうそう#たる顔触れね。\x02\x03",

            "一課の主任捜査官と\x01",
            "伝説の凶手が一緒なんて。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C805")

    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x2, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x2, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    OP_CC(0x0, 0x2, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C88A")

    #C0473
    ChrTalk(
        0x109,
        (
            "#6P#10103F……あいにく今は、\x01",
            "支援課に再出向中でして。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C88A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C8D5")

    #C0474
    ChrTalk(
        0x105,
        (
            "#6P#10402F当然、僕の背景くらい\x01",
            "そろそろ掴んでいるか。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C8D5")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C90D")

    #C0475
    ChrTalk(
        0x106,
        "#6P#10701F………………………………\x02",
    )

    CloseMessageWindow()

    label("loc_C90D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C958")

    #C0476
    ChrTalk(
        0x10A,
        (
            "#6P#00603Fフン……社交辞令は\x01",
            "そのくらいにして頂こう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C958")


    #C0477
    ChrTalk(
        0x102,
        (
            "#6P#00106Fまさかあなた方が、\x01",
            "クロスベルに残っているとは\x01",
            "思っていませんでした。\x02\x03",

            "#00101Fあれから、ずっとこの街に？\x02",
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
            "ああ、調べることが\x01",
            "色々とあったからな～。\x02\x03",

            "だが、これでようやく\x01",
            "エレボニアに帰れそうだぜ。\x02",
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
        "#00011F#12P調べること……？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BF, 3)), scpexpr(EXPR_END)), "loc_CDFD")

    #C0480
    ChrTalk(
        0x28,
        (
            "#11504Fちなみに、俺たち以外にも\x01",
            "リベールの関係者が\x01",
            "動いてるんだが……\x02\x03",

            "#11500Fひょっとして知ってるか？\x02",
        )
    )

    CloseMessageWindow()

    #C0481
    ChrTalk(
        0x101,
        (
            "#00005Fああ……Ｒ＆Ａリサーチの\x01",
            "レインズさんですね。\x02\x03",

            "#00001Fもしかして彼とも協力を？\x02",
        )
    )

    CloseMessageWindow()

    #C0482
    ChrTalk(
        0x27,
        (
            "#03404F#5Pええ、この件に関しては\x01",
            "お互い情報交換をしているわね。\x02\x03",

            "#03402F民間の調査会社にしては\x01",
            "優秀な情報網を持っているし。\x02",
        )
    )

    CloseMessageWindow()

    #C0483
    ChrTalk(
        0x28,
        (
            "#11504Fま、民間だと人手不足だろうから\x01",
            "各地に人を回しきれないで\x01",
            "苦労してんだろうけどな～。\x02",
        )
    )

    CloseMessageWindow()

    #C0484
    ChrTalk(
        0x104,
        (
            "#00306F#12Pそれはともかく……\x02\x03",

            "#00301F《鉄血宰相#8Rア ン タ の ボ ス#》が\x01",
            "撃たれて行方不明なんだろうが？\x02\x03",

            "こんな所で油売ってていいのかよ？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CE81")

    label("loc_CDFD")


    #C0485
    ChrTalk(
        0x104,
        (
            "#00306F#12Pつーか、《鉄血宰相#8Rア ン タ の ボ ス#》が\x01",
            "撃たれて行方不明なんだろうが？\x02\x03",

            "#00301Fこんな所で油売ってていいのかよ？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CE81")


    #C0486
    ChrTalk(
        0x28,
        (
            "#11505Fああ……\x01",
            "ギリアスのオッサンのことか。\x02\x03",

            "#11506Fオレが急いで帰ったところで\x01",
            "助けられるワケでもないしなー。\x02\x03",

            "#11510Fそれにあのオッサンにしてみりゃ、\x01",
            "自分の事もクロスベルの事も\x01",
            "想定してた局面のうちだろうしよ。\x02",
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
        "#6P#00105Fえ……！？\x02",
    )

    CloseMessageWindow()

    #C0488
    ChrTalk(
        0x101,
        (
            "#00007F#12P想定していたって……\x01",
            "自分が撃たれることを！？\x02",
        )
    )

    CloseMessageWindow()

    #C0489
    ChrTalk(
        0x103,
        (
            "#12P#00201Fクロスベルの事というのは……\x01",
            "今回の事件のことですよね？\x02",
        )
    )

    CloseMessageWindow()

    #C0490
    ChrTalk(
        0x28,
        (
            "#11501Fあのオッサンにとって\x01",
            "全ては遊戯盤の《駒》だからな。\x02\x03",

            "#11503Fクロスベルが至宝を手に入れて、\x01",
            "独立どころか大陸全土の支配を\x01",
            "目論#4Rもく ろ #もうとしていること……\x02\x03",

            "帝国軍が返り討ちに遭った隙に\x01",
            "貴族勢力が帝都を占領したこと……\x02\x03",

            "#11508Fその結果、自分が撃たれて\x01",
            "瀕死の重傷を負ったことによって\x01",
            "泥沼の内戦が始まったこと……\x02\x03",

            "にも関わらず、クロスベルという\x01",
            "不可侵の《壁》が出来たことによって\x01",
            "共和国の侵攻を食い止められていること。\x02\x03",

            "#11500Fあのオッサンにとっては\x01",
            "全て想定していた展開だろうさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0491
    ChrTalk(
        0x101,
        "#00010F#12P……くっ…………\x02",
    )

    CloseMessageWindow()

    #C0492
    ChrTalk(
        0x102,
        "#6P#00108Fそ、そんな……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D2FC")

    #C0493
    ChrTalk(
        0x105,
        "#6P#10401F……化物だね、本当に。\x02",
    )

    CloseMessageWindow()
    Jump("loc_D363")

    label("loc_D2FC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D337")

    #C0494
    ChrTalk(
        0x10A,
        "#6P#00610Fそこまでの化物とは……\x02",
    )

    CloseMessageWindow()
    Jump("loc_D363")

    label("loc_D337")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D363")

    #C0495
    ChrTalk(
        0x106,
        "#6P#10703F……化物……\x02",
    )

    CloseMessageWindow()

    label("loc_D363")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D39E")

    #C0496
    ChrTalk(
        0x109,
        "#6P#10110Fし、信じられません……\x02",
    )

    CloseMessageWindow()
    Jump("loc_D435")

    label("loc_D39E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D3EC")

    #C0497
    ChrTalk(
        0x106,
        (
            "#6P#10703F……にわかには\x01",
            "ちょっと信じ難いですね……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D435")

    label("loc_D3EC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D435")

    #C0498
    ChrTalk(
        0x10A,
        (
            "#6P#00610Fさすがに鵜呑みに\x01",
            "出来るものではないが……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D435")


    #C0499
    ChrTalk(
        0x27,
        (
            "#03401F#5Pまあ《結社》も帝国方面で\x01",
            "動き出しているみたいだけど……\x02\x03",

            "本当に恐ろしいのは、\x01",
            "《鉄血宰相》かもしれないわね。\x02\x03",

            "#03403F己#2Rおのれ#すらも《駒》として利用し、\x01",
            "荒ぶる激動の時代を作り出す……\x02\x03",

            "#03401Fまさに傑物#4Rけつぶつ#──いいえ怪物だわ。\x02",
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
            "#00306F#12Pヤバいオッサンだとは思ったが\x01",
            "まさかそこまでとは……\x02",
        )
    )

    CloseMessageWindow()

    #C0502
    ChrTalk(
        0x102,
        (
            "#6P#00101F……ディーター大統領は\x01",
            "その事に気付いているんですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0503
    ChrTalk(
        0x27,
        (
            "#03405F#5Pさて、どうなのかしら。\x02\x03",

            "#03403Fこう言ってはなんだけど……\x01",
            "ディーター・クロイスという人物は\x01",
            "パフォーマンスは超一流だわ。\x02\x03",

            "#03401Fでも、実際の政治家としては……\x01",
            "やや疑問を感じざるを得ないわね。\x02\x03",

            "経営者としての観点からしか\x01",
            "政治を動かしていないという意味で。\x02",
        )
    )

    CloseMessageWindow()

    #C0504
    ChrTalk(
        0x101,
        "#00005F#12Pそれは……\x02",
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
            "#03404F#5Pまあ、あくまで\x01",
            "根は銀行家なのでしょう。\x02\x03",

            "#03402F《クロイス家》の使命にしても\x01",
            "娘の方に任せ切りのようだし。\x02",
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
        "#12P#00205Fそれは……\x02",
    )

    CloseMessageWindow()

    #C0508
    ChrTalk(
        0x101,
        "#00001F#12P……ご存知でしたか。\x02",
    )

    CloseMessageWindow()

    #C0509
    ChrTalk(
        0x28,
        (
            "#11504Fま、こっちにはこっちの\x01",
            "情報ソースがあるんでね。\x02\x03",

            "#11508Fアンタらがあの競売会で\x01",
            "保護したチビッコ……\x02\x03",

            "#11501Fあの子が“核”となって\x01",
            "《至宝》が誕生した経緯は\x01",
            "おおよそ掴んでいる。\x02",
        )
    )

    CloseMessageWindow()

    #C0510
    ChrTalk(
        0x101,
        "#00003F#12P………………………………\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D9C5")

    #C0511
    ChrTalk(
        0x105,
        (
            "#6P#10408Fやれやれ……\x01",
            "世俗の勢力がそこまで\x01",
            "掴んでいるとはね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D9C5")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_DA12")

    #C0512
    ChrTalk(
        0x10A,
        (
            "#6P#00603Fさすがは帝国軍情報局に\x01",
            "ロックスミス機関か……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DA12")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_DA3A")

    #C0513
    ChrTalk(
        0x109,
        "#6P#10101Fくっ……\x02",
    )

    CloseMessageWindow()

    label("loc_DA3A")


    #C0514
    ChrTalk(
        0x27,
        (
            "#03400F#5P誤解して欲しくないけど……\x01",
            "私にしても、そこの彼にしても\x01",
            "あくまで情報畑の人間よ。\x02\x03",

            "個人的な一存で\x01",
            "《至宝》をどうこうしようとか\x01",
            "考えているわけではないわ。\x02\x03",

            "#03403Fただ、大陸全土を混乱に陥れる\x01",
            "契機#4Rきっかけ#となったこの事件……\x02\x03",

            "#03401Fその絵を描いた『真の黒幕#4Rフィクサー#』が\x01",
            "誰なのかが知りたいだけなの。\x02",
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
        "#6P#00101F真の……黒幕#4Rフィクサー#！？\x02",
    )

    CloseMessageWindow()

    #C0517
    ChrTalk(
        0x27,
        (
            "#03404F#5P先ほど言ったように、\x01",
            "ディーター大統領はあくまで\x01",
            "経営者としての側面が強すぎるわ。\x02\x03",

            "マリアベル嬢も底知れないけど\x01",
            "政治面よりは、魔導技術方面を\x01",
            "一手に引き受けているみたいだし。\x02\x03",

            "#03400Fかといって《風の剣聖》は……\x01",
            "黒幕というには余りに自戒的で\x01",
            "ストイックすぎるでしょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0518
    ChrTalk(
        0x28,
        (
            "#11501Fギリアスのオッサンにしても\x01",
            "《結社》にしても……\x02\x03",

            "クロスベルの状況を利用したり、\x01",
            "利害の一致で協力はしたが\x01",
            "主体的に行動してるわけじゃない。\x02\x03",

            "#11503F──誰かいるハズなんだ。\x02\x03",

            "#11508F政治、経済、歴史、国際情勢……\x02\x03",

            "クロイス家やＤ∴Ｇ教団、\x01",
            "《結社》の動きに至るまで……\x02\x03",

            "#11501F全て#4R㈲　㈲#に通じた上で\x01",
            "各方面に働きかけながら\x01",
            "ここまでの絵を描いたヤツが。\x02",
        )
    )

    CloseMessageWindow()

    #C0519
    ChrTalk(
        0x104,
        "#00306F#12Pおいおい……マジかよ。\x02",
    )

    CloseMessageWindow()

    #C0520
    ChrTalk(
        0x102,
        (
            "#6P#00108F少々、陰謀論じみているような\x01",
            "気もしますが……\x02",
        )
    )

    CloseMessageWindow()

    #C0521
    ChrTalk(
        0x103,
        (
            "#12P#00203F確かに……パズルのピースが\x01",
            "足りないような気はします。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BE, 0)), scpexpr(EXPR_END)), "loc_E011")
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
        "#00013F#11P（………まさか…………）\x02",
    )

    CloseMessageWindow()
    Jump("loc_E076")

    label("loc_E011")


    #C0523
    ChrTalk(
        0x101,
        "#00008F#11P（一体、何者だ……？）\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E076")

    #C0524
    ChrTalk(
        0x10A,
        "#00608F#6P#30W（……まさか……いや……）\x02",
    )

    CloseMessageWindow()

    label("loc_E076")

    Sleep(500)

    #C0525
    ChrTalk(
        0x27,
        (
            "#03404F#5Pまあ、そのあたりの確認が\x01",
            "出来ないかと思ったのだけど……\x02\x03",

            "貴方たちにも確証は無さそうだし、\x01",
            "この程度にしておきましょう。\x02\x03",

            "#03402F時間も無いし、もう一つの用件に\x01",
            "入らせてもらうわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0526
    ChrTalk(
        0x101,
        "#00005F#12Pもう一つの用件……？\x02",
    )

    CloseMessageWindow()

    #C0527
    ChrTalk(
        0x28,
        (
            "#11504Fうむ、簡単なことだ。\x02\x03",

            "#11507F『オルキスタワー攻略作戦』、\x01",
            "手伝ってやろうと思ってな！\x02",
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
        "#00011F#12Pええっ！？\x02",
    )

    CloseMessageWindow()

    #C0529
    ChrTalk(
        0x104,
        (
            "#00307F#12Pおいおい、\x01",
            "いきなりすぎんだろ！？\x02",
        )
    )

    CloseMessageWindow()

    #C0530
    ChrTalk(
        0x27,
        (
            "#03404F#5P事件の概要が判った以上、\x01",
            "クロスベルに留まる必要は\x01",
            "ないのだけど……\x02\x03",

            "このまま去るというのも\x01",
            "少しばかり寝覚めが悪いから。\x02\x03",

            "#03400F今後、クロスベルがどうなるか\x01",
            "貴方たち次第でしょうけど……\x02\x03",

            "慢性的な膠着状態に陥られても\x01",
            "こちらとしては困るのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0531
    ChrTalk(
        0x28,
        (
            "#11504F『ポムっと』だってクリア直前に\x01",
            "放り投げるのは気持ち悪いしなー。\x02\x03",

            "#11502Fま、それと同じってことだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0532
    ChrTalk(
        0x102,
        "#6P#00109F同じと言われても……\x02",
    )

    CloseMessageWindow()

    #C0533
    ChrTalk(
        0x103,
        (
            "#12P#00211F……というか何時の間に\x01",
            "『ポムっと』のアカウントを\x01",
            "入手してるんですか？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E4FE")

    #C0534
    ChrTalk(
        0x105,
        (
            "#6P#10404Fでもまあ、戦力が増えたら\x01",
            "作戦の成功率も上がりそうだね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E5B1")

    label("loc_E4FE")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E558")

    #C0535
    ChrTalk(
        0x10A,
        (
            "#6P#00606Fだが確かに、戦力が増えれば\x01",
            "作戦の成功率も上がるか……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E5B1")

    label("loc_E558")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E5B1")

    #C0536
    ChrTalk(
        0x106,
        (
            "#6P#10703Fでも確かに、戦力が増えれば\x01",
            "作戦の成功率も上がりそうです。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E5B1")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E60D")

    #C0537
    ChrTalk(
        0x109,
        (
            "#6P#10108Fちょっと複雑ですけど……\x01",
            "検討してもいいかもしれません。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E6B0")

    label("loc_E60D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E65D")

    #C0538
    ChrTalk(
        0x106,
        (
            "#6P#10708F課長さんに相談しても\x01",
            "いいかもしれませんね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E6B0")

    label("loc_E65D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E6B0")

    #C0539
    ChrTalk(
        0x10A,
        (
            "#6P#00601Fセルゲイさんにも相談して\x01",
            "検討するべきかもしれんな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E6B0")


    #C0540
    ChrTalk(
        0x101,
        (
            "#00006F#12P……分かりました。\x02\x03",

            "#00000Fこちらの拠点に案内するので\x01",
            "俺たちに付いて来てください。\x02",
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
            "その後、ロイドたちは\x01",
            "セルゲイ課長にキリカたちを紹介し……\x02\x03",

            "お互い情報交換をした上で\x01",
            "作戦に協力してもらう事になった。\x02\x03",

            "そしてロバーツ主任による\x01",
            "オルキスタワーへのハッキングが\x01",
            "とうとう成功し……\x02\x03",

            "『オルキスタワー攻略作戦』が\x01",
            "すぐに決行される事となった。\x07\x00\x02",
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

    # Function_43_C153 end

    def Function_44_E84A(): pass

    label("Function_44_E84A")

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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E998")
    SetChrPos(0x102, 280, 0, -7500, 0)
    Jump("loc_EA2B")

    label("loc_E998")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E9BE")
    SetChrPos(0x103, 280, 0, -7500, 0)
    Jump("loc_EA2B")

    label("loc_E9BE")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E9E4")
    SetChrPos(0x104, 280, 0, -7500, 0)
    Jump("loc_EA2B")

    label("loc_E9E4")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_EA0A")
    SetChrPos(0x109, 280, 0, -7500, 0)
    Jump("loc_EA2B")

    label("loc_EA0A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_EA2B")
    SetChrPos(0x105, 280, 0, -7500, 0)

    label("loc_EA2B")

    SetChrPos(0x1A1, -90, 0, -8180, 0)
    SetChrChipByIndex(0x29, 0x1E)
    SetChrSubChip(0x29, 0x0)
    ClearChrFlags(0x29, 0x80)
    SetChrFlags(0x29, 0x8000)
    SetChrPos(0x29, -40, 0, -3180, 0)

    def lambda_EA64():
        OP_95(0x29, -40, 0, 1990, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_EA64)
    SoundLoad(450)
    Sound(450, 2, 100, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(1000)

    #C0542
    ChrTalk(
        0x15,
        (
            "な、なあ、あのお婆さん……\x01",
            "屋根の上から入ってきたよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0543
    ChrTalk(
        0x16,
        (
            "うん……\x01",
            "なんなんだろう、あの人。\x02",
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
            "#5Sええい、うるさいねえ！\x01",
            "見世物じゃないよ！！#3S\x02",
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
        "ひいっ！？\x02",
    )

    CloseMessageWindow()

    #C0546
    ChrTalk(
        0x15,
        "お、おっかない……！？\x02",
    )

    CloseMessageWindow()

    #C0547
    ChrTalk(
        0x101,
        "#00007Fいたぞ！！\x02",
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

    def lambda_EC26():
        OP_95(0xFE, -420, 0, 150, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_EC26)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_EC6A")

    def lambda_EC50():
        OP_95(0xFE, 280, 0, -850, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_EC50)
    Jump("loc_ED21")

    label("loc_EC6A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_EC99")

    def lambda_EC7F():
        OP_95(0xFE, 280, 0, -850, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_EC7F)
    Jump("loc_ED21")

    label("loc_EC99")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_ECC8")

    def lambda_ECAE():
        OP_95(0xFE, 280, 0, -850, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_ECAE)
    Jump("loc_ED21")

    label("loc_ECC8")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_ECF7")

    def lambda_ECDD():
        OP_95(0xFE, 280, 0, -850, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_ECDD)
    Jump("loc_ED21")

    label("loc_ECF7")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_ED21")

    def lambda_ED0C():
        OP_95(0xFE, 280, 0, -850, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_ED0C)

    label("loc_ED21")


    def lambda_ED26():
        OP_95(0xFE, -90, 0, -1650, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x1A1, 1, lambda_ED26)
    WaitChrThread(0x1A1, 1)

    #C0548
    ChrTalk(
        0x29,
        "なっ……！！\x02",
    )

    CloseMessageWindow()
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    #C0549
    ChrTalk(
        0x29,
        "#5Sなんてしつこいヤツらだい！#3S\x02",
    )

    CloseMessageWindow()
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    #C0550
    ChrTalk(
        0x29,
        "#5Sあんたたち、諦めが悪すぎるよ！#3S\x02",
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1A1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_EE97")

    #C0551
    ChrTalk(
        0x102,
        (
            "#00106F正直、こっちのセリフ\x01",
            "なんですけど……\x02\x03",

            "#00101F……もう逃げ場はありません。\x01",
            "おとなしく投降してください。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F0A8")

    label("loc_EE97")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_EF16")

    #C0552
    ChrTalk(
        0x103,
        (
            "#00206Fその言葉、\x01",
            "そのままお返しします。\x02\x03",

            "#00200Fもう逃げ場はないはず……\x01",
            "いい加減観念してください。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F0A8")

    label("loc_EF16")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_EF90")

    #C0553
    ChrTalk(
        0x104,
        (
            "#00306Fこっちのセリフだっつーの。\x02\x03",

            "#00302Fさて、もう逃げ場はねーぜ？\x01",
            "年貢の納め時ってやつだな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F0A8")

    label("loc_EF90")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_F022")

    #C0554
    ChrTalk(
        0x109,
        (
            "#10106Fこ、こちらのセリフな\x01",
            "気がするんですが……\x02\x03",

            "#10101F……とにかく。\x01",
            "逃走はもう不可能です。\x01",
            "おとなしく投降願います。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F0A8")

    label("loc_F022")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_F0A8")

    #C0555
    ChrTalk(
        0x105,
        (
            "#10306Fやれやれ、あなたにだけは\x01",
            "言われたくないよマダム。\x02\x03",

            "#10302Fおとなしくしたほうが\x01",
            "身のためだと思うけど……？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F0A8")


    #C0556
    ChrTalk(
        0x1A1,
        (
            "そ、そうだそうだ！\x01",
            "あきらめろ～！\x02",
        )
    )

    CloseMessageWindow()

    #C0557
    ChrTalk(
        0x29,
        (
            "ハッ……\x01",
            "何を言うかと思えば……\x02",
        )
    )

    CloseMessageWindow()

    #C0558
    ChrTalk(
        0x29,
        "いいかい、覚えときな！\x02",
    )

    CloseMessageWindow()

    #C0559
    ChrTalk(
        0x29,
        (
            "この大陸の続く限り……\x01",
            "アタシが逃げ切れないなんて\x01",
            "ありえないってことをね！\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x29, 0x0, 0x1F4)
    OP_95(0x29, 0, 0, 8290, 4000, 0x0)
    Sound(100, 0, 100, 0)
    ClearMapObjFlags(0x2, 0x10)
    OP_71(0x2, 0x0, 0x5, 0x1, 0x8)
    Sleep(200)

    def lambda_F19B():
        OP_95(0xFE, -10, 0, 10140, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_F19B)
    Sleep(200)

    def lambda_F1B8():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x29, 2, lambda_F1B8)
    Sleep(1000)

    #C0560
    ChrTalk(
        0x101,
        (
            "#00006Fく、くそっ……\x01",
            "意味わかんないし……！\x02\x03",

            "#00007Fとにかく、追うぞみんな！\x02",
        )
    )

    CloseMessageWindow()

    #C0561
    ChrTalk(
        0x1A1,
        "待て～～～～～～！\x02",
    )

    CloseMessageWindow()

    def lambda_F237():
        OP_95(0xFE, -420, 0, 10450, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_F237)
    Sleep(100)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_F27E")

    def lambda_F264():
        OP_95(0xFE, 280, 0, 10250, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_F264)
    Jump("loc_F335")

    label("loc_F27E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_F2AD")

    def lambda_F293():
        OP_95(0xFE, 280, 0, 10250, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_F293)
    Jump("loc_F335")

    label("loc_F2AD")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_F2DC")

    def lambda_F2C2():
        OP_95(0xFE, 280, 0, 10250, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_F2C2)
    Jump("loc_F335")

    label("loc_F2DC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_F30B")

    def lambda_F2F1():
        OP_95(0xFE, 280, 0, 10250, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_F2F1)
    Jump("loc_F335")

    label("loc_F30B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_F335")

    def lambda_F320():
        OP_95(0xFE, 280, 0, 10250, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_F320)

    label("loc_F335")

    Sleep(100)

    def lambda_F33D():
        OP_95(0xFE, -90, 0, 10050, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x1A1, 1, lambda_F33D)
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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_F462")
    SetChrPos(0x102, 130, 0, -6140, 0)
    Jump("loc_F4F5")

    label("loc_F462")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_F488")
    SetChrPos(0x103, 130, 0, -6140, 0)
    Jump("loc_F4F5")

    label("loc_F488")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_F4AE")
    SetChrPos(0x104, 130, 0, -6140, 0)
    Jump("loc_F4F5")

    label("loc_F4AE")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_F4D4")
    SetChrPos(0x109, 130, 0, -6140, 0)
    Jump("loc_F4F5")

    label("loc_F4D4")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_F4F5")
    SetChrPos(0x105, 130, 0, -6140, 0)

    label("loc_F4F5")

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
        "男",
        (
            "列車も発進した……\x01",
            "ようやく一息つけそうだな。\x02",
        )
    )

    CloseMessageWindow()

    #N0563
    NpcTalk(
        0x2B,
        "男",
        (
            "ああ……\x01",
            "これでクロスベルとはオサラバだ。\x02",
        )
    )

    CloseMessageWindow()

    #N0564
    NpcTalk(
        0x2B,
        "男",
        (
            "黒月に捕まった仲間たちには\x01",
            "正直、申し訳ないがな……\x02",
        )
    )

    CloseMessageWindow()

    #N0565
    NpcTalk(
        0x2C,
        "男",
        (
            "なに、今回は準備が\x01",
            "足りなかったというだけだ。\x02",
        )
    )

    CloseMessageWindow()

    #N0566
    NpcTalk(
        0x2C,
        "男",
        (
            "いずれ、奴らには\x01",
            "かならずや制裁を……\x02",
        )
    )

    CloseMessageWindow()

    #N0567
    NpcTalk(
        0x2D,
        "男の声",
        (
            "ほう……おもしろい話を\x01",
            "しているようだな。\x02",
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

    def lambda_F7B2():
        OP_95(0xFE, 30, 0, 1880, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x2D, 1, lambda_F7B2)

    def lambda_F7CC():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2D, 2, lambda_F7CC)
    Sleep(600)

    def lambda_F7E0():
        OP_95(0xFE, -110, 0, 2990, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x2E, 1, lambda_F7E0)

    def lambda_F7FA():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2E, 2, lambda_F7FA)
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
        "男",
        (
            "あ……ああ……\x01",
            "貴様らは……\x02",
        )
    )

    CloseMessageWindow()

    #N0569
    NpcTalk(
        0x2B,
        "男",
        "黒月……！？\x02",
    )

    CloseMessageWindow()

    #N0570
    NpcTalk(
        0x2C,
        "男",
        (
            "く、くそっ……\x01",
            "尾けられていたのか……！\x02",
        )
    )

    CloseMessageWindow()

    #C0571
    ChrTalk(
        0x2D,
        (
            "ツァオ様がお前たちを\x01",
            "見逃すはずはないだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0572
    ChrTalk(
        0x2D,
        (
            "反東方・移民政策主義の諸君……\x01",
            "我々と一緒に来てもらうぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0573
    ChrTalk(
        0x2E,
        (
            "アルタイル市につき次第、\x01",
            "クロスベル行きに\x01",
            "乗り換えてもらおうか。\x02",
        )
    )

    CloseMessageWindow()

    #C0574
    ChrTalk(
        0x2A,
        "ば、万事休すか……\x02",
    )

    CloseMessageWindow()

    #N0575
    NpcTalk(
        0x29,
        "老婆の声",
        "──どきな、そこのガキ！\x02",
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

    def lambda_FA14():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2D, 1, lambda_FA14)
    Sleep(50)

    def lambda_FA24():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2E, 1, lambda_FA24)

    #C0576
    ChrTalk(
        0x2D,
        "え……\x02",
    )

    CloseMessageWindow()

    def lambda_FA3D():
        OP_95(0xFE, 10, 0, 2460, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_FA3D)
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
        "あがっ！\x02",
    )

    CloseMessageWindow()

    #C0578
    ChrTalk(
        0x2E,
        "ぐほっ！？\x02",
    )

    CloseMessageWindow()

    #C0579
    ChrTalk(
        0x29,
        (
            "アイタタ……\x01",
            "このノロマども、\x01",
            "だから言っただろう！？\x02",
        )
    )

    CloseMessageWindow()

    #C0580
    ChrTalk(
        0x29,
        (
            "あたしゃねえ、こんなとこで\x01",
            "立ち止まってる場合じゃないんだよ！\x02",
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
        "（え、ええっと……）\x02",
    )

    CloseMessageWindow()

    #C0582
    ChrTalk(
        0x2A,
        "（何なんだ、この婆さん。）\x02",
    )

    CloseMessageWindow()
    OP_63(0x29, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0x29, 0x10E, 0x1F4)

    #C0583
    ChrTalk(
        0x29,
        "……んん～……？\x02",
    )

    CloseMessageWindow()

    #C0584
    ChrTalk(
        0x29,
        (
            "アンタら、もしかして……\x01",
            "こいつらに追われてたのかい？\x02",
        )
    )

    CloseMessageWindow()

    #C0585
    ChrTalk(
        0x2B,
        (
            "あ、ああ……\x01",
            "正直、助かったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0586
    ChrTalk(
        0x2C,
        "アンタ、恩人だ！\x02",
    )

    CloseMessageWindow()

    #C0587
    ChrTalk(
        0x29,
        "フン、なんだか知らないが……\x02",
    )

    CloseMessageWindow()

    #C0588
    ChrTalk(
        0x29,
        (
            "……奴らに対抗するには\x01",
            "１人でも多くの仲間が必要だね。\x02",
        )
    )

    CloseMessageWindow()
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    #C0589
    ChrTalk(
        0x29,
        (
            "#5Sアンタたち！\x01",
            "少しでも恩に感じてるなら\x01",
            "アタシといっしょに来な！#3S\x02",
        )
    )

    CloseMessageWindow()
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    #C0590
    ChrTalk(
        0x29,
        (
            "#5Sうまくいきゃ、\x01",
            "アンタらも逃げきれる\x01",
            "かもしれないよっ！#3S\x02",
        )
    )

    CloseMessageWindow()

    #C0591
    ChrTalk(
        0x2A,
        "え、ええっ……！？\x02",
    )

    CloseMessageWindow()

    #C0592
    ChrTalk(
        0x2B,
        "本当か……！？\x02",
    )

    CloseMessageWindow()

    #C0593
    ChrTalk(
        0x29,
        "ホラ、モタモタするんじゃないよ！\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("共和国系テロリストたち")

    #A0594
    AnonymousTalk(
        0xFF,
        "わ、わかった！！\x02",
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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_FE44")
    BeginChrThread(0x102, 1, 0, 47)
    Jump("loc_FEAB")

    label("loc_FE44")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_FE5F")
    BeginChrThread(0x103, 1, 0, 47)
    Jump("loc_FEAB")

    label("loc_FE5F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_FE7A")
    BeginChrThread(0x104, 1, 0, 47)
    Jump("loc_FEAB")

    label("loc_FE7A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_FE95")
    BeginChrThread(0x109, 1, 0, 47)
    Jump("loc_FEAB")

    label("loc_FE95")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_FEAB")
    BeginChrThread(0x105, 1, 0, 47)

    label("loc_FEAB")

    Sleep(300)
    BeginChrThread(0x1A1, 1, 0, 47)
    Sleep(2000)

    #C0595
    ChrTalk(
        0x1A1,
        "#7Aま、待て～！！\x02",
    )
    #Auto

    WaitChrThread(0x1A1, 1)
    OP_57(0x0)
    OP_5A()
    Sleep(700)

    #C0596
    ChrTalk(
        0x2E,
        "くっ……\x02",
    )

    CloseMessageWindow()

    #C0597
    ChrTalk(
        0x2D,
        "い、一体何だったんだ……\x02",
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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_FFE6")
    SetChrPos(0x102, -650, 0, -8160, 0)
    Jump("loc_10079")

    label("loc_FFE6")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1000C")
    SetChrPos(0x103, -650, 0, -8160, 0)
    Jump("loc_10079")

    label("loc_1000C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_10032")
    SetChrPos(0x104, -650, 0, -8160, 0)
    Jump("loc_10079")

    label("loc_10032")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_10058")
    SetChrPos(0x109, -650, 0, -8160, 0)
    Jump("loc_10079")

    label("loc_10058")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_10079")
    SetChrPos(0x105, -650, 0, -8160, 0)

    label("loc_10079")

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
        "はあ、はあ……\x02",
    )

    CloseMessageWindow()

    #C0599
    ChrTalk(
        0x1A1,
        (
            "ま、また屋根の上に\x01",
            "登っていったみたいだね……\x02",
        )
    )

    CloseMessageWindow()

    #C0600
    ChrTalk(
        0x101,
        (
            "#00003Fていうか、\x01",
            "誰かを連れてた\x01",
            "みたいだけど……\x02\x03",

            "#00001Fもしかして仲間が\x01",
            "潜伏していたのか！？\x02",
        )
    )

    CloseMessageWindow()

    #C0601
    ChrTalk(
        0x1A1,
        (
            "そ、そんなはずは……\x01",
            "彼女の手下たちはとっくに\x01",
            "全員逮捕したはずだよ～！？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_10318")

    #C0602
    ChrTalk(
        0x102,
        (
            "#00101Fと、とにかく……\x01",
            "今は後を追いましょう！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1045E")

    label("loc_10318")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1035D")

    #C0603
    ChrTalk(
        0x103,
        (
            "#00201Fともかく……\x01",
            "今は後を追いましょう。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1045E")

    label("loc_1035D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_103B2")

    #C0604
    ChrTalk(
        0x104,
        (
            "#00301Fちっ、よく分からねえが……\x01",
            "今は後を追うとしようぜ！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1045E")

    label("loc_103B2")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_10407")

    #C0605
    ChrTalk(
        0x109,
        (
            "#10101Fよ、よくわかりませんけど……\x01",
            "今は後を追いましょう！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1045E")

    label("loc_10407")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1045E")

    #C0606
    ChrTalk(
        0x105,
        (
            "#10302Fとりあえず、\x01",
            "置いといていいんじゃない？\x01",
            "今は後を追おうよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1045E")


    #C0607
    ChrTalk(
        0x101,
        (
            "#00003Fそ、それもそうだな。\x02\x03",

            "#00001F──よし、追跡を続行するぞ！\x02",
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

    # Function_44_E84A end

    def Function_45_104C2(): pass

    label("Function_45_104C2")

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

    # Function_45_104C2 end

    def Function_46_1051E(): pass

    label("Function_46_1051E")

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

    # Function_46_1051E end

    def Function_47_10574(): pass

    label("Function_47_10574")

    OP_95(0xFE, 0, 0, 8350, 4000, 0x0)

    def lambda_1058D():
        OP_95(0xFE, 0, 0, 10000, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_1058D)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
    Return()

    # Function_47_10574 end

    def Function_48_105AE(): pass

    label("Function_48_105AE")

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

    # Function_48_105AE end

    def Function_49_10605(): pass

    label("Function_49_10605")

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

    # Function_49_10605 end

    def Function_50_1065C(): pass

    label("Function_50_1065C")

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

    # Function_50_1065C end

    SaveToFile()

Try(main)
