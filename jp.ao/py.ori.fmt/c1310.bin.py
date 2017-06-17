from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c1310.bin",                # FileName
        "c1310",                    # MapName
        "c1310",                    # Location
        0x001C,                     # MapIndex
        "ed7150",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 28, 0, 1, 0, 3],
    )

    BuildStringList((
        "c1310",                  # 0
        "警備員ウォング",         # 1
        "警備員ポール",           # 2
        "受付嬢ランフィ",         # 3
        "受付嬢コリンナ",         # 4
        "貿易商リゼロ",           # 5
        "市民",                   # 6
        "ロバーツ主任",           # 7
        "ヨナ",                   # 8
        "ディーター市長",         # 9
        "マリアベル",             # 10
    ))

    AddCharChip((
        "chr/ch27900.itc",                   # 00
        "chr/ch29300.itc",                   # 01
        "chr/ch28600.itc",                   # 02
        "chr/ch30500.itc",                   # 03
        "chr/ch21800.itc",                   # 04
        "chr/ch27702.itc",                   # 05
    ))

    DeclNpc(8500,    0,       13310,   270,  257,  0x0, 0,   2,   0,   0,   0,   0,   14,  255,  0)
    DeclNpc(-5730,   300,     29909,   180,  257,  0x0, 0,   2,   0,   0,   0,   0,   15,  255,  0)
    DeclNpc(0,       300,     31700,   180,  257,  0x0, 0,   0,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(7110,    300,     32759,   90,   257,  0x0, 0,   3,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(-4840,   0,       18180,   90,   261,  0x0, 0,   5,   0,   255, 255, 0,   12,  255,  0)
    DeclNpc(6570,    300,     29760,   0,    385,  0x0, 0,   4,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(6500,    0,       17850,   270,  385,  0x0, 0,   1,   0,   0,   0,   0,   13,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 30,  9.5,                   16.0,                  -0.5,                  9.0,                   [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.3333333432674408,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000001788139343,   0.0,                   -4.75,                 -5.333333492279053,    0.10000000894069672,   1.0])

    DeclActor(0,       300,     30300,   1500,    0,       1800,    31700,   0x007E, 0,  4,  0x0000)
    DeclActor(6650,    300,     31080,   1500,    7110,    1800,    32759,   0x007E, 0,  10, 0x0000)

    ChipFrameInfo(744, 0)                                        # 0

    ScpFunction((
        "Function_0_2E8",          # 00, 0
        "Function_1_3A0",          # 01, 1
        "Function_2_551",          # 02, 2
        "Function_3_558",          # 03, 3
        "Function_4_5B4",          # 04, 4
        "Function_5_5B8",          # 05, 5
        "Function_6_71E",          # 06, 6
        "Function_7_2023",         # 07, 7
        "Function_8_278A",         # 08, 8
        "Function_9_2794",         # 09, 9
        "Function_10_2901",        # 0A, 10
        "Function_11_2905",        # 0B, 11
        "Function_12_377D",        # 0C, 12
        "Function_13_4448",        # 0D, 13
        "Function_14_488E",        # 0E, 14
        "Function_15_54AF",        # 0F, 15
        "Function_16_5FD8",        # 10, 16
        "Function_17_7656",        # 11, 17
        "Function_18_767F",        # 12, 18
        "Function_19_7696",        # 13, 19
        "Function_20_76AD",        # 14, 20
        "Function_21_76C4",        # 15, 21
        "Function_22_76DB",        # 16, 22
        "Function_23_9598",        # 17, 23
        "Function_24_AEE6",        # 18, 24
        "Function_25_B1DA",        # 19, 25
        "Function_26_B300",        # 1A, 26
        "Function_27_B4B1",        # 1B, 27
        "Function_28_B814",        # 1C, 28
        "Function_29_B888",        # 1D, 29
        "Function_30_C5D7",        # 1E, 30
    ))


    def Function_0_2E8(): pass

    label("Function_0_2E8")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_328"),
        (1, "loc_334"),
        (2, "loc_340"),
        (3, "loc_34C"),
        (4, "loc_358"),
        (5, "loc_364"),
        (6, "loc_370"),
        (SWITCH_DEFAULT, "loc_37C"),
    )


    label("loc_328")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_388")

    label("loc_334")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_388")

    label("loc_340")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_388")

    label("loc_34C")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_388")

    label("loc_358")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_388")

    label("loc_364")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_388")

    label("loc_370")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_388")

    label("loc_37C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_388")

    label("loc_388")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_39F")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_388")

    label("loc_39F")

    Return()

    # Function_0_2E8 end

    def Function_1_3A0(): pass

    label("Function_1_3A0")

    SetChrChipByIndex(0xC, 0x5)
    SetChrSubChip(0xC, 0x0)
    EndChrThread(0xC, 0x0)
    SetChrBattleFlags(0xC, 0x4)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3C9")
    ClearScenarioFlags(0x25, 1)
    Event(0, 2)

    label("loc_3C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_3F0")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    Jump("loc_4F4")

    label("loc_3F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_417")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    Jump("loc_4F4")

    label("loc_417")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_425")
    Jump("loc_4F4")

    label("loc_425")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_433")
    Jump("loc_4F4")

    label("loc_433")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_446")
    SetChrFlags(0xB, 0x10)
    Jump("loc_4F4")

    label("loc_446")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_454")
    Jump("loc_4F4")

    label("loc_454")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_462")
    Jump("loc_4F4")

    label("loc_462")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_470")
    Jump("loc_4F4")

    label("loc_470")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_497")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    Jump("loc_4F4")

    label("loc_497")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_4B4")
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xB, 0x10)
    SetChrFlags(0xD, 0x10)
    Jump("loc_4F4")

    label("loc_4B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_4EB")
    SetChrFlags(0xC, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4D1")
    SetChrFlags(0xB, 0x10)

    label("loc_4D1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6C, 0x0, 0x2)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x131, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4E6")
    ClearChrFlags(0xE, 0x80)

    label("loc_4E6")

    Jump("loc_4F4")

    label("loc_4EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_4F4")

    label("loc_4F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_511")
    ClearScenarioFlags(0x22, 1)
    SetChrPos(0x0, 60, 300, 28550, 0)

    label("loc_511")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6C, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6C, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6C, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_53A")
    SetMapFlags(0x10000000)
    Event(0, 16)

    label("loc_53A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_550")
    SetMapFlags(0x10000000)
    Event(0, 23)

    label("loc_550")

    Return()

    # Function_1_3A0 end

    def Function_2_551(): pass

    label("Function_2_551")

    Sound(160, 0, 100, 0)
    Return()

    # Function_2_551 end

    def Function_3_558(): pass

    label("Function_3_558")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_59D")
    SetMapObjFrame(0xFF, "wlight_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "ylight_add", 0x0, 0x1)
    Sound(128, 1, 50, 0)

    label("loc_59D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x324, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_5B3")
    ModifyEventFlags(0, 0, 0x80)

    label("loc_5B3")

    Return()

    # Function_3_558 end

    def Function_4_5B4(): pass

    label("Function_4_5B4")

    Call(0, 5)
    Return()

    # Function_4_5B4 end

    def Function_5_5B8(): pass

    label("Function_5_5B8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x177, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x177, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5E1")
    Call(0, 29)
    Return()

    label("loc_5E1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7A, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7A, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7A, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x157, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_621")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C6, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_61D")
    Call(0, 24)
    Jump("loc_620")

    label("loc_61D")

    Call(0, 26)

    label("loc_620")

    Return()

    label("loc_621")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6C, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6C, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6C, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x131, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_64A")
    Call(0, 22)
    Return()

    label("loc_64A")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x134, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_65F")
    Call(0, 6)
    Jump("loc_71A")

    label("loc_65F")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_669")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_71A")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "話をする\x01",        # 0
            "換金をする\x01",      # 1
            "やめる\x01",          # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6C5")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_6C5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6E5")
    OP_AF(0xB4)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_715")

    label("loc_6E5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6F9")
    Jump("loc_715")

    label("loc_6F9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_715")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 6)

    label("loc_715")

    Jump("loc_669")

    label("loc_71A")

    TalkEnd(0xA)
    Return()

    # Function_5_5B8 end

    def Function_6_71E(): pass

    label("Function_6_71E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_72C")
    Jump("loc_2022")

    label("loc_72C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_73A")
    Jump("loc_2022")

    label("loc_73A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_8FD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_849")

    #C0001
    ChrTalk(
        0xA,
        (
            "まさか一般住民を巻き込む形で\x01",
            "マインツを占拠してしまうなんて……\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0xA,
        (
            "ＩＢＣへの影響も懸念されますが、\x01",
            "こうなると最早、株価がどうこうという\x01",
            "レベルの話ではありませんね。\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0xA,
        (
            "とにかく、マインツの皆さんが\x01",
            "ご無事でいらっしゃることを祈ります。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_8F8")

    label("loc_849")


    #C0004
    ChrTalk(
        0xA,
        (
            "ＩＢＣへの影響も懸念されますが、\x01",
            "こうなると最早、株価がどうこうという\x01",
            "レベルの話ではありませんね。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0xA,
        (
            "とにかく、マインツの皆さんが\x01",
            "ご無事でいらっしゃることを祈ります。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8F8")

    Jump("loc_2022")

    label("loc_8FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_AB2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A18")

    #C0006
    ChrTalk(
        0xA,
        (
            "導力ネットというものは、\x01",
            "触れれば触れるほど\x01",
            "その魅力に気付かされますね。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0xA,
        (
            "コリンナは導力ゲームが\x01",
            "一番だと言いますが、\x01",
            "私のお気に入りは天気予報です。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0xA,
        (
            "流石に１００％ではありませんが、\x01",
            "結構当たるので毎日感心しながら\x01",
            "拝見させてもらっていますわ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_AAD")

    label("loc_A18")


    #C0009
    ChrTalk(
        0xA,
        (
            "導力ネットに流されている\x01",
            "天気予報は結構当たるんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0xA,
        (
            "ちなみに今日の予報は\x01",
            "『雨のち晴れ――午後には\x01",
            "　すっかり回復の見込み』だそうですよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AAD")

    Jump("loc_2022")

    label("loc_AB2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_C52")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BE9")

    #C0011
    ChrTalk(
        0xA,
        (
            "コリンナの端末操作の腕前……\x01",
            "というより導力ゲームの腕前は\x01",
            "社内でも１・２を争うほどでして。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0xA,
        (
            "時々、エプスタイン財団の方から\x01",
            "色々なゲームソフトウェアの\x01",
            "テスト依頼が来ることもあるんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0xA,
        (
            "まあ依頼と言っても、\x01",
            "業務時間外にできる範囲でやっている\x01",
            "有志的なものなんですけどね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_C4D")

    label("loc_BE9")


    #C0014
    ChrTalk(
        0xA,
        (
            "それにしても画面に向かって\x01",
            "あんなに楽しそうにできるなんて……\x01",
            "ふふ、ちょっぴり羨ましいですね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C4D")

    Jump("loc_2022")

    label("loc_C52")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_D82")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x177, 4)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CE3")

    #C0015
    ChrTalk(
        0xA,
        (
            "私どもにできることなら\x01",
            "何でも協力させていただきます。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0xA,
        (
            "また何かありましたら\x01",
            "遠慮なくお越しくださいませ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D7D")

    label("loc_CE3")


    #C0017
    ChrTalk(
        0xA,
        (
            "マリアベル総裁代行は\x01",
            "昨日無事に出張から\x01",
            "お戻りになられましたわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0xA,
        (
            "お戻りになられて早々、\x01",
            "今日は朝一番から各部門との\x01",
            "調整で大忙しではありますが。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D7D")

    Jump("loc_2022")

    label("loc_D82")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1738")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16D, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_169B")

    #C0019
    ChrTalk(
        0xA,
        (
            "あら、皆様。\x01",
            "マリアベル総裁代行なら\x01",
            "外国にご出張中ですが……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17C, 0)), scpexpr(EXPR_END)), "loc_E44")

    #C0020
    ChrTalk(
        0x101,
        (
            "#00005Fマリアベル“総裁代行”……\x02\x03",

            "#00003Fああ、確かクロスベルタイムズにも\x01",
            "載ってたっけ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E6D")

    label("loc_E44")


    #C0021
    ChrTalk(
        0x101,
        "#00005Fマリアベル“総裁代行”……？\x02",
    )

    CloseMessageWindow()

    label("loc_E6D")


    #C0022
    ChrTalk(
        0x102,
        (
            "#00100Fええ、おじさまの総裁業務を\x01",
            "取締役会が引き取ってから、\x01",
            "割とすぐ後に任命されたみたいね。\x02\x03",

            "#00104Fつまり今は実質、\x01",
            "ベルがＩＢＣのトップと言えるわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x104,
        (
            "#00306Fなんつうか、あの歳で\x01",
            "ついにそこまで、って感じだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x103,
        "#00200Fマリアベルさんなら頷けもしますが……\x02",
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x109,
        (
            "#10106Fうん。\x01",
            "改めて考えると、とんでもないよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x105,
        (
            "#10300Fそれで、彼女の仕事量も\x01",
            "これまでの比じゃないって\x01",
            "感じなのかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0xA,
        "ええ、当然そうなりますわね。\x02",
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0xA,
        (
            "お嬢様に負担が集中しすぎないよう\x01",
            "取締役会が一丸となって\x01",
            "サポートはしている状況ですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0xA,
        (
            "総裁代行という立場になられた以上、\x01",
            "あらゆる場所にお顔を見せる\x01",
            "必要がどうしても出てきますので。\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x101,
        (
            "#00003Fなるほど……\x01",
            "やはり相当忙しそうですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0xA,
        (
            "ちなみに、お嬢様は\x01",
            "本日の夜にはお戻りになる予定です。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0xA,
        (
            "とは言いましても、明日からはまた\x01",
            "各種会議や会談等でスケジュールは\x01",
            "みっちりと埋まっておりまして。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0xA,
        (
            "申し訳ありませんが、\x01",
            "お嬢様には当分\x01",
            "お会いになれないと思います。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7A, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_15F9")
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0034
    ChrTalk(
        0xA,
        (
            "そうですわ――\x01",
            "お嬢様より皆さんに\x01",
            "伝言がございました。\x02",
        )
    )

    CloseMessageWindow()
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0035
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "『マリアベルのアカウント』\x07\x00",
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x27, 6)
    OP_E4(0x3)

    #C0036
    ChrTalk(
        0x101,
        (
            "#00005Fこ、これは『ポムっと！』の\x01",
            "アカウント……！？\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x103,
        (
            "#00200Fマリアベルさんも\x01",
            "やっているんですね？\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0xA,
        (
            "#18C『フフ、このくらいは\x01",
            "  技術部に携わる者として\x01",
            "  当然の嗜みですわ。』\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0xA,
        (
            "#18C『是非、登録しておいて下さいね。\x01",
            "  わたくしの超絶スキルで\x01",
            "  コテンパンにして差し上げますわ。』\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0xA,
        "……だそうでございます。\x02",
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x109,
        "#10105Fえっと、今のは……\x02",
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x104,
        (
            "#00301Fまさか、ロイドたちの反応を\x01",
            "読んでやがったのか……？\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x102,
        (
            "#00106F……でしょうね。\x01",
            "ベルならやりかねないわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0xA,
        (
            "さすがはエリィお嬢様。\x01",
            "その通りでございますわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x105,
        (
            "#10304Fフフ、本当に大したものだね。\x02\x03",

            "#10302Fそれに、お姉さんの声マネも\x01",
            "なかなかだったよ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xA)

    #C0046
    ChrTalk(
        0xA,
        (
            "い、いえ……\x01",
            "出すぎた真似でした。\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0xA,
        (
            "……とりあえず、\x01",
            "伝言は以上となります。\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0xA,
        (
            "お嬢様は主張先でも\x01",
            "端末を離しませんので、\x01",
            "早速勝負を挑まれてはいかがでしょうか。\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x101,
        "#00012Fはは、そうですね。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1693")

    label("loc_15F9")


    #C0050
    ChrTalk(
        0x102,
        (
            "#00104Fええ、分かりました。\x02\x03",

            "#00100Fランフィさんの方からも\x01",
            "くれぐれも無理だけはしないよう\x01",
            "ベルに言ってあげて下さい。\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0xA,
        "ええ、かしこまりましたわ。\x02",
    )

    CloseMessageWindow()

    label("loc_1693")

    SetScenarioFlags(0x16D, 0)
    Jump("loc_1733")

    label("loc_169B")


    #C0052
    ChrTalk(
        0xA,
        (
            "マリアベル総裁代行は\x01",
            "本日の夜、出張からお戻りに\x01",
            "なられる予定なのですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0xA,
        (
            "申し訳ありませんが、\x01",
            "お嬢様には当分\x01",
            "お会いになれないと思いますわ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1733")

    Jump("loc_2022")

    label("loc_1738")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1AAE")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7A, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1905")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_185A")

    #C0054
    ChrTalk(
        0xA,
        (
            "今後はさらにビルのセキュリティ面を\x01",
            "強化していく必要がありそうですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0xA,
        (
            "とにかく、マリアベルお嬢様の\x01",
            "盗まれた人形を取り戻してくださって\x01",
            "ありがとうございました。\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0xA,
        (
            "また何かありましたら\x01",
            "いつでもいらっしゃってください。\x01",
            "皆様なら大歓迎ですわ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1900")

    label("loc_185A")


    #C0057
    ChrTalk(
        0xA,
        (
            "マリアベルお嬢様の\x01",
            "盗まれた人形を取り戻してくださって\x01",
            "ありがとうございました。\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0xA,
        (
            "また何かありましたら\x01",
            "いつでもいらっしゃってください。\x01",
            "皆様なら大歓迎ですわ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1900")

    Jump("loc_1AA9")

    label("loc_1905")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19F1")

    #C0059
    ChrTalk(
        0xA,
        (
            "その認証カードがあれば、\x01",
            "エレベーターを利用できます。\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0xA,
        (
            "前に皆様に渡した時と同様のフロアに\x01",
            "降りることが出来るはずです。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0xA,
        (
            "マリアベル様は１６階の総裁室で\x01",
            "お待ちしておりますので、\x01",
            "そちらへお越しくださいませ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1AA9")

    label("loc_19F1")


    #C0062
    ChrTalk(
        0xA,
        (
            "その認証カードがあれば、\x01",
            "前に皆様に渡した時と同様のフロアに\x01",
            "降りることが出来るはずです。\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0xA,
        (
            "マリアベル様は１６階の総裁室で\x01",
            "お待ちしておりますので、\x01",
            "そちらへお越しくださいませ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1AA9")

    Jump("loc_2022")

    label("loc_1AAE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1ABC")
    Jump("loc_2022")

    label("loc_1ABC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1E3F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14A, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1DC2")

    #C0064
    ChrTalk(
        0xA,
        (
            "あら、皆様。\x01",
            "ＩＢＣへようこそいらっしゃいました。\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0xA,
        (
            "何かご用がおありでしたら\x01",
            "なるべく本日中にお済ませ下さいね。\x01",
            "明日は臨時休行日となりますので。\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x101,
        "#00005F臨時休行日、ですか？\x02",
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x102,
        (
            "#00100F確か明日の午後、共和国の\x01",
            "ロックスミス大統領が\x01",
            "ＩＢＣを視察されるんですよね。\x02\x03",

            "やはり、そのためでしょうか？\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0xA,
        (
            "流石はエリィ様、お耳が早いですね。\x01",
            "ええ、仰る通りですわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0xA,
        (
            "何と仰いましても、\x01",
            "ロックスミス大統領はＶＩＰ中の\x01",
            "ＶＩＰでいらっしゃいますので。\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0xA,
        (
            "当日はビル内の企業関係者にも\x01",
            "一切出払ってもらった上で\x01",
            "万全の体制でお迎えする予定なんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x109,
        (
            "#10103Fなるほど、ミシュラム方面と\x01",
            "同等の対応というわけですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0x104,
        "#00306Fまあ、当然っちゃ当然だわな。\x02",
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0x101,
        "#00000Fとりあえず、事情は分かりました。\x02",
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x102,
        "#00100Fご丁寧にありがとうございます。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x14A, 7)
    Jump("loc_1E3A")

    label("loc_1DC2")


    #C0075
    ChrTalk(
        0xA,
        (
            "明日、ＩＢＣは\x01",
            "臨時休行日となっております。\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0xA,
        (
            "皆様、何かご用がおありでしたら\x01",
            "なるべく本日中にお済ませ下さいね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E3A")

    Jump("loc_2022")

    label("loc_1E3F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_1F84")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6C, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1EDA")

    #C0077
    ChrTalk(
        0xA,
        (
            "主任のご依頼の件が\x01",
            "無事に終了なさったみたいですね。\x01",
            "ふふ、お疲れ様でした。\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0xA,
        (
            "私の方からもお礼を\x01",
            "言わせていただきますね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F7F")

    label("loc_1EDA")


    #C0079
    ChrTalk(
        0xA,
        (
            "ロバーツ主任は、ＩＢＣビル内にある\x01",
            "エプスタイン財団支部でいつも\x01",
            "お忙しくしていらっしゃいます。\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0xA,
        (
            "私どもも導力ネット関係で\x01",
            "とてもお世話になっているんですよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F7F")

    Jump("loc_2022")

    label("loc_1F84")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_2022")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x134, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F9F")
    Call(0, 7)
    Jump("loc_2022")

    label("loc_1F9F")


    #C0081
    ChrTalk(
        0xA,
        (
            "特務支援課の皆様には\x01",
            "最大限の便宜を図るよう\x01",
            "承っておりますわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0xA,
        (
            "今後とも、何かございましたら\x01",
            "いつでもいらしてくださいね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2022")

    Return()

    # Function_6_71E end

    def Function_7_2023(): pass

    label("Function_7_2023")

    EventBegin(0x0)
    Fade(500)
    OP_68(-370, 1800, 29450, 0)
    MoveCamera(45, 14, 0, 0)
    OP_6E(590, 0)
    SetCameraDistance(14500, 0)
    SetChrPos(0x101, -770, 300, 29530, 0)
    SetChrPos(0x102, 430, 300, 29130, 0)
    SetChrPos(0x109, -1270, 300, 28130, 0)
    SetChrPos(0x105, 530, 300, 27920, 0)
    OP_4B(0xA, 0xFF)
    OP_93(0xA, 0xB4, 0x0)
    OP_0D()
    Sleep(100)
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0083
    ChrTalk(
        0xA,
        (
            "#5Pあら、ロイド様にエリィ様。\x01",
            "お久しぶりにございます。\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0xA,
        (
            "#5Pどうやらまた、特務支援課の\x01",
            "お仕事を再開されたようですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0x101,
        "#12P#00000Fええ、おかげ様で。\x02",
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x102,
        (
            "#12P#00100Fこれからも改めて\x01",
            "よろしくお願いしますね。\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0xA,
        "#5Pええ、もちろんですわ。\x02",
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2398")

    #C0088
    ChrTalk(
        0xA,
        (
            "#5Pそういえば以前、支援課の皆様に\x01",
            "新しい換金サービスの運用テストに\x01",
            "ご協力頂いたと思うのですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0xA,
        (
            "#5P実はその時にお渡ししたカードの\x01",
            "有効期限が切れてしまいまして。\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0xA,
        (
            "#5P新しくご用意致しましたので、\x01",
            "こちらをお受け取り下さいませ。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0091
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x326),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を受け取った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x326, 1)
    SetMessageWindowPos(14, 280, 60, 3)

    #C0092
    ChrTalk(
        0xA,
        (
            "#5Pこのカードを以前のように\x01",
            "受付にてご提示ください。\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0xA,
        (
            "#5P通常より高い換金率で\x01",
            "セピスをミラに換えさせて頂きます。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_250F")

    label("loc_2398")


    #C0094
    ChrTalk(
        0xA,
        (
            "#5Pそういえば、皆様に\x01",
            "お渡しするものがございました。\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0xA,
        "#5Pこちらをお受け取り下さいませ。\x02",
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
            scpstr(SCPSTR_CODE_ITEM, 0x326),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を受け取った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x326, 1)
    SetMessageWindowPos(14, 280, 60, 3)

    #C0097
    ChrTalk(
        0x101,
        "#12P#00005Fこのカードは……？\x02",
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0xA,
        (
            "#5Pはい、そちらは当銀行の\x01",
            "優待会員であることを\x01",
            "示すカードでございます。\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0xA,
        (
            "#5P受付にてご提示頂ければ、\x01",
            "通常より高い換金率で\x01",
            "セピスをミラに換えさせて頂きます。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_250F")


    #C0100
    ChrTalk(
        0x109,
        (
            "#12P#10105Fそ、そんなサービスを\x01",
            "私たちが受けてもいいんですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0xA,
        (
            "#5Pええ、皆様はクロイス市長、\x01",
            "並びにマリアベルお嬢様の\x01",
            "大切なご友人ですから。\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0xA,
        "#5P便宜を図るのは当然のことですわ。\x02",
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0x105,
        (
            "#12P#10302Fフフ、それじゃあありがたく\x01",
            "受けさせてもらおうかな。\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0x101,
        "#12P#00000F是非、今度利用させて頂きます。\x02",
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0xA,
        "#5Pふふ、お待ちしておりますわ。\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    Sound(814, 0, 100, 0)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0106
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※ＩＢＣの換金サービスが利用可能になりました。\x01",
            "　通常のショップメニューより、\x01",
            "　高レートでセピスを換金することができます。\x02\x03",

            "※ランフィに話しかけ、\x01",
            "　『セピス換金』を選んだ後\x01",
            "　<EXCHANGE>を選ぶと換金を行う事ができます。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_4C(0xA, 0xFF)
    OP_69(0xFF, 0x0)
    SetScenarioFlags(0x134, 4)
    EventEnd(0x5)
    Return()

    # Function_7_2023 end

    def Function_8_278A(): pass

    label("Function_8_278A")

    TalkBegin(0xFE)
    Call(0, 9)
    TalkEnd(0xFE)
    Return()

    # Function_8_278A end

    def Function_9_2794(): pass

    label("Function_9_2794")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2848")
    OP_4B(0xD, 0xFF)
    OP_4B(0xB, 0xFF)

    #C0107
    ChrTalk(
        0xB,
        (
            "少々お待ちくださいませー。\x01",
            "（カタカタ、カタタッ……！）\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0xB,
        (
            "ただいま、ご契約内容を\x01",
            "照会いたしますのでー。\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0xD,
        "うむ、よろしくお願いするぞ。\x02",
    )

    CloseMessageWindow()
    OP_4C(0xD, 0xFF)
    OP_4C(0xB, 0xFF)
    SetScenarioFlags(0x0, 3)
    Jump("loc_2900")

    label("loc_2848")

    OP_4B(0xD, 0xFF)
    OP_4B(0xB, 0xFF)
    TurnDirection(0xD, 0x0, 0)
    TurnDirection(0xB, 0x0, 0)

    #C0110
    ChrTalk(
        0xD,
        (
            "ん……何だね、君は？\x01",
            "まさか割り込む\x01",
            "つもりじゃないだろうな。\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0xB,
        (
            "申し訳ございません、\x01",
            "そちらのソファーで\x01",
            "順番をお待ちくださいませー。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xD, 0x0, 0x0)
    OP_93(0xB, 0x5A, 0x0)
    OP_4C(0xD, 0xFF)
    OP_4C(0xB, 0xFF)

    label("loc_2900")

    Return()

    # Function_9_2794 end

    def Function_10_2901(): pass

    label("Function_10_2901")

    Call(0, 11)
    Return()

    # Function_10_2901 end

    def Function_11_2905(): pass

    label("Function_11_2905")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_2916")
    Jump("loc_3779")

    label("loc_2916")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2924")
    Jump("loc_3779")

    label("loc_2924")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_2A64")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_29DE")

    #C0112
    ChrTalk(
        0xB,
        (
            "マインツを襲ったのは\x01",
            "相当危険な連中だそうですねー。\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0xB,
        (
            "正直、ウチの保安部でも\x01",
            "対処し切れないレベルとか……\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0xB,
        (
            "やれやれ、\x01",
            "笑えない話でございますねー。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_2A5F")

    label("loc_29DE")


    #C0115
    ChrTalk(
        0xB,
        (
            "マインツを襲った武装集団は\x01",
            "正直、ウチの保安部でも\x01",
            "対処し切れないレベルとか……\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0xB,
        (
            "やれやれ、\x01",
            "笑えない話でございますねー。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A5F")

    Jump("loc_3779")

    label("loc_2A64")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2AF7")

    #C0117
    ChrTalk(
        0xB,
        (
            "雨の日に外に出かけるのは\x01",
            "億劫ですよねー。\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0xB,
        (
            "導力ネットがもっと広まれば、\x01",
            "在宅でできる仕事にでも\x01",
            "就きたいものでございますー。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3779")

    label("loc_2AF7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_2FA3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D88")

    #C0119
    ChrTalk(
        0xB,
        "（カタカタカタ、カタタタッ……！）\x02",
    )

    Sound(836, 0, 100, 0)
    CloseMessageWindow()

    #C0120
    ChrTalk(
        0xB,
        "（チュイーン、ズッダダダダダンッ！）\x02",
    )

    Sound(449, 0, 100, 0)
    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B9E")

    #C0121
    ChrTalk(
        0x101,
        "#00005Fい、一体何の音だ……？\x02",
    )

    CloseMessageWindow()
    Jump("loc_2CDA")

    label("loc_2B9E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2BD4")

    #C0122
    ChrTalk(
        0x102,
        "#00105Fな、何の音かしら……？\x02",
    )

    CloseMessageWindow()
    Jump("loc_2CDA")

    label("loc_2BD4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C31")

    #C0123
    ChrTalk(
        0x103,
        (
            "#00203F……この音は、最近財団が開発した\x01",
            "シューティングゲームですね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2CDA")

    label("loc_2C31")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C71")

    #C0124
    ChrTalk(
        0x104,
        "#00305Fな、なんつう音を出してんだ……？\x02",
    )

    CloseMessageWindow()
    Jump("loc_2CDA")

    label("loc_2C71")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2CA5")

    #C0125
    ChrTalk(
        0x109,
        "#10105Fこ、これは銃声……？\x02",
    )

    CloseMessageWindow()
    Jump("loc_2CDA")

    label("loc_2CA5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2CDA")

    #C0126
    ChrTalk(
        0x105,
        "#10302Fフフ、何だか楽しそうだね。\x02",
    )

    CloseMessageWindow()

    label("loc_2CDA")

    Sleep(50)
    TurnDirection(0xB, 0x0, 0)

    #C0127
    ChrTalk(
        0xB,
        (
            "申し訳ありません、お客様ー。\x01",
            "こう見えて私、いまは\x01",
            "休憩時間の真っ最中でございまして。\x02",
        )
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0xB,
        (
            "ですので、各種ご相談は\x01",
            "正面受付にてお願い致しますー。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xB, 0x5A, 0x0)
    SetScenarioFlags(0x0, 3)
    Jump("loc_2F9E")

    label("loc_2D88")


    #C0129
    ChrTalk(
        0xB,
        "（カタカタカタ、カタタタッ……！）\x02",
    )

    Sound(836, 0, 100, 0)
    CloseMessageWindow()

    #C0130
    ChrTalk(
        0xB,
        "（キュイーン、ズドドドドドーッ！）\x02",
    )

    Sound(449, 0, 100, 0)
    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2E28")

    #C0131
    ChrTalk(
        0x101,
        "#00012F（す、凄く集中してるみたいだな……）\x02",
    )

    CloseMessageWindow()
    Jump("loc_2F9E")

    label("loc_2E28")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2E68")

    #C0132
    ChrTalk(
        0x102,
        "#00106F（お、お邪魔しちゃ悪そうね……）\x02",
    )

    CloseMessageWindow()
    Jump("loc_2F9E")

    label("loc_2E68")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2ED2")

    #C0133
    ChrTalk(
        0x103,
        (
            "#00205F（この切り返しは……！\x01",
            "  ……どうやら確実に\x01",
            "  ヨナより上手のようですね。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F9E")

    label("loc_2ED2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F16")

    #C0134
    ChrTalk(
        0x104,
        "#00306F（こりゃあ、邪魔しちゃ悪そうだな。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_2F9E")

    label("loc_2F16")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F63")

    #C0135
    ChrTalk(
        0x109,
        (
            "#10106F（も、物凄く\x01",
            "  集中しているみたいですね……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F9E")

    label("loc_2F63")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F9E")

    #C0136
    ChrTalk(
        0x105,
        "#10302F（フフ、見事な入りっぷりだね。）\x02",
    )

    CloseMessageWindow()

    label("loc_2F9E")

    Jump("loc_3779")

    label("loc_2FA3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_306B")

    #C0137
    ChrTalk(
        0xB,
        (
            "最近のマリアベルお嬢様は\x01",
            "あまりの忙しさに、昼食の時間も\x01",
            "ままならないようですねー。\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0xB,
        (
            "移動中に済まされることも多く、\x01",
            "常にブロックタイプの携帯食を\x01",
            "持ち歩いておられるそうですよー。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3779")

    label("loc_306B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3259")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_31D1")

    #C0139
    ChrTalk(
        0xB,
        (
            "市長による独立の提唱以降、\x01",
            "大陸の金融市場はかなり\x01",
            "揺れているみたいですねー。\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0xB,
        (
            "極端な偏りこそありませんが、\x01",
            "相場の売りと買いはどちらも\x01",
            "それぞれ純増傾向にありまして。\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0xB,
        (
            "その判断が正か否か……\x01",
            "全ては今後のクロスベル次第で\x01",
            "決まるというわけでございます。\x02",
        )
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0xB,
        (
            "いやはや、株価指数の変動は\x01",
            "そのまま人生模様というわけですねー。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3254")

    label("loc_31D1")


    #C0143
    ChrTalk(
        0xB,
        (
            "リゼロさんは過去の失敗を\x01",
            "反省してか、かなり慎重になって\x01",
            "おられるようですねー。\x02",
        )
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0xB,
        (
            "私個人的には\x01",
            "正しい判断だと思いますよー。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3254")

    Jump("loc_3779")

    label("loc_3259")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3401")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3375")

    #C0145
    ChrTalk(
        0xB,
        (
            "昨日は大統領訪問のために\x01",
            "仕事がお休みだったのですが。\x02",
        )
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0xB,
        (
            "警戒態勢の街へ出る気にもなれず、\x01",
            "気付けば一日ベッドの上で\x01",
            "過ごしてしまったのでございます。\x02",
        )
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0xB,
        (
            "それなりに英気は養えたのですが、\x01",
            "自宅に導力ネット端末があればと\x01",
            "つくづく思ってしまいましたねー。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_33FC")

    label("loc_3375")


    #C0148
    ChrTalk(
        0xB,
        (
            "昨日は自宅に\x01",
            "導力ネット端末があればと\x01",
            "つくづく思ってしまいましたねー。\x02",
        )
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0xB,
        (
            "そうすれば、日がな一日\x01",
            "導力ゲームに興じたのですがー。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_33FC")

    Jump("loc_3779")

    label("loc_3401")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_340F")
    Jump("loc_3779")

    label("loc_340F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3420")
    Call(0, 9)
    Jump("loc_3779")

    label("loc_3420")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_3529")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_34E1")

    #C0150
    ChrTalk(
        0xB,
        "（カタカタカタ、カタタタッ……！）\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x0, 500)

    #C0151
    ChrTalk(
        0xB,
        (
            "雨の日はやっぱり\x01",
            "お客さんが少なくなりますね。\x02",
        )
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0xB,
        (
            "溜まった事務処理を片付ける\x01",
            "絶好のチャンスでございますー。\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xB, 0x10)
    SetScenarioFlags(0x0, 3)
    Jump("loc_3524")

    label("loc_34E1")


    #C0153
    ChrTalk(
        0xB,
        (
            "たまにはこういう日もないと、\x01",
            "なかなか仕事が回りませんよねー。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3524")

    Jump("loc_3779")

    label("loc_3529")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_3779")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_36C5")

    #C0154
    ChrTalk(
        0xB,
        (
            "技術部による導力ネットワークの\x01",
            "第二次テストもようやく\x01",
            "初期段階クリアなのでございます。\x02",
        )
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0xB,
        (
            "簡単に言うと、より多くのデータを\x01",
            "より早く、より安全に、そして安定的に\x01",
            "送受信可能になったわけですねー。\x02",
        )
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0xB,
        (
            "おかげ様で、これまで社内専用だった\x01",
            "端末のいくつかも社外ネットワークへの\x01",
            "接続を段階的に開始したのですよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0xB,
        (
            "これぞ、マリアベルお嬢様率いる\x01",
            "技術部スタッフの底力ってヤツですねー。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3779")

    label("loc_36C5")


    #C0158
    ChrTalk(
        0xB,
        (
            "クロイス市長も\x01",
            "今回の二次テストの成果には\x01",
            "かなり助けられているみたいですねー。\x02",
        )
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0xB,
        (
            "機密性の低い書類に限ってですが、\x01",
            "既にバンバン導力ネットで\x01",
            "やり取りしているそうですからー。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3779")

    TalkEnd(0xB)
    Return()

    # Function_11_2905 end

    def Function_12_377D(): pass

    label("Function_12_377D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_378E")
    Jump("loc_4444")

    label("loc_378E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_379C")
    Jump("loc_4444")

    label("loc_379C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_3839")

    #C0160
    ChrTalk(
        0xFE,
        (
            "どうやら、マインツが\x01",
            "大変なことになっているようだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0xFE,
        (
            "まだ今の所は金融市場に\x01",
            "ほとんど影響は見られないが、\x01",
            "それも時間の問題だろうな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4444")

    label("loc_3839")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_39EC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3931")

    #C0162
    ChrTalk(
        0xFE,
        (
            "誰かが得をすれば、\x01",
            "一方で誰かが損をする……\x01",
            "相場の真理というヤツだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0xFE,
        (
            "そしてもう１つ……\x01",
            "相場の世界に“絶対”はない。\x02",
        )
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0xFE,
        (
            "もし投資を始めるつもりなら、\x01",
            "自己責任の取れる範囲内での\x01",
            "資金運用を強くオススメするぞ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_39E7")

    label("loc_3931")


    #C0165
    ChrTalk(
        0xFE,
        (
            "もし投資を始めるつもりなら、\x01",
            "自己責任の取れる範囲内での\x01",
            "資金運用を強くオススメするぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0xFE,
        (
            "相場の世界に絶対はないが……\x01",
            "身の丈を超えた行動には\x01",
            "絶対に不幸が伴うと私は思うんだ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_39E7")

    Jump("loc_4444")

    label("loc_39EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_3B18")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A9A")

    #C0167
    ChrTalk(
        0xFE,
        "な、なんだって……？\x02",
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0xFE,
        (
            "今朝あれほどの値を付けた\x01",
            "株がもうここまで\x01",
            "下がっているなんて……\x02",
        )
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0xFE,
        (
            "……これだから、\x01",
            "相場というやつは分からんよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_3B13")

    label("loc_3A9A")


    #C0170
    ChrTalk(
        0xFE,
        (
            "今朝あれほどの値を付けた\x01",
            "株がもうここまで\x01",
            "下がっているなんて……\x02",
        )
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0xFE,
        (
            "……これだから、\x01",
            "相場というやつは分からんよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3B13")

    Jump("loc_4444")

    label("loc_3B18")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3C3B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3BCE")

    #C0172
    ChrTalk(
        0xFE,
        (
            "ふむ、今朝は共和国方面で\x01",
            "値動きが見られるな。\x02",
        )
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0xFE,
        (
            "私が目を付けていた株も\x01",
            "買いだったようだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0xFE,
        (
            "今さら何を言っても、\x01",
            "ただの結果論に過ぎないな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_3C36")

    label("loc_3BCE")


    #C0175
    ChrTalk(
        0xFE,
        (
            "私が目を付けていた株は\x01",
            "買いだったようだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0xFE,
        (
            "今さら何を言っても、\x01",
            "ただの結果論に過ぎないな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3C36")

    Jump("loc_4444")

    label("loc_3C3B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3D8B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D18")

    #C0177
    ChrTalk(
        0xFE,
        (
            "やはり……この頃の\x01",
            "相場はかなり不安定のようだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0xFE,
        (
            "ふむ、ここまで揺れが断続的で\x01",
            "かつ読みにくい相場も珍しい。\x02",
        )
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0xFE,
        (
            "リスクも相当なもの……\x01",
            "間違っても素人は\x01",
            "手を出さない方がいいと思うぞ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_3D86")

    label("loc_3D18")


    #C0180
    ChrTalk(
        0xFE,
        (
            "以前の私ならリスクなど気にせず\x01",
            "飛び込んでいたところだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0xFE,
        (
            "ふむ、これは\x01",
            "手を出さない方が無難だな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3D86")

    Jump("loc_4444")

    label("loc_3D8B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3F09")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E69")

    #C0182
    ChrTalk(
        0xFE,
        (
            "貿易商として通商会議の行方は\x01",
            "いやでも気になる所だよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0xFE,
        (
            "とかく、帝国・共和国は、\x01",
            "隙あらば我を通そうとして来るからね。\x02",
        )
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0xFE,
        (
            "両国にどこまで譲歩を促せるか、\x01",
            "ディーター市長の腕の見せ所だな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_3F04")

    label("loc_3E69")


    #C0185
    ChrTalk(
        0xFE,
        (
            "こと貿易関連の協定に関して\x01",
            "帝国・共和国は、隙あらば\x01",
            "我を通そうとして来るからね。\x02",
        )
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0xFE,
        (
            "両国にどこまで譲歩を促せるか、\x01",
            "ディーター市長の腕の見せ所だな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3F04")

    Jump("loc_4444")

    label("loc_3F09")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3F17")
    Jump("loc_4444")

    label("loc_3F17")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_4051")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3FD6")

    #C0187
    ChrTalk(
        0xFE,
        (
            "通商会議の影響からか\x01",
            "ここ数日間は、平均株価の方も\x01",
            "上昇傾向にあるみたいだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0xFE,
        (
            "私の方でも買ってみたい\x01",
            "銘柄はあるんだが……\x01",
            "今の元手ではどうしようもないな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_404C")

    label("loc_3FD6")


    #C0189
    ChrTalk(
        0xFE,
        (
            "こうして相場を眺めていると、\x01",
            "株を買いたくなって来るんだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0xFE,
        (
            "ふぅ、しばらくは\x01",
            "地道に本業で稼ぐしかないか。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_404C")

    Jump("loc_4444")

    label("loc_4051")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_405F")
    Jump("loc_4444")

    label("loc_405F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_4444")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x134, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_43D8")
    OP_63(0xFE, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0191
    ChrTalk(
        0xFE,
        "おや、君は特務支援課の……\x02",
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0xFE,
        (
            "わ、私を覚えているかね？\x01",
            "例の教団事件で君たちに助けられた\x01",
            "貿易商をしている者だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0x101,
        "#00000Fええ、もちろんです。\x02",
    )

    CloseMessageWindow()

    #C0194
    ChrTalk(
        0x102,
        (
            "#00100Fあれから\x01",
            "お身体に変化はありませんか？\x02",
        )
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0xFE,
        (
            "ああ、今もウルスラ病院で\x01",
            "診てもらっているし、\x01",
            "この通り元気なものだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0xFE,
        (
            "事件の後、負債は抱えたものの\x01",
            "会社が潰れる程ではなかったし……\x02",
        )
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0xFE,
        (
            "あの時はどうもありがとう。\x01",
            "今でも本当に感謝しているよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0xFE,
        (
            "そうだ、よかったら\x01",
            "これを受け取ってくれないか。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0199
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1FC),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を受け取った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x1FC, 1)
    SetMessageWindowPos(14, 280, 60, 3)

    #C0200
    ChrTalk(
        0x101,
        "#00005Fこれは……\x02",
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0xFE,
        (
            "ああ、以前取引先から\x01",
            "もらった品なんだが、\x01",
            "私には使いようのない物でね。\x02",
        )
    )

    CloseMessageWindow()

    #C0202
    ChrTalk(
        0xFE,
        (
            "それに、君たちに少しでも\x01",
            "形あるもので恩を返したくてな。\x02",
        )
    )

    CloseMessageWindow()

    #C0203
    ChrTalk(
        0xFE,
        (
            "あくまで個人的な贈り物だから、\x01",
            "黙って受け取ってくれると嬉しい。\x02",
        )
    )

    CloseMessageWindow()

    #C0204
    ChrTalk(
        0x101,
        (
            "#00000F分かりました……\x01",
            "そういうことでしたら\x01",
            "ありがたく頂戴しておきます。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x134, 5)
    Jump("loc_4444")

    label("loc_43D8")


    #C0205
    ChrTalk(
        0xFE,
        (
            "君たちに、こうして\x01",
            "また会えて良かったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0206
    ChrTalk(
        0xFE,
        (
            "あの時はどうもありがとう。\x01",
            "今でも本当に感謝しているよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4444")

    TalkEnd(0xFE)
    Return()

    # Function_12_377D end

    def Function_13_4448(): pass

    label("Function_13_4448")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6C, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_472D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_46BA")

    #C0207
    ChrTalk(
        0xFE,
        (
            "『ポムっと！』を支援課の端末に\x01",
            "インストールしてみてくれ。\x02",
        )
    )

    CloseMessageWindow()

    #C0208
    ChrTalk(
        0xFE,
        (
            "そのあとエニグマで\x01",
            "連絡をくれるといいよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0209
    ChrTalk(
        0x101,
        (
            "#00000F分かりました、\x01",
            "あとで連絡します。\x02",
        )
    )

    CloseMessageWindow()

    #C0210
    ChrTalk(
        0x105,
        (
            "#10302Fところで、警察の端末に\x01",
            "ゲームとかを入れていいわけ？\x02",
        )
    )

    CloseMessageWindow()

    #C0211
    ChrTalk(
        0x101,
        (
            "#00005Fああ、そういえば……\x01",
            "許可を取る必要があるかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0212
    ChrTalk(
        0xFE,
        (
            "フフ、既に警察の方には\x01",
            "僕の方から許可を貰っているよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0213
    ChrTalk(
        0xFE,
        (
            "導力ネットを推進する\x01",
            "テストケースの一つって説明したら\x01",
            "あっさりと許可してくれてねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0214
    ChrTalk(
        0x101,
        "#00005Fそ、そうですか……\x02",
    )

    CloseMessageWindow()

    #C0215
    ChrTalk(
        0x109,
        "#10106F（な、何だか手際がいいですね。）\x02",
    )

    CloseMessageWindow()

    #C0216
    ChrTalk(
        0x102,
        (
            "#00100F（ふふ、一応クロスベルの\x01",
            "  導力ネットワーク関連の\x01",
            "  責任者みたいだから。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_4728")

    label("loc_46BA")


    #C0217
    ChrTalk(
        0xFE,
        (
            "『ポムっと！』を支援課の端末に\x01",
            "インストールしてみてくれ。\x02",
        )
    )

    CloseMessageWindow()

    #C0218
    ChrTalk(
        0xFE,
        (
            "そのあとエニグマで\x01",
            "連絡をくれるといいよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4728")

    Jump("loc_488A")

    label("loc_472D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4803")

    #C0219
    ChrTalk(
        0xFE,
        (
            "『ポムっと！』のテスト、\x01",
            "付き合ってくれて感謝するよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0220
    ChrTalk(
        0xFE,
        (
            "正式に普及が始まったら、\x01",
            "いろんな人に声をかけて\x01",
            "アカウントを集めるといい。\x02",
        )
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0xFE,
        (
            "そうして輪を広げるのが\x01",
            "そのゲームの醍醐味だからね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_488A")

    label("loc_4803")


    #C0222
    ChrTalk(
        0xFE,
        (
            "正式に『ポムっと！』の\x01",
            "普及が始まったら、\x01",
            "沢山アカウントを集めるといい。\x02",
        )
    )

    CloseMessageWindow()

    #C0223
    ChrTalk(
        0xFE,
        (
            "そうして輪を広げるのが\x01",
            "そのゲームの醍醐味だからね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_488A")

    TalkEnd(0xFE)
    Return()

    # Function_13_4448 end

    def Function_14_488E(): pass

    label("Function_14_488E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_489F")
    Jump("loc_54AB")

    label("loc_489F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_48AD")
    Jump("loc_54AB")

    label("loc_48AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_4955")

    #C0224
    ChrTalk(
        0xFE,
        (
            "何でも武装集団は、\x01",
            "警備隊をも圧倒する火力を\x01",
            "備えているらしいな。\x02",
        )
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0xFE,
        (
            "正体は、悪名高き猟兵団\x01",
            "《赤い星座》だと聞いたが……\x01",
            "これからどう出るつもりだ？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_54AB")

    label("loc_4955")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_49C0")

    #C0226
    ChrTalk(
        0xFE,
        "何だか、朝から忙しそうだな。\x02",
    )

    CloseMessageWindow()

    #C0227
    ChrTalk(
        0xFE,
        (
            "色々大変だとは思うが、\x01",
            "あまり気張り過ぎないようにな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_54AB")

    label("loc_49C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_4B1C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4AAA")

    #C0228
    ChrTalk(
        0xFE,
        "さてと、そろそろ昼の交代時間か。\x02",
    )

    CloseMessageWindow()

    #C0229
    ChrTalk(
        0xFE,
        (
            "ふむ、何を食べようか。\x01",
            "今日のＡランチは肉料理らしいが……\x02",
        )
    )

    CloseMessageWindow()

    #C0230
    ChrTalk(
        0xFE,
        (
            "……ごほん、いかんいかん。\x01",
            "まだ休憩時間に\x01",
            "なったわけじゃないんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0xFE,
        "全く、たるんでいる証拠だな。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_4B17")

    label("loc_4AAA")


    #C0232
    ChrTalk(
        0xFE,
        (
            "飯時が近づくと、どうにも思考が\x01",
            "食欲の方ばかりに向かっていかんな。\x02",
        )
    )

    CloseMessageWindow()

    #C0233
    ChrTalk(
        0xFE,
        "ふう、俺もまだまだ訓練不足だな。\x02",
    )

    CloseMessageWindow()

    label("loc_4B17")

    Jump("loc_54AB")

    label("loc_4B1C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_4CBA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4C1C")

    #C0234
    ChrTalk(
        0xFE,
        (
            "何でも最近、自治州内に\x01",
            "得体の知れない化物が\x01",
            "現れるようになったらしいな。\x02",
        )
    )

    CloseMessageWindow()

    #C0235
    ChrTalk(
        0xFE,
        (
            "我々保安部は対人のみならず\x01",
            "魔獣との戦闘についても\x01",
            "ある程度の心得があるのだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0236
    ChrTalk(
        0xFE,
        (
            "ふむ、万が一の事態に備えて\x01",
            "あらゆる心構えをしておかんとな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_4CB5")

    label("loc_4C1C")


    #C0237
    ChrTalk(
        0xFE,
        (
            "俺たち保安部は対人のみならず\x01",
            "魔獣との戦闘についても\x01",
            "ある程度の心得があるのだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0238
    ChrTalk(
        0xFE,
        (
            "ふむ、万が一の事態に備えて\x01",
            "あらゆる心構えをしておかんとな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4CB5")

    Jump("loc_54AB")

    label("loc_4CBA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_4ED7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4E47")

    #C0239
    ChrTalk(
        0xFE,
        (
            "このＩＢＣビルには社員専用の\x01",
            "トレーニングルームがあってな。\x02",
        )
    )

    CloseMessageWindow()

    #C0240
    ChrTalk(
        0xFE,
        (
            "我々ＩＢＣ保安部はもちろん、\x01",
            "運動不足の社員などにも\x01",
            "積極的に活用されているのだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0241
    ChrTalk(
        0xFE,
        (
            "ちなみに最近は機会が減ったが、\x01",
            "マリアベルお嬢様を\x01",
            "見かけることも結構あってな。\x02",
        )
    )

    CloseMessageWindow()

    #C0242
    ChrTalk(
        0xFE,
        (
            "普段は決してお目にかかれない\x01",
            "トレーニングウェア姿で\x01",
            "汗を流されて行くんだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0243
    ChrTalk(
        0xFE,
        (
            "何と言うか……\x01",
            "あれにはドキドキさせられるぞ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_4ED2")

    label("loc_4E47")


    #C0244
    ChrTalk(
        0xFE,
        (
            "コ、コホン……最後は少し\x01",
            "余計な事を喋ってしまったな。\x02",
        )
    )

    CloseMessageWindow()

    #C0245
    ChrTalk(
        0xFE,
        (
            "と、とにかく、我が社の\x01",
            "トレーニングルームは\x01",
            "施設が充実していて最高なのだ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4ED2")

    Jump("loc_54AB")

    label("loc_4ED7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_512C")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7A, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4FE7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4F8A")

    #C0246
    ChrTalk(
        0xFE,
        (
            "マリアベルお嬢様の部屋に\x01",
            "賊が入ったらしい……\x02",
        )
    )

    CloseMessageWindow()

    #C0247
    ChrTalk(
        0xFE,
        (
            "くっ、不審者の類は見かけて\x01",
            "いないはずだったのだが……\x01",
            "まんまと騙されたという事か。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_4FE2")

    label("loc_4F8A")


    #C0248
    ChrTalk(
        0xFE,
        (
            "くっ、不審者の類は見かけて\x01",
            "いないはずだったのだが……\x01",
            "まんまと騙されたという事か。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4FE2")

    Jump("loc_5127")

    label("loc_4FE7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_50BB")

    #C0249
    ChrTalk(
        0xFE,
        (
            "お嬢様の大切な人形を\x01",
            "取り返してくれてありがとう。\x01",
            "俺からも礼を言わせてもらうぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0250
    ChrTalk(
        0xFE,
        (
            "それにしても、俺たち保安部に\x01",
            "気配すら悟らせないとは……\x02",
        )
    )

    CloseMessageWindow()

    #C0251
    ChrTalk(
        0xFE,
        (
            "怪盗Ｂは一体\x01",
            "どういう手口を使ったんだ！？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_5127")

    label("loc_50BB")


    #C0252
    ChrTalk(
        0xFE,
        (
            "それにしても、俺たち保安部に\x01",
            "気配すら悟らせないとは……\x02",
        )
    )

    CloseMessageWindow()

    #C0253
    ChrTalk(
        0xFE,
        (
            "怪盗Ｂは一体\x01",
            "どういう手口を使ったんだ！？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5127")

    Jump("loc_54AB")

    label("loc_512C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_513A")
    Jump("loc_54AB")

    label("loc_513A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_52B5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_523C")

    #C0254
    ChrTalk(
        0xFE,
        (
            "通商会議を前に、\x01",
            "警察と警備隊による警戒活動が\x01",
            "いよいよ本格化してきたな。\x02",
        )
    )

    CloseMessageWindow()

    #C0255
    ChrTalk(
        0xFE,
        (
            "我がＩＢＣ保安部の方でも\x01",
            "それらの警戒活動には全面的に\x01",
            "協力することになっていてな。\x02",
        )
    )

    CloseMessageWindow()

    #C0256
    ChrTalk(
        0xFE,
        (
            "警察の警備対策本部とも綿密に\x01",
            "連絡を取らせてもらっているぞ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_52B0")

    label("loc_523C")


    #C0257
    ChrTalk(
        0xFE,
        (
            "何といっても、こういう時は\x01",
            "お互い助け合いだからな。\x02",
        )
    )

    CloseMessageWindow()

    #C0258
    ChrTalk(
        0xFE,
        (
            "我々に出来ることがあれば、\x01",
            "何でも協力するつもりだぞ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_52B0")

    Jump("loc_54AB")

    label("loc_52B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_535C")

    #C0259
    ChrTalk(
        0xFE,
        (
            "ふむ、我らがクロイス市長は\x01",
            "やはり相当お忙しいご様子だな。\x02",
        )
    )

    CloseMessageWindow()

    #C0260
    ChrTalk(
        0xFE,
        (
            "それでも何とかこなせているのは\x01",
            "マリアベルお嬢様の協力の\x01",
            "おかげに他ならないと思うぞ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_54AB")

    label("loc_535C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_54AB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5435")

    #C0261
    ChrTalk(
        0xFE,
        (
            "おや、確か君たちは\x01",
            "警察の特務支援課だったか。\x02",
        )
    )

    CloseMessageWindow()

    #C0262
    ChrTalk(
        0xFE,
        (
            "ようこそＩＢＣへ。\x01",
            "ビル内の保全に関する事なら\x01",
            "俺たち保安部に任せてくれよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0263
    ChrTalk(
        0xFE,
        (
            "ウチには警備隊にも負けない\x01",
            "体力自慢が揃ってるからな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_54AB")

    label("loc_5435")


    #C0264
    ChrTalk(
        0xFE,
        (
            "ビル内の保全に関する事なら\x01",
            "俺たち保安部に任せてくれ。\x02",
        )
    )

    CloseMessageWindow()

    #C0265
    ChrTalk(
        0xFE,
        (
            "ウチには警備隊にも負けない\x01",
            "体力自慢が揃ってるからな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_54AB")

    TalkEnd(0xFE)
    Return()

    # Function_14_488E end

    def Function_15_54AF(): pass

    label("Function_15_54AF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_54C0")
    Jump("loc_5FD4")

    label("loc_54C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_54CE")
    Jump("loc_5FD4")

    label("loc_54CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_5577")

    #C0266
    ChrTalk(
        0xFE,
        (
            "武装集団は、まだ何も具体的な\x01",
            "要求をして来ないんだそうですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0267
    ChrTalk(
        0xFE,
        (
            "保安部内でも、既に色々な\x01",
            "推測が飛び交っていますが……\x01",
            "不気味で仕方がありませんよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5FD4")

    label("loc_5577")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_55EC")

    #C0268
    ChrTalk(
        0xFE,
        "皆さん、本日もお仕事お疲れ様です。\x02",
    )

    CloseMessageWindow()

    #C0269
    ChrTalk(
        0xFE,
        (
            "外はあいにくの雨ですが、\x01",
            "どうか体調にはお気を付け下さい。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5FD4")

    label("loc_55EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_56B0")

    #C0270
    ChrTalk(
        0xFE,
        (
            "最近、このＩＢＣビルで\x01",
            "ディーター市長をお見かけする\x01",
            "機会がほとんどなくなりました。\x02",
        )
    )

    CloseMessageWindow()

    #C0271
    ChrTalk(
        0xFE,
        (
            "市長のことなのでお元気に\x01",
            "されている事とは思いますが……\x01",
            "お顔が見れないと少し心配ですね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5FD4")

    label("loc_56B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_5831")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_57AE")

    #C0272
    ChrTalk(
        0xFE,
        (
            "通商会議を襲った\x01",
            "共和国系テロリストの残党が\x01",
            "昨日、捕まったらしいですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0273
    ChrTalk(
        0xFE,
        (
            "何でも列車で共和国に\x01",
            "戻ろうとしていた所を発見され、\x01",
            "一騒動あったらしいですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0274
    ChrTalk(
        0xFE,
        (
            "そんな列車に乗り合わせた\x01",
            "お客さんは、本当に災難ですよね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_582C")

    label("loc_57AE")


    #C0275
    ChrTalk(
        0xFE,
        (
            "何でもテロリストの残党は\x01",
            "列車内で発見されたそうですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0276
    ChrTalk(
        0xFE,
        (
            "そんな列車に乗り合わせた\x01",
            "お客さんは、本当に災難ですよね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_582C")

    Jump("loc_5FD4")

    label("loc_5831")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_59DE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5953")

    #C0277
    ChrTalk(
        0xFE,
        (
            "帝国・共和国系テロリストによる\x01",
            "通商会議の襲撃事件から\x01",
            "早くも１ヶ月以上が経ちましたね。\x02",
        )
    )

    CloseMessageWindow()

    #C0278
    ChrTalk(
        0xFE,
        (
            "実行犯の何名かは未だに\x01",
            "捕まっていないとも聞きましたが……\x02",
        )
    )

    CloseMessageWindow()

    #C0279
    ChrTalk(
        0xFE,
        (
            "そう簡単に帰国も出来ないでしょうし、\x01",
            "もしかすると、今も自治州内に\x01",
            "潜伏でもしているのかもしれませんね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_59D9")

    label("loc_5953")


    #C0280
    ChrTalk(
        0xFE,
        (
            "実行犯の何名かは未だに\x01",
            "捕まっていないとも聞きましたが……\x02",
        )
    )

    CloseMessageWindow()

    #C0281
    ChrTalk(
        0xFE,
        (
            "もしかすると、今も自治州内に\x01",
            "潜伏でもしているのかもしれませんね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_59D9")

    Jump("loc_5FD4")

    label("loc_59DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_5BB2")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7A, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5A53")

    #C0282
    ChrTalk(
        0xFE,
        (
            "あ、ＩＢＣに盗賊なんて……\x01",
            "このセキュリティシステムを\x01",
            "かいくぐって一体どうやって……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5BAD")

    label("loc_5A53")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5B28")

    #C0283
    ChrTalk(
        0xFE,
        (
            "盗難事件を解決して下さって\x01",
            "本当にありがとうございます。\x02",
        )
    )

    CloseMessageWindow()

    #C0284
    ChrTalk(
        0xFE,
        (
            "いくら怪盗Ｂとは言え、\x01",
            "犯人が捕まらなかったのは\x01",
            "残念ですけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0285
    ChrTalk(
        0xFE,
        (
            "それでも、結果的には\x01",
            "何も被害がなくて\x01",
            "本当に安心しました。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_5BAD")

    label("loc_5B28")


    #C0286
    ChrTalk(
        0xFE,
        (
            "それにしても、今回の事件って\x01",
            "完全に愉快犯ですよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0287
    ChrTalk(
        0xFE,
        (
            "盗品が戻ってきたのは\x01",
            "御の字ですが……\x01",
            "ますます謎が深まった気がします。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5BAD")

    Jump("loc_5FD4")

    label("loc_5BB2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_5BC0")
    Jump("loc_5FD4")

    label("loc_5BC0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_5D20")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5C90")

    #C0288
    ChrTalk(
        0xFE,
        (
            "明日の午後、共和国大統領が\x01",
            "このＩＢＣビルを\x01",
            "ご視察される予定なんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0289
    ChrTalk(
        0xFE,
        (
            "それに伴い、僕たち保安部は\x01",
            "ほぼ総出で警備に当たる予定でして。\x02",
        )
    )

    CloseMessageWindow()

    #C0290
    ChrTalk(
        0xFE,
        "……何だか早くも緊張してきます。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_5D1B")

    label("loc_5C90")


    #C0291
    ChrTalk(
        0xFE,
        (
            "明日の午後、共和国大統領が\x01",
            "このＩＢＣビルを\x01",
            "ご視察される予定なんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0292
    ChrTalk(
        0xFE,
        (
            "当日の警備のことを思うと……\x01",
            "何だか早くも緊張してきます。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5D1B")

    Jump("loc_5FD4")

    label("loc_5D20")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_5EA1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5E01")

    #C0293
    ChrTalk(
        0xFE,
        (
            "ディーター市長とマリアベルさん、\x01",
            "今は以前にも増して\x01",
            "猛烈にお忙しいみたいですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0294
    ChrTalk(
        0xFE,
        (
            "でも、お２人はそんな中でも\x01",
            "周りへの気遣いや\x01",
            "笑顔を決して忘れないんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0295
    ChrTalk(
        0xFE,
        "本当に凄い事だと思いますよ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_5E9C")

    label("loc_5E01")


    #C0296
    ChrTalk(
        0xFE,
        (
            "僕なんかだと、忙しくなると\x01",
            "周りの事を気遣ってる余裕なんて\x01",
            "絶対に持てないですからね。\x02",
        )
    )

    CloseMessageWindow()

    #C0297
    ChrTalk(
        0xFE,
        (
            "その一点だけを取ってみても、\x01",
            "お２人は物凄くご立派ですよね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5E9C")

    Jump("loc_5FD4")

    label("loc_5EA1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_5FD4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5F53")

    #C0298
    ChrTalk(
        0xFE,
        (
            "いらっしゃいませ。\x01",
            "クロスベル国際銀行へようこそ。\x02",
        )
    )

    CloseMessageWindow()

    #C0299
    ChrTalk(
        0xFE,
        (
            "自分は警備担当ですが、\x01",
            "簡単な案内くらいなら出来ますよ。\x01",
            "本日はどのようなご要件でしょうか？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_5FD4")

    label("loc_5F53")


    #C0300
    ChrTalk(
        0xFE,
        (
            "いらっしゃいませ。\x01",
            "クロスベル国際銀行へようこそ。\x02",
        )
    )

    CloseMessageWindow()

    #C0301
    ChrTalk(
        0xFE,
        (
            "各種銀行手続きでしたら\x01",
            "正面と右手受付、どちらでも\x01",
            "ご対応できますよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5FD4")

    TalkEnd(0xFE)
    Return()

    # Function_15_54AF end

    def Function_16_5FD8(): pass

    label("Function_16_5FD8")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-640, 1800, 4860, 0)
    MoveCamera(57, 26, 0, 0)
    OP_6E(590, 0)
    SetCameraDistance(15390, 0)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu02900.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu02800.itp")
    SetChrPos(0x101, -610, 300, 2900, 0)
    SetChrPos(0x102, 760, 300, 2650, 0)
    SetChrPos(0x109, -610, 300, 2900, 0)
    SetChrPos(0x105, 760, 300, 2650, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    LoadChrToIndex("chr/ch05600.itc", 0x1E)
    LoadChrToIndex("chr/ch05500.itc", 0x1F)
    LoadChrToIndex("apl/ch51116.itc", 0x20)
    SetChrChipByIndex(0x10, 0x1E)
    SetChrChipByIndex(0x11, 0x1F)
    SetChrSubChip(0x10, 0x0)
    SetChrSubChip(0x11, 0x0)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x10, 0x8000)
    SetChrFlags(0x11, 0x8000)
    SetChrPos(0x10, -610, 300, 24300, 180)
    SetChrPos(0x11, 760, 300, 24800, 180)
    FadeToBright(1000, 0)
    OP_0D()
    Sound(107, 0, 100, 0)
    OP_68(-900, 1800, 5640, 3000)

    def lambda_6156():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6156)

    def lambda_6167():
        OP_98(0x101, 0x0, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6167)
    Sleep(50)

    def lambda_6184():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_6184)

    def lambda_6195():
        OP_98(0x102, 0x0, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6195)
    Sleep(700)

    def lambda_61B2():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_61B2)

    def lambda_61C3():
        OP_98(0x109, 0x0, 0x0, 0x9C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_61C3)
    Sleep(50)

    def lambda_61E0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_61E0)

    def lambda_61F1():
        OP_98(0x105, 0x0, 0x0, 0x9C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_61F1)
    WaitChrThread(0x105, 1)
    OP_6F(0x1)

    #C0302
    ChrTalk(
        0x101,
        (
            "#6P#00000Fさてと、ロバーツ主任からの\x01",
            "依頼が入っていたな。\x02",
        )
    )

    CloseMessageWindow()

    #C0303
    ChrTalk(
        0x102,
        (
            "#11P#00100Fええ、早速、受付のランフィさんに\x01",
            "取り次いでもらいましょうか。\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0x7D0)

    #N0304
    NpcTalk(
        0x10,
        "男性の声",
        "おや、諸君は……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7111", 0)
    OP_68(-1430, 1800, 8130, 3000)
    MoveCamera(45, 23, 0, 3000)
    OP_6E(590, 3000)
    SetCameraDistance(15440, 3000)

    def lambda_634C():
        OP_98(0xFE, 0x0, 0x0, 0xFFFFE4A8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_634C)
    Sleep(50)

    def lambda_6369():
        OP_98(0xFE, 0x0, 0x0, 0xFFFFE4A8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_6369)
    WaitChrThread(0x11, 1)
    OP_6F(0x79)

    #C0305
    ChrTalk(
        0x109,
        "#12P#10105Fディーター市長！\x02",
    )

    CloseMessageWindow()

    #C0306
    ChrTalk(
        0x101,
        "#12P#00000Fそれに、マリアベルさん。\x02",
    )

    CloseMessageWindow()
    OP_68(-330, 1700, 14870, 5000)
    MoveCamera(43, 22, 0, 5000)
    OP_6E(590, 5000)
    SetCameraDistance(13820, 5000)

    def lambda_6401():
        OP_98(0x101, 0x0, 0x0, 0x1F40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6401)
    Sleep(50)

    def lambda_641E():
        OP_98(0x102, 0x0, 0x0, 0x1F40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_641E)
    Sleep(50)

    def lambda_643B():
        OP_98(0x109, 0x0, 0x0, 0x1DB0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_643B)
    Sleep(50)

    def lambda_6458():
        OP_98(0x105, 0x0, 0x0, 0x1DB0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_6458)
    WaitChrThread(0x105, 1)
    OP_6F(0x79)

    #C0307
    ChrTalk(
        0x109,
        (
            "#12P#10100F今日はＩＢＣの方に\x01",
            "いらしていたんですね？\x02",
        )
    )

    CloseMessageWindow()

    #C0308
    ChrTalk(
        0x10,
        (
            "#02800Fああ、銀行での仕事が\x01",
            "随分溜まっていたのでね。\x02\x03",

            "#02804Fベルに手伝って貰いつつ、\x01",
            "ついさっき一通りの仕事を\x01",
            "済ませてきた所なのだよ。\x02",
        )
    )

    CloseMessageWindow()
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0309
    AnonymousTalk(
        0x11,
        (
            "うふふ、皆さん……\x01",
            "こうして顔を突き合せるのも\x01",
            "なんだか久しぶりですわね。\x02\x03",

            "エリィも、元気にしていたかしら？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    #C0310
    ChrTalk(
        0x102,
        (
            "#12P#00109Fふふ、おかげさまで先日、\x01",
            "支援課も再始動したところよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0311
    ChrTalk(
        0x11,
        "#5P#02905Fふむ、どれどれ……\x02",
    )

    CloseMessageWindow()
    OP_68(-330, 1500, 14870, 2000)
    MoveCamera(44, 26, 0, 2000)
    OP_6E(590, 2000)
    SetCameraDistance(14510, 2000)

    def lambda_66B9():

        label("loc_66B9")

        TurnDirection(0xFE, 0x11, 500)
        Yield()
        Jump("loc_66B9")

    QueueWorkItem2(0x101, 1, lambda_66B9)
    Sleep(50)

    def lambda_66CE():

        label("loc_66CE")

        TurnDirection(0xFE, 0x11, 500)
        Yield()
        Jump("loc_66CE")

    QueueWorkItem2(0x109, 1, lambda_66CE)
    Sleep(50)

    def lambda_66E3():

        label("loc_66E3")

        TurnDirection(0xFE, 0x11, 500)
        Yield()
        Jump("loc_66E3")

    QueueWorkItem2(0x105, 1, lambda_66E3)
    OP_99(0x11, 0x102, 0x1F4, 0x7D0, 0x0)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x109, 0x1)
    EndChrThread(0x105, 0x1)
    Fade(500)
    Sound(898, 0, 100, 0)
    SetChrChipByIndex(0x102, 0x20)
    SetChrChipByIndex(0x11, 0x20)
    SetChrSubChip(0x102, 0x1)
    SetChrSubChip(0x11, 0x3)
    SetChrFlags(0x102, 0x2)
    SetChrFlags(0x11, 0x2)
    SetChrPos(0x102, 760, 300, 14650, 180)
    SetChrPos(0x11, 760, 300, 15150, 180)

    #C0312
    ChrTalk(
        0x109,
        "#12P#10111Fわわっ……\x02",
    )

    CloseMessageWindow()

    #C0313
    ChrTalk(
        0x105,
        "#12P#10309Fヒュウ♪\x02",
    )

    CloseMessageWindow()

    def lambda_678A():
        OP_A6(0xFE, 0x0, 0x1E, 0x1F4, 0x7D0)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_678A)
    OP_63(0x102, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x102)

    #C0314
    ChrTalk(
        0x102,
        "#12P#00112Fちょ、ちょっとベル……\x02",
    )

    CloseMessageWindow()

    #C0315
    ChrTalk(
        0x11,
        (
            "#5P#02902Fふむふむ、健康状態は\x01",
            "良好のようですわね。\x02\x03",

            "#02904Fこの柔らかく暖かな感触、\x01",
            "肢体の下に確かに感じる\x01",
            "しなやかな筋肉の手応え……\x02\x03",

            "#02909Fう～ん、たまりませんわ㈱\x02",
        )
    )

    CloseMessageWindow()

    #C0316
    ChrTalk(
        0x102,
        (
            "#12P#00113Fも、もう……！\x01",
            "いちいちいかがわしい言い方を\x01",
            "しないでちょうだい！\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x102, 0x0)
    SetChrSubChip(0x11, 0x2)
    Sleep(500)
    ClearChrFlags(0x102, 0x2)
    ClearChrFlags(0x11, 0x2)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x11, 0x1F)
    SetChrSubChip(0x11, 0x0)
    TurnDirection(0x102, 0x11, 0)

    def lambda_690C():
        OP_9B(0x1, 0xFE, 0xB4, 0x1F4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_690C)
    Sleep(50)

    def lambda_6924():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6924)
    Sleep(1000)
    TurnDirection(0x11, 0x101, 500)
    Sleep(300)

    #C0317
    ChrTalk(
        0x11,
        (
            "#11P#02904Fところでロイドさん……\x02\x03",

            "#02901Fわたくしに何の断りもなく、\x01",
            "エリィにちょっかいを\x01",
            "出してませんわね？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0318
    ChrTalk(
        0x101,
        "#6P#00012Fあ、会っていきなりそれですか？\x02",
    )

    CloseMessageWindow()

    #C0319
    ChrTalk(
        0x11,
        (
            "#11P#02903Fロイドさんは危険人物ですし、\x01",
            "定期チェックは当然のことですわ。\x02\x03",

            "#02901Fもしそのような行動をとったことが\x01",
            "発覚した場合……分かっていますわね？\x02",
        )
    )

    CloseMessageWindow()

    #C0320
    ChrTalk(
        0x101,
        "#6P#00011Fうっ……\x02",
    )

    CloseMessageWindow()

    #C0321
    ChrTalk(
        0x105,
        "#12P#10309Fアハハ、警戒されてるねぇ。\x02",
    )

    CloseMessageWindow()

    #C0322
    ChrTalk(
        0x102,
        "#11P#00106Fもう、ベルったら……\x02",
    )

    CloseMessageWindow()

    #C0323
    ChrTalk(
        0x10,
        (
            "#5P#02806Fやれやれ、ベル。\x01",
            "折角久しぶりに会ったのだから\x01",
            "もう少し自重したまえ。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_6B51():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6B51)
    Sleep(50)

    def lambda_6B61():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_6B61)
    Sleep(50)

    def lambda_6B71():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_6B71)
    Sleep(50)

    def lambda_6B81():
        TurnDirection(0xFE, 0x10, 500)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_6B81)
    Sleep(300)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0324
    AnonymousTalk(
        0x10,
        (
            "改めて久しぶりだね、諸君。\x02\x03",

            "新メンバーのノエル君とワジ君も\x01",
            "馴染んでいるようでなによりだ。\x02\x03",

            "特務支援課の再始動、\x01",
            "この場を借りて祝わせて頂こう。\x02",
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

    #C0325
    ChrTalk(
        0x105,
        (
            "#12P#10300Fフフ、その節はどうも。\x02\x03",

            "#10309F支援課への推薦の件、\x01",
            "改めて礼を言わせて貰うよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0326
    ChrTalk(
        0x109,
        (
            "#12P#10109F導力車の支給の件も\x01",
            "ありがとうございました！\x02\x03",

            "#10104Fあんな素敵な導力車を\x01",
            "運転できるなんて、\x01",
            "夢みたいですよ！\x02",
        )
    )

    CloseMessageWindow()

    #C0327
    ChrTalk(
        0x10,
        (
            "#5P#02809Fハハ、君たちの\x01",
            "役に立てたなら幸いだ。\x02\x03",

            "#02800F私も新市長となった甲斐が\x01",
            "あったというものだよ。\x02\x03",

            "#02806F市長とＩＢＣ総裁……\x01",
            "この２つを両立させるのは\x01",
            "なかなか難儀だがね。\x02",
        )
    )

    CloseMessageWindow()

    #C0328
    ChrTalk(
        0x11,
        (
            "#11P#02906Fまあ、お父様の場合\x01",
            "お忙しいのはほとんど\x01",
            "ご自分のせいでしょうけど。\x02\x03",

            "#02900F何でもかんでも引き受けてきて、\x01",
            "手伝わされるこちらの身にも\x01",
            "なってほしいものですわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0329
    ChrTalk(
        0x10,
        (
            "#5P#02804Fハハ、すまないベル。\x01",
            "クロスベルのためを思うと\x01",
            "手の抜き所が分からなくてね。\x02\x03",

            "#02800Fついつい身の丈以上の仕事を\x01",
            "引き受けてしまいがちなのだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0330
    ChrTalk(
        0x102,
        (
            "#12P#00100Fふふ、おじいさまも\x01",
            "おじさまのバイタリティには\x01",
            "感心していらっしゃるみたいです。\x02\x03",

            "#00104F『彼のような若い政治家こそ\x01",
            "  今のクロスベルに必要なのだ』と、\x01",
            "よく嬉しそうに仰っていますよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0331
    ChrTalk(
        0x10,
        (
            "#5P#02809Fハハ、大先輩のマクダエル議長に\x01",
            "そう言われると照れてしまうな。\x02\x03",

            "#02803Fとはいえ、私も政治家としては\x01",
            "まだまだ駆け出しの若造だ。\x02\x03",

            "#02800Fまだまだ色々と\x01",
            "勉強させてもらわなくてはね。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x11, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0332
    ChrTalk(
        0x11,
        (
            "#11P#02905Fああ、お父様。\x01",
            "そろそろ新市庁ビルの方で\x01",
            "打ち合わせのお時間ですわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0333
    ChrTalk(
        0x10,
        (
            "#5P#02805Fおっと、そうだったか。\x02\x03",

            "#02800Fそれでは諸君、私はこれで\x01",
            "失礼させていただくとしよう。\x02",
        )
    )

    CloseMessageWindow()

    #C0334
    ChrTalk(
        0x101,
        (
            "#12P#00000Fすみません、なんだか\x01",
            "お引き留めしてしまって。\x02",
        )
    )

    CloseMessageWindow()

    #C0335
    ChrTalk(
        0x10,
        (
            "#5P#02809Fいやいや、そんな事はないさ。\x01",
            "おかげでリラックスできたよ。\x02\x03",

            "#02804F何か困った事があったら\x01",
            "いつでも言ってくれたまえ。\x02\x03",

            "#02800F他ならぬ君たちのためなら、\x01",
            "惜しみなく助力させてもらうよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0336
    ChrTalk(
        0x102,
        (
            "#12P#00100Fふふ、ありがとうございます。\x02\x03",

            "#00104Fおじさまもベルも、\x01",
            "お体にだけは気をつけて下さい。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x11, 0x102, 500)
    Sleep(300)

    #C0337
    ChrTalk(
        0x11,
        (
            "#5P#02909Fうふふ、ありがとうエリィ。\x02\x03",

            "#02900Fそれでは、失礼させて\x01",
            "いただきますわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0338
    ChrTalk(
        0x109,
        "#12P#10109Fお疲れ様でした！\x02",
    )

    CloseMessageWindow()
    OP_68(-310, 1500, 13600, 3000)
    MoveCamera(44, 24, 0, 3000)
    OP_6E(590, 3000)
    SetCameraDistance(15430, 3000)
    BeginChrThread(0x101, 3, 0, 18)
    Sleep(50)
    BeginChrThread(0x102, 3, 0, 19)
    Sleep(50)
    BeginChrThread(0x109, 3, 0, 18)
    Sleep(50)
    BeginChrThread(0x105, 3, 0, 19)
    Sleep(500)
    BeginChrThread(0x10, 3, 0, 17)
    Sleep(1000)
    BeginChrThread(0x11, 3, 0, 17)
    Sleep(2000)
    BeginChrThread(0x101, 3, 0, 20)
    Sleep(50)
    BeginChrThread(0x102, 3, 0, 21)
    Sleep(50)
    BeginChrThread(0x109, 3, 0, 20)
    Sleep(50)
    BeginChrThread(0x105, 3, 0, 21)
    WaitChrThread(0x11, 3)
    Sound(107, 0, 100, 0)
    Sleep(700)
    Sound(107, 0, 100, 0)
    Sleep(500)

    #C0339
    ChrTalk(
        0x101,
        "#00000Fやっぱり、相当忙しいみたいだな。\x02",
    )

    CloseMessageWindow()

    #C0340
    ChrTalk(
        0x102,
        (
            "#11P#00103F月末の『通商会議』も迫っているし……\x02\x03",

            "#00100F分刻みのスケジュールなのは\x01",
            "間違いないと思うわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0341
    ChrTalk(
        0x105,
        (
            "#12P#10304Fフフ、昨日の導力車といい、\x01",
            "僕らのために色々と\x01",
            "手を回してくれてるみたいだしね。\x02",
        )
    )

    CloseMessageWindow()

    #C0342
    ChrTalk(
        0x101,
        (
            "#00003Fああ、忙しすぎて体を壊さないよう\x01",
            "気をつけてほしいけど……\x02\x03",

            "#00000F……とにかく、今はロバーツ主任の\x01",
            "仕事を引き受けるとしようか。\x02",
        )
    )

    CloseMessageWindow()

    #C0343
    ChrTalk(
        0x109,
        (
            "#12P#10100Fはい、受付の方に\x01",
            "取り次いでいただきましょう！\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xBB8)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7562", 0)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    ClearMapFlags(0x10000000)
    OP_CC(0x1, 0xFF, 0x0)
    SetScenarioFlags(0x132, 5)
    SetChrPos(0x0, -60, 300, 15630, 0)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_16_5FD8 end

    def Function_17_7656(): pass

    label("Function_17_7656")

    OP_95(0xFE, -330, 300, 15470, 2000, 0x0)
    OP_95(0xFE, -40, 300, 6500, 2000, 0x0)
    Return()

    # Function_17_7656 end

    def Function_18_767F(): pass

    label("Function_18_767F")

    OP_93(0xFE, 0x5A, 0x1F4)
    OP_9B(0x1, 0xFE, 0xB4, 0x3E8, 0x7D0, 0x0)
    Return()

    # Function_18_767F end

    def Function_19_7696(): pass

    label("Function_19_7696")

    OP_93(0xFE, 0x10E, 0x1F4)
    OP_9B(0x1, 0xFE, 0xB4, 0x190, 0x7D0, 0x0)
    Return()

    # Function_19_7696 end

    def Function_20_76AD(): pass

    label("Function_20_76AD")

    OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0x7D0, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_20_76AD end

    def Function_21_76C4(): pass

    label("Function_21_76C4")

    OP_9B(0x0, 0xFE, 0x0, 0x190, 0x7D0, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_21_76C4 end

    def Function_22_76DB(): pass

    label("Function_22_76DB")

    EventBegin(0x0)
    OP_4B(0xA, 0xFF)
    Fade(500)
    OP_68(-20, 1300, 29740, 0)
    MoveCamera(37, 23, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(20420, 0)
    SetChrPos(0x101, -470, 300, 28930, 0)
    SetChrPos(0x102, 540, 300, 28690, 0)
    SetChrPos(0x109, -810, 300, 27570, 0)
    SetChrPos(0x105, 890, 300, 27520, 0)
    OP_0D()

    #C0344
    ChrTalk(
        0x102,
        "#12P#00100Fこんにちは、ランフィさん。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x134, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_78C3")

    #C0345
    ChrTalk(
        0xA,
        (
            "#5Pあら、ロイド様にエリィ様。\x01",
            "お久しぶりにございます。\x02",
        )
    )

    CloseMessageWindow()

    #C0346
    ChrTalk(
        0xA,
        (
            "#5Pどうやらまた、特務支援課の\x01",
            "お仕事を再開されたようですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0347
    ChrTalk(
        0x101,
        "#12P#00000Fええ、おかげ様で。\x02",
    )

    CloseMessageWindow()

    #C0348
    ChrTalk(
        0x102,
        (
            "#12P#00100Fこれからも改めて\x01",
            "よろしくお願いしますね。\x02",
        )
    )

    CloseMessageWindow()

    #C0349
    ChrTalk(
        0xA,
        "#5Pええ、もちろんですわ。\x02",
    )

    CloseMessageWindow()

    #C0350
    ChrTalk(
        0xA,
        (
            "#5Pそれでは、本日は\x01",
            "どういったご用件でしょうか？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_790D")

    label("loc_78C3")


    #C0351
    ChrTalk(
        0xA,
        (
            "#5Pあら、エリィ様に支援課の皆様。\x01",
            "本日はどういったご用件でしょうか？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_790D")


    #C0352
    ChrTalk(
        0x101,
        (
            "#12P#00000Fエプスタイン財団のロバーツ主任に\x01",
            "依頼された件なんですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0353
    ChrTalk(
        0xA,
        (
            "#5Pああ、その件でしたら\x01",
            "承っておりますわ。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x134, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7F89")
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_7B46")

    #C0354
    ChrTalk(
        0xA,
        "#5Pそうですわ、その前に……\x02",
    )

    CloseMessageWindow()

    #C0355
    ChrTalk(
        0xA,
        (
            "#5P以前、支援課の皆様にお渡しした\x01",
            "換金サービスに使うカードの\x01",
            "有効期限が切れてしまいまして。\x02",
        )
    )

    CloseMessageWindow()

    #C0356
    ChrTalk(
        0xA,
        (
            "#5P新しくご用意致しましたので、\x01",
            "こちらをお受け取り下さいませ。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0357
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x326),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を受け取った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x326, 1)
    SetMessageWindowPos(14, 280, 60, 3)

    #C0358
    ChrTalk(
        0xA,
        (
            "#5Pこのカードを以前のように\x01",
            "受付にてご提示ください。\x02",
        )
    )

    CloseMessageWindow()

    #C0359
    ChrTalk(
        0xA,
        (
            "#5P通常より高い換金率で\x01",
            "セピスをミラに換えさせて頂きます。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7CC9")

    label("loc_7B46")


    #C0360
    ChrTalk(
        0xA,
        (
            "#5Pそうですわ、その前に……\x01",
            "皆様にお渡しするものがございました。\x02",
        )
    )

    CloseMessageWindow()

    #C0361
    ChrTalk(
        0xA,
        "#5Pこちらをお受け取り下さいませ。\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0362
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x326),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を受け取った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x326, 1)
    SetMessageWindowPos(14, 280, 60, 3)

    #C0363
    ChrTalk(
        0x101,
        "#12P#00005Fこのカードは……？\x02",
    )

    CloseMessageWindow()

    #C0364
    ChrTalk(
        0xA,
        (
            "#5Pはい、そちらは当銀行の\x01",
            "優待会員であることを\x01",
            "示すカードでございます。\x02",
        )
    )

    CloseMessageWindow()

    #C0365
    ChrTalk(
        0xA,
        (
            "#5P受付にてご提示頂ければ、\x01",
            "通常より高い換金率で\x01",
            "セピスをミラに換えさせて頂きます。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7CC9")

    FadeToDark(300, 0, 100)
    Sound(814, 0, 100, 0)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0366
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※ＩＢＣの換金サービスが利用可能になりました。\x01",
            "　通常のショップメニューより、\x01",
            "　高レートでセピスを換金することができます。\x02\x03",

            "※ランフィに話しかけ、\x01",
            "　『セピス換金』を選んだ後\x01",
            "　<EXCHANGE>を選ぶと換金を行う事ができます。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x134, 4)

    #C0367
    ChrTalk(
        0x109,
        (
            "#12P#10105Fそ、そんなサービスを\x01",
            "私たちが受けてもいいんですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0368
    ChrTalk(
        0xA,
        (
            "#5Pええ、皆様はクロイス市長、\x01",
            "並びにマリアベルお嬢様の\x01",
            "大切なご友人ですから。\x02",
        )
    )

    CloseMessageWindow()

    #C0369
    ChrTalk(
        0xA,
        "#5P便宜を図るのは当然のことですわ。\x02",
    )

    CloseMessageWindow()

    #C0370
    ChrTalk(
        0x105,
        (
            "#12P#10302Fフフ、それじゃあありがたく\x01",
            "受けさせてもらおうかな。\x02",
        )
    )

    CloseMessageWindow()

    #C0371
    ChrTalk(
        0x101,
        "#12P#00000F是非、今度利用させて頂きます。\x02",
    )

    CloseMessageWindow()

    #C0372
    ChrTalk(
        0xA,
        "#5Pふふ、お待ちしておりますわ。\x02",
    )

    CloseMessageWindow()

    #C0373
    ChrTalk(
        0xA,
        (
            "#5Pでは、ロバーツ主任に\x01",
            "お取次ぎ致しますので\x01",
            "少々お待ちくださいませ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7FBF")

    label("loc_7F89")


    #C0374
    ChrTalk(
        0xA,
        (
            "#5Pお取次ぎ致しますので\x01",
            "少々お待ちくださいませ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7FBF")

    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xBB8)
    Sleep(1000)
    OP_68(6520, 1500, 14990, 0)
    MoveCamera(39, 23, 0, 0)
    OP_6E(590, 0)
    SetCameraDistance(13860, 0)
    SetChrPos(0x101, 4820, 0, 16800, 90)
    SetChrPos(0x102, 4820, 0, 15390, 90)
    SetChrPos(0x109, 3530, 0, 16850, 90)
    SetChrPos(0x105, 3470, 0, 15130, 90)
    SetChrPos(0xE, 10590, 0, 16190, 270)
    OP_A7(0xE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_4B(0xE, 0xFF)
    ClearChrFlags(0xE, 0x80)
    FadeToBright(1000, 0)
    OP_0D()
    Sound(160, 0, 100, 0)
    Sleep(700)
    Sound(107, 0, 100, 0)
    ClearMapObjFlags(0x0, 0x10)
    OP_71(0x0, 0x0, 0x10, 0x0, 0x0)
    OP_79(0x1)
    Sleep(1000)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7522", 0)
    OP_68(4600, 1500, 15420, 2000)

    def lambda_80B8():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_80B8)

    def lambda_80C9():
        OP_95(0xFE, 6410, 0, 16170, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_80C9)
    Sleep(1000)
    Sound(107, 0, 100, 0)
    OP_71(0x0, 0x10, 0x0, 0x0, 0x0)
    OP_79(0x0)
    SetMapObjFlags(0x0, 0x10)
    WaitChrThread(0xE, 1)
    OP_6F(0x1)

    #C0375
    ChrTalk(
        0xE,
        "やあ君たち！\x02",
    )

    CloseMessageWindow()

    #C0376
    ChrTalk(
        0x101,
        "#6P#00000Fお疲れさまです、ロバーツ主任。\x02",
    )

    CloseMessageWindow()

    #C0377
    ChrTalk(
        0xE,
        "依頼を見て来てくれたんだよね？\x02",
    )

    CloseMessageWindow()

    #C0378
    ChrTalk(
        0xE,
        (
            "いや～、本当に助かるよ。\x01",
            "君たちに是非とも\x01",
            "やってもらいたい仕事だったんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0379
    ChrTalk(
        0x105,
        (
            "#6P#10300Fフフ、なんだか楽しそうな\x01",
            "内容だったよね。\x02\x03",

            "#10304F何とかってサービスの\x01",
            "最終テストがどうとか……\x02",
        )
    )

    CloseMessageWindow()

    #C0380
    ChrTalk(
        0x109,
        (
            "#6P#10100Fたしか……\x01",
            "『ポムっと！』でしたね。\x02",
        )
    )

    CloseMessageWindow()

    #C0381
    ChrTalk(
        0x102,
        (
            "#6P#00105Fなんだか、どこかで\x01",
            "聞いたことのある名前ですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0382
    ChrTalk(
        0x101,
        "#6P#00005F言われてみれば確かに……\x02",
    )

    CloseMessageWindow()

    #C0383
    ChrTalk(
        0xE,
        "ふふ、きっと楽しいと思うよ～。\x02",
    )

    CloseMessageWindow()

    #C0384
    ChrTalk(
        0xE,
        (
            "それじゃ、早速だけど\x01",
            "仕事を受けてもらえるかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0385
    ChrTalk(
        0x101,
        "#6P#00000Fええ、もちろんです。\x02",
    )

    CloseMessageWindow()

    #C0386
    ChrTalk(
        0x102,
        (
            "#6P#00100Fそれでは、仕事の内容を\x01",
            "説明してもらえますか？\x02",
        )
    )

    CloseMessageWindow()

    #C0387
    ChrTalk(
        0xE,
        "ふふ、任せてくれ。\x02",
    )

    CloseMessageWindow()

    #C0388
    ChrTalk(
        0xE,
        (
            "実は、近いうちに\x01",
            "『ポムっと！』という\x01",
            "導力ゲームを配布する予定でね。\x02",
        )
    )

    CloseMessageWindow()

    #C0389
    ChrTalk(
        0xE,
        (
            "市内の導力ネット端末\x01",
            "所有者にむけて開発を\x01",
            "進めていたところなんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0390
    ChrTalk(
        0x109,
        "#6P#10105F導力ゲーム……？\x02",
    )

    CloseMessageWindow()

    #C0391
    ChrTalk(
        0x105,
        (
            "#6P#10305Fそれって、ビリヤードや\x01",
            "ポーカーみたいなものとは\x01",
            "違うのかい？\x02",
        )
    )

    CloseMessageWindow()

    #C0392
    ChrTalk(
        0xE,
        (
            "まあ、一定のルールに則って\x01",
            "勝敗や得点を競うという点では\x01",
            "似たようなものかな。\x02",
        )
    )

    CloseMessageWindow()

    #C0393
    ChrTalk(
        0xE,
        (
            "最も異なるのは、\x01",
            "端末の画面上のものを\x01",
            "動かして遊ぶって所だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0394
    ChrTalk(
        0x101,
        (
            "#6P#00003Fな、なんだか\x01",
            "すごそうですね……\x02",
        )
    )

    CloseMessageWindow()

    #C0395
    ChrTalk(
        0x102,
        (
            "#6P#00105Fそれじゃあ、今回の依頼の\x01",
            "『テスト』というのは……\x02",
        )
    )

    CloseMessageWindow()

    #C0396
    ChrTalk(
        0xE,
        (
            "もちろん、この\x01",
            "『ポムっと！』のテストを\x01",
            "してほしいんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0397
    ChrTalk(
        0xE,
        (
            "プログラムを組む以上、\x01",
            "バグは出てしまうものだから\x01",
            "テストの繰り返しは必須なんだよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0398
    ChrTalk(
        0x105,
        (
            "#6P#10302Fふうん……\x01",
            "でも、その程度のテストなら\x01",
            "財団でもできるんじゃないのかい？\x02",
        )
    )

    CloseMessageWindow()

    #C0399
    ChrTalk(
        0xE,
        (
            "うーん、このテストは\x01",
            "少し前からティオ君に手伝って\x01",
            "もらってたんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0400
    ChrTalk(
        0xE,
        (
            "実は、２つほど問題があってね。\x01",
            "どうしても財団の外部に\x01",
            "手伝いが欲しいんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0401
    ChrTalk(
        0x101,
        "#6P#00005F２つの問題……ですか？\x02",
    )

    CloseMessageWindow()

    #C0402
    ChrTalk(
        0xE,
        "うん、まず１つ目だけど……\x02",
    )

    CloseMessageWindow()

    #C0403
    ChrTalk(
        0xE,
        (
            "ティオくんは時々、テストに\x01",
            "『エイオンシステム』を\x01",
            "持ち出してたみたいでねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0404
    ChrTalk(
        0xE,
        (
            "だから、ちょっと有用なデータを\x01",
            "取れたとは言い難いというか……\x02",
        )
    )

    CloseMessageWindow()

    #C0405
    ChrTalk(
        0x109,
        "#6P#10105Fエイオンシステムっていうと……\x02",
    )

    CloseMessageWindow()

    #C0406
    ChrTalk(
        0x102,
        (
            "#6P#00100Fティオちゃんが何度か\x01",
            "使っていたアレね。\x02\x03",

            "#00104F前にちょっとだけ\x01",
            "教えてもらったわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0407
    ChrTalk(
        0x101,
        (
            "#6P#00000Fああ、確か導力端末や魔導杖を\x01",
            "扱うときに使っているシステム……\x01",
            "という話だったよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0408
    ChrTalk(
        0xE,
        (
            "ふむ、この際だから改めて、\x01",
            "僕から説明しておこうかな。\x02",
        )
    )

    CloseMessageWindow()

    #C0409
    ChrTalk(
        0xE,
        (
            "『エイオンシステム』とは、\x01",
            "ティオ君の胸部プロテクターに\x01",
            "内蔵されたシステムの名称だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0410
    ChrTalk(
        0xE,
        (
            "魔導杖によるノーウェイトでの\x01",
            "導力魔法の発動や、\x01",
            "ティオ君の高速処理能力……\x02",
        )
    )

    CloseMessageWindow()

    #C0411
    ChrTalk(
        0xE,
        (
            "それらを補助するというのが\x01",
            "主な機能になるかな。\x02",
        )
    )

    CloseMessageWindow()

    #C0412
    ChrTalk(
        0xE,
        (
            "このシステムを使いこなすのは\x01",
            "かなりの適性が必要なんだけどね。\x02",
        )
    )

    CloseMessageWindow()

    #C0413
    ChrTalk(
        0x101,
        (
            "#6P#00006Fう、うーん、\x01",
            "全然簡単じゃないような……\x02",
        )
    )

    CloseMessageWindow()

    #C0414
    ChrTalk(
        0x102,
        (
            "#6P#00106Fやっぱりティオちゃんがいないと\x01",
            "この手の話題は厳しいわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0415
    ChrTalk(
        0x105,
        (
            "#6P#10300F要するに、そのシステム自体が\x01",
            "テストには適さないってことかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0416
    ChrTalk(
        0xE,
        "ま、まあね。\x02",
    )

    CloseMessageWindow()

    #C0417
    ChrTalk(
        0xE,
        (
            "なんでも、エイオンシステムで\x01",
            "常人じゃ組めないような大連鎖を\x01",
            "組んだりして圧勝を重ねてたらしい。\x02",
        )
    )

    CloseMessageWindow()

    #C0418
    ChrTalk(
        0xE,
        (
            "ヨナ君がテストに\x01",
            "付き合ってたらしいけど、\x01",
            "１度も勝てたことはなかったそうだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0419
    ChrTalk(
        0xE,
        (
            "……あっ、でもティオ君がズルいとか\x01",
            "言ってるわけじゃないからね！？\x02",
        )
    )

    CloseMessageWindow()

    #C0420
    ChrTalk(
        0xE,
        (
            "くれぐれもティオ君に\x01",
            "おかしなことはいわないでくれよ？\x02",
        )
    )

    CloseMessageWindow()

    #C0421
    ChrTalk(
        0x101,
        "#6P#00006Fは、はあ……\x02",
    )

    CloseMessageWindow()

    #C0422
    ChrTalk(
        0x109,
        (
            "#6P#10105Fえっと……\x01",
            "のこりの１つの理由は\x01",
            "どういったものなんですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0423
    ChrTalk(
        0xE,
        (
            "ああ、もう１つは……\x01",
            "このゲームが“対戦ゲーム”って\x01",
            "ところにあるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0424
    ChrTalk(
        0xE,
        (
            "さっきもちょっと触れたけど、\x01",
            "このゲームは遠方の端末同士で\x01",
            "遊ぶことができるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0425
    ChrTalk(
        0xE,
        (
            "だから、どうしても市内での\x01",
            "実地テストがやりたかったってわけさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0426
    ChrTalk(
        0x102,
        (
            "#6P#00105Fなるほど……\x01",
            "そういうことですか。\x02\x03",

            "#00100Fそれにしても\x01",
            "離れた場所同士で遊べるって、\x01",
            "結構すごいことですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0427
    ChrTalk(
        0xE,
        "ふふ、だろう？\x02",
    )

    CloseMessageWindow()

    #C0428
    ChrTalk(
        0xE,
        (
            "これは導力ネット構想の\x01",
            "初期段階で企画されたものでね。\x02",
        )
    )

    CloseMessageWindow()

    #C0429
    ChrTalk(
        0xE,
        (
            "導力ネットがもっと普及すれば、\x01",
            "たくさんの人が楽しく\x01",
            "遊べるようになるだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0430
    ChrTalk(
        0xE,
        (
            "たとえば、こんな雨の日にも\x01",
            "家の中にいながら\x01",
            "友達と楽しめるしね。\x02",
        )
    )

    CloseMessageWindow()

    #C0431
    ChrTalk(
        0x101,
        (
            "#6P#00000Fへえ……\x01",
            "すごい時代になりましたね。\x02",
        )
    )

    CloseMessageWindow()

    #C0432
    ChrTalk(
        0xE,
        (
            "ちょっと話は逸れたけど……\x01",
            "ま、事情はそんなところかな。\x02",
        )
    )

    CloseMessageWindow()

    #C0433
    ChrTalk(
        0xE,
        (
            "……ってことで、キミたちには\x01",
            "これをプレゼントしよう。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0434
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x339),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を受け取った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x339, 1)
    SetMessageWindowPos(14, 280, 60, 3)

    #C0435
    ChrTalk(
        0x101,
        "#6P#00005Fこれは……記憶結晶#8Rメモリークオーツ#ですか？\x02",
    )

    CloseMessageWindow()

    #C0436
    ChrTalk(
        0xE,
        (
            "その記憶結晶に、完成直前の\x01",
            "『ポムっと！』のデータが入ってる。\x02",
        )
    )

    CloseMessageWindow()

    #C0437
    ChrTalk(
        0xE,
        (
            "それを支援課の端末に\x01",
            "インストールすれば、\x01",
            "すぐに遊べるはずだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0438
    ChrTalk(
        0x102,
        (
            "#6P#00100Fインストール……\x01",
            "要するに端末にプログラムを\x01",
            "組み込む作業ですよね。\x02\x03",

            "#00104F前にティオちゃんが\x01",
            "やっているのを見たことがあるし、\x01",
            "何とかなると思うわ。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)
    Sleep(300)

    #C0439
    ChrTalk(
        0x101,
        (
            "#6P#00000Fそれじゃあエリィ、\x01",
            "よろしくたのむよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0440
    ChrTalk(
        0xE,
        "うんうん、心強いね。\x02",
    )

    CloseMessageWindow()

    #C0441
    ChrTalk(
        0xE,
        (
            "それと、こいつも渡しておくよ。\x01",
            "僕のエニグマの番号と、\x01",
            "『ポムっと！』のアカウントだ。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x5A, 0x1F4)
    Sleep(300)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0442
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "『ロバーツ主任のアカウント』\x07\x00",
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x27, 3)
    OP_E4(0x3)

    #C0443
    ChrTalk(
        0x101,
        "#6P#00005Fア、アカウント……？\x02",
    )

    CloseMessageWindow()

    #C0444
    ChrTalk(
        0x109,
        (
            "#6P#10106Fちょ、ちょっと待ってください。\x01",
            "立て続けに難しい用語が……\x02",
        )
    )

    CloseMessageWindow()

    #C0445
    ChrTalk(
        0xE,
        (
            "ええと、要するに\x01",
            "ネットワーク上で使用する\x01",
            "名前みたいなものなんだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0446
    ChrTalk(
        0xE,
        (
            "まあ、対戦を遊ぶために\x01",
            "必要なものとだけ\x01",
            "考えてくれればいいよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0447
    ChrTalk(
        0xE,
        (
            "難しいことは置いといていいから、\x01",
            "とりあえずβ版をインストールするときに\x01",
            "一緒に入力してくれればいい。\x02",
        )
    )

    CloseMessageWindow()

    #C0448
    ChrTalk(
        0xE,
        (
            "その後エニグマで連絡をくれたら、\x01",
            "次の手順を教えるからね。\x02",
        )
    )

    CloseMessageWindow()

    #C0449
    ChrTalk(
        0xE,
        (
            "……ま、こんなところかな。\x01",
            "さっそくテストを始めてくれるかい？\x02",
        )
    )

    CloseMessageWindow()

    #C0450
    ChrTalk(
        0x101,
        (
            "#6P#00000Fは、はい。\x01",
            "お任せください。\x02\x03",

            "#00004Fとりあえず、\x01",
            "支援課に戻るとしよう。\x02",
        )
    )

    CloseMessageWindow()

    #C0451
    ChrTalk(
        0x102,
        "#6P#00102Fええ、そうしましょう。\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    Sound(80, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0452
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "クエスト【βテストの参加依頼】\x07\x00",
            "を開始した！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xBB8)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7562", 0)
    SetScenarioFlags(0x131, 3)
    OP_29(0x6C, 0x1, 0x0)
    OP_4C(0xA, 0xFF)
    OP_4C(0xE, 0xFF)
    SetChrPos(0xE, 6500, 0, 17850, 270)
    SetChrPos(0x0, 4010, 0, 16140, 90)
    EventEnd(0x5)
    Return()

    # Function_22_76DB end

    def Function_23_9598(): pass

    label("Function_23_9598")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch29300.itc", 0x1E)
    LoadChrToIndex("chr/ch06100.itc", 0x1F)
    LoadChrToIndex("apl/ch51255.itc", 0x20)
    OP_68(0, 1400, 4600, 0)
    MoveCamera(54, 21, 0, 0)
    OP_6E(590, 0)
    SetCameraDistance(16149, 0)
    SetChrPos(0x101, 500, 300, 2000, 0)
    SetChrPos(0x102, -1000, 300, 800, 0)
    SetChrPos(0x103, -500, 300, 2000, 0)
    SetChrPos(0x104, 1000, 300, 1200, 0)
    SetChrPos(0x109, 500, 300, 0, 0)
    SetChrPos(0x105, -500, 300, 0, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_96A5():
        OP_97(0x101, 0x0, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_96A5)
    Sleep(100)

    def lambda_96C2():
        OP_97(0x103, 0x0, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_96C2)
    Sleep(100)

    def lambda_96DF():
        OP_97(0x104, 0x0, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_96DF)
    Sleep(100)

    def lambda_96FC():
        OP_97(0x102, 0x0, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_96FC)
    Sleep(100)

    def lambda_9719():
        OP_97(0x109, 0x0, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_9719)
    Sleep(100)

    def lambda_9736():
        OP_97(0x105, 0x0, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_9736)
    OP_68(-70, 1400, 7250, 3000)
    Sound(107, 0, 100, 0)
    FadeToBright(1000, 0)

    def lambda_9770():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_9770)
    Sleep(100)

    def lambda_9784():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_9784)
    Sleep(500)

    def lambda_9798():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_9798)
    Sleep(100)

    def lambda_97AC():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_97AC)
    Sleep(500)

    def lambda_97C0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_97C0)
    Sleep(100)

    def lambda_97D4():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_97D4)
    WaitChrThread(0x105, 0)
    Sound(107, 0, 100, 0)
    OP_6F(0x79)

    #C0453
    ChrTalk(
        0x101,
        (
            "#11P#00000Fさてと……\x01",
            "ロバーツ主任はいるかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0454
    ChrTalk(
        0x103,
        (
            "#00203F#6P多分、財団のフロアで\x01",
            "ヒマそうにしてると思います。\x02\x03",

            "#00200Fエニグマで連絡してみましょう。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_988D():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_988D)

    def lambda_989A():
        TurnDirection(0x101, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_989A)
    Sleep(50)

    def lambda_98AA():
        TurnDirection(0x104, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_98AA)
    Sleep(50)

    def lambda_98BA():
        TurnDirection(0x102, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_98BA)
    Sleep(50)

    def lambda_98CA():
        TurnDirection(0x105, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_98CA)
    Sleep(50)

    def lambda_98DA():
        TurnDirection(0x109, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_98DA)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x109, 0)
    SetCameraDistance(15650, 2000)
    Sound(802, 0, 100, 0)
    Fade(250)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x0)
    SetChrFlags(0x103, 0x20)
    SetChrFlags(0x103, 0x10)
    SetChrFlags(0x103, 0x2)
    Sleep(500)
    Sound(804, 0, 100, 0)
    Sleep(300)
    SetChrSubChip(0x103, 0x1)
    Sound(823, 0, 100, 0)
    Sleep(2700)

    #C0455
    ChrTalk(
        0x103,
        (
            "#00200F#5P……どうも、ティオです。\x02\x03",

            "#00205Fいえ……\x01",
            "別にそんなつもりは。\x02\x03",

            "#00203F………………………………\x02\x03",

            "#00211Fしつこいです、主任。\x01",
            "いい加減にしてください。\x02",
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

    #C0456
    ChrTalk(
        0x101,
        "#11P#00012F（あ、相変わらずみたいだな……）\x02",
    )

    CloseMessageWindow()

    #C0457
    ChrTalk(
        0x102,
        (
            "#12P#00106F（ティオちゃんももう少し\x01",
            "  優しく接すればいいのに……）\x02",
        )
    )

    CloseMessageWindow()

    #C0458
    ChrTalk(
        0x104,
        (
            "#00302F#11P（むしろあのオッサンなら\x01",
            "  冷たくされて喜んでんじゃねえか？）\x02",
        )
    )

    CloseMessageWindow()

    #C0459
    ChrTalk(
        0x103,
        (
            "#00203F#5P……ええ、エニグマⅡの\x01",
            "緊急アラート機能について……\x02\x03",

            "#00200F………ええ……そうです………\x02\x03",

            "#00203Fはい、下に来ているので\x01",
            "よろしくお願いします。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x103, 0x0)
    Sleep(300)
    Sound(804, 0, 100, 0)
    Sleep(400)
    Sound(802, 0, 100, 0)
    Fade(250)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    ClearChrFlags(0x103, 0x20)
    ClearChrFlags(0x103, 0x10)
    ClearChrFlags(0x103, 0x2)
    OP_0D()

    #C0460
    ChrTalk(
        0x101,
        "#11P#00000F相談に乗ってくれるって？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 500)

    #C0461
    ChrTalk(
        0x103,
        (
            "#00204F#6Pええ、すぐにこちらに\x01",
            "降りてくるそうです。\x02\x03",

            "#00202F何でもヨナも一緒だとか。\x02",
        )
    )

    CloseMessageWindow()

    #C0462
    ChrTalk(
        0x102,
        "#12P#00102Fあら……\x02",
    )

    CloseMessageWindow()

    #C0463
    ChrTalk(
        0x109,
        (
            "#10100F#11Pそれって確か、爆破された\x01",
            "ジオフロントの部屋を使っていた？\x02",
        )
    )

    CloseMessageWindow()

    #C0464
    ChrTalk(
        0x105,
        (
            "#12P#10300Fエプスタイン財団出身の\x01",
            "天才ハッカー君だったかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0465
    ChrTalk(
        0x104,
        (
            "#00304F#11Pああ、小生意気だが\x01",
            "微妙にヘタレな小僧だぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0466
    ChrTalk(
        0x101,
        (
            "#11P#00000Fさすがに今は財団の事務所に\x01",
            "厄介になってるらしいな？\x02",
        )
    )

    CloseMessageWindow()

    #C0467
    ChrTalk(
        0x103,
        (
            "#00206F#6Pええ……\x01",
            "イヤイヤみたいですけど。\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(15150, 2000)
    StopSound(128, 2000, 40)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    StopBGM(0xFA0)
    WaitBGM()
    SetChrPos(0x101, 4900, 0, 21000, 90)
    SetChrPos(0x102, 4700, 0, 22200, 135)
    SetChrPos(0x103, 4900, 0, 19900, 90)
    SetChrPos(0x104, 6900, 0, 23000, 180)
    SetChrPos(0x109, 5800, 0, 23000, 135)
    SetChrPos(0x105, 4400, 0, 18500, 45)
    OP_4B(0xE, 0xFF)
    SetChrChipByIndex(0xE, 0x1E)
    SetChrSubChip(0xE, 0x0)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x8000)
    SetChrPos(0xE, 7300, 0, 21000, 270)
    SetChrChipByIndex(0xF, 0x1F)
    SetChrSubChip(0xF, 0x0)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x8000)
    SetChrPos(0xF, 7300, 0, 19900, 270)
    OP_68(6100, 1100, 20450, 0)
    MoveCamera(43, 17, 0, 0)
    OP_6E(590, 0)
    SetCameraDistance(15000, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0468
    AnonymousTalk(
        0xE,
        (
            "──なるほど。\x01",
            "そんな事情だったのか。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    PlayBGM("ed7111", 0)
    SetCameraDistance(16000, 2000)
    FadeToBright(2000, 0)
    OP_0D()
    Sound(128, 2, 50, 0)
    OP_6F(0x79)

    #C0469
    ChrTalk(
        0xF,
        (
            "#02306F#11Pハッ、どうせ導力切れで\x01",
            "連絡が取れないってだけだろ？\x02\x03",

            "#02301F遊撃士なんて良い子ぶった連中、\x01",
            "放っときゃいいじゃん。\x02",
        )
    )

    CloseMessageWindow()

    #C0470
    ChrTalk(
        0x101,
        "#6P#00006Fヨナ、お前なぁ。\x02",
    )

    CloseMessageWindow()

    #C0471
    ChrTalk(
        0x102,
        (
            "#6P#00108Fもう……\x01",
            "そんな事言っちゃダメよ？\x02",
        )
    )

    CloseMessageWindow()

    #C0472
    ChrTalk(
        0xE,
        (
            "#11Pはあ、ヨナ君ときたら\x01",
            "最近ずっとこうなんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0473
    ChrTalk(
        0xE,
        (
            "#11Pせっかく事務所の一角に\x01",
            "最新型の専用端末ルームを\x01",
            "用意してあげたっていうのにさ。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xF, 0xE, 500)
    Sleep(200)

    #C0474
    ChrTalk(
        0xF,
        (
            "#02310F#12Pいくら処理能力が高くたって\x01",
            "あんな制限付きのシステムで\x01",
            "満足できるかっつーの！\x02\x03",

            "#02307Fとっととセキュリティコードを\x01",
            "ボクに解放しろよな！？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0xF, 500)

    #C0475
    ChrTalk(
        0xE,
        "#5Pあ、それはダメだよ、ヨナ君。\x02",
    )

    CloseMessageWindow()

    #C0476
    ChrTalk(
        0xE,
        (
            "#5Pそんな事をしたら君、\x01",
            "またやりたい放題しちゃうだろ？\x02",
        )
    )

    CloseMessageWindow()

    #C0477
    ChrTalk(
        0xE,
        (
            "#5Pかわりに『ポムっと！』でティオ君に\x01",
            "勝てるよう、特訓用のプログラムを\x01",
            "組んであげたからさ～。\x02",
        )
    )

    CloseMessageWindow()

    #C0478
    ChrTalk(
        0xF,
        "#02311F#12Pよ、余計なお世話だっつーの！\x02",
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

    #C0479
    ChrTalk(
        0x101,
        (
            "#6P#00012F（何だかんだいってヨナの事、\x01",
            "  ちゃんと監督してるみたいだな。）\x02",
        )
    )

    CloseMessageWindow()

    #C0480
    ChrTalk(
        0x103,
        (
            "#6P#00203F（まあ、イラっとする所はともかく\x01",
            "  有能な人ではありますから。）\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xE, 0x10E, 0x1F4)
    Sleep(150)

    #C0481
    ChrTalk(
        0xE,
        "#11P──まあ、それはともかく。\x02",
    )

    CloseMessageWindow()

    #C0482
    ChrTalk(
        0xE,
        (
            "#11PエニグマⅡのアラート機能だが\x01",
            "お役に立てないかもしれないねぇ。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_A3C4():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF, 2, lambda_A3C4)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0483
    ChrTalk(
        0x101,
        "#6P#00011Fそ、そうなんですか？\x02",
    )

    CloseMessageWindow()

    #C0484
    ChrTalk(
        0x102,
        (
            "#6P#00105Fそういった機能が\x01",
            "あるのはあるんですよね？\x02",
        )
    )

    CloseMessageWindow()

    #C0485
    ChrTalk(
        0xE,
        (
            "#11Pうん、ただ導力波が弱くて\x01",
            "ほとんど感知できなくてねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0486
    ChrTalk(
        0xE,
        (
            "#11P１０セルジュくらい近付かないと\x01",
            "測定器でも感知できないんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0487
    ChrTalk(
        0x109,
        "#10101F#5P１０セルジュ……\x02",
    )

    CloseMessageWindow()

    #C0488
    ChrTalk(
        0x104,
        "#00306F#5Pそりゃまた微妙な距離だな……\x02",
    )

    CloseMessageWindow()

    #C0489
    ChrTalk(
        0x105,
        (
            "#6P#10301Fクロスベル市内にいるのなら\x01",
            "感知できそうだけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0490
    ChrTalk(
        0x103,
        (
            "#6P#00203F……わたしのセンサーと\x01",
            "組み合わせるのはどうでしょう？\x02\x03",

            "#00201Fマトリクス化されたシステムなら\x01",
            "エイオンで連動できそうですが。\x02",
        )
    )

    CloseMessageWindow()

    #C0491
    ChrTalk(
        0xE,
        "#11Pああ、それならあるいは──\x02",
    )

    CloseMessageWindow()

    #C0492
    ChrTalk(
        0xE,
        (
            "#11P……いや、やっぱりダメだ。\x01",
            "エイオンに連動させるには\x01",
            "測定器の精度が不安定すぎる。\x02",
        )
    )

    CloseMessageWindow()

    #C0493
    ChrTalk(
        0xE,
        (
            "#11P導力圧の問題もあるし、\x01",
            "周辺地形の反射も考えられるから\x01",
            "かなり無理があると思うよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0494
    ChrTalk(
        0x103,
        "#6P#00206Fそうですか……\x02",
    )

    CloseMessageWindow()

    #C0495
    ChrTalk(
        0x101,
        (
            "#6P#00006Fな、何がダメなのか\x01",
            "イマイチ分かりませんが……\x02",
        )
    )

    CloseMessageWindow()

    #C0496
    ChrTalk(
        0x102,
        (
            "#6P#00108Fどうやら技術的な\x01",
            "問題があるみたいね……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xF, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0xF)

    #C0497
    ChrTalk(
        0xF,
        (
            "#02305F#11P──だったらさぁ。\x02\x03",

            "#02300Fオルキスタワーの屋上で\x01",
            "測定しちゃえばいいんじゃね？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_A8D7():
        TurnDirection(0xFE, 0xF, 500)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_A8D7)

    #C0498
    ChrTalk(
        0x103,
        "#6P#00205Fえ……\x02",
    )

    CloseMessageWindow()

    #C0499
    ChrTalk(
        0xE,
        "#5P……ヨナ君？\x02",
    )

    CloseMessageWindow()

    #C0500
    ChrTalk(
        0x101,
        "#6P#00001Fえっと、どういうことだ？\x02",
    )

    CloseMessageWindow()

    #C0501
    ChrTalk(
        0xF,
        (
            "#02301F#11Pアラート用の導力波は微弱すぎて\x01",
            "測定器から近い場所にないと\x01",
            "感知しきれない。\x02\x03",

            "#02303Fかといって測定器と\x01",
            "ティオのセンサーと連動させても\x01",
            "出力が足りないし精度不足なんだろ？\x02\x03",

            "#02302Fでも、遮蔽物のないタワーの屋上なら\x01",
            "感知精度も上げられるだろうし\x01",
            "高出力の導力が確保できるんじゃね？\x02",
        )
    )

    CloseMessageWindow()

    #C0502
    ChrTalk(
        0x104,
        "#00305F#5Pあ、相変わらず意味不明だが……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x103, 500)

    #C0503
    ChrTalk(
        0x109,
        "#10100F#5Pどうなの、ティオちゃん？\x02",
    )

    CloseMessageWindow()

    #C0504
    ChrTalk(
        0x103,
        "#6P#00204F……驚きました。\x02",
    )

    CloseMessageWindow()

    #C0505
    ChrTalk(
        0xE,
        "#5Pいやはや、さすがヨナ君！\x02",
    )

    CloseMessageWindow()

    #C0506
    ChrTalk(
        0xE,
        (
            "#5Pシステムエンジニアとしての才能は\x01",
            "目を見張るものがあるねぇ！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xF, 0xE, 500)
    Sleep(100)

    #C0507
    ChrTalk(
        0xF,
        (
            "#02309F#12Pフ、フフン。\x01",
            "まあそれほどでもあるけどなー！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_AB82():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_AB82)

    #C0508
    ChrTalk(
        0x101,
        "#6P#00002Fそれじゃあ……\x02",
    )

    CloseMessageWindow()

    #C0509
    ChrTalk(
        0x105,
        "#6P#10302F何とか目処が立ったみたいだね？\x02",
    )

    CloseMessageWindow()

    #C0510
    ChrTalk(
        0x103,
        "#6P#00202Fええ、行けるかもしれません。\x02",
    )

    CloseMessageWindow()
    OP_93(0xE, 0x10E, 0x1F4)

    #C0511
    ChrTalk(
        0xE,
        (
            "#11P早速、オルキスタワーの管理部に\x01",
            "屋上の使用許可が貰えないか\x01",
            "掛け合ってみよう。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0xF, 500)
    Sleep(150)

    #C0512
    ChrTalk(
        0xE,
        "#5Pヨナ君、君も手伝ってくれるね？\x02",
    )

    CloseMessageWindow()

    #C0513
    ChrTalk(
        0xF,
        (
            "#02302F#12Pなんでボクが──って言いたいけど\x01",
            "まあヒマだし手伝ってやるよ。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xF, 0x10E, 0x1F4)
    Sleep(100)

    #C0514
    ChrTalk(
        0xF,
        (
            "#02301F#11Pその代わりアンタら。\x01",
            "これで貸し１つだからな！？\x02",
        )
    )

    CloseMessageWindow()

    #C0515
    ChrTalk(
        0x101,
        "#6P#00004Fはは、分かった。\x02",
    )

    CloseMessageWindow()

    #C0516
    ChrTalk(
        0x102,
        (
            "#6P#00102F無茶な頼みでもない限り\x01",
            "きっとお返しさせてもらうわ。\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(15500, 2000)
    StopSound(128, 2000, 40)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    StopBGM(0xFA0)
    WaitBGM()
    SetChrName("")

    #A0517
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "その後、オルキスタワーの管理部から\x01",
            "屋上の使用許可をもらった主任たちは\x01",
            "機材と共に一足先にタワーへと向かった。\x02\x03",

            "準備に少し時間が掛かるらしく、\x01",
            "ロイドたちは他の用事を片付けてから\x01",
            "オルキスタワーに向かうことにした。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    OP_49()
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_D7(0x20)
    SetChrPos(0x0, 0, 300, 8000, 180)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetScenarioFlags(0x164, 2)
    OP_29(0xA9, 0x1, 0x1)
    ClearMapFlags(0x10000000)
    PlayBGM("ed7150", 0)
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x96), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sound(128, 2, 50, 0)
    EventEnd(0x5)
    Return()

    # Function_23_9598 end

    def Function_24_AEE6(): pass

    label("Function_24_AEE6")

    EventBegin(0x0)
    Fade(1000)
    OP_68(-230, 1400, 29510, 0)
    MoveCamera(42, 21, 0, 0)
    OP_6E(590, 0)
    SetCameraDistance(15440, 0)
    SetChrPos(0x101, 0, 300, 28870, 0)
    SetChrPos(0x102, -1300, 300, 28870, 0)
    SetChrPos(0x104, 1300, 300, 28870, 0)
    SetChrPos(0x109, 0, 300, 27710, 0)
    SetChrPos(0x103, -1300, 300, 27710, 0)
    SetChrPos(0x105, 1300, 300, 27710, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0xA, 0xFF)
    OP_0D()

    #C0518
    ChrTalk(
        0xA,
        (
            "#5P皆様……\x01",
            "ようこそおいで下さいました。\x02",
        )
    )

    CloseMessageWindow()

    #C0519
    ChrTalk(
        0xA,
        (
            "#5Pもしかして、\x01",
            "マリアベルお嬢様の依頼の件で\x01",
            "来ていただけたのでしょうか？\x02",
        )
    )

    CloseMessageWindow()

    #C0520
    ChrTalk(
        0x101,
        "#00000Fええ、その件で伺いました。\x02",
    )

    CloseMessageWindow()

    #C0521
    ChrTalk(
        0x102,
        (
            "#12P#00101F何でも、ベルの大事にしている\x01",
            "アンティークドールが\x01",
            "盗難にあってしまったそうですね？\x02",
        )
    )

    CloseMessageWindow()

    #C0522
    ChrTalk(
        0x103,
        (
            "#12P#00205Fもしかして、例の\x01",
            "ローゼンベルク工房製のものが……？\x02",
        )
    )

    CloseMessageWindow()

    #C0523
    ChrTalk(
        0xA,
        (
            "#5Pええ、そうなのです。\x01",
            "マリアベルお嬢様も\x01",
            "大変落胆されている様子で……\x02",
        )
    )

    CloseMessageWindow()

    #C0524
    ChrTalk(
        0xA,
        (
            "#5P早速ですが、お嬢様のご依頼を\x01",
            "お引き受け頂けますでしょうか？\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 25)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B18B")
    Call(0, 27)

    label("loc_B18B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B1B4")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    Jump("loc_B1BE")

    label("loc_B1B4")

    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)

    label("loc_B1BE")

    SetChrPos(0x0, 0, 300, 28280, 0)
    OP_69(0xFF, 0x0)
    OP_4C(0xA, 0xFF)
    EventEnd(0x5)
    Return()

    # Function_24_AEE6 end

    def Function_25_B1DA(): pass

    label("Function_25_B1DA")

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
            "引き受ける\x01",      # 0
            "やめる\x01",          # 1
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
        (0, "loc_B23C"),
        (1, "loc_B241"),
        (SWITCH_DEFAULT, "loc_B2FF"),
    )


    label("loc_B23C")

    Jump("loc_B2FF")

    label("loc_B241")


    #C0525
    ChrTalk(
        0x101,
        (
            "#00006F申しわけありませんが、\x01",
            "今は手を離せなくて……\x02",
        )
    )

    CloseMessageWindow()

    #C0526
    ChrTalk(
        0xA,
        (
            "#5Pそうでございますか……\x01",
            "仕方がありませんね。\x02",
        )
    )

    CloseMessageWindow()

    #C0527
    ChrTalk(
        0xA,
        (
            "#5Pもしお時間に余裕が出来ましたら、\x01",
            "今一度声をおかけくださいませ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1C6, 1)
    Jump("loc_B2FF")

    label("loc_B2FF")

    Return()

    # Function_25_B1DA end

    def Function_26_B300(): pass

    label("Function_26_B300")

    EventBegin(0x0)
    Fade(1000)
    OP_68(-230, 1400, 29510, 0)
    MoveCamera(42, 21, 0, 0)
    OP_6E(590, 0)
    SetCameraDistance(15440, 0)
    SetChrPos(0x101, 0, 300, 28870, 0)
    SetChrPos(0x102, -1300, 300, 28870, 0)
    SetChrPos(0x104, 1300, 300, 28870, 0)
    SetChrPos(0x109, 0, 300, 27710, 0)
    SetChrPos(0x103, -1300, 300, 27710, 0)
    SetChrPos(0x105, 1300, 300, 27710, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0xA, 0xFF)
    OP_0D()

    #C0528
    ChrTalk(
        0xA,
        (
            "#5Pアンティークドールの盗難で、\x01",
            "マリアベルお嬢様も\x01",
            "大変落胆されている様子で……\x02",
        )
    )

    CloseMessageWindow()

    #C0529
    ChrTalk(
        0xA,
        (
            "#5P早速ですが、お嬢様のご依頼を\x01",
            "お引き受け頂けますでしょうか？\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 25)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B462")
    Call(0, 27)

    label("loc_B462")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B48B")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    Jump("loc_B495")

    label("loc_B48B")

    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)

    label("loc_B495")

    SetChrPos(0x0, 0, 300, 28280, 0)
    OP_69(0xFF, 0x0)
    OP_4C(0xA, 0xFF)
    EventEnd(0x5)
    Return()

    # Function_26_B300 end

    def Function_27_B4B1(): pass

    label("Function_27_B4B1")


    #C0530
    ChrTalk(
        0x101,
        "#00000Fええ、引き受けさせていただきます。\x02",
    )

    CloseMessageWindow()

    #C0531
    ChrTalk(
        0x103,
        (
            "#12P#00200Fマリアベルさんには\x01",
            "色々とお世話になっていますしね。\x02",
        )
    )

    CloseMessageWindow()

    #C0532
    ChrTalk(
        0xA,
        "#5Pふふ、ありがとうございます。\x02",
    )

    CloseMessageWindow()

    #C0533
    ChrTalk(
        0xA,
        (
            "#5Pそれでは、カードを発行しますので\x01",
            "お受け取りくださいませ。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0534
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x324),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x324, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()

    #C0535
    ChrTalk(
        0x105,
        "#12P#10305Fふむ、これはどういうものなんだい？\x02",
    )

    CloseMessageWindow()

    #C0536
    ChrTalk(
        0x102,
        (
            "#6P#00100Fこれは私たちも以前受け取っていた\x01",
            "ＩＢＣの認証カードよ。\x02\x03",

            "#00103Fこれがあればエレベーターで\x01",
            "許可されたフロアに行けるようになるの。\x02",
        )
    )

    CloseMessageWindow()

    #C0537
    ChrTalk(
        0x109,
        (
            "#12P#10105Fなるほど、\x01",
            "セキュリティシステムですか。\x01",
            "流石は天下のＩＢＣですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0538
    ChrTalk(
        0xA,
        (
            "#5Pちなみにそのカードでは、\x01",
            "前回皆様に渡した時と同様のフロアに\x01",
            "降りることが出来ますわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0539
    ChrTalk(
        0xA,
        (
            "#5Pマリアベルお嬢様は１６階の総裁室で\x01",
            "お待ちしておりますので、\x01",
            "そちらへお越しくださいませ。\x02",
        )
    )

    CloseMessageWindow()

    #C0540
    ChrTalk(
        0x101,
        "#12P#00000Fはい、ありがとうございます。\x02",
    )

    CloseMessageWindow()
    ModifyEventFlags(0, 0, 0x80)
    OP_29(0x7A, 0x1, 0x0)
    SetScenarioFlags(0x157, 0)
    Return()

    # Function_27_B4B1 end

    def Function_28_B814(): pass

    label("Function_28_B814")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    FadeToBright(1000, 0)
    OP_0D()
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0541
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "クエスト【消えたコレクションの捜索】\x07\x00",
            "を達成した！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_29(0x7A, 0x4, 0x10)
    EventEnd(0x5)
    Return()

    # Function_28_B814 end

    def Function_29_B888(): pass

    label("Function_29_B888")

    EventBegin(0x0)
    SoundLoad(836)
    OP_4B(0xA, 0xFF)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-230, 1400, 29510, 0)
    MoveCamera(42, 21, 0, 0)
    OP_6E(590, 0)
    SetCameraDistance(15440, 0)
    SetChrPos(0x101, -470, 300, 28930, 0)
    SetChrPos(0x102, 540, 300, 28690, 0)
    SetChrPos(0x103, -1190, 300, 27930, 0)
    SetChrPos(0x104, -70, 300, 27510, 0)
    SetChrPos(0x109, 890, 300, 27020, 0)
    SetChrPos(0x105, -810, 300, 26570, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()

    #C0542
    ChrTalk(
        0xA,
        (
            "#5Pあら、特務支援課の皆様……\x01",
            "本日はどんなご用件でしょうか？\x02",
        )
    )

    CloseMessageWindow()

    #C0543
    ChrTalk(
        0x101,
        (
            "#00000Fええ、実は……\x01",
            "ＩＢＣに協力してもらいたい\x01",
            "捜査があるんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0544
    ChrTalk(
        0x102,
        (
            "#00100Fランフィさん、\x01",
            "ＩＢＣで使われている口座を\x01",
            "捜査することはできますか？\x02\x03",

            "それにあたって、\x01",
            "ある口座のミラの動きなどを\x01",
            "洗ってみたいんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0545
    ChrTalk(
        0xA,
        "#5Pまぁ……口座をですか？\x02",
    )

    CloseMessageWindow()

    #C0546
    ChrTalk(
        0xA,
        (
            "#5Pううん……\x01",
            "事件性が確認できるなら、\x01",
            "許可する事はできますが……\x02",
        )
    )

    CloseMessageWindow()

    #C0547
    ChrTalk(
        0xA,
        (
            "#5P……そうですね、まずは\x01",
            "詳しい事情をお聞かせ願えますか？\x02",
        )
    )

    CloseMessageWindow()

    #C0548
    ChrTalk(
        0x101,
        (
            "#00000Fええ、分かりました。\x01",
            "それでは……\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    #A0549
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ロイドは詐欺の疑いのある\x01",
            "今回の件について説明した。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0550
    ChrTalk(
        0xA,
        (
            "#5Pなるほど……\x01",
            "そういった事情でしたか。\x02",
        )
    )

    CloseMessageWindow()

    #C0551
    ChrTalk(
        0x103,
        (
            "#00200Fある程度の調査理由には\x01",
            "ならないでしょうか？\x02",
        )
    )

    CloseMessageWindow()

    #C0552
    ChrTalk(
        0x105,
        (
            "#10300FＩＢＣとしても、このまま犯罪に\x01",
            "口座が利用されたとなったら\x01",
            "信用問題にも関わるだろうしね。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0xFFFF)

    #C0553
    ChrTalk(
        0xA,
        (
            "#5Pそうですね、充分に\x01",
            "事件性が確認できるようですし……\x02",
        )
    )

    CloseMessageWindow()

    #C0554
    ChrTalk(
        0xA,
        (
            "#5P端末の情報を口頭で\x01",
            "お伝えする程度なら\x01",
            "許可できると思います。\x02",
        )
    )

    CloseMessageWindow()

    #C0555
    ChrTalk(
        0x101,
        (
            "#00000Fええ、それで結構です。\x01",
            "どうかよろしくお願いします。\x02",
        )
    )

    CloseMessageWindow()

    #C0556
    ChrTalk(
        0xA,
        "#5Pかしこまりました、それでは……\x02",
    )

    CloseMessageWindow()
    OP_93(0xA, 0x5A, 0x1F4)

    #C0557
    ChrTalk(
        0xA,
        (
            "#5P口座名義は『ミンネス』様……\x01",
            "（カタカタ、カタカタカタカタ）\x02",
        )
    )

    Sound(836, 0, 100, 0)
    CloseMessageWindow()

    #C0558
    ChrTalk(
        0xA,
        (
            "#5P『クインシー社』子会社、\x01",
            "『アルモリカ・ハニーカンパニー』……\x01",
            "（カタ、カタカタ、カタカタカタ）\x02",
        )
    )

    Sound(836, 0, 100, 0)
    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0xFFFF)
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0559
    ChrTalk(
        0xA,
        (
            "#5Pありました。\x01",
            "確かに開設なされてますね。\x02",
        )
    )

    CloseMessageWindow()

    #C0560
    ChrTalk(
        0xA,
        "#5P……あら……？\x02",
    )

    CloseMessageWindow()

    #C0561
    ChrTalk(
        0x109,
        (
            "#10100Fど、どうかしたんですか？\x02\x03",

            "やっぱり何か、\x01",
            "問題があったとか……\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xA, 0xB4, 0x1F4)

    #C0562
    ChrTalk(
        0xA,
        (
            "#5Pええと……詳しく預金額などを\x01",
            "お教えするわけには\x01",
            "いかないのですけれど……\x02",
        )
    )

    CloseMessageWindow()

    #C0563
    ChrTalk(
        0xA,
        (
            "#5P『アルモリカ・ハニーカンパニー』の口座には\x01",
            "最低限のミラしか預けられていないようです。\x02",
        )
    )

    CloseMessageWindow()

    #C0564
    ChrTalk(
        0x101,
        (
            "#00000Fえっと……\x01",
            "それってどういう……？\x02",
        )
    )

    CloseMessageWindow()

    #C0565
    ChrTalk(
        0xA,
        (
            "#5Pえ、ええとですね。\x01",
            "法人様向けの口座を開設するためには\x01",
            "資本金というものが必要なのですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0566
    ChrTalk(
        0xA,
        (
            "#5Pそれが、口座開設に必要な\x01",
            "最低限のミラ……つまり、\x01",
            "数万ミラ程度しか入っていないのです。\x02",
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

    #C0567
    ChrTalk(
        0x103,
        (
            "#00200F製菓工場の建造、\x01",
            "及び各畑などの管理……\x02\x03",

            "そんなことをするには\x01",
            "明らかにミラが足りていない……\x01",
            "そういうわけですか。\x02",
        )
    )

    CloseMessageWindow()

    #C0568
    ChrTalk(
        0x102,
        (
            "#00100F彼は土地の権利書を預かったり、\x01",
            "色々と取引きしてるはずなのに\x01",
            "その辺りに変更がないとすると……\x02\x03",

            "……うん、\x01",
            "かなり不自然だと言えるわね。\x02\x03",

            "デリックさんの信用を得るために\x01",
            "形だけの口座を用意した……\x01",
            "そんなところじゃないかしら。\x02",
        )
    )

    CloseMessageWindow()

    #C0569
    ChrTalk(
        0x105,
        (
            "#10300Fなるほどね。\x01",
            "フフ、これは明らかな矛盾じゃないか。\x02",
        )
    )

    CloseMessageWindow()

    #C0570
    ChrTalk(
        0x101,
        (
            "#00000Fああ、いい材料が手に入ったな。\x02\x03",

            "ランフィさん、\x01",
            "ご協力ありがとうございました。\x02",
        )
    )

    CloseMessageWindow()

    #C0571
    ChrTalk(
        0xA,
        (
            "#5Pいえ、私どもにできることなら\x01",
            "なんなりと……\x02",
        )
    )

    CloseMessageWindow()

    #C0572
    ChrTalk(
        0xA,
        (
            "#5Pまた何かありましたら\x01",
            "遠慮なくお越しくださいませ。\x02",
        )
    )

    CloseMessageWindow()

    #C0573
    ChrTalk(
        0x102,
        "#00100Fふふ、そうさせてもらいますね。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C46B")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    #A0574
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "◆マクダエル邸を（テスト用）\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【変更しない】\x01",                  # 0
            "【調べたことにする】\x01",            # 1
            "【調べていないことにする】\x01",      # 2
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
        (0, "loc_C456"),
        (1, "loc_C45B"),
        (2, "loc_C463"),
        (SWITCH_DEFAULT, "loc_C46B"),
    )


    label("loc_C456")

    Jump("loc_C46B")

    label("loc_C45B")

    SetScenarioFlags(0x177, 5)
    Jump("loc_C46B")

    label("loc_C463")

    ClearScenarioFlags(0x177, 5)
    Jump("loc_C46B")

    label("loc_C46B")

    OP_29(0x87, 0x1, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x177, 5)), scpexpr(EXPR_END)), "loc_C52A")
    OP_93(0x101, 0xB4, 0x1F4)
    Sleep(300)

    #C0575
    ChrTalk(
        0x101,
        (
            "#00000Fよし……ひとまずこれで、\x01",
            "ミンネスの疑惑を追及する\x01",
            "材料が集まったはずだ。\x02\x03",

            "一旦、ハロルドさんの家に\x01",
            "戻る事にしよう。\x02",
        )
    )

    CloseMessageWindow()

    #C0576
    ChrTalk(
        0x109,
        "#10100Fイエス・サー！\x02",
    )

    CloseMessageWindow()
    OP_29(0x87, 0x1, 0x4)
    Jump("loc_C599")

    label("loc_C52A")

    OP_93(0x101, 0xB4, 0x1F4)
    Sleep(300)

    #C0577
    ChrTalk(
        0x101,
        (
            "#00000F……残るはマクダエル邸での捜査だけだな。\x01",
            "早速調べにいくとしよう。\x02",
        )
    )

    CloseMessageWindow()

    #C0578
    ChrTalk(
        0x109,
        "#10100F了解です！\x02",
    )

    CloseMessageWindow()

    label("loc_C599")

    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetScenarioFlags(0x177, 4)
    SetChrPos(0x0, 0, 300, 28600, 180)
    OP_69(0xFF, 0x0)
    OP_4C(0xA, 0xFF)
    EventEnd(0x5)
    Return()

    # Function_29_B888 end

    def Function_30_C5D7(): pass

    label("Function_30_C5D7")

    EventBegin(0x1)
    OP_4B(0x8, 0xFF)
    TurnDirection(0x8, 0x0, 500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x134, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C68D")

    #C0579
    ChrTalk(
        0x8,
        (
            "君たち、エレベーターを使うのなら\x01",
            "認証カードが必要だぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0580
    ChrTalk(
        0x8,
        (
            "何か用事があるなら\x01",
            "受付に行って用件を伝えるといい。\x02",
        )
    )

    CloseMessageWindow()

    #C0581
    ChrTalk(
        0x101,
        "#00000Fええ、分かりました。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x134, 6)
    Jump("loc_C703")

    label("loc_C68D")


    #C0582
    ChrTalk(
        0x8,
        (
            "君たち、エレベーターを使うのなら\x01",
            "認証カードが必要だぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0583
    ChrTalk(
        0x8,
        (
            "何か用事があるなら\x01",
            "受付に行って用件を伝えるといい。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C703")

    Sleep(50)
    SetChrPos(0x0, 6280, 0, 15970, 270)
    OP_93(0x8, 0x10E, 0x0)
    OP_4C(0x8, 0xFF)
    EventEnd(0x4)
    Return()

    # Function_30_C5D7 end

    SaveToFile()

Try(main)
