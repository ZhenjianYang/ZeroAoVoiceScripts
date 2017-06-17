from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c0140.bin",                # FileName
        "c0140",                    # MapName
        "c0140",                    # Location
        0x0006,                     # MapIndex
        "ed7100",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 6, 0, 2, 0, 3],
    )

    BuildStringList((
        "c0140",                  # 0
        "チャコ",                 # 1
        "ウェンディ",             # 2
        "フェルナンド",           # 3
        "ミゼット",               # 4
        "バジリオ",               # 5
    ))

    AddCharChip((
        "chr/ch26100.itc",                   # 00
        "chr/ch27800.itc",                   # 01
        "chr/ch25700.itc",                   # 02
        "chr/ch21000.itc",                   # 03
        "chr/ch20800.itc",                   # 04
        "chr/ch21900.itc",                   # 05
    ))

    DeclNpc(9270,    0,       2650,    270,  261,  0x0, 0,   2,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(9329,    0,       -1350,   270,  261,  0x0, 0,   0,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(-1519,   0,       14659,   180,  261,  0x0, 0,   1,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(-4480,   0,       7440,    0,    261,  0x0, 0,   5,   0,   0,   0,   0,   13,  255,  0)
    DeclNpc(2299,    0,       6420,    90,   261,  0x0, 0,   3,   0,   0,   0,   0,   14,  255,  0)

    DeclActor(8130,    0,       3080,    1000,    9270,    1500,    2650,    0x007E, 0,  4,  0x0000)
    DeclActor(8310,    0,       -1360,   1000,    9330,    1500,    -1350,   0x007E, 0,  7,  0x0000)

    ScpFunction((
        "Function_0_1C8",          # 00, 0
        "Function_1_280",          # 01, 1
        "Function_2_3D1",          # 02, 2
        "Function_3_570",          # 03, 3
        "Function_4_5A4",          # 04, 4
        "Function_5_76E",          # 05, 5
        "Function_6_FCB",          # 06, 6
        "Function_7_1ABF",         # 07, 7
        "Function_8_1AC3",         # 08, 8
        "Function_9_299C",         # 09, 9
        "Function_10_4200",        # 0A, 10
        "Function_11_4A93",        # 0B, 11
        "Function_12_4D90",        # 0C, 12
        "Function_13_5A3A",        # 0D, 13
        "Function_14_6403",        # 0E, 14
        "Function_15_7053",        # 0F, 15
        "Function_16_737B",        # 10, 16
        "Function_17_7F79",        # 11, 17
    ))


    def Function_0_1C8(): pass

    label("Function_0_1C8")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_208"),
        (1, "loc_214"),
        (2, "loc_220"),
        (3, "loc_22C"),
        (4, "loc_238"),
        (5, "loc_244"),
        (6, "loc_250"),
        (SWITCH_DEFAULT, "loc_25C"),
    )


    label("loc_208")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_268")

    label("loc_214")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_268")

    label("loc_220")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_268")

    label("loc_22C")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_268")

    label("loc_238")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_268")

    label("loc_244")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_268")

    label("loc_250")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_268")

    label("loc_25C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_268")

    label("loc_268")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_27F")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_268")

    label("loc_27F")

    Return()

    # Function_0_1C8 end

    def Function_1_280(): pass

    label("Function_1_280")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3D0")
    OP_95(0xFE, -4480, 0, 9380, 2000, 0x0)
    OP_95(0xFE, -1380, 0, 11120, 2000, 0x0)
    OP_95(0xFE, 5230, 0, 9480, 2000, 0x0)
    OP_95(0xFE, 5230, 0, 9480, 2000, 0x0)
    OP_95(0xFE, 5230, 0, 6900, 2000, 0x0)
    OP_93(0xFE, 0x10E, 0x190)
    Sleep(1300)
    OP_93(0xFE, 0xB4, 0x190)
    Sleep(100)
    OP_95(0xFE, 5230, 0, 1000, 2000, 0x0)
    OP_95(0xFE, 3800, 0, 930, 2000, 0x0)
    OP_93(0xFE, 0xB4, 0x190)
    Sleep(2000)
    OP_93(0xFE, 0x10E, 0x190)
    Sleep(100)
    OP_95(0xFE, -1350, 0, 930, 2000, 0x0)
    OP_95(0xFE, -1310, 0, -1230, 2000, 0x0)
    OP_93(0xFE, 0x5A, 0x190)
    Sleep(2000)
    OP_93(0xFE, 0x0, 0x190)
    Sleep(100)
    OP_95(0xFE, -1310, 0, 2990, 2000, 0x0)
    OP_95(0xFE, -4480, 0, 4640, 2000, 0x0)
    OP_95(0xFE, -4480, 0, 7440, 2000, 0x0)
    OP_93(0xFE, 0x5A, 0x190)
    Sleep(1800)
    OP_93(0xFE, 0x0, 0x190)
    Sleep(100)
    Jump("Function_1_280")

    label("loc_3D0")

    Return()

    # Function_1_280 end

    def Function_2_3D1(): pass

    label("Function_2_3D1")

    BeginChrThread(0xB, 0, 0, 1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_3EC")
    OP_93(0xA, 0x0, 0x0)
    Jump("loc_55D")

    label("loc_3EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_40B")
    SetChrPos(0xC, 11460, 4000, 8870, 90)
    Jump("loc_55D")

    label("loc_40B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_419")
    Jump("loc_55D")

    label("loc_419")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_END)), "loc_427")
    Jump("loc_55D")

    label("loc_427")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_43A")
    SetChrFlags(0xC, 0x80)
    Jump("loc_55D")

    label("loc_43A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_448")
    Jump("loc_55D")

    label("loc_448")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_467")
    SetChrPos(0xC, 11460, 4000, 8870, 90)
    Jump("loc_55D")

    label("loc_467")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_486")
    SetChrPos(0xC, 11460, 4000, 8870, 90)
    Jump("loc_55D")

    label("loc_486")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_4A5")
    SetChrPos(0xA, 11420, 4000, 7630, 270)
    Jump("loc_55D")

    label("loc_4A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_4B3")
    Jump("loc_55D")

    label("loc_4B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_4C1")
    Jump("loc_55D")

    label("loc_4C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_4E0")
    SetChrPos(0xC, -4700, 0, -1320, 90)
    Jump("loc_55D")

    label("loc_4E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_527")
    SetChrPos(0xA, 820, 0, 850, 270)
    SetChrPos(0xB, -530, 0, 850, 90)
    BeginChrThread(0xB, 0, 0, 0)
    SetChrPos(0xC, 11800, 4000, -1260, 90)
    Jump("loc_55D")

    label("loc_527")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_546")
    SetChrPos(0xC, 11460, 4000, 8870, 90)
    Jump("loc_55D")

    label("loc_546")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_554")
    Jump("loc_55D")

    label("loc_554")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_55D")

    label("loc_55D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_56F")
    Event(0, 15)

    label("loc_56F")

    Return()

    # Function_2_3D1 end

    def Function_3_570(): pass

    label("Function_3_570")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_58C")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    Jump("loc_5A3")

    label("loc_58C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_5A3")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    Jump("loc_5A3")

    label("loc_5A3")

    Return()

    # Function_3_570 end

    def Function_4_5A4(): pass

    label("Function_4_5A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF1, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_764")
    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x71, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6A9")

    #C0001
    ChrTalk(
        0x8,
        (
            "あ、ウェンディ先輩の\x01",
            "お友達の人たちですよね～。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x8,
        (
            "知ってます～？\x01",
            "最近、戦術オーブメントの\x01",
            "カバー交換サービスを始めたんですぅ。\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0x8,
        (
            "オシャレなデザインを\x01",
            "いくつも揃えてるですよ～。\x01",
            "ぜひ見ていって欲しいですぅ～。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x71, 4)

    label("loc_6A9")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6B3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_75C")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "話をする\x01",                # 0
            "カバーの交換をする\x01",      # 1
            "やめる\x01",                  # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_717")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_717")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_738")
    Call(0, 6)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_757")

    label("loc_738")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_757")
    OP_60(0x0)
    Call(0, 5)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_757")

    Jump("loc_6B3")

    label("loc_75C")

    TalkEnd(0x8)
    Jump("loc_76D")

    label("loc_764")

    TalkBegin(0x8)
    Call(0, 6)
    TalkEnd(0x8)

    label("loc_76D")

    Return()

    # Function_4_5A4 end

    def Function_5_76E(): pass

    label("Function_5_76E")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_778")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FCA")
    MenuCmd(0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 5)), scpexpr(EXPR_END)), "loc_7BE")
    MenuCmd(1, 0, "ブルーシェリフ　　　　購入済み")
    MenuCmd(3, 0, 0x0)
    Jump("loc_7E0")

    label("loc_7BE")

    MenuCmd(1, 0, "ブルーシェリフ　　　　1000ミラ")

    label("loc_7E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 6)), scpexpr(EXPR_END)), "loc_814")
    MenuCmd(1, 0, "ピースグリーン　　　　購入済み")
    MenuCmd(3, 0, 0x1)
    Jump("loc_836")

    label("loc_814")

    MenuCmd(1, 0, "ピースグリーン　　　　1000ミラ")

    label("loc_836")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 7)), scpexpr(EXPR_END)), "loc_86A")
    MenuCmd(1, 0, "ブラックキャット　　　購入済み")
    MenuCmd(3, 0, 0x2)
    Jump("loc_88C")

    label("loc_86A")

    MenuCmd(1, 0, "ブラックキャット　　　1000ミラ")

    label("loc_88C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF1, 0)), scpexpr(EXPR_END)), "loc_8C0")
    MenuCmd(1, 0, "デンジャーオレンジ　　購入済み")
    MenuCmd(3, 0, 0x3)
    Jump("loc_8E2")

    label("loc_8C0")

    MenuCmd(1, 0, "デンジャーオレンジ　　1000ミラ")

    label("loc_8E2")

    MenuCmd(1, 0, "やめる")

    #A0004
    AnonymousTalk(
        0x8,
        (
            scpstr(0x18),
            "どれに交換しますか～？\x02",
        )
    )

    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_937")
    Sleep(1)
    Return()

    label("loc_937")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_977")
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis172.itp")
    Jump("loc_A32")

    label("loc_977")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9B7")
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis173.itp")
    Jump("loc_A32")

    label("loc_9B7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9F7")
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis174.itp")
    Jump("loc_A32")

    label("loc_9F7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A32")
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis175.itp")

    label("loc_A32")

    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AEB")

    #A0005
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "このカバーはロイド専用です。\x01",
            "購入するとキャンプメニューの[ORBMENT]で表示される\x01",
            "戦術オーブメントのカバーが変わります。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CA1")

    label("loc_AEB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B7E")

    #A0006
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "このカバーはエリィ専用です。\x01",
            "購入するとキャンプメニューの[ORBMENT]で表示される\x01",
            "戦術オーブメントのカバーが変わります。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CA1")

    label("loc_B7E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C11")

    #A0007
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "このカバーはティオ専用です。\x01",
            "購入するとキャンプメニューの[ORBMENT]で表示される\x01",
            "戦術オーブメントのカバーが変わります。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CA1")

    label("loc_C11")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CA1")

    #A0008
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "このカバーはランディ専用です。\x01",
            "購入するとキャンプメニューの[ORBMENT]で表示される\x01",
            "戦術オーブメントのカバーが変わります。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CA1")


    #A0009
    AnonymousTalk(
        0x8,
        "はい、これでいいですか～？\x02",
    )

    CloseMessageWindow()
    OP_5A()
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "【交換を頼む】\x01",      # 0
            "【やめておく】\x01",      # 1
        )
    )

    MenuEnd(0x3)
    OP_60(0x0)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FAD")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x12), scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_D94")

    #C0010
    ChrTalk(
        0x8,
        (
            "あれ～、ミラが足りないみたいですよ？\x01",
            "それじゃ交換はできないですぅ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F9E")

    label("loc_D94")


    #C0011
    ChrTalk(
        0x8,
        (
            "了解ですぅ。\x01",
            "ちょっと待っててくださいですぅ～㈱\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(71, 0, 100, 0)
    Sleep(800)
    FadeToBright(1000, 0)
    OP_0D()

    #C0012
    ChrTalk(
        0x8,
        "はい、お待たせですぅ。\x02",
    )

    CloseMessageWindow()
    SetChrName("")
    Sound(17, 0, 100, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E54")

    #A0013
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ロイドのオーブメントのカバーを交換した。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xF0, 5)
    Jump("loc_F2C")

    label("loc_E54")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E9D")

    #A0014
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "エリィのオーブメントのカバーを交換した。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xF0, 6)
    Jump("loc_F2C")

    label("loc_E9D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EE6")

    #A0015
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ティオのオーブメントのカバーを交換した。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xF0, 7)
    Jump("loc_F2C")

    label("loc_EE6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F2C")

    #A0016
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ランディのオーブメントのカバーを交換した。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xF1, 0)

    label("loc_F2C")

    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x50, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x50, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF1, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F67")
    OP_DE(0x16, 0x0)

    label("loc_F67")


    #C0017
    ChrTalk(
        0x8,
        (
            "ふふ、またのご利用を\x01",
            "お待ちしてま～す。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_50(0x12, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_SUB_SAVE), scpexpr(EXPR_END)))

    label("loc_F9E")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_FB7")

    label("loc_FAD")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_FB7")

    OP_CA(0x1, 0xFF, 0x0)
    FadeToDark(300, 0, 100)
    Jump("loc_778")

    label("loc_FCA")

    Return()

    # Function_5_76E end

    def Function_6_FCB(): pass

    label("Function_6_FCB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_1068")

    #C0018
    ChrTalk(
        0x8,
        (
            "もう、パパったらまだ\x01",
            "あのことを気にしてるのかしらねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x8,
        (
            "私はもう気にしてないし、\x01",
            "今の仕事も気に入ってるから\x01",
            "気に病むことないのにぃ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1ABE")

    label("loc_1068")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_10D5")

    #C0020
    ChrTalk(
        0x8,
        (
            "ウェンディ先輩、朝はいつも\x01",
            "すっごく眠そうなんですぅ。\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x8,
        "店長に怒られちゃいますよ～……\x02",
    )

    CloseMessageWindow()
    Jump("loc_1ABE")

    label("loc_10D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_1159")

    #C0022
    ChrTalk(
        0x8,
        (
            "……昨日あれだけ言ったのに、\x01",
            "結局パパが見にきてますぅ。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x8,
        (
            "ううん、もう飽きるまで\x01",
            "放っておくしかないですねぇ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1ABE")

    label("loc_1159")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_END)), "loc_1167")
    Jump("loc_1ABE")

    label("loc_1167")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_120C")

    #C0024
    ChrTalk(
        0x8,
        (
            "隠れて覗いてたパパに\x01",
            "もう職場に来ないように言ったら、\x01",
            "悲しい顔をして帰っちゃいました。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x8,
        (
            "うう、私なんにも悪くないのに\x01",
            "すごい罪悪感ですうぅ……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1ABE")

    label("loc_120C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_12A2")

    #C0026
    ChrTalk(
        0x8,
        (
            "う～、今日もパパが\x01",
            "こっそり私のことを見に来てますぅ。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x8,
        (
            "心配してくれるのは嬉しいんですけど、\x01",
            "仕事中気になって仕方ないですよぅ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1ABE")

    label("loc_12A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_1308")

    #C0028
    ChrTalk(
        0x8,
        (
            "導力器は、同じ価格帯でも\x01",
            "メーカーによって微妙に性能が\x01",
            "違っていたりするんですよぉ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1ABE")

    label("loc_1308")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_1385")

    #C0029
    ChrTalk(
        0x8,
        (
            "導力器は、買う商品を\x01",
            "悩んでいる時間が\x01",
            "一番楽しいんですよぉ。\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x8,
        (
            "どうかゆっくり\x01",
            "見ていってくださいねぇ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1ABE")

    label("loc_1385")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_1412")

    #C0031
    ChrTalk(
        0x8,
        (
            "あそこに隠れてるの\x01",
            "うちのパパなんですけど……\x01",
            "バレバレですよね～。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x8,
        (
            "もう、いつまでたっても\x01",
            "子離れできないんだからぁ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1ABE")

    label("loc_1412")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_14B1")

    #C0033
    ChrTalk(
        0x8,
        (
            "導力器には同じものでも\x01",
            "色々なメーカーの製品があるんですよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x8,
        (
            "お客さんごとに好きなメーカーが\x01",
            "違っていたりして、\x01",
            "なかなか面白いんですぅ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1ABE")

    label("loc_14B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_152D")

    #C0035
    ChrTalk(
        0x8,
        (
            "ウェンディ先輩の師匠のことは\x01",
            "よく知らないんですけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x8,
        (
            "とっても立派な導力技師さん\x01",
            "らしいですよ～。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1ABE")

    label("loc_152D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_1650")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15E2")

    #C0037
    ChrTalk(
        0x8,
        (
            "店長ったら、\x01",
            "今朝もウェンディ先輩に\x01",
            "嫌味を言ってたんですぅ。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x8,
        (
            "昨日はウェンディ先輩に\x01",
            "助けてもらったのに……\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x8,
        (
            "やっぱり店長は\x01",
            "ヤな性格ですぅ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_164B")

    label("loc_15E2")


    #C0040
    ChrTalk(
        0x8,
        (
            "昨日はウェンディ先輩に\x01",
            "助けてもらったのに\x01",
            "嫌味を言うなんて……\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x8,
        (
            "やっぱり店長は\x01",
            "ヤな性格ですぅ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_164B")

    Jump("loc_1ABE")

    label("loc_1650")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_16E3")

    #C0042
    ChrTalk(
        0x8,
        (
            "あ、店長が無謀にも\x01",
            "お客さんの対応してますよ～。\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x8,
        (
            "店長ったら導力器オンチで\x01",
            "チャコよりダメダメなのに……\x01",
            "よくやりますよね～。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1ABE")

    label("loc_16E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_1796")

    #C0044
    ChrTalk(
        0x8,
        (
            "おはよーございまーす☆\x01",
            "さっき遊撃士の人が来てたんですよ～。\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x8,
        (
            "爽やかな黒髪でぇ、\x01",
            "きれーな琥珀色の瞳……㈱\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x8,
        (
            "きゃっ、チャコ\x01",
            "一目ボレしちゃいそうでした～。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1ABE")

    label("loc_1796")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_1815")

    #C0047
    ChrTalk(
        0x8,
        (
            "わ～……\x01",
            "またパパが私の仕事振りを\x01",
            "覗きにきてますねえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x8,
        (
            "いつまでも子ども扱いで\x01",
            "なんだか恥ずかしいです。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1ABE")

    label("loc_1815")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18AB")

    #C0049
    ChrTalk(
        0x8,
        (
            "いらっしゃいませー☆\x01",
            "こちらはお買い上げカウンターです。\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x8,
        (
            "導力製品の修理には\x01",
            "となりのサービスカウンターを\x01",
            "ご利用くださいねー！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1ABE")

    label("loc_18AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_193D")

    #C0051
    ChrTalk(
        0x8,
        (
            "皆さんって、ウェンディ先輩の\x01",
            "知り合いだったんですね～。\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x8,
        (
            "わたし、販売員のチャコっていいます。\x01",
            "よろぴくお願いしま～す☆\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x4C, 0)
    Jump("loc_1ABE")

    label("loc_193D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A56")

    #C0053
    ChrTalk(
        0x8,
        (
            "このストア、開店してから\x01",
            "毎日大繁盛なんですよー。\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x8,
        (
            "でもチャコ、導力製品のこと\x01",
            "よく判んなくってぇ……\x01",
            "先輩に教わってばかりなんですぅ。\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x8,
        (
            "ウェンディ先輩って\x01",
            "とっても物知りですよね～。\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x101,
        (
            "#0000F（物知りっていうか……\x01",
            "  昔からメカ好きなだけだけどな。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1ABE")

    label("loc_1A56")


    #C0057
    ChrTalk(
        0x8,
        (
            "ウェンディ先輩って\x01",
            "とっても物知りですよね～。\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x8,
        (
            "チャコ、いつも\x01",
            "先輩に教わってばかりなんですぅ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1ABE")

    Return()

    # Function_6_FCB end

    def Function_7_1ABF(): pass

    label("Function_7_1ABF")

    Call(0, 8)
    Return()

    # Function_7_1ABF end

    def Function_8_1AC3(): pass

    label("Function_8_1AC3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xE, 0x1, 0x0)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5A, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0xE, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0xE, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1AED")
    Call(0, 17)
    Return()

    label("loc_1AED")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xE, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0xE, 0x1, 0x0)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0xE, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1B0E")
    Call(0, 16)
    Return()

    label("loc_1B0E")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_25F0")
    EventBegin(0x0)
    Fade(500)
    OP_68(7380, 1500, -2280, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(20000, 0)
    SetChrPos(0x101, 6900, 0, -2250, 90)
    SetChrPos(0x102, 6900, 0, -1100, 90)
    SetChrPos(0x103, 5600, 0, -2250, 90)
    SetChrPos(0x104, 5600, 0, -1100, 90)
    OP_93(0x9, 0x10E, 0x0)
    SetChrSubChip(0x9, 0x0)
    OP_4B(0x9, 0xFF)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    OP_6F(0x10)
    OP_0D()

    #C0059
    ChrTalk(
        0x9,
        (
            "#11Pちわ～す！　こんにちは～！\x01",
            "《ゲンテン工房》……\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x9,
        (
            "#11P……じゃなかった、\x01",
            "オーバルストア《ゲンテン》へようこそ～。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0061
    ChrTalk(
        0x9,
        (
            "#11Pって……\x01",
            "わわっ、ロイドじゃない！\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x101,
        (
            "#0011F#6Pウェンディ！？\x01",
            "こんな所で何をしてるんだ？\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x9,
        "#11Pぶー、失礼ねー。\x02",
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x9,
        (
            "#11P私がこのストアの技師#4Rエンジニア#だからに\x01",
            "決まってるじゃな～い。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1D6A")
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    label("loc_1D6A")


    #C0065
    ChrTalk(
        0x101,
        (
            "#0011F#6Pそ、そうなのか！？\x01",
            "そういや就職したって聞いたけど……\x02\x03",

            "#0002Fいや、ちょっと\x01",
            "意外だったからさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x104,
        (
            "#0302F#5Pなんだよ、ロイドの幼馴染か？\x01",
            "へえ～、可愛い子じゃん。\x02\x03",

            "#0309F今度俺とデートでもどう？\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x102,
        (
            "#0106F#6P……どさくさに紛れて\x01",
            "何を言っているのかしら。\x02\x03",

            "#0100Fこんにちは。\x01",
            "ここの噂は聞いていましたけど\x01",
            "随分と綺麗なお店なんですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x9,
        "#11Pあ、ロイドの同僚の人？\x02",
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x9,
        (
            "#11Pあはは、まあ店の見栄えは\x01",
            "完全に店長の趣味なんですけどねー。\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x9,
        (
            "#11Pちなみにここはカスタマーサービス用の\x01",
            "カウンターなの。\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x9,
        (
            "#11P戦術オーブメントの\x01",
            "お手入れなんかも扱ってるわよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0x101,
        (
            "#0000F#6Pそっか、ウェンディに頼めば\x01",
            "一通りの事はできるみたいだな。\x02\x03",

            "#0005Fあ、でも俺たちのオーブメントは\x01",
            "『エニグマ』っていう新型なんだけど\x01",
            "……大丈夫かな？\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0x9,
        (
            "#11Pあれ……ロイドたちも\x01",
            "新型を使ってるんだー。\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x9,
        (
            "#11Pうんうん、任せといて。\x01",
            "新型用のクオーツ調整器もあるし……\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0x9,
        (
            "#11P実はこの前からちょくちょく\x01",
            "遊撃士の人が利用していくのよね～。\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x101,
        "#0011F#6Pそ、そう……なのか？\x02",
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0x103,
        (
            "#0203F#6P遊撃士協会の方でも\x01",
            "エニグマの実戦配備が\x01",
            "始まっていたようですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0x104,
        (
            "#0302F#5Pハハ、やっぱ\x01",
            "遊撃士どもは行動が早いねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0x102,
        "#0106F#6Pあまり笑い事じゃないけれど。\x02",
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1200)

    #C0080
    ChrTalk(
        0x101,
        (
            "#0012F#6Pいや、大したことじゃ\x01",
            "ないんだけどさ。\x02\x03",

            "#0000Fともかく、ウェンディには\x01",
            "これから何度もお世話になると思う。\x01",
            "よろしく頼むよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0x9,
        "#11Pうん、こちらこそよろしく！\x02",
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x9,
        (
            "#11Pオーブメントを改造したいときは\x01",
            "私に話しかけて\x01",
            "『改造・合成する』を選んでね。\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x9,
        (
            "#11Pそれと、もしオーブメントについて\x01",
            "分からない事があったら\x01",
            "何でも聞いちゃって。\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x9,
        "#11P私、これでもプロの技師#4Rエンジニア#なんだから。\x02",
    )

    CloseMessageWindow()
    Sound(828, 0, 100, 0)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 180, 60, -1)

    #A0085
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※オーバルストアで『改造・合成する』を選択すると、\x01",
            "  新しいクオーツの合成や\x01",
            "  戦術オーブメントのスロット開封が行えます。\x02\x03",

            "※新しいクオーツを合成し、セットすれば\x01",
            "  様々なアーツを使うことが出来るようになります。\x01",
            "  （メニューから[QUARTZ]を選択してください。）\x02\x03",

            "※スロットの開封を行えば、\x01",
            "  セットできるクオーツの数が増えるとともに\x01",
            "  最大ＥＰを増加させることができます。\x01",
            "  （メニューから[SLOT]を選択してください。）\x02\x03",

            "※各機能を利用するためには\x01",
            "  『セピス』と呼ばれる結晶のカケラが必要です。\x01",
            "  『セピス』は、魔獣を倒すことで入手できます。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToBright(300, 0)
    SetScenarioFlags(0x4C, 1)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    OP_4C(0x9, 0xFF)
    SetChrPos(0x0, 6980, 0, -1400, 90)
    EventEnd(0x5)
    Return()

    label("loc_25F0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xE, 0x1, 0x0)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0xE, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0xE, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_284C")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2617")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2847")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "話をする\x01",              # 0
            "改造・合成する\x01",        # 1
            "質問をする\x01",            # 2
            "依頼について聞く\x01",      # 3
            "やめる\x01",                # 4
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2693")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_2693")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2714")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD9, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_26B3")
    Call(0, 11)

    label("loc_26B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_26C3")
    OP_AF(0xF)
    Jump("loc_2705")

    label("loc_26C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_26D3")
    OP_AF(0xE)
    Jump("loc_2705")

    label("loc_26D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_26E3")
    OP_AF(0xD)
    Jump("loc_2705")

    label("loc_26E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_26F3")
    OP_AF(0xC)
    Jump("loc_2705")

    label("loc_26F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_2703")
    OP_AF(0xB)
    Jump("loc_2705")

    label("loc_2703")

    OP_AF(0xA)

    label("loc_2705")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2842")

    label("loc_2714")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2735")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 10)
    Jump("loc_2842")

    label("loc_2735")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2812")

    #C0086
    ChrTalk(
        0x9,
        (
            "エニグマの性能評価には\x01",
            "『敵から認識されなくなるアーツ』を\x01",
            "試してみて。\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x9,
        (
            "実戦で使用して、\x01",
            "ちゃんと効果があるかまで\x01",
            "確認してほしい所ね。\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0x9,
        (
            "それが終わったら\x01",
            "私の所に報告しに来てね。\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2842")

    label("loc_2812")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2826")
    Jump("loc_2842")

    label("loc_2826")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2842")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 9)

    label("loc_2842")

    Jump("loc_2617")

    label("loc_2847")

    Jump("loc_2998")

    label("loc_284C")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2856")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2998")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "話をする\x01",            # 0
            "改造・合成する\x01",      # 1
            "質問をする\x01",          # 2
            "やめる\x01",              # 3
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_28C1")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_28C1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2942")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD9, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_28E1")
    Call(0, 11)

    label("loc_28E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_28F1")
    OP_AF(0xF)
    Jump("loc_2933")

    label("loc_28F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_2901")
    OP_AF(0xE)
    Jump("loc_2933")

    label("loc_2901")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_2911")
    OP_AF(0xD)
    Jump("loc_2933")

    label("loc_2911")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_2921")
    OP_AF(0xC)
    Jump("loc_2933")

    label("loc_2921")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_2931")
    OP_AF(0xB)
    Jump("loc_2933")

    label("loc_2931")

    OP_AF(0xA)

    label("loc_2933")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2993")

    label("loc_2942")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2963")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 10)
    Jump("loc_2993")

    label("loc_2963")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2977")
    Jump("loc_2993")

    label("loc_2977")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2993")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 9)

    label("loc_2993")

    Jump("loc_2856")

    label("loc_2998")

    TalkEnd(0x9)
    Return()

    # Function_8_1AC3 end

    def Function_9_299C(): pass

    label("Function_9_299C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_2A3D")

    #C0089
    ChrTalk(
        0x9,
        (
            "でも助かったわー。\x01",
            "やっぱりユーザーの意見は貴重よね。\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x9,
        (
            "ロイド、また\x01",
            "何かあったらよろしくね！\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x101,
        (
            "#0000Fああ、遠慮なく\x01",
            "依頼を回してくれ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_41FF")

    label("loc_2A3D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_2B5E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2AF9")

    #C0092
    ChrTalk(
        0x9,
        (
            "フェルナンドさんも\x01",
            "なんだか丸くなったわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x9,
        (
            "それに、最近は導力器についても\x01",
            "勉強を始めたみたい。\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x9,
        (
            "ふふん、せっかくだし\x01",
            "また私が教えてあげよっかな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2B59")

    label("loc_2AF9")


    #C0095
    ChrTalk(
        0x9,
        (
            "フェルナンドさんとも\x01",
            "昔よりはうまくやってけそう。\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0x9,
        (
            "導力器の勉強も\x01",
            "今度見てあげようかな\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B59")

    Jump("loc_41FF")

    label("loc_2B5E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_2BB2")

    #C0097
    ChrTalk(
        0x9,
        "くあ……朝は弱いのよねー。\x02",
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x9,
        "チャコの元気さがうらやましいわ。\x02",
    )

    CloseMessageWindow()
    Jump("loc_41FF")

    label("loc_2BB2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_2D0D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C9A")

    #C0099
    ChrTalk(
        0x9,
        (
            "最初はどうかなと思ったけど、\x01",
            "オーバルストアってのも悪くないわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0x9,
        (
            "修理の対応も整った機材で\x01",
            "きちんとできるし、工房だった頃より\x01",
            "お客さんが入りやすそうだもの。\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0x9,
        "んー、見た目もやっぱり大事よね。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2D08")

    label("loc_2C9A")


    #C0102
    ChrTalk(
        0x9,
        (
            "この前、街でお客さんに\x01",
            "修理のお礼を言わちゃったのよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0x9,
        (
            "やっぱこの仕事を\x01",
            "やってて良かったと思うわ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D08")

    Jump("loc_41FF")

    label("loc_2D0D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_END)), "loc_2D1B")
    Jump("loc_41FF")

    label("loc_2D1B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_2D88")

    #C0104
    ChrTalk(
        0x9,
        "ウチの父さん、また出張に出たわ。\x02",
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0x9,
        (
            "あー、パンセの世話を任せられて\x01",
            "ラクだったのになー。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_41FF")

    label("loc_2D88")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_33B6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBF, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_32C6")

    #C0106
    ChrTalk(
        0x9,
        "あ、ロイドだ。\x02",
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0x9,
        (
            "久し振りじゃな～い。\x01",
            "やっほー！\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0x153,
        (
            "#1110Fやっほー！\x01",
            "すごいおミセだねー！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0x9, 0x153, 500)
    Sleep(300)
    OP_63(0x9, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1800)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2E83")

    #C0109
    ChrTalk(
        0x102,
        (
            "#0100Fキーアちゃん、\x01",
            "また絶妙なタイミングで……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F26")

    label("loc_2E83")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2ED7")

    #C0110
    ChrTalk(
        0x103,
        (
            "#0200Fキーア、また絶妙なタイミングで\x01",
            "割り込みましたね……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F26")

    label("loc_2ED7")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2F26")

    #C0111
    ChrTalk(
        0x104,
        (
            "#0300Fキー坊、ナイスタイミングで\x01",
            "割り込んじまったなぁ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F26")

    OP_64(0x9)

    #C0112
    ChrTalk(
        0x9,
        "なにその子……スゴク可愛い。\x02",
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0x101,
        (
            "#0000Fハハ、やっぱり\x01",
            "ウェンディでもそう思うんだ？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x101, 500)
    Sleep(300)

    #C0114
    ChrTalk(
        0x9,
        (
            "なによう、私だって\x01",
            "メカだけを愛でてるわけじゃないわよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0x9,
        (
            "でも驚いた……ロイドにそんな\x01",
            "甲斐性があるなんてねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0x101,
        "#0000Fえ…………甲斐性って？\x02",
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0x9,
        (
            "記念祭で迷子になってた子を\x01",
            "支援課の方で預かってるんでしょ？\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0x9,
        (
            "あ、１週間も顔を出さなかったのは\x01",
            "そのせいか～。\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0x101,
        "#0003F（あながち間違ってない……）\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_312D")

    #C0120
    ChrTalk(
        0x102,
        (
            "#0100Fこの子はキーアちゃんと言って……\x01",
            "確かに身元の方を\x01",
            "探している所なんです。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_31EA")

    label("loc_312D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3190")

    #C0121
    ChrTalk(
        0x103,
        (
            "#0200Fこの子はキーアと言って……\x01",
            "確かに身元の方を\x01",
            "探している所なんです。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_31EA")

    label("loc_3190")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_31EA")

    #C0122
    ChrTalk(
        0x104,
        (
            "#0300Fこの子はキーアつってな、\x01",
            "確かに身元の方を\x01",
            "探している所なんだ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_31EA")


    #C0123
    ChrTalk(
        0x9,
        (
            "やっぱりそうなんだ。\x01",
            "ん～、私には心当たりはないけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0x9,
        (
            "何か困った事があったら言ってね？\x01",
            "ウチにも妹がいるし、\x01",
            "小さい子の世話なら慣れてるんだから。\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0x101,
        (
            "#0000Fサンキュー、何かあったら\x01",
            "頼らせてもらうよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xBF, 6)
    Jump("loc_33B1")

    label("loc_32C6")

    TurnDirection(0x9, 0x153, 0)

    #C0126
    ChrTalk(
        0x9,
        (
            "キーアちゃんかぁ……\x01",
            "ウチのパンセより\x01",
            "ちょっと下くらいかしら。\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0x9,
        (
            "キーアちゃん、歩くのに疲れたら\x01",
            "ちゃんとロイドに言うのよ～？\x02",
        )
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0x9,
        (
            "ロイドって時々\x01",
            "抜けてる所があるから。\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0x153,
        "#1109Fうん、わかった～！\x02",
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0x101,
        "#0000Fハハハ……\x02",
    )

    CloseMessageWindow()

    label("loc_33B1")

    Jump("loc_41FF")

    label("loc_33B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_342C")

    #C0131
    ChrTalk(
        0x9,
        (
            "そういえば来月、\x01",
            "父さんが出張から帰ってくるわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0x9,
        (
            "記念祭には間に合いそうね。\x01",
            "よかったよかった。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_41FF")

    label("loc_342C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_3526")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_34D1")

    #C0133
    ChrTalk(
        0x9,
        (
            "普段駅を行き来している列車は、\x01",
            "帝国ラインフォルト社製なのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0x9,
        (
            "鼻先についてるユニコーンの飾りが\x01",
            "いかにも帝国製って感じなのよね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3521")

    label("loc_34D1")


    #C0135
    ChrTalk(
        0x9,
        (
            "ラインフォルト社製品は\x01",
            "ゴツい、厳ついって言葉が\x01",
            "いつも当てはまるのよね～。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3521")

    Jump("loc_41FF")

    label("loc_3526")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_35A2")

    #C0136
    ChrTalk(
        0x9,
        "もうそろそろあがりなのよね。\x02",
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0x9,
        (
            "パンセへのお土産に\x01",
            "ベーカリーショップで\x01",
            "菓子パンでも買って帰ろうかな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_41FF")

    label("loc_35A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_36D3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_368A")

    #C0138
    ChrTalk(
        0x9,
        (
            "店内にある導力車、\x01",
            "どうやって店に入れたでしょう？\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0x9,
        (
            "正解は……\x01",
            "導力車の周りに店を建てたのでした！\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0x101,
        (
            "#0005Fそ、そうなのか！？\x01",
            "なるほど、逆転の発想ってわけか……\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0x9,
        "……ウソに決まってるでしょ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_36CE")

    label("loc_368A")


    #C0142
    ChrTalk(
        0x9,
        (
            "あはは、ロイドって\x01",
            "根が真面目だから\x01",
            "おちょくりやすいのよねー。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_36CE")

    Jump("loc_41FF")

    label("loc_36D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_381B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_37AE")

    #C0143
    ChrTalk(
        0x9,
        (
            "ロイド、今日はエプスタイン製の\x01",
            "新型導力掃除機が入ってるわよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0x101,
        (
            "#0000Fえっとウェンディ、\x01",
            "それを俺に買えってこと？\x02",
        )
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0x9,
        (
            "あはは、やだなー。\x01",
            "愛でて行きなさいって\x01",
            "言ってるだけじゃなーい。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3816")

    label("loc_37AE")


    #C0146
    ChrTalk(
        0x9,
        (
            "今日はエプスタイン製の\x01",
            "新型導力掃除機が入ってるわよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0x9,
        (
            "新製品の独特の匂いって\x01",
            "大好きなのよ～。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3816")

    Jump("loc_41FF")

    label("loc_381B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_3A97")

    #C0148
    ChrTalk(
        0x9,
        (
            "クロスベル警備隊が\x01",
            "特殊装甲車を追加発注したそうね。\x02",
        )
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0x9,
        (
            "うーん、あそこの装備は\x01",
            "相変わらず凄いわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0x9,
        "技師として勤めてみたいかも。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8D, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A92")

    #C0151
    ChrTalk(
        0x104,
        (
            "#0300Fま、一応自治州を守る\x01",
            "治安維持部隊だからな。\x02\x03",

            "#0304Fでも勤めるのは\x01",
            "やめた方が良いと思うぜ。\x02\x03",

            "#0300Fフ……君にはもっと\x01",
            "似合いの職場があるはずさっ！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)

    #C0152
    ChrTalk(
        0x9,
        "わー、ありがとランディさん！\x02",
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0x9,
        (
            "やっぱり私って\x01",
            "発明工房とかの方が向いてるよね！\x02",
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

    #C0154
    ChrTalk(
        0x104,
        "#0306F（ダメだ、うまく掛からねえや。）\x02",
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0x103,
        (
            "#0200F（ランディさん、病院に引き続き\x01",
            "  黒星２つですね。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x8D, 4)

    label("loc_3A92")

    Jump("loc_41FF")

    label("loc_3A97")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_3B07")

    #C0156
    ChrTalk(
        0x9,
        (
            "店長ったら……\x01",
            "導力器オンチのくせに\x01",
            "すぐに見栄を張るんだから。\x02",
        )
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0x9,
        "後で助けてあげなくちゃ。\x02",
    )

    CloseMessageWindow()
    Jump("loc_41FF")

    label("loc_3B07")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_3DD7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6A, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3C81")

    #C0158
    ChrTalk(
        0x9,
        (
            "おはよー、ロイドに皆さん。\x01",
            "仕事は順調？\x02",
        )
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0x101,
        (
            "#0000Fはは、まあ\x01",
            "それなりに……かな。\x02",
        )
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0x103,
        (
            "#0203F色々な仕事が舞い込んで\x01",
            "けっこう大変ですけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0x9,
        (
            "あはははは……\x01",
            "うんうん、頑張ってるみたいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0x9,
        (
            "出かける前には\x01",
            "ちゃんとオーブメントの状態を\x01",
            "確認しておいてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0x9,
        "後で慌てても知らないぞ～？\x02",
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0x101,
        (
            "#0000Fああ、分かってる。\x01",
            "サンキュー、ウェンディ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x6A, 5)
    Jump("loc_3DD2")

    label("loc_3C81")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D6A")

    #C0165
    ChrTalk(
        0x9,
        (
            "最近は遊撃士の人も\x01",
            "新型のオーブメントを\x01",
            "使ってるみたいよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0x9,
        (
            "それに昨日は\x01",
            "ダドリーさんって警察の人が来たし……\x01",
            "新型も普及してきたみたいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0x104,
        (
            "#0300F俺たちも\x01",
            "踏ん張らねえとなぁ……\x02",
        )
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0x102,
        "#0106Fそうねぇ……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3DD2")

    label("loc_3D6A")


    #C0169
    ChrTalk(
        0x9,
        (
            "ウチには警察や\x01",
            "遊撃士の人が結構来るの。\x02",
        )
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0x9,
        (
            "新型オーブメントを使ってる人も\x01",
            "増えてきてるみたいよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3DD2")

    Jump("loc_41FF")

    label("loc_3DD7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_3EE5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E86")

    #C0171
    ChrTalk(
        0x9,
        (
            "うちの店長は元々\x01",
            "有名なデザイナーだったらしいの。\x02",
        )
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0x9,
        (
            "確かに美的感覚#8Rセ 　ン 　ス#はあるんだろうけど……\x01",
            "ちょーっと性格に難アリなのよねー。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3EE0")

    label("loc_3E86")


    #C0173
    ChrTalk(
        0x9,
        (
            "このストアの内装も\x01",
            "店長が自分で設計したのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0x9,
        (
            "……何となく\x01",
            "見れば分かるでしょ？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3EE0")

    Jump("loc_41FF")

    label("loc_3EE5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_41FF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_40E6")

    #C0175
    ChrTalk(
        0x9,
        (
            "このオーバルストアは\x01",
            "去年までは普通の工房だったのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0x9,
        (
            "でもこの前店長が代わってね、\x01",
            "お店も経営方針も\x01",
            "ピカピカになっちゃったの。\x02",
        )
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0x9,
        (
            "私は泥臭い工房の方が\x01",
            "好きだったんだけどな～。\x02",
        )
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0x101,
        (
            "#0000Fははは……\x01",
            "確かにそっちの方が\x01",
            "ウェンディのイメージだよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0x9,
        "……ねえロイド、今何か言った？\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0180
    ChrTalk(
        0x101,
        (
            "#0006Fごめんなさい。\x01",
            "何でもありません。\x02",
        )
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0x9,
        (
            "そうそう、工房時代の私の師匠がね、\x01",
            "旧市街で店を始めたらしいの。\x02",
        )
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0x9,
        (
            "ロイド達も暇なら\x01",
            "一度覗いてみるといいかもね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x4D, 0)
    Jump("loc_41FF")

    label("loc_40E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_41B0")

    #C0183
    ChrTalk(
        0x9,
        (
            "このオーバルストアは\x01",
            "去年までは普通の工房だったのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0x9,
        (
            "私の師匠も\x01",
            "腕を振るってたんだけど……\x01",
            "肌に合わなくてやめちゃったわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0x9,
        (
            "私も泥臭い工房の方が\x01",
            "好きだったんだけどな～。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_41FF")

    label("loc_41B0")


    #C0186
    ChrTalk(
        0x9,
        (
            "師匠は旧市街で\x01",
            "店を始めたらしいけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0x9,
        "一度覗いてみるといいかもね。\x02",
    )

    CloseMessageWindow()

    label("loc_41FF")

    Return()

    # Function_9_299C end

    def Function_10_4200(): pass

    label("Function_10_4200")


    #C0188
    ChrTalk(
        0x9,
        (
            "オッケー。\x01",
            "何について聞きたいの？\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4231")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4A85")
    FadeToDark(300, 0, 100)

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "戦術オーブメントについて\x01",        # 0
            "クオーツについて\x01",                # 1
            "スロットについて\x01",                # 2
            "導力魔法（アーツ）について\x01",      # 3
            "やめる\x01",                          # 4
        )
    )

    MenuEnd(0x3)
    OP_60(0x1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_NEQ), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_42DA")
    FadeToBright(300, 0)
    OP_5A()

    label("loc_42DA")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_END)),
        (0, "loc_42FC"),
        (1, "loc_451D"),
        (2, "loc_464E"),
        (3, "loc_4795"),
        (SWITCH_DEFAULT, "loc_4A71"),
    )


    label("loc_42FC")


    #C0189
    ChrTalk(
        0x9,
        (
            "《戦術オーブメント》っていうのは、\x01",
            "個人の戦闘用に特化した\x01",
            "小型の携帯導力器のことよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0x9,
        (
            "使用者の能力を強化してくれるほか\x01",
            "導力魔法#8Rア  ー  ツ#の使用もサポートしてくれるの。\x02",
        )
    )

    CloseMessageWindow()

    #C0191
    ChrTalk(
        0x9,
        (
            "一般的には、単に『オーブメント』って\x01",
            "呼ばれたりするわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0x9,
        (
            "ロイド達が使ってるのは、\x01",
            "その中でも最新型の\x01",
            "『エニグマ』っていうタイプよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0x9,
        (
            "オーブメントは個人に合わせて\x01",
            "完璧に調整されてるから、\x01",
            "持ち主によって構造が異なるわよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0194
    ChrTalk(
        0x9,
        (
            "属性限定のスロットがあったり、\x01",
            "スロットを結ぶ線#2Rライン#の形が違ったりするわ。\x01",
            "一度みんなで見比べてみるといいかもね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4A80")

    label("loc_451D")


    #C0195
    ChrTalk(
        0x9,
        (
            "クオーツは、セピスを精錬して作られる\x01",
            "オーブメント用の『結晶回路』のことね。\x02",
        )
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0x9,
        (
            "必要なセピスさえ持ってきてくれれば\x01",
            "ウチで合成ができるわよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0x9,
        (
            "クオーツによって色々な効果があるし、\x01",
            "属性値が一定以上になると\x01",
            "導力魔法#8Rア  ー  ツ#が使えるようになるの。\x02",
        )
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0x9,
        "セピスが溜まったら色々試してみてね。\x02",
    )

    CloseMessageWindow()
    Jump("loc_4A80")

    label("loc_464E")


    #C0199
    ChrTalk(
        0x9,
        (
            "オーブメントのスロットは\x01",
            "初めはほとんどが未開封の状態なの。\x02",
        )
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0x9,
        (
            "クオーツをセットするには\x01",
            "まずはスロットを開封する必要があるわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0x9,
        (
            "スロットを開封すれば、\x01",
            "クオーツも沢山セットできるようになるし\x01",
            "最大ＥＰの値も上昇するわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0202
    ChrTalk(
        0x9,
        (
            "開封にはセピスが必要だけど\x01",
            "かなり便利になるはずよ。\x01",
            "積極的に開けていくといいと思うわ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4A80")

    label("loc_4795")


    #C0203
    ChrTalk(
        0x9,
        (
            "戦術オーブメントを使って発動する魔法が\x01",
            "いわゆる導力魔法#8Rオーバルアーツ#ね。\x02",
        )
    )

    CloseMessageWindow()

    #C0204
    ChrTalk(
        0x9,
        "単純に『アーツ』って呼ばれる事が多いわ。\x02",
    )

    CloseMessageWindow()

    #C0205
    ChrTalk(
        0x9,
        (
            "オーブメントに内蔵されている機構と\x01",
            "クオーツが使用者と共鳴連鎖することで\x01",
            "魔法現象を展開するんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0206
    ChrTalk(
        0x9,
        "ま、細かいことはいいかな。\x02",
    )

    CloseMessageWindow()

    #C0207
    ChrTalk(
        0x9,
        (
            "アーツは、セットしたクオーツの\x01",
            "『ラインごとの属性値の合計』によって\x01",
            "発動できる種類が決まってくるの。\x02",
        )
    )

    CloseMessageWindow()

    #C0208
    ChrTalk(
        0x9,
        (
            "ちょっと難しいけど……\x01",
            "そうね、例えば。\x02",
        )
    )

    CloseMessageWindow()

    #C0209
    ChrTalk(
        0x9,
        (
            "ラインが繋がっているスロットに\x01",
            "クオーツをセットしていって、\x01",
            "地属性の合計値が２以上になると……\x02",
        )
    )

    CloseMessageWindow()

    #C0210
    ChrTalk(
        0x9,
        (
            "『クエイク』ってアーツが\x01",
            "使えるようになるわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0211
    ChrTalk(
        0x9,
        (
            "クオーツをセットするほど、\x01",
            "たくさんのアーツが\x01",
            "使えるようになるってわけね。\x02",
        )
    )

    CloseMessageWindow()

    #C0212
    ChrTalk(
        0x9,
        (
            "他のアーツの組み合わせは\x01",
            "アーツリストに載ってるはずよ。\x01",
            "参考にしてね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4A80")

    label("loc_4A71")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4A80")

    label("loc_4A80")

    Jump("loc_4231")

    label("loc_4A85")

    Sleep(150)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_10_4200 end

    def Function_11_4A93(): pass

    label("Function_11_4A93")

    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    #C0213
    ChrTalk(
        0x9,
        (
            "そうだ、ロイドたちって\x01",
            "『上位クオーツ』を持ってたりしない？\x02",
        )
    )

    CloseMessageWindow()

    #C0214
    ChrTalk(
        0x101,
        "#0005F『上位クオーツ』……？\x02",
    )

    CloseMessageWindow()

    #C0215
    ChrTalk(
        0x9,
        (
            "うんうん、強力すぎて普通のスロットには\x01",
            "セットできないクオーツなの。\x02",
        )
    )

    CloseMessageWindow()

    #C0216
    ChrTalk(
        0x9,
        (
            "セットするためには\x01",
            "スロット自体の強化が必要になるわ。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4C16")

    #C0217
    ChrTalk(
        0x9,
        (
            "上位クオーツ自体は\x01",
            "うちでもまだ扱ってないんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0218
    ChrTalk(
        0x9,
        (
            "スロットの強化は請け負ってるから、\x01",
            "必要があったら声を掛けてね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4C76")

    label("loc_4C16")


    #C0219
    ChrTalk(
        0x9,
        (
            "うちでもスロットの強化と\x01",
            "上位クオーツの取り扱いを始めたから、\x01",
            "必要があったら声を掛けてね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4C76")

    OP_5A()
    Sound(828, 0, 100, 0)
    FadeToDark(300, 0, 100)

    #A0220
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※スロットの強化が行えるようになりました。\x02",
        )
    )

    CloseMessageWindow()

    #A0221
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※[SLOT]を選んで\x01",
            "  開封済みのスロットを選択すると\x01",
            "  スロットレベルを強化する事ができます。\x02",
        )
    )

    CloseMessageWindow()

    #A0222
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※上位クオーツのセットが可能になるほか、\x01",
            "  最大ＥＰもこれまで以上に\x01",
            "  引き上げる事ができます。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0xD9, 3)
    OP_C7(0x1, 0x80)
    Return()

    # Function_11_4A93 end

    def Function_12_4D90(): pass

    label("Function_12_4D90")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_4EF9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4E6A")
    OP_93(0xFE, 0x0, 0x0)

    #C0223
    ChrTalk(
        0xFE,
        "ふむ……ふむふむなるほど……\x02",
    )

    CloseMessageWindow()

    #C0224
    ChrTalk(
        0xFE,
        (
            "導力灯はソケットの汚れなどにより\x01",
            "接触不良の可能性も……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xFE, 0x0, 500)

    #C0225
    ChrTalk(
        0xFE,
        (
            "し、失礼しました。\x01",
            "なにか御用でしょうか？\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    OP_93(0xA, 0xB4, 0x0)
    SetScenarioFlags(0x0, 2)
    Return()

    label("loc_4E6A")


    #C0226
    ChrTalk(
        0xFE,
        "導力器について聞きたいことでも？\x02",
    )

    CloseMessageWindow()

    #C0227
    ChrTalk(
        0xFE,
        (
            "すみませんが私、今勉強中でして……\x01",
            "サポートカウンターのほうで\x01",
            "お聞きくださるようお願いします。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5A36")

    label("loc_4EF9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_4F7D")

    #C0228
    ChrTalk(
        0xFE,
        (
            "……ん……ウェンディめ、\x01",
            "また寝坊頭でカウンターに……\x02",
        )
    )

    CloseMessageWindow()

    #C0229
    ChrTalk(
        0xFE,
        (
            "ふん、あとできちんと\x01",
            "言っておかなければなりませんな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5A36")

    label("loc_4F7D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_500A")

    #C0230
    ChrTalk(
        0xFE,
        (
            "この間、ウェンディが\x01",
            "私の商品の陳列を\x01",
            "初めて褒めてくれましてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0xFE,
        (
            "……べ、別に嬉しかったという\x01",
            "わけではないのですよ？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5A36")

    label("loc_500A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_END)), "loc_5018")
    Jump("loc_5A36")

    label("loc_5018")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_50E6")

    #C0232
    ChrTalk(
        0xFE,
        (
            "ウェンディから要望がありましてね。\x01",
            "修理サポートの時間外受付を\x01",
            "実施できないかと……\x02",
        )
    )

    CloseMessageWindow()

    #C0233
    ChrTalk(
        0xFE,
        (
            "……実際彼女のおかげでついた\x01",
            "リピーターもなかなか多い。\x02",
        )
    )

    CloseMessageWindow()

    #C0234
    ChrTalk(
        0xFE,
        (
            "検討してみても\x01",
            "いいかもしれませんな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5A36")

    label("loc_50E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_5271")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5208")

    #C0235
    ChrTalk(
        0xFE,
        (
            "おや……こちらの高級導力車を\x01",
            "お買い上げですかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0236
    ChrTalk(
        0x153,
        (
            "#1105Fねぇねぇ、\x01",
            "触ってもいいの？　あれ。\x02\x03",

            "#1100F（そ～……）\x02",
        )
    )

    CloseMessageWindow()

    #C0237
    ChrTalk(
        0x101,
        (
            "#0005Fわー、ダメダメ！\x01",
            "キズなんてつけたら\x01",
            "弁償しきれないぞ！\x02",
        )
    )

    CloseMessageWindow()

    #C0238
    ChrTalk(
        0x153,
        "#1106Fなーんだ。\x02",
    )

    CloseMessageWindow()

    #C0239
    ChrTalk(
        0xFE,
        (
            "……お子様から目を離さないよう\x01",
            "お願いしますよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_526C")

    label("loc_5208")


    #C0240
    ChrTalk(
        0xFE,
        (
            "……コホン。\x01",
            "お子様から目を離さないよう\x01",
            "お願いしますよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0241
    ChrTalk(
        0x101,
        "#0006F（警戒されてしまった……）\x02",
    )

    CloseMessageWindow()

    label("loc_526C")

    Jump("loc_5A36")

    label("loc_5271")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_5304")

    #C0242
    ChrTalk(
        0xFE,
        (
            "私としては、導力車の販売を\x01",
            "軌道に乗せたいところですよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0243
    ChrTalk(
        0xFE,
        (
            "ここは一つ、自治州政府が\x01",
            "大々的に普及を推し進めて\x01",
            "欲しいものです。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5A36")

    label("loc_5304")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_53DA")

    #C0244
    ChrTalk(
        0xFE,
        (
            "くうぅ、ウェンディめ……\x01",
            "私の華麗な商品陳列術に\x01",
            "ケチをつけるなんて。\x02",
        )
    )

    CloseMessageWindow()

    #C0245
    ChrTalk(
        0xFE,
        (
            "……しかし悔しい事に\x01",
            "ピタリと的を射ているのです。\x02",
        )
    )

    CloseMessageWindow()

    #C0246
    ChrTalk(
        0xFE,
        (
            "さすが、オーバルストアになる前から\x01",
            "工房に勤めているだけはある……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5A36")

    label("loc_53DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_555E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_54C2")

    #C0247
    ChrTalk(
        0xFE,
        (
            "当店は最先端の\x01",
            "導力ネット……なんとかの端末も\x01",
            "展示しておりますよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0248
    ChrTalk(
        0xFE,
        (
            "よくは知りませんが、\x01",
            "大変高価なものです。\x02",
        )
    )

    CloseMessageWindow()

    #C0249
    ChrTalk(
        0xFE,
        (
            "フフ……宜しければ\x01",
            "２階、エプスタイン財団の\x01",
            "展示コーナーをご覧になってください。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_5559")

    label("loc_54C2")


    #C0250
    ChrTalk(
        0xFE,
        (
            "２階展示コーナーにありますのは\x01",
            "エプスタイン財団開発の\x01",
            "最新型ナントカ端末です。\x02",
        )
    )

    CloseMessageWindow()

    #C0251
    ChrTalk(
        0xFE,
        (
            "……将来はああいった製品が\x01",
            "一般的に流通するのでしょうかねえ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5559")

    Jump("loc_5A36")

    label("loc_555E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_5603")

    #C0252
    ChrTalk(
        0xFE,
        (
            "記念祭セールとして\x01",
            "オーバルカメラを売る予定なのです。\x02",
        )
    )

    CloseMessageWindow()

    #C0253
    ChrTalk(
        0xFE,
        (
            "カメラは最近、低価格化が進んで\x01",
            "だんだん庶民の手に届くものに\x01",
            "なりつつありますからねぇ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5A36")

    label("loc_5603")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_5670")

    #C0254
    ChrTalk(
        0xFE,
        (
            "記念祭に向けて\x01",
            "新製品を仕入れるつもりなのです。\x02",
        )
    )

    CloseMessageWindow()

    #C0255
    ChrTalk(
        0xFE,
        "ふふふ、来月が楽しみでなりませんな。\x02",
    )

    CloseMessageWindow()
    Jump("loc_5A36")

    label("loc_5670")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_56F2")

    #C0256
    ChrTalk(
        0xFE,
        (
            "ウェンディめ、昨日は\x01",
            "私に恥をかかせおって……\x02",
        )
    )

    CloseMessageWindow()

    #C0257
    ChrTalk(
        0xFE,
        (
            "少し詳しいからといって\x01",
            "いい気になってるんじゃないだろうな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5A36")

    label("loc_56F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_5746")
    OP_93(0xFE, 0x10E, 0x0)

    #C0258
    ChrTalk(
        0xFE,
        (
            "え、えーっと、ですから……\x01",
            "きゅ、吸引力とか……ですかね？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5A36")

    label("loc_5746")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_57E3")

    #C0259
    ChrTalk(
        0xFE,
        (
            "さあ、今日も一日\x01",
            "張り切って参りましょう！\x02",
        )
    )

    CloseMessageWindow()

    #C0260
    ChrTalk(
        0xFE,
        (
            "目標は打倒百貨店《タイムズ》です。\x01",
            "今月こそは、売り上げ記録を\x01",
            "塗り替えて差し上げますよっ！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5A36")

    label("loc_57E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_5913")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_58BE")

    #C0261
    ChrTalk(
        0xFE,
        (
            "古臭い陳列棚、\x01",
            "いびつで醜い工作装置の数々……\x02",
        )
    )

    CloseMessageWindow()

    #C0262
    ChrTalk(
        0xFE,
        (
            "ですがこれからの時代、工房も\x01",
            "美しくなければいけません！\x02",
        )
    )

    CloseMessageWindow()

    #C0263
    ChrTalk(
        0xFE,
        (
            "そう考えて清潔に美しく\x01",
            "デザインされた店舗が\x01",
            "《ゲンテン》のウリなのですよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_590E")

    label("loc_58BE")


    #C0264
    ChrTalk(
        0xFE,
        (
            "これからの時代、何物も\x01",
            "美しくなければいけません！\x01",
            "それが私の信念ですので。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_590E")

    Jump("loc_5A36")

    label("loc_5913")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_5A36")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_59D1")

    #C0265
    ChrTalk(
        0xFE,
        (
            "オーバルストア《ゲンテン》は\x01",
            "皆様の生活を便利にする\x01",
            "様々な商品をご提供しております。\x02",
        )
    )

    CloseMessageWindow()

    #C0266
    ChrTalk(
        0xFE,
        (
            "きっとお気に召す製品がございます。\x01",
            "心行くまでご覧になってください。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_5A36")

    label("loc_59D1")


    #C0267
    ChrTalk(
        0xFE,
        (
            "ちなみにこちらの高級導力車、\x01",
            "お値段は１５０万ミラとなります。\x02",
        )
    )

    CloseMessageWindow()

    #C0268
    ChrTalk(
        0xFE,
        "……いかがですかな、お客様？\x02",
    )

    CloseMessageWindow()

    label("loc_5A36")

    TalkEnd(0xFE)
    Return()

    # Function_12_4D90 end

    def Function_13_5A3A(): pass

    label("Function_13_5A3A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_5AC7")

    #C0269
    ChrTalk(
        0xFE,
        (
            "昔は道路を車が走るなんて\x01",
            "全く思ってなかったわねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0270
    ChrTalk(
        0xFE,
        (
            "将来はもっと思いもよらないものが\x01",
            "発明されていくんでしょうね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_63FF")

    label("loc_5AC7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_5B0C")

    #C0271
    ChrTalk(
        0xFE,
        (
            "こんな朝早くから来るなんて\x01",
            "私も好きねぇ……ふふ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_63FF")

    label("loc_5B0C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_5BA1")

    #C0272
    ChrTalk(
        0xFE,
        (
            "導力器ってやっぱりすごいわよね。\x01",
            "私たちの生活をこんなに便利に\x01",
            "してくれるんだもの。\x02",
        )
    )

    CloseMessageWindow()

    #C0273
    ChrTalk(
        0xFE,
        (
            "最初に発明した人は\x01",
            "本当に偉大だと思うわ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_63FF")

    label("loc_5BA1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_END)), "loc_5BAF")
    Jump("loc_63FF")

    label("loc_5BAF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_5CB9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5C6F")

    #C0274
    ChrTalk(
        0xFE,
        (
            "ここの店の店員さんは親切でね、\x01",
            "壊れた導力灯なんかを持っていくと\x01",
            "目の前で直してくれるのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0275
    ChrTalk(
        0xFE,
        (
            "おばさんビックリしちゃったわ。\x01",
            "世の中には凄い人がいるのねえ……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_5CB4")

    label("loc_5C6F")


    #C0276
    ChrTalk(
        0xFE,
        (
            "おばさん、導力製品は大好きだけど\x01",
            "仕組みとかはサッパリなのよね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5CB4")

    Jump("loc_63FF")

    label("loc_5CB9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_5D60")

    #C0277
    ChrTalk(
        0xFE,
        (
            "あら、あなた達も\x01",
            "導力レンジを買いに来たの？\x02",
        )
    )

    CloseMessageWindow()

    #C0278
    ChrTalk(
        0xFE,
        (
            "おばさんは今\x01",
            "新製品を見比べている所よ。\x02",
        )
    )

    CloseMessageWindow()

    #C0279
    ChrTalk(
        0xFE,
        (
            "大きな買い物だもの。\x01",
            "慎重に選ばなくっちゃね、うふふ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_63FF")

    label("loc_5D60")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_5E03")

    #C0280
    ChrTalk(
        0xFE,
        (
            "お店の人に聞いたら、\x01",
            "来週はヴェルヌ社製の導力カメラが\x01",
            "入荷するそうなのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0281
    ChrTalk(
        0xFE,
        (
            "うふふ……これは見逃せないわ。\x01",
            "来週も来なくちゃいけないわね～。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_63FF")

    label("loc_5E03")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_5EB8")

    #C0282
    ChrTalk(
        0xFE,
        (
            "オーバルストアを見て回るの、\x01",
            "どうしてこんなに楽しいのかしら。\x02",
        )
    )

    CloseMessageWindow()

    #C0283
    ChrTalk(
        0xFE,
        (
            "カラフルな導力製品……\x01",
            "洗練された機能美……\x02",
        )
    )

    CloseMessageWindow()

    #C0284
    ChrTalk(
        0xFE,
        (
            "ほんと、見てるだけで\x01",
            "不思議なほど楽しいわ～。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_63FF")

    label("loc_5EB8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_5F5F")

    #C0285
    ChrTalk(
        0xFE,
        (
            "この前の掃除機に続いて\x01",
            "今月は冷蔵庫を買うつもりなの。\x02",
        )
    )

    CloseMessageWindow()

    #C0286
    ChrTalk(
        0xFE,
        (
            "どれにしようかしら～。\x01",
            "大きな買い物だから悩んじゃうけど\x01",
            "おばさんは可愛いのがいいわねえ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_63FF")

    label("loc_5F5F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_5FF9")

    #C0287
    ChrTalk(
        0xFE,
        (
            "まあ、オシャレな新製品！\x01",
            "やっぱり新製品はいいわよねえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0288
    ChrTalk(
        0xFE,
        (
            "仕組みとか難しい話は知らないけど、\x01",
            "この目新しいフォルムがたまらないわ～。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_63FF")

    label("loc_5FF9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_6090")

    #C0289
    ChrTalk(
        0xFE,
        (
            "おばさんはアルカンシェルには\x01",
            "あまり興味ないわねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0290
    ChrTalk(
        0xFE,
        (
            "見てみたい気も少しするけど……\x01",
            "チケットの前に\x01",
            "最新の冷蔵庫を買いたいわ～。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_63FF")

    label("loc_6090")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_6194")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6147")

    #C0291
    ChrTalk(
        0xFE,
        (
            "ここのお店、観光客の人も\x01",
            "よく立ち寄っていくのよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0292
    ChrTalk(
        0xFE,
        "おばさんも分かるわ、その気持ち。\x02",
    )

    CloseMessageWindow()

    #C0293
    ChrTalk(
        0xFE,
        (
            "遠くからでも目立つから\x01",
            "ついつい立ち寄っちゃうのよねえ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_618F")

    label("loc_6147")


    #C0294
    ChrTalk(
        0xFE,
        (
            "『オーバルストア』なんて\x01",
            "外国人にはなおの事\x01",
            "物珍しいでしょうねえ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_618F")

    Jump("loc_63FF")

    label("loc_6194")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_6206")
    OP_93(0xFE, 0x5A, 0x0)

    #C0295
    ChrTalk(
        0xFE,
        "掃除機を買おうと思っているのよ。\x02",
    )

    CloseMessageWindow()

    #C0296
    ChrTalk(
        0xFE,
        (
            "あの赤いのと白いのじゃ\x01",
            "どういう差があるのかしら？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_63FF")

    label("loc_6206")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_6284")

    #C0297
    ChrTalk(
        0xFE,
        (
            "あらっ、今月は掃除機の新製品が\x01",
            "出ているみたいね！？\x02",
        )
    )

    CloseMessageWindow()

    #C0298
    ChrTalk(
        0xFE,
        (
            "うふふ……おばさん思い切って\x01",
            "買っちゃおうかしら。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_63FF")

    label("loc_6284")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_6306")

    #C0299
    ChrTalk(
        0xFE,
        (
            "ふむふむ、最近は随分と\x01",
            "オシャレな製品が増えてるのね。\x02",
        )
    )

    CloseMessageWindow()

    #C0300
    ChrTalk(
        0xFE,
        (
            "あれは……ＺＣＦ製ですって。\x01",
            "どこのメーカーかしら。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_63FF")

    label("loc_6306")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_63FF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_63C8")

    #C0301
    ChrTalk(
        0xFE,
        (
            "オーバルストア、だったかしら。\x01",
            "随分とカラフルな店なのねえ……\x02",
        )
    )

    CloseMessageWindow()

    #C0302
    ChrTalk(
        0xFE,
        (
            "導力灯を買いに来ただけのに\x01",
            "目移りしちゃうわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0303
    ChrTalk(
        0xFE,
        (
            "あらっ、あっちにある製品は\x01",
            "何なのかしら！？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_63FF")

    label("loc_63C8")


    #C0304
    ChrTalk(
        0xFE,
        (
            "あなた達もお買い物？\x01",
            "うふふ、おばさんと同じねえ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_63FF")

    TalkEnd(0xFE)
    Return()

    # Function_13_5A3A end

    def Function_14_6403(): pass

    label("Function_14_6403")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_6522")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_64F4")

    #C0305
    ChrTalk(
        0xFE,
        (
            "チャコは元々百貨店の受付を\x01",
            "目指していたんだが……\x01",
            "私が反対してしまったんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0306
    ChrTalk(
        0xFE,
        (
            "そういう負い目もあって\x01",
            "チャコが無事に仕事できるよう\x01",
            "見守ることにしたのさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0307
    ChrTalk(
        0xFE,
        (
            "まだ危なっかしいから\x01",
            "目を離せないけどね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_651D")

    label("loc_64F4")


    #C0308
    ChrTalk(
        0xFE,
        (
            "チャコ……\x01",
            "お父さんがついてるぞ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_651D")

    Jump("loc_704F")

    label("loc_6522")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_65B3")

    #C0309
    ChrTalk(
        0xFE,
        (
            "ときどき、僕の存在が\x01",
            "チャコにとって迷惑じゃないかとも\x01",
            "考えることもあるが……\x02",
        )
    )

    CloseMessageWindow()

    #C0310
    ChrTalk(
        0xFE,
        (
            "まぁ、そんなことはないと\x01",
            "いつも思い直すよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_704F")

    label("loc_65B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_66EB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6677")

    #C0311
    ChrTalk(
        0xFE,
        (
            "昨日はチャコにあんなことを\x01",
            "言われてしまったが……\x02",
        )
    )

    CloseMessageWindow()

    #C0312
    ChrTalk(
        0xFE,
        (
            "一人娘の仕事振りが心配なのは\x01",
            "父親なら当たり前だろう？\x02",
        )
    )

    CloseMessageWindow()

    #C0313
    ChrTalk(
        0xFE,
        (
            "なに、今度からばれないように\x01",
            "見守ればいいだけさ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_66E6")

    label("loc_6677")


    #C0314
    ChrTalk(
        0xFE,
        "なるべく無関係を装って……\x02",
    )

    CloseMessageWindow()

    #C0315
    ChrTalk(
        0xFE,
        "チラッ。\x02",
    )

    CloseMessageWindow()

    #C0316
    ChrTalk(
        0xFE,
        (
            "……うむ、がんばっているなチャコ。\x01",
            "お父さんは嬉しいぞ……！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_66E6")

    Jump("loc_704F")

    label("loc_66EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_END)), "loc_66F9")
    Jump("loc_704F")

    label("loc_66F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_6707")
    Jump("loc_704F")

    label("loc_6707")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_677F")

    #C0317
    ChrTalk(
        0xFE,
        (
            "……今日も娘は\x01",
            "元気に働いているようだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0318
    ChrTalk(
        0xFE,
        (
            "オーバルストアで働くなど\x01",
            "心配だったが……感心、感心。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_704F")

    label("loc_677F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_6800")

    #C0319
    ChrTalk(
        0xFE,
        (
            "さて……\x01",
            "チャコの様子を見ないと。\x02",
        )
    )

    CloseMessageWindow()

    #C0320
    ChrTalk(
        0xFE,
        (
            "どうも私が来ているのに\x01",
            "気づいているみたいだから、\x01",
            "慎重にしないとな……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_704F")

    label("loc_6800")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_68A7")

    #C0321
    ChrTalk(
        0xFE,
        (
            "導力ネットワークが整備されているのは\x01",
            "今のところ一部の企業くらいだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0322
    ChrTalk(
        0xFE,
        (
            "ＩＢＣくらいの規模になると\x01",
            "すでに実用レベルに\x01",
            "達してるんじゃないかな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_704F")

    label("loc_68A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_6975")

    #C0323
    ChrTalk(
        0xFE,
        (
            "ああ、チャコ……\x01",
            "若い娘がこんな時間まで\x01",
            "働いているなんて。\x02",
        )
    )

    CloseMessageWindow()

    #C0324
    ChrTalk(
        0xFE,
        (
            "帰りに暴漢に襲われたりしたら\x01",
            "一体どうするつもりなんだ……\x02",
        )
    )

    CloseMessageWindow()

    #C0325
    ChrTalk(
        0xFE,
        (
            "あたたかい夕食を用意しているから\x01",
            "早く家に帰って欲しい……！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_704F")

    label("loc_6975")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_69FB")

    #C0326
    ChrTalk(
        0xFE,
        (
            "しかし……オーバルカメラか。\x01",
            "そろそろ購入を考えてもいい時期かな。\x02",
        )
    )

    CloseMessageWindow()

    #C0327
    ChrTalk(
        0xFE,
        (
            "最近のは随分小型化が\x01",
            "進んでいるというし……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_704F")

    label("loc_69FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_6B67")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6AF0")

    #C0328
    ChrTalk(
        0xFE,
        (
            "ふむふむ、これは\x01",
            "ＺＣＦ製の新製品だね。\x02",
        )
    )

    CloseMessageWindow()

    #C0329
    ChrTalk(
        0xFE,
        (
            "ＺＣＦは『ツァイス中央工房』の略で\x01",
            "リベール王国の時計工房を前身とする\x01",
            "技術者集団なんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0330
    ChrTalk(
        0xFE,
        (
            "非常に高い技術力を持っていてね、\x01",
            "特に飛行船技術は世界一と言っていいよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_6B62")

    label("loc_6AF0")


    #C0331
    ChrTalk(
        0xFE,
        (
            "ＺＣＦは世界で初めて\x01",
            "導力飛行船を実用化したんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0332
    ChrTalk(
        0xFE,
        (
            "今でも国際定期便なんかは\x01",
            "ＺＣＦが製造しているんだよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6B62")

    Jump("loc_704F")

    label("loc_6B67")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_6C78")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6C3A")

    #C0333
    ChrTalk(
        0xFE,
        (
            "おっ、これは\x01",
            "ヴェルヌ社製の新式ペンライト！\x02",
        )
    )

    CloseMessageWindow()

    #C0334
    ChrTalk(
        0xFE,
        (
            "……私はヴェルヌ社系列の\x01",
            "工房に勤めていてね。\x01",
            "同僚が研究していたものなんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0335
    ChrTalk(
        0xFE,
        (
            "ついに製品化したんだな。\x01",
            "ちょっと感慨深いよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_6C73")

    label("loc_6C3A")


    #C0336
    ChrTalk(
        0xFE,
        (
            "そうか、ついに完成したのか……\x01",
            "ちょっと感慨深いよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6C73")

    Jump("loc_704F")

    label("loc_6C78")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_6D5B")

    #C0337
    ChrTalk(
        0xFE,
        (
            "帝国ラインフォルト社は\x01",
            "武器メーカーとして有名だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0338
    ChrTalk(
        0xFE,
        (
            "しかし実際は巨大複合企業#12Rコ ン グ ロ マ リ ッ ト#でね、\x01",
            "導力製品も数多く手がけているんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0339
    ChrTalk(
        0xFE,
        (
            "帝国人気質を反映してか\x01",
            "質実剛健な製品が多いけどね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_704F")

    label("loc_6D5B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_6EF1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6E59")

    #C0340
    ChrTalk(
        0xFE,
        (
            "現在、有名な\x01",
            "導力器メーカーは４つある。\x02",
        )
    )

    CloseMessageWindow()

    #C0341
    ChrTalk(
        0xFE,
        (
            "帝国ラインフォルト社、共和国ヴェルヌ社\x01",
            "エプスタイン財団、リベールのＺＣＦだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0342
    ChrTalk(
        0xFE,
        (
            "このうちエプスタイン財団は\x01",
            "研究目的の開発が多くてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0343
    ChrTalk(
        0xFE,
        "一般向けの製品は数が少ないんだよ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_6EEC")

    label("loc_6E59")


    #C0344
    ChrTalk(
        0xFE,
        (
            "エプスタイン財団は\x01",
            "研究目的の開発が多くてね。\x01",
            "一般向けの製品は数が少ないんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0345
    ChrTalk(
        0xFE,
        (
            "その分変わった製品が多くてね。\x01",
            "眺めていると中々面白いよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6EEC")

    Jump("loc_704F")

    label("loc_6EF1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_6FB3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6F6A")

    #C0346
    ChrTalk(
        0xFE,
        (
            "……さて、チャコは\x01",
            "仕事を頑張っているかな。\x02",
        )
    )

    CloseMessageWindow()

    #C0347
    ChrTalk(
        0xFE,
        (
            "心配になっていつも\x01",
            "覗きに来てしまうよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_6FAE")

    label("loc_6F6A")


    #C0348
    ChrTalk(
        0xFE,
        (
            "……い、言っておくが\x01",
            "私はストーカーの類では\x01",
            "断じてないからね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6FAE")

    Jump("loc_704F")

    label("loc_6FB3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_704F")

    #C0349
    ChrTalk(
        0xFE,
        (
            "私は導力器メーカーに\x01",
            "いたんだがすでに退職してね。\x02",
        )
    )

    CloseMessageWindow()

    #C0350
    ChrTalk(
        0xFE,
        (
            "クロスベルには\x01",
            "世界中から様々な品物が\x01",
            "集まってくる。\x02",
        )
    )

    CloseMessageWindow()

    #C0351
    ChrTalk(
        0xFE,
        "鑑賞するにはもってこいだよ。\x02",
    )

    CloseMessageWindow()

    label("loc_704F")

    TalkEnd(0xFE)
    Return()

    # Function_14_6403 end

    def Function_15_7053(): pass

    label("Function_15_7053")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(11560, 1500, 5410, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(26850, 0)
    SetChrPos(0x101, -2990, 0, 1860, 89)
    SetChrPos(0x102, -3340, 0, 3240, 45)
    SetChrPos(0x103, -4740, 0, 3260, 45)
    SetChrPos(0x104, -4310, 0, 1920, 90)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    SetCameraDistance(24490, 3000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    Fade(500)
    OP_68(14920, 1500, 20510, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(43880, 0)
    OP_68(4170, 1500, 6370, 5000)
    OP_6F(0x79)
    Fade(500)
    OP_68(-2550, 1500, 2270, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(22240, 0)
    OP_0D()

    #C0352
    ChrTalk(
        0x104,
        (
            "#0305F#6Pへえ……\x01",
            "ここが《オーバルストア》かよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0353
    ChrTalk(
        0x102,
        (
            "#0105F#5P最新の導力車から\x01",
            "家庭用の生活導力製品まで……\x02\x03",

            "#0102F随分、近未来的というか\x01",
            "真新しいデザインの内装みたいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0354
    ChrTalk(
        0x101,
        (
            "#0011F#5P３年前には普通の工房店だったと\x01",
            "思うんだけど……\x02\x03",

            "#0001Fええと、ともかく\x01",
            "オーブメントの調整を頼んでみよう。\x01",
            "場所は……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 500)

    #C0355
    ChrTalk(
        0x103,
        (
            "#0203F#5P確かサポートカウンターがあると\x01",
            "聞いています。\x02\x03",

            "#0200Fカウンターで頼めば\x01",
            "各種調整を行ってくれるはずです。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 500)

    #C0356
    ChrTalk(
        0x101,
        (
            "#0000F#11Pそうか……\x01",
            "よし、行ってみるとしよう。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, -3570, 0, 2660, 89)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    SetScenarioFlags(0x4B, 2)
    EventEnd(0x5)
    Return()

    # Function_15_7053 end

    def Function_16_737B(): pass

    label("Function_16_737B")

    EventBegin(0x0)
    OP_4B(0x9, 0xFF)
    Fade(800)
    OP_68(6570, 1500, -1770, 0)
    MoveCamera(49, 21, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(21780, 0)
    SetChrPos(0x101, 6620, 0, -1810, 90)
    SetChrPos(0x102, 5650, 0, -2670, 90)
    SetChrPos(0x103, 5650, 0, -1320, 90)
    SetChrPos(0x104, 5650, 0, -200, 90)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    OP_0D()

    #C0357
    ChrTalk(
        0x9,
        (
            "#11Pあ、ロイドに皆さん。\x01",
            "いらっしゃーい！\x02",
        )
    )

    CloseMessageWindow()

    #C0358
    ChrTalk(
        0x101,
        (
            "#6P#0000Fウェンディ、\x01",
            "エニグマの実戦テスト……\x01",
            "とかいう仕事はここでいいのかな。\x02\x03",

            "支援課に要請が来てたんだけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0359
    ChrTalk(
        0x9,
        "#11Pあっ、あの話ね？\x02",
    )

    CloseMessageWindow()

    #C0360
    ChrTalk(
        0x9,
        "#11Pうんうん、私が出した依頼よ。\x02",
    )

    CloseMessageWindow()

    #C0361
    ChrTalk(
        0x9,
        (
            "#11Pちょっと財団から頼まれてる事があって……\x01",
            "エニグマ利用者に\x01",
            "協力してほしいかなと思ったの。\x02",
        )
    )

    CloseMessageWindow()

    #C0362
    ChrTalk(
        0x9,
        (
            "#11Pでもロイド達が受けてくれたんだ。\x01",
            "助かるわ～！\x02",
        )
    )

    CloseMessageWindow()

    #C0363
    ChrTalk(
        0x102,
        (
            "#6P#0100F私たちにできる事なら喜んで。\x02\x03",

            "それで、お仕事の内容は\x01",
            "どういったものなんですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0364
    ChrTalk(
        0x9,
        (
            "#11Pえへへ、そんなに\x01",
            "難しい話じゃないんだけどね。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1200)

    #C0365
    ChrTalk(
        0x9,
        (
            "みんなにはエニグマの\x01",
            "『性能評価プログラム』に\x01",
            "参加してほしいの！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_63(0x0, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x1, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x2, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x3, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0x0)
    OP_64(0x1)
    OP_64(0x2)
    OP_64(0x3)
    Sleep(500)

    #C0366
    ChrTalk(
        0x101,
        "#6P#0005Fえっと、それは一体……\x02",
    )

    CloseMessageWindow()

    #C0367
    ChrTalk(
        0x9,
        (
            "#11Pエプスタイン財団が\x01",
            "《エニグマ》を扱っている工房に\x01",
            "打診しているアンケートよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0368
    ChrTalk(
        0x9,
        (
            "#11Pほらエニグマって新型だし\x01",
            "まだ普及し始めたばかりでしょ？\x02",
        )
    )

    CloseMessageWindow()

    #C0369
    ChrTalk(
        0x9,
        (
            "#11P財団の方も仕様を調整#2Rチューニング#中みたいでね。\x01",
            "工房サイドにも性能や\x01",
            "使い勝手なんかを聞いてるわけ。\x02",
        )
    )

    CloseMessageWindow()

    #C0370
    ChrTalk(
        0x103,
        (
            "#6P#0203Fそれがエプスタイン財団の\x01",
            "『性能評価プログラム』……\x02\x03",

            "#0200F実用レベルでの耐久性や使用感、\x01",
            "トラブルなどの情報を\x01",
            "集めているわけですね。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x103, 400)
    Sleep(300)

    #C0371
    ChrTalk(
        0x104,
        (
            "#5P#0300Fつーかティオすけも\x01",
            "財団の関係者だろ？\x01",
            "何も知らなかったのか？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_78E7():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_78E7)

    def lambda_78F4():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_78F4)
    Sleep(100)
    TurnDirection(0x103, 0x104, 400)
    Sleep(300)

    #C0372
    ChrTalk(
        0x103,
        (
            "#12P#0200Fいえ、わたしは\x01",
            "魔導杖開発チームですから。\x02\x03",

            "魔導杖の実戦テストを\x01",
            "している所ですが。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0373
    ChrTalk(
        0x101,
        (
            "#11P#0000Fそうだった……\x01",
            "何となく忘れてたよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0374
    ChrTalk(
        0x9,
        (
            "#11Pあはは……\x01",
            "財団は開発チームごとに\x01",
            "色んなテストをしてるみたいね。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_7A38():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_7A38)

    def lambda_7A45():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_7A45)

    def lambda_7A52():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_7A52)

    def lambda_7A5F():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_7A5F)
    Sleep(500)

    #C0375
    ChrTalk(
        0x9,
        (
            "#11Pでね、大体の評価項目は\x01",
            "書き終えたんだけど\x01",
            "問題は『実戦での性能評価』なのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0376
    ChrTalk(
        0x9,
        (
            "#11Pま、私がてきとーに\x01",
            "試しちゃってもいいんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0377
    ChrTalk(
        0x9,
        (
            "#11Pエンジニアとしては\x01",
            "やっぱりきちんと利用者の意見を\x01",
            "聞きたいじゃない？\x02",
        )
    )

    CloseMessageWindow()

    #C0378
    ChrTalk(
        0x102,
        "#6P#0100Fなるほど、それで依頼を。\x02",
    )

    CloseMessageWindow()

    #C0379
    ChrTalk(
        0x101,
        (
            "#6P#0000Fウェンディらしい話だな……\x02\x03",

            "分かった、引き受けるよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0380
    ChrTalk(
        0x9,
        "#11Pありがと、ロイドー！\x02",
    )

    CloseMessageWindow()

    #C0381
    ChrTalk(
        0x101,
        (
            "#6P#0000Fはは、そう難しい依頼でも\x01",
            "なさそうだしさ。\x02\x03",

            "で、具体的には\x01",
            "何をすればいいんだ？\x02",
        )
    )

    CloseMessageWindow()

    #C0382
    ChrTalk(
        0x9,
        (
            "#11Pうん、簡単簡単。\x01",
            "『敵から認識されなくなるアーツ』\x01",
            "っていうのを使ってみてほしいの。\x02",
        )
    )

    CloseMessageWindow()

    #C0383
    ChrTalk(
        0x9,
        (
            "#11P何でもエニグマで初めて\x01",
            "利用可能になったアーツらしいわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0384
    ChrTalk(
        0x101,
        (
            "#6P#0000F『敵から認識されなくなるアーツ』……\x01",
            "そいつが正しく\x01",
            "発動できればいいんだな？\x02",
        )
    )

    CloseMessageWindow()

    #C0385
    ChrTalk(
        0x103,
        (
            "#6P#0200F効果からして\x01",
            "かなり特殊なアーツのようですね。\x02\x03",

            "うまくクオーツを組み合わせる\x01",
            "必要がありそうですが……\x01",
            "まあ色々試してみましょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0386
    ChrTalk(
        0x104,
        (
            "#5P#0309Fはは、頼りにしてるぜ\x01",
            "ティオすけ。\x02\x03",

            "#0300Fあとは……実際の戦闘でも使って\x01",
            "効果の程も確認してみねえとな。\x02",
        )
    )

    CloseMessageWindow()

    #C0387
    ChrTalk(
        0x102,
        (
            "#6P#0100Fええ、確認しましょう。\x02\x03",

            "ついでにエニグマの使用感なんかも\x01",
            "気をつけていた方がよさそうね。\x02",
        )
    )

    CloseMessageWindow()

    #C0388
    ChrTalk(
        0x9,
        "#11Pお願いするわ。\x02",
    )

    CloseMessageWindow()

    #C0389
    ChrTalk(
        0x9,
        (
            "#11Pじゃ、アーツが\x01",
            "確認できたら報告に来てね。\x01",
            "よろしくっ！\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    FadeToDark(300, 0, 100)
    Sound(80, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0390
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "クエスト【エニグマの実戦テスト】\x07\x00",
            "を開始した！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    ClearScenarioFlags(0x5A, 7)
    SetChrPos(0x0, 6620, 0, -1810, 90)
    OP_4C(0x9, 0xFF)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    OP_29(0xE, 0x1, 0x0)
    EventEnd(0x5)
    Return()

    # Function_16_737B end

    def Function_17_7F79(): pass

    label("Function_17_7F79")

    EventBegin(0x0)
    OP_4B(0x9, 0xFF)
    Fade(800)
    OP_68(6570, 1500, -1770, 0)
    MoveCamera(49, 21, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(21780, 0)
    SetChrPos(0x101, 6620, 0, -1810, 90)
    SetChrPos(0x102, 5650, 0, -2670, 90)
    SetChrPos(0x103, 5650, 0, -1320, 90)
    SetChrPos(0x104, 5650, 0, -200, 90)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    OP_0D()

    #C0391
    ChrTalk(
        0x9,
        "#11Pあ、ロイド。\x02",
    )

    CloseMessageWindow()

    #C0392
    ChrTalk(
        0x9,
        (
            "#11P例のエニグマのテストの件、\x01",
            "どうなったの？\x02",
        )
    )

    CloseMessageWindow()

    #C0393
    ChrTalk(
        0x101,
        (
            "#6P#0000Fああ、大丈夫だ。\x01",
            "実戦で使ってみたよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0394
    ChrTalk(
        0x103,
        (
            "#6P#0203F『ホロウスフィア』ですね。\x02\x03",

            "#0200F確かに相手からは\x01",
            "認識されなくなっていたようです。\x02",
        )
    )

    CloseMessageWindow()

    #C0395
    ChrTalk(
        0x104,
        (
            "#5P#0300F幻属性の特性を\x01",
            "最大限に生かしたアーツって所か。\x02\x03",

            "エニグマには毎度お世話になってるが\x01",
            "使えるアーツも増えたし\x01",
            "便利になったもんだぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0396
    ChrTalk(
        0x102,
        (
            "#6P#0100Fそうね、戦闘以外でも\x01",
            "通信機能が凄く便利だし。\x02\x03",

            "まあ……クオーツの合成や\x01",
            "スロットの開封が大変なのは\x01",
            "旧式と変わらないけれど。\x02",
        )
    )

    CloseMessageWindow()

    #C0397
    ChrTalk(
        0x9,
        (
            "#11Pうんうん、なるほどね……\x01",
            "（サラサラ……）\x02",
        )
    )

    CloseMessageWindow()

    #C0398
    ChrTalk(
        0x9,
        (
            "#11Pうん、これでレポートも\x01",
            "きっちり纏められそうかな。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1200)

    #C0399
    ChrTalk(
        0x9,
        (
            "#11Pロイドに皆さん、\x01",
            "協力してくれてありがとう。\x02",
        )
    )

    CloseMessageWindow()

    #C0400
    ChrTalk(
        0x9,
        (
            "#11Pお礼といっちゃなんだけど……\x01",
            "今日はこれを持ってっちゃって頂戴。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0401
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0xAF),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を受け取った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0xAF, 1)

    #C0402
    ChrTalk(
        0x101,
        "#6P#0005Fこれは……？\x02",
    )

    CloseMessageWindow()

    #C0403
    ChrTalk(
        0x9,
        (
            "#11Pなんでも中世の遺跡から発掘された\x01",
            "年代物のクオーツみたいよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0404
    ChrTalk(
        0x9,
        (
            "#11P前の工房時代の倉庫を\x01",
            "あさっていたら出てきたの。\x02",
        )
    )

    CloseMessageWindow()

    #C0405
    ChrTalk(
        0x104,
        (
            "#5P#0305F発掘品……\x01",
            "そんな物が使えんのかよ！？\x02",
        )
    )

    CloseMessageWindow()

    #C0406
    ChrTalk(
        0x103,
        (
            "#6P#0200F理論的には作動しても\x01",
            "不思議ではないかと。\x02\x03",

            "そもそもオーブメント技術は\x01",
            "古代の結晶回路を解析することで\x01",
            "生み出された物ですし。\x02\x03",

            "大崩壊以前の結晶回路が\x01",
            "利用できたという報告もあるそうです。\x02",
        )
    )

    CloseMessageWindow()

    #C0407
    ChrTalk(
        0x9,
        (
            "#11Pそうなのよね。\x01",
            "ちょっとワクワクする話だと思わない？\x02",
        )
    )

    CloseMessageWindow()

    #C0408
    ChrTalk(
        0x9,
        (
            "#11Pま、１００％の性能は保証できないけど\x01",
            "まだ導力反応があるみたいだし。\x02",
        )
    )

    CloseMessageWindow()

    #C0409
    ChrTalk(
        0x9,
        (
            "#11P軽く加工しておいたから\x01",
            "エニグマでも利用できると思うわ！\x02",
        )
    )

    CloseMessageWindow()

    #C0410
    ChrTalk(
        0x101,
        (
            "#6P#0000Fはは、ウェンディのお宝ってわけか……\x02\x03",

            "サンキュー、受け取っておくよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0411
    ChrTalk(
        0x104,
        (
            "#5P#0300Fありがたく\x01",
            "使わせてもらうぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0412
    ChrTalk(
        0x102,
        (
            "#6P#0100Fウェンディさん、\x01",
            "また何かあったら\x01",
            "支援課にご依頼下さいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0413
    ChrTalk(
        0x9,
        "#11Pうん、その時はよろしく！\x02",
    )

    CloseMessageWindow()
    OP_5A()
    FadeToDark(300, 0, 100)
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0414
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "クエスト【エニグマの実戦テスト】\x07\x00",
            "を達成した！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, 6620, 0, -1810, 90)
    OP_4C(0x9, 0xFF)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    OP_29(0xE, 0x4, 0x10)
    OP_29(0xE, 0x1, 0x2)
    SetScenarioFlags(0x0, 5)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_17_7F79 end

    SaveToFile()

Try(main)
