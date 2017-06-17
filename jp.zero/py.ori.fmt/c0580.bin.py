from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "イメルダ夫人",           # 1
        "レン",                   # 2
        "見物客",                 # 3
        "人形",                   # 4
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
        "Function_5_3FB7",         # 05, 5
        "Function_6_4233",         # 06, 6
        "Function_7_44DC",         # 07, 7
        "Function_8_4660",         # 08, 8
        "Function_9_48B9",         # 09, 9
        "Function_10_4C73",        # 0A, 10
        "Function_11_50CA",        # 0B, 11
        "Function_12_51EC",        # 0C, 12
        "Function_13_5276",        # 0D, 13
        "Function_14_5A3D",        # 0E, 14
        "Function_15_5ACC",        # 0F, 15
        "Function_16_5F6A",        # 10, 16
        "Function_17_608F",        # 11, 17
        "Function_18_6201",        # 12, 18
        "Function_19_65D7",        # 13, 19
        "Function_20_6D89",        # 14, 20
        "Function_21_73F5",        # 15, 21
        "Function_22_78C7",        # 16, 22
        "Function_23_82F0",        # 17, 23
        "Function_24_8E8B",        # 18, 24
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
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x2C6, 0x0)"), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x2C7, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x2C8, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x2C9, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x2CA, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x2CB, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x2CC, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x2CD, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x2CE, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x2CF, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x2D0, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x2D1, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x2D2, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x2D3, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9D, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xEF, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6C2")
    Call(0, 10)
    SetChrSubChip(0x8, 0x0)
    TalkEnd(0x8)
    Return()

    label("loc_6C2")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6CC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3FAF")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_72A")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_72A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_75A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_749")
    OP_AF(0x44)
    Jump("loc_74B")

    label("loc_749")

    OP_AF(0x43)

    label("loc_74B")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3FAA")

    label("loc_75A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_76E")
    Jump("loc_3FAA")

    label("loc_76E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3FAA")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_AC9")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x2C6, 0x0)"), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x2C7, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x2C8, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x2C9, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x2CA, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x2CB, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x2CC, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x2CD, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x2CE, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x2CF, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x2D0, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x2D1, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x2D2, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x2D3, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9D, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7F6")
    Call(0, 10)
    Jump("loc_AC4")

    label("loc_7F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xED, 7)), scpexpr(EXPR_END)), "loc_874")

    #C0001
    ChrTalk(
        0x8,
        (
            "ギルド共々、坊やたちには\x01",
            "せいぜい気張ってもらおうか。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x8,
        (
            "このワケの分からない\x01",
            "事態の収拾のためにもねぇ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AC4")

    label("loc_874")


    #C0003
    ChrTalk(
        0x8,
        (
            "そういや、マルコーニたちが\x01",
            "姿を消したんだってねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x8,
        "一体何が起こってるんだい？\x02",
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x101,
        "#0003Fやはりご存知でしたか……\x02",
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x104,
        (
            "#0306Fま、こんだけ近けりゃ\x01",
            "情報くらいは入ってくるか。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x8,
        (
            "当然さ。\x01",
            "だが肝心の状況については\x01",
            "曖昧なところが多すぎてねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x8,
        (
            "知り合いの議員や\x01",
            "警察の上の連中に聞いても\x01",
            "ロクな返事が返って来ないんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x102,
        "#0108Fそうでしたか……\x02",
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x103,
        (
            "#0203Fどうやら、どこも\x01",
            "混乱しているみたいですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x8,
        (
            "まあ、坊やたちには\x01",
            "せいぜい気張ってもらおうか。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x8,
        (
            "このワケの分からない\x01",
            "事態の収拾のためにもねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x101,
        "#0001F……ええ、勿論です。\x02",
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x102,
        "#0100F微力を尽くさせて頂きます。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0xED, 7)

    label("loc_AC4")

    Jump("loc_3FAA")

    label("loc_AC9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_D14")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_B8F")

    #C0015
    ChrTalk(
        0x8,
        (
            "どうにも妙な事に\x01",
            "なって来ているようだねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x8,
        (
            "日頃から税金を\x01",
            "たんまりと払っているんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x8,
        (
            "きっちり働いて\x01",
            "解決してくれないと困るよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x10A,
        "#0603F……承知しています。\x02",
    )

    CloseMessageWindow()
    Jump("loc_D0F")

    label("loc_B8F")


    #C0019
    ChrTalk(
        0x8,
        (
            "おや、坊やたち。\x01",
            "珍しいのを連れてるじゃないか。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x10A,
        (
            "#0603F……イメルダさん。\x01",
            "こいつらはあくまで\x01",
            "私の指揮下にあります。\x02\x03",

            "#0600F調子に乗らせるような事を\x01",
            "あまり言わないで頂きたい。\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x8,
        (
            "ヒヒャヒャ、アンタだって\x01",
            "同じケツの青いガキだろうに。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x8,
        "ナマ言ってるんじゃないよ。\x02",
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x10A,
        "#0601Fぐっ……\x02",
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x101,
        "#0000F（さ、さすがイメルダさん……）\x02",
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x103,
        "#0200F（一課のエースも形無しですね。）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_D0F")

    Jump("loc_3FAA")

    label("loc_D14")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_E75")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_D9E")

    #C0026
    ChrTalk(
        0x8,
        (
            "そういや、明け方、\x01",
            "ルバーチェの車が何台も\x01",
            "出て行ったみたいだねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x8,
        (
            "何かしら動きが\x01",
            "あったとは思うんだが。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E70")

    label("loc_D9E")


    #C0028
    ChrTalk(
        0x8,
        (
            "………………………………\x01",
            "しかし今日は妙に静かだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x8,
        (
            "黒月の報復も無いようだし、\x01",
            "一体どうなってるんだか。\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x101,
        "#0003F（確かにそうだな……）\x02",
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x104,
        (
            "#0301F（嵐の前のって訳じゃ\x01",
            "  なけりゃあいいんだが。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_E70")

    Jump("loc_3FAA")

    label("loc_E75")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_END)), "loc_1507")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x14), scpexpr(EXPR_PUSH_LONG, 0x120), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_F66")

    #C0032
    ChrTalk(
        0x8,
        (
            "さて、趣味もそこそこにして\x01",
            "仕事の話を進めておかないとねえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x8,
        (
            "今日はあのジジイから\x01",
            "連絡があるはずなんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x8,
        (
            "ヒヒ……受け取りの手筈を\x01",
            "整えておかないとね。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xA, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_F61")

    #C0035
    ChrTalk(
        0x101,
        "#0003F（な、何の話だろうな。）\x02",
    )

    CloseMessageWindow()

    label("loc_F61")

    Jump("loc_1502")

    label("loc_F66")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x30, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_110F")

    #C0036
    ChrTalk(
        0x8,
        (
            "#2Pそういや、人形といえば\x01",
            "前に変な噂があったねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x8,
        (
            "#2Pリベールの異変の時、\x01",
            "勝手に動く機械人形が\x01",
            "各地で暴れまわったとか……\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x8,
        (
            "#2Pヒヒ、案外ヨルグが一枚\x01",
            "噛んでいるかもしれないねぇ。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_110A")
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
        "#0211F（洒落になってませんね。）\x02",
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x101,
        (
            "#0006F（ああ……例の《結社》が\x01",
            "  起こしたって話だからな。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_110A")

    Jump("loc_1502")

    label("loc_110F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x30, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_1239")

    #C0041
    ChrTalk(
        0x8,
        (
            "そうそう、期限についてだが\x01",
            "買い手の都合で今日いっぱいが\x01",
            "デッドラインでね。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x8,
        (
            "何とか今日中に\x01",
            "受け取ってきて欲しいんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x8,
        "よろしく頼んだからね！\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1234")

    #C0044
    ChrTalk(
        0x101,
        "#0006F（またハードルが上がったな……）\x02",
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x102,
        (
            "#0100F（こちらも任務があるし、\x01",
            "  無理そうなら諦めましょう。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1234")

    Jump("loc_1502")

    label("loc_1239")

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
            "まったくあのジジイ、\x01",
            "今になってゴネるとは……\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x8,
        (
            "かといって遊撃士を頼るには\x01",
            "時間が足りなさそうだし……\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x8,
        (
            "……仕方ない。\x01",
            "他の顧客を見つけるしかないか。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0049
    ChrTalk(
        0x8,
        "おや、アンタたち……\x02",
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x102,
        "#0100Fこんにちは、イメルダさん。\x02",
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x101,
        "#0000F何かあったんですか？\x02",
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x8,
        (
            "いやね、知り合いの偏屈ジジイが\x01",
            "ふざけたことを言い出して……\x02",
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
            "ヒヒャヒャ、これも\x01",
            "女神の巡り合わせじゃないか！\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x8,
        "そうだそうだ、そうしよう！\x02",
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x101,
        "#0005Fへ……\x02",
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x104,
        "#0306Fなんかイヤな予感が……\x02",
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x103,
        (
            "#0200F……予感ではなく\x01",
            "確信だと思いますが。\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 22)
    ClearScenarioFlags(0xF1, 5)
    EventEnd(0x5)

    label("loc_1502")

    Jump("loc_3FAA")

    label("loc_1507")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_18D4")
    SetChrSubChip(0x8, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_15D9")

    #C0058
    ChrTalk(
        0x8,
        (
            "カタカタ……早く\x01",
            "新しい情報が入らないものかね。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x8,
        (
            "警察も何をモタモタやってるんだか。\x01",
            "さっさと捜査しないかい、まったく……\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x101,
        (
            "#0003F（他人事だと思って\x01",
            "  言いたい放題だ……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18CF")

    label("loc_15D9")

    SetChrName("")

    #A0061
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "夫人はカウンターの下で\x01",
            "端末らしきものを操作している。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0062
    ChrTalk(
        0x8,
        "カタカタ、カタタタタ……\x02",
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x8,
        "なんと、黒月の支社が襲撃……！\x02",
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x8,
        (
            "ヒヒ……こいつは一大事件だね。\x01",
            "久し振りに血が騒ぐじゃないかい。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6C, 2)), scpexpr(EXPR_END)), "loc_16D3")

    #C0065
    ChrTalk(
        0x103,
        "#0200Fまたヨナからの情報ですか……\x02",
    )

    CloseMessageWindow()

    label("loc_16D3")

    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0066
    ChrTalk(
        0x8,
        (
            "クロスベルに住んでいると\x01",
            "たまにこんな事件があるんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x8,
        (
            "クヒヒ……ゾクゾクするねぇ。\x01",
            "さてさてツァオの方は\x01",
            "どう反撃に出るのかねぇ……\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x102,
        (
            "#0106Fお婆さん……\x01",
            "さすがに不謹慎なのでは。\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x104,
        (
            "#0301Fルバーチェ商会の近くなんだし\x01",
            "ちっとは心配じゃねえのかよ？\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x8,
        "んー、そうだね。\x02",
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x8,
        (
            "この辺りの地価が\x01",
            "下がらないかは心配だね。\x02",
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
            "#0006F（そういやこの人、\x01",
            "  土地成金だったな……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_18CF")

    Jump("loc_3FAA")

    label("loc_18D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_END)), "loc_1A68")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_194B")

    #C0073
    ChrTalk(
        0x8,
        (
            "ヒヒ……うちは結構\x01",
            "遅くまで開けてるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x8,
        (
            "なにか欲しいなら\x01",
            "相談に乗るが……どうだい？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A63")

    label("loc_194B")


    #C0075
    ChrTalk(
        0x8,
        (
            "……おや～あ？\x01",
            "何だか疲れた顔をしてるじゃないか。\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x8,
        (
            "ヒヒャヒャ……\x01",
            "なにか買っていくかい？\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0x8,
        (
            "こっちの壷をもっていると\x01",
            "元気一杯、幸せになれるんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0x101,
        (
            "#0006Fあ、怪しげなものを\x01",
            "売りつけないでくださいよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0x104,
        (
            "#0300Fまったく、人の弱味に\x01",
            "付け込もうとする婆さんだな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1A63")

    Jump("loc_3FAA")

    label("loc_1A68")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_1CA6")
    SetChrSubChip(0x8, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1B09")

    #C0080
    ChrTalk(
        0x8,
        (
            "ほうほう、定期飛行船の新型に\x01",
            "警備隊の新型装甲車のスペック……\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0x8,
        (
            "さすが情報屋、いいネタを\x01",
            "仕入れてくるじゃないか、ヒャヒャ……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CA1")

    label("loc_1B09")

    SetChrName("")

    #A0082
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "夫人はカウンターの下で\x01",
            "端末らしきものを操作している。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0083
    ChrTalk(
        0x8,
        "カタカタ、カタタタタ……\x02",
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x8,
        (
            "ほうほう、定期飛行船の新型に\x01",
            "警備隊の新型装甲車のスペック……\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0x8,
        (
            "さすが情報屋、いいネタを\x01",
            "仕入れてくるじゃないか、ヒヒャヒャ！\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x109,
        (
            "#0505F（な、なんですか、\x01",
            "  このお婆さんは……）\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x101,
        (
            "#0006F（まあ、知り合いの\x01",
            "  情報通てところかな……）\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0x103,
        (
            "#0200F（しかしヨナも好き放題、\x01",
            "  情報を売っていますね……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1CA1")

    Jump("loc_3FAA")

    label("loc_1CA6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_227C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB1, 5)), scpexpr(EXPR_END)), "loc_1D8B")

    #C0089
    ChrTalk(
        0x8,
        (
            "なるほどねぇ……\x01",
            "色んな噂が飛び交ってるが、\x01",
            "確かに面白い娘だよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x8,
        (
            "ヒヒ……\x01",
            "お嬢ちゃん、また遊びにきな。\x01",
            "アタシが相手してあげよう。\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x153,
        "#1109Fうん、まったねー！\x02",
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0x101,
        "#0000F（キーアはすごいな……）\x02",
    )

    CloseMessageWindow()
    Jump("loc_2277")

    label("loc_1D8B")


    #C0093
    ChrTalk(
        0x8,
        (
            "おや～あ？\x01",
            "支援課の坊やじゃないかい。\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x8,
        (
            "ヒヒャヒャ、生きとったか。\x01",
            "あんたらもしぶといねえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0x101,
        "#0012Fいや、はは……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1E5B")

    #C0096
    ChrTalk(
        0x102,
        (
            "#0100Fそういえばイメルダさんも\x01",
            "会場に来られてましたね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1EF2")

    label("loc_1E5B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1EAB")

    #C0097
    ChrTalk(
        0x103,
        (
            "#0200Fそういえばイメルダさんも\x01",
            "会場で見かけましたね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1EF2")

    label("loc_1EAB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1EF2")

    #C0098
    ChrTalk(
        0x104,
        (
            "#0300Fそういや婆さんも\x01",
            "会場に来てたんだったよな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1EF2")


    #C0099
    ChrTalk(
        0x8,
        (
            "ああ、あの後、\x01",
            "会場は大騒ぎで大変だったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0x8,
        (
            "……でぇ？\x01",
            "そっちの可愛らしい娘が\x01",
            "例の子かね……？\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0x8,
        "ふむぅ？　……ふむふむぅ……\x02",
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x153,
        (
            "#1111Fじー……\x02\x03",

            "#1110Fメガネのおばーちゃん、\x01",
            "マジョみたいな頭してるねー。\x02",
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
            "#0011Fあの……すいません。\x01",
            "本人に悪気はないんですが……\x02",
        )
    )

    CloseMessageWindow()
    OP_64(0x0)
    OP_64(0x1)
    OP_82(0xC8, 0x0, 0xBB8, 0x190)

    #C0105
    ChrTalk(
        0x8,
        "#4Sヒヒャヒャヒャヒャ……！\x02",
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0x8,
        "なるほど、確かに面白い娘だねえ！\x02",
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0x8,
        (
            "お嬢ちゃん、気に入ったよ。\x01",
            "また遊びにきな。\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0x8,
        "アタシが相手してあげよう。\x02",
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0x153,
        (
            "#1109Fうん、おばーちゃん。\x01",
            "キーアまた来るねー！\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_21D3")

    #C0110
    ChrTalk(
        0x102,
        (
            "#0106F（……キーアちゃん、\x01",
            "  怖いもの知らずなのね……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2274")

    label("loc_21D3")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2225")

    #C0111
    ChrTalk(
        0x103,
        (
            "#0200F（……キーアは怖いもの\x01",
            "  知らずのようですね……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2274")

    label("loc_2225")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2274")

    #C0112
    ChrTalk(
        0x104,
        (
            "#0300F（はは……さすがキー坊。\x01",
            "  怖いもの知らずだなァ。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2274")

    SetScenarioFlags(0xB1, 5)

    label("loc_2277")

    Jump("loc_3FAA")

    label("loc_227C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_2306")

    #C0113
    ChrTalk(
        0x8,
        "おや、あんたたちかい。\x02",
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0x8,
        (
            "ヒヒャヒャ……買い物なら\x01",
            "早めにしておくれよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0x8,
        (
            "今日は夕方から\x01",
            "出かけるつもりだからね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3FAA")

    label("loc_2306")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_24E5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_23A7")

    #C0116
    ChrTalk(
        0x8,
        (
            "そういや、頼まれていた\x01",
            "ぬいぐるみが入荷してるよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0x8,
        (
            "包んでおくから\x01",
            "帰りにでも寄っとくれ。\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0x160,
        "#3300Fふふ、そうさせてもらうわね。\x02",
    )

    CloseMessageWindow()
    Jump("loc_24E0")

    label("loc_23A7")


    #C0119
    ChrTalk(
        0x8,
        (
            "おや、レン。\x01",
            "しばらくぶりだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0x8,
        "なんだ、その坊やと一緒かい？\x02",
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0x160,
        (
            "#3304Fええ、困っているみたいだから\x01",
            "助けてあげることにしたの。\x02\x03",

            "#3300F頼りない男性を支えるのも\x01",
            "一人前のレディの務めだから。\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0x8,
        "ヒヒャヒャ、それはいい！\x02",
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0x8,
        (
            "坊やもあんまりレンの手を\x01",
            "煩わせるんじゃないよ？\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0x101,
        "#0006Fま、参ったな……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_24E0")

    Jump("loc_3FAA")

    label("loc_24E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_26AA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 3)), scpexpr(EXPR_END)), "loc_2562")

    #C0125
    ChrTalk(
        0x8,
        (
            "表通りの事は知らないが\x01",
            "少なくともウチには来てないよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0x8,
        (
            "子供の入るような店じゃ\x01",
            "ないからねぇ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_26A5")

    label("loc_2562")


    #C0127
    ChrTalk(
        0x101,
        (
            "#0001F（うん、この人なら\x01",
            "  何か知っているかもしれないな……）\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    #A0128
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ロイドはコリンの写真を見せ\x01",
            "心当たりが無いか尋ねてみた。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0129
    ChrTalk(
        0x8,
        (
            "さぁて、知らないねえ。\x01",
            "少なくともウチには来てないよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0x8,
        (
            "ヒヒャヒャ……\x01",
            "子供の来るような店じゃ\x01",
            "ないからねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0x101,
        (
            "#0003Fそうですか……\x01",
            "ありがとうございました。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xAB, 3)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 14)

    label("loc_26A5")

    Jump("loc_3FAA")

    label("loc_26AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_2766")

    #C0132
    ChrTalk(
        0x8,
        (
            "やれやれ、こんな店にまで\x01",
            "客が来てるよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0x8,
        (
            "今日はあちこち\x01",
            "出かけなきゃなんないんだが。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xA, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2761")

    #C0134
    ChrTalk(
        0x102,
        (
            "#0100Fイメルダさんって……\x01",
            "あまり商売をする気は\x01",
            "ないんですね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2761")

    Jump("loc_3FAA")

    label("loc_2766")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_29C9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_27CD")

    #C0135
    ChrTalk(
        0x8,
        (
            "今日はあちこちお呼ばれしてるんだ。\x01",
            "ヒヒ……買い物なら\x01",
            "早めにしておくれよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_29C4")

    label("loc_27CD")


    #C0136
    ChrTalk(
        0x8,
        (
            "今日はクロスベル商工会の方に\x01",
            "呼ばれてるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0x8,
        "昔から少々付き合いがあってねぇ。\x02",
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0x8,
        (
            "ヒヒ……夜は\x01",
            "アルカンシェルの打ち上げに\x01",
            "混じらせてもらう予定だよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0x101,
        "#0005Fアルカンシェルの打ち上げに……？\x02",
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0x8,
        (
            "ヒヒャヒャ、\x01",
            "不思議そうな顔をしてるじゃないか。\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0x8,
        (
            "……当然だろう？\x01",
            "このアタシも出資者の一人なんだからね。\x02",
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
        "#0105Fそ、そうだったんですか……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xA, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_29C1")

    #C0143
    ChrTalk(
        0x104,
        "#0306Fさすが婆さんだぜ……\x02",
    )

    CloseMessageWindow()

    label("loc_29C1")

    SetScenarioFlags(0x0, 0)

    label("loc_29C4")

    Jump("loc_3FAA")

    label("loc_29C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_2BE3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_2A59")

    #C0144
    ChrTalk(
        0x8,
        (
            "アンタたち、アタシのアパートに\x01",
            "傷なんてつけたらタダじゃおかないよ？\x02",
        )
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0x104,
        "#0303F（ノーコメントが利口だな……多分。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_2BDE")

    label("loc_2A59")


    #C0146
    ChrTalk(
        0x8,
        (
            "市長暗殺を食い止めた\x01",
            "功労者だってのに\x01",
            "旧市街でお遊びとはねえ……\x02",
        )
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0x8,
        (
            "アタシのアパートに\x01",
            "傷なんて付けてないだろうね？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xA, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2B59")

    #C0148
    ChrTalk(
        0x101,
        (
            "#0011Fだ、大丈夫……\x01",
            "だと思います、多分。\x02",
        )
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0x104,
        (
            "#0300Fああ、指一本触れてねえッス！\x01",
            "（………………大嘘だけど。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2BDB")

    label("loc_2B59")


    #C0150
    ChrTalk(
        0x101,
        (
            "#0011Fア、アパート？\x01",
            "（そんなの持ってるのかこの人……）\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0x104,
        (
            "#0300Fああ、指一本触れてねえッス！\x01",
            "（………………多分だけど。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2BDB")

    SetScenarioFlags(0x0, 0)

    label("loc_2BDE")

    Jump("loc_3FAA")

    label("loc_2BE3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_2D18")

    #C0152
    ChrTalk(
        0x8,
        "今日はパーティに呼ばれてるんだ。\x02",
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0x8,
        (
            "ヒヒャヒャ……\x01",
            "おめかしして行かなくちゃねえ。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xA, 0x0, 0x10)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2D10")

    #C0154
    ChrTalk(
        0x101,
        (
            "#0000F（……イメルダさん、\x01",
            "  意外と顔が広いみたいだな。）\x02",
        )
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0x102,
        (
            "#0100F（まあ一応、クロスベルの\x01",
            "  名士の一人でもあるから……）\x02",
        )
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0x104,
        "#0306F（土地成金の因業#4Rいんごう#婆さんだけどな。\x02",
    )

    CloseMessageWindow()

    label("loc_2D10")

    SetScenarioFlags(0x0, 0)
    Jump("loc_3FAA")

    label("loc_2D18")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_2E34")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2D35")
    Call(0, 7)
    Jump("loc_2E2F")

    label("loc_2D35")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x95, 7)), scpexpr(EXPR_END)), "loc_2D46")
    Call(0, 7)
    Jump("loc_2E2F")

    label("loc_2D46")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x1, 0x6)"), scpexpr(EXPR_END)), "loc_2E2C")

    #C0157
    ChrTalk(
        0x8,
        (
            "あのキツネ顔なら\x01",
            "昨晩遅くにやってきたよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0x8,
        (
            "妻にヘソクリを取られただの\x01",
            "もう許してだの……\x02",
        )
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0x8,
        (
            "一人でギャアギャア愚痴った挙句\x01",
            "飲み直すとか言って出て行った。\x02",
        )
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0x8,
        (
            "ヒヒャヒャ……\x01",
            "その後の事は知らないねぇ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E2F")

    label("loc_2E2C")

    Call(0, 7)

    label("loc_2E2F")

    Jump("loc_3FAA")

    label("loc_2E34")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_2F50")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2E51")
    Call(0, 8)
    Jump("loc_2F4B")

    label("loc_2E51")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x95, 7)), scpexpr(EXPR_END)), "loc_2E62")
    Call(0, 8)
    Jump("loc_2F4B")

    label("loc_2E62")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x1, 0x6)"), scpexpr(EXPR_END)), "loc_2F48")

    #C0161
    ChrTalk(
        0x8,
        (
            "あのキツネ顔なら\x01",
            "昨晩遅くにやってきたよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0x8,
        (
            "妻にヘソクリを取られただの\x01",
            "もう許してだの……\x02",
        )
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0x8,
        (
            "一人でギャアギャア愚痴った挙句\x01",
            "飲み直すとか言って出て行った。\x02",
        )
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0x8,
        (
            "ヒヒャヒャ……\x01",
            "その後の事は知らないねぇ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F4B")

    label("loc_2F48")

    Call(0, 8)

    label("loc_2F4B")

    Jump("loc_3FAA")

    label("loc_2F50")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_312B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_2FFB")

    #C0165
    ChrTalk(
        0x8,
        (
            "そういや、あの偏屈ジジイとは\x01",
            "また交渉しなくちゃならないね。\x02",
        )
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0x8,
        (
            "やれやれ、毎度毎度、\x01",
            "面倒をかけてくれるよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0x101,
        "#0005F（何の話だろう……？）\x02",
    )

    CloseMessageWindow()
    Jump("loc_3126")

    label("loc_2FFB")


    #C0168
    ChrTalk(
        0x8,
        (
            "あんたたち\x01",
            "レンの知り合いなのかい？\x02",
        )
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0x8,
        (
            "ヒヒャヒャ、\x01",
            "面白い偶然もあったもんだねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0x101,
        (
            "#0005Fえっと……\x01",
            "お知り合いなんですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0x8,
        (
            "知り合いの偏屈ジジイの\x01",
            "工房に来ている子だよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0x8,
        (
            "本当の孫じゃないらしいが\x01",
            "随分可愛がっているみたいだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0x8,
        (
            "目利きも確かだし、\x01",
            "なかなかのお得意様だよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_3126")

    Jump("loc_3FAA")

    label("loc_312B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_3222")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_3187")

    #C0174
    ChrTalk(
        0x8,
        (
            "土地権利の確認もしておこうかねぇ。\x01",
            "管理も色々と苦労するんだよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_321D")

    label("loc_3187")


    #C0175
    ChrTalk(
        0x8,
        (
            "ＩＢＣに寄るついでに\x01",
            "土地権利の確認もしておこうかねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0x8,
        (
            "ヒヒ……アタシは市内に\x01",
            "何十箇所も土地を持ってるからね。\x01",
            "色々管理も苦労するんだ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_321D")

    Jump("loc_3FAA")

    label("loc_3222")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_3591")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_32D7")

    #C0177
    ChrTalk(
        0x8,
        "あんたら、導力オンチかい？\x02",
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0x8,
        (
            "ハア、その若さでそれじゃ\x01",
            "この先が思いやられるね。\x02",
        )
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0x101,
        (
            "#0006F（その歳で使いこなしている\x01",
            "  そちらが凄すぎなだけでは……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_358C")

    label("loc_32D7")


    #C0180
    ChrTalk(
        0x8,
        (
            "今日は夕方からＩＢＣに\x01",
            "行かなくちゃならないんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0x8,
        (
            "掘り出し物の骨董品を\x01",
            "購入したんで、その送金にねえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0x8,
        (
            "やれやれ……導力ネットが\x01",
            "本格的に始動すれば、イチイチ銀行に\x01",
            "足を運ぶ事もなくなるんだけどねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0x101,
        (
            "#0005F？？？\x01",
            "……どういうことですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0x103,
        (
            "#0203Fつまり導力端末から\x01",
            "ＩＢＣ口座にアクセスし\x01",
            "オンライン決算できるということです。\x02\x03",

            "#0200F銀行機能の仮想化と遍在化……\x01",
            "ＩＢＣが導力ネット事業を推進している\x01",
            "一番のメリットでしょうね。\x02\x03",

            "もっとも実現は\x01",
            "まだまだ先になると思いますが。\x02",
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
            "#0006Fごめん、ティオ。\x01",
            "さっぱり分からなかった。\x02",
        )
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0x104,
        "#0306F俺もさっぱりだぜ……\x02",
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0x102,
        (
            "#0106Fな、何となく\x01",
            "概要は判るんだけど……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_358C")

    Jump("loc_3FAA")

    label("loc_3591")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_3761")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xA, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_3683")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_35B7")
    Call(0, 9)
    Jump("loc_367E")

    label("loc_35B7")


    #C0188
    ChrTalk(
        0x8,
        (
            "アパートの鍵はしばらく\x01",
            "あんたらに預けておこう。\x02",
        )
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0x8,
        (
            "ヒヒ、また暇なときにでも\x01",
            "中を掃除しておいておくれ！\x02",
        )
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0x101,
        (
            "#0003F（このお婆さんとは\x01",
            "  長い付き合いになりそうだよ。\x01",
            "  ……何となくだけど。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_367E")

    Jump("loc_375C")

    label("loc_3683")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xA, 0x1, 0x1)"), scpexpr(EXPR_END)), "loc_3744")

    #C0191
    ChrTalk(
        0x8,
        (
            "魔獣が沸いているアパートは\x01",
            "旧市街の『メゾン・イメルダ』だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0x8,
        "まあ行けば分かるだろうさ。\x02",
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0x8,
        (
            "魔獣は１匹残らず退治しておくれ。\x01",
            "ヒヒ……頼んだよ\x01",
            "特務支援課の坊やたち。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_375C")

    label("loc_3744")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xA, 0x1, 0x0)"), scpexpr(EXPR_END)), "loc_3759")
    Call(0, 16)
    Jump("loc_375C")

    label("loc_3759")

    Call(0, 9)

    label("loc_375C")

    Jump("loc_3FAA")

    label("loc_3761")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_3A1F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6C, 3)), scpexpr(EXPR_END)), "loc_37E6")

    #C0194
    ChrTalk(
        0x8,
        (
            "白ハヤブサが刻まれた\x01",
            "リベール王家に伝わる指輪……\x02",
        )
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0x8,
        (
            "ヒヒヒ、坊やたちの\x01",
            "安月給じゃ手が出ないだろうね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A1A")

    label("loc_37E6")


    #C0196
    ChrTalk(
        0x8,
        (
            "ヒヒャヒャ……\x01",
            "今日はいい品が入ったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0x8,
        (
            "白ハヤブサの紋章が刻まれた\x01",
            "金耀石を加工した指輪……\x02",
        )
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0x8,
        (
            "リベール王家に伝わる品で\x01",
            "数年前に放蕩者の公爵が\x01",
            "手放した逸品らしい。\x02",
        )
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0x103,
        (
            "#0200F（王家に伝わる品って……\x01",
            "  そんなものを扱っても\x01",
            "  いいんでしょうか。）\x02",
        )
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0x102,
        (
            "#0105F（下手をしたら外交問題にも\x01",
            "  発展しそうだけど……）\x02",
        )
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0x101,
        (
            "#0003F（うーん……まずはそれが\x01",
            "  本物だとはっきりしないと\x01",
            "  何とも言えないな。）\x02",
        )
    )

    CloseMessageWindow()

    #C0202
    ChrTalk(
        0x8,
        (
            "ヒヒャヒャ……\x01",
            "この指輪を調べたいなら\x01",
            "坊やたちで買い取るんだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0203
    ChrTalk(
        0x8,
        (
            "もっとも、高いよこれは。\x01",
            "細工も見事だし、質の良い\x01",
            "金耀石を使っているからねぇ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x6C, 3)

    label("loc_3A1A")

    Jump("loc_3FAA")

    label("loc_3A1F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_3D23")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6C, 2)), scpexpr(EXPR_END)), "loc_3A8B")

    #C0204
    ChrTalk(
        0x8,
        "ヒヒャヒャ……アンタ達面白いよ。\x02",
    )

    CloseMessageWindow()

    #C0205
    ChrTalk(
        0x8,
        (
            "これからも注目させて\x01",
            "もらうとしようかね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3D1E")

    label("loc_3A8B")


    #C0206
    ChrTalk(
        0x8,
        "先日はお手柄だったねぇ。\x02",
    )

    CloseMessageWindow()

    #C0207
    ChrTalk(
        0x8,
        (
            "テスタメンツのヘッドの\x01",
            "計画に乗って囮役をやるとは。\x01",
            "ヒヒ、大したものじゃないか。\x02",
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
        "#0005Fえっ……？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x48, 1)), scpexpr(EXPR_END)), "loc_3BC0")

    #C0209
    ChrTalk(
        0x102,
        (
            "#0105Fそれは……\x01",
            "クロスベルタイムズの記事にも\x01",
            "載っていなかったはずだけど……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3BFD")

    label("loc_3BC0")


    #C0210
    ChrTalk(
        0x102,
        (
            "#0105Fグレイスさん……\x01",
            "そんな事まで記事にしたのかしら。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3BFD")


    #C0211
    ChrTalk(
        0x8,
        (
            "ヒヒャヒャ……なァに。\x01",
            "取引してる情報屋がいてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0212
    ChrTalk(
        0x8,
        (
            "ミラさえ出せば\x01",
            "大抵の事はわかるのさ。\x02",
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
        "#0200F情報屋……ですか。\x02",
    )

    CloseMessageWindow()

    #C0214
    ChrTalk(
        0x104,
        (
            "#0300Fさすがクロスベル。\x01",
            "怪しい商売もてんこ盛りだな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x6C, 2)

    label("loc_3D1E")

    Jump("loc_3FAA")

    label("loc_3D23")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_3EB2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F, 1)), scpexpr(EXPR_END)), "loc_3D6F")

    #C0215
    ChrTalk(
        0x8,
        (
            "気に入った品はあるかい？\x01",
            "特務支援課の坊やたち。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3EAD")

    label("loc_3D6F")


    #C0216
    ChrTalk(
        0x8,
        (
            "気に入った品はあるかい？\x01",
            "特務支援課の坊やたち。\x02",
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
        "#0005Fえっ……？\x02",
    )

    CloseMessageWindow()

    #C0218
    ChrTalk(
        0x104,
        (
            "#0305Fおいおい、婆さん。\x01",
            "何で俺たちの事を知ってるんだ？\x02",
        )
    )

    CloseMessageWindow()

    #C0219
    ChrTalk(
        0x8,
        (
            "ヒヒャヒャ……\x01",
            "この裏通りには色んな情報が\x01",
            "集まってくるからねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0220
    ChrTalk(
        0x8,
        "まあせいぜい頑張るといいさ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x4F, 1)

    label("loc_3EAD")

    Jump("loc_3FAA")

    label("loc_3EB2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_3F19")

    #C0221
    ChrTalk(
        0x8,
        "ヒヒャヒャ、いらっしゃい。\x02",
    )

    CloseMessageWindow()

    #C0222
    ChrTalk(
        0x8,
        (
            "うちはアンティーク屋だよ。\x01",
            "何でも見ていくがいいさ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3FAA")

    label("loc_3F19")


    #C0223
    ChrTalk(
        0x8,
        "ヒヒャヒャ、いらっしゃい。\x02",
    )

    CloseMessageWindow()

    #C0224
    ChrTalk(
        0x8,
        (
            "うちはアンティーク屋だよ。\x01",
            "何でも見ていくがいいさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0x101,
        (
            "#0003F（な、何だか\x01",
            "  怪しい雰囲気の店だな……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_3FAA")

    Jump("loc_6CC")

    label("loc_3FAF")

    SetChrSubChip(0x8, 0x0)
    TalkEnd(0x8)
    Return()

    # Function_4_490 end

    def Function_5_3FB7(): pass

    label("Function_5_3FB7")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0x8)
    ClearChrFlags(0x8, 0x10)
    TurnDirection(0x8, 0x0, 0)
    OP_52(0x8, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_404B")
    Jump("loc_4095")

    label("loc_404B")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_406B")
    OP_52(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4095")

    label("loc_406B")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_408B")
    OP_52(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4095")

    label("loc_408B")

    OP_52(0x8, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4095")

    OP_52(0x8, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x8, 0x10)

    #C0226
    ChrTalk(
        0x8,
        "ジロッ……\x02",
    )

    CloseMessageWindow()

    #C0227
    ChrTalk(
        0x101,
        (
            "#0003Fす、すみません。\x01",
            "ちょっと手が空かなくて。\x02",
        )
    )

    CloseMessageWindow()

    #C0228
    ChrTalk(
        0x102,
        (
            "#0106Fその……\x01",
            "なんとお詫びしたらいいか。\x02",
        )
    )

    CloseMessageWindow()

    #C0229
    ChrTalk(
        0x8,
        (
            "……まあいいさ。\x01",
            "アンタらも忙しそうだしね。\x02",
        )
    )

    CloseMessageWindow()

    #C0230
    ChrTalk(
        0x8,
        (
            "ヒヒ……\x01",
            "それに例のブローカーとは別に\x01",
            "新たな買い手が見つかってねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0x8,
        (
            "ミラ払いも遥かに良さそうだし\x01",
            "ま、不幸中の幸いだったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0232
    ChrTalk(
        0x101,
        "#0005Fそうでしたか……\x02",
    )

    CloseMessageWindow()

    #C0233
    ChrTalk(
        0x102,
        "#0100Fそれを聞いて安心しました。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0xD3, 3)
    SetChrSubChip(0x8, 0x0)
    TalkEnd(0x8)
    Return()

    # Function_5_3FB7 end

    def Function_6_4233(): pass

    label("Function_6_4233")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0x8)
    ClearChrFlags(0x8, 0x10)
    TurnDirection(0x8, 0x0, 0)
    OP_52(0x8, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_42C7")
    Jump("loc_4311")

    label("loc_42C7")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_42E7")
    OP_52(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4311")

    label("loc_42E7")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4307")
    OP_52(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4311")

    label("loc_4307")

    OP_52(0x8, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4311")

    OP_52(0x8, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x8, 0x10)

    #C0234
    ChrTalk(
        0x8,
        "おや、特務支援課かい。\x02",
    )

    CloseMessageWindow()

    #C0235
    ChrTalk(
        0x8,
        (
            "そうそう……\x01",
            "あんたらが途中で投げ出した\x01",
            "『メゾン・イメルダ』の話だけどねえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0236
    ChrTalk(
        0x8,
        (
            "あの後遊撃士が\x01",
            "さっくり片付けてくれたよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0237
    ChrTalk(
        0x8,
        (
            "ヒヒャヒャ、誰かさんと違って\x01",
            "頼りになるねぇ？\x02",
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
            "#0000F……あの、本当に\x01",
            "申し訳ありませんでした。\x02",
        )
    )

    CloseMessageWindow()

    #C0239
    ChrTalk(
        0x104,
        (
            "#0306F（何か末代まで\x01",
            "  祟られそうだなぁ……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x93, 4)
    SetChrSubChip(0x8, 0x0)
    TalkEnd(0x8)
    Return()

    # Function_6_4233 end

    def Function_7_44DC(): pass

    label("Function_7_44DC")

    SetChrSubChip(0x8, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_4533")

    #C0240
    ChrTalk(
        0x8,
        (
            "《銀》と特務支援課の対決……\x01",
            "ヒヒャヒャ、こいつは楽しみだねえ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_465F")

    label("loc_4533")

    SetChrName("")

    #A0241
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "夫人はカウンターの下で\x01",
            "端末らしきものを操作している。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0242
    ChrTalk(
        0x8,
        "カタカタ……\x02",
    )

    CloseMessageWindow()

    #C0243
    ChrTalk(
        0x8,
        (
            "おや、情報屋から\x01",
            "新しい情報が来てるじゃないか。\x02",
        )
    )

    CloseMessageWindow()

    #C0244
    ChrTalk(
        0x8,
        (
            "《銀》と特務支援課の対決……？\x01",
            "変わったニュースだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0245
    ChrTalk(
        0x101,
        (
            "#0001F（ヨナ……何よそに\x01",
            "  情報を回してるんだ……！）\x02",
        )
    )

    CloseMessageWindow()

    #C0246
    ChrTalk(
        0x103,
        "#0203F（……やっぱり後でシメます。）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_465F")

    Return()

    # Function_7_44DC end

    def Function_8_4660(): pass

    label("Function_8_4660")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_46C8")

    #C0247
    ChrTalk(
        0x8,
        (
            "アルカンシェルの劇場に\x01",
            "警察が出入りしてるらしいねぇ。\x01",
            "ヒヒ……これは要注目情報だよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_48B8")

    label("loc_46C8")


    #C0248
    ChrTalk(
        0x8,
        "アタシの掴んだ情報では……\x02",
    )

    CloseMessageWindow()

    #C0249
    ChrTalk(
        0x8,
        (
            "アルカンシェルの劇場に\x01",
            "警察が出入りしてるらしいねぇ。\x02",
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
            "新作公開も近いって時期に\x01",
            "スキャンダルでもあったら事だよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0251
    ChrTalk(
        0x8,
        (
            "まったく、せっかくの新作が\x01",
            "台無しにならないといいけどねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0252
    ChrTalk(
        0x101,
        (
            "#0003F（い、一部じゃ情報が\x01",
            "  流れ始めてるみたいだな……）\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6C, 2)), scpexpr(EXPR_END)), "loc_4878")

    #C0253
    ChrTalk(
        0x104,
        (
            "#0306F（情報屋の連中か……\x01",
            "  どの程度流れてるんだか。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_48B5")

    label("loc_4878")


    #C0254
    ChrTalk(
        0x104,
        (
            "#0300F（まあ、まだ眉唾情報って\x01",
            "  レベルみたいだが……）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_48B5")

    SetScenarioFlags(0x0, 0)

    label("loc_48B8")

    Return()

    # Function_8_4660 end

    def Function_9_48B9(): pass

    label("Function_9_48B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_4964")

    #C0255
    ChrTalk(
        0x8,
        (
            "ヒヒャヒャ……\x01",
            "あたしゃ７０年生きてるが\x01",
            "この街は飽きないねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0256
    ChrTalk(
        0x8,
        (
            "最近、新しい情報屋からも\x01",
            "直接情報を買っていてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0257
    ChrTalk(
        0x8,
        "毎日楽しませてもらっとるよ。\x02",
    )

    CloseMessageWindow()
    Jump("loc_4C72")

    label("loc_4964")


    #C0258
    ChrTalk(
        0x8,
        (
            "そういや、警備隊は\x01",
            "もう引き上げちまったらしいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0259
    ChrTalk(
        0x8,
        (
            "だらしがないねぇ。\x01",
            "まだ狼型魔獣ってのは\x01",
            "退治されてないんだろう？\x02",
        )
    )

    CloseMessageWindow()

    #C0260
    ChrTalk(
        0x103,
        (
            "#0205F……それはまだ\x01",
            "機密情報のはずですが……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6C, 2)), scpexpr(EXPR_END)), "loc_4AF6")

    #C0261
    ChrTalk(
        0x101,
        (
            "#0003F（また情報屋とやらから\x01",
            "  仕入れたみたいだな。）\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xA, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_4AB0")

    #C0262
    ChrTalk(
        0x104,
        (
            "#0306F（土地成金の上に地獄耳か……\x01",
            "  ホント喰えない婆さんだぜ。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4AF1")

    label("loc_4AB0")


    #C0263
    ChrTalk(
        0x104,
        (
            "#0303F（野次馬根性か……\x01",
            "  うーん、タチの悪い婆さんだぜ。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4AF1")

    Jump("loc_4C6F")

    label("loc_4AF6")


    #C0264
    ChrTalk(
        0x8,
        (
            "ヒヒャヒャ……なァに。\x01",
            "取引してる情報屋がいてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0265
    ChrTalk(
        0x8,
        (
            "ミラさえ出せば\x01",
            "大抵の事はわかるのさ。\x02",
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
        "#0003F情報屋……ですか。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xA, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_4C31")

    #C0267
    ChrTalk(
        0x104,
        (
            "#0306F（土地成金の上に地獄耳か……\x01",
            "  ホント喰えない婆さんだぜ。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4C6C")

    label("loc_4C31")


    #C0268
    ChrTalk(
        0x104,
        (
            "#0300Fさすがクロスベル。\x01",
            "怪しい商売もてんこ盛りだな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4C6C")

    SetScenarioFlags(0x6C, 2)

    label("loc_4C6F")

    SetScenarioFlags(0x0, 0)

    label("loc_4C72")

    Return()

    # Function_9_48B9 end

    def Function_10_4C73(): pass

    label("Function_10_4C73")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xEF, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4D7D")

    #C0269
    ChrTalk(
        0x8,
        (
            "おやあんたたち、\x01",
            "『闇医者グレン』を\x01",
            "全巻持ってるみたいだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0270
    ChrTalk(
        0x8,
        (
            "ふむ……アタシも\x01",
            "揃えようと思ってたんだが\x01",
            "つい買いそびれた巻があってねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0271
    ChrTalk(
        0x8,
        "どうだい、１つ相談だ。\x02",
    )

    CloseMessageWindow()

    #C0272
    ChrTalk(
        0x8,
        (
            "その『闇グレ』全巻、\x01",
            "あたしの持っている\x01",
            "掘り出し物と交換しないかい？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xEF, 6)
    Jump("loc_4DF1")

    label("loc_4D7D")


    #C0273
    ChrTalk(
        0x8,
        (
            "あんたたち、『闇グレ』全巻\x01",
            "持ってるんだねぇ……\x02",
        )
    )

    CloseMessageWindow()

    #C0274
    ChrTalk(
        0x8,
        (
            "どうだい、あたしの持っている\x01",
            "掘り出し物と交換しないかい？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4DF1")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【はい】\x01",        # 0
            "【いいえ】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5045")

    #C0275
    ChrTalk(
        0x8,
        (
            "ヒヒャヒャ！\x01",
            "確かに受け取ったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0276
    ChrTalk(
        0x8,
        (
            "それじゃあ今度はアタシの番だね。\x01",
            "……ほら、こいつをやろう。\x02",
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
            scpstr(SCPSTR_CODE_ITEM, 0x396),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を受け取った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    SubItemNumber(0x2C6, 1)
    SubItemNumber(0x2C7, 1)
    SubItemNumber(0x2C8, 1)
    SubItemNumber(0x2C9, 1)
    SubItemNumber(0x2CA, 1)
    SubItemNumber(0x2CB, 1)
    SubItemNumber(0x2CC, 1)
    SubItemNumber(0x2CD, 1)
    SubItemNumber(0x2CE, 1)
    SubItemNumber(0x2CF, 1)
    SubItemNumber(0x2D0, 1)
    SubItemNumber(0x2D1, 1)
    SubItemNumber(0x2D2, 1)
    SubItemNumber(0x2D3, 1)
    AddItemNumber(0x396, 1)
    SetScenarioFlags(0x9D, 6)

    #C0278
    ChrTalk(
        0x101,
        (
            "#0005Fあ、ありがとうございます。\x02\x03",

            "でもこれは……？\x02",
        )
    )

    CloseMessageWindow()

    #C0279
    ChrTalk(
        0x8,
        (
            "ヒヒ……とあるルートで仕入れた\x01",
            "掘り出し物だよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0280
    ChrTalk(
        0x8,
        (
            "なんでも古代ゼムリア文明期の\x01",
            "遺物らしい。\x02",
        )
    )

    CloseMessageWindow()

    #C0281
    ChrTalk(
        0x8,
        (
            "うんと硬くて、どんな方法でも\x01",
            "加工できないそうだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0282
    ChrTalk(
        0x8,
        (
            "ヒヒャヒャ、だが持ってれば\x01",
            "何かの役に立つかもしれないねぇ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_50C9")

    label("loc_5045")


    #C0283
    ChrTalk(
        0x8,
        "そうかい、そりゃ残念だね……\x02",
    )

    CloseMessageWindow()

    #C0284
    ChrTalk(
        0x8,
        (
            "また古本屋でも当たってみようかね。\x01",
            "ここまできたら、全巻揃えて\x01",
            "一気読みしたい所だからねぇ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_50C9")

    Return()

    # Function_10_4C73 end

    def Function_11_50CA(): pass

    label("Function_11_50CA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_514C")
    OP_63(0xA, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0285
    ChrTalk(
        0xA,
        "あれ、十、百、千……\x02",
    )

    CloseMessageWindow()

    #C0286
    ChrTalk(
        0xA,
        (
            "ゼロが３つくらい\x01",
            "多い気がするけど\x01",
            "……気のせいかなぁ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_51E8")

    label("loc_514C")


    #C0287
    ChrTalk(
        0xA,
        (
            "へえ、こんな店が\x01",
            "あったんだなぁ～。\x02",
        )
    )

    CloseMessageWindow()

    #C0288
    ChrTalk(
        0xA,
        (
            "パレードを追っかけた帰りに\x01",
            "思わぬ発見をしちゃったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0289
    ChrTalk(
        0xA,
        (
            "にひひ……なんか\x01",
            "買って帰ろうかな。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xA, 0x5A, 0x0)
    SetChrFlags(0xA, 0x10)
    SetScenarioFlags(0x0, 2)

    label("loc_51E8")

    TalkEnd(0xFE)
    Return()

    # Function_11_50CA end

    def Function_12_51EC(): pass

    label("Function_12_51EC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x93, 0)), scpexpr(EXPR_END)), "loc_526F")

    #C0290
    ChrTalk(
        0x9,
        (
            "#3300Fあの狼さん、お兄さんたちの\x01",
            "お友達になったんでしょう？\x02\x03",

            "#3309F今度レンにも\x01",
            "改めて紹介してちょうだいね？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5272")

    label("loc_526F")

    Call(0, 13)

    label("loc_5272")

    TalkEnd(0xFE)
    Return()

    # Function_12_51EC end

    def Function_13_5276(): pass

    label("Function_13_5276")

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
        "#3305F#5Pあら……？\x02",
    )

    CloseMessageWindow()

    #C0292
    ChrTalk(
        0x103,
        "#0205F#6Pあなたは確か……\x02",
    )

    CloseMessageWindow()

    #C0293
    ChrTalk(
        0x101,
        (
            "#0005F#12Pああ……人形工房の。\x02\x03",

            "#0000Fお久しぶり。\x01",
            "確か、レンちゃんだったか？\x02",
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
            "うふふ、一月ぶりかしら。\x02\x03",

            "でも、レディの名前を\x01",
            "わざわざ確認するものじゃないわ。\x02\x03",

            "当然のように覚えていて\x01",
            "再会の挨拶をするのが紳士でしょう？\x02",
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
        "#0012F#12Pはは、確かに。\x02",
    )

    CloseMessageWindow()

    #C0296
    ChrTalk(
        0x104,
        "#0304F#11Pなかなか手厳しいねぇ。\x02",
    )

    CloseMessageWindow()

    #C0297
    ChrTalk(
        0x102,
        (
            "#0102F#11Pふふっ、１人みたいだけど\x01",
            "バスで遊びに来たのかしら？\x02",
        )
    )

    CloseMessageWindow()

    #C0298
    ChrTalk(
        0x9,
        (
            "#3304F#5Pええ、そんな所ね。\x02\x03",

            "#3300Fこのアンティーク屋さんには\x01",
            "たまに一人で遊びに来ているの。\x02\x03",

            "おじいさんの人形がたまに出てるし\x01",
            "可愛いぬいぐるみが\x01",
            "入荷してることもあるから。\x02",
        )
    )

    CloseMessageWindow()

    #C0299
    ChrTalk(
        0x101,
        (
            "#0005F#12Pへえ、そうなのか。\x02\x03",

            "#0006Fでもこの辺り、\x01",
            "子供が一人でうろつくのは……\x02",
        )
    )

    CloseMessageWindow()

    #C0300
    ChrTalk(
        0x9,
        (
            "#3304F#5Pクスクス。\x01",
            "別に危ないことはないわ。\x02\x03",

            "呼び込みのお兄さんも\x01",
            "お水のお姉さんも優しいし……\x02\x03",

            "#3302F路地の奥の黒メガネさんたちも\x01",
            "けっこう楽しい人たちだもの。\x02",
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
        "#0003F#12Pう、うーん……\x02",
    )

    CloseMessageWindow()

    #C0302
    ChrTalk(
        0x102,
        "#0108F#11Pちょっと心配だけど……\x02",
    )

    CloseMessageWindow()

    #C0303
    ChrTalk(
        0x9,
        (
            "#3304F#5Pうふふ、ところで──\x02\x03",

            "#3302F狼さんとの鬼ごっこは\x01",
            "なかなか楽しかったみたいね？\x02\x03",

            "特別ゲストがいっぱい\x01",
            "参加してくれたみたいだし。\x02",
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
        "#0105F#11Pえっ……\x02",
    )

    CloseMessageWindow()

    #C0305
    ChrTalk(
        0x101,
        (
            "#0011F#12Pもしかして……\x01",
            "クロスベルタイムズの記事から\x01",
            "そんな風に察したのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0306
    ChrTalk(
        0x9,
        (
            "#3304F#5Pクスクス、そんな所かしら。\x02\x03",

            "#3300Fあの狼さん、お兄さんたちの\x01",
            "お友達になったんでしょう？\x02\x03",

            "#3309F今度レンにも\x01",
            "改めて紹介してちょうだいね？\x02",
        )
    )

    CloseMessageWindow()

    #C0307
    ChrTalk(
        0x101,
        "#0002F#12Pあ、ああ、分かったよ。\x02",
    )

    CloseMessageWindow()

    #C0308
    ChrTalk(
        0x104,
        (
            "#0302F#11P（相変わらず\x01",
            "  ミステリアスな嬢ちゃんだな。）\x02",
        )
    )

    CloseMessageWindow()

    #C0309
    ChrTalk(
        0x103,
        "#0200F#6P（……そうですね。）\x02",
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

    # Function_13_5276 end

    def Function_14_5A3D(): pass

    label("Function_14_5A3D")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5ACB")
    OP_29(0x46, 0x1, 0x4)

    #C0310
    ChrTalk(
        0x101,
        (
            "#0003F（よし、裏通りの聞き込みは\x01",
            "  これで十分だな。）\x02\x03",

            "#0001F（次は中央広場で\x01",
            "  聞き込みをしてみよう。）\x02",
        )
    )

    CloseMessageWindow()
    OP_D0(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0xB9, 4)

    label("loc_5ACB")

    Return()

    # Function_14_5A3D end

    def Function_15_5ACC(): pass

    label("Function_15_5ACC")

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
        "#11Pおや来たかい、『特務支援課』。\x02",
    )

    CloseMessageWindow()

    #C0312
    ChrTalk(
        0x101,
        (
            "#5P#0000Fどうも……\x01",
            "イメルダさんというのは\x01",
            "貴女でいいみたいですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0313
    ChrTalk(
        0x8,
        (
            "#11Pその通りだよ。\x01",
            "アタシがイメルダだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0314
    ChrTalk(
        0x8,
        (
            "#11Pヒヒ、それにしても\x01",
            "若い坊やたちが沢山来たねぇ。\x01",
            "……どれどぉれ？\x02",
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
            "イメルダ夫人は立ち上がって\x01",
            "顔をのぞき込んできた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0316
    ChrTalk(
        0x101,
        "#5P#0005F（か、顔の大きい人だ……）\x02",
    )

    CloseMessageWindow()

    #C0317
    ChrTalk(
        0x102,
        (
            "#5P#0105F（インパクトのある方ね……）\x02\x03",

            "#0103F（『イメルダ夫人』といえば\x01",
            "  確かクロスベルの名士の\x01",
            "  一人だったと思うけど……）\x02\x03",

            "#0100Fえっと、イメルダさん。\x01",
            "要請ではお持ちのアパートに\x01",
            "魔獣が沸いたという事でしたが……\x02",
        )
    )

    CloseMessageWindow()

    #C0318
    ChrTalk(
        0x104,
        (
            "#6P#0305Fアパートって市内だよな。\x01",
            "ヤバイんじゃないか？\x02",
        )
    )

    CloseMessageWindow()

    #C0319
    ChrTalk(
        0x8,
        (
            "#11Pヒヒャヒャ……\x01",
            "まあそう言う事だね。\x02",
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
        "#6P#0200F（危機感が感じられない……）\x02",
    )

    CloseMessageWindow()

    #C0321
    ChrTalk(
        0x104,
        (
            "#6P#0306F（神経の図太そうな\x01",
            "  婆さんだなぁ……）\x02",
        )
    )

    CloseMessageWindow()

    #C0322
    ChrTalk(
        0x8,
        "#11Pともかく、受けてくれるのかい？\x02",
    )

    CloseMessageWindow()
    OP_29(0xA, 0x1, 0x0)
    Call(0, 17)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5EDE")
    Call(0, 18)

    label("loc_5EDE")

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

    # Function_15_5ACC end

    def Function_16_5F6A(): pass

    label("Function_16_5F6A")

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
            "#11Pアタシの持っているアパートに\x01",
            "魔獣が沸いているらしくてね。\x01",
            "坊やたちに駆除を頼みたい。\x02",
        )
    )

    CloseMessageWindow()

    #C0324
    ChrTalk(
        0x8,
        "#11Pヒヒ……受けてくれるかい？\x02",
    )

    CloseMessageWindow()
    Call(0, 17)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_607B")
    Call(0, 18)

    label("loc_607B")

    SetChrPos(0x0, -750, 0, 2000, 0)
    EventEnd(0x5)
    Return()

    # Function_16_5F6A end

    def Function_17_608F(): pass

    label("Function_17_608F")

    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【引き受ける】\x01",      # 0
            "【やめる】\x01",          # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6200")

    #C0325
    ChrTalk(
        0x101,
        (
            "#5P#0006F今は少し……\x01",
            "仕事が立て込んでまして。\x02",
        )
    )

    CloseMessageWindow()

    #C0326
    ChrTalk(
        0x8,
        (
            "#11Pヒヒ……そうかい。\x01",
            "ならなるべく早く頼むよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0327
    ChrTalk(
        0x8,
        (
            "#11Pあまり遅いとギルドの方に\x01",
            "回すつもりだからねぇ。\x02",
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
        "#5P#0003Fぜ、善処します……\x02",
    )

    CloseMessageWindow()

    label("loc_6200")

    Return()

    # Function_17_608F end

    def Function_18_6201(): pass

    label("Function_18_6201")


    #C0329
    ChrTalk(
        0x8,
        (
            "#11Pヒヒヒ、それでは\x01",
            "仕事の話をしようかね。\x02",
        )
    )

    CloseMessageWindow()

    #C0330
    ChrTalk(
        0x101,
        "#5P#0000Fええ、お願いします。\x02",
    )

    CloseMessageWindow()

    #C0331
    ChrTalk(
        0x8,
        (
            "#11Pアタシは市内に\x01",
            "何軒か土地を持っていてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0332
    ChrTalk(
        0x8,
        (
            "#11P今問題のアパート\x01",
            "『メゾン・イメルダ』もその一つだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0333
    ChrTalk(
        0x8,
        (
            "#11P場所は旧市街。\x01",
            "やや奥まった場所だね。\x02",
        )
    )

    CloseMessageWindow()

    #C0334
    ChrTalk(
        0x102,
        "#5P#0105F旧市街でしたか……\x02",
    )

    CloseMessageWindow()

    #C0335
    ChrTalk(
        0x104,
        (
            "#6P#0303F確かにごちゃっとしてるし\x01",
            "ほっときゃ魔獣くらい\x01",
            "沸きそうだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0336
    ChrTalk(
        0x8,
        (
            "#11Pああ、本当に\x01",
            "どこからともなく\x01",
            "沸いてくるもんでね。\x02",
        )
    )

    CloseMessageWindow()

    #C0337
    ChrTalk(
        0x8,
        (
            "#11Pきっちり綺麗にしておかないと\x01",
            "１週間と持たないんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0338
    ChrTalk(
        0x8,
        (
            "#11P坊やたちに頼みたいのは\x01",
            "魔獣の掃討だよ。\x01",
            "１匹残らず退治しておくれ。\x02",
        )
    )

    CloseMessageWindow()

    #C0339
    ChrTalk(
        0x101,
        (
            "#5P#0001F分かりました。\x01",
            "魔獣の全掃討ですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0340
    ChrTalk(
        0x103,
        (
            "#6P#0200F放置しておくと危険ですし\x01",
            "綺麗に退治してしまいましょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0341
    ChrTalk(
        0x8,
        (
            "#11Pそれでは\x01",
            "これを預けておくよ。\x02",
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
            "を受け取った。\x02",
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
        "#5P#0000Fお預かりします。\x02",
    )

    CloseMessageWindow()

    #C0344
    ChrTalk(
        0x102,
        (
            "#5P#0100Fそれでは早速\x01",
            "旧市街に向かいましょうか。\x02",
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
            "クエスト【廃アパートの魔獣駆除要請】\x07\x00",
            "を開始した！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_29(0xA, 0x1, 0x1)
    Return()

    # Function_18_6201 end

    def Function_19_65D7(): pass

    label("Function_19_65D7")

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
        "#11Pほお、そんな事が……\x02",
    )

    CloseMessageWindow()

    #C0347
    ChrTalk(
        0x8,
        (
            "#11Pヒヒャヒャ、特務支援課。\x01",
            "中々やるじゃないか。\x02",
        )
    )

    CloseMessageWindow()

    #C0348
    ChrTalk(
        0x8,
        (
            "#11Pちぃと手際は悪いが\x01",
            "やる事はやってくれるようだねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0349
    ChrTalk(
        0x101,
        "#5P#0006Fはあ、どうも……\x02",
    )

    CloseMessageWindow()

    #C0350
    ChrTalk(
        0x104,
        (
            "#6P#0301Fというか魔獣が\x01",
            "あんなにはびこってるなんざ……\x01",
            "何年ほったらかしてんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0351
    ChrTalk(
        0x103,
        (
            "#6P#0203Fそうですね。\x01",
            "安全のためにも\x01",
            "もう少し管理してほしいかと。\x02",
        )
    )

    CloseMessageWindow()

    #C0352
    ChrTalk(
        0x102,
        (
            "#5P#0100Fでも、これで\x01",
            "アパートが運用できますよね。\x02\x03",

            "人が住むようになれば\x01",
            "もう魔獣も……\x02",
        )
    )

    CloseMessageWindow()

    #C0353
    ChrTalk(
        0x8,
        (
            "#11Pああ、そうさね。\x01",
            "もう何年かしたら\x01",
            "運用を考えるとしようか。\x02",
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
        "#5P#0105Fえ……？\x02",
    )

    CloseMessageWindow()

    #C0355
    ChrTalk(
        0x8,
        (
            "#11P旧市街は家賃が安いからね、\x01",
            "もう少し地価が上がってからの方が\x01",
            "ウマミが増すんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0356
    ChrTalk(
        0x8,
        (
            "#11Pヒヒ……まあ土地運用に関しては\x01",
            "アタシを信用しな。\x02",
        )
    )

    CloseMessageWindow()

    #C0357
    ChrTalk(
        0x8,
        (
            "#11Pアタシはイメルダ、\x01",
            "クロスベルで一、二を争う\x01",
            "大地主だからねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0358
    ChrTalk(
        0x8,
        (
            "#11P旧市街のボロアパートなんざ序の口、\x01",
            "好景気と地価上昇に合わせて\x01",
            "市内何十箇所って土地を運用してるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0359
    ChrTalk(
        0x101,
        (
            "#5P#0000Fと、土地成金……\x01",
            "……というやつですか。\x02\x03",

            "#0006F（もしかして、本業はそっち？）\x02",
        )
    )

    CloseMessageWindow()

    #C0360
    ChrTalk(
        0x102,
        (
            "#5P#0103F（『イメルダ夫人』……\x01",
            "  クロスベルの社交界では\x01",
            "  そこそこ名の通った人よ。）\x02\x03",

            "#0100F（資産家とは聞いていたけど……）\x02",
        )
    )

    CloseMessageWindow()

    #C0361
    ChrTalk(
        0x104,
        (
            "#6P#0300F（ハハ、道理で\x01",
            "  只者じゃねえ雰囲気なわけだ……）\x02",
        )
    )

    CloseMessageWindow()

    #C0362
    ChrTalk(
        0x8,
        (
            "#11Pま、土地は放っておくと\x01",
            "たまに魔獣が沸くから\x01",
            "掃除は必要なんだがねぇ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0363
    ChrTalk(
        0x8,
        (
            "#11Pおお……そうだ。\x01",
            "アパートの鍵はしばらく\x01",
            "あんたらに預けておこう。\x02",
        )
    )

    CloseMessageWindow()

    #C0364
    ChrTalk(
        0x8,
        (
            "#11Pヒヒ、また暇なときにでも\x01",
            "中を掃除しておいておくれ！\x02",
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
        "#6P#0200F（達者なお婆さんです。）\x02",
    )

    CloseMessageWindow()

    #C0366
    ChrTalk(
        0x101,
        (
            "#5P#0006F（そろそろ仕事に戻ろうか。\x01",
            "  今回はどっと疲れたよ……）\x02",
        )
    )

    CloseMessageWindow()

    #C0367
    ChrTalk(
        0x102,
        "#5P#0106F（ええ、そうしましょう……）\x02",
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
            "クエスト【廃アパートの魔獣駆除要請】\x07\x00",
            "を達成した！\x02",
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

    # Function_19_65D7 end

    def Function_20_6D89(): pass

    label("Function_20_6D89")

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
        "#6P#1200Fグルルルル……\x02",
    )

    CloseMessageWindow()

    #C0370
    ChrTalk(
        0x103,
        (
            "#5P#0200F店内に匂いが\x01",
            "残っているようです。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xA, 0x1, 0x1)"), scpexpr(EXPR_END)), "loc_6EAA")

    #C0371
    ChrTalk(
        0x101,
        (
            "#11P#0003Fイメルダさんに聞いてみようか。\x01",
            "何か知っているかもしれない。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6EF1")

    label("loc_6EAA")


    #C0372
    ChrTalk(
        0x101,
        (
            "#11P#0003F店主の人に聞いてみようか。\x01",
            "何か知っているかもしれない。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6EF1")

    OP_68(-730, 1450, 2860, 3000)

    def lambda_6F07():
        OP_97(0x101, 0x0, 0x0, 0xCB2, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6F07)
    Sleep(50)

    def lambda_6F24():
        OP_97(0x103, 0x0, 0x0, 0xCB2, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_6F24)
    Sleep(50)

    def lambda_6F41():
        OP_97(0x11C, 0x0, 0x0, 0xCB2, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x11C, 1, lambda_6F41)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x11C, 1)

    #C0373
    ChrTalk(
        0x101,
        (
            "#6P#0000Fあの、スミマセン。\x01",
            "少し尋ねたいんですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0374
    ChrTalk(
        0x8,
        (
            "#11Pおやぁ？\x01",
            "特務支援課じゃないか。\x02",
        )
    )

    CloseMessageWindow()

    #C0375
    ChrTalk(
        0x8,
        (
            "#11Pヒャヒャ、ついに\x01",
            "警察をクビにでもなったのかい？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xA, 0x1, 0x1)"), scpexpr(EXPR_END)), "loc_7037")

    #C0376
    ChrTalk(
        0x101,
        "#6P#0006F何でそうなるんですか……\x02",
    )

    CloseMessageWindow()
    Jump("loc_707E")

    label("loc_7037")


    #C0377
    ChrTalk(
        0x101,
        (
            "#6P#0006Fな、何の話ですか。\x01",
            "（まったく怪しい\x01",
            "  お婆さんだな……）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_707E")


    #C0378
    ChrTalk(
        0x101,
        (
            "#6P#0001Fつかぬ事を伺いますが、\x01",
            "昨日こちらに\x01",
            "酔った客が来ませんでしたか？\x02\x03",

            "#0003Fどうやらこの辺りで\x01",
            "失くし物をしたらしいんですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0379
    ChrTalk(
        0x8,
        "#11Pおお、あのキツネ顔の男かい。\x02",
    )

    CloseMessageWindow()

    #C0380
    ChrTalk(
        0x8,
        (
            "#11Pそういえば\x01",
            "プンプン酒臭くなって\x01",
            "入ってきたねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0381
    ChrTalk(
        0x8,
        (
            "#11P妻にヘソクリを取られただの\x01",
            "もう許してだの……\x02",
        )
    )

    CloseMessageWindow()

    #C0382
    ChrTalk(
        0x8,
        (
            "#11Pひとしきり愚痴った挙句、\x01",
            "飲み直すとか言って出て行ったが。\x02",
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
        "#6P#0006Fな、なんというか……\x02",
    )

    CloseMessageWindow()

    #C0384
    ChrTalk(
        0x103,
        (
            "#6P#0200Fそれはご迷惑を\x01",
            "お掛けしました。\x02",
        )
    )

    CloseMessageWindow()

    #C0385
    ChrTalk(
        0x8,
        (
            "#11Pヒヒ、全くだよ。\x01",
            "今度宝石でも買いに来るように\x01",
            "言っといておくれ。\x02",
        )
    )

    CloseMessageWindow()

    #C0386
    ChrTalk(
        0x101,
        (
            "#6P#0003F（結婚指輪が見つからなかったら\x01",
            "  そういう事になりそうだけどな……）\x02\x03",

            "#0000Fわ、分かりました。\x01",
            "協力感謝します。\x02",
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
            "#6P#0203Fしかし、この店内にも\x01",
            "指輪は落ちていないようですね。\x02\x03",

            "#0200F……もう少し\x01",
            "探してみましょう。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 500)

    #C0388
    ChrTalk(
        0x101,
        "#12P#0000Fああ、そうしよう。\x02",
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, -750, 0, 2000, 0)
    OP_29(0x15, 0x1, 0x6)
    EventEnd(0x5)
    Return()

    # Function_20_6D89 end

    def Function_21_73F5(): pass

    label("Function_21_73F5")

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
            "カウンターの下にある通信器で\x01",
            "イメルダ夫人が通話している。\x02",
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
            "#11Pなんだってぇ！？\x01",
            "冗談じゃあないよ！\x02",
        )
    )

    CloseMessageWindow()

    #C0391
    ChrTalk(
        0x8,
        (
            "#11Pこっちはとっくに\x01",
            "買い手を見つけてるんだ！\x02",
        )
    )

    CloseMessageWindow()

    #C0392
    ChrTalk(
        0x8,
        (
            "#11P完成はしてるんだろう！？\x01",
            "だったらとっとと寄越しな！\x02",
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
            "#11Pクソッ！\x01",
            "あのジジイ、切りやがった！\x02",
        )
    )

    CloseMessageWindow()
    OP_68(-10, 1350, 1330, 3000)
    MoveCamera(317, 17, 0, 3000)
    SetCameraDistance(21890, 3000)

    def lambda_7603():
        OP_97(0x101, 0x0, 0x0, 0x8CA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7603)
    Sleep(50)

    def lambda_7620():
        OP_97(0x102, 0x0, 0x0, 0x8CA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7620)
    Sleep(50)

    def lambda_763D():
        OP_97(0x103, 0x0, 0x0, 0x8CA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_763D)
    Sleep(50)

    def lambda_765A():
        OP_97(0x104, 0x0, 0x0, 0x8CA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_765A)
    OP_6F(0x79)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    #C0395
    ChrTalk(
        0x102,
        "#6P#0100Fこんにちは、イメルダさん。\x02",
    )

    CloseMessageWindow()

    #C0396
    ChrTalk(
        0x101,
        "#6P#0005F何かあったんですか？\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0397
    ChrTalk(
        0x8,
        "#11Pああ、アンタたちか。\x02",
    )

    CloseMessageWindow()

    #C0398
    ChrTalk(
        0x8,
        (
            "#11Pいやね、知り合いの偏屈ジジイが\x01",
            "ふざけたことを言い出して……\x02",
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
            "#11Pヒヒャヒャ、これも\x01",
            "女神の巡り合わせじゃないか！\x02",
        )
    )

    CloseMessageWindow()

    #C0400
    ChrTalk(
        0x8,
        "#11Pそうだそうだ、そうしよう！\x02",
    )

    CloseMessageWindow()

    #C0401
    ChrTalk(
        0x101,
        "#6P#0011Fへ……\x02",
    )

    CloseMessageWindow()

    #C0402
    ChrTalk(
        0x104,
        "#6P#0306Fなんかイヤな予感が……\x02",
    )

    CloseMessageWindow()

    #C0403
    ChrTalk(
        0x103,
        (
            "#6P#0211F……予感ではなく\x01",
            "確信だと思いますが。\x02",
        )
    )

    CloseMessageWindow()

    #C0404
    ChrTalk(
        0x8,
        "#11Pアンタたち、今ヒマかい？\x02",
    )

    CloseMessageWindow()
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0405
    ChrTalk(
        0x8,
        (
            "#11Pそうかヒマかい！\x01",
            "いやぁ、それは何よりだねぇ。\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 22)
    EventEnd(0x5)
    Return()

    # Function_21_73F5 end

    def Function_22_78C7(): pass

    label("Function_22_78C7")


    #C0406
    ChrTalk(
        0x101,
        (
            "#6P#0012Fい、いや。\x01",
            "一応行く所がありまして。\x02",
        )
    )

    CloseMessageWindow()

    #C0407
    ChrTalk(
        0x8,
        (
            "#11Pフン、どうせ急ぎの\x01",
            "仕事ってわけじゃないんだろ？\x02",
        )
    )

    CloseMessageWindow()

    #C0408
    ChrTalk(
        0x8,
        (
            "#11Pこんな所に顔を\x01",
            "出してるくらいだからねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0409
    ChrTalk(
        0x101,
        "#6P#0001Fぐっ……まあそうですけど。\x02",
    )

    CloseMessageWindow()

    #C0410
    ChrTalk(
        0x102,
        (
            "#6P#0100Fひょっとして……\x01",
            "特務支援課にご依頼を？\x02",
        )
    )

    CloseMessageWindow()

    #C0411
    ChrTalk(
        0x8,
        (
            "#11Pさすがマクダエルの孫娘。\x01",
            "察しがいいじゃないか。\x02",
        )
    )

    CloseMessageWindow()

    #C0412
    ChrTalk(
        0x8,
        (
            "#11Pヒヒ、もちろん報酬は\x01",
            "それなりに用意させてもらうよ？\x02",
        )
    )

    CloseMessageWindow()

    #C0413
    ChrTalk(
        0x101,
        (
            "#6P#0006Fいや、そういう問題じゃ……\x02\x03",

            "#0000F……まあいいや。\x01",
            "一応、話を聞かせてください。\x02",
        )
    )

    CloseMessageWindow()

    #C0414
    ChrTalk(
        0x8,
        "#11Pヒヒ、いいともさ。\x02",
    )

    CloseMessageWindow()

    #C0415
    ChrTalk(
        0x8,
        (
            "#11Pアンタたちに頼みたいのは\x01",
            "《人形》の受け取りと運搬でね。\x02",
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
        "#6P#0005Fえ……！？\x02",
    )

    CloseMessageWindow()

    #C0417
    ChrTalk(
        0x102,
        "#6P#0105F人形というと、まさか……\x02",
    )

    CloseMessageWindow()

    #C0418
    ChrTalk(
        0x8,
        (
            "#11Pああ、北の山道外れにある\x01",
            "《ローゼンベルク工房》の人形さ。\x02",
        )
    )

    CloseMessageWindow()

    #C0419
    ChrTalk(
        0x8,
        (
            "#11Pもちろん、例の競売会の時みたいに\x01",
            "ガセってわけじゃないよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0420
    ChrTalk(
        0x8,
        (
            "#11P正真正銘の、完成したばかりの\x01",
            "ローゼンベルクドールの新作でね。\x02",
        )
    )

    CloseMessageWindow()

    #C0421
    ChrTalk(
        0x104,
        (
            "#6P#0305Fおいおい、それって\x01",
            "数十万ミラはするっていう……\x02",
        )
    )

    CloseMessageWindow()

    #C0422
    ChrTalk(
        0x103,
        (
            "#6P#0203Fクロスベル市民の平均年収に\x01",
            "匹敵しそうな値段の人形ですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0423
    ChrTalk(
        0x8,
        (
            "#11Pああ、一応ウチは\x01",
            "あそこの人形の販売代理を\x01",
            "請け負っているんだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0424
    ChrTalk(
        0x8,
        (
            "#11P問題の工房の主人ってのが\x01",
            "人嫌いの偏屈なジジイでね！\x02",
        )
    )

    CloseMessageWindow()

    #C0425
    ChrTalk(
        0x8,
        (
            "#11Pせっかく新作人形の\x01",
            "買い手が決まったっていうのに\x01",
            "今更ゴネ始めやがったんだよ！\x02",
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
            "#6P#0012Fえっと、さすがにそれは\x01",
            "俺たちにはどうしようもない\x01",
            "問題だと思うんですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0427
    ChrTalk(
        0x102,
        (
            "#6P#0106Fせめて運搬だけなら\x01",
            "何とかなりそうですけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0428
    ChrTalk(
        0x103,
        (
            "#6P#0200Fでも、その工房の主人は\x01",
            "どうしていきなり反対を？\x02",
        )
    )

    CloseMessageWindow()

    #C0429
    ChrTalk(
        0x8,
        (
            "#11Pいや、その買い手ってのが\x01",
            "ちょいと問題でねぇ……\x02",
        )
    )

    CloseMessageWindow()

    #C0430
    ChrTalk(
        0x8,
        (
            "#11P実は、美術品のたぐいを\x01",
            "不当な高値で転売している\x01",
            "評判の悪いブローカーだったんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0431
    ChrTalk(
        0x8,
        (
            "#11Pそれがあのジジイには\x01",
            "気に入らなかったらしくてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0432
    ChrTalk(
        0x102,
        (
            "#6P#0108Fそれは作り手としては\x01",
            "気に入らないでしょうね……\x02",
        )
    )

    CloseMessageWindow()

    #C0433
    ChrTalk(
        0x104,
        (
            "#6P#0301Fうーん、ちょいと\x01",
            "難易度高すぎじゃねぇか？\x02",
        )
    )

    CloseMessageWindow()

    #C0434
    ChrTalk(
        0x8,
        (
            "#11Pなに言ってんだい。\x01",
            "若いモンがだらしがない。\x02",
        )
    )

    CloseMessageWindow()

    #C0435
    ChrTalk(
        0x8,
        (
            "#11Pアタシはこれでも\x01",
            "アンタらの事は買ってるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0436
    ChrTalk(
        0x8,
        (
            "#11Pアンタらならきっと、\x01",
            "あの偏屈ジジイの心を開いて\x01",
            "無事、新作人形を受け取れるさね！\x02",
        )
    )

    CloseMessageWindow()

    #C0437
    ChrTalk(
        0x101,
        (
            "#6P#0006Fう、うーん……\x02\x03",

            "#0008F（……でも人形工房か。\x01",
            "  レンの事も気になるし……）\x02\x03",

            "（キーア絡みでも\x01",
            "  気にはなっていたけど……）\x02",
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
            "#6P#0003F──他の任務もありますし、\x01",
            "確約まではできませんが……\x02\x03",

            "#0000Fそれでよかったら\x01",
            "一応、承っておきます。\x02",
        )
    )

    CloseMessageWindow()

    #C0439
    ChrTalk(
        0x8,
        "#11Pああもう、それでいいさ！\x02",
    )

    CloseMessageWindow()

    #C0440
    ChrTalk(
        0x8,
        (
            "#11Pとにかく一切合財\x01",
            "アンタらに任せたよ！\x02",
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
            "クエスト【新作人形の受け取り】\x07\x00",
            "を開始した！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    SetChrPos(0x0, -750, 0, 2000, 0)
    OP_29(0x30, 0x4, 0x2)
    Return()

    # Function_22_78C7 end

    def Function_23_82F0(): pass

    label("Function_23_82F0")

    EventBegin(0x1)
    OP_63(0x8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0442
    ChrTalk(
        0x8,
        (
            "おお！\x01",
            "そのトランクは……\x02",
        )
    )

    CloseMessageWindow()

    #C0443
    ChrTalk(
        0x101,
        (
            "#0000F一応、ヨルグさんから\x01",
            "こちらを預かってきました。\x02",
        )
    )

    CloseMessageWindow()

    #C0444
    ChrTalk(
        0x102,
        "#0100Fどうかご確認ください。\x02",
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
            "#2Pヒヒャヒャ！\x01",
            "確かにヨルグの新作だ！\x02",
        )
    )

    CloseMessageWindow()

    #C0446
    ChrTalk(
        0x8,
        (
            "#2Pあんたたち、\x01",
            "よく説得してくれたねぇ！\x02",
        )
    )

    CloseMessageWindow()

    #C0447
    ChrTalk(
        0x104,
        (
            "#6P#0309Fいや～、説得したっつーか、\x01",
            "根性で当たったっつーか。\x02",
        )
    )

    CloseMessageWindow()

    #C0448
    ChrTalk(
        0x102,
        (
            "#6P#0104Fでも……相変わらず\x01",
            "素晴らしい人形ですね。\x02\x03",

            "#0102F友人のところでも\x01",
            "何体か見ていますけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0449
    ChrTalk(
        0x103,
        "#6P#0202Fため息が出てしまいます……\x02",
    )

    CloseMessageWindow()

    #C0450
    ChrTalk(
        0x101,
        (
            "#6P#0004F確かに芸術品ですね……\x02\x03",

            "#0005F……でも、てっきりキーアと\x01",
            "同じくらいの大きさかと思ったけど。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB1, 5)), scpexpr(EXPR_END)), "loc_864C")

    #C0451
    ChrTalk(
        0x8,
        (
            "#2P以前ここに連れて来た\x01",
            "あの愉快な嬢ちゃんだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0452
    ChrTalk(
        0x8,
        (
            "#2P確かに、あの子くらいの大きさの\x01",
            "ローゼンベルク人形もあるんだ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_86D0")

    label("loc_864C")


    #C0453
    ChrTalk(
        0x8,
        (
            "#2Pアンタらが引き取ったっていう\x01",
            "競売会に紛れてた子供だね。\x02",
        )
    )

    CloseMessageWindow()

    #C0454
    ChrTalk(
        0x8,
        (
            "#2P確かに、子供くらいの大きさの\x01",
            "ローゼンベルク人形もあるんだ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_86D0")


    #C0455
    ChrTalk(
        0x8,
        (
            "#2Pヨルグも滅多に作らないから\x01",
            "殆んど出回らないそうだがね。\x02",
        )
    )

    CloseMessageWindow()

    #C0456
    ChrTalk(
        0x8,
        (
            "#2Pだからこそ競売会では\x01",
            "途方もない値が付きそうだと\x01",
            "噂されていたワケだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0457
    ChrTalk(
        0x102,
        (
            "#6P#0104F普通に出回っているのは\x01",
            "大体このくらいの大きさかしら。\x02\x03",

            "#0100Fベルの所にあったのも\x01",
            "同じくらいのサイズだったし。\x02",
        )
    )

    CloseMessageWindow()

    #C0458
    ChrTalk(
        0x101,
        (
            "#6P#0003Fなるほど……\x02\x03",

            "#0001F……しかしイメルダさん。\x02\x03",

            "あの工房で作られている\x01",
            "“他の人形”はご存知なんですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0459
    ChrTalk(
        0x8,
        "#2P他の人形？\x02",
    )

    CloseMessageWindow()

    #C0460
    ChrTalk(
        0x104,
        (
            "#6P#0306Fなんつーか、勝手に動きまくる\x01",
            "デカイ人形なんだけどよ。\x02\x03",

            "#0301F天使だの、デカイ顔だの。\x02",
        )
    )

    CloseMessageWindow()

    #C0461
    ChrTalk(
        0x8,
        (
            "#2Pああ、歯車仕掛けの\x01",
            "自動人形#8Rオ ー ト マ タ#のことかい。\x02",
        )
    )

    CloseMessageWindow()

    #C0462
    ChrTalk(
        0x8,
        (
            "#2Pどちらかというと\x01",
            "そちらの方が専門らしいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0463
    ChrTalk(
        0x8,
        (
            "#2P最近じゃ導力化させて\x01",
            "より精巧に動くらしいが。\x02",
        )
    )

    CloseMessageWindow()

    #C0464
    ChrTalk(
        0x102,
        "#6P#0105Fご、ご存知だったんですか？\x02",
    )

    CloseMessageWindow()

    #C0465
    ChrTalk(
        0x8,
        (
            "#2Pご存知も何も……\x01",
            "あの《アルカンシェル》でも\x01",
            "舞台装置として使っているよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0466
    ChrTalk(
        0x8,
        (
            "#2P今度の新作じゃ、槍を持った兵士が\x01",
            "自動人形だったはずだけどね。\x02",
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
            "#6P#0011Fええっ！？\x01",
            "あの槍を回していた……\x02",
        )
    )

    CloseMessageWindow()

    #C0468
    ChrTalk(
        0x102,
        "#6P#0101F本当ですか……！？\x02",
    )

    CloseMessageWindow()

    #C0469
    ChrTalk(
        0x8,
        (
            "#2Pああ、それ以外にも\x01",
            "複雑な舞台装置のほとんどは\x01",
            "あの工房に発注してるそうだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0470
    ChrTalk(
        0x8,
        (
            "#2P照明やら、水の制御やら\x01",
            "ワイヤーアクションの装置やら。\x02",
        )
    )

    CloseMessageWindow()

    #C0471
    ChrTalk(
        0x8,
        (
            "#2P世間じゃあんまり\x01",
            "知られてないみたいだけどね。\x02",
        )
    )

    CloseMessageWindow()

    #C0472
    ChrTalk(
        0x104,
        "#6P#0305Fなんとまあ……\x02",
    )

    CloseMessageWindow()

    #C0473
    ChrTalk(
        0x103,
        (
            "#6P#0201F確かにかなりの技術を使った\x01",
            "舞台装置だとは思いましたが……\x02\x03",

            "#0208Fとなると、あの天使や化物も\x01",
            "そうしたギミックの一種……？\x02",
        )
    )

    CloseMessageWindow()

    #C0474
    ChrTalk(
        0x8,
        (
            "#2Pま、人嫌いで偏屈で\x01",
            "色々と謎の多いジジイだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0475
    ChrTalk(
        0x8,
        (
            "#2Pたまに新作を出して\x01",
            "こっちを儲けさせてくれりゃあ\x01",
            "アタシとしては文句はないさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0476
    ChrTalk(
        0x8,
        (
            "#2P──アンタたちもご苦労だった。\x01",
            "また何かあったらよろしく頼むよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0477
    ChrTalk(
        0x101,
        "#6P#0005Fあ……はい。\x02",
    )

    CloseMessageWindow()

    #C0478
    ChrTalk(
        0x102,
        (
            "#6P#0100Fえっと……\x01",
            "それでは失礼します。\x02",
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
            "クエスト【新作人形の受け取り】\x07\x00",
            "を達成した！\x02",
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

    # Function_23_82F0 end

    def Function_24_8E8B(): pass

    label("Function_24_8E8B")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8FE4")
    SetChrName("")

    #A0480
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "精巧な人形たちが並べられている。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x50, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8FE4")

    #C0481
    ChrTalk(
        0x101,
        (
            "#0005Fへえ、アンティークドール\x01",
            "なんかも並んでるんだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0482
    ChrTalk(
        0x103,
        (
            "#0200F精巧な作りですね。\x01",
            "まるで美術品みたいです。\x02",
        )
    )

    CloseMessageWindow()

    #C0483
    ChrTalk(
        0x104,
        (
            "#0304Fはー、すげえもんだな。\x01",
            "値段も相当するみてえだが。\x02",
        )
    )

    CloseMessageWindow()

    #C0484
    ChrTalk(
        0x102,
        (
            "#0100Fまさにアンティークショップね。\x02\x03",

            "#0103F（でも“あの人形”じゃ\x01",
            "  ないみたいね……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x50, 4)

    label("loc_8FE4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_92B0")
    SetChrName("")

    #A0485
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "精巧な人形たちが並べられている。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x50, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_92B0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x50, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_90A6")

    #C0486
    ChrTalk(
        0x101,
        (
            "#0000Fへえ、凄い精巧な\x01",
            "アンティークドールだな……\x02\x03",

            "#0005Fあ、もしかして\x01",
            "山道の方にあった人形工房の……？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9111")

    label("loc_90A6")


    #C0487
    ChrTalk(
        0x101,
        (
            "#0000F精巧なアンティークドール……\x02\x03",

            "#0005Fあ、もしかしてこの人形って\x01",
            "山道の方にあった人形工房の……？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9111")


    #C0488
    ChrTalk(
        0x102,
        (
            "#0103Fいいえ、ローゼンベルク工房の\x01",
            "物じゃないと思うわ。\x02\x03",

            "#0100Fあそこの人形はもっと凄いから。\x02",
        )
    )

    CloseMessageWindow()

    #C0489
    ChrTalk(
        0x104,
        (
            "#0300Fはー、そうなのか。\x02\x03",

            "#0301F……つーかお嬢、\x01",
            "やけに詳しいじゃねえか。\x02\x03",

            "まさか持ってたりするのかよ？\x02",
        )
    )

    CloseMessageWindow()

    #C0490
    ChrTalk(
        0x102,
        (
            "#0104Fあはは……私じゃなくて\x01",
            "知り合いがね。\x02\x03",

            "#0100Fその影響で何体か\x01",
            "見た事があるのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0491
    ChrTalk(
        0x103,
        (
            "#0200Fそうでしたか。\x02\x03",

            "ローゼンベルク製の人形……\x01",
            "素晴らしい出来だそうですが\x01",
            "一度実物を見てみたいものです。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x50, 5)

    label("loc_92B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_9323")
    SetChrName("")

    #A0492
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "精巧な人形たちが並べられている。\x02\x03",

            "いい値段が付けられているが\x01",
            "ローゼンベルク製ではないようだ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_9323")

    TalkEnd(0xFF)
    Return()

    # Function_24_8E8B end

    SaveToFile()

Try(main)
