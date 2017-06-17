from ScenarioHelper import *

def main():
    CreateScenaFile(
        "c1050.bin",                # FileName
        "c1050",                    # MapName
        "c1050",                    # Location
        0x0001,                     # MapIndex
        "ed7150",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 1, 0, 2, 0, 3],
    )

    BuildStringList((
        "c1050",                  # 0
        "摩尔斯老人",             # 1
        "帕拉夫人",               # 2
        "洛依",                   # 3
        "梅琳",                   # 4
    ))

    AddCharChip((
        "chr/ch20800.itc",                   # 00
        "chr/ch20900.itc",                   # 01
        "chr/ch20802.itc",                   # 02
        "chr/ch21202.itc",                   # 03
        "chr/ch21502.itc",                   # 04
        "chr/ch21200.itc",                   # 05
        "chr/ch21500.itc",                   # 06
    ))

    DeclNpc(569,     4019,    7690,    135,  261,  0x0, 0,   0,   0,   0,   1,   0,   4,   255,  0)
    DeclNpc(379,     0,       9850,    0,    261,  0x0, 0,   1,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(889,     100,     6969,    270,  389,  0x0, 0,   3,   0,   255, 255, 0,   6,   255,  0)
    DeclNpc(-2150,   100,     7010,    90,   389,  0x0, 0,   4,   0,   255, 255, 0,   7,   255,  0)

    ChipFrameInfo(328, 0)                                        # 0

    ScpFunction((
        "Function_0_148",          # 00, 0
        "Function_1_200",          # 01, 1
        "Function_2_22B",          # 02, 2
        "Function_3_3B3",          # 03, 3
        "Function_4_43C",          # 04, 4
        "Function_5_1533",         # 05, 5
        "Function_6_22B5",         # 06, 6
        "Function_7_23FA",         # 07, 7
        "Function_8_2472",         # 08, 8
        "Function_9_296C",         # 09, 9
    ))


    def Function_0_148(): pass

    label("Function_0_148")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_188"),
        (1, "loc_194"),
        (2, "loc_1A0"),
        (3, "loc_1AC"),
        (4, "loc_1B8"),
        (5, "loc_1C4"),
        (6, "loc_1D0"),
        (SWITCH_DEFAULT, "loc_1DC"),
    )


    label("loc_188")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_1E8")

    label("loc_194")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_1E8")

    label("loc_1A0")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_1E8")

    label("loc_1AC")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_1E8")

    label("loc_1B8")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_1E8")

    label("loc_1C4")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_1E8")

    label("loc_1D0")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_1E8")

    label("loc_1DC")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_1E8")

    label("loc_1E8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1FF")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_1E8")

    label("loc_1FF")

    Return()

    # Function_0_148 end

    def Function_1_200(): pass

    label("Function_1_200")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_22A")
    OP_94(0xFE, 0x582, 0x24F4, 0xFFFFFCF4, 0x1306, 0x3E8)
    Sleep(300)
    Jump("Function_1_200")

    label("loc_22A")

    Return()

    # Function_1_200 end

    def Function_2_22B(): pass

    label("Function_2_22B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_239")
    Jump("loc_3B2")

    label("loc_239")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_2C8")
    ClearChrFlags(0xA, 0x80)
    SetChrChipByIndex(0xA, 0x5)
    BeginChrThread(0xA, 0, 0, 0)
    SetChrPos(0xA, 1020, 0, 3500, 270)
    SetChrPos(0x8, -800, 0, 3500, 90)
    BeginChrThread(0x8, 0, 0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_288")
    SetChrFlags(0xA, 0x10)

    label("loc_288")

    SetChrFlags(0x8, 0x10)
    ClearChrFlags(0xB, 0x80)
    SetChrChipByIndex(0xB, 0x6)
    BeginChrThread(0xB, 0, 0, 0)
    SetChrPos(0xB, 1040, 4019, 7540, 0)
    SetChrPos(0x9, 1040, 4019, 8540, 180)
    SetChrFlags(0x9, 0x10)
    Jump("loc_3B2")

    label("loc_2C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_2D6")
    Jump("loc_3B2")

    label("loc_2D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2E9")
    SetChrFlags(0x8, 0x80)
    Jump("loc_3B2")

    label("loc_2E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_2F7")
    Jump("loc_3B2")

    label("loc_2F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_305")
    Jump("loc_3B2")

    label("loc_305")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_318")
    SetChrFlags(0x8, 0x80)
    Jump("loc_3B2")

    label("loc_318")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_32B")
    SetChrFlags(0x8, 0x80)
    Jump("loc_3B2")

    label("loc_32B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_339")
    Jump("loc_3B2")

    label("loc_339")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_347")
    Jump("loc_3B2")

    label("loc_347")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_355")
    Jump("loc_3B2")

    label("loc_355")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_363")
    Jump("loc_3B2")

    label("loc_363")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_3A9")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6B, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_3A4")
    SetChrChipByIndex(0xA, 0x3)
    SetChrSubChip(0xA, 0x0)
    EndChrThread(0xA, 0x0)
    SetChrBattleFlags(0xA, 0x4)
    ClearChrFlags(0xA, 0x80)
    SetChrChipByIndex(0xB, 0x4)
    SetChrSubChip(0xB, 0x0)
    EndChrThread(0xB, 0x0)
    SetChrBattleFlags(0xB, 0x4)
    ClearChrFlags(0xB, 0x80)

    label("loc_3A4")

    Jump("loc_3B2")

    label("loc_3A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_3B2")

    label("loc_3B2")

    Return()

    # Function_2_22B end

    def Function_3_3B3(): pass

    label("Function_3_3B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3FC")
    SetMapObjFrame(0xFF, "hikari00_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hikari01_add", 0x0, 0x1)
    Sound(128, 1, 50, 0)

    label("loc_3FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_43B")
    OP_7D(0xD2, 0xD2, 0xE6, 0x0, 0x0)
    SetMapObjFrame(0xFF, "hikari00_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hikari01_add", 0x0, 0x1)

    label("loc_43B")

    Return()

    # Function_3_3B3 end

    def Function_4_43C(): pass

    label("Function_4_43C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_5A1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_518")

    #C0001
    ChrTalk(
        0xFE,
        (
            "虽然克洛斯贝尔已经\x01",
            "逐渐恢复到了以往的状态，\x01",
            "但问题仍然堆积如山。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0xFE,
        (
            "受到与各国断交的影响，\x01",
            "所有商店的储备\x01",
            "都不是很充足。\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0xFE,
        (
            "必须要与麦克道尔\x01",
            "议长他们取得联络，\x01",
            "并努力思考有效对策。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_59C")

    label("loc_518")


    #C0004
    ChrTalk(
        0xFE,
        (
            "虽然克洛斯贝尔已经\x01",
            "逐渐恢复到了以往的状态，\x01",
            "但问题仍然堆积如山。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0xFE,
        (
            "必须要与麦克道尔\x01",
            "议长他们取得联络，\x01",
            "并努力思考有效对策。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_59C")

    Jump("loc_152F")

    label("loc_5A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_6F2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_66A")

    #C0006
    ChrTalk(
        0xFE,
        (
            "唔唔，不知道经营露天店\x01",
            "的各位如今可好。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0xFE,
        (
            "虽说下达了戒严令，但很多人\x01",
            "还是希望继续做生意，\x01",
            "所以我便批准了他们的要求……\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0xFE,
        (
            "万一他们出现什么意外，\x01",
            "就都是我的责任了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_6ED")

    label("loc_66A")


    #C0009
    ChrTalk(
        0xFE,
        (
            "唔唔，不知道经营露天店\x01",
            "的各位如今可好。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0xFE,
        (
            "万一他们出现什么意外，\x01",
            "批准他们在戒严令生效期间继续\x01",
            "做生意的我就要承担主要责任。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6ED")

    Jump("loc_152F")

    label("loc_6F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_8E3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_854")

    #C0011
    ChrTalk(
        0xFE,
        (
            "在迪塔先生的演说中……\x01",
            "麦克道尔议长并没有现身，\x01",
            "真是令人在意啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0xFE,
        (
            "艾莉，\x01",
            "你了解什么情况吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x102,
        (
            "#00103F……不，\x01",
            "其实我也有些在意……\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0xFE,
        (
            "嗯，是吗……\x01",
            "难免要担心的。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0xFE,
        (
            "不管怎么说，\x01",
            "既然事情已经发展到这种地步了，\x01",
            "与两大国的对立恐怕是无法避免的。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0xFE,
        (
            "工商协会有必要发起呼吁，\x01",
            "让市民做好准备，预防特殊情况的发生……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_8DE")

    label("loc_854")


    #C0017
    ChrTalk(
        0xFE,
        (
            "既然事情已经发展到这种地步了，\x01",
            "与两大国的对立恐怕是无法避免的。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0xFE,
        (
            "工商协会有必要发起呼吁，\x01",
            "让市民做好准备，预防特殊情况的发生……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8DE")

    Jump("loc_152F")

    label("loc_8E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_8F1")
    Jump("loc_152F")

    label("loc_8F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_A1F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9B5")

    #C0019
    ChrTalk(
        0xFE,
        (
            "唔，竟然在居民投票活动\x01",
            "即将到来之际\x01",
            "发生那种事件……\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0xFE,
        (
            "若是处理不善，恐怕会\x01",
            "成为被帝国和共和国\x01",
            "加以利用的绝好材料。\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0xFE,
        (
            "不管怎么说，真希望\x01",
            "这起事件能尽早解决。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_A1A")

    label("loc_9B5")


    #C0022
    ChrTalk(
        0xFE,
        (
            "毕竟帝国和共和国\x01",
            "原本就已了解\x01",
            "我们的治安状况较差。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0xFE,
        (
            "不管怎么说，真希望\x01",
            "这起事件能尽早解决。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A1A")

    Jump("loc_152F")

    label("loc_A1F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_B73")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AEF")

    #C0024
    ChrTalk(
        0xFE,
        (
            "听说昨天那起列车事故\x01",
            "是由一只来历不明的怪物\x01",
            "引起的……\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0xFE,
        (
            "唔，和最近这段时间\x01",
            "被人目击到的那种不可思议的怪物\x01",
            "是不是同一种类呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0xFE,
        (
            "最近的意外事件真多啊，\x01",
            "你们也要多加小心。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_B6E")

    label("loc_AEF")


    #C0027
    ChrTalk(
        0xFE,
        (
            "不知道引起列车事故的怪物\x01",
            "和最近盛传的那种不可思议\x01",
            "的怪物是不是同一种类……\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0xFE,
        (
            "最近的意外事件真多啊，\x01",
            "你们也要多加小心。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B6E")

    Jump("loc_152F")

    label("loc_B73")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_B81")
    Jump("loc_152F")

    label("loc_B81")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_B8F")
    Jump("loc_152F")

    label("loc_B8F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_D9E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CF1")

    #C0029
    ChrTalk(
        0xFE,
        (
            "克洛斯贝尔自治州独立……\x01",
            "迪塔市长真是做出了\x01",
            "相当大胆的宣言啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0xFE,
        (
            "不过，我们如今在整个大陆的\x01",
            "影响力之强是前所未有的，\x01",
            "现在确实是独立的最好时机。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0xFE,
        (
            "在漫长的历史中，克洛斯贝尔一直被两大国所支配，\x01",
            "不断丧失自己的骄傲和自尊……\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0xFE,
        (
            "虽然今后也许会面对各种磨难，\x01",
            "但我真的很希望以实现独立为契机，\x01",
            "将当初的骄傲和自尊找回来。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_D99")

    label("loc_CF1")


    #C0033
    ChrTalk(
        0xFE,
        (
            "……对了，为了声援市长，\x01",
            "继续推动最近这种势头，\x01",
            "我们正在策划一场活动。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0xFE,
        (
            "这是一项和克洛斯贝尔通讯社共同推行的活动，\x01",
            "相信一定能为市民们带来活力。\x01",
            "敬请诸位期待。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D99")

    Jump("loc_152F")

    label("loc_D9E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_E8B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E3A")

    #C0035
    ChrTalk(
        0xFE,
        "通商会议终于开始了。\x02",
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0xFE,
        (
            "我们这些市民\x01",
            "也只能等待克洛斯贝尔\x01",
            "时代周刊发表的结果了。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0xFE,
        (
            "嗯……\x01",
            "究竟会是一场怎样的会议呢……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_E86")

    label("loc_E3A")


    #C0038
    ChrTalk(
        0xFE,
        (
            "我原本很想去\x01",
            "会议现场看看的。\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0xFE,
        (
            "嗯……\x01",
            "究竟会是一场怎样的会议呢……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E86")

    Jump("loc_152F")

    label("loc_E8B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_F0A")

    #C0040
    ChrTalk(
        0xFE,
        (
            "我孙子洛依\x01",
            "好像开始对经营\x01",
            "露天店产生兴趣了。\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0xFE,
        (
            "……我当年也是个经营露天店的商人。\x01",
            "嗯，这真是血脉相承啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_152F")

    label("loc_F0A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1018")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 3)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_FA4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F3E")
    Call(0, 9)
    Jump("loc_F9F")

    label("loc_F3E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 0)), scpexpr(EXPR_END)), "loc_F9F")

    #C0042
    ChrTalk(
        0x8,
        (
            "唔，真没想到\x01",
            "黑月长老的孙子\x01",
            "会来我家。\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x8,
        (
            "不管怎么说，\x01",
            "希望你能喜欢\x01",
            "这座城市哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F9F")

    Jump("loc_1013")

    label("loc_FA4")


    #C0044
    ChrTalk(
        0xFE,
        (
            "在通商会议中，各国代表\x01",
            "主要会针对经济相关方面\x01",
            "的问题展开协商。\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0xFE,
        (
            "我们工商协会也在\x01",
            "密切注意会议的动向。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1013")

    Jump("loc_152F")

    label("loc_1018")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_1325")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6B, 0x0, 0x2)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_11F4")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6B, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1195")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1163")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10FF")

    #C0046
    ChrTalk(
        0xFE,
        (
            "哦，这不是罗伊德吗，\x01",
            "有什么事吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x101,
        (
            "#00000F那个……\x01",
            "请问梅琳\x01",
            "在家吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0xFE,
        (
            "嗯？我记得她\x01",
            "刚才回来了……\x01",
            "难道又出门了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0xFE,
        (
            "不好意思，你还是\x01",
            "问问我老伴吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_115E")

    label("loc_10FF")


    #C0050
    ChrTalk(
        0xFE,
        (
            "我一直在工作，\x01",
            "都没注意到\x01",
            "孙女出门了。\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0xFE,
        (
            "如果想打听我孙女的情况，\x01",
            "还是去问问我老伴吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_115E")

    Jump("loc_1190")

    label("loc_1163")


    #C0052
    ChrTalk(
        0xFE,
        (
            "接下来，得继续处理\x01",
            "工商协会的工作了……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1190")

    Jump("loc_11F0")

    label("loc_1195")


    #C0053
    ChrTalk(
        0xFE,
        (
            "本想教训\x01",
            "洛依那小子\x01",
            "几句……\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0xFE,
        (
            "但在梅琳面前开口\x01",
            "也不太好。\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0xFE,
        "今天就先放过他吧。\x02",
    )

    CloseMessageWindow()

    label("loc_11F0")

    TalkEnd(0xFE)
    Return()

    label("loc_11F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12D2")

    #C0056
    ChrTalk(
        0xFE,
        (
            "在教团事件暴发之前召开的\x01",
            "克洛斯贝尔预算会议，在中断\x01",
            "一段时间后要再次开幕了。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0xFE,
        (
            "接下来将以新市长和新议长为中心，\x01",
            "重新制定不涉及利益牵扯\x01",
            "的新预算方案。\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0xFE,
        (
            "嗯，市政状况\x01",
            "总算开始向\x01",
            "好的方向发展了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1320")

    label("loc_12D2")


    #C0059
    ChrTalk(
        0xFE,
        (
            "市政状况总算开始向\x01",
            "好的方向发展了。\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0xFE,
        (
            "这都是新市长\x01",
            "和新议长的功劳啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1320")

    Jump("loc_152F")

    label("loc_1325")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_152F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12F, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14D1")

    #C0061
    ChrTalk(
        0xFE,
        (
            "哦……罗伊德，还有\x01",
            "麦克道尔议长家的大小姐啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0xFE,
        (
            "好久不见了，\x01",
            "你们好像很有精神啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x101,
        "#00000F您好，摩尔斯会长。\x02",
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x102,
        "#00100F久疏问候了。\x02",
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x105,
        (
            "#10300F您好像是统率东街众商人\x01",
            "的工商协会会长吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x109,
        (
            "#10105F啊，这位是……\x01",
            "（妈妈当年经营露天店时，\x01",
            "  也曾受到过他的关照呢。）\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0xFE,
        (
            "唔，增加了新面孔啊，\x01",
            "看来特别任务支援科\x01",
            "总算要重新开始工作了。\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0xFE,
        (
            "我们这些市民\x01",
            "都很期待你们的表现，\x01",
            "请努力加油吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x12F, 1)
    Jump("loc_152F")

    label("loc_14D1")


    #C0069
    ChrTalk(
        0xFE,
        (
            "我很期待你们特别任务\x01",
            "支援科今后的表现。\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0xFE,
        (
            "如果有什么事情需要我帮忙，\x01",
            "随时都可以过来。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_152F")

    TalkEnd(0xFE)
    Return()

    # Function_4_43C end

    def Function_5_1533(): pass

    label("Function_5_1533")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6B, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6B, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6B, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_155C")
    Call(0, 8)
    Return()

    label("loc_155C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_16A1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1619")

    #C0071
    ChrTalk(
        0xFE,
        (
            "总统已经被拘捕了，\x01",
            "我们今后又该怎么做呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0xFE,
        (
            "对克洛斯贝尔的广大居民来说，\x01",
            "这可是比任何事都重要的问题。\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0xFE,
        (
            "希望大家集思广益，\x01",
            "让情况向好的方向发展。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_169C")

    label("loc_1619")


    #C0074
    ChrTalk(
        0xFE,
        (
            "今后应该怎么做呢……\x01",
            "对克洛斯贝尔的广大居民来说，\x01",
            "这可是比任何事都重要的问题。\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0xFE,
        (
            "希望大家集思广益，\x01",
            "让情况向好的方向发展。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_169C")

    Jump("loc_22B1")

    label("loc_16A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_1704")

    #C0076
    ChrTalk(
        0xFE,
        (
            "有洛依和爷爷\x01",
            "在认真看守，\x01",
            "可怕的东西不会进来的。\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0xFE,
        (
            "所以，梅琳，\x01",
            "不用害怕哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_22B1")

    label("loc_1704")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_184D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17D4")

    #C0078
    ChrTalk(
        0xFE,
        (
            "迪塔先生竟然发表了独立宣言……\x01",
            "这是不是为时尚早呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0xFE,
        (
            "世间的一切事物\x01",
            "都在不断变化着，\x01",
            "我也想理解这一点……\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0xFE,
        (
            "不……克洛斯贝尔\x01",
            "如今的状况或许已经\x01",
            "不能用此言来形容了……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1848")

    label("loc_17D4")


    #C0081
    ChrTalk(
        0xFE,
        (
            "一切事物都在急剧变化，\x01",
            "对我们这些老年人来说，\x01",
            "真是很可怕呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0xFE,
        (
            "克洛斯贝尔\x01",
            "已经到了\x01",
            "再也无法回头的地步呢……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1848")

    Jump("loc_22B1")

    label("loc_184D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_18C8")

    #C0083
    ChrTalk(
        0xFE,
        (
            "我老伴去市民会馆\x01",
            "处理工商协会的事情了。\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0xFE,
        (
            "洛依好像也要在\x01",
            "这次的慈善宴会中帮忙……\x01",
            "不知结果将会如何。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_22B1")

    label("loc_18C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_192E")

    #C0085
    ChrTalk(
        0xFE,
        (
            "总之，现在能做的\x01",
            "也只有向女神祈祷了。\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0xFE,
        (
            "希望克洛斯贝尔的人们\x01",
            "不要再白白流血……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_22B1")

    label("loc_192E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_19B1")

    #C0087
    ChrTalk(
        0xFE,
        (
            "最近的状况真是让人搞不懂，\x01",
            "随时都有可能发生意外……\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0xFE,
        (
            "必须要好好提醒洛依和梅琳，\x01",
            "让他们在外走动时\x01",
            "多加小心。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_22B1")

    label("loc_19B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_1A0C")

    #C0089
    ChrTalk(
        0xFE,
        (
            "嗯……\x01",
            "老头子和梅琳\x01",
            "应该快回来了吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0xFE,
        (
            "我准备好红茶和点心\x01",
            "等他们吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_22B1")

    label("loc_1A0C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1A7A")

    #C0091
    ChrTalk(
        0xFE,
        (
            "老头子现在\x01",
            "大概在街上\x01",
            "陪梅琳玩。\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0xFE,
        (
            "呵呵，能在难得的假期\x01",
            "陪孙女一起玩，\x01",
            "他好像很开心呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_22B1")

    label("loc_1A7A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1AEC")

    #C0093
    ChrTalk(
        0xFE,
        (
            "工商协会好像也在帮忙准备\x01",
            "居民投票活动呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0xFE,
        (
            "接下来究竟会如何发展呢……\x01",
            "我真是完全搞不懂啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_22B1")

    label("loc_1AEC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1B6B")

    #C0095
    ChrTalk(
        0xFE,
        (
            "老头子身为工商协会的会长，\x01",
            "总是要考虑各种各样的问题。\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0xFE,
        (
            "他都已经一大把年纪了，\x01",
            "希望他不要\x01",
            "太勉强自己啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_22B1")

    label("loc_1B6B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1C83")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C1C")

    #C0097
    ChrTalk(
        0xFE,
        (
            "洛依以前总是无精打采的，\x01",
            "让我老伴\x01",
            "非常头疼……\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0xFE,
        (
            "但他最近已开始努力，\x01",
            "在工商协会帮起了忙……\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0xFE,
        (
            "如果将来能取得成就，\x01",
            "老头子一定会很高兴的。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1C7E")

    label("loc_1C1C")


    #C0100
    ChrTalk(
        0xFE,
        (
            "洛依最近已开始努力，\x01",
            "在工商协会帮起了忙……\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0xFE,
        (
            "如果将来能取得成就，\x01",
            "他爷爷一定会很高兴的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C7E")

    Jump("loc_22B1")

    label("loc_1C83")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1FAE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 3)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1E97")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DC, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E4F")

    #C0102
    ChrTalk(
        0x9,
        (
            "哎呀呀，是你们啊。\x01",
            "今天还带来了一位\x01",
            "可爱的小朋友呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0x1A2,
        (
            "嗯，夫人，\x01",
            "打扰您了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x1A2, 500)
    Sleep(300)

    #C0104
    ChrTalk(
        0x9,
        (
            "呵呵，哪里的话。\x01",
            "你真是很懂礼貌啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0x9,
        "要不要喝杯红茶？\x02",
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0x1A2,
        (
            "不，\x01",
            "我们不准备久留，\x01",
            "所以不必劳烦了。\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0x102,
        "#00100F（呵呵，社交能力真出色啊。）\x02",
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0x101,
        "#00006F（该怎么说呢……）\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_1DF0")

    #C0109
    ChrTalk(
        0x104,
        "#00300F（嗯，无可挑剔啊。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_1E47")

    label("loc_1DF0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_1E1D")

    #C0110
    ChrTalk(
        0x109,
        "#10100F（嗯，无可挑剔。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_1E47")

    label("loc_1E1D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_1E47")

    #C0111
    ChrTalk(
        0x105,
        "#10300F（嗯，无可挑剔呢。）\x02",
    )

    CloseMessageWindow()

    label("loc_1E47")

    SetScenarioFlags(0x1DC, 2)
    Jump("loc_1E92")

    label("loc_1E4F")


    #C0112
    ChrTalk(
        0x9,
        (
            "呵呵，真是个\x01",
            "懂礼貌的好孩子啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0x9,
        "真希望洛依也能向你学学。\x02",
    )

    CloseMessageWindow()

    label("loc_1E92")

    Jump("loc_1FA9")

    label("loc_1E97")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F51")

    #C0114
    ChrTalk(
        0xFE,
        (
            "连一向对政治状况\x01",
            "抱怨不断的老头子\x01",
            "都对迪塔市长赞许有加呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0xFE,
        (
            "再怎么说，迪塔市长毕竟是\x01",
            "天下闻名的ＩＢＣ的管理者啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0xFE,
        (
            "在通商会议中，\x01",
            "他也一定会有活跃表现吧？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1FA9")

    label("loc_1F51")


    #C0117
    ChrTalk(
        0xFE,
        (
            "连老头子都对新市长\x01",
            "赞许有加呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0xFE,
        (
            "在通商会议中，\x01",
            "迪塔市长也一定会有活跃表现吧？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1FA9")

    Jump("loc_22B1")

    label("loc_1FAE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_2198")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6B, 0x0, 0x2)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2145")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6B, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2105")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 4)), scpexpr(EXPR_END)), "loc_2100")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2084")

    #C0119
    ChrTalk(
        0xFE,
        (
            "洛依和梅琳\x01",
            "去雨中散步了。\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0xFE,
        (
            "我想他们应该\x01",
            "不会走得太远，\x01",
            "不妨去附近的街区找找看。\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0x9,
        (
            "洛依撑着绿色的伞，\x01",
            "梅琳撑着粉色的伞，\x01",
            "应该都挺显眼的。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2100")

    label("loc_2084")


    #C0122
    ChrTalk(
        0xFE,
        (
            "我想洛依和梅琳\x01",
            "应该不会走得很远，\x01",
            "不妨去附近的街区找找看。\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0x9,
        (
            "洛依撑着绿色的伞，\x01",
            "梅琳撑着粉色的伞，\x01",
            "应该都挺显眼的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2100")

    Jump("loc_2141")

    label("loc_2105")


    #C0124
    ChrTalk(
        0xFE,
        (
            "两个孙儿\x01",
            "都回来了……\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0xFE,
        (
            "我来给他们冲杯\x01",
            "热柠檬汁吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2141")

    TalkEnd(0xFE)
    Return()

    label("loc_2145")


    #C0126
    ChrTalk(
        0xFE,
        (
            "唔，雨势虽然减小了，\x01",
            "但还是没有停呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0xFE,
        (
            "洛依他们到底\x01",
            "去哪里买东西了？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_22B1")

    label("loc_2198")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_22B1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12F, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2264")

    #C0128
    ChrTalk(
        0xFE,
        "哦哦，你们是……！\x02",
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0x101,
        "#00002F老婆婆，好久不见了。\x02",
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0xFE,
        (
            "嗯嗯，好久不见。\x01",
            "你们好像很有精神啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0xFE,
        (
            "已经见过\x01",
            "老头子了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0xFE,
        (
            "他就在上面，\x01",
            "如果方便，\x01",
            "就去和他打个招呼吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x12F, 2)
    Jump("loc_22B1")

    label("loc_2264")


    #C0133
    ChrTalk(
        0xFE,
        (
            "已经见过\x01",
            "老头子了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0xFE,
        (
            "他就在上面，\x01",
            "如果方便，\x01",
            "就去和他打个招呼吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_22B1")

    TalkEnd(0xFE)
    Return()

    # Function_5_1533 end

    def Function_6_22B5(): pass

    label("Function_6_22B5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_23AA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2348")

    #C0135
    ChrTalk(
        0xFE,
        (
            "不用担心啦，爷爷。\x01",
            "库隆克先生他们\x01",
            "一定不会有事的。\x02",
        )
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0xFE,
        (
            "现在也没办法去\x01",
            "市民会馆咨询，\x01",
            "还是好好待在家里吧。\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xA, 0x10)
    SetScenarioFlags(0x0, 2)
    Jump("loc_23A5")

    label("loc_2348")


    #C0137
    ChrTalk(
        0xFE,
        (
            "库隆克先生他们\x01",
            "一定不会有事的。\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0xFE,
        (
            "现在也没办法去\x01",
            "市民会馆咨询，\x01",
            "还是好好待在家里吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_23A5")

    Jump("loc_23F6")

    label("loc_23AA")


    #C0139
    ChrTalk(
        0xFE,
        (
            "哟，你们好像已经把雨伞\x01",
            "送回去了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0xFE,
        (
            "以后我也得\x01",
            "再细心一些才行……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_23F6")

    TalkEnd(0xFE)
    Return()

    # Function_6_22B5 end

    def Function_7_23FA(): pass

    label("Function_7_23FA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_2442")

    #C0141
    ChrTalk(
        0xFE,
        (
            "哥哥和爷爷让我\x01",
            "待在这里别出去。\x02",
        )
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0xFE,
        "好害怕啊……\x02",
    )

    CloseMessageWindow()
    Jump("loc_246E")

    label("loc_2442")


    #C0143
    ChrTalk(
        0xFE,
        "（嚼嚼）……\x02",
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0xFE,
        "哥哥，这面包真好吃！\x02",
    )

    CloseMessageWindow()

    label("loc_246E")

    TalkEnd(0xFE)
    Return()

    # Function_7_23FA end

    def Function_8_2472(): pass

    label("Function_8_2472")

    EventBegin(0x0)
    Fade(500)
    OP_68(-610, 1000, 9780, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(21000, 0)
    SetChrPos(0x101, -1400, 20, 9580, 90)
    SetChrPos(0x102, -2470, 0, 10160, 90)
    SetChrPos(0x109, -2700, 30, 8760, 90)
    SetChrPos(0x105, -3840, 30, 9080, 90)
    OP_4B(0x9, 0xFF)
    OP_0D()

    #C0145
    ChrTalk(
        0x101,
        "#6P#00000F打扰了，您好。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x101, 500)

    #C0146
    ChrTalk(
        0x9,
        (
            "哦，你们好啊。\x01",
            "在这种下雨天过来，真是少见啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0x101,
        (
            "#6P#00003F嗯，有件事情\x01",
            "想问问您。\x02\x03",

            "#00000F请问您见过这把伞吗？\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    #A0148
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "罗伊德向夫人出示了\x01",
            "梅琳的伞。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0149
    ChrTalk(
        0x9,
        (
            "啊，这不是……\x01",
            "梅琳的伞吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0x9,
        "你们特意帮忙送回来吗？\x02",
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0151
    ChrTalk(
        0x9,
        "啊，可是……\x02",
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0x9,
        (
            "我记得那孩子\x01",
            "从面包店回来时\x01",
            "是带着伞的。\x02",
        )
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0x101,
        "#6P#00003F那个，其实是这样的……\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    #A0154
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "罗伊德将\x01",
            "帮小桃寻找雨伞\x01",
            "一事做了说明。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0155
    ChrTalk(
        0x9,
        (
            "哦哦，原来是\x01",
            "这么回事啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0x9,
        (
            "真对不起那个\x01",
            "叫小桃的孩子呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0x105,
        (
            "#6P#10305F夫人，请问您的\x01",
            "孙女现在在哪里？\x02\x03",

            "#10300F好像不在\x01",
            "这里呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0x9,
        (
            "嗯，她刚才和洛依一起\x01",
            "打着伞出去散步了。\x02",
        )
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0x9,
        (
            "……不好意思，\x01",
            "我忘记问他们\x01",
            "要去哪里了。\x02",
        )
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0x109,
        (
            "#6P#10103F嗯，看来是\x01",
            "和他们错过了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0x102,
        (
            "#6P#00100F在这种下雨天，\x01",
            "应该不会走太远吧？\x02\x03",

            "#00104F说到离东街较近的地方，\x01",
            "有中央广场、港湾区和旧城区……\x01",
            "我想他们应该就在这几个地方之一。\x02",
        )
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0x9,
        "嗯，应该没错。\x02",
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0x9,
        (
            "洛依撑着绿色的伞，\x01",
            "梅琳撑着粉色的伞，\x01",
            "应该都挺显眼的，你们去找找看吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0x109,
        (
            "#6P#10100F绿色和粉色的雨伞……\x01",
            "的确很醒目呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0x101,
        (
            "#6P#00000F嗯，那我们赶快去找吧。\x02\x03",

            "#00004F谢谢您的合作。\x02",
        )
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0x9,
        (
            "哪里哪里，\x01",
            "以后有空时再来做客哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, -3270, 20, 8130, 225)
    OP_93(0x9, 0x0, 0x0)
    OP_4C(0x9, 0xFF)
    SetScenarioFlags(0x132, 4)
    OP_29(0x6B, 0x1, 0x1)
    EventEnd(0x5)
    Return()

    # Function_8_2472 end

    def Function_9_296C(): pass

    label("Function_9_296C")

    EventBegin(0x0)
    Fade(500)
    OP_68(630, 5020, 6780, 0)
    MoveCamera(44, 20, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(18950, 0)
    SetChrPos(0x8, 390, 4019, 5600, 0)
    SetChrPos(0x1A2, -600, 4000, 8580, 180)
    SetChrPos(0x101, 390, 4019, 6840, 180)
    SetChrPos(0x102, 390, 4019, 8320, 180)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_2A04")
    SetChrPos(0x104, 1590, 4019, 8580, 180)
    Jump("loc_2A3D")

    label("loc_2A04")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_2A23")
    SetChrPos(0x109, 1590, 4019, 8580, 180)
    Jump("loc_2A3D")

    label("loc_2A23")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_2A3D")
    SetChrPos(0x105, 1590, 4019, 8580, 180)

    label("loc_2A3D")

    OP_4B(0x8, 0xFF)
    OP_0D()

    #C0167
    ChrTalk(
        0x8,
        "#12P哦，这不是罗伊德和各位吗。\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_2A80():

        label("loc_2A80")

        TurnDirection(0xFE, 0x1A2, 500)
        Yield()
        Jump("loc_2A80")

    QueueWorkItem2(0x8, 1, lambda_2A80)
    Sleep(300)

    #C0168
    ChrTalk(
        0x8,
        (
            "#12P那个孩子……\x01",
            "虽然一身东方打扮，\x01",
            "但好像从没见过呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_9B(0x0, 0x1A2, 0x0, 0x7D0, 0x7D0, 0x0)
    TurnDirection(0x1A2, 0x8, 500)
    Sleep(300)
    EndChrThread(0x8, 0x1)

    #C0169
    ChrTalk(
        0x1A2,
        (
            "#6P原来如此，您就是\x01",
            "克洛斯贝尔工商协会的会长啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0x1A2,
        (
            "#6P我的名字是秦，\x01",
            "肩负着『黑月』未来的男子汉！\x02",
        )
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0x8,
        (
            "#12P唔，说起『黑月』，\x01",
            "好像是不久前进驻到克洛斯贝尔\x01",
            "的那个东方人街组织吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0x8,
        (
            "#12P你刚才说肩负着『黑月』的未来，\x01",
            "莫非与长老会有什么关系吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0x1A2,
        (
            "#6P嗯，事实上，\x01",
            "我的祖父就是长老之一。\x02",
        )
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0x1A2,
        (
            "#6P摩尔斯先生，莫非您\x01",
            "认识长老们吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0x8,
        (
            "#12P不不，只是在商业方面\x01",
            "有少许往来而已，\x01",
            "并没有直接会面过。\x02",
        )
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0x8,
        (
            "#12P唔，话说回来，\x01",
            "不愧是长老的孙子啊，\x01",
            "实在是相当聪明。\x02",
        )
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0x8,
        (
            "#12P不过，你为什么会和\x01",
            "罗伊德他们在一起？\x02",
        )
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0x101,
        (
            "#00009F这个嘛……\x01",
            "说来话长了。\x02",
        )
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0x1A2,
        (
            "#6P呵呵，这些人\x01",
            "纠缠不休，非要陪我\x01",
            "在市区游览。\x02",
        )
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0x1A2,
        (
            "#6P我实在没办法，\x01",
            "也只能陪陪他们了。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_2E12")
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    def lambda_2DC9():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2DC9)
    Sleep(50)

    def lambda_2DD9():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2DD9)
    Sleep(50)

    def lambda_2DE9():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2DE9)
    Sleep(300)

    #C0181
    ChrTalk(
        0x104,
        "#11P#00306F喂喂……\x02",
    )

    CloseMessageWindow()
    Jump("loc_2F55")

    label("loc_2E12")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_2EB4")
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    def lambda_2E6B():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2E6B)
    Sleep(50)

    def lambda_2E7B():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2E7B)
    Sleep(50)

    def lambda_2E8B():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_2E8B)
    Sleep(300)

    #C0182
    ChrTalk(
        0x109,
        "#11P#10106F那个……\x02",
    )

    CloseMessageWindow()
    Jump("loc_2F55")

    label("loc_2EB4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_2F55")
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    def lambda_2F0D():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2F0D)
    Sleep(50)

    def lambda_2F1D():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2F1D)
    Sleep(50)

    def lambda_2F2D():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_2F2D)
    Sleep(300)

    #C0183
    ChrTalk(
        0x105,
        "#11P#10306F呼，哎呀呀。\x02",
    )

    CloseMessageWindow()

    label("loc_2F55")


    #C0184
    ChrTalk(
        0x8,
        (
            "#12P哈哈，虽然不知道是怎么回事，\x01",
            "但你们相处得好像不错呢，这就好。\x02",
        )
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0x8,
        (
            "#12P你是叫秦吧？\x01",
            "如果你能喜欢上克洛斯贝尔这座城市，\x01",
            "我会很高兴的。\x02",
        )
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0x1A2,
        (
            "#6P嗯，我会用心观摩的。\x01",
            "那么，就此告辞了。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, 390, 4019, 8320, 0)
    OP_4C(0x8, 0xFF)
    SetScenarioFlags(0x1CA, 0)
    OP_29(0x73, 0x1, 0x7)
    EventEnd(0x5)
    Return()

    # Function_9_296C end

    SaveToFile()

Try(main)
