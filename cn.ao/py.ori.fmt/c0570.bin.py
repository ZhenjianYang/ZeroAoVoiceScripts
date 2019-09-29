from ScenarioHelper import *

def main():
    CreateScenaFile(
        "c0570.bin",                # FileName
        "c0570",                    # MapName
        "c0570",                    # Location
        0x0027,                     # MapIndex
        "ed7117",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 39, 0, 1, 0, 2],
    )

    BuildStringList((
        "c0570",                  # 0
        "埃里克",                 # 1
        "桑多拉",                 # 2
        "赛尔丹分部长",           # 3
        "克潘",                   # 4
        "彼德",                   # 5
        "达德利搜查官",           # 6
        "爱丽斯",                 # 7
        "揽客员比修",             # 8
        "奥利维尔",               # 9
        "尼尔森",                 # 10
    ))

    AddCharChip((
        "chr/ch32202.itc",                   # 00
        "chr/ch23600.itc",                   # 01
        "chr/ch24202.itc",                   # 02
        "chr/ch22000.itc",                   # 03
        "chr/ch26802.itc",                   # 04
        "chr/ch00902.itc",                   # 05
        "chr/ch26900.itc",                   # 06
        "chr/ch26700.itc",                   # 07
    ))

    DeclNpc(0,       0,       6400,    180,  261,  0x0, 0,   3,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(-4699,   79,      4449,    0,    261,  0x0, 0,   4,   0,   255, 255, 0,   6,   255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 0,   7,   255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   1,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   2,   0,   255, 255, 0,   9,   255,  0)
    DeclNpc(2109,    150,     4250,    0,    389,  0x0, 0,   5,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(-5420,   0,       1649,    90,   385,  0x0, 0,   6,   0,   0,   0,   0,   13,  255,  0)
    DeclNpc(-1090,   0,       3950,    135,  385,  0x0, 0,   7,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    405,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclActor(0,       0,       5000,    1000,    0,       1500,    6400,    0x007E, 0,  4,  0x0000)
    DeclActor(-7600,   750,     5400,    1200,    -7600,   800,     5400,    0x007C, 0,  3,  0x0000)

    ChipFrameInfo(604, 0)                                        # 0

    ScpFunction((
        "Function_0_25C",          # 00, 0
        "Function_1_314",          # 01, 1
        "Function_2_52D",          # 02, 2
        "Function_3_5D6",          # 03, 3
        "Function_4_685",          # 04, 4
        "Function_5_689",          # 05, 5
        "Function_6_19A0",         # 06, 6
        "Function_7_26DD",         # 07, 7
        "Function_8_2774",         # 08, 8
        "Function_9_27F1",         # 09, 9
        "Function_10_2880",        # 0A, 10
        "Function_11_28FB",        # 0B, 11
        "Function_12_3022",        # 0C, 12
        "Function_13_3083",        # 0D, 13
        "Function_14_30AF",        # 0E, 14
        "Function_15_40BD",        # 0F, 15
        "Function_16_4A68",        # 10, 16
        "Function_17_4AB8",        # 11, 17
    ))


    def Function_0_25C(): pass

    label("Function_0_25C")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_29C"),
        (1, "loc_2A8"),
        (2, "loc_2B4"),
        (3, "loc_2C0"),
        (4, "loc_2CC"),
        (5, "loc_2D8"),
        (6, "loc_2E4"),
        (SWITCH_DEFAULT, "loc_2F0"),
    )


    label("loc_29C")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_2FC")

    label("loc_2A8")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_2FC")

    label("loc_2B4")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_2FC")

    label("loc_2C0")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_2FC")

    label("loc_2CC")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_2FC")

    label("loc_2D8")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_2FC")

    label("loc_2E4")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2FC")

    label("loc_2F0")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2FC")

    label("loc_2FC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_313")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2FC")

    label("loc_313")

    Return()

    # Function_0_25C end

    def Function_1_314(): pass

    label("Function_1_314")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6A, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6A, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6A, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3A7")
    ClearChrFlags(0xA, 0x40)
    ClearChrFlags(0xA, 0x80)
    SetChrChipByIndex(0xA, 0x0)
    SetChrSubChip(0xA, 0x0)
    EndChrThread(0xA, 0x0)
    SetChrBattleFlags(0xA, 0x4)
    SetChrPos(0xA, -8400, 100, -500, 90)
    ClearChrFlags(0xB, 0x40)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, -8900, 0, 1500, 90)
    ClearChrFlags(0xC, 0x40)
    ClearChrFlags(0xC, 0x80)
    SetChrChipByIndex(0xC, 0x2)
    SetChrSubChip(0xC, 0x0)
    EndChrThread(0xC, 0x0)
    SetChrBattleFlags(0xC, 0x4)
    SetChrPos(0xC, -5800, 100, -2050, 0)

    label("loc_3A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x156, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x76, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x76, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x76, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3DB")
    SetScenarioFlags(0x0, 5)
    SetMapFlags(0x10000000)
    Event(0, 15)

    label("loc_3DB")

    SetChrChipByIndex(0x9, 0x4)
    SetChrSubChip(0x9, 0x0)
    EndChrThread(0x9, 0x0)
    SetChrBattleFlags(0x9, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3FA")
    Jump("loc_50E")

    label("loc_3FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_412")
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    Jump("loc_50E")

    label("loc_412")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_420")
    Jump("loc_50E")

    label("loc_420")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_444")
    ClearChrFlags(0xD, 0x80)
    SetChrChipByIndex(0xD, 0x5)
    SetChrSubChip(0xD, 0x0)
    EndChrThread(0xD, 0x0)
    SetChrBattleFlags(0xD, 0x4)
    Jump("loc_50E")

    label("loc_444")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_452")
    Jump("loc_50E")

    label("loc_452")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_465")
    SetChrFlags(0x9, 0x10)
    Jump("loc_50E")

    label("loc_465")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_482")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_47D")
    SetChrFlags(0x9, 0x10)

    label("loc_47D")

    Jump("loc_50E")

    label("loc_482")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_495")
    SetChrFlags(0x9, 0x10)
    Jump("loc_50E")

    label("loc_495")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_4A3")
    Jump("loc_50E")

    label("loc_4A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_4B6")
    SetChrFlags(0x9, 0x10)
    Jump("loc_50E")

    label("loc_4B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_4C4")
    Jump("loc_50E")

    label("loc_4C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_4D2")
    Jump("loc_50E")

    label("loc_4D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 4)), scpexpr(EXPR_END)), "loc_4F7")
    SetChrFlags(0x9, 0x10)
    OP_63(0x9, 0x0, 1700, 0x1C, 0x21, 0xFA, 0x0)
    Jump("loc_50E")

    label("loc_4F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_505")
    Jump("loc_50E")

    label("loc_505")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_50E")

    label("loc_50E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_52C")
    ClearScenarioFlags(0x22, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x95, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_52C")
    SetScenarioFlags(0x0, 6)
    Event(0, 17)

    label("loc_52C")

    Return()

    # Function_1_314 end

    def Function_2_52D(): pass

    label("Function_2_52D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_549")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x97), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_594")

    label("loc_549")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_565")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x7D), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_594")

    label("loc_565")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_57F")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x243), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 5)
    Jump("loc_594")

    label("loc_57F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_594")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 6)

    label("loc_594")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5B5")
    Sound(128, 1, 50, 0)

    label("loc_5B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5CC")
    OP_7D(0xD2, 0xD2, 0xE6, 0x0, 0x0)

    label("loc_5CC")

    OP_10(0x0, 0x1)
    OP_10(0x1, 0x0)
    OP_10(0x2, 0x0)
    Return()

    # Function_2_52D end

    def Function_3_5D6(): pass

    label("Function_3_5D6")

    SetChrName("")

    #A0001
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "摆放着《面向商务人士的招牌饮品》。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x2, 0x0)"), scpexpr(EXPR_END)), "loc_681")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B2(0x17)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_681")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0002
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "『浓厚卡布奇诺』\x07\x00",
            "的做法已经学会了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_681")

    TalkEnd(0xFF)
    Return()

    # Function_3_5D6 end

    def Function_4_685(): pass

    label("Function_4_685")

    Call(0, 5)
    Return()

    # Function_4_685 end

    def Function_5_689(): pass

    label("Function_5_689")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x139, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_76F")

    #C0003
    ChrTalk(
        0x8,
        "欢迎光……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x105, 500)
    Sleep(300)
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0004
    ChrTalk(
        0x8,
        (
            "哎呀……\x01",
            "这不是瓦吉先生吗！\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x8,
        (
            "您很少在这种时间\x01",
            "过来呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x105,
        (
            "#10303F呵呵，\x01",
            "我正在巡逻。\x02\x03",

            "#10300F下次有空时，\x01",
            "再来喝酒吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x8,
        "嗯，恭候您的大驾。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x139, 3)
    TalkEnd(0x8)
    Return()

    label("loc_76F")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_779")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_199C")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "对话\x01",      # 0
            "购物\x01",      # 1
            "放弃\x01",      # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7C9")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_7C9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7E9")
    OP_AF(0x42)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1997")

    label("loc_7E9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7FD")
    Jump("loc_1997")

    label("loc_7FD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1997")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_96E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8F6")

    #C0008
    ChrTalk(
        0x8,
        (
            "近期之内，『黑月』大概就能\x01",
            "掌控地下世界的实权了。\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x8,
        (
            "虽然黑月和鲁巴彻不同，\x01",
            "并不是一个喜欢张扬的组织，\x01",
            "但他们的威严感却相当强烈。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x8,
        (
            "后巷这一带也\x01",
            "多少会受点影响……\x01",
            "看来还是留意一些为好。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_969")

    label("loc_8F6")


    #C0011
    ChrTalk(
        0x8,
        (
            "近期之内，『黑月』大概就能\x01",
            "掌控地下世界的实权了。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x8,
        (
            "后巷这一带也\x01",
            "多少会受点影响……\x01",
            "看来还是留意一些为好。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_969")

    Jump("loc_1997")

    label("loc_96E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_9D7")

    #C0013
    ChrTalk(
        0x8,
        (
            "那些怪物似乎\x01",
            "没有进入后巷。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x8,
        (
            "不过，还不知道\x01",
            "会有怎样的危险，\x01",
            "请大家随意进店避难。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1997")

    label("loc_9D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_B2C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AA3")

    #C0015
    ChrTalk(
        0x8,
        (
            "这次的独立宣言，应该也会\x01",
            "对地下世界造成巨大影响。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x8,
        (
            "国防军今后恐怕会对\x01",
            "帝国、共和国系的\x01",
            "黑手党组织进行取缔。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x8,
        (
            "形势风云突变……\x01",
            "但克洛斯贝尔或许\x01",
            "正需要下这样的猛药。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_B27")

    label("loc_AA3")


    #C0018
    ChrTalk(
        0x8,
        (
            "国防军今后恐怕会对\x01",
            "帝国、共和国系的\x01",
            "黑手党组织进行取缔。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x8,
        (
            "独立宣言使形势风云突变……\x01",
            "但克洛斯贝尔或许\x01",
            "正需要下这样的猛药。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B27")

    Jump("loc_1997")

    label("loc_B2C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_C81")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C01")

    #C0020
    ChrTalk(
        0x8,
        (
            "竟然袭击克洛斯贝尔市……\x01",
            "『赤色星座』的那些家伙\x01",
            "真是做出了很不得了的事啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x8,
        (
            "我们店的小道消息非常灵通，\x01",
            "但却没察觉到丝毫预兆……\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x8,
        (
            "他们恐怕从很久以前\x01",
            "就开始制定周密的计划了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_C7C")

    label("loc_C01")


    #C0023
    ChrTalk(
        0x8,
        (
            "我们店的小道消息非常灵通，\x01",
            "但却没察觉到丝毫预兆……\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x8,
        (
            "他们恐怕从很久以前\x01",
            "就开始制定袭击\x01",
            "克洛斯贝尔市的周密计划了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C7C")

    Jump("loc_1997")

    label("loc_C81")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_DD6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D54")

    #C0025
    ChrTalk(
        0x8,
        (
            "看到警察那慌张的样子之后，\x01",
            "我才察觉到\x01",
            "『赤色星座』的人消失了。\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x8,
        (
            "他们是通过地下暗道逃过警察监视，\x01",
            "前往玛因兹地区的吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x8,
        (
            "……这起占领事件究竟意味着什么，\x01",
            "我实在是难以预测。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_DD1")

    label("loc_D54")


    #C0028
    ChrTalk(
        0x8,
        (
            "看到警察那慌张的样子之后，\x01",
            "我才察觉到\x01",
            "『赤色星座』的人消失了。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x8,
        (
            "……这起占领事件究竟意味着什么，\x01",
            "我实在是难以预测。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DD1")

    Jump("loc_1997")

    label("loc_DD6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_F0D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E9C")

    #C0030
    ChrTalk(
        0x8,
        (
            "昨天的脱轨事故……\x01",
            "听说是由一只出现在\x01",
            "附近的巨大怪物引发的。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x8,
        (
            "但在临近居民投票的时期发生这种事，\x01",
            "总觉得不像是单纯由魔兽引起的事故呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x8,
        "……实在是非常可疑啊。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_F08")

    label("loc_E9C")


    #C0033
    ChrTalk(
        0x8,
        (
            "在临近居民投票的时期\x01",
            "发生昨天那种脱轨事故，总觉得\x01",
            "不像是单纯由魔兽引起的。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x8,
        "……实在是非常可疑啊。\x02",
    )

    CloseMessageWindow()

    label("loc_F08")

    Jump("loc_1997")

    label("loc_F0D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_F57")

    #C0035
    ChrTalk(
        0x8,
        "远处传来了急救车的警笛声……\x02",
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x8,
        "……真是让人不安啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1997")

    label("loc_F57")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_10D8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1068")

    #C0037
    ChrTalk(
        0x8,
        (
            "听说阿尔泰尔市那边\x01",
            "昨天逮捕了几个\x01",
            "共和国的恐怖分子……\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x8,
        (
            "有传闻说，黑月的人\x01",
            "也在暗地追踪。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x81, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_103B")

    #C0039
    ChrTalk(
        0x101,
        (
            "#00005F（黑月当时也在场吗……）\x02\x03",

            "#00003F（完全没有察觉到，\x01",
            "  真是一群滴水不漏的人啊。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1060")

    label("loc_103B")


    #C0040
    ChrTalk(
        0x8,
        (
            "不愧是黑月……\x01",
            "果然滴水不漏啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1060")

    SetScenarioFlags(0x0, 0)
    Jump("loc_10D3")

    label("loc_1068")


    #C0041
    ChrTalk(
        0x8,
        (
            "据说阿尔泰尔市那边\x01",
            "昨天逮捕共和国恐怖分子时，\x01",
            "黑月也在暗中行动。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x8,
        (
            "不愧是黑月……\x01",
            "果然滴水不漏啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10D3")

    Jump("loc_1997")

    label("loc_10D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1232")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11B7")

    #C0043
    ChrTalk(
        0x8,
        (
            "听说在通商会议的时候，\x01",
            "『赤色星座』受帝国政府的委托，\x01",
            "击退了恐怖分子……\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x8,
        (
            "不过，深红商会最近\x01",
            "倒是没惹什么麻烦，\x01",
            "一直都很安分。\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x8,
        (
            "……且不论好坏，\x01",
            "总之可以深切感受到\x01",
            "他们是职业猎兵啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_122D")

    label("loc_11B7")


    #C0046
    ChrTalk(
        0x8,
        (
            "在通商会议时大显身手的\x01",
            "深红商会，最近一直\x01",
            "都很安分。\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x8,
        (
            "……且不论好坏，\x01",
            "总之可以深切感受到\x01",
            "他们是职业猎兵啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_122D")

    Jump("loc_1997")

    label("loc_1232")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1367")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12EA")

    #C0048
    ChrTalk(
        0x8,
        (
            "猎兵团『赤色星座』，\x01",
            "还有港湾区的『黑月』……\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x8,
        (
            "今天是正式会议的召开日，\x01",
            "警察似乎对这些势力\x01",
            "加强了警戒。\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x8,
        (
            "来后巷的警官们\x01",
            "也处于相当\x01",
            "紧张的状态。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1362")

    label("loc_12EA")


    #C0051
    ChrTalk(
        0x8,
        (
            "今天是正式会议的召开日，\x01",
            "警察似乎对『赤色星座』和『黑月』\x01",
            "加强了警戒。\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x8,
        (
            "来后巷的警官们\x01",
            "也处于相当\x01",
            "紧张的状态。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1362")

    Jump("loc_1997")

    label("loc_1367")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_14C7")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x76, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1459")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1403")

    #C0053
    ChrTalk(
        0x8,
        (
            "通商会议……\x01",
            "终于要开始了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x8,
        (
            "负责警备后巷的\x01",
            "警察们似乎\x01",
            "也提高了警惕。\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x8,
        (
            "看来他们果然很\x01",
            "戒备深红商会。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1454")

    label("loc_1403")


    #C0056
    ChrTalk(
        0x8,
        (
            "负责警备后巷的\x01",
            "警察们似乎\x01",
            "也提高了警惕。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x8,
        (
            "看来他们果然很\x01",
            "戒备深红商会。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1454")

    Jump("loc_14C2")

    label("loc_1459")


    #C0058
    ChrTalk(
        0x8,
        (
            "奥利维尔先生真是个\x01",
            "相当有意思的人。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x8,
        (
            "如果可能，真希望那位演奏家\x01",
            "能和我正式签约啊……\x01",
            "真是遗憾。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14C2")

    Jump("loc_1997")

    label("loc_14C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1650")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15C7")

    #C0060
    ChrTalk(
        0x8,
        (
            "新搬进后巷那栋大楼的\x01",
            "『深红商会』……\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x8,
        (
            "与骚动不断的\x01",
            "鲁巴彻相比，\x01",
            "感觉是个比较安分的组织。\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x8,
        (
            "可是，据说其真面目是\x01",
            "西塞姆里亚最强的猎兵团之一\x01",
            "『赤色星座』……\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x8,
        (
            "虽说表面上很安分，\x01",
            "但给人带来的威压感\x01",
            "却比鲁巴彻更强。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_164B")

    label("loc_15C7")


    #C0064
    ChrTalk(
        0x8,
        (
            "据说深红商会的真面目是\x01",
            "西塞姆里亚最强的猎兵团之一\x01",
            "『赤色星座』……\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x8,
        (
            "虽说表面上很安分，\x01",
            "但给人带来的威压感\x01",
            "却比鲁巴彻更强。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_164B")

    Jump("loc_1997")

    label("loc_1650")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 4)), scpexpr(EXPR_END)), "loc_16F9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16B7")

    #C0066
    ChrTalk(
        0x8,
        (
            "……雨好像\x01",
            "越下越大了。\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x8,
        (
            "差不多也该把桑多拉小姐\x01",
            "叫醒，让她回家了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_16F4")

    label("loc_16B7")


    #C0068
    ChrTalk(
        0x8,
        "……请问有何吩咐？\x02",
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x8,
        (
            "店里现在只有\x01",
            "我和桑多拉小姐……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16F4")

    Jump("loc_1997")

    label("loc_16F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_1842")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17C6")

    #C0070
    ChrTalk(
        0x8,
        (
            "看来鲁巴彻的旧址\x01",
            "肯定要落到黑月的\x01",
            "手里了。\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x8,
        (
            "一旦如此，黑月就将在\x01",
            "克洛斯贝尔的地下世界\x01",
            "站稳脚跟……\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0x8,
        (
            "考虑到克洛斯贝尔的现状，\x01",
            "从某种程度上说，\x01",
            "这或许也是没办法的事。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_183D")

    label("loc_17C6")


    #C0073
    ChrTalk(
        0x8,
        (
            "黑月成立了没多久，\x01",
            "就已在地下世界中崛起……\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x8,
        (
            "考虑到克洛斯贝尔的现状，\x01",
            "从某种程度上说，\x01",
            "这或许也是没办法的事。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_183D")

    Jump("loc_1997")

    label("loc_1842")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_1997")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1919")

    #C0075
    ChrTalk(
        0x8,
        (
            "鲁巴彻覆灭以后，\x01",
            "以前低调行事的恶人们\x01",
            "都逐渐现身了。\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x8,
        (
            "从这种意义上来说，\x01",
            "后巷的治安状况反而\x01",
            "变得比以前更差了。\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0x8,
        (
            "直到鲁巴彻已经覆灭的如今，\x01",
            "才深刻体会到他们拥有\x01",
            "多大的势力……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1997")

    label("loc_1919")


    #C0078
    ChrTalk(
        0x8,
        (
            "鲁巴彻覆灭以后，\x01",
            "以前低调行事的恶人们\x01",
            "都逐渐现身了。\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0x8,
        (
            "直到鲁巴彻已经覆灭的如今，\x01",
            "才深刻体会到他们拥有\x01",
            "多大的势力……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1997")

    Jump("loc_779")

    label("loc_199C")

    TalkEnd(0x8)
    Return()

    # Function_5_689 end

    def Function_6_19A0(): pass

    label("Function_6_19A0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1AAF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A68")
    SetChrSubChip(0xFE, 0x2)

    #C0080
    ChrTalk(
        0xFE,
        (
            "呜……嗝……\x01",
            "埃里克～来喝酒嘛～\x02",
        )
    )

    CloseMessageWindow()
    OP_4B(0x8, 0xFF)

    #C0081
    ChrTalk(
        0xFE,
        (
            "那诡异的雾已经散去了，\x01",
            "不是很值得庆祝吗～？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0xFE, 500)
    Sleep(300)

    #C0082
    ChrTalk(
        0x8,
        (
            "桑多拉小姐，你在这里会妨碍我工作，\x01",
            "还是快回去吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0xB4, 0x0)
    OP_4C(0x8, 0xFF)
    SetScenarioFlags(0x0, 1)
    Jump("loc_1AAA")

    label("loc_1A68")


    #C0083
    ChrTalk(
        0xFE,
        "呜……嗝，埃里克欺负人……\x02",
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0xFE,
        "不过，这种态度也很·迷·人⊥\x02",
    )

    CloseMessageWindow()

    label("loc_1AAA")

    Jump("loc_26D9")

    label("loc_1AAF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_1B25")

    #C0085
    ChrTalk(
        0xFE,
        (
            "唔唔……唔唔……\x01",
            "由于戒严令，我们店停业了，\x01",
            "所以我就来这里喝酒睡觉……\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0xFE,
        "怎么，发生了什么事吗？\x02",
    )

    CloseMessageWindow()
    Jump("loc_26D9")

    label("loc_1B25")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_1C1B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1BCC")

    #C0087
    ChrTalk(
        0xFE,
        (
            "有客人来我们店预约席位，\x01",
            "说是要召开什么\x01",
            "『纪念独立庆祝会』。\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0xFE,
        (
            "我不太了解\x01",
            "那些复杂的事情……\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0xFE,
        (
            "但大家好像都很高兴，\x01",
            "这挺好的啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1C16")

    label("loc_1BCC")


    #C0090
    ChrTalk(
        0xFE,
        (
            "我不太了解\x01",
            "那些复杂的事情……\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0xFE,
        (
            "但大家好像都很高兴，\x01",
            "这挺好的啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C16")

    Jump("loc_26D9")

    label("loc_1C1B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1DA4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D0E")

    #C0092
    ChrTalk(
        0xFE,
        (
            "袭击事件发生后，我们店\x01",
            "也自主休业了，\x01",
            "不过，今晚就要重新开店了。\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0xFE,
        (
            "市里的复兴建设工作\x01",
            "总算有点起色了，\x01",
            "我也不能一直休息下去～\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0xFE,
        (
            "虽说我们那里只是个普通的夜总会，\x01",
            "但也有一些客人期待来店呢。\x01",
            "……努力加油吧～\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1D9F")

    label("loc_1D0E")


    #C0095
    ChrTalk(
        0xFE,
        (
            "市里的复兴建设工作总算有点起色了，\x01",
            "我也不能一直休息下去～\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0xFE,
        (
            "虽说我们那里只是个普通的夜总会，\x01",
            "但也有一些客人期待来店呢。\x01",
            "……努力加油吧～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D9F")

    Jump("loc_26D9")

    label("loc_1DA4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_1ED9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E66")

    #C0097
    ChrTalk(
        0xFE,
        (
            "埃里克说，\x01",
            "深红商会是\x01",
            "猎兵团开的公司？\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0xFE,
        (
            "哇……\x01",
            "就是经营那家著名夜总会\x01",
            "『诺艾·布朗』的深红商会啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0xFE,
        (
            "本以为只是个普通的黑社会组织，\x01",
            "没想到竟然那么厉害。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1ED4")

    label("loc_1E66")


    #C0100
    ChrTalk(
        0xFE,
        (
            "经营『诺艾·布朗』的深红商会\x01",
            "竟然是猎兵团啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0xFE,
        (
            "本以为只是个普通的黑社会组织，\x01",
            "没想到竟然那么厉害。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1ED4")

    Jump("loc_26D9")

    label("loc_1ED9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1FFE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F9D")
    OP_4B(0x8, 0xFF)

    #C0102
    ChrTalk(
        0xFE,
        (
            "喂～埃里克真是的，\x01",
            "别老说些听不懂的话了，\x01",
            "来陪我喝酒啦～\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0xFE, 500)
    Sleep(300)

    #C0103
    ChrTalk(
        0x8,
        (
            "桑多拉小姐，\x01",
            "你不要总在我们店里睡觉，\x01",
            "回家好不好？\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0xFE,
        "讨厌，埃里克欺负人～\x02",
    )

    CloseMessageWindow()
    OP_93(0x8, 0xB4, 0x1F4)
    OP_4C(0x8, 0xFF)
    SetScenarioFlags(0x0, 1)
    Jump("loc_1FF9")

    label("loc_1F9D")


    #C0105
    ChrTalk(
        0xFE,
        (
            "哼，埃里克竟然\x01",
            "赶我走，好过分啊～\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0xFE,
        (
            "不过，这种态度也很·迷·人。\x01",
            "……开个玩笑啦～⊥\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1FF9")

    Jump("loc_26D9")

    label("loc_1FFE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_20F8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_20AF")

    #C0107
    ChrTalk(
        0xFE,
        (
            "唔唔……唔唔……\x01",
            "怎么样，你个可恶的色老头……！\x01",
            "记住教训吧，看打看打～\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0108
    ChrTalk(
        0xFE,
        "……嗯！？\x02",
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0xFE,
        "……怎么，是做梦啊。\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xFE, 0x10)
    SetScenarioFlags(0x0, 1)
    Jump("loc_20F3")

    label("loc_20AF")


    #C0110
    ChrTalk(
        0xFE,
        (
            "唉……\x01",
            "正做着美梦呢，\x01",
            "结果却突然醒了。\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0xFE,
        "嗯……出什么事了？\x02",
    )

    CloseMessageWindow()

    label("loc_20F3")

    Jump("loc_26D9")

    label("loc_20F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_217C")

    #C0112
    ChrTalk(
        0xFE,
        (
            "唔唔……唔唔……\x01",
            "那个色老头，总是\x01",
            "黏着人家到处乱摸……\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0xFE,
        (
            "我明明每次都跟他说，\x01",
            "我们这里不是那种店……\x01",
            "可恶……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_26D9")

    label("loc_217C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2282")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2225")

    #C0114
    ChrTalk(
        0xFE,
        (
            "听说要举办一个\x01",
            "居民投票活动。\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0xFE,
        (
            "埃里克说，\x01",
            "我们都应该去参加。\x01",
            "但说实话，我还没想好要不要去。\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0xFE,
        (
            "因为投票的时间段\x01",
            "正是我的睡觉时间。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_227D")

    label("loc_2225")


    #C0117
    ChrTalk(
        0xFE,
        (
            "老实说，我还没想好\x01",
            "要不要去参加居民投票。\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0xFE,
        (
            "因为投票的时间段\x01",
            "正是我的睡觉时间。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_227D")

    Jump("loc_26D9")

    label("loc_2282")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2369")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2322")
    OP_4B(0x8, 0xFF)

    #C0119
    ChrTalk(
        0xFE,
        (
            "埃里克……\x01",
            "再来一杯朗姆汽水……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0xFE, 500)
    Sleep(300)

    #C0120
    ChrTalk(
        0x8,
        (
            "桑多拉小姐，天都亮了，\x01",
            "你还是快回去吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0xFE,
        "讨厌，埃里克欺负人～\x02",
    )

    CloseMessageWindow()
    OP_93(0x8, 0xB4, 0x1F4)
    OP_4C(0x8, 0xFF)
    SetScenarioFlags(0x0, 1)
    Jump("loc_2364")

    label("loc_2322")


    #C0122
    ChrTalk(
        0xFE,
        (
            "埃里克欺负人～\x01",
            "偶尔也陪陪人家嘛～\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0xFE,
        (
            "难得赶上\x01",
            "人家放假呀～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2364")

    Jump("loc_26D9")

    label("loc_2369")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_244D")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x76, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_23E2")

    #C0124
    ChrTalk(
        0xFE,
        (
            "昨天店里来了个恶劣的客人，\x01",
            "我被灌了好多酒呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0xFE,
        (
            "呜……头一阵一阵地痛，\x01",
            "真是受不了啦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2448")

    label("loc_23E2")


    #C0126
    ChrTalk(
        0xFE,
        (
            "那个人的演奏\x01",
            "非常精彩啊～\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0xFE,
        (
            "我工作得很累，已经疲惫不堪了，\x01",
            "但听了他的演奏后，完全恢复了精神～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2448")

    Jump("loc_26D9")

    label("loc_244D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_24F1")

    #C0128
    ChrTalk(
        0xFE,
        (
            "深红商会搬过来之后，\x01",
            "欢乐街『诺艾·布朗』的生意\x01",
            "似乎比以前更好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0xFE,
        (
            "呼，如果能在高级夜总会工作，\x01",
            "待遇应该非常高吧。\x01",
            "能不能把我也招过去呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_26D9")

    label("loc_24F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 4)), scpexpr(EXPR_END)), "loc_2528")
    OP_64(0x9)

    #C0130
    ChrTalk(
        0xFE,
        "（打瞌睡）……\x02",
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 1700, 0x1C, 0x21, 0xFA, 0x0)
    Jump("loc_26D9")

    label("loc_2528")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_2604")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_25AA")

    #C0131
    ChrTalk(
        0xFE,
        (
            "呼～\x01",
            "完全睡着了。\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0xFE,
        (
            "陪酒工作结束之后，\x01",
            "我总会来这家店。\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0xFE,
        (
            "因为这里安静又舒服，\x01",
            "能睡得很好。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_25FF")

    label("loc_25AA")


    #C0134
    ChrTalk(
        0xFE,
        (
            "这家店总是很安静，\x01",
            "可以睡得很好。\x02",
        )
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0xFE,
        (
            "埃里克也会默默地\x01",
            "陪着我，\x01",
            "待得很舒心呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_25FF")

    Jump("loc_26D9")

    label("loc_2604")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_26D9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2681")

    #C0136
    ChrTalk(
        0xFE,
        (
            "我每天都要在夜总会中\x01",
            "挂着工作性的笑容，\x01",
            "喝一整晚的酒。\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0xFE,
        (
            "唉……\x01",
            "为什么我会\x01",
            "做这种工作呢？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_26D9")

    label("loc_2681")


    #C0138
    ChrTalk(
        0xFE,
        (
            "唉……\x01",
            "我最近觉得\x01",
            "这份工作很空虚。\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0xFE,
        (
            "但待遇还不错，\x01",
            "所以总是下不了\x01",
            "辞职的决心。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_26D9")

    TalkEnd(0xFE)
    Return()

    # Function_6_19A0 end

    def Function_7_26DD(): pass

    label("Function_7_26DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6A, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6A, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6A, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_270F")
    Call(0, 14)
    Return()

    label("loc_270F")

    TalkBegin(0xFE)

    #C0140
    ChrTalk(
        0xFE,
        (
            "我打算先找个适合\x01",
            "重新再来的新事务所。\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0xFE,
        (
            "罗伊德团员，如果有什么情况，\x01",
            "就来交换情报吧。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_7_26DD end

    def Function_8_2774(): pass

    label("Function_8_2774")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6A, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6A, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6A, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_27A6")
    Call(0, 14)
    Return()

    label("loc_27A6")

    TalkBegin(0xFE)

    #C0142
    ChrTalk(
        0xFE,
        (
            "好，我这就要\x01",
            "出去钓鱼啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0xFE,
        (
            "这点小雨，\x01",
            "我完全都不在意的说！\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_8_2774 end

    def Function_9_27F1(): pass

    label("Function_9_27F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6A, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6A, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6A, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2823")
    Call(0, 14)
    Return()

    label("loc_2823")

    TalkBegin(0xFE)

    #C0144
    ChrTalk(
        0xFE,
        (
            "话说回来，那个男人……\x01",
            "真是不可原谅啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0xFE,
        (
            "职业钓师又如何，\x01",
            "简直就是钓师之耻。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_9_27F1 end

    def Function_10_2880(): pass

    label("Function_10_2880")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18F, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2895")
    Call(0, 11)
    Jump("loc_28F7")

    label("loc_2895")


    #C0146
    ChrTalk(
        0xD,
        (
            "#00600F嗯……\x01",
            "喝完这杯，就回去工作吧。\x02\x03",

            "#00603F居民投票日已经临近，\x01",
            "还远远不到放松的时候啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_28F7")

    TalkEnd(0xFE)
    Return()

    # Function_10_2880 end

    def Function_11_28FB(): pass

    label("Function_11_28FB")

    EventBegin(0x0)
    Fade(500)
    OP_68(1500, 1430, 2330, 0)
    MoveCamera(328, 28, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(21430, 0)
    SetChrPos(0xD, 2070, 200, 4000, 180)
    SetChrPos(0x101, 680, 0, 2770, 45)
    SetChrPos(0x102, 1730, 0, 2320, 0)
    SetChrPos(0x103, 920, 0, 1020, 0)
    SetChrPos(0x104, -160, 0, 1970, 45)
    SetChrPos(0x109, -640, 0, 3120, 90)
    SetChrPos(0x105, 2330, 0, 910, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrSubChip(0xD, 0x0)
    OP_0D()

    #C0147
    ChrTalk(
        0x101,
        "#00005F达德利警官。\x02",
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0xD,
        (
            "#00603F是你们啊。\x01",
            "……没想到会在这里碰面。\x02\x03",

            "#00600F听说你们从今天开始\x01",
            "就要恢复工作了？\x02",
        )
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0x101,
        "#00000F嗯，托您的福。\x02",
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0x102,
        (
            "#6P#00100F顺便一问，\x01",
            "关于『赤色星座』的去向，\x01",
            "有没有什么新情报？\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0xD,
        (
            "#00600F哼，说来惭愧，\x01",
            "完全没有。\x02\x03",

            "帝国政府似乎也\x01",
            "不打算发表\x01",
            "新的评论。\x02\x03",

            "#00603F如果今后还要发生什么大事的话，\x01",
            "就很有可能在三天后居民投票的时候……\x02\x03",

            "#00600F现在光是为了备战那一天，\x01",
            "就已经竭尽全力了。\x02",
        )
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0x109,
        "#5P#10103F是吗……\x02",
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0x104,
        (
            "#00302F嘿，该怎么说呢……\x01",
            "你似乎散发着一股奇妙的哀愁情绪啊。\x02\x03",

            "难道是喝醉了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0xD,
        (
            "#00603F哼，我虽然喜欢喝酒，\x01",
            "但显然不会在大白天喝。\x02\x03",

            "#00600F这只是无酒精饮品而已。\x02",
        )
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0x105,
        (
            "#6P#10300F呵呵，没有酒精\x01",
            "就能酝酿出这种气氛，\x01",
            "真是厉害呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0xD)

    #C0156
    ChrTalk(
        0xD,
        (
            "#00603F……班宁斯，\x01",
            "你会喝酒吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0x101,
        (
            "#00005F嗯，还行，\x01",
            "虽然喝不了太多。\x02",
        )
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0xD,
        (
            "#00602F哼，那就比\x01",
            "盖伊那家伙差远了。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0159
    ChrTalk(
        0x101,
        (
            "#00005F达德利警官，莫非\x01",
            "您和我大哥在这里喝过酒？\x02",
        )
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0xD,
        (
            "#00603F嗯，虽然次数屈指可数。\x02\x03",

            "#00600F顺便一提，第一次来\x01",
            "这家店，就是因为盖伊的介绍。\x02\x03",

            "#00608F那家伙就擅长\x01",
            "探寻这种店。\x02",
        )
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0x101,
        (
            "#00000F哈哈，可以想象，\x01",
            "这是性格使然嘛。\x02",
        )
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0x104,
        (
            "#00300F顺带一问，\x01",
            "你和罗伊德的大哥相比，\x01",
            "谁的酒量比较大？\x02\x03",

            "以你们的个性来说，\x01",
            "应该会来场比赛什么的吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0xD,
        (
            "#00603F哼，无可奉告。\x02\x03",

            "#00602F但有一点可以告诉你们，\x01",
            "奥兰多、班宁斯……\x01",
            "我和盖伊都比你们两个能喝。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0164
    ChrTalk(
        0x104,
        (
            "#00301F什么！？你根本不知道我的酒量有多强，\x01",
            "就敢如此大言不惭……\x02\x03",

            "#00304F既然已经把话说到这份上了，\x01",
            "下次要不要用实际行动来证明？\x02",
        )
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0xD,
        "#00604F哼，要是有机会的话。\x02",
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0x101,
        (
            "#00002F啊哈哈……\x02\x03",

            "（原来达德利警官\x01",
            "  在这种方面\x01",
            "  也不肯服输啊。）\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x18F, 3)
    OP_50(0x6B, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_69(0xFF, 0x0)
    SetChrPos(0xD, 2110, 150, 4250, 0)
    SetChrPos(0x0, 1210, 0, 2500, 180)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_11_28FB end

    def Function_12_3022(): pass

    label("Function_12_3022")

    TalkBegin(0xFE)

    #C0167
    ChrTalk(
        0xFE,
        (
            "怎么回事，事情好像\x01",
            "闹得很大啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0xFE,
        (
            "反正今天也拉不到客人了，\x01",
            "就在这里老实待着吧。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_12_3022 end

    def Function_13_3083(): pass

    label("Function_13_3083")

    TalkBegin(0xFE)

    #C0169
    ChrTalk(
        0xFE,
        (
            "怎么办，\x01",
            "这下连家都不能回了……\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_13_3083 end

    def Function_14_30AF(): pass

    label("Function_14_30AF")

    EventBegin(0x0)
    OP_4B(0xB, 0xFF)
    Fade(500)
    OP_68(-5430, 1430, 390, 0)
    MoveCamera(315, 25, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(21500, 0)
    SetChrPos(0x101, -6170, 0, 1680, 180)
    SetChrPos(0x102, -5200, 0, 1810, 180)
    SetChrPos(0x109, -5400, 0, 3000, 180)
    SetChrPos(0x105, -4200, 0, 2000, 225)
    OP_0D()

    #C0170
    ChrTalk(
        0xC,
        "#6P罗伊德团员，你来了啊。\x02",
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0xA,
        "麻烦你特地跑一趟，真是不好意思。\x02",
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0xA,
        (
            "好……人已经到齐了，\x01",
            "那就赶快开始作战会议吧。\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(1000)
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch00102.itc", 0x1F)
    OP_68(-4570, 1630, -1220, 0)
    MoveCamera(318, 17, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(20220, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrPos(0xB, -8400, 0, 1500, 90)
    SetChrPos(0x101, -3100, 100, -1000, 270)
    SetChrPos(0x102, -3100, 100, 0, 270)
    SetChrPos(0x105, -4690, 0, 1380, 225)
    SetChrPos(0x109, -3190, 0, 1380, 225)
    SetChrSubChip(0xC, 0x2)
    FadeToBright(1000, 0)
    OP_0D()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7117", 0)

    #C0173
    ChrTalk(
        0xA,
        (
            "#5P首先要向罗伊德团员\x01",
            "说明一下我们的情况。\x02",
        )
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0xA,
        (
            "#5P其实，在这几个月……钓公师团的全体成员\x01",
            "一直都在闭门自省，已经停止了一切活动。\x02",
        )
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0x101,
        "#12P#00005F自、自省吗……？\x02",
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0xC,
        (
            "#6P嗯，毕竟我们的同伴——\x01",
            "约亚西姆原团员引发了\x01",
            "那种事件……\x02",
        )
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0xB,
        (
            "#5P所以，经过商讨之后，\x01",
            "大家就决定各自反省一阵子的说。\x02",
        )
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0x102,
        "#12P#00108F可是，那并不是你们的责任……\x02",
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0xA,
        "#5P我们的确与那起事件无关……\x02",
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0xA,
        (
            "#5P但身为同样热爱钓鱼的同志，我们曾与\x01",
            "约亚西姆原团员共同度过许多时光。\x02",
        )
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0xA,
        (
            "#5P……然而，我们\x01",
            "却完全没有察觉到\x01",
            "他心底的想法。\x02",
        )
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0xA,
        "#5P无论从社会角度，还是个人角度，都该承担充分责任。\x02",
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0x101,
        "#12P#00003F赛尔丹分部长……\x02",
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0xA,
        "#5P……好啦，先不提这些。\x02",
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0xA,
        (
            "#5P就在大约一周前，\x01",
            "房产公司的人突然联系了我。\x02",
        )
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0xA,
        (
            "#5P不知他们是否了解我们闭门自省的情况，\x01",
            "说是因为建筑物看上去没人使用，\x01",
            "就解除了租赁合同。\x02",
        )
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0xA,
        (
            "#5P而且还通知我，他们已经和\x01",
            "『钓皇俱乐部』签订了新合同。\x02",
        )
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0xC,
        (
            "#6P在那之后，我马上尝试联络\x01",
            "钓皇俱乐部的代表，\x01",
            "但一直联络不上……\x02",
        )
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0xB,
        (
            "#5P今天直接去了事务所，\x01",
            "刚好遇到他们的代表的说。\x02",
        )
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0xB,
        "#5P总算得知了合同的真相……\x02",
    )

    CloseMessageWindow()

    #C0191
    ChrTalk(
        0xB,
        (
            "#5P然后你们\x01",
            "就来了的说。\x02",
        )
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0x101,
        (
            "#12P#00005F原来如此，是这样啊……\x02\x03",

            "#00003F我已经大致掌握情况了。\x02",
        )
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0xA,
        (
            "#5P话说回来……\x01",
            "雷克罗德公司的『钓皇俱乐部』吗……\x02",
        )
    )

    CloseMessageWindow()

    #C0194
    ChrTalk(
        0xA,
        (
            "#5P如果他们只想扩张活动据点的话，\x01",
            "倒也不关我们的事……\x02",
        )
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0xA,
        (
            "#5P可没想到他们会\x01",
            "强夺事务所……\x02",
        )
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0xC,
        (
            "#6P嗯，而且也不清楚\x01",
            "敌视我们的理由……\x02",
        )
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0xB,
        (
            "#5P……总而言之，\x01",
            "这摆明是在为难我们的说。\x02",
        )
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0xB,
        (
            "#5P话虽如此，\x01",
            "但却没有什么\x01",
            "解决问题的办法……\x02",
        )
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0xA,
        (
            "#5P嗯，目前看来，\x01",
            "暂时也只能静观其变了。\x02",
        )
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0xA,
        (
            "#5P……但是，\x01",
            "总不能就这样\x01",
            "丢掉分部啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0xA,
        (
            "#5P虽说还不够充分……\x01",
            "但从现在开始，我们可以停止自省了。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0xB, 0xB4, 0x1F4)
    SetChrSubChip(0xC, 0x1)

    #C0202
    ChrTalk(
        0xC,
        (
            "#6P呵呵，也就是说，钓公师团·\x01",
            "克洛斯贝尔分部要恢复活动了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0203
    ChrTalk(
        0xB,
        "#11P哦哦，已经等了很久的说！\x02",
    )

    CloseMessageWindow()

    #C0204
    ChrTalk(
        0xA,
        (
            "#5P但条件是……所有人都要\x01",
            "从『新手钓师』阶段重新练起，\x01",
            "以此找回垂钓的初衷。\x02",
        )
    )

    CloseMessageWindow()

    #C0205
    ChrTalk(
        0xA,
        (
            "#5P另外，\x01",
            "『等级认证考试』\x01",
            "也暂时中止。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0206
    ChrTalk(
        0xB,
        "#11P哎……？\x02",
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    #C0207
    ChrTalk(
        0xB,
        (
            "#11P请、请等\x01",
            "一下的说。\x02",
        )
    )

    CloseMessageWindow()

    #C0208
    ChrTalk(
        0xB,
        (
            "#11P这就是说……\x01",
            "我已经不再是\x01",
            "『特级钓师』了？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xA, 0x1)

    #C0209
    ChrTalk(
        0xA,
        (
            "#5P嗯，很遗憾，正是如此，这也是为了\x01",
            "重新出发，和过去的一切划下界线。\x02",
        )
    )

    CloseMessageWindow()

    #C0210
    ChrTalk(
        0xB,
        "#11P呜，我的努力都泡汤了……\x02",
    )

    CloseMessageWindow()

    #C0211
    ChrTalk(
        0xC,
        (
            "#6P好了好了，克潘，\x01",
            "重新再努力不就好了嘛。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xB, 0x87, 0x1F4)

    #C0212
    ChrTalk(
        0xB,
        (
            "#11P呜呜……\x01",
            "原本也只是『业余钓师』的\x01",
            "彼德先生没资格安慰我的说。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x131, 0)), scpexpr(EXPR_END)), "loc_3B7F")

    #C0213
    ChrTalk(
        0x101,
        (
            "#12P#00012F啊哈哈……\x02\x03",

            "#00006F（克洛斯贝尔的『钓圣』……\x01",
            "  我可是费尽千辛万苦，才得到这个称号的。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3CA9")

    label("loc_3B7F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x131, 1)), scpexpr(EXPR_END)), "loc_3BF0")

    #C0214
    ChrTalk(
        0x101,
        (
            "#12P#00012F啊哈哈……\x02\x03",

            "#00006F（『特级钓师』……\x01",
            "  我可是付出了大量努力，才拿到这个称号的。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3CA9")

    label("loc_3BF0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x131, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5A, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3C5A")

    #C0215
    ChrTalk(
        0x101,
        (
            "#12P#00009F啊哈哈……\x02\x03",

            "#00003F（我原本也只是『新手钓师』，\x01",
            "  倒是不受什么影响。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3CA9")

    label("loc_3C5A")


    #C0216
    ChrTalk(
        0x101,
        (
            "#12P#00009F啊哈哈……\x02\x03",

            "#00006F（呼，这样一来，\x01",
            "  我的称号也被取消了啊。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3CA9")

    SetChrSubChip(0xA, 0x0)

    #C0217
    ChrTalk(
        0xA,
        (
            "#5P好，接下来，就把事先准备\x01",
            "好的新钓具套组发给你们。\x02",
        )
    )

    CloseMessageWindow()

    #C0218
    ChrTalk(
        0xA,
        (
            "#5P彼德、克潘，还有罗伊德团员，\x01",
            "收下这个吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xB, 0xB4, 0x1F4)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0219
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x14),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x14, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0220
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x3),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x3, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0221
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x189),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "×１０\x01",
            scpstr(SCPSTR_CODE_ITEM, 0x187),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "×１０收下了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x189, 10)
    AddItemNumber(0x187, 10)
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x131, 0)), scpexpr(EXPR_END)), "loc_3EDD")

    #C0222
    ChrTalk(
        0xA,
        (
            "#5P对于曾经取得过『钓圣』荣誉的\x01",
            "罗伊德团员，就给点额外奖励吧。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0223
    AnonymousTalk(
        0xFF,
        (
            "又收下了",
            scpstr(SCPSTR_CODE_ITEM, 0x189),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "×２０\x01",
            scpstr(SCPSTR_CODE_ITEM, 0x187),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "×２０。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x189, 20)
    AddItemNumber(0x187, 20)
    SetMessageWindowPos(14, 280, 60, 3)

    #C0224
    ChrTalk(
        0x101,
        "#12P#00002F非、非常感谢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3FDE")

    label("loc_3EDD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x131, 1)), scpexpr(EXPR_END)), "loc_3FDE")

    #C0225
    ChrTalk(
        0xA,
        (
            "#5P对于曾经取得过『特级钓师』称号的\x01",
            "克潘团员和罗伊德团员，\x01",
            "就给点额外奖励吧。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0226
    AnonymousTalk(
        0xFF,
        (
            "又收下了",
            scpstr(SCPSTR_CODE_ITEM, 0x189),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "×１０\x01",
            scpstr(SCPSTR_CODE_ITEM, 0x187),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "×１０。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x189, 10)
    AddItemNumber(0x187, 10)
    SetMessageWindowPos(14, 280, 60, 3)

    #C0227
    ChrTalk(
        0x101,
        "#12P#00002F非、非常感谢。\x02",
    )

    CloseMessageWindow()

    #C0228
    ChrTalk(
        0xB,
        "#5P太谢谢了，那我就收下了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3FDE")

    label("loc_3FDE")


    #C0229
    ChrTalk(
        0xA,
        (
            "#5P好，接下来就可以\x01",
            "自由行动了。\x02",
        )
    )

    CloseMessageWindow()

    #C0230
    ChrTalk(
        0xA,
        (
            "#5P我打算先去找个能让\x01",
            "我们重新开始的新事务所……\x02",
        )
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0xA,
        (
            "#5P至于钓皇俱乐部的动向，\x01",
            "我们近期再交换一下情报吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0232
    ChrTalk(
        0x101,
        "#12P#00000F嗯，明白了。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_D7(0x1E)
    OP_D7(0x1F)
    SetChrSubChip(0xC, 0x0)
    StopSound(128, 2000, 40)
    StopBGM(0xBB8)
    WaitBGM()
    SetScenarioFlags(0x22, 4)
    NewScene("c0500", 106, 0, 0)
    IdleLoop()
    Return()

    # Function_14_30AF end

    def Function_15_40BD(): pass

    label("Function_15_40BD")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch46500.itc", 0x1E)
    LoadChrToIndex("apl/ch51230.itc", 0x1F)
    LoadChrToIndex("apl/ch51270.itc", 0x20)
    OP_68(1350, 1830, 1580, 0)
    MoveCamera(315, 26, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(21000, 0)
    SetChrPos(0x101, -100, 0, 1950, 270)
    SetChrPos(0x102, -100, 0, 3150, 270)
    SetChrPos(0x104, 1060, 0, 2520, 270)
    SetChrPos(0x109, 2020, 0, 1660, 270)
    SetChrPos(0x105, 1590, 0, 3440, 270)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x10, 0x80)
    SetChrChipByIndex(0x10, 0x1F)
    SetChrSubChip(0x10, 0x0)
    EndChrThread(0x10, 0x0)
    SetChrBattleFlags(0x10, 0x4)
    SetChrFlags(0x10, 0x2)
    SetChrFlags(0x10, 0x10)
    SetChrFlags(0x10, 0x20)
    SetChrPos(0x10, -13920, 550, 4900, 45)
    BeginChrThread(0x10, 0, 0, 16)
    OP_4B(0x8, 0xFF)
    SetChrSubChip(0x9, 0x1)
    SetChrPos(0x8, -5430, 0, 6530, 0)
    TurnDirection(0x8, 0x10, 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
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
    Sleep(1000)
    OP_68(-13000, 1830, 4650, 3000)
    MoveCamera(292, 17, 0, 3000)
    OP_6E(400, 3000)
    SetCameraDistance(19150, 3000)
    OP_6F(0x79)

    #C0233
    ChrTalk(
        0x101,
        "#00005F（奥、奥利维尔先生……？）\x02",
    )

    CloseMessageWindow()

    #C0234
    ChrTalk(
        0x105,
        (
            "#10300F（哦……\x01",
            "  弹得挺不错嘛。）\x02",
        )
    )

    CloseMessageWindow()
    OP_68(-7750, 1830, 3690, 3000)
    MoveCamera(301, 22, 0, 3000)
    OP_6E(400, 3000)
    SetCameraDistance(21280, 3000)
    OP_6F(0x79)
    StopBGM(0x3E8)
    WaitBGM()
    Fade(500)
    SetChrFlags(0x10, 0x8000)
    ClearChrFlags(0x10, 0x4)
    ClearChrFlags(0x10, 0x2)
    ClearChrFlags(0x10, 0x10)
    ClearChrFlags(0x10, 0x20)
    EndChrThread(0x10, 0x0)
    Sound(812, 0, 100, 0)
    SetChrChipByIndex(0x10, 0x1E)
    SetChrSubChip(0x10, 0x0)
    SetChrPos(0x10, -11230, 400, 3690, 90)
    OP_0D()

    #C0235
    ChrTalk(
        0x10,
        (
            "#5P#13904F呵……\x01",
            "感谢各位的倾听。\x02",
        )
    )

    CloseMessageWindow()
    Sound(971, 0, 50, 0)

    #C0236
    ChrTalk(
        0x9,
        "精彩～！\x02",
    )

    CloseMessageWindow()

    #C0237
    ChrTalk(
        0x9,
        "小哥，你弹得好棒啊！\x02",
    )

    CloseMessageWindow()

    #C0238
    ChrTalk(
        0x8,
        (
            "如何？要不要在这里\x01",
            "演奏一阵子呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0239
    ChrTalk(
        0x8,
        (
            "我会支付一些\x01",
            "表演费的。\x02",
        )
    )

    CloseMessageWindow()

    #C0240
    ChrTalk(
        0x10,
        (
            "#5P#13909F哦哦，您的请求\x01",
            "真是深得我心啊！\x02\x03",

            "#13900F我当然是\x01",
            "乐意之至。\x02",
        )
    )

    CloseMessageWindow()

    #C0241
    ChrTalk(
        0x101,
        "#00007F等、等一下！！\x02",
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7117", 0)
    OP_68(-7500, 1630, 2280, 3000)
    MoveCamera(325, 17, 0, 3000)
    OP_6E(400, 3000)
    SetCameraDistance(22280, 3000)

    def lambda_4488():
        OP_97(0xFE, 0xFFFFE4A8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4488)
    Sleep(50)

    def lambda_44A5():
        OP_97(0xFE, 0xFFFFE4A8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_44A5)
    Sleep(50)

    def lambda_44C2():
        OP_97(0xFE, 0xFFFFE4A8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_44C2)
    Sleep(50)

    def lambda_44DF():
        OP_97(0xFE, 0xFFFFE4A8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_44DF)
    Sleep(50)

    def lambda_44FC():
        OP_97(0xFE, 0xFFFFE4A8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_44FC)
    WaitChrThread(0x105, 1)
    OP_6F(0x79)
    OP_63(0x10, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0242
    ChrTalk(
        0x10,
        (
            "#5P#13905F咦、咦咦，\x01",
            "这么快就被你们找到了吗……\x02",
        )
    )

    CloseMessageWindow()

    #C0243
    ChrTalk(
        0x101,
        (
            "#12P#00006F你、你怎么还悠闲地\x01",
            "找了份工作啊！\x02",
        )
    )

    CloseMessageWindow()

    #C0244
    ChrTalk(
        0x104,
        "#12P#00306F真是位特立独行的老兄啊……\x02",
    )

    CloseMessageWindow()

    #C0245
    ChrTalk(
        0x10,
        (
            "#5P#13904F呵，别这么说，\x01",
            "受到如此夸奖，我会害羞啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0246
    ChrTalk(
        0x104,
        "#12P#00301F没人在夸你啊！\x02",
    )

    CloseMessageWindow()

    #C0247
    ChrTalk(
        0x109,
        "#12P#10101F这次一定要把你带走。\x02",
    )

    CloseMessageWindow()

    #C0248
    ChrTalk(
        0x10,
        (
            "#5P#13910F哎呀呀，你们\x01",
            "可真是想不开。\x02\x03",

            "#13900F人生在世，应该过得更加快乐、\x01",
            "更加舒心才对啊。\x02\x03",

            "#13904F不如让我为你们\x01",
            "献上一曲吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    Sound(802, 0, 100, 0)
    SetChrChipByIndex(0x10, 0x20)
    SetChrSubChip(0x10, 0x0)
    OP_0D()

    #C0249
    ChrTalk(
        0x10,
        (
            "#5P#13912F请聆听这饱含爱与真心，\x01",
            "可以慰藉你们那消极心灵的曲调……\x02",
        )
    )

    CloseMessageWindow()

    #C0250
    ChrTalk(
        0x102,
        "#12P#00103F唉……\x02",
    )

    CloseMessageWindow()
    OP_63(0x10, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0251
    ChrTalk(
        0x10,
        (
            "#5P#13905F呀……\x01",
            "怎么了？小姐。\x02\x03",

            "#13904F虽然你那略带忧愁的叹息\x01",
            "也充满魅力，\x01",
            "但这样会让幸福白白溜走哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0252
    ChrTalk(
        0x102,
        (
            "#12P#00103F……为你考虑，\x01",
            "我话说在先。\x02\x03",

            "#00100F穆拉先生向我们\x01",
            "提出的委托是\x01",
            "『无论怎样也要把你带回去』。\x02\x03",

            "#00109F从他的意思来看，\x01",
            "似乎并不介意让你稍吃一点苦头哦……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x10, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x10)
    Fade(500)
    Sound(812, 0, 100, 0)
    SetChrChipByIndex(0x10, 0x1E)
    SetChrSubChip(0x10, 0x0)
    OP_0D()

    #C0253
    ChrTalk(
        0x10,
        (
            "#5P#13911F我、我明白了！\x01",
            "我这就和你们回去！\x02",
        )
    )

    CloseMessageWindow()

    #C0254
    ChrTalk(
        0x101,
        (
            "#12P#00012F（艾莉面带笑容，\x01",
            "  感觉却好恐怖……）\x02",
        )
    )

    CloseMessageWindow()

    #C0255
    ChrTalk(
        0x10,
        (
            "#5P#13910F哎呀呀……\x01",
            "看来该谢幕了啊。\x02\x03",

            "#13900F那么，你们能带我\x01",
            "去找穆拉吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0256
    ChrTalk(
        0x109,
        (
            "#12P#10108F嗯……这个嘛……\x01",
            "也许还是让穆拉先生\x01",
            "来这里比较好。\x02\x03",

            "#10106F虽然有些麻烦他。\x02",
        )
    )

    CloseMessageWindow()

    #C0257
    ChrTalk(
        0x105,
        (
            "#12P#10302F嗯，还是这样比较保险，\x01",
            "免得让他在路上逃掉。\x02",
        )
    )

    CloseMessageWindow()

    #C0258
    ChrTalk(
        0x10,
        "#5P#13910F哎呀呀，你们真是不信任我啊。\x02",
    )

    CloseMessageWindow()

    #C0259
    ChrTalk(
        0x101,
        (
            "#12P#00003F总、总之……\x01",
            "先和车站那边联系一下吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xBB8)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x6F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x22, 5)
    NewScene("c0500", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_15_40BD end

    def Function_16_4A68(): pass

    label("Function_16_4A68")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4AB7")
    SetChrSubChip(0xFE, 0x0)
    Sleep(200)
    SetChrSubChip(0xFE, 0x1)
    Sleep(200)
    SetChrSubChip(0xFE, 0x2)
    Sleep(200)
    SetChrSubChip(0xFE, 0x3)
    Sleep(200)
    SetChrSubChip(0xFE, 0x4)
    Sleep(200)
    SetChrSubChip(0xFE, 0x3)
    Sleep(200)
    SetChrSubChip(0xFE, 0x2)
    Sleep(200)
    SetChrSubChip(0xFE, 0x1)
    Sleep(200)
    SetChrSubChip(0xFE, 0x0)
    Sleep(200)
    Jump("Function_16_4A68")

    label("loc_4AB7")

    Return()

    # Function_16_4A68 end

    def Function_17_4AB8(): pass

    label("Function_17_4AB8")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch00102.itc", 0x1F)
    LoadChrToIndex("chr/ch00202.itc", 0x20)
    LoadChrToIndex("chr/ch00302.itc", 0x21)
    LoadChrToIndex("chr/ch45100.itc", 0x22)
    LoadChrToIndex("chr/ch45102.itc", 0x23)
    OP_68(-7510, 900, -380, 0)
    MoveCamera(300, 15, 0, 0)
    OP_6E(420, 0)
    SetCameraDistance(20290, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x1)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x1)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x1)
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x104, 0x0)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x103, 0x4)
    SetChrFlags(0x104, 0x4)
    SetChrPos(0x101, -7000, 100, -2050, 0)
    SetChrPos(0x102, -5800, 100, -2050, 0)
    SetChrPos(0x103, -4600, 100, -2050, 0)
    SetChrPos(0x104, -3100, 100, -500, 270)
    ClearChrFlags(0x11, 0x80)
    SetChrChipByIndex(0x11, 0x23)
    SetChrSubChip(0x11, 0x2)
    SetChrPos(0x11, -8400, 100, -500, 90)
    ClearChrFlags(0x11, 0x8000)
    PlayBGM("ed7117", 0)
    FadeToBright(2000, 0)
    OP_0D()

    #C0260
    ChrTalk(
        0x101,
        (
            "#00005F#6P爵士酒吧『加兰特』……\x01",
            "为什么要来这里？\x02",
        )
    )

    CloseMessageWindow()

    #C0261
    ChrTalk(
        0x11,
        (
            "#5P其实，我和盖伊先生\x01",
            "曾在三年前约定过，\x01",
            "要在这里交换情报。\x02",
        )
    )

    CloseMessageWindow()

    #C0262
    ChrTalk(
        0x11,
        (
            "#5P……然而，在约定时间即将到来的时候，\x01",
            "我却收到了讣告。\x02",
        )
    )

    CloseMessageWindow()

    #C0263
    ChrTalk(
        0x101,
        "#6P#00006F是这样啊……\x02",
    )

    CloseMessageWindow()

    #C0264
    ChrTalk(
        0x11,
        (
            "#5P#5P……教团事件发生以后，\x01",
            "帝国派和共和国派的议员被捕，\x01",
            "新市长上任……\x02",
        )
    )

    CloseMessageWindow()

    #C0265
    ChrTalk(
        0x11,
        (
            "#5P随后，通商会议召开，\x01",
            "克洛斯贝尔市遭遇袭击……\x02",
        )
    )

    CloseMessageWindow()

    #C0266
    ChrTalk(
        0x11,
        (
            "#5P……而现在，\x01",
            "又发表了独立宣言。\x02",
        )
    )

    CloseMessageWindow()

    #C0267
    ChrTalk(
        0x11,
        (
            "#5P这些事件，看似七零八落，\x01",
            "却又相互干涉影响。\x02",
        )
    )

    CloseMessageWindow()

    #C0268
    ChrTalk(
        0x11,
        (
            "#5P也就是说，所有事件恐怕都是在\x01",
            "一股巨大潮流的推动下顺势发生的。\x02",
        )
    )

    CloseMessageWindow()

    #C0269
    ChrTalk(
        0x102,
        "#6P#00101F巨大潮流……\x02",
    )

    CloseMessageWindow()

    #C0270
    ChrTalk(
        0x11,
        (
            "#5P如果能把握住这股潮流，\x01",
            "也就是所谓的『大局』，\x01",
            "便可以看清每一个单独的事件了。\x02",
        )
    )

    CloseMessageWindow()

    #C0271
    ChrTalk(
        0x11,
        (
            "#5P这样的话，说不定也能\x01",
            "让盖伊先生遇害事件的真相\x01",
            "水落石出。\x02",
        )
    )

    CloseMessageWindow()

    #C0272
    ChrTalk(
        0x11,
        (
            "#5P我正是抱着如此想法，\x01",
            "才请求各位协助我一起探讨。\x02",
        )
    )

    CloseMessageWindow()

    #C0273
    ChrTalk(
        0x11,
        (
            "#5P我想，这也许会让\x01",
            "罗伊德警官感到难过……\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0x1388)

    #C0274
    ChrTalk(
        0x101,
        (
            "#6P#00003F………………………\x02\x03",

            "#00000F不……没关系。\x02",
        )
    )

    CloseMessageWindow()

    #C0275
    ChrTalk(
        0x102,
        "#6P#00108F罗伊德……\x02",
    )

    CloseMessageWindow()

    #C0276
    ChrTalk(
        0x103,
        "#6P#00208F罗伊德前辈……\x02",
    )

    CloseMessageWindow()

    #C0277
    ChrTalk(
        0x104,
        (
            "#12P#00303F……嗯，时间也不多了。\x02\x03",

            "#00300F我们赶快开始吧。\x02",
        )
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7302", 0)

    #C0278
    ChrTalk(
        0x11,
        (
            "#5P说的也是……\x01",
            "那么，这就开始吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0279
    ChrTalk(
        0x11,
        (
            "#5P首先是盖伊先生的遗体\x01",
            "被发现时的情况——\x02",
        )
    )

    CloseMessageWindow()

    #C0280
    ChrTalk(
        0x11,
        (
            "#5P时值三年前的一天，当时阴有小雨，\x01",
            "发现遗体的地点是兰花塔的建设工地。\x02",
        )
    )

    CloseMessageWindow()

    #C0281
    ChrTalk(
        0x11,
        (
            "#5P推测死亡时刻是当天凌晨，\x01",
            "发现遗体时，距离死亡时间\x01",
            "已有大约半天。\x02",
        )
    )

    CloseMessageWindow()

    #C0282
    ChrTalk(
        0x11,
        "#5P而死因则是——\x02",
    )

    CloseMessageWindow()

    #C0283
    ChrTalk(
        0x11,
        (
            "#5P被导力枪从背后\x01",
            "射穿心脏，\x01",
            "出血性休克致死。\x02",
        )
    )

    CloseMessageWindow()

    #C0284
    ChrTalk(
        0x11,
        "#5P……这些都没错吧？\x02",
    )

    CloseMessageWindow()

    #C0285
    ChrTalk(
        0x101,
        "#6P#00003F嗯……完全正确。\x02",
    )

    CloseMessageWindow()

    #C0286
    ChrTalk(
        0x102,
        "#6P#00101F从背后……\x02",
    )

    CloseMessageWindow()

    #C0287
    ChrTalk(
        0x104,
        "#12P#00306F是这样啊……\x02",
    )

    CloseMessageWindow()

    #C0288
    ChrTalk(
        0x103,
        "#6P#00208F…………………………\x02",
    )

    CloseMessageWindow()

    #C0289
    ChrTalk(
        0x11,
        (
            "#5P嗯……那么，接下来就开始整理\x01",
            "发现遗体时的现场情况吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0290
    ChrTalk(
        0x11,
        (
            "#5P首先，现场周边有\x01",
            "激烈打斗的痕迹……\x02",
        )
    )

    CloseMessageWindow()

    #C0291
    ChrTalk(
        0x11,
        (
            "#5P但除了盖伊先生的遗体之外，\x01",
            "并没有留下其它任何证物。\x02",
        )
    )

    CloseMessageWindow()

    #C0292
    ChrTalk(
        0x11,
        (
            "#5P他平时\x01",
            "常用的旋棍被人\x01",
            "从现场拿走……\x02",
        )
    )

    CloseMessageWindow()

    #C0293
    ChrTalk(
        0x11,
        (
            "#5P连佩戴在胸前的\x01",
            "警察徽章也被夺走了。\x02",
        )
    )

    CloseMessageWindow()

    #C0294
    ChrTalk(
        0x11,
        "#5P关于那枚警察徽章……\x02",
    )

    CloseMessageWindow()

    #C0295
    ChrTalk(
        0x11,
        (
            "#5P听说你们已经查明了事实，\x01",
            "确定是由黑手党『鲁巴彻』的成员\x01",
            "从现场带走的？\x02",
        )
    )

    CloseMessageWindow()

    #C0296
    ChrTalk(
        0x101,
        (
            "#6P#00003F是的，这是马尔克尼会长\x01",
            "亲口告诉我们的。\x02\x03",

            "#00001F经过审问之后，那名成员本人\x01",
            "也提供了正式供述。\x02",
        )
    )

    CloseMessageWindow()

    #C0297
    ChrTalk(
        0x11,
        "#5P嗯，原来如此……\x02",
    )

    CloseMessageWindow()

    #C0298
    ChrTalk(
        0x11,
        (
            "#5P那么，接下来就确认一下，\x01",
            "当时是否有目击者吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0299
    ChrTalk(
        0x11,
        "#5P……从结论来说，是没有目击者的。\x02",
    )

    CloseMessageWindow()

    #C0300
    ChrTalk(
        0x11,
        (
            "#5P当时，兰花塔的建设工程\x01",
            "处于暂时中断的状态，\x01",
            "并没有相关人员在场。\x02",
        )
    )

    CloseMessageWindow()

    #C0301
    ChrTalk(
        0x11,
        (
            "#5P而且事件发生在凌晨时分，\x01",
            "风雨交加，还伴有雷鸣……\x02",
        )
    )

    CloseMessageWindow()

    #C0302
    ChrTalk(
        0x11,
        (
            "#5P因此没有任何人接近过现场，\x01",
            "完全找不到见证了\x01",
            "杀害瞬间的证人。\x02",
        )
    )

    CloseMessageWindow()

    #C0303
    ChrTalk(
        0x11,
        (
            "#5P另外，盖伊先生\x01",
            "没有向身边的任何人\x01",
            "提到过自己准备前往现场。\x02",
        )
    )

    CloseMessageWindow()

    #C0304
    ChrTalk(
        0x11,
        (
            "#5P……关于此事件，\x01",
            "我所掌握到的情况就是这些。\x02",
        )
    )

    CloseMessageWindow()

    #C0305
    ChrTalk(
        0x11,
        "#5P罗伊德警官，你还有什么可以补充的吗？\x02",
    )

    CloseMessageWindow()

    #C0306
    ChrTalk(
        0x101,
        (
            "#6P#00006F不，没有了……\x02\x03",

            "#00001F我所了解的也就是这些。\x02",
        )
    )

    CloseMessageWindow()

    #C0307
    ChrTalk(
        0x102,
        (
            "#6P#00108F（尼尔森先生……\x01",
            "  收集情报的能力还是如此惊人。）\x02",
        )
    )

    CloseMessageWindow()

    #C0308
    ChrTalk(
        0x103,
        (
            "#6P#00203F（嗯，他似乎和\x01",
            "  盖伊先生\x01",
            "  私交甚密……）\x02\x03",

            "#00201F（或许正因如此，\x01",
            "  才会如此重视这个事件吧。）\x02",
        )
    )

    CloseMessageWindow()

    #C0309
    ChrTalk(
        0x11,
        (
            "#5P嗯……\x01",
            "那么，我们要开始探讨事件了。\x02",
        )
    )

    CloseMessageWindow()

    #C0310
    ChrTalk(
        0x11,
        (
            "#5P首先要探讨事件的真相——\x01",
            "再说得直接一点，也就是推定犯人。\x02",
        )
    )

    CloseMessageWindow()

    #C0311
    ChrTalk(
        0x11,
        (
            "#5P说起嫌疑最大的候选者，\x01",
            "自然是『鲁巴彻』……\x01",
            "以及『Ｄ∴Ｇ教团』的成员。\x02",
        )
    )

    CloseMessageWindow()

    #C0312
    ChrTalk(
        0x11,
        "#5P罗伊德警官，犯人会是他们吗？\x02",
    )

    CloseMessageWindow()
    ClearScenarioFlags(0x0, 2)
    ClearScenarioFlags(0x0, 3)
    ClearScenarioFlags(0x0, 4)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_56FC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5857")
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    #A0313
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1K盖伊是被黑手党或\x01",
            "Ｄ∴Ｇ教团的成员杀害的吗？\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "犯人是黑手党的成员\x01",      # 0
            "犯人是教团的成员\x01",        # 1
            "两者都不可能\x01",            # 2
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
        (0, "loc_57C7"),
        (1, "loc_57F5"),
        (2, "loc_5823"),
        (SWITCH_DEFAULT, "loc_5844"),
    )


    label("loc_57C7")


    #C0314
    ChrTalk(
        0x101,
        "#6P#00006F（……不，并非如此。）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_5844")

    label("loc_57F5")


    #C0315
    ChrTalk(
        0x101,
        "#6P#00006F（……不，并非如此。）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_5844")

    label("loc_5823")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_583C")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_583C")

    SetScenarioFlags(0x0, 2)
    Jump("loc_5844")

    label("loc_5844")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_5852")
    Jump("loc_5857")

    label("loc_5852")

    Jump("loc_56FC")

    label("loc_5857")


    #C0316
    ChrTalk(
        0x101,
        (
            "#6P#00003F不，两者都不可能。\x02\x03",

            "#00008F鲁巴彻会长马尔克尼及其手下，\x01",
            "还有教团的约亚西姆……\x02\x03",

            "#00001F他们分别交代过\x01",
            "企图杀害大哥，\x01",
            "但未能得逞的供述。\x02\x03",

            "#00006F如果猜测为，在他们毫不知情的情况下，\x01",
            "其他部下或相关人士擅自行动，\x01",
            "未免太过牵强。\x02\x03",

            "#00013F……而且，听说大哥\x01",
            "从未对这些势力\x01",
            "放松过警惕。\x02\x03",

            "大哥遭受了引诱，\x01",
            "将自己置身于致命险境……\x02\x03",

            "这种可能性应该很低。\x02",
        )
    )

    CloseMessageWindow()

    #C0317
    ChrTalk(
        0x104,
        (
            "#12P#00306F……有道理。\x02\x03",

            "#00301F听说他虽然大胆无畏，\x01",
            "但同时拥有着异常灵敏的直觉。\x02",
        )
    )

    CloseMessageWindow()

    #C0318
    ChrTalk(
        0x103,
        (
            "#6P#00206F……是的。\x02\x03",

            "#00201F我不认为他会\x01",
            "输给黑手党或教团。\x02",
        )
    )

    CloseMessageWindow()

    #C0319
    ChrTalk(
        0x11,
        (
            "#5P的确如此，各种因素\x01",
            "都否定了这些可能性。\x02",
        )
    )

    CloseMessageWindow()

    #C0320
    ChrTalk(
        0x11,
        (
            "#5P在教团事件发生之前，或许还难说，\x01",
            "但现在要说他们是犯人，\x01",
            "实在是太过牵强了。\x02",
        )
    )

    CloseMessageWindow()

    #C0321
    ChrTalk(
        0x11,
        (
            "#5P那么，接下来是两大国的相关人士——\x01",
            "来探讨一下这种可能性吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0322
    ChrTalk(
        0x11,
        (
            "#5P贪图权力的帝国派、共和国派议员，\x01",
            "还有和他们来往密切的两国政府高官，\x01",
            "以及谍报方面的人士——\x02",
        )
    )

    CloseMessageWindow()

    #C0323
    ChrTalk(
        0x11,
        (
            "#5P盖伊先生有没有\x01",
            "可能是遭到了\x01",
            "那些人的毒手呢？\x02",
        )
    )

    CloseMessageWindow()
    ClearScenarioFlags(0x0, 2)
    ClearScenarioFlags(0x0, 3)
    ClearScenarioFlags(0x0, 4)

    label("loc_5BC0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5D78")
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    #A0324
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1K盖伊是被帝国或共和国的相关人士所杀害的吗？\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "可能性很高\x01",      # 0
            "可能性很低\x01",      # 1
            "很难说\x01",          # 2
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
        (0, "loc_5C76"),
        (1, "loc_5CDF"),
        (2, "loc_5D00"),
        (SWITCH_DEFAULT, "loc_5D65"),
    )


    label("loc_5C76")


    #C0325
    ChrTalk(
        0x101,
        (
            "#6P#00008F（可能性很高……\x01",
            "  真的是这样吗？）\x02\x03",

            "#00001F（再仔细想想吧，\x01",
            "  罗伊德·班宁斯。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_5D65")

    label("loc_5CDF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5CF8")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_5CF8")

    SetScenarioFlags(0x0, 2)
    Jump("loc_5D65")

    label("loc_5D00")


    #C0326
    ChrTalk(
        0x101,
        (
            "#6P#00008F（很难说……\x01",
            "  真的是这样吗？）\x02\x03",

            "#00001F（再仔细想想吧，\x01",
            "  罗伊德·班宁斯。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_5D65")

    label("loc_5D65")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_5D73")
    Jump("loc_5D78")

    label("loc_5D73")

    Jump("loc_5BC0")

    label("loc_5D78")


    #C0327
    ChrTalk(
        0x101,
        (
            "#6P#00003F不，我认为\x01",
            "可能性很低。\x02\x03",

            "#00008F在克洛斯贝尔，的确存在很多\x01",
            "从事着不正当行径的两大国人士。\x02\x03",

            "听说大哥当年经常\x01",
            "追查其中的黑幕。\x02\x03",

            "#00001F而和他们来往密切的\x01",
            "谍报人士，也确实会频繁\x01",
            "出入克洛斯贝尔。\x02\x03",

            "#00006F但说实话，对他们来说，\x01",
            "大哥的个人行动所能造成的影响\x01",
            "根本就无关痛痒。\x02",
        )
    )

    CloseMessageWindow()

    #C0328
    ChrTalk(
        0x102,
        (
            "#6P#00106F的确如此……\x02\x03",

            "#00108F只要两大国有意，\x01",
            "甚至可以通过自治州政府，\x01",
            "直接向警察局施压……\x02\x03",

            "#00101F尤其是在以前的体制下，\x01",
            "再蛮横的压力\x01",
            "也可以随意施加。\x02",
        )
    )

    CloseMessageWindow()

    #C0329
    ChrTalk(
        0x101,
        (
            "#6P#00003F嗯，所以说，无论大哥有多么难缠，\x01",
            "终究也只是一名普通的搜查官而已，\x01",
            "完全没必要特意将他叫出来并加以杀害。\x02\x03",

            "#00001F那种行为根本无法\x01",
            "给他们带来与成本\x01",
            "等价的利益。\x02",
        )
    )

    CloseMessageWindow()

    #C0330
    ChrTalk(
        0x11,
        "#5P嗯……\x02",
    )

    CloseMessageWindow()

    #C0331
    ChrTalk(
        0x104,
        (
            "#12P#00303F而且，就算那些人真的\x01",
            "心怀不轨，罗伊德的大哥肯定也\x01",
            "不会完全不加防范。\x02\x03",

            "#00300F大概会像防备黑手党一样，\x01",
            "保持警觉，不容对方随意靠近吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0332
    ChrTalk(
        0x103,
        "#6P#00206F我也有同感。\x02",
    )

    CloseMessageWindow()

    #C0333
    ChrTalk(
        0x11,
        (
            "#5P不愧是各位……\x01",
            "我也没什么\x01",
            "好补充的了。\x02",
        )
    )

    CloseMessageWindow()

    #C0334
    ChrTalk(
        0x11,
        "#5P那么，进入最后的分析吧。\x02",
    )

    CloseMessageWindow()

    #C0335
    ChrTalk(
        0x11,
        (
            "#5P在此之前，我们已经用\x01",
            "反证法排除了一些\x01",
            "有嫌疑的人选……\x02",
        )
    )

    CloseMessageWindow()

    #C0336
    ChrTalk(
        0x11,
        (
            "#5P既然如此，那就直截了当地说吧，\x01",
            "除此之外，还有什么人有嫌疑？\x02",
        )
    )

    CloseMessageWindow()
    ClearScenarioFlags(0x0, 2)
    ClearScenarioFlags(0x0, 3)
    ClearScenarioFlags(0x0, 4)

    label("loc_617D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_63B0")
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    #A0337
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1K有嫌疑的人选是？\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "结社『噬身之蛇』的成员\x01",                # 0
            "克洛斯贝尔警察局的成员\x01",                # 1
            "盖伊有所防范，但又非常熟悉的人物\x01",      # 2
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
        (0, "loc_624B"),
        (1, "loc_62C2"),
        (2, "loc_637C"),
        (SWITCH_DEFAULT, "loc_639D"),
    )


    label("loc_624B")


    #C0338
    ChrTalk(
        0x101,
        (
            "#6P#00006F（结社的确是个谜团重重的组织，\x01",
            "  但还是再好好想想吧。）\x02\x03",

            "#00013F（应该还有更加\x01",
            "  合理的答案。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_639D")

    label("loc_62C2")


    #C0339
    ChrTalk(
        0x101,
        (
            "#6P#00008F（对大哥心怀怨恨的人所进行的内部犯案……\x01",
            "  虽然也不是完全没可能，\x01",
            "  但应该还有更加合理的答案。）\x02\x03",

            "#00013F（以此前的考证成果为基础，\x01",
            "  自然推导出答案，那就是——）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_639D")

    label("loc_637C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6395")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6395")

    SetScenarioFlags(0x0, 2)
    Jump("loc_639D")

    label("loc_639D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_63AB")
    Jump("loc_63B0")

    label("loc_63AB")

    Jump("loc_617D")

    label("loc_63B0")

    OP_63(0x101, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    Sleep(500)

    #C0340
    ChrTalk(
        0x101,
        (
            "#6P#00003F大哥有所防范，\x01",
            "但又非常熟悉的人物。\x02\x03",

            "#00001F我认为犯人\x01",
            "符合以上条件。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0341
    ChrTalk(
        0x103,
        "#6P#00205F哎……\x02",
    )

    CloseMessageWindow()

    #C0342
    ChrTalk(
        0x104,
        "#12P#00301F这……\x02",
    )

    CloseMessageWindow()

    #C0343
    ChrTalk(
        0x11,
        "#5P嗯，理由呢？\x02",
    )

    CloseMessageWindow()

    #C0344
    ChrTalk(
        0x101,
        (
            "#6P#00003F……首先，大哥并没有\x01",
            "将自己准备前往现场的事情\x01",
            "告诉任何人。\x02\x03",

            "#00008F而且，从当时的情况看来，\x01",
            "他应该是独自一人\x01",
            "前往现场的。\x02\x03",

            "#00013F由此来看，\x01",
            "犯人为『熟人』的\x01",
            "可能性恐怕相当高。\x02",
        )
    )

    CloseMessageWindow()

    #C0345
    ChrTalk(
        0x102,
        "#6P#00106F的、的确……\x02",
    )

    CloseMessageWindow()

    #C0346
    ChrTalk(
        0x101,
        (
            "#6P#00006F究竟是大哥约了对方，\x01",
            "还是应对方之约而前往……\x01",
            "目前还不得而知。\x02\x03",

            "#00003F会面地点是荒无人烟的建设工地。\x02\x03",

            "#00008F也就是说，他们要谈一些\x01",
            "不想让别人听到，也绝不能让别人\x01",
            "听到的重要事情。\x02\x03",

            "#00013F其间，经过一定程度的交涉……\x01",
            "最终导致交涉决裂，\x01",
            "大哥也因此而丧生。\x02",
        )
    )

    CloseMessageWindow()

    #C0347
    ChrTalk(
        0x11,
        "#5P所谓的交涉是……？\x02",
    )

    CloseMessageWindow()

    #C0348
    ChrTalk(
        0x101,
        (
            "#6P#00003F具体情况就不清楚了。\x02\x03",

            "#00008F不过，考虑到对方\x01",
            "不惜夺去大哥的性命，\x01",
            "交涉内容必定相当重要……\x02\x03",

            "#00001F比如……\x01",
            "与『某些阴谋』有关。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0349
    ChrTalk(
        0x103,
        "#6P#00200F阴谋吗……\x02",
    )

    CloseMessageWindow()

    #C0350
    ChrTalk(
        0x11,
        "#5P唔……\x02",
    )

    CloseMessageWindow()

    #C0351
    ChrTalk(
        0x101,
        (
            "#6P#00003F……尼尔森先生，\x01",
            "您刚才说过，『只要把握住大局，就有可能\x01",
            "使大哥遇害一案的真相水落石出』。\x02\x03",

            "#00000F在听到这句话的时候，我就有种\x01",
            "朦胧的感觉，隐隐想到了某些线索。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x11, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0352
    ChrTalk(
        0x11,
        "#5P哦……？\x02",
    )

    CloseMessageWindow()

    #C0353
    ChrTalk(
        0x101,
        (
            "#6P#00006F大哥当年也许逼近了\x01",
            "某个阴谋……\x02\x03",

            "#00003F那个阴谋的策划者，虽然与Ｄ∴Ｇ教团、\x01",
            "黑手党、帝国和共和国存在一定关联，\x01",
            "但却属于单独一方势力。\x02\x03",

            "#00008F在他的暗中推动下，那个阴谋\x01",
            "也许至今仍在继续进展。\x02\x03",

            "#00001F这种推测\x01",
            "是否可以成立呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0354
    ChrTalk(
        0x102,
        "#6P#00105F单独一方势力……\x02",
    )

    CloseMessageWindow()

    #C0355
    ChrTalk(
        0x103,
        "#6P#00201F而且阴谋仍在继续进展……\x02",
    )

    CloseMessageWindow()

    #C0356
    ChrTalk(
        0x101,
        (
            "#6P#00001F嗯，至今都没有\x01",
            "查明杀害大哥的犯人，\x01",
            "也正能说明这一点。\x02\x03",

            "#00003F我认为，这正是\x01",
            "事件仍未完结的\x01",
            "最好证明。\x02",
        )
    )

    CloseMessageWindow()

    #C0357
    ChrTalk(
        0x11,
        "#5P…………………………\x02",
    )

    CloseMessageWindow()
    OP_63(0x11, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0358
    ChrTalk(
        0x101,
        (
            "#6P#00005F尼尔森先生？\x02\x03",

            "#00006F……我的看法还是太牵强了吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_64(0x11)
    Sleep(500)

    #C0359
    ChrTalk(
        0x11,
        (
            "#5P不……\x01",
            "我觉得这是相当精彩的推理。\x02",
        )
    )

    CloseMessageWindow()

    #C0360
    ChrTalk(
        0x11,
        "#5P我就直说吧，罗伊德警官。\x02",
    )

    CloseMessageWindow()

    #C0361
    ChrTalk(
        0x11,
        (
            "#5P经过之前的多番探讨，\x01",
            "你能确定犯人是谁了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0362
    ChrTalk(
        0x11,
        (
            "#5P三年前叫出盖伊先生，\x01",
            "并将其杀害的人物是……？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    Sleep(500)

    #C0363
    ChrTalk(
        0x101,
        (
            "#6P#00006F不，很遗憾……\x02\x03",

            "#00003F虽然已经推断凶手为『熟人』，\x01",
            "但大哥的人脉之广简直令人咋舌。\x02\x03",

            "#00008F……被人从现场拿走，\x01",
            "至今下落不明的旋棍，\x01",
            "还有被人从背后击中要害这个事实……\x02\x03",

            "#00013F我个人感觉，\x01",
            "这些因素也许是\x01",
            "解明事件的关键……\x02\x03",

            "#00006F但如果光凭这些就能确定犯人，\x01",
            "搜查一科早在三年之前\x01",
            "就可以查明真相了。\x02",
        )
    )

    CloseMessageWindow()

    #C0364
    ChrTalk(
        0x11,
        "#5P嗯……有道理。\x02",
    )

    CloseMessageWindow()

    #C0365
    ChrTalk(
        0x11,
        (
            "#5P截止至今，可以确定犯人的\x01",
            "拼图碎片还没有全部集齐。\x02",
        )
    )

    CloseMessageWindow()

    #C0366
    ChrTalk(
        0x11,
        (
            "#5P不过，我有一点\x01",
            "可以肯定。\x02",
        )
    )

    CloseMessageWindow()

    #C0367
    ChrTalk(
        0x11,
        (
            "#5P能够寻找到最后一块缺失碎片的人\x01",
            "也只有你了，罗伊德警官。\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0xBB8)
    OP_63(0x102, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0368
    ChrTalk(
        0x102,
        "#6P#00105F尼尔森先生……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    Sleep(500)

    #C0369
    ChrTalk(
        0x101,
        "#6P#00004F嗯……我正有此意。\x02",
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7151", 0)

    #C0370
    ChrTalk(
        0x11,
        "#5P呵呵，听你这么说，我就安心了。\x02",
    )

    CloseMessageWindow()

    #C0371
    ChrTalk(
        0x11,
        (
            "#5P……三年前与盖伊先生相约，\x01",
            "要在此交换情报。如今的感觉，\x01",
            "就像是已经履行了那时的约定。\x02",
        )
    )

    CloseMessageWindow()

    #C0372
    ChrTalk(
        0x11,
        (
            "#5P非常感谢大家\x01",
            "陪我一起分析探讨。\x02",
        )
    )

    CloseMessageWindow()

    #C0373
    ChrTalk(
        0x101,
        (
            "#6P#00000F哪里，该道谢的是我……\x01",
            "真的非常感谢您。\x02",
        )
    )

    CloseMessageWindow()

    #C0374
    ChrTalk(
        0x11,
        (
            "#5P那么，我就此失陪了，\x01",
            "期待各位今后的活跃表现。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    Sound(812, 0, 100, 0)
    SetChrChipByIndex(0x11, 0x22)
    ClearChrFlags(0x11, 0x4)
    SetChrFlags(0x11, 0x8000)
    SetChrPos(0x11, -8170, 0, -500, 90)
    OP_0D()
    Sleep(500)

    def lambda_6F6D():
        OP_95(0xFE, -7730, 0, 1910, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_6F6D)
    SetChrSubChip(0x101, 0x0)
    Sleep(50)
    SetChrSubChip(0x102, 0x0)
    Sleep(50)
    SetChrSubChip(0x103, 0x0)
    WaitChrThread(0x11, 1)

    def lambda_6F9D():
        OP_95(0xFE, 690, 0, 1520, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_6F9D)
    SetChrSubChip(0x101, 0x2)
    Sleep(50)
    SetChrSubChip(0x102, 0x2)
    Sleep(50)
    SetChrSubChip(0x103, 0x2)
    Sleep(50)
    SetChrSubChip(0x104, 0x2)
    WaitChrThread(0x11, 1)
    SetChrSubChip(0x101, 0x2)
    Sleep(50)
    SetChrSubChip(0x102, 0x2)
    Sleep(50)
    SetChrSubChip(0x103, 0x2)
    Sleep(50)
    SetChrSubChip(0x104, 0x2)

    #C0375
    ChrTalk(
        0x103,
        (
            "#6P#00202F尼尔森先生……\x01",
            "他仿佛一直在\x01",
            "引导着我们。\x02",
        )
    )

    CloseMessageWindow()

    #C0376
    ChrTalk(
        0x101,
        (
            "#5P#00004F嗯……看来他一直\x01",
            "都在记挂着与大哥的约定。\x02\x03",

            "#00002F能和他讨论，真是太好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0377
    ChrTalk(
        0x102,
        "#6P#00109F呵呵……是呀。\x02",
    )

    CloseMessageWindow()

    #C0378
    ChrTalk(
        0x104,
        "#6P#00304F嗯。\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x104, 0x1)
    Sleep(300)

    #C0379
    ChrTalk(
        0x104,
        (
            "#6P#00301F#12P……好，已经受到了激励，\x01",
            "差不多也该走了吧！\x02",
        )
    )

    CloseMessageWindow()

    #C0380
    ChrTalk(
        0x101,
        (
            "#5P#00003F嗯……我们赶快去\x01",
            "鲁巴彻旧址的会长室吧。\x02\x03",

            "#00013F应该可以从雷克特大尉的口中\x01",
            "套出一些情报！\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0381
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "任务【盖伊·班宁斯遇害事件的分析】\x07\x00",
            "完成！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_71D1")
    OP_2C(0x95, 0x2)
    Jump("loc_71E5")

    label("loc_71D1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_71E5")
    OP_2C(0x95, 0x1)

    label("loc_71E5")

    ClearChrFlags(0x11, 0x8000)
    SetChrChipByIndex(0x11, 0x0)
    SetChrFlags(0x11, 0x80)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x102, 0x4)
    ClearChrFlags(0x103, 0x4)
    ClearChrFlags(0x104, 0x4)
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_D7(0x20)
    OP_D7(0x21)
    OP_D7(0x22)
    OP_D7(0x23)
    SetChrPos(0x0, -4660, 0, 1270, 90)
    OP_69(0xFF, 0x0)
    OP_29(0x95, 0x1, 0x0)
    OP_29(0x95, 0x4, 0x10)
    EventEnd(0x5)
    Return()

    # Function_17_4AB8 end

    SaveToFile()

Try(main)
