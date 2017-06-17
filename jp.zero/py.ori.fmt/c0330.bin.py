from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c0330.bin",                # FileName
        "c0330",                    # MapName
        "c0330",                    # Location
        0x002C,                     # MapIndex
        "ed7100",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 44, 0, 4, 0, 5],
    )

    BuildStringList((
        "c0330",                  # 0
        "ハロルド",               # 1
        "ソフィア",               # 2
        "コリン",                 # 3
        "ハロルド",               # 4
        "ソフィア",               # 5
        "コリン",                 # 6
        "シンディ",               # 7
        "クレイユ",               # 8
    ))

    AddCharChip((
        "chr/ch09300.itc",                   # 00
        "chr/ch09302.itc",                   # 01
        "chr/ch09400.itc",                   # 02
        "chr/ch09402.itc",                   # 03
        "chr/ch07200.itc",                   # 04
        "chr/ch07202.itc",                   # 05
        "chr/ch22100.itc",                   # 06
        "chr/ch33300.itc",                   # 07
    ))

    DeclNpc(-340,    0,       4409,    315,  389,  0x0, 0,   0,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(550,     0,       2039,    180,  261,  0x0, 0,   2,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(37479,   0,       3799,    180,  257,  0x0, 0,   4,   0,   0,   1,   0,   15,  255,  0)
    DeclNpc(34450,   200,     3339,    225,  389,  0x0, 0,   1,   0,   255, 255, 0,   7,   255,  0)
    DeclNpc(34340,   200,     519,     315,  389,  0x0, 0,   3,   0,   255, 255, 0,   14,  255,  0)
    DeclNpc(31280,   200,     3420,    135,  389,  0x0, 0,   5,   0,   255, 255, 0,   16,  255,  0)
    DeclNpc(33299,   0,       -100,    0,    405,  0x0, 0,   6,   0,   0,   0,   0,   17,  255,  0)
    DeclNpc(35319,   0,       1679,    277,  389,  0x0, 0,   7,   0,   0,   0,   0,   18,  255,  0)

    ScpFunction((
        "Function_0_1E4",          # 00, 0
        "Function_1_29C",          # 01, 1
        "Function_2_2C7",          # 02, 2
        "Function_3_2F2",          # 03, 3
        "Function_4_353",          # 04, 4
        "Function_5_75E",          # 05, 5
        "Function_6_7B1",          # 06, 6
        "Function_7_13CC",         # 07, 7
        "Function_8_1745",         # 08, 8
        "Function_9_183D",         # 09, 9
        "Function_10_2850",        # 0A, 10
        "Function_11_2A95",        # 0B, 11
        "Function_12_2B5F",        # 0C, 12
        "Function_13_2C48",        # 0D, 13
        "Function_14_2DF7",        # 0E, 14
        "Function_15_305E",        # 0F, 15
        "Function_16_3C19",        # 10, 16
        "Function_17_4315",        # 11, 17
        "Function_18_442F",        # 12, 18
        "Function_19_45C0",        # 13, 19
    ))


    def Function_0_1E4(): pass

    label("Function_0_1E4")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_224"),
        (1, "loc_230"),
        (2, "loc_23C"),
        (3, "loc_248"),
        (4, "loc_254"),
        (5, "loc_260"),
        (6, "loc_26C"),
        (SWITCH_DEFAULT, "loc_278"),
    )


    label("loc_224")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_284")

    label("loc_230")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_284")

    label("loc_23C")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_284")

    label("loc_248")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_284")

    label("loc_254")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_284")

    label("loc_260")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_284")

    label("loc_26C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_284")

    label("loc_278")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_284")

    label("loc_284")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_29B")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_284")

    label("loc_29B")

    Return()

    # Function_0_1E4 end

    def Function_1_29C(): pass

    label("Function_1_29C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2C6")
    OP_94(0xFE, 0x9268, 0x157C, 0x8F48, 0x85C, 0x3E8)
    Sleep(300)
    Jump("Function_1_29C")

    label("loc_2C6")

    Return()

    # Function_1_29C end

    def Function_2_2C7(): pass

    label("Function_2_2C7")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2F1")
    OP_94(0xFE, 0xFFFFF240, 0x80C, 0xC58, 0x139C, 0x3E8)
    Sleep(300)
    Jump("Function_2_2C7")

    label("loc_2F1")

    Return()

    # Function_2_2C7 end

    def Function_3_2F2(): pass

    label("Function_3_2F2")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_352")
    OP_95(0xFE, 35110, 0, 1240, 1000, 0x0)
    OP_93(0xFE, 0x13B, 0x1F4)
    Sleep(2500)
    OP_93(0xFE, 0x87, 0x1F4)
    Sleep(100)
    OP_95(0xFE, 37510, 0, -1160, 1000, 0x0)
    OP_93(0xFE, 0x87, 0x1F4)
    Sleep(2500)
    OP_93(0xFE, 0x13B, 0x1F4)
    Sleep(100)
    Jump("Function_3_2F2")

    label("loc_352")

    Return()

    # Function_3_2F2 end

    def Function_4_353(): pass

    label("Function_4_353")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_393")
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrPos(0x8, 0, 0, 5360, 180)
    SetChrPos(0xA, 0, 0, 3930, 360)
    BeginChrThread(0xA, 0, 0, 0)
    Jump("loc_75D")

    label("loc_393")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_3A6")
    SetChrFlags(0x9, 0x80)
    Jump("loc_75D")

    label("loc_3A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_3FE")
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0x9, 0x10)
    SetChrFlags(0xF, 0x10)
    SetChrPos(0x9, 35510, 0, 3010, 222)
    SetChrPos(0xA, 37530, 0, -1240, 89)
    BeginChrThread(0xA, 0, 0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_3F9")
    ClearChrFlags(0xE, 0x10)

    label("loc_3F9")

    Jump("loc_75D")

    label("loc_3FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_434")
    SetChrPos(0x9, -370, 0, -2190, 180)
    SetChrPos(0xA, -1230, 0, -1880, 135)
    BeginChrThread(0xA, 0, 0, 0)
    Jump("loc_75D")

    label("loc_434")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_45B")
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    Jump("loc_75D")

    label("loc_45B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_4A7")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 10, 0, -2230, 180)
    SetChrPos(0x9, 32350, 0, 7580, 270)
    SetChrPos(0xA, 30940, 0, 7580, 90)
    BeginChrThread(0xA, 0, 0, 0)
    Jump("loc_75D")

    label("loc_4A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_4BF")
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    Jump("loc_75D")

    label("loc_4BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_519")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, -490, 0, 5140, 180)
    SetChrPos(0x9, 790, 0, 4260, 270)
    SetChrPos(0xA, -690, 0, 3590, 0)
    BeginChrThread(0xA, 0, 0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_514")
    SetChrFlags(0x8, 0x10)

    label("loc_514")

    Jump("loc_75D")

    label("loc_519")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_567")
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x10)
    SetChrPos(0x9, -1230, 0, 5370, 135)
    SetChrPos(0xA, -1670, 0, 3900, 45)
    BeginChrThread(0xA, 0, 0, 2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_562")
    SetChrFlags(0x8, 0x10)

    label("loc_562")

    Jump("loc_75D")

    label("loc_567")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_5BD")
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x10)
    SetChrFlags(0xA, 0x10)
    SetChrPos(0x8, 790, 0, 4260, 270)
    SetChrPos(0x9, -490, 0, 5140, 180)
    SetChrPos(0xA, -690, 0, 3590, 0)
    BeginChrThread(0xA, 0, 0, 0)
    Jump("loc_75D")

    label("loc_5BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_5D5")
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    Jump("loc_75D")

    label("loc_5D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_61A")
    SetChrPos(0x9, 5170, 0, 3210, 360)
    SetChrPos(0xA, 34480, 0, 5610, 315)
    BeginChrThread(0xA, 0, 0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_615")
    SetChrFlags(0x9, 0x10)

    label("loc_615")

    Jump("loc_75D")

    label("loc_61A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_639")
    SetChrPos(0x9, -370, 0, -2190, 180)
    Jump("loc_75D")

    label("loc_639")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_695")
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0x9, 0x10)
    SetChrPos(0x9, 35510, 0, 3010, 222)
    SetChrPos(0xA, 38540, 0, 320, 180)
    SetChrPos(0xF, 35110, 0, 1240, 315)
    BeginChrThread(0xA, 0, 0, 0)
    BeginChrThread(0xF, 0, 0, 3)
    Jump("loc_75D")

    label("loc_695")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_6CB")
    SetChrPos(0x9, 40930, 0, -1640, 90)
    SetChrPos(0xA, 40920, 0, -410, 135)
    BeginChrThread(0xA, 0, 0, 0)
    Jump("loc_75D")

    label("loc_6CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_703")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x9, -1230, 0, 5370, 135)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6A, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6FE")
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0x9, 0x10)

    label("loc_6FE")

    Jump("loc_75D")

    label("loc_703")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_735")
    SetChrPos(0x9, 4560, 0, 10380, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_730")
    SetChrFlags(0x9, 0x10)

    label("loc_730")

    Jump("loc_75D")

    label("loc_735")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_75D")
    SetChrPos(0x9, 40930, 0, -1640, 90)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 5)), scpexpr(EXPR_END)), "loc_75D")
    SetChrFlags(0x9, 0x10)

    label("loc_75D")

    Return()

    # Function_4_353 end

    def Function_5_75E(): pass

    label("Function_5_75E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_777")
    OP_10(0x0, 0x0)
    OP_10(0x3, 0x1)
    Jump("loc_77D")

    label("loc_777")

    OP_10(0x0, 0x1)
    OP_10(0x3, 0x0)

    label("loc_77D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_799")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    Jump("loc_7B0")

    label("loc_799")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_7B0")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    Jump("loc_7B0")

    label("loc_7B0")

    Return()

    # Function_5_75E end

    def Function_6_7B1(): pass

    label("Function_6_7B1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_92A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_84D")

    #C0001
    ChrTalk(
        0x8,
        (
            "#3600Fご近所で行方不明の方がでるとは……\x01",
            "私もできる限り協力するつもりです。\x02\x03",

            "こんな時こそ家族で協力して\x01",
            "支えてあげなくては。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_925")

    label("loc_84D")


    #C0002
    ChrTalk(
        0x8,
        (
            "#3600F妻はクレイユさんに\x01",
            "付き添っているそうですね。\x02\x03",

            "#3603F……クレイユさんは\x01",
            "妻の親友なんです。\x01",
            "妻もさぞかし心配でしょう……\x02\x03",

            "#3600F今は傍にいて差し上げるのが\x01",
            "良いと思います。\x01",
            "私もできる限り協力しますから。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_925")

    Jump("loc_13C8")

    label("loc_92A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_D4E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAE, 7)), scpexpr(EXPR_END)), "loc_B4B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_9E3")

    #C0003
    ChrTalk(
        0x8,
        (
            "#3603F昨日は大変お世話になって……\x01",
            "そして長々とお話を聞かせてしまって\x01",
            "申し訳ありませんでした。\x02\x03",

            "#3601Fすみません、私ももう少し\x01",
            "頭を冷やしてみます。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B46")

    label("loc_9E3")


    #C0004
    ChrTalk(
        0x8,
        (
            "#3603F昨日は大変お世話になって……\x01",
            "そして長々とお話を聞かせてしまって\x01",
            "申し訳ありませんでした。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x8)

    #C0005
    ChrTalk(
        0x8,
        (
            "#3608Fこれは私の勘なのですが……\x01",
            "昨日手伝ってくれた女の子が\x01",
            "名乗り出ることはない気がします。\x02\x03",

            "#3603Fそれは本当に、天国にいる\x01",
            "娘だったのではないかと……\x02\x03",

            "#3600F……ハハ、美化しすぎですね。\x01",
            "すみません、私も頭を冷やさないと。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_B46")

    Jump("loc_D49")

    label("loc_B4B")

    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0006
    ChrTalk(
        0x8,
        (
            "#3600F皆さん……\x02\x03",

            "昨日は本当に\x01",
            "ありがとうございました。\x01",
            "返す返すも何と礼を言えばいいか……\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x101,
        "#0000Fいえ、それはもう。\x02",
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x102,
        (
            "#0100Fご家族も少し\x01",
            "落ち着かれたみたいですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x8,
        (
            "#3603Fええ、ソフィアとコリンには\x01",
            "ゆっくり休むように言ってあります。\x02\x03",

            "#3600Fコリンはまだ懲りてない\x01",
            "ようなんですが、ははは……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x8)

    #C0010
    ChrTalk(
        0x8,
        (
            "#3608Fわたし達はもう懲りたのです。\x01",
            "恐ろしい事や悲しい事、\x01",
            "何かを失うようなことは……\x02\x03",

            "#3603Fただ平穏に暮らしていきたい。\x01",
            "今はそれだけが望みなんです。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xAE, 7)

    label("loc_D49")

    Jump("loc_13C8")

    label("loc_D4E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_E85")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_DCE")
    OP_4B(0xA, 0xFF)

    #C0011
    ChrTalk(
        0x8,
        (
            "#3600Fコリン、支度はいいかい？\x02\x03",

            "喉が渇いたらママに言いなさい。\x01",
            "水筒を持ってきているからね。\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xA, 0xFF)
    Jump("loc_E80")

    label("loc_DCE")


    #C0012
    ChrTalk(
        0x8,
        (
            "#3600F今日はパレードだー……！\x01",
            "と息子が言い出しまして。\x02\x03",

            "たまの家族サービスです。\x01",
            "こうなったら\x01",
            "とことん付き合いますよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x101,
        "#0000Fははは……大変そうですね。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0xA, 500)
    SetChrFlags(0x8, 0x10)
    SetScenarioFlags(0x0, 0)

    label("loc_E80")

    Jump("loc_13C8")

    label("loc_E85")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_FB7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_F1F")
    OP_4B(0x9, 0xFF)

    #C0014
    ChrTalk(
        0x8,
        (
            "#3603F記念祭の間は\x01",
            "市内も渋滞しているから\x01",
            "車は使えないな……\x02\x03",

            "#3600Fソフィア、君は大丈夫かい？\x01",
            "疲れたら言ってくれよ？\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x9, 0xFF)
    Jump("loc_FB2")

    label("loc_F1F")


    #C0015
    ChrTalk(
        0x8,
        (
            "#3600Fコリンがどうしても\x01",
            "港湾区の催し物を見たいと\x01",
            "言いだしたんです。\x02\x03",

            "昨日は疲れたと\x01",
            "音を上げていたのに……\x01",
            "こりない子だなぁ。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x9, 500)
    SetChrFlags(0x8, 0x10)
    SetScenarioFlags(0x0, 0)

    label("loc_FB2")

    Jump("loc_13C8")

    label("loc_FB7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_11E2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1081")

    #C0016
    ChrTalk(
        0x8,
        (
            "#3600Fさすがに７０周年だけあって\x01",
            "例年より人が多いと聞きますね。\x02\x03",

            "コリンも疲れてしまうといけません。\x01",
            "近所を見て回るだけにしようかと。\x02\x03",

            "皆さんの方も\x01",
            "お仕事頑張ってくださいね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11DD")

    label("loc_1081")


    #C0017
    ChrTalk(
        0x8,
        (
            "#3605Fおや皆さん、お仕事中ですか？\x02\x03",

            "#3600F大変ですね……\x01",
            "私たちはこれから\x01",
            "楽しんでくる所なんですよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x101,
        (
            "#0000Fご家族で記念祭……\x01",
            "一番オードソックスな\x01",
            "過ごし方ですよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x102,
        (
            "#0100Fふふ、私たちの事は気にせず\x01",
            "楽しんできてください。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x8,
        (
            "#3600Fそうさせて頂きます。\x02\x03",

            "なにぶん……コリンは幼いですから\x01",
            "ぐるっと回ってくる\x01",
            "だけだと思うんですが。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_11DD")

    Jump("loc_13C8")

    label("loc_11E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6A, 4)), scpexpr(EXPR_END)), "loc_13BD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1289")

    #C0021
    ChrTalk(
        0x8,
        (
            "#3600Fもしお疲れでしたら、\x01",
            "うちでゆっくり\x01",
            "休んでらしてください。\x02\x03",

            "はは、遠慮はなさらないで下さい。\x01",
            "商売柄お客様を\x01",
            "迎える事は多いですから。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13B8")

    label("loc_1289")

    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0022
    ChrTalk(
        0x8,
        (
            "#3605Fああ、これは皆さん……\x01",
            "いらっしゃってたんですか！\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x102,
        (
            "#0100Fお邪魔してしまった\x01",
            "みたいですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x8,
        (
            "#3600Fいえいえ、とんでもない。\x02\x03",

            "そうだ……もしかして\x01",
            "お疲れじゃありませんか？\x02\x03",

            "うちで良かったら\x01",
            "ゆっくり休んでらしてください。\x02\x03",

            "はは、大した\x01",
            "おもてなしもできませんが。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_13B8")

    Jump("loc_13C8")

    label("loc_13BD")

    OP_4B(0x9, 0xFF)
    Call(0, 8)
    OP_4C(0x9, 0xFF)

    label("loc_13C8")

    TalkEnd(0xFE)
    Return()

    # Function_6_7B1 end

    def Function_7_13CC(): pass

    label("Function_7_13CC")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xB)
    ClearChrFlags(0xB, 0x10)
    TurnDirection(0xB, 0x0, 0)
    OP_52(0xB, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1460")
    Jump("loc_14AA")

    label("loc_1460")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1480")
    OP_52(0xB, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_14AA")

    label("loc_1480")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_14A0")
    OP_52(0xB, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_14AA")

    label("loc_14A0")

    OP_52(0xB, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_14AA")

    OP_52(0xB, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xB, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_173D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_159F")

    #C0025
    ChrTalk(
        0xB,
        (
            "#3608Fこの数年で、娘の話をしたのは\x01",
            "皆さんが初めてなんです……\x02\x03",

            "色々考えたのですが、少しの間\x01",
            "のんびりしようと思いまして。\x02\x03",

            "いま仕事に打ち込んでも仕方ない、\x01",
            "大切なのは家族ですから。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_173D")

    label("loc_159F")


    #C0026
    ChrTalk(
        0x101,
        (
            "#0000Fハロルドさん……\x01",
            "お食事中でしたか。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0xB,
        (
            "#3600Fはは、実はしばらく\x01",
            "仕事は休みにしているんです。\x02\x03",

            "２週間ほどのんびりして\x01",
            "気持ちを整理しようかと思いまして。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1675")

    #C0028
    ChrTalk(
        0x102,
        "#0102Fそうでしたか……\x02",
    )

    CloseMessageWindow()
    Jump("loc_16D2")

    label("loc_1675")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_16A6")

    #C0029
    ChrTalk(
        0x103,
        "#0202Fそうでしたか……\x02",
    )

    CloseMessageWindow()
    Jump("loc_16D2")

    label("loc_16A6")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_16D2")

    #C0030
    ChrTalk(
        0x104,
        "#0300Fなるほどなぁ……\x02",
    )

    CloseMessageWindow()

    label("loc_16D2")


    #C0031
    ChrTalk(
        0xB,
        (
            "#3600Fここ１週間は家族そろって\x01",
            "団欒ばかりなんですよ。\x02\x03",

            "お陰で妻もコリンも\x01",
            "とても喜んでくれました。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_173D")

    SetChrSubChip(0xB, 0x0)
    TalkEnd(0xB)
    Return()

    # Function_7_13CC end

    def Function_8_1745(): pass

    label("Function_8_1745")


    #C0032
    ChrTalk(
        0x8,
        (
            "#3600Fすまない、商談が長引いてね。\x02\x03",

            "……コリンは\x01",
            "元気にしているかな。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x9,
        (
            "#3700Fええ、またお絵かきを\x01",
            "して遊んでいるわ。\x02\x03",

            "新しいお絵かき帳がほしいって\x01",
            "言っていたわよ？\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x8,
        (
            "#3600Fははは、そうか……\x01",
            "あの子も好奇心が旺盛だからな。\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x8, 0x10)
    ClearChrFlags(0x9, 0x10)
    SetScenarioFlags(0x6A, 4)
    Return()

    # Function_8_1745 end

    def Function_9_183D(): pass

    label("Function_9_183D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_18F3")
    OP_4B(0xE, 0xFF)
    OP_4B(0xF, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_18DE")

    #C0035
    ChrTalk(
        0x9,
        (
            "#3701Fでも……あの優しいご主人が\x01",
            "汚い言葉を吐くだなんて。\x02\x03",

            "なんだか心配です。\x01",
            "もしかしてご主人に\x01",
            "何かあったのではなくて？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18E6")

    label("loc_18DE")

    Call(0, 13)
    ClearChrFlags(0xE, 0x10)

    label("loc_18E6")

    OP_4C(0xE, 0xFF)
    OP_4C(0xF, 0xFF)
    Jump("loc_284C")

    label("loc_18F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_1B7B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1A23")

    #C0036
    ChrTalk(
        0x9,
        (
            "#3700F最近、仕事の方も順調なんです。\x02\x03",

            "お商売がうまくいくという\x01",
            "事ではなくて……\x01",
            "主人と２人で働くのが楽しいのです。\x02\x03",

            "#3708F……皆さんに全てお話して\x01",
            "少し吹っ切れたのかもしれませんね。\x02\x03",

            "#3700F主人なら今日はアルモリカ村へ\x01",
            "行っていますから、見かけたら\x01",
            "声を掛けてあげてくださいな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B76")

    label("loc_1A23")


    #C0037
    ChrTalk(
        0x9,
        (
            "#3700F支援課の皆さん……？\x01",
            "まあ、お久し振りです……！\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x101,
        (
            "#0000Fソフィアさん、\x01",
            "お仕事再開されたみたいですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x9,
        (
            "#3700Fええ、主人がしばらく休むと\x01",
            "言い出したときは驚きましたけど。\x02\x03",

            "#3708F色々とありましたから……\x01",
            "仕事を始める前に、気分を\x01",
            "切り替えたかったのだと思います。\x02\x03",

            "#3700Fふふ、その甲斐あってか\x01",
            "最近は仕事も順調なんですよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_1B76")

    Jump("loc_284C")

    label("loc_1B7B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_1D7F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAF, 0)), scpexpr(EXPR_END)), "loc_1BFA")

    #C0040
    ChrTalk(
        0x9,
        (
            "#3700F今日は一日\x01",
            "コリンと過ごそうと思っています。\x02\x03",

            "本当に良かった……\x01",
            "女神さま、感謝いたします……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D7A")

    label("loc_1BFA")


    #C0041
    ChrTalk(
        0x9,
        (
            "#3700Fあ……警察の皆さん。\x02\x03",

            "昨日は本当に、\x01",
            "本当にありがとうございました。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x101,
        (
            "#0000Fはは、あまり\x01",
            "気になさらないでください。\x01",
            "これも警察の仕事ですので。\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x104,
        (
            "#0300Fま、珍しく\x01",
            "警察っぽい仕事だったよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x102,
        (
            "#0100Fまた何かありましたら\x01",
            "特務支援課にご連絡ください。\x01",
            "お力になりますから。\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x9,
        (
            "#3700Fはい、それはもう……\x02\x03",

            "皆さん、ありがとうございます。\x01",
            "ぜひそうさせていただきます。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xAF, 0)

    label("loc_1D7A")

    Jump("loc_284C")

    label("loc_1D7F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_1F38")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1DEC")

    #C0046
    ChrTalk(
        0x9,
        (
            "#3700Fパレードは何時からだったかしら。\x01",
            "急がないとそろそろ\x01",
            "始まってしまいますね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F33")

    label("loc_1DEC")


    #C0047
    ChrTalk(
        0x9,
        (
            "#3700F結局コリンに\x01",
            "押し切られてしまいました。\x02\x03",

            "ふう、最近はわがままも言うし\x01",
            "甘え方も心得てきたみたいですね。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0048
    ChrTalk(
        0x9,
        (
            "#3708F……あ……………\x02\x03",

            "………………………………\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x101,
        "#0000Fどうかなさいましたか？\x02",
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x9,
        (
            "#3708Fいえ……何でもありません。\x02\x03",

            "#3700Fふふ、今日のパレードを\x01",
            "精一杯楽しまないといけませんね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_1F33")

    Jump("loc_284C")

    label("loc_1F38")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1FCD")
    OP_4B(0x8, 0xFF)

    #C0051
    ChrTalk(
        0x9,
        (
            "#3701Fコリンたら、催し物なんて\x01",
            "どこで聞いてきたのかしら……\x02\x03",

            "ともかく、私は少し心配だわ。\x02\x03",

            "ただでさえ人出が多いんだもの。\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x8, 0xFF)
    Jump("loc_284C")

    label("loc_1FCD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1FE6")
    OP_4B(0xA, 0xFF)
    Call(0, 12)
    OP_4C(0xA, 0xFF)
    Jump("loc_284C")

    label("loc_1FE6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_2116")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_206D")

    #C0052
    ChrTalk(
        0x9,
        (
            "#3700F今日は教会に\x01",
            "お祈りにいく日なんです。\x02\x03",

            "……コリンたら、靴下を履くのに\x01",
            "いつまでかかっているのかしら。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2111")

    label("loc_206D")

    SetChrPos(0xA, 9860, 4000, 23690, 45)

    #C0053
    ChrTalk(
        0x9,
        (
            "#3700Fコリン～、おしたく出来た～？\x02\x03",

            "早くしないと\x01",
            "置いていってしまうわよ～！\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0xA,
        "#100P#3805Fう～、まってよママぁ～！\x02",
    )

    CloseMessageWindow()
    SetChrPos(0xA, 34480, 0, 5610, 315)
    ClearChrFlags(0x9, 0x10)
    SetScenarioFlags(0x0, 1)

    label("loc_2111")

    Jump("loc_284C")

    label("loc_2116")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_228B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_21AC")

    #C0055
    ChrTalk(
        0x9,
        (
            "#3700F主人は今日はウルスラ病院の方に\x01",
            "行っています。\x02\x03",

            "また何かサービスして\x01",
            "くるんじゃないかしら。\x01",
            "……あの人らしいですね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2286")

    label("loc_21AC")


    #C0056
    ChrTalk(
        0x9,
        (
            "#3700F実は、先月の事件以来\x01",
            "主人はマインツの人たちには\x01",
            "１割ほど値引きしているんです。\x02\x03",

            "おかげであちらの販売は\x01",
            "ほとんどトントンなんですよ。\x01",
            "……ふう、困った人。\x02\x03",

            "でも……そんな所も\x01",
            "主人らしいと思うんですけどね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_2286")

    Jump("loc_284C")

    label("loc_228B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_2366")
    OP_4B(0xE, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_235A")

    #C0057
    ChrTalk(
        0x9,
        (
            "#3700Fそうそう、パセリは\x01",
            "そんな感じで散らして……\x02\x03",

            "うん、上出来ね。\x01",
            "きっとシンディちゃんは\x01",
            "将来いいお嫁さんになるわ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Sleep(1000)

    #C0058
    ChrTalk(
        0xE,
        "わーい、ホントですか～？\x02",
    )

    CloseMessageWindow()
    Jump("loc_235D")

    label("loc_235A")

    Call(0, 11)

    label("loc_235D")

    OP_4C(0xE, 0xFF)
    Jump("loc_284C")

    label("loc_2366")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_24A4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2427")

    #C0059
    ChrTalk(
        0x9,
        (
            "#3700F今日はお料理教室を\x01",
            "開く日なんです。\x02\x03",

            "といっても、近所の方と\x01",
            "わいわい楽しくやるだけ\x01",
            "なんですけど……\x02\x03",

            "ふふっ、ともかく準備を\x01",
            "しておかなくてはいけませんね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_249F")

    label("loc_2427")


    #C0060
    ChrTalk(
        0x9,
        (
            "#3700F本当に大した事はないんですけど、\x01",
            "近所の皆さんは\x01",
            "楽しみにしてくれているんです。\x02\x03",

            "さ、準備をしておかなくちゃ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_249F")

    Jump("loc_284C")

    label("loc_24A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_254C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6A, 4)), scpexpr(EXPR_END)), "loc_253C")

    #C0061
    ChrTalk(
        0x9,
        (
            "#3700F皆さんは主人の\x01",
            "お知り合いの方だったんですね。\x02\x03",

            "私、ハロルドの妻の\x01",
            "ソフィアと申します。\x01",
            "どうかお見知りおきくださいね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2547")

    label("loc_253C")

    OP_4B(0x8, 0xFF)
    Call(0, 8)
    OP_4C(0x8, 0xFF)

    label("loc_2547")

    Jump("loc_284C")

    label("loc_254C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_26E6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 5)), scpexpr(EXPR_END)), "loc_26D2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_25EB")

    #C0062
    ChrTalk(
        0x9,
        (
            "#3700F私、お商売のことは判りません。\x01",
            "本当はこういった事も\x01",
            "苦手なんですけれど……\x02\x03",

            "ふふ、これも\x01",
            "主人を助けるためですもの。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_26CD")

    label("loc_25EB")


    #C0063
    ChrTalk(
        0x9,
        "#3700Fええと、こちらの伝票は……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x0, 500)

    #C0064
    ChrTalk(
        0x9,
        (
            "#3700F主人が買い付けに行っている間に\x01",
            "伝票の整理をしているんです。\x02\x03",

            "私、本当はこういうのは\x01",
            "苦手なんですけれど……\x02\x03",

            "これも主人を助けるため。\x01",
            "頑張らなくてはいけませんね。\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x9, 0x10)
    SetScenarioFlags(0x0, 1)

    label("loc_26CD")

    Jump("loc_26E1")

    label("loc_26D2")

    Call(0, 10)
    OP_93(0x9, 0x0, 0x1F4)
    SetChrFlags(0x9, 0x10)

    label("loc_26E1")

    Jump("loc_284C")

    label("loc_26E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_2782")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 5)), scpexpr(EXPR_END)), "loc_276E")

    #C0065
    ChrTalk(
        0x9,
        (
            "#3700Fうん、お料理の盛り付けは\x01",
            "こうでなくちゃね。\x02\x03",

            "ふふ……あの人ったら\x01",
            "今日は早く帰って\x01",
            "きてくれるかしら。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_277D")

    label("loc_276E")

    Call(0, 10)
    OP_93(0x9, 0x5A, 0x1F4)
    SetChrFlags(0x9, 0x10)

    label("loc_277D")

    Jump("loc_284C")

    label("loc_2782")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 5)), scpexpr(EXPR_END)), "loc_2849")

    #C0066
    ChrTalk(
        0x9,
        (
            "#3700F間違えてしまってごめんなさいね。\x02\x03",

            "主人は貿易商をしているので\x01",
            "お客様もよくいらっしゃるんです。\x02\x03",

            "もし何か入用なときは\x01",
            "またぜひいらして下さいな。\x01",
            "お力になれるかもしれませんし。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_284C")

    label("loc_2849")

    Call(0, 10)

    label("loc_284C")

    TalkEnd(0xFE)
    Return()

    # Function_9_183D end

    def Function_10_2850(): pass

    label("Function_10_2850")


    #C0067
    ChrTalk(
        0x9,
        (
            "#3700Fあら……\x01",
            "主人に御用でしょうか。\x02\x03",

            "ごめんなさい、\x01",
            "ハロルドは出かけていますの。\x02\x03",

            "よろしければ私に仰ってくださいな。\x01",
            "主人に取り次いでおきますから。\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x101,
        "#0005Fえ？　えっと……\x02",
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0069
    ChrTalk(
        0x9,
        (
            "#3700Fあ、あらすみません。\x01",
            "主人のお客様ではなくて……？\x02\x03",

            "ふふ……そうよね。\x01",
            "こんな若い方達が\x01",
            "商談なんておかしいと思ったわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x102,
        (
            "#0100Fご主人は商売関係の\x01",
            "お仕事みたいですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x9,
        (
            "#3700Fええ、貿易商をしております。\x01",
            "小さな商いばかりですけれど。\x02\x03",

            "間違えてしまってごめんなさいね。\x02\x03",

            "でも、もし何か入用なときは\x01",
            "私どもの所にいらして下さいな。\x01",
            "お力になれるかもしれませんし。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x4C, 5)
    Return()

    # Function_10_2850 end

    def Function_11_2A95(): pass

    label("Function_11_2A95")


    #C0072
    ChrTalk(
        0x9,
        (
            "#3700Fごめんなさいね、\x01",
            "明日は少し用事があって。\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0xE,
        "あ、教会に行く日でしたっけ。\x02",
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0xE,
        (
            "毎週ミサに\x01",
            "参加なさってるんですよね。\x01",
            "すごいなー。\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0x9,
        (
            "#3708Fいいえ、凄いとか……\x01",
            "そんなのじゃないのよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Return()

    # Function_11_2A95 end

    def Function_12_2B5F(): pass

    label("Function_12_2B5F")


    #C0076
    ChrTalk(
        0x9,
        (
            "#3700Fほらコリン、じっとしてて……\x01",
            "お洋服が着れないでしょう？\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0xA,
        (
            "#3800Fえへへ、ぼくね～、\x01",
            "アイスたべたい！\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0x9,
        (
            "#3700Fはいはい、アイスね。\x01",
            "それじゃあアイス屋さんを探しに\x01",
            "行ってみましょうか？\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0xA,
        "#3800Fうん、さがしにいく～！\x02",
    )

    CloseMessageWindow()
    Return()

    # Function_12_2B5F end

    def Function_13_2C48(): pass

    label("Function_13_2C48")


    #C0080
    ChrTalk(
        0xE,
        (
            "昨日クレイユさんの所のご主人と\x01",
            "すれ違ったんですけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0xE,
        (
            "何だか最近\x01",
            "様子が変じゃありません？\x01",
            "横柄になったっていうか……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xF, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0082
    ChrTalk(
        0xF,
        "あら……そうでしたの？\x02",
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0xF,
        "うーん、そういえば最近……\x02",
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0xF,
        (
            "汚い言葉を吐くようになった気が\x01",
            "するような、しないような……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0xE, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0085
    ChrTalk(
        0xE,
        "ど、どっちなんですか～？\x02",
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x9,
        (
            "#3700Fふふ……クレイユさんはいつも\x01",
            "のんびりしていますわね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Return()

    # Function_13_2C48 end

    def Function_14_2DF7(): pass

    label("Function_14_2DF7")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xC)
    ClearChrFlags(0xC, 0x10)
    TurnDirection(0xC, 0x0, 0)
    OP_52(0xC, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2E8B")
    Jump("loc_2ED5")

    label("loc_2E8B")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2EAB")
    OP_52(0xC, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2ED5")

    label("loc_2EAB")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2ECB")
    OP_52(0xC, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2ED5")

    label("loc_2ECB")

    OP_52(0xC, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2ED5")

    OP_52(0xC, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xC, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2F53")

    #C0087
    ChrTalk(
        0xC,
        (
            "#3700F皆さん、またいらしてくださいね。\x01",
            "いつでもご馳走いたしますから。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3056")

    label("loc_2F53")


    #C0088
    ChrTalk(
        0xC,
        (
            "#3700Fあら、皆さん……\x02\x03",

            "よろしかったらご一緒にいかが？\x01",
            "たくさん作ってありますから。\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0x101,
        (
            "#0000Fははは、今日は少し\x01",
            "用事があるもので……\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x153,
        "#1110Fまったこんどねーっ！\x02",
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0xC,
        (
            "#3700Fふふ……そうね。\x01",
            "それじゃあまた今度ね。\x01",
            "（ロイドさんの妹さんかしら……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_3056")

    SetChrSubChip(0xC, 0x0)
    TalkEnd(0xC)
    Return()

    # Function_14_2DF7 end

    def Function_15_305E(): pass

    label("Function_15_305E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x1, 0x1)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x1, 0x2)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3121")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x1, 0x6)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_309C")
    Call(0, 19)
    Jump("loc_311C")

    label("loc_309C")


    #C0092
    ChrTalk(
        0xA,
        (
            "#3800Fその仔猫ね、ときどき\x01",
            "へいのうえをあるいてたよ。\x02\x03",

            "#3809Fそこのまどからみてるとね、\x01",
            "とことこ～ってとおっていくんだ～。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_311C")

    Jump("loc_3C15")

    label("loc_3121")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_31A7")

    #C0093
    ChrTalk(
        0xA,
        (
            "#3800Fママ、きょうはごきんじょに\x01",
            "おとまりするんだって。\x02\x03",

            "#3809Fえへへ、かわりにパパが\x01",
            "いっしょにねてくれるんだよ！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C15")

    label("loc_31A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_3201")

    #C0094
    ChrTalk(
        0xA,
        (
            "#3800Fママ、ちょっと出かけてくるって～。\x02\x03",

            "どこにいっちゃったのかな～。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C15")

    label("loc_3201")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_32F8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_3251")

    #C0095
    ChrTalk(
        0xA,
        (
            "#3800Fえへへ～、つまみぐい\x01",
            "するときのパパの真似～！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_32F3")

    label("loc_3251")


    #C0096
    ChrTalk(
        0xA,
        (
            "#3800Fえへへ～、パパはいつも\x01",
            "こうやるんだよ～！\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xA, 0x59, 0x1F4)

    #C0097
    ChrTalk(
        0xA,
        (
            "#3800F『やあ、これはおいしそうだなぁ。\x01",
            "  ソフィア、一ついただくよ～？』\x02\x03",

            "パクリ、もぐもぐ……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_32F3")

    Jump("loc_3C15")

    label("loc_32F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_336D")

    #C0098
    ChrTalk(
        0xA,
        (
            "#3800Fきょうはママのお手伝いするんだー。\x02\x03",

            "ぼくもね、いつかパパみたいな\x01",
            "しょうにんになるんだもん。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C15")

    label("loc_336D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_35F6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAF, 1)), scpexpr(EXPR_END)), "loc_340B")

    #C0099
    ChrTalk(
        0xA,
        (
            "#3800Fぼく、きょうは\x01",
            "ママといっしょにいるー。\x02\x03",

            "#3809Fおにいちゃんたち、\x01",
            "きのうはありがとー。\x02\x03",

            "あのおねえちゃんにも\x01",
            "よろしくねー！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_35F1")

    label("loc_340B")


    #C0100
    ChrTalk(
        0xA,
        (
            "#3800Fあ、きのうの\x01",
            "おにいちゃんたちだー！\x02\x03",

            "あのねー、ママきょうは\x01",
            "いっしょにご本をよもうって。\x02\x03",

            "でもぼく、おそとに\x01",
            "あそびにいきたいんだけどなー……\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0x104,
        (
            "#0300Fハハ、相変わらずの\x01",
            "ガキンチョだな……\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x101,
        (
            "#0000Fコリン君、あんまりママを\x01",
            "心配させちゃダメだぞ。\x02\x03",

            "昨日だって、あのお姉ちゃんが\x01",
            "来てくれなかったら\x01",
            "こわーい目に遭ってたんだからさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0xA,
        (
            "#3805Fうん……わかったー。\x01",
            "ぼくきょうはママといっしょにいる。\x02\x03",

            "#3809Fおにいちゃんたち、ありがとー。\x01",
            "あのおねえちゃんにもよろしくねー！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xAF, 1)

    label("loc_35F1")

    Jump("loc_3C15")

    label("loc_35F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_367C")

    #C0104
    ChrTalk(
        0xA,
        (
            "#3800Fパパとママにお願いしたらね、\x01",
            "パレードをみにいってもいいって！\x02\x03",

            "#3809Fわーい、やったー！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    Jump("loc_3C15")

    label("loc_367C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_374D")

    #C0105
    ChrTalk(
        0xA,
        (
            "#3800Fえへへー、きのう\x01",
            "ガイコクからきた人にきいたんだ。\x02\x03",

            "みなとの方で\x01",
            "すっごくたのしいこと\x01",
            "やってるんだって。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)

    #C0106
    ChrTalk(
        0xA,
        (
            "#3800Fどんなことしてるのかなー。\x01",
            "ぼくも見にいきたい！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C15")

    label("loc_374D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_3766")
    OP_4B(0x9, 0xFF)
    Call(0, 12)
    OP_4C(0x9, 0xFF)
    Jump("loc_3C15")

    label("loc_3766")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_37C7")

    #C0107
    ChrTalk(
        0xA,
        (
            "#3800Fおみずやり、おみずやり……\x02\x03",

            "あさね、おみずをあげるの\x01",
            "わすれてたんだー。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C15")

    label("loc_37C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_38E4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_3877")

    #C0108
    ChrTalk(
        0xA,
        (
            "#3800Fコリンがいいこにしてたら……\x01",
            "パパ、きねんさいには\x01",
            "いっしょに遊んでくれるかな。\x02\x03",

            "うん、じゃあぼくいいこにする！\x01",
            "パパとママと遊びたいんだもん！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_38DF")

    label("loc_3877")


    #C0109
    ChrTalk(
        0xA,
        (
            "#3800Fパパはきょうもお仕事なんだよね。\x02\x03",

            "うーん……\x02\x03",

            "きねんさいには\x01",
            "ぼくと遊んでくれるのかなー。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_38DF")

    Jump("loc_3C15")

    label("loc_38E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_3976")

    #C0110
    ChrTalk(
        0xA,
        (
            "#3800Fあのねー、きょうは\x01",
            "おりょうりきょうしつなんだよー！\x02\x03",

            "#3809Fすっごくたのしいの。\x02\x03",

            "ぼくもママたちの\x01",
            "お手伝いをするんだー！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C15")

    label("loc_3976")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_39CD")

    #C0111
    ChrTalk(
        0xA,
        (
            "#3800Fえっへん、あのねー……\x02\x03",

            "ぼくもおりょうり、\x01",
            "てつだうんだよ～！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C15")

    label("loc_39CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_3AB1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A54")

    #C0112
    ChrTalk(
        0xA,
        (
            "#3800Fあれ～、なんだか\x01",
            "パパが帰ってきたよかんがする！\x02\x03",

            "だってね～、パパのくるまの\x01",
            "おとがしたんだもん！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3AAC")

    label("loc_3A54")


    #C0113
    ChrTalk(
        0xA,
        (
            "#3800Fパパ、はやく\x01",
            "あがってこないかな～。\x02\x03",

            "えへへ、わあって\x01",
            "おどろかしちゃおっと！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3AAC")

    Jump("loc_3C15")

    label("loc_3AB1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_3B28")

    #C0114
    ChrTalk(
        0xA,
        (
            "#3800Fきょうね、パパが\x01",
            "行ってきますの\x01",
            "チューしてくれたんだ～。\x02\x03",

            "えへへ、はやおきして\x01",
            "よかったな～。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C15")

    label("loc_3B28")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_3BAB")

    #C0115
    ChrTalk(
        0xA,
        (
            "#3800Fあのねー、パパは\x01",
            "ぼうえきしょうのお仕事を\x01",
            "してるんだよー。\x02\x03",

            "あさはいっつも、\x01",
            "はやくにでかけちゃうんだー。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C15")

    label("loc_3BAB")


    #C0116
    ChrTalk(
        0xA,
        (
            "#3800Fたらら、ららら～ん♪\x01",
            "きょうはおえかきしてあそぶんだー！\x02\x03",

            "おにいちゃんたちも、\x01",
            "ぼくとあそぶ～？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3C15")

    TalkEnd(0xFE)
    Return()

    # Function_15_305E end

    def Function_16_3C19(): pass

    label("Function_16_3C19")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xD)
    ClearChrFlags(0xD, 0x10)
    TurnDirection(0xD, 0x0, 0)
    OP_52(0xD, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3CAD")
    Jump("loc_3CF7")

    label("loc_3CAD")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3CCD")
    OP_52(0xD, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3CF7")

    label("loc_3CCD")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3CED")
    OP_52(0xD, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3CF7")

    label("loc_3CED")

    OP_52(0xD, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3CF7")

    OP_52(0xD, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xD, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_3D8E")

    #C0117
    ChrTalk(
        0xD,
        (
            "#3809Fおねーちゃん、カミふわふわ～！\x02\x03",

            "#3800Fまた遊びに来てね！\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0x153,
        "#1109Fうん、まったねーっ！\x02",
    )

    CloseMessageWindow()
    Jump("loc_430D")

    label("loc_3D8E")

    OP_52(0x153, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xD)
    ClearChrFlags(0xD, 0x10)
    TurnDirection(0xD, 0x153, 0)
    OP_52(0xD, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3E22")
    Jump("loc_3E6C")

    label("loc_3E22")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3E42")
    OP_52(0xD, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3E6C")

    label("loc_3E42")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3E62")
    OP_52(0xD, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3E6C")

    label("loc_3E62")

    OP_52(0xD, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3E6C")

    OP_52(0xD, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x153, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x153, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xD, 0x10)

    #C0119
    ChrTalk(
        0xD,
        (
            "#3805Fほえ～…………？\x02\x03",

            "おねーちゃん、だあれ～？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x153, 0x101, 500)

    #C0120
    ChrTalk(
        0x153,
        (
            "#1111F……おねーちゃん………？\x02\x03",

            "#1110Fねえロイドー、\x01",
            "キーアっておねーちゃんなのかなー。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x153, 500)

    #C0121
    ChrTalk(
        0x101,
        (
            "#0000Fはは……コリン君から見れば\x01",
            "キーアもお姉さんだよ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x153, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_40A3")

    #C0122
    ChrTalk(
        0x153,
        (
            "#1108Fそっかー。\x02\x03",

            "#1111Fじゃあエリィからみれば\x01",
            "ロイドはオトウト？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0x102, 0x101, 500)

    #C0123
    ChrTalk(
        0x102,
        (
            "#0112Fえ、えっと……\x01",
            "（確かに弟みたいな所は\x01",
            "  あるけど……）\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)

    #C0124
    ChrTalk(
        0x101,
        "#0006Fいや絶対違うだろ。\x02",
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0x102,
        "#0108F（……そうよねぇ……）\x02",
    )

    CloseMessageWindow()
    Jump("loc_430A")

    label("loc_40A3")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_41E7")

    #C0126
    ChrTalk(
        0x153,
        (
            "#1108Fそっかー。\x02\x03",

            "#1111Fじゃあロイドからみれば\x01",
            "ティオはイモウト？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0x103, 0x153, 500)

    #C0127
    ChrTalk(
        0x103,
        "#0203F……ええ、間違いないかと。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 500)

    #C0128
    ChrTalk(
        0x101,
        (
            "#0006Fいやいや違うだろ。\x01",
            "ティオ、そこは否定しないと。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 500)

    #C0129
    ChrTalk(
        0x103,
        (
            "#0211Fただの茶目っ気です。\x01",
            "それくらい空気読んでください。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_430A")

    label("loc_41E7")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_430A")

    #C0130
    ChrTalk(
        0x153,
        (
            "#1108Fそっかー。\x02\x03",

            "#1111Fじゃあランディからみれば\x01",
            "ロイドはオトウト？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0x104, 0x101, 500)

    #C0131
    ChrTalk(
        0x104,
        (
            "#0309Fあー、確かにそんな所もあるか？\x02\x03",

            "#0306F若いのに無茶しやがる所とか\x01",
            "あるしなぁ……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 500)

    #C0132
    ChrTalk(
        0x101,
        "#0006Fランディ、また年寄り臭いことを……\x02",
    )

    CloseMessageWindow()

    label("loc_430A")

    SetScenarioFlags(0x0, 2)

    label("loc_430D")

    SetChrSubChip(0xD, 0x0)
    TalkEnd(0xD)
    Return()

    # Function_16_3C19 end

    def Function_17_4315(): pass

    label("Function_17_4315")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_43C5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_43A8")
    OP_63(0xE, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0133
    ChrTalk(
        0xE,
        (
            "クレイユさんって\x01",
            "……ニブイっていうか……\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0xE,
        (
            "うん、いいんだけどね。\x01",
            "可愛らしい人だし。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_43C0")

    label("loc_43A8")

    OP_4B(0x9, 0xFF)
    OP_4B(0xF, 0xFF)
    Call(0, 13)
    OP_4C(0x9, 0xFF)
    OP_4C(0xF, 0xFF)
    ClearChrFlags(0xE, 0x10)

    label("loc_43C0")

    Jump("loc_442B")

    label("loc_43C5")

    OP_4B(0x9, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_4424")

    #C0135
    ChrTalk(
        0xE,
        "あ、盛り付け手伝いますよ～。\x02",
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0xE,
        (
            "えへへ、あたし\x01",
            "こういうの好きなんで㈱\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4427")

    label("loc_4424")

    Call(0, 11)

    label("loc_4427")

    OP_4C(0x9, 0xFF)

    label("loc_442B")

    TalkEnd(0xFE)
    Return()

    # Function_17_4315 end

    def Function_18_442F(): pass

    label("Function_18_442F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_44C6")
    OP_4B(0x9, 0xFF)
    OP_4B(0xE, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_44B1")

    #C0137
    ChrTalk(
        0xF,
        (
            "うーん、うーん……\x01",
            "そういえば最近、\x01",
            "様子がおかしな気が……\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0xF,
        "……しなくもないですの～。\x02",
    )

    CloseMessageWindow()
    Jump("loc_44B9")

    label("loc_44B1")

    Call(0, 13)
    ClearChrFlags(0xE, 0x10)

    label("loc_44B9")

    OP_4C(0x9, 0xFF)
    OP_4C(0xE, 0xFF)
    Jump("loc_45BC")

    label("loc_44C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_4538")

    #C0139
    ChrTalk(
        0xF,
        (
            "お料理教室の後は\x01",
            "いつもお食事会なんですの。\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0xF,
        (
            "ふふ、今日もお喋りが\x01",
            "弾んでしまいそうですの。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_45BC")

    label("loc_4538")


    #C0141
    ChrTalk(
        0xF,
        (
            "今日のお料理教室は\x01",
            "帝国風サーモンシチューが\x01",
            "メインですの。\x02",
        )
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0xF,
        (
            "うふふ、お友達で集まって\x01",
            "お料理をするのは楽しいものですわ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_45BC")

    TalkEnd(0xFE)
    Return()

    # Function_18_442F end

    def Function_19_45C0(): pass

    label("Function_19_45C0")

    EventBegin(0x0)
    Fade(800)
    OP_4B(0xA, 0xFF)
    OP_68(36520, 1500, 4730, 0)
    MoveCamera(45, 23, 0, 0)
    OP_6E(270, 0)
    SetCameraDistance(30020, 0)
    SetChrPos(0x101, 36580, 0, 5220, 180)
    SetChrPos(0x102, 37720, 0, 5220, 180)
    SetChrPos(0x103, 36580, 0, 6620, 180)
    SetChrPos(0x104, 37720, 0, 6620, 180)
    SetChrPos(0xA, 37190, 0, 3550, 0)
    OP_0D()

    #C0143
    ChrTalk(
        0x101,
        (
            "#5P#0000Fちょっといいかな。\x02\x03",

            "君は仔猫を\x01",
            "飼ってたりしないかな？\x01",
            "もしくは心当たりとか……\x02",
        )
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0xA,
        (
            "#12P#3805Fこねこ～……？\x01",
            "どんな猫ちゃんなの～？\x02",
        )
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0x101,
        "#5P#0000Fああ、この子なんだけど……\x02",
    )

    CloseMessageWindow()
    Sound(804, 0, 100, 0)
    Sleep(300)
    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0146
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ロイドはジャケットから\x01",
            "仔猫の姿を出してみせた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToBright(300, 0)
    Sound(823, 0, 100, 0)
    OP_63(0xA, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(300)

    #C0147
    ChrTalk(
        0xA,
        "#12P#3805Fあっ、見たことあるー！\x02",
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0x102,
        "#5P#0105Fあら本当……？\x02",
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0xA,
        (
            "#12P#3800Fうん、ときどき\x01",
            "へいのうえをあるいてるんだよ～。\x02\x03",

            "んっとお、さいきんは\x01",
            "みてなかったけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0x104,
        (
            "#5P#0303Fふむ、元々はこの辺りの\x01",
            "猫だったみてえだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0x103,
        (
            "#5P#0200Fとなると飼い主も\x01",
            "住宅街にいる可能性が高そうですね。\x01",
            "探してみましょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0x101,
        "#5P#0000Fありがとう、助かったよ。\x02",
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0xA,
        (
            "#12P#3809Fうん、お兄ちゃんたち\x01",
            "まったねー！\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 37320, 0, 5200, 180)
    BeginChrThread(0xA, 0, 0, 1)
    OP_29(0x8, 0x1, 0x6)
    EventEnd(0x5)
    Return()

    # Function_19_45C0 end

    SaveToFile()

Try(main)
