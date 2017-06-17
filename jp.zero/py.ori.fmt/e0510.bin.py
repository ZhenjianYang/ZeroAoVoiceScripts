from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "e0510.bin",                # FileName
        "e0510",                    # MapName
        "e0510",                    # Location
        0x00A1,                     # MapIndex
        "ed7104",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 161, 0, 1, 0, 2],
    )

    BuildStringList((
        "e0510",                  # 0
        "キリカ",                 # 1
        "乗組員サルサ",           # 2
        "娘",                     # 3
        "青年",                   # 4
        "男性",                   # 5
        "青年",                   # 6
        "観光客",                 # 7
    ))

    AddCharChip((
        "chr/ch07302.itc",                   # 00
        "chr/ch28400.itc",                   # 01
        "chr/ch21302.itc",                   # 02
        "chr/ch21202.itc",                   # 03
        "chr/ch27702.itc",                   # 04
        "chr/ch23602.itc",                   # 05
        "chr/ch26702.itc",                   # 06
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

    DeclNpc(0,       -899,    7349,    0,    341,  0x0, 0,   0,   0,   255, 255, 0,   3,   255,  0)
    DeclNpc(-100,    0,       -15420,  0,    257,  0x0, 0,   1,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(-3660,   150,     -8829,   180,  341,  0x0, 0,   2,   0,   255, 255, 0,   5,   255,  0)
    DeclNpc(-2450,   150,     -8829,   180,  341,  0x0, 0,   3,   0,   255, 255, 0,   6,   255,  0)
    DeclNpc(3049,    150,     -6349,   180,  341,  0x0, 0,   4,   0,   255, 255, 0,   7,   255,  0)
    DeclNpc(-2450,   150,     -3799,   180,  341,  0x0, 0,   5,   0,   255, 255, 0,   8,   255,  0)
    DeclNpc(2180,    150,     -8829,   180,  341,  0x0, 0,   6,   0,   255, 255, 0,   9,   255,  0)

    ScpFunction((
        "Function_0_204",          # 00, 0
        "Function_1_299",          # 01, 1
        "Function_2_2BF",          # 02, 2
        "Function_3_2C6",          # 03, 3
        "Function_4_553",          # 04, 4
        "Function_5_689",          # 05, 5
        "Function_6_871",          # 06, 6
        "Function_7_A5C",          # 07, 7
        "Function_8_BD1",          # 08, 8
        "Function_9_DE1",          # 09, 9
        "Function_10_F8A",         # 0A, 10
        "Function_11_125A",        # 0B, 11
        "Function_12_1F80",        # 0C, 12
    ))


    def Function_0_204(): pass

    label("Function_0_204")

    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4B), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_227")
    Sleep(600)
    Jump("loc_250")

    label("loc_227")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_23E")
    Sleep(400)
    Jump("loc_250")

    label("loc_23E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x19), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_250")
    Sleep(200)

    label("loc_250")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_298")
    SetChrSubChip(0xFE, 0x0)
    Sleep(100)
    SetChrSubChip(0xFE, 0x1)
    Sleep(100)
    SetChrSubChip(0xFE, 0x2)
    Sleep(100)
    SetChrSubChip(0xFE, 0x1)
    Sleep(100)
    SetChrSubChip(0xFE, 0x0)
    Sleep(100)
    SetChrSubChip(0xFE, 0x3)
    Sleep(100)
    SetChrSubChip(0xFE, 0x4)
    Sleep(100)
    SetChrSubChip(0xFE, 0x3)
    Sleep(100)
    Jump("loc_250")

    label("loc_298")

    Return()

    # Function_0_204 end

    def Function_1_299(): pass

    label("Function_1_299")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2AF")
    Event(0, 12)

    label("loc_2AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_2BE")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 10)

    label("loc_2BE")

    Return()

    # Function_1_299 end

    def Function_2_2BF(): pass

    label("Function_2_2BF")

    Sound(480, 1, 100, 0)
    Return()

    # Function_2_2BF end

    def Function_3_2C6(): pass

    label("Function_3_2C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2DC")
    Call(0, 11)
    Jump("loc_552")

    label("loc_2DC")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0x8)
    ClearChrFlags(0x8, 0x10)
    TurnDirection(0x8, 0x0, 0)
    OP_52(0x8, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_370")
    Jump("loc_3BA")

    label("loc_370")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_390")
    OP_52(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3BA")

    label("loc_390")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3B0")
    OP_52(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3BA")

    label("loc_3B0")

    OP_52(0x8, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3BA")

    OP_52(0x8, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x8, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_518")

    #C0001
    ChrTalk(
        0x8,
        (
            "#3404Fフフ、いきなり難しい話を\x01",
            "してしまったわね。\x02\x03",

            "#3400F折角の保養地……\x01",
            "私はヤボ用があるけど、\x01",
            "あなた達は存分に楽しむといいわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x104,
        "#0309Fモチのロンっす！\x02",
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0x103,
        (
            "#0211F（……ランディさん、\x01",
            "  目的をお忘れですか？）\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x104,
        (
            "#0306F（わ、分かってるっつーの。\x01",
            "  そんな目で見んなよティオすけ……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_54B")

    label("loc_518")


    #C0005
    ChrTalk(
        0x8,
        (
            "#3400F折角の保養地……\x01",
            "存分に楽しむといいわ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_54B")

    SetChrSubChip(0x8, 0x0)
    TalkEnd(0x8)

    label("loc_552")

    Return()

    # Function_3_2C6 end

    def Function_4_553(): pass

    label("Function_4_553")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_600")

    #C0006
    ChrTalk(
        0xFE,
        (
            "お客様、水上バスは\x01",
            "初めてでしょうか？\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0xFE,
        (
            "ミシュラムまでの短い一時ですが\x01",
            "波に揺られる穏やかな旅を\x01",
            "お楽しみくださいませ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB5, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5FB")
    SetScenarioFlags(0xB5, 2)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5FB")

    Jump("loc_685")

    label("loc_600")


    #C0008
    ChrTalk(
        0xFE,
        (
            "……もしかして\x01",
            "酔ってしまいましたか？\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0xFE,
        (
            "酔い止め薬も常備いたしておりますので\x01",
            "ご気分のすぐれない方は\x01",
            "声をお掛けくださいませ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_685")

    TalkEnd(0xFE)
    Return()

    # Function_4_553 end

    def Function_5_689(): pass

    label("Function_5_689")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_71D")
    Jump("loc_767")

    label("loc_71D")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_73D")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_767")

    label("loc_73D")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_75D")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_767")

    label("loc_75D")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_767")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_810")

    #C0010
    ChrTalk(
        0xFE,
        "今日は待ちに待ったミシュラム㈱\x02",
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0xFE,
        (
            "ブティックや宝飾店で\x01",
            "とことんお洒落に過ごすの㈱\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB5, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_80B")
    SetScenarioFlags(0xB5, 3)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_80B")

    Jump("loc_869")

    label("loc_810")


    #C0012
    ChrTalk(
        0xFE,
        (
            "今日は彼がたっくさんミラを\x01",
            "持って来てくれたらしいの。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0xFE,
        "ふふ、遊びつくすわよ～㈱\x02",
    )

    CloseMessageWindow()

    label("loc_869")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_5_689 end

    def Function_6_871(): pass

    label("Function_6_871")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_905")
    Jump("loc_94F")

    label("loc_905")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_925")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_94F")

    label("loc_925")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_945")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_94F")

    label("loc_945")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_94F")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9FD")

    #C0014
    ChrTalk(
        0xFE,
        (
            "今日の為に\x01",
            "貯金を全額下ろしてきたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0xFE,
        (
            "……彼女の浪費癖には\x01",
            "充分注意しないとね……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB5, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9F8")
    SetScenarioFlags(0xB5, 4)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_9F8")

    Jump("loc_A54")

    label("loc_9FD")


    #C0016
    ChrTalk(
        0xFE,
        "僕の彼女は浪費癖があってね。\x02",
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0xFE,
        (
            "この貯金を全部使うハメに\x01",
            "ならなきゃいいけど……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A54")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_6_871 end

    def Function_7_A5C(): pass

    label("Function_7_A5C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B66")

    #C0018
    ChrTalk(
        0xFE,
        (
            "ふっふっふ……\x01",
            "今夜のために資金を\x01",
            "増やしてきたのじゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0xFE,
        (
            "予算が足りずに目当ての商品を\x01",
            "手に入れられなかった屈辱……\x01",
            "今回こそ晴らしてやるわい。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x101,
        (
            "#0001F（どうやらこの人も\x01",
            "  黒の競売会の\x01",
            "  招待客みたいだな……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB5, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B61")
    SetScenarioFlags(0xB5, 5)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_B61")

    Jump("loc_BCD")

    label("loc_B66")


    #C0021
    ChrTalk(
        0xFE,
        (
            "ふっふっふ……\x01",
            "今夜のために資金を\x01",
            "増やしてきたのじゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0xFE,
        (
            "噂の商品……\x01",
            "必ず落としてくれるわい。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BCD")

    TalkEnd(0xFE)
    Return()

    # Function_7_A5C end

    def Function_8_BD1(): pass

    label("Function_8_BD1")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_C65")
    Jump("loc_CAF")

    label("loc_C65")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_C85")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_CAF")

    label("loc_C85")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_CA5")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_CAF")

    label("loc_CA5")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_CAF")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D9A")

    #C0023
    ChrTalk(
        0xFE,
        (
            "テーマパークを楽しみに来たんだ。\x01",
            "パンフレットも持ったし準備万端だよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0xFE,
        (
            "……別に男一人で来てもいいだろ？\x01",
            "僕は純粋にテーマパークを\x01",
            "楽しみたいんだ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB5, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D95")
    SetScenarioFlags(0xB5, 6)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_D95")

    Jump("loc_DD9")

    label("loc_D9A")


    #C0025
    ChrTalk(
        0xFE,
        (
            "……何？　テーマパークに\x01",
            "男一人で行っちゃ悪いってのかい？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DD9")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_8_BD1 end

    def Function_9_DE1(): pass

    label("Function_9_DE1")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_E75")
    Jump("loc_EBF")

    label("loc_E75")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_E95")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_EBF")

    label("loc_E95")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_EB5")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_EBF")

    label("loc_EB5")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_EBF")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0026
    ChrTalk(
        0xFE,
        (
            "なぁ、見たか？\x01",
            "後ろの方に座ってるあの美人……\x01",
            "パンツルックが絶妙だよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0xFE,
        (
            "くぅ、たまんねぇぜ。\x01",
            "やっぱ来た甲斐があったなぁ。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB5, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F82")
    SetScenarioFlags(0xB5, 7)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_F82")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_9_DE1 end

    def Function_10_F8A(): pass

    label("Function_10_F8A")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch00102.itc", 0x1F)
    LoadChrToIndex("chr/ch00202.itc", 0x20)
    LoadChrToIndex("chr/ch00302.itc", 0x21)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x104, 0x0)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x103, 0x4)
    SetChrFlags(0x104, 0x4)
    SetChrPos(0x102, 3000, 150, -13830, 180)
    SetChrPos(0x101, 2120, 150, -13830, 180)
    SetChrPos(0x103, 3120, 150, -11330, 180)
    SetChrPos(0x104, 2120, 150, -11330, 180)
    OP_68(-600, 1100, -8060, 0)
    MoveCamera(45, 14, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(18500, 0)
    FadeToBright(1000, 0)
    OP_68(2560, 1100, -12450, 8000)
    OP_6F(0x1)
    OP_0D()
    SetChrSubChip(0x101, 0x2)
    Sleep(300)

    #C0028
    ChrTalk(
        0x101,
        (
            "#0000F#5P水上バスか……\x02\x03",

            "初めて乗ったけど\x01",
            "けっこう豪華な内装だな。\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x2)

    #C0029
    ChrTalk(
        0x102,
        (
            "#0104F#11Pふふ、バスと違ってＩＢＣが\x01",
            "全面的に運営しているから。\x02\x03",

            "#0102F乗船料も基本的にタダだしね。\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x103,
        "#0205F#5P太っ腹ですね、それは……\x02",
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x104,
        (
            "#0304F#5Pまあ、ミラを持ってないと\x01",
            "行った先で何も出来ねぇけどな。\x02\x03",

            "#0300F到着まで２０分くらい……\x01",
            "適当にノンビリするとしようぜ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x103, 0x4)
    SetChrFlags(0x104, 0x4)
    OP_49()
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_D5(0x20)
    OP_D5(0x21)
    SetChrPos(0x0, -200, 0, -11700, 0)
    SetScenarioFlags(0xA3, 5)
    OP_29(0x44, 0x4, 0x10)
    OP_29(0x47, 0x4, 0x2)
    OP_29(0x47, 0x1, 0x0)
    OP_D0(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_10_F8A end

    def Function_11_125A(): pass

    label("Function_11_125A")

    EventBegin(0x0)
    Fade(1000)
    OP_68(1260, 300, 7490, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18060, 0)
    SetCameraDistance(17060, 2000)
    SetChrPos(0x101, 1890, -1000, 8970, 225)
    SetChrPos(0x102, 2920, -1000, 8620, 225)
    SetChrPos(0x103, 2580, -1000, 7410, 270)
    SetChrPos(0x104, 3530, -1000, 7820, 270)
    SetChrSubChip(0x8, 0x2)
    OP_6F(0x10)
    OP_0D()

    #C0032
    ChrTalk(
        0x8,
        (
            "#3404F#6Pミシュラム……\x01",
            "なかなか興味深い場所ね。\x02\x03",

            "#3400Fもう少し時間があったら\x01",
            "テーマパークにも寄りたいのだけど。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0033
    ChrTalk(
        0x101,
        (
            "#0005F#5Pえっと……テーマパークに\x01",
            "用があるんじゃないんですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x8,
        (
            "#3404F#6Pええ、ヤボ用があってね。\x02\x03",

            "#3400Fまあ、クロスベルに来るのは\x01",
            "これで最後ではないでしょうし……\x02\x03",

            "またの機会にゆっくり訪ねるわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x102,
        "#0109F#5Pふふ、是非そうされてください。\x02",
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x104,
        (
            "#0300F#11Pそういえば……\x01",
            "アルカンシェルの新作は\x01",
            "どうだったッスか？\x02\x03",

            "確か昨日、見たんですよね？\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x8,
        (
            "#3404F#6Pええ、夜の部にね。\x02\x03",

            "#3402F私も色々な舞台を\x01",
            "見てきたつもりだけど……\x02\x03",

            "あんな奇跡的なバランスで\x01",
            "成立しているステージは\x01",
            "初めて見たかもしれないわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x103,
        "#0205F#11P奇跡的なバランス……ですか。\x02",
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x8,
        (
            "#3400F#6P脚本、演出、衣装、音楽……\x02\x03",

            "そして派手な舞台装置に\x01",
            "アクロバティックなパフォーマンス……\x02\x03",

            "どれも極めて質は高いけれど\x01",
            "他の名だたる劇場と比較しても\x01",
            "ズバ抜けている程ではないわ。\x02\x03",

            "#3404Fでも、イリア・プラティエ……\x02\x03",

            "彼女の存在が核となって\x01",
            "個々の要素が有機的に結びついた時、\x01",
            "舞台が生き物のようになるのね。\x02\x03",

            "#3402Fまるで生命の誕生に\x01",
            "立ち会った気分にさせられたわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x101,
        "#0002F#5Pなるほど……\x02",
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x102,
        (
            "#0104F#5P生命の誕生……\x01",
            "まさに奇跡かもしれませんね。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x104,
        (
            "#0309F#11Pいや～！\x01",
            "さすが芸能プロデューサー！\x02\x03",

            "言われてみれば\x01",
            "確かにその通りッスよ！\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x8,
        (
            "#3404F#6Pふふ……\x02\x03",

            "ただ、今回の新作については\x01",
            "奇跡の立役者はもう一人いるわ。\x02\x03",

            "#3400F《月の姫》演じる\x01",
            "大型新人、リーシャ・マオ。\x02\x03",

            "死の気配を漂わせる彼女の存在が、\x01",
            "舞台をさらに高みへ押し上げている。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0044
    ChrTalk(
        0x101,
        "#0005F#5Pリーシャが……？\x02",
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x102,
        "#0105F#5P死の気配……ですか？\x02",
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x8,
        (
            "#3400F#6Pあくまで私の直感だけどね。\x02\x03",

            "#3404F太陽と月、金と銀、光と闇、\x01",
            "そして生と死……\x02\x03",

            "彼女とイリア・プラティエは\x01",
            "見事なまでに対照的な\x01",
            "“気”を纏#2Rまと#っているわ。\x02\x03",

            "#3400Fまさに『陰陽』『太極』を\x01",
            "２人で体現していると言えるわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x103,
        "#0205F#11P『陰陽』『太極』……\x02",
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x104,
        (
            "#0300F#11Pたしか東方武術で\x01",
            "使われてる概念でしたっけ？\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x8,
        (
            "#3400F#6Pフフ……\x01",
            "別に武術限定ではないけれど。\x02\x03",

            "#3404Fただ、彼女たちが出会ったのは\x01",
            "まさに運命的な偶然でしょうね。\x02\x03",

            "そして、それを導いたのが\x01",
            "クロスベルという都市が持っている\x01",
            "“場”の特異性……\x02\x03",

            "#3400Fそんな風に言えるかもしれない。\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x101,
        "#0001F#5P運命を導く“場”……\x02",
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x102,
        (
            "#0103F#5P……難しい話ですけど\x01",
            "何となく判るような気もします。\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x8,
        (
            "#3404F#6Pまあそんなに\x01",
            "真剣に捉えなくてもいいわ。\x02\x03",

            "#3400Fただ、アルカンシェルの魅力は\x01",
            "クロスベルという都市そのものと\x01",
            "密接に関わっている所がある。\x02\x03",

            "そのあたりに注意しないと\x01",
            "自治州以外での公演は\x01",
            "上手く行かないかもしれないわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x103,
        (
            "#0205F#11Pでは、共和国での公演は\x01",
            "白紙に戻すつもりとか……？\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x8,
        (
            "#3402F#6Pいえ、それは勿体ないわ。\x02\x03",

            "クロスベル以外でも\x01",
            "アルカンシェルの魅力を\x01",
            "引き出す方法はあるはずよ。\x02\x03",

            "#3404F今後の交渉にあたっては\x01",
            "そのあたりのプランニングが\x01",
            "口説く鍵になるでしょうね。\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x103,
        "#0202F#11Pなるほど……\x02",
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x104,
        (
            "#0302F#11P凄いッスね……\x01",
            "そこまで考えてるなんて。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x8,
        (
            "#3404F#6Pフフ、これでもプロだから。\x02\x03",

            "#3400F自分なりに本質を見抜き、\x01",
            "あるべき目標と状況を設定し、\x01",
            "それに至るための手段を考える。\x02\x03",

            "どのような仕事であれ、\x01",
            "それがプロの流儀というものよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x101,
        (
            "#0000F#5Pプロの流儀……\x01",
            "なるほど、勉強になります。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x102,
        (
            "#0109F#5Pふふ、私たちにとっても\x01",
            "必要な心構えかもしれないわね。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, 2970, -1000, 6660, 180)
    SetScenarioFlags(0xA3, 7)
    SetChrSubChip(0x8, 0x0)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    EventEnd(0x5)
    Return()

    # Function_11_125A end

    def Function_12_1F80(): pass

    label("Function_12_1F80")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_D0(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToBright(1000, 0)
    OP_0D()
    Sound(801, 0, 100, 0)
    Sleep(500)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("女性の声")

    #A0060
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "──お待たせしました。\x02",
        )
    )

    CloseMessageWindow()

    #A0061
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "当水上バスはまもなく\x01",
            "《ミシュラム》に到着いたします。\x02",
        )
    )

    CloseMessageWindow()

    #A0062
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "どなた様もお忘れ物のないよう\x01",
            "お気をつけてお降りになって下さい。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    OP_25(0x1E0, 0x5A)
    Sleep(100)
    OP_25(0x1E0, 0x50)
    Sleep(100)
    OP_25(0x1E0, 0x46)
    Sleep(100)
    OP_25(0x1E0, 0x3C)
    Sleep(100)
    OP_25(0x1E0, 0x32)
    Sleep(100)
    OP_25(0x1E0, 0x28)
    Sleep(100)
    OP_25(0x1E0, 0x1E)
    Sleep(100)
    OP_25(0x1E0, 0x14)
    Sleep(100)
    OP_25(0x1E0, 0xA)
    Sleep(100)
    OP_25(0x1E0, 0x0)
    WaitBGM()
    SetScenarioFlags(0x5C, 0)
    NewScene("t1000", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_12_1F80 end

    SaveToFile()

Try(main)
