from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t6010.bin",                # FileName
        "t6010",                    # MapName
        "t6010",                    # Location
        0x00A4,                     # MapIndex
        "ed7111",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x25,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 164, 0, 1, 0, 2],
    )

    BuildStringList((
        "t6010",                  # 0
        "ホアン事務長",           # 1
        "訓練生",                 # 2
        "訓練生",                 # 3
        "教官",                   # 4
        "受付嬢レベッカ",         # 5
        "ジョーリッジ課長",       # 6
        "警官",                   # 7
        "セルゲイ課長",           # 8
    ))

    AddCharChip((
        "chr/ch28000.itc",                   # 00
        "chr/ch30000.itc",                   # 01
        "chr/ch30600.itc",                   # 02
        "chr/ch30100.itc",                   # 03
        "chr/ch30400.itc",                   # 04
        "chr/ch30100.itc",                   # 05
        "chr/ch00000.itc",                   # 06
        "chr/ch00000.itc",                   # 07
        "chr/ch00000.itc",                   # 08
        "chr/ch00000.itc",                   # 09
        "chr/ch00000.itc",                   # 0A
        "chr/ch00000.itc",                   # 0B
        "chr/ch00000.itc",                   # 0C
        "chr/ch00000.itc",                   # 0D
        "chr/ch00000.itc",                   # 0E
        "chr/ch00000.itc",                   # 0F
        "chr/ch00000.itc",                   # 10
        "chr/ch00000.itc",                   # 11
        "chr/ch00000.itc",                   # 12
        "chr/ch00000.itc",                   # 13
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

    DeclNpc(0,       0,       15399,   180,  261,  0x0, 0,   0,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(15500,   0,       12250,   0,    389,  0x0, 0,   1,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(67300,   0,       5900,    270,  389,  0x0, 0,   2,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(18000,   0,       12250,   0,    389,  0x0, 0,   3,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(3200,    0,       16090,   90,   389,  0x0, 0,   4,   0,   0,   0,   0,   13,  255,  0)
    DeclNpc(67300,   0,       20149,   270,  389,  0x0, 0,   5,   0,   0,   0,   0,   24,  255,  0)
    DeclNpc(66099,   0,       20149,   90,   389,  0x0, 0,   1,   0,   0,   0,   0,   25,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclActor(0,       0,       14400,   1000,    0,       1500,    15400,   0x007E, 0,  3,  0x0000)
    DeclActor(2690,    0,       14400,   1000,    3200,    1500,    16090,   0x007E, 0,  12, 0x0000)
    DeclActor(20020,   0,       9890,    1000,    20020,   1500,    9890,    0x007C, 0,  31, 0x0000)
    DeclActor(15360,   0,       12700,   1000,    15360,   1500,    12700,   0x007C, 0,  32, 0x0000)
    DeclActor(17920,   0,       12660,   1000,    17920,   1500,    12660,   0x007C, 0,  32, 0x0000)

    ChipFrameInfo(804, 0)                                        # 0

    ScpFunction((
        "Function_0_324",          # 00, 0
        "Function_1_3DC",          # 01, 1
        "Function_2_563",          # 02, 2
        "Function_3_5A9",          # 03, 3
        "Function_4_5AD",          # 04, 4
        "Function_5_17EA",         # 05, 5
        "Function_6_2CBE",         # 06, 6
        "Function_7_2E91",         # 07, 7
        "Function_8_305A",         # 08, 8
        "Function_9_3710",         # 09, 9
        "Function_10_3BA8",        # 0A, 10
        "Function_11_3E8F",        # 0B, 11
        "Function_12_42ED",        # 0C, 12
        "Function_13_42F1",        # 0D, 13
        "Function_14_4C58",        # 0E, 14
        "Function_15_4CE8",        # 0F, 15
        "Function_16_4CF7",        # 10, 16
        "Function_17_6CB8",        # 11, 17
        "Function_18_6DC3",        # 12, 18
        "Function_19_7926",        # 13, 19
        "Function_20_85F9",        # 14, 20
        "Function_21_8F6D",        # 15, 21
        "Function_22_9055",        # 16, 22
        "Function_23_914A",        # 17, 23
        "Function_24_9E58",        # 18, 24
        "Function_25_9FCB",        # 19, 25
        "Function_26_A197",        # 1A, 26
        "Function_27_BA5A",        # 1B, 27
        "Function_28_BA8A",        # 1C, 28
        "Function_29_BABA",        # 1D, 29
        "Function_30_C568",        # 1E, 30
        "Function_31_C636",        # 1F, 31
        "Function_32_C68A",        # 20, 32
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

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_434")
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x10)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 17870, 0, 12360, 270)
    SetChrFlags(0x9, 0x10)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 16670, 0, 12360, 90)
    SetChrFlags(0xA, 0x10)
    Jump("loc_551")

    label("loc_434")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_47D")
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 67300, 0, 20150, 270)
    SetChrFlags(0x9, 0x10)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 66100, 0, 20150, 90)
    SetChrFlags(0xA, 0x10)
    ClearChrFlags(0xC, 0x80)
    Jump("loc_551")

    label("loc_47D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_490")
    ClearChrFlags(0xB, 0x80)
    Jump("loc_551")

    label("loc_490")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x163, 2)), scpexpr(EXPR_END)), "loc_4A3")
    ClearChrFlags(0xA, 0x80)
    Jump("loc_551")

    label("loc_4A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_4C7")
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 19000, 0, 9000, 90)
    Jump("loc_551")

    label("loc_4C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_4EB")
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 18000, 0, 12250, 0)
    Jump("loc_551")

    label("loc_4EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_50F")
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 66700, 0, 19750, 180)
    Jump("loc_551")

    label("loc_50F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_522")
    ClearChrFlags(0xA, 0x80)
    Jump("loc_551")

    label("loc_522")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_535")
    ClearChrFlags(0x9, 0x80)
    Jump("loc_551")

    label("loc_535")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 6)), scpexpr(EXPR_END)), "loc_548")
    ClearChrFlags(0xB, 0x80)
    Jump("loc_551")

    label("loc_548")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_551")

    label("loc_551")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_562")
    Event(0, 26)

    label("loc_562")

    Return()

    # Function_1_3DC end

    def Function_2_563(): pass

    label("Function_2_563")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_58C")
    SetMapObjFrame(0xFF, "t6010:Layer11", 0x0, 0x1)
    Sound(128, 1, 50, 0)

    label("loc_58C")

    OP_65(0x1, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5A2")
    OP_66(0x1, 0x1)

    label("loc_5A2")

    ClearMapObjFlags(0x7, 0x10)
    Return()

    # Function_2_563 end

    def Function_3_5A9(): pass

    label("Function_3_5A9")

    Call(0, 4)
    Return()

    # Function_3_5A9 end

    def Function_4_5AD(): pass

    label("Function_4_5AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_5C4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BC, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5C4")
    Call(0, 29)
    Return()

    label("loc_5C4")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20F, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20F, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_17D9")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5DF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17D4")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "話をする\x01",              # 0
            "予想外料理を渡す\x01",      # 1
            "やめる\x01",                # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_641")
    FadeToBright(300, 0)
    OP_0D()

    label("loc_641")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_662")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 5)
    Jump("loc_17CF")

    label("loc_662")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17CF")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_67B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17C5")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuCmd(0, 1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20C, 0)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x192, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_6CE")
    MenuCmd(1, 1, "極苦麺≪断頭≫")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20C, 0)), scpexpr(EXPR_END)), "loc_6C4")
    Call(0, 7)

    label("loc_6C4")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20C, 1)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x195, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_707")
    MenuCmd(1, 1, "煉獄麻婆≪閻魔≫")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20C, 1)), scpexpr(EXPR_END)), "loc_6FD")
    Call(0, 7)

    label("loc_6FD")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_707")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20C, 2)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x198, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_73C")
    MenuCmd(1, 1, "まだら焦げ飯")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20C, 2)), scpexpr(EXPR_END)), "loc_732")
    Call(0, 7)

    label("loc_732")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_73C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20C, 3)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x19B, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_771")
    MenuCmd(1, 1, "頑固肉≪巌≫")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20C, 3)), scpexpr(EXPR_END)), "loc_767")
    Call(0, 7)

    label("loc_767")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_771")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20C, 4)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x19E, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_7AA")
    MenuCmd(1, 1, "混沌煮込み≪濁≫")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20C, 4)), scpexpr(EXPR_END)), "loc_7A0")
    Call(0, 7)

    label("loc_7A0")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_7AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20C, 5)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1A1, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_7DF")
    MenuCmd(1, 1, "男料理≪山≫")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20C, 5)), scpexpr(EXPR_END)), "loc_7D5")
    Call(0, 7)

    label("loc_7D5")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_7DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20C, 6)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1A4, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_814")
    MenuCmd(1, 1, "男料理≪川≫")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20C, 6)), scpexpr(EXPR_END)), "loc_80A")
    Call(0, 7)

    label("loc_80A")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_814")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20C, 7)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1A7, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_84D")
    MenuCmd(1, 1, "フィッシュアロー")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20C, 7)), scpexpr(EXPR_END)), "loc_843")
    Call(0, 7)

    label("loc_843")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_84D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20D, 0)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1AA, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_884")
    MenuCmd(1, 1, "激辛ボムライス")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20D, 0)), scpexpr(EXPR_END)), "loc_87A")
    Call(0, 7)

    label("loc_87A")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_884")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20D, 1)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1AD, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8BB")
    MenuCmd(1, 1, "ニードルパスタ")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20D, 1)), scpexpr(EXPR_END)), "loc_8B1")
    Call(0, 7)

    label("loc_8B1")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20D, 2)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1B0, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8F2")
    MenuCmd(1, 1, "ビターバーガー")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20D, 2)), scpexpr(EXPR_END)), "loc_8E8")
    Call(0, 7)

    label("loc_8E8")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20D, 3)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1B3, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_92D")
    MenuCmd(1, 1, "クワトロトマトピザ")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20D, 3)), scpexpr(EXPR_END)), "loc_923")
    Call(0, 7)

    label("loc_923")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_92D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20D, 4)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1B6, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_964")
    MenuCmd(1, 1, "プロテクサンド")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20D, 4)), scpexpr(EXPR_END)), "loc_95A")
    Call(0, 7)

    label("loc_95A")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_964")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20D, 5)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1B9, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_99F")
    MenuCmd(1, 1, "不思議弁当≪仰天≫")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20D, 5)), scpexpr(EXPR_END)), "loc_995")
    Call(0, 7)

    label("loc_995")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_99F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20D, 6)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1BC, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9D4")
    MenuCmd(1, 1, "マジカスープ")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20D, 6)), scpexpr(EXPR_END)), "loc_9CA")
    Call(0, 7)

    label("loc_9CA")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20D, 7)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1BF, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A0F")
    MenuCmd(1, 1, "エニグマキャンディ")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20D, 7)), scpexpr(EXPR_END)), "loc_A05")
    Call(0, 7)

    label("loc_A05")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A0F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20E, 0)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1C2, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A48")
    MenuCmd(1, 1, "リフレクショコラ")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20E, 0)), scpexpr(EXPR_END)), "loc_A3E")
    Call(0, 7)

    label("loc_A3E")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A48")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20E, 1)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1C5, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A7F")
    MenuCmd(1, 1, "プルプルプリン")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20E, 1)), scpexpr(EXPR_END)), "loc_A75")
    Call(0, 7)

    label("loc_A75")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A7F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20E, 2)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1C8, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_AB6")
    MenuCmd(1, 1, "リカバリアイス")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20E, 2)), scpexpr(EXPR_END)), "loc_AAC")
    Call(0, 7)

    label("loc_AAC")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_AB6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20E, 3)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1CB, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_AEF")
    MenuCmd(1, 1, "隠密ポップコーン")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20E, 3)), scpexpr(EXPR_END)), "loc_AE5")
    Call(0, 7)

    label("loc_AE5")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_AEF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20E, 4)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1CE, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_B24")
    MenuCmd(1, 1, "良薬≪熊笹≫")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20E, 4)), scpexpr(EXPR_END)), "loc_B1A")
    Call(0, 7)

    label("loc_B1A")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_B24")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20E, 5)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1D1, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_B5D")
    MenuCmd(1, 1, "パープルリキッド")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20E, 5)), scpexpr(EXPR_END)), "loc_B53")
    Call(0, 7)

    label("loc_B53")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_B5D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20E, 6)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1D4, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_B96")
    MenuCmd(1, 1, "ブラウンリキッド")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20E, 6)), scpexpr(EXPR_END)), "loc_B8C")
    Call(0, 7)

    label("loc_B8C")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_B96")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20E, 7)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1D7, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_BCF")
    MenuCmd(1, 1, "ももいろリキッド")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20E, 7)), scpexpr(EXPR_END)), "loc_BC5")
    Call(0, 7)

    label("loc_BC5")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_BCF")

    MenuCmd(1, 1, "やめる")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuCmd(2, 1, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x1)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_C4F")
    FadeToBright(300, 0)
    OP_0D()

    #C0001
    ChrTalk(
        0x8,
        (
            "ありがとう、また良さそうな物が\x01",
            "あったら頼むよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17C0")

    label("loc_C4F")

    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20C, 0)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x192, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_CC8")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CBE")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x192, 1)
    SetScenarioFlags(0x20C, 0)

    #A0002
    AnonymousTalk(
        0xFF,
        (
            "ホアン事務長に",
            scpstr(SCPSTR_CODE_ITEM, 0x192),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を渡した。\x02",
        )
    )


    label("loc_CBE")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_CC8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20C, 1)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x195, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_D22")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D18")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x195, 1)
    SetScenarioFlags(0x20C, 1)

    #A0003
    AnonymousTalk(
        0xFF,
        (
            "ホアン事務長に",
            scpstr(SCPSTR_CODE_ITEM, 0x195),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を渡した。\x02",
        )
    )


    label("loc_D18")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_D22")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20C, 2)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x198, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_D7C")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D72")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x198, 1)
    SetScenarioFlags(0x20C, 2)

    #A0004
    AnonymousTalk(
        0xFF,
        (
            "ホアン事務長に",
            scpstr(SCPSTR_CODE_ITEM, 0x198),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を渡した。\x02",
        )
    )


    label("loc_D72")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_D7C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20C, 3)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x19B, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_DD6")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DCC")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x19B, 1)
    SetScenarioFlags(0x20C, 3)

    #A0005
    AnonymousTalk(
        0xFF,
        (
            "ホアン事務長に",
            scpstr(SCPSTR_CODE_ITEM, 0x19B),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を渡した。\x02",
        )
    )


    label("loc_DCC")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_DD6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20C, 4)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x19E, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_E30")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E26")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x19E, 1)
    SetScenarioFlags(0x20C, 4)

    #A0006
    AnonymousTalk(
        0xFF,
        (
            "ホアン事務長に",
            scpstr(SCPSTR_CODE_ITEM, 0x19E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を渡した。\x02",
        )
    )


    label("loc_E26")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_E30")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20C, 5)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1A1, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_E8A")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E80")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x1A1, 1)
    SetScenarioFlags(0x20C, 5)

    #A0007
    AnonymousTalk(
        0xFF,
        (
            "ホアン事務長に",
            scpstr(SCPSTR_CODE_ITEM, 0x1A1),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を渡した。\x02",
        )
    )


    label("loc_E80")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_E8A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20C, 6)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1A4, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_EE4")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EDA")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x1A4, 1)
    SetScenarioFlags(0x20C, 6)

    #A0008
    AnonymousTalk(
        0xFF,
        (
            "ホアン事務長に",
            scpstr(SCPSTR_CODE_ITEM, 0x1A4),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を渡した。\x02",
        )
    )


    label("loc_EDA")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_EE4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20C, 7)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1A7, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_F3E")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F34")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x1A7, 1)
    SetScenarioFlags(0x20C, 7)

    #A0009
    AnonymousTalk(
        0xFF,
        (
            "ホアン事務長に",
            scpstr(SCPSTR_CODE_ITEM, 0x1A7),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を渡した。\x02",
        )
    )


    label("loc_F34")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_F3E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20D, 0)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1AA, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_F98")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F8E")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x1AA, 1)
    SetScenarioFlags(0x20D, 0)

    #A0010
    AnonymousTalk(
        0xFF,
        (
            "ホアン事務長に",
            scpstr(SCPSTR_CODE_ITEM, 0x1AA),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を渡した。\x02",
        )
    )


    label("loc_F8E")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_F98")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20D, 1)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1AD, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_FF2")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FE8")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x1AD, 1)
    SetScenarioFlags(0x20D, 1)

    #A0011
    AnonymousTalk(
        0xFF,
        (
            "ホアン事務長に",
            scpstr(SCPSTR_CODE_ITEM, 0x1AD),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を渡した。\x02",
        )
    )


    label("loc_FE8")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_FF2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20D, 2)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1B0, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_104C")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1042")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x1B0, 1)
    SetScenarioFlags(0x20D, 2)

    #A0012
    AnonymousTalk(
        0xFF,
        (
            "ホアン事務長に",
            scpstr(SCPSTR_CODE_ITEM, 0x1B0),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を渡した。\x02",
        )
    )


    label("loc_1042")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_104C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20D, 3)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1B3, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_10A6")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_109C")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x1B3, 1)
    SetScenarioFlags(0x20D, 3)

    #A0013
    AnonymousTalk(
        0xFF,
        (
            "ホアン事務長に",
            scpstr(SCPSTR_CODE_ITEM, 0x1B3),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を渡した。\x02",
        )
    )


    label("loc_109C")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_10A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20D, 4)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1B6, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1100")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10F6")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x1B6, 1)
    SetScenarioFlags(0x20D, 4)

    #A0014
    AnonymousTalk(
        0xFF,
        (
            "ホアン事務長に",
            scpstr(SCPSTR_CODE_ITEM, 0x1B6),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を渡した。\x02",
        )
    )


    label("loc_10F6")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_1100")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20D, 5)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1B9, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_115A")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1150")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x1B9, 1)
    SetScenarioFlags(0x20D, 5)

    #A0015
    AnonymousTalk(
        0xFF,
        (
            "ホアン事務長に",
            scpstr(SCPSTR_CODE_ITEM, 0x1B9),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を渡した。\x02",
        )
    )


    label("loc_1150")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_115A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20D, 6)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1BC, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_11B4")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11AA")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x1BC, 1)
    SetScenarioFlags(0x20D, 6)

    #A0016
    AnonymousTalk(
        0xFF,
        (
            "ホアン事務長に",
            scpstr(SCPSTR_CODE_ITEM, 0x1BC),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を渡した。\x02",
        )
    )


    label("loc_11AA")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_11B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20D, 7)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1BF, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_120E")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1204")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x1BF, 1)
    SetScenarioFlags(0x20D, 7)

    #A0017
    AnonymousTalk(
        0xFF,
        (
            "ホアン事務長に",
            scpstr(SCPSTR_CODE_ITEM, 0x1BF),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を渡した。\x02",
        )
    )


    label("loc_1204")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_120E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20E, 0)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1C2, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1268")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_125E")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x1C2, 1)
    SetScenarioFlags(0x20E, 0)

    #A0018
    AnonymousTalk(
        0xFF,
        (
            "ホアン事務長に",
            scpstr(SCPSTR_CODE_ITEM, 0x1C2),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を渡した。\x02",
        )
    )


    label("loc_125E")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_1268")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20E, 1)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1C5, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_12C2")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12B8")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x1C5, 1)
    SetScenarioFlags(0x20E, 1)

    #A0019
    AnonymousTalk(
        0xFF,
        (
            "ホアン事務長に",
            scpstr(SCPSTR_CODE_ITEM, 0x1C5),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を渡した。\x02",
        )
    )


    label("loc_12B8")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_12C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20E, 2)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1C8, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_131C")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1312")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x1C8, 1)
    SetScenarioFlags(0x20E, 2)

    #A0020
    AnonymousTalk(
        0xFF,
        (
            "ホアン事務長に",
            scpstr(SCPSTR_CODE_ITEM, 0x1C8),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を渡した。\x02",
        )
    )


    label("loc_1312")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_131C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20E, 3)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1CB, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1376")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_136C")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x1CB, 1)
    SetScenarioFlags(0x20E, 3)

    #A0021
    AnonymousTalk(
        0xFF,
        (
            "ホアン事務長に",
            scpstr(SCPSTR_CODE_ITEM, 0x1CB),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を渡した。\x02",
        )
    )


    label("loc_136C")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_1376")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20E, 4)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1CE, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_13D0")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13C6")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x1CE, 1)
    SetScenarioFlags(0x20E, 4)

    #A0022
    AnonymousTalk(
        0xFF,
        (
            "ホアン事務長に",
            scpstr(SCPSTR_CODE_ITEM, 0x1CE),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を渡した。\x02",
        )
    )


    label("loc_13C6")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_13D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20E, 5)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1D1, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_142A")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1420")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x1D1, 1)
    SetScenarioFlags(0x20E, 5)

    #A0023
    AnonymousTalk(
        0xFF,
        (
            "ホアン事務長に",
            scpstr(SCPSTR_CODE_ITEM, 0x1D1),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を渡した。\x02",
        )
    )


    label("loc_1420")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_142A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20E, 6)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1D4, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1484")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_147A")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x1D4, 1)
    SetScenarioFlags(0x20E, 6)

    #A0024
    AnonymousTalk(
        0xFF,
        (
            "ホアン事務長に",
            scpstr(SCPSTR_CODE_ITEM, 0x1D4),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を渡した。\x02",
        )
    )


    label("loc_147A")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_1484")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20E, 7)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1D7, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_14DE")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14D4")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x1D7, 1)
    SetScenarioFlags(0x20E, 7)

    #A0025
    AnonymousTalk(
        0xFF,
        (
            "ホアン事務長に",
            scpstr(SCPSTR_CODE_ITEM, 0x1D7),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を渡した。\x02",
        )
    )


    label("loc_14D4")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_14DE")

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Call(0, 6)
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17B6")
    FadeToBright(300, 0)
    OP_0D()

    #C0026
    ChrTalk(
        0x8,
        (
            "おっと、随分とたくさん\x01",
            "『変わった料理』を持ってきて\x01",
            "くれたみたいだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x8,
        (
            "これなら鑑識班の研修も\x01",
            "当分まかなえるはずだ。\x01",
            "……ありがとう、本当に助かったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x101,
        (
            "#00000Fはは、気にしないで下さい。\x01",
            "大した物でもないですし……\x02\x03",

            "一応母校の役に\x01",
            "立てたみたいですから。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x8,
        (
            "ロイド君は殊勝だなぁ……\x01",
            "うん、そういう所は学生時代から\x01",
            "変わってないよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x8,
        (
            "そうだ、よかったら\x01",
            "今日はこれを持って行ってくれないか。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x8,
        (
            "最近研修でも使い始めた\x01",
            "エニグマⅡ用のクオーツなんだが、\x01",
            "備品が１つ余っていてね。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0032
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0xBD),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を受け取った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0xBD, 1)
    SetMessageWindowPos(14, 280, 60, 3)

    #C0033
    ChrTalk(
        0x101,
        (
            "#00000Fありがとうございます、\x01",
            "ホアン事務長。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x8,
        (
            "いやいや、こちらこそだ。\x01",
            "また何かあればよろしく頼むよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x20F, 1)
    TalkEnd(0x8)
    Return()

    label("loc_17B6")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_17C0")

    Jump("loc_67B")

    label("loc_17C5")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_17CF")

    Jump("loc_5DF")

    label("loc_17D4")

    Jump("loc_17E6")

    label("loc_17D9")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 5)

    label("loc_17E6")

    TalkEnd(0x8)
    Return()

    # Function_4_5AD end

    def Function_5_17EA(): pass

    label("Function_5_17EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1955")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18D4")

    #C0035
    ChrTalk(
        0x8,
        (
            "大統領が拘束されたとの\x01",
            "一報が入って、国防軍は\x01",
            "撤退していったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x8,
        (
            "各地の混乱を収めるためにも、\x01",
            "国防軍には頑張ってもらわないと\x01",
            "いけないからね。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x8,
        (
            "私たちも、私たちの\x01",
            "できることをしていかないとな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1950")

    label("loc_18D4")


    #C0038
    ChrTalk(
        0x8,
        (
            "今は、本部から来た応援部隊が\x01",
            "この付近の混乱を収拾しているんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x8,
        (
            "私たちも、私たちの\x01",
            "できることをしていかないとな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1950")

    Jump("loc_2CBA")

    label("loc_1955")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1AC8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A32")

    #C0040
    ChrTalk(
        0x8,
        (
            "……あの襲撃事件は、\x01",
            "あまりにも凄惨だった。\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x8,
        (
            "この警察学校の敷地と\x01",
            "若き警察官たちが無事だったのは\x01",
            "不幸中の幸いだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x8,
        (
            "クロスベルが完全に立ち直るには\x01",
            "まだまだ時間がかかりそうだね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1AC3")

    label("loc_1A32")


    #C0043
    ChrTalk(
        0x8,
        (
            "……あの襲撃事件で、\x01",
            "若き警察官たちが無事だったのは\x01",
            "不幸中の幸いだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x8,
        (
            "クロスベルが完全に立ち直るには\x01",
            "まだまだ時間がかかりそうだね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1AC3")

    Jump("loc_2CBA")

    label("loc_1AC8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1C35")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1BAB")

    #C0045
    ChrTalk(
        0x8,
        (
            "昨日壊されてしまったゲートは、\x01",
            "新しいものの用意に\x01",
            "少々時間がかかりそうだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x8,
        (
            "まさか、あんな壊れ方をするなんて\x01",
            "思いも寄らなかったからね……\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x8,
        (
            "しばらくは警備隊に\x01",
            "警備を頼むしかないだろうね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1C30")

    label("loc_1BAB")


    #C0048
    ChrTalk(
        0x8,
        (
            "昨日壊されてしまったゲートは、\x01",
            "新しいものの用意に\x01",
            "少々時間がかかりそうだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x8,
        (
            "しばらくは警備隊に\x01",
            "警備を頼むしかないだろうね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C30")

    Jump("loc_2CBA")

    label("loc_1C35")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x163, 2)), scpexpr(EXPR_END)), "loc_1EBA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x170, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E53")

    #C0050
    ChrTalk(
        0x8,
        "おお、ロイド君たちか。\x02",
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x8,
        (
            "さっき、敷地内で\x01",
            "ものすごい音が聞こえたが……\x01",
            "あれは一体何だったんだ？\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x101,
        (
            "#00000F……先ほど、敷地前のゲートが\x01",
            "破壊されてしまったのを確認しました。\x01",
            "多分、その音だと思います。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0053
    ChrTalk(
        0x8,
        (
            "な、なんだって！？\x01",
            "あの特殊合金製ゲートを……\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x8,
        (
            "まさか《幻獣》か……？\x01",
            "そこまでのパワーがあるなんて\x01",
            "報告にはなかったが。\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x103,
        (
            "#00200Fまだ私たちも\x01",
            "なんとも言えませんが……\x02\x03",

            "こちらに来る可能性は\x01",
            "決してゼロではないはずです。\x01",
            "……充分に警戒を。\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x8,
        "あ、ああ……君たちもな。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x170, 0)
    Jump("loc_1EB5")

    label("loc_1E53")


    #C0057
    ChrTalk(
        0x8,
        (
            "私たちも、周囲には充分に\x01",
            "警戒しておくとしよう。\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x8,
        (
            "君たち……\x01",
            "くれぐれも気をつけたまえよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1EB5")

    Jump("loc_2CBA")

    label("loc_1EBA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1F38")

    #C0059
    ChrTalk(
        0x8,
        (
            "今日は森林地帯では\x01",
            "幻獣の目撃情報もないようだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x8,
        (
            "遊撃士たちも、今日は別の場所を\x01",
            "調査しているようだね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2CBA")

    label("loc_1F38")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_20DC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2043")

    #C0061
    ChrTalk(
        0x8,
        (
            "《幻獣》とやらは、\x01",
            "ノックスの森林地帯でも\x01",
            "目撃されていてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x8,
        (
            "リン君、エオリア君という\x01",
            "遊撃士が退治に当たったが、\x01",
            "結局退治には至らなかったそうだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x8,
        (
            "あそこは警備隊の演習地だし、\x01",
            "今後の事を考えると\x01",
            "警戒は続けた方がよさそうだね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_20D7")

    label("loc_2043")


    #C0064
    ChrTalk(
        0x8,
        (
            "《幻獣》とやらは、\x01",
            "ノックスの森林地帯でも\x01",
            "目撃されていてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x8,
        (
            "どこかへ逃げたそうだが……\x01",
            "今後の事を考えると\x01",
            "警戒は続けた方がよさそうだね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_20D7")

    Jump("loc_2CBA")

    label("loc_20DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_226F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_21F6")

    #C0066
    ChrTalk(
        0x8,
        (
            "警察学校のカリキュラムは、\x01",
            "半年間みっちりと行われる。\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x8,
        (
            "座学と訓練が主となり、\x01",
            "卒業後は適正に応じて\x01",
            "様々な部署に配属されるわけだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x8,
        (
            "いわば、警察官の雛鳥たちに\x01",
            "最初の飛び方を教える場所……\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x8,
        (
            "ここに勤めていることに、\x01",
            "私は誇りを感じているよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_226A")

    label("loc_21F6")


    #C0070
    ChrTalk(
        0x8,
        (
            "警察官の雛鳥たちに\x01",
            "最初の飛び方を教える場所……\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x8,
        (
            "この警察学校に勤めていることに、\x01",
            "私は誇りを感じているよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_226A")

    Jump("loc_2CBA")

    label("loc_226F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_26C8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14F, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_262E")

    #C0072
    ChrTalk(
        0x8,
        (
            "警備隊副司令になったダグラス君は、\x01",
            "しばらくの間、ここで教官をしていた。\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0x8,
        (
            "主に訓練を担当して教え、\x01",
            "演習場にもよく顔を出していたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x101,
        (
            "#00000Fはは……\x01",
            "本当、厳しい人でしたよ。\x02\x03",

            "#00008F１人、また１人と訓練から\x01",
            "脱落していくあの地獄絵図……\x02\x03",

            "#00006F今思い出しても\x01",
            "震えが止まらないというか。\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0x104,
        (
            "#00306Fまー、あの兄さんは\x01",
            "爽やかに笑いながら無理難題を\x01",
            "突きつけてくるタイプだからなあ。\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x105,
        (
            "#10302Fフフ、この間言っていた\x01",
            "『鬼のダグラス』たる由縁だね。\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0x109,
        (
            "#10100Fでも、警備隊のホープから\x01",
            "戦闘技術を学べるなんて、\x01",
            "あたしはうらやましいです。\x02\x03",

            "#10104Fできればあたしも、新人時代に\x01",
            "学びたかったくらいですし。\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0x101,
        (
            "#00009Fま、まあ感謝はしてるよ。\x01",
            "教えてもらったことは実戦で\x01",
            "何度も役に立ってるしな。\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0x8,
        (
            "実際、ロイド君を含めて\x01",
            "彼のおかげで優秀な警察官が\x01",
            "何人も輩出されたからね。\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0x8,
        (
            "警察学校としては、何としても\x01",
            "手放したくない人材だったんだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0x8,
        (
            "まあ、元々警備隊出身だし、\x01",
            "ソーニャ司令の要請だから\x01",
            "仕方の無いことだけどね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x14F, 6)
    Jump("loc_26C3")

    label("loc_262E")


    #C0082
    ChrTalk(
        0x8,
        (
            "ダグラス君は警察学校としても、\x01",
            "手放したくなかったんだがねえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x8,
        (
            "まあ、元々警備隊出身だし、\x01",
            "ソーニャ司令の要請だから\x01",
            "仕方の無いことだけどね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_26C3")

    Jump("loc_2CBA")

    label("loc_26C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_29FC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14F, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2973")

    #C0084
    ChrTalk(
        0x8,
        "おや、特務支援課の諸君か。\x02",
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0x8,
        (
            "セルゲイ君に聞いたが、\x01",
            "あの新型導力車を毎日\x01",
            "乗り回しているらしいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x101,
        (
            "#00000Fはは、ええまあ。\x01",
            "市外活動にも大いに\x01",
            "役立たせてもらっていますよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x8,
        (
            "まあ、交通ルールをよく守って\x01",
            "運転することだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0x8,
        (
            "警察官が交通事故を起こしました……\x01",
            "なんて、笑い話にもならないからね。\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0x105,
        "#10300Fフフ、だってさ。\x02",
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x109,
        (
            "#10105Fあ、あたしはそんな、\x01",
            "事故なんて……！\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x104,
        (
            "#00300Fまー、ノエルは\x01",
            "スピード狂とかとは\x01",
            "違うだろうが……\x02\x03",

            "#00304F導力車ラブが過ぎて、\x01",
            "視野が狭まるなんてことも\x01",
            "ありえるかもしれねえしなあ。\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0x109,
        "#10106Fせ、先輩まで……\x02",
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x102,
        (
            "#00100Fまあ、まだ私たちも\x01",
            "完全に慣れたわけではないし……\x01",
            "皆で肝に銘じておきましょう。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x14F, 5)
    Jump("loc_29F7")

    label("loc_2973")


    #C0094
    ChrTalk(
        0x8,
        (
            "車を運転するなら、\x01",
            "交通ルールをよく守らなくてはね。\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0x8,
        (
            "警察官が交通事故を起こしました……\x01",
            "なんて、笑い話にもならないからね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_29F7")

    Jump("loc_2CBA")

    label("loc_29FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_2CBA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x139, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C3E")

    #C0096
    ChrTalk(
        0x8,
        "君たち、講習は終わったようだね。\x02",
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0x8,
        "これからいよいよ実技という所かな？\x02",
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x101,
        "#00000Fはは、まあそんな所です。\x02",
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0x105,
        (
            "#10304Fしかし、あの課長さんが\x01",
            "講習なんかできるとは、\x01",
            "結構意外だったね。\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0x8,
        (
            "彼は、警察学校では\x01",
            "車両運転の教官を\x01",
            "兼任していたからね。\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0x8,
        (
            "ふふ、さぞ分かりやすかった\x01",
            "ことだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x102,
        (
            "#00105Fあ、そういえばそんな事を\x01",
            "前に言っていました。\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0x109,
        (
            "#10104Fうーん、セルゲイ課長も\x01",
            "なかなか謎の多い方ですよね。\x02\x03",

            "#10101F個人的にはソーニャ司令との\x01",
            "関係とかも気になりますけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0x101,
        (
            "#00003Fまあ、あまり自分の事を\x01",
            "話したがらない人だからなあ……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x139, 5)
    Jump("loc_2CBA")

    label("loc_2C3E")


    #C0105
    ChrTalk(
        0x8,
        (
            "それはそうと、セルゲイ君が\x01",
            "外で待っているんじゃないかね？\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0x8,
        (
            "あまり上司を待たせるものじゃない。\x01",
            "早く行ってきたまえ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2CBA")

    Call(0, 8)
    Return()

    # Function_5_17EA end

    def Function_6_2CBE(): pass

    label("Function_6_2CBE")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20C, 0)), scpexpr(EXPR_END)), "loc_2CDB")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2CDB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20C, 1)), scpexpr(EXPR_END)), "loc_2CEE")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2CEE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20C, 2)), scpexpr(EXPR_END)), "loc_2D01")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2D01")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20C, 3)), scpexpr(EXPR_END)), "loc_2D14")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2D14")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20C, 4)), scpexpr(EXPR_END)), "loc_2D27")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2D27")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20C, 5)), scpexpr(EXPR_END)), "loc_2D3A")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2D3A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20C, 6)), scpexpr(EXPR_END)), "loc_2D4D")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2D4D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20C, 7)), scpexpr(EXPR_END)), "loc_2D60")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2D60")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20D, 0)), scpexpr(EXPR_END)), "loc_2D73")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2D73")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20D, 1)), scpexpr(EXPR_END)), "loc_2D86")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2D86")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20D, 2)), scpexpr(EXPR_END)), "loc_2D99")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2D99")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20D, 3)), scpexpr(EXPR_END)), "loc_2DAC")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2DAC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20D, 4)), scpexpr(EXPR_END)), "loc_2DBF")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2DBF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20D, 5)), scpexpr(EXPR_END)), "loc_2DD2")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2DD2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20D, 6)), scpexpr(EXPR_END)), "loc_2DE5")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2DE5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20D, 7)), scpexpr(EXPR_END)), "loc_2DF8")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2DF8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20E, 0)), scpexpr(EXPR_END)), "loc_2E0B")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2E0B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20E, 1)), scpexpr(EXPR_END)), "loc_2E1E")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2E1E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20E, 2)), scpexpr(EXPR_END)), "loc_2E31")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2E31")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20E, 3)), scpexpr(EXPR_END)), "loc_2E44")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2E44")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20E, 4)), scpexpr(EXPR_END)), "loc_2E57")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2E57")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20E, 5)), scpexpr(EXPR_END)), "loc_2E6A")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2E6A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20E, 6)), scpexpr(EXPR_END)), "loc_2E7D")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2E7D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20E, 7)), scpexpr(EXPR_END)), "loc_2E90")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2E90")

    Return()

    # Function_6_2CBE end

    def Function_7_2E91(): pass

    label("Function_7_2E91")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2EA4")
    MenuCmd(3, 1, 0x0)

    label("loc_2EA4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2EB7")
    MenuCmd(3, 1, 0x1)

    label("loc_2EB7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2ECA")
    MenuCmd(3, 1, 0x2)

    label("loc_2ECA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2EDD")
    MenuCmd(3, 1, 0x3)

    label("loc_2EDD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2EF0")
    MenuCmd(3, 1, 0x4)

    label("loc_2EF0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F03")
    MenuCmd(3, 1, 0x5)

    label("loc_2F03")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F16")
    MenuCmd(3, 1, 0x6)

    label("loc_2F16")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F29")
    MenuCmd(3, 1, 0x7)

    label("loc_2F29")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F3C")
    MenuCmd(3, 1, 0x8)

    label("loc_2F3C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F4F")
    MenuCmd(3, 1, 0x9)

    label("loc_2F4F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F62")
    MenuCmd(3, 1, 0xA)

    label("loc_2F62")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F75")
    MenuCmd(3, 1, 0xB)

    label("loc_2F75")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F88")
    MenuCmd(3, 1, 0xC)

    label("loc_2F88")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F9B")
    MenuCmd(3, 1, 0xD)

    label("loc_2F9B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2FAE")
    MenuCmd(3, 1, 0xE)

    label("loc_2FAE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2FC1")
    MenuCmd(3, 1, 0xF)

    label("loc_2FC1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2FD4")
    MenuCmd(3, 1, 0x10)

    label("loc_2FD4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x11), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2FE7")
    MenuCmd(3, 1, 0x11)

    label("loc_2FE7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x12), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2FFA")
    MenuCmd(3, 1, 0x12)

    label("loc_2FFA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x13), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_300D")
    MenuCmd(3, 1, 0x13)

    label("loc_300D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3020")
    MenuCmd(3, 1, 0x14)

    label("loc_3020")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x15), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3033")
    MenuCmd(3, 1, 0x15)

    label("loc_3033")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x16), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3046")
    MenuCmd(3, 1, 0x16)

    label("loc_3046")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x17), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3059")
    MenuCmd(3, 1, 0x17)

    label("loc_3059")

    Return()

    # Function_7_2E91 end

    def Function_8_305A(): pass

    label("Function_8_305A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20F, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_370F")
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0107
    ChrTalk(
        0x8,
        (
            "それはそうと……君たち、\x01",
            "突然だけど何か『変わった料理』を\x01",
            "持っていたりしないかい？\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0x101,
        "#00005F『変わった料理』、ですか……？\x02",
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0x8,
        (
            "ああ、実は鑑識班の研修に使う\x01",
            "サンプルを探していてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0x8,
        (
            "成分が推測しづらいような、\x01",
            "そんな料理であれば助かるんだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0x101,
        (
            "#00004Fなるほど、鑑識用のサンプルですか。\x02\x03",

            "#00005Fでも……変わった料理といっても\x01",
            "具体的にどういうものだったら\x01",
            "いいんでしょうか？\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0x102,
        (
            "#00100Fそうねぇ、クロスベル警察の\x01",
            "鑑識班といえば\x01",
            "高度な分析設備で有名だし……\x02\x03",

            "#00106F料理の専門家でもない私たちが、\x01",
            "お役に立てるかどうか。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_333A")

    #C0113
    ChrTalk(
        0x103,
        (
            "#00200Fあまり硬く考えなくてもいいのでは？\x02\x03",

            "#00203F普通に料理をしているだけでも、\x01",
            "わたしたちでも予想しなかったものが\x01",
            "完成することもありますし。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_345C")

    label("loc_333A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_33D2")

    #C0114
    ChrTalk(
        0x105,
        (
            "#10404Fフフ、硬く考える必要はないんじゃない？\x02\x03",

            "#10400F普通に料理をしているだけでも、\x01",
            "予想しなかったものが\x01",
            "できちゃうことがあるしね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_345C")

    label("loc_33D2")


    #C0115
    ChrTalk(
        0x105,
        (
            "#10304Fフフ、硬く考える必要はないんじゃない？\x02\x03",

            "#10300F普通に料理をしているだけでも、\x01",
            "予想しなかったものが\x01",
            "できちゃうことがあるしね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_345C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_34C4")

    #C0116
    ChrTalk(
        0x109,
        (
            "#10106Fた、確かに……\x01",
            "ときどき妙な化学反応みたいなのが\x01",
            "起きることがあるよね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_351D")

    label("loc_34C4")


    #C0117
    ChrTalk(
        0x104,
        (
            "#00306Fああ、アレな。\x01",
            "ときどき妙な化学反応みたいなのが\x01",
            "起きることがあるんだよなあ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_351D")


    #C0118
    ChrTalk(
        0x8,
        (
            "おおっ、なんとか用意できる\x01",
            "アテがあるみたいだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0x8,
        "それなら、是非君たちにお願いしよう。\x02",
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0x8,
        (
            "いつでもいいから、\x01",
            "そんな料理を手に入れたら\x01",
            "私の所へ持ってきてくれたまえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0x101,
        "#00000Fええ、分かりました。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x20F, 0)
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0122
    ChrTalk(
        0x8,
        (
            "そうだな。\x01",
            "代わりといってはなんだが……\x01",
            "君たちにこの本をあげようじゃないか。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0123
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x2EE),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x2EE, 1)
    SetMessageWindowPos(14, 280, 60, 3)

    #C0124
    ChrTalk(
        0x8,
        (
            "時間のあるときは読書でもして、\x01",
            "日頃の疲れを癒すといい。\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0x101,
        "#00002Fはは、ありがとうございます。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x188, 0)

    label("loc_370F")

    Return()

    # Function_8_305A end

    def Function_9_3710(): pass

    label("Function_9_3710")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_377F")

    #C0126
    ChrTalk(
        0xFE,
        (
            "随分前から、授業も訓練も\x01",
            "やれてないんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0xFE,
        (
            "こんなので警察官になんて\x01",
            "なれるのかな……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3BA4")

    label("loc_377F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3807")

    #C0128
    ChrTalk(
        0x9,
        (
            "襲撃事件のとき、警察本部に\x01",
            "爆弾が投げ込まれたらしい……\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0x9,
        (
            "ぶるぶる……恐ろしいよ、オレ。\x01",
            "やっぱり警察になんて……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3BA4")

    label("loc_3807")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3815")
    Jump("loc_3BA4")

    label("loc_3815")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x163, 2)), scpexpr(EXPR_END)), "loc_3823")
    Jump("loc_3BA4")

    label("loc_3823")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3886")

    #C0130
    ChrTalk(
        0x9,
        "わー、遅刻だ～！\x02",
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0x9,
        (
            "今日は朝から訓練だってのに……\x01",
            "教官に怒鳴られちゃうよ～。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3BA4")

    label("loc_3886")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3894")
    Jump("loc_3BA4")

    label("loc_3894")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_38A2")
    Jump("loc_3BA4")

    label("loc_38A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_38B0")
    Jump("loc_3BA4")

    label("loc_38B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3B8D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B13")

    #C0132
    ChrTalk(
        0x9,
        (
            "あれ、もしかしてあなた方は……\x01",
            "特務支援課の方々では！？\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0x9,
        (
            "自分、クロスベルタイムズで\x01",
            "あの教団事件の記事を見てから、\x01",
            "ずっと憧れてたんです！\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0x9,
        (
            "将来は自分も特務支援課に\x01",
            "配属されれば、と！\x02",
        )
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0x102,
        "#00100Fふふ、それはありがたい話ね。\x02",
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0x105,
        (
            "#10306Fやれやれ、わざわざこんな\x01",
            "大変そうな部署に入りたいなんて、\x01",
            "なかなか物好きだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0x101,
        (
            "#00006Fあのな……\x01",
            "その部署にわざわざ自分から\x01",
            "入ってきたのは誰だよ？\x02\x03",

            "#00000Fコホン、えっと。\x01",
            "配属は適正を見られて決まるから\x01",
            "自分では選べないけど……\x02\x03",

            "#00002Fもし将来、特務支援課に配属されたら\x01",
            "そのときはよろしくな。\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0x9,
        "はい！！　自分、がんばります！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3B88")

    label("loc_3B13")


    #C0139
    ChrTalk(
        0x9,
        (
            "皆さんに会えて、\x01",
            "俄然やる気がでてきました！\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0x9,
        (
            "特務支援課に入れるかは\x01",
            "分かりませんが……\x01",
            "自分、がんばります！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3B88")

    Jump("loc_3BA4")

    label("loc_3B8D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 6)), scpexpr(EXPR_END)), "loc_3B9B")
    Jump("loc_3BA4")

    label("loc_3B9B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_3BA4")

    label("loc_3BA4")

    TalkEnd(0xFE)
    Return()

    # Function_9_3710 end

    def Function_10_3BA8(): pass

    label("Function_10_3BA8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3C33")

    #C0141
    ChrTalk(
        0xFE,
        (
            "そういえば、しばらく家にも\x01",
            "帰れてなかったのよね……\x02",
        )
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0xFE,
        (
            "結界は消えたみたいだし、\x01",
            "一度実家に戻ったほうがいいかな……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E8B")

    label("loc_3C33")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3CAF")

    #C0143
    ChrTalk(
        0xA,
        (
            "せっかくカリキュラムを\x01",
            "がんばってきたんじゃない。\x02",
        )
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0xA,
        (
            "早く先輩たちの力になれるよう\x01",
            "がんばりましょうよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E8B")

    label("loc_3CAF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3CBD")
    Jump("loc_3E8B")

    label("loc_3CBD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x163, 2)), scpexpr(EXPR_END)), "loc_3D09")

    #C0145
    ChrTalk(
        0xA,
        (
            "列車事故が\x01",
            "起こったって聞いたけど……\x01",
            "一体どうなったの？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E8B")

    label("loc_3D09")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_3D17")
    Jump("loc_3E8B")

    label("loc_3D17")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3DAB")

    #C0146
    ChrTalk(
        0xA,
        (
            "今回の独立提唱、私たち訓練生も\x01",
            "大きな意味を感じています。\x02",
        )
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0xA,
        (
            "警察組織の今後の発展のためにも、\x01",
            "どうか実現に至ってほしいですね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E8B")

    label("loc_3DAB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3DB9")
    Jump("loc_3E8B")

    label("loc_3DB9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3E66")

    #C0148
    ChrTalk(
        0xA,
        (
            "今日はこのミーティングルームで\x01",
            "自治州法の講義が行われるんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0xA,
        (
            "警察官にとって法律は\x01",
            "切っても切れない存在ですから。\x01",
            "しっかり学ばないといけませんね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E8B")

    label("loc_3E66")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3E74")
    Jump("loc_3E8B")

    label("loc_3E74")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 6)), scpexpr(EXPR_END)), "loc_3E82")
    Jump("loc_3E8B")

    label("loc_3E82")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_3E8B")

    label("loc_3E8B")

    TalkEnd(0xFE)
    Return()

    # Function_10_3BA8 end

    def Function_11_3E8F(): pass

    label("Function_11_3E8F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3EA0")
    Jump("loc_42E9")

    label("loc_3EA0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_4011")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F66")

    #C0150
    ChrTalk(
        0xB,
        (
            "訓練生たちも昨日の列車事故に\x01",
            "どよめいているようだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0xB,
        (
            "だが、今の彼らが騒いだとて\x01",
            "どうしようもないことだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0xB,
        (
            "一度活を入れて、カリキュラムに\x01",
            "集中させなければな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_400C")

    label("loc_3F66")


    #C0153
    ChrTalk(
        0xB,
        (
            "昨日の列車事故は、\x01",
            "ここにいる訓練生たちが騒いだとて\x01",
            "どうしようもないことだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0xB,
        (
            "今は授業に集中させて、\x01",
            "将来いくらでも起こる事件に向けて\x01",
            "成長してもらわねばな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_400C")

    Jump("loc_42E9")

    label("loc_4011")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x163, 2)), scpexpr(EXPR_END)), "loc_401F")
    Jump("loc_42E9")

    label("loc_401F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_402D")
    Jump("loc_42E9")

    label("loc_402D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_403B")
    Jump("loc_42E9")

    label("loc_403B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_4223")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_415E")

    #C0155
    ChrTalk(
        0xB,
        (
            "近頃の訓練生たちは、\x01",
            "カリキュラムに臨む姿勢が\x01",
            "以前より前向きになっている。\x02",
        )
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0xB,
        (
            "教団事件という大きな事件を\x01",
            "警察が主となって解決したことが、\x01",
            "いい影響を与えたのだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0xB,
        (
            "まだ見ぬ後輩たちのためにも、\x01",
            "是非とも現役の警官には\x01",
            "その活躍を見せ続けてほしいものだ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_421E")

    label("loc_415E")


    #C0158
    ChrTalk(
        0xB,
        (
            "教団事件という大きな事件を\x01",
            "警察が主となって解決したことが、\x01",
            "訓練生たちにいい影響を与えている。\x02",
        )
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0xB,
        (
            "まだ見ぬ後輩たちのためにも、\x01",
            "是非とも現役の警官には\x01",
            "その活躍を見せ続けてほしいものだ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_421E")

    Jump("loc_42E9")

    label("loc_4223")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_4231")
    Jump("loc_42E9")

    label("loc_4231")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_423F")
    Jump("loc_42E9")

    label("loc_423F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 6)), scpexpr(EXPR_END)), "loc_42E0")

    #C0160
    ChrTalk(
        0xB,
        (
            "今日も警備隊たちが\x01",
            "サバイバル訓練に励んでおる。\x02",
        )
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0xB,
        (
            "さっき見てきたが、あの様子だと\x01",
            "調子もかなりもどってきたようだ。\x01",
            "いや、本当によかったな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_42E9")

    label("loc_42E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_42E9")

    label("loc_42E9")

    TalkEnd(0xFE)
    Return()

    # Function_11_3E8F end

    def Function_12_42ED(): pass

    label("Function_12_42ED")

    Call(0, 13)
    Return()

    # Function_12_42ED end

    def Function_13_42F1(): pass

    label("Function_13_42F1")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18F, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_471F")

    #C0162
    ChrTalk(
        0xC,
        "皆さん、お疲れ様です。\x02",
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0xC,
        (
            "本日はわざわざ\x01",
            "こちらに出向いてくださって\x01",
            "ありがとうございます。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18F, 4)), scpexpr(EXPR_END)), "loc_43C1")

    #C0164
    ChrTalk(
        0x101,
        (
            "#00000Fああいえ……\x02\x03",

            "#00003Fなんでも、しばらく\x01",
            "こちらで業務を行うそうですね？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4414")

    label("loc_43C1")


    #C0165
    ChrTalk(
        0x101,
        (
            "#00000Fああいえ……\x02\x03",

            "#00003Fレベッカさんは、\x01",
            "警察学校の方に来ていたんですね？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4414")


    #C0166
    ChrTalk(
        0xC,
        (
            "はい、警察本部の受付は\x01",
            "まだとても業務を再開できる\x01",
            "状態ではありませんからね。\x02",
        )
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0xC,
        (
            "ですが幸い、\x01",
            "こちらの端末にデータの\x01",
            "バックアップがありましたので。\x02",
        )
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0xC,
        (
            "それを利用する形で\x01",
            "業務を再開させて頂きました。\x02",
        )
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0xC,
        (
            "皆さんも、受付に用事がある際は\x01",
            "いつでも仰ってくださいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0x102,
        "#00100Fなるほど、分かりました。\x02",
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0x109,
        (
            "#10100Fあの、レベッカさん。\x02\x03",

            "#10104Fフランが目を覚ました時、\x01",
            "真っ先に駆けつけてくれて\x01",
            "本当にありがとうございました。\x02\x03",

            "#10109Fあの子もすごく喜んでいました。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xC, 0x109, 500)

    #C0172
    ChrTalk(
        0xC,
        "いえ、そんな……\x02",
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0xC,
        (
            "本当なら、こちらが元気付けて\x01",
            "あげないといけない立場なのに\x01",
            "逆に元気をもらう始末で……\x02",
        )
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0xC,
        (
            "ですが、本当に\x01",
            "目を覚ましてくれて良かったです。\x02",
        )
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0x109,
        (
            "#10104Fええ、まったくです。\x02\x03",

            "#10100Fよければまた、\x01",
            "顔を出してあげてくれますか？\x02",
        )
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0xC,
        "はい、もちろんです。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x18F, 5)
    TalkEnd(0xC)
    Return()

    label("loc_471F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x334, 0x0)"), scpexpr(EXPR_END)), "loc_4ACA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12B, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4ACA")
    OP_63(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0177
    ChrTalk(
        0xC,
        (
            "あら、皆さんが\x01",
            "お持ちになっているそれは……\x02",
        )
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0xC,
        (
            "もしかして、『フラグメント』\x01",
            "ではありませんか？\x02",
        )
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0x101,
        (
            "#00005Fえっと、これのことですか？\x02\x03",

            "#00000F手に入れたはいいものの、\x01",
            "いまいち使い道が\x01",
            "分からなかったんですが……\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    #A0180
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ロイドはレベッカに\x01",
            "フラグメントを見せた。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0181
    ChrTalk(
        0xC,
        "まあ、やっぱり……！\x02",
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0xC,
        (
            "これは、鑑識課の者が探していた\x01",
            "破損した記憶結晶#8Rメモリークオーツ#のデータを\x01",
            "復旧させるためのプログラムです。\x02",
        )
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0xC,
        (
            "それさえあれば、\x01",
            "教団の端末データの一部分を\x01",
            "解析することができるはずです。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4962")
    OP_63(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)

    label("loc_4962")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_498B")
    OP_63(0x1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)

    label("loc_498B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_49B4")
    OP_63(0x2, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)

    label("loc_49B4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_49DA")
    OP_63(0x3, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    label("loc_49DA")

    Sleep(1000)

    #C0184
    ChrTalk(
        0x102,
        (
            "#00105Fそ、それじゃあ……\x01",
            "ヨアヒム・ギュンターによって\x01",
            "隠された文章が読めるように……！？\x02",
        )
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0xC,
        (
            "ええ、あくまでも一部では\x01",
            "あるそうですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0xC,
        (
            "すぐに結果が出ると思いますし、\x01",
            "『フラグメント』を鑑識に回しても\x01",
            "よろしいですか？\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 16)
    TalkEnd(0xC)
    Return()

    label("loc_4ACA")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4AD4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4C47")
    FadeToDark(300, 0, 100)
    ClearScenarioFlags(0x0, 5)
    Call(0, 15)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_4B5C")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "話をする\x01",                        # 0
            "戦闘手帳を見せる\x01",                # 1
            "教団の端末データを確認する\x01",      # 2
            "フラグメントを渡す\x01",              # 3
            "やめる\x01",                          # 4
        )
    )

    MenuEnd(0x0)
    Jump("loc_4BBD")

    label("loc_4B5C")


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "話をする\x01",                        # 0
            "戦闘手帳を見せる\x01",                # 1
            "教団の端末データを確認する\x01",      # 2
            "やめる\x01",                          # 3
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4BBD")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4BBD")

    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4BEB")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 14)
    Jump("loc_4C42")

    label("loc_4BEB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4C0F")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 7)
    Call(0, 23)
    Jump("loc_4C42")

    label("loc_4C0F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4C30")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 17)
    Jump("loc_4C42")

    label("loc_4C30")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4C42")
    Call(0, 16)

    label("loc_4C42")

    Jump("loc_4AD4")

    label("loc_4C47")

    TalkEnd(0xC)
    OP_93(0xC, 0x5A, 0x0)
    BeginChrThread(0xC, 0, 0, 0)
    Return()

    # Function_13_42F1 end

    def Function_14_4C58(): pass

    label("Function_14_4C58")


    #C0187
    ChrTalk(
        0xC,
        (
            "何はともあれ……\x01",
            "フランが目を覚ましてくれて\x01",
            "本当に良かったです。\x02",
        )
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0xC,
        (
            "彼女を元気付けてあげるためにも、\x01",
            "私たちも頑張らないといけませんね。\x02",
        )
    )

    CloseMessageWindow()
    Return()

    # Function_14_4C58 end

    def Function_15_4CE8(): pass

    label("Function_15_4CE8")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x334, 0x0)"), scpexpr(EXPR_END)), "loc_4CF6")
    SetScenarioFlags(0x0, 5)

    label("loc_4CF6")

    Return()

    # Function_15_4CE8 end

    def Function_16_4CF7(): pass

    label("Function_16_4CF7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12B, 1)), scpexpr(EXPR_END)), "loc_4D95")

    #C0189
    ChrTalk(
        0xC,
        (
            "あら、『フラグメント』を\x01",
            "持ってきてくださったんですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0xC,
        (
            "教団の端末データを解析するため、\x01",
            "『フラグメント』を鑑識に回しても\x01",
            "よろしいですか？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4D95")


    #C0191
    ChrTalk(
        0x101,
        "#00000Fええ、よろしくお願いします。\x02",
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0xC,
        "それでは、少々お待ち下さい。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x12B, 1)
    FadeToDark(1000, 0, -1)
    OP_0D()

    label("loc_4DEE")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x334, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6BA0")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x334, 0x0)"), scpexpr(EXPR_END)), "loc_6B9B")
    OP_D2(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SubItemNumber(0x334, 1)
    SetChrName("")
    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4E76")
    Sound(9, 0, 100, 0)

    #A0193
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "第０１情報端末データ\x01",
            "『教団について』のページ１を解析した！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_4E76")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4ED2")
    Sound(9, 0, 100, 0)

    #A0194
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "第０１情報端末データ\x01",
            "『教団について』のページ３を解析した！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_4ED2")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4F34")
    Sound(9, 0, 100, 0)

    #A0195
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "第０２情報端末データ\x01",
            "『グノーシスについて』のページ１を解析した！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_4F34")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4F96")
    Sound(9, 0, 100, 0)

    #A0196
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "第０２情報端末データ\x01",
            "『グノーシスについて』のページ２を解析した！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_4F96")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5853")
    Sound(9, 0, 100, 0)

    #A0197
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "第０１情報端末データ\x01",
            "『教団について』のページ４を解析した！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(9, 0, 100, 0)

    #A0198
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "第０１情報端末データ\x01",
            "『教団について』の解析を完了した！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    EventBegin(0x0)
    OP_68(2310, 1440, 13000, 0)
    MoveCamera(39, 17, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(21380, 0)
    Call(0, 22)
    FadeToBright(1000, 0)
    OP_0D()

    #C0199
    ChrTalk(
        0xC,
        (
            "#5P第０１情報端末の全データの\x01",
            "解析が完了しました。\x02",
        )
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0xC,
        "#5Pさっそく確認してみますか？\x02",
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0x101,
        "#12P#00001Fええ、お願いします。\x02",
    )

    CloseMessageWindow()
    Sound(72, 0, 100, 0)
    Call(0, 18)

    #C0202
    ChrTalk(
        0xC,
        (
            "#5P……このデータには、\x01",
            "教団についての概要が\x01",
            "記載されていたようですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0203
    ChrTalk(
        0xC,
        (
            "#5P女神の否定という教義……\x01",
            "本当に信じられません。\x02",
        )
    )

    CloseMessageWindow()

    #C0204
    ChrTalk(
        0x101,
        (
            "#12P#00003Fええ……ですが\x01",
            "ヨアヒム・ギュンターの\x01",
            "証言とも一致します。\x02\x03",

            "#00001Fそして、この《Ｄ》という言葉……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_538A")

    #C0205
    ChrTalk(
        0x103,
        (
            "#12P#00203F彼らが女神の代わりに信奉した\x01",
            "《真なる神》を指す言葉なんでしょう。\x02\x03",

            "#00201FＤ∴Ｇ教団の名前にある『Ｇ』が\x01",
            "《真なる叡智#10Rグ ノ ー シ ス#》を指すということは\x01",
            "既に突き止められていますし……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_5335")

    #C0206
    ChrTalk(
        0x105,
        (
            "#12P#10403Fふむ、これで『Ｄ∴Ｇ』の意味も\x01",
            "ようやく判明したと言えそうだね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5385")

    label("loc_5335")


    #C0207
    ChrTalk(
        0x105,
        (
            "#12P#10303Fふむ、これで『Ｄ∴Ｇ』の意味も\x01",
            "ようやく判明したと言えそうだね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5385")

    Jump("loc_5493")

    label("loc_538A")


    #C0208
    ChrTalk(
        0x103,
        (
            "#12P#00200F彼らが女神の代わりに信奉した\x01",
            "《真なる神》を指す言葉なんでしょう。\x02\x03",

            "#00201FＤ∴Ｇ教団の名前にある『Ｇ』が\x01",
            "《真なる叡智#10Rグ ノ ー シ ス#》を指すということは\x01",
            "既に突き止められていますし……\x02\x03",

            "これで『Ｄ∴Ｇ』の意味も\x01",
            "ようやく判明したと言えるはずです。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5493")


    #C0209
    ChrTalk(
        0x102,
        (
            "#12P#00108Fでも……確かヨアヒム先生は、\x01",
            "キーアちゃんの事を\x01",
            "『神となる御方』と言ってたのよね。\x02\x03",

            "そうなると、《Ｄ》とは\x01",
            "キーアちゃんを指す言葉にも\x01",
            "なってしまうけど……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_55BB")

    #C0210
    ChrTalk(
        0x109,
        (
            "#12P#10101Fヨアヒム・ギュンターが\x01",
            "どこまでの事を知ってたのか……\x02\x03",

            "……これだけじゃまだ判りませんね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_56A1")

    label("loc_55BB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5643")

    #C0211
    ChrTalk(
        0x104,
        (
            "#12P#00301Fヨアヒムの野郎が\x01",
            "どこまでの事を知ってたのか……\x02",
        )
    )

    CloseMessageWindow()

    #C0212
    ChrTalk(
        0x109,
        "#12P#10101F……これだけじゃまだ判りませんね。\x02",
    )

    CloseMessageWindow()
    Jump("loc_56A1")

    label("loc_5643")


    #C0213
    ChrTalk(
        0x104,
        (
            "#12P#00301Fヨアヒムの野郎が\x01",
            "どこまでの事を知ってたのか……\x02\x03",

            "これだけじゃまだ判らねえな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_56A1")


    #C0214
    ChrTalk(
        0x101,
        (
            "#12P#00001Fアーネストさんも、ヨアヒムから\x01",
            "すべてを聞いていたわけじゃ\x01",
            "ないみたいだし……\x02\x03",

            "#00003F彼を逮捕できていれば……\x01",
            "つくづくそう思ってしまうな。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x334, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_57AD")

    #C0215
    ChrTalk(
        0xC,
        (
            "#5P……ともかく、この調子で\x01",
            "データを解析していけば、\x01",
            "色々な事が見えてくると思います。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5853")

    label("loc_57AD")


    #C0216
    ChrTalk(
        0xC,
        (
            "#5P……ともかく、この調子で\x01",
            "データを解析していけば、\x01",
            "色々な事が見えてくると思います。\x02",
        )
    )

    CloseMessageWindow()

    #C0217
    ChrTalk(
        0xC,
        (
            "#5P残りの『フラグメント』も\x01",
            "解析に回してみるとしましょう。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()

    label("loc_5853")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_58B5")
    Sound(9, 0, 100, 0)

    #A0218
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "第０２情報端末データ\x01",
            "『グノーシスについて』のページ３を解析した！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_58B5")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5911")
    Sound(9, 0, 100, 0)

    #A0219
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "第０３情報端末データ\x01",
            "『御子について』のページ１を解析した！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_5911")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6230")
    Sound(9, 0, 100, 0)

    #A0220
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "第０２情報端末データ\x01",
            "『グノーシスについて』のページ４を解析した！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(9, 0, 100, 0)

    #A0221
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "第０２情報端末データ\x01",
            "『グノーシスについて』の解析を完了した！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    EventBegin(0x0)
    OP_68(2310, 1440, 13000, 0)
    MoveCamera(39, 17, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(21380, 0)
    Call(0, 22)
    FadeToBright(1000, 0)
    OP_0D()

    #C0222
    ChrTalk(
        0xC,
        (
            "#5P第０２情報端末の全データの\x01",
            "解析が完了しました。\x02",
        )
    )

    CloseMessageWindow()

    #C0223
    ChrTalk(
        0xC,
        "#5Pさっそく確認してみますか？\x02",
    )

    CloseMessageWindow()

    #C0224
    ChrTalk(
        0x101,
        "#12P#00001Fええ、お願いします。\x02",
    )

    CloseMessageWindow()
    Sound(72, 0, 100, 0)
    Call(0, 19)

    #C0225
    ChrTalk(
        0xC,
        (
            "#5P……このデータには、\x01",
            "あの《グノーシス》に関する\x01",
            "詳細が記されているみたいですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0xC,
        (
            "#5P身体能力と感応力を高め、\x01",
            "さらには潜在能力すら\x01",
            "引き出す効能を持つ薬物……\x02",
        )
    )

    CloseMessageWindow()

    #C0227
    ChrTalk(
        0xC,
        (
            "#5P“魔人化”といった現象といい、\x01",
            "かなり謎の多い薬物ですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0228
    ChrTalk(
        0x101,
        (
            "#12P#00001F原料として使われた\x01",
            "《プレロマ草》という植物が\x01",
            "湿地帯に群生していた事から……\x02\x03",

            "ヨアヒムが湿地帯に材料を\x01",
            "採取しに行っていたらしい事も\x01",
            "状況的に間違いなさそうです。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5D00")

    #C0229
    ChrTalk(
        0x102,
        (
            "#12P#00101Fそれと、データにはグノーシスが\x01",
            "彼らの言う所の真なる神……\x02\x03",

            "つまり、《Ｄ》を復活させる為の\x01",
            "薬物だという一節もあるわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0230
    ChrTalk(
        0x109,
        (
            "#12P#10108F正直言って、荒唐無稽な話に\x01",
            "聞こえますけど……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5DBB")

    label("loc_5D00")


    #C0231
    ChrTalk(
        0x102,
        (
            "#12P#00101Fそれと、データにはグノーシスが\x01",
            "彼らの言う所の真なる神……\x02\x03",

            "つまり、《Ｄ》を復活させる為の\x01",
            "薬物だという一節もあるわね。\x02\x03",

            "#00108F正直言って、荒唐無稽な話に\x01",
            "聞こえるけど……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5DBB")


    #C0232
    ChrTalk(
        0x103,
        (
            "#12P#00201Fそれでも、教団は５００年もの間\x01",
            "“儀式”という形で\x01",
            "グノーシスの研究を続けてきた……\x02\x03",

            "#00203F……わたしは運良くガイさんに\x01",
            "助け出されましたが、今までに\x01",
            "相当な数の犠牲者も出たそうです。\x02",
        )
    )

    CloseMessageWindow()

    #C0233
    ChrTalk(
        0x104,
        (
            "#12P#00301Fそれを“多少の犠牲”だなんて\x01",
            "言い方をしてるんだからな……\x02\x03",

            "本当に救いようのねえ連中だぜ。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6002")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_5F59")

    #C0234
    ChrTalk(
        0x105,
        (
            "#12P#10403F……それと、最近はヴァルドも\x01",
            "グノーシスを服用していたんだよね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5FA9")

    label("loc_5F59")


    #C0235
    ChrTalk(
        0x105,
        (
            "#12P#10303F……それと、最近はヴァルドも\x01",
            "グノーシスを服用していたんだよね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5FA9")


    #C0236
    ChrTalk(
        0x101,
        (
            "#12P#00001Fああ……教団がなくなったとはいえ、\x01",
            "まだ注意は必要なのかもしれない。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_608E")

    label("loc_6002")


    #C0237
    ChrTalk(
        0x101,
        (
            "#12P#00003F……それと、最近はヴァルドも\x01",
            "グノーシスを服用していた。\x02\x03",

            "#00001F教団がなくなったとはいえ、\x01",
            "まだ注意は必要なのかもしれない。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_608E")


    #C0238
    ChrTalk(
        0x102,
        (
            "#12P#00101Fええ……本当にそうね。\x02\x03",

            "グノーシスに限らず、\x01",
            "こんな薬物は、私たち警察が\x01",
            "きちんと取り締まらなくちゃね。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x334, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_6180")

    #C0239
    ChrTalk(
        0xC,
        "#5Pええ、本当にそう思います。\x02",
    )

    CloseMessageWindow()

    #C0240
    ChrTalk(
        0xC,
        (
            "#5P……ひとまずグノーシスに関しては\x01",
            "こんなところでしょうか。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6230")

    label("loc_6180")


    #C0241
    ChrTalk(
        0xC,
        "#5Pええ、本当にそう思います。\x02",
    )

    CloseMessageWindow()

    #C0242
    ChrTalk(
        0xC,
        (
            "#5P……ひとまずグノーシスに関しては\x01",
            "こんなところでしょうか。\x02",
        )
    )

    CloseMessageWindow()

    #C0243
    ChrTalk(
        0xC,
        (
            "#5P残りの『フラグメント』も\x01",
            "解析に回してみるとしましょう。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()

    label("loc_6230")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_628C")
    Sound(9, 0, 100, 0)

    #A0244
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "第０３情報端末データ\x01",
            "『御子について』のページ２を解析した！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_628C")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6B9B")
    Sound(9, 0, 100, 0)

    #A0245
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "第０３情報端末データ\x01",
            "『御子について』のページ３を解析した！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(9, 0, 100, 0)

    #A0246
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "第０３情報端末データ\x01",
            "『御子について』の解析を完了した！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    EventBegin(0x0)
    OP_68(2310, 1440, 13000, 0)
    MoveCamera(39, 17, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(21380, 0)
    Call(0, 22)
    SetScenarioFlags(0x12A, 6)
    FadeToBright(1000, 0)
    OP_0D()

    #C0247
    ChrTalk(
        0xC,
        (
            "#5P第０３情報端末の全データの\x01",
            "解析が完了しました。\x02",
        )
    )

    CloseMessageWindow()

    #C0248
    ChrTalk(
        0xC,
        "#5Pさっそく確認してみますか？\x02",
    )

    CloseMessageWindow()

    #C0249
    ChrTalk(
        0x101,
        "#12P#00001Fええ、お願いします。\x02",
    )

    CloseMessageWindow()
    Sound(72, 0, 100, 0)
    Call(0, 20)

    #C0250
    ChrTalk(
        0xC,
        (
            "#5Pこの内容は、\x01",
            "支援課で保護されていた\x01",
            "キーアさんの……？\x02",
        )
    )

    CloseMessageWindow()

    #C0251
    ChrTalk(
        0x101,
        (
            "#12P#00003F５００年前、クロイス家によって\x01",
            "キーアが生み出され……\x01",
            "信仰対象として教団に与えられた。\x02\x03",

            "《揺籃#4Rゆりかご#》に眠り続ける、\x01",
            "神の依り代たる『御子』として……\x02",
        )
    )

    CloseMessageWindow()

    #C0252
    ChrTalk(
        0x102,
        (
            "#12P#00101F……教団の人間も、何一つ真実を\x01",
            "知らされていなかったんでしょうね。\x02",
        )
    )

    CloseMessageWindow()

    #C0253
    ChrTalk(
        0x103,
        (
            "#12P#00203Fクロイス家の真の目的のために\x01",
            "影で誘導されているとも知らずに、\x01",
            "《真なる神》という幻想を求め続けた……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_65F5")

    #C0254
    ChrTalk(
        0x106,
        "#12P#10708F……ある意味、哀れな人たちですね。\x02",
    )

    CloseMessageWindow()
    Jump("loc_666C")

    label("loc_65F5")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_663D")

    #C0255
    ChrTalk(
        0x109,
        "#12P#10108F……ある意味、哀れな人たちですね。\x02",
    )

    CloseMessageWindow()
    Jump("loc_666C")

    label("loc_663D")


    #C0256
    ChrTalk(
        0x105,
        "#12P#10408F……ある意味、哀れな連中だね。\x02",
    )

    CloseMessageWindow()

    label("loc_666C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_66C3")

    #C0257
    ChrTalk(
        0x10A,
        (
            "#12P#00603F奴らのやってきた事を考えると\x01",
            "同情すら沸かんがな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_676C")

    label("loc_66C3")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6720")

    #C0258
    ChrTalk(
        0x105,
        (
            "#12P#10403F彼らのやってきた事を考えると\x01",
            "同情する余地はないけどね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_676C")

    label("loc_6720")


    #C0259
    ChrTalk(
        0x109,
        (
            "#12P#10103F彼らのやってきた事を考えると\x01",
            "同情する余地はありませんが……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_676C")


    #C0260
    ChrTalk(
        0x101,
        (
            "#12P#00001F教団はともかく……\x01",
            "キーアには何の罪もなかったはずだ。\x02\x03",

            "#00003F例えクロイス家の目的のために\x01",
            "造られた存在だったとしても……\x02\x03",

            "例え不可思議な能力を\x01",
            "持っていたとしても……\x01",
            "そんなことは関係がない。\x02\x03",

            "俺たちの目の前で目覚めたあの子は\x01",
            "正真正銘、普通の女の子だったはずだ。\x02\x03",

            "#00001Fそれなのに、何百年もあんな所に\x01",
            "一人ぼっちで閉じ込められて……\x02\x03",

            "今また、マリアベルさんと\x01",
            "イアン先生によって\x01",
            "利用されようとしている。\x02",
        )
    )

    CloseMessageWindow()

    #C0261
    ChrTalk(
        0x104,
        (
            "#12P#00301F……どんな事情があろうと、\x01",
            "絶対に許すわけにはいかねえな。\x02",
        )
    )

    CloseMessageWindow()

    #C0262
    ChrTalk(
        0xC,
        (
            "#5P……ひとまず、教団のデータは\x01",
            "これで全て解析が完了しました。\x02",
        )
    )

    CloseMessageWindow()

    #C0263
    ChrTalk(
        0xC,
        (
            "#5P私は皆さんほど今回の事件の\x01",
            "細かい事情に通じてはいませんが……\x02",
        )
    )

    CloseMessageWindow()

    #C0264
    ChrTalk(
        0xC,
        (
            "#5P皆さんにとってキーアさんが\x01",
            "とても大切な存在だという事は\x01",
            "痛いほど分かります。\x02",
        )
    )

    CloseMessageWindow()

    #C0265
    ChrTalk(
        0xC,
        (
            "#5Pどうか……頑張ってください。\x01",
            "私も陰ながら応援させていただきます。\x02",
        )
    )

    CloseMessageWindow()

    #C0266
    ChrTalk(
        0x101,
        (
            "#12P#00001Fありがとうございます、レベッカさん。\x02\x03",

            "俺たちの手で絶対に、\x01",
            "キーアを取り戻してみせます。\x02\x03",

            "#00007F俺たちの大切なキーアが……\x01",
            "あの子自身が笑顔で過ごせる\x01",
            "未来を作るためにも……！\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, 2840, 0, 12040, 180)
    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_6B76")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)

    label("loc_6B76")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_6B8F")
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)

    label("loc_6B8F")

    OP_69(0xFF, 0x0)
    OP_E0(0x9, 0x0)
    OP_E0(0x80, 0x0)
    EventEnd(0x5)

    label("loc_6B9B")

    Jump("loc_4DEE")

    label("loc_6BA0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6CB7")
    FadeToBright(1000, 0)
    OP_0D()

    #C0267
    ChrTalk(
        0xC,
        (
            "また『フラグメント』を手に入れたら\x01",
            "私の方にお持ちくださいませ。\x02",
        )
    )

    CloseMessageWindow()

    #C0268
    ChrTalk(
        0xC,
        (
            "解析されたデータを確認する場合も\x01",
            "改めてお申し付けください。\x02",
        )
    )

    CloseMessageWindow()

    #C0269
    ChrTalk(
        0x101,
        "#00000Fええ、ありがとうございます。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, 2840, 0, 12040, 180)
    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_6C98")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)

    label("loc_6C98")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_6CB1")
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)

    label("loc_6CB1")

    OP_69(0xFF, 0x0)
    EventEnd(0x5)

    label("loc_6CB7")

    Return()

    # Function_16_4CF7 end

    def Function_17_6CB8(): pass

    label("Function_17_6CB8")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6CC2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6DC2")
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(173, 40, -1, -1)
    SetChrName("")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "【教団について】\x01",            # 0
            "【グノーシスについて】\x01",      # 1
            "【御子について】\x01",            # 2
            "【何もしない】\x01",              # 3
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    SetMessageWindowPos(14, 280, 60, 3)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_6D75"),
        (1, "loc_6D83"),
        (2, "loc_6D91"),
        (3, "loc_6D9F"),
        (SWITCH_DEFAULT, "loc_6DAE"),
    )


    label("loc_6D75")

    Sound(72, 0, 100, 0)
    Call(0, 18)
    Jump("loc_6DBD")

    label("loc_6D83")

    Sound(72, 0, 100, 0)
    Call(0, 19)
    Jump("loc_6DBD")

    label("loc_6D91")

    Sound(72, 0, 100, 0)
    Call(0, 20)
    Jump("loc_6DBD")

    label("loc_6D9F")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6DBD")

    label("loc_6DAE")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6DBD")

    label("loc_6DBD")

    Jump("loc_6CC2")

    label("loc_6DC2")

    Return()

    # Function_17_6CB8 end

    def Function_18_6DC3(): pass

    label("Function_18_6DC3")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, 34, -1)
    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6F8A")
    SetChrName("")

    #A0270
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2S『教団について』\x01\x01",
            "──私の名はヨアヒム・ギュンター。\x01",
            "《Ｄ∴Ｇ教団》に属する幹部司祭である。\x01",
            "６年前、遊撃士を含む多くの勢力の手で\x01",
            "我が教団は壊滅状態に陥ってしまった。\x01",
            "しかし、私だけは故あって難を逃れ、\x01",
            "この■■の地へと落ち延びる事ができた。\x01",
            "大いなる《■》の導きによって\x01",
            "教団の大望を成すべく私は永らえたのだ。\x01",
            "いずれ来るその時──\x01",
            "新たな聖典を記すための資料として\x01",
            "各端末にデータを記録しておく事とする。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_712B")

    label("loc_6F8A")

    SetChrName("")

    #A0271
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2S『教団について』\x01\x01",
            "──私の名はヨアヒム・ギュンター。\x01",
            "《Ｄ∴Ｇ教団》に属する幹部司祭である。\x01",
            "６年前、遊撃士を含む多くの勢力の手で\x01",
            "我が教団は壊滅状態に陥ってしまった。\x01",
            "しかし、私だけは故あって難を逃れ、\x01",
            "この起源の地へと落ち延びる事ができた。\x01",
            "大いなる《Ｄ》の導きによって\x01",
            "教団の大望を成すべく私は永らえたのだ。\x01",
            "いずれ来るその時──\x01",
            "新たな聖典を記すための資料として\x01",
            "各端末にデータを記録しておく事とする。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_712B")

    SetChrName("")

    #A0272
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2Sまず、我が教団の成り立ちについて語ろう。\x01",
            "そのためには、このゼムリア大陸が辿った\x01",
            "忌々しい歴史を振り返る必要がある。\x01\x01",
            "──約１２００年前の《大崩壊》によって\x01",
            "大陸は高度な文明と秩序を失い、\x01",
            "戦と貧困の支配する《暗黒時代》が訪れた。\x01",
            "そして、疲れ果てた人々は\x01",
            "大いなる間違いを犯してしまった。\x01\x01",
            "突如現れた愚か者どもの甘言に惑わされ、\x01",
            "彼らの作りだした身勝手な秩序を\x01",
            "受け入れてしまったのだ。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_7472")
    SetChrName("")

    #A0273
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2Sすなわち──愚かなる■■■■と\x01",
            "信仰の象徴たる《■の■■》である。\x01",
            "彼らの秩序によって《暗黒時代》は終焉し、\x01",
            "その信仰はたちまち大陸中に広まったが……\x01\x01",
            "よく考えてみてほしい。\x01",
            "もし真に《■■》が存在するというのならば\x01",
            "誰もが等しく救いを受けるべきではないか？\x01",
            "しかし、未だに格差の概念は無くならず、\x01",
            "災厄や不幸で命を落とす者も後を絶たない。\x01\x01",
            "《■■》は救う人間を選ぶというのか？\x01",
            "あまりに馬鹿馬鹿しい話ではないか。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_7619")

    label("loc_7472")

    SetChrName("")

    #A0274
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2Sすなわち──愚かなる七耀教会と\x01",
            "信仰の象徴たる《空の女神》である。\x01",
            "彼らの秩序によって《暗黒時代》は終焉し、\x01",
            "その信仰はたちまち大陸中に広まったが……\x01\x01",
            "よく考えてみてほしい。\x01",
            "もし真に《女神》が存在するというのならば\x01",
            "誰もが等しく救いを受けるべきではないか？\x01",
            "しかし、未だに格差の概念は無くならず、\x01",
            "災厄や不幸で命を落とす者も後を絶たない。\x01\x01",
            "《女神》は救う人間を選ぶというのか？\x01",
            "あまりに馬鹿馬鹿しい話ではないか。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_7619")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_779F")
    SetChrName("")

    #A0275
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2S所詮は■■■■が権威を得るため\x01",
            "作りだした虚像に過ぎないのである。\x01",
            "《■■》など、存在するわけがないのだ。\x01\x01",
            "真理に辿りついた我々の先人たちは、\x01",
            "《■■■■》に邂逅すべく長き旅路に出た。\x01\x01",
            "そして時代が中世に移り変わる頃、\x01",
            "ついに彼らは見出したのである。\x01",
            "この地の奥深くで■■■■■■■■■■\x01",
            "■■■■■■■■■■■■■■■……\x01\x01",
            "《■》──それはそう呼ばれていた。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_7912")

    label("loc_779F")

    SetChrName("")

    #A0276
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2S所詮は七耀教会が権威を得るため\x01",
            "作りだした虚像に過ぎないのである。\x01",
            "《女神》など、存在するわけがないのだ。\x01\x01",
            "真理に辿りついた我々の先人たちは、\x01",
            "《真なる神》に邂逅すべく長き旅路に出た。\x01\x01",
            "そして時代が中世に移り変わる頃、\x01",
            "ついに彼らは見出したのである。\x01",
            "この地の奥深くで永い眠りにつきながら\x01",
            "大いなる力をその身に宿した存在……\x01\x01",
            "《Ｄ》──それはそう呼ばれていた。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_7912")

    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Return()

    # Function_18_6DC3 end

    def Function_19_7926(): pass

    label("Function_19_7926")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, 34, -1)
    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_7ADB")
    SetChrName("")

    #A0277
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2S『グノーシスについて』\x01\x01",
            "《グノーシス》……それは、\x01",
            "■■■■■■■■という■■■■■、\x01",
            "《プレロマ草》を原料とした秘薬である。\x01\x01",
            "その調合方法は■■■■■■■■■、\x01",
            "服用することで身体能力と感応力を高め、\x01",
            "さらには潜在能力すら引き出す効能を持つ。\x01",
            "■■■■■■■■■■■■■■■■■。\x01",
            "■■■■■■■■■■■■■■■。\x01",
            "《グノーシス》は、■■■の■■を\x01",
            "《■》の■■に■■■■■■■薬なのだ。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_7C6A")

    label("loc_7ADB")

    SetChrName("")

    #A0278
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2S『グノーシスについて』\x01\x01",
            "《グノーシス》……それは、\x01",
            "七耀脈の上に咲くという伝説の植物、\x01",
            "《プレロマ草》を原料とした秘薬である。\x01\x01",
            "その調合方法は《Ｄ》と共に伝わり、\x01",
            "服用することで身体能力と感応力を高め、\x01",
            "さらには潜在能力すら引き出す効能を持つ。\x01",
            "だが、それらは単なる布石にすぎない。\x01",
            "この薬の真の力は別にあったのだ。\x01",
            "《グノーシス》は、服用者の精神を\x01",
            "《Ｄ》の御心に接続するための薬なのだ。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_7C6A")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_7E08")
    SetChrName("")

    #A0279
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2S《■》は■■■の■■を■■することで\x01",
            "■■を蓄え、■■する性質を持つ。\x01",
            "いずれその■■が《■■》に至ったとき、\x01",
            "《■》は■■するのである。\x01\x01",
            "さらに、《グノーシス》には\x01",
            "改良の余地が残されていた。\x01",
            "■■■■■■■■■■■■■■■■■、\x01",
            "■■■■■■■を《■》に■■■■■のだ。\x01\x01",
            "それから■■■■■■■、我が教団は\x01",
            "より効果の高い《グノーシス》の研究……\x01",
            "いわゆる“儀式”を繰り返してきた。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_7F93")

    label("loc_7E08")

    SetChrName("")

    #A0280
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2S《Ｄ》は服用者の精神を統合することで\x01",
            "知識を蓄え、成長する性質を持つ。\x01",
            "いずれその知識が《叡智》に至ったとき、\x01",
            "《Ｄ》は復活するのである。\x01\x01",
            "さらに、《グノーシス》には\x01",
            "改良の余地が残されていた。\x01",
            "服用者の能力を限界まで引き出せれば、\x01",
            "より多くの知識を《Ｄ》に供給できるのだ。\x01\x01",
            "それから５００年もの間、我が教団は\x01",
            "より効果の高い《グノーシス》の研究……\x01",
            "いわゆる“儀式”を繰り返してきた。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_7F93")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_8125")
    SetChrName("")

    #A0281
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2Sそうして、■■■■■の■■■とは\x01",
            "■■■■■■■■■■■■\x01",
            "《グノーシス》は完成へと近づいたが、\x01",
            "今一歩のところで誤算が生じてしまう。\x01\x01",
            "実験の規模を大きくしたことで\x01",
            "遊撃士やその他の勢力に存在を感づかれ、\x01",
            "各ロッジ、及び教団そのものの壊滅に\x01",
            "繋がってしまったのである。\x01\x01",
            "誠に愚かな事であると言わざるを得ない。\x01",
            "《■■■■》の■■のためには\x01",
            "多少の犠牲は付き物だというのに……\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_82A4")

    label("loc_8125")

    SetChrName("")

    #A0282
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2Sそうして、５００年前の発足時とは\x01",
            "比較できないほどの速度で\x01",
            "《グノーシス》は完成へと近づいたが、\x01",
            "今一歩のところで誤算が生じてしまう。\x01\x01",
            "実験の規模を大きくしたことで\x01",
            "遊撃士やその他の勢力に存在を感づかれ、\x01",
            "各ロッジ、及び教団そのものの壊滅に\x01",
            "繋がってしまったのである。\x01\x01",
            "誠に愚かな事であると言わざるを得ない。\x01",
            "《真なる神》の復活のためには\x01",
            "多少の犠牲は付き物だというのに……\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_82A4")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_844E")
    SetChrName("")

    #A0283
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2S私は、壊滅したロッジから\x01",
            "実験のデータを秘密裏に回収し、\x01",
            "この■■の地クロスベルへと至った。\x01\x01",
            "《グノーシス》の材料である\x01",
            "《プレロマ草》は■■■■■■■の\x01",
            "■■■に■■しているため、\x01",
            "■■■■■に困ることはなかった。\x01",
            "また、この《太陽の砦》の深層は\x01",
            "■■の■■■■の■■■研究施設であり、\x01",
            "数々の高度な設備を備えている。\x01",
            "こうして私は恵まれた研究環境を手に入れ\x01",
            "遂にこの秘薬を完成させたのである──。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_85E5")

    label("loc_844E")

    SetChrName("")

    #A0284
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2S私は、壊滅したロッジから\x01",
            "実験のデータを秘密裏に回収し、\x01",
            "この起源の地クロスベルへと至った。\x01\x01",
            "《グノーシス》の材料である\x01",
            "《プレロマ草》はクロスベル南部の\x01",
            "湿地帯に群生しているため、\x01",
            "材料の調達に困ることはなかった。\x01",
            "また、この《太陽の砦》の深層は\x01",
            "中世の錬金術師の築いた研究施設であり、\x01",
            "数々の高度な設備を備えている。\x01",
            "こうして私は恵まれた研究環境を手に入れ\x01",
            "遂にこの秘薬を完成させたのである──。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_85E5")

    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Return()

    # Function_19_7926 end

    def Function_20_85F9(): pass

    label("Function_20_85F9")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, 34, -1)
    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_87BC")
    SetChrName("")

    #A0285
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2S『御子について』\x01\x01",
            "このクロスベルは我々《Ｄ∴Ｇ教団》の\x01",
            "■■■であるとともに、■■■■とされる。\x01",
            "その■■は、《御子》たるものが\x01",
            "■■■■■■■■■■■■■だからである。\x01\x01",
            "《御子》とは、《■■■■》■■■■■■■\x01",
            "■■《Ｄ∴Ｇ教団》■■■■■■■■■■。\x01",
            "《太陽の砦》■■■■■■■■■■■■、\x01",
            "■■■■■■■■■■■■■■■■■、\x01",
            "■■■■■■■《太陽の砦》■■■■\x01",
            "■■■■■■■■■■■■■■のだ。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_8959")

    label("loc_87BC")

    SetChrName("")

    #A0286
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2S『御子について』\x01\x01",
            "このクロスベルは我々《Ｄ∴Ｇ教団》の\x01",
            "本拠地であるとともに、起源の地とされる。\x01",
            "その理由は、《御子》たるものが\x01",
            "始祖より継承されてきた場所だからである。\x01\x01",
            "《御子》とは、《真なる神》の依り代にして\x01",
            "我が《Ｄ∴Ｇ教団》の象徴たる存在である。\x01",
            "《太陽の砦》の地下で眠り続けるそれは、\x01",
            "一見すれば人間の少女の姿をしており、\x01",
            "５００年もの間《太陽の砦》の祭壇で\x01",
            "目覚めの時を待っているというのだ。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_8959")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_8AE9")
    SetChrName("")

    #A0287
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2S■■がそれほどの■■を■■■など、\x01",
            "俗世の者には信じ難い話であろう。\x01\x01",
            "だが、私は確かにこの目で見たのだ。\x01",
            "『■■■■■』と呼ばれる■■の■で\x01",
            "■■■■■■■■■■■■■■──\x01",
            "その神々しき■■を。\x01\x01",
            "『■■■■■』は、《古代遺物》を\x01",
            "■■していた■■■■■■の■■を元に\x01",
            "■■■■■■■■■■■■■■■である。\x01",
            "ならば、この■■■■■■■■■■にも\x01",
            "何ら不思議はないだろう。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_8C72")

    label("loc_8AE9")

    SetChrName("")

    #A0288
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2S人間がそれほどの時間を生きるなど、\x01",
            "俗世の者には信じ難い話であろう。\x01\x01",
            "だが、私は確かにこの目で見たのだ。\x01",
            "『聖なる揺籃#4Rゆりかご#』と呼ばれる球体の中で\x01",
            "まどろむように眠り続ける少女──\x01",
            "その神々しき御姿を。\x01\x01",
            "『聖なる揺籃』は、《古代遺物》を\x01",
            "研究していた錬金術師たちの技術を元に\x01",
            "教団の先人たちが造り上げたものである。\x01",
            "ならば、この奇蹟ともいうべき現象にも\x01",
            "何ら不思議はないだろう。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_8C72")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_8DEF")
    SetChrName("")

    #A0289
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2S《御子》は■■■■■■から\x01",
            "《グノーシス》を■■■、■■■■■■■\x01",
            "■■■■■■■■■■■■■。\x01\x01",
            "──《■■》■■■■■《御子》は■■■、\x01",
            "■■■■《■》■■■であろう。\x01",
            "そして、■■の■■の■■と■■は\x01",
            "《■》のもとに■■され、\x01",
            "人々を《■■》の呪縛から解き放つのだ。\x01\x01",
            "それが我が《Ｄ∴Ｇ教団》の先人が残した\x01",
            "預言であり、成すべき大望なのである──。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_8F59")

    label("loc_8DEF")

    SetChrName("")

    #A0290
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2S《御子》は生まれし時代から\x01",
            "《グノーシス》を介して、無限ともいえる\x01",
            "知識を御身に宿したとされる。\x01\x01",
            "──《叡智》に至りし時《御子》は目覚め、\x01",
            "真なる神《Ｄ》と成るであろう。\x01",
            "そして、全ての人々の意思と魂魄は\x01",
            "《Ｄ》のもとに集約され、\x01",
            "人々を《女神》の呪縛から解き放つのだ。\x01\x01",
            "それが我が《Ｄ∴Ｇ教団》の先人が残した\x01",
            "預言であり、成すべき大望なのである──。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_8F59")

    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Return()

    # Function_20_85F9 end

    def Function_21_8F6D(): pass

    label("Function_21_8F6D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8F92")
    SetChrPos(0xFE, 3220, 0, 12810, 0)
    Jump("loc_9046")

    label("loc_8F92")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8FB7")
    SetChrPos(0xFE, 2220, 0, 12400, 0)
    Jump("loc_9046")

    label("loc_8FB7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8FDC")
    SetChrPos(0xFE, 4050, 0, 12360, 0)
    Jump("loc_9046")

    label("loc_8FDC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9001")
    SetChrPos(0xFE, 3080, 0, 11680, 0)
    Jump("loc_9046")

    label("loc_9001")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9026")
    SetChrPos(0xFE, 2430, 0, 10480, 0)
    Jump("loc_9046")

    label("loc_9026")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9046")
    SetChrPos(0xFE, 3790, 0, 10440, 0)

    label("loc_9046")

    RunExpression(0x4, (scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_21_8F6D end

    def Function_22_9055(): pass

    label("Function_22_9055")

    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9075")
    BeginChrThread(0x101, 1, 0, 21)

    label("loc_9075")

    OP_49()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_908C")
    BeginChrThread(0x102, 1, 0, 21)

    label("loc_908C")

    OP_49()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_90A3")
    BeginChrThread(0x103, 1, 0, 21)

    label("loc_90A3")

    OP_49()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_90BA")
    BeginChrThread(0x104, 1, 0, 21)

    label("loc_90BA")

    OP_49()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_90D1")
    BeginChrThread(0x109, 1, 0, 21)

    label("loc_90D1")

    OP_49()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_90E8")
    BeginChrThread(0x105, 1, 0, 21)

    label("loc_90E8")

    OP_49()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_90FF")
    BeginChrThread(0x106, 1, 0, 21)

    label("loc_90FF")

    OP_49()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9116")
    BeginChrThread(0x10A, 1, 0, 21)

    label("loc_9116")

    OP_49()
    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_9130")
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    label("loc_9130")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_9149")
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)

    label("loc_9149")

    Return()

    # Function_22_9055 end

    def Function_23_914A(): pass

    label("Function_23_914A")

    ClearScenarioFlags(0x0, 7)
    ClearScenarioFlags(0x1, 0)
    ClearScenarioFlags(0x1, 1)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_915D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_9380")
    Jc((scpexpr(EXPR_23, 0x6), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_E4(0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_919C")
    OP_D2(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x0, 7)
    Jump("loc_937B")

    label("loc_919C")

    Jc((scpexpr(EXPR_23, 0x6), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_E4(0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x28), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_91D0")
    OP_D2(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x0, 7)
    Jump("loc_937B")

    label("loc_91D0")

    Jc((scpexpr(EXPR_23, 0x6), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_E4(0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x46), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9204")
    OP_D2(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x0, 7)
    Jump("loc_937B")

    label("loc_9204")

    Jc((scpexpr(EXPR_23, 0x6), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_E4(0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9238")
    OP_D2(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x0, 7)
    Jump("loc_937B")

    label("loc_9238")

    Jc((scpexpr(EXPR_23, 0x6), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_E4(0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x82), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_926C")
    OP_D2(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x0, 7)
    Jump("loc_937B")

    label("loc_926C")

    Jc((scpexpr(EXPR_23, 0x6), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_E4(0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0xA0), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_92A0")
    OP_D2(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x0, 7)
    Jump("loc_937B")

    label("loc_92A0")

    Jc((scpexpr(EXPR_23, 0x6), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_E4(0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0xC8), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_92D4")
    OP_D2(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x0, 7)
    Jump("loc_937B")

    label("loc_92D4")

    Jc((scpexpr(EXPR_23, 0x6), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_E4(0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0xFA), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9308")
    OP_D2(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x0, 7)
    Jump("loc_937B")

    label("loc_9308")

    Jc((scpexpr(EXPR_23, 0x6), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_E4(0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x118), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_933F")
    OP_D2(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x0, 7)
    SetScenarioFlags(0x1, 0)
    Jump("loc_937B")

    label("loc_933F")

    Jc((scpexpr(EXPR_23, 0x6), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_E4(0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x131), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9376")
    OP_D2(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x0, 7)
    SetScenarioFlags(0x1, 1)
    Jump("loc_937B")

    label("loc_9376")

    Jump("loc_9380")

    label("loc_937B")

    Jump("loc_915D")

    label("loc_9380")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_9D15")
    EventBegin(0x0)
    FadeToDark(500, 0, -1)
    OP_0D()
    OP_68(2310, 1440, 13000, 0)
    MoveCamera(39, 17, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(21380, 0)
    Call(0, 22)
    OP_93(0xC, 0xB4, 0x0)
    SetChrSubChip(0xC, 0x0)
    OP_4B(0xC, 0xFF)
    FadeToBright(500, 0)
    OP_0D()

    #C0291
    ChrTalk(
        0xC,
        (
            "あら、皆さん……\x01",
            "戦闘手帳が\x01",
            "大分埋まってきたようですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0292
    ChrTalk(
        0xC,
        (
            "魔獣の情報を控えたいので\x01",
            "一度見せてもらっていいでしょうか？\x02",
        )
    )

    CloseMessageWindow()

    #C0293
    ChrTalk(
        0x101,
        "#12P#0000Fええ、喜んで。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(1800)
    FadeToBright(1000, 0)
    OP_0D()

    #C0294
    ChrTalk(
        0xC,
        (
            "ありがとうございました。\x01",
            "手帳を返却しますね。\x02",
        )
    )

    CloseMessageWindow()

    #C0295
    ChrTalk(
        0xC,
        (
            "こちらは今回の手当てとなります。\x01",
            "どうぞ受け取ってください。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9585")

    #A0296
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "５００ミラ\x07\x00",
            "を受け取った。\x02",
        )
    )

    AddMira(500)
    CloseMessageWindow()
    Sound(17, 0, 100, 0)

    #A0297
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x38E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を1個、受け取った。\x02",
        )
    )

    AddItemNumber(0x38E, 1)
    Jump("loc_98FC")

    label("loc_9585")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_95E8")

    #A0298
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "１０００ミラ\x07\x00",
            "を受け取った。\x02",
        )
    )

    AddMira(1000)
    CloseMessageWindow()
    Sound(17, 0, 100, 0)

    #A0299
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x38E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を2個、受け取った。\x02",
        )
    )

    AddItemNumber(0x38E, 2)
    Jump("loc_98FC")

    label("loc_95E8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_964B")

    #A0300
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "１５００ミラ\x07\x00",
            "を受け取った。\x02",
        )
    )

    AddMira(1500)
    CloseMessageWindow()
    Sound(17, 0, 100, 0)

    #A0301
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x38E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を3個、受け取った。\x02",
        )
    )

    AddItemNumber(0x38E, 3)
    Jump("loc_98FC")

    label("loc_964B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_96AE")

    #A0302
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "２０００ミラ\x07\x00",
            "を受け取った。\x02",
        )
    )

    AddMira(2000)
    CloseMessageWindow()
    Sound(17, 0, 100, 0)

    #A0303
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x38E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を4個、受け取った。\x02",
        )
    )

    AddItemNumber(0x38E, 4)
    Jump("loc_98FC")

    label("loc_96AE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9711")

    #A0304
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "２５００ミラ\x07\x00",
            "を受け取った。\x02",
        )
    )

    AddMira(2500)
    CloseMessageWindow()
    Sound(17, 0, 100, 0)

    #A0305
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x38E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を5個、受け取った。\x02",
        )
    )

    AddItemNumber(0x38E, 5)
    Jump("loc_98FC")

    label("loc_9711")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9774")

    #A0306
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "３０００ミラ\x07\x00",
            "を受け取った。\x02",
        )
    )

    AddMira(3000)
    CloseMessageWindow()
    Sound(17, 0, 100, 0)

    #A0307
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x38E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を6個、受け取った。\x02",
        )
    )

    AddItemNumber(0x38E, 6)
    Jump("loc_98FC")

    label("loc_9774")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_97D7")

    #A0308
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "３５００ミラ\x07\x00",
            "を受け取った。\x02",
        )
    )

    AddMira(3500)
    CloseMessageWindow()
    Sound(17, 0, 100, 0)

    #A0309
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x38E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を7個、受け取った。\x02",
        )
    )

    AddItemNumber(0x38E, 7)
    Jump("loc_98FC")

    label("loc_97D7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_983A")

    #A0310
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "４０００ミラ\x07\x00",
            "を受け取った。\x02",
        )
    )

    AddMira(4000)
    CloseMessageWindow()
    Sound(17, 0, 100, 0)

    #A0311
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x38E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を8個、受け取った。\x02",
        )
    )

    AddItemNumber(0x38E, 8)
    Jump("loc_98FC")

    label("loc_983A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_989D")

    #A0312
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "４５００ミラ\x07\x00",
            "を受け取った。\x02",
        )
    )

    AddMira(4500)
    CloseMessageWindow()
    Sound(17, 0, 100, 0)

    #A0313
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x38E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を9個、受け取った。\x02",
        )
    )

    AddItemNumber(0x38E, 9)
    Jump("loc_98FC")

    label("loc_989D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_98FC")

    #A0314
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "５０００ミラ\x07\x00",
            "を受け取った。\x02",
        )
    )

    AddMira(5000)
    CloseMessageWindow()
    Sound(17, 0, 100, 0)

    #A0315
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x38E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を10個、受け取った。\x02",
        )
    )

    AddItemNumber(0x38E, 10)

    label("loc_98FC")

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9938")
    Sound(17, 0, 100, 0)

    #A0316
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x395),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を2個、受け取った。\x02",
        )
    )

    AddItemNumber(0x395, 2)
    CloseMessageWindow()
    Jump("loc_9969")

    label("loc_9938")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9969")
    Sound(17, 0, 100, 0)

    #A0317
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x395),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を受け取った。\x02",
        )
    )

    AddItemNumber(0x395, 1)
    CloseMessageWindow()

    label("loc_9969")

    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    Jc((scpexpr(EXPR_23, 0x6), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_9AA6")

    #C0318
    ChrTalk(
        0xC,
        (
            "また魔獣の情報が集まったら\x01",
            "立ち寄ってくださいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0319
    ChrTalk(
        0x101,
        "#12P#0000Fはい、宜しくお願いします。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9A2E")

    #C0320
    ChrTalk(
        0x102,
        "#12P#0100Fまたお邪魔させて頂きますね。\x02",
    )

    CloseMessageWindow()
    Jump("loc_9AA1")

    label("loc_9A2E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9A65")

    #C0321
    ChrTalk(
        0x103,
        "#12P#0200Fまたお邪魔します。\x02",
    )

    CloseMessageWindow()
    Jump("loc_9AA1")

    label("loc_9A65")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9AA1")

    #C0322
    ChrTalk(
        0x104,
        "#12P#0300Fまたお邪魔させてもらうッス。\x02",
    )

    CloseMessageWindow()

    label("loc_9AA1")

    Jump("loc_9CAD")

    label("loc_9AA6")


    #C0323
    ChrTalk(
        0xC,
        (
            "新型魔獣の情報も\x01",
            "十分に集まったようですね。\x01",
            "どうもありがとうございました。\x02",
        )
    )

    CloseMessageWindow()

    #C0324
    ChrTalk(
        0xC,
        (
            "これで今後の安全対策も\x01",
            "より万全なものに出来ると思います。\x02",
        )
    )

    CloseMessageWindow()

    #C0325
    ChrTalk(
        0x101,
        "#12P#0000Fはは……お役に立てて光栄です。\x02",
    )

    CloseMessageWindow()

    #C0326
    ChrTalk(
        0xC,
        (
            "ふふ、皆さんには本当に\x01",
            "お世話になりますね。\x02",
        )
    )

    CloseMessageWindow()

    #C0327
    ChrTalk(
        0xC,
        (
            "それでは、今回は\x01",
            "特別報酬もお渡しさせていただきます。\x01",
            "是非お受け取りください。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0328
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "１００００ミラ\x07\x00",
            "を受け取った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddMira(10000)

    #C0329
    ChrTalk(
        0xC,
        (
            "今後とも皆様のご活躍を\x01",
            "お祈りさせていただきます。\x02",
        )
    )

    CloseMessageWindow()

    #C0330
    ChrTalk(
        0xC,
        (
            "また何かありましたら\x01",
            "いつでもお越しくださいね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9CAD")

    FadeToDark(500, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_9CC4")
    ClearScenarioFlags(0x0, 6)

    label("loc_9CC4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_9CDD")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)

    label("loc_9CDD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_9CF6")
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)

    label("loc_9CF6")

    OP_4C(0xC, 0xFF)
    SetChrPos(0x0, 2470, 0, 12690, 0)
    EventEnd(0x5)
    TalkBegin(0xC)
    Jump("loc_9E57")

    label("loc_9D15")

    Jc((scpexpr(EXPR_23, 0x6), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9DCC")

    #C0331
    ChrTalk(
        0xC,
        (
            "本部に集まった情報も\x01",
            "もう十分だと思いますので、\x01",
            "調査はここまでとさせて頂きます。\x02",
        )
    )

    CloseMessageWindow()

    #C0332
    ChrTalk(
        0xC,
        (
            "また何かお願いする事が\x01",
            "あるかもしれません。\x01",
            "その時は宜しくお願いします。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9E57")

    label("loc_9DCC")


    #C0333
    ChrTalk(
        0xC,
        (
            "戦闘手帳の内容も\x01",
            "溜まってきているようですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0334
    ChrTalk(
        0xC,
        (
            "もう少し情報が集まったら\x01",
            "私の方に見せてください。\x01",
            "情報を控えさせてもらいますから。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9E57")

    Return()

    # Function_23_914A end

    def Function_24_9E58(): pass

    label("Function_24_9E58")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_9FC7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9F3C")

    #C0335
    ChrTalk(
        0xFE,
        "おー、セルゲイのとこの子達かー。\x02",
    )

    CloseMessageWindow()

    #C0336
    ChrTalk(
        0xFE,
        (
            "実は、手の足りなくなった\x01",
            "警察学校周辺の警備を\x01",
            "任せられることになってなー。\x02",
        )
    )

    CloseMessageWindow()

    #C0337
    ChrTalk(
        0xFE,
        (
            "久々の現場指揮だが、\x01",
            "若い警官たちのためにも、\x01",
            "なんとかやっていかんとなー。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_9FC7")

    label("loc_9F3C")


    #C0338
    ChrTalk(
        0xFE,
        (
            "広域防犯課の課長となってからは\x01",
            "デスクワークが多かったが……\x02",
        )
    )

    CloseMessageWindow()

    #C0339
    ChrTalk(
        0xFE,
        (
            "この非常時だ、\x01",
            "若い警官たちのためにも、\x01",
            "なんとかやっていかんとなー。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9FC7")

    TalkEnd(0xFE)
    Return()

    # Function_24_9E58 end

    def Function_25_9FCB(): pass

    label("Function_25_9FCB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_A193")
    OP_4B(0xD, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A123")

    #C0340
    ChrTalk(
        0xE,
        (
            "やはり訓練生たちに\x01",
            "不安が広がっている様子です。\x02",
        )
    )

    CloseMessageWindow()

    #C0341
    ChrTalk(
        0xE,
        (
            "たまたま交通の講習に来ていた\x01",
            "市民たちも、結界の消滅を聞いて\x01",
            "街に帰りたがっています。\x02",
        )
    )

    CloseMessageWindow()

    #C0342
    ChrTalk(
        0xD,
        (
            "うーむ、やはりそちらの対処が\x01",
            "性急かもしれんなー。\x02",
        )
    )

    CloseMessageWindow()

    #C0343
    ChrTalk(
        0xD,
        (
            "よしわかった、そちらの対応は\x01",
            "私と婦警たちで行おう。\x02",
        )
    )

    CloseMessageWindow()

    #C0344
    ChrTalk(
        0xD,
        (
            "君たちは引き続き\x01",
            "警備を続けてくれー。\x02",
        )
    )

    CloseMessageWindow()

    #C0345
    ChrTalk(
        0xE,
        "ハッ！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_A18F")

    label("loc_A123")


    #C0346
    ChrTalk(
        0xD,
        (
            "訓練生たちや市民の対応は\x01",
            "私と婦警たちで行おう。\x02",
        )
    )

    CloseMessageWindow()

    #C0347
    ChrTalk(
        0xD,
        (
            "君たちは引き続き\x01",
            "警備を続けてくれー。\x02",
        )
    )

    CloseMessageWindow()

    #C0348
    ChrTalk(
        0xE,
        "ハッ！\x02",
    )

    CloseMessageWindow()

    label("loc_A18F")

    OP_4C(0xD, 0xFF)

    label("loc_A193")

    TalkEnd(0xFE)
    Return()

    # Function_25_9FCB end

    def Function_26_A197(): pass

    label("Function_26_A197")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch02500.itc", 0x1E)
    LoadChrToIndex("chr/ch00002.itc", 0x1F)
    LoadChrToIndex("chr/ch00102.itc", 0x20)
    LoadChrToIndex("chr/ch02902.itc", 0x21)
    LoadChrToIndex("chr/ch03002.itc", 0x22)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis416.itp")
    OP_68(0, 1000, 15000, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(25000, 0)
    SetChrPos(0x101, 500, 0, 1000, 0)
    SetChrPos(0x109, -500, 0, 1000, 0)
    SetChrPos(0x102, 500, 0, 0, 0)
    SetChrPos(0x105, -500, 0, 0, 0)
    SetChrChipByIndex(0xF, 0x1E)
    SetChrSubChip(0xF, 0x0)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 750, 0, 10000, 270)
    ClearChrFlags(0x8, 0x80)
    OP_4B(0x8, 0xFF)
    SetChrPos(0x8, -750, 0, 10000, 90)
    FadeToBright(1000, 0)
    OP_68(0, 1000, 10000, 6000)
    OP_6F(0x79)
    OP_0D()
    OP_63(0xF, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_A2CE():
        OP_93(0xF, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF, 0, lambda_A2CE)
    Sleep(50)

    def lambda_A2DE():
        OP_93(0x8, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_A2DE)
    Sleep(50)
    WaitChrThread(0xF, 0)
    WaitChrThread(0x8, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x69, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_A527")

    #C0349
    ChrTalk(
        0xF,
        "#01005F#5Pおー、やっと来やがったか。\x02",
    )

    CloseMessageWindow()
    OP_68(0, 1000, 9000, 4000)

    def lambda_A33D():
        OP_9B(0x0, 0x101, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_A33D)
    Sleep(0)

    def lambda_A355():
        OP_9B(0x0, 0x102, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_A355)
    Sleep(0)

    def lambda_A36D():
        OP_9B(0x0, 0x109, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_A36D)
    Sleep(0)

    def lambda_A385():
        OP_9B(0x0, 0x105, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_A385)
    Sleep(0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    OP_6F(0x79)

    #C0350
    ChrTalk(
        0x8,
        (
            "#5Pロイド君、ノエル曹長。\x01",
            "しばらくぶりだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0351
    ChrTalk(
        0x101,
        (
            "#00004F#11Pただいま到着しました、\x01",
            "遅くなって申し訳ありません。\x02",
        )
    )

    CloseMessageWindow()

    #C0352
    ChrTalk(
        0xF,
        (
            "#01000F#5Pああ、さっき連絡があったが\x01",
            "暴走車の取り締まりを\x01",
            "手伝っていたそうだな。\x02\x03",

            "#01004Fまあ、そういう事なら\x01",
            "遅刻も大目に見てやろう。\x01",
            "……ご苦労だったな。\x02",
        )
    )

    CloseMessageWindow()

    #C0353
    ChrTalk(
        0x101,
        (
            "#00012F#11Pはは、ありがとうございます。\x02\x03",

            "#00002Fそれと、ホアン事務長、\x01",
            "ご無沙汰しています。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A653")

    label("loc_A527")


    #C0354
    ChrTalk(
        0xF,
        "#01005F#5Pおー、来やがったか。\x02",
    )

    CloseMessageWindow()
    OP_68(0, 1000, 9000, 4000)

    def lambda_A561():
        OP_9B(0x0, 0x101, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_A561)
    Sleep(0)

    def lambda_A579():
        OP_9B(0x0, 0x102, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_A579)
    Sleep(0)

    def lambda_A591():
        OP_9B(0x0, 0x109, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_A591)
    Sleep(0)

    def lambda_A5A9():
        OP_9B(0x0, 0x105, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_A5A9)
    Sleep(0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    OP_6F(0x79)

    #C0355
    ChrTalk(
        0x8,
        (
            "#5Pロイド君、ノエル曹長。\x01",
            "しばらくぶりだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0356
    ChrTalk(
        0x101,
        (
            "#00004F#11Pただいま到着しました。\x02\x03",

            "#00002Fホアン事務長、\x01",
            "ご無沙汰しています。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A653")


    #C0357
    ChrTalk(
        0x109,
        "#10109F#12Pお元気そうで何よりです。\x02",
    )

    CloseMessageWindow()

    #C0358
    ChrTalk(
        0x8,
        (
            "#5Pはは、ノエル君とは\x01",
            "この前の定期演習以来か。\x02",
        )
    )

    CloseMessageWindow()

    #C0359
    ChrTalk(
        0x8,
        (
            "#5Pロイド君は卒業以来だから\x01",
            "１０ヶ月ぶりになるかな。\x02",
        )
    )

    CloseMessageWindow()

    #C0360
    ChrTalk(
        0x8,
        (
            "#5Pいや、しばらく見ないうちに\x01",
            "すっかり立派になったもんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0361
    ChrTalk(
        0x101,
        (
            "#00012F#11Pはは……\x01",
            "まだまだ半人前ですよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0362
    ChrTalk(
        0x102,
        "#00105F#12Pえっと……\x02",
    )

    CloseMessageWindow()

    #C0363
    ChrTalk(
        0x105,
        (
            "#10300F#12P察するに警察学校の\x01",
            "責任者といった所かな？\x02",
        )
    )

    CloseMessageWindow()

    #C0364
    ChrTalk(
        0xF,
        (
            "#01004F#5Pああ、周辺施設の管理全般を\x01",
            "担当されているホアン事務長だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0365
    ChrTalk(
        0x8,
        (
            "#5Pいやいや。\x01",
            "そんな大層なもんじゃないよ。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0xF, 500)
    Sleep(300)

    #C0366
    ChrTalk(
        0x8,
        (
            "#6Pそれじゃあ、セルゲイ君。\x01",
            "ミーティングルームは\x01",
            "自由に使ってくれたまえ。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xF, 0x8, 500)

    #C0367
    ChrTalk(
        0xF,
        "#01002F#11Pええ、そうさせてもらいます。\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x8, 3, 0, 27)
    Sleep(3000)
    TurnDirection(0xF, 0x101, 500)

    #C0368
    ChrTalk(
        0xF,
        (
            "#01003F#5P──さて、時間が惜しい。\x02\x03",

            "#01000F早速始めるから\x01",
            "とっとと付いて来い。\x02",
        )
    )

    CloseMessageWindow()
    OP_68(1280, 1000, 9280, 1500)
    OP_93(0xF, 0x5A, 0x1F4)

    def lambda_A936():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_A936)

    def lambda_A94B():

        label("loc_A94B")

        TurnDirection(0xFE, 0xF, 500)
        Yield()
        Jump("loc_A94B")

    QueueWorkItem2(0x101, 2, lambda_A94B)

    def lambda_A95D():

        label("loc_A95D")

        TurnDirection(0xFE, 0xF, 500)
        Yield()
        Jump("loc_A95D")

    QueueWorkItem2(0x102, 2, lambda_A95D)

    def lambda_A96F():

        label("loc_A96F")

        TurnDirection(0xFE, 0xF, 500)
        Yield()
        Jump("loc_A96F")

    QueueWorkItem2(0x109, 2, lambda_A96F)

    def lambda_A981():

        label("loc_A981")

        TurnDirection(0xFE, 0xF, 500)
        Yield()
        Jump("loc_A981")

    QueueWorkItem2(0x105, 2, lambda_A981)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x109, 0x2)
    EndChrThread(0x105, 0x2)
    OP_4B(0xF, 0xFF)

    #C0369
    ChrTalk(
        0x102,
        "#00105F#12Pあの、セルゲイ課長？\x02",
    )

    CloseMessageWindow()

    #C0370
    ChrTalk(
        0x101,
        (
            "#00001F#6Pえっと……\x01",
            "結局どんな用件なんですか？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xF, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xF, 0x101, 500)

    #C0371
    ChrTalk(
        0xF,
        (
            "#01005F#11Pなんだ、まだ気付いてないのか？\x02\x03",

            "#01004F色々ヒントはあったはずだが……\x01",
            "クク、まだまだヒヨッ子って所か。\x02",
        )
    )

    CloseMessageWindow()

    #C0372
    ChrTalk(
        0x101,
        (
            "#00011F#6Pうっ……ま、待ってください！\x02\x03",

            "#00003F色々なヒント……\x01",
            "この場所に俺たちを呼ぶ意味……\x02\x03",

            "#00000Fもしかして──\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    #A0373
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1Kセルゲイが呼んだ用件は？\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【捜査官試験の講習】\x01",          # 0
            "【交通基本法の講習】\x01",          # 1
            "【導力ネット技術の講習】\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_ABDB"),
        (1, "loc_ACD8"),
        (2, "loc_AD7E"),
        (SWITCH_DEFAULT, "loc_AE6B"),
    )


    label("loc_ABDB")


    #C0374
    ChrTalk(
        0xF,
        (
            "#01006F#11P捜査官資格は既に\x01",
            "お前が持ってるだろうが。\x02\x03",

            "#01003F特務支援課の性質上、\x01",
            "メンバー全員が捜査官資格を\x01",
            "持っている必要はない。\x02\x03",

            "#01000F答えは──\x01",
            "『交通基本法の講習』だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0375
    ChrTalk(
        0x101,
        "#00005F#6Pあ……\x02",
    )

    CloseMessageWindow()

    #C0376
    ChrTalk(
        0x102,
        "#00102F#12Pということは、もしかして……\x02",
    )

    CloseMessageWindow()
    Jump("loc_AE6B")

    label("loc_ACD8")

    OP_2C(0xA1, 0x1)

    #C0377
    ChrTalk(
        0x101,
        (
            "#00002F#6Pそうか……\x01",
            "『交通基本法の講習』ですね？\x02",
        )
    )

    CloseMessageWindow()

    #C0378
    ChrTalk(
        0x102,
        "#00105F#12Pあ……！\x02",
    )

    CloseMessageWindow()

    #C0379
    ChrTalk(
        0xF,
        "#01004F#11Pクク、正解だ。\x02",
    )

    CloseMessageWindow()

    #C0380
    ChrTalk(
        0x109,
        (
            "#10105F#6Pえっと……\x01",
            "それはもしかして？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AE6B")

    label("loc_AD7E")


    #C0381
    ChrTalk(
        0xF,
        (
            "#01003F#11P確かにここにも導力ネットが\x01",
            "引かれているが……\x02\x03",

            "お前らにそれをさせるなら\x01",
            "財団の事務所あたりに行かせるさ。\x02\x03",

            "#01000F答えは──\x01",
            "『交通基本法の講習』だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0382
    ChrTalk(
        0x101,
        "#00005F#6Pあ……\x02",
    )

    CloseMessageWindow()

    #C0383
    ChrTalk(
        0x102,
        "#00102F#12Pということは、もしかして……\x02",
    )

    CloseMessageWindow()
    Jump("loc_AE6B")

    label("loc_AE6B")


    #C0384
    ChrTalk(
        0xF,
        (
            "#01004F#11Pああ、このたび特務支援課に\x01",
            "導力車が支給される事になった。\x02\x03",

            "#01002Fこれを機に、交通法のイロハを\x01",
            "頭に叩き込んでもらうぞ。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x8, 0x3)
    SetChrPos(0x8, 0, 0, 15500, 180)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(2000)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_68(65000, 3000, 16500, 0)
    MoveCamera(51, 15, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(17000, 0)
    SetChrChipByIndex(0x101, 0x1F)
    SetChrSubChip(0x101, 0x2)
    SetChrChipByIndex(0x102, 0x20)
    SetChrSubChip(0x102, 0x1)
    SetChrChipByIndex(0x109, 0x21)
    SetChrSubChip(0x109, 0x2)
    SetChrChipByIndex(0x105, 0x22)
    SetChrSubChip(0x105, 0x1)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x109, 0x4)
    SetChrFlags(0x105, 0x4)
    SetChrPos(0x101, 66840, 150, 16500, 270)
    SetChrPos(0x102, 63210, 150, 16500, 90)
    SetChrPos(0x109, 66800, 150, 13500, 270)
    SetChrPos(0x105, 63230, 150, 13500, 90)
    SetChrPos(0xF, 65000, 0, 20000, 0)
    FadeToBright(1000, 0)
    OP_68(65000, 1000, 16500, 3000)
    OP_6F(0x79)
    OP_0D()
    Sleep(500)
    OP_93(0xF, 0xB4, 0x1F4)

    #C0385
    ChrTalk(
        0xF,
        (
            "#01003F#5P──以上が導力車を扱う上で\x01",
            "最低限覚えておく交通基本法だ。\x02\x03",

            "#01000F一応、頭に叩き込んだか？\x02",
        )
    )

    CloseMessageWindow()

    #C0386
    ChrTalk(
        0x101,
        "#00006F#11Pな、何とか。\x02",
    )

    CloseMessageWindow()

    #C0387
    ChrTalk(
        0x105,
        (
            "#10306F#12Pやれやれ、こんな所で\x01",
            "授業が待っているとはね……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x69, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_B2B6")

    #C0388
    ChrTalk(
        0x102,
        (
            "#00100F#6P……でも、思ったよりも\x01",
            "簡単なルールしかないんですね。\x02\x03",

            "#00103Fさっきの暴走車の事件みたいに、\x01",
            "外国人への罰則が弱い面も\x01",
            "もちろんありますけど……\x02\x03",

            "#00101Fこの先、導力車が増えてきたら\x01",
            "これだけでは対処できなさそうな\x01",
            "気がするんですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0389
    ChrTalk(
        0xF,
        (
            "#01006F#5Pそいつは今後の課題だな。\x02\x03",

            "#01001F自家用導力車が普及し始めてから\x01",
            "まだ１０年と経っていない。\x02\x03",

            "いずれ、より厳密なルールが\x01",
            "求められることになるだろう。\x02\x03",

            "外国人への罰則などに関してもな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B3F7")

    label("loc_B2B6")


    #C0390
    ChrTalk(
        0x102,
        (
            "#00103F#6P……でも、思ったよりも\x01",
            "簡単なルールしかないんですね。\x02\x03",

            "#00101Fこの先、導力車が増えてきたら\x01",
            "これだけでは対処できなさそうな\x01",
            "気がするんですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0391
    ChrTalk(
        0xF,
        (
            "#01006F#5Pそいつは今後の課題だな。\x02\x03",

            "#01001F自家用導力車が普及し始めてから\x01",
            "まだ１０年と経っていない。\x02\x03",

            "いずれ、より厳密なルールが\x01",
            "求められることになるだろう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B3F7")


    #C0392
    ChrTalk(
        0x109,
        (
            "#10103F#11P今だと役所に申請すれば\x01",
            "簡単に運転免許が\x01",
            "交付されるわけですけど……\x02\x03",

            "#10101Fたしか試験制度の導入も\x01",
            "検討されているんですよね？\x02",
        )
    )

    CloseMessageWindow()

    #C0393
    ChrTalk(
        0xF,
        (
            "#01003F#5Pああ、そうなった場合は\x01",
            "各種講習に実技試験も\x01",
            "入ってくるだろう。\x02\x03",

            "#01000Fま、とりあえず今日のところは\x01",
            "基本のルールを叩き込んでおけ。\x02\x03",

            "実際の運転は──\x01",
            "ノエル、お前にやってもらおう。\x02",
        )
    )

    CloseMessageWindow()

    #C0394
    ChrTalk(
        0x109,
        "#10102F#11Pはい、了解しました！\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x1)
    Sleep(50)
    SetChrSubChip(0x102, 0x0)
    Sleep(50)
    SetChrSubChip(0x105, 0x0)

    #C0395
    ChrTalk(
        0x101,
        (
            "#00002F#5Pそうか、ノエルは当然、\x01",
            "導力車を運転できるんだよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0396
    ChrTalk(
        0x102,
        (
            "#00109F#6P警備隊車両をあれだけ自在に\x01",
            "運転できるくらいだものね。\x02",
        )
    )

    CloseMessageWindow()

    #C0397
    ChrTalk(
        0x105,
        "#10305F#6Pへえ、そうなんだ？\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x109, 0x0)
    Sleep(300)

    #C0398
    ChrTalk(
        0x109,
        (
            "#10112F#11Pあはは……入隊して以来、\x01",
            "司令に叩き込まれたから。\x02",
        )
    )

    CloseMessageWindow()

    #C0399
    ChrTalk(
        0xF,
        (
            "#01003F#5Pよし、それじゃあ早速、\x01",
            "お前らに導力車を支給する。\x02\x03",

            "#01000F外に用意するから付いて来い。\x02",
        )
    )

    CloseMessageWindow()
    OP_68(65000, 1000, 15350, 6000)
    BeginChrThread(0xF, 3, 0, 28)
    WaitChrThread(0xF, 3)
    OP_6F(0x79)
    SetChrFlags(0xF, 0x80)
    Sound(103, 0, 100, 0)
    Sleep(600)
    Sound(104, 0, 100, 0)
    Sleep(600)

    #C0400
    ChrTalk(
        0x101,
        (
            "#00012F#5Pはは……\x01",
            "とんだサプライズだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0401
    ChrTalk(
        0x102,
        "#00102F#6Pええ、課長も人が悪いわね。\x02",
    )

    CloseMessageWindow()

    #C0402
    ChrTalk(
        0x105,
        (
            "#10304F#6Pしかし導力車か。\x02\x03",

            "#10300F僕はあんまり詳しくないけど\x01",
            "ヴェルヌ社かラインフォルト社の\x01",
            "どちらかになるんだっけ？\x02",
        )
    )

    CloseMessageWindow()

    #C0403
    ChrTalk(
        0x109,
        (
            "#10109F#11Pうん、自家用導力車といえば\x01",
            "その２大メーカーしかないからね。\x02\x03",

            "#10102Fで、ヴェルヌ社の方が\x01",
            "老舗#4Rしにせ#でラインナップも豊富なの。\x02\x03",

            "小型車から中型車、\x01",
            "バスまで手広く扱っているし。\x02",
        )
    )

    CloseMessageWindow()

    #C0404
    ChrTalk(
        0x102,
        (
            "#00100F#6Pラインフォルト社が出しているのは\x01",
            "運搬車やリムジンが多いのよね？\x02",
        )
    )

    CloseMessageWindow()

    #C0405
    ChrTalk(
        0x109,
        (
            "#10104F#11Pええ、どちらかというと\x01",
            "頑丈で高級なものが多いですね。\x02\x03",

            "#10100F導力列車や導力戦車の技術を\x01",
            "転用したものが多いみたいですし。\x02",
        )
    )

    CloseMessageWindow()

    #C0406
    ChrTalk(
        0x101,
        (
            "#00004F#5Pうーん……\x01",
            "いきなりで実感が無かったけど\x01",
            "ちょっとドキドキしてきたな。\x02\x03",

            "#00000Fよし、見に行ってみよう。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_CC(0x1, 0xFF, 0x0)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x102, 0x4)
    ClearChrFlags(0x109, 0x4)
    ClearChrFlags(0x105, 0x4)
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_D7(0x20)
    OP_D7(0x21)
    OP_D7(0x22)
    SetChrPos(0x0, 61500, 0, 18000, 180)
    SetScenarioFlags(0x127, 5)
    OP_29(0xA1, 0x1, 0x8)
    EventEnd(0x5)
    Return()

    # Function_26_A197 end

    def Function_27_BA5A(): pass

    label("Function_27_BA5A")

    OP_93(0xFE, 0x13B, 0x1F4)
    OP_95(0xFE, -3000, 0, 13250, 2000, 0x0)
    OP_95(0xFE, -6500, 0, 13250, 2000, 0x0)
    Return()

    # Function_27_BA5A end

    def Function_28_BA8A(): pass

    label("Function_28_BA8A")

    OP_93(0xFE, 0xE1, 0x1F4)
    OP_95(0xFE, 61500, 0, 18500, 2500, 0x0)
    OP_95(0xFE, 61500, 0, 6500, 2500, 0x0)
    Return()

    # Function_28_BA8A end

    def Function_29_BABA(): pass

    label("Function_29_BABA")

    EventBegin(0x0)
    Fade(500)
    OP_68(-970, 1400, 13500, 0)
    MoveCamera(42, 20, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(20360, 0)
    SetChrPos(0x101, -600, 0, 13400, 0)
    SetChrPos(0x102, 600, 0, 13400, 0)
    SetChrPos(0x103, -700, 0, 12200, 0)
    SetChrPos(0x104, 700, 0, 12200, 0)
    SetChrPos(0xF4, -800, 0, 11000, 0)
    SetChrPos(0xF5, 800, 0, 11000, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0x8, 0xFF)
    OP_93(0x8, 0xB4, 0x0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BC, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C308")

    #C0407
    ChrTalk(
        0x8,
        (
            "おや、君たちは\x01",
            "特務支援課じゃないか。\x02",
        )
    )

    CloseMessageWindow()

    #C0408
    ChrTalk(
        0x8,
        (
            "いや、よかった。\x01",
            "無事だったんだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0409
    ChrTalk(
        0x101,
        (
            "#12P#00000Fホアン事務長……\x01",
            "そちらこそ無事でなによりです。\x02",
        )
    )

    CloseMessageWindow()

    #C0410
    ChrTalk(
        0x102,
        (
            "#12P#00105Fこちらには警官隊が\x01",
            "来ているみたいですね。\x02\x03",

            "#00103Fこの辺りは国防軍が\x01",
            "警備していたんじゃ……？\x02",
        )
    )

    CloseMessageWindow()

    #C0411
    ChrTalk(
        0x8,
        (
            "ああ、大統領が拘束されたとの\x01",
            "一報が入って、撤退していったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0412
    ChrTalk(
        0x8,
        (
            "各地の混乱を収めるためにも、\x01",
            "国防軍には頑張ってもらわないと\x01",
            "いけないからね。\x02",
        )
    )

    CloseMessageWindow()

    #C0413
    ChrTalk(
        0x8,
        (
            "入れ替わりに警察本部からの応援がきて、\x01",
            "この場の混乱を収拾しているわけさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0414
    ChrTalk(
        0x102,
        "#12P#00100Fそうでしたか……\x02",
    )

    CloseMessageWindow()

    #C0415
    ChrTalk(
        0x104,
        (
            "#12P#00303Fそういえば……\x01",
            "ガルシアのオッサンは\x01",
            "結局どうなったんだろうな？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_BE36")

    #C0416
    ChrTalk(
        0x105,
        (
            "#12P#10402Fロイドが拘置所を脱出するのに\x01",
            "力を貸りたっていう話だったね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BEF9")

    label("loc_BE36")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_BE9B")

    #C0417
    ChrTalk(
        0x109,
        (
            "#12P#10100Fロイドさんが拘置所を脱出するのに\x01",
            "力を貸りたっていう話でしたね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BEF9")

    label("loc_BE9B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_BEF9")

    #C0418
    ChrTalk(
        0x106,
        (
            "#12P#10702Fロイドさんが拘置所を脱出するのに\x01",
            "力を貸りたという話でしたね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BEF9")


    #C0419
    ChrTalk(
        0x101,
        (
            "#12P#00000Fああ……あの時は\x01",
            "本当に助けられたよ。\x02\x03",

            "#00006Fって、さすがにこんな事を\x01",
            "こんな場所で言うのは憚#2Rはばか#られるけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0420
    ChrTalk(
        0x8,
        (
            "いや、君の逮捕に関しては、\x01",
            "大統領の拘束を受けて\x01",
            "不当性が認められたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0421
    ChrTalk(
        0x8,
        (
            "その点に関しては、\x01",
            "今更だし気にすることもないだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0422
    ChrTalk(
        0x8,
        (
            "それで、ガルシアだが……\x01",
            "彼は国防軍相手に大立ち回りをして、\x01",
            "しばらくしてから拘束されたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0423
    ChrTalk(
        0x8,
        (
            "今は拘置所に再び拘禁されて、\x01",
            "治療を受けているところだよ。\x02",
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
    OP_63(0xF4, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0xF5, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0424
    ChrTalk(
        0x103,
        "#12P#00205F治療……ですか。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C1A7")

    #C0425
    ChrTalk(
        0x10A,
        (
            "#12P#00603F一人で国防軍と戦ったのだ。\x01",
            "その消耗は推して知るべしだろう。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C277")

    label("loc_C1A7")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C20C")

    #C0426
    ChrTalk(
        0x106,
        (
            "#12P#10703F一人で国防軍と戦ったとすると……\x01",
            "消耗が激しかったんでしょうね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C277")

    label("loc_C20C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C277")

    #C0427
    ChrTalk(
        0x109,
        (
            "#12P#10103F一人で国防軍と戦ったとすると……\x01",
            "やっぱりかなりの\x01",
            "消耗があったでしょうね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C277")


    #C0428
    ChrTalk(
        0x8,
        (
            "ああ、しばらくは\x01",
            "動けない状態でね。\x02",
        )
    )

    CloseMessageWindow()

    #C0429
    ChrTalk(
        0x8,
        (
            "ただ、君達が希望するなら、\x01",
            "面会することも可能だが……\x02",
        )
    )

    CloseMessageWindow()

    #C0430
    ChrTalk(
        0x102,
        "#12P#00100Fロイド、どうするの？\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1BC, 1)
    Jump("loc_C383")

    label("loc_C308")


    #C0431
    ChrTalk(
        0x8,
        (
            "ガルシアは、\x01",
            "拘置所に再び拘禁されて\x01",
            "治療を受けているところだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0432
    ChrTalk(
        0x8,
        (
            "君達が希望するなら、\x01",
            "面会することも可能だが……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C383")

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
            "ガルシアと面会する\x01",      # 0
            "やめておく\x01",              # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C4BC")

    #C0433
    ChrTalk(
        0x101,
        (
            "#12P#00003F（ガルシアには、あの時の\x01",
            "  礼を言わなくちゃいけないな……）\x02\x03",

            "#00000F……ホアン事務長、是非お願いします。\x02",
        )
    )

    CloseMessageWindow()

    #C0434
    ChrTalk(
        0x8,
        (
            "では、メルビン君に案内させよう。\x01",
            "一緒についてきたまえ。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 1)
    NewScene("t6050", 101, 0, 0)
    IdleLoop()
    Jump("loc_C538")

    label("loc_C4BC")


    #C0435
    ChrTalk(
        0x101,
        "#12P#00003F……今はやめておきます。\x02",
    )

    CloseMessageWindow()

    #C0436
    ChrTalk(
        0x8,
        "ふむ、そうかね？\x02",
    )

    CloseMessageWindow()

    #C0437
    ChrTalk(
        0x8,
        (
            "まあ、面会を希望するなら\x01",
            "いつでも声をかけてくれたまえ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C538")

    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 0, 0, 13400, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_4C(0x8, 0xFF)
    EventEnd(0x5)
    Return()

    # Function_29_BABA end

    def Function_30_C568(): pass

    label("Function_30_C568")


    #C0438
    ChrTalk(
        0x101,
        (
            "#12P#00003F（ガルシアには、あの時の\x01",
            "  礼を言わなくちゃいけないな……）\x02\x03",

            "#00000F……ホアン事務長、是非お願いします。\x02",
        )
    )

    CloseMessageWindow()

    #C0439
    ChrTalk(
        0x8,
        (
            "では、メルビン君に案内させよう。\x01",
            "一緒についてきたまえ。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 1)
    NewScene("t6050", 101, 0, 0)
    IdleLoop()
    Return()

    # Function_30_C568 end

    def Function_31_C636(): pass

    label("Function_31_C636")

    EventBegin(0x2)
    ClearMapFlags(0x20)

    #C0440
    ChrTalk(
        0x101,
        (
            "#00000F他の階に用事はないな。\x01",
            "あまりウロウロするのは\x01",
            "止めておこう。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    EventEnd(0x3)
    Return()

    # Function_31_C636 end

    def Function_32_C68A(): pass

    label("Function_32_C68A")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    OP_0D()
    OP_AF(0xFA)
    FadeToBright(300, 0)
    OP_0D()
    TalkEnd(0xFF)
    Return()

    # Function_32_C68A end

    SaveToFile()

Try(main)
