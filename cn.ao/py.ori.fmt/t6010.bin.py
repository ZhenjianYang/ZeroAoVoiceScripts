from ScenarioHelper import *

def main():
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
        "胡安事务长",             # 1
        "训练生",                 # 2
        "训练生",                 # 3
        "教官",                   # 4
        "接待小姐瑞贝卡",         # 5
        "乔里基科长",             # 6
        "警官",                   # 7
        "赛尔盖科长",             # 8
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
        "Function_5_16B6",         # 05, 5
        "Function_6_28DC",         # 06, 6
        "Function_7_2AAF",         # 07, 7
        "Function_8_2C78",         # 08, 8
        "Function_9_31B6",         # 09, 9
        "Function_10_35F0",        # 0A, 10
        "Function_11_3865",        # 0B, 11
        "Function_12_3C71",        # 0C, 12
        "Function_13_3C75",        # 0D, 13
        "Function_14_43F0",        # 0E, 14
        "Function_15_4456",        # 0F, 15
        "Function_16_4465",        # 10, 16
        "Function_17_5F6C",        # 11, 17
        "Function_18_605F",        # 12, 18
        "Function_19_6A1C",        # 13, 19
        "Function_20_74DB",        # 14, 20
        "Function_21_7C85",        # 15, 21
        "Function_22_7D6D",        # 16, 22
        "Function_23_7E62",        # 17, 23
        "Function_24_89AC",        # 18, 24
        "Function_25_8AFD",        # 19, 25
        "Function_26_8C79",        # 1A, 26
        "Function_27_A2AE",        # 1B, 27
        "Function_28_A2DE",        # 1C, 28
        "Function_29_A30E",        # 1D, 29
        "Function_30_ABF2",        # 1E, 30
        "Function_31_ACA2",        # 1F, 31
        "Function_32_ACE6",        # 20, 32
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20F, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20F, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_16A5")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5DF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16A0")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "对话\x01",                # 0
            "交出预想外料理\x01",      # 1
            "放弃\x01",                # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_639")
    FadeToBright(300, 0)
    OP_0D()

    label("loc_639")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_65A")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 5)
    Jump("loc_169B")

    label("loc_65A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_169B")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_673")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1691")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuCmd(0, 1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20C, 0)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x192, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_6C6")
    MenuCmd(1, 1, "极苦面『断头』")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20C, 0)), scpexpr(EXPR_END)), "loc_6BC")
    Call(0, 7)

    label("loc_6BC")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20C, 1)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x195, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_6FF")
    MenuCmd(1, 1, "炼狱麻婆『阎魔』")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20C, 1)), scpexpr(EXPR_END)), "loc_6F5")
    Call(0, 7)

    label("loc_6F5")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20C, 2)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x198, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_732")
    MenuCmd(1, 1, "杂色锅巴饭")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20C, 2)), scpexpr(EXPR_END)), "loc_728")
    Call(0, 7)

    label("loc_728")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_732")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20C, 3)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x19B, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_769")
    MenuCmd(1, 1, "顽固肉排『岩』")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20C, 3)), scpexpr(EXPR_END)), "loc_75F")
    Call(0, 7)

    label("loc_75F")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_769")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20C, 4)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x19E, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_7A0")
    MenuCmd(1, 1, "混沌久煮『浊』")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20C, 4)), scpexpr(EXPR_END)), "loc_796")
    Call(0, 7)

    label("loc_796")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_7A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20C, 5)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1A1, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_7D7")
    MenuCmd(1, 1, "男人料理『山』")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20C, 5)), scpexpr(EXPR_END)), "loc_7CD")
    Call(0, 7)

    label("loc_7CD")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_7D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20C, 6)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1A4, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_80E")
    MenuCmd(1, 1, "男人料理『川』")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20C, 6)), scpexpr(EXPR_END)), "loc_804")
    Call(0, 7)

    label("loc_804")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_80E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20C, 7)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1A7, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_83D")
    MenuCmd(1, 1, "箭之鱼")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20C, 7)), scpexpr(EXPR_END)), "loc_833")
    Call(0, 7)

    label("loc_833")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_83D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20D, 0)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1AA, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_874")
    MenuCmd(1, 1, "激辣炸弹蛋包饭")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20D, 0)), scpexpr(EXPR_END)), "loc_86A")
    Call(0, 7)

    label("loc_86A")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_874")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20D, 1)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1AD, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8A3")
    MenuCmd(1, 1, "细针面")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20D, 1)), scpexpr(EXPR_END)), "loc_899")
    Call(0, 7)

    label("loc_899")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20D, 2)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1B0, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8D4")
    MenuCmd(1, 1, "苦味汉堡")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20D, 2)), scpexpr(EXPR_END)), "loc_8CA")
    Call(0, 7)

    label("loc_8CA")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20D, 3)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1B3, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_909")
    MenuCmd(1, 1, "四重番茄比萨")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20D, 3)), scpexpr(EXPR_END)), "loc_8FF")
    Call(0, 7)

    label("loc_8FF")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_909")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20D, 4)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1B6, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_93C")
    MenuCmd(1, 1, "守护三明治")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20D, 4)), scpexpr(EXPR_END)), "loc_932")
    Call(0, 7)

    label("loc_932")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_93C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20D, 5)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1B9, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_979")
    MenuCmd(1, 1, "不可思议盒饭『仰天』")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20D, 5)), scpexpr(EXPR_END)), "loc_96F")
    Call(0, 7)

    label("loc_96F")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_979")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20D, 6)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1BC, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9A8")
    MenuCmd(1, 1, "奇妙汤")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20D, 6)), scpexpr(EXPR_END)), "loc_99E")
    Call(0, 7)

    label("loc_99E")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20D, 7)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1BF, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9DB")
    MenuCmd(1, 1, "秘密棉花糖")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20D, 7)), scpexpr(EXPR_END)), "loc_9D1")
    Call(0, 7)

    label("loc_9D1")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20E, 0)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1C2, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A12")
    MenuCmd(1, 1, "反射巧克力蛋糕")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20E, 0)), scpexpr(EXPR_END)), "loc_A08")
    Call(0, 7)

    label("loc_A08")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A12")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20E, 1)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1C5, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A43")
    MenuCmd(1, 1, "爽弹布丁")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20E, 1)), scpexpr(EXPR_END)), "loc_A39")
    Call(0, 7)

    label("loc_A39")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A43")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20E, 2)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1C8, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A76")
    MenuCmd(1, 1, "痊愈冰激凌")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20E, 2)), scpexpr(EXPR_END)), "loc_A6C")
    Call(0, 7)

    label("loc_A6C")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A76")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20E, 3)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1CB, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_AA9")
    MenuCmd(1, 1, "隐秘爆米花")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20E, 3)), scpexpr(EXPR_END)), "loc_A9F")
    Call(0, 7)

    label("loc_A9F")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_AA9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20E, 4)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1CE, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_ADE")
    MenuCmd(1, 1, "良药『熊竹』")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20E, 4)), scpexpr(EXPR_END)), "loc_AD4")
    Call(0, 7)

    label("loc_AD4")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_ADE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20E, 5)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1D1, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_B0F")
    MenuCmd(1, 1, "紫色液体")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20E, 5)), scpexpr(EXPR_END)), "loc_B05")
    Call(0, 7)

    label("loc_B05")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_B0F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20E, 6)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1D4, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_B40")
    MenuCmd(1, 1, "褐色液体")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20E, 6)), scpexpr(EXPR_END)), "loc_B36")
    Call(0, 7)

    label("loc_B36")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_B40")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20E, 7)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1D7, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_B71")
    MenuCmd(1, 1, "粉红液体")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20E, 7)), scpexpr(EXPR_END)), "loc_B67")
    Call(0, 7)

    label("loc_B67")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_B71")

    MenuCmd(1, 1, "放弃")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuCmd(2, 1, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x1)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_BED")
    FadeToBright(300, 0)
    OP_0D()

    #C0001
    ChrTalk(
        0x8,
        (
            "谢谢，如果有什么合适的料理，\x01",
            "就请再拿过来吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_168C")

    label("loc_BED")

    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20C, 0)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x192, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_C62")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C58")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x192, 1)
    SetScenarioFlags(0x20C, 0)

    #A0002
    AnonymousTalk(
        0xFF,
        (
            "把",
            scpstr(SCPSTR_CODE_ITEM, 0x192),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "交给了胡安事务长。\x02",
        )
    )


    label("loc_C58")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_C62")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20C, 1)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x195, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_CB8")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CAE")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x195, 1)
    SetScenarioFlags(0x20C, 1)

    #A0003
    AnonymousTalk(
        0xFF,
        (
            "把",
            scpstr(SCPSTR_CODE_ITEM, 0x195),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "交给了胡安事务长。\x02",
        )
    )


    label("loc_CAE")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_CB8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20C, 2)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x198, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_D0E")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D04")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x198, 1)
    SetScenarioFlags(0x20C, 2)

    #A0004
    AnonymousTalk(
        0xFF,
        (
            "把",
            scpstr(SCPSTR_CODE_ITEM, 0x198),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "交给了胡安事务长。\x02",
        )
    )


    label("loc_D04")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_D0E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20C, 3)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x19B, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_D64")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D5A")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x19B, 1)
    SetScenarioFlags(0x20C, 3)

    #A0005
    AnonymousTalk(
        0xFF,
        (
            "把",
            scpstr(SCPSTR_CODE_ITEM, 0x19B),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "交给了胡安事务长。\x02",
        )
    )


    label("loc_D5A")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_D64")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20C, 4)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x19E, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_DBA")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DB0")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x19E, 1)
    SetScenarioFlags(0x20C, 4)

    #A0006
    AnonymousTalk(
        0xFF,
        (
            "把",
            scpstr(SCPSTR_CODE_ITEM, 0x19E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "交给了胡安事务长。\x02",
        )
    )


    label("loc_DB0")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_DBA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20C, 5)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1A1, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_E10")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E06")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x1A1, 1)
    SetScenarioFlags(0x20C, 5)

    #A0007
    AnonymousTalk(
        0xFF,
        (
            "把",
            scpstr(SCPSTR_CODE_ITEM, 0x1A1),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "交给了胡安事务长。\x02",
        )
    )


    label("loc_E06")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_E10")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20C, 6)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1A4, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_E66")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E5C")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x1A4, 1)
    SetScenarioFlags(0x20C, 6)

    #A0008
    AnonymousTalk(
        0xFF,
        (
            "把",
            scpstr(SCPSTR_CODE_ITEM, 0x1A4),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "交给了胡安事务长。\x02",
        )
    )


    label("loc_E5C")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_E66")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20C, 7)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1A7, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_EBC")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EB2")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x1A7, 1)
    SetScenarioFlags(0x20C, 7)

    #A0009
    AnonymousTalk(
        0xFF,
        (
            "把",
            scpstr(SCPSTR_CODE_ITEM, 0x1A7),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "交给了胡安事务长。\x02",
        )
    )


    label("loc_EB2")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_EBC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20D, 0)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1AA, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_F12")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F08")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x1AA, 1)
    SetScenarioFlags(0x20D, 0)

    #A0010
    AnonymousTalk(
        0xFF,
        (
            "把",
            scpstr(SCPSTR_CODE_ITEM, 0x1AA),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "交给了胡安事务长。\x02",
        )
    )


    label("loc_F08")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_F12")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20D, 1)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1AD, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_F68")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F5E")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x1AD, 1)
    SetScenarioFlags(0x20D, 1)

    #A0011
    AnonymousTalk(
        0xFF,
        (
            "把",
            scpstr(SCPSTR_CODE_ITEM, 0x1AD),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "交给了胡安事务长。\x02",
        )
    )


    label("loc_F5E")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_F68")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20D, 2)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1B0, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_FBE")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FB4")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x1B0, 1)
    SetScenarioFlags(0x20D, 2)

    #A0012
    AnonymousTalk(
        0xFF,
        (
            "把",
            scpstr(SCPSTR_CODE_ITEM, 0x1B0),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "交给了胡安事务长。\x02",
        )
    )


    label("loc_FB4")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_FBE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20D, 3)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1B3, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1014")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_100A")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x1B3, 1)
    SetScenarioFlags(0x20D, 3)

    #A0013
    AnonymousTalk(
        0xFF,
        (
            "把",
            scpstr(SCPSTR_CODE_ITEM, 0x1B3),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "交给了胡安事务长。\x02",
        )
    )


    label("loc_100A")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_1014")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20D, 4)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1B6, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_106A")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1060")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x1B6, 1)
    SetScenarioFlags(0x20D, 4)

    #A0014
    AnonymousTalk(
        0xFF,
        (
            "把",
            scpstr(SCPSTR_CODE_ITEM, 0x1B6),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "交给了胡安事务长。\x02",
        )
    )


    label("loc_1060")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_106A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20D, 5)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1B9, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_10C0")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10B6")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x1B9, 1)
    SetScenarioFlags(0x20D, 5)

    #A0015
    AnonymousTalk(
        0xFF,
        (
            "把",
            scpstr(SCPSTR_CODE_ITEM, 0x1B9),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "交给了胡安事务长。\x02",
        )
    )


    label("loc_10B6")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_10C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20D, 6)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1BC, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1116")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_110C")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x1BC, 1)
    SetScenarioFlags(0x20D, 6)

    #A0016
    AnonymousTalk(
        0xFF,
        (
            "把",
            scpstr(SCPSTR_CODE_ITEM, 0x1BC),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "交给了胡安事务长。\x02",
        )
    )


    label("loc_110C")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_1116")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20D, 7)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1BF, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_116C")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1162")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x1BF, 1)
    SetScenarioFlags(0x20D, 7)

    #A0017
    AnonymousTalk(
        0xFF,
        (
            "把",
            scpstr(SCPSTR_CODE_ITEM, 0x1BF),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "交给了胡安事务长。\x02",
        )
    )


    label("loc_1162")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_116C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20E, 0)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1C2, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_11C2")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11B8")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x1C2, 1)
    SetScenarioFlags(0x20E, 0)

    #A0018
    AnonymousTalk(
        0xFF,
        (
            "把",
            scpstr(SCPSTR_CODE_ITEM, 0x1C2),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "交给了胡安事务长。\x02",
        )
    )


    label("loc_11B8")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_11C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20E, 1)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1C5, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1218")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_120E")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x1C5, 1)
    SetScenarioFlags(0x20E, 1)

    #A0019
    AnonymousTalk(
        0xFF,
        (
            "把",
            scpstr(SCPSTR_CODE_ITEM, 0x1C5),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "交给了胡安事务长。\x02",
        )
    )


    label("loc_120E")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_1218")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20E, 2)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1C8, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_126E")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1264")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x1C8, 1)
    SetScenarioFlags(0x20E, 2)

    #A0020
    AnonymousTalk(
        0xFF,
        (
            "把",
            scpstr(SCPSTR_CODE_ITEM, 0x1C8),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "交给了胡安事务长。\x02",
        )
    )


    label("loc_1264")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_126E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20E, 3)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1CB, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_12C4")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12BA")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x1CB, 1)
    SetScenarioFlags(0x20E, 3)

    #A0021
    AnonymousTalk(
        0xFF,
        (
            "把",
            scpstr(SCPSTR_CODE_ITEM, 0x1CB),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "交给了胡安事务长。\x02",
        )
    )


    label("loc_12BA")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_12C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20E, 4)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1CE, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_131A")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1310")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x1CE, 1)
    SetScenarioFlags(0x20E, 4)

    #A0022
    AnonymousTalk(
        0xFF,
        (
            "把",
            scpstr(SCPSTR_CODE_ITEM, 0x1CE),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "交给了胡安事务长。\x02",
        )
    )


    label("loc_1310")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_131A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20E, 5)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1D1, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1370")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1366")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x1D1, 1)
    SetScenarioFlags(0x20E, 5)

    #A0023
    AnonymousTalk(
        0xFF,
        (
            "把",
            scpstr(SCPSTR_CODE_ITEM, 0x1D1),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "交给了胡安事务长。\x02",
        )
    )


    label("loc_1366")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_1370")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20E, 6)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1D4, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_13C6")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13BC")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x1D4, 1)
    SetScenarioFlags(0x20E, 6)

    #A0024
    AnonymousTalk(
        0xFF,
        (
            "把",
            scpstr(SCPSTR_CODE_ITEM, 0x1D4),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "交给了胡安事务长。\x02",
        )
    )


    label("loc_13BC")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_13C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20E, 7)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1D7, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_141C")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1412")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x1D7, 1)
    SetScenarioFlags(0x20E, 7)

    #A0025
    AnonymousTalk(
        0xFF,
        (
            "把",
            scpstr(SCPSTR_CODE_ITEM, 0x1D7),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "交给了胡安事务长。\x02",
        )
    )


    label("loc_1412")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_141C")

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Call(0, 6)
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1682")
    FadeToBright(300, 0)
    OP_0D()

    #C0026
    ChrTalk(
        0x8,
        (
            "啊，你们已经\x01",
            "给了我很多\x01",
            "『古怪的料理』了。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x8,
        (
            "这样一来，足够鉴定班\x01",
            "维持一段时间的研究了。\x01",
            "……谢谢你们，真是帮了大忙。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x101,
        (
            "#00000F哈哈，请不要客气，\x01",
            "这又不是什么贵重之物……\x02\x03",

            "而且我原本就很想\x01",
            "为母校尽一份力。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x8,
        (
            "罗伊德，你真是个好孩子……\x01",
            "和学生时代\x01",
            "一模一样呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x8,
        (
            "对了，\x01",
            "你们把这个拿去吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x8,
        (
            "这是我们在最近的研修中\x01",
            "开始使用的艾尼格玛Ⅱ的回路，\x01",
            "手头正好多了一个备用品。\x02",
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
            "收下了。\x02",
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
            "#00000F非常感谢您，\x01",
            "胡安事务长。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x8,
        (
            "不用客气，我才应该感谢你们呢。\x01",
            "今后要是再有什么事，就拜托你们了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x20F, 1)
    TalkEnd(0x8)
    Return()

    label("loc_1682")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_168C")

    Jump("loc_673")

    label("loc_1691")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_169B")

    Jump("loc_5DF")

    label("loc_16A0")

    Jump("loc_16B2")

    label("loc_16A5")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 5)

    label("loc_16B2")

    TalkEnd(0x8)
    Return()

    # Function_4_5AD end

    def Function_5_16B6(): pass

    label("Function_5_16B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_17DD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1772")

    #C0035
    ChrTalk(
        0x8,
        (
            "得到总统被拘捕的\x01",
            "消息后，国防军\x01",
            "迅速撤退了。\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x8,
        (
            "为了稳定各地的混乱局势，\x01",
            "国防军必须得好好\x01",
            "发挥作用才行啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x8,
        (
            "我们也必须要全力做好\x01",
            "自己所能做到的事情。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_17D8")

    label("loc_1772")


    #C0038
    ChrTalk(
        0x8,
        (
            "总部派遣过来的支援部队\x01",
            "正在处理这一带的混乱局面。\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x8,
        (
            "我们也必须要全力做好\x01",
            "自己所能做到的事情。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17D8")

    Jump("loc_28D8")

    label("loc_17DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1928")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18A2")

    #C0040
    ChrTalk(
        0x8,
        (
            "……那起袭击事件真是\x01",
            "造成了极为凄惨的后果。\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x8,
        (
            "这所警察学校和年轻的\x01",
            "警察们能够平安无事，\x01",
            "可谓不幸中的万幸……\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x8,
        (
            "但克洛斯贝尔要想完全恢复，\x01",
            "恐怕要花费不少时间。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1923")

    label("loc_18A2")


    #C0043
    ChrTalk(
        0x8,
        (
            "……在那起袭击事件中，\x01",
            "年轻的警察们能够平安无事，\x01",
            "可谓不幸中的万幸……\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x8,
        (
            "但克洛斯贝尔要想完全恢复，\x01",
            "恐怕要花费不少时间。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1923")

    Jump("loc_28D8")

    label("loc_1928")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1A47")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19D5")

    #C0045
    ChrTalk(
        0x8,
        (
            "大门在昨天被毁坏了，\x01",
            "要想换上一扇新的，\x01",
            "似乎需要一些时间。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x8,
        (
            "真没想到，竟然能\x01",
            "破坏成那样……\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x8,
        (
            "这段时间就只能拜托\x01",
            "警备队来负责警备了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1A42")

    label("loc_19D5")


    #C0048
    ChrTalk(
        0x8,
        (
            "大门在昨天被毁坏了，\x01",
            "要想换上一扇新的，\x01",
            "似乎需要一些时间。\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x8,
        (
            "这段时间就只能拜托\x01",
            "警备队来负责警备了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A42")

    Jump("loc_28D8")

    label("loc_1A47")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x163, 2)), scpexpr(EXPR_END)), "loc_1C7C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x170, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C29")

    #C0050
    ChrTalk(
        0x8,
        "啊，罗伊德，是你们啊。\x02",
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x8,
        (
            "外面刚才传来了\x01",
            "一声巨响……\x01",
            "到底是怎么回事？\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x101,
        (
            "#00000F……森林道入口处的大门\x01",
            "刚才被破坏了，我想您听到的\x01",
            "应该就是那时的声响。\x02",
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
            "你、你说什么！？\x01",
            "那扇用特殊合金制造的大门竟然会被……\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x8,
        (
            "难道是『幻兽』所为吗……？\x01",
            "但报告上从没提过\x01",
            "他们有那么大的力量啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x103,
        (
            "#00200F我们目前还无法\x01",
            "提供任何情报……\x02\x03",

            "另外，对方并不是没有\x01",
            "闯入这里的可能。\x01",
            "……请全力保持警戒。\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x8,
        "好、好的……你们也要小心。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x170, 0)
    Jump("loc_1C77")

    label("loc_1C29")


    #C0057
    ChrTalk(
        0x8,
        (
            "我们会用心安排\x01",
            "周边地带的警备工作。\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x8,
        (
            "你们几个……\x01",
            "可千万要注意安全。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C77")

    Jump("loc_28D8")

    label("loc_1C7C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1CE6")

    #C0059
    ChrTalk(
        0x8,
        (
            "森林地带今天没有任何\x01",
            "关于幻兽的目击情报。\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x8,
        (
            "游击士们今天好像已经去调查\x01",
            "别的地方了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28D8")

    label("loc_1CE6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1E52")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1DC7")

    #C0061
    ChrTalk(
        0x8,
        (
            "之前有人在诺克斯\x01",
            "森林地带目击到了\x01",
            "那个所谓的『幻兽』。\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x8,
        (
            "游击士协会的林和\x01",
            "艾欧莉娅前去消灭它，\x01",
            "可最后却没能成功。\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x8,
        (
            "那里毕竟是警备队的演习场，\x01",
            "考虑到今后的情况，\x01",
            "还是要继续加强警戒才行。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1E4D")

    label("loc_1DC7")


    #C0064
    ChrTalk(
        0x8,
        (
            "之前有人在诺克斯\x01",
            "森林地带目击到了\x01",
            "那个所谓的『幻兽』。\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x8,
        (
            "但最后还是让它逃走了……\x01",
            "考虑到今后的情况，\x01",
            "还是要继续加强警戒才行。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E4D")

    Jump("loc_28D8")

    label("loc_1E52")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1FC7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F5C")

    #C0066
    ChrTalk(
        0x8,
        (
            "警察学校的教育课程\x01",
            "浓缩在半年的时间里。\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x8,
        (
            "教育课程以讲座和训练为主。\x01",
            "学员毕业之后，我们会根据其自身特点，\x01",
            "把他们分配到相应的部门。\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x8,
        (
            "也就是说，这里是教导雏鸟警察们\x01",
            "如何展翅飞翔的地方……\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x8,
        (
            "能够在这里工作，\x01",
            "我由衷地感到骄傲。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1FC2")

    label("loc_1F5C")


    #C0070
    ChrTalk(
        0x8,
        (
            "这里就是教导雏鸟警察们\x01",
            "如何展翅飞翔的地方……\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x8,
        (
            "能够在这所警察学校里任职，\x01",
            "我由衷地感到骄傲。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1FC2")

    Jump("loc_28D8")

    label("loc_1FC7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_23CC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14F, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2330")

    #C0072
    ChrTalk(
        0x8,
        (
            "如今已经成为警备队副司令的道格拉斯，\x01",
            "曾在这里担任过一段时间的教官。\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0x8,
        (
            "他主要负责训练方面的课程，\x01",
            "时常会到演习场露面。\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x101,
        (
            "#00000F哈哈……\x01",
            "他真是个非常严格的人呢。\x02\x03",

            "#00008F学员们承受不住高强度的训练，\x01",
            "一个接一个地掉队……\x02\x03",

            "#00006F现在回想一下当时那种地狱般的场面，\x01",
            "仍会忍不住颤抖呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0x104,
        (
            "#00306F唉，那位老兄一向如此，\x01",
            "一边爽朗地笑着，\x01",
            "一边提出各种无理要求。\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x105,
        (
            "#10302F呵呵，这就是他被称作\x01",
            "『鬼之道格拉斯』的原因吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0x109,
        (
            "#10100F不过，能从『警备队的希望』\x01",
            "身上学到各种战斗技术，\x01",
            "真是让人羡慕。\x02\x03",

            "#10104F如果可能，我很希望在新人时代\x01",
            "接受他的教导呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0x101,
        (
            "#00009F是、是啊，其实我很感谢他。\x01",
            "他所教导的战斗要点在实战中\x01",
            "多次派上了用场。\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0x8,
        (
            "包括罗伊德在内，\x01",
            "很多优秀的警察都是\x01",
            "在他的教导下成才的。\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0x8,
        (
            "站在警察学校的立场来看，\x01",
            "实在是不想失去这样的人才……\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0x8,
        (
            "不过，他毕竟是出身于警备队的人。\x01",
            "既然索妮亚司令提出了请求，\x01",
            "我们也只能放手了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x14F, 6)
    Jump("loc_23C7")

    label("loc_2330")


    #C0082
    ChrTalk(
        0x8,
        (
            "站在警察学校的立场来看，\x01",
            "实在是不想失去道格拉斯这样的人才……\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x8,
        (
            "不过，他毕竟是出身于警备队的人。\x01",
            "既然索妮亚司令提出了请求，\x01",
            "我们也只能放手了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_23C7")

    Jump("loc_28D8")

    label("loc_23CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2690")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14F, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2621")

    #C0084
    ChrTalk(
        0x8,
        "哎呀，这不是特别任务支援科的各位吗。\x02",
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0x8,
        (
            "我听赛尔盖说了，\x01",
            "你们每天都开着那辆\x01",
            "新型导力车外出吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x101,
        (
            "#00000F哈哈，是啊。\x01",
            "那辆导力车给我们的市外活动\x01",
            "提供了许多帮助。\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x8,
        (
            "要记得遵守交通规则，\x01",
            "安全驾驶啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0x8,
        (
            "如果警察引起交通事故……\x01",
            "可就成了让人完全笑不出的笑话了。\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0x105,
        "#10300F呵呵，听到了吗？\x02",
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x109,
        (
            "#10105F我、我怎么可能\x01",
            "会出事故……！\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x104,
        (
            "#00300F诺艾尔确实\x01",
            "算不上所谓的\x01",
            "速度狂……\x02\x03",

            "#00304F但太过喜爱导力车，\x01",
            "说不定会导致自己的视野\x01",
            "变得狭窄哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0x109,
        "#10106F连、连前辈都这么说……\x02",
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x102,
        (
            "#00100F反正我们现在还没有\x01",
            "完全习惯开车工作……\x01",
            "大家就把这个忠告牢记在心吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x14F, 5)
    Jump("loc_268B")

    label("loc_2621")


    #C0094
    ChrTalk(
        0x8,
        (
            "开车的时候，\x01",
            "一定要严格遵守交通规则。\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0x8,
        (
            "如果警察引起交通事故……\x01",
            "可就成了让人完全笑不出的笑话了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_268B")

    Jump("loc_28D8")

    label("loc_2690")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_28D8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x139, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_288A")

    #C0096
    ChrTalk(
        0x8,
        "诸位，看来讲座已经结束了啊。\x02",
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0x8,
        "接下来就要实际操作了吗？\x02",
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x101,
        "#00000F哈哈，是的。\x02",
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0x105,
        (
            "#10304F话说回来，那位科长\x01",
            "竟然能给人开办讲座，\x01",
            "真是让人意外。\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0x8,
        (
            "他曾在警察学校\x01",
            "兼任过车辆驾驶的\x01",
            "教官呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0x8,
        (
            "呵呵，怎么样，他的讲座\x01",
            "非常通俗易懂吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x102,
        (
            "#00105F啊，说起来，\x01",
            "之前也听科长提到过这件事。\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0x109,
        (
            "#10104F嗯……看来赛尔盖科长\x01",
            "也有很多不为人知的往事呢。\x02\x03",

            "#10101F我个人还是比较在意他和索妮亚司令\x01",
            "之间的关系……\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0x101,
        (
            "#00003F嗯，他很少谈起自己的事情，\x01",
            "这反而会让人更感兴趣……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x139, 5)
    Jump("loc_28D8")

    label("loc_288A")


    #C0105
    ChrTalk(
        0x8,
        (
            "话说回来，赛尔盖\x01",
            "正在外面等你们吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0x8,
        (
            "别让上司等得太久，\x01",
            "快点过去吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_28D8")

    Call(0, 8)
    Return()

    # Function_5_16B6 end

    def Function_6_28DC(): pass

    label("Function_6_28DC")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20C, 0)), scpexpr(EXPR_END)), "loc_28F9")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_28F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20C, 1)), scpexpr(EXPR_END)), "loc_290C")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_290C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20C, 2)), scpexpr(EXPR_END)), "loc_291F")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_291F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20C, 3)), scpexpr(EXPR_END)), "loc_2932")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2932")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20C, 4)), scpexpr(EXPR_END)), "loc_2945")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2945")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20C, 5)), scpexpr(EXPR_END)), "loc_2958")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2958")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20C, 6)), scpexpr(EXPR_END)), "loc_296B")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_296B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20C, 7)), scpexpr(EXPR_END)), "loc_297E")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_297E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20D, 0)), scpexpr(EXPR_END)), "loc_2991")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2991")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20D, 1)), scpexpr(EXPR_END)), "loc_29A4")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_29A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20D, 2)), scpexpr(EXPR_END)), "loc_29B7")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_29B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20D, 3)), scpexpr(EXPR_END)), "loc_29CA")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_29CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20D, 4)), scpexpr(EXPR_END)), "loc_29DD")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_29DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20D, 5)), scpexpr(EXPR_END)), "loc_29F0")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_29F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20D, 6)), scpexpr(EXPR_END)), "loc_2A03")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2A03")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20D, 7)), scpexpr(EXPR_END)), "loc_2A16")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2A16")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20E, 0)), scpexpr(EXPR_END)), "loc_2A29")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2A29")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20E, 1)), scpexpr(EXPR_END)), "loc_2A3C")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2A3C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20E, 2)), scpexpr(EXPR_END)), "loc_2A4F")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2A4F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20E, 3)), scpexpr(EXPR_END)), "loc_2A62")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2A62")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20E, 4)), scpexpr(EXPR_END)), "loc_2A75")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2A75")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20E, 5)), scpexpr(EXPR_END)), "loc_2A88")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2A88")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20E, 6)), scpexpr(EXPR_END)), "loc_2A9B")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2A9B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20E, 7)), scpexpr(EXPR_END)), "loc_2AAE")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2AAE")

    Return()

    # Function_6_28DC end

    def Function_7_2AAF(): pass

    label("Function_7_2AAF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2AC2")
    MenuCmd(3, 1, 0x0)

    label("loc_2AC2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2AD5")
    MenuCmd(3, 1, 0x1)

    label("loc_2AD5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2AE8")
    MenuCmd(3, 1, 0x2)

    label("loc_2AE8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2AFB")
    MenuCmd(3, 1, 0x3)

    label("loc_2AFB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B0E")
    MenuCmd(3, 1, 0x4)

    label("loc_2B0E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B21")
    MenuCmd(3, 1, 0x5)

    label("loc_2B21")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B34")
    MenuCmd(3, 1, 0x6)

    label("loc_2B34")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B47")
    MenuCmd(3, 1, 0x7)

    label("loc_2B47")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B5A")
    MenuCmd(3, 1, 0x8)

    label("loc_2B5A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B6D")
    MenuCmd(3, 1, 0x9)

    label("loc_2B6D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B80")
    MenuCmd(3, 1, 0xA)

    label("loc_2B80")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B93")
    MenuCmd(3, 1, 0xB)

    label("loc_2B93")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2BA6")
    MenuCmd(3, 1, 0xC)

    label("loc_2BA6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2BB9")
    MenuCmd(3, 1, 0xD)

    label("loc_2BB9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2BCC")
    MenuCmd(3, 1, 0xE)

    label("loc_2BCC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2BDF")
    MenuCmd(3, 1, 0xF)

    label("loc_2BDF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2BF2")
    MenuCmd(3, 1, 0x10)

    label("loc_2BF2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x11), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C05")
    MenuCmd(3, 1, 0x11)

    label("loc_2C05")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x12), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C18")
    MenuCmd(3, 1, 0x12)

    label("loc_2C18")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x13), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C2B")
    MenuCmd(3, 1, 0x13)

    label("loc_2C2B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C3E")
    MenuCmd(3, 1, 0x14)

    label("loc_2C3E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x15), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C51")
    MenuCmd(3, 1, 0x15)

    label("loc_2C51")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x16), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C64")
    MenuCmd(3, 1, 0x16)

    label("loc_2C64")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x17), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C77")
    MenuCmd(3, 1, 0x17)

    label("loc_2C77")

    Return()

    # Function_7_2AAF end

    def Function_8_2C78(): pass

    label("Function_8_2C78")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20F, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_31B5")
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0107
    ChrTalk(
        0x8,
        (
            "对了……这个话题也许有些唐突，\x01",
            "请问你们手上有没有\x01",
            "『古怪的料理』？\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0x101,
        "#00005F『古怪的料理』……？\x02",
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0x8,
        (
            "是的，其实我正在寻找能在\x01",
            "鉴定班研修中使用的样本。\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0x8,
        (
            "最好是那种难以推测\x01",
            "其成分的菜式……\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0x101,
        (
            "#00004F原来如此，用于鉴定的样本吗？\x02\x03",

            "#00005F不过……您所说的\x01",
            "古怪的料理，\x01",
            "具体是什么样的呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0x102,
        (
            "#00100F克洛斯贝尔警察局的\x01",
            "鉴定班一向以拥有\x01",
            "高级分析设备而闻名……\x02\x03",

            "#00106F我们毕竟不是什么烹饪专家，\x01",
            "也不知自己能否派上用场。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2EB6")

    #C0113
    ChrTalk(
        0x103,
        (
            "#00200F也不用想太多吧？\x02\x03",

            "#00203F反正平时烹饪的时候，\x01",
            "偶尔也会做出一些\x01",
            "出人意料的菜式。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F84")

    label("loc_2EB6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2F24")

    #C0114
    ChrTalk(
        0x105,
        (
            "#10404F呵呵，不必想太多吧？\x02\x03",

            "#10400F反正平时烹饪的时候，\x01",
            "偶尔也会做出一些\x01",
            "出人意料的东西。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F84")

    label("loc_2F24")


    #C0115
    ChrTalk(
        0x105,
        (
            "#10304F呵呵，不必想太多吧？\x02\x03",

            "#10300F反正平时烹饪的时候，\x01",
            "偶尔也会做出一些\x01",
            "出乎意料的东西。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F84")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2FE8")

    #C0116
    ChrTalk(
        0x109,
        (
            "#10106F说、说的也是……\x01",
            "烹饪时，偶尔会出现一些\x01",
            "类似于化学反应的奇怪变化。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3037")

    label("loc_2FE8")


    #C0117
    ChrTalk(
        0x104,
        (
            "#00306F啊，说的也是啊。\x01",
            "烹饪时，偶尔会出现一些\x01",
            "类似于化学反应的奇怪变化。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3037")


    #C0118
    ChrTalk(
        0x8,
        (
            "哦，看来各位真的能给我\x01",
            "准备那种料理啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0x8,
        "既然如此，那就拜托你们了。\x02",
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0x8,
        (
            "得到那种料理后，\x01",
            "随时都可以\x01",
            "拿到我这里来。\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0x101,
        "#00000F好的，我明白了。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x20F, 0)
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0122
    ChrTalk(
        0x8,
        (
            "对了，\x01",
            "也谈不上是什么谢礼……\x01",
            "就把这本书给你们吧。\x02",
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
            "获得了。\x02",
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
            "空闲时可以靠看书来\x01",
            "扫去平日积累的疲惫哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0x101,
        "#00002F哈哈，谢谢您。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x188, 0)

    label("loc_31B5")

    Return()

    # Function_8_2C78 end

    def Function_9_31B6(): pass

    label("Function_9_31B6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3221")

    #C0126
    ChrTalk(
        0xFE,
        (
            "从好久以前开始，就没有\x01",
            "任何授课和相关训练了。\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0xFE,
        (
            "再这样下去，真的能\x01",
            "成为警察吗……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_35EC")

    label("loc_3221")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_32A1")

    #C0128
    ChrTalk(
        0x9,
        (
            "听说在袭击事件中，犯罪分子往\x01",
            "警察总部里扔了炸弹……\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0x9,
        (
            "（瑟瑟发抖）……好可怕啊。\x01",
            "我果然不该当什么警察……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_35EC")

    label("loc_32A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_32AF")
    Jump("loc_35EC")

    label("loc_32AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x163, 2)), scpexpr(EXPR_END)), "loc_32BD")
    Jump("loc_35EC")

    label("loc_32BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3314")

    #C0130
    ChrTalk(
        0x9,
        "哇～要迟到了～！\x02",
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0x9,
        (
            "今天一大早就有训练……\x01",
            "我大概要被教官怒斥了～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_35EC")

    label("loc_3314")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3322")
    Jump("loc_35EC")

    label("loc_3322")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3330")
    Jump("loc_35EC")

    label("loc_3330")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_333E")
    Jump("loc_35EC")

    label("loc_333E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_35D5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_355F")

    #C0132
    ChrTalk(
        0x9,
        (
            "咦，难道你们就是……\x01",
            "特别任务支援科的成员吗！？\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0x9,
        (
            "我在克洛斯贝尔时代周刊上看了\x01",
            "那篇关于教团事件的报道之后，\x01",
            "就一直很崇拜各位！\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0x9,
        (
            "真希望自己将来也能\x01",
            "进入特别任务支援科工作！\x02",
        )
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0x102,
        "#00100F呵呵，这真是让人高兴。\x02",
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0x105,
        (
            "#10306F真是的，竟然想主动加入\x01",
            "这种充满麻烦的部门，\x01",
            "你还真是个好事者啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0x101,
        (
            "#00006F我说……\x01",
            "主动加入这种部门的人\x01",
            "到底是谁啊？\x02\x03",

            "#00000F咳咳，怎么说呢。\x01",
            "最后会根据学员的实际情况来分配岗位，\x01",
            "无法自主选择……\x02\x03",

            "#00002F要是你将来真的分配到支援科，\x01",
            "到时就请多多指教了。\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0x9,
        "好的！！我一定会努力的！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_35D0")

    label("loc_355F")


    #C0139
    ChrTalk(
        0x9,
        (
            "这次见到诸位，\x01",
            "让我一下就充满了干劲！\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0x9,
        (
            "虽然不知道自己今后能否\x01",
            "加入特别任务支援科……\x01",
            "但我一定会努力的！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_35D0")

    Jump("loc_35EC")

    label("loc_35D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 6)), scpexpr(EXPR_END)), "loc_35E3")
    Jump("loc_35EC")

    label("loc_35E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_35EC")

    label("loc_35EC")

    TalkEnd(0xFE)
    Return()

    # Function_9_31B6 end

    def Function_10_35F0(): pass

    label("Function_10_35F0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_365D")

    #C0141
    ChrTalk(
        0xFE,
        (
            "说起来，我好久没有\x01",
            "回过家了……\x02",
        )
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0xFE,
        (
            "既然结界已经消失了，\x01",
            "我还是找个时间回去看看吧……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3861")

    label("loc_365D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_36CD")

    #C0143
    ChrTalk(
        0xA,
        (
            "我们好不容易才坚持学习了\x01",
            "这么久的教育课程。\x02",
        )
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0xA,
        (
            "为了早日成为前辈们的助力，\x01",
            "一起继续努力吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3861")

    label("loc_36CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_36DB")
    Jump("loc_3861")

    label("loc_36DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x163, 2)), scpexpr(EXPR_END)), "loc_371B")

    #C0145
    ChrTalk(
        0xA,
        (
            "听说发生了\x01",
            "列车事故……\x01",
            "现在的情况怎么样了？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3861")

    label("loc_371B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_3729")
    Jump("loc_3861")

    label("loc_3729")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_37A9")

    #C0146
    ChrTalk(
        0xA,
        (
            "关于这次的独立提案，我们这些\x01",
            "训练生也觉得非常有意义。\x02",
        )
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0xA,
        (
            "为了警察组织今后的发展，\x01",
            "真希望独立能成功实现啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3861")

    label("loc_37A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_37B7")
    Jump("loc_3861")

    label("loc_37B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_383C")

    #C0148
    ChrTalk(
        0xA,
        (
            "今天将会在这个会议室举行\x01",
            "一场关于自治州法的讲座。\x02",
        )
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0xA,
        (
            "对警察来说，法律是与\x01",
            "工作息息相关的，\x01",
            "必须要认真学习才行。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3861")

    label("loc_383C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_384A")
    Jump("loc_3861")

    label("loc_384A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 6)), scpexpr(EXPR_END)), "loc_3858")
    Jump("loc_3861")

    label("loc_3858")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_3861")

    label("loc_3861")

    TalkEnd(0xFE)
    Return()

    # Function_10_35F0 end

    def Function_11_3865(): pass

    label("Function_11_3865")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3876")
    Jump("loc_3C6D")

    label("loc_3876")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_39EF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_393E")

    #C0150
    ChrTalk(
        0xB,
        (
            "训练生们在得知昨天发生的列车\x01",
            "事故之后，也开始吵嚷起来了。\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0xB,
        (
            "但现在的他们就算展开行动，\x01",
            "对事情也起不到任何作用。\x02",
        )
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0xB,
        (
            "必须好好劝戒他们，\x01",
            "让他们把注意力集中在课程上。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_39EA")

    label("loc_393E")


    #C0153
    ChrTalk(
        0xB,
        (
            "那些训练生现在就算展开行动，\x01",
            "对昨天发生的那起列车事故\x01",
            "也不会起到任何作用。\x02",
        )
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0xB,
        (
            "现在必须让他们集中精神听课，\x01",
            "只有这样，他们将来才能成长为\x01",
            "可以应对各种事件的优秀人才。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_39EA")

    Jump("loc_3C6D")

    label("loc_39EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x163, 2)), scpexpr(EXPR_END)), "loc_39FD")
    Jump("loc_3C6D")

    label("loc_39FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_3A0B")
    Jump("loc_3C6D")

    label("loc_3A0B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3A19")
    Jump("loc_3C6D")

    label("loc_3A19")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3BBB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B14")

    #C0155
    ChrTalk(
        0xB,
        (
            "最近这段时间，\x01",
            "训练生们对待课程的态度\x01",
            "比以前更加积极了。\x02",
        )
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0xB,
        (
            "以警察为中心的队伍解决了\x01",
            "教团事件那样的重大事件，\x01",
            "想必给他们带来了正面的影响。\x02",
        )
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0xB,
        (
            "为了这群尚未谋面的后辈，\x01",
            "真希望各位现任警官能\x01",
            "更加努力，成为他们的榜样。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3BB6")

    label("loc_3B14")


    #C0158
    ChrTalk(
        0xB,
        (
            "以警察为中心的队伍解决了\x01",
            "教团事件那样的重大事件，\x01",
            "给训练生们带来了正面的影响。\x02",
        )
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0xB,
        (
            "为了这群尚未谋面的后辈，\x01",
            "真希望各位现任警官能\x01",
            "更加努力，成为他们的榜样。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3BB6")

    Jump("loc_3C6D")

    label("loc_3BBB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3BC9")
    Jump("loc_3C6D")

    label("loc_3BC9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3BD7")
    Jump("loc_3C6D")

    label("loc_3BD7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 6)), scpexpr(EXPR_END)), "loc_3C64")

    #C0160
    ChrTalk(
        0xB,
        (
            "警备队的队员们今天也在\x01",
            "努力进行生存训练。\x02",
        )
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0xB,
        (
            "我刚才去看了一下情况，\x01",
            "他们好像已经恢复得差不多了。\x01",
            "哎呀，这可真是太好了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C6D")

    label("loc_3C64")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_3C6D")

    label("loc_3C6D")

    TalkEnd(0xFE)
    Return()

    # Function_11_3865 end

    def Function_12_3C71(): pass

    label("Function_12_3C71")

    Call(0, 13)
    Return()

    # Function_12_3C71 end

    def Function_13_3C75(): pass

    label("Function_13_3C75")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18F, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3FAF")

    #C0162
    ChrTalk(
        0xC,
        "各位辛苦了。\x02",
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0xC,
        (
            "非常感谢你们\x01",
            "今天特地\x01",
            "前来这里。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18F, 4)), scpexpr(EXPR_END)), "loc_3D0D")

    #C0164
    ChrTalk(
        0x101,
        (
            "#00000F不用客气……\x02\x03",

            "#00003F听说相关业务暂时\x01",
            "会转移在这里办理？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3D52")

    label("loc_3D0D")


    #C0165
    ChrTalk(
        0x101,
        (
            "#00000F不用客气……\x02\x03",

            "#00003F瑞贝卡小姐，\x01",
            "你到警察学校这边了啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3D52")


    #C0166
    ChrTalk(
        0xC,
        (
            "是的，警察总部\x01",
            "暂时还无法恢复\x01",
            "接待工作。\x02",
        )
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0xC,
        (
            "不过，所幸\x01",
            "这里的终端中\x01",
            "存有备份数据。\x02",
        )
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0xC,
        (
            "所以我们利用这些备份数据，\x01",
            "重新开始了业务。\x02",
        )
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0xC,
        (
            "各位如果有什么需要，\x01",
            "随时都可以来这里找我。\x02",
        )
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0x102,
        "#00100F这样啊，我明白了。\x02",
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0x109,
        (
            "#10100F……瑞贝卡小姐。\x02\x03",

            "#10104F芙兰醒来时，\x01",
            "你第一时间赶去探望她，\x01",
            "真是非常感谢。\x02\x03",

            "#10109F那孩子也很高兴呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xC, 0x109, 500)

    #C0172
    ChrTalk(
        0xC,
        "哪里，这没什么……\x02",
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0xC,
        (
            "我原本应该鼓励她，\x01",
            "让她打起精神，\x01",
            "结果却反被她鼓舞了……\x02",
        )
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0xC,
        (
            "不管怎样，她能够醒过来，\x01",
            "真的是太好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0x109,
        (
            "#10104F是啊，真是太好了。\x02\x03",

            "#10100F如果方便，\x01",
            "您以后可以再抽时间去看看她吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0xC,
        "好的，当然没问题。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x18F, 5)
    TalkEnd(0xC)
    Return()

    label("loc_3FAF")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x334, 0x0)"), scpexpr(EXPR_END)), "loc_428C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12B, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_428C")
    OP_63(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0177
    ChrTalk(
        0xC,
        (
            "啊，各位身上\x01",
            "带着的……\x02",
        )
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0xC,
        (
            "莫非是\x01",
            "『结晶碎片』吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0x101,
        (
            "#00005F哎，是指这个吗？\x02\x03",

            "#00000F这是之前无意中得到的，\x01",
            "但一直不知道\x01",
            "有什么用处……\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    #A0180
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "罗伊德将结晶碎片\x01",
            "交给瑞贝卡查看。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0181
    ChrTalk(
        0xC,
        "嗯，果然没错……！\x02",
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0xC,
        (
            "这正是鉴定科的人正在寻找的\x01",
            "结晶碎片，可以用来修复\x01",
            "破损的记录结晶。\x02",
        )
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0xC,
        (
            "只要有它，\x01",
            "应该就可以解析教团终端\x01",
            "中的一部分情报了。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_415E")
    OP_63(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)

    label("loc_415E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4187")
    OP_63(0x1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)

    label("loc_4187")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_41B0")
    OP_63(0x2, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)

    label("loc_41B0")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_41D6")
    OP_63(0x3, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    label("loc_41D6")

    Sleep(1000)

    #C0184
    ChrTalk(
        0x102,
        (
            "#00105F这、这就是说……\x01",
            "可以查阅约亚西姆·琼塔\x01",
            "隐藏起来的文章了……！？\x02",
        )
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0xC,
        (
            "嗯，虽然只是\x01",
            "一部分而已……\x02",
        )
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0xC,
        (
            "我想马上就能得出结果了，\x01",
            "要把『结晶碎片』\x01",
            "交给鉴定科吗？\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 16)
    TalkEnd(0xC)
    Return()

    label("loc_428C")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4296")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_43DF")
    FadeToDark(300, 0, 100)
    ClearScenarioFlags(0x0, 5)
    Call(0, 15)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_4306")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "对话\x01",                    # 0
            "出示战斗手册\x01",            # 1
            "确认教团终端的资料\x01",      # 2
            "交付结晶碎片\x01",            # 3
            "放弃\x01",                    # 4
        )
    )

    MenuEnd(0x0)
    Jump("loc_4355")

    label("loc_4306")


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "对话\x01",                    # 0
            "出示战斗手册\x01",            # 1
            "确认教团终端的资料\x01",      # 2
            "放弃\x01",                    # 3
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4355")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4355")

    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4383")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 14)
    Jump("loc_43DA")

    label("loc_4383")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_43A7")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 7)
    Call(0, 23)
    Jump("loc_43DA")

    label("loc_43A7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_43C8")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 17)
    Jump("loc_43DA")

    label("loc_43C8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_43DA")
    Call(0, 16)

    label("loc_43DA")

    Jump("loc_4296")

    label("loc_43DF")

    TalkEnd(0xC)
    OP_93(0xC, 0x5A, 0x0)
    BeginChrThread(0xC, 0, 0, 0)
    Return()

    # Function_13_3C75 end

    def Function_14_43F0(): pass

    label("Function_14_43F0")


    #C0187
    ChrTalk(
        0xC,
        (
            "不管怎样……\x01",
            "芙兰能平安醒过来，\x01",
            "真的是太好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0xC,
        (
            "为了让她打起精神，\x01",
            "我们一定要努力工作才行。\x02",
        )
    )

    CloseMessageWindow()
    Return()

    # Function_14_43F0 end

    def Function_15_4456(): pass

    label("Function_15_4456")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x334, 0x0)"), scpexpr(EXPR_END)), "loc_4464")
    SetScenarioFlags(0x0, 5)

    label("loc_4464")

    Return()

    # Function_15_4456 end

    def Function_16_4465(): pass

    label("Function_16_4465")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12B, 1)), scpexpr(EXPR_END)), "loc_44D7")

    #C0189
    ChrTalk(
        0xC,
        (
            "啊，你们把『结晶碎片』\x01",
            "带来了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0xC,
        (
            "为了解析教团终端中的资料，\x01",
            "可以把『结晶碎片』\x01",
            "交给鉴定科吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_44D7")


    #C0191
    ChrTalk(
        0x101,
        "#00000F嗯，拜托了。\x02",
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0xC,
        "好，请稍等一下。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x12B, 1)
    FadeToDark(1000, 0, -1)
    OP_0D()

    label("loc_4514")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x334, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5E7E")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x334, 0x0)"), scpexpr(EXPR_END)), "loc_5E79")
    OP_D2(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SubItemNumber(0x334, 1)
    SetChrName("")
    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4598")
    Sound(9, 0, 100, 0)

    #A0193
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "第０１情报终端的资料\x01",
            "『关于教团』的第一页已经解析完毕！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_4598")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_45F0")
    Sound(9, 0, 100, 0)

    #A0194
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "第０１情报终端的资料\x01",
            "『关于教团』的第三页已经解析完毕！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_45F0")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4648")
    Sound(9, 0, 100, 0)

    #A0195
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "第０２情报终端的资料\x01",
            "『关于真知』的第一页已经解析完毕！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_4648")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_46A0")
    Sound(9, 0, 100, 0)

    #A0196
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "第０２情报终端的资料\x01",
            "『关于真知』的第二页已经解析完毕！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_46A0")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4DA9")
    Sound(9, 0, 100, 0)

    #A0197
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "第０１情报终端的资料\x01",
            "『关于教团』的第四页已经解析完毕！\x07\x00\x02",
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
            "第０１情报终端的资料\x01",
            "『关于教团』已经全部解析完毕！\x07\x00\x02",
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
            "#5P第０１情报终端的全部资料\x01",
            "已经解析完毕。\x02",
        )
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0xC,
        "#5P要立刻查阅吗？\x02",
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0x101,
        "#12P#00001F嗯，麻烦你了。\x02",
    )

    CloseMessageWindow()
    Sound(72, 0, 100, 0)
    Call(0, 18)

    #C0202
    ChrTalk(
        0xC,
        (
            "#5P……这些资料中\x01",
            "似乎记载了有关教团的\x01",
            "基本概要呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0203
    ChrTalk(
        0xC,
        (
            "#5P否定女神的教义……\x01",
            "真是让人难以置信。\x02",
        )
    )

    CloseMessageWindow()

    #C0204
    ChrTalk(
        0x101,
        (
            "#12P#00003F嗯……\x01",
            "不过，确实与约亚西姆·琼塔\x01",
            "的证言一致。\x02\x03",

            "#00001F另外，『Ｄ』这个字眼……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_49E7")

    #C0205
    ChrTalk(
        0x103,
        (
            "#12P#00203F应该就是指代他们否定女神\x01",
            "而信奉的所谓『真神』吧。\x02\x03",

            "#00201F在Ｄ∴Ｇ教团的名称中，\x01",
            "『Ｇ』是指『真知』，\x01",
            "这是之前就了解的……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_499E")

    #C0206
    ChrTalk(
        0x105,
        (
            "#12P#10403F嗯，这样的话，『Ｄ∴Ｇ』的含义\x01",
            "总算是已经解明了啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_49E2")

    label("loc_499E")


    #C0207
    ChrTalk(
        0x105,
        (
            "#12P#10303F嗯，如此一来，『Ｄ∴Ｇ』的含义\x01",
            "也算是彻底解明了啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_49E2")

    Jump("loc_4AA1")

    label("loc_49E7")


    #C0208
    ChrTalk(
        0x103,
        (
            "#12P#00200F应该就是指代他们否定女神\x01",
            "而信奉的所谓『真神』吧。\x02\x03",

            "#00201F在Ｄ∴Ｇ教团的名称中，\x01",
            "『Ｇ』是指『真知』，\x01",
            "这是之前就了解的……\x02\x03",

            "这样一来，『Ｄ∴Ｇ』的含义\x01",
            "总算是完全解明了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4AA1")


    #C0209
    ChrTalk(
        0x102,
        (
            "#12P#00108F说起来……\x01",
            "约亚西姆医生说过，小琪雅\x01",
            "『将会成为真正的神』吧。\x02\x03",

            "既然如此，『Ｄ』\x01",
            "不就是指代\x01",
            "小琪雅的字眼了吗……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4B83")

    #C0210
    ChrTalk(
        0x109,
        (
            "#12P#10101F约亚西姆·琼塔\x01",
            "究竟了解多少隐情……\x02\x03",

            "……我们目前还无法得知啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4C43")

    label("loc_4B83")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4BF7")

    #C0211
    ChrTalk(
        0x104,
        (
            "#12P#00301F约亚西姆那混帐\x01",
            "到底知道多少隐情……\x02",
        )
    )

    CloseMessageWindow()

    #C0212
    ChrTalk(
        0x109,
        "#12P#10101F……我们目前还无法得知啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_4C43")

    label("loc_4BF7")


    #C0213
    ChrTalk(
        0x104,
        (
            "#12P#00301F约亚西姆那混帐\x01",
            "到底了解多少隐情……\x02\x03",

            "我们目前还无法得知啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4C43")


    #C0214
    ChrTalk(
        0x101,
        (
            "#12P#00001F阿奈斯特先生\x01",
            "似乎也没有从约亚西姆口中\x01",
            "得知一切……\x02\x03",

            "#00003F当时要是能将他顺利逮捕就好了……\x01",
            "现在想想，真是越来越懊恼了啊。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x334, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4D29")

    #C0215
    ChrTalk(
        0xC,
        (
            "#5P……总之，只要继续\x01",
            "解析这些资料，\x01",
            "应该就能了解到各种内情了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4DA9")

    label("loc_4D29")


    #C0216
    ChrTalk(
        0xC,
        (
            "#5P……总之，只要继续\x01",
            "解析这些资料，\x01",
            "应该就能了解到各种内情了。\x02",
        )
    )

    CloseMessageWindow()

    #C0217
    ChrTalk(
        0xC,
        (
            "#5P把剩下的『结晶碎片』\x01",
            "也拿来解析一下吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()

    label("loc_4DA9")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4E01")
    Sound(9, 0, 100, 0)

    #A0218
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "第０２情报终端的资料\x01",
            "『关于真知』的第三页已经解析完毕！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_4E01")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4E59")
    Sound(9, 0, 100, 0)

    #A0219
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "第０３情报终端的资料\x01",
            "『关于圣子』的第一页已经解析完毕！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_4E59")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_560E")
    Sound(9, 0, 100, 0)

    #A0220
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "第０２情报终端的资料\x01",
            "『关于真知』的第四页已经解析完毕！\x07\x00\x02",
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
            "第０２情报终端的资料\x01",
            "『关于真知』已经全部解析完毕！\x07\x00\x02",
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
            "#5P第０２情报终端的全部资料\x01",
            "已经解析完毕。\x02",
        )
    )

    CloseMessageWindow()

    #C0223
    ChrTalk(
        0xC,
        "#5P要立刻查阅吗？\x02",
    )

    CloseMessageWindow()

    #C0224
    ChrTalk(
        0x101,
        "#12P#00001F嗯，麻烦你了。\x02",
    )

    CloseMessageWindow()
    Sound(72, 0, 100, 0)
    Call(0, 19)

    #C0225
    ChrTalk(
        0xC,
        (
            "#5P……在这些资料中，\x01",
            "似乎详细记录了有关那个\x01",
            "『真知』的信息啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0xC,
        (
            "#5P可以提高服用者的身体能力与感应力，\x01",
            "进而引发出潜在能力\x01",
            "的药物……\x02",
        )
    )

    CloseMessageWindow()

    #C0227
    ChrTalk(
        0xC,
        (
            "#5P而且还会造成『魔人化』现象，\x01",
            "真是种充满谜团的药物呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0228
    ChrTalk(
        0x101,
        (
            "#12P#00001F作为其原料而使用，\x01",
            "名为『灵智之草』的植物\x01",
            "广泛生长在湿地一带……\x02\x03",

            "约亚西姆曾经前往那里\x01",
            "采摘材料，\x01",
            "这一点也无需怀疑了。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_51BE")

    #C0229
    ChrTalk(
        0x102,
        (
            "#12P#00101F另外，根据资料中的某一段记录，\x01",
            "『真知』正是让他们信奉的所谓真神……\x02\x03",

            "也就是『Ｄ』复活\x01",
            "所需要的药物呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0230
    ChrTalk(
        0x109,
        (
            "#12P#10108F老实说，听起来\x01",
            "完全就是些荒唐的无稽之谈……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5269")

    label("loc_51BE")


    #C0231
    ChrTalk(
        0x102,
        (
            "#12P#00101F另外，根据资料中的某一段记录，\x01",
            "『真知』正是让他们信奉的所谓真神……\x02\x03",

            "也就是『Ｄ』复活\x01",
            "所需要的药物呢。\x02\x03",

            "#00108F老实说，听起来\x01",
            "完全就是些荒唐的无稽之谈……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5269")


    #C0232
    ChrTalk(
        0x103,
        (
            "#12P#00201F话虽如此，但教团在这五百年间，\x01",
            "一直以『仪式』的形式\x01",
            "进行着『真知』的研究……\x02\x03",

            "#00203F……虽然我幸运地被盖伊先生所救，\x01",
            "不过至今为止，已经有无数人\x01",
            "成为了他们的牺牲品。\x02",
        )
    )

    CloseMessageWindow()

    #C0233
    ChrTalk(
        0x104,
        (
            "#12P#00301F可在他们的眼里，\x01",
            "却仅仅是『这点牺牲』而已……\x02\x03",

            "真是一群无可救药的家伙啊。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5456")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_53D1")

    #C0234
    ChrTalk(
        0x105,
        (
            "#12P#10403F……而且，瓦鲁多最近\x01",
            "也服用了『真知』……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_540B")

    label("loc_53D1")


    #C0235
    ChrTalk(
        0x105,
        (
            "#12P#10303F……而且，瓦鲁多最近\x01",
            "也服用了『真知』呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_540B")


    #C0236
    ChrTalk(
        0x101,
        (
            "#12P#00001F嗯……虽然教团已经不复存在了，\x01",
            "但似乎还是需要注意呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_54C6")

    label("loc_5456")


    #C0237
    ChrTalk(
        0x101,
        (
            "#12P#00003F……而且，瓦鲁多最近\x01",
            "也服用了『真知』。\x02\x03",

            "#00001F虽然教团已经不复存在了，\x01",
            "但似乎还是需要注意呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_54C6")


    #C0238
    ChrTalk(
        0x102,
        (
            "#12P#00101F嗯……确实如此。\x02\x03",

            "不仅是『真知』，\x01",
            "像这样的违禁药物，\x01",
            "我们警察都要严厉取缔才行。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x334, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5588")

    #C0239
    ChrTalk(
        0xC,
        "#5P嗯，的确如此。\x02",
    )

    CloseMessageWindow()

    #C0240
    ChrTalk(
        0xC,
        (
            "#5P……总之，关于『真知』的内容\x01",
            "就只有这些了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_560E")

    label("loc_5588")


    #C0241
    ChrTalk(
        0xC,
        "#5P嗯，的确如此。\x02",
    )

    CloseMessageWindow()

    #C0242
    ChrTalk(
        0xC,
        (
            "#5P……总之，关于『真知』的内容\x01",
            "就只有这些了。\x02",
        )
    )

    CloseMessageWindow()

    #C0243
    ChrTalk(
        0xC,
        (
            "#5P把剩下的『结晶碎片』\x01",
            "也拿来解析一下吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()

    label("loc_560E")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5666")
    Sound(9, 0, 100, 0)

    #A0244
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "第０３情报终端的资料\x01",
            "『关于圣子』的第２页已经解析完毕！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_5666")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5E79")
    Sound(9, 0, 100, 0)

    #A0245
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "第０３情报终端的资料\x01",
            "『关于圣子』的第３页已经解析完毕！\x07\x00\x02",
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
            "第０３情报终端的资料\x01",
            "『关于圣子』已经全部解析完毕！\x07\x00\x02",
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
            "#5P第０３情报终端的全部资料\x01",
            "已经解析完毕。\x02",
        )
    )

    CloseMessageWindow()

    #C0248
    ChrTalk(
        0xC,
        "#5P要立刻查阅吗？\x02",
    )

    CloseMessageWindow()

    #C0249
    ChrTalk(
        0x101,
        "#12P#00001F嗯，麻烦你了。\x02",
    )

    CloseMessageWindow()
    Sound(72, 0, 100, 0)
    Call(0, 20)

    #C0250
    ChrTalk(
        0xC,
        (
            "#5P这些内容……\x01",
            "似乎都和支援科看护的\x01",
            "小琪雅有关……？\x02",
        )
    )

    CloseMessageWindow()

    #C0251
    ChrTalk(
        0x101,
        (
            "#12P#00003F五百年前，库罗伊斯家族\x01",
            "创造了琪雅……\x01",
            "并将她作为信仰对象交给了教团。\x02\x03",

            "此后，她就作为象征着神的『圣子』，\x01",
            "一直沉睡在摇篮之中……\x02",
        )
    )

    CloseMessageWindow()

    #C0252
    ChrTalk(
        0x102,
        (
            "#12P#00101F……即使是教团中的成员，\x01",
            "也不了解其中的真相呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0253
    ChrTalk(
        0x103,
        (
            "#12P#00203F库罗伊斯家族为了达到真正目的，\x01",
            "在暗中诱导着他们。而他们却毫无察觉，\x01",
            "一直都在盲目追寻着虚无缥缈的『真神』……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5989")

    #C0254
    ChrTalk(
        0x106,
        "#12P#10708F……从某种意义上说，也是一群可怜的人呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_5A12")

    label("loc_5989")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_59D7")

    #C0255
    ChrTalk(
        0x109,
        "#12P#10108F……从某种意义上说，也是一群可怜的人啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_5A12")

    label("loc_59D7")


    #C0256
    ChrTalk(
        0x105,
        "#12P#10408F……从某种意义上说，也是一群可怜的家伙呢。\x02",
    )

    CloseMessageWindow()

    label("loc_5A12")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5A6D")

    #C0257
    ChrTalk(
        0x10A,
        (
            "#12P#00603F但只要想想那群家伙做过的事情，\x01",
            "就实在是同情不起来啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5B04")

    label("loc_5A6D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5AC0")

    #C0258
    ChrTalk(
        0x105,
        (
            "#12P#10403F但想想他们的所作所为，\x01",
            "便也没有同情的余地了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5B04")

    label("loc_5AC0")


    #C0259
    ChrTalk(
        0x109,
        (
            "#12P#10103F但只要想想他们做过的事情，\x01",
            "也就没有同情的必要了……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5B04")


    #C0260
    ChrTalk(
        0x101,
        (
            "#12P#00001F教团的成员暂且不说……\x01",
            "琪雅可是没有任何罪过的。\x02\x03",

            "#00003F就算她是库罗伊斯家族为了\x01",
            "达成自己的目的而制造出来的……\x02\x03",

            "就算她拥有\x01",
            "不可思议的能力……\x01",
            "那一切也都与她无关。\x02\x03",

            "在我们的眼前醒来的琪雅，\x01",
            "只是一个有血有肉的普通女孩。\x02\x03",

            "#00001F这样一个普通的孩子，却被独自关在\x01",
            "那种地方长达数百年……\x02\x03",

            "直到现在，她还继续被\x01",
            "玛丽亚贝尔小姐和\x01",
            "伊安律师利用着。\x02",
        )
    )

    CloseMessageWindow()

    #C0261
    ChrTalk(
        0x104,
        (
            "#12P#00301F……无论有任何理由，\x01",
            "我们也绝对不能任由这种事情发生。\x02",
        )
    )

    CloseMessageWindow()

    #C0262
    ChrTalk(
        0xC,
        (
            "#5P……有关教团的资料\x01",
            "已经全部解析完毕了。\x02",
        )
    )

    CloseMessageWindow()

    #C0263
    ChrTalk(
        0xC,
        (
            "#5P我对此次事件的了解\x01",
            "虽然不像各位一样详细……\x02",
        )
    )

    CloseMessageWindow()

    #C0264
    ChrTalk(
        0xC,
        (
            "#5P但琪雅对你们而言\x01",
            "有多么重要，我却有着\x01",
            "深切的体会。\x02",
        )
    )

    CloseMessageWindow()

    #C0265
    ChrTalk(
        0xC,
        (
            "#5P请各位……多加努力。\x01",
            "我也会默默支持你们的。\x02",
        )
    )

    CloseMessageWindow()

    #C0266
    ChrTalk(
        0x101,
        (
            "#12P#00001F谢谢了，瑞贝卡小姐。\x02\x03",

            "我们绝对会凭借自己的双手\x01",
            "把琪雅带回来。\x02\x03",

            "#00007F一定要努力创造出让琪雅……\x01",
            "让我们最疼爱的那个孩子\x01",
            "可以欢笑生活的未来……\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, 2840, 0, 12040, 180)
    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_5E54")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)

    label("loc_5E54")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_5E6D")
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)

    label("loc_5E6D")

    OP_69(0xFF, 0x0)
    OP_E0(0x9, 0x0)
    OP_E0(0x80, 0x0)
    EventEnd(0x5)

    label("loc_5E79")

    Jump("loc_4514")

    label("loc_5E7E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5F6B")
    FadeToBright(1000, 0)
    OP_0D()

    #C0267
    ChrTalk(
        0xC,
        (
            "如果今后取得了新的『结晶碎片』，\x01",
            "请拿到我这里来。\x02",
        )
    )

    CloseMessageWindow()

    #C0268
    ChrTalk(
        0xC,
        (
            "如果想再次查阅已经解析过的资料，\x01",
            "也可以来找我。\x02",
        )
    )

    CloseMessageWindow()

    #C0269
    ChrTalk(
        0x101,
        "#00000F嗯，谢谢啦。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, 2840, 0, 12040, 180)
    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_5F4C")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)

    label("loc_5F4C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_5F65")
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)

    label("loc_5F65")

    OP_69(0xFF, 0x0)
    EventEnd(0x5)

    label("loc_5F6B")

    Return()

    # Function_16_4465 end

    def Function_17_5F6C(): pass

    label("Function_17_5F6C")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5F76")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_605E")
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
            "【关于教团】\x01",      # 0
            "【关于真知】\x01",      # 1
            "【关于圣子】\x01",      # 2
            "【放弃】\x01",          # 3
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
        (0, "loc_6011"),
        (1, "loc_601F"),
        (2, "loc_602D"),
        (3, "loc_603B"),
        (SWITCH_DEFAULT, "loc_604A"),
    )


    label("loc_6011")

    Sound(72, 0, 100, 0)
    Call(0, 18)
    Jump("loc_6059")

    label("loc_601F")

    Sound(72, 0, 100, 0)
    Call(0, 19)
    Jump("loc_6059")

    label("loc_602D")

    Sound(72, 0, 100, 0)
    Call(0, 20)
    Jump("loc_6059")

    label("loc_603B")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6059")

    label("loc_604A")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6059")

    label("loc_6059")

    Jump("loc_5F76")

    label("loc_605E")

    Return()

    # Function_17_5F6C end

    def Function_18_605F(): pass

    label("Function_18_605F")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, 34, -1)
    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_61E6")
    SetChrName("")

    #A0270
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2S『关于教团』\x01\x01",
            "我的名字是约亚西姆·琼塔。\x01",
            "隶属于『Ｄ∴Ｇ教团』的干部祭司。\x01",
            "六年前，在众多势力与游击士共同联手之下，\x01",
            "我们的教团被毁灭了。\x01",
            "但是，唯有我逃了出来，\x01",
            "并来到了这片■■之地。\x01",
            "在伟大的『■』的引导下，\x01",
            "为了完成教团的伟业，我努力坚持了下来。\x01",
            "那一刻终将到来──\x01",
            "为了留下书写新时代圣典所用的资料，\x01",
            "我决定把这些数据保存在各个终端之上。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_6347")

    label("loc_61E6")

    SetChrName("")

    #A0271
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2S『关于教团』\x01\x01",
            "我的名字是约亚西姆·琼塔。\x01",
            "隶属于『Ｄ∴Ｇ教团』的干部祭司。\x01",
            "六年前，在众多势力与游击士共同联手之下，\x01",
            "我们的教团被毁灭了。\x01",
            "但是，唯有我逃了出来，\x01",
            "并来到了这片起源之地。\x01",
            "在伟大的『Ｄ』的引导下，\x01",
            "为了完成教团的伟业，我努力坚持了下来。\x01",
            "那一刻终将到来──\x01",
            "为了留下书写新时代圣典所用的资料，\x01",
            "我决定把这些数据保存在各个终端之上。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_6347")

    SetChrName("")

    #A0272
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2S首先，从我们教团的成立说起吧。\x01",
            "关于这件事，有必要回顾一下\x01",
            "塞姆里亚大陆那段骇人听闻的历史。\x01\x01",
            "经历了大约在一千两百年前发生的\x01",
            "『大崩坏』，大陆失去了高度的文明与秩序，\x01",
            "迎来了被战争与贫困支配的『黑暗时代』。\x01",
            "最终，精疲力尽的人们\x01",
            "犯下了巨大的错误。\x01\x01",
            "被突然出现的愚蠢之人的花言巧语迷惑，\x01",
            "接受了那些人创造的，\x01",
            "毫无道理的秩序。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_660C")
    SetChrName("")

    #A0273
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2S即──愚蠢的■■■■\x01",
            "与象征着其信仰的『■之■■』。\x01",
            "他们创造的秩序使『黑暗时代』终结，\x01",
            "但这种信仰也散播到了大陆各处……\x01\x01",
            "可是，请仔细想一想。\x01",
            "如果『■■』真的存在，\x01",
            "每个人不是应该都能得到平等的救赎吗？\x01",
            "然而，差距这种概念并没有消失，\x01",
            "依然不断有人因为灾难与不幸而丧命。\x01\x01",
            "『■■』在赐予救赎时，难道是有选择性的吗？\x01",
            "这未免也太过愚蠢可笑了吧。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_676F")

    label("loc_660C")

    SetChrName("")

    #A0274
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2S即──愚蠢的七耀教会\x01",
            "与象征着其信仰的『空之女神』。\x01",
            "他们创造的秩序使『黑暗时代』终结，\x01",
            "但这种信仰也散播到了大陆各处……\x01\x01",
            "可是，请仔细想一想。\x01",
            "如果『女神』真的存在，\x01",
            "每个人不是应该都能得到平等的救赎吗？\x01",
            "然而，差距这种概念并没有消失，\x01",
            "依然不断有人因为灾难与不幸而丧命。\x01\x01",
            "『女神』在赐予救赎时，难道是有选择性的吗？\x01",
            "这未免也太过愚蠢可笑了吧。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_676F")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_68C5")
    SetChrName("")

    #A0275
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2S其实，那不过就是■■■■为了得到权势，\x01",
            "而人为创造出来的虚幻存在罢了。\x01",
            "『■■』这种东西，是不可能存在的。\x01\x01",
            "我们那些终于寻得真理的前辈们，\x01",
            "为了与『■■』相遇，踏上了漫长的旅途。\x01\x01",
            "时代不断变迁，当中世纪来临时，\x01",
            "他们终于发现了……\x01",
            "在这地底深处，■■■■■■■■■■\x01",
            "■■■■■■■■……\x01\x01",
            "『■』──便是其名字。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_6A08")

    label("loc_68C5")

    SetChrName("")

    #A0276
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2S其实，那不过就是七耀教会为了得到权势，\x01",
            "而人为创造出来的虚幻存在罢了。\x01",
            "『女神』这种东西，是不可能存在的。\x01\x01",
            "我们那些终于寻得真理的前辈们，\x01",
            "为了与『真神』相遇，踏上了漫长的旅途。\x01\x01",
            "时代不断变迁，当中世纪来临时，\x01",
            "他们终于发现了……\x01",
            "在这地底深处，蕴藏着伟大力量的东西\x01",
            "正在安祥地长眠中……\x01\x01",
            "『Ｄ』──便是其名字。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_6A08")

    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Return()

    # Function_18_605F end

    def Function_19_6A1C(): pass

    label("Function_19_6A1C")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, 34, -1)
    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_6B9B")
    SetChrName("")

    #A0277
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2S『关于真知』\x01\x01",
            "『真知』……是以盛开在\x01",
            "■■■■■的■■■■■■■■\x01",
            "『灵智之草』为原料制成的秘药。\x01\x01",
            "它的调配方法■■■■■■■■■■，\x01",
            "服用之后，可以提高身体能力与感应力，\x01",
            "更拥有激发出人体潜在能力的效果。\x01",
            "■■■■■■■■■■■■■■■■■。\x01",
            "■■■■■■■■■■■■■■■。\x01",
            "『真知』是可以将■■■的■■\x01",
            "■■■『■』的■■的药物。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_6CF4")

    label("loc_6B9B")

    SetChrName("")

    #A0278
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2S『关于真知』\x01\x01",
            "『真知』……是以盛开在\x01",
            "七耀脉之上的传说中的植物——\x01",
            "『灵智之草』为原料而制成的秘药。\x01\x01",
            "它的调配方法与『Ｄ』一同传承下来，\x01",
            "服用之后，可以提高身体能力与感应力，\x01",
            "更拥有激发出人体潜在能力的效果。\x01",
            "不过，那些仅仅是不值一提的辅助作用而已。\x01",
            "此药物的真正力量不止于此。\x01",
            "『真知』是为了将服用者的精神\x01",
            "接续至『Ｄ』的核心的药物。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_6CF4")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_6E4A")
    SetChrName("")

    #A0279
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2S『■』拥有通过将■■■的■■进行■■，\x01",
            "储存■■，并获得■■的性质。\x01",
            "当那■■达到『■■』的境界之时，\x01",
            "『■』就会■■。\x01\x01",
            "另外，『真知』\x01",
            "尚有改良的余地。\x01",
            "■■■■■■■■■■■■■■■，\x01",
            "就可以■■■■■■■■■『■』。\x01\x01",
            "在随后的■■■■，我们教团一直\x01",
            "在对更具效果的『真知』进行研究……\x01",
            "即举行所谓的『仪式』。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_6F8D")

    label("loc_6E4A")

    SetChrName("")

    #A0280
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2S『Ｄ』拥有通过将服用者的精神进行聚合，\x01",
            "储存知识，并获得成长的性质。\x01",
            "当那知识达到『睿智』的境界之时，\x01",
            "『Ｄ』就会复活。\x01\x01",
            "另外，『真知』\x01",
            "尚有改良的余地。\x01",
            "如果能将服用者的能力引发至极限，\x01",
            "就可以将更多的知识贡献给『Ｄ』。\x01\x01",
            "在随后的五百年间，我们教团一直\x01",
            "在对更具效果的『真知』进行研究……\x01",
            "即举行所谓的『仪式』。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_6F8D")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_70CF")
    SetChrName("")

    #A0281
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2S因此，■■■■的■■\x01",
            "■■■■■■■■■■■■■，\x01",
            "虽然『真知』已经接近完成，\x01",
            "但就在只差一步的关头，出现了差错。\x01\x01",
            "由于实验规模太过庞大，\x01",
            "所以被游击士及其它势力所察觉，\x01",
            "各据点，以及整个教团，\x01",
            "因此步入毁灭。\x01\x01",
            "不得不说，这确实太过愚蠢了。\x01",
            "但为了『■■』的■■，\x01",
            "多少有点牺牲也是免不了的……\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_71FE")

    label("loc_70CF")

    SetChrName("")

    #A0282
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2S因此，研究进展的速度\x01",
            "是五百年前起步时无法比拟的，\x01",
            "虽然『真知』已经接近完成，\x01",
            "但就在只差一步的关头，出现了差错。\x01\x01",
            "由于实验规模太过庞大，\x01",
            "所以被游击士及其它势力所察觉，\x01",
            "各据点，以及整个教团，\x01",
            "因此步入毁灭。\x01\x01",
            "不得不说，这确实太过愚蠢了。\x01",
            "但为了『真神』的复活，\x01",
            "多少有点牺牲也是免不了的……\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_71FE")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_736C")
    SetChrName("")

    #A0283
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2S我从已经覆灭的据点中\x01",
            "秘密回收了实验资料，\x01",
            "并来到了克洛斯贝尔这个■■之地。\x01\x01",
            "由于『真知』的材料\x01",
            "『灵智之草』■■生长在■■■■■■■\x01",
            "的■■■■，所以■■\x01",
            "■■■■■并没有任何困难。\x01",
            "此外，在这『太阳堡垒』的深层地带，\x01",
            "有着■■■的■■■■■■的研究设施，\x01",
            "备有众多先进设备。\x01",
            "如此一来，我拥有了完美的研究环境，\x01",
            "最后终于将秘药彻底完成。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_74C7")

    label("loc_736C")

    SetChrName("")

    #A0284
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2S我从已经覆灭的据点中\x01",
            "秘密回收了实验资料，\x01",
            "并来到了克洛斯贝尔这个起源之地。\x01\x01",
            "由于『真知』的材料\x01",
            "『灵智之草』大量生长在克洛斯贝尔南部\x01",
            "的湿地一带，所以采集\x01",
            "材料的工作并没有任何困难。\x01",
            "此外，在这『太阳堡垒』的深层地带，\x01",
            "有着中世纪的炼金术师建造的研究设施，\x01",
            "备有众多先进设备。\x01",
            "如此一来，我拥有了完美的研究环境，\x01",
            "最后终于将秘药彻底完成。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_74C7")

    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Return()

    # Function_19_6A1C end

    def Function_20_74DB(): pass

    label("Function_20_74DB")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, 34, -1)
    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_763C")
    SetChrName("")

    #A0285
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2S『关于圣子』\x01\x01",
            "克洛斯贝尔不仅是我们『Ｄ∴Ｇ教团』\x01",
            "的■■■，而且也是■■■■。\x01",
            "这是■■，■■■■■■■■■■■\x01",
            "■■■『圣子』■。\x01\x01",
            "所谓『圣子』，是『■■』■■■，\x01",
            "■■■■■■『Ｄ∴Ｇ教团』。\x01",
            "■『太阳堡垒』■■■■■■■■，\x01",
            "■■■■■■■■，\x01",
            "■■■■■■■『太阳堡垒』\x01",
            "■■■■■■■■■■■■。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_7777")

    label("loc_763C")

    SetChrName("")

    #A0286
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2S『关于圣子』\x01\x01",
            "克洛斯贝尔不仅是我们『Ｄ∴Ｇ教团』\x01",
            "的根据地，而且也是起源之地。\x01",
            "这是因为，我们就是在此地从始祖处\x01",
            "继承了『圣子』的。\x01\x01",
            "所谓『圣子』，是『真神』的宿主，\x01",
            "也象征着我们『Ｄ∴Ｇ教团』。\x01",
            "在『太阳堡垒』地下沉睡着的圣子，\x01",
            "外表形如人类少女，\x01",
            "五百年间一直在『太阳堡垒』\x01",
            "的祭坛等待着醒来的那一天。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_7777")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_78CD")
    SetChrName("")

    #A0287
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2S■■竟能■■如此■■的■■，\x01",
            "对凡夫俗子而言，也许难以置信吧。\x01\x01",
            "但是，我确实曾经亲眼见证过。\x01",
            "在被称作『■■■■■』的■■之■\x01",
            "■■■■■■■──\x01",
            "那神圣的■■。\x01\x01",
            "『■■■■■』是■■■■■\x01",
            "以■■『古代遗物』的■■■■的■■为基础，\x01",
            "从而■■■■■。\x01",
            "既然如此，这■■■■■■■■■■\x01",
            "也就没什么不可思议的了吧。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_7A12")

    label("loc_78CD")

    SetChrName("")

    #A0288
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2S人类竟能存活如此长久的时间，\x01",
            "对凡夫俗子而言，也许难以置信吧。\x01\x01",
            "但是，我确实曾经亲眼见证过。\x01",
            "在被称作『神圣的摇篮』的球体之中\x01",
            "一直沉睡的少女──\x01",
            "那神圣的姿态。\x01\x01",
            "『神圣的摇篮』是教团的前人们\x01",
            "以研究『古代遗物』的炼金术师的技术为基础，\x01",
            "从而创造出来的。\x01",
            "既然如此，这可以称之为奇迹的现象\x01",
            "也就没什么不可思议的了吧。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_7A12")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_7B4B")
    SetChrName("")

    #A0289
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2S『圣子』从■■■■■■■，\x01",
            "■■『真知』，■■■\x01",
            "■■■■■■■■■。\x01\x01",
            "■■■『■■』■■■，『圣子』■■■■，\x01",
            "■■■■■『■』。\x01",
            "接下来，■■■■的■■与■■\x01",
            "会归集于『■』之下，\x01",
            "人类将从『■■』的咒缚中解放。\x01\x01",
            "那正是我们『Ｄ∴Ｇ教团』的前人们\x01",
            "留下的预言，终将实现的伟大愿望。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_7C71")

    label("loc_7B4B")

    SetChrName("")

    #A0290
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2S『圣子』从诞生的时代开始，\x01",
            "通过『真知』，获取了\x01",
            "可以说是无限的知识。\x01\x01",
            "当达到『睿智』境界时，『圣子』便将苏醒，\x01",
            "并化为真神『Ｄ』。\x01",
            "接下来，全部人类的意志与魂魄\x01",
            "会归集于『Ｄ』之下，\x01",
            "人类将从『女神』的咒缚中解放。\x01\x01",
            "那正是我们『Ｄ∴Ｇ教团』的前人们\x01",
            "留下的预言，终将实现的伟大愿望。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_7C71")

    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Return()

    # Function_20_74DB end

    def Function_21_7C85(): pass

    label("Function_21_7C85")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7CAA")
    SetChrPos(0xFE, 3220, 0, 12810, 0)
    Jump("loc_7D5E")

    label("loc_7CAA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7CCF")
    SetChrPos(0xFE, 2220, 0, 12400, 0)
    Jump("loc_7D5E")

    label("loc_7CCF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7CF4")
    SetChrPos(0xFE, 4050, 0, 12360, 0)
    Jump("loc_7D5E")

    label("loc_7CF4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7D19")
    SetChrPos(0xFE, 3080, 0, 11680, 0)
    Jump("loc_7D5E")

    label("loc_7D19")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7D3E")
    SetChrPos(0xFE, 2430, 0, 10480, 0)
    Jump("loc_7D5E")

    label("loc_7D3E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7D5E")
    SetChrPos(0xFE, 3790, 0, 10440, 0)

    label("loc_7D5E")

    RunExpression(0x4, (scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_21_7C85 end

    def Function_22_7D6D(): pass

    label("Function_22_7D6D")

    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7D8D")
    BeginChrThread(0x101, 1, 0, 21)

    label("loc_7D8D")

    OP_49()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7DA4")
    BeginChrThread(0x102, 1, 0, 21)

    label("loc_7DA4")

    OP_49()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7DBB")
    BeginChrThread(0x103, 1, 0, 21)

    label("loc_7DBB")

    OP_49()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7DD2")
    BeginChrThread(0x104, 1, 0, 21)

    label("loc_7DD2")

    OP_49()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7DE9")
    BeginChrThread(0x109, 1, 0, 21)

    label("loc_7DE9")

    OP_49()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7E00")
    BeginChrThread(0x105, 1, 0, 21)

    label("loc_7E00")

    OP_49()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7E17")
    BeginChrThread(0x106, 1, 0, 21)

    label("loc_7E17")

    OP_49()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7E2E")
    BeginChrThread(0x10A, 1, 0, 21)

    label("loc_7E2E")

    OP_49()
    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_7E48")
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    label("loc_7E48")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_7E61")
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)

    label("loc_7E61")

    Return()

    # Function_22_7D6D end

    def Function_23_7E62(): pass

    label("Function_23_7E62")

    ClearScenarioFlags(0x0, 7)
    ClearScenarioFlags(0x1, 0)
    ClearScenarioFlags(0x1, 1)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7E75")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_8098")
    Jc((scpexpr(EXPR_23, 0x6), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_E4(0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7EB4")
    OP_D2(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x0, 7)
    Jump("loc_8093")

    label("loc_7EB4")

    Jc((scpexpr(EXPR_23, 0x6), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_E4(0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x28), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7EE8")
    OP_D2(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x0, 7)
    Jump("loc_8093")

    label("loc_7EE8")

    Jc((scpexpr(EXPR_23, 0x6), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_E4(0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x46), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7F1C")
    OP_D2(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x0, 7)
    Jump("loc_8093")

    label("loc_7F1C")

    Jc((scpexpr(EXPR_23, 0x6), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_E4(0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7F50")
    OP_D2(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x0, 7)
    Jump("loc_8093")

    label("loc_7F50")

    Jc((scpexpr(EXPR_23, 0x6), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_E4(0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x82), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7F84")
    OP_D2(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x0, 7)
    Jump("loc_8093")

    label("loc_7F84")

    Jc((scpexpr(EXPR_23, 0x6), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_E4(0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0xA0), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7FB8")
    OP_D2(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x0, 7)
    Jump("loc_8093")

    label("loc_7FB8")

    Jc((scpexpr(EXPR_23, 0x6), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_E4(0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0xC8), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7FEC")
    OP_D2(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x0, 7)
    Jump("loc_8093")

    label("loc_7FEC")

    Jc((scpexpr(EXPR_23, 0x6), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_E4(0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0xFA), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8020")
    OP_D2(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x0, 7)
    Jump("loc_8093")

    label("loc_8020")

    Jc((scpexpr(EXPR_23, 0x6), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_E4(0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x118), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8057")
    OP_D2(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x0, 7)
    SetScenarioFlags(0x1, 0)
    Jump("loc_8093")

    label("loc_8057")

    Jc((scpexpr(EXPR_23, 0x6), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_E4(0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x131), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_808E")
    OP_D2(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x0, 7)
    SetScenarioFlags(0x1, 1)
    Jump("loc_8093")

    label("loc_808E")

    Jump("loc_8098")

    label("loc_8093")

    Jump("loc_7E75")

    label("loc_8098")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_88C7")
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
            "啊，各位……\x01",
            "你们的战斗手册内容\x01",
            "似乎有了很多更新呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0292
    ChrTalk(
        0xC,
        (
            "为了协助总部收集魔兽情报，\x01",
            "可以把手册给我检查一下吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0293
    ChrTalk(
        0x101,
        "#12P#0000F嗯，没问题。\x02",
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
            "谢谢，\x01",
            "手册还给你们。\x02",
        )
    )

    CloseMessageWindow()

    #C0295
    ChrTalk(
        0xC,
        (
            "这是这次的奖励津贴，\x01",
            "请收下吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_824F")

    #A0296
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "５００米拉\x07\x00",
            "收下了。\x02",
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
            "1个收下了。\x02",
        )
    )

    AddItemNumber(0x38E, 1)
    Jump("loc_8548")

    label("loc_824F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_82A4")

    #A0298
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "１０００米拉\x07\x00",
            "收下了。\x02",
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
            "2个收下了。\x02",
        )
    )

    AddItemNumber(0x38E, 2)
    Jump("loc_8548")

    label("loc_82A4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_82F9")

    #A0300
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "１５００米拉\x07\x00",
            "收下了。\x02",
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
            "3个收下了。\x02",
        )
    )

    AddItemNumber(0x38E, 3)
    Jump("loc_8548")

    label("loc_82F9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_834E")

    #A0302
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "２０００米拉\x07\x00",
            "收下了。\x02",
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
            "4个收下了。\x02",
        )
    )

    AddItemNumber(0x38E, 4)
    Jump("loc_8548")

    label("loc_834E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_83A3")

    #A0304
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "２５００米拉\x07\x00",
            "收下了。\x02",
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
            "5个收下了。\x02",
        )
    )

    AddItemNumber(0x38E, 5)
    Jump("loc_8548")

    label("loc_83A3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_83F8")

    #A0306
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "３０００米拉\x07\x00",
            "收下了。\x02",
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
            "6个收下了。\x02",
        )
    )

    AddItemNumber(0x38E, 6)
    Jump("loc_8548")

    label("loc_83F8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_844D")

    #A0308
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "３５００米拉\x07\x00",
            "收下了。\x02",
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
            "7个收下了。\x02",
        )
    )

    AddItemNumber(0x38E, 7)
    Jump("loc_8548")

    label("loc_844D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_84A2")

    #A0310
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "４０００米拉\x07\x00",
            "收下了。\x02",
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
            "8个收下了。\x02",
        )
    )

    AddItemNumber(0x38E, 8)
    Jump("loc_8548")

    label("loc_84A2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_84F7")

    #A0312
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "４５００米拉\x07\x00",
            "收下了。\x02",
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
            "9个收下了。\x02",
        )
    )

    AddItemNumber(0x38E, 9)
    Jump("loc_8548")

    label("loc_84F7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8548")

    #A0314
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "５０００米拉\x07\x00",
            "收下了。\x02",
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
            "10个收下了。\x02",
        )
    )

    AddItemNumber(0x38E, 10)

    label("loc_8548")

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_857C")
    Sound(17, 0, 100, 0)

    #A0316
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x395),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "2个收下了。\x02",
        )
    )

    AddItemNumber(0x395, 2)
    CloseMessageWindow()
    Jump("loc_85A7")

    label("loc_857C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_85A7")
    Sound(17, 0, 100, 0)

    #A0317
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x395),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    AddItemNumber(0x395, 1)
    CloseMessageWindow()

    label("loc_85A7")

    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    Jc((scpexpr(EXPR_23, 0x6), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_86C8")

    #C0318
    ChrTalk(
        0xC,
        (
            "如果今后收集到了更多的魔兽情报，\x01",
            "请再拿来给我看哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0319
    ChrTalk(
        0x101,
        "#12P#0000F好的，那到时就麻烦了。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_865E")

    #C0320
    ChrTalk(
        0x102,
        "#12P#0100F下次再来打扰啦。\x02",
    )

    CloseMessageWindow()
    Jump("loc_86C3")

    label("loc_865E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8691")

    #C0321
    ChrTalk(
        0x103,
        "#12P#0200F下次再来打扰。\x02",
    )

    CloseMessageWindow()
    Jump("loc_86C3")

    label("loc_8691")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_86C3")

    #C0322
    ChrTalk(
        0x104,
        "#12P#0300F下次再来打扰你啦。\x02",
    )

    CloseMessageWindow()

    label("loc_86C3")

    Jump("loc_885F")

    label("loc_86C8")


    #C0323
    ChrTalk(
        0xC,
        (
            "你们收集到了很多\x01",
            "新型魔兽的情报啊。\x01",
            "真是太感谢了。\x02",
        )
    )

    CloseMessageWindow()

    #C0324
    ChrTalk(
        0xC,
        (
            "如此一来，今后应该就能制定出\x01",
            "更加完善的安全对策了。\x02",
        )
    )

    CloseMessageWindow()

    #C0325
    ChrTalk(
        0x101,
        "#12P#0000F哈哈……能帮上忙，是我们的荣幸。\x02",
    )

    CloseMessageWindow()

    #C0326
    ChrTalk(
        0xC,
        (
            "呵呵，真是多谢各位\x01",
            "协助了。\x02",
        )
    )

    CloseMessageWindow()

    #C0327
    ChrTalk(
        0xC,
        (
            "那么，这次就将\x01",
            "特别报酬交给你们，\x01",
            "请一定要收下。\x02",
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
            "１００００米拉\x07\x00",
            "收下了。\x02",
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
            "期待各位今后的\x01",
            "活跃表现。\x02",
        )
    )

    CloseMessageWindow()

    #C0330
    ChrTalk(
        0xC,
        (
            "如果遇到了什么事情，\x01",
            "随时都可以过来哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_885F")

    FadeToDark(500, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_8876")
    ClearScenarioFlags(0x0, 6)

    label("loc_8876")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_888F")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)

    label("loc_888F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_88A8")
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)

    label("loc_88A8")

    OP_4C(0xC, 0xFF)
    SetChrPos(0x0, 2470, 0, 12690, 0)
    EventEnd(0x5)
    TalkBegin(0xC)
    Jump("loc_89AB")

    label("loc_88C7")

    Jc((scpexpr(EXPR_23, 0x6), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8944")

    #C0331
    ChrTalk(
        0xC,
        (
            "总部收集的情报\x01",
            "已经足够了，\x01",
            "所以调查就到此为止。\x02",
        )
    )

    CloseMessageWindow()

    #C0332
    ChrTalk(
        0xC,
        (
            "以后也许还有事情\x01",
            "需要麻烦各位，\x01",
            "到时就拜托了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_89AB")

    label("loc_8944")


    #C0333
    ChrTalk(
        0xC,
        (
            "战斗手册上好像\x01",
            "没有新内容呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0334
    ChrTalk(
        0xC,
        (
            "收集到更多的情报之后\x01",
            "再来拿给我看吧，\x01",
            "我们会将情报记录整理的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_89AB")

    Return()

    # Function_23_7E62 end

    def Function_24_89AC(): pass

    label("Function_24_89AC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_8AF9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8A74")

    #C0335
    ChrTalk(
        0xFE,
        "哦，是赛尔盖手下的孩子们啊～\x02",
    )

    CloseMessageWindow()

    #C0336
    ChrTalk(
        0xFE,
        (
            "由于人手不足，\x01",
            "上面把警察学校\x01",
            "这一带的警备任务交给我了～\x02",
        )
    )

    CloseMessageWindow()

    #C0337
    ChrTalk(
        0xFE,
        (
            "我很久没有在现场指挥过了，\x01",
            "但为了年轻的警官们，\x01",
            "一定得努力完成工作～\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_8AF9")

    label("loc_8A74")


    #C0338
    ChrTalk(
        0xFE,
        (
            "自从担任公共安全科的科长之后，\x01",
            "我平时基本只处理行政类工作。\x02",
        )
    )

    CloseMessageWindow()

    #C0339
    ChrTalk(
        0xFE,
        (
            "但现在可是非常时期，\x01",
            "为了年轻的警官们，\x01",
            "我一定得努力完成工作～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8AF9")

    TalkEnd(0xFE)
    Return()

    # Function_24_89AC end

    def Function_25_8AFD(): pass

    label("Function_25_8AFD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_8C75")
    OP_4B(0xD, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8C19")

    #C0340
    ChrTalk(
        0xE,
        (
            "训练生们似乎\x01",
            "都有些不安。\x02",
        )
    )

    CloseMessageWindow()

    #C0341
    ChrTalk(
        0xE,
        (
            "偶然来这里参加交通讲座的\x01",
            "市民们在听说结界已经消失后，\x01",
            "也都很想立刻回到市里。\x02",
        )
    )

    CloseMessageWindow()

    #C0342
    ChrTalk(
        0xD,
        (
            "唔，确实需要尽快\x01",
            "应对那方面的情况啊～\x02",
        )
    )

    CloseMessageWindow()

    #C0343
    ChrTalk(
        0xD,
        (
            "好，明白了，那方面的应对工作\x01",
            "就交给我和女警们吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0344
    ChrTalk(
        0xD,
        (
            "你们继续\x01",
            "执行警备工作～\x02",
        )
    )

    CloseMessageWindow()

    #C0345
    ChrTalk(
        0xE,
        "是！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_8C71")

    label("loc_8C19")


    #C0346
    ChrTalk(
        0xD,
        (
            "应对训练生和市民的工作\x01",
            "就交给我和女警们吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0347
    ChrTalk(
        0xD,
        (
            "你们继续\x01",
            "执行警备工作～\x02",
        )
    )

    CloseMessageWindow()

    #C0348
    ChrTalk(
        0xE,
        "是！\x02",
    )

    CloseMessageWindow()

    label("loc_8C71")

    OP_4C(0xD, 0xFF)

    label("loc_8C75")

    TalkEnd(0xFE)
    Return()

    # Function_25_8AFD end

    def Function_26_8C79(): pass

    label("Function_26_8C79")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A2AD")
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

    def lambda_8DBA():
        OP_93(0xF, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF, 0, lambda_8DBA)
    Sleep(50)

    def lambda_8DCA():
        OP_93(0x8, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_8DCA)
    Sleep(50)
    WaitChrThread(0xF, 0)
    WaitChrThread(0x8, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x69, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_8FCF")

    #C0349
    ChrTalk(
        0xF,
        "#01005F#5P啊，你们终于来了。\x02",
    )

    CloseMessageWindow()
    OP_68(0, 1000, 9000, 4000)

    def lambda_8E21():
        OP_9B(0x0, 0x101, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_8E21)
    Sleep(0)

    def lambda_8E39():
        OP_9B(0x0, 0x102, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_8E39)
    Sleep(0)

    def lambda_8E51():
        OP_9B(0x0, 0x109, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_8E51)
    Sleep(0)

    def lambda_8E69():
        OP_9B(0x0, 0x105, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_8E69)
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
            "#5P罗伊德、诺艾尔上士，\x01",
            "好久不见了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0351
    ChrTalk(
        0x101,
        (
            "#00004F#11P我们到了，刚才耽搁了\x01",
            "一些时间，实在是不好意思。\x02",
        )
    )

    CloseMessageWindow()

    #C0352
    ChrTalk(
        0xF,
        (
            "#01000F#5P嗯，我刚才接到了联络，\x01",
            "听说你们协助\x01",
            "取缔了飙车族。\x02\x03",

            "#01004F既然发生了那种事，\x01",
            "迟到这种小事就不必计较了。\x01",
            "……辛苦你们了。\x02",
        )
    )

    CloseMessageWindow()

    #C0353
    ChrTalk(
        0x101,
        (
            "#00012F#11P哈哈，谢谢您。\x02\x03",

            "#00002F另外，胡安事务长，\x01",
            "好久不见了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_90DB")

    label("loc_8FCF")


    #C0354
    ChrTalk(
        0xF,
        "#01005F#5P哦，你们来了啊。\x02",
    )

    CloseMessageWindow()
    OP_68(0, 1000, 9000, 4000)

    def lambda_9005():
        OP_9B(0x0, 0x101, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_9005)
    Sleep(0)

    def lambda_901D():
        OP_9B(0x0, 0x102, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_901D)
    Sleep(0)

    def lambda_9035():
        OP_9B(0x0, 0x109, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_9035)
    Sleep(0)

    def lambda_904D():
        OP_9B(0x0, 0x105, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_904D)
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
            "#5P罗伊德、诺艾尔上士，\x01",
            "好久不见了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0356
    ChrTalk(
        0x101,
        (
            "#00004F#11P我们到了。\x02\x03",

            "#00002F胡安事务长，\x01",
            "好久不见了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_90DB")


    #C0357
    ChrTalk(
        0x109,
        "#10109F#12P您这么有精神，真是太好了。\x02",
    )

    CloseMessageWindow()

    #C0358
    ChrTalk(
        0x8,
        (
            "#5P哈哈，和诺艾尔最后一次见面，\x01",
            "还是在上次的定期演习时吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0359
    ChrTalk(
        0x8,
        (
            "#5P至于罗伊德，毕业之后就没有再见了，\x01",
            "差不多有十个月了吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0360
    ChrTalk(
        0x8,
        (
            "#5P哎呀，才过这么一段时间，\x01",
            "你就已经变得如此可靠了。\x02",
        )
    )

    CloseMessageWindow()

    #C0361
    ChrTalk(
        0x101,
        (
            "#00012F#11P哈哈……\x01",
            "我还差得远呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0362
    ChrTalk(
        0x102,
        "#00105F#12P这位是……\x02",
    )

    CloseMessageWindow()

    #C0363
    ChrTalk(
        0x105,
        (
            "#10300F#12P看来就是\x01",
            "警察学校的负责人了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0364
    ChrTalk(
        0xF,
        (
            "#01004F#5P是的，他就是负责管理这个区域\x01",
            "所有设施的胡安事务长。\x02",
        )
    )

    CloseMessageWindow()

    #C0365
    ChrTalk(
        0x8,
        (
            "#5P哪里哪里，\x01",
            "没有那么了不起啦。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0xF, 500)
    Sleep(300)

    #C0366
    ChrTalk(
        0x8,
        (
            "#6P好了，赛尔盖，\x01",
            "会议室就给你\x01",
            "随意使用吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xF, 0x8, 500)

    #C0367
    ChrTalk(
        0xF,
        "#01002F#11P嗯，多谢。\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x8, 3, 0, 27)
    Sleep(3000)
    TurnDirection(0xF, 0x101, 500)

    #C0368
    ChrTalk(
        0xF,
        (
            "#01003F#5P好，我们就别浪费时间了。\x02\x03",

            "#01000F马上开始吧，\x01",
            "你们快跟我过来。\x02",
        )
    )

    CloseMessageWindow()
    OP_68(1280, 1000, 9280, 1500)
    OP_93(0xF, 0x5A, 0x1F4)

    def lambda_9374():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_9374)

    def lambda_9389():

        label("loc_9389")

        TurnDirection(0xFE, 0xF, 500)
        Yield()
        Jump("loc_9389")

    QueueWorkItem2(0x101, 2, lambda_9389)

    def lambda_939B():

        label("loc_939B")

        TurnDirection(0xFE, 0xF, 500)
        Yield()
        Jump("loc_939B")

    QueueWorkItem2(0x102, 2, lambda_939B)

    def lambda_93AD():

        label("loc_93AD")

        TurnDirection(0xFE, 0xF, 500)
        Yield()
        Jump("loc_93AD")

    QueueWorkItem2(0x109, 2, lambda_93AD)

    def lambda_93BF():

        label("loc_93BF")

        TurnDirection(0xFE, 0xF, 500)
        Yield()
        Jump("loc_93BF")

    QueueWorkItem2(0x105, 2, lambda_93BF)
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
        "#00105F#12P那个，赛尔盖科长……？\x02",
    )

    CloseMessageWindow()

    #C0370
    ChrTalk(
        0x101,
        (
            "#00001F#6P请问……\x01",
            "到底有什么事呢？\x02",
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
            "#01005F#11P怎么，你们还没明白吗？\x02\x03",

            "#01004F明明已经给了你们各种提示啊……\x01",
            "呵呵，这证明你们还很稚嫩呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0372
    ChrTalk(
        0x101,
        (
            "#00011F#6P唔……请、请等一下！\x02\x03",

            "#00003F各种提示……\x01",
            "还有把我们叫来这里的意义……\x02\x03",

            "#00000F难道说……\x02",
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
            "#1K赛尔盖科长叫我们来此，所为何事？\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【搜查官考试讲座】\x01",        # 0
            "【交通基本法讲座】\x01",        # 1
            "【导力网络技术讲座】\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_95F1"),
        (1, "loc_96DA"),
        (2, "loc_977C"),
        (SWITCH_DEFAULT, "loc_9859"),
    )


    label("loc_95F1")


    #C0374
    ChrTalk(
        0xF,
        (
            "#01006F#11P你不是已经拥有\x01",
            "搜查官资格了吗。\x02\x03",

            "#01003F特别任务支援科的性质比较特殊，\x01",
            "并不需要全部成员都\x01",
            "考取搜查官资格。\x02\x03",

            "#01000F正确答案是──\x01",
            "『交通基本法讲座』。\x02",
        )
    )

    CloseMessageWindow()

    #C0375
    ChrTalk(
        0x101,
        "#00005F#6P啊……\x02",
    )

    CloseMessageWindow()

    #C0376
    ChrTalk(
        0x102,
        "#00102F#12P既然如此，也就是说……\x02",
    )

    CloseMessageWindow()
    Jump("loc_9859")

    label("loc_96DA")

    OP_2C(0xA1, 0x1)

    #C0377
    ChrTalk(
        0x101,
        (
            "#00002F#6P原来如此……\x01",
            "是『交通基本法讲座』吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0378
    ChrTalk(
        0x102,
        "#00105F#12P啊……！\x02",
    )

    CloseMessageWindow()

    #C0379
    ChrTalk(
        0xF,
        "#01004F#11P呵呵，答对了。\x02",
    )

    CloseMessageWindow()

    #C0380
    ChrTalk(
        0x109,
        (
            "#10105F#6P请问……\x01",
            "这难道意味着……？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9859")

    label("loc_977C")


    #C0381
    ChrTalk(
        0xF,
        (
            "#01003F#11P这里确实也覆盖着\x01",
            "导力网络……\x02\x03",

            "但如果要给你们讲那个的话，\x01",
            "就会让你们去财团事务所之类的地方了。\x02\x03",

            "#01000F正确答案是──\x01",
            "『交通基本法讲座』。\x02",
        )
    )

    CloseMessageWindow()

    #C0382
    ChrTalk(
        0x101,
        "#00005F#6P啊……\x02",
    )

    CloseMessageWindow()

    #C0383
    ChrTalk(
        0x102,
        "#00102F#12P既然如此，也就是说……\x02",
    )

    CloseMessageWindow()
    Jump("loc_9859")

    label("loc_9859")


    #C0384
    ChrTalk(
        0xF,
        (
            "#01004F#11P没错，上面给特别任务支援科\x01",
            "配备了一辆导力车。\x02\x03",

            "#01002F借此机会，我要让你们把\x01",
            "交通法的基础知识牢牢记住。\x02",
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
            "#01003F#5P……以上就是在驾驶导力车时\x01",
            "必须要掌握的交通基本法。\x02\x03",

            "#01000F怎么样，都记住了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0386
    ChrTalk(
        0x101,
        "#00006F#11P应、应该没问题。\x02",
    )

    CloseMessageWindow()

    #C0387
    ChrTalk(
        0x105,
        (
            "#10306F#12P哎呀，真没想到\x01",
            "还要在这种地方上课……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x69, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_9C34")

    #C0388
    ChrTalk(
        0x102,
        (
            "#00100F#6P……话说回来，这些法规\x01",
            "比想象中要简单得多啊。\x02\x03",

            "#00103F而且对外国人的惩处力度\x01",
            "实在是太过轻微了……\x01",
            "那宗飙车事件就是个典型的例子。\x02\x03",

            "#00101F如果导力车的数量在今后进一步增多，\x01",
            "凭借现在的法规，\x01",
            "根本就无法应对吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0389
    ChrTalk(
        0xF,
        (
            "#01006F#5P那些就是今后的问题了。\x02\x03",

            "#01001F私家导力车的出现\x01",
            "还不到十年。\x02\x03",

            "今后自然需要更加\x01",
            "严谨的法规。\x02\x03",

            "针对外国人的惩处措施也是一样。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9D2D")

    label("loc_9C34")


    #C0390
    ChrTalk(
        0x102,
        (
            "#00103F#6P……话说回来，这些法规\x01",
            "比想象中要简单得多啊。\x02\x03",

            "#00101F如果导力车的数量在今后进一步增多，\x01",
            "凭借现在的法规，\x01",
            "根本就无法应对吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0391
    ChrTalk(
        0xF,
        (
            "#01006F#5P那些就是今后的问题了。\x02\x03",

            "#01001F私家导力车的出现\x01",
            "还不到十年。\x02\x03",

            "今后自然需要更加\x01",
            "严谨的法规。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9D2D")


    #C0392
    ChrTalk(
        0x109,
        (
            "#10103F#11P目前，只要向\x01",
            "政府提交申请，\x01",
            "就能轻易获得驾照……\x02\x03",

            "#10101F但我记得现在已经开始\x01",
            "商讨引入考试制度了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0393
    ChrTalk(
        0xF,
        (
            "#01003F#5P嗯，到时候将会\x01",
            "开办各种讲座，\x01",
            "并考核实际操作。\x02\x03",

            "#01000F总之，今天就先记牢\x01",
            "这些基本法规吧。\x02\x03",

            "至于实际驾驶……\x01",
            "诺艾尔，就交由你负责了。\x02",
        )
    )

    CloseMessageWindow()

    #C0394
    ChrTalk(
        0x109,
        "#10102F#11P好的，我明白了！\x02",
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
            "#00002F#5P对哦，诺艾尔\x01",
            "当然会驾驶导力车。\x02",
        )
    )

    CloseMessageWindow()

    #C0396
    ChrTalk(
        0x102,
        (
            "#00109F#6P她连警备队的车辆\x01",
            "都可以得心应手地驾驶呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0397
    ChrTalk(
        0x105,
        "#10305F#6P哦？是吗？\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x109, 0x0)
    Sleep(300)

    #C0398
    ChrTalk(
        0x109,
        (
            "#10112F#11P啊哈哈……因为我加入\x01",
            "警备队之后，受到过司令的严格训练。\x02",
        )
    )

    CloseMessageWindow()

    #C0399
    ChrTalk(
        0xF,
        (
            "#01003F#5P好，那就赶快把\x01",
            "导力车交给你们吧。\x02\x03",

            "#01000F它就停在外面，你们跟我来。\x02",
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
            "#00012F#5P哈哈……\x01",
            "真是太让人惊喜了。\x02",
        )
    )

    CloseMessageWindow()

    #C0401
    ChrTalk(
        0x102,
        "#00102F#6P是啊，科长可真坏啊。\x02",
    )

    CloseMessageWindow()

    #C0402
    ChrTalk(
        0x105,
        (
            "#10304F#6P导力车吗？\x02\x03",

            "#10300F我对这方面不太清楚，\x01",
            "不过应该就是乌尔努公司或\x01",
            "莱恩福尔特公司的产品吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0403
    ChrTalk(
        0x109,
        (
            "#10109F#11P嗯，说到私家导力车，\x01",
            "也就只有这两大制造商了嘛。\x02\x03",

            "#10102F其中乌尔努公司是老厂家，\x01",
            "出产的型号相当丰富。\x02\x03",

            "从小型车到中型车，\x01",
            "甚至连巴士都有所涉足。\x02",
        )
    )

    CloseMessageWindow()

    #C0404
    ChrTalk(
        0x102,
        (
            "#00100F#6P莱恩福尔特公司\x01",
            "则主要出产运输车与高级轿车吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0405
    ChrTalk(
        0x109,
        (
            "#10104F#11P是的，相比之下，\x01",
            "它出产的都是结实又高级的东西。\x02\x03",

            "#10100F据说有不少产品还运用了\x01",
            "导力列车和导力战车方面的技术。\x02",
        )
    )

    CloseMessageWindow()

    #C0406
    ChrTalk(
        0x101,
        (
            "#00004F#5P嗯……\x01",
            "虽说事出突然，总觉得不敢相信，\x01",
            "不过我也开始有点激动了。\x02\x03",

            "#00000F好，我们这就去看看吧。\x02",
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

    label("loc_A2AD")

    Return()

    # Function_26_8C79 end

    def Function_27_A2AE(): pass

    label("Function_27_A2AE")

    OP_93(0xFE, 0x13B, 0x1F4)
    OP_95(0xFE, -3000, 0, 13250, 2000, 0x0)
    OP_95(0xFE, -6500, 0, 13250, 2000, 0x0)
    Return()

    # Function_27_A2AE end

    def Function_28_A2DE(): pass

    label("Function_28_A2DE")

    OP_93(0xFE, 0xE1, 0x1F4)
    OP_95(0xFE, 61500, 0, 18500, 2500, 0x0)
    OP_95(0xFE, 61500, 0, 6500, 2500, 0x0)
    Return()

    # Function_28_A2DE end

    def Function_29_A30E(): pass

    label("Function_29_A30E")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BC, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A9E8")

    #C0407
    ChrTalk(
        0x8,
        (
            "哦？是特别任务支援科\x01",
            "的成员啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0408
    ChrTalk(
        0x8,
        (
            "哎呀，太好了。\x01",
            "你们都平安无事。\x02",
        )
    )

    CloseMessageWindow()

    #C0409
    ChrTalk(
        0x101,
        (
            "#12P#00000F胡安事务长……\x01",
            "您也平安无事，真是太好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0410
    ChrTalk(
        0x102,
        (
            "#12P#00105F警队似乎已经\x01",
            "来这里了啊？\x02\x03",

            "#00103F但这一带原本不是\x01",
            "由国防军负责警备的吗……？\x02",
        )
    )

    CloseMessageWindow()

    #C0411
    ChrTalk(
        0x8,
        (
            "总统被拘捕之后，\x01",
            "国防军就全都撤退了。\x02",
        )
    )

    CloseMessageWindow()

    #C0412
    ChrTalk(
        0x8,
        (
            "为了稳定各地的混乱局势，\x01",
            "他们必须得发挥\x01",
            "自己的作用才行。\x02",
        )
    )

    CloseMessageWindow()

    #C0413
    ChrTalk(
        0x8,
        (
            "所以警察总部派来了支援人员，\x01",
            "代替国防军收拾这里的残局。\x02",
        )
    )

    CloseMessageWindow()

    #C0414
    ChrTalk(
        0x102,
        "#12P#00100F原来如此……\x02",
    )

    CloseMessageWindow()

    #C0415
    ChrTalk(
        0x104,
        (
            "#12P#00303F说起来……\x01",
            "加尔西亚那大叔\x01",
            "最后怎么样了？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A5FC")

    #C0416
    ChrTalk(
        0x105,
        (
            "#12P#10402F听说他当时协助罗伊德\x01",
            "逃离了拘留所呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A695")

    label("loc_A5FC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A64B")

    #C0417
    ChrTalk(
        0x109,
        (
            "#12P#10100F听说他当时协助罗伊德警官\x01",
            "逃离了拘留所呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A695")

    label("loc_A64B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A695")

    #C0418
    ChrTalk(
        0x106,
        (
            "#12P#10702F听说他当时协助罗伊德警官\x01",
            "逃离了拘留所呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A695")


    #C0419
    ChrTalk(
        0x101,
        (
            "#12P#00000F是啊……当时真是\x01",
            "多亏有他相助。\x02\x03",

            "#00006F不对，我们在这种地方谈论这种话题，\x01",
            "未免太过肆无忌惮了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0420
    ChrTalk(
        0x8,
        (
            "没关系，由于总统被捕，\x01",
            "我们已经明白你当时\x01",
            "并不应该被关押在此。\x02",
        )
    )

    CloseMessageWindow()

    #C0421
    ChrTalk(
        0x8,
        (
            "事到如今，\x01",
            "就不必在意那件事了。\x02",
        )
    )

    CloseMessageWindow()

    #C0422
    ChrTalk(
        0x8,
        (
            "说到加尔西亚……\x01",
            "他和国防军大战了一场，\x01",
            "最终被制服。\x02",
        )
    )

    CloseMessageWindow()

    #C0423
    ChrTalk(
        0x8,
        (
            "之后再次被关进了拘留所，\x01",
            "如今正在接受治疗。\x02",
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
        "#12P#00205F治疗吗……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A8C9")

    #C0425
    ChrTalk(
        0x10A,
        (
            "#12P#00603F孤身一人与国防军战斗，\x01",
            "不用说也知道他消耗极剧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A96D")

    label("loc_A8C9")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A91E")

    #C0426
    ChrTalk(
        0x106,
        (
            "#12P#10703F孤身一人与国防军战斗……\x01",
            "身体消耗想必相当剧烈。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A96D")

    label("loc_A91E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A96D")

    #C0427
    ChrTalk(
        0x109,
        (
            "#12P#10103F孤身一人与\x01",
            "国防军战斗……\x01",
            "身体消耗肯定很剧烈。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A96D")


    #C0428
    ChrTalk(
        0x8,
        (
            "是啊，他暂时是\x01",
            "无法动弹了。\x02",
        )
    )

    CloseMessageWindow()

    #C0429
    ChrTalk(
        0x8,
        (
            "不过，如果你们想探监，\x01",
            "倒也可以安排一下……\x02",
        )
    )

    CloseMessageWindow()

    #C0430
    ChrTalk(
        0x102,
        "#12P#00100F罗伊德，怎么办？\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1BC, 1)
    Jump("loc_AA4F")

    label("loc_A9E8")


    #C0431
    ChrTalk(
        0x8,
        (
            "加尔西亚已经再次\x01",
            "被关押在拘留所了，\x01",
            "如今正在接受治疗。\x02",
        )
    )

    CloseMessageWindow()

    #C0432
    ChrTalk(
        0x8,
        (
            "如果你们想探监，\x01",
            "倒也可以安排一下……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AA4F")

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
            "与加尔西亚会面\x01",      # 0
            "放弃\x01",                # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AB60")

    #C0433
    ChrTalk(
        0x101,
        (
            "#12P#00003F（必须要为当时一事\x01",
            "  向加尔西亚好好道谢才行……）\x02\x03",

            "#00000F……胡安事务长，那就麻烦您了。\x02",
        )
    )

    CloseMessageWindow()

    #C0434
    ChrTalk(
        0x8,
        (
            "那我让梅尔文给你们带路，\x01",
            "你们跟我一起来。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 1)
    NewScene("t6050", 101, 0, 0)
    IdleLoop()
    Jump("loc_ABC2")

    label("loc_AB60")


    #C0435
    ChrTalk(
        0x101,
        "#12P#00003F……现在还是算了。\x02",
    )

    CloseMessageWindow()

    #C0436
    ChrTalk(
        0x8,
        "嗯？这样啊。\x02",
    )

    CloseMessageWindow()

    #C0437
    ChrTalk(
        0x8,
        (
            "也罢，如果你们想探监，\x01",
            "随时都可以找我。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_ABC2")

    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 0, 0, 13400, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_4C(0x8, 0xFF)
    EventEnd(0x5)
    Return()

    # Function_29_A30E end

    def Function_30_ABF2(): pass

    label("Function_30_ABF2")


    #C0438
    ChrTalk(
        0x101,
        (
            "#12P#00003F（必须要为当时一事\x01",
            "  向加尔西亚好好道谢才行……）\x02\x03",

            "#00000F……胡安事务长，那就麻烦您了。\x02",
        )
    )

    CloseMessageWindow()

    #C0439
    ChrTalk(
        0x8,
        (
            "那我让梅尔文给你们带路，\x01",
            "你们跟我一起来。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 1)
    NewScene("t6050", 101, 0, 0)
    IdleLoop()
    Return()

    # Function_30_ABF2 end

    def Function_31_ACA2(): pass

    label("Function_31_ACA2")

    EventBegin(0x2)
    ClearMapFlags(0x20)

    #C0440
    ChrTalk(
        0x101,
        (
            "#00000F我们没必要去\x01",
            "其它楼层，还是\x01",
            "不要到处乱转了。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    EventEnd(0x3)
    Return()

    # Function_31_ACA2 end

    def Function_32_ACE6(): pass

    label("Function_32_ACE6")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    OP_0D()
    OP_AF(0xFA)
    FadeToBright(300, 0)
    OP_0D()
    TalkEnd(0xFF)
    Return()

    # Function_32_ACE6 end

    SaveToFile()

Try(main)
