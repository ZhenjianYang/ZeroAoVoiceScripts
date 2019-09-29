from ScenarioHelper import *

def main():
    CreateScenaFile(
        "t2020.bin",                # FileName
        "t2020",                    # MapName
        "t2020",                    # Location
        0x0059,                     # MapIndex
        "ed7126",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x1C,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 89, 0, 2, 0, 3],
    )

    BuildStringList((
        "t2020",                  # 0
        "米蕾优准尉",             # 1
        "米蕾优三尉",             # 2
        "索妮亚司令",             # 3
        "士兵罗梅奥",             # 4
        "诺艾尔少尉",             # 5
        "道格拉斯副司令",         # 6
    ))

    AddCharChip((
        "chr/ch32600.itc",                   # 00
        "chr/ch05702.itc",                   # 01
        "chr/ch41400.itc",                   # 02
    ))

    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   0,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   0,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 0,   8,   255,  0)
    DeclNpc(-250,    0,       1409,    0,    389,  0x0, 0,   2,   0,   0,   1,   0,   9,   255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclActor(48900,   0,       -27260,  1200,    48900,   850,     -27260,  0x007C, 0,  4,  0x0000)
    DeclActor(-2000,   0,       -4520,   1200,    -2000,   1000,    -4520,   0x007C, 0,  14, 0x0000)
    DeclActor(-38750,  0,       0,       1200,    -40300,  1500,    0,       0x007E, 0,  7,  0x0000)

    ChipFrameInfo(496, 0)                                        # 0

    ScpFunction((
        "Function_0_1F0",          # 00, 0
        "Function_1_2A0",          # 01, 1
        "Function_2_301",          # 02, 2
        "Function_3_511",          # 03, 3
        "Function_4_629",          # 04, 4
        "Function_5_6D2",          # 05, 5
        "Function_6_B30",          # 06, 6
        "Function_7_133C",         # 07, 7
        "Function_8_1340",         # 08, 8
        "Function_9_1FCE",         # 09, 9
        "Function_10_2153",        # 0A, 10
        "Function_11_3315",        # 0B, 11
        "Function_12_3D42",        # 0C, 12
        "Function_13_4697",        # 0D, 13
        "Function_14_4B76",        # 0E, 14
    ))


    def Function_0_1F0(): pass

    label("Function_0_1F0")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_228"),
        (1, "loc_234"),
        (2, "loc_240"),
        (3, "loc_24C"),
        (4, "loc_258"),
        (5, "loc_264"),
        (6, "loc_270"),
        (SWITCH_DEFAULT, "loc_27C"),
    )


    label("loc_228")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_288")

    label("loc_234")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_288")

    label("loc_240")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_288")

    label("loc_24C")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_288")

    label("loc_258")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_288")

    label("loc_264")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_288")

    label("loc_270")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_288")

    label("loc_27C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_288")

    label("loc_288")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_29F")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_288")

    label("loc_29F")

    Return()

    # Function_0_1F0 end

    def Function_1_2A0(): pass

    label("Function_1_2A0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_300")
    OP_95(0xFE, -250, 0, 4390, 2000, 0x0)
    OP_95(0xFE, 19540, 0, 4390, 2000, 0x0)
    OP_95(0xFE, -250, 0, 4390, 2000, 0x0)
    OP_95(0xFE, -250, 0, -11650, 2000, 0x0)
    Jump("Function_1_2A0")

    label("loc_300")

    Return()

    # Function_1_2A0 end

    def Function_2_301(): pass

    label("Function_2_301")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_314")
    ClearChrFlags(0xB, 0x80)
    Jump("loc_4FE")

    label("loc_314")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_349")
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, -40300, 150, 0, 90)
    SetChrChipByIndex(0xA, 0x1)
    SetChrSubChip(0xA, 0x0)
    EndChrThread(0xA, 0x0)
    SetChrBattleFlags(0xA, 0x4)
    Jump("loc_4FE")

    label("loc_349")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_37E")
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, -40300, 150, 0, 90)
    SetChrChipByIndex(0xA, 0x1)
    SetChrSubChip(0xA, 0x0)
    EndChrThread(0xA, 0x0)
    SetChrBattleFlags(0xA, 0x4)
    Jump("loc_4FE")

    label("loc_37E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3B3")
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, -40300, 150, 0, 90)
    SetChrChipByIndex(0xA, 0x1)
    SetChrSubChip(0xA, 0x0)
    EndChrThread(0xA, 0x0)
    SetChrBattleFlags(0xA, 0x4)
    Jump("loc_4FE")

    label("loc_3B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3FE")
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, -1310, 0, 42250, 0)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, -40300, 150, 0, 90)
    SetChrChipByIndex(0xA, 0x1)
    SetChrSubChip(0xA, 0x0)
    EndChrThread(0xA, 0x0)
    SetChrBattleFlags(0xA, 0x4)
    Jump("loc_4FE")

    label("loc_3FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_449")
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, -1310, 0, 42250, 0)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, -40300, 150, 0, 90)
    SetChrChipByIndex(0xA, 0x1)
    SetChrSubChip(0xA, 0x0)
    EndChrThread(0xA, 0x0)
    SetChrBattleFlags(0xA, 0x4)
    Jump("loc_4FE")

    label("loc_449")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_494")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, -1310, 0, 42250, 0)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, -40300, 150, 0, 90)
    SetChrChipByIndex(0xA, 0x1)
    SetChrSubChip(0xA, 0x0)
    EndChrThread(0xA, 0x0)
    SetChrBattleFlags(0xA, 0x4)
    Jump("loc_4FE")

    label("loc_494")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_4B8")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, -36160, 0, 3980, 0)
    Jump("loc_4FE")

    label("loc_4B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_4FE")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, -1310, 0, 42250, 0)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, -40300, 150, 0, 90)
    SetChrChipByIndex(0xA, 0x1)
    SetChrSubChip(0xA, 0x0)
    EndChrThread(0xA, 0x0)
    SetChrBattleFlags(0xA, 0x4)

    label("loc_4FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_510")
    ClearScenarioFlags(0x22, 0)
    SetScenarioFlags(0x0, 0)
    Event(0, 10)

    label("loc_510")

    Return()

    # Function_2_301 end

    def Function_3_511(): pass

    label("Function_3_511")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_52B")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 0)
    Jump("loc_559")

    label("loc_52B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_547")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x97), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_559")

    label("loc_547")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 3)), scpexpr(EXPR_END)), "loc_559")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x236), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_559")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_578")
    OP_10(0xB, 0x0)
    OP_10(0xD, 0x1)
    OP_10(0xC, 0x0)
    OP_10(0xE, 0x1)
    Jump("loc_584")

    label("loc_578")

    OP_10(0xB, 0x1)
    OP_10(0xD, 0x0)
    OP_10(0xC, 0x1)
    OP_10(0xE, 0x0)

    label("loc_584")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5AA")
    SetMapObjFrame(0xFF, "hikari_add", 0x0, 0x1)
    Sound(128, 1, 50, 0)

    label("loc_5AA")

    SetMapObjFrame(0xFF, "cgf1", 0x1, 0x1)
    SetMapObjFrame(0xFF, "cda1", 0x0, 0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_5E8")
    SetMapObjFrame(0xFF, "cgf1", 0x0, 0x1)
    SetMapObjFrame(0xFF, "cda1", 0x1, 0x1)

    label("loc_5E8")

    OP_65(0x1, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_604")
    ClearMapObjFlags(0x2, 0x10)
    OP_66(0x1, 0x1)

    label("loc_604")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_616")
    OP_65(0x2, 0x1)
    Jump("loc_628")

    label("loc_616")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_628")
    OP_65(0x2, 0x1)

    label("loc_628")

    Return()

    # Function_3_511 end

    def Function_4_629(): pass

    label("Function_4_629")

    SetChrName("")

    #A0001
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "摆放着《家庭烹饪！汤品特辑》。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x2, 0x0)"), scpexpr(EXPR_END)), "loc_6CE")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B2(0xF)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6CE")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0002
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "『奶油浓汤』\x07\x00",
            "的食谱已经记下来了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_6CE")

    TalkEnd(0xFF)
    Return()

    # Function_4_629 end

    def Function_5_6D2(): pass

    label("Function_5_6D2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_754")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x149, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6F0")
    Call(0, 12)
    Jump("loc_74F")

    label("loc_6F0")


    #C0003
    ChrTalk(
        0xFE,
        (
            "#07900F索妮亚司令和道格拉斯副司令\x01",
            "正在商讨应对恐怖分子的措施。\x02\x03",

            "#07903F不要打扰到他们哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_74F")

    Jump("loc_B2C")

    label("loc_754")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_9FF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x149, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_76F")
    Call(0, 12)
    Jump("loc_9FA")

    label("loc_76F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_977")

    #C0004
    ChrTalk(
        0xFE,
        (
            "#07900F索妮亚司令今天在\x01",
            "疗养地米修拉姆\x01",
            "指挥现场的警备工作。\x02\x03",

            "#07903F由于各国要人都要\x01",
            "入住米修拉姆的迎宾馆，\x01",
            "所以那里已成为最重要的警备地点。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x104,
        (
            "#00305F也就是说，\x01",
            "你今天要代替索妮亚司令，\x01",
            "负责指挥贝尔加德门的这群家伙吗？\x02\x03",

            "#00306F唉，就凭你，\x01",
            "真的有能力担当\x01",
            "索妮亚司令的代理吗～？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x104, 500)

    #C0006
    ChrTalk(
        0xFE,
        (
            "#07901F真、真没礼貌……\x02\x03",

            "#07903F……哼，反正不需要你担心。\x01",
            "前司令还在的时候，\x01",
            "经常派我做这种事。\x02\x03",

            "#07907F在索妮亚司令不在的期间，\x01",
            "我一定会把这里管理好的！\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x104,
        "#00309F哈哈，看你这么有干劲，应该没问题了。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_9FA")

    label("loc_977")


    #C0008
    ChrTalk(
        0xFE,
        (
            "#07903F前司令还在的时候，\x01",
            "我时常被任命为代理，\x01",
            "负责这里的指挥工作。\x02\x03",

            "#07901F在索妮亚司令不在的期间，\x01",
            "我一定会把这里管理好的！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9FA")

    Jump("loc_B2C")

    label("loc_9FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_B2C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x149, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A1A")
    Call(0, 12)
    Jump("loc_B2C")

    label("loc_A1A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AC2")

    #C0009
    ChrTalk(
        0xFE,
        (
            "#07904F好、好了，\x01",
            "先不说我升职的事情了……\x02\x03",

            "#07900F为了应对通商会议，\x01",
            "边境大门的警备力度加强了不少。\x02\x03",

            "你们一定要注意，\x01",
            "可别和旅客们\x01",
            "发生冲突哦。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_B2C")

    label("loc_AC2")


    #C0010
    ChrTalk(
        0xFE,
        (
            "#07900F为了应对通商会议，\x01",
            "边境大门的警备力度加强了不少。\x02\x03",

            "你们一定要注意，\x01",
            "可别和旅客们\x01",
            "发生冲突哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B2C")

    TalkEnd(0xFE)
    Return()

    # Function_5_6D2 end

    def Function_6_B30(): pass

    label("Function_6_B30")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_B41")
    Jump("loc_1338")

    label("loc_B41")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_B4F")
    Jump("loc_1338")

    label("loc_B4F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_B5D")
    Jump("loc_1338")

    label("loc_B5D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_DEA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D8B")

    #C0011
    ChrTalk(
        0xFE,
        (
            "#07900F哦，对了……\x02\x03",

            "你们在来贝尔加德门的路上，\x01",
            "有没有遇到什么危险？\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x101,
        "#00005F什么……？\x02",
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x104,
        (
            "#00305F没有啊，和平时一样，\x01",
            "并没什么异常状况。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0xFE,
        (
            "#07900F是吗……\x02\x03",

            "#07903F……看来今天\x01",
            "不会出现了。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0015
    ChrTalk(
        0xFE,
        (
            "#07900F哦，你们不用在意，\x01",
            "只是一件应由我们负责的工作。\x02\x03",

            "#07903F不过，我也许会在\x01",
            "近期内和你们\x01",
            "商量一下这件事……\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x104,
        (
            "#00303F唔，虽然还不知是什么事……\x01",
            "但只要有需要，就尽管找我们吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0xFE,
        "#07902F好的，到时候就要麻烦大家了。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_DE5")

    label("loc_D8B")


    #C0018
    ChrTalk(
        0xFE,
        (
            "#07903F……看来今天\x01",
            "不会出现了。\x02\x03",

            "#07901F现在必须要全力应对\x01",
            "与两大国之间的紧张关系。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DE5")

    Jump("loc_1338")

    label("loc_DEA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1338")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16A, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1072")

    #C0019
    ChrTalk(
        0x104,
        (
            "#00309F哟，米蕾优准尉阁下，\x01",
            "最近还好吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x104, 500)

    #C0020
    ChrTalk(
        0xFE,
        (
            "#07901F……你是故意\x01",
            "叫错的吧？\x02\x03",

            "#07906F前段时间不是刚告诉过你，\x01",
            "我已经升为三尉了吗……\x01",
            "真是的。\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x109,
        (
            "#10109F哈哈……总之，\x01",
            "恭喜你升职。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x109, 500)

    #C0022
    ChrTalk(
        0xFE,
        (
            "#07909F呵呵，谢谢了，上士。\x02\x03",

            "#07903F升职自然可喜可贺……\x01",
            "但我需要承担的责任\x01",
            "也将随之加重。\x02\x03",

            "#07901F今后一定要继续努力，\x01",
            "进一步地提高自己才行。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x104,
        (
            "#00306F哎呀呀，你还是老样子，\x01",
            "总是这么一本正经的。\x02\x03",

            "#00302F太过拼命会累坏身体的，\x01",
            "差不多也就行了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x104, 500)
    OP_63(0xFE, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0024
    ChrTalk(
        0xFE,
        (
            "#07901F人家难得有机会\x01",
            "说几句漂亮话……\x01",
            "你、你可真是的，蠢兰迪！\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x109,
        (
            "#10112F啊、啊哈哈……\x01",
            "（升职之后也还是老样子呢……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x16A, 4)
    OP_93(0xFE, 0xB4, 0x0)
    Jump("loc_1338")

    label("loc_1072")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16A, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12B9")

    #C0026
    ChrTalk(
        0x104,
        (
            "#00300F哦，对了……\x01",
            "有没有戴上我送你的\x01",
            "那件贺礼？\x02\x03",

            "就是在米修拉姆的珠宝店\x01",
            "买的那个东西。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15A, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1111")

    #C0027
    ChrTalk(
        0x101,
        (
            "#00005F咦……\x01",
            "原来你还送了礼物啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1141")

    label("loc_1111")


    #C0028
    ChrTalk(
        0x101,
        (
            "#00002F哦……说起来，\x01",
            "你当时买了枚胸针呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1141")

    TurnDirection(0xFE, 0x104, 500)

    #C0029
    ChrTalk(
        0xFE,
        (
            "#07906F喂……\x01",
            "怎么可能戴出来。\x02\x03",

            "#07900F身为警备队的士官，\x01",
            "不能佩戴那种花哨的东西，\x01",
            "我把它小心翼翼地珍藏在了……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_63(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xFE)

    #C0030
    ChrTalk(
        0xFE,
        (
            "#07911F不、不对……你别误会啊！\x01",
            "我才不在乎那东西呢！\x02\x03",

            "#07909F想、想起来了！我随手就把它\x01",
            "扔进柜子的角落里了……！\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x104,
        "#00309F哈哈哈，别害羞啦。\x02",
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x103,
        "#00204F（……他们两个真有趣。）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x16A, 5)
    OP_93(0xFE, 0xB4, 0x0)
    Jump("loc_1338")

    label("loc_12B9")


    #C0033
    ChrTalk(
        0xFE,
        (
            "#07902F咳、咳咳，总之……\x01",
            "既然我升职了，\x01",
            "就必须要比以往更加努力。\x02\x03",

            "#07903F为了能帮上司令的忙，\x01",
            "我一定要让自己更上一层楼！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1338")

    TalkEnd(0xFE)
    Return()

    # Function_6_B30 end

    def Function_7_133C(): pass

    label("Function_7_133C")

    Call(0, 8)
    Return()

    # Function_7_133C end

    def Function_8_1340(): pass

    label("Function_8_1340")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1886")
    OP_52(0x109, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xA, 0x10)
    TurnDirection(0xA, 0x109, 0)
    OP_52(0xA, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_13DD")
    Jump("loc_1427")

    label("loc_13DD")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_13FD")
    OP_52(0xA, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1427")

    label("loc_13FD")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_141D")
    OP_52(0xA, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1427")

    label("loc_141D")

    OP_52(0xA, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1427")

    OP_52(0xA, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x109, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x109, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xA, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17CA")

    #C0034
    ChrTalk(
        0xA,
        "#02008F……………………………………\x02",
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x101,
        (
            "#00001F索妮亚司令……\x01",
            "您有什么烦心事吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0xA,
        (
            "#02003F……警备队的重组问题让我有些头疼。\x02\x03",

            "#02000F在玛因兹山道一战中遭受重创之后，\x01",
            "要想重新振作，恢复原状，\x01",
            "恐怕还需花上一段时间。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x102,
        "#00108F果然如此啊……\x02",
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x109,
        "#10108F…………………………\x02",
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0xA,
        (
            "#02000F……诺艾尔上士，\x01",
            "你的表情很沉重啊。\x02\x03",

            "#02003F开始对回归警备队的决定\x01",
            "感到后悔了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x109,
        (
            "#10103F……不，我并没有后悔。\x02\x03",

            "#10108F只是支援科也很繁忙，\x01",
            "我在这种时候抽身离去，\x01",
            "心中总觉得有些愧疚……\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x101,
        "#00003F诺艾尔……\x02",
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0xA,
        (
            "#02003F……警备队的重组计划\x01",
            "很需要你的力量……\x02\x03",

            "#02000F但既然如此，你还是不要回来了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x109,
        (
            "#10103F不……\x01",
            "既然已经决定了，就不能反悔。\x02\x03",

            "#10101F诺艾尔·希卡在支援科\x01",
            "完成今天一天的工作之后，\x01",
            "就会回归警备队！\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0xA,
        (
            "#02004F很好。\x02\x03",

            "#02000F但你现在仍然是\x01",
            "外派至支援科的成员。\x02\x03",

            "把剩下的工作全部处理好吧，\x01",
            "别给自己留下遗憾。\x01",
            "……听清楚了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x109,
        "#10100F是！我明白了！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_187C")

    label("loc_17CA")


    #C0046
    ChrTalk(
        0xA,
        (
            "#02000F诺艾尔，警备队的重组计划\x01",
            "很需要你的力量。\x02\x03",

            "#02004F今天一天，你要努力把支援科的\x01",
            "工作处理完毕，别给自己留下遗憾。\x01",
            "在那之后，再回到警备队吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x109,
        "#10100F是！我明白了！\x02",
    )

    CloseMessageWindow()

    label("loc_187C")

    ClearChrFlags(0xA, 0x10)
    Jump("loc_1FCA")

    label("loc_1886")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1B39")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16B, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1AB4")

    #C0048
    ChrTalk(
        0xA,
        (
            "#02002F罗伊德，\x01",
            "昨天你真是立了个大功呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x101,
        "#00005F什么……\x02",
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x102,
        (
            "#00100F您是指昨天在事故现场的\x01",
            "调查吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0xA,
        (
            "#02003F……如果当时按照我的命令立刻\x01",
            "抢修铁道的话，脱轨事故的真相\x01",
            "恐怕就再也无法查明了。\x02\x03",

            "#02008F我竟然差点就亲手破坏了\x01",
            "追寻真相的证据……\x01",
            "真是太过急躁了。\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x103,
        (
            "#00203F站在警备队的立场上，\x01",
            "那也是可以理解的……\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x104,
        (
            "#00300F是啊，而且在那之后，\x01",
            "抢修工作的进展不是很快嘛。\x02\x03",

            "#00302F您并不需要为此\x01",
            "而消沉吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x109,
        "#10100F是、是呀！\x02",
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0xA,
        (
            "#02004F……呵呵，听你们这样一说，\x01",
            "我心里真是轻松多了。\x02\x03",

            "#02002F再次向大家表示感谢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x16B, 0)
    Jump("loc_1B34")

    label("loc_1AB4")


    #C0056
    ChrTalk(
        0xA,
        (
            "#02004F总之，托你们的福，\x01",
            "脱轨事故的原因已经查明了。\x02\x03",

            "#02002F虽然大型魔兽的存在很令人担心……\x01",
            "但那方面的事情就交给我们吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B34")

    Jump("loc_1FCA")

    label("loc_1B39")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1D70")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16A, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CE4")

    #C0057
    ChrTalk(
        0xA,
        (
            "#02000F我已经看过你们的\x01",
            "调查报告书了。\x02\x03",

            "#02003F『灵智之草』……\x01",
            "曾在教团事件中出现过的名字\x01",
            "竟然再次出现了。\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x101,
        (
            "#00003F是啊……\x01",
            "我们也非常吃惊。\x02\x03",

            "#00001F今后的调查工作\x01",
            "要如何开展呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0xA,
        (
            "#02003F这个嘛，\x01",
            "警备队目前\x01",
            "仍然无法出动……\x02\x03",

            "#02000F各位查明了『幻兽』出现的原因，\x01",
            "单是这一点，\x01",
            "就已经算是很大的进展了。\x02\x03",

            "接下来，就请你们\x01",
            "继续在条件允许的\x01",
            "范围内展开调查吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x104,
        "#00302F好的，交给我们吧。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x16A, 7)
    Jump("loc_1D6B")

    label("loc_1CE4")


    #C0061
    ChrTalk(
        0xA,
        (
            "#02000F各位查明了『幻兽』出现的原因，\x01",
            "单是这一点，\x01",
            "就已经算是很大的进展了。\x02\x03",

            "接下来，就请你们\x01",
            "继续在条件允许的\x01",
            "范围内展开调查吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D6B")

    Jump("loc_1FCA")

    label("loc_1D70")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1F06")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E88")

    #C0062
    ChrTalk(
        0xA,
        (
            "#02001F竟然出现了不可思议的『幻兽』……\x01",
            "对克洛斯贝尔自治州来说，\x01",
            "这是绝对不容忽视的问题。\x02\x03",

            "#02003F不过，我们警备队\x01",
            "必须要集中精力，专心应对\x01",
            "边境地带的紧张局势……\x02\x03",

            "#02000F所以幻兽出现的原因，\x01",
            "就拜托你们去调查了。\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x101,
        "#00000F好的，尽管交给我们吧。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1F01")

    label("loc_1E88")


    #C0064
    ChrTalk(
        0xA,
        (
            "#02003F我们警备队必须要\x01",
            "集中精力，专心应对\x01",
            "边境地带的紧张局势……\x02\x03",

            "#02000F所以幻兽出现的原因，\x01",
            "就拜托你们去调查了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F01")

    Jump("loc_1FCA")

    label("loc_1F06")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1F14")
    Jump("loc_1FCA")

    label("loc_1F14")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1F22")
    Jump("loc_1FCA")

    label("loc_1F22")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1FCA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x149, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F3D")
    Call(0, 11)
    Jump("loc_1FCA")

    label("loc_1F3D")


    #C0065
    ChrTalk(
        0xA,
        (
            "#02003F在通商会议的警备工作中，\x01",
            "猎兵团『赤色星座』绝对是个\x01",
            "必须要注意的危险团体。\x02\x03",

            "#02000F如果有什么新消息，\x01",
            "请一定要和我们警备队联络。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1FCA")

    TalkEnd(0xA)
    Return()

    # Function_8_1340 end

    def Function_9_1FCE(): pass

    label("Function_9_1FCE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_214F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_20D7")

    #C0066
    ChrTalk(
        0xB,
        (
            "无论是接受了国防军\x01",
            "体制的司令，还是投身\x01",
            "反抗运动的米蕾优三尉等人……\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0xB,
        (
            "他们都是在经过用心思考之后，\x01",
            "选择了各自的道路。\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0xB,
        (
            "但大多数队员却只对警备队\x01",
            "成为国防军这件事兴奋不已，\x01",
            "就此随波逐流。\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0xB,
        "……唉，自己都有些瞧不起自己。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_214F")

    label("loc_20D7")


    #C0070
    ChrTalk(
        0xB,
        (
            "索妮亚司令也好，米蕾优三尉等人也好，\x01",
            "他们都是在经过反复考虑之后，\x01",
            "选择了各自的道路。\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0xB,
        "……我们也必须要努力啊。\x02",
    )

    CloseMessageWindow()

    label("loc_214F")

    TalkEnd(0xFE)
    Return()

    # Function_9_1FCE end

    def Function_10_2153(): pass

    label("Function_10_2153")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch03900.itc", 0x1E)
    LoadChrToIndex("chr/ch12202.itc", 0x1F)
    LoadChrToIndex("apl/ch51533.itc", 0x20)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x101, -36600, 0, 0, 270)
    SetChrPos(0x106, -35830, 0, 870, 270)
    SetChrPos(0x103, -35240, 0, -680, 270)
    SetChrPos(0x104, -35430, 0, -1680, 270)
    SetChrPos(0x107, -34080, 0, 1450, 270)
    SetChrPos(0x105, -34350, 0, -80, 270)
    SetChrSubChip(0x107, 0x5)
    ClearChrFlags(0xC, 0x80)
    SetChrChipByIndex(0xC, 0x1E)
    SetChrSubChip(0xC, 0x0)
    SetChrFlags(0xC, 0x8000)
    SetChrPos(0xC, -40000, 0, 2000, 90)
    ClearChrFlags(0xA, 0x80)
    SetChrChipByIndex(0xA, 0x1F)
    SetChrSubChip(0xA, 0x0)
    SetChrFlags(0xA, 0x8000)
    SetChrPos(0xA, -40150, 100, 0, 90)
    SetChrName("")

    #A0072
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "之后，罗伊德等人\x01",
            "被悄悄带到了司令室……\x02\x03",

            "大家将至今为止的事情经过，\x01",
            "以及『零之至宝』的来历\x01",
            "全部告知给了司令。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    PlayBGM("ed7566", 0)
    OP_68(-40000, 1100, 1000, 0)
    MoveCamera(320, 18, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25500, 0)
    FadeToBright(1000, 0)
    OP_68(-38000, 1100, 1000, 4000)
    OP_6F(0x79)
    OP_0D()

    #C0073
    ChrTalk(
        0xC,
        "#10206F#5P竟、竟然有这种事……\x02",
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0xA,
        (
            "#10603F#5P……原来如此。\x02\x03",

            "#10601F我终于明白总统一派为何要做出\x01",
            "那些令人难以理解的举动了。\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0x104,
        "#00305F#12P言下之意……\x02",
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x101,
        (
            "#00002F#12P……莫非您愿意对我们\x01",
            "提供一定程度的协助吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0xA,
        (
            "#10603F#5P很遗憾，这是不可能的。\x02\x03",

            "无论我们是警备队还是国防军，\x01",
            "『为国效力』的原则都不会改变。\x02\x03",

            "#10608F虽然还存在着不少问题，\x01",
            "但『克洛斯贝尔独立国』已经正式建立。\x01",
            "只要总统还是国家元首……\x02\x03",

            "#10601F我们军人就绝不能擅自做出判断，\x01",
            "并为此行使武力。\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0x101,
        "#00006F#12P……这样啊。\x02",
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0xC,
        "#10208F#5P………………………………\x02",
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0x104,
        (
            "#00306F#12P唉，正规军在这方面\x01",
            "实在是太严格了。\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0x105,
        (
            "#10401F#12P也就是说，我们之间\x01",
            "完全没有妥协退让的余地啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0xA,
        (
            "#10603F#5P嗯，正是。\x02\x03",

            "#10608F另外，亚里欧斯国防长官的\x01",
            "指挥能力非常优秀。\x02\x03",

            "就算贝尔加德门的部队\x01",
            "决定协助你们……\x02\x03",

            "#10601F他也会率领主力部队，\x01",
            "以『讨伐叛乱军』的名义\x01",
            "将我们瞬间镇压。\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x103,
        "#00201F#12P是吗……\x02",
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x104,
        (
            "#00301F#12P没想到那个大叔\x01",
            "还是个优秀的指挥官。\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0xA,
        (
            "#10606F#5P嗯，虽说他当年只是赛尔盖的部下，\x01",
            "但毕竟是被称为『剑圣』的人物，\x01",
            "似乎已经达到了『理』之境界。\x02\x03",

            "#10601F他那巧妙的战略……\x01",
            "与他的师兄──利贝尔王国军司令\x01",
            "卡西乌斯准将有不少异曲同工之处。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xC, 0xB4, 0x1F4)

    #C0086
    ChrTalk(
        0xC,
        (
            "#10206F#11P可、可是……！\x02\x03",

            "#10201F就算对手是亚里欧斯长官，\x01",
            "只要我们能和唐古拉姆门的道格拉斯\x01",
            "副司令齐心协力，说不定也可以……！\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xA, 0x1)

    #C0087
    ChrTalk(
        0xA,
        (
            "#10605F#5P哎呀，诺艾尔。\x02\x03",

            "#10604F你为何要以\x01",
            "协助他们为前提呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0xC,
        "#10208F#11P……啊………\x02",
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0x103,
        "#00202F#12P诺艾尔小姐……\x02",
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x105,
        (
            "#10409F#12P哈哈，看来刚才那场\x01",
            "一对一的决斗起到了作用啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    #C0091
    ChrTalk(
        0x101,
        (
            "#00003F#12P索妮亚司令。\x02\x03",

            "#00008F假如迪塔总统以及\x01",
            "克洛斯贝尔独立国的『正当性』\x01",
            "出现了问题……\x02\x03",

            "#00001F国防军将会采取怎样的应对措施？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x106, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xA, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0xA, 0x0)
    OP_93(0xC, 0x5A, 0x1F4)

    #C0092
    ChrTalk(
        0xC,
        "#10205F#5P哎……\x02",
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x106,
        "#10712F#12P你是指……\x02",
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0xA,
        (
            "#10604F#5P呵呵，这个嘛……\x02\x03",

            "恐怕还要视具体情况而定。\x01",
            "不过，在判明事情的真伪之前，\x01",
            "我们会『慎重地观望情况发展』……\x02\x03",

            "#10602F我认为这就是正确的做法。\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0xC,
        "#10202F#5P……！\x02",
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0x105,
        (
            "#10404F#12P呵呵，原来如此。\x02\x03",

            "#10402F也就是说，如何让他们的\x01",
            "『正当性』出现问题，\x01",
            "就是目前的关键了。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x5A, 0x1F4)

    #C0097
    ChrTalk(
        0x101,
        (
            "#00004F#5P是啊……\x02\x03",

            "像这种事情，交给艾莉来判断\x01",
            "才是最可靠的……\x02\x03",

            "#00000F但依我看，关键应该就在于\x01",
            "麦克道尔议长。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2B98():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_2B98)
    Sleep(50)

    def lambda_2BA8():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_2BA8)
    Sleep(50)

    def lambda_2BB8():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_2BB8)
    Sleep(50)

    def lambda_2BC8():
        TurnDirection(0x106, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_2BC8)
    Sleep(50)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x106, 0)

    #C0098
    ChrTalk(
        0x103,
        "#00205F#12P啊……\x02",
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0x104,
        "#00300F#6P大小姐的外公吗……\x02",
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0x106,
        (
            "#10702F#12P他应该是克洛斯贝尔\x01",
            "自治州的代表之一吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0x101,
        (
            "#00006F#5P嗯，另一个代表\x01",
            "正是迪塔市长。\x02\x03",

            "#00008F听说在发表独立宣言的时候，\x01",
            "麦克道尔议长的意见\x01",
            "完全被封锁了。\x02\x03",

            "#00013F如果他的意见能通过某些方式\x01",
            "向国内外发表……\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x103,
        (
            "#00203F#12P总统和独立国的正当性\x01",
            "也许会产生动摇……\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0xC,
        "#10201F#5P如此一来，国防军也就……！\x02",
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0xA,
        (
            "#10602F#5P呵呵……\x01",
            "你注意到了关键问题呢。\x02\x03",

            "#10604F看来也不需要我\x01",
            "给你什么提示了。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2DB8():
        OP_93(0x101, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2DB8)
    Sleep(50)

    def lambda_2DC8():
        OP_93(0x103, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_2DC8)
    Sleep(50)

    def lambda_2DD8():
        OP_93(0x104, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_2DD8)
    Sleep(50)

    def lambda_2DE8():
        OP_93(0x105, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_2DE8)
    Sleep(50)

    def lambda_2DF8():
        OP_93(0x106, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_2DF8)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x106, 0)
    SetChrSubChip(0xA, 0x1)
    Sleep(300)

    #C0105
    ChrTalk(
        0xA,
        (
            "#10603F#5P诺艾尔少尉。\x02\x03",

            "#10601F麦克道尔前议长\x01",
            "好像在米修拉姆吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xC, 0xB4, 0x1F4)

    #C0106
    ChrTalk(
        0xC,
        (
            "#10211F#11P哎……啊，是的！\x02\x03",

            "#10203F他和外孙女艾莉小姐\x01",
            "都被软禁在迎宾馆内！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0107
    ChrTalk(
        0xA,
        (
            "#10608F#5P嗯，我记得米修拉姆的警备\x01",
            "是由『赤色星座』的部队负责的……\x02\x03",

            "#10601F国防军的部队应该\x01",
            "没有驻扎在那里吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0xC,
        "#10201F#11P是的，正如您所说。\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0x10E, 0x1F4)

    #C0109
    ChrTalk(
        0x101,
        "#00002F#12P索妮亚司令……\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xA, 0x0)
    Sleep(100)

    #C0110
    ChrTalk(
        0xA,
        (
            "#10605F#5P哎呀，我可真是的，\x01",
            "一不留神在外人面前说起这种事……\x02\x03",

            "#10604F请大家立刻忘记\x01",
            "我刚才说的话吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0x103,
        "#00209F#12P呵呵……\x02",
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0x104,
        (
            "#00309F#12P哈哈……\x01",
            "真不愧是索妮亚司令。\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0x105,
        (
            "#10402F#12P这种装傻行为\x01",
            "真是让人赞叹。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xA, 0x1)
    Sleep(200)

    #C0114
    ChrTalk(
        0xA,
        (
            "#10603F#5P还有，诺艾尔少尉。\x02\x03",

            "#10601F在之前那场一对一的决斗中，\x01",
            "对方用『天真』来评价你，说的完全没错。\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0xC,
        "#10206F#11P……是。\x02",
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0xA,
        (
            "#10603F#5P因此，你本该接受\x01",
            "期限不定的禁闭处分。\x02\x03",

            "#10602F作为代替，我决定将你再次外派到\x01",
            "克洛斯贝尔警察局的特别任务支援科。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0117
    ChrTalk(
        0xC,
        "#10202F#11P啊……\x02",
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0xA,
        (
            "#10604F#5P好好想想，你自身还有什么不足之处……\x02\x03",

            "还有，为了克洛斯贝尔的未来，\x01",
            "你又该做些什么。\x02\x03",

            "#10602F先去把这些事情想清楚吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    SetCameraDistance(25200, 0)
    Sound(802, 0, 100, 0)
    SetChrChipByIndex(0xC, 0x20)
    SetChrSubChip(0xC, 0x0)
    OP_0D()
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0119
    ChrTalk(
        0xC,
        "#10212F#11P遵命！\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    SetCameraDistance(25000, 1000)
    OP_6F(0x79)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    SetScenarioFlags(0x22, 6)
    NewScene("e3020", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_10_2153 end

    def Function_11_3315(): pass

    label("Function_11_3315")

    EventBegin(0x0)
    Fade(500)
    OP_68(-38900, 900, 260, 0)
    MoveCamera(314, 22, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25180, 0)
    SetChrPos(0x101, -37250, 0, 0, 270)
    SetChrPos(0x102, -37250, 0, 980, 270)
    SetChrPos(0x109, -37250, 0, -1020, 270)
    SetChrPos(0x104, -36050, 0, -720, 270)
    SetChrPos(0x105, -35700, 0, 680, 270)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrSubChip(0xA, 0x0)
    OP_0D()

    #C0120
    ChrTalk(
        0x109,
        "#12P#10100F您辛苦了，索妮亚司令！\x02",
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0xA,
        (
            "#5P#02000F你也辛苦了，诺艾尔上士。\x02\x03",

            "#02004F听说你在特别任务支援科\x01",
            "工作得非常努力呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0x109,
        "#12P#10104F是的，我在支援科学到了很多东西……\x02",
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0x105,
        (
            "#12P#10300F原来如此，这位就是警备队的司令\x01",
            "索妮亚·贝尔茨阁下啊。\x02\x03",

            "#10302F管理着整个警备队的优秀司令官……\x01",
            "呵呵，真是个女中豪杰。\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0x101,
        (
            "#00004F嗯，我们一直都\x01",
            "蒙受她的关照。\x02\x03",

            "#00000F好久不见了，司令。\x01",
            "还有……虽然现在说这个有点晚，\x01",
            "但还是恭喜您升职了。\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0xA,
        (
            "#5P#02002F呵呵，谢谢。\x01",
            "话说回来，确实很久没见了。\x02\x03",

            "#02002F我最近在处理通商会议的\x01",
            "警备安排，一直没有和你们\x01",
            "会面的机会……\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0x102,
        (
            "#00100F您果然很\x01",
            "繁忙啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0xA,
        (
            "#5P#02000F是啊，最近这几天，\x01",
            "一直都在带队检查\x01",
            "警备区域的周边情况。\x02\x03",

            "#02003F为了避免意外事态的发生，\x01",
            "必须要小心慎重地\x01",
            "完成准备工作。\x02",
        )
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0x104,
        (
            "#12P#00306F嗯，毕竟各国要人\x01",
            "明天就要来了，\x01",
            "这也是理所当然的。\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0x101,
        (
            "#00003F真抱歉，司令，\x01",
            "在您如此忙碌的时候，\x01",
            "我们还来打扰您……\x02",
        )
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0xA,
        (
            "#5P#02003F不，你们来的正是时候。\x02\x03",

            "#02001F我正好有件事\x01",
            "必须要告诉你们。\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0x109,
        "#12P#10105F哎……？\x02",
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0xA,
        (
            "#5P#02003F数日前，有一群人\x01",
            "曾来访贝尔加德门。\x02\x03",

            "#02001F那群人是『赤色星座』……\x01",
            "被称作塞姆里亚大陆西部\x01",
            "最强的猎兵团。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0133
    ChrTalk(
        0x101,
        "#00011F什么……！？\x02",
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0x102,
        "#00101F他们竟然来到这种地方……！？\x02",
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0xA,
        (
            "#5P#02000F兰迪，\x01",
            "我记得赤色星座和你\x01",
            "有很深的渊源。\x02\x03",

            "#02003F所以我认为应该把这条目击情报\x01",
            "直接传达给你们。\x02",
        )
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0x104,
        "#12P#00301F……他们在这里做了什么？\x02",
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0xA,
        (
            "#5P#02000F据目击到他们的警备队员说，\x01",
            "他们并没有做过什么\x01",
            "惹人注目的行为。\x02\x03",

            "#02003F到达大门之后，\x01",
            "他们在食堂休息了一段时间……\x02\x03",

            "#02000F之后迎接了来自帝国的商人，\x01",
            "一起离开了。\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0x105,
        (
            "#12P#10304F唔，迎接帝国的商人啊。\x02\x03",

            "#10302F看来是和『深红商会』\x01",
            "有着某些往来的\x01",
            "商人吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0x102,
        (
            "#00100F嗯，听说那个商会是赤色星座\x01",
            "用来周转资金的空头公司……\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0x109,
        (
            "#12P#10106F看来很有可能……\x01",
            "但、但他们的胆子未免也太大了。\x02\x03",

            "#10101F竟然主动跑到维持治安的组织──\x01",
            "警备队的眼皮底下……而且这里的部队\x01",
            "还是驻守在与帝国接壤处的精锐部队。\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0x101,
        (
            "#00003F……因为他们还没有\x01",
            "在克洛斯贝尔引发事端。\x02\x03",

            "#00001F目前也没有证据能表明之前发生在\x01",
            "旧矿山的那件事与他们有关，\x01",
            "所以没必要偷偷摸摸……\x02",
        )
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0x104,
        (
            "#12P#00303F……要是没有那么厚的脸皮，\x01",
            "又怎么好意思公然经营高级俱乐部。\x02\x03",

            "#00300F索妮亚司令，多谢您提供情报。\x02",
        )
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0xA,
        (
            "#5P#02003F……不必客气。\x02\x03",

            "#02001F在通商会议的警备工作中，\x01",
            "猎兵团『赤色星座』绝对是个\x01",
            "必须要注意的危险团体。\x02\x03",

            "如果有什么新消息，\x01",
            "请一定要和我们警备队联络。\x02",
        )
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0x101,
        (
            "#00001F……明白了，\x01",
            "我们也会多加留意的。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetScenarioFlags(0x149, 5)
    OP_29(0xA3, 0x1, 0x2)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, -37250, 0, 0, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_11_3315 end

    def Function_12_3D42(): pass

    label("Function_12_3D42")

    EventBegin(0x0)
    Fade(500)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x68), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3EAD")
    OP_68(-1550, 910, 41080, 0)
    MoveCamera(315, 25, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25500, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3E14")
    SetChrPos(0x101, -1850, 10, 40450, 0)
    SetChrPos(0x104, -590, 10, 40320, 0)
    SetChrPos(0x102, -2060, 10, 39240, 0)
    SetChrPos(0x103, -720, 10, 39190, 0)
    SetChrPos(0x109, -2140, 10, 38080, 0)
    SetChrPos(0x105, -540, 10, 37980, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    Jump("loc_3EA1")

    label("loc_3E14")

    OP_68(-1940, 910, 41470, 0)
    MoveCamera(315, 25, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25500, 0)
    SetChrPos(0x101, -1850, 10, 40450, 0)
    SetChrPos(0x104, -590, 10, 40320, 0)
    SetChrPos(0x102, -2060, 10, 39240, 0)
    SetChrPos(0x109, -720, 10, 39190, 0)
    SetChrPos(0x105, -1740, 10, 38080, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    label("loc_3EA1")

    OP_93(0x8, 0xB4, 0x0)
    Jump("loc_3F4F")

    label("loc_3EAD")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6A), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3F4F")
    OP_68(-37130, 700, 3380, 0)
    MoveCamera(313, 25, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25500, 0)
    SetChrPos(0x101, -36980, 0, 2200, 0)
    SetChrPos(0x104, -35490, 0, 2200, 0)
    SetChrPos(0x102, -36980, 0, 1200, 0)
    SetChrPos(0x109, -35490, 0, 1200, 0)
    SetChrPos(0x105, -36250, 0, 600, 0)
    OP_93(0x8, 0xB4, 0x0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    label("loc_3F4F")

    OP_4B(0x8, 0xFF)
    OP_0D()

    #C0145
    ChrTalk(
        0x8,
        (
            "#07902F啊，支援科的各位，\x01",
            "好久不见了。\x02\x03",

            "#07909F还有，站在那边的蠢货──\x02\x03",

            "#07903F……咳咳，\x01",
            "兰迪，你最近还好吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4021")
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_4021")

    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0146
    ChrTalk(
        0x104,
        (
            "#6P#00304F呵呵，米蕾优，\x01",
            "虽然你这么说我……\x01",
            "但我明白你的心情哦。\x02\x03",

            "#00302F我回到了支援科之后，\x01",
            "你肯定觉得寂寞难耐吧？\x02\x03",

            "#00309F『不要离开我！兰迪！\x01",
            "  求你永远和我在一起！（拟声）』\x01",
            "……毕竟你当时还说过这种话～\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x8)

    #C0147
    ChrTalk(
        0x8,
        (
            "#07907F我、我什么时候说过那种话了！？\x01",
            "……大、大白痴兰迪！\x02",
        )
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0x109,
        (
            "#6P#10100F（呵呵……\x01",
            "  他们的关系还是这么好啊。）\x02",
        )
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0x101,
        (
            "#00000F哈哈……米蕾优准尉，\x01",
            "看来你很有精神，真是太好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0x102,
        (
            "#00100F对了，\x01",
            "听说你升职了。\x01",
            "呵呵，恭喜恭喜。\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0x8,
        (
            "#07902F咳、咳咳，那个……\x01",
            "老实说，我觉得自己受之有愧。\x02\x03",

            "#07908F在教团事件暴发的时候，\x01",
            "我曾犯下过带头向ＩＢＣ\x01",
            "发动袭击这样的重大过错……\x02",
        )
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0x105,
        (
            "#6P#10300F但我听说你当时误服了奇怪的药物，\x01",
            "意识完全被他人操控了，\x01",
            "所以并没必要如此在意吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0x8,
        (
            "#07903F……嗯，\x01",
            "我也明白，\x01",
            "但还是无法原谅自己……\x02",
        )
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0x104,
        (
            "#6P#00306F哎呀呀，你完全没变，\x01",
            "还是这么死脑筋。\x02\x03",

            "#00300F你这次能够升职，是因为你在之前那个\x01",
            "蠢货司令的手下，依然能做出最妥善的指挥。\x01",
            "所以，受到提拔是很合理的结果。\x02\x03",

            "#00302F坦然接受，\x01",
            "才是对司令的最好回报哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_447F")
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)

    label("loc_447F")

    OP_63(0x109, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_64(0x102)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_44D1")
    OP_64(0x103)

    label("loc_44D1")

    OP_64(0x109)
    OP_64(0x105)
    OP_64(0x8)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4524")

    #C0155
    ChrTalk(
        0x103,
        (
            "#6P#00205F兰迪前辈竟然发表了\x01",
            "如此正经的意见……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4554")

    label("loc_4524")


    #C0156
    ChrTalk(
        0x101,
        (
            "#00006F这……\x01",
            "你竟然能发表如此正经的意见。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4554")


    #C0157
    ChrTalk(
        0x104,
        (
            "#6P#00309F哈哈，我不是一直\x01",
            "都很正经嘛。\x02",
        )
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0x8,
        (
            "#07902F……嗯，说的也对，\x01",
            "那我就坦然接受好了。\x02\x03",

            "#07906F#1S……谢谢你，兰迪。#3S\x02",
        )
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0x104,
        "#6P#00305F……哎？你刚刚说了什么？\x02",
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0x8,
        "#07903F没、没什么。\x02",
    )

    CloseMessageWindow()
    OP_5A()
    SetScenarioFlags(0x149, 4)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x68), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4646")
    OP_93(0x8, 0x0, 0x0)
    SetChrPos(0x0, -1310, 10, 40450, 0)
    Jump("loc_466C")

    label("loc_4646")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6A), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_466C")
    OP_93(0x8, 0x10E, 0x0)
    SetChrPos(0x0, -36300, 0, 2009, 0)

    label("loc_466C")

    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4690")
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)

    label("loc_4690")

    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_12_3D42 end

    def Function_13_4697(): pass

    label("Function_13_4697")

    EventBegin(0x0)
    FadeToDark(500, 0, -1)
    OP_0D()
    LoadChrToIndex("chr/ch44900.itc", 0x1E)
    OP_68(-39050, 900, 70, 0)
    MoveCamera(315, 25, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25500, 0)
    SetChrFlags(0xA, 0x8000)
    SetChrChipByIndex(0xD, 0x1E)
    SetChrSubChip(0xD, 0x0)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x8000)
    SetChrPos(0xD, -37300, 0, 0, 270)
    FadeToBright(1000, 0)
    OP_0D()

    #C0161
    ChrTalk(
        0xA,
        (
            "#5P#02001F──以上就是从警方的\x01",
            "可靠渠道得来的情报。\x02\x03",

            "#02003F恐怖分子们肯定\x01",
            "会以某种方法尝试入侵，\x01",
            "这一点是毋庸置疑的。\x02",
        )
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0xD,
        "#12P唔……真是群麻烦的家伙。\x02",
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0xD,
        (
            "#12P明白了，\x01",
            "我会继续加强\x01",
            "唐古拉姆门的警备。\x02",
        )
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0xA,
        (
            "#5P#02003F嗯，还有……\x01",
            "他们驾驶飞艇入侵的可能性\x01",
            "也不能完全排除。\x02\x03",

            "#02000F至于这方面，你可以活用\x01",
            "配备在边境大门附近的雷达设施。\x02",
        )
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0xD,
        "#12P唔，您是指那个对空雷达吗？\x02",
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0xD,
        (
            "#12P明白了，\x01",
            "我现在就去联系那里的负责人……\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrFlags(0xD, 0x80)
    OP_68(-1850, 900, -4540, 0)
    MoveCamera(315, 25, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25500, 0)
    SetChrPos(0x101, -1050, 0, -4470, 270)
    SetChrPos(0x102, -650, 0, -3490, 270)
    SetChrPos(0x103, -550, 0, -5500, 270)
    SetChrPos(0x104, 950, 0, -4470, 270)
    SetChrPos(0x109, 650, 0, -5500, 270)
    SetChrPos(0x105, 1050, 0, -3200, 270)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    FadeToBright(500, 0)
    OP_0D()

    #C0167
    ChrTalk(
        0x101,
        (
            "#00000F他们好像在讨论今天的\x01",
            "警备体制呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0x102,
        (
            "#00100F嗯，应对恐怖分子的策略\x01",
            "似乎是重点讨论话题。\x02",
        )
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0x104,
        (
            "#12P#00303F话说回来，雷达设施……？\x01",
            "大门附近有那种东西吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0x109,
        (
            "#12P#10100F在两个边境大门的附近应该\x01",
            "都配备了那种设施。\x02\x03",

            "#10103F虽然我从来没有用过……\x02",
        )
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0x103,
        (
            "#6P#00203F那个设施是财团\x01",
            "过去安装在\x01",
            "克洛斯贝尔的。\x02\x03",

            "#00200F据说它的性能很高，\x01",
            "可以在相当大的范围内\x01",
            "监视进入自治州领空的飞船。\x02",
        )
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0x101,
        "#00005F哦……\x02",
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0x105,
        (
            "#12P#10300F既然有那种设施，\x01",
            "我们就不必太过担心了。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetScenarioFlags(0x149, 6)
    OP_D7(0x1E)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, -1050, 0, -4470, 90)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_13_4697 end

    def Function_14_4B76(): pass

    label("Function_14_4B76")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x149, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4B88")
    Call(0, 13)
    Jump("loc_4BEB")

    label("loc_4B88")

    TalkBegin(0xFF)

    #C0174
    ChrTalk(
        0x101,
        (
            "#00000F索妮亚司令和道格拉斯副司令正在\x01",
            "商讨应对恐怖分子的措施。\x01",
            "……还是不要进去打扰了。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFF)

    label("loc_4BEB")

    Return()

    # Function_14_4B76 end

    SaveToFile()

Try(main)
