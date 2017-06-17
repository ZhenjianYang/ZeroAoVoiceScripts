from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c015c.bin",                # FileName
        "c015c",                    # MapName
        "c015c",                    # Location
        0x0007,                     # MapIndex
        "ed7100",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 7, 0, 3, 0, 4],
    )

    BuildStringList((
        "c015c",                  # 0
        "ホイストフ",             # 1
        "ブラウン",               # 2
        "セルテオ",               # 3
        "ノンノ",                 # 4
        "ロバーツ主任",           # 5
        "イズリ夫人",             # 6
        "フェリック",             # 7
        "シンディ",               # 8
        "アンリ",                 # 9
        "ユンクス",               # 10
        "マリエッタ",             # 11
        "青年",                   # 12
        "娘",                     # 13
        "フロテ",                 # 14
        "見物客",                 # 15
        "見物客",                 # 16
        "見物客",                 # 17
        "見物客",                 # 18
        "見物客",                 # 19
        "見物客",                 # 20
        "見物客",                 # 21
        "見物客",                 # 22
        "見物客",                 # 23
        "ジロンド",               # 24
        "遊撃士ヴェンツェル",     # 25
    ))

    AddCharChip((
        "chr/ch25200.itc",                   # 00
        "chr/ch25000.itc",                   # 01
        "chr/ch25100.itc",                   # 02
        "chr/ch25600.itc",                   # 03
        "chr/ch34302.itc",                   # 04
        "chr/ch23402.itc",                   # 05
        "chr/ch21402.itc",                   # 06
        "chr/ch21202.itc",                   # 07
        "chr/ch20200.itc",                   # 08
        "chr/ch20802.itc",                   # 09
        "chr/ch21600.itc",                   # 0A
        "chr/ch21602.itc",                   # 0B
        "chr/ch24500.itc",                   # 0C
        "chr/ch24502.itc",                   # 0D
        "chr/ch21200.itc",                   # 0E
        "chr/ch21702.itc",                   # 0F
        "chr/ch22000.itc",                   # 10
        "chr/ch22100.itc",                   # 11
        "chr/ch22200.itc",                   # 12
        "chr/ch27600.itc",                   # 13
        "chr/ch21900.itc",                   # 14
        "chr/ch32300.itc",                   # 15
        "chr/ch24500.itc",                   # 16
        "chr/ch27300.itc",                   # 17
        "chr/ch29302.itc",                   # 18
        "chr/ch29300.itc",                   # 19
    ))

    DeclNpc(-509,    0,       12449,   180,  257,  0x0, 0,   0,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(-42889,  0,       5699,    0,    257,  0x0, 0,   1,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(-45700,  0,       5530,    0,    257,  0x0, 0,   2,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(-8880,   0,       3240,    45,   257,  0x0, 0,   3,   0,   0,   1,   0,   12,  255,  0)
    DeclNpc(-1750,   5000,    17659,   180,  341,  0x0, 0,   24,  0,   255, 255, 0,   32,  255,  0)
    DeclNpc(-949,    200,     2299,    273,  405,  0x0, 2,   15,  0,   255, 255, 0,   23,  255,  0)
    DeclNpc(-2190,   0,       -200,    0,    389,  0x0, 0,   16,  0,   0,   0,   0,   24,  255,  0)
    DeclNpc(-4670,   0,       4480,    45,   405,  0x0, 0,   17,  0,   0,   0,   0,   25,  255,  0)
    DeclNpc(-5730,   0,       1269,    270,  405,  0x0, 0,   18,  0,   0,   0,   0,   26,  255,  0)
    DeclNpc(-759,    0,       3640,    180,  405,  0x0, 0,   19,  0,   0,   0,   0,   27,  255,  0)
    DeclNpc(-3710,   0,       5789,    225,  405,  0x0, 0,   20,  0,   0,   0,   0,   28,  255,  0)
    DeclNpc(610,     5000,    9779,    180,  389,  0x0, 0,   21,  0,   0,   0,   0,   29,  255,  0)
    DeclNpc(-500,    5000,    9770,    180,  389,  0x0, 0,   22,  0,   0,   0,   0,   30,  255,  0)
    DeclNpc(-7449,   150,     8510,    270,  341,  0x0, 0,   4,   0,   255, 255, 0,   13,  255,  0)
    DeclNpc(6829,    150,     3569,    270,  469,  0x0, 0,   5,   0,   255, 255, 0,   14,  255,  0)
    DeclNpc(2009,    150,     3569,    90,   469,  0x0, 0,   6,   0,   255, 255, 0,   15,  255,  0)
    DeclNpc(1200,    0,       -1909,   135,  385,  0x0, 0,   14,  0,   0,   0,   0,   16,  255,  0)
    DeclNpc(3259,    150,     -1799,   180,  469,  0x0, 0,   7,   0,   255, 255, 0,   17,  255,  0)
    DeclNpc(5519,    150,     -3880,   270,  469,  0x0, 0,   9,   0,   255, 255, 0,   18,  255,  0)
    DeclNpc(2019,    0,       5309,    315,  385,  0x0, 0,   10,  0,   0,   0,   0,   19,  255,  0)
    DeclNpc(3259,    150,     -1799,   180,  469,  0x0, 0,   11,  0,   255, 255, 0,   20,  255,  0)
    DeclNpc(3289,    0,       6320,    315,  385,  0x0, 0,   12,  0,   0,   0,   0,   21,  255,  0)
    DeclNpc(5519,    150,     -3880,   270,  469,  0x0, 0,   13,  0,   255, 255, 0,   22,  255,  0)
    DeclNpc(60580,   -1000,   -8600,   270,  257,  0x0, 0,   8,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(56479,   -1000,   -8770,   90,   389,  0x0, 0,   23,  0,   0,   0,   0,   7,   255,  0)

    DeclActor(59140,   -1000,   -8880,   1500,    60580,   500,     -8600,   0x007E, 0,  5,  0x0000)
    DeclActor(-510,    0,       10640,   1000,    -510,    1500,    12450,   0x007E, 0,  8,  0x0000)

    ScpFunction((
        "Function_0_488",          # 00, 0
        "Function_1_540",          # 01, 1
        "Function_2_5DD",          # 02, 2
        "Function_3_667",          # 03, 3
        "Function_4_7A5",          # 04, 4
        "Function_5_7A6",          # 05, 5
        "Function_6_7AA",          # 06, 6
        "Function_7_1620",         # 07, 7
        "Function_8_1721",         # 08, 8
        "Function_9_1725",         # 09, 9
        "Function_10_1EE1",        # 0A, 10
        "Function_11_2385",        # 0B, 11
        "Function_12_2793",        # 0C, 12
        "Function_13_2919",        # 0D, 13
        "Function_14_2DD5",        # 0E, 14
        "Function_15_2FCE",        # 0F, 15
        "Function_16_3121",        # 10, 16
        "Function_17_3181",        # 11, 17
        "Function_18_31D3",        # 12, 18
        "Function_19_3347",        # 13, 19
        "Function_20_3390",        # 14, 20
        "Function_21_34F7",        # 15, 21
        "Function_22_353F",        # 16, 22
        "Function_23_36B4",        # 17, 23
        "Function_24_3822",        # 18, 24
        "Function_25_3938",        # 19, 25
        "Function_26_3A8E",        # 1A, 26
        "Function_27_3AF5",        # 1B, 27
        "Function_28_3BA2",        # 1C, 28
        "Function_29_3C72",        # 1D, 29
        "Function_30_3D67",        # 1E, 30
        "Function_31_3DE7",        # 1F, 31
        "Function_32_3FB9",        # 20, 32
        "Function_33_4C9F",        # 21, 33
    ))


    def Function_0_488(): pass

    label("Function_0_488")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_4C8"),
        (1, "loc_4D4"),
        (2, "loc_4E0"),
        (3, "loc_4EC"),
        (4, "loc_4F8"),
        (5, "loc_504"),
        (6, "loc_510"),
        (SWITCH_DEFAULT, "loc_51C"),
    )


    label("loc_4C8")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_528")

    label("loc_4D4")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_528")

    label("loc_4E0")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_528")

    label("loc_4EC")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_528")

    label("loc_4F8")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_528")

    label("loc_504")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_528")

    label("loc_510")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_528")

    label("loc_51C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_528")

    label("loc_528")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_53F")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_528")

    label("loc_53F")

    Return()

    # Function_0_488 end

    def Function_1_540(): pass

    label("Function_1_540")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5DC")
    OP_95(0xFE, -4260, 0, 8920, 2000, 0x0)
    OP_95(0xFE, 720, 0, 6870, 2000, 0x0)
    OP_95(0xFE, 780, 0, 1070, 2000, 0x0)
    OP_95(0xFE, 7240, 0, -2090, 2000, 0x0)
    OP_95(0xFE, 7240, 0, -6010, 2000, 0x0)
    OP_95(0xFE, 3280, 0, -8790, 2000, 0x0)
    OP_95(0xFE, -8880, 0, 3240, 2000, 0x0)
    Jump("Function_1_540")

    label("loc_5DC")

    Return()

    # Function_1_540 end

    def Function_2_5DD(): pass

    label("Function_2_5DD")


    def lambda_5E2():
        OP_A6(0xFE, 0x4, 0x0, 0x0, 0x258)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_5E2)

    label("loc_5F6")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_666")
    RunExpression(0x3, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x3C), scpexpr(EXPR_LEQ), scpexpr(EXPR_END)), "loc_63B")
    OP_94(0xFE, 0xFFFFF16E, 0x1C0C, 0x3B6, 0x20DA, 0x3E8)
    Sleep(100)
    Jump("loc_661")

    label("loc_63B")

    OP_93(0xFE, 0xE1, 0x3E8)
    OP_93(0xFE, 0x13B, 0x3E8)
    OP_93(0xFE, 0x2D, 0x3E8)
    OP_93(0xFE, 0x87, 0x3E8)
    OP_93(0xFE, 0xE1, 0x3E8)
    Sleep(500)

    label("loc_661")

    Jump("loc_5F6")

    label("loc_666")

    Return()

    # Function_2_5DD end

    def Function_3_667(): pass

    label("Function_3_667")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_6EF")
    SetChrPos(0xB, -6980, 0, 1280, 90)
    BeginChrThread(0xB, 0, 0, 0)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0xC, -210, 5000, 18380, 0)
    SetChrChipByIndex(0xC, 0x19)
    SetChrSubChip(0xC, 0x0)
    BeginChrThread(0xC, 0, 0, 0)
    ClearChrFlags(0xC, 0x40)
    SetChrFlags(0xC, 0x10)
    OP_63(0xC, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_7A4")

    label("loc_6EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_735")
    SetChrPos(0xA, -1460, 0, 7630, 180)
    BeginChrThread(0xA, 0, 0, 2)
    SetChrPos(0xB, 6810, 0, 9660, 270)
    BeginChrThread(0xB, 0, 0, 0)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1D, 0x80)
    Jump("loc_7A4")

    label("loc_735")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_752")
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x20, 0x80)
    Jump("loc_7A4")

    label("loc_752")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_END)), "loc_76F")
    SetChrFlags(0xB, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    Jump("loc_7A4")

    label("loc_76F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_78C")
    SetChrFlags(0xB, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    Jump("loc_7A4")

    label("loc_78C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_7A4")
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)

    label("loc_7A4")

    Return()

    # Function_3_667 end

    def Function_4_7A5(): pass

    label("Function_4_7A5")

    Return()

    # Function_4_7A5 end

    def Function_5_7A6(): pass

    label("Function_5_7A6")

    Call(0, 6)
    Return()

    # Function_5_7A6 end

    def Function_6_7AA(): pass

    label("Function_6_7AA")

    TalkBegin(0x1F)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_964")

    #C0001
    ChrTalk(
        0x1F,
        (
            "へい、らっしゃい。\x01",
            "と言いてえところだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x1F,
        (
            "坊主ら、クロスベルじゃ\x01",
            "許可証がなきゃ武器は売れねえんだぜ。\x01",
            "冷やかしなら帰るんだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0x101,
        (
            "#0000Fあ、いや俺たちは\x01",
            "クロスベル警察の者ですけど……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1F, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0004
    ChrTalk(
        0x1F,
        "お前らみたいなのが警察……？\x02",
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x1F,
        (
            "そうか、セルゲイの奴が\x01",
            "言っていた例の……\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x1F,
        (
            "フン、分かったぜ。\x01",
            "好きに見ていけよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x1F,
        (
            "武器を買うときは\x01",
            "俺に捜査手帳を見せな。\x01",
            "それが許可証代わりだからよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x4C, 2)
    SetScenarioFlags(0xAF, 2)

    label("loc_964")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_96E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_161C")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "話をする\x01",          # 0
            "買い物をする\x01",      # 1
            "やめる\x01",            # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9CC")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_9CC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A3C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_9EB")
    OP_AF(0x5)
    Jump("loc_A2D")

    label("loc_9EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_9FB")
    OP_AF(0x4)
    Jump("loc_A2D")

    label("loc_9FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_A0B")
    OP_AF(0x3)
    Jump("loc_A2D")

    label("loc_A0B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_A1B")
    OP_AF(0x2)
    Jump("loc_A2D")

    label("loc_A1B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_A2B")
    OP_AF(0x1)
    Jump("loc_A2D")

    label("loc_A2B")

    OP_AF(0x0)

    label("loc_A2D")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1617")

    label("loc_A3C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A50")
    Jump("loc_1617")

    label("loc_A50")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1617")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_B2A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AE4")

    #C0008
    ChrTalk(
        0x1F,
        (
            "やれやれ、バカ騒ぎも\x01",
            "今日で最後だな。\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x1F,
        (
            "へっ……ま、お前らも\x01",
            "騒ぎたいなら今のうちにな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_B25")

    label("loc_AE4")


    #C0010
    ChrTalk(
        0x1F,
        (
            "今日までは無礼講みてえなもんだ。\x01",
            "騒ぎたいなら今のうちにな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B25")

    Jump("loc_1617")

    label("loc_B2A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 4)), scpexpr(EXPR_END)), "loc_BA9")

    #C0011
    ChrTalk(
        0x1F,
        (
            "よう、まだ迷子の子を\x01",
            "探してんのかい？\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x1F,
        (
            "この街は広いからなぁ……\x01",
            "まあ辛抱強く聞き込むしか\x01",
            "ねえだろうな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1617")

    label("loc_BA9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_EF2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAC, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E74")

    #C0013
    ChrTalk(
        0x101,
        (
            "#0001F（うん、この人なら\x01",
            "  何か知っているかもしれないな……）\x02",
        )
    )

    CloseMessageWindow()

    #A0014
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

    #C0015
    ChrTalk(
        0x1F,
        (
            "ほう、写真を使って\x01",
            "聞き込みか……\x01",
            "今日は警察らしい事をしているな。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x101,
        (
            "#0012Fはは、まあ……\x02\x03",

            "#0001Fそれで心当たりはありませんか？\x01",
            "知人のお子さんなんですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x1F,
        (
            "俺はパレードも見てないもんでな。\x01",
            "店に来たんでなきゃ判らねえぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x1F,
        (
            "だがまあ、パレードに\x01",
            "くっ付いて行っちまったんなら\x01",
            "東通りじゃねえか？\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x1F,
        (
            "パレードの道順は\x01",
            "あっちのはずだぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x101,
        (
            "#0008Fそうですね……\x01",
            "（ランディの連絡だと\x01",
            "  東通りはシロだったらしいけど……）\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x160,
        (
            "#3300F……それで、お兄さんは\x01",
            "どうするのかしら？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xAC, 3)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x0, 0)
    Call(0, 31)

    #C0022
    ChrTalk(
        0x160,
        (
            "#3304Fふふ……慎重なのね。\x01",
            "面白いお兄さん。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EED")

    label("loc_E74")


    #C0023
    ChrTalk(
        0x1F,
        (
            "パレードの道順は\x01",
            "ここから東通りだったはずだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x1F,
        (
            "パレードにくっ付いて\x01",
            "行っちまったんなら、\x01",
            "あっちの方じゃねえか？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EED")

    Jump("loc_1617")

    label("loc_EF2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_FD8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F97")

    #C0025
    ChrTalk(
        0x1F,
        (
            "導力車か……パレードも\x01",
            "様変わりしたもんだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x1F,
        (
            "ま、警察連中が大変なのは\x01",
            "昔と変わらねえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x1F,
        "今ごろ新米警官はバテバテだろうよ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_FD3")

    label("loc_F97")


    #C0028
    ChrTalk(
        0x1F,
        (
            "時代が変わっても\x01",
            "警察連中が大変なのは\x01",
            "変わらねえなあ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FD3")

    Jump("loc_1617")

    label("loc_FD8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_10B2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_105C")

    #C0029
    ChrTalk(
        0x1F,
        "今日はパレードがあるな。\x02",
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x1F,
        (
            "やれやれ……\x01",
            "制服連中もご苦労さんなこった。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x1F,
        "俺は同情しちまうぜ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_10AD")

    label("loc_105C")


    #C0032
    ChrTalk(
        0x1F,
        (
            "お前らも暇なら\x01",
            "行政区の広場に行ってみな。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x1F,
        "制服連中が大わらわだろうよ。\x02",
    )

    CloseMessageWindow()

    label("loc_10AD")

    Jump("loc_1617")

    label("loc_10B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_END)), "loc_13AD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1330")

    #C0034
    ChrTalk(
        0x1F,
        (
            "セルゲイのやつと\x01",
            "１杯飲もうかと思ったんだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x1F,
        "あいつ、今日は会議みてえだな。\x02",
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x1F,
        (
            "ふーむ、また面倒事を\x01",
            "押し付けられてなきゃいいんだが……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0037
    ChrTalk(
        0x101,
        "#0005Fどういうことですか……？\x02",
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x1F,
        (
            "ああ、あいつは\x01",
            "昔っからはみ出しモンだからな。\x01",
            "何かと厄介事を背負い込むんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x1F,
        (
            "お前ら『特務支援課』の\x01",
            "お茶にごしとかよ。\x02",
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

    #C0040
    ChrTalk(
        0x103,
        "#0203Fそうでしたね……\x02",
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x1F,
        (
            "ま、支援課はあいつが\x01",
            "自分でブッ建てた部署だ。\x01",
            "自業自得だがな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_13A8")

    label("loc_1330")


    #C0042
    ChrTalk(
        0x1F,
        (
            "まあ今日の会議は\x01",
            "明日のパレードの警備体制絡みだろ。\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x1F,
        (
            "支援課も金星を挙げてることだし\x01",
            "そう心配することもねえか。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13A8")

    Jump("loc_1617")

    label("loc_13AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_149B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_144E")

    #C0044
    ChrTalk(
        0x1F,
        (
            "そういや、アリオスの奴が\x01",
            "帰国したらしいな。\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x1F,
        "今年は人出がハンパじゃねえ。\x02",
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x1F,
        (
            "やっこさんも戻らざるを\x01",
            "得なかったみたいだな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1496")

    label("loc_144E")


    #C0047
    ChrTalk(
        0x1F,
        "アリオスも帰国しているそうだな。\x02",
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x1F,
        "今年の人出じゃ仕方ねえだろ。\x02",
    )

    CloseMessageWindow()

    label("loc_1496")

    Jump("loc_1617")

    label("loc_149B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1617")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAF, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15B9")

    #C0049
    ChrTalk(
        0x1F,
        (
            "……らっしゃい。\x01",
            "ウチは武器屋だぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x1F,
        (
            "って、なんだお前らか。\x01",
            "浮かれた観光客かと思ったぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x1F,
        (
            "お前らも、めでたい日に\x01",
            "しけた武器屋なんぞに入るんじゃねえよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x1F,
        (
            "ほれ、用が済んだら\x01",
            "帰った帰った。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x101,
        "#0000Fははは……\x02",
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x103,
        "#0200Fとりつく島もないですね。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1617")

    label("loc_15B9")


    #C0055
    ChrTalk(
        0x1F,
        (
            "ウチは武器屋だぜ。\x01",
            "めでたい日に入るんじゃねえよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x1F,
        (
            "ほれ、用が済んだら\x01",
            "帰った帰った。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1617")

    Jump("loc_96E")

    label("loc_161C")

    TalkEnd(0x1F)
    Return()

    # Function_6_7AA end

    def Function_7_1620(): pass

    label("Function_7_1620")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_171D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16D4")

    #C0057
    ChrTalk(
        0xFE,
        (
            "仕事と警備で支部の遊撃士が\x01",
            "出払ってしまってな。\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0xFE,
        (
            "緊急時に備えるために、\x01",
            "俺はクロスベル市で待機だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0xFE,
        "今のうちに剣を新調しておくとしよう。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_171D")

    label("loc_16D4")


    #C0060
    ChrTalk(
        0xFE,
        (
            "相棒のスコットも今日は別行動……\x01",
            "まぁ、奴なら１人でも心配はないか。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_171D")

    TalkEnd(0xFE)
    Return()

    # Function_7_1620 end

    def Function_8_1721(): pass

    label("Function_8_1721")

    Call(0, 9)
    Return()

    # Function_8_1721 end

    def Function_9_1725(): pass

    label("Function_9_1725")

    TalkBegin(0x8)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1732")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1EDD")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "話をする\x01",          # 0
            "買い物をする\x01",      # 1
            "やめる\x01",            # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1790")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_1790")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17B0")
    OP_AF(0x8)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1ED8")

    label("loc_17B0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_17C4")
    Jump("loc_1ED8")

    label("loc_17C4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1ED8")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_183C")

    #C0061
    ChrTalk(
        0x8,
        "これはとんだ大家族ですな。\x02",
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x8,
        (
            "フフ、本日は私も\x01",
            "厨房を手伝うとしましょう。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1ED8")

    label("loc_183C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 4)), scpexpr(EXPR_END)), "loc_18D2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_189C")

    #C0063
    ChrTalk(
        0x8,
        "ゴホン……\x02",
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x8,
        (
            "スタッフの一芸、\x01",
            "楽しんで頂けましたでしょうか。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_18CD")

    label("loc_189C")


    #C0065
    ChrTalk(
        0x8,
        (
            "セルテオ……\x01",
            "もっとマシな芸はないのかね……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18CD")

    Jump("loc_1ED8")

    label("loc_18D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_1AF6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAC, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A28")

    #C0066
    ChrTalk(
        0x101,
        (
            "#0001F（うん、この人なら\x01",
            "  何か知っているかもしれないな……）\x02",
        )
    )

    CloseMessageWindow()

    #A0067
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

    #C0068
    ChrTalk(
        0x8,
        (
            "ほう、迷子ですか。\x01",
            "それはお気の毒に……\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x8,
        (
            "しかし心当たりはありませんね。\x01",
            "当店にはいらっしゃってないかと。\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x101,
        (
            "#0000Fそうですか……\x01",
            "ありがとうございました。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xAC, 0)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 31)
    Jump("loc_1AF1")

    label("loc_1A28")


    #C0071
    ChrTalk(
        0x8,
        (
            "ふむ、写真でお伺いする限り\x01",
            "中々美人なお子さんですな。\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0x8,
        (
            "どことなくお嬢さんと\x01",
            "似てらっしゃるようだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0x101,
        (
            "#0005F（言われてみれば……\x01",
            "  ちょっと似てるかな？）\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x160,
        "#3308F………………………………\x02",
    )

    CloseMessageWindow()

    label("loc_1AF1")

    Jump("loc_1ED8")

    label("loc_1AF6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_1B8C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B56")

    #C0075
    ChrTalk(
        0x8,
        "ゴホン……\x02",
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x8,
        (
            "スタッフの一芸、\x01",
            "楽しんで頂けましたでしょうか。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1B87")

    label("loc_1B56")


    #C0077
    ChrTalk(
        0x8,
        (
            "セルテオ……\x01",
            "もっとマシな芸はないのかね……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B87")

    Jump("loc_1ED8")

    label("loc_1B8C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_1C8C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C36")

    #C0078
    ChrTalk(
        0x8,
        (
            "当店では午後より\x01",
            "スタッフによるパフォーマンスを\x01",
            "ご披露いたします。\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0x8,
        (
            "丁度パレードの後の予定ですから、\x01",
            "宜しければ立ち寄られてください。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1C87")

    label("loc_1C36")


    #C0080
    ChrTalk(
        0x8,
        (
            "……セルテオの\x01",
            "突然のアイデアなのですが。\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0x8,
        "うまく行くのでしょうかねえ。\x02",
    )

    CloseMessageWindow()

    label("loc_1C87")

    Jump("loc_1ED8")

    label("loc_1C8C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_END)), "loc_1D1F")

    #C0082
    ChrTalk(
        0x8,
        (
            "ただいま記念祭限定メニュー、\x01",
            "スペシャルランチを\x01",
            "ご用意しております。\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x8,
        (
            "数に限りがございますので\x01",
            "お早めにご注文くださいませ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1ED8")

    label("loc_1D1F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1E05")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1DD9")

    #C0084
    ChrTalk(
        0x8,
        (
            "大入りなのはよいのですが……\x01",
            "朝から一部の食材が\x01",
            "届いていないのですよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0x8,
        (
            "記念祭の影響でどこの\x01",
            "配達業者も遅れているようです。\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x8,
        "はて、困ったものだ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1E00")

    label("loc_1DD9")


    #C0087
    ChrTalk(
        0x8,
        (
            "何か手を考えねば\x01",
            "なりませんね……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E00")

    Jump("loc_1ED8")

    label("loc_1E05")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1ED8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E76")

    #C0088
    ChrTalk(
        0x8,
        (
            "いらっしゃいませ。\x01",
            "４名様でしょうか？\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0x8,
        (
            "空いているお席へ\x01",
            "お座りくださいませ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1ED8")

    label("loc_1E76")


    #C0090
    ChrTalk(
        0x8,
        (
            "まだ２日目だというのに……\x01",
            "今年はお客様が多いですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x8,
        (
            "当店としましても\x01",
            "気を遣いますよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1ED8")

    Jump("loc_1732")

    label("loc_1EDD")

    TalkEnd(0x8)
    Return()

    # Function_9_1725 end

    def Function_10_1EE1(): pass

    label("Function_10_1EE1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_1FEA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F83")

    #C0092
    ChrTalk(
        0xFE,
        (
            "今日は俺たちも\x01",
            "慰労会をやるつもりなんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0xFE,
        (
            "店が終わった後\x01",
            "店員だけで集まって飲むのさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0xFE,
        "今年は色々と忙しかったからな。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1FE5")

    label("loc_1F83")


    #C0095
    ChrTalk(
        0xFE,
        (
            "今日は俺たちも\x01",
            "慰労会をやるつもりなんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0xFE,
        (
            "セルテオは……\x01",
            "飲まない方がよさそうだけどな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1FE5")

    Jump("loc_2381")

    label("loc_1FEA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_202E")

    #C0097
    ChrTalk(
        0xFE,
        "何だか店の方が騒がしいな。\x02",
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0xFE,
        "何かあったのか？\x02",
    )

    CloseMessageWindow()
    Jump("loc_2381")

    label("loc_202E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_2091")

    #C0099
    ChrTalk(
        0xFE,
        (
            "俺も子供の頃は\x01",
            "パレードが楽しみだったなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0xFE,
        "パレードはいいぞ、パレードは。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2381")

    label("loc_2091")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_END)), "loc_2168")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_210A")

    #C0101
    ChrTalk(
        0xFE,
        (
            "ほい、スペシャルランチ\x01",
            "一丁あがり。\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0xFE,
        (
            "やっぱり記念祭は客が多いな。\x01",
            "さすがに忙しいぜ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2163")

    label("loc_210A")


    #C0103
    ChrTalk(
        0xFE,
        "今年はたいした盛り上がりようだな。\x02",
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0xFE,
        (
            "港湾区の方じゃ\x01",
            "ステージもやってるんだって？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2163")

    Jump("loc_2381")

    label("loc_2168")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_22AC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2262")

    #C0105
    ChrTalk(
        0xFE,
        (
            "食材の配達が遅れていてな、\x01",
            "ついにＡからＣランチまで\x01",
            "全滅しちまったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0xFE,
        (
            "というわけで、\x01",
            "全部のランチメニューを混ぜた\x01",
            "記念祭限定メニューを出すことにした。\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0xFE,
        (
            "名づけてスペシャルランチ。\x01",
            "……中々うまいアイデアだろ？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_22A7")

    label("loc_2262")


    #C0108
    ChrTalk(
        0xFE,
        (
            "今日はスペシャルランチを\x01",
            "出している。\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0xFE,
        "ご注文はお早めにな。\x02",
    )

    CloseMessageWindow()

    label("loc_22A7")

    Jump("loc_2381")

    label("loc_22AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_2381")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2340")

    #C0110
    ChrTalk(
        0xFE,
        (
            "記念祭の影響で\x01",
            "食材の配達が遅れていてな、\x01",
            "Ａランチは今日も品切れだぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0xFE,
        (
            "参ったな。\x01",
            "後でホイストフに相談するか。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2381")

    label("loc_2340")


    #C0112
    ChrTalk(
        0xFE,
        (
            "こういう時は慌てても仕方ない。\x01",
            "店長の判断に任せるとしよう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2381")

    TalkEnd(0xFE)
    Return()

    # Function_10_1EE1 end

    def Function_11_2385(): pass

    label("Function_11_2385")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_245D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2421")

    #C0113
    ChrTalk(
        0xFE,
        (
            "いてて……\x01",
            "昨日は飲みすぎちまったらしい。\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0xFE,
        (
            "頭がガンガンして\x01",
            "何も覚えてないんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0xFE,
        "……俺、なんかやってたのかな。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_2458")

    label("loc_2421")


    #C0116
    ChrTalk(
        0xFE,
        (
            "ううっ、頭いてえ……\x01",
            "俺、昨日は何やってたんだろ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2458")

    Jump("loc_278F")

    label("loc_245D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_24F0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_24A6")

    #C0117
    ChrTalk(
        0xFE,
        "うい～っく……\x02",
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0xFE,
        "４番、歌いま～すぅ！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_24EB")

    label("loc_24A6")


    #C0119
    ChrTalk(
        0xFE,
        "うひゃひゃひゃ……！\x02",
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0xFE,
        (
            "ほれきょうは\x01",
            "ガンガン飲んじゃうろ～？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_24EB")

    Jump("loc_278F")

    label("loc_24F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_2583")

    #C0121
    ChrTalk(
        0xFE,
        (
            "フ……実はオレ、\x01",
            "歌が得意なんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0xFE,
        (
            "今日はお客様に\x01",
            "オレの美声を聞かせてやるぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0xFE,
        (
            "女の子がたくさん\x01",
            "来てくれるといいなぁ♪\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_278F")

    label("loc_2583")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_END)), "loc_2669")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_260B")

    #C0124
    ChrTalk(
        0xFE,
        (
            "教えてもらったスペシャルランチ、\x01",
            "やってみたら意外と作れるもんだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0xFE,
        "へへっ……自分の才能が怖いぜ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_2664")

    label("loc_260B")


    #C0126
    ChrTalk(
        0xFE,
        (
            "待ってな、お客さん。\x01",
            "今にオレのスペシャルなランチを……\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0xFE,
        "……熱っ！　油はねた！\x02",
    )

    CloseMessageWindow()

    label("loc_2664")

    Jump("loc_278F")

    label("loc_2669")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_2722")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_26F9")

    #C0128
    ChrTalk(
        0xFE,
        (
            "ブラウンさんから\x01",
            "突然新メニューを\x01",
            "作るように言われたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0xFE,
        (
            "……口頭で聞いただけで\x01",
            "急にそんなの作れるかよ！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_271D")

    label("loc_26F9")


    #C0130
    ChrTalk(
        0xFE,
        "とほほ、俺も遊びにいきてえ～！\x02",
    )

    CloseMessageWindow()

    label("loc_271D")

    Jump("loc_278F")

    label("loc_2722")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_278F")

    #C0131
    ChrTalk(
        0xFE,
        (
            "右手で野菜刻んで、\x01",
            "左手で鍋を見て……\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0xFE,
        (
            "うおおお、追いつかねー！\x01",
            "同時に５品も作れっかよっ！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_278F")

    TalkEnd(0xFE)
    Return()

    # Function_11_2385 end

    def Function_12_2793(): pass

    label("Function_12_2793")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_27FE")

    #C0133
    ChrTalk(
        0xFE,
        (
            "今日は大家族の\x01",
            "お客さんが来ているんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0xFE,
        (
            "こっちも張り切らないと\x01",
            "いけませんね！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2915")

    label("loc_27FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_2845")

    #C0135
    ChrTalk(
        0xFE,
        (
            "セルテオさん、もしかして\x01",
            "お酒ダメだったのかしら……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2915")

    label("loc_2845")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_28A6")

    #C0136
    ChrTalk(
        0xFE,
        "今日はパレードがあるそうですね。\x02",
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0xFE,
        (
            "広場の方が騒がしいのは\x01",
            "そのせいかしら。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2915")

    label("loc_28A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_2915")

    #C0138
    ChrTalk(
        0xFE,
        "いらっしゃいませー！\x02",
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0xFE,
        (
            "今Ａランチは\x01",
            "切らしちゃってるんです。\x01",
            "ランチはＢかＣでお願いしま～す！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2915")

    TalkEnd(0xFE)
    Return()

    # Function_12_2793 end

    def Function_13_2919(): pass

    label("Function_13_2919")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_29AD")
    Jump("loc_29F7")

    label("loc_29AD")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_29CD")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_29F7")

    label("loc_29CD")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_29ED")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_29F7")

    label("loc_29ED")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_29F7")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_2ACC")

    #C0140
    ChrTalk(
        0xFE,
        "今日が最終日ね……\x02",
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0xFE,
        "………………………………\x02",
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0xFE,
        (
            "市長の閉会宣言くらいは\x01",
            "私も聞いてあげてもいいわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0xFE,
        (
            "バカ騒ぎの終わり……\x01",
            "趣きがあって悪くないもの。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DCD")

    label("loc_2ACC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_2B45")

    #C0144
    ChrTalk(
        0xFE,
        "ぶほっ……！？\x02",
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0xFE,
        (
            "……あのコック、\x01",
            "ヘンな芸を聞かせないでよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0xFE,
        "コーヒーこぼしちゃったじゃない。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2DCD")

    label("loc_2B45")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_2BF4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2BAF")

    #C0147
    ChrTalk(
        0xFE,
        (
            "パレード、パレードって\x01",
            "みんな煩いのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0xFE,
        "これだから観光客は嫌いだわ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_2BEF")

    label("loc_2BAF")


    #C0149
    ChrTalk(
        0xFE,
        (
            "静かに読書を\x01",
            "楽しみたい客がいることも\x01",
            "分からないのかしら。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2BEF")

    Jump("loc_2DCD")

    label("loc_2BF4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_END)), "loc_2C7F")

    #C0150
    ChrTalk(
        0xFE,
        "今日も浮かれた客ばかりね……\x02",
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0xFE,
        "フン、何がスペシャルランチよ。\x02",
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0xFE,
        (
            "私はいつも通りコーヒー一杯で\x01",
            "粘ってやるんだから。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DCD")

    label("loc_2C7F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_2D24")

    #C0153
    ChrTalk(
        0xFE,
        "ずずーっ……\x02",
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0xFE,
        (
            "色んな店で、今の時期しか\x01",
            "買えない商品を扱ってるみたい。\x02",
        )
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0xFE,
        (
            "まったく……\x01",
            "ずっと販売してなさいよ。\x01",
            "買い逃したら悔しいじゃない。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DCD")

    label("loc_2D24")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_2DCD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D9A")

    #C0156
    ChrTalk(
        0xFE,
        "ずずーっ……\x02",
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0xFE,
        "みんな浮かれちゃって……\x02",
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0xFE,
        (
            "これだから\x01",
            "クロスベル人は嫌いなのよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_2DCD")

    label("loc_2D9A")


    #C0159
    ChrTalk(
        0xFE,
        (
            "フン、私はお祭りなんかには\x01",
            "染まらないわよー。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2DCD")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_13_2919 end

    def Function_14_2DD5(): pass

    label("Function_14_2DD5")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2E69")
    Jump("loc_2EB3")

    label("loc_2E69")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2E89")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2EB3")

    label("loc_2E89")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2EA9")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2EB3")

    label("loc_2EA9")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2EB3")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F85")

    #C0160
    ChrTalk(
        0xFE,
        (
            "ふむ、息子も\x01",
            "喜んでいるようだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0xFE,
        (
            "僕らは大陸東方の出身でね。\x01",
            "遠路だからどうかと思ったが……\x02",
        )
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0xFE,
        (
            "少々背伸びをしてでも\x01",
            "遊びに来た甲斐があったよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_2FC6")

    label("loc_2F85")


    #C0163
    ChrTalk(
        0xFE,
        (
            "遠路はるばるやってきたんだ。\x01",
            "じっくり楽しませてもらおうか。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2FC6")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_14_2DD5 end

    def Function_15_2FCE(): pass

    label("Function_15_2FCE")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3062")
    Jump("loc_30AC")

    label("loc_3062")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3082")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_30AC")

    label("loc_3082")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_30A2")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_30AC")

    label("loc_30A2")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_30AC")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    SetChrSubChip(0xFE, 0x0)

    #C0164
    ChrTalk(
        0xFE,
        "ねー、お子様ランチまだ～？\x02",
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0xFE,
        "早く食べて遊びにいきたいよ～。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_15_2FCE end

    def Function_16_3121(): pass

    label("Function_16_3121")

    TalkBegin(0xFE)

    #C0166
    ChrTalk(
        0xFE,
        (
            "明日は田舎の父さんが\x01",
            "会いに来てくれるんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0xFE,
        "いい席を予約しておかなくちゃな。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_16_3121 end

    def Function_17_3181(): pass

    label("Function_17_3181")

    TalkBegin(0xFE)

    #C0168
    ChrTalk(
        0xFE,
        "どう父さん、楽しんでる？\x02",
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0xFE,
        (
            "やっぱり予約しておいて\x01",
            "良かったでしょ。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_17_3181 end

    def Function_18_31D3(): pass

    label("Function_18_31D3")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3267")
    Jump("loc_32B1")

    label("loc_3267")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3287")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_32B1")

    label("loc_3287")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_32A7")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_32B1")

    label("loc_32A7")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_32B1")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    SetChrSubChip(0xFE, 0x0)

    #C0170
    ChrTalk(
        0xFE,
        "うむ、中々の味じゃ。\x02",
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0xFE,
        (
            "元料理人のわしでも\x01",
            "文句のつけようが無い。\x02",
        )
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0xFE,
        "安心して味わえるわい。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_18_31D3 end

    def Function_19_3347(): pass

    label("Function_19_3347")

    TalkBegin(0xFE)
    OP_93(0xFE, 0x13B, 0x0)

    #C0173
    ChrTalk(
        0xFE,
        "ひ、酷い芸だな！\x02",
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0xFE,
        (
            "誰の物まねだか\x01",
            "全然分からんぞ！\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_19_3347 end

    def Function_20_3390(): pass

    label("Function_20_3390")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3424")
    Jump("loc_346E")

    label("loc_3424")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3444")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_346E")

    label("loc_3444")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3464")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_346E")

    label("loc_3464")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_346E")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0175
    ChrTalk(
        0xFE,
        (
            "パレードと言えば\x01",
            "やはり中央広場だのう。\x02",
        )
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0xFE,
        (
            "早めに出向いて\x01",
            "良い場所を選んでおかねば。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_20_3390 end

    def Function_21_34F7(): pass

    label("Function_21_34F7")

    TalkBegin(0xFE)
    OP_93(0xFE, 0x13B, 0x0)

    #C0177
    ChrTalk(
        0xFE,
        "あはは、でも面白～い！\x02",
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0xFE,
        "もっとやっちゃって～っ！\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_21_34F7 end

    def Function_22_353F(): pass

    label("Function_22_353F")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_35D3")
    Jump("loc_361D")

    label("loc_35D3")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_35F3")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_361D")

    label("loc_35F3")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3613")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_361D")

    label("loc_3613")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_361D")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    SetChrSubChip(0xFE, 0x0)

    #C0179
    ChrTalk(
        0xFE,
        (
            "もぐもぐ……\x01",
            "パレードまで時間あるっしょ。\x02",
        )
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0xFE,
        (
            "百貨店見に行かない？\x01",
            "セールとかやってそうじゃん。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_22_353F end

    def Function_23_36B4(): pass

    label("Function_23_36B4")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3748")
    Jump("loc_3792")

    label("loc_3748")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3768")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3792")

    label("loc_3768")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3788")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3792")

    label("loc_3788")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3792")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    SetChrSubChip(0xD, 0x2)
    OP_4B(0x11, 0xFF)

    #C0181
    ChrTalk(
        0xD,
        "記念祭は家族で楽しむものです。\x02",
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0xD,
        (
            "少なくとも我が家では\x01",
            "異論は認めませんよ。\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x11, 0xFF)
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    SetChrSubChip(0xD, 0x2)
    Return()

    # Function_23_36B4 end

    def Function_24_3822(): pass

    label("Function_24_3822")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_38B3")

    #C0183
    ChrTalk(
        0xE,
        (
            "俺も友達と遊ぶ約束してたんだが\x01",
            "今日は家族でパーっとやるかな。\x02",
        )
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0xE,
        (
            "親父とお袋が並んでるのを　\x01",
            "見るのも久し振りだもんなー。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3934")

    label("loc_38B3")


    #C0185
    ChrTalk(
        0xE,
        (
            "うちは誰も\x01",
            "婆ちゃんには逆らえないんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0xE,
        "へへ、まあ仕方ないよな。\x02",
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0xE,
        (
            "今日で最終日なんだし\x01",
            "家族でパーっとやろうぜ！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)

    label("loc_3934")

    TalkEnd(0xFE)
    Return()

    # Function_24_3822 end

    def Function_25_3938(): pass

    label("Function_25_3938")

    TalkBegin(0xFE)
    OP_4B(0x12, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_39C5")
    TurnDirection(0xF, 0x0, 0)

    #C0188
    ChrTalk(
        0xF,
        "ママに会うのホント久しぶり。\x02",
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0xF,
        (
            "久しぶりすぎて\x01",
            "今日はビックリしちゃった～。\x01",
            "さすがお婆ちゃんだね！\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xF, 0x2D, 0x0)
    Jump("loc_3A86")

    label("loc_39C5")


    #C0190
    ChrTalk(
        0xF,
        (
            "……ママ！？\x01",
            "いつ帰国してたの！？\x02",
        )
    )

    CloseMessageWindow()

    #C0191
    ChrTalk(
        0xF,
        (
            "仕事は？\x01",
            "ホントに大丈夫なの～？\x02",
        )
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0x12,
        (
            "お義母さんに呼ばれちゃ\x01",
            "仕方ないじゃな～い。\x02",
        )
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0x12,
        (
            "それに子供達の顔も見たかったし。\x01",
            "つい抜け出してきちゃった㈱\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)

    label("loc_3A86")

    OP_4C(0x12, 0xFF)
    TalkEnd(0xFE)
    Return()

    # Function_25_3938 end

    def Function_26_3A8E(): pass

    label("Function_26_3A8E")

    TalkBegin(0xFE)
    OP_4B(0xB, 0xFF)

    #C0194
    ChrTalk(
        0x10,
        (
            "あの、椅子の追加\x01",
            "お願いできますか？\x02",
        )
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0xB,
        (
            "かしこまりました。\x01",
            "すぐにお持ちしますね。\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xB, 0xFF)
    TalkEnd(0xFE)
    Return()

    # Function_26_3A8E end

    def Function_27_3AF5(): pass

    label("Function_27_3AF5")

    TalkBegin(0xFE)

    #C0196
    ChrTalk(
        0x11,
        (
            "母さん、まだ仕事があるんですよ。\x01",
            "勝手なまねは困りますね……\x02",
        )
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0xD,
        "どうやら中休みが取れたようですね。\x02",
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0xD,
        (
            "ほら、突っ立っていないで座りなさい。\x01",
            "食事を始めますよ。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_27_3AF5 end

    def Function_28_3BA2(): pass

    label("Function_28_3BA2")

    TalkBegin(0xFE)
    OP_4B(0xF, 0xFF)

    #C0199
    ChrTalk(
        0xF,
        (
            "……ママ！？\x01",
            "いつ帰国してたの！？\x02",
        )
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0xF,
        (
            "仕事は？\x01",
            "ホントに大丈夫なの～？\x02",
        )
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0x12,
        (
            "お義母さんに呼ばれちゃ\x01",
            "仕方ないじゃな～い。\x02",
        )
    )

    CloseMessageWindow()

    #C0202
    ChrTalk(
        0x12,
        (
            "それに子供達の顔も見たかったし。\x01",
            "つい抜け出してきちゃった㈱\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    OP_4C(0xF, 0xFF)
    TalkEnd(0xFE)
    Return()

    # Function_28_3BA2 end

    def Function_29_3C72(): pass

    label("Function_29_3C72")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_3CD5")

    #C0203
    ChrTalk(
        0x13,
        (
            "あいつんち\x01",
            "ばーちゃんが強いんだよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0204
    ChrTalk(
        0x13,
        (
            "ちぇっ、今日は\x01",
            "一緒に遊べないぜ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3D63")

    label("loc_3CD5")


    #C0205
    ChrTalk(
        0x13,
        (
            "ちぇっ、ダチの俺たちを\x01",
            "差し置いて家族で食事かよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0206
    ChrTalk(
        0x13,
        (
            "フェリックにしちゃ\x01",
            "ガキ臭えけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0207
    ChrTalk(
        0x13,
        (
            "ちょ、ちょっとだけ\x01",
            "羨ましいじゃんか。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)

    label("loc_3D63")

    TalkEnd(0xFE)
    Return()

    # Function_29_3C72 end

    def Function_30_3D67(): pass

    label("Function_30_3D67")

    TalkBegin(0xFE)

    #C0208
    ChrTalk(
        0x14,
        (
            "フェリックのやつ、\x01",
            "なんだか楽しそうね～。\x02",
        )
    )

    CloseMessageWindow()

    #C0209
    ChrTalk(
        0x14,
        (
            "は～あ、うちにも\x01",
            "あんなパワフルなお婆ちゃんが\x01",
            "居たらよかったのにー。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_30_3D67 end

    def Function_31_3DE7(): pass

    label("Function_31_3DE7")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3F41")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_3E9C")

    #C0210
    ChrTalk(
        0x101,
        (
            "#0003F予定通り聞き込みを続けよう。\x01",
            "情報を十分に集めないまま\x01",
            "判断するのは間違いの元だ。\x02\x03",

            "#0000F中央広場はもう十分だと思うから\x01",
            "……次は駅前通りだな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3F2A")

    label("loc_3E9C")


    #C0211
    ChrTalk(
        0x160,
        (
            "#3300F（中央広場の聞き込みは\x01",
            "  こんな所かしら？）\x02",
        )
    )

    CloseMessageWindow()

    #C0212
    ChrTalk(
        0x101,
        (
            "#0003F（ああ、十分だと思う。）\x02\x03",

            "#0000F（次は駅前通りで\x01",
            "  聞き込みをしてみよう。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3F2A")

    OP_D0(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0xB9, 5)
    OP_29(0x46, 0x1, 0x7)
    Jump("loc_3FB8")

    label("loc_3F41")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_3FB8")

    #C0213
    ChrTalk(
        0x101,
        (
            "#0003F予定通り中央広場の\x01",
            "聞き込みを続けよう。\x02\x03",

            "#0000F情報を十分に集めないまま\x01",
            "判断するのは間違いの元だ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3FB8")

    Return()

    # Function_31_3DE7 end

    def Function_32_3FB9(): pass

    label("Function_32_3FB9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_4203")
    TalkBegin(0xFE)
    OP_64(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_407C")

    #C0214
    ChrTalk(
        0xFE,
        "いや～、楽しみだな～。\x02",
    )

    CloseMessageWindow()

    #C0215
    ChrTalk(
        0xFE,
        (
            "ハハハ、だから\x01",
            "心配は要らないさ！\x02",
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
    Jump("loc_41E9")

    label("loc_407C")


    #C0216
    ChrTalk(
        0xFE,
        (
            "あはは、そうなんだよね～。\x01",
            "中央広場は人が多くてさ……\x02",
        )
    )

    CloseMessageWindow()

    #C0217
    ChrTalk(
        0xFE,
        (
            "……ちなみに今日はこれから\x01",
            "ティオ君に会いに行くつもりなんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0218
    ChrTalk(
        0xFE,
        (
            "うんうん、ハハハ！\x01",
            "それは心配要らないさ！\x02",
        )
    )

    CloseMessageWindow()

    #C0219
    ChrTalk(
        0x103,
        "#0211F（……主任……何の通信を……）\x02",
    )

    CloseMessageWindow()

    #C0220
    ChrTalk(
        0x101,
        (
            "#0005F（ティオ、いいのか？\x01",
            "  主任さんに挨拶しなくても……）\x02",
        )
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0x103,
        (
            "#0206F（……ええ、もう精神的に\x01",
            "  疲れてしまいそうなので\x01",
            "  パスしようかと。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)

    label("loc_41E9")

    OP_63(0xFE, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    TalkEnd(0xFE)
    Jump("loc_4C9E")

    label("loc_4203")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_4409")
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_42A0")
    Jump("loc_42EA")

    label("loc_42A0")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_42C0")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_42EA")

    label("loc_42C0")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_42E0")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_42EA")

    label("loc_42E0")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_42EA")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0222
    ChrTalk(
        0xFE,
        (
            "さて、今日はギヨームの修理屋を\x01",
            "訪ねてみようかな。\x02",
        )
    )

    CloseMessageWindow()

    #C0223
    ChrTalk(
        0xFE,
        (
            "あいつは昔からあの調子だから\x01",
            "パレードなんて見てないだろうし……\x02",
        )
    )

    CloseMessageWindow()

    #C0224
    ChrTalk(
        0xFE,
        (
            "ふふふ、何か土産でも\x01",
            "持って行ってやらないとね！\x02",
        )
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0x101,
        (
            "#0000F（ティオの上司さん、\x01",
            "  お祭りを満喫している……）\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Jump("loc_4C9E")

    label("loc_4409")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_459F")
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_44A6")
    Jump("loc_44F0")

    label("loc_44A6")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_44C6")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_44F0")

    label("loc_44C6")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_44E6")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_44F0")

    label("loc_44E6")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_44F0")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0226
    ChrTalk(
        0xFE,
        (
            "いや～、今年のパレードは\x01",
            "素晴らしかったねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0227
    ChrTalk(
        0xFE,
        "あれが噂の《みっしぃ》か……\x02",
    )

    CloseMessageWindow()

    #C0228
    ChrTalk(
        0xFE,
        (
            "うんうん、中々\x01",
            "いい構図で撮れたよ。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Jump("loc_4C9E")

    label("loc_459F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_47BF")
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_463C")
    Jump("loc_4686")

    label("loc_463C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_465C")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4686")

    label("loc_465C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_467C")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4686")

    label("loc_467C")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4686")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_4726")

    #C0229
    ChrTalk(
        0xFE,
        (
            "クロスベル市の\x01",
            "市街マップを呼び出して、\x01",
            "最適な穴場を検索！\x02",
        )
    )

    CloseMessageWindow()

    #C0230
    ChrTalk(
        0xFE,
        (
            "……うん、やっぱり\x01",
            "歓楽街の辺りかな！？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_47B3")

    label("loc_4726")


    #C0231
    ChrTalk(
        0xFE,
        (
            "今日はパレードだねぇ。\x01",
            "さて、どこで見るのがいいか……\x02",
        )
    )

    CloseMessageWindow()

    #C0232
    ChrTalk(
        0xFE,
        (
            "こんな時こそ携帯端末！\x01",
            "ピポパ、と……\x02",
        )
    )

    CloseMessageWindow()

    #C0233
    ChrTalk(
        0x103,
        "#0211F主任……楽しそうですね。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)

    label("loc_47B3")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Jump("loc_4C9E")

    label("loc_47BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_494A")
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_485C")
    Jump("loc_48A6")

    label("loc_485C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_487C")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_48A6")

    label("loc_487C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_489C")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_48A6")

    label("loc_489C")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_48A6")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9C, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_48E1")
    Call(0, 33)
    Jump("loc_493E")

    label("loc_48E1")


    #C0234
    ChrTalk(
        0xFE,
        "記念祭スペシャルランチか……\x02",
    )

    CloseMessageWindow()

    #C0235
    ChrTalk(
        0xFE,
        (
            "うんうん、期間限定とくれば\x01",
            "是非食べておかないとねえ♪\x02",
        )
    )

    CloseMessageWindow()

    label("loc_493E")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Jump("loc_4C9E")

    label("loc_494A")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_49DE")
    Jump("loc_4A28")

    label("loc_49DE")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_49FE")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4A28")

    label("loc_49FE")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4A1E")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4A28")

    label("loc_4A1E")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4A28")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_4AE4")

    #C0236
    ChrTalk(
        0xFE,
        (
            "後で支援課に\x01",
            "差し入れでも持っていくよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0237
    ChrTalk(
        0xFE,
        (
            "こほん……いつもティオ君が\x01",
            "世話になっているんだ。\x01",
            "監督者としてケジメは付けないとね～。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4C97")

    label("loc_4AE4")


    #C0238
    ChrTalk(
        0x103,
        "#0200Fあ、主任……\x02",
    )

    CloseMessageWindow()

    #C0239
    ChrTalk(
        0xFE,
        (
            "ティオ君～……\x01",
            "いやあ記念祭はいいよねぇ！\x02",
        )
    )

    CloseMessageWindow()

    #C0240
    ChrTalk(
        0xFE,
        (
            "僕は去年も回ったが\x01",
            "今年は一段と華やかな気がするなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0241
    ChrTalk(
        0xFE,
        (
            "あ、ティオ君も一緒に食べるかい？\x01",
            "今日は僕が奢っちゃうから……♪\x02",
        )
    )

    CloseMessageWindow()

    #C0242
    ChrTalk(
        0x103,
        "#0211F結構です。\x02",
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0243
    ChrTalk(
        0xFE,
        "そ、そうか、それじゃ仕方ない……\x02",
    )

    CloseMessageWindow()

    #C0244
    ChrTalk(
        0xFE,
        (
            "まあ後で支援課に\x01",
            "差し入れでも持っていくよ、ハハハ～！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)

    #C0245
    ChrTalk(
        0x103,
        "#0211F（浮かれている……）\x02",
    )

    CloseMessageWindow()

    #C0246
    ChrTalk(
        0x101,
        "#0000F（浮かれているな……）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)

    label("loc_4C97")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)

    label("loc_4C9E")

    Return()

    # Function_32_3FB9 end

    def Function_33_4C9F(): pass

    label("Function_33_4C9F")


    #C0247
    ChrTalk(
        0xFE,
        (
            "あ、ティオく～ん。\x01",
            "珍しいね、２人きりで……\x02",
        )
    )

    CloseMessageWindow()

    #C0248
    ChrTalk(
        0xFE,
        (
            "あ、もしかして……\x01",
            "デートかい？\x02",
        )
    )

    CloseMessageWindow()

    #C0249
    ChrTalk(
        0x101,
        "#0011F……えっ！？\x02",
    )

    CloseMessageWindow()

    #C0250
    ChrTalk(
        0x103,
        (
            "#0211F……突然くだらないことを\x01",
            "言わないで下さい、鬱陶しい。\x02",
        )
    )

    CloseMessageWindow()

    #C0251
    ChrTalk(
        0xFE,
        (
            "ははは……\x01",
            "ティオ君は相変わらずだなぁ♪\x02",
        )
    )

    CloseMessageWindow()

    #C0252
    ChrTalk(
        0xFE,
        (
            "よし、そんな君たちに\x01",
            "これをあげようじゃないか。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0253
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x2CC),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を受け取った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()

    #C0254
    ChrTalk(
        0x103,
        (
            "#0203F（……記念祭で浮かれすぎて\x01",
            "  いるようですね。）\x02\x03",

            "#0201F（後で灸を据えてあげないと。）\x02",
        )
    )

    CloseMessageWindow()

    #C0255
    ChrTalk(
        0x101,
        "#0003F（か、顔が怖いぞティオ……）\x02",
    )

    CloseMessageWindow()
    AddItemNumber(0x2CC, 1)
    SetScenarioFlags(0x9C, 6)
    Return()

    # Function_33_4C9F end

    SaveToFile()

Try(main)
