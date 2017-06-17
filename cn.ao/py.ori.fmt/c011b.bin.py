from ScenarioHelper import *

def main():
    CreateScenaFile(
        "c011b.bin",                # FileName
        "c011b",                    # MapName
        "c011b",                    # Location
        0x0009,                     # MapIndex
        "ed7513",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 9, 0, 2, 0, 3],
    )

    BuildStringList((
        "c011b",                  # 0
        "赛尔盖科长",             # 1
        "蔡特",                   # 2
        "琪雅",                   # 3
        "谢莉",                   # 4
        "达德利搜查官",           # 5
        "市民",                   # 6
        "市民",                   # 7
        "市民",                   # 8
        "市民",                   # 9
        "市民",                   # 10
        "警官",                   # 11
        "餐具",                   # 12
        "餐具",                   # 13
        "餐具",                   # 14
        "餐具",                   # 15
        "餐具",                   # 16
        "餐具",                   # 17
        "餐具",                   # 18
        "餐具",                   # 19
        "餐具",                   # 20
        "餐具",                   # 21
        "餐具",                   # 22
        "餐具",                   # 23
        "餐具",                   # 24
        "餐具",                   # 25
        "餐具",                   # 26
        "餐具",                   # 27
        "餐具",                   # 28
        "餐具",                   # 29
        "餐具",                   # 30
        "椅子",                   # 31
        "椅子",                   # 32
        "椅子",                   # 33
        "椅子",                   # 34
        "椅子",                   # 35
        "椅子",                   # 36
        "椅子",                   # 37
        "椅子",                   # 38
    ))

    AddCharChip((
        "chr/ch02500.itc",                   # 00
        "chr/ch02502.itc",                   # 01
        "chr/ch08200.itc",                   # 02
        "chr/ch08202.itc",                   # 03
        "chr/ch02707.itc",                   # 04
        "chr/ch02708.itc",                   # 05
        "chr/ch02702.itc",                   # 06
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

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 0,   4,   255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   4,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   2,   0,   255, 255, 0,   5,   255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    246,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    246,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    246,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    246,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    246,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    246,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    246,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    246,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclActor(170000,  0,       63560,   1500,    170000,  1500,    63560,   0x007C, 0,  7,  0x0000)
    DeclActor(16960,   850,     10840,   2000,    16960,   1300,    10840,   0x007C, 0,  25, 0x0000)

    ChipFrameInfo(1512, 0)                                       # 0

    ScpFunction((
        "Function_0_5E8",          # 00, 0
        "Function_1_698",          # 01, 1
        "Function_2_6B4",          # 02, 2
        "Function_3_7DE",          # 03, 3
        "Function_4_83F",          # 04, 4
        "Function_5_96C",          # 05, 5
        "Function_6_AEA",          # 06, 6
        "Function_7_D4B",          # 07, 7
        "Function_8_D82",          # 08, 8
        "Function_9_2A17",         # 09, 9
        "Function_10_2AA6",        # 0A, 10
        "Function_11_42C0",        # 0B, 11
        "Function_12_42EE",        # 0C, 12
        "Function_13_433F",        # 0D, 13
        "Function_14_4390",        # 0E, 14
        "Function_15_43E8",        # 0F, 15
        "Function_16_4432",        # 10, 16
        "Function_17_4458",        # 11, 17
        "Function_18_4CBA",        # 12, 18
        "Function_19_4CF7",        # 13, 19
        "Function_20_5DD7",        # 14, 20
        "Function_21_7D9A",        # 15, 21
        "Function_22_7E0A",        # 16, 22
        "Function_23_8F68",        # 17, 23
        "Function_24_9E89",        # 18, 24
        "Function_25_A8EE",        # 19, 25
        "Function_26_AF39",        # 1A, 26
    ))


    def Function_0_5E8(): pass

    label("Function_0_5E8")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_620"),
        (1, "loc_62C"),
        (2, "loc_638"),
        (3, "loc_644"),
        (4, "loc_650"),
        (5, "loc_65C"),
        (6, "loc_668"),
        (SWITCH_DEFAULT, "loc_674"),
    )


    label("loc_620")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_680")

    label("loc_62C")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_680")

    label("loc_638")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_680")

    label("loc_644")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_680")

    label("loc_650")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_680")

    label("loc_65C")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_680")

    label("loc_668")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_680")

    label("loc_674")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_680")

    label("loc_680")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_697")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_680")

    label("loc_697")

    Return()

    # Function_0_5E8 end

    def Function_1_698(): pass

    label("Function_1_698")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6B3")
    OP_A1(0xFE, 0x5DC, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Jump("Function_1_698")

    label("loc_6B3")

    Return()

    # Function_1_698 end

    def Function_2_6B4(): pass

    label("Function_2_6B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_72E")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 14400, 850, 12500, 0)
    BeginChrThread(0x8, 0, 0, 0)
    ClearChrFlags(0x8, 0x40)
    ClearChrFlags(0xA, 0x80)
    SetChrChipByIndex(0xA, 0x3)
    SetChrSubChip(0xA, 0x0)
    EndChrThread(0xA, 0x0)
    SetChrBattleFlags(0xA, 0x4)
    SetChrPos(0xA, 5570, 150, 6230, 180)
    ClearChrFlags(0x9, 0x80)
    SetChrChipByIndex(0x9, 0x5)
    SetChrPos(0x9, 2880, 0, 1750, 225)
    SetChrFlags(0x9, 0x10)
    ClearChrFlags(0x9, 0x40)

    label("loc_72E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_742")
    ClearScenarioFlags(0x22, 0)
    Event(0, 8)
    Jump("loc_7DD")

    label("loc_742")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_756")
    ClearScenarioFlags(0x22, 1)
    Event(0, 10)
    Jump("loc_7DD")

    label("loc_756")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 2)), scpexpr(EXPR_END)), "loc_76A")
    ClearScenarioFlags(0x22, 2)
    Event(0, 17)
    Jump("loc_7DD")

    label("loc_76A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 3)), scpexpr(EXPR_END)), "loc_77E")
    ClearScenarioFlags(0x22, 3)
    Event(0, 19)
    Jump("loc_7DD")

    label("loc_77E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 4)), scpexpr(EXPR_END)), "loc_792")
    ClearScenarioFlags(0x22, 4)
    Event(0, 20)
    Jump("loc_7DD")

    label("loc_792")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 5)), scpexpr(EXPR_END)), "loc_7A9")
    ClearScenarioFlags(0x22, 5)
    SetScenarioFlags(0x0, 4)
    Event(0, 22)
    Jump("loc_7DD")

    label("loc_7A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 6)), scpexpr(EXPR_END)), "loc_7BD")
    ClearScenarioFlags(0x22, 6)
    Event(0, 23)
    Jump("loc_7DD")

    label("loc_7BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 7)), scpexpr(EXPR_END)), "loc_7CE")
    ClearScenarioFlags(0x22, 7)
    Jump("loc_7DD")

    label("loc_7CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x23, 0)), scpexpr(EXPR_END)), "loc_7DD")
    ClearScenarioFlags(0x23, 0)
    Event(0, 24)

    label("loc_7DD")

    Return()

    # Function_2_6B4 end

    def Function_3_7DE(): pass

    label("Function_3_7DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_7F3")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x203), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 4)

    label("loc_7F3")

    SetMapObjFlags(0x19, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_816")
    SetMapObjFrame(0xFF, "asihuki", 0x0, 0x1)
    Jump("loc_825")

    label("loc_816")

    SetMapObjFrame(0xFF, "asihuki", 0x1, 0x1)

    label("loc_825")

    ClearMapObjFlags(0x6, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_83E")
    SetMapObjFlags(0x6, 0x10)
    OP_65(0x0, 0x1)

    label("loc_83E")

    Return()

    # Function_3_7DE end

    def Function_4_83F(): pass

    label("Function_4_83F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_906")

    #C0001
    ChrTalk(
        0x8,
        (
            "#01000F我会将有关恐怖分子的情报\x01",
            "传达给市长和警备队。\x02\x03",

            "达德利，这些小家伙\x01",
            "就拜托你照顾了。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x10A,
        (
            "#00603F嗯，交给我吧。\x02\x03",

            "#00601F……好了，你们几个，快出发吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0x101,
        "#00000F是！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_968")

    label("loc_906")


    #C0004
    ChrTalk(
        0x8,
        (
            "#01000F目前还不知道\x01",
            "地下空间发生了什么，\x01",
            "一定要小心些。\x02\x03",

            "达德利，这些小家伙\x01",
            "就拜托你照顾了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_968")

    TalkEnd(0xFE)
    Return()

    # Function_4_83F end

    def Function_5_96C(): pass

    label("Function_5_96C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A90")

    #C0005
    ChrTalk(
        0xA,
        (
            "#01100F大家一路顺风！\x02\x03",

            "#01109F嘿嘿嘿，达德利也要小心一点哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x10A,
        "#00603F都说过不要直呼别人的名字了……！\x02",
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0xA,
        "#01105F嗯？\x02",
    )

    CloseMessageWindow()
    OP_63(0x10A, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0008
    ChrTalk(
        0x10A,
        (
            "#00606F……唉唉！算了算了！\x01",
            "你们几个，赶快出发！\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x101,
        (
            "#00012F（唔……即使是达德利警官，\x01",
            "  也拿琪雅没办法啊。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_AE6")

    label("loc_A90")


    #C0010
    ChrTalk(
        0xA,
        (
            "#01109F大家一路顺风！\x02\x03",

            "嘿嘿嘿，达德利也要小心一点哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x10A,
        "#00603F（真是的……）\x02",
    )

    CloseMessageWindow()

    label("loc_AE6")

    TalkEnd(0xFE)
    Return()

    # Function_5_96C end

    def Function_6_AEA(): pass

    label("Function_6_AEA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D2A")

    #C0012
    ChrTalk(
        0x9,
        "#01200F咕呜呜呜呜……\x02",
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x10A,
        (
            "#00603F哼，这匹狼还是这么盛气凌人啊。\x02\x03",

            "#00600F但既然现在的身份是警犬，\x01",
            "我们便需要借助你的力量。\x01",
            "做好随时出动的准备吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x9,
        "#01200F……嗷。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_BD7")
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)

    label("loc_BD7")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C0B")
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)

    label("loc_C0B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C3F")
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)

    label("loc_C3F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C73")
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)

    label("loc_C73")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CA7")
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)

    label("loc_CA7")

    Sleep(1000)

    #C0015
    ChrTalk(
        0x104,
        (
            "#00306F（盛气凌人这个词\x01",
            "  该用在他自己身上才对吧……）\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x102,
        (
            "#00100F（呵呵，这也是达德利警官\x01",
            "  特有的激励方法啊。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_D47")

    label("loc_D2A")


    #C0017
    ChrTalk(
        0x9,
        "#01200F咕呜呜呜……嗷。\x02",
    )

    CloseMessageWindow()

    label("loc_D47")

    TalkEnd(0xFE)
    Return()

    # Function_6_AEA end

    def Function_7_D4B(): pass

    label("Function_7_D4B")

    TalkBegin(0xFF)

    #C0018
    ChrTalk(
        0x101,
        (
            "#00000F这里是缇欧的房间，\x01",
            "还是不要进去了。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFF)
    Return()

    # Function_7_D4B end

    def Function_8_D82(): pass

    label("Function_8_D82")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis416.itp")
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis120.itp")
    CreatePortrait(2, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis124.itp")
    CreatePortrait(3, 176, 36, 304, 164, 0, 0, 512, 256, 0, 0, 128, 128, 0xFFFFFF, 0x0, "c_vis239.itp")
    OP_68(14100, 1750, 12300, 0)
    MoveCamera(40, 17, 0, 0)
    OP_6E(380, 0)
    SetCameraDistance(22000, 0)
    OP_90(0x101, 1700, 850, 14100, 180)
    OP_90(0x102, 600, 4850, 14400, 180)
    OP_90(0x153, 1700, 4850, 15400, 180)
    OP_90(0x109, 600, 4850, 15700, 180)
    OP_90(0x105, 1700, 4850, 16700, 180)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x153, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    SetChrPos(0x8, 14100, 850, 12300, 0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrChipByIndex(0x9, 0x5)
    SetChrSubChip(0x9, 0x0)
    SetChrPos(0x9, 13100, 850, 9300, 0)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    OP_52(0x9, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SoundLoad(98)
    SoundLoad(2668)
    ClearMapObjFlags(0x19, 0x4)
    SetMapObjFlags(0x19, 0x1000)
    OP_70(0x19, 0x32)
    SetCameraDistance(24000, 3000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)

    #C0019
    ChrTalk(
        0x8,
        (
            "#01003F#11P嗯，嗯……\x02\x03",

            "#01000F是啊，\x01",
            "他们应该快回来了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    #Sound(3054, 255, 80, 0)    #voice#Zeit

    #C0020
    ChrTalk(
        0x9,
        "#01200F#12P嗷。\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0x8, 0x10E, 0x1F4)

    #C0021
    ChrTalk(
        0x8,
        (
            "#01005F#11P……哦，\x01",
            "回来得正是时候。\x02",
        )
    )

    CloseMessageWindow()

    #N0022
    NpcTalk(
        0x101,
        "罗伊德的声音",
        "我们回来了。\x02",
    )

    CloseMessageWindow()
    OP_68(4100, 1750, 10400, 2500)
    SetCameraDistance(25000, 2500)
    Sleep(1000)
    OP_90(0x101, 1700, 4850, 14100, 180)
    BeginChrThread(0x101, 3, 0, 9)

    def lambda_108D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_108D)
    Sleep(400)

    def lambda_10A1():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_10A1)
    Sleep(600)

    def lambda_10B5():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x153, 2, lambda_10B5)
    Sleep(400)

    def lambda_10C9():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_10C9)
    Sleep(600)

    def lambda_10DD():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_10DD)
    WaitChrThread(0x101, 0)

    def lambda_10F2():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_10F2)
    WaitChrThread(0x102, 0)

    def lambda_1103():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1103)
    WaitChrThread(0x153, 0)

    def lambda_1114():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x153, 2, lambda_1114)
    WaitChrThread(0x109, 0)

    def lambda_1125():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_1125)
    WaitChrThread(0x105, 0)

    def lambda_1136():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_1136)

    #C0023
    ChrTalk(
        0x153,
        "#5P#01110F科长，我们回来啦。\x02",
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x102,
        "#6P#00105F啊，正在和人通话吗？\x02",
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x8,
        "#01004F#12P没事，不用介意。\x02",
    )

    CloseMessageWindow()
    OP_93(0x8, 0x0, 0x1F4)
    Sleep(300)
    Sound(838, 0, 100, 0)
    SetMapObjFlags(0x19, 0x4)
    Sleep(500)
    OP_93(0x8, 0x5A, 0x1F4)
    Sleep(300)

    #C0026
    ChrTalk(
        0x8,
        (
            "#01002F#6P好了，赶快启动\x01",
            "那部终端吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x101,
        "#6P#00005F哎……？\x02",
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x102,
        (
            "#6P#00100F警察总部\x01",
            "发来了联络吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x8,
        (
            "#01003F#6P启动了就知道啦。\x02\x03",

            "#01001F二位新人和琪雅\x01",
            "也到这边来。\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x153,
        "#5P#01100F嗯？\x02",
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x109,
        "#6P#10105F是、是的。\x02",
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x105,
        "#10300F好像有什么事情啊。\x02",
    )

    CloseMessageWindow()

    def lambda_12C8():
        OP_97(0x101, 0x1B58, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_12C8)
    Sleep(250)

    def lambda_12E5():
        OP_97(0x153, 0x1B58, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x153, 0, lambda_12E5)
    Sleep(250)

    def lambda_1302():
        OP_97(0x102, 0x1B58, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1302)
    Sleep(250)

    def lambda_131F():
        OP_97(0x109, 0x1B58, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_131F)
    Sleep(100)
    Fade(1000)
    OP_68(16300, 1750, 10200, 0)
    MoveCamera(13, 20, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(23500, 0)
    EndChrThread(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    EndChrThread(0x153, 0xFF)
    SetChrSubChip(0x153, 0x0)
    EndChrThread(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    EndChrThread(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    SetChrPos(0x101, 16300, 850, 10200, 45)
    SetChrPos(0x102, 14800, 850, 9500, 45)
    SetChrPos(0x153, 15250, 850, 8500, 45)
    SetChrPos(0x109, 16200, 850, 7400, 0)
    SetChrPos(0x105, 17200, 850, 7800, 0)
    SetChrPos(0x8, 14200, 850, 11900, 135)
    SetChrPos(0x9, 13100, 850, 8900, 45)
    OP_68(16800, 1750, 10700, 2000)
    OP_0D()
    OP_6F(0x79)

    #C0033
    ChrTalk(
        0x101,
        "#5P#00001F嗯……\x02",
    )

    CloseMessageWindow()
    Sound(836, 0, 100, 0)
    Sleep(1200)
    StopBGM(0xBB8)
    Sound(72, 0, 100, 0)
    OP_CB(0x2, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    Sleep(500)
    OP_CB(0x3, 0x1, 0x3E8, 0x0, 0x0, 0x0)
    OP_CB(0x3, 0x0, 0x0, 0x17700, 0x0, 0x0)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x0, 0x0, 0x0)
    OP_CB(0x2, 0x3, 0xFFFFFF, 0xFA, 0x0, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    Sound(1021, 0, 100, 0)
    OP_CB(0x3, 0x0, 0x0, 0x0, 0xFA, 0x0)
    OP_CB(0x3, 0x1, 0x3E8, 0x3E8, 0xFA, 0x0)
    OP_CB(0x3, 0x3, 0xFFFFFFFF, 0xFA, 0x0, 0x0)
    OP_CC(0x0, 0x3, 0x3)
    Sleep(300)

    #A0034
    AnonymousTalk(
        0x101,
        "#00005F！！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0035
    AnonymousTalk(
        0x102,
        "#00105F缇欧！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0036
    AnonymousTalk(
        0x153,
        "#01109F啊，是缇欧！\x02",
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7515", 0)
    Sleep(500)
    SetMessageWindowPos(-1, 150, -1, -1)
    OP_C9(0x0, 0x80000000)
    SetChrName("缇欧")

    #A0037
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#2668V#40W……晚上好，\x01",
            "好久不见了。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_24(0xA6C)
    OP_C9(0x1, 0x80000000)
    SetMessageWindowPos(14, 280, 60, 3)

    #A0038
    AnonymousTalk(
        0x101,
        (
            "#00002F缇欧……！\x01",
            "这究竟是……\x02\x03",

            "莫非你已经回到\x01",
            "克洛斯贝尔了吗！？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    OP_CB(0x3, 0x8, 0x200, 0x0, 0x300, 0x100)
    OP_0D()
    #Sound(2273, 255, 100, 0)    #voice#Tio
    Sleep(800)
    SetMessageWindowPos(-1, 150, -1, -1)
    SetChrName("缇欧")

    #A0039
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#30W……我还在列曼自治州的\x01",
            "爱普斯泰恩财团研究所。\x02\x03",

            "我的归期会比\x01",
            "预定时间稍有推迟……\x02\x03",

            "所以才提出任性要求，\x01",
            "使用了远程线路。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    #A0040
    AnonymousTalk(
        0x101,
        "#00000F这样啊……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0041
    AnonymousTalk(
        0x102,
        (
            "#00109F缇欧……\x01",
            "能看到你的脸，我好开心啊。\x02\x03",

            "#00105F啊，不过导力网络\x01",
            "并不能连接到自治州\x01",
            "以外的区域吧……？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    OP_CB(0x3, 0x8, 0x100, 0x0, 0x200, 0x100)
    OP_0D()
    SetMessageWindowPos(-1, 150, -1, -1)
    SetChrName("缇欧")

    #A0042
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "是的，原本必须要通过实体线路\x01",
            "才能处理这种庞大的情报量。\x02\x03",

            "但财团与ＩＢＣ正在推进\x01",
            "远程连接实验。\x02\x03",

            "在列曼自治州与克洛斯贝尔\x01",
            "自治州之间架设了十部左右\x01",
            "的强力无线信号增幅装置……\x02\x03",

            "如此一来，就可以像现在这样，\x01",
            "传输影像与声音信息了。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    #A0043
    AnonymousTalk(
        0x102,
        "#00102F原来如此……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0044
    AnonymousTalk(
        0x101,
        "#00004F技术的进步可真是惊人啊……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0045
    AnonymousTalk(
        0x153,
        (
            "#01110F缇欧缇欧！\x02\x03",

            "你刚才说要延后才回来，\x01",
            "到底要延后多久啊？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(-1, 150, -1, -1)
    SetChrName("缇欧")

    #A0046
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "我想大约要等到\x01",
            "月底或下月初吧。\x02\x03",

            "这段时间不能和琪雅见面，\x01",
            "就靠这种通讯\x01",
            "来坚持一下吧。\x02\x03",

            "所以，琪雅一定要\x01",
            "让我看到更可爱的表情哦。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    #A0047
    AnonymousTalk(
        0x153,
        (
            "#01109F嘿嘿嘿……嗯！\x02\x03",

            "#01110F来，蔡特也过来\x01",
            "让缇欧看看吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0048
    AnonymousTalk(
        0x9,
        "#01200F咕呜呜呜……嗷。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(-1, 150, -1, -1)
    SetChrName("缇欧")

    #A0049
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "嗯，没问题，\x01",
            "我很好的。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    #A0050
    AnonymousTalk(
        0x101,
        "#00002F哈哈……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0051
    AnonymousTalk(
        0x102,
        (
            "#00104F呵呵……导力网络\x01",
            "还能给人带来这种恩惠啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    OP_CB(0x3, 0x8, 0x300, 0x0, 0x400, 0x100)
    OP_0D()
    SetMessageWindowPos(-1, 150, -1, -1)
    SetChrName("缇欧")

    #A0052
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "对了，兰迪前辈\x01",
            "好像还没回来啊……\x02\x03",

            "诺艾尔小姐和瓦吉先生\x01",
            "已经正式加入了吧？\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    #A0053
    AnonymousTalk(
        0x101,
        (
            "#00000F嗯，我们今天刚刚\x01",
            "开始工作。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0054
    AnonymousTalk(
        0x109,
        (
            "#10102F呵呵……\x01",
            "缇欧，好久不见！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0055
    AnonymousTalk(
        0x105,
        (
            "#10302F哟，\x01",
            "我也来打扰一下吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    OP_CB(0x3, 0x8, 0x100, 0x0, 0x200, 0x100)
    OP_0D()
    SetMessageWindowPos(-1, 150, -1, -1)
    SetChrName("缇欧")

    #A0056
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "呵呵……\x01",
            "二位，好久不见了。\x02\x03",

            "话说回来，诺艾尔小姐\x01",
            "调任到支援科倒也罢了……\x02\x03",

            "但瓦吉先生站在那里，\x01",
            "感觉真有点不可思议呢。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    #A0057
    AnonymousTalk(
        0x105,
        "#10309F啊哈哈，我也这么想。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0058
    AnonymousTalk(
        0x109,
        (
            "#10106F真是的……\x01",
            "这并不好笑吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0059
    AnonymousTalk(
        0x101,
        (
            "#00004F哈哈，算啦，\x01",
            "眼下就先保持这个阵容吧。\x02\x03",

            "#00002F不过，缇欧……\x01",
            "你可要早点回来啊！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0060
    AnonymousTalk(
        0x102,
        (
            "#00102F嗯，没有缇欧的支援科\x01",
            "根本不能算真正的支援科。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0061
    AnonymousTalk(
        0x153,
        "#01109F嗯嗯！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    OP_CB(0x3, 0x8, 0x200, 0x0, 0x300, 0x100)
    OP_0D()
    SetMessageWindowPos(-1, 150, -1, -1)
    SetChrName("缇欧")

    #A0062
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "呵呵……那我一定会尽量努力，\x01",
            "争取早些回来。\x02\x03",

            "原本想把约纳\x01",
            "也叫来的……\x02\x03",

            "但他大概是工作了一通宵，\x01",
            "用艾尼格玛怎么呼叫都没用。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    #A0063
    AnonymousTalk(
        0x101,
        (
            "#00000F是吗……\x01",
            "看来他也很努力呢。\x02\x03",

            "#00006F应该是想努力弥补\x01",
            "以前给财团造成的损失吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0064
    AnonymousTalk(
        0x102,
        (
            "#00104F希望他别太\x01",
            "勉强自己。\x02\x03",

            "#00100F当然，缇欧也不要\x01",
            "太过拼命哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    OP_CB(0x3, 0x8, 0x100, 0x0, 0x200, 0x100)
    OP_0D()
    SetMessageWindowPos(-1, 150, -1, -1)
    SetChrName("缇欧")

    #A0065
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "嗯，知道了。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sound(839, 0, 90, 0)
    Sleep(400)
    Sound(839, 0, 90, 0)
    Sleep(600)
    Sound(2274, 255, 50, 0)    #voice#Tio
    Fade(250)
    OP_CB(0x3, 0x8, 0x300, 0x0, 0x400, 0x100)
    OP_0D()
    Sleep(1500)
    Sound(2676, 255, 100, 0)    #voice#Tio
    Fade(250)
    OP_CB(0x3, 0x8, 0x0, 0x100, 0x100, 0x200)
    OP_0D()
    Sleep(1200)
    SetMessageWindowPos(-1, 150, -1, -1)
    SetChrName("缇欧")

    #A0066
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "……抱歉，\x01",
            "已经快到时间了。\x02\x03",

            "因为我是在任性使用\x01",
            "实验用的线路……\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    #A0067
    AnonymousTalk(
        0x101,
        "#00001F是吗……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0068
    AnonymousTalk(
        0x102,
        (
            "#00106F本来还想再聊聊呢，\x01",
            "真遗憾啊……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0069
    AnonymousTalk(
        0x8,
        (
            "#01004F算了，以后还会有机会的。\x02\x03",

            "#01002F缇欧，等你定下回来的时间，\x01",
            "就再和我联络吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    OP_CB(0x3, 0x8, 0x100, 0x0, 0x200, 0x100)
    OP_0D()
    SetMessageWindowPos(-1, 150, -1, -1)
    SetChrName("缇欧")

    #A0070
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "明白了。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 4)), scpexpr(EXPR_END)), "loc_21D7")

    #A0071
    AnonymousTalk(
        0x101,
        (
            "#00004F……缇欧。\x02\x03",

            "#00002F等你这次回来之后，\x01",
            "我一定会兑现当时的约定。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    OP_CB(0x3, 0x8, 0x100, 0x100, 0x200, 0x200)
    OP_0D()
    Sound(2275, 255, 100, 0)    #voice#Tio
    Sleep(1000)
    SetMessageWindowPos(-1, 150, -1, -1)
    SetChrName("缇欧")

    #A0072
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "嗯……\x01",
            "我很期待。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    #A0073
    AnonymousTalk(
        0x153,
        "#01111F约定～？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0074
    AnonymousTalk(
        0x102,
        (
            "#00104F实在是让人有点在意呢……\x01",
            "算啦，不管了。\x02\x03",

            "#00102F缇欧，\x01",
            "以后有机会再联络啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    OP_CB(0x3, 0x8, 0x100, 0x0, 0x200, 0x100)
    OP_0D()

    #A0075
    AnonymousTalk(
        0x109,
        (
            "#10109F保重哦！\x01",
            "要注意身体！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_224D")

    label("loc_21D7")


    #A0076
    AnonymousTalk(
        0x101,
        (
            "#00002F嗯，缇欧，\x01",
            "要保重身体啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0077
    AnonymousTalk(
        0x102,
        (
            "#00102F等以后有机会时，\x01",
            "还要再联络哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0078
    AnonymousTalk(
        0x109,
        "#10109F缇欧，保重哦！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_224D")


    #A0079
    AnonymousTalk(
        0x105,
        "#10302F晚安，做个好梦。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0080
    AnonymousTalk(
        0x9,
        "#01200F咕呜呜……嗷。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0081
    AnonymousTalk(
        0x153,
        "#01110F再见啦～缇欧！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    OP_CB(0x3, 0x8, 0x200, 0x0, 0x300, 0x100)
    OP_0D()
    Sound(2276, 255, 100, 0)    #voice#Tio
    Sleep(1000)
    SetMessageWindowPos(-1, 150, -1, -1)
    SetChrName("缇欧")

    #A0082
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "嗯，那就再见啦，\x01",
            "大家晚安。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sound(1021, 0, 50, 0)
    Sound(939, 0, 50, 0)
    OP_CB(0x3, 0x0, 0x0, 0x17700, 0xFA, 0x0)
    OP_CB(0x3, 0x1, 0x3E8, 0x0, 0xFA, 0x0)
    OP_CB(0x3, 0x3, 0xFFFFFF, 0xFA, 0x0, 0x0)
    OP_CC(0x0, 0x3, 0x3)
    Sleep(500)
    OP_24(0x3AB)
    Sound(73, 0, 100, 0)
    OP_68(16300, 1750, 10200, 2000)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_6F(0x79)
    Sleep(500)

    #C0083
    ChrTalk(
        0x153,
        "#6P#01106F消失了……\x02",
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x101,
        "#00008F嗯……\x02",
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0x102,
        (
            "#6P#00104F……不知为何，看到她的脸之后，\x01",
            "就更想赶快见面了。\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x105,
        "#12P#10302F呵呵，这就是青春啊。\x02",
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x109,
        (
            "#6P#10109F嘿，支援科成员之间\x01",
            "的关系真是很好啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0x101,
        (
            "#00004F哈哈，但最初也都是\x01",
            "互不相识的陌生人呢。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x8, 500)
    Sleep(300)

    #C0089
    ChrTalk(
        0x101,
        (
            "#11P#00000F对了，科长，\x01",
            "我们回来晚了，真抱歉。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_24CC():
        TurnDirection(0x102, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_24CC)
    Sleep(50)

    def lambda_24DC():
        TurnDirection(0x109, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_24DC)
    Sleep(50)

    def lambda_24EC():
        TurnDirection(0x105, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_24EC)
    Sleep(50)

    def lambda_24FC():
        TurnDirection(0x153, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x153, 0, lambda_24FC)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x153, 0)

    #C0090
    ChrTalk(
        0x8,
        (
            "#01004F哦，不用介意。\x02\x03",

            "#01000F今天的报告\x01",
            "就稍后再听吧……\x02\x03",

            "晚饭准备得怎么样了？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0091
    ChrTalk(
        0x101,
        "#11P#00011F啊，对了，都给忘了！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)

    #C0092
    ChrTalk(
        0x102,
        (
            "#6P#00108F说起来，我们换成这个阵容之后，\x01",
            "还没有排过做饭的轮班表呢……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_261E():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_261E)
    Sleep(100)

    def lambda_262E():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x153, 2, lambda_262E)
    WaitChrThread(0x109, 2)

    #C0093
    ChrTalk(
        0x109,
        (
            "#6P#10105F是吗，原来特别任务支援科\x01",
            "的伙食是轮班负责制啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x105,
        (
            "#12P#10305F什么嘛，原来是这样啊。\x02\x03",

            "#10306F……唔，\x01",
            "这可真是有点麻烦呢。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12B, 3)), scpexpr(EXPR_END)), "loc_279D")

    #C0095
    ChrTalk(
        0x101,
        (
            "#00003F瓦吉既然加入了支援科，\x01",
            "也要尽责分担烹饪工作哦。\x02\x03",

            "#00000F而且你的料理水平似乎意外地好呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0x105,
        (
            "#12P#10304F还好吧，一般而已。\x02\x03",

            "#10300F因为太麻烦，所以我一般\x01",
            "都是推给阿巴斯他们来做的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2899")

    label("loc_279D")


    #C0097
    ChrTalk(
        0x101,
        (
            "#00003F瓦吉既然加入了支援科，\x01",
            "也要尽责分担烹饪工作哦。\x02\x03",

            "#00000F之前正好得到了新的料理手册，\x01",
            "如果你不会做，我可以指点一下。\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x105,
        (
            "#12P#10302F那可真是让人开心啊，\x01",
            "但我的料理水平还算过得去。\x02\x03",

            "#10309F只是因为太麻烦，所以平时\x01",
            "一般都推给阿巴斯他们来做。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2899")


    #C0099
    ChrTalk(
        0x101,
        (
            "#00013F唉，既然如此，\x01",
            "就不必发牢骚了啊！\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0x102,
        (
            "#6P#00109F呵呵，那今天就由大家\x01",
            "分工协作，一起完成吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0x109,
        (
            "#6P#10102F好，那就做一些\x01",
            "简单快速的料理吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x153,
        "#6P#01109F琪雅也来帮忙！\x02",
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0x8,
        (
            "#01006F……哎呀呀，\x01",
            "那我就喝着咖啡，休息一下吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0x9,
        "#6P#01203F咕呜呜……嗷。\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(24000, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    StopBGM(0xFA0)
    WaitBGM()
    Sleep(1000)
    Sound(13, 0, 100, 0)
    Sleep(4000)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(2000)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    RemoveParty(0x52, 0xFF)
    OP_CC(0x1, 0xFF, 0x0)
    OP_32(0xFF, 0xFE, 0x0)
    SetScenarioFlags(0x22, 1)
    NewScene("c0120", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_8_D82 end

    def Function_9_2A17(): pass

    label("Function_9_2A17")


    def lambda_2A1C():
        OP_97(0x101, 0x0, 0x0, 0xFFFFEC78, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2A1C)
    Sleep(200)

    def lambda_2A39():
        OP_97(0x102, 0x0, 0x0, 0xFFFFEC78, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_2A39)
    Sleep(200)

    def lambda_2A56():
        OP_97(0x153, 0x0, 0x0, 0xFFFFEC78, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x153, 0, lambda_2A56)
    Sleep(200)

    def lambda_2A73():
        OP_97(0x109, 0x0, 0x0, 0xFFFFEC78, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_2A73)
    Sleep(200)

    def lambda_2A90():
        OP_97(0x105, 0x0, 0x0, 0xFFFFEC78, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_2A90)
    Return()

    # Function_9_2A17 end

    def Function_10_2AA6(): pass

    label("Function_10_2AA6")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch03400.itc", 0x1E)
    LoadChrToIndex("apl/ch51201.itc", 0x1F)
    LoadChrToIndex("apl/ch50091.itc", 0x20)
    LoadChrToIndex("chr/ch02710.itc", 0x21)
    SoundLoad(3942)
    SoundLoad(3943)
    SoundLoad(3944)
    SoundLoad(3945)
    SoundLoad(3946)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu04601.itp")
    SetChrPos(0x101, 1200, 0, -2000, 0)
    SetChrPos(0x102, 300, 0, -1800, 0)
    SetChrPos(0x104, 2700, 0, 5000, 90)
    SetChrPos(0x109, 1200, 0, -2300, 0)
    SetChrPos(0x105, 300, 0, -2100, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0xB, 0x1F)
    SetChrSubChip(0xB, 0x3)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8000)
    SetChrFlags(0xB, 0x10)
    SetChrFlags(0xB, 0x2)
    SetChrFlags(0xB, 0x20)
    SetChrPos(0xB, 5300, 150, 6250, 180)
    OP_52(0xB, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x9, 0x6)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, 900, 0, -3000, 0)
    OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0xA, 0x2)
    SetChrSubChip(0xA, 0x0)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)
    SetChrPos(0xA, 700, 0, -2500, 0)
    OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x13, 0x20)
    SetChrSubChip(0x13, 0x1D)
    SetChrFlags(0x13, 0x8000)
    SetChrPos(0x13, 5300, 330, 4600, 0)
    ClearChrFlags(0x13, 0x80)
    ClearChrBattleFlags(0x13, 0x8000)
    OP_68(5300, 900, 6250, 0)
    MoveCamera(50, 19, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(22000, 0)
    SetCameraDistance(24000, 3000)
    StopBGM(0xFA0)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)
    OP_68(4000, 1000, 5250, 2500)
    MoveCamera(40, 19, 0, 2500)
    BeginChrThread(0x104, 3, 0, 11)
    WaitChrThread(0x104, 3)
    WaitChrThread(0x101, 3)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0105
    ChrTalk(
        0x101,
        "#12P#00011F什么……！\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x102, 3)
    WaitChrThread(0x109, 3)
    WaitChrThread(0x105, 3)
    OP_6F(0x79)

    #C0106
    ChrTalk(
        0x102,
        "#6P#00105F兰迪的堂妹……\x02",
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7561", 0)
    SetChrSubChip(0xB, 0x4)
    Sleep(300)
    OP_C9(0x0, 0x80000000)

    #C0107
    ChrTalk(
        0xB,
        (
            "#11P#04609F#3942V#30W嘿嘿嘿，大家好。\x01",
            "我是谢莉·奥兰多。\x02\x03",

            "#04602F#3943V你们好慢啊，\x01",
            "我都等得不耐烦啦。\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xF67)
    OP_C9(0x1, 0x80000000)
    OP_57(0x0)
    OP_5A()

    #C0108
    ChrTalk(
        0x104,
        (
            "#6P#00301F#30W……你……\x02\x03",

            "究竟为何来此……？\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0xB,
        (
            "#11P#04605F啊，兰迪哥好无情啊。\x02\x03",

            "#04606F面对久别两年的可爱妹妹，\x01",
            "态度未免也太冷淡了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0x104,
        (
            "#6P#00303F#30W够了，快回答我……\x01",
            "你来这里要做什么？\x02\x03",

            "#00311F不……你在这里做了什么？\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0xB,
        "#11P#04604F呵呵……\x02",
    )

    CloseMessageWindow()
    Fade(800)
    SetCameraDistance(22800, 800)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_6F(0x79)
    OP_C9(0x0, 0x80000000)

    #A0112
    AnonymousTalk(
        0xB,
        (
            "#3944V#40W兰迪哥，你太迟钝啦。\x02\x03",

            "#3945V#30W如果我之前布置好机关，你们在进门\x01",
            "的一瞬间就会变成一堆碎肉了哦～\x02\x03",

            "#3946V你从什么时候开始\x01",
            "变得这么没用了？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_24(0xF6A)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    OP_C9(0x1, 0x80000000)

    #C0113
    ChrTalk(
        0x104,
        "#6P#00311F#30W…………………………………\x02",
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0x102,
        "#6P#00101F你……\x02",
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0x109,
        "#12P#N#10107F你在说些什么……！\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0116
    ChrTalk(
        0xB,
        (
            "#11P#04612F呵呵，不必担心，\x01",
            "我没布置什么机关啦。\x02\x03",

            "#04602F如果只有兰迪哥一个人，\x01",
            "倒是可以像以前一样玩玩那种游戏。\x02\x03",

            "#04604F除非是在战争中，不然我们\x01",
            "并不想把一般人卷入其中。\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0x102,
        "#6P#00110F你……\x02",
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0xA,
        "#01105F#6P#N哎……\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0119
    ChrTalk(
        0x105,
        (
            "#6P#N#10306F呼……\x01",
            "又是个过激派的孩子啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    #C0120
    ChrTalk(
        0x101,
        (
            "#12P#00003F……你是叫\x01",
            "谢莉吧？\x02\x03",

            "#00001F做个正式自我介绍……\x01",
            "我是支援科的罗伊德·班宁斯。\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0xB,
        (
            "#11P#04602F啊，你好你好。\x02\x03",

            "#04609F上次真是不好意思哦，\x01",
            "一时兴起就咬了你的耳垂～\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0x101,
        (
            "#12P#00006F……那件事姑且不提。\x02\x03",

            "#00013F这里是克洛斯贝尔警察局的部门楼，\x01",
            "你所坐的那个沙发也是\x01",
            "用公费采购的物品。\x02\x03",

            "竟然说些机关陷阱、卷入一般人之类的话……\x01",
            "在小孩子的面前，\x01",
            "能否控制一下这种不妥当的发言？\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0xB,
        (
            "#11P#04612F啊哈哈，抱歉抱歉。\x02\x03",

            "#04611F只是因为太想念哥哥了，\x01",
            "所以想和他玩闹一下～\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0x104,
        (
            "#6P#00306F……哼，\x01",
            "你会想念我吗？\x02\x03",

            "#00301F多半是叔叔派你\x01",
            "来叫我的吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_3464():
        TurnDirection(0x101, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3464)
    Sleep(50)

    def lambda_3474():
        TurnDirection(0x102, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_3474)
    Sleep(50)

    def lambda_3484():
        TurnDirection(0x109, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_3484)
    Sleep(50)

    def lambda_3494():
        TurnDirection(0x105, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_3494)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)

    #C0125
    ChrTalk(
        0x101,
        "#12P#00005F哎……！\x02",
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0x102,
        "#6P#00101F这……\x02",
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0xB,
        "#11P#04604F呵呵，答对啦。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_68(4000, 800, 5250, 800)
    Sound(812, 0, 100, 0)
    SetChrChipByIndex(0xB, 0x1E)
    SetChrSubChip(0xB, 0x0)
    ClearChrFlags(0xB, 0x10)
    ClearChrFlags(0xB, 0x2)
    ClearChrFlags(0xB, 0x20)
    Sound(802, 0, 100, 0)
    OP_9D(0xB, 0x14B4, 0x1E, 0x157C, 0x1F4, 0xBB8)
    OP_93(0xB, 0x10E, 0x1F4)
    Sleep(300)

    #C0128
    ChrTalk(
        0xB,
        (
            "#04602F#11P爸爸当时不是和你说过吗，\x01",
            "近期要找你谈谈。\x02\x03",

            "从明天开始，大概就会很忙了，\x01",
            "所以希望定在今晚。\x02\x03",

            "#04605F啊，当然，你也可以拒绝哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0x104,
        (
            "#6P#00306F哈，但我要是拒绝的话，\x01",
            "你们恐怕就会不择手段了吧？\x02\x03",

            "#00311F我早就看透\x01",
            "你们的做事风格了。\x02",
        )
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0xB,
        (
            "#04609F#11P呵呵，看来你已经\x01",
            "恢复状态了嘛。\x02\x03",

            "#04602F爸爸在『诺艾·布朗』等着你，\x01",
            "意下如何？\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0x104,
        "#6P#00304F哼，好吧。\x02",
    )

    CloseMessageWindow()
    OP_68(4100, 800, 5360, 1000)
    BeginChrThread(0xA, 3, 0, 16)
    Sleep(150)
    TurnDirection(0x104, 0x101, 500)
    Sleep(300)

    #C0132
    ChrTalk(
        0x104,
        (
            "#5P#00300F各位，不好意思了，\x01",
            "今天的晚饭我就不──\x02",
        )
    )

    CloseMessageWindow()
    OP_6F(0x79)
    WaitChrThread(0xA, 3)

    #C0133
    ChrTalk(
        0xA,
        (
            "#6P#01101F兰迪，兰迪……\x02\x03",

            "这个姐姐\x01",
            "是坏人吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_37C0():
        TurnDirection(0x104, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_37C0)
    Sleep(50)

    def lambda_37D0():
        TurnDirection(0x101, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_37D0)
    Sleep(50)

    def lambda_37E0():
        TurnDirection(0x102, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_37E0)
    Sleep(50)

    def lambda_37F0():
        TurnDirection(0x109, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_37F0)
    Sleep(50)

    def lambda_3800():
        TurnDirection(0x105, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_3800)
    Sleep(50)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)

    #C0134
    ChrTalk(
        0x101,
        "#11P#00011F琪、琪雅……！\x02",
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0x102,
        "#6P#00107F琪雅，快回去……！\x02",
    )

    CloseMessageWindow()
    OP_68(3920, 800, 5320, 1000)
    MoveCamera(42, 20, 0, 1000)
    OP_6E(400, 1000)
    SetCameraDistance(24000, 1000)

    def lambda_3893():
        OP_95(0xFE, 1400, 0, 5500, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3893)
    Sleep(300)

    def lambda_38B0():
        OP_95(0xFE, 1800, 0, 4300, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_38B0)
    WaitChrThread(0x102, 1)

    def lambda_38CE():
        TurnDirection(0xFE, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_38CE)
    WaitChrThread(0x101, 1)
    TurnDirection(0x101, 0xA, 500)

    def lambda_38E6():
        OP_96(0xFE, 0x1F4, 0x0, 0x13EC, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_38E6)

    def lambda_3900():
        OP_96(0xFE, 0x384, 0x0, 0xF3C, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3900)

    def lambda_391A():
        OP_96(0xFE, 0x3E8, 0x0, 0x12C0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_391A)
    Sleep(300)

    def lambda_3937():
        OP_95(0xFE, 1300, 0, 2700, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_3937)
    Sleep(300)

    def lambda_3954():
        OP_95(0xFE, 2200, 0, 2500, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_3954)
    WaitChrThread(0x101, 1)

    def lambda_3972():
        TurnDirection(0xFE, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3972)

    #C0136
    ChrTalk(
        0xB,
        (
            "#04606F#11P说我是坏人？太过分了吧。\x02\x03",

            "#04605F嗯？这孩子是谁啊！？\x01",
            "也太可爱了吧！？\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0xA,
        "#6P#01105F嗯？\x02",
    )

    CloseMessageWindow()

    def lambda_39EA():
        TurnDirection(0xFE, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_39EA)
    Sleep(100)

    def lambda_39FA():
        TurnDirection(0xFE, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_39FA)

    def lambda_3A07():
        TurnDirection(0xFE, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_3A07)
    WaitChrThread(0x104, 2)
    Sleep(150)

    #C0138
    ChrTalk(
        0x104,
        (
            "#6P#00303F她是我们照顾的孩子。\x02\x03",

            "#00312F#30W要是敢动她，我就杀了你。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    OP_82(0x32, 0x0, 0xBB8, 0x96)

    #C0139
    ChrTalk(
        0x101,
        "#6P#00013F……！\x02",
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0x102,
        "#6P#00108F唔……\x02",
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0xB,
        (
            "#04612F#11P啊哈哈，知道啦。\x02\x03",

            "#04602F总之，我至少不会\x01",
            "炸掉这座大楼就是了。\x02\x03",

            "#04609F啊，只是开个玩笑哦～\x02",
        )
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0x109,
        "#12P#10106F（这、这是什么对话……）\x02",
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0x105,
        "#6P#10308F（真是刺激心脏啊。）\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 500)
    Sleep(300)

    #C0144
    ChrTalk(
        0x104,
        (
            "#5P#00304F──好了，事情就是这样，\x01",
            "我要到叔叔那里露个面。\x02\x03",

            "#00300F今晚就会回来的，\x01",
            "你们不用担心。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3BCE():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_3BCE)

    #C0145
    ChrTalk(
        0x102,
        "#6P#00108F可、可是……！\x02",
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0x109,
        "#12P#10101F终究还是太危险吧……！\x02",
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0x101,
        (
            "#6P#00006F那个……兰迪。\x02\x03",

            "#00000F既然如此，我也过去\x01",
            "和他们打个招呼如何？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(800)

    def lambda_3CF2():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3CF2)
    Sleep(50)

    def lambda_3D02():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3D02)
    Sleep(50)

    def lambda_3D12():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_3D12)
    Sleep(50)

    def lambda_3D22():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_3D22)
    Sleep(50)

    def lambda_3D32():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_3D32)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0148
    ChrTalk(
        0x104,
        "#5P#00305F！？\x02",
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0x102,
        "#5P#00107F哎！？\x02",
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0x109,
        "#11P#10111F罗、罗伊德警官……！？\x02",
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0x101,
        (
            "#6P#00004F身为支援科的队长，\x01",
            "与同事的亲属打个招呼\x01",
            "也算是基本礼仪。\x02\x03",

            "#00000F而且，能去那种高级俱乐部，\x01",
            "也算是一次不错的社会学习。\x02",
        )
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0xB,
        (
            "#04611F#11P嘿……小哥，你很有趣嘛。\x02\x03",

            "#04609F好啊好啊，反正机会难得，\x01",
            "你就一起来吧¤\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0xB, 500)
    Sleep(150)

    #C0153
    ChrTalk(
        0x105,
        (
            "#6P#10304F呵呵，那就再\x01",
            "加我一个好了。\x02\x03",

            "#10302F高级俱乐部『诺艾·布朗』……\x01",
            "我很想去见识见识呢。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x105, 500)

    #C0154
    ChrTalk(
        0xB,
        (
            "#04612F#11P英俊的小哥当然也欢迎！\x02\x03",

            "#04605F哎……\x01",
            "到底是小哥还是小姐呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0x105,
        (
            "#6P#10309F呵呵，姑且就算是\x01",
            "小哥好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0x104,
        (
            "#5P#00306F喂喂喂！\x01",
            "你们到底在想什么啊！？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0xB, 500)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0157
    ChrTalk(
        0x104,
        (
            "#6P#00307F谢莉，你不要\x01",
            "自作主张！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x104, 500)
    Sleep(150)

    #C0158
    ChrTalk(
        0xB,
        (
            "#04604F#11P好啦好啦，\x01",
            "我派车送你们过去。\x02\x03",

            "#04602F对了，两位姐姐要不要来？\x02\x03",

            "#04606F啊，不过那个孩子和狼\x01",
            "实在是不能一起过去哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0x101,
        (
            "#6P#00003F艾莉、诺艾尔，\x01",
            "你们和琪雅留下来吃晚饭吧。\x02\x03",

            "#00008F另外，别忘了联络科长。\x02\x03",

            "#00013F蔡特，在科长回来之前，\x01",
            "这里就拜托你守卫了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x101, 500)
    Sleep(100)

    #C0160
    ChrTalk(
        0x9,
        "#01201F#12P#N嗷。\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0161
    ChrTalk(
        0x102,
        (
            "#5P#00101F可、可是……！\x02\x03",

            "#00106F……明白了，\x01",
            "我们就留在这里。\x02",
        )
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0x109,
        "#11P#10101F……你们一定要小心啊！\x02",
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0xA,
        (
            "#5P#01110F罗伊德，\x01",
            "你要出门吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xA, 500)
    Sleep(150)

    #C0164
    ChrTalk(
        0x101,
        (
            "#12P#00004F嗯，我们三个\x01",
            "有些事情要出去。\x02\x03",

            "#00000F说不定会回来得比较晚，\x01",
            "早点睡觉，不要熬夜等哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0xA,
        (
            "#5P#01109F嗯！\x01",
            "路上小心！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 500)

    #C0166
    ChrTalk(
        0x104,
        "#5P#00306F可恶，为什么会变成这样……\x02",
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0x105,
        "#6P#10302F毕竟得做好最坏的打算嘛。\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(24500, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    OP_CC(0x1, 0xFF, 0x0)
    StopBGM(0xFA0)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x12E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x22, 1)
    NewScene("c010B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_10_2AA6 end

    def Function_11_42C0(): pass

    label("Function_11_42C0")

    BeginChrThread(0x101, 3, 0, 12)
    Sleep(300)
    BeginChrThread(0x102, 3, 0, 12)
    Sleep(300)
    BeginChrThread(0x109, 3, 0, 13)
    Sleep(300)
    BeginChrThread(0x105, 3, 0, 13)
    BeginChrThread(0xA, 3, 0, 14)
    BeginChrThread(0x9, 3, 0, 15)
    Return()

    # Function_11_42C0 end

    def Function_12_42EE(): pass

    label("Function_12_42EE")


    def lambda_42F3():
        OP_98(0xFE, 0x0, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_42F3)
    Sleep(300)

    def lambda_4310():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4310)
    WaitChrThread(0xFE, 1)

    def lambda_4325():
        OP_97(0xFE, 0x5DC, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4325)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_12_42EE end

    def Function_13_433F(): pass

    label("Function_13_433F")


    def lambda_4344():
        OP_98(0xFE, 0x0, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4344)
    Sleep(300)

    def lambda_4361():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4361)
    WaitChrThread(0xFE, 1)

    def lambda_4376():
        OP_97(0xFE, 0x3E8, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4376)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_13_433F end

    def Function_14_4390(): pass

    label("Function_14_4390")

    Sleep(500)

    def lambda_4398():
        OP_96(0xFE, 0x2BC, 0x0, 0x1F4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4398)

    def lambda_43B2():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_43B2)
    WaitChrThread(0xFE, 1)

    def lambda_43C7():
        OP_96(0xFE, 0x190, 0x0, 0x9C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_43C7)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_14_4390 end

    def Function_15_43E8(): pass

    label("Function_15_43E8")

    Sleep(1500)
    SetChrChipByIndex(0x9, 0x21)
    SetChrSubChip(0x9, 0x0)

    def lambda_43F8():
        OP_98(0xFE, 0x0, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_43F8)

    def lambda_4412():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4412)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0x9, 0x6)
    SetChrSubChip(0x9, 0x0)
    OP_93(0x9, 0x2D, 0x1F4)
    Return()

    # Function_15_43E8 end

    def Function_16_4432(): pass

    label("Function_16_4432")


    def lambda_4437():
        OP_95(0xFE, 1900, 0, 5200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_4437)
    WaitChrThread(0xA, 1)
    TurnDirection(0xA, 0xB, 500)
    Return()

    # Function_16_4432 end

    def Function_17_4458(): pass

    label("Function_17_4458")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis120.itp")
    CreatePortrait(1, 176, 36, 304, 164, 0, 0, 512, 256, 0, 128, 128, 256, 0xFFFFFF, 0x0, "c_vis239.itp")
    OP_68(15900, 1750, 9800, 0)
    MoveCamera(45, 18, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(24500, 0)
    SetChrPos(0x101, 4000, 850, 15000, 0)
    SetChrPos(0x104, 4000, 850, 15000, 0)
    SetChrPos(0x105, 4000, 850, 15000, 0)
    SetChrPos(0x102, 16300, 850, 10200, 45)
    SetChrPos(0x109, 14500, 850, 9100, 45)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrChipByIndex(0x9, 0x5)
    SetChrSubChip(0x9, 0x0)
    SetChrPos(0x9, 2500, 0, 5000, 225)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    OP_52(0x9, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x9, 3, 0, 1)
    SetChrChipByIndex(0xA, 0x2)
    SetChrSubChip(0xA, 0x0)
    SetChrPos(0xA, 14900, 850, 8100, 45)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)
    SetCameraDistance(22500, 3000)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x1, 0x3)
    Sleep(500)
    SetMessageWindowPos(-1, 150, -1, -1)
    SetChrName("缇欧")

    #A0168
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "是吗……发生了那种事啊。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    #A0169
    AnonymousTalk(
        0x102,
        (
            "#00106F嗯……抱歉。\x02\x03",

            "#00108F你难得有机会联络，\x01",
            "结果却是这种情况……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    OP_CB(0x1, 0x8, 0x200, 0x100, 0x300, 0x200)
    OP_0D()
    SetMessageWindowPos(-1, 150, -1, -1)
    SetChrName("缇欧")

    #A0170
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "……哪里，\x01",
            "幸亏打来了。\x02\x03",

            "那今天就先这样吧，\x01",
            "下次有机会再联络。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    #A0171
    AnonymousTalk(
        0x102,
        "#00100F嗯，知道了。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0172
    AnonymousTalk(
        0xA,
        "#01102F缇欧，再见！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0173
    AnonymousTalk(
        0x109,
        (
            "#10100F那个……\x01",
            "不要太担心哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    OP_CB(0x1, 0x8, 0x200, 0x0, 0x300, 0x100)
    OP_0D()
    SetMessageWindowPos(-1, 150, -1, -1)
    SetChrName("缇欧")

    #A0174
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "嗯，那我这就断开了。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sound(1021, 0, 50, 0)
    Sound(939, 0, 50, 0)
    OP_CB(0x1, 0x0, 0x0, 0x17700, 0xFA, 0x0)
    OP_CB(0x1, 0x1, 0x3E8, 0x0, 0xFA, 0x0)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0xFA, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    Sleep(500)
    OP_24(0x3AB)
    Sound(73, 0, 100, 0)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    SetCameraDistance(23000, 1000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    OP_93(0x102, 0xE1, 0x1F4)

    #C0175
    ChrTalk(
        0x102,
        (
            "#00106F呼……\x02\x03",

            "#00108F罗伊德他们……\x01",
            "应该不要紧吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0x109,
        (
            "#6P#10106F对方毕竟是赤色星座，\x01",
            "实在是让人担心呢……\x02",
        )
    )

    CloseMessageWindow()
    Sound(103, 0, 100, 0)
    Sleep(300)
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 1000, 0, -1500, 0)
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    #N0177
    NpcTalk(
        0x8,
        "赛尔盖的声音",
        "我回来了。\x02",
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_4957():

        label("loc_4957")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_4957")

    QueueWorkItem2(0xA, 2, lambda_4957)
    Sleep(50)

    def lambda_496C():

        label("loc_496C")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_496C")

    QueueWorkItem2(0x109, 2, lambda_496C)
    Sleep(50)

    def lambda_4981():

        label("loc_4981")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_4981")

    QueueWorkItem2(0x102, 2, lambda_4981)

    #C0178
    ChrTalk(
        0xA,
        "#01110F#11P啊，科长！\x02",
    )

    CloseMessageWindow()
    OP_68(1960, 1750, 2650, 2500)
    MoveCamera(40, 17, 0, 2500)
    OP_6E(380, 2500)
    SetCameraDistance(24000, 2500)
    Sleep(2000)

    def lambda_49DF():
        OP_95(0xFE, 1000, 0, 1500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_49DF)

    def lambda_49F9():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_49F9)
    WaitChrThread(0x8, 1)
    TurnDirection(0x8, 0x102, 500)
    OP_6F(0x79)
    Sound(104, 0, 100, 0)

    #C0179
    ChrTalk(
        0x102,
        "#00102F科长……！\x02",
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0x109,
        "#10102F#6P您、您辛苦了。\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x8, 3, 0, 18)
    Sleep(1000)
    Fade(1000)
    OP_68(14300, 1850, 9700, 0)
    MoveCamera(40, 21, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(23500, 0)
    EndChrThread(0x8, 0xFF)
    SetChrPos(0x8, 6300, 850, 9700, 90)

    def lambda_4AA3():
        OP_95(0xFE, 12300, 850, 9700, 2200, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_4AA3)
    SetCameraDistance(22500, 2500)
    OP_0D()
    WaitChrThread(0x8, 1)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x109, 0x2)
    EndChrThread(0xA, 0x2)
    OP_6F(0x79)

    #C0181
    ChrTalk(
        0x8,
        (
            "#6P#01000F我回来晚了，\x01",
            "状况没什么变化吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0x102,
        (
            "#11P#00106F嗯，和之前联络时\x01",
            "所说的情况一样……\x02",
        )
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0x109,
        (
            "#12P#10101F……不然我们也去\x01",
            "那家店的附近埋伏起来如何？\x02",
        )
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0x8,
        (
            "#6P#01004F不用那么担心。\x02\x03",

            "#01002F『诺艾·布朗』的周边地带\x01",
            "有一科的人在监视。\x02",
        )
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0x109,
        "#12P#10105F啊……！\x02",
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0x102,
        "#11P#00102F这、这样啊。\x02",
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0x8,
        (
            "#6P#01006F不过，只要那些家伙有意，\x01",
            "想把监视人员解决掉恐怕也毫不为难。\x02\x03",

            "#01000F……总之，我们今晚也只能\x01",
            "在这里等他们回来了。\x02",
        )
    )

    CloseMessageWindow()
    OP_68(14300, 2350, 9700, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    OP_CC(0x1, 0xFF, 0x0)
    StopBGM(0xFA0)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x22, 0)
    NewScene("c0490", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_17_4458 end

    def Function_18_4CBA(): pass

    label("Function_18_4CBA")


    def lambda_4CBF():
        OP_95(0xFE, 1000, 850, 10000, 2200, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_4CBF)
    WaitChrThread(0x8, 1)

    def lambda_4CDD():
        OP_95(0xFE, 10000, 850, 10000, 2200, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_4CDD)
    WaitChrThread(0x8, 1)
    Return()

    # Function_18_4CBA end

    def Function_19_4CF7(): pass

    label("Function_19_4CF7")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(64000, 1100, 8600, 0)
    MoveCamera(50, 15, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(24000, 0)
    SetChrPos(0x101, 63100, 0, 6900, 0)
    SetChrPos(0x102, 64000, 0, 5500, 0)
    SetChrPos(0x109, 65099, 0, 5100, 0)
    SetChrPos(0x104, 64400, 0, 6900, 0)
    SetChrPos(0x105, 62700, 0, 5500, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 64000, 150, 11400, 180)
    SetCameraDistance(23000, 2000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x10)

    #C0188
    ChrTalk(
        0x102,
        "#12P#00108F……竟然有这种事……\x02",
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0x109,
        (
            "#10106F真是一群……\x01",
            "可怕的家伙啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0x8,
        (
            "#01003F呼，让你继承『斗神』名号\x01",
            "的事情暂且不谈……\x02\x03",

            "#01000F此行还是有不少收获的吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0191
    ChrTalk(
        0x104,
        (
            "#00306F嗯……\x02\x03",

            "#00308F他们如今签下了一笔\x01",
            "一亿米拉左右的契约……\x02\x03",

            "#00301F从他们的口气来推测，\x01",
            "签署契约的对象肯定是帝国政府。\x02",
        )
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0x105,
        (
            "#12P#10304F而且他们还说，\x01",
            "明天就要开始忙了……\x02\x03",

            "#10300F自然是要在通商会议期间\x01",
            "做些什么吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0x8,
        (
            "#01003F唔，既然如此，\x01",
            "关于那笔一亿米拉契约的内容……\x02\x03",

            "#01001F罗伊德，你是怎么想的？\x02",
        )
    )

    CloseMessageWindow()

    #C0194
    ChrTalk(
        0x101,
        "#12P#00005F……啊，这个……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    #A0195
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1K一亿米拉契约的内容是什么？\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "暗杀共和国的总统\x01",        # 0
            "确保铁血宰相的安全\x01",      # 1
            "讨伐黑月\x01",                # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_5083"),
        (1, "loc_5276"),
        (2, "loc_5432"),
        (SWITCH_DEFAULT, "loc_55FC"),
    )


    label("loc_5083")


    #C0196
    ChrTalk(
        0x101,
        (
            "#12P#00008F暗杀卡尔瓦德共和国\x01",
            "的洛克史密斯总统……\x02\x03",

            "#00006F……不，不对。\x02\x03",

            "假如他们的目标真是如此，\x01",
            "一亿米拉的报酬未免也太少了。\x02",
        )
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0x8,
        (
            "#01004F呵呵，不错。\x02\x03",

            "#01002F从目前的情况来推测，\x01",
            "他们的任务应该是确保铁血宰相的安全。\x02",
        )
    )

    CloseMessageWindow()
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
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0198
    ChrTalk(
        0x101,
        "#12P#00011F啊……！\x02",
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0x102,
        (
            "#12P#00101F原、原来如此。\x02\x03",

            "据说奥斯本宰相\x01",
            "在帝国境内有\x01",
            "相当多的敌对势力……\x02",
        )
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0x104,
        "#00301F……的确有道理啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_55FC")

    label("loc_5276")

    OP_2C(0xA3, 0x1)

    #C0201
    ChrTalk(
        0x101,
        (
            "#12P#00003F……这只是我的直觉而已……\x02\x03",

            "#00001F据说铁血宰相在帝国境内\x01",
            "有相当多的敌对势力。\x02\x03",

            "赤色星座的任务或许是在克洛斯贝尔地区\x01",
            "抵御那些势力，确保宰相的安全。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_538D():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_538D)
    Sleep(50)

    def lambda_539D():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_539D)
    Sleep(50)

    def lambda_53AD():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_53AD)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)

    #C0202
    ChrTalk(
        0x102,
        "#12P#00105F啊……！\x02",
    )

    CloseMessageWindow()

    #C0203
    ChrTalk(
        0x104,
        (
            "#00301F……原来如此……\x01",
            "的确有道理啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0204
    ChrTalk(
        0x8,
        (
            "#01004F呵呵……\x01",
            "着眼点很不错。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_55FC")

    label("loc_5432")


    #C0205
    ChrTalk(
        0x101,
        (
            "#12P#00008F讨伐『黑月』……\x02\x03",

            "#00006F不对，在通商会议期间，\x01",
            "实在是不适合做出这种事情啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0206
    ChrTalk(
        0x8,
        (
            "#01004F呵呵，不错。\x02\x03",

            "#01002F从目前的情况来推测，\x01",
            "他们的任务应该是确保铁血宰相的安全。\x02",
        )
    )

    CloseMessageWindow()
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
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0207
    ChrTalk(
        0x101,
        "#12P#00011F啊……！\x02",
    )

    CloseMessageWindow()

    #C0208
    ChrTalk(
        0x102,
        (
            "#12P#00101F原、原来如此。\x02\x03",

            "据说奥斯本宰相\x01",
            "在帝国境内有\x01",
            "相当多的敌对势力……\x02",
        )
    )

    CloseMessageWindow()

    #C0209
    ChrTalk(
        0x104,
        "#00301F……的确有道理啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_55FC")

    label("loc_55FC")


    #C0210
    ChrTalk(
        0x105,
        (
            "#12P#10303F唔……但如果真是如此，\x01",
            "一亿米拉的报酬是不是有些多了？\x02\x03",

            "#10301F毕竟宰相还带着\x01",
            "自己的护卫人员。\x02",
        )
    )

    CloseMessageWindow()

    #C0211
    ChrTalk(
        0x109,
        (
            "#10106F的确……\x02\x03",

            "#10101F无论是帝国首脑还是共和国首脑，\x01",
            "应该都有相当多的\x01",
            "护卫军官同行呢。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14F, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14F, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x149, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_58A3")
    OP_2C(0xA3, 0x2)

    #C0212
    ChrTalk(
        0x101,
        (
            "#5P#00003F……自然和那种\x01",
            "表面上的护卫工作不同。\x02\x03",

            "#00008F通过赤色星座最近的动向便可发现，\x01",
            "他们正在以多种形式来\x01",
            "熟悉克洛斯贝尔这片土地。\x02",
        )
    )

    CloseMessageWindow()

    #C0213
    ChrTalk(
        0x105,
        (
            "#12P#10300F在阿尔摩利卡村、玛因兹，\x01",
            "还有贝尔加德门所得到的目击情报\x01",
            "似乎可以证实这一点呢。\x02\x03",

            "#10304F虽然他们有一些诸如采购食物、\x01",
            "买卖七耀石之类的正当理由……\x02",
        )
    )

    CloseMessageWindow()

    #C0214
    ChrTalk(
        0x101,
        (
            "#5P#00003F嗯，我认为他们之所以造访各地，\x01",
            "另有真实用意。\x02\x03",

            "#00001F恐怕和我们或游击士一样，是为了勘察地形，\x01",
            "以便在任何状况下都能迅速采取对策吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_599C")

    label("loc_58A3")


    #C0215
    ChrTalk(
        0x101,
        (
            "#5P#00003F……自然和那种\x01",
            "表面上的护卫工作不同。\x02\x03",

            "#00008F通过赤色星座最近的动向便可发现，\x01",
            "他们正在以多种形式来\x01",
            "熟悉克洛斯贝尔这片土地。\x02\x03",

            "#00001F恐怕和我们或游击士一样，是为了勘察地形，\x01",
            "以便在任何状况下都能迅速采取对策吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0216
    ChrTalk(
        0x105,
        "#12P#10300F嗯……\x02",
    )

    CloseMessageWindow()

    label("loc_599C")


    #C0217
    ChrTalk(
        0x102,
        (
            "#12P#00106F的确……\x01",
            "有那种感觉呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0218
    ChrTalk(
        0x104,
        "#00308F……………………………………\x02",
    )

    CloseMessageWindow()

    #C0219
    ChrTalk(
        0x8,
        (
            "#01000F嗯，现阶段所能做的推测\x01",
            "也只有这些了。\x02\x03",

            "#01003F明天将要召开兰花塔的揭幕式，\x01",
            "到时会有各国首脑来访。\x02\x03",

            "#01002F对了，你们也要\x01",
            "去现场哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_5B03():
        TurnDirection(0x101, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_5B03)
    Sleep(50)

    def lambda_5B13():
        TurnDirection(0x104, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_5B13)
    Sleep(50)

    def lambda_5B23():
        TurnDirection(0x109, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_5B23)
    Sleep(50)

    def lambda_5B33():
        TurnDirection(0x102, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_5B33)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x102, 0)

    #C0220
    ChrTalk(
        0x101,
        "#12P#00005F哎……\x02",
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0x102,
        "#12P#00105F去现场……是指揭幕式吗？\x02",
    )

    CloseMessageWindow()

    #C0222
    ChrTalk(
        0x8,
        (
            "#01004F因为你们的注意力已经\x01",
            "完全被『赤色星座』吸引了。\x02\x03",

            "#01000F但反间谍和对抗恐怖分子\x01",
            "并不是你们的工作。\x02\x03",

            "所以我要让你们转换心情，\x01",
            "再俯瞰一下全局。\x02",
        )
    )

    CloseMessageWindow()

    #C0223
    ChrTalk(
        0x101,
        "#12P#00000F……原来如此……\x02",
    )

    CloseMessageWindow()

    #C0224
    ChrTalk(
        0x104,
        (
            "#00304F哈哈……\x01",
            "真是尖锐的意见啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0x109,
        (
            "#10105F那个……前往揭幕式现场，\x01",
            "是要我们参加警备工作吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0x8,
        (
            "#01003F哦，名义上虽然是这样，\x01",
            "但你们只要专心观察\x01",
            "揭幕式的情况就行了。\x02\x03",

            "#01002F比如通商会议开始时的气氛……\x01",
            "还有首脑们的气场等等。\x02\x03",

            "这也许能让你们发现全新的视角。\x02",
        )
    )

    CloseMessageWindow()

    #C0227
    ChrTalk(
        0x101,
        "#12P#00000F……明白了。\x02",
    )

    CloseMessageWindow()

    #C0228
    ChrTalk(
        0x105,
        (
            "#12P#10302F呵呵，那我们就在特等席\x01",
            "尽情观赏吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_68(64000, 1600, 8600, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    OP_6F(0x79)
    SetScenarioFlags(0x22, 0)
    NewScene("e4010", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_19_4CF7 end

    def Function_20_5DD7(): pass

    label("Function_20_5DD7")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    AddParty(0x9, 0xFF, 0xFF)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis120.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu00600.itp")
    CreatePortrait(2, 176, 36, 304, 164, 0, 0, 512, 256, 128, 0, 256, 128, 0xFFFFFF, 0x0, "c_vis240.itp")
    SoundLoad(3452)
    SoundLoad(4106)
    SoundLoad(3609)
    SoundLoad(3610)
    OP_68(64000, 1100, 8600, 0)
    MoveCamera(50, 17, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(24000, 0)
    SetChrPos(0x101, 63100, 0, 6700, 0)
    SetChrPos(0x102, 64400, 0, 6700, 0)
    SetChrPos(0x109, 62700, 0, 5300, 0)
    SetChrPos(0x104, 64000, 0, 5300, 0)
    SetChrPos(0x105, 65099, 0, 4900, 0)
    SetChrPos(0x10A, 65099, 0, 8600, 225)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 64000, 150, 11400, 180)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0229
    AnonymousTalk(
        0x8,
        (
            "#01001F原来如此，以两国首脑\x01",
            "为目标的恐怖分子啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetCameraDistance(23000, 2000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x10)

    #C0230
    ChrTalk(
        0x10A,
        (
            "#00606F#5P唔，本来只是觉得有这个可能性而已，\x01",
            "但竟会具体到这种程度……\x02\x03",

            "#00610F帝国和共和国\x01",
            "到底在想什么……！？\x02",
        )
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0x8,
        (
            "#1P#01003F他们自然有什么\x01",
            "重要的目的吧。\x02\x03",

            "#01000F我们最好也向市长\x01",
            "和警备队那边通报一下。\x02",
        )
    )

    CloseMessageWindow()

    #C0232
    ChrTalk(
        0x10A,
        (
            "#00603F#5P嗯，这件事情就交给我吧。\x02\x03",

            "#00601F话说回来，\x01",
            "刚听说你们登上了『埃尔赛尤号』的时候，\x01",
            "我甚至都不敢相信自己的耳朵。\x02\x03",

            "而且竟然能从两位首脑级人士\x01",
            "的口中得到这些消息……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_612A():
        TurnDirection(0x101, 0x10A, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_612A)
    Sleep(100)

    def lambda_613A():
        TurnDirection(0x109, 0x10A, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_613A)
    Sleep(100)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x109, 0)

    #C0233
    ChrTalk(
        0x101,
        (
            "#6P#00012F哈哈，一科果然已经\x01",
            "知道了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0234
    ChrTalk(
        0x104,
        (
            "#12P#00302F因为事情比较突然，\x01",
            "所以我们不想太过张扬。\x02",
        )
    )

    CloseMessageWindow()

    #C0235
    ChrTalk(
        0x10A,
        (
            "#00607F#5P这叫什么话！别管突然不突然，\x01",
            "在这种时候，应该先找上级商量，\x01",
            "然后再决定是否接受招待……！\x02",
        )
    )

    CloseMessageWindow()

    #C0236
    ChrTalk(
        0x8,
        (
            "#1P#01004F呵呵，这些家伙又怎会\x01",
            "如此循规蹈矩。\x02\x03",

            "#01002F况且对方也是不拘常理之辈，\x01",
            "这样做，说不定正是最佳选择呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0237
    ChrTalk(
        0x10A,
        "#00606F#5P唔……\x02",
    )

    CloseMessageWindow()

    #C0238
    ChrTalk(
        0x104,
        (
            "#12P#00309F哈～话说回来，的确是\x01",
            "与众不同的公主和皇子呢。\x02\x03",

            "#00300F特别是奥利维特皇子，\x01",
            "没想到竟是那样的怪人啊。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_6320():
        TurnDirection(0x102, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_6320)
    Sleep(100)

    def lambda_6330():
        TurnDirection(0x101, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_6330)
    Sleep(100)

    def lambda_6340():
        TurnDirection(0x105, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_6340)
    Sleep(100)

    def lambda_6350():
        TurnDirection(0x109, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_6350)
    Sleep(100)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x109, 0)

    #C0239
    ChrTalk(
        0x102,
        (
            "#5P#00106F兰迪，你太失礼了。\x02\x03",

            "#00100F不过，该说是不拘小节吗……\x01",
            "他的确是个很随意的人呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0240
    ChrTalk(
        0x101,
        (
            "#5P#00004F不过，我认为他也是个\x01",
            "很有想法的人。\x02\x03",

            "#00000F那个担任护卫的少校，\x01",
            "看起来也有着相当强的实力。\x02",
        )
    )

    CloseMessageWindow()

    #C0241
    ChrTalk(
        0x109,
        (
            "#6P#10102F另外，科洛蒂娅公主\x01",
            "和尤莉亚准校真是太美了……！\x02\x03",

            "#10112F公主殿下虽然直爽随和，但气质高贵，\x01",
            "尤莉亚准校也是英姿飒爽……！\x02",
        )
    )

    CloseMessageWindow()

    #C0242
    ChrTalk(
        0x105,
        (
            "#10302F#11P呵呵，你好像已经要到了签名，\x01",
            "而且还连同妹妹的份一起吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0243
    ChrTalk(
        0x109,
        "#6P#10111F你、你怎么会知道……\x02",
    )

    CloseMessageWindow()

    #C0244
    ChrTalk(
        0x10A,
        (
            "#00606F#5P……真是的。\x02\x03",

            "#00600F算了，能得知恐怖分子的存在，\x01",
            "你们此行便算是有所收获了。\x02\x03",

            "看来应该再调整一下\x01",
            "明天的警备安排啊……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_65B1():
        TurnDirection(0x101, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_65B1)
    Sleep(100)

    def lambda_65C1():
        TurnDirection(0x102, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_65C1)
    Sleep(100)

    def lambda_65D1():
        TurnDirection(0x105, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_65D1)
    Sleep(100)

    def lambda_65E1():
        TurnDirection(0x109, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_65E1)
    Sleep(100)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x109, 0)

    #C0245
    ChrTalk(
        0x101,
        (
            "#6P#00001F最关键的还是明天……\x01",
            "也就是『通商会议』的正式会议吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0246
    ChrTalk(
        0x8,
        (
            "#1P#01003F嗯，后天下午，\x01",
            "各国首脑就要回国了……\x02\x03",

            "#01001F如果会出什么事情的话，\x01",
            "发生在明天的可能性恐怕很高。\x02",
        )
    )

    CloseMessageWindow()

    #C0247
    ChrTalk(
        0x102,
        (
            "#00101F会议……\x01",
            "是从白天开始吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0248
    ChrTalk(
        0x10A,
        (
            "#00600F#5P嗯，下午一点开始，\x01",
            "在兰花塔三十五层的\x01",
            "『国际会议场』召开。\x02\x03",

            "中途将会休息一次，\x01",
            "会议预计持续到傍晚结束。\x02",
        )
    )

    CloseMessageWindow()

    #C0249
    ChrTalk(
        0x104,
        (
            "#12P#00305F也就是说，只要能在会议\x01",
            "召开期间保护好首脑们就可以了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0250
    ChrTalk(
        0x10A,
        (
            "#00604F#5P不，在兰花塔内部已经\x01",
            "安排了万全的警备体制。\x02\x03",

            "大楼本身也拥有安全系统，\x01",
            "在会议召开期间反而是最安全的。\x02",
        )
    )

    CloseMessageWindow()

    #C0251
    ChrTalk(
        0x8,
        (
            "#1P#01003F另外，亚里欧斯\x01",
            "也会参与会场警备工作。\x02\x03",

            "#01002F而且他还会以游击士协会代表的身份\x01",
            "出现在通商会议的会场，\x01",
            "完全可以放心。\x02",
        )
    )

    CloseMessageWindow()

    #C0252
    ChrTalk(
        0x102,
        "#00102F是这样啊……\x02",
    )

    CloseMessageWindow()

    #C0253
    ChrTalk(
        0x109,
        (
            "#12P#10108F也就是说，会议前后\x01",
            "才是最危险的时期吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0254
    ChrTalk(
        0x105,
        (
            "#10304F#12P比如说，在首脑们从兰花塔出来的时候，\x01",
            "从远处发动狙击之类的。\x02",
        )
    )

    CloseMessageWindow()

    #C0255
    ChrTalk(
        0x101,
        (
            "#6P#00006F老实说，那的确是\x01",
            "最让人担心的情况啊……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(103, 0, 100, 0)
    Sleep(300)
    OP_C9(0x0, 0x80000000)
    SetChrChipByIndex(0xA, 0x2)
    SetChrSubChip(0xA, 0x0)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)
    SetChrPos(0xA, 59000, -3000, 3300, 90)
    OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    #Sound(3609, 255, 70, 0)    #voice#KeA

    #N0256
    NpcTalk(
        0xA,
        "琪雅的声音",
        "#11P#13A罗伊德，罗伊德。\x02",
    )
    #Auto

    CloseMessageWindow()
    OP_68(64000, 1000, 6300, 2000)
    MoveCamera(62, 15, 0, 2000)
    OP_6E(400, 2000)
    SetCameraDistance(24000, 2000)
    OP_5A()
    SetChrPos(0xA, 61500, 0, 3800, 90)

    def lambda_6A17():
        TurnDirection(0x109, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_6A17)
    Sleep(50)

    def lambda_6A27():
        TurnDirection(0x102, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_6A27)
    Sleep(50)

    def lambda_6A37():
        TurnDirection(0x104, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_6A37)
    Sleep(50)

    def lambda_6A47():
        TurnDirection(0x105, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_6A47)
    Sleep(50)

    def lambda_6A57():
        TurnDirection(0x101, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_6A57)
    Sleep(50)

    def lambda_6A67():
        TurnDirection(0x10A, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x10A, 0, lambda_6A67)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x10A, 0)
    SetChrChipByIndex(0xA, 0x2)
    SetChrSubChip(0xA, 0x0)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)
    SetChrPos(0xA, 59000, 0, 3300, 90)
    OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_6ABA():
        OP_96(0xFE, 0xEE48, 0x0, 0xCE4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_6ABA)

    def lambda_6AD4():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_6AD4)
    WaitChrThread(0xA, 1)

    def lambda_6AE9():
        OP_95(0xFE, 61500, 0, 3800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_6AE9)
    WaitChrThread(0xA, 1)
    TurnDirection(0xA, 0x10A, 500)
    OP_6F(0x79)
    OP_63(0xA, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_C9(0x0, 0x80000000)

    #C0257
    ChrTalk(
        0xA,
        "#12P#01105F#3610V#30W啊，是板着脸的叔叔！\x02",
    )

    CloseMessageWindow()
    OP_24(0xE1A)
    OP_C9(0x1, 0x80000000)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x10A, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1200)

    #C0258
    ChrTalk(
        0x10A,
        (
            "#5P#00603F……还是和以前一样\x01",
            "不懂礼貌啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0259
    ChrTalk(
        0x101,
        "#5P#00011F对、对不起。\x02",
    )

    CloseMessageWindow()

    #C0260
    ChrTalk(
        0x102,
        (
            "#00112F#5P琪雅，这是\x01",
            "达德利警官……\x02",
        )
    )

    CloseMessageWindow()

    #C0261
    ChrTalk(
        0xA,
        (
            "#12P#01109F嗯，达德利！\x02\x03",

            "#01110F好久不见啦，\x01",
            "你身体还好吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0262
    ChrTalk(
        0x10A,
        (
            "#5P#00604F呵，身为一科的搜查官，\x01",
            "自然要随时保持最佳的身体状况。\x02\x03",

            "#00607F……不对！\x01",
            "你怎么可以直呼我的名字！\x02",
        )
    )

    CloseMessageWindow()

    #C0263
    ChrTalk(
        0xA,
        (
            "#12P#01106F哎？不行吗？\x02\x03",

            "#01111F那……达德利叔叔？\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0264
    ChrTalk(
        0x10A,
        "#5P#00610F谁是叔叔啊！\x02",
    )

    CloseMessageWindow()

    #C0265
    ChrTalk(
        0x109,
        "#5P#10112F哈，算了算了。\x02",
    )

    CloseMessageWindow()

    #C0266
    ChrTalk(
        0x104,
        (
            "#5P#00309F哈哈，对小孩子来说，\x01",
            "你已经是个十足的大叔啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0267
    ChrTalk(
        0x105,
        (
            "#10302F#11P对了，琪雅，\x01",
            "有什么事吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0268
    ChrTalk(
        0xA,
        (
            "#12P#01106F啊，对了。\x02\x03",

            "#01100F那个……有通讯联络哦，\x01",
            "是找你们的。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0269
    ChrTalk(
        0x101,
        "#00005F#5P通讯联络？\x02",
    )

    CloseMessageWindow()

    #C0270
    ChrTalk(
        0x102,
        (
            "#00105F#5P哎，但通讯器的铃声\x01",
            "好像并没响呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0271
    ChrTalk(
        0xA,
        (
            "#12P#01109F啊，不是普通的通讯器，\x01",
            "是能看到脸的那个。\x02",
        )
    )

    CloseMessageWindow()

    #C0272
    ChrTalk(
        0x101,
        (
            "#00011F#5P是终端吗……\x01",
            "琪雅，你竟然还会操作那个啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0273
    ChrTalk(
        0x104,
        (
            "#00305F#5P这么说，是阿缇吧？\x01",
            "看来是到了她的晚间联络时间啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0274
    ChrTalk(
        0xA,
        (
            "#12P#01104F不，是那个脸上有雀斑的人。\x02\x03",

            "#01100F不知道为什么，他的脸色\x01",
            "红一阵青一阵的。\x02",
        )
    )

    CloseMessageWindow()
    OP_68(63000, 1000, 6300, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    Sleep(1000)
    OP_68(17800, 1750, 10700, 0)
    MoveCamera(13, 20, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(23500, 0)
    SetChrPos(0x101, 16300, 850, 10200, 45)
    SetChrPos(0x102, 15250, 850, 8300, 45)
    SetChrPos(0x104, 14600, 850, 9400, 45)
    SetChrPos(0x109, 16200, 850, 7400, 0)
    SetChrPos(0x105, 17200, 850, 7800, 0)
    SetChrPos(0x10A, 14100, 850, 11900, 135)
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    SetChrPos(0x8, 13000, 850, 10400, 90)
    SetChrPos(0xA, 13300, 850, 9300, 90)
    OP_68(16800, 1750, 10700, 2000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)
    Sleep(500)
    Sound(72, 0, 100, 0)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x2, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x2, 0x3)
    Sleep(300)
    BeginChrThread(0x101, 3, 0, 21)
    SetMessageWindowPos(-1, 150, -1, -1)
    SetChrName("约纳的声音")

    #A0275
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#4S慢死了！\x02\x03",

            "#3S真是的，\x01",
            "要让我等多久啊！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    WaitChrThread(0x101, 3)
    SetMessageWindowPos(14, 280, 60, 3)

    #A0276
    AnonymousTalk(
        0x101,
        (
            "#00012F哈哈，抱歉。\x02\x03",

            "#00002F话说回来，真是好久不见了，\x01",
            "你最近还好——\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    OP_CB(0x2, 0x8, 0x300, 0x0, 0x400, 0x100)
    OP_0D()
    SetMessageWindowPos(-1, 150, -1, -1)
    SetChrName("约纳的声音")

    #A0277
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "啊啊，好啦！\x01",
            "不用说这种客套话了！\x02\x03",

            "我有十万火急的事情\x01",
            "要找你们帮忙！\x02\x03",

            "现在可以马上去\x01",
            "我的基地看看吗！？\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    #A0278
    AnonymousTalk(
        0x101,
        "#00011F哎……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0279
    AnonymousTalk(
        0x102,
        (
            "#00105F基地……\x01",
            "就是你当时暂住的那个……？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    OP_CB(0x2, 0x8, 0x200, 0x0, 0x300, 0x100)
    OP_0D()
    SetMessageWindowPos(-1, 150, -1, -1)
    SetChrName("约纳的声音")

    #A0280
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "嗯，就是地下空间Ｂ区域的\x01",
            "第八控制终端所在的地方！\x02\x03",

            "在昨天到今天之间，\x01",
            "有人擅自使用了\x01",
            "那里的终端！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    #A0281
    AnonymousTalk(
        0x101,
        "#00001F擅自使用……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0282
    AnonymousTalk(
        0x109,
        (
            "#10105F你为什么\x01",
            "会知道呢？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0283
    AnonymousTalk(
        0x104,
        (
            "#00301F喂，阿约，\x01",
            "说到擅自使用，\x01",
            "你自己不也是一样嘛。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    OP_CB(0x2, 0x8, 0x300, 0x0, 0x400, 0x100)
    OP_0D()
    SetMessageWindowPos(-1, 150, -1, -1)
    SetChrName("约纳的声音")

    #A0284
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "先、先别说这些了！\x02\x03",

            "我离开的时候，给终端\x01",
            "设置了强力的加密程序。\x02\x03",

            "万一加密程序被破，\x01",
            "在进行导力网络的远程连接实验时\x01",
            "就会有警报发送过来……\x02\x03",

            "我今天就收到了警报！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    #A0285
    AnonymousTalk(
        0x101,
        "#00013F这……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0286
    AnonymousTalk(
        0x105,
        (
            "#10303F……有人破解了\x01",
            "你设有加密程序的终端。\x02\x03",

            "#10301F就是这么回事吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    OP_CB(0x2, 0x8, 0x0, 0x100, 0x100, 0x200)
    OP_0D()
    SetMessageWindowPos(-1, 150, -1, -1)
    SetChrName("约纳的声音")

    #A0287
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "嗯，就是这样！\x01",
            "肯定是个技术相当高超的黑客！\x02\x03",

            "总之，我希望你们赶快抓到犯人，\x01",
            "别让他再碰第二次！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    #A0288
    AnonymousTalk(
        0x104,
        (
            "#00306F真是的，自己做的坏事完全不提，\x01",
            "还说得这么理直气壮。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0289
    AnonymousTalk(
        0x102,
        (
            "#00108F不过，技术相当高超的黑客吗……\x01",
            "真是让人有点担心呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0290
    AnonymousTalk(
        0x101,
        (
            "#00003F嗯，玲应该已经回去了，\x01",
            "也不可能是罗伯兹主任。\x02\x03",

            "#00001F总之，我们这就过去看看，\x01",
            "稍后再和你联络。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    OP_CB(0x2, 0x8, 0x200, 0x0, 0x300, 0x100)
    OP_0D()
    SetMessageWindowPos(-1, 150, -1, -1)
    SetChrName("约纳的声音")

    #A0291
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "嗯！拜托了！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sound(1021, 0, 50, 0)
    Sound(939, 0, 50, 0)
    OP_CB(0x2, 0x0, 0x0, 0x17700, 0xFA, 0x0)
    OP_CB(0x2, 0x1, 0x3E8, 0x0, 0xFA, 0x0)
    OP_CB(0x2, 0x3, 0xFFFFFF, 0xFA, 0x0, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    Sleep(500)
    OP_24(0x3AB)
    OP_68(16300, 1750, 10200, 0)
    MoveCamera(13, 20, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(23500, 0)
    Sound(73, 0, 100, 0)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(300)

    #C0292
    ChrTalk(
        0x8,
        "#01000F#5P怎么？要去吗？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x8, 500)
    Sleep(300)

    #C0293
    ChrTalk(
        0x101,
        (
            "#11P#00003F嗯，谨慎起见，还是去看看吧。\x02\x03",

            "#00000F如果不行的话，\x01",
            "我一个人过去也可以。\x02",
        )
    )

    CloseMessageWindow()

    #C0294
    ChrTalk(
        0x104,
        "#6P#00301F喂喂，别乱说啊。\x02",
    )

    CloseMessageWindow()

    #C0295
    ChrTalk(
        0x102,
        (
            "#6P#00103F是啊……\x01",
            "出现在那里的人\x01",
            "未必就只有黑客。\x02",
        )
    )

    CloseMessageWindow()

    #C0296
    ChrTalk(
        0x109,
        "#12P#10101F我也一起去！\x02",
    )

    CloseMessageWindow()
    OP_68(15300, 1750, 10700, 2000)
    OP_63(0x10A, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x10A)
    OP_6F(0x79)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(300)
    OP_C9(0x0, 0x80000000)

    #A0297
    AnonymousTalk(
        0x10A,
        (
            "#3452V#30W……慢着。\x02\x03",

            "#4106V我也一起去。\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0x100A)
    OP_C9(0x1, 0x80000000)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_7A2C():
        TurnDirection(0x101, 0x10A, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_7A2C)
    Sleep(50)

    def lambda_7A3C():
        TurnDirection(0x104, 0x10A, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_7A3C)
    Sleep(50)

    def lambda_7A4C():
        TurnDirection(0x109, 0x10A, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_7A4C)
    Sleep(50)

    def lambda_7A5C():
        TurnDirection(0x105, 0x10A, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_7A5C)
    Sleep(50)

    def lambda_7A6C():
        TurnDirection(0x102, 0x10A, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_7A6C)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x102, 0)

    #C0298
    ChrTalk(
        0x101,
        "#11P#00005F哎……\x02",
    )

    CloseMessageWindow()

    #C0299
    ChrTalk(
        0x105,
        "#12P#10302F嘿，这是吹的什么风啊？\x02",
    )

    CloseMessageWindow()

    #C0300
    ChrTalk(
        0x10A,
        (
            "#00603F#5P哼，在通商会议开始之前，\x01",
            "要尽可能地掌握一切\x01",
            "不安定要素，仅此而已。\x02\x03",

            "#00601F时间宝贵，赶快出发吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0301
    ChrTalk(
        0x101,
        "#11P#00011F明、明白了。\x02",
    )

    CloseMessageWindow()

    #C0302
    ChrTalk(
        0x105,
        (
            "#12P#10304F呵呵，那我们就稍微\x01",
            "做个饭后运动吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x102, 0x10E, 0x1F4)
    Sleep(100)

    #C0303
    ChrTalk(
        0x102,
        (
            "#12P#00100F科长，小琪雅，\x01",
            "我们这就出发了。\x02",
        )
    )

    CloseMessageWindow()

    #C0304
    ChrTalk(
        0x8,
        "#01002F#5P嗯，小心点。\x02",
    )

    CloseMessageWindow()

    #C0305
    ChrTalk(
        0xA,
        "#6P#01109F一路小心。\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(24000, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    Sound(814, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0306
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "达德利搜查官加入队伍。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #A0307
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "在主菜单的[TACTICS]选项中\x01",
            "可以将其设置为参战队员。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_32(0x9, 0x0, 0x42)
    OP_32(0x9, 0x5, 0xC8)
    OP_42(0x9, 0x466, 0xFF)
    OP_42(0x9, 0x5E1, 0xFF)
    OP_42(0x9, 0x645, 0xFF)
    OP_42(0x9, 0x4E, 0x3)
    OP_42(0x9, 0x49, 0x4)
    OP_38(0x9, 0x80, 0x2)
    OP_38(0x9, 0x81, 0x1)
    OP_38(0x9, 0x82, 0x2)
    OP_38(0x9, 0x83, 0x2)
    OP_38(0x9, 0x84, 0x1)
    OP_38(0x9, 0x85, 0x1)
    OP_38(0x9, 0x86, 0x1)
    OP_42(0x9, 0x6D, 0x1)
    OP_42(0x9, 0xAE, 0x2)
    OP_42(0x9, 0xB8, 0x3)
    OP_42(0x9, 0x8D, 0x4)
    OP_42(0x9, 0x84, 0x5)
    OP_42(0x9, 0x7D, 0x6)
    AddCraft(0x9, 0x179)
    OP_CC(0x1, 0xFF, 0x0)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 14400, 850, 12500, 0)
    BeginChrThread(0x8, 0, 0, 0)
    ClearChrFlags(0x8, 0x40)
    ClearChrFlags(0xA, 0x80)
    SetChrChipByIndex(0xA, 0x3)
    SetChrSubChip(0xA, 0x0)
    EndChrThread(0xA, 0x0)
    SetChrBattleFlags(0xA, 0x4)
    SetChrPos(0xA, 5570, 150, 6230, 180)
    ClearChrFlags(0x9, 0x80)
    SetChrChipByIndex(0x9, 0x5)
    SetChrPos(0x9, 2880, 0, 1750, 225)
    SetChrFlags(0x9, 0x10)
    ClearChrFlags(0x9, 0x40)
    SetChrPos(0x0, 8790, 850, 10000, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetScenarioFlags(0x141, 0)
    OP_29(0xA3, 0x1, 0x12)
    OP_29(0xA3, 0x1, 0x13)
    ReplaceBGM("ed7150", "ed7513")
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_20_5DD7 end

    def Function_21_7D9A(): pass

    label("Function_21_7D9A")

    OP_CB(0x2, 0x0, 0x4B0, 0xFFFFFBB4, 0x1, 0x0)
    Sleep(1)
    OP_CB(0x2, 0x0, 0xFFFFFAEC, 0x4B0, 0x1, 0x0)
    Sleep(1)
    OP_CB(0x2, 0x0, 0xFFFFFC18, 0xFFFFFA24, 0x1, 0x0)
    Sleep(1)
    OP_CB(0x2, 0x0, 0x640, 0xFFFFFB50, 0x1, 0x0)
    Sleep(1)
    OP_CB(0x2, 0x0, 0x0, 0x0, 0x1, 0x0)
    OP_CC(0x0, 0xFF, 0x0)
    Return()

    # Function_21_7D9A end

    def Function_22_7E0A(): pass

    label("Function_22_7E0A")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00900.itc", 0x1E)
    LoadChrToIndex("apl/ch50380.itc", 0x1F)
    LoadChrToIndex("apl/ch51225.itc", 0x20)
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis416.itp")
    OP_68(700, 1100, 4100, 0)
    MoveCamera(53, 19, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(23000, 0)
    SetChrPos(0x101, 500, 0, 2100, 0)
    SetChrPos(0x102, -1500, 0, 1400, 45)
    SetChrPos(0x109, -2200, 0, 2200, 45)
    SetChrPos(0x105, -1900, 0, 3400, 90)
    SetChrPos(0x104, 900, 0, 900, 0)
    SetChrPos(0x103, 700, 0, 3600, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    SetChrPos(0x8, 2700, 0, 5200, 225)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    OP_4B(0x8, 0xFF)
    SetChrChipByIndex(0xA, 0x1F)
    SetChrSubChip(0xA, 0x0)
    SetChrPos(0xA, 700, 0, 4100, 180)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)
    SetChrChipByIndex(0x9, 0x6)
    SetChrSubChip(0x9, 0x0)
    SetChrPos(0x9, -900, 0, 5300, 135)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    SetChrChipByIndex(0xC, 0x1E)
    SetChrSubChip(0xC, 0x0)
    SetChrPos(0xC, 2200, 0, 2400, 315)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8000)
    SetCameraDistance(24000, 2000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)

    #C0308
    ChrTalk(
        0xA,
        (
            "#01109F嘿嘿嘿，是缇欧！\x02\x03",

            "#01110F蔡特蔡特！\x01",
            "缇欧回来了！\x02",
        )
    )

    CloseMessageWindow()

    #C0309
    ChrTalk(
        0x9,
        "#01200F#5P嗷。\x02",
    )

    CloseMessageWindow()

    #C0310
    ChrTalk(
        0x103,
        (
            "#12P#00202F我回来啦，\x01",
            "琪雅，蔡特。\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0xA, 0x2)
    SetChrSubChip(0xA, 0x0)

    def lambda_8027():
        OP_96(0xFE, 0x2BC, 0x0, 0x1194, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_8027)
    WaitChrThread(0xA, 1)
    TurnDirection(0x103, 0x8, 500)
    Sleep(300)

    #C0311
    ChrTalk(
        0x103,
        (
            "#6P#00204F赛尔盖科长，\x01",
            "我回来了。\x02",
        )
    )

    CloseMessageWindow()

    #C0312
    ChrTalk(
        0x8,
        (
            "#5P#01004F嗯，欢迎回来。\x02\x03",

            "#01002F呵呵，听说你突然赶到，\x01",
            "解救了陷入危机的同伴啊？\x02",
        )
    )

    CloseMessageWindow()

    #C0313
    ChrTalk(
        0x101,
        "#12P#00004F嗯，真是救了我们呢。\x02",
    )

    CloseMessageWindow()

    #C0314
    ChrTalk(
        0x102,
        (
            "#12P#00106F当时要是没有缇欧\x01",
            "及时赶到，\x01",
            "后果恐怕就……\x02",
        )
    )

    CloseMessageWindow()

    #C0315
    ChrTalk(
        0x109,
        "#6P#10112F嗯嗯，现在想想都觉得后怕呢。\x02",
    )

    CloseMessageWindow()

    #C0316
    ChrTalk(
        0xC,
        (
            "#00604F……这次真是不得不\x01",
            "向你表示感谢了。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)
    TurnDirection(0x103, 0x101, 500)

    #C0317
    ChrTalk(
        0x103,
        "#5P#00205F那个……没什么大不了的事。\x02",
    )

    CloseMessageWindow()

    #C0318
    ChrTalk(
        0x104,
        "#12P#00309F哈哈，别害羞嘛。\x02",
    )

    CloseMessageWindow()

    #C0319
    ChrTalk(
        0x105,
        (
            "#6P#10304F你确实回来得\x01",
            "正是时候呢。\x02\x03",

            "#10300F被那种黑客缠上，\x01",
            "光凭我们几个，实在是束手无策啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0320
    ChrTalk(
        0x101,
        "#12P#00006F是啊……\x02",
    )

    CloseMessageWindow()
    OP_68(1300, 1100, 2800, 2000)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    OP_93(0x101, 0x2D, 0x1F4)
    OP_6F(0x79)
    Sleep(300)

    #C0321
    ChrTalk(
        0x101,
        (
            "#6P#00003F科长，达德利警官。\x02\x03",

            "#00001F明天的通商会议……\x01",
            "能否让我们也参加\x01",
            "兰花塔的警备工作？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_8388():
        TurnDirection(0xC, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xC, 0, lambda_8388)
    Sleep(50)

    def lambda_8398():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_8398)
    Sleep(50)

    def lambda_83A8():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_83A8)
    Sleep(50)

    def lambda_83B8():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_83B8)
    Sleep(50)

    def lambda_83C8():
        TurnDirection(0x8, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_83C8)
    Sleep(50)
    WaitChrThread(0xC, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x8, 0)

    #C0322
    ChrTalk(
        0x102,
        "#6P#00105F罗伊德，这……\x02",
    )

    CloseMessageWindow()

    #C0323
    ChrTalk(
        0x104,
        (
            "#12P#00305F喂喂，\x01",
            "你怎么突然说这些？\x02",
        )
    )

    CloseMessageWindow()

    #C0324
    ChrTalk(
        0x8,
        "#5P#01000F唔……\x02",
    )

    CloseMessageWindow()

    #C0325
    ChrTalk(
        0xC,
        (
            "#00600F#11P……我不是说过吗，\x01",
            "会场已经有了万全的警备体制。\x02",
        )
    )

    CloseMessageWindow()

    #C0326
    ChrTalk(
        0x101,
        (
            "#6P#00006F可是，今天那个黑客\x01",
            "不知从什么地方得到了\x01",
            "类似兰花塔构造图的东西。\x02\x03",

            "#00008F虽然并不能尽信『银』所说的话，\x01",
            "但那个黑客的确有可能会展开某些行动——\x02\x03",

            "#00001F不对……倒不如说，他把情报\x01",
            "交送给他人的可能性更高。\x02",
        )
    )

    CloseMessageWindow()

    #C0327
    ChrTalk(
        0x109,
        "#6P#10101F他人吗……\x02",
    )

    CloseMessageWindow()

    #C0328
    ChrTalk(
        0x105,
        "#6P#10301F嗯，那会是谁呢？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x109, 500)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 3)

    label("loc_85AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_86E4")
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    #A0329
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1K神秘黑客会把情报交给何方？\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "『黑月』\x01",          # 0
            "『赤色星座』\x01",      # 1
            " 其它势力\x01",         # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_864C"),
        (1, "loc_864C"),
        (2, "loc_86C3"),
        (SWITCH_DEFAULT, "loc_86DF"),
    )


    label("loc_864C")


    #C0330
    ChrTalk(
        0x101,
        (
            "#11P#00006F（不……比起他们，\x01",
            "  有个势力更希望得到它。）\x02\x03",

            "#00001F（那就是……）\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_86BE")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_86BE")

    Jump("loc_86DF")

    label("loc_86C3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_86D7")
    OP_2C(0xA3, 0x1)

    label("loc_86D7")

    SetScenarioFlags(0x0, 3)
    Jump("loc_86DF")

    label("loc_86DF")

    Jump("loc_85AD")

    label("loc_86E4")


    #C0331
    ChrTalk(
        0x101,
        (
            "#11P#00003F『赤色星座』或『黑月』，\x01",
            "还有帝国政府或共和国政府……\x02\x03",

            "虽然都具备一定的可能性，但从实际角度来考虑，\x01",
            "还是交给另一股势力的可能性更高。那股势力是……\x02\x03",

            "#00013F帝国与共和国的恐怖分子。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0332
    ChrTalk(
        0x102,
        (
            "#6P#00101F就是科洛蒂娅殿下\x01",
            "和奥利维特皇子所说的……\x02",
        )
    )

    CloseMessageWindow()

    #C0333
    ChrTalk(
        0x104,
        (
            "#12P#00301F企图狙击本国首脑的\x01",
            "两个恐怖组织吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0334
    ChrTalk(
        0x109,
        (
            "#6P#10108F确实，如果他们能得到大楼的构造图，\x01",
            "恐怕就可以寻找到防范死角了……\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x2D, 0x1F4)
    Sleep(300)

    #C0335
    ChrTalk(
        0x101,
        (
            "#6P#00006F当然，这也有可能是\x01",
            "混淆视听的假情报……\x02\x03",

            "#00001F但兰花塔明天\x01",
            "发生某些意外状况\x01",
            "的可能性实在是很高。\x02\x03",

            "哪怕只是在兰花塔周围警备也好，\x01",
            "可以让我们也参加吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0336
    ChrTalk(
        0x8,
        (
            "#5P#01004F呵呵，原来如此。\x02\x03",

            "#01002F达德利，如何？\x02",
        )
    )

    CloseMessageWindow()

    #C0337
    ChrTalk(
        0xC,
        (
            "#00606F#11P呼……\x01",
            "也罢，那就这样吧。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    SetChrFlags(0xC, 0x20)
    SetChrFlags(0xC, 0x2)
    SetChrChipByIndex(0xC, 0x20)
    SetChrSubChip(0xC, 0x0)
    Sleep(100)
    SetChrSubChip(0xC, 0x1)
    Sleep(100)
    SetChrSubChip(0xC, 0x2)
    Sleep(100)
    SetChrSubChip(0xC, 0x3)
    Sleep(100)
    SetChrSubChip(0xC, 0x4)
    Sleep(100)
    SetChrSubChip(0xC, 0x3)
    Sound(318, 0, 100, 0)
    Sleep(500)

    #C0338
    ChrTalk(
        0xC,
        (
            "#00611F#11P你们明日正午\x01",
            "来兰花塔一层。\x02\x03",

            "以后备警备员的身份\x01",
            "进入通商会议现场。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_8B2B():
        TurnDirection(0x101, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_8B2B)
    Sleep(50)

    def lambda_8B3B():
        TurnDirection(0x104, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_8B3B)
    Sleep(50)

    def lambda_8B4B():
        TurnDirection(0x103, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_8B4B)
    Sleep(50)

    def lambda_8B5B():
        TurnDirection(0x102, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_8B5B)
    Sleep(50)

    def lambda_8B6B():
        TurnDirection(0x109, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_8B6B)
    Sleep(50)

    def lambda_8B7B():
        TurnDirection(0x105, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_8B7B)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)

    #C0339
    ChrTalk(
        0x101,
        "#6P#00005F哎……\x02",
    )

    CloseMessageWindow()

    #C0340
    ChrTalk(
        0x104,
        "#12P#00305F哦，让我们进会场吗？\x02",
    )

    CloseMessageWindow()

    #C0341
    ChrTalk(
        0x105,
        (
            "#6P#10302F嘿……\x01",
            "这么大方吗？\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0xC, 0x1)
    Sleep(80)
    SetChrSubChip(0xC, 0x0)
    Sleep(80)
    ClearChrFlags(0xC, 0x20)
    ClearChrFlags(0xC, 0x2)
    SetChrChipByIndex(0xC, 0x1E)
    SetChrSubChip(0xC, 0x0)
    Sleep(300)

    #C0342
    ChrTalk(
        0xC,
        (
            "#00603F#11P不要搞错，\x01",
            "你们仅仅是后备人员而已。\x02\x03",

            "虽说只是偶然，但你们毕竟\x01",
            "曾在阻止暗杀市长事件中立下功劳，\x01",
            "而且又有熟悉导力网络的成员。\x02\x03",

            "#00601F为了预防万一，才会安排你们过去，\x01",
            "你们要搞清楚自己的立场。\x02",
        )
    )

    CloseMessageWindow()

    #C0343
    ChrTalk(
        0x101,
        "#6P#00000F明、明白了！\x02",
    )

    CloseMessageWindow()

    #C0344
    ChrTalk(
        0x109,
        "#6P#10102F谨遵吩咐！\x02",
    )

    CloseMessageWindow()

    #C0345
    ChrTalk(
        0x103,
        (
            "#5P#00204F不过，这态度果然只是一种\x01",
            "掩饰害羞的方式吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0346
    ChrTalk(
        0x104,
        (
            "#12P#00309F哈哈，他渐渐开始\x01",
            "怜爱起我们了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0347
    ChrTalk(
        0xA,
        "#01111F#5P怜爱～？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x102, 500)
    Sleep(150)

    #C0348
    ChrTalk(
        0xA,
        (
            "#01110F#5P艾莉艾莉，\x01",
            "怜爱是什么意思？\x02",
        )
    )

    CloseMessageWindow()

    #C0349
    ChrTalk(
        0x102,
        (
            "#6P#00109F嗯……这个嘛……\x01",
            "比如说，就像是大家和小琪雅\x01",
            "说话时的态度吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0350
    ChrTalk(
        0x105,
        (
            "#6P#10309F呵呵，照这样下去，\x01",
            "很快就会变成那样了呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0351
    ChrTalk(
        0xC,
        "#00610F#11P你、你们这些家伙……\x02",
    )

    CloseMessageWindow()

    #C0352
    ChrTalk(
        0x8,
        (
            "#5P#01004F呵呵，看样子，\x01",
            "明天恐怕要忙到死啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0353
    ChrTalk(
        0x9,
        "#01203F嗷。\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(24500, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    StopBGM(0xFA0)
    WaitBGM()
    Sleep(1000)
    Sound(13, 0, 100, 0)
    Sleep(4000)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    Sleep(2000)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x1, 0xFF, 0x0)
    OP_32(0xFF, 0xFE, 0x0)
    ReplaceBGM(-1, -1)
    ReplaceBGM("ed7150", "ed7125")
    ReplaceBGM("ed7101", "ed7125")
    SetScenarioFlags(0x22, 7)
    NewScene("c0100", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_22_7E0A end

    def Function_23_8F68(): pass

    label("Function_23_8F68")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch00102.itc", 0x1F)
    LoadChrToIndex("chr/ch00302.itc", 0x20)
    LoadChrToIndex("chr/ch02902.itc", 0x21)
    LoadChrToIndex("chr/ch03002.itc", 0x22)
    LoadChrToIndex("chr/ch00202.itc", 0x23)
    LoadChrToIndex("apl/ch50090.itc", 0x24)
    LoadChrToIndex("apl/ch50092.itc", 0x25)
    LoadChrToIndex("apl/ch51090.itc", 0x26)
    LoadEffect(0x0, "event/ev12002.eff")
    OP_68(12600, 2550, 4300, 0)
    MoveCamera(40, 19, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(22500, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x2)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x104, 0x20)
    SetChrSubChip(0x104, 0x2)
    SetChrChipByIndex(0x109, 0x21)
    SetChrSubChip(0x109, 0x1)
    SetChrChipByIndex(0x105, 0x22)
    SetChrSubChip(0x105, 0x2)
    SetChrChipByIndex(0x103, 0x23)
    SetChrSubChip(0x103, 0x1)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x104, 0x4)
    SetChrFlags(0x109, 0x4)
    SetChrFlags(0x105, 0x4)
    SetChrFlags(0x103, 0x4)
    SetChrPos(0x101, 13900, 900, 5400, 270)
    SetChrPos(0x102, 11300, 900, 7000, 90)
    SetChrPos(0x103, 11300, 900, 3800, 90)
    SetChrPos(0x104, 13900, 900, 3800, 270)
    SetChrPos(0x109, 11300, 900, 2200, 90)
    SetChrPos(0x105, 13900, 900, 2200, 270)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrChipByIndex(0xA, 0x3)
    SetChrSubChip(0xA, 0x0)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)
    SetChrPos(0xA, 11300, 900, 5400, 90)
    SetChrChipByIndex(0x9, 0x6)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, 16300, 850, 6400, 270)
    SetMapObjFrame(0xFF, "isu00", 0x0, 0x1)
    SetMapObjFrame(0xFF, "isu00_sd", 0x0, 0x1)
    ClearChrFlags(0x26, 0x80)
    OP_78(0xA, 0x26)
    ClearChrFlags(0x27, 0x80)
    OP_78(0xB, 0x27)
    ClearChrFlags(0x28, 0x80)
    OP_78(0xC, 0x28)
    ClearChrFlags(0x29, 0x80)
    OP_78(0xD, 0x29)
    ClearChrFlags(0x2A, 0x80)
    OP_78(0xE, 0x2A)
    ClearChrFlags(0x2B, 0x80)
    OP_78(0xF, 0x2B)
    ClearChrFlags(0x2C, 0x80)
    OP_78(0x1A, 0x2C)
    ClearChrFlags(0x2D, 0x80)
    OP_78(0x1B, 0x2D)
    OP_49()
    SetChrPos(0x26, 14000, 0, 7000, 0)
    OP_D5(0x26, 0x0, 0x41EB0, 0x0, 0x0)
    SetChrPos(0x27, 14000, 0, 5400, 0)
    OP_D5(0x27, 0x0, 0x41EB0, 0x0, 0x0)
    SetChrPos(0x28, 14000, 0, 3800, 0)
    OP_D5(0x28, 0x0, 0x41EB0, 0x0, 0x0)
    SetChrPos(0x29, 14000, 0, 2200, 0)
    OP_D5(0x29, 0x0, 0x41EB0, 0x0, 0x0)
    SetChrPos(0x2A, 11200, 0, 7000, 0)
    OP_D5(0x2A, 0x0, 0x15F90, 0x0, 0x0)
    SetChrPos(0x2B, 11200, 0, 5400, 0)
    OP_D5(0x2B, 0x0, 0x15F90, 0x0, 0x0)
    SetChrPos(0x2C, 11200, 0, 3800, 0)
    OP_D5(0x2C, 0x0, 0x15F90, 0x0, 0x0)
    SetChrPos(0x2D, 11200, 0, 2200, 0)
    OP_D5(0x2D, 0x0, 0x15F90, 0x0, 0x0)
    SetChrFlags(0x8, 0x80)
    SetChrChipByIndex(0x13, 0x26)
    SetChrSubChip(0x13, 0x5)
    SetChrFlags(0x13, 0x8000)
    SetChrPos(0x13, 13000, 1350, 7100, 0)
    ClearChrFlags(0x13, 0x80)
    ClearChrBattleFlags(0x13, 0x8000)
    SetChrChipByIndex(0x14, 0x24)
    SetChrSubChip(0x14, 0x14)
    SetChrFlags(0x14, 0x8000)
    SetChrPos(0x14, 13100, 1350, 6800, 0)
    ClearChrFlags(0x14, 0x80)
    ClearChrBattleFlags(0x14, 0x8000)
    SetChrChipByIndex(0x15, 0x26)
    SetChrSubChip(0x15, 0x5)
    SetChrFlags(0x15, 0x8000)
    SetChrPos(0x15, 12200, 1350, 7100, 0)
    ClearChrFlags(0x15, 0x80)
    ClearChrBattleFlags(0x15, 0x8000)
    SetChrChipByIndex(0x16, 0x24)
    SetChrSubChip(0x16, 0x11)
    SetChrFlags(0x16, 0x8000)
    SetChrPos(0x16, 12300, 1300, 6800, 0)
    ClearChrFlags(0x16, 0x80)
    ClearChrBattleFlags(0x16, 0x8000)
    SetChrChipByIndex(0x17, 0x26)
    SetChrSubChip(0x17, 0x5)
    SetChrFlags(0x17, 0x8000)
    SetChrPos(0x17, 13000, 1350, 5200, 0)
    ClearChrFlags(0x17, 0x80)
    ClearChrBattleFlags(0x17, 0x8000)
    SetChrChipByIndex(0x18, 0x24)
    SetChrSubChip(0x18, 0x14)
    SetChrFlags(0x18, 0x8000)
    SetChrPos(0x18, 13100, 1350, 4900, 0)
    ClearChrFlags(0x18, 0x80)
    ClearChrBattleFlags(0x18, 0x8000)
    SetChrChipByIndex(0x19, 0x26)
    SetChrSubChip(0x19, 0x5)
    SetChrFlags(0x19, 0x8000)
    SetChrPos(0x19, 12200, 1350, 5200, 0)
    ClearChrFlags(0x19, 0x80)
    ClearChrBattleFlags(0x19, 0x8000)
    SetChrChipByIndex(0x1A, 0x24)
    SetChrSubChip(0x1A, 0x11)
    SetChrFlags(0x1A, 0x8000)
    SetChrPos(0x1A, 12300, 1300, 4900, 0)
    ClearChrFlags(0x1A, 0x80)
    ClearChrBattleFlags(0x1A, 0x8000)
    SetChrChipByIndex(0x1B, 0x26)
    SetChrSubChip(0x1B, 0x5)
    SetChrFlags(0x1B, 0x8000)
    SetChrPos(0x1B, 13000, 1350, 3800, 0)
    ClearChrFlags(0x1B, 0x80)
    ClearChrBattleFlags(0x1B, 0x8000)
    SetChrChipByIndex(0x1C, 0x24)
    SetChrSubChip(0x1C, 0x14)
    SetChrFlags(0x1C, 0x8000)
    SetChrPos(0x1C, 13100, 1350, 3500, 0)
    ClearChrFlags(0x1C, 0x80)
    ClearChrBattleFlags(0x1C, 0x8000)
    SetChrChipByIndex(0x1D, 0x26)
    SetChrSubChip(0x1D, 0x5)
    SetChrFlags(0x1D, 0x8000)
    SetChrPos(0x1D, 13000, 1350, 2000, 0)
    ClearChrFlags(0x1D, 0x80)
    ClearChrBattleFlags(0x1D, 0x8000)
    SetChrChipByIndex(0x1E, 0x24)
    SetChrSubChip(0x1E, 0x14)
    SetChrFlags(0x1E, 0x8000)
    SetChrPos(0x1E, 13100, 1350, 1700, 0)
    ClearChrFlags(0x1E, 0x80)
    ClearChrBattleFlags(0x1E, 0x8000)
    SetChrChipByIndex(0x1F, 0x26)
    SetChrSubChip(0x1F, 0x5)
    SetChrFlags(0x1F, 0x8000)
    SetChrPos(0x1F, 12200, 1350, 2000, 0)
    ClearChrFlags(0x1F, 0x80)
    ClearChrBattleFlags(0x1F, 0x8000)
    SetChrChipByIndex(0x20, 0x24)
    SetChrSubChip(0x20, 0x11)
    SetChrFlags(0x20, 0x8000)
    SetChrPos(0x20, 12300, 1300, 1700, 0)
    ClearChrFlags(0x20, 0x80)
    ClearChrBattleFlags(0x20, 0x8000)
    SetChrChipByIndex(0x21, 0x26)
    SetChrSubChip(0x21, 0x5)
    SetChrFlags(0x21, 0x8000)
    SetChrPos(0x21, 12200, 1350, 3800, 0)
    ClearChrFlags(0x21, 0x80)
    ClearChrBattleFlags(0x21, 0x8000)
    SetChrChipByIndex(0x22, 0x24)
    SetChrSubChip(0x22, 0x11)
    SetChrFlags(0x22, 0x8000)
    SetChrPos(0x22, 12300, 1300, 3500, 0)
    ClearChrFlags(0x22, 0x80)
    ClearChrBattleFlags(0x22, 0x8000)
    SetChrChipByIndex(0x23, 0x25)
    SetChrSubChip(0x23, 0x0)
    SetChrFlags(0x23, 0x8000)
    SetChrPos(0x23, 16300, 750, 5500, 0)
    SetChrChipByIndex(0x24, 0x26)
    SetChrSubChip(0x24, 0x6)
    SetChrFlags(0x24, 0x8000)
    SetChrPos(0x24, 12650, 1450, 5900, 0)
    ClearChrFlags(0x24, 0x80)
    ClearChrBattleFlags(0x24, 0x8000)
    SetChrChipByIndex(0x25, 0x26)
    SetChrSubChip(0x25, 0x6)
    SetChrFlags(0x25, 0x8000)
    SetChrPos(0x25, 12650, 1450, 2750, 0)
    ClearChrFlags(0x25, 0x80)
    ClearChrBattleFlags(0x25, 0x8000)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 12650, 1550, 5900, 0, 0, 0, 2500, 2500, 2500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 12650, 1550, 2750, 0, 0, 0, 2500, 2500, 2500, 0xFF, 0, 0, 0, 0)
    OP_68(12600, 2050, 4300, 2000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x1)

    #C0354
    ChrTalk(
        0x101,
        (
            "#00008F#11P……科长好慢啊。\x02\x03",

            "#00006F不过毕竟发生了那样的事情，\x01",
            "这也难怪……\x02",
        )
    )

    CloseMessageWindow()

    #C0355
    ChrTalk(
        0x109,
        "#12P#10108F是啊……\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x102, 0x2)
    Sleep(300)

    #C0356
    ChrTalk(
        0x102,
        (
            "#5P#00106F……他现在大概\x01",
            "正在兰花塔探讨\x01",
            "接下来的对策吧。\x02\x03",

            "#00108F另外，政治方面的问题也非常棘手……\x02",
        )
    )

    CloseMessageWindow()

    #C0357
    ChrTalk(
        0x105,
        (
            "#10306F#11P瓦鲁多的情况也是一样……\x02\x03",

            "#10301F在困难时期，\x01",
            "竟然还发生了这样的事情啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0358
    ChrTalk(
        0xA,
        (
            "#6P#01106F……各位。\x02\x03",

            "#01112F如果科长不回来，\x01",
            "我们就不能吃火锅了吧？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x104, 0x0)
    Sleep(100)
    SetChrSubChip(0x101, 0x0)
    Sleep(200)

    #C0359
    ChrTalk(
        0x104,
        (
            "#00304F#11P……不，科长当时说过，\x01",
            "如果他回来得晚，我们先吃就行了。\x02\x03",

            "#00300F阿琪好不容易才做好，\x01",
            "我们就先来享用吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0360
    ChrTalk(
        0xA,
        "#6P#01108F可、可是……\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x103, 0x0)
    Sleep(100)
    SetChrSubChip(0x101, 0x1)
    Sleep(200)

    #C0361
    ChrTalk(
        0x103,
        "#6P#00208F兰迪前辈……\x02",
    )

    CloseMessageWindow()

    #C0362
    ChrTalk(
        0x101,
        (
            "#00006F#5P先不提火锅……\x01",
            "兰迪，你不是在硬撑吧？\x02\x03",

            "#00008F正是在这种时候，\x01",
            "才更要依靠我们大家……\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x104, 0x2)
    Sleep(300)

    #C0363
    ChrTalk(
        0x104,
        (
            "#00302F#11P哈哈，我当然会依靠你们。\x02\x03",

            "#00303F之前就说过……\x01",
            "我和叔叔他们之间已经毫无瓜葛了。\x02\x03",

            "事到如今，不管我的老巢做了什么，\x01",
            "我也不会因为他们而痛苦纠结。\x02\x03",

            "#00304F比起这些，现在更重要的还是\x01",
            "填饱肚子，充分休息……\x02\x03",

            "#00300F这样才能为明天做好准备吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0364
    ChrTalk(
        0x101,
        "#00005F#5P这……\x02",
    )

    CloseMessageWindow()

    #C0365
    ChrTalk(
        0x109,
        (
            "#6P#10112F说、说的对啊……！\x02\x03",

            "#10100F有句话说的好，\x01",
            "不填饱肚子就没法战斗！\x02",
        )
    )

    CloseMessageWindow()

    #C0366
    ChrTalk(
        0x102,
        (
            "#5P#00109F呵呵，兰迪这种坚韧的品性\x01",
            "总是很鼓舞我们呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0367
    ChrTalk(
        0x103,
        "#6P#00202F……是啊。\x02",
    )

    CloseMessageWindow()

    #C0368
    ChrTalk(
        0x105,
        (
            "#10304F#11P也对，今天在湖那边还\x01",
            "遇到了那些惊人的家伙，也够累人了。\x02\x03",

            "#10302F为了明天的工作，我们还是早点吃完，\x01",
            "然后好好休息吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0369
    ChrTalk(
        0x101,
        "#00004F#5P说的对……\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)
    Sleep(300)

    #C0370
    ChrTalk(
        0x101,
        (
            "#00002F#11P好，\x01",
            "那我们就开始吃火锅吧。\x02\x03",

            "#00004F琪雅为我们准备了\x01",
            "肉、鱼、蔬菜……很丰盛啊。\x02\x03",

            "#00000F多吃一些，早点休息……\x01",
            "为明天做好准备吧！\x02",
        )
    )

    CloseMessageWindow()

    #C0371
    ChrTalk(
        0x104,
        "#00309F#11P嗯嗯！\x02",
    )

    CloseMessageWindow()

    #C0372
    ChrTalk(
        0x109,
        "#12P#10109F我开动了！\x02",
    )

    CloseMessageWindow()

    #C0373
    ChrTalk(
        0x102,
        (
            "#5P#00102F琪雅，吃完之后由我们来洗餐具，\x01",
            "你要多吃一点哦。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xA, 0x1)
    Sleep(100)

    #C0374
    ChrTalk(
        0xA,
        "#6P#01109F……嗯！\x02",
    )

    CloseMessageWindow()

    #C0375
    ChrTalk(
        0x103,
        (
            "#6P#00202F蔡特，把鱼和肉\x01",
            "晾凉之后就给你。\x02",
        )
    )

    CloseMessageWindow()

    #C0376
    ChrTalk(
        0x9,
        "#01200F#11P咕呜呜呜……嗷。\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(23000, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    SetChrFlags(0x13, 0x80)
    SetChrBattleFlags(0x13, 0x8000)
    SetChrFlags(0x14, 0x80)
    SetChrBattleFlags(0x14, 0x8000)
    SetChrFlags(0x15, 0x80)
    SetChrBattleFlags(0x15, 0x8000)
    SetChrFlags(0x16, 0x80)
    SetChrBattleFlags(0x16, 0x8000)
    SetChrFlags(0x17, 0x80)
    SetChrBattleFlags(0x17, 0x8000)
    SetChrFlags(0x18, 0x80)
    SetChrBattleFlags(0x18, 0x8000)
    SetChrFlags(0x19, 0x80)
    SetChrBattleFlags(0x19, 0x8000)
    SetChrFlags(0x1A, 0x80)
    SetChrBattleFlags(0x1A, 0x8000)
    SetChrFlags(0x1B, 0x80)
    SetChrBattleFlags(0x1B, 0x8000)
    SetChrFlags(0x1C, 0x80)
    SetChrBattleFlags(0x1C, 0x8000)
    SetChrFlags(0x1D, 0x80)
    SetChrBattleFlags(0x1D, 0x8000)
    SetChrFlags(0x1E, 0x80)
    SetChrBattleFlags(0x1E, 0x8000)
    SetChrFlags(0x1F, 0x80)
    SetChrBattleFlags(0x1F, 0x8000)
    SetChrFlags(0x20, 0x80)
    SetChrBattleFlags(0x20, 0x8000)
    SetChrFlags(0x21, 0x80)
    SetChrBattleFlags(0x21, 0x8000)
    SetChrFlags(0x22, 0x80)
    SetChrBattleFlags(0x22, 0x8000)
    SetChrFlags(0x23, 0x80)
    SetChrBattleFlags(0x23, 0x8000)
    SetChrFlags(0x24, 0x80)
    SetChrBattleFlags(0x24, 0x8000)
    SetChrFlags(0x25, 0x80)
    SetChrBattleFlags(0x25, 0x8000)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x102, 0x4)
    ClearChrFlags(0x104, 0x4)
    ClearChrFlags(0x109, 0x4)
    ClearChrFlags(0x105, 0x4)
    ClearChrFlags(0x103, 0x4)
    SetChrFlags(0x26, 0x80)
    SetChrFlags(0x27, 0x80)
    SetChrFlags(0x28, 0x80)
    SetChrFlags(0x29, 0x80)
    SetChrFlags(0x2A, 0x80)
    SetChrFlags(0x2B, 0x80)
    SetChrFlags(0x2C, 0x80)
    SetChrFlags(0x2D, 0x80)
    SetChrPos(0x26, 22900, 0, 12700, 0)
    SetChrPos(0x27, 22900, 0, 12700, 0)
    SetChrPos(0x28, 22900, 0, 12700, 0)
    SetChrPos(0x29, 22900, 0, 12700, 0)
    SetChrPos(0x2A, 22900, 0, 12700, 0)
    SetChrPos(0x2B, 22900, 0, 12700, 0)
    SetChrPos(0x2C, 22900, 0, 12700, 0)
    SetChrPos(0x2D, 22900, 0, 12700, 0)
    SetMapObjFrame(0xFF, "isu00", 0x1, 0x1)
    SetMapObjFrame(0xFF, "isu00_sd", 0x1, 0x1)
    VolumeBGM(0x3C, 0x7D0)
    Sleep(2000)
    SetScenarioFlags(0x22, 4)
    NewScene("c010B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_23_8F68 end

    def Function_24_9E89(): pass

    label("Function_24_9E89")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50539.itc", 0x1E)
    LoadChrToIndex("apl/ch50006.itc", 0x1F)
    LoadChrToIndex("apl/ch51517.itc", 0x20)
    LoadChrToIndex("chr/ch30000.itc", 0x21)
    LoadChrToIndex("chr/ch20400.itc", 0x22)
    LoadChrToIndex("chr/ch21100.itc", 0x23)
    LoadChrToIndex("chr/ch20100.itc", 0x24)
    LoadChrToIndex("chr/ch21000.itc", 0x25)
    LoadChrToIndex("chr/ch21400.itc", 0x26)
    LoadChrToIndex("chr/ch08201.itc", 0x27)
    LoadEffect(0x0, "event\\ev500_00.eff")
    SoundLoad(803)
    SoundLoad(852)
    SoundLoad(3621)
    SoundLoad(3622)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis416.itp")
    SetChrPos(0x0, 4000, 850, 15000, 0)
    SetChrPos(0x1, 4000, 850, 15000, 0)
    SetChrPos(0x2, 4000, 850, 15000, 0)
    SetChrPos(0x3, 4000, 850, 15000, 0)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 200, 0, 1600, 180)
    SetChrChipByIndex(0x12, 0x21)
    SetChrSubChip(0x12, 0x0)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x12, 0x8000)
    SetChrPos(0x12, 2200, 0, 2300, 225)
    SetChrChipByIndex(0xA, 0x2)
    SetChrSubChip(0xA, 0x0)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xA, 0x4)
    SetChrFlags(0xA, 0x8000)
    SetChrPos(0xA, -1300, 0, 4400, 180)
    SetChrChipByIndex(0xD, 0x22)
    SetChrSubChip(0xD, 0x0)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x8000)
    SetChrPos(0xD, 400, 0, 4000, 180)
    SetChrChipByIndex(0xE, 0x23)
    SetChrSubChip(0xE, 0x0)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x8000)
    SetChrPos(0xE, 1700, 0, 4400, 180)
    SetChrChipByIndex(0xF, 0x24)
    SetChrSubChip(0xF, 0x0)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x8000)
    SetChrPos(0xF, 900, 0, 5600, 180)
    SetChrChipByIndex(0x10, 0x25)
    SetChrSubChip(0x10, 0x0)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x8000)
    SetChrPos(0x10, 3700, 0, 5400, 180)
    SetChrChipByIndex(0x11, 0x26)
    SetChrSubChip(0x11, 0x0)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x8000)
    SetChrPos(0x11, 4700, 0, 5400, 180)
    OP_7D(0xFF, 0xE6, 0xDC, 0x0, 0x0)
    OP_68(1000, 1000, 0, 0)
    MoveCamera(40, 19, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(20400, 0)
    OP_68(1020, 1000, 3180, 4000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)

    #C0377
    ChrTalk(
        0xD,
        (
            "#5P外、外面究竟\x01",
            "发生了什么……\x02",
        )
    )

    CloseMessageWindow()

    #C0378
    ChrTalk(
        0xE,
        (
            "#5P……我丈夫他……\x01",
            "不会有事吧……\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0x0, 0x1F4)
    Sleep(100)

    #C0379
    ChrTalk(
        0x8,
        (
            "#12P#01003F啊，请大家冷静。\x02\x03",

            "#01002F刚才接到了联络，\x01",
            "据说神秘武装集团\x01",
            "已经开始撤退了。\x02\x03",

            "等确认过安全状况之后，\x01",
            "大家就可以放心回家了。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_A1B9():
        TurnDirection(0xE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0xE, 0, lambda_A1B9)
    Sleep(30)

    def lambda_A1C9():
        TurnDirection(0x10, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_A1C9)
    Sleep(30)

    def lambda_A1D9():
        TurnDirection(0x11, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_A1D9)
    Sleep(30)
    WaitChrThread(0xE, 0)
    WaitChrThread(0x10, 0)
    WaitChrThread(0x11, 0)

    #C0380
    ChrTalk(
        0xE,
        "#5P真、真的吗！？\x02",
    )

    CloseMessageWindow()

    #C0381
    ChrTalk(
        0xD,
        (
            "#5P哦哦，女神爱德丝啊……\x01",
            "感谢您的保佑……！\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(20000, 1000)

    def lambda_A247():
        OP_9A(0xFE, 0x8, 0x4B0, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_A247)
    WaitChrThread(0xA, 1)

    #C0382
    ChrTalk(
        0xA,
        (
            "#5P#01112F#30W科长……\x01",
            "已经没事了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0383
    ChrTalk(
        0x8,
        (
            "#11P#01006F嗯，暂时不用担心了。\x02\x03",

            "#01001F但愿罗伊德他们\x01",
            "也平安无事……\x02",
        )
    )

    CloseMessageWindow()

    #C0384
    ChrTalk(
        0xA,
        (
            "#5P#01104F#30W嗯，不用担心。\x02\x03",

            "#01121F罗伊德他们肯定不会有事。\x02",
        )
    )

    CloseMessageWindow()

    #C0385
    ChrTalk(
        0x8,
        (
            "#11P#01005F啊，嗯……说的没错。\x02\x03",

            "#01002F毕竟他们已经\x01",
            "成长了很多。\x02\x03",

            "#01004F说不定已经比\x01",
            "当年的赛尔盖班还要——\x02",
        )
    )

    CloseMessageWindow()
    Sound(803, 2, 100, 0)
    Sleep(300)
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Fade(250)
    Sound(531, 0, 50, 0)
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    OP_0D()
    Sleep(300)
    OP_93(0x8, 0x10E, 0x1F4)
    Sleep(150)
    Fade(250)
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0x8, 0x20)
    SetChrFlags(0x8, 0x2)
    SetChrChipByIndex(0x8, 0x1F)
    SetChrSubChip(0x8, 0x2)
    Sound(802, 0, 100, 0)
    Sleep(500)
    SetChrSubChip(0x8, 0x3)
    OP_24(0x323)
    Sound(804, 0, 100, 0)
    Sleep(300)

    #C0386
    ChrTalk(
        0x8,
        (
            "#11P#01003F你好，这里是支援科。\x02\x03",

            "#01005F……哦哦，达德利吗？\x01",
            "你那边的状况如何？\x02\x03",

            "#01001F…………什么？\x01",
            "猎兵的飞艇……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0xA, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0xA)
    Sleep(500)

    def lambda_A4AA():
        OP_96(0xFE, 0xFFFFFCE0, 0x0, 0xCE4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_A4AA)
    WaitChrThread(0xA, 1)
    OP_93(0xA, 0x0, 0x1F4)
    SetChrChipByIndex(0xA, 0x27)
    SetChrSubChip(0xA, 0x0)

    def lambda_A4D7():
        OP_96(0xFE, 0x190, 0x0, 0x1A90, 0xDAC, 0x1)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_A4D7)
    WaitChrThread(0xA, 1)
    OP_68(1000, 2000, 3000, 3000)

    def lambda_A506():
        OP_96(0xFE, 0x514, 0x352, 0x2BC0, 0xDAC, 0x1)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_A506)
    WaitChrThread(0xA, 1)

    def lambda_A524():
        OP_96(0xFE, 0x514, 0xFA0, 0x3B60, 0xDAC, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_A524)
    FadeToDark(2000, 0, -1)
    OP_0D()
    WaitChrThread(0xA, 1)
    OP_6F(0x79)
    Sleep(1000)
    OP_68(-300, 800, 72310, 0)
    MoveCamera(35, 19, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(20000, 0)
    SetChrPos(0xA, 1400, 0, 70000, 0)
    SetChrChipByIndex(0xA, 0x2)
    SetChrSubChip(0xA, 0x0)
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    OP_68(-260, 1300, 72270, 2500)

    def lambda_A5B3():
        OP_96(0xFE, 0xFFFFFED4, 0x0, 0x11A6C, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_A5B3)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0xA, 1)
    OP_93(0xA, 0x0, 0x1F4)
    OP_6F(0x79)
    Sleep(300)
    OP_63(0xA, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0xA)
    Sleep(500)
    Fade(500)
    SetCameraDistance(19500, 800)
    Sound(928, 0, 60, 0)
    Sound(852, 2, 100, 0)
    PlayEffect(0x0, 0x0, 0xA, 0x0, 0, 750, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_6F(0x79)
    SetCameraDistance(18500, 30000)
    Sleep(500)

    #C0387
    ChrTalk(
        0xA,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#01119F#40W#11P………………………………\x02\x03",

            "#01118F#40W………果然…………\x02\x03",

            "#01120F#40W无论怎么说……\x01",
            "这个选择都是最好的……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    StopEffect(0x0, 0x2)
    StopSound(852, 1000, 100)
    Sleep(1300)

    #C0388
    ChrTalk(
        0xA,
        "#01123F#40W#11P……………………………………\x02",
    )

    CloseMessageWindow()
    Sleep(150)
    Sound(803, 2, 100, 0)
    Sleep(300)
    OP_63(0xA, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Sound(802, 0, 100, 0)
    Fade(250)
    SetChrChipByIndex(0xA, 0x20)
    SetChrSubChip(0xA, 0x0)
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0xA, 0x2)
    SetChrFlags(0xA, 0x20)
    Sleep(500)
    OP_24(0x323)
    Sound(804, 0, 100, 0)
    Sleep(300)
    SetChrSubChip(0xA, 0x1)
    Sleep(500)
    SetCameraDistance(18000, 20000)

    #C0389
    ChrTalk(
        0xA,
        (
            "#01112F#30W#11P#15A………喂喂………？\x02\x03",

            "#01108F#40W#25A………………嗯………\x01",
            "…………嗯…………………\x02",
        )
    )
    #Auto

    CloseMessageWindow()
    Sleep(300)
    OP_63(0xA, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0xA)
    Sleep(500)
    OP_C9(0x0, 0x80000000)

    #C0390
    ChrTalk(
        0xA,
        "#01121F#3621V#40W#11P#20A没问题。\x02",
    )
    #Auto

    CloseMessageWindow()
    SetCameraDistance(18000, 3000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    Sleep(500)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0391
    AnonymousTalk(
        0xA,
        (
            "#3622V#30W#40A我已经……\x01",
            "下定决心了。\x02",
        )
    )
    #Auto

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x80000000)
    StopBGM(0x1770)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(2000)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x1, 0xFF, 0x0)
    OP_32(0xFF, 0xFE, 0x0)
    OP_24(0x323)
    OP_24(0x354)
    Sleep(500)
    SetScenarioFlags(0x22, 0)
    NewScene("c110D", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_24_9E89 end

    def Function_25_A8EE(): pass

    label("Function_25_A8EE")

    TalkBegin(0xFF)
    OP_E5(0xA)
    FadeToDark(300, 0, -1)
    OP_0D()
    OP_E5(0x5)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A90A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_AF1B")
    RunExpression(0x3, (scpexpr(EXPR_EXEC_OP, "OP_E5(0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_END)),
        (0, "loc_A943"),
        (1, "loc_AAE5"),
        (2, "loc_AEFF"),
        (3, "loc_AF07"),
        (SWITCH_DEFAULT, "loc_AF16"),
    )


    label("loc_A943")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_A956")
    OP_2B(0x94, 0xFFFF)
    Jump("loc_AAE0")

    label("loc_A956")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_A971")
    OP_2B(0x8E, 0x8F, 0x90, 0x91, 0x92, 0xFFFF)
    Jump("loc_AAE0")

    label("loc_A971")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_A9BA")
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("自动语音")

    #A0392
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "现在没有支援请求。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    Jump("loc_AAE0")

    label("loc_A9BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_A9D5")
    OP_2B(0x8B, 0x8C, 0x88, 0x80, 0x83, 0xFFFF)
    Jump("loc_AAE0")

    label("loc_A9D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_AA10")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_A9FE")
    OP_2B(0x85, 0x86, 0x87, 0x88, 0x80, 0x83, 0xFFFF)
    Jump("loc_AA0B")

    label("loc_A9FE")

    OP_2B(0x85, 0x86, 0x88, 0x80, 0x83, 0xFFFF)

    label("loc_AA0B")

    Jump("loc_AAE0")

    label("loc_AA10")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_AA29")
    OP_2B(0x80, 0x81, 0x82, 0x83, 0xFFFF)
    Jump("loc_AAE0")

    label("loc_AA29")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_AA37")
    Jump("loc_AAE0")

    label("loc_AA37")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_AA54")
    OP_2B(0x79, 0x7A, 0x7B, 0x77, 0x71, 0x72, 0xFFFF)
    Jump("loc_AAE0")

    label("loc_AA54")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 3)), scpexpr(EXPR_END)), "loc_AA71")
    OP_2B(0x74, 0x75, 0x76, 0x77, 0x71, 0x72, 0xFFFF)
    Jump("loc_AAE0")

    label("loc_AA71")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_AA8A")
    OP_2B(0x6F, 0x70, 0x71, 0x72, 0xFFFF)
    Jump("loc_AAE0")

    label("loc_AA8A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_AABE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 7)), scpexpr(EXPR_END)), "loc_AAAE")
    OP_2B(0x6A, 0x6B, 0x6C, 0x6D, 0x67, 0xFFFF)
    Jump("loc_AAB9")

    label("loc_AAAE")

    OP_2B(0x6A, 0x6B, 0x6C, 0x67, 0xFFFF)

    label("loc_AAB9")

    Jump("loc_AAE0")

    label("loc_AABE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 7)), scpexpr(EXPR_END)), "loc_AAD5")
    OP_2B(0x65, 0x66, 0x67, 0xFFFF)
    Jump("loc_AAE0")

    label("loc_AAD5")

    OP_2B(0x65, 0x66, 0x67, 0x68, 0xFFFF)

    label("loc_AAE0")

    Jump("loc_AF16")

    label("loc_AAE5")

    SetMapFlags(0x40000000)
    OP_E5(0x7)
    Sleep(500)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_AB9C")
    SetChrName("自动语音")

    #A0393
    AnonymousTalk(
        0xFF,
        "这里是克洛斯贝尔警察局。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_E5(0x4)"), scpexpr(EXPR_END)), "loc_AB7D")

    #A0394
    AnonymousTalk(
        0xFF,
        "即将受理您的报告。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    RunExpression(0x5, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x2F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_E5(0xC)
    SetChrName("自动语音")

    #A0395
    AnonymousTalk(
        0xFF,
        (
            "报告处理完毕，\x01",
            "辛苦了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AB97")

    label("loc_AB7D")


    #A0396
    AnonymousTalk(
        0xFF,
        "没有可以报告的委托。\x02",
    )

    CloseMessageWindow()

    label("loc_AB97")

    Jump("loc_AEF1")

    label("loc_AB9C")

    SetChrName("接待小姐芙兰")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_ABEE")
    Sound(3062, 255, 100, 0)    #voice#Fran

    #A0397
    AnonymousTalk(
        0xFF,
        "#26A您好，这里是克洛斯贝尔警察局～！\x02",
    )

    CloseMessageWindow()
    Jump("loc_AC06")

    label("loc_ABEE")

    Sound(3061, 255, 100, 0)    #voice#Fran

    #A0398
    AnonymousTalk(
        0xFF,
        "#29A各位辛苦了。\x02",
    )

    CloseMessageWindow()

    label("loc_AC06")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E5(0x4)"), scpexpr(EXPR_END)), "loc_AE29")
    Sound(3067, 255, 100, 0)    #voice#Fran
    SetChrName("接待小姐芙兰")

    #A0399
    AnonymousTalk(
        0xFF,
        "#27A已经收到大家的报告～\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    RunExpression(0x5, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x2F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_E5(0xC)
    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x2F), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_ADB6")
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x2F), scpexpr(EXPR_END)),
        (14, "loc_AC6F"),
        (13, "loc_ACB7"),
        (12, "loc_ACFB"),
        (SWITCH_DEFAULT, "loc_AD41"),
    )


    label("loc_AC6F")

    Sound(3075, 255, 100, 0)    #voice#Fran
    SetChrName("接待小姐芙兰")

    #A0400
    AnonymousTalk(
        0xFF,
        (
            "#39A级别１ｓｔ——\x01",
            "罗伊德警官，实在太厉害了！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AD41")

    label("loc_ACB7")

    Sound(3074, 255, 100, 0)    #voice#Fran
    SetChrName("接待小姐芙兰")

    #A0401
    AnonymousTalk(
        0xFF,
        (
            "#38A级别２ｎｄ──\x01",
            "罗伊德警官，好厉害呢！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AD41")

    label("loc_ACFB")

    Sound(3073, 255, 100, 0)    #voice#Fran
    SetChrName("接待小姐芙兰")

    #A0402
    AnonymousTalk(
        0xFF,
        (
            "#33A级别３ｒｄ──\x01",
            "罗伊德警官，做得很好啊！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AD41")

    label("loc_AD41")

    Sound(3076, 255, 100, 0)    #voice#Fran
    SetChrName("接待小姐芙兰")

    #A0403
    AnonymousTalk(
        0xFF,
        (
            "#33A马上就会把奖励物品\x01",
            "给你们送去的～！\x02",
        )
    )

    CloseMessageWindow()
    Sound(3077, 255, 100, 0)    #voice#Fran

    #A0404
    AnonymousTalk(
        0xFF,
        (
            "#33A大家辛苦了～！\x01",
            "以后也请随时来向我报告～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AE21")

    label("loc_ADB6")

    Sound(3078, 255, 100, 0)    #voice#Fran
    SetChrName("接待小姐芙兰")

    #A0405
    AnonymousTalk(
        0xFF,
        "#17A报告就是以上这些吧～\x02",
    )

    CloseMessageWindow()
    Sound(3079, 255, 100, 0)    #voice#Fran

    #A0406
    AnonymousTalk(
        0xFF,
        (
            "#38A那么，以后如果完成了新的委托，\x01",
            "请再来向我报告吧～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AE21")

    SetScenarioFlags(0x0, 6)
    Jump("loc_AEF1")

    label("loc_AE29")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_AE98")
    Sound(3063, 255, 100, 0)    #voice#Fran
    SetChrName("接待小姐芙兰")

    #A0407
    AnonymousTalk(
        0xFF,
        (
            "#31A哎……\x01",
            "不是刚刚才报告过吗？\x02",
        )
    )

    CloseMessageWindow()
    Sound(3064, 255, 100, 0)    #voice#Fran

    #A0408
    AnonymousTalk(
        0xFF,
        "#35A等完成了新的委托之后再来报告吧～\x02",
    )

    CloseMessageWindow()
    Jump("loc_AEF1")

    label("loc_AE98")

    Sound(3065, 255, 100, 0)    #voice#Fran
    SetChrName("接待小姐芙兰")

    #A0409
    AnonymousTalk(
        0xFF,
        (
            "#38A哎，好像并没有可以\x01",
            "报告的委托啊～\x02",
        )
    )

    CloseMessageWindow()
    Sound(3066, 255, 100, 0)    #voice#Fran

    #A0410
    AnonymousTalk(
        0xFF,
        "#20A请下次再来报告吧～\x02",
    )

    CloseMessageWindow()

    label("loc_AEF1")

    OP_57(0x0)
    OP_E5(0x8)
    ClearMapFlags(0x40000000)
    Jump("loc_AF16")

    label("loc_AEFF")

    Call(0, 26)
    Jump("loc_AF16")

    label("loc_AF07")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_AF16")

    label("loc_AF16")

    Jump("loc_A90A")

    label("loc_AF1B")

    OP_E5(0x6)
    OP_C9(0x1, 0x4)
    OP_C9(0x1, 0x100)
    FadeToBright(300, 0)
    OP_0D()
    OP_E5(0xB)
    TalkEnd(0xFF)
    Return()

    # Function_25_A8EE end

    def Function_26_AF39(): pass

    label("Function_26_AF39")

    OP_E5(0x6)
    Sleep(100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x27, 3)), scpexpr(EXPR_END)), "loc_AF5B")
    SetScenarioFlags(0x2A, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_AF5B")
    ClearScenarioFlags(0x2A, 0)

    label("loc_AF5B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x27, 4)), scpexpr(EXPR_END)), "loc_AF78")
    SetScenarioFlags(0x2A, 1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_AF78")
    ClearScenarioFlags(0x2A, 1)

    label("loc_AF78")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x27, 5)), scpexpr(EXPR_END)), "loc_AF95")
    SetScenarioFlags(0x2A, 2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_AF95")
    ClearScenarioFlags(0x2A, 2)

    label("loc_AF95")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x27, 6)), scpexpr(EXPR_END)), "loc_AFB2")
    SetScenarioFlags(0x2A, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_AFB2")
    ClearScenarioFlags(0x2A, 3)

    label("loc_AFB2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x27, 7)), scpexpr(EXPR_END)), "loc_AFCF")
    SetScenarioFlags(0x2A, 4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_AFCF")
    ClearScenarioFlags(0x2A, 4)

    label("loc_AFCF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x28, 0)), scpexpr(EXPR_END)), "loc_AFEC")
    SetScenarioFlags(0x2A, 5)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_AFEC")
    ClearScenarioFlags(0x2A, 5)

    label("loc_AFEC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x28, 1)), scpexpr(EXPR_END)), "loc_AFF8")
    SetScenarioFlags(0x2A, 6)

    label("loc_AFF8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6C, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6C, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6C, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x131, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B04A")
    RunExpression(0x7, (scpexpr(EXPR_EXEC_OP, "MiniGame(0x10, 0x3, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    StopBGM(0x0)
    Jump("loc_B0C5")

    label("loc_B04A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 0)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_B09C")
    OP_24(0x80)
    RunExpression(0x7, (scpexpr(EXPR_EXEC_OP, "MiniGame(0x10, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_1F()
    Sound(128, 1, 50, 0)
    Jump("loc_B0C5")

    label("loc_B09C")

    RunExpression(0x7, (scpexpr(EXPR_EXEC_OP, "MiniGame(0x10, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_1F()

    label("loc_B0C5")

    Return()

    # Function_26_AF39 end

    SaveToFile()

Try(main)
