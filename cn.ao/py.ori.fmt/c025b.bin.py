from ScenarioHelper import *

def main():
    CreateScenaFile(
        "c025b.bin",                # FileName
        "c025b",                    # MapName
        "c025b",                    # Location
        0x000E,                     # MapIndex
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
        "c025b",                  # 0
        "雷缇",                   # 1
        "潘莎",                   # 2
        "寇肯",                   # 3
    ))

    AddCharChip((
        "chr/ch10300.itc",                   # 00
        "chr/ch22300.itc",                   # 01
        "chr/ch22302.itc",                   # 02
        "chr/ch32700.itc",                   # 03
        "chr/ch32702.itc",                   # 04
        "apl/ch50148.itc",                   # 05
        "chr/ch21000.itc",                   # 06
        "chr/ch21002.itc",                   # 07
    ))

    DeclNpc(51830,   0,       115930,  0,    261,  0x0, 0,   0,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(-54310,  0,       52840,   90,   261,  0x0, 0,   1,   0,   0,   1,   0,   5,   255,  0)
    DeclNpc(-51919,  0,       108370,  90,   261,  0x0, 0,   6,   0,   0,   0,   0,   6,   255,  0)

    ChipFrameInfo(292, 0)                                        # 0

    ScpFunction((
        "Function_0_124",          # 00, 0
        "Function_1_1D4",          # 01, 1
        "Function_2_1FF",          # 02, 2
        "Function_3_226",          # 03, 3
        "Function_4_227",          # 04, 4
        "Function_5_27C",          # 05, 5
        "Function_6_357",          # 06, 6
    ))


    def Function_0_124(): pass

    label("Function_0_124")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_15C"),
        (1, "loc_168"),
        (2, "loc_174"),
        (3, "loc_180"),
        (4, "loc_18C"),
        (5, "loc_198"),
        (6, "loc_1A4"),
        (SWITCH_DEFAULT, "loc_1B0"),
    )


    label("loc_15C")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_1BC")

    label("loc_168")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_1BC")

    label("loc_174")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_1BC")

    label("loc_180")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_1BC")

    label("loc_18C")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_1BC")

    label("loc_198")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_1BC")

    label("loc_1A4")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_1BC")

    label("loc_1B0")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_1BC")

    label("loc_1BC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1D3")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_1BC")

    label("loc_1D3")

    Return()

    # Function_0_124 end

    def Function_1_1D4(): pass

    label("Function_1_1D4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1FE")
    OP_94(0xFE, 0xFFFF28BA, 0xC9A4, 0xFFFF30C6, 0xD2C8, 0x3E8)
    Sleep(300)
    Jump("Function_1_1D4")

    label("loc_1FE")

    Return()

    # Function_1_1D4 end

    def Function_2_1FF(): pass

    label("Function_2_1FF")

    SetChrPos(0x9, -58130, 0, 58620, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_21F")
    SetChrFlags(0x9, 0x10)

    label("loc_21F")

    BeginChrThread(0x9, 0, 0, 0)
    Return()

    # Function_2_1FF end

    def Function_3_226(): pass

    label("Function_3_226")

    Return()

    # Function_3_226 end

    def Function_4_227(): pass

    label("Function_4_227")

    TalkBegin(0xFE)

    #C0001
    ChrTalk(
        0xFE,
        (
            "啊，不知不觉，\x01",
            "天色已经全黑下来了。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0xFE,
        (
            "我老公也快回来了，\x01",
            "得赶快做饭。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_4_227 end

    def Function_5_27C(): pass

    label("Function_5_27C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_30C")

    #C0003
    ChrTalk(
        0xFE,
        (
            "……啊！\x01",
            "我放时装杂志的书架里\x01",
            "混杂着铁路方面的书……\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0xFE,
        (
            "这肯定是爸爸干的。\x01",
            "同样的伎俩，\x01",
            "他到底还想用多少次啊？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    ClearChrFlags(0xFE, 0x10)
    Jump("loc_353")

    label("loc_30C")


    #C0005
    ChrTalk(
        0xFE,
        (
            "爸爸总是做这种事情，\x01",
            "希望我能喜欢上铁路。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0xFE,
        "真是太纠缠不休了。\x02",
    )

    CloseMessageWindow()

    label("loc_353")

    TalkEnd(0xFE)
    Return()

    # Function_5_27C end

    def Function_6_357(): pass

    label("Function_6_357")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3C7")

    #C0007
    ChrTalk(
        0xFE,
        (
            "我希望隆有朝一日\x01",
            "能继承我的批发生意……\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0xFE,
        (
            "但这小子整天\x01",
            "就知道玩，\x01",
            "真是让人头疼啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_429")

    label("loc_3C7")


    #C0009
    ChrTalk(
        0xFE,
        (
            "隆那小子，在主日学校\x01",
            "的考试成绩也是一塌糊涂。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0xFE,
        (
            "真希望他能稍微认真点学习，\x01",
            "不要只想着玩。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_429")

    TalkEnd(0xFE)
    Return()

    # Function_6_357 end

    SaveToFile()

Try(main)
