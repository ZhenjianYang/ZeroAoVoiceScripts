from ScenarioHelper import *

def main():
    CreateScenaFile(
        "c010b.bin",                # FileName
        "c010b",                    # MapName
        "c010b",                    # Location
        0x0004,                     # MapIndex
        "ed7513",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x1E,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\x03',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 4, 0, 4, 0, 5],
    )

    BuildStringList((
        "c010b",                  # 0
        "吉娜",                   # 1
        "昆提老人",               # 2
        "亚贝尔",                 # 3
        "米米",                   # 4
        "普鲁娜",                 # 5
        "利娜莉",                 # 6
        "哈斯",                   # 7
        "萨莉",                   # 8
        "警官",                   # 9
        "警官",                   # 10
        "柯贝",                   # 11
        "琪雅",                   # 12
        "蔡特",                   # 13
        "谢莉",                   # 14
        "猎兵加雷斯",             # 15
        "车",                     # 16
        "模型",                   # 17
        "警官",                   # 18
        "凯特巡警",               # 19
        "市民１",                 # 20
        "SE控制",                 # 21
        "中央广场",               # 22
        "西街",                   # 23
        "行政区",                 # 24
        "住宅街",                 # 25
        "欢乐街",                 # 26
        "东街",                   # 27
        "旧城区",                 # 28
        "港湾区",                 # 29
        "ＩＢＣ",                 # 30
        "站前街道",               # 31
        "后巷",                   # 32
        "乌尔斯拉间道",           # 33
        "东克洛斯贝尔街道",       # 34
        "西克洛斯贝尔街道",       # 35
        "玛因兹山道",             # 36
        "兰花塔",                 # 37
    ))

    AddCharChip((
        "chr/ch21300.itc",                   # 00
        "chr/ch20002.itc",                   # 01
        "chr/ch20200.itc",                   # 02
        "chr/ch20700.itc",                   # 03
        "chr/ch34600.itc",                   # 04
        "chr/ch22100.itc",                   # 05
        "chr/ch20500.itc",                   # 06
        "chr/ch26000.itc",                   # 07
        "chr/ch30000.itc",                   # 08
        "chr/ch39200.itc",                   # 09
    ))

    DeclNpc(12619,   0,       2160,    90,   261,  0x0, 0,   0,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(-6090,   150,     4449,    270,  325,  0x0, 0,   1,   0,   255, 255, 0,   7,   255,  0)
    DeclNpc(-6099,   0,       -9409,   90,   389,  0x0, 0,   2,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(-289,    0,       -10319,  225,  261,  0x0, 0,   3,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(850,     0,       17969,   90,   277,  0x0, 0,   6,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(2539,    0,       17870,   270,  277,  0x0, 0,   5,   0,   0,   0,   0,   13,  255,  0)
    DeclNpc(14130,   0,       340,     270,  261,  0x0, 0,   7,   0,   0,   0,   0,   14,  255,  0)
    DeclNpc(-6099,   0,       -9409,   90,   389,  0x0, 0,   4,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(13850,   0,       24000,   180,  385,  0x0, 0,   8,   0,   0,   0,   0,   15,  255,  0)
    DeclNpc(10050,   0,       24000,   180,  385,  0x0, 0,   8,   0,   0,   0,   0,   17,  255,  0)
    DeclNpc(-22809,  1299,    -18829,  180,  389,  0x0, 0,   9,   0,   0,   2,   0,   18,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    236,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 45,  12.449999809265137,    27.34000015258789,     -1.0,                  625.0,                 [0.10000000149011612,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -1.2450000047683716,   -5.4679999351501465,   0.20000000298023224,   1.0])

    DeclActor(0,       0,       -1600,   1000,    0,       2500,    0,       0x007C, 0,  46, 0x0000)

    PlaceName(-5.449999809265137, 0.0, -2.7200000286102295, 0x0000, 0x0000, "中央广场")
    PlaceName(-70.54000091552734, 0.0, 1.7300000190734863, 0x0000, 0x0000, "西街")
    PlaceName(21.290000915527344, 0.0, 85.38999938964844, 0x0000, 0x0000, "行政区")
    PlaceName(-130.92999267578125, 0.0, 75.48999786376953, 0x0000, 0x0000, "住宅街")
    PlaceName(-58.65999984741211, 0.0, 67.56999969482422, 0x0000, 0x0000, "欢乐街")
    PlaceName(74.98999786376953, 0.0, -25.489999771118164, 0x0000, 0x0000, "东街")
    PlaceName(110.13999938964844, 0.0, -79.94000244140625, 0x0000, 0x0000, "旧城区")
    PlaceName(102.70999908447266, 0.0, 39.849998474121094, 0x0000, 0x0000, "港湾区")
    PlaceName(76.97000122070312, 0.0, 132.91000366210938, 0x0000, 0x0000, "ＩＢＣ")
    PlaceName(5.690000057220459, 0.0, -71.02999877929688, 0x0000, 0x0000, "站前街道")
    PlaceName(-40.84000015258789, 0.0, 31.93000030517578, 0x0000, 0x0000, "后巷")
    PlaceName(2.7200000286102295, 0.0, -101.72000122070312, 0x0000, 0x0000, "乌尔斯拉间道")
    PlaceName(128.4499969482422, 0.0, -11.630000114440918, 0x0000, 0x0000, "东克洛斯贝尔街道")
    PlaceName(-121.02999877929688, 0.0, 0.25, 0x0000, 0x0000, "西克洛斯贝尔街道")
    PlaceName(-115.08999633789062, 0.0, 99.25, 0x0000, 0x0000, "玛因兹山道")
    PlaceName(15.0, 0.0, 216.75, 0x0000, 0x0000, "兰花塔")
    PlaceName(-27.229999542236328, 0.0, -16.579999923706055, 0x0000, 0x0051, "")
    PlaceName(25.989999771118164, 0.0, 9.15999984741211, 0x0000, 0x0054, "")
    PlaceName(-2.9700000286102295, 0.0, -24.5, 0x0000, 0x0057, "")
    PlaceName(-27.969999313354492, 0.0, 12.130000114440918, 0x0000, 0x0053, "")
    PlaceName(-7.670000076293945, 0.0, 35.88999938964844, 0x0000, 0x0053, "")
    PlaceName(-57.91999816894531, 0.0, 7.179999828338623, 0x0000, 0x0053, "")
    PlaceName(-67.56999969482422, 0.0, 27.969999313354492, 0x0000, 0x0053, "")
    PlaceName(-43.810001373291016, 0.0, 59.650001525878906, 0x0000, 0x0052, "")
    PlaceName(-39.11000061035156, 0.0, 46.779998779296875, 0x0000, 0x0053, "")
    PlaceName(-30.440000534057617, 0.0, 38.36000061035156, 0x0000, 0x0053, "")
    PlaceName(-2.2300000190734863, 0.0, 108.6500015258789, 0x0000, 0x0051, "")
    PlaceName(108.6500015258789, 0.0, -25.489999771118164, 0x0000, 0x0052, "")
    PlaceName(91.81999969482422, 0.0, -115.08999633789062, 0x0000, 0x0053, "")
    PlaceName(78.94999694824219, 0.0, -96.7699966430664, 0x0000, 0x0053, "")

    ChipFrameInfo(1712, 0)                                       # 0

    ScpFunction((
        "Function_0_6B0",          # 00, 0
        "Function_1_760",          # 01, 1
        "Function_2_7AD",          # 02, 2
        "Function_3_7D8",          # 03, 3
        "Function_4_802",          # 04, 4
        "Function_5_8E5",          # 05, 5
        "Function_6_96D",          # 06, 6
        "Function_7_9AB",          # 07, 7
        "Function_8_A7D",          # 08, 8
        "Function_9_AC1",          # 09, 9
        "Function_10_AF9",         # 0A, 10
        "Function_11_B4B",         # 0B, 11
        "Function_12_BA9",         # 0C, 12
        "Function_13_C93",         # 0D, 13
        "Function_14_D08",         # 0E, 14
        "Function_15_D6A",         # 0F, 15
        "Function_16_DE8",         # 10, 16
        "Function_17_EC3",         # 11, 17
        "Function_18_F40",         # 12, 18
        "Function_19_1015",        # 13, 19
        "Function_20_21DF",        # 14, 20
        "Function_21_2215",        # 15, 21
        "Function_22_2259",        # 16, 22
        "Function_23_229D",        # 17, 23
        "Function_24_22E1",        # 18, 24
        "Function_25_231E",        # 19, 25
        "Function_26_2362",        # 1A, 26
        "Function_27_23A6",        # 1B, 27
        "Function_28_23EA",        # 1C, 28
        "Function_29_242E",        # 1D, 29
        "Function_30_247F",        # 1E, 30
        "Function_31_24E1",        # 1F, 31
        "Function_32_255A",        # 20, 32
        "Function_33_25DD",        # 21, 33
        "Function_34_2660",        # 22, 34
        "Function_35_2BAF",        # 23, 35
        "Function_36_2DC0",        # 24, 36
        "Function_37_2E99",        # 25, 37
        "Function_38_2EED",        # 26, 38
        "Function_39_30D5",        # 27, 39
        "Function_40_329B",        # 28, 40
        "Function_41_3332",        # 29, 41
        "Function_42_333C",        # 2A, 42
        "Function_43_3C56",        # 2B, 43
        "Function_44_3E26",        # 2C, 44
        "Function_45_3E4B",        # 2D, 45
        "Function_46_3F03",        # 2E, 46
        "Function_47_403D",        # 2F, 47
        "Function_48_4067",        # 30, 48
        "Function_49_4091",        # 31, 49
        "Function_50_40BB",        # 32, 50
    ))


    def Function_0_6B0(): pass

    label("Function_0_6B0")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_6E8"),
        (1, "loc_6F4"),
        (2, "loc_700"),
        (3, "loc_70C"),
        (4, "loc_718"),
        (5, "loc_724"),
        (6, "loc_730"),
        (SWITCH_DEFAULT, "loc_73C"),
    )


    label("loc_6E8")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_748")

    label("loc_6F4")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_748")

    label("loc_700")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_748")

    label("loc_70C")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_748")

    label("loc_718")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_748")

    label("loc_724")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_748")

    label("loc_730")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_748")

    label("loc_73C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_748")

    label("loc_748")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_75F")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_748")

    label("loc_75F")

    Return()

    # Function_0_6B0 end

    def Function_1_760(): pass

    label("Function_1_760")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7AC")
    OP_95(0xFE, 11850, 0, -1800, 2000, 0x0)
    OP_95(0xFE, 11850, 0, 39440, 2000, 0x0)
    Sleep(2000)
    SetChrPos(0xFE, 30000, 0, -3010, 270)
    Jump("Function_1_760")

    label("loc_7AC")

    Return()

    # Function_1_760 end

    def Function_2_7AD(): pass

    label("Function_2_7AD")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7D7")
    OP_94(0xFE, 0xFFFFA484, 0xFFFFB348, 0xFFFFA722, 0xFFFFB9BA, 0x3E8)
    Sleep(300)
    Jump("Function_2_7AD")

    label("loc_7D7")

    Return()

    # Function_2_7AD end

    def Function_3_7D8(): pass

    label("Function_3_7D8")

    SetMapObjFlags(0x17, 0x2000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 2)), scpexpr(EXPR_END)), "loc_7F2")
    ClearMapObjFlags(0x17, 0x2000000)
    Jump("loc_801")

    label("loc_7F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 3)), scpexpr(EXPR_END)), "loc_801")
    ClearMapObjFlags(0x17, 0x2000000)

    label("loc_801")

    Return()

    # Function_3_7D8 end

    def Function_4_802(): pass

    label("Function_4_802")

    SetChrChipByIndex(0x9, 0x1)
    SetChrSubChip(0x9, 0x0)
    EndChrThread(0x9, 0x0)
    SetChrBattleFlags(0x9, 0x4)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xF, -4240, 0, -7750, 225)
    SetChrPos(0xB, -4450, 0, -9880, 315)
    SetChrFlags(0xF, 0x10)
    SetChrFlags(0xB, 0x10)
    SetChrFlags(0xA, 0x10)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_871")
    ClearScenarioFlags(0x22, 0)
    Event(0, 19)
    Jump("loc_8E4")

    label("loc_871")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_885")
    ClearScenarioFlags(0x22, 1)
    Event(0, 34)
    Jump("loc_8E4")

    label("loc_885")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 2)), scpexpr(EXPR_END)), "loc_899")
    ClearScenarioFlags(0x22, 2)
    Event(0, 35)
    Jump("loc_8E4")

    label("loc_899")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 3)), scpexpr(EXPR_END)), "loc_8AD")
    ClearScenarioFlags(0x22, 3)
    Event(0, 38)
    Jump("loc_8E4")

    label("loc_8AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 4)), scpexpr(EXPR_END)), "loc_8C1")
    ClearScenarioFlags(0x22, 4)
    Event(0, 39)
    Jump("loc_8E4")

    label("loc_8C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 5)), scpexpr(EXPR_END)), "loc_8D5")
    ClearScenarioFlags(0x22, 5)
    Event(0, 42)
    Jump("loc_8E4")

    label("loc_8D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 6)), scpexpr(EXPR_END)), "loc_8E4")
    ClearScenarioFlags(0x22, 6)
    Event(0, 43)

    label("loc_8E4")

    Return()

    # Function_4_802 end

    def Function_5_8E5(): pass

    label("Function_5_8E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_8FA")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 4)

    label("loc_8FA")

    SetMapObjFlags(0xF, 0x4)
    SetMapObjFlags(0x10, 0x4)
    SetMapObjFlags(0x11, 0x4)
    SetMapObjFlags(0x12, 0x4)
    SetMapObjFlags(0x13, 0x4)
    SetMapObjFlags(0x14, 0x4)
    SetMapObjFlags(0x15, 0x4)
    SetMapObjFrame(0xFF, "black", 0x0, 0x1)
    SetMapObjFrame(0xFF, "nwindow", 0x0, 0x1)
    OP_1B(0x0, 0xFF, 0xFFFF)
    OP_1B(0x1, 0xFF, 0xFFFF)
    OP_1B(0x3, 0xFF, 0xFFFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_96C")
    OP_1B(0x0, 0x0, 0x2F)
    OP_1B(0x1, 0x0, 0x30)
    OP_1B(0x3, 0x0, 0x31)

    label("loc_96C")

    Return()

    # Function_5_8E5 end

    def Function_6_96D(): pass

    label("Function_6_96D")

    TalkBegin(0xFE)

    #C0001
    ChrTalk(
        0xFE,
        "啊，已经这么晚了啊。\x02",
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0xFE,
        (
            "得快点回家\x01",
            "帮妈妈做事。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_6_96D end

    def Function_7_9AB(): pass

    label("Function_7_9AB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A32")

    #C0003
    ChrTalk(
        0xFE,
        (
            "哎呀，不知不觉，\x01",
            "天都这么黑了。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0xFE,
        (
            "呵呵，我也被通商会议的\x01",
            "气氛感染了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0xFE,
        "得早点回家，免得老婆子担心。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_A79")

    label("loc_A32")


    #C0006
    ChrTalk(
        0xFE,
        (
            "哎呀，不知不觉，\x01",
            "天都这么黑了。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0xFE,
        "得早点回家，免得老婆子担心。\x02",
    )

    CloseMessageWindow()

    label("loc_A79")

    TalkEnd(0xFE)
    Return()

    # Function_7_9AB end

    def Function_8_A7D(): pass

    label("Function_8_A7D")

    TalkBegin(0xFE)

    #C0008
    ChrTalk(
        0xFE,
        (
            "哎呀，让你们久等了，\x01",
            "真抱歉。\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0xFE,
        "那我们就赶快出发吧。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_8_A7D end

    def Function_9_AC1(): pass

    label("Function_9_AC1")

    TalkBegin(0xFE)

    #C0010
    ChrTalk(
        0xFE,
        (
            "嗯，快走吧，\x01",
            "我和米米的肚子都饿得咕咕叫了。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_9_AC1 end

    def Function_10_AF9(): pass

    label("Function_10_AF9")

    TalkBegin(0xFE)

    #C0011
    ChrTalk(
        0xFE,
        "出发出发，今天要在外面吃饭¤\x02",
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0xFE,
        (
            "米米想吃东街那家店的\x01",
            "『东方料理』。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_10_AF9 end

    def Function_11_B4B(): pass

    label("Function_11_B4B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B60")
    Call(0, 12)
    Jump("loc_BA5")

    label("loc_B60")


    #C0013
    ChrTalk(
        0xFE,
        "嗯～这样啊。\x02",
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0xFE,
        (
            "（……看她这样子，\x01",
            "  根本就已经不再跑了吧。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BA5")

    TalkEnd(0xFE)
    Return()

    # Function_11_B4B end

    def Function_12_BA9(): pass

    label("Function_12_BA9")

    OP_4B(0xC, 0xFF)
    OP_4B(0xD, 0xFF)

    #C0015
    ChrTalk(
        0xC,
        (
            "对了，利娜莉，\x01",
            "你还在坚持慢跑吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0xD,
        (
            "哎？啊……嗯……\x01",
            "差不多吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0xD,
        (
            "但我觉得勉强自己减肥\x01",
            "也不太好，\x01",
            "所以最近只在想跑的时候才去跑……\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0xC,
        "……这样啊。\x02",
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0xC,
        (
            "（……看她这样子，\x01",
            "  根本就已经不再跑了吧。）\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xC, 0xFF)
    OP_4C(0xD, 0xFF)
    SetScenarioFlags(0x0, 1)
    SetScenarioFlags(0x0, 2)
    Return()

    # Function_12_BA9 end

    def Function_13_C93(): pass

    label("Function_13_C93")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CA8")
    Call(0, 12)
    Jump("loc_D04")

    label("loc_CA8")


    #C0020
    ChrTalk(
        0xFE,
        (
            "虽、虽说是只在想跑时才跑，\x01",
            "但我还是一直在坚持的哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0xFE,
        (
            "唔……干脆今天\x01",
            "就跑步回去吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D04")

    TalkEnd(0xFE)
    Return()

    # Function_13_C93 end

    def Function_14_D08(): pass

    label("Function_14_D08")

    TalkBegin(0xFE)

    #C0022
    ChrTalk(
        0xFE,
        "好了，差不多也该收摊了。\x02",
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0xFE,
        (
            "多亏通商会议的影响，今天的行人很多，\x01",
            "我发出去很多气球。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_14_D08 end

    def Function_15_D6A(): pass

    label("Function_15_D6A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x149, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D7F")
    Call(0, 16)
    Jump("loc_DE4")

    label("loc_D7F")


    #C0024
    ChrTalk(
        0xFE,
        (
            "在把首脑们送到\x01",
            "米修拉姆之前，\x01",
            "前方路段暂时禁止通行。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0xFE,
        (
            "希望支援科的各位多加理解，\x01",
            "配合我们。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DE4")

    TalkEnd(0xFE)
    Return()

    # Function_15_D6A end

    def Function_16_DE8(): pass

    label("Function_16_DE8")

    OP_4B(0x10, 0xFF)
    OP_4B(0x11, 0xFF)
    TurnDirection(0x10, 0x0, 0)

    #C0026
    ChrTalk(
        0x10,
        (
            "支援科的各位，\x01",
            "还有达德利搜查官……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x11, 0x0, 500)

    #C0027
    ChrTalk(
        0x11,
        (
            "你们要过去吗？\x01",
            "在首脑们观剧结束之前，\x01",
            "前方路段会暂时封锁。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x10A,
        (
            "#00600F不用了，\x01",
            "你们继续保持警戒吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x10,
        "明白！\x02",
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x11,
        "明白！\x02",
    )

    CloseMessageWindow()
    OP_93(0x10, 0xB4, 0x0)
    OP_93(0x11, 0xB4, 0x0)
    OP_4C(0x10, 0xFF)
    OP_4C(0x11, 0xFF)
    SetScenarioFlags(0x149, 1)
    Return()

    # Function_16_DE8 end

    def Function_17_EC3(): pass

    label("Function_17_EC3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x149, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_ED8")
    Call(0, 16)
    Jump("loc_F3C")

    label("loc_ED8")


    #C0031
    ChrTalk(
        0xFE,
        (
            "在首脑们观剧结束之前，\x01",
            "从欢乐街到港湾区的\x01",
            "路段将会暂时封锁。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0xFE,
        "连一只苍蝇都别想从这里飞过。\x02",
    )

    CloseMessageWindow()

    label("loc_F3C")

    TalkEnd(0xFE)
    Return()

    # Function_17_EC3 end

    def Function_18_F40(): pass

    label("Function_18_F40")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1003")

    #C0033
    ChrTalk(
        0x12,
        "喵。\x02",
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x10A,
        (
            "#00600F是支援科养的猫啊。\x02\x03",

            "#00603F（轻轻抚摸……）\x01",
            "……你竟然选了个\x01",
            "这么麻烦的地方安家。\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x12,
        "喵～～喵呜……⊥\x02",
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x101,
        (
            "#00002F（达德利警官\x01",
            "  竟然这么会哄猫……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_1011")

    label("loc_1003")


    #C0037
    ChrTalk(
        0x12,
        "喵呜……\x02",
    )

    CloseMessageWindow()

    label("loc_1011")

    TalkEnd(0xFE)
    Return()

    # Function_18_F40 end

    def Function_19_1015(): pass

    label("Function_19_1015")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch02710.itc", 0x1E)
    LoadChrToIndex("chr/ch08200.itc", 0x1F)
    LoadChrToIndex("chr/ch02750.itc", 0x20)
    LoadChrToIndex("apl/ch51200.itc", 0x21)
    OP_68(9400, 1400, -5200, 0)
    MoveCamera(55, 17, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(18500, 0)
    SetChrPos(0x101, 15800, 0, -4900, 270)
    SetChrPos(0x102, 16000, 0, -6500, 270)
    SetChrPos(0x104, 16700, 0, -3400, 270)
    SetChrPos(0x109, 18000, 0, -3800, 270)
    SetChrPos(0x105, 18800, 0, -4400, 270)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrChipByIndex(0x14, 0x1E)
    SetChrSubChip(0x14, 0x0)
    ClearChrFlags(0x14, 0x80)
    SetChrFlags(0x14, 0x8000)
    ClearChrFlags(0x14, 0x4)
    SetChrPos(0x14, 17500, 0, -7000, 270)
    OP_52(0x14, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x13, 0x1F)
    SetChrSubChip(0x13, 0x0)
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x13, 0x8000)
    ClearChrFlags(0x13, 0x4)
    SetChrPos(0x13, 17000, 0, -5200, 270)
    ClearChrFlags(0x18, 0x4)
    ClearChrFlags(0x18, 0x80)
    OP_90(0x18, -12500, -4200, -16400, 225)
    SetChrFlags(0x8, 0x80)

    def lambda_1151():
        OP_97(0x101, 0xFFFFE4A8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1151)
    Sleep(50)

    def lambda_116E():
        OP_97(0x102, 0xFFFFE4A8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_116E)
    Sleep(50)

    def lambda_118B():
        OP_97(0x104, 0xFFFFE4A8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_118B)
    Sleep(50)

    def lambda_11A8():
        OP_97(0x14, 0xFFFFE4A8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_11A8)
    Sleep(50)

    def lambda_11C5():
        OP_97(0x13, 0xFFFFE4A8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_11C5)
    Sleep(50)

    def lambda_11E2():
        OP_97(0x109, 0xFFFFE4A8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_11E2)
    Sleep(50)

    def lambda_11FF():
        OP_97(0x105, 0xFFFFE4A8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_11FF)
    SetCameraDistance(14700, 3500)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x101, 0)
    OP_6F(0x79)
    TurnDirection(0x101, 0x13, 500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x148, 2)), scpexpr(EXPR_END)), "loc_127B")

    #C0038
    ChrTalk(
        0x101,
        (
            "#6P#00000F对了，你明天要和小滴一起\x01",
            "去百货店楼顶吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12B6")

    label("loc_127B")


    #C0039
    ChrTalk(
        0x101,
        (
            "#6P#00000F这样啊，你明天要和小滴一起\x01",
            "去百货店楼顶啊？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12B6")


    def lambda_12BB():
        TurnDirection(0x102, 0x13, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_12BB)
    Sleep(50)

    def lambda_12CB():
        TurnDirection(0x104, 0x13, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_12CB)
    Sleep(50)

    def lambda_12DB():
        TurnDirection(0x109, 0x13, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_12DB)
    Sleep(50)

    def lambda_12EB():
        TurnDirection(0x105, 0x13, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_12EB)
    Sleep(50)

    def lambda_12FB():
        TurnDirection(0x14, 0x13, 500)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_12FB)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x14, 0)
    WaitChrThread(0x14, 0)
    SetChrSubChip(0x14, 0x5)

    #C0040
    ChrTalk(
        0x13,
        (
            "#11P#01109F嗯！\x01",
            "是叫揭幕式吧？\x02\x03",

            "#01110F我们约好\x01",
            "要一起去看～\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x102,
        (
            "#12P#00109F呵呵，这样啊。\x02\x03",

            "#00105F啊，但小滴看不到\x01",
            "揭幕式呢……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x13, 0x102, 500)

    #C0042
    ChrTalk(
        0x13,
        (
            "#5P#01100F嗯，但她想去\x01",
            "感受一下气氛～\x02\x03",

            "至于揭幕式的样子，\x01",
            "我会说给她听的～\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x101,
        "#6P#00002F这样啊……\x02",
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x104,
        "#5P#00300F#30W……那孩子真是坚强啊。\x02",
    )

    CloseMessageWindow()
    OP_63(0x13, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x13, 0x104, 500)

    #C0045
    ChrTalk(
        0x13,
        (
            "#12P#01105F兰迪～\x02\x03",

            "#01112F你一直没什么精神呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_68(9400, 1400, -4700, 1000)
    Sleep(300)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(700)

    def lambda_14C2():
        TurnDirection(0x101, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_14C2)
    Sleep(50)

    def lambda_14D2():
        TurnDirection(0x102, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_14D2)
    Sleep(50)

    def lambda_14E2():
        TurnDirection(0x104, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_14E2)
    Sleep(50)

    def lambda_14F2():
        TurnDirection(0x109, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_14F2)
    Sleep(50)

    def lambda_1502():
        TurnDirection(0x105, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_1502)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    Sleep(100)
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x104, 0x1)
    SetChrFlags(0x104, 0x10)
    SetChrFlags(0x104, 0x2)
    SetChrFlags(0x104, 0x20)
    BeginChrThread(0x104, 3, 0, 20)
    Sleep(300)

    #C0046
    ChrTalk(
        0x104,
        "#5P#00309F哈哈，哪有的事。\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x104, 3)
    SetChrSubChip(0x104, 0x5)
    Sleep(110)
    SetChrSubChip(0x104, 0x6)
    Sleep(110)
    SetChrSubChip(0x104, 0x7)
    Sound(822, 0, 100, 0)
    OP_63(0x104, 0x12C, 1300, 0x36, 0x39, 0xFA, 0x0)
    Sleep(1300)
    SetChrSubChip(0x104, 0x8)
    Sleep(110)
    SetChrSubChip(0x104, 0x9)
    Sleep(110)
    SetChrSubChip(0x104, 0xA)
    OP_82(0x32, 0x0, 0x7D0, 0xC8)

    #C0047
    ChrTalk(
        0x104,
        (
            "#5P#00303F看！\x02\x03",

            "#00302F我还是像平常一样有精神，\x01",
            "是不是帅呆了？\x02",
        )
    )

    CloseMessageWindow()
    OP_64(0x104)

    #C0048
    ChrTalk(
        0x13,
        "#12P#01111F帅呆了～？\x02",
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x109,
        (
            "#11P#10112F前辈……帅呆了这种说法\x01",
            "未免也太老土了……\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x105,
        (
            "#10302F#11P呵呵，装模作样\x01",
            "也算有精神吗？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x104, 0xB)
    Sleep(90)
    ClearChrFlags(0x104, 0x10)
    ClearChrFlags(0x104, 0x2)
    ClearChrFlags(0x104, 0x20)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    Sleep(150)
    TurnDirection(0x104, 0x109, 500)
    OP_82(0x32, 0x0, 0x7D0, 0xC8)

    #C0051
    ChrTalk(
        0x104,
        (
            "#5P#00301F可恶！\x01",
            "你们这些后辈不许插嘴！\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x101,
        (
            "#12P#00012F哈哈……\x02\x03",

            "#00000F兰迪，你不要一个人\x01",
            "钻牛角尖哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x102,
        (
            "#12P#00106F是啊，在这种时候，\x01",
            "就应该适当依靠一下我们……\x02\x03",

            "#00101F一定不要把所有事情\x01",
            "都扛在自己肩上哦。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x13, 500)

    #C0054
    ChrTalk(
        0x104,
        (
            "#5P#00304F哈哈，我知道啦。\x02\x03",

            "#00308F说到底，他们毕竟\x01",
            "是我的亲人。\x02\x03",

            "#00300F我很想和他们推心置腹地\x01",
            "好好谈一次。\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x102,
        "#12P#00105F这……\x02",
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x101,
        "#12P#00001F……未免太危险了吧？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14E, 3)), scpexpr(EXPR_END)), "loc_18EF")

    #C0057
    ChrTalk(
        0x104,
        (
            "#5P#00304F没事，毕竟我很了解他们。\x02\x03",

            "#00301F话说回来，叔叔说\x01",
            "有事要对我说，\x01",
            "结果却完全没了音讯。\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x101,
        (
            "#12P#00001F是啊，白天去拜访时，\x01",
            "他也不在……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1994")

    label("loc_18EF")


    #C0059
    ChrTalk(
        0x104,
        (
            "#5P#00304F没事，毕竟我很了解他们。\x02\x03",

            "#00301F话说回来，叔叔说\x01",
            "有事要对我说，\x01",
            "结果却完全没了音讯。\x02\x03",

            "我去鲁巴彻的旧址找他，\x01",
            "他也假装不在。\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x101,
        "#12P#00001F是吗……\x02",
    )

    CloseMessageWindow()

    label("loc_1994")


    def lambda_1999():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_1999)

    def lambda_19A6():
        OP_93(0x101, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_19A6)
    Sleep(50)

    def lambda_19B6():
        OP_93(0x102, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_19B6)
    Sleep(50)

    def lambda_19C6():
        OP_93(0x14, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_19C6)
    Sleep(50)

    def lambda_19D6():
        OP_93(0x13, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_19D6)
    Sleep(50)

    def lambda_19E6():
        OP_93(0x109, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_19E6)
    Sleep(50)

    def lambda_19F6():
        OP_93(0x105, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_19F6)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x14, 0)
    WaitChrThread(0x13, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    SetCameraDistance(17500, 3000)

    def lambda_1A24():
        OP_97(0x101, 0xFFFFD508, 0x0, 0xFFFFEC78, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1A24)
    Sleep(50)

    def lambda_1A41():
        OP_97(0x102, 0xFFFFD508, 0x0, 0xFFFFEC78, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1A41)
    Sleep(50)

    def lambda_1A5E():
        OP_97(0x104, 0xFFFFD508, 0x0, 0xFFFFEC78, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_1A5E)
    Sleep(50)

    def lambda_1A7B():
        OP_97(0x14, 0xFFFFD508, 0x0, 0xFFFFEC78, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_1A7B)
    Sleep(50)

    def lambda_1A98():
        OP_97(0x13, 0xFFFFD508, 0x0, 0xFFFFEC78, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_1A98)
    Sleep(50)

    def lambda_1AB5():
        OP_97(0x109, 0xFFFFD508, 0x0, 0xFFFFEC78, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1AB5)
    Sleep(50)

    def lambda_1AD2():
        OP_97(0x105, 0xFFFFD508, 0x0, 0xFFFFEC78, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_1AD2)
    Sleep(2000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_69(0x2, 0x0)
    OP_6B(0x18)
    OP_68(-12500, -3000, -16400, 0)
    MoveCamera(33, 19, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(20000, 0)
    EndChrThread(0x101, 0xFF)
    EndChrThread(0x102, 0xFF)
    EndChrThread(0x13, 0xFF)
    EndChrThread(0x14, 0xFF)
    EndChrThread(0x104, 0xFF)
    EndChrThread(0x109, 0xFF)
    EndChrThread(0x105, 0xFF)
    SetChrPos(0x101, -13100, -4200, -17800, 225)
    SetChrPos(0x104, -13900, -4200, -17000, 225)
    SetChrPos(0x13, -12100, -4200, -16800, 225)
    SetChrPos(0x109, -12900, -4200, -16000, 225)
    SetChrPos(0x102, -11100, -4200, -15800, 225)
    SetChrPos(0x105, -11900, -4200, -15000, 225)
    SetChrPos(0x14, -13900, -4200, -18700, 225)
    BeginChrThread(0x14, 3, 0, 28)
    BeginChrThread(0x18, 3, 0, 24)
    Sleep(50)
    BeginChrThread(0x101, 3, 0, 21)
    Sleep(50)
    BeginChrThread(0x104, 3, 0, 22)
    Sleep(50)
    BeginChrThread(0x13, 3, 0, 23)
    Sleep(50)
    BeginChrThread(0x109, 3, 0, 25)
    Sleep(50)
    BeginChrThread(0x102, 3, 0, 26)
    Sleep(50)
    BeginChrThread(0x105, 3, 0, 27)
    MoveCamera(40, 23, 0, 10000)
    SetCameraDistance(16000, 10000)
    FadeToBright(1000, 0)
    OP_0D()

    #C0061
    ChrTalk(
        0x104,
        (
            "#00306F#5P呼，肚子饿了。\x02\x03",

            "#00305F对了，科长今天\x01",
            "要很晚才能回来吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x101,
        (
            "#00000F#11P是啊，他们要安排明天的揭幕式，\x01",
            "恐怕会拖到很晚。\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x102,
        (
            "#00102F#11P呵呵，既然如此，\x01",
            "那我们今天就去\x01",
            "外面吃饭好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x109,
        "#10109F#5P嗯，偶尔出去吃也不错。\x02",
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x105,
        (
            "#10302F#11P那就去旁边的餐厅\x01",
            "或龙老饭店吧？\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x101, 3)

    #C0066
    ChrTalk(
        0x101,
        (
            "#6P#00002F好，放下手上的东西，\x01",
            "大家一起出门吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    WaitChrThread(0x105, 3)
    OP_6B(0xFF)
    OP_6F(0x79)
    SetChrChipByIndex(0x14, 0x20)
    SetChrSubChip(0x14, 0x0)
    OP_52(0x14, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    #Sound(2937, 255, 100, 0)    #voice#Zeit

    #C0067
    ChrTalk(
        0x14,
        "#01201F#40W#11P咕噜噜噜噜……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x13, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_68(-26700, -7000, -24400, 2000)
    SetCameraDistance(17000, 2000)

    def lambda_1E5A():
        OP_93(0x101, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1E5A)
    Sleep(50)

    def lambda_1E6A():
        OP_93(0x104, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_1E6A)
    Sleep(50)

    def lambda_1E7A():
        OP_93(0x13, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_1E7A)
    Sleep(50)

    def lambda_1E8A():
        OP_93(0x109, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1E8A)
    Sleep(50)

    def lambda_1E9A():
        OP_93(0x102, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1E9A)
    Sleep(50)

    def lambda_1EAA():
        OP_93(0x105, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_1EAA)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x13, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x105, 0)

    def lambda_1ECF():
        OP_A6(0xFE, 0x0, 0x1E, 0x190, 0x7D0)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_1ECF)
    OP_6F(0x79)

    def lambda_1EEA():
        OP_97(0x101, 0xFFFFF63C, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1EEA)
    Sleep(100)

    def lambda_1F07():
        OP_97(0x104, 0xFFFFF63C, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_1F07)
    Sleep(100)

    def lambda_1F24():
        OP_97(0x13, 0xFFFFF63C, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_1F24)
    Sleep(100)

    def lambda_1F41():
        OP_97(0x109, 0xFFFFF63C, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1F41)
    Sleep(100)

    def lambda_1F5E():
        OP_97(0x102, 0xFFFFF63C, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1F5E)
    Sleep(100)

    def lambda_1F7B():
        OP_97(0x105, 0xFFFFF63C, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_1F7B)
    WaitChrThread(0x104, 0)

    def lambda_1F99():
        TurnDirection(0xFE, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_1F99)
    WaitChrThread(0x109, 0)

    def lambda_1FAA():
        TurnDirection(0xFE, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_1FAA)

    #C0068
    ChrTalk(
        0x101,
        "#11P#00001F蔡特？\x02",
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x102,
        "#00105F#11P怎么了？\x02",
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x13,
        (
            "#12P#01105F嗯……它在说，\x01",
            "有客人来了哦～\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x101,
        "#11P#00005F客人？\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    OP_93(0x104, 0x13B, 0x1F4)
    Sleep(300)

    #C0072
    ChrTalk(
        0x104,
        "#11P#00311F#40W………………………………\x02",
    )

    CloseMessageWindow()
    Sleep(150)

    def lambda_2069():
        OP_95(0xFE, -28500, -8200, -22800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2069)
    Sleep(500)

    def lambda_2086():

        label("loc_2086")

        TurnDirection(0xFE, 0x104, 500)
        Yield()
        Jump("loc_2086")

    QueueWorkItem2(0x101, 2, lambda_2086)
    Sleep(100)

    def lambda_209B():

        label("loc_209B")

        TurnDirection(0xFE, 0x104, 500)
        Yield()
        Jump("loc_209B")

    QueueWorkItem2(0x109, 2, lambda_209B)

    def lambda_20AD():

        label("loc_20AD")

        TurnDirection(0xFE, 0x104, 500)
        Yield()
        Jump("loc_20AD")

    QueueWorkItem2(0x13, 2, lambda_20AD)
    Sleep(50)

    def lambda_20C2():

        label("loc_20C2")

        TurnDirection(0xFE, 0x104, 500)
        Yield()
        Jump("loc_20C2")

    QueueWorkItem2(0x102, 2, lambda_20C2)

    def lambda_20D4():

        label("loc_20D4")

        TurnDirection(0xFE, 0x104, 500)
        Yield()
        Jump("loc_20D4")

    QueueWorkItem2(0x105, 2, lambda_20D4)
    WaitChrThread(0x104, 1)

    def lambda_20EA():
        OP_95(0xFE, -28500, -8200, -19800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_20EA)
    Sleep(100)
    Sound(103, 0, 100, 0)
    ClearMapObjFlags(0x0, 0x10)
    OP_71(0x0, 0x0, 0xA, 0x0, 0x0)
    OP_79(0x0)
    Sleep(400)

    #C0073
    ChrTalk(
        0x101,
        "#11P#00011F兰迪？\x02",
    )


    def lambda_213B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_213B)
    WaitChrThread(0x104, 1)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x13, 0x2)
    EndChrThread(0x109, 0x2)
    EndChrThread(0x105, 0x2)
    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x105,
        "#10301F#11P……总之，先进去吧。\x02",
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    BeginChrThread(0x101, 3, 0, 29)
    Sleep(400)
    BeginChrThread(0x109, 3, 0, 29)
    Sleep(400)
    BeginChrThread(0x13, 3, 0, 29)
    Sleep(400)
    BeginChrThread(0x105, 3, 0, 29)
    Sleep(400)
    BeginChrThread(0x102, 3, 0, 29)
    OP_0D()
    EndChrThread(0x101, 0xFF)
    EndChrThread(0x102, 0xFF)
    EndChrThread(0x13, 0xFF)
    EndChrThread(0x104, 0xFF)
    EndChrThread(0x109, 0xFF)
    EndChrThread(0x105, 0xFF)
    SetScenarioFlags(0x22, 1)
    NewScene("c011B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_19_1015 end

    def Function_20_21DF(): pass

    label("Function_20_21DF")

    SetChrSubChip(0x104, 0x2)
    Sleep(100)
    SetChrSubChip(0x104, 0x3)
    Sleep(100)
    SetChrSubChip(0x104, 0x4)
    Sleep(100)
    SetChrSubChip(0x104, 0x5)
    Sleep(100)
    SetChrSubChip(0x104, 0x4)
    Sleep(100)
    SetChrSubChip(0x104, 0x3)
    Sleep(100)
    SetChrSubChip(0x104, 0x4)
    Sleep(100)
    SetChrSubChip(0x104, 0x5)
    Return()

    # Function_20_21DF end

    def Function_21_2215(): pass

    label("Function_21_2215")


    def lambda_221A():
        OP_95(0xFE, -20000, -8200, -25100, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_221A)
    WaitChrThread(0xFE, 1)

    def lambda_2238():
        OP_95(0xFE, -23800, -8200, -25100, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2238)
    WaitChrThread(0xFE, 1)
    TurnDirection(0xFE, 0x18, 500)
    Return()

    # Function_21_2215 end

    def Function_22_2259(): pass

    label("Function_22_2259")


    def lambda_225E():
        OP_95(0xFE, -20000, -8200, -23100, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_225E)
    WaitChrThread(0xFE, 1)

    def lambda_227C():
        OP_95(0xFE, -23800, -8200, -23700, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_227C)
    WaitChrThread(0xFE, 1)
    TurnDirection(0xFE, 0x18, 500)
    Return()

    # Function_22_2259 end

    def Function_23_229D(): pass

    label("Function_23_229D")


    def lambda_22A2():
        OP_95(0xFE, -20000, -8200, -25100, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_22A2)
    WaitChrThread(0xFE, 1)

    def lambda_22C0():
        OP_95(0xFE, -23000, -8200, -25700, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_22C0)
    WaitChrThread(0xFE, 1)
    TurnDirection(0xFE, 0x18, 500)
    Return()

    # Function_23_229D end

    def Function_24_22E1(): pass

    label("Function_24_22E1")


    def lambda_22E6():
        OP_95(0xFE, -20000, -8200, -24400, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_22E6)
    WaitChrThread(0xFE, 1)

    def lambda_2304():
        OP_95(0xFE, -22700, -8200, -24400, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2304)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_24_22E1 end

    def Function_25_231E(): pass

    label("Function_25_231E")


    def lambda_2323():
        OP_95(0xFE, -20000, -8200, -23100, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2323)
    WaitChrThread(0xFE, 1)

    def lambda_2341():
        OP_95(0xFE, -22400, -8200, -23100, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2341)
    WaitChrThread(0xFE, 1)
    TurnDirection(0xFE, 0x18, 500)
    Return()

    # Function_25_231E end

    def Function_26_2362(): pass

    label("Function_26_2362")


    def lambda_2367():
        OP_95(0xFE, -20000, -8200, -25100, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2367)
    WaitChrThread(0xFE, 1)

    def lambda_2385():
        OP_95(0xFE, -21600, -8200, -25100, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2385)
    WaitChrThread(0xFE, 1)
    TurnDirection(0xFE, 0x18, 500)
    Return()

    # Function_26_2362 end

    def Function_27_23A6(): pass

    label("Function_27_23A6")


    def lambda_23AB():
        OP_95(0xFE, -20000, -8200, -23100, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_23AB)
    WaitChrThread(0xFE, 1)

    def lambda_23C9():
        OP_95(0xFE, -21600, -8200, -23700, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_23C9)
    WaitChrThread(0xFE, 1)
    TurnDirection(0xFE, 0x18, 500)
    Return()

    # Function_27_23A6 end

    def Function_28_23EA(): pass

    label("Function_28_23EA")


    def lambda_23EF():
        OP_95(0xFE, -20000, -8200, -25100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_23EF)
    WaitChrThread(0xFE, 1)

    def lambda_240D():
        OP_95(0xFE, -28500, -8200, -26000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_240D)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_28_23EA end

    def Function_29_242E(): pass

    label("Function_29_242E")


    def lambda_2433():
        OP_95(0xFE, -28500, -8200, -22800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2433)
    WaitChrThread(0xFE, 1)

    def lambda_2451():
        OP_95(0xFE, -28500, -8200, -19800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2451)
    Sleep(500)

    def lambda_246E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_246E)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_29_242E end

    def Function_30_247F(): pass

    label("Function_30_247F")


    def lambda_2484():
        OP_95(0xFE, -12800, -4200, -16800, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2484)
    WaitChrThread(0xFE, 1)

    def lambda_24A2():
        OP_95(0xFE, -1000, 0, -16800, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_24A2)
    WaitChrThread(0xFE, 1)

    def lambda_24C0():
        OP_95(0xFE, 2500, 0, -14700, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_24C0)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xE1, 0x1F4)
    Return()

    # Function_30_247F end

    def Function_31_24E1(): pass

    label("Function_31_24E1")


    def lambda_24E6():
        OP_95(0xFE, -19800, -4200, -23800, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_24E6)
    WaitChrThread(0xFE, 1)

    def lambda_2504():
        OP_95(0xFE, -12800, -4200, -16800, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2504)
    WaitChrThread(0xFE, 1)

    def lambda_2522():
        OP_95(0xFE, -1000, 0, -16800, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2522)
    WaitChrThread(0xFE, 1)

    def lambda_2540():
        OP_95(0xFE, 1700, 0, -16800, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2540)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_31_24E1 end

    def Function_32_255A(): pass

    label("Function_32_255A")

    Sleep(500)

    def lambda_2562():
        OP_95(0xFE, -19800, -4200, -23800, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2562)
    WaitChrThread(0xFE, 1)

    def lambda_2580():
        OP_95(0xFE, -12800, -4200, -16800, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2580)
    WaitChrThread(0xFE, 1)

    def lambda_259E():
        OP_95(0xFE, -1000, 0, -16800, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_259E)
    WaitChrThread(0xFE, 1)

    def lambda_25BC():
        OP_95(0xFE, 900, 0, -16000, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_25BC)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_32_255A end

    def Function_33_25DD(): pass

    label("Function_33_25DD")

    Sleep(800)

    def lambda_25E5():
        OP_95(0xFE, -19800, -4200, -23800, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_25E5)
    WaitChrThread(0xFE, 1)

    def lambda_2603():
        OP_95(0xFE, -12800, -4200, -16800, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2603)
    WaitChrThread(0xFE, 1)

    def lambda_2621():
        OP_95(0xFE, -1000, 0, -16800, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2621)
    WaitChrThread(0xFE, 1)

    def lambda_263F():
        OP_95(0xFE, 600, 0, -17200, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_263F)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_33_25DD end

    def Function_34_2660(): pass

    label("Function_34_2660")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch03400.itc", 0x1E)
    LoadChrToIndex("chr/ch42900.itc", 0x1F)
    SetChrPos(0x101, -22100, -8200, -23800, 90)
    SetChrPos(0x104, -20600, -8200, -23800, 90)
    SetChrPos(0x105, -23600, -8200, -23800, 90)
    SetChrPos(0x102, -22000, -8200, -20000, 0)
    SetChrPos(0x109, -22000, -8200, -20000, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrChipByIndex(0x15, 0x1E)
    SetChrSubChip(0x15, 0x0)
    ClearChrFlags(0x15, 0x80)
    SetChrFlags(0x15, 0x8000)
    ClearChrFlags(0x15, 0x4)
    SetChrPos(0x15, -19800, -4200, -23800, 0)
    SetChrChipByIndex(0x16, 0x1F)
    SetChrSubChip(0x16, 0x0)
    SetChrFlags(0x16, 0x8000)
    SetChrPos(0x16, 4700, 500, -16800, 270)
    OP_A7(0x16, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_52(0x16, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x17, 0x80)
    OP_78(0x16, 0x17)
    OP_49()
    SetChrPos(0x17, 5800, 0, -16500, 0)
    OP_D5(0x17, 0x0, 0x0, 0x0, 0x0)
    ClearMapObjFlags(0x16, 0x4)
    SetMapObjFlags(0x16, 0x1000)
    OP_74(0x16, 0x1E)
    OP_70(0x16, 0x1)
    OP_68(-16500, -3900, -20500, 0)
    MoveCamera(5, 27, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(18000, 0)
    BeginChrThread(0x15, 3, 0, 30)
    BeginChrThread(0x104, 3, 0, 31)
    BeginChrThread(0x101, 3, 0, 32)
    BeginChrThread(0x105, 3, 0, 33)
    FadeToBright(1000, 0)
    OP_0D()
    OP_68(3700, 1300, -16800, 12500)
    MoveCamera(35, 27, 0, 12500)
    SetCameraDistance(15000, 12500)
    WaitChrThread(0x105, 3)
    OP_6F(0x79)

    #C0075
    ChrTalk(
        0x101,
        "#00011F这是……\x02",
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x105,
        (
            "#6P#10305F这是莱恩福尔特公司的\x01",
            "高级防弹轿车吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0x104,
        (
            "#6P#00303F哼，都已经购置\x01",
            "这种豪车了。\x02\x03",

            "#00302F看来生意不错啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0x15,
        (
            "#5P#04609F哈哈，托你的福，\x01",
            "我们捞了不少。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(462, 0, 100, 0)
    OP_71(0x16, 0xF1, 0x10E, 0x0, 0x0)
    OP_79(0x16)
    OP_68(3200, 1200, -16800, 1000)
    ClearChrFlags(0x16, 0x80)

    def lambda_28F6():
        OP_96(0xFE, 0xE74, 0x0, 0xFFFFBE60, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_28F6)

    def lambda_2910():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x16, 2, lambda_2910)
    WaitChrThread(0x16, 1)
    TurnDirection(0x16, 0x15, 500)

    #C0079
    ChrTalk(
        0x16,
        "#11P谢莉大小姐，您辛苦了。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x16, 0x104, 500)
    Sleep(300)

    #C0080
    ChrTalk(
        0x16,
        (
            "#11P还有少爷，\x01",
            "好久不见了。\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0x104,
        (
            "#6P#00300F加雷斯……好久不见了。\x02\x03",

            "#00306F不过，你还是\x01",
            "别再叫我少爷了。\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x16,
        (
            "#11P……我想您已经听说\x01",
            "巴德尔大人的事情了。\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x16,
        (
            "#11P对于他的去世……\x01",
            "我真心感到万分遗憾。\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x104,
        "#6P#00308F……嗯。\x02",
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0x15,
        (
            "#5P#04604F别说这种阴郁的话题了！\x01",
            "今晚要大玩一场哦！\x02\x03",

            "#04602F来来，快上来！\x01",
            "两位小哥，你们也快点上来！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2AA6():
        OP_95(0xFE, 3200, 0, -18400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_2AA6)
    WaitChrThread(0x16, 1)
    TurnDirection(0x16, 0x104, 500)

    #C0086
    ChrTalk(
        0x101,
        (
            "#00001F嗯……\x01",
            "那我就不客气了。\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x105,
        "#6P#10304F呵呵，打扰了。\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(14500, 2000)
    FadeToDark(2000, 0, -1)

    def lambda_2B20():
        OP_95(0xFE, 3700, 0, -16800, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2B20)
    Sleep(500)

    def lambda_2B3D():
        OP_95(0xFE, 3700, 0, -16800, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2B3D)
    WaitChrThread(0x104, 1)

    def lambda_2B5B():
        OP_95(0xFE, 4700, 500, -16800, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2B5B)

    def lambda_2B75():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_2B75)

    def lambda_2B86():
        OP_95(0xFE, 3700, 0, -16800, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_2B86)
    OP_0D()
    OP_6F(0x79)
    EndChrThread(0x104, 0xFF)
    SetScenarioFlags(0x22, 0)
    NewScene("e0111", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_34_2660 end

    def Function_35_2BAF(): pass

    label("Function_35_2BAF")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch30600.itc", 0x1E)
    SoundLoad(835)
    SetChrChipByIndex(0x1A, 0x1E)
    SetChrChipByIndex(0x19, 0x8)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0xE, 0x8000)
    SetChrFlags(0x9, 0x8000)
    SetChrFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x8000)
    SetChrFlags(0xB, 0x8000)
    SetChrFlags(0xF, 0x8000)
    SetChrFlags(0x1A, 0x8000)
    SetChrFlags(0x19, 0x8000)
    ClearChrFlags(0x17, 0x80)
    OP_78(0x17, 0x17)
    OP_49()
    ClearMapObjFlags(0x17, 0x4)
    SetMapObjFlags(0x17, 0x1000)
    SetMapObjFrame(0x17, "chukin", 0x0, 0x1)
    OP_71(0x17, 0x79, 0xB4, 0x0, 0x20)
    SetChrFlags(0x0, 0x80)
    SetChrBattleFlags(0x0, 0x8000)
    SetChrFlags(0x1, 0x80)
    SetChrBattleFlags(0x1, 0x8000)
    SetChrFlags(0x2, 0x80)
    SetChrBattleFlags(0x2, 0x8000)
    SetChrFlags(0x3, 0x80)
    SetChrBattleFlags(0x3, 0x8000)
    SetChrPos(0xF, -6100, 0, -9410, 0)
    BeginChrThread(0xF, 0, 0, 0)
    SetChrPos(0xB, -5000, 0, -9410, 0)
    BeginChrThread(0xB, 0, 0, 0)
    SetChrPos(0x1A, -1200, 0, -2400, 180)
    BeginChrThread(0x1A, 0, 0, 0)
    SetChrPos(0x19, -18700, 0, 3950, 180)
    BeginChrThread(0x19, 0, 0, 36)
    SetChrPos(0x17, 4700, 0, -30500, 90)
    OP_D5(0x17, 0x0, 0x15F90, 0x0, 0x0)
    BeginChrThread(0x17, 0, 0, 37)
    OP_68(-1000, 3500, 11000, 0)
    MoveCamera(40, 6, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(30000, 0)
    OP_68(-1000, 1500, 11000, 10000)
    MoveCamera(23, 6, 0, 10000)
    SetCameraDistance(34500, 10000)
    Sound(835, 2, 100, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(2500)
    Sound(457, 0, 70, 0)
    OP_6F(0x79)
    Fade(500)
    OP_68(-25800, -7600, -16800, 0)
    MoveCamera(35, 12, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(23500, 0)
    SetCameraDistance(20500, 4000)
    Sleep(3000)
    StopSound(835, 1000, 100)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 4)
    NewScene("c011B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_35_2BAF end

    def Function_36_2DC0(): pass

    label("Function_36_2DC0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2E98")
    OP_95(0xFE, -15910, 0, 1150, 1000, 0x0)
    OP_95(0xFE, -290, 0, 16770, 1000, 0x0)
    OP_95(0xFE, -300, 800, 24250, 1000, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    Sleep(500)
    OP_93(0xFE, 0xD7, 0x1F4)
    Sleep(500)
    OP_93(0xFE, 0x87, 0x1F4)
    Sleep(500)
    OP_93(0xFE, 0xB4, 0x1F4)
    Sleep(1000)
    OP_95(0xFE, -290, 0, 16770, 1000, 0x0)
    OP_95(0xFE, -15910, 0, 1150, 1000, 0x0)
    OP_95(0xFE, -18720, 0, 3960, 1000, 0x0)
    OP_93(0xFE, 0x87, 0x1F4)
    Sleep(500)
    OP_93(0xFE, 0xB4, 0x1F4)
    Sleep(500)
    OP_93(0xFE, 0x5A, 0x1F4)
    Sleep(500)
    OP_93(0xFE, 0x87, 0x1F4)
    Sleep(1000)
    Jump("Function_36_2DC0")

    label("loc_2E98")

    Return()

    # Function_36_2DC0 end

    def Function_37_2E99(): pass

    label("Function_37_2E99")

    OP_9F(0x0, 0xFE)
    OP_9F(0x1, 4700, 0, -30500)
    OP_9F(0x1, 4700, 0, -12500)
    OP_9F(0x1, 8580, 0, 4180)
    OP_9F(0x1, 11000, 0, 30000)
    OP_9F(0x1, 11000, 0, 60000)
    OP_9F(0x2, 0xFE, 6000, 0x6)
    Return()

    # Function_37_2E99 end

    def Function_38_2EED(): pass

    label("Function_38_2EED")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch30600.itc", 0x1E)
    SoundLoad(835)
    SetChrChipByIndex(0x1A, 0x1E)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0xF, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0x1A, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0xE, 0x8000)
    SetChrFlags(0x9, 0x8000)
    SetChrFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x8000)
    SetChrFlags(0xB, 0x8000)
    SetChrFlags(0xA, 0x8000)
    SetChrFlags(0x1A, 0x8000)
    SetChrFlags(0x19, 0x8000)
    ClearChrFlags(0x17, 0x80)
    OP_78(0x17, 0x17)
    OP_49()
    ClearMapObjFlags(0x17, 0x4)
    SetMapObjFlags(0x17, 0x1000)
    SetMapObjFrame(0x17, "chukin", 0x0, 0x1)
    OP_71(0x17, 0x79, 0xB4, 0x0, 0x20)
    SetChrFlags(0x0, 0x80)
    SetChrBattleFlags(0x0, 0x8000)
    SetChrFlags(0x1, 0x80)
    SetChrBattleFlags(0x1, 0x8000)
    SetChrFlags(0x2, 0x80)
    SetChrBattleFlags(0x2, 0x8000)
    SetChrFlags(0x3, 0x80)
    SetChrBattleFlags(0x3, 0x8000)
    SetChrPos(0x1A, -1200, 0, -2400, 180)
    BeginChrThread(0x1A, 0, 0, 0)
    SetChrPos(0xA, -6100, 0, -9400, 90)
    SetChrPos(0xB, -5000, 0, -9400, 270)
    SetChrPos(0x17, 15000, 0, -5000, 270)
    OP_D5(0x17, 0x0, 0x41EB0, 0x0, 0x0)
    OP_68(-1000, 2500, 11000, 0)
    MoveCamera(25, 6, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(34500, 0)
    OP_68(-1000, 1500, 11000, 7000)
    MoveCamera(23, 5, 0, 7000)
    Sound(458, 0, 80, 0)

    def lambda_3056():
        OP_9B(0x1, 0xFE, 0x0, 0x9C40, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_3056)
    StopSound(835, 1000, 100)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    Fade(500)
    OP_68(-25800, -7600, -16800, 0)
    MoveCamera(35, 12, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(23500, 0)
    SetCameraDistance(20500, 4000)
    Sleep(3000)
    StopSound(835, 1000, 100)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 6)
    NewScene("c011B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_38_2EED end

    def Function_39_30D5(): pass

    label("Function_39_30D5")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch23400.itc", 0x1E)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrChipByIndex(0x1B, 0x1E)
    SetChrSubChip(0x1B, 0x0)
    ClearChrFlags(0x1B, 0x80)
    SetChrFlags(0x1B, 0x8000)
    SetMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x1, 0x4)
    SetMapObjFlags(0x2, 0x4)
    SetMapObjFlags(0x3, 0x4)
    SetMapObjFlags(0x4, 0x4)
    SetMapObjFlags(0x5, 0x4)
    SetMapObjFlags(0x6, 0x4)
    SetMapObjFlags(0x7, 0x4)
    SetMapObjFlags(0x8, 0x4)
    SetMapObjFlags(0x9, 0x4)
    SetMapObjFlags(0xA, 0x4)
    SetMapObjFlags(0xB, 0x4)
    SetMapObjFlags(0xC, 0x4)
    SetMapObjFlags(0xD, 0x4)
    SetMapObjFlags(0xE, 0x4)
    ClearMapObjFlags(0xF, 0x4)
    ClearMapObjFlags(0x10, 0x4)
    ClearMapObjFlags(0x11, 0x4)
    ClearMapObjFlags(0x12, 0x4)
    ClearMapObjFlags(0x13, 0x4)
    ClearMapObjFlags(0x14, 0x4)
    ClearMapObjFlags(0x15, 0x4)
    SetMapObjFrame(0xFF, "white", 0x0, 0x1)
    SetMapObjFrame(0xFF, "lwindow", 0x0, 0x1)
    SetMapObjFrame(0xFF, "black", 0x1, 0x1)
    SetMapObjFrame(0xFF, "nwindow", 0x1, 0x1)
    SetChrFlags(0x0, 0x80)
    SetChrBattleFlags(0x0, 0x8000)
    SetChrFlags(0x1, 0x80)
    SetChrBattleFlags(0x1, 0x8000)
    SetChrFlags(0x2, 0x80)
    SetChrBattleFlags(0x2, 0x8000)
    SetChrFlags(0x3, 0x80)
    SetChrBattleFlags(0x3, 0x8000)
    SetChrPos(0x1B, 1500, 0, -4700, 270)
    BeginChrThread(0x1B, 1, 0, 40)
    OP_68(-15350, 1800, 5500, 0)
    MoveCamera(10, 5, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(20000, 0)
    OP_68(3000, 1800, -6000, 12000)
    MoveCamera(45, 5, 0, 12000)
    FadeToBright(1000, 0)
    OP_0D()
    BeginChrThread(0x1C, 1, 0, 41)
    Sleep(10000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 7)
    NewScene("c012B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_39_30D5 end

    def Function_40_329B(): pass

    label("Function_40_329B")

    OP_63(0xFE, 0x0, 1850, 0x26, 0x27, 0xFA, 0x0)

    label("loc_32AD")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3331")
    OP_9B(0x1, 0xFE, 0x28, 0x3E8, 0x7D0, 0x0)

    def lambda_32CC():
        OP_A6(0xFE, 0x1E, 0x1E, 0x1F4, 0x7D0)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_32CC)
    OP_9B(0x1, 0xFE, 0x37, 0x1F4, 0x3E8, 0x0)
    Sleep(1500)
    OP_9B(0x1, 0xFE, 0xFFD3, 0x5DC, 0x7D0, 0x0)

    def lambda_3306():
        OP_A6(0xFE, 0x1E, 0x1E, 0x1F4, 0x7D0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3306)
    OP_9B(0x1, 0xFE, 0xFFD3, 0x1F4, 0x3E8, 0x0)
    Sleep(2000)
    Jump("loc_32AD")

    label("loc_3331")

    Return()

    # Function_40_329B end

    def Function_41_3332(): pass

    label("Function_41_3332")

    Sleep(3000)
    Sound(1012, 0, 80, 0)
    Return()

    # Function_41_3332 end

    def Function_42_333C(): pass

    label("Function_42_333C")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch51425.itc", 0x1E)
    LoadChrToIndex("apl/ch51443.itc", 0x1F)
    LoadChrToIndex("apl/ch51426.itc", 0x20)
    SoundLoad(2916)
    SoundLoad(2760)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis416.itp")
    OP_68(-28700, -7200, -22000, 0)
    MoveCamera(0, 13, 0, 0)
    OP_6E(660, 0)
    SetCameraDistance(13500, 0)
    SetChrPos(0x101, -22000, -8200, -20000, 0)
    SetChrPos(0x102, -22000, -8200, -20000, 0)
    SetChrPos(0x103, -22000, -8200, -20000, 0)
    SetChrPos(0x109, -22000, -8200, -20000, 0)
    SetChrChipByIndex(0x104, 0x1E)
    SetChrSubChip(0x104, 0x0)
    SetChrPos(0x104, -28700, -8200, -20000, 180)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x105, 0x20)
    SetChrSubChip(0x105, 0x0)
    SetChrFlags(0x105, 0x10)
    SetChrFlags(0x105, 0x2)
    SetChrFlags(0x105, 0x20)
    SetChrFlags(0x105, 0x40)
    SetChrPos(0x105, -21000, -8200, -22800, 180)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x1, 0x4)
    SetMapObjFlags(0x2, 0x4)
    SetMapObjFlags(0x3, 0x4)
    SetMapObjFlags(0x4, 0x4)
    SetMapObjFlags(0x5, 0x4)
    SetMapObjFlags(0x6, 0x4)
    SetMapObjFlags(0x7, 0x4)
    SetMapObjFlags(0x8, 0x4)
    SetMapObjFlags(0x9, 0x4)
    SetMapObjFlags(0xA, 0x4)
    SetMapObjFlags(0xB, 0x4)
    SetMapObjFlags(0xC, 0x4)
    SetMapObjFlags(0xD, 0x4)
    SetMapObjFlags(0xE, 0x4)
    ClearMapObjFlags(0xF, 0x4)
    ClearMapObjFlags(0x10, 0x4)
    ClearMapObjFlags(0x11, 0x4)
    ClearMapObjFlags(0x12, 0x4)
    ClearMapObjFlags(0x13, 0x4)
    ClearMapObjFlags(0x14, 0x4)
    ClearMapObjFlags(0x15, 0x4)
    SetMapObjFrame(0xFF, "white", 0x0, 0x1)
    SetMapObjFrame(0xFF, "lwindow", 0x0, 0x1)
    SetMapObjFrame(0xFF, "black", 0x1, 0x1)
    SetMapObjFrame(0xFF, "nwindow", 0x1, 0x1)
    SetCameraDistance(15000, 3000)
    FadeToBright(2000, 0)
    Sleep(1000)
    Sound(103, 0, 70, 0)
    ClearMapObjFlags(0xF, 0x10)
    OP_71(0xF, 0x0, 0xA, 0x0, 0x0)
    OP_79(0xF)

    def lambda_3554():
        OP_96(0xFE, 0xFFFF8FE4, 0xFFFFDFF8, 0xFFFFA2A4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3554)

    def lambda_356E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_356E)
    WaitChrThread(0x104, 1)
    Sound(104, 0, 70, 0)
    OP_71(0xF, 0xA, 0x0, 0x0, 0x0)
    OP_79(0xF)
    SetMapObjFlags(0xF, 0x10)
    OP_C9(0x0, 0x80000000)

    #N0088
    NpcTalk(
        0x105,
        "少年的声音",
        "#2916V#30W要走了吗？\x02",
    )

    CloseMessageWindow()
    OP_24(0xB64)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0089
    ChrTalk(
        0x104,
        "#5P#00308F#2760V#30W是你啊……\x02",
    )

    CloseMessageWindow()
    OP_24(0xAC8)
    OP_C9(0x1, 0x80000000)
    VolumeBGM(0x64, 0x64)
    PlayBGM("ed7568", 0)
    OP_68(-22350, -7200, -23350, 2000)
    MoveCamera(31, 13, 0, 2000)
    SetCameraDistance(13000, 2000)
    TurnDirection(0x104, 0x105, 350)
    OP_6F(0x79)
    Sleep(300)

    #C0090
    ChrTalk(
        0x104,
        (
            "#00301F#5P#N真是的，怎么大半夜\x01",
            "还没睡。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    def lambda_3679():
        OP_96(0xFE, 0xFFFFA36C, 0xFFFFDFF8, 0xFFFFA2A4, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3679)
    Sleep(1000)
    OP_68(-21400, -7200, -22930, 2500)
    WaitChrThread(0x104, 1)
    OP_6F(0x79)
    SetCameraDistance(12000, 40000)

    #C0091
    ChrTalk(
        0x105,
        (
            "#10302F#5P呵呵，刚从\x01",
            "酒吧回来。\x02\x03",

            "#10306F嗯……以我的性格来说，\x01",
            "倒是不介意你这种做法……\x02\x03",

            "#10301F但他们肯定会很生气吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0x104,
        (
            "#6P#00306F……大概吧。\x02\x03",

            "#00301F但这是我个人的问题。\x02\x03",

            "和叔叔、谢莉都无关。\x02\x03",

            "更不能把罗伊德他们\x01",
            "卷进来。\x02\x03",

            "#00303F我……为了给自己\x01",
            "做个了断，才决定离开这里。\x02\x03",

            "#00300F仅此而已。\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x105,
        (
            "#10308F#5P呼，好吧。\x02\x03",

            "#10306F你也好，瓦鲁多也好……\x01",
            "男人全都是笨蛋呢。\x02\x03",

            "#10302F为什么非要活得\x01",
            "这么累呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x104,
        (
            "#6P#00306F不用你管。\x02\x03",

            "#00305F……话说回来……\x01",
            "我一直都想问你一个问题。\x02\x03",

            "#00302F你到底是哪一边的？\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0x105,
        (
            "#10304F#5P呵呵，你在说什么？\x01",
            "我完全听不懂呢。\x02\x03",

            "#10300F不过，你的另一个猜测\x01",
            "大概是正确的。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0096
    ChrTalk(
        0x104,
        (
            "#6P#00303F……果然如此。\x02\x03",

            "#00311F你散发出的气息，和我过去\x01",
            "曾经交手过数次的家伙很相似……\x02\x03",

            "你和那个女孩当时是刻意\x01",
            "装作互不相识的吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0x105,
        (
            "#10304F#5P呵呵，算是吧。\x02\x03",

            "#10302F为了答谢你替我隐瞒此事，\x01",
            "我明天早上会装作不知情的。\x02\x03",

            "你就去大闹一场吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x104,
        "#6P#00304F嗯……感激不尽。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(150)
    Sound(812, 0, 100, 0)
    SetChrChipByIndex(0x104, 0x1F)
    SetChrSubChip(0x104, 0x7)
    SetChrFlags(0x104, 0x10)
    SetChrFlags(0x104, 0x2)
    SetChrFlags(0x104, 0x20)
    Sleep(80)
    SetChrSubChip(0x104, 0x0)
    Sleep(500)
    SetCameraDistance(12000, 2000)
    OP_68(-20360, -7200, -22560, 2500)

    def lambda_3A92():

        label("loc_3A92")

        OP_A0(0xFE, 1500, 0x0, 0xFB)
        Yield()
        Jump("loc_3A92")

    QueueWorkItem2(0x104, 3, lambda_3A92)

    def lambda_3AA4():
        OP_95(0xFE, -20000, -8200, -23900, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3AA4)
    Sleep(800)
    SetChrSubChip(0x105, 0x1)
    WaitChrThread(0x104, 1)
    EndChrThread(0x104, 0x3)
    SetChrChipByIndex(0x104, 0x1E)
    SetChrSubChip(0x104, 0x0)
    ClearChrFlags(0x104, 0x10)
    ClearChrFlags(0x104, 0x2)
    ClearChrFlags(0x104, 0x20)

    def lambda_3AE4():
        OP_95(0xFE, -13000, -4200, -17000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3AE4)
    Sleep(500)
    SetChrSubChip(0x105, 0x2)
    Sleep(500)
    OP_6F(0x79)
    OP_68(-20360, -6600, -23560, 2000)
    WaitChrThread(0x104, 1)

    def lambda_3B1F():
        OP_95(0xFE, 0, 0, -17000, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3B1F)
    Sleep(1000)
    OP_6F(0x79)
    OP_63(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x105)
    Sleep(500)

    #C0099
    ChrTalk(
        0x105,
        (
            "#5P#10306F……呼，少了他，\x01",
            "战斗力可能会有点不足吧？\x02\x03",

            "#10308F如果情况需要，\x01",
            "或许要让阿巴斯前来支援了……\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(12500, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    EndChrThread(0x104, 0x1)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)
    ClearChrFlags(0x105, 0x10)
    ClearChrFlags(0x105, 0x2)
    ClearChrFlags(0x105, 0x20)
    ClearChrFlags(0x105, 0x40)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(2000)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x1, 0xFF, 0x0)
    OP_32(0xFF, 0xFE, 0x0)
    RemoveParty(0x3, 0xFF)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x23, 2)
    NewScene("c0120", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_42_333C end

    def Function_43_3C56(): pass

    label("Function_43_3C56")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch02750.itc", 0x1E)
    SoundLoad(868)
    SetChrChipByIndex(0x14, 0x1E)
    SetChrSubChip(0x14, 0x0)
    ClearChrFlags(0x14, 0x80)
    SetChrFlags(0x14, 0x8000)
    OP_52(0x14, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    SetMapObjFrame(0xFF, "bell", 0x0, 0x1)
    ClearMapObjFlags(0x18, 0x4)
    ClearMapObjFlags(0x19, 0x4)
    SetChrFlags(0x0, 0x80)
    SetChrBattleFlags(0x0, 0x8000)
    SetChrFlags(0x1, 0x80)
    SetChrBattleFlags(0x1, 0x8000)
    SetChrFlags(0x2, 0x80)
    SetChrBattleFlags(0x2, 0x8000)
    SetChrFlags(0x3, 0x80)
    SetChrBattleFlags(0x3, 0x8000)
    SetChrPos(0x14, -28800, -8200, -23050, 180)
    BeginChrThread(0x14, 0, 0, 44)
    OP_68(7000, 7500, 11000, 0)
    MoveCamera(35, -5, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(34500, 0)
    OP_68(5000, 2500, 11000, 7000)
    MoveCamera(30, 5, 0, 7000)
    Sound(868, 2, 20, 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    Fade(500)
    OP_68(-28700, -6900, -21200, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(18000, 0)
    MoveCamera(40, 20, 0, 4000)
    SetCameraDistance(15000, 4000)
    StopSound(868, 1000, 20)
    StopBGM(0x1388)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7560", 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x230), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetCameraDistance(14000, 3000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x23, 0)
    NewScene("c011B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_43_3C56 end

    def Function_44_3E26(): pass

    label("Function_44_3E26")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3E4A")
    OP_A1(0xFE, 0x5DC, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    OP_A1(0xFE, 0x5DC, 0x3, 0x3, 0x2, 0x1)
    Jump("Function_44_3E26")

    label("loc_3E4A")

    Return()

    # Function_44_3E26 end

    def Function_45_3E4B(): pass

    label("Function_45_3E4B")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x149, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E5F")
    Call(0, 16)
    Jump("loc_3EEC")

    label("loc_3E5F")

    OP_4B(0x10, 0xFF)
    OP_4B(0x11, 0xFF)
    TurnDirection(0x10, 0x0, 0)
    TurnDirection(0x11, 0x0, 0)

    #C0100
    ChrTalk(
        0x10,
        (
            "在把首脑们送到\x01",
            "米修拉姆之前，\x01",
            "前方路段禁止通行。\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0x10,
        (
            "希望支援科的各位\x01",
            "多加理解，配合我们。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x10, 0xB4, 0x0)
    OP_93(0x11, 0xB4, 0x0)
    OP_4C(0x10, 0xFF)
    OP_4C(0x11, 0xFF)

    label("loc_3EEC")

    Sleep(50)
    SetChrPos(0x0, 11850, 0, 22430, 180)
    EventEnd(0x4)
    Return()

    # Function_45_3E4B end

    def Function_46_3F03(): pass

    label("Function_46_3F03")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0102
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "       『克洛斯贝尔之钟』\x01",
            "Ｓ１１８５，在克洛斯贝尔自治州\x01",
            "发掘出土的巨型大钟。\x01",
            "依据出土遗迹的情况来看，\x01",
            "可推断为中世纪时期的物品。\x01",
            "使用多种金属打造而成，\x01",
            "敲打时会发出悦耳的低音。\x02",
        )
    )

    CloseMessageWindow()

    #A0103
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "据推测，是由当时的权贵人士所制造，\x01",
            "但关于其具体用途，\x01",
            "目前仍然诸说纷纭。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_46_3F03 end

    def Function_47_403D(): pass

    label("Function_47_403D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4066")
    EventBegin(0x1)
    Call(0, 50)
    Sleep(50)
    SetChrPos(0x0, 4240, 0, -20650, 0)
    EventEnd(0x4)

    label("loc_4066")

    Return()

    # Function_47_403D end

    def Function_48_4067(): pass

    label("Function_48_4067")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4090")
    EventBegin(0x1)
    Call(0, 50)
    Sleep(50)
    SetChrPos(0x0, 16840, 0, -3910, 270)
    EventEnd(0x4)

    label("loc_4090")

    Return()

    # Function_48_4067 end

    def Function_49_4091(): pass

    label("Function_49_4091")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_40BA")
    EventBegin(0x1)
    Call(0, 50)
    Sleep(50)
    SetChrPos(0x0, -13380, 0, 14530, 135)
    EventEnd(0x4)

    label("loc_40BA")

    Return()

    # Function_49_4091 end

    def Function_50_40BB(): pass

    label("Function_50_40BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4133")

    #C0104
    ChrTalk(
        0x10A,
        (
            "#00603F通往地下空间Ｂ区域的\x01",
            "入口在住宅街。\x02\x03",

            "#00600F别绕远路了，赶快过去。\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0x101,
        "#00000F嗯，明白。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_4182")

    label("loc_4133")


    #C0106
    ChrTalk(
        0x10A,
        (
            "#00603F通往地下空间Ｂ区域的\x01",
            "入口在住宅街。\x02\x03",

            "#00600F别绕远路了，赶快过去。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4182")

    Return()

    # Function_50_40BB end

    SaveToFile()

Try(main)
