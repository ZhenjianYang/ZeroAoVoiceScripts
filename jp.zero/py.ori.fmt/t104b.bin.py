from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t104b.bin",                # FileName
        "t104b",                    # MapName
        "t104b",                    # Location
        0x0044,                     # MapIndex
        "ed7513",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 68, 0, 2, 0, 3],
    )

    BuildStringList((
        "t104b",                  # 0
        "リュート",               # 1
        "メーシェ",               # 2
        "娘",                     # 3
        "青年",                   # 4
        "観光客",                 # 5
        "老人",                   # 6
        "老婦人",                 # 7
        "ウィノナ",               # 8
        "ドローナ",               # 9
        "観光客",                 # 10
    ))

    AddCharChip((
        "chr/ch25000.itc",                   # 00
        "chr/ch34500.itc",                   # 01
        "chr/ch21302.itc",                   # 02
        "chr/ch21202.itc",                   # 03
        "chr/ch21602.itc",                   # 04
        "chr/ch33002.itc",                   # 05
        "chr/ch21702.itc",                   # 06
        "chr/ch27900.itc",                   # 07
        "chr/ch26600.itc",                   # 08
        "chr/ch24400.itc",                   # 09
    ))

    DeclNpc(-104069, 0,       2980,    90,   257,  0x0, 0,   0,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(-101099, 0,       5880,    90,   257,  0x0, 0,   1,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(-104949, 0,       8989,    45,   341,  0x0, 0,   2,   0,   255, 255, 0,   7,   255,  0)
    DeclNpc(-102970, 0,       10960,   225,  341,  0x0, 0,   3,   0,   255, 255, 0,   8,   255,  0)
    DeclNpc(-93940,  0,       11039,   225,  341,  0x0, 0,   4,   0,   255, 255, 0,   9,   255,  0)
    DeclNpc(-97919,  0,       18979,   45,   341,  0x0, 0,   5,   0,   255, 255, 0,   10,  255,  0)
    DeclNpc(-97930,  0,       20979,   135,  341,  0x0, 0,   6,   0,   255, 255, 0,   11,  255,  0)
    DeclNpc(-1860,   0,       10640,   180,  257,  0x0, 0,   7,   0,   0,   0,   0,   13,  255,  0)
    DeclNpc(4159,    0,       2349,    0,    257,  0x0, 0,   8,   0,   0,   0,   0,   14,  255,  0)
    DeclNpc(3950,    0,       3309,    270,  257,  0x0, 0,   9,   0,   0,   0,   0,   15,  255,  0)

    DeclActor(-1770,   0,       8810,    1000,    -1860,   1500,    10640,   0x007E, 0,  12, 0x0000)
    DeclActor(-101650, 0,       2470,    1000,    -104070, 1500,    2980,    0x007E, 0,  4,  0x0000)

    ScpFunction((
        "Function_0_260",          # 00, 0
        "Function_1_318",          # 01, 1
        "Function_2_3A1",          # 02, 2
        "Function_3_3A8",          # 03, 3
        "Function_4_3A9",          # 04, 4
        "Function_5_3AD",          # 05, 5
        "Function_6_91E",          # 06, 6
        "Function_7_9A2",          # 07, 7
        "Function_8_B93",          # 08, 8
        "Function_9_D1C",          # 09, 9
        "Function_10_ED9",         # 0A, 10
        "Function_11_1063",        # 0B, 11
        "Function_12_11EB",        # 0C, 12
        "Function_13_11EF",        # 0D, 13
        "Function_14_13E2",        # 0E, 14
        "Function_15_1467",        # 0F, 15
        "Function_16_1523",        # 10, 16
    ))


    def Function_0_260(): pass

    label("Function_0_260")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_2A0"),
        (1, "loc_2AC"),
        (2, "loc_2B8"),
        (3, "loc_2C4"),
        (4, "loc_2D0"),
        (5, "loc_2DC"),
        (6, "loc_2E8"),
        (SWITCH_DEFAULT, "loc_2F4"),
    )


    label("loc_2A0")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_300")

    label("loc_2AC")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_300")

    label("loc_2B8")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_300")

    label("loc_2C4")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_300")

    label("loc_2D0")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_300")

    label("loc_2DC")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_300")

    label("loc_2E8")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_300")

    label("loc_2F4")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_300")

    label("loc_300")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_317")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_300")

    label("loc_317")

    Return()

    # Function_0_260 end

    def Function_1_318(): pass

    label("Function_1_318")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3A0")
    OP_95(0xFE, -98090, 0, 5880, 2000, 0x0)
    OP_95(0xFE, -98090, 0, 12710, 2000, 0x0)
    OP_95(0xFE, -92260, 0, 12710, 2000, 0x0)
    OP_95(0xFE, -92260, 0, 15180, 2000, 0x0)
    OP_95(0xFE, -101100, 0, 15180, 2000, 0x0)
    OP_95(0xFE, -101100, 0, 5880, 2000, 0x0)
    Jump("Function_1_318")

    label("loc_3A0")

    Return()

    # Function_1_318 end

    def Function_2_3A1(): pass

    label("Function_2_3A1")

    BeginChrThread(0x9, 0, 0, 1)
    Return()

    # Function_2_3A1 end

    def Function_3_3A8(): pass

    label("Function_3_3A8")

    Return()

    # Function_3_3A8 end

    def Function_4_3A9(): pass

    label("Function_4_3A9")

    Call(0, 5)
    Return()

    # Function_4_3A9 end

    def Function_5_3AD(): pass

    label("Function_5_3AD")

    TalkBegin(0x8)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3BA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_91A")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_418")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_418")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_438")
    OP_AF(0x66)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_915")

    label("loc_438")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_44C")
    Jump("loc_915")

    label("loc_44C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_915")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_88F")

    #C0001
    ChrTalk(
        0x8,
        (
            "ディナーのお供には\x01",
            "帝国から取り寄せた傑作ワイン\x01",
            "《エル・ヴォワール》をどうぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x8,
        (
            "少々値は張りますが、その芳醇な香りは\x01",
            "かの《グラン・シャリネ》にも\x01",
            "劣らないと言われる代物です。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5D5")

    #C0003
    ChrTalk(
        0x102,
        (
            "#0103F《グラン・シャリネ》……\x01",
            "確かリベール王国で醸造されていた\x01",
            "ヴィンテージワインね。\x02\x03",

            "#0100F数年前にリベール王国内の競売で\x01",
            "５０万ミラの値がついたとか。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_674")

    label("loc_5D5")


    #C0004
    ChrTalk(
        0x102,
        (
            "#5303F《グラン・シャリネ》……\x01",
            "確かリベール王国で醸造されていた\x01",
            "ヴィンテージワインね。\x02\x03",

            "#5300F数年前にリベール王国内の競売で\x01",
            "５０万ミラの値がついたとか。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_674")


    #C0005
    ChrTalk(
        0x101,
        (
            "#5005Fご、５０万ミラ……！？\x01",
            "ワイン１本にそんな値段が……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6E4")

    #C0006
    ChrTalk(
        0x103,
        "#0203F理解しがたい世界です。\x02",
    )

    CloseMessageWindow()
    Jump("loc_706")

    label("loc_6E4")


    #C0007
    ChrTalk(
        0x103,
        "#5403F理解しがたい世界です。\x02",
    )

    CloseMessageWindow()

    label("loc_706")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_76E")

    #C0008
    ChrTalk(
        0x104,
        (
            "#0304Fそんなに美味いなら\x01",
            "是非とも飲んでみたいもんだな。\x02\x03",

            "#0309Fどれ、試しに一杯……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7C7")

    label("loc_76E")


    #C0009
    ChrTalk(
        0x104,
        (
            "#5604Fそんなに美味いなら\x01",
            "是非とも飲んでみたいもんだな。\x02\x03",

            "#5609Fどれ、試しに一杯……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7F6")

    #C0010
    ChrTalk(
        0x103,
        "#0211F…………………………\x02",
    )

    CloseMessageWindow()
    Jump("loc_816")

    label("loc_7F6")


    #C0011
    ChrTalk(
        0x103,
        "#5411F…………………………\x02",
    )

    CloseMessageWindow()

    label("loc_816")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_849")

    #C0012
    ChrTalk(
        0x104,
        "#0306F……じょ、冗談だっつの！\x02",
    )

    CloseMessageWindow()
    Jump("loc_86D")

    label("loc_849")


    #C0013
    ChrTalk(
        0x104,
        "#5606F……じょ、冗談だっつの！\x02",
    )

    CloseMessageWindow()

    label("loc_86D")


    #C0014
    ChrTalk(
        0x101,
        "#5003F分かればよし。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_915")

    label("loc_88F")


    #C0015
    ChrTalk(
        0x8,
        (
            "《エル・ヴォワール》は\x01",
            "かの《グラン・シャリネ》にも\x01",
            "劣らないと言われる傑作ワインです。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x8,
        "よろしければディナーのお供にどうぞ。\x02",
    )

    CloseMessageWindow()

    label("loc_915")

    Jump("loc_3BA")

    label("loc_91A")

    TalkEnd(0x8)
    Return()

    # Function_5_3AD end

    def Function_6_91E(): pass

    label("Function_6_91E")

    TalkBegin(0xFE)

    #C0017
    ChrTalk(
        0xFE,
        (
            "そういえば……\x01",
            "今日で記念祭も終わりなのよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0xFE,
        (
            "街のほうは\x01",
            "随分盛り上がったらしいけど……\x01",
            "ううん、行きたかったなぁ。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_6_91E end

    def Function_7_9A2(): pass

    label("Function_7_9A2")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A36")
    Jump("loc_A80")

    label("loc_A36")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_A56")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A80")

    label("loc_A56")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A76")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A80")

    label("loc_A76")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A80")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B3A")

    #C0019
    ChrTalk(
        0xFE,
        "ぱくぱく……\x02",
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0xFE,
        "もぐもぐ……\x02",
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0xFE,
        "んん！　絶品ねぇこの料理は！\x02",
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0xFE,
        (
            "宝石を買えなかった怒りは\x01",
            "何処かに飛んで行っちゃったわ！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_B8B")

    label("loc_B3A")


    #C0023
    ChrTalk(
        0xFE,
        "まむまむ……ごきゅっ。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x2)

    #C0024
    ChrTalk(
        0xFE,
        (
            "……すいませーん、\x01",
            "おかわりお願いしますー㈱\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B8B")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_7_9A2 end

    def Function_8_B93(): pass

    label("Function_8_B93")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_C27")
    Jump("loc_C71")

    label("loc_C27")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_C47")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_C71")

    label("loc_C47")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C67")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_C71")

    label("loc_C67")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_C71")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CED")

    #C0025
    ChrTalk(
        0xFE,
        "ま……まだ食べるのかい？\x02",
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0xFE,
        (
            "ちょ、貯金が……\x01",
            "僕の全財産が……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_D14")

    label("loc_CED")


    #C0027
    ChrTalk(
        0xFE,
        (
            "ちょ、貯金が……\x01",
            "僕の全財産が……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D14")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_8_B93 end

    def Function_9_D1C(): pass

    label("Function_9_D1C")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_DB0")
    Jump("loc_DFA")

    label("loc_DB0")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_DD0")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_DFA")

    label("loc_DD0")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_DF0")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_DFA")

    label("loc_DF0")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_DFA")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E7F")

    #C0028
    ChrTalk(
        0xFE,
        "ごちそうさまでした。\x02",
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0xFE,
        (
            "ふぅ……\x01",
            "美味い料理に出会えて\x01",
            "満足、満足じゃ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_ED1")

    label("loc_E7F")


    #C0030
    ChrTalk(
        0xFE,
        (
            "美味い料理に出会えた。\x01",
            "わざわざクロスベルくんだりまで\x01",
            "来た甲斐があったわい。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_ED1")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_9_D1C end

    def Function_10_ED9(): pass

    label("Function_10_ED9")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_F6D")
    Jump("loc_FB7")

    label("loc_F6D")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_F8D")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_FB7")

    label("loc_F8D")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_FAD")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_FB7")

    label("loc_FAD")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_FB7")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0031
    ChrTalk(
        0xFE,
        (
            "おっと……\x01",
            "そろそろ議長邸のパーティが\x01",
            "始まる時間だな。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0xFE,
        (
            "妻は初めて連れて行くからね。\x01",
            "気に入ってくれるといいのだが……\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_10_ED9 end

    def Function_11_1063(): pass

    label("Function_11_1063")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_10F7")
    Jump("loc_1141")

    label("loc_10F7")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1117")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1141")

    label("loc_1117")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1137")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1141")

    label("loc_1137")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1141")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0033
    ChrTalk(
        0xFE,
        (
            "夫が今夜、\x01",
            "このミシュラムでのパーティに\x01",
            "連れて行ってくれるそうなの。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0xFE,
        (
            "ふふ、楽しみだわ。\x01",
            "どんなパーティなのかしら。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_11_1063 end

    def Function_12_11EB(): pass

    label("Function_12_11EB")

    Call(0, 13)
    Return()

    # Function_12_11EB end

    def Function_13_11EF(): pass

    label("Function_13_11EF")

    TalkBegin(0xF)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_11FC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13DE")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_125A")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_125A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_127A")
    OP_AF(0x69)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_13D9")

    label("loc_127A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_128E")
    Jump("loc_13D9")

    label("loc_128E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13D9")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1398")

    #C0035
    ChrTalk(
        0xF,
        "お客様、良くお似合いですよ。\x02",
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0xF,
        (
            "最近の流行を取り入れながらも\x01",
            "それが下品に見えない\x01",
            "整った組み合わせ……\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0xF,
        (
            "ワジ様のコーディネイトには\x01",
            "プロである私どもも形無しですわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x101,
        "#5005F（あいつ……本当に何者なんだ……？）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_13D9")

    label("loc_1398")


    #C0039
    ChrTalk(
        0xF,
        (
            "ワジ様のコーディネイトには\x01",
            "プロである私どもも形無しですわ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13D9")

    Jump("loc_11FC")

    label("loc_13DE")

    TalkEnd(0xF)
    Return()

    # Function_13_11EF end

    def Function_14_13E2(): pass

    label("Function_14_13E2")

    TalkBegin(0xFE)
    TurnDirection(0x10, 0x11, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13FE")
    Call(0, 16)
    Jump("loc_1463")

    label("loc_13FE")


    #C0040
    ChrTalk(
        0xFE,
        "お客様のお気に召しませんか……\x02",
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0xFE,
        (
            "それなら、趣向を変えて\x01",
            "こちらのハットなどはいかがでしょう？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1463")

    TalkEnd(0xFE)
    Return()

    # Function_14_13E2 end

    def Function_15_1467(): pass

    label("Function_15_1467")

    TalkBegin(0xFE)
    OP_93(0xFE, 0x10E, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1483")
    Call(0, 16)
    Jump("loc_151F")

    label("loc_1483")


    #C0042
    ChrTalk(
        0xFE,
        (
            "（こ、困った……\x01",
            "  適当に冷やかして\x01",
            "  帰ろうと思ってたのに……）\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0xFE,
        (
            "（こんなに話しかけられると\x01",
            "  何も買わずに出るのが\x01",
            "  申し訳ないじゃないか……！）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_151F")

    TalkEnd(0xFE)
    Return()

    # Function_15_1467 end

    def Function_16_1523(): pass

    label("Function_16_1523")

    OP_4B(0x10, 0xFF)
    OP_4B(0x11, 0xFF)

    #C0044
    ChrTalk(
        0x10,
        (
            "そうですね……\x01",
            "お客様はラフな格好が\x01",
            "お好みのようですし……\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x10,
        (
            "こちらの帽子など\x01",
            "お似合いになるかとおもいますよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x11,
        (
            "え、えっと……\x01",
            "今回はいいかなぁ～……\x01",
            "なんて……\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x10, 0xFF)
    OP_4C(0x11, 0xFF)
    SetScenarioFlags(0x0, 5)
    Return()

    # Function_16_1523 end

    SaveToFile()

Try(main)
