from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "ガルシア",               # 1
        "脅迫状",                 # 2
        "イス",                   # 3
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
        "Function_4_6C9",          # 04, 4
        "Function_5_816",          # 05, 5
        "Function_6_870",          # 06, 6
        "Function_7_924",          # 07, 7
        "Function_8_A2F",          # 08, 8
        "Function_9_B3A",          # 09, 9
        "Function_10_2120",        # 0A, 10
        "Function_11_2196",        # 0B, 11
        "Function_12_2212",        # 0C, 12
        "Function_13_3874",        # 0D, 13
        "Function_14_3C2E",        # 0E, 14
        "Function_15_3D00",        # 0F, 15
        "Function_16_3D6A",        # 10, 16
        "Function_17_3DD5",        # 11, 17
        "Function_18_40F8",        # 12, 18
        "Function_19_442A",        # 13, 19
        "Function_20_4531",        # 14, 20
        "Function_21_47DA",        # 15, 21
        "Function_22_4881",        # 16, 22
        "Function_23_4D0B",        # 17, 23
        "Function_24_527B",        # 18, 24
        "Function_25_5319",        # 19, 25
        "Function_26_565C",        # 1A, 26
        "Function_27_566A",        # 1B, 27
        "Function_28_58EC",        # 1C, 28
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x111, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_678")
    Sound(14, 0, 100, 0)
    OP_71(0x1C, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1F5, 1)"), scpexpr(EXPR_END)), "loc_601")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0001
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1F5),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x111, 1)
    OP_DE(0x6, 0x0)
    Jump("loc_673")

    label("loc_601")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0002
    AnonymousTalk(
        0x3E7,
        (
            "宝箱には",
            scpstr(SCPSTR_CODE_ITEM, 0x1F5),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "が入っている。\x01",
            "持ち物が一杯なので、",
            scpstr(SCPSTR_CODE_ITEM, 0x1F5),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "をあきらめた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x1C, 0x1E, 0x0, 0x0, 0x0)

    label("loc_673")

    Jump("loc_6BD")

    label("loc_678")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0003
    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "宝箱には何も入っていない。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_6BD")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_57C end

    def Function_4_6C9(): pass

    label("Function_4_6C9")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x111, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7C5")
    Sound(14, 0, 100, 0)
    OP_71(0x1D, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1F9, 1)"), scpexpr(EXPR_END)), "loc_74E")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0004
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1F9),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x111, 2)
    OP_DE(0x6, 0x0)
    Jump("loc_7C0")

    label("loc_74E")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0005
    AnonymousTalk(
        0x3E7,
        (
            "宝箱には",
            scpstr(SCPSTR_CODE_ITEM, 0x1F9),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "が入っている。\x01",
            "持ち物が一杯なので、",
            scpstr(SCPSTR_CODE_ITEM, 0x1F9),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "をあきらめた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x1D, 0x1E, 0x0, 0x0, 0x0)

    label("loc_7C0")

    Jump("loc_80A")

    label("loc_7C5")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0006
    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "宝箱には何も入っていない。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_80A")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_6C9 end

    def Function_5_816(): pass

    label("Function_5_816")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B0(0xF)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_82C")
    Call(0, 6)
    Jump("loc_86C")

    label("loc_82C")

    FadeToDark(300, 0, 100)

    #A0007
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "『料理大百科』と書かれた本がある。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()

    label("loc_86C")

    TalkEnd(0xFF)
    Return()

    # Function_5_816 end

    def Function_6_870(): pass

    label("Function_6_870")

    FadeToDark(300, 0, 100)

    #A0008
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "『料理大百科』と書かれた本がある。\x02",
        )
    )

    CloseMessageWindow()

    #A0009
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "開くと濃厚クリームスープの\x01",
            "レシピが書かれていた。\x02",
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
            scpstr(SCPSTR_CODE_ITEM, 0x1BB),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "のレシピを覚えた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    OP_B0(0xF)
    Return()

    # Function_6_870 end

    def Function_7_924(): pass

    label("Function_7_924")

    OP_F2(0x2)
    FadeToDark(300, 0, 100)

    #A0011
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "オーブメントを回復できる装置がある。\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "ここで休憩する\x01",      # 0
            "やめる\x01",              # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A11")
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

    label("loc_A11")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A2D")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_A2D")

    Return()

    # Function_7_924 end

    def Function_8_A2F(): pass

    label("Function_8_A2F")

    OP_F2(0x2)
    FadeToDark(300, 0, 100)

    #A0012
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "オーブメントを回復できる装置がある。\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "ここで休憩する\x01",      # 0
            "やめる\x01",              # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B1C")
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

    label("loc_B1C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B38")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_B38")

    Return()

    # Function_8_A2F end

    def Function_9_B3A(): pass

    label("Function_9_B3A")

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
    SetChrName("豪胆な声")

    #A0013
    AnonymousTalk(
        0xFF,
        "クク──何かと思えば。\x02",
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
            "#5P#3104Fウチの会長が、イリア・プラティエに\x01",
            "脅迫状で嫌がらせだと……？\x02\x03",

            "#5P#3100Fククク……\x01",
            "とんだヨタ話もあったもんだぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x101,
        (
            "#0003F#12P……無論、こちらもそうだと\x01",
            "決め付けているわけではありません。\x02\x03",

            "#0001Fですが、殆んど手がかりがない状況で\x01",
            "先日もめ事があったと聞きまして……\x02\x03",

            "参考までに話を伺えればと。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x8,
        (
            "#5P#3104Fハハ……\x01",
            "会長が引っ叩#2Rぱた#かれたヤツか。\x02\x03",

            "#3100Fありゃ、酒の席での\x01",
            "ちょっとしたハプニングだ。\x02\x03",

            "会長も酒が入ってたせいか\x01",
            "ほとんど記憶にないらしいしな。\x02\x03",

            "全然、気にしてないと思うぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x101,
        "#0005F#12Pそう……なんですか？\x02",
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x102,
        (
            "#4P#0103Fお聞きした話だと……\x02\x03",

            "#0100F帝都のオペラハウスへの進出を\x01",
            "イリアさんに持ちかけられたとか？\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x8,
        (
            "#5P#3100Fああ……そんな話もあったな。\x02\x03",

            "ウチも色々な付き合いがある。\x01",
            "そっちの方から仲介された話だ。\x02\x03",

            "#3104Fまあ、むしろそれは口実で\x01",
            "会長はあれの特別ゲストとして\x01",
            "彼女を招待したかったらしいが……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0020
    ChrTalk(
        0x101,
        "#0005F#12Pあれ……？\x02",
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x103,
        "#0205F#6P#N特別ゲスト……？\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0022
    ChrTalk(
        0x8,
        (
            "#5P#3101Fああ、こっちの話だ。\x02\x03",

            "#3104F──まあ、そういうわけで\x01",
            "何の関わりもねぇ話ってことだ。\x02\x03",

            "#3100Fクク……分かったか、坊主ども？\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x101,
        (
            "#0003F#12P……………………………………\x02\x03",

            "#0001F……念のため、脅迫状の現物を\x01",
            "確認してもらってもいいですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x8,
        (
            "#5P#3100Fハ……まあいいだろう。\x02\x03",

            "よこせ。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x101,
        "#0001F#12P……これです。\x02",
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
            "ロイドはガルシアに脅迫状を渡した。\x07\x00\x02",
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
            "#5P#3101Fはん……なんだこいつは。\x02\x03",

            "確かにイリア・プラティエの\x01",
            "公演を妨害したいみてぇだが……\x02",
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
        "#5P#3105Fん……！？\x02",
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
        "#0001F#12P（え……！？）\x02",
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x102,
        "#4P#0101F（何か気付いたみたい……）\x02",
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
            "ガルシアはロイドに脅迫状を投げ返した。\x07\x00\x02",
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
            "#5P#3104F……フン、下らねぇな。\x02\x03",

            "#3100F脅迫状というよりは\x01",
            "単なるイタズラじゃねえのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x101,
        "#0005F#12Pえ……\x02",
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x104,
        "#3P#0301Fおいおい……\x02",
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x102,
        (
            "#4P#0101F何か心当たりがあるような\x01",
            "反応でしたけど……？\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x8,
        (
            "#5P#3104Fフン、何のことだ？\x02\x03",

            "手紙の文面についても\x01",
            "まったく心当たりはねぇな。\x02\x03",

            "#3100Fま、少なくともウチの会長が\x01",
            "書いたんじゃねえのは断言できる。\x02\x03",

            "クク……とんだ無駄足だったなぁ？\x02",
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
            "#3P#0301F（チッ……\x01",
            "  何か知っていそうだが……）\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x103,
        "#6P#0201F#N（聞き出すのは難しそうですね……）\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0041
    ChrTalk(
        0x101,
        (
            "#0003F#12P……話は判りました。\x02\x03",

            "#0000Fところで、今の話を会長さんから\x01",
            "直接お聞きできないでしょうか？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0042
    ChrTalk(
        0x8,
        "#5P#3105Fは……？\x02",
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x104,
        (
            "#3P#0304Fああ、確かにそういった話は\x01",
            "本人から直接聞きたいもんだな。\x02\x03",

            "#0300Fそれとも留守でもしてんのかい？\x02",
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
        "#5P#3109F#4S#11Aははははははッ！\x02",
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
        "#6P#0210F#Nっ……\x02",
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
            "#5P#3103F──調子に乗るなよ、小僧ども？\x02\x03",

            "てめぇらみたいなガキどもに\x01",
            "会長が会うわけねえだろうが……\x02\x03",

            "#3102Fいつでもヒネリ潰すことのできる\x01",
            "無知で哀れな仔犬ごときによ……？\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x101,
        "#0007F#12Pなっ……\x02",
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x104,
        "#3P#0301F……チッ…………\x02",
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x8,
        (
            "#5P#3104F本来なら俺も、てめぇらごときに\x01",
            "わざわざ会うつもりは無かったが……\x02\x03",

            "せっかくの機会だから\x01",
            "親切に忠告してやろうと思ったわけだ。\x02\x03",

            "#3102F──てめぇらが何をしようが\x01",
            "この街#6Rクロスベル#の現実は変わらねぇ……\x02\x03",

            "ましてや俺たちをどうこうする事など\x01",
            "不可能ってことをな。\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x101,
        "#0013F#12P………くっ………………\x02",
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
        "#3P#0301F随分、余裕タップリじゃねぇか……\x02",
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x8,
        (
            "#5P#3103F分かったら、とっとと失せろ。\x02\x03",

            "てめえらみてぇなガキどもを\x01",
            "相手してるほど暇じゃねえんだ。\x02\x03",

            "#3101Fだが、これ以上歯向かえば……\x01",
            "ガキだろうが容赦なく叩き潰す。\x02",
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
            "#12P#0003F……忠告、ありがたく\x01",
            "受け取っておきますよ。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x10E, 0x1F4)
    Sleep(300)

    #C0056
    ChrTalk(
        0x101,
        (
            "#0001F#11P──行こう、みんな。\x01",
            "聞き込みはこれで十分だ。\x02",
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
        "#4P#0103Fええ……\x02",
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x103,
        "#0203F#5P……ですね。\x02",
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x104,
        (
            "#0303Fヘッ……茶の一杯くらい\x01",
            "出しやがれってんだ。\x02",
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

    def lambda_1E76():
        OP_95(0xFE, -2000, 0, 54200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1E76)
    WaitChrThread(0x104, 1)

    def lambda_1E94():
        OP_95(0xFE, 0, 0, 52200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1E94)
    Sleep(500)
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    WaitChrThread(0x104, 1)

    def lambda_1EC7():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1EC7)

    #C0060
    ChrTalk(
        0x8,
        (
            "#3105F──待て。\x02\x03",

            "そこの赤毛……\x02",
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
        "#0301F……ああ、俺のことか？\x02",
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x8,
        (
            "#3101Fその赤毛……\x01",
            "どこかで見たような……\x02\x03",

            "……いや……そんな筈は………\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x104,
        (
            "#0306Fおいおい、勘弁してくれよ。\x02\x03",

            "グラマーな姉ちゃんならともかく\x01",
            "オッサンに言い寄られる趣味はねえぞ？\x02",
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
            "#3104F……フン、まあいいだろう。\x02\x03",

            "#3100F目障りだ、とっとと失せろ。\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x104,
        (
            "#0301Fハッ……\x01",
            "そっちが引き止めたんだろうが。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x104, 0xB4, 0x1F4)

    def lambda_2099():
        OP_95(0xFE, 0, 0, 50000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2099)
    FadeToDark(2000, 0, -1)
    Sleep(500)

    def lambda_20C0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_20C0)
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

    # Function_9_B3A end

    def Function_10_2120(): pass

    label("Function_10_2120")

    OP_93(0xFE, 0xB4, 0x1F4)

    def lambda_212C():
        OP_95(0xFE, 2000, 0, 54200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_212C)
    WaitChrThread(0xFE, 1)

    def lambda_214A():
        OP_95(0xFE, 0, 0, 52200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_214A)
    WaitChrThread(0xFE, 1)

    def lambda_2168():
        OP_95(0xFE, 0, 0, 50000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2168)
    Sleep(500)

    def lambda_2185():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2185)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_10_2120 end

    def Function_11_2196(): pass

    label("Function_11_2196")

    OP_93(0xFE, 0xB4, 0x1F4)

    def lambda_21A2():
        OP_95(0xFE, -2000, 0, 54200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_21A2)
    WaitChrThread(0xFE, 1)

    def lambda_21C0():
        OP_95(0xFE, 0, 0, 52200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_21C0)
    WaitChrThread(0xFE, 1)

    def lambda_21DE():
        OP_95(0xFE, 0, 0, 50000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_21DE)
    Sound(103, 0, 100, 0)
    Sleep(500)

    def lambda_2201():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2201)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_11_2196 end

    def Function_12_2212(): pass

    label("Function_12_2212")

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
            "#1K同日、１１：００──\x02",
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
            "#0608F#11Pクッ……\x01",
            "一体どうなっている……\x02\x03",

            "#0610Fルバーチェめ……\x01",
            "何をしようとしてるんだ！？\x02",
        )
    )

    CloseMessageWindow()
    Sound(103, 0, 100, 0)
    Sleep(300)
    OP_63(0x10A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_2470():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10A, 2, lambda_2470)
    OP_68(110, 1100, 3690, 2000)
    MoveCamera(45, 19, 0, 2000)
    SetCameraDistance(20000, 2000)

    def lambda_24A2():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_24A2)

    def lambda_24B3():
        OP_96(0xFE, 0xFFFFFE0C, 0x0, 0x834, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_24B3)
    Sleep(400)

    def lambda_24D0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_24D0)

    def lambda_24E1():
        OP_96(0xFE, 0x1F4, 0x0, 0x834, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_24E1)
    Sleep(400)

    def lambda_24FE():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_24FE)

    def lambda_250F():
        OP_96(0xFE, 0xFFFFFD44, 0x0, 0x44C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_250F)
    Sleep(400)

    def lambda_252C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_252C)

    def lambda_253D():
        OP_96(0xFE, 0x2BC, 0x0, 0x44C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_253D)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    OP_6F(0x79)

    #C0068
    ChrTalk(
        0x10A,
        "#5P#0605Fお、お前たち……！？\x02",
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x101,
        (
            "#12P#0000Fやっぱり中にいたのは\x01",
            "ダドリーさんでしたか……\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x104,
        (
            "#0301F#12Pおいおい。\x01",
            "一体どうなってんだよ？\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x10A,
        (
            "#5P#0607Fええい、首を突っ込むなと\x01",
            "言ったばかりだろうが！？\x02\x03",

            "お前たちは薬物捜査の方に\x01",
            "専念していれば──\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0x102,
        (
            "#0106F#12Pお言葉ですが、そんな事を\x01",
            "言ってる場合でしょうか？\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0x103,
        (
            "#12P#0201F……やっぱり中に\x01",
            "誰もいないみたいですね？\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x10A,
        "#5P#0610Fくっ……\x02",
    )

    CloseMessageWindow()
    OP_63(0x10A, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1200)

    #C0075
    ChrTalk(
        0x10A,
        (
            "#5P#0603F……先程から大声で呼んでいるが\x01",
            "誰一人として出てくる気配がない。\x02\x03",

            "かといって争った形跡が\x01",
            "あるわけでもない……\x02\x03",

            "#0610F一体どうなっているか\x01",
            "こちらが聞きたいくらいだ……ッ！\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x101,
        (
            "#12P#0001F確か一課は、ルバーチェの動向を\x01",
            "監視していたはずですよね？\x02\x03",

            "マフィアたちがいつ消えたのか\x01",
            "把握できていないんですか？\x02",
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
            "#5P#0603F……昨晩、警察本部に\x01",
            "犯行予告が届けられた。\x02\x03",

            "クロスベル空港に爆発物を\x01",
            "仕掛けるという予告だ。\x02",
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
        "#12P#0011Fば、爆発物！？\x02",
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0x102,
        "#0105F#12Pそ、そんな事が……！？\x02",
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0x10A,
        (
            "#5P#0603F急遽、一課の人間が集められ、\x01",
            "空港での警戒に当たる事となった。\x02\x03",

            "#0601F……上からの指示で\x01",
            "ルバーチェを監視していた人員を\x01",
            "そちらに回すという形でな。\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x101,
        "#12P#0013Fあ……\x02",
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x104,
        (
            "#0306F#12Pそれで監視が引き上げた後に\x01",
            "消えちまったってわけか……\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x103,
        (
            "#12P#0203F……怪しいですね。\x02\x03",

            "#0211Fその爆発物の予告は\x01",
            "どこまで本当なんでしょうか？\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0x10A,
        (
            "#5P#0603Fさてな……\x02\x03",

            "#0608F……クッ、上の連中も\x01",
            "いったい何を考えている……！\x02\x03",

            "どこまで警察の誇りを\x01",
            "踏みにじるつもりだ……！？\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x102,
        "#0108F#12Pダドリー捜査官……\x02",
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
            "#12P#0003F──いずれにしても\x01",
            "このままでは何が起きているのか\x01",
            "把握することすら困難です。\x02\x03",

            "#0001Fここは建物内部を\x01",
            "一通り調べてみませんか？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x10A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0089
    ChrTalk(
        0x10A,
        "#5P#0607Fおい……！？\x02",
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x101,
        (
            "#12P#0006F警察とルバーチェの微妙な関係は\x01",
            "もちろん自分も分かっています。\x02\x03",

            "捜査令状がない状態で家捜ししたら\x01",
            "どんな反撃材料を相手に与えるか……\x02\x03",

            "#0001Fそのリスクも承知しています。\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x102,
        "#0108F#12Pロイド……\x02",
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0x10A,
        (
            "#5P#0610Fクッ……だったら何故、\x01",
            "そんな無謀なことを言い出す！？\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x101,
        (
            "#12P#0003F“それ所ではない状況”に\x01",
            "なっている可能性が高いからです。\x02\x03",

            "#0001F──昨日から今朝にかけて\x01",
            "明らかになった事をお伝えします。\x02",
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
            "蒼い錠剤が、６年前に壊滅した\x01",
            "狂気の教団が作り出した薬物である\x01",
            "可能性が出てきたこと……\x02\x03",

            "そして薬を使用していた人間たちが\x01",
            "一斉に姿を消したことを説明した。\x07\x00\x02",
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
            "#5P#0605Fし、信じられん……\x02\x03",

            "その教団の話は聞いた事があるが\x01",
            "てっきり壊滅したものかと……\x02\x03",

            "#0608F……いや、しかし……\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0x101,
        (
            "#12P#0001F事は人命に関わる話です。\x02\x03",

            "もしかしたら失踪者たちの情報が\x01",
            "ここに残されているかもしれません。\x02\x03",

            "#0003Fダドリーさんが納得できないのなら\x01",
            "せめて俺たちの……\x02\x03",

            "#0013Fいや──俺の独断専行を\x01",
            "このまま見逃してくれませんか？\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0x10A,
        "#5P#0605F…………………………………\x02",
    )

    CloseMessageWindow()

    def lambda_309B():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_309B)
    Sleep(100)
    TurnDirection(0x102, 0x101, 500)

    #C0098
    ChrTalk(
        0x104,
        (
            "#0306F#11Pおいおい、自分ひとりで\x01",
            "責任を被ろうとしてんじゃねえよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0x102,
        (
            "#0100F#11P当然、私たちも付き合うわ。\x02\x03",

            "支援課が取り潰されたとしても\x01",
            "見過ごせる状況じゃないもの。\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0x103,
        "#12P#0204Fええ、一連托生です。\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0xB3, 0x1F4)

    #C0101
    ChrTalk(
        0x101,
        "#5P#0000Fみんな……\x02",
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x10A,
        (
            "#5P#0603F……フン……\x01",
            "血は争えないものだな。\x02\x03",

            "#0602Fその強引さ……\x01",
            "ヤツにそっくりじゃないか。\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0x101,
        "#5P#0005Fえ……\x02",
    )

    CloseMessageWindow()

    def lambda_321A():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_321A)
    Sleep(50)

    def lambda_322A():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_322A)
    Sleep(50)

    def lambda_323A():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_323A)
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
            "#5P#0611F──違法捜査による証拠物件は\x01",
            "法的な証拠能力を認められない。\x02\x03",

            "連中がどんな証拠を残していても\x01",
            "見て見ぬフリをする必要があるぞ？\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0x101,
        (
            "#12P#0006Fそれは……構いません。\x02\x03",

            "#0008F今、必要なのは\x01",
            "このクロスベル市において\x01",
            "何が起こりつつあるのか……\x02\x03",

            "#0013Fそれを見極めることですから。\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0x10A,
        "#5P#0611Fフン、一丁前の口を利く……\x02",
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
            "#5P#0604Fだが、それが分かっているなら\x01",
            "とやかく言うつもりはない。\x02\x03",

            "#0602Fせいぜい足手まといにならないよう\x01",
            "付いて来るがいい。\x02",
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
        "#12P#0011Fえ……\x02",
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0x102,
        (
            "#0105F#12Pその……\x01",
            "見逃してくれるだけでは？\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0x10A,
        (
            "#5P#0603Fこの状況、\x01",
            "お前たちのようなヒヨッ子どもに\x01",
            "任せきりに出来るとでも思うか？\x02\x03",

            "#0601F今からお前たちには\x01",
            "私の指揮下に入ってもらう。\x02\x03",

            "#0607F全ての責任は私が持つ……\x01",
            "反論は許さん！\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0x101,
        "#12P#0002Fダドリーさん……\x02",
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0x104,
        (
            "#0300F#12Pやれやれ……\x01",
            "ホント素直じゃないっつーか。\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0x103,
        (
            "#12P#0204Fやはり照れ隠しの\x01",
            "一種ではないかと……\x02",
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
            "#11P#0603Fええい、うるさい！\x02\x03",

            "#0601F──まずは建物内を\x01",
            "一通り捜索してゆく……\x02\x03",

            "異常があればすぐに報告しろ。\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0x101,
        "#12P#0000Fはい……！\x02",
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
            "ダドリー捜査官がパーティに加入しました。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #A0117
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "キャンプメニューの[TACTICS]で\x01",
            "アタックメンバーに加える事が出来ます。\x07\x00\x02",
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

    # Function_12_2212 end

    def Function_13_3874(): pass

    label("Function_13_3874")

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
            "#0001Fここは……\x01",
            "前に通された応接間か。\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0x104,
        "#0301F無駄に豪華な調度だよな。\x02",
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0x10A,
        (
            "#5P#0601Fフン、まさかこんな場所に\x01",
            "犯罪の証拠は無いだろうが……\x02",
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
            "#0101Fティオちゃん……\x01",
            "何か感じたの？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3A57():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3A57)
    Sleep(50)

    def lambda_3A67():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_3A67)
    Sleep(50)
    TurnDirection(0x10A, 0x103, 500)

    #C0122
    ChrTalk(
        0x103,
        (
            "#12P#0206Fええ、前に通された時にも\x01",
            "少し感じたのですが……\x02\x03",

            "#0201Fこの部屋、何か仕掛けが\x01",
            "ありそうな気配がします。\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0x101,
        "#5P#0005F仕掛けのある気配……？\x02",
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0x10A,
        "#5P#0601Fどういう事だ？\x02",
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0x103,
        (
            "#12P#0208F何か機械的なギミックが\x01",
            "存在しているような……\x02\x03",

            "#0206F……すみません。\x01",
            "気のせいかもしれませんが。\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0x104,
        (
            "#0300Fいや、ティオすけの見立てに\x01",
            "ハズレはあり得ねぇだろ。\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0x101,
        (
            "#5P#0000Fああ……\x01",
            "少し調べてみるか。\x02",
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

    # Function_13_3874 end

    def Function_14_3C2E(): pass

    label("Function_14_3C2E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3C40")
    Call(0, 17)
    Jump("loc_3CFF")

    label("loc_3C40")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3C56")
    Call(0, 15)
    Jump("loc_3CFF")

    label("loc_3C56")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3C6C")
    Call(0, 16)
    Jump("loc_3CFF")

    label("loc_3C6C")

    TalkBegin(0xFF)
    SetChrName("")
    FadeToDark(300, 0, 100)

    #A0128
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "２つの差込み口のような物が並んでいる。\x02",
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
            "#0000Fこれが鍵穴だとすれば……\x01",
            "どこかに鍵が隠されているはずだな。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFF)

    label("loc_3CFF")

    Return()

    # Function_14_3C2E end

    def Function_15_3D00(): pass

    label("Function_15_3D00")

    EventBegin(0x2)
    Sleep(500)
    Sound(141, 0, 100, 0)
    SetChrName("")

    #A0130
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "紅耀石の鍵を差し込んだ。\x01\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SubItemNumber(0x32E, 1)
    Fade(250)
    SetMapObjFrame(0xFF, "key_red", 0x1, 0x1)
    Sleep(500)
    SetScenarioFlags(0xC6, 6)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3D67")
    Call(0, 18)
    Jump("loc_3D69")

    label("loc_3D67")

    EventEnd(0x3)

    label("loc_3D69")

    Return()

    # Function_15_3D00 end

    def Function_16_3D6A(): pass

    label("Function_16_3D6A")

    EventBegin(0x2)
    Sleep(500)
    Sound(141, 0, 100, 0)
    SetChrName("")

    #A0131
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "蒼耀石の鍵を差し込んだ。\x01\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SubItemNumber(0x32C, 1)
    Fade(250)
    SetMapObjFrame(0xFF, "key_blue", 0x1, 0x1)
    Sleep(500)
    SetScenarioFlags(0xC6, 7)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3DD2")
    Call(0, 18)
    Jump("loc_3DD4")

    label("loc_3DD2")

    EventEnd(0x3)

    label("loc_3DD4")

    Return()

    # Function_16_3D6A end

    def Function_17_3DD5(): pass

    label("Function_17_3DD5")

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
        "#0005Fあれ、この絵……\x02",
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0x10A,
        (
            "#12P#0601Fフン……臭いな。\x02\x03",

            "調べてみろ。\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0x101,
        "#0001Fはい──\x02",
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
        "#6P#0105Fこれは……\x02",
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0x104,
        (
            "#0304F#6Pティオすけのカン的中だな。\x02\x03",

            "#0305Fなんか差込み口みてぇなのが\x01",
            "２つ付いてるみてぇだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0x103,
        (
            "#6P#0203F何らかの“鍵”の\x01",
            "差し込み口ではないかと。\x02\x03",

            "#0202F両方解除したら何か\x01",
            "起きるかもしれませんね。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_409E")

    #C0138
    ChrTalk(
        0x101,
        (
            "#0000F#5Pよし……\x01",
            "（さっきの鍵を試してみるか）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_40CE")

    label("loc_409E")


    #C0139
    ChrTalk(
        0x101,
        (
            "#0000F#5Pよし……\x01",
            "見つけたら試してみよう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_40CE")

    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, 6400, 0, 60800, 90)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetScenarioFlags(0xC4, 3)
    OP_29(0x4C, 0x1, 0xE)
    EventEnd(0x5)
    Return()

    # Function_17_3DD5 end

    def Function_18_40F8(): pass

    label("Function_18_40F8")

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

    def lambda_41AC():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_41AC)
    Sleep(50)

    def lambda_41BC():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10A, 2, lambda_41BC)

    def lambda_41C9():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_41C9)
    Sleep(50)

    def lambda_41D9():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_41D9)

    def lambda_41E6():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_41E6)
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
            "#5P#0105Fま、まさかこの部屋に\x01",
            "こんな仕掛けがあったなんて……\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0x101,
        (
            "#0006F#5Pしかも足跡を見る限り、\x01",
            "頻繁に使っていそうだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0x10A,
        (
            "#0603F#11Pフン、マルコーニあたりが\x01",
            "嬉々として使ってるんだろう。\x02\x03",

            "#0601Fとなると……\x01",
            "この先がヤツの私室か……？\x02",
        )
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0x104,
        (
            "#0303F#5Pそういや、会長室とか\x01",
            "それっぽいのは無かったよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0x103,
        (
            "#5P#0201Fこの先に、何か手がかりが\x01",
            "あるかもしれませんね。\x02",
        )
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0x101,
        "#0001F#5Pよし……降りてみよう。\x02",
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

    # Function_18_40F8 end

    def Function_19_442A(): pass

    label("Function_19_442A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_443C")
    Call(0, 20)
    Jump("loc_4530")

    label("loc_443C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 5)), scpexpr(EXPR_END)), "loc_444D")
    Call(0, 23)
    Jump("loc_4530")

    label("loc_444D")

    TalkBegin(0xFF)
    SetChrName("")
    FadeToDark(300, 0, 100)

    #A0146
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "文字の入力パネルがある。\x01",
            "どうやらパスワードの入力装置のようだ。\x02",
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
            "#0603Fフン、適当に入力して\x01",
            "開くものでは無さそうだな。\x02\x03",

            "#0601Fパスワードの手がかりが無いか、\x01",
            "このビル内を捜索してみるぞ！\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFF)

    label("loc_4530")

    Return()

    # Function_19_442A end

    def Function_20_4531(): pass

    label("Function_20_4531")

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
        "#11P#0005Fこれは……\x02",
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0x102,
        (
            "#12P#0101Fそれは……\x01",
            "文字の入力パネル？\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0x103,
        (
            "#12P#0203Fおそらくパスワードの\x01",
            "入力装置ではないかと……\x02",
        )
    )

    CloseMessageWindow()
    OP_68(-59500, 1000, 700, 1500)
    Sleep(500)

    def lambda_4663():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_4663)
    OP_6F(0x1)

    #C0151
    ChrTalk(
        0x103,
        (
            "#11P#0202F……思わせぶりな\x01",
            "鉄格子もある事ですし。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_46A9():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_46A9)
    Sleep(50)

    def lambda_46B9():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_46B9)
    Sleep(50)

    def lambda_46C9():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10A, 2, lambda_46C9)
    Sleep(50)
    OP_93(0x104, 0x10E, 0x1F4)

    #C0152
    ChrTalk(
        0x104,
        (
            "#0306Fつうか露骨に\x01",
            "怪しすぎんだろ……\x02",
        )
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0x10A,
        (
            "#0603F#11P#Nフン、適当に入力して\x01",
            "開くものでは無さそうだな。\x02\x03",

            "#0608F書き置きでも残してあれば\x01",
            "何とかなりそうだが……\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0154
    ChrTalk(
        0x101,
        (
            "#0000F#11P#Nそうですね……\x01",
            "捜してみましょう。\x02",
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

    # Function_20_4531 end

    def Function_21_47DA(): pass

    label("Function_21_47DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_47EC")
    Call(0, 22)
    Jump("loc_4880")

    label("loc_47EC")

    TalkBegin(0xFF)
    SetChrName("")

    #A0155
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "グラビア誌のページに\x01",
            "一枚のメモが挟まっている。\x07\x00\x02",
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
            "『図書館で一番人気の童話の\x01",
            "  タイトルと著者名』\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)

    label("loc_4880")

    Return()

    # Function_21_47DA end

    def Function_22_4881(): pass

    label("Function_22_4881")

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
            "机の上にグラビア誌が置かれている。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0158
    ChrTalk(
        0x101,
        (
            "#5P#0005Fこれは……\x01",
            "マフィアの手下たちが\x01",
            "読んでいた雑誌か？\x02",
        )
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0x104,
        (
            "#11P#0302Fああ、俺も愛読してる\x01",
            "『ホットショット』の最新号だな。\x02\x03",

            "#0309Fパラパラ……\x01",
            "うーん、眼福眼福。\x02",
        )
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0x102,
        "#5P#0111Fランディ……貴方ね。\x02",
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0x103,
        "#0206F#5Pまあ、ランディさんですし。\x02",
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0x10A,
        "#0606F#11Pまったく、今時の若い連中は……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0163
    ChrTalk(
        0x101,
        (
            "#5P#0005Fあれ……\x02\x03",

            "#0001F今、何かページに\x01",
            "挟まっていなかったか？\x02",
        )
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0x104,
        (
            "#11P#0301Fん……？\x02\x03",

            "#0305F……おお。\x01",
            "メモが挟まってんな。\x02",
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
            "グラビア誌のページに\x01",
            "一枚のメモが挟まっている。\x07\x00\x02",
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
            "『図書館で一番人気の童話の\x01",
            "  タイトルと著者名』\x07\x00\x02",
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
        "#5P#0101Fこれって……\x02",
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0x103,
        (
            "#0201F#5P……もしかして下の部屋の\x01",
            "パスワードのメモでしょうか？\x02",
        )
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0x10A,
        (
            "#0604F#11Pフン……\x01",
            "いかにもありそうだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0x101,
        (
            "#5P#0000Fええ、１階の入力装置で\x01",
            "色々と試してみましょう。\x02",
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

    # Function_22_4881 end

    def Function_23_4D0B(): pass

    label("Function_23_4D0B")

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
            "#1K２種類のパスワードを\x01",
            "連続で入力してください\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "リーネと７匹の竜\x01",          # 0
            "王妃カロン物語\x01",            # 1
            "アリューゼ放浪記\x01",          # 2
            "マルクと深き森の魔女\x01",      # 3
            "リデル童話集\x01",              # 4
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4E66")
    ClearScenarioFlags(0x0, 0)

    label("loc_4E66")


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "アリー・ベイ\x01",            # 0
            "ショーン・アルナム\x01",      # 1
            "ヨーコ・アッシマー\x01",      # 2
            "アマニタ・ハイム\x01",        # 3
            "レイチェル・ブラン\x01",      # 4
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4EE1")
    ClearScenarioFlags(0x0, 0)

    label("loc_4EE1")

    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_5254")
    Sound(87, 0, 100, 0)
    Sleep(300)
    OP_68(-59500, 1000, 700, 1500)
    Sleep(500)

    def lambda_4F16():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4F16)
    Sleep(50)

    def lambda_4F26():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_4F26)
    Sleep(50)

    def lambda_4F36():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10A, 2, lambda_4F36)
    Sleep(50)

    def lambda_4F46():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_4F46)
    Sleep(50)

    def lambda_4F56():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_4F56)
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
            "#0000F#11Pよかった……\x01",
            "合ってたみたいだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0x102,
        (
            "#11P#0102Fふふ、凝った仕掛けの割には\x01",
            "ちょっと迂闊だったわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0x104,
        (
            "#0306F#11Pああ、あんなグラビア誌に\x01",
            "大事な情報を挟むなっつーの。\x02\x03",

            "#0301Fすぐに侵入者に\x01",
            "見つかっちまうじゃねえか。\x02",
        )
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0x103,
        (
            "#11P#0206F普通の侵入者はグラビア誌を\x01",
            "パラパラめくらないと思いますが……\x02",
        )
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0x10A,
        (
            "#11P#0604Fまあ、どんなセキュリティも\x01",
            "運用する人間次第ということだ。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10A, 0x103, 500)
    Sleep(300)

    #C0177
    ChrTalk(
        0x10A,
        (
            "#5P#0600F──行くぞ。\x01",
            "この先は何かありそうだ。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_51F0():
        TurnDirection(0xFE, 0x10A, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_51F0)
    Sleep(150)

    def lambda_5200():
        TurnDirection(0xFE, 0x10A, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_5200)
    Sleep(50)

    def lambda_5210():
        TurnDirection(0xFE, 0x10A, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_5210)
    Sleep(50)
    TurnDirection(0x104, 0x10A, 500)

    #C0178
    ChrTalk(
        0x101,
        "#6P#0000Fええ……！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_65(0x3, 0x1)
    OP_65(0x4, 0x1)
    SetScenarioFlags(0xC4, 6)
    OP_29(0x4C, 0x1, 0x10)
    Jump("loc_525D")

    label("loc_5254")

    Sound(3, 0, 100, 0)
    Sleep(300)

    label("loc_525D")

    SetChrPos(0x0, -57000, 0, 400, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_23_4D0B end

    def Function_24_527B(): pass

    label("Function_24_527B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_528D")
    Call(0, 25)
    Jump("loc_5318")

    label("loc_528D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_52A3")
    Call(0, 28)
    Jump("loc_5318")

    label("loc_52A3")

    TalkBegin(0xFF)
    SetChrName("")
    FadeToDark(300, 0, 100)

    #A0179
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "本棚には不自然に隙間が空いている。\x01",
            "どうやら感圧式の仕掛けが隠されているようだ。\x02",
        )
    )

    CloseMessageWindow()
    FadeToBright(300, 0)
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)

    label("loc_5318")

    Return()

    # Function_24_527B end

    def Function_25_5319(): pass

    label("Function_25_5319")

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
            "#0005F#12Pん……？\x02\x03",

            "#0001Fなんだか不自然に\x01",
            "隙間が空いているな……\x02",
        )
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0x102,
        (
            "#12P#0105F誰かここの本を\x01",
            "持っていったのかしら？\x02",
        )
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0x103,
        "#6P#0201Fいえ……\x02",
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x103)

    #C0183
    ChrTalk(
        0x103,
        (
            "#6P#0203F──どうやら感圧装置が\x01",
            "下に仕込まれているようです。\x02\x03",

            "#0200F特定の重さの物体を置いたら\x01",
            "解除される仕掛けみたいですね。\x02",
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
            "#12P#0306Fおいおい……\x01",
            "どこのスパイ小説だよ？\x02",
        )
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0x10A,
        (
            "#0603F#12Pフン……\x01",
            "セキュリティのつもりか。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x10A, 0x10E, 0x1F4)
    Sleep(300)

    #C0186
    ChrTalk(
        0x10A,
        (
            "#0601F#11Pだったら話は早い。\x01",
            "それらしい“重り”がないか\x01",
            "ビル内を調べてみるぞ。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x5A, 0x1F4)

    #C0187
    ChrTalk(
        0x101,
        "#5P#0000F分かりました！\x02",
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

    # Function_25_5319 end

    def Function_26_565C(): pass

    label("Function_26_565C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5669")
    Call(0, 27)

    label("loc_5669")

    Return()

    # Function_26_565C end

    def Function_27_566A(): pass

    label("Function_27_566A")

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
            "金色の台座が置いてある。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_57E4")

    #C0189
    ChrTalk(
        0x101,
        (
            "#0005F#11Pこの台座は……\x01",
            "金で出来ているのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0x102,
        (
            "#12P#0101Fううん、他の金属に\x01",
            "メッキしただけみたいね。\x02\x03",

            "#0103Fルバーチェの資産力なら\x01",
            "本物があっても\x01",
            "おかしくない筈だけど……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_57E4")

    FadeToDark(300, 0, 100)
    OP_0D()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【台座を持っていく】\x01",        # 0
            "【そのままにしておく】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_584A"),
        (1, "loc_58C6"),
        (SWITCH_DEFAULT, "loc_58CB"),
    )


    label("loc_584A")

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
            scpstr(SCPSTR_CODE_ITEM, 0x32D),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x32D, 1)
    OP_65(0x6, 0x1)
    SetScenarioFlags(0xC6, 5)
    Jump("loc_58CB")

    label("loc_58C6")

    Jump("loc_58CB")

    label("loc_58CB")

    SetScenarioFlags(0xC5, 3)
    SetChrPos(0x0, 200, 0, 64400, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_27_566A end

    def Function_28_58EC(): pass

    label("Function_28_58EC")

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
    SubItemNumber(0x32D, 1)
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

    def lambda_59F5():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_59F5)
    Sleep(50)

    def lambda_5A05():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10A, 2, lambda_5A05)

    def lambda_5A12():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_5A12)
    Sleep(50)

    def lambda_5A22():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_5A22)

    def lambda_5A2F():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_5A2F)
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
        "#5P#0000Fよし……！\x02",
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0x104,
        (
            "#6P#0306Fしかしまあ、\x01",
            "随分と趣味的な仕掛けだな。\x02\x03",

            "#0301F何で普通の鍵にしないんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0194
    ChrTalk(
        0x103,
        (
            "#6P#0211Fしかも結構なミラが\x01",
            "掛かっている仕掛けですね。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x10A, 0x10E, 0x1F4)

    #C0195
    ChrTalk(
        0x10A,
        (
            "#0603F#11P恐らくマルコーニの趣味だろう。\x02\x03",

            "#0600F目新しくケレン味のあるものが\x01",
            "とにかく好きだと聞いている。\x02",
        )
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0x102,
        (
            "#6P#0106F付き合わされる下の人間は\x01",
            "大変かもしれませんね……\x02",
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

    # Function_28_58EC end

    SaveToFile()

Try(main)
