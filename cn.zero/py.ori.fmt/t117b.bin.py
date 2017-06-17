from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "t117b.bin",                # FileName
        "t117b",                    # MapName
        "t117b",                    # Location
        0x004A,                     # MapIndex
        "ed7125",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 74, 0, 1, 0, 2],
    )

    BuildStringList((
        "t117b",                  # 0
        "客人",                   # 1
        "客人",                   # 2
        "客人",                   # 3
        "艾维琳夫人",             # 4
        "詹姆斯",                 # 5
        "向导",                   # 6
        "黑手党１",               # 7
        "黑手党２",               # 8
        "bt113b",                 # 9
    ))

    ATBonus("ATBonus_1FC", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)

    MonsterBattlePostion("MonsterBattlePostion_2DC", 6, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_2E0", 10, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_2E4", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_2E8", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_2EC", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_2F0", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_2F4", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_2F8", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_2BC", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_2C0", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_2C4", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_2C8", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_2CC", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_2D0", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_2D4", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_2D8", 5, 5, 45)

    # monster count: 0

    # event battle count: 1

    BattleInfo(
        "BattleInfo_2FC", 0x000A, 27, 6, 0, 0, 0, 0, 0, "bt113b", 0x00000000, 100, 0, 0, 0,
        (
            ("ms31002.dat", "ms31102.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_2DC", "MonsterBattlePostion_2BC", "ed7509", "ed7000", "ATBonus_1FC"),
            (),
            (),
            (),
        )
    )

    AddCharChip((
        "chr/ch22000.itc",                   # 00
        "chr/ch33002.itc",                   # 01
        "chr/ch26902.itc",                   # 02
        "chr/ch33302.itc",                   # 03
        "chr/ch27802.itc",                   # 04
        "chr/ch00000.itc",                   # 05
        "chr/ch00000.itc",                   # 06
        "chr/ch00000.itc",                   # 07
        "chr/ch00000.itc",                   # 08
        "chr/ch00000.itc",                   # 09
        "chr/ch00000.itc",                   # 0A
        "chr/ch00000.itc",                   # 0B
        "chr/ch00000.itc",                   # 0C
        "chr/ch00000.itc",                   # 0D
        "chr/ch00000.itc",                   # 0E
        "chr/ch00000.itc",                   # 0F
        "chr/ch00000.itc",                   # 10
        "chr/ch00000.itc",                   # 11
        "chr/ch00000.itc",                   # 12
        "chr/ch00000.itc",                   # 13
        "chr/ch00000.itc",                   # 14
        "chr/ch00000.itc",                   # 15
        "chr/ch00000.itc",                   # 16
        "chr/ch00000.itc",                   # 17
        "chr/ch00000.itc",                   # 18
        "chr/ch00000.itc",                   # 19
        "chr/ch00000.itc",                   # 1A
        "chr/ch00000.itc",                   # 1B
        "chr/ch31051.itc",                   # 1C
        "chr/ch31151.itc",                   # 1D
    ))

    DeclNpc(-310,    0,       -71709,  180,  385,  0x0, 0,   0,   0,   0,   0,   0,   3,   255,  0)
    DeclNpc(44860,   150,     -13789,  270,  469,  0x0, 0,   1,   0,   255, 255, 0,   4,   255,  0)
    DeclNpc(40840,   150,     -13789,  90,   469,  0x0, 0,   2,   0,   255, 255, 0,   5,   255,  0)
    DeclNpc(44860,   150,     26239,   270,  469,  0x0, 0,   3,   0,   255, 255, 0,   6,   255,  0)
    DeclNpc(40840,   150,     26290,   90,   469,  0x0, 0,   4,   0,   255, 255, 0,   7,   255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   28,  0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   29,  0,   255, 255, 255, 255, 255,  0)

    ScpFunction((
        "Function_0_36C",          # 00, 0
        "Function_1_424",          # 01, 1
        "Function_2_4AB",          # 02, 2
        "Function_3_502",          # 03, 3
        "Function_4_5A8",          # 04, 4
        "Function_5_755",          # 05, 5
        "Function_6_785",          # 06, 6
        "Function_7_A0F",          # 07, 7
        "Function_8_C29",          # 08, 8
        "Function_9_1A84",         # 09, 9
        "Function_10_2B5D",        # 0A, 10
    ))


    def Function_0_36C(): pass

    label("Function_0_36C")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_3AC"),
        (1, "loc_3B8"),
        (2, "loc_3C4"),
        (3, "loc_3D0"),
        (4, "loc_3DC"),
        (5, "loc_3E8"),
        (6, "loc_3F4"),
        (SWITCH_DEFAULT, "loc_400"),
    )


    label("loc_3AC")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_40C")

    label("loc_3B8")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_40C")

    label("loc_3C4")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_40C")

    label("loc_3D0")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_40C")

    label("loc_3DC")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_40C")

    label("loc_3E8")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_40C")

    label("loc_3F4")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_40C")

    label("loc_400")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_40C")

    label("loc_40C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_423")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_40C")

    label("loc_423")

    Return()

    # Function_0_36C end

    def Function_1_424(): pass

    label("Function_1_424")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_45E")
    ClearScenarioFlags(0x5C, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_441")
    Event(0, 8)
    Jump("loc_45E")

    label("loc_441")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_452")
    Event(0, 9)
    Jump("loc_45E")

    label("loc_452")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_45E")
    Event(0, 9)

    label("loc_45E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 5)), scpexpr(EXPR_END)), "loc_46C")
    Jump("loc_4AA")

    label("loc_46C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_END)), "loc_47A")
    Jump("loc_4AA")

    label("loc_47A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 1)), scpexpr(EXPR_END)), "loc_492")
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    Jump("loc_4AA")

    label("loc_492")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_4AA")
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)

    label("loc_4AA")

    Return()

    # Function_1_424 end

    def Function_2_4AB(): pass

    label("Function_2_4AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 5)), scpexpr(EXPR_END)), "loc_4B4")

    label("loc_4B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_4C2")
    Jump("loc_501")

    label("loc_4C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 6)), scpexpr(EXPR_END)), "loc_501")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6B), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6D), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x71), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_501")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_501")
    Event(0, 10)

    label("loc_501")

    Return()

    # Function_2_4AB end

    def Function_3_502(): pass

    label("Function_3_502")

    TalkBegin(0xFE)

    #C0001
    ChrTalk(
        0xFE,
        (
            "这次受到邀请的客人……\x01",
            "虽然没有透露姓名，\x01",
            "但都是帝国与共和国的要人。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0xFE,
        (
            "那些政治家与贵族\x01",
            "真是擅长表里不一\x01",
            "这一套啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0xFE,
        (
            "……当然我也不例外。\x01",
            "呵呵……\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_3_502 end

    def Function_4_5A8(): pass

    label("Function_4_5A8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6AF")

    #C0004
    ChrTalk(
        0xFE,
        (
            "这个竞拍会是与各国要人\x01",
            "缔结关系的\x01",
            "绝好机会。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0xFE,
        (
            "呵呵……女儿啊，\x01",
            "顺便也找个\x01",
            "夫婿怎么样？\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0xA,
        (
            "呵呵……父亲可真是的，\x01",
            "那简直像是政治婚姻嘛。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0xA,
        (
            "父亲以上门女婿的身份\x01",
            "入赘到母亲家，\x01",
            "其实也是这么回事吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0xFE,
        (
            "哇哈哈哈，\x01",
            "真是说不过你啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_751")

    label("loc_6AF")


    #C0009
    ChrTalk(
        0xFE,
        (
            "呵呵……\x01",
            "从实际上说，也没有比婚姻\x01",
            "更加可靠的联盟了嘛。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0xFE,
        (
            "要是有机会的话，最好能找个……虽然我是这么想，\x01",
            "但她终究已经到了有自己见解的年龄了啊。\x01",
            "哇哈哈哈。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_751")

    TalkEnd(0xFE)
    Return()

    # Function_4_5A8 end

    def Function_5_755(): pass

    label("Function_5_755")

    TalkBegin(0xFE)

    #C0011
    ChrTalk(
        0xFE,
        (
            "呵呵……父亲可真是的，\x01",
            "就会开玩笑。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_5_755 end

    def Function_6_785(): pass

    label("Function_6_785")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_819")
    Jump("loc_863")

    label("loc_819")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_839")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_863")

    label("loc_839")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_859")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_863")

    label("loc_859")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_863")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_994")

    #C0012
    ChrTalk(
        0xFE,
        (
            "和丈夫的缘分已尽，也该分手了……\x01",
            "就在我如此想的时候，\x01",
            "瓦吉却这样对我说——\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0xFE,
        (
            "『你之所以不能原谅你的丈夫，\x01",
            "  正是因为你仍然真心爱着他。』……\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0xFE,
        (
            "我竟然忘记了最重要的事呢，\x01",
            "要感谢瓦吉才行……\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0xFE,
        (
            "我先生也在反省了，\x01",
            "我想，这次就原谅他吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xBF, 2)
    SetScenarioFlags(0x0, 1)
    Jump("loc_A07")

    label("loc_994")

    SetChrSubChip(0xB, 0x0)

    #C0016
    ChrTalk(
        0xFE,
        (
            "我非常感谢瓦吉，\x01",
            "结果是他让我们夫妇\x01",
            "破镜重圆了。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0xFE,
        (
            "……好了，亲爱的，我们走吧。\x01",
            "竞拍差不多也快开始了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A07")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_6_785 end

    def Function_7_A0F(): pass

    label("Function_7_A0F")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_AA3")
    Jump("loc_AED")

    label("loc_AA3")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_AC3")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_AED")

    label("loc_AC3")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AE3")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_AED")

    label("loc_AE3")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_AED")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BD4")

    #C0018
    ChrTalk(
        0xFE,
        (
            "我还是第一次见到\x01",
            "艾维琳那么生气的样子呢。\x01",
            "……说实话，好可怕啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0xFE,
        (
            "平时她都很温柔安分，\x01",
            "所以我才敢大胆地\x01",
            "花心出轨……\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0xFE,
        (
            "原来她的性格这么刚烈啊。\x01",
            "我都不知道呢……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xBF, 2)
    SetScenarioFlags(0x0, 2)
    Jump("loc_C21")

    label("loc_BD4")


    #C0021
    ChrTalk(
        0xFE,
        (
            "无论如何，能和艾维琳\x01",
            "和解，真是太好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0xFE,
        "……我以后再也不会花心了。\x02",
    )

    CloseMessageWindow()

    label("loc_C21")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_7_A0F end

    def Function_8_C29(): pass

    label("Function_8_C29")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(47070, 2000, -52070, 0)
    MoveCamera(48, 18, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18250, 0)
    SetChrPos(0x101, 46200, 0, -52600, 90)
    SetChrPos(0x102, 46200, 0, -51400, 90)
    SetChrPos(0x138, 48700, 0, -52000, 270)
    FadeToBright(1000, 0)
    OP_68(47070, 1200, -52070, 3000)
    OP_6F(0x1)
    OP_0D()

    #C0023
    ChrTalk(
        0x138,
        (
            "#2904F#11P呵呵，原来如此，\x01",
            "还有这样的内情啊。\x02\x03",

            "#2902F你们还真大胆呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x101,
        (
            "#5106F#6P……嗯，是啊。\x02\x03",

            "#5108F其实除了旁观之外也做不了什么，\x01",
            "所以也许只是为了自我满足而已吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x138,
        (
            "#2902F#11P呵呵，不过我很欣赏啊。\x02\x03",

            "#2909F身为艾莉的同事，\x01",
            "要是连这点胆识都没有，\x01",
            "可就太不合格了呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    #C0026
    ChrTalk(
        0x102,
        (
            "#5313F#6P真、真是的，你在说什么啊。\x02\x03",

            "#5301F……话说回来，\x01",
            "贝尔，你怎么会在这里？\x02\x03",

            "听你刚才说的那些话，\x01",
            "你好像也是第一次来啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x138,
        (
            "#2902F#11P哈尔特曼议长\x01",
            "每年都很热心地邀请我们。\x02\x03",

            "#2903F只是，那个人\x01",
            "不是和一些可疑的家伙有所来往吗？\x02\x03",

            "所以父亲一直以种种\x01",
            "理由加以拒绝……\x02\x03",

            "#2901F不过我却\x01",
            "不能完全置之不理。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x102,
        (
            "#5306F#6P原来如此……\x01",
            "确实可以理解。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0029
    ChrTalk(
        0x101,
        "#5105F#6P有什么内情吗？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)
    Sleep(300)

    #C0030
    ChrTalk(
        0x102,
        (
            "#5300F#5P之前也说过的，\x01",
            "叔叔把ＩＢＣ的好几项事业\x01",
            "都交给贝尔来打理。\x02\x03",

            "这个米修拉姆的开发计划\x01",
            "似乎也是由她来管理的。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0031
    ChrTalk(
        0x101,
        "#5111F#6P哎……！？\x02",
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x138,
        (
            "#2902F#11P呵呵，话虽如此，\x01",
            "但其实也只是参与了酒店\x01",
            "和主题公园的运营而已。\x02\x03",

            "#2906F只是，由于这层关系，\x01",
            "实在没办法每次都拒绝\x01",
            "一直住在此地的议长的邀请。\x02\x03",

            "#2900F所以今年\x01",
            "就决定出席了。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x101,
        "#5101F#6P原、原来如此……\x02",
    )

    CloseMessageWindow()
    OP_93(0x102, 0x5A, 0x190)
    Sleep(300)

    #C0034
    ChrTalk(
        0x102,
        "#5311F#6P………………………………\x02",
    )

    CloseMessageWindow()
    OP_63(0x138, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0035
    ChrTalk(
        0x138,
        (
            "#2905F#11P哎呀，艾莉？\x02\x03",

            "你好像是\x01",
            "有什么话想说吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x102,
        (
            "#5303F#6P……嗯，算是吧。\x02\x03",

            "#5300F贝尔是那种，对于自己不喜欢的事情\x01",
            "就绝对不会去做的类型吧？\x02\x03",

            "可是，你竟然会特意来到这种自己不感兴趣\x01",
            "的地方。虽说存在着某些内情……\x02\x03",

            "但是不是还有其它目的？\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x138,
        (
            "#2904F#11P呵呵……不愧是艾莉。\x02\x03",

            "#2902F──其实，在这次的拍卖品里，\x01",
            "似乎有件很有意思的东西。\x02\x03",

            "我对那个很感兴趣，\x01",
            "所以才决定出席的。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0038
    ChrTalk(
        0x101,
        "#5105F#6P那是……\x02",
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x102,
        "#5301F#6P是什么样的展品呢？\x02",
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x138,
        (
            "#2904F#11P是罗赞贝尔克工房制造的\x01",
            "初期古典人偶……\x02\x03",

            "#2902F据宣传说，在爱好者之间，\x01",
            "那可是能标到天价的梦幻作品。\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x101,
        (
            "#5105F#6P古典人偶……\x01",
            "是那个人偶工房制造的吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x102,
        (
            "#5301F#6P……那也是\x01",
            "有隐情的作品吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x138,
        (
            "#2904F#11P可能是赃物，也可能是什么地方的资产家\x01",
            "因为某些见不得人的理由而卖出的……\x02\x03",

            "#2902F详情虽然还不清楚，\x01",
            "但据传闻说，那是件非常精美的杰作。\x02\x03",

            "作为一名收藏家，\x01",
            "是不能错过的吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x102,
        (
            "#5306F#6P原来如此，你从以前开始\x01",
            "就对那里制作的人偶很着迷呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x101,
        (
            "#5101F#6P……顺带一问，那个人偶\x01",
            "大概值多少钱呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x138,
        (
            "#2905F#11P这个啊……\x02\x03",

            "#2906F初期的作品好像比最近的作品\x01",
            "要大一圈，\x01",
            "几乎没在市场上出现过。\x02\x03",

            "大师似乎也\x01",
            "不打算再做那种尺寸的人偶了，\x01",
            "所以必然很珍贵……\x02\x03",

            "#2900F以前在帝都举行的竞拍会上，\x01",
            "听说还有过以五百万米拉\x01",
            "落槌的作品呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0047
    ChrTalk(
        0x101,
        "#5111F#6P一、一件人偶值那么多钱！？\x02",
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x102,
        (
            "#5309F#6P嗯，因为是拥有众多\x01",
            "热切爱好者的艺术品嘛……\x02\x03",

            "#5300F不过，看你的样子，\x01",
            "好像是势在必得了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x138,
        (
            "#2904F#11P呵呵，不管来路如何，\x01",
            "人偶本身是无罪的。\x02\x03",

            "#2902F当然了，如果那是赃物，\x01",
            "我也会采取相应措施的。\x02\x03",

            "#2909F但在此之后，我还是打算和\x01",
            "之前的所有者交涉，将它弄到手。\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x101,
        "#5106F#6P……无话可说了。\x02",
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x102,
        "#5306F#6P呼，真是比不过你啊。\x02",
    )

    CloseMessageWindow()
    Sound(811, 0, 100, 0)
    Sleep(500)
    OP_63(0x138, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0052
    ChrTalk(
        0x138,
        "#2905F#11P哎呀……\x02",
    )

    CloseMessageWindow()
    SetChrPos(0xD, 38000, 0, -52000, 0)
    OP_68(45720, 1200, -52070, 1500)

    def lambda_1803():
        OP_93(0xFE, 0x10E, 0x190)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1803)
    Sleep(50)

    def lambda_1813():
        OP_93(0xFE, 0x10E, 0x190)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1813)
    OP_6F(0x1)

    #N0053
    NpcTalk(
        0xD,
        "向导的声音",
        "#2S打扰了，玛丽亚贝尔小姐。\x02",
    )

    CloseMessageWindow()

    #N0054
    NpcTalk(
        0xD,
        "向导的声音",
        (
            "#2S竞拍会快要开始了，\x01",
            "所以我前来通知您……\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x138,
        (
            "#2904F#11P是吗，谢谢。\x02\x03",

            "#2900F我立刻就过去，\x01",
            "能帮我在后排\x01",
            "准备三个人的席位吗？\x02",
        )
    )

    CloseMessageWindow()

    #N0056
    NpcTalk(
        0xD,
        "向导的声音",
        (
            "#2S──遵命。\x01",
            "那么，我这就去准备。\x02",
        )
    )

    CloseMessageWindow()
    OP_68(47070, 1200, -52070, 1200)

    def lambda_1921():
        OP_93(0xFE, 0x5A, 0x190)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1921)
    Sleep(50)

    def lambda_1931():
        OP_93(0xFE, 0x5A, 0x190)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1931)
    OP_6F(0x1)

    #C0057
    ChrTalk(
        0x102,
        "#5308F#6P那个，贝尔……\x02",
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x138,
        (
            "#2902F#11P呵呵，不必担心。\x02\x03",

            "我打算等竞拍会结束之后\x01",
            "再去跟议长打招呼的。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x102,
        (
            "#5306F#6P嗯，这样啊～……\x02\x03",

            "#5300F没关系吧，罗伊德？\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x101,
        (
            "#5104F#6P嗯，机会难得，\x01",
            "就让我们跟您一起出席吧。\x02\x03",

            "#5100F玛丽亚贝尔小姐，\x01",
            "请多关照了。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x138,
        "#2909F#11P嗯，彼此彼此。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, 44770, 0, -52070, 270)
    SetScenarioFlags(0xA6, 1)
    OP_29(0x47, 0x1, 0xB)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_8_C29 end

    def Function_9_1A84(): pass

    label("Function_9_1A84")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(47070, 2000, -52070, 0)
    MoveCamera(48, 18, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18250, 0)
    SetChrPos(0x101, 46200, 0, -52600, 90)
    SetChrPos(0xEF, 46200, 0, -51400, 90)
    SetChrPos(0x138, 48700, 0, -52000, 270)
    FadeToBright(1000, 0)
    OP_68(47070, 1200, -52070, 3000)
    OP_6F(0x1)
    OP_0D()

    #C0062
    ChrTalk(
        0x138,
        (
            "#2904F#11P呵呵，原来如此，\x01",
            "还有这样的内情啊。\x02\x03",

            "#2902F你们还真大胆呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x101,
        (
            "#5106F#6P……嗯，是啊。\x02\x03",

            "#5108F其实除了旁观之外也做不了什么，\x01",
            "所以也许只是为了自我满足而已吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x138,
        (
            "#2902F#11P呵呵，不过我很欣赏啊。\x02\x03",

            "#2909F身为艾莉的同事，\x01",
            "要是连这点胆识都没有，\x01",
            "可就太不合格了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x101,
        "#5112F#6P是、是这样吗……？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_1C7C")

    #C0066
    ChrTalk(
        0x103,
        (
            "#5402F#6P看来您很重视\x01",
            "艾莉前辈呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CB1")

    label("loc_1C7C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_1CB1")

    #C0067
    ChrTalk(
        0x104,
        (
            "#5602F#6P哈哈，看来你很重视\x01",
            "大小姐啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1CB1")


    #C0068
    ChrTalk(
        0x138,
        (
            "#2904F#11P嗯，说我爱她\x01",
            "也不为过呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xEF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0069
    ChrTalk(
        0x101,
        "#5111F#6P咦咦！？\x02",
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x138,
        (
            "#2902F#11P因为那孩子很可爱，对吧？\x02\x03",

            "性格直率、意志坚强、\x01",
            "凛然不屈，\x01",
            "却又沉稳高雅、不失温柔。\x02\x03",

            "#2909F是我引以为傲的朋友呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x101,
        (
            "#5100F#6P的确……\x02\x03",

            "#5104F她也是我们\x01",
            "引以为傲的同事呢。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_1E37")

    #C0072
    ChrTalk(
        0x103,
        (
            "#5404F#6P呵呵，不过这种话要是被她本人听见了，\x01",
            "一定会满脸通红的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E84")

    label("loc_1E37")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_1E84")

    #C0073
    ChrTalk(
        0x104,
        (
            "#5609F#6P哈哈，不过这话要是被她本人听见了，\x01",
            "肯定会满脸通红的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E84")


    #C0074
    ChrTalk(
        0x138,
        (
            "#2906F#11P只是，没能在这里\x01",
            "见到艾莉，真有点可惜呢。\x02\x03",

            "#2900F本来还想和她一起\x01",
            "鉴赏竞拍会的展品呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0x101,
        (
            "#5101F#6P话说回来……\x01",
            "贝尔小姐为什么会在这里？\x02\x03",

            "听您刚才说的那些话，\x01",
            "好像也是第一次来啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x138,
        (
            "#2902F#11P哈尔特曼议长\x01",
            "每年都很热心地邀请我们。\x02\x03",

            "#2903F只是，那个人\x01",
            "不是和一些可疑的家伙有所来往吗？\x02\x03",

            "所以父亲一直以种种\x01",
            "理由加以拒绝……\x02\x03",

            "#2901F不过我却\x01",
            "不能完全置之不理。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_202E")

    #C0077
    ChrTalk(
        0x103,
        "#5400F#6P……是有什么内情吗？\x02",
    )

    CloseMessageWindow()
    Jump("loc_2058")

    label("loc_202E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_2058")

    #C0078
    ChrTalk(
        0x104,
        "#5605F#6P难道有什么内情吗？\x02",
    )

    CloseMessageWindow()

    label("loc_2058")


    #C0079
    ChrTalk(
        0x138,
        (
            "#2904F#11P因为米修拉姆的开发计划\x01",
            "是由我负责的。\x02\x03",

            "#2900F由于这层关系，\x01",
            "实在没办法每次都拒绝\x01",
            "一直住在此地的议长的邀请。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xEF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_2130")

    #C0080
    ChrTalk(
        0x103,
        "#5401F#6P哎……！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_2152")

    label("loc_2130")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_2152")

    #C0081
    ChrTalk(
        0x104,
        "#5607F#6P真的吗！？\x02",
    )

    CloseMessageWindow()

    label("loc_2152")


    #C0082
    ChrTalk(
        0x101,
        (
            "#5111F#6P这、这么说来……\x01",
            "好像确实曾听说过您负责了\x01",
            "ＩＢＣ的几项事业……\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x138,
        (
            "#2904F#11P呵呵，话虽如此，\x01",
            "但其实也只是参与了酒店\x01",
            "和主题公园的运营而已。\x02\x03",

            "#2902F──而且，今年的竞拍会\x01",
            "似乎有件很有意思的拍卖品。\x02\x03",

            "我对那个感兴趣，\x01",
            "所以才决定出席的。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xEF, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0084
    ChrTalk(
        0x101,
        "#5101F#6P那是……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_22BC")

    #C0085
    ChrTalk(
        0x103,
        "#5401F#6P是什么样的展品呢……？\x02",
    )

    CloseMessageWindow()
    Jump("loc_22E6")

    label("loc_22BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_22E6")

    #C0086
    ChrTalk(
        0x104,
        "#5602F#6P……是什么展品啊？\x02",
    )

    CloseMessageWindow()

    label("loc_22E6")


    #C0087
    ChrTalk(
        0x138,
        (
            "#2904F#11P是罗赞贝尔克工房制造的\x01",
            "初期古典人偶……\x02\x03",

            "#2902F据宣传说，在爱好者之间，\x01",
            "那可是能标到天价的梦幻作品。\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0x101,
        (
            "#5105F#6P古典人偶……\x01",
            "是那个人偶工房制造的吧。\x02\x03",

            "#5101F……那也是\x01",
            "有隐情的作品吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0x138,
        (
            "#2904F#11P可能是赃物，也可能是什么地方的资产家\x01",
            "因为某些见不得人的理由而卖出的……\x02\x03",

            "详情虽然还不清楚，\x01",
            "但据传闻说，那是件非常精美的杰作。\x02\x03",

            "#2902F作为一名收藏家，\x01",
            "是不能错过的吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x101,
        "#5112F#6P原、原来如此……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_24CB")

    #C0091
    ChrTalk(
        0x103,
        (
            "#5400F#6P顺便一问，这种人偶……\x01",
            "大约值多少钱呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2508")

    label("loc_24CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_2508")

    #C0092
    ChrTalk(
        0x104,
        (
            "#5609F#6P顺带问一下，这种人偶\x01",
            "大概值多少钱啊？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2508")


    #C0093
    ChrTalk(
        0x138,
        (
            "#2905F#11P这个啊……\x02\x03",

            "#2906F初期的作品好像比最近的作品\x01",
            "要大一圈，\x01",
            "几乎没在市场上出现过。\x02\x03",

            "大师似乎也\x01",
            "不打算再做那种尺寸的人偶了，\x01",
            "所以必然很珍贵……\x02\x03",

            "#2900F以前在帝都举行的竞拍会上，\x01",
            "听说还有过以五百万米拉\x01",
            "落槌的作品呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xEF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0094
    ChrTalk(
        0x101,
        "#5111F#6P一、一件人偶值那么多钱！？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_26BE")

    #C0095
    ChrTalk(
        0x103,
        (
            "#5406F#6P这个价格应该都可以买一台主流的\x01",
            "导力演算器了呢……\x02\x03",

            "#5400F莫非您打算\x01",
            "拍下那个人偶吗……？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2720")

    label("loc_26BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_2720")

    #C0096
    ChrTalk(
        0x104,
        (
            "#5606F#6P这个价格都可以\x01",
            "买下一辆旧式战车了啊……\x02\x03",

            "#5605F莫非你打算\x01",
            "拍下那个人偶吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2720")


    #C0097
    ChrTalk(
        0x138,
        (
            "#2904F#11P呵呵，不管来路如何，\x01",
            "人偶本身是无罪的。\x02\x03",

            "#2902F当然了，如果那是赃物，\x01",
            "我也会采取相应措施的。\x02\x03",

            "#2909F但在此之后，我还是打算和\x01",
            "之前的所有者交涉，将它弄到手。\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x101,
        "#5106F#6P……无话可说了。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_2817")

    #C0099
    ChrTalk(
        0x103,
        "#5406F#6P真是太有钱了……\x02",
    )

    CloseMessageWindow()
    Jump("loc_283F")

    label("loc_2817")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_283F")

    #C0100
    ChrTalk(
        0x104,
        "#5606F#6P真是太阔绰了……\x02",
    )

    CloseMessageWindow()

    label("loc_283F")

    Sound(811, 0, 100, 0)
    Sleep(500)

    #C0101
    ChrTalk(
        0x138,
        "#2905F#11P哎呀……\x02",
    )

    CloseMessageWindow()
    SetChrPos(0xD, 38000, 0, -52000, 0)
    OP_68(45720, 1200, -52070, 1200)

    def lambda_2887():
        OP_93(0xFE, 0x10E, 0x190)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2887)
    Sleep(50)

    def lambda_2897():
        OP_93(0xFE, 0x10E, 0x190)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_2897)
    OP_6F(0x1)

    #N0102
    NpcTalk(
        0xD,
        "向导的声音",
        "#2S打扰了，玛丽亚贝尔小姐。\x02",
    )

    CloseMessageWindow()

    #N0103
    NpcTalk(
        0xD,
        "向导的声音",
        (
            "#2S竞拍会快要开始了，\x01",
            "所以我前来通知您……\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0x138,
        (
            "#2909F#11P是吗，谢谢。\x02\x03",

            "#2900F我立刻就过去，\x01",
            "能帮我在后排\x01",
            "准备三个人的席位吗？\x02",
        )
    )

    CloseMessageWindow()

    #N0105
    NpcTalk(
        0xD,
        "向导的声音",
        (
            "#2S──遵命。\x01",
            "那么，我这就去准备。\x02",
        )
    )

    CloseMessageWindow()
    OP_68(47070, 1200, -52070, 1200)

    def lambda_29A5():
        OP_93(0xFE, 0x5A, 0x190)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_29A5)
    Sleep(50)

    def lambda_29B5():
        OP_93(0xFE, 0x5A, 0x190)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_29B5)
    OP_6F(0x1)

    #C0106
    ChrTalk(
        0x101,
        "#5108F#6P那个，玛丽亚贝尔小姐……\x02",
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0x138,
        (
            "#2902F#11P呵呵，不必担心。\x02\x03",

            "我打算等竞拍会结束之后\x01",
            "再去跟议长打招呼的。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_2A73")

    #C0108
    ChrTalk(
        0x103,
        (
            "#5402F#6P嗯，那样的话，\x01",
            "应该就没有问题了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2AAC")

    label("loc_2A73")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_2AAC")

    #C0109
    ChrTalk(
        0x104,
        (
            "#5600F#6P嗯，那样的话，\x01",
            "应该就没问题了啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2AAC")


    #C0110
    ChrTalk(
        0x101,
        (
            "#5103F#6P……我明白了。\x01",
            "机会难得，\x01",
            "就让我们跟您一起出席吧。\x02\x03",

            "#5100F玛丽亚贝尔小姐，\x01",
            "请多关照了。\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0x138,
        "#2909F#11P嗯，彼此彼此。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, 44770, 0, -52070, 270)
    SetScenarioFlags(0xA6, 1)
    OP_29(0x47, 0x1, 0xB)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_9_1A84 end

    def Function_10_2B5D(): pass

    label("Function_10_2B5D")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    RunExpression(0x4, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2B9A")
    LoadChrToIndex("chr/ch00150.itc", 0x1F)
    Jump("loc_2BBB")

    label("loc_2B9A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2BB5")
    LoadChrToIndex("chr/ch00250.itc", 0x1F)
    Jump("loc_2BBB")

    label("loc_2BB5")

    LoadChrToIndex("chr/ch00350.itc", 0x1F)

    label("loc_2BBB")

    LoadChrToIndex("chr/ch00450.itc", 0x20)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrChipByIndex(0xEF, 0x1F)
    SetChrChipByIndex(0x105, 0x20)
    SetChrSubChip(0x101, 0x0)
    SetChrSubChip(0xEF, 0x0)
    SetChrSubChip(0x105, 0x0)
    ClearChrFlags(0x133, 0x80)
    ClearChrBattleFlags(0x133, 0x8000)
    SetChrSubChip(0xE, 0x0)
    SetChrSubChip(0xF, 0x0)
    SetChrFlags(0xE, 0x8000)
    SetChrFlags(0xF, 0x8000)
    ClearChrFlags(0xE, 0x80)
    ClearChrBattleFlags(0xE, 0x8000)
    ClearChrFlags(0xF, 0x80)
    ClearChrBattleFlags(0xF, 0x8000)
    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6B), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2CB1")
    OP_68(0, 1200, -11000, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(420, 0)
    SetCameraDistance(22000, 0)
    SetChrPos(0x101, 0, 0, -11000, 0)
    SetChrPos(0xEF, -750, 0, -12500, 0)
    SetChrPos(0x105, 750, 0, -12250, 0)
    SetChrPos(0x133, 0, 0, -14000, 0)
    SetChrPos(0xE, 0, 0, -5000, 180)
    SetChrPos(0xF, -750, 0, -4250, 180)
    Jump("loc_2DED")

    label("loc_2CB1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6D), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D59")
    OP_68(0, 1200, -19000, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(420, 0)
    SetCameraDistance(22000, 0)
    SetChrPos(0x101, 0, 0, -19000, 0)
    SetChrPos(0xEF, -750, 0, -20500, 0)
    SetChrPos(0x105, 750, 0, -20250, 0)
    SetChrPos(0x133, 0, 0, -22000, 0)
    SetChrPos(0xE, 0, 0, -13000, 180)
    SetChrPos(0xF, -750, 0, -12250, 180)
    Jump("loc_2DED")

    label("loc_2D59")

    OP_68(0, 1200, -22000, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(420, 0)
    SetCameraDistance(22000, 0)
    SetChrPos(0x101, 0, 0, -22000, 0)
    SetChrPos(0xEF, -750, 0, -23500, 0)
    SetChrPos(0x105, 750, 0, -23250, 0)
    SetChrPos(0x133, 0, 0, -25000, 0)
    SetChrPos(0xE, 0, 0, -16000, 180)
    SetChrPos(0xF, -750, 0, -15250, 180)

    label("loc_2DED")


    def lambda_2DF2():
        OP_97(0xE, 0x0, 0x0, 0xFFFFEE6C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_2DF2)
    Sleep(50)

    def lambda_2E0F():
        OP_97(0xF, 0x0, 0x0, 0xFFFFEE6C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_2E0F)
    FadeToBright(500, 0)
    OP_0D()
    WaitChrThread(0xE, 1)
    Battle("BattleInfo_2FC", 0x0, 0x0, 0x0, 0xF, 0xFF)
    FadeToDark(0, 0, -1)
    EventBegin(0x0)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrChipByIndex(0xEF, 0xFF)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrSubChip(0xEF, 0x0)
    SetChrSubChip(0x105, 0x0)
    SetChrFlags(0x133, 0x80)
    SetChrBattleFlags(0x133, 0x8000)
    EndChrThread(0xE, 0x1)
    EndChrThread(0xF, 0x1)
    SetChrFlags(0xE, 0x80)
    SetChrBattleFlags(0xE, 0x8000)
    SetChrFlags(0xF, 0x80)
    SetChrBattleFlags(0xF, 0x8000)
    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6B), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F01")
    OP_68(0, 1200, -11000, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(420, 0)
    SetCameraDistance(25000, 0)
    SetChrPos(0x101, 0, 0, -11000, 0)
    SetChrPos(0xEF, 0, 0, -11000, 0)
    SetChrPos(0x105, 0, 0, -11000, 0)
    Jump("loc_2FD7")

    label("loc_2F01")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6D), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F76")
    OP_68(0, 1200, -19000, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(420, 0)
    SetCameraDistance(25000, 0)
    SetChrPos(0x101, 0, 0, -19000, 0)
    SetChrPos(0xEF, 0, 0, -19000, 0)
    SetChrPos(0x105, 0, 0, -19000, 0)
    Jump("loc_2FD7")

    label("loc_2F76")

    OP_68(0, 1200, -23250, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(420, 0)
    SetCameraDistance(25000, 0)
    SetChrPos(0x101, 0, 0, -23250, 0)
    SetChrPos(0xEF, 0, 0, -23250, 0)
    SetChrPos(0x105, 0, 0, -23250, 0)

    label("loc_2FD7")

    FadeToBright(500, 0)
    OP_0D()
    EventEnd(0x5)
    Return()

    # Function_10_2B5D end

    SaveToFile()

Try(main)
