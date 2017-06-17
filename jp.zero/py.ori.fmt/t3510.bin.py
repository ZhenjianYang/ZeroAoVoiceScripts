from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t3510.bin",                # FileName
        "t3510",                    # MapName
        "t3510",                    # Location
        0x005C,                     # MapIndex
        "ed7100",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\x03',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 92, 0, 4, 0, 5],
    )

    BuildStringList((
        "t3510",                  # 0
        "受付嬢マルカナ",         # 1
        "受付トーマス",           # 2
        "リカルド",               # 3
        "運送員レグ",             # 4
        "運送員ロッシ",           # 5
        "アリオス",               # 6
        "乗客",                   # 7
        "乗客",                   # 8
        "男の子",                 # 9
        "乗客",                   # 10
        "乗客",                   # 11
        "男の子",                 # 12
        "ドノバン警部",           # 13
        "レイモンド捜査官",       # 14
        "エマ捜査官",             # 15
        "アントン",               # 16
        "リックス",               # 17
        "受付ミシェル",           # 18
        "シズク",                 # 19
        "レン",                   # 20
        "アリオス",               # 21
        "遊撃士スコット",         # 22
        "遊撃士ヴェンツェル",     # 23
        "遊撃士リン",             # 24
        "遊撃士エオリア",         # 25
        "ツァイト",               # 26
        "キーア",                 # 27
        "カード",                 # 28
        "マーシャ",               # 29
    ))

    AddCharChip((
        "chr/ch28200.itc",                   # 00
        "chr/ch28100.itc",                   # 01
        "chr/ch26000.itc",                   # 02
        "chr/ch10500.itc",                   # 03
        "chr/ch22100.itc",                   # 04
        "chr/ch24200.itc",                   # 05
        "chr/ch23800.itc",                   # 06
        "chr/ch20000.itc",                   # 07
        "chr/ch23500.itc",                   # 08
        "chr/ch30300.itc",                   # 09
        "chr/ch30200.itc",                   # 0A
        "chr/ch30500.itc",                   # 0B
        "chr/ch02402.itc",                   # 0C
        "chr/ch37300.itc",                   # 0D
        "chr/ch37400.itc",                   # 0E
    ))

    DeclNpc(-10220,  150,     2849,    90,   261,  0x0, 0,   0,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(-8350,   150,     6730,    135,  261,  0x0, 0,   1,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(6679,    0,       5530,    180,  261,  0x0, 0,   2,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(6630,    0,       -3460,   180,  389,  0x0, 0,   3,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(6110,    0,       -4760,   45,   389,  0x0, 0,   3,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(-4750,   5179,    12399,   75,   469,  0x0, 0,   12,  0,   255, 255, 0,   22,  255,  0)
    DeclNpc(6500,    0,       -10180,  345,  389,  0x0, 0,   4,   0,   0,   0,   0,   13,  255,  0)
    DeclNpc(-10500,  5000,    7010,    270,  389,  0x0, 0,   5,   0,   0,   0,   0,   14,  255,  0)
    DeclNpc(-10970,  5000,    6079,    270,  389,  0x0, 0,   6,   0,   0,   0,   0,   15,  255,  0)
    DeclNpc(-1120,   5000,    13970,   0,    389,  0x0, 0,   7,   0,   0,   0,   0,   16,  255,  0)
    DeclNpc(-2160,   0,       -2170,   165,  389,  0x0, 0,   8,   0,   0,   0,   0,   17,  255,  0)
    DeclNpc(29,      0,       -8789,   135,  389,  0x0, 0,   6,   0,   0,   2,   0,   18,  255,  0)
    DeclNpc(8850,    0,       -7480,   225,  389,  0x0, 0,   9,   0,   0,   0,   0,   19,  255,  0)
    DeclNpc(7630,    0,       -8699,   45,   389,  0x0, 0,   10,  0,   0,   0,   0,   20,  255,  0)
    DeclNpc(-7539,   5000,    11000,   315,  405,  0x0, 0,   11,  0,   0,   0,   0,   21,  255,  0)
    DeclNpc(8329,    0,       -319,    45,   385,  0x0, 0,   13,  0,   0,   0,   0,   23,  255,  0)
    DeclNpc(6500,    0,       -330,    45,   385,  0x0, 0,   14,  0,   0,   0,   0,   24,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 37,  0.25999999046325684,   7.989999771118164,     0.0,                   36.0,                  [0.1666666716337204,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.3333333432674408,    0.0,                   -0.04333333298563957,  -3.994999885559082,    -0.0,                  1.0])

    DeclActor(-8690,   0,       2530,    1000,    -10220,  1600,    2850,    0x007E, 0,  6,  0x0000)
    DeclActor(-7210,   0,       5680,    1000,    -8350,   1600,    6730,    0x007E, 0,  8,  0x0000)
    DeclActor(-7590,   0,       -2440,   1200,    -7590,   1500,    -2440,   0x007C, 0,  38, 0x0000)

    ScpFunction((
        "Function_0_564",          # 00, 0
        "Function_1_61C",          # 01, 1
        "Function_2_647",          # 02, 2
        "Function_3_672",          # 03, 3
        "Function_4_673",          # 04, 4
        "Function_5_73E",          # 05, 5
        "Function_6_7F0",          # 06, 6
        "Function_7_7F4",          # 07, 7
        "Function_8_C7E",          # 08, 8
        "Function_9_C82",          # 09, 9
        "Function_10_1097",        # 0A, 10
        "Function_11_15D0",        # 0B, 11
        "Function_12_16A4",        # 0C, 12
        "Function_13_1788",        # 0D, 13
        "Function_14_1814",        # 0E, 14
        "Function_15_1881",        # 0F, 15
        "Function_16_18BD",        # 10, 16
        "Function_17_1933",        # 11, 17
        "Function_18_198D",        # 12, 18
        "Function_19_19C9",        # 13, 19
        "Function_20_1B15",        # 14, 20
        "Function_21_1B4B",        # 15, 21
        "Function_22_1BDC",        # 16, 22
        "Function_23_1D7D",        # 17, 23
        "Function_24_253A",        # 18, 24
        "Function_25_25CC",        # 19, 25
        "Function_26_2C30",        # 1A, 26
        "Function_27_2EFA",        # 1B, 27
        "Function_28_31C2",        # 1C, 28
        "Function_29_3502",        # 1D, 29
        "Function_30_373F",        # 1E, 30
        "Function_31_3ECA",        # 1F, 31
        "Function_32_3F07",        # 20, 32
        "Function_33_49C5",        # 21, 33
        "Function_34_49DA",        # 22, 34
        "Function_35_49EF",        # 23, 35
        "Function_36_4A18",        # 24, 36
        "Function_37_4A41",        # 25, 37
        "Function_38_4AD4",        # 26, 38
    ))


    def Function_0_564(): pass

    label("Function_0_564")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_5A4"),
        (1, "loc_5B0"),
        (2, "loc_5BC"),
        (3, "loc_5C8"),
        (4, "loc_5D4"),
        (5, "loc_5E0"),
        (6, "loc_5EC"),
        (SWITCH_DEFAULT, "loc_5F8"),
    )


    label("loc_5A4")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_604")

    label("loc_5B0")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_604")

    label("loc_5BC")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_604")

    label("loc_5C8")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_604")

    label("loc_5D4")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_604")

    label("loc_5E0")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_604")

    label("loc_5EC")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_604")

    label("loc_5F8")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_604")

    label("loc_604")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_61B")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_604")

    label("loc_61B")

    Return()

    # Function_0_564 end

    def Function_1_61C(): pass

    label("Function_1_61C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_646")
    OP_94(0xFE, 0xFFFFF704, 0xFFFFF876, 0xDB6, 0xFFFFE1C4, 0x3E8)
    Sleep(300)
    Jump("Function_1_61C")

    label("loc_646")

    Return()

    # Function_1_61C end

    def Function_2_647(): pass

    label("Function_2_647")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_671")
    OP_94(0xFE, 0x406, 0xFFFFE192, 0xFFFFFBFA, 0xFFFFD9C2, 0x3E8)
    Sleep(100)
    Jump("Function_2_647")

    label("loc_671")

    Return()

    # Function_2_647 end

    def Function_3_672(): pass

    label("Function_3_672")

    Return()

    # Function_3_672 end

    def Function_4_673(): pass

    label("Function_4_673")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_682")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 25)

    label("loc_682")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_69F")
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    Jump("loc_707")

    label("loc_69F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_6CB")
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x12, 0x10)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    Jump("loc_707")

    label("loc_6CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_707")
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xB, 0x10)
    SetChrFlags(0xC, 0x10)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0xF, 0x10)
    BeginChrThread(0x13, 0, 0, 2)

    label("loc_707")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_73D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_71F")
    Jump("loc_73D")

    label("loc_71F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_735")
    SetMapFlags(0x10000000)
    Event(0, 29)
    Jump("loc_73D")

    label("loc_735")

    SetMapFlags(0x10000000)
    Event(0, 28)

    label("loc_73D")

    Return()

    # Function_4_673 end

    def Function_5_73E(): pass

    label("Function_5_73E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 1)), scpexpr(EXPR_END)), "loc_750")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0xCB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_750")

    SetMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x1, 0x4)
    SetMapObjFlags(0x2, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_782")
    OP_63(0x16, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_7AB")

    label("loc_782")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_79C")
    ClearMapObjFlags(0x1, 0x4)
    ClearMapObjFlags(0x2, 0x4)
    Jump("loc_7AB")

    label("loc_79C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_7AB")
    ClearMapObjFlags(0x0, 0x4)

    label("loc_7AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_7C2")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    Jump("loc_7C2")

    label("loc_7C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE6, 4)), scpexpr(EXPR_END)), "loc_7D3")
    OP_24(0x86)
    Jump("loc_7EF")

    label("loc_7D3")

    SoundDistance(0x86, 0x16D0, 0x0, 0x259E, 0x1388, 0x30D40, 0x64, 0x0)

    label("loc_7EF")

    Return()

    # Function_5_73E end

    def Function_6_7F0(): pass

    label("Function_6_7F0")

    Call(0, 7)
    Return()

    # Function_6_7F0 end

    def Function_7_7F4(): pass

    label("Function_7_7F4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x1, 0x8)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x1, 0x9)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_816")
    Call(0, 32)
    Return()

    label("loc_816")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_97A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8FA")

    #C0001
    ChrTalk(
        0x8,
        (
            "警察の方に空港内を\x01",
            "くまなく捜索していただきました。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x8,
        (
            "どうやら嘘の爆破予告だったらしいと\x01",
            "捜査官の方は仰っていましたが……\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0x8,
        (
            "……ともかく。\x01",
            "早急に飛行船の運行を\x01",
            "再開しないといけませんね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_975")

    label("loc_8FA")


    #C0004
    ChrTalk(
        0x8,
        (
            "嘘の爆破予告を送る意図は\x01",
            "私には分かりませんが……\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x8,
        (
            "今はとにかく、\x01",
            "早急に飛行船の運行を\x01",
            "再開しないといけませんね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_975")

    Jump("loc_C7A")

    label("loc_97A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_A88")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_A0C")

    #C0006
    ChrTalk(
        0x8,
        (
            "まもなくリベール方面行き定期便\x01",
            "『カラブリア号』が出航いたします。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x8,
        (
            "ご利用のお客様は\x01",
            "搭乗をお急ぎくださいませ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A83")

    label("loc_A0C")


    #C0008
    ChrTalk(
        0x8,
        (
            "よく判りませんけど……\x01",
            "カーラ様は当空港をご利用では\x01",
            "なかったようですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x8,
        (
            "またのご利用を\x01",
            "お待ちしております。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A83")

    Jump("loc_C7A")

    label("loc_A88")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_C7A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BB6")

    #C0010
    ChrTalk(
        0x8,
        (
            "ここから出る飛行船は、\x01",
            "主に北方のレミフェリア公国方面、\x01",
            "南方のリベール王国方面に経路をとります。\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x8,
        (
            "エレボニア帝国やカルバード共和国に\x01",
            "向かう飛行船もありますが、\x01",
            "他の便に比べると利用者数は少ないです。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x8,
        (
            "庶民にとってはまだまだ鉄道の方が\x01",
            "主流だということでしょうね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_C7A")

    label("loc_BB6")


    #C0013
    ChrTalk(
        0x8,
        (
            "ここから出る飛行船は、\x01",
            "主に北方のレミフェリア公国方面、\x01",
            "南方のリベール王国方面に経路をとります。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x8,
        (
            "帝国や共和国にも便はあるのですが、\x01",
            "そちらはまだまだ鉄道の方が\x01",
            "主流になっているんですよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C7A")

    TalkEnd(0x8)
    Return()

    # Function_7_7F4 end

    def Function_8_C7E(): pass

    label("Function_8_C7E")

    Call(0, 9)
    Return()

    # Function_8_C7E end

    def Function_9_C82(): pass

    label("Function_9_C82")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_E03")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D86")

    #C0015
    ChrTalk(
        0x9,
        (
            "爆破予告を出されたと聞いたときは\x01",
            "背筋が凍りましたよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x9,
        (
            "最悪の事態には至りませんでしたが、\x01",
            "本日の運行スケジュールは\x01",
            "完全に凍結してしまいましたし……\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x9,
        (
            "多くのお客様に迷惑をかけてしまい、\x01",
            "大変心苦しい思いをしております。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_DFE")

    label("loc_D86")


    #C0018
    ChrTalk(
        0x9,
        (
            "運行スケジュールの凍結で、\x01",
            "多くのお客様のご予定を\x01",
            "大幅に遅らせてしまいました。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x9,
        "犯人には怒りを禁じえませんよ。\x02",
    )

    CloseMessageWindow()

    label("loc_DFE")

    Jump("loc_1093")

    label("loc_E03")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_F14")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EA1")

    #C0020
    ChrTalk(
        0x9,
        (
            "こちらは出入国届け及び\x01",
            "手荷物預かり窓口です。\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x9,
        (
            "目的地まで責任を持って\x01",
            "運搬させていただきますので、\x01",
            "どうかご安心ください。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_F0F")

    label("loc_EA1")


    #C0022
    ChrTalk(
        0x9,
        (
            "飛行船に乗せる荷物も\x01",
            "こちらでお預かりしています。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x9,
        (
            "重い荷物等をお持ちの際は\x01",
            "是非ご利用くださいませ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F0F")

    Jump("loc_1093")

    label("loc_F14")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_1093")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FF3")

    #C0024
    ChrTalk(
        0x9,
        (
            "これだけ観光客の方が多いと、\x01",
            "入国手続きも大変ですよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x9,
        (
            "何もかも投げ出して\x01",
            "記念祭の楽しみを\x01",
            "享受したい気分です。\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x9,
        (
            "……そういうわけにもいきませんよね。\x01",
            "責任を持って仕事に当たらないと。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1093")

    label("loc_FF3")


    #C0027
    ChrTalk(
        0x9,
        (
            "この仕事の忙しさ、\x01",
            "逃げてしまいたくなっても\x01",
            "仕方ありませんよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x9,
        (
            "……いや、それじゃダメですね。\x01",
            "あくまでも責任を持って\x01",
            "仕事に当たらないといけません。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1093")

    TalkEnd(0x9)
    Return()

    # Function_9_C82 end

    def Function_10_1097(): pass

    label("Function_10_1097")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x22, 0x1, 0x3)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x22, 0x1, 0x5)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x22, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_10B9")
    Call(0, 30)
    Return()

    label("loc_10B9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_1141")

    #C0029
    ChrTalk(
        0xFE,
        (
            "いや、驚いたな。\x01",
            "いつの間にそんなカードが……\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0xFE,
        (
            "さっき運送会社の人に\x01",
            "荷物を渡したときは\x01",
            "無かったはずなんだが。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15CC")

    label("loc_1141")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_12AA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_121E")

    #C0031
    ChrTalk(
        0xFE,
        (
            "しかし警察も大変だね。\x01",
            "大事な任務を放ってまで\x01",
            "こっちの捜査に来たらしいんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0xFE,
        (
            "……彼らにとっては\x01",
            "骨折り損ってことになるのかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0xFE,
        (
            "まぁ、安全が分かっただけでも\x01",
            "良しとしなきゃだよね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_12A5")

    label("loc_121E")


    #C0034
    ChrTalk(
        0xFE,
        (
            "僕も警察と一緒に\x01",
            "空港のあちこちを探して回ってね、\x01",
            "もうクタクタだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0xFE,
        (
            "……まぁ、安全が分かっただけでも\x01",
            "良しとしなきゃだよね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12A5")

    Jump("loc_15CC")

    label("loc_12AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_1406")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1393")

    #C0036
    ChrTalk(
        0xFE,
        (
            "富裕層の乗客なんかは\x01",
            "ペットを旅行に連れてきたりするんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0xFE,
        (
            "専用のケージにいれて\x01",
            "荷物扱いで運んでくるんだけど……\x01",
            "着いたとたん吠えるわ鳴くわでねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0xFE,
        (
            "別に悪かないけど、\x01",
            "個人的には遠慮したいね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1401")

    label("loc_1393")


    #C0039
    ChrTalk(
        0xFE,
        (
            "ペットにも、飼い主にも\x01",
            "まったく罪はないんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0xFE,
        (
            "ペットのお預かりなんて\x01",
            "個人的には遠慮したいね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1401")

    Jump("loc_15CC")

    label("loc_1406")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_15CC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14EF")

    #C0041
    ChrTalk(
        0xFE,
        (
            "今、新進気鋭の運送会社\x01",
            "『カプア特急便』が来てるよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0xFE,
        (
            "元々やくざな商売をしてたそうだけど、\x01",
            "少し前に運送会社に鞍替えしたらしい。\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0xFE,
        (
            "社長の顔が怖いし\x01",
            "ぶっきらぼうだけど、\x01",
            "気の良い人たちばかりだよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_15CC")

    label("loc_14EF")


    #C0044
    ChrTalk(
        0xFE,
        (
            "ところで、彼らが使っている\x01",
            "飛行船《山猫号》は\x01",
            "なかなか大した性能らしいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0xFE,
        (
            "彼らによると、あの有名な\x01",
            "高速巡洋船《アルセイユ》にも\x01",
            "劣らない速度が出るらしいけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0xFE,
        (
            "ま、いくらなんでも\x01",
            "それは信じてないけどね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15CC")

    TalkEnd(0xFE)
    Return()

    # Function_10_1097 end

    def Function_11_15D0(): pass

    label("Function_11_15D0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1657")

    #C0047
    ChrTalk(
        0xFE,
        "ほいっ、こいつは頼むぜ！\x02",
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0xFE,
        (
            "空港の外にライムス運送っていう\x01",
            "地元の同業者がいるから、\x01",
            "そっちに渡してこいな！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_16A0")

    label("loc_1657")


    #C0049
    ChrTalk(
        0xFE,
        "ほれっ、急げっての！\x02",
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0xFE,
        (
            "早くしないとお嬢たちに\x01",
            "どやされちまうぜ！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16A0")

    TalkEnd(0xFE)
    Return()

    # Function_11_15D0 end

    def Function_12_16A4(): pass

    label("Function_12_16A4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1716")

    #C0051
    ChrTalk(
        0xFE,
        "へいへい、わーったよ。\x02",
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0xFE,
        (
            "ったく、手間の掛かる仕事は\x01",
            "いつも俺に押し付けやがってよぉ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_1784")

    label("loc_1716")


    #C0053
    ChrTalk(
        0xFE,
        (
            "そういや、クロスベルには\x01",
            "あいつらも来てるんだっけな。\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0xFE,
        (
            "お嬢、仕事が忙しくなきゃ\x01",
            "会いてえだろうなぁ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1784")

    TalkEnd(0xFE)
    Return()

    # Function_12_16A4 end

    def Function_13_1788(): pass

    label("Function_13_1788")

    TalkBegin(0xFE)

    #C0055
    ChrTalk(
        0xFE,
        (
            "あのひとたち、\x01",
            "運送会社の社員らしいけど……\x01",
            "あんまりそれっぽくないわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0xFE,
        (
            "……ま、いっか。\x01",
            "なんだかワイルドでかっこいいし。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_13_1788 end

    def Function_14_1814(): pass

    label("Function_14_1814")

    TalkBegin(0xFE)

    #C0057
    ChrTalk(
        0xFE,
        (
            "ハハ、遠くのほう見てみろ。\x01",
            "そろそろ飛行船が飛び立つぞ～。\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x10,
        (
            "ワ～、すごいすごい！\x01",
            "かっこいー！\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_14_1814 end

    def Function_15_1881(): pass

    label("Function_15_1881")

    TalkBegin(0xFE)

    #C0059
    ChrTalk(
        0xFE,
        (
            "今から飛行船に乗るんだよ～。\x01",
            "すっごく楽しみ～。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_15_1881 end

    def Function_16_18BD(): pass

    label("Function_16_18BD")

    TalkBegin(0xFE)

    #C0060
    ChrTalk(
        0xFE,
        (
            "空の旅も随分と\x01",
            "快適になったものだよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0xFE,
        (
            "空は女神が住む場所だ。\x01",
            "何らかの加護が\x01",
            "あるのかもしれないな。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_16_18BD end

    def Function_17_1933(): pass

    label("Function_17_1933")

    TalkBegin(0xFE)

    #C0062
    ChrTalk(
        0xFE,
        "これ、早くおし！\x02",
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0xFE,
        (
            "搭乗手続きを済ませないと、\x01",
            "飛行船に乗りそびれちゃうよ！\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_17_1933 end

    def Function_18_198D(): pass

    label("Function_18_198D")

    TalkBegin(0xFE)

    #C0064
    ChrTalk(
        0xFE,
        (
            "ちぇー、もっとクロスベルで\x01",
            "遊んでたかったなー。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_18_198D end

    def Function_19_19C9(): pass

    label("Function_19_19C9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1ABD")

    #C0065
    ChrTalk(
        0xFE,
        "よう、お前らか。\x02",
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0xFE,
        "とりあえず空港には何もナシだ。\x02",
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0xFE,
        (
            "やれやれ、誰の仕業だか知らないが\x01",
            "面倒な事をやらかしてくれたぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x101,
        "#0000F……お疲れ様です。\x02",
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0xFE,
        "おう、マジで疲れたぜ。\x02",
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0xFE,
        "ったくどこの野郎の仕業なんだか。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_1B11")

    label("loc_1ABD")


    #C0071
    ChrTalk(
        0xFE,
        "さて、後は一課に任せて引き上げるか。\x02",
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0xFE,
        "本部に戻って報告書を書かなきゃなぁ。\x02",
    )

    CloseMessageWindow()

    label("loc_1B11")

    TalkEnd(0xFE)
    Return()

    # Function_19_19C9 end

    def Function_20_1B15(): pass

    label("Function_20_1B15")

    TalkBegin(0xFE)

    #C0073
    ChrTalk(
        0xFE,
        (
            "また報告書書きかぁ。\x01",
            "勘弁して欲しいな～。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_20_1B15 end

    def Function_21_1B4B(): pass

    label("Function_21_1B4B")

    TalkBegin(0xFE)
    OP_64(0xFE)

    #C0074
    ChrTalk(
        0xFE,
        "ええ、ええ……\x02",
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0xFE,
        (
            "分かりました、予告状の\x01",
            "送付元はこちらで洗ってみます。\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0xFE,
        "ダドリーさんの方もお気をつけて。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    OP_63(0x16, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Return()

    # Function_21_1B4B end

    def Function_22_1BDC(): pass

    label("Function_22_1BDC")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1C70")
    Jump("loc_1CBA")

    label("loc_1C70")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1C90")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1CBA")

    label("loc_1C90")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1CB0")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1CBA")

    label("loc_1CB0")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1CBA")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_1D75")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB3, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CFA")
    Call(0, 26)
    Jump("loc_1D75")

    label("loc_1CFA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB7, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB4, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1D10")
    Call(0, 27)
    Jump("loc_1D75")

    label("loc_1D10")


    #C0077
    ChrTalk(
        0xFE,
        (
            "#1403F……記念祭の最終日は\x01",
            "思わぬトラブルも起こりやすい。\x02\x03",

            "#1400F最後まで気を抜かないようにな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D75")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_22_1BDC end

    def Function_23_1D7D(): pass

    label("Function_23_1D7D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2A, 0x1, 0x0)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2A, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_217A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_1E1C")

    #C0078
    ChrTalk(
        0xFE,
        (
            "リベールで手酷くフラれ、\x01",
            "クロスベルでは優しくフラれ……\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0xFE,
        (
            "なぁリックス。\x01",
            "僕はこれからどうすれば\x01",
            "いいんだろう……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2175")

    label("loc_1E1C")


    #C0080
    ChrTalk(
        0x101,
        (
            "#0000Fあれ……\x01",
            "アントンさん。\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0xFE,
        (
            "……君たちか。\x01",
            "昨日は待ってたんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x103,
        "#0200F（……すっかり忘れてました。）\x02",
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x101,
        (
            "#0000Fあの……\x01",
            "本当にすみませんでした。\x02\x03",

            "どうしても外せない\x01",
            "調査があって……\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0xFE,
        (
            "……結局昨日は自分で\x01",
            "フランさんに会いに行ったんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0xFE,
        (
            "なんとか食事に誘って\x01",
            "アタックしたけど……\x01",
            "結局ダメだった。\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0xFE,
        (
            "彼女……大好きな人が\x01",
            "いるんだってさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x101,
        (
            "#0000Fそ、そうでしたか……\x01",
            "お気の毒です。\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0x104,
        (
            "#0300F（……フランちゃんの\x01",
            "  大好きな人ってのも\x01",
            "  微妙に気になるな。）\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0xFE,
        (
            "いいよ、気を遣ってくれなくても。\x01",
            "こんなことは慣れっこさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0xFE,
        (
            "大好きな人を語る\x01",
            "彼女の笑顔を見て……\x01",
            "ばっさり断ち切れたよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0xFE,
        (
            "今からリベールに帰って\x01",
            "新しい自分を探すつもりさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0x102,
        (
            "#0100F（うーん……\x01",
            "  やっぱり途中で投げ出したのは\x01",
            "  良くなかったかもしれないわね。）\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x101,
        (
            "#0000F（そうだな……）\x02\x03",

            "（これ以上は何もできないし、\x01",
            "  そっとしておくとしよう。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)

    label("loc_2175")

    Jump("loc_2536")

    label("loc_217A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2A, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2429")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_220D")

    #C0094
    ChrTalk(
        0xFE,
        (
            "リベールで手酷くフラれ、\x01",
            "クロスベルでは優しくフラれ……\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0xFE,
        (
            "なぁリックス。\x01",
            "僕はこれからどうすれば\x01",
            "いいんだろう……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2424")

    label("loc_220D")


    #C0096
    ChrTalk(
        0xFE,
        (
            "……やあ、君たちか。\x01",
            "昨日は色々とありがとう。\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0x101,
        (
            "#0000Fアントンさん……\x01",
            "今から帰国するんですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0xFE,
        (
            "ああ……フランさんにも\x01",
            "振られてしまったことだしね。\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0x103,
        "#0200F……お気の毒でした。\x02",
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0xFE,
        (
            "いいよ、気を遣ってくれなくても。\x01",
            "こんなことは慣れっこさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0xFE,
        (
            "大好きな人を語る\x01",
            "彼女の笑顔を見て……\x01",
            "ばっさり断ち切れたよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x101,
        (
            "#0000F（“大好きな人”が曹長だって\x01",
            "  教えた方がいいのかな……？）\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0x104,
        (
            "#0300F（やめとけ。\x01",
            "  話がこじれて面倒なことに\x01",
            "  なるだけだって。）\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0x102,
        (
            "#0100F（そうね、その方がいいわ。\x01",
            "  少しかわいそうだけど……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)

    label("loc_2424")

    Jump("loc_2536")

    label("loc_2429")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_24B0")

    #C0105
    ChrTalk(
        0xFE,
        (
            "リベールで手酷くフラれ、\x01",
            "クロスベルでは優しくフラれ……\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0xFE,
        (
            "なぁリックス。\x01",
            "僕はこれからどうすれば\x01",
            "いいんだろう……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2536")

    label("loc_24B0")


    #C0107
    ChrTalk(
        0xFE,
        (
            "サイフを探してくれたあの子……\x01",
            "せっかく見つけたけど\x01",
            "結局はフラれてしまった。\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0xFE,
        (
            "もう大好きな人がいたなんて\x01",
            "あんまりだよ……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)

    label("loc_2536")

    TalkEnd(0xFE)
    Return()

    # Function_23_1D7D end

    def Function_24_253A(): pass

    label("Function_24_253A")

    TalkBegin(0xFE)

    #C0109
    ChrTalk(
        0xFE,
        (
            "この失恋で成長するか、\x01",
            "際限なく落ち込んでいくか……\x01",
            "それはアントン次第だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0xFE,
        (
            "俺はただ友達として、\x01",
            "これからも生暖かく見守るだけさ。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_24_253A end

    def Function_25_25CC(): pass

    label("Function_25_25CC")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch09500.itc", 0x1E)
    LoadChrToIndex("chr/ch08700.itc", 0x1F)
    LoadChrToIndex("chr/ch09100.itc", 0x20)
    LoadChrToIndex("chr/ch02400.itc", 0x21)
    LoadChrToIndex("chr/ch08200.itc", 0x22)
    LoadChrToIndex("chr/ch02702.itc", 0x23)
    LoadChrToIndex("chr/ch27200.itc", 0x24)
    LoadChrToIndex("chr/ch27300.itc", 0x25)
    LoadChrToIndex("chr/ch32100.itc", 0x26)
    LoadChrToIndex("chr/ch32000.itc", 0x27)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu03300.itp")
    OP_68(0, 900, 1000, 0)
    MoveCamera(310, 29, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(23000, 0)
    OP_7D(0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x101, 600, 0, -400, 0)
    SetChrPos(0x102, 1900, 0, -600, 0)
    SetChrPos(0x104, 200, 0, -1500, 0)
    SetChrPos(0x103, 1500, 0, -1700, 0)
    SetChrPos(0x107, -800, 0, 2700, 180)
    SetChrPos(0x108, 800, 0, 2700, 180)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrChipByIndex(0x1B, 0x1E)
    SetChrSubChip(0x1B, 0x0)
    ClearChrFlags(0x1B, 0x80)
    ClearChrBattleFlags(0x1B, 0x8000)
    SetChrPos(0x1B, 0, 0, 3000, 180)
    SetChrChipByIndex(0x1A, 0x1F)
    SetChrSubChip(0x1A, 0x0)
    ClearChrFlags(0x1A, 0x80)
    ClearChrBattleFlags(0x1A, 0x8000)
    SetChrPos(0x1A, -2200, 0, -1100, 45)
    SetChrChipByIndex(0x19, 0x20)
    SetChrSubChip(0x19, 0x0)
    ClearChrFlags(0x19, 0x80)
    ClearChrBattleFlags(0x19, 0x8000)
    SetChrPos(0x19, -1100, 0, 300, 45)
    SetChrChipByIndex(0x1C, 0x21)
    SetChrSubChip(0x1C, 0x0)
    ClearChrFlags(0x1C, 0x80)
    ClearChrBattleFlags(0x1C, 0x8000)
    SetChrPos(0x1C, -2300, 0, 0, 45)
    SetChrChipByIndex(0x22, 0x22)
    SetChrSubChip(0x22, 0x0)
    ClearChrFlags(0x22, 0x80)
    ClearChrBattleFlags(0x22, 0x8000)
    SetChrPos(0x22, -200, 0, -400, 0)
    SetChrChipByIndex(0x21, 0x23)
    SetChrSubChip(0x21, 0x0)
    ClearChrFlags(0x21, 0x80)
    ClearChrBattleFlags(0x21, 0x8000)
    SetChrPos(0x21, 2700, 0, 600, 315)
    SetChrChipByIndex(0x1D, 0x24)
    SetChrSubChip(0x1D, 0x0)
    ClearChrFlags(0x1D, 0x80)
    ClearChrBattleFlags(0x1D, 0x8000)
    SetChrPos(0x1D, -300, 0, -2800, 0)
    SetChrChipByIndex(0x1E, 0x25)
    SetChrSubChip(0x1E, 0x0)
    ClearChrFlags(0x1E, 0x80)
    ClearChrBattleFlags(0x1E, 0x8000)
    SetChrPos(0x1E, 1000, 0, -3100, 0)
    SetChrChipByIndex(0x1F, 0x27)
    SetChrSubChip(0x1F, 0x0)
    ClearChrFlags(0x1F, 0x80)
    ClearChrBattleFlags(0x1F, 0x8000)
    SetChrPos(0x1F, -3200, 0, -2200, 45)
    SetChrChipByIndex(0x20, 0x26)
    SetChrSubChip(0x20, 0x0)
    ClearChrFlags(0x20, 0x80)
    ClearChrBattleFlags(0x20, 0x8000)
    SetChrPos(0x20, -2200, 0, -2200, 45)
    SetChrFlags(0x14, 0x80)
    SetChrBattleFlags(0x14, 0x8000)
    SetChrFlags(0x15, 0x80)
    SetChrBattleFlags(0x15, 0x8000)
    SetChrFlags(0x16, 0x80)
    SetChrBattleFlags(0x16, 0x8000)
    OP_C7(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0111
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            "#30W──エステルとヨシュアは\x01",
            "レンと共にリベールに帰る事になった。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    MoveCamera(320, 27, 0, 4000)
    SetCameraDistance(19000, 4000)
    FadeToBright(2000, 0)
    OP_6F(0x79)
    FadeToDark(300, 0, 100)
    OP_0D()

    #A0112
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            "#30W遊撃士協会の人手は減ることになるが、\x01",
            "政治改革が行われることによって\x01",
            "警察の体制もより良く変わるだろう。\x02\x03",

            "今後は一層、ギルドとも協力しつつ\x01",
            "彼らの負担も減らせるかもしれない。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(0, 700, 3000, 0)
    MoveCamera(0, 27, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(17000, 0)
    OP_0D()
    Sleep(500)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_C9(0x0, 0x3, 0xFF9B9B9B, 0x1F4, 0x0)
    FadeToDark(500, 0, 100)
    Sleep(500)
    SetMessageWindowPos(50, -1, -1, -1)

    #A0113
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            "#30W──別れ際、レンは俺たちに\x01",
            "改めて気になる言葉を掛けてきた。\x02\x03",

            "５００年前の真実と\x01",
            "キーアが競売会にいた経緯……\x02\x03",

            "そして俺の兄、ガイ・バニングスを\x01",
            "殺めたのは結局何者だったのか……\x02\x03",

            "全てを見通すような彼女にも\x01",
            "それらの真相は判らなかったという。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    SetCameraDistance(16500, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0114
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            "#30Wだが、それを解き明かすのは、\x01",
            "俺の──いや俺たちの役目であるはずだ。\x02\x03",

            "いつかまた再会する約束をして\x01",
            "俺たちは彼らと別れの言葉を交わした。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C7(0x1, 0x800)
    RemoveParty(0x6, 0x0)
    RemoveParty(0x7, 0x0)
    OP_CA(0x1, 0xFF, 0x0)
    SetScenarioFlags(0x5E, 0)
    NewScene("e3500", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_25_25CC end

    def Function_26_2C30(): pass

    label("Function_26_2C30")

    EventBegin(0x0)
    Fade(500)
    OP_68(-4490, 6400, 11460, 0)
    MoveCamera(315, 20, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(27290, 0)
    SetChrPos(0x101, -4250, 5000, 10550, 0)
    SetChrPos(0x102, -5000, 5000, 10200, 0)
    SetChrPos(0x103, -3100, 5000, 10300, 315)
    SetChrPos(0x104, -4500, 5000, 8900, 0)
    SetChrSubChip(0xD, 0x2)
    OP_0D()

    #C0115
    ChrTalk(
        0xD,
        (
            "#11P#1405Fほう、珍しいな。\x01",
            "こんな場所で会うとは。\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0x102,
        "#6P#0105Fアリオスさん……\x02",
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0x101,
        (
            "#6P#0000Fど、どうも……\x01",
            "昨日はお世話になりました。\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0x104,
        "#6P#0300Fそっちは、また出張ッスか？\x02",
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0xD,
        (
            "#11P#1403Fああ、レミフェリアまでな。\x02\x03",

            "#1405Fお前たちの方は飛行船に\x01",
            "乗るわけでもなさそうだが？\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0x101,
        "#6P#0012Fええ、まあ、ちょっと……\x02",
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0x103,
        (
            "#12P#0206Fタチの悪いナゾナゾに\x01",
            "付き合っている最中です。\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0xD,
        (
            "#11P#1404Fふむ……まあいいだろう。\x02\x03",

            "#1402F記念祭も今日で最後だ。\x01",
            "最後まで気を抜かないようにな。\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0x101,
        (
            "#6P#0012Fは、はい。\x01",
            "（競売会に乗り込むことは\x01",
            "  さすがに話せないな……）\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, -4250, 5000, 10550, 0)
    SetChrSubChip(0xD, 0x0)
    SetScenarioFlags(0xB3, 6)
    EventEnd(0x5)
    Return()

    # Function_26_2C30 end

    def Function_27_2EFA(): pass

    label("Function_27_2EFA")

    EventBegin(0x0)
    Fade(500)
    OP_68(-4490, 6400, 11460, 0)
    MoveCamera(315, 20, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(27290, 0)
    SetChrPos(0x101, -4250, 5000, 10550, 0)
    SetChrPos(0x102, -5000, 5000, 10200, 0)
    SetChrPos(0x103, -3100, 5000, 10300, 315)
    SetChrPos(0x104, -4500, 5000, 8900, 0)
    SetChrSubChip(0xD, 0x2)
    OP_0D()
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x102)
    Sleep(500)

    #C0124
    ChrTalk(
        0x102,
        (
            "#6P#0108Fあの……ところでアリオスさん。\x02\x03",

            "#0101Fシズクちゃんの所には\x01",
            "行ってあげなくていいんですか？\x02\x03",

            "記念祭の間も、あまりお会いに\x01",
            "なっていないみたいですけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0xD,
        (
            "#11P#1403F……耳が痛いな。\x02\x03",

            "#1402F何とか週に一度くらいは\x01",
            "会える時間を取りたいんだが……\x02\x03",

            "#1404F最近は、エステルたちの方が\x01",
            "あの子と会っている時間が\x01",
            "多いくらいなのは確かだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0x102,
        (
            "#6P#0106F……すみません。\x01",
            "差し出がましいことを。\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0xD,
        (
            "#11P#1402F……いや、こちらこそすまない。\x01",
            "気を使わせてしまったな。\x02",
        )
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0x101,
        (
            "#6P#0001F（エリィ……\x01",
            "  ご両親の事を思い出してるのかな。）\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, -4250, 5000, 10550, 0)
    SetChrSubChip(0xD, 0x0)
    SetScenarioFlags(0xB4, 2)
    EventEnd(0x5)
    Return()

    # Function_27_2EFA end

    def Function_28_31C2(): pass

    label("Function_28_31C2")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-21960, 1250, 24660, 0)
    MoveCamera(321, 18, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(42870, 0)
    SetChrPos(0x101, -600, 0, -18300, 0)
    SetChrPos(0x102, 750, 0, -20000, 0)
    SetChrPos(0x103, 750, 0, -18300, 0)
    SetChrPos(0x104, -600, 0, -20000, 0)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)
    SetCameraDistance(49570, 4000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x10)
    Fade(500)
    OP_68(-5130, 1250, 17490, 0)
    MoveCamera(320, 27, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(60830, 0)
    OP_68(830, 1250, -11780, 8000)
    MoveCamera(315, 27, 0, 8000)
    OP_6E(300, 8000)
    SetCameraDistance(51170, 8000)
    PlaceName2(340, 200, "c_plac32", 0x0, 1500)
    Sleep(3800)

    def lambda_32D9():
        OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_32D9)
    Sleep(50)

    def lambda_32F1():
        OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_32F1)
    Sleep(50)

    def lambda_3309():
        OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_3309)
    Sleep(50)

    def lambda_3321():
        OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_3321)
    WaitChrThread(0x3, 1)
    Sleep(300)
    Fade(500)
    OP_68(10, 650, -13380, 0)
    MoveCamera(320, 27, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(32259, 0)
    OP_0D()
    Sleep(500)

    #C0129
    ChrTalk(
        0x101,
        "#6P#0001Fさてと、空港に来てみたけど。\x02",
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0x103,
        (
            "#6P#0203F怪盗Ｂの謎掛け『白ハヤブサ』は\x01",
            "リベール王国の国鳥……\x02\x03",

            "#0202F『白ハヤブサに通ずる玄関口』といえば\x01",
            "リベール行き国際定期便がある\x01",
            "このクロスベル空港ですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0x104,
        (
            "#6P#0305Fあとは『時が運び去る場所』\x01",
            "……だったか？\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0x102,
        (
            "#6P#0104Fとにかく\x01",
            "探してみるしかないわね。\x02\x03",

            "#0100Fこの辺りを探してみましょう。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, -110, 0, -15030, 0)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    ClearMapFlags(0x10000000)
    SetScenarioFlags(0xD2, 2)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_28_31C2 end

    def Function_29_3502(): pass

    label("Function_29_3502")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-21960, 1250, 24660, 0)
    MoveCamera(321, 18, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(42870, 0)
    SetChrPos(0x101, -600, 0, -18300, 0)
    SetChrPos(0x102, 750, 0, -20000, 0)
    SetChrPos(0x103, 750, 0, -18300, 0)
    SetChrPos(0x104, -600, 0, -20000, 0)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)
    SetCameraDistance(59570, 4000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x10)
    Fade(500)
    OP_68(-5130, 1250, 17490, 0)
    MoveCamera(320, 27, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(60830, 0)
    OP_0D()
    OP_68(830, 1250, -11780, 8000)
    MoveCamera(315, 27, 0, 8000)
    OP_6E(300, 8000)
    SetCameraDistance(51170, 8000)
    PlaceName2(340, 200, "c_plac32", 0x0, 1500)
    Sleep(3800)

    def lambda_361A():
        OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_361A)

    def lambda_362F():
        OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_362F)

    def lambda_3644():
        OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_3644)

    def lambda_3659():
        OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_3659)
    WaitChrThread(0x3, 1)
    Sleep(300)
    Fade(500)
    OP_68(10, 850, -13380, 0)
    MoveCamera(320, 27, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(32259, 0)
    OP_0D()

    #C0133
    ChrTalk(
        0x101,
        (
            "#5P#0003Fクロスベル空港……\x01",
            "受付のカウンターは向こうだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0x102,
        (
            "#12P#0101Fカーラさんのこと、\x01",
            "早く問い合わせてみましょう！\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, -110, 0, -15030, 0)
    ClearMapFlags(0x10000000)
    SetScenarioFlags(0xD2, 2)
    EventEnd(0x5)
    Return()

    # Function_29_3502 end

    def Function_30_373F(): pass

    label("Function_30_373F")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    LoadChrToIndex("apl/ch50091.itc", 0x1E)
    OP_4B(0xA, 0xFF)
    OP_68(6620, 860, 4440, 0)
    MoveCamera(319, 27, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(32830, 0)
    SetChrPos(0x101, 6000, 10, 3800, 0)
    SetChrPos(0x102, 7200, 10, 2400, 0)
    SetChrPos(0x103, 7200, 10, 3800, 0)
    SetChrPos(0x104, 6000, 10, 2400, 0)
    SetChrPos(0xA, 6680, 0, 5530, 180)
    SetChrPos(0x23, 8580, 600, 8610, 0)
    SetChrChipByIndex(0x23, 0x1E)
    SetChrSubChip(0x23, 0x1E)
    ClearChrFlags(0x23, 0x80)
    ClearChrBattleFlags(0x23, 0x8000)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis030.itp")
    FadeToBright(500, 0)
    OP_0D()

    #C0135
    ChrTalk(
        0xA,
        (
            "#11Pやあ、君たちも\x01",
            "荷物の受け取りかい？\x02",
        )
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0xA,
        (
            "#11P手荷物を受け取るときは\x01",
            "オレに預り証を見せてくれよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0x101,
        (
            "#5P#0003F（ここは空港の\x01",
            "  手荷物受取り場か……\x01",
            "  一応聞いてみよう。）\x02\x03",

            "#0000Fええと、すみません。\x01",
            "この辺りでカードとか\x01",
            "見かけませんでしたか？\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0xA,
        (
            "#11Pカード……？\x01",
            "荷物の預り証じゃないよね？\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0xA,
        (
            "#11P悪いけど、心当たりは無いな。\x01",
            "落し物ならカウンターで\x01",
            "聞いてくれるかい？\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0x104,
        "#6P#0300Fハハ、そうッスね。\x02",
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0x103,
        "#6P#0204Fどうもお邪魔しました。\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x23, 0, 0, 31)
    Sleep(2000)
    OP_63(0x0, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x1, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x2, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x3, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(3000)
    OP_64(0x0)
    OP_64(0x1)
    OP_64(0x2)
    OP_64(0x3)
    Sleep(300)

    #C0142
    ChrTalk(
        0x101,
        "#5P#0011F#12A………えっと、あれは…………\x02",
    )
    #Auto

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0x102,
        "#6P#0111F#12Aまさかとは思うんだけど……\x02",
    )
    #Auto

    CloseMessageWindow()
    OP_68(7130, 1260, 2560, 2000)

    def lambda_3ADE():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3ADE)

    def lambda_3AEB():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_3AEB)

    def lambda_3AF8():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3AF8)
    OP_95(0x102, 8090, 10, 440, 1200, 0x0)
    OP_93(0x102, 0x2D, 0x1F4)
    Sleep(300)
    SetChrFlags(0x23, 0x80)
    SetChrBattleFlags(0x23, 0x8000)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0144
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "白い封筒を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0145
    ChrTalk(
        0x104,
        (
            "#5P#0306Fまさかンな所から流れてくるたぁな。\x02\x03",

            "#0301F怪盗Ｂのヤツも手のかかることを……\x02",
        )
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0x102,
        "#6P#0108Fええと、中身は……\x02",
    )

    CloseMessageWindow()
    OP_95(0x102, 7200, 10, 2400, 1200, 0x0)

    def lambda_3C6E():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_3C6E)

    def lambda_3C7B():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3C7B)
    Sleep(200)
    FadeToDark(300, 0, 100)
    Sound(18, 0, 100, 0)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    Sleep(600)
    SetMessageWindowPos(-1, 90, -1, 3)
    SetChrName("")

    #A0147
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "栄えある伝達者の証\x01",
            "　１１９２・１１　\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    Sleep(500)

    #C0148
    ChrTalk(
        0x101,
        "#11P#0006F……まだあるのか……\x02",
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0x104,
        "#5P#0306F喜びもつかの間だったなぁ……\x02",
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0x103,
        (
            "#12P#0200F『栄えある伝達者の証』……\x01",
            "何の事でしょうか。\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0x102,
        (
            "#6P#0103F伝達者……伝える者……\x02\x03",

            "#0100F……何かを伝える仕事をしている人が\x01",
            "その答えを持っているのかもしれないわ。\x02\x03",

            "#0106F……それが何だかは分からないけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0x101,
        (
            "#11P#0000Fとにかく……\x01",
            "心当たりを探してみよう。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, 6780, 10, 3210, 0)
    OP_4C(0xA, 0xFF)
    OP_D5(0x1E)
    OP_CA(0x1, 0xFF, 0x0)
    OP_29(0x22, 0x1, 0x5)
    SetScenarioFlags(0x0, 7)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_30_373F end

    def Function_31_3ECA(): pass

    label("Function_31_3ECA")

    OP_96(0x23, 0x212A, 0x258, 0x866, 0x2DA, 0x0)
    OP_96(0x23, 0x2300, 0x258, 0x532, 0x2DA, 0x0)
    OP_96(0x23, 0x260C, 0x258, 0x456, 0x2DA, 0x0)
    Return()

    # Function_31_3ECA end

    def Function_32_3F07(): pass

    label("Function_32_3F07")

    EventBegin(0x0)
    OP_4B(0x8, 0xFF)
    FadeToDark(1000, 0, -1)
    OP_0D()
    LoadChrToIndex("chr/ch34500.itc", 0x1E)
    OP_68(-7940, 850, 2230, 0)
    MoveCamera(314, 21, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(32180, 0)
    SetChrPos(0x101, -6570, 0, 2270, 266)
    SetChrPos(0x102, -6260, 0, 970, 266)
    SetChrPos(0x103, -4860, 0, 910, 266)
    SetChrPos(0x104, -5170, 0, 2290, 266)
    SetChrPos(0x24, -3120, 0, -6240, 0)
    SetChrChipByIndex(0x24, 0x1E)
    SetChrSubChip(0x24, 0x0)
    ClearChrFlags(0x24, 0x80)
    ClearChrBattleFlags(0x24, 0x8000)
    SetChrFlags(0x12, 0x80)
    SetChrBattleFlags(0x12, 0x8000)
    SetChrFlags(0x13, 0x80)
    SetChrBattleFlags(0x13, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()

    #C0153
    ChrTalk(
        0x101,
        (
            "#12P#0000Fすみません、よろしいですか？\x01",
            "至急問い合わせたい事が……\x02",
        )
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0x8,
        "#5Pあら……何でしょうか。\x02",
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0x102,
        (
            "#6P#0100Fええと、リベール行きの定期便に\x01",
            "カーラ・キャンベルという方が\x01",
            "乗っているはずなんです。\x02\x03",

            "搭乗手続きは\x01",
            "もう済んでしまっているでしょうか。\x02",
        )
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0x8,
        (
            "#5Pカーラ・キャンベル様ですね。\x01",
            "少々お待ち下さい……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(3000)
    OP_64(0x8)
    Sleep(300)

    #C0157
    ChrTalk(
        0x8,
        (
            "#5P申し訳ありませんが、\x01",
            "そのような方は……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    #C0158
    ChrTalk(
        0x102,
        "#6P#0105Fほ、本当ですか……？\x02",
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0x101,
        (
            "#12P#0003Fおかしいな、\x01",
            "この便のはずなんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0x104,
        (
            "#12P#0305Fリベール行きの便ってのは\x01",
            "１つしかないんだよな？\x02",
        )
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0x103,
        (
            "#12P#0200Fええ、まだ出航は\x01",
            "していないはずですが……\x02",
        )
    )

    CloseMessageWindow()

    #N0162
    NpcTalk(
        0x24,
        "声",
        "#2Pあ、あの……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    def lambda_42D5():
        OP_93(0xFE, 0xA5, 0x190)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_42D5)

    def lambda_42E2():
        OP_93(0xFE, 0xA5, 0x190)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_42E2)

    def lambda_42EF():
        OP_93(0xFE, 0xA5, 0x190)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_42EF)

    def lambda_42FC():
        OP_93(0xFE, 0xA5, 0x190)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_42FC)

    def lambda_4309():
        OP_93(0xFE, 0xA5, 0x190)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_4309)
    OP_68(-3470, 1250, -3500, 2000)
    Sleep(2000)

    #N0163
    NpcTalk(
        0x24,
        "メイド",
        "#6Pやっぱり……\x02",
    )

    CloseMessageWindow()

    #N0164
    NpcTalk(
        0x24,
        "メイド",
        "#6Pあの、警察の方ですよね……？\x02",
    )

    CloseMessageWindow()
    Fade(500)
    OP_68(-6070, 1250, -470, 0)
    MoveCamera(299, 22, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(30600, 0)
    SetChrPos(0x24, -3960, 0, -3890, 355)
    OP_96(0x24, 0xFFFFECD2, 0x0, 0xFFFFF556, 0x3E8, 0x0)
    OP_0D()

    #C0165
    ChrTalk(
        0x102,
        (
            "#11P#0105Fあ、確かキャンベル議員の所の\x01",
            "マーシャさん……\x02",
        )
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0x103,
        (
            "#11P#0200Fもしや、お嬢さんと\x01",
            "家出をなさっているメイドの？\x02",
        )
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0x24,
        "#6Pは、はい、そうです……\x02",
    )

    CloseMessageWindow()
    OP_63(0x24, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x1)
    Sleep(1700)

    #C0168
    ChrTalk(
        0x24,
        (
            "#6P……お嬢様は……\x01",
            "リベール行きではないんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0x24,
        (
            "#6Pあれは旦那様の目をくらますために\x01",
            "わざと言いふらされた事で……\x02",
        )
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0x24,
        (
            "#6P本当は共和国の\x01",
            "知り合いのお宅に\x01",
            "身を寄せられるつもりなんです。\x02",
        )
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
    Sleep(1200)

    #C0171
    ChrTalk(
        0x101,
        (
            "#11P#0005F共和国……！？\x01",
            "しまった、鉄道の方だったか……！\x02",
        )
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0x24,
        "#6P急げばまだ間に合います！\x02",
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0x24,
        (
            "#6P……す、す、すみません、\x01",
            "こんな事をしでかしてしまって。\x02",
        )
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0x24,
        (
            "#6Pでもあの、できれば……\x01",
            "お嬢様を連れ戻してあげてください。\x02",
        )
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0x24,
        (
            "#6Pお嬢様も本当は\x01",
            "クロスベルを離れたくないんです……\x02",
        )
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0x104,
        (
            "#11P#0303F事情アリっつーわけか。\x02\x03",

            "#0300Fうっし、行こうぜ。\x01",
            "とっとと連れ戻してやろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0x103,
        (
            "#11P#0203F共和国行きは……（カタカタ）\x01",
            "そろそろ発車時間ですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0x101,
        "#11P#0001F……よし、急ごう！\x02",
    )

    CloseMessageWindow()

    def lambda_477F():
        OP_93(0xFE, 0xA5, 0x190)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_477F)

    def lambda_478C():
        OP_93(0xFE, 0xA5, 0x190)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_478C)

    def lambda_4799():
        OP_93(0xFE, 0xA5, 0x190)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_4799)

    def lambda_47A6():
        OP_93(0xFE, 0xA5, 0x190)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_47A6)
    Sleep(200)

    def lambda_47B6():

        label("loc_47B6")

        TurnDirection(0xFE, 0x101, 300)
        Yield()
        Jump("loc_47B6")

    QueueWorkItem2(0x24, 1, lambda_47B6)
    OP_68(-3070, 1250, -2850, 3000)
    MoveCamera(314, 28, 0, 3000)
    OP_6E(300, 3000)
    SetCameraDistance(30680, 3000)
    BeginChrThread(0x103, 1, 0, 36)
    BeginChrThread(0x104, 1, 0, 35)
    BeginChrThread(0x101, 1, 0, 33)
    BeginChrThread(0x102, 1, 0, 34)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)

    def lambda_4816():
        TurnDirection(0xFE, 0x24, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4816)

    def lambda_4823():
        TurnDirection(0xFE, 0x24, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4823)
    Sleep(400)
    OP_6F(0x79)

    #C0179
    ChrTalk(
        0x101,
        "#12P#0000Fありがとう、助かったよ。\x02",
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0x102,
        (
            "#6P#0100Fマーシャさんはキャンベル議員に\x01",
            "話を付けておいてくれないかしら。\x02\x03",

            "私たちで何とか\x01",
            "連れ戻してくるから。\x02",
        )
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0x24,
        (
            "#5Pは、はい。\x01",
            "どうかお嬢様をお願いします！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4900():
        OP_93(0xFE, 0xA5, 0x190)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4900)

    def lambda_490D():
        OP_93(0xFE, 0xA5, 0x190)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_490D)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)

    def lambda_4922():
        OP_95(0xFE, 1190, 0, -16350, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4922)

    def lambda_493C():
        OP_95(0xFE, -670, 0, -16360, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_493C)
    Sleep(500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x104, 0x1)
    EndChrThread(0x24, 0x1)
    SetChrPos(0x0, 30, 0, -15120, 180)
    OP_4C(0x8, 0xFF)
    OP_93(0x8, 0x5A, 0x0)
    SetChrFlags(0x24, 0x80)
    SetChrBattleFlags(0x24, 0x8000)
    OP_49()
    OP_D5(0x1E)
    ClearChrFlags(0x12, 0x80)
    ClearChrBattleFlags(0x12, 0x8000)
    ClearChrFlags(0x13, 0x80)
    ClearChrBattleFlags(0x13, 0x8000)
    OP_29(0x2D, 0x1, 0x9)
    Sleep(1000)
    EventEnd(0x5)
    NewScene("r1500", 104, 0, 0)
    IdleLoop()
    Return()

    # Function_32_3F07 end

    def Function_33_49C5(): pass

    label("Function_33_49C5")

    OP_95(0xFE, -2100, 0, -2600, 4000, 0x0)
    Return()

    # Function_33_49C5 end

    def Function_34_49DA(): pass

    label("Function_34_49DA")

    OP_95(0xFE, -2700, 0, -3900, 4000, 0x0)
    Return()

    # Function_34_49DA end

    def Function_35_49EF(): pass

    label("Function_35_49EF")

    OP_95(0xFE, 670, 0, -4290, 5000, 0x0)
    OP_95(0xFE, -400, 0, -16000, 5000, 0x0)
    Return()

    # Function_35_49EF end

    def Function_36_4A18(): pass

    label("Function_36_4A18")

    OP_95(0xFE, 670, 0, -5760, 5000, 0x0)
    OP_95(0xFE, -400, 0, -12500, 5000, 0x0)
    Return()

    # Function_36_4A18 end

    def Function_37_4A41(): pass

    label("Function_37_4A41")

    EventBegin(0x1)
    OP_4B(0xA, 0xFF)
    TurnDirection(0xA, 0x0, 500)

    #C0182
    ChrTalk(
        0xA,
        (
            "おっと……\x01",
            "そっちは搭乗口の方だよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0xA,
        (
            "チケットを持ってないと\x01",
            "入れないから注意してくれよな。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, 960, 0, 5140, 180)
    OP_93(0xA, 0xB4, 0x0)
    OP_4C(0xA, 0xFF)
    EventEnd(0x4)
    Return()

    # Function_37_4A41 end

    def Function_38_4AD4(): pass

    label("Function_38_4AD4")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0184
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "クロスベル自治州へようこそ！\x01",
            "ご滞在・ご宿泊は\x01",
            "《ホテル・ミレニアム》へ！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_38_4AD4 end

    SaveToFile()

Try(main)
