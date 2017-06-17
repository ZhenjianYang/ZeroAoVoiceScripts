from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "c0510.bin",                # FileName
        "c0510",                    # MapName
        "c0510",                    # Location
        0x0029,                     # MapIndex
        "ed7302",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 41, 0, 0, 0, 1],
    )

    BuildStringList((
        "c0510",                  # 0
        "加尔西亚",               # 1
        "恐吓信",                 # 2
        "椅子",                   # 3
    ))

    AddCharChip((
        "chr/ch00000.itc",                   # 00
        "chr/ch00000.itc",                   # 01
        "chr/ch00000.itc",                   # 02
        "chr/ch00000.itc",                   # 03
        "chr/ch00000.itc",                   # 04
        "chr/ch00000.itc",                   # 05
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

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    246,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclActor(89500,   0,       60500,   1200,    89500,   1000,    60500,   0x007C, 0,  3,  0x0000)
    DeclActor(176000,  0,       52000,   1200,    176000,  1000,    52000,   0x007C, 0,  4,  0x0000)
    DeclActor(7500,    0,       60700,   1500,    7800,    1700,    60700,   0x007C, 0,  14, 0x0000)
    DeclActor(-57000,  0,       1000,    1500,    -57000,  1500,    1500,    0x007C, 0,  19, 0x0000)
    DeclActor(52500,   0,       57400,   1500,    52500,   1300,    57400,   0x007C, 0,  21, 0x0000)
    DeclActor(136000,  0,       62000,   1500,    136000,  1500,    62000,   0x007C, 0,  24, 0x0000)
    DeclActor(600,     0,       66000,   1500,    600,     1500,    66200,   0x007C, 0,  26, 0x0000)
    DeclActor(50000,   0,       62110,   1500,    50000,   400,     62110,   0x007C, 0,  5,  0x0000)
    DeclActor(160500,  0,       2500,    1200,    160500,  1500,    2500,    0x007C, 0,  7,  0x0000)
    DeclActor(-51500,  0,       -3500,   1200,    -51500,  1500,    -3500,   0x007C, 0,  8,  0x0000)

    ScpFunction((
        "Function_0_33C",          # 00, 0
        "Function_1_398",          # 01, 1
        "Function_2_534",          # 02, 2
        "Function_3_57C",          # 03, 3
        "Function_4_6B2",          # 04, 4
        "Function_5_7E8",          # 05, 5
        "Function_6_83C",          # 06, 6
        "Function_7_8E2",          # 07, 7
        "Function_8_9D5",          # 08, 8
        "Function_9_AC8",          # 09, 9
        "Function_10_1F5E",        # 0A, 10
        "Function_11_1FD4",        # 0B, 11
        "Function_12_2050",        # 0C, 12
        "Function_13_3568",        # 0D, 13
        "Function_14_38E2",        # 0E, 14
        "Function_15_399A",        # 0F, 15
        "Function_16_39FE",        # 10, 16
        "Function_17_3A63",        # 11, 17
        "Function_18_3D60",        # 12, 18
        "Function_19_4070",        # 13, 19
        "Function_20_415D",        # 14, 20
        "Function_21_43FC",        # 15, 21
        "Function_22_448B",        # 16, 22
        "Function_23_48B3",        # 17, 23
        "Function_24_4DC9",        # 18, 24
        "Function_25_4E4F",        # 19, 25
        "Function_26_516C",        # 1A, 26
        "Function_27_517A",        # 1B, 27
        "Function_28_53D2",        # 1C, 28
    ))


    def Function_0_33C(): pass

    label("Function_0_33C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_35A")
    SetMapFlags(0x10000000)
    SetScenarioFlags(0x0, 1)
    Event(0, 12)
    Jump("loc_374")

    label("loc_35A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_374")
    Event(0, 13)

    label("loc_374")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_383")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 9)

    label("loc_383")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_397")
    OP_C7(0x0, 0x1000)

    label("loc_397")

    Return()

    # Function_0_33C end

    def Function_1_398(): pass

    label("Function_1_398")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_3AD")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 1)

    label("loc_3AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 0)), scpexpr(EXPR_END)), "loc_3BA")
    OP_65(0x2, 0x1)

    label("loc_3BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_3C7")
    OP_65(0x3, 0x1)

    label("loc_3C7")

    OP_65(0x4, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3DD")
    OP_66(0x4, 0x1)

    label("loc_3DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 4)), scpexpr(EXPR_END)), "loc_3EA")
    OP_65(0x5, 0x1)

    label("loc_3EA")

    OP_65(0x6, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_400")
    OP_66(0x6, 0x1)

    label("loc_400")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 3)), scpexpr(EXPR_END)), "loc_412")
    OP_70(0x8, 0xA)
    Jump("loc_416")

    label("loc_412")

    OP_70(0x8, 0x0)

    label("loc_416")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_42F")
    SetMapObjFrame(0xFF, "key_red", 0x0, 0x1)

    label("loc_42F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_449")
    SetMapObjFrame(0xFF, "key_blue", 0x0, 0x1)

    label("loc_449")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 0)), scpexpr(EXPR_END)), "loc_45B")
    OP_70(0x2, 0x2D)
    Jump("loc_47C")

    label("loc_45B")

    OP_70(0x2, 0x0)
    SetBarrier(0x0, 0x0, 0x1, 0x0, 0, -1000, 55000, 3000, 3000, 0)

    label("loc_47C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_494")
    ClearMapObjFlags(0x1, 0x10)
    OP_70(0x1, 0xA)
    Jump("loc_49E")

    label("loc_494")

    ClearMapObjFlags(0x1, 0x10)
    OP_70(0x1, 0x0)

    label("loc_49E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 4)), scpexpr(EXPR_END)), "loc_4C3")
    ClearMapObjFlags(0x0, 0x10)
    OP_70(0x0, 0xA)
    SetMapObjFrame(0xFF, "key0b", 0x1, 0x1)
    Jump("loc_4DA")

    label("loc_4C3")

    ClearMapObjFlags(0x0, 0x10)
    OP_70(0x0, 0x0)
    SetMapObjFrame(0xFF, "key0b", 0x0, 0x1)

    label("loc_4DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 5)), scpexpr(EXPR_END)), "loc_4F5")
    SetMapObjFrame(0xFF, "key0a", 0x0, 0x1)
    Jump("loc_502")

    label("loc_4F5")

    SetMapObjFrame(0xFF, "key0a", 0x1, 0x1)

    label("loc_502")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x111, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_515")
    OP_70(0x1C, 0x0)
    Jump("loc_519")

    label("loc_515")

    OP_70(0x1C, 0x1E)

    label("loc_519")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x111, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_52C")
    OP_70(0x1D, 0x0)
    Jump("loc_530")

    label("loc_52C")

    OP_70(0x1D, 0x1E)

    label("loc_530")

    Call(0, 2)
    Return()

    # Function_1_398 end

    def Function_2_534(): pass

    label("Function_2_534")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6C), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_54D")
    SetMapObjFlags(0x1C, 0x4)
    Jump("loc_553")

    label("loc_54D")

    ClearMapObjFlags(0x1C, 0x4)

    label("loc_553")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x77), scpexpr(EXPR_NEQ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x79), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_575")
    SetMapObjFlags(0x1D, 0x4)
    Jump("loc_57B")

    label("loc_575")

    ClearMapObjFlags(0x1D, 0x4)

    label("loc_57B")

    Return()

    # Function_2_534 end

    def Function_3_57C(): pass

    label("Function_3_57C")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x111, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_669")
    Sound(14, 0, 100, 0)
    OP_71(0x1C, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('中回复药', 1)"), scpexpr(EXPR_END)), "loc_5FB")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0001
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '中回复药'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x111, 1)
    OP_DE(0x6, 0x0)
    Jump("loc_664")

    label("loc_5FB")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0002
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, '中回复药'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多,",
            scpstr(SCPSTR_CODE_ITEM, '中回复药'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x1C, 0x1E, 0x0, 0x0, 0x0)

    label("loc_664")

    Jump("loc_6A6")

    label("loc_669")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0003
    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "宝箱里什么都没有。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_6A6")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_57C end

    def Function_4_6B2(): pass

    label("Function_4_6B2")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x111, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_79F")
    Sound(14, 0, 100, 0)
    OP_71(0x1D, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('ＥＰ填充剂Ⅱ', 1)"), scpexpr(EXPR_END)), "loc_731")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0004
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 'ＥＰ填充剂Ⅱ'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x111, 2)
    OP_DE(0x6, 0x0)
    Jump("loc_79A")

    label("loc_731")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0005
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, 'ＥＰ填充剂Ⅱ'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多,",
            scpstr(SCPSTR_CODE_ITEM, 'ＥＰ填充剂Ⅱ'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x1D, 0x1E, 0x0, 0x0, 0x0)

    label("loc_79A")

    Jump("loc_7DC")

    label("loc_79F")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0006
    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "宝箱里什么都没有。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_7DC")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_6B2 end

    def Function_5_7E8(): pass

    label("Function_5_7E8")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B0(0xF)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7FE")
    Call(0, 6)
    Jump("loc_838")

    label("loc_7FE")

    FadeToDark(300, 0, 100)

    #A0007
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "有本叫做《料理大百科》的书。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()

    label("loc_838")

    TalkEnd(0xFF)
    Return()

    # Function_5_7E8 end

    def Function_6_83C(): pass

    label("Function_6_83C")

    FadeToDark(300, 0, 100)

    #A0008
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "有本叫做《料理大百科》的书。\x02",
        )
    )

    CloseMessageWindow()

    #A0009
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "打开后发现，里面记录着\x01",
            "浓厚奶油汤的食谱。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0010
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '奶油浓汤'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "的做法已经学会了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    OP_B0(0xF)
    Return()

    # Function_6_83C end

    def Function_7_8E2(): pass

    label("Function_7_8E2")

    OP_F2(0x2)
    FadeToDark(300, 0, 100)

    #A0011
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "有恢复导力的装置。\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "在这里休息\x01",      # 0
            "放弃\x01",            # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9B7")
    FadeToBright(100, 0)
    Sleep(500)
    SoundLoad(13)
    OP_74(0x1F, 0x1E)
    Sound(7, 0, 100, 0)
    OP_70(0x1F, 0x0)
    OP_71(0x1F, 0x0, 0x1E, 0x0, 0x0)
    OP_79(0x1F)
    OP_71(0x1F, 0x1F, 0x186, 0x0, 0x20)
    Sleep(1000)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    Sleep(700)
    Sound(13, 0, 100, 0)
    OP_0D()
    OP_32(0xFF, 0xFE, 0x0)
    OP_6A(0x0, 0x0)
    OP_31(0x1)
    Sleep(3500)
    OP_70(0x1F, 0x0)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    label("loc_9B7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9D3")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_9D3")

    Return()

    # Function_7_8E2 end

    def Function_8_9D5(): pass

    label("Function_8_9D5")

    OP_F2(0x2)
    FadeToDark(300, 0, 100)

    #A0012
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "有恢复导力的装置。\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "在这里休息\x01",      # 0
            "放弃\x01",            # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AAA")
    FadeToBright(100, 0)
    Sleep(500)
    SoundLoad(13)
    OP_74(0x20, 0x1E)
    Sound(7, 0, 100, 0)
    OP_70(0x20, 0x0)
    OP_71(0x20, 0x0, 0x1E, 0x0, 0x0)
    OP_79(0x20)
    OP_71(0x20, 0x1F, 0x186, 0x0, 0x20)
    Sleep(1000)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    Sleep(700)
    Sound(13, 0, 100, 0)
    OP_0D()
    OP_32(0xFF, 0xFE, 0x0)
    OP_6A(0x0, 0x0)
    OP_31(0x1)
    Sleep(3500)
    OP_70(0x20, 0x0)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    label("loc_AAA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_AC6")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_AC6")

    Return()

    # Function_8_9D5 end

    def Function_9_AC8(): pass

    label("Function_9_AC8")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50208.itc", 0x1E)
    LoadChrToIndex("chr/ch00002.itc", 0x1F)
    LoadChrToIndex("chr/ch00102.itc", 0x20)
    LoadChrToIndex("chr/ch00202.itc", 0x21)
    LoadChrToIndex("chr/ch00302.itc", 0x22)
    LoadChrToIndex("apl/ch50091.itc", 0x23)
    LoadChrToIndex("apl/ch50209.itc", 0x24)
    OP_68(610, 1000, 55220, 0)
    MoveCamera(37, 20, 0, 0)
    OP_6E(480, 0)
    SetCameraDistance(25770, 0)
    SetChrChipByIndex(0x101, 0x1F)
    SetChrSubChip(0x101, 0x2)
    SetChrChipByIndex(0x102, 0x20)
    SetChrSubChip(0x102, 0x2)
    SetChrChipByIndex(0x103, 0x21)
    SetChrSubChip(0x103, 0x1)
    SetChrChipByIndex(0x104, 0x22)
    SetChrSubChip(0x104, 0x1)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x103, 0x4)
    SetChrFlags(0x104, 0x4)
    SetChrPos(0x101, 2600, 100, 58900, 270)
    SetChrPos(0x102, 2600, 100, 57500, 270)
    SetChrPos(0x103, -2900, 100, 57500, 90)
    SetChrPos(0x104, -2900, 100, 58900, 90)
    OP_52(0x8, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    SetChrPos(0x8, -300, 0, 61300, 180)
    SetChrChipByIndex(0x9, 0x23)
    SetChrSubChip(0x9, 0x1E)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, 0, 300, 59700, 0)
    OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    OP_78(0x1E, 0xA)
    OP_49()
    SetChrPos(0xA, 0, 0, 61700, 0)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis030.itp")
    Sleep(1000)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("豪气的声音")

    #A0013
    AnonymousTalk(
        0xFF,
        "哼哼──我还以为有什么事呢。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_68(610, 1000, 59730, 3000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x1)
    Sleep(500)
    Fade(500)
    OP_68(610, 1000, 59730, 0)
    MoveCamera(37, 20, 0, 0)
    OP_6E(480, 0)
    SetCameraDistance(19420, 0)
    OP_0D()
    Sleep(300)

    #C0014
    ChrTalk(
        0x8,
        (
            "#5P#3104F你怀疑我们会长写恐吓信\x01",
            "威胁伊莉娅·普拉提耶……？\x02\x03",

            "#5P#3100F哼哼哼……\x01",
            "真是蠢话。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x101,
        (
            "#0003F#12P……当然了，我们目前\x01",
            "还并未下结论。\x02\x03",

            "#0001F只是，我们在对案件调查无从下手的时候，\x01",
            "听说了会长和伊莉娅小姐前几天发生的争执……\x02\x03",

            "所以就来向您询问一下情况而已。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x8,
        (
            "#5P#3104F哈哈……\x01",
            "是会长被扇了一耳光的那件事吗？\x02\x03",

            "#3100F那不就是在喝酒时发生的\x01",
            "一点小误会而已吗？\x02\x03",

            "会长当时也喝多了，\x01",
            "好像根本就记不起这件事了。\x02\x03",

            "我觉得他完全没把这件事放在心上。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x101,
        "#0005F#12P是……这样吗？\x02",
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x102,
        (
            "#4P#0103F我们听到过这样的传闻……\x02\x03",

            "#0100F据说，各位准备赞助伊莉娅小姐\x01",
            "去帝都的歌剧院演出？\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x8,
        (
            "#5P#3100F嗯……是有这么回事。\x02\x03",

            "我们这边正好有些人脉关系，\x01",
            "对方想请我们帮忙促成此事。\x02\x03",

            "#3104F哈，不过那也只是一个借口而已。\x01",
            "会长似乎只是想以特邀嘉宾的形式\x01",
            "招待她参加那个……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0020
    ChrTalk(
        0x101,
        "#0005F#12P那个……？\x02",
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x103,
        "#0205F#6P#N特邀嘉宾……？\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0022
    ChrTalk(
        0x8,
        (
            "#5P#3101F啊，那是我们内部的事情。\x02\x03",

            "#3104F──总之，就是这样了，\x01",
            "恐吓信的事和我们完全无关。\x02\x03",

            "#3100F哼哼……听懂了吗，小鬼们？\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x101,
        (
            "#0003F#12P……………………………………\x02\x03",

            "#0001F……慎重起见，能否请您看一下\x01",
            "恐吓信的原件呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x8,
        (
            "#5P#3100F哈……也好。\x02\x03",

            "拿来。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x101,
        "#0001F#12P……就是这个。\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    SetChrName("")

    #A0026
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "罗伊德把恐吓信交给了加尔西亚。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #A0027
    AnonymousTalk(
        0x8,
        (
            "#5P#3101F嗯……什么啊。\x02\x03",

            "看起来，的确有人想要妨碍\x01",
            "伊莉娅·普拉提耶的演出啊……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToBright(300, 0)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    #Sound(1853, 255, 100, 0)    #voice#Garcia

    #C0028
    ChrTalk(
        0x8,
        "#5P#3105F嗯……！？\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0029
    ChrTalk(
        0x101,
        "#0001F#12P（哎……！？）\x02",
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x102,
        "#4P#0101F（他好像察觉到了什么呢……）\x02",
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x8,
        "#5P#3101F……………………………………\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x8)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    SetChrName("")

    #A0032
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "加尔西亚将恐吓信丢回给了罗伊德。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    Sleep(300)

    #C0033
    ChrTalk(
        0x8,
        (
            "#5P#3104F……哼，太可笑了。\x02\x03",

            "#3100F与其说是恐吓信，\x01",
            "倒像是个单纯的恶作剧吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x101,
        "#0005F#12P哎……\x02",
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x104,
        "#3P#0301F喂喂……\x02",
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x102,
        (
            "#4P#0101F不过，看您刚才的反应，\x01",
            "好像是发现了什么问题吧……？\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x8,
        (
            "#5P#3104F哼，你在说什么？\x02\x03",

            "把信上所写的内容全部看完，\x01",
            "我也完全没有头绪。\x02\x03",

            "#3100F不过，我至少可以断言，\x01",
            "这封信绝对不是我们会长写的。\x02\x03",

            "哼哼……看样子，你们是白跑了一趟啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x101,
        "#0001F#12P……………………………………\x02",
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x104,
        (
            "#3P#0301F（可恶……\x01",
            "  他肯定是察觉到了什么……）\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x103,
        "#6P#0201F#N（但是，好像很难打探出来……）\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0041
    ChrTalk(
        0x101,
        (
            "#0003F#12P……我明白您的意思了。\x02\x03",

            "#0000F不过，关于这件事情，\x01",
            "我能否直接向会长先生进行询问呢？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0042
    ChrTalk(
        0x8,
        "#5P#3105F啊……？\x02",
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x104,
        (
            "#3P#0304F是啊，像这种问题，\x01",
            "最好还是直接向当事人进行确认。\x02\x03",

            "#0300F还是说，他现在不在呢？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x8)
    Sound(1857, 255, 100, 0)    #voice#Garcia
    Sleep(1000)
    Sleep(300)
    OP_82(0xC8, 0x0, 0xBB8, 0x190)
    #Sound(1855, 255, 100, 0)    #voice#Garcia

    #C0044
    ChrTalk(
        0x8,
        "#5P#3109F#4S#11A哈哈哈哈哈哈！\x02",
    )
    #Auto

    Sleep(1600)
    SetChrFlags(0x8, 0x20)
    SetChrFlags(0x8, 0x2)
    SetChrChipByIndex(0x8, 0x24)
    SetChrSubChip(0x8, 0x0)
    Sound(804, 0, 100, 0)
    OP_68(0, 1000, 60500, 500)
    SetCameraDistance(18000, 500)
    OP_6F(0x11)
    Sleep(300)
    SetChrSubChip(0x8, 0x1)
    OP_82(0x1F4, 0x1F4, 0xBB8, 0x3E8)
    BlurSwitch(0x12C, 0xBBFFFFFF, 0x0, 0x1, 0xA)
    Sound(818, 0, 100, 0)
    Sound(813, 0, 100, 0)
    OP_68(430, 1000, 59740, 1000)
    SetCameraDistance(18500, 1000)
    Sleep(800)
    OP_63(0x101, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    OP_63(0x102, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    OP_63(0x103, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    OP_63(0x104, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    OP_6F(0x11)
    CancelBlur(300)
    Sleep(300)

    #C0045
    ChrTalk(
        0x103,
        "#6P#0210F#N唔……\x02",
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x102,
        "#4P#0110F……！\x02",
    )

    CloseMessageWindow()
    Sleep(150)
    Fade(250)
    SetChrPos(0x8, -300, 0, 61300, 180)
    ClearChrFlags(0x8, 0x20)
    ClearChrFlags(0x8, 0x2)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    OP_0D()
    Sleep(500)

    #C0047
    ChrTalk(
        0x8,
        (
            "#5P#3103F──别得意忘形啊，小鬼们。\x02\x03",

            "会长怎么可能亲自接见\x01",
            "你们这种菜鸟……\x02\x03",

            "#3102F你们不过就是几只无知又可悲的小狗崽子，\x01",
            "我随时都能用一根手指头捻死你们……\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x101,
        "#0007F#12P什么……\x02",
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x104,
        "#3P#0301F……嘁…………\x02",
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x8,
        (
            "#5P#3104F原本，连我也没打算亲自\x01",
            "来见你们这种小毛头……\x02\x03",

            "只不过看在机会难得的份上，\x01",
            "才来亲切地给你们一个忠告。\x02\x03",

            "#3102F──无论你们怎么努力，\x01",
            "都无法改变这座城市的现状……\x02\x03",

            "更别想把我们给怎么样了，\x01",
            "那是完全不可能的。\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x101,
        "#0013F#12P………唔………………\x02",
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x102,
        "#4P#0101F……………………………………\x02",
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x104,
        "#3P#0301F这还真是嚣张至极啊……\x02",
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x8,
        (
            "#5P#3103F听明白的话，就赶快给我消失。\x02\x03",

            "我可没空和你们这些\x01",
            "小鬼纠缠不清。\x02\x03",

            "#3101F不过，你们以后要是再敢找商会的麻烦……\x01",
            "就算只是小鬼头，我们也会毫不留情地除掉你们。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x101, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    Fade(250)
    ClearChrFlags(0x101, 0x4)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrPos(0x101, 2000, 0, 58900, 315)
    Sound(820, 0, 100, 0)
    OP_0D()
    Sleep(500)

    #C0055
    ChrTalk(
        0x101,
        (
            "#12P#0003F……我们心怀感激地\x01",
            "收下您的忠告。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x10E, 0x1F4)
    Sleep(300)

    #C0056
    ChrTalk(
        0x101,
        (
            "#0001F#11P──各位，我们走吧。\x01",
            "调查工作已经足够了。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x103, 0x0)
    Sleep(100)
    SetChrSubChip(0x104, 0x0)
    Sleep(200)

    #C0057
    ChrTalk(
        0x102,
        "#4P#0103F嗯……\x02",
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x103,
        "#0203F#5P……也对。\x02",
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x104,
        (
            "#0303F嘿……连杯茶\x01",
            "都不舍得给我们喝啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    ClearChrFlags(0x102, 0x4)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrPos(0x102, 2000, 0, 57500, 270)
    ClearChrFlags(0x103, 0x4)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrPos(0x103, -2000, 0, 57500, 90)
    ClearChrFlags(0x104, 0x4)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    SetChrPos(0x104, -2000, 0, 58900, 90)
    Sound(820, 0, 100, 0)
    OP_0D()
    OP_68(0, 1000, 56400, 4000)
    BeginChrThread(0x102, 3, 0, 10)
    Sleep(700)
    BeginChrThread(0x103, 3, 0, 11)
    Sleep(200)
    BeginChrThread(0x101, 3, 0, 10)
    Sleep(700)
    OP_93(0x104, 0xB4, 0x1F4)

    def lambda_1CE0():
        OP_95(0xFE, -2000, 0, 54200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1CE0)
    WaitChrThread(0x104, 1)

    def lambda_1CFE():
        OP_95(0xFE, 0, 0, 52200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1CFE)
    Sleep(500)
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    WaitChrThread(0x104, 1)

    def lambda_1D31():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1D31)

    #C0060
    ChrTalk(
        0x8,
        (
            "#3105F──等等。\x02\x03",

            "那个红毛……\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x104, 1)
    OP_6F(0x1)
    OP_63(0x104, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)
    OP_93(0x104, 0x0, 0x190)
    Sleep(300)

    #C0061
    ChrTalk(
        0x104,
        "#0301F……啊？是在叫我吗？\x02",
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x8,
        (
            "#3101F你这头红毛……\x01",
            "我好像曾在哪里见到过……\x02\x03",

            "……不……那应该是不可能的………\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x104,
        (
            "#0306F喂喂，饶了我吧。\x02\x03",

            "如果是个魅力十足的姐姐倒还好，\x01",
            "我可没兴趣接受大叔的搭讪啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x8)

    #C0064
    ChrTalk(
        0x8,
        (
            "#3104F……哼，算了。\x02\x03",

            "#3100F真是碍眼，快滚吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x104,
        (
            "#0301F哈……\x01",
            "不是你出声叫住我的吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x104, 0xB4, 0x1F4)

    def lambda_1ED7():
        OP_95(0xFE, 0, 0, 50000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1ED7)
    FadeToDark(2000, 0, -1)
    Sleep(500)

    def lambda_1EFE():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_1EFE)
    Sleep(500)
    OP_0D()
    WaitChrThread(0x104, 1)
    StopBGM(0xFA0)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_CA(0x1, 0xFF, 0x0)
    SetScenarioFlags(0x5C, 0)
    NewScene("c0500", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_9_AC8 end

    def Function_10_1F5E(): pass

    label("Function_10_1F5E")

    OP_93(0xFE, 0xB4, 0x1F4)

    def lambda_1F6A():
        OP_95(0xFE, 2000, 0, 54200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1F6A)
    WaitChrThread(0xFE, 1)

    def lambda_1F88():
        OP_95(0xFE, 0, 0, 52200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1F88)
    WaitChrThread(0xFE, 1)

    def lambda_1FA6():
        OP_95(0xFE, 0, 0, 50000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1FA6)
    Sleep(500)

    def lambda_1FC3():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1FC3)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_10_1F5E end

    def Function_11_1FD4(): pass

    label("Function_11_1FD4")

    OP_93(0xFE, 0xB4, 0x1F4)

    def lambda_1FE0():
        OP_95(0xFE, -2000, 0, 54200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1FE0)
    WaitChrThread(0xFE, 1)

    def lambda_1FFE():
        OP_95(0xFE, 0, 0, 52200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1FFE)
    WaitChrThread(0xFE, 1)

    def lambda_201C():
        OP_95(0xFE, 0, 0, 50000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_201C)
    Sound(103, 0, 100, 0)
    Sleep(500)

    def lambda_203F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_203F)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_11_1FD4 end

    def Function_12_2050(): pass

    label("Function_12_2050")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50421.itc", 0x1E)
    AddParty(0x9, 0xFF, 0xFF)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_32(0x9, 0x0, 0x22)
    RemoveCraft(0x9, 0xFFFF)
    OP_38(0x9, 0x80, 0x2)
    OP_38(0x9, 0x81, 0x2)
    OP_38(0x9, 0x82, 0x2)
    OP_38(0x9, 0x83, 0x2)
    OP_38(0x9, 0x84, 0x2)
    OP_38(0x9, 0x85, 0x2)
    OP_38(0x9, 0x86, 0x2)
    OP_42(0x9, 0x451, 0xFF)
    OP_42(0x9, 0x5E9, 0xFF)
    OP_42(0x9, 0x64D, 0xFF)
    AddCraft(0x9, 0xF0)
    AddCraft(0x9, 0xF1)
    AddCraft(0x9, 0xF2)
    AddCraft(0x9, 0xF3)
    AddCraft(0x9, 0xF4)
    AddCraft(0x9, 0x127)
    SetChrChipPat(0x9, 0x6, 0x127)
    AddCraft(0x9, 0x147)
    OP_42(0x9, 0x81, 0x0)
    OP_42(0x9, 0xA3, 0x3)
    OP_42(0x9, 0x87, 0x4)
    OP_42(0x9, 0x69, 0x5)
    OP_42(0x9, 0x66, 0x6)
    OP_42(0x9, 0x6C, 0x2)
    OP_42(0x9, 0x7B, 0x1)
    OP_68(0, 1100, 4800, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(23000, 0)
    SetChrPos(0x101, -200, 0, -500, 0)
    SetChrPos(0x102, 200, 0, -500, 0)
    SetChrPos(0x103, -200, 0, -500, 0)
    SetChrPos(0x104, 200, 0, -500, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x10A, 0, 30, 4800, 0)
    StopBGM(0x7D0)
    WaitBGM()
    OP_C7(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0066
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#1K同日，１１：００──\x02",
        )
    )

    Sleep(2500)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C7(0x1, 0x800)
    PlayBGM("ed7302", 0)
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x12E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetCameraDistance(21000, 4000)
    FadeToBright(2000, 0)
    Sleep(1000)
    OP_93(0x10A, 0x5A, 0x1F4)
    Sleep(700)
    OP_93(0x10A, 0x10F, 0x1F4)
    Sleep(1000)
    OP_93(0x10A, 0x0, 0x1F4)
    OP_6F(0x10)

    #C0067
    ChrTalk(
        0x10A,
        (
            "#0608F#11P哼……\x01",
            "这到底是怎么回事……\x02\x03",

            "#0610F可恶的鲁巴彻……\x01",
            "到底在搞什么鬼！？\x02",
        )
    )

    CloseMessageWindow()
    Sound(103, 0, 100, 0)
    Sleep(300)
    OP_63(0x10A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_22A2():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10A, 2, lambda_22A2)
    OP_68(110, 1100, 3690, 2000)
    MoveCamera(45, 19, 0, 2000)
    SetCameraDistance(20000, 2000)

    def lambda_22D4():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_22D4)

    def lambda_22E5():
        OP_96(0xFE, 0xFFFFFE0C, 0x0, 0x834, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_22E5)
    Sleep(400)

    def lambda_2302():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_2302)

    def lambda_2313():
        OP_96(0xFE, 0x1F4, 0x0, 0x834, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2313)
    Sleep(400)

    def lambda_2330():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_2330)

    def lambda_2341():
        OP_96(0xFE, 0xFFFFFD44, 0x0, 0x44C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2341)
    Sleep(400)

    def lambda_235E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_235E)

    def lambda_236F():
        OP_96(0xFE, 0x2BC, 0x0, 0x44C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_236F)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    OP_6F(0x79)

    #C0068
    ChrTalk(
        0x10A,
        "#5P#0605F你、你们……！？\x02",
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x101,
        (
            "#12P#0000F果然是\x01",
            "达德利警官啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x104,
        (
            "#0301F#12P喂喂，\x01",
            "到底是什么情况啊？\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x10A,
        (
            "#5P#0607F喂！我不是刚说过\x01",
            "不许你们插手的吗！？\x02\x03",

            "你们现在应该专心进行\x01",
            "药物方面的调查──\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0x102,
        (
            "#0106F#12P您说的很有道理，不过\x01",
            "现在是计较这些的时候吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0x103,
        (
            "#12P#0201F……果然，里面连\x01",
            "一个人都没有吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x10A,
        "#5P#0610F唔……\x02",
    )

    CloseMessageWindow()
    OP_63(0x10A, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1200)

    #C0075
    ChrTalk(
        0x10A,
        (
            "#5P#0603F……从刚才开始，我就一直\x01",
            "大声呼喊，但是没有一个人出来。\x02\x03",

            "不过，也没有任何\x01",
            "发生过争斗的迹象……\x02\x03",

            "#0610F不如说我才想知道，\x01",
            "这到底是什么情况呢——！\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x101,
        (
            "#12P#0001F没记错的话，一科应该一直在\x01",
            "监视着鲁巴彻的动向吧？\x02\x03",

            "你们难道不清楚这些黑手党是在何时\x01",
            "消失不见的吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0x10A,
        "#5P#0608F……………………………………\x02",
    )

    CloseMessageWindow()
    OP_63(0x10A, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x10A)

    #C0078
    ChrTalk(
        0x10A,
        (
            "#5P#0603F……昨晚，警察局总部\x01",
            "收到了一封犯罪预告。\x02\x03",

            "预告里写着，他们会在\x01",
            "克洛斯贝尔空港安装炸弹。\x02",
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

    #C0079
    ChrTalk(
        0x101,
        "#12P#0011F炸、炸弹！？\x02",
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0x102,
        "#0105F#12P怎、怎么会……！？\x02",
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0x10A,
        (
            "#5P#0603F于是，我们一科的人就被紧急调配，\x01",
            "前往空港警戒。\x02\x03",

            "#0601F……在上级的指示下，\x01",
            "我们监视鲁巴彻的人员都被\x01",
            "调配到了那边。\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x101,
        "#12P#0013F啊……\x02",
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x104,
        (
            "#0306F#12P也就是说，他们是趁着警察被调走\x01",
            "的机会而离开的吗……\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x103,
        (
            "#12P#0203F……真可疑啊。\x02\x03",

            "#0211F那封安装炸弹的预告信\x01",
            "到底有多少可信度呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0x10A,
        (
            "#5P#0603F谁知道……\x02\x03",

            "#0608F……可恶，上层的家伙\x01",
            "究竟在想些什么……！\x02\x03",

            "到底想把警察的荣耀\x01",
            "践踏到什么地步……！？\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x102,
        "#0108F#12P达德利搜查官……\x02",
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x101,
        "#12P#0008F……………………………………\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    #C0088
    ChrTalk(
        0x101,
        (
            "#12P#0003F──无论如何，\x01",
            "再这么下去，就无法掌握到\x01",
            "事件的进展。\x02\x03",

            "#0001F我们要不要把这栋建筑的内部\x01",
            "彻底搜查一下？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x10A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0089
    ChrTalk(
        0x10A,
        "#5P#0607F喂……！？\x02",
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x101,
        (
            "#12P#0006F我当然知道，警察局和鲁巴彻\x01",
            "之间保持着微妙的平衡关系。\x02\x03",

            "我也知道，在没有搜查令的状态下去搜查\x01",
            "别人的私人领地，会给对方留下多少反击的把柄……\x02\x03",

            "#0001F我完全明白这样做的风险。\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x102,
        "#0108F#12P罗伊德……\x02",
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0x10A,
        (
            "#5P#0610F呃……那为什么\x01",
            "还要说出这种鲁莽的话！？\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x101,
        (
            "#12P#0003F因为这场事件，如今很可能已经发展到\x01",
            "让我们『无法在意那些风险』的严重地步了。\x02\x03",

            "#0001F──让我先把从昨晚到今早\x01",
            "已经查明的事情告诉您吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0094
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "将那种蓝色药片很有可能是\x01",
            "六年前瓦解的疯狂教团\x01",
            "所制作的药物……\x02\x03",

            "以及服用过此药物的人们全部离奇失踪\x01",
            "等情况都进行了说明。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToBright(300, 0)

    #C0095
    ChrTalk(
        0x10A,
        (
            "#5P#0605F难、难以置信……\x02\x03",

            "我以前也曾听说过关于那个教团的事情，\x01",
            "还以为他们已经被完全剿灭了……\x02\x03",

            "#0608F……不过，即使如此……\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0x101,
        (
            "#12P#0001F总之，这是件人命关天的大事。\x02\x03",

            "这里说不定还残留着一些\x01",
            "与失踪人员们有关的情报。\x02\x03",

            "#0003F如果达德利警官无法认同，\x01",
            "至少请允许我们……\x02\x03",

            "#0013F不──请允许我一个人擅做主张一次吧，\x01",
            "您能否睁只眼闭只眼，通融放行呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0x10A,
        "#5P#0605F…………………………………\x02",
    )

    CloseMessageWindow()

    def lambda_2DE7():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_2DE7)
    Sleep(100)
    TurnDirection(0x102, 0x101, 500)

    #C0098
    ChrTalk(
        0x104,
        (
            "#0306F#11P喂喂，不要把所有责任\x01",
            "都揽到自己一个人的身上啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0x102,
        (
            "#0100F#11P我们当然会与你站在同一条战线上。\x02\x03",

            "就算支援科因此被解散，\x01",
            "我们也不能对这种状况坐视不管。\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0x103,
        "#12P#0204F嗯，我们永远共同进退。\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0xB3, 0x1F4)

    #C0101
    ChrTalk(
        0x101,
        "#5P#0000F各位……\x02",
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x10A,
        (
            "#5P#0603F……哼……\x01",
            "这就是所谓的血脉相承吧。\x02\x03",

            "#0602F这种强硬的性格……\x01",
            "跟那家伙可真是一模一样啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0x101,
        "#5P#0005F哎……\x02",
    )

    CloseMessageWindow()

    def lambda_2F64():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2F64)
    Sleep(50)

    def lambda_2F74():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_2F74)
    Sleep(50)

    def lambda_2F84():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_2F84)
    WaitChrThread(0x101, 2)
    Sound(1555, 255, 100, 0)    #voice#Dudley
    Sleep(800)
    SetChrFlags(0x10A, 0x20)
    SetChrFlags(0x10A, 0x2)
    SetChrChipByIndex(0x10A, 0x1E)
    SetChrSubChip(0x10A, 0x0)
    Sleep(130)
    SetChrSubChip(0x10A, 0x1)
    Sleep(130)
    Sound(820, 0, 100, 0)
    SetChrSubChip(0x10A, 0x2)
    Sleep(130)
    SetChrSubChip(0x10A, 0x3)
    Sleep(130)
    SetChrSubChip(0x10A, 0x4)
    Sleep(130)
    SetChrSubChip(0x10A, 0x3)
    Sound(882, 0, 100, 0)
    Sleep(500)

    #C0104
    ChrTalk(
        0x10A,
        (
            "#5P#0611F──通过违法搜查而取得的物证，\x01",
            "是不具备法律效力的。\x02\x03",

            "无论那些家伙留下了多少重要的证据，\x01",
            "我们都要当作没看见，明白吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0x101,
        (
            "#12P#0006F那也……没问题。\x02\x03",

            "#0008F我们目前的当务之急是\x01",
            "尽快查明克洛斯贝尔市\x01",
            "到底发生了什么……\x02\x03",

            "#0013F必须要把这件事情彻底调查清楚。\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0x10A,
        "#5P#0611F哼，话说得还真漂亮……\x02",
    )

    CloseMessageWindow()
    Sleep(150)
    #Sound(1556, 255, 100, 0)    #voice#Dudley
    Sleep(500)
    SetChrSubChip(0x10A, 0x1)
    Sleep(100)
    SetChrSubChip(0x10A, 0x0)
    Sleep(100)
    ClearChrFlags(0x10A, 0x20)
    ClearChrFlags(0x10A, 0x2)
    SetChrChipByIndex(0x10A, 0xFF)
    SetChrSubChip(0x10A, 0x0)
    Sleep(600)

    #C0107
    ChrTalk(
        0x10A,
        (
            "#5P#0604F不过，既然你们已经明白目前的处境，\x01",
            "我也就不再多说废话了。\x02\x03",

            "#0602F那你们就好好跟紧我吧，\x01",
            "至少不要给我拖后腿。\x02",
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

    #C0108
    ChrTalk(
        0x101,
        "#12P#0011F哎……\x02",
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0x102,
        (
            "#0105F#12P那个……\x01",
            "刚才说的不是……只要给我们放行就好了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0x10A,
        (
            "#5P#0603F在这种状况下，我难道会\x01",
            "袖手旁观，把事情全盘推给\x01",
            "你们这些乳臭未干的小家伙吗？\x02\x03",

            "#0601F从现在开始，\x01",
            "你们要听从我的指挥。\x02\x03",

            "#0607F所有责任都由我来承担……\x01",
            "不许反驳！\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0x101,
        "#12P#0002F达德利警官……\x02",
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0x104,
        (
            "#0300F#12P哎呀呀……\x01",
            "真是不坦率啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0x103,
        (
            "#12P#0204F果然只是一种\x01",
            "掩饰害羞的方式吧……\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x10A, 0x0, 0x1F4)
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0114
    ChrTalk(
        0x10A,
        (
            "#11P#0603F少、少啰嗦！\x02\x03",

            "#0601F──首先要把建筑物\x01",
            "的内部彻底搜查一遍……\x02\x03",

            "如果发现异常，要立刻进行报告。\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0x101,
        "#12P#0000F是……！\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(20250, 1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(500)
    Sound(828, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0116
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "达德利搜查官加入了队伍。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #A0117
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "可以在主菜单的[TACTICS]选项中\x01",
            "将其设置为参战队员。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_49()
    OP_D5(0x1E)
    OP_68(0, 1280, 2000, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(23500, 0)
    SetChrPos(0x0, 0, 0, 2000, 0)
    SetChrPos(0x1, 0, 0, 2000, 0)
    SetChrPos(0x2, 0, 0, 2000, 0)
    SetChrPos(0x3, 0, 0, 2000, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    ClearMapFlags(0x10000000)
    SetScenarioFlags(0xC4, 1)
    OP_29(0x4C, 0x1, 0xD)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_12_2050 end

    def Function_13_3568(): pass

    label("Function_13_3568")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(0, 1400, 63000, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(22000, 0)
    SetChrPos(0x102, -700, 0, 52300, 0)
    SetChrPos(0x101, 700, 0, 52300, 0)
    SetChrPos(0x103, -1100, 0, 51400, 0)
    SetChrPos(0x104, 1100, 0, 51400, 0)
    SetChrPos(0x10A, 0, 0, 53700, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_68(0, 1500, 55000, 6000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x1)
    Fade(500)
    OP_68(0, 900, 53000, 0)
    MoveCamera(50, 23, 0, 0)
    OP_6E(380, 0)
    SetCameraDistance(23000, 0)
    OP_0D()

    #C0118
    ChrTalk(
        0x101,
        (
            "#0001F这里是……\x01",
            "以前曾经来过的大厅啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0x104,
        "#0301F这些装饰摆设可真是奢华无度啊。\x02",
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0x10A,
        (
            "#5P#0601F哼，在这种地方\x01",
            "大概也不会留有什么犯罪证据……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_64(0x103)
    TurnDirection(0x102, 0x103, 500)

    #C0121
    ChrTalk(
        0x102,
        (
            "#0101F缇欧……\x01",
            "感觉到什么了吗？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3743():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3743)
    Sleep(50)

    def lambda_3753():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_3753)
    Sleep(50)
    TurnDirection(0x10A, 0x103, 500)

    #C0122
    ChrTalk(
        0x103,
        (
            "#12P#0206F是的，上次来这里的时候\x01",
            "也稍微感觉到了一点……\x02\x03",

            "#0201F我觉得这个房间里\x01",
            "似乎隐藏着什么机关。\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0x101,
        "#5P#0005F隐藏着机关……？\x02",
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0x10A,
        "#5P#0601F什么意思？\x02",
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0x103,
        (
            "#12P#0208F这里似乎暗藏着某种\x01",
            "机械式的机关装置……\x02\x03",

            "#0206F……对不起，\x01",
            "有可能只是我的错觉而已。\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0x104,
        (
            "#0300F不，阿缇的判断\x01",
            "不可能会有错吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0x101,
        (
            "#5P#0000F是啊……\x01",
            "稍微调查一下吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, 0, 0, 52000, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetScenarioFlags(0xC4, 2)
    EventEnd(0x5)
    Return()

    # Function_13_3568 end

    def Function_14_38E2(): pass

    label("Function_14_38E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_38F4")
    Call(0, 17)
    Jump("loc_3999")

    label("loc_38F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_390A")
    Call(0, 15)
    Jump("loc_3999")

    label("loc_390A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3920")
    Call(0, 16)
    Jump("loc_3999")

    label("loc_3920")

    TalkBegin(0xFF)
    SetChrName("")
    FadeToDark(300, 0, 100)

    #A0128
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "有两个类似插口的东西并列着。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()

    #C0129
    ChrTalk(
        0x101,
        (
            "#0000F如果这是钥匙孔的话……\x01",
            "钥匙应该也藏在某处。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFF)

    label("loc_3999")

    Return()

    # Function_14_38E2 end

    def Function_15_399A(): pass

    label("Function_15_399A")

    EventBegin(0x2)
    Sleep(500)
    Sound(141, 0, 100, 0)
    SetChrName("")

    #A0130
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "插入了红耀石钥匙。\x01\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SubItemNumber('迪诺的问诊表', 1)
    Fade(250)
    SetMapObjFrame(0xFF, "key_red", 0x1, 0x1)
    Sleep(500)
    SetScenarioFlags(0xC6, 6)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_39FB")
    Call(0, 18)
    Jump("loc_39FD")

    label("loc_39FB")

    EventEnd(0x3)

    label("loc_39FD")

    Return()

    # Function_15_399A end

    def Function_16_39FE(): pass

    label("Function_16_39FE")

    EventBegin(0x2)
    Sleep(500)
    Sound(141, 0, 100, 0)
    SetChrName("")

    #A0131
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "插入了苍耀石钥匙。\x01\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SubItemNumber('纯白之石', 1)
    Fade(250)
    SetMapObjFrame(0xFF, "key_blue", 0x1, 0x1)
    Sleep(500)
    SetScenarioFlags(0xC6, 7)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3A60")
    Call(0, 18)
    Jump("loc_3A62")

    label("loc_3A60")

    EventEnd(0x3)

    label("loc_3A62")

    Return()

    # Function_16_39FE end

    def Function_17_3A63(): pass

    label("Function_17_3A63")

    EventBegin(0x0)
    Fade(1000)
    OP_68(6700, 1200, 60800, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(21000, 0)
    SetChrPos(0x101, 6700, 0, 60800, 90)
    SetChrPos(0x102, 5100, 30, 61000, 90)
    SetChrPos(0x103, 5100, 30, 60000, 90)
    SetChrPos(0x104, 5800, 0, 62000, 135)
    SetChrPos(0x10A, 6700, 0, 59100, 45)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_0D()

    #C0132
    ChrTalk(
        0x101,
        "#0005F哎，这幅画……\x02",
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0x10A,
        (
            "#12P#0601F哼……真可疑啊。\x02\x03",

            "调查一下吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0x101,
        "#0001F好的──\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    Sound(141, 0, 100, 0)
    Sleep(500)
    OP_74(0x8, 0xF)
    OP_71(0x8, 0x0, 0xA, 0x0, 0x0)
    Sound(100, 0, 100, 0)
    OP_79(0x8)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x10A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0135
    ChrTalk(
        0x102,
        "#6P#0105F这是……\x02",
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0x104,
        (
            "#0304F#6P阿缇的直觉果然没错啊。\x02\x03",

            "#0305F这里有两个插口，\x01",
            "似乎能插些什么东西进去……\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0x103,
        (
            "#6P#0203F似乎是某种『钥匙』\x01",
            "的插孔吧。\x02\x03",

            "#0202F如果能把两边都打开，\x01",
            "也许会发生什么呢。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3D06")

    #C0138
    ChrTalk(
        0x101,
        (
            "#0000F#5P好……\x01",
            "（试试刚才找到的钥匙吧。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3D36")

    label("loc_3D06")


    #C0139
    ChrTalk(
        0x101,
        (
            "#0000F#5P好……\x01",
            "找到钥匙之后就来试试看吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3D36")

    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, 6400, 0, 60800, 90)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetScenarioFlags(0xC4, 3)
    OP_29(0x4C, 0x1, 0xE)
    EventEnd(0x5)
    Return()

    # Function_17_3A63 end

    def Function_18_3D60(): pass

    label("Function_18_3D60")

    EventBegin(0x0)
    Fade(1000)
    OP_68(6700, 1200, 60800, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(21000, 0)
    SetChrPos(0x101, 6700, 0, 60800, 90)
    SetChrPos(0x102, 5100, 30, 61000, 90)
    SetChrPos(0x103, 5100, 30, 60000, 90)
    SetChrPos(0x104, 5800, 0, 62000, 135)
    SetChrPos(0x10A, 6700, 0, 59100, 45)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_0D()
    Sound(809, 0, 100, 0)
    Sleep(500)
    OP_68(0, 1200, 57000, 1500)

    def lambda_3E14():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3E14)
    Sleep(50)

    def lambda_3E24():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10A, 2, lambda_3E24)

    def lambda_3E31():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_3E31)
    Sleep(50)

    def lambda_3E41():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_3E41)

    def lambda_3E4E():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_3E4E)
    OP_6F(0x1)
    Sound(155, 2, 100, 0)
    OP_82(0x64, 0x0, 0xBB8, 0xBB8)
    OP_74(0x2, 0xF)
    OP_71(0x2, 0x0, 0x2D, 0x0, 0x0)
    Sleep(2500)
    Sound(149, 0, 100, 0)
    OP_24(0x9B)
    OP_79(0x2)
    SetBarrier(0x2, 0x0, 0x1)
    Sleep(1000)
    Fade(500)
    OP_68(6700, 1200, 60800, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(21000, 0)
    OP_0D()

    #C0140
    ChrTalk(
        0x102,
        (
            "#5P#0105F没、没想到这个房间里\x01",
            "竟然藏有这种机关啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0x101,
        (
            "#0006F#5P而且，从残留的脚印看来，\x01",
            "使用频率应该还很高呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0x10A,
        (
            "#0603F#11P哼，大概马尔克尼之类的人\x01",
            "很喜欢使用这种东西吧。\x02\x03",

            "#0601F也就是说……\x01",
            "前面就是那家伙的房间了吗……？\x02",
        )
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0x104,
        (
            "#0303F#5P说起来，到现在还没发现\x01",
            "类似会长室的房间呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0x103,
        (
            "#5P#0201F前面的房间里很可能\x01",
            "会留有什么证据。\x02",
        )
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0x101,
        "#0001F#5P好……下去看看吧。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, 6400, 0, 60800, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    OP_65(0x2, 0x1)
    SetScenarioFlags(0xC6, 0)
    OP_29(0x4C, 0x1, 0x19)
    EventEnd(0x5)
    Return()

    # Function_18_3D60 end

    def Function_19_4070(): pass

    label("Function_19_4070")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4082")
    Call(0, 20)
    Jump("loc_415C")

    label("loc_4082")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 5)), scpexpr(EXPR_END)), "loc_4093")
    Call(0, 23)
    Jump("loc_415C")

    label("loc_4093")

    TalkBegin(0xFF)
    SetChrName("")
    FadeToDark(300, 0, 100)

    #A0146
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "有块文字输入面板，\x01",
            "似乎是输入密码的装置。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()

    #C0147
    ChrTalk(
        0x10A,
        (
            "#0603F哼，看样子，随便输入的话，\x01",
            "肯定打不开这道门吧。\x02\x03",

            "#0601F我们先搜索一下这栋建筑，\x01",
            "看看有没有跟密码相关的线索吧！\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFF)

    label("loc_415C")

    Return()

    # Function_19_4070 end

    def Function_20_415D(): pass

    label("Function_20_415D")

    EventBegin(0x0)
    Fade(1000)
    OP_68(-57000, 1000, 700, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(21000, 0)
    SetChrPos(0x101, -57000, 0, 700, 0)
    SetChrPos(0x102, -57000, 0, -1000, 0)
    SetChrPos(0x103, -58000, 0, -1400, 0)
    SetChrPos(0x104, -56000, 0, -1400, 0)
    SetChrPos(0x10A, -55700, 0, 700, 315)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_0D()

    #C0148
    ChrTalk(
        0x101,
        "#11P#0005F这是……\x02",
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0x102,
        (
            "#12P#0101F这是……\x01",
            "输入文字的面板？\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0x103,
        (
            "#12P#0203F恐怕是\x01",
            "输入密码的装置吧……\x02",
        )
    )

    CloseMessageWindow()
    OP_68(-59500, 1000, 700, 1500)
    Sleep(500)

    def lambda_4277():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_4277)
    OP_6F(0x1)

    #C0151
    ChrTalk(
        0x103,
        (
            "#11P#0202F……而且，这边还有个\x01",
            "很显眼的铁栅栏。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_42BB():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_42BB)
    Sleep(50)

    def lambda_42CB():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_42CB)
    Sleep(50)

    def lambda_42DB():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10A, 2, lambda_42DB)
    Sleep(50)
    OP_93(0x104, 0x10E, 0x1F4)

    #C0152
    ChrTalk(
        0x104,
        (
            "#0306F如此露骨地在这里设一个铁栅栏，\x01",
            "反而觉得十分可疑啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0x10A,
        (
            "#0603F#11P#N哼，看样子，随便输入的话，\x01",
            "肯定打不开这道门吧。\x02\x03",

            "#0608F如果有笔记之类的东西可以参考，\x01",
            "说不定可以猜到密码……\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0154
    ChrTalk(
        0x101,
        (
            "#0000F#11P#N是啊……\x01",
            "去找找看吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, -57000, 0, 400, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    OP_66(0x4, 0x1)
    SetScenarioFlags(0xC4, 4)
    EventEnd(0x5)
    Return()

    # Function_20_415D end

    def Function_21_43FC(): pass

    label("Function_21_43FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_440E")
    Call(0, 22)
    Jump("loc_448A")

    label("loc_440E")

    TalkBegin(0xFF)
    SetChrName("")

    #A0155
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "写真杂志里\x01",
            "夹着一张笔记纸。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0156
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "『图书馆最受欢迎的童话书的\x01",
            "  书名与作者名』\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)

    label("loc_448A")

    Return()

    # Function_21_43FC end

    def Function_22_448B(): pass

    label("Function_22_448B")

    EventBegin(0x0)
    Fade(1000)
    OP_68(53720, 1200, 58520, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(19480, 0)
    SetChrPos(0x101, 53900, 0, 59300, 225)
    SetChrPos(0x102, 53400, 0, 60300, 180)
    SetChrPos(0x103, 52400, 0, 60300, 180)
    SetChrPos(0x104, 53900, 0, 58200, 270)
    SetChrPos(0x10A, 54500, 0, 57200, 270)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_0D()
    SetChrName("")

    #A0157
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "桌子上放着写真杂志。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0158
    ChrTalk(
        0x101,
        (
            "#5P#0005F这是……\x01",
            "黑手党成员们\x01",
            "看的杂志吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0x104,
        (
            "#11P#0302F啊，这是我也很爱看的\x01",
            "《热辣宝贝》的最新一期呢。\x02\x03",

            "#0309F（翻动）……\x01",
            "嗯嗯，大饱眼福啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0x102,
        "#5P#0111F兰迪……你可真是……\x02",
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0x103,
        "#0206F#5P算了，反正兰迪前辈一向如此。\x02",
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0x10A,
        "#0606F#11P真是的，现在的年轻人啊……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0163
    ChrTalk(
        0x101,
        (
            "#5P#0005F哎……\x02\x03",

            "#0001F刚才好像看到某一页里\x01",
            "夹着什么啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0x104,
        (
            "#11P#0301F嗯……？\x02\x03",

            "#0305F……哦哦！\x01",
            "夹着一张纸条呢。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0165
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "写真杂志里\x01",
            "夹着一张笔记纸。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0166
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "『图书馆最受欢迎的童话书的\x01",
            "  书名与作者名』\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x10A, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)
    OP_64(0x10A)

    #C0167
    ChrTalk(
        0x102,
        "#5P#0101F这是……\x02",
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0x103,
        (
            "#0201F#5P……莫非是和下面那个房间里的\x01",
            "机关密码有关的笔记吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0x10A,
        (
            "#0604F#11P哼……\x01",
            "很有可能。\x02",
        )
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0x101,
        (
            "#5P#0000F嗯，那就赶快到一层的\x01",
            "输入装置那里试试看吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, 54200, 30, 58200, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetScenarioFlags(0xC4, 5)
    OP_29(0x4C, 0x1, 0xF)
    EventEnd(0x5)
    Return()

    # Function_22_448B end

    def Function_23_48B3(): pass

    label("Function_23_48B3")

    EventBegin(0x0)
    Fade(1000)
    OP_68(-57000, 1000, 700, 0)
    MoveCamera(34, 25, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(21000, 0)
    SetChrPos(0x101, -57000, 0, 700, 0)
    SetChrPos(0x102, -57000, 0, -1000, 0)
    SetChrPos(0x103, -58000, 0, -1400, 0)
    SetChrPos(0x104, -56000, 0, -1400, 0)
    SetChrPos(0x10A, -55700, 0, 700, 315)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_0D()
    SetScenarioFlags(0x0, 0)
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 8, -1, -1)
    SetChrName("")

    #A0171
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1K请连续输入\x01",
            "两种密码。\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "莉奈和七匹龙\x01",                # 0
            "王妃卡隆物语\x01",                # 1
            "阿琉泽流浪记\x01",                # 2
            "玛尔克与森林深处的魔女\x01",      # 3
            "莉黛尔童话集\x01",                # 4
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_49F0")
    ClearScenarioFlags(0x0, 0)

    label("loc_49F0")


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "亚利·贝\x01",            # 0
            "肖恩·阿尔纳姆\x01",      # 1
            "约克·阿西玛\x01",        # 2
            "阿玛尼塔·海姆\x01",      # 3
            "雷切尔·布郎\x01",        # 4
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4A55")
    ClearScenarioFlags(0x0, 0)

    label("loc_4A55")

    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_4DA2")
    Sound(87, 0, 100, 0)
    Sleep(300)
    OP_68(-59500, 1000, 700, 1500)
    Sleep(500)

    def lambda_4A8A():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4A8A)
    Sleep(50)

    def lambda_4A9A():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_4A9A)
    Sleep(50)

    def lambda_4AAA():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10A, 2, lambda_4AAA)
    Sleep(50)

    def lambda_4ABA():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_4ABA)
    Sleep(50)

    def lambda_4ACA():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_4ACA)
    OP_6F(0x1)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)
    Sound(143, 0, 100, 0)
    Sleep(300)
    OP_74(0x1, 0xF)
    OP_71(0x1, 0x0, 0xA, 0x0, 0x0)
    Sound(120, 0, 100, 0)
    OP_79(0x1)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x10A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_68(-57000, 1000, 700, 2000)
    OP_6F(0x1)

    #C0172
    ChrTalk(
        0x101,
        (
            "#0000F#11P太好了……\x01",
            "看来对上了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0x102,
        (
            "#11P#0102F呵呵，机关设计得如此精巧，\x01",
            "密码条却随便乱放，真是粗心大意啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0x104,
        (
            "#0306F#11P是啊，竟然把这么重要的情报\x01",
            "夹在那种写真杂志里。\x02\x03",

            "#0301F入侵者不是\x01",
            "一下就能找到了嘛！\x02",
        )
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0x103,
        (
            "#11P#0206F我认为……一般的入侵者\x01",
            "是不会去翻看那种写真杂志的……\x02",
        )
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0x10A,
        (
            "#11P#0604F总之，无论是何种防范措施，\x01",
            "关键也都在于如何运用。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10A, 0x103, 500)
    Sleep(300)

    #C0177
    ChrTalk(
        0x10A,
        (
            "#5P#0600F──走吧，\x01",
            "前面应该会有些什么。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4D3E():
        TurnDirection(0xFE, 0x10A, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4D3E)
    Sleep(150)

    def lambda_4D4E():
        TurnDirection(0xFE, 0x10A, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_4D4E)
    Sleep(50)

    def lambda_4D5E():
        TurnDirection(0xFE, 0x10A, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_4D5E)
    Sleep(50)
    TurnDirection(0x104, 0x10A, 500)

    #C0178
    ChrTalk(
        0x101,
        "#6P#0000F是啊……！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_65(0x3, 0x1)
    OP_65(0x4, 0x1)
    SetScenarioFlags(0xC4, 6)
    OP_29(0x4C, 0x1, 0x10)
    Jump("loc_4DAB")

    label("loc_4DA2")

    Sound(3, 0, 100, 0)
    Sleep(300)

    label("loc_4DAB")

    SetChrPos(0x0, -57000, 0, 400, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_23_48B3 end

    def Function_24_4DC9(): pass

    label("Function_24_4DC9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4DDB")
    Call(0, 25)
    Jump("loc_4E4E")

    label("loc_4DDB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4DF1")
    Call(0, 28)
    Jump("loc_4E4E")

    label("loc_4DF1")

    TalkBegin(0xFF)
    SetChrName("")
    FadeToDark(300, 0, 100)

    #A0179
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "书架上有一个很不自然的空隙。\x01",
            "似乎隐藏着一个感压式机关。\x02",
        )
    )

    CloseMessageWindow()
    FadeToBright(300, 0)
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)

    label("loc_4E4E")

    Return()

    # Function_24_4DC9 end

    def Function_25_4E4F(): pass

    label("Function_25_4E4F")

    EventBegin(0x0)
    Fade(1000)
    OP_68(135600, 1200, 60700, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(21000, 0)
    SetChrPos(0x101, 136300, 0, 60700, 0)
    SetChrPos(0x102, 135300, 0, 59400, 0)
    SetChrPos(0x103, 135300, 0, 60700, 0)
    SetChrPos(0x104, 136300, 0, 59400, 0)
    SetChrPos(0x10A, 137800, 0, 60000, 315)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_0D()

    #C0180
    ChrTalk(
        0x101,
        (
            "#0005F#12P嗯……？\x02\x03",

            "#0001F这里为什么会有一处\x01",
            "很不自然的空隙呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0x102,
        (
            "#12P#0105F会不会是有人从这里\x01",
            "把书给抽走了？\x02",
        )
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0x103,
        "#6P#0201F不……\x02",
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x103)

    #C0183
    ChrTalk(
        0x103,
        (
            "#6P#0203F──似乎是在下方装设了\x01",
            "一个感压装置。\x02\x03",

            "#0200F只要放上特定重量的物体，\x01",
            "应该就能解除机关了。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x10A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0184
    ChrTalk(
        0x104,
        (
            "#12P#0306F喂喂……\x01",
            "听起来怎么像间谍小说一样啊？\x02",
        )
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0x10A,
        (
            "#0603F#12P哼……\x01",
            "是用于防范入侵者的保安措施吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x10A, 0x10E, 0x1F4)
    Sleep(300)

    #C0186
    ChrTalk(
        0x10A,
        (
            "#0601F#11P那就简单了，\x01",
            "在大楼里找找重量和这处空隙\x01",
            "比较符合的『砝码』吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x5A, 0x1F4)

    #C0187
    ChrTalk(
        0x101,
        "#5P#0000F明白了！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, 136300, 0, 60400, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    OP_66(0x6, 0x1)
    SetScenarioFlags(0xC5, 2)
    OP_29(0x4C, 0x1, 0x13)
    EventEnd(0x5)
    Return()

    # Function_25_4E4F end

    def Function_26_516C(): pass

    label("Function_26_516C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5179")
    Call(0, 27)

    label("loc_5179")

    Return()

    # Function_26_516C end

    def Function_27_517A(): pass

    label("Function_27_517A")

    EventBegin(0x0)
    Fade(1000)
    OP_68(200, 1200, 65200, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(21000, 0)
    SetChrPos(0x101, 600, 0, 64700, 0)
    SetChrPos(0x102, -400, 0, 64700, 0)
    SetChrPos(0x103, -400, 30, 63500, 0)
    SetChrPos(0x104, 600, 30, 63500, 0)
    SetChrPos(0x10A, 1900, 0, 64000, 315)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_0D()
    SetChrName("")

    #A0188
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "摆放着金色的台座。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_52E2")

    #C0189
    ChrTalk(
        0x101,
        (
            "#0005F#11P这个台座……\x01",
            "是用纯金制造的吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0x102,
        (
            "#12P#0101F不，似乎只是在其它的\x01",
            "金属上镀了金。\x02\x03",

            "#0103F不过，以鲁巴彻的财力来说，\x01",
            "就算它是纯金的，\x01",
            "也没什么好奇怪……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_52E2")

    FadeToDark(300, 0, 100)
    OP_0D()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【拿走台座】\x01",      # 0
            "【保持原样】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_5336"),
        (1, "loc_53AC"),
        (SWITCH_DEFAULT, "loc_53B1"),
    )


    label("loc_5336")

    Fade(500)
    SetMapObjFrame(0xFF, "key0a", 0x0, 0x1)
    Sound(51, 0, 100, 0)
    Sleep(100)
    Sound(50, 0, 100, 0)
    OP_0D()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0191
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '尼克鲁的问诊表'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber('尼克鲁的问诊表', 1)
    OP_65(0x6, 0x1)
    SetScenarioFlags(0xC6, 5)
    Jump("loc_53B1")

    label("loc_53AC")

    Jump("loc_53B1")

    label("loc_53B1")

    SetScenarioFlags(0xC5, 3)
    SetChrPos(0x0, 200, 0, 64400, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_27_517A end

    def Function_28_53D2(): pass

    label("Function_28_53D2")

    EventBegin(0x0)
    Fade(1000)
    OP_68(135600, 1200, 60700, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(21000, 0)
    SetChrPos(0x101, 136300, 0, 60700, 0)
    SetChrPos(0x102, 135300, 0, 59400, 0)
    SetChrPos(0x103, 135300, 0, 60700, 0)
    SetChrPos(0x104, 136300, 0, 59400, 0)
    SetChrPos(0x10A, 137800, 0, 60000, 315)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_0D()
    SubItemNumber('尼克鲁的问诊表', 1)
    Fade(500)
    SetMapObjFrame(0xFF, "key0b", 0x1, 0x1)
    Sound(51, 0, 100, 0)
    Sleep(100)
    Sound(50, 0, 100, 0)
    OP_0D()
    Sleep(300)
    OP_68(141600, 1200, 60700, 1500)
    MoveCamera(45, 30, 0, 1500)
    OP_6F(0x1)
    OP_82(0x64, 0x0, 0xBB8, 0x7D0)
    OP_74(0x0, 0x5)
    OP_71(0x0, 0x0, 0xA, 0x0, 0x0)
    Sound(155, 2, 100, 0)

    def lambda_54DB():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_54DB)
    Sleep(50)

    def lambda_54EB():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10A, 2, lambda_54EB)

    def lambda_54F8():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_54F8)
    Sleep(50)

    def lambda_5508():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_5508)

    def lambda_5515():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_5515)
    OP_79(0x0)
    Sound(149, 0, 100, 0)
    OP_24(0x9B)
    Sleep(500)
    Fade(500)
    OP_68(136170, 1200, 60700, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(18910, 0)
    OP_0D()

    #C0192
    ChrTalk(
        0x101,
        "#5P#0000F好……！\x02",
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0x104,
        (
            "#6P#0306F不过，这还真是个\x01",
            "完全出于兴趣而建造的机关……\x02\x03",

            "#0301F为什么不用普通的钥匙啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0194
    ChrTalk(
        0x103,
        (
            "#6P#0211F而且制造这种机关，\x01",
            "需要花费大量的米拉……\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x10A, 0x10E, 0x1F4)

    #C0195
    ChrTalk(
        0x10A,
        (
            "#0603F#11P恐怕正是马尔克尼个人的癖好吧。\x02\x03",

            "#0600F我听说，他最喜欢\x01",
            "稀奇古怪的机关。\x02",
        )
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0x102,
        (
            "#6P#0106F那些在他手下做事的人\x01",
            "为了迎合他这种兴趣，大概也很辛苦吧……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, 136300, 0, 60400, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    OP_65(0x5, 0x1)
    SetScenarioFlags(0xC5, 4)
    OP_29(0x4C, 0x1, 0x14)
    EventEnd(0x5)
    Return()

    # Function_28_53D2 end

    SaveToFile()

Try(main)
