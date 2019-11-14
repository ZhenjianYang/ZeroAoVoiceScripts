from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "c0210.bin",                # FileName
        "c0210",                    # MapName
        "c0210",                    # Location
        0x000B,                     # MapIndex
        "ed7100",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 11, 0, 2, 0, 3],
    )

    BuildStringList((
        "c0210",                  # 0
        "奥斯卡",                 # 1
        "摩尔吉",                 # 2
        "贝奈特",                 # 3
        "卡缇莉娜",               # 4
        "游客",                   # 5
        "游客",                   # 6
        "游击士艾欧莉娅",         # 7
        "塔利兹",                 # 8
        "爱尔莎",                 # 9
        "小桃",                   # 10
        "皮特",                   # 11
        "布里吉塔",               # 12
        "蔡特",                   # 13
        "哈罗德",                 # 14
    ))

    AddCharChip((
        "chr/ch07000.itc",                   # 00
        "chr/ch25000.itc",                   # 01
        "chr/ch34300.itc",                   # 02
        "chr/ch24500.itc",                   # 03
        "chr/ch21600.itc",                   # 04
        "chr/ch21100.itc",                   # 05
        "chr/ch24800.itc",                   # 06
        "chr/ch10400.itc",                   # 07
        "chr/ch20700.itc",                   # 08
        "chr/ch22200.itc",                   # 09
        "chr/ch20300.itc",                   # 0A
        "chr/ch02707.itc",                   # 0B
        "chr/ch09300.itc",                   # 0C
        "chr/ch32100.itc",                   # 0D
    ))

    DeclNpc(56290,   0,       2019,    270,  261,  0x0, 0,   0,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(119120,  0,       -660,    275,  261,  0x0, 0,   1,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(51279,   1000,    12869,   90,   261,  0x0, 0,   2,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(58540,   0,       -2329,   0,    261,  0x0, 0,   3,   0,   0,   0,   0,   13,  255,  0)
    DeclNpc(53500,   0,       5010,    90,   389,  0x0, 0,   4,   0,   0,   0,   0,   14,  255,  0)
    DeclNpc(53500,   0,       6010,    90,   389,  0x0, 0,   5,   0,   0,   0,   0,   15,  255,  0)
    DeclNpc(57319,   0,       -1980,   0,    389,  0x0, 0,   13,  0,   0,   0,   0,   24,  255,  0)
    DeclNpc(200,     0,       8500,    180,  261,  0x0, 0,   6,   0,   0,   0,   0,   17,  255,  0)
    DeclNpc(-65370,  0,       2009,    90,   261,  0x0, 0,   7,   0,   0,   0,   0,   18,  255,  0)
    DeclNpc(3089,    0,       4199,    90,   261,  0x0, 0,   8,   0,   0,   0,   0,   19,  255,  0)
    DeclNpc(-3630,   0,       3509,    270,  389,  0x0, 0,   9,   0,   0,   0,   0,   20,  255,  0)
    DeclNpc(-3569,   0,       2450,    270,  389,  0x0, 0,   10,  0,   0,   0,   0,   21,  255,  0)
    DeclNpc(2589,    0,       1320,    225,  404,  0x0, 0,   11,  0,   0,   0,   0,   22,  255,  0)
    DeclNpc(2089,    0,       2250,    0,    389,  0x0, 0,   12,  0,   0,   0,   0,   23,  255,  0)

    DeclActor(54900,   0,       1720,    1000,    56290,   1500,    2020,    0x007E, 0,  4,  0x0000)
    DeclActor(300,     0,       6960,    1000,    200,     1500,    8500,    0x007E, 0,  16, 0x0000)

    ScpFunction((
        "Function_0_324",          # 00, 0
        "Function_1_3DC",          # 01, 1
        "Function_2_407",          # 02, 2
        "Function_3_89C",          # 03, 3
        "Function_4_91C",          # 04, 4
        "Function_5_936",          # 05, 5
        "Function_6_FA2",          # 06, 6
        "Function_7_39AA",         # 07, 7
        "Function_8_3D4F",         # 08, 8
        "Function_9_3E7B",         # 09, 9
        "Function_10_4E4E",        # 0A, 10
        "Function_11_4F33",        # 0B, 11
        "Function_12_5C80",        # 0C, 12
        "Function_13_5DB6",        # 0D, 13
        "Function_14_6A3C",        # 0E, 14
        "Function_15_6B2E",        # 0F, 15
        "Function_16_6C99",        # 10, 16
        "Function_17_6C9D",        # 11, 17
        "Function_18_83CC",        # 12, 18
        "Function_19_8D5D",        # 13, 19
        "Function_20_951D",        # 14, 20
        "Function_21_96A9",        # 15, 21
        "Function_22_9906",        # 16, 22
        "Function_23_99AC",        # 17, 23
        "Function_24_9C10",        # 18, 24
        "Function_25_9D79",        # 19, 25
        "Function_26_9E1E",        # 1A, 26
        "Function_27_A858",        # 1B, 27
        "Function_28_A98E",        # 1C, 28
        "Function_29_AA78",        # 1D, 29
        "Function_30_AFCF",        # 1E, 30
        "Function_31_B417",        # 1F, 31
        "Function_32_B8CA",        # 20, 32
        "Function_33_BC68",        # 21, 33
    ))


    def Function_0_324(): pass

    label("Function_0_324")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_364"),
        (1, "loc_370"),
        (2, "loc_37C"),
        (3, "loc_388"),
        (4, "loc_394"),
        (5, "loc_3A0"),
        (6, "loc_3AC"),
        (SWITCH_DEFAULT, "loc_3B8"),
    )


    label("loc_364")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_3C4")

    label("loc_370")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_3C4")

    label("loc_37C")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_3C4")

    label("loc_388")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_3C4")

    label("loc_394")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_3C4")

    label("loc_3A0")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_3C4")

    label("loc_3AC")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_3C4")

    label("loc_3B8")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_3C4")

    label("loc_3C4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3DB")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_3C4")

    label("loc_3DB")

    Return()

    # Function_0_324 end

    def Function_1_3DC(): pass

    label("Function_1_3DC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_406")
    OP_94(0xFE, 0xFFFEEFB2, 0x19A, 0xFFFEF926, 0xBE0, 0x3E8)
    Sleep(300)
    Jump("Function_1_3DC")

    label("loc_406")

    Return()

    # Function_1_3DC end

    def Function_2_407(): pass

    label("Function_2_407")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x46, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_422")
    SetMapFlags(0x10000000)
    Event(0, 26)

    label("loc_422")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_44C")
    SetChrFlags(0xA, 0x80)
    SetChrPos(0x11, -68430, 0, 1820, 180)
    BeginChrThread(0x11, 0, 0, 1)
    Jump("loc_89B")

    label("loc_44C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_497")
    SetChrPos(0x9, 51330, 1000, 13550, 90)
    SetChrPos(0xA, 120860, 0, 2360, 0)
    SetChrPos(0x10, 3090, 0, 4200, 90)
    SetChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    Jump("loc_89B")

    label("loc_497")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_4E2")
    SetChrPos(0x8, 122290, 0, -2810, 90)
    SetChrPos(0x9, 56290, 0, 2020, 270)
    SetChrPos(0xA, 120860, 0, 2360, 0)
    SetChrFlags(0x11, 0x80)
    ClearChrFlags(0x13, 0x80)
    Jump("loc_89B")

    label("loc_4E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_528")
    SetChrPos(0x9, 51330, 1000, 13550, 90)
    SetChrPos(0xA, 119120, 0, -660, 275)
    SetChrPos(0x10, 3090, 0, 4200, 90)
    SetChrFlags(0x11, 0x80)
    Jump("loc_89B")

    label("loc_528")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_587")
    SetChrPos(0x9, 51330, 1000, 13550, 90)
    SetChrPos(0xA, 119120, 0, -660, 275)
    SetChrFlags(0x10, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBD, 2)), scpexpr(EXPR_END)), "loc_56B")
    SetChrFlags(0x11, 0x80)
    Jump("loc_582")

    label("loc_56B")

    SetChrPos(0x11, -68430, 0, 1820, 180)
    BeginChrThread(0x11, 0, 0, 1)

    label("loc_582")

    Jump("loc_89B")

    label("loc_587")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_5B8")
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    ClearChrFlags(0xE, 0x80)
    Jump("loc_89B")

    label("loc_5B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_5EB")
    SetChrPos(0x9, 51330, 1000, 13550, 90)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    Jump("loc_89B")

    label("loc_5EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_61E")
    SetChrPos(0x9, 51330, 1000, 13550, 90)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    Jump("loc_89B")

    label("loc_61E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_651")
    SetChrPos(0x9, 51330, 1000, 13550, 90)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    Jump("loc_89B")

    label("loc_651")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_6A0")
    SetChrPos(0x9, 120860, 0, 2360, 0)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrPos(0x11, -68430, 0, 1820, 180)
    BeginChrThread(0x11, 0, 0, 1)
    Jump("loc_89B")

    label("loc_6A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_6C7")
    SetChrFlags(0xA, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    Jump("loc_89B")

    label("loc_6C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_70D")
    SetChrPos(0x9, 51330, 1000, 13550, 90)
    SetChrPos(0xA, 119120, 0, -660, 275)
    SetChrPos(0x11, -72880, 0, 6950, 0)
    ClearChrFlags(0x13, 0x80)
    Jump("loc_89B")

    label("loc_70D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_775")
    SetChrPos(0x9, 119050, 0, -140, 180)
    SetChrPos(0xA, 119050, 0, -1650, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_75A")
    SetChrPos(0x11, -72880, 0, 6950, 0)
    Jump("loc_770")

    label("loc_75A")

    SetChrPos(0x11, 2240, 0, 2350, 180)
    ClearChrFlags(0x14, 0x80)

    label("loc_770")

    Jump("loc_89B")

    label("loc_775")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_799")
    SetChrPos(0xA, 55920, 1000, 10640, 90)
    SetChrFlags(0x11, 0x80)
    Jump("loc_89B")

    label("loc_799")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_7BD")
    SetChrPos(0xA, 55920, 1000, 10640, 90)
    SetChrFlags(0x11, 0x80)
    Jump("loc_89B")

    label("loc_7BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_7F7")
    SetChrPos(0xA, 55170, 1000, 14200, 270)
    SetChrPos(0x10, 2090, 0, 3530, 180)
    SetChrFlags(0x11, 0x80)
    ClearChrFlags(0x15, 0x80)
    Jump("loc_89B")

    label("loc_7F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_820")
    SetChrPos(0xA, 55170, 1000, 14200, 270)
    SetChrFlags(0x11, 0x80)
    ClearChrFlags(0x13, 0x80)
    Jump("loc_89B")

    label("loc_820")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_855")
    SetChrPos(0xA, 55170, 1000, 14200, 270)
    SetChrPos(0x9, 120860, 0, 2360, 0)
    SetChrFlags(0x11, 0x80)
    Jump("loc_89B")

    label("loc_855")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_88D")
    SetChrFlags(0x10, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 6)), scpexpr(EXPR_END)), "loc_888")
    SetChrPos(0x11, -68430, 0, 1820, 180)
    BeginChrThread(0x11, 0, 0, 1)
    ClearChrFlags(0x12, 0x80)

    label("loc_888")

    Jump("loc_89B")

    label("loc_88D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_89B")
    SetChrFlags(0x10, 0x80)

    label("loc_89B")

    Return()

    # Function_2_407 end

    def Function_3_89C(): pass

    label("Function_3_89C")

    OP_52(0x14, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8DC")
    OP_10(0x0, 0x0)
    OP_10(0x2, 0x1)
    OP_10(0x1, 0x0)
    OP_10(0x3, 0x1)
    Jump("loc_8E8")

    label("loc_8DC")

    OP_10(0x0, 0x1)
    OP_10(0x2, 0x0)
    OP_10(0x1, 0x1)
    OP_10(0x3, 0x0)

    label("loc_8E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_904")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    Jump("loc_91B")

    label("loc_904")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_91B")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    Jump("loc_91B")

    label("loc_91B")

    Return()

    # Function_3_89C end

    def Function_4_91C(): pass

    label("Function_4_91C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_932")
    Call(0, 5)
    Jump("loc_935")

    label("loc_932")

    Call(0, 8)

    label("loc_935")

    Return()

    # Function_4_91C end

    def Function_5_936(): pass

    label("Function_5_936")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6, 0x1, 0x0)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_962")
    OP_4B(0x8, 0xFF)
    TurnDirection(0x0, 0x8, 0)
    Call(0, 29)
    Return()

    label("loc_962")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6, 0x1, 0x0)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x12D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x12F, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A62")

    #C0001
    ChrTalk(
        0x8,
        (
            "罗伊德，收集食材的事情\x01",
            "怎么样了？\x02",
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
            "【交出收集的食材】\x01",      # 0
            "【放弃】\x01",                # 1
        )
    )

    MenuEnd(0x0)
    FadeToBright(300, 0)
    OP_60(0x0)
    OP_5A()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_A20"),
        (1, "loc_A27"),
        (SWITCH_DEFAULT, "loc_A62"),
    )


    label("loc_A20")

    Call(0, 30)
    TalkEnd(0x8)
    Return()

    label("loc_A27")


    #C0002
    ChrTalk(
        0x8,
        (
            "那就下次吧，\x01",
            "等你办妥之后再来找我。\x01",
            "拜托你们啦！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A62")

    label("loc_A62")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_F9B")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6, 0x1, 0x0)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E87")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A97")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E82")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "对话\x01",                # 0
            "购物\x01",                # 1
            "询问委托的事情\x01",      # 2
            "放弃\x01",                # 3
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_AF6")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_AF6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B76")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_B15")
    OP_AF(0xCE)
    Jump("loc_B67")

    label("loc_B15")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_B25")
    OP_AF(0xCD)
    Jump("loc_B67")

    label("loc_B25")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_B35")
    OP_AF(0xCC)
    Jump("loc_B67")

    label("loc_B35")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_B45")
    OP_AF(0xCB)
    Jump("loc_B67")

    label("loc_B45")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_B55")
    OP_AF(0xCA)
    Jump("loc_B67")

    label("loc_B55")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_B65")
    OP_AF(0xC9)
    Jump("loc_B67")

    label("loc_B65")

    OP_AF(0xC8)

    label("loc_B67")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_E7D")

    label("loc_B76")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E4D")

    #C0003
    ChrTalk(
        0x8,
        (
            "我希望你们收集的是\x01",
            "四个『魔兽鱼肉』\x01",
            "和三个『魔兽之卵』。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x8,
        (
            "食材好像不太够啊，\x01",
            "忙其它事情的时候顺便\x01",
            "帮我收集一下就可以啦。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x71, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D4E")

    #C0005
    ChrTalk(
        0x104,
        (
            "#0304F『魔兽鱼肉』一般可以在\x01",
            "鱼形魔兽的身上得到。\x02\x03",

            "而『魔兽之卵』则会从\x01",
            "鸟形或蛇形的魔兽身上掉落。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x101,
        (
            "#0000F哦，兰迪果然对这些\x01",
            "很熟悉啊。\x01",
            "真不愧是原警备队员。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x104,
        (
            "#0300F哈哈，战斗之类的事情，\x01",
            "我早就习惯啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x102,
        (
            "#0100F魔兽所掉落的食材，\x01",
            "也能用于制作料理哦。\x02\x03",

            "趁这个机会记住，\x01",
            "以后探索时也会轻松许多。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x71, 7)
    Jump("loc_E3E")

    label("loc_D4E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x12D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x12F, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E3E")

    #C0009
    ChrTalk(
        0x104,
        (
            "#0300F『魔兽鱼肉』是鱼形魔兽掉落的，\x01",
            "『魔兽之卵』可以从鸟形或蛇形的魔兽\x01",
            "身上得到。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x101,
        (
            "#0000F总之，只要在郊外多转转，\x01",
            "就能收集到这些东西。\x02\x03",

            "#0004F好，那我们这就\x01",
            "开始收集吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x8,
        "哇哈哈，那就拜托你们啦！\x02",
    )

    CloseMessageWindow()

    label("loc_E3E")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_E7D")

    label("loc_E4D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E61")
    Jump("loc_E7D")

    label("loc_E61")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E7D")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 6)

    label("loc_E7D")

    Jump("loc_A97")

    label("loc_E82")

    Jump("loc_F96")

    label("loc_E87")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_E91")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F96")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_EE1")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_EE1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F61")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_F00")
    OP_AF(0xCE)
    Jump("loc_F52")

    label("loc_F00")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_F10")
    OP_AF(0xCD)
    Jump("loc_F52")

    label("loc_F10")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_F20")
    OP_AF(0xCC)
    Jump("loc_F52")

    label("loc_F20")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_F30")
    OP_AF(0xCB)
    Jump("loc_F52")

    label("loc_F30")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_F40")
    OP_AF(0xCA)
    Jump("loc_F52")

    label("loc_F40")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_F50")
    OP_AF(0xC9)
    Jump("loc_F52")

    label("loc_F50")

    OP_AF(0xC8)

    label("loc_F52")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_F91")

    label("loc_F61")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F75")
    Jump("loc_F91")

    label("loc_F75")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F91")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 6)

    label("loc_F91")

    Jump("loc_E91")

    label("loc_F96")

    Jump("loc_F9E")

    label("loc_F9B")

    Call(0, 6)

    label("loc_F9E")

    TalkEnd(0x8)
    Return()

    # Function_5_936 end

    def Function_6_FA2(): pass

    label("Function_6_FA2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_END)), "loc_1020")

    #C0012
    ChrTalk(
        0x8,
        (
            "今天真是得救了。\x01",
            "你们就顺便尝尝\x01",
            "我烤的面包吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x8,
        "呵呵，免费赠送哦。\x02",
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x101,
        "#0000F谢啦，那就让我选一点吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_39A9")

    label("loc_1020")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_134B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xED, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12C5")

    #C0015
    ChrTalk(
        0x8,
        (
            "哟，罗伊德，\x01",
            "你还在调查什么案子吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x101,
        (
            "#0000F嗯，差不多吧。\x02\x03",

            "#0001F……奥斯卡，为求谨慎，\x01",
            "我想问你这附近\x01",
            "有没有发生什么奇怪的事？\x02\x03",

            "比如看见一些黑衣人什么的……\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x8,
        "奇怪的事啊……嗯～\x02",
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x8,
        (
            "其实，贝奈特刚才\x01",
            "突然很生气，\x01",
            "然后就跑出去了。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x8,
        "到底发生了什么事呢？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xED, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_120C")
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0020
    ChrTalk(
        0x101,
        (
            "#0006F你啊，真是的，\x01",
            "对这方面太迟钝了吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x102,
        (
            "#0100F西街附近好像\x01",
            "没什么事件发生吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12BD")

    label("loc_120C")

    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0022
    ChrTalk(
        0x101,
        (
            "#0000F不、不太清楚呢……\x02\x03",

            "但说不定是奥斯卡的错吧？\x01",
            "你有时的确很迟钝……\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x8,
        "哎，是吗？\x02",
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x102,
        (
            "#0100F（嗯，西街一带好像\x01",
            "　没发生什么特别的事件。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12BD")

    SetScenarioFlags(0xED, 2)
    Jump("loc_1346")

    label("loc_12C5")


    #C0025
    ChrTalk(
        0x8,
        (
            "贝奈特今天\x01",
            "烤了很美味的面包\x01",
            "给我吃呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x8,
        (
            "然后，我坦率地说出了想法后，\x01",
            "她就突然生气地跑出去了。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x8,
        "唔，到底是怎么了啊？\x02",
    )

    CloseMessageWindow()

    label("loc_1346")

    Jump("loc_39A9")

    label("loc_134B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_143B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13F7")

    #C0028
    ChrTalk(
        0x8,
        (
            "昨天，在港湾区那边\x01",
            "好像发生了枪击事件吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x8,
        (
            "黑手党如果认真起来，\x01",
            "就会毫无顾忌地展开争斗，\x01",
            "将市民都牵连进去……\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x8,
        "真是群棘手的家伙啊。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1436")

    label("loc_13F7")


    #C0031
    ChrTalk(
        0x8,
        (
            "难得店里的营业额\x01",
            "刚刚有起色呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x8,
        "希望不要碰到麻烦事。\x02",
    )

    CloseMessageWindow()

    label("loc_1436")

    Jump("loc_39A9")

    label("loc_143B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_1583")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_154D")
    OP_93(0x8, 0x5A, 0x0)

    #C0033
    ChrTalk(
        0x8,
        "那个，毛毯在哪里啊……？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x0, 500)

    #C0034
    ChrTalk(
        0x8,
        (
            "贝奈特为了研究新面包的烤制方法，\x01",
            "几乎都没有睡过觉。\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x8,
        (
            "哈哈，还真是费事啊，\x01",
            "就像小时候那个一直\x01",
            "被塞茜尔小姐照顾的罗伊德一样。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0036
    ChrTalk(
        0x101,
        (
            "#0003F不、不要突然\x01",
            "提起过去的事情啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_157E")

    label("loc_154D")


    #C0037
    ChrTalk(
        0x8,
        (
            "哎呀呀，先得把她带回房去，\x01",
            "免得她生病着凉。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_157E")

    Jump("loc_39A9")

    label("loc_1583")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_187B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1818")

    #C0038
    ChrTalk(
        0x8,
        (
            "罗伊德，你们好啊。\x01",
            "今天带稀客来了啊？\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x101,
        (
            "#0000F嗯，这位是警备队的\x01",
            "诺艾尔上士。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x109,
        (
            "#0500F呵呵，初次见面。\x02\x03",

            "话说……\x01",
            "我听芙兰提起过\x01",
            "这家名叫『摩尔吉』的面包店。\x02\x03",

            "据说有位年轻的天才面包师，\x01",
            "还曾被杂志报道过呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x8,
        "哦，是指那次的采访啊……\x02",
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x104,
        (
            "#0300F好厉害啊，竟然能\x01",
            "接受杂志的采访。\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x103,
        (
            "#0200F不过，这家店的面包确实很美味，\x01",
            "会被杂志报道也并不奇怪。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x8,
        (
            "呵呵，我也还在学习中，\x01",
            "所以对这种事不是很感兴趣。\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x8,
        (
            "不过师傅倒是很热衷，\x01",
            "而且也有助于提高营业额，\x01",
            "所以就勉强接受了采访。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x8,
        (
            "结果拜其所赐，研制这个月的面包新品\x01",
            "让我很有压力呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x101,
        "#0000F哈哈，你还真会说。\x02",
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x102,
        (
            "#0100F呵呵，既然如此，\x01",
            "那我们也来尝尝那个新品面包吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xCD, 3)
    Jump("loc_1876")

    label("loc_1818")


    #C0049
    ChrTalk(
        0x8,
        (
            "我哪里是什么天才啊，\x01",
            "和师傅比起来还差得很远。\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x8,
        (
            "技术方面也有很多东西\x01",
            "需要贝奈特教我。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1876")

    Jump("loc_39A9")

    label("loc_187B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_1A20")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAD, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18A1")
    Call(0, 7)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    label("loc_18A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19D0")

    #C0051
    ChrTalk(
        0x153,
        (
            "#1110F这里的味道好香啊！\x01",
            "大哥哥，你是做什么的～？\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x8,
        "噢，我是面包师哦。\x02",
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x8,
        (
            "小琪雅要不要也来一个啊？\x01",
            "我们的面包很好吃哦～\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x153,
        "#1109F嗯，我要吃～！\x02",
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x101,
        (
            "#0006F喂喂……\x01",
            "别不经过我就擅自决定啊。\x02\x03",

            "#0000F（不过，她好像不认得\x01",
            "　这家面包店啊。）\x02\x03",

            "（果然不是\x01",
            "　克洛斯贝尔出身吧……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1A1B")

    label("loc_19D0")


    #C0056
    ChrTalk(
        0x8,
        (
            "罗伊德，给小琪雅\x01",
            "买点什么吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x8,
        (
            "我推荐\x01",
            "限时供应的\x01",
            "甜蜜牛奶面包哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A1B")

    Jump("loc_39A9")

    label("loc_1A20")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_1C6E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAD, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C09")

    #C0058
    ChrTalk(
        0x8,
        (
            "听说已经找到\x01",
            "那个男孩子了？\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x8,
        (
            "哈，真是太好了。\x01",
            "参加纪念庆典的人那么多，\x01",
            "做父母的一定会很担心吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x101,
        "#0000F嗯，他们非常担心呢。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0061
    ChrTalk(
        0x101,
        (
            "#0005F话说回来，奥斯卡。\x02\x03",

            "#0000F你去过『米修拉姆』\x01",
            "这个地方吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0062
    ChrTalk(
        0x8,
        "很不巧，没去过。\x02",
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x8,
        (
            "听说是什么主题公园，\x01",
            "不过我没什么兴趣呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x8,
        (
            "温蒂似乎倒是\x01",
            "去那里玩过好几次。\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x101,
        "#0000F这样啊……\x02",
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x8,
        (
            "据说那里是\x01",
            "非常受欢迎的度假地哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x8,
        (
            "已经成为了约会和\x01",
            "家庭出游的必选之地了呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xAD, 4)
    Jump("loc_1C69")

    label("loc_1C09")


    #C0068
    ChrTalk(
        0x8,
        (
            "对了，师傅要在今天下午\x01",
            "给我放假呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x8,
        (
            "我对主题公园没什么兴趣，\x01",
            "还是在市内随便逛逛好了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C69")

    Jump("loc_39A9")

    label("loc_1C6E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 7)), scpexpr(EXPR_END)), "loc_1DA4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D55")

    #C0070
    ChrTalk(
        0x8,
        (
            "哟，罗伊德，是你们啊。\x01",
            "找到那个男孩了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x101,
        (
            "#0001F不，我们还在找，\x01",
            "不过已经有线索了，\x01",
            "别担心。\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0x8,
        "是吗，那真是太好了。\x02",
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0x8,
        (
            "他现在可能很害怕呢，\x01",
            "所以要赶紧找到他才行！\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x160,
        "#3300F……嗯，是啊。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1D9F")

    label("loc_1D55")


    #C0075
    ChrTalk(
        0x8,
        (
            "还好已经有\x01",
            "线索了。\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x8,
        (
            "他现在可能很害怕呢，\x01",
            "所以要赶紧找到他才行！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D9F")

    Jump("loc_39A9")

    label("loc_1DA4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_1FE7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAC, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F96")

    #C0077
    ChrTalk(
        0x8,
        "哦，这不是罗伊德嘛。\x02",
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0x8,
        (
            "带着那么可爱的小姑娘，\x01",
            "在干什么呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0x101,
        (
            "#0003F啊，只是\x01",
            "正在找人……\x02\x03",

            "#0001F奥斯卡，你见过\x01",
            "这张照片上的孩子吗？\x02",
        )
    )

    CloseMessageWindow()

    #A0080
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

    #C0081
    ChrTalk(
        0x8,
        (
            "咦，这孩子\x01",
            "不是柯林吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x101,
        "#0005F哎，你认识他吗？\x02",
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x8,
        "嗯，是住在住宅街的孩子吧？\x02",
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x8,
        (
            "他们一家人\x01",
            "偶尔会一起来买面包呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0x8,
        (
            "只是……\x01",
            "今天没有见过他。\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x8,
        (
            "去看游行的时候，\x01",
            "在西街也没见到过。\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x101,
        (
            "#0000F果然是这样啊……\x01",
            "谢啦，真是帮大忙了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xAC, 7)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 25)
    Jump("loc_1FE2")

    label("loc_1F96")


    #C0088
    ChrTalk(
        0x8,
        (
            "这孩子我认识，\x01",
            "不过今天没有见过。\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0x8,
        (
            "至少他没有从\x01",
            "我们店门前经过呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1FE2")

    Jump("loc_39A9")

    label("loc_1FE7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_20B7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2067")

    #C0090
    ChrTalk(
        0x8,
        (
            "欢迎光临……\x01",
            "罗伊德，是你们啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x8,
        (
            "今天我一整天\x01",
            "都要烤面包。\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0x8,
        (
            "没想到竟然\x01",
            "会有这么多人啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_20B2")

    label("loc_2067")


    #C0093
    ChrTalk(
        0x8,
        "今年的人流真是格外壮观啊。\x02",
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x8,
        (
            "师傅说，他也是\x01",
            "第一次见到那么多人呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_20B2")

    Jump("loc_39A9")

    label("loc_20B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_211D")

    #C0095
    ChrTalk(
        0x8,
        (
            "游行队伍好像\x01",
            "也会经过我们店门口哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0x8,
        (
            "希望不要有人因为太过兴奋\x01",
            "而不小心受伤啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_39A9")

    label("loc_211D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_21D3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_217B")

    #C0097
    ChrTalk(
        0x8,
        (
            "贝奈特的试吃活动\x01",
            "好像很顺利。\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x8,
        "看来今天能卖出更多面包呢。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_21CE")

    label("loc_217B")


    #C0099
    ChrTalk(
        0x8,
        "贝奈特提议的试吃活动已经开始了。\x02",
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0x8,
        (
            "真是个好主意啊，\x01",
            "看来今天能卖出更多呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_21CE")

    Jump("loc_39A9")

    label("loc_21D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_22F0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22A4")

    #C0101
    ChrTalk(
        0x8,
        "罗伊德，你们好啊。\x02",
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x8,
        (
            "纪念庆典期间，我们店也很忙。\x01",
            "面包的销量是平时的\x01",
            "三倍左右。\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0x8,
        (
            "那起暗杀麦克道尔市长的事件之后，\x01",
            "我还在担心今后会怎么样，\x01",
            "不过，好像对客流没什么影响呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_22EB")

    label("loc_22A4")


    #C0104
    ChrTalk(
        0x8,
        (
            "针对纪念庆典，\x01",
            "我也试做了新的面包。\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0x8,
        "有兴趣的话，就来尝尝吧。\x02",
    )

    CloseMessageWindow()

    label("loc_22EB")

    Jump("loc_39A9")

    label("loc_22F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_2439")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_23F3")

    #C0106
    ChrTalk(
        0x8,
        (
            "最近，经常有\x01",
            "警察到店里来。\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0x8,
        (
            "虽然穿着便装，\x01",
            "不过看那架势就知道是搜查官。\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0x8,
        "大概是在监视什么吧？\x02",
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0x103,
        (
            "#0200F……奥斯卡先生，\x01",
            "你的观察力真是不错啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0x101,
        (
            "#0000F他在这方面\x01",
            "倒是一直很敏锐的……\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0x8,
        "哈哈，也没有这么夸张啦。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2434")

    label("loc_23F3")


    #C0112
    ChrTalk(
        0x8,
        (
            "最近，经常有\x01",
            "警察到店里来。\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0x8,
        "好像在对什么情况进行监视。\x02",
    )

    CloseMessageWindow()

    label("loc_2434")

    Jump("loc_39A9")

    label("loc_2439")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_27CB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2723")

    #C0114
    ChrTalk(
        0x8,
        (
            "彩虹剧团的新剧目\x01",
            "下个月就要开始公演了。\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0x8,
        (
            "虽然我没有什么兴趣，\x01",
            "不过客人们一直\x01",
            "都在谈论这个呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0x8,
        (
            "——对了，罗伊德。\x01",
            "要是愿意的话，一起去吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0x8,
        "我有门票哦。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0118
    ChrTalk(
        0x101,
        (
            "#0005F奥斯卡……\x01",
            "你竟然有门票！？\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0x8,
        "嗯，是一个老顾客给我的。\x02",
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0x8,
        (
            "她就住在那边的公寓里，\x01",
            "是个非常漂亮的美人呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0x8,
        (
            "我偶尔会送她面包，\x01",
            "所以她就送票来答谢我了。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8F, 1)), scpexpr(EXPR_END)), "loc_26F5")
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0122
    ChrTalk(
        0x104,
        "#0300F（喂喂，难不成……）\x02",
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0x103,
        (
            "#0200F（多半是\x01",
            "  伊莉娅小姐吧……）\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0x101,
        (
            "#0006F（不愧是奥斯卡……\x01",
            "  在这方面真是很迟钝啊。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_271B")

    label("loc_26F5")


    #C0125
    ChrTalk(
        0x104,
        "#0300F真、真是个慷慨的客人啊……\x02",
    )

    CloseMessageWindow()

    label("loc_271B")

    SetScenarioFlags(0x0, 0)
    Jump("loc_27C6")

    label("loc_2723")


    #C0126
    ChrTalk(
        0x8,
        (
            "她就住在那边的公寓里，\x01",
            "是个非常漂亮的美人呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0x8,
        (
            "每天早上六点左右，\x01",
            "她都会来买很多很多面包。\x02",
        )
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0x8,
        (
            "我偶尔会赠送给她一些新品面包，\x01",
            "所以她就送门票来答谢我了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_27C6")

    Jump("loc_39A9")

    label("loc_27CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_2A3B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8E, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_29B7")

    #C0129
    ChrTalk(
        0x8,
        (
            "我们店门口正好\x01",
            "是一条能通往主干道的大街。\x02",
        )
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0x8,
        (
            "最近有很多导力车\x01",
            "来来往往呢～\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0x102,
        (
            "#0100F说起来，最近\x01",
            "有很多运输公司\x01",
            "开始使用导力卡车了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0x8,
        "对了，还有……\x02",
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0x8,
        (
            "大概是凌晨三点左右，\x01",
            "我正准备开始制作面包的时候，\x01",
            "看到了一辆黑色的搬运车。\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0x8,
        (
            "据说那是『鲁巴彻』的车，\x01",
            "是不是真的啊？\x02",
        )
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0x101,
        (
            "#0003F（西克洛斯贝尔街道……\x01",
            "  会不会是与帝国之间的\x01",
            "  走私路线呢？）\x02",
        )
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0x104,
        (
            "#0300F（无限接近黑暗的\x01",
            "  灰色地带啊……）\x02\x03",

            "（他们也在矿山镇露过面，\x01",
            "  最近的活动好像很频繁啊。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x8E, 1)
    Jump("loc_2A36")

    label("loc_29B7")


    #C0137
    ChrTalk(
        0x8,
        (
            "最近大概凌晨三点左右，\x01",
            "我正准备开始制作面包的时候，\x01",
            "看到了一辆黑色的搬运车。\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0x8,
        (
            "据说那是『鲁巴彻』的车，\x01",
            "是不是真的啊？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A36")

    Jump("loc_39A9")

    label("loc_2A3B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_2CCA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8E, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C4A")

    #C0139
    ChrTalk(
        0x8,
        "罗伊德，你们好啊。\x02",
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0x8,
        (
            "你们最近备受好评，\x01",
            "客人们都在谈论你们呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0x101,
        (
            "#0000F哈哈，总觉得有点难为情。\x02\x03",

            "因为我们最近\x01",
            "处理的都是一些\x01",
            "很普通的支援请求……\x02",
        )
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0x102,
        (
            "#0100F即使是平淡无奇的事情，\x01",
            "只要持之以恒，自然就会受到好评呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0x8,
        (
            "哈哈，\x01",
            "不过更受好评的\x01",
            "还是那条白色的警犬呢。\x02",
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

    #C0144
    ChrTalk(
        0x101,
        "#0006F果然是蔡特啊……\x02",
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0x8,
        (
            "早上做准备工作的时候，\x01",
            "偶尔会看到它，\x01",
            "真是很帅啊～\x02",
        )
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0x8,
        (
            "我也很喜欢狗，\x01",
            "下次把它介绍给我吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x8E, 0)
    Jump("loc_2CC5")

    label("loc_2C4A")


    #C0147
    ChrTalk(
        0x8,
        (
            "那条警犬，在这附近\x01",
            "已经成了热门话题呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0x8,
        (
            "我也很喜欢狗，\x01",
            "下次把它介绍给我吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0x8,
        (
            "我会请它尝尝\x01",
            "这个月的新品面包。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2CC5")

    Jump("loc_39A9")

    label("loc_2CCA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_2DE3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D82")

    #C0150
    ChrTalk(
        0x8,
        (
            "贝奈特是师傅的女儿，\x01",
            "制作面包的技术很厉害呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0x8,
        (
            "我刚来这里做学徒的时候，\x01",
            "还是贝奈特教我入门知识的。\x02",
        )
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0x8,
        (
            "不过她的性格不太好，\x01",
            "总是因为一点小事生气。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2DDE")

    label("loc_2D82")


    #C0153
    ChrTalk(
        0x8,
        (
            "其实她长得还是很可爱的，\x01",
            "总是生气的话，真是太可惜了。\x02",
        )
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0x8,
        (
            "下次我要做\x01",
            "高钙的牛奶面包。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2DDE")

    Jump("loc_39A9")

    label("loc_2DE3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_2E97")

    #C0155
    ChrTalk(
        0x8,
        (
            "我们的蔬菜面包\x01",
            "使用了阿尔摩利卡出产的\x01",
            "小麦和蔬菜。\x02",
        )
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0x8,
        (
            "虽然共和国产的食材最近比较便宜，\x01",
            "不过新鲜度还是不能相比啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0x104,
        (
            "#0300F哈哈，你们对食材\x01",
            "还是很讲究的嘛。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_39A9")

    label("loc_2E97")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_310F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_307F")

    #C0158
    ChrTalk(
        0x8,
        (
            "罗伊德，你们今天好早啊。\x01",
            "遇到什么好事了吗？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F5A")

    #C0159
    ChrTalk(
        0x101,
        (
            "#0000F不，没什么特别的理由。\x02\x03",

            "奥斯卡才是，一直都起得这么早……\x01",
            "呃……不过你毕竟是面包师，这也没办法啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2FCF")

    label("loc_2F5A")


    #C0160
    ChrTalk(
        0x101,
        (
            "#0006F不，我们是为工作而来的。\x02\x03",

            "#0000F奥斯卡才是，一直都起得这么早……\x01",
            "呃……不过你毕竟是面包师，这也没办法啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2FCF")


    #C0161
    ChrTalk(
        0x102,
        (
            "#0100F呵呵，早上好。\x01",
            "今天也是香气四溢呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0x8,
        (
            "哈哈哈，那是当然啦。\x01",
            "这边的架子上是刚烤好的\x01",
            "本月新品面包哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0x8,
        (
            "有兴趣的话，就请尝尝吧。\x01",
            "刚烤出来的面包最好吃了！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_310A")

    label("loc_307F")


    #C0164
    ChrTalk(
        0x8,
        (
            "面包师在凌晨三点就要开工。\x01",
            "开始新一天工作的时候，\x01",
            "感觉真是意外地神清气爽啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0x8,
        (
            "我也是因为憧憬这一点，\x01",
            "所以才选择了面包师这个职业。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_310A")

    Jump("loc_39A9")

    label("loc_310F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_3840")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A, 7)), scpexpr(EXPR_END)), "loc_34C0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3468")

    #C0166
    ChrTalk(
        0x8,
        "哟，罗伊德，这么快就来了啊。\x02",
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0x8,
        (
            "我们都有半年没见了吧……\x01",
            "不，已经有一年了吧？\x01",
            "真是过了很久呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0x101,
        (
            "#0003F……那个。\x01",
            "我们都已经有三年没见面了吧？\x02\x03",

            "之前你自己也都这么说过啊。\x01",
            "你这方面还真是一点没变，\x01",
            "总是这么粗枝大叶……\x02",
        )
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0x8,
        "哇哈哈，不要在意这种小事啦！\x02",
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0x8,
        (
            "话说，你好像\x01",
            "长高了很多呢。\x01",
            "不过还是一张娃娃脸。\x02",
        )
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0x101,
        "#0011F唔……\x02",
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0x104,
        "#0309F哈哈。\x02",
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0x102,
        "#0100F嘻嘻……\x02",
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0x103,
        "#0204F呵呵……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0175
    ChrTalk(
        0x101,
        (
            "#0006F好了，这话题到此为止。\x02\x03",

            "#0000F说起来……奥斯卡，\x01",
            "你的手艺好像长进了不少啊？\x02\x03",

            "温蒂在信里也写了哦，\x01",
            "听说你每月推出的新品面包\x01",
            "都很受大家好评呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0x8,
        (
            "哪里哪里，我还在学习呢。\x01",
            "没有比面包师\x01",
            "更深奥的工作了。\x02",
        )
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0x8,
        (
            "不过，这个月的新品，\x01",
            "我觉得确实很不错呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0x8,
        (
            "有兴趣的话……罗伊德的同事们\x01",
            "也都尝尝看吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0x104,
        "#0300F哦，那我就挑一些啦。\x02",
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0x102,
        (
            "#0100F这些面包看上去都很好吃啊，\x01",
            "我也买一些\x01",
            "带回去吃吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x4D, 3)
    Jump("loc_34BB")

    label("loc_3468")


    #C0181
    ChrTalk(
        0x8,
        (
            "虽然我还在学习之中，\x01",
            "不过对本月的新品倒很有自信。\x02",
        )
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0x8,
        "有兴趣的话就请尝尝吧。\x02",
    )

    CloseMessageWindow()

    label("loc_34BB")

    Jump("loc_383B")

    label("loc_34C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_370A")

    #C0183
    ChrTalk(
        0x8,
        (
            "对了，罗伊德，\x01",
            "你见过温蒂了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0x101,
        (
            "#0000F嗯，刚刚偶然遇到了。\x02\x03",

            "作为一个技师，\x01",
            "她似乎做得很不错……\x02\x03",

            "#0003F但作为她的老朋友，\x01",
            "我一直都有些担心……\x01",
            "她会不会发起火来拿扳手揍客人呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0x8,
        "哇哈哈，说得没错。\x02",
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0x8,
        (
            "不过，没问题的。\x01",
            "温蒂表面虽然这样，\x01",
            "但其实很能掌握分寸的。\x02",
        )
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0x8,
        (
            "顶多也就把人家\x01",
            "打出个肿包罢了。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_63(0x101, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0188
    ChrTalk(
        0x102,
        "#0105F（我觉得这已经非常严重了……）\x02",
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0x104,
        (
            "#0306F（唉，小温蒂她居然会这样。\x01",
            "  明明那么可爱……）\x02",
        )
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0x103,
        (
            "#0200F（兰迪前辈最好也\x01",
            "  小心一点呢。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x4D, 3)
    Jump("loc_383B")

    label("loc_370A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_37E5")

    #C0191
    ChrTalk(
        0x8,
        (
            "对了，最近有很多警方人士\x01",
            "光顾我们店呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0x8,
        (
            "我们旁边不就是律师事务所吗？\x01",
            "他们有事去那里的话，\x01",
            "顺道就会光顾这边。\x02",
        )
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0x8,
        (
            "哎呀～真是太好了，\x01",
            "我们的面包竟能让那么严肃的大叔\x01",
            "也露出笑容，实在是光荣啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_383B")

    label("loc_37E5")


    #C0194
    ChrTalk(
        0x8,
        (
            "最近有很多警察\x01",
            "光顾我们店呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0x8,
        (
            "他们要去旁边的律师事务所，\x01",
            "顺道就会光顾这里。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_383B")

    Jump("loc_39A9")

    label("loc_3840")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_39A9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3956")

    #C0196
    ChrTalk(
        0x101,
        (
            "#0000F奥斯卡，你的手艺\x01",
            "好像长进了不少啊？\x02\x03",

            "温蒂在信里也提到过哦，\x01",
            "她说你每月推出的新面包\x01",
            "都很受大家的好评呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0x8,
        "哪里，我还在学习呢。\x02",
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0x8,
        (
            "没有比面包师\x01",
            "更深奥的工作了。\x02",
        )
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0x8,
        (
            "不过这个月的新品，\x01",
            "我倒是觉得确实不错。\x02",
        )
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0x8,
        "有兴趣的话，就尝尝看吧。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_39A9")

    label("loc_3956")


    #C0201
    ChrTalk(
        0x8,
        (
            "虽然我还在学习之中，\x01",
            "不过对本月的新品倒很有自信。\x02",
        )
    )

    CloseMessageWindow()

    #C0202
    ChrTalk(
        0x8,
        "有兴趣的话就请尝尝吧。\x02",
    )

    CloseMessageWindow()

    label("loc_39A9")

    Return()

    # Function_6_FA2 end

    def Function_7_39AA(): pass

    label("Function_7_39AA")

    EventBegin(0x0)
    FadeToDark(500, 0, -1)
    OP_0D()
    OP_68(54330, 1500, 1490, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(30000, 0)
    SetChrPos(0x101, 52480, 0, 1350, 90)
    SetChrPos(0xEF, 51860, 0, 2300, 90)
    SetChrPos(0x153, 52000, 0, 260, 90)
    OP_93(0x8, 0x10E, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(750)

    #C0203
    ChrTalk(
        0x8,
        (
            "哟，罗伊德，\x01",
            "有一周没见了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0204
    ChrTalk(
        0x8,
        (
            "平时不是经常过来吗，\x01",
            "难道发生什么事了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0205
    ChrTalk(
        0x101,
        "#0000F不，其实……\x02",
    )

    CloseMessageWindow()

    #C0206
    ChrTalk(
        0x153,
        (
            "#1110F哇，好高的帽子！\x01",
            "好有趣哦！\x02\x03",

            "#1104F而且……\x01",
            "嗯嗯，好香的味道啊！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0x8)

    #C0207
    ChrTalk(
        0x8,
        "………那个………\x02",
    )

    CloseMessageWindow()

    #C0208
    ChrTalk(
        0x8,
        "这是罗伊德的妹妹吗？\x02",
    )

    CloseMessageWindow()

    #C0209
    ChrTalk(
        0x101,
        (
            "#0006F……不是的，\x01",
            "我没有妹妹啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0210
    ChrTalk(
        0x8,
        (
            "哇哈哈，\x01",
            "当然是开玩笑啦。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_3BB9")

    #C0211
    ChrTalk(
        0x102,
        (
            "#0100F这个孩子叫琪雅，\x01",
            "因为某些原因，暂时由我们照顾。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C48")

    label("loc_3BB9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_3C00")

    #C0212
    ChrTalk(
        0x103,
        (
            "#0200F这孩子叫琪雅，\x01",
            "由于某些原因，暂时由我们照顾。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C48")

    label("loc_3C00")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_3C48")

    #C0213
    ChrTalk(
        0x104,
        (
            "#0300F这小鬼叫琪雅，\x01",
            "稍微有些原因，所以暂时由我们来照顾。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3C48")


    #C0214
    ChrTalk(
        0x8,
        "哦，是这样啊。\x02",
    )

    CloseMessageWindow()

    #C0215
    ChrTalk(
        0x8,
        (
            "好，作为初次见面的纪念，\x01",
            "不嫌弃的话就尝尝吧！\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    #A0216
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "琪雅收下了牛奶瓶。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0217
    ChrTalk(
        0x153,
        (
            "#1105F哇，可以吗～？\x02\x03",

            "#1109F（咕噜咕噜……）真好喝啊！\x02",
        )
    )

    CloseMessageWindow()

    #C0218
    ChrTalk(
        0x8,
        (
            "哈哈哈！\x01",
            "我们店里的牛奶是阿尔摩利卡产的哟。\x02",
        )
    )

    CloseMessageWindow()

    #C0219
    ChrTalk(
        0x101,
        "#0000F哈哈，让你费心了，真不好意思啊。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0xAD, 5)
    EventEnd(0x5)
    Return()

    # Function_7_39AA end

    def Function_8_3D4F(): pass

    label("Function_8_3D4F")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3E74")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3D6A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3E6F")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "交谈\x01",      # 0
            "购物\x01",      # 1
            "放弃\x01",      # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3DBA")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_3DBA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3E3A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_3DD9")
    OP_AF(0xCE)
    Jump("loc_3E2B")

    label("loc_3DD9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_3DE9")
    OP_AF(0xCD)
    Jump("loc_3E2B")

    label("loc_3DE9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_3DF9")
    OP_AF(0xCC)
    Jump("loc_3E2B")

    label("loc_3DF9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_3E09")
    OP_AF(0xCB)
    Jump("loc_3E2B")

    label("loc_3E09")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_3E19")
    OP_AF(0xCA)
    Jump("loc_3E2B")

    label("loc_3E19")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_3E29")
    OP_AF(0xC9)
    Jump("loc_3E2B")

    label("loc_3E29")

    OP_AF(0xC8)

    label("loc_3E2B")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3E6A")

    label("loc_3E3A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3E4E")
    Jump("loc_3E6A")

    label("loc_3E4E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3E6A")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 9)

    label("loc_3E6A")

    Jump("loc_3D6A")

    label("loc_3E6F")

    Jump("loc_3E77")

    label("loc_3E74")

    Call(0, 9)

    label("loc_3E77")

    TalkEnd(0x9)
    Return()

    # Function_8_3D4F end

    def Function_9_3E7B(): pass

    label("Function_9_3E7B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6, 0x0, 0x10)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6D, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3F98")

    #C0220
    ChrTalk(
        0x9,
        (
            "哦，我听说了呢。\x01",
            "已经帮我们收集到食材了吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0x9,
        (
            "太高兴了，这么一来就能\x01",
            "尽情烤面包了。\x02",
        )
    )

    CloseMessageWindow()

    #C0222
    ChrTalk(
        0x101,
        (
            "#0000F如果还有什么事，\x01",
            "请尽管联络支援科。\x02",
        )
    )

    CloseMessageWindow()

    #C0223
    ChrTalk(
        0x104,
        (
            "#0300F这些小事\x01",
            "都是举手之劳啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0224
    ChrTalk(
        0x9,
        "你们真是可靠啊。\x02",
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0x9,
        (
            "呵呵，说不定以后还要请你们帮忙哦。\x01",
            "到时候就拜托啦！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x6D, 6)
    Jump("loc_4E4D")

    label("loc_3F98")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_405A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_402A")

    #C0226
    ChrTalk(
        0x9,
        (
            "哎呀，食材配送时间\x01",
            "居然比预定要晚呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0227
    ChrTalk(
        0x9,
        (
            "今天只能节省着材料\x01",
            "来烤面包了。\x02",
        )
    )

    CloseMessageWindow()

    #C0228
    ChrTalk(
        0x9,
        "感觉真是束手束脚啊。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_4055")

    label("loc_402A")


    #C0229
    ChrTalk(
        0x9,
        (
            "唉，真没办法……\x01",
            "但愿明天能快点送来。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4055")

    Jump("loc_4E4D")

    label("loc_405A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_4144")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4116")

    #C0230
    ChrTalk(
        0x9,
        (
            "贝奈特做的新面包，\x01",
            "我和奥斯卡都赞许有加呢……\x01",
            "但她本人却不这么觉得。\x02",
        )
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0x9,
        (
            "嗯，对味道已经很满意了……\x01",
            "但却不能接受奥斯卡的反应吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0232
    ChrTalk(
        0x9,
        "嗯，真是想不明白啊。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_413F")

    label("loc_4116")


    #C0233
    ChrTalk(
        0x9,
        (
            "这个年纪的女孩，\x01",
            "心思真是难以琢磨。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_413F")

    Jump("loc_4E4D")

    label("loc_4144")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_41F1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_41B1")

    #C0234
    ChrTalk(
        0x9,
        (
            "哦……贝奈特那家伙，\x01",
            "烤的面包可真香啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0235
    ChrTalk(
        0x9,
        (
            "这次的面包，\x01",
            "看来很值得期待啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_41EC")

    label("loc_41B1")


    #C0236
    ChrTalk(
        0x9,
        (
            "贝奈特也开始\x01",
            "很认真地做面包了。\x02",
        )
    )

    CloseMessageWindow()

    #C0237
    ChrTalk(
        0x9,
        "……真是很香啊。\x02",
    )

    CloseMessageWindow()

    label("loc_41EC")

    Jump("loc_4E4D")

    label("loc_41F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_4290")

    #C0238
    ChrTalk(
        0x9,
        (
            "最近增加了很多\x01",
            "从远方而来的客人。\x02",
        )
    )

    CloseMessageWindow()

    #C0239
    ChrTalk(
        0x9,
        (
            "真让人高兴啊，\x01",
            "这也是奥斯卡\x01",
            "努力的成果。\x02",
        )
    )

    CloseMessageWindow()

    #C0240
    ChrTalk(
        0x9,
        (
            "多亏了他，\x01",
            "竟然连克洛斯贝尔时代周刊\x01",
            "都过来采访我们呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4E4D")

    label("loc_4290")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_43E0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4366")

    #C0241
    ChrTalk(
        0x9,
        (
            "贝奈特也一直在\x01",
            "认真地钻研呢，\x01",
            "于是我重新考虑了一下新品面包的上架方式。\x02",
        )
    )

    CloseMessageWindow()

    #C0242
    ChrTalk(
        0x9,
        (
            "简单来说，就是三个人各自拿出自己的试做品，\x01",
            "然后投票决定最好吃的面包。\x02",
        )
    )

    CloseMessageWindow()

    #C0243
    ChrTalk(
        0x9,
        "……怎么样，这种方法很合理吧。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_43DB")

    label("loc_4366")


    #C0244
    ChrTalk(
        0x9,
        (
            "原来一直是\x01",
            "由我试吃后决定的……\x02",
        )
    )

    CloseMessageWindow()

    #C0245
    ChrTalk(
        0x9,
        (
            "不过，奥斯卡和贝奈特\x01",
            "现在都已经可以独当一面了，\x01",
            "所以还是投票决定比较公平。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_43DB")

    Jump("loc_4E4D")

    label("loc_43E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_445A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4434")

    #C0246
    ChrTalk(
        0x9,
        (
            "贝奈特最近\x01",
            "总是霸占着厨房。\x02",
        )
    )

    CloseMessageWindow()

    #C0247
    ChrTalk(
        0x9,
        "真拿她没办法啊……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_4455")

    label("loc_4434")


    #C0248
    ChrTalk(
        0x9,
        (
            "伤脑筋，\x01",
            "我也想烤面包啊……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4455")

    Jump("loc_4E4D")

    label("loc_445A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_44CA")

    #C0249
    ChrTalk(
        0x9,
        (
            "客流差不多也该减少了，\x01",
            "我们也稍微休息一下吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0250
    ChrTalk(
        0x9,
        (
            "……做面包是需要腕力的，\x01",
            "我也有些累了呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4E4D")

    label("loc_44CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_454C")

    #C0251
    ChrTalk(
        0x9,
        "啪啪啦啪啪，啪啪啪～！\x02",
    )

    CloseMessageWindow()

    #C0252
    ChrTalk(
        0x9,
        (
            "游行时放的曲子，\x01",
            "每年都是一样的啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0253
    ChrTalk(
        0x9,
        (
            "每当听到这首曲子，\x01",
            "就感觉自己恢复了童心。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4E4D")

    label("loc_454C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_45C7")

    #C0254
    ChrTalk(
        0x9,
        (
            "今天有纪念庆典期间\x01",
            "最盛大的一项活动——游行。\x02",
        )
    )

    CloseMessageWindow()

    #C0255
    ChrTalk(
        0x9,
        (
            "熬过这段时间，\x01",
            "就能稍微轻松些了。\x01",
            "再继续坚持一下吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4E4D")

    label("loc_45C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_4620")

    #C0256
    ChrTalk(
        0x9,
        "嘿，嘿……\x02",
    )

    CloseMessageWindow()

    #C0257
    ChrTalk(
        0x9,
        (
            "今年的客流量真是不错啊，\x01",
            "无论烤多少面包也都供不应求。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4E4D")

    label("loc_4620")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_4710")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_46C6")

    #C0258
    ChrTalk(
        0x9,
        (
            "那个别扭的贝奈特要进行\x01",
            "店前零售……？\x02",
        )
    )

    CloseMessageWindow()

    #C0259
    ChrTalk(
        0x9,
        (
            "而且她还很努力地\x01",
            "保持着职业微笑。\x02",
        )
    )

    CloseMessageWindow()

    #C0260
    ChrTalk(
        0x9,
        (
            "……这家伙变化太大，\x01",
            "让我这个做爸爸的都有点担心了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_470B")

    label("loc_46C6")


    #C0261
    ChrTalk(
        0x9,
        (
            "那家伙，最近真是\x01",
            "变得很积极了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0262
    ChrTalk(
        0x9,
        "……呵，真是吓了一跳呢。\x02",
    )

    CloseMessageWindow()

    label("loc_470B")

    Jump("loc_4E4D")

    label("loc_4710")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_476E")

    #C0263
    ChrTalk(
        0x9,
        (
            "自从奥斯卡来了之后，\x01",
            "贝奈特就变得很积极了。\x02",
        )
    )

    CloseMessageWindow()

    #C0264
    ChrTalk(
        0x9,
        (
            "嗯，真是收了个\x01",
            "好徒弟呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4E4D")

    label("loc_476E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_47F1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4789")
    Call(0, 12)
    Jump("loc_47EC")

    label("loc_4789")


    #C0265
    ChrTalk(
        0x9,
        (
            "奥斯卡那家伙的手艺非常不错，\x01",
            "更重要的是，他很有男子汉气概。\x02",
        )
    )

    CloseMessageWindow()

    #C0266
    ChrTalk(
        0x9,
        "这样店里也就安稳了，哇哈哈！\x02",
    )

    CloseMessageWindow()

    label("loc_47EC")

    Jump("loc_4E4D")

    label("loc_47F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_4866")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B0(0x17)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_480D")
    Call(0, 10)
    Jump("loc_4861")

    label("loc_480D")


    #C0267
    ChrTalk(
        0x9,
        (
            "好了，我也要\x01",
            "想想下一款新面包了。\x02",
        )
    )

    CloseMessageWindow()

    #C0268
    ChrTalk(
        0x9,
        (
            "如果一直都交给奥斯卡去做，\x01",
            "也不太好呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4861")

    Jump("loc_4E4D")

    label("loc_4866")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_4958")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B0(0x17)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4882")
    Call(0, 10)
    Jump("loc_4953")

    label("loc_4882")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_48EC")

    #C0269
    ChrTalk(
        0x9,
        (
            "虽然贝奈特\x01",
            "好几次都想挑战奥斯卡……\x01",
            "但怎么也赢不了。\x02",
        )
    )

    CloseMessageWindow()

    #C0270
    ChrTalk(
        0x9,
        "所以她才变得那么拼命啊。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_4953")

    label("loc_48EC")


    #C0271
    ChrTalk(
        0x9,
        (
            "奥斯卡的面包\x01",
            "很受欢迎呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0272
    ChrTalk(
        0x9,
        (
            "不仅是因为制作材料和手法，\x01",
            "也是因为那家伙在揉合方面的\x01",
            "技巧感很好。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4953")

    Jump("loc_4E4D")

    label("loc_4958")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_4A6D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4A09")

    #C0273
    ChrTalk(
        0x9,
        (
            "最近的新品面包\x01",
            "都是交给奥斯卡来做的。\x02",
        )
    )

    CloseMessageWindow()

    #C0274
    ChrTalk(
        0x9,
        (
            "那家伙确实富有才能。\x01",
            "而且，他不仅非常努力，\x01",
            "更拥有出类拔萃的天赋。\x02",
        )
    )

    CloseMessageWindow()

    #C0275
    ChrTalk(
        0x9,
        (
            "我已经没有什么\x01",
            "可以教他的了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_4A68")

    label("loc_4A09")


    #C0276
    ChrTalk(
        0x9,
        "奥斯卡的天赋实在是出类拔萃。\x02",
    )

    CloseMessageWindow()

    #C0277
    ChrTalk(
        0x9,
        (
            "呵呵，贝奈特一直对他\x01",
            "抱有竞争意识，也是因为这个原因吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4A68")

    Jump("loc_4E4D")

    label("loc_4A6D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_4B81")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4B15")

    #C0278
    ChrTalk(
        0x9,
        (
            "虽然也许没人察觉到，\x01",
            "不过我做面包的基准是『香味』。\x02",
        )
    )

    CloseMessageWindow()

    #C0279
    ChrTalk(
        0x9,
        (
            "研制新品面包的时候，\x01",
            "也会注重香味。\x02",
        )
    )

    CloseMessageWindow()

    #C0280
    ChrTalk(
        0x9,
        (
            "这也等同于必须将\x01",
            "食材的优点引发出来。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_4B7C")

    label("loc_4B15")


    #C0281
    ChrTalk(
        0x9,
        (
            "我制作新的面包，\x01",
            "说到底就是为了\x01",
            "不断探求活用素材的方法。\x02",
        )
    )

    CloseMessageWindow()

    #C0282
    ChrTalk(
        0x9,
        (
            "当然，赢得顾客的认可\x01",
            "也是理由之一。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4B7C")

    Jump("loc_4E4D")

    label("loc_4B81")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_4C72")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4C01")

    #C0283
    ChrTalk(
        0x9,
        "好了，第二炉烤好了～\x02",
    )

    CloseMessageWindow()

    #C0284
    ChrTalk(
        0x9,
        (
            "嗯，真是香气扑鼻啊。\x01",
            "正因为能够享受这种香味，我才无法放弃当面包师啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_4C6D")

    label("loc_4C01")


    #C0285
    ChrTalk(
        0x9,
        "我们店的面包从五点开始烤制。\x02",
    )

    CloseMessageWindow()

    #C0286
    ChrTalk(
        0x9,
        (
            "在那以前一直在做生面团。\x01",
            "之后就是烤啊烤，\x01",
            "尽情享受香味的快乐时光了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4C6D")

    Jump("loc_4E4D")

    label("loc_4C72")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_4D49")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4D1E")

    #C0287
    ChrTalk(
        0x9,
        (
            "我女儿最讨厌的就是输给别人，\x01",
            "最近好像对奥斯卡\x01",
            "燃起了强烈的竞争意识呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0288
    ChrTalk(
        0x9,
        (
            "之前明明说过\x01",
            "不想当面包师的。\x02",
        )
    )

    CloseMessageWindow()

    #C0289
    ChrTalk(
        0x9,
        "哈哈，真不知道她在想什么啊。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_4D44")

    label("loc_4D1E")


    #C0290
    ChrTalk(
        0x9,
        "这个年纪的女孩，真是让人猜不透。\x02",
    )

    CloseMessageWindow()

    label("loc_4D44")

    Jump("loc_4E4D")

    label("loc_4D49")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_4E4D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4DF5")

    #C0291
    ChrTalk(
        0x9,
        "……哦，欢迎光临！\x02",
    )

    CloseMessageWindow()

    #C0292
    ChrTalk(
        0x9,
        (
            "虽然我们是面包店，\x01",
            "但店门前也设置了能够\x01",
            "享用咖啡的露天座位区哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0293
    ChrTalk(
        0x9,
        (
            "坐在那里吃点东西，很方便吧？\x01",
            "还请随意使用啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_4E4D")

    label("loc_4DF5")


    #C0294
    ChrTalk(
        0x9,
        (
            "我们店门前设置了能够\x01",
            "享用咖啡的露天座位区哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0295
    ChrTalk(
        0x9,
        (
            "而且还提供饮料，\x01",
            "请随意就坐吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4E4D")

    Return()

    # Function_9_3E7B end

    def Function_10_4E4E(): pass

    label("Function_10_4E4E")


    #C0296
    ChrTalk(
        0xFE,
        (
            "哟，欢迎光临。\x01",
            "这个月的新面包已经开始销售了。\x02",
        )
    )

    CloseMessageWindow()

    #C0297
    ChrTalk(
        0xFE,
        (
            "对了，这个月的面包\x01",
            "搭配这款咖啡很不错呢。\x01",
            "有兴趣的话就记下来吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0298
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1D3),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "的做法被教授了。\x02",
        )
    )

    CloseMessageWindow()

    #A0299
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1D3),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "的做法已经学会了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    OP_B0(0x17)
    Return()

    # Function_10_4E4E end

    def Function_11_4F33(): pass

    label("Function_11_4F33")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6, 0x1, 0x0)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6, 0x1, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4F65")
    TurnDirection(0x0, 0xA, 0)
    OP_4B(0xA, 0xFF)
    Call(0, 31)
    Return()

    label("loc_4F65")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6, 0x1, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6, 0x1, 0x3)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_50B4")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x12F, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_5048")

    #C0300
    ChrTalk(
        0xA,
        "啊……\x02",
    )

    CloseMessageWindow()

    #C0301
    ChrTalk(
        0xA,
        "帮我把食材拿来了吗？\x02",
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
            "【交出收集的食材】\x01",      # 0
            "【放弃】\x01",                # 1
        )
    )

    MenuEnd(0x0)
    FadeToBright(300, 0)
    OP_60(0x0)
    OP_5A()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_5019"),
        (1, "loc_5021"),
        (SWITCH_DEFAULT, "loc_5043"),
    )


    label("loc_5019")

    Call(0, 32)
    Jump("loc_5043")

    label("loc_5021")


    #C0302
    ChrTalk(
        0xA,
        (
            "是吗……\x01",
            "请你们尽快啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5043")

    label("loc_5043")

    Jump("loc_50AF")

    label("loc_5048")


    #C0303
    ChrTalk(
        0xFE,
        (
            "我的委托是\x01",
            "两个『魔兽之卵』。\x02",
        )
    )

    CloseMessageWindow()

    #C0304
    ChrTalk(
        0xFE,
        (
            "因为我在研制新面包。\x01",
            "希望能尽量快一点，\x01",
            "还有请对奥斯卡保密哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_50AF")

    Jump("loc_5C7C")

    label("loc_50B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_END)), "loc_51BA")

    #C0305
    ChrTalk(
        0xFE,
        (
            "今、今天真是多谢了。\x01",
            "多亏有你们啊。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x71, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_512A")

    #C0306
    ChrTalk(
        0xFE,
        (
            "哼哼……这样一来，就能超越\x01",
            "奥斯卡那个家伙了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_518C")

    label("loc_512A")


    #C0307
    ChrTalk(
        0xFE,
        (
            "虽然好像晚了一点……\x01",
            "不过先不管这些啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0308
    ChrTalk(
        0xFE,
        (
            "哼哼，可恶的奥斯卡……\x01",
            "这次我一定会打败你的……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_518C")


    #C0309
    ChrTalk(
        0x101,
        (
            "#0000F面包师的修行，\x01",
            "请努力加油哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5C7C")

    label("loc_51BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_51C8")
    Jump("loc_5C7C")

    label("loc_51C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_52B7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5269")

    #C0310
    ChrTalk(
        0xFE,
        (
            "哼哼哼……我的最高杰作\x01",
            "总算烤好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0311
    ChrTalk(
        0xFE,
        (
            "经过我这一个月的反复研究，\x01",
            "终于制作出了这款香气十足的核桃面包！\x02",
        )
    )

    CloseMessageWindow()

    #C0312
    ChrTalk(
        0xFE,
        "颤抖吧，奥斯卡！！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_52B2")

    label("loc_5269")


    #C0313
    ChrTalk(
        0xFE,
        (
            "哼哼哼……我的最高杰作\x01",
            "总算烤好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0314
    ChrTalk(
        0xFE,
        "好了，乖乖认输吧，奥斯卡！\x02",
    )

    CloseMessageWindow()

    label("loc_52B2")

    Jump("loc_5C7C")

    label("loc_52B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_52FD")
    OP_93(0xFE, 0x0, 0x0)

    #C0315
    ChrTalk(
        0xFE,
        (
            "（昏昏欲睡）……\x01",
            "６２度下……发酵两小时……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5C7C")

    label("loc_52FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_5406")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_53B0")

    #C0316
    ChrTalk(
        0xFE,
        (
            "我们店被最新一期的\x01",
            "克洛斯贝尔时代周刊\x01",
            "报道了哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0317
    ChrTalk(
        0xFE,
        (
            "可是……介绍的不是我，\x01",
            "也不是爸爸，\x01",
            "不知为何，竟然是采访奥斯卡。\x02",
        )
    )

    CloseMessageWindow()

    #C0318
    ChrTalk(
        0xFE,
        "呜呜，这是为什么啊……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_5401")

    label("loc_53B0")


    #C0319
    ChrTalk(
        0xFE,
        (
            "而且居然还把他称作什么\x01",
            "『年轻的天才面包师』……\x02",
        )
    )

    CloseMessageWindow()

    #C0320
    ChrTalk(
        0xFE,
        "呜呜，我绝对不承认……\x02",
    )

    CloseMessageWindow()

    label("loc_5401")

    Jump("loc_5C7C")

    label("loc_5406")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_5514")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_54A5")

    #C0321
    ChrTalk(
        0xFE,
        "我正在研制新款面包。\x02",
    )

    CloseMessageWindow()

    #C0322
    ChrTalk(
        0xFE,
        (
            "这次的面包是用大量的\x01",
            "蜂蜜和核桃制成的。\x02",
        )
    )

    CloseMessageWindow()

    #C0323
    ChrTalk(
        0xFE,
        (
            "虽然还在研究烤制方法……\x01",
            "……哼哼，但这次是胜券在握了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_550F")

    label("loc_54A5")


    #C0324
    ChrTalk(
        0xFE,
        (
            "虽然在纪念庆典中的销售量\x01",
            "算是平分秋色……\x02",
        )
    )

    CloseMessageWindow()

    #C0325
    ChrTalk(
        0xFE,
        (
            "哼哼，走着瞧吧，奥斯卡。\x01",
            "这次我绝对会让你彻底败北的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_550F")

    Jump("loc_5C7C")

    label("loc_5514")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_560B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_55A6")
    OP_93(0xA, 0x10E, 0x0)

    #C0326
    ChrTalk(
        0xFE,
        (
            "………………………（捏捏）\x01",
            "嗯，生面团差不多就是这样了。\x02",
        )
    )

    CloseMessageWindow()

    #C0327
    ChrTalk(
        0xFE,
        (
            "这次一定……这次一定要让\x01",
            "奥斯卡彻底哑口无言。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_5606")

    label("loc_55A6")


    #C0328
    ChrTalk(
        0xFE,
        (
            "为了迎接纪念庆典，\x01",
            "我正在制作原创的面包。\x02",
        )
    )

    CloseMessageWindow()

    #C0329
    ChrTalk(
        0xFE,
        (
            "……敬、敬请期待吧。\x01",
            "我会做出很棒的面包的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5606")

    Jump("loc_5C7C")

    label("loc_560B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_5674")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5626")
    Call(0, 12)
    Jump("loc_566F")

    label("loc_5626")

    TurnDirection(0xA, 0x9, 0)

    #C0330
    ChrTalk(
        0xFE,
        (
            "总、总之，我想\x01",
            "使用厨房！\x02",
        )
    )

    CloseMessageWindow()

    #C0331
    ChrTalk(
        0xFE,
        (
            "借我用一段时间\x01",
            "有什么关系嘛！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_566F")

    Jump("loc_5C7C")

    label("loc_5674")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_5768")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5730")
    OP_93(0xA, 0x5A, 0x0)

    #C0332
    ChrTalk(
        0xFE,
        (
            "奇怪，我准备好的\x01",
            "高级小麦粉怎么没了……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 1900, 0x2C, 0x2F, 0x96, 0x1)
    Sound(25, 0, 100, 0)
    Sleep(1000)

    #C0333
    ChrTalk(
        0xFE,
        (
            "又是爸爸。\x01",
            "竟然随便动用别人的食材……！\x02",
        )
    )

    CloseMessageWindow()

    #C0334
    ChrTalk(
        0xFE,
        (
            "这样一来，\x01",
            "不就做不了面包了吗！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_5763")

    label("loc_5730")


    #C0335
    ChrTalk(
        0xFE,
        (
            "我就是讨厌爸爸这一点。\x01",
            "总是这么不顾别人……！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5763")

    Jump("loc_5C7C")

    label("loc_5768")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_5888")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5829")

    #C0336
    ChrTalk(
        0xFE,
        (
            "做面包的第一步\x01",
            "就是挑选食材。\x02",
        )
    )

    CloseMessageWindow()

    #C0337
    ChrTalk(
        0xFE,
        (
            "现在有了横跨全大陆的铁路，\x01",
            "很容易就能订购到各种食材。\x02",
        )
    )

    CloseMessageWindow()

    #C0338
    ChrTalk(
        0xFE,
        (
            "这次就试试奥雷德自治州\x01",
            "出产的小麦粉吧……\x01",
            "感觉一定能做出好面包呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_5883")

    label("loc_5829")


    #C0339
    ChrTalk(
        0xFE,
        (
            "在、在我看来，\x01",
            "我和奥斯卡应该是平分秋色。\x02",
        )
    )

    CloseMessageWindow()

    #C0340
    ChrTalk(
        0xFE,
        (
            "我还没有输呢。\x01",
            "我要在材料上取胜……！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5883")

    Jump("loc_5C7C")

    label("loc_5888")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_58D4")

    #C0341
    ChrTalk(
        0xFE,
        "……今天的面包是我烤的。\x02",
    )

    CloseMessageWindow()

    #C0342
    ChrTalk(
        0xFE,
        "愿、愿意的话，请去尝尝吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_5C7C")

    label("loc_58D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_59CD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5982")

    #C0343
    ChrTalk(
        0xFE,
        (
            "我承认，奥斯卡的确是有才能的。\x01",
            "只用了两年的时间，\x01",
            "就获得了爸爸的认可。\x02",
        )
    )

    CloseMessageWindow()

    #C0344
    ChrTalk(
        0xFE,
        (
            "哼……但这并不\x01",
            "意味着我会输给他。\x02",
        )
    )

    CloseMessageWindow()

    #C0345
    ChrTalk(
        0xFE,
        "明天我一定要让他哑口无言。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_59C8")

    label("loc_5982")


    #C0346
    ChrTalk(
        0xFE,
        (
            "哼哼，奥斯卡，\x01",
            "咱们走着瞧吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0347
    ChrTalk(
        0xFE,
        (
            "明天一定要让你\x01",
            "哑口无言……！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_59C8")

    Jump("loc_5C7C")

    label("loc_59CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_5A20")

    #C0348
    ChrTalk(
        0xFE,
        "……欢迎光临。\x02",
    )

    CloseMessageWindow()

    #C0349
    ChrTalk(
        0xFE,
        (
            "我们今天也照常营业哦。\x01",
            "面包店是不会休息的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5C7C")

    label("loc_5A20")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_5B66")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5AFE")

    #C0350
    ChrTalk(
        0xFE,
        (
            "有一天，奥斯卡\x01",
            "来到我们店里，\x01",
            "说想要做学徒。\x02",
        )
    )

    CloseMessageWindow()

    #C0351
    ChrTalk(
        0xFE,
        (
            "然后得到了父亲的同意，\x01",
            "之后一直在这里学习……\x02",
        )
    )

    CloseMessageWindow()

    #C0352
    ChrTalk(
        0xFE,
        "他现在已经是最有出息的大弟子了。\x02",
    )

    CloseMessageWindow()

    #C0353
    ChrTalk(
        0xFE,
        (
            "呜……\x01",
            "竟然无视我这个亲生女儿，\x01",
            "将他看成大弟子……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_5B61")

    label("loc_5AFE")


    #C0354
    ChrTalk(
        0xFE,
        (
            "我做面包的资历\x01",
            "可要比他长多了。\x02",
        )
    )

    CloseMessageWindow()

    #C0355
    ChrTalk(
        0xFE,
        (
            "竟然无视我这个亲生女儿，\x01",
            "将他看成大弟子……\x01",
            "不可原谅……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5B61")

    Jump("loc_5C7C")

    label("loc_5B66")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_5C7C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5BAE")

    #C0356
    ChrTalk(
        0xFE,
        "……欢迎光临。\x02",
    )

    CloseMessageWindow()

    #C0357
    ChrTalk(
        0xFE,
        "要结账的话，请到柜台。\x02",
    )

    CloseMessageWindow()
    Jump("loc_5C7C")

    label("loc_5BAE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5C3E")

    #C0358
    ChrTalk(
        0xFE,
        "我们店的新品面包很受欢迎哦。\x02",
    )

    CloseMessageWindow()

    #C0359
    ChrTalk(
        0xFE,
        (
            "继承这个特色，负责制作新面包的人，\x01",
            "应该是我这个店中的招牌美女才对……\x01",
            "（自言自语）……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_5C7C")

    label("loc_5C3E")


    #C0360
    ChrTalk(
        0xFE,
        (
            "明明应该是由我来\x01",
            "继承制作新品面包的……\x01",
            "（自言自语）……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5C7C")

    TalkEnd(0xFE)
    Return()

    # Function_11_4F33 end

    def Function_12_5C80(): pass

    label("Function_12_5C80")

    OP_4B(0x9, 0xFF)
    OP_4B(0xA, 0xFF)
    TurnDirection(0x9, 0xA, 0)
    TurnDirection(0xA, 0x9, 0)

    #C0361
    ChrTalk(
        0xA,
        (
            "爸爸，你偶尔也\x01",
            "到店面转转如何？\x02",
        )
    )

    CloseMessageWindow()

    #C0362
    ChrTalk(
        0xA,
        (
            "最近你老是\x01",
            "待在厨房里啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0363
    ChrTalk(
        0x9,
        "哼，小丫头懂什么。\x02",
    )

    CloseMessageWindow()

    #C0364
    ChrTalk(
        0x9,
        (
            "那当然是因为\x01",
            "奥斯卡一表人才！\x02",
        )
    )

    CloseMessageWindow()

    #C0365
    ChrTalk(
        0x9,
        (
            "比你不修边幅的老爸我受欢迎多了～¤\x01",
            "自从他来了之后，\x01",
            "女性客人也增加了不少呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 1700, 0xE, 0xF, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0366
    ChrTalk(
        0xA,
        (
            "唔，爸爸他一直\x01",
            "都是这个样子……\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x9, 0xFF)
    OP_4C(0xA, 0xFF)
    SetScenarioFlags(0x0, 1)
    SetScenarioFlags(0x0, 2)
    Return()

    # Function_12_5C80 end

    def Function_13_5DB6(): pass

    label("Function_13_5DB6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_5DFE")

    #C0367
    ChrTalk(
        0xFE,
        (
            "贝奈特小姐\x01",
            "刚才是怎么了？\x02",
        )
    )

    CloseMessageWindow()

    #C0368
    ChrTalk(
        0xFE,
        "突然就冲了出去……\x02",
    )

    CloseMessageWindow()
    Jump("loc_6A38")

    label("loc_5DFE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_5E62")

    #C0369
    ChrTalk(
        0xFE,
        (
            "今天烤出来的\x01",
            "面包好香啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0370
    ChrTalk(
        0xFE,
        (
            "啊啊，好想尝尝啊……\x01",
            "是不是这次的新品面包呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6A38")

    label("loc_5E62")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_5F6E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5F06")

    #C0371
    ChrTalk(
        0xFE,
        (
            "我买了这家店的面包\x01",
            "给爸爸妈妈吃。\x02",
        )
    )

    CloseMessageWindow()

    #C0372
    ChrTalk(
        0xFE,
        (
            "然后问他们想不想每天都吃，\x01",
            "他们竟然默认了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0373
    ChrTalk(
        0xFE,
        (
            "呵呵，很成功呢！\x01",
            "这样就能经常来面包店了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_5F69")

    label("loc_5F06")


    #C0374
    ChrTalk(
        0xFE,
        (
            "嗯～这个月的\x01",
            "新品是黄油面包啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0375
    ChrTalk(
        0xFE,
        (
            "好像也很好吃呢……\x01",
            "正好刚刚烤好，\x01",
            "配一杯咖啡来尝尝看吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5F69")

    Jump("loc_6A38")

    label("loc_5F6E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_6068")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_601E")

    #C0376
    ChrTalk(
        0xFE,
        (
            "我经常来面包店的事，\x01",
            "被爸爸和妈妈发现了。\x02",
        )
    )

    CloseMessageWindow()

    #C0377
    ChrTalk(
        0xFE,
        (
            "他们两个都很死板，\x01",
            "说绝对不许在外面吃东西。\x02",
        )
    )

    CloseMessageWindow()

    #C0378
    ChrTalk(
        0xFE,
        (
            "哼～这有什么不好嘛！\x01",
            "这里的面包真的很好吃啊～！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_6063")

    label("loc_601E")


    #C0379
    ChrTalk(
        0xFE,
        (
            "再这样下去，\x01",
            "零花钱也会被停掉的。\x02",
        )
    )

    CloseMessageWindow()

    #C0380
    ChrTalk(
        0xFE,
        "爸爸和妈妈都很顽固呢……\x02",
    )

    CloseMessageWindow()

    label("loc_6063")

    Jump("loc_6A38")

    label("loc_6068")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_60EC")

    #C0381
    ChrTalk(
        0xFE,
        (
            "纪念庆典和朋友一起玩，\x01",
            "真是很开心呢～\x02",
        )
    )

    CloseMessageWindow()

    #C0382
    ChrTalk(
        0xFE,
        (
            "……但是琪露露\x01",
            "好像又要出去旅行了。\x02",
        )
    )

    CloseMessageWindow()

    #C0383
    ChrTalk(
        0xFE,
        "真是个不爱待在城市里的人啊～\x02",
    )

    CloseMessageWindow()
    Jump("loc_6A38")

    label("loc_60EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_61A2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_616E")

    #C0384
    ChrTalk(
        0xFE,
        "明明和朋友约好了……\x02",
    )

    CloseMessageWindow()

    #C0385
    ChrTalk(
        0xFE,
        "结果却没有来……\x02",
    )

    CloseMessageWindow()

    #C0386
    ChrTalk(
        0xFE,
        (
            "琪露露到底在做什么啊？\x01",
            "明明说好要在面包店碰面的。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_619D")

    label("loc_616E")


    #C0387
    ChrTalk(
        0xFE,
        (
            "真是的……她该不会是\x01",
            "把约会给忘记了吧……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_619D")

    Jump("loc_6A38")

    label("loc_61A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_62C1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6263")

    #C0388
    ChrTalk(
        0xFE,
        (
            "（……奥斯卡今天\x01",
            "　多送给我一个面包呢！）\x02",
        )
    )

    CloseMessageWindow()

    #C0389
    ChrTalk(
        0xFE,
        (
            "（说是谢谢我平时\x01",
            "  一直来光顾。）\x02",
        )
    )

    CloseMessageWindow()

    #C0390
    ChrTalk(
        0xFE,
        (
            "（心跳加速……）\x01",
            "  （呼，真是吓了一跳……）\x02",
        )
    )

    CloseMessageWindow()

    #C0391
    ChrTalk(
        0xFE,
        (
            "（因为奥斯卡\x01",
            "  很帅嘛。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_62BC")

    label("loc_6263")


    #C0392
    ChrTalk(
        0xFE,
        (
            "（如、如果是常客，\x01",
            "  就会得到很多优惠呢。）\x02",
        )
    )

    CloseMessageWindow()

    #C0393
    ChrTalk(
        0xFE,
        "（嗯，从明天开始，我要天天过来。）\x02",
    )

    CloseMessageWindow()

    label("loc_62BC")

    Jump("loc_6A38")

    label("loc_62C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_63C9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_636C")

    #C0394
    ChrTalk(
        0xFE,
        (
            "我和朋友约好了\x01",
            "在纪念庆典期间要一起逛逛……\x02",
        )
    )

    CloseMessageWindow()

    #C0395
    ChrTalk(
        0xFE,
        "但她到底能不能按时赶回来呢？\x02",
    )

    CloseMessageWindow()

    #C0396
    ChrTalk(
        0xFE,
        (
            "平时总爱说些什么『对人类没兴趣』，\x01",
            "所以很让人担心啊……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_63C4")

    label("loc_636C")


    #C0397
    ChrTalk(
        0xFE,
        (
            "琪露露真的能在纪念庆典期间\x01",
            "赶回来吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0398
    ChrTalk(
        0xFE,
        (
            "应该不会忘记约定，\x01",
            "跑去很远的国家吧……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_63C4")

    Jump("loc_6A38")

    label("loc_63C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_6476")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6444")

    #C0399
    ChrTalk(
        0xFE,
        (
            "琪露露真是的，\x01",
            "好像又出去旅行了……\x02",
        )
    )

    CloseMessageWindow()

    #C0400
    ChrTalk(
        0xFE,
        (
            "这次又想去哪里呢？\x01",
            "本来还想和她一起尝尝新面包的。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_6471")

    label("loc_6444")


    #C0401
    ChrTalk(
        0xFE,
        (
            "琪露露真是个怪人呢。\x01",
            "这次又想去哪里啊？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6471")

    Jump("loc_6A38")

    label("loc_6476")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_6568")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6513")

    #C0402
    ChrTalk(
        0xFE,
        "啊，这个月的新款面包出了！\x02",
    )

    CloseMessageWindow()

    #C0403
    ChrTalk(
        0xFE,
        (
            "这家店的新款面包\x01",
            "实在是太美味了。\x01",
            "所以我总是忍不住过来买～\x02",
        )
    )

    CloseMessageWindow()

    #C0404
    ChrTalk(
        0xFE,
        "……要对我爸爸和妈妈保密哦。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_6563")

    label("loc_6513")


    #C0405
    ChrTalk(
        0xFE,
        (
            "呼……最近都快成为\x01",
            "这里的常客了。\x02",
        )
    )

    CloseMessageWindow()

    #C0406
    ChrTalk(
        0xFE,
        (
            "但是真的很美味啊。\x01",
            "这也是没办法的～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6563")

    Jump("loc_6A38")

    label("loc_6568")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_668D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_664F")

    #C0407
    ChrTalk(
        0xFE,
        "奥斯卡挺英俊的呢。\x02",
    )

    CloseMessageWindow()

    #C0408
    ChrTalk(
        0xFE,
        (
            "容姿端正，很帅气啊。\x01",
            "而且一直都很开朗从容……\x02",
        )
    )

    CloseMessageWindow()

    #C0409
    ChrTalk(
        0xFE,
        (
            "总觉得他做面包师\x01",
            "有点浪费了……\x02",
        )
    )

    CloseMessageWindow()

    #C0410
    ChrTalk(
        0xFE,
        (
            "不对，就算做面包师\x01",
            "也很帅气啊！\x02",
        )
    )

    CloseMessageWindow()

    #C0411
    ChrTalk(
        0x101,
        (
            "#0003F（……奥斯卡这家伙，\x01",
            "  一直都很受欢迎呢。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_6688")

    label("loc_664F")


    #C0412
    ChrTalk(
        0xFE,
        "奥斯卡很帅呢，\x02",
    )

    CloseMessageWindow()

    #C0413
    ChrTalk(
        0xFE,
        (
            "总觉得他做面包师\x01",
            "有点浪费了……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6688")

    Jump("loc_6A38")

    label("loc_668D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_678A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_672C")

    #C0414
    ChrTalk(
        0xFE,
        "鸡蛋三明治和牛角面包……\x02",
    )

    CloseMessageWindow()

    #C0415
    ChrTalk(
        0xFE,
        (
            "嗯，再买个甜甜圈带回去吧。\x01",
            "做点心正好呢⊥\x02",
        )
    )

    CloseMessageWindow()

    #C0416
    ChrTalk(
        0xFE,
        (
            "啊，但是会不会买得太多了……\x01",
            "可是又好想吃点心啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_6785")

    label("loc_672C")


    #C0417
    ChrTalk(
        0xFE,
        (
            "那边的面包是刚刚出炉的，\x01",
            "这边又是限时销售的新品……\x02",
        )
    )

    CloseMessageWindow()

    #C0418
    ChrTalk(
        0xFE,
        "嗯，真不知该怎么选择啊……\x02",
    )

    CloseMessageWindow()

    label("loc_6785")

    Jump("loc_6A38")

    label("loc_678A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_686A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6804")

    #C0419
    ChrTalk(
        0xFE,
        "我的朋友很奇怪吧～\x02",
    )

    CloseMessageWindow()

    #C0420
    ChrTalk(
        0xFE,
        "只要有空就会出去旅行。\x02",
    )

    CloseMessageWindow()

    #C0421
    ChrTalk(
        0xFE,
        (
            "我今天也来找她玩，\x01",
            "但她都已经出门了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_6865")

    label("loc_6804")


    #C0422
    ChrTalk(
        0xFE,
        (
            "琪露露真是的，\x01",
            "又出去旅行了啊。\x01",
            "今天也没见到她。\x02",
        )
    )

    CloseMessageWindow()

    #C0423
    ChrTalk(
        0xFE,
        (
            "嗯，真没办法，\x01",
            "今天买完面包就回去吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6865")

    Jump("loc_6A38")

    label("loc_686A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_696A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_68FC")
    OP_93(0xFE, 0x0, 0x0)

    #C0424
    ChrTalk(
        0xFE,
        "嗯嗯，这个月的新款面包……\x02",
    )

    CloseMessageWindow()

    #C0425
    ChrTalk(
        0xFE,
        (
            "有脆皮培根的\x01",
            "香辣面包……\x02",
        )
    )

    CloseMessageWindow()

    #C0426
    ChrTalk(
        0xFE,
        (
            "唔……而且还是刚烤好的。\x01",
            "看起来很好吃啊……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_6965")

    label("loc_68FC")


    #C0427
    ChrTalk(
        0xFE,
        (
            "这家面包店\x01",
            "好像每个月都有新品呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0428
    ChrTalk(
        0xFE,
        (
            "嗯，看上去真好吃……\x01",
            "……实在忍不住了，\x01",
            "还是买一个带回家吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6965")

    Jump("loc_6A38")

    label("loc_696A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_6A38")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_69E8")

    #C0429
    ChrTalk(
        0xFE,
        (
            "哇～好帅的\x01",
            "面包师啊！\x02",
        )
    )

    CloseMessageWindow()

    #C0430
    ChrTalk(
        0xFE,
        (
            "我本来是到西街\x01",
            "来和朋友见面的……\x02",
        )
    )

    CloseMessageWindow()

    #C0431
    ChrTalk(
        0xFE,
        (
            "顺道就发现了\x01",
            "这家不错的店⊥\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_6A38")

    label("loc_69E8")


    #C0432
    ChrTalk(
        0xFE,
        (
            "这家面包店的\x01",
            "氛围很棒呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0433
    ChrTalk(
        0xFE,
        (
            "呵呵，我很喜欢哦，\x01",
            "要不要买个面包带回家呢？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6A38")

    TalkEnd(0xFE)
    Return()

    # Function_13_5DB6 end

    def Function_14_6A3C(): pass

    label("Function_14_6A3C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_6A82")

    #C0434
    ChrTalk(
        0xFE,
        "今天必须要回国了。\x02",
    )

    CloseMessageWindow()

    #C0435
    ChrTalk(
        0xFE,
        (
            "得多买一些\x01",
            "特产带回去。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6B2A")

    label("loc_6A82")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_6A90")
    Jump("loc_6B2A")

    label("loc_6A90")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_6ACD")

    #C0436
    ChrTalk(
        0xFE,
        (
            "不然就在露天座位区，\x01",
            "配上咖啡一起享用吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6B2A")

    label("loc_6ACD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_6B2A")

    #C0437
    ChrTalk(
        0xFE,
        (
            "逛庆典的时候，\x01",
            "发现了这家不错的店。\x02",
        )
    )

    CloseMessageWindow()

    #C0438
    ChrTalk(
        0xFE,
        (
            "呵呵，都是些看起来\x01",
            "就很美味的面包呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6B2A")

    TalkEnd(0xFE)
    Return()

    # Function_14_6A3C end

    def Function_15_6B2E(): pass

    label("Function_15_6B2E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_6B8F")

    #C0439
    ChrTalk(
        0xFE,
        (
            "庆典的游行队伍\x01",
            "也已经参观过了……\x02",
        )
    )

    CloseMessageWindow()

    #C0440
    ChrTalk(
        0xFE,
        (
            "接下来，就悠闲地\x01",
            "在街上随便逛逛吧～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6C95")

    label("loc_6B8F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_6B9D")
    Jump("loc_6C95")

    label("loc_6B9D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_6C05")

    #C0441
    ChrTalk(
        0xFE,
        (
            "我取消了酒店的餐点服务，\x01",
            "跑到这里来了。\x02",
        )
    )

    CloseMessageWindow()

    #C0442
    ChrTalk(
        0xFE,
        (
            "还是在街上吃东西\x01",
            "更有庆典的节日气氛呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6C95")

    label("loc_6C05")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_6C95")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6C6C")

    #C0443
    ChrTalk(
        0xFE,
        (
            "克洛斯贝尔市实在很大啊，\x01",
            "我都走累了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0444
    ChrTalk(
        0xFE,
        (
            "爸爸总是一个人\x01",
            "走得飞快。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_6C95")

    label("loc_6C6C")


    #C0445
    ChrTalk(
        0xFE,
        (
            "干脆在这家面包\x01",
            "咖啡店休息一下好了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6C95")

    TalkEnd(0xFE)
    Return()

    # Function_15_6B2E end

    def Function_16_6C99(): pass

    label("Function_16_6C99")

    Call(0, 17)
    Return()

    # Function_16_6C99 end

    def Function_17_6C9D(): pass

    label("Function_17_6C9D")

    TalkBegin(0xF)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2E, 0x1, 0x1)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2E, 0x1, 0x3)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2E, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6CC2")
    Call(0, 33)
    Return()

    label("loc_6CC2")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6CCC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_83C8")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6D1C")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_6D1C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6DAC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_6D3B")
    OP_AF(0x2F)
    Jump("loc_6D9D")

    label("loc_6D3B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_6D4B")
    OP_AF(0x2E)
    Jump("loc_6D9D")

    label("loc_6D4B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_6D5B")
    OP_AF(0x2D)
    Jump("loc_6D9D")

    label("loc_6D5B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_6D6B")
    OP_AF(0x2C)
    Jump("loc_6D9D")

    label("loc_6D6B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_6D7B")
    OP_AF(0x2B)
    Jump("loc_6D9D")

    label("loc_6D7B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_6D8B")
    OP_AF(0x2A)
    Jump("loc_6D9D")

    label("loc_6D8B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_6D9B")
    OP_AF(0x29)
    Jump("loc_6D9D")

    label("loc_6D9B")

    OP_AF(0x28)

    label("loc_6D9D")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_83C3")

    label("loc_6DAC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6DC0")
    Jump("loc_83C3")

    label("loc_6DC0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_83C3")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2E, 0x1, 0x4)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6E69")

    #C0446
    ChrTalk(
        0xF,
        (
            "哦，你们好像已经\x01",
            "采到利奎姆之花了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0447
    ChrTalk(
        0xF,
        (
            "让你们费心了，真不好意思。\x01",
            "稍后必须要去向昆特先生\x01",
            "好好道歉才行。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_83C3")

    label("loc_6E69")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2E, 0x1, 0x3)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2E, 0x1, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6EF5")

    #C0448
    ChrTalk(
        0xF,
        (
            "进入位于山道的隧道后，\x01",
            "途中折向通往遗迹的岔路，\x01",
            "利奎姆之花应该就开在那条路的某处。\x02",
        )
    )

    CloseMessageWindow()

    #C0449
    ChrTalk(
        0xF,
        "路上小心点吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_83C3")

    label("loc_6EF5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x94, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6FDC")

    #C0450
    ChrTalk(
        0xF,
        (
            "我家的小桃很喜欢看书呢。\x01",
            "最近好像在看\x01",
            "一部娱乐小说。\x02",
        )
    )

    CloseMessageWindow()

    #C0451
    ChrTalk(
        0xF,
        (
            "不过，好像只得到了\x01",
            "其中的几卷……\x02",
        )
    )

    CloseMessageWindow()

    #C0452
    ChrTalk(
        0xF,
        (
            "因为看她一脸失落，\x01",
            "就忍不住进了几本到店里。\x02",
        )
    )

    CloseMessageWindow()

    #C0453
    ChrTalk(
        0xF,
        (
            "哈哈，有兴趣的话，\x01",
            "你们也看看吧。\x01",
            "虽然只有几卷而已。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x94, 6)
    Jump("loc_83C3")

    label("loc_6FDC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_7030")

    #C0454
    ChrTalk(
        0xF,
        "小桃今天回家的时候，好像都快要哭出来了……\x02",
    )

    CloseMessageWindow()

    #C0455
    ChrTalk(
        0xF,
        "发生了什么事吗？\x02",
    )

    CloseMessageWindow()
    Jump("loc_83C3")

    label("loc_7030")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_70A7")

    #C0456
    ChrTalk(
        0xF,
        "听说最近有很多人失踪，是真的吗？\x02",
    )

    CloseMessageWindow()

    #C0457
    ChrTalk(
        0xF,
        "难道是……人贩子吗？\x02",
    )

    CloseMessageWindow()

    #C0458
    ChrTalk(
        0xF,
        (
            "好可怕啊……\x01",
            "一会要提醒小桃留意点。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_83C3")

    label("loc_70A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_71D1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7165")

    #C0459
    ChrTalk(
        0xF,
        (
            "我家的小桃，最近\x01",
            "好像开始和朋友一起玩了。\x02",
        )
    )

    CloseMessageWindow()

    #C0460
    ChrTalk(
        0xF,
        "她终于克服害羞内向的毛病了啊。\x02",
    )

    CloseMessageWindow()

    #C0461
    ChrTalk(
        0xF,
        (
            "虽然最近听说了一些\x01",
            "可怕事件的传闻……\x01",
            "但这件事还是让我稍微觉得好过了一点。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_71CC")

    label("loc_7165")


    #C0462
    ChrTalk(
        0xF,
        (
            "虽然最近听说了一些可怕的传闻，\x01",
            "不过能看到孩子的笑容，比什么都重要啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0463
    ChrTalk(
        0xF,
        "希望能早日恢复和平呢。\x02",
    )

    CloseMessageWindow()

    label("loc_71CC")

    Jump("loc_83C3")

    label("loc_71D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_730B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7298")

    #C0464
    ChrTalk(
        0xF,
        (
            "哟，欢迎光临。\x01",
            "欢迎来到塔利兹商店。\x02",
        )
    )

    CloseMessageWindow()

    #C0465
    ChrTalk(
        0xF,
        (
            "……最近到处都能听到\x01",
            "关于鲁巴彻的传闻。\x02",
        )
    )

    CloseMessageWindow()

    #C0466
    ChrTalk(
        0xF,
        (
            "比如他们又在市区里\x01",
            "引起了什么纠纷……\x02",
        )
    )

    CloseMessageWindow()

    #C0467
    ChrTalk(
        0xF,
        (
            "我们家也有小孩子，\x01",
            "所以得注意一点呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_7306")

    label("loc_7298")


    #C0468
    ChrTalk(
        0xF,
        (
            "和我有来往的商人之中，\x01",
            "好像也有被鲁巴彻找过麻烦的人。\x02",
        )
    )

    CloseMessageWindow()

    #C0469
    ChrTalk(
        0xF,
        (
            "好可怕啊……我家也有小孩子，\x01",
            "必须得小心点啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7306")

    Jump("loc_83C3")

    label("loc_730B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_741E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_73BE")

    #C0470
    ChrTalk(
        0xF,
        (
            "哎呀哎呀，终于能恢复到\x01",
            "正常的生活了。\x02",
        )
    )

    CloseMessageWindow()

    #C0471
    ChrTalk(
        0xF,
        (
            "连续闹了五天，还真想享受一下\x01",
            "悠闲的时光啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0472
    ChrTalk(
        0xF,
        (
            "虽然爱尔莎\x01",
            "听了之后就对我说：\x01",
            "『你不是一直很悠闲吗』。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_7419")

    label("loc_73BE")


    #C0473
    ChrTalk(
        0xF,
        (
            "纪念庆典结束之后，\x01",
            "感觉终于回到了正常的生活。\x02",
        )
    )

    CloseMessageWindow()

    #C0474
    ChrTalk(
        0xF,
        "嗯，果然还是安宁平静的日子最棒了。\x02",
    )

    CloseMessageWindow()

    label("loc_7419")

    Jump("loc_83C3")

    label("loc_741E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_7519")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_74AC")

    #C0475
    ChrTalk(
        0xF,
        (
            "爱尔莎和小桃\x01",
            "去了米修拉姆哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0476
    ChrTalk(
        0xF,
        (
            "我对她们说，\x01",
            "要玩得尽兴一点。\x02",
        )
    )

    CloseMessageWindow()

    #C0477
    ChrTalk(
        0xF,
        (
            "她们总在店里帮忙，\x01",
            "偶尔也得休息一下呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_7514")

    label("loc_74AC")


    #C0478
    ChrTalk(
        0xF,
        (
            "爱尔莎和小桃现在\x01",
            "应该已经去了米修拉姆。\x02",
        )
    )

    CloseMessageWindow()

    #C0479
    ChrTalk(
        0xF,
        (
            "虽然店里忙翻了……\x01",
            "不过只有今天的话，还是能撑过去的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7514")

    Jump("loc_83C3")

    label("loc_7519")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 7)), scpexpr(EXPR_END)), "loc_75E3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_759F")

    #C0480
    ChrTalk(
        0xF,
        (
            "对了，今天是\x01",
            "游行的日子。\x02",
        )
    )

    CloseMessageWindow()

    #C0481
    ChrTalk(
        0xF,
        "唔，糟了。\x02",
    )

    CloseMessageWindow()

    #C0482
    ChrTalk(
        0xF,
        (
            "因为我对这种东西没什么兴趣，\x01",
            "所以没注意\x01",
            "庆典的日程呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_75DE")

    label("loc_759F")


    #C0483
    ChrTalk(
        0xF,
        "今天可是游行的日子啊。\x02",
    )

    CloseMessageWindow()

    #C0484
    ChrTalk(
        0xF,
        (
            "希望爱尔莎和小桃\x01",
            "能玩得尽兴。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_75DE")

    Jump("loc_83C3")

    label("loc_75E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_7788")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAD, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_772B")

    #C0485
    ChrTalk(
        0x101,
        (
            "#0001F（嗯，这个人\x01",
            "  可能知道些什么吧……）\x02",
        )
    )

    CloseMessageWindow()

    #A0486
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

    #C0487
    ChrTalk(
        0xF,
        (
            "走丢的孩子啊……\x01",
            "那情况还真是紧急呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0488
    ChrTalk(
        0xF,
        (
            "唔，我错过\x01",
            "游行了。\x01",
            "只看到了一点点……\x02",
        )
    )

    CloseMessageWindow()

    #C0489
    ChrTalk(
        0xF,
        (
            "而且还是远远地眺望了一下，\x01",
            "所以没看太清楚啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0490
    ChrTalk(
        0x101,
        (
            "#0000F这样啊……\x01",
            "谢谢您了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xAD, 3)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 25)
    Jump("loc_7783")

    label("loc_772B")


    #C0491
    ChrTalk(
        0xF,
        (
            "我错过游行了呢，\x01",
            "只是远远地眺望了一下。\x02",
        )
    )

    CloseMessageWindow()

    #C0492
    ChrTalk(
        0xF,
        (
            "所以不知道那个孩子\x01",
            "到底有没有出现过。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7783")

    Jump("loc_83C3")

    label("loc_7788")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_7850")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_780E")

    #C0493
    ChrTalk(
        0xF,
        (
            "对了，今天\x01",
            "是游行的日子呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0494
    ChrTalk(
        0xF,
        "唔，真糟糕。\x02",
    )

    CloseMessageWindow()

    #C0495
    ChrTalk(
        0xF,
        (
            "我对这种活动没什么兴趣，\x01",
            "所以都没注意\x01",
            "庆典的日程。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_784B")

    label("loc_780E")


    #C0496
    ChrTalk(
        0xF,
        "今天是游行的日子啊。\x02",
    )

    CloseMessageWindow()

    #C0497
    ChrTalk(
        0xF,
        (
            "希望爱尔莎和小桃\x01",
            "能玩得尽兴。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_784B")

    Jump("loc_83C3")

    label("loc_7850")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_792C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_78F6")

    #C0498
    ChrTalk(
        0xF,
        (
            "爱尔莎和小桃\x01",
            "现在正在街上逛着呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0499
    ChrTalk(
        0xF,
        (
            "因为机会难得，所以我\x01",
            "就让她们出去逛一圈。\x02",
        )
    )

    CloseMessageWindow()

    #C0500
    ChrTalk(
        0xF,
        (
            "虽然我还要看店，但至少希望家人能\x01",
            "玩得开开心心。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_7927")

    label("loc_78F6")


    #C0501
    ChrTalk(
        0xF,
        (
            "毕竟是难得的庆典，\x01",
            "希望家人能够玩得开心点。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7927")

    Jump("loc_83C3")

    label("loc_792C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_7A26")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_79C5")

    #C0502
    ChrTalk(
        0xF,
        (
            "虽然是纪念庆典，\x01",
            "但我并没打算\x01",
            "做什么特别的事……\x02",
        )
    )

    CloseMessageWindow()

    #C0503
    ChrTalk(
        0xF,
        (
            "今年的庆典\x01",
            "办得很隆重啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0504
    ChrTalk(
        0xF,
        (
            "唔，我们店里\x01",
            "是不是也该办点活动呢？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_7A21")

    label("loc_79C5")


    #C0505
    ChrTalk(
        0xF,
        (
            "我们店是不是也该\x01",
            "办个大减价之类的活动啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0506
    ChrTalk(
        0xF,
        (
            "哈哈……那样的话，可真是\x01",
            "迟来的优惠呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7A21")

    Jump("loc_83C3")

    label("loc_7A26")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_7B22")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7ACD")

    #C0507
    ChrTalk(
        0xF,
        (
            "克洛斯贝尔自治州到今年\x01",
            "也创立七十周年了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0508
    ChrTalk(
        0xF,
        (
            "算起来……它正好是在\x01",
            "我爷爷年轻的时候\x01",
            "诞生的呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0509
    ChrTalk(
        0xF,
        (
            "这样想的话，\x01",
            "真让人有点感慨啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_7B1D")

    label("loc_7ACD")


    #C0510
    ChrTalk(
        0xF,
        (
            "平时都不太会\x01",
            "去想自治州的事情……\x02",
        )
    )

    CloseMessageWindow()

    #C0511
    ChrTalk(
        0xF,
        (
            "但仔细想想的话，\x01",
            "还真是让人感慨啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7B1D")

    Jump("loc_83C3")

    label("loc_7B22")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_7BE0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7B93")

    #C0512
    ChrTalk(
        0xF,
        (
            "我和布里吉塔\x01",
            "刚才在聊那条警犬的事。\x02",
        )
    )

    CloseMessageWindow()

    #C0513
    ChrTalk(
        0xF,
        (
            "刚刚还来过我家……\x01",
            "不知道又去哪里了……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_7BDB")

    label("loc_7B93")


    #C0514
    ChrTalk(
        0xF,
        (
            "那条警犬\x01",
            "不知道又去哪里了……\x02",
        )
    )

    CloseMessageWindow()

    #C0515
    ChrTalk(
        0xF,
        (
            "它好像总在这附近\x01",
            "给我们巡逻呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7BDB")

    Jump("loc_83C3")

    label("loc_7BE0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_7D83")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7CCE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7C5E")

    #C0516
    ChrTalk(
        0xF,
        (
            "啊、啊哈哈……\x01",
            "真是条大狗呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0517
    ChrTalk(
        0xF,
        (
            "对了，最近客人们常议论的\x01",
            "就是那条警犬啊……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_7CC9")

    label("loc_7C5E")


    #C0518
    ChrTalk(
        0xF,
        (
            "看起来的确是条\x01",
            "很可靠的警犬……\x01",
            "但感觉它的架子很大呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0519
    ChrTalk(
        0xF,
        (
            "刚刚和它打招呼，\x01",
            "竟然只哼了一声当作回应。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7CC9")

    Jump("loc_7D7E")

    label("loc_7CCE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7D36")

    #C0520
    ChrTalk(
        0xF,
        (
            "那条警犬每周\x01",
            "会来我们店里两三次。\x02",
        )
    )

    CloseMessageWindow()

    #C0521
    ChrTalk(
        0xF,
        (
            "刚刚虽然也来过……\x01",
            "但不知道又去哪里了……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_7D7E")

    label("loc_7D36")


    #C0522
    ChrTalk(
        0xF,
        (
            "那条警犬\x01",
            "不知道又去哪里了……\x02",
        )
    )

    CloseMessageWindow()

    #C0523
    ChrTalk(
        0xF,
        (
            "它好像总在这附近\x01",
            "给我们巡逻呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7D7E")

    Jump("loc_83C3")

    label("loc_7D83")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_7E0D")

    #C0524
    ChrTalk(
        0xF,
        (
            "爱尔莎一直在说\x01",
            "彩虹剧团的事。\x02",
        )
    )

    CloseMessageWindow()

    #C0525
    ChrTalk(
        0xF,
        (
            "唔，果然是\x01",
            "很想去看吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0526
    ChrTalk(
        0xF,
        (
            "虽然她很少提起，\x01",
            "不过她从以前开始就很向往\x01",
            "彩虹剧团呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_83C3")

    label("loc_7E0D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_7E84")

    #C0527
    ChrTalk(
        0xF,
        (
            "哈罗德先生家里\x01",
            "好像也有小孩啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0528
    ChrTalk(
        0xF,
        (
            "他们和我们家一样，\x01",
            "从事家族经营式的买卖。\x01",
            "总觉得很有亲切感啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_83C3")

    label("loc_7E84")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_7F99")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7F2F")

    #C0529
    ChrTalk(
        0xF,
        (
            "哈罗德先生说，\x01",
            "这次蜂蜜的价格确定之后，\x01",
            "他就会来通知我。\x02",
        )
    )

    CloseMessageWindow()

    #C0530
    ChrTalk(
        0xF,
        (
            "真是很诚恳啊。\x01",
            "身为店主我也很高兴呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0531
    ChrTalk(
        0xF,
        (
            "到时候顺便谈谈\x01",
            "下次进货的事情吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_7F94")

    label("loc_7F2F")


    #C0532
    ChrTalk(
        0xF,
        (
            "我和哈罗德先生\x01",
            "也有三年的交情了，\x01",
            "他真是个很诚恳的人啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0533
    ChrTalk(
        0xF,
        (
            "到时候顺便谈谈\x01",
            "下次进货的事情吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7F94")

    Jump("loc_83C3")

    label("loc_7F99")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_8077")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_800B")

    #C0534
    ChrTalk(
        0xF,
        (
            "最近都没有看见过\x01",
            "隆和亨利呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0535
    ChrTalk(
        0xF,
        (
            "平时经常会在\x01",
            "我们店门口玩……\x01",
            "到底去哪里了呢？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_8072")

    label("loc_800B")


    #C0536
    ChrTalk(
        0xF,
        (
            "最近都没有看见过\x01",
            "隆和亨利呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0537
    ChrTalk(
        0xF,
        (
            "我记得隆\x01",
            "应该是住在贝尔海姆的。\x01",
            "是不是生病了，在家睡觉休息呢？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8072")

    Jump("loc_83C3")

    label("loc_8077")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_81B4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_814B")

    #C0538
    ChrTalk(
        0xF,
        (
            "有位商人会从阿尔摩利卡村\x01",
            "帮我们批发蜂蜜。\x02",
        )
    )

    CloseMessageWindow()

    #C0539
    ChrTalk(
        0xF,
        (
            "由于最近的行情很不错，\x01",
            "对方就来通知我说\x01",
            "价格可能会上涨。\x02",
        )
    )

    CloseMessageWindow()

    #C0540
    ChrTalk(
        0xF,
        (
            "只要有什么情况，\x01",
            "那个人都会事先告诉我。\x01",
            "不但有生意头脑，人品也很不错。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_81AF")

    label("loc_814B")


    #C0541
    ChrTalk(
        0xF,
        (
            "他总会提早告诉我情报，\x01",
            "这点真是让人很感谢啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0542
    ChrTalk(
        0xF,
        (
            "因为价格要上涨了，\x01",
            "所以我得提前多进点货啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_81AF")

    Jump("loc_83C3")

    label("loc_81B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_82BD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 6)), scpexpr(EXPR_END)), "loc_824B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_822C")

    #C0543
    ChrTalk(
        0xF,
        "我家的小桃很认生呢。\x02",
    )

    CloseMessageWindow()

    #C0544
    ChrTalk(
        0xF,
        (
            "一有客人来，\x01",
            "她就会躲到里面去。\x01",
            "唔，真拿她没办法啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_8246")

    label("loc_822C")


    #C0545
    ChrTalk(
        0xF,
        "我家的小桃很认生呢。\x02",
    )

    CloseMessageWindow()

    label("loc_8246")

    Jump("loc_82B8")

    label("loc_824B")


    #C0546
    ChrTalk(
        0xF,
        (
            "我们这里是杂货店，\x01",
            "贩卖食材和日用品。\x02",
        )
    )

    CloseMessageWindow()

    #C0547
    ChrTalk(
        0xF,
        (
            "我进的都是一些\x01",
            "能给大家带来便利的商品，\x01",
            "不嫌弃的话请看看吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_82B8")

    Jump("loc_83C3")

    label("loc_82BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_83C3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8369")

    #C0548
    ChrTalk(
        0xF,
        "哟，欢迎光临。\x02",
    )

    CloseMessageWindow()

    #C0549
    ChrTalk(
        0xF,
        (
            "想买日用品就来我这里吧！\x01",
            "我们是招牌老店『塔利兹商店』～\x02",
        )
    )

    CloseMessageWindow()

    #C0550
    ChrTalk(
        0xF,
        (
            "顺便一提，『悠闲地生活吧』\x01",
            "就是我们的口号。\x01",
            "请随便看看吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_83C3")

    label("loc_8369")


    #C0551
    ChrTalk(
        0xF,
        (
            "我们的口号就是\x01",
            "『悠闲地生活吧』。\x02",
        )
    )

    CloseMessageWindow()

    #C0552
    ChrTalk(
        0xF,
        (
            "如你所见，这里的气氛悠闲轻松，\x01",
            "请随便看看吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_83C3")

    Jump("loc_6CCC")

    label("loc_83C8")

    TalkEnd(0xF)
    Return()

    # Function_17_6C9D end

    def Function_18_83CC(): pass

    label("Function_18_83CC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_8491")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_843C")

    #C0553
    ChrTalk(
        0xFE,
        (
            "小桃真是的……\x01",
            "今天和朋友们发生什么事了？\x02",
        )
    )

    CloseMessageWindow()

    #C0554
    ChrTalk(
        0xFE,
        (
            "一直在闹别扭，\x01",
            "都不和我说话。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_848C")

    label("loc_843C")


    #C0555
    ChrTalk(
        0xFE,
        (
            "孩子之间总会产生\x01",
            "各种各样的问题啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0556
    ChrTalk(
        0xFE,
        (
            "做点好吃的东西，\x01",
            "去安慰安慰她吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_848C")

    Jump("loc_8D59")

    label("loc_8491")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_8562")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_84FB")

    #C0557
    ChrTalk(
        0xFE,
        (
            "伊安律师最近好像很忙啊……\x01",
            "手头似乎有很多工作。\x02",
        )
    )

    CloseMessageWindow()

    #C0558
    ChrTalk(
        0xFE,
        "助手皮特也很辛苦呢。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_855D")

    label("loc_84FB")


    #C0559
    ChrTalk(
        0xFE,
        (
            "我丈夫说过，\x01",
            "最近的事件好像增加了不少，\x01",
            "大概就是这个原因吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0560
    ChrTalk(
        0xFE,
        "伊安律师和皮特都很辛苦啊。\x02",
    )

    CloseMessageWindow()

    label("loc_855D")

    Jump("loc_8D59")

    label("loc_8562")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_8674")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_861C")

    #C0561
    ChrTalk(
        0xFE,
        (
            "……我刚刚看了看外面，\x01",
            "发现小桃在和朋友们一起玩呢～！\x02",
        )
    )

    CloseMessageWindow()

    #C0562
    ChrTalk(
        0xFE,
        (
            "那个害羞内向的孩子也开始改变了……\x01",
            "身为母亲，我真是很高兴啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0563
    ChrTalk(
        0xFE,
        (
            "今天晚上就煮\x01",
            "红豆糯米饭吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_866F")

    label("loc_861C")


    #C0564
    ChrTalk(
        0xFE,
        (
            "小桃终于有所改变了啊～\x01",
            "我和丈夫都在暗地里高兴呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0565
    ChrTalk(
        0xFE,
        "今晚可要好好庆祝一下。\x02",
    )

    CloseMessageWindow()

    label("loc_866F")

    Jump("loc_8D59")

    label("loc_8674")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_86CD")

    #C0566
    ChrTalk(
        0xFE,
        "今天有新商品送来了。\x02",
    )

    CloseMessageWindow()

    #C0567
    ChrTalk(
        0xFE,
        (
            "因为价格有点贵，\x01",
            "所以摆放的时候要小心一点。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8D59")

    label("loc_86CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_86DB")
    Jump("loc_8D59")

    label("loc_86DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_87EA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8782")

    #C0568
    ChrTalk(
        0xFE,
        (
            "小桃也会来帮忙，\x01",
            "她很懂事，真是帮了大忙呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0569
    ChrTalk(
        0xFE,
        (
            "不过……她总是\x01",
            "在店里帮忙，\x01",
            "要不然就一个人看书。\x02",
        )
    )

    CloseMessageWindow()

    #C0570
    ChrTalk(
        0xFE,
        (
            "如果偶尔也能去\x01",
            "外面玩玩就好了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_87E5")

    label("loc_8782")


    #C0571
    ChrTalk(
        0xFE,
        (
            "虽然给店里帮忙\x01",
            "是件好事……\x01",
            "不过，小桃真的觉得开心吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0572
    ChrTalk(
        0xFE,
        (
            "事实上，\x01",
            "她或许也想去外面玩玩呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_87E5")

    Jump("loc_8D59")

    label("loc_87EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_88DA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_888D")

    #C0573
    ChrTalk(
        0xFE,
        "马上就要到创立纪念庆典了～\x02",
    )

    CloseMessageWindow()

    #C0574
    ChrTalk(
        0xFE,
        (
            "但是我丈夫好像没兴趣\x01",
            "搞大减价之类的活动。\x02",
        )
    )

    CloseMessageWindow()

    #C0575
    ChrTalk(
        0xFE,
        (
            "呼，对这类节日庆典毫无兴趣，\x01",
            "倒真是很符合他的个性。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_88D5")

    label("loc_888D")


    #C0576
    ChrTalk(
        0xFE,
        (
            "话说回来……\x01",
            "感觉下面很安静呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0577
    ChrTalk(
        0xFE,
        (
            "我丈夫他，\x01",
            "不会是在打瞌睡吧？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_88D5")

    Jump("loc_8D59")

    label("loc_88DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_89FC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_898A")

    #C0578
    ChrTalk(
        0xFE,
        (
            "彩虹剧团的新剧，\x01",
            "好像会有新演员参加演出呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0579
    ChrTalk(
        0xFE,
        (
            "而且刚刚出道，\x01",
            "就和那个大明星伊莉娅小姐同台表演。\x02",
        )
    )

    CloseMessageWindow()

    #C0580
    ChrTalk(
        0xFE,
        (
            "感觉好厉害啊……\x01",
            "到底是个什么样的人呢？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_89F7")

    label("loc_898A")


    #C0581
    ChrTalk(
        0xFE,
        (
            "克洛斯贝尔的女孩子们\x01",
            "都曾憧憬过彩虹剧团。\x02",
        )
    )

    CloseMessageWindow()

    #C0582
    ChrTalk(
        0xFE,
        (
            "出道作就能和伊莉娅小姐\x01",
            "同台表演……\x01",
            "真是像梦幻般幸运呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_89F7")

    Jump("loc_8D59")

    label("loc_89FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_8A93")

    #C0583
    ChrTalk(
        0xFE,
        "小桃今天去主日学校上课了。\x02",
    )

    CloseMessageWindow()

    #C0584
    ChrTalk(
        0xFE,
        (
            "那孩子相当害羞内向，\x01",
            "我有点担心\x01",
            "她是否能融入集体。\x02",
        )
    )

    CloseMessageWindow()

    #C0585
    ChrTalk(
        0xFE,
        (
            "以后有空时，我去找修女\x01",
            "问问上课时的情况吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8D59")

    label("loc_8A93")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_8B70")
    OP_4B(0x15, 0xFF)
    OP_93(0xFE, 0xB4, 0x0)

    #C0586
    ChrTalk(
        0xFE,
        (
            "不不，我才是\x01",
            "一直受您的照顾。\x02",
        )
    )

    CloseMessageWindow()

    #C0587
    ChrTalk(
        0xFE,
        (
            "那么，\x01",
            "下个月的采购\x01",
            "就按照这个方案吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0588
    ChrTalk(
        0x15,
        (
            "#3603F食材增加一成。\x01",
            "嗯，但希望价格能优惠点吗……\x02\x03",

            "#3600F哈哈哈，请包在我身上吧。\x01",
            "塔利兹先生\x01",
            "是老客户了。\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x15, 0xFF)
    Jump("loc_8D59")

    label("loc_8B70")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_8CE4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8C7C")

    #C0589
    ChrTalk(
        0xFE,
        (
            "我刚才去中央广场\x01",
            "买东西……\x02",
        )
    )

    CloseMessageWindow()

    #C0590
    ChrTalk(
        0xFE,
        (
            "结果发现旁边那幢旧大楼\x01",
            "不知何时搬进了一家\x01",
            "不知名的公司。\x02",
        )
    )

    CloseMessageWindow()

    #C0591
    ChrTalk(
        0xFE,
        (
            "到底是什么时候搬进去的呢？\x01",
            "完全没有注意到啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0592
    ChrTalk(
        0x104,
        "#0305F（……是在说支援科的那栋楼吧？）\x02",
    )

    CloseMessageWindow()

    #C0593
    ChrTalk(
        0x101,
        (
            "#0012F（哈哈……知名度果然还\x01",
            "  差得远呢……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_8CDF")

    label("loc_8C7C")


    #C0594
    ChrTalk(
        0xFE,
        (
            "中央广场边缘的那栋大楼，\x01",
            "不知在何时，搬进了\x01",
            "一家不知名的公司。\x02",
        )
    )

    CloseMessageWindow()

    #C0595
    ChrTalk(
        0xFE,
        (
            "那一带的变化\x01",
            "相当频繁呀。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8CDF")

    Jump("loc_8D59")

    label("loc_8CE4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_8D42")

    #C0596
    ChrTalk(
        0xFE,
        "做菜做菜……¤\x02",
    )

    CloseMessageWindow()

    #C0597
    ChrTalk(
        0xFE,
        (
            "卖剩的蔬菜不会扔掉，\x01",
            "而是我们自家吃掉呢。\x01",
            "很能省钱吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8D59")

    label("loc_8D42")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_8D50")
    Jump("loc_8D59")

    label("loc_8D50")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_8D59")

    label("loc_8D59")

    TalkEnd(0xFE)
    Return()

    # Function_18_83CC end

    def Function_19_8D5D(): pass

    label("Function_19_8D5D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_8D8F")

    #C0598
    ChrTalk(
        0xFE,
        (
            "呜呜，隆\x01",
            "果然很爱捉弄人……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9519")

    label("loc_8D8F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_906D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAD, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8FFD")

    #C0599
    ChrTalk(
        0xFE,
        (
            "纪念庆典最后一天，\x01",
            "我和隆一起去逛了露天店。\x02",
        )
    )

    CloseMessageWindow()

    #C0600
    ChrTalk(
        0xFE,
        "庆典我过得好开心啊……\x02",
    )

    CloseMessageWindow()

    #C0601
    ChrTalk(
        0xFE,
        "要是再能一起玩就好了……\x02",
    )

    CloseMessageWindow()
    OP_63(0x153, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0602
    ChrTalk(
        0x153,
        "#1110F庆典～？\x02",
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_63(0xFE, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    TurnDirection(0xFE, 0x153, 500)
    OP_64(0xFE)

    #C0603
    ChrTalk(
        0xFE,
        (
            "不、不……\x01",
            "没、没什么……\x02",
        )
    )

    CloseMessageWindow()

    #C0604
    ChrTalk(
        0xFE,
        "那个，庆典和朋友一起玩了。\x02",
    )

    CloseMessageWindow()

    #C0605
    ChrTalk(
        0xFE,
        "非常开心呢……\x02",
    )

    CloseMessageWindow()

    #C0606
    ChrTalk(
        0x153,
        (
            "#1105F嗯，真不错呢～……\x02\x03",

            "#1109F喂，罗伊德，\x01",
            "下次大家也一起去庆典玩吧～？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0xEF, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0607
    ChrTalk(
        0x101,
        (
            "#0000F说、说得也是……\x01",
            "这提议不坏呢。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_8FA0")

    #C0608
    ChrTalk(
        0x102,
        "#0100F不过要等明年了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_8FF5")

    label("loc_8FA0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_8FCA")

    #C0609
    ChrTalk(
        0x103,
        "#0202F但是要到明年了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_8FF5")

    label("loc_8FCA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_8FF5")

    #C0610
    ChrTalk(
        0x104,
        "#0300F不过也只能等到明年啦。\x02",
    )

    CloseMessageWindow()

    label("loc_8FF5")

    SetScenarioFlags(0xAD, 6)
    Jump("loc_9068")

    label("loc_8FFD")


    #C0611
    ChrTalk(
        0xFE,
        (
            "纪念庆典最后一天，\x01",
            "我和隆一起去逛了露天店。\x02",
        )
    )

    CloseMessageWindow()

    #C0612
    ChrTalk(
        0xFE,
        "庆典我过得好开心啊……\x02",
    )

    CloseMessageWindow()

    #C0613
    ChrTalk(
        0xFE,
        "要是再能一起玩就好了……\x02",
    )

    CloseMessageWindow()

    label("loc_9068")

    Jump("loc_9519")

    label("loc_906D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_90B6")

    #C0614
    ChrTalk(
        0xFE,
        "呜呜……我要休息了……\x02",
    )

    CloseMessageWindow()

    #C0615
    ChrTalk(
        0xFE,
        (
            "因为和客人说话\x01",
            "很累嘛……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9519")

    label("loc_90B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_90C4")
    Jump("loc_9519")

    label("loc_90C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_911C")

    #C0616
    ChrTalk(
        0xFE,
        (
            "嘿嘿嘿，狗狗\x01",
            "好可爱啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0617
    ChrTalk(
        0xFE,
        (
            "以后还想再和它玩，\x01",
            "它还会和我玩吗……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9519")

    label("loc_911C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_9211")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_9184")

    #C0618
    ChrTalk(
        0xFE,
        (
            "嘿嘿嘿，狗狗\x01",
            "好可爱啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0619
    ChrTalk(
        0xFE,
        (
            "还想再和它玩一会……\x01",
            "它还愿意和我玩吗……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_920C")

    label("loc_9184")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_91DB")
    OP_93(0xFE, 0xB4, 0x0)

    #C0620
    ChrTalk(
        0xFE,
        "（摸摸）……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x0, 500)

    #C0621
    ChrTalk(
        0xFE,
        (
            "嘿嘿嘿，狗狗\x01",
            "好像感觉很舒服哦。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_920C")

    label("loc_91DB")

    OP_93(0xFE, 0xB4, 0x0)

    #C0622
    ChrTalk(
        0xFE,
        "（摸摸）……\x02",
    )

    CloseMessageWindow()

    #C0623
    ChrTalk(
        0xFE,
        "狗狗，好可爱啊……\x02",
    )

    CloseMessageWindow()

    label("loc_920C")

    Jump("loc_9519")

    label("loc_9211")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_9293")
    OP_93(0xFE, 0x5A, 0x0)

    #C0624
    ChrTalk(
        0xFE,
        "（忙忙碌碌）……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x0, 500)

    #C0625
    ChrTalk(
        0xFE,
        (
            "新商品到货了，\x01",
            "所以要摆放起来。\x02",
        )
    )

    CloseMessageWindow()

    #C0626
    ChrTalk(
        0xFE,
        (
            "瓶子的标签要擦干净，\x01",
            "让大家都能看到。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9519")

    label("loc_9293")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_9368")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9311")

    #C0627
    ChrTalk(
        0xFE,
        (
            "隆说他被一只\x01",
            "很大的狗狗救了。\x02",
        )
    )

    CloseMessageWindow()

    #C0628
    ChrTalk(
        0xFE,
        (
            "真好啊……\x01",
            "小桃也想玩……\x02",
        )
    )

    CloseMessageWindow()

    #C0629
    ChrTalk(
        0xFE,
        (
            "不、不行……\x01",
            "不能在路上玩。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_9363")

    label("loc_9311")


    #C0630
    ChrTalk(
        0xFE,
        (
            "会有导力车通过的，\x01",
            "所以不能在路上玩。\x02",
        )
    )

    CloseMessageWindow()

    #C0631
    ChrTalk(
        0xFE,
        (
            "隆，一定要\x01",
            "好好听大人的话才行……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9363")

    Jump("loc_9519")

    label("loc_9368")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_94CF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 6)), scpexpr(EXPR_END)), "loc_9415")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_93E0")

    #C0632
    ChrTalk(
        0xFE,
        "……我不太擅长和皮特相处。\x02",
    )

    CloseMessageWindow()

    #C0633
    ChrTalk(
        0xFE,
        (
            "之前他对我发火，\x01",
            "让我『把话说得\x01",
            "更清楚些』……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_9410")

    label("loc_93E0")


    #C0634
    ChrTalk(
        0xFE,
        "皮特虽然人很好，但我就是不擅长和他相处……\x02",
    )

    CloseMessageWindow()

    label("loc_9410")

    Jump("loc_94CA")

    label("loc_9415")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9490")

    #C0635
    ChrTalk(
        0xFE,
        (
            "隆、亨利，\x01",
            "我们一起玩吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0636
    ChrTalk(
        0xFE,
        "#2S我、我们一起玩吧……\x02",
    )

    CloseMessageWindow()

    #C0637
    ChrTalk(
        0xFE,
        (
            "……为了到时候不紧张，\x01",
            "要多练习几次。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_94CA")

    label("loc_9490")


    #C0638
    ChrTalk(
        0xFE,
        "我、我们一起玩吧……\x02",
    )

    CloseMessageWindow()

    #C0639
    ChrTalk(
        0xFE,
        "……要是能说出口就好了……\x02",
    )

    CloseMessageWindow()

    label("loc_94CA")

    Jump("loc_9519")

    label("loc_94CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_9519")

    #C0640
    ChrTalk(
        0xFE,
        (
            "隆和亨利，\x01",
            "一直都很开心啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0641
    ChrTalk(
        0xFE,
        "小桃也想和他们一起玩……\x02",
    )

    CloseMessageWindow()

    label("loc_9519")

    TalkEnd(0xFE)
    Return()

    # Function_19_8D5D end

    def Function_20_951D(): pass

    label("Function_20_951D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_952E")
    Jump("loc_96A5")

    label("loc_952E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_9621")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_95E7")

    #C0642
    ChrTalk(
        0xFE,
        (
            "伊安律师最近很忙，\x01",
            "教我学习法律知识的时间\x01",
            "都减少了很多。\x02",
        )
    )

    CloseMessageWindow()

    #C0643
    ChrTalk(
        0xFE,
        (
            "但是，看着伊安律师工作时的样子，\x01",
            "我也有种自豪感。\x02",
        )
    )

    CloseMessageWindow()

    #C0644
    ChrTalk(
        0xFE,
        (
            "我也想早日学成，\x01",
            "帮上伊安律师的忙。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_961C")

    label("loc_95E7")


    #C0645
    ChrTalk(
        0xFE,
        (
            "真希望能早日成为合格的律师，\x01",
            "帮上伊安律师的忙。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_961C")

    Jump("loc_96A5")

    label("loc_9621")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_962F")
    Jump("loc_96A5")

    label("loc_962F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_96A5")

    #C0646
    ChrTalk(
        0xFE,
        (
            "说起伊安律师，\x01",
            "他午饭就只喝一杯咖啡了事，\x01",
            "不注重健康也要有个限度啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0647
    ChrTalk(
        0xFE,
        (
            "所以我要\x01",
            "为他准备好食物才行。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_96A5")

    TalkEnd(0xFE)
    Return()

    # Function_20_951D end

    def Function_21_96A9(): pass

    label("Function_21_96A9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_96BA")
    Jump("loc_9902")

    label("loc_96BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_977F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9739")

    #C0648
    ChrTalk(
        0xFE,
        (
            "我丈夫从早上开始，\x01",
            "就在事务所里坐立不安的。\x02",
        )
    )

    CloseMessageWindow()

    #C0649
    ChrTalk(
        0xFE,
        (
            "呵呵，因为我丈夫一直\x01",
            "对那栋大楼有特殊感情呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_977A")

    label("loc_9739")


    #C0650
    ChrTalk(
        0xFE,
        (
            "我丈夫从一大早\x01",
            "就开始坐立不安的。\x02",
        )
    )

    CloseMessageWindow()

    #C0651
    ChrTalk(
        0xFE,
        "呵呵，得早点回去呢。\x02",
    )

    CloseMessageWindow()

    label("loc_977A")

    Jump("loc_9902")

    label("loc_977F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_9843")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_97EF")

    #C0652
    ChrTalk(
        0xFE,
        (
            "那条传说中的狗，\x01",
            "好像刚刚还来过\x01",
            "塔利兹先生这里。\x02",
        )
    )

    CloseMessageWindow()

    #C0653
    ChrTalk(
        0xFE,
        (
            "真遗憾，\x01",
            "我也想见见它啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_983E")

    label("loc_97EF")


    #C0654
    ChrTalk(
        0xFE,
        (
            "塔利兹先生说，\x01",
            "它好像偶尔会过来。\x02",
        )
    )

    CloseMessageWindow()

    #C0655
    ChrTalk(
        0xFE,
        (
            "呵呵，明天\x01",
            "要更早一点\x01",
            "过来看看啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_983E")

    Jump("loc_9902")

    label("loc_9843")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_9902")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_98B6")

    #C0656
    ChrTalk(
        0xFE,
        (
            "我之前和小桃打了个招呼，\x01",
            "但她扭扭捏捏地逃到楼上去了。\x02",
        )
    )

    CloseMessageWindow()

    #C0657
    ChrTalk(
        0xFE,
        (
            "小桃她\x01",
            "一直都很怕生啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_9902")

    label("loc_98B6")


    #C0658
    ChrTalk(
        0xFE,
        (
            "我小的时候\x01",
            "也很不擅长与人交往……\x02",
        )
    )

    CloseMessageWindow()

    #C0659
    ChrTalk(
        0xFE,
        (
            "所以就会忍不住\x01",
            "和小桃打招呼呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9902")

    TalkEnd(0xFE)
    Return()

    # Function_21_96A9 end

    def Function_22_9906(): pass

    label("Function_22_9906")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_998A")

    #C0660
    ChrTalk(
        0xFE,
        "#1200F呜噜噜噜噜…………\x02",
    )

    CloseMessageWindow()

    #C0661
    ChrTalk(
        0x101,
        (
            "#0000F蔡特，今天\x01",
            "竟然在这种地方啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0662
    ChrTalk(
        0x104,
        "#0300F这家伙完全变成大明星了啊。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_99A8")

    label("loc_998A")


    #C0663
    ChrTalk(
        0xFE,
        "#1200F呜噜噜噜噜…………\x02",
    )

    CloseMessageWindow()

    label("loc_99A8")

    TalkEnd(0xFE)
    Return()

    # Function_22_9906 end

    def Function_23_99AC(): pass

    label("Function_23_99AC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6D, 4)), scpexpr(EXPR_END)), "loc_9A99")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_99FF")

    #C0664
    ChrTalk(
        0x15,
        (
            "#3600F各位，请加油啊，\x01",
            "我也会在心里默默支持你们的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9A94")

    label("loc_99FF")


    #C0665
    ChrTalk(
        0x15,
        (
            "#3600F各位，请加油啊，\x01",
            "我也会在心里默默支持你们的。\x02",
        )
    )

    CloseMessageWindow()

    #C0666
    ChrTalk(
        0x102,
        (
            "#0100F（有人支持的话，\x01",
            "  就会干劲十足呢……）\x02",
        )
    )

    CloseMessageWindow()

    #C0667
    ChrTalk(
        0x101,
        "#0000F（嗯嗯，我也深有感触啊。）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)

    label("loc_9A94")

    Jump("loc_9C0C")

    label("loc_9A99")

    OP_63(0x15, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0668
    ChrTalk(
        0x15,
        "#3600F哦，大家好……！\x02",
    )

    CloseMessageWindow()

    #C0669
    ChrTalk(
        0x101,
        (
            "#0000F啊，是哈罗德先生……\x02\x03",

            "莫非在谈生意吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0670
    ChrTalk(
        0x15,
        (
            "#3600F嗯，是的。\x01",
            "塔利兹先生一直\x01",
            "都很关照我的生意。\x02\x03",

            "他经常从我这里\x01",
            "进一些商品呢。\x02\x03",

            "各位是……\x01",
            "还在调查那个魔兽事件吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0671
    ChrTalk(
        0x103,
        (
            "#0200F嗯，昨天\x01",
            "还没有把事情解决。\x02",
        )
    )

    CloseMessageWindow()

    #C0672
    ChrTalk(
        0x104,
        (
            "#0300F现在正要\x01",
            "赶去玛因兹呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0673
    ChrTalk(
        0x15,
        (
            "#3600F真是辛苦啊……\x02\x03",

            "各位，请加油啊，\x01",
            "我会在心里默默支持你们的。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x6D, 4)

    label("loc_9C0C")

    TalkEnd(0xFE)
    Return()

    # Function_23_99AC end

    def Function_24_9C10(): pass

    label("Function_24_9C10")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_9D75")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9CBC")

    #C0674
    ChrTalk(
        0xFE,
        "哎呀，午安。\x02",
    )

    CloseMessageWindow()

    #C0675
    ChrTalk(
        0x101,
        (
            "#0000F艾欧莉娅小姐，\x01",
            "竟然会在这种地方相遇，\x01",
            "真是少见啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0676
    ChrTalk(
        0xFE,
        (
            "这家店的面包\x01",
            "最近很受欢迎。\x02",
        )
    )

    CloseMessageWindow()

    #C0677
    ChrTalk(
        0xFE,
        (
            "我一直在这里\x01",
            "买午饭呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_9D75")

    label("loc_9CBC")


    #C0678
    ChrTalk(
        0xFE,
        (
            "说起来，\x01",
            "刚刚有个人来协会了，\x01",
            "好像是林的前辈呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0679
    ChrTalk(
        0xFE,
        (
            "她们两个现在到\x01",
            "『龙老饭店』吃午饭去了……\x01",
            "不知道聊得愉不愉快呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0680
    ChrTalk(
        0xFE,
        (
            "呵呵，看来好像是久别重逢，\x01",
            "所以还是不要打扰她们比较好。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9D75")

    TalkEnd(0xFE)
    Return()

    # Function_24_9C10 end

    def Function_25_9D79(): pass

    label("Function_25_9D79")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9E1D")
    OP_29(0x46, 0x1, 0xB)

    #C0681
    ChrTalk(
        0x101,
        (
            "#0001F（这样一来，\x01",
            "  西街也已经调查过了……）\x02\x03",

            "#0003F（……不知道\x01",
            "  大家调查得怎么样了。）\x02",
        )
    )

    CloseMessageWindow()

    #C0682
    ChrTalk(
        0x160,
        "#3308F（…………………………）\x02",
    )

    CloseMessageWindow()
    OP_D0(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0xB9, 7)

    label("loc_9E1D")

    Return()

    # Function_25_9D79 end

    def Function_26_9E1E(): pass

    label("Function_26_9E1E")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_4B(0x8, 0xFF)
    OP_68(52500, 1500, 0, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(27000, 0)
    BeginChrThread(0x101, 3, 0, 27)
    SetChrSubChip(0x8, 0x0)
    SetCameraDistance(26000, 1500)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x10)
    WaitChrThread(0x101, 3)
    Sleep(300)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0x101, 0x8, 500)
    Sleep(500)

    #C0683
    ChrTalk(
        0x101,
        "#0000F#1P哟，奥斯卡！\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x101, 3, 0, 28)
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0684
    ChrTalk(
        0x8,
        "哎呀，这不是罗伊德嘛！\x02",
    )

    CloseMessageWindow()

    #C0685
    ChrTalk(
        0x8,
        (
            "哈哈哈！\x01",
            "你这家伙终于来见我了啊！\x02",
        )
    )

    CloseMessageWindow()

    #C0686
    ChrTalk(
        0x8,
        (
            "好久不见了啊。\x01",
            "那个，有一年了吧？\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x101, 3)
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0687
    ChrTalk(
        0x101,
        (
            "#0006F……我说啊。\x01",
            "我们都已经有三年没见面了吧？\x02\x03",

            "你这方面还真是一点都没变，\x01",
            "总是这么粗枝大叶……\x02",
        )
    )

    CloseMessageWindow()

    #C0688
    ChrTalk(
        0x8,
        (
            "哇哈哈！\x01",
            "我们一直都在通信啊，\x01",
            "所以感觉没有分别那么久。\x02",
        )
    )

    CloseMessageWindow()

    #C0689
    ChrTalk(
        0x8,
        (
            "你好像长高了很多啊，\x01",
            "不过还是一副娃娃脸。\x02",
        )
    )

    CloseMessageWindow()

    #C0690
    ChrTalk(
        0x101,
        "#0011F唔……\x02",
    )

    CloseMessageWindow()

    #C0691
    ChrTalk(
        0x104,
        "#0300F哈哈。\x02",
    )

    CloseMessageWindow()

    #C0692
    ChrTalk(
        0x102,
        "#0100F嘻嘻……\x02",
    )

    CloseMessageWindow()

    #C0693
    ChrTalk(
        0x103,
        (
            "#0200F看起来，好像是\x01",
            "罗伊德前辈的朋友吧……？\x02",
        )
    )

    CloseMessageWindow()

    #C0694
    ChrTalk(
        0x8,
        (
            "嗯，我叫奥斯卡。\x01",
            "是这家面包店『摩尔吉』\x01",
            "的见习面包师。\x02",
        )
    )

    CloseMessageWindow()

    #C0695
    ChrTalk(
        0x8,
        (
            "你们是……\x01",
            "罗伊德的同事吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0696
    ChrTalk(
        0x104,
        "#0300F嗯，我是兰迪。\x02",
    )

    CloseMessageWindow()

    #C0697
    ChrTalk(
        0x102,
        "#0100F我叫艾莉，请多指教。\x02",
    )

    CloseMessageWindow()

    #C0698
    ChrTalk(
        0x103,
        "#0200F……我叫缇欧·普拉托。\x02",
    )

    CloseMessageWindow()

    #C0699
    ChrTalk(
        0x8,
        "哦哦，请多指教啊！\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0700
    ChrTalk(
        0x101,
        (
            "#0003F（我们也没有穿制服啊，\x01",
            "  竟然能看出我们是同事……）\x02\x03",

            "（他还是老样子，真不知\x01",
            "  该算是直觉敏锐还是粗枝大叶……）\x02",
        )
    )

    CloseMessageWindow()

    #C0701
    ChrTalk(
        0x8,
        "怎么了，你的表情很奇怪哦。\x02",
    )

    CloseMessageWindow()

    #C0702
    ChrTalk(
        0x8,
        (
            "对了，罗伊德。\x01",
            "你还在做料理吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0703
    ChrTalk(
        0x101,
        (
            "#0005F哎，嗯……\x02\x03",

            "#0000F算是在做吧，我在叔叔家里\x01",
            "也会帮忙做家务，总会做一点。\x02",
        )
    )

    CloseMessageWindow()

    #C0704
    ChrTalk(
        0x8,
        (
            "那么，作为再会的纪念，\x01",
            "这东西就送给你吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0705
    ChrTalk(
        0x8,
        "希望能对你有帮助。\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0706
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x2),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x2, 1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B0(0xD)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A4A7")

    #C0707
    ChrTalk(
        0x8,
        (
            "还有，既然机会难得……\x01",
            "我来教你三明治的做法吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0708
    ChrTalk(
        0x8,
        "这很简单，最适合用来练习了。\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0709
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1B5),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "的做法被教授了。\x02",
        )
    )

    CloseMessageWindow()

    #A0710
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1B5),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "的做法已经学会了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    OP_B0(0xD)

    #C0711
    ChrTalk(
        0x101,
        (
            "#0005F谢、谢啦。\x02\x03",

            "#0000F……呵，这东西倒挺有趣啊。\x01",
            "竟然还能记录\x01",
            "食谱的各种变化。\x02",
        )
    )

    CloseMessageWindow()

    #C0712
    ChrTalk(
        0x8,
        (
            "嗯，因为可以大家共用，\x01",
            "所以使用方法可是各种各样的，\x02",
        )
    )

    CloseMessageWindow()

    #C0713
    ChrTalk(
        0x8,
        "你们也多尝试一下吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_A55E")

    label("loc_A4A7")

    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()

    #C0714
    ChrTalk(
        0x101,
        (
            "#0005F谢、谢啦。\x02\x03",

            "#0000F……呵，这东西倒挺有趣啊。\x01",
            "竟然还能记录\x01",
            "食谱的各种变化。\x02",
        )
    )

    CloseMessageWindow()

    #C0715
    ChrTalk(
        0x8,
        (
            "嗯，因为可以大家共用，\x01",
            "所以使用方法可是各种各样的，\x01",
            "你们也多尝试一下吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A55E")


    #C0716
    ChrTalk(
        0x102,
        (
            "#0105F说、说得也是呢……\x02\x03",

            "#0104F不过，至今为止，\x01",
            "我也只制作过点心之类的东西……\x02\x03",

            "#0100F兰迪和缇欧呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0717
    ChrTalk(
        0x104,
        (
            "#0303F唔……\x01",
            "我只擅长做那些只要\x01",
            "煮煮烧烧就能搞定的野外料理。\x02",
        )
    )

    CloseMessageWindow()

    #C0718
    ChrTalk(
        0x103,
        (
            "#0200F如果是那种可以按照流程制作的料理，\x01",
            "我大概没问题……\x02",
        )
    )

    CloseMessageWindow()

    #C0719
    ChrTalk(
        0x101,
        (
            "#0000F哈哈，要是有兴趣的话，\x01",
            "我也可以教你们哦。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    Sound(828, 0, 100, 0)
    SetChrName("")

    #A0720
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※和不同的人交谈，或调查一些特定的场所，\x01",
            "  就有机会得到各种『食谱』。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #A0721
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※『食谱』会被记录在『料理手册』中。\x01",
            "  只要使用『料理手册』，随时都可以\x01",
            "  制作各种效果不同的料理。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #A0722
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※此外，做出的料理还有一定的概率会成为\x01",
            "  『大成功』料理或『预想外』料理。\x01",
            "  （同时，料理也有『制作失败』的可能。）\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #A0723
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※制作料理所需要的『食材』，\x01",
            "  可以在杂货店之类的商店中购得。\x01",
            "  此外，一些魔兽有时也会掉落。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrPos(0x0, 53750, 0, 2000, 90)
    OP_4C(0x8, 0xFF)
    ClearMapFlags(0x10000000)
    SetScenarioFlags(0x46, 1)
    EventEnd(0x5)
    Return()

    # Function_26_9E1E end

    def Function_27_A858(): pass

    label("Function_27_A858")

    SetChrPos(0x101, 47500, 0, 0, 90)
    SetChrPos(0x102, 46350, 0, -500, 90)
    SetChrPos(0x103, 46450, 0, 750, 90)
    SetChrPos(0x104, 45250, 0, 250, 90)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_A8CD():
        OP_98(0x101, 0x1388, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A8CD)
    Sleep(50)

    def lambda_A8EA():
        OP_98(0x103, 0x1388, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_A8EA)
    Sleep(50)

    def lambda_A907():
        OP_98(0x102, 0x1388, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A907)
    Sleep(50)

    def lambda_A924():
        OP_98(0x104, 0x1388, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_A924)
    Sleep(500)

    def lambda_A941():
        OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_A941)
    Sleep(50)

    def lambda_A955():
        OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_A955)
    Sleep(50)

    def lambda_A969():
        OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_A969)
    Sleep(50)

    def lambda_A97D():
        OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_A97D)
    WaitChrThread(0x101, 1)
    Return()

    # Function_27_A858 end

    def Function_28_A98E(): pass

    label("Function_28_A98E")

    OP_68(54000, 1500, 2000, 3000)
    TurnDirection(0x8, 0x101, 500)

    def lambda_A9AB():
        OP_95(0x101, 53750, 0, 2000, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A9AB)
    Sleep(210)

    def lambda_A9C8():
        OP_95(0x103, 52800, 0, 2750, 1400, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_A9C8)
    Sleep(280)

    def lambda_A9E5():
        OP_95(0x102, 52700, 0, 1500, 1600, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A9E5)
    Sleep(140)

    def lambda_AA02():
        OP_95(0x104, 51500, 0, 2250, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_AA02)
    Sleep(300)
    TurnDirection(0x8, 0x101, 500)
    WaitChrThread(0x101, 1)

    def lambda_AA2A():
        OP_93(0x101, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_AA2A)
    WaitChrThread(0x103, 1)

    def lambda_AA3B():
        OP_93(0x103, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_AA3B)
    WaitChrThread(0x102, 1)

    def lambda_AA4C():
        OP_93(0x102, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_AA4C)
    WaitChrThread(0x104, 1)

    def lambda_AA5D():
        OP_93(0x104, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_AA5D)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x104, 1)
    OP_6F(0x1)
    Return()

    # Function_28_A98E end

    def Function_29_AA78(): pass

    label("Function_29_AA78")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(53470, 1500, 1600, 0)
    MoveCamera(36, 20, 0, 0)
    OP_6E(420, 0)
    SetCameraDistance(20740, 0)
    SetChrPos(0x101, 53650, 0, 1940, 90)
    SetChrPos(0x102, 52230, 0, 1940, 90)
    SetChrPos(0x103, 53650, 0, 520, 90)
    SetChrPos(0x104, 52230, 0, 520, 90)
    OP_93(0x8, 0x10E, 0x0)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()

    #C0724
    ChrTalk(
        0x8,
        (
            "#11P哟，罗伊德，\x01",
            "今天也来了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0725
    ChrTalk(
        0x8,
        "#11P哇哈哈，要不要吃点面包啊？\x02",
    )

    CloseMessageWindow()

    #C0726
    ChrTalk(
        0x101,
        (
            "#5P#0006F这种时候，该说的并不是什么\x01",
            "『要不要吃点面包』吧……？\x02\x03",

            "#0000F奥斯卡，你不是向支援科\x01",
            "提出委托了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0727
    ChrTalk(
        0x8,
        "#11P哎，有这种事吗？\x02",
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
    Sleep(1200)

    #C0728
    ChrTalk(
        0x103,
        (
            "#6P#0200F支援科这里的确\x01",
            "是收到了委托……\x02",
        )
    )

    CloseMessageWindow()

    #C0729
    ChrTalk(
        0x101,
        (
            "#5P#0003F拜托，奥斯卡……\x01",
            "我们是为工作而来的。\x02",
        )
    )

    CloseMessageWindow()

    #C0730
    ChrTalk(
        0x8,
        "#11P哦，对了，我想起来啦。\x02",
    )

    CloseMessageWindow()

    #C0731
    ChrTalk(
        0x8,
        (
            "#11P我就是想让你们帮我\x01",
            "收集用于制作新品面包的食材。\x02",
        )
    )

    CloseMessageWindow()

    #C0732
    ChrTalk(
        0x8,
        (
            "#11P其实，我拜托的商家\x01",
            "好像因故而延迟送货了。\x01",
            "所以材料似乎有些不足。\x02",
        )
    )

    CloseMessageWindow()

    #C0733
    ChrTalk(
        0x104,
        (
            "#6P#0300F原来如此，所以你才\x01",
            "希望我们帮忙收集食材啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0734
    ChrTalk(
        0x102,
        (
            "#6P#0100F的确，没有食材的话，\x01",
            "就做不成面包了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0735
    ChrTalk(
        0x8,
        (
            "#11P就是这样，\x01",
            "你们愿意接受吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0736
    ChrTalk(
        0x101,
        (
            "#5P#0000F嗯，只是收集食材的话，\x01",
            "就交给我们吧。\x02\x03",

            "那么……具体需要\x01",
            "什么食材呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0737
    ChrTalk(
        0x8,
        (
            "#11P这个嘛，小麦粉和黄油\x01",
            "倒是没问题……\x02",
        )
    )

    CloseMessageWindow()

    #C0738
    ChrTalk(
        0x8,
        (
            "#11P我希望你们收集的是\x01",
            "四个『魔兽鱼肉』\x01",
            "和三个『魔兽之卵』。\x02",
        )
    )

    CloseMessageWindow()

    #C0739
    ChrTalk(
        0x104,
        (
            "#6P#0304F嗯，这两种东西的话，\x01",
            "只要出了城，都能轻松弄到呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0740
    ChrTalk(
        0x101,
        (
            "#5P#0000F明白了，我们处理其它任务时\x01",
            "顺便收集一下吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    Sound(80, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0741
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "任务【收集食材的委托】\x07\x00",
            "开始！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_4C(0x8, 0xFF)
    SetChrPos(0x0, 53210, 0, 1200, 90)
    SetChrPos(0x1, 53210, 0, 1200, 90)
    SetChrPos(0x2, 53210, 0, 1200, 90)
    SetChrPos(0x3, 53210, 0, 1200, 90)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    OP_29(0x6, 0x1, 0x0)
    EventEnd(0x5)
    Return()

    # Function_29_AA78 end

    def Function_30_AFCF(): pass

    label("Function_30_AFCF")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(53470, 1500, 1600, 0)
    MoveCamera(36, 20, 0, 0)
    OP_6E(420, 0)
    SetCameraDistance(20740, 0)
    SetChrPos(0x101, 53650, 0, 1940, 90)
    SetChrPos(0x102, 52230, 0, 1940, 90)
    SetChrPos(0x103, 53650, 0, 520, 90)
    SetChrPos(0x104, 52230, 0, 520, 90)
    OP_93(0x8, 0x10E, 0x0)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()

    #C0742
    ChrTalk(
        0x101,
        (
            "#5P#0000F嗯，按照你的委托，\x01",
            "都拿来了。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0743
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x12D),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "×４\x01",
            scpstr(SCPSTR_CODE_ITEM, 0x12F),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "×３交给了对方。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    SubItemNumber(0x12D, 4)
    SubItemNumber(0x12F, 3)

    #C0744
    ChrTalk(
        0x8,
        (
            "#11P谢啦，这下得救了。\x01",
            "罗伊德果然\x01",
            "很可靠啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0745
    ChrTalk(
        0x8,
        (
            "#11P呵呵，从以前开始就是这样，\x01",
            "每当有困难的时候，你总是来帮我！\x02",
        )
    )

    CloseMessageWindow()

    #C0746
    ChrTalk(
        0x104,
        (
            "#6P#0309F哈哈，罗伊德果然\x01",
            "从以前就是这样啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0747
    ChrTalk(
        0x103,
        (
            "#6P#0200F从罗伊德前辈平时有求必应的\x01",
            "老好人样子来看，隐约就能察觉到了。\x02",
        )
    )

    CloseMessageWindow()

    #C0748
    ChrTalk(
        0x102,
        (
            "#5P#0109F呵呵……这不正是\x01",
            "罗伊德的优点嘛。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1200)
    OP_93(0x101, 0xE1, 0x1F4)
    Sleep(300)

    #C0749
    ChrTalk(
        0x101,
        (
            "#11P#0003F那个，你们不会\x01",
            "是在说我的坏话吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0750
    ChrTalk(
        0x8,
        (
            "#11P他们只是在说\x01",
            "罗伊德是个好人而已吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0751
    ChrTalk(
        0x8,
        (
            "#11P啊啊，对了，要不要\x01",
            "顺便尝尝\x01",
            "我烤的面包呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0752
    ChrTalk(
        0x8,
        "#11P今天免费赠送给你们哦。\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0x5A, 0x1F4)
    Sleep(300)

    #C0753
    ChrTalk(
        0x101,
        (
            "#5P#0000F好啊，\x01",
            "那我们稍后就挑几个吧。\x02\x03",

            "那么，奥斯卡。\x01",
            "要努力学习做面包啊！\x02",
        )
    )

    CloseMessageWindow()

    #C0754
    ChrTalk(
        0x8,
        "#11P噢，放心吧！\x02",
    )

    CloseMessageWindow()
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0755
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "任务【收集食材的委托】\x07\x00",
            "完成！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_4C(0x8, 0xFF)
    SetChrPos(0x0, 53210, 0, 1200, 90)
    SetChrPos(0x1, 53210, 0, 1200, 90)
    SetChrPos(0x2, 53210, 0, 1200, 90)
    SetChrPos(0x3, 53210, 0, 1200, 90)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    OP_29(0x6, 0x4, 0x10)
    OP_29(0x6, 0x1, 0x1)
    SetScenarioFlags(0x1, 5)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_30_AFCF end

    def Function_31_B417(): pass

    label("Function_31_B417")

    EventBegin(0x0)
    Fade(800)
    OP_68(55260, 2500, 12530, 0)
    MoveCamera(40, 25, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(29710, 0)
    SetChrPos(0x101, 55190, 1000, 12700, 0)
    SetChrPos(0x102, 55190, 1000, 11280, 0)
    SetChrPos(0x103, 55940, 1000, 12200, 0)
    SetChrPos(0x104, 55940, 1000, 10780, 0)
    OP_93(0xA, 0xB4, 0x0)
    OP_0D()

    #C0756
    ChrTalk(
        0xA,
        (
            "#5P……你们几个，\x01",
            "奥斯卡好像拜托你们\x01",
            "帮他收集食材吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0757
    ChrTalk(
        0xA,
        "#5P好狡猾……\x02",
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    #C0758
    ChrTalk(
        0x101,
        "#0005F#11P哎……？\x02",
    )

    CloseMessageWindow()

    #C0759
    ChrTalk(
        0xA,
        (
            "#5P我也在\x01",
            "研究新品面包呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0760
    ChrTalk(
        0xA,
        (
            "#5P为什么只接受奥斯卡的委托……\x01",
            "（自言自语）……\x02",
        )
    )

    CloseMessageWindow()

    #C0761
    ChrTalk(
        0x103,
        (
            "#11P#0200F（这个人\x01",
            "  到底怎么了？）\x02",
        )
    )

    CloseMessageWindow()

    #C0762
    ChrTalk(
        0x104,
        (
            "#0300F#11P（好像对那位老兄\x01",
            "  抱有竞争意识啊。）\x02\x03",

            "（看到我们接受了他的委托，\x01",
            "  感觉很不开心吧？）\x02",
        )
    )

    CloseMessageWindow()

    #C0763
    ChrTalk(
        0x101,
        (
            "#0006F#11P（这么麻烦啊……）\x02\x03",

            "#0005F（……哎，对了。）\x02\x03",

            "#0000F那个，我听说食材\x01",
            "的运送因故延迟了……\x01",
            "难道你也在为此烦恼吗？\x02\x03",

            "不介意的话，\x01",
            "我们也帮你收集吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_63(0xA, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    #C0764
    ChrTalk(
        0xA,
        "#5P…………那、那么………\x02",
    )

    CloseMessageWindow()

    #C0765
    ChrTalk(
        0xA,
        "#5P请帮我收集两个『魔兽之卵』吧。\x02",
    )

    CloseMessageWindow()

    #C0766
    ChrTalk(
        0xA,
        (
            "#5P……请快一点哦。\x01",
            "我想比奥斯卡\x01",
            "更早地研制出新品面包。\x02",
        )
    )

    CloseMessageWindow()

    #C0767
    ChrTalk(
        0x101,
        (
            "#0000F#11P嗯，明白了。\x01",
            "给我们一点时间吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)

    #C0768
    ChrTalk(
        0x104,
        (
            "#0305F（罗伊德那家伙，\x01",
            "  竟然交涉得如此巧妙啊？）\x02",
        )
    )

    CloseMessageWindow()

    #C0769
    ChrTalk(
        0x102,
        "#0111F#12P（而且应对得非常自然呢……）\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 500)
    Sleep(300)

    #C0770
    ChrTalk(
        0x101,
        "#0005F#5P怎么了？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 500)
    Sleep(300)

    #C0771
    ChrTalk(
        0x103,
        "#11P#0211F不，没什么……\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Fade(800)
    OP_93(0xA, 0x10E, 0x0)
    SetChrPos(0x0, 55190, 1000, 12700, 0)
    OP_4C(0xA, 0xFF)
    OP_29(0x6, 0x1, 0x2)
    EventEnd(0x5)
    Return()

    # Function_31_B417 end

    def Function_32_B8CA(): pass

    label("Function_32_B8CA")

    EventBegin(0x0)
    Fade(800)
    OP_68(55260, 2500, 12530, 0)
    MoveCamera(40, 25, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(29710, 0)
    SetChrPos(0x101, 55190, 1000, 12700, 0)
    SetChrPos(0x102, 55190, 1000, 11280, 0)
    SetChrPos(0x103, 55940, 1000, 12200, 0)
    SetChrPos(0x104, 55940, 1000, 10780, 0)
    OP_93(0xA, 0xB4, 0x0)
    OP_0D()

    #C0772
    ChrTalk(
        0x101,
        (
            "#11P#0000F嗯，按照你的委托，\x01",
            "都拿来了。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0773
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x12F),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "×２交给了对方。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    SubItemNumber(0x12F, 2)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BA25")

    #C0774
    ChrTalk(
        0xA,
        "#5P帮大忙啦，谢谢你们。\x02",
    )

    CloseMessageWindow()

    #C0775
    ChrTalk(
        0xA,
        (
            "#5P哼哼……这样一来，\x01",
            "就能打败奥斯卡了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BAD5")

    label("loc_BA25")


    #C0776
    ChrTalk(
        0xA,
        "#5P帮大忙啦，谢谢你们。\x02",
    )

    CloseMessageWindow()

    #C0777
    ChrTalk(
        0xA,
        (
            "#5P但是……还是稍微有点慢啊。\x01",
            "我明明说过请快一点的。\x01",
            "（自言自语）……\x02",
        )
    )

    CloseMessageWindow()

    #C0778
    ChrTalk(
        0xA,
        (
            "#5P按照我的预定计划，\x01",
            "本想比奥斯卡快一步，\x01",
            "让他哑口无言的……！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x71, 2)

    label("loc_BAD5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6, 0x0, 0x20)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BAE7")
    OP_2C(0x6, 0x3)

    label("loc_BAE7")

    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1200)

    #C0779
    ChrTalk(
        0x101,
        (
            "#11P#0003F（唔，明明是看她很困扰，\x01",
            "  所以才顺便接受委托的……）\x02\x03",

            "（这种结果真的好吗？）\x02",
        )
    )

    CloseMessageWindow()

    #C0780
    ChrTalk(
        0x104,
        (
            "#11P#0304F（算啦，不是挺好的吗。）\x02\x03",

            "#0300F（互相竞争才能\x01",
            "  提高技术，\x01",
            "  这也是件好事啊。）\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Fade(800)
    OP_93(0xA, 0x10E, 0x0)
    SetChrPos(0x0, 55190, 1000, 12700, 0)
    SetChrPos(0x1, 55190, 1000, 12700, 0)
    SetChrPos(0x2, 55190, 1000, 12700, 0)
    SetChrPos(0x3, 55190, 1000, 12700, 0)
    OP_4C(0xA, 0xFF)
    OP_29(0x6, 0x1, 0x3)
    SetScenarioFlags(0x1, 6)
    EventEnd(0x5)
    Return()

    # Function_32_B8CA end

    def Function_33_BC68(): pass

    label("Function_33_BC68")

    EventBegin(0x0)
    Fade(500)
    OP_68(-1260, 1800, 5200, 0)
    MoveCamera(40, 21, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(27520, 0)
    SetChrPos(0x101, -600, 0, 5400, 0)
    SetChrPos(0x102, 600, 0, 5400, 0)
    SetChrPos(0x103, -600, 0, 4200, 0)
    SetChrPos(0x104, 600, 0, 4200, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_BD0C")
    SetChrPos(0x10A, 0, 0, 3000, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    label("loc_BD0C")

    OP_4B(0xF, 0xFF)
    OP_93(0xF, 0xB4, 0x0)
    OP_0D()

    #C0781
    ChrTalk(
        0xF,
        (
            "#5P哟，欢迎光临。\x01",
            "欢迎来到『塔利兹商店』。\x02",
        )
    )

    CloseMessageWindow()

    #C0782
    ChrTalk(
        0xF,
        "#5P有什么需要的吗？\x02",
    )

    CloseMessageWindow()

    #C0783
    ChrTalk(
        0x101,
        (
            "#0000F#12P那个……\x01",
            "我们在找一种\x01",
            "名叫『利奎姆』的花。\x02",
        )
    )

    CloseMessageWindow()

    #C0784
    ChrTalk(
        0xF,
        (
            "#5P啊，莫非是……\x01",
            "来取昆特先生之前订购的花吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_BE39")
    OP_63(0x4, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    label("loc_BE39")

    Sleep(1000)

    #C0785
    ChrTalk(
        0x101,
        (
            "#12P#0005F是的……\x01",
            "原来他已经在您这里预订过了啊？\x02",
        )
    )

    CloseMessageWindow()

    #C0786
    ChrTalk(
        0xF,
        (
            "#5P是啊，在我们这里，\x01",
            "会买这种花的人主要就是他了。\x01",
            "再有就是一小部分很虔诚的人……\x02",
        )
    )

    CloseMessageWindow()

    #C0787
    ChrTalk(
        0xF,
        (
            "#5P稍等……\x01",
            "我记得柜台这边\x01",
            "是有货的。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xF, 0x0, 0x1F4)

    def lambda_BF01():
        OP_98(0xFE, 0x0, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_BF01)
    WaitChrThread(0xF, 1)

    def lambda_BF1F():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_BF1F)

    #C0788
    ChrTalk(
        0x104,
        (
            "#0306F呼，还以为\x01",
            "要帮他垫钱呢。\x02\x03",

            "因为他没有给钱，\x01",
            "所以有点担心。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_BF72():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_BF72)
    Sleep(50)

    def lambda_BF82():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_BF82)
    Sleep(50)

    def lambda_BF92():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_BF92)

    #C0789
    ChrTalk(
        0x101,
        (
            "#6P#0000F嗯～\x01",
            "对方是个实在的老人，\x01",
            "应该不会发生这种事。\x02",
        )
    )

    CloseMessageWindow()

    #C0790
    ChrTalk(
        0x103,
        (
            "#6P#0200F既然是这样，\x01",
            "多告诉我们一些\x01",
            "具体情况不是更好嘛。\x02",
        )
    )

    CloseMessageWindow()

    #C0791
    ChrTalk(
        0x102,
        (
            "#0100F是啊……\x01",
            "只说了花的大致\x01",
            "位置而已。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xF, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0xF)

    #C0792
    ChrTalk(
        0xF,
        "#5P唔、唔……\x02",
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C0F7")
    OP_63(0x4, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)

    label("loc_C0F7")

    Sleep(1000)

    def lambda_C0FF():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_C0FF)
    Sleep(50)

    def lambda_C10F():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_C10F)
    Sleep(50)

    def lambda_C11F():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_C11F)
    Sleep(50)

    def lambda_C12F():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_C12F)
    Sleep(50)

    #C0793
    ChrTalk(
        0x101,
        "#12P#0005F请问怎么了吗？\x02",
    )

    CloseMessageWindow()
    OP_93(0xF, 0xB4, 0x1F4)

    #C0794
    ChrTalk(
        0xF,
        (
            "#5P抱歉……那种花\x01",
            "好像没货了。\x02",
        )
    )

    CloseMessageWindow()

    #C0795
    ChrTalk(
        0x101,
        (
            "#12P#0006F这、这样啊……\x01",
            "真伤脑筋。\x02",
        )
    )

    CloseMessageWindow()

    #C0796
    ChrTalk(
        0xF,
        (
            "#5P哎，真对不起啊，\x01",
            "能不能稍微等等呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0797
    ChrTalk(
        0xF,
        (
            "#5P我现在就去拜托游击士\x01",
            "采点回来。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C26A")
    OP_63(0x10A, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    label("loc_C26A")

    Sleep(1000)

    #C0798
    ChrTalk(
        0x101,
        (
            "#12P#0005F原来平时都是\x01",
            "拜托游击士的吗……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C435")

    #C0799
    ChrTalk(
        0x10A,
        (
            "#12P#0603F……你应该明白，\x01",
            "我们可没有时间等游击士了。\x02\x03",

            "#0600F如果没办法解决的话，\x01",
            "我们就马上返回鲁巴彻\x01",
            "那边进行调查吧。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_C32E():
        TurnDirection(0xFE, 0x10A, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_C32E)
    Sleep(50)

    def lambda_C33E():
        TurnDirection(0xFE, 0x10A, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_C33E)
    Sleep(50)

    def lambda_C34E():
        TurnDirection(0xFE, 0x10A, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_C34E)
    Sleep(50)

    def lambda_C35E():
        TurnDirection(0xFE, 0x10A, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_C35E)
    Sleep(50)

    #C0800
    ChrTalk(
        0x101,
        (
            "#6P#0012F也、也对啊。\x02\x03",

            "#0003F（可是，这样的话……）\x02",
        )
    )

    CloseMessageWindow()

    def lambda_C3A7():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_C3A7)

    #C0801
    ChrTalk(
        0x102,
        (
            "#0101F……那个，罗伊德。\x01",
            "既然都已经接受委托了，我们就帮忙\x01",
            "去把那种花采回来吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x10A, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0802
    ChrTalk(
        0x10A,
        "#12P#0605F什么……\x02",
    )

    CloseMessageWindow()
    Jump("loc_C494")

    label("loc_C435")


    def lambda_C43A():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_C43A)

    #C0803
    ChrTalk(
        0x102,
        (
            "#0101F那个，罗伊德……\x01",
            "既然都已经接受委托了，我们就帮忙\x01",
            "去把那种花采回来吧？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C494")


    def lambda_C499():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_C499)
    Sleep(50)

    def lambda_C4A9():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_C4A9)
    Sleep(50)

    #C0804
    ChrTalk(
        0x104,
        (
            "#0300F哦哦，说得没错，\x01",
            "我们可不能输给游击士啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0805
    ChrTalk(
        0x103,
        "#6P#0200F深有同感。\x02",
    )

    CloseMessageWindow()

    def lambda_C507():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_C507)

    #C0806
    ChrTalk(
        0x101,
        (
            "#6P#0000F嗯，我也是这么想的。\x02\x03",

            "这样的话，要比等待游击士\x01",
            "有效率得多吧。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_C560():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_C560)
    Sleep(50)

    def lambda_C570():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_C570)
    Sleep(50)

    def lambda_C580():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_C580)
    Sleep(50)

    def lambda_C590():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_C590)
    Sleep(50)

    #C0807
    ChrTalk(
        0x101,
        (
            "#12P#0000F请问，那个利奎姆之花\x01",
            "开在什么地方呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0808
    ChrTalk(
        0xF,
        (
            "#5P啊，你们打算\x01",
            "自己去采摘吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0809
    ChrTalk(
        0xF,
        (
            "#5P利奎姆之花\x01",
            "开在玛因兹山道外缘。\x02",
        )
    )

    CloseMessageWindow()

    #C0810
    ChrTalk(
        0xF,
        (
            "#5P进入位于山道的隧道后，\x01",
            "途中折向通往遗迹的岔路，\x01",
            "在那条路上应该就有利奎姆之花。\x02",
        )
    )

    CloseMessageWindow()

    #C0811
    ChrTalk(
        0x101,
        (
            "#12P#0000F原来如此，我明白了。\x01",
            "我们去找找看吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0812
    ChrTalk(
        0xF,
        (
            "#5P抱歉啊，\x01",
            "到时帮我向昆特先生\x01",
            "道歉吧。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C724")

    #C0813
    ChrTalk(
        0x10A,
        (
            "#12P#0606F（……本想催他们快点，\x01",
            "　结果好像弄巧成拙了。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C724")

    OP_29(0x2E, 0x1, 0x3)
    OP_4C(0xF, 0xFF)
    SetChrPos(0x0, 0, 0, 5400, 0)
    SetChrPos(0xF, 200, 0, 8500, 180)
    EventEnd(0x5)
    Return()

    # Function_33_BC68 end

    SaveToFile()

Try(main)
