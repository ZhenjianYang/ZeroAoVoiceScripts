from ScenarioHelper import *

def main():
    CreateScenaFile(
        "t1080.bin",                # FileName
        "t1080",                    # MapName
        "t1080",                    # Location
        0x0042,                     # MapIndex
        "ed7565",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x1A,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 66, 0, 2, 0, 3],
    )

    BuildStringList((
        "t1080",                  # 0
        "茜特拉丝",               # 1
        "佐尔克",                 # 2
        "琪雅",                   # 3
        "芙兰",                   # 4
        "塞茜尔",                 # 5
        "伊莉娅",                 # 6
        "莉夏",                   # 7
        "修利",                   # 8
        "艾莉",                   # 9
        "缇欧",                   # 10
        "诺艾尔",                 # 11
        "蔡特",                   # 12
        "玛丽亚贝尔",             # 13
    ))

    AddCharChip((
        "chr/ch08200.itc",                   # 00
        "chr/ch08500.itc",                   # 01
        "chr/ch05200.itc",                   # 02
        "chr/ch05100.itc",                   # 03
        "chr/ch07500.itc",                   # 04
        "chr/ch10000.itc",                   # 05
        "chr/ch00100.itc",                   # 06
        "chr/ch00200.itc",                   # 07
        "chr/ch02900.itc",                   # 08
        "chr/ch25600.itc",                   # 09
        "chr/ch25900.itc",                   # 0A
        "chr/ch02707.itc",                   # 0B
        "chr/ch05202.itc",                   # 0C
        "chr/ch10002.itc",                   # 0D
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
        "chr/ch00000.itc",                   # 1C
        "chr/ch00000.itc",                   # 1D
    ))

    DeclNpc(106129,  0,       11579,   0,    385,  0x0, 0,   9,   0,   0,   1,   0,   16,  255,  0)
    DeclNpc(-14840,  0,       6570,    90,   385,  0x0, 0,   10,  0,   0,   0,   0,   18,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   1,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   4,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   3,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   2,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   5,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   6,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   7,   0,   0,   0,   0,   14,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   8,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(569,     0,       1809,    135,  389,  0x0, 0,   11,  0,   0,   0,   0,   13,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclActor(-13250,  0,       6540,    1500,    -14840,  1500,    6570,    0x007E, 0,  17, 0x0000)

    ChipFrameInfo(804, 0)                                        # 0

    ScpFunction((
        "Function_0_324",          # 00, 0
        "Function_1_3DC",          # 01, 1
        "Function_2_43D",          # 02, 2
        "Function_3_62A",          # 03, 3
        "Function_4_661",          # 04, 4
        "Function_5_86F",          # 05, 5
        "Function_6_C1B",          # 06, 6
        "Function_7_10DC",         # 07, 7
        "Function_8_1343",         # 08, 8
        "Function_9_14E2",         # 09, 9
        "Function_10_1769",        # 0A, 10
        "Function_11_183B",        # 0B, 11
        "Function_12_1B28",        # 0C, 12
        "Function_13_1C9F",        # 0D, 13
        "Function_14_1E4A",        # 0E, 14
        "Function_15_1F4D",        # 0F, 15
        "Function_16_20D5",        # 10, 16
        "Function_17_222A",        # 11, 17
        "Function_18_222E",        # 12, 18
        "Function_19_23A1",        # 13, 19
        "Function_20_3371",        # 14, 20
        "Function_21_3381",        # 15, 21
        "Function_22_3391",        # 16, 22
        "Function_23_33A1",        # 17, 23
        "Function_24_33B1",        # 18, 24
        "Function_25_33DF",        # 19, 25
        "Function_26_341C",        # 1A, 26
        "Function_27_3459",        # 1B, 27
        "Function_28_3496",        # 1C, 28
        "Function_29_34D3",        # 1D, 29
        "Function_30_3510",        # 1E, 30
        "Function_31_355C",        # 1F, 31
        "Function_32_35A8",        # 20, 32
        "Function_33_35F4",        # 21, 33
    ))


    def Function_0_324(): pass

    label("Function_0_324")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_364"),
        (1, "loc_370"),
        (2, "loc_37C"),
        (3, "loc_388"),
        (4, "loc_394"),
        (5, "loc_3A0"),
        (6, "loc_3AC"),
        (SWITCH_DEFAULT, "loc_3B8"),
    )


    label("loc_364")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_3C4")

    label("loc_370")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_3C4")

    label("loc_37C")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_3C4")

    label("loc_388")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_3C4")

    label("loc_394")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_3C4")

    label("loc_3A0")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_3C4")

    label("loc_3AC")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_3C4")

    label("loc_3B8")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_3C4")

    label("loc_3C4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3DB")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_3C4")

    label("loc_3DB")

    Return()

    # Function_0_324 end

    def Function_1_3DC(): pass

    label("Function_1_3DC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_43C")
    OP_95(0xFE, 106130, 0, 11580, 2000, 0x0)
    OP_95(0xFE, 106130, 0, 8150, 2000, 0x0)
    OP_95(0xFE, 94190, 0, 8150, 2000, 0x0)
    OP_95(0xFE, 94190, 0, 11580, 2000, 0x0)
    Jump("Function_1_3DC")

    label("loc_43C")

    Return()

    # Function_1_3DC end

    def Function_2_43D(): pass

    label("Function_2_43D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_44B")
    Jump("loc_5F1")

    label("loc_44B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_45E")
    ClearChrFlags(0x9, 0x80)
    Jump("loc_5F1")

    label("loc_45E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_4F8")
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 5850, 0, 4400, 45)
    SetChrFlags(0xF, 0x10)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 6560, 0, 5100, 225)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4A7")
    SetChrFlags(0x11, 0x10)

    label("loc_4A7")

    SetChrChipByIndex(0xE, 0xC)
    SetChrSubChip(0xE, 0x0)
    EndChrThread(0xE, 0x0)
    SetChrBattleFlags(0xE, 0x4)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 97700, 150, 124100, 90)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, 4800, 0, 6050, 135)
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x13, 0x10)
    ClearChrFlags(0x9, 0x80)
    Jump("loc_5F1")

    label("loc_4F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_506")
    Jump("loc_5F1")

    label("loc_506")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_5F1")
    SetChrChipByIndex(0xF, 0xD)
    SetChrSubChip(0xF, 0x0)
    EndChrThread(0xF, 0x0)
    SetChrBattleFlags(0xF, 0x4)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 104060, 500, 118180, 0)
    SetChrChipByIndex(0xE, 0xC)
    SetChrSubChip(0xE, 0x0)
    EndChrThread(0xE, 0x0)
    SetChrBattleFlags(0xE, 0x4)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 104060, 500, 119880, 180)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 99230, 0, -80380, 90)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 100220, 0, -80390, 270)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15A, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_59D")
    SetChrFlags(0xD, 0x10)
    SetChrFlags(0xC, 0x10)

    label("loc_59D")

    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, -100940, 0, 121230, 90)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, -99810, 0, 121220, 270)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5DD")
    SetChrFlags(0xB, 0x10)
    SetChrFlags(0x12, 0x10)

    label("loc_5DD")

    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x13, 0x10)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)

    label("loc_5F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_605")
    ClearScenarioFlags(0x22, 0)
    Event(0, 19)
    Jump("loc_617")

    label("loc_605")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_617")
    ClearScenarioFlags(0x22, 1)
    SetScenarioFlags(0x0, 0)
    Event(0, 33)

    label("loc_617")

    OP_65(0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_629")
    OP_66(0x0, 0x1)

    label("loc_629")

    Return()

    # Function_2_43D end

    def Function_3_62A(): pass

    label("Function_3_62A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_63F")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 0)

    label("loc_63F")

    OP_52(0x13, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_3_62A end

    def Function_4_661(): pass

    label("Function_4_661")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_672")
    Jump("loc_86B")

    label("loc_672")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_680")
    Jump("loc_86B")

    label("loc_680")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_68E")
    Jump("loc_86B")

    label("loc_68E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_69C")
    Jump("loc_86B")

    label("loc_69C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_6F8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6B7")
    Call(0, 15)
    Jump("loc_6F3")

    label("loc_6B7")


    #C0001
    ChrTalk(
        0xF,
        (
            "#04205F怎、怎么了……\x02\x03",

            "#04206F我说了什么不该说的话吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6F3")

    Jump("loc_86B")

    label("loc_6F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_706")
    Jump("loc_86B")

    label("loc_706")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_86B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15A, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_721")
    Call(0, 6)
    Jump("loc_86B")

    label("loc_721")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_823")

    #C0002
    ChrTalk(
        0xF,
        (
            "#04206F呼，我有生以来\x01",
            "还从来没有游过泳。\x02\x03",

            "#04208F虽然莉夏姐会指点我，\x01",
            "但万一要是溺水了，可该怎么办啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0x104,
        (
            "#00309F哈哈，你竟然会怕这种事，\x01",
            "倒也有一些可爱之处嘛，\x01",
            "阿修。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0xF,
        (
            "#04201F啊啊，真烦人！\x01",
            "非叫阿修就叫吧，\x01",
            "能不能快闪一边去！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_86B")

    label("loc_823")


    #C0005
    ChrTalk(
        0xF,
        (
            "#04206F我有生以来还从来没有游过泳。\x02\x03",

            "#04208F要是溺水可怎么办啊……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_86B")

    TalkEnd(0xFE)
    Return()

    # Function_4_661 end

    def Function_5_86F(): pass

    label("Function_5_86F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_880")
    Jump("loc_C17")

    label("loc_880")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_88E")
    Jump("loc_C17")

    label("loc_88E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_89C")
    Jump("loc_C17")

    label("loc_89C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_8B9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15A, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8B4")
    Jump("loc_8B4")

    label("loc_8B4")

    Jump("loc_C17")

    label("loc_8B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_A5B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A17")

    #C0006
    ChrTalk(
        0xE,
        "#01802F啊……罗伊德警官。\x02",
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x101,
        (
            "#00005F哦，是莉夏啊，\x01",
            "你怎么还在房间里。\x02\x03",

            "#00000F我还以为你已经和\x01",
            "艾莉她们一起去\x01",
            "逛时装店了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0xE,
        (
            "#01809F哈哈，我在沙滩上\x01",
            "玩得有点累。\x02\x03",

            "#01802F先休息一下，\x01",
            "过一会再去逛。\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x101,
        (
            "#00005F这样啊……\x02\x03",

            "#00002F反正离我们在主题公园\x01",
            "集合的时间还早，\x01",
            "你不用太着急。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0xE,
        "#01809F好的，谢谢关心。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_A56")

    label("loc_A17")


    #C0011
    ChrTalk(
        0xE,
        (
            "#01800F小琪雅没有\x01",
            "来过我这里。\x02\x03",

            "说不定她已经离开\x01",
            "酒店了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A56")

    Jump("loc_C17")

    label("loc_A5B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_A69")
    Jump("loc_C17")

    label("loc_A69")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_C17")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15A, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A84")
    Call(0, 6)
    Jump("loc_C17")

    label("loc_A84")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B94")

    #C0012
    ChrTalk(
        0xE,
        (
            "#01803F老实说，像我这种演技尚未成熟的新人，\x01",
            "本不该将时间用于玩乐……\x02\x03",

            "#01802F但伊莉娅小姐说，\x01",
            "对演员而言，休息也很重要。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x101,
        (
            "#00004F伊莉娅小姐说的很对。\x02\x03",

            "#00000F难得来玩一次，你就转换心情，\x01",
            "彻底放松一下吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0xE,
        "#01800F呵呵……嗯，我会尽情享受的。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_C17")

    label("loc_B94")


    #C0015
    ChrTalk(
        0xE,
        (
            "#01804F还是先从最基本的游泳方法开始，\x01",
            "循序渐进地教她吧。\x02\x03",

            "#01803F只要记住了基本要领，\x01",
            "修利就一定可以凭借\x01",
            "自己的天赋练好游泳。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C17")

    TalkEnd(0xFE)
    Return()

    # Function_5_86F end

    def Function_6_C1B(): pass

    label("Function_6_C1B")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xE, 0x10)
    TurnDirection(0xE, 0x0, 0)
    OP_52(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_CAC")
    Jump("loc_CF6")

    label("loc_CAC")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_CCC")
    OP_52(0xE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_CF6")

    label("loc_CCC")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_CEC")
    OP_52(0xE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_CF6")

    label("loc_CEC")

    OP_52(0xE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_CF6")

    OP_52(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xE, 0x10)
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xF, 0x10)
    TurnDirection(0xF, 0x0, 0)
    OP_52(0xF, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_DAC")
    Jump("loc_DF6")

    label("loc_DAC")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_DCC")
    OP_52(0xF, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_DF6")

    label("loc_DCC")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_DEC")
    OP_52(0xF, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_DF6")

    label("loc_DEC")

    OP_52(0xF, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_DF6")

    OP_52(0xF, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xF, 0x10)

    #C0016
    ChrTalk(
        0xE,
        "#01802F啊，各位。\x02",
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x101,
        (
            "#00000F看来你们已经\x01",
            "把行李安置好了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0xE,
        (
            "#01802F嗯，是的……\x02\x03",

            "#01809F修利以前\x01",
            "从来都没游过泳，\x01",
            "现在好像有点紧张呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xF, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xF)

    #C0019
    ChrTalk(
        0xF,
        "#04211F别、别说出来啊！莉夏姐！\x02",
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x104,
        (
            "#00302F哈哈，这种事情\x01",
            "想瞒也瞒不住的，\x01",
            "阿修。\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0xF,
        (
            "#04205F阿、阿修……？\x01",
            "别用这种奇怪的称呼叫我！\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x104,
        (
            "#00309F哈哈，这有什么关系。\x01",
            "现在已经有阿缇、阿约和阿琪了，\x01",
            "再加上一个阿修不是挺好嘛。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0xF,
        (
            "#04206F那和我无关！\x01",
            "根本就不好！\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x105,
        (
            "#10302F呵呵，既然不会游泳，\x01",
            "那我们就手把手地\x01",
            "教她好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0xE,
        (
            "#01802F嗯，修利这么聪明，\x01",
            "学起来一定很快。\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0xF,
        (
            "#04203F哼、哼……那还用说。\x02\x03",

            "#04208F我只是……那个……要做个心理准备……\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x101,
        (
            "#00009F哈哈，你下定决心之后，\x01",
            "就和莉夏一起过来吧。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xE, 0x0)
    SetChrSubChip(0xF, 0x0)
    ClearChrFlags(0xE, 0x10)
    ClearChrFlags(0xF, 0x10)
    SetScenarioFlags(0x15A, 4)
    Return()

    # Function_6_C1B end

    def Function_7_10DC(): pass

    label("Function_7_10DC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_10ED")
    Jump("loc_133F")

    label("loc_10ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_10FB")
    Jump("loc_133F")

    label("loc_10FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_1109")
    Jump("loc_133F")

    label("loc_1109")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_1117")
    Jump("loc_133F")

    label("loc_1117")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_1125")
    Jump("loc_133F")

    label("loc_1125")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_1133")
    Jump("loc_133F")

    label("loc_1133")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_133F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15A, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_114E")
    Call(0, 9)
    Jump("loc_133F")

    label("loc_114E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12B4")

    #C0028
    ChrTalk(
        0xD,
        (
            "#01704F自从在外国的杂志上看到沙滩之后，\x01",
            "我就一直很想亲身\x01",
            "在那种地方畅玩一番～\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x104,
        (
            "#00309F就我个人来说，最期待的场面就是\x01",
            "伊莉娅小姐和各位美女穿着泳装登场！\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0xD,
        (
            "#01705F对了，听说湖水浴场的服务台\x01",
            "提供泳装出租。\x02\x03",

            "#01709F好！我这就去挑一件\x01",
            "超级华丽，而且无比性感的\x01",
            "泳装！\x02",
        )
    )

    CloseMessageWindow()
    OP_4B(0xC, 0xFF)

    #C0031
    ChrTalk(
        0xC,
        (
            "#05909F呵呵，伊莉娅，你真是的，\x01",
            "可不要穿得太过火哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xC, 0xFF)
    SetScenarioFlags(0x1, 0)
    Jump("loc_133F")

    label("loc_12B4")


    #C0032
    ChrTalk(
        0xD,
        (
            "#01709F呵呵，你们就好好期待吧。\x01",
            "我这就去挑一件超级华丽，\x01",
            "而且无比性感的泳装！\x02\x03",

            "#01702F好啦，赶快做好准备，\x01",
            "动身前往期待已久的沙滩吧！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_133F")

    TalkEnd(0xFE)
    Return()

    # Function_7_10DC end

    def Function_8_1343(): pass

    label("Function_8_1343")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_1354")
    Jump("loc_14DE")

    label("loc_1354")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_1362")
    Jump("loc_14DE")

    label("loc_1362")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_1370")
    Jump("loc_14DE")

    label("loc_1370")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_137E")
    Jump("loc_14DE")

    label("loc_137E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_138C")
    Jump("loc_14DE")

    label("loc_138C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_139A")
    Jump("loc_14DE")

    label("loc_139A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_14DE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15A, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13B5")
    Call(0, 9)
    Jump("loc_14DE")

    label("loc_13B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1480")

    #C0033
    ChrTalk(
        0xC,
        (
            "#05900F啊，罗伊德，\x01",
            "你已经做好准备了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x101,
        (
            "#00000F嗯，基本已经准备好了。\x02\x03",

            "#00004F我们先走一步，你们不用着急，\x01",
            "准备好了以后再过去吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0xC,
        (
            "#05902F呵呵，知道了，\x01",
            "我会尽早过去的。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_14DE")

    label("loc_1480")


    #C0036
    ChrTalk(
        0xC,
        (
            "#05904F伊莉娅可真是的，\x01",
            "还是老样子。\x02\x03",

            "#05902F呵呵，彩虹剧团的各位\x01",
            "肯定也都拿她没办法吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14DE")

    TalkEnd(0xFE)
    Return()

    # Function_8_1343 end

    def Function_9_14E2(): pass

    label("Function_9_14E2")

    OP_4B(0xC, 0xFF)
    OP_4B(0xD, 0xFF)

    #C0037
    ChrTalk(
        0xC,
        (
            "#05909F说起来，成年之后，\x01",
            "我好像还是第一次\x01",
            "和伊莉娅一起过夜呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0xD,
        (
            "#01705F哦～还真是。\x02\x03",

            "#01704F因为我一直都在忙着练习，\x01",
            "总是抽不出时间去看你。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0039
    ChrTalk(
        0xD,
        (
            "#01709F对了，我们今天干脆一起\x01",
            "洗澡吧，已经好久没有过了。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0xC,
        (
            "#05905F嗯，可以啊……\x02\x03",

            "#05903F但客房内的浴室比较小，\x01",
            "两个成年人一起进去，肯定会很挤吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0xD,
        (
            "#01703F嘿嘿，就是要挤些才好啊。\x02\x03",

            "#01709F就让我亲手确认一下\x01",
            "你这几年的成长状况吧！\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0xC,
        (
            "#05909F呵呵，伊莉娅，你可真是的，\x01",
            "还是老样子。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(50)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x104)
    Sleep(50)
    OP_64(0x101)

    #C0043
    ChrTalk(
        0x104,
        (
            "#00306F（唔……\x01",
            "  真是太羡慕\x01",
            "  伊莉娅小姐了。）\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x101,
        (
            "#00006F（唉……\x01",
            "  塞茜尔姐姐毫无戒备啊。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x15A, 3)
    ClearChrFlags(0xC, 0x10)
    ClearChrFlags(0xD, 0x10)
    OP_4C(0xC, 0xFF)
    OP_4C(0xD, 0xFF)
    Return()

    # Function_9_14E2 end

    def Function_10_1769(): pass

    label("Function_10_1769")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_177A")
    Jump("loc_1837")

    label("loc_177A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_1788")
    Jump("loc_1837")

    label("loc_1788")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_1796")
    Jump("loc_1837")

    label("loc_1796")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_17A6")
    Jump("loc_1837")

    label("loc_17A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_17B4")
    Jump("loc_1837")

    label("loc_17B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_17C2")
    Jump("loc_1837")

    label("loc_17C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_17D0")
    Jump("loc_1837")

    label("loc_17D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_1837")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17EB")
    Call(0, 12)
    Jump("loc_1837")

    label("loc_17EB")


    #C0045
    ChrTalk(
        0xB,
        (
            "#06401F姐姐真是的，\x01",
            "说得好过分～\x02\x03",

            "#06406F再怎么说，\x01",
            "我也是一名警察啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1837")

    TalkEnd(0xFE)
    Return()

    # Function_10_1769 end

    def Function_11_183B(): pass

    label("Function_11_183B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_184C")
    Jump("loc_1B24")

    label("loc_184C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_185A")
    Jump("loc_1B24")

    label("loc_185A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_1868")
    Jump("loc_1B24")

    label("loc_1868")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_1878")
    Jump("loc_1B24")

    label("loc_1878")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_1886")
    Jump("loc_1B24")

    label("loc_1886")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_1AA0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A20")

    #C0046
    ChrTalk(
        0x12,
        (
            "#10103F嗯～离集合时间还早，\x01",
            "做些什么好呢？\x02\x03",

            "#10108F本想和芙兰一起去\x01",
            "时装店逛逛，可是……\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x101,
        "#00005F嗯？有什么问题吗？\x02",
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x12,
        (
            "#10111F那、那个，其实……\x02\x03",

            "#10109F在沙滩上见识到了\x01",
            "塞茜尔小姐她们的身材之后，\x01",
            "不由自主地产生了一股挫败感……\x02\x03",

            "#10106F实在不想在她们面前\x01",
            "挑选衣服啊，\x01",
            "更别提试穿了……\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x101,
        (
            "#00003F（这、这个～\x01",
            "  她想得也太多了……\x01",
            "  但对女性来说，这大概也是正常心理吧。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_1A9B")

    label("loc_1A20")


    #C0050
    ChrTalk(
        0x12,
        (
            "#10106F真不想在塞茜尔小姐\x01",
            "她们的面前挑选衣服啊，\x01",
            "更别提试穿了……\x02\x03",

            "#10100F我稍后会去兰迪前辈\x01",
            "正在逛的那家珠宝店看看。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A9B")

    Jump("loc_1B24")

    label("loc_1AA0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_1AAE")
    Jump("loc_1B24")

    label("loc_1AAE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_1B1B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1AC9")
    Call(0, 12)
    Jump("loc_1B16")

    label("loc_1AC9")


    #C0051
    ChrTalk(
        0x12,
        (
            "#10106F唉，总有种上当的感觉。\x02\x03",

            "#10101F我竟然会被\x01",
            "芙兰这种傻瓜给骗了……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B16")

    Jump("loc_1B24")

    label("loc_1B1B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_1B24")

    label("loc_1B24")

    TalkEnd(0xFE)
    Return()

    # Function_11_183B end

    def Function_12_1B28(): pass

    label("Function_12_1B28")

    OP_4B(0x12, 0xFF)
    OP_4B(0xB, 0xFF)

    #C0052
    ChrTalk(
        0x12,
        (
            "#10101F芙兰可真是的……\x01",
            "直到昨天都没有\x01",
            "向我透露半点口风。\x02\x03",

            "#10106F而且还说什么\x01",
            "『要是没有工作就能去了』、\x01",
            "『我好羡慕姐姐啊』……\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0xB,
        (
            "#06402F嘿嘿，抱歉啦～\x01",
            "其实我和姐姐是同时\x01",
            "接到邀请的……\x02\x03",

            "#06409F但玛丽亚贝尔小姐\x01",
            "在事先叮嘱过我，\x01",
            "要我一直隐瞒到当天～\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x12,
        (
            "#10106F唉，我竟然会被\x01",
            "芙兰这种傻瓜给骗了……\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0xB,
        "#06405F啊，姐姐说得好过分哦～！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    ClearChrFlags(0x12, 0x10)
    ClearChrFlags(0xB, 0x10)
    OP_4C(0x12, 0xFF)
    OP_4C(0xB, 0xFF)
    Return()

    # Function_12_1B28 end

    def Function_13_1C9F(): pass

    label("Function_13_1C9F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_1CB0")
    Jump("loc_1E46")

    label("loc_1CB0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_1CBE")
    Jump("loc_1E46")

    label("loc_1CBE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_1CCC")
    Jump("loc_1E46")

    label("loc_1CCC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_1CDA")
    Jump("loc_1E46")

    label("loc_1CDA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_1D05")

    #C0056
    ChrTalk(
        0x13,
        "#01200F咕噜噜噜……嗷。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1E46")

    label("loc_1D05")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_1D13")
    Jump("loc_1E46")

    label("loc_1D13")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_1E3D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E17")

    #C0057
    ChrTalk(
        0x13,
        "#01200F……咕噜噜噜…………\x02",
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x101,
        "#00000F蔡特，原来你在这里啊。\x02",
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x104,
        (
            "#00302F哈哈，水上巴士之旅\x01",
            "让你有些疲惫吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x13,
        "#01203F……嗷。\x02",
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x105,
        "#10304F看来不是啊。\x02",
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x101,
        (
            "#00000F算啦，反正蔡特稍后\x01",
            "就会到沙滩来找我们的，\x01",
            "现在就别管它了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_1E38")

    label("loc_1E17")


    #C0063
    ChrTalk(
        0x13,
        "#01200F……咕噜噜噜…………\x02",
    )

    CloseMessageWindow()

    label("loc_1E38")

    Jump("loc_1E46")

    label("loc_1E3D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_1E46")

    label("loc_1E46")

    TalkEnd(0xFE)
    Return()

    # Function_13_1C9F end

    def Function_14_1E4A(): pass

    label("Function_14_1E4A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_1E5B")
    Jump("loc_1F49")

    label("loc_1E5B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_1E69")
    Jump("loc_1F49")

    label("loc_1E69")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_1E77")
    Jump("loc_1F49")

    label("loc_1E77")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_1E87")
    Jump("loc_1F49")

    label("loc_1E87")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_1E95")
    Jump("loc_1F49")

    label("loc_1E95")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_1F24")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1EB0")
    Call(0, 15)
    Jump("loc_1F1F")

    label("loc_1EB0")


    #C0064
    ChrTalk(
        0x11,
        (
            "#00203F连咪西都不知道，\x01",
            "就要去主题公园，\x01",
            "实在是胆大包天。\x02\x03",

            "#00201F看来修利小姐还需要\x01",
            "接受一番彻底教育……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F1F")

    Jump("loc_1F49")

    label("loc_1F24")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_1F32")
    Jump("loc_1F49")

    label("loc_1F32")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_1F40")
    Jump("loc_1F49")

    label("loc_1F40")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_1F49")

    label("loc_1F49")

    TalkEnd(0xFE)
    Return()

    # Function_14_1E4A end

    def Function_15_1F4D(): pass

    label("Function_15_1F4D")

    OP_4B(0x11, 0xFF)
    OP_4B(0xF, 0xFF)

    #C0065
    ChrTalk(
        0xF,
        "#04205F嗯？那个机械上挂着的东西是什么……？\x02",
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x11,
        "#00204F哦，这是咪西的挂件。\x02",
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0xF,
        (
            "#04202F哎？原来这就是那个\x01",
            "传说中的『咪西』啊。\x02\x03",

            "#04204F我还是第一次看到呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0068
    ChrTalk(
        0x11,
        "#00205F……第一次看到？\x02",
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0xF,
        (
            "#04202F是啊，虽然经常听到它的名字，\x01",
            "但一直都不知道它是长这样的。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x11, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x11)

    #C0070
    ChrTalk(
        0x11,
        (
            "#00203F……看来修利小姐需要\x01",
            "接受一番彻底教育……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    ClearChrFlags(0x11, 0x10)
    OP_4C(0x11, 0xFF)
    OP_4C(0xF, 0xFF)
    Return()

    # Function_15_1F4D end

    def Function_16_20D5(): pass

    label("Function_16_20D5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_20E6")
    Jump("loc_2226")

    label("loc_20E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_20F4")
    Jump("loc_2226")

    label("loc_20F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_2226")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_21B1")

    #C0071
    ChrTalk(
        0xFE,
        (
            "ＶＩＰ楼层今天已经\x01",
            "由各位包场了。\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0xFE,
        (
            "此外，遵照玛丽亚贝尔小姐的吩咐，\x01",
            "我们将向各位免费提供\x01",
            "各类客房服务。\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0xFE,
        (
            "各位如果有什么需要，\x01",
            "请不必客气，尽管提出。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2226")

    label("loc_21B1")


    #C0074
    ChrTalk(
        0xFE,
        (
            "遵照玛丽亚贝尔小姐的吩咐，\x01",
            "我们将向各位免费提供\x01",
            "各类房间服务。\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0xFE,
        (
            "各位如果有什么需要，\x01",
            "请不必客气，尽管提出。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2226")

    TalkEnd(0xFE)
    Return()

    # Function_16_20D5 end

    def Function_17_222A(): pass

    label("Function_17_222A")

    Call(0, 18)
    Return()

    # Function_17_222A end

    def Function_18_222E(): pass

    label("Function_18_222E")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_223F")
    Jump("loc_239D")

    label("loc_223F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_232E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22D2")

    #C0076
    ChrTalk(
        0x9,
        (
            "各位在沙滩上\x01",
            "玩得还开心吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0x9,
        (
            "我在休假的时候，\x01",
            "也会去沙滩上\x01",
            "享受日光浴。\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0x9,
        (
            "呵呵，近日之内，\x01",
            "还想再去一次呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2329")

    label("loc_22D2")


    #C0079
    ChrTalk(
        0x9,
        (
            "我在休假的时候，\x01",
            "也会去沙滩上\x01",
            "享受日光浴。\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0x9,
        (
            "呵呵，近日之内，\x01",
            "还想再去一次呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2329")

    Jump("loc_239D")

    label("loc_232E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_239D")

    #C0081
    ChrTalk(
        0x9,
        (
            "这里是ＶＩＰ楼层的\x01",
            "专用吧台。\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x9,
        (
            "可以为各位提供各类鸡尾酒及无酒精饮品，\x01",
            "请不必客气，尽管享用。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_239D")

    TalkEnd(0x9)
    Return()

    # Function_18_222E end

    def Function_19_23A1(): pass

    label("Function_19_23A1")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch05500.itc", 0x24)
    SoundLoad(3801)
    SoundLoad(3771)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)
    OP_4B(0xB, 0xFF)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8000)
    OP_4B(0xD, 0xFF)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x8000)
    OP_4B(0xC, 0xFF)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8000)
    OP_4B(0xE, 0xFF)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x8000)
    OP_4B(0xF, 0xFF)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x8000)
    ClearChrFlags(0x14, 0x80)
    SetChrChipByIndex(0x14, 0x24)
    SetChrSubChip(0x14, 0x0)
    SetChrFlags(0x14, 0x8000)
    SetChrPos(0xD, 9970, 0, 11960, 90)
    SetChrPos(0xC, 8910, 0, 12550, 90)
    SetChrPos(0xE, 8960, 0, 11180, 90)
    SetChrPos(0xF, 7880, 0, 11840, 90)
    SetChrPos(0x14, 1690, 0, 5920, 270)
    SetChrPos(0x109, 2590, 0, 7310, 225)
    SetChrPos(0xB, 3500, 0, 5840, 225)
    SetChrPos(0x102, 4019, 0, 7340, 225)
    SetChrPos(0x103, 4150, 0, 8660, 225)
    SetChrPos(0xA, 5460, 0, 7210, 225)
    SetChrPos(0x101, 5510, 0, 8830, 180)
    SetChrPos(0x104, 6640, 0, 9950, 180)
    SetChrPos(0x105, 5200, 0, 10210, 180)
    ClearMapObjFlags(0x0, 0x10)
    OP_70(0x0, 0xA)
    OP_68(7450, 1700, 8400, 0)
    MoveCamera(315, 25, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(24000, 0)
    SetCameraDistance(27000, 5000)
    FadeToBright(1000, 0)
    BeginChrThread(0xD, 3, 0, 20)
    BeginChrThread(0xC, 3, 0, 21)
    BeginChrThread(0xE, 3, 0, 22)
    BeginChrThread(0xF, 3, 0, 23)
    BeginChrThread(0x14, 3, 0, 24)
    BeginChrThread(0x109, 3, 0, 25)
    BeginChrThread(0xB, 3, 0, 26)
    BeginChrThread(0x102, 3, 0, 27)
    BeginChrThread(0x103, 3, 0, 28)
    BeginChrThread(0xA, 3, 0, 29)
    BeginChrThread(0x101, 3, 0, 30)
    BeginChrThread(0x105, 3, 0, 31)
    BeginChrThread(0x104, 3, 0, 32)
    Sleep(200)
    OP_71(0x0, 0xA, 0x0, 0x0, 0x0)
    Sleep(4000)
    OP_0D()
    FadeToDark(2000, 0, -1)
    OP_0D()
    EndChrThread(0xD, 0x3)
    EndChrThread(0xC, 0x3)
    EndChrThread(0xE, 0x3)
    EndChrThread(0xF, 0x3)
    EndChrThread(0x14, 0x3)
    EndChrThread(0x109, 0x3)
    EndChrThread(0xB, 0x3)
    EndChrThread(0x102, 0x3)
    EndChrThread(0x103, 0x3)
    EndChrThread(0xA, 0x3)
    EndChrThread(0x101, 0x3)
    EndChrThread(0x105, 0x3)
    EndChrThread(0x104, 0x3)
    SetChrSubChip(0xD, 0x0)
    SetChrSubChip(0xC, 0x0)
    SetChrSubChip(0xE, 0x0)
    SetChrSubChip(0xF, 0x0)
    SetChrSubChip(0x14, 0x0)
    SetChrSubChip(0x109, 0x0)
    SetChrSubChip(0xB, 0x0)
    SetChrSubChip(0x102, 0x0)
    SetChrSubChip(0x103, 0x0)
    SetChrSubChip(0xA, 0x0)
    SetChrSubChip(0x101, 0x0)
    SetChrSubChip(0x105, 0x0)
    SetChrSubChip(0x104, 0x0)
    Sleep(500)
    Sound(121, 0, 100, 0)
    Sleep(300)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 7)), scpexpr(EXPR_END)), "loc_2693")
    OP_C9(0x0, 0x80000000)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0083
    AnonymousTalk(
        0x14,
        "#02902F#3801V#30W这里就是各位的房间。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_24(0xED9)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x80000000)
    Jump("loc_26C9")

    label("loc_2693")

    SetMessageWindowPos(-1, -1, -1, -1)

    #A0084
    AnonymousTalk(
        0x14,
        "#02902F这里就是各位的房间。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_26C9")

    OP_68(-100000, 1000, -81500, 0)
    MoveCamera(318, 22, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(20900, 0)
    SetChrPos(0x14, -100000, 0, -78000, 180)
    SetChrPos(0x101, -100000, 0, -80300, 180)
    SetChrPos(0x104, -99000, 0, -80000, 180)
    SetChrPos(0x105, -101000, 0, -80100, 180)
    ClearMapObjFlags(0x7, 0x10)
    OP_70(0x7, 0x5)
    FadeToBright(1000, 0)
    OP_68(-100000, 1000, -79000, 2500)
    OP_6F(0x79)
    OP_0D()

    #C0085
    ChrTalk(
        0x101,
        "#00011F#11P好棒啊……\x02",
    )

    CloseMessageWindow()
    OP_93(0x104, 0x87, 0x1F4)
    Sleep(100)

    #C0086
    ChrTalk(
        0x104,
        "#00309F#5P哇～这也太豪华了吧。\x02",
    )

    CloseMessageWindow()
    OP_93(0x105, 0xE1, 0x1F4)
    Sleep(100)

    #C0087
    ChrTalk(
        0x105,
        (
            "#10302F#11P而且还根据我们的人数，\x01",
            "调整了床的数量。\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0x14,
        (
            "#02904F#11P呵呵，在高级酒店，\x01",
            "这是理所当然的服务。\x02\x03",

            "#02901F话说回来，我原本还想\x01",
            "给这个房间加设一道\x01",
            "可以从外面锁上的门锁呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    def lambda_28A6():
        TurnDirection(0x101, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_28A6)
    Sleep(50)

    def lambda_28B6():
        TurnDirection(0x104, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_28B6)
    Sleep(50)

    def lambda_28C6():
        TurnDirection(0x105, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_28C6)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x105, 0)

    #C0089
    ChrTalk(
        0x101,
        "#00012F#6P这、这是什么话……\x02",
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x104,
        "#00306F#6P你就这么不信任我们吗？\x02",
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x105,
        (
            "#10304F#6P呵呵，真让人伤心啊。\x02\x03",

            "#10302F虽说这里除了我们之外，\x01",
            "全都是美丽的妙龄女性……\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0x14,
        (
            "#02906F#11P嗯，瓦吉先生\x01",
            "倒是可以信任。\x02\x03",

            "#02913F但罗伊德警官和兰迪先生\x01",
            "可就没那么安全了。\x02\x03",

            "#02901F……特别是罗伊德警官，\x01",
            "你可是需要重点盯防的危险人物。\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x101,
        "#00011F#6P什么……！？\x02",
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x105,
        (
            "#10309F#6P呵呵，以你的作风来说，\x01",
            "多半会在半夜起来，去休息厅闲逛，\x01",
            "随后遇到睡不着觉的女孩子……\x02\x03",

            "#10302F聊着聊着，\x01",
            "就产生了暧昧的气氛。\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0x104,
        "#00309F#6P哦哦，的确很有可能呢～\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0096
    ChrTalk(
        0x14,
        (
            "#02909F#11P……罗伊德警官，\x01",
            "不然你就睡在\x01",
            "职工休息室吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(600)

    #C0097
    ChrTalk(
        0x101,
        "#00012F#6P不不，我一定不会做那种事的！\x02",
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x14,
        (
            "#02906F#11P哼，真是的。\x02\x03",

            "#02904F顺便一提，董事会的工作\x01",
            "还等着我去处理，所以我稍后\x01",
            "要回市内一趟……\x02\x03",

            "你可不要对穿着泳装的\x01",
            "艾莉她们动歪脑筋哦。\x02\x03",

            "#02901F……你要是敢乱来，\x01",
            "我会让保安把你扔进湖里的。\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0x101,
        (
            "#00006F#6P都说过不会了……\x02\x03",

            "#00001F……话说回来，玛丽亚贝尔小姐，\x01",
            "你果然相当繁忙啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0x14,
        (
            "#02904F#11P呵呵，毕竟父亲发表了\x01",
            "那样的提案。\x02\x03",

            "#02902F他现在已经没有余力\x01",
            "处理ＩＢＣ的业务了，\x01",
            "所以全都交给董事会来处理。\x02\x03",

            "这自然也给我增添了\x01",
            "不少麻烦。\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0x101,
        (
            "#00003F#6P这样啊……\x01",
            "真是辛苦了。\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x104,
        (
            "#00302F#6P你也要适当\x01",
            "休息一下哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0x105,
        (
            "#10300F#6P没错，休息和减压\x01",
            "有利于美容和养生。\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0x14,
        (
            "#02904F#11P呵呵，多谢关心。\x02\x03",

            "#02900F正如刚才所说，湖水浴场的服务台\x01",
            "就在一层商店街的右侧。\x02\x03",

            "你们可以去那里租借泳装，\x01",
            "然后到更衣室换衣服。\x02\x03",

            "#02901F……当然，只能进男子更衣室哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0x101,
        "#00012F#6P唉，你不必反复提醒。\x02",
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0x104,
        "#00309F#6P好了，我知道啦。\x02",
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0x14,
        (
            "#02904F#11P中午之前，整个湖水浴场\x01",
            "都包场给各位使用。\x02\x03",

            "到了下午，你们就去\x01",
            "主题公园尽情游玩吧。\x02\x03",

            "#02902F你们应该有不少人去过主题公园，\x01",
            "我也就不用再叮嘱什么了。\x02\x03",

            "#02909F另外，今晚会在迎宾馆\x01",
            "举办一场晚宴。\x02\x03",

            "这场晚宴并不需要穿正装出席，\x01",
            "请各位务必准时前来。\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0x101,
        "#00000F#6P我知道了。\x02",
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0x105,
        (
            "#10304F#6P让你如此费心，\x01",
            "真有点不好意思呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0x14,
        "#02904F#11P呵呵，不必客气。\x02",
    )

    CloseMessageWindow()
    OP_93(0x14, 0x0, 0x1F4)
    Sleep(300)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 7)), scpexpr(EXPR_END)), "loc_3089")
    OP_C9(0x0, 0x80000000)

    #C0111
    ChrTalk(
        0x14,
        (
            "#02911F#3771V#5P#40W请各位尽情\x01",
            "享受这次的休假吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xEBB)
    OP_C9(0x1, 0x80000000)
    Jump("loc_30B6")

    label("loc_3089")


    #C0112
    ChrTalk(
        0x14,
        (
            "#02902F#5P请各位尽情\x01",
            "享受这次的休假吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_30B6")

    OP_57(0x0)
    OP_5A()

    def lambda_30BE():

        label("loc_30BE")

        TurnDirection(0xFE, 0x14, 500)
        Yield()
        Jump("loc_30BE")

    QueueWorkItem2(0x101, 2, lambda_30BE)

    def lambda_30D0():

        label("loc_30D0")

        TurnDirection(0xFE, 0x14, 500)
        Yield()
        Jump("loc_30D0")

    QueueWorkItem2(0x104, 2, lambda_30D0)

    def lambda_30E2():

        label("loc_30E2")

        TurnDirection(0xFE, 0x14, 500)
        Yield()
        Jump("loc_30E2")

    QueueWorkItem2(0x105, 2, lambda_30E2)

    def lambda_30F4():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_30F4)
    Sleep(1000)
    OP_A7(0x14, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
    WaitChrThread(0x14, 1)
    Sleep(300)
    Sound(890, 0, 100, 0)
    OP_74(0x7, 0xF)
    OP_71(0x7, 0x5, 0x0, 0x0, 0x8)
    OP_79(0x7)
    OP_74(0x7, 0x1E)
    SetMapObjFlags(0x7, 0x10)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x104, 0x2)
    EndChrThread(0x105, 0x2)
    OP_68(-100000, 1000, -80000, 2000)
    OP_6F(0x79)

    #C0113
    ChrTalk(
        0x101,
        (
            "#00002F#6P……虽然说话有些不留情面，\x01",
            "但她真是相当热心啊。\x02\x03",

            "#00006F只希望她不要总是\x01",
            "莫名其妙地敌视我……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_31CD():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_31CD)
    Sleep(50)

    def lambda_31DD():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_31DD)
    Sleep(50)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x105, 0)
    Sleep(100)

    #C0114
    ChrTalk(
        0x104,
        (
            "#00304F#12P你还是认命吧。\x02\x03",

            "#00302F好了，我们抓紧时间，\x01",
            "赶快去沙滩吧～\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0x105,
        (
            "#10304F#5P呵呵，说的对。\x02\x03",

            "#10300F那些女孩子肯定还要\x01",
            "花不少时间做准备……\x02\x03",

            "我们就先过去看看吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0x101,
        (
            "#00004F#6P好……\x02\x03",

            "#00000F先和她们打个招呼，\x01",
            "然后就出发吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    ClearChrFlags(0xA, 0x8000)
    ClearChrFlags(0xB, 0x8000)
    ClearChrFlags(0xD, 0x8000)
    ClearChrFlags(0xC, 0x8000)
    ClearChrFlags(0xE, 0x8000)
    ClearChrFlags(0xF, 0x8000)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x14, 0x80)
    OP_49()
    OP_D7(0x24)
    SetMapObjFlags(0x0, 0x10)
    SetChrPos(0x0, -100000, 0, -80000, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    RemoveParty(0x1, 0xFF)
    RemoveParty(0x2, 0xFF)
    RemoveParty(0x8, 0xFF)
    SetScenarioFlags(0x144, 5)
    OP_29(0xA5, 0x1, 0x1)
    EventEnd(0x5)
    Return()

    # Function_19_23A1 end

    def Function_20_3371(): pass

    label("Function_20_3371")

    OP_9B(0x0, 0xFE, 0x0, 0x2328, 0x7D0, 0x0)
    Return()

    # Function_20_3371 end

    def Function_21_3381(): pass

    label("Function_21_3381")

    OP_9B(0x0, 0xFE, 0x0, 0x2328, 0x7D0, 0x0)
    Return()

    # Function_21_3381 end

    def Function_22_3391(): pass

    label("Function_22_3391")

    OP_9B(0x0, 0xFE, 0x0, 0x2328, 0x7D0, 0x0)
    Return()

    # Function_22_3391 end

    def Function_23_33A1(): pass

    label("Function_23_33A1")

    OP_9B(0x0, 0xFE, 0x0, 0x2328, 0x7D0, 0x0)
    Return()

    # Function_23_33A1 end

    def Function_24_33B1(): pass

    label("Function_24_33B1")

    OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x2D, 0x1F40, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0xFFD3, 0x2328, 0x7D0, 0x0)
    Return()

    # Function_24_33B1 end

    def Function_25_33DF(): pass

    label("Function_25_33DF")

    OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x2D, 0x7D0, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x2D, 0x2134, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0xFFD3, 0x2328, 0x7D0, 0x0)
    Return()

    # Function_25_33DF end

    def Function_26_341C(): pass

    label("Function_26_341C")

    OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x2D, 0x1194, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x2D, 0x1F40, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0xFFD3, 0x2328, 0x7D0, 0x0)
    Return()

    # Function_26_341C end

    def Function_27_3459(): pass

    label("Function_27_3459")

    OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x2D, 0xED8, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x2D, 0x2328, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0xFFD3, 0x2328, 0x7D0, 0x0)
    Return()

    # Function_27_3459 end

    def Function_28_3496(): pass

    label("Function_28_3496")

    OP_9B(0x0, 0xFE, 0x0, 0x9C4, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x2D, 0xDAC, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x2D, 0x2328, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0xFFD3, 0x2328, 0x7D0, 0x0)
    Return()

    # Function_28_3496 end

    def Function_29_34D3(): pass

    label("Function_29_34D3")

    OP_9B(0x0, 0xFE, 0x0, 0x9C4, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x2D, 0x1388, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x2D, 0x2328, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0xFFD3, 0x2328, 0x7D0, 0x0)
    Return()

    # Function_29_34D3 end

    def Function_30_3510(): pass

    label("Function_30_3510")

    OP_9B(0x0, 0xFE, 0x0, 0x320, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x2D, 0x7D0, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x2D, 0x14B4, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x2D, 0x2328, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0xFFD3, 0x2328, 0x7D0, 0x0)
    Return()

    # Function_30_3510 end

    def Function_31_355C(): pass

    label("Function_31_355C")

    OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x2D, 0xDAC, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x2D, 0xDAC, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x2D, 0x2328, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0xFFD3, 0x2328, 0x7D0, 0x0)
    Return()

    # Function_31_355C end

    def Function_32_35A8(): pass

    label("Function_32_35A8")

    OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x2D, 0xDAC, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x2D, 0x1388, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x2D, 0x2134, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0xFFD3, 0x2328, 0x7D0, 0x0)
    Return()

    # Function_32_35A8 end

    def Function_33_35F4(): pass

    label("Function_33_35F4")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SoundLoad(3396)
    SetChrPos(0x101, -100500, 0, -80500, 90)
    SetChrPos(0x104, -99000, 0, -81000, 270)
    SetChrPos(0x105, -101000, 0, -85000, 0)
    SetChrFlags(0x105, 0x8)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, -100000, 0, -74900, 180)
    OP_A7(0x10, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearMapObjFlags(0x7, 0x10)
    OP_70(0x7, 0x0)
    Sound(808, 0, 100, 0)
    Sleep(500)
    OP_C9(0x0, 0x80000000)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("艾莉的声音")

    #A0117
    AnonymousTalk(
        0xFF,
        "#3396V#30W抱歉，可以打扰一下吗？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_24(0xD44)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x80000000)
    PlayBGM("ed7111", 0)
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x6F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ReplaceBGM("ed7565", "ed7111")
    OP_68(-100000, 1000, -78300, 0)
    MoveCamera(320, 23, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(22500, 0)
    FadeToBright(1000, 0)
    SetCameraDistance(22000, 1500)
    Sleep(500)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_6F(0x79)
    OP_0D()
    Sound(121, 0, 100, 0)
    OP_74(0x7, 0xA)
    OP_71(0x7, 0x0, 0x5, 0x0, 0x8)

    def lambda_375C():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_375C)
    Sleep(50)

    def lambda_376C():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_376C)
    OP_79(0x7)
    OP_68(-100000, 1000, -79300, 2000)

    def lambda_378D():
        OP_9B(0x0, 0xFE, 0x0, 0xC1C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_378D)
    OP_A7(0x10, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
    WaitChrThread(0x10, 1)
    OP_6F(0x79)

    #C0118
    ChrTalk(
        0x101,
        "#00002F#6P哦，是艾莉啊。\x02",
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0x104,
        "#00302F#6P你要出去了吗？\x02",
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0x10,
        (
            "#00102F#11P嗯，伊莉娅小姐她们\x01",
            "邀我一起逛逛商店，\x01",
            "然后再去主题公园……\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x10, 0x87, 0x1F4)
    Sleep(600)
    OP_93(0x10, 0xE1, 0x1F4)
    Sleep(600)
    OP_93(0x10, 0xB4, 0x1F4)

    #C0121
    ChrTalk(
        0x10,
        (
            "#00105F#11P那个，小琪雅\x01",
            "没有来你们这里吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0x101,
        "#00005F#6P琪雅？\x02",
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0x104,
        "#00305F#6P怎么？阿琪不见了？\x02",
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0x10,
        (
            "#00106F#11P她刚才说\x01",
            "『要去找罗伊德』，\x01",
            "然后就离开了房间……\x02\x03",

            "#00108F唔……到底去哪里了呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0x101,
        "#00001F#6P是这样啊……\x02",
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0x104,
        (
            "#00300F#6P说不定正和阿缇\x01",
            "或蔡特待在一起吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0x10,
        (
            "#00104F#11P嗯，确实有可能。\x02\x03",

            "#00102F抱歉，打扰你们了，\x01",
            "我再去找找吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0x101,
        (
            "#00005F#6P啊，等一下。\x02\x03",

            "#00000F伊莉娅小姐她们\x01",
            "不是还在等你吗？\x02\x03",

            "琪雅就由我来找，\x01",
            "你赶快去赴约就行了。\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0x10,
        "#00105F#11P哎？可是……\x02",
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0x101,
        (
            "#00004F#6P一直把琪雅交给\x01",
            "你们照看也不太好意思。\x02\x03",

            "#00002F我一定会找到她，\x01",
            "带她一起去主题公园的。\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0x10,
        (
            "#00106F#11P嗯，\x01",
            "那就麻烦你啦。\x02\x03",

            "#00108F……唉，\x01",
            "本想给小琪雅\x01",
            "挑些新衣服呢……\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x10, 0x0, 0x1F4)

    def lambda_3AFE():
        OP_9B(0x0, 0xFE, 0x0, 0xC1C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_3AFE)
    Sleep(1000)
    OP_A7(0x10, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
    WaitChrThread(0x10, 1)
    SetChrFlags(0x10, 0x80)
    Sound(890, 0, 100, 0)
    OP_74(0x7, 0xA)
    OP_71(0x7, 0x5, 0x0, 0x0, 0x8)
    OP_79(0x7)
    OP_68(-100000, 1000, -80000, 1500)
    OP_6F(0x79)
    OP_93(0x104, 0x10E, 0x1F4)

    #C0132
    ChrTalk(
        0x104,
        (
            "#00309F#12P哈哈，阿琪还是\x01",
            "这么受欢迎啊。\x02\x03",

            "#00300F好，我们就赶快去找吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x5A, 0x1F4)

    #C0133
    ChrTalk(
        0x101,
        (
            "#00000F#5P不，我一个人就够了。\x02\x03",

            "你不是也想去\x01",
            "逛逛商店吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0x104,
        (
            "#00305F#12P没问题吗？\x02\x03",

            "#00304F好吧，我就在楼下的珠宝店里逛，\x01",
            "如果有什么事，可以过来找我。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 0)), scpexpr(EXPR_END)), "loc_3C76")

    #C0135
    ChrTalk(
        0x101,
        "#00002F#5P好，我知道了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3EB0")

    label("loc_3C76")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAE, 1)), scpexpr(EXPR_END)), "loc_3DA0")
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0136
    ChrTalk(
        0x101,
        (
            "#00005F#5P珠宝店……？\x01",
            "那里好像是会员制的吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0x104,
        (
            "#00302F#12P是啊，但玛丽亚贝尔大小姐\x01",
            "已经特地叮嘱过店员了，\x01",
            "现在我们也可以进去了。\x02\x03",

            "#00304F虽然那里的店员让人有点不爽，\x01",
            "但我对里面的商品很有兴趣。\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0x101,
        (
            "#00002F#5P这样啊，我知道了。\x01",
            "（我要不要也过去看看呢？）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3EB0")

    label("loc_3DA0")

    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0139
    ChrTalk(
        0x101,
        (
            "#00005F#5P珠宝店……？\x01",
            "是楼下的那家吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0x104,
        (
            "#00302F#12P是啊，玛丽亚贝尔大小姐\x01",
            "已经特地叮嘱过店员了，\x01",
            "现在我们也可以进去了。\x02\x03",

            "#00304F虽然店员的态度有些傲慢，\x01",
            "但我对里面的商品很有兴趣。\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0x101,
        (
            "#00002F#5P这样啊，我知道了。\x01",
            "（我要不要也过去看看呢？）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3EB0")

    OP_68(-100000, 1000, -78500, 5000)

    def lambda_3EC6():

        label("loc_3EC6")

        TurnDirection(0xFE, 0x104, 500)
        Yield()
        Jump("loc_3EC6")

    QueueWorkItem2(0x101, 2, lambda_3EC6)
    OP_93(0x104, 0x0, 0x1F4)

    def lambda_3EDF():
        OP_95(0xFE, -100000, 0, -76900, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3EDF)
    WaitChrThread(0x104, 1)
    Sound(121, 0, 100, 0)
    OP_74(0x7, 0xA)
    OP_71(0x7, 0x0, 0x5, 0x0, 0x8)
    OP_79(0x7)
    OP_93(0x104, 0x0, 0x0)

    def lambda_3F1D():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3F1D)
    Sleep(500)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
    WaitChrThread(0x104, 1)
    Sound(890, 0, 100, 0)
    OP_74(0x7, 0xA)
    OP_71(0x7, 0x5, 0x0, 0x0, 0x8)
    OP_79(0x7)
    EndChrThread(0x101, 0x2)
    OP_6F(0x79)

    #C0142
    ChrTalk(
        0x101,
        (
            "#00004F#6P好，去找琪雅吧。\x02\x03",

            "#00008F我想她应该还没有\x01",
            "离开这间酒店……\x02\x03",

            "#00001F但如果在这里找不到，\x01",
            "那就只能去其它地方找找看了。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_74(0x7, 0x1E)
    SetMapObjFlags(0x7, 0x10)
    ClearChrFlags(0x105, 0x8)
    OP_A7(0x10, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    RemoveParty(0x3, 0xFF)
    RemoveParty(0x4, 0xFF)
    SetChrPos(0x0, -100000, 0, -80000, 0)
    SetScenarioFlags(0x145, 1)
    OP_29(0xA5, 0x1, 0x4)
    SubItemNumber(0x329, 10)
    SubItemNumber(0x32B, 10)
    SubItemNumber(0x32C, 10)
    EventEnd(0x5)
    Return()

    # Function_33_35F4 end

    SaveToFile()

Try(main)
