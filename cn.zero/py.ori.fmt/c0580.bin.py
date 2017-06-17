from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "c0580.bin",                # FileName
        "c0580",                    # MapName
        "c0580",                    # Location
        0x0028,                     # MapIndex
        "ed7117",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 40, 0, 1, 0, 2],
    )

    BuildStringList((
        "c0580",                  # 0
        "伊梅尔达夫人",           # 1
        "玲",                     # 2
        "游客",                   # 3
        "人偶",                   # 4
    ))

    AddCharChip((
        "chr/ch24400.itc",                   # 00
        "chr/ch09002.itc",                   # 01
        "chr/ch09500.itc",                   # 02
        "apl/ch50093.itc",                   # 03
    ))

    DeclNpc(-750,    100,     4800,    180,  261,  0x0, 0,   1,   0,   255, 255, 0,   4,   255,  0)
    DeclNpc(-4170,   0,       239,     270,  405,  0x0, 0,   2,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(560,     0,       -1159,   90,   389,  0x0, 0,   0,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(-600,    850,     3500,    0,    502,  0x0, 0,   3,   0,   255, 255, 255, 255, 255,  0)

    DeclActor(-750,    0,       3500,    1500,    -750,    1500,    4800,    0x007E, 0,  3,  0x0000)
    DeclActor(-5470,   0,       120,     1200,    -5470,   2000,    120,     0x007C, 0,  24, 0x0000)

    ScpFunction((
        "Function_0_1C0",          # 00, 0
        "Function_1_278",          # 01, 1
        "Function_2_2E1",          # 02, 2
        "Function_3_48C",          # 03, 3
        "Function_4_490",          # 04, 4
        "Function_5_39F7",         # 05, 5
        "Function_6_3C3F",         # 06, 6
        "Function_7_3EE0",         # 07, 7
        "Function_8_4064",         # 08, 8
        "Function_9_428B",         # 09, 9
        "Function_10_4621",        # 0A, 10
        "Function_11_4A22",        # 0B, 11
        "Function_12_4B1E",        # 0C, 12
        "Function_13_4B94",        # 0D, 13
        "Function_14_52B3",        # 0E, 14
        "Function_15_5334",        # 0F, 15
        "Function_16_5780",        # 10, 16
        "Function_17_588E",        # 11, 17
        "Function_18_59E6",        # 12, 18
        "Function_19_5D94",        # 13, 19
        "Function_20_6520",        # 14, 20
        "Function_21_6B06",        # 15, 21
        "Function_22_6F78",        # 16, 22
        "Function_23_78ED",        # 17, 23
        "Function_24_83BE",        # 18, 24
    ))


    def Function_0_1C0(): pass

    label("Function_0_1C0")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_200"),
        (1, "loc_20C"),
        (2, "loc_218"),
        (3, "loc_224"),
        (4, "loc_230"),
        (5, "loc_23C"),
        (6, "loc_248"),
        (SWITCH_DEFAULT, "loc_254"),
    )


    label("loc_200")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_260")

    label("loc_20C")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_260")

    label("loc_218")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_260")

    label("loc_224")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_260")

    label("loc_230")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_260")

    label("loc_23C")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_260")

    label("loc_248")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_260")

    label("loc_254")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_260")

    label("loc_260")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_277")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_260")

    label("loc_277")

    Return()

    # Function_0_1C0 end

    def Function_1_278(): pass

    label("Function_1_278")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_287")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 19)

    label("loc_287")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_295")
    Jump("loc_2E0")

    label("loc_295")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_2B6")
    ClearChrFlags(0xA, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_2B1")
    SetChrFlags(0xA, 0x10)

    label("loc_2B1")

    Jump("loc_2E0")

    label("loc_2B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_2C4")
    Jump("loc_2E0")

    label("loc_2C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_2E0")
    ClearChrFlags(0x9, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x93, 0)), scpexpr(EXPR_END)), "loc_2E0")
    ClearChrFlags(0x9, 0x10)

    label("loc_2E0")

    Return()

    # Function_1_278 end

    def Function_2_2E1(): pass

    label("Function_2_2E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2FD")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_37F")

    label("loc_2FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_319")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_37F")

    label("loc_319")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_335")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_37F")

    label("loc_335")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_351")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x69), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_37F")

    label("loc_351")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_36D")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_37F")

    label("loc_36D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 1)), scpexpr(EXPR_END)), "loc_37F")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0xCB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_37F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_39B")
    OP_10(0x0, 0x0)
    OP_10(0x1, 0x1)
    OP_10(0x2, 0x0)
    Jump("loc_3C0")

    label("loc_39B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3B7")
    OP_10(0x0, 0x0)
    OP_10(0x1, 0x0)
    OP_10(0x2, 0x1)
    Jump("loc_3C0")

    label("loc_3B7")

    OP_10(0x0, 0x1)
    OP_10(0x1, 0x0)
    OP_10(0x2, 0x0)

    label("loc_3C0")

    OP_52(0xB, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_3EF")
    Jump("loc_48B")

    label("loc_3EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_END)), "loc_436")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF1, 5)), scpexpr(EXPR_END)), "loc_406")
    Jump("loc_431")

    label("loc_406")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x30, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_417")
    Jump("loc_431")

    label("loc_417")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x14), scpexpr(EXPR_PUSH_LONG, 0x120), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_431")
    Event(0, 21)

    label("loc_431")

    Jump("loc_48B")

    label("loc_436")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_444")
    Jump("loc_48B")

    label("loc_444")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_48B")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x1, 0x6)"), scpexpr(EXPR_END)), "loc_45F")
    Jump("loc_48B")

    label("loc_45F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x95, 7)), scpexpr(EXPR_END)), "loc_46D")
    Jump("loc_48B")

    label("loc_46D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x1, 0x5)"), scpexpr(EXPR_END)), "loc_48B")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_48B")
    Event(0, 20)

    label("loc_48B")

    Return()

    # Function_2_2E1 end

    def Function_3_48C(): pass

    label("Function_3_48C")

    Call(0, 4)
    Return()

    # Function_3_48C end

    def Function_4_490(): pass

    label("Function_4_490")

    SetScenarioFlags(0x53, 1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_4BD")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x30, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x30, 0x0, 0x40)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD3, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4B8")
    Call(0, 5)
    Return()

    label("loc_4B8")

    Jump("loc_548")

    label("loc_4BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_END)), "loc_4ED")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x30, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_4D7")
    Jump("loc_4E8")

    label("loc_4D7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x30, 0x1, 0x5)"), scpexpr(EXPR_END)), "loc_4E8")
    Call(0, 23)
    Return()

    label("loc_4E8")

    Jump("loc_548")

    label("loc_4ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_4FB")
    Jump("loc_548")

    label("loc_4FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_526")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xA, 0x1, 0x1)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0xA, 0x0, 0x40)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x93, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_521")
    Call(0, 6)
    Return()

    label("loc_521")

    Jump("loc_548")

    label("loc_526")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_548")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xA, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0xA, 0x1, 0x0)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_548")
    Call(0, 15)
    Return()

    label("loc_548")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0x8)
    ClearChrFlags(0x8, 0x10)
    TurnDirection(0x8, 0x0, 0)
    OP_52(0x8, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5DC")
    Jump("loc_626")

    label("loc_5DC")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5FC")
    OP_52(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_626")

    label("loc_5FC")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_61C")
    OP_52(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_626")

    label("loc_61C")

    OP_52(0x8, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_626")

    OP_52(0x8, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x8, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_6C2")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('黑市医生格伦　１卷', 0x0)"), scpexpr(EXPR_EXEC_OP, "GetItemNumber('黑市医生格伦　２卷', 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber('黑市医生格伦　３卷', 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber('黑市医生格伦　４卷', 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber('黑市医生格伦　５卷', 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber('黑市医生格伦　６卷', 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber('黑市医生格伦　７卷', 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber('黑市医生格伦　８卷', 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber('黑市医生格伦　９卷', 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber('黑市医生格伦　10卷', 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber('黑市医生格伦　11卷', 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber('黑市医生格伦　12卷', 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber('黑市医生格伦　13卷', 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber('黑市医生格伦　14卷', 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9D, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xEF, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6C2")
    Call(0, 10)
    SetChrSubChip(0x8, 0x0)
    TalkEnd(0x8)
    Return()

    label("loc_6C2")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6CC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_39EF")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_71C")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_71C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_74C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_73B")
    OP_AF(0x44)
    Jump("loc_73D")

    label("loc_73B")

    OP_AF(0x43)

    label("loc_73D")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_39EA")

    label("loc_74C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_760")
    Jump("loc_39EA")

    label("loc_760")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_39EA")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_A39")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('黑市医生格伦　１卷', 0x0)"), scpexpr(EXPR_EXEC_OP, "GetItemNumber('黑市医生格伦　２卷', 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber('黑市医生格伦　３卷', 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber('黑市医生格伦　４卷', 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber('黑市医生格伦　５卷', 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber('黑市医生格伦　６卷', 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber('黑市医生格伦　７卷', 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber('黑市医生格伦　８卷', 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber('黑市医生格伦　９卷', 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber('黑市医生格伦　10卷', 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber('黑市医生格伦　11卷', 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber('黑市医生格伦　12卷', 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber('黑市医生格伦　13卷', 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber('黑市医生格伦　14卷', 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9D, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7E8")
    Call(0, 10)
    Jump("loc_A34")

    label("loc_7E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xED, 7)), scpexpr(EXPR_END)), "loc_844")

    #C0001
    ChrTalk(
        0x8,
        (
            "小鬼们，和协会的诸位\x01",
            "一起好好加油吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x8,
        (
            "为了平息这种\x01",
            "莫名其妙的事态。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A34")

    label("loc_844")


    #C0003
    ChrTalk(
        0x8,
        (
            "说起来，马尔克尼他们\x01",
            "消失得无影无踪了。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x8,
        "到底发生了什么？\x02",
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x101,
        "#0003F您果然知道了吗……\x02",
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x104,
        (
            "#0306F嗯，离得这么近，\x01",
            "也多少能听到一些情报吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x8,
        (
            "当然啦。\x01",
            "不过，至于最关键的部分，\x01",
            "仍然还是有很多地方暧昧不明呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x8,
        (
            "我向认识的议员和\x01",
            "警察上层的人打听了一下，\x01",
            "也没得到什么可靠的线索。\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x102,
        "#0108F是吗……\x02",
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x103,
        (
            "#0203F看起来，到处\x01",
            "都有种混乱的感觉。\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x8,
        (
            "总之，小鬼们\x01",
            "好好加油吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x8,
        (
            "为了平息这种\x01",
            "莫名其妙的事态。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x101,
        "#0001F……嗯，当然。\x02",
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x102,
        "#0100F虽然力量微薄，但我们仍会全力以赴。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0xED, 7)

    label("loc_A34")

    Jump("loc_39EA")

    label("loc_A39")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_C54")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_AED")

    #C0015
    ChrTalk(
        0x8,
        (
            "看起来，事情好像\x01",
            "变得越来越奇怪了。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x8,
        (
            "我们天天交着\x01",
            "高额的税金。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x8,
        (
            "你们要是不努力把这件事情\x01",
            "尽快解决的话，我们会很困扰的。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x10A,
        "#0603F……明白了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_C4F")

    label("loc_AED")


    #C0019
    ChrTalk(
        0x8,
        (
            "哎呀，小鬼们，\x01",
            "你们这次带来了一位稀客啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x10A,
        (
            "#0603F……伊梅尔达夫人，\x01",
            "这几个家伙只是受我指挥\x01",
            "的部下而已。\x02\x03",

            "#0600F请不要说一些让他们\x01",
            "得意忘形的话。\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x8,
        (
            "嘿嘿嘿，你和他们有什么区别啊，\x01",
            "不也是个连毛都没长齐的小鬼嘛。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x8,
        "就别装模作样啦。\x02",
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x10A,
        "#0601F呜……\x02",
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x101,
        "#0000F（真、真不愧是伊梅尔达夫人……）\x02",
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x103,
        "#0200F（连一科的王牌也完全哑口无言了。）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_C4F")

    Jump("loc_39EA")

    label("loc_C54")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_D85")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_CC0")

    #C0026
    ChrTalk(
        0x8,
        (
            "说起来，清晨的时候，\x01",
            "有好几辆鲁巴彻的车\x01",
            "开出来了。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x8,
        (
            "他们似乎是\x01",
            "有什么动作。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D80")

    label("loc_CC0")


    #C0028
    ChrTalk(
        0x8,
        (
            "………………………………\x01",
            "话说，今天真是安静得反常呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x8,
        (
            "黑月好像也没有发动报复，\x01",
            "这到底是怎么回事呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x101,
        "#0003F（确实如此……）\x02",
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x104,
        (
            "#0301F（但愿不是暴风雨\x01",
            "  来临之前的寂静啊。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_D80")

    Jump("loc_39EA")

    label("loc_D85")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_END)), "loc_1389")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x14), scpexpr(EXPR_PUSH_LONG, 0x120), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_E54")

    #C0032
    ChrTalk(
        0x8,
        (
            "好了，玩笑话就先放到一边，\x01",
            "必须要赶快开始谈工作了。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x8,
        (
            "今天应该能收到那老头\x01",
            "的联络。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x8,
        (
            "嘻嘻……必须要提前\x01",
            "做好提货的准备啊。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xA, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_E4F")

    #C0035
    ChrTalk(
        0x101,
        "#0003F（在、在说什么啊。）\x02",
    )

    CloseMessageWindow()

    label("loc_E4F")

    Jump("loc_1384")

    label("loc_E54")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x30, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_FED")

    #C0036
    ChrTalk(
        0x8,
        (
            "#2P对了，说到人偶的话，\x01",
            "之前听到过奇怪的传言呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x8,
        (
            "#2P据说，在利贝尔发生异变之时，\x01",
            "有很多机械人偶擅自行动，\x01",
            "在各地造成了暴动……\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x8,
        (
            "#2P嘻嘻，说不定约鲁古\x01",
            "也插了一脚呢。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FE8")
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0039
    ChrTalk(
        0x103,
        "#0211F（话题太危险了，完全不好笑呢。）\x02",
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x101,
        (
            "#0006F（嗯……是那个『结社』\x01",
            "  曾经引发的事件啊。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_FE8")

    Jump("loc_1384")

    label("loc_FED")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x30, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_10E9")

    #C0041
    ChrTalk(
        0x8,
        (
            "对了对了，关于期限，\x01",
            "根据买方的情况，\x01",
            "今天已经是最后期限了。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x8,
        (
            "无论如何，也得\x01",
            "在今天之内取回哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x8,
        "万事拜托了！\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10E4")

    #C0044
    ChrTalk(
        0x101,
        "#0006F（难度越来越高了……）\x02",
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x102,
        (
            "#0100F（我们还有其它任务，要是不可能\x01",
            "  做到的话就放弃吧。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_10E4")

    Jump("loc_1384")

    label("loc_10E9")

    EventBegin(0x0)
    Fade(500)
    OP_68(-730, 1450, 2860, 0)
    MoveCamera(315, 22, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(23010, 0)
    SetChrPos(0x101, -250, 0, 2000, 0)
    SetChrPos(0x102, -1250, 0, 1750, 0)
    SetChrPos(0x103, -250, 0, 500, 0)
    SetChrPos(0x104, -1250, 0, 250, 0)
    OP_0D()

    #C0046
    ChrTalk(
        0x8,
        (
            "真是的，那个臭老头，\x01",
            "事到如今还在反复无常……\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x8,
        (
            "不过即使如此，现在再去拜托游击士\x01",
            "也已经来不及了……\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x8,
        (
            "……没办法。\x01",
            "只好去找其他买家了。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0049
    ChrTalk(
        0x8,
        "哎呀，是你们……\x02",
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x102,
        "#0100F您好，伊梅尔达夫人。\x02",
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x101,
        "#0000F发生了什么事吗？\x02",
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x8,
        (
            "没什么，我认识的一个别扭老头，\x01",
            "刚才说了些给人添麻烦的梦话……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x8)
    Sleep(1000)
    OP_63(0x8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0053
    ChrTalk(
        0x8,
        (
            "嘻嘻嘻，这也是\x01",
            "女神的安排吧！\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x8,
        "对了对了，就这么办吧！\x02",
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x101,
        "#0005F哎……\x02",
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x104,
        "#0306F不知为何，有种不好的预感……\x02",
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x103,
        (
            "#0200F……我认为不是预感，\x01",
            "而是真的呢。\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 22)
    ClearScenarioFlags(0xF1, 5)
    EventEnd(0x5)

    label("loc_1384")

    Jump("loc_39EA")

    label("loc_1389")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_170C")
    SetChrSubChip(0x8, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_144F")

    #C0058
    ChrTalk(
        0x8,
        (
            "（敲击键盘）……情报怎么还是\x01",
            "没有更新啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x8,
        (
            "警察磨磨蹭蹭的，到底在干什么啊。\x01",
            "真是的，快点去调查吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x101,
        (
            "#0003F（只因为觉得与自己无关，\x01",
            "  就说得这么轻松啊……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1707")

    label("loc_144F")

    SetChrName("")

    #A0061
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "伊梅尔达夫人在柜台下面\x01",
            "操作着类似终端装置的东西。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0062
    ChrTalk(
        0x8,
        "（敲击键盘）……\x02",
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x8,
        "什么，竟然袭击了黑月的分公司……！\x02",
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x8,
        (
            "嘻嘻……这可是个大事件呢。\x01",
            "好久没有这种热血沸腾的感觉了。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6C, 2)), scpexpr(EXPR_END)), "loc_153D")

    #C0065
    ChrTalk(
        0x103,
        "#0200F又是从约纳那里得来的情报吗……\x02",
    )

    CloseMessageWindow()

    label("loc_153D")

    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0066
    ChrTalk(
        0x8,
        (
            "只要住在克洛斯贝尔，\x01",
            "时不时就会遇到这样的事件呀。\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x8,
        (
            "嘻嘻……让人热血沸腾啊。\x01",
            "这下子，曹那边\x01",
            "会进行怎样的反击呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x102,
        (
            "#0106F老婆婆……\x01",
            "这样说实在是不太好吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x104,
        (
            "#0301F鲁巴彻商会就在这附近，\x01",
            "您难道都不害怕吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x8,
        "嗯，说得也是啊。\x02",
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x8,
        (
            "好担心这附近的地价\x01",
            "会不会下滑呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0072
    ChrTalk(
        0x101,
        (
            "#0006F（对了，这个人\x01",
            "  是靠炒地皮发家的啊……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1707")

    Jump("loc_39EA")

    label("loc_170C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_END)), "loc_1868")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_177D")

    #C0073
    ChrTalk(
        0x8,
        (
            "嘻嘻……我们这里\x01",
            "会营业到很晚呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x8,
        (
            "如果有什么想要的东西，\x01",
            "就来和我谈谈……如何？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1863")

    label("loc_177D")


    #C0075
    ChrTalk(
        0x8,
        (
            "……噢呀～\x01",
            "怎么露出一副如此疲惫的神情啊？\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x8,
        (
            "嘻嘻嘻嘻……\x01",
            "想买点什么吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0x8,
        (
            "买下这只壶的话，\x01",
            "就会精神满满，变得幸福哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0x101,
        (
            "#0006F啊，请不要强行推销\x01",
            "一些奇怪的东西。\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0x104,
        (
            "#0300F真是的，好一个擅长\x01",
            "趁虚而入的老婆婆啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1863")

    Jump("loc_39EA")

    label("loc_1868")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_1A64")
    SetChrSubChip(0x8, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_18EF")

    #C0080
    ChrTalk(
        0x8,
        (
            "呵呵，新型定期飞行船和\x01",
            "警备队的新型装甲车的构造图……\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0x8,
        (
            "真不愧是情报商，\x01",
            "挖到了不少好料嘛，嘻嘻……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A5F")

    label("loc_18EF")

    SetChrName("")

    #A0082
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "伊梅尔达夫人在柜台下面\x01",
            "操作着类似终端装置的东西。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0083
    ChrTalk(
        0x8,
        "（敲击键盘）……\x02",
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x8,
        (
            "呵呵，新型定期飞行船和\x01",
            "警备队的新型装甲车的构造图……\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0x8,
        (
            "真不愧是情报商，\x01",
            "挖到了不少好料嘛，嘻嘻……\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x109,
        (
            "#0505F（怎、怎么回事，\x01",
            "  这位老婆婆……）\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x101,
        (
            "#0006F（嗯，好像正在与我们认识的\x01",
            "  一名情报商联系……）\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0x103,
        (
            "#0200F（话说回来，约纳还真是随心所欲地\x01",
            "  贩卖着情报啊……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1A5F")

    Jump("loc_39EA")

    label("loc_1A64")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_1FA4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB1, 5)), scpexpr(EXPR_END)), "loc_1B29")

    #C0089
    ChrTalk(
        0x8,
        (
            "原来如此……\x01",
            "我听说过不少传闻，\x01",
            "确实是个挺有趣的女孩啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x8,
        (
            "嘻嘻……\x01",
            "小姑娘，欢迎再来玩啊，\x01",
            "我会好好陪你的。\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x153,
        "#1109F嗯，再见啦～！\x02",
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0x101,
        "#0000F（琪雅好厉害啊……）\x02",
    )

    CloseMessageWindow()
    Jump("loc_1F9F")

    label("loc_1B29")


    #C0093
    ChrTalk(
        0x8,
        (
            "哎呀～？\x01",
            "这不是支援科的小鬼们嘛。\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x8,
        (
            "嘻嘻嘻，还活着啊。\x01",
            "你们几个还真够顽强啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0x101,
        "#0012F您过奖了，哈哈……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1BE3")

    #C0096
    ChrTalk(
        0x102,
        (
            "#0100F说起来，伊梅尔达夫人\x01",
            "当时也在会场吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C68")

    label("loc_1BE3")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1C29")

    #C0097
    ChrTalk(
        0x103,
        (
            "#0200F说起来，伊梅尔达夫人\x01",
            "当时也在会场吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C68")

    label("loc_1C29")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1C68")

    #C0098
    ChrTalk(
        0x104,
        (
            "#0300F说起来，老婆婆\x01",
            "当时好像也在会场吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C68")


    #C0099
    ChrTalk(
        0x8,
        (
            "是啊，在那之后，\x01",
            "会场混乱成一团，真是太糟糕了。\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0x8,
        (
            "……哎？\x01",
            "那个可爱的小女孩，\x01",
            "难道就是当时那个……？\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0x8,
        "唔？嗯嗯……\x02",
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x153,
        (
            "#1111F（盯）……\x02\x03",

            "#1110F戴着眼镜的老奶奶，\x01",
            "脑袋好像魔女一样呢～\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0103
    ChrTalk(
        0x8,
        "……………………………………\x02",
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0x1, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(500)

    #C0104
    ChrTalk(
        0x101,
        (
            "#0011F那个……对不起。\x01",
            "她其实并没有什么恶意……\x02",
        )
    )

    CloseMessageWindow()
    OP_64(0x0)
    OP_64(0x1)
    OP_82(0xC8, 0x0, 0xBB8, 0x190)

    #C0105
    ChrTalk(
        0x8,
        "#4S嘻嘻嘻嘻嘻嘻……！\x02",
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0x8,
        "原来如此，的确是个很有趣的小女孩呢！\x02",
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0x8,
        (
            "小姑娘，我很喜欢你，\x01",
            "以后再来玩吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0x8,
        "我会好好陪你的。\x02",
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0x153,
        (
            "#1109F嗯，好啊，老奶奶。\x01",
            "琪雅还会再来的～！\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1F0B")

    #C0110
    ChrTalk(
        0x102,
        (
            "#0106F（……小琪雅\x01",
            "  还真是天不怕地不怕啊……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F9C")

    label("loc_1F0B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1F53")

    #C0111
    ChrTalk(
        0x103,
        (
            "#0200F（……琪雅还真是\x01",
            "  天不怕地不怕呢……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F9C")

    label("loc_1F53")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1F9C")

    #C0112
    ChrTalk(
        0x104,
        (
            "#0300F（哈哈……真不愧是阿琪，\x01",
            "  天不怕地不怕啊。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F9C")

    SetScenarioFlags(0xB1, 5)

    label("loc_1F9F")

    Jump("loc_39EA")

    label("loc_1FA4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_2018")

    #C0113
    ChrTalk(
        0x8,
        "哎呀，是你们啊。\x02",
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0x8,
        (
            "嘻嘻嘻……要是想买东西的话，\x01",
            "就快点买吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0x8,
        (
            "我今天准备在\x01",
            "傍晚时外出呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_39EA")

    label("loc_2018")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_21CB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_209D")

    #C0116
    ChrTalk(
        0x8,
        (
            "对了，你订的玩偶\x01",
            "已经进货了。\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0x8,
        (
            "我会仔细包好的，\x01",
            "回去的时候就顺便过来拿吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0x160,
        "#3300F呵呵，我会的。\x02",
    )

    CloseMessageWindow()
    Jump("loc_21C6")

    label("loc_209D")


    #C0119
    ChrTalk(
        0x8,
        (
            "哎呀，玲。\x01",
            "有段时间没见了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0x8,
        "怎么，你和那小鬼在一起啊？\x02",
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0x160,
        (
            "#3304F是啊，他好像遇到什么麻烦了，\x01",
            "所以我准备帮帮忙。\x02\x03",

            "#3300F向不可靠的软弱男性伸出援手，\x01",
            "也是一个杰出女性应尽的义务啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0x8,
        "哈哈哈哈，说的很好！\x02",
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0x8,
        (
            "你这小鬼，可不要给\x01",
            "玲添太多麻烦哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0x101,
        "#0006F真、真是说不过她们……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_21C6")

    Jump("loc_39EA")

    label("loc_21CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_236E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 3)), scpexpr(EXPR_END)), "loc_2256")

    #C0125
    ChrTalk(
        0x8,
        (
            "我不知道大街上发生了什么事，\x01",
            "但至少能肯定，那孩子没有来过我们店里。\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0x8,
        (
            "我们这里也不是小孩子\x01",
            "会感兴趣的店呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2369")

    label("loc_2256")


    #C0127
    ChrTalk(
        0x101,
        (
            "#0001F（嗯，这个人\x01",
            "  可能知道些什么吧……）\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    #A0128
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "罗伊德出示了柯林的照片，\x01",
            "并询问对方是否有什么线索。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0129
    ChrTalk(
        0x8,
        (
            "嗯，我不知道呢，\x01",
            "至少他没有来过我的店里。\x02",
        )
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0x8,
        (
            "嘻嘻嘻……\x01",
            "因为我这里并不是\x01",
            "小孩子会来的店呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0x101,
        (
            "#0003F是这样吗……\x01",
            "十分感谢您的帮助。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xAB, 3)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 14)

    label("loc_2369")

    Jump("loc_39EA")

    label("loc_236E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_2402")

    #C0132
    ChrTalk(
        0x8,
        (
            "哎呀呀，没想到会有客人\x01",
            "光临本店。\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0x8,
        (
            "今天我得去\x01",
            "很多地方呢。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xA, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_23FD")

    #C0134
    ChrTalk(
        0x102,
        (
            "#0100F伊梅尔达夫人……\x01",
            "好像不是那么想\x01",
            "做生意呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_23FD")

    Jump("loc_39EA")

    label("loc_2402")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_2609")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_2455")

    #C0135
    ChrTalk(
        0x8,
        (
            "今天被叫来叫去的呢。\x01",
            "嘻嘻……想买东西的话，\x01",
            "就快点啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2604")

    label("loc_2455")


    #C0136
    ChrTalk(
        0x8,
        (
            "克洛斯贝尔工商协会那边的人\x01",
            "叫我今天过去。\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0x8,
        "因为我过去和他们有过一点交情。\x02",
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0x8,
        (
            "嘻嘻……晚上\x01",
            "准备参加彩虹剧团\x01",
            "的庆功会呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0x101,
        "#0005F彩虹剧团的庆功会……？\x02",
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0x8,
        (
            "哈哈哈，\x01",
            "干嘛露出那种惊讶的表情啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0x8,
        (
            "……这是很正常的吧？\x01",
            "因为我也是出资者之一啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0142
    ChrTalk(
        0x102,
        "#0105F是、是这样吗……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xA, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2601")

    #C0143
    ChrTalk(
        0x104,
        "#0306F真不愧是老婆婆啊……\x02",
    )

    CloseMessageWindow()

    label("loc_2601")

    SetScenarioFlags(0x0, 0)

    label("loc_2604")

    Jump("loc_39EA")

    label("loc_2609")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_280D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_268F")

    #C0144
    ChrTalk(
        0x8,
        (
            "你们几个，要是弄坏我的公寓，\x01",
            "我可不会轻易饶过你们哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0x104,
        "#0303F（这个……现在大概最好还是别说什么了。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_2808")

    label("loc_268F")


    #C0146
    ChrTalk(
        0x8,
        (
            "明明是阻止了暗杀市长事件\x01",
            "的大功臣，\x01",
            "竟然还去旧城区玩那种游戏啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0x8,
        (
            "你们没有弄坏我的\x01",
            "公寓吧？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xA, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_277F")

    #C0148
    ChrTalk(
        0x101,
        (
            "#0011F没、没有啦……\x01",
            "我想应该是没有吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0x104,
        (
            "#0300F当然啦，连一个手指印都没有留下！\x01",
            "（………………虽然这是说谎。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2805")

    label("loc_277F")


    #C0150
    ChrTalk(
        0x101,
        (
            "#0011F公、公寓？\x01",
            "（这个人竟然还拥有那种东西吗……）\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0x104,
        (
            "#0300F当然啦，连一个手指印都没有留下！\x01",
            "（………………虽然我也不确定。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2805")

    SetScenarioFlags(0x0, 0)

    label("loc_2808")

    Jump("loc_39EA")

    label("loc_280D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_291E")

    #C0152
    ChrTalk(
        0x8,
        "今天被叫去参加聚会了。\x02",
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0x8,
        (
            "嘻嘻嘻……\x01",
            "得赶快化化妆，准备出门啦。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xA, 0x0, 0x10)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2916")

    #C0154
    ChrTalk(
        0x101,
        (
            "#0000F（……伊梅尔达夫人，\x01",
            "  人缘可真广啊，有些意外呢。）\x02",
        )
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0x102,
        (
            "#0100F（嗯，她也算是克洛斯贝尔的\x01",
            "  名流之一了……）\x02",
        )
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0x104,
        "#0306F（虽然是个靠炒地皮发家的老太婆呢。）\x02",
    )

    CloseMessageWindow()

    label("loc_2916")

    SetScenarioFlags(0x0, 0)
    Jump("loc_39EA")

    label("loc_291E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_2A38")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_293B")
    Call(0, 7)
    Jump("loc_2A33")

    label("loc_293B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x95, 7)), scpexpr(EXPR_END)), "loc_294C")
    Call(0, 7)
    Jump("loc_2A33")

    label("loc_294C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x1, 0x6)"), scpexpr(EXPR_END)), "loc_2A30")

    #C0157
    ChrTalk(
        0x8,
        (
            "那个狐狸脸，\x01",
            "昨天挺晚的时候来过。\x02",
        )
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0x8,
        (
            "说什么小金库被老婆发现了，\x01",
            "请原谅我吧之类的……\x02",
        )
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0x8,
        (
            "一个人在那边自言自语地抱怨了半天之后，\x01",
            "说是要再去喝一杯，然后就走掉了。\x02",
        )
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0x8,
        (
            "哈哈哈……\x01",
            "之后的事情我就不知道了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A33")

    label("loc_2A30")

    Call(0, 7)

    label("loc_2A33")

    Jump("loc_39EA")

    label("loc_2A38")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_2B56")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2A55")
    Call(0, 8)
    Jump("loc_2B51")

    label("loc_2A55")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x95, 7)), scpexpr(EXPR_END)), "loc_2A66")
    Call(0, 8)
    Jump("loc_2B51")

    label("loc_2A66")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x1, 0x6)"), scpexpr(EXPR_END)), "loc_2B4E")

    #C0161
    ChrTalk(
        0x8,
        (
            "那个狐狸脸啊，\x01",
            "他昨天挺晚的时候来过。\x02",
        )
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0x8,
        (
            "说什么小金库被老婆发现了，\x01",
            "请原谅我吧之类的……\x02",
        )
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0x8,
        (
            "一个人在那边自言自语地抱怨了半天之后，\x01",
            "说是要再去喝一杯，然后就走掉了。\x02",
        )
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0x8,
        (
            "哈哈哈……\x01",
            "之后的事情我就不知道了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B51")

    label("loc_2B4E")

    Call(0, 8)

    label("loc_2B51")

    Jump("loc_39EA")

    label("loc_2B56")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_2CDB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_2BE3")

    #C0165
    ChrTalk(
        0x8,
        (
            "说起来，又得跟那个别扭的老头\x01",
            "进行交涉了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0x8,
        (
            "哎呀呀，每次都要\x01",
            "给我添麻烦啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0x101,
        "#0005F（在说什么呢……？）\x02",
    )

    CloseMessageWindow()
    Jump("loc_2CD6")

    label("loc_2BE3")


    #C0168
    ChrTalk(
        0x8,
        (
            "你们跟\x01",
            "玲认识吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0x8,
        (
            "哈哈哈，\x01",
            "真是个很有趣的偶然呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0x101,
        (
            "#0005F那个……\x01",
            "您也和她认识吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0x8,
        (
            "那女孩暂住在一个我\x01",
            "认识的别扭老头的工房。\x02",
        )
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0x8,
        (
            "好像并不是那老头的孙女，\x01",
            "但很受他的宠爱呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0x8,
        (
            "她的眼光也很不错，\x01",
            "是个挺有品位的常客呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_2CD6")

    Jump("loc_39EA")

    label("loc_2CDB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_2DA4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_2D2F")

    #C0174
    ChrTalk(
        0x8,
        (
            "稍后去确认一下土地产权吧，\x01",
            "管理土地也得花上不少工夫呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D9F")

    label("loc_2D2F")


    #C0175
    ChrTalk(
        0x8,
        (
            "顺路去ＩＢＣ一趟，\x01",
            "确认一下土地产权吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0x8,
        (
            "嘻嘻……我在市内拥有\x01",
            "数十处土地呢，\x01",
            "管理方面也是很辛苦的。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_2D9F")

    Jump("loc_39EA")

    label("loc_2DA4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_309D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_2E61")

    #C0177
    ChrTalk(
        0x8,
        "你们几个，难道是导力盲吗？\x02",
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0x8,
        (
            "唉，这么年轻却如此落伍，\x01",
            "真让人担心你们的将来啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0x101,
        (
            "#0006F（应该说……是这么大年纪还能熟练操作\x01",
            "  导力装置的您太厉害了吧……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3098")

    label("loc_2E61")


    #C0180
    ChrTalk(
        0x8,
        (
            "今天傍晚得去\x01",
            "ＩＢＣ一趟。\x02",
        )
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0x8,
        (
            "淘到了一件刚出土的古董，\x01",
            "我得去汇款。\x02",
        )
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0x8,
        (
            "哎呀呀……导力网络要是\x01",
            "正式运营起来，也就不用\x01",
            "一趟趟地特意往银行跑了。\x02",
        )
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0x101,
        (
            "#0005F？？？\x01",
            "……什么意思呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0x103,
        (
            "#0203F也就是说，通过导力终端装置\x01",
            "连接到ＩＢＣ的账户，\x01",
            "在线就能完成转账手续。\x02\x03",

            "#0200F银行机能的数据化和普及化……\x01",
            "这正是ＩＢＣ推进导力网络事业\x01",
            "的最大好处。\x02\x03",

            "不过，要想完全实现，\x01",
            "恐怕还要花上不少时间。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x104)

    #C0185
    ChrTalk(
        0x101,
        (
            "#0006F抱歉，缇欧。\x01",
            "我完全听不懂呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0x104,
        "#0306F我也听不懂……\x02",
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0x102,
        (
            "#0106F我、我算是\x01",
            "听懂了一个大概……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_3098")

    Jump("loc_39EA")

    label("loc_309D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_3251")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xA, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_3183")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_30C3")
    Call(0, 9)
    Jump("loc_317E")

    label("loc_30C3")


    #C0188
    ChrTalk(
        0x8,
        (
            "公寓的钥匙暂时就先寄存在\x01",
            "你们那里吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0x8,
        (
            "嘻嘻，什么时候有空的话，\x01",
            "就进去帮我打扫打扫吧！\x02",
        )
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0x101,
        (
            "#0003F（看来以后还要和这位老婆婆\x01",
            "  继续打交道呢。\x01",
            "  ……不如为何，总有这种感觉。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_317E")

    Jump("loc_324C")

    label("loc_3183")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xA, 0x1, 0x1)"), scpexpr(EXPR_END)), "loc_3234")

    #C0191
    ChrTalk(
        0x8,
        (
            "有魔兽骚乱的公寓\x01",
            "是旧城区的『伊梅尔达馆』。\x02",
        )
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0x8,
        "总之，去了就知道啦。\x02",
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0x8,
        (
            "帮我把那些魔兽一只不剩地解决吧。\x01",
            "嘻嘻……拜托你们啦，\x01",
            "特别任务支援科的小鬼们。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_324C")

    label("loc_3234")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xA, 0x1, 0x0)"), scpexpr(EXPR_END)), "loc_3249")
    Call(0, 16)
    Jump("loc_324C")

    label("loc_3249")

    Call(0, 9)

    label("loc_324C")

    Jump("loc_39EA")

    label("loc_3251")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_34E3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6C, 3)), scpexpr(EXPR_END)), "loc_32D8")

    #C0194
    ChrTalk(
        0x8,
        (
            "利贝尔王室代代相传的，\x01",
            "刻有白隼图案的戒指……\x02",
        )
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0x8,
        (
            "嘻嘻嘻，凭你们这些小鬼的\x01",
            "微薄月薪，恐怕永远也买不起吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_34DE")

    label("loc_32D8")


    #C0196
    ChrTalk(
        0x8,
        (
            "哈哈哈……\x01",
            "今天进到了好东西哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0x8,
        (
            "刻着白隼图案，\x01",
            "用金耀石加工制成的戒指……\x02",
        )
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0x8,
        (
            "这可是利贝尔王室代代相传的宝物，\x01",
            "在数年前，从一位放荡的公爵\x01",
            "手中流落到了民间。\x02",
        )
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0x103,
        (
            "#0200F（利贝尔王室代代相传的宝物……\x01",
            "  倒卖这种东西\x01",
            "  真的没问题吗？）\x02",
        )
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0x102,
        (
            "#0105F（处理不好的话，可能会发展成\x01",
            "  外交问题呢……）\x02",
        )
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0x101,
        (
            "#0003F（嗯……不过，在确认\x01",
            "  那件东西是真货之前，\x01",
            "  什么都无法断言呢。）\x02",
        )
    )

    CloseMessageWindow()

    #C0202
    ChrTalk(
        0x8,
        (
            "哈哈哈……\x01",
            "要是想调查这枚戒指的话，\x01",
            "你们先花钱买下来吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0203
    ChrTalk(
        0x8,
        (
            "不过，这个可是很贵的哦。\x01",
            "工艺精致，使用的还是\x01",
            "品质上乘的金耀石呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x6C, 3)

    label("loc_34DE")

    Jump("loc_39EA")

    label("loc_34E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_37B1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6C, 2)), scpexpr(EXPR_END)), "loc_353F")

    #C0204
    ChrTalk(
        0x8,
        "哈哈哈……你们几个可真是有趣。\x02",
    )

    CloseMessageWindow()

    #C0205
    ChrTalk(
        0x8,
        (
            "我以后也会继续\x01",
            "关注你们的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_37AC")

    label("loc_353F")


    #C0206
    ChrTalk(
        0x8,
        "你们前些天表现得真不错呢。\x02",
    )

    CloseMessageWindow()

    #C0207
    ChrTalk(
        0x8,
        (
            "协助完成了圣书会首领的计划，\x01",
            "还去充当诱饵。\x01",
            "嘻嘻，很了不起嘛。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0208
    ChrTalk(
        0x101,
        "#0005F哎……？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x48, 1)), scpexpr(EXPR_END)), "loc_3654")

    #C0209
    ChrTalk(
        0x102,
        (
            "#0105F那件事……\x01",
            "应该并没有刊登在\x01",
            "克洛斯贝尔时代周刊上才对……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_368F")

    label("loc_3654")


    #C0210
    ChrTalk(
        0x102,
        (
            "#0105F格蕾丝小姐……\x01",
            "难道把那种事情都写到报道里了吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_368F")


    #C0211
    ChrTalk(
        0x8,
        (
            "哈哈哈……这有什么可奇怪的。\x01",
            "我认识一个情报商。\x02",
        )
    )

    CloseMessageWindow()

    #C0212
    ChrTalk(
        0x8,
        (
            "只要给他些米拉，\x01",
            "就能了解到大部分情况。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0213
    ChrTalk(
        0x103,
        "#0200F情报商吗……\x02",
    )

    CloseMessageWindow()

    #C0214
    ChrTalk(
        0x104,
        (
            "#0300F真不愧是克洛斯贝尔，\x01",
            "还有人在做这种奇怪的买卖啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x6C, 2)

    label("loc_37AC")

    Jump("loc_39EA")

    label("loc_37B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_3918")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F, 1)), scpexpr(EXPR_END)), "loc_37F9")

    #C0215
    ChrTalk(
        0x8,
        (
            "看中了什么东西吗？\x01",
            "特别任务支援科的小鬼们。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3913")

    label("loc_37F9")


    #C0216
    ChrTalk(
        0x8,
        (
            "看中了什么东西吗？\x01",
            "特别任务支援科的小鬼们。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0217
    ChrTalk(
        0x101,
        "#0005F哎……？\x02",
    )

    CloseMessageWindow()

    #C0218
    ChrTalk(
        0x104,
        (
            "#0305F喂喂，老婆婆。\x01",
            "您怎么会知道我们的身份呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0219
    ChrTalk(
        0x8,
        (
            "哈哈哈……\x01",
            "因为在这条后巷里，\x01",
            "汇集着各种情报啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0220
    ChrTalk(
        0x8,
        "你们几个就好好加油吧。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x4F, 1)

    label("loc_3913")

    Jump("loc_39EA")

    label("loc_3918")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_396F")

    #C0221
    ChrTalk(
        0x8,
        "哈哈哈，欢迎光临。\x02",
    )

    CloseMessageWindow()

    #C0222
    ChrTalk(
        0x8,
        (
            "本店经营各种古董，\x01",
            "有兴趣的话就随便看看吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_39EA")

    label("loc_396F")


    #C0223
    ChrTalk(
        0x8,
        "哈哈哈，欢迎光临。\x02",
    )

    CloseMessageWindow()

    #C0224
    ChrTalk(
        0x8,
        (
            "本店经营各种古董，\x01",
            "请随便看看吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0x101,
        (
            "#0003F（这、这家店，\x01",
            "  总觉得有种奇怪的气氛呢……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_39EA")

    Jump("loc_6CC")

    label("loc_39EF")

    SetChrSubChip(0x8, 0x0)
    TalkEnd(0x8)
    Return()

    # Function_4_490 end

    def Function_5_39F7(): pass

    label("Function_5_39F7")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0x8)
    ClearChrFlags(0x8, 0x10)
    TurnDirection(0x8, 0x0, 0)
    OP_52(0x8, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3A8B")
    Jump("loc_3AD5")

    label("loc_3A8B")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3AAB")
    OP_52(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3AD5")

    label("loc_3AAB")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3ACB")
    OP_52(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3AD5")

    label("loc_3ACB")

    OP_52(0x8, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3AD5")

    OP_52(0x8, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x8, 0x10)

    #C0226
    ChrTalk(
        0x8,
        "（盯）……\x02",
    )

    CloseMessageWindow()

    #C0227
    ChrTalk(
        0x101,
        (
            "#0003F对、对不起，\x01",
            "我们现在有点事。\x02",
        )
    )

    CloseMessageWindow()

    #C0228
    ChrTalk(
        0x102,
        (
            "#0106F那个……\x01",
            "该怎么道歉才好呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0229
    ChrTalk(
        0x8,
        (
            "……算啦，\x01",
            "你们看起来好像也挺忙的。\x02",
        )
    )

    CloseMessageWindow()

    #C0230
    ChrTalk(
        0x8,
        (
            "嘻嘻……\x01",
            "另外，最近认识了跟原来那些倒卖者\x01",
            "不同的新客户呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0x8,
        (
            "花起钱来也大方多了，\x01",
            "哈，真算是不幸中的大幸了。\x02",
        )
    )

    CloseMessageWindow()

    #C0232
    ChrTalk(
        0x101,
        "#0005F是这样吗……\x02",
    )

    CloseMessageWindow()

    #C0233
    ChrTalk(
        0x102,
        "#0100F听到这些，我们也安心了。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0xD3, 3)
    SetChrSubChip(0x8, 0x0)
    TalkEnd(0x8)
    Return()

    # Function_5_39F7 end

    def Function_6_3C3F(): pass

    label("Function_6_3C3F")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0x8)
    ClearChrFlags(0x8, 0x10)
    TurnDirection(0x8, 0x0, 0)
    OP_52(0x8, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3CD3")
    Jump("loc_3D1D")

    label("loc_3CD3")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3CF3")
    OP_52(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3D1D")

    label("loc_3CF3")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3D13")
    OP_52(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3D1D")

    label("loc_3D13")

    OP_52(0x8, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3D1D")

    OP_52(0x8, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x8, 0x10)

    #C0234
    ChrTalk(
        0x8,
        "哎呀，这不是特别任务支援科的小鬼们吗？\x02",
    )

    CloseMessageWindow()

    #C0235
    ChrTalk(
        0x8,
        (
            "对了对了……\x01",
            "你们当时做到一半就扔下不管的\x01",
            "那个『伊梅尔达馆』委托啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0236
    ChrTalk(
        0x8,
        (
            "后来交给游击士去处理了，\x01",
            "他们轻轻松松就解决了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0237
    ChrTalk(
        0x8,
        (
            "哈哈哈，果然和某些人不同，\x01",
            "真是很可靠啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0238
    ChrTalk(
        0x101,
        (
            "#0000F……那个，真是\x01",
            "非常抱歉。\x02",
        )
    )

    CloseMessageWindow()

    #C0239
    ChrTalk(
        0x104,
        (
            "#0306F（感觉会被她\x01",
            "  抱怨到下辈子呢……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x93, 4)
    SetChrSubChip(0x8, 0x0)
    TalkEnd(0x8)
    Return()

    # Function_6_3C3F end

    def Function_7_3EE0(): pass

    label("Function_7_3EE0")

    SetChrSubChip(0x8, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_3F35")

    #C0240
    ChrTalk(
        0x8,
        (
            "『银』与特别任务支援科的对决……\x01",
            "哇哈哈哈，这还真令人期待啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4063")

    label("loc_3F35")

    SetChrName("")

    #A0241
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "伊梅尔达夫人在柜台下面\x01",
            "操作着类似终端装置的东西。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0242
    ChrTalk(
        0x8,
        "（敲击键盘）……\x02",
    )

    CloseMessageWindow()

    #C0243
    ChrTalk(
        0x8,
        (
            "哎呀，从情报商那边\x01",
            "发来了新情报呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0244
    ChrTalk(
        0x8,
        (
            "『银』与特别任务支援科的对决……？\x01",
            "这新闻可真奇怪呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0245
    ChrTalk(
        0x101,
        (
            "#0001F（约纳……为什么要把这种情报\x01",
            "  流传给外人知道啊……！）\x02",
        )
    )

    CloseMessageWindow()

    #C0246
    ChrTalk(
        0x103,
        "#0203F（……果然有必要给他一点警告才行。）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_4063")

    Return()

    # Function_7_3EE0 end

    def Function_8_4064(): pass

    label("Function_8_4064")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_40B6")

    #C0247
    ChrTalk(
        0x8,
        (
            "好像频繁有警察进出\x01",
            "彩虹剧场呢。\x01",
            "嘻嘻……这个情报要重点关注啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_428A")

    label("loc_40B6")


    #C0248
    ChrTalk(
        0x8,
        "从我掌握的情报来看……\x02",
    )

    CloseMessageWindow()

    #C0249
    ChrTalk(
        0x8,
        (
            "似乎有警察在频繁进出\x01",
            "彩虹剧场呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0250
    ChrTalk(
        0x8,
        (
            "在这个新剧即将公演的时期，\x01",
            "难道又要出现丑闻了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0251
    ChrTalk(
        0x8,
        (
            "真是的，好不容易编排的新剧，\x01",
            "希望不要半途流产啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0252
    ChrTalk(
        0x101,
        (
            "#0003F（看、看样子，部分情报\x01",
            "  好像已经流传出去了……）\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6C, 2)), scpexpr(EXPR_END)), "loc_4240")

    #C0253
    ChrTalk(
        0x104,
        (
            "#0306F（是那些情报商干的吗……\x01",
            "  不知已经流传到什么程度了。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4287")

    label("loc_4240")


    #C0254
    ChrTalk(
        0x104,
        (
            "#0300F（算了，看起来也只不过是一些\x01",
            "  让人不明真伪的消息而已……）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4287")

    SetScenarioFlags(0x0, 0)

    label("loc_428A")

    Return()

    # Function_8_4064 end

    def Function_9_428B(): pass

    label("Function_9_428B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_4328")

    #C0255
    ChrTalk(
        0x8,
        (
            "嘻嘻嘻……\x01",
            "我都已经活了七十年，\x01",
            "但还是没有在这座城市住厌呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0256
    ChrTalk(
        0x8,
        (
            "最近，我都从一个新情报商那里\x01",
            "直接购买情报呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0257
    ChrTalk(
        0x8,
        "每天都看得很开心啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_4620")

    label("loc_4328")


    #C0258
    ChrTalk(
        0x8,
        (
            "说起来，警备队\x01",
            "似乎已经放弃了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0259
    ChrTalk(
        0x8,
        (
            "真是丢脸啊。\x01",
            "不是还没有把那些狼形魔兽\x01",
            "消灭掉吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0260
    ChrTalk(
        0x103,
        (
            "#0205F……这应该还是\x01",
            "机密情报才对……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6C, 2)), scpexpr(EXPR_END)), "loc_4496")

    #C0261
    ChrTalk(
        0x101,
        (
            "#0003F（似乎是从情报商之类的人手里\x01",
            "  买到的消息呢。）\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xA, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_4456")

    #C0262
    ChrTalk(
        0x104,
        (
            "#0306F（不仅是个大地产商，而且还是个顺风耳……\x01",
            "  真是个不可小瞧的婆婆呢。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4491")

    label("loc_4456")


    #C0263
    ChrTalk(
        0x104,
        (
            "#0303F（天生的好奇心吗……\x01",
            "  真是个恶趣味的婆婆啊。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4491")

    Jump("loc_461D")

    label("loc_4496")


    #C0264
    ChrTalk(
        0x8,
        (
            "哈哈哈……这也没什么奇怪啦。\x01",
            "因为我认识一个情报商。\x02",
        )
    )

    CloseMessageWindow()

    #C0265
    ChrTalk(
        0x8,
        (
            "只要给他些米拉，\x01",
            "大部分的消息都能了解到。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0266
    ChrTalk(
        0x101,
        "#0003F情报商……吗。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xA, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_45DD")

    #C0267
    ChrTalk(
        0x104,
        (
            "#0306F（不仅是个大地产商，而且还是个顺风耳……\x01",
            "  真是个不可小瞧的婆婆呢。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_461A")

    label("loc_45DD")


    #C0268
    ChrTalk(
        0x104,
        (
            "#0300F真不愧是克洛斯贝尔。\x01",
            "还有人在做这种奇怪的买卖啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_461A")

    SetScenarioFlags(0x6C, 2)

    label("loc_461D")

    SetScenarioFlags(0x0, 0)

    label("loc_4620")

    Return()

    # Function_9_428B end

    def Function_10_4621(): pass

    label("Function_10_4621")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xEF, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4711")

    #C0269
    ChrTalk(
        0x8,
        (
            "哎呀，你们好像\x01",
            "收集到了全套的\x01",
            "《黑市医生格伦》呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0270
    ChrTalk(
        0x8,
        (
            "嗯……我本来也很想收集的，\x01",
            "但稍一疏忽，\x01",
            "就有几本漏买了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0271
    ChrTalk(
        0x8,
        "怎么样，我们来谈谈吧。\x02",
    )

    CloseMessageWindow()

    #C0272
    ChrTalk(
        0x8,
        (
            "我用这里的稀有宝贝来交换\x01",
            "你们手中的全套《黑市医生格伦》，\x01",
            "意下如何？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xEF, 6)
    Jump("loc_4773")

    label("loc_4711")


    #C0273
    ChrTalk(
        0x8,
        (
            "你们收集到了全套\x01",
            "《黑市医生格伦》啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0274
    ChrTalk(
        0x8,
        (
            "怎么样啊，要不要用它来交换\x01",
            "我这里的稀有宝贝呢？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4773")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【同意】\x01",      # 0
            "【拒绝】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_49A5")

    #C0275
    ChrTalk(
        0x8,
        (
            "嘻嘻嘻！\x01",
            "好，那我就收下啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0276
    ChrTalk(
        0x8,
        (
            "接下来，该轮到我拿出好东西了。\x01",
            "……给，把这个拿去吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0277
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '塞姆里亚石'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    SubItemNumber('黑市医生格伦　１卷', 1)
    SubItemNumber('黑市医生格伦　２卷', 1)
    SubItemNumber('黑市医生格伦　３卷', 1)
    SubItemNumber('黑市医生格伦　４卷', 1)
    SubItemNumber('黑市医生格伦　５卷', 1)
    SubItemNumber('黑市医生格伦　６卷', 1)
    SubItemNumber('黑市医生格伦　７卷', 1)
    SubItemNumber('黑市医生格伦　８卷', 1)
    SubItemNumber('黑市医生格伦　９卷', 1)
    SubItemNumber('黑市医生格伦　10卷', 1)
    SubItemNumber('黑市医生格伦　11卷', 1)
    SubItemNumber('黑市医生格伦　12卷', 1)
    SubItemNumber('黑市医生格伦　13卷', 1)
    SubItemNumber('黑市医生格伦　14卷', 1)
    AddItemNumber('塞姆里亚石', 1)
    SetScenarioFlags(0x9D, 6)

    #C0278
    ChrTalk(
        0x101,
        (
            "#0005F十、十分感谢。\x02\x03",

            "不过，这东西是……？\x02",
        )
    )

    CloseMessageWindow()

    #C0279
    ChrTalk(
        0x8,
        (
            "嘻嘻……这可是通过某个渠道买到的\x01",
            "稀有宝物哟。\x02",
        )
    )

    CloseMessageWindow()

    #C0280
    ChrTalk(
        0x8,
        (
            "据说是古代塞姆里亚文明\x01",
            "时期的遗物呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0281
    ChrTalk(
        0x8,
        (
            "由于质地极端坚硬，好像无论用什么方法\x01",
            "都无法进行加工呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0282
    ChrTalk(
        0x8,
        (
            "哈哈哈，不过拿着的话，\x01",
            "以后说不定就能派上什么用场呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4A21")

    label("loc_49A5")


    #C0283
    ChrTalk(
        0x8,
        "是吗，那真是太遗憾了……\x02",
    )

    CloseMessageWindow()

    #C0284
    ChrTalk(
        0x8,
        (
            "我再去旧书店碰碰运气吧。\x01",
            "都已经收集到这种地步了，无论如何\x01",
            "也想凑齐全套，一口气读完啊……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4A21")

    Return()

    # Function_10_4621 end

    def Function_11_4A22(): pass

    label("Function_11_4A22")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_4A9E")
    OP_63(0xA, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0285
    ChrTalk(
        0xA,
        "咦，十、百、千……\x02",
    )

    CloseMessageWindow()

    #C0286
    ChrTalk(
        0xA,
        (
            "这价格是不是\x01",
            "多了三个零呢，\x01",
            "……大概是我看错了吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4B1A")

    label("loc_4A9E")


    #C0287
    ChrTalk(
        0xA,
        (
            "哎，还有\x01",
            "这种店啊～\x02",
        )
    )

    CloseMessageWindow()

    #C0288
    ChrTalk(
        0xA,
        (
            "跟着游行队伍往回走，\x01",
            "没想到发现了这种店呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0289
    ChrTalk(
        0xA,
        (
            "嘻嘻嘻……买点什么\x01",
            "再回去吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xA, 0x5A, 0x0)
    SetChrFlags(0xA, 0x10)
    SetScenarioFlags(0x0, 2)

    label("loc_4B1A")

    TalkEnd(0xFE)
    Return()

    # Function_11_4A22 end

    def Function_12_4B1E(): pass

    label("Function_12_4B1E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x93, 0)), scpexpr(EXPR_END)), "loc_4B8D")

    #C0290
    ChrTalk(
        0x9,
        (
            "#3300F那位狼先生已经成为\x01",
            "大哥哥们的朋友了吧？\x02\x03",

            "#3309F下次见面时，\x01",
            "也把它正式介绍给玲吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4B90")

    label("loc_4B8D")

    Call(0, 13)

    label("loc_4B90")

    TalkEnd(0xFE)
    Return()

    # Function_12_4B1E end

    def Function_13_4B94(): pass

    label("Function_13_4B94")

    EventBegin(0x0)
    Fade(500)
    OP_68(-3250, 1450, 180, 0)
    MoveCamera(320, 25, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(20690, 0)
    SetChrPos(0x101, -2800, 0, 310, 270)
    SetChrPos(0x102, -2500, 0, 1400, 225)
    SetChrPos(0x103, -2550, 0, -960, 315)
    SetChrPos(0x104, -3500, 0, 1870, 180)
    SetChrSubChip(0x9, 0x0)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu03300.itp")
    OP_0D()
    OP_63(0x9, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x9, 0x101, 500)

    #C0291
    ChrTalk(
        0x9,
        "#3305F#5P哎呀……？\x02",
    )

    CloseMessageWindow()

    #C0292
    ChrTalk(
        0x103,
        "#0205F#6P你是……\x02",
    )

    CloseMessageWindow()

    #C0293
    ChrTalk(
        0x101,
        (
            "#0005F#12P啊……是人偶工房的那个小姑娘。\x02\x03",

            "#0000F好久不见了。\x01",
            "没记错的话，你好像是叫小玲吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0294
    AnonymousTalk(
        0x9,
        (
            "呵呵，有一个月没见了吧。\x02\x03",

            "不过，怎么可以这么不确定地\x01",
            "再次询问淑女的名字呢。\x02\x03",

            "牢记清楚，再会的时候\x01",
            "优雅地问候，才能算是合格的绅士吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)

    #C0295
    ChrTalk(
        0x101,
        "#0012F#12P哈哈，的确如此。\x02",
    )

    CloseMessageWindow()

    #C0296
    ChrTalk(
        0x104,
        "#0304F#11P还真是很严厉啊。\x02",
    )

    CloseMessageWindow()

    #C0297
    ChrTalk(
        0x102,
        (
            "#0102F#11P呵呵，你好像是一个人来的啊，\x01",
            "是乘巴士来玩的吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0298
    ChrTalk(
        0x9,
        (
            "#3304F#5P嗯，是的。\x02\x03",

            "#3300F我偶尔会一个人来这家\x01",
            "古董店玩玩。\x02\x03",

            "因为这里有时会陈列爷爷所做的人偶，\x01",
            "而且还会进一些\x01",
            "可爱的玩偶。\x02",
        )
    )

    CloseMessageWindow()

    #C0299
    ChrTalk(
        0x101,
        (
            "#0005F#12P哦，是这样啊。\x02\x03",

            "#0006F不过，小孩子孤身一人\x01",
            "在这附近走动，多少也有点……\x02",
        )
    )

    CloseMessageWindow()

    #C0300
    ChrTalk(
        0x9,
        (
            "#3304F#5P嘻嘻，\x01",
            "不会有什么危险啦。\x02\x03",

            "揽客的大哥哥\x01",
            "和陪酒的大姐姐都很和善……\x02\x03",

            "#3302F小巷里面戴着墨镜的叔叔们\x01",
            "也都是很有趣的人呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0301
    ChrTalk(
        0x101,
        "#0003F#12P唔，那个～……\x02",
    )

    CloseMessageWindow()

    #C0302
    ChrTalk(
        0x102,
        "#0108F#11P还是有点担心呢……\x02",
    )

    CloseMessageWindow()

    #C0303
    ChrTalk(
        0x9,
        (
            "#3304F#5P呵呵，对了──\x02\x03",

            "#3302F和狼先生玩捉迷藏，\x01",
            "好像挺有趣的吧？\x02\x03",

            "似乎还有很多特殊的客人\x01",
            "也加入其中了呢。\x02",
        )
    )

    CloseMessageWindow()
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

    #C0304
    ChrTalk(
        0x102,
        "#0105F#11P哎……\x02",
    )

    CloseMessageWindow()

    #C0305
    ChrTalk(
        0x101,
        (
            "#0011F#12P难道说……\x01",
            "你从克洛斯贝尔时代周刊的报道中\x01",
            "看出了这些信息吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0306
    ChrTalk(
        0x9,
        (
            "#3304F#5P呵呵，差不多吧。\x02\x03",

            "#3300F那位狼先生已经和大哥哥们\x01",
            "成为朋友了吧？\x02\x03",

            "#3309F下次见面的时候，\x01",
            "也把它正式介绍给玲吧？？\x02",
        )
    )

    CloseMessageWindow()

    #C0307
    ChrTalk(
        0x101,
        "#0002F#12P啊，好的。\x02",
    )

    CloseMessageWindow()

    #C0308
    ChrTalk(
        0x104,
        (
            "#0302F#11P（跟以前一样，\x01",
            "  还是个充满谜团的小姑娘呢。）\x02",
        )
    )

    CloseMessageWindow()

    #C0309
    ChrTalk(
        0x103,
        "#0200F#6P（……是啊。）\x02",
    )

    CloseMessageWindow()
    OP_5A()
    OP_CA(0x1, 0xFF, 0x0)
    SetChrPos(0x0, -2800, 0, 310, 270)
    OP_93(0x9, 0x10E, 0x0)
    ClearChrFlags(0x9, 0x10)
    SetScenarioFlags(0x93, 0)
    EventEnd(0x5)
    Return()

    # Function_13_4B94 end

    def Function_14_52B3(): pass

    label("Function_14_52B3")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5333")
    OP_29(0x46, 0x1, 0x4)

    #C0310
    ChrTalk(
        0x101,
        (
            "#0003F（好，在后巷的询问工作\x01",
            "  也差不多了。）\x02\x03",

            "#0001F（接下来，就去中央广场\x01",
            "  问问看吧。）\x02",
        )
    )

    CloseMessageWindow()
    OP_D0(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0xB9, 4)

    label("loc_5333")

    Return()

    # Function_14_52B3 end

    def Function_15_5334(): pass

    label("Function_15_5334")

    EventBegin(0x0)
    FadeToDark(500, 0, -1)
    OP_0D()
    LoadChrToIndex("chr/ch09000.itc", 0x1E)
    OP_68(-730, 1150, 2860, 0)
    MoveCamera(314, 24, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(24040, 0)
    SetChrPos(0x101, -250, 0, 2000, 0)
    SetChrPos(0x102, -1250, 0, 1750, 0)
    SetChrPos(0x103, -250, 0, 500, 0)
    SetChrPos(0x104, -1250, 0, 250, 0)
    FadeToBright(1000, 0)
    OP_0D()

    #C0311
    ChrTalk(
        0x8,
        "#11P哎呀，你们来了吗，『特别任务支援科』。\x02",
    )

    CloseMessageWindow()

    #C0312
    ChrTalk(
        0x101,
        (
            "#5P#0000F打扰了……\x01",
            "您就是\x01",
            "伊梅尔达夫人吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0313
    ChrTalk(
        0x8,
        (
            "#11P没错，\x01",
            "我就是伊梅尔达。\x02",
        )
    )

    CloseMessageWindow()

    #C0314
    ChrTalk(
        0x8,
        (
            "#11P嘻嘻，来了好多\x01",
            "年轻的小鬼呢。\x01",
            "……让我好好看看你们。\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    SetChrPos(0x8, -750, 0, 4600, 180)
    Sound(820, 0, 100, 0)
    OP_0D()
    SetChrName("")

    #A0315
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "伊梅尔达夫人站了起来，\x01",
            "盯着罗伊德等人仔细端详。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0316
    ChrTalk(
        0x101,
        "#5P#0005F（这、这人的脸好大啊……）\x02",
    )

    CloseMessageWindow()

    #C0317
    ChrTalk(
        0x102,
        (
            "#5P#0105F（好有冲击力的长相呢……）\x02\x03",

            "#0103F（说起『伊梅尔达夫人』，\x01",
            "  好像的确是克洛斯贝尔的\x01",
            "  名流之一呢……）\x02\x03",

            "#0100F那个，伊梅尔达夫人。\x01",
            "我们接到了委托，听说您名下的\x01",
            "公寓中有魔兽骚乱……\x02",
        )
    )

    CloseMessageWindow()

    #C0318
    ChrTalk(
        0x104,
        (
            "#6P#0305F说到公寓，应该就在市内吧。\x01",
            "那情况不是很紧急吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0319
    ChrTalk(
        0x8,
        (
            "#11P哈哈哈……\x01",
            "嗯，就是这么一回事啦。\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    SetChrPos(0x8, -750, 100, 4800, 180)
    Sound(820, 0, 100, 0)
    OP_0D()

    #C0320
    ChrTalk(
        0x103,
        "#6P#0200F（完全不觉得她有危机感呢……）\x02",
    )

    CloseMessageWindow()

    #C0321
    ChrTalk(
        0x104,
        (
            "#6P#0306F（似乎是个粗神经\x01",
            "  的婆婆啊……）\x02",
        )
    )

    CloseMessageWindow()

    #C0322
    ChrTalk(
        0x8,
        "#11P总之，你们肯接受吗？\x02",
    )

    CloseMessageWindow()
    OP_29(0xA, 0x1, 0x0)
    Call(0, 17)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_56F4")
    Call(0, 18)

    label("loc_56F4")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_D5(0x1E)
    OP_68(-750, 1450, 2000, 0)
    MoveCamera(315, 26, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25500, 0)
    SetChrPos(0x0, -750, 0, 2000, 0)
    SetChrPos(0x1, -750, 0, 2000, 0)
    SetChrPos(0x2, -750, 0, 2000, 0)
    SetChrPos(0x3, -750, 0, 2000, 0)
    FadeToBright(500, 0)
    OP_0D()
    EventEnd(0x5)
    Return()

    # Function_15_5334 end

    def Function_16_5780(): pass

    label("Function_16_5780")

    EventBegin(0x0)
    Fade(500)
    OP_68(-730, 1450, 2860, 0)
    MoveCamera(315, 22, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(23010, 0)
    SetChrPos(0x101, -250, 0, 2000, 0)
    SetChrPos(0x102, -1250, 0, 1750, 0)
    SetChrPos(0x103, -250, 0, 500, 0)
    SetChrPos(0x104, -1250, 0, 250, 0)
    OP_0D()

    #C0323
    ChrTalk(
        0x8,
        (
            "#11P我名下的公寓里似乎\x01",
            "有魔兽在作乱呢 。\x01",
            "想拜托你们这些小鬼帮我驱除。\x02",
        )
    )

    CloseMessageWindow()

    #C0324
    ChrTalk(
        0x8,
        "#11P嘻嘻……你们肯接受吗？\x02",
    )

    CloseMessageWindow()
    Call(0, 17)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_587A")
    Call(0, 18)

    label("loc_587A")

    SetChrPos(0x0, -750, 0, 2000, 0)
    EventEnd(0x5)
    Return()

    # Function_16_5780 end

    def Function_17_588E(): pass

    label("Function_17_588E")

    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【接受】\x01",      # 0
            "【拒绝】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_59E5")

    #C0325
    ChrTalk(
        0x101,
        (
            "#5P#0006F现在不太方便呢……\x01",
            "工作太忙了。\x02",
        )
    )

    CloseMessageWindow()

    #C0326
    ChrTalk(
        0x8,
        (
            "#11P嘻嘻……是吗。\x01",
            "那就拜托你们尽快了。\x02",
        )
    )

    CloseMessageWindow()

    #C0327
    ChrTalk(
        0x8,
        (
            "#11P要是太慢的话，我就转交给\x01",
            "协会那边的人啦。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0328
    ChrTalk(
        0x101,
        "#5P#0003F我、我们会尽力的……\x02",
    )

    CloseMessageWindow()

    label("loc_59E5")

    Return()

    # Function_17_588E end

    def Function_18_59E6(): pass

    label("Function_18_59E6")


    #C0329
    ChrTalk(
        0x8,
        (
            "#11P嘻嘻嘻，那我就\x01",
            "开始说说工作的事情吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0330
    ChrTalk(
        0x101,
        "#5P#0000F好的，拜托您了。\x02",
    )

    CloseMessageWindow()

    #C0331
    ChrTalk(
        0x8,
        (
            "#11P我在市内\x01",
            "拥有多处土地。\x02",
        )
    )

    CloseMessageWindow()

    #C0332
    ChrTalk(
        0x8,
        (
            "#11P如今发生问题的公寓\x01",
            "『伊梅尔达馆』也是其中之一。\x02",
        )
    )

    CloseMessageWindow()

    #C0333
    ChrTalk(
        0x8,
        (
            "#11P地点在旧城区，\x01",
            "大概是在稍微靠里一点的地方。\x02",
        )
    )

    CloseMessageWindow()

    #C0334
    ChrTalk(
        0x102,
        "#5P#0105F是在旧城区吗……\x02",
    )

    CloseMessageWindow()

    #C0335
    ChrTalk(
        0x104,
        (
            "#6P#0303F那里的环境的确十分混乱，\x01",
            "要是一直弃之不管，\x01",
            "似乎确实会有魔兽出没啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0336
    ChrTalk(
        0x8,
        (
            "#11P是啊，那些魔兽\x01",
            "确实会在不知不觉间\x01",
            "就冒出来呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0337
    ChrTalk(
        0x8,
        (
            "#11P要是再不赶快解决干净的话，\x01",
            "恐怕连一周都坚持不了了。\x02",
        )
    )

    CloseMessageWindow()

    #C0338
    ChrTalk(
        0x8,
        (
            "#11P小鬼们，我想拜托你们的\x01",
            "就是清除那些魔兽。\x01",
            "一只不留地解决干净吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0339
    ChrTalk(
        0x101,
        (
            "#5P#0001F我知道了，\x01",
            "把魔兽都解决掉就行了吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0340
    ChrTalk(
        0x103,
        (
            "#6P#0200F放着不管的话，后果会很危险的，\x01",
            "我们快点去把它们消灭掉吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0341
    ChrTalk(
        0x8,
        (
            "#11P那么，\x01",
            "把这个交给你们吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0342
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x33C),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x33C, 1)

    #C0343
    ChrTalk(
        0x101,
        "#5P#0000F嗯，那我们就暂时借用一下。\x02",
    )

    CloseMessageWindow()

    #C0344
    ChrTalk(
        0x102,
        (
            "#5P#0100F那么，我们立刻出发，\x01",
            "前往旧城区吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    Sound(80, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0345
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "任务【驱除废旧公寓的魔兽】\x07\x00",
            "开始！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_29(0xA, 0x1, 0x1)
    Return()

    # Function_18_59E6 end

    def Function_19_5D94(): pass

    label("Function_19_5D94")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-730, 1150, 2860, 0)
    MoveCamera(314, 24, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(24040, 0)
    SetChrPos(0x101, -250, 0, 2000, 0)
    SetChrPos(0x102, -1250, 0, 1750, 0)
    SetChrPos(0x103, -250, 0, 500, 0)
    SetChrPos(0x104, -1250, 0, 250, 0)
    FadeToBright(1000, 0)
    OP_0D()

    #C0346
    ChrTalk(
        0x8,
        "#11P噢，原来是这么一回事吗……\x02",
    )

    CloseMessageWindow()

    #C0347
    ChrTalk(
        0x8,
        (
            "#11P嘻嘻嘻，特别任务支援科。\x01",
            "你们挺能干的嘛。\x02",
        )
    )

    CloseMessageWindow()

    #C0348
    ChrTalk(
        0x8,
        (
            "#11P虽然手法让人难以恭维，\x01",
            "但至少也算是把事情解决了。\x02",
        )
    )

    CloseMessageWindow()

    #C0349
    ChrTalk(
        0x101,
        "#5P#0006F呼，多谢夸奖……\x02",
    )

    CloseMessageWindow()

    #C0350
    ChrTalk(
        0x104,
        (
            "#6P#0301F不过，真没想到魔兽\x01",
            "出没的面积竟然都那么大了……\x01",
            "到底有多少年没管了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0351
    ChrTalk(
        0x103,
        (
            "#6P#0203F是啊。\x01",
            "就算是为了保证安全，\x01",
            "也应该定时进行基本管理。\x02",
        )
    )

    CloseMessageWindow()

    #C0352
    ChrTalk(
        0x102,
        (
            "#5P#0100F不过，这样一来，\x01",
            "那间公寓就可以正常出租了啊。\x02\x03",

            "只要住进了人，魔兽也就不会\x01",
            "再跑到那里面驻窝了……\x02",
        )
    )

    CloseMessageWindow()

    #C0353
    ChrTalk(
        0x8,
        (
            "#11P嗯，是啊。\x01",
            "不过，还是过几年\x01",
            "再考虑出租的事情吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0354
    ChrTalk(
        0x102,
        "#5P#0105F哎……？\x02",
    )

    CloseMessageWindow()

    #C0355
    ChrTalk(
        0x8,
        (
            "#11P因为旧城区的房租很便宜嘛，\x01",
            "等地价稍微上涨一些之后再出租，\x01",
            "这样就能获得更多的利润了。\x02",
        )
    )

    CloseMessageWindow()

    #C0356
    ChrTalk(
        0x8,
        (
            "#11P嘻嘻……跟土地有关的事情，\x01",
            "听我的准没错。\x02",
        )
    )

    CloseMessageWindow()

    #C0357
    ChrTalk(
        0x8,
        (
            "#11P我可是伊梅尔达，\x01",
            "克洛斯贝尔\x01",
            "数一数二的大地产商啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0358
    ChrTalk(
        0x8,
        (
            "#11P旧城区的破旧公寓只是小意思罢了，\x01",
            "等到经济状况好转，地价上涨之后，\x01",
            "我要同时周转市内的几十处土地呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0359
    ChrTalk(
        0x101,
        (
            "#5P#0000F这、这就是平时常说的……\x01",
            "……炒地皮吗？\x02\x03",

            "#0006F（难道那才是她的主业吗？）\x02",
        )
    )

    CloseMessageWindow()

    #C0360
    ChrTalk(
        0x102,
        (
            "#5P#0103F（『伊梅尔达夫人』……\x01",
            "  在克洛斯贝尔的社交界中，\x01",
            "  也算是个知名度很高的名人呢。）\x02\x03",

            "#0100F（原来就听说她是个资本家……）\x02",
        )
    )

    CloseMessageWindow()

    #C0361
    ChrTalk(
        0x104,
        (
            "#6P#0300F（哈哈，所以才会有这种\x01",
            "  非同等闲的气质啊……）\x02",
        )
    )

    CloseMessageWindow()

    #C0362
    ChrTalk(
        0x8,
        (
            "#11P不过，要是放着空地不管的话，\x01",
            "以后也许还会有魔兽来作乱的，\x01",
            "看来有必要进行定期的扫除呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0363
    ChrTalk(
        0x8,
        (
            "#11P啊……对了，\x01",
            "公寓的钥匙暂时就\x01",
            "放在你们那里好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0364
    ChrTalk(
        0x8,
        (
            "#11P嘻嘻，什么时候有空的话，\x01",
            "就进去帮我打扫一下吧！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0365
    ChrTalk(
        0x103,
        "#6P#0200F（好一个会指使人的老婆婆啊。）\x02",
    )

    CloseMessageWindow()

    #C0366
    ChrTalk(
        0x101,
        (
            "#5P#0006F（我们差不多也该去继续工作了吧。\x01",
            "  这次真是非常累人啊……）\x02",
        )
    )

    CloseMessageWindow()

    #C0367
    ChrTalk(
        0x102,
        "#5P#0106F（嗯，是啊……）\x02",
    )

    CloseMessageWindow()
    OP_5A()
    FadeToDark(300, 0, 100)
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0368
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "任务【驱除废旧公寓的魔兽】\x07\x00",
            "完成！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    SetChrPos(0x0, -750, 0, 2000, 0)
    OP_29(0xA, 0x1, 0x7)
    OP_29(0xA, 0x4, 0x10)
    EventEnd(0x5)
    Return()

    # Function_19_5D94 end

    def Function_20_6520(): pass

    label("Function_20_6520")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-750, 1450, -2000, 0)
    MoveCamera(315, 22, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(23010, 0)
    SetChrPos(0x101, -250, 0, -1250, 0)
    SetChrPos(0x103, -1250, 0, -1250, 0)
    SetChrPos(0x11C, -750, 0, -3000, 0)
    FadeToBright(1000, 0)
    OP_0D()

    #C0369
    ChrTalk(
        0x11C,
        "#6P#1200F呜噜噜噜噜……\x02",
    )

    CloseMessageWindow()

    #C0370
    ChrTalk(
        0x103,
        (
            "#5P#0200F似乎在这间店内\x01",
            "留有气味。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xA, 0x1, 0x1)"), scpexpr(EXPR_END)), "loc_6629")

    #C0371
    ChrTalk(
        0x101,
        (
            "#11P#0003F去问问伊梅尔达夫人吧，\x01",
            "她说不定知道些什么。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_665E")

    label("loc_6629")


    #C0372
    ChrTalk(
        0x101,
        (
            "#11P#0003F去问一下店主吧，\x01",
            "她可能会知道些什么。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_665E")

    OP_68(-730, 1450, 2860, 3000)

    def lambda_6674():
        OP_97(0x101, 0x0, 0x0, 0xCB2, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6674)
    Sleep(50)

    def lambda_6691():
        OP_97(0x103, 0x0, 0x0, 0xCB2, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_6691)
    Sleep(50)

    def lambda_66AE():
        OP_97(0x11C, 0x0, 0x0, 0xCB2, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x11C, 1, lambda_66AE)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x11C, 1)

    #C0373
    ChrTalk(
        0x101,
        (
            "#6P#0000F那个，打扰一下，\x01",
            "想向您打听一点事情……\x02",
        )
    )

    CloseMessageWindow()

    #C0374
    ChrTalk(
        0x8,
        (
            "#11P哎呀！\x01",
            "这不是特别任务支援科吗。\x02",
        )
    )

    CloseMessageWindow()

    #C0375
    ChrTalk(
        0x8,
        (
            "#11P哈哈，你们终于被\x01",
            "警察局开除了吗？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xA, 0x1, 0x1)"), scpexpr(EXPR_END)), "loc_678E")

    #C0376
    ChrTalk(
        0x101,
        "#6P#0006F为什么会这么说啊……\x02",
    )

    CloseMessageWindow()
    Jump("loc_67CF")

    label("loc_678E")


    #C0377
    ChrTalk(
        0x101,
        (
            "#6P#0006F您、您在说什么啊。\x01",
            "（真是个奇怪的\x01",
            "  老婆婆啊……）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_67CF")


    #C0378
    ChrTalk(
        0x101,
        (
            "#6P#0001F我们想向您打听一点事情，\x01",
            "请问，昨天有没有\x01",
            "一位喝醉的客人来过这里？\x02\x03",

            "#0003F他好像在这附近\x01",
            "丢失了什么东西……\x02",
        )
    )

    CloseMessageWindow()

    #C0379
    ChrTalk(
        0x8,
        "#11P哦，是在说那个狐狸脸的男人吗。\x02",
    )

    CloseMessageWindow()

    #C0380
    ChrTalk(
        0x8,
        (
            "#11P这么说来，\x01",
            "他进来的时候，\x01",
            "全身都散发着难闻的酒气。\x02",
        )
    )

    CloseMessageWindow()

    #C0381
    ChrTalk(
        0x8,
        (
            "#11P说什么小金库被老婆发现了，\x01",
            "请原谅我吧之类的……\x02",
        )
    )

    CloseMessageWindow()

    #C0382
    ChrTalk(
        0x8,
        (
            "#11P唠唠叨叨地抱怨了一通之后，\x01",
            "说要再去喝一杯，然后就走掉了。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0383
    ChrTalk(
        0x101,
        "#6P#0006F该、该怎么说才好呢……\x02",
    )

    CloseMessageWindow()

    #C0384
    ChrTalk(
        0x103,
        (
            "#6P#0200F这可真是给您\x01",
            "添麻烦了。\x02",
        )
    )

    CloseMessageWindow()

    #C0385
    ChrTalk(
        0x8,
        (
            "#11P嘻嘻，确实如此。\x01",
            "替我告诉他，下次再来的时候，\x01",
            "买点宝石之类的东西吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0386
    ChrTalk(
        0x101,
        (
            "#6P#0003F（要是找不到结婚戒指的话，\x01",
            "  也许还真的要买了……）\x02\x03",

            "#0000F我知道了，\x01",
            "感谢您的协助。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x103, 0xE1, 0x1F4)
    Sleep(500)
    OP_93(0x103, 0x87, 0x1F4)
    Sleep(500)
    TurnDirection(0x103, 0x101, 500)

    #C0387
    ChrTalk(
        0x103,
        (
            "#6P#0203F看起来，戒指似乎并没有\x01",
            "掉落在这间店里呢。\x02\x03",

            "#0200F……再稍微\x01",
            "找一下好了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 500)

    #C0388
    ChrTalk(
        0x101,
        "#12P#0000F嗯，好的。\x02",
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, -750, 0, 2000, 0)
    OP_29(0x15, 0x1, 0x6)
    EventEnd(0x5)
    Return()

    # Function_20_6520 end

    def Function_21_6B06(): pass

    label("Function_21_6B06")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-430, 1450, 4410, 0)
    MoveCamera(315, 27, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(19970, 0)
    SetChrPos(0x101, -250, 0, -1750, 0)
    SetChrPos(0x102, -1250, 0, -2000, 0)
    SetChrPos(0x103, -250, 0, -3250, 0)
    SetChrPos(0x104, -1250, 0, -3500, 0)
    FadeToBright(1000, 0)
    OP_0D()
    SetChrName("")

    #A0389
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "伊梅尔达夫人正在使用\x01",
            "柜台下的通讯器进行通话。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(200)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0390
    ChrTalk(
        0x8,
        (
            "#11P你说什么！？\x01",
            "不是开玩笑吧！\x02",
        )
    )

    CloseMessageWindow()

    #C0391
    ChrTalk(
        0x8,
        (
            "#11P我这边都已经\x01",
            "找到买家了啊！\x02",
        )
    )

    CloseMessageWindow()

    #C0392
    ChrTalk(
        0x8,
        (
            "#11P不是已经做完了吗！？\x01",
            "那就快点送来吧！\x02",
        )
    )

    CloseMessageWindow()

    #C0393
    ChrTalk(
        0x8,
        "#11P…………………………………\x02",
    )

    CloseMessageWindow()
    Sleep(200)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0394
    ChrTalk(
        0x8,
        (
            "#11P可恶！\x01",
            "那个死老头，居然挂掉了！\x02",
        )
    )

    CloseMessageWindow()
    OP_68(-10, 1350, 1330, 3000)
    MoveCamera(317, 17, 0, 3000)
    SetCameraDistance(21890, 3000)

    def lambda_6CE0():
        OP_97(0x101, 0x0, 0x0, 0x8CA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6CE0)
    Sleep(50)

    def lambda_6CFD():
        OP_97(0x102, 0x0, 0x0, 0x8CA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6CFD)
    Sleep(50)

    def lambda_6D1A():
        OP_97(0x103, 0x0, 0x0, 0x8CA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_6D1A)
    Sleep(50)

    def lambda_6D37():
        OP_97(0x104, 0x0, 0x0, 0x8CA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_6D37)
    OP_6F(0x79)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    #C0395
    ChrTalk(
        0x102,
        "#6P#0100F您好，伊梅尔达夫人。\x02",
    )

    CloseMessageWindow()

    #C0396
    ChrTalk(
        0x101,
        "#6P#0005F发生什么事了吗？\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0397
    ChrTalk(
        0x8,
        "#11P哦，是你们啊。\x02",
    )

    CloseMessageWindow()

    #C0398
    ChrTalk(
        0x8,
        (
            "#11P没什么，我认识的一个别扭老头，\x01",
            "刚才说了些给人添麻烦的梦话……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x8)
    Sleep(1000)
    OP_63(0x8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0399
    ChrTalk(
        0x8,
        (
            "#11P嘻嘻嘻，这也是\x01",
            "女神的安排啊！\x02",
        )
    )

    CloseMessageWindow()

    #C0400
    ChrTalk(
        0x8,
        "#11P对了对了，就这么办吧！\x02",
    )

    CloseMessageWindow()

    #C0401
    ChrTalk(
        0x101,
        "#6P#0011F哎……\x02",
    )

    CloseMessageWindow()

    #C0402
    ChrTalk(
        0x104,
        "#6P#0306F不知为何，有种不好的预感……\x02",
    )

    CloseMessageWindow()

    #C0403
    ChrTalk(
        0x103,
        (
            "#6P#0211F……我认为不是预感，\x01",
            "而是真的呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0404
    ChrTalk(
        0x8,
        "#11P你们几个，现在有空吗？\x02",
    )

    CloseMessageWindow()
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0405
    ChrTalk(
        0x8,
        (
            "#11P是吗，有空啊！\x01",
            "哎呀，这可真是太好了。\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 22)
    EventEnd(0x5)
    Return()

    # Function_21_6B06 end

    def Function_22_6F78(): pass

    label("Function_22_6F78")


    #C0406
    ChrTalk(
        0x101,
        (
            "#6P#0012F那、那个，请等一下，\x01",
            "我们还有事要做呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0407
    ChrTalk(
        0x8,
        (
            "#11P哼，反正也不是什么\x01",
            "太着急的工作吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0408
    ChrTalk(
        0x8,
        (
            "#11P不然你们哪还有时间\x01",
            "来我这里闲晃啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0409
    ChrTalk(
        0x101,
        "#6P#0001F呜……说的好像也没错。\x02",
    )

    CloseMessageWindow()

    #C0410
    ChrTalk(
        0x102,
        (
            "#6P#0100F难道说……您要向\x01",
            "特别任务支援科提出委托吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0411
    ChrTalk(
        0x8,
        (
            "#11P真不愧是麦克道尔的孙女，\x01",
            "直觉很敏锐嘛。\x02",
        )
    )

    CloseMessageWindow()

    #C0412
    ChrTalk(
        0x8,
        (
            "#11P嘻嘻，当然了，我也准备了\x01",
            "很丰厚的报酬哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0413
    ChrTalk(
        0x101,
        (
            "#6P#0006F不不，重点并不是那种问题……\x02\x03",

            "#0000F……算了，也无所谓。\x01",
            "不管怎样，就先听听您的委托内容吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0414
    ChrTalk(
        0x8,
        "#11P嘻嘻，真是太好了。\x02",
    )

    CloseMessageWindow()

    #C0415
    ChrTalk(
        0x8,
        (
            "#11P想拜托你们的事情，\x01",
            "是『人偶』的提货和搬运。\x02",
        )
    )

    CloseMessageWindow()
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

    #C0416
    ChrTalk(
        0x101,
        "#6P#0005F哎……！？\x02",
    )

    CloseMessageWindow()

    #C0417
    ChrTalk(
        0x102,
        "#6P#0105F您说的人偶，难道是……\x02",
    )

    CloseMessageWindow()

    #C0418
    ChrTalk(
        0x8,
        (
            "#11P没错，就是位于北部山道尽头的\x01",
            "『罗赞贝尔克工房』制造的人偶。\x02",
        )
    )

    CloseMessageWindow()

    #C0419
    ChrTalk(
        0x8,
        (
            "#11P当然啦，肯定不会像之前的竞拍会那样，\x01",
            "把其它东西掉包进去。\x02",
        )
    )

    CloseMessageWindow()

    #C0420
    ChrTalk(
        0x8,
        (
            "#11P而是真真正正的、刚刚制造完成的\x01",
            "罗赞贝尔克工房的新作人偶哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0421
    ChrTalk(
        0x104,
        (
            "#6P#0305F喂喂，听说那种东西的价值\x01",
            "高达数十万米拉……\x02",
        )
    )

    CloseMessageWindow()

    #C0422
    ChrTalk(
        0x103,
        (
            "#6P#0203F是价格几乎相当于克洛斯贝尔市民\x01",
            "人均年收入的昂贵人偶呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0423
    ChrTalk(
        0x8,
        (
            "#11P是啊，我这里也负责\x01",
            "对那边的人偶进行\x01",
            "代售……\x02",
        )
    )

    CloseMessageWindow()

    #C0424
    ChrTalk(
        0x8,
        (
            "#11P但那间工房的主人是一个\x01",
            "不喜欢与人接触的别扭老头子！\x02",
        )
    )

    CloseMessageWindow()

    #C0425
    ChrTalk(
        0x8,
        (
            "#11P明明好不容易找到了\x01",
            "新作人偶的买家，\x01",
            "但他现在却开始闹别扭了！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1200)

    #C0426
    ChrTalk(
        0x101,
        (
            "#6P#0012F这个……我觉得\x01",
            "这种事情实在不是我们\x01",
            "可以解决的……\x02",
        )
    )

    CloseMessageWindow()

    #C0427
    ChrTalk(
        0x102,
        (
            "#6P#0106F如果只是负责搬运的话，\x01",
            "倒还好说……\x02",
        )
    )

    CloseMessageWindow()

    #C0428
    ChrTalk(
        0x103,
        (
            "#6P#0200F不过，那间工房的主人\x01",
            "为什么要突然拒绝出售呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0429
    ChrTalk(
        0x8,
        (
            "#11P嗯，其实是买家那边\x01",
            "稍微有点问题吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0430
    ChrTalk(
        0x8,
        (
            "#11P那个买家，好像经常\x01",
            "以不正当的高价倒卖艺术品，\x01",
            "是个风评很差的掮客。\x02",
        )
    )

    CloseMessageWindow()

    #C0431
    ChrTalk(
        0x8,
        (
            "#11P那个老头子似乎对\x01",
            "这一点非常不满。\x02",
        )
    )

    CloseMessageWindow()

    #C0432
    ChrTalk(
        0x102,
        (
            "#6P#0108F身为创作者，把自己的心血\x01",
            "卖给那种人，肯定会很不开心吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0433
    ChrTalk(
        0x104,
        (
            "#6P#0301F嗯……这件任务\x01",
            "的难度会不会太高了啊？\x02",
        )
    )

    CloseMessageWindow()

    #C0434
    ChrTalk(
        0x8,
        (
            "#11P这叫什么话，\x01",
            "年轻人怎么能这么没自信啊！\x02",
        )
    )

    CloseMessageWindow()

    #C0435
    ChrTalk(
        0x8,
        (
            "#11P别看我平时不说什么，\x01",
            "其实我可是很看好你们的。\x02",
        )
    )

    CloseMessageWindow()

    #C0436
    ChrTalk(
        0x8,
        (
            "#11P你们肯定能让那个\x01",
            "别扭的臭老头敞开心扉，\x01",
            "然后顺利拿到新作人偶！\x02",
        )
    )

    CloseMessageWindow()

    #C0437
    ChrTalk(
        0x101,
        (
            "#6P#0006F嗯、嗯……\x02\x03",

            "#0008F（……不过，人偶工房吗……\x01",
            "  正好也很在意玲的情况……）\x02\x03",

            "（而且，那里似乎和琪雅也存在着一定\x01",
            "  的关联……）\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    #C0438
    ChrTalk(
        0x101,
        (
            "#6P#0003F──我们手头还有其它任务，\x01",
            "无法做出百分之百成功的保证……\x02\x03",

            "#0000F如果这样也可以的话，\x01",
            "我们就接受这件委托了。\x02",
        )
    )

    CloseMessageWindow()

    #C0439
    ChrTalk(
        0x8,
        "#11P哎呀，真是的，当然没问题啦！\x02",
    )

    CloseMessageWindow()

    #C0440
    ChrTalk(
        0x8,
        (
            "#11P总之，一切都\x01",
            "交给你们啦！\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    Sound(80, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0441
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "任务【新作人偶的提货】\x07\x00",
            "开始！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    SetChrPos(0x0, -750, 0, 2000, 0)
    OP_29(0x30, 0x4, 0x2)
    Return()

    # Function_22_6F78 end

    def Function_23_78ED(): pass

    label("Function_23_78ED")

    EventBegin(0x1)
    OP_63(0x8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0442
    ChrTalk(
        0x8,
        (
            "哦哦！\x01",
            "这个箱子就是……\x02",
        )
    )

    CloseMessageWindow()

    #C0443
    ChrTalk(
        0x101,
        (
            "#0000F总之，约鲁古先生\x01",
            "把这个交给我们了。\x02",
        )
    )

    CloseMessageWindow()

    #C0444
    ChrTalk(
        0x102,
        "#0100F请您先确认一下吧。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(500)
    EventBegin(0x0)
    OP_68(200, 1350, 2420, 0)
    MoveCamera(317, 17, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(22800, 0)
    SetCameraDistance(20800, 3000)
    SetChrPos(0x101, -250, 0, 2000, 0)
    SetChrPos(0x102, -1250, 0, 1750, 0)
    SetChrPos(0x103, -250, 0, 500, 0)
    SetChrPos(0x104, -1250, 0, 250, 0)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)

    #C0445
    ChrTalk(
        0x8,
        (
            "#2P哈哈哈！\x01",
            "的确是约鲁古的新作品！\x02",
        )
    )

    CloseMessageWindow()

    #C0446
    ChrTalk(
        0x8,
        (
            "#2P你们太厉害了，\x01",
            "竟然真的说服了他啊！\x02",
        )
    )

    CloseMessageWindow()

    #C0447
    ChrTalk(
        0x104,
        (
            "#6P#0309F不，那个～与其说是说服，\x01",
            "倒不如说是我们用顽强的毅力打动了他吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0448
    ChrTalk(
        0x102,
        (
            "#6P#0104F不过……这可真是个完美的人偶啊，\x01",
            "一如既往地漂亮呢。\x02\x03",

            "#0102F我在朋友那里\x01",
            "也见过几个……\x02",
        )
    )

    CloseMessageWindow()

    #C0449
    ChrTalk(
        0x103,
        "#6P#0202F真是美得令人叹服呢……\x02",
    )

    CloseMessageWindow()

    #C0450
    ChrTalk(
        0x101,
        (
            "#6P#0004F的确称得上是艺术品啊……\x02\x03",

            "#0005F……不过，我本来还以为是和琪雅\x01",
            "差不多大小的呢。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB1, 5)), scpexpr(EXPR_END)), "loc_7C1B")

    #C0451
    ChrTalk(
        0x8,
        (
            "#2P琪雅？就是你们以前带到这里的\x01",
            "那个有趣的小姑娘吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0452
    ChrTalk(
        0x8,
        (
            "#2P确实也有和她差不多大小的\x01",
            "罗赞贝尔克人偶呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7C9F")

    label("loc_7C1B")


    #C0453
    ChrTalk(
        0x8,
        (
            "#2P琪雅？就是被人送到竞拍会的会场，\x01",
            "之后被你们解救并监护的那个孩子吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0454
    ChrTalk(
        0x8,
        (
            "#2P确实也有和小孩子差不多大小的\x01",
            "罗赞贝尔克人偶呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7C9F")


    #C0455
    ChrTalk(
        0x8,
        (
            "#2P但由于约鲁古很少制作，\x01",
            "所以市面上基本没有出售。\x02",
        )
    )

    CloseMessageWindow()

    #C0456
    ChrTalk(
        0x8,
        (
            "#2P正因如此，\x01",
            "才会有在竞拍会上\x01",
            "拍出天价的传闻……\x02",
        )
    )

    CloseMessageWindow()

    #C0457
    ChrTalk(
        0x102,
        (
            "#6P#0104F市面上的人偶，\x01",
            "大多数都是这种大小吧。\x02\x03",

            "#0100F在贝尔那里看到的人偶，\x01",
            "尺寸大概也和这个差不多。\x02",
        )
    )

    CloseMessageWindow()

    #C0458
    ChrTalk(
        0x101,
        (
            "#6P#0003F原来如此……\x02\x03",

            "#0001F……不过，伊梅尔达夫人。\x02\x03",

            "您知道由那个工房制作的\x01",
            "『其它人偶』吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0459
    ChrTalk(
        0x8,
        "#2P其它人偶？\x02",
    )

    CloseMessageWindow()

    #C0460
    ChrTalk(
        0x104,
        (
            "#6P#0306F该怎么说呢，大概就是那种\x01",
            "会自行活动的巨大人偶。\x02\x03",

            "#0301F有的外形看上去很像天使，有的脸很大。\x02",
        )
    )

    CloseMessageWindow()

    #C0461
    ChrTalk(
        0x8,
        (
            "#2P哦哦，你们说的是装设了齿轮的\x01",
            "自动人偶吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0462
    ChrTalk(
        0x8,
        (
            "#2P其实硬要说的话，\x01",
            "他好像更专于制造那种东西呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0463
    ChrTalk(
        0x8,
        (
            "#2P据说最近还进行了导力化改造，\x01",
            "使人偶的动作变得更为精准了。\x02",
        )
    )

    CloseMessageWindow()

    #C0464
    ChrTalk(
        0x102,
        "#6P#0105F您、您原来早就知道了吗？\x02",
    )

    CloseMessageWindow()

    #C0465
    ChrTalk(
        0x8,
        (
            "#2P这有什么好奇怪的……\x01",
            "连那个『彩虹剧团』\x01",
            "也用它们做舞台道具呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0466
    ChrTalk(
        0x8,
        (
            "#2P在这次的新剧中出现的持枪士兵，\x01",
            "应该就是他制造的自动人偶呢。\x02",
        )
    )

    CloseMessageWindow()
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
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0467
    ChrTalk(
        0x101,
        (
            "#6P#0011F哎！？\x01",
            "那些挥枪的人竟然是……\x02",
        )
    )

    CloseMessageWindow()

    #C0468
    ChrTalk(
        0x102,
        "#6P#0101F真的吗……！？\x02",
    )

    CloseMessageWindow()

    #C0469
    ChrTalk(
        0x8,
        (
            "#2P是啊，除此之外，\x01",
            "那些复杂的舞台装置几乎\x01",
            "都是由那个工房制造的。\x02",
        )
    )

    CloseMessageWindow()

    #C0470
    ChrTalk(
        0x8,
        (
            "#2P像照明啦、水位控制啦、\x01",
            "演员的飞天装置啦，等等。\x02",
        )
    )

    CloseMessageWindow()

    #C0471
    ChrTalk(
        0x8,
        (
            "#2P虽然这些并不为\x01",
            "世人所知。\x02",
        )
    )

    CloseMessageWindow()

    #C0472
    ChrTalk(
        0x104,
        "#6P#0305F真令人吃惊……\x02",
    )

    CloseMessageWindow()

    #C0473
    ChrTalk(
        0x103,
        (
            "#6P#0201F我也觉得那些舞台装置\x01",
            "的技术相当厉害……\x02\x03",

            "#0208F也就是说，那些天使和怪物\x01",
            "也都属于类似的机械装置……？\x02",
        )
    )

    CloseMessageWindow()

    #C0474
    ChrTalk(
        0x8,
        (
            "#2P嗯，那家伙虽然是个讨厌与人接触，\x01",
            "性格别扭，又充满谜团的怪老头……\x02",
        )
    )

    CloseMessageWindow()

    #C0475
    ChrTalk(
        0x8,
        (
            "#2P不过，既然他能偶尔做几个新人偶\x01",
            "送过来，让我多赚点钱，\x01",
            "我也就不想抱怨什么了。\x02",
        )
    )

    CloseMessageWindow()

    #C0476
    ChrTalk(
        0x8,
        (
            "#2P──你们也辛苦啦。\x01",
            "以后要是再有什么事，还要拜托你们啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0477
    ChrTalk(
        0x101,
        "#6P#0005F啊……好的。\x02",
    )

    CloseMessageWindow()

    #C0478
    ChrTalk(
        0x102,
        (
            "#6P#0100F那么……\x01",
            "我们就先告辞了。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0479
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "任务【新作人偶的提货】\x07\x00",
            "完成！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SubItemNumber(0x359, 1)
    OP_68(-750, 1450, 2000, 0)
    MoveCamera(315, 26, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25500, 0)
    SetChrPos(0x0, -750, 0, 2000, 0)
    SetChrPos(0x1, -750, 0, 2000, 0)
    SetChrPos(0x2, -750, 0, 2000, 0)
    SetChrPos(0x3, -750, 0, 2000, 0)
    OP_29(0x30, 0x1, 0x6)
    OP_29(0x30, 0x4, 0x10)
    FadeToBright(500, 0)
    OP_0D()
    EventEnd(0x5)
    Return()

    # Function_23_78ED end

    def Function_24_83BE(): pass

    label("Function_24_83BE")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_84D5")
    SetChrName("")

    #A0480
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "陈列着许多精巧的人偶。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x50, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_84D5")

    #C0481
    ChrTalk(
        0x101,
        (
            "#0005F咦，还摆放着\x01",
            "古典人偶呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0482
    ChrTalk(
        0x103,
        (
            "#0200F制作得好精巧呢。\x01",
            "简直就像是艺术品。\x02",
        )
    )

    CloseMessageWindow()

    #C0483
    ChrTalk(
        0x104,
        (
            "#0304F哈，好厉害啊。\x01",
            "不过，价格好像也相当不菲。\x02",
        )
    )

    CloseMessageWindow()

    #C0484
    ChrTalk(
        0x102,
        (
            "#0100F真不愧是古董店呢。\x02\x03",

            "#0103F（但是，似乎并不是\x01",
            "  『那种人偶』……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x50, 4)

    label("loc_84D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_875D")
    SetChrName("")

    #A0485
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "陈列着许多精巧的人偶。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x50, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_875D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x50, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8575")

    #C0486
    ChrTalk(
        0x101,
        (
            "#0000F唔，好精巧的\x01",
            "古典人偶……\x02\x03",

            "#0005F啊，难道是山道的那间\x01",
            "人偶工房制造的……？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_85C4")

    label("loc_8575")


    #C0487
    ChrTalk(
        0x101,
        (
            "#0000F精巧的古典人偶……\x02\x03",

            "#0005F啊，难道是山道的\x01",
            "那间人偶工房制造的……？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_85C4")


    #C0488
    ChrTalk(
        0x102,
        (
            "#0103F不，我认为这并不是\x01",
            "罗赞贝尔克工房的作品。\x02\x03",

            "#0100F因为那里的人偶更加厉害呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0489
    ChrTalk(
        0x104,
        (
            "#0300F哈……是这样啊。\x02\x03",

            "#0301F……说起来，大小姐，\x01",
            "你还真是相当熟悉啊。\x02\x03",

            "难道说，你也拥有这种东西吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0490
    ChrTalk(
        0x102,
        (
            "#0104F啊哈哈……我可没有啦，\x01",
            "不过我有个朋友很喜欢收集这些。\x02\x03",

            "#0100F拜其所赐，\x01",
            "我曾经见过好几个实物呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0491
    ChrTalk(
        0x103,
        (
            "#0200F原来如此。\x02\x03",

            "罗赞贝尔克工房的人偶吗……\x01",
            "听说好像制作得相当精美啊，\x01",
            "有机会的话，真想看看实物。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x50, 5)

    label("loc_875D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_87BC")
    SetChrName("")

    #A0492
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "陈列着许多精巧的人偶。\x02\x03",

            "虽然价格不菲，\x01",
            "但似乎并不是罗赞贝尔克工房制造的。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_87BC")

    TalkEnd(0xFF)
    Return()

    # Function_24_83BE end

    SaveToFile()

Try(main)
