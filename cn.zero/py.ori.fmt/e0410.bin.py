from ZeroScenarioHelper import *

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
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 270, 1, 160, 0, 1, 0, 2],
    )

    BuildStringList((
        "e0410",                  # 0
        "青年",                   # 1
        "少女",                   # 2
        "男性",                   # 3
        "父亲",                   # 4
        "母亲",                   # 5
        "男孩",                   # 6
        "贸易商",                 # 7
        "女性",                   # 8
        "卡拉",                   # 9
        "老人",                   # 10
        "老妇人",                 # 11
        "乘客",                   # 12
        "乘客",                   # 13
        "乘客",                   # 14
        "乘客",                   # 15
        "乘客",                   # 16
        "乘客",                   # 17
        "SE控制",                 # 18
    ))

    AddCharChip((
        "chr/ch22002.itc",                   # 00
        "chr/ch22102.itc",                   # 01
        "chr/ch32302.itc",                   # 02
        "chr/ch21002.itc",                   # 03
        "chr/ch21102.itc",                   # 04
        "chr/ch21400.itc",                   # 05
        "chr/ch32202.itc",                   # 06
        "chr/ch33302.itc",                   # 07
        "chr/ch33202.itc",                   # 08
        "chr/ch21802.itc",                   # 09
        "chr/ch20702.itc",                   # 0A
        "chr/ch21902.itc",                   # 0B
        "chr/ch27602.itc",                   # 0C
        "chr/ch23702.itc",                   # 0D
        "chr/ch24400.itc",                   # 0E
        "chr/ch24202.itc",                   # 0F
        "chr/ch32402.itc",                   # 10
        "chr/ch21602.itc",                   # 11
        "chr/ch22202.itc",                   # 12
        "chr/ch20402.itc",                   # 13
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

    DeclNpc(-1899,   150,     4300,    0,    421,  0x0, 0,   0,   0,   255, 255, 0,   3,   255,  0)
    DeclNpc(-1899,   150,     5739,    180,  421,  0x0, 0,   1,   0,   255, 255, 0,   4,   255,  0)
    DeclNpc(2200,    150,     3299,    180,  421,  0x0, 0,   2,   0,   255, 255, 0,   5,   255,  0)
    DeclNpc(-1600,   150,     750,     180,  421,  0x0, 0,   3,   0,   255, 255, 0,   6,   255,  0)
    DeclNpc(-1600,   150,     -750,    0,    421,  0x0, 0,   4,   0,   255, 255, 0,   7,   255,  0)
    DeclNpc(-3000,   0,       0,       225,  389,  0x0, 0,   5,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(-1600,   150,     -3299,   0,    421,  0x0, 0,   6,   0,   255, 255, 0,   9,   255,  0)
    DeclNpc(2200,    150,     -1799,   180,  421,  0x0, 0,   7,   0,   255, 255, 0,   10,  255,  0)
    DeclNpc(-1990,   150,     2970,    180,  469,  0x0, 2,   8,   0,   255, 255, 0,   31,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    469,  0x0, 0,   0,   0,   255, 255, 0,   11,  255,  0)
    DeclNpc(0,       0,       0,       0,    469,  0x0, 0,   0,   0,   255, 255, 0,   12,  255,  0)
    DeclNpc(0,       0,       0,       0,    469,  0x0, 0,   0,   0,   255, 255, 0,   13,  255,  0)
    DeclNpc(0,       0,       0,       0,    469,  0x0, 0,   0,   0,   255, 255, 0,   14,  255,  0)
    DeclNpc(0,       0,       0,       0,    469,  0x0, 0,   0,   0,   255, 255, 0,   15,  255,  0)
    DeclNpc(0,       0,       0,       0,    469,  0x0, 0,   0,   0,   255, 255, 0,   16,  255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 24,  3.5,                   -7.849999904632568,    0.0,                   6.25,                  [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.3999999761581421,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.19999998807907104,   0.0,                   -1.75,                 3.1399998664855957,    -0.0,                  1.0])
    DeclEvent(0x0000, 0, 26,  0.0,                   10.5,                  0.0,                   4.0,                   [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -0.0,                  -5.25,                 -0.0,                  1.0])
    DeclEvent(0x0000, 0, 27,  0.0,                   -10.0,                 0.0,                   4.0,                   [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -0.0,                  5.0,                   -0.0,                  1.0])
    DeclEvent(0x0000, 0, 28,  0.0,                   9.5,                   0.0,                   4.0,                   [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -0.0,                  -4.75,                 -0.0,                  1.0])

    ScpFunction((
        "Function_0_514",          # 00, 0
        "Function_1_5CC",          # 01, 1
        "Function_2_62F",          # 02, 2
        "Function_3_94C",          # 03, 3
        "Function_4_B35",          # 04, 4
        "Function_5_CED",          # 05, 5
        "Function_6_F98",          # 06, 6
        "Function_7_1186",         # 07, 7
        "Function_8_1332",         # 08, 8
        "Function_9_1425",         # 09, 9
        "Function_10_15EF",        # 0A, 10
        "Function_11_17B2",        # 0B, 11
        "Function_12_1AEA",        # 0C, 12
        "Function_13_1DCA",        # 0D, 13
        "Function_14_1E57",        # 0E, 14
        "Function_15_2161",        # 0F, 15
        "Function_16_22EE",        # 10, 16
        "Function_17_2478",        # 11, 17
        "Function_18_25B1",        # 12, 18
        "Function_19_28F1",        # 13, 19
        "Function_20_2C02",        # 14, 20
        "Function_21_3148",        # 15, 21
        "Function_22_3449",        # 16, 22
        "Function_23_391C",        # 17, 23
        "Function_24_3AB1",        # 18, 24
        "Function_25_3BB9",        # 19, 25
        "Function_26_443F",        # 1A, 26
        "Function_27_44AE",        # 1B, 27
        "Function_28_44FE",        # 1C, 28
        "Function_29_456A",        # 1D, 29
        "Function_30_49A7",        # 1E, 30
        "Function_31_4B11",        # 1F, 31
        "Function_32_5FF7",        # 20, 32
        "Function_33_756B",        # 21, 33
        "Function_34_75A4",        # 22, 34
        "Function_35_75EF",        # 23, 35
    ))


    def Function_0_514(): pass

    label("Function_0_514")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_554"),
        (1, "loc_560"),
        (2, "loc_56C"),
        (3, "loc_578"),
        (4, "loc_584"),
        (5, "loc_590"),
        (6, "loc_59C"),
        (SWITCH_DEFAULT, "loc_5A8"),
    )


    label("loc_554")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_5B4")

    label("loc_560")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_5B4")

    label("loc_56C")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_5B4")

    label("loc_578")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_5B4")

    label("loc_584")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_5B4")

    label("loc_590")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_5B4")

    label("loc_59C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_5B4")

    label("loc_5A8")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_5B4")

    label("loc_5B4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5CB")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_5B4")

    label("loc_5CB")

    Return()

    # Function_0_514 end

    def Function_1_5CC(): pass

    label("Function_1_5CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_5E0")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 32)
    Jump("loc_62E")

    label("loc_5E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 1)), scpexpr(EXPR_END)), "loc_61C")
    ClearScenarioFlags(0x5C, 1)
    Event(0, 17)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    Jump("loc_62E")

    label("loc_61C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 2)), scpexpr(EXPR_END)), "loc_62E")
    ClearScenarioFlags(0x5C, 2)
    SetScenarioFlags(0x0, 1)
    Event(0, 29)

    label("loc_62E")

    Return()

    # Function_1_5CC end

    def Function_2_62F(): pass

    label("Function_2_62F")

    ClearMapObjFlags(0x0, 0x10)
    ClearMapObjFlags(0x1, 0x10)
    ClearMapObjFlags(0x2, 0x10)
    ModifyEventFlags(0, 0, 0x80)
    ModifyEventFlags(0, 1, 0x80)
    ModifyEventFlags(0, 2, 0x80)
    ModifyEventFlags(0, 3, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_66E")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_66E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x1, 0x9)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_93C")
    ModifyEventFlags(0, 0, 0x80)
    Switch(
        (scpexpr(EXPR_23, 0x5), scpexpr(EXPR_END)),
        (0, "loc_6B1"),
        (1, "loc_761"),
        (2, "loc_829"),
        (3, "loc_8CE"),
        (SWITCH_DEFAULT, "loc_920"),
    )


    label("loc_6B1")

    ModifyEventFlags(1, 1, 0x80)
    SetMapObjFlags(0x2, 0x10)
    OP_78(0x3, 0xF)
    SetChrPos(0xF, 0, 0, -9450, 0)
    ClearMapObjFlags(0x3, 0x4)
    SetMapObjFlags(0x3, 0x2)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    SetChrFlags(0x17, 0x80)
    SetChrFlags(0x18, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrChipByIndex(0x13, 0x9)
    SetChrChipByIndex(0x14, 0xA)
    SetChrSubChip(0x14, 0x1)
    SetChrChipByIndex(0x15, 0xB)
    SetChrChipByIndex(0x16, 0xC)
    SetChrPos(0x13, -2620, 150, 500, 180)
    SetChrPos(0x14, 1740, 150, 540, 180)
    SetChrPos(0x15, 2870, 150, 540, 180)
    SetChrPos(0x16, 2290, 150, 5520, 180)
    EndChrThread(0x14, 0xFF)
    Jump("loc_920")

    label("loc_761")

    ModifyEventFlags(1, 1, 0x80)
    ModifyEventFlags(1, 2, 0x80)
    SetMapObjFlags(0x2, 0x10)
    SetMapObjFlags(0x3, 0x4)
    ClearMapObjFlags(0x3, 0x2)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrChipByIndex(0x13, 0xD)
    SetChrChipByIndex(0x14, 0xE)
    SetChrChipByIndex(0x15, 0xF)
    SetChrChipByIndex(0x16, 0x7)
    SetChrChipByIndex(0x17, 0x10)
    SetChrChipByIndex(0x18, 0x2)
    SetChrPos(0x13, -1680, 150, -2120, 180)
    SetChrPos(0x14, -3070, 0, -2450, 270)
    SetChrPos(0x15, 2430, 150, -4380, 180)
    SetChrPos(0x16, 2390, 150, 1950, 0)
    SetChrPos(0x17, 2390, 150, 3090, 180)
    SetChrPos(0x18, -2260, 150, 5600, 180)
    BeginChrThread(0x14, 0, 0, 0)
    Jump("loc_920")

    label("loc_829")

    ModifyEventFlags(1, 1, 0x80)
    ModifyEventFlags(1, 2, 0x80)
    SetMapObjFlags(0x2, 0x10)
    ModifyEventFlags(1, 3, 0x80)
    SetMapObjFlags(0x3, 0x4)
    ClearMapObjFlags(0x3, 0x2)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    SetChrFlags(0x17, 0x80)
    SetChrFlags(0x18, 0x80)
    ClearChrFlags(0x10, 0x80)
    SetChrChipByIndex(0x13, 0x11)
    SetChrChipByIndex(0x14, 0x12)
    SetChrSubChip(0x14, 0x0)
    SetChrChipByIndex(0x15, 0x13)
    SetChrChipByIndex(0x16, 0x3)
    SetChrPos(0x13, 1950, 150, -2080, 180)
    SetChrPos(0x14, 2710, 150, -1990, 180)
    SetChrPos(0x15, 2210, 0, 4300, 0)
    SetChrPos(0x16, 2280, 0, 5650, 180)
    EndChrThread(0x14, 0xFF)
    Jump("loc_920")

    label("loc_8CE")

    ModifyEventFlags(1, 2, 0x80)
    OP_70(0x2, 0x0)
    OP_78(0x3, 0xF)
    SetChrPos(0xF, 0, 0, 8800, 0)
    ClearMapObjFlags(0x3, 0x4)
    SetMapObjFlags(0x3, 0x2)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x17, 0x80)
    SetChrFlags(0x18, 0x80)
    SetChrFlags(0x10, 0x80)
    Jump("loc_920")

    label("loc_920")

    BeginChrThread(0x101, 3, 0, 33)
    SetMapObjFlags(0x4, 0x4)
    OP_74(0x5, 0x2D)
    OP_71(0x5, 0xF0, 0x0, 0x0, 0x20)

    label("loc_93C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_94B")
    Sound(450, 1, 100, 0)

    label("loc_94B")

    Return()

    # Function_2_62F end

    def Function_3_94C(): pass

    label("Function_3_94C")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9E0")
    Jump("loc_A2A")

    label("loc_9E0")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_A00")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A2A")

    label("loc_A00")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A20")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A2A")

    label("loc_A20")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A2A")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0x9)"), scpexpr(EXPR_END)), "loc_AA3")

    #C0001
    ChrTalk(
        0xFE,
        "她总是这么急性子，真是的。\x02",
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0xFE,
        "旅行就是要轻松悠闲地享受嘛。\x02",
    )

    CloseMessageWindow()
    Jump("loc_B2D")

    label("loc_AA3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0x4)"), scpexpr(EXPR_END)), "loc_AFA")

    #C0003
    ChrTalk(
        0x8,
        (
            "我们从克洛斯贝尔出发，\x01",
            "要去帝国旅行。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x8,
        "真是期待啊，哈哈哈。\x02",
    )

    CloseMessageWindow()
    Jump("loc_B2D")

    label("loc_AFA")

    Call(0, 18)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0x4)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0x5)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0x6)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0x7)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0x8)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B2D")
    Call(0, 23)

    label("loc_B2D")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_3_94C end

    def Function_4_B35(): pass

    label("Function_4_B35")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_BC9")
    Jump("loc_C13")

    label("loc_BC9")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_BE9")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_C13")

    label("loc_BE9")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C09")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_C13")

    label("loc_C09")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_C13")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0x9)"), scpexpr(EXPR_END)), "loc_C73")

    #C0005
    ChrTalk(
        0xFE,
        (
            "喂～还没发车吗？\x01",
            "难道就不能快点吗。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CE5")

    label("loc_C73")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0x4)"), scpexpr(EXPR_END)), "loc_CB2")

    #C0006
    ChrTalk(
        0x9,
        (
            "真是的，安检已经结束了吧？\x01",
            "快点走开啦！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CE5")

    label("loc_CB2")

    Call(0, 18)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0x4)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0x5)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0x6)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0x7)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0x8)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CE5")
    Call(0, 23)

    label("loc_CE5")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_4_B35 end

    def Function_5_CED(): pass

    label("Function_5_CED")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_D81")
    Jump("loc_DCB")

    label("loc_D81")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_DA1")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_DCB")

    label("loc_DA1")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_DC1")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_DCB")

    label("loc_DC1")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_DCB")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0x9)"), scpexpr(EXPR_END)), "loc_EED")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x70, 0)), scpexpr(EXPR_END)), "loc_E0E")
    Call(0, 25)
    Jump("loc_EE8")

    label("loc_E0E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_E69")

    #C0007
    ChrTalk(
        0xFE,
        (
            "啊啊，真是期待啊。\x01",
            "可以看到车窗外的景色。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0xFE,
        "……真希望能快点发车呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_EE8")

    label("loc_E69")


    #C0009
    ChrTalk(
        0xFE,
        (
            "啊啊，真是期待啊。\x01",
            "可以看到车窗外的景色。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0xFE,
        (
            "诺库斯森林地带的深绿景色\x01",
            "一定超级美丽呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0xFE,
        "……真希望能快点发车呢。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_EE8")

    Jump("loc_F90")

    label("loc_EED")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0x5)"), scpexpr(EXPR_END)), "loc_F5D")

    #C0012
    ChrTalk(
        0xA,
        (
            "呵呵，话说回来，\x01",
            "真期待列车旅行啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0xA,
        (
            "在列车里欣赏外面的景色，\x01",
            "真是别有一番情趣呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F90")

    label("loc_F5D")

    Call(0, 19)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0x4)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0x5)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0x6)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0x7)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0x8)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F90")
    Call(0, 23)

    label("loc_F90")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_5_CED end

    def Function_6_F98(): pass

    label("Function_6_F98")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_102C")
    Jump("loc_1076")

    label("loc_102C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_104C")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1076")

    label("loc_104C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_106C")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1076")

    label("loc_106C")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1076")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x70, 0)), scpexpr(EXPR_END)), "loc_10D0")

    #C0014
    ChrTalk(
        0xFE,
        (
            "哈哈，这急性子好像\x01",
            "和某人有点像。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_117E")

    label("loc_10D0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0x9)"), scpexpr(EXPR_END)), "loc_10E5")
    Call(0, 20)
    Jump("loc_117E")

    label("loc_10E5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0x6)"), scpexpr(EXPR_END)), "loc_114B")

    #C0015
    ChrTalk(
        0xB,
        (
            "从共和国出发，\x01",
            "旅途还真是挺远呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0xB,
        (
            "哈欠……\x01",
            "在发车之前，不如先小睡一觉吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_117E")

    label("loc_114B")

    Call(0, 20)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0x4)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0x5)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0x6)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0x7)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0x8)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_117E")
    Call(0, 23)

    label("loc_117E")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_6_F98 end

    def Function_7_1186(): pass

    label("Function_7_1186")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_121A")
    Jump("loc_1264")

    label("loc_121A")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_123A")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1264")

    label("loc_123A")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_125A")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1264")

    label("loc_125A")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1264")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x70, 0)), scpexpr(EXPR_END)), "loc_12AF")

    #C0017
    ChrTalk(
        0xFE,
        "真是的，这孩子……\x02",
    )

    CloseMessageWindow()
    Jump("loc_132A")

    label("loc_12AF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0x9)"), scpexpr(EXPR_END)), "loc_12C4")
    Call(0, 20)
    Jump("loc_132A")

    label("loc_12C4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0x6)"), scpexpr(EXPR_END)), "loc_12F7")

    #C0018
    ChrTalk(
        0xC,
        (
            "这孩子一直都\x01",
            "安静不下来呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_132A")

    label("loc_12F7")

    Call(0, 20)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0x4)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0x5)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0x6)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0x7)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0x8)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_132A")
    Call(0, 23)

    label("loc_132A")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_7_1186 end

    def Function_8_1332(): pass

    label("Function_8_1332")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x70, 0)), scpexpr(EXPR_END)), "loc_13B1")

    #C0019
    ChrTalk(
        0xFE,
        (
            "哼～……\x01",
            "对面座位上的那个大哥哥\x01",
            "是从前面那节车厢过来的～\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0xFE,
        "真狡猾呀。\x02",
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x101,
        "#0001F…………………………\x02",
    )

    CloseMessageWindow()
    Jump("loc_1421")

    label("loc_13B1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0x9)"), scpexpr(EXPR_END)), "loc_13C6")
    Call(0, 20)
    Jump("loc_1421")

    label("loc_13C6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0x6)"), scpexpr(EXPR_END)), "loc_13EE")

    #C0022
    ChrTalk(
        0xD,
        "还不快点发车吗～\x02",
    )

    CloseMessageWindow()
    Jump("loc_1421")

    label("loc_13EE")

    Call(0, 20)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0x4)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0x5)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0x6)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0x7)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0x8)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1421")
    Call(0, 23)

    label("loc_1421")

    TalkEnd(0xFE)
    Return()

    # Function_8_1332 end

    def Function_9_1425(): pass

    label("Function_9_1425")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_14B9")
    Jump("loc_1503")

    label("loc_14B9")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_14D9")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1503")

    label("loc_14D9")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_14F9")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1503")

    label("loc_14F9")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1503")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0x9)"), scpexpr(EXPR_END)), "loc_158C")

    #C0023
    ChrTalk(
        0xFE,
        (
            "……呼，必须要\x01",
            "稍微冷静一点啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0xFE,
        (
            "如果没有平和的心态，\x01",
            "生意是不会成功的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15E7")

    label("loc_158C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0x7)"), scpexpr(EXPR_END)), "loc_15B4")

    #C0025
    ChrTalk(
        0xE,
        "怎么，还有事吗？\x02",
    )

    CloseMessageWindow()
    Jump("loc_15E7")

    label("loc_15B4")

    Call(0, 21)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0x4)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0x5)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0x6)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0x7)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0x8)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_15E7")
    Call(0, 23)

    label("loc_15E7")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_9_1425 end

    def Function_10_15EF(): pass

    label("Function_10_15EF")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1683")
    Jump("loc_16CD")

    label("loc_1683")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_16A3")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_16CD")

    label("loc_16A3")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_16C3")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_16CD")

    label("loc_16C3")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_16CD")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0x9)"), scpexpr(EXPR_END)), "loc_172E")

    #C0026
    ChrTalk(
        0xFE,
        "唉……\x02",
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0xFE,
        "……真想找个有钱人啊……\x02",
    )

    CloseMessageWindow()
    Jump("loc_17AA")

    label("loc_172E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0x8)"), scpexpr(EXPR_END)), "loc_1777")
    SetChrSubChip(0xF, 0x0)

    #C0028
    ChrTalk(
        0xF,
        (
            "唉……\x01",
            "男人都是一样的。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0xF,
        "（嘟嘟哝哝）……\x02",
    )

    CloseMessageWindow()
    Jump("loc_17AA")

    label("loc_1777")

    Call(0, 22)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0x4)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0x5)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0x6)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0x7)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0x8)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_17AA")
    Call(0, 23)

    label("loc_17AA")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_10_15EF end

    def Function_11_17B2(): pass

    label("Function_11_17B2")

    Switch(
        (scpexpr(EXPR_23, 0x5), scpexpr(EXPR_END)),
        (0, "loc_17CD"),
        (1, "loc_1938"),
        (2, "loc_1991"),
        (SWITCH_DEFAULT, "loc_1AE9"),
    )


    label("loc_17CD")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1861")
    Jump("loc_18AB")

    label("loc_1861")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1881")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_18AB")

    label("loc_1881")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_18A1")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_18AB")

    label("loc_18A1")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_18AB")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0030
    ChrTalk(
        0xFE,
        (
            "难得有机会休假，\x01",
            "我准备回老家阿尔泰尔市。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0xFE,
        (
            "妻子和孩子都在等着我呢，\x01",
            "真是很期待啊¤\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Jump("loc_1AE9")

    label("loc_1938")

    TalkBegin(0xFE)

    #C0032
    ChrTalk(
        0xFE,
        "你还真是个急性子啊。\x02",
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0xFE,
        (
            "离共和国的首都\x01",
            "还远得很呢，\x01",
            "用不着如此焦躁啊。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Jump("loc_1AE9")

    label("loc_1991")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1A25")
    Jump("loc_1A6F")

    label("loc_1A25")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1A45")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1A6F")

    label("loc_1A45")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1A65")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1A6F")

    label("loc_1A65")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1A6F")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0034
    ChrTalk(
        0xFE,
        "我的家乡是奥雷德自治州。\x02",
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0xFE,
        (
            "呵呵，这次是带着孙子一起\x01",
            "过去看看的。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Jump("loc_1AE9")

    label("loc_1AE9")

    Return()

    # Function_11_17B2 end

    def Function_12_1AEA(): pass

    label("Function_12_1AEA")

    Switch(
        (scpexpr(EXPR_23, 0x5), scpexpr(EXPR_END)),
        (0, "loc_1B05"),
        (1, "loc_1C2B"),
        (2, "loc_1C77"),
        (SWITCH_DEFAULT, "loc_1DC9"),
    )


    label("loc_1B05")

    TalkBegin(0xFE)
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1B9C")
    Jump("loc_1BE6")

    label("loc_1B9C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1BBC")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1BE6")

    label("loc_1BBC")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1BDC")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1BE6")

    label("loc_1BDC")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1BE6")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0036
    ChrTalk(
        0xFE,
        "哇～好棒呀～！\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x1)
    TalkEnd(0xFE)
    Jump("loc_1DC9")

    label("loc_1C2B")

    TalkBegin(0xFE)

    #C0037
    ChrTalk(
        0xFE,
        "拍照，拍照！\x02",
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0xFE,
        (
            "期待已久的铁路之旅！\x01",
            "必须要多拍些照片呀！\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Jump("loc_1DC9")

    label("loc_1C77")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1D0B")
    Jump("loc_1D55")

    label("loc_1D0B")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1D2B")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1D55")

    label("loc_1D2B")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1D4B")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1D55")

    label("loc_1D4B")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1D55")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0039
    ChrTalk(
        0xFE,
        "爷爷的故乡真是让人期待！\x02",
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0xFE,
        (
            "听说那里有非常\x01",
            "广阔的大农场呢！\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Jump("loc_1DC9")

    label("loc_1DC9")

    Return()

    # Function_12_1AEA end

    def Function_13_1DCA(): pass

    label("Function_13_1DCA")

    TalkBegin(0xFE)
    Switch(
        (scpexpr(EXPR_23, 0x5), scpexpr(EXPR_END)),
        (0, "loc_1DE8"),
        (1, "loc_1E0E"),
        (2, "loc_1E2B"),
        (SWITCH_DEFAULT, "loc_1E53"),
    )


    label("loc_1DE8")


    #C0041
    ChrTalk(
        0xFE,
        (
            "不要闹过头了哦。\x01",
            "老实一点！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E53")

    label("loc_1E0E")


    #C0042
    ChrTalk(
        0xFE,
        "（昏昏欲睡………）\x02",
    )

    CloseMessageWindow()
    Jump("loc_1E53")

    label("loc_1E2B")


    #C0043
    ChrTalk(
        0xFE,
        (
            "哇哈哈哈哈！\x01",
            "那是不可能的啦！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E53")

    label("loc_1E53")

    TalkEnd(0xFE)
    Return()

    # Function_13_1DCA end

    def Function_14_1E57(): pass

    label("Function_14_1E57")

    Switch(
        (scpexpr(EXPR_23, 0x5), scpexpr(EXPR_END)),
        (0, "loc_1E72"),
        (1, "loc_1FD6"),
        (2, "loc_2130"),
        (SWITCH_DEFAULT, "loc_2160"),
    )


    label("loc_1E72")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1F06")
    Jump("loc_1F50")

    label("loc_1F06")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1F26")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1F50")

    label("loc_1F26")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1F46")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1F50")

    label("loc_1F46")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1F50")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0044
    ChrTalk(
        0xFE,
        (
            "那个可恶的安检官，\x01",
            "竟然一直盯着我看……\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0xFE,
        "虽然是常有的事了，但真是让人不爽！\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Jump("loc_2160")

    label("loc_1FD6")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_206A")
    Jump("loc_20B4")

    label("loc_206A")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_208A")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_20B4")

    label("loc_208A")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_20AA")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_20B4")

    label("loc_20AA")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_20B4")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0046
    ChrTalk(
        0xFE,
        (
            "要去共和国观光的话，\x01",
            "就绝对不能错过各种美食啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0xFE,
        "然后就是温泉了！\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Jump("loc_2160")

    label("loc_2130")

    TalkBegin(0xFE)

    #C0048
    ChrTalk(
        0xFE,
        (
            "哇哈哈哈哈！\x01",
            "那可真是有意思啊！\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Jump("loc_2160")

    label("loc_2160")

    Return()

    # Function_14_1E57 end

    def Function_15_2161(): pass

    label("Function_15_2161")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_21F5")
    Jump("loc_223F")

    label("loc_21F5")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2215")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_223F")

    label("loc_2215")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2235")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_223F")

    label("loc_2235")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_223F")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Switch(
        (scpexpr(EXPR_23, 0x5), scpexpr(EXPR_END)),
        (0, "loc_227F"),
        (1, "loc_2284"),
        (2, "loc_22E1"),
        (SWITCH_DEFAULT, "loc_22E6"),
    )


    label("loc_227F")

    Jump("loc_22E6")

    label("loc_2284")


    #C0049
    ChrTalk(
        0xFE,
        (
            "果然还是和女性朋友\x01",
            "一起旅行最快乐～\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0xFE,
        (
            "要是和老公一起来的话，\x01",
            "肯定不会这么开心。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_22E6")

    label("loc_22E1")

    Jump("loc_22E6")

    label("loc_22E6")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_15_2161 end

    def Function_16_22EE(): pass

    label("Function_16_22EE")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2382")
    Jump("loc_23CC")

    label("loc_2382")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_23A2")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_23CC")

    label("loc_23A2")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_23C2")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_23CC")

    label("loc_23C2")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_23CC")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Switch(
        (scpexpr(EXPR_23, 0x5), scpexpr(EXPR_END)),
        (0, "loc_240C"),
        (1, "loc_2411"),
        (2, "loc_246B"),
        (SWITCH_DEFAULT, "loc_2470"),
    )


    label("loc_240C")

    Jump("loc_2470")

    label("loc_2411")


    #C0051
    ChrTalk(
        0xFE,
        (
            "这个座位的光线稍微有些暗啊……\x01",
            "看不清书上的字呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0xFE,
        "不如移动到靠窗的座位吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2470")

    label("loc_246B")

    Jump("loc_2470")

    label("loc_2470")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_16_22EE end

    def Function_17_2478(): pass

    label("Function_17_2478")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(3750, 1000, -7850, 0)
    MoveCamera(315, 30, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(16000, 0)
    SetChrPos(0x101, 3750, 0, -7850, 270)
    OP_68(0, 1000, -7850, 3000)

    def lambda_24D9():
        OP_97(0x101, 0xFFFFF15A, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_24D9)
    PlayBGM("ed7111", 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x6F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToBright(1000, 0)
    OP_0D()
    Fade(500)
    OP_68(0, 1000, 5000, 0)
    MoveCamera(315, 30, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(16000, 0)
    OP_68(0, 1000, -7850, 7000)
    WaitChrThread(0x101, 1)
    OP_93(0x101, 0x0, 0x0)
    OP_6F(0x79)

    #C0053
    ChrTalk(
        0x101,
        (
            "#0001F……看起来，乘客的数量\x01",
            "果然相当多呢。\x02\x03",

            "#0003F必须要仔细地逐人检查啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_29(0x9, 0x1, 0x3)
    EventEnd(0x5)
    Return()

    # Function_17_2478 end

    def Function_18_25B1(): pass

    label("Function_18_25B1")

    EventBegin(0x0)
    Fade(500)
    OP_68(-1400, 1000, 4980, 0)
    MoveCamera(315, 28, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(16540, 0)
    SetChrPos(0x101, -150, 0, 5000, 270)
    SetChrSubChip(0x8, 0x2)
    SetChrSubChip(0x9, 0x1)
    OP_0D()

    #C0054
    ChrTalk(
        0x101,
        (
            "#12P#0000F不好意思，我是\x01",
            "代理安检官……\x02\x03",

            "抱歉打扰了，\x01",
            "能否让我确认一下您的\x01",
            "随身行李和入境申请书呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x8,
        (
            "#5P……啊～好的好的，是安检啊。\x01",
            "真是麻烦，不过算了，这也是没办法的事。\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x9,
        "#11P哎～不要啊～\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x9, 0x0)

    #C0057
    ChrTalk(
        0x9,
        (
            "#11P背包里面还装着\x01",
            "我的内衣内裤呢。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 0x0)

    #C0058
    ChrTalk(
        0x8,
        "#5P……唔，是吗？\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 0x2)

    #C0059
    ChrTalk(
        0x8,
        (
            "#5P那个，很不好意思，不过……\x01",
            "情况就是这样。\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x101,
        (
            "#12P#0005F……不不不！\x01",
            "这样可不行啊。\x02\x03",

            "#0003F这是规定，所以还请您合作一下。\x01",
            "至于内衣之类的东西……\x01",
            "我一定会极力小心避开的。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 0x0)

    #C0061
    ChrTalk(
        0x8,
        "#5P看啊，没办法啦。\x02",
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x9,
        "#11P真是的，明白啦～……\x02",
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x101,
        "#12P#0006F（这、这可真是劳心伤神……）\x02",
    )

    CloseMessageWindow()
    FadeToDark(500, 0, -1)
    OP_0D()
    SetChrSubChip(0x8, 0x2)
    SetChrSubChip(0x9, 0x1)
    Sleep(2000)
    FadeToBright(500, 0)
    OP_0D()

    #C0064
    ChrTalk(
        0x101,
        (
            "#12P#0000F……可以了。\x01",
            "您的随身行李和入境申请书，\x01",
            "已经确认完毕了。\x02\x03",

            "非常感谢您的配合。\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x8,
        "#5P没什么，不客气。\x02",
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x9,
        "#5P哼～那就快走吧！\x02",
    )

    CloseMessageWindow()
    OP_5A()
    SetChrSubChip(0x8, 0x0)
    SetChrSubChip(0x9, 0x0)
    OP_29(0x9, 0x1, 0x4)
    EventEnd(0x5)
    Return()

    # Function_18_25B1 end

    def Function_19_28F1(): pass

    label("Function_19_28F1")

    EventBegin(0x0)
    Fade(500)
    OP_68(1440, 1000, 3000, 0)
    MoveCamera(315, 28, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(15000, 0)
    SetChrPos(0x101, 800, 0, 2500, 45)
    SetChrSubChip(0xA, 0x2)
    OP_0D()

    #C0067
    ChrTalk(
        0x101,
        (
            "#5P#0000F不好意思，打扰了，我是代理安检官。\x02\x03",

            "麻烦您了，\x01",
            "能否让我确认一下您的\x01",
            "随身行李和入境申请书呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0xA,
        (
            "#12P啊啊，好好。\x01",
            "稍等一下啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0xA,
        "#12P……呵呵。\x02",
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x101,
        "#5P#0005F……那个……怎么了？\x02",
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0xA,
        "#12P没什么，失礼了。\x02",
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0xA,
        (
            "#12P我在想象，车窗外的风景……\x01",
            "尤其是诺克斯森林的那片新绿，\x01",
            "真是特别美丽啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0xA,
        (
            "#12P一想到发车以后就能欣赏到这些，\x01",
            "就不知不觉面露微笑了……\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x101,
        (
            "#5P#0000F嘿……\x01",
            "您真是很有雅兴啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0xA,
        (
            "#12P……啊，\x01",
            "抱歉，耽误你工作了。\x01",
            "你是来进行安检的吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x101,
        (
            "#5P#0005F啊……是的。\x02\x03",

            "#0000F那么，失礼了……\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(500, 0, -1)
    OP_0D()
    Sleep(2000)
    FadeToBright(500, 0)
    OP_0D()

    #C0077
    ChrTalk(
        0x101,
        (
            "#5P#0000F……您的随身行李与入境申请书\x01",
            "已经确认完毕了。\x02\x03",

            "非常感谢您的配合。\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0xA,
        "#12P哪里哪里，辛苦啦。\x02",
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0xA,
        (
            "#12P呵呵，话说回来，\x01",
            "真期待发车啊……\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrSubChip(0xA, 0x0)
    OP_29(0x9, 0x1, 0x5)
    EventEnd(0x5)
    Return()

    # Function_19_28F1 end

    def Function_20_2C02(): pass

    label("Function_20_2C02")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0x9)"), scpexpr(EXPR_END)), "loc_2E2A")
    EventBegin(0x0)
    Fade(500)
    OP_68(-1560, 1000, 0, 0)
    MoveCamera(320, 32, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17360, 0)
    SetChrPos(0x101, -150, 0, 0, 270)
    SetChrSubChip(0xB, 0x2)
    SetChrSubChip(0xC, 0x1)
    SetChrSubChip(0xD, 0x0)
    OP_4B(0xD, 0xFF)
    TurnDirection(0xD, 0x101, 0)
    OP_0D()

    #C0080
    ChrTalk(
        0xD,
        (
            "#5P喂～妈妈，我可不可以到旁边的\x01",
            "那节车厢里去探险呀？\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0xC,
        (
            "#12P不行～！在安检结束之前，\x01",
            "给我老实坐好！\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0xB,
        (
            "#11P是呀，\x01",
            "不然安检官先生可就要生气啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0xD,
        (
            "#5P哎～……可是，\x01",
            "坐在那边的那个大哥哥\x01",
            "就是从前面的车厢里跑进来的哦～！\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x101,
        (
            "#12P#0000F（前面的车厢……是指由库瓦特罗先生\x01",
            "　负责安检的那节车厢吧。）\x02\x03",

            "（那位乘客大概是有些事情\x01",
            "　要去找乘务员吧。）\x02\x03",

            "#0005F（咦，可是………\x01",
            "　……安检开始之后……\x01",
            "　就不能再移动到其它车厢了吧……？）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x70, 0)
    Jump("loc_3131")

    label("loc_2E2A")

    EventBegin(0x0)
    Fade(500)
    OP_68(-1560, 1000, 0, 0)
    MoveCamera(320, 32, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17360, 0)
    SetChrPos(0x101, -150, 0, 0, 270)
    SetChrSubChip(0xB, 0x1)
    SetChrSubChip(0xC, 0x2)
    SetChrSubChip(0xD, 0x0)
    OP_4B(0xD, 0xFF)
    TurnDirection(0xD, 0x101, 0)
    OP_0D()

    #C0085
    ChrTalk(
        0x101,
        (
            "#12P#0000F不好意思，打扰了，我是代理安检官。\x02\x03",

            "麻烦您了，\x01",
            "能否让我确认一下您的\x01",
            "随身行李和入境申请书呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0xB,
        (
            "#5P啊，是安检人员吗？\x01",
            "嗯，没问题。\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0xD,
        (
            "#5P我说，列车\x01",
            "还不发车吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0xD,
        "#5P我都已经等不及了。\x02",
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0xC,
        (
            "#6P这孩子真是\x01",
            "缺乏耐性……\x01",
            "呵呵，真不好意思啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x101,
        "#12P#0005F啊，不不，没关系的。\x02",
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x101,
        (
            "#12P#0000F抱歉啊，很不好意思，\x01",
            "不过还是请你再稍微坚持一下吧。\x02\x03",

            "在哥哥完成工作之前，\x01",
            "再乖乖等一会，好吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0xD,
        "#5P知道啦～\x02",
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x101,
        (
            "#12P#0003F（……动作尽量\x01",
            "　利落一点吧。）\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(500, 0, -1)
    OP_0D()
    Sleep(2000)
    FadeToBright(500, 0)
    OP_0D()

    #C0094
    ChrTalk(
        0x101,
        (
            "#12P#0000F……您的随身行李与入境申请书\x01",
            "已经确认完毕了。\x02\x03",

            "非常感谢您的配合。\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0xB,
        "#5P好的。\x02",
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0xD,
        (
            "#5P大哥哥，请你尽量\x01",
            "快点把工作完成吧～\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xC, 0x1)

    #C0097
    ChrTalk(
        0xC,
        "#6P喂！没礼貌。这孩子真是的……\x02",
    )

    CloseMessageWindow()
    OP_29(0x9, 0x1, 0x6)

    label("loc_3131")

    OP_5A()
    SetChrSubChip(0xB, 0x0)
    SetChrSubChip(0xC, 0x0)
    OP_93(0xD, 0xE1, 0x0)
    OP_4C(0xD, 0xFF)
    EventEnd(0x5)
    Return()

    # Function_20_2C02 end

    def Function_21_3148(): pass

    label("Function_21_3148")

    EventBegin(0x0)
    Fade(500)
    OP_68(-780, 1000, -2950, 0)
    MoveCamera(305, 30, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17320, 0)
    SetChrPos(0x101, -150, 0, -2500, 225)
    SetChrSubChip(0xE, 0x2)
    OP_0D()

    #C0098
    ChrTalk(
        0xE,
        "#5P嗯～？安检官……？\x02",
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0xE,
        (
            "#5P你全身上下有哪点像安检官啊。\x01",
            "给我看看证据啊，证据！\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0x101,
        (
            "#12P#0006F嗯，这个嘛……\x01",
            "（真是败给他了……）\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0101
    ChrTalk(
        0x101,
        (
            "#12P#0005F对、对了。\x01",
            "……这个，请您过目。\x02",
        )
    )

    CloseMessageWindow()
    Sound(804, 0, 100, 0)
    SetChrName("")

    #A0102
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "罗伊德拿出调查手册给乘客看。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0103
    ChrTalk(
        0x101,
        (
            "#12P#0000F我是警察局特别任务支援科的成员，\x01",
            "来协助进行安检……\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0xE,
        "#5P警察……哼，好像不是冒牌的。\x02",
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0xE,
        (
            "#5P总是这么没事找事……\x01",
            "算了，随便你吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0x101,
        "#12P#0005F……谢、谢谢您的谅解。\x02",
    )

    CloseMessageWindow()
    FadeToDark(500, 0, -1)
    OP_0D()
    Sleep(2000)
    FadeToBright(500, 0)
    OP_0D()

    #C0107
    ChrTalk(
        0x101,
        (
            "#12P#0000F……可以了。\x01",
            "您的随身行李与入境申请书\x01",
            "已经确认完毕了。\x02\x03",

            "非常感谢您的配合。\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0xE,
        (
            "#5P哼，不必多礼，与其说这些客套话，\x01",
            "倒不如快点把工作完成。\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0xE,
        "#5P我可是很赶时间的。\x02",
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0x101,
        "#12P#0006F真、真是失礼了。\x02",
    )

    CloseMessageWindow()
    OP_5A()
    SetChrSubChip(0xE, 0x0)
    OP_29(0x9, 0x1, 0x7)
    EventEnd(0x5)
    Return()

    # Function_21_3148 end

    def Function_22_3449(): pass

    label("Function_22_3449")

    EventBegin(0x0)
    Fade(500)
    OP_68(1430, 1000, -2180, 0)
    MoveCamera(315, 28, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(16540, 0)
    SetChrPos(0x101, 800, 0, -2500, 45)
    SetChrSubChip(0xF, 0x2)
    OP_0D()

    #C0111
    ChrTalk(
        0x101,
        (
            "#5P#0000F不好意思，打扰了，我是代理安检官。\x02\x03",

            "麻烦您了，\x01",
            "能否让我确认一下您的\x01",
            "随身行李和入境申请书呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0xF,
        (
            "#12P……安检官？\x01",
            "居然穿着便服，真是少见啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0xF,
        (
            "#12P……不过，你这算是什么意思啊？\x01",
            "是不是觉得一个女人独自\x01",
            "出来旅行，是件很奇怪的事情？\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0x101,
        "#5P#0005F哎？不不，没有没有，我完全没那样想……\x02",
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0xF,
        (
            "#12P我本来也想和男朋友\x01",
            "一起来旅游的啊！\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0xF,
        (
            "#12P可是昨天却突然被他甩了，\x01",
            "所以才会一个人来旅行，这也是没办法的吧！？\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0xF,
        (
            "#12P但我绝对不会就这么认输的！\x01",
            "一定要在帝国找到一个\x01",
            "超级有钱的新男友……！！\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0x101,
        (
            "#5P#0011F（唔……好像被她\x01",
            "　当作发泄对象了。）\x02\x03",

            "#0006F（没办法，\x01",
            "　只能一边听她说，\x01",
            "　一边进行安检工作了……）\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(500, 0, -1)
    OP_0D()
    Sleep(2000)
    FadeToBright(500, 0)
    OP_0D()

    #C0119
    ChrTalk(
        0xF,
        (
            "#12P……你明白了吗？安检官先生。\x01",
            "那个混蛋男人是不是很过分啊……？\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0x101,
        (
            "#5P#0012F确、确实是啊……\x02\x03",

            "#0000F啊，那个……\x01",
            "您的随身行李与入境申请书\x01",
            "已经确认完毕了。\x02\x03",

            "非常感谢您的配合。\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0xF,
        "#12P…………………………\x02",
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0x101,
        "#5P#0005F……那、那个，还有什么事吗？\x02",
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0xF,
        "#12P……嗯，没什么了。\x02",
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0xF,
        (
            "#12P总觉得，和你说完这些之后，\x01",
            "心情一下爽快了很多。\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0xF,
        (
            "#12P真是好久都没遇到过\x01",
            "可以这么耐心听我说话的人了……\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0xF,
        "#12P那个，如果你愿意的话，我们两个不如就……\x02",
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0x101,
        (
            "#5P#0011F我、我还有工作在身……\x01",
            "先失陪了！\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrSubChip(0xF, 0x0)
    OP_29(0x9, 0x1, 0x8)
    EventEnd(0x5)
    Return()

    # Function_22_3449 end

    def Function_23_391C(): pass

    label("Function_23_391C")

    EventBegin(0x0)
    Fade(500)
    OP_68(0, 1000, -7350, 0)
    MoveCamera(315, 28, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(15000, 0)
    SetChrPos(0x101, 0, 0, -7350, 180)
    OP_0D()

    #C0128
    ChrTalk(
        0x101,
        (
            "#11P#0006F呼……这样一来，总算是\x01",
            "对全员都进行过安检了啊。\x02\x03",

            "#0000F并没有发现任何可疑人物，\x01",
            "接下来只要与大家会合，\x01",
            "再去向库瓦特罗先生报告，就算是完成任务了。\x02\x03",

            "#0003F………………………………\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0x101, 0x0, 0x1F4)
    Sleep(300)

    #C0129
    ChrTalk(
        0x101,
        (
            "#5P#0003F这种工作还是第一次做，\x01",
            "难免会有些紧张……\x02\x03",

            "#0001F会不会有什么\x01",
            "失误或遗漏呢……？\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    ModifyEventFlags(1, 0, 0x80)
    OP_29(0x9, 0x1, 0x9)
    EventEnd(0x5)
    Return()

    # Function_23_391C end

    def Function_24_3AB1(): pass

    label("Function_24_3AB1")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0x9)"), scpexpr(EXPR_END)), "loc_3B67")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【结束安检工作，到外面去】\x01",      # 0
            "【继续进行安检工作】\x01",            # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3B4C")
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0x7D0)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x5C, 2)
    NewScene("c0800", 0, 0, 0)
    IdleLoop()
    Jump("loc_3B62")

    label("loc_3B4C")

    Sleep(50)
    SetChrPos(0x0, 2000, 0, -7850, 270)
    EventEnd(0x4)

    label("loc_3B62")

    Jump("loc_3BB8")

    label("loc_3B67")


    #C0130
    ChrTalk(
        0x101,
        (
            "#0001F……安检工作还没有完成，\x01",
            "现在还不能离开列车啊。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, 2000, 0, -7850, 270)
    EventEnd(0x4)

    label("loc_3BB8")

    Return()

    # Function_24_3AB1 end

    def Function_25_3BB9(): pass

    label("Function_25_3BB9")

    EventBegin(0x0)
    Fade(500)
    OP_68(1440, 1000, 3000, 0)
    MoveCamera(315, 28, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(15000, 0)
    SetChrPos(0x101, 800, 0, 2500, 45)
    SetChrSubChip(0xA, 0x2)
    OP_0D()

    #C0131
    ChrTalk(
        0xA,
        (
            "#12P啊啊，真是期待啊。\x01",
            "可以看到车窗外的景色。\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0xA,
        "#12P……真希望能快点发车呢。\x02",
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0x101,
        (
            "#5P#0001F……不好意思，\x01",
            "可以稍微打扰您一下吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0xA,
        "#12P喔，怎么了？\x02",
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0xA,
        (
            "#12P安检不是\x01",
            "已经结束了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0x101,
        (
            "#5P#0003F嗯，但有件事令我稍微有些在意。\x02\x03",

            "#0001F如果方便的话，可以再\x01",
            "配合我做一次安检吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0xA,
        (
            "#12P……啊，这倒是没问题。\x01",
            "是不是有什么东西忘记检查了？\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0xA,
        (
            "#12P看啊，我的行李和入境申请书\x01",
            "都在这里……\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0x101,
        (
            "#5P#0003F不，要进行安检的人\x01",
            "并不是我。\x02\x03",

            "#0001F而是真正的安检官……\x01",
            "接下来的事情就交给\x01",
            "库瓦特罗先生吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0140
    ChrTalk(
        0xA,
        (
            "#12P为、为什么是库瓦特罗……？\x01",
            "由你来检查不就足够了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0x101,
        "#5P#0003F……您果然认识他啊。\x02",
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0142
    ChrTalk(
        0xA,
        "#12P啊……不、不是啦，那个……\x02",
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0x101,
        (
            "#5P#0003F……在开始这次安检之前，\x01",
            "我从库瓦特罗先生那里学习到了\x01",
            "几条关于安检工作的基本规则。\x02\x03",

            "#0001F其中之一就是……\x01",
            "『在安检中，不可移动至其它车厢』。\x01",
            "就是这样。\x02",
        )
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0xA,
        "#12P嗯……这我当然知道。\x02",
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0xA,
        "#12P你难道是想说我违反了这条规则吗？\x02",
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0x101,
        (
            "#5P#0001F很遗憾……正是如此，\x01",
            "因为有目击证人。\x02\x03",

            "坐在斜对面座位上的那个小男孩\x01",
            "亲眼看到你从前面的那节车厢\x01",
            "跑到了这里。\x02",
        )
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0xA,
        "#12P……骗、骗人的吧……！？\x02",
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0xA,
        (
            "#12P那、那个，也许只是不小心\x01",
            "看错了吧，这种事情也常有……\x02",
        )
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0x101,
        (
            "#5P#0003F是不是真的看错了，只需去问一问\x01",
            "首节车厢的乘务员，马上就可以真相大白了吧。\x02\x03",

            "#0001F比起这个，更加关键的问题是……\x01",
            "你为什么要这么做。\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0xA,
        "#12P唔……\x02",
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0x101,
        (
            "#5P#0003F按照规则，\x01",
            "你应该留在那节车厢内，\x01",
            "等待接受库瓦特罗先生的检查。\x02\x03",

            "可是你却无视这条规定，跑到了这节车厢，\x01",
            "而且还装出一副若无其事的样子，\x01",
            "你这么做的理由……\x02\x03",

            "#0001F自然是为了逃避\x01",
            "库瓦特罗先生的检查。\x02\x03",

            "……我说的没错吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0xA,
        "#12P……啊……啊啊啊……\x02",
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)

    #C0153
    ChrTalk(
        0xA,
        (
            "#12P──求……求你了！\x01",
            "能不能放我一马呢！？\x02",
        )
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0xA,
        (
            "#12P我……我只是想开心地旅行，\x01",
            "仅此而已啊！\x02",
        )
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0xA,
        (
            "#12P看、看啊……我的入境申请书\x01",
            "并没有什么不妥的地方吧？\x01",
            "所以……\x02",
        )
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0x101,
        (
            "#5P#0003F──既然如此……\x01",
            "就算拿给库瓦特罗先生看一看，\x01",
            "也不会有什么问题的，不是吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_64(0xFFFF)

    #C0157
    ChrTalk(
        0xA,
        "#12P……！这、这个……\x02",
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0x101,
        (
            "#0008F我虽然不了解事情的详情……\x02\x03",

            "#0001F但身为代理安检官，\x01",
            "既然发现你做出了可疑的举动，\x01",
            "自然不能就这么视而不见。\x02\x03",

            "#0003F……请跟我走一趟吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0xA,
        "#12P……啊………啊啊………………\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_29(0x9, 0x1, 0xB)
    StopBGM(0xFA0)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x5C, 2)
    NewScene("c0800", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_25_3BB9 end

    def Function_26_443F(): pass

    label("Function_26_443F")

    EventBegin(0x1)
    OP_D0(0x5, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Call(0, 2)
    SetChrPos(0x0, 100, 0, -8640, 0)
    OP_68(100, 1000, -8640, 0)
    MoveCamera(315, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(20000, 0)
    Jc((scpexpr(EXPR_23, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x1, 0xD)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_44AB")
    Call(0, 30)
    Jump("loc_44AD")

    label("loc_44AB")

    EventEnd(0x4)

    label("loc_44AD")

    Return()

    # Function_26_443F end

    def Function_27_44AE(): pass

    label("Function_27_44AE")

    EventBegin(0x1)
    OP_D0(0x5, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_SUB_SAVE), scpexpr(EXPR_END)))
    Call(0, 2)
    SetChrPos(0x0, 90, 0, 8340, 180)
    OP_68(90, 1000, 8340, 0)
    MoveCamera(315, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(20000, 0)
    EventEnd(0x4)
    Return()

    # Function_27_44AE end

    def Function_28_44FE(): pass

    label("Function_28_44FE")

    EventBegin(0x1)

    #C0160
    ChrTalk(
        0x101,
        (
            "#0001F……去试着说服卡拉小姐吧。\x02\x03",

            "再继续磨磨蹭蹭的话，\x01",
            "就该到达阿尔泰尔市了。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, 10, 0, 7210, 180)
    EventEnd(0x4)
    Return()

    # Function_28_44FE end

    def Function_29_456A(): pass

    label("Function_29_456A")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(280, 1000, 2990, 0)
    MoveCamera(315, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(20000, 0)
    SetChrPos(0x101, 1800, 0, -7650, 270)
    SetChrPos(0x102, 1800, 0, -8780, 270)
    SetChrPos(0x103, 2950, 0, -8780, 270)
    SetChrPos(0x104, 2950, 0, -7650, 270)
    BeginChrThread(0x101, 3, 0, 33)
    SetMapObjFlags(0x4, 0x4)
    OP_74(0x5, 0x2D)
    OP_71(0x5, 0xF0, 0x0, 0x0, 0x20)
    FadeToBright(2000, 0)
    OP_0D()
    OP_68(760, 1000, -4250, 4000)
    Sleep(4300)
    Fade(500)
    OP_68(1750, 1000, -7500, 0)
    SetCameraDistance(16500, 0)
    OP_0D()

    #C0161
    ChrTalk(
        0x103,
        "#6P#0200F总算赶上了呢。\x02",
    )

    CloseMessageWindow()

    def lambda_4664():
        TurnDirection(0xFE, 0x103, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4664)
    Sleep(15)

    def lambda_4674():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_4674)
    Sleep(12)

    def lambda_4684():
        TurnDirection(0xFE, 0x104, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4684)
    Sleep(20)

    def lambda_4694():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_4694)
    Sleep(300)

    #C0162
    ChrTalk(
        0x102,
        (
            "#6P#0106F我们没接受安检呢，\x01",
            "没问题吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0x101,
        (
            "#11P#0003F警官为了执行任务，\x01",
            "应该是可以紧急乘车的……\x01",
            "这个倒是不用担心。\x02\x03",

            "#0001F不过，现在要考虑的问题是，\x01",
            "接下来应该怎么做。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)
    TurnDirection(0x102, 0x101, 400)
    Sleep(300)

    #C0164
    ChrTalk(
        0x102,
        (
            "#6P#0105F还是应该先去试着\x01",
            "说服卡拉小姐吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0x104,
        (
            "#11P#0303F不过，话虽如此，\x01",
            "但总不能在车上耗太久，\x01",
            "就这么一直坐下去吧。\x02\x03",

            "#0301F我们还要赶快把\x01",
            "那个药给送到乌尔斯拉\x01",
            "医科大学去呢。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x104, 400)
    Sleep(300)

    #C0166
    ChrTalk(
        0x103,
        (
            "#6P#0203F……说得也是呢。\x02\x03",

            "#0200F不过，既然都走到这一步了，\x01",
            "总不能就此放弃。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x1)
    Sleep(1800)

    #C0167
    ChrTalk(
        0x101,
        (
            "#5P#0003F下一次停车的车站是\x01",
            "共和国西端的阿尔泰尔市……\x02\x03",

            "#0001F大概三十分钟左右就到了。\x02\x03",

            "在那之前，我们就抓紧时间，\x01",
            "尽量说服她，让她回家吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0x104,
        "#11P#0300F了解，那我们这就行动吧。\x02",
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0x102,
        (
            "#6P#0108F是啊……希望\x01",
            "她能把话听进去……\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, 2480, 0, -8200, 270)
    OP_29(0x2D, 0x1, 0xC)
    EventEnd(0x5)
    Return()

    # Function_29_456A end

    def Function_30_49A7(): pass

    label("Function_30_49A7")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(100, 1000, -8640, 0)
    MoveCamera(315, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17060, 0)
    SetChrPos(0x101, 830, 0, -7830, 0)
    SetChrPos(0x102, -300, 0, -7830, 0)
    SetChrPos(0x103, 830, 0, -8680, 0)
    SetChrPos(0x104, -300, 0, -8680, 0)
    Sleep(500)
    FadeToBright(1000, 0)
    OP_0D()
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)
    OP_68(-2760, 1000, 3450, 2500)
    Sleep(2500)

    #C0170
    ChrTalk(
        0x102,
        "#0105F（是卡拉小姐……）\x02",
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0x104,
        "#0300F（嘿，终于发现了啊。）\x02",
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0x103,
        (
            "#0200F（试着去说服她，\x01",
            "  让她答应回家吧。）\x02\x03",

            "（虽然不知道她是否\x01",
            "  能听进我们的话……）\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, 100, 0, -8640, 0)
    OP_29(0x2D, 0x1, 0xD)
    EventEnd(0x5)
    Return()

    # Function_30_49A7 end

    def Function_31_4B11(): pass

    label("Function_31_4B11")

    EventBegin(0x1)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EventBegin(0x0)
    OP_68(-1200, 700, 2970, 0)
    MoveCamera(332, 25, 0, 0)
    OP_6E(360, 0)
    SetCameraDistance(23510, 0)
    SetChrPos(0x101, -280, 0, 2800, 286)
    SetChrPos(0x102, -430, 0, 1750, 286)
    SetChrPos(0x103, 590, 0, 1300, 286)
    SetChrPos(0x104, 740, 0, 2430, 286)
    SetCameraDistance(22500, 2000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x10)

    #C0173
    ChrTalk(
        0x10,
        (
            "#5P玛夏，难道还是\x01",
            "没能赶上吗……\x02",
        )
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0x10,
        (
            "#5P那我不就是一个人了……\x01",
            "……没问题吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0x102,
        "#6P#0100F好久不见了，卡拉小姐。\x02",
    )

    CloseMessageWindow()
    OP_63(0x10, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    SetChrSubChip(0x10, 0x1)
    Sleep(200)

    #C0176
    ChrTalk(
        0x10,
        "#5P艾莉小姐……？\x02",
    )

    CloseMessageWindow()
    OP_63(0x10, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(800)

    #C0177
    ChrTalk(
        0x10,
        (
            "#5P真、真巧呢，\x01",
            "竟然会在这里遇见你。\x02",
        )
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0x10,
        "#5P那几位都是你的朋友吧……\x02",
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0x10,
        (
            "#5P莫非，你们有事情\x01",
            "要去共和国吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0x102,
        (
            "#6P#0109F啊哈哈……那个……\x01",
            "（该怎么应对才好呢……）\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【其实我们是来带你回去的】\x01",      # 0
            "【我们准备到共和国去观光】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    FadeToBright(300, 0)
    OP_60(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4F4C")
    OP_63(0x10, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1200)

    #C0181
    ChrTalk(
        0x10,
        "#5P难、难道是父亲指使你来的吗……！？\x02",
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0x10,
        (
            "#5P我、我可真是看错你了！！\x01",
            "他们几个也都是你的同伙吧！\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x10, 0x2)
    Sleep(200)

    #C0183
    ChrTalk(
        0x10,
        (
            "#5P哼……不要。\x01",
            "我绝对不会回去的！\x02",
        )
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0x101,
        "#11P#0006F（这么直接果然不行啊。）\x02",
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0x104,
        "#12P#0303F（看起来，的确是这样……）\x02",
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0x102,
        (
            "#6P#0106F（实在是抱歉，\x01",
            "　我好像把事情给搞糟了。）\x02",
        )
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0x103,
        (
            "#12P#0203F总之，能不能先把你\x01",
            "离家出走的原因向我们说说呢？\x02\x03",

            "#0200F从你留下的字条来看，\x01",
            "我想，好像是有一些\x01",
            "特别的原因吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_50A3")

    label("loc_4F4C")

    OP_2C(0x2D, 0x1)

    #C0188
    ChrTalk(
        0x102,
        (
            "#6P#0100F嗯，我们几个\x01",
            "想去共和国欣赏\x01",
            "国立乐团的表演。\x02",
        )
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0x10,
        (
            "#5P啊，这样的话，在达到共和国的首都之前，\x01",
            "我们就可以一直在一起了。\x02",
        )
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0x10,
        (
            "#5P太好了……\x01",
            "其、其实我稍微有些不安呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0191
    ChrTalk(
        0x10,
        (
            "#5P那个，因为出了一些事情，\x01",
            "而我现在又是一个人……\x02",
        )
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0x101,
        (
            "#11P#0003F（好，总算是引出了她的话，\x01",
            "　应该可以进一步问下去了……）\x02\x03",

            "#0000F那到底是什么事情呢……？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_50A3")


    #C0193
    ChrTalk(
        0x10,
        "#5P那、那个……\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x10, 0x2)
    Sleep(200)

    #C0194
    ChrTalk(
        0x10,
        (
            "#5P父亲总是只考虑自己，\x01",
            "蛮不讲理地制订一大堆规矩要别人遵守，\x01",
            "可他自己却从来都无法遵守。\x02",
        )
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0x10,
        "#5P……今天早上，更是过分到了极点。\x02",
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0x10,
        (
            "#5P那种行为…\x01",
            "我绝对不会原谅的……！\x02",
        )
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0x102,
        "#6P#0105F那种行为……？\x02",
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0x101,
        "#11P#0005F………究竟是什么呢………\x02",
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0x10,
        "#5P……………………………\x02",
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0x10,
        (
            "#5P吃过早饭之后，他没有敲门\x01",
            "就直接进入我的房间了。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    #C0201
    ChrTalk(
        0x104,
        "#12P#0305F哎……只是这样而已啊？\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x10, 0x1)
    Sleep(200)

    #C0202
    ChrTalk(
        0x10,
        (
            "#5P当然不只是这样而已！\x01",
            "我当时可是正在换衣服啊！\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x10, 0x0)
    Sleep(200)

    #C0203
    ChrTalk(
        0x10,
        (
            "#5P而且，『进屋之前先敲门』\x01",
            "这条规矩是父亲自己定的，\x01",
            "平时总是唠唠叨叨地提醒别人！\x02",
        )
    )

    CloseMessageWindow()

    #C0204
    ChrTalk(
        0x10,
        (
            "#5P只要别人偶尔疏忽，没有遵守，\x01",
            "他就抱怨个没完没了，可是……\x02",
        )
    )

    CloseMessageWindow()

    #C0205
    ChrTalk(
        0x10,
        (
            "#5P他今天早上却大摇大摆地走进来，\x01",
            "还让我中午之前做这个、做那个，\x01",
            "然后晚上还要去参加什么晚宴……！\x02",
        )
    )

    CloseMessageWindow()

    #C0206
    ChrTalk(
        0x10,
        (
            "#5P他总是这样\x01",
            "对我的私生活\x01",
            "指手划脚个没完没了……！\x02",
        )
    )

    CloseMessageWindow()

    #C0207
    ChrTalk(
        0x103,
        (
            "#12P#0203F（她的心情确实可以理解，不过……\x01",
            "　这听上去只是极为常见的\x01",
            "　『父女之间的矛盾』吧。）\x02",
        )
    )

    CloseMessageWindow()

    #C0208
    ChrTalk(
        0x101,
        "#11P#0003F（嗯～我认为……）\x02",
    )

    CloseMessageWindow()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【确实是令尊做得不对啊】\x01",          # 0
            "【事先把房间的门反锁如何？】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    FadeToBright(300, 0)
    OP_60(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_558C")
    OP_2C(0x2D, 0x1)

    #C0209
    ChrTalk(
        0x101,
        (
            "#11P#0006F这确实是令尊做得不对啊，\x01",
            "真令人同情。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x10, 0x1)
    Sleep(200)

    #C0210
    ChrTalk(
        0x10,
        "#5P果、果然是这样没错吧。\x02",
    )

    CloseMessageWindow()

    #C0211
    ChrTalk(
        0x10,
        (
            "#5P哼……看来我今天离家出走，\x01",
            "果然是正确的选择。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_56A7")

    label("loc_558C")


    #C0212
    ChrTalk(
        0x101,
        (
            "#11P#0006F那个……你不如\x01",
            "事先把房间的门反锁吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x10, 0x0, 1600, 0x2C, 0x2F, 0x96, 0x1)
    Sound(25, 0, 100, 0)
    SetChrSubChip(0x10, 0x1)
    Sleep(1200)

    #C0213
    ChrTalk(
        0x10,
        (
            "#5P问题的重点并不在这里！\x01",
            "我都说过了，我最不能容忍的是，\x01",
            "他总是这么自私，只为自己考虑！\x02",
        )
    )

    CloseMessageWindow()

    #C0214
    ChrTalk(
        0x10,
        (
            "#5P哼……够了，就这样吧。\x01",
            "我要去共和国。\x02",
        )
    )

    CloseMessageWindow()

    #C0215
    ChrTalk(
        0x10,
        (
            "#5P至于父亲，就留他一个人在家，\x01",
            "他爱怎么样就怎么样吧！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_56A7")

    SetChrSubChip(0x10, 0x0)
    Sleep(300)
    OP_63(0x10, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x1)
    Sleep(1800)

    #C0216
    ChrTalk(
        0x10,
        (
            "#5P不过……我还是第一次\x01",
            "离开克洛斯贝尔呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0217
    ChrTalk(
        0x10,
        (
            "#5P唉，玛夏说过要和我一起走，\x01",
            "所以我才能下定决心出来，\x01",
            "可是……\x02",
        )
    )

    CloseMessageWindow()

    #C0218
    ChrTalk(
        0x104,
        (
            "#12P#0303F（情况已经大致弄清了……\x01",
            "　看样子，她好像\x01",
            "　还是很犹豫不决呢。）\x02",
        )
    )

    CloseMessageWindow()

    #C0219
    ChrTalk(
        0x102,
        (
            "#6P#0108F（她心里原本就\x01",
            "　觉得很没有着落吧……）\x02\x03",

            "（虽然一时冲动，离家出走了，\x01",
            "　却渐渐开始感到不安，\x01",
            "　这也是不足为奇的。）\x02",
        )
    )

    CloseMessageWindow()

    #C0220
    ChrTalk(
        0x101,
        (
            "#11P#0003F（是吗……既然如此，\x01",
            "　我们就一鼓作气……）\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【一个人旅行，毕竟还是很危险的】\x01",      # 0
            "【令尊其实也很担心你的】\x01",              # 1
            "【女仆小姐也很担心你的】\x01",              # 2
        )
    )

    MenuEnd(0x0)
    FadeToBright(300, 0)
    OP_60(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5D7E")
    OP_2C(0x2D, 0x5)
    OP_63(0x10, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    SetChrSubChip(0x10, 0x1)
    Sleep(1000)

    #C0221
    ChrTalk(
        0x10,
        (
            "#5P说起来，我根本就没有\x01",
            "看到玛夏的身影呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0222
    ChrTalk(
        0x10,
        (
            "#5P……难道她\x01",
            "背叛了我吗！？\x02",
        )
    )

    CloseMessageWindow()

    #C0223
    ChrTalk(
        0x10,
        (
            "#5P不、不可原谅……\x01",
            "我明明和她说过，不要告诉任何人的……！\x02",
        )
    )

    CloseMessageWindow()

    #C0224
    ChrTalk(
        0x102,
        (
            "#6P#0105F请冷静一点，卡拉小姐。\x02\x03",

            "#0103F玛夏小姐确实把\x01",
            "你的事情告诉我们了。\x02\x03",

            "#0100F但她正是因为非常担心你，\x01",
            "所以才会这么做的。\x02",
        )
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0x103,
        (
            "#12P#0200F嗯，其实卡拉小姐并不是\x01",
            "真心想要离开克洛斯贝尔。\x01",
            "玛夏小姐是这样说的。\x02",
        )
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0x10,
        (
            "#5P玛夏……\x01",
            "真的说过那种话吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0227
    ChrTalk(
        0x101,
        (
            "#11P#0000F小姐就拜托各位了——\x01",
            "这是她的原话，所以我们才来到了这里。\x02",
        )
    )

    CloseMessageWindow()

    #C0228
    ChrTalk(
        0x104,
        (
            "#12P#0304F算了，毕竟只是父女之间的摩擦，\x01",
            "还是应该心平气和地好好谈一谈吧。\x02\x03",

            "#0300F与其离家逃跑，倒不如理直气壮地\x01",
            "把你的不满表达清楚。只有这样，才能\x01",
            "真正解开自己的心结，没错吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0229
    ChrTalk(
        0x10,
        "#5P说的……也对啊……\x02",
    )

    CloseMessageWindow()

    #C0230
    ChrTalk(
        0x10,
        (
            "#5P我一直都觉得……\x01",
            "周围没有任何人站在我这边……\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x10, 0x0)
    Sleep(200)
    OP_63(0x10, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x1)
    Sleep(1800)

    #C0231
    ChrTalk(
        0x10,
        (
            "#5P不过，既然有玛夏和各位支持我，\x01",
            "回去应该也可以吧……\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x10, 0x1)
    Sleep(200)

    #C0232
    ChrTalk(
        0x10,
        (
            "#5P那个，各位……\x01",
            "能不能再稍微\x01",
            "听我发一会牢骚呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0233
    ChrTalk(
        0x10,
        (
            "#5P见到父亲以后，要对他说些什么，\x01",
            "要趁现在想清楚才行。\x02",
        )
    )

    CloseMessageWindow()

    #C0234
    ChrTalk(
        0x101,
        "#11P#0000F哈哈，也是呢。\x02",
    )

    CloseMessageWindow()

    #C0235
    ChrTalk(
        0x103,
        (
            "#12P#0200F差不多也快到达阿尔泰尔市了，\x01",
            "应该还能赶上回去的列车。\x02",
        )
    )

    CloseMessageWindow()

    #C0236
    ChrTalk(
        0x102,
        (
            "#6P#0100F如果不嫌弃，\x01",
            "我们很愿意陪你一起回去哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_29(0x2D, 0x1, 0xE)
    BeginChrThread(0x19, 0, 0, 34)
    FadeToDark(2000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 1)
    SetScenarioFlags(0x5C, 3)
    NewScene("c0800", 0, 0, 0)
    IdleLoop()
    Jump("loc_5FF6")

    label("loc_5D7E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5E0C")

    #C0237
    ChrTalk(
        0x10,
        (
            "#5P呜……\x01",
            "我当然明白啊。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x10, 0x2)
    Sleep(200)

    #C0238
    ChrTalk(
        0x10,
        (
            "#5P不过，正因为明白，所以才更要出走呢！\x01",
            "必须要让父亲体会到\x01",
            "我的决心有多么坚定！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5E82")

    label("loc_5E0C")

    SetChrSubChip(0x10, 0x1)
    Sleep(200)

    #C0239
    ChrTalk(
        0x10,
        (
            "#5P……你们果然是父亲\x01",
            "雇来的帮手吧……\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x10, 0x2)
    Sleep(200)

    #C0240
    ChrTalk(
        0x10,
        "#5P哼，让他担心死才好呢。\x02",
    )

    CloseMessageWindow()

    #C0241
    ChrTalk(
        0x10,
        "#5P我是绝对不会回去的！\x02",
    )

    CloseMessageWindow()

    label("loc_5E82")


    #C0242
    ChrTalk(
        0x101,
        (
            "#11P#0006F是、是吗……\x02\x03",

            "#0008F（到了这个地步，要想继续说服她的话，\x01",
            "  恐怕就很困难了……）\x02",
        )
    )

    CloseMessageWindow()

    #C0243
    ChrTalk(
        0x103,
        (
            "#12P#0200F（嗯，而且差不多也该到达\x01",
            "  阿尔泰尔市了。）\x02",
        )
    )

    CloseMessageWindow()

    #C0244
    ChrTalk(
        0x104,
        "#12P#0306F（ＧＡＭＥＯＶＥＲ了吗……）\x02",
    )

    CloseMessageWindow()

    #C0245
    ChrTalk(
        0x102,
        (
            "#6P#0100F卡拉小姐……\x01",
            "那么，请你至少把联络地址\x01",
            "告诉我们，可以吗？\x02\x03",

            "至少也要把这个转告给议员，\x01",
            "然后请求他多加理解。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_29(0x2D, 0x1, 0xF)
    BeginChrThread(0x19, 0, 0, 34)
    FadeToDark(2000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 1)
    SetScenarioFlags(0x5C, 3)
    NewScene("c0800", 0, 0, 0)
    IdleLoop()

    label("loc_5FF6")

    Return()

    # Function_31_4B11 end

    def Function_32_5FF7(): pass

    label("Function_32_5FF7")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch20802.itc", 0x1E)
    LoadChrToIndex("chr/ch20902.itc", 0x1F)
    LoadChrToIndex("chr/ch00002.itc", 0x20)
    LoadChrToIndex("apl/ch50000.itc", 0x21)
    LoadChrToIndex("chr/ch20002.itc", 0x22)
    LoadChrToIndex("chr/ch20102.itc", 0x23)
    LoadChrToIndex("chr/ch21202.itc", 0x24)
    LoadChrToIndex("chr/ch20402.itc", 0x25)
    LoadChrToIndex("chr/ch20502.itc", 0x26)
    LoadChrToIndex("chr/ch22002.itc", 0x27)
    SoundLoad(450)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis000.itp")
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis150.itp")
    OP_68(-2530, 900, 950, 0)
    MoveCamera(300, 18, 0, 0)
    OP_6E(420, 0)
    SetCameraDistance(19000, 0)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x21)
    SetChrSubChip(0x101, 0x0)
    SetChrPos(0x101, -2300, 150, 750, 180)
    SetChrChipByIndex(0x11, 0x1E)
    SetChrSubChip(0x11, 0x0)
    SetChrChipByIndex(0x12, 0x1F)
    SetChrSubChip(0x12, 0x0)
    SetChrFlags(0x11, 0x8000)
    SetChrPos(0x11, -1600, 150, -750, 0)
    SetChrFlags(0x12, 0x8000)
    SetChrPos(0x12, -2600, 150, -750, 0)
    ClearChrFlags(0x11, 0x80)
    ClearChrBattleFlags(0x11, 0x8000)
    ClearChrFlags(0x12, 0x80)
    ClearChrBattleFlags(0x12, 0x8000)
    SetChrChipByIndex(0x13, 0x22)
    SetChrSubChip(0x13, 0x0)
    SetChrChipByIndex(0x14, 0x23)
    SetChrSubChip(0x14, 0x0)
    SetChrChipByIndex(0x15, 0x24)
    SetChrSubChip(0x15, 0x0)
    SetChrChipByIndex(0x16, 0x25)
    SetChrSubChip(0x16, 0x0)
    SetChrChipByIndex(0x17, 0x26)
    SetChrSubChip(0x17, 0x0)
    SetChrChipByIndex(0x18, 0x27)
    SetChrSubChip(0x18, 0x0)
    SetChrFlags(0x13, 0x8000)
    SetChrFlags(0x14, 0x8000)
    SetChrFlags(0x15, 0x8000)
    SetChrFlags(0x16, 0x8000)
    SetChrFlags(0x17, 0x8000)
    SetChrFlags(0x18, 0x8000)
    SetChrPos(0x13, 1900, 150, 750, 180)
    SetChrPos(0x14, 2900, 150, 750, 180)
    SetChrPos(0x15, -1900, 150, -3300, 0)
    SetChrPos(0x16, 2200, 150, 1800, 0)
    SetChrPos(0x17, 2200, 150, 3300, 180)
    SetChrPos(0x18, -2000, 150, 3300, 180)
    ClearChrFlags(0x13, 0x80)
    ClearChrBattleFlags(0x13, 0x8000)
    ClearChrFlags(0x14, 0x80)
    ClearChrBattleFlags(0x14, 0x8000)
    ClearChrFlags(0x15, 0x80)
    ClearChrBattleFlags(0x15, 0x8000)
    ClearChrFlags(0x16, 0x80)
    ClearChrBattleFlags(0x16, 0x8000)
    ClearChrFlags(0x17, 0x80)
    ClearChrBattleFlags(0x17, 0x8000)
    ClearChrFlags(0x18, 0x80)
    ClearChrBattleFlags(0x18, 0x8000)
    SetMapObjFlags(0x4, 0x4)
    OP_74(0x5, 0x1E)
    OP_71(0x5, 0x0, 0xF0, 0x0, 0x20)
    Sleep(500)
    Sound(2179, 255, 60, 0)    #voice#KeA
    Sleep(2000)
    BeginChrThread(0x101, 3, 0, 33)
    SetMapObjFlags(0x4, 0x4)
    OP_74(0x5, 0x2D)
    OP_71(0x5, 0x0, 0xF0, 0x0, 0x20)
    Sound(450, 2, 0, 0)
    BeginChrThread(0x19, 0, 0, 35)
    Sleep(3000)
    SetCameraDistance(21000, 5000)
    FadeToBright(5000, 0)
    OP_0D()
    OP_6F(0x10)
    Fade(250)
    SetChrSubChip(0x101, 0x1)
    Sound(820, 0, 100, 0)
    OP_0D()
    #Sound(1078, 255, 100, 0)    #voice#Lloyd

    #N0246
    NpcTalk(
        0x101,
        "？？？",
        "#11P──啊！？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrSubChip(0x101, 0x8)
    Sleep(50)
    SetChrSubChip(0x101, 0x9)
    Sleep(50)
    SetChrSubChip(0x101, 0x8)
    Sleep(50)
    SetChrSubChip(0x101, 0x1)
    Sleep(50)
    SetChrSubChip(0x101, 0x8)
    Sleep(50)
    SetChrSubChip(0x101, 0x9)
    Sleep(50)
    SetChrSubChip(0x101, 0x8)
    Sleep(50)
    SetChrSubChip(0x101, 0x1)
    Sleep(500)
    Fade(250)
    ClearChrFlags(0x101, 0x20)
    ClearChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x20)
    SetChrSubChip(0x101, 0x0)
    OP_0D()
    SetChrSubChip(0x101, 0x1)
    Sleep(800)
    SetChrSubChip(0x101, 0x2)
    Sleep(1000)
    #Sound(1079, 255, 100, 0)    #voice#Lloyd

    #C0247
    ChrTalk(
        0x101,
        "#11P#60W……这里是………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    PlayBGM("ed7200", 0)
    Sleep(500)
    SetChrSubChip(0x101, 0x0)
    Sleep(500)
    OP_63(0x101, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)

    #C0248
    ChrTalk(
        0x101,
        (
            "#11P#0006F#30W是吗……对了，想起来了。\x02\x03",

            "#30W和叔叔他们道别之后……\x01",
            "托运了行李，随后就乘上了列车……\x02\x03",

            "#0008F#40W…………然后………………\x02",
        )
    )

    CloseMessageWindow()

    #N0249
    NpcTalk(
        0x12,
        "老妇人的声音",
        "#1P……小伙子，你不要紧吧？\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Fade(500)
    OP_68(-2300, 900, 750, 0)
    MoveCamera(237, 21, 0, 0)
    OP_6E(420, 0)
    SetCameraDistance(21000, 0)
    OP_68(-2300, 900, 0, 1500)
    OP_0D()
    OP_6F(0x1)

    #C0250
    ChrTalk(
        0x11,
        "好像已经醒过来了啊。\x02",
    )

    CloseMessageWindow()

    #C0251
    ChrTalk(
        0x11,
        (
            "你刚才似乎在做噩梦呢，\x01",
            "是不是哪里不太舒服？\x02",
        )
    )

    CloseMessageWindow()

    #C0252
    ChrTalk(
        0x101,
        (
            "#7P#0011F不不，没有……\x01",
            "只是稍微有点睡眠不足而已。\x02\x03",

            "#0006F好像是……\x01",
            "做了一个很奇怪的梦。\x02",
        )
    )

    CloseMessageWindow()

    #C0253
    ChrTalk(
        0x11,
        "呵呵，奇怪的梦啊。\x02",
    )

    CloseMessageWindow()

    #C0254
    ChrTalk(
        0x11,
        (
            "莫非是做了个被充满魅力的女孩子穷追猛打，\x01",
            "让你感到不知所措的梦～？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0255
    ChrTalk(
        0x101,
        (
            "#7P#0012F不、不是～……\x01",
            "应该不是那么好的美梦。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x12, 0x2)
    Sleep(300)

    #C0256
    ChrTalk(
        0x12,
        (
            "#5P你这老头子，可真是的。\x01",
            "不要对年轻人开这么没有分寸的玩笑啊。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x12, 0x0)
    Sleep(300)

    #C0257
    ChrTalk(
        0x12,
        (
            "#5P对了，要不要喝点冰镇柠檬汁\x01",
            "来提提神呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0258
    ChrTalk(
        0x12,
        (
            "#5P我把它冰镇之后装进水壶，\x01",
            "带来了不少呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0259
    ChrTalk(
        0x101,
        (
            "#7P#0000F啊……谢谢您，\x01",
            "那我就不客气了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(-2300, 900, 250, 0)
    MoveCamera(300, 18, 0, 0)
    OP_6E(420, 0)
    SetCameraDistance(21000, 0)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x21)
    SetChrSubChip(0x101, 0x3)
    OP_0D()
    Sleep(500)
    Fade(250)
    SetChrSubChip(0x101, 0x4)
    OP_0D()

    #C0260
    ChrTalk(
        0x101,
        "#11P（咕噜、咕噜……）\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    SetChrSubChip(0x101, 0x3)
    OP_0D()

    #C0261
    ChrTalk(
        0x101,
        (
            "#0014F#11P呼啊～～！\x02\x03",

            "#0002F承蒙款待！\x01",
            "真是冰凉又美味呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0262
    ChrTalk(
        0x12,
        "#1P呵呵，招待不周，请多包涵呢。\x02",
    )

    CloseMessageWindow()

    #C0263
    ChrTalk(
        0x11,
        (
            "#6P话说回来，看你的打扮……\x01",
            "好像不是帝国人啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0264
    ChrTalk(
        0x11,
        "#6P应该是出身于克洛斯贝尔的吧？\x02",
    )

    CloseMessageWindow()
    Fade(250)
    ClearChrFlags(0x101, 0x20)
    ClearChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x20)
    SetChrSubChip(0x101, 0x0)
    OP_0D()

    #C0265
    ChrTalk(
        0x101,
        (
            "#0005F#11P啊，是的。\x02\x03",

            "#0004F……虽然之前在国外\x01",
            "生活了一段时间，\x01",
            "但还是回到这里来了。\x02\x03",

            "#0000F话说回来，老爷爷，\x01",
            "您也是克洛斯贝尔人吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0266
    ChrTalk(
        0x11,
        (
            "#6P嗯，去共和国那边旅行了一趟，\x01",
            "正要回去呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0267
    ChrTalk(
        0x11,
        (
            "#6P……不过，如果你是刚从国外回来，\x01",
            "在看到克洛斯贝尔如今的样貌之后，\x01",
            "说不定会大吃一惊啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0268
    ChrTalk(
        0x12,
        "#1P也是呢。\x02",
    )

    CloseMessageWindow()

    #C0269
    ChrTalk(
        0x12,
        (
            "#1P在最近这两三年，\x01",
            "街道的格局可是发生了很大变化……\x02",
        )
    )

    CloseMessageWindow()

    #C0270
    ChrTalk(
        0x101,
        (
            "#0003F#11P果然如此吗……\x02\x03",

            "#0001F……其实，最近这段时间，\x01",
            "我曾经好几次乘坐列车\x01",
            "经过了克洛斯贝尔市……\x02\x03",

            "市内好像建起了不少\x01",
            "高楼大厦吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0271
    ChrTalk(
        0x11,
        (
            "#6P嗯，克洛斯贝尔原本就是\x01",
            "大陆中首屈一指的贸易都市。\x02",
        )
    )

    CloseMessageWindow()

    #C0272
    ChrTalk(
        0x11,
        (
            "#6P由于金融业也非常发达，\x01",
            "很容易吸引各国的投资者前来投资，\x01",
            "所以有相当多的资金流入克洛斯贝尔……\x02",
        )
    )

    CloseMessageWindow()

    #C0273
    ChrTalk(
        0x11,
        (
            "#6P而且自从前年签署了《互不侵犯条约》，\x01",
            "这种趋势似乎就更加明显了。\x02",
        )
    )

    CloseMessageWindow()

    #C0274
    ChrTalk(
        0x11,
        (
            "#6P在它成为巨额投资的对象后，\x01",
            "诸如百货商场、办公大楼等设施，\x01",
            "很快就拔地而起了。\x02",
        )
    )

    CloseMessageWindow()

    #C0275
    ChrTalk(
        0x12,
        (
            "#1P虽然庆幸市内增添了许多方便生活的设施，\x01",
            "但总体发展速度太快，倒也让人有些无所适从啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0276
    ChrTalk(
        0x12,
        (
            "#1P每个人都在莫名其妙地忙碌个不停，\x01",
            "简直就像是时间和金钱的奴隶一样……\x02",
        )
    )

    CloseMessageWindow()

    #C0277
    ChrTalk(
        0x101,
        "#0008F#11P……………………………………\x02",
    )

    CloseMessageWindow()

    #C0278
    ChrTalk(
        0x12,
        (
            "#1P啊，\x01",
            "真是抱歉。\x02",
        )
    )

    CloseMessageWindow()

    #C0279
    ChrTalk(
        0x12,
        "#1P你难得回到家乡，我却说了这种扫兴话。\x02",
    )

    CloseMessageWindow()

    #C0280
    ChrTalk(
        0x101,
        (
            "#0012F#11P哪里，请不必介意。\x02\x03",

            "#0002F之前在与朋友的书信中已经了解到不少情况了……\x01",
            "而且，无论如何变化，克洛斯贝尔也\x01",
            "永远都是我的故乡啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0281
    ChrTalk(
        0x12,
        "#1P说得对……\x02",
    )

    CloseMessageWindow()

    #C0282
    ChrTalk(
        0x11,
        "#6P嗯，虽然年纪轻轻，但真是很懂事啊。\x02",
    )

    CloseMessageWindow()

    #C0283
    ChrTalk(
        0x11,
        (
            "#6P跟你这种有为的年轻人相比，最近上任的\x01",
            "那群政治家真是……\x02",
        )
    )

    CloseMessageWindow()

    #C0284
    ChrTalk(
        0x11,
        (
            "#6P搞出什么帝国派，什么共和国派的，\x01",
            "全都是一个德性，只会争权夺利……\x02",
        )
    )

    CloseMessageWindow()

    #C0285
    ChrTalk(
        0x11,
        (
            "#6P值得信赖的人，恐怕\x01",
            "只剩下麦克道尔市长一个了。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x12, 0x2)
    Sleep(300)

    #C0286
    ChrTalk(
        0x12,
        "#1P老头子、老头子。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x12, 0x0)
    Sleep(300)

    #C0287
    ChrTalk(
        0x12,
        (
            "#1P……真是不好意思啊。\x01",
            "这个老家伙，只要一扯到政治，\x01",
            "就会忘乎所以地说个没完。\x02",
        )
    )

    CloseMessageWindow()

    #C0288
    ChrTalk(
        0x101,
        (
            "#0000F#11P哪里……其实这些话也使我受益匪浅呢。\x02\x03",

            "虽然在国外也能订阅到\x01",
            "《克洛斯贝尔时代周刊》……\x02\x03",

            "但有些事情，还是只有亲耳听到\x01",
            "才能真正把握住其本质呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0289
    ChrTalk(
        0x11,
        (
            "#6P哦，你也是《克洛斯贝尔时代周刊》\x01",
            "的忠实读者啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0290
    ChrTalk(
        0x11,
        (
            "#6P虽然多少有些庸俗的内容，但总体来说，\x01",
            "也还算是一本挺不错的新闻杂志，对吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0291
    ChrTalk(
        0x11,
        (
            "#6P但还是希望他们能对自治州行政\x01",
            "方面的问题多做一些报道……\x02",
        )
    )

    CloseMessageWindow()

    #C0292
    ChrTalk(
        0x101,
        (
            "#0012F#11P原来如此……看起来，目前\x01",
            "克洛斯贝尔果然存在着很多问题啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    SetChrSubChip(0x101, 0x2)
    Sleep(300)

    #C0293
    ChrTalk(
        0x101,
        "#0005F#2P啊……！\x02",
    )

    CloseMessageWindow()
    OP_68(-3300, 900, 250, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x1)
    OP_24(0x1C2)
    OP_C7(0x0, 0x10)
    FadeToBright(0, 0)
    OP_0D()
    PlayMovie(0x0, "ed7_ev01.pmf", 0xC8, 0x1)
    Sleep(1000)
    OP_57(0x2)
    PlayMovie(0x1, "", 0x0, 0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    OP_C7(0x1, 0x10)
    SoundLoad(450)
    OP_68(-2300, 900, 250, 0)
    MoveCamera(300, 18, 0, 0)
    OP_6E(420, 0)
    SetCameraDistance(21000, 0)
    EndChrThread(0x19, 0x1)
    Sound(450, 2, 100, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sound(801, 0, 100, 0)
    Sleep(1500)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("乘务员的声音")

    #A0294
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "──各位乘客请注意。\x02",
        )
    )

    CloseMessageWindow()

    #A0295
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "本列车即将到达克洛斯贝尔自治州\x01",
            "的克洛斯贝尔市。\x02",
        )
    )

    CloseMessageWindow()

    #A0296
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "需要乘坐定期飞行船前往利贝尔、\x01",
            "雷米菲利亚等地区的乘客，\x01",
            "请您做好换乘的准备。\x02",
        )
    )

    CloseMessageWindow()

    #A0297
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "另外，根据大陆铁道公司规章，\x01",
            "本列车在抵达克洛斯贝尔车站之后，\x01",
            "将会停留三十分钟。\x02",
        )
    )

    CloseMessageWindow()

    #A0298
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "准备前往埃雷波尼亚帝国的乘客，\x01",
            "请填写入境申请书，\x01",
            "并将其提交给安检官。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    #C0299
    ChrTalk(
        0x11,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#6P……嗯，好像要到站了。\x02",
        )
    )

    CloseMessageWindow()

    #C0300
    ChrTalk(
        0x11,
        (
            "#6P我可不想看到帝国军人的脸，\x01",
            "赶快收拾一下东西，准备下车吧。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)
    Sleep(300)

    #C0301
    ChrTalk(
        0x101,
        (
            "#0012F#11P哈哈，说得也是呢。\x02\x03",

            "#0008F…………………………………\x02\x03",

            "（自那之后，已经过去三年了吗……）\x02\x03",

            "（虽然曾和塞茜尔姐姐使用导力通讯\x01",
            "　进行过数次联络……）\x02\x03",

            "#0003F（…………………………………）\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x21)
    SetChrSubChip(0x101, 0x5)
    OP_68(-2300, 900, 750, 1500)
    OP_0D()
    OP_6F(0x1)
    Fade(250)
    Sound(804, 0, 100, 0)
    SetChrSubChip(0x101, 0x6)
    OP_0D()
    Sleep(500)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    Sleep(1000)
    SetMessageWindowPos(80, 200, -1, -1)
    SetChrName("罗伊德")

    #A0302
    AnonymousTalk(
        0xFF,
        (
            "#0004F（……大哥、塞茜尔姐姐………）\x02\x03",

            "（我……终于回来了。）\x02\x03",

            "#0002F（回到克洛斯贝尔……\x01",
            "　这座我们曾经一起生活过的城市。）\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C7(0x1, 0x800)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    SetCameraDistance(20500, 3000)
    FadeToDark(3000, 0, -1)
    OP_0D()
    BeginChrThread(0x19, 0, 0, 34)
    OP_6F(0x10)
    OP_CA(0x0, 0x0, 0x3)
    EndChrThread(0x101, 0x3)
    StopBGM(0xFA0)
    WaitBGM()
    Sleep(1000)
    EndChrThread(0x19, 0x0)
    OP_24(0x1C2)
    OP_C7(0x0, 0x10)
    FadeToBright(0, 0)
    OP_0D()
    OP_E3(0xA)
    PlayMovie(0x0, "ed7_op.pmf", 0x2, 0x0)
    Sleep(1000)
    OP_57(0x2)
    PlayMovie(0x1, "", 0x0, 0x0)
    StopBGM(0x1F4)
    WaitBGM()
    OP_C7(0x1, 0x10)
    Sleep(2500)
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x320, 0x0)
    OP_CA(0x0, 0x1, 0x3)
    OP_57(0x3)
    OP_C9(0x1, 0x3, 0xFFFFFF, 0x320, 0x0)
    OP_CA(0x0, 0x1, 0x3)
    OP_E3(0xB)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x101, 0x20)
    ClearChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    OP_24(0x1C2)
    SetScenarioFlags(0x5C, 0)
    NewScene("c0800", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_32_5FF7 end

    def Function_33_756B(): pass

    label("Function_33_756B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_75A3")
    OP_82(0xA, 0xA, 0x5DC, 0x2EE)
    Sleep(3500)
    OP_82(0xA, 0xA, 0x4B0, 0x1F4)
    Sleep(3500)
    Jump("Function_33_756B")

    label("loc_75A3")

    Return()

    # Function_33_756B end

    def Function_34_75A4(): pass

    label("Function_34_75A4")

    OP_25(0x1C2, 0x64)
    Sleep(200)
    OP_25(0x1C2, 0x5A)
    Sleep(200)
    OP_25(0x1C2, 0x50)
    Sleep(200)
    OP_25(0x1C2, 0x46)
    Sleep(200)
    OP_25(0x1C2, 0x3C)
    Sleep(200)
    OP_25(0x1C2, 0x32)
    Sleep(200)
    OP_25(0x1C2, 0x28)
    Sleep(200)
    OP_25(0x1C2, 0x1E)
    Sleep(200)
    OP_25(0x1C2, 0x14)
    Sleep(200)
    OP_25(0x1C2, 0xA)
    Sleep(200)
    OP_25(0x1C2, 0x0)
    Return()

    # Function_34_75A4 end

    def Function_35_75EF(): pass

    label("Function_35_75EF")

    OP_25(0x1C2, 0x0)
    Sleep(300)
    OP_25(0x1C2, 0xA)
    Sleep(300)
    OP_25(0x1C2, 0x14)
    Sleep(300)
    OP_25(0x1C2, 0x1E)
    Sleep(300)
    OP_25(0x1C2, 0x28)
    Sleep(300)
    OP_25(0x1C2, 0x32)
    Sleep(300)
    OP_25(0x1C2, 0x3C)
    Sleep(300)
    OP_25(0x1C2, 0x46)
    Sleep(300)
    OP_25(0x1C2, 0x50)
    Sleep(300)
    OP_25(0x1C2, 0x5A)
    Sleep(300)
    OP_25(0x1C2, 0x64)
    Return()

    # Function_35_75EF end

    SaveToFile()

Try(main)
