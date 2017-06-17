from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c014c.bin",                # FileName
        "c014c",                    # MapName
        "c014c",                    # Location
        0x0006,                     # MapIndex
        "ed7100",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 6, 0, 2, 0, 3],
    )

    BuildStringList((
        "c014c",                  # 0
        "チャコ",                 # 1
        "ウェンディ",             # 2
        "フェルナンド",           # 3
        "ミゼット",               # 4
        "バジリオ",               # 5
        "観光客",                 # 6
        "観光客",                 # 7
    ))

    AddCharChip((
        "chr/ch26100.itc",                   # 00
        "chr/ch27800.itc",                   # 01
        "chr/ch25700.itc",                   # 02
        "chr/ch21000.itc",                   # 03
        "chr/ch20800.itc",                   # 04
        "chr/ch21900.itc",                   # 05
        "chr/ch24400.itc",                   # 06
        "chr/ch33200.itc",                   # 07
    ))

    DeclNpc(9270,    0,       2650,    270,  261,  0x0, 0,   2,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(9329,    0,       -1350,   270,  261,  0x0, 0,   0,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(-1519,   0,       14659,   180,  261,  0x0, 0,   1,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(-4480,   0,       7440,    0,    261,  0x0, 0,   5,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(2299,    0,       6420,    90,   261,  0x0, 0,   3,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(11119,   4000,    8699,    90,   261,  0x0, 0,   6,   0,   0,   0,   0,   14,  255,  0)
    DeclNpc(-3309,   0,       790,     90,   261,  0x0, 0,   7,   0,   0,   0,   0,   15,  255,  0)

    DeclActor(8130,    0,       3080,    1000,    9270,    1500,    3140,    0x007E, 0,  4,  0x0000)
    DeclActor(8310,    0,       -1360,   1000,    9330,    1500,    -1350,   0x007E, 0,  7,  0x0000)

    ScpFunction((
        "Function_0_200",          # 00, 0
        "Function_1_2B8",          # 01, 1
        "Function_2_409",          # 02, 2
        "Function_3_4FB",          # 03, 3
        "Function_4_4FC",          # 04, 4
        "Function_5_6C6",          # 05, 5
        "Function_6_F23",          # 06, 6
        "Function_7_1341",         # 07, 7
        "Function_8_1345",         # 08, 8
        "Function_9_2200",         # 09, 9
        "Function_10_2A78",        # 0A, 10
        "Function_11_2E76",        # 0B, 11
        "Function_12_3216",        # 0C, 12
        "Function_13_3609",        # 0D, 13
        "Function_14_36B2",        # 0E, 14
        "Function_15_3AB0",        # 0F, 15
    ))


    def Function_0_200(): pass

    label("Function_0_200")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_240"),
        (1, "loc_24C"),
        (2, "loc_258"),
        (3, "loc_264"),
        (4, "loc_270"),
        (5, "loc_27C"),
        (6, "loc_288"),
        (SWITCH_DEFAULT, "loc_294"),
    )


    label("loc_240")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_2A0")

    label("loc_24C")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_2A0")

    label("loc_258")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_2A0")

    label("loc_264")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_2A0")

    label("loc_270")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_2A0")

    label("loc_27C")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_2A0")

    label("loc_288")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2A0")

    label("loc_294")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2A0")

    label("loc_2A0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2B7")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2A0")

    label("loc_2B7")

    Return()

    # Function_0_200 end

    def Function_1_2B8(): pass

    label("Function_1_2B8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_408")
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
    Jump("Function_1_2B8")

    label("loc_408")

    Return()

    # Function_1_2B8 end

    def Function_2_409(): pass

    label("Function_2_409")

    BeginChrThread(0xB, 0, 0, 1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_450")
    SetChrPos(0xC, 11460, 4000, 8870, 90)
    SetChrPos(0xD, 10670, 4000, 15920, 0)
    SetChrPos(0xE, 1050, 0, 3500, 90)
    Jump("loc_4FA")

    label("loc_450")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_46F")
    SetChrPos(0xE, 1680, 0, 12640, 0)
    Jump("loc_4FA")

    label("loc_46F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_49F")
    SetChrPos(0xD, 11460, 4000, -1040, 90)
    SetChrPos(0xE, 40, 0, 4670, 315)
    Jump("loc_4FA")

    label("loc_49F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_END)), "loc_4CF")
    SetChrPos(0xD, 9090, 4000, 3890, 180)
    SetChrPos(0xE, 3670, 0, -2980, 0)
    Jump("loc_4FA")

    label("loc_4CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_4FA")
    SetChrPos(0xD, 11040, 4000, 7060, 225)
    SetChrPos(0xE, 310, 0, -2980, 0)

    label("loc_4FA")

    Return()

    # Function_2_409 end

    def Function_3_4FB(): pass

    label("Function_3_4FB")

    Return()

    # Function_3_4FB end

    def Function_4_4FC(): pass

    label("Function_4_4FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF1, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6BC")
    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x71, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_601")

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

    label("loc_601")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_60B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6B4")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_66F")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_66F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_690")
    Call(0, 6)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6AF")

    label("loc_690")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6AF")
    OP_60(0x0)
    Call(0, 5)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6AF")

    Jump("loc_60B")

    label("loc_6B4")

    TalkEnd(0x8)
    Jump("loc_6C5")

    label("loc_6BC")

    TalkBegin(0x8)
    Call(0, 6)
    TalkEnd(0x8)

    label("loc_6C5")

    Return()

    # Function_4_4FC end

    def Function_5_6C6(): pass

    label("Function_5_6C6")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6D0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F22")
    MenuCmd(0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 5)), scpexpr(EXPR_END)), "loc_716")
    MenuCmd(1, 0, "ブルーシェリフ　　　　購入済み")
    MenuCmd(3, 0, 0x0)
    Jump("loc_738")

    label("loc_716")

    MenuCmd(1, 0, "ブルーシェリフ　　　　1000ミラ")

    label("loc_738")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 6)), scpexpr(EXPR_END)), "loc_76C")
    MenuCmd(1, 0, "ピースグリーン　　　　購入済み")
    MenuCmd(3, 0, 0x1)
    Jump("loc_78E")

    label("loc_76C")

    MenuCmd(1, 0, "ピースグリーン　　　　1000ミラ")

    label("loc_78E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 7)), scpexpr(EXPR_END)), "loc_7C2")
    MenuCmd(1, 0, "ブラックキャット　　　購入済み")
    MenuCmd(3, 0, 0x2)
    Jump("loc_7E4")

    label("loc_7C2")

    MenuCmd(1, 0, "ブラックキャット　　　1000ミラ")

    label("loc_7E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF1, 0)), scpexpr(EXPR_END)), "loc_818")
    MenuCmd(1, 0, "デンジャーオレンジ　　購入済み")
    MenuCmd(3, 0, 0x3)
    Jump("loc_83A")

    label("loc_818")

    MenuCmd(1, 0, "デンジャーオレンジ　　1000ミラ")

    label("loc_83A")

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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_88F")
    Sleep(1)
    Return()

    label("loc_88F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8CF")
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis172.itp")
    Jump("loc_98A")

    label("loc_8CF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_90F")
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis173.itp")
    Jump("loc_98A")

    label("loc_90F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_94F")
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis174.itp")
    Jump("loc_98A")

    label("loc_94F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_98A")
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis175.itp")

    label("loc_98A")

    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A43")

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
    Jump("loc_BF9")

    label("loc_A43")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AD6")

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
    Jump("loc_BF9")

    label("loc_AD6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B69")

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
    Jump("loc_BF9")

    label("loc_B69")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BF9")

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

    label("loc_BF9")


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
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F05")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x12), scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_CEC")

    #C0010
    ChrTalk(
        0x8,
        (
            "あれ～、ミラが足りないみたいですよ？\x01",
            "それじゃ交換はできないですぅ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EF6")

    label("loc_CEC")


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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DAC")

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
    Jump("loc_E84")

    label("loc_DAC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DF5")

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
    Jump("loc_E84")

    label("loc_DF5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E3E")

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
    Jump("loc_E84")

    label("loc_E3E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E84")

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

    label("loc_E84")

    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x50, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x50, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF1, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_EBF")
    OP_DE(0x16, 0x0)

    label("loc_EBF")


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

    label("loc_EF6")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_F0F")

    label("loc_F05")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_F0F")

    OP_CA(0x1, 0xFF, 0x0)
    FadeToDark(300, 0, 100)
    Jump("loc_6D0")

    label("loc_F22")

    Return()

    # Function_5_6C6 end

    def Function_6_F23(): pass

    label("Function_6_F23")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_1050")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1014")

    #C0018
    ChrTalk(
        0x8,
        (
            "今年も記念祭は\x01",
            "大きな事件もなく終わりそうで、\x01",
            "よかったですねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x8,
        "やっぱり平和が一番ですよ。\x02",
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x101,
        (
            "#0003F（う～ん、かなり色々と\x01",
            "  起こっていたけど……）\x02\x03",

            "#0000F（まぁ、警察と市民の\x01",
            "  温度差ってやつかな。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_104B")

    label("loc_1014")


    #C0021
    ChrTalk(
        0x8,
        (
            "記念祭は何事もなく終わりそうで\x01",
            "よかったですねぇ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_104B")

    Jump("loc_1340")

    label("loc_1050")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_1135")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10DD")

    #C0022
    ChrTalk(
        0x8,
        (
            "パレードの写真、\x01",
            "いっぱい撮っちゃいましたぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x8,
        (
            "……展示用のカメラで。\x01",
            "あとでこっそり現像しなきゃですぅ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1130")

    label("loc_10DD")


    #C0024
    ChrTalk(
        0x8,
        (
            "展示用のいいカメラで\x01",
            "パレードの写真を撮りました。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x8,
        "店長には内緒ですよぉ？\x02",
    )

    CloseMessageWindow()

    label("loc_1130")

    Jump("loc_1340")

    label("loc_1135")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_11B9")

    #C0026
    ChrTalk(
        0x8,
        (
            "店頭には性能比較用の\x01",
            "デモ製品を置いてるんですよぉ。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x8,
        (
            "実際に使い心地を確かめてから\x01",
            "買ってみてはどうですかぁ？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1340")

    label("loc_11B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_END)), "loc_124F")

    #C0028
    ChrTalk(
        0x8,
        "明日はパレードですねぇ。\x02",
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x8,
        (
            "記念撮影用にオーバルカメラ、\x01",
            "どうですかぁ？\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x8,
        (
            "以前に比べれば、\x01",
            "結構お求め安い価格になってますよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1340")

    label("loc_124F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_12CB")

    #C0031
    ChrTalk(
        0x8,
        (
            "友達は今日からミシュラムに\x01",
            "行くそうなんですよぉ。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x8,
        (
            "あ～ん、私も仕事がなかったら\x01",
            "行きたかったですぅ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1340")

    label("loc_12CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1340")

    #C0033
    ChrTalk(
        0x8,
        "いやぁ、外は凄い人出ですねー。\x02",
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x8,
        (
            "まぁ、オーバルストアの中は\x01",
            "いつもと余り\x01",
            "変わらないんですけどねぇ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1340")

    Return()

    # Function_6_F23 end

    def Function_7_1341(): pass

    label("Function_7_1341")

    Call(0, 8)
    Return()

    # Function_7_1341 end

    def Function_8_1345(): pass

    label("Function_8_1345")

    TalkBegin(0x9)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1352")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_21FC")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_13BD")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_13BD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1737")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD9, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_16D6")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    #C0035
    ChrTalk(
        0x9,
        (
            "そうだ、ロイドたちって\x01",
            "『上位クオーツ』を持ってたりしない？\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x101,
        "#0005F『上位クオーツ』……？\x02",
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x9,
        (
            "うんうん、強力すぎて普通のスロットには\x01",
            "セットできないクオーツなの。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x9,
        (
            "セットするためには\x01",
            "スロット自体の強化が必要になるわ。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_155D")

    #C0039
    ChrTalk(
        0x9,
        (
            "上位クオーツ自体は\x01",
            "うちでもまだ扱ってないんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x9,
        (
            "スロットの強化は請け負ってるから、\x01",
            "必要があったら声を掛けてね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15BD")

    label("loc_155D")


    #C0041
    ChrTalk(
        0x9,
        (
            "うちでもスロットの強化と\x01",
            "上位クオーツの取り扱いを始めたから、\x01",
            "必要があったら声を掛けてね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15BD")

    OP_5A()
    Sound(828, 0, 100, 0)
    FadeToDark(300, 0, 100)

    #A0042
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※スロットの強化が行えるようになりました。\x02",
        )
    )

    CloseMessageWindow()

    #A0043
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

    #A0044
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

    label("loc_16D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_16E6")
    OP_AF(0xF)
    Jump("loc_1728")

    label("loc_16E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_16F6")
    OP_AF(0xE)
    Jump("loc_1728")

    label("loc_16F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1706")
    OP_AF(0xD)
    Jump("loc_1728")

    label("loc_1706")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_1716")
    OP_AF(0xC)
    Jump("loc_1728")

    label("loc_1716")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_1726")
    OP_AF(0xB)
    Jump("loc_1728")

    label("loc_1726")

    OP_AF(0xA)

    label("loc_1728")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_21F7")

    label("loc_1737")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1758")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 9)
    Jump("loc_21F7")

    label("loc_1758")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_176C")
    Jump("loc_21F7")

    label("loc_176C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_21F7")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_18DB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1888")

    #C0045
    ChrTalk(
        0x9,
        (
            "ロイド達って今日も捜査なの？\x01",
            "警察官は大変ねえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x9,
        (
            "ね、こっちに戻ってから全然だし……\x01",
            "今度オスカーと３人で遊びましょ。\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x101,
        (
            "#0000Fああ、そうだな。\x01",
            "時間ができたらだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x9,
        (
            "あは、それはこっちのセリフでも\x01",
            "あるんだけどね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_18D6")

    label("loc_1888")


    #C0049
    ChrTalk(
        0x9,
        (
            "みんな忙しいけど……\x01",
            "ま、時間が出来たら\x01",
            "今度オスカーと３人で遊びましょ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18D6")

    Jump("loc_21F7")

    label("loc_18DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 4)), scpexpr(EXPR_END)), "loc_19DE")

    #C0050
    ChrTalk(
        0x9,
        "迷子の男の子、まだ捜してるの？\x02",
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x9,
        (
            "私にできる事があったら言ってね。\x01",
            "導力車くらいなら\x01",
            "店から発進させるから！\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x101,
        (
            "#0006Fウェンディなら\x01",
            "本当にやりそうで怖いな……\x02\x03",

            "#0000F手がかりも揃ってきたし\x01",
            "こっちは大丈夫だ。\x01",
            "気持ちだけ受け取っておくよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21F7")

    label("loc_19DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_1DA3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAC, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C18")

    #C0053
    ChrTalk(
        0x101,
        (
            "#0001Fウェンディ、ちょっといいかな。\x02\x03",

            "この子を見かけていたら\x01",
            "教えて欲しいんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x9,
        "え？　なになに？\x02",
    )

    CloseMessageWindow()

    #A0055
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

    #C0056
    ChrTalk(
        0x9,
        (
            "ふ～ん、５歳くらいの子かぁ。\x01",
            "ウチのパンセよりちょっと年下ね。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x9,
        (
            "でもゴメン、私パレードは\x01",
            "見なかったから判らないかも。\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x101,
        "#0005F店にも来てないみたいだな？\x02",
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x9,
        (
            "うん、それだけは\x01",
            "はっきり言えるわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x9,
        (
            "私、そこの導力ドアが開く回数を\x01",
            "カウントしてるもの。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x101,
        (
            "#0006Fそ、そうか……\x01",
            "（それは確実そうだな。）\x02\x03",

            "#0000Fサンキュー、助かったよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xAC, 1)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 13)
    Jump("loc_1D9E")

    label("loc_1C18")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D53")

    #C0062
    ChrTalk(
        0x9,
        (
            "表は凄かったらしいし、\x01",
            "あれで迷子になっちゃうと心配ね。\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x9,
        (
            "ツァイト……だっけ。\x01",
            "あの例の警察犬を使ってみたら？\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x101,
        (
            "#0000Fああ、そっちは\x01",
            "ティオに頼んでいる所だ。\x02\x03",

            "#0008Fただ人ごみが凄いから\x01",
            "時間は掛かるだろうな……\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x9,
        (
            "粘り強く聞き込みを\x01",
            "してくしかなさそうね。\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x9,
        "……頑張って、ロイド！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1D9E")

    label("loc_1D53")


    #C0067
    ChrTalk(
        0x9,
        (
            "やっぱり最後は\x01",
            "地道な聞き込みってことね。\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x9,
        "……頑張って、ロイド！\x02",
    )

    CloseMessageWindow()

    label("loc_1D9E")

    Jump("loc_21F7")

    label("loc_1DA3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_1E4F")

    #C0069
    ChrTalk(
        0x9,
        (
            "パレードに使われてた導力車、\x01",
            "どんな部品を使ってるのかなー……\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x9,
        (
            "なんて考えてたら\x01",
            "いつの間にか終わっちゃってたわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x9,
        "あはは、職業病ってやつかしら。\x02",
    )

    CloseMessageWindow()
    Jump("loc_21F7")

    label("loc_1E4F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_1F40")

    #C0072
    ChrTalk(
        0x9,
        (
            "新型のクオーツより\x01",
            "安くなった旧式クオーツが\x01",
            "売れたりするのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0x9,
        (
            "まだまだ普及してない地域も多いし、\x01",
            "旧式の方が構造が単純だものね。\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x9,
        (
            "んま、完全に移行しても\x01",
            "一旦セピスにまで砕いちゃえば\x01",
            "再利用できるのはいいことよね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21F7")

    label("loc_1F40")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_END)), "loc_202D")

    #C0075
    ChrTalk(
        0x9,
        (
            "アルカンシェルの公演、\x01",
            "スキあらば見に行こうと思ったけど……\x01",
            "今年はやっぱり難しいなあ。\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x9,
        (
            "やっぱオーバルストアになってから\x01",
            "お客さんがふえたもんね。\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0x9,
        (
            "ありがたいことだけど、\x01",
            "もっと気楽に導力器を\x01",
            "いじってたいなー。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21F7")

    label("loc_202D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_2177")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_20F1")

    #C0078
    ChrTalk(
        0x9,
        "仕事中に客がナンパしてきてね。\x02",
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0x9,
        (
            "お客さんも多いのに\x01",
            "空気を読まないもんだから、\x01",
            "思わずブン殴りそうになったわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0x101,
        (
            "#0006Fもう大人なんだし\x01",
            "ほどほどにしとけよ……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2172")

    label("loc_20F1")


    #C0081
    ChrTalk(
        0x9,
        (
            "ま、殴りはしなかったけど\x01",
            "客が詰まってたから\x01",
            "早々にお帰りいただいたわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x9,
        (
            "全く、忙しいときくらい\x01",
            "空気を呼んで欲しいわね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2172")

    Jump("loc_21F7")

    label("loc_2177")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_21F7")

    #C0083
    ChrTalk(
        0x9,
        (
            "すっごい人ごみね。\x01",
            "興味本位で見に来てくれる\x01",
            "お客さんの多いこと。\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x9,
        (
            "私も日が落ちたらちょっと\x01",
            "歩いてみよっかな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_21F7")

    Jump("loc_1352")

    label("loc_21FC")

    TalkEnd(0x9)
    Return()

    # Function_8_1345 end

    def Function_9_2200(): pass

    label("Function_9_2200")


    #C0085
    ChrTalk(
        0x9,
        (
            "オッケー。\x01",
            "何について聞きたいの？\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2231")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2A6D")
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
    FadeToBright(300, 0)
    OP_5A()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_END)),
        (0, "loc_22E2"),
        (1, "loc_2505"),
        (2, "loc_2636"),
        (3, "loc_277D"),
        (SWITCH_DEFAULT, "loc_2A59"),
    )


    label("loc_22E2")


    #C0086
    ChrTalk(
        0x9,
        (
            "《戦術オーブメント》っていうのは、\x01",
            "個人の戦闘用に特化した\x01",
            "小型の携帯導力器のことよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x9,
        (
            "使用者の能力を強化してくれるほか\x01",
            "導力魔法#8Rア  ー  ツ#の使用もサポートしてくれるの。\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0x9,
        (
            "一般的には、たんに『オーブメント』って\x01",
            "呼ばれたりするわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0x9,
        (
            "ロイド達が使ってるのは、\x01",
            "その中でも最新型の\x01",
            "『エニグマ』っていうタイプよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x9,
        (
            "オーブメントは個人に合わせて\x01",
            "完璧に調整されてるから、\x01",
            "持ち主によって構造が異なるわよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x9,
        (
            "属性限定のスロットがあったり、\x01",
            "スロットを結ぶ線#2Rライン#の形が違ったりするわ。\x01",
            "一度みんなで見比べてみるといいかもね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A68")

    label("loc_2505")


    #C0092
    ChrTalk(
        0x9,
        (
            "クオーツは、セピスを精錬して作られる\x01",
            "オーブメント用の『結晶回路』のことね。\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x9,
        (
            "必要なセピスさえ持ってきてくれれば\x01",
            "ウチで合成ができるわよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x9,
        (
            "クオーツによって色々な効果があるし、\x01",
            "属性値が一定以上になると\x01",
            "導力魔法#8Rア  ー  ツ#が使えるようになるの。\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0x9,
        "セピスが溜まったら色々試してみてね。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2A68")

    label("loc_2636")


    #C0096
    ChrTalk(
        0x9,
        (
            "オーブメントのスロットは\x01",
            "初めはほとんどが未開封の状態なの。\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0x9,
        (
            "クオーツをセットするには\x01",
            "まずはスロットを開封する必要があるわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x9,
        (
            "スロットを開封すれば、\x01",
            "クオーツも沢山セットできるようになるし\x01",
            "最大ＥＰの値も上昇するわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0x9,
        (
            "開封にはセピスが必要だけど\x01",
            "かなり便利になるはずよ。\x01",
            "積極的に開けていくといいと思うわ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A68")

    label("loc_277D")


    #C0100
    ChrTalk(
        0x9,
        (
            "戦術オーブメントを使って発動する魔法が\x01",
            "いわゆる導力魔法#8Rオーバルアーツ#ね。\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0x9,
        "単純に『アーツ』って呼ばれる事が多いわ。\x02",
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x9,
        (
            "オーブメントに内蔵されている機構と\x01",
            "クオーツが使用者と共鳴連鎖することで\x01",
            "魔法現象を展開するんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0x9,
        "ま、細かいことはいいかな。\x02",
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0x9,
        (
            "アーツは、セットしたクオーツの\x01",
            "『ラインごとの属性値の合計』によって\x01",
            "発動できる種類が決まってくるの。\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0x9,
        (
            "ちょっと難しいけど……\x01",
            "そうね、例えば。\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0x9,
        (
            "ラインが繋がっているスロットに\x01",
            "クオーツをセットしていって、\x01",
            "地属性の合計値が２以上になると……\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0x9,
        (
            "『クエイク』ってアーツが\x01",
            "使えるようになるわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0x9,
        (
            "クオーツをセットするほど、\x01",
            "たくさんのアーツが\x01",
            "使えるようになるってわけね。\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0x9,
        (
            "他のアーツの組み合わせは\x01",
            "アーツリストに載ってるはずよ。\x01",
            "参考にしてね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A68")

    label("loc_2A59")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2A68")

    label("loc_2A68")

    Jump("loc_2231")

    label("loc_2A6D")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_9_2200 end

    def Function_10_2A78(): pass

    label("Function_10_2A78")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_2B1A")

    #C0110
    ChrTalk(
        0xFE,
        (
            "先程、帝国の観光客に\x01",
            "導力車を購入して頂きました。\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0xFE,
        (
            "パレードでの優雅な走りを見て\x01",
            "欲しくなったのだとか。\x01",
            "いや、パレードさまさまですねぇ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E72")

    label("loc_2B1A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_2BC0")

    #C0112
    ChrTalk(
        0xFE,
        (
            "……よく考えると、\x01",
            "私は無意識にウェンディの知識を\x01",
            "頼っていた気がします。\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0xFE,
        (
            "私も導力器の勉強を\x01",
            "しっかりはじめた方が\x01",
            "いいのかもしれませんねぇ……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E72")

    label("loc_2BC0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_2C94")

    #C0114
    ChrTalk(
        0xFE,
        (
            "感光クオーツが壊れたので\x01",
            "ウェンディのもとに修理に来るという\x01",
            "観光客を何度か見かけるのです。\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0xFE,
        (
            "ううむ……買い替えさせたほうが\x01",
            "利益になると思いましたが\x01",
            "あの方法ならリピーターがつきますねぇ……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E72")

    label("loc_2C94")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_END)), "loc_2CDB")

    #C0116
    ChrTalk(
        0xFE,
        (
            "ううむ、もっと外の観光客を\x01",
            "呼び込む手段があれば……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E72")

    label("loc_2CDB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_2DBE")

    #C0117
    ChrTalk(
        0xFE,
        (
            "ウェンディめ……\x01",
            "よりにもよってお客様に\x01",
            "手を上げようとするとは。\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0xFE,
        (
            "聞けば、前の工房の時も\x01",
            "何度か同じようなことがあった\x01",
            "そうではないですか。\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0xFE,
        (
            "まったく、師匠とやらは彼女に\x01",
            "どんな教育をしていたのやら……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E72")

    label("loc_2DBE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_2E72")

    #C0120
    ChrTalk(
        0xFE,
        (
            "オーバルカメラはぽつぽつと\x01",
            "売れているようなのですが、\x01",
            "全体的な売り上げはまだまだですねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0xFE,
        (
            "外の出店に客をとられているのか……\x01",
            "もっと賑やかに打ち出すべきでした。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E72")

    TalkEnd(0xFE)
    Return()

    # Function_10_2A78 end

    def Function_11_2E76(): pass

    label("Function_11_2E76")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_2F2E")

    #C0122
    ChrTalk(
        0xFE,
        "今日は最終日かぁ……\x02",
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0xFE,
        (
            "今年はあまり外を回らずに\x01",
            "ここにばっかり来てたわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0xFE,
        (
            "まあおばさんにとっては\x01",
            "ここで商品を眺めるのが\x01",
            "一番刺激的で楽しいって事かしら。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3212")

    label("loc_2F2E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_2FAA")

    #C0125
    ChrTalk(
        0xFE,
        (
            "パレードの様子、\x01",
            "ばっちりカメラに収めたわよ～。\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0xFE,
        (
            "さすがは新製品のカメラね、\x01",
            "使いやすくって最高よ～！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3212")

    label("loc_2FAA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_3042")

    #C0127
    ChrTalk(
        0xFE,
        (
            "そういえば２階のコーナーは\x01",
            "あまり覗いたことないのよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0xFE,
        (
            "最先端の製品が展示されているそうだし……\x01",
            "一度じっくり見てみようかしら。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3212")

    label("loc_3042")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_END)), "loc_30DE")

    #C0129
    ChrTalk(
        0xFE,
        "パシャッ、パシャッ……！\x02",
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0xFE,
        (
            "せっかく来たのだし、賑わう\x01",
            "店内の写真をとっておきましょ。\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0xFE,
        (
            "オシャレな新製品も写せるし\x01",
            "一石二鳥よね～。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3212")

    label("loc_30DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_316A")

    #C0132
    ChrTalk(
        0xFE,
        (
            "おばさん、\x01",
            "人ごみってダメなのよ～……\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0xFE,
        (
            "その点、この店は\x01",
            "空調も効いてるから快適よぉ。\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0xFE,
        "思わず入り浸っちゃうわ～。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3212")

    label("loc_316A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_3212")

    #C0135
    ChrTalk(
        0xFE,
        (
            "オーバルカメラが安くなっていたから\x01",
            "思い切って買ってしまったわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0xFE,
        (
            "うふふ、夢だったのよね～\x01",
            "カメラを扱うの。\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0xFE,
        (
            "これで記念祭も\x01",
            "バッチリ楽しむわよ～！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3212")

    TalkEnd(0xFE)
    Return()

    # Function_11_2E76 end

    def Function_12_3216(): pass

    label("Function_12_3216")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_32A6")

    #C0138
    ChrTalk(
        0xFE,
        (
            "チャコ……\x01",
            "記念祭に休みもとらずに\x01",
            "よくがんばっていたなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0xFE,
        (
            "よし、今度お父さんが\x01",
            "ミシュラムにでも連れてってあげよう。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3605")

    label("loc_32A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_333A")

    #C0140
    ChrTalk(
        0xFE,
        (
            "パレードが来たとき、チャコが\x01",
            "急いで店外に飛び出ていったんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0xFE,
        (
            "め……目が合ってしまった気がしたけど\x01",
            "気づかれなかったかな……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3605")

    label("loc_333A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_33D7")

    #C0142
    ChrTalk(
        0xFE,
        (
            "ううん、迷っている間に\x01",
            "パレードの時間が近づいてしまったな。\x02",
        )
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0xFE,
        (
            "練習もしないで\x01",
            "いい写真を撮るのは難しいと聞く。\x01",
            "今回の購入は見送るか……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3605")

    label("loc_33D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_END)), "loc_347C")

    #C0144
    ChrTalk(
        0xFE,
        (
            "うーん、さっきから見ていたが、\x01",
            "チャコの先輩はなかなか面倒見が\x01",
            "よさそうな娘さんじゃないか。\x02",
        )
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0xFE,
        (
            "あれならチャコのことを\x01",
            "安心して任せられそうだな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3605")

    label("loc_347C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_359A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3554")

    #C0146
    ChrTalk(
        0xFE,
        "さ、さっきはビックリしたな……\x02",
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0xFE,
        (
            "チャコの隣のカウンターの娘が\x01",
            "しつこそうな観光客を\x01",
            "スパナで殴ろうとしたんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0xFE,
        (
            "あ、あんな凶暴そうな先輩の下で\x01",
            "チャコは大丈夫なんだろうか……？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_3595")

    label("loc_3554")


    #C0149
    ChrTalk(
        0xFE,
        (
            "あんな凶暴そうな先輩の下で\x01",
            "チャコは大丈夫なんだろうか……？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3595")

    Jump("loc_3605")

    label("loc_359A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_3605")

    #C0150
    ChrTalk(
        0xFE,
        (
            "ふむふむ……\x01",
            "結局どのカメラにしようかな。\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0xFE,
        (
            "どうせなら長く使えるものが\x01",
            "望ましいんだが……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3605")

    TalkEnd(0xFE)
    Return()

    # Function_12_3216 end

    def Function_13_3609(): pass

    label("Function_13_3609")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_36B1")

    #C0152
    ChrTalk(
        0x160,
        (
            "#3300F（中央広場の聞き込みは\x01",
            "  こんな所かしら？）\x02",
        )
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0x101,
        (
            "#0000F（ああ、十分だと思う。）\x02\x03",

            "（次は駅前通りで\x01",
            "  聞き込みをしてみよう。）\x02",
        )
    )

    CloseMessageWindow()
    OP_D0(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0xB9, 5)
    OP_29(0x46, 0x1, 0x7)

    label("loc_36B1")

    Return()

    # Function_13_3609 end

    def Function_14_36B2(): pass

    label("Function_14_36B2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_37A6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_36FB")

    #C0154
    ChrTalk(
        0xFE,
        (
            "俺、昔から導力製品と\x01",
            "相性悪いんだよな……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_37A1")

    label("loc_36FB")


    #C0155
    ChrTalk(
        0xFE,
        (
            "昨日買った導力腕時計が\x01",
            "嵌めたとたんに壊れちまったんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0xFE,
        (
            "……今、修理カウンターで\x01",
            "直してもらってるんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0xFE,
        (
            "トホホ、俺ってやっぱ\x01",
            "導力オンチなのかな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)

    label("loc_37A1")

    Jump("loc_3AAC")

    label("loc_37A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_38F9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_383A")

    #C0158
    ChrTalk(
        0xFE,
        (
            "店員のねーちゃん、\x01",
            "『愛でて行くといいですよ』とか\x01",
            "良く分からん事を言うんだよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0xFE,
        (
            "ハキハキしてて\x01",
            "俺の好みなのに……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_38F4")

    label("loc_383A")


    #C0160
    ChrTalk(
        0xFE,
        (
            "さっき店員のねーちゃんが\x01",
            "導力製品の解説をしてくれたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0xFE,
        (
            "……でもあのねーちゃん、\x01",
            "『愛でて行くといいですよ』とか\x01",
            "良く分からん事を言うんだよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0xFE,
        "……可愛いのにな………\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)

    label("loc_38F4")

    Jump("loc_3AAC")

    label("loc_38F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_3985")

    #C0163
    ChrTalk(
        0xFE,
        (
            "うーむ、これは……\x01",
            "明るい導力灯って書いてあるな。\x02",
        )
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0xFE,
        (
            "しかも豊富なカラーバリエーション！？\x01",
            "土産に１つ買って帰りたいぜ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3AAC")

    label("loc_3985")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_END)), "loc_39EA")

    #C0165
    ChrTalk(
        0xFE,
        (
            "こ、こいつは最新型の\x01",
            "戦術オーブメントらしいぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0xFE,
        "さ、触ったら壊れねえかな！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_3AAC")

    label("loc_39EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_3A43")

    #C0167
    ChrTalk(
        0xFE,
        (
            "あれ……？\x01",
            "下の方が騒がしかったみたいだけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0xFE,
        "何かあったのかな。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3AAC")

    label("loc_3A43")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_3AAC")

    #C0169
    ChrTalk(
        0xFE,
        (
            "スッゲーっ……！\x01",
            "なんじゃこりゃー！\x02",
        )
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0xFE,
        (
            "導力オンチの俺には\x01",
            "さっぱり分かんねー物ばっかだ！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3AAC")

    TalkEnd(0xFE)
    Return()

    # Function_14_36B2 end

    def Function_15_3AB0(): pass

    label("Function_15_3AB0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_3B4A")

    #C0171
    ChrTalk(
        0xFE,
        (
            "クロスベルに来た記念に\x01",
            "導力ライト付きペンダントっていうのを\x01",
            "買うことにしたわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0xFE,
        (
            "たくさん珍しい物があるけど\x01",
            "どれも高いんだもん。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3D8D")

    label("loc_3B4A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_3BD2")

    #C0173
    ChrTalk(
        0xFE,
        (
            "夢中でこのお店を見てたら\x01",
            "パレードを見逃しちゃったのよっ！\x02",
        )
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0xFE,
        (
            "……仕方ないわ……\x01",
            "代わりに導力車を拝んでいきましょ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3D8D")

    label("loc_3BD2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_3C69")

    #C0175
    ChrTalk(
        0xFE,
        (
            "『保温力バツグン！\x01",
            "  最新の高出力結晶回路搭載！』\x02",
        )
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0xFE,
        (
            "……ど、どれがいいのかしら。\x01",
            "仕様書って、難しくて\x01",
            "読んでも分かんないよのね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3D8D")

    label("loc_3C69")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_END)), "loc_3CCE")

    #C0177
    ChrTalk(
        0xFE,
        "強力冷凍装置つき……\x02",
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0xFE,
        (
            "うむむ……買って帰りたいけど\x01",
            "とても持ち運べないわね……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3D8D")

    label("loc_3CCE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_3D33")

    #C0179
    ChrTalk(
        0xFE,
        "自動首フリ機能……？\x02",
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0xFE,
        (
            "ううっ、さすがはクロスベル。\x01",
            "何でも最新型ばっかなのね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3D8D")

    label("loc_3D33")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_3D8D")

    #C0181
    ChrTalk(
        0xFE,
        "ここが噂のオーバルストアね！\x02",
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0xFE,
        (
            "よぉし、お祭りのついでに\x01",
            "見て回るわよっ！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3D8D")

    TalkEnd(0xFE)
    Return()

    # Function_15_3AB0 end

    SaveToFile()

Try(main)
