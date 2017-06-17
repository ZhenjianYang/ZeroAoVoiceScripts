from ScenarioHelper import *

def main():
    CreateScenaFile(
        "c035b.bin",                # FileName
        "c035b",                    # MapName
        "c035b",                    # Location
        0x002D,                     # MapIndex
        "ed7513",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 1, 0, 2, 0, 3],
    )

    BuildStringList((
        "c035b",                  # 0
        "尤利",                   # 1
        "塞克斯",                 # 2
        "瑞吉",                   # 3
    ))

    AddCharChip((
        "chr/ch44100.itc",                   # 00
        "chr/ch47500.itc",                   # 01
        "chr/ch23600.itc",                   # 02
        "chr/ch44102.itc",                   # 03
    ))

    DeclNpc(7989,    200,     1600,    270,  261,  0x0, 0,   0,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(5699,    0,       469,     45,   261,  0x0, 0,   1,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(7780,    0,       -810,    0,    261,  0x0, 0,   2,   0,   0,   0,   0,   7,   255,  0)

    ChipFrameInfo(280, 0)                                        # 0

    ScpFunction((
        "Function_0_118",          # 00, 0
        "Function_1_1C8",          # 01, 1
        "Function_2_1F3",          # 02, 2
        "Function_3_231",          # 03, 3
        "Function_4_232",          # 04, 4
        "Function_5_42A",          # 05, 5
        "Function_6_434",          # 06, 6
        "Function_7_59B",          # 07, 7
    ))


    def Function_0_118(): pass

    label("Function_0_118")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_150"),
        (1, "loc_15C"),
        (2, "loc_168"),
        (3, "loc_174"),
        (4, "loc_180"),
        (5, "loc_18C"),
        (6, "loc_198"),
        (SWITCH_DEFAULT, "loc_1A4"),
    )


    label("loc_150")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_1B0")

    label("loc_15C")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_1B0")

    label("loc_168")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_1B0")

    label("loc_174")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_1B0")

    label("loc_180")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_1B0")

    label("loc_18C")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_1B0")

    label("loc_198")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_1B0")

    label("loc_1A4")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_1B0")

    label("loc_1B0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1C7")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_1B0")

    label("loc_1C7")

    Return()

    # Function_0_118 end

    def Function_1_1C8(): pass

    label("Function_1_1C8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1F2")
    OP_94(0xFE, 0x334, 0x2904, 0xFFFFF31C, 0x3804, 0x3E8)
    Sleep(300)
    Jump("Function_1_1C8")

    label("loc_1F2")

    Return()

    # Function_1_1C8 end

    def Function_2_1F3(): pass

    label("Function_2_1F3")

    SetChrChipByIndex(0x8, 0x3)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    SetChrPos(0x9, 1000, 0, 3700, 270)
    SetChrPos(0xA, -500, 0, 3700, 90)
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0x9, 0x10)
    Return()

    # Function_2_1F3 end

    def Function_3_231(): pass

    label("Function_3_231")

    Return()

    # Function_3_231 end

    def Function_4_232(): pass

    label("Function_4_232")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x149, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B2")

    #C0001
    ChrTalk(
        0xFE,
        "……这么晚来，要干什么？\x02",
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0xFE,
        (
            "你们白天干的好事……\x01",
            "可别说已经忘记了。\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0x10A,
        (
            "#00605F（你们几个……\x01",
            "  与他们发生过什么矛盾吗？）\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x104,
        (
            "#00303F（哎，这个嘛……\x01",
            "  只能说是没办法的事……）\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x10A,
        (
            "#00603F（真是的……在这种敏感时期，\x01",
            "  不要引起无谓的纠纷啊。）\x02\x03",

            "#00600F（在明天的正式会议结束之前，\x01",
            "  绝对不能有丝毫松懈。\x01",
            "  ……知道了吗？）\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x101,
        "#00005F（明、明白了。）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x149, 3)
    Jump("loc_426")

    label("loc_3B2")


    #C0007
    ChrTalk(
        0xFE,
        (
            "你们白天干的好事……\x01",
            "可别说已经忘记了。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0xFE,
        "有朝一日，一定会让你们后悔的。\x02",
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x104,
        "#00306F（真是纠缠不休啊……）\x02",
    )

    CloseMessageWindow()

    label("loc_426")

    TalkEnd(0xFE)
    Return()

    # Function_4_232 end

    def Function_5_42A(): pass

    label("Function_5_42A")

    TalkBegin(0xFE)
    Call(0, 6)
    TalkEnd(0xFE)
    Return()

    # Function_5_42A end

    def Function_6_434(): pass

    label("Function_6_434")

    OP_4B(0x9, 0xFF)
    OP_4B(0xA, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_541")

    #C0010
    ChrTalk(
        0x9,
        (
            "尤利那家伙的\x01",
            "心情非常糟糕啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x9,
        (
            "本想带他去欢乐街转换一下心情，\x01",
            "但很多警官在那一带\x01",
            "守卫各国要人。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0xA,
        (
            "嗯，既然如此……\x01",
            "就开车去山道那边来个\x01",
            "夜间兜风吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0xA,
        (
            "这个时间行人\x01",
            "应该很少，可以\x01",
            "尽情驰骋一番……\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x9,
        "哦哦，这主意相当不错嘛。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_592")

    label("loc_541")


    #C0015
    ChrTalk(
        0x9,
        (
            "好，既然决定了，\x01",
            "那就去问问尤利吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x9,
        "瑞吉，你去准备车吧。\x02",
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0xA,
        "知道了。\x02",
    )

    CloseMessageWindow()

    label("loc_592")

    OP_4C(0x9, 0xFF)
    OP_4C(0xA, 0xFF)
    Return()

    # Function_6_434 end

    def Function_7_59B(): pass

    label("Function_7_59B")

    TalkBegin(0xFE)
    Call(0, 6)
    TalkEnd(0xFE)
    Return()

    # Function_7_59B end

    SaveToFile()

Try(main)
