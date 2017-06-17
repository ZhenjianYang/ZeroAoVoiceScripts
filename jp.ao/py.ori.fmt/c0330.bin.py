from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c0330.bin",                # FileName
        "c0330",                    # MapName
        "c0330",                    # Location
        0x002C,                     # MapIndex
        "ed7150",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 44, 0, 3, 0, 4],
    )

    BuildStringList((
        "c0330",                  # 0
        "ハロルド",               # 1
        "ソフィア",               # 2
        "コリン",                 # 3
        "シンディ",               # 4
        "トルタ村長",             # 5
        "イアン弁護士",           # 6
    ))

    AddCharChip((
        "chr/ch09300.itc",                   # 00
        "chr/ch09302.itc",                   # 01
        "chr/ch09400.itc",                   # 02
        "chr/ch09402.itc",                   # 03
        "chr/ch07200.itc",                   # 04
        "chr/ch07202.itc",                   # 05
        "chr/ch22100.itc",                   # 06
        "chr/ch24000.itc",                   # 07
        "chr/ch05900.itc",                   # 08
    ))

    DeclNpc(-340,    0,       4409,    315,  261,  0x0, 0,   0,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(550,     0,       2039,    180,  261,  0x0, 0,   2,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(37479,   0,       3799,    180,  261,  0x0, 0,   4,   0,   0,   1,   0,   9,   255,  0)
    DeclNpc(-490,    0,       5139,    180,  389,  0x0, 0,   6,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(9,       0,       -230,    0,    389,  0x0, 0,   7,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(660,     0,       4599,    270,  453,  0x0, 0,   8,   0,   0,   0,   0,   13,  255,  0)

    DeclActor(34620,   0,       7280,    1200,    34620,   1750,    7280,    0x007C, 0,  5,  0x0000)

    ChipFrameInfo(464, 0)                                        # 0

    ScpFunction((
        "Function_0_1D0",          # 00, 0
        "Function_1_288",          # 01, 1
        "Function_2_2B3",          # 02, 2
        "Function_3_2DE",          # 03, 3
        "Function_4_7C5",          # 04, 4
        "Function_5_846",          # 05, 5
        "Function_6_8EE",          # 06, 6
        "Function_7_16DD",         # 07, 7
        "Function_8_2809",         # 08, 8
        "Function_9_2906",         # 09, 9
        "Function_10_3383",        # 0A, 10
        "Function_11_3460",        # 0B, 11
        "Function_12_3585",        # 0C, 12
        "Function_13_37CB",        # 0D, 13
        "Function_14_3A12",        # 0E, 14
        "Function_15_4185",        # 0F, 15
        "Function_16_44C6",        # 10, 16
        "Function_17_45F7",        # 11, 17
        "Function_18_5641",        # 12, 18
    ))


    def Function_0_1D0(): pass

    label("Function_0_1D0")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_210"),
        (1, "loc_21C"),
        (2, "loc_228"),
        (3, "loc_234"),
        (4, "loc_240"),
        (5, "loc_24C"),
        (6, "loc_258"),
        (SWITCH_DEFAULT, "loc_264"),
    )


    label("loc_210")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_270")

    label("loc_21C")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_270")

    label("loc_228")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_270")

    label("loc_234")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_270")

    label("loc_240")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_270")

    label("loc_24C")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_270")

    label("loc_258")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_270")

    label("loc_264")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_270")

    label("loc_270")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_287")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_270")

    label("loc_287")

    Return()

    # Function_0_1D0 end

    def Function_1_288(): pass

    label("Function_1_288")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2B2")
    OP_94(0xFE, 0x9268, 0x157C, 0x8F48, 0x85C, 0x3E8)
    Sleep(300)
    Jump("Function_1_288")

    label("loc_2B2")

    Return()

    # Function_1_288 end

    def Function_2_2B3(): pass

    label("Function_2_2B3")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2DD")
    OP_94(0xFE, 0xFFFFF240, 0x80C, 0xC58, 0x139C, 0x3E8)
    Sleep(300)
    Jump("Function_2_2B3")

    label("loc_2DD")

    Return()

    # Function_2_2B3 end

    def Function_3_2DE(): pass

    label("Function_3_2DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_325")
    SetChrPos(0x8, -1780, 0, 4730, 180)
    SetChrPos(0x9, 40940, 0, -550, 180)
    SetChrPos(0xA, 40930, 0, -1640, 90)
    BeginChrThread(0xA, 0, 0, 0)
    Jump("loc_7C4")

    label("loc_325")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_342")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    Jump("loc_7C4")

    label("loc_342")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_37D")
    SetChrFlags(0x8, 0x80)
    SetChrPos(0xA, -1000, 0, 3850, 90)
    SetChrPos(0x9, 670, 0, 3900, 270)
    BeginChrThread(0xA, 0, 0, 0)
    Jump("loc_7C4")

    label("loc_37D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_390")
    SetChrFlags(0x8, 0x80)
    Jump("loc_7C4")

    label("loc_390")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_3C0")
    SetChrPos(0x8, -490, 0, 5140, 180)
    SetChrPos(0x9, -690, 0, 3590, 0)
    Jump("loc_7C4")

    label("loc_3C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3EA")
    SetChrFlags(0x8, 0x80)
    SetChrPos(0xA, 38280, 0, 11000, 0)
    BeginChrThread(0xA, 0, 0, 0)
    Jump("loc_7C4")

    label("loc_3EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_414")
    SetChrFlags(0x8, 0x80)
    SetChrPos(0xA, -1670, 0, 3900, 45)
    BeginChrThread(0xA, 0, 0, 2)
    Jump("loc_7C4")

    label("loc_414")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_58B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x177, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_485")
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, -690, 0, 3590, 0)
    SetChrPos(0x8, -490, 0, 5140, 180)
    SetChrFlags(0xC, 0x10)
    SetChrFlags(0x8, 0x10)
    SetChrPos(0x9, 37670, 0, 3210, 180)
    SetChrPos(0xA, 37670, 0, 1940, 0)
    BeginChrThread(0xA, 0, 0, 0)
    Jump("loc_586")

    label("loc_485")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x177, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x177, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_507")
    SetChrPos(0xC, -690, 0, 3590, 0)
    SetChrPos(0x8, -490, 0, 5140, 180)
    SetChrPos(0xD, 660, 0, 4600, 270)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xA, 41130, 0, 1090, 90)
    BeginChrThread(0xA, 0, 0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_502")
    SetChrFlags(0xA, 0x10)

    label("loc_502")

    Jump("loc_586")

    label("loc_507")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_545")
    SetChrFlags(0x8, 0x80)
    SetChrPos(0xA, 32700, 500, 9220, 270)
    BeginChrThread(0xA, 0, 0, 0)
    SetChrChipByIndex(0xA, 0x5)
    SetChrSubChip(0xA, 0x0)
    EndChrThread(0xA, 0x0)
    SetChrBattleFlags(0xA, 0x4)
    Jump("loc_586")

    label("loc_545")

    SetChrFlags(0x8, 0x80)
    SetChrPos(0xA, 41130, 0, 1090, 90)
    BeginChrThread(0xA, 0, 0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_570")
    SetChrFlags(0xA, 0x10)

    label("loc_570")

    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, -10, 0, 5370, 270)

    label("loc_586")

    Jump("loc_7C4")

    label("loc_58B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_59E")
    SetChrFlags(0x8, 0x80)
    Jump("loc_7C4")

    label("loc_59E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_613")
    SetChrFlags(0x8, 0x80)
    SetChrPos(0x9, 40930, 0, -1640, 90)
    SetChrPos(0xA, -690, 0, 3590, 0)
    BeginChrThread(0xA, 0, 0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5E3")
    SetChrFlags(0xA, 0x10)

    label("loc_5E3")

    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, -490, 0, 5140, 180)
    BeginChrThread(0xB, 0, 0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_60E")
    SetChrFlags(0xB, 0x10)

    label("loc_60E")

    Jump("loc_7C4")

    label("loc_613")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_66B")
    SetChrPos(0x8, 1940, 200, 6910, 270)
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    SetChrPos(0x9, 40940, 0, -550, 180)
    SetChrPos(0xA, 40930, 0, -1640, 90)
    BeginChrThread(0xA, 0, 0, 0)
    Jump("loc_7C4")

    label("loc_66B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_6C4")
    SetChrFlags(0x8, 0x80)
    SetChrPos(0x9, -490, 0, 5140, 180)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_699")
    SetChrFlags(0x9, 0x10)

    label("loc_699")

    SetChrPos(0xA, -690, 0, 3590, 0)
    BeginChrThread(0xA, 0, 0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6BF")
    SetChrFlags(0xA, 0x10)

    label("loc_6BF")

    Jump("loc_7C4")

    label("loc_6C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_6D7")
    SetChrFlags(0x8, 0x80)
    Jump("loc_7C4")

    label("loc_6D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_74F")
    SetChrPos(0x8, -820, 200, 10200, 180)
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    SetChrPos(0x9, 40930, 0, -1640, 90)
    SetChrPos(0xA, 34300, 0, 1140, 315)
    BeginChrThread(0xA, 0, 0, 0)
    SetChrFlags(0xA, 0x10)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 38720, 0, 510, 270)
    SetChrFlags(0xB, 0x10)
    Jump("loc_7C4")

    label("loc_74F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_7C4")
    SetChrPos(0x8, -820, 200, 10200, 180)
    SetChrPos(0x9, 1940, 200, 8290, 270)
    SetChrPos(0xA, 1940, 200, 6910, 270)
    BeginChrThread(0xA, 0, 0, 0)
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    SetChrChipByIndex(0x9, 0x3)
    SetChrSubChip(0x9, 0x0)
    EndChrThread(0x9, 0x0)
    SetChrBattleFlags(0x9, 0x4)
    SetChrChipByIndex(0xA, 0x5)
    SetChrSubChip(0xA, 0x0)
    EndChrThread(0xA, 0x0)
    SetChrBattleFlags(0xA, 0x4)

    label("loc_7C4")

    Return()

    # Function_3_2DE end

    def Function_4_7C5(): pass

    label("Function_4_7C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_80A")
    SetMapObjFrame(0xFF, "light01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "model05_light", 0x0, 0x1)
    Sound(128, 1, 50, 0)

    label("loc_80A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_845")
    OP_7D(0xD2, 0xD2, 0xE6, 0x0, 0x0)
    SetMapObjFrame(0xFF, "light01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "model05_light", 0x0, 0x1)

    label("loc_845")

    Return()

    # Function_4_7C5 end

    def Function_5_846(): pass

    label("Function_5_846")

    SetChrName("")

    #A0001
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "車雑誌『月間カーマニアvol.1』がある。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 1)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x36C, 0x0)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8EA")
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0002
    AnonymousTalk(
        0xFF,
        (
            "ペイントパターン\x01\x07\x02",

            "『スカイカラー』\x07\x00",
            "を覚えた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    AddItemNumber(0x36C, 1)

    label("loc_8EA")

    TalkEnd(0xFF)
    Return()

    # Function_5_846 end

    def Function_6_8EE(): pass

    label("Function_6_8EE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_CDD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CD, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BA2")

    #C0003
    ChrTalk(
        0x8,
        (
            "#03600Fおや、みなさん。\x01",
            "ご無事でなによりです。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x101,
        (
            "#00000Fハロルドさん、アルモリカ村から\x01",
            "帰ってきてたんですね？\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x8,
        (
            "#03604Fええ、結界が消えたのを見て\x01",
            "ついさっき戻ってきた所でして。\x02\x03",

            "#03600Fこれからすぐに\x01",
            "出かけるところではありますが。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x103,
        "#00203Fさすがに忙しいみたいですね。\x02",
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x104,
        (
            "#00300F家族もいるんだし、\x01",
            "もう少しゆっくりしても\x01",
            "いいんじゃないッスか？\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x8,
        (
            "#03603Fいえ、今は少しでも\x01",
            "クロスベル各地の皆さんの\x01",
            "力になりたいと思いまして。\x02\x03",

            "#03600F手始めに、マインツのほうへ\x01",
            "行ってみるつもりです。\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x101,
        (
            "#00004Fそうですか……\x01",
            "さすがハロルドさんというか。\x02\x03",

            "#00002Fどうか、気をつけて行って下さい。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x8,
        (
            "#03609Fええ、みなさんも……\x01",
            "女神の加護をお祈りしています。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1CD, 0)
    Jump("loc_CD8")

    label("loc_BA2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C66")

    #C0011
    ChrTalk(
        0x8,
        (
            "#03600F手始めに、マインツのほうへ\x01",
            "行ってみるつもりです。\x02\x03",

            "#03603F今は少しでも各地の皆さんの\x01",
            "力になりたいと思いまして……\x02\x03",

            "#03609Fみなさんも、\x01",
            "女神の加護をお祈りしています。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_CD8")

    label("loc_C66")


    #C0012
    ChrTalk(
        0x8,
        (
            "#03600F手始めに、マインツのほうへ\x01",
            "行ってみるつもりです。\x02\x03",

            "#03609Fみなさんも、\x01",
            "女神の加護をお祈りしています。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CD8")

    Jump("loc_16D9")

    label("loc_CDD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_CEB")
    Jump("loc_16D9")

    label("loc_CEB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_CF9")
    Jump("loc_16D9")

    label("loc_CF9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_D07")
    Jump("loc_16D9")

    label("loc_D07")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_EBE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E16")

    #C0013
    ChrTalk(
        0x8,
        (
            "#03601F今日はマインツに行く\x01",
            "予定だったのですが……\x01",
            "まさかこんな事になるなんて。\x02\x03",

            "#03603F……マインツには何度も取引きに\x01",
            "伺っていますし、町の方々には\x01",
            "とても良くしてもらってます。\x02\x03",

            "#03608Fそれなのに、何一つ出来ない自分が\x01",
            "情けない思いです……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_EB9")

    label("loc_E16")


    #C0014
    ChrTalk(
        0x8,
        (
            "#03603F……マインツには何度も取引きに\x01",
            "伺っていますし、町の方々には\x01",
            "とても良くしてもらってます。\x02\x03",

            "#03608Fそれなのに、何一つ出来ない自分が\x01",
            "情けない思いです……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EB9")

    Jump("loc_16D9")

    label("loc_EBE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_ECC")
    Jump("loc_16D9")

    label("loc_ECC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_EDA")
    Jump("loc_16D9")

    label("loc_EDA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_100E")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_F7D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x177, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F01")
    Call(0, 15)
    Jump("loc_F78")

    label("loc_F01")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x177, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F13")
    Call(0, 18)
    Jump("loc_F78")

    label("loc_F13")


    #C0015
    ChrTalk(
        0x8,
        (
            "#03600F村長たちは、あとで私の車で\x01",
            "村へと送り届けます。\x02\x03",

            "みなさん、\x01",
            "どうかお気をつけてください。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F78")

    Jump("loc_1009")

    label("loc_F7D")


    #C0016
    ChrTalk(
        0x8,
        (
            "#03601Fとにかく、\x01",
            "昨日調べて分かったことを\x01",
            "まとめてみましょう。\x02\x03",

            "#03603Fそれと、後でイアン先生に\x01",
            "相談してみた方が\x01",
            "いいかもしれません。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1009")

    Jump("loc_16D9")

    label("loc_100E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_101C")
    Jump("loc_16D9")

    label("loc_101C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_102A")
    Jump("loc_16D9")

    label("loc_102A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_11FC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14A, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_117A")

    #C0017
    ChrTalk(
        0x8,
        "#03605Fおや、みなさん。\x02",
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x101,
        "#00000Fこんばんは、ハロルドさん。\x02",
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x102,
        (
            "#00104F２階の方からいい匂いが……\x01",
            "奥様が夕食の準備を\x01",
            "されてるみたいですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x8,
        (
            "#03609Fええ、そうなんですよ。\x01",
            "それに今日はコリンも\x01",
            "手伝っているみたいでして。\x02\x03",

            "#03604Fいやあ、私も出先から\x01",
            "戻ってきたところなので、\x01",
            "お腹がペコペコですよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x14A, 6)
    Jump("loc_11F7")

    label("loc_117A")


    #C0021
    ChrTalk(
        0x8,
        (
            "#03600Fどうやら今日は、\x01",
            "コリンが料理を手伝っている\x01",
            "みたいでしてね。\x02\x03",

            "#03609Fふふ、どんな料理が\x01",
            "出てくるか楽しみですよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11F7")

    Jump("loc_16D9")

    label("loc_11FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_120A")
    Jump("loc_16D9")

    label("loc_120A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1218")
    Jump("loc_16D9")

    label("loc_1218")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_14EE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x134, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1465")

    #C0022
    ChrTalk(
        0x8,
        (
            "#03603Fこうして１人で\x01",
            "静かに過ごしていると、\x01",
            "ふと考えることがあります。\x02\x03",

            "以前コリンを助けてくれたと言う\x01",
            "スミレ色の髪の女の子……\x02\x03",

            "#03608Fその子に会うことは\x01",
            "本当にできないのだろうか、とね。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x101,
        "#00005Fそ、それは……\x02",
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x8,
        (
            "#03604Fはは、今のところ\x01",
            "何の手がかりもないので、\x01",
            "単なる希望なんですけどね。\x02\x03",

            "#03600Fもしそんな機会があったら……\x01",
            "是非ともお礼をしたいものです。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x101,
        (
            "#00008F（スミレ色の髪の女の子……\x01",
            "  レンはエステルたちと\x01",
            "  リベールに戻ったんだよな……）\x02\x03",

            "#00003F（あの子もまだ気持ちの整理は\x01",
            "  必要なんだろうけど……\x01",
            "  いつかそんな日が来るといいな。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x134, 0)
    Jump("loc_14E9")

    label("loc_1465")


    #C0026
    ChrTalk(
        0x8,
        (
            "#03603F以前コリンを助けてくれたと言う\x01",
            "スミレ色の髪の女の子……\x02\x03",

            "#03600Fもし会える日が来たなら、\x01",
            "是非ともお礼をしたいものです。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14E9")

    Jump("loc_16D9")

    label("loc_14EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_16D9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12F, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_150D")
    TalkEnd(0xFE)
    Call(0, 14)
    Return()

    label("loc_150D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1660")

    #C0027
    ChrTalk(
        0x8,
        (
            "#03600F最近は、商売も上向きに\x01",
            "なってきていましてね。\x02\x03",

            "#03604Fこうして休みをとって\x01",
            "家族サービスをする余裕も\x01",
            "出来てきました。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x102,
        (
            "#00100Fふふ、ハロルドさんの堅実な姿勢が\x01",
            "実を結んでいるんでしょうね。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x8,
        (
            "#03609Fハハ、それはその……\x01",
            "正直むず痒いですね。\x02\x03",

            "#03600F私は最低限、家族さえ養えれば\x01",
            "それだけで充分なんですが。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_16D9")

    label("loc_1660")


    #C0030
    ChrTalk(
        0x8,
        (
            "#03600Fみなさん、また何かあったら\x01",
            "是非うちにいらしてください。\x02\x03",

            "私で力になれることなら\x01",
            "なんでもお手伝いしますから。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16D9")

    TalkEnd(0xFE)
    Return()

    # Function_6_8EE end

    def Function_7_16DD(): pass

    label("Function_7_16DD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_187E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17D9")

    #C0031
    ChrTalk(
        0x9,
        (
            "#03708Fもう少しゆっくりしていけば、\x01",
            "とは私も思うんですが……\x02\x03",

            "#03700Fあの優しくて気配り上手なのが\x01",
            "ハロルド・ヘイワースという人ですもの。\x02\x03",

            "#03709F主人が皆の力になりたいというなら、\x01",
            "私たちはそれを支えていくだけですわ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1879")

    label("loc_17D9")


    #C0032
    ChrTalk(
        0x9,
        (
            "#03700Fあの優しくて気配り上手なのが\x01",
            "ハロルド・ヘイワースという人ですもの。\x02\x03",

            "#03709F主人が皆の力になりたいというなら、\x01",
            "私たちはそれを支えていくだけですわ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1879")

    Jump("loc_2805")

    label("loc_187E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_188C")
    Jump("loc_2805")

    label("loc_188C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_1916")

    #C0033
    ChrTalk(
        0x9,
        (
            "#03708Fこれから、どうなって\x01",
            "しまうんでしょう……\x02\x03",

            "#03710F主人やコリンになにかあったら……\x01",
            "とにかくそれだけが心配です。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2805")

    label("loc_1916")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1A93")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19F9")

    #C0034
    ChrTalk(
        0x9,
        (
            "#03700F今日は主人はマインツのほうに\x01",
            "様子を見に行っています。\x02\x03",

            "先日の襲撃事件をうけて、\x01",
            "自分に出来るかぎりの事を\x01",
            "やろうとしているみたいで……\x02\x03",

            "#03709F心優しい主人のことを、\x01",
            "改めて誇りに思います。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1A8E")

    label("loc_19F9")


    #C0035
    ChrTalk(
        0x9,
        (
            "#03700F主人は襲撃事件をうけて、\x01",
            "自分に出来るかぎりの事を\x01",
            "やろうとしているみたいです。\x02\x03",

            "#03709F心優しい主人のことを、\x01",
            "あらためて誇りに思います。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A8E")

    Jump("loc_2805")

    label("loc_1A93")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_1BC4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B76")

    #C0036
    ChrTalk(
        0x9,
        (
            "#03708F事件の報せを聞いて、一瞬\x01",
            "『主人が巻き込まれなくて良かった』\x01",
            "などと考えてしまいました。\x02\x03",

            "今まさにこの瞬間、\x01",
            "マインツの人々が恐怖に\x01",
            "怯えているというのに……\x02\x03",

            "#03710F……自分が嫌になります。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1BBF")

    label("loc_1B76")


    #C0037
    ChrTalk(
        0x9,
        (
            "#03708F……とにかく、\x01",
            "早く事件が解決することを\x01",
            "女神に祈りましょう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BBF")

    Jump("loc_2805")

    label("loc_1BC4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1C6B")

    #C0038
    ChrTalk(
        0x9,
        (
            "#03700F主人は今日はベルガード門の方へ\x01",
            "商品を卸しに行っています。\x02\x03",

            "#03708F昨日は西の街道で巨大な化物が\x01",
            "目撃されたそうですし、\x01",
            "少し心配なのですが……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2805")

    label("loc_1C6B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_1E87")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x177, 2)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16C, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1D7A")

    #C0039
    ChrTalk(
        0x9,
        (
            "#03705Fあら、みなさん？\x02\x03",

            "主人なら、村長さんと一緒に\x01",
            "アルモリカ村に向かいましたが……\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x101,
        (
            "#00003F（捜査に最後まで\x01",
            "  付き合いたかったけど……\x01",
            "  今は事故の確認が最優先だ。）\x02\x03",

            "（アルモリカ村は\x01",
            "  ハロルドさんに任せるしかないな。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x16C, 7)
    Jump("loc_1E82")

    label("loc_1D7A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E26")

    #C0041
    ChrTalk(
        0x9,
        (
            "#03700F先ほど、シンディちゃんが来て\x01",
            "教えてくれたんですが……\x02\x03",

            "たくさんの救急車が\x01",
            "西通りを通っていったそうです。\x02\x03",

            "#03708Fなんだか胸騒ぎがしますね……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1E82")

    label("loc_1E26")


    #C0042
    ChrTalk(
        0x9,
        (
            "#03708Fたくさんの救急車が\x01",
            "西通りを通っていったそうです。\x02\x03",

            "なんだか胸騒ぎがしますね……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E82")

    Jump("loc_2805")

    label("loc_1E87")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_21CE")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1FD0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F4D")

    #C0043
    ChrTalk(
        0x9,
        (
            "#03700F先ほど主人から連絡がありました。\x01",
            "アルモリカ村の事件は\x01",
            "無事に解決したそうですね。\x02\x03",

            "#03708Fそれにしても詐欺だなんて……\x01",
            "本当に悪い人がいたものです。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1FCB")

    label("loc_1F4D")


    #C0044
    ChrTalk(
        0x9,
        (
            "#03700Fアルモリカ村の事件は\x01",
            "無事に解決したそうですね。\x02\x03",

            "#03708Fそれにしても詐欺だなんて……\x01",
            "本当に悪い人がいたものです。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1FCB")

    Jump("loc_21C9")

    label("loc_1FD0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x177, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2060")

    #C0045
    ChrTalk(
        0x9,
        (
            "#03700F村長さんの息子さんが\x01",
            "何か、厄介事に巻き込まれている\x01",
            "みたいですね……\x02\x03",

            "#03708F早いところ\x01",
            "解決に向かえばよいのですが。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21C9")

    label("loc_2060")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_213C")

    #C0046
    ChrTalk(
        0x9,
        (
            "#03700F村長さん、とても思いつめて\x01",
            "いらっしゃるようですね……\x02\x03",

            "#03708F息子さんのことですから、\x01",
            "当然といえば当然ですが……\x02\x03",

            "#03700F心配のしすぎはお体に障りますし、\x01",
            "ひとまず落ちついていただかないと。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_21C9")

    label("loc_213C")


    #C0047
    ChrTalk(
        0x9,
        (
            "#03700F心配のしすぎはお体に障りますし、\x01",
            "ひとまず落ちついていただかないと。\x02\x03",

            "たしか、鎮静効果のあるハーブティの\x01",
            "取り置きがあったはず……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_21C9")

    Jump("loc_2805")

    label("loc_21CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2276")

    #C0048
    ChrTalk(
        0x9,
        (
            "#03700Fアルモリカ村の村長さんから\x01",
            "主人に連絡があったんです。\x02\x03",

            "なんだか相談事があるらしく……\x01",
            "商談ではないようなのですが、\x01",
            "一体どうしたんでしょう……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2805")

    label("loc_2276")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_23AF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_233C")

    #C0049
    ChrTalk(
        0x9,
        (
            "#03700F昨夜、コリンと一緒に\x01",
            "カレーを作ったんですが……\x02\x03",

            "ちょっと作りすぎたかしら。\x01",
            "まだかなり余っているみたい。\x02\x03",

            "#03709Fふふ、しばらくは\x01",
            "カレーの日が続きそうですね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_23AA")

    label("loc_233C")


    #C0050
    ChrTalk(
        0x9,
        (
            "#03700F昨夜のカレー……\x01",
            "ちょっと作りすぎたかしら。\x02\x03",

            "#03709Fふふ、しばらくは\x01",
            "カレーの日が続きそうですね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_23AA")

    Jump("loc_2805")

    label("loc_23AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_242C")

    #C0051
    ChrTalk(
        0x9,
        (
            "#03700Fさ、あとは煮立つのを待つだけよ。\x02\x03",

            "#03709Fふふ、よく出来たわねコリン。\x01",
            "きっとパパも喜んでくれるわ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2805")

    label("loc_242C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_24B4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2447")
    Call(0, 8)
    Jump("loc_24AF")

    label("loc_2447")


    #C0052
    ChrTalk(
        0x9,
        (
            "#03700F今からちょっと買い物に\x01",
            "行くところなんです。\x02\x03",

            "#03709Fふふ、コリンったら\x01",
            "はりきっていますね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_24AF")

    Jump("loc_2805")

    label("loc_24B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2612")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_257D")

    #C0053
    ChrTalk(
        0x9,
        (
            "#03700Fこの間、ご近所にいた\x01",
            "クレイユさんが会いにきてくれました。\x02\x03",

            "やっと生活が落ち着いたらしくて、\x01",
            "とても安心なさった様子で……\x02\x03",

            "#03709Fふふ、私も安心してしまいました。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_260D")

    label("loc_257D")


    #C0054
    ChrTalk(
        0x9,
        (
            "#03700Fクレイユさんたち、\x01",
            "今は東通りのアパルトメントに\x01",
            "住んでらっしゃるとか。\x02\x03",

            "けっこう馴染んでいるみたいですし、\x01",
            "とりあえず安心しました。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_260D")

    Jump("loc_2805")

    label("loc_2612")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_277B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_26F2")

    #C0055
    ChrTalk(
        0x9,
        (
            "#03700Fご近所にいたボンドさん一家は\x01",
            "少し前に引っ越してしまったんです。\x02\x03",

            "#03708F家を引き払うときに\x01",
            "挨拶に来て下さったのですが……\x01",
            "それからまだ連絡もなくて。\x02\x03",

            "元気にしているといいのですけど……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2776")

    label("loc_26F2")


    #C0056
    ChrTalk(
        0x9,
        (
            "#03700Fボンドさんの奥さんとは、\x01",
            "一緒にお料理をしたりして\x01",
            "とても仲が良かったのです。\x02\x03",

            "#03708F元気にしているといいのですけど……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2776")

    Jump("loc_2805")

    label("loc_277B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_2805")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12F, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_279A")
    TalkEnd(0xFE)
    Call(0, 14)
    Return()

    label("loc_279A")


    #C0057
    ChrTalk(
        0x9,
        (
            "#03700F以前、皆さんには\x01",
            "本当にお世話になりました。\x02\x03",

            "主人ともども、これからまた\x01",
            "よろしくお願いします。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2805")

    TalkEnd(0xFE)
    Return()

    # Function_7_16DD end

    def Function_8_2809(): pass

    label("Function_8_2809")

    OP_4B(0x9, 0xFF)
    OP_4B(0xA, 0xFF)

    #C0058
    ChrTalk(
        0x9,
        (
            "#03700Fほらコリン、今日は何を\x01",
            "買いに行くんだったかしら？\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0xA,
        (
            "#03805Fえーっとえーっと……\x01",
            "にんじんに、じゃがいもに、\x01",
            "たまねぎに……\x02\x03",

            "#03809F……カレーのルー！\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x9,
        (
            "#03709Fふふ、正解。\x01",
            "それじゃあ行くとしましょうか。\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x9, 0xFF)
    OP_4C(0xA, 0xFF)
    ClearChrFlags(0x9, 0x10)
    ClearChrFlags(0xA, 0x10)
    SetScenarioFlags(0x0, 1)
    SetScenarioFlags(0x0, 2)
    Return()

    # Function_8_2809 end

    def Function_9_2906(): pass

    label("Function_9_2906")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2A43")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_29C7")

    #C0061
    ChrTalk(
        0xA,
        (
            "#03800Fお仕事にいくパパのために、\x01",
            "ママとお弁当を作ってるんだ～。\x02\x03",

            "#03809Fカミーユくんちのおばさんが\x01",
            "お野菜をいっぱいくれたんだよ～。\x01",
            "えへへ、おいしそーだね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2A3E")

    label("loc_29C7")


    #C0062
    ChrTalk(
        0xA,
        (
            "#03800Fまた、アルモリカ村に行きたいな～。\x02\x03",

            "#03809Fカミーユくんやプーリーちゃんたちと\x01",
            "また遊ぶ約束をしたんだよ～。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A3E")

    Jump("loc_337F")

    label("loc_2A43")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_2A51")
    Jump("loc_337F")

    label("loc_2A51")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_2ACA")

    #C0063
    ChrTalk(
        0xA,
        (
            "#03805Fパパもママも、\x01",
            "なんだか心配そうなんだ～。\x02\x03",

            "これからあそびに行くのに、\x01",
            "どうしちゃったのかな～？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_337F")

    label("loc_2ACA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2BDC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B72")

    #C0064
    ChrTalk(
        0xA,
        (
            "#03800Fこんどね～、\x01",
            "パパとママといっしょに\x01",
            "あそびに行くんだよ～。\x02\x03",

            "#03809Fとってもキレイなばしょなんだって～。\x01",
            "えへへ、たのしみだな～。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2BD7")

    label("loc_2B72")


    #C0065
    ChrTalk(
        0xA,
        (
            "#03800Fこんどね～、キレイなばしょに\x01",
            "あそびに行くんだよ～。\x02\x03",

            "#03809Fわくわく……たのしみだな～。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2BD7")

    Jump("loc_337F")

    label("loc_2BDC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_2C6C")

    #C0066
    ChrTalk(
        0xA,
        (
            "#03800Fパパ、きょうは\x01",
            "おしごとって言ってたけど、\x01",
            "まだいかないみたいなんだ～。\x02\x03",

            "#3802Fもしかして、\x01",
            "おやすみになったのかな～？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_337F")

    label("loc_2C6C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2CD7")

    #C0067
    ChrTalk(
        0xA,
        (
            "#03802Fみてみて、\x01",
            "窓にカエルがくっついてるよ～。\x02\x03",

            "#03809Fもぞもぞしててかわいいよね～。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_337F")

    label("loc_2CD7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_2D5B")

    #C0068
    ChrTalk(
        0xA,
        (
            "#03802Fさっきシンディお姉ちゃんが\x01",
            "やいたクッキーを\x01",
            "もってきてくれたんだ～。\x02\x03",

            "#03809Fさくさくしてておいし～な～。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_337F")

    label("loc_2D5B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2F2D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x177, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2DD8")

    #C0069
    ChrTalk(
        0xA,
        (
            "#03800Fきょうはだいじな\x01",
            "おはなしがあるから\x01",
            "２階にいなさい、だって～。\x02\x03",

            "おしごとのはなしかな～？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F28")

    label("loc_2DD8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2E3E")

    #C0070
    ChrTalk(
        0xA,
        (
            "#03805Fひとりであそぶのも\x01",
            "あきちゃった～。\x02\x03",

            "パパ、はやく\x01",
            "かえってこないかな～。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F28")

    label("loc_2E3E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2EB7")

    #C0071
    ChrTalk(
        0xA,
        (
            "#03805Fあっ、こんなところに\x01",
            "ハチミツがあった～。\x02\x03",

            "#03809Fぺろっ。\x01",
            "えへへ、甘くておいし～な。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    ClearChrFlags(0xA, 0x10)
    Jump("loc_2F28")

    label("loc_2EB7")


    #C0072
    ChrTalk(
        0xA,
        (
            "#03809Fこのハチミツ、このあいだ\x01",
            "パパがおみやげに\x01",
            "もってかえってきたんだ～。\x02\x03",

            "ぼく、このハチミツだいすき～。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F28")

    Jump("loc_337F")

    label("loc_2F2D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3028")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2FCE")

    #C0073
    ChrTalk(
        0xA,
        (
            "#03805Fパパ、きょうはおやすみだったのに\x01",
            "どこかに行っちゃったんだ～。\x02\x03",

            "きゅうなおしごとが\x01",
            "はいっちゃったのかな～？\x01",
            "がっかり～……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3023")

    label("loc_2FCE")


    #C0074
    ChrTalk(
        0xA,
        (
            "#03805Fきょうはパパにあそんでもらう\x01",
            "やくそくだったんだけどな～。\x01",
            "がっかり～……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3023")

    Jump("loc_337F")

    label("loc_3028")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3086")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3043")
    Call(0, 10)
    Jump("loc_3081")

    label("loc_3043")


    #C0075
    ChrTalk(
        0xA,
        (
            "#03809Fえへへ、シンディお姉ちゃんに\x01",
            "ほめられちゃった～。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3081")

    Jump("loc_337F")

    label("loc_3086")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_3109")

    #C0076
    ChrTalk(
        0xA,
        (
            "#03802Fきょうのばんごはんは\x01",
            "カレーなんだよ～。\x02\x03",

            "#03809Fえへへ、ぼくが\x01",
            "おやさいを切ったんだ～。\x01",
            "すごいでしょ～？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_337F")

    label("loc_3109")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_31B4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3124")
    Call(0, 8)
    Jump("loc_31AF")

    label("loc_3124")


    #C0077
    ChrTalk(
        0xA,
        (
            "#03800Fきょうはね～、\x01",
            "ぼくがばんごはんの\x01",
            "おてつだいをするんだよ～。\x02\x03",

            "#03809Fおしごとからかえってくるパパを\x01",
            "びっくりさせちゃうんだ～。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_31AF")

    Jump("loc_337F")

    label("loc_31B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3231")

    #C0078
    ChrTalk(
        0xA,
        (
            "#03800Fきょうはパパ、おしごとなんだ～。\x02\x03",

            "#03802Fまた、いっぱいおみやげを\x01",
            "もってかえってきてくれるかな～。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_337F")

    label("loc_3231")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_32E4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_329D")

    #C0079
    ChrTalk(
        0xA,
        (
            "#03802Fひょい、ぱくっ。\x02\x03",

            "#03809Fもぐもぐ……\x01",
            "えへへ、とってもおいしいな～。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_32DF")

    label("loc_329D")


    #C0080
    ChrTalk(
        0xA,
        (
            "#03809Fえへへ、やっぱりママは、\x01",
            "おりょうりがじょうずだね～。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_32DF")

    Jump("loc_337F")

    label("loc_32E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_337F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12F, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3303")
    TalkEnd(0xFE)
    Call(0, 14)
    Return()

    label("loc_3303")


    #C0081
    ChrTalk(
        0xA,
        (
            "#03805F話してたら、またあの\x01",
            "スミレ色のお姉ちゃんに\x01",
            "会いたくなっちゃったな～。\x02\x03",

            "#03809Fえへへ、またいつか会えるよね～。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_337F")

    TalkEnd(0xFE)
    Return()

    # Function_9_2906 end

    def Function_10_3383(): pass

    label("Function_10_3383")

    OP_4B(0xA, 0xFF)
    OP_4B(0xB, 0xFF)

    #C0082
    ChrTalk(
        0xA,
        (
            "#03802Fシンディお姉ちゃん、あのね～。\x02\x03",

            "ぼく、きのうはカレーを\x01",
            "つくったんだよ～。\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0xB,
        (
            "へえ、コリン君が？\x01",
            "すごいすご～い！\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0xB,
        (
            "こりゃ、うちのお兄ちゃんよりも\x01",
            "よっぽど料理できるわね。\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xA, 0xFF)
    OP_4C(0xB, 0xFF)
    ClearChrFlags(0xA, 0x10)
    ClearChrFlags(0xB, 0x10)
    SetScenarioFlags(0x0, 2)
    SetScenarioFlags(0x0, 3)
    Return()

    # Function_10_3383 end

    def Function_11_3460(): pass

    label("Function_11_3460")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_352B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_347E")
    Call(0, 10)
    Jump("loc_3526")

    label("loc_347E")


    #C0085
    ChrTalk(
        0xFE,
        (
            "ふふ、今日はソフィアさんに\x01",
            "美味しいお菓子の作り方を\x01",
            "教えてもらうつもりなのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0xFE,
        (
            "それにしてもコリン君、\x01",
            "小さいのにえらいわね～……\x01",
            "お兄ちゃんに見習わせたいわ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3526")

    Jump("loc_3581")

    label("loc_352B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_3581")

    #C0087
    ChrTalk(
        0xFE,
        (
            "あっ、コリン君ったら\x01",
            "つまみ食いしてる。\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0xFE,
        "ふふっ、いたずらっ子め～。\x02",
    )

    CloseMessageWindow()

    label("loc_3581")

    TalkEnd(0xFE)
    Return()

    # Function_11_3460 end

    def Function_12_3585(): pass

    label("Function_12_3585")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_37B2")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_35DD")

    #C0089
    ChrTalk(
        0xFE,
        (
            "すまない、ハロルド君。\x01",
            "君には迷惑をかけるな……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_37B2")

    label("loc_35DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x177, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_35EF")
    Call(0, 15)
    Jump("loc_37B2")

    label("loc_35EF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_37B2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x177, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x177, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_36A0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x177, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_361B")
    Call(0, 18)
    Jump("loc_369B")

    label("loc_361B")


    #C0090
    ChrTalk(
        0xFE,
        (
            "わしらはイアン先生の\x01",
            "探し物を手伝ってから、\x01",
            "村に向かうとしよう。\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0xFE,
        (
            "あんたたち……\x01",
            "デリックのことを\x01",
            "よろしくお願い申す。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_369B")

    Jump("loc_37B2")

    label("loc_36A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3749")

    #C0092
    ChrTalk(
        0xFE,
        (
            "アルモリカの村長であり、\x01",
            "デリックの父である私が\x01",
            "何もできないのは不甲斐ないが……\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0xFE,
        (
            "どうか、よろしく頼む。\x01",
            "ミンネスという男の正体を暴いてくれ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_37B2")

    label("loc_3749")


    #C0094
    ChrTalk(
        0xFE,
        "何もできない自分が不甲斐ないが……\x02",
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0xFE,
        (
            "どうか、よろしく頼む。\x01",
            "ミンネスという男の正体を暴いてくれ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_37B2")

    TalkEnd(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x177, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x177, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_37CA")
    OP_93(0xC, 0x10E, 0x0)

    label("loc_37CA")

    Return()

    # Function_12_3585 end

    def Function_13_37CB(): pass

    label("Function_13_37CB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x177, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_37E0")
    Call(0, 18)
    Jump("loc_3A0E")

    label("loc_37E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3950")

    #C0096
    ChrTalk(
        0xD,
        (
            "#02200F私が探している証拠は、\x01",
            "ミンネスとやらを追い詰めたあとの、\x01",
            "ダメ押し程度にはなるかもしれない。\x02\x03",

            "とにかく、君たちはアルモリカ村に\x01",
            "急いだほうがいいだろう。\x02\x03",

            "#02203Fミンネスという男が本当に詐欺師なら、\x01",
            "計画は最終局面にまで\x01",
            "進行していてもおかしくない。\x02\x03",

            "#02200Fだが、君たちならきっと\x01",
            "手持ちの証拠で何とかできるはずだ。\x01",
            "健闘を祈らせてもらうよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_3A0E")

    label("loc_3950")


    #C0097
    ChrTalk(
        0xD,
        (
            "#02203Fミンネスという男が本当に詐欺師なら、\x01",
            "計画は最終局面にまで\x01",
            "進行していてもおかしくない。\x02\x03",

            "#02200Fだが、君たちならきっと\x01",
            "手持ちの証拠で何とかできるはずだ。\x01",
            "健闘を祈らせてもらうよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3A0E")

    TalkEnd(0xFE)
    Return()

    # Function_13_37CB end

    def Function_14_3A12(): pass

    label("Function_14_3A12")

    EventBegin(0x0)
    SetChrSubChip(0x9, 0x0)
    SetChrSubChip(0xA, 0x0)
    SetChrSubChip(0x8, 0x0)
    Fade(500)
    OP_68(-960, 1600, 6740, 0)
    MoveCamera(46, 18, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(24100, 0)
    SetChrPos(0x101, -970, 0, 4960, 0)
    SetChrPos(0x102, 640, 0, 4960, 0)
    SetChrPos(0x109, -470, 0, 4260, 0)
    SetChrPos(0x105, 1040, 0, 3960, 0)
    OP_0D()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x9, 0x1)
    SetChrSubChip(0xA, 0x1)
    Sleep(300)

    #C0098
    ChrTalk(
        0x9,
        "#11P#03705Fあら、あなた方は……\x02",
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0x8,
        "#5P#03609Fおお、支援課のみなさん！\x02",
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0xA,
        "#11P#03802Fこんにちは～！\x02",
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0x101,
        (
            "#12P#00000Fお久しぶりです、\x01",
            "ハロルドさん、ソフィアさん。\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x102,
        (
            "#12P#00102Fふふ、コリン君も\x01",
            "お元気そうで。\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0x8,
        (
            "#5P#03600Fおかげさまで……\x01",
            "あれ以来、何事も無く\x01",
            "平穏に暮らしていますよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0x109,
        (
            "#12P#10105Fロイドさんたちは、\x01",
            "こちらの御一家とは\x01",
            "お知り合いみたいですね？\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0x105,
        (
            "#12P#10304Fフフ、なんだか\x01",
            "色々あったみたいだけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0x8,
        (
            "#5P#03600Fええ、支援課の皆さんには\x01",
            "以前コリンが行方不明になった際に\x01",
            "お世話になりまして。\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0x9,
        (
            "#11P#03709Fその節は本当に\x01",
            "ありがとうございました。\x02\x03",

            "#03700F今、こうしていられるのも、\x01",
            "皆さんのおかげだと思います。\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0x101,
        (
            "#12P#00012Fい、いえ……\x01",
            "俺たちはそんな大したことは。\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0x8,
        (
            "#5P#03600Fどうかそう仰らずに……\x01",
            "実際、皆さんにはいくら感謝しても\x01",
            "足りないくらいです。\x02\x03",

            "#03608F本当なら、その時に\x01",
            "手伝ってくれたという女の子にも\x01",
            "お礼を言いたい所なんですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0xA,
        (
            "#11P#03805Fもしかして、\x01",
            "スミレ色のお姉ちゃんのこと～？\x02\x03",

            "#03809F僕もまた会いたいな～。\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0x9,
        (
            "#11P#03700Fふふ……そうね。\x01",
            "私も一度お会いしてみたいわ。\x02\x03",

            "皆さんは、その方について\x01",
            "ご存じないのでしょうか？\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0x102,
        (
            "#12P#00103F……残念ですが……\x01",
            "彼女についてはその後、\x01",
            "私たちも会っていなくて。\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0x8,
        (
            "#5P#03603Fふむ、そうですか……\x02\x03",

            "#03600Fまあ、ご縁があれば\x01",
            "いつか会うこともあるでしょう。\x02\x03",

            "気長にその機会を待つしか\x01",
            "ないのかもしれませんね。\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0x101,
        (
            "#12P#00003F（……“あの子”は、\x01",
            "  もう既にクロスベルを\x01",
            "  離れたんだよな……）\x02\x03",

            "#00008F（結局ハロルドさんたちにも\x01",
            "  事情を話さないまま\x01",
            "  だったらしいけど……）\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0x8,
        (
            "#5P#03600F……それではみなさん。\x01",
            "もし何かありましたら、\x01",
            "いつでもいらしてください。\x02\x03",

            "私で力になれることなら\x01",
            "なんでもお手伝いしますから。\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0x101,
        "#12P#00000Fええ、ありがとうございます。\x02",
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0xA,
        "#11P#03809Fえへへ、また来てね～。\x02",
    )

    CloseMessageWindow()
    OP_5A()
    SetChrSubChip(0x9, 0x0)
    SetChrSubChip(0xA, 0x0)
    Sleep(50)
    SetScenarioFlags(0x12F, 7)
    EventEnd(0x5)
    Return()

    # Function_14_3A12 end

    def Function_15_4185(): pass

    label("Function_15_4185")

    EventBegin(0x0)
    OP_4B(0xC, 0xFF)
    OP_4B(0x8, 0xFF)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-2040, 1500, 4340, 0)
    MoveCamera(44, 26, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(23010, 0)
    OP_93(0xC, 0x10E, 0x0)
    OP_93(0x8, 0x10E, 0x0)
    SetChrPos(0x101, -2360, 0, 4740, 90)
    SetChrPos(0x102, -2780, 0, 3340, 90)
    SetChrPos(0x103, -2620, 0, 2009, 45)
    SetChrPos(0x104, -3660, 0, 4220, 90)
    SetChrPos(0x109, -3080, 0, 5820, 90)
    SetChrPos(0x105, -2380, 0, 7190, 135)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x177, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4403")

    #C0118
    ChrTalk(
        0x101,
        (
            "#00000F失礼します、\x01",
            "特務支援課です。\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0xC,
        "おお、特務支援課の諸君……\x02",
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0xC,
        (
            "昨日に引き続き、\x01",
            "来てくれて感謝するぞい。\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0x8,
        "#03600Fありがとうございます、皆さん。\x02",
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0x101,
        (
            "#00005Fトルタ村長、\x01",
            "一体何があったんですか？\x02\x03",

            "#00003Fどうやら昨日の事件について\x01",
            "進展があったみたいですが。\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0xC,
        (
            "うむ……どうやら事態は\x01",
            "わしが考えていた以上に\x01",
            "深刻になっていたようでな。\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0xC,
        (
            "早速依頼について\x01",
            "話したいのだが……\x01",
            "構わないかね？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4481")

    label("loc_4403")


    #C0125
    ChrTalk(
        0xC,
        (
            "どうやら事態は\x01",
            "わしが考えていた以上に\x01",
            "深刻になっていたようじゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0xC,
        (
            "早速依頼について\x01",
            "話したいのだが……\x01",
            "構わないかね？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4481")

    Call(0, 16)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x0, -2190, 0, 4360, 225)
    OP_69(0xFF, 0x0)
    OP_93(0xC, 0x0, 0x0)
    OP_93(0x8, 0xB4, 0x0)
    OP_4C(0xC, 0xFF)
    OP_4C(0x8, 0xFF)
    EventEnd(0x5)
    Return()

    # Function_15_4185 end

    def Function_16_44C6(): pass

    label("Function_16_44C6")

    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【引き受ける】\x01",      # 0
            "【やめる】\x01",          # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_4530"),
        (1, "loc_4538"),
        (SWITCH_DEFAULT, "loc_45F6"),
    )


    label("loc_4530")

    Call(0, 17)
    Jump("loc_45F6")

    label("loc_4538")


    #C0127
    ChrTalk(
        0x101,
        (
            "#00006F申し訳ありません……\x01",
            "今はちょっと忙しくて。\x02",
        )
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0xC,
        "ううむ、そうかね……\x02",
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0xC,
        (
            "では、時間ができたら\x01",
            "もう一度来てくれ。\x02",
        )
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0xC,
        (
            "どうしても君たちに\x01",
            "力を貸してほしいのだよ。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x177, 1)

    label("loc_45F6")

    Return()

    # Function_16_44C6 end

    def Function_17_45F7(): pass

    label("Function_17_45F7")


    #C0131
    ChrTalk(
        0x101,
        "#00000Fええ、詳しくお聞かせください。\x02",
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0x102,
        (
            "#00100F昨日から、状況が進展したとの\x01",
            "ことでしたけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0xC,
        "うむ……そうなのだ。\x02",
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0xC,
        (
            "昨夜、宿酒場に泊まっていた\x01",
            "デリックのところに行って\x01",
            "改めて説得してみたのじゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0xC,
        (
            "あのミンネスという外国人は\x01",
            "怪しい所が多いから、\x01",
            "付き合うのはやめろとな。\x02",
        )
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0x104,
        (
            "#00306Fそりゃあ……\x01",
            "ストレートに言ったもんッスね。\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0xC,
        (
            "ああ、だが……\x01",
            "結局デリックは聞き耳を\x01",
            "もってはくれなかった。\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0xC,
        (
            "その代わり、\x01",
            "ある新しい事実をもらしおってな。\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0xC,
        (
            "急ぎ、ハロルド君のもとへ\x01",
            "相談に来たところだったのだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0x103,
        (
            "#00205F新事実……？\x02\x03",

            "あのミンネスという人が\x01",
            "何かしていたということですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0x8,
        (
            "#03603F相談されたときは\x01",
            "私も驚いたのですが……\x02\x03",

            "#03601Fミンネス氏は、どうやら予想以上に\x01",
            "村へと食い込んでいたようなのです。\x02",
        )
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0x102,
        (
            "#00105Fえっと……\x01",
            "つまり、どういうことなんですか？\x02\x03",

            "村人の皆さんに信用を得ていることは\x01",
            "昨日の段階で分かりましたけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0xC,
        "実はあのミンネスという男は……\x02",
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0xC,
        (
            "村の私有地だけでなく、\x01",
            "畑や土地の権利書を\x01",
            "集めていたようなのじゃ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0145
    ChrTalk(
        0x101,
        "#00005Fと、土地の権利書を……！？\x02",
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0x105,
        (
            "#10303Fふむ……しかしそうなると\x01",
            "気になる点があるね。\x02\x03",

            "#10301Fミンネスさんは一体どうやって\x01",
            "そんな大事なものを\x01",
            "手に入れていたというのかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0x8,
        (
            "#03601Fええ、聞くところによると……\x01",
            "名目は『レンゲ畑の拡大』と\x01",
            "いうことらしいのです。\x02\x03",

            "村人から少しずつ畑の土地を集め、\x01",
            "レンゲ畑を拡大する事で\x01",
            "その収穫をより効率的にする……\x02\x03",

            "#03603Fさらには、畑の管理を\x01",
            "クインシー社が請け負うことで\x01",
            "収穫などの労力を軽減できる……\x02",
        )
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0x109,
        (
            "#10101Fそのあたりは……\x01",
            "昨日聞いた話にもつながりますね。\x02\x03",

            "#10103F一見、いい話のように見えますけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0x101,
        (
            "#00001Fああ……\x01",
            "またも『上手すぎる話』だ。\x02\x03",

            "#00003Fしかも土地の権利書となると……\x01",
            "もし悪用されたとしたら\x01",
            "取り返しのつかないことになる。\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0xC,
        (
            "うむ……ミンネスという男の怪しさが\x01",
            "全く払拭されていない状況じゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0xC,
        (
            "私有地だけなら、\x01",
            "万が一何かあったとしても\x01",
            "人的な被害はほとんどないが……\x02",
        )
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0xC,
        (
            "村の中の土地に\x01",
            "そんな事が起こってるとは\x01",
            "思いもよらなかったのじゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0x104,
        (
            "#00301Fなるほど、のっぴきならねえ\x01",
            "状況と言えるかもしれねえな。\x02",
        )
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0xC,
        (
            "そこで、あんたたちには\x01",
            "より明確な形であの男の正体を\x01",
            "暴いてもらいたいと思っておる。\x02",
        )
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0xC,
        (
            "容疑が確定していない今の状況で\x01",
            "警察にこういったことを\x01",
            "頼めるものじゃろうか……？\x02",
        )
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0x101,
        (
            "#00003Fいえ……もともと俺たちは\x01",
            "警察の規律からは外れた存在です。\x02\x03",

            "#00000Fミンネスという男に\x01",
            "少しでも怪しい点がある今の状況……\x01",
            "謹んで捜査に当たらせてもらいます。\x02",
        )
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0xC,
        (
            "すまない……\x01",
            "あんたたちには\x01",
            "本当に世話になるのう。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)
    Sleep(300)

    #C0158
    ChrTalk(
        0x102,
        (
            "#00100Fそれじゃあ、どこから\x01",
            "手をつけるのがいいかしら？\x02\x03",

            "#00103F正直、今のところ\x01",
            "何の手がかりもないけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0x105,
        (
            "#10300F確かに、根拠と言えるものは\x01",
            "何もない状況だよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0x101,
        "#00006Fそうなんだよな……\x02",
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0x8,
        (
            "#03600Fそれでは皆さん……\x01",
            "まずはイアン先生に\x01",
            "相談してみるのはどうでしょう？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0x102, 0x5A, 0x1F4)
    Sleep(300)

    #C0162
    ChrTalk(
        0x103,
        "#00205Fイアン先生に……？\x02",
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0x8,
        (
            "#03600Fええ、今はミンネスという男が\x01",
            "“怪しい”という事しか\x01",
            "分かっていませんが……\x02\x03",

            "イアン先生に状況を説明すれば、\x01",
            "なんらかの犯罪への兆候を\x01",
            "読み取ってもらえるかもしれません。\x02",
        )
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0x101,
        (
            "#00004Fなるほど……\x01",
            "いい考えかも知れませんね。\x02\x03",

            "#00000F彼がやろうとしている事に\x01",
            "少しでも近づければ、\x01",
            "捜査の取っ掛かりになるかも……\x02",
        )
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0x8,
        (
            "#03603Fただ、イアン先生は最近、\x01",
            "例の独立宣言に関連して\x01",
            "相当忙しくしているようです。\x02\x03",

            "#03608Fもしかしたら、いらっしゃらない\x01",
            "可能性はあるかもしれませんが……\x02",
        )
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0x104,
        (
            "#00300Fま、なんにしろ\x01",
            "法律事務所に行くとしようぜ。\x02\x03",

            "いないならいないで、\x01",
            "そのとき考えりゃいいさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0x101,
        (
            "#00000Fああ……\x01",
            "早速訪ねてみよう。\x02",
        )
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0x8,
        (
            "#03600Fでは、そちらは\x01",
            "よろしくおねがいします。\x02\x03",

            "私も商売仲間などに\x01",
            "クインシー社やミンネス氏の噂を\x01",
            "当たってみようと思います。\x02",
        )
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0x103,
        (
            "#00200Fそれは……助かりますね。\x01",
            "よろしくお願いします。\x02",
        )
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0xC,
        (
            "すまぬな……\x01",
            "あんたたちだけが頼りじゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0xC,
        (
            "何もできない自分が\x01",
            "不甲斐ないが……\x02",
        )
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0x101,
        (
            "#00000Fいえ……\x01",
            "俺たちにお任せください。\x02",
        )
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0x105,
        (
            "#10300Fま、村長はここで\x01",
            "待ってるといいさ。\x02\x03",

            "いい報告ができることを\x01",
            "女神に祈っておいてよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0xC,
        (
            "うむ……\x01",
            "よろしく頼んだぞ。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(80, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0175
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "クエスト【不審商人の調査】\x07\x00",
            "を開始した！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x177, 2)
    OP_29(0x87, 0x1, 0x0)
    ClearChrFlags(0xC, 0x10)
    SetChrFlags(0x8, 0x80)
    SetChrPos(0x9, 550, 0, 2040, 180)
    SetChrPos(0xC, -10, 0, 5370, 270)
    SetChrPos(0x0, -2130, 0, 3860, 270)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_17_45F7 end

    def Function_18_5641(): pass

    label("Function_18_5641")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_4B(0xC, 0xFF)
    OP_4B(0x8, 0xFF)
    OP_4B(0xD, 0xFF)
    OP_68(-2330, 1500, 4180, 0)
    MoveCamera(57, 21, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25120, 0)
    SetChrPos(0xC, -690, 0, 3590, 270)
    SetChrPos(0x8, -490, 0, 5140, 270)
    SetChrPos(0xD, 660, 0, 4600, 270)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0xD, 0x80)
    OP_93(0xC, 0x10E, 0x0)
    OP_93(0x8, 0x10E, 0x0)
    SetChrPos(0x101, -2360, 0, 4740, 90)
    SetChrPos(0x102, -2780, 0, 3340, 90)
    SetChrPos(0x103, -2620, 0, 2009, 45)
    SetChrPos(0x104, -3660, 0, 4220, 90)
    SetChrPos(0x109, -3080, 0, 5820, 90)
    SetChrPos(0x105, -2380, 0, 7190, 135)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()

    #C0176
    ChrTalk(
        0xC,
        "おお、あんたたち……\x02",
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0xD,
        "#11P#02200Fどうやら戻ったようだね。\x02",
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0x101,
        (
            "#00000Fイアン先生……\x01",
            "来てくださったんですね。\x02\x03",

            "ハロルドさんも\x01",
            "戻ってきたみたいですし。\x02",
        )
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0x8,
        (
            "#03604Fええ、一通り商売仲間へ\x01",
            "聞き込みが終わりましたので。\x02\x03",

            "#03601Fそちらの首尾はどうですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0x101,
        (
            "#00000Fええ、おかげさまで\x01",
            "いろいろと掴むことができました。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x8, 500)
    Sleep(300)

    #C0181
    ChrTalk(
        0x102,
        (
            "#00100Fハロルドさんのほうでは\x01",
            "なにか分かった事がありますか？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x102, 500)
    Sleep(300)

    #C0182
    ChrTalk(
        0x8,
        (
            "#03603Fええ……一応は。\x02\x03",

            "#03608Fと言っても、\x01",
            "これが何を意味するのか……\x02",
        )
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0x105,
        (
            "#10302Fフフ、せっかくの情報だ。\x01",
            "何でもいいから話してみたら\x01",
            "いいじゃない。\x02",
        )
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0x103,
        (
            "#00200Fええ、お願いします。\x01",
            "何か現状の情報と\x01",
            "結びつくかもしれませんし。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 500)
    Sleep(300)

    #C0185
    ChrTalk(
        0x8,
        (
            "#03603F確かに……それもそうですね。\x02\x03",

            "#03601F私はミンネスという名前に\x01",
            "心当たりがないか、\x01",
            "貿易仲間たちを尋ねて回りました。\x02\x03",

            "すると……どうやらミンネス氏は、\x01",
            "クロスベル入りした頃に、\x01",
            "ある事を調べていたようなのです。\x02",
        )
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0x102,
        "#00105Fある事……というと？\x02",
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0x8,
        (
            "#03601Fええ、それは……\x01",
            "クロスベル各地の\x01",
            "『地価』なんだそうです。\x02",
        )
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0x104,
        "#00305F『地価』ねえ……\x02",
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0x109,
        (
            "#10103Fミンネス氏が不動産屋のような\x01",
            "ことをしていた訳ですね……\x02\x03",

            "#10105Fでも、なんでそんな事を\x01",
            "調べる必要が……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)

    #C0190
    ChrTalk(
        0x101,
        (
            "#00001Fもしかすると……\x01",
            "これはミンネスの目的につながる\x01",
            "重要な証言かもしれない。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0191
    ChrTalk(
        0xC,
        "ほ、本当かね？\x02",
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0xD,
        (
            "#11P#02203Fふむ、一理あるかもしれんな。\x02\x03",

            "#02200Fそれに、私のほうでも\x01",
            "役に立てそうな事を見つけたよ。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x102, 0x5A, 0x1F4)
    Sleep(300)

    #C0193
    ChrTalk(
        0x101,
        "#00005Fえ……？\x02",
    )

    CloseMessageWindow()

    #C0194
    ChrTalk(
        0xD,
        (
            "#11P#02200Fハロルド君、それにトルタ村長。\x02\x03",

            "これから私の事務所で、\x01",
            "探し物を手伝ってくれないかね？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5DEC():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_5DEC)
    Sleep(50)

    def lambda_5DFC():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_5DFC)
    Sleep(300)

    #C0195
    ChrTalk(
        0x8,
        "#03605Fイアン先生……？\x02",
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0xC,
        (
            "わしらは構わんが……\x01",
            "何か重要なものなのかね？\x02",
        )
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0xD,
        (
            "#11P#02203Fいや、そこまで決定力のある\x01",
            "証拠にはならないでしょうが……\x02\x03",

            "#02200Fミンネスとやらを追い詰めたあとの、\x01",
            "ダメ押し程度にはなるかもしれません。\x02",
        )
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0x104,
        "#00305Fんん～？　よくわかんねえが……\x02",
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0xD,
        (
            "#11P#02200Fまあ、間に合うかは分からないから\x01",
            "あまり期待はしないでくれ。\x02\x03",

            "#02203Fそれよりも、支援課諸君。\x01",
            "君たちはアルモリカ村に\x01",
            "急いだほうがいいだろう。\x02\x03",

            "#02200Fミンネスという男が本当に詐欺師なら、\x01",
            "計画は最終局面にまで\x01",
            "進行していてもおかしくない。\x02\x03",

            "だが、君たちならきっと、\x01",
            "手持ちの証拠で何とかできるはずだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0x101,
        "#00001F……そうですね、分かりました！\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0x10E, 0x1F4)
    Sleep(300)

    #C0201
    ChrTalk(
        0x101,
        (
            "#00001Fそれじゃあ皆……\x01",
            "さっそくアルモリカ村に向かおう。\x02\x03",

            "あのミンネスの正体を暴いて、\x01",
            "これ以上の取引きを阻止するんだ！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_610C():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_610C)
    Sleep(50)

    def lambda_611C():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_611C)
    Sleep(50)

    def lambda_612C():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_612C)
    Sleep(50)

    def lambda_613C():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_613C)
    Sleep(50)

    def lambda_614C():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_614C)
    Sleep(300)

    #C0202
    ChrTalk(
        0x102,
        "#00101Fええ……行きましょう！\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_29(0x87, 0x1, 0x5)
    SetScenarioFlags(0x177, 6)
    ClearMapFlags(0x10000000)
    OP_93(0x8, 0xB4, 0x0)
    OP_93(0xC, 0x0, 0x0)
    OP_4C(0xC, 0xFF)
    OP_4C(0x8, 0xFF)
    OP_4C(0xD, 0xFF)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x0, -2130, 0, 3860, 270)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_18_5641 end

    SaveToFile()

Try(main)
