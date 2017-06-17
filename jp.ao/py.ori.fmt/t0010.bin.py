from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t0010.bin",                # FileName
        "t0010",                    # MapName
        "t0010",                    # Location
        0x0037,                     # MapIndex
        "ed7120",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x19,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 55, 0, 2, 0, 3],
    )

    BuildStringList((
        "t0010",                  # 0
        "ミリア",                 # 1
        "ドナルド",               # 2
        "アンジェ",               # 3
        "トルタ村長",             # 4
        "エナ夫人",               # 5
        "デリック",               # 6
        "エルキン",               # 7
        "ハロルド",               # 8
        "ピート",                 # 9
        "トルタ村長",             # 10
        "ゲバル",                 # 11
        "アルム",                 # 12
        "エアリー",               # 13
    ))

    AddCharChip((
        "chr/ch24002.itc",                   # 00
        "chr/ch45400.itc",                   # 01
        "chr/ch09302.itc",                   # 02
        "chr/ch24300.itc",                   # 03
        "chr/ch32300.itc",                   # 04
        "chr/ch23702.itc",                   # 05
        "chr/ch24202.itc",                   # 06
        "chr/ch24100.itc",                   # 07
        "chr/ch24400.itc",                   # 08
        "chr/ch22200.itc",                   # 09
        "chr/ch24302.itc",                   # 0A
        "chr/ch24000.itc",                   # 0B
        "chr/ch47700.itc",                   # 0C
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

    DeclNpc(519,     180,     -1850,   180,  261,  0x0, 0,   5,   0,   255, 255, 0,   4,   255,  0)
    DeclNpc(38409,   180,     540,     180,  261,  0x0, 0,   6,   0,   255, 255, 0,   5,   255,  0)
    DeclNpc(33700,   0,       -2619,   204,  261,  0x0, 0,   3,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(-38479,  180,     -1779,   90,   325,  0x0, 0,   0,   0,   255, 255, 0,   8,   255,  0)
    DeclNpc(-81620,  0,       3410,    0,    261,  0x0, 0,   7,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(-38049,  0,       -140,    180,  389,  0x0, 0,   4,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(-1139,   0,       2380,    90,   389,  0x0, 0,   8,   0,   0,   1,   0,   14,  255,  0)
    DeclNpc(-34200,  180,     -1529,   270,  389,  0x0, 0,   2,   0,   0,   0,   0,   15,  255,  0)
    DeclNpc(-34400,  0,       -300,    270,  389,  0x0, 0,   9,   0,   0,   0,   0,   16,  255,  0)
    DeclNpc(76569,   0,       -2180,   0,    389,  0x0, 0,   11,  0,   0,   0,   0,   8,   255,  0)
    DeclNpc(75800,   0,       2000,    0,    389,  0x0, 0,   12,  0,   0,   0,   0,   17,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    ChipFrameInfo(792, 0)                                        # 0

    ScpFunction((
        "Function_0_318",          # 00, 0
        "Function_1_3D0",          # 01, 1
        "Function_2_3FB",          # 02, 2
        "Function_3_65A",          # 03, 3
        "Function_4_693",          # 04, 4
        "Function_5_165E",         # 05, 5
        "Function_6_2378",         # 06, 6
        "Function_7_2480",         # 07, 7
        "Function_8_2F6F",         # 08, 8
        "Function_9_41DD",         # 09, 9
        "Function_10_4529",        # 0A, 10
        "Function_11_47CA",        # 0B, 11
        "Function_12_550F",        # 0C, 12
        "Function_13_58F2",        # 0D, 13
        "Function_14_5B16",        # 0E, 14
        "Function_15_5C11",        # 0F, 15
        "Function_16_60F2",        # 10, 16
        "Function_17_623D",        # 11, 17
        "Function_18_62DD",        # 12, 18
        "Function_19_6D6F",        # 13, 19
        "Function_20_729F",        # 14, 20
        "Function_21_73E5",        # 15, 21
        "Function_22_7E8B",        # 16, 22
        "Function_23_819B",        # 17, 23
        "Function_24_8F2D",        # 18, 24
        "Function_25_9BFB",        # 19, 25
        "Function_26_A31F",        # 1A, 26
        "Function_27_B6A5",        # 1B, 27
        "Function_28_B6F0",        # 1C, 28
        "Function_29_B73B",        # 1D, 29
        "Function_30_B786",        # 1E, 30
        "Function_31_B7D1",        # 1F, 31
        "Function_32_B81C",        # 20, 32
        "Function_33_B867",        # 21, 33
        "Function_34_B8C6",        # 22, 34
        "Function_35_B8F5",        # 23, 35
        "Function_36_B90C",        # 24, 36
        "Function_37_B923",        # 25, 37
        "Function_38_C016",        # 26, 38
        "Function_39_C061",        # 27, 39
    ))


    def Function_0_318(): pass

    label("Function_0_318")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_358"),
        (1, "loc_364"),
        (2, "loc_370"),
        (3, "loc_37C"),
        (4, "loc_388"),
        (5, "loc_394"),
        (6, "loc_3A0"),
        (SWITCH_DEFAULT, "loc_3AC"),
    )


    label("loc_358")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_3B8")

    label("loc_364")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_3B8")

    label("loc_370")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_3B8")

    label("loc_37C")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_3B8")

    label("loc_388")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_3B8")

    label("loc_394")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_3B8")

    label("loc_3A0")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_3B8")

    label("loc_3AC")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_3B8")

    label("loc_3B8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3CF")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_3B8")

    label("loc_3CF")

    Return()

    # Function_0_318 end

    def Function_1_3D0(): pass

    label("Function_1_3D0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3FA")
    OP_94(0xFE, 0xFFFFF326, 0xB68, 0x100E, 0xFFFFFEDE, 0x7D0)
    Sleep(250)
    Jump("Function_1_3D0")

    label("loc_3FA")

    Return()

    # Function_1_3D0 end

    def Function_2_3FB(): pass

    label("Function_2_3FB")

    SetChrChipByIndex(0xB, 0x0)
    SetChrSubChip(0xB, 0x0)
    EndChrThread(0xB, 0x0)
    SetChrBattleFlags(0xB, 0x4)
    SetChrChipByIndex(0x8, 0x5)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    SetChrChipByIndex(0x9, 0x6)
    SetChrSubChip(0x9, 0x0)
    EndChrThread(0x9, 0x0)
    SetChrBattleFlags(0x9, 0x4)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_4CB")
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, -47480, 0, -1230, 90)
    SetChrChipByIndex(0xB, 0xB)
    ClearChrBattleFlags(0xB, 0x4)
    ClearChrFlags(0xB, 0x40)
    BeginChrThread(0xB, 0, 0, 0)
    SetChrPos(0xB, -46490, 0, -1230, 270)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AD, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_490")
    SetChrFlags(0xD, 0x10)
    SetChrFlags(0xB, 0x10)

    label("loc_490")

    SetChrChipByIndex(0xA, 0xA)
    SetChrSubChip(0xA, 0x0)
    EndChrThread(0xA, 0x0)
    SetChrBattleFlags(0xA, 0x4)
    SetChrPos(0xA, 38320, 180, -2250, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4C6")
    SetChrFlags(0x9, 0x10)
    SetChrFlags(0xA, 0x10)

    label("loc_4C6")

    Jump("loc_5FA")

    label("loc_4CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_4D9")
    Jump("loc_5FA")

    label("loc_4D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_END)), "loc_4E7")
    Jump("loc_5FA")

    label("loc_4E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_4F5")
    Jump("loc_5FA")

    label("loc_4F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_51E")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x90, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_519")
    SetChrFlags(0xB, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)

    label("loc_519")

    Jump("loc_5FA")

    label("loc_51E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_540")
    SetChrFlags(0xB, 0x10)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x10)
    ClearChrFlags(0xE, 0x80)
    Jump("loc_5FA")

    label("loc_540")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_584")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_57A")
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xF, 0x80)
    SetChrChipByIndex(0xF, 0x2)
    SetChrSubChip(0xF, 0x0)
    EndChrThread(0xF, 0x0)
    SetChrBattleFlags(0xF, 0x4)
    ClearChrFlags(0x10, 0x80)
    Jump("loc_57F")

    label("loc_57A")

    SetChrFlags(0xB, 0x80)

    label("loc_57F")

    Jump("loc_5FA")

    label("loc_584")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_5B4")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_5AF")
    ClearChrFlags(0xF, 0x80)
    SetChrChipByIndex(0xF, 0x2)
    SetChrSubChip(0xF, 0x0)
    EndChrThread(0xF, 0x0)
    SetChrBattleFlags(0xF, 0x4)

    label("loc_5AF")

    Jump("loc_5FA")

    label("loc_5B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_5C2")
    Jump("loc_5FA")

    label("loc_5C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_5D5")
    SetChrFlags(0xA, 0x80)
    Jump("loc_5FA")

    label("loc_5D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_5E3")
    Jump("loc_5FA")

    label("loc_5E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_5F1")
    Jump("loc_5FA")

    label("loc_5F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_5FA")

    label("loc_5FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_60E")
    ClearScenarioFlags(0x22, 0)
    Event(0, 18)
    Jump("loc_659")

    label("loc_60E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_622")
    ClearScenarioFlags(0x22, 1)
    Event(0, 23)
    Jump("loc_659")

    label("loc_622")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 2)), scpexpr(EXPR_END)), "loc_636")
    ClearScenarioFlags(0x22, 2)
    Event(0, 24)
    Jump("loc_659")

    label("loc_636")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 3)), scpexpr(EXPR_END)), "loc_64A")
    ClearScenarioFlags(0x22, 3)
    Event(0, 26)
    Jump("loc_659")

    label("loc_64A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 4)), scpexpr(EXPR_END)), "loc_659")
    ClearScenarioFlags(0x22, 4)
    Event(0, 37)

    label("loc_659")

    Return()

    # Function_2_3FB end

    def Function_3_65A(): pass

    label("Function_3_65A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_END)), "loc_66C")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x233), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_66C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_692")
    SetMapObjFrame(0xFF, "hikari_add", 0x0, 0x1)
    Sound(128, 1, 50, 0)

    label("loc_692")

    Return()

    # Function_3_65A end

    def Function_4_693(): pass

    label("Function_4_693")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_811")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_778")

    #C0001
    ChrTalk(
        0xFE,
        (
            "クロスベル市で\x01",
            "大統領が拘束されたらしいわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0xFE,
        (
            "自由に動けるようになった\x01",
            "ギルドの遊撃士さんが、\x01",
            "早速村に来てくれたわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0xFE,
        (
            "こんな状況だけど、\x01",
            "クロスベル全体で力をあわせて\x01",
            "いかなくっちゃね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_80C")

    label("loc_778")


    #C0004
    ChrTalk(
        0xFE,
        (
            "自由に動けるようになった\x01",
            "ギルドの遊撃士さんが、\x01",
            "早速村に来てくれたわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0xFE,
        (
            "こんな状況だけど、\x01",
            "クロスベル全体で力をあわせて\x01",
            "いかなくっちゃね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_80C")

    Jump("loc_165A")

    label("loc_811")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_992")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8EE")

    #C0006
    ChrTalk(
        0xFE,
        (
            "最近、デリックが安否確認も兼ねて\x01",
            "よく村の家を訪ねて回ってるの。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0xFE,
        (
            "こんな状況だし、\x01",
            "知りあいの顔が見れるだけでも\x01",
            "結構安心できるものよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0xFE,
        (
            "真面目でしっかりしている\x01",
            "デリックらしいわ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_98D")

    label("loc_8EE")


    #C0009
    ChrTalk(
        0xFE,
        (
            "最近、デリックが安否確認も兼ねて\x01",
            "よく村の家を訪ねて回ってるの。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0xFE,
        (
            "知りあいの顔が見れるだけでも\x01",
            "結構安心できるものよね。\x01",
            "ふふ、デリックらしいというか。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_98D")

    Jump("loc_165A")

    label("loc_992")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_B34")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A91")

    #C0011
    ChrTalk(
        0xFE,
        (
            "弟のエルキンが\x01",
            "毎日『ドライブができない』って\x01",
            "ため息ばかりなのよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0xFE,
        (
            "ただでさえ窮屈な状況に\x01",
            "気が滅入ってるのに、\x01",
            "グチグチグチグチ……\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0xFE,
        (
            "こんな状況下で\x01",
            "毎日新鮮な食事を食べられるだけ、\x01",
            "ありがたいと思いなさいっての。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_B2F")

    label("loc_A91")


    #C0014
    ChrTalk(
        0xFE,
        (
            "弟のエルキンが\x01",
            "毎日『ドライブができない』って\x01",
            "ため息ばかりなのよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0xFE,
        (
            "こんな状況下で\x01",
            "毎日新鮮な食事を食べられるだけ、\x01",
            "ありがたいと思いなさいっての。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B2F")

    Jump("loc_165A")

    label("loc_B34")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_BCB")

    #C0016
    ChrTalk(
        0xFE,
        (
            "最近、古戦場の辺りで\x01",
            "鎧みたいなのをつけた\x01",
            "ヘンな魔獣を見かけるのよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0xFE,
        (
            "どこかの金持ちが飼ってた魔獣が\x01",
            "逃げちゃったのかしら……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_165A")

    label("loc_BCB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_CE0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C74")

    #C0018
    ChrTalk(
        0xFE,
        (
            "私たち農家にとって、\x01",
            "雨は作物を育ててくれる\x01",
            "天からの恵みよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0xFE,
        (
            "女神様のおかげで\x01",
            "私たちもゴハンを食べられる。\x01",
            "ちゃんと感謝しなきゃね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_CDB")

    label("loc_C74")


    #C0020
    ChrTalk(
        0xFE,
        (
            "私たち農家にとって、\x01",
            "雨は作物を育ててくれる\x01",
            "天の恵みなの。\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0xFE,
        (
            "女神様に\x01",
            "ちゃんと感謝しなきゃね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CDB")

    Jump("loc_165A")

    label("loc_CE0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_F4D")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E4F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DCB")

    #C0022
    ChrTalk(
        0xFE,
        (
            "デリックが進めてる村の改革……\x01",
            "私にはあまりピンとこないのよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0xFE,
        (
            "畑にも導力器を導入して、\x01",
            "色々と楽になるらしいけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0xFE,
        (
            "私、畑仕事好きだからなぁ。\x01",
            "機械に仕事を取られるのは複雑かも。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_E4A")

    label("loc_DCB")


    #C0025
    ChrTalk(
        0xFE,
        (
            "村を改革して、\x01",
            "色々と便利になっていくのは\x01",
            "いいんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0xFE,
        (
            "私、畑仕事好きだからなぁ。\x01",
            "便利になりすぎるのは複雑かも。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E4A")

    Jump("loc_F48")

    label("loc_E4F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EF0")

    #C0027
    ChrTalk(
        0xFE,
        (
            "あのミンネスって人には、\x01",
            "村人全員が騙されてたわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0xFE,
        (
            "世の中には、\x01",
            "平気で人を騙そうなんて\x01",
            "考える人もいる……\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0xFE,
        "一つ勉強になったわね。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_F48")

    label("loc_EF0")


    #C0030
    ChrTalk(
        0xFE,
        (
            "世の中には、\x01",
            "平気で人を騙そうなんて\x01",
            "考える人もいる……\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0xFE,
        "一つ勉強になったわね。\x02",
    )

    CloseMessageWindow()

    label("loc_F48")

    Jump("loc_165A")

    label("loc_F4D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_116F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x174, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10B6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_104D")

    #C0032
    ChrTalk(
        0xFE,
        (
            "エルキンなら、今は街へ\x01",
            "作物を出荷しに行ってるわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0xFE,
        (
            "最近、なんだか舞い上がっててね。\x01",
            "よく寄り道してドライブしながら\x01",
            "帰ってくるのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0xFE,
        (
            "まあ、あんな物を\x01",
            "安く手に入れることができて、\x01",
            "うれしいのは分かるけどね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_10B1")

    label("loc_104D")


    #C0035
    ChrTalk(
        0xFE,
        (
            "エルキンなら、今は街へ\x01",
            "出荷に行ってるわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0xFE,
        (
            "もうしばらくしたら\x01",
            "帰ってくるんじゃないかしら。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10B1")

    Jump("loc_116A")

    label("loc_10B6")


    #C0037
    ChrTalk(
        0xFE,
        (
            "エルキンのやつ、ミンネスさんに\x01",
            "導力トラックを安く譲ってもらってから\x01",
            "ずっと浮かれちゃってるのよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0xFE,
        (
            "気持ちは分かるけど……\x01",
            "事故とかあわないように\x01",
            "よく言っておかなくちゃ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_116A")

    Jump("loc_165A")

    label("loc_116F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1338")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12B7")

    #C0039
    ChrTalk(
        0xFE,
        (
            "この村の村長は、代々村人の中から\x01",
            "多数決で相応しい人が選ばれてるの。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0xFE,
        (
            "次期村長は、村長の息子のデリックが\x01",
            "相応しいって村のみんなが認めてるけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0xFE,
        (
            "デリックって真面目だから、\x01",
            "何でも難しく考えちゃうのよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0xFE,
        (
            "村の将来について考えるのは\x01",
            "いいことだけど……\x01",
            "少しは私たちにも頼ってほしいわ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1333")

    label("loc_12B7")


    #C0043
    ChrTalk(
        0xFE,
        (
            "デリックって真面目だから、\x01",
            "何でも難しく考えちゃうのよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0xFE,
        (
            "このまま１人で悩んで、\x01",
            "ロクなことにならないといいけど。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1333")

    Jump("loc_165A")

    label("loc_1338")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_14FB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_146D")

    #C0045
    ChrTalk(
        0xFE,
        (
            "エルキンの訛りは、\x01",
            "『アルモリカ訛り』って言ってね。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0xFE,
        (
            "村ではドナルドおじさんと\x01",
            "エルキンくらいしか喋らない、\x01",
            "昔から伝わってきた訛りなのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0xFE,
        (
            "『これぞアルモリカ村人』って\x01",
            "感じがするから、ムリに直さなくて\x01",
            "いいと思うんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0xFE,
        (
            "男って、どうでもいいことで\x01",
            "悩むわよね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_14F6")

    label("loc_146D")


    #C0049
    ChrTalk(
        0xFE,
        (
            "エルキンのアルモリカ訛りは、\x01",
            "昔から伝わってきた\x01",
            "ある意味貴重な訛りなのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0xFE,
        (
            "私は嫌いじゃないし、\x01",
            "ムリに直さなくていいと思うわ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14F6")

    Jump("loc_165A")

    label("loc_14FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_165A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15DE")

    #C0051
    ChrTalk(
        0xFE,
        (
            "近頃は本当に平和なのよね。\x01",
            "雨の日も適度にあるから\x01",
            "作物もよく育つし……\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0xFE,
        (
            "今日みたいな天気のいい日は\x01",
            "日向ぼっこが気持ちいいわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0xFE,
        (
            "うーん、導力トラックの上に\x01",
            "ワラでもしいて昼寝しようかしら。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_165A")

    label("loc_15DE")


    #C0054
    ChrTalk(
        0xFE,
        (
            "今日みたいな天気のいい日は\x01",
            "日向ぼっこが気持ちいいわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0xFE,
        (
            "うーん、導力トラックの上に\x01",
            "ワラでもしいて昼寝しようかしら。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_165A")

    TalkEnd(0xFE)
    Return()

    # Function_4_693 end

    def Function_5_165E(): pass

    label("Function_5_165E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_16FF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_167C")
    Call(0, 6)
    Jump("loc_16FA")

    label("loc_167C")


    #C0056
    ChrTalk(
        0xFE,
        "はあ、アンジェの言う通りだな。\x02",
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0xFE,
        (
            "村の食糧を維持するためにも、\x01",
            "オラたち農家はしっかりと\x01",
            "働いていかなきゃなんねえだよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16FA")

    Jump("loc_2374")

    label("loc_16FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_189E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_180A")

    #C0058
    ChrTalk(
        0xFE,
        (
            "独立宣言の後、クロスベル市には\x01",
            "村からのトラックは\x01",
            "行けなくなってしまったけんど……\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0xFE,
        (
            "クロスベル市にも、\x01",
            "新鮮な野菜を楽しみにしている人は\x01",
            "絶対にいるはずだべ。\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0xFE,
        (
            "そんな人たちに\x01",
            "農作物を届けられないのは、\x01",
            "生産者として心苦しいべよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1899")

    label("loc_180A")


    #C0061
    ChrTalk(
        0xFE,
        (
            "クロスベル市にも、\x01",
            "新鮮な野菜を楽しみにしていた人は\x01",
            "絶対にいるはずだべ。\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0xFE,
        (
            "今回の無効宣言が、取引きの再開に\x01",
            "繋がってくれればいいだが。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1899")

    Jump("loc_2374")

    label("loc_189E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_1A28")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_199C")

    #C0063
    ChrTalk(
        0xFE,
        (
            "《幻獣》って怪物が\x01",
            "街道にある畑を荒らすだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0xFE,
        (
            "移動制限もあいまって\x01",
            "収穫もかなり落ち込んでるし、\x01",
            "正直商売あがったりだべ。\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0xFE,
        (
            "まあ、それでも村の中だけなら\x01",
            "なんとか自給自足で賄えてるだ。\x01",
            "女神に感謝しないといけねえな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1A23")

    label("loc_199C")


    #C0066
    ChrTalk(
        0xFE,
        (
            "村の中だけならなんとか\x01",
            "自給自足で賄っていけてるだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0xFE,
        (
            "ただ、こんな状況が\x01",
            "いつまで続いてくれるか……\x01",
            "正直オラにも分からんだよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A23")

    Jump("loc_2374")

    label("loc_1A28")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1B39")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1ADE")

    #C0068
    ChrTalk(
        0xFE,
        (
            "街が襲撃されちまうなんて\x01",
            "びっくらこいただよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0xFE,
        (
            "しかも襲撃犯たちは\x01",
            "まだ捕まってねぇらしいだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0xFE,
        (
            "アルモリカ村に来やしねえか、\x01",
            "不安で仕方ねえべ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1B34")

    label("loc_1ADE")


    #C0071
    ChrTalk(
        0xFE,
        (
            "街の襲撃事件以来、\x01",
            "なんだか不安でよぉ。\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0xFE,
        (
            "はあ、畑仕事にも\x01",
            "身が入んねえだよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B34")

    Jump("loc_2374")

    label("loc_1B39")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1C30")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1BE5")

    #C0073
    ChrTalk(
        0xFE,
        (
            "今日は、カミーユたちは\x01",
            "宿酒場で日曜学校の授業だべ。\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0xFE,
        (
            "オラは農業のことくれえしか\x01",
            "教えらんねえからなぁ。\x01",
            "ちゃんと勉強してきてほしいだよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1C2B")

    label("loc_1BE5")


    #C0075
    ChrTalk(
        0xFE,
        "さて、今日は農業も休みだァ。\x02",
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0xFE,
        "久々に家でゆっくりとするべよ。\x02",
    )

    CloseMessageWindow()

    label("loc_1C2B")

    Jump("loc_2374")

    label("loc_1C30")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1E54")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CE7")

    #C0077
    ChrTalk(
        0xFE,
        (
            "ミンネスさんは、\x01",
            "古道の途中にある私有地にも\x01",
            "何か建てるつもりらしいだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0xFE,
        (
            "あそこは農耕用具置き場に\x01",
            "してたんだが……\x01",
            "まあ、移動させるしかねえだなあ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E4F")

    label("loc_1CE7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1DBF")

    #C0079
    ChrTalk(
        0xFE,
        (
            "あのミンネスって男は、\x01",
            "ホンに悪いヤツだったなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0xFE,
        (
            "オラも、あの笑顔と態度に\x01",
            "すっかり騙されてただよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0xFE,
        (
            "……しかし、当事者の\x01",
            "デリック君はきっとショックだべ。\x01",
            "思いつめてなきゃいいだが……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1E4F")

    label("loc_1DBF")


    #C0082
    ChrTalk(
        0xFE,
        (
            "村のことを一番に思っている\x01",
            "デリック君を騙すなんて、\x01",
            "ホンに悪いヤツだったべ。\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0xFE,
        (
            "あのミンネスって男、\x01",
            "今度見かけたら\x01",
            "とっちめてやるだよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E4F")

    Jump("loc_2374")

    label("loc_1E54")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1ED8")

    #C0084
    ChrTalk(
        0xFE,
        (
            "最近よく村に来る外国のひとは、\x01",
            "なかなか朗らかな方でな。\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0xFE,
        (
            "いつもニコニコしてて、\x01",
            "なんていうか、安心するだよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2374")

    label("loc_1ED8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_205A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1FC0")

    #C0086
    ChrTalk(
        0xFE,
        (
            "エルキンくんから\x01",
            "導力トラックについて\x01",
            "相談されてただが……\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0xFE,
        (
            "たぶん、もうそろそろ寿命だべ。\x01",
            "修理してもすぐ壊れちまうだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0xFE,
        (
            "エルキンくんが\x01",
            "特に大事にしてたから、\x01",
            "ヘコんじまわなきゃいいけんど。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2055")

    label("loc_1FC0")


    #C0089
    ChrTalk(
        0xFE,
        (
            "村の導力トラックは\x01",
            "たぶん、もう寿命だべ。\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0xFE,
        (
            "村のミラも余裕はないだろうから、\x01",
            "村長には相談しづらいだが……\x01",
            "早いうちに買い替えないとだめだァ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2055")

    Jump("loc_2374")

    label("loc_205A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2202")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_214F")

    #C0091
    ChrTalk(
        0xFE,
        (
            "世の中には、農業用の導力器\x01",
            "なんてものもあるだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0xFE,
        (
            "畑を耕すための導力耕転機や、\x01",
            "収穫用の導力トラクター……\x01",
            "農業やるにゃあ、必要不可欠だべ。\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0xFE,
        (
            "まあ、アルモリカ村に置いてるのは\x01",
            "みんなボロっちい旧式だけどなァ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_21FD")

    label("loc_214F")


    #C0094
    ChrTalk(
        0xFE,
        (
            "導力耕転機に導力トラクター……\x01",
            "今の時代、導力器は\x01",
            "農業にも必要不可欠なモンだァ。\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0xFE,
        (
            "欲を言やあ、もっと便利な\x01",
            "最新型が欲しいもんだが……\x01",
            "まあ、そりゃ贅沢ってもんだべ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_21FD")

    Jump("loc_2374")

    label("loc_2202")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2374")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22E5")

    #C0096
    ChrTalk(
        0xFE,
        (
            "おら、村の畑で\x01",
            "色々な野菜とか作ってるだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0xFE,
        (
            "アルモリカでできた野菜は\x01",
            "お天道様の光をたっぷり浴びて、\x01",
            "そりゃあうめえだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0xFE,
        (
            "クロスベル市にも出荷してっから、\x01",
            "おいしく食べてくれると嬉しいだ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2374")

    label("loc_22E5")


    #C0099
    ChrTalk(
        0xFE,
        (
            "アルモリカ産の野菜は、\x01",
            "お天道様の光をたっぷり浴びて、\x01",
            "そりゃあうめえだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0xFE,
        (
            "最近は輸入も増えたけんど、\x01",
            "おいしさじゃ絶対に負けねえだ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2374")

    TalkEnd(0xFE)
    Return()

    # Function_5_165E end

    def Function_6_2378(): pass

    label("Function_6_2378")

    OP_4B(0x9, 0xFF)
    OP_4B(0xA, 0xFF)

    #C0101
    ChrTalk(
        0x9,
        (
            "はあああ……\x01",
            "まさかあんなもんが\x01",
            "クロスベルに現れるとは……\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x9,
        (
            "不安で農作業にも\x01",
            "手がつかなくなっちまっただ……\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0xA,
        (
            "はあ、何を情けない事を\x01",
            "言ってるんだい。\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0xA,
        (
            "こんな時だからこそ、\x01",
            "カミーユやプーリーのために\x01",
            "必死で働かなきゃ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    ClearChrFlags(0x9, 0x10)
    ClearChrFlags(0xA, 0x10)
    OP_4C(0x9, 0xFF)
    OP_4C(0xA, 0xFF)
    Return()

    # Function_6_2378 end

    def Function_7_2480(): pass

    label("Function_7_2480")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2531")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_249E")
    Call(0, 6)
    Jump("loc_252C")

    label("loc_249E")


    #C0105
    ChrTalk(
        0xFE,
        (
            "この人は、ちょっと\x01",
            "気の弱い所があるから\x01",
            "時々尻を叩いてやんないと。\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0xFE,
        (
            "人間、こんな時だからこそ\x01",
            "必死で働いていくのが\x01",
            "大事ってもんだよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_252C")

    Jump("loc_2F6B")

    label("loc_2531")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_268B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_25DD")

    #C0107
    ChrTalk(
        0xFE,
        (
            "今日はコリンくんも\x01",
            "うちのチビたちと\x01",
            "遊んでくれてるみたいだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0xFE,
        (
            "ハロルドさんにはお世話になってるし、\x01",
            "今日はあたしがご馳走しようかねえ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2686")

    label("loc_25DD")


    #C0109
    ChrTalk(
        0xFE,
        (
            "ハロルドさんにはお世話になってるし、\x01",
            "今日はあたしがご馳走しようかねえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0xFE,
        (
            "はは、毎日ソフィアさんの料理を\x01",
            "食べているコリンくんには\x01",
            "物足りないかもしれないけどね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2686")

    Jump("loc_2F6B")

    label("loc_268B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_27DB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2768")

    #C0111
    ChrTalk(
        0xFE,
        (
            "ハロルドさんの奥さんは\x01",
            "本当にお料理が上手な人でねえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0xFE,
        (
            "何でも、街にあるご自宅で\x01",
            "お料理教室なんかを\x01",
            "開いてるそうじゃないか。\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0xFE,
        (
            "こんな状況じゃなけりゃ、\x01",
            "あたしも通ってみたいもんだよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_27D6")

    label("loc_2768")


    #C0114
    ChrTalk(
        0xFE,
        (
            "ハロルドさんの奥さんは\x01",
            "本当にお料理が上手な人でねえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0xFE,
        (
            "子供も歳が近いし、\x01",
            "仲良くさせてもらってるよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_27D6")

    Jump("loc_2F6B")

    label("loc_27DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_294D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_28C3")

    #C0116
    ChrTalk(
        0xFE,
        (
            "襲撃事件の被害は、\x01",
            "本当に甚大だったみたいだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0xFE,
        (
            "……ああ、やだやだ。\x01",
            "こんな話題ばっかりで、\x01",
            "気が滅入っちまっていけないよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0xFE,
        (
            "こんなときこそ、\x01",
            "いつも通りの日常を送って\x01",
            "元気よく過ごさないとね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2948")

    label("loc_28C3")


    #C0119
    ChrTalk(
        0xFE,
        (
            "襲撃事件で出た被害の話を聞くと、\x01",
            "どうも気が滅入っちまう。\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0xFE,
        (
            "こんなときこそ、\x01",
            "いつも通りの日常を送るのが\x01",
            "一番大事だと思うよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2948")

    Jump("loc_2F6B")

    label("loc_294D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2A9C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A27")

    #C0121
    ChrTalk(
        0xFE,
        (
            "昨日の事件を通じて、\x01",
            "村長さんとデリックが\x01",
            "仲直りしたみたいでね。\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0xFE,
        (
            "２人とも、村のことを\x01",
            "第一に考えてる人間だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0xFE,
        (
            "最近さびれてきたこの村も、\x01",
            "これからきっと\x01",
            "よくなっていくだろうさ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2A97")

    label("loc_2A27")


    #C0124
    ChrTalk(
        0xFE,
        (
            "村長とデリックは、村のことを\x01",
            "第一に考えてる人間だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0xFE,
        (
            "この村も、これからきっと\x01",
            "よくなっていくだろうさ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A97")

    Jump("loc_2F6B")

    label("loc_2A9C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2BA8")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B2A")

    #C0126
    ChrTalk(
        0xFE,
        (
            "それにしても、\x01",
            "村の改革んてモンが\x01",
            "こんな急に進むとはねえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0xFE,
        (
            "これもミンネスさんの\x01",
            "手腕ってやつなのかねえ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2BA3")

    label("loc_2B2A")


    #C0128
    ChrTalk(
        0xFE,
        (
            "あのミンネスってやつが\x01",
            "魔獣を放すとは\x01",
            "思いも寄らなかったけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0xFE,
        (
            "とにかく、子供たちに\x01",
            "怪我がなくてよかったよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2BA3")

    Jump("loc_2F6B")

    label("loc_2BA8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2C5F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x174, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2BE4")

    #C0130
    ChrTalk(
        0xFE,
        "さ～て、今日は何を作るかねぇ。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2C5A")

    label("loc_2BE4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x174, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2BF6")
    Call(0, 22)
    Jump("loc_2C5A")

    label("loc_2BF6")


    #C0131
    ChrTalk(
        0xFE,
        (
            "いやあ、あの人は\x01",
            "なかなかできた人だよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0xFE,
        (
            "子供にも優しいし、\x01",
            "悪い人じゃないと思うけどねえ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C5A")

    Jump("loc_2F6B")

    label("loc_2C5F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2E01")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D54")

    #C0133
    ChrTalk(
        0xFE,
        (
            "畑じゃ、たまに形の悪い\x01",
            "野菜や果物が取れるんだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0xFE,
        (
            "そういうのは売り物にならないから、\x01",
            "村人で分け合って食べてるんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0xFE,
        (
            "どんなに形は悪くても、\x01",
            "味は変わらず美味しいんだから。\x01",
            "おかげで家計は助かってるよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2DFC")

    label("loc_2D54")


    #C0136
    ChrTalk(
        0xFE,
        (
            "形の悪い野菜や果物は\x01",
            "店じゃ買い取ってくれないから、\x01",
            "村人同士で分けて食べてるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0xFE,
        (
            "こんなに美味しいのに\x01",
            "形が悪いから買わないなんて、\x01",
            "都会人の気が知れないよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2DFC")

    Jump("loc_2F6B")

    label("loc_2E01")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2E0F")
    Jump("loc_2F6B")

    label("loc_2E0F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2F6B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2EEE")

    #C0138
    ChrTalk(
        0xFE,
        (
            "最近、アレサさんが\x01",
            "正式にこっちに引っ越してね。\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0xFE,
        (
            "息子さんがウチのチビどもと\x01",
            "遊んでくれて、本当に助かるよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0xFE,
        (
            "今は宿の部屋を間借りしてる\x01",
            "みたいだし、ちょくちょく\x01",
            "挨拶しに行こうかねえ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2F6B")

    label("loc_2EEE")


    #C0141
    ChrTalk(
        0xFE,
        (
            "ステファンくんは、\x01",
            "ウチのチビどもとよく\x01",
            "遊んでくれてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0xFE,
        (
            "もともと子供が少ない村だし、\x01",
            "いい友達ができてよかったよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F6B")

    TalkEnd(0xFE)
    Return()

    # Function_7_2480 end

    def Function_8_2F6F(): pass

    label("Function_8_2F6F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x90, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x90, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x90, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19B, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19B, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2F9C")
    Call(0, 25)
    Return()

    label("loc_2F9C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x174, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2FC1")
    Call(0, 19)
    Return()

    label("loc_2FC1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3187")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AD, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2FDF")
    Call(0, 13)
    Jump("loc_3182")

    label("loc_2FDF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_30E0")

    #C0143
    ChrTalk(
        0xFE,
        (
            "ハロルド君が\x01",
            "先ほど街に戻っていってな。\x02",
        )
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0xFE,
        (
            "今後の村の対応を\x01",
            "デリックと話し合っていたんじゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0xFE,
        (
            "ハロルド君にはもうしばらく\x01",
            "残ってもらいたかったが……\x02",
        )
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0xFE,
        (
            "今は各地を回って出来ることを\x01",
            "したいと言っておった。\x01",
            "……致し方あるまいな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3182")

    label("loc_30E0")


    #C0147
    ChrTalk(
        0xFE,
        (
            "……村の今後の対応もあるし、\x01",
            "ハロルド君にはもうしばらく\x01",
            "残ってもらいたかったが……\x02",
        )
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0xFE,
        (
            "ともあれ、遊撃士殿も\x01",
            "来てくれていることだし、\x01",
            "わしらも頑張らねばな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3182")

    Jump("loc_41D9")

    label("loc_3187")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_330E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3277")

    #C0149
    ChrTalk(
        0xFE,
        (
            "独立の無効宣言が出されて、\x01",
            "デリックが色々と動いてくれておる。\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0xFE,
        (
            "此度の状況……\x01",
            "長く村長を務めてきたわしでも\x01",
            "何が起こるか分からん。\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0xFE,
        (
            "とにかく、各人ができる事を\x01",
            "しっかりとやっていくのが\x01",
            "大事じゃろうな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3309")

    label("loc_3277")


    #C0152
    ChrTalk(
        0xFE,
        (
            "此度の状況……\x01",
            "長く村長を務めてきたわしでも\x01",
            "何が起こるか分からん。\x02",
        )
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0xFE,
        (
            "とにかく、各人ができる事を\x01",
            "しっかりとやっていくのが\x01",
            "大事じゃろうな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3309")

    Jump("loc_41D9")

    label("loc_330E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_END)), "loc_3461")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_33DF")

    #C0154
    ChrTalk(
        0xFE,
        (
            "ふむ、まさか古戦場に\x01",
            "そのような者達がいたとは……\x02",
        )
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0xFE,
        (
            "油断のならん相手のようだが、\x01",
            "村に手を出すつもりは\x01",
            "なさそうじゃな。\x02",
        )
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0xFE,
        (
            "アルモリカ村としては、\x01",
            "ひとまず静観するとしよう。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_345C")

    label("loc_33DF")


    #C0157
    ChrTalk(
        0xFE,
        (
            "古戦場に潜んでいる者達は、\x01",
            "村に手を出すつもりは\x01",
            "なさそうじゃな。\x02",
        )
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0xFE,
        (
            "アルモリカ村としては、\x01",
            "ひとまず静観するとしよう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_345C")

    Jump("loc_41D9")

    label("loc_3461")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_360B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3594")

    #C0159
    ChrTalk(
        0xFE,
        (
            "ディーター大統領には正直、\x01",
            "付いていけないものを感じる。\x02",
        )
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0xFE,
        (
            "かといって、この村の影響力など\x01",
            "クロスベル市の人口に比べれば\x01",
            "あって無いようなもの……\x02",
        )
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0xFE,
        (
            "……とにかく、\x01",
            "ハロルド君の一家も\x01",
            "協力してくれていることだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0xFE,
        (
            "村全体で協力してこの困難を\x01",
            "乗り切っていくほかあるまいな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3606")

    label("loc_3594")


    #C0163
    ChrTalk(
        0xFE,
        (
            "ハロルド君の一家も\x01",
            "協力してくれていることだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0xFE,
        (
            "村全体で協力してこの困難を\x01",
            "乗り切っていくほかあるまいな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3606")

    Jump("loc_41D9")

    label("loc_360B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_391A")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x90, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_3770")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_36F3")

    #C0165
    ChrTalk(
        0xFE,
        (
            "ふふ、色々と大変な時じゃが……\x01",
            "おかげで心が温まったのう。\x02",
        )
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0xFE,
        (
            "ともあれ、ゲバル殿のことは、\x01",
            "わしに任せてくれたまえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0xFE,
        (
            "彼が落ち着いて市内に戻れるまで、\x01",
            "きちんと面倒は見させてもらうよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_376B")

    label("loc_36F3")


    #C0168
    ChrTalk(
        0xFE,
        (
            "ゲバル殿のことは、\x01",
            "わしに任せてくれたまえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0xFE,
        (
            "彼が落ち着いて市内に戻れるまで、\x01",
            "きちんと面倒は見させてもらうよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_376B")

    Jump("loc_3915")

    label("loc_3770")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3878")

    #C0170
    ChrTalk(
        0xFE,
        (
            "先日の街の襲撃事件……\x01",
            "アルモリカ村の住民にも、\x01",
            "不安が広がっておるようじゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0xFE,
        (
            "帝国の陰謀説も流れておるが、\x01",
            "確たる証拠がない以上は\x01",
            "鵜呑みにするのもはばかられる……\x02",
        )
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0xFE,
        (
            "……とにかく今は、\x01",
            "村周辺の警戒を怠らないように\x01",
            "しておかなければな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3915")

    label("loc_3878")


    #C0173
    ChrTalk(
        0xFE,
        (
            "デリック含む、村の若い衆が\x01",
            "周辺の警戒にあたってくれておる。\x02",
        )
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0xFE,
        (
            "村の住民たちにこれ以上、\x01",
            "不安な思いをさせない為にも……\x01",
            "警戒を怠らないようにせねばな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3915")

    Jump("loc_41D9")

    label("loc_391A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_39C7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16F, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3935")
    Call(0, 10)
    Jump("loc_39C2")

    label("loc_3935")


    #C0175
    ChrTalk(
        0xFE,
        (
            "ふむ、村の特色を\x01",
            "皆に知ってもらうというのは\x01",
            "決して悪くはないじゃろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0xFE,
        (
            "興味を持ってもらえれば、\x01",
            "村への移住も増えるかもしれんし……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_39C2")

    Jump("loc_41D9")

    label("loc_39C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3B62")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_39E2")
    Jump("loc_3B5D")

    label("loc_39E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x177, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_39F1")
    Jump("loc_3B5D")

    label("loc_39F1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A03")
    Jump("loc_3B5D")

    label("loc_3A03")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3AD3")

    #C0177
    ChrTalk(
        0xFE,
        "このアルモリカという村を守る……\x02",
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0xFE,
        (
            "目的は同じだったのに、わしも息子も\x01",
            "視野が狭くなりすぎていたのじゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0xFE,
        (
            "今回の事件は、それに気づかせるために\x01",
            "女神が与えた試練だったのじゃろうな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3B5D")

    label("loc_3AD3")


    #C0180
    ChrTalk(
        0xFE,
        (
            "このアルモリカという村を守る……\x01",
            "わしも息子も、その気持ちは同じじゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0xFE,
        (
            "これからは、若い者の言葉にも\x01",
            "しかと耳を傾けねばならんな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3B5D")

    Jump("loc_41D9")

    label("loc_3B62")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3DE5")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B7D")
    Jump("loc_3DE0")

    label("loc_3B7D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x174, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B8C")
    Jump("loc_3DE0")

    label("loc_3B8C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3CD2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3C4F")

    #C0182
    ChrTalk(
        0xFE,
        (
            "デリックと密談する外国人……\x01",
            "どうもキナ臭い匂いがするのじゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0xFE,
        (
            "何か悪い企みがあるなら、\x01",
            "早急に対処せねばならん。\x02",
        )
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0xFE,
        "君たち、どうか情報を集めてきてくれ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3CCD")

    label("loc_3C4F")


    #C0185
    ChrTalk(
        0xFE,
        (
            "デリックと密談する外国人……\x01",
            "何か悪い企みがあるなら、\x01",
            "早急に対処せねばならん。\x02",
        )
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0xFE,
        "君たち、どうか情報を集めてきてくれ。\x02",
    )

    CloseMessageWindow()

    label("loc_3CCD")

    Jump("loc_3DE0")

    label("loc_3CD2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D84")

    #C0187
    ChrTalk(
        0xFE,
        (
            "君たち、本当にご苦労だったな。\x01",
            "おかげでおおよそのことを\x01",
            "知る事ができたわい。\x02",
        )
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0xFE,
        (
            "あとは村長として、\x01",
            "なんとかデリックと話をして\x01",
            "説得してみることにしよう。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3DE0")

    label("loc_3D84")


    #C0189
    ChrTalk(
        0xFE,
        (
            "村長として、親として……\x01",
            "デリックが早まったことをする前に、\x01",
            "なんとか説得しなければな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3DE0")

    Jump("loc_41D9")

    label("loc_3DE5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3FA0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14F, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E00")
    Call(0, 9)
    Jump("loc_3F9B")

    label("loc_3E00")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F0F")

    #C0190
    ChrTalk(
        0xFE,
        (
            "若者が離れていくことによる\x01",
            "人手不足、貿易の活発化に伴う\x01",
            "自治州内食料自給率の低下……\x02",
        )
    )

    CloseMessageWindow()

    #C0191
    ChrTalk(
        0xFE,
        (
            "村が抱える問題は山積みだが……\x01",
            "デリックの改革案をおいそれと\x01",
            "採用するわけにもいかん。\x02",
        )
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0xFE,
        (
            "村の伝統を守るのも村長の使命じゃ。\x01",
            "そこを分かってほしいものだが……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3F9B")

    label("loc_3F0F")


    #C0193
    ChrTalk(
        0xFE,
        (
            "村の伝統を守るのも村長の使命。\x01",
            "変化することはいいことばかりではない。\x02",
        )
    )

    CloseMessageWindow()

    #C0194
    ChrTalk(
        0xFE,
        (
            "デリックも次期村長として、\x01",
            "そこを分かってほしいものだが……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3F9B")

    Jump("loc_41D9")

    label("loc_3FA0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_413B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14F, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3FBB")
    Call(0, 9)
    Jump("loc_4136")

    label("loc_3FBB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_40B5")

    #C0195
    ChrTalk(
        0xFE,
        (
            "改革に盲目的になって\x01",
            "村の伝統をないがしろにしては、\x01",
            "災いを招いてしまうじゃろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0xFE,
        (
            "デリックが村の為を思って\x01",
            "改革案を出しているのは\x01",
            "充分に分かっておるが……\x02",
        )
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0xFE,
        (
            "村があるべき姿を\x01",
            "見失わないためにも、\x01",
            "もっと慎重に考えねばな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4136")

    label("loc_40B5")


    #C0198
    ChrTalk(
        0xFE,
        (
            "……村の状況、わしとて\x01",
            "このままでいいとは思わん。\x02",
        )
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0xFE,
        (
            "だが、村があるべき姿を\x01",
            "見失わないためにも、\x01",
            "もっと慎重に考えねばな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4136")

    Jump("loc_41D9")

    label("loc_413B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_41D9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14F, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4156")
    Call(0, 9)
    Jump("loc_41D9")

    label("loc_4156")


    #C0200
    ChrTalk(
        0xFE,
        (
            "……この悩みは、そもそも\x01",
            "わし自身が解決すべき問題じゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0xFE,
        (
            "もし何かあったら\x01",
            "頼むかもしれんが……\x01",
            "今は心配せんでくれたまえ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_41D9")

    TalkEnd(0xFE)
    Return()

    # Function_8_2F6F end

    def Function_9_41DD(): pass

    label("Function_9_41DD")


    #C0202
    ChrTalk(
        0xB,
        "おお、君たちは特務支援課の……\x02",
    )

    CloseMessageWindow()

    #C0203
    ChrTalk(
        0x101,
        "#00000Fトルタ村長、ご無沙汰しています。\x02",
    )

    CloseMessageWindow()

    #C0204
    ChrTalk(
        0xB,
        (
            "はは、活動を\x01",
            "再開したと聞いていたが、\x01",
            "息災なようでなによりじゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0205
    ChrTalk(
        0xB,
        "……ふう……\x02",
    )

    CloseMessageWindow()

    #C0206
    ChrTalk(
        0x102,
        (
            "#00105Fあの……\x01",
            "なんだかお疲れのようですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0207
    ChrTalk(
        0xB,
        (
            "いや……最近、少しばかり\x01",
            "個人的な問題で悩んでいてな。\x02",
        )
    )

    CloseMessageWindow()

    #C0208
    ChrTalk(
        0xB,
        (
            "まあ、諸君の手を\x01",
            "煩わせるほどのことではないよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0209
    ChrTalk(
        0x109,
        (
            "#10102Fそんな、悩みがあるなら\x01",
            "おっしゃったほうが……\x02",
        )
    )

    CloseMessageWindow()

    #C0210
    ChrTalk(
        0x104,
        (
            "#00300Fああ、溜め込むのは\x01",
            "体に毒だぜ？\x02",
        )
    )

    CloseMessageWindow()

    #C0211
    ChrTalk(
        0x105,
        (
            "#10304Fフフ、僕ら特務支援課なら\x01",
            "力になれるかもしれないしね。\x02",
        )
    )

    CloseMessageWindow()

    #C0212
    ChrTalk(
        0xB,
        (
            "はは、本当に\x01",
            "大したことじゃないんじゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0213
    ChrTalk(
        0xB,
        (
            "本当にどうにもならなくなったら\x01",
            "君たちに頼むかもしれんが、\x01",
            "今は心配せんでくれたまえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0214
    ChrTalk(
        0x101,
        (
            "#00003Fそうですか……\x01",
            "分かりました。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_44C8")

    #C0215
    ChrTalk(
        0x103,
        (
            "#00200F何かあったら\x01",
            "いつでもご連絡ください。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_44FC")

    label("loc_44C8")


    #C0216
    ChrTalk(
        0x102,
        (
            "#00100F何かあったら\x01",
            "いつでもご連絡くださいね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_44FC")


    #C0217
    ChrTalk(
        0xB,
        (
            "ああ、そのときは\x01",
            "よろしく頼むぞい。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x14F, 1)
    Return()

    # Function_9_41DD end

    def Function_10_4529(): pass

    label("Function_10_4529")

    OP_4B(0xB, 0xFF)
    OP_4B(0xD, 0xFF)

    #C0218
    ChrTalk(
        0xB,
        (
            "デリック、お前が出した\x01",
            "『養蜂業の体験イベント』\x01",
            "という案じゃが……\x02",
        )
    )

    CloseMessageWindow()

    #C0219
    ChrTalk(
        0xB,
        (
            "確かに魅力はあるかもしれんが、\x01",
            "素人を畑に入れていいもんかのう？\x02",
        )
    )

    CloseMessageWindow()

    #C0220
    ChrTalk(
        0xD,
        (
            "それはもちろんあるが……\x01",
            "ハチミツは村の特産だし、\x01",
            "悪くはないと思うんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0xD,
        (
            "ハチへの対策も、\x01",
            "俺たちで教えていけると思うし……\x02",
        )
    )

    CloseMessageWindow()

    #C0222
    ChrTalk(
        0xB,
        "ふむ、一考の余地はあるか……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_471C")

    #C0223
    ChrTalk(
        0x101,
        (
            "#00002F（どうやら、村長とデリックさんは\x01",
            "  完全に和解できたみたいだな。）\x02",
        )
    )

    CloseMessageWindow()

    #C0224
    ChrTalk(
        0x102,
        (
            "#00104F（『雨降って地固まる』という事ね。\x01",
            "  ふふ、邪魔しちゃ悪いし行きましょう。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_47BE")

    label("loc_471C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_47BE")

    #C0225
    ChrTalk(
        0x101,
        (
            "#00005F（あれ、村長とデリックさん……\x01",
            "  いつの間にか和解したみたいだな。）\x02",
        )
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0x102,
        (
            "#00104F（ミンネスの件を通して\x01",
            "  何かあったのかもしれないわね。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_47BE")

    SetScenarioFlags(0x16F, 6)
    OP_4C(0xB, 0xFF)
    OP_4C(0xD, 0xFF)
    Return()

    # Function_10_4529 end

    def Function_11_47CA(): pass

    label("Function_11_47CA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_490B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_487D")

    #C0227
    ChrTalk(
        0xFE,
        (
            "あの青白く光る大樹を見ると、\x01",
            "とても不安な気持ちになるわ……\x02",
        )
    )

    CloseMessageWindow()

    #C0228
    ChrTalk(
        0xFE,
        (
            "でも、夫やデリックが\x01",
            "頑張ってくれてるんですもの。\x01",
            "私も応援していかなくちゃね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4906")

    label("loc_487D")


    #C0229
    ChrTalk(
        0xFE,
        (
            "夫やデリックに限らず、\x01",
            "今この状況下で沢山の人が\x01",
            "頑張っている事でしょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0230
    ChrTalk(
        0xFE,
        (
            "大した事はできないけど、\x01",
            "私も応援していかなくちゃね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4906")

    Jump("loc_550B")

    label("loc_490B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_49C6")

    #C0231
    ChrTalk(
        0xFE,
        (
            "独立国の無効宣言が出たということは、\x01",
            "ディーター大統領という存在の\x01",
            "正当性が揺らいだということよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0232
    ChrTalk(
        0xFE,
        (
            "クロスベル市にいる人たちは、\x01",
            "さぞ混乱していることでしょうね……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_550B")

    label("loc_49C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_4B74")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4AD0")

    #C0233
    ChrTalk(
        0xFE,
        (
            "あのアリオスさんが\x01",
            "国防長官になってしまうなんて……\x01",
            "未だに信じられないわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0234
    ChrTalk(
        0xFE,
        (
            "この村は、遊撃士の皆さんに\x01",
            "とてもお世話になっていたのだけど、\x01",
            "独立以来はろくに連絡もとれていないの。\x02",
        )
    )

    CloseMessageWindow()

    #C0235
    ChrTalk(
        0xFE,
        (
            "心配だわ……皆さん、\x01",
            "今はどうしているのかしら。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4B6F")

    label("loc_4AD0")


    #C0236
    ChrTalk(
        0xFE,
        (
            "この村は、遊撃士の皆さんに\x01",
            "とてもお世話になっていたのだけど、\x01",
            "独立以来はろくに連絡もとれていないの。\x02",
        )
    )

    CloseMessageWindow()

    #C0237
    ChrTalk(
        0xFE,
        (
            "心配だわ……皆さん、\x01",
            "今はどうしているのかしら。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4B6F")

    Jump("loc_550B")

    label("loc_4B74")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_4C0D")

    #C0238
    ChrTalk(
        0xFE,
        (
            "デリックたちは、率先して\x01",
            "村周辺の見回りをしてくれてるの。\x02",
        )
    )

    CloseMessageWindow()

    #C0239
    ChrTalk(
        0xFE,
        (
            "得体の知れない化物も\x01",
            "目撃されているっていうし、\x01",
            "気をつけてほしいわ……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_550B")

    label("loc_4C0D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_4DE8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4D42")

    #C0240
    ChrTalk(
        0xFE,
        (
            "昨日の夜から、夫とデリックは\x01",
            "村の新しい改革案について\x01",
            "色々と話し合っているの。\x02",
        )
    )

    CloseMessageWindow()

    #C0241
    ChrTalk(
        0xFE,
        (
            "ただ変化するのではなく、\x01",
            "村の伝統的な魅力を伝えることで\x01",
            "活気を取り戻そうとしているみたいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0242
    ChrTalk(
        0xFE,
        (
            "あの２人が手を取り合えば、\x01",
            "きっとアルモリカ村は良くなるわ。\x01",
            "ふふ、私もしっかりと支えなくちゃ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4DE3")

    label("loc_4D42")


    #C0243
    ChrTalk(
        0xFE,
        (
            "さてと、夫とデリックに\x01",
            "暖かいココアでも淹れましょうか。\x02",
        )
    )

    CloseMessageWindow()

    #C0244
    ChrTalk(
        0xFE,
        (
            "あの２人が手を取り合えば、\x01",
            "きっとアルモリカ村は良くなるわ。\x01",
            "ふふ、私もしっかりと支えなくちゃ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4DE3")

    Jump("loc_550B")

    label("loc_4DE8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_4F8E")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4F20")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4ED3")

    #C0245
    ChrTalk(
        0xFE,
        (
            "夫は、デリックのことで\x01",
            "ハロルドさんの所に\x01",
            "相談しに行っているわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0246
    ChrTalk(
        0xFE,
        (
            "もう私たちだけじゃ\x01",
            "どうすることもできなくて……\x02",
        )
    )

    CloseMessageWindow()

    #C0247
    ChrTalk(
        0xFE,
        (
            "ああ女神さま、\x01",
            "どうかアルモリカ村を、\x01",
            "デリックをお守りください……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4F1B")

    label("loc_4ED3")


    #C0248
    ChrTalk(
        0xFE,
        (
            "ああ女神さま、\x01",
            "どうかアルモリカ村を、\x01",
            "デリックをお守りください……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4F1B")

    Jump("loc_4F89")

    label("loc_4F20")


    #C0249
    ChrTalk(
        0xFE,
        (
            "夫とデリックが、\x01",
            "ようやく和解できたみたいで\x01",
            "私も安心したわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0250
    ChrTalk(
        0xFE,
        (
            "みなさん……\x01",
            "本当にありがとうね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4F89")

    Jump("loc_550B")

    label("loc_4F8E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_50CA")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5036")

    #C0251
    ChrTalk(
        0xFE,
        (
            "近頃、デリックはほとんど\x01",
            "家に顔を見せなくなってしまって……\x02",
        )
    )

    CloseMessageWindow()

    #C0252
    ChrTalk(
        0xFE,
        (
            "ああ、心配だわ。\x01",
            "まさか、おかしなことに\x01",
            "巻き込まれてしまったんじゃ……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_50C5")

    label("loc_5036")


    #C0253
    ChrTalk(
        0xFE,
        (
            "デリックがミンネスという方と\x01",
            "改革の話を進めてたなんて……\x02",
        )
    )

    CloseMessageWindow()

    #C0254
    ChrTalk(
        0xFE,
        (
            "ああ、もう二人の関係は\x01",
            "取り返しがつかないところまで\x01",
            "きてしまったのかしら。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_50C5")

    Jump("loc_550B")

    label("loc_50CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_5206")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_519C")

    #C0255
    ChrTalk(
        0xFE,
        (
            "昨日の夫とデリックの口論は\x01",
            "今までで一番激しかったの。\x02",
        )
    )

    CloseMessageWindow()

    #C0256
    ChrTalk(
        0xFE,
        (
            "２人とも熱くなってしまって、\x01",
            "私もとうとう諌#2Rいさ#められなくて……\x02",
        )
    )

    CloseMessageWindow()

    #C0257
    ChrTalk(
        0xFE,
        (
            "はあ……どうしたら２人は\x01",
            "和解できるのかしら。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_5201")

    label("loc_519C")


    #C0258
    ChrTalk(
        0xFE,
        (
            "はあ……\x01",
            "どうしたらデリックと夫は\x01",
            "和解できるのかしら。\x02",
        )
    )

    CloseMessageWindow()

    #C0259
    ChrTalk(
        0xFE,
        (
            "私にはもう、\x01",
            "どうすればいいのか……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5201")

    Jump("loc_550B")

    label("loc_5206")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_5366")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_52EC")

    #C0260
    ChrTalk(
        0xFE,
        (
            "夫とデリックの口論は、\x01",
            "日増しに激しくなってるの。\x02",
        )
    )

    CloseMessageWindow()

    #C0261
    ChrTalk(
        0xFE,
        (
            "いつもは私がなんとか場を\x01",
            "収めているけれど、それも段々\x01",
            "手に負えなくなってきて……\x02",
        )
    )

    CloseMessageWindow()

    #C0262
    ChrTalk(
        0xFE,
        (
            "はあ、不安だわ。\x01",
            "これ以上悪くならないと\x01",
            "いいのだけれど。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_5361")

    label("loc_52EC")


    #C0263
    ChrTalk(
        0xFE,
        (
            "夫とデリックの口論は、\x01",
            "日増しに激しくなってるの。\x02",
        )
    )

    CloseMessageWindow()

    #C0264
    ChrTalk(
        0xFE,
        (
            "はあ、不安だわ。\x01",
            "これ以上悪くならないと\x01",
            "いいのだけれど。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5361")

    Jump("loc_550B")

    label("loc_5366")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_550B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5475")

    #C0265
    ChrTalk(
        0xFE,
        (
            "ここ最近、夫とデリックは\x01",
            "アルモリカ村の今後について\x01",
            "毎日激しく議論をしているの。\x02",
        )
    )

    CloseMessageWindow()

    #C0266
    ChrTalk(
        0xFE,
        (
            "それ自体はいいのだけど、\x01",
            "どっちも一歩も譲らないから\x01",
            "いつも口論になってしまって……\x02",
        )
    )

    CloseMessageWindow()

    #C0267
    ChrTalk(
        0xFE,
        (
            "このままでは親子の関係が\x01",
            "悪くなるばかりよ。\x01",
            "はあ、頭が痛いわ……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_550B")

    label("loc_5475")


    #C0268
    ChrTalk(
        0xFE,
        (
            "村のために、夫と息子が\x01",
            "議論を交わす事自体は\x01",
            "いいことだと思うけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0269
    ChrTalk(
        0xFE,
        (
            "２人とも頑固だから、\x01",
            "全然決着が付く気配がないの。\x01",
            "はあ、頭が痛いわ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_550B")

    TalkEnd(0xFE)
    Return()

    # Function_11_47CA end

    def Function_12_550F(): pass

    label("Function_12_550F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_56C4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AD, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_552D")
    Call(0, 13)
    Jump("loc_56BF")

    label("loc_552D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5623")

    #C0270
    ChrTalk(
        0xFE,
        (
            "あの巨大な樹木の出現に、\x01",
            "村人達もかなりの不安を\x01",
            "感じているようだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0271
    ChrTalk(
        0xFE,
        (
            "大統領が拘束されたとはいえ、\x01",
            "蒼い花や街道の《幻獣》の問題も\x01",
            "まだ解決していない……\x02",
        )
    )

    CloseMessageWindow()

    #C0272
    ChrTalk(
        0xFE,
        (
            "村人達には引き続き、\x01",
            "注意を呼びかけていく\x01",
            "必要がありそうだな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_56BF")

    label("loc_5623")


    #C0273
    ChrTalk(
        0xFE,
        (
            "大統領が拘束されたとはいえ、\x01",
            "蒼い花や街道の《幻獣》の問題も\x01",
            "まだ解決していない……\x02",
        )
    )

    CloseMessageWindow()

    #C0274
    ChrTalk(
        0xFE,
        (
            "村人達には引き続き、\x01",
            "注意を呼びかけていく\x01",
            "必要がありそうだな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_56BF")

    Jump("loc_58EE")

    label("loc_56C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_56D2")
    Jump("loc_58EE")

    label("loc_56D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_56E0")
    Jump("loc_58EE")

    label("loc_56E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_56EE")
    Jump("loc_58EE")

    label("loc_56EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_5778")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16F, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5709")
    Call(0, 10)
    Jump("loc_5773")

    label("loc_5709")


    #C0275
    ChrTalk(
        0xFE,
        (
            "……ふむ、親父の言う事も\x01",
            "もっともだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0276
    ChrTalk(
        0xFE,
        (
            "それなら、もう少しこの案を\x01",
            "掘り下げていけばよさそうだ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5773")

    Jump("loc_58EE")

    label("loc_5778")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_58EE")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5793")
    Jump("loc_58EE")

    label("loc_5793")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_587A")

    #C0277
    ChrTalk(
        0xFE,
        (
            "村の問題を俺１人で\x01",
            "解決しようとしたのが\x01",
            "そもそもの間違いだった。\x02",
        )
    )

    CloseMessageWindow()

    #C0278
    ChrTalk(
        0xFE,
        (
            "今回の事件で、俺自身の\x01",
            "思慮の浅さを思い知らされたよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0279
    ChrTalk(
        0xFE,
        (
            "これからは親父と……\x01",
            "いや、住民みんなといっしょに\x01",
            "村の事を考えていかないとな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_58EE")

    label("loc_587A")


    #C0280
    ChrTalk(
        0xFE,
        (
            "今回の事件で、俺自身の\x01",
            "思慮の浅さを思い知らされたよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0281
    ChrTalk(
        0xFE,
        (
            "これからは住民みんなで\x01",
            "村の事を考えていかないとな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_58EE")

    TalkEnd(0xFE)
    Return()

    # Function_12_550F end

    def Function_13_58F2(): pass

    label("Function_13_58F2")

    OP_4B(0xD, 0xFF)
    OP_4B(0xB, 0xFF)

    #C0282
    ChrTalk(
        0xB,
        (
            "これほどの事が起こるとは、\x01",
            "誰しもが予想しなかったじゃろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0283
    ChrTalk(
        0xB,
        (
            "貿易都市として発展し、\x01",
            "強引に独立という形をとって\x01",
            "大陸全土に影響を与え……\x02",
        )
    )

    CloseMessageWindow()

    #C0284
    ChrTalk(
        0xB,
        (
            "そうして伝統をないがしろにし、\x01",
            "急すぎる進化を続けてきたことの\x01",
            "揺れ戻しが今、来たのかもしれん。\x02",
        )
    )

    CloseMessageWindow()

    #C0285
    ChrTalk(
        0xD,
        (
            "……だが、それを甘んじて\x01",
            "受け入れるのは違うんじゃないか？\x02",
        )
    )

    CloseMessageWindow()

    #C0286
    ChrTalk(
        0xD,
        (
            "これが女神の与えた試練というなら、\x01",
            "俺達がそれを乗り越えられるか……\x01",
            "試されているのはそれだと思う。\x02",
        )
    )

    CloseMessageWindow()

    #C0287
    ChrTalk(
        0xB,
        "……うむ、そうじゃな。\x02",
    )

    CloseMessageWindow()

    #C0288
    ChrTalk(
        0xB,
        (
            "やれやれ、わしもいい加減\x01",
            "凝り固まった考え方を\x01",
            "改めるべきかもしれんのう。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1AD, 4)
    ClearChrFlags(0xD, 0x10)
    ClearChrFlags(0xB, 0x10)
    OP_4C(0xD, 0xFF)
    OP_4C(0xB, 0xFF)
    Return()

    # Function_13_58F2 end

    def Function_14_5B16(): pass

    label("Function_14_5B16")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_5B27")
    Jump("loc_5C0D")

    label("loc_5B27")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_5BCC")

    #C0289
    ChrTalk(
        0xFE,
        (
            "ミンネスさんから買った新型導力車を\x01",
            "警察に調べてもらってるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0290
    ChrTalk(
        0xFE,
        (
            "何日もしないうちに終わるって\x01",
            "話だったけど……\x01",
            "はあ、早く戻ってこないかなあ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5C0D")

    label("loc_5BCC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_5BDA")
    Jump("loc_5C0D")

    label("loc_5BDA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_5BE8")
    Jump("loc_5C0D")

    label("loc_5BE8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_5BF6")
    Jump("loc_5C0D")

    label("loc_5BF6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_5C04")
    Jump("loc_5C0D")

    label("loc_5C04")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_5C0D")

    label("loc_5C0D")

    TalkEnd(0xFE)
    Return()

    # Function_14_5B16 end

    def Function_15_5C11(): pass

    label("Function_15_5C11")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x174, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5C36")
    Call(0, 19)
    Return()

    label("loc_5C36")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_5C47")
    Jump("loc_60EE")

    label("loc_5C47")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_5DA5")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5C62")
    Jump("loc_5DA0")

    label("loc_5C62")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5C74")
    Jump("loc_5DA0")

    label("loc_5C74")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5D2A")

    #C0291
    ChrTalk(
        0xF,
        (
            "#03603F今回は本当に\x01",
            "ありがとうございました。\x02\x03",

            "#03600Fおかげさまでデリック君と\x01",
            "村長も和解出来たみたいです。\x02\x03",

            "#03609Fふふ、やはり皆さんに\x01",
            "相談して正解でしたね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_5DA0")

    label("loc_5D2A")


    #C0292
    ChrTalk(
        0xF,
        (
            "#03603Fおかげさまでデリック君と\x01",
            "村長も和解出来たみたいです。\x02\x03",

            "#03609Fふふ、やはり皆さんに\x01",
            "相談して正解でしたね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5DA0")

    Jump("loc_60EE")

    label("loc_5DA5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_60EE")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5F53")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5EBE")

    #C0293
    ChrTalk(
        0xF,
        (
            "#03603Fデリック君とは、村との取引きで\x01",
            "何度も顔を合わせていますし、\x01",
            "礼儀正しく真面目な好青年です。\x02\x03",

            "#03608Fそんな彼が何かに巻き込まれて\x01",
            "いるとしたら、私も放ってはおけません。\x02\x03",

            "#03601F皆さん、ぜひとも有益な情報を\x01",
            "手に入れてきてください。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_5F4E")

    label("loc_5EBE")


    #C0294
    ChrTalk(
        0xF,
        (
            "#03608Fデリック君が何かに巻き込まれて\x01",
            "いるとしたら、私も放ってはおけません。\x02\x03",

            "#03601F皆さん、ぜひとも有益な情報を\x01",
            "手に入れてきてください。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5F4E")

    Jump("loc_60EE")

    label("loc_5F53")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6064")

    #C0295
    ChrTalk(
        0xF,
        (
            "#03608Fミンネスという男の真意は\x01",
            "今のところ分からないままですが……\x02\x03",

            "#03603Fこの件に関しては、私も村長と一緒に\x01",
            "慎重に進めていこうと思います。\x02\x03",

            "#03600F皆さん、相談に乗っていただいて\x01",
            "ありがとうございました。\x02\x03",

            "また何かありましたら\x01",
            "よろしくお願いします。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_60EE")

    label("loc_6064")


    #C0296
    ChrTalk(
        0xF,
        (
            "#03603Fこの件に関しては、私も村長と一緒に\x01",
            "慎重に進めていこうと思います。\x02\x03",

            "#03600F皆さん、また何かありましたら\x01",
            "よろしくお願いします。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_60EE")

    TalkEnd(0xFE)
    Return()

    # Function_15_5C11 end

    def Function_16_60F2(): pass

    label("Function_16_60F2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_61CD")

    #C0297
    ChrTalk(
        0xFE,
        (
            "イアン先生は、憲法草案の\x01",
            "作成の関係でどうしても\x01",
            "来ることが出来なかったんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0298
    ChrTalk(
        0xFE,
        (
            "でも、無事に解決したみたいで、\x01",
            "本当に良かったですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0299
    ChrTalk(
        0xFE,
        (
            "先生には僕のほうから\x01",
            "顛末をお伝えしておきますね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_6239")

    label("loc_61CD")


    #C0300
    ChrTalk(
        0xFE,
        (
            "無事に解決したみたいで、\x01",
            "本当に良かったですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0301
    ChrTalk(
        0xFE,
        (
            "先生には僕のほうから\x01",
            "顛末をお伝えしておきますね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6239")

    TalkEnd(0xFE)
    Return()

    # Function_16_60F2 end

    def Function_17_623D(): pass

    label("Function_17_623D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_62BD")

    #C0302
    ChrTalk(
        0xFE,
        (
            "……あの小さかったアルムが、\x01",
            "あんなに立派になっていたとは……\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xFE, 0x0, 0x1F4)

    #C0303
    ChrTalk(
        0xFE,
        "…………グスッ…………\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0x12, 0x10)
    SetScenarioFlags(0x1, 1)
    Jump("loc_62D9")

    label("loc_62BD")


    #C0304
    ChrTalk(
        0xFE,
        "…………グスッ…………\x02",
    )

    CloseMessageWindow()

    label("loc_62D9")

    TalkEnd(0xFE)
    Return()

    # Function_17_623D end

    def Function_18_62DD(): pass

    label("Function_18_62DD")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch00202.itc", 0x1F)
    LoadChrToIndex("chr/ch03102.itc", 0x20)
    LoadChrToIndex("chr/ch02702.itc", 0x21)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x1)
    SetChrFlags(0x101, 0x4)
    SetChrChipByIndex(0x103, 0x1F)
    SetChrSubChip(0x103, 0x1)
    SetChrFlags(0x103, 0x4)
    SetChrChipByIndex(0x105, 0x20)
    SetChrSubChip(0x105, 0x2)
    SetChrFlags(0x105, 0x4)
    SetChrChipByIndex(0x107, 0x21)
    SetChrSubChip(0x107, 0x0)
    BeginChrThread(0x107, 3, 0, 0)
    SetMapObjFrame(0xFF, "kage03", 0x1, 0x1)
    SetMapObjFrame(0xFF, "tuika01", 0x1, 0x1)
    SetMapObjFrame(0xFF, "ha03", 0x0, 0x1)
    SetMapObjFrame(0xFF, "kage02", 0x0, 0x1)
    SetMapObjFrame(0xFF, "tuika00", 0x0, 0x1)
    SetChrPos(0x101, -38500, 200, -1500, 90)
    SetChrPos(0x103, -38500, 200, -2800, 90)
    SetChrPos(0x105, -34300, 200, -1700, 270)
    SetChrPos(0x107, -38700, 0, 600, 90)
    SetChrPos(0xB, -36300, 200, 100, 180)
    OP_68(-36290, 2500, -2150, 0)
    MoveCamera(327, 15, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25000, 0)
    Sleep(1000)
    OP_68(-36290, 1500, -2150, 3000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)

    #C0305
    ChrTalk(
        0xB,
        (
            "#11P──なるほど。\x01",
            "そんな事があったのか。\x02",
        )
    )

    CloseMessageWindow()

    #C0306
    ChrTalk(
        0xB,
        (
            "#11P最初、そちらの狼殿と共に\x01",
            "訪ねてきた時は\x01",
            "腰を抜かすかと思ったが。\x02",
        )
    )

    CloseMessageWindow()

    #C0307
    ChrTalk(
        0x101,
        "#00006F#5Pす、すみません。\x02",
    )

    CloseMessageWindow()

    #C0308
    ChrTalk(
        0x107,
        (
            "#01200F#5P#3Cふむ、どうやら私の\x01",
            "配慮不足だったようだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0309
    ChrTalk(
        0xB,
        (
            "#11Pいやいや、伝説の神狼殿に\x01",
            "こうしてお目にかかれるとは\x01",
            "光栄の至りですわい。\x02",
        )
    )

    CloseMessageWindow()

    #C0310
    ChrTalk(
        0xB,
        (
            "#11P村には《国防軍》とやらも\x01",
            "ほとんど来ることはないし……\x02",
        )
    )

    CloseMessageWindow()

    #C0311
    ChrTalk(
        0xB,
        (
            "#11P好きなだけ滞在してくれると\x01",
            "いいじゃろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0312
    ChrTalk(
        0x101,
        "#00002F#5P……ありがとうございます。\x02",
    )

    CloseMessageWindow()

    #C0313
    ChrTalk(
        0x103,
        "#00204F#6Pとても助かります。\x02",
    )

    CloseMessageWindow()

    #C0314
    ChrTalk(
        0x105,
        (
            "#10406F#12Pしかし病院の方でも\x01",
            "批判的な人は多かったけど……\x02\x03",

            "#10401Fここでもディーター大統領は\x01",
            "あまり評判が良くないみたいだね？\x02",
        )
    )

    CloseMessageWindow()

    #C0315
    ChrTalk(
        0xB,
        (
            "#11Pうむ……元々この村とは\x01",
            "縁の薄い人物ではあるからな。\x02",
        )
    )

    CloseMessageWindow()

    #C0316
    ChrTalk(
        0xB,
        (
            "#11P『独立国』などと言われても\x01",
            "全くピンと来ぬし……\x02",
        )
    )

    CloseMessageWindow()

    #C0317
    ChrTalk(
        0xB,
        (
            "#11P例の《幻獣》が現れたせいで\x01",
            "農作物の収穫も落ち込んでおる。\x02",
        )
    )

    CloseMessageWindow()

    #C0318
    ChrTalk(
        0xB,
        (
            "#11Pなのにたまに国防軍とやらが\x01",
            "見回りに来る程度の対応じゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0319
    ChrTalk(
        0x101,
        "#00006F#5Pそうでしたか……\x02",
    )

    CloseMessageWindow()

    #C0320
    ChrTalk(
        0x103,
        "#00206F#6P……ぞんざいすぎますね。\x02",
    )

    CloseMessageWindow()

    #C0321
    ChrTalk(
        0x107,
        (
            "#01203F#5P#3C街の者が周辺の村里#4Rむらざと#を\x01",
            "省みぬのは世の常……\x02\x03",

            "#01201Fしかし、どうもそれが\x01",
            "行き過ぎているようだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0322
    ChrTalk(
        0xB,
        (
            "#11Pうむ……わしも正直、\x01",
            "付いていけないものを感じる。\x02",
        )
    )

    CloseMessageWindow()

    #C0323
    ChrTalk(
        0xB,
        (
            "#11Pかといって、この村の影響力など\x01",
            "クロスベル市の人口に比べれば\x01",
            "あって無いようなもの……\x02",
        )
    )

    CloseMessageWindow()

    #C0324
    ChrTalk(
        0xB,
        (
            "#11P正直、どうしたものかと\x01",
            "考えあぐねていたところじゃよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0325
    ChrTalk(
        0x105,
        "#10408F#12Pふむ、なるほどね。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)

    #C0326
    ChrTalk(
        0x101,
        (
            "#00003F#5P《幻獣》については\x01",
            "こちらも気を付けておきます。\x02\x03",

            "#00001Fそれ以外に、ここ最近で\x01",
            "何か困ったことはありますか？\x02\x03",

            "村の治安や雰囲気が\x01",
            "悪化していたりとか……\x02",
        )
    )

    CloseMessageWindow()

    #C0327
    ChrTalk(
        0xB,
        (
            "#11Pいや、幸いにして\x01",
            "そこまでには至っていない。\x02",
        )
    )

    CloseMessageWindow()

    #C0328
    ChrTalk(
        0xB,
        (
            "#11P今は村全体で協力して\x01",
            "この困難を乗り切って行こうと\x01",
            "頑張っているところじゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0329
    ChrTalk(
        0xB,
        (
            "#11Pハロルド君の一家も\x01",
            "協力してくれているしな。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0330
    ChrTalk(
        0x101,
        "#00005F#5Pハロルドさん……！？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x192, 0)), scpexpr(EXPR_END)), "loc_6B6D")

    #C0331
    ChrTalk(
        0x103,
        (
            "#00208F#6Pそういえば……\x01",
            "家族で遊びに行くと\x01",
            "言っていたような。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6B9E")

    label("loc_6B6D")


    #C0332
    ChrTalk(
        0x103,
        (
            "#00205F#6Pこちらに一家で\x01",
            "来ているんですか？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6B9E")


    #C0333
    ChrTalk(
        0xB,
        (
            "#11Pうむ、ちょうど異変の時、\x01",
            "一家で遊びに来ておってな。\x02",
        )
    )

    CloseMessageWindow()

    #C0334
    ChrTalk(
        0xB,
        (
            "#11Pその後すぐに\x01",
            "街道の移動制限が出されたから\x01",
            "そのまま留まっているんじゃよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0335
    ChrTalk(
        0x101,
        "#00003F#5Pそうだったんですか……\x02",
    )

    CloseMessageWindow()

    #C0336
    ChrTalk(
        0xB,
        (
            "#11Pハロルド君の一家なら\x01",
            "宿の２階に滞在しておる。\x02",
        )
    )

    CloseMessageWindow()

    #C0337
    ChrTalk(
        0xB,
        "#11Pよかったら顔を出すといい。\x02",
    )

    CloseMessageWindow()

    #C0338
    ChrTalk(
        0x101,
        "#00000F#5Pええ、分かりました。\x02",
    )

    CloseMessageWindow()

    #C0339
    ChrTalk(
        0x105,
        "#10400F#12Pさっそく訪ねてみようか。\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(25250, 1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)
    SetChrChipByIndex(0x107, 0xFF)
    SetChrSubChip(0x107, 0x0)
    EndChrThread(0x107, 0x3)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x103, 0x4)
    ClearChrFlags(0x105, 0x4)
    OP_49()
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_D7(0x20)
    OP_D7(0x21)
    SetChrPos(0x0, -40400, 0, -1800, 270)
    OP_69(0xFF, 0x0)
    SetScenarioFlags(0x1A1, 3)
    OP_29(0xAF, 0x1, 0x4)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_18_62DD end

    def Function_19_6D6F(): pass

    label("Function_19_6D6F")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-37080, 1500, -1060, 0)
    MoveCamera(329, 28, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25000, 0)
    SetChrPos(0x101, -38110, 0, 380, 180)
    SetChrPos(0x102, -37060, 0, 1370, 180)
    SetChrPos(0x103, -39710, 0, -190, 135)
    SetChrPos(0x104, -35620, 0, 1220, 180)
    SetChrPos(0x109, -38610, 0, 2220, 180)
    SetChrPos(0x105, -39730, 0, 1380, 135)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7204")

    #C0340
    ChrTalk(
        0xB,
        (
            "ふう……\x01",
            "デリックのやつめ、\x01",
            "一体何をやっておるのか……\x02",
        )
    )

    CloseMessageWindow()

    #C0341
    ChrTalk(
        0xF,
        (
            "#03603F心配ですね……\x01",
            "もしかすると、彼は……\x02",
        )
    )

    CloseMessageWindow()

    #C0342
    ChrTalk(
        0x101,
        (
            "#00000Fトルタ村長、こんにちは。\x01",
            "特務支援課の者です……\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x87, 0x1F4)
    Sleep(300)

    #C0343
    ChrTalk(
        0x101,
        "#00005Fって……ハロルドさん？\x02",
    )

    CloseMessageWindow()

    def lambda_6F14():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6F14)
    Sleep(50)

    def lambda_6F24():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_6F24)
    Sleep(50)

    def lambda_6F34():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_6F34)
    OP_63(0xB, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0xF, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0xB, 0x1)

    #C0344
    ChrTalk(
        0xB,
        (
            "おお、君たち……\x01",
            "待っていたぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0345
    ChrTalk(
        0xF,
        (
            "#03600F依頼を見て来てくれたんですね。\x01",
            "ありがとうございます。\x02",
        )
    )

    CloseMessageWindow()

    #C0346
    ChrTalk(
        0x101,
        (
            "#00012Fえ、ええ……\x02\x03",

            "#00005Fでも、ハロルドさんまで\x01",
            "なぜここに？\x02",
        )
    )

    CloseMessageWindow()

    #C0347
    ChrTalk(
        0xB,
        (
            "ああ、実は……\x01",
            "今回の件については\x01",
            "彼も関係あってな。\x02",
        )
    )

    CloseMessageWindow()

    #C0348
    ChrTalk(
        0xF,
        (
            "#03603F村長さんと話し合った末、\x01",
            "皆さんに相談することにしたのです。\x02\x03",

            "#03601Fなにせ、事情が事情です。\x01",
            "ここは捜査のプロの方に\x01",
            "頼んだ方がいいと思いまして。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x102, 0xB4, 0x1F4)
    Sleep(300)

    #C0349
    ChrTalk(
        0x102,
        (
            "#00101Fとても深刻そうな\x01",
            "事情みたいですね。\x02\x03",

            "#00103F村長さんの息子さんに\x01",
            "関係する話みたいですけど……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_7166():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7166)
    Sleep(50)

    def lambda_7176():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_7176)
    Sleep(50)

    def lambda_7186():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_7186)
    Sleep(300)

    #C0350
    ChrTalk(
        0xB,
        "うむ、少々込み入っておってな。\x02",
    )

    CloseMessageWindow()

    #C0351
    ChrTalk(
        0xB,
        (
            "引き受けてもらえるなら\x01",
            "詳しく話させてもらうが……\x01",
            "時間は大丈夫かね？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7270")

    label("loc_7204")

    SetChrSubChip(0xB, 0x1)

    #C0352
    ChrTalk(
        0xB,
        "おや、時間ができたのかな？\x02",
    )

    CloseMessageWindow()

    #C0353
    ChrTalk(
        0xB,
        (
            "依頼を引き受けてくれるなら\x01",
            "詳しく話させてもらうが……\x01",
            "大丈夫かね？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7270")

    Call(0, 20)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x0, -41050, 0, -1950, 270)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_19_6D6F end

    def Function_20_729F(): pass

    label("Function_20_729F")

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
            "【引き受ける】\x01",              # 0
            "【準備ができていない】\x01",      # 1
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
        (0, "loc_7315"),
        (1, "loc_731D"),
        (SWITCH_DEFAULT, "loc_73E4"),
    )


    label("loc_7315")

    Call(0, 21)
    Jump("loc_73E4")

    label("loc_731D")


    #C0354
    ChrTalk(
        0x101,
        (
            "#00006F申し訳ありません……\x01",
            "今はちょっと忙しくて。\x02",
        )
    )

    CloseMessageWindow()

    #C0355
    ChrTalk(
        0xB,
        "ううむ、そうかね……\x02",
    )

    CloseMessageWindow()

    #C0356
    ChrTalk(
        0xB,
        (
            "では、時間ができたら\x01",
            "もう一度来てくれ。\x02",
        )
    )

    CloseMessageWindow()

    #C0357
    ChrTalk(
        0xB,
        (
            "どうしても君たちに\x01",
            "力を貸してほしいのだよ。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrSubChip(0xB, 0x0)
    SetScenarioFlags(0x173, 7)
    Jump("loc_73E4")

    label("loc_73E4")

    Return()

    # Function_20_729F end

    def Function_21_73E5(): pass

    label("Function_21_73E5")


    #C0358
    ChrTalk(
        0x101,
        (
            "#00000Fええ、大丈夫です。\x01",
            "ぜひお聞かせください。\x02",
        )
    )

    CloseMessageWindow()

    #C0359
    ChrTalk(
        0xB,
        "ああ、恩に着るぞ。\x02",
    )

    CloseMessageWindow()

    #C0360
    ChrTalk(
        0xB,
        (
            "──実は近頃、息子の\x01",
            "デリックの様子が変でな。\x02",
        )
    )

    CloseMessageWindow()

    #C0361
    ChrTalk(
        0xB,
        (
            "裏でなにやらよからぬことを\x01",
            "目論んでいる様子なのじゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0362
    ChrTalk(
        0x104,
        "#00305Fよからぬことッスか？\x02",
    )

    CloseMessageWindow()

    #C0363
    ChrTalk(
        0xB,
        (
            "詳しくは分からないのだが……\x01",
            "とにかく考えが読めんのじゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0364
    ChrTalk(
        0xB,
        (
            "この間など、勝手にハロルド君に\x01",
            "『今後の取引を遠慮したい』\x01",
            "などと申し出おったらしい。\x02",
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

    #C0365
    ChrTalk(
        0x101,
        (
            "#00005F取引を……\x01",
            "なぜそんな事を急に？\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x87, 0x1F4)
    Sleep(300)

    #C0366
    ChrTalk(
        0x101,
        (
            "#00003F確か、ハロルドさんは\x01",
            "アルモリカ村と友好的な\x01",
            "関係だったはずじゃあ……\x02",
        )
    )

    CloseMessageWindow()

    #C0367
    ChrTalk(
        0xF,
        (
            "#03608Fええ、以前から懇意に\x01",
            "させていただいていた\x01",
            "つもりだったのですが……\x02\x03",

            "#03601Fそれで、何かしら自分に\x01",
            "非があったのだろうと思って\x01",
            "理由を村長に尋ねたんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0368
    ChrTalk(
        0x105,
        (
            "#10303F聞いてみれば、\x01",
            "村長にもまったく持って\x01",
            "身に覚えのない話だった……\x02\x03",

            "#10300Fつまりはそういうことかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0369
    ChrTalk(
        0xB,
        (
            "さよう……\x01",
            "ハロルド君には大変な\x01",
            "失礼を働いてしまった。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0xB4, 0x1F4)
    Sleep(300)

    #C0370
    ChrTalk(
        0xB,
        (
            "彼という良い取引先を失うのは\x01",
            "村にとってかなりの痛手……\x02",
        )
    )

    CloseMessageWindow()

    #C0371
    ChrTalk(
        0xB,
        (
            "それが分からん息子では\x01",
            "ないはずなのだがな。\x02",
        )
    )

    CloseMessageWindow()

    #C0372
    ChrTalk(
        0x102,
        (
            "#00103F確かに不可解ですね……\x02\x03",

            "#00101F息子さんに\x01",
            "何かあったのでしょうか？\x02",
        )
    )

    CloseMessageWindow()

    #C0373
    ChrTalk(
        0xB,
        (
            "うむ、わしもそう思って\x01",
            "ハロルド君と共に\x01",
            "色々と調べておったんじゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0374
    ChrTalk(
        0xB,
        (
            "すると……\x01",
            "ある得体の知れない人物が\x01",
            "浮かび上がってな。\x02",
        )
    )

    CloseMessageWindow()

    #C0375
    ChrTalk(
        0xB,
        (
            "どうも最近、あやつは\x01",
            "不審な外国人と\x01",
            "会っているようなんじゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0376
    ChrTalk(
        0x109,
        "#10105F外国人……ですか？\x02",
    )

    CloseMessageWindow()

    #C0377
    ChrTalk(
        0xF,
        (
            "#03603Fあまり詳しいことは\x01",
            "分からないのですが……\x02\x03",

            "#03601Fただ、どうもデリックさんと\x01",
            "内々に何かを話し合ったり\x01",
            "しているらしいのです。\x02",
        )
    )

    CloseMessageWindow()

    #C0378
    ChrTalk(
        0x105,
        (
            "#10303Fふうん……密談とは、\x01",
            "確かにただならぬ臭いがするね。\x02",
        )
    )

    CloseMessageWindow()

    #C0379
    ChrTalk(
        0xB,
        (
            "そこで、あんたたちには\x01",
            "その外国人について\x01",
            "詳しく調べてもらいたいんじゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0380
    ChrTalk(
        0xB,
        (
            "何か悪い企みがあるなら、\x01",
            "早急に対処せねばならんからな。\x02",
        )
    )

    CloseMessageWindow()

    #C0381
    ChrTalk(
        0x103,
        (
            "#00203F失礼ですが……\x01",
            "今回の件、わざわざ私たちに\x01",
            "依頼するまでもないのでは？\x02\x03",

            "#00200F直接息子さんに話されるのが\x01",
            "一番合理的なはずですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0382
    ChrTalk(
        0x104,
        "#00306Fおいおい、ティオすけ……\x02",
    )

    CloseMessageWindow()

    #C0383
    ChrTalk(
        0xB,
        (
            "……いや、恥ずかしながら\x01",
            "お嬢さんのいう通りじゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0384
    ChrTalk(
        0xB,
        (
            "実は、以前からわしと息子は\x01",
            "村のあり方を巡って\x01",
            "衝突を繰り返しておってな……\x02",
        )
    )

    CloseMessageWindow()

    #C0385
    ChrTalk(
        0xB,
        (
            "この事についても事情を聞いたが、\x01",
            "結局何も答えてくれなんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0386
    ChrTalk(
        0xB,
        "父親としては情けない話だがな。\x02",
    )

    CloseMessageWindow()

    #C0387
    ChrTalk(
        0x102,
        "#00106Fそんなことは……\x02",
    )

    CloseMessageWindow()

    #C0388
    ChrTalk(
        0x101,
        (
            "#00003F……とにかく、話は分かりました。\x01",
            "早速調査にあたらせていただきます。\x02\x03",

            "#00000F手始めに、村の人たちに\x01",
            "聞き込みをしたいと思いますが……\x02",
        )
    )

    CloseMessageWindow()

    #C0389
    ChrTalk(
        0xB,
        "ああ、是非お願いしよう。\x02",
    )

    CloseMessageWindow()

    #C0390
    ChrTalk(
        0xB,
        (
            "ただ、デリックは今\x01",
            "エルキンという青年と共に\x01",
            "街に作物の納入へ行っておる。\x02",
        )
    )

    CloseMessageWindow()

    #C0391
    ChrTalk(
        0xB,
        (
            "本人への聞き込みは\x01",
            "後回しにしたほうがいいじゃろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0392
    ChrTalk(
        0xF,
        (
            "#03600F皆さん、ぜひとも有益な情報を\x01",
            "手に入れてきてください。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x87, 0x1F4)
    Sleep(300)

    #C0393
    ChrTalk(
        0x101,
        "#00000Fええ、お任せください。\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    Sound(80, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0394
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "クエスト【不審人物の調査】\x07\x00",
            "を開始した！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_29(0x82, 0x1, 0x0)
    SetScenarioFlags(0x174, 0)
    SetChrSubChip(0xB, 0x0)
    Return()

    # Function_21_73E5 end

    def Function_22_7E8B(): pass

    label("Function_22_7E8B")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(35510, 1500, -2430, 0)
    MoveCamera(288, 34, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25000, 0)
    SetChrPos(0x101, 34950, 0, -2440, 225)
    SetChrPos(0x102, 34150, 0, -1180, 180)
    SetChrPos(0x103, 35670, 0, -3780, 270)
    SetChrPos(0x104, 35390, 0, -1060, 225)
    SetChrPos(0x109, 34780, 0, 40, 180)
    SetChrPos(0x105, 35960, 0, -2370, 225)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_93(0xA, 0x2D, 0x0)
    FadeToBright(1000, 0)
    OP_0D()

    #C0395
    ChrTalk(
        0x101,
        (
            "#00003Fあの、少々お尋ね\x01",
            "したいのですが……\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    #A0396
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "最近村を訪れているという\x01",
            "外国人について尋ねた。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0397
    ChrTalk(
        0xA,
        "ああ、あの人かい。\x02",
    )

    CloseMessageWindow()

    #C0398
    ChrTalk(
        0xA,
        (
            "そうだねえ……強いて言うなら、\x01",
            "なかなか良くできたお人だよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0399
    ChrTalk(
        0x103,
        "#00205Fよく出来た……ですか？\x02",
    )

    CloseMessageWindow()

    #C0400
    ChrTalk(
        0xA,
        (
            "ああ、一度うちの子供たちが\x01",
            "遊んでいる拍子に、通りかかった\x01",
            "彼の服を汚しちまったんだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0401
    ChrTalk(
        0xA,
        (
            "気にも留めないばかりか、\x01",
            "親切にもお菓子なんか\x01",
            "もらっちゃってねえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0402
    ChrTalk(
        0xA,
        (
            "いやあ、申し訳ないやら\x01",
            "感心したやらで\x01",
            "ため息がでちゃったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0403
    ChrTalk(
        0x101,
        (
            "#00003Fなるほど……\x01",
            "ご協力、ありがとうございます。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetScenarioFlags(0x174, 3)
    OP_29(0x82, 0x1, 0x3)
    SetChrPos(0x0, 34950, 0, -2440, 135)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_22_7E8B end

    def Function_23_819B(): pass

    label("Function_23_819B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-37080, 2500, -1060, 0)
    MoveCamera(329, 27, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25000, 0)
    SetChrPos(0x101, -38110, 0, 380, 180)
    SetChrPos(0x102, -37060, 0, 1370, 180)
    SetChrPos(0x103, -39710, 0, -190, 135)
    SetChrPos(0x104, -35620, 0, 1220, 180)
    SetChrPos(0x109, -38610, 0, 2220, 180)
    SetChrPos(0x105, -39730, 0, 1380, 135)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrSubChip(0xB, 0x1)
    OP_68(-37080, 1500, -1060, 3000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x1)

    #C0404
    ChrTalk(
        0xB,
        (
            "まさか……\x01",
            "そのミンネスという男、\x01",
            "クインシー社の関係者だったとは……\x02",
        )
    )

    CloseMessageWindow()

    #C0405
    ChrTalk(
        0xB,
        (
            "そして……\x01",
            "『アルモリカ・ハニーカンパニー』か。\x02",
        )
    )

    CloseMessageWindow()

    #C0406
    ChrTalk(
        0xF,
        (
            "#03605F私有地に工場を……\x01",
            "そこまで大掛かりな計画が\x01",
            "進んでいたとは……\x02\x03",

            "#03608Fあのデリックくんが、\x01",
            "そんなことを……\x02",
        )
    )

    CloseMessageWindow()

    #C0407
    ChrTalk(
        0x101,
        (
            "#00005Fあの……\x01",
            "ところでその、デリックさんは？\x02",
        )
    )

    CloseMessageWindow()

    #C0408
    ChrTalk(
        0x102,
        (
            "#00105Fあ……そうね。\x01",
            "姿が見えないけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0409
    ChrTalk(
        0x109,
        (
            "#10100Fホテルですれ違ったときは、\x01",
            "村に帰るって言ってましたよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0410
    ChrTalk(
        0xB,
        (
            "うむ……実は最近、\x01",
            "あまり家に居つかぬように\x01",
            "なってしまってな。\x02",
        )
    )

    CloseMessageWindow()

    #C0411
    ChrTalk(
        0xB,
        (
            "最近では《トネリコ亭》で\x01",
            "部屋を借りているらしい。\x02",
        )
    )

    CloseMessageWindow()

    #C0412
    ChrTalk(
        0xB,
        (
            "ミンネスという男も\x01",
            "宿を訪れておったようだし、\x01",
            "そのために移動したのかもしれんな。\x02",
        )
    )

    CloseMessageWindow()

    #C0413
    ChrTalk(
        0xB,
        (
            "おかげで私有地に工場を建てる計画など、\x01",
            "毛ほども気づく事ができんかったわい。\x01",
            "……情けない話じゃがな。\x02",
        )
    )

    CloseMessageWindow()

    #C0414
    ChrTalk(
        0x105,
        (
            "#10303F……どうなんだろうねえ。\x02\x03",

            "#10300F案外、商人に入れ知恵されて\x01",
            "移動したのかもしれないよ？\x02\x03",

            "#10304F村長に情報が届きにくいように。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0xF, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0415
    ChrTalk(
        0xB,
        "ど、どういうことじゃ……？\x02",
    )

    CloseMessageWindow()

    #C0416
    ChrTalk(
        0x105,
        (
            "#10300Fま、ここからは\x01",
            "リーダーが説明してくれるよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0417
    ChrTalk(
        0x101,
        "#00006Fあのな……まあいいけど。\x02",
    )

    CloseMessageWindow()

    #C0418
    ChrTalk(
        0xF,
        (
            "#03605Fロイドさん、\x01",
            "何か気になることでも\x01",
            "あるのですか？\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x87, 0x1F4)
    Sleep(300)

    #C0419
    ChrTalk(
        0x101,
        (
            "#00003F──あくまで、俺たちの\x01",
            "カンのようなものですが……\x02\x03",

            "#00001Fあのミンネスという男には、\x01",
            "怪しい点があります。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0420
    ChrTalk(
        0xB,
        "何じゃと……！？\x02",
    )

    CloseMessageWindow()

    #C0421
    ChrTalk(
        0x101,
        (
            "#00001F彼の語った計画は、\x01",
            "参加した誰もが\x01",
            "利益を得られるものでした。\x02\x03",

            "#00003Fアルモリカ村は新たな産業を得て、\x01",
            "クインシー社は将来に展望ある\x01",
            "子会社を得ることになる。\x02\x03",

            "#00008F一見説得力のあるように\x01",
            "見える彼の話ですが……\x02\x03",

            "#00001F如何せん話がうますぎる。\x01",
            "……そうは思いませんか？\x02",
        )
    )

    CloseMessageWindow()

    #C0422
    ChrTalk(
        0xF,
        (
            "#03605F……！\x01",
            "い、言われて見れば……\x02",
        )
    )

    CloseMessageWindow()

    #C0423
    ChrTalk(
        0x103,
        (
            "#00203Fそれに、ミンネスさんは\x01",
            "新型導力トラックを\x01",
            "安く譲ったりしています。\x02\x03",

            "#00200Fこれはいわゆる、\x01",
            "『先行投資』とも\x01",
            "見る事ができると思います。\x02",
        )
    )

    CloseMessageWindow()

    #C0424
    ChrTalk(
        0x109,
        (
            "#10108F導力車の新型は、\x01",
            "まだまだ高価なのは\x01",
            "間違いありませんからね……\x02\x03",

            "#10101Fさすがに５万ミラで譲渡するというのは、\x01",
            "あたしも破格すぎる気がします。\x02",
        )
    )

    CloseMessageWindow()

    #C0425
    ChrTalk(
        0x104,
        (
            "#00303Fつまり、逆に言えば……\x02\x03",

            "#00301F必ず代金を回収できる\x01",
            "『見込み』がある、\x01",
            "ってことになりそうだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0426
    ChrTalk(
        0xF,
        (
            "#03601Fそれは……\x01",
            "確かにおかしいですね。\x02\x03",

            "#03603Fクインシー社ほどの大企業なら\x01",
            "コストを度外視したプロジェクトを\x01",
            "進めるはずがありませんから。\x02",
        )
    )

    CloseMessageWindow()

    #C0427
    ChrTalk(
        0xB,
        "ふ、ふむ、それもそうか……\x02",
    )

    CloseMessageWindow()

    #C0428
    ChrTalk(
        0xB,
        (
            "なんだかキナ臭く\x01",
            "なってきおったのう……\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0xB4, 0x1F4)
    Sleep(300)

    #C0429
    ChrTalk(
        0x101,
        (
            "#00001Fミンネス氏には、何か別の目的……\x01",
            "あるいは必ず儲かるアテが\x01",
            "あるのかもしれません。\x02\x03",

            "#00003F何の証拠もありませんが……\x01",
            "念のため、心に留めておいた方が\x01",
            "いいと思います。\x02",
        )
    )

    CloseMessageWindow()

    #C0430
    ChrTalk(
        0xB,
        (
            "うむ……\x01",
            "重々気をつけるとしよう。\x02",
        )
    )

    CloseMessageWindow()

    #C0431
    ChrTalk(
        0xB,
        (
            "……さて、\x01",
            "ご苦労だったな、\x01",
            "特務支援課の諸君。\x02",
        )
    )

    CloseMessageWindow()

    #C0432
    ChrTalk(
        0xB,
        (
            "おかげでかなり\x01",
            "状況を整理できたわい。\x01",
            "礼を言わせてもらうぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0433
    ChrTalk(
        0x101,
        (
            "#00003Fいえ、それはいいんですが……\x02\x03",

            "#00005Fその、大丈夫ですか？\x01",
            "何なら、捜査を継続して……\x02",
        )
    )

    CloseMessageWindow()

    #C0434
    ChrTalk(
        0xB,
        "いや……ひとまずはこれで結構じゃ。\x02",
    )

    CloseMessageWindow()

    #C0435
    ChrTalk(
        0xB,
        (
            "そもそも村の私有地に関しても、\x01",
            "勝手な工場の建造計画などを\x01",
            "認めるわけにはいかん。\x02",
        )
    )

    CloseMessageWindow()

    #C0436
    ChrTalk(
        0xB,
        (
            "あとは村長として、\x01",
            "なんとかデリックと話をして\x01",
            "説得してみることにしよう。\x02",
        )
    )

    CloseMessageWindow()

    #C0437
    ChrTalk(
        0x102,
        "#00103F……それがいいかもしれませんね。\x02",
    )

    CloseMessageWindow()

    #C0438
    ChrTalk(
        0x101,
        (
            "#00003Fでは、自分たちはこれで\x01",
            "失礼します。\x02\x03",

            "#00000Fまた何かあったら\x01",
            "いつでもお呼びください。\x02",
        )
    )

    CloseMessageWindow()

    #C0439
    ChrTalk(
        0xB,
        (
            "うむ、そのときは\x01",
            "よろしく頼むとしよう。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0440
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "クエスト【不審人物の調査】\x07\x00",
            "を達成した！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_29(0x82, 0x1, 0x7)
    OP_29(0x82, 0x1, 0x8)
    OP_29(0x82, 0x4, 0x10)
    OP_50(0x1E, (scpexpr(EXPR_PUSH_LONG, 0x19), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetChrSubChip(0xB, 0x0)
    SetChrPos(0x0, -41050, 0, -1950, 270)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_23_819B end

    def Function_24_8F2D(): pass

    label("Function_24_8F2D")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    OP_4B(0xD, 0xFF)
    OP_4B(0xF, 0xFF)
    OP_4B(0x10, 0xFF)
    LoadChrToIndex("chr/ch24000.itc", 0x1E)
    LoadChrToIndex("chr/ch09300.itc", 0x1F)
    OP_68(-46010, 3100, -2510, 0)
    MoveCamera(315, 25, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25000, 0)
    SetChrChipByIndex(0xB, 0x1E)
    SetChrSubChip(0xB, 0x0)
    SetChrChipByIndex(0xF, 0x1F)
    SetChrSubChip(0xF, 0x0)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0xB, -47740, 0, -120, 180)
    SetChrPos(0xF, -48950, 0, -2510, 45)
    SetChrPos(0xD, -46260, 0, 50, 180)
    SetChrPos(0x10, -49140, 0, -3150, 45)
    SetChrPos(0x101, -47540, 0, -1830, 0)
    SetChrPos(0x102, -46230, 0, -1750, 315)
    SetChrPos(0x103, -44810, 0, -1320, 315)
    SetChrPos(0x104, -45630, 0, -3150, 315)
    SetChrPos(0x109, -46960, 0, -3110, 0)
    SetChrPos(0x105, -44330, 0, -2660, 315)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_68(-46010, 1900, -2510, 3000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x1)

    #C0441
    ChrTalk(
        0xB,
        "諸君、よくやってくれた。\x02",
    )

    CloseMessageWindow()

    #C0442
    ChrTalk(
        0xB,
        (
            "おかげであの\x01",
            "詐欺師の魔の手から\x01",
            "村が救われたよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0443
    ChrTalk(
        0x101,
        (
            "#00006F結局犯人はとり逃して\x01",
            "しまいましたが……\x02",
        )
    )

    CloseMessageWindow()

    #C0444
    ChrTalk(
        0x102,
        (
            "#00103Fでも、警察本部にも\x01",
            "報告できたし……\x02\x03",

            "#00100F捕まるのは時間の問題じゃ\x01",
            "ないかしら。\x02",
        )
    )

    CloseMessageWindow()

    #C0445
    ChrTalk(
        0xD,
        "…………………………\x02",
    )

    CloseMessageWindow()

    #C0446
    ChrTalk(
        0xF,
        "#03605Fデリック君？\x02",
    )

    CloseMessageWindow()

    def lambda_919D():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_919D)
    Sleep(50)

    def lambda_91AD():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_91AD)
    Sleep(50)

    #C0447
    ChrTalk(
        0xD,
        (
            "……みなさんには、\x01",
            "本当に迷惑をかけてしまった。\x02",
        )
    )

    CloseMessageWindow()

    #C0448
    ChrTalk(
        0xD,
        (
            "俺が詐欺なんかに\x01",
            "引っかかったばかりに、\x01",
            "ここまでの事態に……\x02",
        )
    )

    CloseMessageWindow()

    #C0449
    ChrTalk(
        0x109,
        "#10108Fそんな、あなたのせいでは……\x02",
    )

    CloseMessageWindow()

    #C0450
    ChrTalk(
        0xD,
        (
            "いや……\x01",
            "全ては俺の責任だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0451
    ChrTalk(
        0xD,
        (
            "改革、改革と躍起になって、\x01",
            "親父に対して意地を張って……\x01",
            "結果このざまだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0452
    ChrTalk(
        0xD,
        (
            "俺には次期村長の\x01",
            "資格なんてないだろう。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0xD, 500)
    Sleep(300)

    #C0453
    ChrTalk(
        0xB,
        "……そんなことはあるまい。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0xB, 500)
    Sleep(300)

    #C0454
    ChrTalk(
        0xD,
        "親父……？\x02",
    )

    CloseMessageWindow()

    #C0455
    ChrTalk(
        0xB,
        (
            "わしも保守的な考えにばかり\x01",
            "固執して、お前の話を\x01",
            "聞こうともしなかった。\x02",
        )
    )

    CloseMessageWindow()

    #C0456
    ChrTalk(
        0xB,
        (
            "このままでは村はダメに\x01",
            "なってしまうと知りつつ、\x01",
            "何もしようとはしなかった。\x02",
        )
    )

    CloseMessageWindow()

    #C0457
    ChrTalk(
        0xB,
        (
            "今回の件に関しては\x01",
            "わしの責任も大きいじゃろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0458
    ChrTalk(
        0xF,
        "#03608F村長……\x02",
    )

    CloseMessageWindow()
    OP_93(0xB, 0xB4, 0x1F4)
    Sleep(300)

    #C0459
    ChrTalk(
        0xB,
        (
            "わしは今回の件を通して\x01",
            "つくづく思ったのじゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0460
    ChrTalk(
        0xB,
        (
            "村を守るためには\x01",
            "一個人の考えに\x01",
            "固執してはならんとな。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0xD, 500)
    Sleep(300)

    #C0461
    ChrTalk(
        0xB,
        (
            "デリック……\x01",
            "これからは是非、\x01",
            "お前の知恵も貸して欲しい。\x02",
        )
    )

    CloseMessageWindow()

    #C0462
    ChrTalk(
        0xB,
        (
            "互いに案を出し合い、\x01",
            "村人全員で話し合って……\x02",
        )
    )

    CloseMessageWindow()

    #C0463
    ChrTalk(
        0xB,
        (
            "このアルモリカという村を\x01",
            "守っていこうじゃないか。\x02",
        )
    )

    CloseMessageWindow()

    #C0464
    ChrTalk(
        0xD,
        (
            "……ああ、そうだな。\x01",
            "すまなかった親父……\x02",
        )
    )

    CloseMessageWindow()

    #C0465
    ChrTalk(
        0xD,
        (
            "俺も、これまで以上に\x01",
            "村のことを考えて\x01",
            "生きていくことにするよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0466
    ChrTalk(
        0x102,
        (
            "#00102Fふふ……\x01",
            "和解できたみたいで\x01",
            "よかったですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0467
    ChrTalk(
        0x104,
        "#00309Fはは、そうだな。\x02",
    )

    CloseMessageWindow()

    #C0468
    ChrTalk(
        0x105,
        (
            "#10304Fま、こういうオチなら\x01",
            "詐欺にかかったのも\x01",
            "悪くなかったんじゃない？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0xF, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0xD, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x10, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    def lambda_973F():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_973F)
    Sleep(50)

    def lambda_974F():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_974F)
    Sleep(50)

    def lambda_975F():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_975F)
    Sleep(50)

    def lambda_976F():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_976F)
    Sleep(50)

    def lambda_977F():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_977F)
    Sleep(50)

    def lambda_978F():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_978F)
    Sleep(50)

    def lambda_979F():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_979F)
    Sleep(50)

    def lambda_97AF():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_97AF)
    Sleep(50)

    def lambda_97BF():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_97BF)
    Sleep(300)

    #C0469
    ChrTalk(
        0x109,
        "#10106Fワ、ワジ君……\x02",
    )

    CloseMessageWindow()

    #C0470
    ChrTalk(
        0x103,
        "#00200Fふむ、物は言いようですね……\x02",
    )

    CloseMessageWindow()

    #C0471
    ChrTalk(
        0x101,
        (
            "#00006Fい、いやいや、\x01",
            "さすがに不謹慎だから。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xB, 0xB4, 0x1F4)
    Sleep(300)

    #C0472
    ChrTalk(
        0xB,
        "と、とにかく……\x02",
    )

    CloseMessageWindow()

    #C0473
    ChrTalk(
        0xB,
        (
            "あんたたちには本当に\x01",
            "お世話になってしまったな。\x01",
            "重ねて礼を言わせて欲しい。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_98B5():
        TurnDirection(0xFE, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_98B5)
    Sleep(50)

    def lambda_98C5():
        TurnDirection(0xFE, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_98C5)
    Sleep(50)

    def lambda_98D5():
        TurnDirection(0xFE, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_98D5)
    Sleep(50)

    def lambda_98E5():
        TurnDirection(0xFE, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_98E5)
    Sleep(50)

    def lambda_98F5():
        TurnDirection(0xFE, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_98F5)
    Sleep(50)

    def lambda_9905():
        TurnDirection(0xFE, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_9905)
    Sleep(50)

    def lambda_9915():
        TurnDirection(0xFE, 0xB, 500)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_9915)
    Sleep(50)

    def lambda_9925():
        TurnDirection(0xFE, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_9925)
    Sleep(50)

    def lambda_9935():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_9935)
    Sleep(300)

    #C0474
    ChrTalk(
        0xB,
        (
            "イアン先生にも、\x01",
            "改めてお礼を言わねばなるまいて。\x02",
        )
    )

    CloseMessageWindow()

    #C0475
    ChrTalk(
        0x10,
        (
            "先生には僕のほうから\x01",
            "顛末をお伝えしておきますね。\x02",
        )
    )

    CloseMessageWindow()

    #C0476
    ChrTalk(
        0xF,
        (
            "#03604F私も、事件の解決に少しでも\x01",
            "お役に立ててよかったです。\x02\x03",

            "#03600Fまたこれからも\x01",
            "よろしくおねがいしますよ、村長。\x02",
        )
    )

    CloseMessageWindow()

    #C0477
    ChrTalk(
        0xB,
        "はは、こちらこそな。\x02",
    )

    CloseMessageWindow()

    #C0478
    ChrTalk(
        0x101,
        (
            "#00003F念のため、あの詐欺師には\x01",
            "充分に注意するようにしてください。\x02\x03",

            "#00000Fまた何かあったら、\x01",
            "いつでも支援課にご連絡を。\x02",
        )
    )

    CloseMessageWindow()

    #C0479
    ChrTalk(
        0xD,
        (
            "ああ、よろしく頼むよ。\x01",
            "本当にありがとうな。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0480
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "クエスト【不審商人の調査】\x07\x00",
            "を達成した！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_29(0x87, 0x1, 0xA)
    OP_29(0x87, 0x1, 0xB)
    OP_29(0x87, 0x4, 0x10)
    SetChrPos(0xB, -38480, 180, -1780, 90)
    SetChrChipByIndex(0xB, 0x0)
    SetChrSubChip(0xB, 0x0)
    EndChrThread(0xB, 0x0)
    SetChrBattleFlags(0xB, 0x4)
    SetChrPos(0xF, -34200, 180, -1530, 270)
    SetChrChipByIndex(0xF, 0x2)
    SetChrSubChip(0xF, 0x0)
    EndChrThread(0xF, 0x0)
    SetChrBattleFlags(0xF, 0x4)
    SetChrPos(0xD, -38050, 0, -140, 180)
    SetChrPos(0x10, -34400, 0, -300, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_D7(0x1E)
    OP_D7(0x1F)
    SetChrPos(0x0, -46650, 0, -1460, 135)
    OP_69(0xFF, 0x0)
    OP_4C(0xD, 0xFF)
    OP_4C(0xF, 0xFF)
    OP_4C(0x10, 0xFF)
    EventEnd(0x5)
    Return()

    # Function_24_8F2D end

    def Function_25_9BFB(): pass

    label("Function_25_9BFB")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_93(0xB, 0x0, 0x0)
    OP_68(-37850, 1500, -940, 0)
    MoveCamera(327, 34, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(26120, 0)
    SetChrPos(0x101, -38350, 0, -70, 180)
    SetChrPos(0x102, -39580, 0, -40, 135)
    SetChrPos(0x103, -37610, 0, 1040, 180)
    SetChrPos(0x104, -39030, 0, 1050, 180)
    SetChrPos(0x109, -38350, 0, 1950, 180)
    SetChrPos(0x105, -40330, 0, 1370, 135)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()

    #C0481
    ChrTalk(
        0x101,
        "#00000Fトルタ村長、こんにちは。\x02",
    )

    CloseMessageWindow()

    #C0482
    ChrTalk(
        0xB,
        (
            "おお、特務支援課の諸君。\x01",
            "今日は一体何の用だね？\x02",
        )
    )

    CloseMessageWindow()

    #C0483
    ChrTalk(
        0x101,
        (
            "#00000F実は、村長に\x01",
            "お尋ねしたいことが\x01",
            "あるんですが……\x02\x03",

            "#00003F養蜂場にある納屋に、\x01",
            "誰かを住まわせてはいませんか？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0484
    ChrTalk(
        0xB,
        (
            "ふむ、確かに今あそこには\x01",
            "人を泊まらせておる。\x02",
        )
    )

    CloseMessageWindow()

    #C0485
    ChrTalk(
        0xB,
        (
            "３、４日前の話じゃったか。\x01",
            "『しばらくの間かくまってくれ』と\x01",
            "突然頼まれてな。\x02",
        )
    )

    CloseMessageWindow()

    #C0486
    ChrTalk(
        0xB,
        (
            "たしか名前を……\x01",
            "ゲバル殿というたか。\x02",
        )
    )

    CloseMessageWindow()

    #C0487
    ChrTalk(
        0x102,
        (
            "#00105Fやっぱり……！\x02\x03",

            "#00106Fでも、どうして納屋なんかに？\x02",
        )
    )

    CloseMessageWindow()

    #C0488
    ChrTalk(
        0xB,
        (
            "一応、なんなら宿をとろうかと\x01",
            "言うたんじゃが……\x02",
        )
    )

    CloseMessageWindow()

    #C0489
    ChrTalk(
        0xB,
        (
            "『できるだけ目立たない場所がいい』\x01",
            "などと言うて聞かなんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0490
    ChrTalk(
        0xB,
        (
            "事情を聞いても何も言わんし、\x01",
            "よほどの大事に巻き込まれて\x01",
            "いるのではと思っていたが……\x02",
        )
    )

    CloseMessageWindow()

    #C0491
    ChrTalk(
        0xB,
        (
            "まさか、おぬしらの\x01",
            "探し人じゃったとはな。\x02",
        )
    )

    CloseMessageWindow()

    #C0492
    ChrTalk(
        0xB,
        (
            "もしや、なにかの事件の\x01",
            "犯人だったりするのかね？\x02",
        )
    )

    CloseMessageWindow()

    #C0493
    ChrTalk(
        0x103,
        "#00203Fいえ、そういうわけでは。\x02",
    )

    CloseMessageWindow()

    #C0494
    ChrTalk(
        0x109,
        (
            "#10100Fロイドさん、村長さんには\x01",
            "話しておいたほうが\x01",
            "いいかもしれませんね。\x02",
        )
    )

    CloseMessageWindow()

    #C0495
    ChrTalk(
        0x101,
        "#00003Fああ、そうだな……\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    #A0496
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ロイドはアルムとエアリーの依頼で\x01",
            "ゲバルを捜索している事情を説明した。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0497
    ChrTalk(
        0xB,
        (
            "ふむ、なるほど……\x01",
            "元議員先生じゃったか。\x02",
        )
    )

    CloseMessageWindow()

    #C0498
    ChrTalk(
        0xB,
        (
            "大分前に、脱税疑惑を逃れるため\x01",
            "仮病を使って入院していた議員……\x02",
        )
    )

    CloseMessageWindow()

    #C0499
    ChrTalk(
        0xB,
        (
            "言われてみればクロスベルタイムズで\x01",
            "見た顔じゃった気がするわい。\x02",
        )
    )

    CloseMessageWindow()

    #C0500
    ChrTalk(
        0x105,
        (
            "#10304Fま、今回はその件は\x01",
            "直接関係なさそうだけどね。\x02",
        )
    )

    CloseMessageWindow()

    #C0501
    ChrTalk(
        0x101,
        (
            "#00000Fトルタ村長、納屋にいる\x01",
            "ゲバルさんと話させてはくれませんか？\x02\x03",

            "#00008F彼はアルムさんたちに\x01",
            "会いたくないみたいですが、でも……\x02",
        )
    )

    CloseMessageWindow()

    #C0502
    ChrTalk(
        0xB,
        "……うむ、よかろう。\x02",
    )

    CloseMessageWindow()

    #C0503
    ChrTalk(
        0xB,
        (
            "わしも息子と確執があったが、\x01",
            "結局は対話が足りていないのが\x01",
            "何よりの原因じゃった。\x02",
        )
    )

    CloseMessageWindow()

    #C0504
    ChrTalk(
        0xB,
        (
            "おなじ轍#2Rてつ#を他人に\x01",
            "踏ませとうはないでな。\x02",
        )
    )

    CloseMessageWindow()

    #C0505
    ChrTalk(
        0x101,
        "#00002F村長……\x02",
    )

    CloseMessageWindow()

    #C0506
    ChrTalk(
        0xB,
        "ふふ、ついてくるがいい。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 1)
    NewScene("t0000", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_25_9BFB end

    def Function_26_A31F(): pass

    label("Function_26_A31F")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(76390, 1500, 1360, 0)
    MoveCamera(315, 32, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25000, 0)
    OP_4B(0x12, 0xFF)
    SetChrChipByIndex(0x12, 0xC)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x12, 0x8000)
    SetChrPos(0x12, 75800, 0, 2000, 0)
    SetChrChipByIndex(0xB, 0xB)
    SetChrSubChip(0xB, 0x0)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0x101, 75070, 0, -5420, 0)
    SetChrPos(0x102, 75070, 0, -5420, 0)
    SetChrPos(0x103, 75070, 0, -5420, 0)
    SetChrPos(0x104, 75070, 0, -5420, 0)
    SetChrPos(0x109, 75070, 0, -5420, 0)
    SetChrPos(0x105, 75070, 0, -5420, 0)
    SetChrPos(0xB, 75070, 0, -5420, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xB, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_68(76600, 1500, -270, 3000)
    BeginChrThread(0x101, 3, 0, 27)
    Sleep(500)
    BeginChrThread(0x102, 3, 0, 28)
    Sleep(500)
    BeginChrThread(0x103, 3, 0, 29)
    Sleep(500)
    BeginChrThread(0x104, 3, 0, 30)
    Sleep(500)
    BeginChrThread(0x109, 3, 0, 31)
    Sleep(500)
    BeginChrThread(0x105, 3, 0, 32)
    Sleep(500)
    BeginChrThread(0xB, 3, 0, 33)
    WaitChrThread(0xB, 3)
    OP_6F(0x1)

    #C0507
    ChrTalk(
        0x101,
        (
            "#00000Fゲバルさん……ですね？\x02\x03",

            "#00006Fふう、ようやく見つけましたよ。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x12, 0xB4, 0x1F4)
    Sleep(300)

    #C0508
    ChrTalk(
        0x12,
        (
            "#4Pフン……\x01",
            "仕事熱心でご苦労なことだわい。\x02",
        )
    )

    CloseMessageWindow()

    #C0509
    ChrTalk(
        0x12,
        (
            "#4P息子夫婦が\x01",
            "わしを探しているらしいが……\x02",
        )
    )

    CloseMessageWindow()

    #C0510
    ChrTalk(
        0x12,
        (
            "#4Pわしは何と言われようが\x01",
            "会うつもりはないぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0511
    ChrTalk(
        0x109,
        "#10106Fど、どうしてそんな頑なに……？\x02",
    )

    CloseMessageWindow()

    #C0512
    ChrTalk(
        0x12,
        "#4P……当然のことだろう。\x02",
    )

    CloseMessageWindow()

    #C0513
    ChrTalk(
        0x12,
        (
            "#4P息子は……アルムは、\x01",
            "わしを恨んでいるに\x01",
            "違いないのだからな。\x02",
        )
    )

    CloseMessageWindow()

    #C0514
    ChrTalk(
        0x103,
        "#00205F恨んでいる……？\x02",
    )

    CloseMessageWindow()

    #C0515
    ChrTalk(
        0x105,
        (
            "#10301Fできれば、\x01",
            "詳しく聞かせてくれるかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0516
    ChrTalk(
        0x12,
        (
            "#4P……わしは議員の見習い時代から、\x01",
            "様々な汚職に手を染めてきた。\x02",
        )
    )

    CloseMessageWindow()

    #C0517
    ChrTalk(
        0x12,
        (
            "#4P地位や名誉、ミラのためだけに働き、\x01",
            "家族を顧みようとはしなかった。\x02",
        )
    )

    CloseMessageWindow()

    #C0518
    ChrTalk(
        0x12,
        (
            "#4Pそんなわしに、妻は不満を感じつつも、\x01",
            "幼いアルムの育児に専念することで\x01",
            "それを紛らわそうとしていた。\x02",
        )
    )

    CloseMessageWindow()

    #C0519
    ChrTalk(
        0x12,
        (
            "#4Pそしてわしはますます図に乗り、\x01",
            "ある日……子を持つ者として、\x01",
            "やってはならぬ事をしてしまった。\x02",
        )
    )

    CloseMessageWindow()

    #C0520
    ChrTalk(
        0x12,
        (
            "#4P妻が出かけた隙に、自分の屋敷に\x01",
            "当時の愛人を招いてしまったのだ。\x02",
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
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0xB, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0521
    ChrTalk(
        0x109,
        "#10106Fそ、それは……\x02",
    )

    CloseMessageWindow()

    #C0522
    ChrTalk(
        0x104,
        "#00306Fやっちまったって感じだなあ……\x02",
    )

    CloseMessageWindow()

    #C0523
    ChrTalk(
        0x12,
        (
            "#4Pそれも程なくして妻の知る所になり、\x01",
            "ついに愛想をつかした妻は\x01",
            "アルムを連れて故郷リベールに帰った。\x02",
        )
    )

    CloseMessageWindow()

    #C0524
    ChrTalk(
        0x12,
        (
            "#4Pその後の事は一切知らぬが……\x01",
            "離婚したことで、妻にもアルムにも\x01",
            "色々と辛い思いをさせたに違いない。\x02",
        )
    )

    CloseMessageWindow()

    #C0525
    ChrTalk(
        0x12,
        (
            "#4Pしかしわしは、あろうことか\x01",
            "せいせいした気分でいた。\x02",
        )
    )

    CloseMessageWindow()

    #C0526
    ChrTalk(
        0x12,
        (
            "#4P正式に離婚届けが受理された\x01",
            "次の日には、広くなった屋敷に\x01",
            "別の愛人を招いたりしていた……\x02",
        )
    )

    CloseMessageWindow()

    #C0527
    ChrTalk(
        0x101,
        "#00003Fう、うーん……\x02",
    )

    CloseMessageWindow()

    #C0528
    ChrTalk(
        0x104,
        (
            "#00306Fそれは確かに、恨まれても\x01",
            "仕方なさそうな行いだなあ。\x02",
        )
    )

    CloseMessageWindow()

    #C0529
    ChrTalk(
        0x103,
        (
            "#00211F……ランディさん、\x01",
            "ストレートに言い過ぎかと。\x02",
        )
    )

    CloseMessageWindow()

    #C0530
    ChrTalk(
        0x12,
        (
            "#4Pフン、そこの赤毛の言うとおり、\x01",
            "わしは恨まれても仕方のない人間じゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0531
    ChrTalk(
        0x12,
        (
            "#4Pそれに……わしは所詮、\x01",
            "ハルトマン元議長の腰巾着だった男だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0532
    ChrTalk(
        0x12,
        (
            "#4Pだが、つまらない脱税などを\x01",
            "犯したがために元議長には\x01",
            "カンタンに尻尾切りされ……\x02",
        )
    )

    CloseMessageWindow()

    #C0533
    ChrTalk(
        0x12,
        (
            "#4Pいっそ逮捕されていたら\x01",
            "楽だったろうに、皮肉にも\x01",
            "失脚しただけで済んでしまった。\x02",
        )
    )

    CloseMessageWindow()

    #C0534
    ChrTalk(
        0x12,
        (
            "#4Pこの何もかもを失った身を\x01",
            "息子に晒すなどという無様……\x01",
            "わしには耐えられそうにないのだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0535
    ChrTalk(
        0xB,
        "ゲバル殿……\x02",
    )

    CloseMessageWindow()

    #C0536
    ChrTalk(
        0x102,
        "#00103Fそういうことでしたか……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)

    #C0537
    ChrTalk(
        0x101,
        (
            "#00001F……あの。\x01",
            "一ついいでしょうか。\x02",
        )
    )

    CloseMessageWindow()

    #C0538
    ChrTalk(
        0x12,
        (
            "#4P……なんだね？\x01",
            "いまさら何を言われようと……\x02",
        )
    )

    CloseMessageWindow()

    #C0539
    ChrTalk(
        0x101,
        (
            "#00003F……確かにあなたは、\x01",
            "息子さんや奥さんに\x01",
            "ひどいことをしたのかもしれない。\x02\x03",

            "悪徳政治家として、\x01",
            "色々と後ろ暗いことも\x01",
            "やってきたのかもしれない。\x02\x03",

            "#00000Fですが、先ほどの言葉の数々は、\x01",
            "ゲバルさんの懺悔に聞こえました。\x02",
        )
    )

    CloseMessageWindow()

    #C0540
    ChrTalk(
        0x102,
        (
            "#00103F……そうね。\x02\x03",

            "#00100F充分に反省の心が見てとれるし、\x01",
            "社会的に見てもあなたはすでに\x01",
            "制裁を受けています。\x02\x03",

            "#00108F罪悪感から会わないというのは\x01",
            "あまりスジが通らないかも……\x02",
        )
    )

    CloseMessageWindow()

    #C0541
    ChrTalk(
        0x12,
        "#4Pし、しかしだな……！\x02",
    )

    CloseMessageWindow()

    #C0542
    ChrTalk(
        0x101,
        (
            "#00003Fそれに……\x02\x03",

            "#00002F俺には決して、あのアルムさんが\x01",
            "あなたを恨んでいるとは思えません。\x02",
        )
    )

    CloseMessageWindow()

    #C0543
    ChrTalk(
        0x12,
        "#4P……え……\x02",
    )

    CloseMessageWindow()

    #C0544
    ChrTalk(
        0x101,
        (
            "#00004F俺たちにゲバルさんの捜索を\x01",
            "依頼していたアルムさんと、\x01",
            "奥さんのエアリーさん……\x02\x03",

            "#00002F彼らは暖かい家庭を築いていて、\x01",
            "とても幸せそうでした。\x02\x03",

            "そんな中、依頼したアルムさんが\x01",
            "口にした願望はひとつ……\x02\x03",

            "#00004F“生まれてきたお子さんを見せて、\x01",
            "  幸せな家庭を築けたことを\x01",
            "  報告したい”という事だけでした。\x02",
        )
    )

    CloseMessageWindow()

    #C0545
    ChrTalk(
        0x12,
        "#4P……！\x02",
    )

    CloseMessageWindow()

    #C0546
    ChrTalk(
        0x109,
        (
            "#10109Fあはは、そうですね。\x02\x03",

            "#10106Fアテられそうなくらい\x01",
            "ラブラブしてましたし……\x02",
        )
    )

    CloseMessageWindow()

    #C0547
    ChrTalk(
        0x104,
        (
            "#00304Fま、微塵でも“恨み”なんて\x01",
            "暗い気持ちがあったら\x01",
            "あんな表情は出せねえわな。\x02",
        )
    )

    CloseMessageWindow()

    #C0548
    ChrTalk(
        0x105,
        (
            "#10309Fフフ、どうかな？\x02\x03",

            "#10304F僕くらいのポーカーフェイスになると\x01",
            "けっこうなんとかなっちゃうかも。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x105, 500)
    Sleep(300)

    #C0549
    ChrTalk(
        0x103,
        (
            "#00211F……ワジさん、\x01",
            "まぜっ返さないでください。\x02",
        )
    )

    CloseMessageWindow()

    #C0550
    ChrTalk(
        0x104,
        (
            "#00300Fまあ、とにかくだ。\x01",
            "ゲバルさんよ、あんたの息子は\x01",
            "明るく成長できたってことさ。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x103, 0x0, 0x1F4)
    Sleep(300)

    #C0551
    ChrTalk(
        0x101,
        "#00004F……俺たちから言えるのはそれだけです。\x02",
    )

    CloseMessageWindow()

    #C0552
    ChrTalk(
        0x102,
        (
            "#00100Fどうでしょう……\x01",
            "やっぱり、アルムさんたちに\x01",
            "会ってはいただけませんか？\x02",
        )
    )

    CloseMessageWindow()

    #C0553
    ChrTalk(
        0x12,
        "#4P…………………………\x02",
    )

    CloseMessageWindow()
    OP_93(0x12, 0x0, 0x1F4)
    OP_63(0x12, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    Sleep(2000)
    OP_64(0x12)

    #C0554
    ChrTalk(
        0x12,
        (
            "#4P……そこまで言うなら……\x01",
            "会ってやらんでもないわい。\x02",
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
    Sleep(50)
    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0555
    ChrTalk(
        0x101,
        "#00005Fほ、本当ですか？\x02",
    )

    CloseMessageWindow()
    OP_93(0x12, 0xB4, 0x1F4)
    Sleep(300)

    #C0556
    ChrTalk(
        0x12,
        "#4Pフン、ウソを言ってどうするんじゃ。\x02",
    )

    CloseMessageWindow()

    #C0557
    ChrTalk(
        0x12,
        (
            "#4P……ほら、わしの気が変わらぬうちに\x01",
            "さっさと呼び出したらどうだ！\x02",
        )
    )

    CloseMessageWindow()

    #C0558
    ChrTalk(
        0x101,
        (
            "#00011Fわ、分かりました。\x01",
            "それじゃあすぐに呼んできます！\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x103, 3, 0, 35)
    Sleep(50)
    BeginChrThread(0x109, 3, 0, 36)
    Sleep(300)
    OP_68(76460, 1500, -1540, 2000)
    BeginChrThread(0x101, 3, 0, 34)

    def lambda_B52D():

        label("loc_B52D")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_B52D")

    QueueWorkItem2(0x102, 1, lambda_B52D)
    Sleep(50)

    def lambda_B542():

        label("loc_B542")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_B542")

    QueueWorkItem2(0x103, 1, lambda_B542)
    Sleep(50)

    def lambda_B557():

        label("loc_B557")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_B557")

    QueueWorkItem2(0x104, 1, lambda_B557)
    Sleep(50)

    def lambda_B56C():

        label("loc_B56C")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_B56C")

    QueueWorkItem2(0x109, 1, lambda_B56C)
    Sleep(50)

    def lambda_B581():

        label("loc_B581")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_B581")

    QueueWorkItem2(0x105, 1, lambda_B581)
    Sleep(50)

    def lambda_B596():

        label("loc_B596")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_B596")

    QueueWorkItem2(0xB, 1, lambda_B596)
    WaitChrThread(0x101, 3)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x104, 0x1)
    EndChrThread(0x109, 0x1)
    EndChrThread(0x105, 0x1)
    EndChrThread(0xB, 0x1)
    OP_6F(0x1)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrName("")

    #A0559
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "こうしてロイドは\x01",
            "《龍老飯店》に急ぎ連絡をいれ……\x02\x03",

            "アルムとエアリーを\x01",
            "アルモリカ村に呼び出したのだった。\x02\x03",

            "そして、心の準備をさせろというゲバルのため\x01",
            "一同は納屋の外で彼らを待つことになった。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x22, 2)
    NewScene("t0000", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_26_A31F end

    def Function_27_B6A5(): pass

    label("Function_27_B6A5")


    def lambda_B6AA():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_B6AA)

    def lambda_B6BB():
        OP_98(0xFE, 0x0, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B6BB)
    WaitChrThread(0x101, 1)
    OP_95(0x101, 75280, 0, 270, 2000, 0x0)
    OP_93(0x101, 0x0, 0x1F4)
    Return()

    # Function_27_B6A5 end

    def Function_28_B6F0(): pass

    label("Function_28_B6F0")


    def lambda_B6F5():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_B6F5)

    def lambda_B706():
        OP_98(0xFE, 0x0, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_B706)
    WaitChrThread(0x102, 1)
    OP_95(0x102, 76460, 0, 280, 2000, 0x0)
    OP_93(0x102, 0x0, 0x1F4)
    Return()

    # Function_28_B6F0 end

    def Function_29_B73B(): pass

    label("Function_29_B73B")


    def lambda_B740():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_B740)

    def lambda_B751():
        OP_98(0xFE, 0x0, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_B751)
    WaitChrThread(0x103, 1)
    OP_95(0x103, 75260, 0, -920, 2000, 0x0)
    OP_93(0x103, 0x0, 0x1F4)
    Return()

    # Function_29_B73B end

    def Function_30_B786(): pass

    label("Function_30_B786")


    def lambda_B78B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_B78B)

    def lambda_B79C():
        OP_98(0xFE, 0x0, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_B79C)
    WaitChrThread(0x104, 1)
    OP_95(0x104, 76470, 0, -920, 2000, 0x0)
    OP_93(0x104, 0x0, 0x1F4)
    Return()

    # Function_30_B786 end

    def Function_31_B7D1(): pass

    label("Function_31_B7D1")


    def lambda_B7D6():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_B7D6)

    def lambda_B7E7():
        OP_98(0xFE, 0x0, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_B7E7)
    WaitChrThread(0x109, 1)
    OP_95(0x109, 75210, 0, -2040, 2000, 0x0)
    OP_93(0x109, 0x0, 0x1F4)
    Return()

    # Function_31_B7D1 end

    def Function_32_B81C(): pass

    label("Function_32_B81C")


    def lambda_B821():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_B821)

    def lambda_B832():
        OP_98(0xFE, 0x0, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_B832)
    WaitChrThread(0x105, 1)
    OP_95(0x105, 76180, 0, -2040, 2000, 0x0)
    OP_93(0x105, 0x0, 0x1F4)
    Return()

    # Function_32_B81C end

    def Function_33_B867(): pass

    label("Function_33_B867")


    def lambda_B86C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_B86C)

    def lambda_B87D():
        OP_98(0xFE, 0x0, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_B87D)
    WaitChrThread(0xB, 1)
    OP_95(0xB, 77380, 0, -2650, 2000, 0x0)
    OP_95(0xB, 77640, 0, -310, 2000, 0x0)
    OP_93(0xB, 0x13B, 0x1F4)
    Return()

    # Function_33_B867 end

    def Function_34_B8C6(): pass

    label("Function_34_B8C6")


    def lambda_B8CB():
        OP_95(0xFE, 75070, 0, -5420, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B8CB)
    Sleep(1000)

    def lambda_B8E8():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_B8E8)
    Return()

    # Function_34_B8C6 end

    def Function_35_B8F5(): pass

    label("Function_35_B8F5")

    OP_93(0x103, 0x5A, 0x0)
    OP_9B(0x1, 0x103, 0xB4, 0x1F4, 0x7D0, 0x0)
    Return()

    # Function_35_B8F5 end

    def Function_36_B90C(): pass

    label("Function_36_B90C")

    OP_93(0x109, 0x5A, 0x0)
    OP_9B(0x1, 0x109, 0xB4, 0x2EE, 0x7D0, 0x0)
    Return()

    # Function_36_B90C end

    def Function_37_B923(): pass

    label("Function_37_B923")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(76170, 1500, -1190, 0)
    MoveCamera(315, 25, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(27560, 0)
    LoadChrToIndex("chr/ch46300.itc", 0x1E)
    LoadChrToIndex("chr/ch46200.itc", 0x1F)
    OP_4B(0x12, 0xFF)
    SetChrChipByIndex(0x12, 0xC)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x12, 0x8000)
    SetChrPos(0x12, 75790, 0, 2210, 0)
    SetChrChipByIndex(0x13, 0x1E)
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x13, 0x8000)
    SetChrPos(0x13, 75070, 0, -5420, 0)
    SetChrChipByIndex(0x14, 0x1F)
    ClearChrFlags(0x14, 0x80)
    SetChrFlags(0x14, 0x8000)
    SetChrPos(0x14, 75070, 0, -5420, 0)
    OP_A7(0x13, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x14, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    BeginChrThread(0x13, 3, 0, 38)
    Sleep(500)
    BeginChrThread(0x14, 3, 0, 39)
    OP_68(76070, 1500, 900, 4000)
    SetCameraDistance(24880, 4000)
    OP_6F(0x79)

    #C0560
    ChrTalk(
        0x13,
        "あ……\x02",
    )

    CloseMessageWindow()

    #C0561
    ChrTalk(
        0x13,
        "もしかして……父さんかい？\x02",
    )

    CloseMessageWindow()

    #C0562
    ChrTalk(
        0x13,
        "あはは、久しぶりだね。\x02",
    )

    CloseMessageWindow()
    OP_93(0x12, 0xB4, 0x1F4)
    Sleep(300)

    #C0563
    ChrTalk(
        0x12,
        "う、うム……\x02",
    )

    CloseMessageWindow()

    #C0564
    ChrTalk(
        0x12,
        (
            "ひ、久しぶりだなアルム。\x01",
            "１５年ぶりくらいか……\x02",
        )
    )

    CloseMessageWindow()

    #C0565
    ChrTalk(
        0x12,
        "それにそちらは……\x02",
    )

    CloseMessageWindow()

    #C0566
    ChrTalk(
        0x14,
        "どうも、はじめましてお義父さま。\x02",
    )

    CloseMessageWindow()

    #C0567
    ChrTalk(
        0x14,
        (
            "アルムの妻のエアリーです。\x01",
            "よろしくおねがいしますね。\x02",
        )
    )

    CloseMessageWindow()

    #C0568
    ChrTalk(
        0x12,
        "う、うむ……\x02",
    )

    CloseMessageWindow()

    #C0569
    ChrTalk(
        0x12,
        (
            "息子がこんなにも可憐な\x01",
            "お嬢さんと一緒になったというのは、\x01",
            "わしも鼻が高い。\x02",
        )
    )

    CloseMessageWindow()

    #C0570
    ChrTalk(
        0x14,
        "まあ、お義父さまったら……\x02",
    )

    CloseMessageWindow()
    OP_63(0x12, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0571
    ChrTalk(
        0x12,
        "あ…………\x02",
    )

    CloseMessageWindow()

    #C0572
    ChrTalk(
        0x12,
        (
            "……そ、それが……\x01",
            "その腕に抱えているのは……\x02",
        )
    )

    CloseMessageWindow()

    #C0573
    ChrTalk(
        0x13,
        "フフ、僕たちの子供さ。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x13, 0x14, 500)
    Sleep(300)

    #C0574
    ChrTalk(
        0x13,
        (
            "……アルミン、\x01",
            "おじいちゃんにご挨拶は？\x02",
        )
    )

    CloseMessageWindow()

    #N0575
    NpcTalk(
        0x14,
        "赤ん坊",
        "ばぶぶ。\x02",
    )

    CloseMessageWindow()

    #C0576
    ChrTalk(
        0x14,
        "おお、よしよし～。\x02",
    )

    CloseMessageWindow()

    #C0577
    ChrTalk(
        0x12,
        "…………は、はは…………\x02",
    )

    CloseMessageWindow()
    OP_63(0x12, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x12)

    #C0578
    ChrTalk(
        0x12,
        (
            "そ、その……アルム。\x01",
            "お前と母さんには、\x01",
            "色々と辛い思いを……\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x13, 0x0, 0x1F4)
    Sleep(300)
    OP_63(0x13, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0579
    ChrTalk(
        0x13,
        "えっ……なんのことだい？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x13, 0x14, 500)
    Sleep(300)

    #C0580
    ChrTalk(
        0x13,
        (
            "そんなことより、見てよ父さん。\x01",
            "このアルミンの瞳ときたら……\x01",
            "まるで蒼耀石のようにキレイだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0581
    ChrTalk(
        0x13,
        (
            "エアリー……\x01",
            "青空のように美しい\x01",
            "君の瞳にそっくりだよ。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x14, 0x13, 500)
    Sleep(300)

    #C0582
    ChrTalk(
        0x14,
        (
            "ああ、それをいうならアルム……\x01",
            "アルミンの耳の形は\x01",
            "あなたとうりふたつよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0583
    ChrTalk(
        0x14,
        (
            "ウフフ……\x01",
            "みてるとカプリと\x01",
            "食べちゃいたくなるわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0584
    ChrTalk(
        0x13,
        (
            "ああエアリー……\x01",
            "一生君とこの子を離さないよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0585
    ChrTalk(
        0x14,
        (
            "アルム……\x01",
            "ずっと幸せでいましょうね。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x12, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x12)
    OP_93(0x12, 0x0, 0x1F4)
    Sleep(300)

    #C0586
    ChrTalk(
        0x12,
        "…………ぐすっ…………\x02",
    )

    CloseMessageWindow()
    OP_63(0x13, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x14, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_BF3A():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_BF3A)
    Sleep(50)

    def lambda_BF4A():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_BF4A)
    Sleep(300)

    #C0587
    ChrTalk(
        0x13,
        "あれ、父さん……どうしたんだい？\x02",
    )

    CloseMessageWindow()

    #C0588
    ChrTalk(
        0x14,
        (
            "アルム、もしかして\x01",
            "お体の具合がよろしくないんじゃ……\x02",
        )
    )

    CloseMessageWindow()

    #C0589
    ChrTalk(
        0x12,
        (
            "……グスッ……\x01",
            "………大丈夫……大丈夫だとも……\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4C(0x12, 0xFF)
    SetScenarioFlags(0x22, 3)
    NewScene("t0000", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_37_B923 end

    def Function_38_C016(): pass

    label("Function_38_C016")


    def lambda_C01B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_C01B)

    def lambda_C02C():
        OP_98(0xFE, 0x0, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_C02C)
    WaitChrThread(0x13, 1)
    OP_95(0x13, 74920, 0, 210, 2000, 0x0)
    OP_93(0x13, 0x0, 0x1F4)
    Return()

    # Function_38_C016 end

    def Function_39_C061(): pass

    label("Function_39_C061")


    def lambda_C066():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_C066)

    def lambda_C077():
        OP_98(0xFE, 0x0, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_C077)
    WaitChrThread(0x14, 1)
    OP_95(0x14, 76120, 0, 210, 2000, 0x0)
    OP_93(0x14, 0x0, 0x1F4)
    Return()

    # Function_39_C061 end

    SaveToFile()

Try(main)
