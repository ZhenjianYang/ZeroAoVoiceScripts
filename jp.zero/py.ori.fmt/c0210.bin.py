from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "オスカー",               # 1
        "モルジュ",               # 2
        "ベネット",               # 3
        "カテリーナ",             # 4
        "見物客",                 # 5
        "見物客",                 # 6
        "遊撃士エオリア",         # 7
        "タリーズ",               # 8
        "エルサ",                 # 9
        "モモ",                   # 10
        "ピート",                 # 11
        "ブリジッタ",             # 12
        "ツァイト",               # 13
        "ハロルド",               # 14
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
        "Function_6_101A",         # 06, 6
        "Function_7_402C",         # 07, 7
        "Function_8_4421",         # 08, 8
        "Function_9_455B",         # 09, 9
        "Function_10_5734",        # 0A, 10
        "Function_11_583B",        # 0B, 11
        "Function_12_66E8",        # 0C, 12
        "Function_13_6858",        # 0D, 13
        "Function_14_7772",        # 0E, 14
        "Function_15_7894",        # 0F, 15
        "Function_16_7A4D",        # 10, 16
        "Function_17_7A51",        # 11, 17
        "Function_18_95A2",        # 12, 18
        "Function_19_A0CB",        # 13, 19
        "Function_20_A9B1",        # 14, 20
        "Function_21_AB6F",        # 15, 21
        "Function_22_AE58",        # 16, 22
        "Function_23_AF0C",        # 17, 23
        "Function_24_B200",        # 18, 24
        "Function_25_B3A5",        # 19, 25
        "Function_26_B456",        # 1A, 26
        "Function_27_C00A",        # 1B, 27
        "Function_28_C140",        # 1C, 28
        "Function_29_C22A",        # 1D, 29
        "Function_30_C80D",        # 1E, 30
        "Function_31_CCAD",        # 1F, 31
        "Function_32_D1D8",        # 20, 32
        "Function_33_D594",        # 21, 33
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
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6, 0x1, 0x0)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x12D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x12F, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A74")

    #C0001
    ChrTalk(
        0x8,
        (
            "ロイド、食材集めの方は\x01",
            "どうなった？\x02",
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
            "【集めた食材を渡す】\x01",      # 0
            "【やめておく】\x01",            # 1
        )
    )

    MenuEnd(0x0)
    FadeToBright(300, 0)
    OP_60(0x0)
    OP_5A()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_A2A"),
        (1, "loc_A31"),
        (SWITCH_DEFAULT, "loc_A74"),
    )


    label("loc_A2A")

    Call(0, 30)
    TalkEnd(0x8)
    Return()

    label("loc_A31")


    #C0002
    ChrTalk(
        0x8,
        (
            "それじゃ、また\x01",
            "いい時に声を掛けてくれ。\x01",
            "よろしく頼むぜ！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A74")

    label("loc_A74")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1013")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6, 0x1, 0x0)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_EF1")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_AA9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EEC")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "話をする\x01",              # 0
            "買い物をする\x01",          # 1
            "依頼について聞く\x01",      # 2
            "やめる\x01",                # 3
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B18")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_B18")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B98")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_B37")
    OP_AF(0xCE)
    Jump("loc_B89")

    label("loc_B37")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_B47")
    OP_AF(0xCD)
    Jump("loc_B89")

    label("loc_B47")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_B57")
    OP_AF(0xCC)
    Jump("loc_B89")

    label("loc_B57")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_B67")
    OP_AF(0xCB)
    Jump("loc_B89")

    label("loc_B67")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_B77")
    OP_AF(0xCA)
    Jump("loc_B89")

    label("loc_B77")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_B87")
    OP_AF(0xC9)
    Jump("loc_B89")

    label("loc_B87")

    OP_AF(0xC8)

    label("loc_B89")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_EE7")

    label("loc_B98")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EB7")

    #C0003
    ChrTalk(
        0x8,
        (
            "集めてきて欲しいのは\x01",
            "『魔獣の魚肉』を４つ、\x01",
            "『魔獣の卵』を３つって所だな。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x8,
        (
            "食材が不足気味でな、\x01",
            "何かのついででいいから\x01",
            "集めてくれると嬉しいぜ。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x71, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DAA")

    #C0005
    ChrTalk(
        0x104,
        (
            "#0304F『魔獣の魚肉』は\x01",
            "魚型の魔獣が持ってる事があるな。\x02\x03",

            "『魔獣の卵』の方は\x01",
            "鳥や蛇型の魔獣が落とすはずだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x101,
        (
            "#0000Fへえ、やっぱりランディって\x01",
            "詳しいんだな。\x01",
            "さすが元警備隊員。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x104,
        (
            "#0300Fははっ、戦闘のたぐいは\x01",
            "慣れてるからな。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x102,
        (
            "#0100F魔獣が落とす食材は\x01",
            "料理にも使えるのよね。\x02\x03",

            "この機会に覚えておくと\x01",
            "探索も楽になるかもしれないわ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x71, 7)
    Jump("loc_EA8")

    label("loc_DAA")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x12D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x12F, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EA8")

    #C0009
    ChrTalk(
        0x104,
        (
            "#0300F『魔獣の魚肉』は魚型の魔獣、\x01",
            "『魔獣の卵』は鳥や蛇型の魔獣が\x01",
            "持ってることがあるな。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x101,
        (
            "#0000Fまあ街道を歩いていれば\x01",
            "手に入りそうだよな。\x02\x03",

            "#0004Fよし、どこかで適当に\x01",
            "調達してくるか。\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x8,
        "わはは、頼りにしてるぜ！\x02",
    )

    CloseMessageWindow()

    label("loc_EA8")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_EE7")

    label("loc_EB7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_ECB")
    Jump("loc_EE7")

    label("loc_ECB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EE7")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 6)

    label("loc_EE7")

    Jump("loc_AA9")

    label("loc_EEC")

    Jump("loc_100E")

    label("loc_EF1")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_EFB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_100E")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F59")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_F59")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FD9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_F78")
    OP_AF(0xCE)
    Jump("loc_FCA")

    label("loc_F78")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_F88")
    OP_AF(0xCD)
    Jump("loc_FCA")

    label("loc_F88")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_F98")
    OP_AF(0xCC)
    Jump("loc_FCA")

    label("loc_F98")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_FA8")
    OP_AF(0xCB)
    Jump("loc_FCA")

    label("loc_FA8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_FB8")
    OP_AF(0xCA)
    Jump("loc_FCA")

    label("loc_FB8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_FC8")
    OP_AF(0xC9)
    Jump("loc_FCA")

    label("loc_FC8")

    OP_AF(0xC8)

    label("loc_FCA")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1009")

    label("loc_FD9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_FED")
    Jump("loc_1009")

    label("loc_FED")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1009")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 6)

    label("loc_1009")

    Jump("loc_EFB")

    label("loc_100E")

    Jump("loc_1016")

    label("loc_1013")

    Call(0, 6)

    label("loc_1016")

    TalkEnd(0x8)
    Return()

    # Function_5_936 end

    def Function_6_101A(): pass

    label("Function_6_101A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_END)), "loc_10B8")

    #C0012
    ChrTalk(
        0x8,
        (
            "今日は助かったぜ。\x01",
            "ついでにオレの焼いたパンでも\x01",
            "食べていってくれ。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x8,
        "へへっ、サービスしとくぜ？\x02",
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x101,
        "#0000Fサンキュー、選ばせて貰うよ。\x02",
    )

    CloseMessageWindow()
    Jump("loc_402B")

    label("loc_10B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_1465")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xED, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13B5")

    #C0015
    ChrTalk(
        0x8,
        (
            "ようロイド。\x01",
            "また何かの捜査してんのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x101,
        (
            "#0000Fああ、そんな所だよ。\x02\x03",

            "#0001F……オスカー、念のため\x01",
            "聞いておくけど、この辺りで\x01",
            "何か変わった事は無かったか？\x02\x03",

            "黒服の連中を見かけた、とか……\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x8,
        "変わった事か……んー。\x02",
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x8,
        (
            "実はさっき、\x01",
            "ベネットが急に怒り出して\x01",
            "出て行っちまったんだよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x8,
        "一体どうしちまったんだ？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xED, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12E4")
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
            "#0006Fお前、ホント、\x01",
            "そういう所は鈍いよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x102,
        (
            "#0100F西通りのあたりは\x01",
            "特に事件も無さそうね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13AD")

    label("loc_12E4")

    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0022
    ChrTalk(
        0x101,
        (
            "#0000Fさ、さあ、知らないけど……\x02\x03",

            "オスカーのせいじゃないのか？\x01",
            "お前、たまに鈍いしさ……\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x8,
        "え、そうか？\x02",
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x102,
        (
            "#0100F（まあ、西通りのあたりは\x01",
            "  特に事件も無さそうね。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13AD")

    SetScenarioFlags(0xED, 2)
    Jump("loc_1460")

    label("loc_13B5")


    #C0025
    ChrTalk(
        0x8,
        (
            "今日はベネットが\x01",
            "すごく美味いパンを焼いて\x01",
            "食べさせてくれたんだよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x8,
        (
            "で、素直に感想を言ったら\x01",
            "急に怒って出て行っちまったんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x8,
        "んー、一体どうしたのかねぇ？\x02",
    )

    CloseMessageWindow()

    label("loc_1460")

    Jump("loc_402B")

    label("loc_1465")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_157B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1521")

    #C0028
    ChrTalk(
        0x8,
        (
            "昨日は港湾区の方で\x01",
            "撃ち合いがあったんだって？\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x8,
        (
            "マフィアも本気になれば\x01",
            "市民を巻き込んだ抗争くらい\x01",
            "平気でやるってことか……\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x8,
        "ったく、厄介な連中だぜ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1576")

    label("loc_1521")


    #C0031
    ChrTalk(
        0x8,
        (
            "せっかく店の売り上げも\x01",
            "順調に伸びてる所だしな。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x8,
        "面倒事は勘弁して欲しいぜ。\x02",
    )

    CloseMessageWindow()

    label("loc_1576")

    Jump("loc_402B")

    label("loc_157B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_16E1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16A1")
    OP_93(0x8, 0x5A, 0x0)

    #C0033
    ChrTalk(
        0x8,
        "っと、毛布はどこだ……？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x0, 500)

    #C0034
    ChrTalk(
        0x8,
        (
            "ベネット、新作の開発で\x01",
            "ほとんど寝てないみてぇなんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x8,
        (
            "はは、手間がかかるよな。\x01",
            "セシルさんに面倒を見られてた\x01",
            "小さい頃のロイドみたいだぜ。\x02",
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
            "#0003Fむ、昔のことを\x01",
            "いきなり持ち出すなよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_16DC")

    label("loc_16A1")


    #C0037
    ChrTalk(
        0x8,
        (
            "やれやれ、バッタリいく前に\x01",
            "部屋に連れて行かねぇとな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16DC")

    Jump("loc_402B")

    label("loc_16E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_1A27")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19AE")

    #C0038
    ChrTalk(
        0x8,
        (
            "よう、ロイドたち。\x01",
            "今日は珍しい人を連れてるな？\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x101,
        (
            "#0000Fああ、こちらは警備隊の\x01",
            "ノエル曹長って言うんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x109,
        (
            "#0500Fふふっ、初めまして。\x02\x03",

            "そう言えば……\x01",
            "この《モルジュ》ってお店、\x01",
            "フランから聞いた事があります。\x02\x03",

            "何でも雑誌に載った\x01",
            "若き天才パン職人がいるって。\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x8,
        "あー、あの取材か……\x02",
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x104,
        (
            "#0300F凄ぇな、雑誌なんかで\x01",
            "取り上げられてんのかよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x103,
        (
            "#0200Fまあ、取り上げられても\x01",
            "全然不思議ではありませんが。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x8,
        (
            "いや、まだ修行中の身だから\x01",
            "気が進まなかったんだけどよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x8,
        (
            "親方も乗り気だったし\x01",
            "売り上げアップも狙えそうだから\x01",
            "仕方なくな。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x8,
        (
            "おかげで今月の新作は\x01",
            "凄いプレッシャーだったぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x101,
        "#0000Fはは、よく言うよ。\x02",
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x102,
        (
            "#0100Fふふ、それじゃあ新作、\x01",
            "一つ試させてもらおうかしら。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xCD, 3)
    Jump("loc_1A22")

    label("loc_19AE")


    #C0049
    ChrTalk(
        0x8,
        (
            "天才なんてとんでもねぇ。\x01",
            "親方に較べりゃまだまださ。\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x8,
        (
            "技術的にはベネットからも\x01",
            "まだまだ教わる事が多いしな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A22")

    Jump("loc_402B")

    label("loc_1A27")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_1C26")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAD, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A4D")
    Call(0, 7)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    label("loc_1A4D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1BBC")

    #C0051
    ChrTalk(
        0x153,
        (
            "#1110Fここ、いいニオイがするねー！\x01",
            "おにーさんは何をしてるヒト～？\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x8,
        "おう、オレはパン屋さんだ。\x02",
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x8,
        (
            "キーアちゃんも１つどうだ？\x01",
            "うちのパンは美味いぞ～？\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x153,
        "#1109Fうん、そうする～！\x02",
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x101,
        (
            "#0006Fおいおい……\x01",
            "俺抜きで決めないでくれよ。\x02\x03",

            "#0000F（でも、パン屋の記憶は\x01",
            "  無いみたいだな。）\x02\x03",

            "（やっぱりクロスベル出身じゃ\x01",
            "  ないのかもしれない……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1C21")

    label("loc_1BBC")


    #C0056
    ChrTalk(
        0x8,
        (
            "ロイド、キーアちゃんに\x01",
            "なんか買ってやれよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x8,
        (
            "期間限定の\x01",
            "ハニーミルクパンなんて\x01",
            "お勧めだぜ？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C21")

    Jump("loc_402B")

    label("loc_1C26")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_1EDA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAD, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E5F")

    #C0058
    ChrTalk(
        0x8,
        (
            "例の坊主、\x01",
            "見つかったんだってな？\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x8,
        (
            "いや、良かったぜ。\x01",
            "記念祭の人ごみじゃ\x01",
            "やっぱ親も心配だろうしな。\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x101,
        "#0000Fああ、すごく心配してたよ。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0061
    ChrTalk(
        0x101,
        (
            "#0005Fそういえば、オスカー。\x02\x03",

            "#0000F《ミシュラム》って\x01",
            "お前、行ったことあるか？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0062
    ChrTalk(
        0x8,
        "いや、生憎ねぇなぁ。\x02",
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x8,
        (
            "テーマパークとか言われても\x01",
            "あんまり興味ねぇしよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x8,
        (
            "ウェンディの方は何回か\x01",
            "遊びに行ってるみたいだが。\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x101,
        "#0000Fそうなのか……\x02",
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x8,
        (
            "ただまあ、結構、\x01",
            "流行ってるみたいだぜ？\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x8,
        (
            "デートや家族サービスの\x01",
            "定番スポットになってるって話だ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xAD, 4)
    Jump("loc_1ED5")

    label("loc_1E5F")


    #C0068
    ChrTalk(
        0x8,
        (
            "そうそう、親方が午後から\x01",
            "非番にしてくれたんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x8,
        (
            "テーマパークには興味ねぇが\x01",
            "ぶらっと市内を回ってみるかね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1ED5")

    Jump("loc_402B")

    label("loc_1EDA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 7)), scpexpr(EXPR_END)), "loc_2068")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1FF7")

    #C0070
    ChrTalk(
        0x8,
        (
            "ようロイドたち。\x01",
            "例の坊主、見つかったのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x101,
        (
            "#0001Fいや、まだ探してる所だけど\x01",
            "手がかりは見つかったんだ。\x01",
            "心配しないでくれ。\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0x8,
        "そっか、そりゃ良かったな。\x02",
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0x8,
        (
            "不安がってるかもしれねぇし、\x01",
            "早いとこ迎えに行ってやんな！\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x160,
        "#3300F……ええ、そうね。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2063")

    label("loc_1FF7")


    #C0075
    ChrTalk(
        0x8,
        (
            "手がかりが見つかったんなら\x01",
            "良かったぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x8,
        (
            "不安がってるかもしれねぇし、\x01",
            "早いとこ迎えに行ってやんな！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2063")

    Jump("loc_402B")

    label("loc_2068")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_231B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAC, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22B4")

    #C0077
    ChrTalk(
        0x8,
        "お、ロイドじゃないか。\x02",
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0x8,
        (
            "可愛らしいお嬢ちゃん連れて\x01",
            "どうしたんだ？\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0x101,
        (
            "#0003Fああ、ちょっと\x01",
            "人を探していて……\x02\x03",

            "#0001Fオスカー、この写真の子を\x01",
            "見かけたりしてないか？\x02",
        )
    )

    CloseMessageWindow()

    #A0080
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

    #C0081
    ChrTalk(
        0x8,
        (
            "あれ、この子って\x01",
            "確かコリンじゃねえか？\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x101,
        "#0005Fえ、知ってるのか？\x02",
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x8,
        "ああ、住宅街の子だろ？\x02",
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x8,
        (
            "たまに家族連れでパンを\x01",
            "買いに来ることがあんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0x8,
        (
            "ただ……\x01",
            "今日は見かけてねぇなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x8,
        (
            "パレードの時にも\x01",
            "西通りじゃ見かけなかったぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x101,
        (
            "#0000Fやっぱりそうか……\x01",
            "サンキュー、助かったよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xAC, 7)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 25)
    Jump("loc_2316")

    label("loc_22B4")


    #C0088
    ChrTalk(
        0x8,
        (
            "その子なら知ってるが\x01",
            "今日は見かけてねぇなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0x8,
        (
            "少なくともウチの前は\x01",
            "通ってないと思うぜ？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2316")

    Jump("loc_402B")

    label("loc_231B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_2405")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_23B3")

    #C0090
    ChrTalk(
        0x8,
        (
            "らっしゃーい……\x01",
            "ってロイド達か。\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x8,
        (
            "今日はフルで\x01",
            "パン焼き中なんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0x8,
        (
            "こんなに人が多いとは\x01",
            "思わなかったもんでな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2400")

    label("loc_23B3")


    #C0093
    ChrTalk(
        0x8,
        "今年は格別人が多いぜ。\x02",
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x8,
        (
            "親方もこんな人出は\x01",
            "初めてだって言ってたな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2400")

    Jump("loc_402B")

    label("loc_2405")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_2471")

    #C0095
    ChrTalk(
        0x8,
        (
            "ウチの前も\x01",
            "パレードが通るらしいぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0x8,
        (
            "あんまりはしゃいで\x01",
            "ケガ人が出なきゃいいんだが。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_402B")

    label("loc_2471")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_2535")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_24DB")

    #C0097
    ChrTalk(
        0x8,
        (
            "ベネットの試食、\x01",
            "うまく行ってるみてぇだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x8,
        "今日は更に売れそうだぜ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2530")

    label("loc_24DB")


    #C0099
    ChrTalk(
        0x8,
        "ベネットが試食を始めたんだ。\x02",
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0x8,
        (
            "いいアイデアだよな。\x01",
            "今日は更に売れそうだぜ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2530")

    Jump("loc_402B")

    label("loc_2535")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_2656")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_25FA")

    #C0101
    ChrTalk(
        0x8,
        "よお、ロイド達か。\x02",
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x8,
        (
            "記念祭は大変だぜ。\x01",
            "普段の３倍くらいは\x01",
            "パンが売れてくからな。\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0x8,
        (
            "マクダエル市長の一件で\x01",
            "どうなることかと思ったが\x01",
            "客入りに影響は無かったな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2651")

    label("loc_25FA")


    #C0104
    ChrTalk(
        0x8,
        (
            "オレも記念祭用仕様の\x01",
            "新作パンを作ってみたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0x8,
        "よかったら試してみてくれよ。\x02",
    )

    CloseMessageWindow()

    label("loc_2651")

    Jump("loc_402B")

    label("loc_2656")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_27D5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2777")

    #C0106
    ChrTalk(
        0x8,
        (
            "最近、警察関係者が\x01",
            "よく店に来てくれるんだよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0x8,
        (
            "私服なんだが\x01",
            "雰囲気がモロ捜査官なんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0x8,
        "やっぱり張り込み中なのかね？\x02",
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0x103,
        (
            "#0200F……オスカーさん。\x01",
            "よく判りますね。\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0x101,
        (
            "#0000F昔からそういう所は\x01",
            "鋭いんだよな……\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0x8,
        "はは、それ程でもないけどな。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_27D0")

    label("loc_2777")


    #C0112
    ChrTalk(
        0x8,
        (
            "最近、警察関係者が\x01",
            "よく店に来てくれるんだよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0x8,
        "どこかに張り込み中みたいだぜ。\x02",
    )

    CloseMessageWindow()

    label("loc_27D0")

    Jump("loc_402B")

    label("loc_27D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_2BE9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B27")

    #C0114
    ChrTalk(
        0x8,
        (
            "アルカンシェルの新作公演が\x01",
            "来月公開なんだってな。\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0x8,
        (
            "俺はあんま興味無いけど\x01",
            "お客さんがひっきりなしに\x01",
            "噂していくぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0x8,
        (
            "──そうだロイド。\x01",
            "よかったら一緒に見に行くか？\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0x8,
        "オレ、チケット持ってんだよな。\x02",
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
            "#0005Fオスカー……\x01",
            "チケット持ってるのか！？\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0x8,
        "ああ、お得意さんから貰ってな。\x02",
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0x8,
        (
            "そこのメゾンに住んでる\x01",
            "美人のお客さんなんだけどよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0x8,
        (
            "たまにサービスしてたら\x01",
            "お礼にってチケットをくれたんだ。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8F, 1)), scpexpr(EXPR_END)), "loc_2AF7")
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
        "#0300F（おいおい、まさか……）\x02",
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0x103,
        (
            "#0200F（多分イリアさんの事では\x01",
            "  ないかと……）\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0x101,
        (
            "#0006F（さすがオスカー……\x01",
            "  こういう所は抜けてるんだよな。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B1F")

    label("loc_2AF7")


    #C0125
    ChrTalk(
        0x104,
        "#0300Fな、なんつー太っ腹な客だ……\x02",
    )

    CloseMessageWindow()

    label("loc_2B1F")

    SetScenarioFlags(0x0, 0)
    Jump("loc_2BE4")

    label("loc_2B27")


    #C0126
    ChrTalk(
        0x8,
        (
            "そこのメゾンに住んでいる\x01",
            "美人のお客さんなんだけどよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0x8,
        (
            "いつも朝の６時くらいに来て\x01",
            "山ほどパンを買ってくんだよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0x8,
        (
            "たまに新作をサービスしてたら\x01",
            "お礼にってチケットをくれたんだ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2BE4")

    Jump("loc_402B")

    label("loc_2BE9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_2EA1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8E, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E13")

    #C0129
    ChrTalk(
        0x8,
        (
            "ウチの前って\x01",
            "街道から続く大通りだろ？\x02",
        )
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0x8,
        (
            "最近導力車の行き来が\x01",
            "激しいんだよな～。\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0x102,
        (
            "#0100Fそういえば最近は\x01",
            "導力トラックを使った\x01",
            "運送会社も増えているみたいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0x8,
        "そうそう、それに……\x02",
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0x8,
        (
            "パンの仕込みを始める\x01",
            "朝３時くらいに、黒い運搬車を\x01",
            "見かけることがあんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0x8,
        (
            "《ルバーチェ》の車って噂だが\x01",
            "本当なのかねぇ？\x02",
        )
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0x101,
        (
            "#0003F（西クロスベル街道……\x01",
            "  帝国との密輸ルートだったり\x01",
            "  するのかな。）\x02",
        )
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0x104,
        (
            "#0300F（限りなく黒に近い\x01",
            "  グレーって所か……）\x02\x03",

            "（鉱山町にも顔を出してやがったし\x01",
            "  最近活発に動いてるみたいだな。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x8E, 1)
    Jump("loc_2E9C")

    label("loc_2E13")


    #C0137
    ChrTalk(
        0x8,
        (
            "最近、パンの仕込みを始める\x01",
            "朝３時くらいに、黒い運搬車を\x01",
            "見かけることがあんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0x8,
        (
            "《ルバーチェ》の車って噂だが\x01",
            "本当なのかねぇ？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E9C")

    Jump("loc_402B")

    label("loc_2EA1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_3180")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8E, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_30E0")

    #C0139
    ChrTalk(
        0x8,
        "よう、ロイドたちか。\x02",
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0x8,
        (
            "最近評判みたいだな？\x01",
            "お客さんも噂してたぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0x101,
        (
            "#0000Fはは、何だか照れるな。\x02\x03",

            "ここ最近は\x01",
            "地味な支援要請ばっかり\x01",
            "だったと思うけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0x102,
        (
            "#0100F何事も地道に続けていれば\x01",
            "評価されるものなのね。\x02",
        )
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0x8,
        (
            "はは、まあそれ以上に\x01",
            "評判になってるのは\x01",
            "あの白い警察犬だけどな。\x02",
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
        "#0006Fやっぱツァイトか……\x02",
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0x8,
        (
            "朝の仕込みの時に\x01",
            "たまに見かけるんだが、\x01",
            "すげぇカッコいいんだよな～。\x02",
        )
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0x8,
        (
            "犬は大好きだし\x01",
            "今度オレにも紹介してくれよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x8E, 0)
    Jump("loc_317B")

    label("loc_30E0")


    #C0147
    ChrTalk(
        0x8,
        (
            "あの警察犬、この辺りじゃ\x01",
            "かなり話題になってるぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0x8,
        (
            "犬は大好きだし\x01",
            "今度オレにも紹介してくれよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0x8,
        (
            "今月の新作パンでも\x01",
            "ご馳走させてもらうからさ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_317B")

    Jump("loc_402B")

    label("loc_3180")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_32DD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_325C")

    #C0150
    ChrTalk(
        0x8,
        (
            "ベネットって親方の娘さんでな。\x01",
            "パン作りの腕も大したモンなんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0x8,
        (
            "オレも弟子入りした当初は\x01",
            "ベネットからイロハを教わったぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0x8,
        (
            "でも彼女、無愛想でな。\x01",
            "いつも何か怒ってる気がすんだよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_32D8")

    label("loc_325C")


    #C0153
    ChrTalk(
        0x8,
        (
            "結構可愛い顔してんだから\x01",
            "怒ってばかりじゃ勿体ねぇよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0x8,
        (
            "今度、カルシウムたっぷりの\x01",
            "ミルクパンでも焼いてやるかね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_32D8")

    Jump("loc_402B")

    label("loc_32DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_33A5")

    #C0155
    ChrTalk(
        0x8,
        (
            "うちの惣菜パンには\x01",
            "アルモリカ産の小麦と\x01",
            "野菜を使ってるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0x8,
        (
            "最近じゃ共和国産の方が安いけど\x01",
            "やっぱり鮮度が違うからな。\x02",
        )
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0x104,
        (
            "#0300Fはは、食材にも結構\x01",
            "こだわりがあるみてえだな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_402B")

    label("loc_33A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_362D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_35A1")

    #C0158
    ChrTalk(
        0x8,
        (
            "ロイドたち、今日は早いな。\x01",
            "何かいい事でもあったのかよ？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_346C")

    #C0159
    ChrTalk(
        0x101,
        (
            "#0000Fいや、別に理由はないけど。\x02\x03",

            "オスカーこそいつも早いよな……\x01",
            "って、パン屋なんだから当然か。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_34DF")

    label("loc_346C")


    #C0160
    ChrTalk(
        0x101,
        (
            "#0006Fいやだから、仕事で来たんだってば。\x02\x03",

            "#0000Fオスカーこそいつも早いよな……\x01",
            "って、パン屋なんだから当然か。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_34DF")


    #C0161
    ChrTalk(
        0x102,
        (
            "#0100Fふふ、おはよう。\x01",
            "今日もとってもいい匂いね。\x02",
        )
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0x8,
        (
            "はっはっは、当然だろ。\x01",
            "こっちの棚はさっき焼き上がった\x01",
            "今月の新作パンなんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0x8,
        (
            "良かったらどうぞ。\x01",
            "出来立てが一番美味いぜ！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_3628")

    label("loc_35A1")


    #C0164
    ChrTalk(
        0x8,
        (
            "パン屋の朝は３時だからな。\x01",
            "仕事始めはびっくりするくらい\x01",
            "すがすがしいぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0x8,
        (
            "オレ、そんな所にも憧れて\x01",
            "パン職人になったんだよな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3628")

    Jump("loc_402B")

    label("loc_362D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_3E88")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A, 7)), scpexpr(EXPR_END)), "loc_3A6C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A0E")

    #C0166
    ChrTalk(
        0x8,
        "ようロイド、さっそく来てくれたのか。\x02",
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0x8,
        (
            "お前と会うのは半年ぶり……\x01",
            "いや１年ぶりだっけか？\x01",
            "結構経つよなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0x101,
        (
            "#0003F……あのな。\x01",
            "顔を合わせるのは３年振りだろ？\x02\x03",

            "さっきは自分でもそう言ってたくせに、\x01",
            "そういう所は相変わらず\x01",
            "大ざっぱっていうか……\x02",
        )
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0x8,
        "わはは、まあ細かい事は気にすんな！\x02",
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0x8,
        (
            "それにお前、\x01",
            "かなり背は伸びたみたいだが\x01",
            "相変わらずの童顔だしよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0x101,
        "#0011Fむぐっ……\x02",
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0x104,
        "#0309Fははっ。\x02",
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0x102,
        "#0100Fクスクス……\x02",
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0x103,
        "#0204Fふふっ……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0175
    ChrTalk(
        0x101,
        (
            "#0006Fはあ、もういいけどさ。\x02\x03",

            "#0000Fそういや……オスカーの方は\x01",
            "随分腕が上がったみたいだな？\x02\x03",

            "毎月出してる新作のパンが\x01",
            "すごく評判がいいって\x01",
            "ウェンディが手紙で書いてたぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0x8,
        (
            "いやいや、まだ修行中の身さ。\x01",
            "パン職人ほど\x01",
            "奥の深い道はねえからなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0x8,
        (
            "ただまあ、今月の新作は\x01",
            "けっこう良い出来だと思うぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0x8,
        (
            "よかったら……ロイドの同僚の人らも\x01",
            "試してみてくれよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0x104,
        "#0300Fああ、選ばせて貰うぜ。\x02",
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0x102,
        (
            "#0100F美味しそうなパンばかりだし、\x01",
            "持ち帰ってどこかで\x01",
            "いただきましょうか。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x4D, 3)
    Jump("loc_3A67")

    label("loc_3A0E")


    #C0181
    ChrTalk(
        0x8,
        (
            "まだまだ修行中の身だが\x01",
            "今月の新作は自信があるぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0x8,
        "よかったら試してみてくれよ。\x02",
    )

    CloseMessageWindow()

    label("loc_3A67")

    Jump("loc_3E83")

    label("loc_3A6C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D1C")

    #C0183
    ChrTalk(
        0x8,
        (
            "そういやロイド、\x01",
            "ウェンディには会ったのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0x101,
        (
            "#0000Fああ、さっき偶然会ったよ。\x02\x03",

            "技師として立派に\x01",
            "仕事してるみたいだけど……\x02\x03",

            "#0003F昔のあいつを知ってる身としては\x01",
            "客相手に切れてスパナで殴らないか\x01",
            "……微妙に心配なんだよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0x8,
        "わはは、ちがいねぇ。\x02",
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0x8,
        (
            "ま、大丈夫だろ。\x01",
            "ウェンディはあれでも\x01",
            "加減くらいは分かってるからよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0x8,
        (
            "タンコブくらいで\x01",
            "何とか収まるんじゃねーか？\x02",
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
        "#0105F（十分大事#4Rおおごと#だと思うけど……）\x02",
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0x104,
        (
            "#0306F（はぁ、ウェンディちゃん。\x01",
            "  けっこう可愛いのに……）\x02",
        )
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0x103,
        (
            "#0200F（ランディさんも\x01",
            "  気をつけた方が良さそうですね。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x4D, 3)
    Jump("loc_3E83")

    label("loc_3D1C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E17")

    #C0191
    ChrTalk(
        0x8,
        (
            "そうそう、最近警察関係の\x01",
            "お客さんが増えてんだよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0x8,
        (
            "ウチの隣って法律事務所だろ？\x01",
            "そこに用事があって\x01",
            "ついでに立ち寄ってくれるらしい。\x02",
        )
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0x8,
        (
            "いや～、ありがてぇよな。\x01",
            "ウチのパンで厳ついオッサンを\x01",
            "笑顔に出来るなんざ、光栄だぜ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_3E83")

    label("loc_3E17")


    #C0194
    ChrTalk(
        0x8,
        (
            "最近警察関係の\x01",
            "お客さんが増えてんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0x8,
        (
            "隣の法律事務所を訪ねるついでに\x01",
            "立ち寄ってくれるみてぇだ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3E83")

    Jump("loc_402B")

    label("loc_3E88")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_402B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3FD2")

    #C0196
    ChrTalk(
        0x101,
        (
            "#0000Fオスカーの方は\x01",
            "随分腕が上がったみたいだな？\x02\x03",

            "毎月出してる新作のパンが\x01",
            "すごく評判がいいって\x01",
            "ウェンディが手紙で書いてたぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0x8,
        "いやいや、まだ修行中の身さ。\x02",
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0x8,
        (
            "パン職人ほど\x01",
            "奥の深い道はねえからなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0x8,
        (
            "ただまあ、今月の新作は\x01",
            "けっこう良い出来だと思うぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0x8,
        "よかったら試してみてくれよ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_402B")

    label("loc_3FD2")


    #C0201
    ChrTalk(
        0x8,
        (
            "まだまだ修行中の身だが\x01",
            "今月の新作は自信があるぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0202
    ChrTalk(
        0x8,
        "よかったら試してみてくれよ。\x02",
    )

    CloseMessageWindow()

    label("loc_402B")

    Return()

    # Function_6_101A end

    def Function_7_402C(): pass

    label("Function_7_402C")

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
            "よお、ロイド。\x01",
            "一週間ぶりくらいか。\x02",
        )
    )

    CloseMessageWindow()

    #C0204
    ChrTalk(
        0x8,
        (
            "いつも顔を見せてるのに\x01",
            "何かあったのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0205
    ChrTalk(
        0x101,
        "#0000Fいや、それが……\x02",
    )

    CloseMessageWindow()

    #C0206
    ChrTalk(
        0x153,
        (
            "#1110Fわー、のっぽな帽子だー！\x01",
            "面白いねー！\x02\x03",

            "#1104Fそれに……\x01",
            "くんくん、いいニオイがする！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0x8)

    #C0207
    ChrTalk(
        0x8,
        "…………えっと………\x02",
    )

    CloseMessageWindow()

    #C0208
    ChrTalk(
        0x8,
        "ロイドの妹だったっけ？\x02",
    )

    CloseMessageWindow()

    #C0209
    ChrTalk(
        0x101,
        (
            "#0006F……違うから。\x01",
            "妹なんていないから。\x02",
        )
    )

    CloseMessageWindow()

    #C0210
    ChrTalk(
        0x8,
        (
            "わはは。\x01",
            "冗談に決まってんだろ。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_4271")

    #C0211
    ChrTalk(
        0x102,
        (
            "#0100Fこの子はキーアと言って、\x01",
            "少し訳ありで預かっているの。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4310")

    label("loc_4271")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_42C4")

    #C0212
    ChrTalk(
        0x103,
        (
            "#0200Fこの子はキーアと言って、\x01",
            "少し訳あって預かっているんです。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4310")

    label("loc_42C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_4310")

    #C0213
    ChrTalk(
        0x104,
        (
            "#0300Fこいつはキーアつって、\x01",
            "ちょいとワケありで預かってんだ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4310")


    #C0214
    ChrTalk(
        0x8,
        "へぇ、そうなのか。\x02",
    )

    CloseMessageWindow()

    #C0215
    ChrTalk(
        0x8,
        (
            "よーし、お近づきの印だ。\x01",
            "よかったらご馳走するぜ。\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    #A0216
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "キーアはミルク瓶を受け取った。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0217
    ChrTalk(
        0x153,
        (
            "#1105Fわっ、いいの～？\x02\x03",

            "#1109Fごくごく……おいしー！\x02",
        )
    )

    CloseMessageWindow()

    #C0218
    ChrTalk(
        0x8,
        (
            "はっはっは！\x01",
            "ウチのはアルモリカ産だからな。\x02",
        )
    )

    CloseMessageWindow()

    #C0219
    ChrTalk(
        0x101,
        "#0000Fはは、なんか済まないな。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0xAD, 5)
    EventEnd(0x5)
    Return()

    # Function_7_402C end

    def Function_8_4421(): pass

    label("Function_8_4421")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4554")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_443C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_454F")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_449A")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_449A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_451A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_44B9")
    OP_AF(0xCE)
    Jump("loc_450B")

    label("loc_44B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_44C9")
    OP_AF(0xCD)
    Jump("loc_450B")

    label("loc_44C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_44D9")
    OP_AF(0xCC)
    Jump("loc_450B")

    label("loc_44D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_44E9")
    OP_AF(0xCB)
    Jump("loc_450B")

    label("loc_44E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_44F9")
    OP_AF(0xCA)
    Jump("loc_450B")

    label("loc_44F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_4509")
    OP_AF(0xC9)
    Jump("loc_450B")

    label("loc_4509")

    OP_AF(0xC8)

    label("loc_450B")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_454A")

    label("loc_451A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_452E")
    Jump("loc_454A")

    label("loc_452E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_454A")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 9)

    label("loc_454A")

    Jump("loc_443C")

    label("loc_454F")

    Jump("loc_4557")

    label("loc_4554")

    Call(0, 9)

    label("loc_4557")

    TalkEnd(0x9)
    Return()

    # Function_8_4421 end

    def Function_9_455B(): pass

    label("Function_9_455B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6, 0x0, 0x10)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6D, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4698")

    #C0220
    ChrTalk(
        0x9,
        (
            "おう、聞いたぜ。\x01",
            "食材を集めてきてくれたんだって？\x02",
        )
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0x9,
        (
            "嬉しいな、これでバンバン\x01",
            "焼けるってもんだぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0222
    ChrTalk(
        0x101,
        (
            "#0000Fまた何かあれば\x01",
            "支援課にご連絡下さい。\x02",
        )
    )

    CloseMessageWindow()

    #C0223
    ChrTalk(
        0x104,
        (
            "#0300Fま、このくらい\x01",
            "お安い御用ッスから。\x02",
        )
    )

    CloseMessageWindow()

    #C0224
    ChrTalk(
        0x9,
        "こりゃ頼もしいな。\x02",
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0x9,
        (
            "へへ、また手を借りるかもしれん。\x01",
            "そんときゃ宜しくなぁ！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x6D, 6)
    Jump("loc_5733")

    label("loc_4698")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4778")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4738")

    #C0226
    ChrTalk(
        0x9,
        (
            "やれやれ、食材の配達が\x01",
            "遅れちまっててな。\x02",
        )
    )

    CloseMessageWindow()

    #C0227
    ChrTalk(
        0x9,
        (
            "今日も材料をセーブしながら\x01",
            "焼いてるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0228
    ChrTalk(
        0x9,
        "こりゃ肩身が狭いぜ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_4773")

    label("loc_4738")


    #C0229
    ChrTalk(
        0x9,
        (
            "はあ、参ったな……明日には\x01",
            "届いてくれりゃいいんだが。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4773")

    Jump("loc_5733")

    label("loc_4778")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_4882")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4858")

    #C0230
    ChrTalk(
        0x9,
        (
            "ベネットの新作パンは\x01",
            "俺もオスカーも絶賛したんだが……\x01",
            "本人としては納得いかんらしい。\x02",
        )
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0x9,
        (
            "いや、味に納得はしてるんだが……\x01",
            "オスカーの反応が物足りなかったのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0232
    ChrTalk(
        0x9,
        "うーむ、どうも分からんな。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_487D")

    label("loc_4858")


    #C0233
    ChrTalk(
        0x9,
        (
            "やっぱ年頃の娘は\x01",
            "分からんねェ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_487D")

    Jump("loc_5733")

    label("loc_4882")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_4953")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_48FF")

    #C0234
    ChrTalk(
        0x9,
        (
            "ほう……ベネットのやつ\x01",
            "いい香りを出させてやがるな。\x02",
        )
    )

    CloseMessageWindow()

    #C0235
    ChrTalk(
        0x9,
        (
            "今度のパンは\x01",
            "中々期待できそうだぞ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_494E")

    label("loc_48FF")


    #C0236
    ChrTalk(
        0x9,
        (
            "ベネットも真剣に\x01",
            "パン作りしてやがったからな。\x02",
        )
    )

    CloseMessageWindow()

    #C0237
    ChrTalk(
        0x9,
        "……実にいい香りだぜ。\x02",
    )

    CloseMessageWindow()

    label("loc_494E")

    Jump("loc_5733")

    label("loc_4953")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_4A24")

    #C0238
    ChrTalk(
        0x9,
        (
            "近頃遠方から来てくれる\x01",
            "客が増えてるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0239
    ChrTalk(
        0x9,
        (
            "嬉しいモンだぜ。\x01",
            "これもオスカーが\x01",
            "頑張ってくれたお陰かね。\x02",
        )
    )

    CloseMessageWindow()

    #C0240
    ChrTalk(
        0x9,
        (
            "あいつのお陰で、とうとう\x01",
            "クロスベルタイムズにも\x01",
            "取り上げられちまったもんなぁ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5733")

    label("loc_4A24")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_4B7C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4AFC")

    #C0241
    ChrTalk(
        0x9,
        (
            "ベネットが熱心に\x01",
            "研究してるもんでな。\x01",
            "新作パンの採用方法を考え直したぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0242
    ChrTalk(
        0x9,
        (
            "ズバリ、３人で試作品を出し合って\x01",
            "一番うまいやつを多数決で決めるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0243
    ChrTalk(
        0x9,
        "……どうだ、合理的な方法だろ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_4B77")

    label("loc_4AFC")


    #C0244
    ChrTalk(
        0x9,
        (
            "いつもは俺が\x01",
            "試食して決めてるんだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0245
    ChrTalk(
        0x9,
        (
            "オスカーもベネットも\x01",
            "一人前になってきた。\x01",
            "多数決ってのも公平でいいだろ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4B77")

    Jump("loc_5733")

    label("loc_4B7C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_4C08")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4BD6")

    #C0246
    ChrTalk(
        0x9,
        (
            "最近ベネットに\x01",
            "厨房を占拠されてんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0247
    ChrTalk(
        0x9,
        "参ったなァ……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_4C03")

    label("loc_4BD6")


    #C0248
    ChrTalk(
        0x9,
        (
            "参ったな、俺も\x01",
            "パンが焼きてえんだが……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4C03")

    Jump("loc_5733")

    label("loc_4C08")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_4C9A")

    #C0249
    ChrTalk(
        0x9,
        (
            "そろそろ人の波も引いてきた。\x01",
            "俺たちも一息入れるとするか。\x02",
        )
    )

    CloseMessageWindow()

    #C0250
    ChrTalk(
        0x9,
        (
            "……パン作りは腕力を使うからな。\x01",
            "俺もそろそろ疲れてきてんだよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5733")

    label("loc_4C9A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_4D1A")

    #C0251
    ChrTalk(
        0x9,
        "ぱっぱらぱっぱ、ぱっぱっぱ～！\x02",
    )

    CloseMessageWindow()

    #C0252
    ChrTalk(
        0x9,
        (
            "パレードの曲は\x01",
            "毎年変わらねえなァ。\x02",
        )
    )

    CloseMessageWindow()

    #C0253
    ChrTalk(
        0x9,
        (
            "あれを聞くと\x01",
            "俺も童心に帰るぜ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5733")

    label("loc_4D1A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_4DA5")

    #C0254
    ChrTalk(
        0x9,
        (
            "今日は記念祭の\x01",
            "一大イベント、パレードだなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0255
    ChrTalk(
        0x9,
        (
            "こいつを乗り切れば\x01",
            "忙しさもあと少しだ。\x01",
            "もうちょい踏ん張るとするか。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5733")

    label("loc_4DA5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_4E04")

    #C0256
    ChrTalk(
        0x9,
        "えっほ、えっほ……\x02",
    )

    CloseMessageWindow()

    #C0257
    ChrTalk(
        0x9,
        (
            "今年は客入りがいいな。\x01",
            "いくら焼いても追いつかんぜ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5733")

    label("loc_4E04")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_4F0A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4EB8")

    #C0258
    ChrTalk(
        0x9,
        (
            "あのヒネクレ者のベネットが\x01",
            "店頭販売だと……？\x02",
        )
    )

    CloseMessageWindow()

    #C0259
    ChrTalk(
        0x9,
        (
            "しかも頑張って\x01",
            "営業スマイルまで作りやがって。\x02",
        )
    )

    CloseMessageWindow()

    #C0260
    ChrTalk(
        0x9,
        (
            "……変わりすぎて\x01",
            "パパ心配しちゃうぞこの野郎。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_4F05")

    label("loc_4EB8")


    #C0261
    ChrTalk(
        0x9,
        (
            "あいつ、ほんとに\x01",
            "積極的になったよなァ。\x02",
        )
    )

    CloseMessageWindow()

    #C0262
    ChrTalk(
        0x9,
        "……いや、マジで驚いたぜ。\x02",
    )

    CloseMessageWindow()

    label("loc_4F05")

    Jump("loc_5733")

    label("loc_4F0A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_4F78")

    #C0263
    ChrTalk(
        0x9,
        (
            "オスカーが来てから\x01",
            "ベネットも積極的になったんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0264
    ChrTalk(
        0x9,
        (
            "いやあ、いい弟子を\x01",
            "持ったもんだぜ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5733")

    label("loc_4F78")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_4FED")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4F93")
    Call(0, 12)
    Jump("loc_4FE8")

    label("loc_4F93")


    #C0265
    ChrTalk(
        0x9,
        (
            "オスカーの奴は腕もいい。\x01",
            "何より男前だからな。\x02",
        )
    )

    CloseMessageWindow()

    #C0266
    ChrTalk(
        0x9,
        "これで店も安泰だぜ、ふはは！\x02",
    )

    CloseMessageWindow()

    label("loc_4FE8")

    Jump("loc_5733")

    label("loc_4FED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_506A")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B0(0x17)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5009")
    Call(0, 10)
    Jump("loc_5065")

    label("loc_5009")


    #C0267
    ChrTalk(
        0x9,
        (
            "さて、俺も\x01",
            "次の新作パンを考えるか。\x02",
        )
    )

    CloseMessageWindow()

    #C0268
    ChrTalk(
        0x9,
        (
            "オスカーに任せっぱなし\x01",
            "ってのも悪いからなァ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5065")

    Jump("loc_5733")

    label("loc_506A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_518E")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B0(0x17)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5086")
    Call(0, 10)
    Jump("loc_5189")

    label("loc_5086")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_510C")

    #C0269
    ChrTalk(
        0x9,
        (
            "ベネットは何度か\x01",
            "オスカーに勝負を挑んでるんだが……\x01",
            "どうしても勝てねえらしい。\x02",
        )
    )

    CloseMessageWindow()

    #C0270
    ChrTalk(
        0x9,
        "ありゃあムキになってるな。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_5189")

    label("loc_510C")


    #C0271
    ChrTalk(
        0x9,
        (
            "オスカーのパンは\x01",
            "人気があるんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0272
    ChrTalk(
        0x9,
        (
            "材料や焼き方だけじゃあねえ、\x01",
            "あいつにはテクを組み合わせる\x01",
            "センスがあるからな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5189")

    Jump("loc_5733")

    label("loc_518E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_52BF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5251")

    #C0273
    ChrTalk(
        0x9,
        (
            "最近の新作パンは\x01",
            "オスカーに任せてるんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0274
    ChrTalk(
        0x9,
        (
            "あいつには才能がある。\x01",
            "努力も大したもんだが\x01",
            "何よりセンスが抜群なんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0275
    ChrTalk(
        0x9,
        (
            "俺はもう教える事は\x01",
            "ないと思ってるぜ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_52BA")

    label("loc_5251")


    #C0276
    ChrTalk(
        0x9,
        "オスカーはセンスが抜群なんだ。\x02",
    )

    CloseMessageWindow()

    #C0277
    ChrTalk(
        0x9,
        (
            "ま、ベネットが対抗意識燃やすのも\x01",
            "その辺りが原因なんだろうなァ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_52BA")

    Jump("loc_5733")

    label("loc_52BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_5421")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5399")

    #C0278
    ChrTalk(
        0x9,
        (
            "誰も気付いてねえだろうが、\x01",
            "俺のパン作りの基準は『香り』なんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0279
    ChrTalk(
        0x9,
        (
            "新作パンを作るときも\x01",
            "香りってのを大事にしている。\x02",
        )
    )

    CloseMessageWindow()

    #C0280
    ChrTalk(
        0x9,
        (
            "そいつはつまり、素材のよさを\x01",
            "引き出しているってことだからな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_541C")

    label("loc_5399")


    #C0281
    ChrTalk(
        0x9,
        (
            "俺が新作パンを作ってたのも\x01",
            "元はといえば\x01",
            "素材の生かし方を探求するためだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0282
    ChrTalk(
        0x9,
        (
            "ま、客受けがいいからって\x01",
            "理由もあるんだがなァ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_541C")

    Jump("loc_5733")

    label("loc_5421")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_5520")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_549D")

    #C0283
    ChrTalk(
        0x9,
        "第二弾焼き上がりィ～っと。\x02",
    )

    CloseMessageWindow()

    #C0284
    ChrTalk(
        0x9,
        (
            "うーん、香ばしいカオリ。\x01",
            "これだからパン屋はやめられんなァ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_551B")

    label("loc_549D")


    #C0285
    ChrTalk(
        0x9,
        "うちのパン焼きは５時からだ。\x02",
    )

    CloseMessageWindow()

    #C0286
    ChrTalk(
        0x9,
        (
            "それまでに生地は作っちまうからな。\x01",
            "後は焼いて焼いて\x01",
            "香りを楽しむフィーバータイムだぜ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_551B")

    Jump("loc_5733")

    label("loc_5520")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_5603")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_55E0")

    #C0287
    ChrTalk(
        0x9,
        (
            "俺の娘は負けず嫌いでな、\x01",
            "最近はオスカーに\x01",
            "対抗意識を燃やしてるらしい。\x02",
        )
    )

    CloseMessageWindow()

    #C0288
    ChrTalk(
        0x9,
        (
            "前はパン屋になる気はねえ\x01",
            "なんて言ってたくせにな。\x02",
        )
    )

    CloseMessageWindow()

    #C0289
    ChrTalk(
        0x9,
        "ハァ、何を考えてやがんだか。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_55FE")

    label("loc_55E0")


    #C0290
    ChrTalk(
        0x9,
        "年頃の娘は分からんねェ。\x02",
    )

    CloseMessageWindow()

    label("loc_55FE")

    Jump("loc_5733")

    label("loc_5603")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_5733")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_56C5")

    #C0291
    ChrTalk(
        0x9,
        "……お、らっしゃーい！\x02",
    )

    CloseMessageWindow()

    #C0292
    ChrTalk(
        0x9,
        (
            "うちはパン屋だが\x01",
            "表にちょっとした\x01",
            "カフェスペースも設けてるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0293
    ChrTalk(
        0x9,
        (
            "ちょいと食べるのに便利だろ？\x01",
            "まァ使いたきゃ自由に使ってくれや。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_5733")

    label("loc_56C5")


    #C0294
    ChrTalk(
        0x9,
        (
            "うちは表にちょっとした\x01",
            "カフェスペースも設けてるぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0295
    ChrTalk(
        0x9,
        (
            "ドリンクサービスもあるから\x01",
            "自由に使ってくれや。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5733")

    Return()

    # Function_9_455B end

    def Function_10_5734(): pass

    label("Function_10_5734")


    #C0296
    ChrTalk(
        0xFE,
        (
            "よう、いらっしゃい。\x01",
            "今月の新作パンも売りに出してるぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0297
    ChrTalk(
        0xFE,
        (
            "そうだなぁ、今月のパンには\x01",
            "こんなコーヒーが合うだろ。\x01",
            "良かったら覚えていけよ。\x02",
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
            "のレシピを教えてもらった。\x02",
        )
    )

    CloseMessageWindow()

    #A0299
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1D3),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "のレシピを覚えた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    OP_B0(0x17)
    Return()

    # Function_10_5734 end

    def Function_11_583B(): pass

    label("Function_11_583B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6, 0x1, 0x0)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6, 0x1, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_586D")
    TurnDirection(0x0, 0xA, 0)
    OP_4B(0xA, 0xFF)
    Call(0, 31)
    Return()

    label("loc_586D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6, 0x1, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6, 0x1, 0x3)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_59DA")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x12F, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_595E")

    #C0300
    ChrTalk(
        0xA,
        "あ……\x02",
    )

    CloseMessageWindow()

    #C0301
    ChrTalk(
        0xA,
        "食材、とってきてくれた？\x02",
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
            "【集めた食材を渡す】\x01",      # 0
            "【やめておく】\x01",            # 1
        )
    )

    MenuEnd(0x0)
    FadeToBright(300, 0)
    OP_60(0x0)
    OP_5A()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_592D"),
        (1, "loc_5935"),
        (SWITCH_DEFAULT, "loc_5959"),
    )


    label("loc_592D")

    Call(0, 32)
    Jump("loc_5959")

    label("loc_5935")


    #C0302
    ChrTalk(
        0xA,
        (
            "そう……\x01",
            "早めにお願いね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5959")

    label("loc_5959")

    Jump("loc_59D5")

    label("loc_595E")


    #C0303
    ChrTalk(
        0xFE,
        (
            "私の依頼は\x01",
            "『魔獣の卵』を２つよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0304
    ChrTalk(
        0xFE,
        (
            "私も新作パンの研究をしてるの。\x01",
            "なるべく早く、\x01",
            "オスカーには内緒でお願いね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_59D5")

    Jump("loc_66E4")

    label("loc_59DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_END)), "loc_5B0C")

    #C0305
    ChrTalk(
        0xFE,
        (
            "きょ、今日はどうもありがとう。\x01",
            "お陰で助かったわ。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x71, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5A5E")

    #C0306
    ChrTalk(
        0xFE,
        (
            "ふふ……これでオスカーの奴を\x01",
            "出し抜いてやる……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5ADA")

    label("loc_5A5E")


    #C0307
    ChrTalk(
        0xFE,
        (
            "ちょっと遅かった気がするけど……\x01",
            "そこは気にしない事にする。\x02",
        )
    )

    CloseMessageWindow()

    #C0308
    ChrTalk(
        0xFE,
        (
            "ふふ、オスカーめ……\x01",
            "今度こそ負かしてやるんだから……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5ADA")


    #C0309
    ChrTalk(
        0x101,
        (
            "#0000Fパン屋の修行、\x01",
            "頑張ってくれよな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_66E4")

    label("loc_5B0C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_5B1A")
    Jump("loc_66E4")

    label("loc_5B1A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_5C1F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5BBF")

    #C0310
    ChrTalk(
        0xFE,
        (
            "ふふふ……いよいよ\x01",
            "私の最高傑作が焼きあがるのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0311
    ChrTalk(
        0xFE,
        (
            "この一月、研究に研究を重ねた\x01",
            "薫り高いくるみパン！\x02",
        )
    )

    CloseMessageWindow()

    #C0312
    ChrTalk(
        0xFE,
        "さあ、驚けオスカー！！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_5C1A")

    label("loc_5BBF")


    #C0313
    ChrTalk(
        0xFE,
        (
            "ふふふ……いよいよ\x01",
            "私の最高傑作が焼きあがるのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0314
    ChrTalk(
        0xFE,
        "さあ、負けを認めろオスカー！！\x02",
    )

    CloseMessageWindow()

    label("loc_5C1A")

    Jump("loc_66E4")

    label("loc_5C1F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_5C69")
    OP_93(0xFE, 0x0, 0x0)

    #C0315
    ChrTalk(
        0xFE,
        (
            "うつら、うつら……\x01",
            "６２度で……２時間発酵………\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_66E4")

    label("loc_5C69")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_5D82")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5D2C")

    #C0316
    ChrTalk(
        0xFE,
        (
            "ウチの店が\x01",
            "最新のクロスベルタイムズで\x01",
            "取り上げられたの。\x02",
        )
    )

    CloseMessageWindow()

    #C0317
    ChrTalk(
        0xFE,
        (
            "でも……紹介されたのは\x01",
            "私でも父さんでもなくて\x01",
            "なぜかオスカーだったのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0318
    ChrTalk(
        0xFE,
        "ううっ、なんでよう……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_5D7D")

    label("loc_5D2C")


    #C0319
    ChrTalk(
        0xFE,
        (
            "それも『若き天才パン職人』\x01",
            "だなんて……\x02",
        )
    )

    CloseMessageWindow()

    #C0320
    ChrTalk(
        0xFE,
        "ううっ、私は絶対認めないわ……\x02",
    )

    CloseMessageWindow()

    label("loc_5D7D")

    Jump("loc_66E4")

    label("loc_5D82")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_5E9E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5E31")

    #C0321
    ChrTalk(
        0xFE,
        "新作パンを研究中なのよ。\x02",
    )

    CloseMessageWindow()

    #C0322
    ChrTalk(
        0xFE,
        (
            "今回は蜂蜜とくるみを\x01",
            "ふんだんに使ったパンよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0323
    ChrTalk(
        0xFE,
        (
            "まだまだ焼き上がりを研究中だけど\x01",
            "……ふふ、今回は勝算ありよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_5E99")

    label("loc_5E31")


    #C0324
    ChrTalk(
        0xFE,
        (
            "記念祭中の売り上げは\x01",
            "互角だったけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0325
    ChrTalk(
        0xFE,
        (
            "ふふ、見てなさいオスカー。\x01",
            "今度こそ負かしてやるから。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5E99")

    Jump("loc_66E4")

    label("loc_5E9E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_5FB7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5F4C")
    OP_93(0xA, 0x10E, 0x0)

    #C0326
    ChrTalk(
        0xFE,
        (
            "………………………（コネコネ）\x01",
            "うん、パン生地はこんな所かしら。\x02",
        )
    )

    CloseMessageWindow()

    #C0327
    ChrTalk(
        0xFE,
        (
            "今度こそ……今度こそオスカーを\x01",
            "ぎゃふんと言わせてやるんだから……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_5FB2")

    label("loc_5F4C")


    #C0328
    ChrTalk(
        0xFE,
        (
            "記念祭に向けて、\x01",
            "オリジナルパンを作っているの。\x02",
        )
    )

    CloseMessageWindow()

    #C0329
    ChrTalk(
        0xFE,
        (
            "……き、期待しててね。\x01",
            "いいパンを作るから。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5FB2")

    Jump("loc_66E4")

    label("loc_5FB7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_6032")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5FD2")
    Call(0, 12)
    Jump("loc_602D")

    label("loc_5FD2")

    TurnDirection(0xA, 0x9, 0)

    #C0330
    ChrTalk(
        0xFE,
        (
            "と、とにかく厨房は\x01",
            "私が使いたいの！\x02",
        )
    )

    CloseMessageWindow()

    #C0331
    ChrTalk(
        0xFE,
        (
            "しばらく貸して\x01",
            "くれてもいいじゃない！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_602D")

    Jump("loc_66E4")

    label("loc_6032")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_6142")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_60FA")
    OP_93(0xA, 0x5A, 0x0)

    #C0332
    ChrTalk(
        0xFE,
        (
            "あれっ、私が確保してた\x01",
            "高級小麦粉がない……\x02",
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
            "また父さんね。\x01",
            "勝手に人の食材を使って……！\x02",
        )
    )

    CloseMessageWindow()

    #C0334
    ChrTalk(
        0xFE,
        (
            "これじゃあ\x01",
            "パンが作れないじゃない！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_613D")

    label("loc_60FA")


    #C0335
    ChrTalk(
        0xFE,
        (
            "これだから父さんは嫌いなのよ。\x01",
            "いっつも無神経なんだから……！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_613D")

    Jump("loc_66E4")

    label("loc_6142")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_6298")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6225")

    #C0336
    ChrTalk(
        0xFE,
        (
            "パン作りの第一歩は\x01",
            "やっぱり食材選びね。\x02",
        )
    )

    CloseMessageWindow()

    #C0337
    ChrTalk(
        0xFE,
        (
            "今じゃ横断鉄道もあるし\x01",
            "簡単に色んな品が取り寄せられるの。\x02",
        )
    )

    CloseMessageWindow()

    #C0338
    ChrTalk(
        0xFE,
        (
            "今度はオレド自治州産の\x01",
            "小麦粉を使ってみようかしら……\x01",
            "いいパンが作れそうな気がするの。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_6293")

    label("loc_6225")


    #C0339
    ChrTalk(
        0xFE,
        (
            "わ、私の見たところ\x01",
            "私とオスカーの腕は互角よ。\x02",
        )
    )

    CloseMessageWindow()

    #C0340
    ChrTalk(
        0xFE,
        (
            "まだ負けてないもの。\x01",
            "材料の工夫で差をつけてやる……！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6293")

    Jump("loc_66E4")

    label("loc_6298")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_62F0")

    #C0341
    ChrTalk(
        0xFE,
        "……今日のパンは私が焼いたのよ。\x02",
    )

    CloseMessageWindow()

    #C0342
    ChrTalk(
        0xFE,
        "よ、よかったら食べて行ってね。\x02",
    )

    CloseMessageWindow()
    Jump("loc_66E4")

    label("loc_62F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_6411")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_63B8")

    #C0343
    ChrTalk(
        0xFE,
        (
            "たしかにオスカーの才能は認めるわ。\x01",
            "たった２年で\x01",
            "父さんに認められるなんてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0344
    ChrTalk(
        0xFE,
        (
            "フン……だからって\x01",
            "私が負けたわけじゃないから。\x02",
        )
    )

    CloseMessageWindow()

    #C0345
    ChrTalk(
        0xFE,
        "明日こそぎゃふんと言わせてやる。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_640C")

    label("loc_63B8")


    #C0346
    ChrTalk(
        0xFE,
        (
            "ふふん、オスカー\x01",
            "みてなさいよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0347
    ChrTalk(
        0xFE,
        (
            "明日こそぎゃふんと\x01",
            "言わせてやるから……！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_640C")

    Jump("loc_66E4")

    label("loc_6411")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_6476")

    #C0348
    ChrTalk(
        0xFE,
        "……いらっしゃいませ。\x02",
    )

    CloseMessageWindow()

    #C0349
    ChrTalk(
        0xFE,
        (
            "うちは今日も平常営業よ。\x01",
            "パン屋に休みはないんだから。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_66E4")

    label("loc_6476")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_65D2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_655E")

    #C0350
    ChrTalk(
        0xFE,
        (
            "オスカーはある日\x01",
            "ウチに弟子入りしたいって\x01",
            "やって来たの。\x02",
        )
    )

    CloseMessageWindow()

    #C0351
    ChrTalk(
        0xFE,
        (
            "そのまま父さんに話を付けて、\x01",
            "ずっーと修行してて……\x02",
        )
    )

    CloseMessageWindow()

    #C0352
    ChrTalk(
        0xFE,
        "今じゃ立派な一番弟子よ。\x02",
    )

    CloseMessageWindow()

    #C0353
    ChrTalk(
        0xFE,
        (
            "う……\x01",
            "娘である私を差し置いて\x01",
            "一番弟子だなんて……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_65CD")

    label("loc_655E")


    #C0354
    ChrTalk(
        0xFE,
        (
            "パン作りのキャリアは\x01",
            "私の方がずっと長いのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0355
    ChrTalk(
        0xFE,
        (
            "その私を差し置いて\x01",
            "一番弟子だなんて……\x01",
            "許せないわ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_65CD")

    Jump("loc_66E4")

    label("loc_65D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_66E4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_662C")

    #C0356
    ChrTalk(
        0xFE,
        "……いらっしゃいませ。\x02",
    )

    CloseMessageWindow()

    #C0357
    ChrTalk(
        0xFE,
        "お会計ならカウンターでお願いね。\x02",
    )

    CloseMessageWindow()
    Jump("loc_66E4")

    label("loc_662C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_66A4")

    #C0358
    ChrTalk(
        0xFE,
        "ウチの新作パンは人気商品なのよ。\x02",
    )

    CloseMessageWindow()

    #C0359
    ChrTalk(
        0xFE,
        (
            "それを継ぐのは看板娘の\x01",
            "私だったはずなのに……\x01",
            "ぶつぶつ……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_66E4")

    label("loc_66A4")


    #C0360
    ChrTalk(
        0xFE,
        (
            "新作パン作りを継ぐのは\x01",
            "私だったはずなのに……\x01",
            "ぶつぶつ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_66E4")

    TalkEnd(0xFE)
    Return()

    # Function_11_583B end

    def Function_12_66E8(): pass

    label("Function_12_66E8")

    OP_4B(0x9, 0xFF)
    OP_4B(0xA, 0xFF)
    TurnDirection(0x9, 0xA, 0)
    TurnDirection(0xA, 0x9, 0)

    #C0361
    ChrTalk(
        0xA,
        (
            "父さんもたまには\x01",
            "お店に出たらどうなの？\x02",
        )
    )

    CloseMessageWindow()

    #C0362
    ChrTalk(
        0xA,
        (
            "最近は厨房に\x01",
            "篭りっぱなしじゃない。\x02",
        )
    )

    CloseMessageWindow()

    #C0363
    ChrTalk(
        0x9,
        "フン、娘よ何言ってやがる。\x02",
    )

    CloseMessageWindow()

    #C0364
    ChrTalk(
        0x9,
        (
            "そりゃあオスカーが\x01",
            "男前だからに決まってんだろ！\x02",
        )
    )

    CloseMessageWindow()

    #C0365
    ChrTalk(
        0x9,
        (
            "むさい親父より客受けがいい～♪\x01",
            "現にあいつが来てから\x01",
            "女性客が倍増したからなァ。\x02",
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
            "むー、父さんはいつも\x01",
            "その調子なんだから……\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x9, 0xFF)
    OP_4C(0xA, 0xFF)
    SetScenarioFlags(0x0, 1)
    SetScenarioFlags(0x0, 2)
    Return()

    # Function_12_66E8 end

    def Function_13_6858(): pass

    label("Function_13_6858")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_68BA")

    #C0367
    ChrTalk(
        0xFE,
        (
            "ベネットさん、\x01",
            "どうしちゃったのかしら。\x02",
        )
    )

    CloseMessageWindow()

    #C0368
    ChrTalk(
        0xFE,
        "さっき飛び出して行ったけど……\x02",
    )

    CloseMessageWindow()
    Jump("loc_776E")

    label("loc_68BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_692A")

    #C0369
    ChrTalk(
        0xFE,
        (
            "今日はとっても\x01",
            "いい匂いがするわね……\x02",
        )
    )

    CloseMessageWindow()

    #C0370
    ChrTalk(
        0xFE,
        (
            "ああん、気になるなぁ……\x01",
            "今度の新作パンかしら……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_776E")

    label("loc_692A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_6A64")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_69F0")

    #C0371
    ChrTalk(
        0xFE,
        (
            "このお店のパンを買って\x01",
            "パパとママに食べさせてやったの。\x02",
        )
    )

    CloseMessageWindow()

    #C0372
    ChrTalk(
        0xFE,
        (
            "毎日食べたくなるでしょって\x01",
            "言ったら、黙って納得したわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0373
    ChrTalk(
        0xFE,
        (
            "ふふっ、大成功！\x01",
            "これでパン屋通いも公認ね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_6A5F")

    label("loc_69F0")


    #C0374
    ChrTalk(
        0xFE,
        (
            "ん～、今月の\x01",
            "新作パンはバターパンね。\x02",
        )
    )

    CloseMessageWindow()

    #C0375
    ChrTalk(
        0xFE,
        (
            "これも美味しそう……\x01",
            "焼きたての所を\x01",
            "カフェでいただこうかしら。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6A5F")

    Jump("loc_776E")

    label("loc_6A64")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_6B84")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6B2C")

    #C0376
    ChrTalk(
        0xFE,
        (
            "パン屋に通ってる事が\x01",
            "パパとママにばれちゃったの。\x02",
        )
    )

    CloseMessageWindow()

    #C0377
    ChrTalk(
        0xFE,
        (
            "２人ともお堅いから\x01",
            "外食なんて絶対許さない、だって。\x02",
        )
    )

    CloseMessageWindow()

    #C0378
    ChrTalk(
        0xFE,
        (
            "え～ん、いいじゃない！\x01",
            "ここのパン、美味しいんだから～！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_6B7F")

    label("loc_6B2C")


    #C0379
    ChrTalk(
        0xFE,
        (
            "このままだと\x01",
            "お小遣いも禁止されちゃいそう。\x02",
        )
    )

    CloseMessageWindow()

    #C0380
    ChrTalk(
        0xFE,
        "パパもママもお堅いのよね……\x02",
    )

    CloseMessageWindow()

    label("loc_6B7F")

    Jump("loc_776E")

    label("loc_6B84")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_6C08")

    #C0381
    ChrTalk(
        0xFE,
        (
            "記念祭は友達と遊んで\x01",
            "楽しかったな～。\x02",
        )
    )

    CloseMessageWindow()

    #C0382
    ChrTalk(
        0xFE,
        (
            "……でもチルル\x01",
            "また旅に出るんだって。\x02",
        )
    )

    CloseMessageWindow()

    #C0383
    ChrTalk(
        0xFE,
        "ほんと街にいない子よね～。\x02",
    )

    CloseMessageWindow()
    Jump("loc_776E")

    label("loc_6C08")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_6CD6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6CA0")

    #C0384
    ChrTalk(
        0xFE,
        "友達と約束してたのに……\x02",
    )

    CloseMessageWindow()

    #C0385
    ChrTalk(
        0xFE,
        "来ないのよねー……\x02",
    )

    CloseMessageWindow()

    #C0386
    ChrTalk(
        0xFE,
        (
            "チルルったら何してるのかしら。\x01",
            "パン屋で待ち合わせって言ったのに。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_6CD1")

    label("loc_6CA0")


    #C0387
    ChrTalk(
        0xFE,
        (
            "んもう……まさか\x01",
            "約束忘れてないわよねえ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6CD1")

    Jump("loc_776E")

    label("loc_6CD6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_6E39")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6DD3")

    #C0388
    ChrTalk(
        0xFE,
        (
            "（……今日はオスカーさんに\x01",
            "  １つおまけしてもらっちゃったの！）\x02",
        )
    )

    CloseMessageWindow()

    #C0389
    ChrTalk(
        0xFE,
        (
            "（いつも買いに来てくれて\x01",
            "  ありがとう、だって。）\x02",
        )
    )

    CloseMessageWindow()

    #C0390
    ChrTalk(
        0xFE,
        (
            "（ドキドキ……\x01",
            "  ふう、びっくりしたぁ……）\x02",
        )
    )

    CloseMessageWindow()

    #C0391
    ChrTalk(
        0xFE,
        (
            "（だってオスカーさん、\x01",
            "  ハンサムなんだもの。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_6E34")

    label("loc_6DD3")


    #C0392
    ChrTalk(
        0xFE,
        (
            "（じょ、常連になると\x01",
            "  お得なことが多いわよね。）\x02",
        )
    )

    CloseMessageWindow()

    #C0393
    ChrTalk(
        0xFE,
        "（うん、明日からも毎日来ようっと。）\x02",
    )

    CloseMessageWindow()

    label("loc_6E34")

    Jump("loc_776E")

    label("loc_6E39")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_6F71")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6EFE")

    #C0394
    ChrTalk(
        0xFE,
        (
            "記念祭は友達と\x01",
            "一緒に回る事にしてるんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0395
    ChrTalk(
        0xFE,
        "あの子、ちゃんと帰ってくるのかなぁ。\x02",
    )

    CloseMessageWindow()

    #C0396
    ChrTalk(
        0xFE,
        (
            "普段から『ニンゲンには興味ないの』\x01",
            "とか言ってる子だから、心配だわ……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_6F6C")

    label("loc_6EFE")


    #C0397
    ChrTalk(
        0xFE,
        (
            "チルル、ちゃんと記念祭には\x01",
            "帰ってくるのかなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0398
    ChrTalk(
        0xFE,
        (
            "約束を忘れて遠い国に\x01",
            "行っちゃったりしないわよね……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6F6C")

    Jump("loc_776E")

    label("loc_6F71")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_7050")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7006")

    #C0399
    ChrTalk(
        0xFE,
        (
            "チルルったら\x01",
            "また旅に出てるみたい……\x02",
        )
    )

    CloseMessageWindow()

    #C0400
    ChrTalk(
        0xFE,
        (
            "今度はどこに行っちゃったのかしら。\x01",
            "新作パンを一緒に食べようと思ったのに。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_704B")

    label("loc_7006")


    #C0401
    ChrTalk(
        0xFE,
        (
            "チルルって変わってるのよね。\x01",
            "今度はどこに行っちゃったのかしら。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_704B")

    Jump("loc_776E")

    label("loc_7050")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_7178")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_710B")

    #C0402
    ChrTalk(
        0xFE,
        "あ、今月の新作パンが出てる！\x02",
    )

    CloseMessageWindow()

    #C0403
    ChrTalk(
        0xFE,
        (
            "ここのお店の新作パンは\x01",
            "それはもうとっても美味しいのよ。\x01",
            "ついつい通い詰めちゃうのよね～。\x02",
        )
    )

    CloseMessageWindow()

    #C0404
    ChrTalk(
        0xFE,
        "……パパとママには内緒よ？\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_7173")

    label("loc_710B")


    #C0405
    ChrTalk(
        0xFE,
        (
            "ふう……最近すっかり\x01",
            "常連になっちゃったかも。\x02",
        )
    )

    CloseMessageWindow()

    #C0406
    ChrTalk(
        0xFE,
        (
            "でも美味しいんだもの。\x01",
            "これも仕方ないわよね～。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7173")

    Jump("loc_776E")

    label("loc_7178")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_72F7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_729B")

    #C0407
    ChrTalk(
        0xFE,
        "オスカーさんって結構ハンサムよね。\x02",
    )

    CloseMessageWindow()

    #C0408
    ChrTalk(
        0xFE,
        (
            "顔立ちだって端整でカッコいいし\x01",
            "いつも明るくて余裕あるし……\x02",
        )
    )

    CloseMessageWindow()

    #C0409
    ChrTalk(
        0xFE,
        (
            "なんだかパン屋さんには\x01",
            "もったいないかも……\x02",
        )
    )

    CloseMessageWindow()

    #C0410
    ChrTalk(
        0xFE,
        (
            "その、パン屋さんしてても\x01",
            "ハンサムだけどね！\x02",
        )
    )

    CloseMessageWindow()

    #C0411
    ChrTalk(
        0x101,
        (
            "#0003F（……オスカーって昔から\x01",
            "  結構もてるんだよな。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_72F2")

    label("loc_729B")


    #C0412
    ChrTalk(
        0xFE,
        "オスカーさんってハンサムよね……\x02",
    )

    CloseMessageWindow()

    #C0413
    ChrTalk(
        0xFE,
        (
            "なんだかパン屋さんには\x01",
            "もったいないかも……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_72F2")

    Jump("loc_776E")

    label("loc_72F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_740C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_73AE")

    #C0414
    ChrTalk(
        0xFE,
        "卵サンドにクロワッサン……\x02",
    )

    CloseMessageWindow()

    #C0415
    ChrTalk(
        0xFE,
        (
            "うん、ドーナツも買って帰ろっと。\x01",
            "おやつに丁度いいわよね㈱\x02",
        )
    )

    CloseMessageWindow()

    #C0416
    ChrTalk(
        0xFE,
        (
            "あ、でも買いすぎかしら……\x01",
            "でもおやつも欲しいわよね……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_7407")

    label("loc_73AE")


    #C0417
    ChrTalk(
        0xFE,
        (
            "あっちは焼きたてだし\x01",
            "こっちは期間限定の新作パン……\x02",
        )
    )

    CloseMessageWindow()

    #C0418
    ChrTalk(
        0xFE,
        "うーん、どれも迷うわ～……\x02",
    )

    CloseMessageWindow()

    label("loc_7407")

    Jump("loc_776E")

    label("loc_740C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_7528")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_74A6")

    #C0419
    ChrTalk(
        0xFE,
        "私の友達って変わってるのよね～。\x02",
    )

    CloseMessageWindow()

    #C0420
    ChrTalk(
        0xFE,
        "暇さえあれば旅に出ちゃうの。\x02",
    )

    CloseMessageWindow()

    #C0421
    ChrTalk(
        0xFE,
        (
            "今日も遊びに来たけど、\x01",
            "出かけちゃった後だったわ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_7523")

    label("loc_74A6")


    #C0422
    ChrTalk(
        0xFE,
        (
            "チルルったら\x01",
            "また旅に出ちゃったのね。\x01",
            "今日も会えなかったわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0423
    ChrTalk(
        0xFE,
        (
            "うん、仕方ないから\x01",
            "今日もここのパンを買って帰ろっと。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7523")

    Jump("loc_776E")

    label("loc_7528")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_766A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_75DA")
    OP_93(0xFE, 0x0, 0x0)

    #C0424
    ChrTalk(
        0xFE,
        "ふむふむ、今月の新作パン……\x02",
    )

    CloseMessageWindow()

    #C0425
    ChrTalk(
        0xFE,
        (
            "カリカリベーコンの\x01",
            "スパイシーブレッド……\x02",
        )
    )

    CloseMessageWindow()

    #C0426
    ChrTalk(
        0xFE,
        (
            "ううっ……しかも焼きたてですって。\x01",
            "これは美味しそうね……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_7665")

    label("loc_75DA")


    #C0427
    ChrTalk(
        0xFE,
        (
            "このパン屋さんって\x01",
            "毎月新作を売り出してるみたい。\x02",
        )
    )

    CloseMessageWindow()

    #C0428
    ChrTalk(
        0xFE,
        (
            "ううっ、すごく美味しそう……\x01",
            "……我慢できないから\x01",
            "やっぱり１つ買って帰ろっと。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7665")

    Jump("loc_776E")

    label("loc_766A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_776E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7706")

    #C0429
    ChrTalk(
        0xFE,
        (
            "わーお、とっても\x01",
            "ステキなパン屋さん！\x02",
        )
    )

    CloseMessageWindow()

    #C0430
    ChrTalk(
        0xFE,
        (
            "西通りには友達に会いに\x01",
            "来たんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0431
    ChrTalk(
        0xFE,
        (
            "ついでにいいお店\x01",
            "見つけちゃったわ㈱\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_776E")

    label("loc_7706")


    #C0432
    ChrTalk(
        0xFE,
        (
            "このパン屋さんて\x01",
            "とってもステキな雰囲気ね。\x02",
        )
    )

    CloseMessageWindow()

    #C0433
    ChrTalk(
        0xFE,
        (
            "ふふっ、気に入っちゃった。\x01",
            "１つ買って帰ろうかな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_776E")

    TalkEnd(0xFE)
    Return()

    # Function_13_6858 end

    def Function_14_7772(): pass

    label("Function_14_7772")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_77D2")

    #C0434
    ChrTalk(
        0xFE,
        "今日で国に帰らねばならんのだ。\x02",
    )

    CloseMessageWindow()

    #C0435
    ChrTalk(
        0xFE,
        (
            "たっぷりお土産を\x01",
            "買っていかんとのう。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7890")

    label("loc_77D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_77E0")
    Jump("loc_7890")

    label("loc_77E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_7821")

    #C0436
    ChrTalk(
        0xFE,
        (
            "カフェでコーヒーと一緒に\x01",
            "頂くとしようかのう。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7890")

    label("loc_7821")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_7890")

    #C0437
    ChrTalk(
        0xFE,
        (
            "祭りを見て回ってるうちに\x01",
            "良い店をみつけたわい。\x02",
        )
    )

    CloseMessageWindow()

    #C0438
    ChrTalk(
        0xFE,
        (
            "ほほほ、どれも美味そうな\x01",
            "パンばかりじゃよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7890")

    TalkEnd(0xFE)
    Return()

    # Function_14_7772 end

    def Function_15_7894(): pass

    label("Function_15_7894")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_7903")

    #C0439
    ChrTalk(
        0xFE,
        (
            "お祭りのパレードも\x01",
            "ばっちり見物したし……\x02",
        )
    )

    CloseMessageWindow()

    #C0440
    ChrTalk(
        0xFE,
        (
            "後はのんびり\x01",
            "街を回ってみようかしらね～。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7A49")

    label("loc_7903")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_7911")
    Jump("loc_7A49")

    label("loc_7911")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_7989")

    #C0441
    ChrTalk(
        0xFE,
        (
            "ホテルの食事サービスを断って\x01",
            "こっちに来ちゃったわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0442
    ChrTalk(
        0xFE,
        (
            "街中で食べた方が\x01",
            "お祭りって気分がするもの。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7A49")

    label("loc_7989")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_7A49")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7A18")

    #C0443
    ChrTalk(
        0xFE,
        (
            "クロスベル市って広いわねー。\x01",
            "歩き疲れちゃったわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0444
    ChrTalk(
        0xFE,
        (
            "お父さんったらトコトコ\x01",
            "１人で歩いて行っちゃうんだもの。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_7A49")

    label("loc_7A18")


    #C0445
    ChrTalk(
        0xFE,
        (
            "このカフェで一休み\x01",
            "させてもらおうかしらね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7A49")

    TalkEnd(0xFE)
    Return()

    # Function_15_7894 end

    def Function_16_7A4D(): pass

    label("Function_16_7A4D")

    Call(0, 17)
    Return()

    # Function_16_7A4D end

    def Function_17_7A51(): pass

    label("Function_17_7A51")

    TalkBegin(0xF)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2E, 0x1, 0x1)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2E, 0x1, 0x3)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2E, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7A76")
    Call(0, 33)
    Return()

    label("loc_7A76")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7A80")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_959E")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7ADE")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_7ADE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7B6E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_7AFD")
    OP_AF(0x2F)
    Jump("loc_7B5F")

    label("loc_7AFD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_7B0D")
    OP_AF(0x2E)
    Jump("loc_7B5F")

    label("loc_7B0D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_7B1D")
    OP_AF(0x2D)
    Jump("loc_7B5F")

    label("loc_7B1D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_7B2D")
    OP_AF(0x2C)
    Jump("loc_7B5F")

    label("loc_7B2D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_7B3D")
    OP_AF(0x2B)
    Jump("loc_7B5F")

    label("loc_7B3D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_7B4D")
    OP_AF(0x2A)
    Jump("loc_7B5F")

    label("loc_7B4D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_7B5D")
    OP_AF(0x29)
    Jump("loc_7B5F")

    label("loc_7B5D")

    OP_AF(0x28)

    label("loc_7B5F")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9599")

    label("loc_7B6E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7B82")
    Jump("loc_9599")

    label("loc_7B82")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9599")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2E, 0x1, 0x4)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7C39")

    #C0446
    ChrTalk(
        0xF,
        (
            "おっ、リクエムの花を\x01",
            "とってこれたみたいだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0447
    ChrTalk(
        0xF,
        (
            "手間をかけさせて悪かったね。\x01",
            "あとでクイントさんにも\x01",
            "謝っとかなきゃな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9599")

    label("loc_7C39")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2E, 0x1, 0x3)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2E, 0x1, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7CD5")

    #C0448
    ChrTalk(
        0xF,
        (
            "山道のトンネルから\x01",
            "遺跡に向かう分かれ道に入ると、\x01",
            "途中にリクエムの花の咲いた場所があるよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0449
    ChrTalk(
        0xF,
        "気をつけていっといで。\x02",
    )

    CloseMessageWindow()
    Jump("loc_9599")

    label("loc_7CD5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x94, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7E04")

    #C0450
    ChrTalk(
        0xF,
        (
            "うちのモモは本好きでね。\x01",
            "最近は娯楽小説なんかも\x01",
            "読んでるみたいなんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0451
    ChrTalk(
        0xF,
        (
            "でも一部の巻だけ\x01",
            "手に入らなかったらしくてね……\x02",
        )
    )

    CloseMessageWindow()

    #C0452
    ChrTalk(
        0xF,
        (
            "あんまり寂しそうにしてたから、\x01",
            "つい店の方で仕入れちゃったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0453
    ChrTalk(
        0xF,
        (
            "はは、良かったら\x01",
            "君たちも見ていくかい？\x01",
            "ほんとに一部の巻だけなんだけどさ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x94, 6)
    Jump("loc_9599")

    label("loc_7E04")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_7E52")

    #C0454
    ChrTalk(
        0xF,
        "モモ、今日は半べそかいてたけど……\x02",
    )

    CloseMessageWindow()

    #C0455
    ChrTalk(
        0xF,
        "何かあったのかな。\x02",
    )

    CloseMessageWindow()
    Jump("loc_9599")

    label("loc_7E52")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_7ED9")

    #C0456
    ChrTalk(
        0xF,
        "最近失踪者が出てるって本当かい？\x02",
    )

    CloseMessageWindow()

    #C0457
    ChrTalk(
        0xF,
        "まさか……人攫いとかかな。\x02",
    )

    CloseMessageWindow()

    #C0458
    ChrTalk(
        0xF,
        (
            "怖いなぁ……\x01",
            "後でモモにも注意しておかないと。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9599")

    label("loc_7ED9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_8001")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7F91")

    #C0459
    ChrTalk(
        0xF,
        (
            "うちのモモ、最近は\x01",
            "友達と遊んでるみたいなんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0460
    ChrTalk(
        0xF,
        "引っ込み思案も治ってきたのかな。\x02",
    )

    CloseMessageWindow()

    #C0461
    ChrTalk(
        0xF,
        (
            "最近は何かと怖い事件を\x01",
            "耳にするけど……\x01",
            "ちょっと救われるな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_7FFC")

    label("loc_7F91")


    #C0462
    ChrTalk(
        0xF,
        (
            "最近は何かと事件を耳にするけど\x01",
            "やっぱり子供の笑顔が一番だよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0463
    ChrTalk(
        0xF,
        "早く平和になって欲しいものだよ。\x02",
    )

    CloseMessageWindow()

    label("loc_7FFC")

    Jump("loc_9599")

    label("loc_8001")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_816D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_80E0")

    #C0464
    ChrTalk(
        0xF,
        (
            "やあいらっしゃい。\x01",
            "タリーズ商店へようこそ。\x02",
        )
    )

    CloseMessageWindow()

    #C0465
    ChrTalk(
        0xF,
        (
            "……最近あちこちから\x01",
            "ルバーチェの噂を聞くね。\x02",
        )
    )

    CloseMessageWindow()

    #C0466
    ChrTalk(
        0xF,
        (
            "また市街で\x01",
            "トラブルを起こしているとか……\x02",
        )
    )

    CloseMessageWindow()

    #C0467
    ChrTalk(
        0xF,
        (
            "うちも小さい子が\x01",
            "いるから気をつけないとな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_8168")

    label("loc_80E0")


    #C0468
    ChrTalk(
        0xF,
        (
            "付き合いのある商人さんたちの中にも\x01",
            "ルバーチェに絡まれた人がいるみたいだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0469
    ChrTalk(
        0xF,
        (
            "怖いな……うちも小さい子が\x01",
            "いるから気をつけないと。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8168")

    Jump("loc_9599")

    label("loc_816D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_8286")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_822A")

    #C0470
    ChrTalk(
        0xF,
        (
            "やれやれ、ようやく\x01",
            "日常が戻ってきたね。\x02",
        )
    )

    CloseMessageWindow()

    #C0471
    ChrTalk(
        0xF,
        (
            "５日間も騒ぐと\x01",
            "のんびりしたい気分だよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0472
    ChrTalk(
        0xF,
        (
            "エルサには\x01",
            "『いつものんびりしてるでしょ』\x01",
            "って言われちゃったけど。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_8281")

    label("loc_822A")


    #C0473
    ChrTalk(
        0xF,
        (
            "記念祭も終わって\x01",
            "日常が戻ってきた感じだよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0474
    ChrTalk(
        0xF,
        "うん、やっぱり平和が一番だよ。\x02",
    )

    CloseMessageWindow()

    label("loc_8281")

    Jump("loc_9599")

    label("loc_8286")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_83B9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8340")

    #C0475
    ChrTalk(
        0xF,
        (
            "エルサとモモは\x01",
            "ミシュラムに行っているよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0476
    ChrTalk(
        0xF,
        (
            "思いっきり楽しんでくるように\x01",
            "言ってあるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0477
    ChrTalk(
        0xF,
        (
            "いつも店を手伝ってばかりだし\x01",
            "たまには息抜きしないとね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_83B4")

    label("loc_8340")


    #C0478
    ChrTalk(
        0xF,
        (
            "エルサとモモは今頃\x01",
            "ミシュラムに行っているはずだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0479
    ChrTalk(
        0xF,
        (
            "店の方は大変だけど……\x01",
            "まあ今日一日なら何とかなるさ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_83B4")

    Jump("loc_9599")

    label("loc_83B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 7)), scpexpr(EXPR_END)), "loc_84C1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8465")

    #C0480
    ChrTalk(
        0xF,
        (
            "そうか、今日は\x01",
            "パレードの日だったんだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0481
    ChrTalk(
        0xF,
        "うーんしまったよ。\x02",
    )

    CloseMessageWindow()

    #C0482
    ChrTalk(
        0xF,
        (
            "あまり興味が無かったから\x01",
            "祭りの日程は\x01",
            "ノーチェックだったんだよねぇ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_84BC")

    label("loc_8465")


    #C0483
    ChrTalk(
        0xF,
        "今日はパレードの日だったんだな。\x02",
    )

    CloseMessageWindow()

    #C0484
    ChrTalk(
        0xF,
        (
            "エルザとモモも\x01",
            "楽しんでいるといいんだけど。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_84BC")

    Jump("loc_9599")

    label("loc_84C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_86BA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAD, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8643")

    #C0485
    ChrTalk(
        0x101,
        (
            "#0001F（うん、この人なら\x01",
            "  何か知っているかもしれないな……）\x02",
        )
    )

    CloseMessageWindow()

    #A0486
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

    #C0487
    ChrTalk(
        0xF,
        (
            "迷子の男の子か……\x01",
            "そりゃあ大変だね……\x02",
        )
    )

    CloseMessageWindow()

    #C0488
    ChrTalk(
        0xF,
        (
            "うーん、僕はパレードを\x01",
            "見逃しちゃってね。\x01",
            "少ししか見てないし……\x02",
        )
    )

    CloseMessageWindow()

    #C0489
    ChrTalk(
        0xF,
        (
            "遠目だったから\x01",
            "ちょっと判らないかな。\x02",
        )
    )

    CloseMessageWindow()

    #C0490
    ChrTalk(
        0x101,
        (
            "#0000Fそうですか……\x01",
            "ありがとうございました。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xAD, 3)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 25)
    Jump("loc_86B5")

    label("loc_8643")


    #C0491
    ChrTalk(
        0xF,
        (
            "パレードは見逃しちゃってね。\x01",
            "遠目に見ただけだったんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0492
    ChrTalk(
        0xF,
        (
            "その子が居たかどうかまでは\x01",
            "ちょっと判らないな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_86B5")

    Jump("loc_9599")

    label("loc_86BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_87C2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8766")

    #C0493
    ChrTalk(
        0xF,
        (
            "そうか、今日は\x01",
            "パレードの日だったんだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0494
    ChrTalk(
        0xF,
        "うーんしまったよ。\x02",
    )

    CloseMessageWindow()

    #C0495
    ChrTalk(
        0xF,
        (
            "あまり興味が無かったから\x01",
            "祭りの日程は\x01",
            "ノーチェックだったんだよねぇ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_87BD")

    label("loc_8766")


    #C0496
    ChrTalk(
        0xF,
        "今日はパレードの日だったんだな。\x02",
    )

    CloseMessageWindow()

    #C0497
    ChrTalk(
        0xF,
        (
            "エルザとモモも\x01",
            "楽しんでいるといいんだけど。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_87BD")

    Jump("loc_9599")

    label("loc_87C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_88A0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8864")

    #C0498
    ChrTalk(
        0xF,
        (
            "エルサとモモは\x01",
            "街の中を見て回ってるよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0499
    ChrTalk(
        0xF,
        (
            "折角だし一回りして\x01",
            "くるように言ったんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0500
    ChrTalk(
        0xF,
        (
            "せめて家族には\x01",
            "楽しんで欲しいからね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_889B")

    label("loc_8864")


    #C0501
    ChrTalk(
        0xF,
        (
            "折角のお祭りなんだ。\x01",
            "家族には楽しんで欲しいよね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_889B")

    Jump("loc_9599")

    label("loc_88A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_89C6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_895D")

    #C0502
    ChrTalk(
        0xF,
        (
            "記念祭だからって\x01",
            "特別なことは\x01",
            "しないつもりだったけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0503
    ChrTalk(
        0xF,
        (
            "今年は大々的な\x01",
            "お祭りになっちゃってるよねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0504
    ChrTalk(
        0xF,
        (
            "うーん、ウチも何か\x01",
            "やった方が良かったかな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_89C1")

    label("loc_895D")


    #C0505
    ChrTalk(
        0xF,
        (
            "ウチもセールくらい\x01",
            "やった方が良かったかな。\x02",
        )
    )

    CloseMessageWindow()

    #C0506
    ChrTalk(
        0xF,
        (
            "たはは……これこそ\x01",
            "後の祭りってやつだけどね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_89C1")

    Jump("loc_9599")

    label("loc_89C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_8AF4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8A93")

    #C0507
    ChrTalk(
        0xF,
        (
            "クロスベル自治州も\x01",
            "今年で創立７０周年になるんだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0508
    ChrTalk(
        0xF,
        (
            "となると……丁度\x01",
            "僕のお爺さんが若かった頃に\x01",
            "誕生したってことだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0509
    ChrTalk(
        0xF,
        (
            "そう考えると\x01",
            "なんだか感慨深いものがあるよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_8AEF")

    label("loc_8A93")


    #C0510
    ChrTalk(
        0xF,
        (
            "普段自治州のことなんて\x01",
            "あまり考えないけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0511
    ChrTalk(
        0xF,
        (
            "よく考えると\x01",
            "なかなか感慨深いよね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8AEF")

    Jump("loc_9599")

    label("loc_8AF4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_8BF6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8B8B")

    #C0512
    ChrTalk(
        0xF,
        (
            "ブリジッタさんと\x01",
            "例の警察犬の話をしていたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0513
    ChrTalk(
        0xF,
        (
            "さっきまで家にいたんだけど……\x01",
            "またどこかに出かけちゃったのかな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_8BF1")

    label("loc_8B8B")


    #C0514
    ChrTalk(
        0xF,
        (
            "例の警察犬は\x01",
            "またどこかに出かけちゃったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0515
    ChrTalk(
        0xF,
        (
            "この辺りをパトロール\x01",
            "してくれているみたいだね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8BF1")

    Jump("loc_9599")

    label("loc_8BF6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_8E09")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8D12")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8C8E")

    #C0516
    ChrTalk(
        0xF,
        (
            "あ、あはは……\x01",
            "大きいワンちゃんだね……\x02",
        )
    )

    CloseMessageWindow()

    #C0517
    ChrTalk(
        0xF,
        (
            "そっか、最近お客さんが噂してる\x01",
            "警察犬ってこの犬のことかぁ……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_8D0D")

    label("loc_8C8E")


    #C0518
    ChrTalk(
        0xF,
        (
            "確かに頼りになりそうな\x01",
            "警察犬だけど……\x01",
            "なんだか態度が大きいよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0519
    ChrTalk(
        0xF,
        (
            "さっき声を掛けたら\x01",
            "鼻の先であしらわれちゃったよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8D0D")

    Jump("loc_8E04")

    label("loc_8D12")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8D9E")

    #C0520
    ChrTalk(
        0xF,
        (
            "例の警察犬、うちには\x01",
            "週に２～３回来てるんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0521
    ChrTalk(
        0xF,
        (
            "さっきも来ていたんだけど……\x01",
            "またどこかに出かけちゃったのかな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_8E04")

    label("loc_8D9E")


    #C0522
    ChrTalk(
        0xF,
        (
            "例の警察犬は\x01",
            "またどこかに出かけちゃったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0523
    ChrTalk(
        0xF,
        (
            "この辺りをパトロール\x01",
            "してくれているみたいだね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8E04")

    Jump("loc_9599")

    label("loc_8E09")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_8EB9")

    #C0524
    ChrTalk(
        0xF,
        (
            "エルサがアルカンシェルの\x01",
            "話ばかりするんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0525
    ChrTalk(
        0xF,
        (
            "うーん、やっぱり\x01",
            "見に行きたいのかな。\x02",
        )
    )

    CloseMessageWindow()

    #C0526
    ChrTalk(
        0xF,
        (
            "あんまり口にしないけど\x01",
            "昔はアルカンシェルに\x01",
            "憧れてたみたいだし。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9599")

    label("loc_8EB9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_8F3C")

    #C0527
    ChrTalk(
        0xF,
        (
            "ハロルドさんの所も\x01",
            "お子さんが居るそうだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0528
    ChrTalk(
        0xF,
        (
            "うちと同じく\x01",
            "家族経営でやってるらしいし\x01",
            "何だか親近感がわくよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9599")

    label("loc_8F3C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_9095")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_900D")

    #C0529
    ChrTalk(
        0xF,
        (
            "ハロルドさん、\x01",
            "今度の蜂蜜価格が決まったから\x01",
            "知らせに来てくれたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0530
    ChrTalk(
        0xF,
        (
            "本当にこまめなんだよねぇ。\x01",
            "うちとしても嬉しいよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0531
    ChrTalk(
        0xF,
        (
            "ついでに次の仕入れについて\x01",
            "相談しておこうかな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_9090")

    label("loc_900D")


    #C0532
    ChrTalk(
        0xF,
        (
            "ハロルドさんとは\x01",
            "３年くらいの付き合いになるけど\x01",
            "本当にこまめなんだよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0533
    ChrTalk(
        0xF,
        (
            "ついでに次の仕入れの話も\x01",
            "相談しておかなくちゃ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9090")

    Jump("loc_9599")

    label("loc_9095")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_91B5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9125")

    #C0534
    ChrTalk(
        0xF,
        (
            "最近リュウ君とアンリ君、\x01",
            "見かけないよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0535
    ChrTalk(
        0xF,
        (
            "よくうちの前で\x01",
            "遊びまわってたのに……\x01",
            "どこへ行っちゃったのかな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_91B0")

    label("loc_9125")


    #C0536
    ChrTalk(
        0xF,
        (
            "最近リュウ君とアンリ君、\x01",
            "見かけないよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0537
    ChrTalk(
        0xF,
        (
            "リュウ君はたしか\x01",
            "ベルハイムに住んでたはずだけど。\x01",
            "病気でもして寝込んじゃってるのかな？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_91B0")

    Jump("loc_9599")

    label("loc_91B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_9326")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_92AD")

    #C0538
    ChrTalk(
        0xF,
        (
            "アルモリカ村から蜂蜜を\x01",
            "卸してもらってる業者さんがいるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0539
    ChrTalk(
        0xF,
        (
            "景気もいいし、近々\x01",
            "買取価格が上がるかもしれませんって\x01",
            "予告されちゃったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0540
    ChrTalk(
        0xF,
        (
            "あの人は何でも\x01",
            "事前に言ってくれるんだよね。\x01",
            "商売上手だけどいい人だよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_9321")

    label("loc_92AD")


    #C0541
    ChrTalk(
        0xF,
        (
            "情報を早めに教えてくれる\x01",
            "ってのはありがたいよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0542
    ChrTalk(
        0xF,
        (
            "ま、価格が上がるならってことで\x01",
            "多めに仕入れたんだけどね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9321")

    Jump("loc_9599")

    label("loc_9326")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_9469")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 6)), scpexpr(EXPR_END)), "loc_93DF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_93B4")

    #C0543
    ChrTalk(
        0xF,
        "うちのモモは人見知りでね。\x02",
    )

    CloseMessageWindow()

    #C0544
    ChrTalk(
        0xF,
        (
            "お客さんがくると\x01",
            "奥に引っ込んでしまうんだ。\x01",
            "うーん、困った子だなぁ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_93DA")

    label("loc_93B4")


    #C0545
    ChrTalk(
        0xF,
        "うちのモモは人見知りなんだよね。\x02",
    )

    CloseMessageWindow()

    label("loc_93DA")

    Jump("loc_9464")

    label("loc_93DF")


    #C0546
    ChrTalk(
        0xF,
        (
            "うちは雑貨屋だから\x01",
            "食材や日用品を扱ってるよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0547
    ChrTalk(
        0xF,
        (
            "それなりに便利な商品を\x01",
            "仕入れてるつもりだから、\x01",
            "見て行ってくれると嬉しいな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9464")

    Jump("loc_9599")

    label("loc_9469")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_9599")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_952F")

    #C0548
    ChrTalk(
        0xF,
        "やあ、いらっしゃい。\x02",
    )

    CloseMessageWindow()

    #C0549
    ChrTalk(
        0xF,
        (
            "日用品ならウチにお任せ！\x01",
            "地域の柱《タリーズ商店》で～す。\x02",
        )
    )

    CloseMessageWindow()

    #C0550
    ChrTalk(
        0xF,
        (
            "ちなみに『のんびりやろうよ』が\x01",
            "うちのモットーです。\x01",
            "気軽に利用していってね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_9599")

    label("loc_952F")


    #C0551
    ChrTalk(
        0xF,
        (
            "うちのモットーは\x01",
            "『のんびりやろうよ』なんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0552
    ChrTalk(
        0xF,
        (
            "ご覧の通りゆるゆるだから\x01",
            "気軽に利用していってよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9599")

    Jump("loc_7A80")

    label("loc_959E")

    TalkEnd(0xF)
    Return()

    # Function_17_7A51 end

    def Function_18_95A2(): pass

    label("Function_18_95A2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_9681")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9622")

    #C0553
    ChrTalk(
        0xFE,
        (
            "モモったら……\x01",
            "今日は友達と何かあったのかしら。\x02",
        )
    )

    CloseMessageWindow()

    #C0554
    ChrTalk(
        0xFE,
        (
            "すっかりすねてて\x01",
            "話してくれないのよね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_967C")

    label("loc_9622")


    #C0555
    ChrTalk(
        0xFE,
        (
            "まあ子供同士は\x01",
            "色々あるものだわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0556
    ChrTalk(
        0xFE,
        (
            "美味しい物でも作って\x01",
            "慰めてあげるとしますか。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_967C")

    Jump("loc_A0C7")

    label("loc_9681")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_976E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9701")

    #C0557
    ChrTalk(
        0xFE,
        (
            "イアン先生、最近お忙しそうね……\x01",
            "何件も仕事を抱えているみたいよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0558
    ChrTalk(
        0xFE,
        "支えるピート君も大変ね。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_9769")

    label("loc_9701")


    #C0559
    ChrTalk(
        0xFE,
        (
            "主人が最近事件が\x01",
            "増えているっていってたけれど、\x01",
            "そのせいなのかしら。\x02",
        )
    )

    CloseMessageWindow()

    #C0560
    ChrTalk(
        0xFE,
        "先生もピート君も大変ね。\x02",
    )

    CloseMessageWindow()

    label("loc_9769")

    Jump("loc_A0C7")

    label("loc_976E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_989E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9838")

    #C0561
    ChrTalk(
        0xFE,
        (
            "……さっき外を覗いてきたら、\x01",
            "モモが友達と遊んでいたのよ～！\x02",
        )
    )

    CloseMessageWindow()

    #C0562
    ChrTalk(
        0xFE,
        (
            "引っ込み思案なあの子がねえ……\x01",
            "お母さん、とっても嬉しいわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0563
    ChrTalk(
        0xFE,
        (
            "今夜はお赤飯でも\x01",
            "炊いてあげなくっちゃ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_9899")

    label("loc_9838")


    #C0564
    ChrTalk(
        0xFE,
        (
            "モモ、ついにやったのね～。\x01",
            "主人共々、密かに大喜びよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0565
    ChrTalk(
        0xFE,
        "今夜はお祝いしてあげなくっちゃ。\x02",
    )

    CloseMessageWindow()

    label("loc_9899")

    Jump("loc_A0C7")

    label("loc_989E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_990D")

    #C0566
    ChrTalk(
        0xFE,
        "今日は新しい商品が届いたのよ。\x02",
    )

    CloseMessageWindow()

    #C0567
    ChrTalk(
        0xFE,
        (
            "ちょっとお高い品だから\x01",
            "並べるのも気を遣っちゃうわねぇ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A0C7")

    label("loc_990D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_991B")
    Jump("loc_A0C7")

    label("loc_991B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_9A6A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_99F2")

    #C0568
    ChrTalk(
        0xFE,
        (
            "モモは店の手伝いをしてくれるし\x01",
            "聞き分けもいいから助かっちゃうわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0569
    ChrTalk(
        0xFE,
        (
            "でも……いつも\x01",
            "店の手伝いをするか\x01",
            "一人で本ばかり読んでいるのよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0570
    ChrTalk(
        0xFE,
        (
            "たまには外で\x01",
            "遊んでくればいいのにねえ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_9A65")

    label("loc_99F2")


    #C0571
    ChrTalk(
        0xFE,
        (
            "店の手伝いを\x01",
            "してくれるのはいいけど……\x01",
            "モモはこれでいいのかしら。\x02",
        )
    )

    CloseMessageWindow()

    #C0572
    ChrTalk(
        0xFE,
        (
            "本当は外で\x01",
            "遊びたいんじゃないかしら。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9A65")

    Jump("loc_A0C7")

    label("loc_9A6A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_9B6C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9B0B")

    #C0573
    ChrTalk(
        0xFE,
        "もうすぐ創立記念祭よね～。\x02",
    )

    CloseMessageWindow()

    #C0574
    ChrTalk(
        0xFE,
        (
            "でも主人はセールとかを\x01",
            "する気は無いみたいよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0575
    ChrTalk(
        0xFE,
        (
            "ふう、のほほんとしてる所が\x01",
            "あの人らしいわね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_9B67")

    label("loc_9B0B")


    #C0576
    ChrTalk(
        0xFE,
        (
            "にしても……\x01",
            "なんだか下が静かねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0577
    ChrTalk(
        0xFE,
        (
            "主人たら、居眠り\x01",
            "してるんじゃないでしょうね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9B67")

    Jump("loc_A0C7")

    label("loc_9B6C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_9CC0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9C36")

    #C0578
    ChrTalk(
        0xFE,
        (
            "アルカンシェルの新作には\x01",
            "新人アーティストが出演するそうよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0579
    ChrTalk(
        0xFE,
        (
            "しかもデビューから\x01",
            "あのイリア様と共演なんですって。\x02",
        )
    )

    CloseMessageWindow()

    #C0580
    ChrTalk(
        0xFE,
        (
            "なんだか凄いわねえ……\x01",
            "一体どんな人なのかしら。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_9CBB")

    label("loc_9C36")


    #C0581
    ChrTalk(
        0xFE,
        (
            "クロスベルの女の子なら\x01",
            "一度はアルカンシェルに憧れるものよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0582
    ChrTalk(
        0xFE,
        (
            "デビューからイリア様と\x01",
            "共演なんて……\x01",
            "まるで夢みたいな話ねえ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9CBB")

    Jump("loc_A0C7")

    label("loc_9CC0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_9D6D")

    #C0583
    ChrTalk(
        0xFE,
        "今日、モモは日曜学校なのよね。\x02",
    )

    CloseMessageWindow()

    #C0584
    ChrTalk(
        0xFE,
        (
            "あの子引っ込み思案だから、\x01",
            "上手くやってるのか\x01",
            "ちょっと心配だわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0585
    ChrTalk(
        0xFE,
        (
            "今度シスターに授業の様子を\x01",
            "聞いてみようかしら。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A0C7")

    label("loc_9D6D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_9E8E")
    OP_4B(0x15, 0xFF)
    OP_93(0xFE, 0xB4, 0x0)

    #C0586
    ChrTalk(
        0xFE,
        (
            "いえいえ、こちらこそ\x01",
            "いつもお世話になっていますー。\x02",
        )
    )

    CloseMessageWindow()

    #C0587
    ChrTalk(
        0xFE,
        (
            "それで来月の\x01",
            "仕入れなんですけどね、\x01",
            "この通りにお願いしようかと……\x02",
        )
    )

    CloseMessageWindow()

    #C0588
    ChrTalk(
        0x15,
        (
            "#3603F食材を１割追加ですね。\x01",
            "ふむ、お値段割引希望ですか……\x02\x03",

            "#3600Fははは、お任せください。\x01",
            "タリーズさんは\x01",
            "お得意様ですから。\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x15, 0xFF)
    Jump("loc_A0C7")

    label("loc_9E8E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_A040")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9FC2")

    #C0589
    ChrTalk(
        0xFE,
        (
            "中央広場まで買い物に\x01",
            "行ってきたんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0590
    ChrTalk(
        0xFE,
        (
            "外れにあった古ビルに\x01",
            "いつの間にかどこかの会社が\x01",
            "入居したみたいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0591
    ChrTalk(
        0xFE,
        (
            "いつ頃から入ったのかしら。\x01",
            "全然気付かなかったわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0592
    ChrTalk(
        0x104,
        "#0305F（……支援課のビルの事だよな？）\x02",
    )

    CloseMessageWindow()

    #C0593
    ChrTalk(
        0x101,
        (
            "#0012F（はは……やっぱり知名度は\x01",
            "  まだまだだなぁ……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_A03B")

    label("loc_9FC2")


    #C0594
    ChrTalk(
        0xFE,
        (
            "中央広場の外れにあるビル、\x01",
            "いつの間にかどこかの会社が\x01",
            "入居したみたいよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0595
    ChrTalk(
        0xFE,
        (
            "あの辺りは移り変わりが\x01",
            "激しいわねぇ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A03B")

    Jump("loc_A0C7")

    label("loc_A040")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_A0B0")

    #C0596
    ChrTalk(
        0xFE,
        "お料理お料理……♪\x02",
    )

    CloseMessageWindow()

    #C0597
    ChrTalk(
        0xFE,
        (
            "売れ残りのお野菜は\x01",
            "捨てずにウチで食べちゃうの。\x01",
            "ありがたいわよねー。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A0C7")

    label("loc_A0B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_A0BE")
    Jump("loc_A0C7")

    label("loc_A0BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_A0C7")

    label("loc_A0C7")

    TalkEnd(0xFE)
    Return()

    # Function_18_95A2 end

    def Function_19_A0CB(): pass

    label("Function_19_A0CB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_A109")

    #C0598
    ChrTalk(
        0xFE,
        (
            "ううっ、リュウ君は\x01",
            "やっぱりイジワル……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A9AD")

    label("loc_A109")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_A42D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAD, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A3B9")

    #C0599
    ChrTalk(
        0xFE,
        (
            "記念祭の最後の日は\x01",
            "リュウ君と出店を回ったの。\x02",
        )
    )

    CloseMessageWindow()

    #C0600
    ChrTalk(
        0xFE,
        "おまつり、楽しかったな……\x02",
    )

    CloseMessageWindow()

    #C0601
    ChrTalk(
        0xFE,
        "また遊べるといいな……\x02",
    )

    CloseMessageWindow()
    OP_63(0x153, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0602
    ChrTalk(
        0x153,
        "#1110Fおまつり～？\x02",
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
            "あうう……\x01",
            "なんでも、ないの……\x02",
        )
    )

    CloseMessageWindow()

    #C0604
    ChrTalk(
        0xFE,
        "その、おまつり、お友達と遊んだの。\x02",
    )

    CloseMessageWindow()

    #C0605
    ChrTalk(
        0xFE,
        "とっても楽しかったの……\x02",
    )

    CloseMessageWindow()

    #C0606
    ChrTalk(
        0x153,
        (
            "#1105Fふーん、いいな～……\x02\x03",

            "#1109Fねえロイドー、こんどは\x01",
            "みんなでおまつりに行こう～！\x02",
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
            "#0000Fそ、そうだな……\x01",
            "悪くはないかも。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_A350")

    #C0608
    ChrTalk(
        0x102,
        "#0100F来年になっちゃうけどね。\x02",
    )

    CloseMessageWindow()
    Jump("loc_A3B1")

    label("loc_A350")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_A384")

    #C0609
    ChrTalk(
        0x103,
        "#0202F来年になってしまいますが。\x02",
    )

    CloseMessageWindow()
    Jump("loc_A3B1")

    label("loc_A384")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_A3B1")

    #C0610
    ChrTalk(
        0x104,
        "#0300F来年になっちまうけどな。\x02",
    )

    CloseMessageWindow()

    label("loc_A3B1")

    SetScenarioFlags(0xAD, 6)
    Jump("loc_A428")

    label("loc_A3B9")


    #C0611
    ChrTalk(
        0xFE,
        (
            "記念祭の最後の日は\x01",
            "リュウ君と出店を回ったの。\x02",
        )
    )

    CloseMessageWindow()

    #C0612
    ChrTalk(
        0xFE,
        "おまつり、楽しかったな……\x02",
    )

    CloseMessageWindow()

    #C0613
    ChrTalk(
        0xFE,
        "また遊べるといいな……\x02",
    )

    CloseMessageWindow()

    label("loc_A428")

    Jump("loc_A9AD")

    label("loc_A42D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_A494")

    #C0614
    ChrTalk(
        0xFE,
        "うう……もうきゅーけいする……\x02",
    )

    CloseMessageWindow()

    #C0615
    ChrTalk(
        0xFE,
        (
            "だってお客さんと\x01",
            "お話しすると疲れるんだもん……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A9AD")

    label("loc_A494")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_A4A2")
    Jump("loc_A9AD")

    label("loc_A4A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_A508")

    #C0616
    ChrTalk(
        0xFE,
        (
            "えへへ、ワンちゃん\x01",
            "かわいかったな……\x02",
        )
    )

    CloseMessageWindow()

    #C0617
    ChrTalk(
        0xFE,
        (
            "また遊びたいな……\x01",
            "遊んでくれるかな……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A9AD")

    label("loc_A508")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_A617")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_A57A")

    #C0618
    ChrTalk(
        0xFE,
        (
            "えへへ、ワンちゃん\x01",
            "かわいかったな……\x02",
        )
    )

    CloseMessageWindow()

    #C0619
    ChrTalk(
        0xFE,
        (
            "また遊びたいな……\x01",
            "遊んでくれるかな……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A612")

    label("loc_A57A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A5D9")
    OP_93(0xFE, 0xB4, 0x0)

    #C0620
    ChrTalk(
        0xFE,
        "なでなで……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x0, 500)

    #C0621
    ChrTalk(
        0xFE,
        (
            "えへへ、ワンちゃん\x01",
            "気持ちよさそうだよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_A612")

    label("loc_A5D9")

    OP_93(0xFE, 0xB4, 0x0)

    #C0622
    ChrTalk(
        0xFE,
        "なでなで……\x02",
    )

    CloseMessageWindow()

    #C0623
    ChrTalk(
        0xFE,
        "ワンちゃん、かわいいな……\x02",
    )

    CloseMessageWindow()

    label("loc_A612")

    Jump("loc_A9AD")

    label("loc_A617")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_A6A5")
    OP_93(0xFE, 0x5A, 0x0)

    #C0624
    ChrTalk(
        0xFE,
        "せっせ、せっせ……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x0, 500)

    #C0625
    ChrTalk(
        0xFE,
        (
            "新しい商品が\x01",
            "入ったから並べてるの。\x02",
        )
    )

    CloseMessageWindow()

    #C0626
    ChrTalk(
        0xFE,
        (
            "瓶のラベルがみえるように\x01",
            "きれーにしないと。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A9AD")

    label("loc_A6A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_A7B8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A751")

    #C0627
    ChrTalk(
        0xFE,
        (
            "リュウ君、大きな犬に\x01",
            "助けてもらったんだって。\x02",
        )
    )

    CloseMessageWindow()

    #C0628
    ChrTalk(
        0xFE,
        (
            "いいな……\x01",
            "モモも遊びたいかも……\x02",
        )
    )

    CloseMessageWindow()

    #C0629
    ChrTalk(
        0xFE,
        (
            "じゃ、じゃなくて……\x01",
            "道路で遊んじゃダメなんだよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_A7B3")

    label("loc_A751")


    #C0630
    ChrTalk(
        0xFE,
        (
            "導力車が通るから、\x01",
            "道路で遊んじゃダメなの。\x02",
        )
    )

    CloseMessageWindow()

    #C0631
    ChrTalk(
        0xFE,
        (
            "リュウ君、ちゃんと\x01",
            "言いつけは守らないと……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A7B3")

    Jump("loc_A9AD")

    label("loc_A7B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_A94F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 6)), scpexpr(EXPR_END)), "loc_A86D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A840")

    #C0632
    ChrTalk(
        0xFE,
        "……ピート君、苦手なの。\x02",
    )

    CloseMessageWindow()

    #C0633
    ChrTalk(
        0xFE,
        (
            "前に『もっとはっきり\x01",
            "物を言ったほうがいいよ』\x01",
            "って怒られたの……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_A868")

    label("loc_A840")


    #C0634
    ChrTalk(
        0xFE,
        "ピート君、いい人だけど苦手なの……\x02",
    )

    CloseMessageWindow()

    label("loc_A868")

    Jump("loc_A94A")

    label("loc_A86D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A904")

    #C0635
    ChrTalk(
        0xFE,
        (
            "リュウ君、アンリちゃん、\x01",
            "いっしょにあそぼ……！\x02",
        )
    )

    CloseMessageWindow()

    #C0636
    ChrTalk(
        0xFE,
        "#2Sい、いっしょにあそぼ……\x02",
    )

    CloseMessageWindow()

    #C0637
    ChrTalk(
        0xFE,
        (
            "……本番で緊張しないように\x01",
            "練習してるの。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_A94A")

    label("loc_A904")


    #C0638
    ChrTalk(
        0xFE,
        "い、いっしょにあそぼ……\x02",
    )

    CloseMessageWindow()

    #C0639
    ChrTalk(
        0xFE,
        "……ちゃんと言えたらいいのにな……\x02",
    )

    CloseMessageWindow()

    label("loc_A94A")

    Jump("loc_A9AD")

    label("loc_A94F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_A9AD")

    #C0640
    ChrTalk(
        0xFE,
        (
            "リュウ君とアンリちゃん、\x01",
            "いつも楽しそうだな……\x02",
        )
    )

    CloseMessageWindow()

    #C0641
    ChrTalk(
        0xFE,
        "モモも一緒に遊びたいな……\x02",
    )

    CloseMessageWindow()

    label("loc_A9AD")

    TalkEnd(0xFE)
    Return()

    # Function_19_A0CB end

    def Function_20_A9B1(): pass

    label("Function_20_A9B1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_A9C2")
    Jump("loc_AB6B")

    label("loc_A9C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_AAD1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AA8D")

    #C0642
    ChrTalk(
        0xFE,
        (
            "先生は最近お忙しくて、\x01",
            "法律の勉強を見てくれる時間も\x01",
            "減ってしまいました。\x02",
        )
    )

    CloseMessageWindow()

    #C0643
    ChrTalk(
        0xFE,
        (
            "でも、働いている先生を見ると\x01",
            "僕も誇らしいです。\x02",
        )
    )

    CloseMessageWindow()

    #C0644
    ChrTalk(
        0xFE,
        (
            "僕も早く\x01",
            "先生のお力になりたいものです。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_AACC")

    label("loc_AA8D")


    #C0645
    ChrTalk(
        0xFE,
        (
            "早く一人前の弁護士になって\x01",
            "先生のお力になりたいものです。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AACC")

    Jump("loc_AB6B")

    label("loc_AAD1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_AADF")
    Jump("loc_AB6B")

    label("loc_AADF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_AB6B")

    #C0646
    ChrTalk(
        0xFE,
        (
            "先生ときたら\x01",
            "昼食をコーヒー一杯で済ませるなんて\x01",
            "不養生にもほどがあります。\x02",
        )
    )

    CloseMessageWindow()

    #C0647
    ChrTalk(
        0xFE,
        (
            "ここは僕がお食事を\x01",
            "用意して差し上げなくちゃ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AB6B")

    TalkEnd(0xFE)
    Return()

    # Function_20_A9B1 end

    def Function_21_AB6F(): pass

    label("Function_21_AB6F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_AB80")
    Jump("loc_AE54")

    label("loc_AB80")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_AC57")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AC05")

    #C0648
    ChrTalk(
        0xFE,
        (
            "主人は朝から事務所で\x01",
            "そわそわしているんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0649
    ChrTalk(
        0xFE,
        (
            "ふふ、主人はあのビルに\x01",
            "ずっと拘っていましたから。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_AC52")

    label("loc_AC05")


    #C0650
    ChrTalk(
        0xFE,
        (
            "主人が朝から\x01",
            "そわそわしているんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0651
    ChrTalk(
        0xFE,
        "ふふ、早く戻ってあげないと。\x02",
    )

    CloseMessageWindow()

    label("loc_AC52")

    Jump("loc_AE54")

    label("loc_AC57")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_AD61")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_ACE7")

    #C0652
    ChrTalk(
        0xFE,
        (
            "あの噂のワンちゃん、\x01",
            "さっきまでタリーズさんの所に\x01",
            "来てたそうなんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0653
    ChrTalk(
        0xFE,
        (
            "残念、私も\x01",
            "会ってみたかったですね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_AD5C")

    label("loc_ACE7")


    #C0654
    ChrTalk(
        0xFE,
        (
            "タリーズさんによると\x01",
            "ときどき来ているそうなんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0655
    ChrTalk(
        0xFE,
        (
            "ふふ、明日は\x01",
            "もう少し早い時間に\x01",
            "お邪魔してみようかな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AD5C")

    Jump("loc_AE54")

    label("loc_AD61")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_AE54")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_ADF6")

    #C0656
    ChrTalk(
        0xFE,
        (
            "表でモモちゃんに挨拶したんですけど、\x01",
            "もじもじした上に逃げてしまいました。\x02",
        )
    )

    CloseMessageWindow()

    #C0657
    ChrTalk(
        0xFE,
        (
            "モモちゃん、\x01",
            "いつも奥手なんですよね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_AE54")

    label("loc_ADF6")


    #C0658
    ChrTalk(
        0xFE,
        (
            "私も小さい頃は\x01",
            "人付き合いが苦手で……\x02",
        )
    )

    CloseMessageWindow()

    #C0659
    ChrTalk(
        0xFE,
        (
            "モモちゃんには\x01",
            "ついつい声を掛けてしまいます。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AE54")

    TalkEnd(0xFE)
    Return()

    # Function_21_AB6F end

    def Function_22_AE58(): pass

    label("Function_22_AE58")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AEEA")

    #C0660
    ChrTalk(
        0xFE,
        "#1200Fグルルルル…………\x02",
    )

    CloseMessageWindow()

    #C0661
    ChrTalk(
        0x101,
        (
            "#0000Fツァイト、今日は\x01",
            "こんな所にいたのか……\x02",
        )
    )

    CloseMessageWindow()

    #C0662
    ChrTalk(
        0x104,
        "#0300Fちゃっかり人気者だよな、こいつ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_AF08")

    label("loc_AEEA")


    #C0663
    ChrTalk(
        0xFE,
        "#1200Fグルルルル…………\x02",
    )

    CloseMessageWindow()

    label("loc_AF08")

    TalkEnd(0xFE)
    Return()

    # Function_22_AE58 end

    def Function_23_AF0C(): pass

    label("Function_23_AF0C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6D, 4)), scpexpr(EXPR_END)), "loc_B023")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_AF6D")

    #C0664
    ChrTalk(
        0x15,
        (
            "#3600F皆さん、頑張ってくださいね。\x01",
            "私も陰ながら応援してますから。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B01E")

    label("loc_AF6D")


    #C0665
    ChrTalk(
        0x15,
        (
            "#3600F皆さん、頑張ってくださいね。\x01",
            "私も陰ながら応援してますから。\x02",
        )
    )

    CloseMessageWindow()

    #C0666
    ChrTalk(
        0x102,
        (
            "#0100F（応援してくれる人がいると\x01",
            "  励みになるわね……）\x02",
        )
    )

    CloseMessageWindow()

    #C0667
    ChrTalk(
        0x101,
        "#0000F（ああ、しみじみそう思うよ。）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)

    label("loc_B01E")

    Jump("loc_B1FC")

    label("loc_B023")

    OP_63(0x15, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0668
    ChrTalk(
        0x15,
        "#3600Fやあ皆さん……！\x02",
    )

    CloseMessageWindow()

    #C0669
    ChrTalk(
        0x101,
        (
            "#0000Fあれ、ハロルドさん……\x02\x03",

            "もしかして商談ですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0670
    ChrTalk(
        0x15,
        (
            "#3600Fええそうです、\x01",
            "ここのタリーズさんには\x01",
            "お世話になっておりまして。\x02\x03",

            "いくつか商品を\x01",
            "卸させてもらっているんですよ。\x02\x03",

            "皆さんの方は……\x01",
            "例の魔獣の調査ですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0671
    ChrTalk(
        0x103,
        (
            "#0200Fええ、昨日中には\x01",
            "終わらなかったもので。\x02",
        )
    )

    CloseMessageWindow()

    #C0672
    ChrTalk(
        0x104,
        (
            "#0300Fこれからさくっと\x01",
            "マインツまで行ってくる所っす。\x02",
        )
    )

    CloseMessageWindow()

    #C0673
    ChrTalk(
        0x15,
        (
            "#3600Fそれは大変ですね……\x02\x03",

            "どうか頑張ってください。\x01",
            "私も陰ながら応援してますから。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x6D, 4)

    label("loc_B1FC")

    TalkEnd(0xFE)
    Return()

    # Function_23_AF0C end

    def Function_24_B200(): pass

    label("Function_24_B200")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_B3A1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B2C6")

    #C0674
    ChrTalk(
        0xFE,
        "あら、こんにちは。\x02",
    )

    CloseMessageWindow()

    #C0675
    ChrTalk(
        0x101,
        (
            "#0000Fエオリアさん、\x01",
            "こんな所で会うなんて\x01",
            "珍しいですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0676
    ChrTalk(
        0xFE,
        (
            "最近、ここのパンに\x01",
            "はまっちゃってね。\x02",
        )
    )

    CloseMessageWindow()

    #C0677
    ChrTalk(
        0xFE,
        (
            "お昼はいつも\x01",
            "ここで買ってるのよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_B3A1")

    label("loc_B2C6")


    #C0678
    ChrTalk(
        0xFE,
        (
            "そういえば、\x01",
            "さっきリンの先輩らしい人が\x01",
            "ギルドに尋ねてきたの。\x02",
        )
    )

    CloseMessageWindow()

    #C0679
    ChrTalk(
        0xFE,
        (
            "２人で《龍老飯店》に\x01",
            "昼食を取りに行ったけど……\x01",
            "楽しくお話できてるかしら。\x02",
        )
    )

    CloseMessageWindow()

    #C0680
    ChrTalk(
        0xFE,
        (
            "ふふ、かなり久しぶりの再会らしいし、\x01",
            "邪魔しないようにしなきゃね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B3A1")

    TalkEnd(0xFE)
    Return()

    # Function_24_B200 end

    def Function_25_B3A5(): pass

    label("Function_25_B3A5")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B455")
    OP_29(0x46, 0x1, 0xB)

    #C0681
    ChrTalk(
        0x101,
        (
            "#0001F（これで西通りも\x01",
            "  一通り回ったけど……）\x02\x03",

            "#0003F（……みんなの捜索状況は\x01",
            "  どうなってるかな。）\x02",
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

    label("loc_B455")

    Return()

    # Function_25_B3A5 end

    def Function_26_B456(): pass

    label("Function_26_B456")

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
        "#0000F#1Pやあ、オスカー！\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x101, 3, 0, 28)
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0684
    ChrTalk(
        0x8,
        "おっと、ロイドじゃねーか！\x02",
    )

    CloseMessageWindow()

    #C0685
    ChrTalk(
        0x8,
        (
            "ははは！\x01",
            "やっと顔見せやがったなコイツ！\x02",
        )
    )

    CloseMessageWindow()

    #C0686
    ChrTalk(
        0x8,
        (
            "久しぶりだなぁ。\x01",
            "えーと、１年振りだったか？\x02",
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
            "#0006F……あのな。\x01",
            "顔を合わせるのは３年振りだろ？\x02\x03",

            "お前、そういう所は\x01",
            "相変わらず大ざっぱっていうか……\x02",
        )
    )

    CloseMessageWindow()

    #C0688
    ChrTalk(
        0x8,
        (
            "わはは！\x01",
            "何度も手紙でやり取りしてたから\x01",
            "そんなに離れてた気がしなくてなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0689
    ChrTalk(
        0x8,
        (
            "かなり背は伸びたみたいだが\x01",
            "お前、相変わらずの童顔だしよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0690
    ChrTalk(
        0x101,
        "#0011Fむぐっ……\x02",
    )

    CloseMessageWindow()

    #C0691
    ChrTalk(
        0x104,
        "#0300Fははっ。\x02",
    )

    CloseMessageWindow()

    #C0692
    ChrTalk(
        0x102,
        "#0100Fクスクス……\x02",
    )

    CloseMessageWindow()

    #C0693
    ChrTalk(
        0x103,
        (
            "#0200Fどうやらロイドさんの\x01",
            "ご友人みたいですね……？\x02",
        )
    )

    CloseMessageWindow()

    #C0694
    ChrTalk(
        0x8,
        (
            "ああ、俺はオスカー。\x01",
            "このベーカリー《モルジュ》で\x01",
            "見習いパン職人をやってンだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0695
    ChrTalk(
        0x8,
        (
            "あんたらはえーと……\x01",
            "ロイドの同僚ってところか？\x02",
        )
    )

    CloseMessageWindow()

    #C0696
    ChrTalk(
        0x104,
        "#0300Fああ、俺はランディだ。\x02",
    )

    CloseMessageWindow()

    #C0697
    ChrTalk(
        0x102,
        "#0100Fエリィです、よろしく。\x02",
    )

    CloseMessageWindow()

    #C0698
    ChrTalk(
        0x103,
        "#0200F……ティオ・プラトーです。\x02",
    )

    CloseMessageWindow()

    #C0699
    ChrTalk(
        0x8,
        "おう、よろしくな！\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0700
    ChrTalk(
        0x101,
        (
            "#0003F（俺たち別に制服を着てないのに\x01",
            "  このメンツを同僚と見抜くなんて……）\x02\x03",

            "（相変わらず鋭いんだか、\x01",
            "  大ざっぱなんだか……）\x02",
        )
    )

    CloseMessageWindow()

    #C0701
    ChrTalk(
        0x8,
        "なんだなんだ、変な顔しやがって。\x02",
    )

    CloseMessageWindow()

    #C0702
    ChrTalk(
        0x8,
        (
            "そうだロイド。\x01",
            "お前、相変わらず料理はしてんのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0703
    ChrTalk(
        0x101,
        (
            "#0005Fえ、ああ……\x02\x03",

            "#0000Fまあ、叔父さんの家でも\x01",
            "家事は手伝ってたからそれなりかな。\x02",
        )
    )

    CloseMessageWindow()

    #C0704
    ChrTalk(
        0x8,
        (
            "だったら再会の印に\x01",
            "コイツをプレゼントしてやろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0705
    ChrTalk(
        0x8,
        "せいぜい役立ててくれや。\x02",
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
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x2, 1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B0(0xD)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BBE5")

    #C0707
    ChrTalk(
        0x8,
        (
            "それと、せっかくだし……\x01",
            "サンドイッチの作り方を教えてやるか。\x02",
        )
    )

    CloseMessageWindow()

    #C0708
    ChrTalk(
        0x8,
        "簡単だから、練習には最適だと思うぜ。\x02",
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
            "のレシピを教えてもらった。\x02",
        )
    )

    CloseMessageWindow()

    #A0710
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1B5),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "のレシピを覚えた。\x02",
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
            "#0005Fサ、サンキュー。\x02\x03",

            "#0000F……へえ、面白いなこれ。\x01",
            "レシピのバリエーションまで\x01",
            "記録できるのか。\x02",
        )
    )

    CloseMessageWindow()

    #C0712
    ChrTalk(
        0x8,
        (
            "ああ、複数の人間で使えるから\x01",
            "色々と活用できるはずだぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0713
    ChrTalk(
        0x8,
        "あんたらも色々試してみなよ。\x02",
    )

    CloseMessageWindow()
    Jump("loc_BCBA")

    label("loc_BBE5")

    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()

    #C0714
    ChrTalk(
        0x101,
        (
            "#0005Fサ、サンキュー。\x02\x03",

            "#0000F……へえ、面白いなこれ。\x01",
            "レシピのバリエーションまで\x01",
            "記録できるのか。\x02",
        )
    )

    CloseMessageWindow()

    #C0715
    ChrTalk(
        0x8,
        (
            "ああ、複数の人間で使えるから\x01",
            "色々と活用できるはずだぜ。\x01",
            "あんたらも色々試してみなよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BCBA")


    #C0716
    ChrTalk(
        0x102,
        (
            "#0105Fそ、そうですね……\x02\x03",

            "#0104F今までお菓子作りくらいしか\x01",
            "したことなかったけど……\x02\x03",

            "#0100Fランディとティオちゃんはどう？\x02",
        )
    )

    CloseMessageWindow()

    #C0717
    ChrTalk(
        0x104,
        (
            "#0303Fうーん……\x01",
            "煮たり焼いたりするだけの\x01",
            "野外料理なら得意なんだが。\x02",
        )
    )

    CloseMessageWindow()

    #C0718
    ChrTalk(
        0x103,
        (
            "#0200F計量通りに作れるものなら\x01",
            "何とか……\x02",
        )
    )

    CloseMessageWindow()

    #C0719
    ChrTalk(
        0x101,
        (
            "#0000Fはは、その気があるなら\x01",
            "俺の方でも教えるよ。\x02",
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
            "※人々に話しかけたり、特定の場所を調べると、\x01",
            "  料理の『レシピ』を覚えることがあります。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #A0721
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※『レシピ』は『料理手帳』に記録されていきます。\x01",
            "  『料理手帳』を使えば、いつでも\x01",
            "  様々な効力のある料理を作ることができます。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #A0722
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※また、『大成功』料理や、『予想外』料理など、\x01",
            "  一定の確率で完成する料理が変化します。\x01",
            "  （料理に『失敗』してしまうこともあります。）\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #A0723
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※料理に使う『食材』は\x01",
            "  雑貨屋などの商店で販売されています。\x01",
            "  また、魔獣が落とす場合もあります。\x07\x00\x02",
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

    # Function_26_B456 end

    def Function_27_C00A(): pass

    label("Function_27_C00A")

    SetChrPos(0x101, 47500, 0, 0, 90)
    SetChrPos(0x102, 46350, 0, -500, 90)
    SetChrPos(0x103, 46450, 0, 750, 90)
    SetChrPos(0x104, 45250, 0, 250, 90)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_C07F():
        OP_98(0x101, 0x1388, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_C07F)
    Sleep(50)

    def lambda_C09C():
        OP_98(0x103, 0x1388, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_C09C)
    Sleep(50)

    def lambda_C0B9():
        OP_98(0x102, 0x1388, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_C0B9)
    Sleep(50)

    def lambda_C0D6():
        OP_98(0x104, 0x1388, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_C0D6)
    Sleep(500)

    def lambda_C0F3():
        OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_C0F3)
    Sleep(50)

    def lambda_C107():
        OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_C107)
    Sleep(50)

    def lambda_C11B():
        OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_C11B)
    Sleep(50)

    def lambda_C12F():
        OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_C12F)
    WaitChrThread(0x101, 1)
    Return()

    # Function_27_C00A end

    def Function_28_C140(): pass

    label("Function_28_C140")

    OP_68(54000, 1500, 2000, 3000)
    TurnDirection(0x8, 0x101, 500)

    def lambda_C15D():
        OP_95(0x101, 53750, 0, 2000, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_C15D)
    Sleep(210)

    def lambda_C17A():
        OP_95(0x103, 52800, 0, 2750, 1400, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_C17A)
    Sleep(280)

    def lambda_C197():
        OP_95(0x102, 52700, 0, 1500, 1600, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_C197)
    Sleep(140)

    def lambda_C1B4():
        OP_95(0x104, 51500, 0, 2250, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_C1B4)
    Sleep(300)
    TurnDirection(0x8, 0x101, 500)
    WaitChrThread(0x101, 1)

    def lambda_C1DC():
        OP_93(0x101, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_C1DC)
    WaitChrThread(0x103, 1)

    def lambda_C1ED():
        OP_93(0x103, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_C1ED)
    WaitChrThread(0x102, 1)

    def lambda_C1FE():
        OP_93(0x102, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_C1FE)
    WaitChrThread(0x104, 1)

    def lambda_C20F():
        OP_93(0x104, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_C20F)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x104, 1)
    OP_6F(0x1)
    Return()

    # Function_28_C140 end

    def Function_29_C22A(): pass

    label("Function_29_C22A")

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
            "#11Pようロイド、\x01",
            "今日も来やがったか。\x02",
        )
    )

    CloseMessageWindow()

    #C0725
    ChrTalk(
        0x8,
        "#11Pわはは、パンでも食べてくか？\x02",
    )

    CloseMessageWindow()

    #C0726
    ChrTalk(
        0x101,
        (
            "#5P#0006F『パンでも食べてくか』\x01",
            "……じゃないだろ？\x02\x03",

            "#0000Fオスカー、お前支援課に\x01",
            "依頼を出してたじゃないか。\x02",
        )
    )

    CloseMessageWindow()

    #C0727
    ChrTalk(
        0x8,
        "#11Pあれ、そうだったか？\x02",
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
            "#6P#0200F確かに支援課に\x01",
            "依頼が来ていたはずですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0729
    ChrTalk(
        0x101,
        (
            "#5P#0003F頼むぞオスカー……\x01",
            "一応仕事で来てるんだからさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0730
    ChrTalk(
        0x8,
        "#11Pおう、大丈夫だ、今思い出したぜ。\x02",
    )

    CloseMessageWindow()

    #C0731
    ChrTalk(
        0x8,
        (
            "#11Pいやあ新作パンの調理に使う\x01",
            "食材を頼もうと思ってたんだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0732
    ChrTalk(
        0x8,
        (
            "#11P実は頼んでた業者さんの\x01",
            "配達が遅れてるみたいでさ。\x01",
            "不足気味になっちまってなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0733
    ChrTalk(
        0x104,
        (
            "#6P#0300Fなるほど、それで\x01",
            "食材を集めてほしいっつーわけか。\x02",
        )
    )

    CloseMessageWindow()

    #C0734
    ChrTalk(
        0x102,
        (
            "#6P#0100F確かに食材がなくちゃ\x01",
            "パンが作れないわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0735
    ChrTalk(
        0x8,
        (
            "#11Pそういうことだ。\x01",
            "引き受けてくれるか？\x02",
        )
    )

    CloseMessageWindow()

    #C0736
    ChrTalk(
        0x101,
        (
            "#5P#0000Fああ、そういう事なら\x01",
            "任せておいてくれ。\x02\x03",

            "それで……具体的には\x01",
            "どんな食材が足りないんだ？\x02",
        )
    )

    CloseMessageWindow()

    #C0737
    ChrTalk(
        0x8,
        (
            "#11Pそうだな、小麦粉やバターは\x01",
            "何とかなるとして……\x02",
        )
    )

    CloseMessageWindow()

    #C0738
    ChrTalk(
        0x8,
        (
            "#11P集めてきて欲しいのは\x01",
            "『魔獣の魚肉』を４つ、\x01",
            "『魔獣の卵』を３つって所だな。\x02",
        )
    )

    CloseMessageWindow()

    #C0739
    ChrTalk(
        0x104,
        (
            "#6P#0304Fふむ、どれも街道に出りゃあ\x01",
            "楽勝で手に入りそうだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0740
    ChrTalk(
        0x101,
        (
            "#5P#0000F了解、何かのついでに\x01",
            "集めてくるよ。\x02",
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
            "クエスト【食材集めの依頼】\x07\x00",
            "を開始した！\x02",
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

    # Function_29_C22A end

    def Function_30_C80D(): pass

    label("Function_30_C80D")

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
            "#5P#0000Fああ、ご注文どおり\x01",
            "持ってきたよ。\x02",
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
            "×４、\x01",
            scpstr(SCPSTR_CODE_ITEM, 0x12F),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "×３を渡した。\x02",
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
            "#11Pサンキュー、助かったぜ。\x01",
            "やっぱりロイドは\x01",
            "頼りになるなぁ……\x02",
        )
    )

    CloseMessageWindow()

    #C0745
    ChrTalk(
        0x8,
        (
            "#11Pヘヘ、昔から困ったときは\x01",
            "助けてくれるんだよな！\x02",
        )
    )

    CloseMessageWindow()

    #C0746
    ChrTalk(
        0x104,
        (
            "#6P#0309Fはは、やっぱロイドは\x01",
            "昔からそうなのか。\x02",
        )
    )

    CloseMessageWindow()

    #C0747
    ChrTalk(
        0x103,
        (
            "#6P#0200F普段のお人よしぶりから\x01",
            "何となく察してはいましたが。\x02",
        )
    )

    CloseMessageWindow()

    #C0748
    ChrTalk(
        0x102,
        (
            "#5P#0109Fまあまあ……それが\x01",
            "ロイドなんだからいいじゃない。\x02",
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
            "#11P#0003Fあの、何か俺に\x01",
            "不名誉な話になってるのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0750
    ChrTalk(
        0x8,
        (
            "#11Pロイドはいい奴だよなって\x01",
            "話をしてるだけじゃねえか。\x02",
        )
    )

    CloseMessageWindow()

    #C0751
    ChrTalk(
        0x8,
        (
            "#11Pああそうだ、ついでに\x01",
            "オレの焼いたパンでも\x01",
            "食べていけよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0752
    ChrTalk(
        0x8,
        "#11P今日はサービスしとくぜ？\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0x5A, 0x1F4)
    Sleep(300)

    #C0753
    ChrTalk(
        0x101,
        (
            "#5P#0000Fはいはい、\x01",
            "後で選ばせて貰うよ。\x02\x03",

            "じゃあなオスカー。\x01",
            "パン修行の方も頑張れよ！\x02",
        )
    )

    CloseMessageWindow()

    #C0754
    ChrTalk(
        0x8,
        "#11Pおう、任せとけって！\x02",
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
            "クエスト【食材集めの依頼】\x07\x00",
            "を達成した！\x02",
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

    # Function_30_C80D end

    def Function_31_CCAD(): pass

    label("Function_31_CCAD")

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
            "#5P……あなたたち、\x01",
            "オスカーに頼まれて\x01",
            "食材を集めてるそうね。\x02",
        )
    )

    CloseMessageWindow()

    #C0757
    ChrTalk(
        0xA,
        "#5Pずるい……\x02",
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
        "#0005F#11Pえっ……？\x02",
    )

    CloseMessageWindow()

    #C0759
    ChrTalk(
        0xA,
        (
            "#5P私も新作パンの\x01",
            "研究をしてるのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0760
    ChrTalk(
        0xA,
        (
            "#5Pどうしてオスカーの依頼だけ……\x01",
            "ぶつぶつ……\x02",
        )
    )

    CloseMessageWindow()

    #C0761
    ChrTalk(
        0x103,
        (
            "#11P#0200F（この方は\x01",
            "  どうしたのでしょうか。）\x02",
        )
    )

    CloseMessageWindow()

    #C0762
    ChrTalk(
        0x104,
        (
            "#0300F#11P（あっちの兄ちゃんに対抗意識を\x01",
            "  持っちまってるみたいだな。）\x02\x03",

            "（依頼を受けちまったのが\x01",
            "  気に入らないんじゃねえか？）\x02",
        )
    )

    CloseMessageWindow()

    #C0763
    ChrTalk(
        0x101,
        (
            "#0006F#11P（そんな面倒な……）\x02\x03",

            "#0005F（……ってあれ、そういえば。）\x02\x03",

            "#0000Fえっと、食材の配達が遅れてるとか\x01",
            "聞いたけど……\x01",
            "もしかしてそれで困ってるのか？\x02\x03",

            "よかったら\x01",
            "君の分も探してこようか？\x02",
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
        "#5P…………そ、それじゃ………\x02",
    )

    CloseMessageWindow()

    #C0765
    ChrTalk(
        0xA,
        "#5P『魔獣の卵』を２つお願い。\x02",
    )

    CloseMessageWindow()

    #C0766
    ChrTalk(
        0xA,
        (
            "#5P……急ぎで頼むわね。\x01",
            "オスカーより早く\x01",
            "新作を完成させたいんだもの。\x02",
        )
    )

    CloseMessageWindow()

    #C0767
    ChrTalk(
        0x101,
        (
            "#0000F#11Pああ、了解だ。\x01",
            "少し待っていてくれ。\x02",
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
            "#0305F（ロイドの奴、\x01",
            "  あっさりかわしたぞ？）\x02",
        )
    )

    CloseMessageWindow()

    #C0769
    ChrTalk(
        0x102,
        "#0111F#12P（意外と慣れてるわね……）\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 500)
    Sleep(300)

    #C0770
    ChrTalk(
        0x101,
        "#0005F#5Pどうかしたのか？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 500)
    Sleep(300)

    #C0771
    ChrTalk(
        0x103,
        "#11P#0211Fいいえ、別に……\x02",
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

    # Function_31_CCAD end

    def Function_32_D1D8(): pass

    label("Function_32_D1D8")

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
            "#11P#0000Fああ、依頼通り\x01",
            "集めてきたよ。\x02",
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
            "×２を渡した。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    SubItemNumber(0x12F, 2)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D33B")

    #C0774
    ChrTalk(
        0xA,
        "#5P助かったわ、ありがとう。\x02",
    )

    CloseMessageWindow()

    #C0775
    ChrTalk(
        0xA,
        (
            "#5Pふふ……これで\x01",
            "オスカーを出し抜けるわね……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D3F5")

    label("loc_D33B")


    #C0776
    ChrTalk(
        0xA,
        "#5P助かったわ、ありがとう。\x02",
    )

    CloseMessageWindow()

    #C0777
    ChrTalk(
        0xA,
        (
            "#5Pでも……ちょっと遅いじゃない。\x01",
            "早めにお願いって言ったのに、\x01",
            "ぶつぶつ……\x02",
        )
    )

    CloseMessageWindow()

    #C0778
    ChrTalk(
        0xA,
        (
            "#5Pオスカーを出し抜いて\x01",
            "ぎゃふんと言わせてやる\x01",
            "予定なのに……！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x71, 2)

    label("loc_D3F5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6, 0x0, 0x20)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D407")
    OP_2C(0x6, 0x3)

    label("loc_D407")

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
            "#11P#0003F（うーん、困ってるようだから\x01",
            "  つい依頼を受けたけど……）\x02\x03",

            "（これで良かったのかな。）\x02",
        )
    )

    CloseMessageWindow()

    #C0780
    ChrTalk(
        0x104,
        (
            "#11P#0304F（まあ大丈夫だろ。）\x02\x03",

            "#0300F（競い合って\x01",
            "  技術を高めるってのは\x01",
            "  いいことだしな。）\x02",
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

    # Function_32_D1D8 end

    def Function_33_D594(): pass

    label("Function_33_D594")

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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D638")
    SetChrPos(0x10A, 0, 0, 3000, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    label("loc_D638")

    OP_4B(0xF, 0xFF)
    OP_93(0xF, 0xB4, 0x0)
    OP_0D()

    #C0781
    ChrTalk(
        0xF,
        (
            "#5Pやあ、いらっしゃい。\x01",
            "《タリーズ商店》にようこそ。\x02",
        )
    )

    CloseMessageWindow()

    #C0782
    ChrTalk(
        0xF,
        "#5Pなにかお探しかい？\x02",
    )

    CloseMessageWindow()

    #C0783
    ChrTalk(
        0x101,
        (
            "#0000F#12Pえっと……\x01",
            "『リクエム』という花を\x01",
            "探してるんですが。\x02",
        )
    )

    CloseMessageWindow()

    #C0784
    ChrTalk(
        0xF,
        (
            "#5Pあ、もしかして……\x01",
            "クイントさんに頼まれたのかな？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D781")
    OP_63(0x4, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    label("loc_D781")

    Sleep(1000)

    #C0785
    ChrTalk(
        0x101,
        (
            "#12P#0005Fそうですけど……\x01",
            "話が通されてたんですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0786
    ChrTalk(
        0xF,
        (
            "#5Pまぁ、うちでその花を\x01",
            "買ってくのはあの人くらいだしね。\x01",
            "あとは一部の敬虔な人達とか……\x02",
        )
    )

    CloseMessageWindow()

    #C0787
    ChrTalk(
        0xF,
        (
            "#5Pちょっとまってよ、\x01",
            "確かカウンターに在庫が\x01",
            "あったからさ。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xF, 0x0, 0x1F4)

    def lambda_D867():
        OP_98(0xFE, 0x0, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_D867)
    WaitChrThread(0xF, 1)

    def lambda_D885():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_D885)

    #C0788
    ChrTalk(
        0x104,
        (
            "#0306Fはぁ、立て替えるハメに\x01",
            "なるかと思ったぜ。\x02\x03",

            "ミラを渡してくれなかったから\x01",
            "ちょっと心配してたんだよ。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_D900():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_D900)
    Sleep(50)

    def lambda_D910():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_D910)
    Sleep(50)

    def lambda_D920():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_D920)

    #C0789
    ChrTalk(
        0x101,
        (
            "#6P#0000Fうーん、しっかりした\x01",
            "お爺さんだし、そんな事は\x01",
            "しなさそうだったけどな。\x02",
        )
    )

    CloseMessageWindow()

    #C0790
    ChrTalk(
        0x103,
        (
            "#6P#0200Fそれにしたって、\x01",
            "もう少し事情を話してくれても\x01",
            "良かったかと思いますが。\x02",
        )
    )

    CloseMessageWindow()

    #C0791
    ChrTalk(
        0x102,
        (
            "#0100Fそうねぇ……\x01",
            "かなり大まかな花の場所しか\x01",
            "教えてくれなかったし。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xF, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0xF)

    #C0792
    ChrTalk(
        0xF,
        "#5Pう、うーん……\x02",
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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_DAD3")
    OP_63(0x4, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)

    label("loc_DAD3")

    Sleep(1000)

    def lambda_DADB():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_DADB)
    Sleep(50)

    def lambda_DAEB():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_DAEB)
    Sleep(50)

    def lambda_DAFB():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_DAFB)
    Sleep(50)

    def lambda_DB0B():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_DB0B)
    Sleep(50)

    #C0793
    ChrTalk(
        0x101,
        "#12P#0005Fどうかしたんですか？\x02",
    )

    CloseMessageWindow()
    OP_93(0xF, 0xB4, 0x1F4)

    #C0794
    ChrTalk(
        0xF,
        (
            "#5P悪いけど……あの花の\x01",
            "在庫を切らしてるみたいだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0795
    ChrTalk(
        0x101,
        (
            "#12P#0006Fそ、そうですか……\x01",
            "参ったな。\x02",
        )
    )

    CloseMessageWindow()

    #C0796
    ChrTalk(
        0xF,
        (
            "#5Pいや、本当にすまないね。\x01",
            "ちょっと待っててくれるかい？\x02",
        )
    )

    CloseMessageWindow()

    #C0797
    ChrTalk(
        0xF,
        (
            "#5P今から遊撃士に依頼して\x01",
            "花を採ってきてもらうからさ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_DC8A")
    OP_63(0x10A, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    label("loc_DC8A")

    Sleep(1000)

    #C0798
    ChrTalk(
        0x101,
        (
            "#12P#0005Fそうか、普段は遊撃士に\x01",
            "頼んでいるんだな……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_DE73")

    #C0799
    ChrTalk(
        0x10A,
        (
            "#12P#0603F……分かっているとは思うが、\x01",
            "遊撃士を待つヒマなどないぞ。\x02\x03",

            "#0600F片付けるアテがないのなら、\x01",
            "今すぐにでもルバーチェの捜査に\x01",
            "戻ってもらう。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_DD76():
        TurnDirection(0xFE, 0x10A, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_DD76)
    Sleep(50)

    def lambda_DD86():
        TurnDirection(0xFE, 0x10A, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_DD86)
    Sleep(50)

    def lambda_DD96():
        TurnDirection(0xFE, 0x10A, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_DD96)
    Sleep(50)

    def lambda_DDA6():
        TurnDirection(0xFE, 0x10A, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_DDA6)
    Sleep(50)

    #C0800
    ChrTalk(
        0x101,
        (
            "#6P#0012Fで、ですよね。\x02\x03",

            "#0003F（でも、それなら……）\x02",
        )
    )

    CloseMessageWindow()

    def lambda_DDF1():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_DDF1)

    #C0801
    ChrTalk(
        0x102,
        (
            "#0101F……ねぇロイド。\x01",
            "せっかくだし、花は私たちで\x01",
            "取りに行かない？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x10A, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0802
    ChrTalk(
        0x10A,
        "#12P#0605Fなっ……\x02",
    )

    CloseMessageWindow()
    Jump("loc_DEC6")

    label("loc_DE73")


    def lambda_DE78():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_DE78)

    #C0803
    ChrTalk(
        0x102,
        (
            "#0101Fねぇロイド……\x01",
            "せっかくだし、花は私たちで\x01",
            "取りに行かない？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DEC6")


    def lambda_DECB():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_DECB)
    Sleep(50)

    def lambda_DEDB():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_DEDB)
    Sleep(50)

    #C0804
    ChrTalk(
        0x104,
        (
            "#0300Fおお、そうだぜ。\x01",
            "遊撃士に負けてられるかっての。\x02",
        )
    )

    CloseMessageWindow()

    #C0805
    ChrTalk(
        0x103,
        "#6P#0200F同感です。\x02",
    )

    CloseMessageWindow()

    def lambda_DF3F():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_DF3F)

    #C0806
    ChrTalk(
        0x101,
        (
            "#6P#0000Fああ、俺もそう思っていた所だ。\x02\x03",

            "仕事の効率的にも、遊撃士を待つより\x01",
            "そっちの方がいいだろう。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_DFB6():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_DFB6)
    Sleep(50)

    def lambda_DFC6():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_DFC6)
    Sleep(50)

    def lambda_DFD6():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_DFD6)
    Sleep(50)

    def lambda_DFE6():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_DFE6)
    Sleep(50)

    #C0807
    ChrTalk(
        0x101,
        (
            "#12P#0000Fあの、リクエムの花っていうのは\x01",
            "どこに咲いているんですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0808
    ChrTalk(
        0xF,
        (
            "#5Pああ、自分たちで\x01",
            "行くつもりなのかい？\x02",
        )
    )

    CloseMessageWindow()

    #C0809
    ChrTalk(
        0xF,
        (
            "#5Pリクエムの花は、マインツ山道の\x01",
            "外れに咲いているんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0810
    ChrTalk(
        0xF,
        (
            "#5P山道のトンネルから\x01",
            "遺跡の方に向かう分かれ道の\x01",
            "途中にあると思うよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0811
    ChrTalk(
        0x101,
        (
            "#12P#0000Fなるほど、わかりました。\x01",
            "ちょっと探してみます。\x02",
        )
    )

    CloseMessageWindow()

    #C0812
    ChrTalk(
        0xF,
        (
            "#5P悪いね。\x01",
            "クイントさんにもあとで\x01",
            "謝っといてくれよ。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E1C6")

    #C0813
    ChrTalk(
        0x10A,
        (
            "#12P#0606F（……急かすつもりが\x01",
            "　余計なことを言ってしまったらしい。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E1C6")

    OP_29(0x2E, 0x1, 0x3)
    OP_4C(0xF, 0xFF)
    SetChrPos(0x0, 0, 0, 5400, 0)
    SetChrPos(0xF, 200, 0, 8500, 180)
    EventEnd(0x5)
    Return()

    # Function_33_D594 end

    SaveToFile()

Try(main)
