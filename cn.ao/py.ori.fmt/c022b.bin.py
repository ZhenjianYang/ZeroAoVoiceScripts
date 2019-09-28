from ScenarioHelper import *

def main():
    CreateScenaFile(
        "c022b.bin",                # FileName
        "c022b",                    # MapName
        "c022b",                    # Location
        0x000D,                     # MapIndex
        "ed7513",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 2],
    )

    BuildStringList((
        "c022b",                  # 0
        "伊安律师",               # 1
        "皮特",                   # 2
    ))

    AddCharChip((
        "chr/ch05900.itc",                   # 00
        "chr/ch05902.itc",                   # 01
        "chr/ch22200.itc",                   # 02
    ))

    DeclNpc(4510,    1169,    15779,   180,  261,  0x0, 0,   0,   0,   0,   0,   0,   3,   255,  0)
    DeclNpc(12869,   1000,    4809,    90,   261,  0x0, 0,   2,   0,   0,   0,   0,   4,   255,  0)

    DeclActor(14350,   1000,    -70,     2000,    14350,   2500,    -70,     0x007C, 0,  5,  0x0000)

    ChipFrameInfo(276, 0)                                        # 0

    ScpFunction((
        "Function_0_114",          # 00, 0
        "Function_1_1C4",          # 01, 1
        "Function_2_1E4",          # 02, 2
        "Function_3_1EB",          # 03, 3
        "Function_4_39B",          # 04, 4
        "Function_5_531",          # 05, 5
    ))


    def Function_0_114(): pass

    label("Function_0_114")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_14C"),
        (1, "loc_158"),
        (2, "loc_164"),
        (3, "loc_170"),
        (4, "loc_17C"),
        (5, "loc_188"),
        (6, "loc_194"),
        (SWITCH_DEFAULT, "loc_1A0"),
    )


    label("loc_14C")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_1AC")

    label("loc_158")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_1AC")

    label("loc_164")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_1AC")

    label("loc_170")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_1AC")

    label("loc_17C")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_1AC")

    label("loc_188")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_1AC")

    label("loc_194")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_1AC")

    label("loc_1A0")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_1AC")

    label("loc_1AC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1C3")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_1AC")

    label("loc_1C3")

    Return()

    # Function_0_114 end

    def Function_1_1C4(): pass

    label("Function_1_1C4")

    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x188, 3)), scpexpr(EXPR_END)), "loc_1E3")
    SetChrFlags(0x9, 0x10)

    label("loc_1E3")

    Return()

    # Function_1_1C4 end

    def Function_2_1E4(): pass

    label("Function_2_1E4")

    ClearMapObjFlags(0x0, 0x10)
    Return()

    # Function_2_1E4 end

    def Function_3_1EB(): pass

    label("Function_3_1EB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_33C")

    #C0001
    ChrTalk(
        0xFE,
        (
            "#02200F哦，是你们啊。\x01",
            "这么晚来，真是少见呢。\x02\x03",

            "达德利竟然也在一起……\x01",
            "是不是发生了什么与明天的\x01",
            "正式会议有关的问题？\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x10A,
        (
            "#00603F我们正要去\x01",
            "确认这一点。\x02\x03",

            "#00600F为了确保万无一失，\x01",
            "最重要的事情就是在事前\x01",
            "消除一切不安定要素。\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0xFE,
        (
            "#02200F嗯，谨慎一些\x01",
            "终究没有坏处啊。\x02\x03",

            "虽然不知道事情的详情……\x01",
            "但各位一定要加油啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_397")

    label("loc_33C")


    #C0004
    ChrTalk(
        0xFE,
        (
            "#02200F好了……\x01",
            "准备工作至此已经足够了。\x02\x03",

            "为了顺利完成明天的任务，\x01",
            "今天就早点休息吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_397")

    TalkEnd(0xFE)
    Return()

    # Function_3_1EB end

    def Function_4_39B(): pass

    label("Function_4_39B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x188, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4D3")

    #C0005
    ChrTalk(
        0xFE,
        (
            "我在整理文件的时候，\x01",
            "找到了一本以前留下\x01",
            "看家时读过的书。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0xFE,
        (
            "我很喜欢这本书里的角色『黑猫影丸』……\x01",
            "比咪西还要喜欢呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0xFE,
        (
            "但我看书一般只看一遍，\x01",
            "没有反复回味的习惯……\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0xFE,
        (
            "机会难得，\x01",
            "各位也读读看如何？\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0009
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x2F1),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('沐浴阳光的阿尼艾丝４卷', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x188, 3)
    TalkEnd(0xFE)
    SetChrFlags(0x9, 0x10)
    Return()

    label("loc_4D3")


    #C0010
    ChrTalk(
        0xFE,
        (
            "哎，这份文件……\x01",
            "放错地方了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0xFE,
        (
            "伊安律师可真是的，\x01",
            "在这些方面实在是糊涂马虎……\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_4_39B end

    def Function_5_531(): pass

    label("Function_5_531")

    EventBegin(0x2)
    ClearMapFlags(0x20)
    Sound(807, 0, 100, 0)
    SetChrName("")

    #A0012
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "门上了锁。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    EventEnd(0x3)
    Return()

    # Function_5_531 end

    SaveToFile()

Try(main)
