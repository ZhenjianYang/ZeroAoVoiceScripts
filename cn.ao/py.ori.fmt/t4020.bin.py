from ScenarioHelper import *

def main():
    CreateScenaFile(
        "t4020.bin",                # FileName
        "t4020",                    # MapName
        "t4020",                    # Location
        0x005D,                     # MapIndex
        "ed7124",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x1F,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 93, 0, 2, 0, 3],
    )

    BuildStringList((
        "t4020",                  # 0
        "昆特老人",               # 1
        "尼尔森",                 # 2
        "修利",                   # 3
        "热可可",                 # 4
    ))

    AddCharChip((
        "chr/ch20000.itc",                   # 00
        "chr/ch45100.itc",                   # 01
        "chr/ch10102.itc",                   # 02
        "apl/ch51090.itc",                   # 03
    ))

    DeclNpc(260260,  0,       250,     0,    385,  0x0, 0,   0,   0,   0,   1,   0,   5,   255,  0)
    DeclNpc(260149,  0,       -1750,   135,  389,  0x0, 0,   1,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(257899,  50,      2880,    90,   389,  0x0, 0,   2,   0,   255, 255, 0,   10,  255,  0)
    DeclNpc(258209,  500,     2099,    0,    502,  0x0, 7,   3,   0,   255, 255, 255, 255, 255,  0)

    DeclActor(262920,  0,       3100,    1200,    262920,  1200,    3100,    0x007C, 0,  4,  0x0000)
    DeclActor(257930,  0,       1240,    1200,    257899,  1000,    2880,    0x007E, 0,  9,  0x0000)

    ChipFrameInfo(396, 0)                                        # 0

    ScpFunction((
        "Function_0_18C",          # 00, 0
        "Function_1_23C",          # 01, 1
        "Function_2_267",          # 02, 2
        "Function_3_44F",          # 03, 3
        "Function_4_4F5",          # 04, 4
        "Function_5_5A2",          # 05, 5
        "Function_6_11A0",         # 06, 6
        "Function_7_14BC",         # 07, 7
        "Function_8_15D0",         # 08, 8
        "Function_9_165E",         # 09, 9
        "Function_10_1662",        # 0A, 10
        "Function_11_17A7",        # 0B, 11
    ))


    def Function_0_18C(): pass

    label("Function_0_18C")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_1C4"),
        (1, "loc_1D0"),
        (2, "loc_1DC"),
        (3, "loc_1E8"),
        (4, "loc_1F4"),
        (5, "loc_200"),
        (6, "loc_20C"),
        (SWITCH_DEFAULT, "loc_218"),
    )


    label("loc_1C4")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_224")

    label("loc_1D0")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_224")

    label("loc_1DC")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_224")

    label("loc_1E8")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_224")

    label("loc_1F4")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_224")

    label("loc_200")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_224")

    label("loc_20C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_224")

    label("loc_218")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_224")

    label("loc_224")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_23B")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_224")

    label("loc_23B")

    Return()

    # Function_0_18C end

    def Function_1_23C(): pass

    label("Function_1_23C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_266")
    OP_94(0xFE, 0x3F516, 0xFFFFFA38, 0x3FD0E, 0x8B6, 0x3E8)
    Sleep(600)
    Jump("Function_1_23C")

    label("loc_266")

    Return()

    # Function_1_23C end

    def Function_2_267(): pass

    label("Function_2_267")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_275")
    Jump("loc_44E")

    label("loc_275")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_283")
    Jump("loc_44E")

    label("loc_283")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_29C")
    ClearChrFlags(0x8, 0x80)
    BeginChrThread(0x8, 0, 0, 1)
    Jump("loc_44E")

    label("loc_29C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2B5")
    ClearChrFlags(0x8, 0x80)
    BeginChrThread(0x8, 0, 0, 1)
    Jump("loc_44E")

    label("loc_2B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_2CE")
    ClearChrFlags(0x8, 0x80)
    BeginChrThread(0x8, 0, 0, 1)
    Jump("loc_44E")

    label("loc_2CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2E7")
    ClearChrFlags(0x8, 0x80)
    BeginChrThread(0x8, 0, 0, 1)
    Jump("loc_44E")

    label("loc_2E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_300")
    ClearChrFlags(0x8, 0x80)
    BeginChrThread(0x8, 0, 0, 1)
    Jump("loc_44E")

    label("loc_300")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_319")
    ClearChrFlags(0x8, 0x80)
    BeginChrThread(0x8, 0, 0, 1)
    Jump("loc_44E")

    label("loc_319")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 7)), scpexpr(EXPR_END)), "loc_332")
    ClearChrFlags(0x8, 0x80)
    BeginChrThread(0x8, 0, 0, 1)
    Jump("loc_44E")

    label("loc_332")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 5)), scpexpr(EXPR_END)), "loc_340")
    Jump("loc_44E")

    label("loc_340")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_34E")
    Jump("loc_44E")

    label("loc_34E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_367")
    ClearChrFlags(0x8, 0x80)
    BeginChrThread(0x8, 0, 0, 1)
    Jump("loc_44E")

    label("loc_367")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3B7")
    ClearChrFlags(0x8, 0x80)
    BeginChrThread(0x8, 0, 0, 0)
    SetChrPos(0x8, 260209, 0, -130, 0)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 260260, 0, 1420, 180)
    BeginChrThread(0x9, 0, 0, 0)
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0x9, 0x10)
    Jump("loc_44E")

    label("loc_3B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3C5")
    Jump("loc_44E")

    label("loc_3C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_41E")
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    SetChrChipByIndex(0xA, 0x2)
    SetChrSubChip(0xA, 0x0)
    EndChrThread(0xA, 0x0)
    SetChrBattleFlags(0xA, 0x4)
    SetChrPos(0x8, 259550, 0, 2840, 270)
    BeginChrThread(0x8, 0, 0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x133, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_419")
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0xA, 0x10)

    label("loc_419")

    Jump("loc_44E")

    label("loc_41E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 0)), scpexpr(EXPR_END)), "loc_437")
    ClearChrFlags(0x8, 0x80)
    BeginChrThread(0x8, 0, 0, 1)
    Jump("loc_44E")

    label("loc_437")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 7)), scpexpr(EXPR_END)), "loc_445")
    Jump("loc_44E")

    label("loc_445")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_44E")

    label("loc_44E")

    Return()

    # Function_2_267 end

    def Function_3_44F(): pass

    label("Function_3_44F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_46B")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    Jump("loc_482")

    label("loc_46B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_482")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)

    label("loc_482")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4CB")
    SetMapObjFrame(0xFF, "hikari00", 0x0, 0x1)
    SetMapObjFrame(0xFF, "footlight00", 0x0, 0x1)
    Sound(128, 1, 50, 0)
    Jump("loc_4DE")

    label("loc_4CB")

    SetMapObjFrame(0xFF, "footlight01", 0x0, 0x1)

    label("loc_4DE")

    OP_65(0x1, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4F4")
    OP_66(0x1, 0x1)

    label("loc_4F4")

    Return()

    # Function_3_44F end

    def Function_4_4F5(): pass

    label("Function_4_4F5")

    SetChrName("")

    #A0001
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "摆放着《一分钟学会烹饪·小吃篇》。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x2, 0x0)"), scpexpr(EXPR_END)), "loc_59E")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B2(0xD)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_59E")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0002
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "『鲜美三明治』\x07\x00",
            "的做法已经学会了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_59E")

    TalkEnd(0xFF)
    Return()

    # Function_4_4F5 end

    def Function_5_5A2(): pass

    label("Function_5_5A2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_69B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 2)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x89, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x95, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_630")

    #C0003
    ChrTalk(
        0xFE,
        (
            "尼尔森来给\x01",
            "盖伊扫墓了。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0xFE,
        (
            "他最近好像一直在调查\x01",
            "盖伊被害的那起事件……\x01",
            "不知有没有什么进展呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_696")

    label("loc_630")


    #C0005
    ChrTalk(
        0xFE,
        (
            "成为独立自主的国家……\x01",
            "这会给克洛斯贝尔带来什么呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0xFE,
        (
            "……希望长眠于此的各位\x01",
            "继续守护我们。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_696")

    Jump("loc_119C")

    label("loc_69B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_797")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_734")

    #C0007
    ChrTalk(
        0xFE,
        (
            "亚里欧斯刚才来这里扫墓了，\x01",
            "还过来和我打了声招呼。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0xFE,
        (
            "虽然没有像当年一样，\x01",
            "陪我一起喝点酒……\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0xFE,
        "但那家伙完全没变呢。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_792")

    label("loc_734")


    #C0010
    ChrTalk(
        0xFE,
        (
            "亚里欧斯每次来扫墓时，\x01",
            "都会顺便来这里探望我，\x01",
            "至今都是如此有礼。\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0xFE,
        "那家伙完全没变呢。\x02",
    )

    CloseMessageWindow()

    label("loc_792")

    Jump("loc_119C")

    label("loc_797")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_80A")

    #C0012
    ChrTalk(
        0xFE,
        (
            "据说在山道作战的\x01",
            "警备队伤亡惨重。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0xFE,
        (
            "……前途无量的年轻人\x01",
            "就这么不幸丧命，\x01",
            "我实在是难以接受。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_119C")

    label("loc_80A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_951")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8BB")

    #C0014
    ChrTalk(
        0xFE,
        (
            "经受风雨的摧残，\x01",
            "刻在墓碑上面的文字\x01",
            "也会渐渐消褪。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0xFE,
        (
            "有很多墓碑就这样\x01",
            "慢慢被人们遗忘……\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0xFE,
        (
            "为了避免这种情况的发生，\x01",
            "才需要我这样的守墓人。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_94C")

    label("loc_8BB")


    #C0017
    ChrTalk(
        0xFE,
        (
            "经过漫长岁月的洗礼，以及风雨的摧残，\x01",
            "有很多墓碑上的文字会渐渐消褪，\x01",
            "从而被大家遗忘……\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0xFE,
        (
            "为了避免那种情况的发生，\x01",
            "才需要我这样的守墓人。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_94C")

    Jump("loc_119C")

    label("loc_951")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_ACA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A42")

    #C0019
    ChrTalk(
        0xFE,
        (
            "盖伊在刚与从小一起长大\x01",
            "的恋人订婚之后殉职。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0xFE,
        (
            "亚里欧斯的妻子在一起事故中不幸丧生，\x01",
            "爱女也因事故失明。\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0xFE,
        (
            "他们为克洛斯贝尔和大家\x01",
            "鞠躬尽瘁，拼命操劳，\x01",
            "结果却遭遇如此不幸……\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0xFE,
        "……这真是让人痛心万分啊。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_AC5")

    label("loc_A42")


    #C0023
    ChrTalk(
        0xFE,
        (
            "盖伊和亚里欧斯比任何人\x01",
            "都认真尽职，为了克洛斯贝尔\x01",
            "和大家鞠躬尽瘁，拼命操劳。\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0xFE,
        (
            "但却遭到如此不幸……\x01",
            "这真是让人痛心万分啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AC5")

    Jump("loc_119C")

    label("loc_ACA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_C4B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BC6")

    #C0025
    ChrTalk(
        0xFE,
        (
            "如今已经赫赫有名的亚里欧斯，\x01",
            "当年时而会被盖伊拉过来\x01",
            "陪我一起喝酒。\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0xFE,
        (
            "那小子做什么事情都很有节制。\x01",
            "每当我和盖伊喝得烂醉如泥时，\x01",
            "他总是坐在一旁，若无其事地望着我们。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0xFE,
        (
            "呵呵，真想看一次那小子\x01",
            "喝醉之后耍酒疯的模样啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_C46")

    label("loc_BC6")


    #C0028
    ChrTalk(
        0xFE,
        (
            "亚里欧斯那小子，\x01",
            "当年时而会被盖伊拉过来\x01",
            "陪我一起喝酒。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0xFE,
        (
            "他是个很有节制的家伙，\x01",
            "从来都不会像我和盖伊\x01",
            "一样喝得烂醉如泥。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C46")

    Jump("loc_119C")

    label("loc_C4B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 7)), scpexpr(EXPR_END)), "loc_D05")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CB5")

    #C0030
    ChrTalk(
        0xFE,
        "你们要去扫墓吗？\x02",
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0xFE,
        (
            "天黑之后，这里会有些冷，\x01",
            "你们还是早点扫完墓回去吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_D00")

    label("loc_CB5")


    #C0032
    ChrTalk(
        0xFE,
        (
            "这里的地势比较高，\x01",
            "到了晚上会有些冷。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0xFE,
        "你们还是早点扫完墓回去吧。\x02",
    )

    CloseMessageWindow()

    label("loc_D00")

    Jump("loc_119C")

    label("loc_D05")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 5)), scpexpr(EXPR_END)), "loc_D13")
    Jump("loc_119C")

    label("loc_D13")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_D21")
    Jump("loc_119C")

    label("loc_D21")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_ED2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E42")

    #C0034
    ChrTalk(
        0xFE,
        (
            "早在『克洛斯贝尔问题』\x01",
            "这种说法流行起来之前，\x01",
            "这个问题本身就已根深蒂固地存在于此地了。\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0xFE,
        (
            "克洛斯贝尔经常会被卷入到\x01",
            "帝国和共和国的纷争之中，\x01",
            "因此而丧生的无辜者简直不计其数。\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0xFE,
        (
            "多亏盖伊，我才能从\x01",
            "过去的悲伤中振作起来……\x01",
            "但如今仍有很多人的创伤没有愈合。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_ECD")

    label("loc_E42")


    #C0037
    ChrTalk(
        0xFE,
        (
            "刚才驾临此地的科洛蒂娅公主\x01",
            "对『克洛斯贝尔问题』痛心不已，\x01",
            "完全将其视为自身的问题。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0xFE,
        (
            "虽然年纪轻轻，但真是一位\x01",
            "满怀大慈大爱的人啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_ECD")

    Jump("loc_119C")

    label("loc_ED2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_F36")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EED")
    Call(0, 7)
    Jump("loc_F31")

    label("loc_EED")


    #C0039
    ChrTalk(
        0xFE,
        (
            "唔，没想到\x01",
            "尼尔森竟然回来了。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0xFE,
        (
            "好，今晚要和他\x01",
            "好好聊一聊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F31")

    Jump("loc_119C")

    label("loc_F36")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_F44")
    Jump("loc_119C")

    label("loc_F44")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_FEB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x133, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F5F")
    Call(0, 11)
    Jump("loc_FE6")

    label("loc_F5F")


    #C0041
    ChrTalk(
        0xFE,
        (
            "出身于诺桑比亚吗……\x01",
            "这孩子可能也受过不少苦呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0xFE,
        (
            "再怎么说，也不能让小孩子喝酒，\x01",
            "等她下次过来的时候，\x01",
            "给她准备一些茶点好了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FE6")

    Jump("loc_119C")

    label("loc_FEB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 0)), scpexpr(EXPR_END)), "loc_1185")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x135, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1006")
    Call(0, 6)
    Jump("loc_1180")

    label("loc_1006")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1104")

    #C0043
    ChrTalk(
        0xFE,
        (
            "盖伊亡故之后，\x01",
            "我喝酒的量也大大减少了。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0xFE,
        (
            "失去了可以开怀共饮的朋友，\x01",
            "真是寂寞啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x153,
        (
            "#01108F老爷爷……\x02\x03",

            "#01100F……等我长大以后，一定会和\x01",
            "罗伊德他们一起过来陪你喝酒！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x153, 500)

    #C0046
    ChrTalk(
        0xFE,
        (
            "哈哈，是吗～\x01",
            "那我可要好好期待\x01",
            "那一天的到来了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1180")

    label("loc_1104")


    #C0047
    ChrTalk(
        0xFE,
        (
            "呵呵呵，等这个小姑娘\x01",
            "成长到可以喝酒的年纪时，\x01",
            "肯定会是个超级大美女。\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0xFE,
        (
            "我可要尽量活久点，\x01",
            "好好期待那一天\x01",
            "的到来啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1180")

    Jump("loc_119C")

    label("loc_1185")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 7)), scpexpr(EXPR_END)), "loc_1193")
    Jump("loc_119C")

    label("loc_1193")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_119C")

    label("loc_119C")

    TalkEnd(0xFE)
    Return()

    # Function_5_5A2 end

    def Function_6_11A0(): pass

    label("Function_6_11A0")

    OP_4B(0x8, 0xFF)
    TurnDirection(0x8, 0x101, 0)
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0049
    ChrTalk(
        0x8,
        (
            "哦哦，是罗伊德啊……\x01",
            "真是好久不见了。\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x8,
        "你是什么时候回来的？\x02",
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x101,
        (
            "#00000F刚回来没多久，\x01",
            "好久不见。\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x109,
        "#10105F罗伊德警官，这位是……？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2E, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1292")

    #C0053
    ChrTalk(
        0x102,
        (
            "#00100F呵呵，是在以前的某次委托中\x01",
            "认识的老爷爷。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1292")


    #C0054
    ChrTalk(
        0x101,
        (
            "#00000F嗯……\x01",
            "是当年经常和我大哥\x01",
            "一起喝酒的昆特先生。\x02\x03",

            "#00004F昆特先生对我也很好。\x01",
            "在教团事件结束后，我们一起喝酒时，\x01",
            "他讲了很多过去的事情呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x8,
        "当时确实聊得挺开心。\x02",
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x8,
        (
            "不过你的酒量比盖伊差远了，\x01",
            "稍微有点无趣啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x101,
        "#00012F哈哈……真抱歉。\x02",
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x102,
        (
            "#00100F呵呵，我们当时\x01",
            "也应邀而来了。\x02\x03",

            "#00109F缇欧还没有成年，所以当时\x01",
            "只能喝果汁，她好像还有些不满呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x105,
        (
            "#10302F呵呵，原来如此。\x02\x03",

            "#10304F老人家，今后也请\x01",
            "多多关照我们哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x8,
        "嗯，既然是罗伊德的同事，我自然非常欢迎。\x02",
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x8,
        (
            "我平时就在这里管理这片墓地。\x01",
            "只要你们高兴，什么时候过来都可以。\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x8, 0xFF)
    SetScenarioFlags(0x135, 4)
    Return()

    # Function_6_11A0 end

    def Function_7_14BC(): pass

    label("Function_7_14BC")

    OP_4B(0x9, 0xFF)
    OP_4B(0x8, 0xFF)

    #C0062
    ChrTalk(
        0x8,
        (
            "真是不好意思啊，尼尔森，\x01",
            "竟然让你送我这么好的酒。\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x8,
        "价格肯定很贵吧？\x02",
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x9,
        (
            "哪里，这是别人送给我的，\x01",
            "请不必在意。\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x9,
        (
            "只要您能喝掉，\x01",
            "我就很开心了。\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x8,
        (
            "呵呵，既然如此，\x01",
            "我们今天晚上一起喝如何？\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x9,
        (
            "呵呵，好啊。\x01",
            "好久没和您一起喝酒了。\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x9, 0xFF)
    OP_4C(0x8, 0xFF)
    SetScenarioFlags(0x0, 0)
    SetScenarioFlags(0x0, 1)
    ClearChrFlags(0x8, 0x10)
    ClearChrFlags(0x9, 0x10)
    Return()

    # Function_7_14BC end

    def Function_8_15D0(): pass

    label("Function_8_15D0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_165A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15EE")
    Call(0, 7)
    Jump("loc_165A")

    label("loc_15EE")


    #C0068
    ChrTalk(
        0xFE,
        (
            "呵呵，只要您不嫌和我聊天无聊，\x01",
            "我有很多话想说呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0xFE,
        (
            "话说回来，昆特先生的身体如此健康，\x01",
            "真是太好了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_165A")

    TalkEnd(0xFE)
    Return()

    # Function_8_15D0 end

    def Function_9_165E(): pass

    label("Function_9_165E")

    Call(0, 10)
    Return()

    # Function_9_165E end

    def Function_10_1662(): pass

    label("Function_10_1662")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x133, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1677")
    Call(0, 11)
    Jump("loc_17A3")

    label("loc_1677")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1732")

    #C0070
    ChrTalk(
        0xA,
        (
            "#14008F该怎么说呢……\x01",
            "克洛斯贝尔真是一座\x01",
            "不可思议的城市啊。\x02\x03",

            "#14003F……总之，多亏你们，\x01",
            "我总算找到了目标。\x01",
            "　　\x02\x03",

            "#14002F为了报答伊莉娅小姐的恩情，\x01",
            "我一定会拼命努力。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17A3")

    label("loc_1732")


    #C0071
    ChrTalk(
        0xA,
        (
            "#14003F……总之，多亏你们，\x01",
            "我总算找到了目标。\x01",
            "　　　\x02\x03",

            "#14002F为了报答伊莉娅小姐的恩情，\x01",
            "我一定会拼命努力。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17A3")

    TalkEnd(0xA)
    Return()

    # Function_10_1662 end

    def Function_11_17A7(): pass

    label("Function_11_17A7")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(258420, 1500, 830, 0)
    MoveCamera(28, 23, 0, 0)
    OP_6E(260, 0)
    SetCameraDistance(33960, 0)
    SetChrPos(0x101, 258709, 0, 120, 0)
    SetChrPos(0x102, 259860, 0, -120, 0)
    SetChrPos(0x109, 259010, 0, -1110, 0)
    SetChrPos(0x105, 260160, 0, -1370, 0)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu14000.itp")
    OP_4B(0x8, 0xFF)
    OP_93(0x8, 0xB4, 0x0)
    OP_93(0xA, 0x64, 0x0)
    SetChrSubChip(0xA, 0x2)
    FadeToBright(1000, 0)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x10)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x137, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_190C")

    #C0072
    ChrTalk(
        0x101,
        (
            "#12P#00005F哎，是修利……？\x01",
            "我们在意外的地方见面了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0xA,
        "#14000F……哟，是你们啊。\x02",
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x102,
        "#12P#00100F那个……你在这里做什么呢？\x02",
    )

    CloseMessageWindow()
    Jump("loc_1A9D")

    label("loc_190C")


    #C0075
    ChrTalk(
        0x101,
        (
            "#12P#00005F哎，是彩虹剧团的……\x01",
            "我们在意外的地方见面了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0xA,
        (
            "#14000F……你们是\x01",
            "伊莉娅姐和莉夏姐\x01",
            "的朋友吧？\x02\x03",

            "说起来，还没做过\x01",
            "自我介绍呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0077
    AnonymousTalk(
        0xA,
        (
            "我是在剧团中打杂的\x01",
            "修利·亚特雷德。\x02\x03",

            "……那个，请多指教。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    #C0078
    ChrTalk(
        0x102,
        (
            "#12P#00109F呵呵，请多指教哦，修利。\x02\x03",

            "#00100F那个……你在这里做什么呢？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A9D")


    #C0079
    ChrTalk(
        0x8,
        (
            "她连伞都没带，淋着大雨\x01",
            "走在墓地中。\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0x8,
        (
            "所以我就把她叫到小屋，\x01",
            "冲杯热可可\x01",
            "给她喝。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xA, 0x0)
    Sleep(100)

    #C0081
    ChrTalk(
        0xA,
        (
            "#14002F……谢谢您带我\x01",
            "来避雨，老爷爷。\x02\x03",

            "#14004F喝了这杯可可之后……\x01",
            "身体暖和多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0x10E, 0x1F4)

    #C0082
    ChrTalk(
        0x8,
        "#11P呵呵，那就好。\x02",
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x109,
        "#12P#10100F不过，你为何要来墓地……？\x02",
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0xA)
    SetChrSubChip(0xA, 0x2)
    Sleep(100)

    #C0084
    ChrTalk(
        0xA,
        (
            "#14001F……我原本是想去\x01",
            "教会做祷告的。\x02\x03",

            "#14003F但不知为什么，最后还是退缩了。\x02\x03",

            "#14008F……也许是因为在诺桑比亚\x01",
            "从没见过那么雄伟的教堂吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0085
    ChrTalk(
        0x101,
        "#12P#00001F诺桑比亚，好像是……\x02",
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x105,
        "#12P#10303F嗯，是个位于大陆北部的自治州。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1D6B")

    #C0087
    ChrTalk(
        0x102,
        (
            "#12P#00105F也就是说……修利当时提到的\x01",
            "那个贫民窟就在……\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0xA,
        "#14008F嗯……就在那个自治州。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1D9D")

    label("loc_1D6B")


    #C0089
    ChrTalk(
        0xA,
        (
            "#14008F嗯……我就是出身于那里的\x01",
            "一座贫民窟。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D9D")


    #C0090
    ChrTalk(
        0x109,
        "#12P#10108F这样啊……\x02",
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x8,
        (
            "#11P唔，我听说诺桑比亚\x01",
            "是个相当贫困的地方……\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0xA,
        (
            "#14003F嗯……\x01",
            "可以说是贫困得超乎想象。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0xA)

    #C0093
    ChrTalk(
        0xA,
        (
            "#14008F在那个地方，大家都在\x01",
            "为了生存而拼命。\x02\x03",

            "根本没有一丝多余的精力\x01",
            "可以用来关怀他人。\x02\x03",

            "#14003F……我不是太理解，\x01",
            "但克洛斯贝尔真是很不可思议。\x02\x03",

            "虽然有很多让人厌恶的家伙……\x02\x03",

            "但也有伊莉娅小姐这种温柔的人，\x01",
            "愿意收留我这样的人加入剧团……\x02\x03",

            "这位老爷爷也是一样，面对陌生人，\x01",
            "会主动关怀帮助。\x02\x03",

            "#14000F而且，在不知不觉间，\x01",
            "彩虹剧团的大家还开始让我参加\x01",
            "演员们的表演练习……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0094
    ChrTalk(
        0x101,
        (
            "#12P#00002F表演练习……\x01",
            "嘿，那可真是很厉害呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0xA,
        (
            "#14005F啊……嗯嗯……\x02\x03",

            "#14003F但我现在总觉得还是\x01",
            "有些困惑。\x02\x03",

            "#14008F像我这样的人竟然\x01",
            "能以成为演员为目标……\x01",
            "这真是以前从来没有想过的。\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0x102,
        "#12P#00108F修利……\x02",
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0xA,
        (
            "#14003F算啦，我也明白\x01",
            "烦恼下去\x01",
            "也无济于事。\x02\x03",

            "#14002F话说回来……\x01",
            "你们几个真是\x01",
            "很奇怪啊。\x02\x03",

            "竟然会如此认真地\x01",
            "听我说这些。\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x101,
        "#12P#00005F奇、奇怪吗……？\x02",
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0x102,
        (
            "#12P#00100F呵呵，但好像\x01",
            "无法否认呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0x109,
        (
            "#12P#10102F在警察局里，\x01",
            "支援科确实是个\x01",
            "相当另类的部门啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0x105,
        (
            "#12P#10302F呵呵，特别是队长，\x01",
            "可是个十足的怪人呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x101,
        (
            "#12P#00006F瓦吉，你可没资格这么说。\x02\x03",

            "#00000F嗯……该怎么说呢，\x01",
            "我们能以这种形式相识，\x01",
            "也算是某种缘分。\x02\x03",

            "要是你以后遇到了什么困难，\x01",
            "随时都可以找我们商量哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0x8,
        (
            "#11P呵呵，这间小屋\x01",
            "也随时欢迎你来做客。\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0x8,
        (
            "#11P下次我会给你\x01",
            "准备一些茶点的。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xA, 0x0)

    #C0105
    ChrTalk(
        0xA,
        "#14002F哈哈……谢谢您了。\x02",
    )

    CloseMessageWindow()
    OP_5A()
    SetScenarioFlags(0x133, 6)
    OP_50(0x6F, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_CC(0x1, 0xFF, 0x0)
    OP_4C(0x8, 0xFF)
    OP_93(0x8, 0x10E, 0x0)
    OP_93(0xA, 0x5A, 0x0)
    SetChrSubChip(0xA, 0x0)
    ClearChrFlags(0x8, 0x10)
    ClearChrFlags(0xA, 0x10)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 259230, 0, -370, 0)
    EventEnd(0x5)
    Return()

    # Function_11_17A7 end

    SaveToFile()

Try(main)
