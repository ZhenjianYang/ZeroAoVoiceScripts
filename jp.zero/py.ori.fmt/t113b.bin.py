from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t113b.bin",                # FileName
        "t113b",                    # MapName
        "t113b",                    # Location
        0x0049,                     # MapIndex
        "ed7125",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 73, 0, 4, 0, 5],
    )

    BuildStringList((
        "t113b",                  # 0
        "ワジ",                   # 1
        "ジェイムズ",             # 2
        "エヴェリン夫人",         # 3
        "ニキータ",               # 4
        "パメラ",                 # 5
        "執事フェント",           # 6
        "執事クリストフ",         # 7
        "ジュディ",               # 8
    ))

    AddCharChip((
        "apl/ch50353.itc",                   # 00
        "chr/ch27800.itc",                   # 01
        "chr/ch33300.itc",                   # 02
        "chr/ch26800.itc",                   # 03
        "chr/ch25600.itc",                   # 04
        "chr/ch25900.itc",                   # 05
        "chr/ch25700.itc",                   # 06
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

    DeclNpc(-150,    100,     -1149,   180,  469,  0x0, 0,   0,   0,   255, 255, 0,   6,   255,  0)
    DeclNpc(5349,    0,       -3500,   315,  385,  0x0, 0,   1,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(4000,    0,       -2150,   135,  385,  0x0, 0,   2,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(4500,    0,       -3500,   180,  385,  0x0, 0,   3,   0,   0,   0,   255, 255, 255,  0)
    DeclNpc(5599,    0,       -12590,  0,    257,  0x0, 0,   4,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(3859,    0,       -13729,  0,    257,  0x0, 0,   5,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(-3150,   0,       3569,    90,   385,  0x0, 0,   5,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(-2099,   0,       3569,    270,  385,  0x0, 0,   6,   0,   0,   0,   0,   13,  255,  0)

    ScpFunction((
        "Function_0_22C",          # 00, 0
        "Function_1_2E4",          # 01, 1
        "Function_2_395",          # 02, 2
        "Function_3_3C0",          # 03, 3
        "Function_4_41A",          # 04, 4
        "Function_5_533",          # 05, 5
        "Function_6_53D",          # 06, 6
        "Function_7_803",          # 07, 7
        "Function_8_87F",          # 08, 8
        "Function_9_8E6",          # 09, 9
        "Function_10_A32",         # 0A, 10
        "Function_11_CE0",         # 0B, 11
        "Function_12_ECB",         # 0C, 12
        "Function_13_F01",         # 0D, 13
        "Function_14_F51",         # 0E, 14
        "Function_15_1A07",        # 0F, 15
    ))


    def Function_0_22C(): pass

    label("Function_0_22C")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_26C"),
        (1, "loc_278"),
        (2, "loc_284"),
        (3, "loc_290"),
        (4, "loc_29C"),
        (5, "loc_2A8"),
        (6, "loc_2B4"),
        (SWITCH_DEFAULT, "loc_2C0"),
    )


    label("loc_26C")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_2CC")

    label("loc_278")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_2CC")

    label("loc_284")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_2CC")

    label("loc_290")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_2CC")

    label("loc_29C")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_2CC")

    label("loc_2A8")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_2CC")

    label("loc_2B4")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2CC")

    label("loc_2C0")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2CC")

    label("loc_2CC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2E3")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2CC")

    label("loc_2E3")

    Return()

    # Function_0_22C end

    def Function_1_2E4(): pass

    label("Function_1_2E4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_394")
    OP_95(0xFE, 3320, 0, -13010, 2000, 0x0)
    OP_93(0xFE, 0x10E, 0x190)
    Sleep(1300)
    OP_93(0xFE, 0x0, 0x190)
    Sleep(100)
    OP_95(0xFE, 3320, 0, -6980, 2000, 0x0)
    OP_93(0xFE, 0x10E, 0x190)
    Sleep(1300)
    OP_93(0xFE, 0xB4, 0x190)
    Sleep(100)
    OP_95(0xFE, 3320, 0, -9020, 2000, 0x0)
    OP_93(0xFE, 0x10E, 0x190)
    Sleep(1300)
    OP_93(0xFE, 0xB4, 0x190)
    Sleep(100)
    OP_95(0xFE, 3320, 0, -16960, 2000, 0x0)
    OP_93(0xFE, 0x10E, 0x190)
    Sleep(1300)
    OP_93(0xFE, 0x0, 0x190)
    Sleep(100)
    Jump("Function_1_2E4")

    label("loc_394")

    Return()

    # Function_1_2E4 end

    def Function_2_395(): pass

    label("Function_2_395")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3BF")
    OP_94(0xFE, 0x79E, 0xFFFFFB1E, 0x19E6, 0xFFFFFD8A, 0x3E8)
    Sleep(300)
    Jump("Function_2_395")

    label("loc_3BF")

    Return()

    # Function_2_395 end

    def Function_3_3C0(): pass

    label("Function_3_3C0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_419")
    OP_95(0xFE, -5090, 0, -19580, 2000, 0x0)
    OP_93(0xFE, 0x10E, 0x190)
    Sleep(1300)
    OP_93(0xFE, 0x0, 0x190)
    Sleep(100)
    OP_95(0xFE, -5090, 0, -1190, 2000, 0x0)
    Sleep(1000)
    OP_93(0xFE, 0xB4, 0x190)
    Sleep(100)
    Jump("Function_3_3C0")

    label("loc_419")

    Return()

    # Function_3_3C0 end

    def Function_4_41A(): pass

    label("Function_4_41A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 5)), scpexpr(EXPR_END)), "loc_46A")
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 4670, 0, -1000, 0)
    BeginChrThread(0xC, 0, 0, 2)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, -5090, 0, -1190, 180)
    BeginChrThread(0xD, 0, 0, 3)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    Jump("loc_521")

    label("loc_46A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_END)), "loc_4B0")
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 3020, 0, -13010, 360)
    BeginChrThread(0xC, 0, 0, 1)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, -5090, 0, -1190, 180)
    BeginChrThread(0xD, 0, 0, 3)
    Jump("loc_521")

    label("loc_4B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 1)), scpexpr(EXPR_END)), "loc_4F0")
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 3020, 0, -13010, 360)
    BeginChrThread(0xC, 0, 0, 1)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 1660, 0, 4960, 180)
    Jump("loc_521")

    label("loc_4F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_521")
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_521")
    ClearChrFlags(0xB, 0x80)

    label("loc_521")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_532")
    Event(0, 14)

    label("loc_532")

    Return()

    # Function_4_41A end

    def Function_5_533(): pass

    label("Function_5_533")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 5)), scpexpr(EXPR_END)), "loc_53C")

    label("loc_53C")

    Return()

    # Function_5_533 end

    def Function_6_53D(): pass

    label("Function_6_53D")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5D1")
    Jump("loc_61B")

    label("loc_5D1")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5F1")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_61B")

    label("loc_5F1")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_611")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_61B")

    label("loc_611")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_61B")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7B4")

    #C0001
    ChrTalk(
        0x8,
        (
            "#5702Fフフ……また後でね。\x02\x03",

            "#5709Fまだこの喧嘩は続くだろうから\x01",
            "僕もしばらく付き合うことにするよ。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_709")

    #C0002
    ChrTalk(
        0x102,
        (
            "#5306Fあなた……\x01",
            "さっき煽ってたくせに\x01",
            "他人事みたいなことを言って……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_786")

    label("loc_709")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_73B")

    #C0003
    ChrTalk(
        0x103,
        "#5411F……まるで他人事ですね。\x02",
    )

    CloseMessageWindow()
    Jump("loc_786")

    label("loc_73B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_786")

    #C0004
    ChrTalk(
        0x104,
        (
            "#5602F火遊びしてみない？\x01",
            "なんて言ってたくせに\x01",
            "よく言うぜ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_786")


    #C0005
    ChrTalk(
        0x101,
        "#5106Fま、まぁ……ほどほどにな？\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_7FB")

    label("loc_7B4")


    #C0006
    ChrTalk(
        0x8,
        (
            "#5702Fフフ……また後でね。\x02\x03",

            "２人の気が済んだ後で\x01",
            "会場に向かうよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7FB")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_6_53D end

    def Function_7_803(): pass

    label("Function_7_803")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_818")
    Call(0, 9)
    Jump("loc_87B")

    label("loc_818")

    TurnDirection(0x9, 0xA, 0)

    #C0007
    ChrTalk(
        0x9,
        (
            "この通りだ、\x01",
            "何度でも頭を下げよう！\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x9,
        (
            "だからエヴェリン……\x01",
            "どうか機嫌を直してくれ！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_87B")

    TalkEnd(0xFE)
    Return()

    # Function_7_803 end

    def Function_8_87F(): pass

    label("Function_8_87F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_894")
    Call(0, 9)
    Jump("loc_8E2")

    label("loc_894")

    TurnDirection(0xA, 0x9, 0)

    #C0009
    ChrTalk(
        0xA,
        (
            "もう貴方のことなんて知りません！\x01",
            "こうなったら私も、ワジ君と……！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8E2")

    TalkEnd(0xFE)
    Return()

    # Function_8_87F end

    def Function_9_8E6(): pass

    label("Function_9_8E6")

    OP_4B(0x9, 0xFF)
    OP_4B(0xA, 0xFF)
    TurnDirection(0x9, 0xA, 0)
    TurnDirection(0xA, 0x9, 0)

    #C0010
    ChrTalk(
        0x9,
        (
            "あぁエヴェリン、待ってくれ！\x01",
            "僕が悪かった……\x01",
            "実家に帰るなんて言わないでくれ。\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x9,
        (
            "ニキータ君とは、その……\x01",
            "魔が差してしまったというか……\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0xA,
        "よくもまぁ抜け抜けと……！\x02",
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0xA,
        (
            "もううんざりです！\x01",
            "お義母様にも今回のことは\x01",
            "報告させて頂きますから！\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x9,
        (
            "そ、そんな！\x01",
            "それだけは勘弁してくれ……！\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x9, 0xFF)
    OP_4C(0xA, 0xFF)
    SetScenarioFlags(0x0, 1)
    Return()

    # Function_9_8E6 end

    def Function_10_A32(): pass

    label("Function_10_A32")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 5)), scpexpr(EXPR_END)), "loc_B23")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AF6")

    #C0015
    ChrTalk(
        0xFE,
        "あら、そのお子様は……？\x02",
    )

    CloseMessageWindow()

    #N0016
    NpcTalk(
        0x101,
        "キーア",
        "#5810Fキーアだよー！\x02",
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0xFE,
        (
            "え、えぇっと……？\x01",
            "（招待客にそんな子いたかしら……）\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x101,
        "#0001Fす、すみません、急いでますので！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_B1E")

    label("loc_AF6")


    #C0019
    ChrTalk(
        0xFE,
        "（招待客にこんな子いたかしら……）\x02",
    )

    CloseMessageWindow()

    label("loc_B1E")

    Jump("loc_CDC")

    label("loc_B23")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_END)), "loc_B4B")

    #C0020
    ChrTalk(
        0xFE,
        "ああ忙しい忙しい……\x02",
    )

    CloseMessageWindow()
    Jump("loc_CDC")

    label("loc_B4B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 1)), scpexpr(EXPR_END)), "loc_C55")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BE4")

    #C0021
    ChrTalk(
        0xFE,
        (
            "ふぅ……さっきのご夫妻の口論は\x01",
            "ようやく収まりましたよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0xFE,
        (
            "あわや血を見るかと言う所まで\x01",
            "発展した時はどうしようかと……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_C50")

    label("loc_BE4")


    #C0023
    ChrTalk(
        0xFE,
        (
            "とにかく、ようやくこれで\x01",
            "お掃除が始められます。\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0xFE,
        (
            "時間も押していますし\x01",
            "急いで進めてしまいましょう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C50")

    Jump("loc_CDC")

    label("loc_C55")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_CDC")

    #C0025
    ChrTalk(
        0xFE,
        (
            "こんな所で喧嘩なされては\x01",
            "掃除が出来なくて困ってしまいます。\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0xFE,
        (
            "かといって割って入れるような\x01",
            "雰囲気じゃありませんし……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CDC")

    TalkEnd(0xFE)
    Return()

    # Function_10_A32 end

    def Function_11_CE0(): pass

    label("Function_11_CE0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 5)), scpexpr(EXPR_END)), "loc_D64")

    #C0027
    ChrTalk(
        0xFE,
        (
            "突然ルバーチェ商会の方に\x01",
            "ここから出ないようにと\x01",
            "申されまして……\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0xFE,
        (
            "慌しいですが、\x01",
            "何かあったんでしょうか。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EC7")

    label("loc_D64")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_END)), "loc_DE9")

    #C0029
    ChrTalk(
        0xFE,
        (
            "オークションが終わるまでに\x01",
            "夜会の準備を\x01",
            "済まさなければなりません。\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0xFE,
        (
            "こちらの掃除も\x01",
            "早いところ済ませないと……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EC7")

    label("loc_DE9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 1)), scpexpr(EXPR_END)), "loc_E81")

    #C0031
    ChrTalk(
        0xFE,
        (
            "こちらは饗応の間……\x01",
            "要人の方々をもてなす為の場所です。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0xFE,
        (
            "本日は使用される予定はありません。\x01",
            "あまり立ち入らないようお願いします。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EC7")

    label("loc_E81")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_EC7")

    #C0033
    ChrTalk(
        0xFE,
        (
            "……ほとぼりが冷めるまで\x01",
            "掃除は諦めるしかありませんね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EC7")

    TalkEnd(0xFE)
    Return()

    # Function_11_CE0 end

    def Function_12_ECB(): pass

    label("Function_12_ECB")

    TalkBegin(0xFE)

    #C0034
    ChrTalk(
        0xFE,
        (
            "おや、お客様……\x01",
            "一体どうなさいましたか？\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_12_ECB end

    def Function_13_F01(): pass

    label("Function_13_F01")

    TalkBegin(0xFE)

    #C0035
    ChrTalk(
        0xFE,
        (
            "なんだか屋敷が\x01",
            "騒がしいみたいですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0xFE,
        "何かあったのでしょうか？\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_13_F01 end

    def Function_14_F51(): pass

    label("Function_14_F51")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_4B(0x8, 0xFF)
    OP_4B(0x9, 0xFF)
    OP_4B(0xA, 0xFF)
    OP_4B(0xB, 0xFF)
    SetChrSubChip(0x8, 0x1)
    SetChrFlags(0x8, 0x40)
    SetChrFlags(0x8, 0x4)
    SetChrFlags(0x8, 0x10)
    SetChrPos(0x8, -150, 100, -1150, 180)
    SetChrPos(0xA, 3750, 0, -3000, 90)
    SetChrPos(0x9, 5150, 0, -3600, 270)
    SetChrPos(0xB, 5150, 0, -2400, 270)
    SetChrPos(0x101, -600, 0, 4900, 180)
    SetChrPos(0xEF, 600, 0, 4900, 180)
    OP_68(0, 1200, 6000, 0)
    MoveCamera(45, 17, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18500, 0)
    FadeToBright(1000, 0)
    OP_0D()

    #N0037
    NpcTalk(
        0x9,
        "男性の声",
        (
            "だ、だからその……\x01",
            "誤解だと言っているだろう？\x02",
        )
    )

    CloseMessageWindow()

    #N0038
    NpcTalk(
        0x9,
        "男性の声",
        (
            "こちらの女性とは\x01",
            "ただの仕事上の付き合いでね……\x02",
        )
    )

    CloseMessageWindow()

    #N0039
    NpcTalk(
        0xA,
        "女性の声",
        "いいえ、誤魔化されませんから！\x02",
    )

    CloseMessageWindow()

    #N0040
    NpcTalk(
        0xA,
        "女性の声",
        (
            "様子がおかしいと思ったら\x01",
            "やっぱり他の女性と\x01",
            "一緒に来ていたなんて……！\x02",
        )
    )

    CloseMessageWindow()
    OP_68(2850, 1200, -2450, 3500)
    OP_6F(0x1)
    Sleep(300)
    OP_63(0x8, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_68(-550, 1200, -1000, 4000)
    SetChrSubChip(0x8, 0x0)

    def lambda_115F():
        OP_95(0xFE, -1700, 0, -1250, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_115F)
    Sleep(150)
    SetChrSubChip(0x8, 0x2)
    Sleep(350)

    def lambda_1183():
        OP_95(0xFE, -1600, 0, 0, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_1183)
    WaitChrThread(0x101, 1)

    def lambda_11A1():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_11A1)
    WaitChrThread(0xEF, 1)

    def lambda_11B2():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_11B2)
    WaitChrThread(0x101, 1)
    WaitChrThread(0xEF, 1)
    OP_6F(0x1)

    #C0041
    ChrTalk(
        0x8,
        (
            "#5702F#11Pやあ君たち。\x01",
            "無事に入れたようで何より。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x101,
        (
            "#5104F#6Pおかげさまでね。\x02\x03",

            "#5101F……それより、\x01",
            "これは何の騒ぎなんだ？\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x8,
        (
            "#5704F#11Pフフ……\x01",
            "ご覧の通り修羅場ってヤツさ。\x02",
        )
    )

    CloseMessageWindow()
    OP_68(4450, 1200, -3000, 2000)
    SetChrSubChip(0x8, 0x0)
    Sleep(150)
    SetChrSubChip(0x8, 0x1)
    OP_6F(0x1)

    #C0044
    ChrTalk(
        0x9,
        (
            "#11P──き、君だって\x01",
            "そんないかがわしい格好の少年と\x01",
            "一緒にいるじゃないか！\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x9,
        (
            "#11Pま、ま、まさか、\x01",
            "そういう関係なのか……！？\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0xA,
        (
            "#5Pその子は困っていた私を\x01",
            "手助けしてくれた恩人ですわ！\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0xA,
        (
            "#5Pクロスベルに来て右も左も分からず\x01",
            "困っていた所を助けてくれて……\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0xA,
        (
            "#5Pオークション会場まで案内してくれて\x01",
            "わざわざ付き添いまでしてくれた……\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0xA,
        (
            "#5Pあなたと、そちらの女性のような\x01",
            "いかがわしい関係ではありません！\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x9,
        "#11Pぐっ……\x02",
    )

    CloseMessageWindow()
    OP_68(1600, 1200, -2500, 1200)
    OP_6F(0x1)

    #C0051
    ChrTalk(
        0x8,
        (
            "#5709F#6Pフフ、僕としてはそれ以上の\x01",
            "関係になってもいいんだけどね。\x02\x03",

            "#5702F──ねえ、奥さん。\x02\x03",

            "そんな薄情なご主人なんか放って\x01",
            "このまま僕と火遊びしてみない？\x02\x03",

            "#5704F奥さんみたいな健気で可愛い女性、\x01",
            "キライじゃないしさ。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xA, 0x10E, 0x1F4)
    OP_63(0xA, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    #C0052
    ChrTalk(
        0xA,
        "#11Pワ、ワジ君、そんな……\x02",
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    OP_93(0x9, 0x10E, 0x1F4)
    Sleep(1000)
    OP_98(0x9, 0xFFFFFD12, 0x0, 0x0, 0x7D0, 0x0)

    #C0053
    ChrTalk(
        0x9,
        "#11Pき、君ぃ！\x02",
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x9,
        (
            "#11P人のワイフに色目を使うのは\x01",
            "止めてもらおうか！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x9, 500)

    #C0055
    ChrTalk(
        0xB,
        (
            "#5Pああもう……\x01",
            "これ以上付き合ってられないわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0xB,
        (
            "#5Pジェイムズさん。\x01",
            "火遊びをするんだったら\x01",
            "もう少し上手に立ち回ってよね。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1685():

        label("loc_1685")

        TurnDirection(0xFE, 0xB, 500)
        Yield()
        Jump("loc_1685")

    QueueWorkItem2(0x9, 1, lambda_1685)

    def lambda_1697():

        label("loc_1697")

        TurnDirection(0xFE, 0xB, 500)
        Yield()
        Jump("loc_1697")

    QueueWorkItem2(0xA, 1, lambda_1697)
    OP_93(0xB, 0x13B, 0x1F4)

    #C0057
    ChrTalk(
        0xB,
        (
            "#2Pまったく、とっとと\x01",
            "他の招待客を引っ掛けないと……\x02",
        )
    )

    CloseMessageWindow()
    OP_68(950, 1200, -1850, 3000)
    BeginChrThread(0xB, 3, 0, 15)
    Sleep(500)

    #C0058
    ChrTalk(
        0x9,
        "#11Pニ、ニキータ君……！\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0xB, 3)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    EndChrThread(0x9, 0x1)
    EndChrThread(0xA, 0x1)
    OP_6F(0x1)
    OP_63(0xA, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0xA, 0x9, 500)

    #C0059
    ChrTalk(
        0xA,
        (
            "#5Pや、やっぱり仕事上の\x01",
            "付き合いなんて嘘でしたのね！？\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0xA,
        "#5Pも、もう愛想が尽きました！\x02",
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0xA,
        (
            "#5Pわたくし、このまま\x01",
            "実家に帰らせてもらいます！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0xA, 500)

    #C0062
    ChrTalk(
        0x9,
        "#11Pエヴェリン、そんな……！\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0xEF, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_1888")

    #C0063
    ChrTalk(
        0x102,
        (
            "#5306F#6Pな、何だか\x01",
            "お邪魔しちゃ悪そうね……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_190D")

    label("loc_1888")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_18CA")

    #C0064
    ChrTalk(
        0x103,
        (
            "#5400F#6Pなるほど……\x01",
            "これが痴話ゲンカですか。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_190D")

    label("loc_18CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_190D")

    #C0065
    ChrTalk(
        0x104,
        (
            "#5609F#6Pま、夫婦ゲンカは\x01",
            "犬も喰わないってヤツだな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_190D")


    #C0066
    ChrTalk(
        0x101,
        (
            "#5112F#6P……えっと、俺たちは\x01",
            "これで失礼させてもらうよ。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 0x0)
    Sleep(100)
    SetChrSubChip(0x8, 0x2)
    Sleep(200)

    #C0067
    ChrTalk(
        0x8,
        (
            "#5704F#11Pフフ、それがいいね。\x02\x03",

            "#5702F──また後で。\x01",
            "宴を楽しんでくるといい。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, -2009, 0, -1560, 270)
    SetChrPos(0x9, 5350, 0, -3500, 315)
    SetChrPos(0xA, 4000, 0, -2150, 135)
    OP_4C(0x9, 0xFF)
    OP_4C(0xA, 0xFF)
    SetChrSubChip(0x8, 0x0)
    OP_49()
    OP_4C(0x8, 0xFF)
    SetScenarioFlags(0xA5, 5)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_14_F51 end

    def Function_15_1A07(): pass

    label("Function_15_1A07")


    def lambda_1A0C():
        OP_95(0xFE, 0, 0, 4600, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1A0C)
    WaitChrThread(0xB, 1)

    def lambda_1A2A():
        OP_95(0xFE, 0, 0, 6750, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1A2A)
    Sleep(250)

    def lambda_1A47():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_1A47)
    WaitChrThread(0xB, 1)
    WaitChrThread(0xB, 2)
    Return()

    # Function_15_1A07 end

    SaveToFile()

Try(main)
