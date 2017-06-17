from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "t119b.bin",                # FileName
        "t119b",                    # MapName
        "t119b",                    # Location
        0x0094,                     # MapIndex
        "ed7125",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 148, 0, 1, 0, 2],
    )

    BuildStringList((
        "t119b",                  # 0
        "尼基塔",                 # 1
    ))

    AddCharChip((
        "chr/ch26800.itc",                   # 00
    ))

    DeclNpc(67760,   0,       17290,   0,    401,  0x0, 0,   0,   0,   0,   0,   0,   3,   255,  0)

    ScpFunction((
        "Function_0_E4",           # 00, 0
        "Function_1_19C",          # 01, 1
        "Function_2_1DC",          # 02, 2
        "Function_3_27B",          # 03, 3
        "Function_4_38F",          # 04, 4
        "Function_5_445",          # 05, 5
        "Function_6_624",          # 06, 6
        "Function_7_6DA",          # 07, 7
        "Function_8_914",          # 08, 8
        "Function_9_983",          # 09, 9
        "Function_10_9F9",         # 0A, 10
        "Function_11_A4B",         # 0B, 11
    ))


    def Function_0_E4(): pass

    label("Function_0_E4")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_124"),
        (1, "loc_130"),
        (2, "loc_13C"),
        (3, "loc_148"),
        (4, "loc_154"),
        (5, "loc_160"),
        (6, "loc_16C"),
        (SWITCH_DEFAULT, "loc_178"),
    )


    label("loc_124")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_184")

    label("loc_130")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_184")

    label("loc_13C")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_184")

    label("loc_148")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_184")

    label("loc_154")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_184")

    label("loc_160")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_184")

    label("loc_16C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_184")

    label("loc_178")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_184")

    label("loc_184")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_19B")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_184")

    label("loc_19B")

    Return()

    # Function_0_E4 end

    def Function_1_19C(): pass

    label("Function_1_19C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_1B0")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 5)
    Jump("loc_1BF")

    label("loc_1B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 1)), scpexpr(EXPR_END)), "loc_1BF")
    ClearScenarioFlags(0x5C, 1)
    Event(0, 7)

    label("loc_1BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 1)), scpexpr(EXPR_END)), "loc_1CD")
    Jump("loc_1DB")

    label("loc_1CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 5)), scpexpr(EXPR_END)), "loc_1DB")
    ClearChrFlags(0x8, 0x80)

    label("loc_1DB")

    Return()

    # Function_1_19C end

    def Function_2_1DC(): pass

    label("Function_2_1DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 5)), scpexpr(EXPR_END)), "loc_1E5")

    label("loc_1E5")

    OP_1B(0x2, 0xFF, 0xFFFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1FD")
    OP_1B(0x2, 0x0, 0x8)

    label("loc_1FD")

    OP_1B(0x0, 0xFF, 0xFFFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_21A")
    OP_1B(0x0, 0x0, 0x4)
    Jump("loc_22D")

    label("loc_21A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_22D")
    OP_1B(0x0, 0x0, 0xA)

    label("loc_22D")

    OP_1B(0x1, 0xFF, 0xFFFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_24F")
    OP_1B(0x1, 0x0, 0x6)
    Jump("loc_262")

    label("loc_24F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_262")
    OP_1B(0x1, 0x0, 0xB)

    label("loc_262")

    OP_1B(0x3, 0xFF, 0xFFFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_27A")
    OP_1B(0x3, 0x0, 0x9)

    label("loc_27A")

    Return()

    # Function_2_1DC end

    def Function_3_27B(): pass

    label("Function_3_27B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_322")

    #C0001
    ChrTalk(
        0xFE,
        (
            "说什么为我\x01",
            "拍得宝石，\x01",
            "到最后还是失败了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0xFE,
        (
            "现在开始，必须要努力寻找\x01",
            "其他没有伴的客人了。\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0xFE,
        (
            "呼，真是的……\x01",
            "所以说，男人就是这么没用。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_38B")

    label("loc_322")


    #C0004
    ChrTalk(
        0xFE,
        (
            "詹姆斯先生今后也必须\x01",
            "更加机灵一些才行啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0xFE,
        (
            "唉……\x01",
            "现在开始，必须要努力寻找\x01",
            "其他没有伴的客人了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_38B")

    TalkEnd(0xFE)
    Return()

    # Function_3_27B end

    def Function_4_38F(): pass

    label("Function_4_38F")

    EventBegin(0x0)
    Fade(1000)
    OP_68(57500, 1400, 16000, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17750, 0)
    SetCameraDistance(17000, 1500)
    SetChrPos(0x101, 57310, 0, 16379, 270)
    SetChrPos(0xEF, 58340, 0, 15070, 270)
    SetChrPos(0x105, 59150, 0, 16640, 270)
    SetChrPos(0x133, 61160, 0, 16030, 270)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    FadeToDark(500, 0, -1)
    OP_0D()
    SetScenarioFlags(0x5C, 2)
    NewScene("t111B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_4_38F end

    def Function_5_445(): pass

    label("Function_5_445")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    FadeToBright(1000, 0)
    OP_68(57500, 1400, 16000, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17750, 0)
    SetCameraDistance(17000, 1500)
    SetChrPos(0x101, 57310, 0, 16379, 270)
    SetChrPos(0xEF, 58340, 0, 15070, 270)
    SetChrPos(0x105, 59150, 0, 16640, 270)
    SetChrPos(0x133, 61160, 0, 16030, 270)
    OP_0D()
    Sleep(500)

    #C0006
    ChrTalk(
        0x101,
        "#0010F#11P（唔……）\x02",
    )

    CloseMessageWindow()

    #N0007
    NpcTalk(
        0x101,
        "琪雅",
        "#5805F#5P（好像有个很高大的人呢～）\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_56A")

    #C0008
    ChrTalk(
        0x102,
        (
            "#0101F#11P（看上去，从正门逃走\x01",
            "  是不太可能了啊……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5F7")

    label("loc_56A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_5B1")

    #C0009
    ChrTalk(
        0x103,
        (
            "#0206F#11P（看起来，从正门逃走\x01",
            "  是不太可能了……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5F7")

    label("loc_5B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_5F7")

    #C0010
    ChrTalk(
        0x104,
        (
            "#0306F#11P（看样子，想从正门逃走\x01",
            "  是不太可能了啊……）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5F7")

    OP_57(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, 56900, 0, 16200, 270)
    SetScenarioFlags(0xA6, 7)
    OP_29(0x47, 0x1, 0x10)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_5_445 end

    def Function_6_624(): pass

    label("Function_6_624")

    EventBegin(0x0)
    Fade(1000)
    OP_68(-57500, 1400, 16000, 0)
    MoveCamera(315, 26, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17750, 0)
    SetCameraDistance(17000, 1500)
    SetChrPos(0x101, -57310, 0, 16379, 90)
    SetChrPos(0xEF, -58340, 0, 15070, 90)
    SetChrPos(0x105, -59150, 0, 16640, 90)
    SetChrPos(0x133, -61160, 0, 16030, 90)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    FadeToDark(500, 0, -1)
    OP_0D()
    SetScenarioFlags(0x5C, 3)
    NewScene("t111B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_6_624 end

    def Function_7_6DA(): pass

    label("Function_7_6DA")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    FadeToBright(1000, 0)
    OP_68(-57500, 1400, 16000, 0)
    MoveCamera(315, 26, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17750, 0)
    SetCameraDistance(17000, 1500)
    SetChrPos(0x101, -57310, 0, 16379, 90)
    SetChrPos(0xEF, -58340, 0, 15070, 90)
    SetChrPos(0x105, -59150, 0, 16640, 90)
    SetChrPos(0x133, -61160, 0, 16030, 90)
    OP_0D()
    Sleep(500)

    #C0011
    ChrTalk(
        0x101,
        "#0010F#5P（想从正门逃走，果然是行不通的吗……）\x02",
    )

    CloseMessageWindow()

    #N0012
    NpcTalk(
        0x101,
        "琪雅",
        (
            "#5805F#6P（喂喂，罗伊德。）\x02\x03",

            "#5809F（那个叔叔长得\x01",
            "  圆滚滚的，好有趣啊～！）\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x101,
        "#0006F#5P（呃……）\x02",
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x105,
        (
            "#0409F#5P（哈哈哈……\x01",
            "  这孩子真是太有意思了！）\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_885")

    #C0015
    ChrTalk(
        0x102,
        (
            "#0102F#5P（呵呵……\x01",
            "  可不能小看她哦。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8ED")

    label("loc_885")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_8B8")

    #C0016
    ChrTalk(
        0x103,
        "#0204F#5P（可不能小看她呢……）\x02",
    )

    CloseMessageWindow()
    Jump("loc_8ED")

    label("loc_8B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_8ED")

    #C0017
    ChrTalk(
        0x104,
        (
            "#0309F#5P（哈哈……\x01",
            "  不能小看她啊。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8ED")

    OP_57(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, -56900, 0, 16200, 90)
    SetScenarioFlags(0xA7, 1)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_7_6DA end

    def Function_8_914(): pass

    label("Function_8_914")

    EventBegin(0x1)

    #C0018
    ChrTalk(
        0x101,
        (
            "#0003F……必须尽早把这个孩子\x01",
            "带到安全的地方去……\x02\x03",

            "#0001F直接从正门的\x01",
            "出口出去吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 64000, 2000, 25100, 180)
    EventEnd(0x4)
    Return()

    # Function_8_914 end

    def Function_9_983(): pass

    label("Function_9_983")

    EventBegin(0x1)

    #C0019
    ChrTalk(
        0x101,
        (
            "#0004F还好有雷克特的帮忙，\x01",
            "正门的守备应该已经很薄弱了……\x02\x03",

            "#0000F不管怎样，绕到那边去吧！\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, -64000, 2000, 25100, 180)
    EventEnd(0x4)
    Return()

    # Function_9_983 end

    def Function_10_9F9(): pass

    label("Function_10_9F9")

    EventBegin(0x1)

    #C0020
    ChrTalk(
        0x101,
        (
            "#0013F（正门是行不通了……\x01",
            "  必须要寻找其它路线……）\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 57500, 0, 16000, 90)
    EventEnd(0x4)
    Return()

    # Function_10_9F9 end

    def Function_11_A4B(): pass

    label("Function_11_A4B")

    EventBegin(0x1)

    #C0021
    ChrTalk(
        0x101,
        (
            "#0013F（正门口有马尔克尼会长和\x01",
            "  那个加尔西亚在。\x01",
            "  必须要寻找其它路线……）\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, -57500, 0, 16000, 270)
    EventEnd(0x4)
    Return()

    # Function_11_A4B end

    SaveToFile()

Try(main)
