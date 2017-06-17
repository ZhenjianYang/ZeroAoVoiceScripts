from ZeroScenarioHelper import *

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
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 270, 1, 160, 0, 1, 0, 2],
    )

    BuildStringList((
        "e0410",                  # 0
        "青年",                   # 1
        "娘",                     # 2
        "男性",                   # 3
        "父親",                   # 4
        "母親",                   # 5
        "男の子",                 # 6
        "交易商",                 # 7
        "女性",                   # 8
        "カーラ",                 # 9
        "老人",                   # 10
        "老婦人",                 # 11
        "乗客",                   # 12
        "乗客",                   # 13
        "乗客",                   # 14
        "乗客",                   # 15
        "乗客",                   # 16
        "乗客",                   # 17
        "SE制御",                 # 18
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
        "Function_4_B3F",          # 04, 4
        "Function_5_D0B",          # 05, 5
        "Function_6_FD0",          # 06, 6
        "Function_7_11C2",         # 07, 7
        "Function_8_1386",         # 08, 8
        "Function_9_1485",         # 09, 9
        "Function_10_1667",        # 0A, 10
        "Function_11_1834",        # 0B, 11
        "Function_12_1B9C",        # 0C, 12
        "Function_13_1E8E",        # 0D, 13
        "Function_14_1F37",        # 0E, 14
        "Function_15_223F",        # 0F, 15
        "Function_16_23CE",        # 10, 16
        "Function_17_2550",        # 11, 17
        "Function_18_269F",        # 12, 18
        "Function_19_2A25",        # 13, 19
        "Function_20_2D78",        # 14, 20
        "Function_21_3346",        # 15, 21
        "Function_22_3687",        # 16, 22
        "Function_23_3B62",        # 17, 23
        "Function_24_3CFF",        # 18, 24
        "Function_25_3E09",        # 19, 25
        "Function_26_477F",        # 1A, 26
        "Function_27_47EE",        # 1B, 27
        "Function_28_483E",        # 1C, 28
        "Function_29_48B8",        # 1D, 29
        "Function_30_4D29",        # 1E, 30
        "Function_31_4EA7",        # 1F, 31
        "Function_32_6433",        # 20, 32
        "Function_33_7A35",        # 21, 33
        "Function_34_7A6E",        # 22, 34
        "Function_35_7AB9",        # 23, 35
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
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0x9)"), scpexpr(EXPR_END)), "loc_AA7")

    #C0001
    ChrTalk(
        0xFE,
        "彼女はせっかちだなぁ、ほんと。\x02",
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0xFE,
        "旅はゆるりと楽しまなきゃな。\x02",
    )

    CloseMessageWindow()
    Jump("loc_B37")

    label("loc_AA7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0x4)"), scpexpr(EXPR_END)), "loc_B04")

    #C0003
    ChrTalk(
        0x8,
        (
            "僕らはクロスベルから\x01",
            "帝国に旅行に行くんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x8,
        "楽しみだよ、ハハハ。\x02",
    )

    CloseMessageWindow()
    Jump("loc_B37")

    label("loc_B04")

    Call(0, 18)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0x4)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0x5)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0x6)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0x7)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0x8)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B37")
    Call(0, 23)

    label("loc_B37")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_3_94C end

    def Function_4_B3F(): pass

    label("Function_4_B3F")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_BD3")
    Jump("loc_C1D")

    label("loc_BD3")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_BF3")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_C1D")

    label("loc_BF3")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C13")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_C1D")

    label("loc_C13")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_C1D")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0x9)"), scpexpr(EXPR_END)), "loc_C85")

    #C0005
    ChrTalk(
        0xFE,
        (
            "ねー、まだ発車しないの？\x01",
            "さっさとしてよね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D03")

    label("loc_C85")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0x4)"), scpexpr(EXPR_END)), "loc_CD0")

    #C0006
    ChrTalk(
        0x9,
        (
            "もー臨検は終わったんでしょぉ？\x01",
            "早くあっち行ってよ！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D03")

    label("loc_CD0")

    Call(0, 18)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0x4)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0x5)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0x6)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0x7)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0x8)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D03")
    Call(0, 23)

    label("loc_D03")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_4_B3F end

    def Function_5_D0B(): pass

    label("Function_5_D0B")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_D9F")
    Jump("loc_DE9")

    label("loc_D9F")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_DBF")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_DE9")

    label("loc_DBF")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_DDF")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_DE9")

    label("loc_DDF")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_DE9")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0x9)"), scpexpr(EXPR_END)), "loc_F29")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x70, 0)), scpexpr(EXPR_END)), "loc_E2C")
    Call(0, 25)
    Jump("loc_F24")

    label("loc_E2C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_E91")

    #C0007
    ChrTalk(
        0xFE,
        (
            "あぁ、楽しみだなぁ。\x01",
            "この車窓からみる景色。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0xFE,
        "……早く発車してくれないかなぁ。\x02",
    )

    CloseMessageWindow()
    Jump("loc_F24")

    label("loc_E91")


    #C0009
    ChrTalk(
        0xFE,
        (
            "あぁ、楽しみだなぁ。\x01",
            "この車窓からみる景色。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0xFE,
        (
            "ノックス森林地帯の深緑は、\x01",
            "さぞ美しいに違いないね。\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0xFE,
        "……早く発車してくれないかなぁ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_F24")

    Jump("loc_FC8")

    label("loc_F29")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0x5)"), scpexpr(EXPR_END)), "loc_F95")

    #C0012
    ChrTalk(
        0xA,
        (
            "ふふ、それにしても\x01",
            "発車が楽しみだなぁ……\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0xA,
        (
            "列車から見る景色は\x01",
            "格別なんだよねぇ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FC8")

    label("loc_F95")

    Call(0, 19)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0x4)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0x5)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0x6)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0x7)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0x8)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_FC8")
    Call(0, 23)

    label("loc_FC8")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_5_D0B end

    def Function_6_FD0(): pass

    label("Function_6_FD0")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1064")
    Jump("loc_10AE")

    label("loc_1064")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1084")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_10AE")

    label("loc_1084")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_10A4")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_10AE")

    label("loc_10A4")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_10AE")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x70, 0)), scpexpr(EXPR_END)), "loc_1110")

    #C0014
    ChrTalk(
        0xFE,
        (
            "はは、落ち着きがないのは\x01",
            "誰に似たんだか。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11BA")

    label("loc_1110")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0x9)"), scpexpr(EXPR_END)), "loc_1125")
    Call(0, 20)
    Jump("loc_11BA")

    label("loc_1125")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0x6)"), scpexpr(EXPR_END)), "loc_1187")

    #C0015
    ChrTalk(
        0xB,
        (
            "共和国からは\x01",
            "そこそこ長旅なんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0xB,
        (
            "ふああ……\x01",
            "発車まで一眠りしようか。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11BA")

    label("loc_1187")

    Call(0, 20)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0x4)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0x5)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0x6)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0x7)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0x8)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_11BA")
    Call(0, 23)

    label("loc_11BA")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_6_FD0 end

    def Function_7_11C2(): pass

    label("Function_7_11C2")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1256")
    Jump("loc_12A0")

    label("loc_1256")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1276")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_12A0")

    label("loc_1276")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1296")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_12A0")

    label("loc_1296")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_12A0")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x70, 0)), scpexpr(EXPR_END)), "loc_12F3")

    #C0017
    ChrTalk(
        0xFE,
        "まったく、この子ったら……\x02",
    )

    CloseMessageWindow()
    Jump("loc_137E")

    label("loc_12F3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0x9)"), scpexpr(EXPR_END)), "loc_1308")
    Call(0, 20)
    Jump("loc_137E")

    label("loc_1308")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0x6)"), scpexpr(EXPR_END)), "loc_134B")

    #C0018
    ChrTalk(
        0xC,
        (
            "この子ったらもう、\x01",
            "落ち着きが無いんだから。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_137E")

    label("loc_134B")

    Call(0, 20)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0x4)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0x5)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0x6)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0x7)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0x8)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_137E")
    Call(0, 23)

    label("loc_137E")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_7_11C2 end

    def Function_8_1386(): pass

    label("Function_8_1386")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x70, 0)), scpexpr(EXPR_END)), "loc_140B")

    #C0019
    ChrTalk(
        0xFE,
        (
            "ぶ～……\x01",
            "向こうの席のお兄ちゃんは\x01",
            "前の車両から来てたのにぃ～。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0xFE,
        "ズルいや。\x02",
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x101,
        "#0001F…………………………\x02",
    )

    CloseMessageWindow()
    Jump("loc_1481")

    label("loc_140B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0x9)"), scpexpr(EXPR_END)), "loc_1420")
    Call(0, 20)
    Jump("loc_1481")

    label("loc_1420")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0x6)"), scpexpr(EXPR_END)), "loc_144E")

    #C0022
    ChrTalk(
        0xD,
        "早く発車しないかなー。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1481")

    label("loc_144E")

    Call(0, 20)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0x4)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0x5)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0x6)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0x7)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0x8)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1481")
    Call(0, 23)

    label("loc_1481")

    TalkEnd(0xFE)
    Return()

    # Function_8_1386 end

    def Function_9_1485(): pass

    label("Function_9_1485")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1519")
    Jump("loc_1563")

    label("loc_1519")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1539")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1563")

    label("loc_1539")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1559")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1563")

    label("loc_1559")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1563")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0x9)"), scpexpr(EXPR_END)), "loc_15F6")

    #C0023
    ChrTalk(
        0xFE,
        (
            "……ふぅ、ちっとは\x01",
            "頭を冷やさんとな。\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0xFE,
        (
            "心に余裕を持たんと\x01",
            "商売に成功はないからな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_165F")

    label("loc_15F6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0x7)"), scpexpr(EXPR_END)), "loc_162C")

    #C0025
    ChrTalk(
        0xE,
        "なんじゃい、まだ用があるのか？\x02",
    )

    CloseMessageWindow()
    Jump("loc_165F")

    label("loc_162C")

    Call(0, 21)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0x4)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0x5)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0x6)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0x7)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0x8)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_165F")
    Call(0, 23)

    label("loc_165F")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_9_1485 end

    def Function_10_1667(): pass

    label("Function_10_1667")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_16FB")
    Jump("loc_1745")

    label("loc_16FB")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_171B")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1745")

    label("loc_171B")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_173B")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1745")

    label("loc_173B")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1745")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0x9)"), scpexpr(EXPR_END)), "loc_17A8")

    #C0026
    ChrTalk(
        0xFE,
        "はぁ……\x02",
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0xFE,
        "……玉の輿にのりたい……\x02",
    )

    CloseMessageWindow()
    Jump("loc_182C")

    label("loc_17A8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0x8)"), scpexpr(EXPR_END)), "loc_17F9")
    SetChrSubChip(0xF, 0x0)

    #C0028
    ChrTalk(
        0xF,
        (
            "はぁ……\x01",
            "男ってみんなそう。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0xF,
        "ぶつぶつぶつぶつ……\x02",
    )

    CloseMessageWindow()
    Jump("loc_182C")

    label("loc_17F9")

    Call(0, 22)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0x4)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0x5)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0x6)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0x7)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0x8)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_182C")
    Call(0, 23)

    label("loc_182C")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_10_1667 end

    def Function_11_1834(): pass

    label("Function_11_1834")

    Switch(
        (scpexpr(EXPR_23, 0x5), scpexpr(EXPR_END)),
        (0, "loc_184F"),
        (1, "loc_19C8"),
        (2, "loc_1A35"),
        (SWITCH_DEFAULT, "loc_1B9B"),
    )


    label("loc_184F")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_18E3")
    Jump("loc_192D")

    label("loc_18E3")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1903")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_192D")

    label("loc_1903")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1923")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_192D")

    label("loc_1923")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_192D")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0030
    ChrTalk(
        0xFE,
        (
            "休みが取れたので\x01",
            "アルタイル市の実家に帰るんですよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0xFE,
        (
            "妻と子供が待っているんです。\x01",
            "楽しみだなぁ♪\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Jump("loc_1B9B")

    label("loc_19C8")

    TalkBegin(0xFE)

    #C0032
    ChrTalk(
        0xFE,
        "あんた、せっかちよねぇ。\x02",
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0xFE,
        (
            "共和国の首都まで\x01",
            "まだまだあるんだから。\x01",
            "焦らなくてもいいわよ。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Jump("loc_1B9B")

    label("loc_1A35")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1AC9")
    Jump("loc_1B13")

    label("loc_1AC9")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1AE9")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1B13")

    label("loc_1AE9")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1B09")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1B13")

    label("loc_1B09")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1B13")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0034
    ChrTalk(
        0xFE,
        "ワシの祖国はオレド自治州なのだ。\x02",
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0xFE,
        (
            "おっほん、孫を連れてってやる\x01",
            "所なんじゃよ。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Jump("loc_1B9B")

    label("loc_1B9B")

    Return()

    # Function_11_1834 end

    def Function_12_1B9C(): pass

    label("Function_12_1B9C")

    Switch(
        (scpexpr(EXPR_23, 0x5), scpexpr(EXPR_END)),
        (0, "loc_1BB7"),
        (1, "loc_1CE1"),
        (2, "loc_1D35"),
        (SWITCH_DEFAULT, "loc_1E8D"),
    )


    label("loc_1BB7")

    TalkBegin(0xFE)
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1C4E")
    Jump("loc_1C98")

    label("loc_1C4E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1C6E")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1C98")

    label("loc_1C6E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1C8E")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1C98")

    label("loc_1C8E")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1C98")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0036
    ChrTalk(
        0xFE,
        "わー、すっごーい！\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x1)
    TalkEnd(0xFE)
    Jump("loc_1E8D")

    label("loc_1CE1")

    TalkBegin(0xFE)

    #C0037
    ChrTalk(
        0xFE,
        "パシャ、パシャ！\x02",
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0xFE,
        (
            "念願の鉄道の旅！\x01",
            "写真を撮りまくらなくっちゃ！\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Jump("loc_1E8D")

    label("loc_1D35")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1DC9")
    Jump("loc_1E13")

    label("loc_1DC9")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1DE9")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1E13")

    label("loc_1DE9")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1E09")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1E13")

    label("loc_1E09")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1E13")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0039
    ChrTalk(
        0xFE,
        "おじいちゃんの故郷、楽しみ！\x02",
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0xFE,
        (
            "すっごい広い\x01",
            "農場があるんだって！\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Jump("loc_1E8D")

    label("loc_1E8D")

    Return()

    # Function_12_1B9C end

    def Function_13_1E8E(): pass

    label("Function_13_1E8E")

    TalkBegin(0xFE)
    Switch(
        (scpexpr(EXPR_23, 0x5), scpexpr(EXPR_END)),
        (0, "loc_1EAC"),
        (1, "loc_1EE6"),
        (2, "loc_1F09"),
        (SWITCH_DEFAULT, "loc_1F33"),
    )


    label("loc_1EAC")


    #C0041
    ChrTalk(
        0xFE,
        (
            "あまりはしゃいじゃダメよ。\x01",
            "大人しくしてなさい！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F33")

    label("loc_1EE6")


    #C0042
    ChrTalk(
        0xFE,
        "スカー………スカー………\x02",
    )

    CloseMessageWindow()
    Jump("loc_1F33")

    label("loc_1F09")


    #C0043
    ChrTalk(
        0xFE,
        (
            "わはははは！\x01",
            "ありえねーっすよ！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F33")

    label("loc_1F33")

    TalkEnd(0xFE)
    Return()

    # Function_13_1E8E end

    def Function_14_1F37(): pass

    label("Function_14_1F37")

    Switch(
        (scpexpr(EXPR_23, 0x5), scpexpr(EXPR_END)),
        (0, "loc_1F52"),
        (1, "loc_20B2"),
        (2, "loc_220C"),
        (SWITCH_DEFAULT, "loc_223E"),
    )


    label("loc_1F52")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1FE6")
    Jump("loc_2030")

    label("loc_1FE6")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2006")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2030")

    label("loc_2006")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2026")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2030")

    label("loc_2026")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2030")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0044
    ChrTalk(
        0xFE,
        (
            "あの臨検官め、\x01",
            "人をジロジロと見やがって……\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0xFE,
        "いつもの事だが腹が立つぞ！\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Jump("loc_223E")

    label("loc_20B2")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2146")
    Jump("loc_2190")

    label("loc_2146")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2166")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2190")

    label("loc_2166")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2186")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2190")

    label("loc_2186")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2190")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0046
    ChrTalk(
        0xFE,
        (
            "共和国観光といえば\x01",
            "やはりグルメですわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0xFE,
        "それから温泉でしょうね！\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Jump("loc_223E")

    label("loc_220C")

    TalkBegin(0xFE)

    #C0048
    ChrTalk(
        0xFE,
        (
            "わはははは！\x01",
            "ウケルのう、その話！\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Jump("loc_223E")

    label("loc_223E")

    Return()

    # Function_14_1F37 end

    def Function_15_223F(): pass

    label("Function_15_223F")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_22D3")
    Jump("loc_231D")

    label("loc_22D3")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_22F3")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_231D")

    label("loc_22F3")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2313")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_231D")

    label("loc_2313")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_231D")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Switch(
        (scpexpr(EXPR_23, 0x5), scpexpr(EXPR_END)),
        (0, "loc_235D"),
        (1, "loc_2362"),
        (2, "loc_23C1"),
        (SWITCH_DEFAULT, "loc_23C6"),
    )


    label("loc_235D")

    Jump("loc_23C6")

    label("loc_2362")


    #C0049
    ChrTalk(
        0xFE,
        (
            "やはり女同士の旅が\x01",
            "気楽よね～。\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0xFE,
        (
            "旦那なんかと来ても\x01",
            "ちっとも楽しくないんだもの。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_23C6")

    label("loc_23C1")

    Jump("loc_23C6")

    label("loc_23C6")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_15_223F end

    def Function_16_23CE(): pass

    label("Function_16_23CE")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2462")
    Jump("loc_24AC")

    label("loc_2462")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2482")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_24AC")

    label("loc_2482")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_24A2")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_24AC")

    label("loc_24A2")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_24AC")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Switch(
        (scpexpr(EXPR_23, 0x5), scpexpr(EXPR_END)),
        (0, "loc_24EC"),
        (1, "loc_24F1"),
        (2, "loc_2543"),
        (SWITCH_DEFAULT, "loc_2548"),
    )


    label("loc_24EC")

    Jump("loc_2548")

    label("loc_24F1")


    #C0051
    ChrTalk(
        0xFE,
        (
            "この席、ちょっと暗いな……\x01",
            "読書しにくいよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0xFE,
        "窓際の席に移ろうかな。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2548")

    label("loc_2543")

    Jump("loc_2548")

    label("loc_2548")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_16_23CE end

    def Function_17_2550(): pass

    label("Function_17_2550")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(3750, 1000, -7850, 0)
    MoveCamera(315, 30, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(16000, 0)
    SetChrPos(0x101, 3750, 0, -7850, 270)
    OP_68(0, 1000, -7850, 3000)

    def lambda_25B1():
        OP_97(0x101, 0xFFFFF15A, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_25B1)
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
            "#0001F……やっぱり、\x01",
            "結構な数の乗客がいるみたいだ。\x02\x03",

            "#0003F一人一人、丁寧に臨検していかないとな。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_29(0x9, 0x1, 0x3)
    EventEnd(0x5)
    Return()

    # Function_17_2550 end

    def Function_18_269F(): pass

    label("Function_18_269F")

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
            "#12P#0000Fすみません、私は臨検官の補佐を\x01",
            "勤めている者なのですが……\x02\x03",

            "お手数ですが、\x01",
            "手荷物と入国申請書を\x01",
            "確認させていただけますか？\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x8,
        (
            "#5P……あー、はいはい、臨検ね。\x01",
            "めんどいけど、まぁいっか。\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x9,
        "#11Pえぇ～、やだーぁ。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x9, 0x0)

    #C0057
    ChrTalk(
        0x9,
        (
            "#11Pカバンには私の下着とかも\x01",
            "入ってるのよぉ？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 0x0)

    #C0058
    ChrTalk(
        0x8,
        "#5P……んー、そうか。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 0x2)

    #C0059
    ChrTalk(
        0x8,
        (
            "#5Pキミ、悪いけど……\x01",
            "そういう事だから。\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x101,
        (
            "#12P#0005F……いやいやいや！\x01",
            "そういうわけにはいきません。\x02\x03",

            "#0003F規則ですのでご協力ください。\x01",
            "下着とかにはその……\x01",
            "極力配慮しますので。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 0x0)

    #C0061
    ChrTalk(
        0x8,
        "#5Pだってさ。\x02",
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x9,
        "#11Pんもぉ、わかったぁ～……\x02",
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x101,
        "#12P#0006F（つ、疲れるなこれは……）\x02",
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
            "#12P#0000F……結構です。\x01",
            "手荷物、入国申請書ともに\x01",
            "確認できました。\x02\x03",

            "ご協力ありがとうございます。\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x8,
        "#5Pどういたしまして。\x02",
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x9,
        "#5Pふーんだ、早くあっち行ってよ！\x02",
    )

    CloseMessageWindow()
    OP_5A()
    SetChrSubChip(0x8, 0x0)
    SetChrSubChip(0x9, 0x0)
    OP_29(0x9, 0x1, 0x4)
    EventEnd(0x5)
    Return()

    # Function_18_269F end

    def Function_19_2A25(): pass

    label("Function_19_2A25")

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
            "#5P#0000Fすみません、臨検官補佐の者です。\x02\x03",

            "お手数ですが、\x01",
            "手荷物と入国申請書を\x01",
            "確認させていただけますか？\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0xA,
        (
            "#12Pああ、はいはい。\x01",
            "ちょっと待ってくれよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0xA,
        "#12P……ふふふ。\x02",
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x101,
        "#5P#0005F……えっと……何か？\x02",
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0xA,
        "#12Pいや、失礼。\x02",
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0xA,
        (
            "#12P列車の車窓からの風景……\x01",
            "特にノックス大森林の新緑は\x01",
            "なかなか格別なんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0xA,
        (
            "#12P発車したらあの風景を\x01",
            "見られると思うと、つい笑みがね……\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x101,
        (
            "#5P#0000Fへぇ……\x01",
            "いい趣味をお持ちですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0xA,
        (
            "#12P……おっと、\x01",
            "つい足止めしてしまったね。\x01",
            "臨検に来たんだろう？\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x101,
        (
            "#5P#0005Fあ……そうでした。\x02\x03",

            "#0000Fでは、失礼して……\x02",
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
            "#5P#0000F……手荷物、入国申請書ともに\x01",
            "確認できました。\x02\x03",

            "ご協力ありがとうございます。\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0xA,
        "#12Pいえいえ、ご苦労さま。\x02",
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0xA,
        (
            "#12Pふふ、それにしても\x01",
            "発車が楽しみだなぁ……\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrSubChip(0xA, 0x0)
    OP_29(0x9, 0x1, 0x5)
    EventEnd(0x5)
    Return()

    # Function_19_2A25 end

    def Function_20_2D78(): pass

    label("Function_20_2D78")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0x9)"), scpexpr(EXPR_END)), "loc_2FC2")
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
            "#5Pねーお母さん、隣の車両まで\x01",
            "探検してきていい？\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0xC,
        (
            "#12Pだ～め！　臨検が終わるまで\x01",
            "ちゃんと座っておきなさい！\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0xB,
        (
            "#11Pそうだぞ。\x01",
            "臨検官さんに怒られちゃうぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0xD,
        (
            "#5Pえぇ～……でも、\x01",
            "あっちに座ってるお兄ちゃんは\x01",
            "前の車両から来てたよ～！？\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x101,
        (
            "#12P#0000F（前の車両って……クワトロさんが\x01",
            "  臨検している機関車のことか。）\x02\x03",

            "（車掌さんに何か\x01",
            "  用事がある人でもいたのかな。）\x02\x03",

            "#0005F（あれ、だけど………\x01",
            "  ……臨検が始まってから……\x01",
            "  車両を移動したってことか……？）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x70, 0)
    Jump("loc_332F")

    label("loc_2FC2")

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
            "#12P#0000F失礼します、臨検官補佐の者です。\x02\x03",

            "お手数ですが、\x01",
            "手荷物と入国申請書を\x01",
            "確認させていただけますか？\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0xB,
        (
            "#5Pああ臨検の人だったのか。\x01",
            "ふむ、お安いご用だよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0xD,
        (
            "#5Pねぇねぇ、まだ列車は\x01",
            "発車しないの？\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0xD,
        "#5P僕もう待ちくたびれちゃった。\x02",
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0xC,
        (
            "#6Pこの子ったら\x01",
            "堪え性がないんだから……\x01",
            "ふふ、ごめんなさいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x101,
        "#12P#0005Fあ、いえいえ。\x02",
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x101,
        (
            "#12P#0000Fごめんな、悪いけど\x01",
            "もう少しかかっちゃうんだ。\x02\x03",

            "お兄ちゃんたちのお仕事が済むまで、\x01",
            "大人しく待ってくれるかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0xD,
        "#5Pわかった～。\x02",
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x101,
        (
            "#12P#0003F（……手際よく\x01",
            "  やっていくとするか。）\x02",
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
            "#12P#0000F……手荷物、入国申請書ともに\x01",
            "確認できました。\x02\x03",

            "ご協力ありがとうございます。\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0xB,
        "#5Pはいよ。\x02",
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0xD,
        (
            "#5Pお兄ちゃん、お仕事は\x01",
            "できるだけ早くお願いね～。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xC, 0x1)

    #C0097
    ChrTalk(
        0xC,
        "#6Pこれ！　この子ったらもう……\x02",
    )

    CloseMessageWindow()
    OP_29(0x9, 0x1, 0x6)

    label("loc_332F")

    OP_5A()
    SetChrSubChip(0xB, 0x0)
    SetChrSubChip(0xC, 0x0)
    OP_93(0xD, 0xE1, 0x0)
    OP_4C(0xD, 0xFF)
    EventEnd(0x5)
    Return()

    # Function_20_2D78 end

    def Function_21_3346(): pass

    label("Function_21_3346")

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
        "#5Pあ～ん？　臨検官だと……？\x02",
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0xE,
        (
            "#5Pお前のどこが臨検官だというんだ。\x01",
            "証拠をみせろ、証拠を！\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0x101,
        (
            "#12P#0006Fえ、えっと……\x01",
            "（まいったな……）\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0101
    ChrTalk(
        0x101,
        (
            "#12P#0005Fそ、そうだ。\x01",
            "……これ、見てください。\x02",
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
            "ロイドは乗客に捜査手帳を見せた。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0103
    ChrTalk(
        0x101,
        (
            "#12P#0000F自分は警察の特務支援課から\x01",
            "臨検の手伝いに来ていまして……\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0xE,
        "#5P警察……フン、確かなようだな。\x02",
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0xE,
        (
            "#5Pまぎらわしいことを……\x01",
            "まぁいい、勝手にしたまえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0x101,
        "#12P#0005F……あ、ありがとうございます。\x02",
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
            "#12P#0000F……結構です。\x01",
            "手荷物、入国申請書ともに\x01",
            "確認できました。\x02\x03",

            "ご協力ありがとうございます。\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0xE,
        (
            "#5Pフン、礼などいらんから\x01",
            "さっさと仕事を済ませてくれ。\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0xE,
        "#5Pこっちは急いでるんでな。\x02",
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0x101,
        "#12P#0006Fし、失礼しました。\x02",
    )

    CloseMessageWindow()
    OP_5A()
    SetChrSubChip(0xE, 0x0)
    OP_29(0x9, 0x1, 0x7)
    EventEnd(0x5)
    Return()

    # Function_21_3346 end

    def Function_22_3687(): pass

    label("Function_22_3687")

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
            "#5P#0000Fすみません、臨検官補佐の者です。\x02\x03",

            "お手数ですが、\x01",
            "手荷物と入国申請書を\x01",
            "確認させていただけますか？\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0xF,
        (
            "#12P……臨検官？\x01",
            "私服なんて珍しいわね……\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0xF,
        (
            "#12P……ていうか、何？\x01",
            "女の一人旅だからって\x01",
            "なんか変だとか思ってるわけ？\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0x101,
        "#5P#0005Fえ？　い、いえ、別にそんな事は……\x02",
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0xF,
        (
            "#12P私だってねぇ、本当は\x01",
            "彼氏と遊びに行きたかったわよ！\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0xF,
        (
            "#12Pだけど昨日いきなりフラれたの、\x01",
            "一人旅でも仕方ないでしょ！？\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0xF,
        (
            "#12Pでもあたしは負けないわ！\x01",
            "帝国で絶対素敵で金持ちな\x01",
            "彼氏を見つけて……！！\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0x101,
        (
            "#5P#0011F（う……なんだか\x01",
            "  ラチがあかなそうだ。）\x02\x03",

            "#0006F（仕方ない、\x01",
            "  話を聞き流しながら\x01",
            "  臨検を進めるとするか……）\x02",
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
            "#12P……分かる？　臨検官さぁん。\x01",
            "アイツったらひどいでしょぉ……？\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0x101,
        (
            "#5P#0012Fそ、そうですね……\x02\x03",

            "#0000Fあ、えっと……\x01",
            "手荷物、入国申請書ともに\x01",
            "確認できました。\x02\x03",

            "ご協力ありがとうございます。\x02",
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
        "#5P#0005F……あ、あの？\x02",
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0xF,
        "#12P……ううん、なんでもないの。\x02",
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0xF,
        (
            "#12Pなんだかあなたに話してたら\x01",
            "すっきりしちゃった。\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0xF,
        (
            "#12Pこんなに話を聞いてもらったのは\x01",
            "随分ひさしぶり……\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0xF,
        "#12Pねぇ、よかったらこのまま２人で……\x02",
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0x101,
        (
            "#5P#0011Fし、仕事があるので……\x01",
            "失礼しますっ！\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrSubChip(0xF, 0x0)
    OP_29(0x9, 0x1, 0x8)
    EventEnd(0x5)
    Return()

    # Function_22_3687 end

    def Function_23_3B62(): pass

    label("Function_23_3B62")

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
            "#11P#0006Fふう……とりあえずこれで\x01",
            "全員の臨検が終わったはずだ。\x02\x03",

            "#0000F不審な人物もいなかったし、\x01",
            "あとは皆と合流して\x01",
            "クワトロさんに報告すれば完了だな。\x02\x03",

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
            "#5P#0003Fこういう仕事は初めてだったから\x01",
            "緊張したけど……\x02\x03",

            "#0001Fミスとか見落としは\x01",
            "無かったよな……？\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    ModifyEventFlags(1, 0, 0x80)
    OP_29(0x9, 0x1, 0x9)
    EventEnd(0x5)
    Return()

    # Function_23_3B62 end

    def Function_24_3CFF(): pass

    label("Function_24_3CFF")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x9, 0x1, 0x9)"), scpexpr(EXPR_END)), "loc_3DA9")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【臨検を終えて外に出る】\x01",      # 0
            "【やめる】\x01",                    # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3D8E")
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0x7D0)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x5C, 2)
    NewScene("c0800", 0, 0, 0)
    IdleLoop()
    Jump("loc_3DA4")

    label("loc_3D8E")

    Sleep(50)
    SetChrPos(0x0, 2000, 0, -7850, 270)
    EventEnd(0x4)

    label("loc_3DA4")

    Jump("loc_3E08")

    label("loc_3DA9")


    #C0130
    ChrTalk(
        0x101,
        (
            "#0001F……まだ臨検は終わってない。\x01",
            "列車から出るわけにはいかないな。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, 2000, 0, -7850, 270)
    EventEnd(0x4)

    label("loc_3E08")

    Return()

    # Function_24_3CFF end

    def Function_25_3E09(): pass

    label("Function_25_3E09")

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
            "#12Pあぁ、楽しみだなぁ。\x01",
            "この車窓からみる景色。\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0xA,
        "#12P……早く発車してくれないかなぁ。\x02",
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0x101,
        (
            "#5P#0001F……すみません。\x01",
            "少し、いいでしょうか。\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0xA,
        "#12Pおや、どうしたんだい？\x02",
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0xA,
        (
            "#12P臨検は終わったんじゃあ\x01",
            "なかったのかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0x101,
        (
            "#5P#0003Fいえ、少し気になる事がありまして。\x02\x03",

            "#0001Fもしよろしければ、\x01",
            "もう一度臨検をさせて頂けないかと。\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0xA,
        (
            "#12P……ああ、構わないとも。\x01",
            "何かチェックし忘れでもあったかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0xA,
        (
            "#12Pほら、荷物も入国申請書も\x01",
            "ここにあるけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0x101,
        (
            "#5P#0003Fいえ、臨検するのは\x01",
            "自分ではありません。\x02\x03",

            "#0001F本職の臨検官である……\x01",
            "クワトロさんに\x01",
            "お願いしようと思ってます。\x02",
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
            "#12Pな、何でクワトロさんに……？\x01",
            "君で十分じゃないのかい？\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0x101,
        "#5P#0003F……やはり、彼をご存知でしたか。\x02",
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0142
    ChrTalk(
        0xA,
        "#12Pあっ……い、いやその……\x02",
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0x101,
        (
            "#5P#0003F……この臨検を始める前に\x01",
            "クワトロさんからいくつか、\x01",
            "臨検のルールを聞いていました。\x02\x03",

            "#0001Fその一つに……\x01",
            "『臨検中は車両を移動できない』\x01",
            "というものがあります。\x02",
        )
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0xA,
        "#12Pあ、ああ……もちろん知ってるよ。\x02",
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0xA,
        "#12P僕がそれを破ったとでもいうのかい？\x02",
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0x101,
        (
            "#5P#0001F残念な事ですが……\x01",
            "それを目撃した人物がいます。\x02\x03",

            "向こうの席に座っている男の子が、\x01",
            "あなたが前の車両から移動してくるのを\x01",
            "見ていたそうなんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0xA,
        "#12P……う、うそ……！？\x02",
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0xA,
        (
            "#12Pそ、そんなの、ただの見間違いって\x01",
            "ことだってあるんじゃあ……\x02",
        )
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0x101,
        (
            "#5P#0003Fそれは、機関車にいる車掌に聞けば\x01",
            "おそらく裏がとれるでしょう。\x02\x03",

            "#0001Fそれより問題は……\x01",
            "あなたがなぜそんな事をしたか、です。\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0xA,
        "#12Pうっ……\x02",
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0x101,
        (
            "#5P#0003F規則である以上、あなたは\x01",
            "機関車でクワトロさんの臨検を\x01",
            "受けるべきだったはずです。\x02\x03",

            "にも関わらず、\x01",
            "こちらの車両に移ってから\x01",
            "何食わぬ顔で応対していた理由……\x02\x03",

            "#0001Fそれはおそらく、\x01",
            "クワトロさんから逃れるためだ。\x02\x03",

            "……違いますか？\x02",
        )
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0xA,
        "#12P……あ……あああ……\x02",
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)

    #C0153
    ChrTalk(
        0xA,
        (
            "#12P──た……頼む！\x01",
            "どうか見逃してくれないか！？\x02",
        )
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0xA,
        (
            "#12Pぼ……僕は楽しく旅行がしたい、\x01",
            "ただそれだけなんだ！\x02",
        )
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0xA,
        (
            "#12Pほ、ほら……入国申請書には\x01",
            "怪しいところなんてなかったろう？\x01",
            "だったら……\x02",
        )
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0x101,
        (
            "#5P#0003F──だったら……\x01",
            "クワトロさんに見せていたとしても\x01",
            "大丈夫だったはず、ですよね？\x02",
        )
    )

    CloseMessageWindow()
    OP_64(0xFFFF)

    #C0157
    ChrTalk(
        0xA,
        "#12P……！　そ、それは……\x02",
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0x101,
        (
            "#0008F自分には詳しい事情はわかりませんが……\x02\x03",

            "#0001F臨検官補佐として来ている以上、\x01",
            "不審な行動をとっていたあなたを\x01",
            "このまま見逃すわけにはいきません。\x02\x03",

            "#0003F……ご同行をお願いします。\x02",
        )
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0xA,
        "#12P……あ………ああ………………\x02",
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

    # Function_25_3E09 end

    def Function_26_477F(): pass

    label("Function_26_477F")

    EventBegin(0x1)
    OP_D0(0x5, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Call(0, 2)
    SetChrPos(0x0, 100, 0, -8640, 0)
    OP_68(100, 1000, -8640, 0)
    MoveCamera(315, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(20000, 0)
    Jc((scpexpr(EXPR_23, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x1, 0xD)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_47EB")
    Call(0, 30)
    Jump("loc_47ED")

    label("loc_47EB")

    EventEnd(0x4)

    label("loc_47ED")

    Return()

    # Function_26_477F end

    def Function_27_47EE(): pass

    label("Function_27_47EE")

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

    # Function_27_47EE end

    def Function_28_483E(): pass

    label("Function_28_483E")

    EventBegin(0x1)

    #C0160
    ChrTalk(
        0x101,
        (
            "#0001F……カーラさんを説得してみよう。\x02\x03",

            "もたもたしていると\x01",
            "アルタイル市に着いてしまうしな。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, 10, 0, 7210, 180)
    EventEnd(0x4)
    Return()

    # Function_28_483E end

    def Function_29_48B8(): pass

    label("Function_29_48B8")

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
        "#6P#0200Fつい駆け込んでしまいましたね。\x02",
    )

    CloseMessageWindow()

    def lambda_49C2():
        TurnDirection(0xFE, 0x103, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_49C2)
    Sleep(15)

    def lambda_49D2():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_49D2)
    Sleep(12)

    def lambda_49E2():
        TurnDirection(0xFE, 0x104, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_49E2)
    Sleep(20)

    def lambda_49F2():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_49F2)
    Sleep(300)

    #C0162
    ChrTalk(
        0x102,
        (
            "#6P#0106F臨検の手続きとかは\x01",
            "良かったのかしら。\x02",
        )
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0x101,
        (
            "#11P#0003F捜査中の警察官なら\x01",
            "緊急乗車できるはずだ……\x01",
            "そっちは心配要らないよ。\x02\x03",

            "#0001Fただ、問題は\x01",
            "ここからどうするかだな。\x02",
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
            "#6P#0105Fカーラさんを\x01",
            "説得してみるんじゃなかったの？\x02",
        )
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0x104,
        (
            "#11P#0303Fま、といっても\x01",
            "どこまでも乗っていくわけには\x01",
            "いかねえだろ。\x02\x03",

            "#0301F俺たちはまだ例の薬を\x01",
            "ウルスラ大に持ってかなくちゃ\x01",
            "ならねえしな。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x104, 400)
    Sleep(300)

    #C0166
    ChrTalk(
        0x103,
        (
            "#6P#0203F……そうでしたね。\x02\x03",

            "#0200Fでも、ここまで来て\x01",
            "諦めるというのも。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x1)
    Sleep(1800)

    #C0167
    ChrTalk(
        0x101,
        (
            "#5P#0003F次の停車駅は\x01",
            "共和国西端のアルタイル市だ……\x02\x03",

            "#0001F多分３０分くらいで着くはずだよ。\x02\x03",

            "そこまでは粘って、\x01",
            "家に戻るよう説得してみよう。\x02",
        )
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0x104,
        "#11P#0300F了解、それで行くか。\x02",
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0x102,
        (
            "#6P#0108Fそうね……話を聞いてくれると\x01",
            "いいんだけど……\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, 2480, 0, -8200, 270)
    OP_29(0x2D, 0x1, 0xC)
    EventEnd(0x5)
    Return()

    # Function_29_48B8 end

    def Function_30_4D29(): pass

    label("Function_30_4D29")

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
        "#0105F（カーラさんだわ……）\x02",
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0x104,
        "#0300F（へっ、ようやく見つけたか。）\x02",
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0x103,
        (
            "#0200F（家に帰るように\x01",
            "  説得してみましょう。）\x02\x03",

            "（聞き分けてくれるかは\x01",
            "  分かりませんが……）\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, 100, 0, -8640, 0)
    OP_29(0x2D, 0x1, 0xD)
    EventEnd(0x5)
    Return()

    # Function_30_4D29 end

    def Function_31_4EA7(): pass

    label("Function_31_4EA7")

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
            "#5Pマーシャ、まさか\x01",
            "乗り遅れてしまったのかしら……\x02",
        )
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0x10,
        (
            "#5Pそれじゃあ私一人じゃない……\x01",
            "……大丈夫、かしら……\x02",
        )
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0x102,
        "#6P#0100F久し振りね、カーラさん。\x02",
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
        "#5Pエリィさん……？\x02",
    )

    CloseMessageWindow()
    OP_63(0x10, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(800)

    #C0177
    ChrTalk(
        0x10,
        (
            "#5Pき、奇遇ですわね、\x01",
            "こんな所でお会いするなんて。\x02",
        )
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0x10,
        "#5Pそちらの方はお友達……かしら。\x02",
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0x10,
        (
            "#5Pもしかして\x01",
            "皆さんで共和国にご用なの？\x02",
        )
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0x102,
        (
            "#6P#0109Fあはは……その……\x01",
            "（何て切り出そうかしら……）\x02",
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
            "【実は連れ戻しに来たの】\x01",          # 0
            "【共和国に観光に行く所なの】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    FadeToBright(300, 0)
    OP_60(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_532E")
    OP_63(0x10, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1200)

    #C0181
    ChrTalk(
        0x10,
        "#5Pま、まさかお父様の差し金で……！？\x02",
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0x10,
        (
            "#5Pみ、見損ないましたわ！！\x01",
            "そちらの方々もお仲間ですのね！\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x10, 0x2)
    Sleep(200)

    #C0183
    ChrTalk(
        0x10,
        (
            "#5Pフン……嫌です。\x01",
            "私は絶対帰りません！\x02",
        )
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0x101,
        "#11P#0006F（直球だとダメなのかな。）\x02",
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0x104,
        "#12P#0303F（みてえだなぁ……）\x02",
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0x102,
        (
            "#6P#0106F（ゴメンなさい、\x01",
            "  頑なになってしまったかも。）\x02",
        )
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0x103,
        (
            "#12P#0203Fともかく、家出の事情を\x01",
            "話して頂けませんか？\x02\x03",

            "#0200F書き置きからすると、\x01",
            "何か原因があったように\x01",
            "思われますが。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_546D")

    label("loc_532E")

    OP_2C(0x2D, 0x1)

    #C0188
    ChrTalk(
        0x102,
        (
            "#6P#0100Fええ、みんなで\x01",
            "共和国の国立楽団でも\x01",
            "見に行こうかと思って。\x02",
        )
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0x10,
        (
            "#5Pそれなら共和国の首都まで\x01",
            "ご一緒できるわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0x10,
        (
            "#5Pよかった……\x01",
            "私、少し心細かったんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0191
    ChrTalk(
        0x10,
        (
            "#5Pその、事情があって\x01",
            "今は一人だから……\x02",
        )
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0x101,
        (
            "#11P#0003F（よし、何とか\x01",
            "  踏み込んだ話ができそうだ……）\x02\x03",

            "#0000Fその事情というのは……？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_546D")


    #C0193
    ChrTalk(
        0x10,
        "#5Pそ、それは……\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x10, 0x2)
    Sleep(200)

    #C0194
    ChrTalk(
        0x10,
        (
            "#5Pお父様は身勝手で、\x01",
            "あれこれルールを決めて指図するくせに\x01",
            "自分はろくに守らないんですわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0x10,
        "#5P……その極め付けが今朝なんです。\x02",
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0x10,
        (
            "#5Pあの行為だけは\x01",
            "絶対に許せませんわ……！\x02",
        )
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0x102,
        "#6P#0105Fあの行為……？\x02",
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0x101,
        "#11P#0005F………それは一体………\x02",
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
            "#5P朝食の後、ノックをせずに\x01",
            "私の部屋に入って来たんです。\x02",
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
        "#12P#0305Fえ……それだけかよ？\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x10, 0x1)
    Sleep(200)

    #C0202
    ChrTalk(
        0x10,
        (
            "#5Pそれだけじゃありません！\x01",
            "着替え中だったらどうするんですの！\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x10, 0x0)
    Sleep(200)

    #C0203
    ChrTalk(
        0x10,
        (
            "#5Pそれに『ノックしろ』というのは\x01",
            "お父様がいつも\x01",
            "うるさく言ってくる事なんです！\x02",
        )
    )

    CloseMessageWindow()

    #C0204
    ChrTalk(
        0x10,
        (
            "#5Pそれを破ると散々文句を\x01",
            "言ってくるくせに……\x02",
        )
    )

    CloseMessageWindow()

    #C0205
    ChrTalk(
        0x10,
        (
            "#5P今朝は平然と入ってきて、\x01",
            "午前中はあれをしろだの\x01",
            "夜の晩餐会に出ろだの……！\x02",
        )
    )

    CloseMessageWindow()

    #C0206
    ChrTalk(
        0x10,
        (
            "#5P私の私生活に\x01",
            "いちいちいちいち\x01",
            "細かい事ばかり……！\x02",
        )
    )

    CloseMessageWindow()

    #C0207
    ChrTalk(
        0x103,
        (
            "#12P#0203F（確かに気持ちは分かりますが……\x01",
            "  『父娘の行き違い』以上でも\x01",
            "  以下でもありませんね。）\x02",
        )
    )

    CloseMessageWindow()

    #C0208
    ChrTalk(
        0x101,
        "#11P#0003F（うーん、ここは……）\x02",
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
            "【それはお父上が悪いですね】\x01",        # 0
            "【鍵を掛けておくというのは？】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    FadeToBright(300, 0)
    OP_60(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5960")
    OP_2C(0x2D, 0x1)

    #C0209
    ChrTalk(
        0x101,
        (
            "#11P#0006Fそれはお父上が悪いですね。\x01",
            "同情いたします。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x10, 0x1)
    Sleep(200)

    #C0210
    ChrTalk(
        0x10,
        "#5Pや、やっぱりそうですわよね。\x02",
    )

    CloseMessageWindow()

    #C0211
    ChrTalk(
        0x10,
        (
            "#5Pフン……今日は家出して\x01",
            "正解でしたわ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5A7F")

    label("loc_5960")


    #C0212
    ChrTalk(
        0x101,
        (
            "#11P#0006Fええと……お部屋に\x01",
            "鍵を掛けておくというのは？\x02",
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
            "#5Pそういう事じゃないんですの！\x01",
            "自分だけ身勝手なのが許せないと\x01",
            "言ってるんです！\x02",
        )
    )

    CloseMessageWindow()

    #C0214
    ChrTalk(
        0x10,
        (
            "#5Pプン……もういいですわ。\x01",
            "私は共和国に行きます。\x02",
        )
    )

    CloseMessageWindow()

    #C0215
    ChrTalk(
        0x10,
        (
            "#5Pお父様は１人で\x01",
            "好きになさったらいいんですわ！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5A7F")

    SetChrSubChip(0x10, 0x0)
    Sleep(300)
    OP_63(0x10, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x1)
    Sleep(1800)

    #C0216
    ChrTalk(
        0x10,
        (
            "#5Pでも……クロスベルを\x01",
            "離れるのは初めてですし……\x02",
        )
    )

    CloseMessageWindow()

    #C0217
    ChrTalk(
        0x10,
        (
            "#5Pはあ、マーシャが\x01",
            "一緒に来てくれるって言ったから\x01",
            "決行したのに……\x02",
        )
    )

    CloseMessageWindow()

    #C0218
    ChrTalk(
        0x104,
        (
            "#12P#0303F（大体の事情は判ったが……\x01",
            "  どうやらまだ\x01",
            "  迷いがあるみてえだな？）\x02",
        )
    )

    CloseMessageWindow()

    #C0219
    ChrTalk(
        0x102,
        (
            "#6P#0108F（もともと\x01",
            "  心の強い方ではないし……）\x02\x03",

            "（つい飛び出してしまったけれど、\x01",
            "  段々と不安になって\x01",
            "  きたんじゃないかしら。）\x02",
        )
    )

    CloseMessageWindow()

    #C0220
    ChrTalk(
        0x101,
        (
            "#11P#0003F（そうか……となると\x01",
            "  もう一押し……）\x02",
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
            "【やはり一人旅は危険ですし】\x01",          # 0
            "【お父上も心配していますし】\x01",          # 1
            "【メイドさんも心配していますし】\x01",      # 2
        )
    )

    MenuEnd(0x0)
    FadeToBright(300, 0)
    OP_60(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_61A0")
    OP_2C(0x2D, 0x5)
    OP_63(0x10, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    SetChrSubChip(0x10, 0x1)
    Sleep(1000)

    #C0221
    ChrTalk(
        0x10,
        (
            "#5Pそういえば、マーシャの姿が\x01",
            "見えないと思っていたけれど……\x02",
        )
    )

    CloseMessageWindow()

    #C0222
    ChrTalk(
        0x10,
        (
            "#5P……あの子、私を\x01",
            "裏切ったんですのね！？\x02",
        )
    )

    CloseMessageWindow()

    #C0223
    ChrTalk(
        0x10,
        (
            "#5Pゆ、許せませんわ……\x01",
            "誰にも喋るなと命じたのに……！\x02",
        )
    )

    CloseMessageWindow()

    #C0224
    ChrTalk(
        0x102,
        (
            "#6P#0105F落ち着いてください、カーラさん。\x02\x03",

            "#0103F確かにマーシャさんは\x01",
            "お話を聞かせてくれました。\x02\x03",

            "#0100Fでもそれはカーラさんの身を\x01",
            "案じてのことなんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0x103,
        (
            "#12P#0200Fええ、カーラさんが本心では\x01",
            "クロスベルを離れたがっていないと。\x01",
            "そう仰っていました。\x02",
        )
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0x10,
        (
            "#5Pマーシャ……\x01",
            "本当にそんなことを？\x02",
        )
    )

    CloseMessageWindow()

    #C0227
    ChrTalk(
        0x101,
        (
            "#11P#0000Fお嬢様をお願いします、と\x01",
            "言われて参りました。\x02",
        )
    )

    CloseMessageWindow()

    #C0228
    ChrTalk(
        0x104,
        (
            "#12P#0304Fま、親父さんとの事は\x01",
            "一度話し合うべきだろうな。\x02\x03",

            "#0300Fあんたも姿をくらますより、\x01",
            "ガツンと言った方が\x01",
            "気が晴れるんじゃねえか？\x02",
        )
    )

    CloseMessageWindow()

    #C0229
    ChrTalk(
        0x10,
        "#5Pそう、ですね……\x02",
    )

    CloseMessageWindow()

    #C0230
    ChrTalk(
        0x10,
        (
            "#5P私、周りに味方が\x01",
            "誰もいないのかと思って……\x02",
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
            "#5Pでもマーシャや皆さんがいるのなら、\x01",
            "戻ってもいいかもしれません。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x10, 0x1)
    Sleep(200)

    #C0232
    ChrTalk(
        0x10,
        (
            "#5Pあの、皆さん……\x01",
            "もう少し私の愚痴に\x01",
            "付き合ってくださいます？\x02",
        )
    )

    CloseMessageWindow()

    #C0233
    ChrTalk(
        0x10,
        (
            "#5Pお父様に何と言ってやるか、\x01",
            "今から考えておかないと。\x02",
        )
    )

    CloseMessageWindow()

    #C0234
    ChrTalk(
        0x101,
        "#11P#0000Fハハ、そうですね。\x02",
    )

    CloseMessageWindow()

    #C0235
    ChrTalk(
        0x103,
        (
            "#12P#0200Fそろそろアルタイル市ですが、\x01",
            "まだ帰りの便がありますし。\x02",
        )
    )

    CloseMessageWindow()

    #C0236
    ChrTalk(
        0x102,
        (
            "#6P#0100F私達で良ければ\x01",
            "喜んでお付き合いします。\x02",
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
    Jump("loc_6432")

    label("loc_61A0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6236")

    #C0237
    ChrTalk(
        0x10,
        (
            "#5Pう……\x01",
            "それは分かっていますわ。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x10, 0x2)
    Sleep(200)

    #C0238
    ChrTalk(
        0x10,
        (
            "#5Pでも、だからこそ行くんですわ！\x01",
            "私の覚悟をお父様に\x01",
            "思い知らせてやるんです！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_62BE")

    label("loc_6236")

    SetChrSubChip(0x10, 0x1)
    Sleep(200)

    #C0239
    ChrTalk(
        0x10,
        (
            "#5P……やはりあなた達は\x01",
            "お父様に雇われて……\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x10, 0x2)
    Sleep(200)

    #C0240
    ChrTalk(
        0x10,
        "#5Pフン、心配すればいいんですわ。\x02",
    )

    CloseMessageWindow()

    #C0241
    ChrTalk(
        0x10,
        "#5P私、絶対帰りませんから！\x02",
    )

    CloseMessageWindow()

    label("loc_62BE")


    #C0242
    ChrTalk(
        0x101,
        (
            "#11P#0006Fそ、そうですか……\x02\x03",

            "#0008F（これ以上の説得は\x01",
            "  難しいかもしれないな……）\x02",
        )
    )

    CloseMessageWindow()

    #C0243
    ChrTalk(
        0x103,
        (
            "#12P#0200F（ええ、そろそろアルタイル市に\x01",
            "  着いてしまいます。）\x02",
        )
    )

    CloseMessageWindow()

    #C0244
    ChrTalk(
        0x104,
        "#12P#0306F（タイムオーバーか……）\x02",
    )

    CloseMessageWindow()

    #C0245
    ChrTalk(
        0x102,
        (
            "#6P#0100Fカーラさん……\x01",
            "それでは連絡先だけ\x01",
            "教えていただけますか？\x02\x03",

            "議員にはそれだけ伝えて\x01",
            "納得してもらいますから。\x02",
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

    label("loc_6432")

    Return()

    # Function_31_4EA7 end

    def Function_32_6433(): pass

    label("Function_32_6433")

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
        "#11P──はっ！？\x02",
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
        "#11P#60W……ここは………\x02",
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
            "#11P#0006F#30Wそっか……そうだった。\x02\x03",

            "#30W叔父さんたちに挨拶して……\x01",
            "荷物を送ってから列車に乗って……\x02\x03",

            "#0008F#40W…………それで………………\x02",
        )
    )

    CloseMessageWindow()

    #N0249
    NpcTalk(
        0x12,
        "老婦人の声",
        "#1P……あなた、大丈夫？\x02",
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
        "目が覚めたようじゃな。\x02",
    )

    CloseMessageWindow()

    #C0251
    ChrTalk(
        0x11,
        (
            "うなされておったが\x01",
            "どこか具合でも悪いのかね？\x02",
        )
    )

    CloseMessageWindow()

    #C0252
    ChrTalk(
        0x101,
        (
            "#7P#0011Fい、いや……\x01",
            "ちょっと寝不足だっただけで。\x02\x03",

            "#0006Fなんだか……\x01",
            "変な夢を見ていたみたいだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0253
    ChrTalk(
        0x11,
        "ほほう、変な夢か。\x02",
    )

    CloseMessageWindow()

    #C0254
    ChrTalk(
        0x11,
        (
            "もしや色っぽい女子#4Rお な ご#どもに迫られて\x01",
            "あたふたする夢でも見てたかの～？\x02",
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
            "#7P#0012Fい、いや～……\x01",
            "そんな良い夢じゃなかった気が。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x12, 0x2)
    Sleep(300)

    #C0256
    ChrTalk(
        0x12,
        (
            "#5Pもう、おじいさん。\x01",
            "若い人をからかっちゃ駄目ですよ。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x12, 0x0)
    Sleep(300)

    #C0257
    ChrTalk(
        0x12,
        (
            "#5Pそうだ、眠気覚ましに\x01",
            "冷たいレモネードでもいかが？\x02",
        )
    )

    CloseMessageWindow()

    #C0258
    ChrTalk(
        0x12,
        (
            "#5P凍らせたものを水筒に入れて\x01",
            "持ってきているの。\x02",
        )
    )

    CloseMessageWindow()

    #C0259
    ChrTalk(
        0x101,
        (
            "#7P#0000Fあ……\x01",
            "それじゃ、ありがたく。\x02",
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
        "#11Pんくっ、んくっ……\x02",
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
            "#0014F#11Pぷは～～っ！\x02\x03",

            "#0002Fごちそうさま！\x01",
            "冷たくて凄く美味しかった。\x02",
        )
    )

    CloseMessageWindow()

    #C0262
    ChrTalk(
        0x12,
        "#1Pふふ、お粗末さま。\x02",
    )

    CloseMessageWindow()

    #C0263
    ChrTalk(
        0x11,
        (
            "#6Pしかしその格好……\x01",
            "帝国人ではなさそうじゃな。\x02",
        )
    )

    CloseMessageWindow()

    #C0264
    ChrTalk(
        0x11,
        "#6Pやはりクロスベル出身かね？\x02",
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
            "#0005F#11Pあ、うん。\x02\x03",

            "#0004F……しばらく外国で\x01",
            "暮らしていたんだけど\x01",
            "戻ってくる事になったんだ。\x02\x03",

            "#0000Fそういうお爺さんたちも\x01",
            "やっぱりクロスベル出身？\x02",
        )
    )

    CloseMessageWindow()

    #C0266
    ChrTalk(
        0x11,
        (
            "#6Pうむ、共和国方面を旅行して\x01",
            "ちょうど戻ってきたところじゃよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0267
    ChrTalk(
        0x11,
        (
            "#6P……しかし、そういう事なら\x01",
            "今のクロスベルを見たら\x01",
            "驚くかもしれんな。\x02",
        )
    )

    CloseMessageWindow()

    #C0268
    ChrTalk(
        0x12,
        "#1Pそうですねぇ。\x02",
    )

    CloseMessageWindow()

    #C0269
    ChrTalk(
        0x12,
        (
            "#1Pここ２、３年で街並みも\x01",
            "けっこう変わってしまって……\x02",
        )
    )

    CloseMessageWindow()

    #C0270
    ChrTalk(
        0x101,
        (
            "#0003F#11Pやっぱり、そうか……\x02\x03",

            "#0001F……実は最近、\x01",
            "何度か列車でクロスベル市を\x01",
            "通り過ぎたんだけど……\x02\x03",

            "ずいぶん背の高い建物が\x01",
            "建つようになったみたいだね？\x02",
        )
    )

    CloseMessageWindow()

    #C0271
    ChrTalk(
        0x11,
        (
            "#6Pうむ、元々クロスベルは\x01",
            "大陸有数の貿易都市の一つじゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0272
    ChrTalk(
        0x11,
        (
            "#6P金融業も発達していたため、\x01",
            "諸外国からミラが集まりやすい\x01",
            "傾向にあったのじゃが……\x02",
        )
    )

    CloseMessageWindow()

    #C0273
    ChrTalk(
        0x11,
        (
            "#6P一昨年の《不戦条約》以来、\x01",
            "その流れが加速したようでな。\x02",
        )
    )

    CloseMessageWindow()

    #C0274
    ChrTalk(
        0x11,
        (
            "#6P莫大なミラの投資対象として\x01",
            "デパートやらオフィスビルやらが\x01",
            "次々と建てられているのじゃよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0275
    ChrTalk(
        0x12,
        (
            "#1P色々便利になったのはいいけれど\x01",
            "少し目まぐるしくなったわねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0276
    ChrTalk(
        0x12,
        (
            "#1P誰もがみんな、時間とミラ儲けに\x01",
            "追われるようになったというか……\x02",
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
            "#1Pあら、ごめんなさいね。\x01",
            "せっかく帰って来てくれたのに。\x02",
        )
    )

    CloseMessageWindow()

    #C0279
    ChrTalk(
        0x12,
        "#1P悪いことを言ってしまったかしら。\x02",
    )

    CloseMessageWindow()

    #C0280
    ChrTalk(
        0x101,
        (
            "#0012F#11Pいや、気にしないでよ。\x02\x03",

            "#0002F手紙で色々と聞いているし……\x01",
            "それにどんなに変わったとしても\x01",
            "故郷#4Rクロスベル#は故郷#4Rクロスベル#だから。\x02",
        )
    )

    CloseMessageWindow()

    #C0281
    ChrTalk(
        0x12,
        "#1Pそう……\x02",
    )

    CloseMessageWindow()

    #C0282
    ChrTalk(
        0x11,
        "#6Pふむ、若いのに分かっとるのう。\x02",
    )

    CloseMessageWindow()

    #C0283
    ChrTalk(
        0x11,
        (
            "#6Pそれに引き換え、\x01",
            "最近の政治家どもときたら……\x02",
        )
    )

    CloseMessageWindow()

    #C0284
    ChrTalk(
        0x11,
        (
            "#6Pやれ帝国派だの、やれ共和国派だの\x01",
            "利権争いばかり繰り広げおって……\x02",
        )
    )

    CloseMessageWindow()

    #C0285
    ChrTalk(
        0x11,
        (
            "#6Pもはや信頼できるのは\x01",
            "マクダエル市長しかおらんわい。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x12, 0x2)
    Sleep(300)

    #C0286
    ChrTalk(
        0x12,
        "#1Pおじいさん、おじいさん。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x12, 0x0)
    Sleep(300)

    #C0287
    ChrTalk(
        0x12,
        (
            "#1P……ごめんなさいね。\x01",
            "この人ときたら、政治の話になると\x01",
            "いつも我を忘れてしまって。\x02",
        )
    )

    CloseMessageWindow()

    #C0288
    ChrTalk(
        0x101,
        (
            "#0000F#11Pいや……勉強になるよ。\x02\x03",

            "外国でも《クロスベルタイムズ》は\x01",
            "取り寄せていたんだけど……\x02\x03",

            "実際に話を聞いてみないと\x01",
            "本当のところは分からないから。\x02",
        )
    )

    CloseMessageWindow()

    #C0289
    ChrTalk(
        0x11,
        (
            "#6Pほう、お前さんも\x01",
            "《クロスベルタイムズ》の愛読者か。\x02",
        )
    )

    CloseMessageWindow()

    #C0290
    ChrTalk(
        0x11,
        (
            "#6P多少ミーハーなところもあるが\x01",
            "なかなか良い記事を書く雑誌じゃろ？\x02",
        )
    )

    CloseMessageWindow()

    #C0291
    ChrTalk(
        0x11,
        (
            "#6Pもう少し自治州行政の問題点に\x01",
            "突っ込んで欲しいところじゃが……\x02",
        )
    )

    CloseMessageWindow()

    #C0292
    ChrTalk(
        0x101,
        (
            "#0012F#11Pなるほど……\x01",
            "やっぱり色々あるみたいだね。\x02",
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
        "#0005F#2Pあ……！\x02",
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
    SetChrName("車掌の声")

    #A0294
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "──乗客の皆様にお伝えします。\x02",
        )
    )

    CloseMessageWindow()

    #A0295
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "まもなく、クロスベル自治州、\x01",
            "クロスベル市に到着いたします。\x02",
        )
    )

    CloseMessageWindow()

    #A0296
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

    #A0297
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

    #A0298
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

    #C0299
    ChrTalk(
        0x11,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#6P……ふむ、到着のようじゃの。\x02",
        )
    )

    CloseMessageWindow()

    #C0300
    ChrTalk(
        0x11,
        (
            "#6P帝国軍人の顔など見たくもないし、\x01",
            "とっとと支度をするとしようか。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)
    Sleep(300)

    #C0301
    ChrTalk(
        0x101,
        (
            "#0012F#11Pははっ、そうだね。\x02\x03",

            "#0008F…………………………………\x02\x03",

            "（あれから３年、か……）\x02\x03",

            "（セシル姉とは何度か\x01",
            "  導力通信で話してるけど……）\x02\x03",

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
    SetChrName("ロイド")

    #A0302
    AnonymousTalk(
        0xFF,
        (
            "#0004F（……兄貴、セシル姉………）\x02\x03",

            "（俺、やっと帰ってきたよ。）\x02\x03",

            "#0002F（クロスベルに……\x01",
            "  みんなで過ごしたあの街に。）\x02",
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

    # Function_32_6433 end

    def Function_33_7A35(): pass

    label("Function_33_7A35")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7A6D")
    OP_82(0xA, 0xA, 0x5DC, 0x2EE)
    Sleep(3500)
    OP_82(0xA, 0xA, 0x4B0, 0x1F4)
    Sleep(3500)
    Jump("Function_33_7A35")

    label("loc_7A6D")

    Return()

    # Function_33_7A35 end

    def Function_34_7A6E(): pass

    label("Function_34_7A6E")

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

    # Function_34_7A6E end

    def Function_35_7AB9(): pass

    label("Function_35_7AB9")

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

    # Function_35_7AB9 end

    SaveToFile()

Try(main)
