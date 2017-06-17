from ScenarioHelper import *

def main():
    CreateScenaFile(
        "e4400.bin",                # FileName
        "e4400",                    # MapName
        "e4400",                    # Location
        0x0000,                     # MapIndex
        "ed7570",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0xFF,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 2],
    )

    BuildStringList((
        "e4400",                  # 0
        "艾莉",                   # 1
        "莉夏",                   # 2
        "神狼蔡特",               # 3
        "格蕾丝",                 # 4
    ))

    AddCharChip((
        "chr/ch00100.itc",                   # 00
        "chr/ch03200.itc",                   # 01
        "chr/ch02708.itc",                   # 02
        "chr/ch06000.itc",                   # 03
    ))

    DeclNpc(-2930,   0,       509,     270,  389,  0x0, 0,   0,   0,   0,   0,   0,   3,   255,  0)
    DeclNpc(2589,    0,       -29,     90,   389,  0x0, 0,   1,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(-1549,   0,       -959,    180,  405,  0x0, 0,   2,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(-2930,   0,       509,     270,  389,  0x0, 0,   3,   0,   0,   0,   0,   9,   255,  0)

    ChipFrameInfo(324, 0)                                        # 0

    ScpFunction((
        "Function_0_144",          # 00, 0
        "Function_1_1F4",          # 01, 1
        "Function_2_2BE",          # 02, 2
        "Function_3_382",          # 03, 3
        "Function_4_52D",          # 04, 4
        "Function_5_8CD",          # 05, 5
        "Function_6_BD3",          # 06, 6
        "Function_7_E52",          # 07, 7
        "Function_8_115A",         # 08, 8
        "Function_9_12E1",         # 09, 9
        "Function_10_1909",        # 0A, 10
        "Function_11_1AFB",        # 0B, 11
    ))


    def Function_0_144(): pass

    label("Function_0_144")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_17C"),
        (1, "loc_188"),
        (2, "loc_194"),
        (3, "loc_1A0"),
        (4, "loc_1AC"),
        (5, "loc_1B8"),
        (6, "loc_1C4"),
        (SWITCH_DEFAULT, "loc_1D0"),
    )


    label("loc_17C")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_1DC")

    label("loc_188")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_1DC")

    label("loc_194")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_1DC")

    label("loc_1A0")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_1DC")

    label("loc_1AC")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_1DC")

    label("loc_1B8")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_1DC")

    label("loc_1C4")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_1DC")

    label("loc_1D0")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_1DC")

    label("loc_1DC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1F3")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_1DC")

    label("loc_1F3")

    Return()

    # Function_0_144 end

    def Function_1_1F4(): pass

    label("Function_1_1F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 4)), scpexpr(EXPR_END)), "loc_207")
    ClearChrFlags(0xB, 0x80)
    Jump("loc_2A8")

    label("loc_207")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 2)), scpexpr(EXPR_END)), "loc_21A")
    ClearChrFlags(0xB, 0x80)
    Jump("loc_2A8")

    label("loc_21A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_22D")
    ClearChrFlags(0xB, 0x80)
    Jump("loc_2A8")

    label("loc_22D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_240")
    ClearChrFlags(0x9, 0x80)
    Jump("loc_2A8")

    label("loc_240")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 1)), scpexpr(EXPR_END)), "loc_253")
    ClearChrFlags(0x8, 0x80)
    Jump("loc_2A8")

    label("loc_253")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 3)), scpexpr(EXPR_END)), "loc_266")
    ClearChrFlags(0xB, 0x80)
    Jump("loc_2A8")

    label("loc_266")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 7)), scpexpr(EXPR_END)), "loc_279")
    ClearChrFlags(0xA, 0x80)
    Jump("loc_2A8")

    label("loc_279")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_END)), "loc_28C")
    ClearChrFlags(0x9, 0x80)
    Jump("loc_2A8")

    label("loc_28C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_29A")
    Jump("loc_2A8")

    label("loc_29A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_2A8")
    ClearChrFlags(0xA, 0x80)

    label("loc_2A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_2BD")
    ClearScenarioFlags(0x22, 0)
    SetScenarioFlags(0x0, 0)
    SetScenarioFlags(0x0, 1)
    Event(0, 11)

    label("loc_2BD")

    Return()

    # Function_1_1F4 end

    def Function_2_2BE(): pass

    label("Function_2_2BE")

    OP_50(0x31, (scpexpr(EXPR_PUSH_LONG, 0xD0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2E4")
    Sound(132, 1, 70, 0)
    Sound(497, 1, 30, 0)
    ClearScenarioFlags(0x0, 1)
    Jump("loc_2F0")

    label("loc_2E4")

    Sound(132, 1, 100, 0)
    Sound(497, 1, 100, 0)

    label("loc_2F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_305")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 0)

    label("loc_305")

    OP_50(0x51, (scpexpr(EXPR_PUSH_LONG, 0xFF032877), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_F0(0x1, 0x7D0)
    SetMapFlags(0x10000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_345")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_33C")
    OP_7D(0xD7, 0xFF, 0xFF, 0x0, 0x0)
    Jump("loc_345")

    label("loc_33C")

    OP_7D(0xFF, 0xFF, 0xFF, 0x0, 0x0)

    label("loc_345")

    SetMapObjFrame(0x0, "door_l1", 0x0, 0x1)
    SetMapObjFrame(0x0, "door_l2", 0x0, 0x1)
    SetMapObjFrame(0x0, "door_r1", 0x0, 0x1)
    SetMapObjFrame(0x0, "door_r2", 0x0, 0x1)
    Return()

    # Function_2_2BE end

    def Function_3_382(): pass

    label("Function_3_382")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D6, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_397")
    Call(0, 4)
    Jump("loc_529")

    label("loc_397")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_483")

    #C0001
    ChrTalk(
        0xFE,
        (
            "#00103F独立无效宣言……\x01",
            "虽然现在还不知道\x01",
            "这样做是否正确……\x02\x03",

            "#00101F但以牺牲小琪雅为代价\x01",
            "而换取的和平，\x01",
            "绝对是有问题的。\x02\x03",

            "#00103F我们要把小琪雅带回来……\x01",
            "就算是为了向这个目标踏出第一步，\x01",
            "也一定要让此次作战取得成功。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_529")

    label("loc_483")


    #C0002
    ChrTalk(
        0xFE,
        (
            "#00103F独立无效宣言……\x01",
            "虽然现在还不知道\x01",
            "这样做是否正确……\x02\x03",

            "#00100F但我们必须要把小琪雅带回来……\x01",
            "就算是为了向这个目标踏出第一步，\x01",
            "也一定要让此次作战取得成功。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_529")

    TalkEnd(0xFE)
    Return()

    # Function_3_382 end

    def Function_4_52D(): pass

    label("Function_4_52D")


    #C0003
    ChrTalk(
        0x8,
        (
            "#00103F『克洛斯贝尔独立无效宣言』吗……\x01",
            "我们接下来要做的事情，\x01",
            "就只剩下寻找入侵网络的时机了。\x02\x03",

            "#00106F……呼，不由得紧张起来了。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x101,
        (
            "#00002F哈哈……这也难怪。\x02\x03",

            "#00003F毕竟我们即将亲手撼动\x01",
            "存在于克洛斯贝尔这片\x01",
            "土地上的短暂和平。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x8)

    #C0005
    ChrTalk(
        0x8,
        (
            "#00108F……我们要做的事情，\x01",
            "真的是正确的吗？\x02\x03",

            "#00103F多亏迪塔叔叔，居住在克洛斯贝尔的\x01",
            "广大居民才能免遭两大国的侵扰，\x01",
            "过着安定和平的生活……\x02\x03",

            "#00108F而我们却要从他们的手中\x01",
            "夺走这一切……\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x101,
        (
            "#00003F……是啊。\x02\x03",

            "#00001F但是，如今的和平\x01",
            "是建立在迪塔总统他们利用琪雅\x01",
            "这个基础上的。\x02\x03",

            "#00003F我想，绝大多数市民\x01",
            "对于此事应该毫不知情……\x01",
            "但失去琪雅对我们来说，是很重大的问题。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x8,
        (
            "#00108F……嗯，没错。\x02\x03",

            "#00103F以牺牲小琪雅为代价\x01",
            "而换取的和平，\x01",
            "绝对是有问题的。\x02\x03",

            "#00100F……呵呵，谢谢，罗伊德。\x01",
            "多亏你，我好像\x01",
            "已经没那么迷惘了。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x101,
        (
            "#00009F哈哈，能帮上忙就好。\x02\x03",

            "#00000F我们要把琪雅带回来……\x01",
            "为了这个目标，\x01",
            "必须让此次作战取得成功。\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x8,
        "#00100F嗯……我们一起努力吧。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1D6, 0)
    Return()

    # Function_4_52D end

    def Function_5_8CD(): pass

    label("Function_5_8CD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 4)), scpexpr(EXPR_END)), "loc_8DE")
    Jump("loc_BCF")

    label("loc_8DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_A6A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9D1")

    #C0010
    ChrTalk(
        0x9,
        (
            "#10703F『钢之圣女』……\x02\x03",

            "#10701F说起来，\x01",
            "我还没有向她讨回\x01",
            "打碎面具的那笔帐呢。\x02\x03",

            "#10706F面对那样的顶级高手，\x01",
            "我不知道自己能\x01",
            "坚持到什么程度……\x02\x03",

            "#10701F但我现在有无法退让、\x01",
            "必须要完成的使命。\x01",
            "……所以，绝不能输。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_A65")

    label("loc_9D1")


    #C0011
    ChrTalk(
        0x9,
        (
            "#10703F面对『钢之圣女』那样的顶级高手，\x01",
            "我不知道自己能\x01",
            "坚持到什么程度……\x02\x03",

            "#10701F但我现在有无法退让、\x01",
            "必须要完成的使命。\x01",
            "……所以，绝不能输。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A65")

    Jump("loc_BCF")

    label("loc_A6A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_END)), "loc_BCF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D8, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A85")
    Call(0, 6)
    Jump("loc_BCF")

    label("loc_A85")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B6B")

    #C0012
    ChrTalk(
        0x9,
        (
            "#10703F我潜伏在古战场的时候，\x01",
            "从国防军那里得到了有关\x01",
            "玛因兹反抗势力的消息。\x02\x03",

            "#10708F……如今想想，我曾蒙受过\x01",
            "『黑月』的不少照顾。\x02\x03",

            "但最后却以那种形式\x01",
            "废除了契约……\x02\x03",

            "#10703F将来一定要还\x01",
            "曹先生他们这个人情。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_BCF")

    label("loc_B6B")


    #C0013
    ChrTalk(
        0x9,
        (
            "#10708F……如今想想，我曾蒙受过\x01",
            "『黑月』的不少照顾。\x02\x03",

            "#10703F将来一定要还\x01",
            "曹先生他们这个人情。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BCF")

    TalkEnd(0xFE)
    Return()

    # Function_5_8CD end

    def Function_6_BD3(): pass

    label("Function_6_BD3")


    #C0014
    ChrTalk(
        0x9,
        (
            "#10702F伊莉娅小姐能够恢复意识……\x01",
            "真是太好了。\x02\x03",

            "#10703F…………………………………………\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x101,
        (
            "#00003F……莉夏，如果你想\x01",
            "和伊莉娅小姐见面，\x01",
            "不必客气，随时都可以和我说。\x02\x03",

            "#00000F我一定会找个机会，\x01",
            "让你去一趟乌尔斯拉医院。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x9,
        (
            "#10702F呵呵，\x01",
            "谢谢关心。\x02\x03",

            "#10703F但我已经决定，\x01",
            "现在要全力投入到解放\x01",
            "克洛斯贝尔市和彩虹剧团的作战中。\x02\x03",

            "#10701F这也是为了让自己\x01",
            "能昂首挺胸地\x01",
            "站在伊莉娅小姐面前……\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x101,
        (
            "#00000F……是吗。\x01",
            "既然如此，那我们就要\x01",
            "尽快达成这项任务了。\x02\x03",

            "#00004F如果这样能让你鼓起勇气\x01",
            "去和伊莉娅小姐见面，\x01",
            "我们也会更有动力的。\x02\x03",

            "#00000F为了琪雅、伊莉娅小姐，\x01",
            "还有同伴们……\x01",
            "我们就一起加油吧，莉夏。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x9,
        (
            "#10702F好的……！\x01",
            "请多指教！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1D8, 3)
    Return()

    # Function_6_BD3 end

    def Function_7_E52(): pass

    label("Function_7_E52")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 4)), scpexpr(EXPR_END)), "loc_E63")
    Jump("loc_1156")

    label("loc_E63")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 7)), scpexpr(EXPR_END)), "loc_FF0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F71")

    #C0019
    ChrTalk(
        0xA,
        (
            "#01203F#3C支援科的成员\x01",
            "已经陆续集结了。\x02\x03",

            "#01200F等到没有必要\x01",
            "直接帮助你们的时候，\x01",
            "我就会重回后方。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x101,
        (
            "#00004F嗯……我明白。\x02\x03",

            "#00000F不过，在那之前\x01",
            "就要拜托你了，蔡特。\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0xA,
        (
            "#01200F#3C呵呵，当然没问题。\x01",
            "我一定会切实履行\x01",
            "身为警犬的义务。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_FEB")

    label("loc_F71")


    #C0022
    ChrTalk(
        0xA,
        (
            "#01200F#3C等到没有必要\x01",
            "直接帮助你们的时候，\x01",
            "我就会重回后方。\x02\x03",

            "不过，我一定会切实履行\x01",
            "身为警犬的义务，\x01",
            "你尽管放心吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FEB")

    Jump("loc_1156")

    label("loc_FF0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_1156")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D8, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_100B")
    Call(0, 8)
    Jump("loc_1156")

    label("loc_100B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10E2")

    #C0023
    ChrTalk(
        0xA,
        (
            "#01203F#3C虽然我无法使用\x01",
            "你们所持有的\x01",
            "战术导力器……\x02\x03",

            "#01200F但身为神狼，我多少通晓一些法术，\x01",
            "在战技方面，也可以像之前一样\x01",
            "为你们提供帮助。\x02\x03",

            "罗伊德，你也要\x01",
            "让我好好见识一下\x01",
            "身为队长的实力啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_1156")

    label("loc_10E2")


    #C0024
    ChrTalk(
        0xA,
        (
            "#01200F#3C罗伊德，你也要\x01",
            "让我好好见识一下\x01",
            "身为队长的实力啊。\x02\x03",

            "#01203F呵呵，你就充分引发出\x01",
            "我这头神狼的力量吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1156")

    TalkEnd(0xFE)
    Return()

    # Function_7_E52 end

    def Function_8_115A(): pass

    label("Function_8_115A")


    #C0025
    ChrTalk(
        0xA,
        (
            "#01200F#3C乌尔斯拉医院啊…………\x02\x03",

            "#01203F……………………………\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x101,
        "#00005F蔡特……？\x02",
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0xA,
        (
            "#01203F#3C呵呵，没什么，\x01",
            "只是想起了一些过去的事情。\x02\x03",

            "#01200F话说回来，虽然以前\x01",
            "也帮助过你们很多次……\x02\x03",

            "但像现在这样并肩而行，\x01",
            "好像还是第一次呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x101,
        (
            "#00009F哈哈……的确如此。\x02\x03",

            "#00000F暂时就要请你多多关照了，\x01",
            "蔡特，万事拜托。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0xA,
        (
            "#01200F#3C呵呵，你也要\x01",
            "让我好好见识一下\x01",
            "身为队长的实力啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1D8, 7)
    Return()

    # Function_8_115A end

    def Function_9_12E1(): pass

    label("Function_9_12E1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 4)), scpexpr(EXPR_END)), "loc_146E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DA, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12FF")
    Call(0, 10)
    Jump("loc_1469")

    label("loc_12FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13F5")

    #C0030
    ChrTalk(
        0xB,
        (
            "#02105F真没想到你们能\x01",
            "把亚里欧斯·马克莱因\x01",
            "打败啊。\x02\x03",

            "#02102F呵呵，\x01",
            "你们有了如此显著的成长，\x01",
            "姐姐我也很高兴呢☆\x02\x03",

            "#02104F凭你们现在的实力，无论面对什么难关，\x01",
            "也都可以顺利跨越的。\x02\x03",

            "#02109F大家继续努力，\x01",
            "共同迎接美好的结局吧！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_1469")

    label("loc_13F5")


    #C0031
    ChrTalk(
        0xB,
        (
            "#02104F凭你们现在的实力，无论面对什么难关，\x01",
            "也都可以顺利跨越的。\x02\x03",

            "#02109F大家继续努力，\x01",
            "共同迎接美好的结局吧！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1469")

    Jump("loc_1905")

    label("loc_146E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 2)), scpexpr(EXPR_END)), "loc_15EB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1570")

    #C0032
    ChrTalk(
        0xB,
        (
            "#02104F我要趁在『大树』的这段时间，\x01",
            "尽量多拍些照片。\x02\x03",

            "#02100F回到通讯社之后，\x01",
            "我一定会把此次事件的\x01",
            "真相一举公开……\x02\x03",

            "#02102F所以你们一定要继续努力，\x01",
            "将这起事件完美解决哦！\x02\x03",

            "#02109F到时候，我一定会为你们\x01",
            "写一篇最棒的社会新闻！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_15E6")

    label("loc_1570")


    #C0033
    ChrTalk(
        0xB,
        (
            "#02100F罗伊德，你们一定要继续努力，\x01",
            "将这起事件完美解决哦！\x02\x03",

            "#02109F到时候，我一定会为你们\x01",
            "写一篇最棒的社会新闻！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15E6")

    Jump("loc_1905")

    label("loc_15EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1750")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16E3")

    #C0034
    ChrTalk(
        0xB,
        (
            "#02106F湿地居然出现了\x01",
            "那样的『大树』～\x02\x03",

            "#02100F它的大小远远超过了兰花塔，\x01",
            "就算在帝国或共和国，\x01",
            "说不定也能看得到吧。\x02\x03",

            "#02103F如今，整个大陆肯定都在关注\x01",
            "克洛斯贝尔的动向……\x02\x03",

            "#02102F既然如此，我也要\x01",
            "豁出性命跟随你们！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_174B")

    label("loc_16E3")


    #C0035
    ChrTalk(
        0xB,
        (
            "#02103F如今，整个大陆肯定都在关注\x01",
            "克洛斯贝尔的动向……\x02\x03",

            "#02102F既然如此，我也要\x01",
            "豁出性命跟随你们！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_174B")

    Jump("loc_1905")

    label("loc_1750")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 3)), scpexpr(EXPR_END)), "loc_1905")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1880")

    #C0036
    ChrTalk(
        0xB,
        (
            "#02103F救出身为自治州代表之一的\x01",
            "麦克道尔议长，\x01",
            "请他向国内外发表讲话……\x02\x03",

            "#02100F如果能实现这一计划，\x01",
            "国防军就不得不持\x01",
            "观望态度了。\x02\x03",

            "#02104F虽然还要想办法筹备\x01",
            "让议长发表讲话的方式及手段……\x01",
            "但一旦成功，必定会成为最重大的独家新闻！\x02\x03",

            "#02102F呵呵，你们就努力\x01",
            "把议长救出来吧！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_1905")

    label("loc_1880")


    #C0037
    ChrTalk(
        0xB,
        (
            "#02104F请麦克道尔议长发表意见……\x01",
            "要想撼动独立国的正当性，\x01",
            "应该没有比这更好的办法了。\x02\x03",

            "#02102F呵呵，你们就努力\x01",
            "把议长救出来吧！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1905")

    TalkEnd(0xFE)
    Return()

    # Function_9_12E1 end

    def Function_10_1909(): pass

    label("Function_10_1909")


    #C0038
    ChrTalk(
        0xB,
        (
            "#02105F听说你们已经把\x01",
            "亚里欧斯·马克莱因打败了？\x02\x03",

            "#02106F呼……\x01",
            "真没想到你们\x01",
            "能做得这么出色……\x02\x03",

            "#02109F看来『克洛斯贝尔的英雄』\x01",
            "这个称号也要易主了呢。\x01",
            "哎呀呀～真是个爆炸性的消息！\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x101,
        (
            "#00004F哈哈……太过奖了。\x02\x03",

            "#00000F而且，我认为亚里欧斯先生\x01",
            "依然是克洛斯贝尔的英雄，\x01",
            "这是不会改变的。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0xB,
        (
            "#02104F呵呵……\x01",
            "罗伊德，你真是成长了不少呢。\x02\x03",

            "#02102F你们已经超越了亚里欧斯先生，\x01",
            "接下来，无论再面对什么难关，\x01",
            "也一定可以顺利跨越。\x02\x03",

            "#02109F大家继续努力，\x01",
            "共同迎接美好的结局吧！\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x101,
        "#00000F是！！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1DA, 0)
    Return()

    # Function_10_1909 end

    def Function_11_1AFB(): pass

    label("Function_11_1AFB")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearParty()
    AddParty(0x0, 0xFF, 0xFF)
    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x2, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    AddParty(0x4, 0xFF, 0xFF)
    AddParty(0x8, 0xFF, 0xFF)
    AddParty(0x5, 0xFF, 0xFF)
    OP_32(0xFF, 0xFE, 0x0)
    PartySelect(1)
    RemoveParty(0x4, 0xFF)
    RemoveParty(0x8, 0xFF)
    RemoveParty(0x5, 0xFF)
    SetChrFlags(0xB, 0x80)
    PlayBGM("ed7534", 0)
    SetChrPos(0x101, 0, 0, -2000, 180)
    SetChrPos(0x102, 1050, 0, -2950, 270)
    SetChrPos(0x103, -950, 0, -3250, 90)
    SetChrPos(0x104, 0, 0, -4250, 0)
    OP_68(1840, 1100, 14830, 0)
    MoveCamera(51, 25, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(27300, 0)
    OP_68(0, 1100, -3000, 7000)
    MoveCamera(51, 25, 0, 7000)
    OP_6E(800, 7000)
    SetCameraDistance(18480, 7000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    Fade(500)
    OP_68(0, 1100, -3000, 0)
    MoveCamera(51, 25, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(10200, 0)
    OP_0D()
    Sleep(300)

    #C0042
    ChrTalk(
        0x104,
        (
            "#00306F#12P回想一下，总觉得我们\x01",
            "已经走了很远的路。\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x103,
        (
            "#00208F#6P是啊……\x01",
            "但其实仍然没有离开\x01",
            "这小小的克洛斯贝尔。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x102,
        (
            "#00103F#11P……不仅是我们，\x01",
            "整个克洛斯贝尔……不，整个大陆\x01",
            "恐怕都开始风起云涌了。\x02\x03",

            "#00108F说不定，我们正在见证\x01",
            "历史的转折点……\x02\x03",

            "…………………………………\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x101,
        (
            "#00003F#5P……艾莉。\x02\x03",

            "#00008F与玛丽亚贝尔小姐他们为敌\x01",
            "始终让你有些抵触吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x102,
        (
            "#00106F#11P是啊……对我来说，\x01",
            "他们都是非常亲密的人。\x02\x03",

            "#00108F而且，就政治观点来说，\x01",
            "我也无法完全否定\x01",
            "他们的做法……\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x103,
        "#00208F#6P………………………………\x02",
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x101,
        "#00006F#5P……是吗……\x02",
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x104,
        (
            "#00306F#12P嗯，铁血宰相自不必说，\x01",
            "手段比他们更加肮脏的家伙\x01",
            "数不胜数……\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x102,
        (
            "#00103F#11P总之，唯有一点我可以确定──\x02\x03",

            "#00101F无论情况发生怎样的变化，\x01",
            "我们也都是『特别任务支援科』。\x02\x03",

            "这一点是永远都\x01",
            "不会动摇的。\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x101,
        "#00005F#5P艾莉……\x02",
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x103,
        "#00202F#6P……艾莉前辈……\x02",
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x104,
        (
            "#00309F#12P哈哈，什么啊，大小姐。\x02\x03",

            "#00302F对你来说，警察工作原本\x01",
            "不应该只是一块跳板吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x102,
        (
            "#00109F#11P呵呵，最初确实是这样想的。\x02\x03",

            "#00104F……但还是不行啊，\x01",
            "我已经被某些人感染了。\x02\x03",

            "不管将来会选择\x01",
            "什么样的道路……\x02\x03",

            "#00102F我也一定会把\x01",
            "与你们共度的这段\x01",
            "时光永存心底的。\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x101,
        "#00000F#5P……是吗。\x02",
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x103,
        "#00204F#6P我也是这样想的……\x02",
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x104,
        (
            "#00304F#12P哈哈，说起来，\x01",
            "科长真是成立了一个\x01",
            "糟糕的部门啊。\x02\x03",

            "#00305F不对，这好像是\x01",
            "罗伊德的大哥的主意吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x101,
        (
            "#00012F#5P哈哈，但大哥\x01",
            "应该也没有料想到\x01",
            "情况会变成现在这样。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    #C0059
    ChrTalk(
        0x101,
        (
            "#00001F#5P……夺回琪雅，\x01",
            "解决此次事件。\x02\x03",

            "这也许就是我们特别任务支援科\x01",
            "必须要履行的使命。\x02\x03",

            "#00004F不过，也没必要勉强去思考\x01",
            "这些大道理。\x02\x03",

            "为了我们珍视的\x01",
            "一切……\x02\x03",

            "#00000F现在就一心向前吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x102,
        "#00102F#11P嗯……！\x02",
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x103,
        (
            "#00204F#6P另外，我们还要把\x01",
            "音讯全无的科长找到。\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x104,
        "#00309F#12P哈哈……是啊。\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(9200, 3000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopSound(132, 1000, 70)
    StopSound(497, 1000, 30)
    StopBGM(0xFA0)
    WaitBGM()
    Sound(814, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0063
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "艾莉加入了队伍。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(500)
    Sound(517, 0, 100, 0)
    AddCraft(0x1, 0x11F)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0064
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "艾莉习得Ｓ战技\x01\x07\x02",

            "『神圣十字波』\x07\x05",
            "。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, 52, -1, -1)

    #A0065
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "『神圣十字波』\x07\x05",
            "设置为Ｓ爆发技吗？",
            scpstr(0x6),
            scpstr(0x18),
            scpstr(SCPSTR_CODE_ENTER),
        )
    )

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        1,
        -1,
        208,
        0,
        (
            "【是】\x01",      # 0
            "【否】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_57(0x0)
    OP_60(0x1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_23A1")
    SetChrChipPat(0x1, 0x6, 0x11F)

    label("loc_23A1")

    OP_5A()
    SetChrName("")

    #A0066
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "艾莉加入之后，\x01",
            "队伍人数已超过六人限制。\x02\x03",

            "请从以下成员中\x01",
            "选择编入队伍的\x01",
            "成员。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    PartySelect(0)
    PartySelect(2)
    Sleep(500)
    SetChrName("")

    #A0067
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "今后只要与飞艇内的\x01",
            "阿巴斯对话，\x01",
            "即可编组队伍。\x02\x03",

            "另外，想发展剧情时，\x01",
            "请选择位于梅尔卡瓦移动地图东侧的\x01",
            "『无线信号增幅器地点』。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    ClearParty()
    AddParty(0x0, 0xFF, 0xFF)
    SetScenarioFlags(0x1A4, 1)
    OP_29(0xAF, 0x1, 0x14)
    SetScenarioFlags(0x31, 6)
    SetScenarioFlags(0x31, 7)
    EventEnd(0x5)
    NewScene("e3020", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_11_1AFB end

    SaveToFile()

Try(main)
