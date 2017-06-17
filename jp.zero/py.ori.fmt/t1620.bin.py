from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t1620.bin",                # FileName
        "t1620",                    # MapName
        "t1620",                    # Location
        0x0055,                     # MapIndex
        "ed7123",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 85, 0, 1, 0, 2],
    )

    BuildStringList((
        "t1620",                  # 0
    ))

    AddCharChip((
        "chr/ch29400.itc",                   # 00
        "chr/ch29200.itc",                   # 01
    ))

    DeclActor(-3000,   0,       64599,   1000,    -3000,   1200,    64599,   0x007C, 0,  5,  0x0000)
    DeclActor(-880,    0,       62400,   1000,    -880,    1200,    62400,   0x007C, 0,  6,  0x0000)
    DeclActor(-880,    0,       58300,   1000,    -880,    1200,    58300,   0x007C, 0,  7,  0x0000)
    DeclActor(880,     0,       58300,   1000,    880,     1200,    58300,   0x007C, 0,  8,  0x0000)
    DeclActor(880,     0,       62400,   1000,    880,     1200,    62400,   0x007C, 0,  9,  0x0000)
    DeclActor(3000,    0,       64599,   1000,    3000,    1200,    64599,   0x007C, 0,  10, 0x0000)
    DeclActor(5100,    0,       62400,   1000,    5100,    1200,    62400,   0x007C, 0,  4,  0x0000)
    DeclActor(5100,    0,       58300,   1000,    5100,    1200,    58300,   0x007C, 0,  11, 0x0000)
    DeclActor(6940,    0,       58300,   1000,    6940,    1200,    58300,   0x007C, 0,  12, 0x0000)
    DeclActor(6940,    0,       62400,   1000,    6940,    1200,    62400,   0x007C, 0,  13, 0x0000)
    DeclActor(9000,    0,       64599,   1000,    9000,    1200,    64599,   0x007C, 0,  14, 0x0000)
    DeclActor(11500,   0,       62400,   1000,    11500,   1200,    62400,   0x007C, 0,  15, 0x0000)
    DeclActor(11500,   0,       55800,   1000,    11500,   1200,    55800,   0x007C, 0,  16, 0x0000)

    ScpFunction((
        "Function_0_2B8",          # 00, 0
        "Function_1_370",          # 01, 1
        "Function_2_393",          # 02, 2
        "Function_3_3B0",          # 03, 3
        "Function_4_7AD",          # 04, 4
        "Function_5_BF4",          # 05, 5
        "Function_6_CA8",          # 06, 6
        "Function_7_D5C",          # 07, 7
        "Function_8_E10",          # 08, 8
        "Function_9_EC4",          # 09, 9
        "Function_10_F78",         # 0A, 10
        "Function_11_102C",        # 0B, 11
        "Function_12_10E0",        # 0C, 12
        "Function_13_1194",        # 0D, 13
        "Function_14_1248",        # 0E, 14
        "Function_15_12FC",        # 0F, 15
        "Function_16_13B0",        # 10, 16
        "Function_17_1464",        # 11, 17
    ))


    def Function_0_2B8(): pass

    label("Function_0_2B8")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_2F8"),
        (1, "loc_304"),
        (2, "loc_310"),
        (3, "loc_31C"),
        (4, "loc_328"),
        (5, "loc_334"),
        (6, "loc_340"),
        (SWITCH_DEFAULT, "loc_34C"),
    )


    label("loc_2F8")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_358")

    label("loc_304")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_358")

    label("loc_310")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_358")

    label("loc_31C")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_358")

    label("loc_328")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_358")

    label("loc_334")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_358")

    label("loc_340")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_358")

    label("loc_34C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_358")

    label("loc_358")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_36F")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_358")

    label("loc_36F")

    Return()

    # Function_0_2B8 end

    def Function_1_370(): pass

    label("Function_1_370")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x72), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0x8)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0x9)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_392")
    Event(0, 3)

    label("loc_392")

    Return()

    # Function_1_370 end

    def Function_2_393(): pass

    label("Function_2_393")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3AA")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)

    label("loc_3AA")

    OP_1B(0xE, 0x0, 0x11)
    Return()

    # Function_2_393 end

    def Function_3_3B0(): pass

    label("Function_3_3B0")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(250, 1000, 52660, 0)
    MoveCamera(45, 28, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(20000, 0)
    SetChrPos(0x101, 0, 0, 52500, 0)
    SetChrPos(0x102, 1200, 0, 52500, 0)
    SetChrPos(0x103, 0, 0, 51300, 0)
    SetChrPos(0x104, 1200, 0, 51300, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_45E")
    SetChrPos(0x109, -1200, 0, 51900, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    Jump("loc_489")

    label("loc_45E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_489")
    SetChrPos(0x10A, -1200, 0, 51900, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    label("loc_489")

    FadeToBright(500, 0)
    OP_0D()

    #C0001
    ChrTalk(
        0x101,
        (
            "#12P#0000Fここが資料室か……\x02\x03",

            "どうやらフローラさんは\x01",
            "この本棚の中に延滞本を\x01",
            "紛れさせてしまったみたいだな。\x02",
        )
    )

    CloseMessageWindow()
    OP_68(2900, 1000, 60120, 4000)
    MoveCamera(45, 19, 0, 4000)
    OP_6E(440, 4000)
    SetCameraDistance(28640, 4000)
    OP_6F(0x79)
    Fade(500)
    OP_68(250, 1000, 52660, 0)
    MoveCamera(45, 28, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(20000, 0)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5EF")
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_5EF")

    Sleep(1000)

    #C0002
    ChrTalk(
        0x101,
        (
            "#12P#0006Fう、うーん。\x01",
            "改めて見るとすごい量だな。\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0x102,
        (
            "#12P#0106Fそうねぇ……\x01",
            "さすがに骨が折れそうかも。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x103,
        "#12P#0200Fやってらんないです。\x02",
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x104,
        (
            "#12P#0300Fまー、しらみつぶしに\x01",
            "調べてみるしかねぇだろ。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x101,
        (
            "#12P#0000Fそうだな……\x01",
            "大変そうだけど、\x01",
            "一丁、探してみるか。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_737")

    #C0007
    ChrTalk(
        0x109,
        "#6P#0501Fお手伝いします！\x02",
    )

    CloseMessageWindow()
    Jump("loc_76E")

    label("loc_737")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_76E")

    #C0008
    ChrTalk(
        0x10A,
        "#6P#0603F………………………………\x02",
    )

    CloseMessageWindow()

    label("loc_76E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_793")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)

    label("loc_793")

    SetChrPos(0x0, 0, 0, 52500, 0)
    OP_29(0x28, 0x1, 0x9)
    EventEnd(0x5)
    Return()

    # Function_3_3B0 end

    def Function_4_7AD(): pass

    label("Function_4_7AD")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0009
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x2D8),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x2D8, 1)
    EventBegin(0x0)
    Fade(500)
    OP_68(4520, 1000, 62040, 0)
    MoveCamera(54, 30, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(19850, 0)
    SetChrPos(0x101, 4140, 0, 61890, 90)
    SetChrPos(0x102, 3110, 0, 62550, 90)
    SetChrPos(0x103, 2910, 0, 60910, 45)
    SetChrPos(0x104, 4100, 0, 63510, 135)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8A7")
    SetChrPos(0x109, 4030, 0, 60190, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    Jump("loc_8D2")

    label("loc_8A7")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8D2")
    SetChrPos(0x10A, 4030, 0, 60190, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    label("loc_8D2")

    OP_0D()

    #C0010
    ChrTalk(
        0x101,
        (
            "#5P#0005Fあ、これってもしかして……！\x02\x03",

            "#0000Fうん、図書館のマークが入ってる。\x01",
            "フローラさんが借りてた本に\x01",
            "間違いなさそうだな。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_98C")

    #C0011
    ChrTalk(
        0x109,
        "#12P#0500Fやりましたね、皆さん！\x02",
    )

    CloseMessageWindow()

    label("loc_98C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_A04")

    #C0012
    ChrTalk(
        0x102,
        "#6P#0106Fよ、ようやく見つかったわね……\x02",
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x103,
        (
            "#12P#0211F……いい加減本棚が\x01",
            "嫌いになりそうです。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AE3")

    label("loc_A04")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_A6A")

    #C0014
    ChrTalk(
        0x102,
        (
            "#6P#0100F何とか見つかって\x01",
            "よかったわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x103,
        "#12P#0206F……少し疲れました。\x02",
    )

    CloseMessageWindow()
    Jump("loc_AE3")

    label("loc_A6A")


    #C0016
    ChrTalk(
        0x102,
        (
            "#6P#0100F早いうちに見つかって\x01",
            "ラッキーだったわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x103,
        (
            "#12P#0203F隅から隅まで調べるハメに\x01",
            "ならなくてよかったです。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AE3")


    #C0018
    ChrTalk(
        0x104,
        (
            "#5P#0300Fとりあえず、\x01",
            "これで回収できたワケか。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x10E, 0x1F4)

    #C0019
    ChrTalk(
        0x101,
        (
            "#0000Fああ。\x01",
            "そろそろ行くとしよう。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B92")

    #C0020
    ChrTalk(
        0x10A,
        (
            "#12P#0606F（まったく、こんな所で\x01",
            "  余計な時間を……）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B92")

    OP_29(0x28, 0x1, 0xA)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0x5)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0x7)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0xA)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_BBB")
    OP_29(0x28, 0x1, 0x1F)

    label("loc_BBB")

    FadeToBright(500, 0)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_BEA")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)

    label("loc_BEA")

    NewScene("t1600", 104, 0, 0)
    IdleLoop()
    Return()

    # Function_4_7AD end

    def Function_5_BF4(): pass

    label("Function_5_BF4")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C7D")
    SetChrName("")

    #A0021
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "本棚に収まっている本を\x01",
            "一通り調べた。\x02\x03",

            "……この本棚には\x01",
            "フローラの借りた延滞本は\x01",
            "無いようだ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x0, 0)
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_CA4")

    label("loc_C7D")

    SetChrName("")

    #A0022
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "この本棚には延滞本はない。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_CA4")

    TalkEnd(0xFF)
    Return()

    # Function_5_BF4 end

    def Function_6_CA8(): pass

    label("Function_6_CA8")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D31")
    SetChrName("")

    #A0023
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "本棚に収まっている本を\x01",
            "一通り調べた。\x02\x03",

            "……この本棚には\x01",
            "フローラの借りた延滞本は\x01",
            "無いようだ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x0, 1)
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_D58")

    label("loc_D31")

    SetChrName("")

    #A0024
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "この本棚には延滞本はない。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_D58")

    TalkEnd(0xFF)
    Return()

    # Function_6_CA8 end

    def Function_7_D5C(): pass

    label("Function_7_D5C")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DE5")
    SetChrName("")

    #A0025
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "本棚に収まっている本を\x01",
            "一通り調べた。\x02\x03",

            "……この本棚には\x01",
            "フローラの借りた延滞本は\x01",
            "無いようだ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x0, 2)
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_E0C")

    label("loc_DE5")

    SetChrName("")

    #A0026
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "この本棚には延滞本はない。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_E0C")

    TalkEnd(0xFF)
    Return()

    # Function_7_D5C end

    def Function_8_E10(): pass

    label("Function_8_E10")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E99")
    SetChrName("")

    #A0027
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "本棚に収まっている本を\x01",
            "一通り調べた。\x02\x03",

            "……この本棚には\x01",
            "フローラの借りた延滞本は\x01",
            "無いようだ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x0, 3)
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_EC0")

    label("loc_E99")

    SetChrName("")

    #A0028
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "この本棚には延滞本はない。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_EC0")

    TalkEnd(0xFF)
    Return()

    # Function_8_E10 end

    def Function_9_EC4(): pass

    label("Function_9_EC4")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F4D")
    SetChrName("")

    #A0029
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "本棚に収まっている本を\x01",
            "一通り調べた。\x02\x03",

            "……この本棚には\x01",
            "フローラの借りた延滞本は\x01",
            "無いようだ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x0, 4)
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_F74")

    label("loc_F4D")

    SetChrName("")

    #A0030
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "この本棚には延滞本はない。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_F74")

    TalkEnd(0xFF)
    Return()

    # Function_9_EC4 end

    def Function_10_F78(): pass

    label("Function_10_F78")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1001")
    SetChrName("")

    #A0031
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "本棚に収まっている本を\x01",
            "一通り調べた。\x02\x03",

            "……この本棚には\x01",
            "フローラの借りた延滞本は\x01",
            "無いようだ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x0, 5)
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_1028")

    label("loc_1001")

    SetChrName("")

    #A0032
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "この本棚には延滞本はない。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_1028")

    TalkEnd(0xFF)
    Return()

    # Function_10_F78 end

    def Function_11_102C(): pass

    label("Function_11_102C")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10B5")
    SetChrName("")

    #A0033
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "本棚に収まっている本を\x01",
            "一通り調べた。\x02\x03",

            "……この本棚には\x01",
            "フローラの借りた延滞本は\x01",
            "無いようだ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x0, 6)
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_10DC")

    label("loc_10B5")

    SetChrName("")

    #A0034
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "この本棚には延滞本はない。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_10DC")

    TalkEnd(0xFF)
    Return()

    # Function_11_102C end

    def Function_12_10E0(): pass

    label("Function_12_10E0")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1169")
    SetChrName("")

    #A0035
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "本棚に収まっている本を\x01",
            "一通り調べた。\x02\x03",

            "……この本棚には\x01",
            "フローラの借りた延滞本は\x01",
            "無いようだ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x0, 7)
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_1190")

    label("loc_1169")

    SetChrName("")

    #A0036
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "この本棚には延滞本はない。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_1190")

    TalkEnd(0xFF)
    Return()

    # Function_12_10E0 end

    def Function_13_1194(): pass

    label("Function_13_1194")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_121D")
    SetChrName("")

    #A0037
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "本棚に収まっている本を\x01",
            "一通り調べた。\x02\x03",

            "……この本棚には\x01",
            "フローラの借りた延滞本は\x01",
            "無いようだ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x1, 0)
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_1244")

    label("loc_121D")

    SetChrName("")

    #A0038
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "この本棚には延滞本はない。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_1244")

    TalkEnd(0xFF)
    Return()

    # Function_13_1194 end

    def Function_14_1248(): pass

    label("Function_14_1248")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12D1")
    SetChrName("")

    #A0039
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "本棚に収まっている本を\x01",
            "一通り調べた。\x02\x03",

            "……この本棚には\x01",
            "フローラの借りた延滞本は\x01",
            "無いようだ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x1, 1)
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_12F8")

    label("loc_12D1")

    SetChrName("")

    #A0040
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "この本棚には延滞本はない。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_12F8")

    TalkEnd(0xFF)
    Return()

    # Function_14_1248 end

    def Function_15_12FC(): pass

    label("Function_15_12FC")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1385")
    SetChrName("")

    #A0041
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "本棚に収まっている本を\x01",
            "一通り調べた。\x02\x03",

            "……この本棚には\x01",
            "フローラの借りた延滞本は\x01",
            "無いようだ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x1, 2)
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_13AC")

    label("loc_1385")

    SetChrName("")

    #A0042
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "この本棚には延滞本はない。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_13AC")

    TalkEnd(0xFF)
    Return()

    # Function_15_12FC end

    def Function_16_13B0(): pass

    label("Function_16_13B0")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1439")
    SetChrName("")

    #A0043
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "本棚に収まっている本を\x01",
            "一通り調べた。\x02\x03",

            "……この本棚には\x01",
            "フローラの借りた延滞本は\x01",
            "無いようだ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x1, 3)
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_1460")

    label("loc_1439")

    SetChrName("")

    #A0044
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "この本棚には延滞本はない。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_1460")

    TalkEnd(0xFF)
    Return()

    # Function_16_13B0 end

    def Function_17_1464(): pass

    label("Function_17_1464")

    EventBegin(0x1)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuCmd(0, 0)
    MenuCmd(1, 0, "【研究棟から出る】")
    FadeToDark(300, 0, 100)
    OP_0D()
    MenuCmd(1, 0, "やめる")
    MenuCmd(2, 0, -1, -1, 0)
    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_14D2"),
        (1, "loc_14E1"),
        (2, "loc_150E"),
        (SWITCH_DEFAULT, "loc_151D"),
    )


    label("loc_14D2")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_151D")

    label("loc_14E1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14FF")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1509")

    label("loc_14FF")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1509")

    Jump("loc_151D")

    label("loc_150E")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_151D")

    label("loc_151D")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_END)),
        (0, "loc_1539"),
        (1, "loc_1646"),
        (2, "loc_1661"),
        (SWITCH_DEFAULT, "loc_167C"),
    )


    label("loc_1539")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_15ED")

    #C0045
    ChrTalk(
        0x101,
        (
            "#0005Fおっと……ヨアヒム先生が\x01",
            "いるかどうか判らないし、\x01",
            "一応受付で確認してみよう。\x02\x03",

            "#0000F部外者が無断で\x01",
            "入っていい所でもないしな。\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, 0, 0, 50500, 0)
    EventEnd(0x4)
    Jump("loc_167C")

    label("loc_15ED")

    FadeToDark(1000, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1617")
    SetScenarioFlags(0x5C, 0)
    NewScene("t1650", 101, 0, 0)
    IdleLoop()
    Jump("loc_1641")

    label("loc_1617")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1636")
    SetScenarioFlags(0x5C, 1)
    NewScene("t1650", 101, 0, 0)
    IdleLoop()
    Jump("loc_1641")

    label("loc_1636")

    EventEnd(0x5)
    NewScene("t1650", 101, 0, 0)
    IdleLoop()

    label("loc_1641")

    Jump("loc_167C")

    label("loc_1646")

    FadeToDark(1000, 0, -1)
    OP_0D()
    EventEnd(0x5)
    NewScene("t1600", 104, 0, 0)
    IdleLoop()
    Jump("loc_167C")

    label("loc_1661")

    Sleep(50)
    SetChrPos(0x0, 0, 0, 50500, 0)
    EventEnd(0x4)
    Jump("loc_167C")

    label("loc_167C")

    Return()

    # Function_17_1464 end

    SaveToFile()

Try(main)
