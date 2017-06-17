from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "t4100.bin",                # FileName
        "t4100",                    # MapName
        "t4100",                    # Location
        0x005D,                     # MapIndex
        "ed7124",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 93, 0, 2, 0, 3],
    )

    BuildStringList((
        "t4100",                  # 0
        "缪夏夫人",               # 1
        "昆特老人",               # 2
        "游客琉玛",               # 3
        "盖伊墓前的花",           # 4
        "亚里欧斯家墓前的花",     # 5
        "格里姆伍德家墓前的墓碑", # 6
    ))

    AddCharChip((
        "chr/ch20100.itc",                   # 00
        "chr/ch20000.itc",                   # 01
        "apl/ch50423.itc",                   # 02
        "chr/ch34200.itc",                   # 03
    ))

    DeclNpc(8579,    2000,    25379,   0,    257,  0x0, 0,   0,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(-8869,   0,       11800,   0,    385,  0x0, 0,   1,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(24340,   0,       33569,   45,   385,  0x0, 0,   3,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(20600,   0,       34000,   0,    502,  0x0, 0,   2,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(12000,   4000,    37000,   0,    502,  0x0, 0,   2,   0,   255, 255, 255, 255, 255,  0)

    DeclActor(190,     4200,    45040,   1200,    190,     5700,    45040,   0x007C, 0,  8,  0x0000)
    DeclActor(-23050,  0,       25770,   1200,    -22620,  1500,    25860,   0x007C, 0,  9,  0x0000)
    DeclActor(5560,    4000,    44710,   5000,    5560,    4000,    44710,   0x007C, 0,  12, 0x0000)
    DeclActor(20570,   0,       34830,   1500,    20570,   1500,    34830,   0x007C, 0,  10, 0x0000)
    DeclActor(12080,   4000,    37650,   1500,    12080,   5500,    37650,   0x007C, 0,  11, 0x0000)

    ScpFunction((
        "Function_0_238",          # 00, 0
        "Function_1_2F0",          # 01, 1
        "Function_2_74D",          # 02, 2
        "Function_3_897",          # 03, 3
        "Function_4_962",          # 04, 4
        "Function_5_15F4",         # 05, 5
        "Function_6_1B67",         # 06, 6
        "Function_7_1C1D",         # 07, 7
        "Function_8_23DF",         # 08, 8
        "Function_9_2482",         # 09, 9
        "Function_10_28B1",        # 0A, 10
        "Function_11_2955",        # 0B, 11
        "Function_12_2A31",        # 0C, 12
        "Function_13_356A",        # 0D, 13
    ))


    def Function_0_238(): pass

    label("Function_0_238")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_278"),
        (1, "loc_284"),
        (2, "loc_290"),
        (3, "loc_29C"),
        (4, "loc_2A8"),
        (5, "loc_2B4"),
        (6, "loc_2C0"),
        (SWITCH_DEFAULT, "loc_2D8"),
    )


    label("loc_278")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_2D8")

    label("loc_284")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_2D8")

    label("loc_290")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_2D8")

    label("loc_29C")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_2D8")

    label("loc_2A8")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_2D8")

    label("loc_2B4")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_2D8")

    label("loc_2C0")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2D8")

    label("loc_2D8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2EF")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2D8")

    label("loc_2EF")

    Return()

    # Function_0_238 end

    def Function_1_2F0(): pass

    label("Function_1_2F0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_74C")
    OP_95(0xFE, -8870, 0, 11800, 2000, 0x0)
    OP_93(0xFE, 0x0, 0x190)
    Sleep(1800)
    OP_93(0xFE, 0x10E, 0x190)
    Sleep(100)
    OP_95(0xFE, -16950, 0, 11340, 2000, 0x0)
    OP_93(0xFE, 0x0, 0x190)
    Sleep(1800)
    OP_93(0xFE, 0x10E, 0x190)
    Sleep(100)
    OP_95(0xFE, -19140, 0, 11340, 2000, 0x0)
    OP_95(0xFE, -19140, 0, 16070, 2000, 0x0)
    OP_95(0xFE, -21040, 0, 16090, 2000, 0x0)
    OP_93(0xFE, 0x0, 0x190)
    Sleep(1800)
    OP_93(0xFE, 0x5A, 0x190)
    Sleep(100)
    OP_95(0xFE, -16960, 0, 16090, 2000, 0x0)
    OP_93(0xFE, 0x0, 0x190)
    Sleep(1800)
    OP_93(0xFE, 0x5A, 0x190)
    Sleep(100)
    OP_95(0xFE, -1200, 0, 16090, 2000, 0x0)
    OP_95(0xFE, -1200, 2000, 25270, 2000, 0x0)
    OP_95(0xFE, -10990, 2000, 25270, 2000, 0x0)
    OP_93(0xFE, 0x0, 0x190)
    Sleep(1800)
    OP_93(0xFE, 0x5A, 0x190)
    Sleep(100)
    OP_95(0xFE, -4930, 2000, 25270, 2000, 0x0)
    OP_93(0xFE, 0x0, 0x190)
    Sleep(1800)
    OP_93(0xFE, 0x5A, 0x190)
    Sleep(100)
    OP_95(0xFE, -1200, 2000, 25270, 2000, 0x0)
    OP_95(0xFE, -1200, 4000, 35990, 2000, 0x0)
    OP_95(0xFE, -8460, 4000, 35990, 2000, 0x0)
    OP_93(0xFE, 0x0, 0x190)
    Sleep(1800)
    OP_93(0xFE, 0x5A, 0x190)
    Sleep(100)
    OP_95(0xFE, -170, 4000, 35990, 2000, 0x0)
    OP_95(0xFE, -50, 4200, 43970, 2000, 0x0)
    OP_93(0xFE, 0x0, 0x190)
    Sleep(1800)
    OP_93(0xFE, 0xB4, 0x190)
    Sleep(100)
    OP_95(0xFE, -170, 4000, 35990, 2000, 0x0)
    OP_95(0xFE, 12000, 4000, 35990, 2000, 0x0)
    OP_93(0xFE, 0x0, 0x190)
    Sleep(1800)
    OP_93(0xFE, 0x10E, 0x190)
    Sleep(100)
    OP_95(0xFE, 4970, 4000, 36140, 2000, 0x0)
    OP_93(0xFE, 0x0, 0x190)
    Sleep(1800)
    OP_93(0xFE, 0x10E, 0x190)
    Sleep(100)
    OP_95(0xFE, 1310, 4000, 35990, 2000, 0x0)
    OP_95(0xFE, 1310, 0, 8039, 2000, 0x0)
    OP_95(0xFE, 15920, 0, 8039, 2000, 0x0)
    OP_93(0xFE, 0x0, 0x190)
    Sleep(1800)
    OP_93(0xFE, 0x5A, 0x190)
    Sleep(100)
    OP_95(0xFE, 22720, 0, 8039, 2000, 0x0)
    OP_95(0xFE, 22720, 0, 13250, 2000, 0x0)
    OP_95(0xFE, 20500, 0, 13250, 2000, 0x0)
    OP_93(0xFE, 0x0, 0x190)
    Sleep(1800)
    OP_93(0xFE, 0x10E, 0x190)
    Sleep(100)
    OP_95(0xFE, 11500, 0, 13250, 2000, 0x0)
    OP_93(0xFE, 0x0, 0x190)
    Sleep(1800)
    OP_93(0xFE, 0x10E, 0x190)
    Sleep(100)
    OP_95(0xFE, 9240, 0, 13250, 2000, 0x0)
    OP_95(0xFE, 9240, 0, 16390, 2000, 0x0)
    OP_95(0xFE, 15980, 0, 19640, 2000, 0x0)
    OP_93(0xFE, 0x0, 0x190)
    Sleep(1800)
    OP_93(0xFE, 0x5A, 0x190)
    Sleep(100)
    OP_95(0xFE, 23050, 0, 19550, 2000, 0x0)
    OP_95(0xFE, 23050, 0, 25610, 2000, 0x0)
    OP_95(0xFE, 21270, 0, 25620, 2000, 0x0)
    OP_93(0xFE, 0x0, 0x190)
    Sleep(1800)
    OP_93(0xFE, 0x5A, 0x190)
    Sleep(100)
    OP_95(0xFE, 27500, 0, 25610, 2000, 0x0)
    OP_95(0xFE, 27500, 0, 31330, 2000, 0x0)
    OP_95(0xFE, 20470, 0, 33170, 2000, 0x0)
    OP_93(0xFE, 0x0, 0x190)
    Sleep(1800)
    OP_93(0xFE, 0x6A, 0x190)
    Sleep(100)
    OP_95(0xFE, 27500, 0, 31330, 2000, 0x0)
    OP_95(0xFE, 27500, 0, 25610, 2000, 0x0)
    OP_95(0xFE, 23050, 0, 19550, 2000, 0x0)
    OP_95(0xFE, 23050, 0, 6410, 2000, 0x0)
    OP_95(0xFE, 30, 0, 6690, 2000, 0x0)
    Jump("Function_1_2F0")

    label("loc_74C")

    Return()

    # Function_1_2F0 end

    def Function_2_74D(): pass

    label("Function_2_74D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_75C")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 7)

    label("loc_75C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2E, 0x1, 0x7)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_774")
    Event(0, 13)

    label("loc_774")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_782")
    Jump("loc_83E")

    label("loc_782")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_790")
    Jump("loc_83E")

    label("loc_790")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_79E")
    Jump("loc_83E")

    label("loc_79E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_7B1")
    ClearChrFlags(0x9, 0x80)
    Jump("loc_83E")

    label("loc_7B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_7C4")
    ClearChrFlags(0x9, 0x80)
    Jump("loc_83E")

    label("loc_7C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_7D7")
    ClearChrFlags(0x9, 0x80)
    Jump("loc_83E")

    label("loc_7D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_7E5")
    Jump("loc_83E")

    label("loc_7E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_7F8")
    ClearChrFlags(0x9, 0x80)
    Jump("loc_83E")

    label("loc_7F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_806")
    Jump("loc_83E")

    label("loc_806")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_814")
    Jump("loc_83E")

    label("loc_814")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_827")
    ClearChrFlags(0x9, 0x80)
    Jump("loc_83E")

    label("loc_827")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_835")
    Jump("loc_83E")

    label("loc_835")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_83E")

    label("loc_83E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2E, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_87D")
    SetChrChipByIndex(0xB, 0x2)
    SetChrPos(0xB, -23000, 0, 25500, 0)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)

    label("loc_87D")

    BeginChrThread(0x9, 0, 0, 1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_896")
    ClearChrFlags(0xA, 0x80)

    label("loc_896")

    Return()

    # Function_2_74D end

    def Function_3_897(): pass

    label("Function_3_897")

    OP_65(0x2, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_8A9")
    Jump("loc_8E6")

    label("loc_8A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_8E6")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_8C3")
    Jump("loc_8E6")

    label("loc_8C3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x5)"), scpexpr(EXPR_END)), "loc_8D5")
    Jump("loc_8E6")

    label("loc_8D5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x1)"), scpexpr(EXPR_END)), "loc_8E6")
    OP_66(0x2, 0x1)

    label("loc_8E6")

    OP_65(0x3, 0x1)
    OP_65(0x4, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2E, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_902")
    OP_66(0x3, 0x1)
    OP_66(0x4, 0x1)

    label("loc_902")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_919")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_919")

    SoundDistance(0x84, 0xFFFFD878, 0xFA0, 0xDEA8, 0x2710, 0x186A0, 0x64, 0x0)
    OP_E1(0x6C2, 0xFA0, 0xDEA8)
    OP_E1(0x4F60, 0xFA0, 0xDEA8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_961")
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)

    label("loc_961")

    Return()

    # Function_3_897 end

    def Function_4_962(): pass

    label("Function_4_962")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2E, 0x0, 0x10)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A68")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A07")

    #C0001
    ChrTalk(
        0xFE,
        (
            "你们……\x01",
            "调查过那块墓碑了吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0xFE,
        (
            "在很久以前，\x01",
            "那块墓碑上刻着名字的部分\x01",
            "就已经变得模糊不清了。\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0xFE,
        (
            "那到底是\x01",
            "谁的墓呢……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_A64")

    label("loc_A07")


    #C0004
    ChrTalk(
        0xFE,
        (
            "就算是每天都来扫墓的我，\x01",
            "也从没看见那块墓碑\x01",
            "前有人来过。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0xFE,
        (
            "那块墓碑到底\x01",
            "是谁的呢……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A64")

    TalkEnd(0xFE)
    Return()

    label("loc_A68")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_B90")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B2C")

    #C0006
    ChrTalk(
        0xFE,
        (
            "经常有人提醒我说，\x01",
            "我只是在已故之人的束缚下\x01",
            "浪费余生……\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0xFE,
        (
            "……呵呵，但是\x01",
            "为了不忘记这个人，\x01",
            "我只有一直来这里，不是吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0xFE,
        (
            "所以，我想我今后\x01",
            "仍然会继续来扫墓。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_B8B")

    label("loc_B2C")


    #C0009
    ChrTalk(
        0xFE,
        (
            "不管别人怎么说……\x01",
            "我今后也会时常\x01",
            "来探望他。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0xFE,
        (
            "因为这是阴阳相隔的夫妇\x01",
            "仅有的维系了……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B8B")

    Jump("loc_15F0")

    label("loc_B90")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_C63")

    #C0011
    ChrTalk(
        0xFE,
        "人与人的斗争是件很悲哀的事情……\x02",
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0xFE,
        (
            "一旦出现组织或者国家之间的战争，\x01",
            "就肯定会将无辜的人卷进去。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0xFE,
        (
            "就像利贝尔的女王陛下\x01",
            "提出了《互不侵犯条约》一样……\x01",
            "希望大家都能思考和平解决问题的方法。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15F0")

    label("loc_C63")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_CDD")

    #C0014
    ChrTalk(
        0xFE,
        (
            "守墓人每天都像那样\x01",
            "守护着每个墓地。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0xFE,
        (
            "尽管墓碑仅仅只是一个标记……\x01",
            "但是安眠于此的人们一定会高兴的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15F0")

    label("loc_CDD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_EEF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E28")
    OP_93(0xFE, 0x0, 0x0)

    #C0016
    ChrTalk(
        0xFE,
        "…………………………\x02",
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x153,
        (
            "#1110F……老婆婆，\x01",
            "你闭着眼睛在干什么呀？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x0, 500)

    #C0018
    ChrTalk(
        0xFE,
        "哎……？\x02",
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x101,
        (
            "#0005F这可不好……！\x01",
            "不可以打扰人家，琪雅……！\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0xFE,
        "呵呵，没关系的。\x02",
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0xFE,
        (
            "……我的丈夫在这里长眠，\x01",
            "所以我在为他祈祷。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x153,
        "#1106F祈祷…………\x02",
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0xFE,
        (
            "对……只要来到这里，\x01",
            "我就觉得能够跟他说上话呢……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_EEA")

    label("loc_E28")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_E77")

    #C0024
    ChrTalk(
        0xFE,
        (
            "好了……\x01",
            "差不多该回家了吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0xFE,
        "再见啦……我还会来看你的。\x02",
    )

    CloseMessageWindow()
    Jump("loc_EEA")

    label("loc_E77")


    #C0026
    ChrTalk(
        0xFE,
        (
            "呵呵……\x01",
            "似乎很久没有跟你这样的孩子\x01",
            "说过话了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0xFE,
        (
            "我的儿子住在国外……\x01",
            "你让我想起那孩子小时候的样子了呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EEA")

    Jump("loc_15F0")

    label("loc_EEF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_F99")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F6F")

    #C0028
    ChrTalk(
        0xFE,
        (
            "克洛斯贝尔成立后的第七十年\x01",
            "即将平静地过去……\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0xFE,
        (
            "……今天就在这里\x01",
            "眺望一会景色，\x01",
            "平静度过吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_F94")

    label("loc_F6F")


    #C0030
    ChrTalk(
        0xFE,
        (
            "……今天就在这里\x01",
            "平静地度过吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F94")

    Jump("loc_15F0")

    label("loc_F99")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_1090")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1043")

    #C0031
    ChrTalk(
        0xFE,
        (
            "昨天晚上已经悠闲地在\x01",
            "热闹的大街上散过步了。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0xFE,
        (
            "被霓虹灯点亮的街道\x01",
            "真的非常漂亮。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0xFE,
        (
            "呵呵……如果可以的话，\x01",
            "真想跟我丈夫一起去散步呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_108B")

    label("loc_1043")


    #C0034
    ChrTalk(
        0xFE,
        (
            "克洛斯贝尔市的美丽夜景……\x01",
            "如果可以的话，\x01",
            "真想跟我丈夫一起欣赏呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_108B")

    Jump("loc_15F0")

    label("loc_1090")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_11EE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_115C")

    #C0035
    ChrTalk(
        0xFE,
        (
            "昨天来祈祷的时候，\x01",
            "守墓的老人\x01",
            "跟我说话了。\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0xFE,
        (
            "我开始觉得，一直在这里祈祷的话，\x01",
            "不就白白浪费了\x01",
            "难得的纪念庆典吗……\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0xFE,
        (
            "所以今天晚上我打算好好去\x01",
            "欣赏下克洛斯贝尔的夜景。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_11E9")

    label("loc_115C")


    #C0038
    ChrTalk(
        0xFE,
        (
            "我开始觉得，一直在这里祈祷的话，\x01",
            "不就白白浪费了\x01",
            "难得的纪念庆典吗……\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0xFE,
        (
            "虽然有点对不起长眠于此的丈夫……\x01",
            "但今天就让我好好享受一下吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11E9")

    Jump("loc_15F0")

    label("loc_11EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_12A2")
    OP_93(0xFE, 0x0, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1283")

    #C0040
    ChrTalk(
        0xFE,
        "…………………………\x02",
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x101,
        "#0001F（正在专心祈祷呢……）\x02",
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x102,
        (
            "#0108F（……打扰到人家就不太好了，\x01",
            "  我们走吧。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_129D")

    label("loc_1283")


    #C0043
    ChrTalk(
        0xFE,
        "…………………………\x02",
    )

    CloseMessageWindow()

    label("loc_129D")

    Jump("loc_15F0")

    label("loc_12A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_1400")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_139F")

    #C0044
    ChrTalk(
        0xFE,
        (
            "我的丈夫在三十年前的战争中\x01",
            "离开了这个世界。\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0xFE,
        (
            "那个人与我吵架而离开家后，\x01",
            "便突然被卷入了战斗里……\x01",
            "结果我连他最后一眼都没有看到。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0xFE,
        "……你们应该也有珍视的人吧？\x02",
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0xFE,
        (
            "千万不要像我一样，\x01",
            "与对方留下永远无法挽回的遗憾。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_13FB")

    label("loc_139F")


    #C0048
    ChrTalk(
        0xFE,
        "……你们应该也有珍视的人吧？\x02",
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0xFE,
        (
            "千万不要像我一样，\x01",
            "与对方留下永远无法挽回的遗憾。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_13FB")

    Jump("loc_15F0")

    label("loc_1400")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_14E6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1495")

    #C0050
    ChrTalk(
        0xFE,
        (
            "……我的丈夫大约在三十年前\x01",
            "被卷入了\x01",
            "帝国与共和国的战争中。\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0xFE,
        (
            "虽然平时一直都在吵架，\x01",
            "但他去世之后\x01",
            "还真是寂寞啊……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_14E1")

    label("loc_1495")


    #C0052
    ChrTalk(
        0xFE,
        (
            "虽说都是三十年前\x01",
            "那场战争的错……\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0xFE,
        (
            "但是他去世之后\x01",
            "还真是寂寞啊……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14E1")

    Jump("loc_15F0")

    label("loc_14E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_15F0")
    OP_93(0xFE, 0x0, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1581")

    #C0054
    ChrTalk(
        0xFE,
        "…………………………\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x0, 500)

    #C0055
    ChrTalk(
        0xFE,
        (
            "哎呀，对不起。\x01",
            "没有注意到你们在这里。\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0xFE,
        (
            "因为刚才正在虔心祈祷……\x01",
            "请不要介意哦。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_15F0")

    label("loc_1581")


    #C0057
    ChrTalk(
        0xFE,
        "…………………………\x02",
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x102,
        (
            "#0105F（正在专心祈祷呢……）\x02\x03",

            "#0108F（……打扰到人家就不太好了，\x01",
            "  我们走吧。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15F0")

    TalkEnd(0xFE)
    Return()

    # Function_4_962 end

    def Function_5_15F4(): pass

    label("Function_5_15F4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_1605")
    Jump("loc_1B63")

    label("loc_1605")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1613")
    Jump("loc_1B63")

    label("loc_1613")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_1621")
    Jump("loc_1B63")

    label("loc_1621")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_1746")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16A4")

    #C0059
    ChrTalk(
        0xFE,
        "我将所有墓碑都打扫了一遍。\x02",
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0xFE,
        (
            "这么多的墓碑，\x01",
            "其中也有不少是无人打扫的。\x01",
            "……真是件可悲的事情呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1741")

    label("loc_16A4")


    #C0061
    ChrTalk(
        0xFE,
        (
            "这么多的墓碑，\x01",
            "其中也有不少是无人打扫的。\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0xFE,
        (
            "虽然不来扫墓的人大概都各有苦衷……\x01",
            "但这片寂寞的土地中有灵魂在沉睡着。\x01",
            "真希望大家平常能够抽时间来看看啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1741")

    Jump("loc_1B63")

    label("loc_1746")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_17D4")

    #C0063
    ChrTalk(
        0xFE,
        (
            "……就算是主日学校的孩子们，\x01",
            "也不太愿意接近墓地这种地方呢……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x153, 500)

    #C0064
    ChrTalk(
        0xFE,
        "哈哈哈，这位小姑娘真是特别啊。\x02",
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x153,
        "#1111F咦咦？\x02",
    )

    CloseMessageWindow()
    Jump("loc_1B63")

    label("loc_17D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_194B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_190D")

    #C0066
    ChrTalk(
        0xFE,
        "哎呀……带着一个没见过的孩子呢。\x02",
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x153,
        (
            "#1110F老爷爷。\x01",
            "你在这种地方做什么呢？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x153, 500)

    #C0068
    ChrTalk(
        0xFE,
        (
            "啊……我在守护沉睡于此的人们，\x01",
            "为了让他们\x01",
            "不被外界打扰。\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0xFE,
        (
            "不过，墓地被破坏之类的事件，\x01",
            "如今已经很少了。\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x153,
        "#1106F嗯……？\x02",
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0xFE,
        (
            "……呵呵呵，抱歉，\x01",
            "对小姑娘来说，这些话未免有些太难懂了吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1946")

    label("loc_190D")


    #C0072
    ChrTalk(
        0xFE,
        (
            "哈哈哈，以小姑娘的年纪来看，\x01",
            "不可能知道守墓的事吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1946")

    Jump("loc_1B63")

    label("loc_194B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_1959")
    Jump("loc_1B63")

    label("loc_1959")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_19FA")

    #C0073
    ChrTalk(
        0xFE,
        (
            "在互不侵犯条约签订之前，\x01",
            "曾经有很多人因战争而丧生。\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0xFE,
        (
            "那些成为牺牲品的人们的葬礼，\x01",
            "真的很令人揪心。\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0xFE,
        (
            "……我已经不想再体验\x01",
            "那种感觉了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B63")

    label("loc_19FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1A08")
    Jump("loc_1B63")

    label("loc_1A08")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1A16")
    Jump("loc_1B63")

    label("loc_1A16")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_1B4C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1ACE")

    #C0076
    ChrTalk(
        0xFE,
        "只有在主日学校的开课日我才能感到救赎。\x02",
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0xFE,
        (
            "因为那时，在这个寂寞的\x01",
            "地方也能够听见\x01",
            "孩子们的欢声笑语了。\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0xFE,
        (
            "不开课的日子里，这片墓地\x01",
            "真的是非常寂寥啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1B47")

    label("loc_1ACE")


    #C0079
    ChrTalk(
        0xFE,
        (
            "在主日学校开课日，\x01",
            "听见孩子们的欢闹声，\x01",
            "就有一种得到救赎的感觉。\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0xFE,
        (
            "在不开课的日子里，这片墓地\x01",
            "真的是非常寂寥啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B47")

    Jump("loc_1B63")

    label("loc_1B4C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_1B5A")
    Jump("loc_1B63")

    label("loc_1B5A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_1B63")

    label("loc_1B63")

    TalkEnd(0xFE)
    Return()

    # Function_5_15F4 end

    def Function_6_1B67(): pass

    label("Function_6_1B67")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1BD6")

    #C0081
    ChrTalk(
        0xFE,
        (
            "我只是偶然误入了这个\x01",
            "遍地墓碑的地方……\x01",
            "但这里的景色非常美丽呢～\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0xFE,
        "高处果然好啊。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_1C19")

    label("loc_1BD6")


    #C0083
    ChrTalk(
        0xFE,
        (
            "这里的视野很好，\x01",
            "空气也清新……\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0xFE,
        "也许算是个不错的地方呢～\x02",
    )

    CloseMessageWindow()

    label("loc_1C19")

    TalkEnd(0xFE)
    Return()

    # Function_6_1B67 end

    def Function_7_1C1D(): pass

    label("Function_7_1C1D")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50013.itc", 0x1E)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis009.itp")
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis010.itp")
    Sleep(500)
    SetChrName("声音")

    #A0085
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xC),
            "#30W──端坐于天国的吾之女神爱德丝啊。\x02\x03",

            "请为这个即将前往御座的灵魂，\x01",
            "敞开通往天国之门吧──\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    PlayBGM("ed7534", 0)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x7D0, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    Sleep(1500)
    SetChrName("声音")

    #A0086
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xC),
            "#30W（真不敢相信……\x01",
            "  那个一直精神健朗的家伙会……）\x02\x03",

            "（他还有个可爱的恋人，\x01",
            "　本以为他们都快要结婚了……\x01",
            "  ……为什么会发生这种事……）\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Sleep(150)
    SetChrName("声音")

    #A0087
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xC),
            "#30W（可恶……！\x01",
            "　警察们到底在干什么啊！？）\x02\x03",

            "（自己人都被杀了！？\x01",
            "　难道还打算让真相不明不白吗！？）\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Sleep(150)
    SetChrName("声音")

    #A0088
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xC),
            "#30W（他的父母好像……\x01",
            "　都已经去世了吧？）\x02\x03",

            "（他的弟弟该怎么办呢……）\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x3E8, 0x0)
    OP_CA(0x0, 0x1, 0x3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x0, 0x0)
    Sleep(800)
    SetChrName("女性")

    #A0089
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xC),
            "#30W……没关系吧，罗伊德？\x02\x03",

            "不要勉强自己哦，\x01",
            "最近都没有怎么休息吧？\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0090
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xC),
            "#30W……塞茜尔姐姐才是呢。\x02\x03",

            "麻烦你帮了那么多忙，真是抱歉。\x01",
            "本来，这必须是要由\x01",
            "我一人承担的……\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrName("女性")

    #A0091
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xC),
            "#30W……别说得那么见外。\x01",
            "我们不是一直都像家人一样吗？\x02\x03",

            "#40W另外……盖伊对\x01",
            "我来说也……\x02\x03",

            "#40W……………………………………………\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0092
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xC),
            "#30W………塞茜尔姐姐………………\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrName("女性")

    #A0093
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xC),
            "#30W……对不起哦，\x01",
            "最痛苦的明明是罗伊德。\x02\x03",

            "这之后的日子可能会有些艰难，\x01",
            "不要客气，尽量依靠我吧……\x02\x03",

            "在你能够独立之前，\x01",
            "我一定会好好守护你的……\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x1, 0x3, 0xFFFFFF, 0x7D0, 0x0)
    OP_CA(0x0, 0x1, 0x3)
    OP_68(11000, 1500, 18800, 0)
    MoveCamera(312, 11, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(30500, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x2)
    SetChrPos(0x101, -23000, 0, 24500, 0)
    SetChrChipByIndex(0xB, 0x1E)
    SetChrSubChip(0xB, 0x2)
    SetChrFlags(0xB, 0x8000)
    SetChrPos(0xB, -23000, 0, 25500, 0)
    MoveCamera(322, 13, 0, 6000)
    SetCameraDistance(37500, 6000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x50)
    Fade(1000)
    OP_68(-23300, 600, 21800, 0)
    MoveCamera(315, 18, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16000, 0)
    OP_68(-23300, 600, 25800, 4000)
    SetCameraDistance(15500, 4000)
    OP_6F(0x11)

    #C0094
    ChrTalk(
        0x101,
        (
            "#6P#0008F……………………………………\x02\x03",

            "#0004F……哈哈，\x01",
            "我那时还真是个小孩啊。\x02\x03",

            "明明坦率地依靠塞茜尔姐姐就好了，\x01",
            "……却在那里逞强……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(300)
    Fade(250)
    SetChrSubChip(0x101, 0x1)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    Sound(46, 0, 100, 0)
    OP_0D()
    Sleep(500)

    #C0095
    ChrTalk(
        0x101,
        (
            "#6P#0003F（──大哥，我回来了。）\x02\x03",

            "#0008F（抱歉，现在才来看你。\x01",
            "　因为我好像有点逞强呢。）\x02\x03",

            "#0002F（但是我……已经回来了。）\x02\x03",

            "（作为和大哥一样的搜查官，\x01",
            "　回克洛斯贝尔来了。）\x02\x03",

            "#0004F（虽然还远不能算是独当一面……\x01",
            "　……而且还被分配到了\x01",
            "　奇怪的部门……）\x02\x03",

            "#0000F（但我还是会尽量努力的，\x01",
            "　就拜托你守护我了。）\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(16500, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    StopBGM(0xFA0)
    WaitBGM()
    ClearChrFlags(0x101, 0x20)
    ClearChrFlags(0x101, 0x2)
    SetChrSubChip(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    OP_CA(0x1, 0xFF, 0x0)
    SetScenarioFlags(0x5C, 1)
    NewScene("c0110", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_7_1C1D end

    def Function_8_23DF(): pass

    label("Function_8_23DF")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0096
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            "生于钟下的羔羊们\x01",
            "　　请安息吧\x02",
        )
    )

    CloseMessageWindow()

    #A0097
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            "纯白云间洒下的金色阳光\x01",
            " 将成为连接苍穹的大道\x01",
            "引导汝之灵魂至女神座前\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_8_23DF end

    def Function_9_2482(): pass

    label("Function_9_2482")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0098
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            "　　    盖伊·班宁斯\x01",
            "　　　    沉睡于此\x01",
            "───────────────\x01",
            "　Ｓ１１７６　～　Ｓ１２０１　\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2554")

    #C0099
    ChrTalk(
        0x101,
        "#6P#0008F……………………………………\x02",
    )

    CloseMessageWindow()

    label("loc_2554")

    TalkEnd(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_28B0")
    Sleep(150)
    EventBegin(0x0)
    StopBGM(0x7D0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    WaitBGM()
    SetChrPos(0x101, -22900, 0, 24540, 0)
    SetChrPos(0x102, -23050, 0, 21800, 0)
    SetChrPos(0x103, -21380, 0, 22100, 350)
    SetChrPos(0x104, -24580, 0, 22100, 0)
    OP_68(-22960, 2500, 24900, 0)
    MoveCamera(334, 18, 0, 0)
    OP_6E(560, 0)
    SetCameraDistance(14810, 0)
    Sleep(10)
    PlayBGM("ed7001", 0)
    FadeToBright(1000, 0)
    OP_68(-22960, 1500, 24900, 3000)
    OP_0D()
    OP_6F(0x79)

    #C0100
    ChrTalk(
        0x101,
        (
            "#6P#0003F（大哥的徽章……\x01",
            "　终于拿回来了。）\x02\x03",

            "（……这样的话，\x01",
            "　总算有希望给大哥报仇了……）\x02\x03",

            "#0008F（但是……抱歉，现在还是\x01",
            "　先让我集中精神，应对眼前的事件吧。）\x02\x03",

            "（最近，不断有市民因为某种违禁药物而失踪……\x01",
            "　前所未有的大事件\x01",
            "　似乎就要在克洛斯贝尔发生了。）\x02\x03",

            "#0001F（大哥你也绝对不会\x01",
            "　坐视不管吧……）\x02\x03",

            "#0004F（……我虽然还远远不够成熟，\x01",
            "　但还有艾莉、缇欧和兰迪……\x01",
            "　这些可靠的伙伴都陪伴在我的身边。）\x02\x03",

            "（还有……我已经找到了\x01",
            "　无论如何都想要守护的存在。）\x02\x03",

            "#0000F（所以大哥……\x01",
            "　请安心守护我吧！）\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0x102,
        "#0105F……罗伊德？\x02",
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x104,
        "#0300F哈哈……怎么了？\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0xB4, 0x1F4)

    #C0103
    ChrTalk(
        0x101,
        (
            "#0004F#11P……不，没什么。\x02\x03",

            "#0000F好了，各位……我们走吧！\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0x103,
        "#0202F#2P………是……！\x02",
    )

    CloseMessageWindow()
    OP_5A()
    SetScenarioFlags(0xE7, 1)
    EventEnd(0x5)

    label("loc_28B0")

    Return()

    # Function_9_2482 end

    def Function_10_28B1(): pass

    label("Function_10_28B1")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0105
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            "　　　  纱绫·马克莱因\x01",
            "　　　　　 沉睡于此\x01",
            "───────────────\x01",
            "　Ｓ１１７５　～　Ｓ１１９９　\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    TalkEnd(0xFF)
    Return()

    # Function_10_28B1 end

    def Function_11_2955(): pass

    label("Function_11_2955")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0106
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            "　………………　……　　　　　\x01",
            "　……　……………………\x01",
            "　　　　　沉……于……\x01",
            "───────────────……\x01",
            "　Ｓ１………　～　Ｓ１…８…　\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A2D")
    SetScenarioFlags(0x0, 2)
    ClearScenarioFlags(0x0, 0)

    label("loc_2A2D")

    TalkEnd(0xFF)
    Return()

    # Function_11_2955 end

    def Function_12_2A31(): pass

    label("Function_12_2A31")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    OP_68(4760, 5200, 45880, 0)
    MoveCamera(339, 17, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(19410, 0)
    LoadChrToIndex("apl/ch50387.itc", 0x32)
    LoadEffect(0x0, "event\\eva02_00.eff")
    SetChrPos(0x101, 7090, 4000, 45490, 320)
    SetChrPos(0x102, 5840, 4000, 45440, 320)
    SetChrPos(0x103, 6560, 4000, 43510, 320)
    SetChrPos(0x104, 5070, 4000, 43640, 320)
    FadeToBright(500, 0)
    OP_0D()

    #C0107
    ChrTalk(
        0x104,
        (
            "#6P#0305F哎呀……真危险呢，\x01",
            "连个防护栏都没有啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0x101,
        (
            "#12P#0003F因为根本就不会有人\x01",
            "站在这种悬崖边吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0x102,
        (
            "#6P#0105F从这里看……\x01",
            "谷底相当的深啊。\x02\x03",

            "#0103F一直盯着看的话，\x01",
            "感觉仿佛会被\x01",
            "吸入其中一样。\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0x103,
        (
            "#12P#0200F这里是墓地……\x01",
            "死者长眠的地方。\x02\x03",

            "#0204F说不定\x01",
            "是有人在另一个世界\x01",
            "召唤我们过去呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0x102,
        (
            "#6P#0105F缇、缇欧你真是的，\x01",
            "别说那么可怕的事啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0x101,
        (
            "#12P#0003F总、总之……\x02\x03",

            "#0000F格蕾丝小姐委托我们拍摄的照片，\x01",
            "在这里似乎能拍到很不错的呢。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x3)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x5)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x6)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x7)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x9)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0xA)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3227")
    TurnDirection(0x101, 0x102, 500)

    #C0113
    ChrTalk(
        0x101,
        (
            "#12P#0000F那么艾莉，\x01",
            "可以拜托你来拍照吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)

    #C0114
    ChrTalk(
        0x102,
        (
            "#6P#0108F哎，好的。\x01",
            "虽然我没什么自信……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x102, 500)

    #C0115
    ChrTalk(
        0x104,
        (
            "#12P#0300F哪里哪里，应该没问题吧。\x02\x03",

            "只要看看镜头，\x01",
            "然后咔嚓一下拍下来\x01",
            "不就搞定了嘛。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x104, 500)

    #C0116
    ChrTalk(
        0x102,
        (
            "#6P#0103F我说你啊……\x01",
            "要拍出好照片，\x01",
            "可没有那么简单哦。\x02\x03",

            "#0100F要注意确认\x01",
            "拍摄对象有没有被收入取景框中，\x01",
            "还要构思摄影角度……\x02\x03",

            "而且受到天气和风的影响，\x01",
            "照片所呈现出的感觉也会有很大不同。\x02\x03",

            "有时只要错过那一瞬的时机，\x01",
            "就再也拍不到\x01",
            "那么好的风景了。\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0x103,
        (
            "#12P#0200F外行和专家所拍出的照片，\x01",
            "差别可是一目了然的。\x02\x03",

            "#0203F不过，某些粗神经的人\x01",
            "大概无法理解这种细致的工作吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x103, 500)

    #C0118
    ChrTalk(
        0x104,
        (
            "#6P#0306F唔……\x01",
            "你在说谁啊，说谁啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0x101,
        (
            "#12P#0000F好啦好啦，\x01",
            "总之就交给艾莉吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0x102,
        (
            "#6P#0100F那么……\x01",
            "我来试试看吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_93(0x102, 0x12C, 0x1F4)
    OP_93(0x101, 0x12C, 0x1F4)
    OP_93(0x103, 0x12C, 0x1F4)
    OP_93(0x104, 0x12C, 0x1F4)
    Fade(1000)
    SetChrChipByIndex(0x102, 0x32)
    SetChrSubChip(0x102, 0x0)
    OP_0D()
    Sound(817, 0, 100, 0)
    PlayEffect(0x0, 0xFF, 0x102, 0xC0, 0, 1200, 400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    Sound(817, 0, 100, 0)
    PlayEffect(0x0, 0xFF, 0x102, 0xC0, 0, 1200, 400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    Sound(817, 0, 100, 0)
    PlayEffect(0x0, 0xFF, 0x102, 0xC0, 0, 1200, 400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)

    #C0121
    ChrTalk(
        0x102,
        (
            "#6P#0103F……呼，\x01",
            "为了保险起见，我多拍了几张。\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0x101,
        (
            "#12P#0000F看样子，似乎已经拍好了呢。\x02\x03",

            "感觉怎么样啊？\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0x102,
        (
            "#6P#0100F在没有实际显像出来之前，\x01",
            "还无法确定……\x02\x03",

            "不过，我觉得至少\x01",
            "不会很差吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0x103,
        (
            "#12P#0200F艾莉前辈似乎\x01",
            "找回感觉了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0x104,
        (
            "#6P#0300F哼……\x01",
            "反正只有我完全搞不懂。\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0x101,
        (
            "#12P#0000F如果发现了这种风景漂亮的地方，\x01",
            "就再拍些照片吧。\x02\x03",

            "那么，我们走吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3534")

    label("loc_3227")

    TurnDirection(0x101, 0x102, 500)

    #C0127
    ChrTalk(
        0x101,
        (
            "#12P#0000F那么……\x01",
            "艾莉，麻烦你拍照了哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0x102,
        "#6P#0100F嗯，知道了。\x02",
    )

    CloseMessageWindow()
    OP_5A()
    OP_93(0x102, 0x12C, 0x1F4)
    OP_93(0x101, 0x12C, 0x1F4)
    OP_93(0x103, 0x12C, 0x1F4)
    OP_93(0x104, 0x12C, 0x1F4)
    Fade(1000)
    SetChrChipByIndex(0x102, 0x32)
    SetChrSubChip(0x102, 0x0)
    OP_0D()
    Sound(817, 0, 100, 0)
    PlayEffect(0x0, 0xFF, 0x102, 0xC0, 0, 1200, 400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    Sound(817, 0, 100, 0)
    PlayEffect(0x0, 0xFF, 0x102, 0xC0, 0, 1200, 400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    Sound(817, 0, 100, 0)
    PlayEffect(0x0, 0xFF, 0x102, 0xC0, 0, 1200, 400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)

    #C0129
    ChrTalk(
        0x102,
        (
            "#6P#0103F……呼，\x01",
            "大概就这样吧。\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x2)"), scpexpr(EXPR_END)), "loc_33AA")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_33AA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x3)"), scpexpr(EXPR_END)), "loc_33C1")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_33C1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x4)"), scpexpr(EXPR_END)), "loc_33D8")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_33D8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x5)"), scpexpr(EXPR_END)), "loc_33EF")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_33EF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x6)"), scpexpr(EXPR_END)), "loc_3406")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3406")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x7)"), scpexpr(EXPR_END)), "loc_341D")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_341D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x8)"), scpexpr(EXPR_END)), "loc_3434")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3434")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x9)"), scpexpr(EXPR_END)), "loc_344B")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_344B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0xA)"), scpexpr(EXPR_END)), "loc_3462")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3462")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_34F3")

    #C0130
    ChrTalk(
        0x101,
        (
            "#12P#0000F辛苦了，\x01",
            "看来已经顺利拍好了啊。\x02\x03",

            "这样一来，就拍完了格蕾丝小姐\x01",
            "所要求的五张照片了。\x01",
            "现在随时都可以去交付了啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3534")

    label("loc_34F3")


    #C0131
    ChrTalk(
        0x101,
        (
            "#12P#0000F辛苦了，\x01",
            "看来已经顺利拍好了啊。\x02\x03",

            "那么，我们走吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3534")

    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, 5840, 4000, 45440, 320)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    OP_D5(0x32)
    OP_29(0x18, 0x1, 0x5)
    Sleep(500)
    OP_65(0x2, 0x1)
    EventEnd(0x5)
    Return()

    # Function_12_2A31 end

    def Function_13_356A(): pass

    label("Function_13_356A")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(21970, 1500, 30960, 0)
    MoveCamera(315, 30, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17000, 0)
    SetChrPos(0x101, 21500, 0, 30200, 0)
    SetChrPos(0x102, 20300, 0, 30200, 0)
    SetChrPos(0x103, 21500, 0, 29000, 0)
    SetChrPos(0x104, 20300, 0, 29000, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3613")
    SetChrPos(0x10A, 22710, 0, 29860, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    label("loc_3613")

    SetChrPos(0x9, 20830, 0, 32299, 0)
    ClearChrFlags(0x9, 0x80)
    BeginChrThread(0x9, 0, 0, 0)
    OP_4B(0x9, 0xFF)
    SetChrSubChip(0x9, 0x0)
    SetChrChipByIndex(0xB, 0x2)
    SetChrFlags(0xB, 0x8000)
    SetChrPos(0xB, -23000, 0, 25500, 0)
    SetCameraDistance(16000, 3000)
    FadeToBright(500, 0)
    OP_0D()
    OP_6F(0x79)
    Fade(500)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    Sound(46, 0, 100, 0)
    OP_0D()
    Sleep(1000)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0132
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            "　　　  纱绫·马克莱因\x01",
            "　　　　　 沉睡于此\x01",
            "───────────────\x01",
            "　Ｓ１１７５　～　Ｓ１１９９　\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()

    #C0133
    ChrTalk(
        0x101,
        "#6P#0005F（这块墓碑……）\x02",
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0x102,
        "#6P#0105F（是亚里欧斯先生的夫人……？）\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_379C")

    #C0135
    ChrTalk(
        0x10A,
        "#12P#0608F（……………………）\x02",
    )

    CloseMessageWindow()

    label("loc_379C")

    OP_63(0x9, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0x9)

    #C0136
    ChrTalk(
        0x9,
        "#11P……接下来是这里。\x02",
    )

    CloseMessageWindow()

    def lambda_37D5():
        OP_95(0xFE, 24000, 0, 32299, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_37D5)
    WaitChrThread(0x9, 1)

    def lambda_37F3():
        OP_95(0xFE, 24000, 0, 29000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_37F3)
    FadeToDark(1000, 0, -1)
    OP_0D()
    WaitChrThread(0x9, 1)
    OP_68(13470, 5500, 33550, 0)
    MoveCamera(315, 23, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16200, 0)
    SetChrPos(0x101, 13200, 4000, 33300, 0)
    SetChrPos(0x102, 12000, 4000, 33300, 0)
    SetChrPos(0x103, 13200, 4000, 32100, 0)
    SetChrPos(0x104, 12000, 4000, 32100, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_38AA")
    SetChrPos(0x10A, 14210, 4000, 32460, 0)

    label("loc_38AA")

    SetChrPos(0x9, 12330, 4000, 35000, 0)
    ClearChrFlags(0x9, 0x80)
    BeginChrThread(0x9, 0, 0, 0)
    OP_4B(0x9, 0xFF)
    SetChrSubChip(0x9, 0x0)
    SetCameraDistance(15200, 3000)
    FadeToBright(500, 0)
    OP_0D()
    OP_6F(0x79)
    Fade(500)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    Sound(46, 0, 100, 0)
    OP_0D()
    Sleep(1000)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0137
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            "　………………　……　　　　　\x01",
            "　……　……………………\x01",
            "　　　　　沉……于……\x01",
            "───────────────……\x01",
            "　Ｓ１………　～　Ｓ１…８…　\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()

    #C0138
    ChrTalk(
        0x104,
        (
            "#6P#0303F（好破旧的墓碑……\x01",
            "  姓名之类的地方基本已经模糊不清了。）\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0x103,
        "#6P#0200F（是他的……熟人吧。）\x02",
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0x9,
        "#11P……下一个就是最后的了。\x02",
    )

    CloseMessageWindow()

    def lambda_3A55():
        OP_95(0xFE, 10300, 4000, 35000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_3A55)
    WaitChrThread(0x9, 1)

    def lambda_3A73():
        OP_95(0xFE, 10300, 4000, 33300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_3A73)
    FadeToDark(1000, 0, -1)
    OP_0D()
    WaitChrThread(0x9, 1)
    OP_68(-21390, 1500, 21840, 0)
    MoveCamera(315, 23, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17000, 0)
    SetChrPos(0x101, -21500, 0, 21800, 0)
    SetChrPos(0x102, -22700, 0, 21800, 0)
    SetChrPos(0x103, -21500, 0, 20600, 0)
    SetChrPos(0x104, -22700, 0, 20600, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3B2A")
    SetChrPos(0x10A, -20400, 0, 20980, 0)

    label("loc_3B2A")

    SetChrPos(0x9, -22460, 0, 23700, 0)
    ClearChrFlags(0x9, 0x80)
    BeginChrThread(0x9, 0, 0, 0)
    OP_4B(0x9, 0xFF)
    SetChrSubChip(0x9, 0x0)
    SetCameraDistance(16000, 3000)
    FadeToBright(500, 0)
    OP_0D()
    Sleep(1000)
    OP_6F(0x79)

    #C0141
    ChrTalk(
        0x101,
        "#6P#0005F这、这里是……\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    Sound(46, 0, 100, 0)
    OP_0D()
    Sleep(1000)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0142
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            "　　　   盖伊·班宁斯\x01",
            "　　　　   沉睡于此\x01",
            "───────────────\x01",
            "　Ｓ１１７６　～　Ｓ１２０１　\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0143
    ChrTalk(
        0x104,
        "#5P#0305F难道这里是……\x02",
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0x102,
        "#5P#0105F罗伊德的哥哥……\x02",
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0x103,
        "#6P#0208F……………………\x02",
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0x9,
        "#11P……我之所以拜托你们收集三色花……\x02",
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0x9,
        (
            "#11P是为了献给盖伊·班宁斯……\x01",
            "以及献给他\x01",
            "所珍视的人们。\x02",
        )
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0x9,
        (
            "#11P他是我最重要的朋友……\x01",
            "不管是不是葬礼，也都应该表达\x01",
            "自己最大的敬意，这是理所当然的吧？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3DDB")

    #C0149
    ChrTalk(
        0x10A,
        (
            "#12P#0603F……老人家，\x01",
            "您认识那个男人吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E0C")

    label("loc_3DDB")


    #C0150
    ChrTalk(
        0x101,
        (
            "#6P#0005F老爷爷……\x01",
            "您认识\x01",
            "盖伊·班宁斯吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3E0C")

    OP_93(0x9, 0xB4, 0x1F4)

    #C0151
    ChrTalk(
        0x9,
        (
            "#11P嗯，别说是认识了，\x01",
            "他根本就是我一辈子都不会忘记的人。\x02",
        )
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0x9,
        (
            "#11P盖伊生前\x01",
            "常来守墓的小屋玩。\x02",
        )
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0x9,
        (
            "#11P是经常与我一起\x01",
            "小酌几杯的酒友。\x02",
        )
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0x9,
        (
            "#11P因此，我这个没有家人的老头子的心灵\x01",
            "不知道被拯救了多少次。\x02",
        )
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0x101,
        "#6P#0003F原来是这样……\x02",
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0x103,
        "#6P#0203F……我觉得自己能够明白这种心情。\x02",
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0x9,
        (
            "#11P……因此在参加那家伙的葬礼时，\x01",
            "简直是撕心裂肺般地难受。\x02",
        )
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0x9,
        (
            "#11P你是叫……罗伊德吧，\x01",
            "你应该是盖伊的弟弟吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0159
    ChrTalk(
        0x101,
        "#6P#0005F您、您连我都知道吗？\x02",
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0x9,
        "#11P我在盖伊的葬礼上曾经见过你一次。\x02",
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0x9,
        (
            "#11P四个月前，\x01",
            "看到克洛斯贝尔时代周刊上刊载的\x01",
            "照片之后，就想起来了。\x02",
        )
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0x9,
        (
            "#11P呵呵，虽然长得不太像，\x01",
            "但这样看来，还有点盖伊的影子呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0x101,
        (
            "#6P#0012F哈哈……\x01",
            "但比起哥哥，我还差得太远了。\x02",
        )
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0x102,
        "#5P#0108F罗伊德……\x02",
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0x9,
        (
            "#11P……这次向你们提出收集三色花\x01",
            "这么麻烦的委托，还有另一个理由。\x02",
        )
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0x9,
        (
            "#11P那就是我想亲眼确认一下，看看身为\x01",
            "盖伊后辈的你们是否成长起来了。\x02",
        )
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0x104,
        (
            "#5P#0300F那么……\x01",
            "我们合格了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0x9,
        (
            "#11P虽然完成了任务……\x01",
            "但是从各方面来看都还不成熟，\x01",
            "算不上是独当一面呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0x104,
        "#5P#0306F说、说得真直接……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_424C")

    #C0170
    ChrTalk(
        0x10A,
        "#12P#0603F……这对小鬼来说是理所当然的评价。\x02",
    )

    CloseMessageWindow()

    label("loc_424C")


    #C0171
    ChrTalk(
        0x9,
        (
            "#11P哈哈哈，但是……\x01",
            "你们这些年轻人要走的路还很长。\x02",
        )
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0x9,
        (
            "#11P说不定哪天就会成长到能赶上，\x01",
            "甚至是超越盖伊呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0x9,
        (
            "#11P如果那一天到来的话……\x01",
            "就来这里玩吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0x9,
        (
            "#11P就像过去盖伊所做的一样，\x01",
            "和我一起喝酒吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0x101,
        (
            "#6P#0004F……嗯，一定会的，\x01",
            "我期待着那天的到来。\x02",
        )
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0x102,
        (
            "#5P#0100F罗伊德……\x01",
            "你的哥哥\x01",
            "活在很多人的心中呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0x103,
        (
            "#6P#0202F……是啊。\x02\x03",

            "#0204F（没错，也活在我的心中……）\x02",
        )
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0x104,
        (
            "#5P#0306F要想追上这个目标，\x01",
            "似乎要花不少时间啊。\x02\x03",

            "#0309F从某种意义上说，这也许是一道\x01",
            "比黑手党啊、扭曲的制度什么的\x01",
            "更加难以越过的壁障呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0x101,
        (
            "#6P#0004F是啊……我也那么觉得。\x02\x03",

            "#0001F（即使如此，总有一天……\x01",
            "　我也必须要跨越过去。）\x02",
        )
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0x9,
        (
            "#11P呵呵，话说得太多了，\x01",
            "差不多该回屋子里去了。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    NewScene("t4020", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_13_356A end

    SaveToFile()

Try(main)
