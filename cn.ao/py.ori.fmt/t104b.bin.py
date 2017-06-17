from ScenarioHelper import *

def main():
    CreateScenaFile(
        "t104b.bin",                # FileName
        "t104b",                    # MapName
        "t104b",                    # Location
        0x0043,                     # MapIndex
        "ed7513",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x1A,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 67, 0, 2, 0, 3],
    )

    BuildStringList((
        "t104b",                  # 0
        "鲁特",                   # 1
        "梅夏",                   # 2
        "游客",                   # 3
        "游客",                   # 4
        "游客",                   # 5
        "游客",                   # 6
        "沙扎克",                 # 7
        "珍妮特",                 # 8
        "薇娜",                   # 9
        "德罗娜",                 # 10
        "游客",                   # 11
    ))

    AddCharChip((
        "chr/ch25000.itc",                   # 00
        "chr/ch34500.itc",                   # 01
        "chr/ch24002.itc",                   # 02
        "chr/ch21802.itc",                   # 03
        "chr/ch21902.itc",                   # 04
        "chr/ch34402.itc",                   # 05
        "chr/ch27900.itc",                   # 06
        "chr/ch26600.itc",                   # 07
        "chr/ch32400.itc",                   # 08
        "chr/ch22002.itc",                   # 09
        "chr/ch26602.itc",                   # 0A
    ))

    DeclNpc(-104069, 0,       2980,    90,   389,  0x0, 0,   0,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(-101099, 0,       5880,    90,   385,  0x0, 0,   1,   0,   0,   1,   0,   6,   255,  0)
    DeclNpc(-97959,  119,     19090,   45,   453,  0x0, 0,   2,   0,   255, 255, 0,   7,   255,  0)
    DeclNpc(-104800, 119,     8930,    45,   453,  0x0, 0,   3,   0,   255, 255, 0,   8,   255,  0)
    DeclNpc(-103000, 119,     10930,   225,  453,  0x0, 0,   4,   0,   255, 255, 0,   9,   255,  0)
    DeclNpc(-96120,  119,     20889,   225,  453,  0x0, 0,   5,   0,   255, 255, 0,   10,  255,  0)
    DeclNpc(-94010,  119,     11039,   225,  453,  0x0, 0,   9,   0,   255, 255, 0,   11,  255,  0)
    DeclNpc(-95819,  119,     9050,    45,   453,  0x0, 0,   10,  0,   255, 255, 0,   13,  255,  0)
    DeclNpc(-1860,   0,       10640,   180,  389,  0x0, 0,   6,   0,   0,   0,   0,   15,  255,  0)
    DeclNpc(3930,    0,       3420,    225,  389,  0x0, 0,   7,   0,   0,   0,   0,   16,  255,  0)
    DeclNpc(3930,    0,       2299,    315,  389,  0x0, 0,   8,   0,   0,   0,   0,   17,  255,  0)

    DeclActor(-1770,   0,       8810,    1000,    -1860,   1500,    10640,   0x007E, 0,  14, 0x0000)
    DeclActor(-101650, 0,       2470,    1000,    -104070, 1500,    2980,    0x007E, 0,  4,  0x0000)

    ChipFrameInfo(644, 0)                                        # 0

    ScpFunction((
        "Function_0_284",          # 00, 0
        "Function_1_33C",          # 01, 1
        "Function_2_3C5",          # 02, 2
        "Function_3_48E",          # 03, 3
        "Function_4_4B6",          # 04, 4
        "Function_5_4BA",          # 05, 5
        "Function_6_6BD",          # 06, 6
        "Function_7_7FC",          # 07, 7
        "Function_8_884",          # 08, 8
        "Function_9_903",          # 09, 9
        "Function_10_9AE",         # 0A, 10
        "Function_11_A26",         # 0B, 11
        "Function_12_A55",         # 0C, 12
        "Function_13_C18",         # 0D, 13
        "Function_14_C47",         # 0E, 14
        "Function_15_C4B",         # 0F, 15
        "Function_16_E36",         # 10, 16
        "Function_17_EC8",         # 11, 17
    ))


    def Function_0_284(): pass

    label("Function_0_284")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_2C4"),
        (1, "loc_2D0"),
        (2, "loc_2DC"),
        (3, "loc_2E8"),
        (4, "loc_2F4"),
        (5, "loc_300"),
        (6, "loc_30C"),
        (SWITCH_DEFAULT, "loc_318"),
    )


    label("loc_2C4")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_324")

    label("loc_2D0")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_324")

    label("loc_2DC")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_324")

    label("loc_2E8")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_324")

    label("loc_2F4")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_324")

    label("loc_300")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_324")

    label("loc_30C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_324")

    label("loc_318")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_324")

    label("loc_324")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_33B")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_324")

    label("loc_33B")

    Return()

    # Function_0_284 end

    def Function_1_33C(): pass

    label("Function_1_33C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3C4")
    OP_95(0xFE, -98090, 0, 5880, 2000, 0x0)
    OP_95(0xFE, -98090, 0, 12710, 2000, 0x0)
    OP_95(0xFE, -92260, 0, 12710, 2000, 0x0)
    OP_95(0xFE, -92260, 0, 15180, 2000, 0x0)
    OP_95(0xFE, -101100, 0, 15180, 2000, 0x0)
    OP_95(0xFE, -101100, 0, 5880, 2000, 0x0)
    Jump("Function_1_33C")

    label("loc_3C4")

    Return()

    # Function_1_33C end

    def Function_2_3C5(): pass

    label("Function_2_3C5")

    SetChrChipByIndex(0xA, 0x2)
    SetChrSubChip(0xA, 0x0)
    EndChrThread(0xA, 0x0)
    SetChrBattleFlags(0xA, 0x4)
    SetChrChipByIndex(0xB, 0x3)
    SetChrSubChip(0xB, 0x0)
    EndChrThread(0xB, 0x0)
    SetChrBattleFlags(0xB, 0x4)
    SetChrChipByIndex(0xC, 0x4)
    SetChrSubChip(0xC, 0x0)
    EndChrThread(0xC, 0x0)
    SetChrBattleFlags(0xC, 0x4)
    SetChrChipByIndex(0xD, 0x5)
    SetChrSubChip(0xD, 0x0)
    EndChrThread(0xD, 0x0)
    SetChrBattleFlags(0xD, 0x4)
    SetChrChipByIndex(0xE, 0x9)
    SetChrSubChip(0xE, 0x0)
    EndChrThread(0xE, 0x0)
    SetChrBattleFlags(0xE, 0x4)
    SetChrChipByIndex(0xF, 0xA)
    SetChrSubChip(0xF, 0x0)
    EndChrThread(0xF, 0x0)
    SetChrBattleFlags(0xF, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 7)), scpexpr(EXPR_END)), "loc_439")
    Jump("loc_48D")

    label("loc_439")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_48D")
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x10)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x10)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x10)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x12, 0x10)

    label("loc_48D")

    Return()

    # Function_2_3C5 end

    def Function_3_48E(): pass

    label("Function_3_48E")

    OP_65(0x0, 0x1)
    OP_65(0x1, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 7)), scpexpr(EXPR_END)), "loc_4A4")
    Jump("loc_4B5")

    label("loc_4A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_4B5")
    OP_66(0x0, 0x1)
    OP_66(0x1, 0x1)

    label("loc_4B5")

    Return()

    # Function_3_48E end

    def Function_4_4B6(): pass

    label("Function_4_4B6")

    Call(0, 5)
    Return()

    # Function_4_4B6 end

    def Function_5_4BA(): pass

    label("Function_5_4BA")

    TalkBegin(0x8)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4C7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6B9")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_517")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_517")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_537")
    OP_AF(0x66)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6B4")

    label("loc_537")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_54B")
    Jump("loc_6B4")

    label("loc_54B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6B4")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_69D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_626")

    #C0001
    ChrTalk(
        0x8,
        (
            "如果您想庆祝生日，开欢迎会、欢送会，\x01",
            "甚至是向心上人求婚……\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x8,
        (
            "本店都会竭尽全力，\x01",
            "为您提供协助。\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0x8,
        (
            "如有兴趣，可以与我们详谈。\x01",
            "一定能带给您一个最棒的夜晚……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_698")

    label("loc_626")


    #C0004
    ChrTalk(
        0x8,
        (
            "本店的宗旨便是竭尽全力\x01",
            "满足客人们的一切想法。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x8,
        (
            "如有兴趣，可以与我们详谈。\x01",
            "一定能带给您一个最棒的夜晚……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_698")

    Jump("loc_6B4")

    label("loc_69D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_6AB")
    Jump("loc_6B4")

    label("loc_6AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_6B4")

    label("loc_6B4")

    Jump("loc_4C7")

    label("loc_6B9")

    TalkEnd(0x8)
    Return()

    # Function_5_4BA end

    def Function_6_6BD(): pass

    label("Function_6_6BD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_7E1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_778")

    #C0006
    ChrTalk(
        0xFE,
        (
            "中间那桌的客人\x01",
            "今天过生日呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0xFE,
        (
            "那位男子做了安排，\x01",
            "让店里所有人拍着手\x01",
            "为她唱歌庆祝生日。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0xFE,
        (
            "我们店长非常\x01",
            "好说话，所以偶尔会\x01",
            "像这样配合客人的想法。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_7DC")

    label("loc_778")


    #C0009
    ChrTalk(
        0xFE,
        (
            "哎，今晚有预约的客人好多，\x01",
            "真是太忙了。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0xFE,
        (
            "不好意思，如果没有提前预约，\x01",
            "请前往里面的服务台。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7DC")

    Jump("loc_7F8")

    label("loc_7E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_7EF")
    Jump("loc_7F8")

    label("loc_7EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_7F8")

    label("loc_7F8")

    TalkEnd(0xFE)
    Return()

    # Function_6_6BD end

    def Function_7_7FC(): pass

    label("Function_7_7FC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_869")

    #C0011
    ChrTalk(
        0xFE,
        (
            "正中间那桌的年轻人\x01",
            "还真是有创意啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0xFE,
        (
            "孙女明年过生日时，\x01",
            "我也要想办法给她一个惊喜。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_880")

    label("loc_869")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_877")
    Jump("loc_880")

    label("loc_877")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_880")

    label("loc_880")

    TalkEnd(0xFE)
    Return()

    # Function_7_7FC end

    def Function_8_884(): pass

    label("Function_8_884")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_8E8")

    #C0013
    ChrTalk(
        0xFE,
        (
            "哎，店长突然来找我，\x01",
            "还以为他要我帮忙做什么呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0xFE,
        "嗯，这种创意也不错啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_8FF")

    label("loc_8E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_8F6")
    Jump("loc_8FF")

    label("loc_8F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_8FF")

    label("loc_8FF")

    TalkEnd(0xFE)
    Return()

    # Function_8_884 end

    def Function_9_903(): pass

    label("Function_9_903")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_993")

    #C0015
    ChrTalk(
        0xFE,
        (
            "其实，这种大张旗鼓的事\x01",
            "要是真的发生在自己身上，\x01",
            "我大概会觉得很不好意思。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0xFE,
        (
            "呵呵，但以旁观者的身份\x01",
            "来看，还是很有趣的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9AA")

    label("loc_993")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_9A1")
    Jump("loc_9AA")

    label("loc_9A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_9AA")

    label("loc_9AA")

    TalkEnd(0xFE)
    Return()

    # Function_9_903 end

    def Function_10_9AE(): pass

    label("Function_10_9AE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_A0B")

    #C0017
    ChrTalk(
        0xFE,
        (
            "那位姐姐\x01",
            "今天过生日呢～\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0xFE,
        (
            "有这么多人给她庆祝生日，\x01",
            "真是让人羡慕啊～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A22")

    label("loc_A0B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_A19")
    Jump("loc_A22")

    label("loc_A19")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_A22")

    label("loc_A22")

    TalkEnd(0xFE)
    Return()

    # Function_10_9AE end

    def Function_11_A26(): pass

    label("Function_11_A26")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_A3A")
    Call(0, 12)
    Jump("loc_A51")

    label("loc_A3A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_A48")
    Jump("loc_A51")

    label("loc_A48")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_A51")

    label("loc_A51")

    TalkEnd(0xFE)
    Return()

    # Function_11_A26 end

    def Function_12_A55(): pass

    label("Function_12_A55")

    OP_4B(0xE, 0xFF)
    OP_4B(0xF, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B94")

    #C0019
    ChrTalk(
        0xF,
        (
            "呼，我刚才\x01",
            "真是吓了一跳。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0xF,
        (
            "没想到店员和店里的客人们\x01",
            "会一起为我庆祝生日。\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0xE,
        (
            "哈哈，是我拜托店里的各位帮忙的，\x01",
            "就是想给你一个惊喜呀。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0xF,
        "呵呵，我真的很高兴！\x02",
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0xF,
        (
            "但是，沙扎克先生，\x01",
            "你为什么要对我这么好呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0xE,
        (
            "呵呵，看到你那么消沉，\x01",
            "我实在是无法坐视不管。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0xF,
        "哎，你的意思是……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_C0F")

    label("loc_B94")


    #C0026
    ChrTalk(
        0xE,
        (
            "……没、没什么啦。\x01",
            "哈哈，我只是想耍帅一下而已。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0xE,
        (
            "……咳咳。\x01",
            "夜晚还长着呢，今天就好好\x01",
            "享受一下吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0xF,
        "好、好的⊥\x02",
    )

    CloseMessageWindow()

    label("loc_C0F")

    OP_4C(0xE, 0xFF)
    OP_4C(0xF, 0xFF)
    Return()

    # Function_12_A55 end

    def Function_13_C18(): pass

    label("Function_13_C18")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_C2C")
    Call(0, 12)
    Jump("loc_C43")

    label("loc_C2C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_C3A")
    Jump("loc_C43")

    label("loc_C3A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_C43")

    label("loc_C43")

    TalkEnd(0xFE)
    Return()

    # Function_13_C18 end

    def Function_14_C47(): pass

    label("Function_14_C47")

    Call(0, 15)
    Return()

    # Function_14_C47 end

    def Function_15_C4B(): pass

    label("Function_15_C4B")

    TalkBegin(0x10)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_C58")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E32")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CA8")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_CA8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CC8")
    OP_AF(0x69)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_E2D")

    label("loc_CC8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CDC")
    Jump("loc_E2D")

    label("loc_CDC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E2D")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_E08")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D9D")

    #C0029
    ChrTalk(
        0x10,
        (
            "这位客人，您今晚打算\x01",
            "参加宴会吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x10,
        (
            "本店出售各种用于正式\x01",
            "场合的服装。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x10,
        (
            "并且可以立刻为您量身修改尺寸，\x01",
            "如果有兴趣，可以慢慢看看。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_E03")

    label("loc_D9D")


    #C0032
    ChrTalk(
        0x10,
        (
            "本店出售各种用于正式\x01",
            "场合的服装。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x10,
        (
            "并且可以立刻为您量身修改尺寸，\x01",
            "如果有兴趣，可以慢慢看看。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E03")

    Jump("loc_E2D")

    label("loc_E08")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_E16")
    Jump("loc_E2D")

    label("loc_E16")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_E24")
    Jump("loc_E2D")

    label("loc_E24")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_E2D")

    label("loc_E2D")

    Jump("loc_C58")

    label("loc_E32")

    TalkEnd(0x10)
    Return()

    # Function_15_C4B end

    def Function_16_E36(): pass

    label("Function_16_E36")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_E9F")

    #C0034
    ChrTalk(
        0xFE,
        "呵呵呵，很适合您啊。\x02",
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0xFE,
        (
            "而且这条裙子的设计风格\x01",
            "端庄稳重，\x01",
            "在平时也能穿出去呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EC4")

    label("loc_E9F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_EAD")
    Jump("loc_EC4")

    label("loc_EAD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_EBB")
    Jump("loc_EC4")

    label("loc_EBB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_EC4")

    label("loc_EC4")

    TalkEnd(0xFE)
    Return()

    # Function_16_E36 end

    def Function_17_EC8(): pass

    label("Function_17_EC8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_F48")

    #C0036
    ChrTalk(
        0xFE,
        (
            "这样啊，我原本打算在\x01",
            "这次的宴会中穿……\x01",
            "平时也能穿可真不错呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0xFE,
        (
            "难得来一次，顺便\x01",
            "再买些配饰之类的吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F5F")

    label("loc_F48")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_F56")
    Jump("loc_F5F")

    label("loc_F56")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_F5F")

    label("loc_F5F")

    TalkEnd(0xFE)
    Return()

    # Function_17_EC8 end

    SaveToFile()

Try(main)
