from ScenarioHelper import *

def main():
    CreateScenaFile(
        "c0500.bin",                # FileName
        "c0500",                    # MapName
        "c0500",                    # Location
        0x0026,                     # MapIndex
        "ed7117",
        0x00002000,                 # Flags
        ("c0500", "c1000_1", "", "", "", ""),   # include
        0x1E,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 38, 0, 3, 0, 4],
    )

    BuildStringList((
        "c0500",                  # 0
        "爱丽斯",                 # 1
        "揽客员比修",             # 2
        "警官",                   # 3
        "警官",                   # 4
        "猎兵扎克斯",             # 5
        "猎兵",                   # 6
        "房产经营者",             # 7
        "独眼男人",               # 8
        "红发少女",               # 9
        "雷克特",                 # 10
        "猎兵加雷斯",             # 11
        "车辆",                   # 12
        "格蕾丝",                 # 13
        "曹",                     # 14
        "刘",                     # 15
        "绳子",                   # 16
        "尤利",                   # 17
        "塞克斯",                 # 18
        "瑞吉",                   # 19
        "凯特巡警",               # 20
        "弗兰茨巡警",             # 21
        "SE制御",                 # 22
        "穆拉",                   # 23
        "奥利维尔",               # 24
        "中央广场",               # 25
        "西街",                   # 26
        "行政区",                 # 27
        "住宅街",                 # 28
        "欢乐街",                 # 29
        "东街",                   # 30
        "旧城区",                 # 31
        "港湾区",                 # 32
        "ＩＢＣ",                 # 33
        "站前街道",               # 34
        "后巷",                   # 35
        "乌尔斯拉间道",           # 36
        "东克洛斯贝尔街道",       # 37
        "西克洛斯贝尔街道",       # 38
        "玛因兹山道",             # 39
        "兰花塔",                 # 40
    ))

    AddCharChip((
        "chr/ch26900.itc",                   # 00
        "chr/ch26700.itc",                   # 01
        "chr/ch30000.itc",                   # 02
        "chr/ch27800.itc",                   # 03
        "chr/ch42800.itc",                   # 04
        "chr/ch42900.itc",                   # 05
        "chr/ch43000.itc",                   # 06
        "chr/ch00000.itc",                   # 07
        "chr/ch00000.itc",                   # 08
        "chr/ch00000.itc",                   # 09
        "chr/ch00000.itc",                   # 0A
        "chr/ch00000.itc",                   # 0B
        "chr/ch00000.itc",                   # 0C
        "chr/ch00000.itc",                   # 0D
        "chr/ch00000.itc",                   # 0E
        "chr/ch00000.itc",                   # 0F
        "monster/ch85150.itc",               # 10
        "monster/ch85151.itc",               # 11
    ))

    DeclNpc(-6170,   0,       1399,    90,   257,  0x0, 0,   0,   0,   0,   1,   0,   5,   255,  0)
    DeclNpc(-7590,   0,       2980,    180,  257,  0x0, 0,   1,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(-800,    0,       40500,   180,  389,  0x0, 0,   2,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(800,     0,       40500,   180,  389,  0x0, 0,   2,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(-800,    0,       40500,   180,  389,  0x0, 0,   4,   0,   0,   0,   255, 255, 255,  0)
    DeclNpc(800,     0,       40500,   180,  389,  0x0, 0,   6,   0,   0,   0,   255, 255, 255,  0)
    DeclNpc(-11949,  0,       3000,    180,  449,  0x0, 0,   3,   0,   0,   0,   255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 28,  8.0,                   -2.0,                  -0.5,                  900.0,                 [0.20000000298023224,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.0833333358168602,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -1.600000023841858,    0.1666666716337204,    0.10000000149011612,   1.0])
    DeclEvent(0x0000, 0, 29,  -8.0,                  -2.0,                  -0.5,                  576.0,                 [0.25,                 -0.0,                  0.0,                   0.0,                   -0.0,                  0.0833333358168602,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000001788139343,   0.0,                   2.0,                   0.1666666716337204,    0.10000000894069672,   1.0])
    DeclEvent(0x0000, 0, 34,  0.09000000357627869,   5.46999979019165,      -0.5,                  4.0,                   [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -0.04500000178813934,  -2.734999895095825,    0.10000000149011612,   1.0])

    DeclActor(0,       300,     43650,   1000,    0,       1800,    43650,   0x007C, 0,  35, 0x0000)
    DeclActor(18980,   600,     4810,    1000,    18980,   2100,    4810,    0x007C, 0,  36, 0x0000)
    DeclActor(5660,    790,     5620,    1000,    5660,    2000,    5620,    0x007C, 0,  37, 0x0000)

    PlaceName(79.5, 0.0, -9.0, 0x0000, 0x0000, "中央广场")
    PlaceName(0.0, 0.0, -76.5, 0x0000, 0x0000, "西街")
    PlaceName(11.0, 0.0, 116.0, 0x0000, 0x0000, "行政区")
    PlaceName(-148.0, 0.0, -60.0, 0x0000, 0x0000, "住宅街")
    PlaceName(-57.25, 0.0, 10.0, 0x0000, 0x0000, "欢乐街")
    PlaceName(196.0, 0.0, 56.0, 0x0000, 0x0000, "东街")
    PlaceName(294.0, 0.0, 31.0, 0x0000, 0x0000, "旧城区")
    PlaceName(154.0, 0.0, 158.0, 0x0000, 0x0000, "港湾区")
    PlaceName(20.0, 0.0, 233.0, 0x0000, 0x0000, "ＩＢＣ")
    PlaceName(168.0, 0.0, -73.0, 0x0000, 0x0000, "站前街道")
    PlaceName(1.0, 0.0, -9.0, 0x0000, 0x0000, "后巷")
    PlaceName(200.0, 0.0, -112.0, 0x0000, 0x0000, "乌尔斯拉间道")
    PlaceName(240.0, 0.0, 130.0, 0x0000, 0x0000, "东克洛斯贝尔街道")
    PlaceName(-52.0, 0.0, -134.0, 0x0000, 0x0000, "西克洛斯贝尔街道")
    PlaceName(-156.0, 0.0, -17.0, 0x0000, 0x0000, "玛因兹山道")
    PlaceName(-140.0, 0.0, 255.0, 0x0000, 0x0000, "兰花塔")
    PlaceName(71.0, 0.0, -49.0, 0x0000, 0x0051, "")
    PlaceName(100.5, 0.0, 38.5, 0x0000, 0x0054, "")
    PlaceName(106.0, 0.0, -31.0, 0x0000, 0x0057, "")
    PlaceName(38.0, 0.0, -18.5, 0x0000, 0x0053, "")
    PlaceName(35.5, 0.0, 32.0, 0x0000, 0x0053, "")
    PlaceName(9.0, 0.0, -57.0, 0x0000, 0x0053, "")
    PlaceName(-23.5, 0.0, -45.0, 0x0000, 0x0053, "")
    PlaceName(-33.0, 0.0, 16.0, 0x0000, 0x0052, "")
    PlaceName(-15.0, 0.0, 8.0, 0x0000, 0x0053, "")
    PlaceName(6.0, 0.0, 8.0, 0x0000, 0x0053, "")
    PlaceName(-41.0, 0.0, 118.0, 0x0000, 0x0051, "")
    PlaceName(233.0, 0.0, 91.0, 0x0000, 0x0052, "")
    PlaceName(313.0, 0.0, -26.0, 0x0000, 0x0053, "")
    PlaceName(278.0, 0.0, -19.5, 0x0000, 0x0053, "")

    ChipFrameInfo(2048, 0)                                       # 0

    ScpFunction((
        "Function_0_800",          # 00, 0
        "Function_1_8B0",          # 01, 1
        "Function_2_917",          # 02, 2
        "Function_3_9A0",          # 03, 3
        "Function_4_C78",          # 04, 4
        "Function_5_FF8",          # 05, 5
        "Function_6_1BC4",         # 06, 6
        "Function_7_25D9",         # 07, 7
        "Function_8_26F5",         # 08, 8
        "Function_9_272D",         # 09, 9
        "Function_10_2791",        # 0A, 10
        "Function_11_2EF2",        # 0B, 11
        "Function_12_363D",        # 0C, 12
        "Function_13_390E",        # 0D, 13
        "Function_14_3A47",        # 0E, 14
        "Function_15_3A74",        # 0F, 15
        "Function_16_3AAB",        # 10, 16
        "Function_17_4A38",        # 11, 17
        "Function_18_4A96",        # 12, 18
        "Function_19_4A97",        # 13, 19
        "Function_20_4AED",        # 14, 20
        "Function_21_4AEE",        # 15, 21
        "Function_22_4B53",        # 16, 22
        "Function_23_4B54",        # 17, 23
        "Function_24_5135",        # 18, 24
        "Function_25_54FE",        # 19, 25
        "Function_26_5527",        # 1A, 26
        "Function_27_558F",        # 1B, 27
        "Function_28_5706",        # 1C, 28
        "Function_29_5A7B",        # 1D, 29
        "Function_30_5DC9",        # 1E, 30
        "Function_31_72F8",        # 1F, 31
        "Function_32_7577",        # 20, 32
        "Function_33_79D9",        # 21, 33
        "Function_34_8567",        # 22, 34
        "Function_35_88BB",        # 23, 35
        "Function_36_89CE",        # 24, 36
        "Function_37_8A26",        # 25, 37
        "Function_38_8A4F",        # 26, 38
        "Function_39_8A9E",        # 27, 39
    ))


    def Function_0_800(): pass

    label("Function_0_800")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_838"),
        (1, "loc_844"),
        (2, "loc_850"),
        (3, "loc_85C"),
        (4, "loc_868"),
        (5, "loc_874"),
        (6, "loc_880"),
        (SWITCH_DEFAULT, "loc_88C"),
    )


    label("loc_838")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_898")

    label("loc_844")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_898")

    label("loc_850")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_898")

    label("loc_85C")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_898")

    label("loc_868")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_898")

    label("loc_874")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_898")

    label("loc_880")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_898")

    label("loc_88C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_898")

    label("loc_898")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_8AF")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_898")

    label("loc_8AF")

    Return()

    # Function_0_800 end

    def Function_1_8B0(): pass

    label("Function_1_8B0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_916")
    OP_95(0xFE, -240, 0, 1400, 1000, 0x0)
    OP_95(0xFE, -240, 0, 15530, 1000, 0x0)
    Sleep(3600)
    OP_95(0xFE, -240, 0, 1400, 1000, 0x0)
    OP_95(0xFE, -24330, 0, 1400, 1000, 0x0)
    Sleep(1200)
    Jump("Function_1_8B0")

    label("loc_916")

    Return()

    # Function_1_8B0 end

    def Function_2_917(): pass

    label("Function_2_917")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_99F")
    OP_95(0xFE, -240, 0, 1400, 1000, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Sleep(1800)
    OP_93(0xFE, 0x5A, 0x1F4)
    OP_95(0xFE, 8240, 0, 1400, 1000, 0x0)
    Sleep(3600)
    OP_95(0xFE, 740, 0, 1400, 1000, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Sleep(1800)
    OP_93(0xFE, 0x10E, 0x1F4)
    OP_95(0xFE, -24330, 0, 1400, 1000, 0x0)
    Sleep(1200)
    Jump("Function_2_917")

    label("loc_99F")

    Return()

    # Function_2_917 end

    def Function_3_9A0(): pass

    label("Function_3_9A0")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6D), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B30")
    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A8F")
    SetChrPos(0x0, 20160, 0, 650, 270)
    SetChrPos(0x1, 20160, 0, 650, 270)
    SetChrPos(0x2, 20160, 0, 650, 270)
    SetChrPos(0x3, 20160, 0, 650, 270)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A62")
    SetChrPos(0x4, 20160, 0, 650, 270)
    SetChrPos(0x5, 20160, 0, 650, 270)
    Jump("loc_A81")

    label("loc_A62")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A81")
    SetChrPos(0x4, 20160, 0, 650, 270)

    label("loc_A81")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B30")

    label("loc_A8F")

    SetChrPos(0x0, -24900, 0, 220, 90)
    SetChrPos(0x1, -24900, 0, 220, 90)
    SetChrPos(0x2, -24900, 0, 220, 90)
    SetChrPos(0x3, -24900, 0, 220, 90)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B08")
    SetChrPos(0x4, -24900, 0, 220, 90)
    SetChrPos(0x5, -24900, 0, 220, 90)
    Jump("loc_B27")

    label("loc_B08")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B27")
    SetChrPos(0x4, -24900, 0, 220, 90)

    label("loc_B27")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_B30")

    OP_D2(0x7, (scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_B47")
    Jump("loc_B93")

    label("loc_B47")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_B5F")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    Jump("loc_B93")

    label("loc_B5F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_B6D")
    Jump("loc_B93")

    label("loc_B6D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_B80")
    SetChrFlags(0x8, 0x80)
    Jump("loc_B93")

    label("loc_B80")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_B93")
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)

    label("loc_B93")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_BA7")
    ClearScenarioFlags(0x22, 0)
    Event(0, 13)
    Jump("loc_C32")

    label("loc_BA7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_BBB")
    ClearScenarioFlags(0x22, 1)
    Event(0, 23)
    Jump("loc_C32")

    label("loc_BBB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 2)), scpexpr(EXPR_END)), "loc_BCF")
    ClearScenarioFlags(0x22, 2)
    Event(0, 24)
    Jump("loc_C32")

    label("loc_BCF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 3)), scpexpr(EXPR_END)), "loc_BE8")
    ClearScenarioFlags(0x22, 3)
    SetMapFlags(0x10000000)
    Event(0, 31)
    Jump("loc_C32")

    label("loc_BE8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 4)), scpexpr(EXPR_END)), "loc_C01")
    ClearScenarioFlags(0x22, 4)
    SetMapFlags(0x10000000)
    Event(0, 32)
    Jump("loc_C32")

    label("loc_C01")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 5)), scpexpr(EXPR_END)), "loc_C15")
    ClearScenarioFlags(0x22, 5)
    Event(0, 33)
    Jump("loc_C32")

    label("loc_C15")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 6)), scpexpr(EXPR_END)), "loc_C32")
    ClearScenarioFlags(0x22, 6)
    SetChrPos(0x0, -10280, 0, 250, 90)

    label("loc_C32")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C4C")
    Event(0, 27)

    label("loc_C4C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 6)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6A, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6B, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6C, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C77")
    SetMapFlags(0x10000000)
    Event(1, 0)

    label("loc_C77")

    Return()

    # Function_3_9A0 end

    def Function_4_C78(): pass

    label("Function_4_C78")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C94")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x97), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_CC8")

    label("loc_C94")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CB0")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x7D), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_CC8")

    label("loc_CB0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 0)), scpexpr(EXPR_END)), "loc_CC8")
    SetScenarioFlags(0x0, 3)
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x25, 0)

    label("loc_CC8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_CDC")
    OP_24(0x80)
    ClearScenarioFlags(0x0, 3)
    Jump("loc_D87")

    label("loc_CDC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_D87")
    OP_7D(0xB4, 0xB4, 0xB4, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0xE, 0x64, 0x0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x68), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_D7C")
    LoadEffect(0x9, "map/mprain00.eff")
    PlayEffect(0x9, 0x7, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 1000)
    Sound(128, 1, 100, 0)
    Jump("loc_D87")

    label("loc_D7C")

    StopEffect(0x7, 0x0)
    OP_8A(0x9)
    Sound(128, 1, 60, 0)

    label("loc_D87")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_DF6")
    LoadEffect(0x9, "map/mpmoya.eff")
    PlayEffect(0x9, 0x7, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 1000)
    OP_7D(0x78, 0x96, 0xFF, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xFF, 0xE, 0x64, 0x0)

    label("loc_DF6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_E18")
    OP_7D(0xDC, 0xEB, 0xFF, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0x1E, 0x78, 0x0)

    label("loc_E18")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E31")
    OP_10(0x0, 0x0)
    OP_10(0xB, 0x1)
    Jump("loc_E37")

    label("loc_E31")

    OP_10(0x0, 0x1)
    OP_10(0xB, 0x0)

    label("loc_E37")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E50")
    BeginChrThread(0x8, 0, 0, 2)
    OP_1B(0x2, 0x0, 0x10)

    label("loc_E50")

    ModifyEventFlags(0, 0, 0x80)
    ModifyEventFlags(0, 1, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x66, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x66, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x66, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x130, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x130, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E89")
    ModifyEventFlags(1, 0, 0x80)
    ModifyEventFlags(1, 1, 0x80)

    label("loc_E89")

    ModifyEventFlags(0, 2, 0x80)
    ClearMapObjFlags(0x2, 0x10)
    OP_70(0x2, 0x0)
    OP_65(0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_EAE")
    OP_66(0x0, 0x1)
    Jump("loc_F9F")

    label("loc_EAE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_ED4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 2)), scpexpr(EXPR_END)), "loc_ECB")
    SetMapObjFlags(0x2, 0x10)
    Jump("loc_ECF")

    label("loc_ECB")

    OP_66(0x0, 0x1)

    label("loc_ECF")

    Jump("loc_F9F")

    label("loc_ED4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_EE6")
    OP_66(0x0, 0x1)
    Jump("loc_F9F")

    label("loc_EE6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_EF4")
    Jump("loc_F9F")

    label("loc_EF4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_F07")
    ModifyEventFlags(1, 2, 0x80)
    Jump("loc_F9F")

    label("loc_F07")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_F1A")
    ModifyEventFlags(1, 2, 0x80)
    Jump("loc_F9F")

    label("loc_F1A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_F2D")
    ModifyEventFlags(1, 2, 0x80)
    Jump("loc_F9F")

    label("loc_F2D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_F40")
    ModifyEventFlags(1, 2, 0x80)
    Jump("loc_F9F")

    label("loc_F40")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_F53")
    ModifyEventFlags(1, 2, 0x80)
    Jump("loc_F9F")

    label("loc_F53")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 4)), scpexpr(EXPR_END)), "loc_F71")
    SetMapObjFlags(0x2, 0x10)
    OP_1B(0x0, 0x0, 0x26)
    OP_1B(0x1, 0x0, 0x27)
    Jump("loc_F9F")

    label("loc_F71")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_F83")
    OP_66(0x0, 0x1)
    Jump("loc_F9F")

    label("loc_F83")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_F9F")
    OP_66(0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x130, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F9F")
    ModifyEventFlags(1, 2, 0x80)

    label("loc_F9F")

    ClearMapObjFlags(0x3, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_FBB")
    OP_70(0x3, 0x5)
    OP_65(0x1, 0x1)

    label("loc_FBB")

    OP_65(0x2, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x85, 0x0, 0x10)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_FDE")
    ClearMapObjFlags(0x0, 0x10)
    OP_70(0x0, 0x0)
    OP_66(0x2, 0x1)

    label("loc_FDE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FF7")
    SetMapObjFrame(0xFF, "crimson", 0x0, 0x1)

    label("loc_FF7")

    Return()

    # Function_4_C78 end

    def Function_5_FF8(): pass

    label("Function_5_FF8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_112A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10B9")

    #C0001
    ChrTalk(
        0xFE,
        (
            "由于现在的状况太糟糕，\x01",
            "连店里的气氛都受到了影响。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0xFE,
        (
            "我突然觉得和同行竞争\x01",
            "这种小事已经\x01",
            "无关紧要了。\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0xFE,
        (
            "身为一名女公关，\x01",
            "只要能让客人开开心心\x01",
            "喝酒就好了☆\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1125")

    label("loc_10B9")


    #C0004
    ChrTalk(
        0xFE,
        (
            "我突然觉得和同行竞争\x01",
            "这种小事已经\x01",
            "无关紧要了。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0xFE,
        (
            "身为一名女公关，\x01",
            "只要能让客人开开心心\x01",
            "喝酒就好了☆\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1125")

    Jump("loc_1BC0")

    label("loc_112A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_1138")
    Jump("loc_1BC0")

    label("loc_1138")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_122F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11CF")

    #C0006
    ChrTalk(
        0xFE,
        (
            "独立……\x01",
            "听起来可真威风啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0xFE,
        (
            "店里的客人们\x01",
            "听了总统的演讲之后，\x01",
            "都非常兴奋。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0xFE,
        (
            "……连我也忍不住\x01",
            "跟着兴奋起来了¤\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_122A")

    label("loc_11CF")


    #C0009
    ChrTalk(
        0xFE,
        (
            "店里的客人们\x01",
            "听了总统的演讲之后，\x01",
            "都非常兴奋。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0xFE,
        (
            "……连我也忍不住\x01",
            "跟着兴奋起来了¤\x02",
        )
    )

    CloseMessageWindow()

    label("loc_122A")

    Jump("loc_1BC0")

    label("loc_122F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_123D")
    Jump("loc_1BC0")

    label("loc_123D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_12C2")

    #C0011
    ChrTalk(
        0xFE,
        (
            "玛因兹居然被占领了，\x01",
            "这可真是重大事件……！\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0xFE,
        (
            "那里的矿工们前不久\x01",
            "还到我们店里玩过呢。\x01",
            "真希望他们平安无事啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BC0")

    label("loc_12C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_13D0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1364")

    #C0013
    ChrTalk(
        0xFE,
        "听我说，听我说，这可是大新闻啊！\x02",
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0xFE,
        (
            "我们店本月被客人指名\x01",
            "次数最多的人已经公布了！\x01",
            "那就是我！\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0xFE,
        (
            "呵呵呵，不枉我那么\x01",
            "努力呢～！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_13CB")

    label("loc_1364")


    #C0016
    ChrTalk(
        0xFE,
        (
            "终于成为梦寐以求的\x01",
            "第一名啦！\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0xFE,
        (
            "呵呵，今后大概会有\x01",
            "更多的客人指名找我，\x01",
            "我一定要继续努力才行！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13CB")

    Jump("loc_1BC0")

    label("loc_13D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_1413")

    #C0018
    ChrTalk(
        0xFE,
        (
            "中央广场那边很吵呢……\x01",
            "怎么了？发生了什么事吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BC0")

    label("loc_1413")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_151F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14D0")

    #C0019
    ChrTalk(
        0xFE,
        (
            "和我竞争指名次数的那个女孩，\x01",
            "为了增加自己的指名次数，\x01",
            "居然把朋友叫到我们的店里消费。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0xFE,
        "唔唔～这也太狡猾了吧！？\x02",
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0xFE,
        (
            "既然如此，\x01",
            "那我也要使出\x01",
            "浑身解数了！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_151A")

    label("loc_14D0")


    #C0022
    ChrTalk(
        0xFE,
        (
            "怎么能输给\x01",
            "那个女孩呢！\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0xFE,
        (
            "为了夺得第一名的宝座，\x01",
            "我什么都会做的！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_151A")

    Jump("loc_1BC0")

    label("loc_151F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1649")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15BF")

    #C0024
    ChrTalk(
        0xFE,
        (
            "小哥～\x01",
            "要不要来我们店玩玩啊～？\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0xFE,
        (
            "……我和竞争对手的\x01",
            "指名次数相差无几。\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0xFE,
        (
            "赢了的人就是本月的第一名！\x01",
            "所以你们就帮帮我嘛！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1644")

    label("loc_15BF")


    #C0027
    ChrTalk(
        0xFE,
        (
            "……唔……这样啊。\x01",
            "原来你们在工作啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0xFE,
        (
            "那就没办法了，以后来我们店时，\x01",
            "可要记得指名找我哦。\x01",
            "这可关系到我能不能成为第一名呢！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1644")

    Jump("loc_1BC0")

    label("loc_1649")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_16B2")

    #C0029
    ChrTalk(
        0xFE,
        (
            "最近这几天，我那个竞争对手的\x01",
            "指名次数一直在不断增加。\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0xFE,
        "我也要加油，绝不能输给她。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1BC0")

    label("loc_16B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_17FD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_179D")

    #C0031
    ChrTalk(
        0xFE,
        (
            "兰花塔可真是\x01",
            "一栋惊人的建筑啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0xFE,
        (
            "我也放下工作，\x01",
            "去现场观看了那场揭幕式，\x01",
            "当时真是震撼得双腿发软。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0xFE,
        (
            "在那种地方工作的人，\x01",
            "一定都是十分有钱的\x01",
            "贵人吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0xFE,
        (
            "如果他们来我们店玩，\x01",
            "真希望能指名找我啊～\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_17F8")

    label("loc_179D")


    #C0035
    ChrTalk(
        0xFE,
        (
            "兰花塔可真是\x01",
            "一栋惊人的建筑啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0xFE,
        (
            "在那种地方工作的人，\x01",
            "一定都是十分有钱的\x01",
            "贵人吧？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17F8")

    Jump("loc_1BC0")

    label("loc_17FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_191E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1896")

    #C0037
    ChrTalk(
        0xFE,
        (
            "我听客人说，\x01",
            "从明天开始，\x01",
            "要召开一个什么通商会议～\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0xFE,
        (
            "听起来不像是纪念庆典\x01",
            "那样的重大庆典……\x01",
            "到底是个什么样的活动呢？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1919")

    label("loc_1896")


    #C0039
    ChrTalk(
        0xFE,
        (
            "算啦，不管那些了，\x01",
            "反正也不是什么值得留意的事情。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0xFE,
        (
            "为了不输给我的竞争对手，\x01",
            "现在最重要的事情是想办法\x01",
            "增加自己的指名次数。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1919")

    Jump("loc_1BC0")

    label("loc_191E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 4)), scpexpr(EXPR_END)), "loc_1A4E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19E2")

    #C0041
    ChrTalk(
        0xFE,
        (
            "刚才有个满头红发，\x01",
            "体格健壮的大叔\x01",
            "在这附近。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0xFE,
        (
            "他带着一个像小猫一样\x01",
            "可爱的女孩，还有一个\x01",
            "看上去很散漫的小哥……\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0xFE,
        (
            "总之，那几个人凑在一起，\x01",
            "看起来真是奇怪啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1A49")

    label("loc_19E2")


    #C0044
    ChrTalk(
        0xFE,
        (
            "说起来，\x01",
            "刚才过去的那个小哥，\x01",
            "头发颜色和那大叔一样～\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0xFE,
        (
            "他们是不是一家人呢？\x01",
            "但相貌却不是很像。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A49")

    Jump("loc_1BC0")

    label("loc_1A4E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_1ACE")

    #C0046
    ChrTalk(
        0xFE,
        (
            "听说小巷里那片地已经售出了，\x01",
            "这是真的吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0xFE,
        (
            "那里以前有一群身穿黑衣服的可怕小哥……\x01",
            "这次会是什么人入驻呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BC0")

    label("loc_1ACE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_1BC0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B51")

    #C0048
    ChrTalk(
        0xFE,
        "嘻嘻，我是爱丽斯～☆\x02",
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0xFE,
        (
            "小哥～\x01",
            "要不要来我们店玩玩呀～？\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0xFE,
        (
            "可以跟我喝酒谈心，\x01",
            "会很开心的哦～⊥\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1BC0")

    label("loc_1B51")


    #C0051
    ChrTalk(
        0xFE,
        (
            "最近，我的指名次数增加了，\x01",
            "工作十分充实。\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0xFE,
        (
            "接下来要和竞争对手\x01",
            "拉开差距，然后夺下\x01",
            "指名次数第一的宝座！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BC0")

    TalkEnd(0xFE)
    Return()

    # Function_5_FF8 end

    def Function_6_1BC4(): pass

    label("Function_6_1BC4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1D00")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C83")

    #C0053
    ChrTalk(
        0xFE,
        (
            "小哥小哥，\x01",
            "要不要来我们店玩玩呀～？\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0xFE,
        (
            "为了纪念迪塔总统被捕，\x01",
            "本店正在举行大酬宾活动～！\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0xFE,
        (
            "……其实纪念独立时，本店也搞了\x01",
            "大酬宾，不过那可是个秘密喔。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1CFB")

    label("loc_1C83")


    #C0056
    ChrTalk(
        0xFE,
        (
            "为了纪念迪塔总统被捕，\x01",
            "本店正在举行大酬宾活动～！\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0xFE,
        (
            "……其实纪念独立时，本店也搞了\x01",
            "大酬宾，不过那可是个秘密喔。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1CFB")

    Jump("loc_25D5")

    label("loc_1D00")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_1D0E")
    Jump("loc_25D5")

    label("loc_1D0E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_1D9C")

    #C0058
    ChrTalk(
        0xFE,
        (
            "小哥小哥，\x01",
            "本店为了纪念独立成功，\x01",
            "正在举行大酬宾活动！\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0xFE,
        (
            "克洛斯贝尔终于迎来了黎明，\x01",
            "自然要和可爱的女孩子一起\x01",
            "庆祝啊～！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_25D5")

    label("loc_1D9C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1E2B")

    #C0060
    ChrTalk(
        0xFE,
        (
            "小哥小哥，本店已经在\x01",
            "不久前重新开始营业了～\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0xFE,
        (
            "因重建工作而疲惫不堪的身心，\x01",
            "就要靠和可爱女孩一起\x01",
            "喝酒玩闹的方式来治愈哦！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_25D5")

    label("loc_1E2B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_1E93")

    #C0062
    ChrTalk(
        0xFE,
        (
            "玛因兹居然被占领了……\x01",
            "真是重大事件啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0xFE,
        (
            "发生了这种事情，\x01",
            "连我都没心情去揽客了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_25D5")

    label("loc_1E93")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1F17")

    #C0064
    ChrTalk(
        0xFE,
        (
            "哎呀呀，又开始下雨了。\x01",
            "客人也那么少，真让人郁闷～\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0xFE,
        (
            "听说昨天发生了一起十分严重的事故，\x01",
            "最近可真是坏事不断啊～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_25D5")

    label("loc_1F17")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_1F70")

    #C0066
    ChrTalk(
        0xFE,
        (
            "广场那边老是传来\x01",
            "嘟嘟嘟的声音，吵死人了。\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0xFE,
        "是不是又出了什么事啊？\x02",
    )

    CloseMessageWindow()
    Jump("loc_25D5")

    label("loc_1F70")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_20B0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2034")

    #C0068
    ChrTalk(
        0xFE,
        (
            "本店今天正在举行\x01",
            "开心大酬宾活动。\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0xFE,
        (
            "可爱的女孩子们会\x01",
            "身穿可爱的衣服\x01",
            "迎接各位～！\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0xFE,
        (
            "一旦错过今天，可就不知何时\x01",
            "才能再次享受这种服务了！\x01",
            "来来来，快来看看吧～！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_20AB")

    label("loc_2034")


    #C0071
    ChrTalk(
        0xFE,
        (
            "本店今天正在举行\x01",
            "开心大酬宾活动。\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0xFE,
        (
            "一旦错过今天，可就不知何时\x01",
            "才能再次享受这种服务了！\x01",
            "来来来，快来看看吧～！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_20AB")

    Jump("loc_25D5")

    label("loc_20B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2139")

    #C0073
    ChrTalk(
        0xFE,
        (
            "大家最近总是在讨论一些\x01",
            "诸如独立之类的深奥话题。\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0xFE,
        (
            "在这种时候，\x01",
            "就更该来本店转换一下心情～\x01",
            "保证会让你开开心心的～¤\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_25D5")

    label("loc_2139")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_21BE")

    #C0075
    ChrTalk(
        0xFE,
        (
            "我在大街上看到的\x01",
            "几位警察小哥\x01",
            "好像都很卖力呢～\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0xFE,
        (
            "我的揽客对象就是工作得疲惫不堪的人。\x01",
            "呵呵，稍后去招呼一声吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_25D5")

    label("loc_21BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_222A")

    #C0077
    ChrTalk(
        0xFE,
        (
            "各国首脑们好像\x01",
            "已经来到了克洛斯贝尔。\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0xFE,
        (
            "如果他们能来本店喝一杯，\x01",
            "肯定会成为绝佳宣传～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_25D5")

    label("loc_222A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_22BB")

    #C0079
    ChrTalk(
        0xFE,
        (
            "入驻后面那座大楼的\x01",
            "深红商会的小哥们\x01",
            "看起来都是些爽朗的人啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0xFE,
        (
            "呵呵，给他们介绍些可爱的女孩，\x01",
            "发展他们成为本店的新常客吧～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_25D5")

    label("loc_22BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 4)), scpexpr(EXPR_END)), "loc_236D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_232E")

    #C0081
    ChrTalk(
        0xFE,
        (
            "哎呀～不好不好，\x01",
            "雨越下越大了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0xFE,
        (
            "估计今天已经揽不到客人了。\x01",
            "不如收工回家吧～\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2368")

    label("loc_232E")


    #C0083
    ChrTalk(
        0xFE,
        (
            "……你问那个红发的小哥？\x01",
            "他刚刚走进了\x01",
            "那边那条小巷。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2368")

    Jump("loc_25D5")

    label("loc_236D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_23C2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x139, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2388")
    Call(0, 7)
    Jump("loc_23BD")

    label("loc_2388")


    #C0084
    ChrTalk(
        0xFE,
        (
            "在下雨天\x01",
            "很难揽到客人。\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0xFE,
        "哎呀呀，真讨厌啊。\x02",
    )

    CloseMessageWindow()

    label("loc_23BD")

    Jump("loc_25D5")

    label("loc_23C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_25D5")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x66, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x130, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_24D9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_246D")

    #C0086
    ChrTalk(
        0xFE,
        (
            "刚刚有位红发小哥从这里通过，\x01",
            "往欢乐街方向去了……\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0xFE,
        (
            "总觉得以前也\x01",
            "曾在这附近\x01",
            "见过他呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0xFE,
        "算了，应该是心理作用吧。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_24D4")

    label("loc_246D")


    #C0089
    ChrTalk(
        0xFE,
        (
            "那个红发小哥\x01",
            "往欢乐街方向走了。\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0xFE,
        (
            "总觉得以前也曾\x01",
            "在这附近见过他呢……\x01",
            "算了，应该是心理作用吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_24D4")

    Jump("loc_25D5")

    label("loc_24D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x139, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_24EB")
    Call(0, 7)
    Jump("loc_25D5")

    label("loc_24EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_25AE")

    #C0091
    ChrTalk(
        0xFE,
        (
            "嘿嘿，不好意思啦，\x01",
            "这次就放过我吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0xFE,
        (
            "我可以送你几张下次\x01",
            "来店时能用到的优惠券。\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x101,
        (
            "#00003F我不需要那种东西。\x01",
            "……而且贿赂也属于犯罪行为哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0xFE,
        (
            "嘿嘿，\x01",
            "真是服了你了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_25D5")

    label("loc_25AE")


    #C0095
    ChrTalk(
        0xFE,
        (
            "嘿嘿，不好意思，\x01",
            "这次就放过我吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_25D5")

    TalkEnd(0xFE)
    Return()

    # Function_6_1BC4 end

    def Function_7_25D9(): pass

    label("Function_7_25D9")


    #C0096
    ChrTalk(
        0x9,
        (
            "啊，几位小哥，\x01",
            "你们有空吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0x9,
        (
            "本店有很多\x01",
            "可爱的女孩子哦～！\x01",
            "来来，来看看嘛！怎么样啊？\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x101,
        "#00001F……强行揽客可是违法行为哦。\x02",
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0x9,
        (
            "别说这种扫兴的话嘛……\x01",
            "咦？你们是警察啊？\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0x9,
        (
            "嘿嘿，不好意思啦，\x01",
            "这次就放过我吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0x102,
        (
            "#00106F（呼……这一带还是老样子，\x01",
            "  治安真差啊。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x139, 2)
    Return()

    # Function_7_25D9 end

    def Function_8_26F5(): pass

    label("Function_8_26F5")

    TalkBegin(0xFE)

    #C0102
    ChrTalk(
        0xFE,
        (
            "一科正在调查\x01",
            "这栋建筑。\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0xFE,
        "请勿随便入内。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_8_26F5 end

    def Function_9_272D(): pass

    label("Function_9_272D")

    TalkBegin(0xFE)

    #C0104
    ChrTalk(
        0xFE,
        (
            "赤色星座的那帮混蛋，\x01",
            "竟敢干出如此\x01",
            "无法无天的事情。\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0xFE,
        (
            "真希望能早日\x01",
            "解决这起事件啊……\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_9_272D end

    def Function_10_2791(): pass

    label("Function_10_2791")

    EventBegin(0x0)
    SetChrPos(0x101, -600, 0, 37200, 0)
    SetChrPos(0x102, 600, 0, 37200, 0)
    SetChrPos(0x109, -1200, 0, 36000, 0)
    SetChrPos(0x105, 1200, 0, 36000, 0)
    ClearChrFlags(0xE, 0x8)
    SetChrPos(0xE, 0, 0, 27000, 0)
    ClearChrFlags(0xE, 0x80)
    ClearChrBattleFlags(0xE, 0x8000)
    Fade(1000)
    OP_68(-100, 900, 38010, 0)
    MoveCamera(24, 25, 0, 0)
    OP_6E(520, 0)
    SetCameraDistance(17100, 0)
    OP_0D()

    #C0106
    ChrTalk(
        0x101,
        (
            "#12P#00001F这里是……\x01",
            "鲁巴彻商会的旧址。\x02\x03",

            "#00003F现在应该已经是空屋了……\x02",
        )
    )

    CloseMessageWindow()

    #N0107
    NpcTalk(
        0xE,
        "男人的声音",
        (
            "哎呀，你们几个，\x01",
            "在那里干什么呢？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_68(200, 900, 36700, 3000)
    MoveCamera(36, 27, 0, 3000)
    OP_6E(520, 3000)
    SetCameraDistance(17780, 3000)

    def lambda_2933():

        label("loc_2933")

        TurnDirection(0xFE, 0xE, 300)
        Yield()
        Jump("loc_2933")

    QueueWorkItem2(0x101, 2, lambda_2933)

    def lambda_2945():

        label("loc_2945")

        TurnDirection(0xFE, 0xE, 300)
        Yield()
        Jump("loc_2945")

    QueueWorkItem2(0x102, 2, lambda_2945)

    def lambda_2957():

        label("loc_2957")

        TurnDirection(0xFE, 0xE, 300)
        Yield()
        Jump("loc_2957")

    QueueWorkItem2(0x109, 2, lambda_2957)

    def lambda_2969():

        label("loc_2969")

        TurnDirection(0xFE, 0xE, 300)
        Yield()
        Jump("loc_2969")

    QueueWorkItem2(0x105, 2, lambda_2969)

    def lambda_297B():
        OP_95(0xFE, 0, 0, 33500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_297B)
    WaitChrThread(0xE, 1)
    OP_4B(0xE, 0xFF)

    #C0108
    ChrTalk(
        0x101,
        "#00005F请问您是……？\x02",
    )

    CloseMessageWindow()
    EndChrThread(0x101, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x109, 0x2)
    EndChrThread(0x105, 0x2)

    #N0109
    NpcTalk(
        0xE,
        "男人",
        (
            "#12P咳咳，我是克洛斯贝尔市的\x01",
            "一名房产经营者。\x02",
        )
    )

    CloseMessageWindow()

    #N0110
    NpcTalk(
        0xE,
        "男人",
        (
            "#12P受自治州政府所托，\x01",
            "目前负责管理这一片土地，\x02",
        )
    )

    CloseMessageWindow()

    #N0111
    NpcTalk(
        0xE,
        "男人",
        "#12P你们随便进入这里可不大好哦。\x02",
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0x102,
        (
            "#5P#00103F受政府所托……\x01",
            "说起来，我倒是听外公\x01",
            "说过这件事。\x02\x03",

            "#00100F毕竟这里曾是黑手党的地盘，\x01",
            "总不能放置不管，\x01",
            "所以就委托给他人负责管理了。\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0x101,
        (
            "#5P#00003F原来如此……\x02\x03",

            "#00000F那个……不好意思，\x01",
            "我们是克洛斯贝尔的警察。\x02\x03",

            "现在正在市内\x01",
            "巡逻。\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0xE,
        (
            "#12P哦，原来你们是警察啊。\x01",
            "还得到这种地方来巡逻，真是辛苦了。\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0x109,
        (
            "#5P#10100F请问……您今天是来对\x01",
            "这栋大楼进行定期检查的吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0xE,
        (
            "#12P不是的……\x01",
            "这栋大楼在近期内\x01",
            "就要正式出售了。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0117
    ChrTalk(
        0x101,
        "#5P#00005F这里要出售了……？\x02",
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0xE,
        (
            "#12P是啊，之前已经有好几家企业\x01",
            "联系过我，表示想要入驻这里了。\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0xE,
        (
            "#12P今天也有一家企业要来和我交涉，\x01",
            "所以我先来这里等着他们。\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0x109,
        (
            "#5P#10105F打算入驻原黑手党\x01",
            "地盘的企业吗……\x02\x03",

            "#10106F那个，虽说这样问不太合适……\x01",
            "不过真的没问题吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0xE,
        "#12P这个嘛，其实我们也有些不安……\x02",
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0xE,
        (
            "#12P但这栋大楼实在是很大，\x01",
            "光是管理费就不是一笔小数目。\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0xE,
        (
            "#12P如果有人肯接手，\x01",
            "我们可没有拒绝的理由啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0x105,
        (
            "#5P#10303F说的也是，作为房产经营者，\x01",
            "自然想把这栋大楼\x01",
            "早点抛售出去吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0x101,
        (
            "#5P#00003F嗯，虽然有点在意……\x02\x03",

            "#00000F但总不能打扰别人谈生意，\x01",
            "我们还是赶快离开吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0x102,
        "#5P#00103F嗯……好的。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrFlags(0xE, 0x8)
    SetChrPos(0x0, 90, 0, 80, 180)
    SetScenarioFlags(0x139, 1)
    EventEnd(0x5)
    Return()

    # Function_10_2791 end

    def Function_11_2EF2(): pass

    label("Function_11_2EF2")

    EventBegin(0x0)
    FadeToDark(500, 0, -1)
    OP_0D()
    OP_68(0, 1000, 45000, 0)
    MoveCamera(0, 10, 0, 0)
    OP_6E(660, 0)
    SetCameraDistance(17000, 0)
    ClearChrFlags(0xC, 0x8)
    ClearChrFlags(0xD, 0x8)
    SetChrPos(0xC, -800, 0, 40500, 180)
    SetChrPos(0xD, 800, 0, 40500, 180)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrPos(0x101, -600, 0, 29200, 0)
    SetChrPos(0x102, 600, 0, 29200, 0)
    SetChrPos(0x104, 0, 0, 31000, 0)
    SetChrPos(0x109, -600, 0, 28000, 0)
    SetChrPos(0x105, 600, 0, 28000, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    Fade(1000)
    OP_68(110, 900, 37020, 0)
    MoveCamera(30, 23, 0, 0)
    OP_6E(520, 0)
    SetCameraDistance(18000, 0)
    OP_0D()

    def lambda_303C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_303C)

    def lambda_304D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_304D)

    def lambda_305E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_305E)

    def lambda_306F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_306F)

    def lambda_3080():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_3080)

    def lambda_3091():
        OP_95(0xFE, -600, 0, 34200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3091)

    def lambda_30AB():
        OP_95(0xFE, 600, 0, 34200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_30AB)

    def lambda_30C5():
        OP_95(0xFE, 0, 0, 36000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_30C5)

    def lambda_30DF():
        OP_95(0xFE, -1200, 0, 33000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_30DF)

    def lambda_30F9():
        OP_95(0xFE, 1200, 0, 33000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_30F9)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x109, 1)
    WaitChrThread(0x105, 1)
    OP_4B(0xC, 0xFF)
    OP_4B(0xD, 0xFF)
    OP_63(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0xD, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0127
    ChrTalk(
        0xD,
        "哎呀，你们几个是……\x02",
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0xC,
        "哦哦，这不是兰道夫队长吗！？\x02",
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0xC,
        "哈哈，你今天也来啦。\x02",
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0x101,
        (
            "#6P#00001F（赤色星座的猎兵……\x01",
            "　看来还是兰迪认识的人呢。）\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0x104,
        (
            "#12P#00303F……扎克斯，看来你在新据点\x01",
            "待得很舒服嘛。\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0xC,
        "哈哈，托各位的福。\x02",
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0xC,
        (
            "欢乐街的『诺艾·布朗』分店离这里也很近，\x01",
            "所以真是相当便利呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0x104,
        (
            "#12P#00303F哈……你还是老样子，真辛苦啊。\x02\x03",

            "#00301F……叔叔他们今天又不在吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0xC,
        (
            "是的，老大和大小姐\x01",
            "出门办事了。\x02",
        )
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0xC,
        (
            "如果需要传话，\x01",
            "我可以代为转达。\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0x104,
        "#12P#00303F……不用了，打扰你了。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 500)

    #C0138
    ChrTalk(
        0x104,
        "#5P#00300F我们走吧，罗伊德。\x02",
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0x101,
        "#6P#00005F好、好的……\x02",
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0xD,
        "各位辛苦了。\x02",
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0xC,
        "呵呵，下次见啦，队长。\x02",
    )

    CloseMessageWindow()
    FadeToDark(500, 0, -1)
    OP_0D()
    SetChrFlags(0xC, 0x8)
    SetChrFlags(0xD, 0x8)
    OP_4B(0x9, 0xFF)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    OP_4B(0x8, 0xFF)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    SetChrPos(0x101, -760, 0, 930, 45)
    SetChrPos(0x102, 1220, 0, 930, 0)
    SetChrPos(0x104, 370, 0, 3760, 0)
    SetChrPos(0x109, 2170, 0, 2080, 315)
    SetChrPos(0x105, 3000, 0, 660, 315)
    OP_68(1930, 1850, 500, 0)
    MoveCamera(323, 19, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(12700, 0)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(300)

    #C0142
    ChrTalk(
        0x104,
        (
            "#00303F……哼，\x01",
            "又假装不在。\x02",
        )
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0x102,
        (
            "#12P#00105F『又』……？\x01",
            "你最近来过这里吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x104, 0xB4, 0x1F4)
    Sleep(300)

    #C0144
    ChrTalk(
        0x104,
        (
            "#00303F叔叔自己说有话要对我说，\x01",
            "结果却一直毫无音讯。\x02\x03",

            "#00301F看样子，\x01",
            "就算我主动来找他，\x01",
            "他也不打算露面。\x02",
        )
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0x105,
        (
            "#12P#10300F唔，说不定\x01",
            "在近期内就会\x01",
            "来找你了。\x02",
        )
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0x109,
        (
            "#11P#10106F这样一来……\x01",
            "要想调查赤色星座，就只能\x01",
            "老老实实地四处探查了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0x101,
        (
            "#6P#00000F那就在解决支援请求的同时，\x01",
            "去各地问问看吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 90, 0, 80, 180)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    OP_4C(0x8, 0xFF)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    OP_4C(0x9, 0xFF)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    SetScenarioFlags(0x14E, 3)
    EventEnd(0x5)
    Return()

    # Function_11_2EF2 end

    def Function_12_363D(): pass

    label("Function_12_363D")

    EventBegin(0x0)
    FadeToDark(500, 0, -1)
    OP_0D()
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x101, -400, 110, 43100, 0)
    SetChrPos(0x102, -950, 0, 41870, 0)
    SetChrPos(0x103, 1520, 0, 41870, 0)
    SetChrPos(0x104, 450, 0, 42540, 0)
    SetChrPos(0x109, 1020, 0, 39990, 0)
    SetChrPos(0x105, -400, 0, 40830, 0)
    OP_68(-100, 1950, 41030, 0)
    MoveCamera(359, 23, 0, 0)
    OP_6E(760, 0)
    SetCameraDistance(11000, 0)
    FadeToBright(2000, 0)
    OP_0D()
    Sound(807, 0, 100, 0)
    Sleep(300)

    #C0148
    ChrTalk(
        0x101,
        (
            "#00003F……门被锁上了呢。\x02\x03",

            "#00001F一科的搜查已经结束，\x01",
            "里面应该没有人了。\x02",
        )
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0x102,
        (
            "#00108F他们乘坐那艘飞艇逃跑之后，\x01",
            "现在到底潜伏在什么地方呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0x109,
        (
            "#12P#10101F警备队也在对他们\x01",
            "严加戒备。\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0x104,
        "#00303F……………………………………\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x104, 500)
    Sleep(50)

    #C0152
    ChrTalk(
        0x103,
        "#12P#00200F兰迪前辈……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 500)
    Sleep(50)
    TurnDirection(0x102, 0x104, 500)
    TurnDirection(0x105, 0x104, 500)
    TurnDirection(0x109, 0x104, 500)
    Sleep(50)

    #C0153
    ChrTalk(
        0x105,
        "#6P#10308F……你没事吧？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 500)
    Sleep(300)
    OP_93(0x104, 0xB4, 0x1F4)
    Sleep(500)

    #C0154
    ChrTalk(
        0x104,
        (
            "#00304F……哈哈，别担心。\x02\x03",

            "#00301F不过……下次再遇到他们的时候，\x01",
            "一定要做个彻底的了断。\x02",
        )
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0x101,
        "#00003F嗯……说的没错。\x02",
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, -100, 0, 41030, 180)
    SetScenarioFlags(0x18E, 1)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_12_363D end

    def Function_13_390E(): pass

    label("Function_13_390E")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x101, 0x8)
    SetChrFlags(0x102, 0x8)
    SetChrFlags(0x109, 0x8)
    SetChrFlags(0x105, 0x8)
    SoundLoad(468)
    ClearChrFlags(0x13, 0x80)
    OP_78(0x4, 0x13)
    OP_49()
    SetChrPos(0x13, 18000, 0, 500, 0)
    OP_D5(0x13, 0x0, 0x15F90, 0x0, 0x0)
    ClearMapObjFlags(0x4, 0x4)
    SetMapObjFlags(0x4, 0x1000)
    SetMapObjFrame(0x4, "light", 0x0, 0x1)
    OP_74(0x4, 0x1E)
    OP_71(0x4, 0x79, 0xB4, 0x1, 0x20)
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_39D2")
    SetChrFlags(0x9, 0x8000)
    SetChrFlags(0x8, 0x8000)
    EndChrThread(0x8, 0xFF)
    BeginChrThread(0x8, 0, 0, 0)
    SetChrPos(0x9, -8800, 0, 3100, 90)
    SetChrPos(0x8, -7300, 0, 3100, 270)

    label("loc_39D2")

    FadeToBright(1000, 0)
    BeginChrThread(0x13, 3, 0, 14)
    BeginChrThread(0x1D, 1, 0, 15)
    OP_68(-13800, 2750, 3000, 0)
    MoveCamera(57, 7, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(18000, 0)
    OP_68(-13800, 750, 3000, 7000)
    OP_6F(0x79)
    OP_0D()
    Sleep(1500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_24(0x1D4)
    SetScenarioFlags(0x22, 0)
    NewScene("c0400", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_13_390E end

    def Function_14_3A47(): pass

    label("Function_14_3A47")

    SetChrPos(0xFE, 18000, 0, 500, 0)
    OP_9F(0x0, 0xFE)
    OP_9F(0x1, -37000, 0, 500)
    OP_9F(0x2, 0xFE, 5000, 0x6)
    Return()

    # Function_14_3A47 end

    def Function_15_3A74(): pass

    label("Function_15_3A74")

    Sound(468, 2, 100, 0)
    Sound(458, 0, 60, 0)
    Sleep(1500)
    Sound(491, 0, 90, 0)
    Sleep(400)
    Sound(491, 0, 90, 0)
    Sleep(1100)
    Sound(459, 0, 100, 0)
    Sleep(2500)
    Sound(494, 0, 70, 0)
    StopSound(468, 1000, 100)
    Return()

    # Function_15_3A74 end

    def Function_16_3AAB(): pass

    label("Function_16_3AAB")

    EventBegin(0x0)
    SoundLoad(2753)
    SoundLoad(3834)
    SoundLoad(3941)
    Fade(500)
    OP_68(0, 1950, 3500, 0)
    MoveCamera(0, 10, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16500, 0)
    SetChrPos(0x101, -50, 0, 4650, 0)
    SetChrPos(0x102, -630, 0, 3570, 0)
    SetChrPos(0x109, 910, 0, 2930, 0)
    SetChrPos(0x105, 520, 0, 2260, 0)
    SetChrFlags(0x8, 0x80)
    OP_0D()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0156
    ChrTalk(
        0x101,
        "#00013F#6P（……！）\x02",
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0x102,
        "#00108F#6P（……啊……）\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    AddParty(0x3, 0xFF, 0xFF)
    LoadChrToIndex("chr/ch03300.itc", 0x1E)
    LoadChrToIndex("chr/ch03400.itc", 0x1F)
    LoadChrToIndex("chr/ch07400.itc", 0x20)
    LoadChrToIndex("apl/ch51114.itc", 0x21)
    LoadEffect(0x9, "map/mprain00.eff")
    PlayEffect(0x9, 0x7, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 1000)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis403.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu04601.itp")
    CreatePortrait(2, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu04500.itp")
    ClearMapObjFlags(0x2, 0x10)
    OP_32(0xFF, 0xFE, 0x0)
    OP_68(0, 2150, 37500, 0)
    MoveCamera(0, 22, 0, 0)
    OP_6E(760, 0)
    SetCameraDistance(19000, 0)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x8000)
    ClearChrFlags(0xF, 0x4)
    SetChrChipByIndex(0xF, 0x1E)
    SetChrPos(0xF, 300, 0, 41500, 180)
    OP_52(0xF, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x8000)
    ClearChrFlags(0x10, 0x4)
    SetChrChipByIndex(0x10, 0x1F)
    SetChrPos(0x10, -900, 0, 41600, 180)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x8000)
    ClearChrFlags(0x11, 0x4)
    SetChrChipByIndex(0x11, 0x20)
    SetChrPos(0x11, -3020, 0, 40750, 135)
    SetChrPos(0x104, -200, 0, 37500, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    PlayBGM("ed7561", 0)
    OP_25(0x80, 0x50)
    FadeToBright(1000, 0)
    SetCameraDistance(15000, 4500)
    OP_0D()
    OP_6F(0x79)
    Fade(500)
    OP_68(0, 850, 39710, 0)
    MoveCamera(1, 18, 0, 0)
    OP_6E(760, 0)
    SetCameraDistance(11100, 0)
    SetChrFlags(0x10, 0x2000)
    SetChrFlags(0xF, 0x2000)
    OP_0D()
    Sleep(300)
    OP_C9(0x0, 0x80000000)

    #C0158
    ChrTalk(
        0x104,
        "#00311F#2753V#6P#30W叔叔、谢莉。\x02",
    )

    CloseMessageWindow()
    OP_24(0xAC1)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(300)

    #A0159
    AnonymousTalk(
        0x10,
        (
            "#3941V#5P#20W啊哈哈，\x01",
            "好久不见啦，兰迪哥！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_24(0xF65)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    OP_CB(0x2, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x2, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    OP_CC(0x0, 0x2, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(300)

    #A0160
    AnonymousTalk(
        0xF,
        (
            "#3834V#11P#30W两年不见了，\x01",
            "你好像还是老样子啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_24(0xEFA)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x2, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x2, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    OP_CC(0x0, 0x2, 0x0)
    OP_C9(0x1, 0x80000000)
    ClearChrFlags(0x10, 0x2000)
    ClearChrFlags(0xF, 0x2000)
    SetChrPos(0x101, -50, 0, 30650, 0)
    SetChrPos(0x102, -630, 0, 29570, 0)
    SetChrPos(0x109, 910, 0, 28930, 0)
    SetChrPos(0x105, 420, 0, 28060, 0)
    SetChrPos(0x104, 0, 0, 37500, 0)
    OP_68(-240, 1350, 37560, 0)
    MoveCamera(325, 14, 0, 0)
    OP_6E(760, 0)
    SetCameraDistance(11830, 0)
    Fade(500)

    def lambda_3FC5():
        OP_9B(0x0, 0x101, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3FC5)
    Sleep(50)

    def lambda_3FDD():
        OP_9B(0x0, 0x102, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_3FDD)
    Sleep(50)

    def lambda_3FF5():
        OP_9B(0x0, 0x105, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_3FF5)
    Sleep(50)

    def lambda_400D():
        OP_9B(0x0, 0x109, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_400D)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x109, 0)
    OP_0D()

    #C0161
    ChrTalk(
        0x101,
        "#00007F#6P……兰迪……！\x02",
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0x109,
        "#10111F#6P#N是、是昨天那些人……！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0163
    ChrTalk(
        0x105,
        "#10303F#6P#N可疑人物齐聚一堂了呢。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0164
    ChrTalk(
        0x11,
        (
            "#03509F#5P哈哈，他果然是\x01",
            "这大叔的亲戚啊。\x02\x03",

            "#03502F因为发色一模一样，\x01",
            "我之前就有过这种猜测了～\x02",
        )
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0x104,
        "#00311F#6P……………………………………\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0x13B, 0x1F4)
    Sleep(150)

    #C0166
    ChrTalk(
        0x101,
        (
            "#00013F#6P雷克特大尉……\x01",
            "你为何会在这里？\x02",
        )
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0x102,
        (
            "#00101F#6P你与这次的交易\x01",
            "有什么关系吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0x11,
        (
            "#03504F#5P嗯，我只是做了点地下工作而已。\x02\x03",

            "#03510F哎呀呀～好不容易才领先了\x01",
            "黑月那个眼镜大哥一步。\x02",
        )
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0x10,
        (
            "#04609F#11P呵呵，真叫人期待呀。\x02\x03",

            "#04602F在东方人街的那次，我们因故撤退了，\x01",
            "但这次似乎可以尽情玩一场了呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x0, 0x1F4)
    Sleep(100)

    #C0170
    ChrTalk(
        0x101,
        "#00005F#6P东方人街……\x02",
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0x104,
        (
            "#00303F#6P就是你们去年在卡尔瓦德\x01",
            "和黑月掀起的那场『战争』吗？\x02\x03",

            "#00311F回答我，叔叔，\x01",
            "你们为什么会到克洛斯贝尔来？\x02\x03",

            "到底想做什么？\x02",
        )
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0xF,
        (
            "#04504F#11P呵呵……\x01",
            "这还用问？当然是为了生意啊。\x02\x03",

            "#04500F先不说这些了，兰道夫，\x01",
            "我有件事要告诉你。\x02\x03",

            "大哥死了。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0173
    ChrTalk(
        0x104,
        "#00305F#6P#40W#2S………什么………………\x02",
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0x101,
        "#00011F#6P！？\x02",
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0xF,
        (
            "#04503F#11P大约在半年之前……\x02\x03",

            "他和『西风』的老大同归于尽了。\x02",
        )
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0x10,
        (
            "#04602F#11P多年宿敌──\x01",
            "『斗神』和『猎兵王』的对决！\x02\x03",

            "#04612F哎呀，真是太震撼了！\x02",
        )
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0x104,
        (
            "#00308F#6P#40W…………………………………\x02\x03",

            "#00304F#40W……哈哈……是吗……\x02\x03",

            "#30W那个混账老爸……\x01",
            "至死都在战斗着啊。\x02\x03",

            "#00300F#40W……他肯定很满足吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0x10,
        (
            "#04602F#11P嗯！\x01",
            "看起来好像很快乐呢！\x02\x03",

            "#04606F真羡慕呀，谢莉也\x01",
            "想要个那样的对手～\x02",
        )
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0xF,
        (
            "#04504F#11P总之，大哥并没有留下什么遗憾。\x02\x03",

            "#04501F除了烦心于某个\x01",
            "尚在迷茫的不肖子之外。\x02",
        )
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0x104,
        "#00301F#6P……！\x02",
    )

    CloseMessageWindow()
    OP_93(0xF, 0x0, 0x1F4)
    Sleep(300)

    #C0181
    ChrTalk(
        0xF,
        (
            "#04504F#5P你的休假结束了，兰道夫。\x02\x03",

            "#04502F改日我还有话要和你谈谈，\x01",
            "在那之前，就做好心理准备吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0182
    ChrTalk(
        0x10,
        "#04609F#11P回头见啦～兰迪哥！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0183
    ChrTalk(
        0x11,
        "#03509F#5P那就先这样，各位辛苦了～\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0xF, 0, 0, 17)
    BeginChrThread(0x10, 0, 0, 19)
    BeginChrThread(0x11, 0, 0, 21)
    WaitChrThread(0xF, 0)
    WaitChrThread(0x10, 0)
    WaitChrThread(0x11, 0)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    Sleep(500)
    Fade(500)
    OP_68(-680, 1150, 38230, 0)
    MoveCamera(328, 13, 0, 0)
    OP_6E(760, 0)
    SetCameraDistance(11000, 0)
    OP_0D()
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_6F(0x79)

    #C0184
    ChrTalk(
        0x102,
        "#00108F#6P#N……兰迪……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0185
    ChrTalk(
        0x109,
        "#10113F#6P#N兰迪前辈……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0186
    ChrTalk(
        0x101,
        "#00008F#6P那两个人是兰迪的……？\x02",
    )

    CloseMessageWindow()
    OP_64(0x104)
    Sleep(500)

    #C0187
    ChrTalk(
        0x104,
        "#00306F#5P#30W没错……\x02",
    )

    CloseMessageWindow()
    OP_93(0x104, 0xB4, 0x190)
    Sleep(150)
    Fade(250)
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x104, 0x0)
    SetChrFlags(0x104, 0x2)
    SetChrFlags(0x104, 0x20)
    OP_0D()
    Sleep(500)

    #C0188
    ChrTalk(
        0x104,
        (
            "#00303F#11P#30W『赤色星座』副团长，\x01",
            "西格蒙德·奥兰多。\x02\x03",

            "以及他的女儿兼队长之一，\x01",
            "谢莉·奥兰多。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    SetChrSubChip(0x104, 0x1)
    Sleep(150)
    ClearChrFlags(0x104, 0x2)
    ClearChrFlags(0x104, 0x20)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    Sleep(350)

    #C0189
    ChrTalk(
        0x104,
        (
            "#00311F#11P#30W是我的叔叔和堂妹……\x01",
            "也是两个最强最凶恶的战鬼。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    MoveCamera(330, 22, 0, 0)
    MoveCamera(333, 30, 0, 4500)
    SetCameraDistance(14500, 4500)
    FadeToDark(0, 16777215, -1)
    FadeToBright(2000, 16777215)
    Sound(896, 0, 100, 0)
    Sleep(1000)
    Sound(966, 0, 70, 0)
    Sleep(1000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    StopBGM(0x1388)
    Sleep(2000)
    StopSound(128, 2000, 80)
    WaitBGM()
    OP_29(0xA2, 0x1, 0x6)
    OP_29(0xA1, 0x4, 0x10)
    OP_29(0xA2, 0x4, 0x10)
    SetScenarioFlags(0x20B, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x67, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_4923")
    Jump("loc_4928")

    label("loc_4923")

    OP_29(0x67, 0x4, 0x40)

    label("loc_4928")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6D, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_4939")
    Jump("loc_493E")

    label("loc_4939")

    OP_29(0x6D, 0x4, 0x40)

    label("loc_493E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6E, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_494F")
    Jump("loc_4954")

    label("loc_494F")

    OP_29(0x6E, 0x4, 0x40)

    label("loc_4954")

    OP_E5(0xA)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_57(0x3)
    OP_E5(0x3)
    Sleep(100)
    MiniGame(0x2B, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_E0(0x1D, 0x0)
    Sleep(100)
    OP_68(-1000000, 0, 0, 0)
    OP_C9(0x0, 0x10)
    OP_C9(0x0, 0x10000)
    SetScenarioFlags(0x25, 0)
    OP_50(0x50, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_50(0x31, (scpexpr(EXPR_PUSH_LONG, 0x97), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ShowSaveMenu()
    ClearScenarioFlags(0x25, 0)
    MiniGame(0x2B, 0x1, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    SetMapObjFlags(0x2, 0x10)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_49()
    OP_CC(0x1, 0xFF, 0x0)
    OP_C9(0x1, 0x10)
    OP_E5(0xB)
    OP_CC(0x1, 0xFF, 0x0)
    OP_50(0x4, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x22, 0)
    NewScene("c1500", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_16_3AAB end

    def Function_17_4A38(): pass

    label("Function_17_4A38")

    OP_95(0xFE, 0, 0, 42270, 2000, 0x0)
    OP_95(0xFE, 0, 300, 43640, 2000, 0x0)
    Sound(103, 0, 100, 0)
    OP_71(0x2, 0x1, 0xA, 0x1, 0x0)
    Sleep(500)

    def lambda_4A7A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4A7A)
    OP_9B(0x0, 0xFE, 0x0, 0x9C4, 0x7D0, 0x0)
    Return()

    # Function_17_4A38 end

    def Function_18_4A96(): pass

    label("Function_18_4A96")

    Return()

    # Function_18_4A96 end

    def Function_19_4A97(): pass

    label("Function_19_4A97")

    Sleep(1500)
    OP_93(0xFE, 0x2D, 0x1F4)
    Sleep(500)
    OP_95(0xFE, 0, 0, 42270, 2000, 0x0)
    OP_95(0xFE, 0, 300, 43640, 2000, 0x0)

    def lambda_4AD1():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4AD1)
    OP_9B(0x0, 0xFE, 0x0, 0x9C4, 0x7D0, 0x0)
    Return()

    # Function_19_4A97 end

    def Function_20_4AED(): pass

    label("Function_20_4AED")

    Return()

    # Function_20_4AED end

    def Function_21_4AEE(): pass

    label("Function_21_4AEE")

    Sleep(2000)
    OP_93(0xFE, 0x2D, 0x1F4)
    OP_95(0xFE, 0, 0, 42270, 2000, 0x0)
    OP_95(0xFE, 0, 300, 43640, 2000, 0x0)

    def lambda_4B25():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4B25)
    OP_9B(0x0, 0xFE, 0x0, 0x9C4, 0x7D0, 0x0)
    Sound(104, 0, 100, 0)
    OP_71(0x2, 0xA, 0x0, 0x1, 0x0)
    Return()

    # Function_21_4AEE end

    def Function_22_4B53(): pass

    label("Function_22_4B53")

    Return()

    # Function_22_4B53 end

    def Function_23_4B54(): pass

    label("Function_23_4B54")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SoundLoad(3973)
    SoundLoad(3974)
    LoadChrToIndex("chr/ch03300.itc", 0x1E)
    LoadChrToIndex("chr/ch03400.itc", 0x1F)
    LoadChrToIndex("chr/ch03401.itc", 0x20)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x8000)
    SetChrChipByIndex(0xF, 0x1E)
    SetChrSubChip(0xF, 0x0)
    SetChrPos(0xF, -3800, 6500, 7700, 20)
    OP_8E(0xF, "西格蒙德")
    OP_52(0xF, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x8000)
    SetChrChipByIndex(0x10, 0x1F)
    SetChrSubChip(0x10, 0x0)
    SetChrPos(0x10, -2500, 6500, 8100, 20)
    OP_8E(0x10, "谢莉")
    OP_52(0x10, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x12, 0x8000)
    SetChrChipByIndex(0x12, 0x5)
    SetChrSubChip(0x12, 0x0)
    SetChrPos(0x12, -2800, 6500, 5900, 20)
    OP_52(0x12, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8000)
    SetChrChipByIndex(0xC, 0x4)
    SetChrSubChip(0xC, 0x0)
    SetChrPos(0xC, -4500, 6500, 5900, 20)
    OP_4B(0xC, 0xFF)
    OP_52(0xC, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_68(-3100, 7700, 7000, 0)
    MoveCamera(348, 17, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16540, 0)
    VolumeBGM(0x5A, 0x3E8)
    SetCameraDistance(14540, 3000)
    FadeToBright(2000, 0)
    Sleep(2500)
    OP_63(0x10, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Sleep(1000)
    OP_C9(0x0, 0x80000000)

    #C0190
    ChrTalk(
        0x10,
        (
            "#04602F#3973V#5P#30W呜哇～！\x01",
            "那栋大楼可真不得了啊～！\x02\x03",

            "#04612F#3974V我说，能不能让我带人\x01",
            "把它彻底破坏掉！？\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xF86)
    OP_C9(0x1, 0x80000000)
    TurnDirection(0xF, 0x10, 500)
    Sleep(300)

    #C0191
    ChrTalk(
        0xF,
        (
            "#04504F#5P呵呵……虽然能理解\x01",
            "你的心情，但还是不要那么做了。\x02\x03",

            "#04500F不久之后，我们还要\x01",
            "用到那栋大楼呢。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10, 0xF, 500)

    #C0192
    ChrTalk(
        0x10,
        (
            "#04606F#11P唔……真遗憾。\x02\x03",

            "#04602F算啦，\x01",
            "那我就去街上逛逛吧。\x02\x03",

            "#04612F受那栋大楼的影响，\x01",
            "整座城市的气氛好像都沸腾起来了呢¤\x02",
        )
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0xF,
        "#04504F#5P嗯，你去吧。\x02",
    )

    CloseMessageWindow()
    OP_68(-2220, 7700, 6340, 1500)
    MoveCamera(346, 20, 0, 1500)
    OP_6E(600, 1500)
    SetCameraDistance(14540, 1500)
    OP_92(0x10, 0x0, 0x1DB0, 0x1F4)
    Sound(809, 0, 50, 0)
    SetChrChipByIndex(0x10, 0x20)
    SetChrSubChip(0x10, 0x1)

    def lambda_4ED7():
        OP_9D(0xFE, 0x0, 0x1450, 0x1DB0, 0x1F4, 0x7D0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_4ED7)
    Sleep(300)

    def lambda_4EF7():

        label("loc_4EF7")

        TurnDirection(0xFE, 0x10, 500)
        Yield()
        Jump("loc_4EF7")

    QueueWorkItem2(0xF, 2, lambda_4EF7)

    def lambda_4F09():

        label("loc_4F09")

        TurnDirection(0xFE, 0x10, 500)
        Yield()
        Jump("loc_4F09")

    QueueWorkItem2(0x12, 2, lambda_4F09)

    def lambda_4F1B():

        label("loc_4F1B")

        TurnDirection(0xFE, 0x10, 500)
        Yield()
        Jump("loc_4F1B")

    QueueWorkItem2(0xC, 2, lambda_4F1B)
    WaitChrThread(0x10, 1)
    Sound(62, 0, 100, 0)
    OP_92(0x10, 0x0, 0x1004, 0x1F4)

    def lambda_4F44():
        OP_98(0xFE, 0x0, 0x0, 0xFFFFFC18, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_4F44)
    WaitChrThread(0x10, 1)
    Sound(844, 0, 50, 0)
    SetChrSubChip(0x10, 0x2)

    def lambda_4F6C():
        OP_9D(0xFE, 0x0, 0x0, 0xE10, 0x1F4, 0x7D0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_4F6C)
    WaitChrThread(0x10, 1)
    EndChrThread(0xF, 0x2)
    EndChrThread(0x12, 0x2)
    EndChrThread(0xC, 0x2)
    SetChrFlags(0x10, 0x80)
    Sleep(300)

    #C0194
    ChrTalk(
        0xC,
        "#5P哈哈……真不愧是大小姐啊。\x02",
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0xC,
        (
            "#5P看来她很中意\x01",
            "那栋大楼呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0xF,
        (
            "#04504F#5P呵呵，也有这个原因吧。\x02\x03",

            "#04502F但更重要的是──\x01",
            "她已经沉醉于对鲜血的期待了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0xF, 500)

    #C0197
    ChrTalk(
        0xC,
        "#6P……！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x12, 0xF, 500)

    #C0198
    ChrTalk(
        0x12,
        (
            "#12P……原来如此，\x01",
            "真有谢莉大小姐的作风呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_68(-2660, 7700, 8140, 1500)
    MoveCamera(345, 17, 0, 1500)
    OP_6E(600, 1500)
    SetCameraDistance(14500, 1500)
    OP_93(0xF, 0x14, 0x12C)
    OP_6F(0x79)

    #C0199
    ChrTalk(
        0xF,
        (
            "#04504F#5P呵呵……不愧是我的女儿。\x02\x03",

            "#04502F看来她明天也能\x01",
            "好好享受一番呢。\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(15000, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    SetScenarioFlags(0x22, 1)
    NewScene("m0101", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_23_4B54 end

    def Function_24_5135(): pass

    label("Function_24_5135")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x8, 0x8)
    SetChrFlags(0x9, 0x8)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    OP_68(20160, 1950, 650, 0)
    MoveCamera(23, 10, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16500, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x101, 21160, 0, 650, 270)
    SetChrPos(0x102, 22560, 0, -410, 270)
    SetChrPos(0x103, 23560, 0, 2050, 270)
    SetChrPos(0x104, 24160, 0, -760, 270)
    SetChrPos(0x109, 25160, 0, 1120, 270)
    SetChrPos(0x105, 26260, 0, 250, 270)
    OP_68(360, 1950, 3660, 4800)
    MoveCamera(344, 10, 0, 3000)
    OP_6E(600, 4000)
    SetCameraDistance(16500, 4000)
    BeginChrThread(0x101, 3, 0, 25)
    BeginChrThread(0x102, 3, 0, 25)
    BeginChrThread(0x103, 3, 0, 25)
    BeginChrThread(0x104, 3, 0, 25)
    BeginChrThread(0x109, 3, 0, 25)
    BeginChrThread(0x105, 3, 0, 25)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x1)
    EndChrThread(0x101, 0x3)
    EndChrThread(0x102, 0x3)
    EndChrThread(0x103, 0x3)
    EndChrThread(0x104, 0x3)
    EndChrThread(0x109, 0x3)
    EndChrThread(0x105, 0x3)
    Fade(500)
    OP_68(210, 1950, 34660, 0)
    MoveCamera(0, 39, 0, 0)
    OP_6E(760, 0)
    SetCameraDistance(13640, 0)
    SetChrPos(0x101, 0, 0, 33570, 0)
    SetChrPos(0x102, -760, 0, 32800, 0)
    SetChrPos(0x103, 940, 0, 32549, 0)
    SetChrPos(0x104, 140, 0, 31650, 0)
    SetChrPos(0x109, 1450, 0, 31370, 0)
    SetChrPos(0x105, -1150, 0, 31220, 0)

    def lambda_5311():
        OP_95(0xFE, 10, 0, 39370, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5311)
    Sleep(30)

    def lambda_532E():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_532E)
    Sleep(30)

    def lambda_5346():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5346)
    Sleep(50)

    def lambda_535E():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_535E)
    Sleep(30)

    def lambda_5376():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_5376)

    def lambda_538B():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_538B)
    OP_68(320, 1950, 40090, 6000)
    MoveCamera(9, 40, 0, 5000)
    OP_6E(760, 5000)
    SetCameraDistance(11370, 5000)
    WaitChrThread(0x101, 1)
    OP_4B(0xA, 0xFF)
    OP_4B(0xB, 0xFF)
    Sleep(200)
    TurnDirection(0x101, 0xA, 500)
    TurnDirection(0xA, 0x101, 500)
    Sleep(600)
    OP_93(0x101, 0x3C, 0x1F4)
    TurnDirection(0xB, 0x101, 500)
    Sleep(600)
    OP_93(0x101, 0x0, 0x1F4)
    Sleep(300)

    def lambda_5409():
        OP_95(0xFE, 10, 0, 43000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5409)
    Sleep(400)
    BeginChrThread(0x102, 3, 0, 26)
    Sleep(600)
    BeginChrThread(0x103, 3, 0, 26)
    OP_93(0xA, 0xB4, 0x1F4)
    Sleep(200)
    OP_93(0xB, 0xB4, 0x1F4)
    Sleep(200)
    BeginChrThread(0x104, 3, 0, 26)
    WaitChrThread(0x101, 1)
    Sleep(150)
    Sound(103, 0, 100, 0)
    ClearMapObjFlags(0x2, 0x10)
    OP_71(0x2, 0x0, 0xA, 0x0, 0x0)

    def lambda_546E():
        OP_95(0xFE, 0, 0, 45000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_546E)

    def lambda_5488():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5488)
    Sleep(100)
    BeginChrThread(0x109, 3, 0, 26)
    Sleep(700)
    BeginChrThread(0x105, 3, 0, 26)
    OP_68(-120, 1950, 43100, 5000)
    MoveCamera(9, 43, 0, 5000)
    OP_6E(760, 5000)
    SetCameraDistance(19370, 5000)
    Sleep(2000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x22, 0)
    NewScene("c0510", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_24_5135 end

    def Function_25_54FE(): pass

    label("Function_25_54FE")

    OP_95(0xFE, 0, 0, 650, 5000, 0x0)
    OP_95(0xFE, 0, 0, 6000, 5000, 0x0)
    Return()

    # Function_25_54FE end

    def Function_26_5527(): pass

    label("Function_26_5527")


    def lambda_552C():
        OP_95(0xFE, 0, 0, 39370, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_552C)
    WaitChrThread(0xFE, 1)

    def lambda_554A():
        OP_95(0xFE, 0, 0, 43670, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_554A)
    WaitChrThread(0xFE, 1)

    def lambda_5568():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_5568)

    def lambda_5579():
        OP_95(0xFE, 0, 0, 45000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5579)
    Return()

    # Function_26_5527 end

    def Function_27_558F(): pass

    label("Function_27_558F")

    EventBegin(0x0)
    Fade(1000)
    OP_68(0, 900, 40500, 0)
    MoveCamera(0, 23, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(22000, 0)
    OP_F0(0x0, 0x5)
    SetChrPos(0x101, -600, 0, 34200, 0)
    SetChrPos(0x102, 600, 0, 34200, 0)
    SetChrPos(0x103, -1200, 0, 33000, 0)
    SetChrPos(0x104, 1200, 0, 33000, 0)
    OP_68(0, 900, 35500, 4000)
    SetCameraDistance(20000, 4000)
    OP_0D()
    OP_6F(0x1)

    #C0200
    ChrTalk(
        0x101,
        (
            "#00001F#5P看样子……\x01",
            "好像已经没人了。\x02",
        )
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0x103,
        (
            "#00208F#6P警察在离开之前，\x01",
            "应该给大门上过锁的。\x02",
        )
    )

    CloseMessageWindow()

    #C0202
    ChrTalk(
        0x104,
        (
            "#00301F#12P特地叫我们到这里来，\x01",
            "而且还替我们撬了锁吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0203
    ChrTalk(
        0x102,
        "#00103F#11P总之，我们进去吧。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, 0, 0, 34000, 0)
    OP_69(0xFF, 0x0)
    SetScenarioFlags(0x182, 3)
    EventEnd(0x5)
    Return()

    # Function_27_558F end

    def Function_28_5706(): pass

    label("Function_28_5706")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    LoadChrToIndex("chr/ch06000.itc", 0x1E)
    LoadChrToIndex("chr/ch06300.itc", 0x20)
    LoadChrToIndex("chr/ch31400.itc", 0x21)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu02100.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu03200.itp")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    EndChrThread(0x8, 0x0)
    SetChrChipByIndex(0x14, 0x1E)
    SetChrSubChip(0x14, 0x0)
    ClearChrFlags(0x14, 0x80)
    SetChrFlags(0x14, 0x8000)
    SetChrPos(0x14, 0, 0, 3460, 0)
    OP_68(60, 1950, 1170, 0)
    MoveCamera(0, 10, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(9020, 0)
    OP_0D()
    SetChrPos(0x101, 5800, 0, 1000, 270)
    SetChrPos(0x102, 5000, 0, 0, 270)
    SetChrPos(0x109, 7000, 0, 740, 270)
    SetChrPos(0x105, 6200, 0, -260, 270)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(300)

    #C0204
    ChrTalk(
        0x14,
        (
            "#02101F嗯……\x01",
            "终于开始行动了啊。\x02\x03",

            "#02103F只是交涉而已的话，\x01",
            "就算写进报道应该也没问题吧？\x02\x03",

            "#02101F反正共和国派施加的压力\x01",
            "在最近已经有所减弱了……\x02",
        )
    )

    CloseMessageWindow()
    Fade(1000)
    OP_68(4410, 1950, 40, 0)
    MoveCamera(316, 23, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(12090, 0)
    OP_0D()

    #C0205
    ChrTalk(
        0x101,
        (
            "#00005F格蕾丝小姐，\x01",
            "您在做什么呢？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x14, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_68(1680, 1950, 600, 3000)
    MoveCamera(312, 19, 0, 3000)
    OP_6E(600, 3000)
    SetCameraDistance(11520, 3000)

    def lambda_596C():
        OP_93(0x14, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_596C)

    def lambda_5979():
        OP_95(0x101, 850, 0, 1360, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5979)
    Sleep(100)

    def lambda_5996():
        OP_9B(0x0, 0x102, 0x0, 0x1388, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5996)
    Sleep(100)

    def lambda_59AE():
        OP_95(0x105, 0, 0, 360, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_59AE)
    Sleep(100)

    def lambda_59CB():
        OP_9B(0x0, 0x109, 0x0, 0x1194, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_59CB)
    WaitChrThread(0x109, 1)

    def lambda_59E4():
        OP_95(0x109, 1300, 0, 260, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_59E4)
    Sleep(100)
    OP_6F(0x79)
    WaitChrThread(0x102, 1)

    def lambda_5A07():
        OP_95(0x102, -600, 0, 1560, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5A07)
    WaitChrThread(0x101, 1)

    def lambda_5A25():
        TurnDirection(0x101, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5A25)

    def lambda_5A32():
        OP_93(0x14, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_5A32)
    WaitChrThread(0x109, 1)

    def lambda_5A43():
        TurnDirection(0x109, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_5A43)
    Sleep(200)
    WaitChrThread(0x105, 1)

    def lambda_5A57():
        TurnDirection(0x105, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_5A57)
    Sleep(200)
    WaitChrThread(0x102, 1)

    def lambda_5A6B():
        TurnDirection(0x102, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5A6B)
    WaitChrThread(0x105, 1)
    Call(0, 30)
    Return()

    # Function_28_5706 end

    def Function_29_5A7B(): pass

    label("Function_29_5A7B")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    LoadChrToIndex("chr/ch06000.itc", 0x1E)
    LoadChrToIndex("chr/ch06300.itc", 0x20)
    LoadChrToIndex("chr/ch31400.itc", 0x21)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu02100.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu03200.itp")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    EndChrThread(0x8, 0x0)
    SetChrChipByIndex(0x14, 0x1E)
    SetChrSubChip(0x14, 0x0)
    ClearChrFlags(0x14, 0x80)
    SetChrFlags(0x14, 0x8000)
    SetChrPos(0x14, 0, 0, 3460, 0)
    OP_68(60, 1950, 1170, 0)
    MoveCamera(0, 10, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(9020, 0)
    OP_0D()
    SetChrPos(0x101, -5120, 0, 1430, 90)
    SetChrPos(0x102, -6740, 0, 1310, 90)
    SetChrPos(0x109, -6070, 0, 120, 90)
    SetChrPos(0x105, -8320, 0, 280, 90)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(300)

    #C0206
    ChrTalk(
        0x14,
        (
            "#12P#02101F嗯……\x01",
            "终于开始行动了啊。\x02\x03",

            "#02103F只是交涉而已的话，\x01",
            "就算写进报道应该也没问题吧？\x02\x03",

            "#02101F反正共和国派施加的压力\x01",
            "在最近已经有所减弱了……\x02",
        )
    )

    CloseMessageWindow()
    Fade(1000)
    OP_68(250, 1950, 420, 0)
    MoveCamera(305, 13, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(9020, 0)
    OP_0D()

    #C0207
    ChrTalk(
        0x101,
        (
            "#00005F格蕾丝小姐，\x01",
            "您在做什么呢？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x14, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_68(1680, 1950, 600, 3000)
    MoveCamera(312, 19, 0, 3000)
    OP_6E(600, 3000)
    SetCameraDistance(11520, 3000)

    def lambda_5CE5():
        TurnDirection(0x14, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_5CE5)

    def lambda_5CF2():
        OP_95(0x101, 850, 0, 1360, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5CF2)
    Sleep(100)

    def lambda_5D0F():
        OP_95(0x102, -600, 0, 1560, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5D0F)
    Sleep(100)

    def lambda_5D2C():
        OP_95(0x109, 1300, 0, 260, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_5D2C)
    Sleep(100)

    def lambda_5D49():
        OP_95(0x105, 0, 0, 360, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_5D49)
    Sleep(1000)

    def lambda_5D66():
        OP_93(0x14, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_5D66)
    OP_6F(0x79)
    WaitChrThread(0x101, 1)

    def lambda_5D79():
        TurnDirection(0x101, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5D79)

    def lambda_5D86():
        OP_93(0x14, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_5D86)
    WaitChrThread(0x102, 1)

    def lambda_5D97():
        TurnDirection(0x102, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5D97)
    WaitChrThread(0x109, 1)

    def lambda_5DA8():
        TurnDirection(0x109, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_5DA8)
    WaitChrThread(0x105, 1)

    def lambda_5DB9():
        TurnDirection(0x105, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_5DB9)
    WaitChrThread(0x105, 1)
    Call(0, 30)
    Return()

    # Function_29_5A7B end

    def Function_30_5DC9(): pass

    label("Function_30_5DC9")

    Sleep(100)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0208
    AnonymousTalk(
        0x14,
        (
            "什、什么嘛……\x01",
            "是你们啊。\x02\x03",

            "原来如此，特别任务支援科\x01",
            "终于重新恢复工作了啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    #C0209
    ChrTalk(
        0x101,
        "#6P#00000F是的，托您的福。\x02",
    )

    CloseMessageWindow()

    #C0210
    ChrTalk(
        0x102,
        (
            "#6P#00100F不过缇欧和兰迪还要\x01",
            "再过一段时间才能归队。\x02",
        )
    )

    CloseMessageWindow()

    #C0211
    ChrTalk(
        0x14,
        (
            "#02100F是吗，那还真有点遗憾呢。\x02\x03",

            "#02106F话说回来，真没想到瓦吉\x01",
            "会加入支援科啊～\x02\x03",

            "#02102F连姐姐我都大吃一惊呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0212
    ChrTalk(
        0x105,
        (
            "#6P#10300F呵呵，能让你吃惊，真是倍感荣幸。\x02\x03",

            "#10304F如果愿意，就算把这件事情\x01",
            "写进特辑报道，我也不会介意哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0213
    ChrTalk(
        0x101,
        "#11P#00006F我说你啊……\x02",
    )

    CloseMessageWindow()
    OP_93(0x14, 0xB4, 0x0)

    #C0214
    ChrTalk(
        0x14,
        (
            "#02109F呵呵，你们相处得很不错嘛。\x02\x03",

            "#02106F本想和你们好好聊聊，\x01",
            "可惜现在有点忙。\x02\x03",

            "#02102F等我的事情忙完了，再跟你们慢慢——\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0xBB8)
    SetChrChipByIndex(0x15, 0x20)
    SetChrSubChip(0x15, 0x0)
    ClearChrFlags(0x15, 0x80)
    SetChrFlags(0x15, 0x8000)
    SetChrPos(0x15, 2490, 0, 32509, 180)

    #N0215
    NpcTalk(
        0x15,
        "青年的声音",
        "#N哎呀，真是难得一见的面孔。\x02",
    )

    CloseMessageWindow()
    OP_63(0x14, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(500)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7114", 0)
    Fade(500)
    OP_68(0, 1950, 4810, 0)
    MoveCamera(0, 19, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(8890, 0)
    SetChrPos(0x15, 0, 0, 10350, 180)
    OP_93(0x14, 0x168, 0x0)
    SetChrChipByIndex(0x16, 0x21)
    SetChrSubChip(0x16, 0x0)
    ClearChrFlags(0x16, 0x80)
    SetChrFlags(0x16, 0x8000)
    SetChrPos(0x16, -750, 0, 11350, 180)

    def lambda_61C8():
        OP_98(0x15, 0x0, 0x0, 0xFFFFFC18, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_61C8)
    Sleep(50)

    def lambda_61E5():
        OP_98(0x16, 0x0, 0x0, 0xFFFFFC18, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_61E5)
    Sleep(50)
    OP_0D()

    #C0216
    ChrTalk(
        0x101,
        "#12P#N#00005F啊……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0217
    ChrTalk(
        0x102,
        "#3P#N#00101F曹先生……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0218
    ChrTalk(
        0x14,
        "#12P#N#02106F……糟糕。\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    OP_68(1580, 1750, 1260, 0)
    MoveCamera(315, 22, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(12350, 0)
    SetChrPos(0x15, 1000, 0, 3350, 180)
    SetChrPos(0x16, 750, 0, 4350, 180)
    SetChrPos(0x14, -1000, 0, 3460, 90)
    OP_93(0x101, 0x0, 0x0)
    OP_93(0x102, 0x2D, 0x0)
    OP_93(0x109, 0x0, 0x0)
    OP_93(0x105, 0x2D, 0x0)
    OP_0D()
    Sleep(100)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0219
    AnonymousTalk(
        0x15,
        (
            "好久不见了，\x01",
            "罗伊德警官，艾莉小姐。\x02\x03",

            "还有……瓦吉先生和\x01",
            "诺艾尔上士，没错吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0220
    ChrTalk(
        0x109,
        "#6P#10111F你、你为何会知道……！\x02",
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0x105,
        (
            "#6P#10302F哦……？\x01",
            "很厉害的情报网啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0222
    ChrTalk(
        0x15,
        (
            "#03204F呵呵，毕竟是关系到\x01",
            "特别任务支援科的事情嘛。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x15, 0x10E, 0x1F4)

    #C0223
    ChrTalk(
        0x15,
        (
            "#03200F话说回来，真没想到格蕾丝小姐\x01",
            "能掌握到我们的行动。\x02\x03",

            "#03209F不愧是天下闻名的\x01",
            "克洛斯贝尔时代周刊呀。\x02",
        )
    )

    CloseMessageWindow()

    #C0224
    ChrTalk(
        0x14,
        (
            "#5P#02109F哪、哪有的事～\x01",
            "这只是偶然啦，偶然！\x02",
        )
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0x101,
        (
            "#6P#00001F……请问，您为何会到\x01",
            "这种地方来？\x02",
        )
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0x102,
        (
            "#6P#00101F专程来鲁巴彻的旧址，\x01",
            "有什么事情吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x15, 0xB4, 0x1F4)

    #C0227
    ChrTalk(
        0x15,
        (
            "#03200F哈哈，这还用问吗？\x02\x03",

            "#03204F如果放任这片土地荒废下去，\x01",
            "未免也太过浪费了。\x02\x03",

            "#03202F既然如此，何不由敝公司\x01",
            "将其有效利用？\x02",
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
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0228
    ChrTalk(
        0x101,
        "#6P#00001F……！\x02",
    )

    CloseMessageWindow()

    #C0229
    ChrTalk(
        0x15,
        (
            "#03203F呵呵，普通人恐怕也不敢\x01",
            "轻易接手这种黑手党的地产。\x02\x03",

            "#03210F但我们却已经习惯\x01",
            "处理这类地产了。\x02\x03",

            "#03204F另外，负责管理此地的房产经营者也因\x01",
            "每个月的管理费而头痛不已，\x01",
            "此次交易想必会相当顺利。\x02",
        )
    )

    CloseMessageWindow()

    #C0230
    ChrTalk(
        0x101,
        "#6P#00010F这……\x02",
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0x14,
        (
            "#5P#02101F……打扰一下，曹先生，\x01",
            "请问我可以把这些消息写入报道吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0232
    ChrTalk(
        0x15,
        (
            "#03200F哦，当然没问题，\x01",
            "这又不是什么见不得人的事情。\x02\x03",

            "#03204F不过，请不要仅凭臆测就在\x01",
            "报道中对我们横加论断哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0233
    ChrTalk(
        0x14,
        (
            "#5P#02109F啊、啊哈哈……\x01",
            "这些事情我自然明白。\x02",
        )
    )

    CloseMessageWindow()

    #C0234
    ChrTalk(
        0x15,
        (
            "#03200F呵呵，那我就告辞了。\x02\x03",

            "罗伊德警官，如果有什么事，\x01",
            "随时可以到敝公司来。\x02\x03",

            "#03204F……走吧，刘。\x02",
        )
    )

    CloseMessageWindow()

    #C0235
    ChrTalk(
        0x16,
        "是。\x02",
    )

    CloseMessageWindow()
    OP_93(0x102, 0x0, 0x0)

    def lambda_68FA():
        OP_9B(0x1, 0x101, 0xB4, 0x1F4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_68FA)
    Sleep(50)

    def lambda_6912():
        OP_9B(0x1, 0x102, 0xB4, 0x1F4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6912)

    def lambda_6927():
        OP_9B(0x1, 0x109, 0xB4, 0x1F4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_6927)
    Sleep(50)

    def lambda_693F():
        OP_9B(0x1, 0x105, 0xB4, 0x1F4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_693F)
    Sleep(50)

    def lambda_6957():
        OP_95(0x15, -2500, 0, 1660, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_6957)
    Sleep(500)
    OP_96(0x16, 0x0, 0x0, 0x898, 0x7D0, 0x0)

    def lambda_6988():
        OP_95(0x15, -12000, 0, 1660, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_6988)

    def lambda_69A2():
        OP_95(0x16, -12000, 0, 1560, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_69A2)

    def lambda_69BC():
        OP_93(0x101, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_69BC)
    Sleep(50)

    def lambda_69CC():
        OP_93(0x102, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_69CC)
    Sleep(50)

    def lambda_69DC():
        OP_93(0x109, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_69DC)
    Sleep(50)

    def lambda_69EC():
        OP_93(0x105, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_69EC)
    Sleep(50)

    def lambda_69FC():
        OP_93(0x14, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_69FC)
    OP_0D()
    WaitChrThread(0x16, 1)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x16, 0x80)
    StopBGM(0xDAC)
    OP_63(0x14, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x109, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x14)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x109)
    OP_64(0x105)

    #C0236
    ChrTalk(
        0x101,
        "#12P#00001F……………………………\x02",
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7117", 0)

    #C0237
    ChrTalk(
        0x109,
        (
            "#12P#10101F好、好厉害的人物。\x02\x03",

            "#10106F让我感觉自己就像\x01",
            "被蛇盯上的青蛙一样……\x02",
        )
    )

    CloseMessageWindow()

    #C0238
    ChrTalk(
        0x102,
        "#12P#00103F是啊……\x02",
    )

    CloseMessageWindow()

    #C0239
    ChrTalk(
        0x105,
        (
            "#6P#10300F那就是黑月的精英年轻干部，\x01",
            "『白兰龙』曹·李吗？\x02\x03",

            "#10306F似乎比传闻中还要厉害呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0240
    ChrTalk(
        0x101,
        "#12P#00003F是啊，他一直那样。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_68(240, 1750, 1140, 3000)
    MoveCamera(326, 26, 0, 3000)
    OP_6E(600, 3000)
    SetCameraDistance(12930, 3000)

    def lambda_6BD8():
        OP_93(0x14, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_6BD8)

    def lambda_6BE5():
        OP_95(0x101, 500, 0, 2660, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6BE5)
    Sleep(100)

    def lambda_6C02():
        OP_95(0x102, -710, 0, 1990, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6C02)
    Sleep(100)

    def lambda_6C1F():
        OP_95(0x109, 900, 0, 1300, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_6C1F)
    Sleep(100)

    def lambda_6C3C():
        OP_95(0x105, -270, 0, 760, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_6C3C)
    WaitChrThread(0x101, 1)

    def lambda_6C5A():
        TurnDirection(0x101, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6C5A)
    WaitChrThread(0x102, 1)

    def lambda_6C6B():
        TurnDirection(0x102, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6C6B)
    WaitChrThread(0x109, 1)

    def lambda_6C7C():
        TurnDirection(0x109, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_6C7C)
    WaitChrThread(0x105, 1)

    def lambda_6C8D():
        TurnDirection(0x105, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_6C8D)
    OP_6F(0x79)
    Sleep(100)

    #C0241
    ChrTalk(
        0x101,
        (
            "#12P#00001F格蕾丝小姐，\x01",
            "黑月打算买下鲁巴彻旧址吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0242
    ChrTalk(
        0x14,
        (
            "#5P#02101F是的，听说他们打算\x01",
            "连同仓库一起买下来。\x02\x03",

            "#02103F如果黑月能顺利收购这个地方，\x01",
            "就等于是完全掌控了\x01",
            "克洛斯贝尔的地下世界……\x02\x03",

            "#02101F到时候，事态恐怕会很麻烦。\x02",
        )
    )

    CloseMessageWindow()

    #C0243
    ChrTalk(
        0x101,
        (
            "#12P#00003F……我有同感。\x02\x03",

            "#00006F话说回来，我们只是来探听情报的，\x01",
            "没想到却撞到了这么重大的场面。\x02",
        )
    )

    CloseMessageWindow()

    #C0244
    ChrTalk(
        0x102,
        (
            "#6P#00101F是啊，最好把这件事情\x01",
            "也一并汇报给一科。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x14, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0245
    ChrTalk(
        0x14,
        (
            "#5P#02105F咦？你们不是来调查\x01",
            "曹的动向的吗？\x02\x03",

            "#02102F难道在调查别的案子？\x02",
        )
    )

    CloseMessageWindow()

    #C0246
    ChrTalk(
        0x101,
        (
            "#12P#00012F这、这个……\x02\x03",

            "#00003F（对了，我记得格蕾丝小姐\x01",
            "  也见过那个人……）\x02\x03",

            "#00001F……其实我们正在搜寻一个\x01",
            "格蕾丝小姐也见过的人。\x02\x03",

            "就是那个名叫雷克特，\x01",
            "曾在巴鲁卡战胜矿工的人……\x02",
        )
    )

    CloseMessageWindow()

    #C0247
    ChrTalk(
        0x14,
        (
            "#5P#02105F啊，这样啊？\x02\x03",

            "#02103F我不久前刚在龙老饭店\x01",
            "见过那个人呢。\x02",
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
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0248
    ChrTalk(
        0x101,
        "#12P#00011F咦咦！？\x02",
    )

    CloseMessageWindow()

    #C0249
    ChrTalk(
        0x102,
        "#6P#00105F真、真的吗！？\x02",
    )

    CloseMessageWindow()

    #C0250
    ChrTalk(
        0x14,
        (
            "#5P#02100F是啊，他穿着一贯的度假装扮，\x01",
            "正在里面悠闲地用餐呢。\x02\x03",

            "#02103F我急着来这里取材，\x01",
            "所以没和他打招呼……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x14, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0251
    ChrTalk(
        0x14,
        (
            "#5P#02105F对了！我可不能在这里傻站着。\x02\x03",

            "#02101F至少也得从曹的口中挖出\x01",
            "一些核心情报才行啊。\x02\x03",

            "#02109F……我先走了！\x01",
            "下次一起吃个饭吧！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_7148():
        OP_93(0x101, 0x10E, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7148)

    def lambda_7155():
        OP_93(0x102, 0x10E, 0x12C)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7155)

    def lambda_7162():
        OP_93(0x109, 0x10E, 0x12C)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_7162)

    def lambda_716F():
        OP_93(0x105, 0x10E, 0x12C)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_716F)
    OP_95(0x14, -2000, 0, 2000, 5000, 0x0)
    OP_95(0x14, -15000, 0, 2000, 5000, 0x0)
    WaitChrThread(0x14, 1)
    Sleep(100)
    SetChrFlags(0x14, 0x80)
    OP_0D()

    #C0252
    ChrTalk(
        0x101,
        "#00012F真、真是老样子啊……\x02",
    )

    CloseMessageWindow()

    def lambda_71D2():
        OP_93(0x105, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_71D2)
    Sleep(100)

    #C0253
    ChrTalk(
        0x105,
        (
            "#6P#10300F话说回来，居然在意想不到的地方\x01",
            "得到了目击情报呢。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_7223():
        OP_93(0x101, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7223)

    def lambda_7230():
        OP_93(0x102, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7230)

    def lambda_723D():
        OP_93(0x109, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_723D)
    Sleep(100)

    #C0254
    ChrTalk(
        0x102,
        (
            "#5P#00100F是啊，赶快去\x01",
            "『龙老饭店』看看吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0255
    ChrTalk(
        0x109,
        "#12P#10100F明白了！\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_D7(0x1E)
    OP_D7(0x20)
    OP_D7(0x21)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x8, -6170, 0, 1400, 90)
    BeginChrThread(0x8, 0, 0, 1)
    OP_CC(0x1, 0xFF, 0x0)
    ModifyEventFlags(0, 0, 0x80)
    ModifyEventFlags(0, 1, 0x80)
    ModifyEventFlags(0, 2, 0x80)
    SetScenarioFlags(0x130, 2)
    OP_29(0x66, 0x1, 0x2)
    SetChrPos(0x0, -600, 0, 1560, 0)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_30_5DC9 end

    def Function_31_72F8(): pass

    label("Function_31_72F8")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(23420, 1450, 3590, 0)
    MoveCamera(0, 10, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16500, 0)
    OP_68(16170, 1450, 3590, 3000)
    ClearChrFlags(0x17, 0x80)
    SetChrFlags(0x17, 0x8000)
    SetMapObjFlags(0x5, 0x1000)
    ClearMapObjFlags(0x5, 0x4)
    OP_78(0x5, 0x17)
    SetChrPos(0x17, 16750, 16900, 4000, 0)
    OP_D5(0x17, 0x0, 0x0, 0x0, 0x0)
    SetChrPos(0x101, 25000, 0, 650, 270)
    SetChrPos(0x102, 27000, 0, 1500, 270)
    SetChrPos(0x109, 29000, 0, 2350, 270)
    SetChrPos(0x105, 31000, 0, 2350, 270)

    def lambda_73CA():
        OP_95(0x101, 15750, 0, 1500, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_73CA)
    Sleep(50)

    def lambda_73E7():
        OP_95(0x102, 16750, 0, 1200, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_73E7)
    Sleep(50)

    def lambda_7404():
        OP_95(0x109, 17750, 0, 1500, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_7404)
    Sleep(50)

    def lambda_7421():
        OP_95(0x105, 18750, 0, 2350, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_7421)
    Sleep(50)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x101, 1)

    def lambda_744C():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_744C)
    WaitChrThread(0x102, 1)

    def lambda_745D():
        OP_93(0x102, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_745D)
    WaitChrThread(0x109, 1)

    def lambda_746E():
        OP_93(0x109, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_746E)
    WaitChrThread(0x105, 1)

    def lambda_747F():
        OP_93(0x105, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_747F)
    WaitChrThread(0x105, 1)

    #C0256
    ChrTalk(
        0x109,
        "#12P#10111F居然真的爬下来了……\x02",
    )

    CloseMessageWindow()

    #C0257
    ChrTalk(
        0x105,
        (
            "#12P#10302F呵呵，是特意\x01",
            "练习过的吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0258
    ChrTalk(
        0x102,
        "#6P#00106F总、总之，赶紧追吧。\x02",
    )

    CloseMessageWindow()

    #C0259
    ChrTalk(
        0x101,
        (
            "#6P#00001F嗯，只能一个一个地询问\x01",
            "这条巷子里的人了……！\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x130, 4)
    OP_29(0x66, 0x1, 0x4)
    SetChrPos(0x0, 16750, 0, 1500, 0)
    ClearMapFlags(0x10000000)
    SetChrFlags(0x17, 0x80)
    SetMapObjFlags(0x5, 0x4)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_31_72F8 end

    def Function_32_7577(): pass

    label("Function_32_7577")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    EndChrThread(0x8, 0x0)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis011.itp")
    OP_68(-10220, 1950, 550, 0)
    MoveCamera(0, 10, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(14110, 0)
    SetChrPos(0x101, -10720, 0, 1550, 135)
    SetChrPos(0x102, -9720, 0, 1550, 225)
    SetChrPos(0x109, -11320, 0, -450, 45)
    SetChrPos(0x105, -9120, 0, -450, 315)
    FadeToBright(1000, 0)
    OP_0D()

    #C0260
    ChrTalk(
        0x102,
        (
            "#00106F呼，虽说过程有些漫长，\x01",
            "但对『钓皇俱乐部』的调查总算是完成了。\x02",
        )
    )

    CloseMessageWindow()

    #C0261
    ChrTalk(
        0x101,
        "#00000F嗯，是啊。\x02",
    )

    CloseMessageWindow()
    OP_29(0x6A, 0x1, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_777B")
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    #A0262
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "◆「调查状况？（测试用）\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【未变更】\x01",                # 0
            "【还有其它地点】\x01",          # 1
            "【六处全部确认完毕】\x01",      # 2
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
        (0, "loc_7754"),
        (1, "loc_7759"),
        (2, "loc_776A"),
        (SWITCH_DEFAULT, "loc_777B"),
    )


    label("loc_7754")

    Jump("loc_777B")

    label("loc_7759")

    ClearScenarioFlags(0x131, 5)
    ClearScenarioFlags(0x131, 6)
    ClearScenarioFlags(0x131, 7)
    ClearScenarioFlags(0x132, 2)
    Jump("loc_777B")

    label("loc_776A")

    SetScenarioFlags(0x131, 5)
    SetScenarioFlags(0x131, 6)
    SetScenarioFlags(0x131, 7)
    SetScenarioFlags(0x132, 2)
    Jump("loc_777B")

    label("loc_777B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x131, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x131, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_77C9")

    #C0263
    ChrTalk(
        0x101,
        (
            "#00000F那么，我们继续去\x01",
            "调查剩下的地方吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_780C")

    label("loc_77C9")

    OP_29(0x6A, 0x1, 0x6)

    #C0264
    ChrTalk(
        0x101,
        (
            "#00000F好，已经全部调查完毕了。\x02\x03",

            "去市民会馆汇报结果吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_780C")

    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(814, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0265
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※可以开始『钓鱼』了。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #A0266
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※在郊外或市区中的水边，\x01",
            "　会有一些『水面有波纹扩散的钓鱼点』。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #A0267
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※调查钓鱼点，\x01",
            "  并选择所持有的『钓竿』和『鱼饵』，\x01",
            "  罗伊德就会开始钓鱼。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #A0268
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※当 ！标志出现时，迅速按下○键，\x01",
            "  就能钓到鱼了。\x01",
            "  （运气不好时，鱼有可能会逃掉。）\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #A0269
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※另外，在克洛斯贝尔市内的\x01",
            "　『港湾区』和『住宅街』都有钓鱼点。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x8, -6170, 0, 1400, 90)
    BeginChrThread(0x8, 0, 0, 1)
    OP_CC(0x1, 0xFF, 0x0)
    SetScenarioFlags(0x132, 1)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, -10220, 0, 550, 180)
    EventEnd(0x5)
    Return()

    # Function_32_7577 end

    def Function_33_79D9(): pass

    label("Function_33_79D9")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch46500.itc", 0x1E)
    LoadChrToIndex("chr/ch46600.itc", 0x1F)
    LoadChrToIndex("apl/ch51276.itc", 0x20)
    OP_68(-11420, 1650, 160, 0)
    MoveCamera(40, 19, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(12580, 0)
    SetChrPos(0x101, -10990, 0, 1460, 90)
    SetChrPos(0x102, -10980, 0, 290, 90)
    SetChrPos(0x104, -12450, 0, 1970, 90)
    SetChrPos(0x109, -12260, 0, 770, 90)
    SetChrPos(0x105, -12420, 0, -470, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x1F, 0x80)
    SetChrChipByIndex(0x1F, 0x1E)
    SetChrPos(0x1F, -8340, 0, 1660, 270)
    SetChrFlags(0x1F, 0x8000)
    ClearChrFlags(0x1E, 0x80)
    SetChrChipByIndex(0x1E, 0x1F)
    SetChrPos(0x1E, -8320, 0, -60, 270)
    SetChrFlags(0x1E, 0x8000)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    FadeToBright(1000, 0)
    OP_0D()

    #C0270
    ChrTalk(
        0x1E,
        (
            "#12404F……各位，真是辛苦你们了。\x02\x03",

            "多亏有你们相助，才能在闹出\x01",
            "大乱子之前成功回收这东西。\x02",
        )
    )

    CloseMessageWindow()

    #C0271
    ChrTalk(
        0x101,
        (
            "#00000F哈哈……\x01",
            "能帮上您的忙，\x01",
            "我们也很高兴。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1F, 0x1E, 500)

    #C0272
    ChrTalk(
        0x1F,
        (
            "#5P#13900F呵……居然称我为『这东西』，\x01",
            "简直就像在谈论一件物品。\x02\x03",

            "#13903F……不过，这种粗暴的对待方式\x01",
            "也很有意思，好像挺不错呢。\x02\x03",

            "#13912F穆拉，今后偶尔也要\x01",
            "如此粗暴地对待我哟⊥\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1E, 0x1F, 500)

    #C0273
    ChrTalk(
        0x1E,
        "#12401F#4S#500W给#500W　我#500W　闭#500W　嘴。#3S\x02",
    )

    CloseMessageWindow()

    #C0274
    ChrTalk(
        0x1F,
        "#5P#13910F……对不起。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0x1E, 0x102, 500)

    #C0275
    ChrTalk(
        0x1E,
        (
            "#12400F……不好意思，其实我和\x01",
            "这个白痴相识已久。\x02\x03",

            "#12406F他的胡闹行为一直在\x01",
            "变本加厉，所以我总得\x01",
            "正颜厉色地对待他。\x02",
        )
    )

    CloseMessageWindow()

    #C0276
    ChrTalk(
        0x104,
        "#6P#00309F哈哈，好像很辛苦呢。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x1F, 0x101, 500)

    #C0277
    ChrTalk(
        0x1F,
        (
            "#13904F哪里哪里，身边有这样一位\x01",
            "用心辅助我的朋友，使我得益良多呢。\x02\x03",

            "#13909F呵呵，这也算是人望所归吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0278
    ChrTalk(
        0x104,
        (
            "#6P#00306F我、我那句话并不是\x01",
            "对你说的啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0279
    ChrTalk(
        0x105,
        (
            "#6P#10309F呵呵，好像一点\x01",
            "都没有反省呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0280
    ChrTalk(
        0x1E,
        (
            "#12400F……说的没错。\x02\x03",

            "待会我会狠狠教训你一顿，\x01",
            "做好心理准备吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0281
    ChrTalk(
        0x1F,
        (
            "#5P#13911F讨、讨厌啦～\x01",
            "我只是开个玩笑而已嘛，穆拉。\x02\x03",

            "#13910F……请你们不要\x01",
            "刺激到他。\x02",
        )
    )

    CloseMessageWindow()

    #C0282
    ChrTalk(
        0x109,
        (
            "#6P#10109F啊、啊哈哈……\x01",
            "（从某种意义上来说，他们的感情其实很好呢……）\x02",
        )
    )

    CloseMessageWindow()

    #C0283
    ChrTalk(
        0x1E,
        (
            "#12400F……那么，我们就此告辞。\x02\x03",

            "#12404F在如此繁忙的时期还麻烦各位，\x01",
            "实在是不好意思，请容我郑重道谢。\x02",
        )
    )

    CloseMessageWindow()

    #C0284
    ChrTalk(
        0x101,
        (
            "#00000F哪里，这是我们的本职工作。\x02\x03",

            "#00006F那个……请您今后看紧一些，\x01",
            "别让他再次跑掉。\x02",
        )
    )

    CloseMessageWindow()

    #C0285
    ChrTalk(
        0x1E,
        "#12406F……我明白。\x02",
    )

    CloseMessageWindow()

    #C0286
    ChrTalk(
        0x1F,
        (
            "#13910F唉……真是的……\x01",
            "快乐的时间就此结束了吗？\x02\x03",

            "#13900F这次真的要说再见了，各位。\x01",
            "如果有缘，我们还会在其它地方重逢的。\x02",
        )
    )

    CloseMessageWindow()

    #C0287
    ChrTalk(
        0x101,
        "#00006F好、好的……\x02",
    )

    CloseMessageWindow()

    #C0288
    ChrTalk(
        0x1F,
        (
            "#13910F话说回来，其实我还想去\x01",
            "参观一下那座传闻中的\x01",
            "主题公园呢。\x02\x03",

            "#13905F对了，我现在可以委托\x01",
            "你们几位当我的导游吗？\x02\x03",

            "#13904F呵呵，这主意真是太棒了。\x01",
            "只要能度过一段愉快的时光，\x01",
            "穆拉眉间的皱褶也一定会……\x02",
        )
    )

    CloseMessageWindow()
    OP_95(0x1E, -7500, 0, 690, 2000, 0x0)
    OP_95(0x1E, -7490, 0, 1670, 2000, 0x0)
    OP_93(0x1E, 0x10E, 0x1F4)
    Sound(802, 0, 100, 0)

    #C0289
    ChrTalk(
        0x1F,
        (
            "#13911F啊！穆拉！？\x01",
            "我、我只是开个玩笑而已啊！\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x1F, 0x13B, 0x0)
    SetChrChipByIndex(0x1F, 0x20)
    SetChrSubChip(0x1F, 0x0)
    SetChrFlags(0x1F, 0x20)

    def lambda_8220():
        OP_95(0xFE, 2000, 0, 1310, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_8220)
    Sleep(50)

    def lambda_823D():
        OP_96(0xFE, 0x7D0, 0x0, 0x4F6, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_823D)
    Sleep(50)

    #C0290
    ChrTalk(
        0x1F,
        "#11A哎～呀………………\x02",
    )
    #Auto

    Sleep(1500)
    OP_57(0x0)
    OP_5A()
    WaitChrThread(0x1E, 1)
    WaitChrThread(0x1F, 1)
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0291
    ChrTalk(
        0x101,
        (
            "#00012F这、这两个人\x01",
            "都很奇特呢。\x02\x03",

            "#00003F说真的，他们到底是\x01",
            "什么人呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0292
    ChrTalk(
        0x105,
        (
            "#12P#10302F这个问题就留到\x01",
            "下次见面的时候\x01",
            "再问吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0293
    ChrTalk(
        0x109,
        (
            "#6P#10106F老实说，我觉得到时候\x01",
            "肯定又会相当累人……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x102)

    #C0294
    ChrTalk(
        0x102,
        (
            "#00103F（刚才一时情急，就出口威吓了他……\x01",
            "  但那个人难道是……）\x02\x03",

            "#00109F（再、再怎么说，应该也不可能吧……）\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)

    #C0295
    ChrTalk(
        0x101,
        (
            "#00005F怎么了？艾莉。\x01",
            "你从刚才开始就一直在沉默……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)

    #C0296
    ChrTalk(
        0x102,
        "#11P#00102F啊，没、没什么啦。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0297
    ChrTalk(
        0x104,
        (
            "#00303F……总之，我们已经\x01",
            "解决掉一件委托了。\x02\x03",

            "#00300F走吧，罗伊德。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_8514():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8514)
    Sleep(50)

    def lambda_8524():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8524)
    Sleep(300)
    OP_62(0x101)

    #C0298
    ChrTalk(
        0x101,
        "#11P#00000F嗯，走吧。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x24, 3)
    NewScene("c0100", 100, 0, 0)
    IdleLoop()
    EventEnd(0x5)
    Return()

    # Function_33_79D9 end

    def Function_34_8567(): pass

    label("Function_34_8567")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_8575")
    Jump("loc_88BA")

    label("loc_8575")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_8583")
    Jump("loc_88BA")

    label("loc_8583")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_8591")
    Jump("loc_88BA")

    label("loc_8591")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_86E8")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8662")

    #C0299
    ChrTalk(
        0x101,
        "#00001F这里是深红商会。\x02",
    )

    CloseMessageWindow()

    #C0300
    ChrTalk(
        0x104,
        (
            "#00303F自通商会议那起事件之后，\x01",
            "叔叔他们就\x01",
            "彻底没了动静。\x02\x03",

            "#00301F就算进去，恐怕也得不到\x01",
            "什么有用的情报。\x02",
        )
    )

    CloseMessageWindow()

    #C0301
    ChrTalk(
        0x101,
        (
            "#00003F是啊……\x01",
            "现在还是别进去了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_86D0")

    label("loc_8662")


    #C0302
    ChrTalk(
        0x101,
        (
            "#00003F自通商会议之后，深红商会\x01",
            "就彻底没了动静。\x02\x03",

            "#00001F现在应该得不到什么有用的情报，\x01",
            "还是不要进去了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_86D0")

    SetChrPos(0x0, 90, 0, 80, 180)
    EventEnd(0x4)
    Jump("loc_88BA")

    label("loc_86E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_876E")
    EventBegin(0x1)

    #C0303
    ChrTalk(
        0x101,
        (
            "#00000F搜查一科正在严密监视着\x01",
            "深红商会。\x02\x03",

            "这里就交给一科负责，\x01",
            "我们还是专心完成自己的工作吧。\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, 90, 0, 80, 180)
    EventEnd(0x4)
    Jump("loc_88BA")

    label("loc_876E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_8810")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14E, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8789")
    Call(0, 11)
    Jump("loc_880B")

    label("loc_8789")

    EventBegin(0x1)

    #C0304
    ChrTalk(
        0x101,
        (
            "#00003F在这里恐怕调查不到\x01",
            "『赤色星座』的动向。\x02\x03",

            "#00000F还是在处理支援请求的同时，\x01",
            "去各地询问一下吧。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, 90, 0, 80, 180)
    EventEnd(0x4)

    label("loc_880B")

    Jump("loc_88BA")

    label("loc_8810")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 4)), scpexpr(EXPR_END)), "loc_881E")
    Jump("loc_88BA")

    label("loc_881E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_882C")
    Jump("loc_88BA")

    label("loc_882C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_88BA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x130, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_88BA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x139, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8851")
    Call(0, 10)
    Jump("loc_88BA")

    label("loc_8851")

    EventBegin(0x1)

    #C0305
    ChrTalk(
        0x101,
        (
            "#00000F房产经营者正在里面\x01",
            "等待商谈生意的对象。\x02\x03",

            "总不能打扰人家，还是赶快走吧。\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, 90, 0, 80, 180)
    EventEnd(0x4)

    label("loc_88BA")

    Return()

    # Function_34_8567 end

    def Function_35_88BB(): pass

    label("Function_35_88BB")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_88FA")
    Sound(807, 0, 100, 0)
    SetChrName("")

    #A0306
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "门锁着。\x01",
            "里面应该没有人。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_89CA")

    label("loc_88FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_8936")
    Sound(807, 0, 100, 0)
    SetChrName("")

    #A0307
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "门锁着。\x01",
            "里面应该没有人。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_89CA")

    label("loc_8936")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_8988")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18E, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8955")
    TalkEnd(0xFF)
    Call(0, 12)
    Return()

    label("loc_8955")

    Sound(807, 0, 100, 0)
    SetChrName("")

    #A0308
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "门锁着。\x01",
            "里面应该没有人。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_89CA")

    label("loc_8988")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_8996")
    Jump("loc_89CA")

    label("loc_8996")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_89A4")
    Jump("loc_89CA")

    label("loc_89A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_89CA")
    Sound(807, 0, 100, 0)
    SetChrName("")

    #A0309
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "门锁着。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_89CA")

    TalkEnd(0xFF)
    Return()

    # Function_35_88BB end

    def Function_36_89CE(): pass

    label("Function_36_89CE")

    EventBegin(0x2)
    ClearMapFlags(0x20)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0310
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※　百货店『时代』　※\x01",
            "※　职员专用出入口　※\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    EventEnd(0x3)
    Return()

    # Function_36_89CE end

    def Function_37_8A26(): pass

    label("Function_37_8A26")

    EventBegin(0x2)
    ClearMapFlags(0x20)
    Sound(807, 0, 100, 0)
    SetChrName("")

    #A0311
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "门上了锁。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    EventEnd(0x3)
    Return()

    # Function_37_8A26 end

    def Function_38_8A4F(): pass

    label("Function_38_8A4F")

    EventBegin(0x1)

    #C0312
    ChrTalk(
        0x101,
        (
            "#00001F我们得赶快追上兰迪，\x01",
            "马上前往鲁巴彻旧址吧！\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, -24330, 0, 210, 90)
    EventEnd(0x4)
    Return()

    # Function_38_8A4F end

    def Function_39_8A9E(): pass

    label("Function_39_8A9E")

    EventBegin(0x1)

    #C0313
    ChrTalk(
        0x101,
        (
            "#00001F我们得赶快追上兰迪，\x01",
            "马上前往鲁巴彻旧址吧！\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 19310, 0, 650, 270)
    EventEnd(0x4)
    Return()

    # Function_39_8A9E end

    SaveToFile()

Try(main)
