from ScenarioHelper import *

def main():
    CreateScenaFile(
        "t2520.bin",                # FileName
        "t2520",                    # MapName
        "t2520",                    # Location
        0x005A,                     # MapIndex
        "ed7126",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x1B,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 90, 0, 3, 0, 4],
    )

    BuildStringList((
        "t2520",                  # 0
        "弗拉米队员",             # 1
        "道格拉斯副司令",         # 2
    ))

    AddCharChip((
        "chr/ch34100.itc",                   # 00
        "chr/ch44902.itc",                   # 01
        "chr/ch41800.itc",                   # 02
    ))

    DeclNpc(-32750,  9,       40700,   0,    261,  0x0, 0,   0,   0,   0,   1,   0,   6,   255,  0)
    DeclNpc(6210,    150,     -150,    270,  325,  0x0, 0,   1,   0,   255, 255, 0,   9,   255,  0)

    DeclActor(4760,    0,       -280,    1200,    6210,    1500,    -150,    0x007E, 0,  8,  0x0000)
    DeclActor(-83680,  0,       22050,   1200,    -83680,  1200,    22050,   0x007C, 0,  5,  0x0000)

    ChipFrameInfo(384, 0)                                        # 0

    ScpFunction((
        "Function_0_180",          # 00, 0
        "Function_1_238",          # 01, 1
        "Function_2_263",          # 02, 2
        "Function_3_2C4",          # 03, 3
        "Function_4_40A",          # 04, 4
        "Function_5_532",          # 05, 5
        "Function_6_5DB",          # 06, 6
        "Function_7_1153",         # 07, 7
        "Function_8_127A",         # 08, 8
        "Function_9_12CC",         # 09, 9
        "Function_10_2E71",        # 0A, 10
        "Function_11_3827",        # 0B, 11
        "Function_12_393B",        # 0C, 12
        "Function_13_396B",        # 0D, 13
        "Function_14_39C3",        # 0E, 14
        "Function_15_3A1B",        # 0F, 15
        "Function_16_3A66",        # 10, 16
        "Function_17_3AB1",        # 11, 17
        "Function_18_3BB5",        # 12, 18
        "Function_19_3D49",        # 13, 19
        "Function_20_4B93",        # 14, 20
        "Function_21_5218",        # 15, 21
        "Function_22_5333",        # 16, 22
        "Function_23_5B0B",        # 17, 23
    ))


    def Function_0_180(): pass

    label("Function_0_180")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_1C0"),
        (1, "loc_1CC"),
        (2, "loc_1D8"),
        (3, "loc_1E4"),
        (4, "loc_1F0"),
        (5, "loc_1FC"),
        (6, "loc_208"),
        (SWITCH_DEFAULT, "loc_214"),
    )


    label("loc_1C0")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_220")

    label("loc_1CC")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_220")

    label("loc_1D8")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_220")

    label("loc_1E4")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_220")

    label("loc_1F0")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_220")

    label("loc_1FC")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_220")

    label("loc_208")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_220")

    label("loc_214")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_220")

    label("loc_220")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_237")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_220")

    label("loc_237")

    Return()

    # Function_0_180 end

    def Function_1_238(): pass

    label("Function_1_238")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_262")
    OP_94(0xFE, 0xFFFF86E8, 0xA5A0, 0xFFFF793C, 0x9858, 0x3E8)
    Sleep(300)
    Jump("Function_1_238")

    label("loc_262")

    Return()

    # Function_1_238 end

    def Function_2_263(): pass

    label("Function_2_263")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2C3")
    OP_95(0xFE, -33890, 0, 4560, 2000, 0x0)
    OP_95(0xFE, -33890, 0, -11290, 2000, 0x0)
    OP_95(0xFE, -33890, 0, 4560, 2000, 0x0)
    OP_95(0xFE, -53890, 0, 4560, 2000, 0x0)
    Jump("Function_2_263")

    label("loc_2C3")

    Return()

    # Function_2_263 end

    def Function_3_2C4(): pass

    label("Function_3_2C4")

    SetChrChipByIndex(0x9, 0x1)
    SetChrSubChip(0x9, 0x0)
    EndChrThread(0x9, 0x0)
    SetChrBattleFlags(0x9, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_303")
    SetChrChipByIndex(0x8, 0x2)
    SetChrFlags(0x9, 0x80)
    SetChrPos(0x8, -40000, 0, 4560, 90)
    BeginChrThread(0x8, 0, 0, 2)
    Jump("loc_3B9")

    label("loc_303")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_311")
    Jump("loc_3B9")

    label("loc_311")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_31F")
    Jump("loc_3B9")

    label("loc_31F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_32D")
    Jump("loc_3B9")

    label("loc_32D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_366")
    SetChrPos(0x8, 3900, 0, -150, 90)
    BeginChrThread(0x8, 0, 0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_361")
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0x9, 0x10)

    label("loc_361")

    Jump("loc_3B9")

    label("loc_366")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_390")
    SetChrPos(0x8, 740, 0, 4470, 0)
    BeginChrThread(0x8, 0, 0, 0)
    SetChrFlags(0x9, 0x80)
    Jump("loc_3B9")

    label("loc_390")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_39E")
    Jump("loc_3B9")

    label("loc_39E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3B9")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6F, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B9")
    SetChrFlags(0x9, 0x80)

    label("loc_3B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_3CD")
    ClearScenarioFlags(0x22, 0)
    Event(0, 19)
    Jump("loc_3DC")

    label("loc_3CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_3DC")
    ClearScenarioFlags(0x22, 1)
    Event(0, 23)

    label("loc_3DC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6A), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6F, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6F, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x152, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_409")
    Event(0, 10)

    label("loc_409")

    Return()

    # Function_3_2C4 end

    def Function_4_40A(): pass

    label("Function_4_40A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_426")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x97), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_438")

    label("loc_426")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 3)), scpexpr(EXPR_END)), "loc_438")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x236), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_438")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_44A")
    OP_65(0x0, 0x1)
    Jump("loc_4C0")

    label("loc_44A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_458")
    Jump("loc_4C0")

    label("loc_458")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_466")
    Jump("loc_4C0")

    label("loc_466")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_474")
    Jump("loc_4C0")

    label("loc_474")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_486")
    OP_65(0x0, 0x1)
    Jump("loc_4C0")

    label("loc_486")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_498")
    OP_65(0x0, 0x1)
    Jump("loc_4C0")

    label("loc_498")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_4A6")
    Jump("loc_4C0")

    label("loc_4A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_4C0")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6F, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4C0")
    OP_65(0x0, 0x1)

    label("loc_4C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4E6")
    SetMapObjFrame(0xFF, "hikari_add", 0x0, 0x1)
    Sound(128, 1, 50, 0)

    label("loc_4E6")

    SetMapObjFrame(0xFF, "bear", 0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_519")
    SetMapObjFrame(0xFF, "cgf2", 0x1, 0x1)
    SetMapObjFrame(0xFF, "cda2", 0x0, 0x1)
    Jump("loc_531")

    label("loc_519")

    SetMapObjFrame(0xFF, "cgf2", 0x0, 0x1)
    SetMapObjFrame(0xFF, "cda2", 0x1, 0x1)

    label("loc_531")

    Return()

    # Function_4_40A end

    def Function_5_532(): pass

    label("Function_5_532")

    SetChrName("")

    #A0001
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "摆放着《美味锅类料理　砂锅篇》。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x2, 0x0)"), scpexpr(EXPR_END)), "loc_5D7")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B2(0x7)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5D7")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0002
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "『芳醇潮锅』\x07\x00",
            "的做法已经学会了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_5D7")

    TalkEnd(0xFF)
    Return()

    # Function_5_532 end

    def Function_6_5DB(): pass

    label("Function_6_5DB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_7BA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_71B")

    #N0003
    NpcTalk(
        0x8,
        "士兵弗拉米",
        (
            "道格拉斯副司令\x01",
            "正在克洛斯贝尔市\x01",
            "研究今后的应对方式。\x02",
        )
    )

    CloseMessageWindow()

    #N0004
    NpcTalk(
        0x8,
        "士兵弗拉米",
        (
            "那棵蓝白色的大树，以及随时\x01",
            "可能发起侵略的帝国和共和国……\x01",
            "还有一大堆问题等着解决呢。\x02",
        )
    )

    CloseMessageWindow()

    #N0005
    NpcTalk(
        0x8,
        "士兵弗拉米",
        (
            "身为国防军士兵，我也不知道\x01",
            "自己能做多少事情……\x02",
        )
    )

    CloseMessageWindow()

    #N0006
    NpcTalk(
        0x8,
        "士兵弗拉米",
        (
            "但我一定不放弃希望，\x01",
            "会坚持努力到最后。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_7B5")

    label("loc_71B")


    #N0007
    NpcTalk(
        0x8,
        "士兵弗拉米",
        (
            "道格拉斯副司令\x01",
            "正在克洛斯贝尔市\x01",
            "研究今后的应对方式。\x02",
        )
    )

    CloseMessageWindow()

    #N0008
    NpcTalk(
        0x8,
        "士兵弗拉米",
        (
            "身为国防军士兵，我也不知道\x01",
            "自己能做多少事情……\x01",
            "但我还是想继续努力。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7B5")

    Jump("loc_114F")

    label("loc_7BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_96B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8EA")

    #C0009
    ChrTalk(
        0x8,
        (
            "诺艾尔上士……\x01",
            "你妹妹能获救，\x01",
            "真是太好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x109,
        (
            "#10108F嗯……但看到警备队的损伤如此惨重，\x01",
            "我实在是开心不起来。\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x8,
        (
            "……嗯，其实我们\x01",
            "也在强忍悲伤……\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x8,
        (
            "但正是因为身处这种状况，\x01",
            "诺艾尔上士的妹妹能够获救，\x01",
            "才更是个令人鼓舞的喜讯。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x109,
        (
            "#10103F……让你挂心了，\x01",
            "十分感谢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_966")

    label("loc_8EA")


    #C0014
    ChrTalk(
        0x8,
        (
            "正因为身处这种状况，\x01",
            "我们才更要忍住悲伤，\x01",
            "继续努力。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x8,
        (
            "警备队的使命就是\x01",
            "为了保卫克洛斯贝尔\x01",
            "而燃尽性命，奉献一生……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_966")

    Jump("loc_114F")

    label("loc_96B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_AA1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A28")

    #C0016
    ChrTalk(
        0x8,
        "说起昨天那起列车脱轨事故……\x02",
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x8,
        (
            "考虑到如今正是临近\x01",
            "居民投票日的关键时期，\x01",
            "说不定会是两大国……\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x8,
        (
            "……我也知道不该\x01",
            "妄下定论，\x01",
            "但实在是无法抑制这种猜测。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_A9C")

    label("loc_A28")


    #C0019
    ChrTalk(
        0x8,
        (
            "昨天那起列车脱轨事故\x01",
            "多半是两大国之一所为吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x8,
        (
            "来自两大国的压力逐日增强，\x01",
            "实在是让人无法抑制这样的猜测。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A9C")

    Jump("loc_114F")

    label("loc_AA1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_C3F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B9E")

    #C0021
    ChrTalk(
        0x8,
        (
            "虽说居民投票的结果\x01",
            "并不能决定克洛斯贝尔\x01",
            "是否会走上独立之路……\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x8,
        (
            "但从帝国和共和国那与日俱增的压力来看，\x01",
            "不难发现，居民投票的影响力\x01",
            "对两大国来说也是一种威胁。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x8,
        (
            "居民投票对\x01",
            "周边诸国的影响之大，\x01",
            "似乎超出我们的想象呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_C3A")

    label("loc_B9E")


    #C0024
    ChrTalk(
        0x8,
        (
            "从帝国和共和国那与日俱增的压力来看，\x01",
            "不难发现，居民投票的影响力\x01",
            "对两大国来说也是一种威胁。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x8,
        (
            "居民投票对\x01",
            "周边诸国的影响之大，\x01",
            "似乎超出我们的想象呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C3A")

    Jump("loc_114F")

    label("loc_C3F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_C98")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C5A")
    Call(0, 7)
    Jump("loc_C93")

    label("loc_C5A")


    #C0026
    ChrTalk(
        0x8,
        (
            "共和国施加的压力\x01",
            "与日俱增。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x8,
        "果然不容松懈啊……\x02",
    )

    CloseMessageWindow()

    label("loc_C93")

    Jump("loc_114F")

    label("loc_C98")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_DC8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D3F")

    #C0028
    ChrTalk(
        0x8,
        (
            "道格拉斯副司令为了商讨\x01",
            "对抗恐怖分子的方案，\x01",
            "已经前往贝尔加德门了。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x8,
        (
            "在正式会议开始之前，\x01",
            "真希望能建立起一套\x01",
            "周全完善的警备体制啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_DC3")

    label("loc_D3F")


    #C0030
    ChrTalk(
        0x8,
        (
            "道格拉斯副司令为了商讨\x01",
            "对抗恐怖分子的方案，\x01",
            "已经前往贝尔加德门了。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x8,
        (
            "他和索妮亚司令一定能\x01",
            "建立起一套周全完善的\x01",
            "警备体制吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DC3")

    Jump("loc_114F")

    label("loc_DC8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_102C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F98")

    #C0032
    ChrTalk(
        0x8,
        (
            "索妮亚司令的调动与\x01",
            "诺艾尔上士的外派\x01",
            "几乎发生在同一时间。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x8,
        (
            "让贝尔加德门的\x01",
            "女性比例瞬间下降了……\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x109,
        (
            "#10106F唔……虽说这是无可奈何的事，\x01",
            "但还真是抱歉啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x8,
        (
            "呜呜，晚上陪我聊八卦的对象\x01",
            "都减少了，真是寂寞啊～\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x101,
        (
            "#00005F请问……\x01",
            "这个不能\x01",
            "和男队员聊吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x105,
        (
            "#10304F呵呵，你真是不明白啊。\x02\x03",

            "#10309F女孩子聊八卦的时侯，\x01",
            "如果有男性在场，\x01",
            "一般就会聊不下去了。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x101,
        (
            "#00006F（虽然搀杂着一些偏见……\x01",
            "  但却能隐隐感觉到其中的恐怖啊。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1027")

    label("loc_F98")


    #C0039
    ChrTalk(
        0x8,
        (
            "诺艾尔上士……请您早点\x01",
            "回警备队吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x8,
        (
            "我会收集很多有趣的八卦，\x01",
            "等您回来以后一起聊的！\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x109,
        "#10106F（回、回来之后，恐怕要说很久了……）\x02",
    )

    CloseMessageWindow()

    label("loc_1027")

    Jump("loc_114F")

    label("loc_102C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_114F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10F0")

    #C0042
    ChrTalk(
        0x8,
        (
            "道格拉斯副司令曾被降职，\x01",
            "在警察学校工作了\x01",
            "很长一段时间……\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x8,
        (
            "但在不久之前，\x01",
            "他在索妮亚司令的要求下，\x01",
            "重新返回警备队工作了。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x8,
        (
            "我们都为副司令的\x01",
            "回归感到高兴。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_114F")

    label("loc_10F0")


    #C0045
    ChrTalk(
        0x8,
        (
            "道格拉斯副司令一直\x01",
            "都是一位名声响亮的\x01",
            "优秀警备队员。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x8,
        (
            "我们都为副司令的\x01",
            "回归感到高兴。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_114F")

    TalkEnd(0xFE)
    Return()

    # Function_6_5DB end

    def Function_7_1153(): pass

    label("Function_7_1153")

    OP_4B(0x8, 0xFF)

    #C0047
    ChrTalk(
        0x8,
        "报告完毕。\x02",
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x9,
        (
            "原来如此，\x01",
            "在唐古拉姆丘陵举行模拟演习吗……\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x9,
        (
            "虽说只是个小规模演习，\x01",
            "但明显是为了\x01",
            "给我们施加压力。\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x8,
        (
            "是的，看来在居民投票日到来之前，\x01",
            "我们绝对不能放松警惕啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x9,
        (
            "只能与各界人士齐心协力，\x01",
            "继续严加戒备了。\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x9,
        "辛苦你了，继续监视吧。\x02",
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x8,
        "明白！\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x8, 0x10)
    ClearChrFlags(0x9, 0x10)
    SetScenarioFlags(0x0, 2)
    OP_4C(0x8, 0xFF)
    Return()

    # Function_7_1153 end

    def Function_8_127A(): pass

    label("Function_8_127A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6F, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6F, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x152, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_12A3")
    Call(0, 11)
    Return()

    label("loc_12A3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x91, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x91, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x91, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19B, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_12C8")
    Call(0, 20)
    Return()

    label("loc_12C8")

    Call(0, 9)
    Return()

    # Function_8_127A end

    def Function_9_12CC(): pass

    label("Function_9_12CC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6F, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6F, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x152, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_12F5")
    Call(0, 11)
    Return()

    label("loc_12F5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x91, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x91, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x91, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19B, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_131A")
    Call(0, 20)
    Return()

    label("loc_131A")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1DD5")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x91, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_1A50")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x91, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14A6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1423")

    #C0054
    ChrTalk(
        0x9,
        (
            "我已经联络过负责人员，\x01",
            "交代他们解除古战场的封锁了。\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x9,
        (
            "你们就经由阿尔摩利卡古道，\x01",
            "前往魔兽的出现地点吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x9,
        (
            "警备队无法抽出人手去消灭魔兽，\x01",
            "我也感到十分遗憾……\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x9,
        (
            "但我相信你们一定\x01",
            "能解决这个问题的。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_14A1")

    label("loc_1423")


    #C0058
    ChrTalk(
        0x9,
        (
            "我已经联络过负责人员，\x01",
            "交代他们解除古战场的封锁了。\x02\x03",

            "你们就经由古道，前往现场吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x9,
        (
            "我相信你们一定能\x01",
            "解决这个问题的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14A1")

    Jump("loc_1A4C")

    label("loc_14A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19D, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19D7")

    #C0060
    ChrTalk(
        0x9,
        "辛苦你们了，支援科的各位。\x02",
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x9,
        (
            "虽说还有一大堆事情等着处理，\x01",
            "但多亏有你们相助，总算解决掉了\x01",
            "一件让人挂心的问题。\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x9,
        (
            "在那场袭击事件中，我们蒙受了\x01",
            "巨大损失，如今实在是人手不足，\x01",
            "所以真的很感谢你们。\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x101,
        "#00000F不用客气，困难的时候就该互相帮助。\x02",
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x102,
        (
            "#00103F……警备队的损失\x01",
            "肯定相当严重吧？\x02\x03",

            "#00101F重振警备队的计划\x01",
            "如今已经进展到哪个阶段了？\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x9,
        (
            "……毕竟还得应对眼前的紧张状态，\x01",
            "老实说，如今还没有多大进展。\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x9,
        (
            "不过，等诺艾尔上士回到警备队之后，\x01",
            "应该就可以兼顾到那方面了吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x9,
        (
            "到时候，会把她安排在最合适的\x01",
            "岗位上，以便为重振警备队\x01",
            "做出贡献。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_16FE")
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)

    label("loc_16FE")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1721")
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)

    label("loc_1721")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1744")
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)

    label("loc_1744")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1764")
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    label("loc_1764")

    Sleep(1000)

    #C0068
    ChrTalk(
        0x104,
        "#00305F这是指……\x02",
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x109,
        "#10108F……升职吗？\x02",
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x9,
        (
            "……在警备队这次遭受的损伤中，\x01",
            "从某种意义上来说，最为重大的\x01",
            "其实是对『士气』的打击。\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x9,
        (
            "因同伴的牺牲而深受打击，\x01",
            "不少人已经开始对警备队的\x01",
            "职责感到恐惧了。\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0x9,
        (
            "尽管也有一部分队员\x01",
            "凭借愤怒和自尊而\x01",
            "坚定了勇气，但还是……\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0x103,
        (
            "#00203F……确实如此，\x01",
            "我能感受到他们\x01",
            "那种想法。\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x9,
        (
            "为了恢复丧失的士气，\x01",
            "我们需要优秀的士官。\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0x9,
        (
            "虽说此事还没定案……\x01",
            "但你确实拥有\x01",
            "那样的能力。\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x109,
        (
            "#10103F……我也不知自己能否\x01",
            "做得像米蕾优三尉那样出色……\x02\x03",

            "#10101F但只要警备队有需要，\x01",
            "我一定会拼尽全力，完成自己的使命。\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0x9,
        (
            "……抱歉，\x01",
            "接下来将会是一段艰难时期，\x01",
            "就拜托你多多努力了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x19D, 3)
    Jump("loc_1A4C")

    label("loc_19D7")


    #C0078
    ChrTalk(
        0x9,
        (
            "为了重振警备队，\x01",
            "到时候肯定会把上士\x01",
            "安排在最合适的岗位上。\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0x9,
        (
            "接下来将会是一段艰难时期，\x01",
            "就拜托你多多努力了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A4C")

    TalkEnd(0x9)
    Return()

    label("loc_1A50")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18E, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D5B")

    #C0080
    ChrTalk(
        0x9,
        (
            "警备队在这一系列事件中蒙受的\x01",
            "损失简直无法估量。\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0x9,
        (
            "等诺艾尔上士回到警备队之后，\x01",
            "必然会让她站在适合的岗位上，\x01",
            "以便为重振警备队做出贡献。\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x101,
        "#00005F这是指……\x02",
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x109,
        "#10108F……升职吗？\x02",
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x9,
        (
            "……在警备队这次遭受的损伤中，\x01",
            "从某种意义上来说，最为重大的\x01",
            "其实是对『士气』的打击。\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0x9,
        (
            "因同伴的牺牲而深受打击，\x01",
            "不少人已经开始对警备队的\x01",
            "职责感到恐惧了。\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x9,
        (
            "尽管也有一部分队员\x01",
            "凭借愤怒和自尊而\x01",
            "坚定了勇气，但还是……\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x103,
        (
            "#00203F……确实如此，\x01",
            "我能感受到他们\x01",
            "那种想法。\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0x9,
        (
            "为了恢复丧失的士气，\x01",
            "我们需要优秀的士官。\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0x9,
        (
            "虽说此事还没有定案……\x01",
            "但你确实拥有\x01",
            "那样的能力。\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x109,
        (
            "#10103F……我也不知自己能否\x01",
            "做得像米蕾优三尉那样出色……\x02\x03",

            "#10101F但只要警备队有需要，\x01",
            "我一定会拼尽全力，完成自己的使命。\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x9,
        (
            "……抱歉，\x01",
            "接下来将会是一段艰难时期，\x01",
            "就拜托你多多努力了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x18E, 3)
    Jump("loc_1DD0")

    label("loc_1D5B")


    #C0092
    ChrTalk(
        0x9,
        (
            "为了重振警备队，\x01",
            "到时候肯定会把上士\x01",
            "安排在最合适的岗位上。\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x9,
        (
            "接下来将会是一段艰难时期，\x01",
            "就拜托你多多努力了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DD0")

    Jump("loc_2E6D")

    label("loc_1DD5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_22E8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x170, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2030")

    #C0094
    ChrTalk(
        0x9,
        (
            "听说你们几个在昨天那起\x01",
            "脱轨事件的现场\x01",
            "立了大功啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0x104,
        (
            "#00300F哈哈，多亏我们支援科的\x01",
            "队长大显身手。\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0x101,
        (
            "#00006F等等……\x01",
            "你说得也太夸张了。\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0x102,
        "#00100F呵呵，没有的事。\x02",
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x9,
        (
            "我在警察学校对你的教导\x01",
            "以战斗技术为主……\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0x9,
        (
            "但罗伊德，如今你已经成长为\x01",
            "一名很全面的优秀搜查官了，\x01",
            "真是让人觉得感慨万分啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0x101,
        (
            "#00012F连、连副司令都……\x02\x03",

            "#00003F……我仍有很多不足之处，\x01",
            "还远远及不上大哥。\x02\x03",

            "#00000F能取得现在的成绩，只是因为我拥有\x01",
            "一群能替我弥补这段差距的同伴而已。\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0x103,
        "#00200F罗伊德前辈……\x02",
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x9,
        (
            "呵呵，很好。\x01",
            "这样下去，你一定\x01",
            "还能继续成长。\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0x9,
        "罗伊德，我很期待你的将来哦。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x170, 2)
    Jump("loc_22E3")

    label("loc_2030")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x189, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_21E1")

    #C0104
    ChrTalk(
        0x9,
        "啊，对了……\x02",
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0x9,
        (
            "你们几个要不要\x01",
            "读一读这本书？\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0106
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x2F6),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x2F6, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x189, 0)

    #C0107
    ChrTalk(
        0x102,
        "#00105F这是……娱乐小说吗？\x02",
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0x104,
        (
            "#00309F道格拉斯老兄，你居然也会\x01",
            "看这种书，真叫人意外啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0x9,
        "哈哈，我平时也会看看小说的。\x02",
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0x9,
        (
            "这本书是索妮亚司令\x01",
            "推荐给我的……\x01",
            "但你们也知道，我最近实在是太忙了。\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0x9,
        (
            "总之，就是这么一回事，\x01",
            "你们要是有时间的话，就看看那本书吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0x101,
        "#00000F嗯，谢谢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_22E3")

    label("loc_21E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_227A")

    #C0113
    ChrTalk(
        0x9,
        "好了，还是说回正题吧……\x02",
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0x9,
        (
            "现在离脱轨事故只过了一晚而已，\x01",
            "还不能完全放下心来。\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0x9,
        (
            "暂时还是让\x01",
            "警备队在铁路附近\x01",
            "加强警戒为好。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_22E3")

    label("loc_227A")


    #C0116
    ChrTalk(
        0x9,
        (
            "现在离脱轨事故只过了一晚而已，\x01",
            "还不能完全放下心来。\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0x9,
        (
            "暂时还是让\x01",
            "警备队在铁路附近\x01",
            "加强警戒为好。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_22E3")

    Jump("loc_2E6D")

    label("loc_22E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2598")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x170, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2528")

    #C0118
    ChrTalk(
        0x9,
        (
            "你们通过调查而发现的那种\x01",
            "名为『灵智之草』的东西……\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0x9,
        (
            "听说就是『真知』的\x01",
            "原材料啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0x9,
        (
            "那可是一种\x01",
            "十分危险的药物……\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0x101,
        (
            "#00005F对了，副司令……\x01",
            "教团事件发生时，\x01",
            "您在警察学校里吧？\x02\x03",

            "#00003F我记得被操控的警备队\x01",
            "首先就袭击了那个地方……\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0x109,
        "#10105F啊……\x02",
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0x9,
        (
            "……老实说，那群被操纵的\x01",
            "队员突然袭来时，\x01",
            "我们可真是狼狈不堪。\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0x9,
        (
            "结果，我和警察学校的人员\x01",
            "没能控制住局面……\x01",
            "导致阿奈斯特秘书从拘留所逃走了。\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0x102,
        "#00108F原来是这样……\x02",
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0x9,
        (
            "能制成那种强力药物的原料，\x01",
            "居然就是幻兽出现的原因。\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0x9,
        (
            "这次的幻兽骚动……\x01",
            "说不定比想象中\x01",
            "还要危险。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x170, 1)
    Jump("loc_2593")

    label("loc_2528")


    #C0128
    ChrTalk(
        0x9,
        (
            "能制成那种强力药物的原料，\x01",
            "居然就是幻兽出现的原因。\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0x9,
        (
            "这次的幻兽骚动……\x01",
            "说不定比想象中\x01",
            "还要危险。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2593")

    Jump("loc_2E6D")

    label("loc_2598")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2632")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_25B3")
    Call(0, 7)
    Jump("loc_262D")

    label("loc_25B3")


    #C0130
    ChrTalk(
        0x9,
        (
            "正如你们所见，我们实在是抽不出人手\x01",
            "去处理『幻兽』的问题。\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0x9,
        (
            "虽说这样会给你们增加负担，\x01",
            "但调查方面还是拜托各位了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_262D")

    Jump("loc_2E6D")

    label("loc_2632")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2640")
    Jump("loc_2E6D")

    label("loc_2640")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2C3C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x159, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B1F")

    #C0132
    ChrTalk(
        0x109,
        "#10100F副司令，您辛苦了！\x02",
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0x9,
        (
            "哦，是你们啊。\x01",
            "来得正好。\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0x9,
        (
            "我正想休息一下，\x01",
            "难得你们过来一趟，\x01",
            "就随便聊聊吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0x104,
        (
            "#00300F呼，我还以为\x01",
            "老兄你又会让\x01",
            "我们陪你演习呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0x9,
        (
            "嗯，虽然我很想那么做，\x01",
            "但实在是没时间啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0x101,
        (
            "#00009F哈哈……\x01",
            "您果然很忙呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0x9,
        (
            "不管怎么说，\x01",
            "明天就是正式会议了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0x9,
        (
            "我们已经把通商会议的\x01",
            "警备措施安排得十分周全了，\x01",
            "但实际状况总是瞬息万变。\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0x9,
        (
            "明天早上，有必要再和\x01",
            "负责米修拉姆警备工作的\x01",
            "索妮亚司令商量一下。\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0x102,
        (
            "#00103F说得也是……\x01",
            "毕竟众多国宾都\x01",
            "聚集在兰花塔。\x02",
        )
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0x105,
        (
            "#10300F无论花多少精力\x01",
            "准备都不为过。\x02",
        )
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0x104,
        (
            "#00300F总之，这方面的事情交给\x01",
            "警备队就能安心了。\x02\x03",

            "#00304F毕竟现在的警备队中\x01",
            "有『迅雷道格拉斯』坐镇啊。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2907")
    OP_63(0x0, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)

    label("loc_2907")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2931")
    OP_63(0x1, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)

    label("loc_2931")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_295B")
    OP_63(0x2, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)

    label("loc_295B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2982")
    OP_63(0x3, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)

    label("loc_2982")

    Sleep(1000)

    #C0144
    ChrTalk(
        0x109,
        "#10105F迅雷吗……？\x02",
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0x9,
        (
            "哈哈，这名字可真\x01",
            "叫人怀念啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0x9,
        (
            "被派到警察学校之前，\x01",
            "有些人就是那样\x01",
            "称呼我的。\x02",
        )
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0x9,
        (
            "话说回来，又是迅雷又是鬼的……\x01",
            "总有人随便给我起\x01",
            "这种绰号啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0x101,
        (
            "#00000F哈哈，我倒觉得\x01",
            "这两个绰号都很适合您呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0x9,
        "你就别拿我开玩笑了。\x02",
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0x9,
        (
            "咳咳，还是回到正题吧……\x01",
            "通商会议的警备措施\x01",
            "已经安排得很妥当了。\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0x9,
        (
            "你们不必太过挂心，\x01",
            "专心去做自己的工作吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0x101,
        "#00000F好的，我们会的。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x159, 0)
    Jump("loc_2C37")

    label("loc_2B1F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2BD3")

    #C0153
    ChrTalk(
        0x9,
        (
            "『迅雷』吗……\x01",
            "哈哈，这绰号可真叫人怀念。\x02",
        )
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0x9,
        (
            "咳咳，总之……\x01",
            "我们已经把通商会议的\x01",
            "警备措施安排得十分周全了。\x02",
        )
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0x9,
        (
            "你们不必太过挂心，\x01",
            "专心去做自己的工作吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2C37")

    label("loc_2BD3")


    #C0156
    ChrTalk(
        0x9,
        (
            "我们已经把通商会议的\x01",
            "警备措施安排得十分周全了。\x02",
        )
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0x9,
        (
            "你们不必太过挂心，\x01",
            "专心去做自己的工作吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C37")

    Jump("loc_2E6D")

    label("loc_2C3C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2E6D")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6F, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2E6D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2DD6")

    #C0158
    ChrTalk(
        0x9,
        (
            "#4P这次的演习真是辛苦各位了。\x01",
            "如果还有什么事，我会再联络你们的。\x02",
        )
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0x9,
        (
            "#4P还有，刚才说的那件事……\x01",
            "请你们千万不要外传，\x01",
            "就把它当作一个秘密吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0x101,
        (
            "#00005F明、明白了。\x01",
            "我们一定会\x01",
            "注意的……\x02",
        )
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0x104,
        (
            "#00304F……到时可得把这件事\x01",
            "告诉阿缇才行¤\x02",
        )
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0x105,
        (
            "#10309F呵呵，说的没错，\x01",
            "不然就太不公平了。\x02",
        )
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0x101,
        (
            "#00011F喂喂，你们两个！\x01",
            "不要当场拆我的台啊！\x02",
        )
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0x9,
        "#4P……总之，拜托各位了。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2E6D")

    label("loc_2DD6")


    #C0165
    ChrTalk(
        0x9,
        (
            "#4P这次的演习真是辛苦各位了。\x01",
            "如果还有什么事，我会再联络你们的。\x02",
        )
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0x9,
        (
            "#4P还有，刚才说的那件事……\x01",
            "请你们千万不要外传，\x01",
            "就把它当作一个『秘密』吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E6D")

    TalkEnd(0x9)
    Return()

    # Function_9_12CC end

    def Function_10_2E71(): pass

    label("Function_10_2E71")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-1120, 900, -310, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25500, 0)
    SetChrPos(0x9, 6630, 0, -20, 270)
    SetChrPos(0x101, -5500, 0, -20, 90)
    SetChrPos(0x102, -5500, 0, -20, 90)
    SetChrPos(0x104, -5500, 0, -20, 90)
    SetChrPos(0x109, -5500, 0, -20, 90)
    SetChrPos(0x105, -5500, 0, -20, 90)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()
    Sound(105, 0, 100, 0)
    BeginChrThread(0x101, 3, 0, 12)
    Sleep(700)
    BeginChrThread(0x109, 3, 0, 13)
    Sleep(700)
    BeginChrThread(0x102, 3, 0, 14)
    OP_68(930, 900, -520, 3000)
    Sleep(700)
    BeginChrThread(0x104, 3, 0, 15)
    Sleep(700)
    BeginChrThread(0x105, 3, 0, 16)
    WaitChrThread(0x105, 3)
    OP_6F(0x79)

    #C0167
    ChrTalk(
        0x9,
        "#11P你们总算来了啊。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0168
    ChrTalk(
        0x101,
        "#6P#00002F啊……\x02",
    )

    CloseMessageWindow()
    OP_68(3420, 900, 80, 3000)
    MoveCamera(45, 19, 0, 3000)
    OP_6E(350, 3000)
    SetCameraDistance(25500, 3000)

    def lambda_3070():
        OP_98(0xFE, 0x9C4, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3070)
    Sleep(100)

    def lambda_308D():
        OP_98(0xFE, 0xBB8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_308D)
    Sleep(100)

    def lambda_30AA():
        OP_98(0xFE, 0xBB8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_30AA)
    Sleep(100)

    def lambda_30C7():
        OP_98(0xFE, 0xAF0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_30C7)
    Sleep(100)

    def lambda_30E4():
        OP_98(0xFE, 0x9C4, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_30E4)
    Sleep(1000)
    OP_6F(0x79)
    OP_0D()

    #C0169
    ChrTalk(
        0x109,
        (
            "#10100F道格拉斯副司令……\x01",
            "您辛苦了！\x02",
        )
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0x9,
        "#11P哟，希卡上士。\x02",
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0x9,
        (
            "#11P你在特别任务支援科\x01",
            "待得还好吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0x109,
        (
            "#10100F是的！\x01",
            "我每天都能学到\x01",
            "很多东西！\x02",
        )
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0x9,
        "#11P哈哈，那真是再好不过。\x02",
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0x9,
        (
            "#11P为了将来，\x01",
            "你可要好好磨练自己。\x02",
        )
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0x102,
        "#12P#00105F诺艾尔小姐，请问这位就是……？\x02",
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0x9,
        (
            "#11P……啊，我还没向各位\x01",
            "自我介绍呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0x9,
        (
            "#11P我的名字是道格拉斯，\x01",
            "目前担任警备队的\x01",
            "副司令。\x02",
        )
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0x9,
        (
            "#11P我听司令说过\x01",
            "你们不少的事迹，\x01",
            "今后有需要的话就麻烦你们了。\x02",
        )
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0x102,
        "#6P#00100F请您多多指教。\x02",
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0x105,
        (
            "#6P#10302F呵呵，看来是位\x01",
            "表里如一的率直之人。\x02",
        )
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0x104,
        (
            "#6P#00300F你还是和以前一样有精神啊，\x01",
            "道格拉斯老兄。\x02",
        )
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0x9,
        (
            "#11P你也没变啊，兰迪。\x01",
            "贝尔加德门的复健训练，\x01",
            "实在是辛苦你啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0x9,
        (
            "#11P还有，罗伊德，\x01",
            "好久不见了。\x02",
        )
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0x9,
        (
            "#11P在之前的教团事件中，\x01",
            "你似乎大展身手啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0x101,
        (
            "#6P#00000F哈哈……\x01",
            "好久不见。\x02\x03",

            "#00004F听到教官成为\x01",
            "副司令这个消息时，\x01",
            "真让我大吃一惊。\x02\x03",

            "#00012F被『鬼之道格拉斯』\x01",
            "严厉训练的记忆又清晰地\x01",
            "浮现在我的脑海中了……\x02",
        )
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0x9,
        (
            "#11P喂喂，别再提起我\x01",
            "以前的绰号了。\x02",
        )
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0x9,
        "#11P真是的，会让人不好意思的。\x02",
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0x102,
        (
            "#6P#00100F（唔……看来他在警察学校\x01",
            "  是位十分严厉的人呢……）\x02",
        )
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0x9,
        (
            "#11P……好了，\x01",
            "叙旧就到此为止吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0x9,
        (
            "#11P今天可是为了工作，\x01",
            "才特地叫你们过来的。\x02",
        )
    )

    CloseMessageWindow()

    #C0191
    ChrTalk(
        0x105,
        (
            "#6P#10300F说到工作……\x01",
            "就是『参加演习』吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0x9,
        "#11P是啊，就是那个。\x02",
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0x9,
        (
            "#11P这次演习的目的，就是狠狠\x01",
            "纠正你们特别任务支援科的弱点。\x02",
        )
    )

    CloseMessageWindow()

    #C0194
    ChrTalk(
        0x9,
        (
            "#11P让你们好好体会一下\x01",
            "我的超严厉训练。\x02",
        )
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0x101,
        (
            "#6P#00005F咦……\x01",
            "这场演习不是为了警备队，\x01",
            "而是为了我们吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0x9,
        (
            "#11P对警备队员来说，\x01",
            "这自然也会是一次难得的经验。\x02",
        )
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0x9,
        (
            "#11P另外，我已经跟警察局的\x01",
            "上层打过招呼了，这次的演习\x01",
            "将会以正式联合训练为名义。\x02",
        )
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0x104,
        (
            "#6P#00300F原来如此……\x01",
            "与其说是支援请求，\x01",
            "更应该算是一场正式训练啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0x9,
        "#11P哈哈，就是这么一回事。\x02",
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0x9,
        (
            "#11P我们这边已经准备完毕，\x01",
            "接下来就看你们了……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)
    Sleep(500)

    #C0201
    ChrTalk(
        0x102,
        (
            "#12P#00100F我们还是先\x01",
            "调整一下装备为好。\x02\x03",

            "#00104F回路的组合也\x01",
            "有必要认真调整。\x02",
        )
    )

    CloseMessageWindow()

    #C0202
    ChrTalk(
        0x9,
        (
            "#11P怎么样？\x01",
            "可以马上开始演习吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x6F, 0x1, 0x0)
    Call(0, 17)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_10_2E71 end

    def Function_11_3827(): pass

    label("Function_11_3827")

    EventBegin(0x0)
    Fade(500)
    OP_68(3420, 900, 80, 0)
    MoveCamera(45, 19, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25500, 0)
    SetChrPos(0x101, 2500, 0, -20, 90)
    SetChrPos(0x109, 2500, 0, 980, 90)
    SetChrPos(0x102, 2500, 0, -1020, 90)
    SetChrPos(0x104, 1300, 0, 680, 90)
    SetChrPos(0x105, 1000, 0, -720, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_0D()

    #C0203
    ChrTalk(
        0x9,
        (
            "#11P为了队员们的训练，\x01",
            "希望你们能当他们的\x01",
            "演习对手。\x02",
        )
    )

    CloseMessageWindow()

    #C0204
    ChrTalk(
        0x9,
        (
            "#11P我们这边已经准备完毕，\x01",
            "可以马上开始演习吗？\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 17)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_11_3827 end

    def Function_12_393B(): pass

    label("Function_12_393B")


    def lambda_3940():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3940)

    def lambda_3951():
        OP_98(0xFE, 0x157C, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3951)
    WaitChrThread(0x101, 1)
    Return()

    # Function_12_393B end

    def Function_13_396B(): pass

    label("Function_13_396B")


    def lambda_3970():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_3970)

    def lambda_3981():
        OP_98(0xFE, 0xFA0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_3981)
    WaitChrThread(0x109, 1)
    OP_97(0x109, 0x0, 0x0, 0x3E8, 0x7D0, 0x0)
    OP_97(0x109, 0x3E8, 0x0, 0x0, 0x7D0, 0x0)
    Return()

    # Function_13_396B end

    def Function_14_39C3(): pass

    label("Function_14_39C3")


    def lambda_39C8():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_39C8)

    def lambda_39D9():
        OP_98(0xFE, 0xFA0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_39D9)
    WaitChrThread(0x102, 1)
    OP_97(0x102, 0x0, 0x0, 0xFFFFFC18, 0x7D0, 0x0)
    OP_97(0x102, 0x3E8, 0x0, 0x0, 0x7D0, 0x0)
    Return()

    # Function_14_39C3 end

    def Function_15_3A1B(): pass

    label("Function_15_3A1B")


    def lambda_3A20():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_3A20)

    def lambda_3A31():
        OP_98(0xFE, 0xBB8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3A31)
    WaitChrThread(0x104, 1)
    OP_97(0x104, 0x3E8, 0x0, 0x2BC, 0x7D0, 0x0)
    OP_93(0x104, 0x5A, 0x1F4)
    Return()

    # Function_15_3A1B end

    def Function_16_3A66(): pass

    label("Function_16_3A66")


    def lambda_3A6B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_3A6B)

    def lambda_3A7C():
        OP_98(0xFE, 0xBB8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_3A7C)
    WaitChrThread(0x105, 1)
    OP_97(0x105, 0x3E8, 0x0, 0xFFFFFD44, 0x7D0, 0x0)
    OP_93(0x105, 0x5A, 0x1F4)
    Return()

    # Function_16_3A66 end

    def Function_17_3AB1(): pass

    label("Function_17_3AB1")

    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【开始演习】\x01",          # 0
            "【还没做好准备】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3B1F"),
        (1, "loc_3B27"),
        (SWITCH_DEFAULT, "loc_3BB4"),
    )


    label("loc_3B1F")

    Call(0, 18)
    Jump("loc_3BB4")

    label("loc_3B27")


    #C0205
    ChrTalk(
        0x101,
        (
            "#6P#00000F不好意思……\x01",
            "可以再给我们一些时间吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0206
    ChrTalk(
        0x9,
        "#11P唔，这样啊。\x02",
    )

    CloseMessageWindow()

    #C0207
    ChrTalk(
        0x9,
        (
            "#11P那么，等你们做好准备之后，\x01",
            "再来和我打声招呼吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetScenarioFlags(0x152, 0)
    Jump("loc_3BB4")

    label("loc_3BB4")

    Return()

    # Function_17_3AB1 end

    def Function_18_3BB5(): pass

    label("Function_18_3BB5")


    #C0208
    ChrTalk(
        0x101,
        (
            "#6P#00000F没问题，我们也\x01",
            "已经准备好了。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x102, 0x5A, 0x1F4)
    Sleep(500)

    #C0209
    ChrTalk(
        0x9,
        "#11P很好。\x02",
    )

    CloseMessageWindow()

    #C0210
    ChrTalk(
        0x9,
        (
            "#11P希卡上士，\x01",
            "不要因为对手是警备队员\x01",
            "而出手迟疑哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0211
    ChrTalk(
        0x9,
        (
            "#11P站在与过去的同伴对立的立场上，\x01",
            "也能让你学到一些新的东西。\x02",
        )
    )

    CloseMessageWindow()

    #C0212
    ChrTalk(
        0x109,
        "#10100F是，我明白了！\x02",
    )

    CloseMessageWindow()

    #C0213
    ChrTalk(
        0x9,
        (
            "#11P好了，\x01",
            "那就赶快开始演习吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0214
    ChrTalk(
        0x9,
        (
            "#11P全员到\x01",
            "室外的停车场集合。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(80, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0215
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "任务【参加警备队的演习】\x07\x00",
            "开始！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_29(0x6F, 0x1, 0x1)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetScenarioFlags(0x22, 1)
    NewScene("t2500", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_18_3BB5 end

    def Function_19_3D49(): pass

    label("Function_19_3D49")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(3420, 900, 80, 0)
    MoveCamera(45, 19, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25500, 0)
    SetChrPos(0x9, 6630, 0, -20, 270)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x101, 2500, 0, -20, 90)
    SetChrPos(0x109, 2500, 0, 980, 90)
    SetChrPos(0x102, 2500, 0, -1020, 90)
    SetChrPos(0x104, 1300, 0, 680, 90)
    SetChrPos(0x105, 1000, 0, -720, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()

    #C0216
    ChrTalk(
        0x9,
        (
            "#11P各位，\x01",
            "这次演习真是辛苦你们了。\x02",
        )
    )

    CloseMessageWindow()

    #C0217
    ChrTalk(
        0x9,
        (
            "#11P对各位警备队员来说，\x01",
            "这肯定是一次难得的经历。\x02",
        )
    )

    CloseMessageWindow()

    #C0218
    ChrTalk(
        0x101,
        (
            "#6P#00000F哪里，我们应该向您道谢才对。\x01",
            "对于我们而言，这也是一次很难得的经历。\x02",
        )
    )

    CloseMessageWindow()

    #C0219
    ChrTalk(
        0x104,
        (
            "#6P#00306F话说回来，你的实力\x01",
            "可真是丝毫没有减退啊。\x02\x03",

            "#00300F我又想起在第一次演习时，\x01",
            "被你修理得惨兮兮的事情了。\x02",
        )
    )

    CloseMessageWindow()

    #C0220
    ChrTalk(
        0x9,
        (
            "#11P说起来，你真是\x01",
            "成长了不少嘛。\x02",
        )
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0x9,
        (
            "#11P我当初传授的冲击斧枪技术，\x01",
            "你如今也已经能运用自如了。\x02",
        )
    )

    CloseMessageWindow()

    #C0222
    ChrTalk(
        0x104,
        (
            "#6P#00304F那当然，而且已经进化为\x01",
            "超绝潇洒，优雅无比的\x01",
            "兰迪风格了。\x02",
        )
    )

    CloseMessageWindow()

    #C0223
    ChrTalk(
        0x101,
        (
            "#6P#00000F冲击斧枪……？\x01",
            "原来是这样啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0224
    ChrTalk(
        0x102,
        (
            "#6P#00109F呵呵，对兰迪来说，\x01",
            "您就像恩人一样呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0x9,
        (
            "#11P没办法，因为这小子无论如何也\x01",
            "不肯使用来复枪，\x01",
            "只好集中教他练习另一种武器了。\x02",
        )
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0x9,
        (
            "#11P可能也正因如此，\x01",
            "使他练就了一身只靠斧枪\x01",
            "也足以在第一线战斗的本领。\x02",
        )
    )

    CloseMessageWindow()

    #C0227
    ChrTalk(
        0x9,
        (
            "#11P不过，这也正是前司令阁下\x01",
            "讨厌他的主要原因。\x02",
        )
    )

    CloseMessageWindow()

    #C0228
    ChrTalk(
        0x104,
        (
            "#6P#00300F哈哈，反正被规矩限制\x01",
            "也不符合我的性格。\x02\x03",

            "#00309F多亏如此，我才被调到了支援科，\x01",
            "如今过得非常愉快。\x02",
        )
    )

    CloseMessageWindow()

    #C0229
    ChrTalk(
        0x105,
        (
            "#6P#10304F呵呵，也就是说，\x01",
            "好事坏事都是拜\x01",
            "副司令阁下所赐呢。\x02\x03",

            "#10302F把您贬职到\x01",
            "警察学校真是一次\x01",
            "错误的人事调动啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0230
    ChrTalk(
        0x109,
        (
            "#10100F嗯，毕竟在教团事件之前，\x01",
            "警备队都在那位前司令的\x01",
            "掌控之下。\x02\x03",

            "#10109F您深得部下的信赖，\x01",
            "自身又具备极强的实力，\x01",
            "难免会受到排挤……\x02",
        )
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0x9,
        (
            "#11P倒也没有那么夸张……\x01",
            "不过，我确实是前司令的眼中钉。\x02",
        )
    )

    CloseMessageWindow()

    #C0232
    ChrTalk(
        0x9,
        (
            "#11P前往警察学校之后，\x01",
            "我一直都在专心培养\x01",
            "可以改变那种腐朽体制的人才。\x02",
        )
    )

    CloseMessageWindow()

    #C0233
    ChrTalk(
        0x9,
        (
            "#11P现在回想起来，\x01",
            "被贬职或许也是\x01",
            "一种幸运呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0234
    ChrTalk(
        0x9,
        (
            "#11P多亏如此，我才有机会去教导\x01",
            "那些尚如白纸般纯净的\x01",
            "警备队员与警察雏鸟。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0235
    ChrTalk(
        0x101,
        (
            "#6P#00012F但当时觉得您\x01",
            "实在是太严厉了。\x02\x03",

            "#00006F弗兰茨他们有时候\x01",
            "甚至会掉眼泪呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0236
    ChrTalk(
        0x9,
        (
            "#11P哈哈，别这么说。\x01",
            "那些锻炼不是对你们很有益处嘛。\x02",
        )
    )

    CloseMessageWindow()

    #C0237
    ChrTalk(
        0x9,
        (
            "#11P总之，虽然发生了很多事情，\x01",
            "但我最终还是再次回到警备队了。\x02",
        )
    )

    CloseMessageWindow()

    #C0238
    ChrTalk(
        0x9,
        (
            "#11P希望你们今后也能\x01",
            "和我齐心协力，\x01",
            "共同保卫自治州。\x02",
        )
    )

    CloseMessageWindow()

    #C0239
    ChrTalk(
        0x102,
        (
            "#6P#00100F呵呵……\x01",
            "我们会竭尽全力的。\x02\x03",

            "#00104F但我们几个\x01",
            "都还不够成熟呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0240
    ChrTalk(
        0x9,
        (
            "#11P不必谦虚，\x01",
            "你们已经拥有\x01",
            "很不错的实力了。\x02",
        )
    )

    CloseMessageWindow()

    #C0241
    ChrTalk(
        0x9,
        (
            "#11P这应该是在赛尔盖前辈建立的\x01",
            "特别任务支援科中努力工作，\x01",
            "一点一滴累积起来的成果吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0242
    ChrTalk(
        0x101,
        "#6P#00005F赛尔盖前辈……？\x02",
    )

    CloseMessageWindow()

    #C0243
    ChrTalk(
        0x104,
        (
            "#6P#00305F哦？你还认识\x01",
            "那大叔吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0244
    ChrTalk(
        0x9,
        "#11P嗯？当然认识啊……\x02",
    )

    CloseMessageWindow()

    #C0245
    ChrTalk(
        0x9,
        (
            "#11P赛尔盖前辈和\x01",
            "索妮亚前辈\x01",
            "一直都很照顾我。\x02",
        )
    )

    CloseMessageWindow()

    #C0246
    ChrTalk(
        0x9,
        (
            "#11P而且他们两人正是由于我的牵线搭桥\x01",
            "才会结婚的。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0247
    ChrTalk(
        0x101,
        "#6P#00011F什么……！！！！\x02",
    )

    CloseMessageWindow()

    #C0248
    ChrTalk(
        0x102,
        "#4S#6P#00105F结婚…………！？\x02",
    )

    CloseMessageWindow()

    #C0249
    ChrTalk(
        0x109,
        (
            "#4S#10111F索妮亚司令和……\x01",
            "赛尔盖科长！？\x02",
        )
    )

    CloseMessageWindow()

    #C0250
    ChrTalk(
        0x105,
        "#6P#10305F哇……\x02",
    )

    CloseMessageWindow()

    #C0251
    ChrTalk(
        0x104,
        (
            "#6P#00306F喂喂喂，\x01",
            "怎么突然曝出了\x01",
            "冲击性这么强的事情啊……！\x02",
        )
    )

    CloseMessageWindow()

    #C0252
    ChrTalk(
        0x9,
        (
            "#11P……怎、怎么？\x01",
            "难道你们不知道吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0253
    ChrTalk(
        0x9,
        (
            "#11P不过，他们已经在\x01",
            "五年前分手了。\x02",
        )
    )

    CloseMessageWindow()

    #C0254
    ChrTalk(
        0x9,
        (
            "#11P赛尔盖前辈遭到降职，\x01",
            "而索妮亚前辈却得到晋升，\x01",
            "总之，当时的情况很复杂……\x02",
        )
    )

    CloseMessageWindow()

    #C0255
    ChrTalk(
        0x105,
        (
            "#6P#10304F呵呵，原来如此。\x01",
            "似乎是只会出现在成年男女\x01",
            "之间的戏剧性故事呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0256
    ChrTalk(
        0x109,
        (
            "#10105F这……\x01",
            "索妮亚司令居然……\x02",
        )
    )

    CloseMessageWindow()

    #C0257
    ChrTalk(
        0x104,
        (
            "#6P#00303F老实说，我一直隐隐觉得\x01",
            "他们两个的关系有些古怪……\x02\x03",

            "#00309F这该怎么说呢，\x01",
            "算是解开了一个谜团吧¤\x02",
        )
    )

    CloseMessageWindow()

    #C0258
    ChrTalk(
        0x101,
        (
            "#6P#00011F等、等等，各位……\x01",
            "别拿这件事来说笑啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0259
    ChrTalk(
        0x102,
        (
            "#6P#00109F（其、其实我也\x01",
            "  有些在意……）\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0260
    ChrTalk(
        0x9,
        (
            "#11P……糟了，\x01",
            "一不小心就说漏嘴了。\x02",
        )
    )

    CloseMessageWindow()

    #C0261
    ChrTalk(
        0x9,
        (
            "#11P总、总之，\x01",
            "千万别随便把\x01",
            "这件事告诉其他人。\x02",
        )
    )

    CloseMessageWindow()

    #C0262
    ChrTalk(
        0x9,
        (
            "#11P咳咳，那么……\x01",
            "这次的演习真是辛苦你们了。\x02",
        )
    )

    CloseMessageWindow()

    #C0263
    ChrTalk(
        0x9,
        "#11P如果还有什么事，我会再拜托你们的。\x02",
    )

    CloseMessageWindow()

    #C0264
    ChrTalk(
        0x101,
        (
            "#6P#00000F好、好的，\x01",
            "我们期待您的联络。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0265
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "任务【参加警备队的演习】\x07\x00",
            "完成！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    OP_29(0x6F, 0x1, 0x4)
    OP_29(0x6F, 0x1, 0x5)
    OP_29(0x6F, 0x4, 0x10)
    OP_29(0xA3, 0x1, 0x4)
    SetChrPos(0x0, 3000, 0, 0, 90)
    EventEnd(0x5)
    Return()

    # Function_19_3D49 end

    def Function_20_4B93(): pass

    label("Function_20_4B93")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(3420, 900, 80, 0)
    MoveCamera(44, 23, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25500, 0)
    SetChrPos(0x101, 2500, 0, -20, 90)
    SetChrPos(0x102, 2300, 0, -1020, 90)
    SetChrPos(0x103, 2300, 0, 980, 90)
    SetChrPos(0x104, 1000, 0, -20, 90)
    SetChrPos(0x109, 900, 0, 980, 90)
    SetChrPos(0x105, 900, 0, -1020, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_93(0x9, 0x10E, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19B, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_51A5")

    #C0266
    ChrTalk(
        0x101,
        (
            "#6P#00000F道格拉斯副司令，\x01",
            "您辛苦了。\x02",
        )
    )

    CloseMessageWindow()

    #C0267
    ChrTalk(
        0x9,
        (
            "#11P……哦，是你们啊，\x01",
            "各位也辛苦了。\x02",
        )
    )

    CloseMessageWindow()

    #C0268
    ChrTalk(
        0x9,
        (
            "#11P你们这次是为了\x01",
            "委托而来的吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0269
    ChrTalk(
        0x104,
        (
            "#6P#00300F嗯，是的……\x02\x03",

            "#00303F……道格拉斯老兄，总觉得整个\x01",
            "边境门的气氛都很紧张啊。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_4EDE")

    #C0270
    ChrTalk(
        0x9,
        (
            "#11P你们走进边境门的时候，\x01",
            "应该切身感受到了吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0271
    ChrTalk(
        0x9,
        (
            "#11P克洛斯贝尔警备队正处在\x01",
            "严加戒备的状态之中。\x02",
        )
    )

    CloseMessageWindow()

    #C0272
    ChrTalk(
        0x9,
        (
            "#11P不仅如此，刚才还有个\x01",
            "通缉犯驾车强行\x01",
            "冲过了边境大门。\x02",
        )
    )

    CloseMessageWindow()

    #C0273
    ChrTalk(
        0x9,
        (
            "#11P因此现在的状态\x01",
            "更加紧张了。\x02",
        )
    )

    CloseMessageWindow()

    #C0274
    ChrTalk(
        0x102,
        "#6P#00100F是吗……\x02",
    )

    CloseMessageWindow()

    #C0275
    ChrTalk(
        0x9,
        (
            "#11P对了，听说通缉犯被\x01",
            "你们几个逮捕归案了。\x02",
        )
    )

    CloseMessageWindow()

    #C0276
    ChrTalk(
        0x9,
        (
            "#11P我在此要向\x01",
            "你们郑重道谢。\x02",
        )
    )

    CloseMessageWindow()

    #C0277
    ChrTalk(
        0x101,
        (
            "#6P#00003F哪里，那是我们的分内职责。\x02\x03",

            "#00001F……这次的任务\x01",
            "也和如今的局势有关吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_512C")

    label("loc_4EDE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x40)"), scpexpr(EXPR_END)), "loc_5051")

    #C0278
    ChrTalk(
        0x9,
        (
            "#11P你们走进边境门的时候，\x01",
            "应该切身感受到了吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0279
    ChrTalk(
        0x9,
        (
            "#11P克洛斯贝尔警备队正处在\x01",
            "严加戒备的状态之中。\x02",
        )
    )

    CloseMessageWindow()

    #C0280
    ChrTalk(
        0x9,
        (
            "#11P不仅如此，刚才还有个\x01",
            "不像话的家伙驾车强行\x01",
            "冲过了边境大门。\x02",
        )
    )

    CloseMessageWindow()

    #C0281
    ChrTalk(
        0x9,
        (
            "#11P因此现在的状态\x01",
            "更加紧张了。\x02",
        )
    )

    CloseMessageWindow()

    #C0282
    ChrTalk(
        0x102,
        "#6P#00100F是吗……\x02",
    )

    CloseMessageWindow()

    #C0283
    ChrTalk(
        0x101,
        (
            "#6P#00003F（就是我们没能逮捕归案的\x01",
            "　那个医疗物资盗窃犯吧……？）\x02\x03",

            "#00001F……这次的任务\x01",
            "也和如今的局势有关吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_512C")

    label("loc_5051")


    #C0284
    ChrTalk(
        0x9,
        (
            "#11P你们走进边境门的时候，\x01",
            "应该切身感受到了吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0285
    ChrTalk(
        0x9,
        (
            "#11P克洛斯贝尔警备队正处在\x01",
            "严加戒备的状态之中。\x02",
        )
    )

    CloseMessageWindow()

    #C0286
    ChrTalk(
        0x9,
        (
            "#11P我们现在紧张得\x01",
            "连喘口气的时间都没有。\x02",
        )
    )

    CloseMessageWindow()

    #C0287
    ChrTalk(
        0x101,
        (
            "#6P#00001F是吗……\x01",
            "那么，这次的任务\x01",
            "也和如今的局势有关吧？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_512C")


    #C0288
    ChrTalk(
        0x9,
        "#11P嗯，可以这么说。\x02",
    )

    CloseMessageWindow()

    #C0289
    ChrTalk(
        0x9,
        (
            "#11P我想尽早向你们说明\x01",
            "一下任务的具体内容……\x02",
        )
    )

    CloseMessageWindow()

    #C0290
    ChrTalk(
        0x9,
        (
            "#11P怎么样，你们可以\x01",
            "接受委托吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_51E9")

    label("loc_51A5")


    #C0291
    ChrTalk(
        0x9,
        "#11P你们现在有空了吗？\x02",
    )

    CloseMessageWindow()

    #C0292
    ChrTalk(
        0x9,
        "#11P我希望你们尽早接下这个任务……\x02",
    )

    CloseMessageWindow()

    label("loc_51E9")

    Call(0, 21)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 2710, 0, -330, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_20_4B93 end

    def Function_21_5218(): pass

    label("Function_21_5218")

    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【接受】\x01",      # 0
            "【放弃】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_527B")
    Call(0, 22)
    Jump("loc_5332")

    label("loc_527B")


    #C0293
    ChrTalk(
        0x101,
        (
            "#6P#00006F……不好意思，\x01",
            "我们手上已经堆积了\x01",
            "很多工作……\x02",
        )
    )

    CloseMessageWindow()

    #C0294
    ChrTalk(
        0x9,
        (
            "#11P唔……\x01",
            "没办法，毕竟现在\x01",
            "处于特殊时期啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0295
    ChrTalk(
        0x9,
        (
            "#11P我明白了，等你们空闲下来之后，\x01",
            "我再拜托你们吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x19B, 3)

    label("loc_5332")

    Return()

    # Function_21_5218 end

    def Function_22_5333(): pass

    label("Function_22_5333")


    #C0296
    ChrTalk(
        0x101,
        "#6P#00000F好的，那就麻烦您说明一下吧。\x02",
    )

    CloseMessageWindow()

    #C0297
    ChrTalk(
        0x9,
        "#11P嗯，感激不尽。\x02",
    )

    CloseMessageWindow()

    #C0298
    ChrTalk(
        0x9,
        (
            "#11P……在支援请求上已经提到了，\x01",
            "我们接到目击情报，\x01",
            "据说最近出现了奇怪的『黑色魔兽』。\x02",
        )
    )

    CloseMessageWindow()

    #C0299
    ChrTalk(
        0x9,
        (
            "#11P在阿尔摩利卡村一带，\x01",
            "还出现了农作物\x01",
            "与家畜遭到侵害的情况。\x02",
        )
    )

    CloseMessageWindow()

    #C0300
    ChrTalk(
        0x102,
        (
            "#6P#00105F黑色魔兽……\x01",
            "好像曾在\x01",
            "哪里听过呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0301
    ChrTalk(
        0x104,
        (
            "#6P#00303F农作物遭到侵害这种情况\x01",
            "也挺耳熟的。\x02",
        )
    )

    CloseMessageWindow()

    #C0302
    ChrTalk(
        0x109,
        (
            "#10105F这……\x01",
            "不是和以前那起『狼形魔兽』\x01",
            "事件很相似吗？\x02\x03",

            "#10103F那起事件的真凶是\x01",
            "被黑手党操纵的军犬……\x02",
        )
    )

    CloseMessageWindow()

    #C0303
    ChrTalk(
        0x9,
        (
            "#11P……我也曾查阅过\x01",
            "那起事件的报告书，\x01",
            "所以有些在意。\x02",
        )
    )

    CloseMessageWindow()

    #C0304
    ChrTalk(
        0x9,
        (
            "#11P虽说鲁巴彻已经覆灭，\x01",
            "但他们那些军犬大多都\x01",
            "行踪不明。\x02",
        )
    )

    CloseMessageWindow()

    #C0305
    ChrTalk(
        0x9,
        "#11P所以，这次的魔兽很可能就是那些军犬。\x02",
    )

    CloseMessageWindow()

    #C0306
    ChrTalk(
        0x103,
        (
            "#00200F请问，警备队已经\x01",
            "调查到什么程度了？\x02",
        )
    )

    CloseMessageWindow()

    #C0307
    ChrTalk(
        0x9,
        (
            "#11P我们在受害现场\x01",
            "做了一些取证工作，\x01",
            "还向附近的居民询问了一些问题。\x02",
        )
    )

    CloseMessageWindow()

    #C0308
    ChrTalk(
        0x9,
        (
            "#11P调查结果显示，\x01",
            "那些『黑色魔兽』\x01",
            "来自古战场方向。\x02",
        )
    )

    CloseMessageWindow()

    #C0309
    ChrTalk(
        0x9,
        (
            "#11P所以我希望你们\x01",
            "去古战场看看。\x02",
        )
    )

    CloseMessageWindow()

    #C0310
    ChrTalk(
        0x9,
        (
            "#11P调查一下那些魔兽，\x01",
            "如果可能，就把它们消灭掉。\x02",
        )
    )

    CloseMessageWindow()

    #C0311
    ChrTalk(
        0x105,
        (
            "#6P#10302F我们已经大致了解了。\x02\x03",

            "#10303F话说回来，看来你们\x01",
            "相当繁忙啊。\x02\x03",

            "#10300F这类工作原本\x01",
            "都是由警备队\x01",
            "负责处理的……\x02",
        )
    )

    CloseMessageWindow()

    #C0312
    ChrTalk(
        0x9,
        (
            "#11P我也想派人去解决这件事……\x01",
            "但正如刚才所说，\x01",
            "警备队如今正在严加戒备。\x02",
        )
    )

    CloseMessageWindow()

    #C0313
    ChrTalk(
        0x9,
        (
            "#11P袭击了克洛斯贝尔市的犯人\x01",
            "『赤色星座』踪影全无，\x01",
            "我们对他们的下落毫无头绪。\x02",
        )
    )

    CloseMessageWindow()

    #C0314
    ChrTalk(
        0x9,
        (
            "#11P而帝国和共和国正打算\x01",
            "举行大规模演习，\x01",
            "在这种状况下……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_585F")

    #C0315
    ChrTalk(
        0x9,
        (
            "#11P为了不再发生之前那样的事件，\x01",
            "警备队的首要任务\x01",
            "就是加强边境的警备。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5892")

    label("loc_585F")


    #C0316
    ChrTalk(
        0x9,
        (
            "#11P警备队现在的首要任务\x01",
            "就是加强边境的警备。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5892")


    #C0317
    ChrTalk(
        0x102,
        (
            "#6P#00108F毕竟现在的状况……\x01",
            "简直可以和签订《互不侵犯条约》\x01",
            "之前的那段时间相比了。\x02",
        )
    )

    CloseMessageWindow()

    #C0318
    ChrTalk(
        0x9,
        "#11P……嗯。\x02",
    )

    CloseMessageWindow()

    #C0319
    ChrTalk(
        0x9,
        (
            "#11P虽说发生了魔兽侵害事件，\x01",
            "但在这种情况下，优先度还是\x01",
            "比不上边境地带的警备任务。\x02",
        )
    )

    CloseMessageWindow()

    #C0320
    ChrTalk(
        0x9,
        (
            "#11P况且魔兽也没造成\x01",
            "太严重的损失，\x01",
            "我们不可能派人去处理此事。\x02",
        )
    )

    CloseMessageWindow()

    #C0321
    ChrTalk(
        0x104,
        (
            "#6P#00304F……说的也是，\x01",
            "现在可不是派警备队\x01",
            "去消灭魔兽的时候。\x02",
        )
    )

    CloseMessageWindow()

    #C0322
    ChrTalk(
        0x101,
        (
            "#6P#00003F……我们已经大致明白了。\x02\x03",

            "#00000F调查『黑色魔兽』的任务\x01",
            "就交给我们负责吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0323
    ChrTalk(
        0x9,
        "#11P好，麻烦你们了。\x02",
    )

    CloseMessageWindow()

    #C0324
    ChrTalk(
        0x9,
        "#11P特别任务支援科的诸位，拜托了。\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    Sound(80, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0325
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "任务【调查古战场】\x07\x00",
            "开始！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x19B, 4)
    OP_29(0x91, 0x1, 0x0)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 2710, 0, -330, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_22_5333 end

    def Function_23_5B0B(): pass

    label("Function_23_5B0B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(3420, 1800, 80, 0)
    MoveCamera(44, 23, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25500, 0)
    SetChrPos(0x101, 2500, 0, -20, 90)
    SetChrPos(0x102, 2300, 0, -1020, 90)
    SetChrPos(0x103, 2300, 0, 980, 90)
    SetChrPos(0x104, 1000, 0, -20, 90)
    SetChrPos(0x109, 900, 0, 980, 90)
    SetChrPos(0x105, 900, 0, -1020, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_93(0x9, 0x10E, 0x0)
    OP_68(3420, 900, 80, 3000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x1)

    #C0326
    ChrTalk(
        0x101,
        (
            "#6P#00000F以上就是有关本次任务的报告。\x02\x03",

            "#00003F我想那些军犬应该不会\x01",
            "再危害人类了。\x02",
        )
    )

    CloseMessageWindow()

    #C0327
    ChrTalk(
        0x9,
        "#11P……是这样啊……\x02",
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x9)

    #C0328
    ChrTalk(
        0x101,
        "#6P#00012F请、请问……\x02",
    )

    CloseMessageWindow()

    #C0329
    ChrTalk(
        0x104,
        (
            "#6P#00305F嗯？道格拉斯老兄，\x01",
            "你怎么突然不出声了。\x02",
        )
    )

    CloseMessageWindow()

    #C0330
    ChrTalk(
        0x109,
        (
            "#10106F没有消灭那些军犬，\x01",
            "您还是觉得有些不放心吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0331
    ChrTalk(
        0x9,
        "#11P……不，你们做得很好。\x02",
    )

    CloseMessageWindow()

    #C0332
    ChrTalk(
        0x9,
        (
            "#11P因为成果超出我的想象，\x01",
            "所以不禁愣住了。\x02",
        )
    )

    CloseMessageWindow()

    #C0333
    ChrTalk(
        0x105,
        (
            "#6P#10300F嗯，这也是正常反应。\x02\x03",

            "#10309F毕竟像『说服军犬』这种事，\x01",
            "听起来简直就是荒谬至极。\x02",
        )
    )

    CloseMessageWindow()

    #C0334
    ChrTalk(
        0x102,
        (
            "#6P#00106F确、确实令人\x01",
            "难以相信。\x02",
        )
    )

    CloseMessageWindow()

    #C0335
    ChrTalk(
        0x103,
        (
            "#00200F但那是事实，\x01",
            "今后应该不会再有问题了。\x02",
        )
    )

    CloseMessageWindow()

    #C0336
    ChrTalk(
        0x9,
        "#11P……嗯，就这样吧。\x02",
    )

    CloseMessageWindow()

    #C0337
    ChrTalk(
        0x9,
        (
            "#11P能和平地解决问题，\x01",
            "真是再好不过了。\x02",
        )
    )

    CloseMessageWindow()

    #C0338
    ChrTalk(
        0x9,
        (
            "#11P辛苦你们了，支援科的各位。\x01",
            "多亏有你们相助，总算解决了\x01",
            "一个让人挂心的问题。\x02",
        )
    )

    CloseMessageWindow()

    #C0339
    ChrTalk(
        0x101,
        (
            "#6P#00004F那真是太好了。\x02\x03",

            "#00000F今后如果还有什么需要，\x01",
            "请随时联系我们。\x02",
        )
    )

    CloseMessageWindow()

    #C0340
    ChrTalk(
        0x9,
        "#11P好，我会的。\x02",
    )

    CloseMessageWindow()

    #C0341
    ChrTalk(
        0x9,
        (
            "#11P……那么，我们会继续\x01",
            "严加戒备。\x02",
        )
    )

    CloseMessageWindow()

    #C0342
    ChrTalk(
        0x9,
        "#11P你们也要保持警觉哦。\x02",
    )

    CloseMessageWindow()

    #C0343
    ChrTalk(
        0x101,
        "#6P#00000F……是！\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0344
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "任务【调查古战场】\x07\x00",
            "完成！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_29(0x91, 0x1, 0x2)
    OP_29(0x91, 0x1, 0x3)
    OP_29(0x91, 0x4, 0x10)
    OP_50(0x6A, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 2710, 0, -330, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_23_5B0B end

    SaveToFile()

Try(main)
