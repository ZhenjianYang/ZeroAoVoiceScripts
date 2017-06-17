from ScenarioHelper import *

def main():
    CreateScenaFile(
        "t2100.bin",                # FileName
        "t2100",                    # MapName
        "t2100",                    # Location
        0x0059,                     # MapIndex
        "ed7126",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x1C,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 89, 0, 1, 0, 2],
    )

    BuildStringList((
        "t2100",                  # 0
        "布鲁德队员",             # 1
        "达利亚队员",             # 2
        "琪露露",                 # 3
        "帝国军战车",             # 4
        "帝国军战车",             # 5
        "帝国军战车",             # 6
        "帝国军战车",             # 7
        "帝国军战车",             # 8
        "SE控制",                 # 9
    ))

    AddCharChip((
        "chr/ch31200.itc",                   # 00
        "chr/ch34100.itc",                   # 01
        "chr/ch20500.itc",                   # 02
    ))

    DeclNpc(-13829,  10000,   -2960,   270,  261,  0x0, 0,   0,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(-14060,  10000,   2900,    270,  261,  0x0, 0,   1,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(-18600,  5000,    -17350,  270,  389,  0x0, 0,   2,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclActor(1500,    5050,    -20000,  1200,    1500,    6050,    -20000,  0x007C, 0,  3,  0x0000)

    ChipFrameInfo(516, 0)                                        # 0

    ScpFunction((
        "Function_0_204",          # 00, 0
        "Function_1_2B4",          # 01, 1
        "Function_2_33D",          # 02, 2
        "Function_3_47A",          # 03, 3
        "Function_4_5B5",          # 04, 4
        "Function_5_C89",          # 05, 5
        "Function_6_1692",         # 06, 6
        "Function_7_16E6",         # 07, 7
        "Function_8_1AB7",         # 08, 8
        "Function_9_1AC7",         # 09, 9
        "Function_10_1AD7",        # 0A, 10
        "Function_11_1AF4",        # 0B, 11
        "Function_12_1B14",        # 0C, 12
        "Function_13_1B34",        # 0D, 13
        "Function_14_1B54",        # 0E, 14
        "Function_15_1B74",        # 0F, 15
        "Function_16_1BBF",        # 10, 16
    ))


    def Function_0_204(): pass

    label("Function_0_204")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_23C"),
        (1, "loc_248"),
        (2, "loc_254"),
        (3, "loc_260"),
        (4, "loc_26C"),
        (5, "loc_278"),
        (6, "loc_284"),
        (SWITCH_DEFAULT, "loc_290"),
    )


    label("loc_23C")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_29C")

    label("loc_248")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_29C")

    label("loc_254")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_29C")

    label("loc_260")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_29C")

    label("loc_26C")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_29C")

    label("loc_278")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_29C")

    label("loc_284")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_29C")

    label("loc_290")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_29C")

    label("loc_29C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2B3")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_29C")

    label("loc_2B3")

    Return()

    # Function_0_204 end

    def Function_1_2B4(): pass

    label("Function_1_2B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2C2")
    Jump("loc_316")

    label("loc_2C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2D0")
    Jump("loc_316")

    label("loc_2D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2DE")
    Jump("loc_316")

    label("loc_2DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2EC")
    Jump("loc_316")

    label("loc_2EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2FA")
    Jump("loc_316")

    label("loc_2FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_308")
    Jump("loc_316")

    label("loc_308")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_316")
    ClearChrFlags(0xA, 0x80)

    label("loc_316")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_32D")
    ClearScenarioFlags(0x22, 0)
    SetScenarioFlags(0x0, 0)
    Event(0, 7)
    Jump("loc_33C")

    label("loc_32D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_33C")
    ClearScenarioFlags(0x22, 1)
    Event(0, 16)

    label("loc_33C")

    Return()

    # Function_1_2B4 end

    def Function_2_33D(): pass

    label("Function_2_33D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_357")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 0)
    Jump("loc_385")

    label("loc_357")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_373")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x97), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_385")

    label("loc_373")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 3)), scpexpr(EXPR_END)), "loc_385")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x236), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_385")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_409")
    LoadEffect(0x9, "map/mprain00.eff")
    PlayEffect(0x9, 0x7, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 1000)
    OP_7D(0xB4, 0xB4, 0xB4, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0xD, 0xE6, 0x0)
    Sound(128, 1, 100, 0)

    label("loc_409")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_END)), "loc_420")
    OP_7D(0xDC, 0xEB, 0xFF, 0x0, 0x0)
    Jump("loc_420")

    label("loc_420")

    SetMapObjFrame(0xFF, "open", 0x0, 0x1)
    SetMapObjFrame(0xFF, "amor0", 0x0, 0x1)
    SetMapObjFrame(0xFF, "amor0b", 0x0, 0x1)
    SetMapObjFrame(0xFF, "cano0", 0x0, 0x1)
    SetMapObjFrame(0xFF, "kage01", 0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1ED, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_475")
    OP_70(0x2, 0x0)
    Jump("loc_479")

    label("loc_475")

    OP_70(0x2, 0x1E)

    label("loc_479")

    Return()

    # Function_2_33D end

    def Function_3_47A(): pass

    label("Function_3_47A")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1ED, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_56C")
    Sound(14, 0, 100, 0)
    OP_74(0x2, 0x1E)
    OP_71(0x2, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('狙击枪管', 1)"), scpexpr(EXPR_END)), "loc_4FD")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0001
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '狙击枪管'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1ED, 6)
    OP_E0(0x5, 0x0)
    Jump("loc_567")

    label("loc_4FD")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0002
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, '狙击枪管'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多，",
            scpstr(SCPSTR_CODE_ITEM, '狙击枪管'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x2, 0x1E, 0x0, 0x0, 0x0)

    label("loc_567")

    Jump("loc_5A9")

    label("loc_56C")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0003
    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "宝箱里什么都没有。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_5A9")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_47A end

    def Function_4_5B5(): pass

    label("Function_4_5B5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_704")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_68D")

    #C0004
    ChrTalk(
        0xFE,
        (
            "最近流传着这样的传闻，\x01",
            "据说袭击克洛斯贝尔市的\x01",
            "猎兵团是帝国雇佣的……\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0xFE,
        (
            "我无论如何也无法原谅那些\x01",
            "伤害警备队战友们的家伙。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0xFE,
        (
            "既然帝国图谋不轨，\x01",
            "那我们也只能下定决心对抗到底了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_6FF")

    label("loc_68D")


    #C0007
    ChrTalk(
        0xFE,
        (
            "听说帝国军正在\x01",
            "进行大规模的\x01",
            "演习……\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0xFE,
        (
            "……真露骨啊。\x01",
            "既然帝国图谋不轨，\x01",
            "那我们也只能下定决心对抗到底了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6FF")

    Jump("loc_C85")

    label("loc_704")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_771")

    #C0009
    ChrTalk(
        0xFE,
        (
            "虽然只是小雨，\x01",
            "但能见度还是很低。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0xFE,
        (
            "近来似乎又有人\x01",
            "目击到了幻兽……\x01",
            "必须要多加注意啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C85")

    label("loc_771")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_870")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_81B")

    #C0011
    ChrTalk(
        0xFE,
        (
            "哎呀呀，最近实在太忙了，\x01",
            "连休息的时间都没有。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0xFE,
        (
            "……不过，司令和三尉\x01",
            "要比我们更加辛苦。\x01",
            "真敬佩她们的毅力啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0xFE,
        "我也必须要继续努力。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_86B")

    label("loc_81B")


    #C0014
    ChrTalk(
        0xFE,
        (
            "司令和三尉\x01",
            "比我们更加辛苦。\x01",
            "真敬佩她们的毅力啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0xFE,
        "我也必须要继续努力。\x02",
    )

    CloseMessageWindow()

    label("loc_86B")

    Jump("loc_C85")

    label("loc_870")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_976")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_924")

    #C0016
    ChrTalk(
        0xFE,
        (
            "自从市长发表独立提案以来，\x01",
            "帝国和共和国就一直在\x01",
            "露骨地给我们施加压力。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0xFE,
        "老实说，这种紧张状态真是让我连胃都觉得疼。\x02",
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0xFE,
        (
            "真希望能尽早\x01",
            "做个了结。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_971")

    label("loc_924")


    #C0019
    ChrTalk(
        0xFE,
        "老实说，这种紧张状态真是让我连胃都觉得疼。\x02",
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0xFE,
        (
            "真希望能尽早\x01",
            "做个了结。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_971")

    Jump("loc_C85")

    label("loc_976")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_9FA")

    #C0021
    ChrTalk(
        0xFE,
        (
            "根据我们接到的情报，\x01",
            "恐怖分子很可能由帝国\x01",
            "侵入克洛斯贝尔。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0xFE,
        (
            "真是让人紧张啊，\x01",
            "但愿今天什么事情\x01",
            "都不要发生……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C85")

    label("loc_9FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_B8A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B06")

    #C0023
    ChrTalk(
        0xFE,
        (
            "驻守在唐古拉姆门的巴雷尔\x01",
            "是我的朋友……\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0xFE,
        (
            "听说他在魔鬼般严厉的副司令的指导下，\x01",
            "每天都要承受地狱般的磨练。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0xFE,
        (
            "不过，比起上司无能，\x01",
            "能接受严厉的磨练真是奢侈的烦恼啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0xFE,
        (
            "虽然索妮亚司令也非常严厉，\x01",
            "但我从来都不觉得\x01",
            "以前的司令更好。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_B85")

    label("loc_B06")


    #C0027
    ChrTalk(
        0xFE,
        (
            "不过，比起上司无能，\x01",
            "能接受严厉的磨练真是奢侈的烦恼啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0xFE,
        (
            "虽然索妮亚司令也非常严厉，\x01",
            "但我从来都不觉得\x01",
            "以前的司令更好。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B85")

    Jump("loc_C85")

    label("loc_B8A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_C85")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C1A")

    #C0029
    ChrTalk(
        0xFE,
        (
            "自从索妮亚司令赴任以后，\x01",
            "贝尔加德门的警备状态\x01",
            "立刻就有了明显改善。\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0xFE,
        (
            "遇到一位有能力的上司，\x01",
            "真是让人幸福啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_C85")

    label("loc_C1A")


    #C0031
    ChrTalk(
        0xFE,
        (
            "在前司令手下工作的时候，\x01",
            "我从来都没有过\x01",
            "这么充实的感觉。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0xFE,
        (
            "遇到一位有能力的上司，\x01",
            "真是让人幸福啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C85")

    TalkEnd(0xFE)
    Return()

    # Function_4_5B5 end

    def Function_5_C89(): pass

    label("Function_5_C89")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_E43")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D88")

    #C0033
    ChrTalk(
        0xFE,
        (
            "要求独立的呼声持续高涨，\x01",
            "与签署《互不侵犯条约》之前相比，\x01",
            "如今的紧张程度恐怕有过之而无不及。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0xFE,
        (
            "如果与帝国之间的对立关系达到极限，\x01",
            "他们极有可能再次亮出\x01",
            "『列车炮』。\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0xFE,
        (
            "与帝国和共和国的斗争……\x01",
            "终究还是无法回避吗……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_E3E")

    label("loc_D88")


    #C0036
    ChrTalk(
        0xFE,
        (
            "……最近这段时间，索妮亚司令\x01",
            "经常一脸凝重地思考。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0xFE,
        (
            "听说她正在与迪塔市长\x01",
            "和麦克道尔议长他们协商\x01",
            "重新编制警备队的问题……\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0xFE,
        (
            "连同与两大国的对立在内，\x01",
            "问题还真是堆积如山啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E3E")

    Jump("loc_168E")

    label("loc_E43")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_F89")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F02")

    #C0039
    ChrTalk(
        0xFE,
        (
            "昨天的脱轨事故……\x01",
            "真是太惨烈了。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0xFE,
        (
            "如果犯人就是那只\x01",
            "巨大的怪物……\x01",
            "今后恐怕还会引发类似的事故。\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0xFE,
        (
            "如此看来，无论如何也要找到\x01",
            "那只怪物，并把它消灭才行。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_F84")

    label("loc_F02")


    #C0042
    ChrTalk(
        0xFE,
        (
            "考虑到铁路的重要性，目前最关键的任务\x01",
            "就是防止同样的事故再度发生。\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0xFE,
        (
            "如此看来，无论如何也要找到\x01",
            "那只怪物，并把它消灭才行。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F84")

    Jump("loc_168E")

    label("loc_F89")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_11F3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x188, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1052")

    #C0044
    ChrTalk(
        0xFE,
        (
            "布鲁德队员为了让我转换心情，\x01",
            "送给我一本书。\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0xFE,
        (
            "这本书很有意思，\x01",
            "各位要是有兴趣，\x01",
            "也请读读看吧。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0046
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '沐浴阳光的阿尼艾丝８卷'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('沐浴阳光的阿尼艾丝８卷', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x188, 7)
    Jump("loc_11EE")

    label("loc_1052")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_114C")

    #C0047
    ChrTalk(
        0xFE,
        (
            "在位于那座岩壁内部的\x01",
            "『卡雷利亚要塞』中，\x01",
            "配备着各种各样的武器。\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0xFE,
        (
            "我们与帝国之间的紧张关系曾在过去\x01",
            "达到过极限，他们当时举行了大规模\x01",
            "演习，并在演习中开动了『列车炮』。\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0xFE,
        (
            "但愿这次的紧张状态\x01",
            "不要导致当时那种场面\x01",
            "再度出现。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_11EE")

    label("loc_114C")


    #C0050
    ChrTalk(
        0xFE,
        (
            "我们与帝国之间的紧张关系曾在过去\x01",
            "达到过极限，他们当时举行了大规模\x01",
            "演习，并在演习中开动了『列车炮』。\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0xFE,
        (
            "但愿这次的紧张状态\x01",
            "不要导致当时那种场面\x01",
            "再度出现。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11EE")

    Jump("loc_168E")

    label("loc_11F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_12F8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1299")

    #C0052
    ChrTalk(
        0xFE,
        (
            "市长的独立提案\x01",
            "让我大为震惊，\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0xFE,
        (
            "但是……为了保证今后\x01",
            "能够继续守护克洛斯贝尔，\x01",
            "独立也许真的是必要之举。\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0xFE,
        "要是能顺利实现就好了。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_12F3")

    label("loc_1299")


    #C0055
    ChrTalk(
        0xFE,
        (
            "市长的独立提案\x01",
            "让我大为震惊，\x01",
            "但独立也许真的是必要之举。\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0xFE,
        "要是能顺利实现就好了。\x02",
    )

    CloseMessageWindow()

    label("loc_12F3")

    Jump("loc_168E")

    label("loc_12F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_14AD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1423")

    #C0057
    ChrTalk(
        0xFE,
        (
            "接到有关恐怖分子的情报之后，\x01",
            "我们一直在尽最大努力\x01",
            "来执行边境一带的警备工作。\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0xFE,
        (
            "为了防备由空中侵入的入侵者，\x01",
            "我们已经开始使用设置在\x01",
            "这附近的特别设施了。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0xFE,
        (
            "如果再配备上军队专用的高射炮，\x01",
            "应该就可以保证万无一失了……\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0xFE,
        (
            "……但根本没有的东西，\x01",
            "再怎么想也没用啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_14A8")

    label("loc_1423")


    #C0061
    ChrTalk(
        0xFE,
        (
            "如果能配备上军队专用的高射炮，\x01",
            "我们就可以万无一失地防备\x01",
            "由空中侵入的入侵者了……\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0xFE,
        (
            "……但根本没有的东西，\x01",
            "再怎么想也没用啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14A8")

    Jump("loc_168E")

    label("loc_14AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_15F3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_157E")

    #C0063
    ChrTalk(
        0xFE,
        (
            "今天早上，我看到一辆火红色的\x01",
            "导力列车从边境大门下方通过。\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0xFE,
        (
            "那是帝国政府的专用列车……\x01",
            "『铁血宰相』和奥利维特皇子\x01",
            "应该就坐在里面。\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0xFE,
        (
            "这让人深切感觉到\x01",
            "通商会议终于开始了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_15EE")

    label("loc_157E")


    #C0066
    ChrTalk(
        0xFE,
        (
            "今天早上，我看到一辆火红色的\x01",
            "导力列车从边境大门下方通过。\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0xFE,
        (
            "这让人深深的感觉到……\x01",
            "通商会议终于开始了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15EE")

    Jump("loc_168E")

    label("loc_15F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_168E")

    #C0068
    ChrTalk(
        0xFE,
        (
            "通商会议已经渐渐临近，\x01",
            "我们警备队担负的责任\x01",
            "比平时更加重大。\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0xFE,
        (
            "为了保护好来访克洛斯贝尔\x01",
            "的各国首脑……\x01",
            "必须要严格做好边境大门的警备工作。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_168E")

    TalkEnd(0xFE)
    Return()

    # Function_5_C89 end

    def Function_6_1692(): pass

    label("Function_6_1692")

    TalkBegin(0xFE)

    #C0070
    ChrTalk(
        0xFE,
        "这山谷真是壮观啊……\x02",
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0xFE,
        (
            "要是失足掉下去，肯定会丢掉小命呢。\x01",
            "真刺激……\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_6_1692 end

    def Function_7_16E6(): pass

    label("Function_7_16E6")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_C9(0x0, 0x10)
    FadeToBright(0, 0)
    OP_0D()
    PlayMovie(0x0, "ed72_04a.pmf", 0x22C, 0x1)
    Sleep(1000)
    OP_57(0x2)
    PlayMovie(0x1, "", 0x0, 0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    OP_C9(0x1, 0x10)
    OP_F3(200000)
    LoadEffect(0x0, "event/ev15060.eff")
    SoundLoad(825)
    SoundLoad(923)
    OP_68(-66820, 1000, -14120, 0)
    MoveCamera(307, 12, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(75270, 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x22C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapObjFrame(0xFF, "close", 0x0, 0x1)
    SetMapObjFrame(0xFF, "open", 0x1, 0x1)
    SetMapObjFrame(0xFF, "amor0", 0x1, 0x1)
    SetMapObjFrame(0xFF, "amor0b", 0x1, 0x1)
    SetMapObjFrame(0xFF, "cano0", 0x1, 0x1)
    SetMapObjFrame(0xFF, "kage01", 0x1, 0x1)
    OP_68(-69430, 11500, -13600, 0)
    MoveCamera(297, 8, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(65000, 0)
    SetCameraDistance(71000, 5500)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, -122940, 200, -1170, 0)
    SetMapObjFlags(0x5, 0x1000)
    ClearMapObjFlags(0x5, 0x4)
    OP_78(0x5, 0xB)
    OP_93(0xB, 0x5A, 0x0)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, -139790, 200, -2770, 0)
    SetMapObjFlags(0x4, 0x1000)
    ClearMapObjFlags(0x4, 0x4)
    OP_78(0x4, 0xC)
    OP_93(0xC, 0x5A, 0x0)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, -156790, 200, 2770, 0)
    SetMapObjFlags(0x3, 0x1000)
    ClearMapObjFlags(0x3, 0x4)
    OP_78(0x3, 0xD)
    OP_93(0xD, 0x5A, 0x0)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, -177000, 200, 1140, 0)
    SetMapObjFlags(0x6, 0x1000)
    ClearMapObjFlags(0x6, 0x4)
    OP_78(0x6, 0xE)
    OP_93(0xE, 0x5A, 0x0)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, -198000, 200, -1150, 0)
    SetMapObjFlags(0x7, 0x1000)
    ClearMapObjFlags(0x7, 0x4)
    OP_78(0x7, 0xF)
    OP_93(0xF, 0x5A, 0x0)
    OP_75(0x6, 0x1, 0x0)
    OP_75(0x7, 0x1, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    PlaceName2(340, 200, "c_plac66", 0x0, 0)
    OP_6F(0x79)
    BeginChrThread(0xB, 0, 0, 10)
    BeginChrThread(0xC, 0, 0, 11)
    BeginChrThread(0xD, 0, 0, 12)
    BeginChrThread(0xE, 0, 0, 13)
    BeginChrThread(0xF, 0, 0, 14)
    BeginChrThread(0x10, 1, 0, 15)
    OP_68(-91380, 15200, 2180, 0)
    MoveCamera(331, 11, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(83380, 0)
    Fade(500)
    OP_0D()
    OP_68(-90600, 7400, 2210, 7500)
    MoveCamera(331, 5, 0, 7500)
    OP_6E(450, 7500)
    SetCameraDistance(77550, 7200)
    OP_6F(0x79)
    SetCameraDistance(40000, 5000)
    OP_68(-85000, 4700, 1860, 8200)
    Sleep(4500)
    MoveCamera(317, -1, 0, 3500)
    OP_6F(0x79)
    OP_68(-32549, 4800, -7710, 18500)
    SetCameraDistance(42000, 4000)
    Sleep(6000)
    EndChrThread(0xB, 0x1)
    EndChrThread(0xC, 0x1)
    EndChrThread(0xD, 0x1)
    EndChrThread(0xE, 0x1)
    EndChrThread(0xF, 0x1)
    OP_68(-54250, 2570, -1160, 0)
    MoveCamera(270, 10, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(14060, 0)
    Fade(500)
    BeginChrThread(0xB, 1, 0, 9)
    BeginChrThread(0xC, 1, 0, 9)
    BeginChrThread(0xD, 1, 0, 9)
    BeginChrThread(0xE, 1, 0, 9)
    BeginChrThread(0xF, 1, 0, 9)
    OP_68(-43550, 2570, -690, 8000)
    MoveCamera(266, 7, 0, 8000)
    OP_6E(450, 8000)
    SetCameraDistance(17940, 8000)
    Sleep(1500)
    OP_75(0x6, 0x2, 0x2BC)
    Sleep(3500)
    OP_75(0x7, 0x2, 0x2BC)
    Sleep(2000)
    StopSound(923, 1000, 60)
    StopSound(825, 1000, 80)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 0)
    NewScene("e4101", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_7_16E6 end

    def Function_8_1AB7(): pass

    label("Function_8_1AB7")

    OP_9B(0x1, 0xFE, 0x0, 0x1D4C0, 0xBB8, 0x0)
    Return()

    # Function_8_1AB7 end

    def Function_9_1AC7(): pass

    label("Function_9_1AC7")

    OP_9B(0x1, 0xFE, 0x0, 0x1D4C0, 0x7D0, 0x0)
    Return()

    # Function_9_1AC7 end

    def Function_10_1AD7(): pass

    label("Function_10_1AD7")

    Sleep(1500)
    BeginChrThread(0xFE, 1, 0, 8)

    label("loc_1AE0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1AF3")
    Sleep(5000)
    Jump("loc_1AE0")

    label("loc_1AF3")

    Return()

    # Function_10_1AD7 end

    def Function_11_1AF4(): pass

    label("Function_11_1AF4")

    Sleep(1500)
    BeginChrThread(0xFE, 1, 0, 8)
    Sleep(1200)

    label("loc_1B00")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1B13")
    Sleep(5000)
    Jump("loc_1B00")

    label("loc_1B13")

    Return()

    # Function_11_1AF4 end

    def Function_12_1B14(): pass

    label("Function_12_1B14")

    Sleep(1500)
    BeginChrThread(0xFE, 1, 0, 8)
    Sleep(2400)

    label("loc_1B20")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1B33")
    Sleep(5000)
    Jump("loc_1B20")

    label("loc_1B33")

    Return()

    # Function_12_1B14 end

    def Function_13_1B34(): pass

    label("Function_13_1B34")

    Sleep(1500)
    BeginChrThread(0xFE, 1, 0, 8)
    Sleep(3600)

    label("loc_1B40")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1B53")
    Sleep(5000)
    Jump("loc_1B40")

    label("loc_1B53")

    Return()

    # Function_13_1B34 end

    def Function_14_1B54(): pass

    label("Function_14_1B54")

    Sleep(1500)
    BeginChrThread(0xFE, 1, 0, 8)
    Sleep(4800)

    label("loc_1B60")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1B73")
    Sleep(5000)
    Jump("loc_1B60")

    label("loc_1B73")

    Return()

    # Function_14_1B54 end

    def Function_15_1B74(): pass

    label("Function_15_1B74")

    Sound(923, 2, 10, 0)
    Sound(825, 2, 20, 0)
    Sleep(1500)
    OP_25(0x39B, 0x14)
    OP_25(0x339, 0x1E)
    Sleep(1000)
    OP_25(0x39B, 0x1E)
    OP_25(0x339, 0x28)
    Sleep(1000)
    OP_25(0x39B, 0x28)
    OP_25(0x339, 0x32)
    Sleep(500)
    OP_25(0x39B, 0x32)
    OP_25(0x339, 0x3C)
    Sleep(500)
    OP_25(0x39B, 0x3C)
    OP_25(0x339, 0x46)
    Sleep(500)
    OP_25(0x339, 0x50)
    Return()

    # Function_15_1B74 end

    def Function_16_1BBF(): pass

    label("Function_16_1BBF")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetMapObjFrame(0xFF, "close", 0x0, 0x1)
    SetMapObjFrame(0xFF, "open", 0x1, 0x1)
    SetMapObjFrame(0xFF, "amor0", 0x1, 0x1)
    SetMapObjFrame(0xFF, "amor0b", 0x1, 0x1)
    SetMapObjFrame(0xFF, "cano0", 0x1, 0x1)
    SetMapObjFrame(0xFF, "kage01", 0x1, 0x1)
    OP_68(-100000, 0, 0, 0)
    MoveCamera(300, 15, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(80000, 0)
    FadeToBright(1000, 0)
    OP_68(-100000, 10000, 0, 7000)
    Sleep(5000)
    OP_0D()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 0)
    NewScene("e4000", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_16_1BBF end

    SaveToFile()

Try(main)
