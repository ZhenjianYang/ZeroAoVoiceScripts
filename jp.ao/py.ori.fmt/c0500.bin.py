from ScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "アイリス",               # 1
        "客引きビッシュ",         # 2
        "警官",                   # 3
        "警官",                   # 4
        "猟兵ザックス",           # 5
        "猟兵",                   # 6
        "不動産業者",             # 7
        "隻眼の男",               # 8
        "赤毛の少女",             # 9
        "レクター",               # 10
        "猟兵ガレス",             # 11
        "車",                     # 12
        "グレイス",               # 13
        "ツァオ",                 # 14
        "ラウ",                   # 15
        "ザイル",                 # 16
        "ユーリ",                 # 17
        "サイクス",               # 18
        "レジー",                 # 19
        "ケイト巡査",             # 20
        "フランツ巡査",           # 21
        "SE制御",                 # 22
        "ミュラー",               # 23
        "オリビエ",               # 24
        "中央広場",               # 25
        "西通り",                 # 26
        "行政区",                 # 27
        "住宅街",                 # 28
        "歓楽街",                 # 29
        "東通り",                 # 30
        "旧市街",                 # 31
        "港湾区",                 # 32
        "ＩＢＣ",                 # 33
        "駅前通り",               # 34
        "裏通り",                 # 35
        "ウルスラ間道",           # 36
        "東クロスベル街道",       # 37
        "西クロスベル街道",       # 38
        "マインツ山道",           # 39
        "オルキスタワー",         # 40
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

    PlaceName(79.5, 0.0, -9.0, 0x0000, 0x0000, "中央広場")
    PlaceName(0.0, 0.0, -76.5, 0x0000, 0x0000, "西通り")
    PlaceName(11.0, 0.0, 116.0, 0x0000, 0x0000, "行政区")
    PlaceName(-148.0, 0.0, -60.0, 0x0000, 0x0000, "住宅街")
    PlaceName(-57.25, 0.0, 10.0, 0x0000, 0x0000, "歓楽街")
    PlaceName(196.0, 0.0, 56.0, 0x0000, 0x0000, "東通り")
    PlaceName(294.0, 0.0, 31.0, 0x0000, 0x0000, "旧市街")
    PlaceName(154.0, 0.0, 158.0, 0x0000, 0x0000, "港湾区")
    PlaceName(20.0, 0.0, 233.0, 0x0000, 0x0000, "ＩＢＣ")
    PlaceName(168.0, 0.0, -73.0, 0x0000, 0x0000, "駅前通り")
    PlaceName(1.0, 0.0, -9.0, 0x0000, 0x0000, "裏通り")
    PlaceName(200.0, 0.0, -112.0, 0x0000, 0x0000, "ウルスラ間道")
    PlaceName(240.0, 0.0, 130.0, 0x0000, 0x0000, "東クロスベル街道")
    PlaceName(-52.0, 0.0, -134.0, 0x0000, 0x0000, "西クロスベル街道")
    PlaceName(-156.0, 0.0, -17.0, 0x0000, 0x0000, "マインツ山道")
    PlaceName(-140.0, 0.0, 255.0, 0x0000, 0x0000, "オルキスタワー")
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
        "Function_6_1E4E",         # 06, 6
        "Function_7_29F7",         # 07, 7
        "Function_8_2B53",         # 08, 8
        "Function_9_2BA7",         # 09, 9
        "Function_10_2C25",        # 0A, 10
        "Function_11_34B8",        # 0B, 11
        "Function_12_3D07",        # 0C, 12
        "Function_13_401E",        # 0D, 13
        "Function_14_4157",        # 0E, 14
        "Function_15_4184",        # 0F, 15
        "Function_16_41BB",        # 10, 16
        "Function_17_520E",        # 11, 17
        "Function_18_526C",        # 12, 18
        "Function_19_526D",        # 13, 19
        "Function_20_52C3",        # 14, 20
        "Function_21_52C4",        # 15, 21
        "Function_22_5329",        # 16, 22
        "Function_23_532A",        # 17, 23
        "Function_24_595B",        # 18, 24
        "Function_25_5D24",        # 19, 25
        "Function_26_5D4D",        # 1A, 26
        "Function_27_5DB5",        # 1B, 27
        "Function_28_5F4C",        # 1C, 28
        "Function_29_62D7",        # 1D, 29
        "Function_30_663B",        # 1E, 30
        "Function_31_7D2F",        # 1F, 31
        "Function_32_7FC8",        # 20, 32
        "Function_33_84DB",        # 21, 33
        "Function_34_9189",        # 22, 34
        "Function_35_9551",        # 23, 35
        "Function_36_96B0",        # 24, 36
        "Function_37_9710",        # 25, 37
        "Function_38_9747",        # 26, 38
        "Function_39_979E",        # 27, 39
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_118C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10F3")

    #C0001
    ChrTalk(
        0xFE,
        (
            "なんだか大変な時だからか、\x01",
            "お店の方でも妙な連帯感なのよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0xFE,
        (
            "あたしもライバルの子との\x01",
            "トップ争いなんて、\x01",
            "どうでもよくなっちゃった。\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0xFE,
        (
            "ホステスとして、お客さんに\x01",
            "楽しんでお酒を飲んでもらえれば\x01",
            "それでいいよね☆\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1187")

    label("loc_10F3")


    #C0004
    ChrTalk(
        0xFE,
        (
            "ライバルの子との\x01",
            "トップ争いなんて、\x01",
            "どうでもよくなっちゃった。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0xFE,
        (
            "ホステスとして、お客さんに\x01",
            "楽しんでお酒を飲んでもらえれば\x01",
            "それでいいよね☆\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1187")

    Jump("loc_1E4A")

    label("loc_118C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_119A")
    Jump("loc_1E4A")

    label("loc_119A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_12CF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1255")

    #C0006
    ChrTalk(
        0xFE,
        (
            "国家独立……\x01",
            "口に出すといい響きよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0xFE,
        (
            "お店の人たちも、\x01",
            "大統領の演説を見て\x01",
            "すっごく喜んでたみたい。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0xFE,
        (
            "……なんだかあたしも\x01",
            "嬉しくなってきちゃった♪\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_12CA")

    label("loc_1255")


    #C0009
    ChrTalk(
        0xFE,
        (
            "お店の人たちも、\x01",
            "大統領の演説を見て\x01",
            "すっごく喜んでたみたい。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0xFE,
        (
            "……なんだかあたしも\x01",
            "嬉しくなってきちゃった♪\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12CA")

    Jump("loc_1E4A")

    label("loc_12CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_12DD")
    Jump("loc_1E4A")

    label("loc_12DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_1370")

    #C0011
    ChrTalk(
        0xFE,
        (
            "マインツの占領なんて、\x01",
            "本当に大事件じゃない……！\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0xFE,
        (
            "あそこの鉱員さんも、\x01",
            "前に店に来てくれてたのよ。\x01",
            "無事だといいんだけど……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E4A")

    label("loc_1370")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_14A0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1422")

    #C0013
    ChrTalk(
        0xFE,
        "聞いて聞いて、大ニュース！\x02",
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0xFE,
        (
            "なんと、ウチの店の\x01",
            "今月の指名ナンバーワンが\x01",
            "あたしに決まっちゃったの！\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0xFE,
        (
            "うふふ、がんばった甲斐が\x01",
            "あったわ～！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_149B")

    label("loc_1422")


    #C0016
    ChrTalk(
        0xFE,
        (
            "ついに念願のナンバーワンに\x01",
            "なっちゃったわ！\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0xFE,
        (
            "ふふ、これから指名も\x01",
            "どんどん増えるだろうし、\x01",
            "がんばんなくちゃね！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_149B")

    Jump("loc_1E4A")

    label("loc_14A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_14ED")

    #C0018
    ChrTalk(
        0xFE,
        (
            "中央広場のほうが騒がしいけど……\x01",
            "なになに、何かあったの？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E4A")

    label("loc_14ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1641")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15D4")

    #C0019
    ChrTalk(
        0xFE,
        (
            "指名数を競ってるライバルの子が、\x01",
            "自分の指名を増やすために\x01",
            "知り合いを店に呼んでたのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0xFE,
        "き～っ、ズルいと思わない！？\x02",
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0xFE,
        (
            "こうなったらあたしだって、\x01",
            "やれることはなんだって\x01",
            "やってやるんだからっ！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_163C")

    label("loc_15D4")


    #C0022
    ChrTalk(
        0xFE,
        (
            "ライバルの子になんて\x01",
            "負けてられないっ！\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0xFE,
        (
            "ナンバーワンになるためなら\x01",
            "なんだってやってやるわっ！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_163C")

    Jump("loc_1E4A")

    label("loc_1641")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_179B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1705")

    #C0024
    ChrTalk(
        0xFE,
        (
            "お兄さ～ん、\x01",
            "ウチの店で遊んでかな～い？\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0xFE,
        (
            "……実は今、ライバルの子と\x01",
            "僅差で指名数を争ってるのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0xFE,
        (
            "勝ったほうが今月のナンバーワン！\x01",
            "だから協力してよ、ねっ？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1796")

    label("loc_1705")


    #C0027
    ChrTalk(
        0xFE,
        (
            "……うーん、そっか。\x01",
            "お兄さんたちは仕事中かあ。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0xFE,
        (
            "それじゃ、ウチの店に来る時は\x01",
            "是非あたしを指名してよね。\x01",
            "ナンバーワンがかかってるから！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1796")

    Jump("loc_1E4A")

    label("loc_179B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_180E")

    #C0029
    ChrTalk(
        0xFE,
        (
            "最近、店のライバルの子が\x01",
            "指名をバンバン増やしてきたの。\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0xFE,
        "あたしも負けないようにしないとね。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1E4A")

    label("loc_180E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_19C5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_193D")

    #C0031
    ChrTalk(
        0xFE,
        (
            "オルキスタワーって\x01",
            "とってもすっごい建物ねえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0xFE,
        (
            "ちょっと仕事を抜け出して、\x01",
            "お披露目を見てきたんだけど、\x01",
            "度肝を抜かれちゃったわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0xFE,
        (
            "あんな所で働く人は、\x01",
            "きっとものすごく景気のいい\x01",
            "人たちにちがいないわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0xFE,
        (
            "ウチの店に接待にきたら、\x01",
            "是非とも指名してほしいわね～。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_19C0")

    label("loc_193D")


    #C0035
    ChrTalk(
        0xFE,
        (
            "オルキスタワーって\x01",
            "とってもすっごい建物ねえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0xFE,
        (
            "あんな所で働く人が\x01",
            "ウチの店に接待にきたら、\x01",
            "是非とも指名してほしいわね～。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19C0")

    Jump("loc_1E4A")

    label("loc_19C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1B1C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A86")

    #C0037
    ChrTalk(
        0xFE,
        (
            "お客さんから聞いたんだけど、\x01",
            "明日から通商会議ってのが\x01",
            "始まるらしいわね～。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0xFE,
        (
            "記念祭みたいなお祭りじゃあ\x01",
            "ないみたいだけど……\x01",
            "一体どんなイベントなのかしらね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1B17")

    label("loc_1A86")


    #C0039
    ChrTalk(
        0xFE,
        (
            "おっと、いけないいけない。\x01",
            "別に気にすることじゃないわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0xFE,
        (
            "今はライバルの子に負けないように\x01",
            "一つでも多く指名を増やす事を\x01",
            "考えないとね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B17")

    Jump("loc_1E4A")

    label("loc_1B1C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 4)), scpexpr(EXPR_END)), "loc_1C94")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C08")

    #C0041
    ChrTalk(
        0xFE,
        (
            "さっき、赤い髪をして\x01",
            "ガタイのいいオジサンが\x01",
            "このあたりにいたのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0xFE,
        (
            "猫みたいな可愛い女の子と、\x01",
            "見るからに遊び人風のお兄さんを\x01",
            "連れていたみたいだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0xFE,
        (
            "とにかく、なんだか\x01",
            "異様な光景だったわね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1C8F")

    label("loc_1C08")


    #C0044
    ChrTalk(
        0xFE,
        (
            "そういえば、\x01",
            "ついさっき見かけたお兄さんも、\x01",
            "同じような髪の色だったなー。\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0xFE,
        (
            "みんな家族か何かかしら？\x01",
            "あんまり似てなかったけど。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C8F")

    Jump("loc_1E4A")

    label("loc_1C94")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_1D24")

    #C0046
    ChrTalk(
        0xFE,
        (
            "裏路地の方の一帯が\x01",
            "売りに出されたってホント？\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0xFE,
        (
            "前は黒服の怖～いお兄さんがいたけど……\x01",
            "次はどんな人たちが入るのかしらね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E4A")

    label("loc_1D24")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_1E4A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1DC5")

    #C0048
    ChrTalk(
        0xFE,
        "うふっ、アイリスで～すっ☆\x02",
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0xFE,
        (
            "お兄さ～ん、\x01",
            "ウチの店で遊んでかな～い？\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0xFE,
        (
            "あたしと飲んでおしゃべりして、\x01",
            "楽しく過ごそうよ～㈱\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1E4A")

    label("loc_1DC5")


    #C0051
    ChrTalk(
        0xFE,
        (
            "最近、指名も増えてきて\x01",
            "とっても充実してるの。\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0xFE,
        (
            "ライバルの子に差をつけて、\x01",
            "そのうち指名数ナンバーワンに\x01",
            "なってやるんだから！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E4A")

    TalkEnd(0xFE)
    Return()

    # Function_5_FF8 end

    def Function_6_1E4E(): pass

    label("Function_6_1E4E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1F96")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F19")

    #C0053
    ChrTalk(
        0xFE,
        (
            "お兄さんお兄さん、\x01",
            "ウチの店寄っていかへんか～？\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0xFE,
        (
            "ディーター大統領拘束記念の\x01",
            "ハイパーハッピーセール中や～！\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0xFE,
        (
            "……独立記念の時にも\x01",
            "セールをやったんはヒミツやで？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1F91")

    label("loc_1F19")


    #C0056
    ChrTalk(
        0xFE,
        (
            "ディーター大統領拘束記念の\x01",
            "ハイパーハッピーセール中や～！\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0xFE,
        (
            "……独立記念の時にも\x01",
            "セールをやったんはヒミツやで？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F91")

    Jump("loc_29F3")

    label("loc_1F96")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_1FA4")
    Jump("loc_29F3")

    label("loc_1FA4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_205A")

    #C0058
    ChrTalk(
        0xFE,
        (
            "お兄さんお兄さん、\x01",
            "ウチの店では独立記念の、\x01",
            "スーパーハッピーセール中や！\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0xFE,
        (
            "せっかくのクロスベルの夜明け、\x01",
            "可愛い女の子と一緒に過ごさな\x01",
            "ソンっちゅうもんやで～！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_29F3")

    label("loc_205A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_20FD")

    #C0060
    ChrTalk(
        0xFE,
        (
            "お兄さんお兄さん、ウチの店も\x01",
            "この間、営業を再開したで～。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0xFE,
        (
            "復旧作業で疲れた心と身体、\x01",
            "可愛い女の子たちと一緒に\x01",
            "飲んで遊んで癒してこ、な！？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_29F3")

    label("loc_20FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_218B")

    #C0062
    ChrTalk(
        0xFE,
        (
            "占領事件やなんて……\x01",
            "とんでもない事になってしもたなあ。\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0xFE,
        (
            "さすがのワテも、こんな状況じゃ\x01",
            "客引きに励む気にもなれへんよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_29F3")

    label("loc_218B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_222D")

    #C0064
    ChrTalk(
        0xFE,
        (
            "やれやれ、また雨が降ってもうた。\x01",
            "お客さんも少なくて切ないわ～。\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0xFE,
        (
            "昨日はデカい事故が起きたっちゅう話やし、\x01",
            "なんや景気が悪うてかなわんで～。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_29F3")

    label("loc_222D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_2296")

    #C0066
    ChrTalk(
        0xFE,
        (
            "なんや、広場のほうが\x01",
            "ピーポーピーポーうるさいなあ。\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0xFE,
        "またなんか事件でもあったん？\x02",
    )

    CloseMessageWindow()
    Jump("loc_29F3")

    label("loc_2296")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_23E4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_236A")

    #C0068
    ChrTalk(
        0xFE,
        (
            "ウチの店、今日は恒例の\x01",
            "ハッピーセールや。\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0xFE,
        (
            "可愛い女の子たちが\x01",
            "これまたかわいい衣装で\x01",
            "出迎えてくれるで～！\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0xFE,
        (
            "今日を逃すと、\x01",
            "次はいつやるか分からんで！\x01",
            "ほらほら、ついてきー！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_23DF")

    label("loc_236A")


    #C0071
    ChrTalk(
        0xFE,
        (
            "ウチの店、今日は恒例の\x01",
            "ハッピーセールや。\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0xFE,
        (
            "今日を逃すと、\x01",
            "次はいつやるか分からんで！\x01",
            "ほらほら、ついてきー！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_23DF")

    Jump("loc_29F3")

    label("loc_23E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_247B")

    #C0073
    ChrTalk(
        0xFE,
        (
            "最近は、独立がどーだの、\x01",
            "ムズかしいことばっかりやな。\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0xFE,
        (
            "こんなときこそ、\x01",
            "ウチの店で気晴らししていきー。\x01",
            "ハッピーにさせたるで～♪\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_29F3")

    label("loc_247B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_251C")

    #C0075
    ChrTalk(
        0xFE,
        (
            "表通りの方で見た\x01",
            "警察のあんさんたちも、\x01",
            "なんや気合入っとるみたいやな～。\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0xFE,
        (
            "仕事に疲れとる人は客引きの狙い目や。\x01",
            "へへ、あとで声かけてみよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_29F3")

    label("loc_251C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_259E")

    #C0077
    ChrTalk(
        0xFE,
        (
            "各国の首脳たちが\x01",
            "クロスベル入りしたみたいやね。\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0xFE,
        (
            "ウチの店で飲んでってくれたら\x01",
            "ええ宣伝になるんやけどな～。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_29F3")

    label("loc_259E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2631")

    #C0079
    ChrTalk(
        0xFE,
        (
            "裏路地に入った\x01",
            "クリムゾン商会の兄さんら、\x01",
            "元気良さそうな人ばっかやな。\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0xFE,
        (
            "へへ、可愛い子紹介して\x01",
            "新しい常連さんゲットやで～。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_29F3")

    label("loc_2631")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 4)), scpexpr(EXPR_END)), "loc_270D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_26C4")

    #C0081
    ChrTalk(
        0xFE,
        (
            "あちゃ～、こりゃアカン。\x01",
            "本降りになってもうたなあ。\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0xFE,
        (
            "今日はもう誰も引っかからんやろ。\x01",
            "そろそろ引き上げるか～。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2708")

    label("loc_26C4")


    #C0083
    ChrTalk(
        0xFE,
        (
            "……赤毛の兄さん？\x01",
            "さっきそこの路地裏に\x01",
            "入ってったみたいやで。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2708")

    Jump("loc_29F3")

    label("loc_270D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_277E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x139, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2728")
    Call(0, 7)
    Jump("loc_2779")

    label("loc_2728")


    #C0084
    ChrTalk(
        0xFE,
        (
            "雨の日はあんまり\x01",
            "お客さんが引っかからんのや。\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0xFE,
        "やれやれ、困るでしかし。\x02",
    )

    CloseMessageWindow()

    label("loc_2779")

    Jump("loc_29F3")

    label("loc_277E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_29F3")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x66, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x130, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_28C9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2847")

    #C0086
    ChrTalk(
        0xFE,
        (
            "さっきここを通って\x01",
            "歓楽街の方に行った赤毛のニーさん……\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0xFE,
        (
            "なんやあのヒト、\x01",
            "前にもこの辺りで\x01",
            "見たような気ィするなあ……\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0xFE,
        "ま、気のせいやろけどな。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_28C4")

    label("loc_2847")


    #C0089
    ChrTalk(
        0xFE,
        (
            "赤毛のニーさんなら、\x01",
            "歓楽街の方に歩いていったで。\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0xFE,
        (
            "前にもこの辺りで\x01",
            "見たような気ィするけど……\x01",
            "まあ、気のせいやな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_28C4")

    Jump("loc_29F3")

    label("loc_28C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x139, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_28DB")
    Call(0, 7)
    Jump("loc_29F3")

    label("loc_28DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_29C4")

    #C0091
    ChrTalk(
        0xFE,
        (
            "ヘヘ、こりゃ失礼。\x01",
            "今回だけ見逃してえな。\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0xFE,
        (
            "なんやったら、次回来店の際の\x01",
            "サービス券をプレゼントするさかい。\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x101,
        (
            "#00003Fいりませんから。\x01",
            "……贈賄も立派な犯罪ですよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0xFE,
        (
            "へへ、あんさんらには\x01",
            "かなわんなあ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_29F3")

    label("loc_29C4")


    #C0095
    ChrTalk(
        0xFE,
        (
            "ヘヘ、こりゃ失礼。\x01",
            "今回だけ見逃してえな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_29F3")

    TalkEnd(0xFE)
    Return()

    # Function_6_1E4E end

    def Function_7_29F7(): pass

    label("Function_7_29F7")


    #C0096
    ChrTalk(
        0x9,
        (
            "あ、そこの兄さんたち\x01",
            "暇してんとちゃいますの？\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0x9,
        (
            "ウチの店、カワイコちゃんが\x01",
            "ぎょーさんおるで～！\x01",
            "な、寄ってって！　な？\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x101,
        "#00001F……強引な客引きは違法行為ですよ？\x02",
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0x9,
        (
            "ンなカタいこと……って、\x01",
            "アンタらケーサツの人？\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0x9,
        (
            "ヘヘ、こりゃ失礼。\x01",
            "今回だけ見逃してえな、な？\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0x102,
        (
            "#00106F（ふう……相変わらず\x01",
            "  このあたりは治安が悪いわね。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x139, 2)
    Return()

    # Function_7_29F7 end

    def Function_8_2B53(): pass

    label("Function_8_2B53")

    TalkBegin(0xFE)

    #C0102
    ChrTalk(
        0xFE,
        (
            "現在、こちらのビルは\x01",
            "一課が捜査中です。\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0xFE,
        "立ち入りはご遠慮願います。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_8_2B53 end

    def Function_9_2BA7(): pass

    label("Function_9_2BA7")

    TalkBegin(0xFE)

    #C0104
    ChrTalk(
        0xFE,
        (
            "赤い星座の連中め、\x01",
            "とんでもないことを\x01",
            "しでかしてくれたものだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0xFE,
        (
            "早いうちに事件が\x01",
            "解決できればいいんだが……\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_9_2BA7 end

    def Function_10_2C25(): pass

    label("Function_10_2C25")

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
            "#12P#00001Fここは……\x01",
            "ルバーチェ商会の跡地だな。\x02\x03",

            "#00003F今はもぬけの空のはずだけど……\x02",
        )
    )

    CloseMessageWindow()

    #N0107
    NpcTalk(
        0xE,
        "男性の声",
        (
            "おや君たち、\x01",
            "そこで何をしてるのかね？\x02",
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

    def lambda_2DD7():

        label("loc_2DD7")

        TurnDirection(0xFE, 0xE, 300)
        Yield()
        Jump("loc_2DD7")

    QueueWorkItem2(0x101, 2, lambda_2DD7)

    def lambda_2DE9():

        label("loc_2DE9")

        TurnDirection(0xFE, 0xE, 300)
        Yield()
        Jump("loc_2DE9")

    QueueWorkItem2(0x102, 2, lambda_2DE9)

    def lambda_2DFB():

        label("loc_2DFB")

        TurnDirection(0xFE, 0xE, 300)
        Yield()
        Jump("loc_2DFB")

    QueueWorkItem2(0x109, 2, lambda_2DFB)

    def lambda_2E0D():

        label("loc_2E0D")

        TurnDirection(0xFE, 0xE, 300)
        Yield()
        Jump("loc_2E0D")

    QueueWorkItem2(0x105, 2, lambda_2E0D)

    def lambda_2E1F():
        OP_95(0xFE, 0, 0, 33500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_2E1F)
    WaitChrThread(0xE, 1)
    OP_4B(0xE, 0xFF)

    #C0108
    ChrTalk(
        0x101,
        "#00005Fえっと、あなたは……？\x02",
    )

    CloseMessageWindow()
    EndChrThread(0x101, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x109, 0x2)
    EndChrThread(0x105, 0x2)

    #N0109
    NpcTalk(
        0xE,
        "男性",
        (
            "#12Pコホン、私はクロスベル市で\x01",
            "不動産業を営んでいる者だ。\x02",
        )
    )

    CloseMessageWindow()

    #N0110
    NpcTalk(
        0xE,
        "男性",
        (
            "#12P自治州政府に委託されて、\x01",
            "一帯の土地の管理を任されている。\x02",
        )
    )

    CloseMessageWindow()

    #N0111
    NpcTalk(
        0xE,
        "男性",
        "#12P勝手に敷地に入られると困るんだがね。\x02",
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0x102,
        (
            "#5P#00103F政府が委託した……\x01",
            "そういえばおじいさまからも\x01",
            "そんな話を聞いていたわね。\x02\x03",

            "#00100F仮にもマフィアが保有していた物件だし\x01",
            "放っておくわけにはいかないからって、\x01",
            "早々に委託が決定されたらしいわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0x101,
        (
            "#5P#00003Fなるほどな……\x02\x03",

            "#00000Fえっと、失礼しました、\x01",
            "俺たちはクロスベル警察の者です。\x02\x03",

            "今はちょっと市内を\x01",
            "巡回しているところでして。\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0xE,
        (
            "#12Pああ、警察の人たちだったか。\x01",
            "こんな所までお疲れ様だね。\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0x109,
        (
            "#5P#10100Fえっと、それじゃあ今日は\x01",
            "このビルの定期的な点検か何かに？\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0xE,
        (
            "#12Pいや……\x01",
            "実は、このビルは近いうちに、\x01",
            "売りに出されることになってね。\x02",
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
        "#5P#00005Fこの物件が売りに……？\x02",
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0xE,
        (
            "#12Pああ、実は前々からいくつかの企業に\x01",
            "入居希望を出されていてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0xE,
        (
            "#12P今日もその一つが交渉に来る予定だから、\x01",
            "ここで待たせてもらうんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0x109,
        (
            "#5P#10105F元マフィアの物件に\x01",
            "入居希望を出す企業ですか……\x02\x03",

            "#10106Fその、こう言ってはなんですけど……\x01",
            "大丈夫#6R㈲　㈲　㈲#なんでしょうか？\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0xE,
        "#12Pまあ、私たちも多少は不安だが……\x02",
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0xE,
        (
            "#12Pなんせ、これほどのビルだからね。\x01",
            "管理費だけでもバカにならない。\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0xE,
        (
            "#12P誰かに引き受けてもらえるなら、\x01",
            "私たちも断る理由はないのさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0x105,
        (
            "#5P#10303Fまあ、業者としては\x01",
            "さっさと手放したいってのは\x01",
            "当たり前の感情だろうね。\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0x101,
        (
            "#5P#00003Fああ、気にはなるけど……\x02\x03",

            "#00000Fお邪魔してもなんだし、\x01",
            "俺たちは行くとしようか。\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0x102,
        "#5P#00103Fええ……そうしましょう。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrFlags(0xE, 0x8)
    SetChrPos(0x0, 90, 0, 80, 180)
    SetScenarioFlags(0x139, 1)
    EventEnd(0x5)
    Return()

    # Function_10_2C25 end

    def Function_11_34B8(): pass

    label("Function_11_34B8")

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

    def lambda_3602():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3602)

    def lambda_3613():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_3613)

    def lambda_3624():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_3624)

    def lambda_3635():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_3635)

    def lambda_3646():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_3646)

    def lambda_3657():
        OP_95(0xFE, -600, 0, 34200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3657)

    def lambda_3671():
        OP_95(0xFE, 600, 0, 34200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3671)

    def lambda_368B():
        OP_95(0xFE, 0, 0, 36000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_368B)

    def lambda_36A5():
        OP_95(0xFE, -1200, 0, 33000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_36A5)

    def lambda_36BF():
        OP_95(0xFE, 1200, 0, 33000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_36BF)
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
        "おや、あなたたちは……\x02",
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0xC,
        "おお、ランドルフ隊長じゃねえか！\x02",
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0xC,
        "はは、今日も来たのかよ？\x02",
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0x101,
        (
            "#6P#00001F（赤い星座の猟兵……\x01",
            "　ランディの知ってる顔みたいだな。）\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0x104,
        (
            "#12P#00303F……ザックス、新しい根城の居心地は\x01",
            "随分いいみてえじゃねえか。\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0xC,
        "ハハ、おかげ様でな。\x02",
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0xC,
        (
            "歓楽街の《ノイエ＝ブラン》支店にも近いし、\x01",
            "なかなか便利に使わせてもらってるぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0x104,
        (
            "#12P#00303Fハッ……相変わらずご苦労なこった。\x02\x03",

            "#00301F……今日も叔父貴たちはいねえのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0xC,
        (
            "ああ、今日もお頭とお嬢は\x01",
            "所用で出かけちまってるとこでな。\x02",
        )
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0xC,
        (
            "何か伝言があんなら\x01",
            "俺から伝えておくが、どうする？\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0x104,
        "#12P#00303F……いい、邪魔したな。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 500)

    #C0138
    ChrTalk(
        0x104,
        "#5P#00300F行くぞ、ロイド。\x02",
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0x101,
        "#6P#00005Fあ、ああ……\x02",
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0xD,
        "どうも、お疲れ様でした。\x02",
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0xC,
        "クク、またな隊長。\x02",
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
            "#00303F……フン、\x01",
            "また居留守を使われたみてぇだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0x102,
        (
            "#12P#00105F“また”って……\x01",
            "最近訪ねたことがあったの？\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x104, 0xB4, 0x1F4)
    Sleep(300)

    #C0144
    ChrTalk(
        0x104,
        (
            "#00303F話があるとか抜かしながら\x01",
            "全然、音沙汰がなかったからな。\x02\x03",

            "#00301Fしかしどうやら、\x01",
            "こっちから会いに行っても\x01",
            "姿を現すつもりはないらしい。\x02",
        )
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0x105,
        (
            "#12P#10300Fふむ、近いうちに\x01",
            "なんらかのコンタクトを\x01",
            "とってくるかもしれないね。\x02",
        )
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0x109,
        (
            "#11P#10106Fでも、そうなると……\x01",
            "赤い星座については地道に\x01",
            "聞き込みをするしかなさそうですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0x101,
        (
            "#6P#00000Fああ、俺たちは支援要請を片付けながら\x01",
            "各地を回ってみるとしよう。\x02",
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

    # Function_11_34B8 end

    def Function_12_3D07(): pass

    label("Function_12_3D07")

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
            "#00003F……鍵がかかってるみたいだな。\x02\x03",

            "#00001F一課の捜査も一通り終わって、\x01",
            "中には誰もいないはずだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0x102,
        (
            "#00108Fあんな飛行艇で逃げ去って、\x01",
            "今はどこに潜伏してるのかしら……\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0x109,
        (
            "#12P#10101F彼らについては、警備隊も\x01",
            "厳重に警戒しているみたいです。\x02",
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
        "#12P#00200Fランディさん……\x02",
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
        "#6P#10308F……大丈夫かい？\x02",
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
            "#00304F……ハハ、心配すんな。\x02\x03",

            "#00301Fだが……今度会ったら絶対に\x01",
            "決着をつけてやらねえとな。\x02",
        )
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0x101,
        "#00003Fああ……そうだな。\x02",
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

    # Function_12_3D07 end

    def Function_13_401E(): pass

    label("Function_13_401E")

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
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_40E2")
    SetChrFlags(0x9, 0x8000)
    SetChrFlags(0x8, 0x8000)
    EndChrThread(0x8, 0xFF)
    BeginChrThread(0x8, 0, 0, 0)
    SetChrPos(0x9, -8800, 0, 3100, 90)
    SetChrPos(0x8, -7300, 0, 3100, 270)

    label("loc_40E2")

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

    # Function_13_401E end

    def Function_14_4157(): pass

    label("Function_14_4157")

    SetChrPos(0xFE, 18000, 0, 500, 0)
    OP_9F(0x0, 0xFE)
    OP_9F(0x1, -37000, 0, 500)
    OP_9F(0x2, 0xFE, 5000, 0x6)
    Return()

    # Function_14_4157 end

    def Function_15_4184(): pass

    label("Function_15_4184")

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

    # Function_15_4184 end

    def Function_16_41BB(): pass

    label("Function_16_41BB")

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
        "#00108F#6P（……あ……）\x02",
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
        "#00311F#2753V#6P#30W──叔父貴、シャーリィ。\x02",
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
            "#3941V#5P#20Wあははっ。\x01",
            "久しぶりだね、ランディ兄！\x02",
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
            "#3834V#11P#30W２年ぶりか。\x01",
            "変わってないようだな。\x02",
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

    def lambda_46EB():
        OP_9B(0x0, 0x101, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_46EB)
    Sleep(50)

    def lambda_4703():
        OP_9B(0x0, 0x102, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_4703)
    Sleep(50)

    def lambda_471B():
        OP_9B(0x0, 0x105, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_471B)
    Sleep(50)

    def lambda_4733():
        OP_9B(0x0, 0x109, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_4733)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x109, 0)
    OP_0D()

    #C0161
    ChrTalk(
        0x101,
        "#00007F#6P……ランディ……！\x02",
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0x109,
        "#10111F#6P#Nき、昨日の人たち……！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0163
    ChrTalk(
        0x105,
        "#10303F#6P#N怪しい連中が揃い踏みか。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0164
    ChrTalk(
        0x11,
        (
            "#03509F#5Pハハ、やっぱり彼氏、\x01",
            "このオッサンの身内だったか。\x02\x03",

            "#03502Fそっくりな髪の色だったから\x01",
            "まさかとは思ったけどよ～。\x02",
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
            "#00013F#6Pレクター大尉……\x01",
            "どうして貴方がここに。\x02",
        )
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0x102,
        (
            "#00101F#6P今回の買収について\x01",
            "何か関係しているんですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0x11,
        (
            "#03504F#5Pああ、ちょいと裏工作をな。\x02\x03",

            "#03510Fいや～、何とか黒月のメガネを\x01",
            "出し抜けてよかったぜェ。\x02",
        )
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0x10,
        (
            "#04609F#11Pふふっ、楽しみだなぁ！\x02\x03",

            "#04602F東方人街の時は撤退したけど\x01",
            "今度は思いっきり遊べそう！\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x0, 0x1F4)
    Sleep(100)

    #C0170
    ChrTalk(
        0x101,
        "#00005F#6P東方人街……\x02",
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0x104,
        (
            "#00303F#6P去年カルバードで\x01",
            "黒月とやらかした“戦争”か。\x02\x03",

            "#00311F──なあ、叔父貴。\x01",
            "どうしてクロスベルに来た？\x02\x03",

            "いったい何をするつもりだ？\x02",
        )
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0xF,
        (
            "#04504F#11Pクク……\x01",
            "ビジネスに決まってるだろう。\x02\x03",

            "#04500Fそれよりも、ランドルフ。\x01",
            "貴様に伝えておくことがある。\x02\x03",

            "──兄貴が逝#2Rい#ったぞ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0173
    ChrTalk(
        0x104,
        "#00305F#6P#40W#2S………え………………\x02",
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
            "#04503F#11P半年ほど前だ。\x02\x03",

            "《西風》の頭と相討ちだった。\x02",
        )
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0x10,
        (
            "#04602F#11P長年の宿敵同士である\x01",
            "《闘神》と《猟兵王》の決着！\x02\x03",

            "#04612Fもう、ホント凄かったんだから！\x02",
        )
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0x104,
        (
            "#00308F#6P#40W…………………………………\x02\x03",

            "#00304F#40W……はは……そうか……\x02\x03",

            "#30Wあのクソ親父……最後まで\x01",
            "戦いながら逝ったってことかよ。\x02\x03",

            "#00300F#40W……満足そうだっただろ？\x02",
        )
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0x10,
        (
            "#04602F#11Pうん！\x01",
            "すっごく楽しそうだった！\x02\x03",

            "#04606Fいいなぁ、シャーリィも\x01",
            "あんな相手が欲しいよ～。\x02",
        )
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0xF,
        (
            "#04504F#11Pま、兄貴も悔いは無いだろう。\x02\x03",

            "#04501F──どこぞで迷ってる\x01",
            "不肖の息子のこと以外はな。\x02",
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
            "#04504F#5P休暇は終わりだ、ランドルフ。\x02\x03",

            "#04502Fいずれ話があるから\x01",
            "身体を開けておくがいい。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0182
    ChrTalk(
        0x10,
        "#04609F#11Pまたねー、ランディ兄！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0183
    ChrTalk(
        0x11,
        "#03509F#5Pそんじゃ、お疲れさん～。\x02",
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
        "#00108F#6P#N……ランディ……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0185
    ChrTalk(
        0x109,
        "#10113F#6P#Nランディ先輩……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0186
    ChrTalk(
        0x101,
        "#00008F#6Pあの２人、ランディの……？\x02",
    )

    CloseMessageWindow()
    OP_64(0x104)
    Sleep(500)

    #C0187
    ChrTalk(
        0x104,
        "#00306F#5P#30Wああ……\x02",
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
            "#00303F#11P#30W《赤い星座》の副団長、\x01",
            "シグムント・オルランド。\x02\x03",

            "その娘で部隊長の一人、\x01",
            "シャーリィ・オルランド。\x02",
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
            "#00311F#11P#30W俺の叔父貴と従妹で……\x01",
            "──最強最悪の戦鬼どもだ。\x02",
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
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x67, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_50F9")
    Jump("loc_50FE")

    label("loc_50F9")

    OP_29(0x67, 0x4, 0x40)

    label("loc_50FE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6D, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_510F")
    Jump("loc_5114")

    label("loc_510F")

    OP_29(0x6D, 0x4, 0x40)

    label("loc_5114")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6E, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_5125")
    Jump("loc_512A")

    label("loc_5125")

    OP_29(0x6E, 0x4, 0x40)

    label("loc_512A")

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

    # Function_16_41BB end

    def Function_17_520E(): pass

    label("Function_17_520E")

    OP_95(0xFE, 0, 0, 42270, 2000, 0x0)
    OP_95(0xFE, 0, 300, 43640, 2000, 0x0)
    Sound(103, 0, 100, 0)
    OP_71(0x2, 0x1, 0xA, 0x1, 0x0)
    Sleep(500)

    def lambda_5250():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_5250)
    OP_9B(0x0, 0xFE, 0x0, 0x9C4, 0x7D0, 0x0)
    Return()

    # Function_17_520E end

    def Function_18_526C(): pass

    label("Function_18_526C")

    Return()

    # Function_18_526C end

    def Function_19_526D(): pass

    label("Function_19_526D")

    Sleep(1500)
    OP_93(0xFE, 0x2D, 0x1F4)
    Sleep(500)
    OP_95(0xFE, 0, 0, 42270, 2000, 0x0)
    OP_95(0xFE, 0, 300, 43640, 2000, 0x0)

    def lambda_52A7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_52A7)
    OP_9B(0x0, 0xFE, 0x0, 0x9C4, 0x7D0, 0x0)
    Return()

    # Function_19_526D end

    def Function_20_52C3(): pass

    label("Function_20_52C3")

    Return()

    # Function_20_52C3 end

    def Function_21_52C4(): pass

    label("Function_21_52C4")

    Sleep(2000)
    OP_93(0xFE, 0x2D, 0x1F4)
    OP_95(0xFE, 0, 0, 42270, 2000, 0x0)
    OP_95(0xFE, 0, 300, 43640, 2000, 0x0)

    def lambda_52FB():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_52FB)
    OP_9B(0x0, 0xFE, 0x0, 0x9C4, 0x7D0, 0x0)
    Sound(104, 0, 100, 0)
    OP_71(0x2, 0xA, 0x0, 0x1, 0x0)
    Return()

    # Function_21_52C4 end

    def Function_22_5329(): pass

    label("Function_22_5329")

    Return()

    # Function_22_5329 end

    def Function_23_532A(): pass

    label("Function_23_532A")

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
    OP_8E(0xF, "シグムント")
    OP_52(0xF, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x8000)
    SetChrChipByIndex(0x10, 0x1F)
    SetChrSubChip(0x10, 0x0)
    SetChrPos(0x10, -2500, 6500, 8100, 20)
    OP_8E(0x10, "シャーリィ")
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
            "#04602F#3973V#5P#30Wうっわーっ！\x01",
            "あのビル、とんでもないね～！\x02\x03",

            "#04612F#3974Vねえねえ、シャーリィたちで\x01",
            "ブッ壊せたりしないかな！？\x02",
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
            "#04504F#5Pフフ……\x01",
            "気持ちはわかるが止めとけ。\x02\x03",

            "#04500Fいずれあのビルにも\x01",
            "役立ってもらうつもりだからな。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10, 0xF, 500)

    #C0192
    ChrTalk(
        0x10,
        (
            "#04606F#11Pむー、残念。\x02\x03",

            "#04602Fまあいいや、\x01",
            "街の方をブラついてくるね？\x02\x03",

            "#04612Fあのビルのせいで\x01",
            "すごく賑わってるみたいだし♪\x02",
        )
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0xF,
        "#04504F#5Pああ、行ってくるがいい。\x02",
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

    def lambda_56D9():
        OP_9D(0xFE, 0x0, 0x1450, 0x1DB0, 0x1F4, 0x7D0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_56D9)
    Sleep(300)

    def lambda_56F9():

        label("loc_56F9")

        TurnDirection(0xFE, 0x10, 500)
        Yield()
        Jump("loc_56F9")

    QueueWorkItem2(0xF, 2, lambda_56F9)

    def lambda_570B():

        label("loc_570B")

        TurnDirection(0xFE, 0x10, 500)
        Yield()
        Jump("loc_570B")

    QueueWorkItem2(0x12, 2, lambda_570B)

    def lambda_571D():

        label("loc_571D")

        TurnDirection(0xFE, 0x10, 500)
        Yield()
        Jump("loc_571D")

    QueueWorkItem2(0xC, 2, lambda_571D)
    WaitChrThread(0x10, 1)
    Sound(62, 0, 100, 0)
    OP_92(0x10, 0x0, 0x1004, 0x1F4)

    def lambda_5746():
        OP_98(0xFE, 0x0, 0x0, 0xFFFFFC18, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_5746)
    WaitChrThread(0x10, 1)
    Sound(844, 0, 50, 0)
    SetChrSubChip(0x10, 0x2)

    def lambda_576E():
        OP_9D(0xFE, 0x0, 0x0, 0xE10, 0x1F4, 0x7D0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_576E)
    WaitChrThread(0x10, 1)
    EndChrThread(0xF, 0x2)
    EndChrThread(0x12, 0x2)
    EndChrThread(0xC, 0x2)
    SetChrFlags(0x10, 0x80)
    Sleep(300)

    #C0194
    ChrTalk(
        0xC,
        "#5Pはは……さすがお嬢だぜ。\x02",
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0xC,
        (
            "#5Pよっぽどあのビルが\x01",
            "気に入ったんスかねぇ？\x02",
        )
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0xF,
        (
            "#04504F#5Pフフ、それもあるだろう。\x02\x03",

            "#04502Fだがそれよりも──\x01",
            "血の予感に酔ってるんだろうさ。\x02",
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
            "#12P……なるほど。\x01",
            "シャーリィ様らしいかと。\x02",
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
            "#04504F#5Pクク……さすがは俺の娘。\x02\x03",

            "#04502Fどうやら明日はたっぷりと\x01",
            "愉しませてやれそうだ。\x02",
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

    # Function_23_532A end

    def Function_24_595B(): pass

    label("Function_24_595B")

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

    def lambda_5B37():
        OP_95(0xFE, 10, 0, 39370, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5B37)
    Sleep(30)

    def lambda_5B54():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5B54)
    Sleep(30)

    def lambda_5B6C():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5B6C)
    Sleep(50)

    def lambda_5B84():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_5B84)
    Sleep(30)

    def lambda_5B9C():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_5B9C)

    def lambda_5BB1():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_5BB1)
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

    def lambda_5C2F():
        OP_95(0xFE, 10, 0, 43000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5C2F)
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

    def lambda_5C94():
        OP_95(0xFE, 0, 0, 45000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5C94)

    def lambda_5CAE():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5CAE)
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

    # Function_24_595B end

    def Function_25_5D24(): pass

    label("Function_25_5D24")

    OP_95(0xFE, 0, 0, 650, 5000, 0x0)
    OP_95(0xFE, 0, 0, 6000, 5000, 0x0)
    Return()

    # Function_25_5D24 end

    def Function_26_5D4D(): pass

    label("Function_26_5D4D")


    def lambda_5D52():
        OP_95(0xFE, 0, 0, 39370, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5D52)
    WaitChrThread(0xFE, 1)

    def lambda_5D70():
        OP_95(0xFE, 0, 0, 43670, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5D70)
    WaitChrThread(0xFE, 1)

    def lambda_5D8E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_5D8E)

    def lambda_5D9F():
        OP_95(0xFE, 0, 0, 45000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5D9F)
    Return()

    # Function_26_5D4D end

    def Function_27_5DB5(): pass

    label("Function_27_5DB5")

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
            "#00001F#5Pもう……\x01",
            "誰もいないみたいだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0x103,
        (
            "#00208F#6P警察でも施錠だけして\x01",
            "放置していたはずですが。\x02",
        )
    )

    CloseMessageWindow()

    #C0202
    ChrTalk(
        0x104,
        (
            "#00301F#12Pわざわざ呼びつけたって事は\x01",
            "ピッキングでもしやがったか？\x02",
        )
    )

    CloseMessageWindow()

    #C0203
    ChrTalk(
        0x102,
        "#00103F#11Pとにかく入ってみましょう。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, 0, 0, 34000, 0)
    OP_69(0xFF, 0x0)
    SetScenarioFlags(0x182, 3)
    EventEnd(0x5)
    Return()

    # Function_27_5DB5 end

    def Function_28_5F4C(): pass

    label("Function_28_5F4C")

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
            "#02101Fうーん……\x01",
            "いよいよ動き始めたわね。\x02\x03",

            "#02103F交渉している事くらいなら\x01",
            "記事にしてもＯＫかしら？\x02\x03",

            "#02101F共和国派からの圧力も\x01",
            "最近、減ってはいるけど……\x02",
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
            "#00005Fグレイスさん、\x01",
            "何をしているんですか？\x02",
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

    def lambda_61C8():
        OP_93(0x14, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_61C8)

    def lambda_61D5():
        OP_95(0x101, 850, 0, 1360, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_61D5)
    Sleep(100)

    def lambda_61F2():
        OP_9B(0x0, 0x102, 0x0, 0x1388, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_61F2)
    Sleep(100)

    def lambda_620A():
        OP_95(0x105, 0, 0, 360, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_620A)
    Sleep(100)

    def lambda_6227():
        OP_9B(0x0, 0x109, 0x0, 0x1194, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_6227)
    WaitChrThread(0x109, 1)

    def lambda_6240():
        OP_95(0x109, 1300, 0, 260, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_6240)
    Sleep(100)
    OP_6F(0x79)
    WaitChrThread(0x102, 1)

    def lambda_6263():
        OP_95(0x102, -600, 0, 1560, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6263)
    WaitChrThread(0x101, 1)

    def lambda_6281():
        TurnDirection(0x101, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6281)

    def lambda_628E():
        OP_93(0x14, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_628E)
    WaitChrThread(0x109, 1)

    def lambda_629F():
        TurnDirection(0x109, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_629F)
    Sleep(200)
    WaitChrThread(0x105, 1)

    def lambda_62B3():
        TurnDirection(0x105, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_62B3)
    Sleep(200)
    WaitChrThread(0x102, 1)

    def lambda_62C7():
        TurnDirection(0x102, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_62C7)
    WaitChrThread(0x105, 1)
    Call(0, 30)
    Return()

    # Function_28_5F4C end

    def Function_29_62D7(): pass

    label("Function_29_62D7")

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
            "#12P#02101Fうーん……\x01",
            "いよいよ動き始めたわね。\x02\x03",

            "#02103F交渉している事くらいなら\x01",
            "記事にしてもＯＫかしら？\x02\x03",

            "#02101F共和国派からの圧力も\x01",
            "最近、減ってはいるけど……\x02",
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
            "#00005Fグレイスさん、\x01",
            "何をしているんですか？\x02",
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

    def lambda_6557():
        TurnDirection(0x14, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_6557)

    def lambda_6564():
        OP_95(0x101, 850, 0, 1360, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6564)
    Sleep(100)

    def lambda_6581():
        OP_95(0x102, -600, 0, 1560, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6581)
    Sleep(100)

    def lambda_659E():
        OP_95(0x109, 1300, 0, 260, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_659E)
    Sleep(100)

    def lambda_65BB():
        OP_95(0x105, 0, 0, 360, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_65BB)
    Sleep(1000)

    def lambda_65D8():
        OP_93(0x14, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_65D8)
    OP_6F(0x79)
    WaitChrThread(0x101, 1)

    def lambda_65EB():
        TurnDirection(0x101, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_65EB)

    def lambda_65F8():
        OP_93(0x14, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_65F8)
    WaitChrThread(0x102, 1)

    def lambda_6609():
        TurnDirection(0x102, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6609)
    WaitChrThread(0x109, 1)

    def lambda_661A():
        TurnDirection(0x109, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_661A)
    WaitChrThread(0x105, 1)

    def lambda_662B():
        TurnDirection(0x105, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_662B)
    WaitChrThread(0x105, 1)
    Call(0, 30)
    Return()

    # Function_29_62D7 end

    def Function_30_663B(): pass

    label("Function_30_663B")

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
            "な、なんだ……\x01",
            "ロイド君たちじゃないの。\x02\x03",

            "そっか、特務支援課、\x01",
            "いよいよ再始動ってわけね？\x02",
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
        "#6P#00000Fはい、おかげさまで。\x02",
    )

    CloseMessageWindow()

    #C0210
    ChrTalk(
        0x102,
        (
            "#6P#00100Fティオちゃんとランディは\x01",
            "後から合流なんですけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0211
    ChrTalk(
        0x14,
        (
            "#02100Fそっか、ちょっと残念ね。\x02\x03",

            "#02106Fしっかし、まさかワジ君が\x01",
            "支援課に入っちゃうなんてね～。\x02\x03",

            "#02102Fお姉さん、さすがに魂消#5R たまげ#たわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0212
    ChrTalk(
        0x105,
        (
            "#6P#10300Fフフ、驚いてくれて何よりだ。\x02\x03",

            "#10304F何だったら特集記事を\x01",
            "組んでくれても構わないけどね。\x02",
        )
    )

    CloseMessageWindow()

    #C0213
    ChrTalk(
        0x101,
        "#11P#00006Fあのな……\x02",
    )

    CloseMessageWindow()
    OP_93(0x14, 0xB4, 0x0)

    #C0214
    ChrTalk(
        0x14,
        (
            "#02109Fふふっ、楽しそうじゃない。\x02\x03",

            "#02106Fできれば色々話したいんだけど\x01",
            "今ちょーっと取り込んでてね。\x02\x03",

            "#02102Fそれが終わったらゆっくりと──\x02",
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
        "青年の声",
        "#Nおや、これは珍しい顔触れだ。\x02",
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

    def lambda_6A7B():
        OP_98(0x15, 0x0, 0x0, 0xFFFFFC18, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_6A7B)
    Sleep(50)

    def lambda_6A98():
        OP_98(0x16, 0x0, 0x0, 0xFFFFFC18, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_6A98)
    Sleep(50)
    OP_0D()

    #C0216
    ChrTalk(
        0x101,
        "#12P#N#00005Fあ……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0217
    ChrTalk(
        0x102,
        "#3P#N#00101Fツァオ支社長……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0218
    ChrTalk(
        0x14,
        "#12P#N#02106F……しまった。\x02",
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
            "お久しぶりですね。\x01",
            "ロイドさん、エリィさん。\x02\x03",

            "それと──ワジ君に\x01",
            "ノエル曹長でよろしいですか？\x02",
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
        "#6P#10111Fど、どうしてそれを……！\x02",
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0x105,
        (
            "#6P#10302Fへえ……\x01",
            "さすが大した情報網だね。\x02",
        )
    )

    CloseMessageWindow()

    #C0222
    ChrTalk(
        0x15,
        (
            "#03204Fフフ、他ならぬ\x01",
            "特務支援課のことですから。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x15, 0x10E, 0x1F4)

    #C0223
    ChrTalk(
        0x15,
        (
            "#03200Fしかし、まさかグレイスさんに\x01",
            "こちらの動きを掴まれていたとは。\x02\x03",

            "#03209Fさすがは天下の\x01",
            "クロスベル・タイムズですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0224
    ChrTalk(
        0x14,
        (
            "#5P#02109Fい、いや～……\x01",
            "偶然ですよ、そう偶然！\x02",
        )
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0x101,
        (
            "#6P#00001F……一体、こんな場所で\x01",
            "何をなさっているんですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0x102,
        (
            "#6P#00101Fルバーチェの跡地に\x01",
            "何か御用だったんですか？\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x15, 0xB4, 0x1F4)

    #C0227
    ChrTalk(
        0x15,
        (
            "#03200Fハハ、決まっているでしょう？\x02\x03",

            "#03204Fこのまま寝かせておくには\x01",
            "余りにもったいない土地です。\x02\x03",

            "#03202Fならば我が社が有効に\x01",
            "活用させてもらおうと思いまして。\x02",
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
            "#03203Fフフ、マフィアの保有物件など\x01",
            "普通なら手を出しにくいでしょう。\x02\x03",

            "#03210Fしかし我々ならば多少は#6R㈲　㈲　㈲#\x01",
            "その手の物件にも慣れています。\x02\x03",

            "#03204F委託業者にしても\x01",
            "月々の管理費は頭が痛いでしょうし、\x01",
            "良い取引が出来そうですよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0230
    ChrTalk(
        0x101,
        "#6P#00010Fくっ……\x02",
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0x14,
        (
            "#5P#02101F……えっと、ツァオさん。\x01",
            "そうした情報は記事にしても？\x02",
        )
    )

    CloseMessageWindow()

    #C0232
    ChrTalk(
        0x15,
        (
            "#03200Fああ、構いませんよ。\x01",
            "やましい事ではありませんし。\x02\x03",

            "#03204F憶測で決め付けるのは\x01",
            "勘弁していただきたい所ですが。\x02",
        )
    )

    CloseMessageWindow()

    #C0233
    ChrTalk(
        0x14,
        (
            "#5P#02109Fあ、あはは……\x01",
            "もちろん心得ていますわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0234
    ChrTalk(
        0x15,
        (
            "#03200Fフフ、それでは失礼します。\x02\x03",

            "ロイドさん、何かあれば\x01",
            "我が社にいらしてください。\x02\x03",

            "#03204F……行きますよ、ラウ。\x02",
        )
    )

    CloseMessageWindow()

    #C0235
    ChrTalk(
        0x16,
        "は。\x02",
    )

    CloseMessageWindow()
    OP_93(0x102, 0x0, 0x0)

    def lambda_7259():
        OP_9B(0x1, 0x101, 0xB4, 0x1F4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7259)
    Sleep(50)

    def lambda_7271():
        OP_9B(0x1, 0x102, 0xB4, 0x1F4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7271)

    def lambda_7286():
        OP_9B(0x1, 0x109, 0xB4, 0x1F4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_7286)
    Sleep(50)

    def lambda_729E():
        OP_9B(0x1, 0x105, 0xB4, 0x1F4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_729E)
    Sleep(50)

    def lambda_72B6():
        OP_95(0x15, -2500, 0, 1660, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_72B6)
    Sleep(500)
    OP_96(0x16, 0x0, 0x0, 0x898, 0x7D0, 0x0)

    def lambda_72E7():
        OP_95(0x15, -12000, 0, 1660, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_72E7)

    def lambda_7301():
        OP_95(0x16, -12000, 0, 1560, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_7301)

    def lambda_731B():
        OP_93(0x101, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_731B)
    Sleep(50)

    def lambda_732B():
        OP_93(0x102, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_732B)
    Sleep(50)

    def lambda_733B():
        OP_93(0x109, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_733B)
    Sleep(50)

    def lambda_734B():
        OP_93(0x105, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_734B)
    Sleep(50)

    def lambda_735B():
        OP_93(0x14, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_735B)
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
            "#12P#10101Fす、凄い人でしたね。\x02\x03",

            "#10106Fヘビに睨まれたカエルみたいな\x01",
            "気分だったんですけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0238
    ChrTalk(
        0x102,
        "#12P#00103Fそうね……\x02",
    )

    CloseMessageWindow()

    #C0239
    ChrTalk(
        0x105,
        (
            "#6P#10300F黒月きっての若手幹部、\x01",
            "《白蘭竜》のツァオ・リーか。\x02\x03",

            "#10306F噂以上のキレ者みたいだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0240
    ChrTalk(
        0x101,
        "#12P#00003Fああ、相変わらずだな。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_68(240, 1750, 1140, 3000)
    MoveCamera(326, 26, 0, 3000)
    OP_6E(600, 3000)
    SetCameraDistance(12930, 3000)

    def lambda_7553():
        OP_93(0x14, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_7553)

    def lambda_7560():
        OP_95(0x101, 500, 0, 2660, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7560)
    Sleep(100)

    def lambda_757D():
        OP_95(0x102, -710, 0, 1990, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_757D)
    Sleep(100)

    def lambda_759A():
        OP_95(0x109, 900, 0, 1300, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_759A)
    Sleep(100)

    def lambda_75B7():
        OP_95(0x105, -270, 0, 760, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_75B7)
    WaitChrThread(0x101, 1)

    def lambda_75D5():
        TurnDirection(0x101, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_75D5)
    WaitChrThread(0x102, 1)

    def lambda_75E6():
        TurnDirection(0x102, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_75E6)
    WaitChrThread(0x109, 1)

    def lambda_75F7():
        TurnDirection(0x109, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_75F7)
    WaitChrThread(0x105, 1)

    def lambda_7608():
        TurnDirection(0x105, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_7608)
    OP_6F(0x79)
    Sleep(100)

    #C0241
    ChrTalk(
        0x101,
        (
            "#12P#00001F──グレイスさん。\x01",
            "黒月がこのルバーチェ跡地を？\x02",
        )
    )

    CloseMessageWindow()

    #C0242
    ChrTalk(
        0x14,
        (
            "#5P#02101Fええ、倉庫なんかも合わせて\x01",
            "まとめて買い取るつもりみたいね。\x02\x03",

            "#02103Fもし黒月がここを押さえたら\x01",
            "クロスベルの裏社会は\x01",
            "完全に掌握される事になる……\x02\x03",

            "#02101F厄介なことになりそうだわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0243
    ChrTalk(
        0x101,
        (
            "#12P#00003F……同感です。\x02\x03",

            "#00006Fしかし、聞き込みに来たところで\x01",
            "えらい場面に出くわしたな。\x02",
        )
    )

    CloseMessageWindow()

    #C0244
    ChrTalk(
        0x102,
        (
            "#6P#00101Fそうね、これも一課に\x01",
            "伝えた方がいいかもしれないわ。\x02",
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
            "#5P#02105Fあれ、あなた達もツァオの\x01",
            "動向を調べに来たんじゃないの？\x02\x03",

            "#02102Fもしかして別件を追ってる？\x02",
        )
    )

    CloseMessageWindow()

    #C0246
    ChrTalk(
        0x101,
        (
            "#12P#00012Fいえ、その……\x02\x03",

            "#00003F（そうだな、グレイスさんは\x01",
            "  確か面識はあったみたいだし……）\x02\x03",

            "#00001F……実は、以前グレイスさんも\x01",
            "会っている人を捜しているんです。\x02\x03",

            "カジノで鉱員の人を負かした\x01",
            "レクターっていう人なんですけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0247
    ChrTalk(
        0x14,
        (
            "#5P#02105Fああ、そうなんだ？\x02\x03",

            "#02103Fあの子なら、龍老飯店で\x01",
            "さっき見かけたばかりだけど。\x02",
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
        "#12P#00011Fええっ！？\x02",
    )

    CloseMessageWindow()

    #C0249
    ChrTalk(
        0x102,
        "#6P#00105Fほ、本当ですか！？\x02",
    )

    CloseMessageWindow()

    #C0250
    ChrTalk(
        0x14,
        (
            "#5P#02100Fええ、例のバカンスルックで\x01",
            "呑気そうに食事してたわね。\x02\x03",

            "#02103F取材で急いでたから\x01",
            "声を掛けそびれちゃったけど……\x02",
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
            "#5P#02105Fって、こうしちゃいられない。\x02\x03",

            "#02101Fせめてツァオからもう少し\x01",
            "突っ込んだ情報を聞き出さないと。\x02\x03",

            "#02109F……じゃあね！\x01",
            "また今度、食事でもしましょう！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_7B73():
        OP_93(0x101, 0x10E, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7B73)

    def lambda_7B80():
        OP_93(0x102, 0x10E, 0x12C)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7B80)

    def lambda_7B8D():
        OP_93(0x109, 0x10E, 0x12C)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_7B8D)

    def lambda_7B9A():
        OP_93(0x105, 0x10E, 0x12C)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_7B9A)
    OP_95(0x14, -2000, 0, 2000, 5000, 0x0)
    OP_95(0x14, -15000, 0, 2000, 5000, 0x0)
    WaitChrThread(0x14, 1)
    Sleep(100)
    SetChrFlags(0x14, 0x80)
    OP_0D()

    #C0252
    ChrTalk(
        0x101,
        "#00012Fあ、相変わらずだな……\x02",
    )

    CloseMessageWindow()

    def lambda_7BFF():
        OP_93(0x105, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_7BFF)
    Sleep(100)

    #C0253
    ChrTalk(
        0x105,
        (
            "#6P#10300Fでも、思わぬところで\x01",
            "目撃情報が入ったじゃない。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_7C4E():
        OP_93(0x101, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7C4E)

    def lambda_7C5B():
        OP_93(0x102, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7C5B)

    def lambda_7C68():
        OP_93(0x109, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_7C68)
    Sleep(100)

    #C0254
    ChrTalk(
        0x102,
        (
            "#5P#00100Fええ、さっそく\x01",
            "《龍老飯店》に行きましょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0255
    ChrTalk(
        0x109,
        "#12P#10100F了解です！\x02",
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

    # Function_30_663B end

    def Function_31_7D2F(): pass

    label("Function_31_7D2F")

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

    def lambda_7E01():
        OP_95(0x101, 15750, 0, 1500, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7E01)
    Sleep(50)

    def lambda_7E1E():
        OP_95(0x102, 16750, 0, 1200, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7E1E)
    Sleep(50)

    def lambda_7E3B():
        OP_95(0x109, 17750, 0, 1500, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_7E3B)
    Sleep(50)

    def lambda_7E58():
        OP_95(0x105, 18750, 0, 2350, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_7E58)
    Sleep(50)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x101, 1)

    def lambda_7E83():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7E83)
    WaitChrThread(0x102, 1)

    def lambda_7E94():
        OP_93(0x102, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7E94)
    WaitChrThread(0x109, 1)

    def lambda_7EA5():
        OP_93(0x109, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_7EA5)
    WaitChrThread(0x105, 1)

    def lambda_7EB6():
        OP_93(0x105, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_7EB6)
    WaitChrThread(0x105, 1)

    #C0256
    ChrTalk(
        0x109,
        "#12P#10111Fホントに降りたんだ……\x02",
    )

    CloseMessageWindow()

    #C0257
    ChrTalk(
        0x105,
        (
            "#12P#10302Fフフ、わざわざ\x01",
            "仕込んでいたのかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0258
    ChrTalk(
        0x102,
        "#6P#00106Fと、とにかく追いましょう。\x02",
    )

    CloseMessageWindow()

    #C0259
    ChrTalk(
        0x101,
        (
            "#6P#00001Fああ、通りにいる人たちに\x01",
            "片っ端から聞くしかない……！\x02",
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

    # Function_31_7D2F end

    def Function_32_7FC8(): pass

    label("Function_32_7FC8")

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
            "#00106Fふう、何だか長くなっちゃったけど、\x01",
            "これで『釣皇倶楽部』の調査は完了ね。\x02",
        )
    )

    CloseMessageWindow()

    #C0261
    ChrTalk(
        0x101,
        "#00000Fああ、そういうことになるな。\x02",
    )

    CloseMessageWindow()
    OP_29(0x6A, 0x1, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_81F8")
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
            "◆「調査状況は？（テスト用）\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【変更しない】\x01",                  # 0
            "【まだ残りがある】\x01",              # 1
            "【６箇所の確認が終わった】\x01",      # 2
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
        (0, "loc_81D1"),
        (1, "loc_81D6"),
        (2, "loc_81E7"),
        (SWITCH_DEFAULT, "loc_81F8"),
    )


    label("loc_81D1")

    Jump("loc_81F8")

    label("loc_81D6")

    ClearScenarioFlags(0x131, 5)
    ClearScenarioFlags(0x131, 6)
    ClearScenarioFlags(0x131, 7)
    ClearScenarioFlags(0x132, 2)
    Jump("loc_81F8")

    label("loc_81E7")

    SetScenarioFlags(0x131, 5)
    SetScenarioFlags(0x131, 6)
    SetScenarioFlags(0x131, 7)
    SetScenarioFlags(0x132, 2)
    Jump("loc_81F8")

    label("loc_81F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x131, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x131, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8250")

    #C0263
    ChrTalk(
        0x101,
        (
            "#00000Fよし、それじゃ引き続き\x01",
            "残りの調査にあたろう。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_829D")

    label("loc_8250")

    OP_29(0x6A, 0x1, 0x6)

    #C0264
    ChrTalk(
        0x101,
        (
            "#00000Fよし、これで一通り調査も終了だ。\x02\x03",

            "市民会館へ報告に戻ろう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_829D")

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
            "※ミニゲーム『釣り』が出来るようになりました。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #A0266
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※街道や街中などの水場にはたまに\x01",
            "　『水面に波紋が広がっている釣りポイント』があります。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #A0267
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※釣りポイントを調べて\x01",
            "  持っている『釣り竿』と『エサ』を選ぶと\x01",
            "  ロイドが魚釣りを始めます。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #A0268
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※！マークが出たときに素早く○ボタンを押すと\x01",
            "  魚を釣り上げることができます。\x01",
            "  （運悪く逃してしまうこともあります。）\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #A0269
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※なお、クロスベル市内には\x01",
            "　『港湾区』と『住宅街』に釣りポイントがあります。\x07\x00\x02",
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

    # Function_32_7FC8 end

    def Function_33_84DB(): pass

    label("Function_33_84DB")

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
            "#12404F……諸君、ご苦労だった。\x02\x03",

            "おかげで大した騒ぎになる前に\x01",
            "これを回収することができたようだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0271
    ChrTalk(
        0x101,
        (
            "#00000Fはは……\x01",
            "こちらもお役に立てて\x01",
            "よかったですよ。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1F, 0x1E, 500)

    #C0272
    ChrTalk(
        0x1F,
        (
            "#5P#13900Fフッ……言うに事欠いて“これ”とはね。\x01",
            "まるでモノを扱うような言い草じゃないか。\x02\x03",

            "#13903F……いや、そういう扱いも\x01",
            "趣があって悪くないかもしれない。\x02\x03",

            "#13912Fこれからもときどき、\x01",
            "そういう扱いで頼むよ、ミュラー㈱\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1E, 0x1F, 500)

    #C0273
    ChrTalk(
        0x1E,
        "#12401F#4S#500W黙#500W　っ#500W　て#500W　ろ。#3S\x02",
    )

    CloseMessageWindow()

    #C0274
    ChrTalk(
        0x1F,
        "#5P#13910F……スミマセンデシタ。\x02",
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
            "#12400F……すまない、この阿呆とは\x01",
            "昔からの付き合いでな。\x02\x03",

            "#12406F毎度、調子の乗り方が\x01",
            "エスカレートしてきているから、\x01",
            "時々は厳しく躾けねばならんのだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0276
    ChrTalk(
        0x104,
        "#6P#00309Fはは、なかなか苦労してるみたいッスね。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x1F, 0x101, 500)

    #C0277
    ChrTalk(
        0x1F,
        (
            "#13904Fなに、フォローしてくれる友人がいて\x01",
            "いつも助かっているさ。\x02\x03",

            "#13909Fフッ、これもボクの人徳の賜物だろうね。\x02",
        )
    )

    CloseMessageWindow()

    #C0278
    ChrTalk(
        0x104,
        (
            "#6P#00306Fア、アンタに言ったんじゃ\x01",
            "ないんだけどな。\x02",
        )
    )

    CloseMessageWindow()

    #C0279
    ChrTalk(
        0x105,
        (
            "#6P#10309Fフフ、反省なんて\x01",
            "してたまるかって感じだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0280
    ChrTalk(
        0x1E,
        (
            "#12400F……そのようだな。\x02\x03",

            "あとでみっちり\x01",
            "説教してやるから覚悟しておけ。\x02",
        )
    )

    CloseMessageWindow()

    #C0281
    ChrTalk(
        0x1F,
        (
            "#5P#13911Fや、やだなあ。\x01",
            "ほんの冗談だよミュラー。\x02\x03",

            "#13910F……キミたちも\x01",
            "煽らないでくれるかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0282
    ChrTalk(
        0x109,
        (
            "#6P#10109Fあ、あはは……\x01",
            "（ある意味、仲がいいのかも……）\x02",
        )
    )

    CloseMessageWindow()

    #C0283
    ChrTalk(
        0x1E,
        (
            "#12400F……では、そろそろ失礼する。\x02\x03",

            "#12404F忙しい中、世話になった。\x01",
            "改めて礼を言わせていただこう。\x02",
        )
    )

    CloseMessageWindow()

    #C0284
    ChrTalk(
        0x101,
        (
            "#00000Fいえ、それが俺たちの仕事ですから。\x02\x03",

            "#00006Fなんというか、その……\x01",
            "目を離さないように気をつけて下さい。\x02",
        )
    )

    CloseMessageWindow()

    #C0285
    ChrTalk(
        0x1E,
        "#12406F……心得た。\x02",
    )

    CloseMessageWindow()

    #C0286
    ChrTalk(
        0x1F,
        (
            "#13910Fふぅ、やれやれ……\x01",
            "楽しい時間もこれでおしまいか。\x02\x03",

            "#13900F今度こそ、さらばだ諸君。\x01",
            "縁があればまた会うこともあるだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0287
    ChrTalk(
        0x101,
        "#00006Fは、はあ……\x02",
    )

    CloseMessageWindow()

    #C0288
    ChrTalk(
        0x1F,
        (
            "#13910Fまあ、ボクとしては\x01",
            "噂のテーマパークなんかも\x01",
            "見物したかったんだがね。\x02\x03",

            "#13905Fおお、そうだキミたち。\x01",
            "今から案内を依頼できないかな？\x02\x03",

            "#13904Fフフ、我ながら名案だ。\x01",
            "楽しい気分で過ごせば、きっと\x01",
            "ミュラーの眉間のシワも……\x02",
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
            "#13911Fあっ、ミュラー君！？\x01",
            "ほ、ほんの冗談ダヨ？\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x1F, 0x13B, 0x0)
    SetChrChipByIndex(0x1F, 0x20)
    SetChrSubChip(0x1F, 0x0)
    SetChrFlags(0x1F, 0x20)

    def lambda_8DF4():
        OP_95(0xFE, 2000, 0, 1310, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_8DF4)
    Sleep(50)

    def lambda_8E11():
        OP_96(0xFE, 0x7D0, 0x0, 0x4F6, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_8E11)
    Sleep(50)

    #C0290
    ChrTalk(
        0x1F,
        "#11Aあーれー………………\x02",
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
            "#00012Fな、なんだかすごい人たち\x01",
            "だったな。\x02\x03",

            "#00003F実際のところ、どういう\x01",
            "人たちなんだろう……\x02",
        )
    )

    CloseMessageWindow()

    #C0292
    ChrTalk(
        0x105,
        (
            "#12P#10302Fま、それこそ\x01",
            "また会えた時にでも\x01",
            "聞いてみればいいさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0293
    ChrTalk(
        0x109,
        (
            "#6P#10106F正直、すっごく\x01",
            "疲れそうですけどね……\x02",
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
            "#00103F（つい脅かしてしまったけど、\x01",
            "  あの人はもしかして……）\x02\x03",

            "#00109F（……さ、さすがにそれは無いわよね。）\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)

    #C0295
    ChrTalk(
        0x101,
        (
            "#00005Fどうしたんだ、エリィ？\x01",
            "さっきから黙ってるみたいだけど……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)

    #C0296
    ChrTalk(
        0x102,
        "#11P#00102Fう、ううん、なんでもないのよ。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0297
    ChrTalk(
        0x104,
        (
            "#00303F……ま、ひとまず\x01",
            "一件落着ってとこだろ。\x02\x03",

            "#00300F行くとしようぜ、ロイド。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_9130():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9130)
    Sleep(50)

    def lambda_9140():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_9140)
    Sleep(300)
    OP_62(0x101)

    #C0298
    ChrTalk(
        0x101,
        "#11P#00000Fああ、そうだな。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x24, 3)
    NewScene("c0100", 100, 0, 0)
    IdleLoop()
    EventEnd(0x5)
    Return()

    # Function_33_84DB end

    def Function_34_9189(): pass

    label("Function_34_9189")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_9197")
    Jump("loc_9550")

    label("loc_9197")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_91A5")
    Jump("loc_9550")

    label("loc_91A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_91B3")
    Jump("loc_9550")

    label("loc_91B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_9346")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_92A4")

    #C0299
    ChrTalk(
        0x101,
        "#00001Fこっちはクリムゾン商会だ。\x02",
    )

    CloseMessageWindow()

    #C0300
    ChrTalk(
        0x104,
        (
            "#00303F叔父貴たちは、\x01",
            "通商会議での事件以来\x01",
            "鳴りを潜めてやがるみてぇだ。\x02\x03",

            "#00301F行ってもロクな情報は\x01",
            "得られねえだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0301
    ChrTalk(
        0x101,
        (
            "#00003Fああ……\x01",
            "今は行くのはやめておこう。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_932E")

    label("loc_92A4")


    #C0302
    ChrTalk(
        0x101,
        (
            "#00003Fクリムゾン商会は通商会議以来、\x01",
            "鳴りを潜めているみたいだ。\x02\x03",

            "#00001F大した情報も得られないだろうし、\x01",
            "今は行くのはやめておこう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_932E")

    SetChrPos(0x0, 90, 0, 80, 180)
    EventEnd(0x4)
    Jump("loc_9550")

    label("loc_9346")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_93E2")
    EventBegin(0x1)

    #C0303
    ChrTalk(
        0x101,
        (
            "#00000Fクリムゾン商会は捜査一課が\x01",
            "警戒に当たっているはずだ。\x02\x03",

            "ここは一課に任せて、\x01",
            "俺たちは自分の仕事に専念しよう。\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, 90, 0, 80, 180)
    EventEnd(0x4)
    Jump("loc_9550")

    label("loc_93E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_9496")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14E, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_93FD")
    Call(0, 11)
    Jump("loc_9491")

    label("loc_93FD")

    EventBegin(0x1)

    #C0304
    ChrTalk(
        0x101,
        (
            "#00003F『赤い星座』の動向は、\x01",
            "ここでは得られそうにないな。\x02\x03",

            "#00000F支援要請を片付けつつ、\x01",
            "各地で聞き込みをしてみよう。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, 90, 0, 80, 180)
    EventEnd(0x4)

    label("loc_9491")

    Jump("loc_9550")

    label("loc_9496")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 4)), scpexpr(EXPR_END)), "loc_94A4")
    Jump("loc_9550")

    label("loc_94A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_94B2")
    Jump("loc_9550")

    label("loc_94B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_9550")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x130, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9550")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x139, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_94D7")
    Call(0, 10)
    Jump("loc_9550")

    label("loc_94D7")

    EventBegin(0x1)

    #C0305
    ChrTalk(
        0x101,
        (
            "#00000F今は不動産業者の人が\x01",
            "交渉相手を待っているみたいだ。\x02\x03",

            "邪魔するのもなんだし行くとしよう。\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, 90, 0, 80, 180)
    EventEnd(0x4)

    label("loc_9550")

    Return()

    # Function_34_9189 end

    def Function_35_9551(): pass

    label("Function_35_9551")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_95A4")
    Sound(807, 0, 100, 0)
    SetChrName("")

    #A0306
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "鍵がかかっているようだ。\x01",
            "中に人の気配はない。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_96AC")

    label("loc_95A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_95F4")
    Sound(807, 0, 100, 0)
    SetChrName("")

    #A0307
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "鍵がかかっているようだ。\x01",
            "中に人の気配はない。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_96AC")

    label("loc_95F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_965A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18E, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9613")
    TalkEnd(0xFF)
    Call(0, 12)
    Return()

    label("loc_9613")

    Sound(807, 0, 100, 0)
    SetChrName("")

    #A0308
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "鍵がかかっているようだ。\x01",
            "中に人の気配はない。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_96AC")

    label("loc_965A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_9668")
    Jump("loc_96AC")

    label("loc_9668")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_9676")
    Jump("loc_96AC")

    label("loc_9676")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_96AC")
    Sound(807, 0, 100, 0)
    SetChrName("")

    #A0309
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "鍵がかかっているようだ。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_96AC")

    TalkEnd(0xFF)
    Return()

    # Function_35_9551 end

    def Function_36_96B0(): pass

    label("Function_36_96B0")

    EventBegin(0x2)
    ClearMapFlags(0x20)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0310
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※　百貨店《タイムズ》　※\x01",
            "※　　 従業員専用口 　　※\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    EventEnd(0x3)
    Return()

    # Function_36_96B0 end

    def Function_37_9710(): pass

    label("Function_37_9710")

    EventBegin(0x2)
    ClearMapFlags(0x20)
    Sound(807, 0, 100, 0)
    SetChrName("")

    #A0311
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "扉には鍵がかかっている。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    EventEnd(0x3)
    Return()

    # Function_37_9710 end

    def Function_38_9747(): pass

    label("Function_38_9747")

    EventBegin(0x1)

    #C0312
    ChrTalk(
        0x101,
        (
            "#00001Fランディを追いかけるぞ――\x01",
            "ルバーチェ跡地に急ごう！\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, -24330, 0, 210, 90)
    EventEnd(0x4)
    Return()

    # Function_38_9747 end

    def Function_39_979E(): pass

    label("Function_39_979E")

    EventBegin(0x1)

    #C0313
    ChrTalk(
        0x101,
        (
            "#00001Fランディを追いかけるぞ――\x01",
            "ルバーチェ跡地に急ごう！\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 19310, 0, 650, 270)
    EventEnd(0x4)
    Return()

    # Function_39_979E end

    SaveToFile()

Try(main)
