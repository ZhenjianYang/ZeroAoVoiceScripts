from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c1010.bin",                # FileName
        "c1010",                    # MapName
        "c1010",                    # Location
        0x0013,                     # MapIndex
        "ed7100",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 19, 0, 1, 0, 2],
    )

    BuildStringList((
        "c1010",                  # 0
        "受付ミシェル",           # 1
        "アリオス",               # 2
        "アリオス",               # 3
        "エステル",               # 4
        "エステル",               # 5
        "ヨシュア",               # 6
        "ヨシュア",               # 7
        "遊撃士スコット",         # 8
        "遊撃士スコット",         # 9
        "遊撃士ヴェンツェル",     # 10
        "遊撃士リン",             # 11
        "遊撃士エオリア",         # 12
        "シズク",                 # 13
    ))

    AddCharChip((
        "chr/ch09100.itc",                   # 00
        "chr/ch02400.itc",                   # 01
        "chr/ch00600.itc",                   # 02
        "chr/ch00700.itc",                   # 03
        "chr/ch27200.itc",                   # 04
        "chr/ch27300.itc",                   # 05
        "chr/ch32100.itc",                   # 06
        "chr/ch02402.itc",                   # 07
        "chr/ch00602.itc",                   # 08
        "chr/ch00702.itc",                   # 09
        "chr/ch27202.itc",                   # 0A
        "chr/ch32002.itc",                   # 0B
        "chr/ch00000.itc",                   # 0C
        "chr/ch27302.itc",                   # 0D
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

    DeclNpc(1000,    0,       12819,   180,  261,  0x0, 0,   0,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(970,     0,       10300,   0,    389,  0x0, 0,   1,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(-5900,   150,     49279,   180,  469,  0x0, 0,   7,   0,   255, 255, 0,   6,   255,  0)
    DeclNpc(1559,    0,       10220,   0,    389,  0x0, 0,   2,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(-5900,   150,     49279,   180,  469,  0x0, 0,   8,   0,   255, 255, 0,   8,   255,  0)
    DeclNpc(180,     0,       9859,    0,    389,  0x0, 0,   3,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(-8430,   150,     49189,   180,  469,  0x0, 0,   9,   0,   255, 255, 0,   10,  255,  0)
    DeclNpc(-4780,   0,       52229,   315,  389,  0x0, 0,   4,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(-8430,   150,     46919,   0,    469,  0x0, 0,   10,  0,   255, 255, 0,   12,  255,  0)
    DeclNpc(-6320,   0,       52229,   45,   389,  0x0, 0,   5,   0,   0,   0,   0,   13,  255,  0)
    DeclNpc(-6000,   150,     46930,   0,    469,  0x0, 0,   11,  0,   255, 255, 0,   14,  255,  0)
    DeclNpc(-5099,   0,       51909,   270,  405,  0x0, 0,   6,   0,   0,   0,   0,   15,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclActor(5500,    0,       6000,    1200,    5500,    1500,    6000,    0x007C, 0,  16, 0x0000)
    DeclActor(8000,    0,       6000,    1200,    8000,    1500,    6000,    0x007C, 0,  37, 0x0000)
    DeclActor(5500,    0,       2500,    1200,    5500,    1500,    2500,    0x007C, 0,  37, 0x0000)
    DeclActor(8000,    0,       2500,    1200,    8000,    1500,    2500,    0x007C, 0,  37, 0x0000)
    DeclActor(680,     0,       11370,   1700,    1000,    1500,    12820,   0x007E, 0,  3,  0x0000)

    ScpFunction((
        "Function_0_3C4",          # 00, 0
        "Function_1_47C",          # 01, 1
        "Function_2_72E",          # 02, 2
        "Function_3_792",          # 03, 3
        "Function_4_796",          # 04, 4
        "Function_5_2C01",         # 05, 5
        "Function_6_318C",         # 06, 6
        "Function_7_3BED",         # 07, 7
        "Function_8_3C73",         # 08, 8
        "Function_9_4052",         # 09, 9
        "Function_10_4182",        # 0A, 10
        "Function_11_45F5",        # 0B, 11
        "Function_12_4821",        # 0C, 12
        "Function_13_4CC6",        # 0D, 13
        "Function_14_5270",        # 0E, 14
        "Function_15_59D0",        # 0F, 15
        "Function_16_5DEE",        # 10, 16
        "Function_17_6D6B",        # 11, 17
        "Function_18_714D",        # 12, 18
        "Function_19_7496",        # 13, 19
        "Function_20_7A84",        # 14, 20
        "Function_21_80E2",        # 15, 21
        "Function_22_8BCE",        # 16, 22
        "Function_23_946A",        # 17, 23
        "Function_24_962C",        # 18, 24
        "Function_25_9726",        # 19, 25
        "Function_26_EBB1",        # 1A, 26
        "Function_27_F4AF",        # 1B, 27
        "Function_28_10486",       # 1C, 28
        "Function_29_104D1",       # 1D, 29
        "Function_30_1052C",       # 1E, 30
        "Function_31_10587",       # 1F, 31
        "Function_32_13772",       # 20, 32
        "Function_33_13798",       # 21, 33
        "Function_34_159A2",       # 22, 34
        "Function_35_159F7",       # 23, 35
        "Function_36_15A6D",       # 24, 36
        "Function_37_15AC5",       # 25, 37
    ))


    def Function_0_3C4(): pass

    label("Function_0_3C4")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_404"),
        (1, "loc_410"),
        (2, "loc_41C"),
        (3, "loc_428"),
        (4, "loc_434"),
        (5, "loc_440"),
        (6, "loc_44C"),
        (SWITCH_DEFAULT, "loc_458"),
    )


    label("loc_404")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_464")

    label("loc_410")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_464")

    label("loc_41C")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_464")

    label("loc_428")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_464")

    label("loc_434")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_464")

    label("loc_440")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_464")

    label("loc_44C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_464")

    label("loc_458")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_464")

    label("loc_464")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_47B")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_464")

    label("loc_47B")

    Return()

    # Function_0_3C4 end

    def Function_1_47C(): pass

    label("Function_1_47C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_48A")
    Jump("loc_6DE")

    label("loc_48A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_498")
    Jump("loc_6DE")

    label("loc_498")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_END)), "loc_4AB")
    ClearChrFlags(0xA, 0x80)
    Jump("loc_6DE")

    label("loc_4AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_501")
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x11, -6640, 0, 51900, 90)
    SetChrFlags(0x11, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCF, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4FC")
    SetChrFlags(0x8, 0x10)

    label("loc_4FC")

    Jump("loc_6DE")

    label("loc_501")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_50F")
    Jump("loc_6DE")

    label("loc_50F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_549")
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xC, -8400, 150, 49200, 180)
    SetChrPos(0xE, -10700, 150, 49200, 180)
    Jump("loc_6DE")

    label("loc_549")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_583")
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0xF, 2220, 0, 4610, 90)
    SetChrPos(0x11, 3840, 0, 4540, 270)
    Jump("loc_6DE")

    label("loc_583")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_5D8")
    ClearChrFlags(0x11, 0x80)
    SetChrChipByIndex(0x11, 0xD)
    SetChrSubChip(0x11, 0x0)
    EndChrThread(0x11, 0x0)
    SetChrFlags(0x11, 0x4)
    SetChrFlags(0x11, 0x10)
    SetChrPos(0x11, -6030, 0, 46890, 0)
    SetChrFlags(0x11, 0x10)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, -5960, 150, 49360, 180)
    Jump("loc_6DE")

    label("loc_5D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_601")
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 600, 0, 39580, 90)
    SetChrFlags(0x9, 0x10)
    Jump("loc_6DE")

    label("loc_601")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_614")
    ClearChrFlags(0xA, 0x80)
    Jump("loc_6DE")

    label("loc_614")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_63A")
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xD, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6D, 2)), scpexpr(EXPR_END)), "loc_635")
    SetChrFlags(0x8, 0x10)

    label("loc_635")

    Jump("loc_6DE")

    label("loc_63A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_679")
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, -5930, 150, 43070, 180)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x13, 0x10)
    SetChrPos(0x13, -4610, 0, 43390, 225)
    Jump("loc_6DE")

    label("loc_679")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_68C")
    ClearChrFlags(0xA, 0x80)
    Jump("loc_6DE")

    label("loc_68C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_6CB")
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, -5930, 150, 43070, 180)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x13, 0x10)
    SetChrPos(0x13, -4610, 0, 43390, 225)
    Jump("loc_6DE")

    label("loc_6CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_6DE")
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x11, 0x80)

    label("loc_6DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6F4")
    SetMapFlags(0x10000000)
    Event(0, 31)

    label("loc_6F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_708")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 27)
    Jump("loc_717")

    label("loc_708")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 1)), scpexpr(EXPR_END)), "loc_717")
    ClearScenarioFlags(0x5C, 1)
    Event(0, 33)

    label("loc_717")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_72D")
    Event(0, 21)

    label("loc_72D")

    Return()

    # Function_1_47C end

    def Function_2_72E(): pass

    label("Function_2_72E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x43, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_745")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_745")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_761")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    Jump("loc_778")

    label("loc_761")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_778")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    Jump("loc_778")

    label("loc_778")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_791")
    SetMapObjFrame(0xFF, "red_", 0x2, "on")

    label("loc_791")

    Return()

    # Function_2_72E end

    def Function_3_792(): pass

    label("Function_3_792")

    Call(0, 4)
    Return()

    # Function_3_792 end

    def Function_4_796(): pass

    label("Function_4_796")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_8C0")

    #C0001
    ChrTalk(
        0x8,
        (
            "ウチのメンバーには\x01",
            "各地の捜索を割り当てたわ。\x01",
            "市外については任せてくれてＯＫよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x8,
        (
            "アナタたちは気兼ねなく\x01",
            "薬物調査の方を進めてちょうだい。\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0x8,
        (
            "それと、くれぐれも\x01",
            "シズクちゃんのことを頼むわよ！\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x102,
        "#0100Fええ、それはもう。\x02",
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x101,
        (
            "#0000F責任をもって\x01",
            "預からせていただきます。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2BFD")

    label("loc_8C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_8CE")
    Jump("loc_2BFD")

    label("loc_8CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_DFE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCF, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D21")

    #C0006
    ChrTalk(
        0x8,
        (
            "あら、アナタたち。\x01",
            "何だか余裕が無さそうね。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x8,
        (
            "まさかマフィアたちの抗争に\x01",
            "進展でもあったのかしら？\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x101,
        "#0003Fいえ、それとは別なんですが……\x02",
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x8,
        (
            "あら、だったら……\x01",
            "ひょっとして行方不明者の件？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1200)

    #C0010
    ChrTalk(
        0x101,
        (
            "#0005Fギルドの方でも\x01",
            "掴んでいたんですか！？\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x8,
        (
            "ええ、ちょうど\x01",
            "アリオスが調べている所よ。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x8,
        (
            "ただ、そっちの方でも\x01",
            "問題になっているという事は……\x01",
            "かなり深刻かもしれないわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x8,
        (
            "消えたのは１人や２人じゃ\x01",
            "きかないかもしれないわよ？\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x104,
        "#0301F確かにな……\x02",
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x103,
        (
            "#0200Fできれば情報交換を\x01",
            "しておきたい所ですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x8,
        (
            "あら、こっちの方は\x01",
            "むしろ大歓迎だけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x8,
        (
            "そっちはいいの？\x01",
            "支援課だけで判断してしまって。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x1, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x2, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x3, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0x0)
    OP_64(0x1)
    OP_64(0x2)
    OP_64(0x3)
    Sleep(300)

    #C0018
    ChrTalk(
        0x101,
        (
            "#0003F（確かに一課から資料を借りてる手前、\x01",
            "  外に捜査情報をもらす訳にも……）\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x102,
        (
            "#0108F（ダドリーさんあたりが知ったら\x01",
            "  目を剥いて怒りそうね……）\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x8,
        (
            "ま、そのあたりの折り合いが\x01",
            "付いたら来てちょうだい。\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x8,
        (
            "アリオスが戻ってきたら\x01",
            "こちらの情報も整理しておくから。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xCF, 3)
    Jump("loc_DF9")

    label("loc_D21")


    #C0022
    ChrTalk(
        0x8,
        (
            "あ、そうそう、ちょうど今、\x01",
            "シズクちゃんが街に来てるのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x8,
        (
            "調査に出たアリオスの代わりに\x01",
            "エステルちゃんたちが遊びに\x01",
            "連れていってくれてるけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x8,
        (
            "うーん、シズクちゃんには\x01",
            "申しわけない事をしちゃったわね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DF9")

    Jump("loc_2BFD")

    label("loc_DFE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_END)), "loc_EC5")

    #C0025
    ChrTalk(
        0x8,
        (
            "ようやく状況が掴めたけど\x01",
            "今すぐ本格的な抗争が起こる\x01",
            "雰囲気では無さそうね。\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x8,
        "ただ、予断は許さない状況よ。\x02",
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x8,
        (
            "いつでもメンバーを動かせるよう、\x01",
            "シフトを組みなおしておかないと。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2BFD")

    label("loc_EC5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_F96")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCF, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EE0")
    Call(0, 5)
    Jump("loc_F91")

    label("loc_EE0")


    #C0028
    ChrTalk(
        0x8,
        (
            "《黒月》を襲撃したのは\x01",
            "間違いなくルバーチェとして……\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x8,
        (
            "問題は、どうしてこの状況で\x01",
            "突発的に事を起こしたかよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x8,
        (
            "ふむ……とにかく状況を\x01",
            "正確に見極めておきたい所ね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F91")

    Jump("loc_2BFD")

    label("loc_F96")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_14A2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCF, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11D8")

    #C0031
    ChrTalk(
        0x8,
        (
            "あら、支援課の坊やたち。\x01",
            "２週間ぶりくらいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x8,
        (
            "……悪いわね、\x01",
            "キーアちゃんの情報の事。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x103,
        (
            "#0200Fギルドの情報網でも\x01",
            "まだ掴めてないんですよね？\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x8,
        (
            "ええ、噂の一つくらいは\x01",
            "引っかかると思ったんだけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x101,
        (
            "#0003Fいや、いいんです。\x01",
            "キーアもすっかり支援課に\x01",
            "馴染んでしまいましたし。\x02\x03",

            "#0000F身元や記憶を探るよりも\x01",
            "日常の生活を優先してやりたいと\x01",
            "思っているので。\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x8,
        (
            "そう……\x01",
            "ま、それも判断の一つよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x8,
        (
            "一応引き続き\x01",
            "調査の方は続けさせてもらうわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x8,
        (
            "そっちも、また何か判ったら\x01",
            "連絡してちょうだい。\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x102,
        "#0100Fええ、よろしくお願いします。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0xCF, 1)
    Jump("loc_149D")

    label("loc_11D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13E9")

    #C0040
    ChrTalk(
        0x8,
        (
            "アリオスは先週から\x01",
            "帝国方面に飛んでいるわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x8,
        (
            "かなり面倒な仕事だったけど\x01",
            "そろそろ戻ってくるはずよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x104,
        (
            "#0305Fへえ、なんか向こうで\x01",
            "デカイ事件でもあったとか？\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x8,
        (
            "大事件ってほどでもないけど、\x01",
            "向こうのギルド支部が\x01",
            "軍部と揉めちゃってね。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x8,
        (
            "今だと、調停できるのが\x01",
            "アリオスくらいしか居ないのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x8,
        (
            "前はリベールにもう一人、\x01",
            "打ってつけの人がいたんだけど\x01",
            "遊撃士を辞めちゃってねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x102,
        "#0106Fそ、それは大変ですね。\x02",
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x8,
        "そうよ、大変なのよ。\x02",
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x8,
        (
            "高位の遊撃士になるほど\x01",
            "この手の面倒事が増えるのよねぇ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_149D")

    label("loc_13E9")


    #C0049
    ChrTalk(
        0x8,
        (
            "ちなみに帝国政府と\x01",
            "遊撃士協会の関係は\x01",
            "あまりよろしくないのよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x8,
        (
            "その点だけはクロスベルは\x01",
            "恵まれているわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x8,
        (
            "市民からの支持も高いし、\x01",
            "政府からも信頼されているもの。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_149D")

    Jump("loc_2BFD")

    label("loc_14A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_1689")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1612")

    #C0052
    ChrTalk(
        0x8,
        (
            "キーアちゃんの身元は\x01",
            "大陸全土の遊撃士協会の\x01",
            "情報網を使って調べてみるわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x8,
        (
            "簡単な報告なら１週間、\x01",
            "詳しく調べるなら１ヶ月って所ね。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_157B")

    #C0054
    ChrTalk(
        0x102,
        "#0105Fいつもながら速いですね……\x02",
    )

    CloseMessageWindow()
    Jump("loc_15E8")

    label("loc_157B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_15B6")

    #C0055
    ChrTalk(
        0x103,
        "#0200Fいつもながら速いですね……\x02",
    )

    CloseMessageWindow()
    Jump("loc_15E8")

    label("loc_15B6")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_15E8")

    #C0056
    ChrTalk(
        0x104,
        "#0306Fいつもながら速いな……\x02",
    )

    CloseMessageWindow()

    label("loc_15E8")


    #C0057
    ChrTalk(
        0x101,
        "#0000Fよろしくお願いします。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1684")

    label("loc_1612")


    #C0058
    ChrTalk(
        0x8,
        (
            "遊撃士協会は大陸全土に\x01",
            "独自の情報網を持っているわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x8,
        (
            "まあ、絶対とは言えないけど\x01",
            "大抵の身元は判るはずよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1684")

    Jump("loc_2BFD")

    label("loc_1689")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_18B4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17EC")

    #C0060
    ChrTalk(
        0x8,
        (
            "あら……支援課じゃない。\x01",
            "どこかへ出かけるのかしら？\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x101,
        (
            "#0000Fええ、ちょっと\x01",
            "ウルスラ間道の遺跡へ。\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x8,
        (
            "『星見の塔』か……\x01",
            "警備隊が封鎖してるハズだけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x8,
        (
            "あの辺りは手強い魔獣が\x01",
            "出没する事があるのよ。\x01",
            "準備は怠らないことねえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x102,
        "#0100Fええ、気をつけます。\x02",
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x103,
        (
            "#0203F（……いつも意外と\x01",
            "  面倒見がいいんですよね。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_18AF")

    label("loc_17EC")


    #C0066
    ChrTalk(
        0x8,
        (
            "ふう……アナタたちが訪ねてくると\x01",
            "ついつい世話を焼いちゃうわねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x8,
        (
            "まあいいわ、『星見の塔』に行くなら\x01",
            "十分に準備しておきなさい。\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x8,
        (
            "あの辺り、手強い魔獣が\x01",
            "出没することがあるんだから。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18AF")

    Jump("loc_2BFD")

    label("loc_18B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_1BA7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B02")

    #C0069
    ChrTalk(
        0x8,
        (
            "そういえば、アルカンシェルの\x01",
            "新作公演も近づいて来たわねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x8,
        (
            "アタシも早速、来月分の\x01",
            "チケットを購入しちゃったわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x104,
        "#0300Fへえ、よく取れたモンだぜ。\x02",
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0x102,
        (
            "#0100Fやっぱりミシェルさんも\x01",
            "イリアさんのファンなんですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0x8,
        (
            "ファンというより、\x01",
            "同志といった感じかしら。\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x8,
        (
            "ホラ、アタシも見ての通り、\x01",
            "この罪作りな美貌でしょ？\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0x8,
        (
            "同じ美を追求する者として\x01",
            "イリア・プラティエには\x01",
            "共感を覚えちゃうのよねぇ㈱\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x1, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x2, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x3, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x0)
    OP_64(0x1)
    OP_64(0x2)
    OP_64(0x3)
    Sleep(300)
    OP_63(0x8, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(500)

    #C0076
    ChrTalk(
        0x8,
        (
            "ちょっと。\x01",
            "何か返しなさいよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1BA2")

    label("loc_1B02")


    #C0077
    ChrTalk(
        0x8,
        (
            "イリアもいいけど、\x01",
            "あの胸の大きい新人の子も\x01",
            "なかなか期待できそうねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0x8,
        (
            "ま、アタシとしては\x01",
            "テオ＆ユージーンの美形コンビの\x01",
            "立ち回りが楽しみなんだけど㈱\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BA2")

    Jump("loc_2BFD")

    label("loc_1BA7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_1E28")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1DA5")

    #C0079
    ChrTalk(
        0x8,
        (
            "ルバーチェはクロスベルに\x01",
            "根を張っているマフィア組織……\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0x8,
        (
            "犯罪や違法行為が服を着て\x01",
            "歩いてるようなものでしょうね。\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0x8,
        (
            "でも、議員や政府高官みたいな\x01",
            "有力者を味方にしているから\x01",
            "こちらも介入しにくいのよねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x8,
        (
            "ま、民間人に手を出したら\x01",
            "速攻で出張らせてもらうけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x101,
        (
            "#0003Fその辺りのフットワークは\x01",
            "さすが警察より優秀ですね……\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x104,
        (
            "#0306Fいつも遊撃士が片付けた\x01",
            "後だったりするんだよなぁ……\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0x8,
        (
            "そうねえ、アナタたちも\x01",
            "もう少し機敏に動いてくれると\x01",
            "こっちも助かるんだけど。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1E23")

    label("loc_1DA5")


    #C0086
    ChrTalk(
        0x8,
        (
            "ウチにも規約ってものがあるから、\x01",
            "政治が絡むと介入しにくいのよねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x8,
        (
            "民間人に手を出したら\x01",
            "遠慮なく出張れるんだけど。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E23")

    Jump("loc_2BFD")

    label("loc_1E28")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_1FF0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F1C")

    #C0088
    ChrTalk(
        0x8,
        (
            "最近、ルバーチェの連中、\x01",
            "動きが活発になってるわねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0x8,
        (
            "ウチに回ってくる依頼も\x01",
            "ソレっぽいのが急増中だわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x8,
        (
            "ま、警察が頼りにならない分、\x01",
            "ウチに相談してくるんでしょうね。\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x101,
        "#0003F（返す言葉もないな……）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1FEB")

    label("loc_1F1C")


    #C0092
    ChrTalk(
        0x8,
        (
            "ちなみにエステルちゃんたちは\x01",
            "自宅にいると思うわよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x8,
        (
            "……しかしまぁ、\x01",
            "アリオスほどじゃないけれど\x01",
            "あの２人も働き者よね～。\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x8,
        (
            "昨日も遅くまで仕事して\x01",
            "もらっちゃったし……\x01",
            "ふふ、これからが楽しみね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1FEB")

    Jump("loc_2BFD")

    label("loc_1FF0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_2193")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6D, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_200B")
    Call(0, 17)
    Jump("loc_218E")

    label("loc_200B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_20EF")
    OP_4B(0xB, 0xFF)
    OP_4B(0xD, 0xFF)

    #C0095
    ChrTalk(
        0x8,
        (
            "まあいいわ、今日は幾つか\x01",
            "難しい仕事をやってもらうわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0x8,
        (
            "出張中のアリオスの代理だけど\x01",
            "アナタたちなら十分こなせるハズよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0x8,
        "よろしくお願いするわね。\x02",
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0xB,
        "#2Pはいっ！\x02",
    )


    #C0099
    ChrTalk(
        0xD,
        "#3Pはいっ！\x02",
    )

    OP_57(0x1)
    OP_4C(0xB, 0xFF)
    OP_4C(0xD, 0xFF)
    SetScenarioFlags(0x0, 0)
    Jump("loc_218E")

    label("loc_20EF")


    #C0100
    ChrTalk(
        0x8,
        (
            "それじゃあ、幾つか\x01",
            "関連する資料を渡すわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0x8,
        (
            "まずは今回の仕事を\x01",
            "リストにした物だけど──\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x101,
        (
            "#0003F（忙しそうだな……\x01",
            "  邪魔するのは止めておこう。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_218E")

    Jump("loc_2BFD")

    label("loc_2193")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_22D6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2253")

    #C0103
    ChrTalk(
        0x8,
        (
            "クロスベルの警備隊が\x01",
            "色々と動いているみたいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0x8,
        (
            "ま、あそこは司令はともかく\x01",
            "副司令さんは優秀みたいだから。\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0x8,
        (
            "こちらはしばらく\x01",
            "様子見しておきましょうか。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_22D1")

    label("loc_2253")


    #C0106
    ChrTalk(
        0x8,
        (
            "ちなみにアリオスなら\x01",
            "共和国へ出張に出かけたわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0x8,
        (
            "ふう、本当に仕事の虫なんだから。\x01",
            "一度休みを取らせないとダメかしら。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_22D1")

    Jump("loc_2BFD")

    label("loc_22D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_25AE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2547")

    #C0108
    ChrTalk(
        0x8,
        "あら、坊やたちじゃない。\x02",
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0x8,
        (
            "わざわざ商売敵の所に\x01",
            "来るなんてヒマなのかしら？\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0x8,
        (
            "よかったらこちらの仕事でも\x01",
            "回してあげようかしら？\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0x101,
        (
            "#0005Fい、いえ。\x01",
            "これでも任務中なので。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2440")

    #C0112
    ChrTalk(
        0x101,
        (
            "#0001F（遊撃士協会・クロスベル支部の\x01",
            "  受付をしているミシェルさんか……）\x02\x03",

            "#0006F（少し前に知り合ったけど\x01",
            "  どうも半人前扱いされてるんだよな。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2440")


    #C0113
    ChrTalk(
        0x8,
        "あらそう、残念。\x02",
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0x8,
        (
            "……ま、アナタたちもそろそろ\x01",
            "焦った方がいいかもしれないわね。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    #C0115
    ChrTalk(
        0x101,
        "#0005Fえ……\x02",
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0x104,
        "#0305Fなんだ、そりゃ？\x02",
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0x8,
        (
            "ウフフ……\x01",
            "何でもないわ、こっちの話よ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_25A9")

    label("loc_2547")


    #C0118
    ChrTalk(
        0x8,
        (
            "任務中なんでしょ？\x01",
            "とっとと行きなさいな。\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0x8,
        (
            "モタモタしてると\x01",
            "またウチが解決しちゃうわよ？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_25A9")

    Jump("loc_2BFD")

    label("loc_25AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_2782")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x4, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2766")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_2642")

    #C0120
    ChrTalk(
        0x8,
        (
            "まぁ、せいぜいこれから\x01",
            "がんばりなさいな。\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0x8,
        (
            "私たちの邪魔に\x01",
            "ならないくらいには\x01",
            "成長してくれると助かるわ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2761")

    label("loc_2642")


    #C0122
    ChrTalk(
        0x8,
        "うふふ、テストお疲れ様。\x02",
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0x8,
        (
            "おかげでアナタたちの今のレベルが\x01",
            "なんとなく分かったわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0x103,
        "#0205F……あの程度のテストでですか？\x02",
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0x8,
        "あの程度のテストだからこそ、よ。\x02",
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0x8,
        (
            "まぁ、せいぜいこれから\x01",
            "がんばりなさいな。\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0x8,
        (
            "私たちの邪魔に\x01",
            "ならないくらいには\x01",
            "成長してくれると助かるわ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_2761")

    Jump("loc_277D")

    label("loc_2766")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x4, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_277A")
    Call(0, 23)
    Jump("loc_277D")

    label("loc_277A")

    Call(0, 22)

    label("loc_277D")

    Jump("loc_2BFD")

    label("loc_2782")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_2BFD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B66")

    #C0128
    ChrTalk(
        0x8,
        "しかし『特務支援課』ねぇ……\x02",
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0x8,
        (
            "警察内部のしがらみと\x01",
            "ゴタゴタで生まれた部署って\x01",
            "聞いたけど、本当なのかしら？\x02",
        )
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0x101,
        (
            "#0006Fうぐっ……\x01",
            "よ、よくご存知ですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0x8,
        (
            "ギルドの情報網を\x01",
            "侮ってもらっちゃ困るわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0x8,
        (
            "ここには周辺諸国の噂や情報が\x01",
            "逐一入ってくるわよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0x8,
        (
            "その気になれば\x01",
            "エレボニアの帝都にいるイイ男の\x01",
            "数だって調べられるんだから。\x02",
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
    Sleep(1200)

    #C0134
    ChrTalk(
        0x104,
        (
            "#0300F（たしかにギルドの\x01",
            "  情報網っていやあ有名だが、\x01",
            "  例えがアレだなぁ……）\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    #C0135
    ChrTalk(
        0x8,
        (
            "でも、そうね。\x01",
            "今後のこともあるワケだし……\x02",
        )
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0x8,
        (
            "──アナタたち。\x01",
            "よかったら後でまた来なさい。\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0x8,
        (
            "お近づきの印に\x01",
            "面白い趣向を用意しとくわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0x101,
        "#0005Fへ……\x02",
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0x102,
        "#0105Fあの、面白い趣向って……\x02",
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0x8,
        (
            "アナタたちの実力を\x01",
            "見極めさせてもらうだけよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0x8,
        (
            "ウフフ、安心しなさい。\x01",
            "別に取って喰いやしないから。\x02",
        )
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0x104,
        "#0303F（あからさまに怪しいな……）\x02",
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0x103,
        (
            "#0200F（というか、そもそもどうして\x01",
            "  女性言葉なんでしょう……？）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x4F, 6)
    Jump("loc_2BFD")

    label("loc_2B66")


    #C0144
    ChrTalk(
        0x8,
        (
            "アナタたち。\x01",
            "よかったら後でまた来なさい。\x02",
        )
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0x8,
        (
            "お近づきの印に\x01",
            "面白い趣向を用意しとくわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0x8,
        (
            "ウフフ、安心しなさい。\x01",
            "別に取って喰いやしないから。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2BFD")

    TalkEnd(0x8)
    Return()

    # Function_4_796 end

    def Function_5_2C01(): pass

    label("Function_5_2C01")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_2F0A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCF, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E6E")
    OP_4B(0x8, 0xFF)
    OP_4B(0x9, 0xFF)
    TurnDirection(0x8, 0x0, 0)
    TurnDirection(0x9, 0x0, 0)

    #C0147
    ChrTalk(
        0x8,
        "あら、支援課の坊やたち。\x02",
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0x9,
        (
            "#1401Fお前たちか……\x01",
            "話は聞いているようだな？\x02",
        )
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0x101,
        (
            "#0001Fええ、その様子だと\x01",
            "そちらもご存知のようですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0x8,
        "当たり前でしょ。\x02",
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0x8,
        (
            "さっき全員に連絡して\x01",
            "２階に集まってもらった所よ。\x02",
        )
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0x8,
        (
            "マフィア同士の\x01",
            "全面抗争の危険に備えてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0x102,
        "#0105Fさ、さすがですね……\x02",
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0x104,
        (
            "#0306Fやれやれ、警察の方が\x01",
            "完全に出遅れてるみたいだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0x9,
        (
            "#1403Fまあ、お互い役目と\x01",
            "やり方が違うというだけだ。\x02\x03",

            "#1400F俺たちは俺たちのやり方で\x01",
            "有事に備えておく……\x02\x03",

            "お前たちはお前たちなりの\x01",
            "やり方で動くといいだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0x101,
        "#0001Fはい……！\x02",
    )

    CloseMessageWindow()
    OP_93(0x8, 0xB4, 0x0)
    OP_93(0x9, 0x0, 0x0)
    OP_4C(0x8, 0xFF)
    OP_4C(0x9, 0xFF)
    ClearChrFlags(0x8, 0x10)
    SetScenarioFlags(0xCF, 2)
    Jump("loc_2F05")

    label("loc_2E6E")


    #C0157
    ChrTalk(
        0x9,
        (
            "#1403F《黒月》のツァオは\x01",
            "相当頭の切れる男だ。\x02\x03",

            "恐らく、短絡的な報復には\x01",
            "踏み切らないだろうが……\x02\x03",

            "#1401F……まあいい。\x01",
            "今はただ備えておくだけだ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F05")

    Jump("loc_3188")

    label("loc_2F0A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_3188")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3115")
    SetChrName("")

    #A0158
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "アリオスが旧式の\x01",
            "国際通信器で通話している。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0159
    ChrTalk(
        0x9,
        (
            "#1404F#5P……大公閣下。\x01",
            "ご無沙汰しています。\x02\x03",

            "ええ、ええ……\x02\x03",

            "…………………………………\x02\x03",

            "#1405F……なるほど。\x01",
            "それは少々やっかいですね。\x02\x03",

            "#1404F──承知しました。\x01",
            "急ぎの仕事を片付け次第、\x01",
            "そちらへ伺います。\x02",
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
    Sleep(1200)

    #C0160
    ChrTalk(
        0x101,
        (
            "#0012F（な、なんか凄い人と\x01",
            "  話しているみたいだけど……）\x02",
        )
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0x102,
        (
            "#0105F（大公ということは……\x01",
            "  まさかレミフェリア公国の？）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3188")

    label("loc_3115")


    #C0162
    ChrTalk(
        0x9,
        (
            "#1402F#5Pええ、夕方には\x01",
            "そちらに伺えると思います。\x02\x03",

            "#1404F……とんでもない。\x01",
            "わざわざ相談して頂いて光栄です。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3188")

    TalkEnd(0xFE)
    Return()

    # Function_5_2C01 end

    def Function_6_318C(): pass

    label("Function_6_318C")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3220")
    Jump("loc_326A")

    label("loc_3220")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3240")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_326A")

    label("loc_3240")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3260")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_326A")

    label("loc_3260")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_326A")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_END)), "loc_3739")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCF, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_366A")

    #C0163
    ChrTalk(
        0xFE,
        (
            "#1403Fお前たちか。\x02\x03",

            "#1400F何でも《黒月》の\x01",
            "ツァオに会ってきたらしいな？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(500)

    #C0164
    ChrTalk(
        0x101,
        "#0011Fええっ！？\x02",
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0x102,
        "#0105Fどうしてそれを……\x02",
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0xFE,
        (
            "#1404Fフ……そうした噂は\x01",
            "こちらにもすぐに届く。\x02\x03",

            "#1400Fどうやら《黒月》の方は\x01",
            "すぐに報復をするつもりは\x01",
            "無さそうだな？\x02",
        )
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0x101,
        "#0001Fは、はい……\x02",
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0x104,
        (
            "#0301Fま、一触即発なのは\x01",
            "変わっちゃいないッスけどね。\x02",
        )
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0x103,
        (
            "#0206F彼らの本体が介入する\x01",
            "可能性もありそうですし……\x02",
        )
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0xFE,
        (
            "#1403F確かに《黒月》本体は\x01",
            "カルバードの裏社会を支配する\x01",
            "巨大な犯罪組織だ。\x02\x03",

            "#1400Fだが、幾つもの勢力に分かれ、\x01",
            "決して一枚岩とは言えない状況だ。\x02\x03",

            "あのツァオならば\x01",
            "何とか介入は食い止めるだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0x101,
        "#0005Fなるほど……\x02",
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0x102,
        (
            "#0100Fそれにしても……\x01",
            "随分、お詳しいんですね？\x02",
        )
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0xFE,
        (
            "#1404F仕事柄、共和国の方に\x01",
            "出張する事も多いのでな。\x02\x03",

            "例の《銀》についても\x01",
            "危険ではあるが、無用な殺戮を\x01",
            "好むタイプではなさそうだ。\x02\x03",

            "#1401F……むしろ危険なのは\x01",
            "ルバーチェの方かもしれんな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xCF, 4)
    Jump("loc_3734")

    label("loc_366A")


    #C0174
    ChrTalk(
        0xFE,
        (
            "#1403Fルバーチェは狡猾な組織だ。\x01",
            "今回のような短絡的な襲撃を\x01",
            "引き起こすのは珍しい。\x02\x03",

            "どうやら若頭のガルシアの\x01",
            "統制が弱まっているようだが……\x02\x03",

            "#1401F……ふむ、水面下で\x01",
            "何かが起こりつつあるようだな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3734")

    Jump("loc_3BE5")

    label("loc_3739")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_39B5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x92, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_38CB")

    #C0175
    ChrTalk(
        0xFE,
        (
            "#1400Fお前たちか……\x02\x03",

            "#1404Fフ……一月ぶりくらいか。\x01",
            "少しは成長したようだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0x101,
        (
            "#0002Fはは、アリオスさん\x01",
            "ご無沙汰しています。\x02",
        )
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0x104,
        (
            "#0300Fまあ《風の剣聖》に較べりゃ\x01",
            "微々たる成長ッスけどね。\x02",
        )
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0xFE,
        (
            "#1404F恥じる事はない。\x01",
            "お前たちはお前たちの道を\x01",
            "進んでいけばいい。\x02\x03",

            "#1402F今のクロスベルの姿を\x01",
            "よく見ておくことだ。\x01",
            "……いつか役立つ時が来るだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0x101,
        "#0011Fは、はあ……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x92, 4)
    Jump("loc_39B0")

    label("loc_38CB")


    #C0180
    ChrTalk(
        0xFE,
        (
            "#1404F仕事中のようだな。\x01",
            "……精進するがいい。\x02\x03",

            "#1402Fお前たちが\x01",
            "どこまで成長できるか……\x01",
            "楽しみにしているぞ。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_39AD")

    #C0181
    ChrTalk(
        0x101,
        "#0012F（アリオスさん……冗談かな。）\x02",
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0x102,
        (
            "#0106F（楽しみなんて、\x01",
            "  さすがに過大評価よねぇ……）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_39AD")

    SetScenarioFlags(0x0, 1)

    label("loc_39B0")

    Jump("loc_3BE5")

    label("loc_39B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_3BE5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6D, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B4C")

    #C0183
    ChrTalk(
        0xFE,
        "#1405Fほう、お前たちか。\x02",
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0x101,
        "#0011Fアリオスさん……\x02",
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0x102,
        "#0103Fその、ご無沙汰しています。\x02",
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0xFE,
        (
            "#1404Fフ……\x01",
            "そう緊張する事はない。\x02\x03",

            "#1402F旧市街の件については\x01",
            "ご苦労だった。\x02\x03",

            "こちらが介入する前に\x01",
            "解決してくれて助かったぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0x101,
        "#0012Fいや、そんな……\x02",
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0x104,
        (
            "#0306F（ま、このオッサンが出てきたら\x01",
            "  一発で解決しただろうけどな……）\x02",
        )
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0x103,
        "#0211F（やはり掌の上にいる感じですね。）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x6D, 3)
    Jump("loc_3BE5")

    label("loc_3B4C")


    #C0190
    ChrTalk(
        0xFE,
        (
            "#1404Fさてと……\x01",
            "そろそろ行くとするか。\x02\x03",

            "#1402Fフフ、彼らが来てくれたお陰で\x01",
            "少々時間に余裕が出来たな……\x02",
        )
    )

    CloseMessageWindow()

    #C0191
    ChrTalk(
        0x101,
        (
            "#0005F……？\x01",
            "（誰のことなんだろう？）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3BE5")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_6_318C end

    def Function_7_3BED(): pass

    label("Function_7_3BED")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_3C6F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6D, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3C0B")
    Call(0, 17)
    Jump("loc_3C6F")

    label("loc_3C0B")


    #C0192
    ChrTalk(
        0xB,
        (
            "#0800Fロイド君たちも\x01",
            "これから仕事みたいね。\x02\x03",

            "#0809Fえへへ……またどこかで\x01",
            "会ったらよろしくね！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3C6F")

    TalkEnd(0xFE)
    Return()

    # Function_7_3BED end

    def Function_8_3C73(): pass

    label("Function_8_3C73")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3D07")
    Jump("loc_3D51")

    label("loc_3D07")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3D27")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3D51")

    label("loc_3D27")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3D47")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3D51")

    label("loc_3D47")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3D51")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_3E4D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCF, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D91")
    Call(0, 18)
    Jump("loc_3E48")

    label("loc_3D91")


    #C0193
    ChrTalk(
        0xC,
        (
            "#0806Fあたしたちもマフィアに\x01",
            "直接問い質したいんだけど……\x02\x03",

            "こういう時は警察が優先って\x01",
            "取り決めがあるみたいなのよね～。\x02\x03",

            "#0800Fだからロイド君たち！\x01",
            "代わりに頑張って調べてきてね！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3E48")

    Jump("loc_404A")

    label("loc_3E4D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_404A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F9E")

    #C0194
    ChrTalk(
        0x153,
        (
            "#1106Fエステルー、さっきはゴメンね。\x02\x03",

            "#1108Fキーア、エステルのこと\x01",
            "キライじゃないけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0xC,
        (
            "#0809Fあはは、大丈夫。\x01",
            "全然気にしてないから。\x02\x03",

            "#0802Fでもま、困った事があったら\x01",
            "お姉さんにも相談して欲しいかな。\x02\x03",

            "きっと力に\x01",
            "なれることもあると思うし。\x02",
        )
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0x153,
        "#1109Fうんっ！\x02",
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0x101,
        "#0002Fああ、その時はよろしくな。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_404A")

    label("loc_3F9E")


    #C0198
    ChrTalk(
        0xC,
        (
            "#0806F……は～、ここのところ\x01",
            "立て続けにフラれちゃってるなぁ。\x02\x03",

            "#0808F記念祭に来てたキリカさんとは\x01",
            "結局、会えずじまいだったし……\x02\x03",

            "#0805Fでも……何しに来てたのかしら？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_404A")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_8_3C73 end

    def Function_9_4052(): pass

    label("Function_9_4052")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_417E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6D, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4070")
    Call(0, 17)
    Jump("loc_417E")

    label("loc_4070")


    #C0199
    ChrTalk(
        0xD,
        (
            "#0900F今日は依頼をこなしながら\x01",
            "アルモリカ方面を\x01",
            "歩いてみる予定なんだ。\x02\x03",

            "#0904F僕もエステルも\x01",
            "クロスベル市の周辺は\x01",
            "まだまだ不慣れだからね。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_417B")

    #C0200
    ChrTalk(
        0x101,
        (
            "#0003Fそうか……\x02\x03",

            "#0000F君たちなら問題ないと思うけど\x01",
            "魔獣には気をつけてくれ。\x02",
        )
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0xD,
        "#0902Fうん、ありがとう。\x02",
    )

    CloseMessageWindow()

    label("loc_417B")

    SetScenarioFlags(0x0, 3)

    label("loc_417E")

    TalkEnd(0xFE)
    Return()

    # Function_9_4052 end

    def Function_10_4182(): pass

    label("Function_10_4182")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4216")
    Jump("loc_4260")

    label("loc_4216")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4236")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4260")

    label("loc_4236")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4256")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4260")

    label("loc_4256")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4260")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_4360")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCF, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_42A0")
    Call(0, 18)
    Jump("loc_435B")

    label("loc_42A0")


    #C0202
    ChrTalk(
        0xE,
        (
            "#0901Fクロスベルの事情は大体、\x01",
            "分かっていたつもりだったけど……\x02\x03",

            "こういう事件が起きた時は\x01",
            "確かに大きな“壁”を感じるね。\x02\x03",

            "#0903F何とか正確な状況だけでも\x01",
            "把握できるといいんだけど……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_435B")

    Jump("loc_45ED")

    label("loc_4360")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_453F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_44C4")

    #C0203
    ChrTalk(
        0xE,
        (
            "#0905Fえ……大聖堂は\x01",
            "空振りだったのかい？\x02",
        )
    )

    CloseMessageWindow()

    #C0204
    ChrTalk(
        0x101,
        "#0006Fああ、実は……\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    #A0205
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "大聖堂のシスターにキーアを\x01",
            "診てもらった時のことを話した。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0206
    ChrTalk(
        0xE,
        (
            "#0903Fそうか……\x02\x03",

            "#0900F確かにそういう事情なら\x01",
            "ウルスラ病院を\x01",
            "頼るしかなさそうだね。\x02\x03",

            "あそこには最先端の医療、\x01",
            "『神経科』があると聞くから。\x02",
        )
    )

    CloseMessageWindow()

    #C0207
    ChrTalk(
        0x101,
        (
            "#0002Fああ。\x01",
            "これから訪ねてみるよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_453A")

    label("loc_44C4")


    #C0208
    ChrTalk(
        0xE,
        (
            "#0903F現状ではウルスラ病院を\x01",
            "頼るしかなさそうだね。\x02\x03",

            "#0900Fあそこには最先端の医療、\x01",
            "『神経科』があると聞くから。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_453A")

    Jump("loc_45ED")

    label("loc_453F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_45ED")

    #C0209
    ChrTalk(
        0xE,
        (
            "#0904F七耀教会は昔から\x01",
            "心身を癒す技を伝えているんだ。\x02\x03",

            "#0900Fキーアちゃんの記憶を\x01",
            "取り戻す手がかりに\x01",
            "なるんじゃないかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0210
    ChrTalk(
        0x101,
        "#0000Fああ、一度相談してみるよ。\x02",
    )

    CloseMessageWindow()

    label("loc_45ED")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_10_4182 end

    def Function_11_45F5(): pass

    label("Function_11_45F5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_478E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4724")

    #C0211
    ChrTalk(
        0xFE,
        (
            "パールは今も\x01",
            "百貨店の受付で\x01",
            "頑張ってるだろうな……\x02",
        )
    )

    CloseMessageWindow()

    #C0212
    ChrTalk(
        0x102,
        "#0102Fお付き合いされている方ですか？\x02",
    )

    CloseMessageWindow()

    #C0213
    ChrTalk(
        0xFE,
        (
            "ああ、実は婚約していてね。\x01",
            "忙しくて会う時間を\x01",
            "なかなか作れないけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0214
    ChrTalk(
        0xFE,
        (
            "……おっと、俺としたことが。\x01",
            "公私混同は素人のやることだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0215
    ChrTalk(
        0xFE,
        "気を引き締めて仕事しないとな。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4789")

    label("loc_4724")


    #C0216
    ChrTalk(
        0xFE,
        (
            "公私はしっかり分けないと、\x01",
            "どっちもおろそかになってしまう。\x02",
        )
    )

    CloseMessageWindow()

    #C0217
    ChrTalk(
        0xFE,
        "気を引き締めて仕事しないとな。\x02",
    )

    CloseMessageWindow()

    label("loc_4789")

    Jump("loc_481D")

    label("loc_478E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_479C")
    Jump("loc_481D")

    label("loc_479C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_481D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_47B7")
    Call(0, 19)
    Jump("loc_481D")

    label("loc_47B7")


    #C0218
    ChrTalk(
        0xFE,
        (
            "今朝からアルモリカ村の方で\x01",
            "２、３件頼まれているんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0219
    ChrTalk(
        0xFE,
        (
            "さてと……\x01",
            "今日も忙しくなりそうだな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_481D")

    TalkEnd(0xFE)
    Return()

    # Function_11_45F5 end

    def Function_12_4821(): pass

    label("Function_12_4821")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_48B5")
    Jump("loc_48FF")

    label("loc_48B5")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_48D5")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_48FF")

    label("loc_48D5")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_48F5")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_48FF")

    label("loc_48F5")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_48FF")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_49D5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCF, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_493F")
    Call(0, 18)
    Jump("loc_49D0")

    label("loc_493F")


    #C0220
    ChrTalk(
        0xFE,
        (
            "とりあえず、マフィアの周辺を\x01",
            "調べたいところだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0xFE,
        (
            "重火器の入手経路に\x01",
            "不気味に広いコネクション……\x01",
            "キナくさい事はいくらでもありそうだ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_49D0")

    Jump("loc_4CBE")

    label("loc_49D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_4CBE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4BFA")
    SetChrSubChip(0x11, 0x0)

    #C0222
    ChrTalk(
        0x10,
        (
            "君たち、２年ほど前に起こった\x01",
            "帝国ギルド連続襲撃事件を知ってるか？\x02",
        )
    )

    CloseMessageWindow()

    #C0223
    ChrTalk(
        0x10,
        (
            "当時、帝国にいたヴェンツェルは、\x01",
            "あの事件の解決に貢献したんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0224
    ChrTalk(
        0x102,
        (
            "#0108Fあの事件……\x01",
            "一時期大騒ぎになっていましたね。\x02\x03",

            "#0103F猟兵団による連続テロで\x01",
            "帝国のギルドは半壊状態だったとか。\x02",
        )
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0x101,
        (
            "#0000Fそんな大事件の解決に\x01",
            "貢献したなんて……流石ですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0x11,
        "……何、俺は大した事はしていない。\x02",
    )

    CloseMessageWindow()

    #C0227
    ChrTalk(
        0x11,
        (
            "解決の要因は、\x01",
            "助っ人に来ていた高位の遊撃士の\x01",
            "完璧な知略によるものだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0228
    ChrTalk(
        0x11,
        (
            "俺は作戦のコマとして、たまたま目立つ場所で\x01",
            "働いていたというだけの話さ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4CBE")

    label("loc_4BFA")

    SetChrSubChip(0x10, 0x0)

    #C0229
    ChrTalk(
        0x11,
        (
            "俺のことよりスコット……\x01",
            "最近、婚約者とは会えているのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0230
    ChrTalk(
        0x10,
        (
            "……いや、全然だ。\x01",
            "この忙しさじゃ仕方ないさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0x10,
        (
            "結婚も当分先の話だろうし……\x01",
            "いつか手が空いたら\x01",
            "埋め合わせをしないとな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4CBE")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_12_4821 end

    def Function_13_4CC6(): pass

    label("Function_13_4CC6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_4E94")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4E0A")
    OP_4B(0x11, 0xFF)
    OP_4B(0x13, 0xFF)

    #C0232
    ChrTalk(
        0x11,
        (
            "エオリア、万が一ことが起こったら\x01",
            "君はまず怪我人たちの保護に\x01",
            "尽力してくれ。\x02",
        )
    )

    CloseMessageWindow()

    #C0233
    ChrTalk(
        0x13,
        (
            "ええ、自分の役割は\x01",
            "理解しているつもりよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0234
    ChrTalk(
        0x13,
        (
            "……でも、なんとか穏便に\x01",
            "事態を収拾する方法を\x01",
            "探したいところね。\x02",
        )
    )

    CloseMessageWindow()

    #C0235
    ChrTalk(
        0x11,
        "もちろんだ。\x02",
    )

    CloseMessageWindow()

    #C0236
    ChrTalk(
        0x11,
        (
            "そのためにも……\x01",
            "今後の情報収集が重要になるな。\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x11, 0xFF)
    OP_4C(0x13, 0xFF)
    ClearChrFlags(0x11, 0x10)
    ClearChrFlags(0x13, 0x10)
    SetScenarioFlags(0x0, 5)
    Jump("loc_4E8F")

    label("loc_4E0A")


    #C0237
    ChrTalk(
        0xFE,
        (
            "マフィアの抗争などという\x01",
            "下らないことのために、\x01",
            "市民を傷つけさせはしない。\x02",
        )
    )

    CloseMessageWindow()

    #C0238
    ChrTalk(
        0xFE,
        (
            "そのためにも……\x01",
            "確実に情報を集めていかねばな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4E8F")

    Jump("loc_526C")

    label("loc_4E94")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_4FF8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4F90")

    #C0239
    ChrTalk(
        0xFE,
        (
            "今朝から捜査一課の連中が\x01",
            "うろついているようだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0240
    ChrTalk(
        0xFE,
        (
            "……連中は好きになれん。\x01",
            "帝国軍のＭＰを思い出すんでな。\x02",
        )
    )

    CloseMessageWindow()

    #C0241
    ChrTalk(
        0x101,
        (
            "#0005F（ＭＰ……憲兵のことか。）\x02\x03",

            "#0003F（帝国軍は秘密主義らしいし……\x01",
            "  確かに体質は似ているかもな。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_4FF3")

    label("loc_4F90")


    #C0242
    ChrTalk(
        0xFE,
        (
            "帝国軍には\x01",
            "苦い思い出がある……\x02",
        )
    )

    CloseMessageWindow()

    #C0243
    ChrTalk(
        0xFE,
        (
            "同じように\x01",
            "コソコソとしている捜査一課は\x01",
            "好きになれんな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4FF3")

    Jump("loc_526C")

    label("loc_4FF8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_51D1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5013")
    Call(0, 12)
    Jump("loc_51CC")

    label("loc_5013")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_50A7")
    Jump("loc_50F1")

    label("loc_50A7")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_50C7")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_50F1")

    label("loc_50C7")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_50E7")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_50F1")

    label("loc_50E7")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_50F1")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0244
    ChrTalk(
        0x11,
        (
            "……あの事件以来、\x01",
            "帝国ギルドは政府からの圧力で\x01",
            "衰退を始めてしまった。\x02",
        )
    )

    CloseMessageWindow()

    #C0245
    ChrTalk(
        0x11,
        (
            "俺は運良くクロスベルの支部に\x01",
            "引き抜かれたが……\x02",
        )
    )

    CloseMessageWindow()

    #C0246
    ChrTalk(
        0x11,
        (
            "……いや、よそう。\x01",
            "無駄話をしてしまったな。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)

    label("loc_51CC")

    Jump("loc_526C")

    label("loc_51D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_526C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_51EC")
    Call(0, 19)
    Jump("loc_526C")

    label("loc_51EC")


    #C0247
    ChrTalk(
        0xFE,
        (
            "今度、このクロスベルのギルドに\x01",
            "有望な新人が来ることになっている。\x02",
        )
    )

    CloseMessageWindow()

    #C0248
    ChrTalk(
        0xFE,
        (
            "せいぜい、その存在を\x01",
            "忘れられぬようにすることだな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_526C")

    TalkEnd(0xFE)
    Return()

    # Function_13_4CC6 end

    def Function_14_5270(): pass

    label("Function_14_5270")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5304")
    Jump("loc_534E")

    label("loc_5304")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5324")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_534E")

    label("loc_5324")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5344")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_534E")

    label("loc_5344")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_534E")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_558C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCF, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_538E")
    Call(0, 18)
    Jump("loc_5587")

    label("loc_538E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_54EB")

    #C0249
    ChrTalk(
        0xFE,
        (
            "《風の剣聖》アリオスさんに、\x01",
            "リベールの英雄エステルとヨシュア。\x02",
        )
    )

    CloseMessageWindow()

    #C0250
    ChrTalk(
        0xFE,
        (
            "ライフルの名手スコットと\x01",
            "帝国ギルドの猛者ヴェンツェル。\x02",
        )
    )

    CloseMessageWindow()

    #C0251
    ChrTalk(
        0xFE,
        (
            "医師でもあるエオリア、\x01",
            "そして《泰斗流》の使い手である私。\x02",
        )
    )

    CloseMessageWindow()

    #C0252
    ChrTalk(
        0xFE,
        (
            "これだけのメンツが揃う遊撃士でも、\x01",
            "クロスベル内の事件の対処には\x01",
            "慎重にならざるを得ない。\x02",
        )
    )

    CloseMessageWindow()

    #C0253
    ChrTalk(
        0xFE,
        "そっちもとにかく、慎重に動いてくれよ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_5587")

    label("loc_54EB")


    #C0254
    ChrTalk(
        0xFE,
        (
            "《風の剣聖》アリオスさんを筆頭に\x01",
            "これだけのメンツが揃う遊撃士でも、\x01",
            "事件の対処には慎重にならざるを得ない。\x02",
        )
    )

    CloseMessageWindow()

    #C0255
    ChrTalk(
        0xFE,
        "そっちもとにかく、慎重に動いてくれよ。\x02",
    )

    CloseMessageWindow()

    label("loc_5587")

    Jump("loc_59C8")

    label("loc_558C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_592F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_572E")

    #C0256
    ChrTalk(
        0xFE,
        (
            "よう、警察のルーキー君たち。\x01",
            "調子はどうだい？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x50, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_561A")

    #C0257
    ChrTalk(
        0x101,
        (
            "#0000F（この人は……\x01",
            "  遊撃士のリンさんだったな。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5636")

    label("loc_561A")


    #C0258
    ChrTalk(
        0x101,
        "#0000Fはは、どうも……\x02",
    )

    CloseMessageWindow()

    label("loc_5636")


    #C0259
    ChrTalk(
        0x102,
        (
            "#0100F珍しいですね、\x01",
            "今日は出張無しですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0260
    ChrTalk(
        0xFE,
        (
            "うんうん、その通り。\x01",
            "昨日戻ったばかりなんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0261
    ChrTalk(
        0xFE,
        (
            "ミシェルに頼んで\x01",
            "出張はやめて～って言っておいたから、\x01",
            "しばらくは大丈夫だと思うんだけどね。\x02",
        )
    )

    CloseMessageWindow()

    #C0262
    ChrTalk(
        0x104,
        "#0300Fはは、遊撃士ってのも大変だねぇ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_592A")

    label("loc_572E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_58AC")

    #C0263
    ChrTalk(
        0xFE,
        (
            "悪いね、ティオちゃん。\x01",
            "またエオリアが絡んじゃって。\x02",
        )
    )

    CloseMessageWindow()

    #C0264
    ChrTalk(
        0x103,
        (
            "#0206Fはあ、わたしは別に……\x01",
            "というか理由が\x01",
            "判らないのですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0265
    ChrTalk(
        0xFE,
        (
            "エオリアの趣向は\x01",
            "私にもよく判らないのだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0266
    ChrTalk(
        0xFE,
        (
            "ま、諦めておもちゃにでも\x01",
            "なってやってくれ。\x02",
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
    Sleep(1200)

    #C0267
    ChrTalk(
        0x101,
        "#0003F（リンさん、サッパリしすぎだ……）\x02",
    )

    CloseMessageWindow()
    Jump("loc_592A")

    label("loc_58AC")


    #C0268
    ChrTalk(
        0xFE,
        (
            "エオリアには特殊な技能があってね。\x01",
            "あちこち引っ張りだこなんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0269
    ChrTalk(
        0xFE,
        (
            "お陰で出張ばかりでね、\x01",
            "この子と組むと苦労するよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_592A")

    Jump("loc_59C8")

    label("loc_592F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_59C8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x50, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_594A")
    Call(0, 20)
    Jump("loc_59C8")

    label("loc_594A")


    #C0270
    ChrTalk(
        0xFE,
        (
            "ま、ちょっと言い過ぎたかもだけど……\x01",
            "そっちも遊びじゃないんだろう？\x02",
        )
    )

    CloseMessageWindow()

    #C0271
    ChrTalk(
        0xFE,
        (
            "だったらヘコまず\x01",
            "これから挽回していかなきゃね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_59C8")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_14_5270 end

    def Function_15_59D0(): pass

    label("Function_15_59D0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_5A78")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_59EE")
    Call(0, 13)
    Jump("loc_5A73")

    label("loc_59EE")


    #C0272
    ChrTalk(
        0xFE,
        (
            "私は医者として\x01",
            "動くことができるけど……\x01",
            "できるならそうしたくはないものね。\x02",
        )
    )

    CloseMessageWindow()

    #C0273
    ChrTalk(
        0xFE,
        (
            "怪我人を出さない方法を\x01",
            "なんとか模索しましょう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5A73")

    Jump("loc_5DEA")

    label("loc_5A78")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_5D40")
    TurnDirection(0x13, 0x103, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5C96")

    #C0274
    ChrTalk(
        0xFE,
        (
            "あら……\x01",
            "ティオちゃんじゃない。\x02",
        )
    )

    CloseMessageWindow()

    #C0275
    ChrTalk(
        0xFE,
        (
            "うーん、相変わらず\x01",
            "可愛い可愛い……っ！\x02",
        )
    )

    CloseMessageWindow()

    #C0276
    ChrTalk(
        0xFE,
        (
            "お願い、お姉さんに\x01",
            "抱っこさせて～！\x02",
        )
    )

    CloseMessageWindow()

    #C0277
    ChrTalk(
        0x103,
        "#0211Fあのう……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x50, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5B94")

    #C0278
    ChrTalk(
        0x101,
        (
            "#0000F（エオリアさんって\x01",
            "  何度か話したことがあるけど……\x01",
            "  ティオに会わせると壊れるよな。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5BD5")

    label("loc_5B94")


    #C0279
    ChrTalk(
        0x101,
        (
            "#0000F（エオリアさん……\x01",
            "  ティオに会わせると壊れるよな。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5BD5")


    #C0280
    ChrTalk(
        0x104,
        (
            "#0303F（超美人な異国のお姉さん……\x01",
            "  俺的にはドストライクなんだが……）\x02\x03",

            "#0301F（ティオすけに\x01",
            "  惚れてるんじゃ仕方ねえ。\x01",
            "  譲ってやるぜ……！）\x02",
        )
    )

    CloseMessageWindow()

    #C0281
    ChrTalk(
        0x103,
        "#0206F（……一体どうしろと。）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_5D3B")

    label("loc_5C96")


    #C0282
    ChrTalk(
        0xFE,
        (
            "ティオちゃん、おいで～！\x01",
            "抱っこしてあげる～っ！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x13, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Sleep(1200)

    #C0283
    ChrTalk(
        0x101,
        (
            "#0000F（ティオにラブコールを\x01",
            "  送っている……）\x02",
        )
    )

    CloseMessageWindow()

    #C0284
    ChrTalk(
        0x103,
        "#0206F（……どうしろと。）\x02",
    )

    CloseMessageWindow()

    label("loc_5D3B")

    Jump("loc_5DEA")

    label("loc_5D40")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_5DEA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x50, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5D5B")
    Call(0, 20)
    Jump("loc_5DEA")

    label("loc_5D5B")


    #C0285
    ChrTalk(
        0xFE,
        (
            "うふふ、今日は出張帰りだから\x01",
            "ここまでにしとくわね。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x103, 500)

    #C0286
    ChrTalk(
        0xFE,
        (
            "ティオちゃん、\x01",
            "今度、抱っこさせてね㈱\x02",
        )
    )

    CloseMessageWindow()

    #C0287
    ChrTalk(
        0x103,
        "#0211F（……危険人物と認識。）\x02",
    )

    CloseMessageWindow()

    label("loc_5DEA")

    TalkEnd(0xFE)
    Return()

    # Function_15_59D0 end

    def Function_16_5DEE(): pass

    label("Function_16_5DEE")

    TalkBegin(0xFF)
    SetChrName("")

    #A0288
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "遊撃士たちのシフト表が貼り付けられている。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_5F6D")
    SetChrName("")

    #A0289
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            "　　　　　　　　　  行き先　　　\x01",
            "━━━━━━━━━━━━━━━━\x01",
            " 　アリオス　：  マインツ方面\x01",
            " 　スコット　： ベルガード方面\x01",
            " ヴェンツェル： ベルガード方面\x01",
            " 　　リン　　： タングラム方面\x01",
            " 　エオリア　： タングラム方面\x01",
            " 　エステル　： アルモリカ方面\x01",
            " 　ヨシュア　： アルモリカ方面\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_6D54")

    label("loc_5F6D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_6097")
    SetChrName("")

    #A0290
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            "　　　　　　　　　  行き先　　　\x01",
            "━━━━━━━━━━━━━━━━\x01",
            " 　アリオス　：　  市内巡回\x01",
            " 　スコット　：  ベルガード門\x01",
            " ヴェンツェル：  ベルガード門\x01",
            " 　　リン　　：　 　旧市街\x01",
            " 　エオリア　：　 　旧市街\x01",
            " 　エステル　： ※私用（東通り）\x01",
            " 　ヨシュア　： ※私用（東通り）\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_6D54")

    label("loc_6097")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_61C1")
    SetChrName("")

    #A0291
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            "　　　　　　　　　  行き先　　　\x01",
            "━━━━━━━━━━━━━━━━\x01",
            " 　アリオス　：　  市内巡回\x01",
            " 　スコット　：  ベルガード門\x01",
            " ヴェンツェル：  ベルガード門\x01",
            " 　　リン　　：　 　旧市街\x01",
            " 　エオリア　：　 　旧市街\x01",
            " 　エステル　： ※私用（歓楽街）\x01",
            " 　ヨシュア　： ※私用（歓楽街）\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_6D54")

    label("loc_61C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_END)), "loc_62EC")
    SetChrName("")

    #A0292
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            "　　　　　　　　　  行き先　　　\x01",
            "━━━━━━━━━━━━━━━━\x01",
            " 　アリオス　：　 《待機中》　　\x01",
            " 　スコット　：　　 裏通り\x01",
            " ヴェンツェル：　　 裏通り\x01",
            " 　　リン　　：　クロスベル駅\x01",
            " 　エオリア　：　クロスベル駅\x01",
            " 　エステル　： ※休憩（自宅）\x01",
            " 　ヨシュア　： ※休憩（自宅）\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_6D54")

    label("loc_62EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_642D")
    SetChrName("")

    #A0293
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            "　　　　　　　　　  行き先　　　\x01",
            "━━━━━━━━━━━━━━━━\x01",
            " 　アリオス　：　 《待機中》　　\x01",
            " 　スコット　：　 《待機中》　　\x01",
            " ヴェンツェル：　 《待機中》　　\x01",
            " 　　リン　　：　 《待機中》　　\x01",
            " 　エオリア　：　 《待機中》　　\x01",
            " 　エステル　：　 《待機中》　　\x01",
            " 　ヨシュア　：　 《待機中》　　\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_6D54")

    label("loc_642D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_6554")
    SetChrName("")

    #A0294
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            "　　　　　　　　　  行き先　　　\x01",
            "━━━━━━━━━━━━━━━━\x01",
            " 　アリオス　： エレボニア帝国\x01",
            " 　スコット　：　 　旧市街\x01",
            " ヴェンツェル：　 　旧市街\x01",
            " 　　リン　　：  ウルスラ病院\x01",
            " 　エオリア　：  ウルスラ病院\x01",
            " 　エステル　：　アルモリカ村\x01",
            " 　ヨシュア　：　アルモリカ村\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_6D54")

    label("loc_6554")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_667B")
    SetChrName("")

    #A0295
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            "　　　　　　　　　  行き先　　　\x01",
            "━━━━━━━━━━━━━━━━\x01",
            " 　アリオス　：    市外巡回\x01",
            " 　スコット　：　　 ※休暇\x01",
            " ヴェンツェル：　　市外巡回\x01",
            " 　　リン　　：レミフェリア公国\x01",
            " 　エオリア　：レミフェリア公国\x01",
            " 　エステル　：　 《待機中》\x01",
            " 　ヨシュア　：　 《待機中》\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_6D54")

    label("loc_667B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_67A3")
    SetChrName("")

    #A0296
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            "　　　　　　　　　  行き先　　　\x01",
            "━━━━━━━━━━━━━━━━\x01",
            " 　アリオス　：レミフェリア公国\x01",
            " 　スコット　：　 《待機中》\x01",
            " ヴェンツェル：　 《待機中》\x01",
            " 　　リン　　：  タングラム門\x01",
            " 　エオリア　：  タングラム門\x01",
            " 　エステル　：　  マインツ\x01",
            " 　ヨシュア　：　  マインツ\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_6D54")

    label("loc_67A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_68CA")
    SetChrName("")

    #A0297
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            "　　　　　　　　　  行き先　　　\x01",
            "━━━━━━━━━━━━━━━━\x01",
            " 　アリオス　：　 《待機中》\x01",
            " 　スコット　：　  マインツ\x01",
            " ヴェンツェル：　  マインツ\x01",
            " 　　リン　　：  ウルスラ病院\x01",
            " 　エオリア　：  ウルスラ病院\x01",
            " 　エステル　：  ベルガード門\x01",
            " 　ヨシュア　：  ベルガード門\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_6D54")

    label("loc_68CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_69F3")
    SetChrName("")

    #A0298
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            "　　　　　　　　　  行き先　　　\x01",
            "━━━━━━━━━━━━━━━━\x01",
            " 　アリオス　：　 《待機中》\x01",
            " 　スコット　：　  マインツ\x01",
            " ヴェンツェル：　  マインツ\x01",
            " 　　リン　　：  ウルスラ病院\x01",
            " 　エオリア　：  ウルスラ病院\x01",
            " 　エステル　： ※休憩（自宅）\x01",
            " 　ヨシュア　： ※休憩（自宅）\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_6D54")

    label("loc_69F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_6B28")
    SetChrName("")

    #A0299
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            "　　　　　　　　　  行き先　　 \x01",
            "━━━━━━━━━━━━━━━━\x01",
            " 　アリオス　：カルバード共和国\x01",
            " 　スコット　： エレボニア帝国\x01",
            " ヴェンツェル： エレボニア帝国\x01",
            " 　　リン　　：　  市外巡回　　\x01",
            " 　エオリア　：　  市外巡回　　\x01",
            " 　エステル　：　 《待機中》　\x01",
            " 　ヨシュア　：　 《待機中》　\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_6D54")

    label("loc_6B28")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_6B70")
    SetChrName("")

    #A0300
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            "シフト組み直し中……\x01",
            "ちょっと待ってちょうだい！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_6D54")

    label("loc_6B70")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_6C6D")
    SetChrName("")

    #A0301
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            "　　　　　　　　　  行き先　　\x01",
            "━━━━━━━━━━━━━━━━\x01",
            " 　アリオス　： エレボニア帝国　\x01",
            " 　スコット　：　　市外巡回　　 \x01",
            " ヴェンツェル：　　市外巡回　　 \x01",
            " 　　リン　　：　 《待機中》　　\x01",
            " 　エオリア　：　 《待機中》　　\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_6D54")

    label("loc_6C6D")

    SetChrName("")

    #A0302
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            "　　　　　　　　　  行き先　　\x01",
            "━━━━━━━━━━━━━━━━\x01",
            " 　アリオス　： エレボニア帝国\x01",
            " 　スコット　：　 《待機中》　\x01",
            " ヴェンツェル：　 《待機中》　\x01",
            " 　　リン　　：　　市外巡回　　\x01",
            " 　エオリア　：　　市外巡回　　\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_6D54")

    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    TalkEnd(0xFF)
    Return()

    # Function_16_5DEE end

    def Function_17_6D6B(): pass

    label("Function_17_6D6B")

    EventBegin(0x0)
    Fade(500)
    OP_4B(0x8, 0xFF)
    OP_4B(0xB, 0xFF)
    OP_4B(0xD, 0xFF)
    OP_68(810, 1300, 9650, 0)
    MoveCamera(45, 24, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(18820, 0)
    SetChrPos(0x101, 1520, 0, 8250, 0)
    SetChrPos(0x102, 340, 0, 8029, 0)
    SetChrPos(0x103, 1520, 0, 6890, 0)
    SetChrPos(0x104, 340, 0, 6640, 0)
    OP_93(0x8, 0xB4, 0x0)
    OP_93(0xB, 0x0, 0x0)
    OP_93(0xD, 0x0, 0x0)
    OP_0D()
    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xD, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_6E32():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_6E32)
    Sleep(50)

    def lambda_6E42():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_6E42)
    WaitChrThread(0xB, 1)
    WaitChrThread(0xD, 1)

    #C0303
    ChrTalk(
        0xB,
        (
            "#0805Fあっ、昨日の……\x02\x03",

            "#0809Fやっほー！\x01",
            "特務支援課のみんな～！\x02",
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
    Sleep(1200)

    #C0304
    ChrTalk(
        0x101,
        (
            "#0012Fや、やあ。\x01",
            "エステルにヨシュア。\x02",
        )
    )

    CloseMessageWindow()

    #C0305
    ChrTalk(
        0x103,
        "#0204F昨日はどうもでした。\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0306
    ChrTalk(
        0x8,
        (
            "ハァ……\x01",
            "あのねえ、エステルちゃん。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_6FA3():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_6FA3)
    Sleep(100)

    def lambda_6FB3():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_6FB3)
    WaitChrThread(0xB, 1)
    WaitChrThread(0xD, 1)

    #C0307
    ChrTalk(
        0xB,
        "#0805Fん？　なにミシェルさん。\x02",
    )

    CloseMessageWindow()

    #C0308
    ChrTalk(
        0x8,
        "………………………………\x02",
    )

    CloseMessageWindow()

    #C0309
    ChrTalk(
        0x8,
        (
            "ふぅ、やっぱりいいわ。\x01",
            "打ち合わせを続けましょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0310
    ChrTalk(
        0xB,
        "#0800F？？？\x02",
    )

    CloseMessageWindow()
    OP_93(0xD, 0xB4, 0x1F4)

    #C0311
    ChrTalk(
        0xD,
        (
            "#0906Fまあ、ご覧のとおり、\x01",
            "こういう子だから……\x02\x03",

            "#0900F色々なしがらみは抜きにして\x01",
            "普通に付き合えると嬉しいな。\x02",
        )
    )

    CloseMessageWindow()

    #C0312
    ChrTalk(
        0x101,
        "#0002F……ああ、こちらこそ。\x02",
    )

    CloseMessageWindow()

    #C0313
    ChrTalk(
        0x102,
        "#0104Fよろしくお願いしますね。\x02",
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 1000, 0, 8250, 0)
    OP_93(0x8, 0xB4, 0x0)
    OP_93(0xB, 0x0, 0x0)
    OP_93(0xD, 0x0, 0x0)
    SetChrFlags(0x8, 0x10)
    OP_4C(0x8, 0xFF)
    OP_4C(0xB, 0xFF)
    OP_4C(0xD, 0xFF)
    SetScenarioFlags(0x6D, 2)
    EventEnd(0x5)
    Return()

    # Function_17_6D6B end

    def Function_18_714D(): pass

    label("Function_18_714D")

    EventBegin(0x0)
    Fade(500)
    OP_68(-5920, 1300, 48320, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(20500, 0)
    SetChrPos(0x101, -3550, 0, 48770, 270)
    SetChrPos(0x102, -3440, 0, 47510, 270)
    SetChrPos(0x103, -2420, 0, 48770, 270)
    SetChrPos(0x104, -2320, 0, 47490, 270)
    SetChrSubChip(0xC, 0x1)
    SetChrSubChip(0xE, 0x1)
    SetChrSubChip(0x10, 0x2)
    SetChrSubChip(0x12, 0x2)
    OP_0D()

    #C0314
    ChrTalk(
        0xC,
        (
            "#0801F#1Pあ、ロイド君たち！\x01",
            "もう《黒月》の話は聞いた！？\x02",
        )
    )

    CloseMessageWindow()

    #C0315
    ChrTalk(
        0x101,
        (
            "#0001F#11Pああ、今ちょうど\x01",
            "情報収集している最中さ。\x02",
        )
    )

    CloseMessageWindow()

    #C0316
    ChrTalk(
        0x102,
        (
            "#0105F#11Pそれにしても……\x01",
            "遊撃士全員が揃い踏みですか。\x02",
        )
    )

    CloseMessageWindow()

    #C0317
    ChrTalk(
        0x103,
        (
            "#0202F#11P《風の剣聖》も居ましたし\x01",
            "なかなか壮観ですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0318
    ChrTalk(
        0xE,
        (
            "#0904F#1Pはは……朝早くに\x01",
            "エニグマで連絡があってね。\x02",
        )
    )

    CloseMessageWindow()

    #C0319
    ChrTalk(
        0x10,
        (
            "#6Pそれで取り急ぎ\x01",
            "駆けつけたってわけだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0320
    ChrTalk(
        0x104,
        (
            "#0306F#11Pやれやれ、あんたら\x01",
            "フットワーク良過ぎだぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0321
    ChrTalk(
        0x12,
        (
            "#6Pうーん、そっちの方が\x01",
            "ノンビリしすぎなだけじゃない？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x12, 0x0)
    Sleep(200)

    #C0322
    ChrTalk(
        0x12,
        (
            "#12Pしかしルバーチェの連中……\x01",
            "とんでもない事しでかすよな！\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xC, 0x0)

    #C0323
    ChrTalk(
        0xC,
        (
            "#0803F#5Pうんうん！\x01",
            "夜人通りが少ない場所とはいえ、\x01",
            "市民だって通るかもしれないのに！\x02\x03",

            "#0801F許すまじ、マフィアどもね！\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, -3420, 0, 48200, 270)
    SetChrSubChip(0xC, 0x0)
    SetChrSubChip(0x12, 0x0)
    SetChrSubChip(0xE, 0x0)
    SetChrSubChip(0x10, 0x0)
    SetScenarioFlags(0xCF, 7)
    EventEnd(0x5)
    Return()

    # Function_18_714D end

    def Function_19_7496(): pass

    label("Function_19_7496")

    EventBegin(0x0)
    Fade(500)
    OP_4B(0xF, 0xFF)
    OP_4B(0x11, 0xFF)
    OP_68(-4610, 1000, 51100, 0)
    MoveCamera(0, 30, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(20950, 0)
    SetChrPos(0x101, -3630, 0, 50910, 315)
    SetChrPos(0x102, -4250, 0, 49980, 315)
    SetChrPos(0x103, -2650, 0, 50000, 315)
    SetChrPos(0x104, -3250, 0, 48910, 315)
    SetChrSubChip(0xF, 0x0)
    SetChrSubChip(0x11, 0x0)
    OP_93(0xF, 0x13B, 0x0)
    OP_93(0x11, 0x2D, 0x0)
    SetMapObjFrame(0xFF, "on_off", 0x0, 0x1)
    SetMapObjFrame(0xFF, "shadow_onoff", 0x0, 0x1)
    OP_0D()

    #C0324
    ChrTalk(
        0xF,
        (
            "#11Pアリオスさんは出張か……\x01",
            "相変わらず忙しそうにしてるな。\x02",
        )
    )

    CloseMessageWindow()

    #C0325
    ChrTalk(
        0xF,
        (
            "#11Pって、俺たちも人の事は言えないか。\x01",
            "これから出るところだし……\x02",
        )
    )

    CloseMessageWindow()

    #C0326
    ChrTalk(
        0x11,
        (
            "#5Pリンとエオリアは\x01",
            "そろそろ戻ってくる頃だろうがな。\x02",
        )
    )

    CloseMessageWindow()

    #C0327
    ChrTalk(
        0x11,
        "#5P流石、ミシェルのシフトには隙がない。\x02",
    )

    CloseMessageWindow()

    #C0328
    ChrTalk(
        0xF,
        "#11Pはは、ちょっと人使いは荒いけどな。\x02",
    )

    CloseMessageWindow()

    #C0329
    ChrTalk(
        0x101,
        (
            "#11P#0005Fえっと……\x01",
            "遊撃士の方ですか？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xF, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x11, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_76C4():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_76C4)

    def lambda_76D1():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_76D1)
    WaitChrThread(0xF, 1)
    WaitChrThread(0x11, 1)

    #C0330
    ChrTalk(
        0xF,
        "#5P君たちは……\x02",
    )

    CloseMessageWindow()

    #C0331
    ChrTalk(
        0xF,
        (
            "#5Pああ、もしかして\x01",
            "例の『特務支援課』か？\x02",
        )
    )

    CloseMessageWindow()

    #C0332
    ChrTalk(
        0x103,
        "#11P#0200Fその通りですが……\x02",
    )

    CloseMessageWindow()

    #C0333
    ChrTalk(
        0x104,
        "#12P#0304Fやっぱ分かっちまうかね。\x02",
    )

    CloseMessageWindow()

    #C0334
    ChrTalk(
        0x11,
        "#5P……新人くさい気配がするからな。\x02",
    )

    CloseMessageWindow()

    #C0335
    ChrTalk(
        0x11,
        (
            "#5P見るからに練度が足りないようだが……\x01",
            "本当にこのクロスベルでやっていけるのか？\x02",
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
    Sleep(1200)

    #C0336
    ChrTalk(
        0x102,
        (
            "#12P#0106F（うーん、悔しいけど……\x01",
            "  否定できないわね。）\x02",
        )
    )

    CloseMessageWindow()

    #C0337
    ChrTalk(
        0x101,
        (
            "#11P#0001Fとにかく……\x01",
            "やれるだけのことは\x01",
            "やるつもりです。\x02",
        )
    )

    CloseMessageWindow()

    #C0338
    ChrTalk(
        0x11,
        "#5P……甘い。\x02",
    )

    CloseMessageWindow()

    #C0339
    ChrTalk(
        0x11,
        (
            "#5Pやれる以上のことをやらねば\x01",
            "いつまでたっても成長しないぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0340
    ChrTalk(
        0x101,
        (
            "#11P#0003Fうっ……\x01",
            "（手厳しい……）\x02",
        )
    )

    CloseMessageWindow()

    #C0341
    ChrTalk(
        0xF,
        (
            "#5Pハハ、まあ頑張れ。\x01",
            "個人的には応援しているんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0342
    ChrTalk(
        0xF,
        (
            "#5P君たち警察が頑張ってくれれば\x01",
            "この忙しさも軽減するかもしれない……\x02",
        )
    )

    CloseMessageWindow()

    #C0343
    ChrTalk(
        0xF,
        (
            "#5P警察がしくじった案件は\x01",
            "ことごとくウチに回ってくるからな。\x02",
        )
    )

    CloseMessageWindow()

    #C0344
    ChrTalk(
        0x101,
        "#11P#0006Fぜ、善処します……\x02",
    )

    CloseMessageWindow()
    SetChrPos(0x0, -3630, 0, 50910, 315)
    SetMapObjFrame(0xFF, "on_off", 0x1, 0x1)
    SetMapObjFrame(0xFF, "shadow_onoff", 0x1, 0x1)
    OP_93(0xF, 0x0, 0x0)
    OP_93(0x11, 0x2D, 0x0)
    OP_4C(0xF, 0xFF)
    OP_4C(0x11, 0xFF)
    SetScenarioFlags(0x4F, 7)
    EventEnd(0x5)
    Return()

    # Function_19_7496 end

    def Function_20_7A84(): pass

    label("Function_20_7A84")

    EventBegin(0x0)
    Fade(500)
    OP_4B(0x13, 0xFF)
    OP_68(-4460, 1300, 41900, 0)
    MoveCamera(17, 23, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(20100, 0)
    SetChrPos(0x101, -3430, 0, 42620, 270)
    SetChrPos(0x103, -3440, 0, 41360, 270)
    SetChrPos(0x102, -2320, 0, 42620, 270)
    SetChrPos(0x104, -2320, 0, 41360, 270)
    TurnDirection(0x13, 0x103, 0)
    SetChrSubChip(0x12, 0x1)
    OP_0D()

    #C0345
    ChrTalk(
        0x12,
        "#5Pあれ、君たちは……\x02",
    )

    CloseMessageWindow()
    OP_63(0x13, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0346
    ChrTalk(
        0x13,
        "#5Pきゃっ……可愛い……！\x02",
    )

    CloseMessageWindow()

    #C0347
    ChrTalk(
        0x103,
        (
            "#11P#0205Fえ……\x01",
            "わ、わたしのことでしょうか。\x02",
        )
    )

    CloseMessageWindow()

    #C0348
    ChrTalk(
        0x13,
        "#5Pもちろん！\x02",
    )

    CloseMessageWindow()

    #C0349
    ChrTalk(
        0x13,
        (
            "#5Pひんやりした雰囲気で大人びてるのに\x01",
            "子供らしい大きな瞳と小さな唇が主張して……\x02",
        )
    )

    CloseMessageWindow()

    #C0350
    ChrTalk(
        0x13,
        "#5Pた、たまんな～い！！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x13, 0x12, 500)

    #C0351
    ChrTalk(
        0x13,
        (
            "#11Pどうこれ、リン！\x01",
            "持って帰ってもいいかしら！？\x02",
        )
    )

    CloseMessageWindow()

    #C0352
    ChrTalk(
        0x103,
        "#11P#0211F……………………\x02",
    )

    CloseMessageWindow()

    #C0353
    ChrTalk(
        0x12,
        (
            "#5P……エオリア、悪い癖だよ。\x01",
            "初対面の子を怖がらせちゃって。\x02",
        )
    )

    CloseMessageWindow()

    #C0354
    ChrTalk(
        0x12,
        (
            "#5P出張から帰ってきたばかりなんだから\x01",
            "程ほどにしときなさいって。\x02",
        )
    )

    CloseMessageWindow()

    #C0355
    ChrTalk(
        0x104,
        (
            "#11P#0302Fお姉さん、俺だったら\x01",
            "お持ち帰り自由ですよ。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x13, 0x104, 500)

    #C0356
    ChrTalk(
        0x13,
        "#5Pううん、遠慮するわ㈱\x02",
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
    Sleep(1200)

    #C0357
    ChrTalk(
        0x104,
        "#11P#0306F……即答ッスか。\x02",
    )

    CloseMessageWindow()

    #C0358
    ChrTalk(
        0x102,
        (
            "#11P#0106Fな、なんていうか……\x01",
            "おしとやかそうな見た目と\x01",
            "随分ギャップのある人ねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0359
    ChrTalk(
        0x101,
        (
            "#11P#0000Fもしかして、お２人は\x01",
            "こちらに所属する遊撃士の方ですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0360
    ChrTalk(
        0x13,
        (
            "#5Pそういうあなた達は\x01",
            "『特務支援課』かしら？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0361
    ChrTalk(
        0x101,
        "#11P#0005Fご存知でしたか。\x02",
    )

    CloseMessageWindow()

    #C0362
    ChrTalk(
        0x12,
        "#5Pミシェルさんが教えてくれたよ。\x02",
    )

    CloseMessageWindow()

    #C0363
    ChrTalk(
        0x12,
        (
            "#5P初任務でアリオスさんに\x01",
            "助けられるなんて、情けないなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0364
    ChrTalk(
        0x13,
        (
            "#5Pまだまだ警察には任せられないわね。\x01",
            "少しは精進してもらわなくっちゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0365
    ChrTalk(
        0x12,
        (
            "#5Pま、へっぽこはへっぽこなりに\x01",
            "がんばれってことだね。\x02",
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
    Sleep(1200)

    #C0366
    ChrTalk(
        0x102,
        "#11P#0106F（ひどい言われようねぇ……）\x02",
    )

    CloseMessageWindow()

    #C0367
    ChrTalk(
        0x101,
        "#11P#0000Fき、肝に銘じます。\x02",
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, -3430, 0, 42620, 270)
    OP_93(0x13, 0x10E, 0x0)
    OP_4C(0x13, 0xFF)
    SetScenarioFlags(0x50, 0)
    EventEnd(0x5)
    Return()

    # Function_20_7A84 end

    def Function_21_80E2(): pass

    label("Function_21_80E2")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(7120, 1300, 4730, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(23000, 0)
    SetChrPos(0x101, -1750, 0, 2150, 0)
    SetChrPos(0x102, -2750, 0, 1900, 0)
    SetChrPos(0x103, -1750, 0, 650, 0)
    SetChrPos(0x104, -2750, 0, 400, 0)
    SetChrFlags(0x101, 0x80)
    SetChrBattleFlags(0x101, 0x8000)
    SetChrFlags(0x102, 0x80)
    SetChrBattleFlags(0x102, 0x8000)
    SetChrFlags(0x103, 0x80)
    SetChrBattleFlags(0x103, 0x8000)
    SetChrFlags(0x104, 0x80)
    SetChrBattleFlags(0x104, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_68(950, 1300, 11510, 5000)
    OP_6F(0x1)
    Sleep(1000)
    Fade(500)
    OP_68(-2160, 1300, 4030, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(23000, 0)
    ClearChrFlags(0x101, 0x80)
    ClearChrBattleFlags(0x101, 0x8000)
    ClearChrFlags(0x102, 0x80)
    ClearChrBattleFlags(0x102, 0x8000)
    ClearChrFlags(0x103, 0x80)
    ClearChrBattleFlags(0x103, 0x8000)
    ClearChrFlags(0x104, 0x80)
    ClearChrBattleFlags(0x104, 0x8000)
    OP_4B(0x8, 0xFF)
    SetChrSubChip(0x8, 0x0)
    OP_0D()

    #C0368
    ChrTalk(
        0x101,
        (
            "#11P#0000Fここは──\x01",
            "遊撃士協会#10Rブレイサーギルド#か。\x02",
        )
    )

    CloseMessageWindow()

    #C0369
    ChrTalk(
        0x103,
        (
            "#11P#0203F遊撃士協会……\x01",
            "民間人の保護・支援を請け負う\x01",
            "国際的な非政府組織ですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0370
    ChrTalk(
        0x104,
        (
            "#11P#0300Fいわゆる正義の味方、\x01",
            "俺たちの商売敵ってやつだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0371
    ChrTalk(
        0x102,
        (
            "#11P#0100F一応、名目上は\x01",
            "協力関係にあるはずだけど……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0x8, 0xE1, 0x1F4)

    #C0372
    ChrTalk(
        0x8,
        "#6Pあら、いらっしゃい。\x02",
    )

    CloseMessageWindow()

    #C0373
    ChrTalk(
        0x8,
        (
            "#6Pひょっとして、アナタ達が\x01",
            "《特務支援課》の坊やたちかしら？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0374
    ChrTalk(
        0x101,
        "#11P#0005Fえ……！？\x02",
    )

    CloseMessageWindow()

    #C0375
    ChrTalk(
        0x102,
        "#11P#0105Fどうして私たちのことを……\x02",
    )

    CloseMessageWindow()
    OP_68(1000, 1300, 10500, 5000)
    MoveCamera(45, 26, 0, 5000)
    SetCameraDistance(21750, 5000)

    def lambda_8468():
        OP_96(0xFE, 0x5DC, 0x0, 0x27A6, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8468)
    Sleep(50)

    def lambda_8485():
        OP_96(0xFE, 0x1F4, 0x0, 0x26AC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8485)
    Sleep(50)

    def lambda_84A2():
        OP_96(0xFE, 0x5DC, 0x0, 0x21CA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_84A2)
    Sleep(50)

    def lambda_84BF():
        OP_96(0xFE, 0x1F4, 0x0, 0x20D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_84BF)
    Sleep(500)
    OP_93(0x8, 0xB4, 0x1F4)
    WaitChrThread(0x101, 1)

    def lambda_84E7():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_84E7)
    WaitChrThread(0x102, 1)

    def lambda_84F8():
        OP_93(0x102, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_84F8)
    WaitChrThread(0x103, 1)

    def lambda_8509():
        OP_93(0x103, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_8509)
    WaitChrThread(0x104, 1)

    def lambda_851A():
        OP_93(0x104, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_851A)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    OP_6F(0x1)

    #C0376
    ChrTalk(
        0x101,
        (
            "#12P#0000F──初めまして。\x01",
            "クロスベル警察、特務支援課の\x01",
            "ロイド・バニングスです。\x02\x03",

            "#0005Fえっと、あなたは……？\x02",
        )
    )

    CloseMessageWindow()

    #C0377
    ChrTalk(
        0x8,
        "#5Pアタシの名前はミシェル。\x02",
    )

    CloseMessageWindow()

    #C0378
    ChrTalk(
        0x8,
        (
            "#5P遊撃士協会・クロスベル支部の\x01",
            "受付を担当させてもらってるわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0379
    ChrTalk(
        0x8,
        (
            "#5Pアナタたちのことは\x01",
            "アリオスから聞いてるわよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0380
    ChrTalk(
        0x101,
        "#12P#0000Fああ、そうだったんですか。\x02",
    )

    CloseMessageWindow()

    #C0381
    ChrTalk(
        0x102,
        (
            "#12P#0100Fでも、よく私たちが\x01",
            "支援課だと気付かれましたね？\x02",
        )
    )

    CloseMessageWindow()

    #C0382
    ChrTalk(
        0x8,
        (
            "#5Pフフ、その胸のエンブレムと\x01",
            "顔触れを見たら一目瞭然よ。\x02",
        )
    )

    CloseMessageWindow()

    #C0383
    ChrTalk(
        0x8,
        (
            "#5Pどうやらウチと似たような\x01",
            "活動をするみたいだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0384
    ChrTalk(
        0x101,
        "#12P#0000Fそ、それは……\x02",
    )

    CloseMessageWindow()

    #C0385
    ChrTalk(
        0x103,
        "#11P#0203Fまあ、否定できませんね。\x02",
    )

    CloseMessageWindow()

    #C0386
    ChrTalk(
        0x104,
        (
            "#12P#0300Fやっぱギルドとしちゃ、\x01",
            "あんまり面白くはねぇか？\x02",
        )
    )

    CloseMessageWindow()

    #C0387
    ChrTalk(
        0x8,
        (
            "#5Pあら、とんでもない。\x01",
            "ウチとしては大歓迎よ。\x02",
        )
    )

    CloseMessageWindow()

    #C0388
    ChrTalk(
        0x8,
        (
            "#5P何せ依頼の数が多すぎてね。\x01",
            "今いるメンバーだけじゃ\x01",
            "回しきれなくなってるのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0389
    ChrTalk(
        0x8,
        (
            "#5Pアナタたちが分担してくれたら\x01",
            "こちらとしては大助かりだわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0390
    ChrTalk(
        0x101,
        (
            "#12P#0004Fそ、そうですか。\x01",
            "それを聞いて少し安心──\x02",
        )
    )

    CloseMessageWindow()

    #C0391
    ChrTalk(
        0x8,
        (
            "#5P──ただし、\x01",
            "使い物になるんだったらね。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0392
    ChrTalk(
        0x101,
        "#12P#0001Fっ……\x02",
    )

    CloseMessageWindow()

    #C0393
    ChrTalk(
        0x8,
        (
            "#5Pこう言ったらなんだけど\x01",
            "ウチの遊撃士たちは優秀よ。\x02",
        )
    )

    CloseMessageWindow()

    #C0394
    ChrTalk(
        0x8,
        (
            "#5Pアリオスはもちろん、\x01",
            "他のメンバーも全員粒揃い……\x01",
            "エース級の実力を持ってるわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0395
    ChrTalk(
        0x8,
        (
            "#5P警察が市民の人気取りのために\x01",
            "でっち上げた新人ばかりの部署……\x02",
        )
    )

    CloseMessageWindow()

    #C0396
    ChrTalk(
        0x8,
        (
            "#5Pそんな所に果たして\x01",
            "代わりが勤まるのかしらねぇ？\x02",
        )
    )

    CloseMessageWindow()

    #C0397
    ChrTalk(
        0x101,
        "#12P#0005Fそ、それは……\x02",
    )

    CloseMessageWindow()

    #C0398
    ChrTalk(
        0x102,
        "#12P#0108F（……反論できないわね。）\x02",
    )

    CloseMessageWindow()

    #C0399
    ChrTalk(
        0x104,
        "#12P#0303F（ま、正直厳しいかもなぁ。）\x02",
    )

    CloseMessageWindow()

    #C0400
    ChrTalk(
        0x8,
        (
            "#5Pフフ、まあイジめるのは\x01",
            "このくらいにしてあげるわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0401
    ChrTalk(
        0x8,
        (
            "#5Pアナタたちはアナタたちで\x01",
            "せいぜい勝手に頑張りなさい。\x02",
        )
    )

    CloseMessageWindow()

    #C0402
    ChrTalk(
        0x8,
        (
            "#5Pしくじったとしても\x01",
            "こちらがフォローするから。\x02",
        )
    )

    CloseMessageWindow()

    #C0403
    ChrTalk(
        0x101,
        "#12P#0001F……精進させてもらいます。\x02",
    )

    CloseMessageWindow()
    SetChrPos(0x0, 1000, 0, 10150, 0)
    OP_4C(0x8, 0xFF)
    SetScenarioFlags(0x47, 2)
    EventEnd(0x5)
    Return()

    # Function_21_80E2 end

    def Function_22_8BCE(): pass

    label("Function_22_8BCE")

    EventBegin(0x0)
    Fade(500)
    OP_4B(0x8, 0xFF)
    OP_68(1000, 1300, 10500, 0)
    MoveCamera(37, 26, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(21630, 0)
    SetChrPos(0x101, 1500, 0, 10150, 360)
    SetChrPos(0x102, 500, 0, 9900, 360)
    SetChrPos(0x103, 1500, 0, 8650, 360)
    SetChrPos(0x104, 500, 0, 8400, 360)
    OP_93(0x8, 0xB4, 0x0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F, 6)), scpexpr(EXPR_END)), "loc_8E53")

    #C0404
    ChrTalk(
        0x101,
        (
            "#11P#0005Fええっと……\x01",
            "ミシェルさん？\x02\x03",

            "#0000F言われたとおり\x01",
            "来てみたんですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0405
    ChrTalk(
        0x8,
        "#5Pうふふ……待ってたわ。\x02",
    )

    CloseMessageWindow()

    #C0406
    ChrTalk(
        0x8,
        (
            "#5P呼ばれて素直に来るなんて、\x01",
            "なかなか可愛い所もあるじゃない。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0407
    ChrTalk(
        0x101,
        (
            "#11P#0003F……コホン。\x01",
            "ええっと、確か……\x02\x03",

            "#0000F俺たちの実力を確かめるための\x01",
            "趣向を用意しているという話でしたね。\x02",
        )
    )

    CloseMessageWindow()

    #C0408
    ChrTalk(
        0x8,
        "#5Pよく覚えていたわね。\x02",
    )

    CloseMessageWindow()

    #C0409
    ChrTalk(
        0x8,
        (
            "#5P──アナタたち。\x01",
            "よかったらテストを\x01",
            "受けて見る気はない？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_914F")

    label("loc_8E53")


    #C0410
    ChrTalk(
        0x8,
        "#5Pしかし『特務支援課』ねぇ……\x02",
    )

    CloseMessageWindow()

    #C0411
    ChrTalk(
        0x8,
        (
            "#5P警察内部のしがらみと\x01",
            "ゴタゴタで生まれた部署って\x01",
            "聞いたけど、本当なのかしら？\x02",
        )
    )

    CloseMessageWindow()

    #C0412
    ChrTalk(
        0x101,
        (
            "#11P#0006Fうぐっ……\x01",
            "よ、よくご存知ですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0413
    ChrTalk(
        0x8,
        (
            "#5Pギルドの情報網を\x01",
            "侮ってもらっちゃ困るわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0414
    ChrTalk(
        0x8,
        (
            "#5Pここには周辺諸国の噂や情報が\x01",
            "逐一入ってくるわよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0415
    ChrTalk(
        0x8,
        (
            "#5Pその気になれば\x01",
            "エレボニアの帝都にいるイイ男の\x01",
            "数だって調べられるんだから。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0416
    ChrTalk(
        0x104,
        (
            "#12P#0303F（たしかにギルドの\x01",
            "  情報網っていやあ有名だが、\x01",
            "  例えがアレだなぁ……）\x02",
        )
    )

    CloseMessageWindow()

    #C0417
    ChrTalk(
        0x103,
        (
            "#12P#0200F（というか、そもそもどうして\x01",
            "  女性言葉なんでしょう……？）\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0418
    ChrTalk(
        0x8,
        (
            "#5Pでも、そうね。\x01",
            "今後のこともあるワケだし……\x02",
        )
    )

    CloseMessageWindow()

    #C0419
    ChrTalk(
        0x8,
        (
            "#5P──アナタたち。\x01",
            "よかったらテストを\x01",
            "受けて見る気はない？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_914F")

    SetScenarioFlags(0x4F, 6)

    #C0420
    ChrTalk(
        0x101,
        "#11P#0005Fへ……\x02",
    )

    CloseMessageWindow()

    #C0421
    ChrTalk(
        0x102,
        "#12P#0105Fテ、テスト……ですか？\x02",
    )

    CloseMessageWindow()

    #C0422
    ChrTalk(
        0x8,
        (
            "#5P遊撃士の研修に使われる\x01",
            "一般教養の筆記テストから、\x01",
            "私が問題を１０問、出題するわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0423
    ChrTalk(
        0x8,
        (
            "#5Pそのテストは\x01",
            "全問正解すると準遊撃士程度の\x01",
            "知識があると判定できるの。\x02",
        )
    )

    CloseMessageWindow()

    #C0424
    ChrTalk(
        0x8,
        "#5Pつ・ま・り……\x02",
    )

    CloseMessageWindow()

    #C0425
    ChrTalk(
        0x103,
        (
            "#12P#0203Fその問題を解けないようでは\x01",
            "優秀な遊撃士が集うクロスベルじゃ\x01",
            "到底やっていけない……\x02\x03",

            "#0200Fそういうことですか。\x02",
        )
    )

    CloseMessageWindow()

    #C0426
    ChrTalk(
        0x101,
        "#11P#0006Fな、なんかプレッシャーですね……\x02",
    )

    CloseMessageWindow()

    #C0427
    ChrTalk(
        0x104,
        (
            "#12P#0306Fつーか、間違えたら\x01",
            "今後馬鹿にされ続けそうだな……\x02",
        )
    )

    CloseMessageWindow()

    #C0428
    ChrTalk(
        0x8,
        (
            "#5Pんふふ……\x01",
            "そんな悪趣味なことしないわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0429
    ChrTalk(
        0x8,
        (
            "#5P問題の内容も、行政区の図書館で\x01",
            "一通り学べる程度のものだし。\x02",
        )
    )

    CloseMessageWindow()

    #C0430
    ChrTalk(
        0x8,
        (
            "#5Pあくまで、あんたたちが\x01",
            "ここクロスベルで使い物になるか\x01",
            "確かめたいってだけよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0431
    ChrTalk(
        0x8,
        (
            "#5P……で、どうする？\x01",
            "早速やってみる？\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x4, 0x4, 0x2)
    OP_29(0x4, 0x1, 0x0)
    Call(0, 24)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9452")
    Call(0, 25)
    Call(0, 26)

    label("loc_9452")

    SetChrPos(0x0, 1000, 0, 10150, 360)
    OP_4C(0x8, 0xFF)
    EventEnd(0x5)
    Return()

    # Function_22_8BCE end

    def Function_23_946A(): pass

    label("Function_23_946A")

    EventBegin(0x0)
    Fade(500)
    OP_4B(0x8, 0xFF)
    OP_68(1000, 1300, 10500, 0)
    MoveCamera(37, 26, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(21630, 0)
    SetChrPos(0x101, 1500, 0, 10150, 360)
    SetChrPos(0x102, 500, 0, 9900, 360)
    SetChrPos(0x103, 1500, 0, 8650, 360)
    SetChrPos(0x104, 500, 0, 8400, 360)
    OP_93(0x8, 0xB4, 0x0)
    OP_0D()

    #C0432
    ChrTalk(
        0x8,
        (
            "#5P遊撃士の研修に使われる\x01",
            "一般教養の筆記テストから、\x01",
            "私が問題を１０問、出題するわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0433
    ChrTalk(
        0x8,
        (
            "#5P全問正解すると準遊撃士程度の\x01",
            "知識があると判定できるわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0434
    ChrTalk(
        0x8,
        (
            "#5Pと言っても、行政区の図書館で\x01",
            "一通り学べる程度の簡単な問題だけどね。\x02",
        )
    )

    CloseMessageWindow()

    #C0435
    ChrTalk(
        0x8,
        (
            "#5P……で、どうする？\x01",
            "やってみる？\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 24)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9614")
    Call(0, 25)
    Call(0, 26)

    label("loc_9614")

    SetChrPos(0x0, 1000, 0, 10150, 360)
    OP_4C(0x8, 0xFF)
    EventEnd(0x5)
    Return()

    # Function_23_946A end

    def Function_24_962C(): pass

    label("Function_24_962C")

    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【受けて立つ】\x01",      # 0
            "【やめる】\x01",          # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9725")

    #C0436
    ChrTalk(
        0x101,
        (
            "#11P#0012Fうーん……\x01",
            "ちょっとまだ心の準備が。\x02",
        )
    )

    CloseMessageWindow()

    #C0437
    ChrTalk(
        0x8,
        (
            "#5Pあら、怖気づいちゃった？\x01",
            "意外と小心者なのねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0438
    ChrTalk(
        0x8,
        (
            "#5Pまぁいいわ。\x01",
            "テストを受けたくなったら\x01",
            "また声をかけて頂戴。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9725")

    Return()

    # Function_24_962C end

    def Function_25_9726(): pass

    label("Function_25_9726")


    #C0439
    ChrTalk(
        0x101,
        "#11P#0001F……受けて立ちましょう。\x02",
    )

    CloseMessageWindow()

    #C0440
    ChrTalk(
        0x8,
        "#5Pそうこなくっちゃ♪\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 500)

    #C0441
    ChrTalk(
        0x104,
        "#12P#0305Fおいおい、大丈夫かよロイド。\x02",
    )

    CloseMessageWindow()

    def lambda_97A1():
        TurnDirection(0x101, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_97A1)
    Sleep(50)

    def lambda_97B1():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_97B1)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)

    #C0442
    ChrTalk(
        0x101,
        (
            "#11P#0003Fああ、一般教養のテストなら\x01",
            "警察学校でも出たしな。\x02\x03",

            "#0001Fなにより……\x01",
            "ここで引き下がったら\x01",
            "負けのような気がするし。\x02",
        )
    )

    CloseMessageWindow()

    #C0443
    ChrTalk(
        0x102,
        "#6P#0100F……うん、そうね。\x02",
    )

    CloseMessageWindow()

    #C0444
    ChrTalk(
        0x103,
        "#12P#0203F同感です。\x02",
    )

    CloseMessageWindow()

    #C0445
    ChrTalk(
        0x104,
        (
            "#12P#0300Fま、そう言われりゃ\x01",
            "そうだな。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_98B1():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_98B1)

    def lambda_98BE():
        OP_93(0x102, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_98BE)

    def lambda_98CB():
        OP_93(0x104, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_98CB)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x104, 1)

    #C0446
    ChrTalk(
        0x8,
        (
            "#5Pうふふ……嫌いじゃないわ、\x01",
            "そういう根性論みたいなの。\x02",
        )
    )

    CloseMessageWindow()

    #C0447
    ChrTalk(
        0x8,
        (
            "#5Pそうね、見たところあなたが\x01",
            "リーダーみたいだし……\x02",
        )
    )

    CloseMessageWindow()

    #C0448
    ChrTalk(
        0x8,
        (
            "#5Pテストの回答は\x01",
            "あなたにしてもらおうかしら。\x02",
        )
    )

    CloseMessageWindow()

    #C0449
    ChrTalk(
        0x101,
        "#11P#0001F……分かりました。\x02",
    )

    CloseMessageWindow()

    #C0450
    ChrTalk(
        0x8,
        (
            "#5Pふふん、いい目ね。\x01",
            "ゾクゾクしちゃう。\x02",
        )
    )

    CloseMessageWindow()

    #C0451
    ChrTalk(
        0x8,
        (
            "#5Pそれじゃあ早速……\x01",
            "始めるとしましょうか！\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(80, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0452
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "クエスト【ミシェルの挑戦状】\x07\x00",
            "を開始した！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    StopBGM(0xBB8)
    OP_68(1000, 1950, 9200, 0)
    MoveCamera(0, 22, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(20390, 0)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7111", 0)
    FadeToBright(1000, 0)
    OP_0D()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0453
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "遊撃士協会支部・受付ミシェルの挑戦\x01",
            "　　～遊撃士・一般教養テスト～\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    #C0454
    ChrTalk(
        0x8,
        (
            "#5P──第１問！！\x01",
            "まずは小手調べね。\x02",
        )
    )

    CloseMessageWindow()

    #C0455
    ChrTalk(
        0x8,
        (
            "#5Pこの大陸に導力器#6Rオーブメント#をもたらした\x01",
            "《導力革命》と呼ばれる技術革命……\x02",
        )
    )

    CloseMessageWindow()

    #C0456
    ChrTalk(
        0x8,
        "#5Pそれが起こったのは何年前？\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 16, -1, -1)
    SetChrName("")

    #A0457
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            "《導力革命》が起こったのは？",
            scpstr(0x18),
            scpstr(SCPSTR_CODE_ENTER),
        )
    )


    Menu(
        0,
        -1,
        150,
        0,
        (
            "【①約１０年前】\x01",      # 0
            "【②約３０年前】\x01",      # 1
            "【③約５０年前】\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_9C64"),
        (1, "loc_9DF6"),
        (2, "loc_9F82"),
        (SWITCH_DEFAULT, "loc_A104"),
    )


    label("loc_9C64")


    #C0458
    ChrTalk(
        0x101,
        "#12P#0000F……約１０年前、でしたっけ。\x02",
    )

    CloseMessageWindow()

    #C0459
    ChrTalk(
        0x8,
        "#5P…………………………\x02",
    )

    CloseMessageWindow()
    Sound(3, 0, 100, 0)

    #C0460
    ChrTalk(
        0x8,
        (
            "#5Pブ～ッ！！　はずれ！\x01",
            "そんなに最近なワケないじゃない。\x02",
        )
    )

    CloseMessageWindow()

    #C0461
    ChrTalk(
        0x8,
        "#5P正解は、約５０年前。\x02",
    )

    CloseMessageWindow()

    #C0462
    ChrTalk(
        0x8,
        (
            "#5Pたった半世紀程度で\x01",
            "ここまで導力器が発達しているのは\x01",
            "なかなかすごいことよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0463
    ChrTalk(
        0x8,
        (
            "#5Pアタシも子供の頃は、\x01",
            "まさか車なんて乗り物が\x01",
            "出来るとは思ってなかったわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0464
    ChrTalk(
        0x101,
        (
            "#12P#0006F（うーん、いきなり\x01",
            "  間違えてしまったか……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A104")

    label("loc_9DF6")


    #C0465
    ChrTalk(
        0x101,
        "#12P#0000F……約３０年前、でしたっけ。\x02",
    )

    CloseMessageWindow()

    #C0466
    ChrTalk(
        0x8,
        "#5P…………………………\x02",
    )

    CloseMessageWindow()
    Sound(3, 0, 100, 0)

    #C0467
    ChrTalk(
        0x8,
        (
            "#5Pブ～ッ！！　はずれ！\x01",
            "適当なこと言っちゃダメよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0468
    ChrTalk(
        0x8,
        "#5P正解は、約５０年前。\x02",
    )

    CloseMessageWindow()

    #C0469
    ChrTalk(
        0x8,
        (
            "#5Pたった半世紀程度で\x01",
            "ここまで導力器が発達しているのは\x01",
            "なかなかすごいことよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0470
    ChrTalk(
        0x8,
        (
            "#5Pアタシも子供の頃は、\x01",
            "まさか車なんて乗り物が\x01",
            "出来るとは思ってなかったわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0471
    ChrTalk(
        0x101,
        (
            "#12P#0006F（うーん、いきなり\x01",
            "  間違えてしまったか……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A104")

    label("loc_9F82")


    #C0472
    ChrTalk(
        0x101,
        "#12P#0000F……約５０年前、でしたっけ。\x02",
    )

    CloseMessageWindow()

    #C0473
    ChrTalk(
        0x8,
        "#5P…………………………\x02",
    )

    CloseMessageWindow()
    Sound(87, 0, 100, 0)

    #C0474
    ChrTalk(
        0x8,
        "#5Pピンポーン！　正解！\x02",
    )

    CloseMessageWindow()

    #C0475
    ChrTalk(
        0x8,
        "#5Pま、この程度は常識よね。\x02",
    )

    CloseMessageWindow()

    #C0476
    ChrTalk(
        0x8,
        (
            "#5Pそれにしても、たった半世紀程度で\x01",
            "ここまで導力器が発達しているのは\x01",
            "なかなかすごいことよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0477
    ChrTalk(
        0x8,
        (
            "#5Pアタシも子供の頃は、\x01",
            "まさか車なんて乗り物が\x01",
            "出来るとは思ってなかったわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0478
    ChrTalk(
        0x101,
        "#12P#0004F（とりあえず最初は乗り切ったな。）\x02",
    )

    CloseMessageWindow()
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_A104")

    label("loc_A104")


    #C0479
    ChrTalk(
        0x8,
        (
            "#5Pさぁ、どんどんいくわよ～。\x01",
            "──第２問！！\x02",
        )
    )

    CloseMessageWindow()

    #C0480
    ChrTalk(
        0x8,
        (
            "#5P《導力革命》が起こる要因となったのは、\x01",
            "とある人物が最初の導力器を発明したからなの。\x02",
        )
    )

    CloseMessageWindow()

    #C0481
    ChrTalk(
        0x8,
        (
            "#5P導力器を生み出した人物の名前……\x01",
            "当然、分かるわよね？\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 16, -1, -1)
    SetChrName("")

    #A0482
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            "導力器を生み出した人物は？",
            scpstr(0x18),
            scpstr(SCPSTR_CODE_ENTER),
        )
    )


    Menu(
        0,
        -1,
        150,
        0,
        (
            "【①Ａ・ラッセル博士】\x01",          # 0
            "【②Ｃ・エプスタイン博士】\x01",      # 1
            "【③Ｇ・シュミット博士】\x01",        # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_A290"),
        (1, "loc_A560"),
        (2, "loc_A7DC"),
        (SWITCH_DEFAULT, "loc_AAA4"),
    )


    label("loc_A290")


    #C0483
    ChrTalk(
        0x101,
        "#12P#0000F……Ａ・ラッセル博士、ですよね？\x02",
    )

    CloseMessageWindow()

    #C0484
    ChrTalk(
        0x8,
        "#5P…………………………\x02",
    )

    CloseMessageWindow()
    Sound(3, 0, 100, 0)

    #C0485
    ChrTalk(
        0x8,
        "#5Pブ～ッ！！　惜しい、はずれよ。\x02",
    )

    CloseMessageWindow()

    #C0486
    ChrTalk(
        0x8,
        "#5P正解は、Ｃ・エプスタイン博士。\x02",
    )

    CloseMessageWindow()

    #C0487
    ChrTalk(
        0x8,
        (
            "#5Pエプスタイン博士が発明した導力器は、\x01",
            "最初はあまり世間に\x01",
            "受け入れられていなかったのよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0488
    ChrTalk(
        0x8,
        (
            "#5Pでも、徐々にその利便性は認められて、\x01",
            "今では私たちの生活に\x01",
            "なくてはならないものになったわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0489
    ChrTalk(
        0x8,
        (
            "#5Pちなみに、ラッセル博士は\x01",
            "エプスタイン博士の弟子で、\x01",
            "《導力革命》に大きく貢献した人物ね。\x02",
        )
    )

    CloseMessageWindow()

    #C0490
    ChrTalk(
        0x101,
        (
            "#12P#0006F（うーん……\x01",
            "  そういえば聞いたことあったな。）\x02",
        )
    )

    CloseMessageWindow()

    #C0491
    ChrTalk(
        0x103,
        (
            "#12P#0200Fさらに補足すると……\x01",
            "エプスタイン財団は\x01",
            "わたしが所属している団体です。\x02\x03",

            "#0211Fこの間言ったばかりかと思いますが……\x01",
            "忘れちゃってましたか？\x02",
        )
    )

    CloseMessageWindow()

    #C0492
    ChrTalk(
        0x101,
        (
            "#12P#0003Fう……\x01",
            "（視線がイタイ……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AAA4")

    label("loc_A560")


    #C0493
    ChrTalk(
        0x101,
        "#12P#0000F……Ｃ・エプスタイン博士、ですね。\x02",
    )

    CloseMessageWindow()

    #C0494
    ChrTalk(
        0x8,
        "#5P…………………………\x02",
    )

    CloseMessageWindow()
    Sound(87, 0, 100, 0)

    #C0495
    ChrTalk(
        0x8,
        "#5Pピンポーン！！　正解よ。\x02",
    )

    CloseMessageWindow()

    #C0496
    ChrTalk(
        0x8,
        (
            "#5Pエプスタイン博士が発明した導力器は、\x01",
            "最初はあまり世間に\x01",
            "受け入れられていなかったのよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0497
    ChrTalk(
        0x8,
        (
            "#5Pでも、徐々にその利便性は認められて、\x01",
            "今では私たちの生活に\x01",
            "なくてはならないものになったわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0498
    ChrTalk(
        0x103,
        (
            "#12P#0203F財団が導力器の研究や普及のために\x01",
            "数多くの活動をしているのは\x01",
            "あまりにも有名です。\x02\x03",

            "#0200Fわたしの行う魔導杖の実戦テストも\x01",
            "その一環と言えますね。\x02",
        )
    )

    CloseMessageWindow()

    #C0499
    ChrTalk(
        0x101,
        (
            "#12P#0003F（そういえば、ティオも\x01",
            "  エプスタイン財団の人間だったな。）\x02\x03",

            "#0000F（……危ない危ない。\x01",
            "  不正解だったら何を言われてたことか……）\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_AAA4")

    label("loc_A7DC")


    #C0500
    ChrTalk(
        0x101,
        "#12P#0000F……Ｇ・シュミット博士、でしたっけ？\x02",
    )

    CloseMessageWindow()

    #C0501
    ChrTalk(
        0x8,
        "#5P…………………………\x02",
    )

    CloseMessageWindow()
    Sound(3, 0, 100, 0)

    #C0502
    ChrTalk(
        0x8,
        "#5Pブ～ッ！！　はずれ。\x02",
    )

    CloseMessageWindow()

    #C0503
    ChrTalk(
        0x8,
        "#5P正解は、Ｃ・エプスタイン博士。\x02",
    )

    CloseMessageWindow()

    #C0504
    ChrTalk(
        0x8,
        (
            "#5Pエプスタイン博士が発明した導力器は、\x01",
            "最初はあまり世間に\x01",
            "受け入れられていなかったのよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0505
    ChrTalk(
        0x8,
        (
            "#5Pでも、徐々にその利便性は認められて、\x01",
            "今では私たちの生活に\x01",
            "なくてはならないものになったわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0506
    ChrTalk(
        0x8,
        (
            "#5Pちなみに、シュミット博士は\x01",
            "エプスタイン博士の弟子で、\x01",
            "機械工学の権威と呼ばれる人物ね。\x02",
        )
    )

    CloseMessageWindow()

    #C0507
    ChrTalk(
        0x101,
        (
            "#12P#0006F（うーん……\x01",
            "  そういえば聞いたことあったな。）\x02",
        )
    )

    CloseMessageWindow()

    #C0508
    ChrTalk(
        0x103,
        (
            "#12P#0203Fさらに補足すると……\x01",
            "エプスタイン財団は\x01",
            "わたしが所属している団体です。\x02\x03",

            "#0211Fこの間言ったばかりかと思いますが……\x01",
            "忘れちゃってましたか？\x02",
        )
    )

    CloseMessageWindow()

    #C0509
    ChrTalk(
        0x101,
        (
            "#12P#0003Fう……\x01",
            "（視線がイタイ……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AAA4")

    label("loc_AAA4")


    #C0510
    ChrTalk(
        0x8,
        "#5P次は──第３問！！\x02",
    )

    CloseMessageWindow()

    #C0511
    ChrTalk(
        0x8,
        (
            "#5P導力器の肝とも言える部品に、\x01",
            "結晶回路#8Rクオーツ#というものがあるわね？\x02",
        )
    )

    CloseMessageWindow()

    #C0512
    ChrTalk(
        0x8,
        (
            "#5Pこの結晶回路を作るには\x01",
            "セピスが必要不可欠なの。\x02",
        )
    )

    CloseMessageWindow()

    #C0513
    ChrTalk(
        0x8,
        (
            "#5Pでは……セピスとは、\x01",
            "七耀石のどんな状態のことを\x01",
            "言うのかしら？\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 16, -1, -1)
    SetChrName("")

    #A0514
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            "セピスと呼ばれるもの、\x01",
            "それは……？",
            scpstr(0x18),
            scpstr(SCPSTR_CODE_ENTER),
        )
    )


    Menu(
        0,
        -1,
        150,
        0,
        (
            "【①七耀石の結晶】\x01",        # 0
            "【②七耀石の細工品】\x01",      # 1
            "【③七耀石の欠片】\x01",        # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_AC47"),
        (1, "loc_ADF0"),
        (2, "loc_AF9B"),
        (SWITCH_DEFAULT, "loc_B11E"),
    )


    label("loc_AC47")


    #C0515
    ChrTalk(
        0x101,
        "#12P#0000F……七耀石の結晶です。\x02",
    )

    CloseMessageWindow()

    #C0516
    ChrTalk(
        0x8,
        "#5P…………………………\x02",
    )

    CloseMessageWindow()
    Sound(3, 0, 100, 0)

    #C0517
    ChrTalk(
        0x8,
        "#5Pブー！！　違います！\x02",
    )

    CloseMessageWindow()

    #C0518
    ChrTalk(
        0x8,
        "#5P正解は、七耀石の欠片よ。\x02",
    )

    CloseMessageWindow()

    #C0519
    ChrTalk(
        0x8,
        (
            "#5P欠片の状態になった七耀石を\x01",
            "加工して結晶回路を作るのよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0520
    ChrTalk(
        0x8,
        (
            "#5P魔獣は七耀石に惹かれるという\x01",
            "性質を持っているから、\x01",
            "セピスをよく飲み込んでいるの。\x02",
        )
    )

    CloseMessageWindow()

    #C0521
    ChrTalk(
        0x8,
        (
            "#5Pセピスを集めるためには\x01",
            "魔獣を倒すのが\x01",
            "手っ取り早いってことね。\x02",
        )
    )

    CloseMessageWindow()

    #C0522
    ChrTalk(
        0x101,
        (
            "#12P#0006F（うーん……\x01",
            "  サービス問題だったか……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B11E")

    label("loc_ADF0")


    #C0523
    ChrTalk(
        0x101,
        "#12P#0000F……七耀石の細工品です。\x02",
    )

    CloseMessageWindow()

    #C0524
    ChrTalk(
        0x8,
        "#5P…………………………\x02",
    )

    CloseMessageWindow()
    Sound(3, 0, 100, 0)

    #C0525
    ChrTalk(
        0x8,
        "#5Pブー！！　違います！\x02",
    )

    CloseMessageWindow()

    #C0526
    ChrTalk(
        0x8,
        "#5P正解は、七耀石の欠片よ。\x02",
    )

    CloseMessageWindow()

    #C0527
    ChrTalk(
        0x8,
        (
            "#5P欠片の状態になった七耀石を\x01",
            "加工して結晶回路を作るのよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0528
    ChrTalk(
        0x8,
        (
            "#5P魔獣は七耀石に惹かれるという\x01",
            "性質を持っているから、\x01",
            "セピスをよく飲み込んでいるの。\x02",
        )
    )

    CloseMessageWindow()

    #C0529
    ChrTalk(
        0x8,
        (
            "#5Pセピスを集めるためには\x01",
            "魔獣を倒すのが\x01",
            "手っ取り早いってことね。\x02",
        )
    )

    CloseMessageWindow()

    #C0530
    ChrTalk(
        0x101,
        (
            "#12P#0006F（うーん……\x01",
            "  サービス問題だったか……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B11E")

    label("loc_AF9B")


    #C0531
    ChrTalk(
        0x101,
        "#12P#0000F……七耀石の欠片です。\x02",
    )

    CloseMessageWindow()

    #C0532
    ChrTalk(
        0x8,
        "#5P…………………………\x02",
    )

    CloseMessageWindow()
    Sound(87, 0, 100, 0)

    #C0533
    ChrTalk(
        0x8,
        "#5Pピンポーン！！　正解！\x02",
    )

    CloseMessageWindow()

    #C0534
    ChrTalk(
        0x8,
        (
            "#5P欠片の状態になった七耀石を\x01",
            "加工して結晶回路を作るのよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0535
    ChrTalk(
        0x8,
        (
            "#5P魔獣は七耀石に惹かれるという\x01",
            "性質を持っているから、\x01",
            "セピスをよく飲み込んでいるの。\x02",
        )
    )

    CloseMessageWindow()

    #C0536
    ChrTalk(
        0x8,
        (
            "#5Pセピスを集めるためには\x01",
            "魔獣を倒すのが\x01",
            "手っ取り早いってことね。\x02",
        )
    )

    CloseMessageWindow()

    #C0537
    ChrTalk(
        0x101,
        "#12P#0004F（うん、まぁ常識だな。）\x02",
    )

    CloseMessageWindow()
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_B11E")

    label("loc_B11E")


    #C0538
    ChrTalk(
        0x8,
        "#5P続けて──第４問！！\x02",
    )

    CloseMessageWindow()

    #C0539
    ChrTalk(
        0x8,
        (
            "#5Pクロスベル自治州の西部に位置する\x01",
            "《エレボニア帝国》──\x02",
        )
    )

    CloseMessageWindow()

    #C0540
    ChrTalk(
        0x8,
        (
            "#5P私たちクロスベルに住む者にとって\x01",
            "この存在はとても大きなものよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0541
    ChrTalk(
        0x8,
        (
            "#5Pそのエレボニア帝国の紋章に\x01",
            "象徴として描かれたもの……\x01",
            "あなたに分かるかしら？\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 16, -1, -1)
    SetChrName("")

    #A0542
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            "エレボニア帝国の紋章に\x01",
            "描かれているものは？",
            scpstr(0x18),
            scpstr(SCPSTR_CODE_ENTER),
        )
    )


    Menu(
        0,
        -1,
        150,
        0,
        (
            "【①支える籠手】\x01",      # 0
            "【②白ハヤブサ】\x01",      # 1
            "【③黄金の軍馬】\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_B2D3"),
        (1, "loc_B452"),
        (2, "loc_B5C2"),
        (SWITCH_DEFAULT, "loc_B75A"),
    )


    label("loc_B2D3")


    #C0543
    ChrTalk(
        0x101,
        "#12P#0000F……支える籠手、かな？\x02",
    )

    CloseMessageWindow()

    #C0544
    ChrTalk(
        0x8,
        "#5P…………………………\x02",
    )

    CloseMessageWindow()
    Sound(3, 0, 100, 0)

    #C0545
    ChrTalk(
        0x8,
        "#5Pブ～ッ！！　は・ず・れ。\x02",
    )

    CloseMessageWindow()

    #C0546
    ChrTalk(
        0x8,
        "#5P正解は、黄金の軍馬。\x02",
    )

    CloseMessageWindow()

    #C0547
    ChrTalk(
        0x8,
        (
            "#5P帝国は強大な軍事力を誇る\x01",
            "軍事大国として知られているわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0548
    ChrTalk(
        0x8,
        (
            "#5Pその力の象徴として黄金の軍馬が\x01",
            "紋章に描かれているというわけ。\x02",
        )
    )

    CloseMessageWindow()

    #C0549
    ChrTalk(
        0x8,
        (
            "#5Pちなみに、支える籠手は\x01",
            "遊撃士協会の紋章よ。\x02",
        )
    )

    CloseMessageWindow()

    #C0550
    ChrTalk(
        0x101,
        (
            "#12P#0006F（う～ん……\x01",
            "  段々難しくなってきたな。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B75A")

    label("loc_B452")


    #C0551
    ChrTalk(
        0x101,
        "#12P#0000F……白ハヤブサ……だったような？\x02",
    )

    CloseMessageWindow()

    #C0552
    ChrTalk(
        0x8,
        "#5P…………………………\x02",
    )

    CloseMessageWindow()
    Sound(3, 0, 100, 0)

    #C0553
    ChrTalk(
        0x8,
        "#5Pブ～ッ！！　は・ず・れ。\x02",
    )

    CloseMessageWindow()

    #C0554
    ChrTalk(
        0x8,
        "#5P正解は、黄金の軍馬。\x02",
    )

    CloseMessageWindow()

    #C0555
    ChrTalk(
        0x8,
        (
            "#5P帝国は強大な軍事力を誇る\x01",
            "軍事大国として知られているわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0556
    ChrTalk(
        0x8,
        (
            "#5Pその力の象徴として黄金の軍馬が\x01",
            "紋章に描かれているというわけ。\x02",
        )
    )

    CloseMessageWindow()

    #C0557
    ChrTalk(
        0x8,
        (
            "#5Pちなみに、白ハヤブサは\x01",
            "リベール王国の紋章ね。\x02",
        )
    )

    CloseMessageWindow()

    #C0558
    ChrTalk(
        0x101,
        "#12P#0006F（とほほ……）\x02",
    )

    CloseMessageWindow()
    Jump("loc_B75A")

    label("loc_B5C2")


    #C0559
    ChrTalk(
        0x101,
        "#12P#0000F……確か、黄金の軍馬ですね？\x02",
    )

    CloseMessageWindow()

    #C0560
    ChrTalk(
        0x8,
        "#5P…………………………\x02",
    )

    CloseMessageWindow()
    Sound(87, 0, 100, 0)

    #C0561
    ChrTalk(
        0x8,
        "#5Pピンポーン！！　正解。\x02",
    )

    CloseMessageWindow()

    #C0562
    ChrTalk(
        0x8,
        (
            "#5P帝国は強大な軍事力を誇る\x01",
            "軍事大国として知られているわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0563
    ChrTalk(
        0x8,
        (
            "#5Pその力の象徴として黄金の軍馬が\x01",
            "紋章に描かれているというわけ。\x02",
        )
    )

    CloseMessageWindow()

    #C0564
    ChrTalk(
        0x8,
        (
            "#5P帝国では昔、鉄騎隊っていう\x01",
            "大規模な騎馬部隊が活躍したそうだから、\x01",
            "その辺に由来があるんでしょうね。\x02",
        )
    )

    CloseMessageWindow()

    #C0565
    ChrTalk(
        0x101,
        "#12P#0004F（よし、なんとか正解だ。）\x02",
    )

    CloseMessageWindow()
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_B75A")

    label("loc_B75A")


    #C0566
    ChrTalk(
        0x8,
        (
            "#5P──第５問！！\x01",
            "いよいよ折り返し地点ね。\x02",
        )
    )

    CloseMessageWindow()

    #C0567
    ChrTalk(
        0x8,
        (
            "#5P帝国の反対方向……\x01",
            "つまりクロスベル自治州の東部には、\x01",
            "《カルバード共和国》が存在するわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0568
    ChrTalk(
        0x8,
        (
            "#5P帝国と共和国という２つの大国の\x01",
            "長きに渡る対立が、このクロスベルの\x01",
            "歴史と言って過言ではないわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0569
    ChrTalk(
        0x8,
        (
            "#5Pでは、そのカルバード共和国に存在し、\x01",
            "導力銃や重工業を主に手がける\x01",
            "有名な導力器メーカーは何だったかしら？\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 16, -1, -1)
    SetChrName("")

    #A0570
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            "共和国に存在する\x01",
            "有名導力器メーカーの名前は？",
            scpstr(0x18),
            scpstr(SCPSTR_CODE_ENTER),
        )
    )


    Menu(
        0,
        -1,
        150,
        0,
        (
            "【①ヴェルヌ社】\x01",            # 0
            "【②ラインフォルト社】\x01",      # 1
            "【③ツァイス中央工房】\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_B98A"),
        (1, "loc_BB11"),
        (2, "loc_BD23"),
        (SWITCH_DEFAULT, "loc_BF2B"),
    )


    label("loc_B98A")


    #C0571
    ChrTalk(
        0x101,
        "#12P#0000F……それはもちろん、ヴェルヌ社です。\x02",
    )

    CloseMessageWindow()

    #C0572
    ChrTalk(
        0x8,
        "#5P…………………………\x02",
    )

    CloseMessageWindow()
    Sound(87, 0, 100, 0)

    #C0573
    ChrTalk(
        0x8,
        "#5Pピンポーン！！　正解正解！\x02",
    )

    CloseMessageWindow()

    #C0574
    ChrTalk(
        0x8,
        (
            "#5P共和国のヴェルヌ社と\x01",
            "帝国のラインフォルト社は\x01",
            "導力銃の２大メーカーとして有名よ。\x02",
        )
    )

    CloseMessageWindow()

    #C0575
    ChrTalk(
        0x8,
        (
            "#5P実は導力車や導力バスの開発も\x01",
            "行なっている、意外と手広い\x01",
            "メーカーなのよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0576
    ChrTalk(
        0x101,
        (
            "#12P#0004F（ふう……\x01",
            "  紛らわしかったけど\x01",
            "  間違いじゃなかったみたいだな。）\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_BF2B")

    label("loc_BB11")


    #C0577
    ChrTalk(
        0x101,
        (
            "#12P#0000F……ラインフォルト社、って\x01",
            "見覚えがあるかも……\x02",
        )
    )

    CloseMessageWindow()

    #C0578
    ChrTalk(
        0x8,
        "#5P…………………………\x02",
    )

    CloseMessageWindow()
    Sound(3, 0, 100, 0)

    #C0579
    ChrTalk(
        0x8,
        "#5Pブッブー！！　残念、はずれ！\x02",
    )

    CloseMessageWindow()

    #C0580
    ChrTalk(
        0x8,
        (
            "#5P正解は、ヴェルヌ社よ。\x01",
            "確かに紛らわしかったけど、\x01",
            "ラインフォルト社は帝国ね。\x02",
        )
    )

    CloseMessageWindow()

    #C0581
    ChrTalk(
        0x8,
        (
            "#5P共和国のヴェルヌ社と\x01",
            "帝国のラインフォルト社は\x01",
            "導力銃の２大メーカーとして有名よ。\x02",
        )
    )

    CloseMessageWindow()

    #C0582
    ChrTalk(
        0x8,
        (
            "#5P実は導力車や導力バスの開発も\x01",
            "行なっている、意外と手広い\x01",
            "メーカーなのよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0583
    ChrTalk(
        0x102,
        (
            "#5P#0106Fはぁ……何でこんな問題を\x01",
            "間違えるのかしら。\x02",
        )
    )

    CloseMessageWindow()

    #C0584
    ChrTalk(
        0x101,
        (
            "#12P#0003F（導力銃使いのエリィには\x01",
            "  簡単な問題だったみたいだな……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BF2B")

    label("loc_BD23")


    #C0585
    ChrTalk(
        0x101,
        (
            "#12P#0000F……ツァイス中央工房。\x01",
            "たしかそんな名前だった気が……\x02",
        )
    )

    CloseMessageWindow()

    #C0586
    ChrTalk(
        0x8,
        "#5P…………………………\x02",
    )

    CloseMessageWindow()
    Sound(3, 0, 100, 0)

    #C0587
    ChrTalk(
        0x8,
        "#5Pブッブー！！　残念、はずれ！\x02",
    )

    CloseMessageWindow()

    #C0588
    ChrTalk(
        0x8,
        (
            "#5P正解は、ヴェルヌ社よ。\x01",
            "ツァイス中央工房は\x01",
            "リベールにあるわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0589
    ChrTalk(
        0x8,
        (
            "#5P共和国のヴェルヌ社と\x01",
            "帝国のラインフォルト社は\x01",
            "導力銃の２大メーカーとして有名よ。\x02",
        )
    )

    CloseMessageWindow()

    #C0590
    ChrTalk(
        0x8,
        (
            "#5P実は導力車や導力バスの開発も\x01",
            "行なっている、意外と手広い\x01",
            "メーカーなのよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0591
    ChrTalk(
        0x102,
        (
            "#5P#0106Fはぁ……何でこんな問題を\x01",
            "間違えるのかしら。\x02",
        )
    )

    CloseMessageWindow()

    #C0592
    ChrTalk(
        0x101,
        (
            "#12P#0003F（導力銃使いのエリィには\x01",
            "  簡単な問題だったみたいだな……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BF2B")

    label("loc_BF2B")


    #C0593
    ChrTalk(
        0x8,
        (
            "#5P……さ～て、とりあえず\x01",
            "半分まで来たわね。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C0D1")

    #C0594
    ChrTalk(
        0x103,
        (
            "#12P#0200F……今のところ、かなり\x01",
            "いい感じですね。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_BFA8():
        TurnDirection(0x101, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_BFA8)
    Sleep(50)

    def lambda_BFB8():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_BFB8)

    def lambda_BFC5():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_BFC5)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x104, 1)

    #C0595
    ChrTalk(
        0x104,
        (
            "#6P#0309Fやるじゃん、リーダー。\x01",
            "この調子なら残りも楽勝だな。\x02",
        )
    )

    CloseMessageWindow()

    #C0596
    ChrTalk(
        0x102,
        (
            "#5P#0102Fええ、正直驚いたわ。\x01",
            "すごいじゃない、ロイド。\x02",
        )
    )

    CloseMessageWindow()

    #C0597
    ChrTalk(
        0x101,
        (
            "#11P#0012Fはは……まぁ、\x01",
            "一般教養くらいなら\x01",
            "こんなものだよ。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_C09E():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_C09E)

    def lambda_C0AB():
        OP_93(0x102, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_C0AB)

    def lambda_C0B8():
        OP_93(0x104, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_C0B8)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x104, 1)
    Jump("loc_C331")

    label("loc_C0D1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C203")

    #C0598
    ChrTalk(
        0x103,
        "#12P#0200Fニアミスが目立ちます。\x02",
    )

    CloseMessageWindow()

    def lambda_C10B():
        TurnDirection(0x101, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_C10B)
    Sleep(50)

    def lambda_C11B():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_C11B)

    def lambda_C128():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_C128)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x104, 1)

    #C0599
    ChrTalk(
        0x104,
        "#6P#0303F可もなく不可もなくだな。\x02",
    )

    CloseMessageWindow()

    #C0600
    ChrTalk(
        0x102,
        (
            "#5P#0106Fそうね……\x01",
            "もうちょっと頑張ってほしいかも。\x02",
        )
    )

    CloseMessageWindow()

    #C0601
    ChrTalk(
        0x101,
        "#11P#0006Fな、なんとか挽回してみせるよ。\x02",
    )

    CloseMessageWindow()

    def lambda_C1D0():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_C1D0)

    def lambda_C1DD():
        OP_93(0x102, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_C1DD)

    def lambda_C1EA():
        OP_93(0x104, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_C1EA)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x104, 1)
    Jump("loc_C331")

    label("loc_C203")


    #C0602
    ChrTalk(
        0x103,
        (
            "#12P#0211F……勉強不足が\x01",
            "モロに出ている気がします。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_C241():
        TurnDirection(0x101, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_C241)
    Sleep(50)

    def lambda_C251():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_C251)

    def lambda_C25E():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_C25E)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x104, 1)

    #C0603
    ChrTalk(
        0x104,
        (
            "#6P#0306F確かになぁ。\x01",
            "この先心配になっちまうぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0604
    ChrTalk(
        0x102,
        (
            "#5P#0103Fそうね……\x01",
            "何とか挽回してもらわないと。\x02",
        )
    )

    CloseMessageWindow()

    #C0605
    ChrTalk(
        0x101,
        "#11P#0003Fめ、面目ない……\x02",
    )

    CloseMessageWindow()

    def lambda_C303():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_C303)

    def lambda_C310():
        OP_93(0x102, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_C310)

    def lambda_C31D():
        OP_93(0x104, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_C31D)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x104, 1)

    label("loc_C331")


    #C0606
    ChrTalk(
        0x8,
        (
            "#5Pふふ、泣いても笑っても残り５問よ。\x01",
            "せいぜい頑張って頂戴。\x02",
        )
    )

    CloseMessageWindow()

    #C0607
    ChrTalk(
        0x8,
        (
            "#5Pこれからはちょっと\x01",
            "問題を難しくしていくから、\x01",
            "そのつもりでね。\x02",
        )
    )

    CloseMessageWindow()

    #C0608
    ChrTalk(
        0x8,
        "#5P──それじゃ、第６問！\x02",
    )

    CloseMessageWindow()

    #C0609
    ChrTalk(
        0x8,
        (
            "#5Pその昔、このゼムリア大陸には\x01",
            "《大崩壊》という災厄が起こったというわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0610
    ChrTalk(
        0x8,
        (
            "#5Pこれによって文明を失った人々は\x01",
            "様々な勢力に分かれて、５００年もの間\x01",
            "果てしない争いを続けていたそうよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0611
    ChrTalk(
        0x8,
        (
            "#5Pその後、この《暗黒時代》と呼ばれる時代は\x01",
            "ある勢力によって終結を迎えたの。\x02",
        )
    )

    CloseMessageWindow()

    #C0612
    ChrTalk(
        0x8,
        (
            "#5P《暗黒時代》のゼムリア大陸に現れ、\x01",
            "新たな秩序をも形成した勢力……\x01",
            "分かるわよね？\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 16, -1, -1)
    SetChrName("")

    #A0613
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            "《暗黒時代》を終わらせた勢力の名は？",
            scpstr(0x18),
            scpstr(SCPSTR_CODE_ENTER),
        )
    )


    Menu(
        0,
        -1,
        150,
        0,
        (
            "【①七耀教会】\x01",        # 0
            "【②遊撃士協会】\x01",      # 1
            "【③釣公師団】\x01",        # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_C5EF"),
        (1, "loc_C7F6"),
        (2, "loc_CA41"),
        (SWITCH_DEFAULT, "loc_CC8C"),
    )


    label("loc_C5EF")


    #C0614
    ChrTalk(
        0x101,
        "#12P#0000F……七耀教会、ですね。\x02",
    )

    CloseMessageWindow()

    #C0615
    ChrTalk(
        0x8,
        "#5P…………………………\x02",
    )

    CloseMessageWindow()
    Sound(87, 0, 100, 0)

    #C0616
    ChrTalk(
        0x8,
        "#5Pピンポーン！！　正解！\x02",
    )

    CloseMessageWindow()

    #C0617
    ChrTalk(
        0x8,
        (
            "#5P七耀暦５００年頃、世に現れた七耀教会は、\x01",
            "民衆救済を掲げた教会の社会的活動を通じて\x01",
            "《空の女神》の教えを人々の間に広めたの。\x02",
        )
    )

    CloseMessageWindow()

    #C0618
    ChrTalk(
        0x8,
        (
            "#5Pその影響力は、《暗黒時代》を支配していた\x01",
            "貴族や騎士階級も無視できないものにまで\x01",
            "成長して、徐々に秩序を形成していったそうよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0619
    ChrTalk(
        0x8,
        (
            "#5P今では、七耀教会の崇める《空の女神》の教えは\x01",
            "このゼムリア大陸全土に広く浸透しているわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0620
    ChrTalk(
        0x101,
        "#12P#0004F（ＯＫ、いい調子だ。）\x02",
    )

    CloseMessageWindow()
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_CC8C")

    label("loc_C7F6")


    #C0621
    ChrTalk(
        0x101,
        "#12P#0000F……遊撃士協会、ですね。\x02",
    )

    CloseMessageWindow()

    #C0622
    ChrTalk(
        0x8,
        "#5P…………………………\x02",
    )

    CloseMessageWindow()
    Sound(3, 0, 100, 0)

    #C0623
    ChrTalk(
        0x8,
        "#5Pブー！！　は・ず・れ～！\x02",
    )

    CloseMessageWindow()

    #C0624
    ChrTalk(
        0x8,
        (
            "#5P正解は、七耀教会よ。\x01",
            "……もう、こんなの常識中の常識じゃないの！\x02",
        )
    )

    CloseMessageWindow()

    #C0625
    ChrTalk(
        0x8,
        (
            "#5P七耀暦５００年頃、世に現れた七耀教会は、\x01",
            "民衆救済を掲げた教会の社会的活動を通じて\x01",
            "《空の女神》の教えを人々の間に広めたの。\x02",
        )
    )

    CloseMessageWindow()

    #C0626
    ChrTalk(
        0x8,
        (
            "#5Pその影響力は、《暗黒時代》を支配していた\x01",
            "貴族や騎士階級も無視できないものにまで\x01",
            "成長して、徐々に秩序を形成していったそうよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0627
    ChrTalk(
        0x8,
        (
            "#5P今では、七耀教会の崇める《空の女神》の教えは\x01",
            "このゼムリア大陸全土に広く浸透しているわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0628
    ChrTalk(
        0x101,
        "#12P#0006F（深読みしすぎたか……）\x02",
    )

    CloseMessageWindow()
    Jump("loc_CC8C")

    label("loc_CA41")


    #C0629
    ChrTalk(
        0x101,
        "#12P#0000F……釣公師団、ですね。\x02",
    )

    CloseMessageWindow()

    #C0630
    ChrTalk(
        0x8,
        "#5P…………………………\x02",
    )

    CloseMessageWindow()
    Sound(3, 0, 100, 0)

    #C0631
    ChrTalk(
        0x8,
        "#5Pブー！！　は・ず・れ～！\x02",
    )

    CloseMessageWindow()

    #C0632
    ChrTalk(
        0x8,
        (
            "#5P正解は、七耀教会よ。\x01",
            "……ていうかそれ、ウチのお隣さんじゃないの！\x02",
        )
    )

    CloseMessageWindow()

    #C0633
    ChrTalk(
        0x8,
        (
            "#5P七耀暦５００年頃、世に現れた七耀教会は、\x01",
            "民衆救済を掲げた教会の社会的活動を通じて\x01",
            "《空の女神》の教えを人々の間に広めたの。\x02",
        )
    )

    CloseMessageWindow()

    #C0634
    ChrTalk(
        0x8,
        (
            "#5Pその影響力は、《暗黒時代》を支配していた\x01",
            "貴族や騎士階級も無視できないものにまで\x01",
            "成長して、徐々に秩序を形成していったそうよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0635
    ChrTalk(
        0x8,
        (
            "#5P今では、七耀教会の崇める《空の女神》の教えは\x01",
            "このゼムリア大陸全土に広く浸透しているわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0636
    ChrTalk(
        0x101,
        "#12P#0006F（深読みしすぎたか……）\x02",
    )

    CloseMessageWindow()
    Jump("loc_CC8C")

    label("loc_CC8C")


    #C0637
    ChrTalk(
        0x8,
        "#5P続いて──第７問！\x02",
    )

    CloseMessageWindow()

    #C0638
    ChrTalk(
        0x8,
        (
            "#5P七耀教会の総本山は、\x01",
            "《アルテリア法国》という国にあるわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0639
    ChrTalk(
        0x8,
        (
            "#5Pアルテリア法国は、\x01",
            "様々な行政機関によって\x01",
            "国家としての体制を整えているの。\x02",
        )
    )

    CloseMessageWindow()

    #C0640
    ChrTalk(
        0x8,
        (
            "#5Pその行政機関の中で、\x01",
            "七耀教会の祭儀全般を担当する機関が\x01",
            "何ていうか……知ってるかしら？\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 16, -1, -1)
    SetChrName("")

    #A0641
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            "七耀教会の祭儀全般を担当する\x01",
            "行政機関の名前は？",
            scpstr(0x18),
            scpstr(SCPSTR_CODE_ENTER),
        )
    )


    Menu(
        0,
        -1,
        150,
        0,
        (
            "【①僧兵庁】\x01",      # 0
            "【②典礼省】\x01",      # 1
            "【③封聖省】\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_CE4C"),
        (1, "loc_CFE2"),
        (2, "loc_D161"),
        (SWITCH_DEFAULT, "loc_D31A"),
    )


    label("loc_CE4C")


    #C0642
    ChrTalk(
        0x101,
        "#12P#0000F……僧兵庁、ですか？\x02",
    )

    CloseMessageWindow()

    #C0643
    ChrTalk(
        0x8,
        "#5P…………………………\x02",
    )

    CloseMessageWindow()
    Sound(3, 0, 100, 0)

    #C0644
    ChrTalk(
        0x8,
        "#5Pブッブ～！！　残念、はずれよ。\x02",
    )

    CloseMessageWindow()

    #C0645
    ChrTalk(
        0x8,
        (
            "#5P僧兵庁はアルテリア法国の防衛を\x01",
            "担当している機関ね。\x02",
        )
    )

    CloseMessageWindow()

    #C0646
    ChrTalk(
        0x8,
        "#5P正解は、典礼省よ。\x02",
    )

    CloseMessageWindow()

    #C0647
    ChrTalk(
        0x8,
        (
            "#5P各地にある教会や聖堂に勤める\x01",
            "司祭さんたちは、大体が\x01",
            "この機関に属する人達なの。\x02",
        )
    )

    CloseMessageWindow()

    #C0648
    ChrTalk(
        0x8,
        (
            "#5Pクロスベル市の北口にも\x01",
            "大聖堂があるから、\x01",
            "たまにはお祈りに行くことね。\x02",
        )
    )

    CloseMessageWindow()

    #C0649
    ChrTalk(
        0x101,
        "#12P#0006F（うう、難しいな……）\x02",
    )

    CloseMessageWindow()
    Jump("loc_D31A")

    label("loc_CFE2")


    #C0650
    ChrTalk(
        0x101,
        "#12P#0000F……典礼省、ですか？\x02",
    )

    CloseMessageWindow()

    #C0651
    ChrTalk(
        0x8,
        "#5P…………………………\x02",
    )

    CloseMessageWindow()
    Sound(87, 0, 100, 0)

    #C0652
    ChrTalk(
        0x8,
        "#5Pピンポーン！！　正解よ！\x02",
    )

    CloseMessageWindow()

    #C0653
    ChrTalk(
        0x8,
        (
            "#5P各地にある教会や聖堂に勤める\x01",
            "司祭さんたちは、大体が\x01",
            "この機関に属する人達なの。\x02",
        )
    )

    CloseMessageWindow()

    #C0654
    ChrTalk(
        0x8,
        (
            "#5Pクロスベル市の北口にも\x01",
            "大聖堂があるから、\x01",
            "たまにはお祈りに行くことね。\x02",
        )
    )

    CloseMessageWindow()

    #C0655
    ChrTalk(
        0x8,
        (
            "#5Pそこにいる司教様も、\x01",
            "確か典礼省の出身だったはずよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0656
    ChrTalk(
        0x101,
        "#12P#0004F（よし、いい感じだ。）\x02",
    )

    CloseMessageWindow()
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_D31A")

    label("loc_D161")


    #C0657
    ChrTalk(
        0x101,
        "#12P#0000F……封聖省、ですか？\x02",
    )

    CloseMessageWindow()

    #C0658
    ChrTalk(
        0x8,
        "#5P…………………………\x02",
    )

    CloseMessageWindow()
    Sound(3, 0, 100, 0)

    #C0659
    ChrTalk(
        0x8,
        "#5Pブッブ～！！　残念、はずれよ。\x02",
    )

    CloseMessageWindow()

    #C0660
    ChrTalk(
        0x8,
        (
            "#5P封聖省は、女神の秘蹟に関する\x01",
            "調査・管理をする機関らしいけど\x01",
            "詳細は公表されていないわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0661
    ChrTalk(
        0x8,
        "#5P正解は、典礼省よ。\x02",
    )

    CloseMessageWindow()

    #C0662
    ChrTalk(
        0x8,
        (
            "#5P各地にある教会や聖堂に勤める\x01",
            "司祭さんたちは、大体が\x01",
            "この機関に属する人達なの。\x02",
        )
    )

    CloseMessageWindow()

    #C0663
    ChrTalk(
        0x8,
        (
            "#5Pクロスベル市の北口にも\x01",
            "大聖堂があるから、\x01",
            "たまにはお祈りに行くことね。\x02",
        )
    )

    CloseMessageWindow()

    #C0664
    ChrTalk(
        0x101,
        "#12P#0006F（うう、難しいな……）\x02",
    )

    CloseMessageWindow()
    Jump("loc_D31A")

    label("loc_D31A")


    #C0665
    ChrTalk(
        0x8,
        (
            "#5P終わりが近づいてきたわね。\x01",
            "──第８問！\x02",
        )
    )

    CloseMessageWindow()

    #C0666
    ChrTalk(
        0x8,
        (
            "#5P遊撃士協会は大陸各地に\x01",
            "支部を持っているわ。\x01",
            "その中でも……\x02",
        )
    )

    CloseMessageWindow()

    #C0667
    ChrTalk(
        0x8,
        (
            "#5P遊撃士協会の本部があるのは\x01",
            "どこだったかしら？\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 16, -1, -1)
    SetChrName("")

    #A0668
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            "遊撃士協会の本部があるのは？",
            scpstr(0x18),
            scpstr(SCPSTR_CODE_ENTER),
        )
    )


    Menu(
        0,
        -1,
        150,
        0,
        (
            "【①クロスベル自治州】\x01",      # 0
            "【②レマン自治州】\x01",          # 1
            "【③オレド自治州】\x01",          # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_D477"),
        (1, "loc_D601"),
        (2, "loc_D749"),
        (SWITCH_DEFAULT, "loc_D8AF"),
    )


    label("loc_D477")


    #C0669
    ChrTalk(
        0x101,
        "#12P#0000F……クロスベル自治州です。\x02",
    )

    CloseMessageWindow()

    #C0670
    ChrTalk(
        0x8,
        "#5P…………………………\x02",
    )

    CloseMessageWindow()
    Sound(3, 0, 100, 0)

    #C0671
    ChrTalk(
        0x8,
        "#5Pブ～ッ！！　はずれよ。\x02",
    )

    CloseMessageWindow()

    #C0672
    ChrTalk(
        0x8,
        "#5P正解は、レマン自治州。\x02",
    )

    CloseMessageWindow()

    #C0673
    ChrTalk(
        0x8,
        (
            "#5P遊撃士協会の出資者である\x01",
            "エプスタイン財団の本部も\x01",
            "ここに存在するわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0674
    ChrTalk(
        0x8,
        (
            "#5P重要な事件が起こったときには、\x01",
            "本部から動員命令が\x01",
            "下されることもあるわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0675
    ChrTalk(
        0x101,
        (
            "#12P#0006F（そ、そりゃそうか。\x01",
            "  クロスベルでそんなの、\x01",
            "  見たこと無かったしな……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D8AF")

    label("loc_D601")


    #C0676
    ChrTalk(
        0x101,
        (
            "#12P#0000F……それはもちろん、\x01",
            "レマン自治州ですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0677
    ChrTalk(
        0x8,
        "#5P…………………………\x02",
    )

    CloseMessageWindow()
    Sound(87, 0, 100, 0)

    #C0678
    ChrTalk(
        0x8,
        "#5Pピンポ～ン！！　正解よ。\x02",
    )

    CloseMessageWindow()

    #C0679
    ChrTalk(
        0x8,
        (
            "#5P遊撃士協会の出資者である\x01",
            "エプスタイン財団の本部も\x01",
            "ここに存在するわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0680
    ChrTalk(
        0x8,
        (
            "#5P重要な事件が起こったときには、\x01",
            "本部から動員命令が\x01",
            "下されることもあるわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0681
    ChrTalk(
        0x101,
        "#12P#0004F（ほっ……）\x02",
    )

    CloseMessageWindow()
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_D8AF")

    label("loc_D749")


    #C0682
    ChrTalk(
        0x101,
        "#12P#0000F……オレド自治州、でしたっけ？\x02",
    )

    CloseMessageWindow()

    #C0683
    ChrTalk(
        0x8,
        "#5P…………………………\x02",
    )

    CloseMessageWindow()
    Sound(3, 0, 100, 0)

    #C0684
    ChrTalk(
        0x8,
        "#5Pブ～ッ！！　はずれよ。\x02",
    )

    CloseMessageWindow()

    #C0685
    ChrTalk(
        0x8,
        "#5P正解は、レマン自治州。\x02",
    )

    CloseMessageWindow()

    #C0686
    ChrTalk(
        0x8,
        (
            "#5P遊撃士協会の出資者である\x01",
            "エプスタイン財団の本部も\x01",
            "ここに存在するわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0687
    ChrTalk(
        0x8,
        (
            "#5P重要な事件が起こったときには、\x01",
            "本部から動員命令が\x01",
            "下されることもあるわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0688
    ChrTalk(
        0x101,
        "#12P#0006F（うーん、間違えてしまったか……）\x02",
    )

    CloseMessageWindow()
    Jump("loc_D8AF")

    label("loc_D8AF")


    #C0689
    ChrTalk(
        0x8,
        "#5P──第９問！\x02",
    )

    CloseMessageWindow()

    #C0690
    ChrTalk(
        0x8,
        (
            "#5Pエレボニア帝国では\x01",
            "１人の「怪盗」が\x01",
            "その名を馳せているわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0691
    ChrTalk(
        0x8,
        (
            "#5P言葉遊びに富んだ犯行予告カード、\x01",
            "盗んだ美術品を換金してばらまく性質、\x01",
            "そして正体を隠す神秘的な仮面……\x02",
        )
    )

    CloseMessageWindow()

    #C0692
    ChrTalk(
        0x8,
        (
            "#5P一部ではヒーロー扱いまで\x01",
            "される始末だったそうよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0693
    ChrTalk(
        0x8,
        (
            "#5Pさて、その怪盗に\x01",
            "いつしか付いたコードネーム……\x01",
            "あなたに分かる？\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 16, -1, -1)
    SetChrName("")

    #A0694
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            "数年前帝国に現れた\x01",
            "『怪盗』のコードネームは？",
            scpstr(0x18),
            scpstr(SCPSTR_CODE_ENTER),
        )
    )


    Menu(
        0,
        -1,
        150,
        0,
        (
            "【①怪盗Ａ】\x01",      # 0
            "【②怪盗Ｂ】\x01",      # 1
            "【③怪盗Ｃ】\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_DAA8"),
        (1, "loc_DCC7"),
        (2, "loc_DED1"),
        (SWITCH_DEFAULT, "loc_E0C9"),
    )


    label("loc_DAA8")


    #C0695
    ChrTalk(
        0x101,
        "#12P#0000F……怪盗Ａ……だったような。\x02",
    )

    CloseMessageWindow()

    #C0696
    ChrTalk(
        0x8,
        "#5P…………………………\x02",
    )

    CloseMessageWindow()
    Sound(3, 0, 100, 0)

    #C0697
    ChrTalk(
        0x8,
        (
            "#5Pブッブッブー！！　はっずれ～！\x01",
            "警察らしく少年Ａみたいな呼び名ねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0698
    ChrTalk(
        0x8,
        "#5P正解は怪盗Ｂ――\x02",
    )

    CloseMessageWindow()

    #C0699
    ChrTalk(
        0x8,
        (
            "#5P帝国だけでなく、\x01",
            "大陸各地にその名を馳せる\x01",
            "正体不明、神出鬼没の大泥棒よ。\x02",
        )
    )

    CloseMessageWindow()

    #C0700
    ChrTalk(
        0x8,
        (
            "#5P彼の盗むものはそれこそ千差万別でね。\x01",
            "美術館の絵画から、すごいものでは\x01",
            "戦車なんてものの被害もあるわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0701
    ChrTalk(
        0x8,
        (
            "#5P最近ではリベールでも\x01",
            "その被害が報告されたらしいわ。\x01",
            "今後、関わる事があるかもしれないわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0702
    ChrTalk(
        0x101,
        (
            "#12P#0006F（う～ん……他国の事件までは\x01",
            "  ノーマークだったな。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E0C9")

    label("loc_DCC7")


    #C0703
    ChrTalk(
        0x101,
        "#12P#0000F……怪盗Ｂ……ですね？\x02",
    )

    CloseMessageWindow()

    #C0704
    ChrTalk(
        0x8,
        "#5P…………………………\x02",
    )

    CloseMessageWindow()
    Sound(87, 0, 100, 0)

    #C0705
    ChrTalk(
        0x8,
        (
            "#5Pピンポーン！！\x01",
            "よく他国の事件まで知ってたわねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0706
    ChrTalk(
        0x8,
        (
            "#5P怪盗Ｂ……帝国だけでなく、\x01",
            "大陸各地にその名を馳せる\x01",
            "正体不明、神出鬼没の大泥棒よ。\x02",
        )
    )

    CloseMessageWindow()

    #C0707
    ChrTalk(
        0x8,
        (
            "#5P彼の盗むものはそれこそ千差万別でね。\x01",
            "美術館の絵画から、すごいものでは\x01",
            "戦車なんてものの被害もあるわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0708
    ChrTalk(
        0x8,
        (
            "#5P最近ではリベールでも\x01",
            "その被害が報告されたらしいわ。\x01",
            "今後、関わる事があるかもしれないわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0709
    ChrTalk(
        0x101,
        (
            "#12P#0006F（噂に聞いたくらいの人物だけど……\x01",
            "  正直勘弁してほしいな。）\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_E0C9")

    label("loc_DED1")


    #C0710
    ChrTalk(
        0x101,
        "#12P#0000F……怪盗Ｃ……だったっけ？\x02",
    )

    CloseMessageWindow()

    #C0711
    ChrTalk(
        0x8,
        "#5P…………………………\x02",
    )

    CloseMessageWindow()
    Sound(3, 0, 100, 0)

    #C0712
    ChrTalk(
        0x8,
        "#5Pブッブッブー！！　はっずれ～！\x02",
    )

    CloseMessageWindow()

    #C0713
    ChrTalk(
        0x8,
        "#5P正解は怪盗Ｂ――\x02",
    )

    CloseMessageWindow()

    #C0714
    ChrTalk(
        0x8,
        (
            "#5P帝国だけでなく、\x01",
            "大陸各地にその名を馳せる\x01",
            "正体不明、神出鬼没の大泥棒よ。\x02",
        )
    )

    CloseMessageWindow()

    #C0715
    ChrTalk(
        0x8,
        (
            "#5P彼の盗むものはそれこそ千差万別でね。\x01",
            "美術館の絵画から、すごいものでは\x01",
            "戦車なんてものの被害もあるわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0716
    ChrTalk(
        0x8,
        (
            "#5P最近ではリベールでも\x01",
            "その被害が報告されたらしいわ。\x01",
            "今後、関わる事があるかもしれないわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0717
    ChrTalk(
        0x101,
        (
            "#12P#0006F（う～ん……他国の事件までは\x01",
            "  ノーマークだったな。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E0C9")

    label("loc_E0C9")


    #C0718
    ChrTalk(
        0x8,
        (
            "#5P──第１０問！\x01",
            "さぁ、いよいよ最終問題ね。\x02",
        )
    )

    CloseMessageWindow()

    #C0719
    ChrTalk(
        0x8,
        (
            "#5P帝国と共和国の対立は、\x01",
            "このクロスベルの所有権を巡って\x01",
            "長い間続けられてきたわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0720
    ChrTalk(
        0x8,
        (
            "#5P今まで何度も紛争が起こって、\x01",
            "罪のない人々も巻き込まれてきた。\x02",
        )
    )

    CloseMessageWindow()

    #C0721
    ChrTalk(
        0x8,
        (
            "#5Pそんな事態を重く見た\x01",
            "リベール王国の女王・アリシアⅡ世は\x01",
            "ある条約を提案したの。\x02",
        )
    )

    CloseMessageWindow()

    #C0722
    ChrTalk(
        0x8,
        (
            "#5Pそれは一昨年、\x01",
            "リベール、帝国、共和国の３国で\x01",
            "締結されたわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0723
    ChrTalk(
        0x8,
        (
            "#5Pその重要な条約の名称……\x01",
            "クロスベルの人間なら分かって当然よね？\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 16, -1, -1)
    SetChrName("")

    #A0724
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            "リベール、帝国、共和国の３国で\x01",
            "締結された条約の名称は？",
            scpstr(0x18),
            scpstr(SCPSTR_CODE_ENTER),
        )
    )


    Menu(
        0,
        -1,
        150,
        0,
        (
            "【①非戦条約】\x01",      # 0
            "【②不戦条約】\x01",      # 1
            "【③未戦条約】\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_E33B"),
        (1, "loc_E5DD"),
        (2, "loc_E879"),
        (SWITCH_DEFAULT, "loc_EB2C"),
    )


    label("loc_E33B")


    #C0725
    ChrTalk(
        0x101,
        "#12P#0000F……《非戦条約》でしたよね。\x02",
    )

    CloseMessageWindow()

    #C0726
    ChrTalk(
        0x8,
        "#5P…………………………\x02",
    )

    CloseMessageWindow()
    Sound(3, 0, 100, 0)

    #C0727
    ChrTalk(
        0x8,
        (
            "#5Pブー！！！！　不正解！\x01",
            "もう、しっかりして頂戴。\x02",
        )
    )

    CloseMessageWindow()

    #C0728
    ChrTalk(
        0x8,
        "#5P正しくは、《不戦条約》ね。\x02",
    )

    CloseMessageWindow()

    #C0729
    ChrTalk(
        0x8,
        (
            "#5Pこれは、３国間での対立は\x01",
            "武力ではなく対話で解決するべき\x01",
            "という条約なの。\x02",
        )
    )

    CloseMessageWindow()

    #C0730
    ChrTalk(
        0x8,
        (
            "#5Pこの条約が締結される前まで、\x01",
            "クロスベル自治州は\x01",
            "極度の緊張状態にさらされていたわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0731
    ChrTalk(
        0x8,
        (
            "#5P詳細は省くけど、両大国の機甲師団が\x01",
            "国境付近で大規模な軍事演習を繰り返したの。\x02",
        )
    )

    CloseMessageWindow()

    #C0732
    ChrTalk(
        0x8,
        (
            "#5P一歩間違えればとんでもない\x01",
            "大惨事になってもおかしくない……\x02",
        )
    )

    CloseMessageWindow()

    #C0733
    ChrTalk(
        0x8,
        (
            "#5Pそんな状況を打開するために、\x01",
            "アリシア女王はこの条約を提唱したってわけ。\x02",
        )
    )

    CloseMessageWindow()

    #C0734
    ChrTalk(
        0x8,
        "#5Pフフ、リベールに足を向けて寝られないわね。\x02",
    )

    CloseMessageWindow()

    #C0735
    ChrTalk(
        0x101,
        "#12P#0006F（ううん、まずったな……）\x02",
    )

    CloseMessageWindow()
    Jump("loc_EB2C")

    label("loc_E5DD")


    #C0736
    ChrTalk(
        0x101,
        "#12P#0000F……不戦条約、ですね。\x02",
    )

    CloseMessageWindow()

    #C0737
    ChrTalk(
        0x8,
        "#5P…………………………\x02",
    )

    CloseMessageWindow()
    Sound(87, 0, 100, 0)

    #C0738
    ChrTalk(
        0x8,
        (
            "#5Pピンポーン！！　大正解！\x01",
            "流石にこれくらいは\x01",
            "知っていてもらわないとね。\x02",
        )
    )

    CloseMessageWindow()

    #C0739
    ChrTalk(
        0x8,
        (
            "#5Pこれは、３国間での対立は\x01",
            "武力ではなく対話で解決するべき\x01",
            "という条約なの。\x02",
        )
    )

    CloseMessageWindow()

    #C0740
    ChrTalk(
        0x8,
        (
            "#5Pこの条約が締結される前まで、\x01",
            "クロスベル自治州は\x01",
            "極度の緊張状態にさらされていたわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0741
    ChrTalk(
        0x8,
        (
            "#5P詳細は省くけど、両大国の機甲師団が\x01",
            "国境付近で大規模な軍事演習を繰り返したの。\x02",
        )
    )

    CloseMessageWindow()

    #C0742
    ChrTalk(
        0x8,
        (
            "#5P一歩間違えればとんでもない\x01",
            "大惨事になってもおかしくない……\x02",
        )
    )

    CloseMessageWindow()

    #C0743
    ChrTalk(
        0x8,
        (
            "#5Pそんな状況を打開するために、\x01",
            "アリシア女王はこの条約を提唱したってわけ。\x02",
        )
    )

    CloseMessageWindow()

    #C0744
    ChrTalk(
        0x8,
        "#5Pフフ、リベールに足を向けて寝られないわね。\x02",
    )

    CloseMessageWindow()

    #C0745
    ChrTalk(
        0x101,
        "#12P#0004F（よし、バッチリだったな。）\x02",
    )

    CloseMessageWindow()
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_EB2C")

    label("loc_E879")


    #C0746
    ChrTalk(
        0x101,
        "#12P#0000F……《未戦条約》でしたよね。\x02",
    )

    CloseMessageWindow()

    #C0747
    ChrTalk(
        0x8,
        "#5P…………………………\x02",
    )

    CloseMessageWindow()
    Sound(3, 0, 100, 0)

    #C0748
    ChrTalk(
        0x8,
        (
            "#5Pブー！！！！　不正解！\x01",
            "もう、しっかりして頂戴。\x02",
        )
    )

    CloseMessageWindow()

    #C0749
    ChrTalk(
        0x8,
        "#5P正しくは、《不戦条約》ね。\x02",
    )

    CloseMessageWindow()

    #C0750
    ChrTalk(
        0x8,
        (
            "#5Pこれは、３国間での対立は\x01",
            "武力ではなく対話で解決するべき\x01",
            "という条約なの。\x02",
        )
    )

    CloseMessageWindow()

    #C0751
    ChrTalk(
        0x8,
        (
            "#5Pこの条約が締結される前まで、\x01",
            "クロスベル自治州は\x01",
            "極度の緊張状態にさらされていたわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0752
    ChrTalk(
        0x8,
        (
            "#5P詳細は省くけど、両大国の機甲師団が\x01",
            "国境付近で大規模な軍事演習を繰り返したの。\x02",
        )
    )

    CloseMessageWindow()

    #C0753
    ChrTalk(
        0x8,
        (
            "#5P一歩間違えればとんでもない\x01",
            "大惨事になってもおかしくない……\x02",
        )
    )

    CloseMessageWindow()

    #C0754
    ChrTalk(
        0x8,
        (
            "#5Pそんな状況を打開するために、\x01",
            "アリシア女王はこの条約を提唱したってわけ。\x02",
        )
    )

    CloseMessageWindow()

    #C0755
    ChrTalk(
        0x8,
        "#5Pフフ、リベールに足を向けて寝られないわね。\x02",
    )

    CloseMessageWindow()

    #C0756
    ChrTalk(
        0x101,
        (
            "#12P#0006F（うーん、\x01",
            "  内容は分かってたんだけどな。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EB2C")

    label("loc_EB2C")


    #C0757
    ChrTalk(
        0x8,
        "#5P──以上、これにてテストは終了よ。\x02",
    )

    CloseMessageWindow()

    #C0758
    ChrTalk(
        0x8,
        "#5Pふふ、お疲れ様。\x02",
    )

    CloseMessageWindow()

    #C0759
    ChrTalk(
        0x101,
        "#12P#0006F（はぁ、ようやく終わったか……）\x02",
    )

    CloseMessageWindow()
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Return()

    # Function_25_9726 end

    def Function_26_EBB1(): pass

    label("Function_26_EBB1")

    OP_68(1000, 1300, 10500, 0)
    MoveCamera(37, 26, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(21630, 0)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7102", 0)
    FadeToBright(1000, 0)
    OP_0D()

    #C0760
    ChrTalk(
        0x8,
        "#5P──さて……テストの結果だけど……\x02",
    )

    CloseMessageWindow()

    #C0761
    ChrTalk(
        0x101,
        "#11P#0001F（ごくり……）\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EFAB")

    #C0762
    ChrTalk(
        0x8,
        (
            "#5P全問正解……\x01",
            "準遊撃士並みの知識は\x01",
            "充分に持ち合わせてる。\x02",
        )
    )

    CloseMessageWindow()

    #C0763
    ChrTalk(
        0x8,
        (
            "#5Pふふ、これなら少しは\x01",
            "期待できそうじゃない。\x02",
        )
    )

    CloseMessageWindow()

    #C0764
    ChrTalk(
        0x101,
        (
            "#11P#0000Fありがとうございます。\x01",
            "（意外と素直に褒めてくれたな……）\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 500)

    #C0765
    ChrTalk(
        0x104,
        "#12P#0300Fなんつか、ホッと一安心だな。\x02",
    )

    CloseMessageWindow()

    def lambda_ED3F():
        TurnDirection(0x101, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_ED3F)
    Sleep(50)

    def lambda_ED4F():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_ED4F)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)

    #C0766
    ChrTalk(
        0x102,
        (
            "#12P#0100Fうん、専門外のことまで\x01",
            "よく答えてくれたわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0767
    ChrTalk(
        0x103,
        (
            "#12P#0200Fデータベースの補完も\x01",
            "手伝って欲しいくらいです。\x02",
        )
    )

    CloseMessageWindow()

    #C0768
    ChrTalk(
        0x101,
        "#11P#0012Fはは、それは言い過ぎだって。\x02",
    )

    CloseMessageWindow()

    def lambda_EE0A():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_EE0A)

    def lambda_EE17():
        OP_93(0x102, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_EE17)

    def lambda_EE24():
        OP_93(0x104, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_EE24)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x104, 1)

    #C0769
    ChrTalk(
        0x8,
        (
            "#5Pそれじゃ……\x01",
            "全問正解のごほうびでも\x01",
            "あげようかしらね。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0770
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x7F),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を受け取った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x7F, 1)

    #C0771
    ChrTalk(
        0x101,
        (
            "#11P#0005Fわ……\x01",
            "い、いいんですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0772
    ChrTalk(
        0x8,
        (
            "#5Pうん、正直ここまでやるとは\x01",
            "思わなかったし、\x01",
            "侮っていたお詫び込みってことで。\x02",
        )
    )

    CloseMessageWindow()

    #C0773
    ChrTalk(
        0x8,
        "#5P遠慮しないで貰っちゃって。\x02",
    )

    CloseMessageWindow()

    #C0774
    ChrTalk(
        0x101,
        (
            "#11P#0000Fそれじゃあ……\x01",
            "ありがとうございます。\x02",
        )
    )

    CloseMessageWindow()
    OP_2C(0x4, 0x2)
    OP_29(0x4, 0x1, 0x1)
    Jump("loc_F39F")

    label("loc_EFAB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_F1C0")

    #C0775
    ChrTalk(
        0x8,
        (
            "#5Pうーん……\x01",
            "なんていうか、無難に\x01",
            "まとまっちゃったわねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0776
    ChrTalk(
        0x8,
        (
            "#5Pどうせなら全問正解して\x01",
            "ほしかったかな。\x02",
        )
    )

    CloseMessageWindow()

    #C0777
    ChrTalk(
        0x8,
        "#5Pま、一応合格点ってとこかしら。\x02",
    )

    CloseMessageWindow()

    #C0778
    ChrTalk(
        0x101,
        (
            "#11P#0003Fうーん、確かにちょっと\x01",
            "知識不足だったな……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 500)

    #C0779
    ChrTalk(
        0x104,
        "#12P#0300Fまぁ、よくやった方じゃねぇか？\x02",
    )

    CloseMessageWindow()

    def lambda_F0C7():
        TurnDirection(0x101, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_F0C7)
    Sleep(50)

    def lambda_F0D7():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_F0D7)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)

    #C0780
    ChrTalk(
        0x102,
        (
            "#6P#0104Fうん、そうね。\x02\x03",

            "#0100F足りない知識はこれから補えば\x01",
            "いいと思うし……\x02",
        )
    )

    CloseMessageWindow()

    #C0781
    ChrTalk(
        0x103,
        "#12P#0200F……がんばです。\x02",
    )

    CloseMessageWindow()

    #C0782
    ChrTalk(
        0x101,
        "#11P#0000Fはは……ありがとう。\x02",
    )

    CloseMessageWindow()

    def lambda_F182():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_F182)

    def lambda_F18F():
        OP_93(0x102, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_F18F)

    def lambda_F19C():
        OP_93(0x104, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_F19C)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x104, 1)
    OP_2C(0x4, 0x1)
    OP_29(0x4, 0x1, 0x2)
    Jump("loc_F39F")

    label("loc_F1C0")


    #C0783
    ChrTalk(
        0x8,
        (
            "#5Pうーん……\x01",
            "ちょっと残念な出来ね。\x02",
        )
    )

    CloseMessageWindow()

    #C0784
    ChrTalk(
        0x8,
        (
            "#5Pまだまだ、勉強不足は\x01",
            "否めないんじゃないかしら？\x02",
        )
    )

    CloseMessageWindow()

    #C0785
    ChrTalk(
        0x101,
        "#11P#0006F……お恥ずかしい限りです。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 500)

    #C0786
    ChrTalk(
        0x104,
        (
            "#12P#0300Fま、気にすんな。\x01",
            "これくらいの方が\x01",
            "逆に大物っぽくていいじゃねぇか。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_F2AA():
        TurnDirection(0x101, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_F2AA)
    Sleep(50)

    def lambda_F2BA():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_F2BA)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)

    #C0787
    ChrTalk(
        0x102,
        (
            "#6P#0106Fこれで気にしなかったら\x01",
            "流石に大物過ぎると思うけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0788
    ChrTalk(
        0x103,
        "#12P#0211Fちょっと先が思いやられますね。\x02",
    )

    CloseMessageWindow()

    #C0789
    ChrTalk(
        0x101,
        "#11P#0006Fが、がんばらせてもらうよ。\x02",
    )

    CloseMessageWindow()

    def lambda_F36B():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_F36B)

    def lambda_F378():
        OP_93(0x102, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_F378)

    def lambda_F385():
        OP_93(0x104, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_F385)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x104, 1)
    OP_29(0x4, 0x1, 0x3)

    label("loc_F39F")


    #C0790
    ChrTalk(
        0x8,
        (
            "#5Pさ、ともかくこれで\x01",
            "私のテストは終わりよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0791
    ChrTalk(
        0x8,
        (
            "#5Pまぁ、私たちの邪魔に\x01",
            "ならないくらいには\x01",
            "成長してくれると助かるわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0792
    ChrTalk(
        0x101,
        "#11P#0000Fええ、お互い頑張りましょう。\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0793
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "クエスト【ミシェルの挑戦状】\x07\x00",
            "を達成した！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_29(0x4, 0x4, 0x10)
    Return()

    # Function_26_EBB1 end

    def Function_27_F4AF(): pass

    label("Function_27_F4AF")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch09102.itc", 0x1E)
    OP_68(-6000, 1100, 48100, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(420, 0)
    SetCameraDistance(23000, 0)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    OP_4B(0x8, 0xFF)
    SetChrPos(0x8, -6000, 100, 47100, 0)
    SetChrChipByIndex(0x9, 0x7)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    OP_4B(0x9, 0xFF)
    SetChrPos(0x9, -6000, 100, 49200, 180)
    SetChrFlags(0xF, 0x80)
    SetChrBattleFlags(0xF, 0x8000)
    SetChrFlags(0x11, 0x80)
    SetChrBattleFlags(0x11, 0x8000)
    SetChrFlags(0x12, 0x80)
    SetChrBattleFlags(0x12, 0x8000)
    SetChrFlags(0x13, 0x80)
    SetChrBattleFlags(0x13, 0x8000)
    SetMapObjFrame(0xFF, "on_off", 0x0, 0x1)
    SetMapObjFrame(0xFF, "shadow_onoff", 0x0, 0x1)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu00800.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu00900.itp")
    CreatePortrait(2, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis152.itp")
    Sleep(1000)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("男性の声")

    #A0794
    AnonymousTalk(
        0xFF,
        (
            "──お疲れさま。\x01",
            "今月も大変だったわねぇ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    PlayBGM("ed7111", 0)
    SetCameraDistance(22000, 1500)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x10)

    #C0795
    ChrTalk(
        0x9,
        (
            "#5P#1404Fなに、いつもの事だ。\x02\x03",

            "#1400Fそれよりも……\x01",
            "送金の方はよろしく頼む。\x02",
        )
    )

    CloseMessageWindow()

    #C0796
    ChrTalk(
        0x8,
        (
            "#2Pわかったわ。\x01",
            "ＩＢＣ経由でいいのね？\x02",
        )
    )

    CloseMessageWindow()

    #C0797
    ChrTalk(
        0x8,
        (
            "#2Pそれにしても……\x01",
            "依頼を回しているアタシが\x01",
            "こう言うのもなんだけどさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0798
    ChrTalk(
        0x8,
        (
            "#2Pアナタ、もうちょっと仕事を\x01",
            "減らした方がいいんじゃない？\x02",
        )
    )

    CloseMessageWindow()

    #C0799
    ChrTalk(
        0x8,
        (
            "#2Pシズクちゃんだって\x01",
            "寂しがってるでしょうに……\x02",
        )
    )

    CloseMessageWindow()

    #C0800
    ChrTalk(
        0x9,
        "#5P#1403F……………………………………\x02",
    )

    CloseMessageWindow()

    #C0801
    ChrTalk(
        0x8,
        (
            "#2Pゴメン、これは\x01",
            "言わない約束だったわね。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0802
    ChrTalk(
        0x8,
        (
            "#2Pそれはそうと……\x01",
            "レマン総本部からの連絡が\x01",
            "また来ていたわよ？\x02",
        )
    )

    CloseMessageWindow()

    #C0803
    ChrTalk(
        0x8,
        (
            "#2P──いい加減、\x01",
            "受けてくれる気はないのかって。\x02",
        )
    )

    CloseMessageWindow()

    #C0804
    ChrTalk(
        0x9,
        (
            "#5P#1405Fまたそれか……\x02\x03",

            "#1403Fその件に関しては\x01",
            "何度も断っているはずだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0805
    ChrTalk(
        0x8,
        (
            "#2Pまあ、総本部としては\x01",
            "カシウス・ブライトの代わりを\x01",
            "揃えておきたいんでしょうね。\x02",
        )
    )

    CloseMessageWindow()

    #C0806
    ChrTalk(
        0x8,
        "#2Pあなた、彼の弟弟子#6Rおとうとでし#なんでしょ？\x02",
    )

    CloseMessageWindow()

    #C0807
    ChrTalk(
        0x8,
        (
            "#2P実績だって引けを取らないんだし、\x01",
            "いいかげん観念したらどうなの？\x02",
        )
    )

    CloseMessageWindow()

    #C0808
    ChrTalk(
        0x9,
        (
            "#5P#1404F残念だが……\x01",
            "彼と俺では役者が違いすぎる。\x02\x03",

            "実績にしたところで\x01",
            "彼のように国家的な問題を\x01",
            "解決したわけではないからな。\x02\x03",

            "#1402F正直、身に余る話さ。\x02",
        )
    )

    CloseMessageWindow()

    #C0809
    ChrTalk(
        0x8,
        (
            "#2P国家的な問題っていうなら\x01",
            "レミフェリアの件があるじゃない。\x02",
        )
    )

    CloseMessageWindow()

    #C0810
    ChrTalk(
        0x8,
        (
            "#2P大公閣下から勲章も貰ったんだし、\x01",
            "実績としては十分すぎると思うけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0811
    ChrTalk(
        0x9,
        (
            "#5P#1403F……あの件は本当の意味で\x01",
            "解決できたわけではないからな。\x02\x03",

            "#1401F公国での芽は潰したとはいえ、\x01",
            "一部の黒幕は取り逃がしたままだ。\x02\x03",

            "本来なら勲章など\x01",
            "辞退したかったんだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0812
    ChrTalk(
        0x8,
        (
            "#2Pまったくもう……\x01",
            "生真面目すぎるんだから。\x02",
        )
    )

    CloseMessageWindow()

    #C0813
    ChrTalk(
        0x8,
        (
            "#2Pせめて昇格でもすれば\x01",
            "逆に少しは落ち着くんじゃない？\x02",
        )
    )

    CloseMessageWindow()

    #C0814
    ChrTalk(
        0x8,
        (
            "#2P今月だけでも百件以上……\x01",
            "尋常じゃないわよ、この仕事量は。\x02",
        )
    )

    CloseMessageWindow()

    #C0815
    ChrTalk(
        0x9,
        (
            "#5P#1404F無理をしているつもりはないさ。\x02\x03",

            "#1402F列車と飛行船の便数も増えて\x01",
            "自治州外への出張も楽になった。\x02\x03",

            "頼もしい助っ人たちも来ることだし\x01",
            "今後は一息つけるだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0816
    ChrTalk(
        0x8,
        "#2Pあの子たちか……\x02",
    )

    CloseMessageWindow()

    #C0817
    ChrTalk(
        0x8,
        (
            "#2Pまあ、確かに\x01",
            "期待の大型新人ではあるわね。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 2)), scpexpr(EXPR_END)), "loc_FD9C")

    #C0818
    ChrTalk(
        0x8,
        (
            "#2P少なくとも、\x01",
            "あの支援課の坊やたちよりは\x01",
            "何倍も頼りになりそうだわ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FDE9")

    label("loc_FD9C")


    #C0819
    ChrTalk(
        0x8,
        (
            "#2P少なくとも、\x01",
            "あの警察の支援課とやらよりは\x01",
            "何倍も頼りになりそうだわ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FDE9")

    Sleep(150)
    OP_A7(0xB, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xB, 0x4)
    SetChrFlags(0xB, 0x40)
    OP_4B(0xB, 0xFF)
    OP_A7(0xD, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xD, 0x4)
    SetChrFlags(0xD, 0x40)
    OP_4B(0xD, 0xFF)
    OP_49()
    OP_90(0xB, 0, -500, 47000, 0)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    OP_90(0xD, 0, -500, 47000, 0)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    Sleep(50)
    #Sound(1700, 255, 85, 0)    #voice#Estelle

    #N0820
    NpcTalk(
        0xB,
        "娘の声",
        "#12A#1P#2Sごめんくださーい！\x02",
    )
    #Auto

    Sleep(800)
    OP_63(0x8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    SetChrSubChip(0x8, 0x2)
    Sleep(50)
    SetChrSubChip(0x9, 0x1)
    Sleep(200)

    #C0821
    ChrTalk(
        0x8,
        "#6Pあら、さっそく来たみたいね。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    SetChrPos(0x8, -4900, 0, 46370, 90)
    Sound(820, 0, 100, 0)
    OP_0D()
    Sleep(300)
    OP_68(-2150, 1100, 49550, 2500)

    def lambda_FF33():
        OP_95(0xFE, -2000, 0, 49500, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_FF33)
    WaitChrThread(0x8, 1)

    def lambda_FF51():
        OP_95(0xFE, -2000, 0, 49500, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_FF51)
    WaitChrThread(0x8, 1)
    OP_93(0x8, 0x87, 0x1F4)

    #C0822
    ChrTalk(
        0x8,
        "#5Pこっちよ、上がってきて！\x02",
    )

    CloseMessageWindow()

    #N0823
    NpcTalk(
        0xB,
        "娘の声",
        "#1P#2Sあっ、２階？\x02",
    )

    CloseMessageWindow()
    Sleep(150)
    #Sound(1774, 255, 90, 0)    #voice#Joshua

    #N0824
    NpcTalk(
        0xD,
        "青年の声",
        "#11P#2S失礼します。\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x8, 3, 0, 28)
    Sleep(1000)
    OP_68(-3310, 900, 49440, 3000)
    MoveCamera(40, 19, 0, 3000)
    SetCameraDistance(21500, 3000)
    BeginChrThread(0xB, 3, 0, 29)
    Sleep(700)
    BeginChrThread(0xD, 3, 0, 30)
    Sleep(500)
    WaitChrThread(0x8, 3)
    Sleep(500)

    #N0825
    NpcTalk(
        0xB,
        "ツインテールの娘",
        "#10A#0809F#5Pこんにちは～、ミシェルさん──\x02",
    )
    #Auto

    WaitChrThread(0xB, 3)
    OP_6F(0x79)
    OP_63(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #N0826
    NpcTalk(
        0xB,
        "ツインテールの娘",
        "#0805F#11Pって、アリオスさん！？\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0xD, 3)

    #N0827
    NpcTalk(
        0xD,
        "黒髪の青年",
        (
            "#11P#0902Fよかった。\x01",
            "丁度いらっしゃったんですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0828
    ChrTalk(
        0x9,
        (
            "#1404Fフフ、まあ偶然だがな。\x02\x03",

            "#1402F３ヶ月ぶりになるか……\x01",
            "２人とも、よく来てくれた。\x02",
        )
    )

    CloseMessageWindow()

    #C0829
    ChrTalk(
        0x8,
        (
            "#6Pほんと、アナタたちが\x01",
            "ウチに来てくれるなんてねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0830
    ChrTalk(
        0x8,
        (
            "#6Pうんうん、これで当分、\x01",
            "クロスベル支部も安泰だわ㈱\x02",
        )
    )

    CloseMessageWindow()

    def lambda_101D6():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_101D6)
    Sleep(100)
    OP_93(0xD, 0xE1, 0x1F4)
    Sleep(200)

    #N0831
    NpcTalk(
        0xB,
        "ツインテールの娘",
        (
            "#0809F#5Pあはは……\x01",
            "買い被りすぎだと思いますけど。\x02",
        )
    )

    CloseMessageWindow()

    #N0832
    NpcTalk(
        0xD,
        "黒髪の青年",
        "#11P#0904Fご期待に沿えるよう頑張ります。\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    SetChrName("ツインテールの娘")

    #A0833
    AnonymousTalk(
        0xFF,
        (
            "──改めまして。\x01",
            "正遊撃士、エステル・ブライト。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x1, 0x3)
    OP_CA(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    SetChrName("黒髪の青年")

    #A0834
    AnonymousTalk(
        0xFF,
        "ならびにヨシュア・ブライト。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x1, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x1, 0x3)
    OP_CA(0x0, 0x1, 0x0)
    Sleep(500)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)
    SetMessageWindowPos(230, 100, -1, -1)
    SetMessageWindowPos(-1, 10, -1, -1)
    SetChrName("エステル＆ヨシュア")

    #A0835
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "遊撃士協会・クロスベル支部に\x01",
            "正式に所属させていただきます──！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetCameraDistance(21250, 1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    OP_E3(0xA)
    Sleep(1000)
    OP_C9(0x2, 0x3, 0xFFFFFFFF, 0x320, 0x0)
    OP_CA(0x0, 0x2, 0x3)
    OP_57(0x3)
    OP_C9(0x2, 0x3, 0xFFFFFF, 0x320, 0x0)
    OP_CA(0x0, 0x2, 0x3)
    OP_E3(0xB)
    OP_CA(0x1, 0xFF, 0x0)
    SetScenarioFlags(0x5C, 3)
    NewScene("c0000", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_27_F4AF end

    def Function_28_10486(): pass

    label("Function_28_10486")

    OP_93(0xFE, 0xE1, 0x1F4)

    def lambda_10492():
        OP_95(0xFE, -4900, 0, 46370, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_10492)
    WaitChrThread(0x8, 1)
    Fade(250)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x2)
    SetChrPos(0x8, -6000, 100, 47100, 0)
    Sound(820, 0, 100, 0)
    OP_0D()
    Return()

    # Function_28_10486 end

    def Function_29_104D1(): pass

    label("Function_29_104D1")


    def lambda_104D6():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_104D6)

    def lambda_104E7():
        OP_95(0xFE, 0, 0, 50000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_104E7)
    WaitChrThread(0xB, 1)

    def lambda_10505():
        OP_95(0xFE, -3200, 0, 50000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_10505)
    WaitChrThread(0xB, 1)

    def lambda_10523():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_10523)
    Return()

    # Function_29_104D1 end

    def Function_30_1052C(): pass

    label("Function_30_1052C")


    def lambda_10531():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_10531)

    def lambda_10542():
        OP_95(0xFE, 0, 0, 50000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_10542)
    WaitChrThread(0xD, 1)

    def lambda_10560():
        OP_95(0xFE, -2400, 0, 49600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_10560)
    WaitChrThread(0xD, 1)

    def lambda_1057E():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_1057E)
    Return()

    # Function_30_1052C end

    def Function_31_10587(): pass

    label("Function_31_10587")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch00102.itc", 0x1F)
    LoadChrToIndex("chr/ch00202.itc", 0x20)
    LoadChrToIndex("chr/ch00302.itc", 0x21)
    LoadChrToIndex("chr/ch08202.itc", 0x22)
    LoadChrToIndex("chr/ch09102.itc", 0x23)
    OP_68(-2000, 1000, 2000, 0)
    MoveCamera(40, 23, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(22000, 0)
    SetChrPos(0x101, -2000, 0, -1000, 0)
    SetChrPos(0xEF, -2000, 0, -1000, 0)
    SetChrPos(0x153, -2000, 0, -1000, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xEF, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x153, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_4B(0x8, 0xFF)
    FadeToBright(1000, 0)
    OP_0D()

    def lambda_1064C():
        OP_96(0xFE, 0xFFFFFA24, 0x0, 0x5DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1064C)

    def lambda_10666():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_10666)
    Sleep(250)

    def lambda_1067A():
        OP_96(0xFE, 0xFFFFF63C, 0x0, 0x5DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x153, 1, lambda_1067A)

    def lambda_10694():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x153, 2, lambda_10694)
    Sleep(600)

    def lambda_106A8():
        OP_96(0xFE, 0xFFFFF830, 0x0, 0x190, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_106A8)

    def lambda_106C2():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xEF, 2, lambda_106C2)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x153, 1)
    WaitChrThread(0xEF, 1)

    #C0836
    ChrTalk(
        0x101,
        "#0000F──失礼します。\x02",
    )

    CloseMessageWindow()

    #N0837
    NpcTalk(
        0x8,
        "男性の声",
        "#6Pあら……？\x02",
    )

    CloseMessageWindow()
    OP_68(1000, 1000, 11300, 2000)
    OP_6F(0x79)

    #C0838
    ChrTalk(
        0x8,
        (
            "#5Pあらま、誰かと思えば\x01",
            "支援課の坊やたちじゃない？\x02",
        )
    )

    CloseMessageWindow()

    #C0839
    ChrTalk(
        0x8,
        (
            "#5Pふふ、いらっしゃい。\x01",
            "ようこそ遊撃士協会#10Rブレイサーギルド#へ。\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x101, 500, 0, 3000, 0)
    SetChrPos(0xEF, 0, 0, 1900, 0)
    SetChrPos(0x153, -500, 0, 3000, 0)

    def lambda_107DE():
        OP_96(0xFE, 0x5DC, 0x0, 0x2774, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_107DE)
    Sleep(100)

    def lambda_107FB():
        OP_96(0xFE, 0x1F4, 0x0, 0x2774, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x153, 1, lambda_107FB)
    Sleep(150)

    def lambda_10818():
        OP_96(0xFE, 0x3E8, 0x0, 0x2328, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_10818)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x153, 1)
    WaitChrThread(0xEF, 1)

    #C0840
    ChrTalk(
        0x101,
        "#0000Fこんにちは、ミシェルさん。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_1089E")

    #C0841
    ChrTalk(
        0x102,
        (
            "#12P#0102Fその……\x01",
            "突然訪問してすみません。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_108FF")

    label("loc_1089E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_108CE")

    #C0842
    ChrTalk(
        0x103,
        "#12P#0202Fご無沙汰してます。\x02",
    )

    CloseMessageWindow()
    Jump("loc_108FF")

    label("loc_108CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_108FF")

    #C0843
    ChrTalk(
        0x104,
        "#12P#0300Fよう、ご無沙汰してるな。\x02",
    )

    CloseMessageWindow()

    label("loc_108FF")


    #C0844
    ChrTalk(
        0x8,
        (
            "#5Pアナタたちが訪ねてくるなんて\x01",
            "珍しいこともあるものねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0845
    ChrTalk(
        0x8,
        "#5P──でも、いいの？\x02",
    )

    CloseMessageWindow()

    #C0846
    ChrTalk(
        0x8,
        (
            "#5P何でも《ルバーチェ》と\x01",
            "トラブルを起こしたんですって？\x02",
        )
    )

    CloseMessageWindow()

    #C0847
    ChrTalk(
        0x101,
        (
            "#0006Fやっぱりそちらにも\x01",
            "伝わっていましたか……\x02\x03",

            "#0001F一応、それに関しては\x01",
            "ケリが付いたんですけど。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x153, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x153)
    TurnDirection(0x153, 0x101, 400)

    #C0848
    ChrTalk(
        0x153,
        (
            "#6P#1100Fねー、ロイド。\x02\x03",

            "どうしてこのオジサン、\x01",
            "オンナのヒトみたいな\x01",
            "しゃべり方なのー？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xEF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_10AD4():
        TurnDirection(0xFE, 0x153, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_10AD4)
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0xEF, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_10B32")

    #C0849
    ChrTalk(
        0x102,
        "#12P#0105Fキ、キーアちゃん……\x02",
    )

    CloseMessageWindow()
    Jump("loc_10B8D")

    label("loc_10B32")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_10B62")

    #C0850
    ChrTalk(
        0x103,
        "#12P#0205Fキーア、それは……\x02",
    )

    CloseMessageWindow()
    Jump("loc_10B8D")

    label("loc_10B62")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_10B8D")

    #C0851
    ChrTalk(
        0x104,
        "#12P#0305Fお、おいキー坊……\x02",
    )

    CloseMessageWindow()

    label("loc_10B8D")

    OP_64(0xEF)
    OP_64(0x101)
    WaitChrThread(0x101, 2)
    Sleep(300)
    OP_93(0x101, 0x0, 0x190)
    Sleep(300)

    #C0852
    ChrTalk(
        0x101,
        (
            "#0006Fす、すみません。\x01",
            "まだ子供なもので……\x02",
        )
    )

    CloseMessageWindow()

    #C0853
    ChrTalk(
        0x8,
        "#5Pフッ、いいこと仔猫ちゃん？\x02",
    )

    CloseMessageWindow()

    #C0854
    ChrTalk(
        0x8,
        (
            "#5P人には人それぞれの\x01",
            "スタイルというものがあるの。\x02",
        )
    )

    CloseMessageWindow()

    #C0855
    ChrTalk(
        0x8,
        (
            "#5Pアタシにとって、この喋り方が\x01",
            "一番合っているスタイルなワケ。\x02",
        )
    )

    CloseMessageWindow()

    #C0856
    ChrTalk(
        0x8,
        (
            "#5Pアナタが着ているその服が\x01",
            "アナタに似合ってるみたいにね。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x153, 0x0, 0x1F4)

    #C0857
    ChrTalk(
        0x153,
        (
            "#12P#1105Fおー、なるほど。\x02\x03",

            "#1109Fキーアもオジサンのしゃべり方、\x01",
            "かわいくてイイと思うよー！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Sleep(1100)

    #C0858
    ChrTalk(
        0x8,
        "#5Pあら、見所あるじゃない。\x02",
    )

    CloseMessageWindow()

    #C0859
    ChrTalk(
        0x8,
        (
            "#5Pそれはともかく……\x01",
            "オジサンはやめてくれない？\x02",
        )
    )

    CloseMessageWindow()

    #C0860
    ChrTalk(
        0x8,
        "#5Pミシェルって呼んで頂戴。\x02",
    )

    CloseMessageWindow()

    #C0861
    ChrTalk(
        0x153,
        "#12P#1110Fうん、ミシェル！\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)
    OP_63(0xEF, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0862
    ChrTalk(
        0x8,
        "#5Pウフフ、良いわねこの子。\x02",
    )

    CloseMessageWindow()

    #C0863
    ChrTalk(
        0x8,
        "#5Pアナタたちの知り合いかしら？\x02",
    )

    CloseMessageWindow()

    #C0864
    ChrTalk(
        0x101,
        (
            "#0003Fはい、実は……\x02\x03",

            "#0001Fこの子について、遊撃士協会に\x01",
            "相談したいことがあるんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0865
    ChrTalk(
        0x8,
        "#5Pへぇ……？\x02",
    )

    CloseMessageWindow()
    OP_A7(0xB, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xB, 7600, 1000, 12500, 180)
    SetChrFlags(0xB, 0x40)
    OP_4B(0xB, 0xFF)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    OP_A7(0xD, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xD, 7600, 1000, 12500, 180)
    SetChrFlags(0xD, 0x40)
    OP_4B(0xD, 0xFF)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    Sleep(300)
    #Sound(1705, 255, 95, 0)    #voice#Estelle
    Sleep(1000)

    #N0866
    NpcTalk(
        0xB,
        "娘の声",
        "あれ、お客さん？\x02",
    )

    CloseMessageWindow()
    OP_68(4000, 1000, 9500, 3000)

    def lambda_10F56():
        OP_95(0xFE, 7600, 0, 10500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_10F56)

    def lambda_10F70():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_10F70)
    Sleep(400)

    def lambda_10F84():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_10F84)
    Sleep(50)

    def lambda_10F94():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xEF, 2, lambda_10F94)
    Sleep(50)

    def lambda_10FA4():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x153, 2, lambda_10FA4)
    Sleep(50)

    def lambda_10FB4():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_10FB4)
    Sleep(100)

    def lambda_10FC4():
        OP_95(0xFE, 7600, 0, 10500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_10FC4)

    def lambda_10FDE():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_10FDE)
    WaitChrThread(0xB, 1)

    def lambda_10FF3():
        OP_95(0xFE, 5600, 0, 9000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_10FF3)
    WaitChrThread(0xD, 1)

    def lambda_11011():
        OP_95(0xFE, 6000, 0, 10100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_11011)
    WaitChrThread(0xB, 1)

    def lambda_1102F():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_1102F)
    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0xD, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    WaitChrThread(0xD, 1)

    def lambda_11067():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_11067)
    Sleep(1000)
    OP_6F(0x1)

    #C0867
    ChrTalk(
        0xB,
        "#11P#0802Fあ……ロイド君たち！？\x02",
    )

    CloseMessageWindow()

    #C0868
    ChrTalk(
        0x101,
        "#0000F#6Pやあ、エステル、ヨシュア。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_1112B")

    #C0869
    ChrTalk(
        0x102,
        "#6P#0109Fふふ、この間はどうも。\x02",
    )

    CloseMessageWindow()

    #C0870
    ChrTalk(
        0xD,
        (
            "#11P#0902F珍しいね。\x01",
            "ギルドに来てくれるなんて。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11200")

    label("loc_1112B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_11195")

    #C0871
    ChrTalk(
        0x103,
        "#6P#0202F一週間ぶりくらいですね。\x02",
    )

    CloseMessageWindow()

    #C0872
    ChrTalk(
        0xD,
        (
            "#11P#0902F珍しいね。\x01",
            "ギルドに来てくれるなんて。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11200")

    label("loc_11195")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_11200")

    #C0873
    ChrTalk(
        0x104,
        "#6P#0300Fよ、一週間ぶりくらいだな。\x02",
    )

    CloseMessageWindow()

    #C0874
    ChrTalk(
        0xD,
        (
            "#11P#0902F珍しいですね。\x01",
            "ギルドに来てくれるなんて。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11200")


    #C0875
    ChrTalk(
        0xB,
        (
            "#11P#0809Fえへへ、ひょっとして\x01",
            "あたしたちに会いに来てくれたの？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0876
    ChrTalk(
        0xB,
        "#11P#0805Fあれ、その子は……\x02",
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_63(0xB, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_68(620, 1000, 9840, 1500)
    MoveCamera(35, 21, 0, 1500)
    SetCameraDistance(21500, 1500)

    def lambda_112D3():

        label("loc_112D3")

        TurnDirection(0xFE, 0xB, 500)
        Yield()
        Jump("loc_112D3")

    QueueWorkItem2(0x101, 2, lambda_112D3)

    def lambda_112E5():

        label("loc_112E5")

        TurnDirection(0xFE, 0xB, 500)
        Yield()
        Jump("loc_112E5")

    QueueWorkItem2(0x153, 2, lambda_112E5)

    def lambda_112F7():

        label("loc_112F7")

        TurnDirection(0xFE, 0xB, 500)
        Yield()
        Jump("loc_112F7")

    QueueWorkItem2(0x8, 2, lambda_112F7)

    def lambda_11309():
        OP_95(0xFE, 500, 0, 9000, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_11309)
    Sleep(500)

    def lambda_11326():
        OP_96(0xFE, 0xFFFFFBB4, 0x0, 0x2260, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_11326)
    WaitChrThread(0xB, 1)
    TurnDirection(0xB, 0x153, 800)
    WaitChrThread(0xEF, 1)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x153, 0x2)
    EndChrThread(0x8, 0x2)
    OP_6F(0x79)
    OP_64(0xB)

    #C0877
    ChrTalk(
        0xB,
        (
            "#12P#0809Fわわっ……\x01",
            "すっごく可愛い子ねぇ！\x02\x03",

            "#0802Fどうしたの？\x01",
            "ロイド君たちの知り合い！？\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0xD, 3, 0, 32)

    #C0878
    ChrTalk(
        0x101,
        (
            "#5P#0000Fああ……\x01",
            "キーアっていうんだけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0879
    ChrTalk(
        0x153,
        (
            "#1105F#5Pおねえちゃん、\x01",
            "髪がピョンピョンしてるねー。\x02\x03",

            "#1100Fもしかしてゆーげきしのヒト？\x02",
        )
    )

    CloseMessageWindow()

    #C0880
    ChrTalk(
        0xB,
        (
            "#12P#0800Fうん、あたしはエステル。\x01",
            "こっちのお兄さんはヨシュア。\x02\x03",

            "#0809Fそっか、キーアちゃんって言うんだ。\x01",
            "よろしくね！\x02",
        )
    )

    CloseMessageWindow()

    #C0881
    ChrTalk(
        0x153,
        "#1109F#5Pうんっ！\x02",
    )

    CloseMessageWindow()

    #C0882
    ChrTalk(
        0x101,
        "#5P#0012Fうーん、速攻で馴染んだなぁ。\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0xD, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_11591")

    #C0883
    ChrTalk(
        0xD,
        (
            "#12P#0909Fはは、エステルは子供に\x01",
            "懐かれやすいタイプだけど……\x02\x03",

            "#0900Fそれにしても\x01",
            "人懐っこい子みたいですね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11601")

    label("loc_11591")


    #C0884
    ChrTalk(
        0xD,
        (
            "#12P#0909Fはは、エステルは子供に\x01",
            "懐かれやすいタイプだけど……\x02\x03",

            "#0900Fそれにしても\x01",
            "人懐っこい子みたいだね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11601")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_1163C")

    #C0885
    ChrTalk(
        0x102,
        "#6P#0102Fふふ、それは折り紙付きですね。\x02",
    )

    CloseMessageWindow()
    Jump("loc_116AB")

    label("loc_1163C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_11675")

    #C0886
    ChrTalk(
        0x103,
        "#6P#0204Fええ、それは折り紙付きかと。\x02",
    )

    CloseMessageWindow()
    Jump("loc_116AB")

    label("loc_11675")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_116AB")

    #C0887
    ChrTalk(
        0x104,
        "#6P#0302Fああ、そいつは折り紙付きだぜ。\x02",
    )

    CloseMessageWindow()

    label("loc_116AB")


    #C0888
    ChrTalk(
        0x8,
        (
            "#5Pそれで、その子について\x01",
            "何か相談があるそうだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0889
    ChrTalk(
        0x8,
        (
            "#5Pどうする？\x01",
            "２階で聞かせてもらおうかしら？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1171E():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1171E)
    Sleep(100)

    def lambda_1172E():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_1172E)
    Sleep(50)
    OP_93(0xEF, 0x0, 0x1F4)

    #C0890
    ChrTalk(
        0x101,
        (
            "#2P#0001Fあ……\x01",
            "はい、差し支えなければ。\x02",
        )
    )

    CloseMessageWindow()

    #C0891
    ChrTalk(
        0xB,
        "#12P#0805Fあれ、そういう話なの？\x02",
    )

    CloseMessageWindow()

    #C0892
    ChrTalk(
        0xD,
        "#12P#0901F何か事情があるみたいだね。\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(22000, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    OP_68(-8200, 900, 48300, 0)
    MoveCamera(47, 19, 0, 0)
    OP_6E(460, 0)
    SetCameraDistance(20000, 0)
    SetChrChipByIndex(0xD, 0x9)
    SetChrSubChip(0xD, 0x1)
    SetChrPos(0xD, -10700, 150, 49200, 180)
    SetChrChipByIndex(0xB, 0x8)
    SetChrSubChip(0xB, 0x0)
    SetChrPos(0xB, -8400, 150, 49200, 180)
    SetChrChipByIndex(0x8, 0x23)
    SetChrSubChip(0x8, 0x2)
    SetChrPos(0x8, -6000, 100, 49200, 180)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0xEF, 0x4)
    SetChrFlags(0x153, 0x4)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x153, 0x22)
    SetChrSubChip(0x153, 0x2)
    OP_52(0x153, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x3B6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x153, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x3B6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x153, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x3B6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_118A3")
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x1)
    Jump("loc_118CA")

    label("loc_118A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_118B9")
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x1)
    Jump("loc_118CA")

    label("loc_118B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_118CA")
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x104, 0x1)

    label("loc_118CA")

    SetChrPos(0x153, -10900, 200, 47100, 0)
    SetChrPos(0x101, -8400, 100, 47000, 0)
    SetChrPos(0xEF, -6000, 100, 47000, 0)
    SetMapObjFrame(0xFF, "on_off", 0x0, 0x1)
    SetMapObjFrame(0xFF, "shadow_onoff", 0x0, 0x1)
    Sleep(500)
    SetCameraDistance(19500, 1500)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x10)

    #C0893
    ChrTalk(
        0xB,
        "#5P#0801Fそ、そんな事が……\x02",
    )

    CloseMessageWindow()

    #C0894
    ChrTalk(
        0xD,
        (
            "#0901F#5Pこの一週間、裏通りの空気が\x01",
            "少し緊張した感じだったけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0895
    ChrTalk(
        0x8,
        (
            "#11Pやれやれ……\x01",
            "そんな顛末になってたとはねぇ。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_11A87")

    #C0896
    ChrTalk(
        0x102,
        (
            "#0103F#12P……警察としては\x01",
            "ルバーチェ側の言い分を\x01",
            "一応認める方針になりました。\x02\x03",

            "#0101Fできればギルドの方にも\x01",
            "それを踏まえていただけると\x01",
            "ありがたいんですが……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11B10")

    label("loc_11A87")


    #C0897
    ChrTalk(
        0x101,
        (
            "#12P#0003F……警察としては\x01",
            "ルバーチェ側の言い分を\x01",
            "一応認める事になりました。\x02\x03",

            "#0000Fできればその前提で\x01",
            "話をさせて欲しいんですが……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11B10")


    #C0898
    ChrTalk(
        0xB,
        "#5P#0801Fむむむ……\x02",
    )

    CloseMessageWindow()

    #C0899
    ChrTalk(
        0x8,
        (
            "#11Pまあ、仕方ないわね。\x01",
            "こちらは部外者だったワケだし。\x02",
        )
    )

    CloseMessageWindow()

    #C0900
    ChrTalk(
        0x8,
        (
            "#11Pそれにしても《黒の競売会#10Rシュバルツオークション#》に\x01",
            "潜入捜査を敢行するなんて……\x02",
        )
    )

    CloseMessageWindow()

    #C0901
    ChrTalk(
        0x8,
        "#11Pやるじゃない、見直したわよ？\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)
    Sleep(50)
    SetChrSubChip(0xEF, 0x0)
    Sleep(300)

    #C0902
    ChrTalk(
        0x101,
        "#6P#0002Fそ、そうですか……？\x02",
    )

    CloseMessageWindow()

    #C0903
    ChrTalk(
        0xB,
        (
            "#5P#0806Fあ、あたしたちだって\x01",
            "何とか調べようとしてたのに……\x02\x03",

            "しかも招待カードを渡したのが\x01",
            "レンだったなんて……\x02\x03",

            "#0801Fまったくあの子ったら……\x01",
            "あたし達にくれればいいのに！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0xEF, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    SetChrSubChip(0x101, 0x0)
    Sleep(50)
    SetChrSubChip(0xEF, 0x1)

    #C0904
    ChrTalk(
        0xD,
        (
            "#0904Fまあ、それは仕方ないよ。\x02\x03",

            "#0900F僕たちにはまだ、\x01",
            "会えない事情があるわけだし。\x02",
        )
    )

    CloseMessageWindow()

    #C0905
    ChrTalk(
        0xB,
        "#5P#0806Fそ、それはそうだけど……\x02",
    )

    CloseMessageWindow()

    #C0906
    ChrTalk(
        0x101,
        (
            "#12P#0008F結果的に、君たちから聞いた話を\x01",
            "横取りした形になっちゃったな……\x02\x03",

            "#0003Fゴメン、連絡くらいすればよかった。\x02",
        )
    )

    CloseMessageWindow()

    #C0907
    ChrTalk(
        0xB,
        (
            "#5P#0805Fあ、ううん。\x01",
            "そっちの方は気にしてないわ。\x02\x03",

            "#0802Fロイド君たちも頑張ったみたいだし、\x01",
            "あの子の事が気になるだけだから。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xB, 0x2)
    Sleep(300)

    #C0908
    ChrTalk(
        0xB,
        (
            "#11P#0801F……でも……\x01",
            "確かに問題はキーアちゃんか。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_11EED")

    #C0909
    ChrTalk(
        0x102,
        "#0108F#12Pええ……\x02",
    )

    CloseMessageWindow()
    Jump("loc_11F36")

    label("loc_11EED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_11F13")

    #C0910
    ChrTalk(
        0x103,
        "#0203F#12Pはい……\x02",
    )

    CloseMessageWindow()
    Jump("loc_11F36")

    label("loc_11F13")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_11F36")

    #C0911
    ChrTalk(
        0x104,
        "#0303F#12Pまあな……\x02",
    )

    CloseMessageWindow()

    label("loc_11F36")


    #C0912
    ChrTalk(
        0x153,
        "#6P#1110Fふえ～？\x02",
    )

    CloseMessageWindow()

    #C0913
    ChrTalk(
        0x8,
        (
            "#11P察するに、その子の素性を\x01",
            "当たってみて欲しいわけね？\x02",
        )
    )

    CloseMessageWindow()

    #C0914
    ChrTalk(
        0x8,
        "#11P遊撃士協会の情報網を使って。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)
    Sleep(50)
    SetChrSubChip(0xEF, 0x0)
    Sleep(300)

    #C0915
    ChrTalk(
        0x101,
        (
            "#6P#0003Fはい……\x01",
            "まさにそれをお願いに来ました。\x02\x03",

            "#0000Fその、依頼料も\x01",
            "何とか用意できると思います。\x02",
        )
    )

    CloseMessageWindow()

    #C0916
    ChrTalk(
        0x8,
        "#11Pああ、必要ないわ。\x02",
    )

    CloseMessageWindow()

    #C0917
    ChrTalk(
        0x8,
        (
            "#11Pこういった案件については\x01",
            "ウチは無料#4Rタ ダ#でやらせてもらってるの。\x02",
        )
    )

    CloseMessageWindow()

    #C0918
    ChrTalk(
        0x8,
        (
            "#11P早速、各地の支部に問い合わせて\x01",
            "それっぽい情報を当たってみるわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0919
    ChrTalk(
        0x101,
        "#6P#0002Fあ、ありがとうございます！\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_1215C")

    #C0920
    ChrTalk(
        0x102,
        (
            "#0105F#12Pな、なんだか随分とあっさり\x01",
            "引き受けてくださるんですね……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_121F1")

    label("loc_1215C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_121A9")

    #C0921
    ChrTalk(
        0x103,
        (
            "#0205F#12P……随分とあっさり\x01",
            "引き受けてくださるんですね？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_121F1")

    label("loc_121A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_121F1")

    #C0922
    ChrTalk(
        0x104,
        (
            "#0305F#12Pはー、随分あっさりと\x01",
            "引き受けてくれるもんだな？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_121F1")

    SetChrSubChip(0xB, 0x0)
    Sleep(150)

    #C0923
    ChrTalk(
        0xB,
        (
            "#5P#0800Fまあ、この手の話については\x01",
            "ウチは即断即決がモットーだから。\x02",
        )
    )

    CloseMessageWindow()

    #C0924
    ChrTalk(
        0xD,
        (
            "#0904Fちなみに、こういう案件の費用は\x01",
            "各種の基金や寄付が当てられるんだ。\x02\x03",

            "#0900Fだから遠慮することはないよ。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)
    Sleep(50)
    SetChrSubChip(0xEF, 0x1)
    Sleep(300)

    #C0925
    ChrTalk(
        0x101,
        "#12P#0002Fな、なるほど……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_12332")

    #C0926
    ChrTalk(
        0x102,
        (
            "#0102F#12Pまさに民間人を助けるための\x01",
            "制度があるわけですね……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_123D7")

    label("loc_12332")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_12387")

    #C0927
    ChrTalk(
        0x103,
        (
            "#0202F#12Pまさに民間人を助けるための\x01",
            "システムがあるわけですか……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_123D7")

    label("loc_12387")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_123D7")

    #C0928
    ChrTalk(
        0x104,
        (
            "#0300F#12Pまさに民間人を助けるための\x01",
            "仕組みがあるってわけだな……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_123D7")


    #C0929
    ChrTalk(
        0x8,
        (
            "#11P結果が出るまで\x01",
            "ちょっと時間はかかるけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0930
    ChrTalk(
        0x8,
        (
            "#11Pまあ、１週間くらいで\x01",
            "そちらに連絡できると思うわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0931
    ChrTalk(
        0x101,
        (
            "#12P#0004F……十分です。\x01",
            "どうかよろしくお願いします。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0932
    ChrTalk(
        0xB,
        (
            "#5P#0805Fそうだ、何だったら、\x01",
            "ウチでキーアちゃんを預かる？\x02\x03",

            "#0800F一応基金から、保護対象者の\x01",
            "生活費なんかも出るんだけど。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0933
    ChrTalk(
        0x101,
        "#12P#0005Fえ……！？\x02",
    )

    CloseMessageWindow()

    #C0934
    ChrTalk(
        0xD,
        (
            "#0903Fそうだね……\x02\x03",

            "#0901F安全のことを考えるなら\x01",
            "それもアリかもしれないよ？\x02\x03",

            "いざとなればクロスベル以外の\x01",
            "安全な避難先も手配できるし。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_12622")

    #C0935
    ChrTalk(
        0x102,
        "#0108F#12Pで、でもそれは……\x02",
    )

    CloseMessageWindow()
    Jump("loc_12679")

    label("loc_12622")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_1264E")

    #C0936
    ChrTalk(
        0x103,
        "#0208F#12P……それは……\x02",
    )

    CloseMessageWindow()
    Jump("loc_12679")

    label("loc_1264E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_12679")

    #C0937
    ChrTalk(
        0x104,
        "#0306F#12Pいや、そいつは……\x02",
    )

    CloseMessageWindow()

    label("loc_12679")


    #C0938
    ChrTalk(
        0x101,
        "#12P#0008F…………………………………\x02",
    )

    CloseMessageWindow()

    #C0939
    ChrTalk(
        0x153,
        (
            "#6P#1105Fんー？\x01",
            "どうしたの、ロイド？\x02\x03",

            "#1101Fおなか痛くなっちゃった？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x1)
    Sleep(300)

    #C0940
    ChrTalk(
        0x101,
        (
            "#11P#0005Fああ、いや……\x02\x03",

            "#0006F……そうだな。\x01",
            "この子がクロスベル以外の\x01",
            "出身である可能性は高そうだし……\x02\x03",

            "#0008F……何よりも安全の事を考えたら……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_127B4")

    #C0941
    ChrTalk(
        0x102,
        "#0108F#11Pロイド……\x02",
    )

    CloseMessageWindow()
    Jump("loc_12815")

    label("loc_127B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_127E4")

    #C0942
    ChrTalk(
        0x103,
        "#0208F#11P……ロイドさん……\x02",
    )

    CloseMessageWindow()
    Jump("loc_12815")

    label("loc_127E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_12815")

    #C0943
    ChrTalk(
        0x104,
        "#0308F#11P………………………………\x02",
    )

    CloseMessageWindow()

    label("loc_12815")


    #C0944
    ChrTalk(
        0x153,
        "#6P#1100F？？？\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xB, 0x2)
    Sleep(300)

    #C0945
    ChrTalk(
        0xB,
        (
            "#11P#0800F#11Pえっとね、キーアちゃん。\x02\x03",

            "しばらくあたしたちと一緒に\x01",
            "暮らさないかって話なんだけど……\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xD, 0x0)
    OP_63(0x153, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0946
    ChrTalk(
        0x153,
        (
            "#6P#1105Fエステルたちと？\x02\x03",

            "#1110Fそれじゃ、エステルたちも\x01",
            "あのビルに引っ越してくるの？\x02",
        )
    )

    CloseMessageWindow()

    #C0947
    ChrTalk(
        0xB,
        (
            "#11P#0805Fあ、ううん……\x02\x03",

            "#0800Fキーアちゃんがこっちに\x01",
            "引っ越してくる感じかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0948
    ChrTalk(
        0x153,
        "#6P#1105Fロイドたちもいっしょに？\x02",
    )

    CloseMessageWindow()

    #C0949
    ChrTalk(
        0xB,
        (
            "#11P#0806Fうーん。\x01",
            "それはちょっと無理かな……\x02\x03",

            "#0800Fでも、そんなには離れてないし、\x01",
            "会おうと思えばすぐに会えるわよ？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x153, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(300)
    Sound(2030, 255, 90, 0)    #voice#KeA
    Sleep(1700)
    OP_64(0x153)
    Sleep(800)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0950
    ChrTalk(
        0x153,
        "#6P#5S#1109F#Nゼッタイにヤダ。\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_82(0xC8, 0x0, 0xBB8, 0x320)
    #Sound(1706, 255, 100, 0)    #voice#Estelle

    #C0951
    ChrTalk(
        0xB,
        "#11P#0807F#4Sガーン！\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    #C0952
    ChrTalk(
        0x101,
        "#11P#0011Fキーア……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_12BA0")

    #C0953
    ChrTalk(
        0x153,
        (
            "#6P#1108Fだってロイドたちと\x01",
            "離れるなんてヤダもん。\x02\x03",

            "#1103Fエリィだって、ティオだって\x01",
            "ランディだって、ツァイトだって\x01",
            "かちょーだっているし。\x02\x03",

            "#1101Fキーア、ゼッタイに行かない。\x02",
        )
    )

    CloseMessageWindow()

    #C0954
    ChrTalk(
        0x102,
        "#0102F#11Pキ、キーアちゃん……（じーん）\x02",
    )

    CloseMessageWindow()
    Jump("loc_12D67")

    label("loc_12BA0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_12C8A")

    #C0955
    ChrTalk(
        0x153,
        (
            "#6P#1103Fだってロイドたちと\x01",
            "離れるなんてヤダもん。\x02\x03",

            "ティオだって、エリィだって\x01",
            "ランディだって、ツァイトだって\x01",
            "かちょーだっているし。\x02\x03",

            "#1101Fキーア、ゼッタイに行かない。\x02",
        )
    )

    CloseMessageWindow()

    #C0956
    ChrTalk(
        0x103,
        "#0204F#11P…………………………（じーん）\x02",
    )

    CloseMessageWindow()
    Jump("loc_12D67")

    label("loc_12C8A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_12D67")

    #C0957
    ChrTalk(
        0x153,
        (
            "#6P#1103Fだってロイドたちと\x01",
            "離れるなんてヤダもん。\x02\x03",

            "ランディだって、エリィだって\x01",
            "ティオだって、ツァイトだって\x01",
            "かちょーだっているし。\x02\x03",

            "#1101Fキーア、ゼッタイに行かない。\x02",
        )
    )

    CloseMessageWindow()

    #C0958
    ChrTalk(
        0x104,
        "#0304F#11Pハハ……言葉がねぇな。\x02",
    )

    CloseMessageWindow()

    label("loc_12D67")


    #C0959
    ChrTalk(
        0xB,
        "#11P#0809Fそ、そっか……\x02",
    )

    CloseMessageWindow()

    #C0960
    ChrTalk(
        0xD,
        "#0904F#5Pはは、フラれちゃったね。\x02",
    )

    CloseMessageWindow()

    #C0961
    ChrTalk(
        0x8,
        (
            "#11Pあらら、エステルちゃんが\x01",
            "子供にフラれるなんて\x01",
            "すっごく珍しいわね～。\x02",
        )
    )

    CloseMessageWindow()

    #C0962
    ChrTalk(
        0x8,
        "#11P何気にショック受けちゃってる？\x02",
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    SetChrSubChip(0xB, 0x1)
    Sleep(300)

    #C0963
    ChrTalk(
        0xB,
        (
            "#5P#0801Fう、受けてないってば！\x02\x03",

            "#0806Fはあ……\x01",
            "でもちょっとショックかも。\x02",
        )
    )

    CloseMessageWindow()

    #C0964
    ChrTalk(
        0x153,
        (
            "#6P#1106Fべつにエステルのことは\x01",
            "キライじゃないけど……\x02\x03",

            "#1112Fでも、ヤなもんはヤなんだもん。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xB, 0x0)
    Sleep(50)
    SetChrSubChip(0xB, 0x2)
    Sleep(200)

    #C0965
    ChrTalk(
        0xB,
        (
            "#11P#0809Fあはは、ゴメンゴメン。\x01",
            "あたしが無神経だったわ。\x02\x03",

            "#0802Fロイド君たち、いいなぁ。\x01",
            "こんなに好かれちゃってて……\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)
    Sleep(300)

    #C0966
    ChrTalk(
        0x101,
        (
            "#12P#0004Fはは……\x01",
            "何でか判らないんだけどね。\x02\x03",

            "#0000Fこの子の知り合いに似ている\x01",
            "可能性はありそうなんだけど……\x02\x03",

            "その割には何も思い出せない\x01",
            "みたいなんだよな……\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xD, 0x1)
    Sleep(150)

    #C0967
    ChrTalk(
        0xD,
        (
            "#0903F──それなんだけど。\x02\x03",

            "#0900F身元の確認については\x01",
            "ミシェルさんに頼むとして……\x02\x03",

            "記憶喪失の方は専門家に\x01",
            "相談しなくてもいいのかい？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xEF, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x101, 0x1)
    Sleep(300)

    #C0968
    ChrTalk(
        0x101,
        "#11P#0005Fえ……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_1312C")

    #C0969
    ChrTalk(
        0x102,
        "#0105F#11P専門家というと……？\x02",
    )

    CloseMessageWindow()
    Jump("loc_1317F")

    label("loc_1312C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_1315A")

    #C0970
    ChrTalk(
        0x103,
        "#0205F#11P専門家、ですか？\x02",
    )

    CloseMessageWindow()
    Jump("loc_1317F")

    label("loc_1315A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_1317F")

    #C0971
    ChrTalk(
        0x104,
        "#0305F#11P専門家……？\x02",
    )

    CloseMessageWindow()

    label("loc_1317F")


    #C0972
    ChrTalk(
        0xD,
        (
            "#0908Fうん、キーアちゃんの記憶喪失が\x01",
            "心や精神の問題と仮定するなら……\x02\x03",

            "#0900Fこの場合、専門家といったら\x01",
            "七耀教会の人たちだと思うけど。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0973
    ChrTalk(
        0x101,
        "#11P#0011Fあ……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_13283")

    #C0974
    ChrTalk(
        0x102,
        "#0103F#11P……確かに……\x02",
    )

    CloseMessageWindow()
    Jump("loc_132DA")

    label("loc_13283")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_132AF")

    #C0975
    ChrTalk(
        0x103,
        "#0204F#11P……なるほど。\x02",
    )

    CloseMessageWindow()
    Jump("loc_132DA")

    label("loc_132AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_132DA")

    #C0976
    ChrTalk(
        0x104,
        "#0302F#11P言われてみりゃ……\x02",
    )

    CloseMessageWindow()

    label("loc_132DA")

    OP_63(0x153, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0977
    ChrTalk(
        0x153,
        "#6P#1111Fしちよーキョウカイ？\x02",
    )

    CloseMessageWindow()

    #C0978
    ChrTalk(
        0x8,
        (
            "#11Pそうね、クロスベルでは\x01",
            "近代医療が発達してるけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0979
    ChrTalk(
        0x8,
        (
            "#11P心の分野に関しては\x01",
            "まだまだ教会の専門家の方が\x01",
            "詳しいかもしれないわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0980
    ChrTalk(
        0xB,
        (
            "#11P#0809Fうんうん、確かに！\x02\x03",

            "#0802Fあたしたちも色々と\x01",
            "助けてもらったくらいだし！\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)
    Sleep(300)

    #C0981
    ChrTalk(
        0x101,
        "#12P#0005Fへえ、そうなのか……？\x02",
    )

    CloseMessageWindow()

    #C0982
    ChrTalk(
        0xD,
        (
            "#0904Fうん……主に僕の方が\x01",
            "色々と助けてもらったんだ。\x02\x03",

            "#0900Fその人ほどの使い手が\x01",
            "クロスベル大聖堂にいるかは\x01",
            "ちょっと判らないけど……\x02\x03",

            "一度、相談してみたらどうだい？\x02",
        )
    )

    CloseMessageWindow()

    #C0983
    ChrTalk(
        0x101,
        (
            "#12P#0004F……分かった。\x01",
            "貴重なアドバイス、ありがとう。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x1)
    Sleep(300)

    #C0984
    ChrTalk(
        0x101,
        (
            "#11P#0000F──なあ、キーア。\x02\x03",

            "この後、街外れにある教会に\x01",
            "行きたいんだけど、いいかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0985
    ChrTalk(
        0x153,
        (
            "#6P#1104Fんー、いいよ。\x02\x03",

            "#1100Fキョウカイって女神さまに\x01",
            "オイノリするところだよね？\x02\x03",

            "#1109Fそれじゃあ、れっつごー！\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xB, 0x2)
    Sleep(50)
    SetChrSubChip(0xD, 0x0)
    Sleep(150)

    #C0986
    ChrTalk(
        0xB,
        "#11P#0809Fあはは……\x02",
    )

    CloseMessageWindow()

    #C0987
    ChrTalk(
        0x8,
        "#11Pホント、元気な子ねぇ。\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(20000, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    ClearChrFlags(0x101, 0x4)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    ClearChrFlags(0xEF, 0x4)
    SetChrChipByIndex(0xEF, 0xFF)
    SetChrSubChip(0xEF, 0x0)
    ClearChrFlags(0x153, 0x4)
    SetChrChipByIndex(0x153, 0xFF)
    SetChrSubChip(0x153, 0x0)
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    SetChrPos(0x8, 1000, 0, 12820, 180)
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_D5(0x20)
    OP_D5(0x21)
    OP_D5(0x22)
    OP_D5(0x23)
    OP_4C(0x8, 0xFF)
    OP_68(-8400, 1300, 45000, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(23000, 0)
    SetChrPos(0x0, -8400, 0, 45000, 180)
    SetChrPos(0x1, -8400, 0, 45000, 180)
    SetChrPos(0x2, -8400, 0, 45000, 180)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xC, -8400, 150, 49200, 180)
    SetChrPos(0xE, -10700, 150, 49200, 180)
    SetMapObjFrame(0xFF, "on_off", 0x1, 0x1)
    SetMapObjFrame(0xFF, "shadow_onoff", 0x1, 0x1)
    ClearMapFlags(0x10000000)
    SetScenarioFlags(0xA8, 0)
    OP_29(0x48, 0x1, 0x3)
    EventEnd(0x5)
    Return()

    # Function_31_10587 end

    def Function_32_13772(): pass

    label("Function_32_13772")


    def lambda_13777():
        OP_95(0xFE, 1400, 0, 8500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_13777)
    WaitChrThread(0xD, 1)
    OP_93(0xD, 0x13B, 0x1F4)
    Return()

    # Function_32_13772 end

    def Function_33_13798(): pass

    label("Function_33_13798")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch00102.itc", 0x1F)
    LoadChrToIndex("chr/ch00202.itc", 0x20)
    LoadChrToIndex("chr/ch00302.itc", 0x21)
    LoadChrToIndex("chr/ch08700.itc", 0x22)
    LoadChrToIndex("chr/ch09102.itc", 0x23)
    LoadChrToIndex("chr/ch32000.itc", 0x24)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu06000.itp")
    OP_68(-8200, 1600, 48300, 0)
    MoveCamera(47, 19, 0, 0)
    OP_6E(460, 0)
    SetCameraDistance(19500, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x2)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x1)
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x104, 0x1)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x103, 0x4)
    SetChrFlags(0x104, 0x4)
    SetChrPos(0x102, -10700, 100, 47100, 0)
    SetChrPos(0x101, -8400, 100, 47100, 0)
    SetChrPos(0x104, -6000, 100, 47100, 0)
    SetChrPos(0x103, -10700, 150, 49200, 180)
    OP_4B(0x9, 0xFF)
    SetChrChipByIndex(0x9, 0x7)
    SetChrSubChip(0x9, 0x0)
    SetChrPos(0x9, -8400, 150, 49200, 180)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    OP_4B(0x8, 0xFF)
    SetChrChipByIndex(0x8, 0x23)
    SetChrSubChip(0x8, 0x2)
    SetChrPos(0x8, -6000, 100, 49200, 180)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    SetChrChipByIndex(0x14, 0x22)
    SetChrSubChip(0x14, 0x0)
    SetChrChipByIndex(0x12, 0x24)
    SetMapObjFrame(0xFF, "on_off", 0x0, 0x1)
    SetMapObjFrame(0xFF, "shadow_onoff", 0x0, 0x1)
    Sleep(500)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0988
    AnonymousTalk(
        0x9,
        (
            "──なるほど。\x01",
            "そんな事になっていたとは。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_68(-8200, 1100, 48300, 1500)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x1)

    #C0989
    ChrTalk(
        0x8,
        (
            "#11Pうーん、失踪者の噂については\x01",
            "こちらも掴んではいたけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0990
    ChrTalk(
        0x8,
        "#11P今回は完全に出遅れちゃったわね。\x02",
    )

    CloseMessageWindow()

    #C0991
    ChrTalk(
        0x8,
        (
            "#11Pしかもよりにもよって\x01",
            "あの教団が出てくるなんて……\x02",
        )
    )

    CloseMessageWindow()

    #C0992
    ChrTalk(
        0x9,
        "#5P#1403F……………………………………\x02",
    )

    CloseMessageWindow()

    #C0993
    ChrTalk(
        0x101,
        (
            "#12P#0006F……その、アリオスさんも\x01",
            "６年前の教団事件に\x01",
            "関わっていたんですよね？\x02\x03",

            "#0013F残党が残っている可能性は\x01",
            "どのくらいあると思いますか？\x02",
        )
    )

    CloseMessageWindow()

    #C0994
    ChrTalk(
        0x9,
        (
            "#5P#1403F……そうだな。\x02\x03",

            "#1401F確かに全てのロッジは制圧されたが\x01",
            "地下に残党が潜った可能性はあり得る。\x02\x03",

            "犯罪組織などが手を貸せば\x01",
            "潜伏は非常にやりやすくなるだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0995
    ChrTalk(
        0x103,
        "#0208F#6P……………………………………\x02",
    )

    CloseMessageWindow()

    #C0996
    ChrTalk(
        0x104,
        (
            "#0306F#12Pまさに《ルバーチェ》なんか\x01",
            "打ってつけの隠れ蓑だったわけか。\x02",
        )
    )

    CloseMessageWindow()

    #C0997
    ChrTalk(
        0x102,
        (
            "#6P#0106Fでも、どうしてそんな\x01",
            "リスクの高いことを……\x02\x03",

            "#0108F計算高いマルコーニ会長にしては\x01",
            "少し違和感を感じますけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0998
    ChrTalk(
        0x8,
        (
            "#11P確かに、あの教団の残党を\x01",
            "匿#2Rかくま#ったりしていると分かったら\x01",
            "放っておかない所は多いハズよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0999
    ChrTalk(
        0x8,
        (
            "#11Pウチはもちろんだけど……\x01",
            "教会とか例の《結社》とかもね。\x02",
        )
    )

    CloseMessageWindow()

    #C1000
    ChrTalk(
        0x101,
        (
            "#12P#0008Fとなると……\x02\x03",

            "#0001Fまだ見えていない事情が\x01",
            "存在しているんでしょうか？\x02",
        )
    )

    CloseMessageWindow()

    #C1001
    ChrTalk(
        0x9,
        (
            "#5P#1403Fああ──しかしそれを\x01",
            "確かめている余裕は無さそうだ。\x02\x03",

            "#1401F今は手分けして、マフィアと\x01",
            "失踪者達の行方を追うべきだろう。\x02\x03",

            "おそらくそれが、教団の残党の\x01",
            "正体を炙り出す事にも繋がるはずだ。\x02",
        )
    )

    CloseMessageWindow()

    #C1002
    ChrTalk(
        0x103,
        "#0202F#6Pあの、それでは……\x02",
    )

    CloseMessageWindow()

    #C1003
    ChrTalk(
        0x104,
        (
            "#0305F#12P協力体制を結ぶってことで\x01",
            "そっちもいいのかよ？\x02",
        )
    )

    CloseMessageWindow()

    #C1004
    ChrTalk(
        0x8,
        "#11Pええ、こちらも異存はないわ。\x02",
    )

    CloseMessageWindow()

    #C1005
    ChrTalk(
        0x8,
        (
            "#11P市民から失踪者が出ている時点で\x01",
            "アタシたちは無関係ではいられない。\x02",
        )
    )

    CloseMessageWindow()

    #C1006
    ChrTalk(
        0x8,
        "#11Pそれに薬物被害についてもね。\x02",
    )

    CloseMessageWindow()

    #C1007
    ChrTalk(
        0x101,
        (
            "#12P#0004F……助かります。\x01",
            "どうかよろしくお願いします。\x02",
        )
    )

    CloseMessageWindow()

    #C1008
    ChrTalk(
        0x9,
        (
            "#5P#1404Fああ、こちらこそ。\x02\x03",

            "#1402Fそうと決まれば、役割分担を\x01",
            "決めておきたい所だが……\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x9, 0x1)
    Sleep(300)

    #C1009
    ChrTalk(
        0x9,
        (
            "#1P#1400Fエステルたちはともかく\x01",
            "他のメンバーはどうしている？\x02",
        )
    )

    CloseMessageWindow()

    #C1010
    ChrTalk(
        0x8,
        (
            "#11P幸い、スコットとリンたちにも\x01",
            "緊急の仕事は入っていないわ。\x02",
        )
    )

    CloseMessageWindow()

    #C1011
    ChrTalk(
        0x8,
        (
            "#11Pエステルちゃんたちを含めたら\x01",
            "総勢７名は確保できるわね。\x02",
        )
    )

    CloseMessageWindow()

    #C1012
    ChrTalk(
        0x9,
        (
            "#1P#1403Fよし、全員に召集をかけてくれ。\x02\x03",

            "#1401F今日中に目ぼしい場所は\x01",
            "回れるようにしておきたい。\x02",
        )
    )

    CloseMessageWindow()

    #C1013
    ChrTalk(
        0x8,
        (
            "#11Pオッケー。\x01",
            "それじゃ、連絡してくるわね。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x4)
    SetChrPos(0x8, -5000, 100, 49500, 90)
    Sound(820, 0, 100, 0)
    OP_0D()

    def lambda_14163():
        OP_95(0xFE, 0, 0, 50000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_14163)
    Sleep(300)
    SetChrSubChip(0x104, 0x0)
    Sleep(500)
    SetChrSubChip(0x101, 0x2)
    Sleep(500)
    SetChrSubChip(0x104, 0x2)
    WaitChrThread(0x8, 1)
    StopBGM(0x1F40)

    def lambda_1419B():
        OP_95(0xFE, 0, -500, 48000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1419B)
    Sleep(700)

    def lambda_141B8():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_141B8)
    WaitChrThread(0x8, 1)
    WaitChrThread(0x8, 2)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    Sleep(1000)

    #C1014
    ChrTalk(
        0x102,
        (
            "#6P#0102Fあ、相変わらずの\x01",
            "フットワークの良さですね……\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x9, 0x0)
    Sleep(300)

    #C1015
    ChrTalk(
        0x9,
        (
            "#5P#1404Fそれが俺たち遊撃士の\x01",
            "最大の強みでもあるからな。\x02\x03",

            "#1405Fそういえば、セルゲイさんは\x01",
            "この事を了解しているのか？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)
    Sleep(150)
    SetChrSubChip(0x104, 0x1)
    Sleep(150)

    #C1016
    ChrTalk(
        0x101,
        (
            "#12P#0004Fええ、協力体制については\x01",
            "既に許可を貰っています。\x02\x03",

            "#0000Fアリオスさんに\x01",
            "よろしくと言ってました。\x02",
        )
    )

    CloseMessageWindow()

    #C1017
    ChrTalk(
        0x9,
        (
            "#5P#1402Fそうか……\x02\x03",

            "#1403F………………………………\x02",
        )
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(600)
    SetCameraDistance(18800, 60000)
    MoveCamera(42, 19, 0, 60000)
    PlayBGM("ed7001", 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(800)

    #C1018
    ChrTalk(
        0x101,
        (
            "#12P#0006F……その、アリオスさん。\x02\x03",

            "警察にいた頃は、課長の下で\x01",
            "働いていたんですよね？\x02\x03",

            "#0001F俺の兄貴と一緒に……\x02",
        )
    )

    CloseMessageWindow()

    #C1019
    ChrTalk(
        0x9,
        (
            "#5P#1402F……ああ。\x02\x03",

            "#1404Fセルゲイさんと、俺と、ガイ……\x02\x03",

            "たった３人で\x01",
            "捜査一課以上の実績を打ち立てた\x01",
            "警察史上最高と謳われたチーム……\x02\x03",

            "#1400Fだが５年前、俺が一身上の都合で\x01",
            "警察を辞めてからチームは解散した。\x02\x03",

            "セルゲイさんは警察学校に異動し、\x01",
            "ガイは捜査一課に移り……\x02\x03",

            "#1403Fその２年後──ガイは殉職を遂げた。\x02",
        )
    )

    CloseMessageWindow()

    #C1020
    ChrTalk(
        0x101,
        "#12P#0008F…………………………………\x02",
    )

    CloseMessageWindow()

    #C1021
    ChrTalk(
        0x103,
        "#0208F#6P…………………………………\x02",
    )

    CloseMessageWindow()

    #C1022
    ChrTalk(
        0x9,
        (
            "#5P#1403F俺が警察を辞めなければ──\x01",
            "無論そんな事を言うつもりはない。\x02\x03",

            "俺は俺の事情と決意をもって\x01",
            "警察とは袂#2Rたもと#を分かったからだ。\x02\x03",

            "#1402Fだが……\x01",
            "それでも未だに思い出す事がある。\x02\x03",

            "あの輝かしい日々を……\x01",
            "クセの強い上司と、破天荒な相棒と\x01",
            "共に過ごした歳月のことをな。\x02\x03",

            "#1404Fフフ──だから正直、\x01",
            "お前たちが羨ましいくらいだ。\x02",
        )
    )

    CloseMessageWindow()

    #C1023
    ChrTalk(
        0x101,
        "#12P#0005Fえ……\x02",
    )

    CloseMessageWindow()

    #C1024
    ChrTalk(
        0x104,
        (
            "#0302F#12Pはは、天下の《風の剣聖》に\x01",
            "そんな事を言われるとはね……\x02",
        )
    )

    CloseMessageWindow()

    #C1025
    ChrTalk(
        0x102,
        (
            "#6P#0106Fどちらかというと\x01",
            "ギルドの風通しの良さが\x01",
            "羨ましいくらいですけど……\x02",
        )
    )

    CloseMessageWindow()

    #C1026
    ChrTalk(
        0x9,
        (
            "#5P#1403F──警察には警察の、\x01",
            "ギルドにはギルドの役割がある。\x02\x03",

            "#1400Fいかなる権力にも屈せず\x01",
            "普遍的な理想としての《正義》を\x01",
            "追い求めるのがギルドなら……\x02\x03",

            "権力という矛盾を抱えながら\x01",
            "それでも《正義》を追求するのが\x01",
            "警察の役割だろう。\x02\x03",

            "#1404Fお前たちが感じてるであろう、\x01",
            "様々な矛盾や理不尽な状況……\x02\x03",

            "かつては俺も感じたものだが、\x01",
            "今となってはそれもまた\x01",
            "価値のある経験だったと思う。\x02",
        )
    )

    CloseMessageWindow()

    #C1027
    ChrTalk(
        0x103,
        (
            "#0205F#6P権力という矛盾を抱えながらも\x01",
            "追求する《正義》……\x02",
        )
    )

    CloseMessageWindow()

    #C1028
    ChrTalk(
        0x101,
        (
            "#12P#0013F……兄貴もそれを\x01",
            "追い求めていたんでしょうか？\x02",
        )
    )

    CloseMessageWindow()

    #C1029
    ChrTalk(
        0x9,
        (
            "#5P#1404Fああ……俺はそう信じている。\x02\x03",

            "#1402Fだからこそセルゲイさんも\x01",
            "支援課の設立に尽力したんだろう。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)

    #C1030
    ChrTalk(
        0x9,
        (
            "#5P#1404Fフ……\x01",
            "説教めいた事を言ったようだ。\x02\x03",

            "#1402Fお前たちはお前たちで\x01",
            "答えを見つけるといいだろう。\x02\x03",

            "多分あいつも\x01",
            "それを望んでいるだろうからな。\x02",
        )
    )

    CloseMessageWindow()

    #C1031
    ChrTalk(
        0x101,
        "#12P#0002F……はい。\x02",
    )

    CloseMessageWindow()

    #C1032
    ChrTalk(
        0x104,
        "#0304F#12Pはは、難しい宿題だな。\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xB, 0x4)
    SetChrFlags(0xB, 0x40)
    OP_A7(0xB, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xB, 0, -500, 47000, 0)
    OP_4B(0xB, 0xFF)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    ClearChrFlags(0xD, 0x4)
    SetChrFlags(0xD, 0x40)
    OP_A7(0xD, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xD, 0, -500, 47000, 0)
    OP_4B(0xD, 0xFF)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    ClearChrFlags(0x14, 0x4)
    SetChrFlags(0x14, 0x40)
    OP_A7(0x14, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x14, 0, -500, 47000, 0)
    ClearChrFlags(0x14, 0x80)
    ClearChrBattleFlags(0x14, 0x8000)
    Sleep(300)
    #Sound(1707, 255, 90, 0)    #voice#Estelle

    #N1033
    NpcTalk(
        0xB,
        "娘の声",
        "#10A#1P#2Sただいま～！\x02",
    )
    #Auto

    Sleep(800)
    OP_63(0x9, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x9, 0x1)
    Sleep(50)
    SetChrSubChip(0x101, 0x2)
    Sleep(50)
    SetChrSubChip(0x104, 0x2)
    Sleep(300)
    Fade(500)
    OP_68(-1000, 900, 49400, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(22500, 0)
    OP_0D()
    BeginChrThread(0xB, 3, 0, 34)
    BeginChrThread(0xD, 3, 0, 35)
    BeginChrThread(0x14, 3, 0, 36)
    Sleep(1500)
    OP_68(-6600, 900, 49400, 3000)
    MoveCamera(0, 21, 0, 3000)
    WaitChrThread(0xB, 3)
    WaitChrThread(0xD, 3)
    WaitChrThread(0x14, 3)
    OP_6F(0x79)

    #C1034
    ChrTalk(
        0x101,
        (
            "#6P#0002Fエステル、ヨシュア。\x01",
            "それにシズクちゃんも……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD0, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_14D3C")

    #C1035
    ChrTalk(
        0x102,
        (
            "#6P#0102Fふふ……\x01",
            "今日はとっても可愛い服ね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14D6C")

    label("loc_14D3C")


    #C1036
    ChrTalk(
        0x102,
        (
            "#6P#0102Fあら……！\x01",
            "可愛い服を着てるわね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14D6C")

    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A1037
    AnonymousTalk(
        0x14,
        (
            "ふふっ……\x01",
            "ありがとうございます。\x02\x03",

            "こんにちは、みなさん。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)

    #C1038
    ChrTalk(
        0x103,
        "#0202F#5Pお邪魔しています。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD0, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_14EF9")

    #C1039
    ChrTalk(
        0x104,
        (
            "#6P#0309Fおーおー、外出日を\x01",
            "満喫してるみたいじゃねえか。\x02",
        )
    )

    CloseMessageWindow()

    #C1040
    ChrTalk(
        0x9,
        (
            "#1404F#5P俺に急用が入ったので\x01",
            "彼らが付き添ってくれたんだ。\x02\x03",

            "#1402Fエステル、ヨシュア。\x01",
            "面倒をかけて済まなかったな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15085")

    label("loc_14EF9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCC, 2)), scpexpr(EXPR_END)), "loc_14FC8")

    #C1041
    ChrTalk(
        0x104,
        (
            "#6P#0309Fそうか、シズクちゃんは\x01",
            "今日が外出日とか言ってたな。\x02",
        )
    )

    CloseMessageWindow()

    #C1042
    ChrTalk(
        0x9,
        (
            "#1404F#5Pああ、俺に急用が入ったので\x01",
            "彼らが付き添ってくれたんだ。\x02\x03",

            "#1402Fエステル、ヨシュア。\x01",
            "面倒をかけて済まなかったな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15085")

    label("loc_14FC8")


    #C1043
    ChrTalk(
        0x104,
        (
            "#6P#0300Fなんだ、今日はシズクちゃんの\x01",
            "外出日だったのか？\x02",
        )
    )

    CloseMessageWindow()

    #C1044
    ChrTalk(
        0x9,
        (
            "#1404F#5Pああ、俺に急用が入ったので\x01",
            "彼らが付き添ってくれたんだ。\x02\x03",

            "#1402Fエステル、ヨシュア。\x01",
            "面倒をかけて済まなかったな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15085")


    #C1045
    ChrTalk(
        0xB,
        (
            "#0802F#11Pえへへ、気にしないで。\x02\x03",

            "#0809Fシズクちゃんと一緒にいられて\x01",
            "すっごくラッキーだったもん。\x02\x03",

            "ホッペがプニプニの所も\x01",
            "存分に堪能させてもらったし！\x02",
        )
    )

    CloseMessageWindow()

    #C1046
    ChrTalk(
        0x14,
        "#11P#6010Fエ、エステルさぁん……\x02",
    )

    CloseMessageWindow()

    #C1047
    ChrTalk(
        0xD,
        (
            "#12P#0906Fまったくもう……\x01",
            "オジサンじゃないんだから。\x02\x03",

            "#0901F──ところで、\x01",
            "ミシェルさんから聞きましたけど……\x02\x03",

            "何でも警察と非公式に\x01",
            "協力することになったとか？\x02",
        )
    )

    CloseMessageWindow()

    #C1048
    ChrTalk(
        0x9,
        (
            "#1403F#5Pああ、他の連中が集まり次第、\x01",
            "説明させてもらおう。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x9, 0x0)
    Sleep(300)

    #C1049
    ChrTalk(
        0x9,
        (
            "#5P#1402Fロイド、できれば\x01",
            "お前たちも同席してくれ。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)
    Sleep(300)

    #C1050
    ChrTalk(
        0x101,
        "#6P#0000Fはい……！\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(22000, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    Sleep(1000)
    SetChrName("")

    #A1051
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "その後、集結した遊撃士たちと\x01",
            "現在の状況確認を行った後……\x02\x03",

            "お互いの役割分担を決めた上で、\x01",
            "ロイド達は一旦、支援課に戻ることにした。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearChrFlags(0x101, 0x4)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    ClearChrFlags(0x102, 0x4)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    ClearChrFlags(0x103, 0x4)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    ClearChrFlags(0x104, 0x4)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    OP_68(-2000, 1400, 3000, 0)
    MoveCamera(45, 23, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(22000, 0)
    SetChrPos(0x101, -2500, 0, 1800, 0)
    SetChrPos(0x102, -1500, 0, 1800, 0)
    SetChrPos(0x103, -3200, 0, 900, 0)
    SetChrPos(0x104, -800, 0, 900, 0)
    SetChrPos(0x14, -2000, 0, 800, 0)
    SetChrChipByIndex(0x9, 0x1)
    SetChrSubChip(0x9, 0x0)
    SetChrPos(0x9, -2600, 0, 4000, 180)
    SetChrPos(0xB, 600, 0, 4200, 225)
    SetChrPos(0xD, 1200, 0, 3600, 225)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    SetChrPos(0x8, -1400, 0, 4000, 180)
    ClearChrFlags(0xF, 0x80)
    ClearChrBattleFlags(0xF, 0x8000)
    SetChrPos(0xF, -400, 0, 5500, 180)
    OP_4B(0xF, 0xFF)
    ClearChrFlags(0x11, 0x80)
    ClearChrBattleFlags(0x11, 0x8000)
    SetChrPos(0x11, -1400, 0, 5800, 180)
    OP_4B(0x11, 0xFF)
    ClearChrFlags(0x12, 0x80)
    ClearChrBattleFlags(0x12, 0x8000)
    SetChrPos(0x12, -2600, 0, 5500, 180)
    OP_4B(0x12, 0xFF)
    ClearChrFlags(0x13, 0x80)
    ClearChrBattleFlags(0x13, 0x8000)
    SetChrPos(0x13, -3600, 0, 5200, 180)
    OP_4B(0x13, 0xFF)
    SetCameraDistance(22500, 1500)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x10)

    #C1052
    ChrTalk(
        0x101,
        (
            "#12P#0004F──それではシズクちゃんは\x01",
            "責任をもって預からせてもらいます。\x02",
        )
    )

    CloseMessageWindow()

    #C1053
    ChrTalk(
        0x102,
        (
            "#12P#0100Fこちらは課長もいますし、\x01",
            "頼りになる警察犬もいますから\x01",
            "どうか安心してください。\x02",
        )
    )

    CloseMessageWindow()

    #C1054
    ChrTalk(
        0x9,
        (
            "#1404F#5Pああ、よろしく頼む。\x02\x03",

            "#1402F──シズク。\x01",
            "いい子で待っていてくれ。\x02",
        )
    )

    CloseMessageWindow()

    #C1055
    ChrTalk(
        0x14,
        (
            "#12P#6000Fうん、お父さん。\x02\x03",

            "#6010F……その……\x01",
            "お父さんたちも気をつけてね。\x02",
        )
    )

    CloseMessageWindow()

    #C1056
    ChrTalk(
        0x9,
        "#1404F#5Pああ、心配するな。\x02",
    )

    CloseMessageWindow()

    #C1057
    ChrTalk(
        0xB,
        (
            "#11P#0806Fうーん、もう少し人手が\x01",
            "足りてれば良かったんだけど。\x02",
        )
    )

    CloseMessageWindow()

    #C1058
    ChrTalk(
        0xD,
        (
            "#0900F#11P全員、捜索に出払うとなると\x01",
            "ここもちょっと無用心だからね。\x02",
        )
    )

    CloseMessageWindow()

    #C1059
    ChrTalk(
        0x101,
        (
            "#12P#0006Fでも、良かったんですか？\x02\x03",

            "#0001F俺たちの方からも\x01",
            "捜索の人手を出した方が……\x02",
        )
    )

    CloseMessageWindow()

    #C1060
    ChrTalk(
        0xF,
        (
            "#5Pハハ、気にするなって。\x02\x03",

            "#5Pそっちは病院の先生から\x01",
            "成分調査の連絡が来るんだろう？\x02",
        )
    )

    CloseMessageWindow()

    #C1061
    ChrTalk(
        0x11,
        (
            "#5P人探しは自分たちに任せて\x01",
            "今後の状況に備えておくがいい。\x02",
        )
    )

    CloseMessageWindow()

    #C1062
    ChrTalk(
        0x12,
        (
            "#5Pうーん、しかし警察の連中と\x01",
            "協力することになるとはねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C1063
    ChrTalk(
        0x13,
        (
            "#1Pふふ、レミフェリアでは別に\x01",
            "珍しい事ではないけれど……\x02\x03",

            "よろしくお願いするわね、皆さん。\x02",
        )
    )

    CloseMessageWindow()

    #C1064
    ChrTalk(
        0x104,
        "#12P#0309Fいや～、こちらこそ！\x02",
    )

    CloseMessageWindow()

    #C1065
    ChrTalk(
        0x103,
        "#12P#0204F#Nよろしくお願いします。\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C1066
    ChrTalk(
        0x8,
        (
            "#5P何かあったら遠慮なく\x01",
            "ギルドに連絡してきて頂戴。\x02\x03",

            "#5Pこちらも何か分かったら\x01",
            "支援課に連絡させてもらうから。\x02",
        )
    )

    CloseMessageWindow()

    #C1067
    ChrTalk(
        0xB,
        (
            "#11P#0800Fそれじゃあ、\x01",
            "お互い頑張りましょ！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xB, 500)

    #C1068
    ChrTalk(
        0x101,
        "#6P#0000Fああ……！\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(22000, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    OP_CA(0x1, 0xFF, 0x0)
    SetScenarioFlags(0x5C, 1)
    NewScene("c1000", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_33_13798 end

    def Function_34_159A2(): pass

    label("Function_34_159A2")


    def lambda_159A7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_159A7)

    def lambda_159B8():
        OP_95(0xFE, 0, 0, 50000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_159B8)
    WaitChrThread(0xB, 1)

    def lambda_159D6():
        OP_95(0xFE, -4800, 0, 50000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_159D6)
    WaitChrThread(0xB, 1)
    OP_93(0xB, 0xE1, 0x1F4)
    Return()

    # Function_34_159A2 end

    def Function_35_159F7(): pass

    label("Function_35_159F7")

    Sleep(600)

    def lambda_159FF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_159FF)

    def lambda_15A10():
        OP_95(0xFE, 0, 0, 50000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_15A10)
    WaitChrThread(0xD, 1)

    def lambda_15A2E():
        OP_95(0xFE, -2700, 0, 50000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_15A2E)
    WaitChrThread(0xD, 1)

    def lambda_15A4C():
        OP_95(0xFE, -3300, 0, 49400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_15A4C)
    WaitChrThread(0xD, 1)
    OP_93(0xD, 0x10E, 0x1F4)
    Return()

    # Function_35_159F7 end

    def Function_36_15A6D(): pass

    label("Function_36_15A6D")

    Sleep(1200)

    def lambda_15A75():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_15A75)

    def lambda_15A86():
        OP_95(0xFE, 0, 0, 50500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_15A86)
    WaitChrThread(0x14, 1)

    def lambda_15AA4():
        OP_95(0xFE, -3900, 0, 50500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_15AA4)
    WaitChrThread(0x14, 1)
    OP_93(0x14, 0xE1, 0x1F4)
    Return()

    # Function_36_15A6D end

    def Function_37_15AC5(): pass

    label("Function_37_15AC5")

    TalkBegin(0xFF)
    SetChrName("")

    #A1069
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "遊撃士協会に対する依頼が\x01",
            "数多く張り出されている。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_15B74")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15B74")

    #C1070
    ChrTalk(
        0x104,
        (
            "#0305F結構デカイ仕事も\x01",
            "入ってるみたいだなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C1071
    ChrTalk(
        0x101,
        "#0003Fやっぱ流石だよな……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)

    label("loc_15B74")

    TalkEnd(0xFF)
    Return()

    # Function_37_15AC5 end

    SaveToFile()

Try(main)
