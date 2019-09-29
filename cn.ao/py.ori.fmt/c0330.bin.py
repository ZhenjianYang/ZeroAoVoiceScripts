from ScenarioHelper import *

def main():
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
        "哈罗德",                 # 1
        "索菲亚",                 # 2
        "柯林",                   # 3
        "辛迪",                   # 4
        "特鲁塔村长",             # 5
        "伊安律师",               # 6
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
        "Function_6_8F3",          # 06, 6
        "Function_7_13CE",         # 07, 7
        "Function_8_21DA",         # 08, 8
        "Function_9_22A5",         # 09, 9
        "Function_10_2A9E",        # 0A, 10
        "Function_11_2B29",        # 0B, 11
        "Function_12_2C22",        # 0C, 12
        "Function_13_2E28",        # 0D, 13
        "Function_14_300B",        # 0E, 14
        "Function_15_3678",        # 0F, 15
        "Function_16_3959",        # 10, 16
        "Function_17_3A54",        # 11, 17
        "Function_18_4802",        # 12, 18
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
            "放置着导力车杂志《导力车发烧友月刊 vol.1》。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 1)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x36C, 0x0)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8EF")
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0002
    AnonymousTalk(
        0xFF,
        (
            "导力车喷漆式样\x01\x07\x02",

            "『天空色彩』\x07\x00",
            "已经记下来了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    AddItemNumber(0x36C, 1)

    label("loc_8EF")

    TalkEnd(0xFF)
    Return()

    # Function_5_846 end

    def Function_6_8F3(): pass

    label("Function_6_8F3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_C04")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CD, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B15")

    #C0003
    ChrTalk(
        0x8,
        (
            "#03600F啊，各位……\x01",
            "你们平安无事，真是太好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x101,
        (
            "#00000F哈罗德先生，你们已经从\x01",
            "阿尔摩利卡村回来了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x8,
        (
            "#03604F嗯，我们发现结界已经消失，\x01",
            "就动身回来了，刚刚才到家。\x02\x03",

            "#03600F不过我马上就要\x01",
            "再次出门了。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x103,
        "#00203F实在是很忙啊。\x02",
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x104,
        (
            "#00300F家人都在身边，\x01",
            "稍微多休息一阵子\x01",
            "也没关系吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x8,
        (
            "#03603F不，我希望尽己所能，\x01",
            "为克洛斯贝尔各地的人们\x01",
            "贡献些力量。\x02\x03",

            "#03600F首先准备去玛因兹\x01",
            "那边一趟。\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x101,
        (
            "#00004F这样啊……\x01",
            "真不愧是哈罗德先生。\x02\x03",

            "#00002F请您路上小心。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x8,
        (
            "#03609F嗯，大家也一样……\x01",
            "愿女神保佑你们。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1CD, 0)
    Jump("loc_BFF")

    label("loc_B15")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BB5")

    #C0011
    ChrTalk(
        0x8,
        (
            "#03600F我首先准备去玛因兹\x01",
            "那边一趟。\x02\x03",

            "#03603F在这个特殊时期，我希望能\x01",
            "尽己所能，为各地的人们贡献些力量。\x02\x03",

            "#03609F愿大家得到\x01",
            "女神的保佑。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_BFF")

    label("loc_BB5")


    #C0012
    ChrTalk(
        0x8,
        (
            "#03600F我首先准备去玛因兹\x01",
            "那边一趟。\x02\x03",

            "#03609F愿大家得到\x01",
            "女神的保佑。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BFF")

    Jump("loc_13CA")

    label("loc_C04")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_C12")
    Jump("loc_13CA")

    label("loc_C12")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_C20")
    Jump("loc_13CA")

    label("loc_C20")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_C2E")
    Jump("loc_13CA")

    label("loc_C2E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_D77")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CFD")

    #C0013
    ChrTalk(
        0x8,
        (
            "#03601F我今天本来准备\x01",
            "去玛因兹的……\x01",
            "没想到竟然会发生这种事。\x02\x03",

            "#03603F……我经常去玛因兹\x01",
            "做生意，镇上的各位\x01",
            "都很关照我。\x02\x03",

            "#03608F但如今我却不能为他们做任何事，\x01",
            "真是惭愧啊……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_D72")

    label("loc_CFD")


    #C0014
    ChrTalk(
        0x8,
        (
            "#03603F……我经常去玛因兹\x01",
            "做生意，镇上的各位\x01",
            "都很关照我。\x02\x03",

            "#03608F但如今我却不能为他们做任何事，\x01",
            "真是惭愧啊……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D72")

    Jump("loc_13CA")

    label("loc_D77")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_D85")
    Jump("loc_13CA")

    label("loc_D85")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_D93")
    Jump("loc_13CA")

    label("loc_D93")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_E71")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_E10")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x177, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DBA")
    Call(0, 15)
    Jump("loc_E0B")

    label("loc_DBA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x177, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DCC")
    Call(0, 18)
    Jump("loc_E0B")

    label("loc_DCC")


    #C0015
    ChrTalk(
        0x8,
        (
            "#03600F我稍后会开车把村长\x01",
            "送回村里。\x02\x03",

            "各位，\x01",
            "请小心行事。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E0B")

    Jump("loc_E6C")

    label("loc_E10")


    #C0016
    ChrTalk(
        0x8,
        (
            "#03601F总之，\x01",
            "先整理一下昨天\x01",
            "调查到的情报吧。\x02\x03",

            "#03603F另外，\x01",
            "稍后可以找\x01",
            "伊安律师谈谈。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E6C")

    Jump("loc_13CA")

    label("loc_E71")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_E7F")
    Jump("loc_13CA")

    label("loc_E7F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_E8D")
    Jump("loc_13CA")

    label("loc_E8D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_FE7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14A, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F85")

    #C0017
    ChrTalk(
        0x8,
        "#03605F啊，是各位啊。\x02",
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x101,
        "#00000F晚上好，哈罗德先生。\x02",
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x102,
        (
            "#00104F从二层传来了很香的味道……\x01",
            "您太太正在\x01",
            "准备晚餐吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x8,
        (
            "#03609F嗯，是啊。\x01",
            "而且柯林今天\x01",
            "也在帮忙呢。\x02\x03",

            "#03604F呵呵，我刚刚\x01",
            "工作归来，\x01",
            "肚子已经饿扁了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x14A, 6)
    Jump("loc_FE2")

    label("loc_F85")


    #C0021
    ChrTalk(
        0x8,
        (
            "#03600F柯林好像\x01",
            "也在帮忙做\x01",
            "今天的晚饭呢。\x02\x03",

            "#03609F呵呵，他们会做些什么呢？\x01",
            "真是期待啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FE2")

    Jump("loc_13CA")

    label("loc_FE7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_FF5")
    Jump("loc_13CA")

    label("loc_FF5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1003")
    Jump("loc_13CA")

    label("loc_1003")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_1249")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x134, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11E4")

    #C0022
    ChrTalk(
        0x8,
        (
            "#03603F每当像现在这样\x01",
            "一个人静静独处时，\x01",
            "就会不由自主地思考一些事情。\x02\x03",

            "曾经救下柯林的\x01",
            "那个紫发女孩……\x02\x03",

            "#03608F我是不是永远\x01",
            "没机会见到她了呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x101,
        "#00005F这、这个……\x02",
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x8,
        (
            "#03604F哈哈，虽然现在\x01",
            "没有任何线索，\x01",
            "但我仍旧抱有一丝希望。\x02\x03",

            "#03600F如果以后有机会见面……\x01",
            "我一定要当面向她道谢。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x101,
        (
            "#00008F（紫色头发的女孩……\x01",
            "  玲已经和艾丝蒂尔他们\x01",
            "  回利贝尔了呢……）\x02\x03",

            "#00003F（那孩子还需要一些时间\x01",
            "  来调整自己的心情……\x01",
            "  希望她有朝一日还会再来。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x134, 0)
    Jump("loc_1244")

    label("loc_11E4")


    #C0026
    ChrTalk(
        0x8,
        (
            "#03603F曾经救下柯林的\x01",
            "那个紫发女孩……\x02\x03",

            "#03600F如果以后能和她见面，\x01",
            "我一定要当面向她道谢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1244")

    Jump("loc_13CA")

    label("loc_1249")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_13CA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12F, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1268")
    TalkEnd(0xFE)
    Call(0, 14)
    Return()

    label("loc_1268")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_136B")

    #C0027
    ChrTalk(
        0x8,
        (
            "#03600F最近的生意状况\x01",
            "很不错。\x02\x03",

            "#03604F我也有空休息一下，\x01",
            "和家人团聚在\x01",
            "一起了。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x102,
        (
            "#00100F呵呵，哈罗德先生平时打下了坚实基础，\x01",
            "如今终于有所回报了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x8,
        (
            "#03609F哈哈，那个……\x01",
            "太过奖了。\x02\x03",

            "#03600F其实只要能养活家人，\x01",
            "我就已经满足了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_13CA")

    label("loc_136B")


    #C0030
    ChrTalk(
        0x8,
        (
            "#03600F各位，如果今后有什么事情，\x01",
            "随时欢迎来我家。\x02\x03",

            "只要我能帮得上忙，\x01",
            "一定会全力相助的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13CA")

    TalkEnd(0xFE)
    Return()

    # Function_6_8F3 end

    def Function_7_13CE(): pass

    label("Function_7_13CE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_151B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1496")

    #C0031
    ChrTalk(
        0x9,
        (
            "#03708F我本想让他再\x01",
            "多休息一段时间……\x02\x03",

            "#03700F但哈罗德·海瓦斯就是这样一个\x01",
            "善良温柔，愿意为他人着想的人。\x02\x03",

            "#03709F既然他想为大家做些什么，\x01",
            "我们自然也会全力支持他。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1516")

    label("loc_1496")


    #C0032
    ChrTalk(
        0x9,
        (
            "#03700F哈罗德·海瓦斯就是这样一个\x01",
            "善良温柔，愿意为他人着想的人。\x02\x03",

            "#03709F既然他想为大家做些什么，\x01",
            "我们自然也会全力支持他。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1516")

    Jump("loc_21D6")

    label("loc_151B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_1529")
    Jump("loc_21D6")

    label("loc_1529")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_15A7")

    #C0033
    ChrTalk(
        0x9,
        (
            "#03708F今后克洛斯贝尔究竟会\x01",
            "怎么样呢……\x02\x03",

            "#03710F老公和柯林该不会遇到什么意外吧……\x01",
            "我最担心的就是这一点。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21D6")

    label("loc_15A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_16E0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_165A")

    #C0034
    ChrTalk(
        0x9,
        (
            "#03700F我老公今天要去\x01",
            "玛因兹了解情况。\x02\x03",

            "不久前发生了袭击事件，\x01",
            "他希望为那里的人\x01",
            "做一些力所能及的事情……\x02\x03",

            "#03709F老公的善良性格\x01",
            "再次让我感到骄傲。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_16DB")

    label("loc_165A")


    #C0035
    ChrTalk(
        0x9,
        (
            "#03700F由于不久前发生了袭击事件，\x01",
            "我老公希望为玛因兹的人\x01",
            "做一些力所能及的事情……\x02\x03",

            "#03709F老公的善良性格\x01",
            "再次让我感到骄傲。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16DB")

    Jump("loc_21D6")

    label("loc_16E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_17F5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17B1")

    #C0036
    ChrTalk(
        0x9,
        (
            "#03708F在听到事件报道的一瞬间，\x01",
            "我脑子里想到的只是\x01",
            "『老公没被卷进去，真是太好了』。\x02\x03",

            "但转念想想，玛因兹的人们\x01",
            "如今正处于强烈的恐惧中，\x01",
            "而我却……\x02\x03",

            "#03710F……都开始讨厌自己了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_17F0")

    label("loc_17B1")


    #C0037
    ChrTalk(
        0x9,
        (
            "#03708F……总之，\x01",
            "希望女神能引导我们\x01",
            "将这起事件早日解决。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17F0")

    Jump("loc_21D6")

    label("loc_17F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_187A")

    #C0038
    ChrTalk(
        0x9,
        (
            "#03700F我老公今天去\x01",
            "贝尔加德门卸货了。\x02\x03",

            "#03708F听说昨天有人在西克洛斯\x01",
            "贝尔街道目击到了巨大怪物，\x01",
            "真是有些担心……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21D6")

    label("loc_187A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_1A56")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x177, 2)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16C, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_198F")

    #C0039
    ChrTalk(
        0x9,
        (
            "#03705F啊，是你们啊。\x02\x03",

            "我老公和村长先生\x01",
            "一起去阿尔摩利卡村了……\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x101,
        (
            "#00003F（虽然很想和他们一起\x01",
            "  将那起事件调查到最后……\x01",
            "  但现在最优先的任务还是确认事故现场。）\x02\x03",

            "（至于阿尔摩利卡村那边的事情，\x01",
            "  也只有交给哈罗德先生来处理了。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x16C, 7)
    Jump("loc_1A51")

    label("loc_198F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A07")

    #C0041
    ChrTalk(
        0x9,
        (
            "#03700F辛迪刚才过来\x01",
            "和我说……\x02\x03",

            "有很多辆急救车\x01",
            "从西街开过。\x02\x03",

            "#03708F不知为何，总觉得忐忑不安……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1A51")

    label("loc_1A07")


    #C0042
    ChrTalk(
        0x9,
        (
            "#03708F听说有很多辆急救车\x01",
            "从西街开过。\x02\x03",

            "不知为何，总觉得忐忑不安……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A51")

    Jump("loc_21D6")

    label("loc_1A56")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1CF1")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1B75")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B02")

    #C0043
    ChrTalk(
        0x9,
        (
            "#03700F刚才接到了老公的联络，\x01",
            "他说阿尔摩利卡村的事件\x01",
            "已经顺利解决了。\x02\x03",

            "#03708F话说回来，没想到是诈骗啊……\x01",
            "世上竟有这么坏的人。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1B70")

    label("loc_1B02")


    #C0044
    ChrTalk(
        0x9,
        (
            "#03700F听说阿尔摩利卡村的事件\x01",
            "已经顺利解决了。\x02\x03",

            "#03708F话说回来，没想到是诈骗啊……\x01",
            "世上竟有这么坏的人。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B70")

    Jump("loc_1CEC")

    label("loc_1B75")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x177, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1BDB")

    #C0045
    ChrTalk(
        0x9,
        (
            "#03700F村长先生的儿子\x01",
            "好像被卷到了\x01",
            "很棘手的事情中……\x02\x03",

            "#03708F但愿可以\x01",
            "尽早解决。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CEC")

    label("loc_1BDB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C81")

    #C0046
    ChrTalk(
        0x9,
        (
            "#03700F村长先生似乎\x01",
            "相当担心呢……\x02\x03",

            "#03708F毕竟是自己儿子的事情，\x01",
            "这也是当然的……\x02\x03",

            "#03700F但担心过度会影响到身体的，\x01",
            "必须要先让他冷静下来啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1CEC")

    label("loc_1C81")


    #C0047
    ChrTalk(
        0x9,
        (
            "#03700F担心过度会影响到身体的，\x01",
            "必须要先让他冷静下来啊。\x02\x03",

            "家里应该还存着一些\x01",
            "带有镇静效果的香草茶……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1CEC")

    Jump("loc_21D6")

    label("loc_1CF1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1D85")

    #C0048
    ChrTalk(
        0x9,
        (
            "#03700F阿尔摩利卡村的村长先生\x01",
            "向我老公发来了联络。\x02\x03",

            "好像是有什么事情要商量……\x01",
            "似乎并不是生意方面的问题，\x01",
            "究竟发生了什么事呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21D6")

    label("loc_1D85")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1E76")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E1B")

    #C0049
    ChrTalk(
        0x9,
        (
            "#03700F我昨晚和柯林\x01",
            "一起做了咖喱……\x02\x03",

            "但做得好像太多了，\x01",
            "现在还剩下不少呢。\x02\x03",

            "#03709F呵呵，暂时也只能\x01",
            "连吃几餐咖喱了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1E71")

    label("loc_1E1B")


    #C0050
    ChrTalk(
        0x9,
        (
            "#03700F昨晚的咖喱……\x01",
            "好像做的太多了。\x02\x03",

            "#03709F呵呵，暂时也只能\x01",
            "连吃几餐咖喱了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E71")

    Jump("loc_21D6")

    label("loc_1E76")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_1EE3")

    #C0051
    ChrTalk(
        0x9,
        (
            "#03700F接下来只要等着煮熟就好了。\x02\x03",

            "#03709F呵呵，做得很棒哦，柯林。\x01",
            "爸爸一定也会很高兴的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21D6")

    label("loc_1EE3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1F4F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1EFE")
    Call(0, 8)
    Jump("loc_1F4A")

    label("loc_1EFE")


    #C0052
    ChrTalk(
        0x9,
        (
            "#03700F我正要带柯林一起出去\x01",
            "买些东西。\x02\x03",

            "#03709F呵呵，他好像\x01",
            "很兴奋呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F4A")

    Jump("loc_21D6")

    label("loc_1F4F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2055")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1FF2")

    #C0053
    ChrTalk(
        0x9,
        (
            "#03700F我前几天见到了曾经\x01",
            "住在这附近的库雷优夫人。\x02\x03",

            "她的生活好像已经稳定下来了，\x01",
            "看上去非常平静……\x02\x03",

            "#03709F呵呵，我也可以放心了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2050")

    label("loc_1FF2")


    #C0054
    ChrTalk(
        0x9,
        (
            "#03700F库雷优夫人一家\x01",
            "现在住在东街的\x01",
            "一间公寓里。\x02\x03",

            "他们好像住得很习惯，\x01",
            "我也可以放心了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2050")

    Jump("loc_21D6")

    label("loc_2055")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_2174")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_210F")

    #C0055
    ChrTalk(
        0x9,
        (
            "#03700F曾经住在这附近的本德先生一家\x01",
            "在不久之前搬走了。\x02\x03",

            "#03708F他们在搬走时\x01",
            "还过来和我们打了个招呼……\x01",
            "但之后就再也没有联系了。\x02\x03",

            "希望他们现在过得还好……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_216F")

    label("loc_210F")


    #C0056
    ChrTalk(
        0x9,
        (
            "#03700F我和本德先生的夫人\x01",
            "关系很好，\x01",
            "以前经常一起做料理。\x02\x03",

            "#03708F希望他们现在过得还好……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_216F")

    Jump("loc_21D6")

    label("loc_2174")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_21D6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12F, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2193")
    TalkEnd(0xFE)
    Call(0, 14)
    Return()

    label("loc_2193")


    #C0057
    ChrTalk(
        0x9,
        (
            "#03700F以前真是承蒙\x01",
            "各位的帮助。\x02\x03",

            "今后也请大家\x01",
            "继续关照我们。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_21D6")

    TalkEnd(0xFE)
    Return()

    # Function_7_13CE end

    def Function_8_21DA(): pass

    label("Function_8_21DA")

    OP_4B(0x9, 0xFF)
    OP_4B(0xA, 0xFF)

    #C0058
    ChrTalk(
        0x9,
        (
            "#03700F柯林，还记得\x01",
            "今天要去买什么吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0xA,
        (
            "#03805F嗯，那个……\x01",
            "胡萝卜、土豆、\x01",
            "洋葱，还有……\x02\x03",

            "#03809F……咖喱汁！\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x9,
        (
            "#03709F呵呵，完全正确，\x01",
            "那我们就赶快去买吧。\x02",
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

    # Function_8_21DA end

    def Function_9_22A5(): pass

    label("Function_9_22A5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2392")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2332")

    #C0061
    ChrTalk(
        0xA,
        (
            "#03800F我和妈妈要为辛苦工作\x01",
            "的爸爸做盒饭～\x02\x03",

            "#03809F卡米尤的妈妈\x01",
            "给了我们很多蔬菜～\x01",
            "嘿嘿嘿，好像很好吃呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_238D")

    label("loc_2332")


    #C0062
    ChrTalk(
        0xA,
        (
            "#03800F我还想再去阿尔摩利卡村～\x02\x03",

            "#03809F我和卡米尤、普莉他们约好了，\x01",
            "以后还要一起玩～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_238D")

    Jump("loc_2A9A")

    label("loc_2392")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_23A0")
    Jump("loc_2A9A")

    label("loc_23A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_2403")

    #C0063
    ChrTalk(
        0xA,
        (
            "#03805F爸爸和妈妈好像\x01",
            "都很担心的样子～\x02\x03",

            "我们正要出去玩呢，\x01",
            "到底发生什么事了～？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A9A")

    label("loc_2403")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_24DD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2489")

    #C0064
    ChrTalk(
        0xA,
        (
            "#03800F过几天，我要和\x01",
            "爸爸妈妈一起\x01",
            "出去玩了～\x02\x03",

            "#03809F好像是要去一个很漂亮的地方～\x01",
            "嘿嘿嘿，好期待啊～\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_24D8")

    label("loc_2489")


    #C0065
    ChrTalk(
        0xA,
        (
            "#03800F过几天，我们要去一个\x01",
            "很漂亮的地方玩～\x02\x03",

            "#03809F好兴奋……好期待啊～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_24D8")

    Jump("loc_2A9A")

    label("loc_24DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_2547")

    #C0066
    ChrTalk(
        0xA,
        (
            "#03800F爸爸说今天\x01",
            "要去工作，\x01",
            "但是还没有出门～\x02\x03",

            "#3802F是不是改变计划，\x01",
            "要休息一天了～？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A9A")

    label("loc_2547")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_25A6")

    #C0067
    ChrTalk(
        0xA,
        (
            "#03802F看啊看啊，\x01",
            "窗外趴着一只青蛙～\x02\x03",

            "#03809F它的肚子一鼓一鼓的，好可爱啊～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A9A")

    label("loc_25A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_2606")

    #C0068
    ChrTalk(
        0xA,
        (
            "#03802F辛迪姐姐\x01",
            "刚才给我带来了\x01",
            "她自己烤的甜曲奇～\x02\x03",

            "#03809F又脆又香～真好吃～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A9A")

    label("loc_2606")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_275A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x177, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2673")

    #C0069
    ChrTalk(
        0xA,
        (
            "#03800F爸爸说，\x01",
            "今天有重要的事情要谈，\x01",
            "让我待在二层别下来～\x02\x03",

            "是工作的事情吗～？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2755")

    label("loc_2673")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_26BB")

    #C0070
    ChrTalk(
        0xA,
        (
            "#03805F一个人玩\x01",
            "好无聊～\x02\x03",

            "爸爸能不能\x01",
            "早点回来呢～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2755")

    label("loc_26BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_270E")

    #C0071
    ChrTalk(
        0xA,
        (
            "#03805F啊，这里\x01",
            "有蜂蜜～\x02\x03",

            "#03809F（舔）\x01",
            "嘿嘿嘿，真甜～\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    ClearChrFlags(0xA, 0x10)
    Jump("loc_2755")

    label("loc_270E")


    #C0072
    ChrTalk(
        0xA,
        (
            "#03809F这瓶蜂蜜\x01",
            "是爸爸之前\x01",
            "给我带回的礼物～\x02\x03",

            "我最喜欢这种蜂蜜了～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2755")

    Jump("loc_2A9A")

    label("loc_275A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2829")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_27E3")

    #C0073
    ChrTalk(
        0xA,
        (
            "#03805F爸爸今天休息，但还是出门了，\x01",
            "不知道去了什么地方～\x02\x03",

            "是不是突然接到了\x01",
            "着急的工作呢～？\x01",
            "好失望啊……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2824")

    label("loc_27E3")


    #C0074
    ChrTalk(
        0xA,
        (
            "#03805F爸爸明明和我约好，\x01",
            "今天要陪我一起玩的～\x01",
            "好失望啊……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2824")

    Jump("loc_2A9A")

    label("loc_2829")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2871")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2844")
    Call(0, 10)
    Jump("loc_286C")

    label("loc_2844")


    #C0075
    ChrTalk(
        0xA,
        (
            "#03809F嘿嘿嘿，辛迪姐姐\x01",
            "表扬我了～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_286C")

    Jump("loc_2A9A")

    label("loc_2871")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_28CA")

    #C0076
    ChrTalk(
        0xA,
        (
            "#03802F今天的晚饭\x01",
            "是咖喱哦～\x02\x03",

            "#03809F嘿嘿，\x01",
            "菜是我切的～\x01",
            "很厉害吧～？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A9A")

    label("loc_28CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_293D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_28E5")
    Call(0, 8)
    Jump("loc_2938")

    label("loc_28E5")


    #C0077
    ChrTalk(
        0xA,
        (
            "#03800F我今天要帮\x01",
            "妈妈一起\x01",
            "做晚饭哦～\x02\x03",

            "#03809F爸爸回家以后，\x01",
            "一定会大吃一惊～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2938")

    Jump("loc_2A9A")

    label("loc_293D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2990")

    #C0078
    ChrTalk(
        0xA,
        (
            "#03800F爸爸今天出去工作了～\x02\x03",

            "#03802F他还会给我带回\x01",
            "很多礼物吗～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A9A")

    label("loc_2990")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_2A17")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_29E8")

    #C0079
    ChrTalk(
        0xA,
        (
            "#03802F（狼吞虎咽）。\x02\x03",

            "#03809F嗯嗯……\x01",
            "嘿嘿嘿，真好吃～\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2A12")

    label("loc_29E8")


    #C0080
    ChrTalk(
        0xA,
        (
            "#03809F嘿嘿嘿，妈妈做的\x01",
            "料理真好吃～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A12")

    Jump("loc_2A9A")

    label("loc_2A17")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_2A9A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12F, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A36")
    TalkEnd(0xFE)
    Call(0, 14)
    Return()

    label("loc_2A36")


    #C0081
    ChrTalk(
        0xA,
        (
            "#03805F听爸爸提起之后，\x01",
            "我也好想见那个\x01",
            "紫色头发的小姐姐啊～\x02\x03",

            "#03809F嘿嘿嘿，以后还能再见面吧～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A9A")

    TalkEnd(0xFE)
    Return()

    # Function_9_22A5 end

    def Function_10_2A9E(): pass

    label("Function_10_2A9E")

    OP_4B(0xA, 0xFF)
    OP_4B(0xB, 0xFF)

    #C0082
    ChrTalk(
        0xA,
        (
            "#03802F辛迪姐姐～\x02\x03",

            "我今天做了\x01",
            "咖喱哦～\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0xB,
        (
            "哎，柯林做咖喱吗？\x01",
            "好厉害啊～！\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0xB,
        (
            "比我哥哥\x01",
            "都能干呢。\x02",
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

    # Function_10_2A9E end

    def Function_11_2B29(): pass

    label("Function_11_2B29")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2BD0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B47")
    Call(0, 10)
    Jump("loc_2BCB")

    label("loc_2B47")


    #C0085
    ChrTalk(
        0xFE,
        (
            "呵呵，我今天想让\x01",
            "索菲亚夫人教我\x01",
            "美味点心的制作方法。\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0xFE,
        (
            "话说回来，柯林的年纪虽小，\x01",
            "但却非常能干呢……\x01",
            "真希望我哥哥能学学他。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2BCB")

    Jump("loc_2C1E")

    label("loc_2BD0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_2C1E")

    #C0087
    ChrTalk(
        0xFE,
        (
            "啊，柯林真是的，\x01",
            "直接就伸手抓着吃。\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0xFE,
        "呵呵，这孩子真会捣蛋～\x02",
    )

    CloseMessageWindow()

    label("loc_2C1E")

    TalkEnd(0xFE)
    Return()

    # Function_11_2B29 end

    def Function_12_2C22(): pass

    label("Function_12_2C22")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2E0F")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C6A")

    #C0089
    ChrTalk(
        0xFE,
        (
            "抱歉，哈罗德，\x01",
            "给你添麻烦了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E0F")

    label("loc_2C6A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x177, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C7C")
    Call(0, 15)
    Jump("loc_2E0F")

    label("loc_2C7C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E0F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x177, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x177, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2D0F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x177, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2CA8")
    Call(0, 18)
    Jump("loc_2D0A")

    label("loc_2CA8")


    #C0090
    ChrTalk(
        0xFE,
        (
            "我们帮伊安律师\x01",
            "找到要找的东西之后，\x01",
            "就会回村子了。\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0xFE,
        (
            "各位……\x01",
            "迪利克的事情\x01",
            "就拜托你们了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D0A")

    Jump("loc_2E0F")

    label("loc_2D0F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2DAE")

    #C0092
    ChrTalk(
        0xFE,
        (
            "我身为阿尔摩利卡村的村长\x01",
            "及迪利克的父亲，却什么都做不了，\x01",
            "实在是没用……\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0xFE,
        (
            "一切都靠你们了，\x01",
            "一定要揭穿那个名叫敏涅斯的男人的真面目。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_2E0F")

    label("loc_2DAE")


    #C0094
    ChrTalk(
        0xFE,
        "我什么都做不了，真是没用……\x02",
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0xFE,
        (
            "一切都靠你们了，\x01",
            "一定要揭穿那个名叫敏涅斯的男人的真面目。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E0F")

    TalkEnd(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x177, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x177, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2E27")
    OP_93(0xC, 0x10E, 0x0)

    label("loc_2E27")

    Return()

    # Function_12_2C22 end

    def Function_13_2E28(): pass

    label("Function_13_2E28")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x177, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E3D")
    Call(0, 18)
    Jump("loc_3007")

    label("loc_2E3D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F6B")

    #C0096
    ChrTalk(
        0xD,
        (
            "#02200F我所寻找的证据，\x01",
            "恐怕只能在敏涅斯彻底走投无路之后\x01",
            "起到些稳定局面的辅助作用。\x02\x03",

            "总之，你们还是尽快\x01",
            "赶往阿尔摩利卡村为好。\x02\x03",

            "#02203F如果那个名叫敏涅斯的男人真的是诈骗犯，\x01",
            "他的计划恐怕已经\x01",
            "进行到最终阶段了。\x02\x03",

            "#02200F不过，你们一定可以凭借\x01",
            "手中的证据来阻止他，\x01",
            "祝大家一切顺利。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_3007")

    label("loc_2F6B")


    #C0097
    ChrTalk(
        0xD,
        (
            "#02203F如果那个名叫敏涅斯的男人真的是诈骗犯，\x01",
            "他的计划恐怕已经\x01",
            "进行到最终阶段了。\x02\x03",

            "#02200F不过，你们一定可以凭借\x01",
            "手中的证据来阻止他，\x01",
            "祝大家一切顺利。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3007")

    TalkEnd(0xFE)
    Return()

    # Function_13_2E28 end

    def Function_14_300B(): pass

    label("Function_14_300B")

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
        "#11P#03705F啊，你们是……\x02",
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0x8,
        "#5P#03609F哦哦，是支援科的各位！\x02",
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0xA,
        "#11P#03802F大家好～！\x02",
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0x101,
        (
            "#12P#00000F好久不见了，\x01",
            "哈罗德先生，索菲亚夫人。\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x102,
        (
            "#12P#00102F呵呵，柯林\x01",
            "也很有精神啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0x8,
        (
            "#5P#03600F托大家的福……\x01",
            "自那之后，再没发生过什么意外，\x01",
            "我们一直过着平稳的生活。\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0x109,
        (
            "#12P#10105F罗伊德警官，\x01",
            "你们和这家人\x01",
            "好像很熟啊？\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0x105,
        (
            "#12P#10304F呵呵，看起来，\x01",
            "似乎有过不少来往呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0x8,
        (
            "#5P#03600F嗯，在柯林行踪不明的时候，\x01",
            "支援科的各位曾帮了我们\x01",
            "很大的忙。\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0x9,
        (
            "#11P#03709F现在想起来，\x01",
            "也仍然觉得感激不尽。\x02\x03",

            "#03700F我们现在能像这样幸福地生活，\x01",
            "全都是托各位的福。\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0x101,
        (
            "#12P#00012F哪、哪里……\x01",
            "其实我们并没帮上什么忙。\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0x8,
        (
            "#5P#03600F请不要谦虚……\x01",
            "老实说，无论怎么道谢，\x01",
            "也无法表达我的感激之情。\x02\x03",

            "#03608F说心里话，\x01",
            "我也很想向当时出手帮忙\x01",
            "的那个女孩当面道谢……\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0xA,
        (
            "#11P#03805F是在说那个\x01",
            "紫色头发的小姐姐吗～？\x02\x03",

            "#03809F我也好想再见到她啊～\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0x9,
        (
            "#11P#03700F呵呵……是啊，\x01",
            "我也很想见她一面呢。\x02\x03",

            "各位也不了解\x01",
            "那孩子的行踪吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0x102,
        (
            "#12P#00103F……很遗憾……\x01",
            "自那次的事情之后，\x01",
            "我们也没有再见过她了。\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0x8,
        (
            "#5P#03603F唔，这样啊……\x02\x03",

            "#03600F算了，如果有缘，\x01",
            "今后一定还会再见面的。\x02\x03",

            "我们能做的，恐怕也只有\x01",
            "耐心等待那一天的来临了。\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0x101,
        (
            "#12P#00003F（……『那个孩子』\x01",
            "  现在已经离开\x01",
            "  克洛斯贝尔了……）\x02\x03",

            "#00008F（看来直到最后，\x01",
            "  她也没有向哈罗德先生\x01",
            "  他们说明真相……）\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0x8,
        (
            "#5P#03600F……那么，各位，\x01",
            "如果今后有什么事情，\x01",
            "随时欢迎来我家。\x02\x03",

            "只要我能帮得上忙，\x01",
            "一定会全力相助的。\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0x101,
        "#12P#00000F嗯，谢谢您了。\x02",
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0xA,
        "#11P#03809F嘿嘿嘿，还要再来哦～\x02",
    )

    CloseMessageWindow()
    OP_5A()
    SetChrSubChip(0x9, 0x0)
    SetChrSubChip(0xA, 0x0)
    Sleep(50)
    SetScenarioFlags(0x12F, 7)
    EventEnd(0x5)
    Return()

    # Function_14_300B end

    def Function_15_3678(): pass

    label("Function_15_3678")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x177, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_38AE")

    #C0118
    ChrTalk(
        0x101,
        (
            "#00000F打扰了，\x01",
            "我们是特别任务支援科。\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0xC,
        "哦哦，特别任务支援科的各位……\x02",
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0xC,
        (
            "感谢你们特意过来，\x01",
            "继续处理昨天那件事情。\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0x8,
        "#03600F谢谢大家。\x02",
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0x101,
        (
            "#00005F特鲁塔村长，\x01",
            "究竟发生什么事了？\x02\x03",

            "#00003F昨天的事情\x01",
            "有什么进展了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0xC,
        (
            "嗯……看样子，\x01",
            "事态似乎比我想象中的\x01",
            "更加严重呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0xC,
        (
            "我想马上向你们\x01",
            "交代委托内容……\x01",
            "现在是否方便呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3914")

    label("loc_38AE")


    #C0125
    ChrTalk(
        0xC,
        (
            "看样子，\x01",
            "事态似乎比我想象中的\x01",
            "更加严重呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0xC,
        (
            "我想马上向你们\x01",
            "交代委托内容……\x01",
            "现在是否方便呢？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3914")

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

    # Function_15_3678 end

    def Function_16_3959(): pass

    label("Function_16_3959")

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
            "【接受】\x01",      # 0
            "【放弃】\x01",      # 1
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
        (0, "loc_39BB"),
        (1, "loc_39C3"),
        (SWITCH_DEFAULT, "loc_3A53"),
    )


    label("loc_39BB")

    Call(0, 17)
    Jump("loc_3A53")

    label("loc_39C3")


    #C0127
    ChrTalk(
        0x101,
        (
            "#00006F对不起……\x01",
            "我们现在有些忙。\x02",
        )
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0xC,
        "唔唔，这样啊……\x02",
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0xC,
        (
            "那就请你们有空时\x01",
            "再来一趟吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0xC,
        (
            "如今实在是需要\x01",
            "你们的帮助。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x177, 1)

    label("loc_3A53")

    Return()

    # Function_16_3959 end

    def Function_17_3A54(): pass

    label("Function_17_3A54")


    #C0131
    ChrTalk(
        0x101,
        "#00000F嗯，愿闻其详。\x02",
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0x102,
        (
            "#00100F您刚才说昨天之后，\x01",
            "情况又有所进展……\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0xC,
        "嗯……正是如此。\x02",
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0xC,
        (
            "我昨晚去了迪利克\x01",
            "投宿的酒馆，\x01",
            "再次尝试说服他。\x02",
        )
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0xC,
        (
            "我认为那个名叫敏涅斯\x01",
            "的外国人有太多可疑之处，\x01",
            "希望他不要再与其来往。\x02",
        )
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0x104,
        (
            "#00306F这……\x01",
            "说得还真是直截了当啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0xC,
        (
            "嗯，可是……\x01",
            "迪利克还是\x01",
            "听不进我的话。\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0xC,
        (
            "另外，我还了解到了\x01",
            "一个新情况。\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0xC,
        (
            "所以才立刻赶到\x01",
            "哈罗德这里来商量。\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0x103,
        (
            "#00205F新情况……？\x02\x03",

            "那个名叫敏涅斯的人\x01",
            "做了什么吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0x8,
        (
            "#03603F从村长口中听说的时候，\x01",
            "连我也吃了一惊……\x02\x03",

            "#03601F敏涅斯想侵吞村子的胃口，\x01",
            "似乎比预想中还要大。\x02",
        )
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0x102,
        (
            "#00105F那个……\x01",
            "究竟是怎么回事呢？\x02\x03",

            "我们昨天就已知道，\x01",
            "敏涅斯得到了各位村民的信任……\x02",
        )
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0xC,
        "但事实上，那个名叫敏涅斯的人……\x02",
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0xC,
        (
            "不仅准备使用村子的私有地，\x01",
            "而且还从村民的手中征集了\x01",
            "花田及土地的产权证。\x02",
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
        "#00005F土、土地产权证……！？\x02",
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0x105,
        (
            "#10303F唔……但这样的话，\x01",
            "有个问题就很令人在意了。\x02\x03",

            "#10301F敏涅斯先生究竟\x01",
            "动用了怎样的手段，\x01",
            "才能得到那么重要的东西？\x02",
        )
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0x8,
        (
            "#03601F嗯，据我所知……\x01",
            "他是以『扩大花田』为由，\x01",
            "向大家征收土地产权证。\x02\x03",

            "从村民们手中将一块块小型土地\x01",
            "汇集在一起，扩大花田的面积，\x01",
            "从而提高蜂蜜的收获效率……\x02\x03",

            "#03603F不仅如此，他还提议\x01",
            "由昆西公司来承担花田的管理工作，\x01",
            "以便减轻大家在收获时的劳累……\x02",
        )
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0x109,
        (
            "#10101F这些情况……\x01",
            "昨天也曾谈及呢。\x02\x03",

            "#10103F从表面上看，倒是一件好事……\x02",
        )
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0x101,
        (
            "#00001F嗯……\x01",
            "而且可以说『十分诱人』。\x02\x03",

            "#00003F不过，如果土地产权证落入他人手中……\x01",
            "一旦对方恶意利用，\x01",
            "恐怕就再也无法收回了。\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0xC,
        (
            "嗯……那个名叫敏涅斯的男人\x01",
            "明显十分可疑。\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0xC,
        (
            "如果只是占用私有地，\x01",
            "就算万一发生什么情况，\x01",
            "对村民们也几乎没有损害……\x02",
        )
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0xC,
        (
            "但如果村里的土地\x01",
            "出现什么意外，\x01",
            "后果可就不堪设想了。\x02",
        )
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0x104,
        (
            "#00301F原来如此，现在的情况\x01",
            "的确是不容乐观啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0xC,
        (
            "所以，希望你们能以\x01",
            "更加明确的形式来戳穿那个男人\x01",
            "的伪装，使他暴露出真实面目。\x02",
        )
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0xC,
        (
            "如今还没有确定对方的嫌疑，\x01",
            "向警察提出这样的委托\x01",
            "是不是有些不妥……？\x02",
        )
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0x101,
        (
            "#00003F不……我们支援科在一般情况下\x01",
            "并不会被警察局的硬性规章所约束。\x02\x03",

            "#00000F如今既然已经发现那个\x01",
            "名叫敏涅斯的男人有可疑之处，\x01",
            "我们自然会展开谨慎调查。\x02",
        )
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0xC,
        (
            "抱歉……\x01",
            "真是给你们\x01",
            "添麻烦了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)
    Sleep(300)

    #C0158
    ChrTalk(
        0x102,
        (
            "#00100F那么，我们要从何处\x01",
            "开始着手呢？\x02\x03",

            "#00103F老实说，我们现在\x01",
            "没有任何线索……\x02",
        )
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0x105,
        (
            "#10300F确实，如今根本没有\x01",
            "任何调查依据呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0x101,
        "#00006F说的也是啊……\x02",
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0x8,
        (
            "#03600F既然如此……\x01",
            "各位先去找伊安律师\x01",
            "谈谈如何？\x02",
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
        "#00205F找伊安律师……？\x02",
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0x8,
        (
            "#03600F嗯，虽然我们现在只知道\x01",
            "那个名叫敏涅斯的男人比较可疑，\x01",
            "对具体情况毫无了解……\x02\x03",

            "但只要向伊安律师说明情况，\x01",
            "他说不定可以看出\x01",
            "对方的犯罪征兆呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0x101,
        (
            "#00004F原来如此，\x01",
            "这主意好像不错呢。\x02\x03",

            "#00000F只要能对敏涅斯的行为\x01",
            "有多一点的了解，\x01",
            "就有可能找到调查的切入点……\x02",
        )
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0x8,
        (
            "#03603F不过，在独立宣言发表之后，\x01",
            "伊安律师一直在处理相关的问题，\x01",
            "似乎非常繁忙。\x02\x03",

            "#03608F说不定他现在\x01",
            "并不在事务所……\x02",
        )
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0x104,
        (
            "#00300F不管怎么说，\x01",
            "我们先去法律事务所看看吧。\x02\x03",

            "如果他不在，\x01",
            "我们再想下一步的办法。\x02",
        )
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0x101,
        (
            "#00000F嗯……\x01",
            "赶快去看看吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0x8,
        (
            "#03600F那就麻烦你们\x01",
            "跑一趟了。\x02\x03",

            "我准备向商业伙伴\x01",
            "探听一些有关昆西公司\x01",
            "与敏涅斯的传闻。\x02",
        )
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0x103,
        (
            "#00200F那可真是帮大忙了……\x01",
            "拜托您了。\x02",
        )
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0xC,
        (
            "抱歉啊……\x01",
            "全都得靠你们。\x02",
        )
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0xC,
        (
            "我什么都做不了，\x01",
            "真是没用……\x02",
        )
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0x101,
        (
            "#00000F哪里的话……\x01",
            "请交给我们吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0x105,
        (
            "#10300F村长先生留在这里\x01",
            "等我们就好了。\x02\x03",

            "您不妨向女神祈祷，\x01",
            "祝愿我们带回好消息。\x02",
        )
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0xC,
        (
            "嗯……\x01",
            "拜托你们了。\x02",
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
            "任务【调查可疑商人】\x07\x00",
            "开始！\x02",
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

    # Function_17_3A54 end

    def Function_18_4802(): pass

    label("Function_18_4802")

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
        "哦哦，是你们……\x02",
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0xD,
        "#11P#02200F你们已经回来了啊。\x02",
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0x101,
        (
            "#00000F伊安律师……\x01",
            "您来了啊。\x02\x03",

            "哈罗德先生\x01",
            "也回来了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0x8,
        (
            "#03604F嗯，我已经咨询过\x01",
            "商业伙伴们了。\x02\x03",

            "#03601F你们有什么收获吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0x101,
        (
            "#00000F嗯，托您的福，\x01",
            "掌握到了不少情报。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x8, 500)
    Sleep(300)

    #C0181
    ChrTalk(
        0x102,
        (
            "#00100F哈罗德先生，\x01",
            "您探听到什么消息了吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x102, 500)
    Sleep(300)

    #C0182
    ChrTalk(
        0x8,
        (
            "#03603F嗯……可以这么说吧。\x02\x03",

            "#03608F但我并不清楚\x01",
            "这些情报有何意义……\x02",
        )
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0x105,
        (
            "#10302F呵呵，好不容易探听到了情报，\x01",
            "不管是什么都无所谓，\x01",
            "赶快说来听听吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0x103,
        (
            "#00200F嗯，请说说吧。\x01",
            "说不定与目前的状况\x01",
            "存在着什么联系呢。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 500)
    Sleep(300)

    #C0185
    ChrTalk(
        0x8,
        (
            "#03603F嗯……也是呢。\x02\x03",

            "#03601F我询问了多名贸易伙伴，\x01",
            "问他们是否听说过\x01",
            "敏涅斯这个名字。\x02\x03",

            "结果得知……敏涅斯在\x01",
            "来到克洛斯贝尔之后，\x01",
            "立刻就开始进行某项调查了。\x02",
        )
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0x102,
        "#00105F某项调查是指……？\x02",
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0x8,
        (
            "#03601F嗯，那就是……\x01",
            "调查克洛斯贝尔\x01",
            "各地的『地价』。\x02",
        )
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0x104,
        "#00305F『地价』吗……\x02",
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0x109,
        (
            "#10103F也就是说，敏涅斯做了一些\x01",
            "房地产商才会做的事情……\x02\x03",

            "#10105F不过，他有调查\x01",
            "那种事情的必要吗……\x02",
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
            "#00001F说不定……\x01",
            "这是个牵扯到敏涅斯\x01",
            "真实目的的重要证言。\x02",
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
        "真、真的吗？\x02",
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0xD,
        (
            "#11P#02203F嗯，或许有些道理。\x02\x03",

            "#02200F另外，我也想到了一件事情，\x01",
            "说不定能发挥一些作用。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x102, 0x5A, 0x1F4)
    Sleep(300)

    #C0193
    ChrTalk(
        0x101,
        "#00005F哎……？\x02",
    )

    CloseMessageWindow()

    #C0194
    ChrTalk(
        0xD,
        (
            "#11P#02200F哈罗德，还有特鲁塔村长。\x02\x03",

            "你们可以来我的事务所，\x01",
            "帮我找些东西吗？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4EAB():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_4EAB)
    Sleep(50)

    def lambda_4EBB():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_4EBB)
    Sleep(300)

    #C0195
    ChrTalk(
        0x8,
        "#03605F伊安律师……？\x02",
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0xC,
        (
            "我没问题……\x01",
            "是很重要的东西吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0xD,
        (
            "#11P#02203F不，并不是具有\x01",
            "决定性效果的证据……\x02\x03",

            "#02200F恐怕只能在敏涅斯彻底走投无路之后\x01",
            "起到些稳定局面的辅助作用。\x02",
        )
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0x104,
        "#00305F嗯～？真是听不明白啊……\x02",
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0xD,
        (
            "#11P#02200F好了，也不知道是否还来得及，\x01",
            "总之不要太过期待。\x02\x03",

            "#02203F特别任务支援科的诸位，\x01",
            "你们还是尽快\x01",
            "赶往阿尔摩利卡村为好。\x02\x03",

            "#02200F如果那个名叫敏涅斯的男人真的是诈骗犯，\x01",
            "他的计划恐怕已经\x01",
            "进行到最终阶段了。\x02\x03",

            "不过，你们一定可以凭借\x01",
            "手中的证据来阻止他。\x02",
        )
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0x101,
        "#00001F……嗯，我明白了！\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0x10E, 0x1F4)
    Sleep(300)

    #C0201
    ChrTalk(
        0x101,
        (
            "#00001F那么，各位……\x01",
            "我们马上前往阿尔摩利卡村吧。\x02\x03",

            "揭穿敏涅斯的真面目，\x01",
            "阻止他们完成进一步的交易！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_513D():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_513D)
    Sleep(50)

    def lambda_514D():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_514D)
    Sleep(50)

    def lambda_515D():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_515D)
    Sleep(50)

    def lambda_516D():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_516D)
    Sleep(50)

    def lambda_517D():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_517D)
    Sleep(300)

    #C0202
    ChrTalk(
        0x102,
        "#00101F嗯……出发吧！\x02",
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

    # Function_18_4802 end

    SaveToFile()

Try(main)
