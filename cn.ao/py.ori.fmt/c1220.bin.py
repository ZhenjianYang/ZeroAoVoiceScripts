from ScenarioHelper import *

def main():
    CreateScenaFile(
        "c1220.bin",                # FileName
        "c1220",                    # MapName
        "c1220",                    # Location
        0x0020,                     # MapIndex
        "ed7150",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 32, 0, 1, 0, 2],
    )

    BuildStringList((
        "c1220",                  # 0
        "接待小姐托莉亚",         # 1
        "马凯奈",                 # 2
        "雷因兹",                 # 3
        "格蕾丝",                 # 4
        "尼尔森",                 # 5
        "记者诺蒂亚",             # 6
        "总编",                   # 7
    ))

    AddCharChip((
        "chr/ch26602.itc",                   # 00
        "chr/ch45100.itc",                   # 01
        "chr/ch28100.itc",                   # 02
        "chr/ch06000.itc",                   # 03
        "chr/ch06002.itc",                   # 04
        "chr/ch26700.itc",                   # 05
        "chr/ch47900.itc",                   # 06
        "chr/ch20202.itc",                   # 07
        "chr/ch26600.itc",                   # 08
        "chr/ch20200.itc",                   # 09
        "chr/ch26702.itc",                   # 0A
    ))

    DeclNpc(5789,    0,       -430,    270,  261,  0x0, 0,   8,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(5099,    0,       60020,   0,    261,  0x0, 0,   5,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(-519,    0,       360,     0,    389,  0x0, 0,   2,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   3,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(6420,    0,       55520,   135,  389,  0x0, 0,   1,   0,   0,   0,   0,   14,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   6,   0,   0,   0,   0,   16,  255,  0)
    DeclNpc(66250,   150,     8420,    270,  389,  0x0, 0,   9,   0,   255, 255, 0,   17,  255,  0)

    DeclEvent(0x0000, 0, 26,  -6.510000228881836,    5.110000133514404,     -0.5,                  4.0,                   [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   3.255000114440918,     -2.555000066757202,    0.10000000149011612,   1.0])

    DeclActor(4100,    0,       -520,    1500,    5500,    1800,    -470,    0x007E, 0,  3,  0x0000)
    DeclActor(7270,    0,       54230,   1000,    7270,    1400,    54230,   0x007C, 0,  25, 0x0000)
    DeclActor(-1750,   0,       60890,   1000,    -1750,   1800,    60890,   0x007C, 0,  27, 0x0000)

    ChipFrameInfo(704, 0)                                        # 0

    ScpFunction((
        "Function_0_2C0",          # 00, 0
        "Function_1_370",          # 01, 1
        "Function_2_7B3",          # 02, 2
        "Function_3_863",          # 03, 3
        "Function_4_867",          # 04, 4
        "Function_5_18D0",         # 05, 5
        "Function_6_19FF",         # 06, 6
        "Function_7_1B77",         # 07, 7
        "Function_8_1CD3",         # 08, 8
        "Function_9_2748",         # 09, 9
        "Function_10_295C",        # 0A, 10
        "Function_11_2C4C",        # 0B, 11
        "Function_12_34FF",        # 0C, 12
        "Function_13_41CF",        # 0D, 13
        "Function_14_4302",        # 0E, 14
        "Function_15_448C",        # 0F, 15
        "Function_16_45C1",        # 10, 16
        "Function_17_47CA",        # 11, 17
        "Function_18_49EB",        # 12, 18
        "Function_19_51CC",        # 13, 19
        "Function_20_5832",        # 14, 20
        "Function_21_5BC0",        # 15, 21
        "Function_22_6BDE",        # 16, 22
        "Function_23_6E1E",        # 17, 23
        "Function_24_81E2",        # 18, 24
        "Function_25_857B",        # 19, 25
        "Function_26_8642",        # 1A, 26
        "Function_27_8831",        # 1B, 27
    ))


    def Function_0_2C0(): pass

    label("Function_0_2C0")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_2F8"),
        (1, "loc_304"),
        (2, "loc_310"),
        (3, "loc_31C"),
        (4, "loc_328"),
        (5, "loc_334"),
        (6, "loc_340"),
        (SWITCH_DEFAULT, "loc_34C"),
    )


    label("loc_2F8")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_358")

    label("loc_304")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_358")

    label("loc_310")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_358")

    label("loc_31C")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_358")

    label("loc_328")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_358")

    label("loc_334")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_358")

    label("loc_340")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_358")

    label("loc_34C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_358")

    label("loc_358")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_36F")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_358")

    label("loc_36F")

    Return()

    # Function_0_2C0 end

    def Function_1_370(): pass

    label("Function_1_370")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_38B")
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)

    label("loc_38B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3FB")
    ClearChrFlags(0xE, 0x80)
    SetChrChipByIndex(0xE, 0x7)
    SetChrSubChip(0xE, 0x0)
    EndChrThread(0xE, 0x0)
    SetChrBattleFlags(0xE, 0x4)
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0x9, 2160, 0, 60470, 270)
    SetChrPos(0xA, 760, 0, 60470, 90)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F6")
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0x9, 0x10)

    label("loc_3F6")

    Jump("loc_7B2")

    label("loc_3FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_487")
    ClearChrFlags(0xE, 0x80)
    SetChrChipByIndex(0xE, 0x7)
    SetChrSubChip(0xE, 0x0)
    EndChrThread(0xE, 0x0)
    SetChrBattleFlags(0xE, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BF, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_44F")
    SetChrPos(0x9, 66800, 0, 6990, 315)
    SetChrPos(0x8, 66780, 0, 5780, 315)
    SetChrSubChip(0xE, 0x1)
    Jump("loc_482")

    label("loc_44F")

    SetChrPos(0x9, 61280, 150, 340, 0)
    SetChrChipByIndex(0x9, 0xA)
    SetChrSubChip(0x9, 0x0)
    EndChrThread(0x9, 0x0)
    SetChrBattleFlags(0x9, 0x4)
    SetChrPos(0x8, 51300, 20, -970, 270)

    label("loc_482")

    Jump("loc_7B2")

    label("loc_487")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_4CB")
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xB, 480, 0, 760, 270)
    SetChrPos(0xA, -760, 0, 760, 90)
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0xB, 0x10)
    Jump("loc_7B2")

    label("loc_4CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_50A")
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0x9, 6300, 0, 57090, 180)
    SetChrPos(0xD, 6420, 0, 55520, 0)
    SetChrFlags(0x9, 0x10)
    SetChrFlags(0xD, 0x10)
    Jump("loc_7B2")

    label("loc_50A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_555")
    SetChrPos(0x9, -1000, 0, 60290, 0)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xB, 6300, 0, 57090, 180)
    SetChrPos(0xA, 6420, 0, 55520, 0)
    Jump("loc_7B2")

    label("loc_555")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_5B0")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_57F")
    Jump("loc_5AB")

    label("loc_57F")

    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xB, 480, 0, 760, 270)
    SetChrPos(0xA, -760, 0, 760, 90)

    label("loc_5AB")

    Jump("loc_7B2")

    label("loc_5B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x163, 2)), scpexpr(EXPR_END)), "loc_5D9")
    SetChrFlags(0x9, 0x80)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 2690, 0, 60030, 0)
    Jump("loc_7B2")

    label("loc_5D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_602")
    SetChrFlags(0x9, 0x80)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 2690, 0, 60030, 0)
    Jump("loc_7B2")

    label("loc_602")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_67E")
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x10)
    SetChrPos(0xD, 3490, 20, 490, 135)
    SetChrFlags(0xD, 0x10)
    SetChrPos(0x9, -3840, 0, -1380, 270)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 530, 150, 56890, 180)
    SetChrChipByIndex(0xB, 0x4)
    SetChrSubChip(0xB, 0x0)
    EndChrThread(0xB, 0x0)
    SetChrBattleFlags(0xB, 0x4)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, -420, 0, 710, 0)
    Jump("loc_7B2")

    label("loc_67E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_68C")
    Jump("loc_7B2")

    label("loc_68C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_69A")
    Jump("loc_7B2")

    label("loc_69A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_6D4")
    SetChrPos(0x9, 3350, 0, 56470, 225)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 3490, 20, 490, 135)
    SetChrFlags(0xD, 0x10)
    Jump("loc_7B2")

    label("loc_6D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_718")
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xB, 2690, 0, 60030, 270)
    SetChrPos(0xC, 1190, 0, 60030, 90)
    SetChrFlags(0xB, 0x10)
    SetChrFlags(0xC, 0x10)
    Jump("loc_7B2")

    label("loc_718")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_74D")
    SetChrPos(0x9, -3840, 0, -1380, 270)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 2690, 0, 60030, 0)
    Jump("loc_7B2")

    label("loc_74D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_7B2")
    SetChrPos(0x9, 6420, 0, 55520, 0)
    SetChrFlags(0x9, 0x10)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 6300, 0, 57090, 180)
    SetChrFlags(0xC, 0x10)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 3380, 0, 60280, 135)
    SetChrFlags(0xA, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13E, 2)), scpexpr(EXPR_END)), "loc_7B2")
    OP_93(0xA, 0x0, 0x0)

    label("loc_7B2")

    Return()

    # Function_1_370 end

    def Function_2_7B3(): pass

    label("Function_2_7B3")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_7CC")
    OP_10(0x0, 0x0)
    OP_10(0x5, 0x1)
    Jump("loc_7D2")

    label("loc_7CC")

    OP_10(0x0, 0x1)
    OP_10(0x5, 0x0)

    label("loc_7D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_7E0")
    ModifyEventFlags(0, 0, 0x80)

    label("loc_7E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_81D")
    SetMapObjFrame(0xFF, "light1", 0x0, 0x1)
    SetMapObjFrame(0xFF, "light0", 0x0, 0x1)
    Sound(128, 1, 50, 0)

    label("loc_81D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_850")
    OP_7D(0xD2, 0xD2, 0xE6, 0x0, 0x0)
    SetMapObjFrame(0xFF, "light1", 0x0, 0x1)
    SetMapObjFrame(0xFF, "light0", 0x0, 0x1)

    label("loc_850")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_862")
    OP_65(0x0, 0x1)

    label("loc_862")

    Return()

    # Function_2_7B3 end

    def Function_3_863(): pass

    label("Function_3_863")

    Call(0, 4)
    Return()

    # Function_3_863 end

    def Function_4_867(): pass

    label("Function_4_867")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C1F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A16")
    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_934")

    #C0001
    ChrTalk(
        0x8,
        (
            "特别任务支援科的各位……\x01",
            "莫非你们为了\x01",
            "本社的委托而来的？\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x8,
        (
            "不过，相关的负责人\x01",
            "去调查脱轨事故了……\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0x8,
        (
            "不好意思，\x01",
            "请大家改日再来吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_A12")

    label("loc_934")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x163, 2)), scpexpr(EXPR_END)), "loc_9B3")

    #C0004
    ChrTalk(
        0x8,
        (
            "大家正在二层的编辑部\x01",
            "随时准备着对这起列车脱轨事故\x01",
            "进行速报。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x8,
        (
            "如果有事情要找各位记者，\x01",
            "我可以前去转告。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A12")

    label("loc_9B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_A12")

    #C0006
    ChrTalk(
        0x8,
        (
            "西克洛斯贝尔街道上\x01",
            "竟然发生了脱轨事故……\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x8,
        (
            "难道这又是恐怖分子\x01",
            "搞的鬼吗……？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A12")

    TalkEnd(0x8)
    Return()

    label("loc_A16")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 0)), scpexpr(EXPR_END)), "loc_C11")
    TalkBegin(0x8)
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
            "对话\x01",              # 0
            "报告采访内容\x01",      # 1
            "放弃\x01",              # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A8B")
    TalkEnd(0x8)
    Return()

    label("loc_A8B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C0C")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 1)), scpexpr(EXPR_END)), "loc_AB7")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_AB7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 2)), scpexpr(EXPR_END)), "loc_ACA")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_ACA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 3)), scpexpr(EXPR_END)), "loc_ADD")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_ADD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 4)), scpexpr(EXPR_END)), "loc_AF0")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_AF0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 5)), scpexpr(EXPR_END)), "loc_B03")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_B03")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 6)), scpexpr(EXPR_END)), "loc_B16")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_B16")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 7)), scpexpr(EXPR_END)), "loc_B29")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_B29")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 0)), scpexpr(EXPR_END)), "loc_B3C")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_B3C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 1)), scpexpr(EXPR_END)), "loc_B4F")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_B4F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 2)), scpexpr(EXPR_END)), "loc_B62")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_B62")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 3)), scpexpr(EXPR_END)), "loc_B75")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_B75")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_BA2")
    TalkEnd(0x8)
    Call(0, 22)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B9C")
    Call(0, 23)

    label("loc_B9C")

    Return()

    label("loc_BA2")


    #C0008
    ChrTalk(
        0x101,
        (
            "#00005F（哦，在各地探访过的饮食店\x01",
            "  还不够六处呢。）\x02\x03",

            "#00003F（现在还不能报告，\x01",
            "  继续努力吧。）\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x8)
    Return()

    label("loc_C0C")

    Jump("loc_C1F")

    label("loc_C11")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C1F")
    Call(0, 20)
    Return()

    label("loc_C1F")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_CF4")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CAA")

    #C0009
    ChrTalk(
        0x8,
        (
            "各位，请加油完成\x01",
            "美食向导的取材工作哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x8,
        (
            "在取材过程中还能品尝到各种美食，\x01",
            "就轻松愉快地\x01",
            "完成工作吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CEF")

    label("loc_CAA")


    #C0011
    ChrTalk(
        0x8,
        "大家真是辛苦了。\x02",
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x8,
        (
            "如果以后又有什么事情，\x01",
            "还要请各位帮忙哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CEF")

    Jump("loc_18CC")

    label("loc_CF4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_D61")

    #C0013
    ChrTalk(
        0x8,
        (
            "听说雷因兹躲到了\x01",
            "地下空间，\x01",
            "从而逃过一劫。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x8,
        (
            "呵呵，不管怎么说，\x01",
            "他平安无事真是太好了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18CC")

    label("loc_D61")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_D6F")
    Jump("loc_18CC")

    label("loc_D6F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_EC5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E45")

    #C0015
    ChrTalk(
        0x8,
        (
            "今天早上，国防军的士兵进入这里\x01",
            "的时候，我真是吃了一惊。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x8,
        (
            "距离独立宣言的发表，仅仅过了一周的时间，\x01",
            "没想到事态竟然会发展到如此地步……\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x8,
        (
            "所谓的风云突变，\x01",
            "就是指现在这种状况吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_EC0")

    label("loc_E45")


    #C0018
    ChrTalk(
        0x8,
        (
            "从市里目前的状态来看，\x01",
            "继续支持总统的人\x01",
            "仍然很多……\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x8,
        (
            "但老实说，我却感到很困惑。\x01",
            "……今后究竟会发展成什么局面呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EC0")

    Jump("loc_18CC")

    label("loc_EC5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_103A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FC7")

    #C0020
    ChrTalk(
        0x8,
        (
            "袭击事件之后的复兴活动，\x01",
            "还有三天之后的居民投票活动……\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x8,
        (
            "这两件事情\x01",
            "似乎使这个城市产生了\x01",
            "一股前所未有的凝聚力。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x8,
        (
            "支持独立的一方在讨论时的\x01",
            "那种异常狂热情绪\x01",
            "有些令人在意……\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x8,
        (
            "但考虑到市民们的感情，\x01",
            "也是可以\x01",
            "理解的。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1035")

    label("loc_FC7")


    #C0024
    ChrTalk(
        0x8,
        (
            "支持独立的一方在讨论时的\x01",
            "那种异常狂热情绪\x01",
            "有些令人在意……\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x8,
        (
            "但考虑到市民们的感情，\x01",
            "也是可以\x01",
            "理解的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1035")

    Jump("loc_18CC")

    label("loc_103A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 0)), scpexpr(EXPR_END)), "loc_1048")
    Jump("loc_18CC")

    label("loc_1048")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_10EC")

    #C0026
    ChrTalk(
        0x8,
        (
            "听说格蕾丝小姐他们昨天\x01",
            "擅自接近了事件现场，\x01",
            "遭到了警备队的喝斥。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x8,
        (
            "我虽然理解大家对工作的热情……\x01",
            "但还是很担心呢，\x01",
            "希望他们多注意自身的安全。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18CC")

    label("loc_10EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1276")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11F9")

    #C0028
    ChrTalk(
        0x8,
        (
            "昨天为了对脱轨事故进行速报，\x01",
            "与社会各界的联络业务十分繁忙。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x8,
        (
            "回想一下，本年度发行的号外刊物\x01",
            "似乎比往年都要多呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x8,
        (
            "如果增加号外刊物是为了发布好消息，\x01",
            "那自然是无所谓……\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x8,
        (
            "但如果全都是恶性事件或事故的报道，\x01",
            "可就有点让人沮丧了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1271")

    label("loc_11F9")


    #C0032
    ChrTalk(
        0x8,
        (
            "如果增加号外刊物是为了发布好消息，\x01",
            "那自然是无所谓……\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x8,
        (
            "但如果全都是恶性事件或事故的报道，\x01",
            "可就有点让人沮丧了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1271")

    Jump("loc_18CC")

    label("loc_1276")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x163, 2)), scpexpr(EXPR_END)), "loc_12F5")

    #C0034
    ChrTalk(
        0x8,
        (
            "大家正在二层的编辑部\x01",
            "随时准备着对这起列车脱轨事故\x01",
            "进行速报。\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x8,
        (
            "如果有事情要找各位记者，\x01",
            "我可以前去转告。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18CC")

    label("loc_12F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_1359")

    #C0036
    ChrTalk(
        0x8,
        (
            "西克洛斯贝尔街道上\x01",
            "竟然发生了脱轨事故……\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x8,
        (
            "难道这又是恐怖分子\x01",
            "搞的鬼吗……？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18CC")

    label("loc_1359")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_136A")
    Call(0, 6)
    Jump("loc_18CC")

    label("loc_136A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1555")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14B0")

    #C0038
    ChrTalk(
        0x8,
        (
            "两日之后，好像要在\x01",
            "市民会馆召开以『独立的利弊』\x01",
            "为主题的市民座谈会……\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x8,
        (
            "这是由本社发起提案，\x01",
            "在市政府的宣传与支持之下，\x01",
            "共同举办的活动。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x8,
        (
            "在独立提案发表之后，\x01",
            "有很多读者向本社咨询\x01",
            "居民投票中的判断基准……\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x8,
        (
            "除了报道之外，我们还能做些什么呢——\x01",
            "怀着这样的想法，我们便策划了这个活动。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1550")

    label("loc_14B0")


    #C0042
    ChrTalk(
        0x8,
        (
            "在独立提案发表之后，\x01",
            "有很多读者向本社咨询\x01",
            "居民投票中的判断基准……\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x8,
        (
            "除了报道之外，我们还能做些什么呢——\x01",
            "怀着这样的想法，我们便\x01",
            "策划了这场市民座谈会。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1550")

    Jump("loc_18CC")

    label("loc_1555")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_15DA")

    #C0044
    ChrTalk(
        0x8,
        (
            "格蕾丝小姐和雷因兹\x01",
            "去了百货店，\x01",
            "好像是急着要买什么东西……\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x8,
        (
            "他们不会因为这个缘故\x01",
            "来不及入场采访通商会议吧……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18CC")

    label("loc_15DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_15EB")
    Call(0, 7)
    Jump("loc_18CC")

    label("loc_15EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1666")

    #C0046
    ChrTalk(
        0x8,
        (
            "通商会议终于要在\x01",
            "明天开始了。\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x8,
        (
            "各位记者为了做好准备工作，\x01",
            "全都忙得焦头烂额，\x01",
            "连我都能体会到紧张感。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18CC")

    label("loc_1666")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_17C9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_174E")

    #C0048
    ChrTalk(
        0x8,
        (
            "雷因兹今天去\x01",
            "协助调查遗迹了。\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x8,
        (
            "听话又能干的助手被借走了，\x01",
            "格蕾丝小姐一直在发牢骚……\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x8,
        (
            "仔细想想，雷因兹其实是\x01",
            "今年刚刚入社的新人啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x8,
        (
            "但他却如此可靠，\x01",
            "各方面的工作都能胜任，\x01",
            "真是很了不起。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_17C4")

    label("loc_174E")


    #C0052
    ChrTalk(
        0x8,
        (
            "大家可能都忘了，\x01",
            "雷因兹其实是\x01",
            "今年刚刚入社的新人啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x8,
        (
            "但他却如此可靠，\x01",
            "各方面的工作都能胜任，\x01",
            "真是很了不起。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17C4")

    Jump("loc_18CC")

    label("loc_17C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_18CC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_185F")

    #C0054
    ChrTalk(
        0x8,
        (
            "啊，好久不见，\x01",
            "是特别任务支援科的各位吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x8,
        (
            "欢迎来访克洛斯贝尔通讯社。\x01",
            "如果有什么事情，\x01",
            "请不要客气，尽管和我说哦。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_18CC")

    label("loc_185F")


    #C0056
    ChrTalk(
        0x8,
        (
            "呵呵，听说各位\x01",
            "恢复正常工作时，\x01",
            "格蕾丝小姐也很高兴呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x8,
        (
            "如果有什么事情，\x01",
            "请不要客气，尽管和我说哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18CC")

    TalkEnd(0x8)
    Return()

    # Function_4_867 end

    def Function_5_18D0(): pass

    label("Function_5_18D0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1940")

    #C0058
    ChrTalk(
        0xFE,
        (
            "听说雷因兹躲到了\x01",
            "地下空间，\x01",
            "从而逃过一劫。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0xFE,
        (
            "呵呵，不管怎么说，\x01",
            "他平安无事真是太好了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19FB")

    label("loc_1940")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_19AA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BF, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_195F")
    TalkEnd(0xFE)
    Call(0, 18)
    Return()

    label("loc_195F")


    #C0060
    ChrTalk(
        0xFE,
        (
            "希望雷因兹\x01",
            "不要太乱来啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0xFE,
        (
            "总之，我就先祈祷\x01",
            "他平安无事吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19FB")

    label("loc_19AA")


    #C0062
    ChrTalk(
        0xFE,
        (
            "啊，是大家啊。\x01",
            "不可以进到\x01",
            "里面来哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0xFE,
        (
            "如果有什么事情，\x01",
            "请到正面和我说。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19FB")

    TalkEnd(0xFE)
    Return()

    # Function_5_18D0 end

    def Function_6_19FF(): pass

    label("Function_6_19FF")

    OP_4B(0xD, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1AFB")

    #C0064
    ChrTalk(
        0xD,
        (
            "嗯～是吗。\x01",
            "本以为他今天肯定在呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x8,
        (
            "顺便一说，\x01",
            "他去玛因兹矿山镇了，\x01",
            "可能要很晚才能回来……\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x8,
        (
            "如果想和他见面，\x01",
            "最好在这里留个言，\x01",
            "我会为您转达的。\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0xD,
        "嗯，说的也是。\x02",
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0xD,
        (
            "那好，请帮我\x01",
            "传个话给他吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x8,
        "好的，知道了。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1B72")

    label("loc_1AFB")


    #C0070
    ChrTalk(
        0x8,
        (
            "那么，可以告诉我\x01",
            "您的暂住地吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0xD,
        "哦，在东街的龙老饭店。\x02",
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0xD,
        (
            "请帮我告诉他，\x01",
            "只要接到联络，\x01",
            "我马上就可以赶来。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B72")

    OP_4C(0xD, 0xFF)
    Return()

    # Function_6_19FF end

    def Function_7_1B77(): pass

    label("Function_7_1B77")

    OP_4B(0xD, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C77")

    #C0073
    ChrTalk(
        0xD,
        (
            "唉～真遗憾。\x01",
            "尼尔森先生\x01",
            "外出了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x8,
        (
            "抱歉，\x01",
            "其实他平时就很少\x01",
            "留在通讯社的。\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0x8,
        (
            "今天好像说是要去和\x01",
            "一位友人见个面。\x01",
            "需要帮您转达什么吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0xD,
        (
            "不，不必了。\x01",
            "只是想和他随便聊聊而已，\x01",
            "就不必麻烦了。\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0xD,
        "还是等下次有机会再说吧。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1CCE")

    label("loc_1C77")


    #C0078
    ChrTalk(
        0xD,
        (
            "对了，\x01",
            "我想和总编打个招呼，\x01",
            "现在方便吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0x8,
        (
            "好的，我现在就问一下，\x01",
            "请稍等片刻。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1CCE")

    OP_4C(0xD, 0xFF)
    Return()

    # Function_7_1B77 end

    def Function_8_1CD3(): pass

    label("Function_8_1CD3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1CE4")
    Jump("loc_2744")

    label("loc_1CE4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_1CF2")
    Jump("loc_2744")

    label("loc_1CF2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_1D6E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18F, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D0D")
    Call(0, 9)
    Jump("loc_1D69")

    label("loc_1D0D")

    OP_4B(0xA, 0xFF)

    #C0080
    ChrTalk(
        0xB,
        (
            "#02100F那好，就拜托你\x01",
            "继续去和国防军交涉。\x02\x03",

            "如果有什么情况，要马上和我联络哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xA, 0xFF)

    label("loc_1D69")

    Jump("loc_2744")

    label("loc_1D6E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1D7C")
    Jump("loc_2744")

    label("loc_1D7C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_1E09")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x171, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D9B")
    TalkEnd(0xFE)
    Call(0, 19)
    Return()

    label("loc_1D9B")


    #C0081
    ChrTalk(
        0xB,
        (
            "#02100F罗伊德，你们一定要\x01",
            "多加小心哦。\x02\x03",

            "#02109F一定要让我\x01",
            "再写出一篇特别任务支援科\x01",
            "大展身手的报道！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2744")

    label("loc_1E09")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1FF1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x171, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F65")

    #C0082
    ChrTalk(
        0xB,
        (
            "#02100F啊，是大家啊。\x01",
            "昨天工作到那么晚，真是辛苦了。\x02\x03",

            "#02101F自那之后……\x01",
            "了解到有关瓦鲁多的情况了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x101,
        (
            "#00003F没有……\x02\x03",

            "#00001F我们今天早上去鬼火调查了，\x01",
            "也没有得到任何情报。\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0xB,
        (
            "#02103F是吗……\x02\x03",

            "#02102F算了，我们也会努力\x01",
            "调查各种可能性的。\x02\x03",

            "#02100F另外，瓦吉……\x01",
            "你不要想太多哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0x105,
        "#10304F呵呵，多谢关心。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x171, 1)
    Jump("loc_1FEC")

    label("loc_1F65")


    #C0086
    ChrTalk(
        0xB,
        (
            "#02101F话说回来……\x01",
            "蓝花的事情也很让人担心呢。\x02\x03",

            "#02103F如果除了约亚西姆之外，\x01",
            "还有其他人可以制造那种药物……\x01",
            "那可真是相当棘手啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1FEC")

    Jump("loc_2744")

    label("loc_1FF1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_1FFF")
    Jump("loc_2744")

    label("loc_1FFF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_232B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x171, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_21FB")

    #C0087
    ChrTalk(
        0xB,
        (
            "#02104F呼，早上先喝点咖啡，真是舒服啊～\x02\x03",

            "#02102F罗伊德，你们也来喝点如何？\x01",
            "虽然只是普通的罐装咖啡。\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0x101,
        (
            "#00000F啊，不用了，\x01",
            "好意心领。\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0xB,
        (
            "#02102F哦，这样啊，\x01",
            "呵呵，那就算了。\x02\x03",

            "#02104F话说回来，\x01",
            "各位昨天讨伐『幻兽』，\x01",
            "好像很辛苦吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x102,
        "#00105F的确是花费了不少工夫……\x02",
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x103,
        "#00206F……消息还是这么灵通啊。\x02",
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0xB,
        (
            "#02109F还好啦～毕竟我们就是\x01",
            "靠这个吃饭的嘛。\x02\x03",

            "#02100F总之，大家就多多加油，\x01",
            "同时注意不要受伤吧。\x02\x03",

            "#02102F再怎么说，身体也是\x01",
            "一切的本钱啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x101,
        "#00000F嗯，谢谢。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x171, 2)
    Jump("loc_2326")

    label("loc_21FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2298")

    #C0094
    ChrTalk(
        0xB,
        (
            "#02103F说起那个所谓的『幻兽』……\x01",
            "虽然我不是很了解，\x01",
            "但真是只能用奇异来形容啊。\x02\x03",

            "#02100F罗伊德，你们要多多加油，\x01",
            "同时注意不要受伤哦。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2309")

    label("loc_2298")


    #C0095
    ChrTalk(
        0xB,
        (
            "#02100F啊，对了对了，\x01",
            "如果『美食向导』的取材任务完成了，\x01",
            "就去接待处报告吧。\x02\x03",

            "#02109F全都拜托大家了哦～¤\x02",
        )
    )

    CloseMessageWindow()
    ClearScenarioFlags(0x0, 2)

    label("loc_2309")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x10)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2326")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_2326")
    ClearScenarioFlags(0x0, 2)

    label("loc_2326")

    Jump("loc_2744")

    label("loc_232B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2339")
    Jump("loc_2744")

    label("loc_2339")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2347")
    Jump("loc_2744")

    label("loc_2347")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2355")
    Jump("loc_2744")

    label("loc_2355")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_23D5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x148, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2370")
    Call(0, 10)
    Jump("loc_23D0")

    label("loc_2370")


    #C0096
    ChrTalk(
        0xB,
        (
            "#02102F啊，这不就是最近传得很热的\x01",
            "那个『雪华堂』点心吗？\x02\x03",

            "#02109F谢谢，\x01",
            "我一直都想尝尝呢～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_23D0")

    Jump("loc_2744")

    label("loc_23D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_273B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13E, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_26D8")

    #C0097
    ChrTalk(
        0xB,
        (
            "#02102F啊，是你们啊，\x01",
            "一天没见了～\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x101,
        "#00000F哈哈，是啊。\x02",
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0x102,
        (
            "#00100F自那之后，\x01",
            "对黑月的调查有什么进展吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0xB,
        (
            "#02106F呼，也算是有吧。\x02\x03",

            "#02100F我们对其他的投标业主\x01",
            "也进行了调查……\x02\x03",

            "如果不出什么意外，\x01",
            "那一带恐怕就要落入\x01",
            "黑月手里了。\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0x109,
        "#10103F这样啊……\x02",
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0xB,
        (
            "#02106F至于更加具体的事情，\x01",
            "在出现最后的结果之前，\x01",
            "也就无法得知了。\x02\x03",

            "#02100F事情就是这样了，\x01",
            "我今天准备将这段时间\x01",
            "积压的工作解决一下。\x02\x03",

            "#02102F对了对了，\x01",
            "特别任务支援科恢复了工作，\x01",
            "我会以此为题，写一篇报道的。\x02\x03",

            "#02109F如果你们有什么话想说，\x01",
            "或是有什么照片想放在报道里，\x01",
            "可以现在告诉我哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0x105,
        (
            "#10303F呵呵，那我就\x01",
            "提供几张本人在男公关俱乐部使用\x01",
            "的照片吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0x101, 0x105, 500)
    Sleep(200)

    #C0104
    ChrTalk(
        0x101,
        "#00006F……拜托你不要这样。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x13E, 3)
    Jump("loc_2736")

    label("loc_26D8")


    #C0105
    ChrTalk(
        0xB,
        (
            "#02106F呼，在这种时候，\x01",
            "雷因兹却外出了。\x02\x03",

            "本想把一堆杂事\x01",
            "全部推给他呢……\x01",
            "真是太遗憾了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2736")

    Jump("loc_2744")

    label("loc_273B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_2744")

    label("loc_2744")

    TalkEnd(0xFE)
    Return()

    # Function_8_1CD3 end

    def Function_9_2748(): pass

    label("Function_9_2748")

    OP_4B(0xB, 0xFF)
    OP_4B(0xA, 0xFF)
    TurnDirection(0xB, 0x0, 0)
    TurnDirection(0xA, 0x0, 0)

    #C0106
    ChrTalk(
        0xB,
        (
            "#02101F啊，是大家啊。\x01",
            "你们想必看过了总统的演说吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0x101,
        (
            "#00001F是的，多谢您特意\x01",
            "通知我们。\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0x102,
        (
            "#00101F格蕾丝小姐，\x01",
            "你们今后有何打算？\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0xB,
        (
            "#02103F嗯，不管怎么说，\x01",
            "首先当然是去各处取材。\x02\x03",

            "#02101F至少要再去采访一下\x01",
            "国防军，套出一些具体\x01",
            "的情报……\x02\x03",

            "还要去街上听取民众的声音。\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0xA,
        (
            "另外就是调查\x01",
            "外国媒体的反应。\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0xA,
        (
            "二层的国际通讯器\x01",
            "现在正在被满负荷使用中。\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0x103,
        "#00203F原来如此，还真是很忙啊。\x02",
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0xB,
        (
            "#02104F还好啦～\x01",
            "你们应该也会很辛苦，\x01",
            "我们就一起加油吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0x101,
        "#00000F嗯，知道了。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x18F, 2)
    OP_93(0xB, 0x10E, 0x0)
    OP_93(0xA, 0x5A, 0x0)
    OP_4C(0xB, 0xFF)
    OP_4C(0xA, 0xFF)
    Return()

    # Function_9_2748 end

    def Function_10_295C(): pass

    label("Function_10_295C")

    OP_4B(0xB, 0xFF)
    OP_4B(0xC, 0xFF)

    #C0115
    ChrTalk(
        0xB,
        (
            "#02109F呵呵，尼尔森先生，\x01",
            "总算见到您了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0xC,
        "嗯，我也期待已久了。\x02",
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0xC,
        (
            "对了，\x01",
            "我听总编说了。\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0xC,
        (
            "在这三年间，你已经变得\x01",
            "相当可靠了啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xB)

    #C0119
    ChrTalk(
        0xB,
        (
            "#02109F哪里，我还差得很远呢。\x02\x03",

            "#02104F平时只会挑一些\x01",
            "自己感兴趣的工作……\x01",
            "做的全都是自己喜欢的事情。\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0xC,
        (
            "哈哈，正该如此。\x01",
            "保持愉快的心情，享受工作\x01",
            "的过程才是最重要的。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6E, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2B50")

    #C0121
    ChrTalk(
        0x101,
        (
            "#00000F（格蕾丝小姐……\x01",
            "  在尼尔森先生的面前，\x01",
            "  感觉和平时完全不同了啊。）\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0x102,
        (
            "#00102F（呵呵，是啊，\x01",
            "  这可真是少见的场面。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C40")

    label("loc_2B50")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x133, 3)), scpexpr(EXPR_END)), "loc_2BD0")

    #C0123
    ChrTalk(
        0x101,
        (
            "#00000F（格蕾丝小姐的样子\x01",
            "  似乎和平时完全不同啊。）\x02\x03",

            "#00003F（那个人是叫尼尔森吧，\x01",
            "  看来他们是老相识……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C40")

    label("loc_2BD0")


    #C0124
    ChrTalk(
        0x101,
        (
            "#00000F（格蕾丝小姐的样子\x01",
            "  似乎和平时完全不同啊。）\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0x102,
        (
            "#00100F（嗯，是啊，\x01",
            "  她旁边的那个人又是谁呢？）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C40")

    OP_4C(0xB, 0xFF)
    OP_4C(0xC, 0xFF)
    SetScenarioFlags(0x148, 1)
    Return()

    # Function_10_295C end

    def Function_11_2C4C(): pass

    label("Function_11_2C4C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2D0F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C6A")
    Call(0, 13)
    Jump("loc_2D0A")

    label("loc_2C6A")


    #C0126
    ChrTalk(
        0xFE,
        (
            "有关大树的取材任务就交给格蕾丝前辈了，\x01",
            "我们准备彻底追踪\x01",
            "政府的动向。\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0xFE,
        (
            "在两大国有所行动之前，\x01",
            "政府究竟能建立起怎样的体制呢……\x01",
            "这无论如何也不能错过啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D0A")

    Jump("loc_34FB")

    label("loc_2D0F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_2D1D")
    Jump("loc_34FB")

    label("loc_2D1D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_2D86")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18F, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D38")
    Call(0, 9)
    Jump("loc_2D81")

    label("loc_2D38")

    OP_4B(0xB, 0xFF)

    #C0128
    ChrTalk(
        0xFE,
        "嗯，明白了。\x02",
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0xFE,
        (
            "格蕾丝前辈，请一定不要\x01",
            "过度刺激国防军啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xB, 0xFF)

    label("loc_2D81")

    Jump("loc_34FB")

    label("loc_2D86")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2D94")
    Jump("loc_34FB")

    label("loc_2D94")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_2E12")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x171, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2DB3")
    TalkEnd(0xFE)
    Call(0, 19)
    Return()

    label("loc_2DB3")


    #C0130
    ChrTalk(
        0xFE,
        (
            "……我听说『赤色星座』\x01",
            "并非寻常之敌。\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0xFE,
        (
            "各位，如果要前往玛因兹，\x01",
            "一定要多加小心。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_34FB")

    label("loc_2E12")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2E90")

    #C0132
    ChrTalk(
        0xFE,
        (
            "列车事故并没有造成太大的混乱，\x01",
            "也算是不幸中的万幸啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0xFE,
        (
            "接下来，只要能查明那种药物\x01",
            "的流通渠道就好了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_34FB")

    label("loc_2E90")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_2E9E")
    Jump("loc_34FB")

    label("loc_2E9E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2F20")

    #C0134
    ChrTalk(
        0xFE,
        "从今天一早开始，就一直在开编辑会议。\x02",
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0xFE,
        (
            "最近不仅有不少重大新闻，\x01",
            "大家的讨论也都十分热烈，\x01",
            "真是让人充满干劲。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_34FB")

    label("loc_2F20")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2F2E")
    Jump("loc_34FB")

    label("loc_2F2E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2F3C")
    Jump("loc_34FB")

    label("loc_2F3C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2F4A")
    Jump("loc_34FB")

    label("loc_2F4A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2F58")
    Jump("loc_34FB")

    label("loc_2F58")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_2F66")
    Jump("loc_34FB")

    label("loc_2F66")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_34FB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13E, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3499")

    #C0136
    ChrTalk(
        0xFE,
        (
            "那个人就是本社的传说……\x01",
            "伟大的人一举一动\x01",
            "都是那么与众不同啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0xFE,
        (
            "……啊，不好不好。\x01",
            "我得赶快找齐资料，回办公桌整理。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xFE, 0x0, 500)
    Sleep(200)

    #C0138
    ChrTalk(
        0xFE,
        "啊，是特别任务支援科的各位。\x02",
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0x101,
        (
            "#00005F你好像是……经常和格蕾丝小姐\x01",
            "一起行动的……\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0xFE,
        "嗯，我是记者雷因兹。\x02",
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0xFE,
        (
            "……话虽如此，\x01",
            "但最近已经基本\x01",
            "被定型为摄影师了。\x02",
        )
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0xFE,
        (
            "呼，我总是提醒周围的人，\x01",
            "自己是一名记者，结果还是……\x02",
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

    #C0143
    ChrTalk(
        0x102,
        "#00106F情、情况好像很复杂呢……\x02",
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0x105,
        (
            "#10300F呵呵，这就是理想与现实\x01",
            "之间的差异吧。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x130, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_32A6")

    #C0145
    ChrTalk(
        0x101,
        (
            "#00000F那个……对了，\x01",
            "格蕾丝小姐在吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0xFE,
        (
            "格蕾丝前辈今天\x01",
            "出去采访了。\x02",
        )
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0xFE,
        (
            "她说今天的采访，还是一个人去\x01",
            "行动会更加方便……\x02",
        )
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0xFE,
        (
            "还把自己的\x01",
            "好几件工作\x01",
            "都推给我了。\x02",
        )
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0xFE,
        (
            "呼，不过好在她把注意事项\x01",
            "之类的东西也都写下来了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3383")

    label("loc_32A6")


    #C0150
    ChrTalk(
        0x101,
        (
            "#00000F对了，我们刚才\x01",
            "见到了格蕾丝小姐，\x01",
            "你们今天没在一起啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0xFE,
        (
            "嗯，她说今天的采访，\x01",
            "还是一个人去行动会更加方便……\x02",
        )
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0xFE,
        (
            "还把自己的\x01",
            "好几件工作\x01",
            "都推给我了。\x02",
        )
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0xFE,
        (
            "呼，不过好在她把注意事项\x01",
            "之类的东西也都写下来了……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3383")

    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_63(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xFE)

    #C0154
    ChrTalk(
        0xFE,
        (
            "啊啊，不知不觉，\x01",
            "都快到截稿时间了……！\x02",
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

    #C0155
    ChrTalk(
        0x109,
        "#10100F我、我们好像打扰到你了啊。\x02",
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0x102,
        "#00100F那个……请加油吧。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    OP_93(0xFE, 0x0, 0x1F4)
    SetScenarioFlags(0x13E, 2)
    Return()

    label("loc_3499")


    #C0157
    ChrTalk(
        0xFE,
        (
            "嗯……还有一个报道中需要的\x01",
            "资料是放在哪里了……\x02",
        )
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0xFE,
        (
            "呜呜，不知不觉，\x01",
            "都快到截稿时间了……！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_34FB")

    TalkEnd(0xFE)
    Return()

    # Function_11_2C4C end

    def Function_12_34FF(): pass

    label("Function_12_34FF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3594")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_351D")
    Call(0, 13)
    Jump("loc_358F")

    label("loc_351D")


    #C0159
    ChrTalk(
        0xFE,
        (
            "总之，现在必须要多去四处走动，\x01",
            "尽可能地收集更多的情报。\x02",
        )
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0xFE,
        (
            "完成一件工作之后，\x01",
            "连稍微休息一下的时间都没有。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_358F")

    Jump("loc_41CB")

    label("loc_3594")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_366C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BF, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_35B3")
    TalkEnd(0xFE)
    Call(0, 18)
    Return()

    label("loc_35B3")


    #C0161
    ChrTalk(
        0xFE,
        (
            "我们正准备\x01",
            "以格蕾丝取得的情报\x01",
            "为基础撰写速报……\x02",
        )
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0xFE,
        (
            "但惭愧得很，在现今的体制下，\x01",
            "是无法刊登有关总统不当行为\x01",
            "的报道的。\x02",
        )
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0xFE,
        (
            "所以我只有寄希望于\x01",
            "你们的突入作战\x01",
            "能顺利成功了！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_41CB")

    label("loc_366C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_37F0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3751")

    #C0164
    ChrTalk(
        0xFE,
        (
            "喂喂喂……\x01",
            "事态的发展未免也\x01",
            "太过突然了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0xFE,
        (
            "老实说，接下来\x01",
            "无论再发生什么也都不奇怪了……\x01",
            "但慌张也没用。\x02",
        )
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0xFE,
        (
            "总之，既然都已经这样了，\x01",
            "我们也只能做好最坏的心理准备，\x01",
            "尽量做好自己能做的事情了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_37EB")

    label("loc_3751")


    #C0167
    ChrTalk(
        0xFE,
        (
            "老实说，接下来\x01",
            "无论再发生什么也都不奇怪了……\x01",
            "但慌张也没用。\x02",
        )
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0xFE,
        (
            "总之，既然都已经这样了，\x01",
            "我们也只能做好最坏的心理准备，\x01",
            "尽量做好自己能做的事情了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_37EB")

    Jump("loc_41CB")

    label("loc_37F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_38A2")
    OP_4B(0xD, 0xFF)

    #C0169
    ChrTalk(
        0xFE,
        (
            "这段时间，袭击事件是帝国阴谋\x01",
            "的传闻已经在\x01",
            "市民群体中广为流传了。\x02",
        )
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0xFE,
        (
            "这种猜测的确很符合常理，\x01",
            "但妄下断言终究是很不妥的……\x01",
            "我们必须要想办法查明真相。\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xD, 0xFF)
    Jump("loc_41CB")

    label("loc_38A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 0)), scpexpr(EXPR_END)), "loc_38B0")
    Jump("loc_41CB")

    label("loc_38B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_39C1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3957")

    #C0171
    ChrTalk(
        0xFE,
        (
            "警备队现在的状况\x01",
            "似乎非常严峻呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0xFE,
        (
            "如果玛因兹一直被武装集团占领，\x01",
            "最终就会导致帝国军介入了吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0xFE,
        "哎呀呀，真是让人笑不出来啊。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_39BC")

    label("loc_3957")


    #C0174
    ChrTalk(
        0xFE,
        (
            "如果玛因兹一直被武装集团占领，\x01",
            "最终就会导致帝国军介入了吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0xFE,
        "哎呀呀，真是让人笑不出来啊。\x02",
    )

    CloseMessageWindow()

    label("loc_39BC")

    Jump("loc_41CB")

    label("loc_39C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3AC9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A66")

    #C0176
    ChrTalk(
        0xFE,
        (
            "呼，每次编辑速报的时候，\x01",
            "都觉得体力不够用啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0xFE,
        (
            "二十多岁的时候从来没有过这种感觉……\x01",
            "最近却经常觉得疲劳。\x02",
        )
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0xFE,
        "真是岁月不饶人啊。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3AC4")

    label("loc_3A66")


    #C0179
    ChrTalk(
        0xFE,
        (
            "呼，但话说回来，我也刚三十多岁而已。\x01",
            "正是年富力强\x01",
            "的时候啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0xFE,
        "不能轻易说这种泄气话。\x02",
    )

    CloseMessageWindow()

    label("loc_3AC4")

    Jump("loc_41CB")

    label("loc_3AC9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_3AD7")
    Jump("loc_41CB")

    label("loc_3AD7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3BB9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B9E")

    #C0181
    ChrTalk(
        0xFE,
        "（点烟）\x02",
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0xFE,
        (
            "好，在会议开始之前，\x01",
            "再次看一次资料吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0xFE,
        (
            "不管怎么说，今天的主题\x01",
            "可是关于独立的复杂问题。\x02",
        )
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0xFE,
        (
            "必须要在事前\x01",
            "了解各方面的要素，\x01",
            "才能在辩论时言之有物。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3BB4")

    label("loc_3B9E")


    #C0185
    ChrTalk(
        0xFE,
        "嗯，资料资料……\x02",
    )

    CloseMessageWindow()

    label("loc_3BB4")

    Jump("loc_41CB")

    label("loc_3BB9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3D56")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3CEC")

    #C0186
    ChrTalk(
        0xFE,
        (
            "从政治、经济方面的社会问题，\x01",
            "到文化、艺术方面的娱乐信息……\x02",
        )
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0xFE,
        (
            "本社记者们所负责的新闻报道，\x01",
            "种类丰富得让人吃惊。\x02",
        )
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0xFE,
        (
            "如果是规模更大的通讯社，\x01",
            "一般都会明确划分各种部门，\x01",
            "分工负责不同的领域……\x02",
        )
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0xFE,
        (
            "而本社则更加重视少数精锐人员的机动力。\x01",
            "几乎每个人都要负责\x01",
            "所有方面的内容。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3D51")

    label("loc_3CEC")


    #C0190
    ChrTalk(
        0xFE,
        (
            "今天下午有\x01",
            "三个采访任务……\x01",
            "专栏的文章也还差一点才能完成。\x02",
        )
    )

    CloseMessageWindow()

    #C0191
    ChrTalk(
        0xFE,
        (
            "唔，只能抽个空\x01",
            "迅速搞定专栏了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3D51")

    Jump("loc_41CB")

    label("loc_3D56")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3E71")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E17")

    #C0192
    ChrTalk(
        0xFE,
        (
            "在正式会议的现场，\x01",
            "各社的入内记者数量\x01",
            "都会受到限制。\x02",
        )
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0xFE,
        (
            "本社派遣\x01",
            "格蕾丝和雷因兹\x01",
            "进入会场。\x02",
        )
    )

    CloseMessageWindow()

    #C0194
    ChrTalk(
        0xFE,
        (
            "至于其他成员，则留在这里\x01",
            "等待格蕾丝他们的联络，\x01",
            "准备撰写速报。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3E6C")

    label("loc_3E17")


    #C0195
    ChrTalk(
        0xFE,
        (
            "格蕾丝、雷因兹组合的\x01",
            "采访能力可是社内\x01",
            "公认的。\x02",
        )
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0xFE,
        (
            "他们一定可以\x01",
            "顺利完成任务。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3E6C")

    Jump("loc_41CB")

    label("loc_3E71")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3F5E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F05")

    #C0197
    ChrTalk(
        0xFE,
        (
            "我刚刚把格蕾丝和雷因兹\x01",
            "拍摄的照片显像出来了。\x02",
        )
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0xFE,
        (
            "你们看，全都拍得\x01",
            "很不错吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0xFE,
        (
            "嗯，在号外刊物中\x01",
            "要选用哪张呢？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3F59")

    label("loc_3F05")


    #C0200
    ChrTalk(
        0xFE,
        (
            "这张和那张，还有右边那张\x01",
            "好像都不错。\x02",
        )
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0xFE,
        (
            "选好以后，还要再交给\x01",
            "总编检查一下。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3F59")

    Jump("loc_41CB")

    label("loc_3F5E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_40BE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4021")

    #C0202
    ChrTalk(
        0xFE,
        (
            "嘿，黑月费了那么多工夫，\x01",
            "最后却是被\x01",
            "深红商会捷足先登了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0203
    ChrTalk(
        0xFE,
        (
            "关于这家商会，不仅无法掌握他们的具体状况，\x01",
            "人脉管道也是深不见底。\x02",
        )
    )

    CloseMessageWindow()

    #C0204
    ChrTalk(
        0xFE,
        (
            "呼，暂时也只能\x01",
            "默默观望了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_40B9")

    label("loc_4021")


    #C0205
    ChrTalk(
        0xFE,
        (
            "通商会议总算要在\x01",
            "明天开始了……\x01",
            "在这种时候，四处弥漫着火药味也是没办法的事。\x02",
        )
    )

    CloseMessageWindow()

    #C0206
    ChrTalk(
        0xFE,
        (
            "算了，想这些也没用。\x01",
            "现在必须要集中精神\x01",
            "做好通商会议的相关报道。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_40B9")

    Jump("loc_41CB")

    label("loc_40BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_415B")

    #C0207
    ChrTalk(
        0xFE,
        (
            "（点烟）……\x01",
            "黑月盯上了鲁巴彻的旧址啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0208
    ChrTalk(
        0xFE,
        (
            "呼，既然如此，帝国方面\x01",
            "肯定也不会坐视不管吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0209
    ChrTalk(
        0xFE,
        (
            "哎呀呀……火药味\x01",
            "好像慢慢浓烈起来了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_41CB")

    label("loc_415B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_41CB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4176")
    Call(0, 15)
    Jump("loc_41CB")

    label("loc_4176")


    #C0210
    ChrTalk(
        0xFE,
        "呀，特意麻烦你，真不好意思啊。\x02",
    )

    CloseMessageWindow()

    #C0211
    ChrTalk(
        0xFE,
        (
            "这是树根蛋糕吗？\x01",
            "哈哈，你还是喜欢吃这个啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_41CB")

    TalkEnd(0xFE)
    Return()

    # Function_12_34FF end

    def Function_13_41CF(): pass

    label("Function_13_41CF")

    OP_4B(0xA, 0xFF)
    OP_4B(0x9, 0xFF)

    #C0212
    ChrTalk(
        0x9,
        (
            "喂，雷因兹，\x01",
            "准备好相机了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0213
    ChrTalk(
        0xA,
        "嗯，准备完毕了。\x02",
    )

    CloseMessageWindow()

    #C0214
    ChrTalk(
        0x9,
        (
            "好，那我们就\x01",
            "赶快前往兰花塔\x01",
            "采访吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0215
    ChrTalk(
        0x9,
        (
            "为了不输给格蕾丝，\x01",
            "我们也要加油！\x02",
        )
    )

    CloseMessageWindow()

    #C0216
    ChrTalk(
        0xA,
        "嗯，明白了！\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BF, 3)), scpexpr(EXPR_END)), "loc_42EC")

    #C0217
    ChrTalk(
        0x101,
        (
            "#00000F（雷因兹先生又重新\x01",
            "  恢复记者工作了啊。）\x02",
        )
    )

    CloseMessageWindow()

    #C0218
    ChrTalk(
        0x102,
        (
            "#00104F（两边的工作都不耽误……\x01",
            "  活力真是惊人啊。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_42EC")

    OP_4C(0xA, 0xFF)
    OP_4C(0x9, 0xFF)
    ClearChrFlags(0xA, 0x10)
    ClearChrFlags(0x9, 0x10)
    SetScenarioFlags(0x0, 3)
    Return()

    # Function_13_41CF end

    def Function_14_4302(): pass

    label("Function_14_4302")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_4313")
    Jump("loc_4488")

    label("loc_4313")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_4321")
    Jump("loc_4488")

    label("loc_4321")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_432F")
    Jump("loc_4488")

    label("loc_432F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_433D")
    Jump("loc_4488")

    label("loc_433D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_434B")
    Jump("loc_4488")

    label("loc_434B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_4359")
    Jump("loc_4488")

    label("loc_4359")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_4367")
    Jump("loc_4488")

    label("loc_4367")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_4375")
    Jump("loc_4488")

    label("loc_4375")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_4383")
    Jump("loc_4488")

    label("loc_4383")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_43F9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x148, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_439E")
    Call(0, 10)
    Jump("loc_43F4")

    label("loc_439E")


    #C0219
    ChrTalk(
        0xFE,
        (
            "哈哈，不愧是格蕾丝，\x01",
            "你已经看到了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0220
    ChrTalk(
        0xFE,
        (
            "我可以向你保证——\x01",
            "吃一口就会上瘾的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_43F4")

    Jump("loc_4488")

    label("loc_43F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_4407")
    Jump("loc_4488")

    label("loc_4407")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_4488")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4422")
    Call(0, 15)
    Jump("loc_4488")

    label("loc_4422")


    #C0221
    ChrTalk(
        0xFE,
        (
            "对了对了，我在共和国\x01",
            "发现了一家很不错的店。\x02",
        )
    )

    CloseMessageWindow()

    #C0222
    ChrTalk(
        0xFE,
        (
            "给大家带来了一些特产，\x01",
            "呵呵，你们一定会喜欢的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4488")

    TalkEnd(0xFE)
    Return()

    # Function_14_4302 end

    def Function_15_448C(): pass

    label("Function_15_448C")

    OP_4B(0xC, 0xFF)
    OP_4B(0x9, 0xFF)

    #C0223
    ChrTalk(
        0x9,
        (
            "哎呀～话说回来，\x01",
            "真是好久不见了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0224
    ChrTalk(
        0x9,
        (
            "你最后一次来这里，\x01",
            "已经是三年前的事情了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0xC,
        "嗯，正是那个时候。\x02",
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0xC,
        (
            "在这段时间，我将以\x01",
            "特别协商员的身份\x01",
            "出入这里。\x02",
        )
    )

    CloseMessageWindow()

    #C0227
    ChrTalk(
        0xC,
        (
            "给大家添麻烦了，\x01",
            "还请多多关照。\x02",
        )
    )

    CloseMessageWindow()

    #C0228
    ChrTalk(
        0x9,
        "哪里哪里，没有的事。\x02",
    )

    CloseMessageWindow()

    #C0229
    ChrTalk(
        0x9,
        (
            "如果有什么事情需要我们效劳，\x01",
            "请不必客气，尽管开口。\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x9, 0xFF)
    OP_4C(0xC, 0xFF)
    SetScenarioFlags(0x0, 4)
    SetScenarioFlags(0x0, 3)
    Return()

    # Function_15_448C end

    def Function_16_45C1(): pass

    label("Function_16_45C1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_45D2")
    Jump("loc_47C6")

    label("loc_45D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_4678")
    OP_4B(0x9, 0xFF)

    #C0230
    ChrTalk(
        0xFE,
        (
            "不管事实究竟如何，\x01",
            "帝国肯定不会承认\x01",
            "那起袭击事件是自己所为吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0xFE,
        (
            "面对这种状况，\x01",
            "帝国下一步将会有怎样的行动呢……\x01",
            "我们也只能密切关注了。\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x9, 0xFF)
    Jump("loc_47C6")

    label("loc_4678")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_4686")
    Jump("loc_47C6")

    label("loc_4686")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_4694")
    Jump("loc_47C6")

    label("loc_4694")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x163, 2)), scpexpr(EXPR_END)), "loc_46E5")

    #C0232
    ChrTalk(
        0xFE,
        (
            "嗯，编辑部似乎也比以前\x01",
            "更加忙乱了。\x02",
        )
    )

    CloseMessageWindow()

    #C0233
    ChrTalk(
        0xFE,
        "我还是告辞比较好呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_47C6")

    label("loc_46E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_4763")

    #C0234
    ChrTalk(
        0xFE,
        (
            "二层的各位正在以\x01",
            "最快速度来完成速报。\x02",
        )
    )

    CloseMessageWindow()

    #C0235
    ChrTalk(
        0xFE,
        (
            "该怎么说呢，不管是哪里的通讯社，\x01",
            "这种忙乱的气氛都是共通特色啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_47C6")

    label("loc_4763")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_4774")
    Call(0, 6)
    Jump("loc_47C6")

    label("loc_4774")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_4782")
    Jump("loc_47C6")

    label("loc_4782")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_4790")
    Jump("loc_47C6")

    label("loc_4790")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_47A1")
    Call(0, 7)
    Jump("loc_47C6")

    label("loc_47A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_47AF")
    Jump("loc_47C6")

    label("loc_47AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_47BD")
    Jump("loc_47C6")

    label("loc_47BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_47C6")

    label("loc_47C6")

    TalkEnd(0xFE)
    Return()

    # Function_16_45C1 end

    def Function_17_47CA(): pass

    label("Function_17_47CA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_4946")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_48A9")

    #C0236
    ChrTalk(
        0xFE,
        (
            "我和马凯奈以最快速度\x01",
            "完成了总统被捕的报道，\x01",
            "总算让刊物顺利发行了。\x02",
        )
    )

    CloseMessageWindow()

    #C0237
    ChrTalk(
        0xFE,
        (
            "顺便一说，其他记者\x01",
            "也立刻恢复采访工作了。\x02",
        )
    )

    CloseMessageWindow()

    #C0238
    ChrTalk(
        0xFE,
        (
            "今后就可以和格蕾丝\x01",
            "堂堂正正地取得联络了，\x01",
            "一定要收集到更多的情报啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_4941")

    label("loc_48A9")


    #C0239
    ChrTalk(
        0xFE,
        (
            "今后就可以和格蕾丝\x01",
            "堂堂正正地取得联络了，\x01",
            "一定要收集到更多的情报啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0240
    ChrTalk(
        0xFE,
        (
            "为了抑制市民们的混乱，\x01",
            "我们会竭尽全力，争分夺秒地\x01",
            "向大家传达正确的情报。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4941")

    Jump("loc_49E7")

    label("loc_4946")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_49E7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BF, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4965")
    TalkEnd(0xFE)
    Call(0, 18)
    Return()

    label("loc_4965")


    #C0241
    ChrTalk(
        0xFE,
        (
            "听说格蕾丝受到了\x01",
            "你们的帮助，\x01",
            "真是太感谢了。\x02",
        )
    )

    CloseMessageWindow()

    #C0242
    ChrTalk(
        0xFE,
        (
            "各位今后也务必要多加小心……\x01",
            "请一定让我有朝一日将你们的\x01",
            "活跃表现报道出来。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_49E7")

    TalkEnd(0xFE)
    Return()

    # Function_17_47CA end

    def Function_18_49EB(): pass

    label("Function_18_49EB")

    TalkBegin(0xFF)
    OP_4B(0x9, 0xFF)
    OP_4B(0x8, 0xFF)
    TurnDirection(0x9, 0x0, 0)
    TurnDirection(0x8, 0x0, 0)
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xE, 0x10)
    TurnDirection(0xE, 0x0, 0)
    OP_52(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4A95")
    Jump("loc_4ADF")

    label("loc_4A95")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4AB5")
    OP_52(0xE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4ADF")

    label("loc_4AB5")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4AD5")
    OP_52(0xE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4ADF")

    label("loc_4AD5")

    OP_52(0xE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4ADF")

    OP_52(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xE, 0x10)

    #C0243
    ChrTalk(
        0x9,
        "哦哦，这不是特别任务支援科吗！\x02",
    )

    CloseMessageWindow()

    #C0244
    ChrTalk(
        0x8,
        "各位，你们全都平安无事啊。\x02",
    )

    CloseMessageWindow()

    #C0245
    ChrTalk(
        0xE,
        (
            "唔，虽然这话不能大声说。\x01",
            "不过，有关你们的情况和活跃表现，\x01",
            "我基本都从格蕾丝那里了解到了。\x02",
        )
    )

    CloseMessageWindow()

    #C0246
    ChrTalk(
        0xE,
        (
            "如果可以，\x01",
            "针对如今的状况，\x01",
            "我们来交换一下情报如何？\x02",
        )
    )

    CloseMessageWindow()

    #C0247
    ChrTalk(
        0x101,
        "#00000F嗯，非常愿意。\x02",
    )

    CloseMessageWindow()
    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(61910, 1500, -2140, 0)
    MoveCamera(59, 22, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(21850, 0)
    SetChrPos(0x101, 62030, 0, -2100, 90)
    SetChrPos(0x102, 61830, 0, -1090, 90)
    SetChrPos(0x103, 61480, 0, -3030, 90)
    SetChrPos(0x104, 60040, 0, -1980, 90)
    SetChrPos(0xF4, 59440, 0, -990, 90)
    SetChrPos(0xF5, 59440, 0, -2990, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrChipByIndex(0xE, 0x9)
    ClearChrBattleFlags(0xE, 0x4)
    SetChrSubChip(0xE, 0x0)
    SetChrPos(0xE, 64370, 0, -1800, 270)
    SetChrPos(0x9, 63780, 0, -800, 270)
    SetChrPos(0x8, 64349, 0, -2890, 270)
    Sleep(1000)
    FadeToBright(1000, 0)
    OP_0D()

    #C0248
    ChrTalk(
        0xE,
        (
            "原来如此……也就是说，\x01",
            "接下来就要突入兰花塔了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0249
    ChrTalk(
        0x9,
        (
            "如果作战能取得成功，\x01",
            "这种独裁体制也就宣告破灭了。\x02",
        )
    )

    CloseMessageWindow()

    #C0250
    ChrTalk(
        0x9,
        (
            "真是的，独立无效宣言发表之后，\x01",
            "本以为行动能变得稍微自由些，\x01",
            "结果却下达了戒严令。\x02",
        )
    )

    CloseMessageWindow()

    #C0251
    ChrTalk(
        0x9,
        (
            "不知为何，自从那种\x01",
            "奇怪的雾气出现之后，\x01",
            "通讯器就变得非常不灵敏了。\x02",
        )
    )

    CloseMessageWindow()

    #C0252
    ChrTalk(
        0x102,
        (
            "#6P#00105F是吗，\x01",
            "连普通的导力通讯都……\x02",
        )
    )

    CloseMessageWindow()

    #C0253
    ChrTalk(
        0x103,
        (
            "#12P#00203F那种雾气中\x01",
            "恐怕含有某种\x01",
            "妨害波吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0254
    ChrTalk(
        0x104,
        (
            "#6P#00301F唔，如果不尽快行动，\x01",
            "混乱局面只会变得越来越严重啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0255
    ChrTalk(
        0x101,
        (
            "#6P#00003F嗯……是啊。\x02\x03",

            "#00000F顺便一问，贵社的\x01",
            "全体成员都在这里吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0256
    ChrTalk(
        0xE,
        (
            "哦，还有一些人员被\x01",
            "困在外出地点了。\x02",
        )
    )

    CloseMessageWindow()

    #C0257
    ChrTalk(
        0xE,
        (
            "目前已经和绝大部分人员\x01",
            "取得了联络……\x02",
        )
    )

    CloseMessageWindow()

    #C0258
    ChrTalk(
        0xE,
        (
            "但唯独联络不到\x01",
            "雷因兹。\x02",
        )
    )

    CloseMessageWindow()

    #C0259
    ChrTalk(
        0xE,
        (
            "他现在究竟\x01",
            "在什么地方呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0260
    ChrTalk(
        0x101,
        "#6P#00005F雷因兹先生……\x02",
    )

    CloseMessageWindow()

    #C0261
    ChrTalk(
        0xE,
        (
            "不过，他应该就在\x01",
            "市内的某个地方吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0262
    ChrTalk(
        0x8,
        (
            "但愿雷因兹没有\x01",
            "受格蕾丝小姐的影响，\x01",
            "去做一些很乱来的事情……\x02",
        )
    )

    CloseMessageWindow()

    #C0263
    ChrTalk(
        0xE,
        (
            "不过他也曾经历过危险场面，\x01",
            "这点小事情应该还\x01",
            "不必担心。\x02",
        )
    )

    CloseMessageWindow()

    #C0264
    ChrTalk(
        0xE,
        (
            "好了，我们的事情并不重要，\x01",
            "还是不要再占用\x01",
            "你们的宝贵时间了。\x02",
        )
    )

    CloseMessageWindow()

    #C0265
    ChrTalk(
        0x9,
        (
            "我们就留在这里，\x01",
            "在准备撰写速报的同时，\x01",
            "祈祷各位旗开得胜。\x02",
        )
    )

    CloseMessageWindow()

    #C0266
    ChrTalk(
        0x9,
        (
            "大家一定要取得胜利，\x01",
            "将这种禁锢的体制\x01",
            "彻底打破！\x02",
        )
    )

    CloseMessageWindow()

    #C0267
    ChrTalk(
        0x101,
        (
            "#6P#00000F嗯，明白了！\x02\x03",

            "#00003F（无法和雷因兹先生\x01",
            "  取得联络吗……）\x02\x03",

            "#00001F（格蕾丝小姐肯定也\x01",
            "  很担心他的安危，\x01",
            "  我们也多留意一下吧。）\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(500, 0, -1)
    OP_0D()
    SetChrPos(0x0, -6570, 20, 2860, 180)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetScenarioFlags(0x1BF, 0)
    EventEnd(0x5)
    Return()

    # Function_18_49EB end

    def Function_19_51CC(): pass

    label("Function_19_51CC")

    EventBegin(0x0)
    Fade(500)
    OP_68(4720, 1500, 56190, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(19720, 0)
    SetChrPos(0x101, 4520, 0, 56690, 90)
    SetChrPos(0x102, 4500, 0, 55000, 45)
    SetChrPos(0x103, 3360, 0, 56510, 90)
    SetChrPos(0x109, 4950, 0, 58190, 135)
    SetChrPos(0x105, 3550, 0, 57990, 135)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_93(0xB, 0x10E, 0x0)
    OP_93(0xA, 0x10E, 0x0)
    OP_4B(0xB, 0xFF)
    OP_4B(0xA, 0xFF)
    OP_0D()

    #C0268
    ChrTalk(
        0xA,
        "支援科的各位……\x02",
    )

    CloseMessageWindow()

    #C0269
    ChrTalk(
        0xB,
        (
            "#02101F各位，\x01",
            "情况真是很棘手啊。\x02\x03",

            "#02105F对了，兰迪……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0270
    ChrTalk(
        0xB,
        (
            "#02101F兰迪去哪里了？\x01",
            "难道……\x02",
        )
    )

    CloseMessageWindow()

    #C0271
    ChrTalk(
        0x101,
        "#6P#00003F……呃………\x02",
    )

    CloseMessageWindow()

    #C0272
    ChrTalk(
        0x102,
        "#6P#00108F……这个………\x02",
    )

    CloseMessageWindow()

    #C0273
    ChrTalk(
        0x101,
        (
            "#6P#00001F抱歉，关于此事，\x01",
            "以后有机会再谈吧。\x02\x03",

            "#00003F出发吧，各位。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x10E, 0x1F4)
    Sleep(300)
    OP_93(0x102, 0x0, 0x1F4)
    OP_63(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0274
    ChrTalk(
        0xB,
        (
            "#02101F等一下啊，罗伊德！\x02\x03",

            "#02104F我并不是想追问，\x01",
            "只是想『谈谈』，可以吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0275
    ChrTalk(
        0x101,
        "#6P#00005F哎……\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0x5A, 0x1F4)
    OP_93(0x102, 0x2D, 0x1F4)

    #C0276
    ChrTalk(
        0x109,
        "#6P#10105F那个，这是什么意思……\x02",
    )

    CloseMessageWindow()

    #C0277
    ChrTalk(
        0xB,
        (
            "#02101F先说前提……\x01",
            "关于兰迪的底细，\x01",
            "我也有一定程度的了解。\x02\x03",

            "#02103F这样说也许有些失礼，\x01",
            "但既然存在着一定的可疑性，\x01",
            "我便不可能没有丝毫怀疑。\x02\x03",

            "#02100F不过，至今为止，我也充分\x01",
            "见证了他在支援科的活跃表现。\x01",
            "以个人来说，我还是很信任他的。\x02",
        )
    )

    CloseMessageWindow()

    #C0278
    ChrTalk(
        0x102,
        "#6P#00105F格蕾丝小姐……\x02",
    )

    CloseMessageWindow()

    #C0279
    ChrTalk(
        0xB,
        (
            "#02103F另外，通过你们的反应，\x01",
            "我已经大概明白事情的情况了。\x02\x03",

            "#02101F兰迪一个人\x01",
            "前往玛因兹了吧？\x02\x03",

            "为了解决此事件。\x02",
        )
    )

    CloseMessageWindow()

    #C0280
    ChrTalk(
        0x101,
        "#6P#00001F……竟然连这都想到了。\x02",
    )

    CloseMessageWindow()

    #C0281
    ChrTalk(
        0x103,
        (
            "#6P#00203F……真不愧是\x01",
            "克洛斯贝尔时代周刊\x01",
            "的记者啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0282
    ChrTalk(
        0xB,
        (
            "#02102F呵呵，果然不出所料。\x02\x03",

            "#02103F而你们为了\x01",
            "将他带回，\x01",
            "才会展开行动……\x02\x03",

            "#02101F这个问题也许是多此一问了——\x01",
            "你们想必已经有了相应的觉悟吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0283
    ChrTalk(
        0x101,
        (
            "#6P#00001F当然！\x01",
            "因为兰迪是我们的同伴！\x02",
        )
    )

    CloseMessageWindow()

    #C0284
    ChrTalk(
        0x102,
        "#6P#00101F嗯，是的。\x02",
    )

    CloseMessageWindow()

    #C0285
    ChrTalk(
        0xB,
        (
            "#02104F原来如此，看来也\x01",
            "用不着我再说什么了啊。\x02\x03",

            "#02101F既然如此，\x01",
            "我就用自己的风格\x01",
            "来为各位加油吧。\x02\x03",

            "#02104F请一定要小心！\x02\x03",

            "#02109F以后还要让我\x01",
            "继续写特别任务支援科\x01",
            "大显身手的报道哦！\x02",
        )
    )

    CloseMessageWindow()

    #C0286
    ChrTalk(
        0x101,
        "#6P#00000F嗯，谢谢了。\x02",
    )

    CloseMessageWindow()
    OP_5A()
    OP_4C(0xB, 0xFF)
    OP_4C(0xA, 0xFF)
    OP_93(0xB, 0xB4, 0x0)
    OP_93(0xA, 0x0, 0x0)
    SetChrPos(0x0, 4720, 0, 56190, 90)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetScenarioFlags(0x171, 3)
    EventEnd(0x5)
    Return()

    # Function_19_51CC end

    def Function_20_5832(): pass

    label("Function_20_5832")

    EventBegin(0x0)
    Fade(500)
    OP_68(3050, 1520, -1840, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(20950, 0)
    SetChrPos(0x101, 2700, 20, -1900, 90)
    SetChrPos(0x102, 2700, 20, -800, 90)
    SetChrPos(0x103, 1500, 20, -1900, 90)
    SetChrPos(0x109, 1500, 20, -800, 90)
    SetChrPos(0x105, 300, 20, -1900, 90)
    SetChrPos(0x104, 300, 20, -800, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17D, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_59FE")

    #C0287
    ChrTalk(
        0x8,
        (
            "欢迎，\x01",
            "欢迎来访克洛斯贝尔通讯社。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0288
    ChrTalk(
        0x8,
        "啊，各位是特别任务支援科的……\x02",
    )

    CloseMessageWindow()

    #C0289
    ChrTalk(
        0x101,
        (
            "#00000F你好，我们是接到\x01",
            "支援请求而来的。\x02\x03",

            "听说有件美食向导的取材任务\x01",
            "需要协助……\x02",
        )
    )

    CloseMessageWindow()

    #C0290
    ChrTalk(
        0x8,
        (
            "呵呵，谢谢大家\x01",
            "特意过来。\x02",
        )
    )

    CloseMessageWindow()

    #C0291
    ChrTalk(
        0x8,
        (
            "虽然有些仓促，\x01",
            "不过可以请大家\x01",
            "现在接受委托吗？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x17D, 0)
    Jump("loc_5A4B")

    label("loc_59FE")


    #C0292
    ChrTalk(
        0x8,
        (
            "谢谢大家\x01",
            "特意过来。\x02",
        )
    )

    CloseMessageWindow()

    #C0293
    ChrTalk(
        0x8,
        (
            "虽然有些仓促，\x01",
            "不过可以请大家\x01",
            "现在接受委托吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5A4B")

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
            "接受\x01",      # 0
            "放弃\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5B16")

    #C0294
    ChrTalk(
        0x101,
        "#00000F嗯，没问题。\x02",
    )

    CloseMessageWindow()

    #C0295
    ChrTalk(
        0x8,
        "明白了。\x02",
    )

    CloseMessageWindow()

    #C0296
    ChrTalk(
        0x8,
        (
            "那么，负责人会向大家\x01",
            "说明委托内容，\x01",
            "请到二层稍等片刻吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Call(0, 21)
    Jump("loc_5BBF")

    label("loc_5B16")


    #C0297
    ChrTalk(
        0x101,
        (
            "#00006F抱歉，我们现在\x01",
            "还有其它事情……\x02",
        )
    )

    CloseMessageWindow()

    #C0298
    ChrTalk(
        0x8,
        (
            "啊，是吗……\x01",
            "那我就在这里等着各位。\x02",
        )
    )

    CloseMessageWindow()

    #C0299
    ChrTalk(
        0x8,
        (
            "等各位可以接受委托时，\x01",
            "还请尽早过来哦。\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, 2700, 20, -2000, 90)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)

    label("loc_5BBF")

    Return()

    # Function_20_5832 end

    def Function_21_5BC0(): pass

    label("Function_21_5BC0")

    OP_4B(0xB, 0xFF)
    SetChrChipByIndex(0xB, 0x4)
    SetChrSubChip(0xB, 0x2)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 60010, 150, 10690, 270)
    OP_68(57490, 1500, 11620, 0)
    MoveCamera(76, 28, -1, 0)
    OP_6E(400, 0)
    SetCameraDistance(19000, 0)
    SetChrPos(0x101, 58200, 0, 11760, 135)
    SetChrPos(0x102, 58650, 0, 12660, 135)
    SetChrPos(0x103, 57000, 0, 11920, 135)
    SetChrPos(0x109, 57480, 0, 13060, 135)
    SetChrPos(0x104, 55980, 0, 12490, 135)
    SetChrPos(0x105, 55580, 0, 11290, 90)
    FadeToBright(1000, 0)
    OP_0D()

    #C0300
    ChrTalk(
        0xB,
        (
            "#02100FＨＥＬＬＯ¤\x01",
            "特别任务支援科的各位。\x02\x03",

            "#02109F让大家久等了，\x01",
            "真抱歉哦～\x02",
        )
    )

    CloseMessageWindow()

    #C0301
    ChrTalk(
        0x101,
        (
            "#00006F负责人……果然是\x01",
            "格蕾丝小姐啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0302
    ChrTalk(
        0x103,
        "#00200F已经有所预料了。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_5DEB")

    #C0303
    ChrTalk(
        0xB,
        (
            "#02103F真是的，你们的反应好平淡～\x02\x03",

            "#02100F难得可以再次共事，\x01",
            "应该再开心些才对嘛。\x02",
        )
    )

    CloseMessageWindow()

    #C0304
    ChrTalk(
        0x102,
        (
            "#00109F啊哈哈……上次在克洛斯贝尔\x01",
            "各地东奔西跑，真是很辛苦呢。\x02\x03",

            "#00105F那么，这次的委托\x01",
            "是什么呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5EB1")

    label("loc_5DEB")


    #C0305
    ChrTalk(
        0xB,
        (
            "#02103F真是的，你们的反应好平淡～\x02\x03",

            "#02100F难得可以一起工作，\x01",
            "应该再开心些才对嘛。\x02",
        )
    )

    CloseMessageWindow()

    #C0306
    ChrTalk(
        0x102,
        (
            "#00109F啊、啊哈哈……\x01",
            "一想到委托和格蕾丝小姐有关，\x01",
            "总觉得会很麻烦呢。\x02\x03",

            "#00105F那么，这次的委托\x01",
            "是什么呢？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5EB1")


    #C0307
    ChrTalk(
        0x105,
        (
            "#10300F好像是要协助完成\x01",
            "美食向导的取材任务吧？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xB, 0x0)

    #C0308
    ChrTalk(
        0xB,
        (
            "#02100F嗯，正是。\x02\x03",

            "#02104F在不久之前，克洛斯贝尔\x01",
            "工商协会提议说『借着迪塔市长\x01",
            "的势头，策划一些助兴的活动』。\x02\x03",

            "#02102F通讯社也很赞同这个建议，\x01",
            "于是就决定和工商协会\x01",
            "联合举办美食向导活动。\x02",
        )
    )

    CloseMessageWindow()

    #C0309
    ChrTalk(
        0x109,
        (
            "#10105F联合举办美食向导活动……\x01",
            "具体内容是什么呢？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xB, 0x2)

    #C0310
    ChrTalk(
        0xB,
        (
            "#02104F主要就是介绍克洛斯贝尔\x01",
            "自治州内的饮食店……\x02\x03",

            "#02100F除了采访各个店铺之外，\x01",
            "还要邀请他们参与打折优惠\x01",
            "之类的协助活动。\x02\x03",

            "#02109F大致就是这样，\x01",
            "这个有趣的活动\x01",
            "正在进行之中。\x02",
        )
    )

    CloseMessageWindow()

    #C0311
    ChrTalk(
        0x101,
        (
            "#00000F原来如此……\x01",
            "这还真是前所未有的创意啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0312
    ChrTalk(
        0xB,
        (
            "#02109F说的没错！\x01",
            "但接下来才是问题的重点……\x02\x03",

            "#02100F在这个活动之中，\x01",
            "还包括『名人最中意的美味』\x01",
            "这个部分。\x02\x03",

            "#02104F像ＩＢＣ的玛丽亚贝尔小姐，\x01",
            "还有彩虹剧团的伊莉娅小姐、\x01",
            "缇奥多尔先生和尤金先生……\x02\x03",

            "#02102F曾在克洛斯贝尔时代周刊上\x01",
            "频繁露面的各界名人将会为\x01",
            "大家推荐一种美味。\x02\x03",

            "#02109F所以，我希望你们特别任务支援科\x01",
            "也来协助此次活动。\x02",
        )
    )

    CloseMessageWindow()

    #C0313
    ChrTalk(
        0x103,
        "#00200F嗯……这就是这次的委托啊。\x02",
    )

    CloseMessageWindow()

    #C0314
    ChrTalk(
        0x102,
        (
            "#00103F的确是个很有趣的企划……\x02\x03",

            "#00105F不过，在如此豪华的阵容之中，\x01",
            "让我们加入真的没问题吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0315
    ChrTalk(
        0x104,
        (
            "#00306F是啊，\x01",
            "能和伊莉娅小姐、玛丽亚贝尔小姐并列，\x01",
            "确实是让人开心……\x02\x03",

            "#00301F但如果把我们刊登上去，\x01",
            "报道会不会就变得\x01",
            "不那么引人注目了呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0316
    ChrTalk(
        0x105,
        (
            "#10304F呵呵，依我看，\x01",
            "只是让我们充当\x01",
            "陪衬角色而已吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0317
    ChrTalk(
        0xB,
        (
            "#02105F不不不，\x01",
            "绝不是什么陪衬！\x02\x03",

            "#02102F最近这段时间，支持你们的人\x01",
            "越来越多了哦。\x02\x03",

            "#02109F很多人还强烈要求\x01",
            "我们写一写各位的\x01",
            "私生活呢⊥\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0318
    ChrTalk(
        0x102,
        (
            "#00106F还、还是放过\x01",
            "我们吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0319
    ChrTalk(
        0xB,
        (
            "#02100F呵呵，总之，\x01",
            "你们也被很多人\x01",
            "关注着。\x02\x03",

            "#02104F若非如此，我也就不会\x01",
            "特意向你们发出这种委托了。\x02",
        )
    )

    CloseMessageWindow()

    #C0320
    ChrTalk(
        0x101,
        (
            "#00003F嗯，关于委托，我已经基本了解了。\x02\x03",

            "#00000F具体要怎么做呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0321
    ChrTalk(
        0xB,
        (
            "#02102F呵呵呵，那我就继续说明\x01",
            "采访的步骤啦。\x02\x03",

            "#02104F首先，要前往各地的\x01",
            "餐厅或露天饮食摊，\x01",
            "并亲口品尝其料理。\x02\x03",

            "#02109F希望你们每个人都能\x01",
            "从中发现自己\x01",
            "十分中意的料理。\x02\x03",

            "#02102F最后，还要请你们\x01",
            "回到通讯社，亲自撰写\x01",
            "相应的报道文章。\x02",
        )
    )

    CloseMessageWindow()

    #C0322
    ChrTalk(
        0x109,
        (
            "#10103F前往自治州内的各个饮食店，\x01",
            "并找到六人各自喜欢\x01",
            "的美食啊。\x02\x03",

            "#10105F可是，如果没能找到……\x02",
        )
    )

    CloseMessageWindow()

    #C0323
    ChrTalk(
        0xB,
        (
            "#02102F克洛斯贝尔如此广阔，\x01",
            "一定可以找到一种\x01",
            "自己喜欢的料理。\x02\x03",

            "#02104F如果实在找不到，\x01",
            "只要采访过六处饮食店，\x01",
            "也可以直接撰写报道。\x02\x03",

            "#2100F不过，还是希望\x01",
            "你们六人都能\x01",
            "介绍自己喜欢的美食哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0324
    ChrTalk(
        0x104,
        (
            "#00303F嗯，总之，\x01",
            "最少要采访六家\x01",
            "饮食店啊。\x02\x03",

            "#00300F还有什么其它的\x01",
            "注意事项吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0325
    ChrTalk(
        0xB,
        (
            "#02103F嗯，这个嘛……\x02\x03",

            "#02105F啊，对了，米修拉姆的店，\x01",
            "以及所有的『酒吧』\x01",
            "是排除在外的。\x02\x03",

            "#02102F那些店铺有其他人\x01",
            "负责采访～\x02",
        )
    )

    CloseMessageWindow()

    #C0326
    ChrTalk(
        0x105,
        (
            "#10303F嗯，也就是说，\x01",
            "旧城区的『崔尼蒂』\x01",
            "也在采访范围之外啊。\x02\x03",

            "#10300F呵呵，本以为是个难得\x01",
            "的宣传良机呢，\x01",
            "真是对不住阿巴斯啊。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xB, 0x0)

    #C0327
    ChrTalk(
        0xB,
        (
            "#02109F哎呀～真是抱歉啊，瓦吉！\x01",
            "因为我已经安排其他记者\x01",
            "去采访那些店了。\x02\x03",

            "#02104F……啊，对了，采访的事情，\x01",
            "已经和各个店铺交代过了，\x01",
            "不用担心费用方面的问题。\x02\x03",

            "#02102F只要把事情向店主讲清楚，\x01",
            "对方就会提供试吃料理的。\x02",
        )
    )

    CloseMessageWindow()

    #C0328
    ChrTalk(
        0x102,
        (
            "#00100F总之，酒吧除外，只要采访\x01",
            "最少六家饮食店就可以了吧？\x02\x03",

            "#00103F如果想把每个人喜欢\x01",
            "的料理都找到，\x01",
            "似乎需要相当的耐心呢……\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xB, 0x2)

    #C0329
    ChrTalk(
        0xB,
        (
            "#02104F呵呵，并不是特别着急的工作，\x01",
            "请大家加油吧。\x02\x03",

            "#02100F采访完成之后，\x01",
            "就可以回通讯社报告了。\x02\x03",

            "#02109F到时候，如果我不在通讯社，\x01",
            "只要让接待员托莉亚小姐联络一声，\x01",
            "我马上就会赶回来的！\x02",
        )
    )

    CloseMessageWindow()

    #C0330
    ChrTalk(
        0x101,
        (
            "#00000F嗯，明白了。\x01",
            "我们这就开始行动。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(300, 0, 100)
    Sound(80, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0331
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "任务【美食向导的协助取材】\x07\x00",
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
    SetScenarioFlags(0x0, 6)
    SetChrFlags(0xB, 0x80)
    SetChrPos(0x0, -6370, 250, 2630, 180)
    OP_69(0xFF, 0x0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetScenarioFlags(0x172, 0)
    OP_29(0x80, 0x1, 0x0)
    EventEnd(0x5)
    Return()

    # Function_21_5BC0 end

    def Function_22_6BDE(): pass

    label("Function_22_6BDE")

    EventBegin(0x0)
    Fade(500)
    OP_68(3050, 1520, -1840, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(20950, 0)
    SetChrPos(0x101, 2700, 20, -1900, 90)
    SetChrPos(0x102, 2700, 20, -800, 90)
    SetChrPos(0x103, 1500, 20, -1900, 90)
    SetChrPos(0x109, 1500, 20, -800, 90)
    SetChrPos(0x105, 300, 20, -1900, 90)
    SetChrPos(0x104, 300, 20, -800, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_0D()

    #C0332
    ChrTalk(
        0x8,
        "辛苦了，各位。\x02",
    )

    CloseMessageWindow()

    #C0333
    ChrTalk(
        0x8,
        (
            "你们在美食向导的任务中，\x01",
            "完成取材的饮食店数量\x01",
            "已经达到六家了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0334
    ChrTalk(
        0x8,
        (
            "现在就要向格蕾丝小姐\x01",
            "报告吗？\x02",
        )
    )

    CloseMessageWindow()
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
            "暂时不报告\x01",        # 0
            "向格蕾丝报告\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6DBE")

    #C0335
    ChrTalk(
        0x8,
        "明白了。\x02",
    )

    CloseMessageWindow()

    #C0336
    ChrTalk(
        0x8,
        (
            "我这就联系格蕾丝小姐，\x01",
            "请大家到二层\x01",
            "稍等片刻。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Jump("loc_6E1D")

    label("loc_6DBE")


    #C0337
    ChrTalk(
        0x8,
        "哦，这样啊。\x02",
    )

    CloseMessageWindow()

    #C0338
    ChrTalk(
        0x8,
        (
            "想报告的时候，\x01",
            "就再来和我说吧。\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, 2700, 20, -2000, 90)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    label("loc_6E1D")

    Return()

    # Function_22_6BDE end

    def Function_23_6E1E(): pass

    label("Function_23_6E1E")

    OP_4B(0xB, 0xFF)
    SetChrChipByIndex(0xB, 0x4)
    SetChrSubChip(0xB, 0x2)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 60010, 150, 10690, 270)
    OP_68(57490, 1500, 11620, 0)
    MoveCamera(76, 28, -1, 0)
    OP_6E(400, 0)
    SetCameraDistance(19000, 0)
    SetChrPos(0x101, 58200, 0, 11760, 135)
    SetChrPos(0x102, 58650, 0, 12660, 135)
    SetChrPos(0x103, 57000, 0, 11920, 135)
    SetChrPos(0x109, 57480, 0, 13060, 135)
    SetChrPos(0x104, 55980, 0, 12490, 135)
    SetChrPos(0x105, 55580, 0, 11290, 90)
    Sleep(1000)
    FadeToBright(1000, 0)
    OP_0D()

    #C0339
    ChrTalk(
        0xB,
        (
            "#02109F嗨，辛苦啦⊥\x02\x03",

            "#02102F『美食向导』的取材工作\x01",
            "做得怎么样了～？\x02",
        )
    )

    CloseMessageWindow()

    #C0340
    ChrTalk(
        0x101,
        (
            "#00009F哈哈，这个嘛……\x01",
            "工作过程让人很享受呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0341
    ChrTalk(
        0x104,
        (
            "#00306F不过到处跑来跑去，\x01",
            "也真是够累的。\x02",
        )
    )

    CloseMessageWindow()

    #C0342
    ChrTalk(
        0xB,
        (
            "#02100F呵呵，品尝到了那么多美食，\x01",
            "不是很不错嘛。\x02\x03",

            "#02109F好，那就赶快让我听听\x01",
            "你们的采访结果吧！\x02",
        )
    )

    CloseMessageWindow()

    #C0343
    ChrTalk(
        0x101,
        "#00000F嗯，那么……\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    #A0344
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "罗伊德等人将采访过的店铺\x01",
            "做了报告。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 7)), scpexpr(EXPR_END)), "loc_705A")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_705A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 1)), scpexpr(EXPR_END)), "loc_706D")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_706D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 1)), scpexpr(EXPR_END)), "loc_7080")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_7080")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 2)), scpexpr(EXPR_END)), "loc_7093")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_7093")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 5)), scpexpr(EXPR_END)), "loc_70A6")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_70A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 3)), scpexpr(EXPR_END)), "loc_70B9")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_70B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 3)), scpexpr(EXPR_END)), "loc_70CC")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_70CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 4)), scpexpr(EXPR_END)), "loc_70DF")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_70DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 6)), scpexpr(EXPR_END)), "loc_70F2")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_70F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 0)), scpexpr(EXPR_END)), "loc_7105")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_7105")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 2)), scpexpr(EXPR_END)), "loc_7118")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_7118")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_71CE")

    #C0345
    ChrTalk(
        0xB,
        (
            "#02104F嗯嗯，你们一共采访了\x01",
            "十一家店呢。\x02\x03",

            "#02109F看来你们真是\x01",
            "相当敬业啊～！\x01",
            "呵呵，姐姐好高兴！\x02\x03",

            "#02102F好，接下来……\x01",
            "就把你们发现的\x01",
            "『中意料理』告诉我吧！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_74F8")

    label("loc_71CE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7271")

    #C0346
    ChrTalk(
        0xB,
        (
            "#02104F嗯嗯，你们一共采访了\x01",
            "十家店呢。\x02\x03",

            "#02102F呵呵，圆满完成了\x01",
            "采访工作啊。\x02\x03",

            "#02100F好，接下来……\x01",
            "就把你们发现的\x01",
            "『中意料理』告诉我吧！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_74F8")

    label("loc_7271")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7314")

    #C0347
    ChrTalk(
        0xB,
        (
            "#02104F嗯嗯，你们一共采访了\x01",
            "九家店呢。\x02\x03",

            "#02102F呵呵，圆满完成了\x01",
            "采访工作啊。\x02\x03",

            "#02100F好，接下来……\x01",
            "就把你们发现的\x01",
            "『中意料理』告诉我吧！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_74F8")

    label("loc_7314")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_73B7")

    #C0348
    ChrTalk(
        0xB,
        (
            "#02104F嗯嗯，你们一共采访了\x01",
            "八家店呢。\x02\x03",

            "#02102F呵呵，圆满完成了\x01",
            "采访工作啊。\x02\x03",

            "#02100F好，接下来……\x01",
            "就把你们发现的\x01",
            "『中意料理』告诉我吧！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_74F8")

    label("loc_73B7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_745A")

    #C0349
    ChrTalk(
        0xB,
        (
            "#02104F嗯嗯，你们一共采访了\x01",
            "七家店呢。\x02\x03",

            "#02102F呵呵，圆满完成了\x01",
            "采访工作啊。\x02\x03",

            "#02100F好，接下来……\x01",
            "就把你们发现的\x01",
            "『中意料理』告诉我吧！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_74F8")

    label("loc_745A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_74F8")

    #C0350
    ChrTalk(
        0xB,
        (
            "#02104F嗯嗯，你们一共采访了\x01",
            "六家店呢。\x02\x03",

            "#02102F呵呵，圆满完成了\x01",
            "采访工作啊。\x02\x03",

            "#02100F好，接下来……\x01",
            "就把你们发现的\x01",
            "『中意料理』告诉我吧！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_74F8")

    Fade(500)
    OP_68(58050, 1900, 10380, 0)
    MoveCamera(12, 26, -1, 0)
    OP_6E(400, 0)
    SetCameraDistance(17470, 0)
    OP_0D()
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 7)), scpexpr(EXPR_END)), "loc_7608")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    #C0351
    ChrTalk(
        0x101,
        (
            "#00000F我最喜欢的料理是\x01",
            "阿尔摩利卡村酒馆『白蜡亭』的\x01",
            "『大师蛋包饭』。\x02\x03",

            "#00002F阿尔摩利卡村特有的质朴风味\x01",
            "触动了我的心弦。\x02",
        )
    )

    CloseMessageWindow()

    #C0352
    ChrTalk(
        0xB,
        (
            "#02102F原来如此，那里的蛋包饭\x01",
            "的确有着独一无二的味道啊～！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7608")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 1)), scpexpr(EXPR_END)), "loc_76E4")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    #C0353
    ChrTalk(
        0x102,
        (
            "#00104F我最喜欢的料理是\x01",
            "乌尔斯拉医院招待所『雷克切』的\x01",
            "『三日久煮炖菜』。\x02\x03",

            "#00109F经过长时间的炖煮，入口即化，\x01",
            "而且似乎对身体很有益处。\x02",
        )
    )

    CloseMessageWindow()

    #C0354
    ChrTalk(
        0xB,
        (
            "#02109F嗯嗯，只要吃了那个炖菜，\x01",
            "马上就觉得精力十足呢！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_76E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 1)), scpexpr(EXPR_END)), "loc_77D5")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    #C0355
    ChrTalk(
        0x103,
        (
            "#00204F我想推荐的是欢乐街冰激凌车的\x01",
            "冰凉甜点『七彩』。\x02\x03",

            "#00202F那种不可思议的口感与七种不同的味道……\x01",
            "完全颠覆了我以前对冰激凌的认知，堪称极品。\x02",
        )
    )

    CloseMessageWindow()

    #C0356
    ChrTalk(
        0xB,
        (
            "#02105F哦哦，缇欧对它的评价好高啊！\x01",
            "看来那里以后一定会很受欢迎～！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_77D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 2)), scpexpr(EXPR_END)), "loc_78B8")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    #C0357
    ChrTalk(
        0x104,
        (
            "#00300F我推荐港湾区汤面摊子的\x01",
            "天上面『日轮』。\x02\x03",

            "#00309F口感筋道的面条，\x01",
            "再加上那鲜红的辣汤……\x01",
            "光是想想，就要流口水了。\x02",
        )
    )

    CloseMessageWindow()

    #C0358
    ChrTalk(
        0xB,
        (
            "#02104F嗯嗯，我中午也经常\x01",
            "去那家摊子吃面呢。\x01",
            "老板对面条的执著的确是非同一般～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_78B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 5)), scpexpr(EXPR_END)), "loc_7988")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    #C0359
    ChrTalk(
        0x109,
        (
            "#10107F我推荐东街『龙老饭店』的\x01",
            "『天下一品炒饭』！\x02\x03",

            "#10104F看似简单，却让人回味无穷，\x01",
            "只要吃上一口就停不住了！\x02",
        )
    )

    CloseMessageWindow()

    #C0360
    ChrTalk(
        0xB,
        (
            "#02109F是强霍先生的得意料理呢！\x01",
            "嗯，听你这么一说，\x01",
            "我又想去吃了呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7988")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 3)), scpexpr(EXPR_END)), "loc_7A62")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    #C0361
    ChrTalk(
        0x105,
        (
            "#10304F我最满意的料理是唐古拉姆门食堂的\x01",
            "『芳醇潮锅』。\x02\x03",

            "#10302F味道很不错，在多人聚会聊天时，\x01",
            "没有比这更合适的料理了。\x02",
        )
    )

    CloseMessageWindow()

    #C0362
    ChrTalk(
        0xB,
        (
            "#02102F边境大门的食堂中\x01",
            "还隐藏着如此美食啊！\x01",
            "呵呵，连瓦吉都予以认可。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7A62")


    #C0363
    ChrTalk(
        0x101,
        (
            "#00004F……要报告的就是\x01",
            "以上这些了。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_7BED")
    OP_2C(0x80, 0x2)
    OP_63(0xB, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)

    #C0364
    ChrTalk(
        0xB,
        (
            "#02102F嗯嗯，看来你们\x01",
            "顺利找到了所有人的\x01",
            "『中意料理』啊。\x02\x03",

            "#02104F这样一来，美食向导的专栏\x01",
            "肯定能做得非常充实。\x02\x03",

            "#02109F真是太谢谢大家了！\x02",
        )
    )

    CloseMessageWindow()

    #C0365
    ChrTalk(
        0x101,
        "#00000F哈哈，谢谢夸奖。\x02",
    )

    CloseMessageWindow()

    #C0366
    ChrTalk(
        0x103,
        "#00202F我们努力寻找，总算是有了价值啊。\x02",
    )

    CloseMessageWindow()

    #C0367
    ChrTalk(
        0xB,
        (
            "#02105F对了，工作还没有结束哦。\x02\x03",

            "#02102F请大家赶快写好\x01",
            "自己负责的介绍文章吧！\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x80, 0x1, 0xF)
    Jump("loc_7E98")

    label("loc_7BED")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_7D46")
    OP_2C(0x80, 0x1)

    #C0368
    ChrTalk(
        0xB,
        (
            "#02106F唔，终究还是没有\x01",
            "找到所有人的\x01",
            "『中意料理』啊。\x02\x03",

            "#02102F算啦，也算是合格了，\x01",
            "先向各位道声谢吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0369
    ChrTalk(
        0x101,
        "#00012F谢、谢谢夸奖。\x02",
    )

    CloseMessageWindow()

    #C0370
    ChrTalk(
        0x103,
        (
            "#00206F（我们要是再努力\x01",
            "  一些就好了啊……）\x02",
        )
    )

    CloseMessageWindow()

    #C0371
    ChrTalk(
        0xB,
        (
            "#02104F不过，没找到中意料理的人\x01",
            "应该也发现了几种\x01",
            "基本满意的料理吧？\x02\x03",

            "#02102F想办法把不足的部分补上，\x01",
            "尽快把介绍文章\x01",
            "写完吧！\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x80, 0x1, 0x10)
    Jump("loc_7E98")

    label("loc_7D46")

    OP_63(0xB, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0372
    ChrTalk(
        0xB,
        (
            "#02105F哎？你们发现的\x01",
            "『中意料理』只有这么少吗？\x02\x03",

            "#02106F唔，真是没办法……\x01",
            "哪怕稍微再多些，都还能想办法解决。\x02",
        )
    )

    CloseMessageWindow()

    #C0373
    ChrTalk(
        0x101,
        "#00006F真、真是惭愧。\x02",
    )

    CloseMessageWindow()

    #C0374
    ChrTalk(
        0x103,
        "#00206F（要是再努力些就好了……）\x02",
    )

    CloseMessageWindow()

    #C0375
    ChrTalk(
        0xB,
        (
            "#02103F……算了，这也没办法。\x01",
            "你们至少完成了最低限度的采访。\x02\x03",

            "#02100F想办法把不足的部分补上，\x01",
            "尽快把介绍文章\x01",
            "写完吧！\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x80, 0x1, 0x11)

    label("loc_7E98")

    FadeToDark(2000, 0, -1)
    OP_0D()
    SetChrName("")

    #A0376
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "之后，罗伊德等人\x01",
            "拼命完成自己\x01",
            "很不擅长的写作……\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrName("")

    #A0377
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "总算完成了美食向导\x01",
            "栏目中的『中意料理』\x01",
            "介绍文章。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_68(57490, 1500, 11620, 0)
    MoveCamera(76, 28, -1, 0)
    OP_6E(400, 0)
    SetCameraDistance(19000, 0)
    FadeToBright(2000, 0)
    OP_0D()

    #C0378
    ChrTalk(
        0xB,
        (
            "#02100F嗯，这样就可以了。\x02\x03",

            "#02104F我稍后还要再校对一下，\x01",
            "总之就先这样吧！\x02\x03",

            "#02102F呵呵，多亏大家的帮忙，\x01",
            "应该能刊登出一篇\x01",
            "很有趣的美食向导专栏呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0379
    ChrTalk(
        0x109,
        "#10109F哈哈，真是很辛苦啊……\x02",
    )

    CloseMessageWindow()

    #C0380
    ChrTalk(
        0x105,
        (
            "#10304F总之，我们的任务\x01",
            "已经完成了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0381
    ChrTalk(
        0xB,
        (
            "#02104F嗯，真是多谢帮忙。\x02\x03",

            "#02109F这篇报道还要再过\x01",
            "一段时间才能正式发表，\x01",
            "请尽情期待吧！\x02\x03",

            "#02102F如果以后再有什么事情，还要请大家多帮忙哦～¤\x02",
        )
    )

    CloseMessageWindow()

    #C0382
    ChrTalk(
        0x101,
        "#00000F嗯，那我们就先告辞了。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0383
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "任务【美食向导的协助取材】\x07\x00",
            "完成！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x0, 6)
    OP_29(0x80, 0x1, 0x12)
    OP_29(0x80, 0x4, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 1)), scpexpr(EXPR_END)), "loc_8169")
    OP_50(0x66, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8169")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 2)), scpexpr(EXPR_END)), "loc_817B")
    OP_50(0x67, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_817B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 5)), scpexpr(EXPR_END)), "loc_818D")
    OP_50(0x68, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_818D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 1)), scpexpr(EXPR_END)), "loc_819F")
    OP_50(0x65, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_819F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 3)), scpexpr(EXPR_END)), "loc_81B1")
    OP_50(0x69, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_81B1")

    SetChrFlags(0xB, 0x80)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, -6370, 250, 2630, 180)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_23_6E1E end

    def Function_24_81E2(): pass

    label("Function_24_81E2")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_81EC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_857A")
    MenuCmd(0, 1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 1)), scpexpr(EXPR_END)), "loc_821A")
    MenuCmd(1, 1, "★妖精雪糕")
    Jump("loc_8226")

    label("loc_821A")

    MenuCmd(1, 1, "妖精雪糕")

    label("loc_8226")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 2)), scpexpr(EXPR_END)), "loc_8240")
    MenuCmd(1, 1, "★凤凰面")
    Jump("loc_824A")

    label("loc_8240")

    MenuCmd(1, 1, "凤凰面")

    label("loc_824A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 3)), scpexpr(EXPR_END)), "loc_8268")
    MenuCmd(1, 1, "★会心香草面")
    Jump("loc_8276")

    label("loc_8268")

    MenuCmd(1, 1, "会心香草面")

    label("loc_8276")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 4)), scpexpr(EXPR_END)), "loc_8296")
    MenuCmd(1, 1, "★苦西红柿苏打")
    Jump("loc_82A6")

    label("loc_8296")

    MenuCmd(1, 1, "苦西红柿苏打")

    label("loc_82A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 5)), scpexpr(EXPR_END)), "loc_82C6")
    MenuCmd(1, 1, "★超拉麻婆豆腐")
    Jump("loc_82D6")

    label("loc_82C6")

    MenuCmd(1, 1, "超拉麻婆豆腐")

    label("loc_82D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 6)), scpexpr(EXPR_END)), "loc_82F6")
    MenuCmd(1, 1, "★晚霞牛角面包")
    Jump("loc_8306")

    label("loc_82F6")

    MenuCmd(1, 1, "晚霞牛角面包")

    label("loc_8306")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 7)), scpexpr(EXPR_END)), "loc_8324")
    MenuCmd(1, 1, "★大师蛋包饭")
    Jump("loc_8332")

    label("loc_8324")

    MenuCmd(1, 1, "大师蛋包饭")

    label("loc_8332")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 0)), scpexpr(EXPR_END)), "loc_834E")
    MenuCmd(1, 1, "★超厚牛排")
    Jump("loc_835A")

    label("loc_834E")

    MenuCmd(1, 1, "超厚牛排")

    label("loc_835A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 1)), scpexpr(EXPR_END)), "loc_8378")
    MenuCmd(1, 1, "★全熟炖牛肉")
    Jump("loc_8386")

    label("loc_8378")

    MenuCmd(1, 1, "全熟炖牛肉")

    label("loc_8386")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 2)), scpexpr(EXPR_END)), "loc_83A4")
    MenuCmd(1, 1, "★梦幻咖喱锅")
    Jump("loc_83B2")

    label("loc_83A4")

    MenuCmd(1, 1, "梦幻咖喱锅")

    label("loc_83B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 3)), scpexpr(EXPR_END)), "loc_83D0")
    MenuCmd(1, 1, "★风味豆乳锅")
    Jump("loc_83DE")

    label("loc_83D0")

    MenuCmd(1, 1, "风味豆乳锅")

    label("loc_83DE")

    MenuCmd(1, 1, "放弃")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuCmd(2, 1, -1, -1, 0)
    MenuEnd(0x0)
    OP_60(0x1)
    OP_57(0x0)
    OP_5A()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_8453"),
        (1, "loc_846C"),
        (2, "loc_8485"),
        (3, "loc_849E"),
        (4, "loc_84B7"),
        (5, "loc_84D0"),
        (6, "loc_84E9"),
        (7, "loc_8502"),
        (8, "loc_851B"),
        (9, "loc_8534"),
        (10, "loc_854D"),
        (11, "loc_8566"),
        (SWITCH_DEFAULT, "loc_8575"),
    )


    label("loc_8453")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 1)), scpexpr(EXPR_END)), "loc_8464")
    ClearScenarioFlags(0x172, 1)
    Jump("loc_8467")

    label("loc_8464")

    SetScenarioFlags(0x172, 1)

    label("loc_8467")

    Jump("loc_8575")

    label("loc_846C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 2)), scpexpr(EXPR_END)), "loc_847D")
    ClearScenarioFlags(0x172, 2)
    Jump("loc_8480")

    label("loc_847D")

    SetScenarioFlags(0x172, 2)

    label("loc_8480")

    Jump("loc_8575")

    label("loc_8485")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 3)), scpexpr(EXPR_END)), "loc_8496")
    ClearScenarioFlags(0x172, 3)
    Jump("loc_8499")

    label("loc_8496")

    SetScenarioFlags(0x172, 3)

    label("loc_8499")

    Jump("loc_8575")

    label("loc_849E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 4)), scpexpr(EXPR_END)), "loc_84AF")
    ClearScenarioFlags(0x172, 4)
    Jump("loc_84B2")

    label("loc_84AF")

    SetScenarioFlags(0x172, 4)

    label("loc_84B2")

    Jump("loc_8575")

    label("loc_84B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 5)), scpexpr(EXPR_END)), "loc_84C8")
    ClearScenarioFlags(0x172, 5)
    Jump("loc_84CB")

    label("loc_84C8")

    SetScenarioFlags(0x172, 5)

    label("loc_84CB")

    Jump("loc_8575")

    label("loc_84D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 6)), scpexpr(EXPR_END)), "loc_84E1")
    ClearScenarioFlags(0x172, 6)
    Jump("loc_84E4")

    label("loc_84E1")

    SetScenarioFlags(0x172, 6)

    label("loc_84E4")

    Jump("loc_8575")

    label("loc_84E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 7)), scpexpr(EXPR_END)), "loc_84FA")
    ClearScenarioFlags(0x172, 7)
    Jump("loc_84FD")

    label("loc_84FA")

    SetScenarioFlags(0x172, 7)

    label("loc_84FD")

    Jump("loc_8575")

    label("loc_8502")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 0)), scpexpr(EXPR_END)), "loc_8513")
    ClearScenarioFlags(0x173, 0)
    Jump("loc_8516")

    label("loc_8513")

    SetScenarioFlags(0x173, 0)

    label("loc_8516")

    Jump("loc_8575")

    label("loc_851B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 1)), scpexpr(EXPR_END)), "loc_852C")
    ClearScenarioFlags(0x173, 1)
    Jump("loc_852F")

    label("loc_852C")

    SetScenarioFlags(0x173, 1)

    label("loc_852F")

    Jump("loc_8575")

    label("loc_8534")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 2)), scpexpr(EXPR_END)), "loc_8545")
    ClearScenarioFlags(0x173, 2)
    Jump("loc_8548")

    label("loc_8545")

    SetScenarioFlags(0x173, 2)

    label("loc_8548")

    Jump("loc_8575")

    label("loc_854D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 3)), scpexpr(EXPR_END)), "loc_855E")
    ClearScenarioFlags(0x173, 3)
    Jump("loc_8561")

    label("loc_855E")

    SetScenarioFlags(0x173, 3)

    label("loc_8561")

    Jump("loc_8575")

    label("loc_8566")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8575")

    label("loc_8575")

    Jump("loc_81EC")

    label("loc_857A")

    Return()

    # Function_24_81E2 end

    def Function_25_857B(): pass

    label("Function_25_857B")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0384
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "赶赴「百日战役」的战地现场，\x01",
            "进行了长达三个月的连载报道，\x01",
            "报道内容诚实可信，充满正义感。\x02\x03",

            "为赞扬此功绩，\x01",
            "特此颁发菲利策奖。\x01",
            "Ｓ１１９２　１１月\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_25_857B end

    def Function_26_8642(): pass

    label("Function_26_8642")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_864C")
    Return()

    label("loc_864C")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_87DE")

    #C0385
    ChrTalk(
        0x8,
        "啊，各位……！\x02",
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_86BC():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_86BC)
    Sleep(50)

    def lambda_86CC():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x1, 2, lambda_86CC)
    Sleep(50)

    def lambda_86DC():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x2, 2, lambda_86DC)
    Sleep(50)

    def lambda_86EC():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x3, 2, lambda_86EC)
    Sleep(50)

    def lambda_86FC():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x4, 2, lambda_86FC)
    Sleep(50)

    def lambda_870C():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x5, 2, lambda_870C)
    WaitChrThread(0x0, 2)
    Fade(1000)
    OP_68(-2860, 1510, 720, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(420, 0)
    SetCameraDistance(25500, 0)
    OP_0D()

    #C0386
    ChrTalk(
        0x8,
        (
            "不好意思，一般情况下，\x01",
            "二层的编辑部是禁止\x01",
            "无关人员入内的。\x02",
        )
    )

    CloseMessageWindow()

    #C0387
    ChrTalk(
        0x8,
        "如果有什么事情，就请和我说吧。\x02",
    )

    CloseMessageWindow()

    #C0388
    ChrTalk(
        0x101,
        (
            "#00005F对、对不起，\x01",
            "真是失礼了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_881A")

    label("loc_87DE")


    #C0389
    ChrTalk(
        0x101,
        (
            "#00000F二层好像禁止外部人员上去，\x01",
            "还是不要随便上去了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_881A")

    Sleep(50)
    SetChrPos(0x0, -6370, 20, 2470, 180)
    EventEnd(0x4)
    Return()

    # Function_26_8642 end

    def Function_27_8831(): pass

    label("Function_27_8831")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)

    #A0390
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "资料架上摆放着克洛斯贝尔\x01",
            "时代周刊的往期刊物。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "【阅读０４年度前期①】\x01",      # 0
            "【阅读０４年度前期②】\x01",      # 1
            "【放弃】\x01",                    # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_89E9")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "【克洛斯贝尔时代周刊①】\x01",          # 0
            "【克洛斯贝尔时代周刊②】\x01",          # 1
            "【克洛斯贝尔时代周刊③】\x01",          # 2
            "【克洛斯贝尔时代周刊·号外】\x01",      # 3
            "【克洛斯贝尔时代周刊④】\x01",          # 4
            "【放弃】\x01",                          # 5
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8994")
    UseItem(0x2BC, 0xFF)

    label("loc_8994")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_89A8")
    UseItem(0x2BD, 0xFF)

    label("loc_89A8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_89BC")
    UseItem(0x2BE, 0xFF)

    label("loc_89BC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_89D0")
    UseItem(0x2BF, 0xFF)

    label("loc_89D0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_89E4")
    UseItem(0x2C0, 0xFF)

    label("loc_89E4")

    Jump("loc_8AE5")

    label("loc_89E9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8ADC")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "【克洛斯贝尔时代周刊⑤】\x01",      # 0
            "【克洛斯贝尔时代周刊⑥】\x01",      # 1
            "【克洛斯贝尔时代周刊⑦】\x01",      # 2
            "【克洛斯贝尔时代周刊⑧】\x01",      # 3
            "【放弃】\x01",                      # 4
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8A9B")
    UseItem(0x2C1, 0xFF)

    label("loc_8A9B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8AAF")
    UseItem(0x2C2, 0xFF)

    label("loc_8AAF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8AC3")
    UseItem(0x2C3, 0xFF)

    label("loc_8AC3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8AD7")
    UseItem(0x2C4, 0xFF)

    label("loc_8AD7")

    Jump("loc_8AE5")

    label("loc_8ADC")

    FadeToBright(300, 0)

    label("loc_8AE5")

    TalkEnd(0xFF)
    Return()

    # Function_27_8831 end

    SaveToFile()

Try(main)
