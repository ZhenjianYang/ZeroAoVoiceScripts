from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "e0510.bin",                # FileName
        "e0510",                    # MapName
        "e0510",                    # Location
        0x00A1,                     # MapIndex
        "ed7565",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0xFF,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 161, 0, 1, 0, 2],
    )

    BuildStringList((
        "e0510",                  # 0
        "エリィ",                 # 1
        "ノエル",                 # 2
        "ランディ",               # 3
        "乗組員サルサ",           # 4
        "市民",                   # 5
        "観光客",                 # 6
        "観光客",                 # 7
        "メルスン",               # 8
        "リマ",                   # 9
        "コロナ",                 # 10
        "フラン",                 # 11
        "セシル",                 # 12
        "イリア",                 # 13
        "リーシャ",               # 14
        "シュリ",                 # 15
        "マリアベル",             # 16
        "ツァイト",               # 17
        "SE制御",                 # 18
    ))

    AddCharChip((
        "chr/ch00100.itc",                   # 00
        "chr/ch02900.itc",                   # 01
        "chr/ch00302.itc",                   # 02
        "chr/ch28400.itc",                   # 03
        "chr/ch33002.itc",                   # 04
        "chr/ch20402.itc",                   # 05
        "chr/ch22102.itc",                   # 06
        "chr/ch26202.itc",                   # 07
        "chr/ch22702.itc",                   # 08
        "chr/ch20702.itc",                   # 09
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

    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   0,   0,   0,   0,   0,   3,   255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   1,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(0,       0,       0,       0,    388,  0x0, 1,   2,   0,   255, 255, 0,   5,   255,  0)
    DeclNpc(-100,    0,       -15420,  0,    389,  0x0, 0,   3,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(-2450,   150,     -3799,   180,  453,  0x0, 0,   4,   0,   255, 255, 0,   7,   255,  0)
    DeclNpc(-2450,   150,     -6449,   180,  453,  0x0, 0,   5,   0,   255, 255, 0,   8,   255,  0)
    DeclNpc(-3450,   150,     -6449,   180,  453,  0x0, 0,   6,   0,   255, 255, 0,   9,   255,  0)
    DeclNpc(-3049,   150,     -11350,  180,  389,  0x0, 0,   7,   0,   255, 255, 0,   10,  255,  0)
    DeclNpc(-3750,   150,     -11350,  180,  389,  0x0, 0,   9,   0,   255, 255, 0,   12,  255,  0)
    DeclNpc(-2250,   150,     -11350,  180,  389,  0x0, 0,   8,   0,   255, 255, 0,   11,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    ChipFrameInfo(844, 0)                                        # 0

    ScpFunction((
        "Function_0_34C",          # 00, 0
        "Function_1_3FC",          # 01, 1
        "Function_2_4FF",          # 02, 2
        "Function_3_554",          # 03, 3
        "Function_4_8C2",          # 04, 4
        "Function_5_B46",          # 05, 5
        "Function_6_E70",          # 06, 6
        "Function_7_1005",         # 07, 7
        "Function_8_1100",         # 08, 8
        "Function_9_1188",         # 09, 9
        "Function_10_120E",        # 0A, 10
        "Function_11_13D1",        # 0B, 11
        "Function_12_15AA",        # 0C, 12
        "Function_13_1627",        # 0D, 13
        "Function_14_2967",        # 0E, 14
        "Function_15_38B3",        # 0F, 15
        "Function_16_38DB",        # 10, 16
        "Function_17_3903",        # 11, 17
    ))


    def Function_0_34C(): pass

    label("Function_0_34C")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_384"),
        (1, "loc_390"),
        (2, "loc_39C"),
        (3, "loc_3A8"),
        (4, "loc_3B4"),
        (5, "loc_3C0"),
        (6, "loc_3CC"),
        (SWITCH_DEFAULT, "loc_3D8"),
    )


    label("loc_384")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_3E4")

    label("loc_390")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_3E4")

    label("loc_39C")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_3E4")

    label("loc_3A8")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_3E4")

    label("loc_3B4")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_3E4")

    label("loc_3C0")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_3E4")

    label("loc_3CC")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_3E4")

    label("loc_3D8")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_3E4")

    label("loc_3E4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3FB")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_3E4")

    label("loc_3FB")

    Return()

    # Function_0_34C end

    def Function_1_3FC(): pass

    label("Function_1_3FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4EF")
    SetChrPos(0x8, 630, -1000, 9000, 270)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x9, -620, -1000, 9000, 90)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0xA, 3250, 150, -9100, 180)
    ClearChrFlags(0xA, 0x80)
    SetChrChipByIndex(0xA, 0x2)
    SetChrSubChip(0xA, 0x0)
    EndChrThread(0xA, 0x0)
    SetChrBattleFlags(0xA, 0x4)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetChrChipByIndex(0xC, 0x4)
    SetChrSubChip(0xC, 0x0)
    EndChrThread(0xC, 0x0)
    SetChrBattleFlags(0xC, 0x4)
    ClearChrFlags(0xD, 0x80)
    SetChrChipByIndex(0xD, 0x5)
    SetChrSubChip(0xD, 0x0)
    EndChrThread(0xD, 0x0)
    SetChrBattleFlags(0xD, 0x4)
    ClearChrFlags(0xE, 0x80)
    SetChrChipByIndex(0xE, 0x6)
    SetChrSubChip(0xE, 0x0)
    EndChrThread(0xE, 0x0)
    SetChrBattleFlags(0xE, 0x4)
    ClearChrFlags(0xF, 0x80)
    SetChrChipByIndex(0xF, 0x7)
    SetChrSubChip(0xF, 0x0)
    EndChrThread(0xF, 0x0)
    SetChrBattleFlags(0xF, 0x4)
    ClearChrFlags(0x11, 0x80)
    SetChrChipByIndex(0x11, 0x8)
    SetChrSubChip(0x11, 0x0)
    EndChrThread(0x11, 0x0)
    SetChrBattleFlags(0x11, 0x4)
    ClearChrFlags(0x10, 0x80)
    SetChrChipByIndex(0x10, 0x9)
    SetChrSubChip(0x10, 0x0)
    EndChrThread(0x10, 0x0)
    SetChrBattleFlags(0x10, 0x4)
    SetChrFlags(0x10, 0x10)
    SetChrSubChip(0x10, 0x2)

    label("loc_4EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_4FE")
    ClearScenarioFlags(0x22, 0)
    Event(0, 17)

    label("loc_4FE")

    Return()

    # Function_1_3FC end

    def Function_2_4FF(): pass

    label("Function_2_4FF")

    Sound(480, 1, 100, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_533")
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x9, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)

    label("loc_533")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_553")
    SetChrSubChip(0xA, 0x1)
    OP_63(0xA, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)

    label("loc_553")

    Return()

    # Function_2_4FF end

    def Function_3_554(): pass

    label("Function_3_554")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_56B")
    Call(0, 13)
    Return()

    label("loc_56B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_57C")
    Jump("loc_8BE")

    label("loc_57C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_58A")
    Jump("loc_8BE")

    label("loc_58A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_598")
    Jump("loc_8BE")

    label("loc_598")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_5A8")
    Jump("loc_8BE")

    label("loc_5A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_5B6")
    Jump("loc_8BE")

    label("loc_5B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_5C4")
    Jump("loc_8BE")

    label("loc_5C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_5D2")
    Jump("loc_8BE")

    label("loc_5D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_5E0")
    Jump("loc_8BE")

    label("loc_5E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_8BE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5F8")
    Jump("loc_8BE")

    label("loc_5F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_847")

    #C0001
    ChrTalk(
        0x8,
        (
            "#00100Fせっかくバカンスに来たんですもの、\x01",
            "楽しまないと損というものよね。\x02\x03",

            "#00104F確かベルも、色々とサプライズを\x01",
            "用意してるとか言っていたし……\x02\x03",

            "#00102Fふふ、そう考えたら\x01",
            "結構楽しみになってきたかも。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x101,
        (
            "#00012Fサプライズか……\x01",
            "俺としてはちょっと心配だけど。\x02\x03",

            "#00003Fミシュラム総がかりで歓迎してくる\x01",
            "ようなものだったりしたら、\x01",
            "さすがに萎縮しちゃうだろうし。\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0x8,
        (
            "#00109Fい、いくらベルが派手好きでも\x01",
            "そこまでのものを用意なんて……\x02\x03",

            "#00103F……しないとも言い切れないわね。\x02\x03",

            "#00102Fせ、せめておかしな物じゃない事を\x01",
            "女神に祈りましょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x101,
        "#00006F（し、心配だなあ……）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_8BE")

    label("loc_847")


    #C0005
    ChrTalk(
        0x8,
        (
            "#00103Fうーん、それにしても\x01",
            "ベルのサプライズって一体何なのかしら。\x02\x03",

            "#00111F……おかしなものじゃなければいいけど。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8BE")

    TalkEnd(0xFE)
    Return()

    # Function_3_554 end

    def Function_4_8C2(): pass

    label("Function_4_8C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8D9")
    Call(0, 13)
    Return()

    label("loc_8D9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_8EA")
    Jump("loc_B42")

    label("loc_8EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_8F8")
    Jump("loc_B42")

    label("loc_8F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_906")
    Jump("loc_B42")

    label("loc_906")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_916")
    Jump("loc_B42")

    label("loc_916")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_924")
    Jump("loc_B42")

    label("loc_924")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_932")
    Jump("loc_B42")

    label("loc_932")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_940")
    Jump("loc_B42")

    label("loc_940")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_94E")
    Jump("loc_B42")

    label("loc_94E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_B42")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_966")
    Jump("loc_B42")

    label("loc_966")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AC8")

    #C0006
    ChrTalk(
        0x9,
        (
            "#10105Fそういえば、セルゲイ課長は\x01",
            "一緒に来れなくて残念でしたね。\x02\x03",

            "#10106F楽しんでこい、\x01",
            "なんて言ってましたけど\x01",
            "やっぱり申し訳ないというか……\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x101,
        (
            "#00003F課長もあれで結構忙しい人だしな……\x02\x03",

            "#00002Fはは、もしかしたら単に\x01",
            "プライベートな姿を見られるのが\x01",
            "恥ずかしいだけかもしれないけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x9,
        "#10109Fあはは、それは意外で面白いですね。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_B42")

    label("loc_AC8")


    #C0009
    ChrTalk(
        0x9,
        (
            "#10103Fセルゲイ課長は\x01",
            "一緒に来れなくて残念でしたね。\x02\x03",

            "#10102F今頃、支援課で一人\x01",
            "煙草をふかしてたりするんでしょうか。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B42")

    TalkEnd(0xFE)
    Return()

    # Function_4_8C2 end

    def Function_5_B46(): pass

    label("Function_5_B46")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B5D")
    Call(0, 14)
    Return()

    label("loc_B5D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_B6E")
    Jump("loc_E6C")

    label("loc_B6E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_B7C")
    Jump("loc_E6C")

    label("loc_B7C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_B8A")
    Jump("loc_E6C")

    label("loc_B8A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_B98")
    Jump("loc_E6C")

    label("loc_B98")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_BA6")
    Jump("loc_E6C")

    label("loc_BA6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_BB4")
    Jump("loc_E6C")

    label("loc_BB4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_BC2")
    Jump("loc_E6C")

    label("loc_BC2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_E6C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BDA")
    Jump("loc_E6C")

    label("loc_BDA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DE4")

    #C0010
    ChrTalk(
        0xA,
        (
            "#00303Fかーっ、やっぱ辛気くせえのは\x01",
            "俺様のキャラじゃねえな。\x02\x03",

            "#00301Fこうなったら、今日はとことん\x01",
            "ミシュラムを満喫してやろうじゃねえか！\x02\x03",

            "#00309Fロイド、夜のナンパにはお前も付き合えよ？\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x101,
        (
            "#00012Fはは、まあランディに任せっきりに\x01",
            "なるだろうけど、それでいいなら。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0xA,
        (
            "#00306Fなんだなんだ、消極的だなあ。\x02\x03",

            "#00309Fお前も素材がいいんだから、\x01",
            "いっそ弟キャラなんて脱却して\x01",
            "イケイケになっちまえよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x101,
        (
            "#00006Fい、意味わかんないんだが……\x02\x03",

            "#00000F（……でも、いつもの調子に\x01",
            "  戻ってくれたみたいだな。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_E64")

    label("loc_DE4")


    #C0014
    ChrTalk(
        0xA,
        (
            "#00305Fああそうだ、アイツにも\x01",
            "土産を買っとかねえとなあ……\x02\x03",

            "#00304F昇進するって話だったし、\x01",
            "どっかで祝いの品でも見繕うか。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E64")

    TalkEnd(0xFE)
    SetChrSubChip(0xA, 0x1)
    Return()

    label("loc_E6C")

    TalkEnd(0xFE)
    Return()

    # Function_5_B46 end

    def Function_6_E70(): pass

    label("Function_6_E70")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_E81")
    Jump("loc_1001")

    label("loc_E81")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_E8F")
    Jump("loc_1001")

    label("loc_E8F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_E9D")
    Jump("loc_1001")

    label("loc_E9D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_1001")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F74")

    #C0015
    ChrTalk(
        0xB,
        (
            "本日の水上バスのご利用、\x01",
            "誠にありがとうございます。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0xB,
        (
            "皆様はマリアベル様に\x01",
            "ご招待された方々ですね？\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0xB,
        (
            "ミシュラムまでの短い一時、\x01",
            "波に揺られる穏やかな旅を\x01",
            "お楽しみくださいませ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1001")

    label("loc_F74")


    #C0018
    ChrTalk(
        0xB,
        (
            "酔ってしまわれた時は、\x01",
            "甲板で遠くの景色を眺めて\x01",
            "気を紛らわすとよいですよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0xB,
        (
            "酔い止めの用意もありますので\x01",
            "どうぞご安心くださいませ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1001")

    TalkEnd(0xFE)
    Return()

    # Function_6_E70 end

    def Function_7_1005(): pass

    label("Function_7_1005")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_10FC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10A8")

    #C0020
    ChrTalk(
        0xC,
        (
            "通商会議での独立提唱には\x01",
            "本当に驚いたのう。\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0xC,
        (
            "ディーター殿がどのように\x01",
            "それを実現させるつもりなのか……\x01",
            "楽しみでならんわい。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_10FC")

    label("loc_10A8")


    #C0022
    ChrTalk(
        0xC,
        (
            "ディーター殿がどのように\x01",
            "独立を実現させるつもりなのか……\x01",
            "楽しみでならんわい。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10FC")

    TalkEnd(0xFE)
    Return()

    # Function_7_1005 end

    def Function_8_1100(): pass

    label("Function_8_1100")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_1184")

    #C0023
    ChrTalk(
        0xD,
        (
            "夢にまで見たクロスベル旅行、\x01",
            "保養地ミシュラムのテーマパーク！\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0xD,
        (
            "いやー、楽しみだなあ。\x01",
            "彼女と目一杯遊ぶぞお～！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1184")

    TalkEnd(0xFE)
    Return()

    # Function_8_1100 end

    def Function_9_1188(): pass

    label("Function_9_1188")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_120A")

    #C0025
    ChrTalk(
        0xE,
        (
            "個人的にはレストランや\x01",
            "ブティックも行ってみたいのよね～。\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0xE,
        (
            "うふふ、今日はカレに\x01",
            "たっくさん甘えちゃおうっと。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_120A")

    TalkEnd(0xFE)
    Return()

    # Function_9_1188 end

    def Function_10_120E(): pass

    label("Function_10_120E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_121F")
    Jump("loc_13CD")

    label("loc_121F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_122D")
    Jump("loc_13CD")

    label("loc_122D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_123B")
    Jump("loc_13CD")

    label("loc_123B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_1249")
    Jump("loc_13CD")

    label("loc_1249")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_13CD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1348")

    #C0027
    ChrTalk(
        0xF,
        (
            "クロスベルの独立か……\x01",
            "さすがディーター市長は\x01",
            "他にはない発想をされるね。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0xF,
        (
            "決して簡単な道のりでは\x01",
            "ないだろうけど……\x01",
            "彼の言葉には夢があるからね。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0xF,
        (
            "市長は必ずやクロスベルを\x01",
            "明るく照らしてくれる。\x01",
            "そんな気がするのさ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_13CD")

    label("loc_1348")


    #C0030
    ChrTalk(
        0xF,
        (
            "おっと、せっかく家族で\x01",
            "遊びにきたっていうのに\x01",
            "こういう話もなかったかな。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0xF,
        (
            "今日はリマとコロナに\x01",
            "沢山楽しんでもらわなきゃね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13CD")

    TalkEnd(0xFE)
    Return()

    # Function_10_120E end

    def Function_11_13D1(): pass

    label("Function_11_13D1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_13E2")
    Jump("loc_15A6")

    label("loc_13E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_13F0")
    Jump("loc_15A6")

    label("loc_13F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_13FE")
    Jump("loc_15A6")

    label("loc_13FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_140C")
    Jump("loc_15A6")

    label("loc_140C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_15A6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1528")

    #C0032
    ChrTalk(
        0x11,
        (
            "オルキスタワーの建設が終わって\x01",
            "夫にボーナスが出たので、\x01",
            "家族旅行に来てるんですよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x11,
        (
            "本当なら貯金する所なんですけど、\x01",
            "『たまには家族サービスをしたい』と\x01",
            "夫に押し切られてしまって。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x11,
        (
            "でも、やっぱり来て良かったです。\x01",
            "リマがあんなに喜んでますから。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_15A6")

    label("loc_1528")


    #C0035
    ChrTalk(
        0x11,
        (
            "夫にボーナスが出たので、\x01",
            "家族旅行に来てるんですよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x11,
        (
            "ふふ、やっぱり来て良かったです。\x01",
            "リマがあんなに喜んでますから。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15A6")

    TalkEnd(0xFE)
    Return()

    # Function_11_13D1 end

    def Function_12_15AA(): pass

    label("Function_12_15AA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_15BB")
    Jump("loc_1623")

    label("loc_15BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_15C9")
    Jump("loc_1623")

    label("loc_15C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_15D7")
    Jump("loc_1623")

    label("loc_15D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_15E5")
    Jump("loc_1623")

    label("loc_15E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_1623")

    #C0037
    ChrTalk(
        0x10,
        (
            "パパー、見て見て！！\x01",
            "おさかなさんが飛んだよー！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1623")

    TalkEnd(0xFE)
    Return()

    # Function_12_15AA end

    def Function_13_1627(): pass

    label("Function_13_1627")

    EventBegin(0x0)
    SoundLoad(3515)
    SoundLoad(3394)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu10100.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu00101.itp")
    Fade(500)
    OP_68(700, 200, 8350, 0)
    MoveCamera(15, 33, 0, 0)
    OP_6E(260, 0)
    SetCameraDistance(33390, 0)
    OP_64(0x8)
    OP_64(0x9)
    OP_4B(0x8, 0xFF)
    OP_4B(0x9, 0xFF)
    SetChrPos(0x8, 500, -1000, 9000, 230)
    SetChrPos(0x9, -500, -1000, 9000, 80)
    SetChrPos(0x101, 1500, -1000, 8200, 315)
    OP_0D()
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_1735():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1735)
    Sleep(50)

    def lambda_1745():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1745)
    WaitChrThread(0x9, 1)
    OP_63(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_C9(0x0, 0x80000000)

    #A0038
    AnonymousTalk(
        0x9,
        "#30W#3515Vあ……ロイドさん。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_C9(0x1, 0x80000000)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    Sound(2189, 255, 100, 0)    #voice#Elie
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0039
    AnonymousTalk(
        0x8,
        "#30W甲板に出ていたの？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)

    #C0040
    ChrTalk(
        0x101,
        (
            "#00004F#12Pああ、風に当たりにね。\x02\x03",

            "#00005Fえっと、お邪魔だったかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x8,
        "#00108F#5Pあ、ううん……\x02",
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x9,
        (
            "#10106F#5P……その、通商会議の時の\x01",
            "出来事について……\x02\x03",

            "#10113Fそれとディーター市長の\x01",
            "提案について話してたんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x101,
        (
            "#00001F#12P提案……\x01",
            "『国家として独立』するってあれか。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x8,
        (
            "#00106F#5Pええ……私にとっては\x01",
            "ちょっと他人事ではないわね。\x02\x03",

            "#00108Fまさかおじさまが\x01",
            "あんな事を考えてたなんて……\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x9,
        (
            "#10106F#5Pあたしもその……\x01",
            "正直、他人事じゃない感じです。\x02\x03",

            "#10108F警備隊の存続にも\x01",
            "関わってくる話ですから……\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x101,
        (
            "#00003F#12Pそうか……帝国と共和国は\x01",
            "クロスベル警備隊の規模縮小を\x01",
            "要求して来ているんだよな。\x02\x03",

            "#00013F代わりに自分たちの軍隊を\x01",
            "タングラム門とベルガード門に\x01",
            "駐留させようっていう……\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x8,
        (
            "#00103F#5Pええ……\x02\x03",

            "#00108Fどう考えてもクロスベルから\x01",
            "更なる富を吸い上げるために\x01",
            "結託したとしか思えないわ。\x02\x03",

            "#00101Fそして、あわよくば\x01",
            "お互いの隙を狙って併合して\x01",
            "果実を独り占めをする……\x02\x03",

            "#00106Fその準備としか思えないもの。\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x101,
        (
            "#00006F#12P確かに……\x02\x03",

            "#00001F……となると、市長の提案は\x01",
            "それに対抗する案でもあるのか。\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x9,
        (
            "#10103F#5Pええ、国家として独立すれば\x01",
            "今まで両国に抑え付けられていた\x01",
            "警備隊の装備も充実できます。\x02\x03",

            "#10101F対人用の武装だけじゃなくて、\x01",
            "他国の侵略を阻止するための\x01",
            "戦車や軍用飛行艇なんかも。\x02\x03",

            "#10106F……そんな風に考える自分が\x01",
            "ちょっと嫌になりますけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x101,
        "#00008F#12Pノエル……\x02",
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x8,
        (
            "#00103F#5Pでも、おじさまの提案が\x01",
            "現実的かどうかと言われると……\x02\x03",

            "#00108F帝国と共和国からは早速、\x01",
            "否定的な声明が出されているわ。\x02\x03",

            "#00100Fでも、リベールやレミフェリア、\x01",
            "アルテリア法国などは好意的に\x01",
            "受け取る声明を出してくれて……\x02\x03",

            "#00106F正直、もどかしい状況だわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x101,
        "#00006F#12Pそうだな……\x02",
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x9,
        (
            "#10113F#5P……今日、招待してくれた\x01",
            "マリアベルさんなんかは\x01",
            "どう考えているんでしょう？\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0xE1, 0x1F4)
    Sleep(100)

    #C0054
    ChrTalk(
        0x8,
        (
            "#00106F#11Pどちらかというと彼女は\x01",
            "今はＩＢＣの運営の方に\x01",
            "専念しているみたいね。\x02\x03",

            "#00108F今回の提案については\x01",
            "そこまで関わっていないみたい。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x9, 0x2D, 0x1F4)
    Sleep(100)

    #C0055
    ChrTalk(
        0x9,
        (
            "#10106F#6Pそうですか……\x02\x03",

            "#10108F……せっかくの機会だから\x01",
            "お聞きしたいと思ったんですが。\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x8,
        (
            "#00103F#11Pそうね……私もベルには\x01",
            "聞きたいことが結構あるし……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    #C0057
    ChrTalk(
        0x101,
        (
            "#00004F#12P──なあ、２人とも。\x02\x03",

            "#00000Fこういう時だからこそさ。\x01",
            "目一杯楽しんでいかないか？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_211F():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_211F)
    Sleep(50)

    def lambda_212F():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_212F)
    WaitChrThread(0x8, 2)
    WaitChrThread(0x9, 2)

    #C0058
    ChrTalk(
        0x8,
        "#00105F#5Pえ……\x02",
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x9,
        "#10105F#5P……？\x02",
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x101,
        (
            "#00002F#12P滅多にない休暇で\x01",
            "ミシュラムのホテルに宿泊だぞ？\x02\x03",

            "しかもあのテーマパークで\x01",
            "遊びたい放題だっていうし。\x02\x03",

            "#00009Fさぞかし頭を空っぽに\x01",
            "出来るんじゃないかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x8,
        "#00106F#5P#30Wで、でも……\x02",
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x9,
        "#10108F#5P#30W……あんな事があった後で……\x02",
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x101,
        (
            "#00000F#12Pあんな事があったからさ。\x02\x03",

            "#00003Fこの先、クロスベルの状況が\x01",
            "どうなるか分からない……\x02\x03",

            "俺たちの仕事だって\x01",
            "大変になる可能性が高いだろう。\x02\x03",

            "#00002Fだからこそ何ていうか……\x01",
            "『思い出』が作りたいんだ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0064
    ChrTalk(
        0x8,
        "#00112F#5Pええっ……！\x02",
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x9,
        "#10114F#5Pそ、それって……！？\x02",
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x101,
        (
            "#00005F#12P（……え？\x01",
            "  何でそこまで反応するんだ？）\x02\x03",

            "#00012Fはは……\x01",
            "さすがにクサすぎたかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x9,
        (
            "#10112F#5Pクサすぎっていうか……\x02\x03",

            "#10108F（エリィさん……\x01",
            "  わざとやってるんですか？）\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x8,
        (
            "#00111F#5P（ううん……\x01",
            "  天然の可能性が高いわね……）\x02\x03",

            "#00113F──えっと、ロイド。\x02\x03",

            "#00112Fその『思い出』っていうのは\x01",
            "特定の誰かのことじゃないわよね？\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x101,
        (
            "#00005F#12P？　勿論そうだけど……\x02\x03",

            "#00000Fみんなで休暇が取れるなんて\x01",
            "滅多にあることじゃないからな。\x02\x03",

            "#00012Fはは、課長には申しわけないけどさ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x9, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0070
    ChrTalk(
        0x8,
        "#00113F#5Pはあぁ～～っ……\x02",
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x9,
        (
            "#10112F#5Pそ、そうですよね。\x01",
            "それでこそロイドさんというか……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0072
    ChrTalk(
        0x101,
        (
            "#00005F#12Pあれ、ひょっとして俺、\x01",
            "さっきから外しまくってるか？\x02\x03",

            "#00006Fみんな落ち込んでるみたいだから\x01",
            "少しでも元気付けようと─#3500W─#30W",
            "#00011Fあ。\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0x9,
        "#10102F#5Pぷっ……\x02",
    )

    CloseMessageWindow()
    Sleep(200)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0074
    ChrTalk(
        0x8,
        (
            "#00114F#5Pあははっ……！\x02\x03",

            "#00116Fあ、貴方って本当に……\x01",
            "天然というか不器用というか。\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0x9,
        (
            "#10109F#5Pふふ、何だか悩んでいたのが\x01",
            "バカらしくなっちゃいましたね。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0076
    ChrTalk(
        0x101,
        (
            "#00006F#12P……悪かった。\x01",
            "顔を洗って出直してくるよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0x8,
        (
            "#00104F#5Pふふ、拗#2Rす#ねないの。\x02\x03",

            "#00102F……ごめんなさい。\x01",
            "私たちの方こそちょっと\x01",
            "空気が読めていなかったわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0x9,
        (
            "#10102F#5Pそうですね……\x01",
            "やっぱりバカンスに行くなら\x01",
            "目いっぱい楽しまないと！\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0x101,
        (
            "#00002F#12Pそっか……\x01",
            "（一応、目的は果たせたかな？）\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x8, 630, -1000, 9000, 270)
    SetChrPos(0x9, -620, -1000, 9000, 90)
    OP_4C(0x8, 0xFF)
    OP_4C(0x9, 0xFF)
    SetChrPos(0x0, 3000, -1000, 6500, 180)
    OP_CC(0x1, 0xFF, 0x0)
    SetScenarioFlags(0x144, 2)
    EventEnd(0x5)
    Return()

    # Function_13_1627 end

    def Function_14_2967(): pass

    label("Function_14_2967")

    EventBegin(0x0)
    Fade(500)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu00301.itp")
    OP_68(3170, 1300, -9560, 0)
    MoveCamera(50, 21, 0, 0)
    OP_6E(260, 0)
    SetCameraDistance(34500, 0)
    OP_64(0xA)
    SetChrPos(0x101, 800, 0, -9770, 90)
    SetCameraDistance(34000, 1500)
    OP_9B(0x0, 0x101, 0x0, 0x3E8, 0x3E8, 0x0)
    OP_93(0x101, 0x2D, 0x1F4)
    OP_6F(0x79)
    OP_0D()
    SetChrSubChip(0xA, 0x0)
    Sleep(100)
    SetChrSubChip(0xA, 0x2)
    Sleep(200)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(300)
    #Sound(2756, 255, 100, 0)    #voice#Randy

    #A0080
    AnonymousTalk(
        0xA,
        (
            "#30W──よう、ロイド。\x02\x03",

            "#20Wしっかし、マリアベルお嬢さんも\x01",
            "ずいぶん太っ腹だよなぁ。\x02\x03",

            "ミシュラムのリゾートホテルに\x01",
            "テーマパークも遊びたい放題。\x02\x03",

            "どんな大盤振る舞いだっつーの。\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xAC4)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    #C0081
    ChrTalk(
        0x101,
        (
            "#00002F#6P……そうだな。\x02\x03",

            "#00008F………………………………\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0xA,
        "#00302F#5Pはは……\x02",
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0xA)

    #C0083
    ChrTalk(
        0xA,
        (
            "#00304F#5P──なあロイド。\x02\x03",

            "#00300Fカン違いさせてるみたいだから\x01",
            "ひとつ言っとくぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x101,
        "#00005F#6Pえ……\x02",
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0xA,
        (
            "#00303F#5Pテロリストどもが殺された件……\x02\x03",

            "#00301F身内があんな事をやったことに\x01",
            "俺がショックを受けてると\x01",
            "思ってんだろ？\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x101,
        "#00011F#6Pそ、それは……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    #C0087
    ChrTalk(
        0x101,
        (
            "#00006F#6P……いや、ちょっと違うな。\x02\x03",

            "#00008Fランディは、自分自身のことで\x01",
            "何かを引きずっている気がする。\x02\x03",

            "#00001F叔父さん達のことはそこまで\x01",
            "こだわってないんじゃないか？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    StopBGM(0xBB8)
    BeginChrThread(0x19, 1, 0, 15)

    #C0088
    ChrTalk(
        0xA,
        (
            "#00308F#5P……そっか。\x02\x03",

            "#00303F#30W…………………………………\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7534", 0)
    SetChrSubChip(0xA, 0x0)
    Sleep(150)
    SetChrSubChip(0xA, 0x1)
    SetCameraDistance(33000, 20000)
    Sleep(1000)

    #C0089
    ChrTalk(
        0xA,
        (
            "#00304F#5P──ダチがいたんだ。\x02\x03",

            "俺より１つ下で\x01",
            "仔犬みたいな目をしてた……\x02\x03",

            "#00300F多分、団以外で初めて知り合った\x01",
            "ダチと呼べるような存在が。\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x101,
        "#00005F#6P…………………………………\x02",
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0xA,
        (
            "#00308F#5P色々あって\x01",
            "そいつはいなくなって……\x02\x03",

            "やっぱり色々あって\x01",
            "俺は団を抜けてさ迷った。\x02\x03",

            "#00303Fそしてクロスベルに辿り着いて\x01",
            "警備隊に入って……\x01",
            "お前たちと知り合って……\x02\x03",

            "#00302F……だが、俺は骨の髄まで\x01",
            "俺でしかなかったみてぇだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0x101,
        "#00005F#6Pえ……\x02",
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0xA,
        (
            "#00312F#5P──叔父貴の言うとおり、\x01",
            "テロリストどもが殺された顛末は\x01",
            "俺には珍しいもんじゃなかった。\x02\x03",

            "確かにあの程度の殲滅#4Rせんめつ#戦、\x01",
            "戦場じゃ日常茶飯事だったからな。\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x101,
        "#00008F#6P…………………………………\x02",
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0xA,
        (
            "#00303F#5P俺があの時キレたのは……\x01",
            "義憤に駆られてのことじゃねぇ。\x02\x03",

            "テロリストどもを哀れんだからでも、\x01",
            "叔父貴に怒りを覚えたからでもねぇ。\x02\x03",

            "#00308F#30W俺は──２年たっても\x01",
            "まったく変わらない自分に……\x02\x03",

            "骨の髄まで猟兵でしかない自分に\x01",
            "心底呆れちまっただけなんだ……\x02\x03",

            "#00306Fそれで八つ当たりみたいに\x01",
            "掴みかかって殴り飛ばされた……\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0x101,
        (
            "#00008F#6Pそっか……\x02\x03",

            "#00006F……確かに\x01",
            "それはカッコ悪いかもな。\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0xA,
        (
            "#00302F#5Pハハ、だろ？\x02\x03",

            "#00306Fまったく、クールな伊達男の\x01",
            "俺様がなんつー無様な──\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x101,
        (
            "#00002F#6P……でもさ。\x01",
            "ちょっと嬉しいかな。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    SetChrSubChip(0xA, 0x0)
    Sleep(120)
    SetChrSubChip(0xA, 0x2)
    Sleep(250)

    #C0099
    ChrTalk(
        0xA,
        "#00305F#5Pえ……\x02",
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0x101,
        (
            "#00004F#6P何ていうか、ランディって\x01",
            "いつも大人で余裕があるから\x01",
            "こちらが頼ってばかりじゃないか？\x02\x03",

            "#00000Fでも、そうやって\x01",
            "自分をさらけ出してくれると\x01",
            "仲間としては少し嬉しいんだ。\x02\x03",

            "たぶん俺だけじゃなくて……\x01",
            "他のみんなも同じだと思う。\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0xA,
        "#00305F#5P…………………………………\x02",
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x101,
        (
            "#00006F#6Pそれに……\x01",
            "骨の髄まで猟兵だなんて\x01",
            "ただの思い込みじゃないのか？\x02\x03",

            "#00008F少なくとも俺は、ランディが\x01",
            "ミラのために戦争を請け負うのが\x01",
            "好きなタイプには思えない。\x02\x03",

            "#00000Fお調子者で、夜遊びが好きで\x01",
            "少し好戦的で熱くなりがちだけど\x01",
            "ちゃんと引き際もわきまえてる……\x02\x03",

            "#00002Fそして、いつも年下の俺たちを\x01",
            "フォローしてくれる兄貴分……\x02\x03",

            "#00009Fそれが、俺の知っている\x01",
            "ランディ・オルランドって男だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0xA,
        "#00305F#5P…………………………………\x02",
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0x101,
        (
            "#00003F#6Pだから少しくらい\x01",
            "カッコ悪い所を見せたからって\x01",
            "気にする必要はないさ。\x02\x03",

            "#00000Fむしろその方が\x01",
            "俺やエリィたちだって──\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0xA,
        (
            "#00303F#5P──分かった、皆まで言うな。\x02\x03",

            "#00306Fどうやらお前のポテンシャルを\x01",
            "まだ甘く見てたみてぇだ……\x02\x03",

            "#00310Fどんだけだよ、この天然タラシは！？\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0x101,
        (
            "#00011F#6Pて、天然タラシ？\x02\x03",

            "#00006Fよく分からないけどそこまで\x01",
            "逆ギレされること言ったか？\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0x7D0)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7565", 0)
    BeginChrThread(0x19, 1, 0, 16)

    #C0107
    ChrTalk(
        0xA,
        (
            "#00315F#5Pあーもう、鬱#2Rウツ#ってるのが\x01",
            "馬鹿馬鹿しくなってきたぜ……\x02\x03",

            "#00306Fこうなりゃとことん、\x01",
            "ミシュラムを満喫してやる！\x02\x03",

            "#00301Fテーマパークで遊びまくって\x01",
            "夜は姉ちゃんをナンパするぞ！\x02\x03",

            "#00307Fお前も付き合え、この弟野郎！\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0x101,
        (
            "#00012F#6Pりょ、了解ッス。\x02\x03",

            "#00002F（よく分からないけど……\x01",
            "  元気出してくれたのかな？）\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, 980, 0, -10170, 270)
    SetChrSubChip(0xA, 0x1)
    OP_CC(0x1, 0xFF, 0x0)
    SetScenarioFlags(0x144, 3)
    EventEnd(0x5)
    Return()

    # Function_14_2967 end

    def Function_15_38B3(): pass

    label("Function_15_38B3")

    OP_25(0x1E0, 0x5A)
    Sleep(200)
    OP_25(0x1E0, 0x50)
    Sleep(200)
    OP_25(0x1E0, 0x46)
    Sleep(200)
    OP_25(0x1E0, 0x3C)
    Sleep(200)
    OP_25(0x1E0, 0x32)
    Sleep(200)
    OP_25(0x1E0, 0x28)
    Return()

    # Function_15_38B3 end

    def Function_16_38DB(): pass

    label("Function_16_38DB")

    OP_25(0x1E0, 0x32)
    Sleep(200)
    OP_25(0x1E0, 0x3C)
    Sleep(200)
    OP_25(0x1E0, 0x46)
    Sleep(200)
    OP_25(0x1E0, 0x50)
    Sleep(200)
    OP_25(0x1E0, 0x5A)
    Sleep(200)
    OP_25(0x1E0, 0x64)
    Return()

    # Function_16_38DB end

    def Function_17_3903(): pass

    label("Function_17_3903")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch08502.itc", 0x1E)
    LoadChrToIndex("chr/ch05202.itc", 0x1F)
    LoadChrToIndex("chr/ch05102.itc", 0x20)
    LoadChrToIndex("chr/ch07502.itc", 0x21)
    LoadChrToIndex("chr/ch10002.itc", 0x22)
    LoadChrToIndex("chr/ch05502.itc", 0x23)
    LoadChrToIndex("chr/ch05602.itc", 0x24)
    LoadChrToIndex("chr/ch00102.itc", 0x25)
    LoadChrToIndex("chr/ch00202.itc", 0x26)
    LoadChrToIndex("chr/ch02902.itc", 0x28)
    LoadChrToIndex("chr/ch03002.itc", 0x29)
    LoadChrToIndex("chr/ch02702.itc", 0x2A)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrChipByIndex(0x102, 0x25)
    SetChrSubChip(0x102, 0x1)
    SetChrFlags(0x102, 0x4)
    SetChrChipByIndex(0x103, 0x26)
    SetChrSubChip(0x103, 0x0)
    SetChrFlags(0x103, 0x4)
    SetChrChipByIndex(0x104, 0x2)
    SetChrSubChip(0x104, 0x1)
    SetChrFlags(0x104, 0x4)
    SetChrChipByIndex(0x109, 0x28)
    SetChrSubChip(0x109, 0x1)
    SetChrFlags(0x109, 0x4)
    SetChrChipByIndex(0x105, 0x29)
    SetChrSubChip(0x105, 0x2)
    SetChrFlags(0x105, 0x4)
    SetChrChipByIndex(0x18, 0x2A)
    SetChrSubChip(0x18, 0x0)
    ClearChrFlags(0x18, 0x80)
    SetChrFlags(0x18, 0x8000)
    OP_52(0x18, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x18, 1, 0, 0)
    SetChrChipByIndex(0x12, 0x1E)
    SetChrSubChip(0x12, 0x2)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x12, 0x8000)
    SetChrChipByIndex(0x15, 0x1F)
    SetChrSubChip(0x15, 0x1)
    ClearChrFlags(0x15, 0x80)
    SetChrFlags(0x15, 0x8000)
    SetChrChipByIndex(0x14, 0x20)
    SetChrSubChip(0x14, 0x1)
    ClearChrFlags(0x14, 0x80)
    SetChrFlags(0x14, 0x8000)
    SetChrChipByIndex(0x13, 0x21)
    SetChrSubChip(0x13, 0x2)
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x13, 0x8000)
    SetChrChipByIndex(0x16, 0x22)
    SetChrSubChip(0x16, 0x2)
    ClearChrFlags(0x16, 0x80)
    SetChrFlags(0x16, 0x8000)
    SetChrChipByIndex(0x17, 0x23)
    SetChrSubChip(0x17, 0x2)
    ClearChrFlags(0x17, 0x80)
    SetChrFlags(0x17, 0x8000)
    SetChrPos(0x101, 0, 0, 0, 0)
    SetChrFlags(0x101, 0x8)
    SetChrPos(0x102, 1000, -800, 7350, 0)
    SetChrPos(0x17, 0, -800, 7350, 0)
    SetChrPos(0x103, -2200, 150, -13850, 180)
    SetChrPos(0x18, -1200, 0, -14850, 270)
    SetChrPos(0x104, -3550, 150, -3850, 180)
    SetChrPos(0x105, -2350, 150, -3850, 180)
    SetChrPos(0x109, 2100, 150, -11350, 180)
    SetChrPos(0x12, 3250, 150, -11350, 180)
    SetChrPos(0x15, -3550, 150, -8850, 180)
    SetChrPos(0x16, -2350, 150, -8850, 180)
    SetChrPos(0x14, 2100, 150, -8850, 180)
    SetChrPos(0x13, 3250, 150, -8850, 180)
    OP_68(0, 1000, -15000, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(21000, 0)
    FadeToBright(1000, 0)
    OP_68(0, 1000, 10000, 20000)
    Sleep(14000)
    OP_0D()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 2)
    NewScene("e3000", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_17_3903 end

    SaveToFile()

Try(main)
