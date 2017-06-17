from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "c1050.bin",                # FileName
        "c1050",                    # MapName
        "c1050",                    # Location
        0x0001,                     # MapIndex
        "ed7100",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 1, 0, 2, 0, 3],
    )

    BuildStringList((
        "c1050",                  # 0
        "摩尔斯老人",             # 1
        "摩尔斯老人",             # 2
        "帕拉夫人",               # 3
    ))

    AddCharChip((
        "chr/ch20800.itc",                   # 00
        "chr/ch20900.itc",                   # 01
        "chr/ch20802.itc",                   # 02
    ))

    DeclNpc(569,     4019,    7690,    135,  261,  0x0, 0,   0,   0,   0,   1,   0,   4,   255,  0)
    DeclNpc(-2000,   100,     7030,    90,   389,  0x0, 0,   2,   0,   255, 255, 0,   5,   255,  0)
    DeclNpc(379,     0,       9850,    0,    261,  0x0, 0,   1,   0,   0,   0,   0,   6,   255,  0)

    ScpFunction((
        "Function_0_110",          # 00, 0
        "Function_1_1C8",          # 01, 1
        "Function_2_1F3",          # 02, 2
        "Function_3_346",          # 03, 3
        "Function_4_399",          # 04, 4
        "Function_5_1D1B",         # 05, 5
        "Function_6_20E9",         # 06, 6
    ))


    def Function_0_110(): pass

    label("Function_0_110")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
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

    # Function_0_110 end

    def Function_1_1C8(): pass

    label("Function_1_1C8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1F2")
    OP_94(0xFE, 0x582, 0x24F4, 0xFFFFFCF4, 0x1306, 0x3E8)
    Sleep(300)
    Jump("Function_1_1C8")

    label("loc_1F2")

    Return()

    # Function_1_1C8 end

    def Function_2_1F3(): pass

    label("Function_2_1F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_221")
    SetChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0xA, -2200, 30, 8350, 135)
    SetChrFlags(0xA, 0x10)
    Jump("loc_345")

    label("loc_221")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_22F")
    Jump("loc_345")

    label("loc_22F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_23D")
    Jump("loc_345")

    label("loc_23D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_24B")
    Jump("loc_345")

    label("loc_24B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_259")
    Jump("loc_345")

    label("loc_259")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_26C")
    SetChrFlags(0x8, 0x80)
    Jump("loc_345")

    label("loc_26C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_27F")
    SetChrFlags(0x8, 0x80)
    Jump("loc_345")

    label("loc_27F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_292")
    SetChrFlags(0x8, 0x80)
    Jump("loc_345")

    label("loc_292")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_2A5")
    SetChrFlags(0x8, 0x80)
    Jump("loc_345")

    label("loc_2A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_2BD")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0xA, 0x80)
    Jump("loc_345")

    label("loc_2BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_2D0")
    SetChrFlags(0x8, 0x80)
    Jump("loc_345")

    label("loc_2D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_2E8")
    SetChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    Jump("loc_345")

    label("loc_2E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_2F6")
    Jump("loc_345")

    label("loc_2F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_304")
    Jump("loc_345")

    label("loc_304")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_312")
    Jump("loc_345")

    label("loc_312")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_320")
    Jump("loc_345")

    label("loc_320")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_32E")
    Jump("loc_345")

    label("loc_32E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_33C")
    Jump("loc_345")

    label("loc_33C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_345")

    label("loc_345")

    Return()

    # Function_2_1F3 end

    def Function_3_346(): pass

    label("Function_3_346")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_35F")
    OP_10(0x0, 0x0)
    OP_10(0x1, 0x1)
    Jump("loc_365")

    label("loc_35F")

    OP_10(0x0, 0x1)
    OP_10(0x1, 0x0)

    label("loc_365")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_381")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    Jump("loc_398")

    label("loc_381")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_398")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    Jump("loc_398")

    label("loc_398")

    Return()

    # Function_3_346 end

    def Function_4_399(): pass

    label("Function_4_399")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9A6")
    TurnDirection(0x8, 0x101, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_4D9")

    #C0001
    ChrTalk(
        0xFE,
        (
            "……哦哦，你不就是…在列车上\x01",
            "曾和我同席的那个小伙子吗。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x101,
        (
            "#0002F啊，是那个时候的老爷爷！\x01",
            "……哈哈，好久不见了。\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0xFE,
        "唔唔，自那之后已经过去两个月了吗。\x02",
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0xFE,
        (
            "说起来，那个时候，\x01",
            "你好像说是要去任职报到吧。\x01",
            "工作方面还算顺利吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x101,
        (
            "#0000F嗯，算是吧。\x01",
            "最近总算开始适应了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_67B")

    label("loc_4D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_5FC")

    #C0006
    ChrTalk(
        0xFE,
        (
            "……哦哦，你不就是…在列车上\x01",
            "曾和我同席的那个小伙子吗。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x101,
        (
            "#0002F啊，是那个时候的老爷爷！\x01",
            "……哈哈，好久不见了。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0xFE,
        "唔唔，自那之后已经过去两个月了吗。\x02",
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0xFE,
        (
            "说起来，那个时候，\x01",
            "你好像说是要去任职报到吧。\x01",
            "工作方面还算顺利吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x101,
        (
            "#0000F嗯，算是吧。\x01",
            "最近总算开始适应了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_67B")

    label("loc_5FC")


    #C0011
    ChrTalk(
        0xFE,
        "……哦哦，你是那时的小伙子。\x02",
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0xFE,
        "任职报到的情况怎么样啊？\x02",
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x101,
        (
            "#0012F嗯，那个，哈哈哈……\x01",
            "感觉总算是正式进入状态了啊……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_67B")


    #C0014
    ChrTalk(
        0xFE,
        (
            "呵呵，和同期入职\x01",
            "的伙伴们在一起吗，\x01",
            "一群年轻人凑在一起，真是很有气势啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0xFE,
        (
            "呵呵，虽然我帮不上什么忙，不过，如果\x01",
            "有需要，就尽管来找我商量吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0xFE,
        (
            "我年轻的时候也曾有过经商的经历，\x01",
            "还算是有些人脉啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x101,
        (
            "#0005F哎，是这样啊。\x02\x03",

            "#0000F顺便再请问一下，\x01",
            "您具体都认识些什么人呢……？\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0xFE,
        "嗯，这个嘛。\x02",
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0xFE,
        (
            "像克洛斯贝尔的市长啦，\x01",
            "贸易商团队的领导啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0xFE,
        (
            "还有就是乌尔斯拉医科大学\x01",
            "的理事长，全都是我的好友啊。\x02",
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
    Sleep(1200)

    #C0021
    ChrTalk(
        0x104,
        (
            "#0303F……罗伊德，这位老爷爷\x01",
            "好像是个很有来头的人物啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x101,
        "#0006F那个，老爷爷，您究竟是……\x02",
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0xFE,
        (
            "呵呵，我是克洛\x01",
            "斯贝尔工商协会\x01",
            "的会长。\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0xFE,
        (
            "哈，用不着这么拘束啦。\x01",
            "也不是什么了不起的职位。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x103,
        "#0200F（从外表根本看不出来呢……）\x02",
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x102,
        (
            "#0104F（工商协会的摩尔斯会长……\x01",
            "  就是这个人啊。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x4F, 4)
    Jump("loc_1D17")

    label("loc_9A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_9B4")
    Jump("loc_1D17")

    label("loc_9B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_AB3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A50")

    #C0027
    ChrTalk(
        0xFE,
        (
            "继昨天的事件之后，\x01",
            "空港那边好像也\x01",
            "发生了麻烦呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0xFE,
        (
            "嗯，最近真是\x01",
            "麻烦不断啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0xFE,
        "或许现在并不是适合召开议会的时候呢。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_AAE")

    label("loc_A50")


    #C0030
    ChrTalk(
        0xFE,
        (
            "所谓的商人，总会对\x01",
            "街上的气氛非常敏感。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0xFE,
        (
            "……最近这段时间，\x01",
            "令人在意的事件非常多啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AAE")

    Jump("loc_1D17")

    label("loc_AB3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_B51")

    #C0032
    ChrTalk(
        0xFE,
        (
            "应该在今天早上发行的\x01",
            "克洛斯贝尔时代周刊的最新一期\x01",
            "还没有送到呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0xFE,
        (
            "虽然问了老伴，\x01",
            "但是她也不知道……\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0xFE,
        (
            "看起来，好像是\x01",
            "临时休刊了啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D17")

    label("loc_B51")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_C81")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C18")

    #C0035
    ChrTalk(
        0xFE,
        (
            "自治州议会的会议时间\x01",
            "和以往一样，又延长了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0xFE,
        (
            "再这么拖延下去，\x01",
            "预算就无法正常执行了……\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0xFE,
        (
            "唔唔唔，竟然会这么做。\x01",
            "这样下去，也会对市民们\x01",
            "的生活造成恶劣影响啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_C7C")

    label("loc_C18")


    #C0038
    ChrTalk(
        0xFE,
        (
            "唔唔唔，哈尔特曼议长\x01",
            "果然还是不愿意妥协吗……\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0xFE,
        (
            "这样一来，会议大概就要\x01",
            "继续延长下去了吧……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C7C")

    Jump("loc_1D17")

    label("loc_C81")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_142A")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x10)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F, 4)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBF, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_113D")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_FA9")

    #C0040
    ChrTalk(
        0xFE,
        (
            "哎呀……是你们啊。\x01",
            "在纪念庆典期间，真是麻烦你们了。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0xE)"), scpexpr(EXPR_END)), "loc_E3F")

    #C0041
    ChrTalk(
        0x101,
        (
            "#0000F哪里，并不是什么值得您道谢的事情。\x01",
            "对警官来说，那只是理所当然的分内之事。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D87")

    #C0042
    ChrTalk(
        0x102,
        "#0100F不管怎么说，能顺利解决就很好了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_E0F")

    label("loc_D87")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_DCB")

    #C0043
    ChrTalk(
        0x103,
        (
            "#0204F嗯，这大概也算是\x01",
            "我们实力的体现吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E0F")

    label("loc_DCB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E0F")

    #C0044
    ChrTalk(
        0x104,
        "#0304F嘿，因为我们是传说中的特别任务支援科嘛。\x02",
    )

    CloseMessageWindow()

    label("loc_E0F")


    #C0045
    ChrTalk(
        0xFE,
        (
            "呵呵，看起来，\x01",
            "你们还是一样有精神啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F5B")

    label("loc_E3F")


    #C0046
    ChrTalk(
        0x101,
        (
            "#0006F那个时候，我们没能帮上\x01",
            "什么忙，真是不好意思。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_EAB")

    #C0047
    ChrTalk(
        0x102,
        "#0103F实在是让您担心了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_F10")

    label("loc_EAB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_EE4")

    #C0048
    ChrTalk(
        0x103,
        "#0203F……当时真是让您担心了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_F10")

    label("loc_EE4")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_F10")

    #C0049
    ChrTalk(
        0x104,
        "#0306F真是没脸见人啊。\x02",
    )

    CloseMessageWindow()

    label("loc_F10")


    #C0050
    ChrTalk(
        0xFE,
        (
            "哪里哪里，你们能够全力帮忙调查，\x01",
            "身为一名市民，我就已经感到很高兴了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F5B")


    #C0051
    ChrTalk(
        0xFE,
        (
            "话说回来……唔。\x01",
            "今天还带着一个小孩子啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0xFE,
        "接下来还要去警署吗？\x02",
    )

    CloseMessageWindow()
    Jump("loc_100C")

    label("loc_FA9")


    #C0053
    ChrTalk(
        0xFE,
        (
            "哎呀……是罗伊德嘛。\x01",
            "好久不见了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0xFE,
        (
            "唔……今天还带着\x01",
            "一个小孩子啊。\x01",
            "接下来是要去警署吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_100C")


    #C0055
    ChrTalk(
        0x101,
        (
            "#0000F那个……嗯，算是吧，正要过去一趟呢。\x01",
            "准备去查一查这个孩子的身份来历。\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0xFE,
        "是吗，这样啊。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x153, 500)
    Sleep(300)

    #C0057
    ChrTalk(
        0xFE,
        (
            "小姑娘，一定要小心\x01",
            "路上的导力车啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0xFE,
        "绝对不能在车道上乱跑。\x02",
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x153,
        (
            "#1111F不能在车道上……\x02\x03",

            "#1109F嗯，明白啦～\x01",
            "绝对不能在车道上乱跑，对吧～！\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0xFE,
        "呵呵，真是个记东西很快的孩子呢。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0xBF, 7)
    Jump("loc_1425")

    label("loc_113D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13B0")

    #C0061
    ChrTalk(
        0xFE,
        (
            "那么，从明天开始，\x01",
            "就要召开自治州议会了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0xFE,
        (
            "嗯，帝国派和共和国派\x01",
            "又要争斗不休了吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0xFE,
        (
            "麦克道尔市长大概又会\x01",
            "非常操劳了吧。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x10)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F, 4)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_13A8")
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1290")

    #C0064
    ChrTalk(
        0x101,
        (
            "#0003F（会长先生……好像很担心\x01",
            "  艾莉的外公呢。）\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x102,
        (
            "#0100F（他们两个人以前\x01",
            "  就有些私交呢。）\x02\x03",

            "#0108F（……我也…………\x01",
            "  有些担心议会的事情呢。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13A8")

    label("loc_1290")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1322")

    #C0066
    ChrTalk(
        0x103,
        (
            "#0203F（会长先生他好像\x01",
            "  很担心艾莉前辈\x01",
            "  的外公呢。）\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x101,
        (
            "#0000F（听艾莉说过，会长和她的\x01",
            "  外公好像有一定的私交呢。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13A8")

    label("loc_1322")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_13A8")

    #C0068
    ChrTalk(
        0x104,
        (
            "#0303F（会长先生好像很担心\x01",
            "  大小姐的外公啊。）\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x101,
        (
            "#0000F（听艾莉说过，会长和她的\x01",
            "  外公好像有一定的私交呢。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13A8")

    SetScenarioFlags(0x0, 0)
    Jump("loc_1425")

    label("loc_13B0")


    #C0070
    ChrTalk(
        0xFE,
        (
            "如今的状况就是，\x01",
            "真正出色的政治家\x01",
            "只剩下麦克道尔市长。\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0xFE,
        (
            "议会恐怕又将一片混乱吧……\x01",
            "但我们也只能在一旁观望。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1425")

    Jump("loc_1D17")

    label("loc_142A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_1438")
    Jump("loc_1D17")

    label("loc_1438")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_1446")
    Jump("loc_1D17")

    label("loc_1446")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_15AC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1524")

    #C0072
    ChrTalk(
        0xFE,
        (
            "下个月会有\x01",
            "盛大热闹的纪念庆典啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0xFE,
        (
            "不过，更值得注意的\x01",
            "还是在那一周之后的\x01",
            "自治州议会啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0xFE,
        (
            "那可是要制定州政府一年中所有计划的\x01",
            "重要议会……为了防止议员们谋取私利，\x01",
            "我们也必须密切关注。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_15A7")

    label("loc_1524")


    #C0075
    ChrTalk(
        0xFE,
        (
            "在纪念庆典之后，\x01",
            "还要召开预算会议。\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0xFE,
        (
            "嗯……对中立派的市长而言，\x01",
            "那才是真正需要面对的难题吧。\x01",
            "我们也必须要密切关注才行啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15A7")

    Jump("loc_1D17")

    label("loc_15AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_16B8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1657")

    #C0077
    ChrTalk(
        0xFE,
        (
            "鲁巴彻的那些家伙们\x01",
            "被保释出来了吗……\x01",
            "结果还是一如既往地让人恼火啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0xFE,
        (
            "虽然我早就决定过\x01",
            "不会涉足政治，\x01",
            "但在这种时候，还是很焦急愤怒啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_16B3")

    label("loc_1657")


    #C0079
    ChrTalk(
        0xFE,
        (
            "克洛斯贝尔的政治\x01",
            "早已被金钱与权力彻底污染了。\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0xFE,
        (
            "哎呀呀……每一次都是\x01",
            "如此让人失望。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16B3")

    Jump("loc_1D17")

    label("loc_16B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_17FC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_178F")

    #C0081
    ChrTalk(
        0xFE,
        (
            "露天市场上有个\x01",
            "叫迪因兹的小伙子在卖蔬菜吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0xFE,
        (
            "以前曾经帮助过他，在那之后，\x01",
            "他就不时来拜访我。\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0xFE,
        (
            "呵呵，他好像还是和从前一样，\x01",
            "诚实守信地做着买卖呢。\x01",
            "希望这些年轻人能继续努力啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_17F7")

    label("loc_178F")


    #C0084
    ChrTalk(
        0xFE,
        (
            "培养年轻一代的商人，\x01",
            "也是我们这些老家伙的职责啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0xFE,
        (
            "呵呵，只要能继续诚信地经商，\x01",
            "就比什么都好。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17F7")

    Jump("loc_1D17")

    label("loc_17FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_195C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_191C")

    #C0086
    ChrTalk(
        0xFE,
        "那么，必须去出席今晚的聚会了啊。\x02",
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0xFE,
        (
            "还要做个汇总报告，\x01",
            "提出决算清单。\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0xFE,
        (
            "创立纪念庆典的日子也越来越近了，\x01",
            "过些天还得去和市长谈谈啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0x101,
        (
            "#0000F哈哈……身为会长，\x01",
            "好像还真是很忙呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0xFE,
        (
            "正是如此。\x01",
            "虽然我都已经这把年纪了，\x01",
            "但每天还是有忙不完的工作啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1957")

    label("loc_191C")


    #C0091
    ChrTalk(
        0xFE,
        (
            "今天晚上要去参加工商协会的聚会。\x01",
            "准备工作也有得忙了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1957")

    Jump("loc_1D17")

    label("loc_195C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_1AB5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A3A")

    #C0092
    ChrTalk(
        0xFE,
        (
            "克洛斯贝尔的商人们\x01",
            "并不都是相互敌视的。\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0xFE,
        (
            "在我们东街，很早以前，\x01",
            "商人之间就结成了共同阵线，\x01",
            "彼此之间互帮互助。\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0xFE,
        (
            "呵呵，不知是从什么时候开始，\x01",
            "就有了『克洛斯贝尔工商协会』\x01",
            "这个名字啦。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1AB0")

    label("loc_1A3A")


    #C0095
    ChrTalk(
        0xFE,
        (
            "克洛斯贝尔工商协会\x01",
            "诞生于东街的露天店。\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0xFE,
        (
            "现在，虽然已经扩展到了整个克洛斯贝尔，\x01",
            "但当时的精神一直延续了下来。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1AB0")

    Jump("loc_1D17")

    label("loc_1AB5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_1BB3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B72")

    #C0097
    ChrTalk(
        0xFE,
        (
            "今天和一位老朋友\x01",
            "约好要见面。\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0xFE,
        (
            "那是从前一起和我经商的老友。\x01",
            "虽然我现在已经不再经商了，\x01",
            "但我们的情谊还是一直未变。\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0xFE,
        (
            "呵呵，东街的商人\x01",
            "都是很重感情的。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1BAE")

    label("loc_1B72")


    #C0100
    ChrTalk(
        0xFE,
        (
            "今天和一位老朋友\x01",
            "约好要见面。\x01",
            "差不多也该开始准备了啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BAE")

    Jump("loc_1D17")

    label("loc_1BB3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_1D17")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CAF")

    #C0101
    ChrTalk(
        0xFE,
        (
            "虽然我现在在为工商协会服务，\x01",
            "但年轻的时候，我也在\x01",
            "市场上经营过露天店的。\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0xFE,
        (
            "呵呵，在经营露天店的时代所拓展的\x01",
            "人脉，无论什么时候都很有用处呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0xFE,
        (
            "呵呵，如果有什么困难，就来找我商量吧。\x01",
            "能有人说说话，\x01",
            "我也会很开心的。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1D17")

    label("loc_1CAF")


    #C0104
    ChrTalk(
        0xFE,
        (
            "能和你们相识，也算是一种缘分，\x01",
            "如果遇到困难，就来找我商量吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0xFE,
        (
            "能有人说说话，\x01",
            "我也会很开心的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D17")

    TalkEnd(0xFE)
    Return()

    # Function_4_399 end

    def Function_5_1D1B(): pass

    label("Function_5_1D1B")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1DAF")
    Jump("loc_1DF9")

    label("loc_1DAF")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1DCF")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1DF9")

    label("loc_1DCF")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1DEF")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1DF9")

    label("loc_1DEF")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1DF9")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_1F41")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1EDC")

    #C0106
    ChrTalk(
        0xFE,
        (
            "听说自治州议会\x01",
            "总算是结束了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0xFE,
        (
            "唔……虽然只听到了速报，\x01",
            "不过，差不多也就是这样了吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0xFE,
        (
            "在帝国派与共和国派的阻挠之下，\x01",
            "麦克道尔市长已经做得很不错了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1F3C")

    label("loc_1EDC")


    #C0109
    ChrTalk(
        0xFE,
        (
            "听说自治州议会\x01",
            "总算是结束了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0xFE,
        (
            "考虑到如今的派阀式政治状况，\x01",
            "市长已经做得很不错了啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F3C")

    Jump("loc_20E1")

    label("loc_1F41")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_20E1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_207C")

    #C0111
    ChrTalk(
        0xFE,
        (
            "说起ＩＢＣ，那可是\x01",
            "克洛斯贝尔引以为傲的\x01",
            "全世界最大国际银行。\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0xFE,
        (
            "呵呵，即使是在优秀的克洛斯贝尔商人当中，\x01",
            "ＩＢＣ的成功也算得上是首屈一指了吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0xFE,
        (
            "这家银行任命了一代又一代的\x01",
            "优秀总裁，他们巧妙地操掌着舵盘，\x01",
            "终于成功跨越了时代的激流。\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0xFE,
        (
            "对我们来说，ＩＢＣ\x01",
            "也算得上是一个骄傲了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_20E1")

    label("loc_207C")


    #C0115
    ChrTalk(
        0xFE,
        "ＩＢＣ可是全世界最大的国际银行啊。\x02",
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0xFE,
        (
            "对克洛斯贝尔的市民来说，\x01",
            "可以说得上是引以为荣的骄傲吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_20E1")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_5_1D1B end

    def Function_6_20E9(): pass

    label("Function_6_20E9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_225A")
    TurnDirection(0xFE, 0x101, 0)
    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    #C0117
    ChrTalk(
        0xFE,
        (
            "啊，你不就是……\x01",
            "在列车上和我们同席的那个……\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0x101,
        (
            "#0005F那、那个时候的老婆婆……！？\x02\x03",

            "对了，当时您确实\x01",
            "是说过家在东街……\x01",
            "原来就是这里啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0xFE,
        (
            "呵呵，那个时候\x01",
            "还麻烦你帮我搬行李了。\x01",
            "年纪轻轻就知道助人为乐，真了不起呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0xFE,
        (
            "对了对了，\x01",
            "老头子就在楼上呢。\x01",
            "方便的话，就去见见他吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0x101,
        "#0000F嗯，非常乐意。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x4F, 5)
    Jump("loc_36B0")

    label("loc_225A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_22A2")

    #C0122
    ChrTalk(
        0xFE,
        (
            "喂喂，老头子，\x01",
            "不要一天到晚只关心政治，\x01",
            "快点吃饭吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_36B0")

    label("loc_22A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_23AC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_233F")

    #C0123
    ChrTalk(
        0xFE,
        (
            "从商人们那里听到了传闻，\x01",
            "似乎有好几位来做生意的\x01",
            "贸易商都行踪不明了。\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0xFE,
        (
            "究竟是怎么回事呢？\x01",
            "难道是结伴去国外\x01",
            "进行商谈了吗？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_23A7")

    label("loc_233F")


    #C0125
    ChrTalk(
        0xFE,
        (
            "商人们的情报总是\x01",
            "又快又准确呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0xFE,
        (
            "从早上开始，竟然已经有好几个人失踪了，\x01",
            "总觉得事情有些蹊跷啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_23A7")

    Jump("loc_36B0")

    label("loc_23AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_2427")

    #C0127
    ChrTalk(
        0xFE,
        (
            "老头子一直都十分\x01",
            "关注议会的动向。\x02",
        )
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0xFE,
        (
            "所以，要是克洛斯贝尔时代周刊\x01",
            "没能准时送到，\x01",
            "就会让他坐立不安的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_36B0")

    label("loc_2427")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_2555")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_24F3")

    #C0129
    ChrTalk(
        0xFE,
        (
            "老头子他今天也\x01",
            "捧着克洛斯贝尔时代周刊\x01",
            "读个没完呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0xFE,
        (
            "每年只要一到了议会召开的时候，\x01",
            "他就会陷入这种状态呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0xFE,
        (
            "如果不想听他唠叨\x01",
            "一些难懂的东西，\x01",
            "还是不要接近他为好哦。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2550")

    label("loc_24F3")


    #C0132
    ChrTalk(
        0xFE,
        (
            "老头子他每年\x01",
            "都是如此呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0xFE,
        (
            "如果不想听他唠叨\x01",
            "一些难懂的东西，\x01",
            "还是不要接近他为好哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2550")

    Jump("loc_36B0")

    label("loc_2555")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_2B40")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6C, 7)), scpexpr(EXPR_END)), "loc_29A7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBF, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_27EA")

    #C0134
    ChrTalk(
        0xFE,
        (
            "啊呀……？\x01",
            "今天带着一位可爱的小客人\x01",
            "一起来了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0x153,
        "#1110F你好～！\x02",
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0xFE,
        "呵呵，好有活力的问候呀。\x02",
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0x101,
        (
            "#0000F这孩子叫琪雅，暂时\x01",
            "留在我们支援科生活。\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0xFE,
        (
            "是这样啊。\x01",
            "应该是有什么隐情吧……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    #C0139
    ChrTalk(
        0xFE,
        (
            "对了，小琪雅，\x01",
            "今天就把这个\x01",
            "拿回去吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0xFE,
        (
            "我们家里全是酒，\x01",
            "果汁比较少呢……\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0141
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '甘露『紫绀』'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber('甘露『紫绀』', 1)

    #C0142
    ChrTalk(
        0x153,
        "#1105F哇～可以收下吗～？\x02",
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0xFE,
        (
            "嗯，当然啦，\x01",
            "在疲劳的时候就喝下它吧。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2766")

    #C0144
    ChrTalk(
        0x102,
        (
            "#0100F真是不好意思，\x01",
            "谢谢您了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_27CA")

    label("loc_2766")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_279C")

    #C0145
    ChrTalk(
        0x103,
        (
            "#0200F真不好意思，\x01",
            "谢谢您。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_27CA")

    label("loc_279C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_27CA")

    #C0146
    ChrTalk(
        0x104,
        "#0300F哈哈，不好意思啦。\x02",
    )

    CloseMessageWindow()

    label("loc_27CA")


    #C0147
    ChrTalk(
        0x153,
        "#1109F谢谢奶奶～！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0xBF, 5)
    Jump("loc_29A2")

    label("loc_27EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2938")

    #C0148
    ChrTalk(
        0xFE,
        (
            "说起来……你们应该\x01",
            "已经听说这件事了吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0xFE,
        (
            "在纪念庆典的最后一天，\x01",
            "米修拉姆那里好像\x01",
            "发生了什么事件呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0xFE,
        (
            "据说拱廊大街上\x01",
            "出现了魔兽……\x01",
            "但之后就再也没有什么相关消息了。\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0xFE,
        (
            "应该没人受伤吧，\x01",
            "实在是很让人担心呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0x153,
        "#1111F………………？？？\x02",
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0x101,
        (
            "#0000F哈哈哈……\x01",
            "（看来对这件事\x01",
            "  做了一定的报道限制呢……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_29A2")

    label("loc_2938")


    #C0154
    ChrTalk(
        0xFE,
        (
            "虽然媒体对米修拉姆出现魔兽的\x01",
            "事情做了大篇幅的报道……\x02",
        )
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0xFE,
        (
            "但那其实只是个\x01",
            "毫无根据的小道消息而已吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_29A2")

    Jump("loc_2B3B")

    label("loc_29A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBF, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A18")

    #C0156
    ChrTalk(
        0xFE,
        (
            "啊呀……？\x01",
            "有位可爱的小客人\x01",
            "也一起来了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0xFE,
        (
            "呵呵，请随意放松吧。\x01",
            "老头子今天也回来了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xBF, 5)
    Jump("loc_2B3B")

    label("loc_2A18")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2AD1")

    #C0158
    ChrTalk(
        0xFE,
        (
            "听说，在纪念庆典的最后一天，\x01",
            "米修拉姆那边好像\x01",
            "发生了事件呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0xFE,
        (
            "据说拱廊大街上\x01",
            "出现了魔兽……\x01",
            "应该没人受伤吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0xFE,
        (
            "但关于事件的具体情况，\x01",
            "并没有太多消息呢……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2B3B")

    label("loc_2AD1")


    #C0161
    ChrTalk(
        0xFE,
        (
            "虽然媒体对米修拉姆出现魔兽的\x01",
            "事情做了大篇幅的报道……\x02",
        )
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0xFE,
        (
            "但那其实只是个\x01",
            "毫无根据的小道消息而已吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B3B")

    Jump("loc_36B0")

    label("loc_2B40")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_2B9C")

    #C0163
    ChrTalk(
        0xFE,
        (
            "啊呀，你们\x01",
            "也要出去吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0xFE,
        (
            "在外面一定要小心啊，\x01",
            "今天到处都人山人海的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_36B0")

    label("loc_2B9C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_2C58")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C05")

    #C0165
    ChrTalk(
        0xFE,
        (
            "洛依和梅琳\x01",
            "也渐渐长大了哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0xFE,
        (
            "今天要是能留下来\x01",
            "住一晚就最好不过了呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2C53")

    label("loc_2C05")


    #C0167
    ChrTalk(
        0xFE,
        (
            "见到了久别的孙儿们，\x01",
            "一下就心安了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0xFE,
        (
            "今天就留他们\x01",
            "在家里住一晚吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C53")

    Jump("loc_36B0")

    label("loc_2C58")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_2D25")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2CB0")

    #C0169
    ChrTalk(
        0xFE,
        "今天有游行活动吧？\x02",
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0xFE,
        (
            "我想应该准备一点\x01",
            "饮料什么的吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2D20")

    label("loc_2CB0")


    #C0171
    ChrTalk(
        0xFE,
        (
            "呵呵，也要为工商协会\x01",
            "的各位都准备一份啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0xFE,
        (
            "在我看来，不管什么时候，\x01",
            "大家也都只是些爱撒娇的小孩子而已。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D20")

    Jump("loc_36B0")

    label("loc_2D25")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_2DEC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2DA7")

    #C0173
    ChrTalk(
        0xFE,
        (
            "老头子今天也去了\x01",
            "工商协会的接待帐篷呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0xFE,
        (
            "他好像很在意\x01",
            "那些晚辈们的情况。\x01",
            "呵呵，真是没办法呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2DE7")

    label("loc_2DA7")


    #C0175
    ChrTalk(
        0xFE,
        (
            "稍后就去给他\x01",
            "送份饭吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0xFE,
        (
            "他一定会聊天聊得\x01",
            "忘了吃饭吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2DE7")

    Jump("loc_36B0")

    label("loc_2DEC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_2E7D")

    #C0177
    ChrTalk(
        0xFE,
        (
            "老头子他已经\x01",
            "出门了哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0xFE,
        (
            "他要参加工商协会的聚会，\x01",
            "为纪念庆典做准备呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0xFE,
        (
            "呵呵，一点都不考虑自己的年纪，\x01",
            "还是那么拼命。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_36B0")

    label("loc_2E7D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_2FCA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F4F")

    #C0180
    ChrTalk(
        0xFE,
        "呵呵，说起ＩＢＣ……\x02",
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0xFE,
        (
            "库罗伊斯总裁和\x01",
            "麦克道尔市长的女婿曾经\x01",
            "是好朋友呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0xFE,
        (
            "市长的女婿以前\x01",
            "也是一位政治家。\x02",
        )
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0xFE,
        (
            "他们两个人都有女儿……\x01",
            "不知道那两个女孩\x01",
            "是否也成为了好友。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2FC5")

    label("loc_2F4F")


    #C0184
    ChrTalk(
        0xFE,
        (
            "库罗伊斯总裁和\x01",
            "麦克道尔市长的女婿曾经\x01",
            "是好朋友呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0xFE,
        (
            "他们两个人都有女儿，\x01",
            "不知道那两个女孩\x01",
            "是否也成为了好友。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2FC5")

    Jump("loc_36B0")

    label("loc_2FCA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_30C7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3088")

    #C0186
    ChrTalk(
        0xFE,
        (
            "最近来到克洛斯贝尔的\x01",
            "那两位游击士好像非常\x01",
            "努力呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0xFE,
        (
            "好像是叫艾丝蒂尔\x01",
            "和约修亚吧，\x01",
            "在东街都已经成为名人了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0xFE,
        (
            "能见到年轻人的活跃表现，\x01",
            "我非常高兴啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_30C2")

    label("loc_3088")


    #C0189
    ChrTalk(
        0xFE,
        (
            "新来的那些游击士\x01",
            "也都十分活跃呢，\x01",
            "好像还上了杂志呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_30C2")

    Jump("loc_36B0")

    label("loc_30C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_31C7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3164")

    #C0190
    ChrTalk(
        0xFE,
        (
            "随着纪念庆典的临近，\x01",
            "街上也变得繁华起来了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0191
    ChrTalk(
        0xFE,
        (
            "所有的店铺都在为庆典做准备，\x01",
            "我们也很期待啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0xFE,
        "简直激动得心跳加速呢。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_31C2")

    label("loc_3164")


    #C0193
    ChrTalk(
        0xFE,
        (
            "随着纪念庆典的临近，\x01",
            "街上也变得繁华起来了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0194
    ChrTalk(
        0xFE,
        (
            "呵呵，每年的这个时期\x01",
            "都很让人开心呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_31C2")

    Jump("loc_36B0")

    label("loc_31C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_3250")

    #C0195
    ChrTalk(
        0xFE,
        (
            "今天早上腰突然疼得厉害。\x01",
            "所需的食材是拜托关系很熟\x01",
            "的商人帮忙送来的。\x02",
        )
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0xFE,
        (
            "呵呵，老头子交下的人脉\x01",
            "偶尔也能有些用处啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_36B0")

    label("loc_3250")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_3367")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3328")

    #C0197
    ChrTalk(
        0xFE,
        (
            "啊呀，你们几位……\x01",
            "一脸倦容呢，没事吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0x102,
        "#0100F啊哈哈……没问题的。\x02",
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0x103,
        (
            "#0200F嗯，我也一样……\x01",
            "已经稍微休息过一下了。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6C, 7)), scpexpr(EXPR_END)), "loc_3320")

    #C0200
    ChrTalk(
        0x101,
        (
            "#0000F婆婆，多谢您的\x01",
            "柠檬汁了。\x01",
            "十分有效果呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3320")

    SetScenarioFlags(0x0, 1)
    Jump("loc_3362")

    label("loc_3328")


    #C0201
    ChrTalk(
        0xFE,
        (
            "累了的话，就再和我说啊。\x01",
            "我会再做些柠檬汁\x01",
            "送给你的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3362")

    Jump("loc_36B0")

    label("loc_3367")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_355A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6C, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3520")

    #C0202
    ChrTalk(
        0xFE,
        (
            "啊呀啊呀，\x01",
            "这么多年轻人啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0203
    ChrTalk(
        0xFE,
        (
            "怎么了，大家要\x01",
            "一起出门吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0204
    ChrTalk(
        0x101,
        (
            "#0000F嗯，稍微有点工作。\x01",
            "正要去阿尔摩利卡村\x01",
            "那边呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0205
    ChrTalk(
        0xFE,
        "啊呀，那可真是路途遥远呢。\x02",
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    #C0206
    ChrTalk(
        0xFE,
        (
            "对了，既然如此，\x01",
            "就把这个带去吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0207
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '罗赞贝尔克人偶·Ｒ'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber('罗赞贝尔克人偶·Ｒ', 1)

    #C0208
    ChrTalk(
        0x101,
        (
            "#0000F冰镇的柠檬汁……\x01",
            "就是之前给我喝过的那个饮料呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0209
    ChrTalk(
        0xFE,
        (
            "这个可以补充体力的，\x01",
            "记得在路上喝哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0210
    ChrTalk(
        0x104,
        "#0300F哈哈，明白。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x6C, 7)
    Jump("loc_3555")

    label("loc_3520")


    #C0211
    ChrTalk(
        0xFE,
        (
            "好啦好啦，那就快点出发吧。\x01",
            "趁着太阳还没有下山。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3555")

    Jump("loc_36B0")

    label("loc_355A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_3630")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_35EF")

    #C0212
    ChrTalk(
        0xFE,
        (
            "这一带的街道\x01",
            "总是很喧闹吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0213
    ChrTalk(
        0xFE,
        (
            "不过，一旦习惯之后，不吵闹\x01",
            "的时候反而会令人感到很寂寞呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0214
    ChrTalk(
        0xFE,
        "呵呵，真是难办呢……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_362B")

    label("loc_35EF")


    #C0215
    ChrTalk(
        0xFE,
        (
            "不吵闹的时候，\x01",
            "反倒会觉得寂寞呢。\x01",
            "呵呵，真是难办呢……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_362B")

    Jump("loc_36B0")

    label("loc_3630")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_36B0")

    #C0216
    ChrTalk(
        0xFE,
        (
            "呵呵，能认识些年轻人，\x01",
            "实在是令人开心。\x02",
        )
    )

    CloseMessageWindow()

    #C0217
    ChrTalk(
        0xFE,
        (
            "如果方便的话，以后再来玩吧。\x01",
            "到时候我会给你们\x01",
            "准备一些美味的食物哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_36B0")

    TalkEnd(0xFE)
    Return()

    # Function_6_20E9 end

    SaveToFile()

Try(main)
