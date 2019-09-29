from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "c0110_1.bin",                # FileName
        "c0110",                    # MapName
        "c0110",                    # Location
        0x0009,                     # MapIndex
        "ed7100",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 1000, 0, 2000, 0, 0, 1, 9, 0, 1, 0, 2],
    )

    BuildStringList((
        "c0110_1",                # 0
    ))

    DeclEvent(0x0000, 0, 17,  10.0,                  10.5,                  0.0,                   25.0,                  [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.19999998807907104,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.19999998807907104,   0.0,                   -5.0,                  -2.0999999046325684,   -0.0,                  1.0])

    ScpFunction((
        "Function_0_194",          # 00, 0
        "Function_1_363",          # 01, 1
        "Function_2_367",          # 02, 2
        "Function_3_8AC",          # 03, 3
        "Function_4_1AF0",         # 04, 4
        "Function_5_1DAD",         # 05, 5
        "Function_6_1F06",         # 06, 6
        "Function_7_24ED",         # 07, 7
        "Function_8_2A3E",         # 08, 8
        "Function_9_2D57",         # 09, 9
        "Function_10_2ED5",        # 0A, 10
        "Function_11_30BF",        # 0B, 11
        "Function_12_3374",        # 0C, 12
        "Function_13_368D",        # 0D, 13
        "Function_14_3AE6",        # 0E, 14
        "Function_15_43CB",        # 0F, 15
        "Function_16_4408",        # 10, 16
        "Function_17_4A5B",        # 11, 17
        "Function_18_4C54",        # 12, 18
        "Function_19_4CF3",        # 13, 19
        "Function_20_4E49",        # 14, 20
        "Function_21_5468",        # 15, 21
        "Function_22_5943",        # 16, 22
        "Function_23_5B08",        # 17, 23
        "Function_24_5CCD",        # 18, 24
        "Function_25_5E8E",        # 19, 25
        "Function_26_605A",        # 1A, 26
        "Function_27_6217",        # 1B, 27
        "Function_28_63D4",        # 1C, 28
        "Function_29_6595",        # 1D, 29
        "Function_30_6761",        # 1E, 30
        "Function_31_67B4",        # 1F, 31
        "Function_32_6857",        # 20, 32
        "Function_33_698F",        # 21, 33
        "Function_34_6A30",        # 22, 34
        "Function_35_6AD1",        # 23, 35
        "Function_36_6B74",        # 24, 36
        "Function_37_6C15",        # 25, 37
        "Function_38_6CBE",        # 26, 38
        "Function_39_6D61",        # 27, 39
    ))


    def Function_0_194(): pass

    label("Function_0_194")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_240")
    SetChrName("")

    #A0001
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "留言板上写有消息。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0002
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "『被老狐狸给叫过去了。\x01",
            "  我会随便应付一下的，晚上回来。\x01",
            "                         赛尔盖』\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_35F")

    label("loc_240")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_2C1")
    SetChrName("")

    #A0003
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "留言板上写有消息。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0004
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "『我去总部了，\x01",
            "  打算晚上回来。\x01",
            "         赛尔盖』\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_35F")

    label("loc_2C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x43, 0)), scpexpr(EXPR_END)), "loc_35F")
    SetChrName("")

    #A0005
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "留言板上写有消息。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0006
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "『有点私事，出去了。\x01",
            "  那件事就交给你们随便处理吧。\x01",
            "                       赛尔盖』\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_35F")

    TalkEnd(0xFF)
    Return()

    # Function_0_194 end

    def Function_1_363(): pass

    label("Function_1_363")

    Call(1, 3)
    Return()

    # Function_1_363 end

    def Function_2_367(): pass

    label("Function_2_367")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_382")
    Call(0, 48)
    Jump("loc_8AB")

    label("loc_382")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_393")
    Jump("loc_8A8")

    label("loc_393")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_3A1")
    Jump("loc_8A8")

    label("loc_3A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_END)), "loc_3AF")
    Jump("loc_8A8")

    label("loc_3AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_4C3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_483")
    OP_93(0xFE, 0x5A, 0x0)
    SetChrName("")

    #A0007
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "赛尔盖在厨房\x01",
            "清洗早餐的餐具。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x0, 500)

    #C0008
    ChrTalk(
        0x8,
        (
            "#1003F既然牵扯到了黑手党，\x01",
            "那么搜查一科应该也会有所行动了……\x02\x03",

            "#1000F这种事件确实不能坐视不理啊。\x02\x03",

            "稍后我也准备去\x01",
            "总部露个面。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4BE")

    label("loc_483")


    #C0009
    ChrTalk(
        0x8,
        (
            "#1000F你们也尽早出发吧。\x02\x03",

            "稍后我也准备去\x01",
            "总部露个面。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4BE")

    Jump("loc_8A8")

    label("loc_4C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_END)), "loc_4D1")
    Jump("loc_8A8")

    label("loc_4D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_4DF")
    Jump("loc_8A8")

    label("loc_4DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_4ED")
    Jump("loc_8A8")

    label("loc_4ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_4FB")
    Jump("loc_8A8")

    label("loc_4FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_509")
    Jump("loc_8A8")

    label("loc_509")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_517")
    Jump("loc_8A8")

    label("loc_517")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_525")
    Jump("loc_8A8")

    label("loc_525")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_801")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_77D")

    #C0010
    ChrTalk(
        0x8,
        "#1005F怎么，全都回来了啊。\x02",
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x101,
        (
            "#0000F科长……\x01",
            "您竟然在自己的房间里，真少见啊。\x02\x03",

            "在查什么资料吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x8,
        (
            "#1002F……不是，\x01",
            "只是香烟抽完了。\x02\x03",

            "正在找我平时存下的\x01",
            "私房钱呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0013
    ChrTalk(
        0x103,
        (
            "#0206F唉，早就料到大概\x01",
            "会是这类事情。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x8,
        (
            "#1003F对了对了，蔡特那家伙\x01",
            "在后门附近。\x02\x03",

            "#1000F你们几个可要负起责任，\x01",
            "把它照顾好啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x104,
        (
            "#0302F知道啦～\x02\x03",

            "#0309F哈，反正阿缇和大小姐\x01",
            "每天都会去抚摸它，这就足够了吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x102,
        (
            "#0113F……咳咳，那个，\x01",
            "因为通过身体接触来交流也是很重要的。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x103,
        "#0202F那是当然。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_7FC")

    label("loc_77D")


    #C0018
    ChrTalk(
        0x8,
        (
            "#1003F蔡特那家伙\x01",
            "在后门附近。\x02\x03",

            "#1000F你们几个可要负起责任，\x01",
            "把它照顾好啊。\x02\x03",

            "虽然我平时也会给它喂食，\x01",
            "但其它的可就不管了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7FC")

    Jump("loc_8A8")

    label("loc_801")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_80F")
    Jump("loc_8A8")

    label("loc_80F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_81D")
    Jump("loc_8A8")

    label("loc_81D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_82B")
    Jump("loc_8A8")

    label("loc_82B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_839")
    Jump("loc_8A8")

    label("loc_839")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_847")
    Jump("loc_8A8")

    label("loc_847")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 5)), scpexpr(EXPR_END)), "loc_8A8")

    #C0019
    ChrTalk(
        0x8,
        (
            "#1000F怎么了，赶快\x01",
            "去确认支援请求吧。\x02\x03",

            "只要调查那里的终端，\x01",
            "就可以查看相关情报了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8A8")

    TalkEnd(0x8)

    label("loc_8AB")

    Return()

    # Function_2_367 end

    def Function_3_8AC(): pass

    label("Function_3_8AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8C7")
    Call(0, 48)
    Jump("loc_1AEF")

    label("loc_8C7")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0x9)
    ClearChrFlags(0x9, 0x10)
    TurnDirection(0x9, 0x0, 0)
    OP_52(0x9, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_95B")
    Jump("loc_9A5")

    label("loc_95B")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_97B")
    OP_52(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9A5")

    label("loc_97B")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_99B")
    OP_52(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9A5")

    label("loc_99B")

    OP_52(0x9, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_9A5")

    OP_52(0x9, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x9, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_D4D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 2)), scpexpr(EXPR_END)), "loc_A4F")

    #C0020
    ChrTalk(
        0x9,
        (
            "#1005F怎么，又回来了吗？\x02\x03",

            "#1003F索妮亚那边就由\x01",
            "我来进行联络。\x02\x03",

            "#1001F总之，你们就赶快去\x01",
            "乌尔斯拉医院吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D48")

    label("loc_A4F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 1)), scpexpr(EXPR_END)), "loc_BEB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCC, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B94")

    #C0021
    ChrTalk(
        0x9,
        (
            "#1005F……？\x01",
            "怎么了，还不去医院吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x101,
        "#0003F啊，其实……\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    #A0023
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "将从达德利那里得到的情报，\x01",
            "还有无法和医院取得联络的事情做了说明。\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x9,
        (
            "#1010F………………………………\x02\x03",

            "嘁……火药味好浓啊。\x02\x03",

            "#1003F我也赶快和各方面\x01",
            "取得联络吧。\x02\x03",

            "#1001F总之，你们几个就赶快去\x01",
            "乌尔斯拉医院吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x101,
        "#0013F是！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0xCC, 5)
    Jump("loc_BE6")

    label("loc_B94")


    #C0026
    ChrTalk(
        0x9,
        (
            "#1001F我也赶快和各方面\x01",
            "取得联络吧。\x02\x03",

            "总之，你们几个就赶快去\x01",
            "乌尔斯拉医院吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BE6")

    Jump("loc_D48")

    label("loc_BEB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CB9")

    #C0027
    ChrTalk(
        0x9,
        (
            "#1000F和协会那边的联络\x01",
            "就交给我。\x02\x03",

            "你们赶快去乌尔斯拉医院\x01",
            "找那个什么医生就行了。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x102,
        (
            "#0100F小滴和小琪雅\x01",
            "应该在一起吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x9,
        (
            "#1002F是啊，蔡特也和她们在一起，\x01",
            "所以这边的事情不用担心。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_D48")

    label("loc_CB9")


    #C0030
    ChrTalk(
        0x9,
        (
            "#1003F这边的事情不用担心，\x01",
            "不管发生什么都有我来处理。\x02\x03",

            "#1000F你们几个快点去\x01",
            "乌尔斯拉医院就行了。\x02\x03",

            "最好在今天之内，将药物的成分\x01",
            "检验出来。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D48")

    Jump("loc_1AE8")

    label("loc_D4D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_F2E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_DDE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCC, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D71")
    Call(1, 13)
    Jump("loc_DD9")

    label("loc_D71")


    #C0031
    ChrTalk(
        0x9,
        (
            "#1003F警察局上层那边\x01",
            "就由我来敷衍搪塞。\x02\x03",

            "#1001F……你们要调查的话就尽快，\x01",
            "我这边恐怕也拖不了太久。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DD9")

    Jump("loc_F29")

    label("loc_DDE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EBB")

    #C0032
    ChrTalk(
        0x9,
        (
            "#1003F重要参考人失踪了吗……\x02\x03",

            "#1001F事态的进展速度或许\x01",
            "比想象中的还要快啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x101,
        (
            "#0003F嗯……首先必须要\x01",
            "掌握事件的状况……\x02\x03",

            "#0000F不好意思了，科长，\x01",
            "这边的事情就拜托您了。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x9,
        "#1000F啊，交给我吧。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_F29")

    label("loc_EBB")


    #C0035
    ChrTalk(
        0x9,
        (
            "#1000F如果这次的事件\x01",
            "牵扯到了『教团』……\x01",
            "只要继续追查下去，就必然要面对他们。\x02\x03",

            "你们几个，可不要大意哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F29")

    Jump("loc_1AE8")

    label("loc_F2E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_END)), "loc_FE8")

    #C0036
    ChrTalk(
        0x9,
        (
            "#1003F好啦，那药物就交给\x01",
            "乌尔斯拉医院的医生……\x02\x03",

            "#1002F一科那边就不用管了。\x01",
            "他们都是些优秀的家伙，\x01",
            "一定能取得一些成果。\x02\x03",

            "你们就像平时一样，\x01",
            "按照自己的方式自由行动吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1AE8")

    label("loc_FE8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 7)), scpexpr(EXPR_END)), "loc_10DB")
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0037
    ChrTalk(
        0x9,
        (
            "#1005F什么嘛，这么慢。\x02\x03",

            "#1000F『黑月』那边的询问\x01",
            "难道需要花这么多时间吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x101,
        (
            "#0003F不……其实是又出现了\x01",
            "其它值得注意的事件。\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x102,
        (
            "#0101F我们将把那些情况\x01",
            "与『黑月』遇袭事件一起进行报告。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Call(0, 47)
    Return()

    label("loc_10DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_10E9")
    Jump("loc_1AE8")

    label("loc_10E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_END)), "loc_10F7")
    Jump("loc_1AE8")

    label("loc_10F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_1105")
    Jump("loc_1AE8")

    label("loc_1105")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_11B4")

    #C0040
    ChrTalk(
        0x9,
        (
            "#1004F至于琪雅，罗伊德，\x01",
            "暂时就交给你照顾了。\x02\x03",

            "#1000F只是，如果查明了什么情况，\x01",
            "要立刻进行报告。\x01",
            "毕竟这件事关系到了整个警察系统。\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x101,
        "#0000F是的，明白了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1AE8")

    label("loc_11B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_11C2")
    Jump("loc_1AE8")

    label("loc_11C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_1370")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12F5")

    #C0042
    ChrTalk(
        0x9,
        (
            "#1000F哼，看样子，你们似乎\x01",
            "已经下定决心了啊。\x02\x03",

            "#1004F──算啦，随便你们吧。\x01",
            "至于上级那里，我会\x01",
            "想办法敷衍过去的。\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x101,
        "#0000F不好意思了，科长。\x02",
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x102,
        (
            "#0100F……总之\x01",
            "就拜托您了。\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x9,
        (
            "#1002F呵呵，不用在意。\x01",
            "『特别任务支援科』正是为了\x01",
            "这种时候而存在的。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x102,
        "#0105F是、是吗……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_136B")

    label("loc_12F5")


    #C0047
    ChrTalk(
        0x9,
        (
            "#1004F那么，我就一边泡红茶，\x01",
            "一边想想怎么应付上面那些家伙吧。\x02\x03",

            "#1002F呵呵……不用担心，\x01",
            "我可是很擅长这类事情的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_136B")

    Jump("loc_1AE8")

    label("loc_1370")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_137E")
    Jump("loc_1AE8")

    label("loc_137E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_138C")
    Jump("loc_1AE8")

    label("loc_138C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_139A")
    Jump("loc_1AE8")

    label("loc_139A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_1542")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14C8")

    #C0048
    ChrTalk(
        0x9,
        (
            "#1003F艾丝蒂尔·布莱特和\x01",
            "约修亚·布莱特吗……\x02\x03",

            "#1002F──你们昨天遇到的那两个人\x01",
            "似乎有着非同寻常的经历呢。\x02\x03",

            "这次的事件，如果拖下去的话，\x01",
            "游击士协会那边肯定也会有所动作的。\x02\x03",

            "#1004F如果不希望那种情况出现，\x01",
            "那就拼命干活吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x102,
        (
            "#0111F（……这大概也算是\x01",
            "  在鼓励我们吧。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_153D")

    label("loc_14C8")


    #C0050
    ChrTalk(
        0x9,
        (
            "#1004F这次的事件，如果拖下去的话，\x01",
            "游击士协会那边肯定也会有所动作的。\x02\x03",

            "#1002F哈，总之，你们就打起精神加油干吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_153D")

    Jump("loc_1AE8")

    label("loc_1542")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_1550")
    Jump("loc_1AE8")

    label("loc_1550")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_17B6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_173D")
    SetChrSubChip(0x9, 0x0)

    #C0051
    ChrTalk(
        0x9,
        "#1003F呼，早上吸一支烟真是享受啊……\x02",
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0x9)
    ClearChrFlags(0x9, 0x10)
    TurnDirection(0x9, 0x0, 0)
    OP_52(0x9, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_163A")
    Jump("loc_1684")

    label("loc_163A")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_165A")
    OP_52(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1684")

    label("loc_165A")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_167A")
    OP_52(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1684")

    label("loc_167A")

    OP_52(0x9, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1684")

    OP_52(0x9, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x9, 0x10)

    #C0052
    ChrTalk(
        0x9,
        (
            "#1005F喔，你们已经听过那边的交代了吗？\x02\x03",

            "#1004F那就适当努力一下吧，\x01",
            "至少要让副局长\x01",
            "找不到理由对你们横加指责。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x101,
        "#0006F是是，明白啦。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_17B1")

    label("loc_173D")


    #C0054
    ChrTalk(
        0x9,
        (
            "#1002F虽然还不知道详情，\x01",
            "但工作内容好像和警备队那边有关吧。\x02\x03",

            "如果不能取得像样的成果，\x01",
            "可就要被副局长刁难了啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17B1")

    Jump("loc_1AE8")

    label("loc_17B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_18D9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1895")

    #C0055
    ChrTalk(
        0x9,
        (
            "#1000F去西街的法律\x01",
            "事务所吧。\x02\x03",

            "只要对那里的律师先生说\x01",
            "你们是支援科的人，\x01",
            "他应该就会听你们说下去的。\x02\x03",

            "#1003F你们加油吧，争取多问到\x01",
            "一些有意义的情报──就这样。\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x104,
        "#0306F真是没干劲啊，科长～\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_18D4")

    label("loc_1895")


    #C0057
    ChrTalk(
        0x9,
        (
            "#1003F你们加油吧，争取多问到\x01",
            "一些有意义的情报──就这样。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18D4")

    Jump("loc_1AE8")

    label("loc_18D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 7)), scpexpr(EXPR_END)), "loc_19F2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19AD")

    #C0058
    ChrTalk(
        0x9,
        (
            "#1005F怎么了，你们几个，\x01",
            "不是让你们去旧城区吗。\x02\x03",

            "#1003F我们这里的业务就跟打杂事务所差不多。\x01",
            "除了支援请求之外，随时都有可能\x01",
            "接到其它紧急调查任务。\x02\x03",

            "#1000F这种紧急任务就要优先处理。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_19ED")

    label("loc_19AD")


    #C0059
    ChrTalk(
        0x9,
        (
            "#1003F赶快去旧城区吧。\x02\x03",

            "#1000F具体内容我也不清楚，就这样。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19ED")

    Jump("loc_1AE8")

    label("loc_19F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_1AE8")

    #C0060
    ChrTalk(
        0x9,
        (
            "#1003F处理一些鸡毛蒜皮的支援请求\x01",
            "也是我们特别任务支援科的工作。\x02\x03",

            "#1000F虽然接不接受，决定权在你们。\x01",
            "但警察局的接待处是一定要去的。\x02\x03",

            "另外，对艾尼格玛的\x01",
            "调整，已经委托给导力商店了，\x01",
            "记得顺道去那里看看。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1AE8")

    #C0061
    ChrTalk(
        0x101,
        "#0000F了解。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_1AE8")

    SetChrSubChip(0x9, 0x0)
    TalkEnd(0x9)

    label("loc_1AEF")

    Return()

    # Function_3_8AC end

    def Function_4_1AF0(): pass

    label("Function_4_1AF0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 1)), scpexpr(EXPR_END)), "loc_1B04")
    Call(1, 5)
    Jump("loc_1DA9")

    label("loc_1B04")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_1C48")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C09")

    #C0062
    ChrTalk(
        0xA,
        "#1110F啊，是大家～！\x02",
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x101,
        (
            "#0002F哈哈，你们好像\x01",
            "玩得很开心啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0xA,
        (
            "#1109F嘿嘿嘿～\x02\x03",

            "#1110F罗伊德，你们\x01",
            "又要去工作了吗～？\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x102,
        (
            "#0102F嗯，不过很快\x01",
            "就会回来的哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x103,
        (
            "#0202F晚饭我们就和滴一起，\x01",
            "大家热热闹闹地吃吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0xA,
        "#1109F嗯！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_1C43")

    label("loc_1C09")

    OP_93(0xFE, 0xB4, 0x0)

    #C0068
    ChrTalk(
        0xA,
        (
            "#1100F对啦～像这样抚摸的话，\x01",
            "它就会摇尾巴哦～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C43")

    Jump("loc_1DA9")

    label("loc_1C48")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 7)), scpexpr(EXPR_END)), "loc_1CB9")

    #C0069
    ChrTalk(
        0xFE,
        (
            "#1104F擦擦擦～¤\x01",
            "必须要把盘子整整齐齐地摆好～！\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x101,
        "#0000F（不知为何，她好像很热衷于此呢。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_1DA9")

    label("loc_1CB9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_1DA9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D5A")
    OP_93(0xFE, 0x0, 0x0)
    SetChrName("")

    #A0071
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "琪雅在厨房\x01",
            "收拾早餐后的餐具。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x0, 500)

    #C0072
    ChrTalk(
        0xA,
        (
            "#1100F罗伊德～要是知道了什么，\x01",
            "也要告诉给琪雅哦～！\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0x101,
        "#0002F哈哈，明白。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_1DA9")

    label("loc_1D5A")


    #C0074
    ChrTalk(
        0xA,
        (
            "#1104F继续整理～继续整理～¤\x02\x03",

            "#1110F要是知道了什么，\x01",
            "也要告诉给琪雅哦～！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DA9")

    TalkEnd(0xFE)
    Return()

    # Function_4_1AF0 end

    def Function_5_1DAD(): pass

    label("Function_5_1DAD")

    OP_93(0xA, 0xB4, 0x0)
    OP_93(0xF, 0xE1, 0x0)
    OP_4B(0xA, 0xFF)
    OP_4B(0xF, 0xFF)

    #C0075
    ChrTalk(
        0xF,
        (
            "#6005F哇，真的呢。\x01",
            "皮毛又软又蓬松……\x02\x03",

            "#6000F我的名字是滴。\x01",
            "请多关照哦，蔡特。\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0xD,
        "#1200F呜噜噜，呜噜噜噜噜……\x02",
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0xA,
        (
            "#1110F那个……\x02\x03",

            "#1109F它在说『我不讨厌\x01",
            "  懂礼貌的孩子』～\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1EFD")

    #C0078
    ChrTalk(
        0x102,
        (
            "#0108F（最好还是先不要\x01",
            "  告诉小琪雅她们任何事吧……）\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0x101,
        (
            "#0003F（是啊……\x01",
            "  这里就交给蔡特，我们赶快去医院吧。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)

    label("loc_1EFD")

    OP_4C(0xA, 0xFF)
    OP_4C(0xF, 0xFF)
    Return()

    # Function_5_1DAD end

    def Function_6_1F06(): pass

    label("Function_6_1F06")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1F9A")
    Jump("loc_1FE4")

    label("loc_1F9A")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1FBA")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1FE4")

    label("loc_1FBA")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1FDA")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1FE4")

    label("loc_1FDA")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1FE4")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_2017")
    Jump("loc_24E5")

    label("loc_2017")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_2237")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2203")

    #C0080
    ChrTalk(
        0xB,
        (
            "#1105F哎～？\x01",
            "是那个表情严肃的大叔。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2097")
    OP_63(0x10A, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    label("loc_2097")


    #C0081
    ChrTalk(
        0x10A,
        (
            "#0603F谁、谁是大叔啊。\x02\x03",

            "#0600F我的名字是达德利，\x01",
            "好好记住啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0xB,
        (
            "#1109F嗯！\x01",
            "请多关照，达德利～！\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2125")
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_2125")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_214B")
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_214B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2171")
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_2171")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2197")
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_2197")

    Sleep(1000)

    #C0083
    ChrTalk(
        0x10A,
        (
            "#0603F（……你们几个，\x01",
            "  至少应该教会她对待长辈应有的礼貌啊。）\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x101,
        "#0006F（明、明白了。）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_2232")

    label("loc_2203")


    #C0085
    ChrTalk(
        0xB,
        (
            "#1110F罗伊德，还有达德利！\x01",
            "工作加油呀～！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2232")

    Jump("loc_24E5")

    label("loc_2237")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_2338")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_230E")

    #C0086
    ChrTalk(
        0x103,
        (
            "#0202F琪雅……\x01",
            "你在这里啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x104,
        (
            "#0302F噢，那好像也是\x01",
            "图书馆的书吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0xB,
        (
            "#1100F嗯，这里还留着一本，\x01",
            "所以我就读读看～\x02\x03",

            "#1109F大家工作加油呀～！\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0x101,
        (
            "#0000F嗯，我们一定会\x01",
            "尽快回来的。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_2333")

    label("loc_230E")


    #C0090
    ChrTalk(
        0xB,
        (
            "#1110F嘿嘿嘿，\x01",
            "工作要加油呀～！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2333")

    Jump("loc_24E5")

    label("loc_2338")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_END)), "loc_24E5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCC, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_24BE")

    #C0091
    ChrTalk(
        0xB,
        (
            "#1105F啊～大家\x01",
            "又要出门吗～？\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0x101,
        (
            "#0002F是啊，我们要走了，\x01",
            "晚上之前会回来的。\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x102,
        (
            "#0102F呵呵，要不要买点\x01",
            "什么礼物带给你呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0xB,
        (
            "#1111F嗯～不用啦。\x02\x03",

            "#1109F只要大家能\x01",
            "平安回来就够了哦！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x12C, 1300, 0x36, 0x39, 0xFA, 0x0)
    Sound(892, 0, 100, 0)
    Sleep(1000)

    #C0095
    ChrTalk(
        0x101,
        "#0012F唔……\x02",
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0x102,
        "#0109F啊～……\x02",
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0x103,
        "#0204F透沁心脾的笑脸啊……\x02",
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x104,
        (
            "#0302F哈哈，肃杀紧张的气氛\x01",
            "一下就消失无踪了啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_64(0xB)

    #C0099
    ChrTalk(
        0xB,
        "#1100F嗯～？\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0xCC, 6)
    Jump("loc_24E5")

    label("loc_24BE")


    #C0100
    ChrTalk(
        0xB,
        (
            "#1110F慢走呀～！\x01",
            "大家要小心哦～！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_24E5")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_6_1F06 end

    def Function_7_24ED(): pass

    label("Function_7_24ED")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 1)), scpexpr(EXPR_END)), "loc_2501")
    Call(1, 5)
    Jump("loc_2A3A")

    label("loc_2501")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_252B")

    #C0101
    ChrTalk(
        0xFE,
        "#1200F呜噜噜噜噜噜……\x02",
    )

    CloseMessageWindow()
    Jump("loc_2A3A")

    label("loc_252B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_25FB")

    #C0102
    ChrTalk(
        0xFE,
        "#1200F呜噜噜噜噜噜……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2594")
    OP_63(0x10A, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    label("loc_2594")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_25F6")

    #C0103
    ChrTalk(
        0x10A,
        (
            "#0606F（呼，把它当作警犬了吗……）\x02\x03",

            "#0610F（赛尔盖长官……\x01",
            "  未免太乱来了吧。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)

    label("loc_25F6")

    Jump("loc_2A3A")

    label("loc_25FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_2690")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_266F")

    #C0104
    ChrTalk(
        0xFE,
        "#1200F呜噜噜噜噜噜……\x02",
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0x103,
        (
            "#0202F嗯，那这里\x01",
            "就拜托你了。\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0xC,
        "#1203F呜噜噜噜……！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_268B")

    label("loc_266F")


    #C0107
    ChrTalk(
        0xFE,
        "#1200F呜噜噜噜噜噜……\x02",
    )

    CloseMessageWindow()

    label("loc_268B")

    Jump("loc_2A3A")

    label("loc_2690")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_END)), "loc_2786")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2765")

    #C0108
    ChrTalk(
        0xFE,
        "#1203F呜噜噜噜噜噜……\x02",
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0x103,
        (
            "#0202F『只要有我在，这里的守卫\x01",
            "  就万无一失』，它是这么说的。\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0x101,
        "#0000F哈哈……真是帮大忙了。\x02",
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0x104,
        (
            "#0304F这样的话，必须得不时\x01",
            "给它些肉骨头当作犒劳呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_2781")

    label("loc_2765")


    #C0112
    ChrTalk(
        0xFE,
        "#1200F呜噜噜噜噜噜……\x02",
    )

    CloseMessageWindow()

    label("loc_2781")

    Jump("loc_2A3A")

    label("loc_2786")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_2870")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_284F")

    #C0113
    ChrTalk(
        0xFE,
        "#1200F呜噜噜噜噜噜……\x02",
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0x101,
        (
            "#0000F（虽然态度还是一如既往地高傲……\x01",
            "  但却愿意帮我们守卫支援科呢。）\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0x103,
        (
            "#0202F（嗯，如果有可疑人员擅自进入，\x01",
            "  一定会被它咬住不放呢。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_286B")

    label("loc_284F")


    #C0116
    ChrTalk(
        0xFE,
        "#1200F呜噜噜噜噜噜……\x02",
    )

    CloseMessageWindow()

    label("loc_286B")

    Jump("loc_2A3A")

    label("loc_2870")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_END)), "loc_287E")
    Jump("loc_2A3A")

    label("loc_287E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_288C")
    Jump("loc_2A3A")

    label("loc_288C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_297C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_295B")

    #C0117
    ChrTalk(
        0x153,
        (
            "#1110F蔡特～那我们\x01",
            "就出门啦。\x02\x03",

            "#1109F拜托你留下来看家哦～！\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0xFE,
        "#1200F呜噜噜噜噜噜……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_292A")

    #C0119
    ChrTalk(
        0x103,
        (
            "#0202F它说……\x01",
            "你们就尽管去吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_292A")


    #C0120
    ChrTalk(
        0x101,
        (
            "#0012F哈哈……\x01",
            "看来它完全理解了呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_2977")

    label("loc_295B")


    #C0121
    ChrTalk(
        0xFE,
        "#1200F呜噜噜噜噜噜……\x02",
    )

    CloseMessageWindow()

    label("loc_2977")

    Jump("loc_2A3A")

    label("loc_297C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_29DB")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_29AA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x93, 5)), scpexpr(EXPR_END)), "loc_29A2")
    Call(1, 8)
    Jump("loc_29A5")

    label("loc_29A2")

    Call(1, 19)

    label("loc_29A5")

    Jump("loc_29D6")

    label("loc_29AA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x1, 0x0)"), scpexpr(EXPR_END)), "loc_29BF")
    Call(1, 17)
    Jump("loc_29D6")

    label("loc_29BF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_29D3")
    Call(1, 16)
    Jump("loc_29D6")

    label("loc_29D3")

    Call(1, 8)

    label("loc_29D6")

    Jump("loc_2A3A")

    label("loc_29DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_2A3A")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2A22")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x93, 5)), scpexpr(EXPR_END)), "loc_2A1A")

    #C0122
    ChrTalk(
        0xFE,
        "#1200F呜噜噜噜噜噜……\x02",
    )

    CloseMessageWindow()
    Jump("loc_2A1D")

    label("loc_2A1A")

    Call(1, 19)

    label("loc_2A1D")

    Jump("loc_2A3A")

    label("loc_2A22")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x1, 0x0)"), scpexpr(EXPR_END)), "loc_2A37")
    Call(1, 17)
    Jump("loc_2A3A")

    label("loc_2A37")

    Call(1, 16)

    label("loc_2A3A")

    TalkEnd(0xFE)
    Return()

    # Function_7_24ED end

    def Function_8_2A3E(): pass

    label("Function_8_2A3E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8E, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C91")
    EventBegin(0x0)
    Fade(500)
    OP_68(3640, 1000, 5390, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(340, 0)
    SetCameraDistance(23630, 0)
    SetChrPos(0x101, 2060, 0, 5360, 90)
    SetChrPos(0x102, 2250, 0, 6760, 135)
    SetChrPos(0x103, 3500, 30, 4350, 0)
    SetChrPos(0x104, 4770, 30, 6030, 270)
    SetChrChipByIndex(0xD, 0x6)
    SetChrSubChip(0xD, 0x0)
    BeginChrThread(0xD, 1, 0, 0)
    OP_0D()

    #C0123
    ChrTalk(
        0xD,
        "#1200F#5P呜噜噜……？\x02",
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0x103,
        (
            "#0204F#12P嗯，稍微要出去一下。\x02\x03",

            "#0202F虽然可能会遇到一些\x01",
            "危险……\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0xD,
        (
            "#1203F#5P呜噜噜噜……\x01",
            "……呜噜噜……\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0x101,
        (
            "#0005F#6P那个，缇欧，\x01",
            "它说什么了？\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0x103,
        (
            "#0202F#12P哦，它似乎\x01",
            "明白了我们正在\x01",
            "调查某些事情。\x02\x03",

            "#0204F『适当的时候我会帮忙的，\x01",
            "  不必担心』——它这样说。\x02",
        )
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0x104,
        (
            "#0309F#11P哈哈……这还真是\x01",
            "令人信心倍增的一番话啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0x102,
        (
            "#0102F#5P嗯，像这种时候，\x01",
            "真是相当令人安心的帮手呢。\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, 3500, 30, 4350, 0)
    EndChrThread(0xD, 0x1)
    SetChrChipByIndex(0xD, 0x5)
    SetChrSubChip(0xD, 0x0)
    SetScenarioFlags(0x8E, 4)
    EventEnd(0x5)
    Jump("loc_2D56")

    label("loc_2C91")


    #C0130
    ChrTalk(
        0xFE,
        "#1203F呜噜噜噜……\x02",
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0x103,
        (
            "#0206F『赶快出发吧……\x01",
            "  偶尔欠缺行动力，\x01",
            "  这正是你们的不足之处……』\x02\x03",

            "#0200F……它这样说。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    label("loc_2D56")

    Return()

    # Function_8_2A3E end

    def Function_9_2D57(): pass

    label("Function_9_2D57")

    TalkBegin(0xF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 1)), scpexpr(EXPR_END)), "loc_2D6B")
    Call(1, 5)
    Jump("loc_2ED1")

    label("loc_2D6B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_2ED1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E9E")
    TurnDirection(0xF, 0x0, 0)

    #C0132
    ChrTalk(
        0xF,
        "#6005F啊，各位……\x02",
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0x101,
        (
            "#0000F不好意思，我们要稍微出去一下。\x02\x03",

            "琪雅和蔡特就\x01",
            "拜托你照顾了哦，可以吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0xF,
        (
            "#6000F是的，没问题。\x02\x03",

            "其实是麻烦琪雅和蔡特\x01",
            "陪我玩才对呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0x104,
        (
            "#0309F哈，毕竟是难得的外出日吧？\x01",
            "就尽情玩闹吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0xF,
        (
            "#6002F呵呵……是的，\x01",
            "那我就不客气了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    OP_93(0xF, 0xE1, 0x0)
    Jump("loc_2ED1")

    label("loc_2E9E")


    #C0137
    ChrTalk(
        0xF,
        (
            "#6001F真的可以抚摸它吗……？\x01",
            "（心跳加快）……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2ED1")

    TalkEnd(0xF)
    Return()

    # Function_9_2D57 end

    def Function_10_2ED5(): pass

    label("Function_10_2ED5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2FC7")

    #C0138
    ChrTalk(
        0x10,
        (
            "#0100F啊，小琪雅。\x01",
            "初次出门的感觉怎么样？\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0x153,
        (
            "#1109F嗯，非常开心！\x01",
            "艾莉要是也一起来的话就更好了～\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0x10,
        (
            "#0109F呵呵，因为今天轮到\x01",
            "我留下看家啊……\x02\x03",

            "#0102F下次有机会再\x01",
            "一起出去吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0x153,
        (
            "#1110F嗯，明白了。\x01",
            "约好了哦～！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_30BB")

    label("loc_2FC7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_302C")

    #C0142
    ChrTalk(
        0x10,
        (
            "#0100F罗伊德、缇欧，\x01",
            "要小心啊。\x02\x03",

            "无论如何都绝对不能\x01",
            "在鲁巴彻商会这类地方\x01",
            "露面哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_308C")

    label("loc_302C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_308C")

    #C0143
    ChrTalk(
        0x10,
        (
            "#0100F罗伊德、兰迪，\x01",
            "要小心啊。\x02\x03",

            "无论如何都绝对不能\x01",
            "在鲁巴彻商会这类地方\x01",
            "露面哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_308C")


    #C0144
    ChrTalk(
        0x101,
        (
            "#0000F说的是啊……\x01",
            "我们一定会十分小心的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_30BB")

    TalkEnd(0xFE)
    Return()

    # Function_10_2ED5 end

    def Function_11_30BF(): pass

    label("Function_11_30BF")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3153")
    Jump("loc_319D")

    label("loc_3153")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3173")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_319D")

    label("loc_3173")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3193")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_319D")

    label("loc_3193")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_319D")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3317")

    #C0145
    ChrTalk(
        0x11,
        "#0200F琪雅，你不是出去了么……？\x02",
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0x153,
        (
            "#1110F嗯，但是为了见缇欧，\x01",
            "所以又回来了哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0x11,
        (
            "#0205F………………………………\x02\x03",

            "#0204F琪雅真是很可爱，\x01",
            "请让我稍微抚摸一下吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0x101,
        "#0012F（哈哈哈哈……）\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_32CF")

    #C0149
    ChrTalk(
        0x102,
        (
            "#0102F（缇欧，\x01",
            "  你的心情我能理解哦……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_330F")

    label("loc_32CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_330F")

    #C0150
    ChrTalk(
        0x104,
        (
            "#0309F（连一向冷静自持的阿缇\x01",
            "  都这么疼爱她啊。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_330F")

    SetScenarioFlags(0x1, 1)
    Jump("loc_336C")

    label("loc_3317")


    #C0151
    ChrTalk(
        0x11,
        (
            "#0202F琪雅，要小心车子啊。\x01",
            "一定不要从那两人身边离开。\x02",
        )
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0x153,
        "#1109F嗯，明白啦～！\x02",
    )

    CloseMessageWindow()

    label("loc_336C")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_11_30BF end

    def Function_12_3374(): pass

    label("Function_12_3374")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3408")
    Jump("loc_3452")

    label("loc_3408")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3428")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3452")

    label("loc_3428")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3448")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3452")

    label("loc_3448")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3452")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_35C4")

    #C0153
    ChrTalk(
        0x153,
        (
            "#1110F兰迪，那我就\x01",
            "出门啦～！\x02",
        )
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0x12,
        "#0302F噢！打起精神出发吧！\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_3545")

    #C0155
    ChrTalk(
        0x12,
        (
            "#0300F……罗伊德、大小姐，\x01",
            "阿琪就交给你们啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0x101,
        "#0000F嗯，交给我们好了。\x02",
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0x102,
        (
            "#0100F我们会尽早\x01",
            "回来的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_35BC")

    label("loc_3545")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_35BC")

    #C0158
    ChrTalk(
        0x12,
        (
            "#0300F……罗伊德、阿缇，\x01",
            "阿琪就交给你们啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0x101,
        "#0000F嗯，交给我们好了。\x02",
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0x103,
        (
            "#0202F我们会尽早\x01",
            "回来的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_35BC")

    SetScenarioFlags(0x1, 2)
    Jump("loc_3685")

    label("loc_35C4")


    #C0161
    ChrTalk(
        0x12,
        (
            "#0303F那么，就趁现在\x01",
            "看一看《热辣宝贝》写真集吧。\x02\x03",

            "#0309F这一周以来一直都\x01",
            "紧绷着神经，没法好好放松啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0x101,
        (
            "#0006F（兰迪，在小孩子面前\x01",
            "  看这种不良杂志，是不是有点……）\x02",
        )
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0x153,
        "#1105F？？？\x02",
    )

    CloseMessageWindow()

    label("loc_3685")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_12_3374 end

    def Function_13_368D(): pass

    label("Function_13_368D")

    EventBegin(0x0)
    Fade(500)
    OP_68(63930, 1330, 8550, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25000, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrPos(0x10A, 65489, 0, 8029, 315)
    SetChrPos(0x101, 63000, 0, 6700, 0)
    SetChrPos(0x102, 64300, 0, 6700, 0)
    SetChrPos(0x103, 63200, 0, 5400, 0)
    SetChrPos(0x104, 64500, 0, 5400, 0)
    OP_0D()
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0164
    ChrTalk(
        0x9,
        (
            "#1005F达德利……\x01",
            "你在做什么呢？\x02\x03",

            "#1001F……发生了什么事吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0x10A,
        (
            "#0601F哼，也没什么，\x01",
            "只是被某些人给抢先了一步。\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    #A0166
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "达德利简短地传达了\x01",
            "鲁巴彻商会的状况。\x02",
        )
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0x9,
        (
            "#1001F………………………………\x02\x03",

            "#1003F这可不妙了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0x10A,
        (
            "#0603F总之，我就和这群菜鸟\x01",
            "去鲁巴彻商会调查一下。\x02\x03",

            "#0600F上级那边就由赛尔盖长官……\x02",
        )
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0x104,
        (
            "#0306F呼，恐怕上层那里也\x01",
            "不会有什么动作吧。\x02\x03",

            "#0301F向空港发布炸弹恐吓信息……\x01",
            "这时机未免也太巧了。\x02",
        )
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0x101,
        (
            "#0000F正因如此，所以希望科长\x01",
            "像往常那样，尽量\x01",
            "拖住上边的人……\x02",
        )
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0x9,
        (
            "#1004F明白了，我尽力而为。\x02\x03",

            "#1002F但是，在如今这种状况下，\x01",
            "贸然行动反而有可能会打草惊蛇。\x01",
            "我能做的真的就只有敷衍搪塞而已哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0x102,
        (
            "#0102F嗯，只要能争取到\x01",
            "一些时间就足够了。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x10A, 0xE1, 0x1F4)

    #C0173
    ChrTalk(
        0x10A,
        (
            "#0610F你、你们几个……\x01",
            "都说过会听从我的指挥了，\x01",
            "怎么还这么擅做主张……\x02",
        )
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0x103,
        "#0204F哈，事到如今，再说这些也没用了呢。\x02",
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0x9,
        (
            "#1004F呵呵，不好意思啦，达德利，\x01",
            "这正是我们支援科的行事风格。\x02\x03",

            "#1000F……总之，抓紧时间吧，\x01",
            "这种状况可相当不妙啊。\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, 64000, 30, 7000, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetScenarioFlags(0xCC, 4)
    EventEnd(0x5)
    Return()

    # Function_13_368D end

    def Function_14_3AE6(): pass

    label("Function_14_3AE6")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(254990, 1300, 67290, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(26000, 0)
    SetChrPos(0x101, 251150, 0, 65900, 90)
    SetChrPos(0xEF, 249150, 0, 65900, 90)
    SetChrPos(0x153, 250150, 0, 65500, 90)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xEF, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x153, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetCameraDistance(25000, 3000)
    FadeToBright(500, 0)
    OP_0D()
    BeginChrThread(0x101, 3, 1, 15)
    Sleep(500)
    BeginChrThread(0x153, 3, 1, 15)
    Sleep(500)
    BeginChrThread(0xEF, 3, 1, 15)
    Sleep(500)
    WaitChrThread(0x101, 3)
    WaitChrThread(0xEF, 3)
    WaitChrThread(0x153, 3)

    #C0176
    ChrTalk(
        0x101,
        (
            "#0005F哎，为什么回到了\x01",
            "琪雅的房间啊。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x153, 0x101, 500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_3C4D")

    #C0177
    ChrTalk(
        0x153,
        (
            "#1109F#6P嘿嘿嘿～想给你们看看\x01",
            "我的其它衣服～\x02\x03",

            "#1110F艾莉和缇欧给我买了\x01",
            "各种各样的衣服呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3CAE")

    label("loc_3C4D")


    #C0178
    ChrTalk(
        0x153,
        (
            "#1109F#6P嘿嘿嘿～想给罗伊德看看\x01",
            "我的其它衣服～\x02\x03",

            "#1110F艾莉和缇欧给我买了\x01",
            "各种各样的衣服呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3CAE")


    def lambda_3CB3():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_3CB3)
    Sleep(50)

    def lambda_3CC3():
        TurnDirection(0xFE, 0x153, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3CC3)
    Sleep(250)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_3DCA")

    #C0179
    ChrTalk(
        0x102,
        (
            "#0105F#6P啊，也好呢。\x02\x03",

            "#0109F我正好也想再享受一下\x01",
            "搭配服装的乐趣……\x01",
            "……看，那件衬衣怎么样！\x02",
        )
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0x101,
        (
            "#0011F不、不对，还是等到\x01",
            "下次有机会时再说好啦。\x01",
            "毕竟今天还有正事要办呢。\x02\x03",

            "#0012F（如果放着她们不管，恐怕要\x01",
            "  耗上两个小时左右呢……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3F7D")

    label("loc_3DCA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_3ED2")

    #C0181
    ChrTalk(
        0x103,
        (
            "#0205F#6P啊，这主意不错呢。\x02\x03",

            "#0204F我也想再稍微享受一下\x01",
            "搭配服装的乐趣……\x01",
            "那顶绒线帽也让人很难舍弃啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0x101,
        (
            "#0011F不、不对！这种事情\x01",
            "还是以后有机会再说吧。\x01",
            "毕竟今天还有正事要办呢。\x02\x03",

            "#0012F（如果放着她们不管，恐怕要\x01",
            "  耗上两个小时左右呢……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3F7D")

    label("loc_3ED2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_3F7D")

    #C0183
    ChrTalk(
        0x104,
        (
            "#0309F#6P噢～那还真是令人期待啊。\x02\x03",

            "#0300F不过，还是下次再说吧？\x02\x03",

            "#0306F要是把大小姐和阿缇给引来的话，\x01",
            "肯定又会兴致勃勃地玩个没完吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0x101,
        "#0012F哈哈哈哈……\x02",
    )

    CloseMessageWindow()

    label("loc_3F7D")

    OP_93(0x101, 0x0, 0x1F4)
    Sleep(500)
    OP_93(0x101, 0x13B, 0x1F4)
    Sleep(500)
    OP_93(0x101, 0x0, 0x1F4)
    Sleep(500)

    #C0185
    ChrTalk(
        0x101,
        (
            "#0000F嗯，不过，总算是比较像样了啊。\x02\x03",

            "虽然只是间空房，但已经打扫完毕，\x01",
            "最基本的家具也拜托\x01",
            "艾莉帮忙找来了。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4010():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_4010)
    Sleep(200)

    def lambda_4020():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x153, 1, lambda_4020)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_4167")

    #C0186
    ChrTalk(
        0x102,
        (
            "#0102F#12P呵呵……只是拜托家里将原来的\x01",
            "一些旧东西送过来了而已。\x02\x03",

            "#0106F因为都是我父母用过的东西，\x01",
            "所以全是大人的式样，不好意思了。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_40BE():
        TurnDirection(0xFE, 0x153, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_40BE)
    Sleep(250)

    #C0187
    ChrTalk(
        0x101,
        (
            "#0002F不，这就已经很好了。\x02\x03",

            "#0004F（将琪雅的身份查清之后，\x01",
            "  肯定就要把她送还到\x01",
            "  父母那里了……）\x02\x03",

            "（在那之前，希望尽可能\x01",
            "  多为她做一些事情啊。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_43B4")

    label("loc_4167")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_428A")

    #C0188
    ChrTalk(
        0x103,
        (
            "#0202F#12P是艾莉前辈家中的\x01",
            "旧物哦。\x02\x03",

            "#0204F对琪雅来说，似乎是稍微大了一点，\x01",
            "不过也算不上是什么大问题。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_41E1():
        TurnDirection(0xFE, 0x153, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_41E1)
    Sleep(250)

    #C0189
    ChrTalk(
        0x101,
        (
            "#0002F嗯，这就已经很好了。\x02\x03",

            "#0004F（将琪雅的身份查清之后，\x01",
            "  肯定就要把她送还到\x01",
            "  父母那里了……）\x02\x03",

            "（在那之前，希望尽可能\x01",
            "  多为她做一些事情啊。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_43B4")

    label("loc_428A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_43B4")

    #C0190
    ChrTalk(
        0x104,
        (
            "#0300F#12P似乎是大小姐家里的旧东西啊。\x02\x03",

            "#0309F对阿琪来说，尺寸\x01",
            "好像是有点偏大了，\x01",
            "不过也无所谓，不会有什么大问题。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4310():
        TurnDirection(0xFE, 0x153, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4310)
    Sleep(250)

    #C0191
    ChrTalk(
        0x101,
        (
            "#0002F嗯，这就已经很好了。\x02\x03",

            "#0004F（将琪雅的身份查清之后，\x01",
            "  肯定就要把她送还到\x01",
            "  父母那里了……）\x02\x03",

            "（在那之前，希望尽可能\x01",
            "  多为她做一些事情啊。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_43B4")

    SetChrPos(0x0, 255350, 0, 64650, 0)
    SetScenarioFlags(0xD8, 6)
    EventEnd(0x5)
    Return()

    # Function_14_3AE6 end

    def Function_15_43CB(): pass

    label("Function_15_43CB")


    def lambda_43D0():
        OP_97(0xFE, 0x1388, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_43D0)

    def lambda_43EA():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_43EA)
    WaitChrThread(0xFE, 1)

    def lambda_43FF():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_43FF)
    Return()

    # Function_15_43CB end

    def Function_16_4408(): pass

    label("Function_16_4408")


    #C0192
    ChrTalk(
        0x101,
        (
            "#0000F啊，在这里呢。\x02\x03",

            "副局长的事情\x01",
            "就拜托蔡特试试吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0x103,
        (
            "#0200F说的也对，凭着蔡特的嗅觉，\x01",
            "我想一定可以查明\x01",
            "副局长昨晚的正确行进路线呢。\x02\x03",

            "将事情做个大概说明，\x01",
            "请求它的协助吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    EventBegin(0x0)
    LoadChrToIndex("apl/ch50116.itc", 0x1E)
    OP_68(2940, 1200, 4980, 0)
    MoveCamera(42, 28, 0, 0)
    OP_6E(340, 0)
    SetCameraDistance(24570, 0)
    SetChrPos(0x101, 2250, 30, 5500, 90)
    SetChrPos(0x102, 2500, 30, 6850, 135)
    SetChrPos(0x103, 3500, 30, 4500, 0)
    SetChrPos(0x104, 3000, 30, 3150, 0)
    OP_93(0xD, 0xB4, 0x0)
    SetChrName("")

    #A0194
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "罗伊德等人将事情的情况\x01",
            "告知蔡特，并请求它提供协助。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToBright(2000, 0)
    OP_0D()

    #C0195
    ChrTalk(
        0x101,
        (
            "#6P#0003F事情就是这样，\x01",
            "希望你能助我们一臂之力……\x02\x03",

            "#0012F……那个，蔡特，\x01",
            "你能听明白吧？\x02",
        )
    )

    CloseMessageWindow()
    Sound(848, 0, 100, 0)
    SetChrChipByIndex(0xD, 0x1E)
    SetChrSubChip(0xD, 0x0)
    OP_A1(0xD, 0x4E2, 0x8, 0x0, 0x1, 0x1, 0x1, 0x1, 0x2, 0x3, 0x4)
    SetChrChipByIndex(0xD, 0x5)
    SetChrSubChip(0xD, 0x0)
    OP_0D()

    #C0196
    ChrTalk(
        0xD,
        (
            "#11P#1200F呜噜噜噜噜……\x02\x03",

            "呜噜噜噜噜……！\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0xD, 1, 0, 0)

    #C0197
    ChrTalk(
        0x104,
        "#12P#0305F哎，反应好像很恶劣啊？\x02",
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0x102,
        "#6P#0100F是不是不愿意帮忙呢……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 500)

    #C0199
    ChrTalk(
        0x103,
        (
            "#12P#0200F不，没问题的。\x02\x03",

            "#0203F还是一点长进都没有，一群不中用的家伙……\x01",
            "虽然它这样说，\x01",
            "但好像还是愿意提供协助。\x02\x03",

            "#0200F罗伊德前辈，把副局长的\x01",
            "手帕给它闻闻吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0x101,
        "#6P#0000F嗯，好，就是这个。\x02",
    )

    CloseMessageWindow()
    OP_95(0x101, 2900, 850, 5000, 2000, 0x0)
    Sleep(500)
    OP_96(0x101, 0x8CA, 0x0, 0x157C, 0x7D0, 0x0)

    def lambda_4796():
        OP_93(0x101, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4796)

    def lambda_47A3():
        OP_93(0x103, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_47A3)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x103, 1)

    #C0201
    ChrTalk(
        0x103,
        (
            "#12P#0200F蔡特，\x01",
            "这就是目标对象的气味。\x02\x03",

            "记住了吗？\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    EndChrThread(0xD, 0x1)
    SetChrChipByIndex(0xD, 0x2)
    SetChrSubChip(0xD, 0x0)
    SetChrFlags(0xC, 0x1)
    OP_0D()

    #C0202
    ChrTalk(
        0xD,
        (
            "#5P#1203F（嗅嗅）………\x02\x03",

            "#1200F……呜呜，呜噜噜噜噜……\x02",
        )
    )

    CloseMessageWindow()

    #C0203
    ChrTalk(
        0x103,
        "#12P#0200F『一股卑鄙小人的味道』。\x02",
    )

    CloseMessageWindow()

    #C0204
    ChrTalk(
        0xD,
        "#5P#1200F呜噜噜噜噜……！\x02",
    )

    CloseMessageWindow()

    #C0205
    ChrTalk(
        0x103,
        (
            "#12P#0200F『没办法，只能帮帮你们了……\x01",
            "  想出发的时候就叫我一声吧！』\x01",
            "它这样说。\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    SetChrChipByIndex(0xD, 0x5)
    SetChrSubChip(0xD, 0x0)
    ClearChrFlags(0xC, 0x1)
    OP_0D()

    #C0206
    ChrTalk(
        0x104,
        (
            "#12P#0306F哎呀呀，一点都没变，\x01",
            "还是这么喜欢摆架子啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0207
    ChrTalk(
        0x102,
        (
            "#6P#0100F呵呵，不过，带着警犬去进行调查，\x01",
            "不是很有警察的样子吗？\x02\x03",

            "罗伊德，这次的行动似乎会花费很多时间，\x01",
            "做好准备之后再出发吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0208
    ChrTalk(
        0x101,
        "#6P#0000F啊，是啊。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_D5(0x1E)
    OP_68(3500, 1030, 4500, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(340, 0)
    SetCameraDistance(27500, 0)
    SetChrPos(0x0, 3500, 0, 4500, 0)
    SetChrPos(0x1, 3500, 0, 4500, 0)
    SetChrPos(0x2, 3500, 0, 4500, 0)
    SetChrPos(0x3, 3500, 0, 4500, 0)
    OP_29(0x15, 0x1, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    EventEnd(0x5)
    Return()

    # Function_16_4408 end

    def Function_17_4A5B(): pass

    label("Function_17_4A5B")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4A65")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4C53")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "对话\x01",          # 0
            "请求同行\x01",      # 1
            "放弃\x01",          # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_4ABF"),
        (1, "loc_4B65"),
        (SWITCH_DEFAULT, "loc_4C4E"),
    )


    label("loc_4ABF")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0209
    ChrTalk(
        0xD,
        (
            "#1200F呜噜噜噜……\x01",
            "呜噜噜噜噜噜……\x02",
        )
    )

    CloseMessageWindow()

    #C0210
    ChrTalk(
        0x103,
        (
            "#0200F『如果想找什么结婚戒指的话，\x01",
            "  就来请求我和你们同行吧。』\x02\x03",

            "『可以暂时陪你们一阵。』\x01",
            "……它这么说。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4C4E")

    label("loc_4B65")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x1, 0x1)"), scpexpr(EXPR_END)), "loc_4B9E")

    #C0211
    ChrTalk(
        0x101,
        (
            "#0000F好，那我们\x01",
            "这就去欢乐街吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4C1F")

    label("loc_4B9E")


    #C0212
    ChrTalk(
        0x101,
        (
            "#0000F好，那我们\x01",
            "这就去欢乐街吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0213
    ChrTalk(
        0x102,
        (
            "#0100F副局长离开『巴鲁卡』的时候，\x01",
            "戒指好像还戴在他的手上呢……\x01",
            "就先从那附近找起吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4C1F")

    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    AddParty(0x1B, 0xFF, 0xFF)
    SetScenarioFlags(0x93, 6)
    OP_C7(0x0, 0x1000)
    SetScenarioFlags(0x5C, 5)
    NewScene("c0400", 0, 0, 0)
    IdleLoop()
    Jump("loc_4C4E")

    label("loc_4C4E")

    Jump("loc_4A65")

    label("loc_4C53")

    Return()

    # Function_17_4A5B end

    def Function_18_4C54(): pass

    label("Function_18_4C54")

    EventBegin(0x1)
    FadeToDark(0, 0, -1)
    RemoveParty(0x1B, 0x0)
    ClearScenarioFlags(0x93, 6)
    OP_C7(0x1, 0x1000)
    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    OP_68(3500, 1030, 4500, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(340, 0)
    SetCameraDistance(27500, 0)
    SetChrPos(0x0, 3500, 0, 4500, 0)
    SetChrPos(0x1, 3500, 0, 4500, 0)
    SetChrPos(0x2, 3500, 0, 4500, 0)
    SetChrPos(0x3, 3500, 0, 4500, 0)
    FadeToBright(500, 0)
    OP_0D()
    EventEnd(0x4)
    Return()

    # Function_18_4C54 end

    def Function_19_4CF3(): pass

    label("Function_19_4CF3")


    #C0214
    ChrTalk(
        0x101,
        (
            "#0000F蔡特，今天真是帮大忙啦。\x01",
            "你那敏锐的嗅觉真是名不虚传。\x02",
        )
    )

    CloseMessageWindow()

    #C0215
    ChrTalk(
        0x103,
        (
            "#0200F嗯，超乎想象呢。\x02\x03",

            "在以后的物证调查之类工作中\x01",
            "似乎也能发挥作用呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0216
    ChrTalk(
        0xD,
        "#1200F呜噜噜噜……\x02",
    )

    CloseMessageWindow()

    #C0217
    ChrTalk(
        0x103,
        (
            "#0200F『下次找我时最好接些\x01",
            "  稍微像样一点的工作！』\x01",
            "……它这样说。\x02",
        )
    )

    CloseMessageWindow()

    #C0218
    ChrTalk(
        0x104,
        "#0300F哈哈，被它批评了吗。\x02",
    )

    CloseMessageWindow()

    #C0219
    ChrTalk(
        0x102,
        (
            "#0100F这次它可是比我们\x01",
            "还要活跃啊。\x02\x03",

            "今后也请多关照啦，\x01",
            "蔡特。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x93, 5)
    Return()

    # Function_19_4CF3 end

    def Function_20_4E49(): pass

    label("Function_20_4E49")

    EventBegin(0x0)
    Fade(500)
    OP_68(15900, 1550, 9800, 0)
    MoveCamera(45, 18, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(24500, 0)
    SetChrPos(0x101, 15200, 850, 9800, 45)
    SetChrPos(0x102, 15900, 850, 9100, 45)
    SetChrPos(0x103, 14100, 850, 9500, 45)
    SetChrPos(0x104, 15600, 850, 8000, 45)
    OP_0D()

    #C0220
    ChrTalk(
        0x101,
        (
            "#0000F#6P那么……\x01",
            "只要用这个终端机将报告\x01",
            "发送给警察局总部就可以了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0x103,
        (
            "#0202F#6P是的，\x01",
            "赶快试试吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_E3(0xA)
    FadeToDark(300, 0, -1)
    OP_0D()
    OP_E3(0x5)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_49()

    label("loc_4F4A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5442")
    RunExpression(0x3, (scpexpr(EXPR_EXEC_OP, "OP_E3(0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_END)),
        (0, "loc_4F7D"),
        (1, "loc_4FA3"),
        (255, "loc_53B5"),
        (SWITCH_DEFAULT, "loc_543D"),
    )


    label("loc_4F7D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1, 0x0, 0x20)"), scpexpr(EXPR_END)), "loc_4F99")
    OP_2B(0x1, 0x2, 0x3, 0x35, 0xFFFF)
    Jump("loc_4F9E")

    label("loc_4F99")

    OP_2B(0x1, 0xFFFF)

    label("loc_4F9E")

    Jump("loc_543D")

    label("loc_4FA3")

    SetMapFlags(0x40000000)
    OP_E3(0x7)
    Sleep(500)
    SetChrName("接待小姐芙兰")
    Sound(2062, 255, 100, 0)    #voice#Fran

    #A0222
    AnonymousTalk(
        0xFF,
        "#28A您好，这里是克洛斯贝尔警察局～！\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_E3(0x4)"), scpexpr(EXPR_END)), "loc_5204")
    Sound(2067, 255, 100, 0)    #voice#Fran

    #A0223
    AnonymousTalk(
        0xFF,
        "#27A那么，我将对各位的报告进行处理～\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    RunExpression(0x6, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x2F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_E3(0xC)
    Jc((scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x2F), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_519D")
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x2F), scpexpr(EXPR_END)),
        (14, "loc_504E"),
        (13, "loc_5088"),
        (12, "loc_50BE"),
        (SWITCH_DEFAULT, "loc_50F6"),
    )


    label("loc_504E")

    Sound(2075, 255, 100, 0)    #voice#Fran

    #A0224
    AnonymousTalk(
        0xFF,
        (
            "#36A级别１ｓｔ――\x01",
            "罗伊德警官，实在太厉害了！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5136")

    label("loc_5088")

    Sound(2074, 255, 100, 0)    #voice#Fran

    #A0225
    AnonymousTalk(
        0xFF,
        (
            "#35A级别２ｎｄ──\x01",
            "罗伊德警官，好厉害呢！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5136")

    label("loc_50BE")

    Sound(2073, 255, 100, 0)    #voice#Fran

    #A0226
    AnonymousTalk(
        0xFF,
        (
            "#32A级别３ｒｄ──\x01",
            "罗伊德警官，做得很好啊！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5136")

    label("loc_50F6")

    Sound(2073, 255, 100, 0)    #voice#Fran

    #A0227
    AnonymousTalk(
        0xFF,
        (
            "#32A级别３ｒｄ──（测试）\x01",
            "罗伊德警官，做得很好啊！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5136")

    label("loc_5136")

    Sound(2076, 255, 100, 0)    #voice#Fran

    #A0228
    AnonymousTalk(
        0xFF,
        (
            "#31A奖励物品\x01",
            "也会马上给你们送去的～！\x02",
        )
    )

    CloseMessageWindow()
    Sound(2077, 255, 100, 0)    #voice#Fran

    #A0229
    AnonymousTalk(
        0xFF,
        (
            "#34A大家辛苦了～！\x01",
            "以后也请随时来向我报告～\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_51FC")

    label("loc_519D")

    Sound(2078, 255, 100, 0)    #voice#Fran

    #A0230
    AnonymousTalk(
        0xFF,
        "#16A报告就是以上这些吧～\x02",
    )

    CloseMessageWindow()
    Sound(2079, 255, 100, 0)    #voice#Fran

    #A0231
    AnonymousTalk(
        0xFF,
        (
            "#37A那么，以后如果完成了新的委托，\x01",
            "请再来向我报告吧～\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    label("loc_51FC")

    SetScenarioFlags(0x1, 5)
    Jump("loc_52BC")

    label("loc_5204")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_END)), "loc_526F")
    Sound(2063, 255, 100, 0)    #voice#Fran

    #A0232
    AnonymousTalk(
        0xFF,
        (
            "#32A哎……\x01",
            "刚才已经报告过了哦。        \x02",
        )
    )

    CloseMessageWindow()
    Sound(2064, 255, 100, 0)    #voice#Fran

    #A0233
    AnonymousTalk(
        0xFF,
        "#32A等完成了新的委托之后再来报告吧～\x07\x00\x02",
    )

    CloseMessageWindow()
    Jump("loc_52BC")

    label("loc_526F")

    Sound(2065, 255, 100, 0)    #voice#Fran

    #A0234
    AnonymousTalk(
        0xFF,
        (
            "#37A哎，好像并没有可以\x01",
            "报告的委托哦～\x02",
        )
    )

    CloseMessageWindow()
    Sound(2066, 255, 100, 0)    #voice#Fran

    #A0235
    AnonymousTalk(
        0xFF,
        "#16A请下次再来报告吧～\x07\x00\x02",
    )

    CloseMessageWindow()

    label("loc_52BC")

    OP_57(0x0)
    OP_E3(0x8)
    ClearMapFlags(0x40000000)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1, 0x1, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_53B0")
    Sleep(1000)

    #A0236
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0002F原来如此……\x01",
            "转瞬之间就完成了啊。\x02",
        )
    )

    CloseMessageWindow()

    #A0237
    AnonymousTalk(
        0x102,
        (
            "#0109F今后如果完成了新的委托，\x01",
            "再用同样的方式进行报告就可以了。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)
    Sound(824, 0, 100, 0)
    Sleep(1000)

    #A0238
    AnonymousTalk(
        0x103,
        (
            "#0205F啊……\x01",
            "新的支援请求好像\x01",
            "又发送过来了。\x02\x03",

            "#0202F慎重起见，还是确认一下吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x1, 0x1, 0x2)

    label("loc_53B0")

    Jump("loc_543D")

    label("loc_53B5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1, 0x1, 0x2)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_2A(0x35, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5438")

    #A0239
    AnonymousTalk(
        0x103,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0203F新的支援请求好像\x01",
            "又发送过来了。\x02\x03",

            "#0200F慎重起见，还是确认一下吧。\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5438")

    Jump("loc_543D")

    label("loc_543D")

    Jump("loc_4F4A")

    label("loc_5442")

    OP_E3(0x6)
    FadeToBright(300, 0)
    OP_0D()
    OP_E3(0xB)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1, 0x1, 0x2)"), scpexpr(EXPR_END)), "loc_5465")
    Call(1, 21)
    Jump("loc_5467")

    label("loc_5465")

    EventEnd(0x5)

    label("loc_5467")

    Return()

    # Function_20_4E49 end

    def Function_21_5468(): pass

    label("Function_21_5468")

    Sleep(500)

    #C0240
    ChrTalk(
        0x104,
        (
            "#0301F#12P好像发来了不少任务呢……\x01",
            "地下空间又出现魔兽了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0241
    ChrTalk(
        0x102,
        (
            "#0101F这就是所谓的『通缉魔兽』吧。\x02\x03",

            "这种魔兽好像一般都是由协会的\x01",
            "游击士负责讨伐的……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_93(0x101, 0xB4, 0x1F4)
    Sleep(300)

    #C0242
    ChrTalk(
        0x101,
        (
            "#0003F#5P……那个，各位。\x02\x03",

            "#0001F我们来试着自己对付\x01",
            "这个『通缉魔兽』吧，如何？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_55BB():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_55BB)
    Sleep(50)

    def lambda_55CB():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_55CB)
    Sleep(50)

    def lambda_55DB():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_55DB)
    Sleep(300)

    #C0243
    ChrTalk(
        0x102,
        "#0105F那个……\x02",
    )

    CloseMessageWindow()

    #C0244
    ChrTalk(
        0x104,
        "#0305F#12P是要为昨天的事情出口气吗？\x02",
    )

    CloseMessageWindow()

    #C0245
    ChrTalk(
        0x101,
        (
            "#0006F#5P嗯，那时多亏了\x01",
            "亚里欧斯·马克莱因的相救，\x01",
            "不过……\x02\x03",

            "#0001F如果我们事先做好充足的准备，\x01",
            "凭自己的力量应该也能将它击退的。\x02\x03",

            "毕竟是工作的第一天，机会难得，\x01",
            "就当是开个好头，怎么样？\x02",
        )
    )

    CloseMessageWindow()

    #C0246
    ChrTalk(
        0x102,
        "#0103F嗯～确实呢……\x02",
    )

    CloseMessageWindow()

    #C0247
    ChrTalk(
        0x103,
        (
            "#0204F#6P虽然很麻烦，\x01",
            "但这么说也有道理呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0248
    ChrTalk(
        0x104,
        (
            "#0304F#12P这主意也不错嘛。\x01",
            "而且毕竟被抢了风头，要把面子挽回才行。\x02\x03",

            "#0300F那么，准备完毕之后，\x01",
            "我们就去车站前的入口吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0249
    ChrTalk(
        0x101,
        "#0000F#5P就这么办吧！\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(828, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0250
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "在支援请求中，会有一些紧急度较高，\x01",
            "必须要接受的任务。\x02",
        )
    )

    CloseMessageWindow()

    #A0251
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "这种任务都会附有『紧急』的标示，\x01",
            "只有将其完成，才能使主线剧情继续进展。\x02",
        )
    )

    CloseMessageWindow()

    #A0252
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "除此之外的支援请求\x01",
            "并无全部完成的必要，\x01",
            "但若超过期限则会失效，还请注意。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_68(15730, 1850, 9350, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(340, 0)
    SetCameraDistance(27500, 0)
    SetChrPos(0x0, 15730, 850, 9350, 225)
    SetChrPos(0x1, 15730, 850, 9350, 225)
    SetChrPos(0x2, 15730, 850, 9350, 225)
    SetChrPos(0x3, 15730, 850, 9350, 225)
    OP_29(0x3D, 0x1, 0x3)
    EventEnd(0x5)
    Return()

    # Function_21_5468 end

    def Function_22_5943(): pass

    label("Function_22_5943")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    SetMapObjFrame(0xFF, "01", 0x1, 0x1)
    OP_68(-1560, 1330, 122920, 0)
    MoveCamera(38, 16, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(21500, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_599B")
    SetChrFlags(0x0, 0x8)

    label("loc_599B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_59AE")
    SetChrFlags(0x1, 0x8)

    label("loc_59AE")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_59C1")
    SetChrFlags(0x2, 0x8)

    label("loc_59C1")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_59D4")
    SetChrFlags(0x3, 0x8)

    label("loc_59D4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_59E7")
    SetChrFlags(0x4, 0x8)

    label("loc_59E7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_59FA")
    SetChrFlags(0x5, 0x8)

    label("loc_59FA")

    ClearChrFlags(0x101, 0x8)
    SetChrPos(0x101, -1830, 30, 122400, 270)
    FadeToBright(500, 0)
    OP_0D()

    #C0253
    ChrTalk(
        0x101,
        "#0000F放在这里就可以了吧。\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    SetChrName("")
    Sound(828, 0, 100, 0)

    #A0254
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "罗伊德的房间中\x01",
            "放入了新的家具。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SubItemNumber(0x350, 1)
    SetScenarioFlags(0x50, 6)
    OP_66(0x7, 0x1)
    Call(1, 30)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5A92")
    ClearChrFlags(0x0, 0x8)

    label("loc_5A92")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5AA5")
    ClearChrFlags(0x1, 0x8)

    label("loc_5AA5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5AB8")
    ClearChrFlags(0x2, 0x8)

    label("loc_5AB8")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5ACB")
    ClearChrFlags(0x3, 0x8)

    label("loc_5ACB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5ADE")
    ClearChrFlags(0x4, 0x8)

    label("loc_5ADE")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5AF1")
    ClearChrFlags(0x5, 0x8)

    label("loc_5AF1")

    Call(1, 39)
    SetChrPos(0x0, 20, 30, 121010, 0)
    EventEnd(0x5)
    Return()

    # Function_22_5943 end

    def Function_23_5B08(): pass

    label("Function_23_5B08")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    SetMapObjFrame(0xFF, "02", 0x1, 0x1)
    OP_68(-2440, 1300, 129810, 0)
    MoveCamera(36, 14, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(20500, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5B60")
    SetChrFlags(0x0, 0x8)

    label("loc_5B60")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5B73")
    SetChrFlags(0x1, 0x8)

    label("loc_5B73")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5B86")
    SetChrFlags(0x2, 0x8)

    label("loc_5B86")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5B99")
    SetChrFlags(0x3, 0x8)

    label("loc_5B99")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5BAC")
    SetChrFlags(0x4, 0x8)

    label("loc_5BAC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5BBF")
    SetChrFlags(0x5, 0x8)

    label("loc_5BBF")

    ClearChrFlags(0x101, 0x8)
    SetChrPos(0x101, -1940, 0, 128820, 0)
    FadeToBright(500, 0)
    OP_0D()

    #C0255
    ChrTalk(
        0x101,
        "#0000F放在这里就可以了吧。\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    SetChrName("")
    Sound(828, 0, 100, 0)

    #A0256
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "罗伊德的房间中\x01",
            "放入了新的家具。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SubItemNumber(0x351, 1)
    SetScenarioFlags(0x50, 7)
    OP_66(0x8, 0x1)
    Call(1, 30)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5C57")
    ClearChrFlags(0x0, 0x8)

    label("loc_5C57")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5C6A")
    ClearChrFlags(0x1, 0x8)

    label("loc_5C6A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5C7D")
    ClearChrFlags(0x2, 0x8)

    label("loc_5C7D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5C90")
    ClearChrFlags(0x3, 0x8)

    label("loc_5C90")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5CA3")
    ClearChrFlags(0x4, 0x8)

    label("loc_5CA3")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5CB6")
    ClearChrFlags(0x5, 0x8)

    label("loc_5CB6")

    Call(1, 39)
    SetChrPos(0x0, 20, 30, 121010, 0)
    EventEnd(0x5)
    Return()

    # Function_23_5B08 end

    def Function_24_5CCD(): pass

    label("Function_24_5CCD")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    SetMapObjFrame(0xFF, "05", 0x1, 0x1)
    OP_68(153830, 1330, 130810, 0)
    MoveCamera(29, 16, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(23500, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5D25")
    SetChrFlags(0x0, 0x8)

    label("loc_5D25")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5D38")
    SetChrFlags(0x1, 0x8)

    label("loc_5D38")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5D4B")
    SetChrFlags(0x2, 0x8)

    label("loc_5D4B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5D5E")
    SetChrFlags(0x3, 0x8)

    label("loc_5D5E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5D71")
    SetChrFlags(0x4, 0x8)

    label("loc_5D71")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5D84")
    SetChrFlags(0x5, 0x8)

    label("loc_5D84")

    ClearChrFlags(0x102, 0x8)
    SetChrPos(0x102, 155090, 30, 129770, 344)
    FadeToBright(500, 0)
    OP_0D()

    #C0257
    ChrTalk(
        0x102,
        "#0100F放在这里就好了吧。\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    SetChrName("")
    Sound(828, 0, 100, 0)

    #A0258
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "艾莉的房间中\x01",
            "放入了新的家具。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SubItemNumber(0x352, 1)
    SetScenarioFlags(0x51, 0)
    OP_66(0x9, 0x1)
    Call(1, 30)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5E18")
    ClearChrFlags(0x0, 0x8)

    label("loc_5E18")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5E2B")
    ClearChrFlags(0x1, 0x8)

    label("loc_5E2B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5E3E")
    ClearChrFlags(0x2, 0x8)

    label("loc_5E3E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5E51")
    ClearChrFlags(0x3, 0x8)

    label("loc_5E51")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5E64")
    ClearChrFlags(0x4, 0x8)

    label("loc_5E64")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5E77")
    ClearChrFlags(0x5, 0x8)

    label("loc_5E77")

    Call(1, 39)
    SetChrPos(0x0, 155990, 30, 120980, 0)
    EventEnd(0x5)
    Return()

    # Function_24_5CCD end

    def Function_25_5E8E(): pass

    label("Function_25_5E8E")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    SetMapObjFrame(0xFF, "06", 0x1, 0x1)
    SetMapObjFrame(0xFF, "06a", 0x1, 0x1)
    OP_68(154150, 1330, 121920, 0)
    MoveCamera(53, 18, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(21500, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5EF1")
    SetChrFlags(0x0, 0x8)

    label("loc_5EF1")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5F04")
    SetChrFlags(0x1, 0x8)

    label("loc_5F04")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5F17")
    SetChrFlags(0x2, 0x8)

    label("loc_5F17")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5F2A")
    SetChrFlags(0x3, 0x8)

    label("loc_5F2A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5F3D")
    SetChrFlags(0x4, 0x8)

    label("loc_5F3D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5F50")
    SetChrFlags(0x5, 0x8)

    label("loc_5F50")

    ClearChrFlags(0x102, 0x8)
    SetChrPos(0x102, 154150, 30, 121920, 0)
    FadeToBright(500, 0)
    OP_0D()

    #C0259
    ChrTalk(
        0x102,
        "#0100F放在这里就好了吧。\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    SetChrName("")
    Sound(828, 0, 100, 0)

    #A0260
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "艾莉的房间中\x01",
            "放入了新的家具。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SubItemNumber(0x353, 1)
    SetScenarioFlags(0x51, 1)
    OP_66(0xA, 0x1)
    Call(1, 30)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5FE4")
    ClearChrFlags(0x0, 0x8)

    label("loc_5FE4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5FF7")
    ClearChrFlags(0x1, 0x8)

    label("loc_5FF7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_600A")
    ClearChrFlags(0x2, 0x8)

    label("loc_600A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_601D")
    ClearChrFlags(0x3, 0x8)

    label("loc_601D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6030")
    ClearChrFlags(0x4, 0x8)

    label("loc_6030")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6043")
    ClearChrFlags(0x5, 0x8)

    label("loc_6043")

    Call(1, 39)
    SetChrPos(0x0, 155990, 30, 120980, 0)
    EventEnd(0x5)
    Return()

    # Function_25_5E8E end

    def Function_26_605A(): pass

    label("Function_26_605A")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    SetMapObjFrame(0xFF, "07", 0x1, 0x1)
    OP_68(208030, 1330, 127590, 0)
    MoveCamera(25, 17, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(23500, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_60B2")
    SetChrFlags(0x0, 0x8)

    label("loc_60B2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_60C5")
    SetChrFlags(0x1, 0x8)

    label("loc_60C5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_60D8")
    SetChrFlags(0x2, 0x8)

    label("loc_60D8")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_60EB")
    SetChrFlags(0x3, 0x8)

    label("loc_60EB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_60FE")
    SetChrFlags(0x4, 0x8)

    label("loc_60FE")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6111")
    SetChrFlags(0x5, 0x8)

    label("loc_6111")

    ClearChrFlags(0x103, 0x8)
    SetChrPos(0x103, 208030, 30, 127590, 0)
    FadeToBright(500, 0)
    OP_0D()

    #C0261
    ChrTalk(
        0x103,
        "#0200F就放在这里吧。\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    SetChrName("")
    Sound(828, 0, 100, 0)

    #A0262
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "缇欧的房间中\x01",
            "放入了新的家具。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SubItemNumber(0x354, 1)
    SetScenarioFlags(0x51, 2)
    OP_66(0xB, 0x1)
    Call(1, 30)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_61A1")
    ClearChrFlags(0x0, 0x8)

    label("loc_61A1")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_61B4")
    ClearChrFlags(0x1, 0x8)

    label("loc_61B4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_61C7")
    ClearChrFlags(0x2, 0x8)

    label("loc_61C7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_61DA")
    ClearChrFlags(0x3, 0x8)

    label("loc_61DA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_61ED")
    ClearChrFlags(0x4, 0x8)

    label("loc_61ED")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6200")
    ClearChrFlags(0x5, 0x8)

    label("loc_6200")

    Call(1, 39)
    SetChrPos(0x0, 206030, 30, 121140, 0)
    EventEnd(0x5)
    Return()

    # Function_26_605A end

    def Function_27_6217(): pass

    label("Function_27_6217")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    SetMapObjFrame(0xFF, "08", 0x1, 0x1)
    OP_68(207830, 1330, 127120, 0)
    MoveCamera(56, 17, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(23500, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_626F")
    SetChrFlags(0x0, 0x8)

    label("loc_626F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6282")
    SetChrFlags(0x1, 0x8)

    label("loc_6282")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6295")
    SetChrFlags(0x2, 0x8)

    label("loc_6295")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_62A8")
    SetChrFlags(0x3, 0x8)

    label("loc_62A8")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_62BB")
    SetChrFlags(0x4, 0x8)

    label("loc_62BB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_62CE")
    SetChrFlags(0x5, 0x8)

    label("loc_62CE")

    ClearChrFlags(0x103, 0x8)
    SetChrPos(0x103, 207830, 30, 127120, 107)
    FadeToBright(500, 0)
    OP_0D()

    #C0263
    ChrTalk(
        0x103,
        "#0200F就放在这里吧。\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    SetChrName("")
    Sound(828, 0, 100, 0)

    #A0264
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "缇欧的房间中\x01",
            "放入了新的家具。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SubItemNumber(0x355, 1)
    SetScenarioFlags(0x51, 3)
    OP_66(0xC, 0x1)
    Call(1, 30)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_635E")
    ClearChrFlags(0x0, 0x8)

    label("loc_635E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6371")
    ClearChrFlags(0x1, 0x8)

    label("loc_6371")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6384")
    ClearChrFlags(0x2, 0x8)

    label("loc_6384")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6397")
    ClearChrFlags(0x3, 0x8)

    label("loc_6397")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_63AA")
    ClearChrFlags(0x4, 0x8)

    label("loc_63AA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_63BD")
    ClearChrFlags(0x5, 0x8)

    label("loc_63BD")

    Call(1, 39)
    SetChrPos(0x0, 206030, 30, 121140, 0)
    EventEnd(0x5)
    Return()

    # Function_27_6217 end

    def Function_28_63D4(): pass

    label("Function_28_63D4")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    SetMapObjFrame(0xFF, "03", 0x1, 0x1)
    OP_68(51760, 1300, 129800, 0)
    MoveCamera(29, 14, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(21000, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_642C")
    SetChrFlags(0x0, 0x8)

    label("loc_642C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_643F")
    SetChrFlags(0x1, 0x8)

    label("loc_643F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6452")
    SetChrFlags(0x2, 0x8)

    label("loc_6452")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6465")
    SetChrFlags(0x3, 0x8)

    label("loc_6465")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6478")
    SetChrFlags(0x4, 0x8)

    label("loc_6478")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_648B")
    SetChrFlags(0x5, 0x8)

    label("loc_648B")

    ClearChrFlags(0x104, 0x8)
    SetChrPos(0x104, 51760, 0, 129800, 0)
    FadeToBright(500, 0)
    OP_0D()

    #C0265
    ChrTalk(
        0x104,
        "#0300F放在这里挺不错啊。\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    SetChrName("")
    Sound(828, 0, 100, 0)

    #A0266
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "兰迪的房间中\x01",
            "放入了新的家具。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SubItemNumber(0x356, 1)
    SetScenarioFlags(0x51, 4)
    OP_66(0xD, 0x1)
    Call(1, 30)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_651F")
    ClearChrFlags(0x0, 0x8)

    label("loc_651F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6532")
    ClearChrFlags(0x1, 0x8)

    label("loc_6532")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6545")
    ClearChrFlags(0x2, 0x8)

    label("loc_6545")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6558")
    ClearChrFlags(0x3, 0x8)

    label("loc_6558")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_656B")
    ClearChrFlags(0x4, 0x8)

    label("loc_656B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_657E")
    ClearChrFlags(0x5, 0x8)

    label("loc_657E")

    Call(1, 39)
    SetChrPos(0x0, 49930, 0, 121070, 0)
    EventEnd(0x5)
    Return()

    # Function_28_63D4 end

    def Function_29_6595(): pass

    label("Function_29_6595")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    SetMapObjFrame(0xFF, "04", 0x1, 0x1)
    SetMapObjFrame(0xFF, "04a", 0x1, 0x1)
    OP_68(52520, 1300, 124040, 0)
    MoveCamera(70, 13, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(22000, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_65F8")
    SetChrFlags(0x0, 0x8)

    label("loc_65F8")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_660B")
    SetChrFlags(0x1, 0x8)

    label("loc_660B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_661E")
    SetChrFlags(0x2, 0x8)

    label("loc_661E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6631")
    SetChrFlags(0x3, 0x8)

    label("loc_6631")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6644")
    SetChrFlags(0x4, 0x8)

    label("loc_6644")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6657")
    SetChrFlags(0x5, 0x8)

    label("loc_6657")

    ClearChrFlags(0x104, 0x8)
    SetChrPos(0x104, 52520, 0, 124040, 25)
    FadeToBright(500, 0)
    OP_0D()

    #C0267
    ChrTalk(
        0x104,
        "#0300F放在这里挺不错啊。\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    SetChrName("")
    Sound(828, 0, 100, 0)

    #A0268
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "兰迪的房间中\x01",
            "放入了新的家具。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SubItemNumber(0x357, 1)
    SetScenarioFlags(0x51, 5)
    OP_66(0xE, 0x1)
    Call(1, 30)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_66EB")
    ClearChrFlags(0x0, 0x8)

    label("loc_66EB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_66FE")
    ClearChrFlags(0x1, 0x8)

    label("loc_66FE")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6711")
    ClearChrFlags(0x2, 0x8)

    label("loc_6711")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6724")
    ClearChrFlags(0x3, 0x8)

    label("loc_6724")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6737")
    ClearChrFlags(0x4, 0x8)

    label("loc_6737")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_674A")
    ClearChrFlags(0x5, 0x8)

    label("loc_674A")

    Call(1, 39)
    SetChrPos(0x0, 49930, 0, 121070, 0)
    EventEnd(0x5)
    Return()

    # Function_29_6595 end

    def Function_30_6761(): pass

    label("Function_30_6761")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_67B3")
    SetChrName("")

    #A0269
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "如果获得了家具类的道具，\x01",
            "就可以将其放入主人公们的房间。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetScenarioFlags(0x51, 6)

    label("loc_67B3")

    Return()

    # Function_30_6761 end

    def Function_31_67B4(): pass

    label("Function_31_67B4")

    TalkBegin(0xFF)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis164.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetChrName("")

    #A0270
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "摆放着导力车模型。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    TalkEnd(0xFF)
    Return()

    # Function_31_67B4 end

    def Function_32_6857(): pass

    label("Function_32_6857")

    TalkBegin(0xFF)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis165.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetChrName("")

    #A0271
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "摆放着导力音响。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    StopBGM(0x1F4)
    WaitBGM()
    Sleep(10)
    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_6918"),
        (1, "loc_6921"),
        (2, "loc_692A"),
        (3, "loc_6933"),
        (4, "loc_693C"),
        (5, "loc_6945"),
        (6, "loc_694E"),
        (7, "loc_6957"),
        (SWITCH_DEFAULT, "loc_6960"),
    )


    label("loc_6918")

    PlayBGM("ed7400", 0)
    Jump("loc_6960")

    label("loc_6921")

    PlayBGM("ed7401", 0)
    Jump("loc_6960")

    label("loc_692A")

    PlayBGM("ed7402", 0)
    Jump("loc_6960")

    label("loc_6933")

    PlayBGM("ed7204", 0)
    Jump("loc_6960")

    label("loc_693C")

    PlayBGM("ed7205", 0)
    Jump("loc_6960")

    label("loc_6945")

    PlayBGM("ed7201", 0)
    Jump("loc_6960")

    label("loc_694E")

    PlayBGM("ed7200", 0)
    Jump("loc_6960")

    label("loc_6957")

    PlayBGM("ed7202", 0)
    Jump("loc_6960")

    label("loc_6960")

    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    TalkEnd(0xFF)
    Return()

    # Function_32_6857 end

    def Function_33_698F(): pass

    label("Function_33_698F")

    TalkBegin(0xFF)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis167.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetChrName("")

    #A0272
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "墙上挂着壁挂钟。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    TalkEnd(0xFF)
    Return()

    # Function_33_698F end

    def Function_34_6A30(): pass

    label("Function_34_6A30")

    TalkBegin(0xFF)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis166.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetChrName("")

    #A0273
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "摆放着典雅花瓶。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    TalkEnd(0xFF)
    Return()

    # Function_34_6A30 end

    def Function_35_6AD1(): pass

    label("Function_35_6AD1")

    TalkBegin(0xFF)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis168.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetChrName("")

    #A0274
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "墙上挂着壁挂咪西。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    TalkEnd(0xFF)
    Return()

    # Function_35_6AD1 end

    def Function_36_6B74(): pass

    label("Function_36_6B74")

    TalkBegin(0xFF)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis057.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetChrName("")

    #A0275
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "摆放着坐姿咪西。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    TalkEnd(0xFF)
    Return()

    # Function_36_6B74 end

    def Function_37_6C15(): pass

    label("Function_37_6C15")

    TalkBegin(0xFF)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis171.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetChrName("")

    #A0276
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "墙上张贴着伊莉娅的海报。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    TalkEnd(0xFF)
    Return()

    # Function_37_6C15 end

    def Function_38_6CBE(): pass

    label("Function_38_6CBE")

    TalkBegin(0xFF)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis170.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetChrName("")

    #A0277
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "墙上挂着飞镖套装。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    TalkEnd(0xFF)
    Return()

    # Function_38_6CBE end

    def Function_39_6D61(): pass

    label("Function_39_6D61")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x50, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x50, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF1, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6D99")
    OP_DE(0x16, 0x0)

    label("loc_6D99")

    Return()

    # Function_39_6D61 end

    SaveToFile()

Try(main)
