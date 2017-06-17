from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c0210.bin",                # FileName
        "c0210",                    # MapName
        "c0210",                    # Location
        0x000B,                     # MapIndex
        "ed7150",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 11, 0, 2, 0, 3],
    )

    BuildStringList((
        "c0210",                  # 0
        "オスカー",               # 1
        "モルジュ",               # 2
        "ベネット",               # 3
        "カテリーナ",             # 4
        "チルル",                 # 5
        "タリーズ",               # 6
        "エルサ",                 # 7
        "モモ",                   # 8
        "ピート",                 # 9
    ))

    AddCharChip((
        "chr/ch07000.itc",                   # 00
        "chr/ch25000.itc",                   # 01
        "chr/ch34300.itc",                   # 02
        "chr/ch24500.itc",                   # 03
        "chr/ch20500.itc",                   # 04
        "chr/ch00000.itc",                   # 05
        "chr/ch24800.itc",                   # 06
        "chr/ch10400.itc",                   # 07
        "chr/ch20700.itc",                   # 08
        "chr/ch22200.itc",                   # 09
    ))

    DeclNpc(56290,   0,       2019,    270,  261,  0x0, 0,   0,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(119120,  0,       -660,    275,  261,  0x0, 0,   1,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(51279,   1000,    12869,   90,   261,  0x0, 0,   2,   0,   0,   0,   0,   15,  255,  0)
    DeclNpc(58540,   0,       -2329,   0,    261,  0x0, 0,   3,   0,   0,   0,   0,   17,  255,  0)
    DeclNpc(57799,   0,       -2200,   0,    389,  0x0, 0,   4,   0,   0,   0,   0,   19,  255,  0)
    DeclNpc(200,     0,       8500,    180,  261,  0x0, 0,   6,   0,   0,   0,   0,   21,  255,  0)
    DeclNpc(3089,    0,       4199,    90,   261,  0x0, 0,   7,   0,   0,   0,   0,   22,  255,  0)
    DeclNpc(3089,    0,       4199,    90,   261,  0x0, 0,   8,   0,   0,   0,   0,   24,  255,  0)
    DeclNpc(2589,    0,       1830,    90,   389,  0x0, 0,   9,   0,   0,   0,   0,   25,  255,  0)

    DeclActor(54900,   0,       1720,    1000,    56290,   1500,    2020,    0x007E, 0,  5,  0x0000)
    DeclActor(300,     0,       6960,    1000,    200,     1500,    8500,    0x007E, 0,  20, 0x0000)
    DeclActor(-72380,  0,       8250,    1200,    -72380,  2450,    8250,    0x007C, 0,  4,  0x0000)

    ChipFrameInfo(668, 0)                                        # 0

    ScpFunction((
        "Function_0_29C",          # 00, 0
        "Function_1_34C",          # 01, 1
        "Function_2_377",          # 02, 2
        "Function_3_662",          # 03, 3
        "Function_4_6BF",          # 04, 4
        "Function_5_772",          # 05, 5
        "Function_6_78C",          # 06, 6
        "Function_7_8F1",          # 07, 7
        "Function_8_2114",         # 08, 8
        "Function_9_24A4",         # 09, 9
        "Function_10_2586",        # 0A, 10
        "Function_11_2677",        # 0B, 11
        "Function_12_2759",        # 0C, 12
        "Function_13_3759",        # 0D, 13
        "Function_14_384B",        # 0E, 14
        "Function_15_3B1C",        # 0F, 15
        "Function_16_49BD",        # 10, 16
        "Function_17_4BDA",        # 11, 17
        "Function_18_5719",        # 12, 18
        "Function_19_57E1",        # 13, 19
        "Function_20_5872",        # 14, 20
        "Function_21_5876",        # 15, 21
        "Function_22_67B1",        # 16, 22
        "Function_23_6EFF",        # 17, 23
        "Function_24_7009",        # 18, 24
        "Function_25_73BB",        # 19, 25
        "Function_26_7AAE",        # 1A, 26
        "Function_27_905F",        # 1B, 27
        "Function_28_9537",        # 1C, 28
        "Function_29_A5B7",        # 1D, 29
    ))


    def Function_0_29C(): pass

    label("Function_0_29C")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_2D4"),
        (1, "loc_2E0"),
        (2, "loc_2EC"),
        (3, "loc_2F8"),
        (4, "loc_304"),
        (5, "loc_310"),
        (6, "loc_31C"),
        (SWITCH_DEFAULT, "loc_328"),
    )


    label("loc_2D4")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_334")

    label("loc_2E0")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_334")

    label("loc_2EC")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_334")

    label("loc_2F8")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_334")

    label("loc_304")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_334")

    label("loc_310")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_334")

    label("loc_31C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_334")

    label("loc_328")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_334")

    label("loc_334")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_34B")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_334")

    label("loc_34B")

    Return()

    # Function_0_29C end

    def Function_1_34C(): pass

    label("Function_1_34C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_376")
    OP_94(0xFE, 0xFFFFF308, 0x438, 0x7ED, 0x10B8, 0x3E8)
    Sleep(300)
    Jump("Function_1_34C")

    label("loc_376")

    Return()

    # Function_1_34C end

    def Function_2_377(): pass

    label("Function_2_377")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_39B")
    SetChrPos(0xE, -65370, 0, 2009, 90)
    SetChrFlags(0xF, 0x80)
    Jump("loc_652")

    label("loc_39B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_3E6")
    SetChrFlags(0xB, 0x80)
    SetChrPos(0xA, 123090, 0, 580, 90)
    SetChrPos(0xE, -68850, 0, -980, 0)
    SetChrPos(0xF, -68700, 0, 340, 180)
    ClearChrFlags(0x10, 0x80)
    Jump("loc_652")

    label("loc_3E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_405")
    SetChrPos(0xE, -65370, 0, 2009, 90)
    Jump("loc_652")

    label("loc_405")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_440")
    SetChrFlags(0x8, 0x80)
    SetChrPos(0xA, 56290, 0, 2020, 270)
    SetChrPos(0xE, -65370, 0, 2009, 90)
    BeginChrThread(0xF, 0, 0, 1)
    Jump("loc_652")

    label("loc_440")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_45D")
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    Jump("loc_652")

    label("loc_45D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_4A8")
    SetChrPos(0xA, 51280, 1000, 12870, 180)
    SetChrFlags(0xA, 0x10)
    SetChrPos(0xE, -65370, 0, 2009, 90)
    SetChrPos(0xF, 51240, 1000, 11020, 0)
    SetChrFlags(0xF, 0x10)
    Jump("loc_652")

    label("loc_4A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_4C5")
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    Jump("loc_652")

    label("loc_4C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_522")
    SetChrPos(0x9, 51280, 1000, 12870, 90)
    SetChrPos(0xA, 119120, 0, -660, 275)
    SetChrFlags(0xA, 0x10)
    ClearChrFlags(0xC, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_513")
    SetChrFlags(0xB, 0x10)
    SetChrFlags(0xC, 0x10)

    label("loc_513")

    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    Jump("loc_652")

    label("loc_522")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_535")
    SetChrFlags(0xE, 0x80)
    Jump("loc_652")

    label("loc_535")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_548")
    SetChrFlags(0xF, 0x80)
    Jump("loc_652")

    label("loc_548")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_58C")
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0xB, 0x80)
    SetChrPos(0xE, -68850, 0, -980, 0)
    SetChrFlags(0xE, 0x10)
    SetChrPos(0xF, -68700, 0, 340, 180)
    SetChrFlags(0xF, 0x10)
    Jump("loc_652")

    label("loc_58C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_5A4")
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    Jump("loc_652")

    label("loc_5A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_5E3")
    SetChrPos(0x9, 51280, 1000, 12870, 90)
    SetChrPos(0xA, 119120, 0, -660, 275)
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    Jump("loc_652")

    label("loc_5E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_63F")
    SetChrPos(0xE, -65370, 0, 2009, 90)
    SetChrPos(0xA, 52620, 0, 4250, 90)
    SetChrPos(0xF, 53630, 0, 4250, 270)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6B, 0x0, 0x10)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_63A")
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0xF, 0x10)

    label("loc_63A")

    Jump("loc_652")

    label("loc_63F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_652")
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)

    label("loc_652")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_661")
    ClearScenarioFlags(0x22, 0)
    Event(0, 27)

    label("loc_661")

    Return()

    # Function_2_377 end

    def Function_3_662(): pass

    label("Function_3_662")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_695")
    SetMapObjFrame(0xFF, "hikari_add", 0x0, 0x1)
    Sound(128, 1, 50, 0)

    label("loc_695")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6BE")
    OP_7D(0xD2, 0xD2, 0xE6, 0x0, 0x0)
    SetMapObjFrame(0xFF, "hikari_add", 0x0, 0x1)

    label("loc_6BE")

    Return()

    # Function_3_662 end

    def Function_4_6BF(): pass

    label("Function_4_6BF")

    SetChrName("")

    #A0001
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "『お菓子の王国　第一巻』がある。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x2, 0x0)"), scpexpr(EXPR_END)), "loc_76E")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B2(0x13)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_76E")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0002
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "『ミックスジェラート』\x07\x00",
            "のレシピを覚えた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_76E")

    TalkEnd(0xFF)
    Return()

    # Function_4_6BF end

    def Function_5_772(): pass

    label("Function_5_772")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_788")
    Call(0, 13)
    Jump("loc_78B")

    label("loc_788")

    Call(0, 6)

    label("loc_78B")

    Return()

    # Function_5_772 end

    def Function_6_78C(): pass

    label("Function_6_78C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7C8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_7C3")
    Call(0, 28)
    Return()

    label("loc_7C3")

    Jump("loc_7ED")

    label("loc_7C8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6B, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6B, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6B, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7ED")
    Call(0, 26)
    Return()

    label("loc_7ED")

    TalkBegin(0x8)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7FA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8ED")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_858")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_858")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8B8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_877")
    OP_AF(0xCC)
    Jump("loc_8A9")

    label("loc_877")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_887")
    OP_AF(0xCB)
    Jump("loc_8A9")

    label("loc_887")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_897")
    OP_AF(0xCA)
    Jump("loc_8A9")

    label("loc_897")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_8A7")
    OP_AF(0xC9)
    Jump("loc_8A9")

    label("loc_8A7")

    OP_AF(0xC8)

    label("loc_8A9")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8E8")

    label("loc_8B8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8CC")
    Jump("loc_8E8")

    label("loc_8CC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8E8")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 7)

    label("loc_8E8")

    Jump("loc_7FA")

    label("loc_8ED")

    TalkEnd(0x8)
    Return()

    # Function_6_78C end

    def Function_7_8F1(): pass

    label("Function_7_8F1")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12C, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_90C")
    Call(0, 8)
    Jump("loc_2113")

    label("loc_90C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12C, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_927")
    Call(0, 9)
    Jump("loc_2113")

    label("loc_927")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12C, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_942")
    Call(0, 10)
    Jump("loc_2113")

    label("loc_942")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12C, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_95D")
    Call(0, 11)
    Jump("loc_2113")

    label("loc_95D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_A0E")

    #C0003
    ChrTalk(
        0x8,
        (
            "さっきの『しっとりカツサンド』は\x01",
            "試作品で、店頭には並んでないんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x8,
        (
            "俺的にはベネットのパンを\x01",
            "お勧めしたかったんだが……\x01",
            "やれやれ、女ってのは分からんね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2113")

    label("loc_A0E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_D75")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BD, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BF3")

    #C0005
    ChrTalk(
        0x8,
        "おう、よく来たな！\x02",
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x8,
        (
            "今回は、お前たちの為に\x01",
            "特別な新作パンを作ったんだ。\x01",
            "ほら、持ってってくれ！\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0007
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x214),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x214, 1)
    SetMessageWindowPos(14, 280, 60, 3)

    #C0008
    ChrTalk(
        0x101,
        "#00002Fへえ、すごくいい匂いがするな。\x02",
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x102,
        "#00109Fええ、とっても美味しそう♪\x02",
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x8,
        (
            "はは、だろ？\x01",
            "ここ最近で一番の出来なんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x8,
        (
            "お前たちも色々と大変だろうけど、\x01",
            "そいつを食ってこの事態を\x01",
            "がんばって乗り越えていこうぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x101,
        (
            "#00000Fああ……そうだな。\x01",
            "ありがとう、オスカー。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1BD, 4)
    Jump("loc_D70")

    label("loc_BF3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CD6")

    #C0013
    ChrTalk(
        0x8,
        (
            "こんな時だし、\x01",
            "色んな人にウチのパンを\x01",
            "食べてもらいたいんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x8,
        (
            "俺は美味いパンを作る\x01",
            "くらいしかできねえけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x8,
        (
            "食べたお客さんが少しでも\x01",
            "不安な気持ちを晴らしてくれたら\x01",
            "それ以上のことはないからな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_D70")

    label("loc_CD6")


    #C0016
    ChrTalk(
        0x8,
        (
            "どんなときでも、\x01",
            "美味いパンを作り続けるのが\x01",
            "俺たちの仕事だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x8,
        (
            "ウチのパンを食べたお客さんが\x01",
            "少しでも幸せになってくれたら\x01",
            "それ以上のことはないぜ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D70")

    Jump("loc_2113")

    label("loc_D75")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_FD6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BD, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F67")
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0018
    ChrTalk(
        0x8,
        "お前……ロイドか！？\x02",
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x101,
        (
            "#00000Fオスカー……\x01",
            "よかった、無事だったみたいだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x8,
        (
            "おお、俺たちはなんともないが……\x01",
            "お前たちは大丈夫だったのかよ？\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x8,
        (
            "ていうかロイド、お前って\x01",
            "指名手配されてたんじゃ……\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x101,
        (
            "#00006Fあ、ああ……\x01",
            "話すと長くなるんだが。\x02\x03",

            "#00000Fとにかく、オスカーたちは\x01",
            "このまま屋内から出ないように\x01",
            "注意していてくれ。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x8,
        (
            "うーん……\x01",
            "なんだかよく分かんねえが、\x01",
            "とりあえず了解だぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x8,
        (
            "ロイド、お前たちも\x01",
            "気をつけていくんだぞ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1BD, 3)
    Jump("loc_FD1")

    label("loc_F67")


    #C0025
    ChrTalk(
        0x8,
        (
            "なんだかよく分かんねえが、\x01",
            "お前達が無事で安心したぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x8,
        (
            "ロイド、お前たちも\x01",
            "気をつけていくんだぞ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FD1")

    Jump("loc_2113")

    label("loc_FD6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_1182")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10E6")

    #C0027
    ChrTalk(
        0x8,
        (
            "鉄道便が止まっちまって、\x01",
            "備蓄してたパンの材料が\x01",
            "足りなくなりそうなんだってよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x8,
        (
            "とはいえ、アルモリカ村があるし\x01",
            "食材を外国から仕入れなくても\x01",
            "意外となんとかなりそうだよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x8,
        (
            "ま、俺はどんな状況になっても\x01",
            "美味いパンを作り続けるだけさ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_117D")

    label("loc_10E6")


    #C0030
    ChrTalk(
        0x8,
        (
            "アルモリカ村があるし\x01",
            "食材を外国から仕入れなくても\x01",
            "意外となんとかなりそうだよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x8,
        (
            "ま、俺はどんな状況になっても\x01",
            "美味いパンを作り続けるだけさ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_117D")

    Jump("loc_2113")

    label("loc_1182")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1190")
    Jump("loc_2113")

    label("loc_1190")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_12B0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1258")

    #C0032
    ChrTalk(
        0x8,
        (
            "今日は朝っぱらから、\x01",
            "来るお客さんたちが騒いでてよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x8,
        (
            "どうやら昨日の夜辺りから\x01",
            "鉱山方面でドンパチやってるらしい。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x8,
        (
            "物騒だよな……\x01",
            "これ以上何もないといいんだが。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_12AB")

    label("loc_1258")


    #C0035
    ChrTalk(
        0x8,
        (
            "鉱山方面でドンパチなんざ、\x01",
            "物騒だよな……\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x8,
        "これ以上何もないといいんだが。\x02",
    )

    CloseMessageWindow()

    label("loc_12AB")

    Jump("loc_2113")

    label("loc_12B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_13F3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1377")

    #C0037
    ChrTalk(
        0x8,
        (
            "ベネットはなかなか\x01",
            "面倒見がいいんだよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x8,
        (
            "俺がパン作りのことを聞いても、\x01",
            "ぶつくさ言いながら\x01",
            "ちゃんと教えてくれるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x8,
        (
            "ああ見えて、\x01",
            "根は優しい奴なんだよな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_13EE")

    label("loc_1377")


    #C0040
    ChrTalk(
        0x8,
        (
            "さて、お前らもなにか\x01",
            "買っていってくれるか？\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x8,
        (
            "雨の日だからこそ、\x01",
            "焼きたてふわふわのパンを\x01",
            "召し上がってくれよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13EE")

    Jump("loc_2113")

    label("loc_13F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_15FB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14C6")

    #C0042
    ChrTalk(
        0x8,
        (
            "ベネットの奴、厨房で\x01",
            "一心不乱に小麦をこねてて、\x01",
            "腕を痛めちまったんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x8,
        (
            "丁度湿布があったから\x01",
            "貼ってやったんだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x8,
        (
            "がんばりすぎもよくないし、\x01",
            "俺がちゃんと見てないとな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_154F")

    label("loc_14C6")


    #C0045
    ChrTalk(
        0x8,
        (
            "まあ、がんばり屋なのが\x01",
            "ベネットのいいところでも\x01",
            "あるんだけどな。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x8,
        (
            "がんばりすぎて体を壊さないように、\x01",
            "俺がちゃんと見てないとな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_154F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_15F6")

    #C0047
    ChrTalk(
        0x101,
        (
            "#00008F（ここでグルメガイドの取材が\x01",
            "  出来そうだけど……）\x02\x03",

            "#00003F（今はそれどころじゃない。\x01",
            "  後で忘れずに来るとしよう。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15F6")

    Jump("loc_2113")

    label("loc_15FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_175A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16D2")

    #C0048
    ChrTalk(
        0x8,
        (
            "ベネットの新作パン、\x01",
            "売り上げが好調でな。\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x8,
        (
            "でも、その事を褒めたら\x01",
            "『あんたには負けないから！』とか\x01",
            "ぷりぷりしながら言うんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x8,
        (
            "うーん、俺ってもしかして\x01",
            "嫌われてんのかな……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1755")

    label("loc_16D2")


    #C0051
    ChrTalk(
        0x8,
        (
            "なにか悪い事を言ったなら、\x01",
            "あとで謝らないとな。\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x8,
        (
            "ベネットとはこれからも\x01",
            "力を合わせて美味いパン作りを\x01",
            "していきたいからな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1755")

    Jump("loc_2113")

    label("loc_175A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1880")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1804")

    #C0053
    ChrTalk(
        0x8,
        (
            "ベネットの新作パンは\x01",
            "俺も試食させてもらったけど、\x01",
            "マジでほっぺが落ちそうだったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x8,
        (
            "いやあ、さすがベネットだ。\x01",
            "俺も負けてらんねえな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_187B")

    label("loc_1804")


    #C0055
    ChrTalk(
        0x8,
        (
            "最近、ベネットは\x01",
            "本当に美味いパンを\x01",
            "作るようになったんだよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x8,
        (
            "さすが、親方の娘だぜ。\x01",
            "俺も負けてらんねえな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_187B")

    Jump("loc_2113")

    label("loc_1880")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_19FD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_196A")

    #C0057
    ChrTalk(
        0x8,
        (
            "早朝から、記者さんたちが\x01",
            "大勢詰め掛けてきたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x8,
        (
            "いつもは、早朝のお客さんは\x01",
            "サラリーマンやビジネスマンが\x01",
            "多いんだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x8,
        (
            "へへ、忙しい人たちが\x01",
            "気軽に食べられるのも、\x01",
            "パンの魅力のひとつだよな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_19F8")

    label("loc_196A")


    #C0060
    ChrTalk(
        0x8,
        (
            "忙しい人たちが\x01",
            "気軽に食べられるのも、\x01",
            "パンの魅力のひとつだよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x8,
        (
            "今朝の記者さんたちも\x01",
            "ウチのパンを食べて、\x01",
            "一日がんばってほしいぜ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19F8")

    Jump("loc_2113")

    label("loc_19FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_1BC2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B59")

    #C0062
    ChrTalk(
        0x8,
        (
            "こんな時間に\x01",
            "ウロウロしてるなんて\x01",
            "珍しいじゃないか。\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x8,
        (
            "一応、閉店時間は\x01",
            "過ぎちまってんだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x8,
        (
            "ま、おまえらならいいだろ。\x01",
            "遠慮せず見てってくれ。\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x101,
        (
            "#00000Fサンキュー、オスカー。\x01",
            "是非そうさせてもら……\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x10A,
        "#00603F…………………………\x02",
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x101,
        (
            "#00006F（か、買い物するにしても\x01",
            "  早く済ませた方がよさそうだな。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1BBD")

    label("loc_1B59")


    #C0068
    ChrTalk(
        0x8,
        (
            "一応、閉店時間は\x01",
            "過ぎちまってんだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x8,
        (
            "ま、おまえらならいいだろ。\x01",
            "遠慮せず見てってくれ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BBD")

    Jump("loc_2113")

    label("loc_1BC2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1E20")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D87")

    #C0070
    ChrTalk(
        0x8,
        (
            "この間、女の子から\x01",
            "『あなたのファンです』……\x01",
            "とかいう手紙をもらったんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x8,
        (
            "うーん、俺は別に\x01",
            "アルカンシェルのアーティスト\x01",
            "とかじゃねえんだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0x8,
        (
            "もしかして出す相手を\x01",
            "間違えちまったのかな。\x01",
            "今度来たら返してやらねえと。\x02",
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

    #C0073
    ChrTalk(
        0x101,
        (
            "#00006Fさ、さすがに返すのは\x01",
            "どうかと思うぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x8,
        (
            "んー、そうなのか？\x01",
            "よく分かんねえな……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1E1B")

    label("loc_1D87")


    #C0075
    ChrTalk(
        0x8,
        (
            "それにしても……\x01",
            "手紙をもらったときは、\x01",
            "ベネットの様子が変だったな。\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x8,
        (
            "内容について\x01",
            "やたらと聞いてくるし……\x01",
            "そんなに読みたかったのかねえ？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E1B")

    Jump("loc_2113")

    label("loc_1E20")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1FA8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F24")

    #C0077
    ChrTalk(
        0x8,
        (
            "近頃、ベネットが前以上に\x01",
            "美味いパンを作るようになってな。\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0x8,
        (
            "毎日、閉店時間をすぎてからも\x01",
            "ずっと厨房にこもって\x01",
            "練習してるみたいだし……\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0x8,
        (
            "うーん、こうしちゃいらんねえ。\x01",
            "ベネットに負けないように、\x01",
            "俺ももっと練習しないとな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1FA3")

    label("loc_1F24")


    #C0080
    ChrTalk(
        0x8,
        (
            "ベネットに負けないように、\x01",
            "俺ももっと練習しないとな。\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0x8,
        (
            "そうだ、折角だし一緒に\x01",
            "練習させてくれねえか\x01",
            "頼んでみようかな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1FA3")

    Jump("loc_2113")

    label("loc_1FA8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_2089")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6B, 0x0, 0x2)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2084")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6B, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_203E")

    #C0082
    ChrTalk(
        0x8,
        (
            "メイリンちゃんは、\x01",
            "東通りのモルス爺さんちの\x01",
            "孫娘だったはずだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x8,
        (
            "すまないが、\x01",
            "後はよろしく頼むぜ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2083")

    label("loc_203E")


    #C0084
    ChrTalk(
        0x8,
        "おかげさまで助かったよ。\x02",
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0x8,
        (
            "やっぱお前らは\x01",
            "頼りになるよな～。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2083")

    Return()

    label("loc_2084")

    Jump("loc_2113")

    label("loc_2089")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_2113")

    #C0086
    ChrTalk(
        0x8,
        (
            "最近は、前以上に\x01",
            "色々な新作パンに挑戦していてな。\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x8,
        (
            "ときどき試供品をやるから、\x01",
            "気に入ったらたくさん\x01",
            "買ってってくれよな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2113")

    Return()

    # Function_7_8F1 end

    def Function_8_2114(): pass

    label("Function_8_2114")


    #C0088
    ChrTalk(
        0x8,
        "おお、ロイドじゃねえか！\x02",
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0x101,
        (
            "#00000Fやあオスカー、久しぶり。\x01",
            "仕事の調子はどうだ？\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x8,
        (
            "おう、来る日も来る日も\x01",
            "パンを焼いて過ごしてるさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x8,
        (
            "それにしても、\x01",
            "随分顔を見なかったが\x01",
            "どこ行ってやがったんだ？\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0x8,
        (
            "ミシュラムに長期滞在でも\x01",
            "してたのかよ？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0093
    ChrTalk(
        0x101,
        (
            "#00006Fあのな……\x01",
            "そんなわけないだろ？\x02\x03",

            "#00001Fそれに、『研修のために\x01",
            "一度支援課を離れる』って\x01",
            "ちゃんと挨拶したじゃないか。\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x8,
        (
            "あれ、そうだったか？\x01",
            "すっかり忘れちまってたぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0x8,
        (
            "まあいいや、\x01",
            "とりあえず再会の記念に\x01",
            "こいつを受け取ってくれよ。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0096
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x210),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x210, 1)
    SetMessageWindowPos(14, 280, 60, 3)

    #C0097
    ChrTalk(
        0x102,
        (
            "#00105Fこれは……\x01",
            "恒例の新作パンですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x105,
        "#10300Fへえ、いい匂いがするじゃないか。\x02",
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0x109,
        "#10109Fとっても美味しそうです！\x02",
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0x8,
        (
            "ああ、焼きたてほやほやだ、\x01",
            "きっと美味いはずだぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0x8,
        (
            "へへ、気に入ったら\x01",
            "何個でも買っていってくれよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x101,
        (
            "#00000Fありがとう、オスカー。\x01",
            "おいしく頂かせてもらうよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x12C, 0)
    Return()

    # Function_8_2114 end

    def Function_9_24A4(): pass

    label("Function_9_24A4")


    #C0103
    ChrTalk(
        0x8,
        "おう、よく来たな！\x02",
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0x8,
        (
            "今日も新作パンが出来てるぜ。\x01",
            "試しに食べてみてくれよ。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0105
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x211),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x211, 1)
    SetMessageWindowPos(14, 280, 60, 3)

    #C0106
    ChrTalk(
        0x101,
        (
            "#00000Fありがとう、オスカー。\x01",
            "おいしく頂かせてもらうよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x12C, 1)
    Return()

    # Function_9_24A4 end

    def Function_10_2586(): pass

    label("Function_10_2586")


    #C0107
    ChrTalk(
        0x8,
        "おう、よく来たな！\x02",
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0x8,
        (
            "今回の新作パンは、\x01",
            "ベネットの作ったパンだ。\x01",
            "試しに食べてみてくれよ。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0109
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x212),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x212, 1)
    SetMessageWindowPos(14, 280, 60, 3)

    #C0110
    ChrTalk(
        0x101,
        (
            "#00000Fありがとう、オスカー。\x01",
            "おいしく頂かせてもらうよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x12C, 2)
    Return()

    # Function_10_2586 end

    def Function_11_2677(): pass

    label("Function_11_2677")


    #C0111
    ChrTalk(
        0x8,
        "おう、よく来たな！\x02",
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0x8,
        (
            "今日も新作パンが出来てるぜ。\x01",
            "試しに食べてみてくれよ。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0113
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x213),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x213, 1)
    SetMessageWindowPos(14, 280, 60, 3)

    #C0114
    ChrTalk(
        0x101,
        (
            "#00000Fありがとう、オスカー。\x01",
            "おいしく頂かせてもらうよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x12C, 3)
    Return()

    # Function_11_2677 end

    def Function_12_2759(): pass

    label("Function_12_2759")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2908")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_285E")

    #C0115
    ChrTalk(
        0xFE,
        (
            "政府支給の小麦粉なんかじゃ\x01",
            "美味いパンはまともに\x01",
            "作れない所だったが……\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0xFE,
        (
            "交通が復活した今なら\x01",
            "新鮮なアルモリカ産が手に入る。\x01",
            "ようやく元通りになりそうだぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0xFE,
        (
            "オスカーとベネットにも、\x01",
            "今まで以上に頑張ってもらわねえとな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2903")

    label("loc_285E")


    #C0118
    ChrTalk(
        0xFE,
        (
            "交通が復活した今なら\x01",
            "新鮮なアルモリカ産小麦粉が手に入る。\x01",
            "ようやく美味いパンが作れそうだぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0xFE,
        (
            "オスカーとベネットにも、\x01",
            "今まで以上に頑張ってもらわねえとな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2903")

    Jump("loc_3755")

    label("loc_2908")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_2988")

    #C0120
    ChrTalk(
        0xFE,
        (
            "戒厳令で客も来ないし、\x01",
            "ゆっくり新作パンの研究でも\x01",
            "してようと思ってたが……\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0xFE,
        "こりゃ、一体どういう状況だ？\x02",
    )

    CloseMessageWindow()
    Jump("loc_3755")

    label("loc_2988")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_2B27")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A7C")

    #C0122
    ChrTalk(
        0xFE,
        (
            "食材の仕入れに２大国を\x01",
            "頼れなくなっちまったのは、\x01",
            "ちいっとばかし痛ぇな。\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0xFE,
        (
            "なんだかんだいって、\x01",
            "ほとんどのパンの材料は\x01",
            "他国からの輸入だったからな。\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0xFE,
        (
            "しばらくはクロスベル産だけで\x01",
            "やりくりしてくしかねえか。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2B22")

    label("loc_2A7C")


    #C0125
    ChrTalk(
        0xFE,
        (
            "ふむ、しかし……\x01",
            "『クロスベル産を１００％使用』ってのは、\x01",
            "むしろウリになるかもしれねえな。\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0xFE,
        (
            "……まあ、そこまで\x01",
            "ノンキな話じゃないことは\x01",
            "分かってるんだがよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B22")

    Jump("loc_3755")

    label("loc_2B27")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2C8E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2BFE")

    #C0127
    ChrTalk(
        0xFE,
        (
            "復興応援セールを\x01",
            "やってるのはいいものの……\x02",
        )
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0xFE,
        (
            "今日はオスカーがいないから\x01",
            "女性客には申し訳ねえが……\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0xFE,
        (
            "ま、珍しく親子だけで\x01",
            "店をやるんだ、それはそれとして\x01",
            "がんばってかねえとな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2C89")

    label("loc_2BFE")


    #C0130
    ChrTalk(
        0xFE,
        (
            "今日はオスカーがいないから\x01",
            "女性客には申し訳ねえが……\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0xFE,
        (
            "ま、珍しく親子だけで\x01",
            "店をやるんだ、それはそれとして\x01",
            "がんばってかねえとな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C89")

    Jump("loc_3755")

    label("loc_2C8E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_2D0A")

    #C0132
    ChrTalk(
        0xFE,
        (
            "おいおい、鉱山町が\x01",
            "占拠されたそうじゃねえか。\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0xFE,
        (
            "いったいどこのどいつの仕業だ？\x01",
            "許しちゃおけねえぜ……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3755")

    label("loc_2D0A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2E63")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2DD9")

    #C0134
    ChrTalk(
        0xFE,
        (
            "本当なら雨の日の\x01",
            "パン屋ってのは\x01",
            "客足が減るもんだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0xFE,
        (
            "ウチは雨でも来てくれる\x01",
            "お得意様がいっぱいいてな。\x02",
        )
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0xFE,
        (
            "へへ、ありがたいことだぜ。\x01",
            "これも長年続けてきたおかげだな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2E5E")

    label("loc_2DD9")


    #C0137
    ChrTalk(
        0xFE,
        (
            "ウチは雨でも来てくれる\x01",
            "お得意様がいっぱいいるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0xFE,
        (
            "ヘヘ、ありがたいことだぜ。\x01",
            "今度、感謝を込めて\x01",
            "セールでもやろうかねえ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E5E")

    Jump("loc_3755")

    label("loc_2E63")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_2EAC")

    #C0139
    ChrTalk(
        0xFE,
        (
            "表の通りが騒がしいみてえだが……\x01",
            "何かあったのかねえ？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3755")

    label("loc_2EAC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2F35")

    #C0140
    ChrTalk(
        0xFE,
        (
            "ベネットのやつ、\x01",
            "褒められるとどうも\x01",
            "反発しちまうんだよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0xFE,
        (
            "照れちまってんだろうが……\x01",
            "やれやれ、ソンな性格だぜ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3755")

    label("loc_2F35")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3092")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3013")

    #C0142
    ChrTalk(
        0xFE,
        (
            "オスカーの奴が\x01",
            "俺に弟子入りして、\x01",
            "しばらく経つんだよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0xFE,
        (
            "ベネットもオスカーのことを\x01",
            "意識しているようだし……\x02",
        )
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0xFE,
        (
            "へへ、オスカーには\x01",
            "このままウチの婿養子にでも\x01",
            "来てもらうとするかねえ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_308D")

    label("loc_3013")


    #C0145
    ChrTalk(
        0xFE,
        (
            "オスカーには、\x01",
            "ウチの婿養子にでも\x01",
            "来てもらうとするかねえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0xFE,
        (
            "へへ、俺にとっても\x01",
            "跡取り息子ができて\x01",
            "万々歳だしな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_308D")

    Jump("loc_3755")

    label("loc_3092")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3121")

    #C0147
    ChrTalk(
        0xFE,
        (
            "今朝は、通商会議の取材に行く\x01",
            "記者たちで大繁盛だったぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0xFE,
        (
            "あんなに売れるんなら、\x01",
            "もっとたくさん\x01",
            "焼いとけばよかったなあ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3755")

    label("loc_3121")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_31AE")

    #C0149
    ChrTalk(
        0xFE,
        (
            "さーて、そろそろ\x01",
            "後片付けに入るとするか。\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0xFE,
        (
            "パン屋の仕込みは、\x01",
            "早朝３時からなんでな。\x01",
            "明日に備えてさっさと休まねえと。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3755")

    label("loc_31AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3335")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_32A0")

    #C0151
    ChrTalk(
        0xFE,
        (
            "オスカーは、ちょくちょく\x01",
            "ファンレターなんぞを\x01",
            "もらっているみてえだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0xFE,
        (
            "以前雑誌で紹介されてから\x01",
            "ときどきこんな調子なのさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0xFE,
        (
            "おかげで売り上げも好調だし、\x01",
            "オスカーのファンたちは\x01",
            "大事にしていかないとな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3330")

    label("loc_32A0")


    #C0154
    ChrTalk(
        0xFE,
        (
            "店の売り上げのためにも\x01",
            "オスカーのファンたちは\x01",
            "大事にしていかないとな。\x02",
        )
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0xFE,
        (
            "ただ、ベネットが\x01",
            "不機嫌になっちまうのが\x01",
            "玉にキズなんだけどな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3330")

    Jump("loc_3755")

    label("loc_3335")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_347F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_33FB")

    #C0156
    ChrTalk(
        0xFE,
        (
            "やれやれ、ベネットに\x01",
            "厨房から追い出されちまった。\x02",
        )
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0xFE,
        (
            "最近はパン作りに対して\x01",
            "鬼気迫ってる感じなんだよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0xFE,
        (
            "ま、向上心からきてるんだろうし\x01",
            "いいことなんだけどな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_347A")

    label("loc_33FB")


    #C0159
    ChrTalk(
        0xFE,
        (
            "まあ、ぶつぶつと可愛らしい\x01",
            "独り言が聞こえるのは\x01",
            "ご愛嬌だけどな。\x02",
        )
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0xFE,
        (
            "それがモチベーションに\x01",
            "繋がるなら、ある意味ＯＫさ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_347A")

    Jump("loc_3755")

    label("loc_347F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_35F1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_34F5")

    #C0161
    ChrTalk(
        0xFE,
        (
            "お、あんたら……\x01",
            "仕事で来てくれたのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0xFE,
        (
            "詳しくはオスカーたちに\x01",
            "話を聞いてみてくれ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_35EC")

    label("loc_34F5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6B, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_357C")

    #C0163
    ChrTalk(
        0xFE,
        (
            "パンの生地を急ぎで\x01",
            "作んないと、午後の焼きたてに\x01",
            "間に合わねえんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0xFE,
        (
            "悪いが、仕事の件は\x01",
            "よろしく頼んだぜ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_35EC")

    label("loc_357C")


    #C0165
    ChrTalk(
        0xFE,
        (
            "傘、見つかったみてえだな？\x01",
            "へへ、ありがとな。\x02",
        )
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0xFE,
        (
            "さーて、安心したところで\x01",
            "パン作りを再開するとしますか。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_35EC")

    Jump("loc_3755")

    label("loc_35F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_3755")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_36CA")

    #C0167
    ChrTalk(
        0xFE,
        (
            "最近は、新作パンのほとんどは\x01",
            "オスカーとベネット任せなのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0xFE,
        (
            "あいつら、競い合って\x01",
            "どんどん成長してるし、\x01",
            "いいパンを作るようになった。\x02",
        )
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0xFE,
        (
            "そのうち店を任せても\x01",
            "いいかもしれんなあ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3755")

    label("loc_36CA")


    #C0170
    ChrTalk(
        0xFE,
        (
            "特に、娘のベネットの成長は\x01",
            "俺にとってうれしい誤算だぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0xFE,
        (
            "オスカーの存在が\x01",
            "やっぱりでけえんだろうなぁ。\x01",
            "ライバルってのは大事だぜ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3755")

    TalkEnd(0xFE)
    Return()

    # Function_12_2759 end

    def Function_13_3759(): pass

    label("Function_13_3759")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x198, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x198, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x199, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3787")
    Call(0, 29)
    Return()

    label("loc_3787")

    TalkBegin(0xA)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3794")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3847")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_37F2")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_37F2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3812")
    OP_AF(0xCB)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3842")

    label("loc_3812")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3826")
    Jump("loc_3842")

    label("loc_3826")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3842")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 14)

    label("loc_3842")

    Jump("loc_3794")

    label("loc_3847")

    TalkEnd(0xA)
    Return()

    # Function_13_3759 end

    def Function_14_384B(): pass

    label("Function_14_384B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_38D8")

    #C0172
    ChrTalk(
        0xA,
        (
            "悪いけど、ミスコンなんて、\x01",
            "ガラじゃないのよね……\x02",
        )
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0xA,
        (
            "チャリティの料理、\x01",
            "私も手伝ったんだから\x01",
            "それで勘弁してちょうだい。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3B1B")

    label("loc_38D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12C, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_39C0")

    #C0174
    ChrTalk(
        0xA,
        "いらっしゃいませ。\x02",
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0xA,
        (
            "新作パンが出来てるから、\x01",
            "よかったら食べてみてください。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0176
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x213),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x213, 1)
    SetMessageWindowPos(14, 280, 60, 3)

    #C0177
    ChrTalk(
        0x101,
        (
            "#00000Fありがとう、\x01",
            "おいしく頂かせてもらうよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x12C, 3)
    Jump("loc_3B1B")

    label("loc_39C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A99")

    #C0178
    ChrTalk(
        0xA,
        (
            "オスカーは、\x01",
            "チャリティイベントの\x01",
            "手伝いに行ってるの。\x02",
        )
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0xA,
        (
            "私が行ってもよかったけど\x01",
            "まあ、笑顔の素敵なオスカーの方が\x01",
            "みんなに元気を………………\x02",
        )
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0xA,
        (
            "……って、い、今のなし！\x01",
            "忘れてちょうだい。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3B1B")

    label("loc_3A99")


    #C0181
    ChrTalk(
        0xA,
        (
            "ま、まあ……\x01",
            "私は私でお店を守る\x01",
            "使命があるしね。\x02",
        )
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0xA,
        (
            "チャリティのほうは\x01",
            "オスカーに任せたってわけ。\x01",
            "……それだけなんだから。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3B1B")

    Return()

    # Function_14_384B end

    def Function_15_3B1C(): pass

    label("Function_15_3B1C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_3BA2")

    #C0183
    ChrTalk(
        0xFE,
        (
            "オスカーめ……\x01",
            "勝手に私のパンを雑誌に\x01",
            "お勧めしようとするなんて。\x02",
        )
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0xFE,
        (
            "……ふ、ふんっ。\x01",
            "あてつけのつもりかしら。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_49B9")

    label("loc_3BA2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3D3D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3CAD")

    #C0185
    ChrTalk(
        0xFE,
        (
            "私もオスカーに負けないように、\x01",
            "みんなを幸せに出来る新作パンを\x01",
            "たくさん作らなくちゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0xFE,
        (
            "だけど……\x01",
            "私のパンってオスカーのには\x01",
            "まだまだ敵わないのよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0xFE,
        (
            "こうなったら、オスカーに\x01",
            "アドバイスをもらおうかな。\x01",
            "……ちょっと悔しいけど。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3D38")

    label("loc_3CAD")


    #C0188
    ChrTalk(
        0xFE,
        (
            "私のパンってオスカーのには\x01",
            "まだまだ敵わないのよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0xFE,
        (
            "こうなったら、オスカーに\x01",
            "アドバイスをもらおうかな。\x01",
            "……ちょっと悔しいけど。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3D38")

    Jump("loc_49B9")

    label("loc_3D3D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_3E4C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3DE4")

    #C0190
    ChrTalk(
        0xFE,
        "戸締りは一応オッケーと……\x02",
    )

    CloseMessageWindow()

    #C0191
    ChrTalk(
        0xFE,
        (
            "……あの化物は何なの？\x01",
            "私たち市民には襲い掛かって\x01",
            "来るわけでもないし。\x02",
        )
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0xFE,
        "なんだか不気味すぎるわ……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3E47")

    label("loc_3DE4")


    #C0193
    ChrTalk(
        0xFE,
        "外の化物は不気味すぎるわ……\x02",
    )

    CloseMessageWindow()

    #C0194
    ChrTalk(
        0xFE,
        (
            "いくら市民を襲わないからって、\x01",
            "さすがに安心はできないわね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3E47")

    Jump("loc_49B9")

    label("loc_3E4C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_3FC0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F3D")

    #C0195
    ChrTalk(
        0xFE,
        (
            "オスカーも父さんも、\x01",
            "この状況で意外と前向きなのよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0xFE,
        (
            "……本当に大丈夫なのかしら。\x01",
            "いくらアリオスさんでも\x01",
            "さすがに２大国が相手じゃ……\x02",
        )
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0xFE,
        (
            "……まあ、私が心配したところで\x01",
            "どうなるわけでもないんだけどね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3FBB")

    label("loc_3F3D")


    #C0198
    ChrTalk(
        0xFE,
        (
            "いくらアリオスさんでも\x01",
            "さすがに２大国が相手じゃ……\x02",
        )
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0xFE,
        (
            "……まあ、私が心配したところで\x01",
            "どうなるわけでもないんだけどね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3FBB")

    Jump("loc_49B9")

    label("loc_3FC0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3FD5")
    TalkEnd(0xFE)
    Call(0, 13)
    Return()

    label("loc_3FD5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_40E0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_407D")

    #C0200
    ChrTalk(
        0xFE,
        (
            "……そうだ、次の新作には\x01",
            "あのハーブを混ぜ込んで……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xFE, 0x0, 500)

    #C0201
    ChrTalk(
        0xFE,
        (
            "わっ、ごめんなさい！\x01",
            "ちょっと考え事してたの。\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xFE, 0x10)
    SetScenarioFlags(0x0, 2)
    Jump("loc_40DB")

    label("loc_407D")


    #C0202
    ChrTalk(
        0xFE,
        (
            "次の新作パンの\x01",
            "構想を練っていたの。\x02",
        )
    )

    CloseMessageWindow()

    #C0203
    ChrTalk(
        0xFE,
        (
            "え～っと、確かあのハーブは\x01",
            "備蓄があったはず……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_40DB")

    Jump("loc_49B9")

    label("loc_40E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_40F1")
    Call(0, 16)
    Jump("loc_49B9")

    label("loc_40F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_41EF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_418A")

    #C0204
    ChrTalk(
        0xFE,
        "……むう、オスカーめ……\x02",
    )

    CloseMessageWindow()

    #C0205
    ChrTalk(
        0xFE,
        (
            "こんな湿布を貼ったくらいで\x01",
            "機嫌を取れると思ったら\x01",
            "大間違いなんだからね！\x02",
        )
    )

    CloseMessageWindow()

    #C0206
    ChrTalk(
        0xFE,
        "……ふんっ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_41EA")

    label("loc_418A")


    #C0207
    ChrTalk(
        0xFE,
        "オスカーめ……\x02",
    )

    CloseMessageWindow()

    #C0208
    ChrTalk(
        0xFE,
        (
            "こんな湿布を貼ったくらいで\x01",
            "機嫌を取れると思ったら\x01",
            "大間違いなんだから。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_41EA")

    Jump("loc_49B9")

    label("loc_41EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_433D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_42B9")

    #C0209
    ChrTalk(
        0xFE,
        (
            "ぐぬぬ、オスカーめ……\x01",
            "余裕ぶっちゃってもう……！\x02",
        )
    )

    CloseMessageWindow()

    #C0210
    ChrTalk(
        0xFE,
        (
            "……でも、食べたときのあの表情、\x01",
            "ほんとうに美味しそうに……\x02",
        )
    )

    CloseMessageWindow()

    #C0211
    ChrTalk(
        0xFE,
        (
            "……ち、ちがうもん！\x01",
            "うれしくなんかなかったもん！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_4338")

    label("loc_42B9")


    #C0212
    ChrTalk(
        0xFE,
        (
            "邪・念・退・散ッ……！\x01",
            "（こねこねこねこね……）\x02",
        )
    )

    CloseMessageWindow()

    #C0213
    ChrTalk(
        0xFE,
        (
            "オスカー……\x01",
            "次こそは絶～～～～っ対に、\x01",
            "悔しがらせてやるんだからっ！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4338")

    Jump("loc_49B9")

    label("loc_433D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_4473")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_440E")

    #C0214
    ChrTalk(
        0xFE,
        (
            "せっかくオスカーに勝てる\x01",
            "パンが出来上がったのに、\x01",
            "あんなうれしそうに……\x02",
        )
    )

    CloseMessageWindow()

    #C0215
    ChrTalk(
        0xFE,
        (
            "違う、違うの！\x01",
            "私が見たいのはオスカーの\x01",
            "悔しがった顔なのにっ……！\x02",
        )
    )

    CloseMessageWindow()

    #C0216
    ChrTalk(
        0xFE,
        "ううう、オスカーめっ……！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_446E")

    label("loc_440E")


    #C0217
    ChrTalk(
        0xFE,
        (
            "オスカーめっ……\x01",
            "なんで私のパンを食べて\x01",
            "あんなうれしそうに……\x02",
        )
    )

    CloseMessageWindow()

    #C0218
    ChrTalk(
        0xFE,
        "悔しがってよ、もうっ！\x02",
    )

    CloseMessageWindow()

    label("loc_446E")

    Jump("loc_49B9")

    label("loc_4473")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_457B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_450E")

    #C0219
    ChrTalk(
        0xFE,
        (
            "お客さん、私のパンと\x01",
            "オスカーのパンが並んでたら、\x01",
            "だいたいオスカーのをとっていくの。\x02",
        )
    )

    CloseMessageWindow()

    #C0220
    ChrTalk(
        0xFE,
        "うう、何が違うっていうのよ……！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_4576")

    label("loc_450E")


    #C0221
    ChrTalk(
        0xFE,
        (
            "ええい、こうなったら\x01",
            "作るしかないわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0222
    ChrTalk(
        0xFE,
        (
            "《ベネットスペシャル》を超える、\x01",
            "至高のパンをッ……！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4576")

    Jump("loc_49B9")

    label("loc_457B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_45E5")

    #C0223
    ChrTalk(
        0xFE,
        (
            "私の作ったパン、\x01",
            "オスカーのに\x01",
            "売り上げで負けてる……！？\x02",
        )
    )

    CloseMessageWindow()

    #C0224
    ChrTalk(
        0xFE,
        "ぐぬぬ、明日こそは……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_49B9")

    label("loc_45E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_4741")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_46AE")

    #C0225
    ChrTalk(
        0xFE,
        (
            "オスカー、この間は\x01",
            "変な手紙をもらってたみたい。\x02",
        )
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0xFE,
        (
            "もしかして、あれって\x01",
            "ラブレターなんじゃ……！？\x02",
        )
    )

    CloseMessageWindow()

    #C0227
    ChrTalk(
        0xFE,
        (
            "ちょっとパン作りが\x01",
            "私より上手いからって\x01",
            "いい気になっちゃって！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_473C")

    label("loc_46AE")


    #C0228
    ChrTalk(
        0xFE,
        (
            "オスカーに\x01",
            "ラブレターを出すなんて、\x01",
            "どこの誰なのっ……！？\x02",
        )
    )

    CloseMessageWindow()

    #C0229
    ChrTalk(
        0xFE,
        (
            "……あ、えっと、じゃなくて。\x01",
            "そ、そんなのを貰うなんて\x01",
            "オスカーめっ……！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_473C")

    Jump("loc_49B9")

    label("loc_4741")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_47AB")

    #C0230
    ChrTalk(
        0xFE,
        "（こねこね、こねこね）\x02",
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0xFE,
        (
            "ぶつぶつ……\x01",
            "絶対オスカーなんかには\x01",
            "負けないんだから……！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_49B9")

    label("loc_47AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_4885")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6B, 0x0, 0x2)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_484A")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6B, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_480D")

    #C0232
    ChrTalk(
        0xA,
        (
            "傘のことは任せたわね。\x01",
            "この子は私が面倒みるから。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4846")

    label("loc_480D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4822")
    Call(0, 16)
    SetScenarioFlags(0x1, 0)
    Jump("loc_4846")

    label("loc_4822")


    #C0233
    ChrTalk(
        0xA,
        "まったくもう、世話の焼ける……\x02",
    )

    CloseMessageWindow()

    label("loc_4846")

    TalkEnd(0xFE)
    Return()

    label("loc_484A")


    #C0234
    ChrTalk(
        0xA,
        "ほら、泣かないの。\x02",
    )

    CloseMessageWindow()

    #C0235
    ChrTalk(
        0xA,
        "きっと見つかるから、ね？\x02",
    )

    CloseMessageWindow()
    Jump("loc_49B9")

    label("loc_4885")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_49B9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_494D")

    #C0236
    ChrTalk(
        0xFE,
        (
            "いらっしゃいませ、\x01",
            "焼きたてパンはこちらですよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0237
    ChrTalk(
        0xFE,
        (
            "……ほとんどオスカー作なのが\x01",
            "かなりくやしいんだけどね。\x02",
        )
    )

    CloseMessageWindow()

    #C0238
    ChrTalk(
        0xFE,
        (
            "オスカーめ、いつか絶対に\x01",
            "追い越してやるんだから……！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_49B9")

    label("loc_494D")


    #C0239
    ChrTalk(
        0xFE,
        (
            "オスカーめ、\x01",
            "実力だからしょうがないけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0240
    ChrTalk(
        0xFE,
        (
            "今に見てなさいよ、絶対に\x01",
            "追い越してやるんだから……！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_49B9")

    TalkEnd(0xFE)
    Return()

    # Function_15_3B1C end

    def Function_16_49BD(): pass

    label("Function_16_49BD")

    OP_4B(0xA, 0xFF)
    OP_4B(0xF, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4AB5")

    #C0241
    ChrTalk(
        0xA,
        (
            "それじゃ、\x01",
            "タリーズさんちに\x01",
            "送っていくから。\x02",
        )
    )

    CloseMessageWindow()

    #C0242
    ChrTalk(
        0xA,
        (
            "……今度は忘れ物は\x01",
            "ないでしょうね？\x02",
        )
    )

    CloseMessageWindow()

    #C0243
    ChrTalk(
        0xF,
        "あっ……\x02",
    )

    CloseMessageWindow()

    #C0244
    ChrTalk(
        0xF,
        (
            "せっかくの焼きたてが\x01",
            "すっかり冷めちゃってる。\x02",
        )
    )

    CloseMessageWindow()

    #C0245
    ChrTalk(
        0xF,
        "……くすん。\x02",
    )

    CloseMessageWindow()

    #C0246
    ChrTalk(
        0xA,
        (
            "あーもう、\x01",
            "取り替えたげるから泣かないの。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4BD1")

    label("loc_4AB5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4B89")

    #C0247
    ChrTalk(
        0xA,
        "今日もお使いにきたのね？\x02",
    )

    CloseMessageWindow()

    #C0248
    ChrTalk(
        0xA,
        (
            "また傘をなくしたり\x01",
            "しないようにね。\x02",
        )
    )

    CloseMessageWindow()

    #C0249
    ChrTalk(
        0xF,
        (
            "う、うん、だいじょうぶ。\x01",
            "ここに名前といっしょに、\x01",
            "じゅうしょも書いたから……\x02",
        )
    )

    CloseMessageWindow()

    #C0250
    ChrTalk(
        0xA,
        (
            "ふ～ん、なるほど。\x01",
            "それなら安心ね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_4BD1")

    label("loc_4B89")


    #C0251
    ChrTalk(
        0xA,
        (
            "ふふ、あなたなかなか\x01",
            "字がお上手ね。\x02",
        )
    )

    CloseMessageWindow()

    #C0252
    ChrTalk(
        0xF,
        (
            "そ、そうかな。\x01",
            "えへへ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4BD1")

    OP_4C(0xA, 0xFF)
    OP_4C(0xF, 0xFF)
    Return()

    # Function_16_49BD end

    def Function_17_4BDA(): pass

    label("Function_17_4BDA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_4CEA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4C7B")

    #C0253
    ChrTalk(
        0xFE,
        (
            "やっぱりここのパンって\x01",
            "私に合ってるのよね。\x01",
            "食べると元気が出るっていうか。\x02",
        )
    )

    CloseMessageWindow()

    #C0254
    ChrTalk(
        0xFE,
        (
            "うちの家族たちにも\x01",
            "たくさん買って帰ろうっと。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4CE5")

    label("loc_4C7B")


    #C0255
    ChrTalk(
        0xFE,
        (
            "そういえばチルル、\x01",
            "また旅に出るとか言ってたけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0256
    ChrTalk(
        0xFE,
        (
            "大丈夫かしら。\x01",
            "街道ってまだ危ないんじゃ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4CE5")

    Jump("loc_5715")

    label("loc_4CEA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_4CF8")
    Jump("loc_5715")

    label("loc_4CF8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_4DB4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4D82")

    #C0257
    ChrTalk(
        0xFE,
        (
            "チルルも、\x01",
            "家に戻ってきてたみたい。\x02",
        )
    )

    CloseMessageWindow()

    #C0258
    ChrTalk(
        0xFE,
        (
            "これからどうなるか\x01",
            "わかんないもの、\x01",
            "家族と一緒にいるべきよね……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4DAF")

    label("loc_4D82")


    #C0259
    ChrTalk(
        0xFE,
        (
            "私も今日は寄り道しないで\x01",
            "帰ろうかな……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4DAF")

    Jump("loc_5715")

    label("loc_4DB4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_4E34")

    #C0260
    ChrTalk(
        0xFE,
        (
            "今日は復興応援セールとかで、\x01",
            "一部のパンが半額になってるの。\x02",
        )
    )

    CloseMessageWindow()

    #C0261
    ChrTalk(
        0xFE,
        (
            "せっかくだから、\x01",
            "私も沢山買っていこうかな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5715")

    label("loc_4E34")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_4EB4")

    #C0262
    ChrTalk(
        0xFE,
        (
            "今日はお母さんが、\x01",
            "早く帰ってきなさいって言うのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0263
    ChrTalk(
        0xFE,
        (
            "あんな事件が起こってるんだもん、\x01",
            "仕方ないわよね……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5715")

    label("loc_4EB4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_4F4C")

    #C0264
    ChrTalk(
        0xFE,
        (
            "そういえば……\x01",
            "アルカンシェルの公演って\x01",
            "明日じゃなかったかしら。\x02",
        )
    )

    CloseMessageWindow()

    #C0265
    ChrTalk(
        0xFE,
        (
            "うーん、見たいなあ。\x01",
            "噂の新人ってどんな演技を\x01",
            "するのかしら……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5715")

    label("loc_4F4C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_4F5A")
    Jump("loc_5715")

    label("loc_4F5A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_4FF4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4F75")
    Call(0, 18)
    Jump("loc_4FEF")

    label("loc_4F75")


    #C0266
    ChrTalk(
        0xFE,
        (
            "……あれ、なんだかお店の奥から\x01",
            "ベネットさんの声が……？\x02",
        )
    )

    CloseMessageWindow()

    #C0267
    ChrTalk(
        0xFE,
        (
            "ふふ、新作パンも人気みたいだし\x01",
            "張り切っているみたいね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4FEF")

    Jump("loc_5715")

    label("loc_4FF4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_5197")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_511C")

    #C0268
    ChrTalk(
        0xFE,
        (
            "むむっ、今回の新作パンは\x01",
            "ベネットさんが作ったのね。\x02",
        )
    )

    CloseMessageWindow()

    #C0269
    ChrTalk(
        0xFE,
        (
            "ふんわりコッペパンに\x01",
            "イチゴと生クリームを挟んでて、\x01",
            "たまらなくおいしそう……！\x02",
        )
    )

    CloseMessageWindow()

    #C0270
    ChrTalk(
        0xFE,
        (
            "贅沢なトッピングと具材が\x01",
            "特徴的だった前作とは対照的に、\x01",
            "とってもかわいらしいパンね。\x02",
        )
    )

    CloseMessageWindow()

    #C0271
    ChrTalk(
        0xFE,
        "うーん、これは是非食べないとね！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_5192")

    label("loc_511C")


    #C0272
    ChrTalk(
        0xFE,
        (
            "今回の新作パンは\x01",
            "ベネットさんが作ったみたい。\x02",
        )
    )

    CloseMessageWindow()

    #C0273
    ChrTalk(
        0xFE,
        (
            "とってもかわいらしいパン……\x01",
            "うーん、これは是非食べないとね！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5192")

    Jump("loc_5715")

    label("loc_5197")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_51E9")

    #C0274
    ChrTalk(
        0xFE,
        (
            "あーん、お気に入りの\x01",
            "モーニングブレッドが\x01",
            "売り切れてるよ～……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5715")

    label("loc_51E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_51F7")
    Jump("loc_5715")

    label("loc_51F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_5326")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_52B7")

    #C0275
    ChrTalk(
        0xFE,
        (
            "そういえばチルル、\x01",
            "この間旅から戻ってたそうなの。\x02",
        )
    )

    CloseMessageWindow()

    #C0276
    ChrTalk(
        0xFE,
        (
            "まったく、帰ったら帰ったで\x01",
            "連絡してくれればいいのに。\x02",
        )
    )

    CloseMessageWindow()

    #C0277
    ChrTalk(
        0xFE,
        (
            "せっかくだから\x01",
            "一緒にお茶とかしたかったなー。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_5321")

    label("loc_52B7")


    #C0278
    ChrTalk(
        0xFE,
        (
            "あの子ったら、ほんと家に\x01",
            "いつかないのよねー。\x02",
        )
    )

    CloseMessageWindow()

    #C0279
    ChrTalk(
        0xFE,
        (
            "戻ってきてる間に、\x01",
            "一緒にお茶とかしたかったなー。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5321")

    Jump("loc_5715")

    label("loc_5326")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_5459")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_53FD")

    #C0280
    ChrTalk(
        0xFE,
        (
            "あっ、今回の新作パン……\x01",
            "とってもおいしそうね。\x02",
        )
    )

    CloseMessageWindow()

    #C0281
    ChrTalk(
        0xFE,
        (
            "しっとりしたメロンパンの中に\x01",
            "カスタードクリームが\x01",
            "ギッシリ入ってて……\x02",
        )
    )

    CloseMessageWindow()

    #C0282
    ChrTalk(
        0xFE,
        (
            "ちょっと太りそうだけど……\x01",
            "うん、気にせず買おうっと。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_5454")

    label("loc_53FD")


    #C0283
    ChrTalk(
        0xFE,
        (
            "こんなおいしそうな新作パン、\x01",
            "食べないとソンよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0284
    ChrTalk(
        0xFE,
        "いくつか買って帰ろうっと。\x02",
    )

    CloseMessageWindow()

    label("loc_5454")

    Jump("loc_5715")

    label("loc_5459")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_55DA")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6B, 0x0, 0x2)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_558A")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6B, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_551C")

    #C0285
    ChrTalk(
        0xFE,
        (
            "言われてみれば確かに、\x01",
            "もう一組兄妹が来てた……\x01",
            "ような気がするわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0286
    ChrTalk(
        0xFE,
        (
            "あのモモって子と\x01",
            "同じくらいの歳っぽかったし\x01",
            "間違えてもおかしくないかも……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5586")

    label("loc_551C")


    #C0287
    ChrTalk(
        0xFE,
        (
            "ふふ、傘が見つかって\x01",
            "ほんとによかったわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0288
    ChrTalk(
        0xFE,
        (
            "さーて、わたしもパンを買って\x01",
            "おうちに帰ろうかしら。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5586")

    TalkEnd(0xFE)
    Return()

    label("loc_558A")


    #C0289
    ChrTalk(
        0xFE,
        (
            "あの泣いてる子、\x01",
            "そこの商店の娘さんよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0290
    ChrTalk(
        0xFE,
        "何があったのかしら……\x02",
    )

    CloseMessageWindow()
    Jump("loc_5715")

    label("loc_55DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_5715")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_568E")

    #C0291
    ChrTalk(
        0xFE,
        "今回の新作パンはと……\x02",
    )

    CloseMessageWindow()

    #C0292
    ChrTalk(
        0xFE,
        (
            "満月みたいな目玉焼きを\x01",
            "はさんだマフィン……\x01",
            "あ～ん、おいしそう！\x02",
        )
    )

    CloseMessageWindow()

    #C0293
    ChrTalk(
        0xFE,
        (
            "ふふ、この新作パンを買って、\x01",
            "お茶して帰ろうっと。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_5715")

    label("loc_568E")


    #C0294
    ChrTalk(
        0xFE,
        (
            "このお店に通い始めてから、\x01",
            "新作パンのチェックが\x01",
            "日課になっちゃったのよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0295
    ChrTalk(
        0xFE,
        (
            "ふふ、この新作パンを買って、\x01",
            "お茶して帰ろうっと。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5715")

    TalkEnd(0xFE)
    Return()

    # Function_17_4BDA end

    def Function_18_5719(): pass

    label("Function_18_5719")

    OP_4B(0xC, 0xFF)
    OP_4B(0xB, 0xFF)

    #C0296
    ChrTalk(
        0xB,
        "チルル、どのパンが好き？\x02",
    )

    CloseMessageWindow()

    #C0297
    ChrTalk(
        0xB,
        (
            "ちなみに、あたしのオススメは\x01",
            "この新作パンね。\x02",
        )
    )

    CloseMessageWindow()

    #C0298
    ChrTalk(
        0xC,
        (
            "……それじゃあ、\x01",
            "これにしようかな。\x01",
            "なんだかカワイイし。\x02",
        )
    )

    CloseMessageWindow()

    #C0299
    ChrTalk(
        0xB,
        "でしょ、でしょ～？\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xB, 0x10)
    ClearChrFlags(0xC, 0x10)
    SetScenarioFlags(0x0, 3)
    SetScenarioFlags(0x0, 4)
    OP_4C(0xC, 0xFF)
    OP_4C(0xB, 0xFF)
    Return()

    # Function_18_5719 end

    def Function_19_57E1(): pass

    label("Function_19_57E1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_57F2")
    Jump("loc_586E")

    label("loc_57F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_586E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_580D")
    Call(0, 18)
    Jump("loc_586E")

    label("loc_580D")


    #C0300
    ChrTalk(
        0xFE,
        (
            "旅に出るときは、いつもここで\x01",
            "お弁当を買っていくの。\x02",
        )
    )

    CloseMessageWindow()

    #C0301
    ChrTalk(
        0xFE,
        "それにしても、このパンは可愛い……\x02",
    )

    CloseMessageWindow()

    label("loc_586E")

    TalkEnd(0xFE)
    Return()

    # Function_19_57E1 end

    def Function_20_5872(): pass

    label("Function_20_5872")

    Call(0, 21)
    Return()

    # Function_20_5872 end

    def Function_21_5876(): pass

    label("Function_21_5876")

    TalkBegin(0xD)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5883")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_67AD")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_58E1")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_58E1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5991")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_5900")
    OP_AF(0x31)
    Jump("loc_5982")

    label("loc_5900")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_5910")
    OP_AF(0x30)
    Jump("loc_5982")

    label("loc_5910")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_5920")
    OP_AF(0x2F)
    Jump("loc_5982")

    label("loc_5920")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_5930")
    OP_AF(0x2E)
    Jump("loc_5982")

    label("loc_5930")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_5940")
    OP_AF(0x2D)
    Jump("loc_5982")

    label("loc_5940")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_5950")
    OP_AF(0x2C)
    Jump("loc_5982")

    label("loc_5950")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_5960")
    OP_AF(0x2B)
    Jump("loc_5982")

    label("loc_5960")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_5970")
    OP_AF(0x2A)
    Jump("loc_5982")

    label("loc_5970")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_5980")
    OP_AF(0x29)
    Jump("loc_5982")

    label("loc_5980")

    OP_AF(0x28)

    label("loc_5982")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_67A8")

    label("loc_5991")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_59A5")
    Jump("loc_67A8")

    label("loc_59A5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_67A8")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_5B6D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5ABD")

    #C0302
    ChrTalk(
        0xD,
        (
            "貿易できない状況が依然続いていて、\x01",
            "満足に商品を取り揃えられない事情は\x01",
            "確かにあるけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0303
    ChrTalk(
        0xD,
        (
            "ひとまずは元のクロスベルの姿に\x01",
            "戻っていってるようで安心したよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0304
    ChrTalk(
        0xD,
        (
            "家族みんなで安心して暮らせるように\x01",
            "僕も頑張らなくっちゃね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_5B68")

    label("loc_5ABD")


    #C0305
    ChrTalk(
        0xD,
        (
            "依然貿易できない苦しさはあるけど……\x01",
            "ひとまずは元のクロスベルの姿に\x01",
            "戻っていってるようで安心したよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0306
    ChrTalk(
        0xD,
        (
            "家族みんなで安心して暮らせるように\x01",
            "僕も頑張らなくっちゃね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5B68")

    Jump("loc_67A8")

    label("loc_5B6D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_5C16")

    #C0307
    ChrTalk(
        0xD,
        (
            "い、いったい何なんだろう、\x01",
            "あの中世の鎧みたいな化物は……\x02",
        )
    )

    CloseMessageWindow()

    #C0308
    ChrTalk(
        0xD,
        (
            "と、とにかく、こんな時でも\x01",
            "店に来てくれたんだし……\x01",
            "欲しいものがあるなら言ってくれよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_67A8")

    label("loc_5C16")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_5D43")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5CD9")

    #C0309
    ChrTalk(
        0xD,
        (
            "ディーターさんの演説を聞くと、\x01",
            "独立も仕方ないと思えてくるよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0310
    ChrTalk(
        0xD,
        (
            "この先、どんな危険が\x01",
            "あるかわからないけど……\x01",
            "モモとエルサは、\x01",
            "なんとしても僕が守らなくちゃね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_5D3E")

    label("loc_5CD9")


    #C0311
    ChrTalk(
        0xD,
        (
            "この先、どんな危険が\x01",
            "あるかわからないけど……\x01",
            "モモとエルサは、\x01",
            "なんとしても僕が守らなくちゃね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5D3E")

    Jump("loc_67A8")

    label("loc_5D43")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_5DCA")

    #C0312
    ChrTalk(
        0xD,
        (
            "やあいらっしゃい、\x01",
            "タリーズ商店へようこそ。\x02",
        )
    )

    CloseMessageWindow()

    #C0313
    ChrTalk(
        0xD,
        (
            "生活必需品を中心に\x01",
            "セールを行ってるから、\x01",
            "よかったら見ていってよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_67A8")

    label("loc_5DCA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_5F11")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5E91")

    #C0314
    ChrTalk(
        0xD,
        (
            "例のマインツの事件……\x01",
            "帝国が裏で糸を引いている\x01",
            "なんて噂もあるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0315
    ChrTalk(
        0xD,
        (
            "何の罪もない一般人を\x01",
            "巻き込むなんて……\x02",
        )
    )

    CloseMessageWindow()

    #C0316
    ChrTalk(
        0xD,
        (
            "もし噂が本当だとしたら、\x01",
            "僕は帝国を許せないよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_5F0C")

    label("loc_5E91")


    #C0317
    ChrTalk(
        0xD,
        (
            "もしかしたら、\x01",
            "標的になっていたのは\x01",
            "この場所だったかもしれない。\x02",
        )
    )

    CloseMessageWindow()

    #C0318
    ChrTalk(
        0xD,
        (
            "もし噂が本当だとしたら、\x01",
            "僕は帝国を許せないよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5F0C")

    Jump("loc_67A8")

    label("loc_5F11")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_5FBF")

    #C0319
    ChrTalk(
        0xD,
        (
            "昨日の脱線事故、\x01",
            "けが人も出たらしいけど\x01",
            "なんとか復旧したみたいだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0320
    ChrTalk(
        0xD,
        (
            "仕入れを鉄道便に頼っている\x01",
            "ところも多いだろうし、\x01",
            "みんな安心したんじゃないかな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_67A8")

    label("loc_5FBF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_60EF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6080")

    #C0321
    ChrTalk(
        0xD,
        (
            "救急車の音がして、\x01",
            "あわてて店を飛び出したけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0322
    ChrTalk(
        0xD,
        (
            "ふう……\x01",
            "モモじゃなかったようで\x01",
            "ちょっと安心したよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0323
    ChrTalk(
        0xD,
        (
            "しかし、あんな何台も……\x01",
            "一体何があったのかな？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_60EA")

    label("loc_6080")


    #C0324
    ChrTalk(
        0xD,
        (
            "救急車が何台も\x01",
            "通っているようだし……\x02",
        )
    )

    CloseMessageWindow()

    #C0325
    ChrTalk(
        0xD,
        (
            "通りで遊んでいる子供たちに\x01",
            "注意しておくように言わないと。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_60EA")

    Jump("loc_67A8")

    label("loc_60EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_616D")

    #C0326
    ChrTalk(
        0xD,
        (
            "今日はモモたちは、\x01",
            "そこの通りで遊んでるみたいだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0327
    ChrTalk(
        0xD,
        (
            "最近は交通量も増えてるし、\x01",
            "車に気をつけてほしいね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_67A8")

    label("loc_616D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_62A3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6234")

    #C0328
    ChrTalk(
        0xD,
        (
            "帝国や共和国から\x01",
            "クロスベルが独立するのは\x01",
            "いい事だと思うよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0329
    ChrTalk(
        0xD,
        (
            "だけど、独立すれば\x01",
            "２つの大国を敵に回すことに\x01",
            "なってしまうだろうし……\x02",
        )
    )

    CloseMessageWindow()

    #C0330
    ChrTalk(
        0xD,
        "うーん、難しい問題だな。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_629E")

    label("loc_6234")


    #C0331
    ChrTalk(
        0xD,
        (
            "クロスベルが独立するのは\x01",
            "いい事だと思うけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0332
    ChrTalk(
        0xD,
        (
            "帝国や共和国を敵に回すのは\x01",
            "やっぱり怖いよね……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_629E")

    Jump("loc_67A8")

    label("loc_62A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_6329")

    #C0333
    ChrTalk(
        0xD,
        (
            "次のクロスベルタイムズも\x01",
            "通商会議の話題が一面だろうね。\x02",
        )
    )

    CloseMessageWindow()

    #C0334
    ChrTalk(
        0xD,
        (
            "売り上げも見込めそうだし、\x01",
            "多めに入荷しておこうかな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_67A8")

    label("loc_6329")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_63A2")

    #C0335
    ChrTalk(
        0xD,
        (
            "おやいらっしゃい、\x01",
            "何か入用かい？\x02",
        )
    )

    CloseMessageWindow()

    #C0336
    ChrTalk(
        0xD,
        (
            "店はもう少し\x01",
            "開けてるつもりだから、\x01",
            "ゆっくりしてていいからね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_67A8")

    label("loc_63A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_64EE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6466")

    #C0337
    ChrTalk(
        0xD,
        (
            "今日はオルキスタワーの\x01",
            "お披露目だったんだよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0338
    ChrTalk(
        0xD,
        (
            "うーん、店を休みにしてでも\x01",
            "見に行きたかったなあ。\x02",
        )
    )

    CloseMessageWindow()

    #C0339
    ChrTalk(
        0xD,
        (
            "ふふ、巨大な建物や乗り物は\x01",
            "男の子の永遠の憧れだからね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_64E9")

    label("loc_6466")


    #C0340
    ChrTalk(
        0xD,
        (
            "オルキスタワーのような\x01",
            "巨大な建物や乗り物は、\x01",
            "男の子の永遠の憧れだからね。\x02",
        )
    )

    CloseMessageWindow()

    #C0341
    ChrTalk(
        0xD,
        (
            "いくつになっても\x01",
            "ときめいてしまうものなのさ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_64E9")

    Jump("loc_67A8")

    label("loc_64EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_664A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_65C6")

    #C0342
    ChrTalk(
        0xD,
        (
            "市内でよく\x01",
            "警察の人を見かけるよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0343
    ChrTalk(
        0xD,
        (
            "通商会議で各国の\x01",
            "お偉方が来るそうだし、\x01",
            "それに備えてるみたいだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0344
    ChrTalk(
        0xD,
        (
            "僕も、モモが何かの事件に\x01",
            "巻き込まれたら困るし、\x01",
            "是非がんばってほしいね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_6645")

    label("loc_65C6")


    #C0345
    ChrTalk(
        0xD,
        (
            "警察が、市内で警戒を\x01",
            "強めているみたいだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0346
    ChrTalk(
        0xD,
        (
            "僕も、モモが何かの事件に\x01",
            "巻き込まれたら困るし、\x01",
            "是非がんばってほしいね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6645")

    Jump("loc_67A8")

    label("loc_664A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_672D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_66F5")

    #C0347
    ChrTalk(
        0xD,
        (
            "モモが今日、パン屋へ\x01",
            "お使いに行っているのさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0348
    ChrTalk(
        0xD,
        (
            "でも……\x01",
            "随分帰りが遅いなあ。\x02",
        )
    )

    CloseMessageWindow()

    #C0349
    ChrTalk(
        0xD,
        (
            "頼んだパンが何か\x01",
            "分からなくなって\x01",
            "しまったのかな……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_6728")

    label("loc_66F5")


    #C0350
    ChrTalk(
        0xD,
        (
            "モモ、随分帰りが遅いなあ。\x01",
            "何かあったのかな？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6728")

    Jump("loc_67A8")

    label("loc_672D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_67A8")

    #C0351
    ChrTalk(
        0xD,
        (
            "やあ、いらっしゃい。\x01",
            "《タリーズ商店》にようこそ。\x02",
        )
    )

    CloseMessageWindow()

    #C0352
    ChrTalk(
        0xD,
        (
            "日用品ならウチにお任せあれ。\x01",
            "気軽に利用していってね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_67A8")

    Jump("loc_5883")

    label("loc_67AD")

    TalkEnd(0xD)
    Return()

    # Function_21_5876 end

    def Function_22_67B1(): pass

    label("Function_22_67B1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_695F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_68B5")

    #C0353
    ChrTalk(
        0xFE,
        (
            "モモったら、友達と一緒に\x01",
            "街のみんなのために何かしたいって\x01",
            "飛び出していっちゃったの。\x02",
        )
    )

    CloseMessageWindow()

    #C0354
    ChrTalk(
        0xFE,
        (
            "モモがあんなふうに一所懸命に\x01",
            "意思を主張したのって初めてよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0355
    ChrTalk(
        0xFE,
        (
            "外で遊ばせるのはまだ心配だけど……\x01",
            "今はモモの気持ちを尊重したいかな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_695A")

    label("loc_68B5")


    #C0356
    ChrTalk(
        0xFE,
        (
            "モモったら、友達と一緒に\x01",
            "街のみんなのために何かしたいって\x01",
            "飛び出していっちゃったの。\x02",
        )
    )

    CloseMessageWindow()

    #C0357
    ChrTalk(
        0xFE,
        (
            "外で遊ばせるのはまだ心配だけど……\x01",
            "今はモモの気持ちを尊重したいかな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_695A")

    Jump("loc_6EFB")

    label("loc_695F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_69D9")

    #C0358
    ChrTalk(
        0xFE,
        (
            "まさかあんなものが\x01",
            "街の中に現れるなんて……\x02",
        )
    )

    CloseMessageWindow()

    #C0359
    ChrTalk(
        0xFE,
        (
            "これが大統領の出した\x01",
            "戒厳令の意味だったのかしら……？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6EFB")

    label("loc_69D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_6B2C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6AAC")

    #C0360
    ChrTalk(
        0xFE,
        (
            "これからクロスベルの情勢は\x01",
            "不安定になっていきそうね……\x02",
        )
    )

    CloseMessageWindow()

    #C0361
    ChrTalk(
        0xFE,
        (
            "モモには悪いけど……\x01",
            "やっぱり、しばらくは\x01",
            "外で遊ばせられないわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0362
    ChrTalk(
        0xFE,
        (
            "目の届くところにいないと\x01",
            "不安で仕方ないわ……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_6B27")

    label("loc_6AAC")


    #C0363
    ChrTalk(
        0xFE,
        (
            "モモには悪いけど……\x01",
            "やっぱり、しばらくは\x01",
            "外で遊ばせられないわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0364
    ChrTalk(
        0xFE,
        (
            "目の届くところにいないと\x01",
            "不安で仕方ないわ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6B27")

    Jump("loc_6EFB")

    label("loc_6B2C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_6BBA")

    #C0365
    ChrTalk(
        0xFE,
        (
            "……モモを外で遊ばせるのが\x01",
            "すっかり怖くなってしまったわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0366
    ChrTalk(
        0xFE,
        (
            "あれから一週間も経つんだし、\x01",
            "大丈夫だと思いたいんだけど……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6EFB")

    label("loc_6BBA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_6BC8")
    Jump("loc_6EFB")

    label("loc_6BC8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_6C33")

    #C0367
    ChrTalk(
        0xFE,
        (
            "今日はビーフシチューに添える\x01",
            "バゲットをモモに頼んだの。\x02",
        )
    )

    CloseMessageWindow()

    #C0368
    ChrTalk(
        0xFE,
        "早く帰ってこないかしら……\x02",
    )

    CloseMessageWindow()
    Jump("loc_6EFB")

    label("loc_6C33")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_6C41")
    Jump("loc_6EFB")

    label("loc_6C41")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_6C4F")
    Jump("loc_6EFB")

    label("loc_6C4F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_6C5D")
    Jump("loc_6EFB")

    label("loc_6C5D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_6D70")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6D2B")

    #C0369
    ChrTalk(
        0xFE,
        (
            "モモ、今日もリュウくんたちと\x01",
            "遊びに行っているのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0370
    ChrTalk(
        0xFE,
        (
            "あの子は引っ込み思案だったけど、\x01",
            "最近はそれもなくなってきたみたい。\x02",
        )
    )

    CloseMessageWindow()

    #C0371
    ChrTalk(
        0xFE,
        (
            "ふふ、リュウくんたちには\x01",
            "感謝しなくちゃね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_6D6B")

    label("loc_6D2B")


    #C0372
    ChrTalk(
        0xFE,
        (
            "さてと、モモは今日も\x01",
            "おなかをすかせて\x01",
            "帰ってくるかしらね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6D6B")

    Jump("loc_6EFB")

    label("loc_6D70")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_6DCC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6D90")
    Call(0, 23)
    ClearChrFlags(0xE, 0x10)
    Jump("loc_6DC7")

    label("loc_6D90")


    #C0373
    ChrTalk(
        0xFE,
        (
            "ふふ、モモったらよっぽど\x01",
            "楽しかったんでしょうね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6DC7")

    Jump("loc_6EFB")

    label("loc_6DCC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_6DDA")
    Jump("loc_6EFB")

    label("loc_6DDA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_6DE8")
    Jump("loc_6EFB")

    label("loc_6DE8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_6EF2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6E7F")

    #C0374
    ChrTalk(
        0xFE,
        (
            "モモったら、雨なのに\x01",
            "ウキウキして\x01",
            "お使いに行ったのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0375
    ChrTalk(
        0xFE,
        (
            "ふふ、お父さんに\x01",
            "買ってもらった傘を\x01",
            "使いたかったみたいね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_6EED")

    label("loc_6E7F")


    #C0376
    ChrTalk(
        0xFE,
        (
            "モモの傘は、お父さんが\x01",
            "買ってあげたものなの。\x02",
        )
    )

    CloseMessageWindow()

    #C0377
    ChrTalk(
        0xFE,
        (
            "モモの好きなピンク色で、\x01",
            "とても気に入ってるみたいね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6EED")

    Jump("loc_6EFB")

    label("loc_6EF2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_6EFB")

    label("loc_6EFB")

    TalkEnd(0xFE)
    Return()

    # Function_22_67B1 end

    def Function_23_6EFF(): pass

    label("Function_23_6EFF")

    OP_4B(0xE, 0xFF)
    OP_4B(0xF, 0xFF)

    #C0378
    ChrTalk(
        0xF,
        (
            "……それでね、それでね。\x01",
            "リュウ君、オルキスタワーに\x01",
            "かってに入ろうとしたの。\x02",
        )
    )

    CloseMessageWindow()

    #C0379
    ChrTalk(
        0xF,
        (
            "そしたら、モモとアンリちゃんまで\x01",
            "警察の人におこられちゃって……\x02",
        )
    )

    CloseMessageWindow()

    #C0380
    ChrTalk(
        0xE,
        (
            "あらあら……\x01",
            "それは大変だったわねえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0381
    ChrTalk(
        0xF,
        (
            "でもね、でもね。\x01",
            "とっても楽しかったの……！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    SetScenarioFlags(0x0, 7)
    OP_4C(0xE, 0xFF)
    OP_4C(0xF, 0xFF)
    Return()

    # Function_23_6EFF end

    def Function_24_7009(): pass

    label("Function_24_7009")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_701A")
    Jump("loc_73B7")

    label("loc_701A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_7068")

    #C0382
    ChrTalk(
        0xFE,
        "ううっ、お外コワイ……\x02",
    )

    CloseMessageWindow()

    #C0383
    ChrTalk(
        0xFE,
        "リュウくんたち、大丈夫かな……\x02",
    )

    CloseMessageWindow()
    Jump("loc_73B7")

    label("loc_7068")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_70D2")

    #C0384
    ChrTalk(
        0xFE,
        (
            "ママもパパも、\x01",
            "すごく不安そうなの……\x02",
        )
    )

    CloseMessageWindow()

    #C0385
    ChrTalk(
        0xFE,
        (
            "モモも、なんだか\x01",
            "不安になってきちゃった……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_73B7")

    label("loc_70D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_7149")

    #C0386
    ChrTalk(
        0xFE,
        (
            "最近、お外に\x01",
            "遊びに行こうとすると\x01",
            "ママに止められちゃうの……\x02",
        )
    )

    CloseMessageWindow()

    #C0387
    ChrTalk(
        0xFE,
        (
            "リュウ君たちと\x01",
            "遊びたいのにな……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_73B7")

    label("loc_7149")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_7157")
    Jump("loc_73B7")

    label("loc_7157")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_7168")
    Call(0, 16)
    Jump("loc_73B7")

    label("loc_7168")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_7176")
    Jump("loc_73B7")

    label("loc_7176")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_7184")
    Jump("loc_73B7")

    label("loc_7184")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_71F3")

    #C0388
    ChrTalk(
        0xFE,
        "今日はお店の手伝いなの……\x02",
    )

    CloseMessageWindow()

    #C0389
    ChrTalk(
        0xFE,
        (
            "遊んでばかりじゃダメだよね。\x01",
            "ちゃんとお手伝いもしないと……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_73B7")

    label("loc_71F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_7201")
    Jump("loc_73B7")

    label("loc_7201")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_72BB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_721C")
    Call(0, 23)
    Jump("loc_72B6")

    label("loc_721C")


    #C0390
    ChrTalk(
        0xFE,
        (
            "でもリュウ君、面白かったの。\x01",
            "ぜんぶアンリちゃんのせいに\x01",
            "しようとしちゃって……\x02",
        )
    )

    CloseMessageWindow()

    #C0391
    ChrTalk(
        0xFE,
        (
            "でも、すぐにばれちゃって、\x01",
            "もっと叱られちゃったの。\x01",
            "くすくす……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_72B6")

    Jump("loc_73B7")

    label("loc_72BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_72C9")
    Jump("loc_73B7")

    label("loc_72C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_72D7")
    Jump("loc_73B7")

    label("loc_72D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_73AE")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6B, 0x0, 0x2)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7391")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6B, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7353")

    #C0392
    ChrTalk(
        0xF,
        "あの傘、大事なものなの……\x02",
    )

    CloseMessageWindow()

    #C0393
    ChrTalk(
        0xF,
        (
            "くすん、くすん……\x01",
            "お願いね、お兄ちゃん……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_738D")

    label("loc_7353")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7368")
    Call(0, 16)
    SetScenarioFlags(0x1, 0)
    Jump("loc_738D")

    label("loc_7368")


    #C0394
    ChrTalk(
        0xF,
        (
            "えへへ、\x01",
            "お姉ちゃん優しいな……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_738D")

    TalkEnd(0xFE)
    Return()

    label("loc_7391")


    #C0395
    ChrTalk(
        0xF,
        "くすん、くすん……\x02",
    )

    CloseMessageWindow()
    Jump("loc_73B7")

    label("loc_73AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_73B7")

    label("loc_73B7")

    TalkEnd(0xFE)
    Return()

    # Function_24_7009 end

    def Function_25_73BB(): pass

    label("Function_25_73BB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BD, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7A47")

    #C0396
    ChrTalk(
        0xFE,
        "ああ、特務支援課の皆さんっ……！\x02",
    )

    CloseMessageWindow()

    #C0397
    ChrTalk(
        0x101,
        (
            "#00005F君は、イアン先生の助手の\x01",
            "ピート君じゃないか。\x02\x03",

            "#00001F１人みたいだけど……\x01",
            "先生はどうしたんだ？\x02",
        )
    )

    CloseMessageWindow()

    #C0398
    ChrTalk(
        0xFE,
        (
            "イアン先生は、この状況をみて\x01",
            "オルキスタワーに抗議しに\x01",
            "行ってしまったんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0399
    ChrTalk(
        0xFE,
        (
            "僕をここに預けていってから、\x01",
            "それきり連絡もとれなくて……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x95, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_78D2")

    #C0400
    ChrTalk(
        0x102,
        "#00106Fイアン先生が……心配ね。\x02",
    )

    CloseMessageWindow()

    #C0401
    ChrTalk(
        0x103,
        (
            "#00208Fタワーに行ったとなると、\x01",
            "もしかしたら大統領に\x01",
            "拘束されたかもしれません。\x02",
        )
    )

    CloseMessageWindow()

    #C0402
    ChrTalk(
        0x104,
        "#00301F急いだ方がよさそうだな。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    #C0403
    ChrTalk(
        0x101,
        (
            "#00003F……ピート君。\x02\x03",

            "#00001Fイアン先生は他に、\x01",
            "何か言っていなかったかい？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0404
    ChrTalk(
        0xFE,
        "そういえば……\x02",
    )

    CloseMessageWindow()

    #C0405
    ChrTalk(
        0xFE,
        (
            "先生、なんだか\x01",
            "気になることを言ってました。\x02",
        )
    )

    CloseMessageWindow()

    #C0406
    ChrTalk(
        0xFE,
        (
            "この状況が収まったら、\x01",
            "事務所に戻って先生の机を\x01",
            "掃除しておいてくれって。\x02",
        )
    )

    CloseMessageWindow()

    #C0407
    ChrTalk(
        0x101,
        "#00005F掃除……？\x02",
    )

    CloseMessageWindow()

    #C0408
    ChrTalk(
        0xFE,
        (
            "ええ、最初は急いで出て行くからと\x01",
            "思ってたんですけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0409
    ChrTalk(
        0xFE,
        (
            "いつも掃除は僕任せの先生も\x01",
            "机だけは出来るだけ触らないように\x01",
            "普段から言っていたんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0410
    ChrTalk(
        0xFE,
        (
            "仕事上、助手の僕にも\x01",
            "見せられないものも多いからって\x01",
            "そのままにしてたんですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0411
    ChrTalk(
        0x102,
        (
            "#00108Fイアン先生が……\x01",
            "確かに気になるわね……\x02\x03",

            "#00106Fこんなタイミングで\x01",
            "掃除を頼むというのも、\x01",
            "よく分からないし。\x02",
        )
    )

    CloseMessageWindow()

    #C0412
    ChrTalk(
        0x101,
        (
            "#00003F………………………………\x02\x03",

            "#00000Fピート君、イアン先生のことは\x01",
            "俺たちに任せて、君はこのまま\x01",
            "ここに避難していてくれ。\x02\x03",

            "何か分かったら\x01",
            "すぐに連絡するからさ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7A08")

    label("loc_78D2")


    #C0413
    ChrTalk(
        0x102,
        "#00106Fイアン先生が……心配ね。\x02",
    )

    CloseMessageWindow()

    #C0414
    ChrTalk(
        0x103,
        (
            "#00208Fタワーに行ったとなると、\x01",
            "もしかしたら大統領に\x01",
            "拘束されたかもしれません。\x02",
        )
    )

    CloseMessageWindow()

    #C0415
    ChrTalk(
        0x104,
        "#00301F急いだ方がよさそうだな。\x02",
    )

    CloseMessageWindow()

    #C0416
    ChrTalk(
        0x101,
        (
            "#00003Fああ……\x02\x03",

            "#00000Fピート君、イアン先生のことは\x01",
            "俺たちに任せて、君はこのまま\x01",
            "ここに避難していてくれ。\x02\x03",

            "何か分かったら\x01",
            "すぐに連絡するからさ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7A08")


    #C0417
    ChrTalk(
        0xFE,
        (
            "わ、分かりました……\x01",
            "どうかよろしくお願いします！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1BD, 5)
    Jump("loc_7AAA")

    label("loc_7A47")


    #C0418
    ChrTalk(
        0xFE,
        (
            "皆さん、イアン先生のことは\x01",
            "どうかよろしくお願いします。\x02",
        )
    )

    CloseMessageWindow()

    #C0419
    ChrTalk(
        0xFE,
        "先生……無事だといいんですけど。\x02",
    )

    CloseMessageWindow()

    label("loc_7AAA")

    TalkEnd(0xFE)
    Return()

    # Function_25_73BB end

    def Function_26_7AAE(): pass

    label("Function_26_7AAE")

    EventBegin(0x0)
    Fade(500)
    OP_68(53840, 1200, 2280, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(28210, 0)
    SetChrPos(0x101, 53550, 0, 2200, 90)
    SetChrPos(0x102, 53350, 0, 1200, 90)
    SetChrPos(0x109, 52400, 0, 2200, 90)
    SetChrPos(0x105, 52200, 0, 1200, 90)
    TurnDirection(0x8, 0x101, 0)
    OP_4B(0x8, 0xFF)
    OP_4B(0xF, 0xFF)
    OP_4B(0xA, 0xFF)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12C, 0)), scpexpr(EXPR_END)), "loc_7C01")

    #C0420
    ChrTalk(
        0x101,
        (
            "#6P#00000Fやあ、オスカー。\x01",
            "依頼を見て来させてもらったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0421
    ChrTalk(
        0x8,
        (
            "#11Pおう、ロイド！\x01",
            "来てくれると思ってたぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0422
    ChrTalk(
        0x102,
        (
            "#6P#00100Fではさっそくですが、\x01",
            "詳しく事情をお聞きして\x01",
            "いいですか？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7E5D")

    label("loc_7C01")


    #C0423
    ChrTalk(
        0x101,
        (
            "#6P#00000Fやあオスカー、久しぶり。\x01",
            "依頼を見て来させてもらったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0424
    ChrTalk(
        0x8,
        (
            "#11Pおお、ロイドじゃねえか！\x01",
            "来てくれると思ってたぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0425
    ChrTalk(
        0x8,
        (
            "#11Pそれにしても、\x01",
            "随分顔を見なかったが\x01",
            "どこ行ってやがったんだ？\x02",
        )
    )

    CloseMessageWindow()

    #C0426
    ChrTalk(
        0x8,
        (
            "#11Pミシュラムに長期滞在でも\x01",
            "してたのかよ？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0427
    ChrTalk(
        0x101,
        (
            "#6P#00006Fあのな……\x01",
            "そんなわけないだろ？\x02\x03",

            "#00001Fそれに、『研修のために\x01",
            "一度支援課を離れる』って\x01",
            "ちゃんと挨拶したじゃないか。\x02",
        )
    )

    CloseMessageWindow()

    #C0428
    ChrTalk(
        0x8,
        (
            "#11Pあれ、そうだったか？\x01",
            "すっかり忘れちまってたぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0429
    ChrTalk(
        0x8,
        (
            "#11P……っと話が逸れちまったな。\x01",
            "今回の依頼について話さねえと。\x02",
        )
    )

    CloseMessageWindow()

    #C0430
    ChrTalk(
        0x102,
        (
            "#6P#00100Fでは、さっそくですが\x01",
            "詳しく事情を聞かせてください。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x12C, 0)

    label("loc_7E5D")


    #C0431
    ChrTalk(
        0x8,
        (
            "#11Pああ、依頼っていうのは、\x01",
            "そこにいるモモちゃんの事でな。\x02",
        )
    )

    CloseMessageWindow()

    #C0432
    ChrTalk(
        0x8,
        (
            "#11Pタリーズ商店さんちの子供なんだが、\x01",
            "今日は雨の中傘をさして\x01",
            "お使いに来てくれてたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0433
    ChrTalk(
        0x8,
        "#11Pところが……\x02",
    )

    CloseMessageWindow()
    OP_68(53460, 1500, 2390, 2000)

    def lambda_7F28():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_7F28)
    Sleep(10)

    def lambda_7F38():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF, 2, lambda_7F38)
    Sleep(10)

    def lambda_7F48():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_7F48)
    Sleep(10)

    def lambda_7F58():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_7F58)
    Sleep(10)

    def lambda_7F68():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_7F68)
    Sleep(10)

    def lambda_7F78():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_7F78)
    WaitChrThread(0x105, 2)
    OP_6F(0x1)

    #C0434
    ChrTalk(
        0xF,
        "……くすん、くすん……\x02",
    )

    CloseMessageWindow()

    #C0435
    ChrTalk(
        0xF,
        (
            "モモの、モモの、\x01",
            "大切なピンクの傘が\x01",
            "どこかにいっちゃったのぅ……\x02",
        )
    )

    CloseMessageWindow()

    #C0436
    ChrTalk(
        0x8,
        "#11P……ってわけなんだ。\x02",
    )

    CloseMessageWindow()

    #C0437
    ChrTalk(
        0x101,
        (
            "#12P#00005Fなるほどな……\x02\x03",

            "#00001F店の中や外は探してみたんですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0438
    ChrTalk(
        0xA,
        (
            "一応、オスカーと私で\x01",
            "くまなく探したわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0439
    ChrTalk(
        0xA,
        (
            "そしたらね……\x01",
            "こんなのが出てきたの。\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    #A0440
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ベネットはピンクの傘を差し出した。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0441
    ChrTalk(
        0x109,
        (
            "#12P#10105Fえ、えっと……？\x01",
            "このピンクの傘は……\x02",
        )
    )

    CloseMessageWindow()

    #C0442
    ChrTalk(
        0x105,
        (
            "#12P#10305Fこれがその女の子の\x01",
            "傘なんじゃないのかい？\x02",
        )
    )

    CloseMessageWindow()

    #C0443
    ChrTalk(
        0xA,
        (
            "私もそう思ったんだけど……\x01",
            "ここの部分、見てみてよ。\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    #A0444
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ベネットは、傘の柄の部分を\x01",
            "ロイドたちに指し示した。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0445
    ChrTalk(
        0x102,
        (
            "#12P#00100F『めいりん』……って\x01",
            "書いてあるわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0446
    ChrTalk(
        0x101,
        (
            "#12P#00003Fなるほどな……\x02\x03",

            "#00000F要するに、間違って\x01",
            "持って行かれて\x01",
            "しまったわけだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0447
    ChrTalk(
        0x8,
        "#11Pああ、そうみたいだ。\x02",
    )

    CloseMessageWindow()

    #C0448
    ChrTalk(
        0x8,
        (
            "#11P今日は雨で客が少ないし、\x01",
            "他にも何組か客がいたのは\x01",
            "覚えてるんだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0449
    ChrTalk(
        0x8,
        (
            "#11Pどうしてもその\x01",
            "『めいりん』って名前が\x01",
            "誰のものか分からなくてな。\x02",
        )
    )

    CloseMessageWindow()

    #C0450
    ChrTalk(
        0x8,
        (
            "#11Pなんとかこの持ち主を探し出して、\x01",
            "間違えて持ってかれた\x01",
            "傘を回収してきてほしいんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0451
    ChrTalk(
        0x8,
        "#11Pどうだ、やれそうか？\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0x5A, 0x1F4)

    #C0452
    ChrTalk(
        0x101,
        (
            "#6P#00000Fああ、分かった。\x01",
            "俺たちに任せてくれ。\x02\x03",

            "きっと傘をみつけてみせるよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0453
    ChrTalk(
        0x8,
        "#11Pおう、頼んだぜロイド！\x02",
    )

    CloseMessageWindow()

    #C0454
    ChrTalk(
        0x102,
        (
            "#12P#00103Fでも、そうね。\x01",
            "この『めいりん』って名前……\x01",
            "もう少し手がかりがほしいわね。\x02\x03",

            "#00100Fロイド、心当たりはない？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_84E9():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_84E9)
    Sleep(50)

    def lambda_84F9():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_84F9)
    Sleep(50)

    def lambda_8509():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_8509)
    Sleep(300)

    #C0455
    ChrTalk(
        0x109,
        (
            "#6P#10100Fそうですね、\x01",
            "１度くらい話したことが\x01",
            "あったりしませんか？\x02\x03",

            "#10106Fせめて、どこの街区かくらい\x01",
            "分かればいいんですけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0456
    ChrTalk(
        0x101,
        (
            "#11P#00003Fうーん、どうだったかな……\x01",
            "（確かにどこかで聞いたことが\x01",
            "  あるような、ないような……）\x02\x03",

            "#00000F『めいりん』って子は、確か……\x02",
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
            "中央広場の住民\x01",      # 0
            "西通りの住民\x01",        # 1
            "住宅街の住民\x01",        # 2
            "東通りの住民\x01",        # 3
            "港湾区の住民\x01",        # 4
            "行政区の住民\x01",        # 5
            "歓楽街の住民\x01",        # 6
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8890")
    OP_2C(0x6B, 0x1)

    #C0457
    ChrTalk(
        0x101,
        (
            "#11P#00000F……東通りに住んでいる\x01",
            "女の子の名前じゃなかったか？\x02\x03",

            "たしか商工会会長のモルスさんの\x01",
            "お孫さんだったような気がする。\x02",
        )
    )

    CloseMessageWindow()

    #C0458
    ChrTalk(
        0x102,
        (
            "#11P#12P#00105Fあ、そういえば……！\x01",
            "何度か話したことがあるわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0459
    ChrTalk(
        0x105,
        (
            "#6P#10304Fロイっていう\x01",
            "お兄さんがいる子だね。\x02\x03",

            "#10300Fするとここには兄妹で\x01",
            "買い物に来てたのかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0460
    ChrTalk(
        0x8,
        (
            "#11P……おお、そうだそうだ！\x01",
            "たしかに兄妹で来てた客がいたな。\x02",
        )
    )

    CloseMessageWindow()

    #C0461
    ChrTalk(
        0x8,
        (
            "#11Pしかし、モルス爺さんの孫かあ。\x01",
            "確かに見たことある気がするぜ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8D15")

    label("loc_8890")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_88BE"),
        (1, "loc_8909"),
        (2, "loc_8952"),
        (4, "loc_899B"),
        (5, "loc_89E4"),
        (6, "loc_8A2D"),
        (SWITCH_DEFAULT, "loc_8A76"),
    )


    label("loc_88BE")


    #C0462
    ChrTalk(
        0x101,
        (
            "#11P#00000F……中央広場に住んでいる\x01",
            "女の子の名前じゃなかったか？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8A76")

    label("loc_8909")


    #C0463
    ChrTalk(
        0x101,
        (
            "#11P#00000F……西通りに住んでいる\x01",
            "女の子の名前じゃなかったか？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8A76")

    label("loc_8952")


    #C0464
    ChrTalk(
        0x101,
        (
            "#11P#00000F……住宅街に住んでいる\x01",
            "女の子の名前じゃなかったか？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8A76")

    label("loc_899B")


    #C0465
    ChrTalk(
        0x101,
        (
            "#11P#00000F……港湾区に住んでいる\x01",
            "女の子の名前じゃなかったか？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8A76")

    label("loc_89E4")


    #C0466
    ChrTalk(
        0x101,
        (
            "#11P#00000F……行政区に住んでいる\x01",
            "女の子の名前じゃなかったか？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8A76")

    label("loc_8A2D")


    #C0467
    ChrTalk(
        0x101,
        (
            "#11P#00000F……歓楽街に住んでいる\x01",
            "女の子の名前じゃなかったか？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8A76")

    label("loc_8A76")


    #C0468
    ChrTalk(
        0x105,
        "#6P#10304Fいや、違うね。\x02",
    )

    CloseMessageWindow()

    def lambda_8A99():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_8A99)
    Sleep(50)

    def lambda_8AA9():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_8AA9)
    Sleep(300)

    #C0469
    ChrTalk(
        0x101,
        "#11P#00005Fえ。\x02",
    )

    CloseMessageWindow()

    #C0470
    ChrTalk(
        0x105,
        (
            "#6P#10300F『メイリン』といえば、\x01",
            "東通りの商工会会長、\x01",
            "モルス氏の孫娘の名前だ。\x02\x03",

            "#10304Fロイというお兄さんがいるし、\x01",
            "多分ここには兄妹で\x01",
            "来ていたんじゃないかな。\x02",
        )
    )

    CloseMessageWindow()

    #C0471
    ChrTalk(
        0x8,
        (
            "#11P……おお、そうだそうだ！\x01",
            "たしかに兄妹で来てた客がいたな。\x02",
        )
    )

    CloseMessageWindow()

    #C0472
    ChrTalk(
        0x101,
        (
            "#11P#00005Fそうか……\x01",
            "モルスさんのお孫さんだったか。\x02",
        )
    )

    CloseMessageWindow()

    #C0473
    ChrTalk(
        0x102,
        (
            "#12P#00100Fそういえば何度か\x01",
            "話したことがあったわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0474
    ChrTalk(
        0x109,
        "#6P#10100Fでもワジ君、よく知ってたね？\x02",
    )

    CloseMessageWindow()

    #C0475
    ChrTalk(
        0x105,
        (
            "#6P#10302Fフフ、ホストのバイトをしてると\x01",
            "色々と情報が入ってくるからね。\x02",
        )
    )

    CloseMessageWindow()

    #C0476
    ChrTalk(
        0x109,
        (
            "#6P#10106Fな、なるほど……\x01",
            "って、あんまり感心できないけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0477
    ChrTalk(
        0x101,
        (
            "#11P#00009Fまあまあ。\x01",
            "とにかく助かったよ、ワジ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8D15")


    #C0478
    ChrTalk(
        0x8,
        (
            "#11Pよし、それじゃあ\x01",
            "メイリンちゃんの傘は\x01",
            "お前たちに預けとくよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0479
    ChrTalk(
        0xA,
        "はい、これね。\x02",
    )

    CloseMessageWindow()

    def lambda_8D74():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_8D74)
    Sleep(50)

    def lambda_8D84():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_8D84)
    Sleep(50)

    def lambda_8D94():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_8D94)
    Sleep(50)

    def lambda_8DA4():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_8DA4)
    Sleep(50)

    def lambda_8DB4():
        OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_8DB4)
    WaitChrThread(0xA, 2)
    Sleep(500)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0480
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x325),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を受け取った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x325, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_9B(0x1, 0xA, 0xB4, 0x3E8, 0x5DC, 0x0)

    #C0481
    ChrTalk(
        0x8,
        (
            "#11Pそいつをメイリンちゃんに\x01",
            "返した上で、モモちゃんの傘を\x01",
            "預かってきてくれ。\x02",
        )
    )

    CloseMessageWindow()

    #C0482
    ChrTalk(
        0x8,
        "#11P頼んだぜ、ロイド。\x02",
    )

    CloseMessageWindow()

    #C0483
    ChrTalk(
        0xF,
        (
            "くすん、くすん……\x01",
            "お兄ちゃん、おねがいね……\x02",
        )
    )

    CloseMessageWindow()

    #C0484
    ChrTalk(
        0x101,
        "#12P#00000Fああ、任せてくれ。\x02",
    )

    CloseMessageWindow()

    #C0485
    ChrTalk(
        0x102,
        (
            "#12P#00100Fそれじゃあ、\x01",
            "一度モルス会長のお宅を\x01",
            "訪ねるのがよさそうね。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_8F3B():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_8F3B)
    Sleep(50)

    def lambda_8F4B():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_8F4B)
    Sleep(50)

    def lambda_8F5B():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_8F5B)

    #C0486
    ChrTalk(
        0x101,
        (
            "#5P#00000F確か、東通りの外れにある\x01",
            "お宅だったな。\x02\x03",

            "とりあえず\x01",
            "行ってみるとしよう。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    Sound(80, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0487
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "クエスト【消えた雨傘の捜索】\x07\x00",
            "を開始した！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetChrPos(0x0, 52100, 0, -200, 270)
    TurnDirection(0xA, 0xF, 0)
    TurnDirection(0xF, 0xA, 0)
    OP_4C(0x8, 0xFF)
    OP_4C(0xF, 0xFF)
    OP_4C(0xA, 0xFF)
    SetScenarioFlags(0x132, 3)
    OP_29(0x6B, 0x1, 0x0)
    ClearChrFlags(0xA, 0x10)
    ClearChrFlags(0xF, 0x10)
    EventEnd(0x5)
    Return()

    # Function_26_7AAE end

    def Function_27_905F(): pass

    label("Function_27_905F")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(53840, 1200, 2280, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(28210, 0)
    SetChrPos(0x101, 53550, 0, 2200, 90)
    SetChrPos(0x102, 53350, 0, 1200, 90)
    SetChrPos(0x109, 52400, 0, 2200, 90)
    SetChrPos(0x105, 52200, 0, 1200, 90)
    OP_93(0xA, 0xB4, 0x0)
    OP_93(0xF, 0xB4, 0x0)
    TurnDirection(0x8, 0x101, 0)
    OP_4B(0x8, 0xFF)
    OP_4B(0xF, 0xFF)
    OP_4B(0xA, 0xFF)
    Sleep(500)
    FadeToBright(1000, 0)
    OP_0D()

    #C0488
    ChrTalk(
        0x8,
        (
            "#11Pお、ロイド！\x01",
            "首尾はどうだった？\x02",
        )
    )

    CloseMessageWindow()

    #C0489
    ChrTalk(
        0x101,
        "#6P#00000Fああ、無事回収できたよ。\x02",
    )

    CloseMessageWindow()

    def lambda_9161():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_9161)
    Sleep(10)

    def lambda_9171():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_9171)
    Sleep(10)

    def lambda_9181():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_9181)
    Sleep(10)

    def lambda_9191():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_9191)
    WaitChrThread(0x105, 2)
    Sleep(500)

    #C0490
    ChrTalk(
        0x101,
        (
            "#12P#00000Fはい、モモちゃん。\x01",
            "これをどうぞ。\x02",
        )
    )

    CloseMessageWindow()
    OP_9B(0x1, 0x101, 0x0, 0x3E8, 0x5DC, 0x0)
    Sleep(500)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0491
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#16Iモモの傘\x07\x00",
            "を渡した。\x02",
        )
    )

    Sound(17, 0, 100, 0)
    CloseMessageWindow()
    FadeToBright(300, 0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    SubItemNumber(0x325, 1)
    OP_9B(0x1, 0x101, 0xB4, 0x3E8, 0x5DC, 0x0)

    #C0492
    ChrTalk(
        0xF,
        (
            "ぐすん……\x01",
            "あっ……モモの傘……\x02",
        )
    )

    CloseMessageWindow()

    #C0493
    ChrTalk(
        0xF,
        (
            "これ、お父さんがモモのために\x01",
            "買ってくれた大事なものなの……\x02",
        )
    )

    CloseMessageWindow()

    #C0494
    ChrTalk(
        0xF,
        (
            "あ、ありがとう……\x01",
            "ほんとにありがとうっ……！\x02",
        )
    )

    CloseMessageWindow()

    #C0495
    ChrTalk(
        0x109,
        (
            "#12P#10105Fああ、そうだったんだ。\x02\x03",

            "#10100Fふふ、戻ってきて\x01",
            "よかったね。\x02",
        )
    )

    CloseMessageWindow()

    #C0496
    ChrTalk(
        0xF,
        "うんっ……！\x02",
    )

    CloseMessageWindow()

    def lambda_9345():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_9345)
    Sleep(50)

    def lambda_9355():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_9355)
    Sleep(50)

    def lambda_9365():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_9365)
    Sleep(50)

    def lambda_9375():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_9375)
    Sleep(300)

    #C0497
    ChrTalk(
        0x105,
        (
            "#6P#10304Fさて、これにて\x01",
            "一件落着ってわけだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0498
    ChrTalk(
        0x8,
        "#11Pおかげさまで助かったよ。\x02",
    )

    CloseMessageWindow()

    #C0499
    ChrTalk(
        0x8,
        (
            "#11Pやっぱお前らは\x01",
            "頼りになるよな～。\x02",
        )
    )

    CloseMessageWindow()

    #C0500
    ChrTalk(
        0xA,
        (
            "また何かあったら\x01",
            "よろしく頼むわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0501
    ChrTalk(
        0x102,
        (
            "#6P#00100Fええ、いつでも依頼を\x01",
            "お待ちしてます。\x02",
        )
    )

    CloseMessageWindow()

    #C0502
    ChrTalk(
        0x101,
        "#6P#00000Fそれじゃあな、オスカー。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0503
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "クエスト【消えた雨傘の捜索】\x07\x00",
            "を達成した！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetChrPos(0x0, 52100, 0, -200, 270)
    TurnDirection(0xA, 0xF, 0)
    TurnDirection(0xF, 0xA, 0)
    OP_4C(0x8, 0xFF)
    OP_4C(0xF, 0xFF)
    OP_4C(0xA, 0xFF)
    OP_29(0x6B, 0x1, 0x5)
    OP_29(0x6B, 0x1, 0x6)
    OP_29(0x6B, 0x4, 0x10)
    OP_29(0xA1, 0x1, 0x10)
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0xF, 0x10)
    OP_C9(0x1, 0x1000)
    EventEnd(0x5)
    Return()

    # Function_27_905F end

    def Function_28_9537(): pass

    label("Function_28_9537")

    EventBegin(0x0)
    Fade(500)
    OP_68(52330, 2200, -660, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(340, 0)
    SetCameraDistance(23210, 0)
    SetChrPos(0x101, 53850, 0, 1490, 90)
    SetChrPos(0x102, 53850, 0, 500, 90)
    SetChrPos(0x103, 52650, 0, 1490, 90)
    SetChrPos(0x109, 52650, 0, 500, 90)
    SetChrPos(0x104, 51450, 0, 1490, 90)
    SetChrPos(0x105, 51450, 0, 500, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_93(0x8, 0x10E, 0x0)
    OP_4B(0x8, 0xFF)
    OP_4B(0xA, 0xFF)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12C, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_971A")

    #C0504
    ChrTalk(
        0x8,
        "おう、よく来たなロイド。\x02",
    )

    CloseMessageWindow()

    #C0505
    ChrTalk(
        0x8,
        (
            "今回の新作パンは、\x01",
            "ベネットの作ったパンだ。\x01",
            "試しに食べてみてくれよ。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0506
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x212),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x212, 1)
    SetMessageWindowPos(14, 280, 60, 3)

    #C0507
    ChrTalk(
        0x101,
        (
            "#00000Fありがとう、オスカー。\x01",
            "後でおいしく頂かせてもらうよ。\x02\x03",

            "今日は仕事で来たんだけど……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9786")

    label("loc_971A")


    #C0508
    ChrTalk(
        0x8,
        (
            "おう、よく来たなロイド。\x01",
            "うちのパンを買いにきたのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0509
    ChrTalk(
        0x101,
        "#00000Fえっと、今日は仕事で来たんだけど……\x02",
    )

    CloseMessageWindow()

    label("loc_9786")

    SetChrName("")

    #A0510
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "『一押しグルメ』の取材で\x01",
            "来たことを説明した。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0511
    ChrTalk(
        0x8,
        (
            "ああ、そういやあ\x01",
            "そんな話があったなあ。\x02",
        )
    )

    CloseMessageWindow()

    #C0512
    ChrTalk(
        0x8,
        (
            "そうだな、ウチのパンは\x01",
            "全部お勧めなんだが……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12C, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_987E")

    #C0513
    ChrTalk(
        0x8,
        (
            "強いて言うなら、\x01",
            "さっきお前たちにやった\x01",
            "『ベネットワンダフル』だな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x12C, 2)
    Jump("loc_98C3")

    label("loc_987E")


    #C0514
    ChrTalk(
        0x8,
        (
            "強いて言うなら、お前たちにもやった\x01",
            "『ベネットワンダフル』だな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_98C3")


    #C0515
    ChrTalk(
        0x102,
        "#00105Fへえ、そうなんですか？\x02",
    )

    CloseMessageWindow()

    #C0516
    ChrTalk(
        0x8,
        (
            "ああ、ベネットが作ったパンでも\x01",
            "こいつは本当にいい出来でな。\x02",
        )
    )

    CloseMessageWindow()

    #C0517
    ChrTalk(
        0x8,
        (
            "今の《モルジュ》なら、\x01",
            "まちがいなく最高に美味い──\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("ベネットの声")

    #A0518
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "ちょ、ちょっと待ちなさい！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    def lambda_99AA():

        label("loc_99AA")

        TurnDirection(0xFE, 0xA, 500)
        Yield()
        Jump("loc_99AA")

    QueueWorkItem2(0x109, 0, lambda_99AA)

    def lambda_99BC():

        label("loc_99BC")

        TurnDirection(0xFE, 0xA, 500)
        Yield()
        Jump("loc_99BC")

    QueueWorkItem2(0x102, 0, lambda_99BC)

    def lambda_99CE():

        label("loc_99CE")

        TurnDirection(0xFE, 0xA, 500)
        Yield()
        Jump("loc_99CE")

    QueueWorkItem2(0x104, 0, lambda_99CE)

    def lambda_99E0():

        label("loc_99E0")

        TurnDirection(0xFE, 0xA, 500)
        Yield()
        Jump("loc_99E0")

    QueueWorkItem2(0x101, 0, lambda_99E0)

    def lambda_99F2():

        label("loc_99F2")

        TurnDirection(0xFE, 0xA, 500)
        Yield()
        Jump("loc_99F2")

    QueueWorkItem2(0x105, 0, lambda_99F2)

    def lambda_9A04():

        label("loc_9A04")

        TurnDirection(0xFE, 0xA, 500)
        Yield()
        Jump("loc_9A04")

    QueueWorkItem2(0x103, 0, lambda_9A04)

    def lambda_9A16():

        label("loc_9A16")

        TurnDirection(0xFE, 0xA, 500)
        Yield()
        Jump("loc_9A16")

    QueueWorkItem2(0x8, 1, lambda_9A16)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9AB1")
    OP_68(55480, 1510, 1690, 1500)
    OP_63(0xA, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    def lambda_9A64():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_9A64)
    SetChrPos(0xA, 60080, 10, 4000, 135)
    OP_95(0xA, 59190, 10, 2000, 3000, 0x0)
    OP_95(0xA, 57580, 10, 2090, 3000, 0x0)
    OP_64(0xA)
    Jump("loc_9B32")

    label("loc_9AB1")

    OP_68(52700, 1510, 1930, 1500)
    MoveCamera(45, 22, 0, 1500)
    OP_6E(340, 1500)
    SetCameraDistance(23210, 1500)
    OP_63(0xA, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    SetChrPos(0xA, 52110, 1000, 10270, 315)
    ClearChrFlags(0xA, 0x4)
    OP_95(0xA, 52470, 0, 4720, 3000, 0x0)
    OP_95(0xA, 53600, 0, 4100, 3000, 0x0)
    OP_64(0xA)

    label("loc_9B32")

    EndChrThread(0x101, 0x0)
    EndChrThread(0x102, 0x0)
    EndChrThread(0x103, 0x0)
    EndChrThread(0x104, 0x0)
    EndChrThread(0x109, 0x0)
    EndChrThread(0x105, 0x0)
    EndChrThread(0x8, 0x1)

    #C0519
    ChrTalk(
        0x8,
        (
            "おう、ベネット。\x01",
            "今、ちょうどお前のパンを──\x02",
        )
    )

    CloseMessageWindow()

    #C0520
    ChrTalk(
        0xA,
        (
            "か、勝手なことしないでよ！\x01",
            "私にとってそのパンは、\x01",
            "まだまだ未完成品なんだから！\x02",
        )
    )

    CloseMessageWindow()

    #C0521
    ChrTalk(
        0xA,
        (
            "オスカーを超える\x01",
            "パンが出来るまでは、\x01",
            "グルメガイドになんて……！！\x02",
        )
    )

    CloseMessageWindow()

    #C0522
    ChrTalk(
        0x8,
        (
            "はは、いいじゃねえかよ。\x01",
            "せっかくこんな美味いんだからさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0523
    ChrTalk(
        0xA,
        "……っ……！！\x02",
    )

    CloseMessageWindow()

    #C0524
    ChrTalk(
        0xA,
        (
            "と、とにかく……\x01",
            "勝手にお勧めになんてしたら\x01",
            "承知しないんだからねっ！？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9D2D")
    OP_95(0xA, 59190, 10, 2000, 3000, 0x0)
    OP_95(0xA, 60330, 0, 3200, 3000, 0x0)

    def lambda_9CF7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_9CF7)
    OP_95(0xA, 60080, 10, 4000, 2000, 0x0)
    SetChrPos(0xA, 119120, 0, -660, 275)
    Jump("loc_9D9E")

    label("loc_9D2D")

    OP_95(0xA, 52470, 0, 4720, 3000, 0x0)
    OP_95(0xA, 52110, 1000, 10270, 3000, 0x0)
    OP_95(0xA, 51750, 1000, 10270, 3000, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_9D88")
    SetChrPos(0xA, 51280, 1000, 12870, 180)
    Jump("loc_9D99")

    label("loc_9D88")

    SetChrPos(0xA, 51280, 1000, 12870, 90)

    label("loc_9D99")

    ClearChrFlags(0xA, 0x4)

    label("loc_9D9E")

    OP_68(53180, 2200, 190, 1500)
    MoveCamera(45, 22, 0, 1500)
    OP_6E(340, 1500)
    SetCameraDistance(23210, 1500)
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1500)

    #C0525
    ChrTalk(
        0x8,
        (
            "やれやれ、なんだよベネットのヤツ。\x01",
            "せっかく美味しいって言ってるのによ。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_9EB1():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_9EB1)
    Sleep(50)

    def lambda_9EC1():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_9EC1)
    Sleep(50)

    def lambda_9ED1():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_9ED1)
    Sleep(50)

    def lambda_9EE1():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_9EE1)
    Sleep(50)

    def lambda_9EF1():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_9EF1)
    Sleep(50)

    def lambda_9F01():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_9F01)
    Sleep(300)

    #C0526
    ChrTalk(
        0x105,
        "#10304Fフフ、だからこそって気もするけど。\x02",
    )

    CloseMessageWindow()

    #C0527
    ChrTalk(
        0x104,
        "#00309Fはは、あんたもスミに置けねえなあ。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 500)
    OP_63(0x8, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0528
    ChrTalk(
        0x101,
        (
            "#00006Fと、とにかく……\x01",
            "ベネットさんは嫌がってるみたいだし、\x01",
            "別のお勧めを紹介してくれないか？\x02",
        )
    )

    CloseMessageWindow()

    #C0529
    ChrTalk(
        0x8,
        "んー、仕方ねえなぁ。\x02",
    )

    CloseMessageWindow()

    #C0530
    ChrTalk(
        0x8,
        (
            "それじゃあ俺が今試作してる、\x01",
            "『しっとりカツサンド』を\x01",
            "ごちそうさせてもらうとするか。\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    #A0531
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ロイドたちはしっとりカツサンドを食べた。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0532
    ChrTalk(
        0x109,
        (
            "#10100Fもぐもぐ……\x01",
            "はあ、パンがとってもしっとり……\x02",
        )
    )

    CloseMessageWindow()

    #C0533
    ChrTalk(
        0x101,
        (
            "#00000Fああ、カツのソースも\x01",
            "ジューシーで……\x01",
            "美味しいよ、オスカー。\x02",
        )
    )

    CloseMessageWindow()

    #C0534
    ChrTalk(
        0x8,
        "はは、あんがとよ。\x02",
    )

    CloseMessageWindow()

    #C0535
    ChrTalk(
        0x8,
        (
            "ただ、そいつはまだ試作品でさ。\x01",
            "本格的に商品として売り出すのは\x01",
            "まだ先になりそうなんだよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0536
    ChrTalk(
        0x103,
        (
            "#00205Fそうなんですか……\x02\x03",

            "#00203Fだとしたら、わたしたちが\x01",
            "紹介しないほうが\x01",
            "いいかもしれませんね。\x02",
        )
    )

    CloseMessageWindow()

    #C0537
    ChrTalk(
        0x8,
        (
            "まあ、完成したら\x01",
            "お前たちにもプレゼントするから、\x01",
            "待っててくれよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0538
    ChrTalk(
        0x102,
        "#00100Fええ、楽しみにしていますね。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x1, 1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A28B")
    SetScenarioFlags(0x1, 2)

    label("loc_A28B")

    SetScenarioFlags(0x172, 6)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 1)), scpexpr(EXPR_END)), "loc_A2BF")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A2BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 2)), scpexpr(EXPR_END)), "loc_A2DC")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A2DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 3)), scpexpr(EXPR_END)), "loc_A2EF")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A2EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 4)), scpexpr(EXPR_END)), "loc_A302")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A302")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 5)), scpexpr(EXPR_END)), "loc_A31F")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A31F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 6)), scpexpr(EXPR_END)), "loc_A332")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A332")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 7)), scpexpr(EXPR_END)), "loc_A34F")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A34F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 0)), scpexpr(EXPR_END)), "loc_A362")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A362")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 1)), scpexpr(EXPR_END)), "loc_A37F")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A37F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 2)), scpexpr(EXPR_END)), "loc_A392")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A392")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 3)), scpexpr(EXPR_END)), "loc_A3AF")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A3AF")

    OP_29(0x80, 0x1, 0x6)
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x178, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A4B2")
    SetChrName("")
    Sound(9, 0, 100, 0)

    #A0539
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "飲食店６ヶ所の取材を終えた！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_A4A9")

    #A0540
    AnonymousTalk(
        0x101,
        (
            "#00003Fすぐにでもグレイスさんに\x01",
            "報告に行く事はできそうだけど……\x02\x03",

            "#00000Fまだ６人全員のお気に入りが\x01",
            "見つかったわけじゃない。\x01",
            "もう少し頑張ってみるかな？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_A4A9")

    SetScenarioFlags(0x178, 7)
    OP_29(0x80, 0x1, 0xD)

    label("loc_A4B2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x179, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A583")
    SetChrName("")
    Sound(9, 0, 100, 0)

    #A0541
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "特務支援課メンバー全員の\x01",
            "お気に入りを見つけた！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0542
    AnonymousTalk(
        0x101,
        (
            "#00000Fこれで６人全員の\x01",
            "お気に入りが見つかった。\x02\x03",

            "取材はこれで十分だな。\x01",
            "さっそく通信社に報告へ行こう。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x179, 0)
    OP_29(0x80, 0x1, 0xE)

    label("loc_A583")

    OP_4C(0x8, 0xFF)
    OP_4C(0xA, 0xFF)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 53850, 0, 1490, 90)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_28_9537 end

    def Function_29_A5B7(): pass

    label("Function_29_A5B7")

    TalkBegin(0xA)

    #C0543
    ChrTalk(
        0xA,
        (
            "ふう……\x01",
            "なかなかオスカーに勝てる\x01",
            "新作パンができないわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0544
    ChrTalk(
        0xA,
        (
            "ううん、あきらめずに\x01",
            "何度でも挑戦しなきゃ……！\x02",
        )
    )

    CloseMessageWindow()

    #C0545
    ChrTalk(
        0x101,
        (
            "#00003F（この人なら、『職人』枠で\x01",
            "  ミスコンに出場できそうだな……）\x02\x03",

            "#00000Fあの、すみません。\x01",
            "ちょっと相談なんですが……\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    #A0546
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "チャリティイベントの\x01",
            "ミスコンへの参加を頼んでみた。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0547
    ChrTalk(
        0xA,
        "……はあ、ミスコン！？\x02",
    )

    CloseMessageWindow()

    #C0548
    ChrTalk(
        0xA,
        (
            "え、遠慮しとくわ。\x01",
            "ガラじゃないし……\x02",
        )
    )

    CloseMessageWindow()

    #C0549
    ChrTalk(
        0xA,
        (
            "チャリティイベントは\x01",
            "料理を手伝ったの。\x01",
            "それで勘弁してちょうだい。\x02",
        )
    )

    CloseMessageWindow()

    #C0550
    ChrTalk(
        0x101,
        (
            "#00003Fそ、そうですか……\x01",
            "なら仕方ありませんね。\x02",
        )
    )

    CloseMessageWindow()

    #C0551
    ChrTalk(
        0x102,
        "#00100F他をあたってみましょう。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x198, 6)
    SetScenarioFlags(0x1, 3)
    TalkEnd(0xA)
    Return()

    # Function_29_A5B7 end

    SaveToFile()

Try(main)
