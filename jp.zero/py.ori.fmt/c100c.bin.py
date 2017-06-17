from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c100c.bin",                # FileName
        "c100c",                    # MapName
        "c100c",                    # Location
        0x0010,                     # MapIndex
        "ed7100",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x1D,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 16, 0, 5, 0, 6],
    )

    BuildStringList((
        "c100c",                  # 0
        "クロンク",               # 1
        "ディンズ",               # 2
        "リリィ",                 # 3
        "マルテ",                 # 4
        "アンネ",                 # 5
        "ルノー爺さん",           # 6
        "ロイ",                   # 7
        "メイリン",               # 8
        "スーザン",               # 9
        "クータ",                 # 10
        "サリナ",                 # 11
        "ユゴット",               # 12
        "アゼル",                 # 13
        "見物客",                 # 14
        "見物客",                 # 15
        "アレサ",                 # 16
        "ステファン",             # 17
        "ヴァルド",               # 18
        "ルガノフ",               # 19
        "ジェド",                 # 20
        "コウキ",                 # 21
        "黒髪の女性",             # 22
        "偽ブランド商",           # 23
        "中央広場",               # 24
        "西通り",                 # 25
        "行政区",                 # 26
        "住宅街",                 # 27
        "歓楽街",                 # 28
        "東通り",                 # 29
        "旧市街",                 # 30
        "港湾区",                 # 31
        "ＩＢＣ",                 # 32
        "駅前通り",               # 33
        "裏通り",                 # 34
        "ウルスラ間道",           # 35
        "東クロスベル街道",       # 36
        "西クロスベル街道",       # 37
        "マインツ山道",           # 38
    ))

    AddCharChip((
        "chr/ch22800.itc",                   # 00
        "chr/ch24800.itc",                   # 01
        "chr/ch24900.itc",                   # 02
        "chr/ch23500.itc",                   # 03
        "chr/ch21100.itc",                   # 04
        "chr/ch24000.itc",                   # 05
        "chr/ch21200.itc",                   # 06
        "chr/ch21500.itc",                   # 07
        "chr/ch10300.itc",                   # 08
        "chr/ch21400.itc",                   # 09
        "chr/ch20500.itc",                   # 0A
        "apl/ch50375.itc",                   # 0B
        "chr/ch23300.itc",                   # 0C
        "chr/ch23800.itc",                   # 0D
        "chr/ch20600.itc",                   # 0E
        "chr/ch02100.itc",                   # 0F
        "chr/ch30800.itc",                   # 10
        "chr/ch31700.itc",                   # 11
        "chr/ch22700.itc",                   # 12
        "chr/ch34200.itc",                   # 13
    ))

    DeclNpc(-24409,  -3000,   5239,    180,  261,  0x0, 0,   0,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(-13039,  -3000,   -810,    225,  261,  0x0, 0,   1,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(-16500,  -3000,   2920,    45,   261,  0x0, 0,   2,   0,   0,   4,   0,   9,   255,  0)
    DeclNpc(-4559,   -3000,   -8949,   180,  261,  0x0, 0,   3,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(26200,   -300,    -1049,   270,  261,  0x0, 0,   4,   0,   0,   1,   0,   14,  255,  0)
    DeclNpc(-40490,  -300,    15850,   90,   261,  0x0, 0,   5,   0,   0,   3,   0,   15,  255,  0)
    DeclNpc(-11560,  -300,    6820,    270,  389,  0x0, 0,   6,   0,   0,   0,   0,   16,  255,  0)
    DeclNpc(-12609,  -300,    7650,    135,  389,  0x0, 0,   7,   0,   0,   0,   0,   17,  255,  0)
    DeclNpc(-8470,   -3000,   -7349,   45,   261,  0x0, 0,   8,   0,   0,   0,   0,   18,  255,  0)
    DeclNpc(-15939,  -3000,   -600,    45,   261,  0x0, 0,   9,   0,   0,   2,   0,   19,  255,  0)
    DeclNpc(-15810,  -300,    16629,   180,  261,  0x0, 0,   10,  0,   0,   0,   0,   20,  255,  0)
    DeclNpc(-14960,  -300,    15649,   315,  261,  0x0, 0,   19,  0,   0,   0,   0,   21,  255,  0)
    DeclNpc(-17389,  -300,    16750,   90,   261,  0x0, 0,   11,  0,   0,   0,   0,   22,  255,  0)
    DeclNpc(-19219,  -319,    17000,   135,  261,  0x0, 0,   12,  0,   0,   0,   0,   23,  255,  0)
    DeclNpc(-17950,  -300,    17200,   225,  261,  0x0, 0,   13,  0,   0,   0,   0,   24,  255,  0)
    DeclNpc(5630,    -300,    3789,    135,  389,  0x0, 0,   18,  0,   0,   0,   0,   25,  255,  0)
    DeclNpc(7050,    -300,    3259,    225,  389,  0x0, 0,   14,  0,   0,   0,   0,   26,  255,  0)
    DeclNpc(5429,    -3000,   -13149,  315,  389,  0x0, 0,   15,  0,   0,   0,   0,   27,  255,  0)
    DeclNpc(5199,    -3000,   -11279,  180,  405,  0x0, 0,   16,  0,   0,   0,   0,   28,  255,  0)
    DeclNpc(4239,    -3000,   -12840,  90,   389,  0x0, 0,   17,  0,   0,   0,   0,   29,  255,  0)
    DeclNpc(3789,    -3000,   -11079,  135,  389,  0x0, 0,   16,  0,   0,   0,   0,   30,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclActor(17360,   -300,    4630,    1200,    17530,   1500,    5120,    0x007C, 0,  46, 0x0000)

    PlaceName(-111.26000213623047, 0.0, 15.239999771118164, 0x0000, 0x0000, "中央広場")
    PlaceName(-186.8800048828125, 0.0, 20.40999984741211, 0x0000, 0x0000, "西通り")
    PlaceName(-80.20999908447266, 0.0, 117.58999633789062, 0x0000, 0x0000, "行政区")
    PlaceName(-257.0299987792969, 0.0, 106.08999633789062, 0x0000, 0x0000, "住宅街")
    PlaceName(-173.0800018310547, 0.0, 96.88999938964844, 0x0000, 0x0000, "歓楽街")
    PlaceName(-17.829999923706055, 0.0, -11.210000038146973, 0x0000, 0x0000, "東通り")
    PlaceName(23.0, 0.0, -74.45999908447266, 0x0000, 0x0000, "旧市街")
    PlaceName(14.380000114440918, 0.0, 64.69000244140625, 0x0000, 0x0000, "港湾区")
    PlaceName(-15.529999732971191, 0.0, 172.7899932861328, 0x0000, 0x0000, "ＩＢＣ")
    PlaceName(-98.33000183105469, 0.0, -64.11000061035156, 0x0000, 0x0000, "駅前通り")
    PlaceName(-152.3800048828125, 0.0, 55.4900016784668, 0x0000, 0x0000, "裏通り")
    PlaceName(-101.77999877929688, 0.0, -99.76000213623047, 0x0000, 0x0000, "ウルスラ間道")
    PlaceName(44.279998779296875, 0.0, 4.889999866485596, 0x0000, 0x0000, "東クロスベル街道")
    PlaceName(-245.52999877929688, 0.0, 18.690000534057617, 0x0000, 0x0000, "西クロスベル街道")
    PlaceName(-238.6300048828125, 0.0, 133.69000244140625, 0x0000, 0x0000, "マインツ山道")
    PlaceName(-136.55999755859375, 0.0, -0.8600000143051147, 0x0000, 0x0051, "")
    PlaceName(-74.75, 0.0, 29.040000915527344, 0x0000, 0x0054, "")
    PlaceName(-108.38999938964844, 0.0, -10.0600004196167, 0x0000, 0x0057, "")
    PlaceName(-137.42999267578125, 0.0, 32.4900016784668, 0x0000, 0x0053, "")
    PlaceName(-113.8499984741211, 0.0, 60.09000015258789, 0x0000, 0x0053, "")
    PlaceName(-172.2100067138672, 0.0, 26.739999771118164, 0x0000, 0x0053, "")
    PlaceName(-183.42999267578125, 0.0, 50.88999938964844, 0x0000, 0x0053, "")
    PlaceName(-155.8300018310547, 0.0, 87.69000244140625, 0x0000, 0x0052, "")
    PlaceName(-150.36000061035156, 0.0, 72.73999786376953, 0x0000, 0x0053, "")
    PlaceName(-140.3000030517578, 0.0, 62.959999084472656, 0x0000, 0x0053, "")
    PlaceName(-107.52999877929688, 0.0, 144.61000061035156, 0x0000, 0x0051, "")
    PlaceName(21.280000686645508, 0.0, -11.210000038146973, 0x0000, 0x0052, "")
    PlaceName(1.7300000190734863, 0.0, -115.29000091552734, 0x0000, 0x0053, "")
    PlaceName(-13.229999542236328, 0.0, -94.01000213623047, 0x0000, 0x0053, "")

    ScpFunction((
        "Function_0_694",          # 00, 0
        "Function_1_74C",          # 01, 1
        "Function_2_7E5",          # 02, 2
        "Function_3_85A",          # 03, 3
        "Function_4_91B",          # 04, 4
        "Function_5_968",          # 05, 5
        "Function_6_D65",          # 06, 6
        "Function_7_E2A",          # 07, 7
        "Function_8_1269",         # 08, 8
        "Function_9_16AE",         # 09, 9
        "Function_10_1C47",        # 0A, 10
        "Function_11_38EC",        # 0B, 11
        "Function_12_3C73",        # 0C, 12
        "Function_13_3DB6",        # 0D, 13
        "Function_14_3F7F",        # 0E, 14
        "Function_15_4236",        # 0F, 15
        "Function_16_45B8",        # 10, 16
        "Function_17_466C",        # 11, 17
        "Function_18_46BB",        # 12, 18
        "Function_19_4A69",        # 13, 19
        "Function_20_4CC4",        # 14, 20
        "Function_21_4E61",        # 15, 21
        "Function_22_5032",        # 16, 22
        "Function_23_5168",        # 17, 23
        "Function_24_546B",        # 18, 24
        "Function_25_559A",        # 19, 25
        "Function_26_566A",        # 1A, 26
        "Function_27_5773",        # 1B, 27
        "Function_28_5AB1",        # 1C, 28
        "Function_29_5B21",        # 1D, 29
        "Function_30_5B78",        # 1E, 30
        "Function_31_5C16",        # 1F, 31
        "Function_32_5DD4",        # 20, 32
        "Function_33_60E3",        # 21, 33
        "Function_34_61CE",        # 22, 34
        "Function_35_68CB",        # 23, 35
        "Function_36_7B31",        # 24, 36
        "Function_37_7B61",        # 25, 37
        "Function_38_7B98",        # 26, 38
        "Function_39_7BB7",        # 27, 39
        "Function_40_7BDD",        # 28, 40
        "Function_41_7C03",        # 29, 41
        "Function_42_7C29",        # 2A, 42
        "Function_43_7C66",        # 2B, 43
        "Function_44_7C85",        # 2C, 44
        "Function_45_7CA4",        # 2D, 45
        "Function_46_7D37",        # 2E, 46
        "Function_47_999D",        # 2F, 47
        "Function_48_9C00",        # 30, 48
    ))


    def Function_0_694(): pass

    label("Function_0_694")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_6D4"),
        (1, "loc_6E0"),
        (2, "loc_6EC"),
        (3, "loc_6F8"),
        (4, "loc_704"),
        (5, "loc_710"),
        (6, "loc_71C"),
        (SWITCH_DEFAULT, "loc_728"),
    )


    label("loc_6D4")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_734")

    label("loc_6E0")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_734")

    label("loc_6EC")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_734")

    label("loc_6F8")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_734")

    label("loc_704")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_734")

    label("loc_710")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_734")

    label("loc_71C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_734")

    label("loc_728")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_734")

    label("loc_734")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_74B")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_734")

    label("loc_74B")

    Return()

    # Function_0_694 end

    def Function_1_74C(): pass

    label("Function_1_74C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7E4")
    OP_95(0xFE, -1180, -300, -1100, 2000, 0x0)
    OP_95(0xFE, -15670, -300, 12310, 2000, 0x0)
    OP_95(0xFE, -40270, -300, 12170, 2000, 0x0)
    Sleep(2500)
    OP_95(0xFE, -15670, -300, 12310, 2000, 0x0)
    OP_95(0xFE, -1180, -300, -1100, 2000, 0x0)
    OP_95(0xFE, 26200, -300, -1050, 2000, 0x0)
    Sleep(200)
    OP_93(0xFE, 0x10E, 0x1F4)
    Sleep(300)
    Jump("Function_1_74C")

    label("loc_7E4")

    Return()

    # Function_1_74C end

    def Function_2_7E5(): pass

    label("Function_2_7E5")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_859")
    OP_95(0xFE, -19740, -3000, 3190, 1000, 0x0)
    OP_95(0xFE, -22610, -3000, 3390, 1000, 0x0)
    OP_93(0xFE, 0x0, 0x12C)
    Sleep(1500)
    OP_95(0xFE, -19740, -3000, 3190, 1000, 0x0)
    OP_95(0xFE, -15940, -3000, -600, 1000, 0x0)
    OP_93(0xFE, 0x2D, 0x12C)
    Sleep(1500)
    Jump("Function_2_7E5")

    label("loc_859")

    Return()

    # Function_2_7E5 end

    def Function_3_85A(): pass

    label("Function_3_85A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_91A")
    OP_95(0xFE, -16760, -300, 15130, 2000, 0x0)
    OP_95(0xFE, -13780, -300, 14160, 2000, 0x0)
    OP_95(0xFE, -1180, -300, 2190, 2000, 0x0)
    OP_95(0xFE, 26030, -300, 2230, 2000, 0x0)
    Sleep(200)
    OP_93(0xFE, 0x10E, 0x1F4)
    Sleep(300)
    OP_95(0xFE, -1180, -300, 2190, 2000, 0x0)
    OP_95(0xFE, -13780, -300, 14160, 2000, 0x0)
    OP_95(0xFE, -16760, -300, 15130, 2000, 0x0)
    OP_95(0xFE, -40490, -300, 15850, 2000, 0x0)
    Sleep(2400)
    Jump("Function_3_85A")

    label("loc_91A")

    Return()

    # Function_3_85A end

    def Function_4_91B(): pass

    label("Function_4_91B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_967")
    OP_95(0xFE, -15130, -3000, 1420, 1000, 0x0)
    OP_93(0xFE, 0x2D, 0x12C)
    Sleep(3000)
    OP_95(0xFE, -16500, -3000, 2920, 1000, 0x0)
    OP_93(0xFE, 0x2D, 0x12C)
    Sleep(3000)
    Jump("Function_4_91B")

    label("loc_967")

    Return()

    # Function_4_91B end

    def Function_5_968(): pass

    label("Function_5_968")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6E), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B88")
    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A33")
    SetChrPos(0x0, -20760, -310, 33300, 180)
    SetChrPos(0x1, -20760, -310, 33300, 180)
    SetChrPos(0x2, -20760, -310, 33300, 180)
    SetChrPos(0x3, -20760, -310, 33300, 180)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A06")
    SetChrPos(0x4, -20760, -310, 33300, 180)
    SetChrPos(0x5, -20760, -310, 33300, 180)
    Jump("loc_A25")

    label("loc_A06")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A25")
    SetChrPos(0x4, -20760, -310, 33300, 180)

    label("loc_A25")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B88")

    label("loc_A33")

    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AE7")
    SetChrPos(0x0, 1910, -3000, -35980, 0)
    SetChrPos(0x1, 1910, -3000, -35980, 0)
    SetChrPos(0x2, 1910, -3000, -35980, 0)
    SetChrPos(0x3, 1910, -3000, -35980, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_ABA")
    SetChrPos(0x4, 1910, -3000, -35980, 0)
    SetChrPos(0x5, 1910, -3000, -35980, 0)
    Jump("loc_AD9")

    label("loc_ABA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_AD9")
    SetChrPos(0x4, 1910, -3000, -35980, 0)

    label("loc_AD9")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B88")

    label("loc_AE7")

    SetChrPos(0x0, -29790, -330, 13830, 90)
    SetChrPos(0x1, -29790, -330, 13830, 90)
    SetChrPos(0x2, -29790, -330, 13830, 90)
    SetChrPos(0x3, -29790, -330, 13830, 90)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B60")
    SetChrPos(0x4, -29790, -330, 13830, 90)
    SetChrPos(0x5, -29790, -330, 13830, 90)
    Jump("loc_B7F")

    label("loc_B60")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B7F")
    SetChrPos(0x4, -29790, -330, 13830, 90)

    label("loc_B7F")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_B88")

    OP_D0(0x7, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_BF2")
    SetChrPos(0x12, -14960, -300, 15650, 315)
    SetChrPos(0x13, -15810, -300, 16630, 270)
    SetChrFlags(0x13, 0x10)
    SetChrPos(0x15, -11870, -300, 6120, 315)
    SetChrPos(0x16, -12270, -300, 7480, 180)
    SetChrFlags(0x15, 0x10)
    SetChrFlags(0x16, 0x10)
    Jump("loc_D28")

    label("loc_BF2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_C58")
    SetChrFlags(0x12, 0x10)
    SetChrFlags(0x14, 0x10)
    SetChrPos(0x12, -14960, -300, 15650, 315)
    SetChrPos(0x13, -15810, -300, 16630, 180)
    SetChrPos(0x15, -12120, -310, 6540, 0)
    SetChrPos(0x16, -10940, -300, 6040, 315)
    SetChrFlags(0x15, 0x10)
    SetChrFlags(0x16, 0x10)
    Jump("loc_D28")

    label("loc_C58")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_C9B")
    OP_93(0x12, 0x10E, 0x0)
    SetChrFlags(0x12, 0x10)
    SetChrPos(0x15, -13300, -3000, -2410, 0)
    SetChrPos(0x16, -12550, -3000, -3260, 315)
    OP_93(0x9, 0xB4, 0x0)
    Jump("loc_D28")

    label("loc_C9B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_CFC")
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1C, 0x80)
    SetChrPos(0x15, -24030, -3000, 3630, 315)
    SetChrPos(0x16, -21730, -3000, 5420, 315)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_CF7")
    SetChrFlags(0x1C, 0x10)

    label("loc_CF7")

    Jump("loc_D28")

    label("loc_CFC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_D28")
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)

    label("loc_D28")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_D3C")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 31)
    Jump("loc_D4B")

    label("loc_D3C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 1)), scpexpr(EXPR_END)), "loc_D4B")
    ClearScenarioFlags(0x5C, 1)
    Event(0, 33)

    label("loc_D4B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1F, 0x0, 0x10)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D64")
    SetMapFlags(0x10000000)
    Event(0, 32)

    label("loc_D64")

    Return()

    # Function_5_968 end

    def Function_6_D65(): pass

    label("Function_6_D65")

    ClearMapObjFlags(0x6, 0x10)
    OP_70(0x6, 0x1E)
    LoadEffect(0x7, "event\\ev308_02.eff")
    PlayEffect(0x7, 0xFF, 0xFF, 0x0, -16000, -4300, 14000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x7, 0xFF, 0xFF, 0x0, 10000, -4300, 1000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x7, 0xFF, 0xFF, 0x0, -16000, -6000, -10000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Return()

    # Function_6_D65 end

    def Function_7_E2A(): pass

    label("Function_7_E2A")

    TalkBegin(0xFE)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_E37")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1265")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "話をする\x01",          # 0
            "買い物をする\x01",      # 1
            "やめる\x01",            # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E95")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_E95")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EB5")
    OP_AF(0x39)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1260")

    label("loc_EB5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_EC9")
    Jump("loc_1260")

    label("loc_EC9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1260")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_1021")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FAE")

    #C0001
    ChrTalk(
        0xFE,
        "……ふう、申し訳ないッス。\x02",
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0xFE,
        (
            "７０周年記念のグッズは\x01",
            "すべて売り切れたんスよ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Sleep(1500)

    #C0003
    ChrTalk(
        0xFE,
        (
            "いやあ、売れたッスねぇ～！\x01",
            "こんな売り上げは初めてッスよ～！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_101C")

    label("loc_FAE")


    #C0004
    ChrTalk(
        0xFE,
        (
            "……ふう、申し訳ないッス。\x01",
            "記念グッズは売り切れたッスよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0xFE,
        (
            "ふふふ、頑張って\x01",
            "作ったかいがあったッス。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_101C")

    Jump("loc_1260")

    label("loc_1021")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_1094")

    #C0006
    ChrTalk(
        0xFE,
        (
            "子供達に風車が\x01",
            "たくさん売れたッス。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0xFE,
        (
            "子供って\x01",
            "ああいうのが好きなんスね。\x01",
            "勉強になったッス。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1260")

    label("loc_1094")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_10E7")

    #C0008
    ChrTalk(
        0xFE,
        (
            "なんだか\x01",
            "人が集まってるッスよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0xFE,
        "売り込みのチャンスッスね！\x02",
    )

    CloseMessageWindow()
    Jump("loc_1260")

    label("loc_10E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_114B")

    #C0010
    ChrTalk(
        0xFE,
        (
            "……いやあ\x01",
            "記念祭は凄い人出ッス。\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0xFE,
        (
            "記念グッズが飛ぶように\x01",
            "売れていくッスよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1260")

    label("loc_114B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1260")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1231")

    #C0012
    ChrTalk(
        0xFE,
        "#4Sヘイ、らっしゃ～い！\x02",
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0xFE,
        (
            "いかがッスか、\x01",
            "こちら７０周年記念の\x01",
            "グッズっスよ～っ！\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0xFE,
        (
            "傘たてに卓上時計、\x01",
            "シガレットケースもあるッス！\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0xFE,
        (
            "クロスベル市庁舎の模型は\x01",
            "一品限りの早い者勝ちッスぅ！！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1260")

    label("loc_1231")


    #C0016
    ChrTalk(
        0xFE,
        (
            "７０周年記念の\x01",
            "グッズはいかがっスか～っ！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1260")

    Jump("loc_E37")

    label("loc_1265")

    TalkEnd(0xFE)
    Return()

    # Function_7_E2A end

    def Function_8_1269(): pass

    label("Function_8_1269")

    TalkBegin(0xFE)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1276")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16AA")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "話をする\x01",          # 0
            "買い物をする\x01",      # 1
            "やめる\x01",            # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_12D4")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_12D4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12F4")
    OP_AF(0x38)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_16A5")

    label("loc_12F4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1308")
    Jump("loc_16A5")

    label("loc_1308")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16A5")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_13AB")

    #C0017
    ChrTalk(
        0xFE,
        (
            "らっしゃい、らっしゃ～い！\x01",
            "毎度フレッシュ・ディンズだよっ！\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0xFE,
        (
            "今日はセールの最終日！\x01",
            "買い渋ったりしないでくれよっ！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_16A5")

    label("loc_13AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_1407")

    #C0019
    ChrTalk(
        0xFE,
        "おうおう、今日は凄い売れ行きだな。\x02",
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0xFE,
        "エイドス様もぶったまげそうだぜ！\x02",
    )

    CloseMessageWindow()
    Jump("loc_16A5")

    label("loc_1407")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_148D")

    #C0021
    ChrTalk(
        0xFE,
        "へい、そこのお客さん！\x02",
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0xFE,
        "寄ってくんな、見てくんなっ！\x02",
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0xFE,
        (
            "露店街名物、\x01",
            "フレッシュ・ディンズの\x01",
            "叩き売りだよっ！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_16A5")

    label("loc_148D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_15A2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_154A")

    #C0024
    ChrTalk(
        0xFE,
        (
            "昨晩は商工会の\x01",
            "寄り合いに呼ばれちまってさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0xFE,
        (
            "じーさま達と\x01",
            "一杯引っ掛けてきたぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0xFE,
        (
            "へへっ……\x01",
            "祭りの夜に商売仲間で飲むたぁ\x01",
            "なかなかオツな夜だったぜ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_159D")

    label("loc_154A")


    #C0027
    ChrTalk(
        0xFE,
        (
            "昨晩は商工会の\x01",
            "寄り合いで飲んできたんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0xFE,
        "いやあ、うまい酒だったぜぃ♪\x02",
    )

    CloseMessageWindow()

    label("loc_159D")

    Jump("loc_16A5")

    label("loc_15A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_16A5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_164B")

    #C0029
    ChrTalk(
        0xFE,
        "へい、らっしゃ～い！\x02",
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0xFE,
        (
            "リリィには今日くらい\x01",
            "遊んで来いって言ったんだがな。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0xFE,
        (
            "その気はないんだとよ。\x01",
            "やれやれ、生真面目な奴だぜい。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_16A5")

    label("loc_164B")


    #C0032
    ChrTalk(
        0xFE,
        (
            "リリィの奴は\x01",
            "昔から生真面目なんだよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0xFE,
        (
            "やれやれ、後で\x01",
            "後悔してもしらねえぞ～。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16A5")

    Jump("loc_1276")

    label("loc_16AA")

    TalkEnd(0xFE)
    Return()

    # Function_8_1269 end

    def Function_9_16AE(): pass

    label("Function_9_16AE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_17C1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_173F")

    #C0034
    ChrTalk(
        0xFE,
        (
            "あ、いらっしゃ～い！\x01",
            "何か買っていきます？\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0xFE,
        (
            "お釣りの小銭が\x01",
            "無くなっちゃったんで、\x01",
            "細かいのは勘弁してねー。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_17BC")

    label("loc_173F")


    #C0036
    ChrTalk(
        0xFE,
        (
            "お釣りの小銭が\x01",
            "無くなっちゃったのよね。\x01",
            "この忙しいときに……\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0xFE,
        (
            "マルテさんかクロンクさんに\x01",
            "両替してもらわなくっちゃ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17BC")

    Jump("loc_1C43")

    label("loc_17C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_1809")

    #C0038
    ChrTalk(
        0xFE,
        "わー、すごい人出……\x02",
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0xFE,
        "これじゃ警察の人も大変ね。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1C43")

    label("loc_1809")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_1A65")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_189C")

    #C0040
    ChrTalk(
        0xFE,
        (
            "お隣のクロンクさんの店の\x01",
            "売れ行きが凄いわ……\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0xFE,
        (
            "今年の露店街のＭＶＰは\x01",
            "クロンクさんに\x01",
            "持っていかれちゃったかも。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A60")

    label("loc_189C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19C3")

    #C0042
    ChrTalk(
        0xFE,
        (
            "なんでも、街のあちこちの出店が\x01",
            "ドロボーにあってるんですって？\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0xFE,
        (
            "さっき商工会の会長さんが\x01",
            "直々に教えに来てくれたのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0xFE,
        (
            "ま、あたしたちは\x01",
            "スリとか窃盗犯には慣れてるから。\x01",
            "簡単には引っかからないけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0xFE,
        (
            "普通の出店とかだと狙われちゃうかもね。\x01",
            "ちょっと気の毒だわ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1A60")

    label("loc_19C3")


    #C0046
    ChrTalk(
        0xFE,
        (
            "東通りの露店は\x01",
            "お店同士で声かけとかやってるし、\x01",
            "スリを追っかけるのは慣れてるんだけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0xFE,
        (
            "普通の出店とかだと狙われちゃうかもね。\x01",
            "ちょっと気の毒だわ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A60")

    Jump("loc_1C43")

    label("loc_1A65")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1B19")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1AE5")

    #C0048
    ChrTalk(
        0xFE,
        "ディンズったら……\x02",
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0xFE,
        (
            "商工会の会長さんと\x01",
            "ただ飲んできただけなの？\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0xFE,
        "しょうがないわねえ……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1B14")

    label("loc_1AE5")


    #C0051
    ChrTalk(
        0xFE,
        (
            "ほんと馬鹿正直で\x01",
            "表も裏もないんだから……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B14")

    Jump("loc_1C43")

    label("loc_1B19")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1C43")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C0C")

    #C0052
    ChrTalk(
        0xFE,
        (
            "いらっしゃ～い！\x01",
            "うちはスタンプラリーの加盟店よ。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0xFE,
        (
            "お買い物をしたら声を掛けてね。\x01",
            "ぽんとスタンプ押してあげるから。\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0xFE,
        (
            "それと、景品の交換は港湾公園ね。\x01",
            "商工会のテントが出てるはずだから\x01",
            "すぐに判ると思うわ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1C43")

    label("loc_1C0C")


    #C0055
    ChrTalk(
        0xFE,
        (
            "ふう、スタンプラリーの\x01",
            "案内をするのも大変だわ～。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C43")

    TalkEnd(0xFE)
    Return()

    # Function_9_16AE end

    def Function_10_1C47(): pass

    label("Function_10_1C47")

    TalkBegin(0xFE)
    ClearScenarioFlags(0x1, 6)
    Call(0, 12)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D94")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_END)), "loc_1D8C")

    #C0056
    ChrTalk(
        0xFE,
        (
            "あらあんたたち。\x01",
            "活きのイイ魚を持ってるみたいだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0xFE,
        (
            "あんた達で釣り上げたのかい？\x01",
            "傷も付いてないし……そのまま店に\x01",
            "並べたって良さそうじゃないか。\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0xFE,
        (
            "ふむ、どうだい。\x01",
            "その魚をあたしの店に\x01",
            "卸しちゃくれないかい？\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0xFE,
        (
            "クロスベル産の魚も人気があるんだ。\x01",
            "多少のお礼はするよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x51, 7)
    SetScenarioFlags(0x1, 5)
    TalkEnd(0xFE)
    Return()

    label("loc_1D8C")

    Call(0, 11)
    Jump("loc_38E8")

    label("loc_1D94")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_END)), "loc_38E5")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1DA7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_38E0")
    FadeToDark(300, 0, 100)
    MenuCmd(0, 1)
    MenuCmd(1, 1, "話をする")
    MenuCmd(1, 1, "魚を渡す")
    MenuCmd(1, 1, "やめる")
    ClearScenarioFlags(0x1, 6)
    Call(0, 12)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1DF9")
    MenuCmd(3, 1, 0x1)

    label("loc_1DF9")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuCmd(2, 1, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x1)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1E2B")
    FadeToBright(300, 0)
    OP_0D()

    label("loc_1E2B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_38AB")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1E44")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_389C")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuCmd(0, 1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x15E, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1EB5")
    MenuCmd(1, 1, "スノーシュラブ　　　地 × 10")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x15E, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1EAB")
    Call(0, 13)

    label("loc_1EAB")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_1EB5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x15F, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1F0A")
    MenuCmd(1, 1, "アルモリカブナ　　　水 × 10")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x15F, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1F00")
    Call(0, 13)

    label("loc_1F00")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_1F0A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x2, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x160, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1F5F")
    MenuCmd(1, 1, "オロショ　　　　　　火 × 10")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x160, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1F55")
    Call(0, 13)

    label("loc_1F55")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_1F5F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x3, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x161, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1FB4")
    MenuCmd(1, 1, "ロック　　　　　　　風 × 10")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x161, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1FAA")
    Call(0, 13)

    label("loc_1FAA")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_1FB4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x4, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x162, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2009")
    MenuCmd(1, 1, "カルプ　　　　　　　時 × 10")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x162, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1FFF")
    Call(0, 13)

    label("loc_1FFF")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2009")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x5, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x163, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_205E")
    MenuCmd(1, 1, "レイニー　　　　　　幻 × 10")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x163, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2054")
    Call(0, 13)

    label("loc_2054")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_205E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x6, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x164, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_20B3")
    MenuCmd(1, 1, "エーゼル　　　　　　地 × 20")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x164, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_20A9")
    Call(0, 13)

    label("loc_20A9")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_20B3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x7, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x165, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2108")
    MenuCmd(1, 1, "カサギン　　　　　　水 × 20")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x165, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_20FE")
    Call(0, 13)

    label("loc_20FE")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2108")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x8, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x166, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_215D")
    MenuCmd(1, 1, "レインボウ　　　　　火 × 20")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x166, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2153")
    Call(0, 13)

    label("loc_2153")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_215D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x9, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x167, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_21B2")
    MenuCmd(1, 1, "トラード　　　　　　風 × 20")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x167, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_21A8")
    Call(0, 13)

    label("loc_21A8")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_21B2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0xA, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x168, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2207")
    MenuCmd(1, 1, "サモーナ　　　　　　時 × 20")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x168, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_21FD")
    Call(0, 13)

    label("loc_21FD")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2207")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0xB, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x169, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_225C")
    MenuCmd(1, 1, "イール　　　　　　　幻 × 20")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x169, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2252")
    Call(0, 13)

    label("loc_2252")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_225C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0xC, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16A, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_22B1")
    MenuCmd(1, 1, "パールグラス　　　　空 × 20")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16A, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_22A7")
    Call(0, 13)

    label("loc_22A7")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_22B1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0xD, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16B, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2306")
    MenuCmd(1, 1, "グラトンバス　　　　地 × 40")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16B, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_22FC")
    Call(0, 13)

    label("loc_22FC")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2306")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0xE, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16C, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_235B")
    MenuCmd(1, 1, "バイパーヘッド　　　水 × 40")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16C, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2351")
    Call(0, 13)

    label("loc_2351")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_235B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0xF, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16D, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_23B0")
    MenuCmd(1, 1, "パイソンヘッド　　　火 × 40")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_23A6")
    Call(0, 13)

    label("loc_23A6")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_23B0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x10, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16E, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2405")
    MenuCmd(1, 1, "タイタン　　　　　　風 × 40")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16E, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_23FB")
    Call(0, 13)

    label("loc_23FB")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2405")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x11, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16F, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_245A")
    MenuCmd(1, 1, "クインシザー　　　　時 × 50")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16F, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2450")
    Call(0, 13)

    label("loc_2450")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_245A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x12, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x170, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_24AF")
    MenuCmd(1, 1, "エレキイール　　　　幻 × 50")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x170, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_24A5")
    Call(0, 13)

    label("loc_24A5")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_24AF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x13, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x171, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2504")
    MenuCmd(1, 1, "デモンタイタン　　　時 × 50")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x171, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_24FA")
    Call(0, 13)

    label("loc_24FA")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2504")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x14, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x172, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2559")
    MenuCmd(1, 1, "アークシュラブ　　　空 × 50")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x172, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_254F")
    Call(0, 13)

    label("loc_254F")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2559")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x15, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x173, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_25AF")
    MenuCmd(1, 1, "ゴルドサモーナ　　　時 × 100")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x173, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_25A5")
    Call(0, 13)

    label("loc_25A5")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_25AF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x16, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x174, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2605")
    MenuCmd(1, 1, "ノーブルカルプ　　　空 × 100")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x174, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_25FB")
    Call(0, 13)

    label("loc_25FB")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2605")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x17, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x175, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_265B")
    MenuCmd(1, 1, "サーペントヘッド　　幻 × 100")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x175, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2651")
    Call(0, 13)

    label("loc_2651")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_265B")

    MenuCmd(1, 1, "やめる")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuCmd(2, 1, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x1)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_269C")
    Jump("loc_3897")

    label("loc_269C")

    FadeToBright(300, 0)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x15E, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2729")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_271F")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0060
    ChrTalk(
        0xFE,
        (
            "この魚を\x07\x02",

            "#56I地のセピス10個\x07\x00",
            "で\x01",
            "渡してくれるかい？\x02",
        )
    )


    label("loc_271F")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2729")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x15F, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2799")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_278F")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0061
    ChrTalk(
        0xFE,
        (
            "この魚を\x07\x02",

            "#57I水のセピス10個\x07\x00",
            "で\x01",
            "渡してくれるかい？\x02",
        )
    )


    label("loc_278F")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2799")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x2, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x160, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2809")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_27FF")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0062
    ChrTalk(
        0xFE,
        (
            "この魚を\x07\x02",

            "#58I火のセピス10個\x07\x00",
            "で\x01",
            "渡してくれるかい？\x02",
        )
    )


    label("loc_27FF")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2809")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x3, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x161, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2879")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_286F")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0063
    ChrTalk(
        0xFE,
        (
            "この魚を\x07\x02",

            "#59I風のセピス10個\x07\x00",
            "で\x01",
            "渡してくれるかい？\x02",
        )
    )


    label("loc_286F")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2879")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x4, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x162, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_28E9")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_28DF")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0064
    ChrTalk(
        0xFE,
        (
            "この魚を\x07\x02",

            "#60I時のセピス10個\x07\x00",
            "で\x01",
            "渡してくれるかい？\x02",
        )
    )


    label("loc_28DF")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_28E9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x5, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x163, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2959")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_294F")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0065
    ChrTalk(
        0xFE,
        (
            "この魚を\x07\x02",

            "#62I幻のセピス10個\x07\x00",
            "で\x01",
            "渡してくれるかい？\x02",
        )
    )


    label("loc_294F")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2959")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x6, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x164, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_29C9")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_29BF")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0066
    ChrTalk(
        0xFE,
        (
            "この魚を\x07\x02",

            "#56I地のセピス20個\x07\x00",
            "で\x01",
            "渡してくれるかい？\x02",
        )
    )


    label("loc_29BF")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_29C9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x7, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x165, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2A39")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2A2F")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0067
    ChrTalk(
        0xFE,
        (
            "この魚を\x07\x02",

            "#57I水のセピス20個\x07\x00",
            "で\x01",
            "渡してくれるかい？\x02",
        )
    )


    label("loc_2A2F")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2A39")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x8, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x166, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2AA9")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2A9F")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0068
    ChrTalk(
        0xFE,
        (
            "この魚を\x07\x02",

            "#58I火のセピス20個\x07\x00",
            "で\x01",
            "渡してくれるかい？\x02",
        )
    )


    label("loc_2A9F")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2AA9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x9, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x167, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2B19")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B0F")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0069
    ChrTalk(
        0xFE,
        (
            "この魚を\x07\x02",

            "#59I風のセピス20個\x07\x00",
            "で\x01",
            "渡してくれるかい？\x02",
        )
    )


    label("loc_2B0F")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2B19")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0xA, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x168, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2B89")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B7F")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0070
    ChrTalk(
        0xFE,
        (
            "この魚を\x07\x02",

            "#60I時のセピス20個\x07\x00",
            "で\x01",
            "渡してくれるかい？\x02",
        )
    )


    label("loc_2B7F")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2B89")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0xB, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x169, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2BF9")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2BEF")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0071
    ChrTalk(
        0xFE,
        (
            "この魚を\x07\x02",

            "#62I幻のセピス20個\x07\x00",
            "で\x01",
            "渡してくれるかい？\x02",
        )
    )


    label("loc_2BEF")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2BF9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0xC, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16A, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2C69")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C5F")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0072
    ChrTalk(
        0xFE,
        (
            "この魚を\x07\x02",

            "#61I空のセピス20個\x07\x00",
            "で\x01",
            "渡してくれるかい？\x02",
        )
    )


    label("loc_2C5F")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2C69")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0xD, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16B, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2CD9")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2CCF")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0073
    ChrTalk(
        0xFE,
        (
            "この魚を\x07\x02",

            "#56I地のセピス40個\x07\x00",
            "で\x01",
            "渡してくれるかい？\x02",
        )
    )


    label("loc_2CCF")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2CD9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0xE, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16C, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2D49")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D3F")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0074
    ChrTalk(
        0xFE,
        (
            "この魚を\x07\x02",

            "#57I水のセピス40個\x07\x00",
            "で\x01",
            "渡してくれるかい？\x02",
        )
    )


    label("loc_2D3F")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2D49")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0xF, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16D, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2DB9")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2DAF")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0075
    ChrTalk(
        0xFE,
        (
            "この魚を\x07\x02",

            "#58I火のセピス40個\x07\x00",
            "で\x01",
            "渡してくれるかい？\x02",
        )
    )


    label("loc_2DAF")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2DB9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x10, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16E, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2E29")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2E1F")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0076
    ChrTalk(
        0xFE,
        (
            "この魚を\x07\x02",

            "#59I風のセピス40個\x07\x00",
            "で\x01",
            "渡してくれるかい？\x02",
        )
    )


    label("loc_2E1F")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2E29")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x11, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16F, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2E99")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2E8F")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x11), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0077
    ChrTalk(
        0xFE,
        (
            "この魚を\x07\x02",

            "#60I時のセピス50個\x07\x00",
            "で\x01",
            "渡してくれるかい？\x02",
        )
    )


    label("loc_2E8F")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2E99")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x12, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x170, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2F09")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2EFF")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x12), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0078
    ChrTalk(
        0xFE,
        (
            "この魚を\x07\x02",

            "#62I幻のセピス50個\x07\x00",
            "で\x01",
            "渡してくれるかい？\x02",
        )
    )


    label("loc_2EFF")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2F09")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x13, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x171, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2F79")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F6F")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x13), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0079
    ChrTalk(
        0xFE,
        (
            "この魚を\x07\x02",

            "#60I時のセピス50個\x07\x00",
            "で\x01",
            "渡してくれるかい？\x02",
        )
    )


    label("loc_2F6F")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2F79")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x14, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x172, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2FE9")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2FDF")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0080
    ChrTalk(
        0xFE,
        (
            "この魚を\x07\x02",

            "#61I空のセピス50個\x07\x00",
            "で\x01",
            "渡してくれるかい？\x02",
        )
    )


    label("loc_2FDF")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2FE9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x15, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x173, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_305A")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3050")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x15), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0081
    ChrTalk(
        0xFE,
        (
            "この魚を\x07\x02",

            "#60I時のセピス100個\x07\x00",
            "で\x01",
            "渡してくれるかい？\x02",
        )
    )


    label("loc_3050")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_305A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x16, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x174, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_30CB")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_30C1")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x16), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0082
    ChrTalk(
        0xFE,
        (
            "この魚を\x07\x02",

            "#61I空のセピス100個\x07\x00",
            "で\x01",
            "渡してくれるかい？\x02",
        )
    )


    label("loc_30C1")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_30CB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x17, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x175, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_313C")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3132")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x17), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0083
    ChrTalk(
        0xFE,
        (
            "この魚を\x07\x02",

            "#62I幻のセピス100個\x07\x00",
            "で\x01",
            "渡してくれるかい？\x02",
        )
    )


    label("loc_3132")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_313C")

    CloseMessageWindow()
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "交換する\x01",      # 0
            "やめる\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3897")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x15), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x16), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x17), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_324C")

    #C0084
    ChrTalk(
        0xFE,
        (
            "これは特別立派な魚だし\x01",
            "もう釣れないかもしれないけど……\x01",
            "本当に貰っちまっていいかい？\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "はい\x01",        # 0
            "いいえ\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_324C")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_324C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_388D")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sleep(300)
    Sound(17, 0, 100, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_3313"),
        (1, "loc_334C"),
        (2, "loc_3385"),
        (3, "loc_33BE"),
        (4, "loc_33F7"),
        (5, "loc_3430"),
        (6, "loc_3469"),
        (7, "loc_34A2"),
        (8, "loc_34DB"),
        (9, "loc_3514"),
        (10, "loc_354D"),
        (11, "loc_3586"),
        (12, "loc_35BF"),
        (13, "loc_35F8"),
        (14, "loc_3631"),
        (15, "loc_366A"),
        (16, "loc_36A3"),
        (17, "loc_36DC"),
        (18, "loc_3715"),
        (19, "loc_374E"),
        (20, "loc_3787"),
        (21, "loc_37C0"),
        (22, "loc_37FB"),
        (23, "loc_3836"),
        (SWITCH_DEFAULT, "loc_3871"),
    )


    label("loc_3313")


    #A0085
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#56I地のセピス×１０\x07\x00",
            "を手に入れた。\x02",
        )
    )

    AddSepith(0x0, 10)
    SubItemNumber(0x15E, 1)
    Jump("loc_3871")

    label("loc_334C")


    #A0086
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#57I水のセピス×１０\x07\x00",
            "を手に入れた。\x02",
        )
    )

    AddSepith(0x1, 10)
    SubItemNumber(0x15F, 1)
    Jump("loc_3871")

    label("loc_3385")


    #A0087
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#58I火のセピス×１０\x07\x00",
            "を手に入れた。\x02",
        )
    )

    AddSepith(0x2, 10)
    SubItemNumber(0x160, 1)
    Jump("loc_3871")

    label("loc_33BE")


    #A0088
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#59I風のセピス×１０\x07\x00",
            "を手に入れた。\x02",
        )
    )

    AddSepith(0x3, 10)
    SubItemNumber(0x161, 1)
    Jump("loc_3871")

    label("loc_33F7")


    #A0089
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#60I時のセピス×１０\x07\x00",
            "を手に入れた。\x02",
        )
    )

    AddSepith(0x4, 10)
    SubItemNumber(0x162, 1)
    Jump("loc_3871")

    label("loc_3430")


    #A0090
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#62I幻のセピス×１０\x07\x00",
            "を手に入れた。\x02",
        )
    )

    AddSepith(0x6, 10)
    SubItemNumber(0x163, 1)
    Jump("loc_3871")

    label("loc_3469")


    #A0091
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#56I地のセピス×２０\x07\x00",
            "を手に入れた。\x02",
        )
    )

    AddSepith(0x0, 20)
    SubItemNumber(0x164, 1)
    Jump("loc_3871")

    label("loc_34A2")


    #A0092
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#57I水のセピス×２０\x07\x00",
            "を手に入れた。\x02",
        )
    )

    AddSepith(0x1, 20)
    SubItemNumber(0x165, 1)
    Jump("loc_3871")

    label("loc_34DB")


    #A0093
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#58I火のセピス×２０\x07\x00",
            "を手に入れた。\x02",
        )
    )

    AddSepith(0x2, 20)
    SubItemNumber(0x166, 1)
    Jump("loc_3871")

    label("loc_3514")


    #A0094
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#59I風のセピス×２０\x07\x00",
            "を手に入れた。\x02",
        )
    )

    AddSepith(0x3, 20)
    SubItemNumber(0x167, 1)
    Jump("loc_3871")

    label("loc_354D")


    #A0095
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#60I時のセピス×２０\x07\x00",
            "を手に入れた。\x02",
        )
    )

    AddSepith(0x4, 20)
    SubItemNumber(0x168, 1)
    Jump("loc_3871")

    label("loc_3586")


    #A0096
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#62I幻のセピス×２０\x07\x00",
            "を手に入れた。\x02",
        )
    )

    AddSepith(0x6, 20)
    SubItemNumber(0x169, 1)
    Jump("loc_3871")

    label("loc_35BF")


    #A0097
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#61I空のセピス×２０\x07\x00",
            "を手に入れた。\x02",
        )
    )

    AddSepith(0x5, 20)
    SubItemNumber(0x16A, 1)
    Jump("loc_3871")

    label("loc_35F8")


    #A0098
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#56I地のセピス×４０\x07\x00",
            "を手に入れた。\x02",
        )
    )

    AddSepith(0x0, 40)
    SubItemNumber(0x16B, 1)
    Jump("loc_3871")

    label("loc_3631")


    #A0099
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#57I水のセピス×４０\x07\x00",
            "を手に入れた。\x02",
        )
    )

    AddSepith(0x1, 40)
    SubItemNumber(0x16C, 1)
    Jump("loc_3871")

    label("loc_366A")


    #A0100
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#58I火のセピス×４０\x07\x00",
            "を手に入れた。\x02",
        )
    )

    AddSepith(0x2, 40)
    SubItemNumber(0x16D, 1)
    Jump("loc_3871")

    label("loc_36A3")


    #A0101
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#59I風のセピス×４０\x07\x00",
            "を手に入れた。\x02",
        )
    )

    AddSepith(0x3, 40)
    SubItemNumber(0x16E, 1)
    Jump("loc_3871")

    label("loc_36DC")


    #A0102
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#60I時のセピス×５０\x07\x00",
            "を手に入れた。\x02",
        )
    )

    AddSepith(0x4, 50)
    SubItemNumber(0x16F, 1)
    Jump("loc_3871")

    label("loc_3715")


    #A0103
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#62I幻のセピス×５０\x07\x00",
            "を手に入れた。\x02",
        )
    )

    AddSepith(0x6, 50)
    SubItemNumber(0x170, 1)
    Jump("loc_3871")

    label("loc_374E")


    #A0104
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#60I時のセピス×５０\x07\x00",
            "を手に入れた。\x02",
        )
    )

    AddSepith(0x4, 50)
    SubItemNumber(0x171, 1)
    Jump("loc_3871")

    label("loc_3787")


    #A0105
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#61I空のセピス×５０\x07\x00",
            "を手に入れた。\x02",
        )
    )

    AddSepith(0x5, 50)
    SubItemNumber(0x172, 1)
    Jump("loc_3871")

    label("loc_37C0")


    #A0106
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#60I時のセピス×１００\x07\x00",
            "を手に入れた。\x02",
        )
    )

    AddSepith(0x4, 100)
    SubItemNumber(0x173, 1)
    Jump("loc_3871")

    label("loc_37FB")


    #A0107
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#61I空のセピス×１００\x07\x00",
            "を手に入れた。\x02",
        )
    )

    AddSepith(0x5, 100)
    SubItemNumber(0x174, 1)
    Jump("loc_3871")

    label("loc_3836")


    #A0108
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#62I幻のセピス×１００\x07\x00",
            "を手に入れた。\x02",
        )
    )

    AddSepith(0x6, 100)
    SubItemNumber(0x175, 1)
    Jump("loc_3871")

    label("loc_3871")

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3897")

    label("loc_388D")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3897")

    Jump("loc_1E44")

    label("loc_389C")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_38DB")

    label("loc_38AB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_38BF")
    Jump("loc_38DB")

    label("loc_38BF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_38DB")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 11)

    label("loc_38DB")

    Jump("loc_1DA7")

    label("loc_38E0")

    Jump("loc_38E8")

    label("loc_38E5")

    Call(0, 11)

    label("loc_38E8")

    TalkEnd(0xB)
    Return()

    # Function_10_1C47 end

    def Function_11_38EC(): pass

    label("Function_11_38EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_END)), "loc_39C2")

    #C0109
    ChrTalk(
        0xB,
        (
            "クロスベル産の魚も人気があるんだが\x01",
            "仕入れ先が少なくてね。\x01",
            "いつも品薄気味なんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0xB,
        (
            "あんた達の持ってる魚は\x01",
            "中々質が良さそうだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0xB,
        (
            "良ければあたしの店に卸しておくれよ。\x01",
            "多少のお礼はするよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C72")

    label("loc_39C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_3A1D")

    #C0112
    ChrTalk(
        0xB,
        (
            "今日はいつもの\x01",
            "５倍仕入れたんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0xB,
        "何とか売り切ってやらなくちゃ。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3C72")

    label("loc_3A1D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_3A75")

    #C0114
    ChrTalk(
        0xB,
        "今年の売れ行きはすごいわねえ。\x02",
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0xB,
        "後で亭主に自慢してやらなくちゃ。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3C72")

    label("loc_3A75")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_3AFF")

    #C0116
    ChrTalk(
        0xB,
        "はいよ、いらっしゃ～い！\x02",
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0xB,
        (
            "記念祭の見所は\x01",
            "パレードだけじゃないよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0xB,
        (
            "露店街の店も\x01",
            "しっかり見ていっておくれ～っ！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C72")

    label("loc_3AFF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_3B83")

    #C0119
    ChrTalk(
        0xB,
        (
            "はいよ、いらっしゃ～い！\x01",
            "朝の採れたて、新鮮だよ～っ！\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0xB,
        (
            "ささっとゴハンに盛り付けて\x01",
            "醤油をたらすと絶品だよっ！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C72")

    label("loc_3B83")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_3C72")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3C1D")

    #C0121
    ChrTalk(
        0xB,
        "はいよ、いらっしゃ～い！\x02",
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0xB,
        "こっちのお魚なんていかが？\x02",
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0xB,
        (
            "そこの龍老飯店に持ち込めば\x01",
            "さくっとお刺身にしてくれるよっ！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3C72")

    label("loc_3C1D")


    #C0124
    ChrTalk(
        0xB,
        (
            "東通りの宿は\x01",
            "どこも食材持込ＯＫなんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0xB,
        "これが露店街流の食べ歩き方だよっ！\x02",
    )

    CloseMessageWindow()

    label("loc_3C72")

    Return()

    # Function_11_38EC end

    def Function_12_3C73(): pass

    label("Function_12_3C73")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x15E, 0x0)"), scpexpr(EXPR_END)), "loc_3C81")
    SetScenarioFlags(0x1, 6)

    label("loc_3C81")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x15F, 0x0)"), scpexpr(EXPR_END)), "loc_3C8F")
    SetScenarioFlags(0x1, 6)

    label("loc_3C8F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x160, 0x0)"), scpexpr(EXPR_END)), "loc_3C9D")
    SetScenarioFlags(0x1, 6)

    label("loc_3C9D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x161, 0x0)"), scpexpr(EXPR_END)), "loc_3CAB")
    SetScenarioFlags(0x1, 6)

    label("loc_3CAB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x162, 0x0)"), scpexpr(EXPR_END)), "loc_3CB9")
    SetScenarioFlags(0x1, 6)

    label("loc_3CB9")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x163, 0x0)"), scpexpr(EXPR_END)), "loc_3CC7")
    SetScenarioFlags(0x1, 6)

    label("loc_3CC7")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x164, 0x0)"), scpexpr(EXPR_END)), "loc_3CD5")
    SetScenarioFlags(0x1, 6)

    label("loc_3CD5")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x165, 0x0)"), scpexpr(EXPR_END)), "loc_3CE3")
    SetScenarioFlags(0x1, 6)

    label("loc_3CE3")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x166, 0x0)"), scpexpr(EXPR_END)), "loc_3CF1")
    SetScenarioFlags(0x1, 6)

    label("loc_3CF1")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x167, 0x0)"), scpexpr(EXPR_END)), "loc_3CFF")
    SetScenarioFlags(0x1, 6)

    label("loc_3CFF")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x168, 0x0)"), scpexpr(EXPR_END)), "loc_3D0D")
    SetScenarioFlags(0x1, 6)

    label("loc_3D0D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x169, 0x0)"), scpexpr(EXPR_END)), "loc_3D1B")
    SetScenarioFlags(0x1, 6)

    label("loc_3D1B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16A, 0x0)"), scpexpr(EXPR_END)), "loc_3D29")
    SetScenarioFlags(0x1, 6)

    label("loc_3D29")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16B, 0x0)"), scpexpr(EXPR_END)), "loc_3D37")
    SetScenarioFlags(0x1, 6)

    label("loc_3D37")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16C, 0x0)"), scpexpr(EXPR_END)), "loc_3D45")
    SetScenarioFlags(0x1, 6)

    label("loc_3D45")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16D, 0x0)"), scpexpr(EXPR_END)), "loc_3D53")
    SetScenarioFlags(0x1, 6)

    label("loc_3D53")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16E, 0x0)"), scpexpr(EXPR_END)), "loc_3D61")
    SetScenarioFlags(0x1, 6)

    label("loc_3D61")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16F, 0x0)"), scpexpr(EXPR_END)), "loc_3D6F")
    SetScenarioFlags(0x1, 6)

    label("loc_3D6F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x170, 0x0)"), scpexpr(EXPR_END)), "loc_3D7D")
    SetScenarioFlags(0x1, 6)

    label("loc_3D7D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x171, 0x0)"), scpexpr(EXPR_END)), "loc_3D8B")
    SetScenarioFlags(0x1, 6)

    label("loc_3D8B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x172, 0x0)"), scpexpr(EXPR_END)), "loc_3D99")
    SetScenarioFlags(0x1, 6)

    label("loc_3D99")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x173, 0x0)"), scpexpr(EXPR_END)), "loc_3DA7")
    SetScenarioFlags(0x1, 6)

    label("loc_3DA7")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x174, 0x0)"), scpexpr(EXPR_END)), "loc_3DB5")
    SetScenarioFlags(0x1, 6)

    label("loc_3DB5")

    Return()

    # Function_12_3C73 end

    def Function_13_3DB6(): pass

    label("Function_13_3DB6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3DC9")
    MenuCmd(3, 1, 0x0)

    label("loc_3DC9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3DDC")
    MenuCmd(3, 1, 0x1)

    label("loc_3DDC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3DEF")
    MenuCmd(3, 1, 0x2)

    label("loc_3DEF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3E02")
    MenuCmd(3, 1, 0x3)

    label("loc_3E02")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3E15")
    MenuCmd(3, 1, 0x4)

    label("loc_3E15")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3E28")
    MenuCmd(3, 1, 0x5)

    label("loc_3E28")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3E3B")
    MenuCmd(3, 1, 0x6)

    label("loc_3E3B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3E4E")
    MenuCmd(3, 1, 0x7)

    label("loc_3E4E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3E61")
    MenuCmd(3, 1, 0x8)

    label("loc_3E61")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3E74")
    MenuCmd(3, 1, 0x9)

    label("loc_3E74")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3E87")
    MenuCmd(3, 1, 0xA)

    label("loc_3E87")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3E9A")
    MenuCmd(3, 1, 0xB)

    label("loc_3E9A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3EAD")
    MenuCmd(3, 1, 0xC)

    label("loc_3EAD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3EC0")
    MenuCmd(3, 1, 0xD)

    label("loc_3EC0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3ED3")
    MenuCmd(3, 1, 0xE)

    label("loc_3ED3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3EE6")
    MenuCmd(3, 1, 0xF)

    label("loc_3EE6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3EF9")
    MenuCmd(3, 1, 0x10)

    label("loc_3EF9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x11), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3F0C")
    MenuCmd(3, 1, 0x11)

    label("loc_3F0C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x12), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3F1F")
    MenuCmd(3, 1, 0x12)

    label("loc_3F1F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x13), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3F32")
    MenuCmd(3, 1, 0x13)

    label("loc_3F32")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3F45")
    MenuCmd(3, 1, 0x14)

    label("loc_3F45")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x15), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3F58")
    MenuCmd(3, 1, 0x15)

    label("loc_3F58")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x16), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3F6B")
    MenuCmd(3, 1, 0x16)

    label("loc_3F6B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x17), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3F7E")
    MenuCmd(3, 1, 0x17)

    label("loc_3F7E")

    Return()

    # Function_13_3DB6 end

    def Function_14_3F7F(): pass

    label("Function_14_3F7F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_3FF6")

    #C0126
    ChrTalk(
        0xFE,
        (
            "あらいけない、今日で\x01",
            "スタンプラリーが終わりじゃない。\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0xFE,
        (
            "急いで景品交換\x01",
            "してもらわなくっちゃ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4232")

    label("loc_3FF6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_4055")

    #C0128
    ChrTalk(
        0xFE,
        "今年のパレードは凄かったわねー。\x02",
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0xFE,
        (
            "手を振ってた子供達も\x01",
            "可愛かったわ～。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4232")

    label("loc_4055")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_40CF")

    #C0130
    ChrTalk(
        0xFE,
        (
            "買い物ついでに\x01",
            "出店を回ってしまったわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0xFE,
        (
            "ふう……いけないいけない。\x01",
            "家族には内緒にしておきましょ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4232")

    label("loc_40CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_41D3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4162")

    #C0132
    ChrTalk(
        0xFE,
        (
            "今年はアルモリカ村の方に\x01",
            "行く人もいるみたいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0xFE,
        (
            "確かにきれいな所だし……\x01",
            "何より美味しい料理が食べれるものね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_41CE")

    label("loc_4162")


    #C0134
    ChrTalk(
        0xFE,
        (
            "アルモリカ村はきれいな所だし\x01",
            "美味しい料理が食べれるもの。\x02",
        )
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0xFE,
        (
            "観光客が立ち寄るのも\x01",
            "判る気がするわね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_41CE")

    Jump("loc_4232")

    label("loc_41D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_4232")

    #C0136
    ChrTalk(
        0xFE,
        (
            "記念祭の間も\x01",
            "休めないのが主婦業よね。\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0xFE,
        (
            "夕飯の材料だけは\x01",
            "買っておかなくちゃ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4232")

    TalkEnd(0xFE)
    Return()

    # Function_14_3F7F end

    def Function_15_4236(): pass

    label("Function_15_4236")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_434E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4305")

    #C0138
    ChrTalk(
        0xFE,
        (
            "港湾区のステージでは\x01",
            "毎日催し物をやっていたそうじゃよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0xFE,
        (
            "うーむ、わしは３日目のステージを\x01",
            "見逃してしまったのう。\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0xFE,
        (
            "今日の催しは見逃さんよう\x01",
            "しかと覚えておかんとな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_4349")

    label("loc_4305")


    #C0141
    ChrTalk(
        0xFE,
        (
            "今日も港湾区では\x01",
            "催しをやるはずじゃ。\x01",
            "見逃さんようにせんとな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4349")

    Jump("loc_45B4")

    label("loc_434E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_43D2")

    #C0142
    ChrTalk(
        0xFE,
        (
            "ほっほ、パレードの４台目は\x01",
            "クロスベル商工会の車じゃったな。\x02",
        )
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0xFE,
        (
            "東方風じゃったから\x01",
            "一目で分かってしもうたわい。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_45B4")

    label("loc_43D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_442F")

    #C0144
    ChrTalk(
        0xFE,
        "ほっほ、今日はパレードじゃのう。\x02",
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0xFE,
        (
            "わしも楽しみに\x01",
            "させてもらっとるよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_45B4")

    label("loc_442F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_44B0")

    #C0146
    ChrTalk(
        0xFE,
        (
            "おうおう、また観光客が\x01",
            "詰め掛けておるな。\x02",
        )
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0xFE,
        (
            "そう焦らずともよい。\x01",
            "今年の記念祭は５日間も\x01",
            "開かれるんじゃぞ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_45B4")

    label("loc_44B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_45B4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_453A")

    #C0148
    ChrTalk(
        0xFE,
        "ハッピーアニバーサリーじゃのう！\x02",
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0xFE,
        "今年でクロスベルも７０歳じゃ。\x02",
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0xFE,
        (
            "おんしらも\x01",
            "祝ってやっとくれい！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_45B4")

    label("loc_453A")


    #C0151
    ChrTalk(
        0xFE,
        (
            "ちなみにクロスベルは\x01",
            "このわしより少しばかり若いんじゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0xFE,
        (
            "わしは今年で７２歳、\x01",
            "マクダエル市長と同い年なんじゃよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_45B4")

    TalkEnd(0xFE)
    Return()

    # Function_15_4236 end

    def Function_16_45B8(): pass

    label("Function_16_45B8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_4668")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_463D")

    #C0153
    ChrTalk(
        0xFE,
        (
            "妹を記念祭につれていく役も\x01",
            "押し付けられちまった。\x02",
        )
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0xFE,
        "はあ、結局こうなるんだよな～。\x02",
    )

    CloseMessageWindow()
    OP_93(0xFE, 0x10E, 0x0)
    SetChrFlags(0xFE, 0x10)
    SetScenarioFlags(0x0, 6)
    Jump("loc_4668")

    label("loc_463D")


    #C0155
    ChrTalk(
        0xFE,
        (
            "メイリン、次は\x01",
            "どこに行きたいんだ～？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4668")

    TalkEnd(0xFE)
    Return()

    # Function_16_45B8 end

    def Function_17_466C(): pass

    label("Function_17_466C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_46B7")

    #C0156
    ChrTalk(
        0xFE,
        "おまつり、たのしーねー！\x02",
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0xFE,
        (
            "メイリン\x01",
            "お店みにいきたい！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_46B7")

    TalkEnd(0xFE)
    Return()

    # Function_17_466C end

    def Function_18_46BB(): pass

    label("Function_18_46BB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_47E4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_47A2")

    #C0158
    ChrTalk(
        0xFE,
        (
            "最終日の今日だけ\x01",
            "休みの会社も多いみたいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0xFE,
        (
            "うちの男どもも\x01",
            "全員遊びに出かけちゃったわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0xFE,
        "………………………………\x02",
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0xFE,
        (
            "私に家事を押し付けておいて……\x01",
            "よくもそんな真似ができるものだわ……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_47DF")

    label("loc_47A2")


    #C0162
    ChrTalk(
        0xFE,
        (
            "うちの男どもめ……\x01",
            "ふざけた真似をしてくれるじゃない……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_47DF")

    Jump("loc_4A65")

    label("loc_47E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_4849")

    #C0163
    ChrTalk(
        0xFE,
        (
            "ふ～、パレードを間近で\x01",
            "見るなんて何年ぶりかしら。\x02",
        )
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0xFE,
        "久々に興奮しちゃったわ～！\x02",
    )

    CloseMessageWindow()
    Jump("loc_4A65")

    label("loc_4849")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_48AE")

    #C0165
    ChrTalk(
        0xFE,
        "ええと、サモーナ、サモーナ……\x02",
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0xFE,
        (
            "パレードが始まるまで\x01",
            "まだ少し時間があるわね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4A65")

    label("loc_48AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_4979")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_494B")

    #C0167
    ChrTalk(
        0xFE,
        (
            "ふう、家事をサボっていたら\x01",
            "ウチの男どもが騒ぎはじめたのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0xFE,
        (
            "まったく……自分の食事くらい\x01",
            "自分で作ったらどうなのかしら。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_4974")

    label("loc_494B")


    #C0169
    ChrTalk(
        0xFE,
        (
            "記念祭くらい\x01",
            "主婦も休みたいわよね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4974")

    Jump("loc_4A65")

    label("loc_4979")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_4A65")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4A20")

    #C0170
    ChrTalk(
        0xFE,
        "うーん、お祭りはいいわね～。\x02",
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0xFE,
        (
            "お店もセールをするし、\x01",
            "多少の贅沢も許されるし。\x02",
        )
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0xFE,
        (
            "……うふふ、へそくりを\x01",
            "使うなら今って感じよね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_4A65")

    label("loc_4A20")


    #C0173
    ChrTalk(
        0xFE,
        (
            "後で百貨店にも寄ってみようかしら。\x01",
            "欲しいものがあったのよね～。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4A65")

    TalkEnd(0xFE)
    Return()

    # Function_18_46BB end

    def Function_19_4A69(): pass

    label("Function_19_4A69")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_4ACB")

    #C0174
    ChrTalk(
        0xFE,
        "……記念祭・最終日セール！\x02",
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0xFE,
        (
            "ふむふむ、しっかり\x01",
            "買い溜めておかなくちゃ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4CC0")

    label("loc_4ACB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_4B4A")
    OP_63(0xFE, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0176
    ChrTalk(
        0xFE,
        (
            "パレードって……\x01",
            "豪華すぎだよ……\x02",
        )
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0xFE,
        (
            "あんなにミラを\x01",
            "掛けちゃっていいのかなぁ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4CC0")

    label("loc_4B4A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_4BD1")

    #C0178
    ChrTalk(
        0xFE,
        (
            "この時間だと、\x01",
            "買い物を済ませた頃に\x01",
            "パレードが見れるかな。\x02",
        )
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0xFE,
        (
            "……あっちの方が見やすいかも。\x01",
            "ちょっと移動しよう。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4CC0")

    label("loc_4BD1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_4C47")

    #C0180
    ChrTalk(
        0xFE,
        (
            "ふむふむ、\x01",
            "あっちは記念祭セール……\x02",
        )
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0xFE,
        (
            "いやまてよ、この分だと\x01",
            "あっちのお店も安売りしてるかも……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4CC0")

    label("loc_4C47")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_4CC0")
    OP_63(0xFE, 0x0, 1700, 0xE, 0xF, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1200)

    #C0182
    ChrTalk(
        0xFE,
        (
            "記念祭の間はあちこちで\x01",
            "安売りがあって困るよ……\x02",
        )
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0xFE,
        "どこが一番安いのかなぁ……\x02",
    )

    CloseMessageWindow()

    label("loc_4CC0")

    TalkEnd(0xFE)
    Return()

    # Function_19_4A69 end

    def Function_20_4CC4(): pass

    label("Function_20_4CC4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_4D57")

    #C0184
    ChrTalk(
        0xFE,
        (
            "アゼルが、稼いだアルバイト代で\x01",
            "夕食をご馳走してくれるらしいです。\x02",
        )
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0xFE,
        (
            "外食なんて贅沢だけど……\x01",
            "まぁ、たまにはいいですよね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4E5D")

    label("loc_4D57")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_4DD7")

    #C0186
    ChrTalk(
        0xFE,
        (
            "ふふ、随分はしゃいでたから\x01",
            "疲れちゃったのね。\x02",
        )
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0xFE,
        (
            "ユゴット、おんぶしてあげる。\x01",
            "そろそろお家に戻りましょう？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4E5D")

    label("loc_4DD7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_4E5D")
    OP_4B(0x14, 0xFF)

    #C0188
    ChrTalk(
        0xFE,
        "うん、ここでいいはずよ。\x02",
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0xFE,
        (
            "ふふ、子供の頃は姉弟揃って\x01",
            "よく遊んだわよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0x14,
        "そ、そんな昔のこと忘れたって。\x02",
    )

    CloseMessageWindow()
    OP_4C(0x14, 0xFF)

    label("loc_4E5D")

    TalkEnd(0xFE)
    Return()

    # Function_20_4CC4 end

    def Function_21_4E61(): pass

    label("Function_21_4E61")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_4FB2")
    OP_4B(0x14, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4F43")

    #C0191
    ChrTalk(
        0xFE,
        "兄ちゃん、次は何してあそぶ？\x02",
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0xFE,
        (
            "最近のブームはやっぱ\x01",
            "遊撃士ごっこだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0x14,
        "ああ、じゃあソレやろうぜ。\x02",
    )

    CloseMessageWindow()

    #C0194
    ChrTalk(
        0x14,
        (
            "兄ちゃん、今日は何でも\x01",
            "付き合ってやるからな。\x02",
        )
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0xFE,
        "ホント！？　わーい！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_4FA9")

    label("loc_4F43")


    #C0196
    ChrTalk(
        0xFE,
        (
            "じゃあ兄ちゃんは、\x01",
            "悪いマフィアの役ね～！\x02",
        )
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0x14,
        (
            "（そ、そいつには\x01",
            "  怪我させられた思い出が……！）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4FA9")

    OP_4C(0x14, 0xFF)
    Jump("loc_502E")

    label("loc_4FB2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_4FFA")

    #C0198
    ChrTalk(
        0xFE,
        "ん～……パレード楽しかったぁ。\x02",
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0xFE,
        "むにゃむにゃ……\x02",
    )

    CloseMessageWindow()
    Jump("loc_502E")

    label("loc_4FFA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_502E")

    #C0200
    ChrTalk(
        0xFE,
        (
            "ねぇ、パレードは\x01",
            "まだ来ないのかなぁ？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_502E")

    TalkEnd(0xFE)
    Return()

    # Function_21_4E61 end

    def Function_22_5032(): pass

    label("Function_22_5032")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_50A3")

    #C0201
    ChrTalk(
        0xFE,
        (
            "今日は３人で\x01",
            "メシ食いに行く予定なんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0202
    ChrTalk(
        0xFE,
        (
            "どこに行くかなぁ……\x01",
            "やっぱ中央広場辺りかな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5164")

    label("loc_50A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_50ED")

    #C0203
    ChrTalk(
        0xFE,
        "ユゴット、大丈夫か？\x02",
    )

    CloseMessageWindow()

    #C0204
    ChrTalk(
        0xFE,
        "お前はまだ小さいもんなぁ……\x02",
    )

    CloseMessageWindow()
    Jump("loc_5164")

    label("loc_50ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_5164")

    #C0205
    ChrTalk(
        0xFE,
        (
            "家族でパレードを\x01",
            "見ようと思ったんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0206
    ChrTalk(
        0xFE,
        (
            "この通りでいいのかな。\x01",
            "もう一つ向こうじゃなかったっけ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5164")

    TalkEnd(0xFE)
    Return()

    # Function_22_5032 end

    def Function_23_5168(): pass

    label("Function_23_5168")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_520F")
    OP_4B(0x15, 0xFF)
    OP_4B(0x16, 0xFF)

    #C0207
    ChrTalk(
        0x15,
        (
            "さて、今日は港湾区の\x01",
            "公園に行ってみようかのう。\x02",
        )
    )

    CloseMessageWindow()

    #C0208
    ChrTalk(
        0x15,
        (
            "あちらにも屋台が\x01",
            "たくさん出ているそうじゃよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0209
    ChrTalk(
        0x16,
        "わーい、たのしみだね～！\x02",
    )

    CloseMessageWindow()
    OP_4C(0x15, 0xFF)
    OP_4C(0x16, 0xFF)
    Jump("loc_5467")

    label("loc_520F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_535B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5303")
    OP_4B(0x15, 0xFF)
    OP_4B(0x16, 0xFF)

    #C0210
    ChrTalk(
        0x16,
        (
            "ぱれーどを追いかけてたら\x01",
            "帰り道がわらなくなっちゃったね……\x02",
        )
    )

    CloseMessageWindow()

    #C0211
    ChrTalk(
        0x15,
        "ふむ、心配はいらんぞ。\x02",
    )

    CloseMessageWindow()

    #C0212
    ChrTalk(
        0x15,
        (
            "すぐそこに\x01",
            "遊撃士協会の看板が\x01",
            "出ておるからのう。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    #C0213
    ChrTalk(
        0x16,
        (
            "あ、ほんとだ！\x01",
            "よかったぁ！\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x15, 0xFF)
    OP_4C(0x16, 0xFF)
    SetScenarioFlags(0x1, 3)
    Jump("loc_5356")

    label("loc_5303")


    #C0214
    ChrTalk(
        0xFE,
        "すぐそこに遊撃士協会がある。\x02",
    )

    CloseMessageWindow()

    #C0215
    ChrTalk(
        0xFE,
        (
            "どれ、ちょっといって\x01",
            "道を尋ねてこようかい。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5356")

    Jump("loc_5467")

    label("loc_535B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_53A2")

    #C0216
    ChrTalk(
        0xFE,
        (
            "むう……観光に来たのに\x01",
            "買いたくなってしまうのう……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5467")

    label("loc_53A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_53FB")

    #C0217
    ChrTalk(
        0xFE,
        (
            "みやげに良さそうだと\x01",
            "思ったのじゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0218
    ChrTalk(
        0xFE,
        "孫も興味があるようじゃしな。\x02",
    )

    CloseMessageWindow()
    Jump("loc_5467")

    label("loc_53FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_5467")

    #C0219
    ChrTalk(
        0xFE,
        "これがクロスベルの祭りじゃよ。\x02",
    )

    CloseMessageWindow()

    #C0220
    ChrTalk(
        0xFE,
        (
            "何度か来たが、年を追うごとに\x01",
            "派手になっとるようじゃのう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5467")

    TalkEnd(0xFE)
    Return()

    # Function_23_5168 end

    def Function_24_546B(): pass

    label("Function_24_546B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_547F")
    Call(0, 23)
    Jump("loc_5596")

    label("loc_547F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_54D4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_549A")
    Call(0, 23)
    Jump("loc_54CF")

    label("loc_549A")


    #C0221
    ChrTalk(
        0xFE,
        (
            "ついでに遊撃士さんたちに\x01",
            "あっていきたいなぁ～！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_54CF")

    Jump("loc_5596")

    label("loc_54D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_5517")

    #C0222
    ChrTalk(
        0xFE,
        (
            "おばあちゃん、お野菜より\x01",
            "ぱれーどをみようよー！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5596")

    label("loc_5517")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_556B")

    #C0223
    ChrTalk(
        0xFE,
        "かわったモノがいっぱいあるー！\x02",
    )

    CloseMessageWindow()

    #C0224
    ChrTalk(
        0xFE,
        "わーい、おもちゃみたいだー！\x02",
    )

    CloseMessageWindow()
    Jump("loc_5596")

    label("loc_556B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_5596")

    #C0225
    ChrTalk(
        0xFE,
        "すっごいねー、おばあちゃん！\x02",
    )

    CloseMessageWindow()

    label("loc_5596")

    TalkEnd(0xFE)
    Return()

    # Function_24_546B end

    def Function_25_559A(): pass

    label("Function_25_559A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_5666")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5628")

    #C0226
    ChrTalk(
        0xFE,
        (
            "絶対混むと思って\x01",
            "２日目に来てみたんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0227
    ChrTalk(
        0xFE,
        (
            "うーん、さすが記念祭ね。\x01",
            "初日ともそんな違わないみたい。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_5666")

    label("loc_5628")


    #C0228
    ChrTalk(
        0xFE,
        (
            "さすがは記念祭……\x01",
            "昨日に引き続いて\x01",
            "今日も人が多いわー。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5666")

    TalkEnd(0xFE)
    Return()

    # Function_25_559A end

    def Function_26_566A(): pass

    label("Function_26_566A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_576F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5701")

    #C0229
    ChrTalk(
        0xFE,
        (
            "やっとクロスベル市に\x01",
            "戻ってこれたけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0230
    ChrTalk(
        0xFE,
        (
            "記念祭とはいえ、\x01",
            "クロスベル市って\x01",
            "こんなにゴミゴミした所だったっけ？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_576F")

    label("loc_5701")


    #C0231
    ChrTalk(
        0xFE,
        (
            "クロスベル市って\x01",
            "こんなにゴミゴミした所だったっけ？\x02",
        )
    )

    CloseMessageWindow()

    #C0232
    ChrTalk(
        0xFE,
        (
            "アルモリカ村の\x01",
            "のどかさに馴れちゃったのかも……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_576F")

    TalkEnd(0xFE)
    Return()

    # Function_26_566A end

    def Function_27_5773(): pass

    label("Function_27_5773")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB6, 7)), scpexpr(EXPR_END)), "loc_580F")
    TurnDirection(0x19, 0x104, 0)

    #C0233
    ChrTalk(
        0x19,
        (
            "#1604Fクク、あの黒髪の小僧といい、\x01",
            "楽しませてくれるじゃねえか。\x02\x03",

            "#1602Fワジと合わせて、いずれ全員、\x01",
            "俺様がブチのめしてやるぜ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5AAD")

    label("loc_580F")


    #C0234
    ChrTalk(
        0x19,
        (
            "#1600Fよお、テメエらか。\x02\x03",

            "#1602Fクク……\x01",
            "疲れた顔してるじゃねえか。\x02",
        )
    )

    CloseMessageWindow()

    #C0235
    ChrTalk(
        0x101,
        (
            "#0003Fそっちは元気そうだな。\x02\x03",

            "#0001Fっていうか、またどこかに\x01",
            "出向くつもりなんじゃ……\x02",
        )
    )

    CloseMessageWindow()

    #C0236
    ChrTalk(
        0x19,
        (
            "#1602Fクク、文句あるかよ？\x02\x03",

            "祭りをどう過ごそうが\x01",
            "俺たちの勝手だろうが。\x02",
        )
    )

    CloseMessageWindow()

    #C0237
    ChrTalk(
        0x102,
        "#0106F（はぁ、何ていうか……）\x02",
    )

    CloseMessageWindow()

    #C0238
    ChrTalk(
        0x103,
        "#0203F（付き合いきれませんね。）\x02",
    )

    CloseMessageWindow()
    OP_63(0x19, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0x19, 0x104, 750)
    Sleep(750)

    #C0239
    ChrTalk(
        0x19,
        (
            "#1601Fそういや赤毛……\x01",
            "今度サシで勝負させろや。\x02\x03",

            "#1602Fあんな物を見せられちゃ、\x01",
            "黙ってられねえタチなんでなァ。\x02",
        )
    )

    CloseMessageWindow()

    #C0240
    ChrTalk(
        0x104,
        (
            "#0306Fいや……マジで勘弁してくれ。\x02\x03",

            "#0301F昨日はつい調子に\x01",
            "乗っちまったんだっての。\x02",
        )
    )

    CloseMessageWindow()

    #C0241
    ChrTalk(
        0x19,
        (
            "#1604F……ますます面白え。\x01",
            "本気のてめえと\x01",
            "闘りたくなってきたぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0242
    ChrTalk(
        0x104,
        (
            "#0306Fとほほ……\x01",
            "やっぱあれは失敗だったな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xB6, 7)

    label("loc_5AAD")

    TalkEnd(0xFE)
    Return()

    # Function_27_5773 end

    def Function_28_5AB1(): pass

    label("Function_28_5AB1")

    TalkBegin(0xFE)

    #C0243
    ChrTalk(
        0x1A,
        "ヴァルドさ～ん、今日はどこ行くよ。\x02",
    )

    CloseMessageWindow()

    #C0244
    ChrTalk(
        0x1A,
        (
            "オゥ、イェエエ～ッ……！！\x01",
            "オレ中央広場に行きてえかもよ～？\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_28_5AB1 end

    def Function_29_5B21(): pass

    label("Function_29_5B21")

    TalkBegin(0xFE)

    #C0245
    ChrTalk(
        0x1B,
        (
            "俺たちにも\x01",
            "祭りに出る権利がある。\x02",
        )
    )

    CloseMessageWindow()

    #C0246
    ChrTalk(
        0x1B,
        (
            "サツに口出しされる\x01",
            "筋合いはねえぜ。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_29_5B21 end

    def Function_30_5B78(): pass

    label("Function_30_5B78")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_5BB8")

    #C0247
    ChrTalk(
        0x1C,
        (
            "ヴァルドさん、\x01",
            "俺ジュース買ってきますよ！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5C12")

    label("loc_5BB8")


    #C0248
    ChrTalk(
        0x1C,
        (
            "やっぱ不良なら\x01",
            "家族より仲間だよな！\x02",
        )
    )

    CloseMessageWindow()

    #C0249
    ChrTalk(
        0x1C,
        "祭りは仲間で過ごすもんだぜ！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x1C, 0x19, 0)
    SetChrFlags(0x1C, 0x10)
    SetScenarioFlags(0x1, 4)

    label("loc_5C12")

    TalkEnd(0xFE)
    Return()

    # Function_30_5B78 end

    def Function_31_5C16(): pass

    label("Function_31_5C16")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SoundLoad(885)
    Sound(885, 2, 90, 0)
    FadeToBright(2000, 0)
    LoadEffect(0x7, "event\\ev308_00.eff")
    PlayEffect(0x7, 0xFF, 0xFF, 0x0, 7970, -300, 790, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x7, 0xFF, 0xFF, 0x0, -3800, -3000, -5130, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x7, 0xFF, 0xFF, 0x0, -12310, -3000, -300, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrPos(0x0, -7080, -3000, 1450, 135)
    SetChrPos(0x1, -7080, -3000, 1450, 135)
    SetChrPos(0x2, -7080, -3000, 1450, 135)
    SetChrPos(0x3, -7080, -3000, 1450, 135)
    SetChrFlags(0x0, 0x80)
    SetChrBattleFlags(0x0, 0x8000)
    SetChrFlags(0x1, 0x80)
    SetChrBattleFlags(0x1, 0x8000)
    SetChrFlags(0x2, 0x80)
    SetChrBattleFlags(0x2, 0x8000)
    SetChrFlags(0x3, 0x80)
    SetChrBattleFlags(0x3, 0x8000)
    OP_68(2040, -1400, -8500, 0)
    MoveCamera(89, 17, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(22500, 0)
    OP_68(-16140, -1400, 1060, 10000)
    MoveCamera(37, 30, 0, 10000)
    OP_6E(600, 10000)
    SetCameraDistance(25000, 10000)
    Sleep(8000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_24(0x375)
    SetScenarioFlags(0x5C, 0)
    NewScene("c120C", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_31_5C16 end

    def Function_32_5DD4(): pass

    label("Function_32_5DD4")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(25400, 700, 500, 0)
    MoveCamera(47, 27, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(22500, 0)
    SetChrPos(0x101, 29700, -300, -100, 270)
    SetChrPos(0x102, 29700, -300, 1100, 270)
    SetChrPos(0x103, 31100, -300, -100, 270)
    SetChrPos(0x104, 31100, -300, 1100, 270)
    OP_4B(0xC, 0xFF)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    OP_4B(0xD, 0xFF)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)

    def lambda_5E73():
        OP_98(0xFE, 0xFFFFEC78, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5E73)
    Sleep(50)

    def lambda_5E90():
        OP_98(0xFE, 0xFFFFEC78, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5E90)
    Sleep(50)

    def lambda_5EAD():
        OP_98(0xFE, 0xFFFFEC78, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5EAD)
    Sleep(50)

    def lambda_5ECA():
        OP_98(0xFE, 0xFFFFEC78, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_5ECA)
    SetCameraDistance(20500, 2500)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    OP_6F(0x10)

    #C0250
    ChrTalk(
        0x104,
        (
            "#11P#0305Fそういや、もう昼過ぎか。\x02\x03",

            "#0306Fどうやらパレードは\x01",
            "もう終わっちまったみてぇだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0251
    ChrTalk(
        0x103,
        (
            "#0208F……残念です。\x01",
            "（みっしぃが乗った車があると\x01",
            "  聞いたのですが……）\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 500)

    #C0252
    ChrTalk(
        0x101,
        (
            "#6P#0006F古戦場での捜索が\x01",
            "思った以上に大変だったからな……\x02\x03",

            "#0000Fとりあえず、俺たちも一旦、\x01",
            "支援課に戻って一息入れるか。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_603E():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_603E)
    Sleep(50)
    TurnDirection(0x104, 0x101, 500)

    #C0253
    ChrTalk(
        0x102,
        "#0102Fええ、そうしましょう。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, 24700, -300, 500, 270)
    OP_4C(0xC, 0xFF)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    OP_4C(0xD, 0xFF)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    ClearMapFlags(0x10000000)
    SetScenarioFlags(0xAA, 2)
    OP_29(0x44, 0x1, 0x6)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_60CE")
    OP_29(0x20, 0x4, 0x40)
    Jump("loc_60E0")

    label("loc_60CE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_60E0")
    OP_29(0x20, 0x4, 0x40)

    label("loc_60E0")

    EventEnd(0x5)
    Return()

    # Function_32_5DD4 end

    def Function_33_60E3(): pass

    label("Function_33_60E3")

    EventBegin(0x0)
    OP_EE(0x0, 0x1)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch07300.itc", 0x1E)
    LoadChrToIndex("chr/ch24100.itc", 0x1F)
    LoadChrToIndex("apl/ch50388.itc", 0x20)
    LoadChrToIndex("apl/ch50389.itc", 0x21)
    ClearChrFlags(0x1D, 0x80)
    ClearChrBattleFlags(0x1D, 0x8000)
    SetChrChipByIndex(0x1D, 0x1E)
    SetChrSubChip(0x1D, 0x0)
    ClearChrFlags(0x1E, 0x80)
    ClearChrBattleFlags(0x1E, 0x8000)
    SetChrChipByIndex(0x1E, 0x1F)
    SetChrSubChip(0x1E, 0x0)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x1, 0x13)"), scpexpr(EXPR_END)), "loc_617A")
    Call(0, 34)
    Jump("loc_618A")

    label("loc_617A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x1, 0x14)"), scpexpr(EXPR_END)), "loc_618A")
    Call(0, 35)

    label("loc_618A")

    OP_EE(0x0, 0xA)
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x1D, 0x80)
    SetChrBattleFlags(0x1D, 0x8000)
    SetChrFlags(0x1E, 0x80)
    SetChrBattleFlags(0x1E, 0x8000)
    OP_49()
    OP_D5(0x1E)
    OP_D5(0x1F)
    SetScenarioFlags(0x5C, 0)
    NewScene("c115C", 102, 0, 0)
    IdleLoop()
    Return()

    # Function_33_60E3 end

    def Function_34_61CE(): pass

    label("Function_34_61CE")

    OP_68(10180, 1450, 550, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(11550, 0)
    SetChrPos(0x1D, -4130, -300, 4860, 315)
    SetChrPos(0x1E, 24040, -300, 870, 270)
    SetChrPos(0x101, 24000, -300, 0, 270)
    SetChrPos(0x102, 25000, -300, 1500, 270)
    SetChrPos(0x103, 26000, -300, 0, 270)
    SetChrPos(0x104, 27000, -300, 1500, 270)

    def lambda_6267():
        OP_95(0xFE, -60, -300, 660, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_6267)
    OP_68(-5970, 1450, 2950, 8500)
    BeginChrThread(0x1E, 3, 0, 42)
    FadeToBright(1000, 0)
    OP_0D()

    #C0254
    ChrTalk(
        0x1E,
        "#5P#10Aはぁ、はぁ。\x02",
    )
    #Auto

    OP_5A()

    #C0255
    ChrTalk(
        0x1E,
        (
            "#5P#10Aなめるんじゃないよ\x01",
            "クソガキどもめ……\x02",
        )
    )
    #Auto

    OP_5A()

    #C0256
    ChrTalk(
        0x1E,
        (
            "#5P#10A見てな、若い頃に\x01",
            "登山で鍛えたこの足腰で、\x01",
            "なんとしても逃げ切って……\x02",
        )
    )
    #Auto

    OP_5A()
    Sleep(1200)

    def lambda_6341():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_6341)
    WaitChrThread(0x1D, 1)
    SetChrChipByIndex(0x1D, 0x20)
    SetChrSubChip(0x1D, 0x0)
    Sound(804, 0, 100, 0)
    Sleep(150)
    SetChrSubChip(0x1D, 0x1)
    WaitChrThread(0x1E, 3)
    SetChrFlags(0x1E, 0x20)
    SetChrFlags(0x1E, 0x2)

    def lambda_6375():
        OP_95(0xFE, -6500, -300, 5000, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_6375)
    Sound(814, 0, 100, 0)
    SetChrChipByIndex(0x1E, 0x21)
    SetChrSubChip(0x1E, 0x0)
    Sleep(300)
    SetChrSubChip(0x1E, 0x1)
    Sound(819, 0, 100, 0)
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    #C0257
    ChrTalk(
        0x1E,
        "#6P#5Sぎゃんっ！！\x02",
    )

    CloseMessageWindow()
    OP_63(0x1D, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1500)
    SetChrSubChip(0x1D, 0x0)
    Sleep(100)
    SetChrChipByIndex(0x1D, 0x1E)
    OP_93(0x1D, 0x10E, 0x12C)

    #C0258
    ChrTalk(
        0x1D,
        (
            "#11P#3400Fあら……うっかり足を\x01",
            "突き出してしまったわ。\x02\x03",

            "お婆さん、大丈夫かしら？\x02",
        )
    )

    CloseMessageWindow()

    #C0259
    ChrTalk(
        0x1E,
        (
            "#6Pき……キサマ……\x01",
            "なにをするんじゃ……\x02",
        )
    )

    CloseMessageWindow()

    #C0260
    ChrTalk(
        0x1D,
        (
            "#11P#3404F……フフ。\x01",
            "元気な人だこと。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Fade(1000)
    OP_68(11280, 1450, -20, 0)
    MoveCamera(45, 21, 0, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    BeginChrThread(0x101, 3, 0, 36)
    BeginChrThread(0x102, 3, 0, 36)
    BeginChrThread(0x103, 3, 0, 36)
    BeginChrThread(0x104, 3, 0, 36)
    OP_68(-2430, 1450, -2420, 7000)
    OP_0D()

    #C0261
    ChrTalk(
        0x101,
        (
            "#0001F#6P#10Aくそっ、あの速さじゃ\x01",
            "もうかなり遠くに……\x02",
        )
    )
    #Auto

    OP_5A()

    #C0262
    ChrTalk(
        0x102,
        "#0105F#6P#10Aロイド、見て、あれ！\x02",
    )
    #Auto

    OP_5A()

    #C0263
    ChrTalk(
        0x101,
        "#0005F#6P#10Aえ……\x02",
    )
    #Auto

    OP_5A()
    Fade(1000)
    OP_68(-4840, 1650, 1400, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(12680, 0)
    OP_0D()
    WaitChrThread(0x101, 3)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x103, 3)
    WaitChrThread(0x104, 3)

    #C0264
    ChrTalk(
        0x101,
        (
            "#12P#0005Fこ……\x01",
            "こんなところで倒れてる！？\x02",
        )
    )

    CloseMessageWindow()

    #C0265
    ChrTalk(
        0x104,
        (
            "#11P#0305Fうおお、黒髪のお姉さんじゃ\x01",
            "ないッスか！\x02\x03",

            "#0301Fもしかしてこれ……\x01",
            "お姉さんが！？\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x1D, 0x87, 0xE1)

    #C0266
    ChrTalk(
        0x1D,
        (
            "#5P#3403F……話は後よ。\x01",
            "それより、早くしないと。\x02\x03",

            "#3400Fこのお婆さん、\x01",
            "かなり元気な方みたいだから\x01",
            "すぐ復活してしまうわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0267
    ChrTalk(
        0x1E,
        "#6Pち、ちくしょぉ～……！\x02",
    )

    CloseMessageWindow()

    #C0268
    ChrTalk(
        0x101,
        (
            "#12P#0001F……そうみたいですね。\x01",
            "エリィ、頼む。\x02",
        )
    )

    CloseMessageWindow()

    #C0269
    ChrTalk(
        0x102,
        "#5P#0105Fえ、ええ。\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x101, 3, 0, 37)
    BeginChrThread(0x102, 3, 0, 38)
    BeginChrThread(0x103, 3, 0, 39)
    BeginChrThread(0x104, 3, 0, 40)
    Sleep(2000)
    BeginChrThread(0x1D, 3, 0, 41)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x103, 3)
    WaitChrThread(0x104, 3)
    WaitChrThread(0x1D, 3)

    #C0270
    ChrTalk(
        0x103,
        (
            "#12P#0200Fすみませんが、一応あなたも\x01",
            "同行していただけますか？\x02\x03",

            "#0203Fどうやら、逮捕に\x01",
            "協力していただいたようですし。\x02",
        )
    )

    CloseMessageWindow()

    #C0271
    ChrTalk(
        0x1D,
        (
            "#5P#3403F……分かったわ。\x02\x03",

            "#3400Fあまり目立つ事はしたくなかったけど、\x01",
            "これも巡り合わせ……\x02",
        )
    )

    CloseMessageWindow()

    #C0272
    ChrTalk(
        0x104,
        (
            "#11P#0303Fご安心を！\x02\x03",

            "#0309Fお姉さんは、この俺が丁重に\x01",
            "エスコートさせてもらいますんで！\x02",
        )
    )

    CloseMessageWindow()
    Return()

    # Function_34_61CE end

    def Function_35_68CB(): pass

    label("Function_35_68CB")

    OP_68(19130, 1850, -1230, 0)
    MoveCamera(39, 20, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(14450, 0)
    SetChrPos(0x1E, 24040, -300, 870, 270)
    SetChrPos(0x101, 30000, -300, 0, 270)
    SetChrPos(0x102, 31000, -300, 1500, 270)
    SetChrPos(0x103, 32000, -300, 0, 270)
    SetChrPos(0x104, 33000, -300, 1500, 270)
    OP_A7(0x1D, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_695E():
        OP_95(0xFE, 20000, -300, 1030, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_695E)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x1E, 1)
    OP_63(0x1E, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0x1E)

    #N0273
    NpcTalk(
        0x1E,
        "お婆さん",
        (
            "#5P……フフ……\x01",
            "ついにクロスベルに着いたわ。\x02",
        )
    )

    CloseMessageWindow()

    #N0274
    NpcTalk(
        0x1E,
        "お婆さん",
        (
            "#5P後は駅と空港にいる\x01",
            "あの子たちと合流して、\x01",
            "適当な場所に店を出すだけ。\x02",
        )
    )

    CloseMessageWindow()

    #N0275
    NpcTalk(
        0x1E,
        "お婆さん",
        (
            "#5P毎年毎年、大儲けさせてくれて……\x01",
            "本当にこのクロスベルって所は\x01",
            "ミラの成る木ね。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(400, 20, -1, -1)
    SetChrName("ロイド")

    #A0276
    AnonymousTalk(
        0xFF,
        (
            "#0001F……ちょ、ちょっと\x01",
            "待ってください！\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(14, 280, 60, 3)

    #N0277
    NpcTalk(
        0x1E,
        "お婆さん",
        "#5P……？\x02",
    )

    CloseMessageWindow()
    OP_68(21470, 1850, -490, 3000)
    OP_93(0x1E, 0x5A, 0x1F4)

    def lambda_6B08():
        OP_98(0xFE, 0xFFFFE890, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6B08)

    def lambda_6B22():
        OP_98(0xFE, 0xFFFFE890, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6B22)

    def lambda_6B3C():
        OP_98(0xFE, 0xFFFFE890, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_6B3C)

    def lambda_6B56():
        OP_98(0xFE, 0xFFFFE890, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_6B56)

    def lambda_6B70():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6B70)

    def lambda_6B81():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_6B81)

    def lambda_6B92():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_6B92)

    def lambda_6BA3():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_6BA3)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x101, 2)
    WaitChrThread(0x102, 2)
    WaitChrThread(0x103, 2)
    WaitChrThread(0x104, 2)
    OP_6F(0x1)

    #C0278
    ChrTalk(
        0x101,
        (
            "#0003F#11Pクロスベル警察、\x01",
            "特務支援課の者です。\x02\x03",

            "#0001Fお婆さん……すみませんが、\x01",
            "少々、話をお聞かせ願えませんか？\x02",
        )
    )

    CloseMessageWindow()

    #N0279
    NpcTalk(
        0x1E,
        "お婆さん",
        "#6P……警察……ですって？\x02",
    )

    CloseMessageWindow()

    #N0280
    NpcTalk(
        0x1E,
        "お婆さん",
        (
            "#6Pけ、警察が一体、\x01",
            "私になんのご用なのかしら。\x02",
        )
    )

    CloseMessageWindow()

    #N0281
    NpcTalk(
        0x1E,
        "お婆さん",
        (
            "#6Pこれから、孫の所に\x01",
            "行かなければならないんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0282
    ChrTalk(
        0x101,
        (
            "#11P#0001F……もうネタは上がってるんです。\x01",
            "恐らく、あなたが偽ブランド業者の\x01",
            "リーダー格であることも。\x02",
        )
    )

    CloseMessageWindow()

    #N0283
    NpcTalk(
        0x1E,
        "お婆さん",
        "#6P……！！\x02",
    )

    CloseMessageWindow()

    #C0284
    ChrTalk(
        0x102,
        (
            "#11P#0101F任意同行していただければ、\x01",
            "手荒い真似はいたしません。\x02\x03",

            "#0103Fどうか、大人しく……\x02",
        )
    )

    CloseMessageWindow()

    #N0285
    NpcTalk(
        0x1E,
        "お婆さん",
        "#6P……………………な……\x02",
    )

    CloseMessageWindow()
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    #C0286
    ChrTalk(
        0x1E,
        (
            "#6P#5S……なめるんじゃないよ\x01",
            "クソガキどもぉぉおおお！！\x02",
        )
    )

    CloseMessageWindow()

    #C0287
    ChrTalk(
        0x101,
        "#11P#0011F……ええ！！？\x02",
    )

    CloseMessageWindow()

    #C0288
    ChrTalk(
        0x102,
        "#11P#0105Fきゃあ！！\x02",
    )

    CloseMessageWindow()

    #C0289
    ChrTalk(
        0x104,
        "#11P#0305Fな、なんだぁ……！？\x02",
    )

    CloseMessageWindow()

    #C0290
    ChrTalk(
        0x103,
        "#12P#0201F……正体を現しましたね。\x02",
    )

    CloseMessageWindow()
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    #C0291
    ChrTalk(
        0x1E,
        (
            "#6P#5Sアタシをパクろうったって、\x01",
            "そうはいくかい！\x02",
        )
    )

    CloseMessageWindow()
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    #C0292
    ChrTalk(
        0x1E,
        (
            "#6P#5Sこうなったら、逃げて逃げて、\x01",
            "地の果てまでも逃げ通してやるさ！\x02",
        )
    )

    CloseMessageWindow()

    #C0293
    ChrTalk(
        0x1E,
        (
            "#6P#5Sこのアタシを\x01",
            "捕まえられるものなら……\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0x7D0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_6FB8():
        OP_98(0xFE, 0xFFFFFE0C, 0x0, 0xFFFFFE0C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_6FB8)
    Sleep(1000)

    def lambda_6FD5():
        OP_98(0xFE, 0xFFFFFE0C, 0x0, 0x1F4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_6FD5)
    Sleep(1000)

    def lambda_6FF2():
        OP_95(0xFE, 15000, -300, 1030, 10000, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_6FF2)
    Sound(250, 0, 80, 0)
    PlayBGM("ed7401", 0)
    OP_82(0x0, 0x64, 0xBB8, 0xC8)
    SetMessageWindowPos(-50, 200, -1, -1)
    SetChrName("偽ブランド商")

    #A0294
    AnonymousTalk(
        0x1E,
        "#5S捕まえてみせなぁああ！！！\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0295
    ChrTalk(
        0x101,
        "#11P#0011F……ま、まずい、逃げるぞ！！\x02",
    )

    CloseMessageWindow()

    #C0296
    ChrTalk(
        0x104,
        (
            "#11P#0306Fちっ、さっきまでの\x01",
            "上品なお婆さんキャラは\x01",
            "どこにいっちまったんだよ！\x02",
        )
    )

    CloseMessageWindow()

    #C0297
    ChrTalk(
        0x103,
        "#12P#0205F……驚きです。\x02",
    )

    CloseMessageWindow()

    #C0298
    ChrTalk(
        0x102,
        (
            "#11P#0106Fも、もう！　呆けてる場合！？\x02\x03",

            "#0101F速く追わないと……\x01",
            "本当に逃げる気よ、アレ！\x02",
        )
    )

    CloseMessageWindow()

    #C0299
    ChrTalk(
        0x101,
        (
            "#11P#0001Fそ、そうだな……\x01",
            "行くぞ、みんな！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_71FB():
        OP_98(0xFE, 0xFFFFD8F0, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_71FB)

    def lambda_7215():
        OP_98(0xFE, 0xFFFFD8F0, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7215)

    def lambda_722F():
        OP_98(0xFE, 0xFFFFD8F0, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_722F)

    def lambda_7249():
        OP_98(0xFE, 0xFFFFD8F0, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_7249)
    Sleep(1500)
    FadeToDark(500, 0, -1)
    OP_0D()
    SetChrPos(0x1E, 11450, -300, 1000, 270)
    SetChrPos(0x101, 24000, -300, 0, 270)
    SetChrPos(0x102, 25000, -300, 1500, 270)
    SetChrPos(0x103, 26000, -300, 0, 270)
    SetChrPos(0x104, 27000, -300, 1500, 270)
    SetChrPos(0x1D, 8000, -300, 190, 270)
    OP_68(9270, 1450, -1540, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(11550, 0)
    OP_68(-5970, 1450, 2950, 5000)
    BeginChrThread(0x1E, 3, 0, 42)
    BeginChrThread(0x101, 3, 0, 36)
    BeginChrThread(0x102, 3, 0, 36)
    BeginChrThread(0x103, 3, 0, 36)
    BeginChrThread(0x104, 3, 0, 36)
    FadeToBright(500, 0)
    OP_0D()

    #C0300
    ChrTalk(
        0x1E,
        (
            "#5P#10Aなめるんじゃないよ\x01",
            "クソガキどもめ！\x02",
        )
    )
    #Auto

    OP_5A()

    #C0301
    ChrTalk(
        0x1E,
        (
            "#5P#10A若い頃に登山で鍛えたこの足腰、\x01",
            "追いつけるものなら追いついて……\x02",
        )
    )
    #Auto

    OP_5A()
    WaitChrThread(0x1E, 3)
    SetChrFlags(0x1E, 0x20)
    SetChrFlags(0x1E, 0x2)

    def lambda_73C8():
        OP_95(0xFE, -6500, -300, 5000, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_73C8)
    Sound(814, 0, 100, 0)
    SetChrChipByIndex(0x1E, 0x21)
    SetChrSubChip(0x1E, 0x0)
    Sleep(300)
    SetChrSubChip(0x1E, 0x1)
    Sound(819, 0, 100, 0)
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    #C0302
    ChrTalk(
        0x1E,
        "#6P#5Sぎゃんっ！！\x02",
    )

    OP_5A()
    OP_68(-4030, 1450, 1640, 2000)
    MoveCamera(45, 21, 0, 2000)
    OP_6E(600, 2000)
    SetCameraDistance(12760, 2000)
    OP_6F(0x1)

    #C0303
    ChrTalk(
        0x102,
        "#11P#0105F……お、お婆さん！？\x02",
    )

    CloseMessageWindow()

    #C0304
    ChrTalk(
        0x104,
        "#11P#0305Fうへ……顔面から転んだぞ、おい。\x02",
    )

    CloseMessageWindow()

    #C0305
    ChrTalk(
        0x103,
        "#12P#0206F痛そうです。\x02",
    )

    CloseMessageWindow()

    #C0306
    ChrTalk(
        0x101,
        (
            "#12P#0003Fちょっとかわいそうだけど……\x01",
            "このまま確保しよう！\x02",
        )
    )

    CloseMessageWindow()
    OP_68(-5970, 1450, 2950, 2000)
    BeginChrThread(0x101, 3, 0, 37)
    BeginChrThread(0x102, 3, 0, 38)
    BeginChrThread(0x103, 3, 0, 43)
    BeginChrThread(0x104, 3, 0, 44)
    Sleep(2000)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x103, 3)
    WaitChrThread(0x104, 3)

    #C0307
    ChrTalk(
        0x104,
        (
            "#11P#0306Fふぃー、とりあえず\x01",
            "逃げられずに済んでよかったな。\x02\x03",

            "#0300F歳なんだから無理すんなよバーさん。\x02",
        )
    )

    CloseMessageWindow()

    #C0308
    ChrTalk(
        0x1E,
        (
            "#6Pぬぐぐ……！\x01",
            "誰がバーさんじゃ、デクノボーめ……！\x02",
        )
    )

    CloseMessageWindow()

    #C0309
    ChrTalk(
        0x103,
        (
            "#12P#0203Fこれで……\x01",
            "なんとか確保できましたね。\x02\x03",

            "#0200Fでも、それもこれも……\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("女性の声")
    SetMessageWindowPos(350, 0, -1, -1)

    #C0310
    ChrTalk(
        0x1D,
        "……お見事だったわ。\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_76BC():
        TurnDirection(0xFE, 0x1D, 300)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_76BC)

    def lambda_76C9():
        TurnDirection(0xFE, 0x1D, 300)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_76C9)

    def lambda_76D6():
        TurnDirection(0xFE, 0x1D, 300)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_76D6)

    def lambda_76E3():
        TurnDirection(0xFE, 0x1D, 300)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_76E3)
    OP_A7(0x1D, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    BeginChrThread(0x1D, 3, 0, 45)
    OP_68(-3950, 1450, 1920, 2000)
    WaitChrThread(0x1D, 3)

    #C0311
    ChrTalk(
        0x1D,
        (
            "#3404Fフフ……\x01",
            "警察の捕り物を見たのは\x01",
            "生まれて初めてかもしれない。\x02",
        )
    )

    CloseMessageWindow()

    #C0312
    ChrTalk(
        0x101,
        (
            "#0005Fあ……\x02\x03",

            "#0004F助言、ありがとうございます。\x01",
            "あと一歩で取り逃がす所でした。\x02",
        )
    )

    CloseMessageWindow()

    #C0313
    ChrTalk(
        0x104,
        (
            "#0309Fいや～、ホント間一髪だったな。\x01",
            "お姉さんのおかげッスよ！\x02",
        )
    )

    CloseMessageWindow()

    #C0314
    ChrTalk(
        0x103,
        (
            "#12P#0200Fお婆さんがつまずく、\x01",
            "なんて幸運もありましたしね。\x02",
        )
    )

    CloseMessageWindow()

    #C0315
    ChrTalk(
        0x102,
        (
            "#0104F道に落ちてた石に\x01",
            "つまずいちゃったみたい。\x02\x03",

            "#0100F顔からこけてたけど、\x01",
            "わりと軽傷みたいよ。\x02\x03",

            "#0103Fなんていうか……\x01",
            "いくつもの偶然が重なった感じね。\x02",
        )
    )

    CloseMessageWindow()

    #C0316
    ChrTalk(
        0x1D,
        (
            "#3403F全てのものはあるべき所に\x01",
            "収まるようになっている。\x02\x03",

            "お婆さんが転んだのも、\x01",
            "偶然ではなく必然……\x02\x03",

            "#3400F……残念だったわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0317
    ChrTalk(
        0x1E,
        "#6Pち、ちくしょぉ～……！\x02",
    )

    CloseMessageWindow()

    #C0318
    ChrTalk(
        0x101,
        (
            "#0001F……早いところ、\x01",
            "本部の方に連行しよう。\x02\x03",

            "#0006Fまた逃げられても敵わないし。\x02",
        )
    )

    CloseMessageWindow()

    #C0319
    ChrTalk(
        0x102,
        "#0100Fええ、そうね。\x02",
    )

    CloseMessageWindow()

    #C0320
    ChrTalk(
        0x103,
        (
            "#12P#0200Fすみませんが、一応あなたも\x01",
            "同行していただけますか？\x02\x03",

            "逮捕に協力していただきましたし、\x01",
            "形式的にでも事情を\x01",
            "聞かせていただかないと……\x02",
        )
    )

    CloseMessageWindow()

    #C0321
    ChrTalk(
        0x1D,
        (
            "#3404F……分かったわ。\x02\x03",

            "#3400Fあまり目立つ事はしたくなかったけど、\x01",
            "これも巡り合わせ……\x02",
        )
    )

    CloseMessageWindow()

    #C0322
    ChrTalk(
        0x104,
        (
            "#0304Fご安心を！\x02\x03",

            "#0309Fお姉さんは、この俺が丁重に\x01",
            "エスコートさせてもらいますんで！\x02",
        )
    )

    CloseMessageWindow()
    Return()

    # Function_35_68CB end

    def Function_36_7B31(): pass

    label("Function_36_7B31")


    def lambda_7B36():
        OP_98(0xFE, 0xFFFF9A70, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7B36)
    WaitChrThread(0xFE, 1)

    def lambda_7B54():
        OP_93(0xFE, 0x13B, 0x12C)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7B54)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_36_7B31 end

    def Function_37_7B61(): pass

    label("Function_37_7B61")

    OP_68(-5580, 1450, 2490, 3000)

    def lambda_7B77():
        OP_95(0xFE, -7010, -300, 4430, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7B77)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x2D, 0x12C)
    Return()

    # Function_37_7B61 end

    def Function_38_7B98(): pass

    label("Function_38_7B98")


    def lambda_7B9D():
        OP_95(0xFE, -5410, -300, 4430, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7B9D)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_38_7B98 end

    def Function_39_7BB7(): pass

    label("Function_39_7BB7")


    def lambda_7BBC():
        OP_95(0xFE, -4750, -300, 2009, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7BBC)
    WaitChrThread(0xFE, 1)
    TurnDirection(0xFE, 0x1D, 300)
    Return()

    # Function_39_7BB7 end

    def Function_40_7BDD(): pass

    label("Function_40_7BDD")


    def lambda_7BE2():
        OP_95(0xFE, -3190, -300, 2410, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7BE2)
    WaitChrThread(0xFE, 1)
    TurnDirection(0xFE, 0x1D, 300)
    Return()

    # Function_40_7BDD end

    def Function_41_7C03(): pass

    label("Function_41_7C03")


    def lambda_7C08():
        OP_95(0xFE, -3800, -300, 3830, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7C08)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xB4, 0x12C)
    Return()

    # Function_41_7C03 end

    def Function_42_7C29(): pass

    label("Function_42_7C29")


    def lambda_7C2E():
        OP_95(0xFE, -60, -300, 660, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_7C2E)
    WaitChrThread(0x1E, 1)

    def lambda_7C4C():
        OP_95(0xFE, -5000, -300, 4000, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_7C4C)
    WaitChrThread(0x1E, 1)
    Return()

    # Function_42_7C29 end

    def Function_43_7C66(): pass

    label("Function_43_7C66")


    def lambda_7C6B():
        OP_95(0xFE, -4750, -300, 2009, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7C6B)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_43_7C66 end

    def Function_44_7C85(): pass

    label("Function_44_7C85")


    def lambda_7C8A():
        OP_95(0xFE, -4190, -300, 4030, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7C8A)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_44_7C85 end

    def Function_45_7CA4(): pass

    label("Function_45_7CA4")


    def lambda_7CA9():
        OP_98(0xFE, 0xFFFFE0C0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7CA9)
    WaitChrThread(0xFE, 1)

    def lambda_7CC7():
        TurnDirection(0xFE, 0x1D, 300)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7CC7)

    def lambda_7CD4():
        TurnDirection(0xFE, 0x1D, 300)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7CD4)

    def lambda_7CE1():
        TurnDirection(0xFE, 0x1D, 300)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_7CE1)

    def lambda_7CEE():
        TurnDirection(0xFE, 0x1D, 300)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_7CEE)

    def lambda_7CFB():
        OP_95(0xFE, -2870, -300, 2070, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7CFB)
    OP_68(-5360, 1450, 2770, 2000)
    WaitChrThread(0xFE, 1)

    def lambda_7D2A():
        OP_93(0xFE, 0x13B, 0x12C)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7D2A)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_45_7CA4 end

    def Function_46_7D37(): pass

    label("Function_46_7D37")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x98, 7)), scpexpr(EXPR_END)), "loc_7D71")
    SetChrName("")

    #A0323
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "東方風の地蔵が奉られている。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_9999")

    label("loc_7D71")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x98, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7F3B")
    SetChrName("")

    #A0324
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "東方風の地蔵が奉られている。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0325
    ChrTalk(
        0x104,
        (
            "#0305Fへえ、東方風の\x01",
            "街並みだとは思ってたが。\x01",
            "地蔵まで奉られてんのかよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0326
    ChrTalk(
        0x103,
        (
            "#0200F見るのは初めてかもしれません。\x01",
            "……大きいお顔ですね。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0327
    ChrTalk(
        0x103,
        "#0205Fこの地蔵の前の台座は……？\x02",
    )

    CloseMessageWindow()

    #C0328
    ChrTalk(
        0x102,
        (
            "#0100Fきっと料理を\x01",
            "お供えするための台座ね。\x02\x03",

            "上手にできた料理があれば\x01",
            "お供えしてみたらどうかしら。\x02",
        )
    )

    CloseMessageWindow()

    #C0329
    ChrTalk(
        0x101,
        (
            "#0000Fそうだな、支援課は基本自炊だし。\x02\x03",

            "うまくできた料理があれば\x01",
            "今度持ってきてみよう。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x98, 0)
    Jump("loc_9999")

    label("loc_7F3B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_END)), "loc_7F72")
    SetChrName("")

    #A0330
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "東方風の地蔵が奉られている。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_9999")

    label("loc_7F72")

    Call(0, 47)
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8000")
    SetChrName("")

    #A0331
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "東方風の地蔵が奉られている。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0332
    ChrTalk(
        0x101,
        (
            "#0000Fお供えするのに良さそうな\x01",
            "料理は今は無いな。\x02\x03",

            "今度持ってきてみよう。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFF)
    Return()

    label("loc_8000")

    Call(0, 48)
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x98, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_825F")
    SetChrName("")

    #A0333
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "輝くクオーツと共に\x01",
            "手紙が添えられている。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0334
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "いつもお地蔵様にお供えしてくれる\x01",
            "見知らぬ親切なお方、\x01",
            "本当にありがとうございます。\x01",
            "このような手紙で失礼いたしますが、\x01",
            "皆さまの行いによって\x01",
            "日々心洗われる想いをしている人間として\x01",
            "何か行動を起こさざるを得なかった、\x01",
            "というのが本音なのです。\x02",
        )
    )

    CloseMessageWindow()

    #A0335
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "お地蔵様の代わりといっては僭越ですが、\x01",
            "本日は感謝の品をご用意しました。\x01",
            "皆さまの為になれば……と願っております。\x01",
            "どうかお受け取りください。\x01\x01",
            "　　　　　～見知らぬ皆さまの隣人より\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0336
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0xAB),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    AddItemNumber(0xAB, 1)
    SetScenarioFlags(0x98, 7)
    Jump("loc_9999")

    label("loc_825F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x16), scpexpr(EXPR_GE), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x98, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8474")
    SetChrName("")

    #A0337
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(SCPSTR_CODE_ITEM, 0x1F4),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "と共に\x01",
            "手紙が添えられている。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0338
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "今日は本当に爽やかな朝で、\x01",
            "晴れやかな空の下、いつものように\x01",
            "お地蔵様に参ったところ\x01",
            "綺麗に供えられた料理を\x01",
            "拝見させていただきました。\x01",
            "いつも料理を供えてくださる方に\x01",
            "心嬉しく覚え、つい筆を取った次第です。\x01",
            "優しい方、いつも暖かい心を\x01",
            "ありがとうございます。\x02",
        )
    )

    CloseMessageWindow()

    #A0339
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "私にはこの程度しかできませんが\x01",
            "皆さまへの返礼になればと思います。\x01",
            "どうかこれをお受け取りください。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0340
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1F4),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    AddItemNumber(0x1F4, 1)
    SetScenarioFlags(0x98, 6)
    Jump("loc_9999")

    label("loc_8474")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_GE), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x98, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8686")
    SetChrName("")

    #A0341
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(SCPSTR_CODE_ITEM, 0x1F4),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "と共に\x01",
            "手紙が添えられている。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0342
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "たくさんの料理を供えてくださる方、\x01",
            "きっといつも同じ方なのだと思います。\x01",
            "ここを通りがかるたび、\x01",
            "優しいお心に触れたように感じ\x01",
            "爽やかな一日を過ごさせて貰っております。\x01",
            "昨今何かと騒動の多いクロスベルですが\x01",
            "皆さまのような方がいらっしゃれば\x01",
            "明るい社会になっていくかもしれませんね。\x02",
        )
    )

    CloseMessageWindow()

    #A0343
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "長々と、失礼いたしました。\x01",
            "粗品ですが、どうかこれを\x01",
            "お受け取りください。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0344
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1F4),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    AddItemNumber(0x1F4, 1)
    SetScenarioFlags(0x98, 5)
    Jump("loc_9999")

    label("loc_8686")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_GE), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x98, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8830")
    SetChrName("")

    #A0345
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(SCPSTR_CODE_ITEM, 0x1F4),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "と共に\x01",
            "手紙が添えられている。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0346
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "私は毎朝お地蔵様に\x01",
            "手を合わせている者です。\x01",
            "私以外にもこの地蔵様に\x01",
            "参ってくださる方がいると知り\x01",
            "とても嬉しく思います。\x02",
        )
    )

    CloseMessageWindow()

    #A0347
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "直接会う機会も無く、\x01",
            "どのような方なのか存じませんが、\x01",
            "いつもいらっしゃっているのでしょう。\x01",
            "どうかこの品をお受け取りください。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0348
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1F4),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    AddItemNumber(0x1F4, 1)
    SetScenarioFlags(0x98, 4)
    Jump("loc_9999")

    label("loc_8830")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x98, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8991")
    SetChrName("")

    #A0349
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(SCPSTR_CODE_ITEM, 0x1F4),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "と共に\x01",
            "手紙が添えられている。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0350
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "いつも料理を供えて下さる方、\x01",
            "ありがとうございます。\x01",
            "優しい方に参っていただき\x01",
            "お地蔵様も喜ばれている事と\x01",
            "思います。\x01",
            "わずかながら、お礼を用意しましたので\x01",
            "どうかお受け取りください。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0351
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1F4),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    AddItemNumber(0x1F4, 1)
    SetScenarioFlags(0x98, 3)
    Jump("loc_9999")

    label("loc_8991")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x98, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8AAC")
    SetChrName("")

    #A0352
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(SCPSTR_CODE_ITEM, 0x1F4),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "と共に\x01",
            "手紙が添えられている。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0353
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "どなたか存じませんが、\x01",
            "お供えをして頂いて\x01",
            "ありがとうございました。\x01",
            "どうかお礼に\x01",
            "この品をお受け取りください。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0354
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1F4),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    AddItemNumber(0x1F4, 1)
    SetScenarioFlags(0x98, 2)
    Jump("loc_9999")

    label("loc_8AAC")

    SetChrName("")

    #A0355
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "東方風の地蔵が奉られている。\x02\x03",

            "上手にできた料理を供えますか？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_8AFF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9999")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuCmd(0, 1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 0)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x190, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8B4A")
    MenuCmd(1, 1, "覇王麺")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 0)), scpexpr(EXPR_END)), "loc_8B40")
    Call(0, 13)

    label("loc_8B40")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8B4A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 1)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x193, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8B83")
    MenuCmd(1, 1, "薬膳麻婆≪黄龍≫")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 1)), scpexpr(EXPR_END)), "loc_8B79")
    Call(0, 13)

    label("loc_8B79")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8B83")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 2)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x196, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8BB4")
    MenuCmd(1, 1, "白虎炒飯")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 2)), scpexpr(EXPR_END)), "loc_8BAA")
    Call(0, 13)

    label("loc_8BAA")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8BB4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 3)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x199, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8BEF")
    MenuCmd(1, 1, "極上ステーキ≪雅≫")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 3)), scpexpr(EXPR_END)), "loc_8BE5")
    Call(0, 13)

    label("loc_8BE5")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8BEF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 4)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x19C, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8C2A")
    MenuCmd(1, 1, "極上シチュー≪薫≫")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 4)), scpexpr(EXPR_END)), "loc_8C20")
    Call(0, 13)

    label("loc_8C20")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8C2A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 5)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x19F, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8C61")
    MenuCmd(1, 1, "鉄人鍋≪絢爛≫")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 5)), scpexpr(EXPR_END)), "loc_8C57")
    Call(0, 13)

    label("loc_8C57")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8C61")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 6)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1A2, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8C98")
    MenuCmd(1, 1, "賢人鍋≪繚乱≫")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 6)), scpexpr(EXPR_END)), "loc_8C8E")
    Call(0, 13)

    label("loc_8C8E")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8C98")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 7)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1A5, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8CD1")
    MenuCmd(1, 1, "リザレクトフライ")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 7)), scpexpr(EXPR_END)), "loc_8CC7")
    Call(0, 13)

    label("loc_8CC7")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8CD1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 0)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1A8, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8D0A")
    MenuCmd(1, 1, "黄金卵飯≪輝き≫")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 0)), scpexpr(EXPR_END)), "loc_8D00")
    Call(0, 13)

    label("loc_8D00")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8D0A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 1)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1AB, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8D43")
    MenuCmd(1, 1, "黄金卵麺≪煌き≫")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 1)), scpexpr(EXPR_END)), "loc_8D39")
    Call(0, 13)

    label("loc_8D39")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8D43")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 2)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1AE, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8D7A")
    MenuCmd(1, 1, "キングバーガー")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 2)), scpexpr(EXPR_END)), "loc_8D70")
    Call(0, 13)

    label("loc_8D70")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8D7A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 3)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1B1, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8DAF")
    MenuCmd(1, 1, "クイーンピザ")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 3)), scpexpr(EXPR_END)), "loc_8DA5")
    Call(0, 13)

    label("loc_8DA5")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8DAF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 4)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1B4, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8DEA")
    MenuCmd(1, 1, "行楽サンド≪相棒≫")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 4)), scpexpr(EXPR_END)), "loc_8DE0")
    Call(0, 13)

    label("loc_8DE0")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8DEA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 5)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1B7, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8E25")
    MenuCmd(1, 1, "愛情凝縮箱≪お袋≫")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 5)), scpexpr(EXPR_END)), "loc_8E1B")
    Call(0, 13)

    label("loc_8E1B")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8E25")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 6)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1BA, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8E5E")
    MenuCmd(1, 1, "フルムーンスープ")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 6)), scpexpr(EXPR_END)), "loc_8E54")
    Call(0, 13)

    label("loc_8E54")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8E5E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 7)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1BD, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8E97")
    MenuCmd(1, 1, "クレセントスープ")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 7)), scpexpr(EXPR_END)), "loc_8E8D")
    Call(0, 13)

    label("loc_8E8D")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8E97")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 0)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1C0, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8ECE")
    MenuCmd(1, 1, "絶菓≪白無垢≫")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 0)), scpexpr(EXPR_END)), "loc_8EC4")
    Call(0, 13)

    label("loc_8EC4")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8ECE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 1)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1C3, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8F03")
    MenuCmd(1, 1, "絶菓≪黄熟≫")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 1)), scpexpr(EXPR_END)), "loc_8EF9")
    Call(0, 13)

    label("loc_8EF9")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8F03")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 2)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1C6, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8F38")
    MenuCmd(1, 1, "絶菓≪粉雪≫")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 2)), scpexpr(EXPR_END)), "loc_8F2E")
    Call(0, 13)

    label("loc_8F2E")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8F38")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 3)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1C9, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8F6D")
    MenuCmd(1, 1, "絶菓≪浮雲≫")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 3)), scpexpr(EXPR_END)), "loc_8F63")
    Call(0, 13)

    label("loc_8F63")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8F6D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 4)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1CC, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8FA6")
    MenuCmd(1, 1, "シュプリームラテ")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 4)), scpexpr(EXPR_END)), "loc_8F9C")
    Call(0, 13)

    label("loc_8F9C")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8FA6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 5)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1CF, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8FE1")
    MenuCmd(1, 1, "アルティマミックス")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 5)), scpexpr(EXPR_END)), "loc_8FD7")
    Call(0, 13)

    label("loc_8FD7")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8FE1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 6)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1D2, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_901A")
    MenuCmd(1, 1, "キル・ナイトメア")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 6)), scpexpr(EXPR_END)), "loc_9010")
    Call(0, 13)

    label("loc_9010")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_901A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 7)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1D5, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9051")
    MenuCmd(1, 1, "秘水≪月光蝶≫")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 7)), scpexpr(EXPR_END)), "loc_9047")
    Call(0, 13)

    label("loc_9047")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9051")

    MenuCmd(1, 1, "やめる")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuCmd(2, 1, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x1)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9092")
    Jump("loc_9994")

    label("loc_9092")

    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 0)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x190, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_90FD")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_90F3")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x190, 1)
    SetScenarioFlags(0x99, 0)

    #A0356
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x190),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を供えた。\x02",
        )
    )


    label("loc_90F3")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_90FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 1)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x193, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9149")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_913F")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x193, 1)
    SetScenarioFlags(0x99, 1)

    #A0357
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x193),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を供えた。\x02",
        )
    )


    label("loc_913F")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9149")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 2)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x196, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9195")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_918B")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x196, 1)
    SetScenarioFlags(0x99, 2)

    #A0358
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x196),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を供えた。\x02",
        )
    )


    label("loc_918B")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9195")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 3)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x199, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_91E1")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_91D7")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x199, 1)
    SetScenarioFlags(0x99, 3)

    #A0359
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x199),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を供えた。\x02",
        )
    )


    label("loc_91D7")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_91E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 4)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x19C, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_922D")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9223")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x19C, 1)
    SetScenarioFlags(0x99, 4)

    #A0360
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x19C),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を供えた。\x02",
        )
    )


    label("loc_9223")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_922D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 5)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x19F, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9279")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_926F")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x19F, 1)
    SetScenarioFlags(0x99, 5)

    #A0361
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x19F),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を供えた。\x02",
        )
    )


    label("loc_926F")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9279")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 6)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1A2, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_92C5")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_92BB")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x1A2, 1)
    SetScenarioFlags(0x99, 6)

    #A0362
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1A2),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を供えた。\x02",
        )
    )


    label("loc_92BB")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_92C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 7)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1A5, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9311")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9307")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x1A5, 1)
    SetScenarioFlags(0x99, 7)

    #A0363
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1A5),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を供えた。\x02",
        )
    )


    label("loc_9307")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9311")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 0)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1A8, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_935D")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9353")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x1A8, 1)
    SetScenarioFlags(0x9A, 0)

    #A0364
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1A8),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を供えた。\x02",
        )
    )


    label("loc_9353")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_935D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 1)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1AB, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_93A9")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_939F")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x1AB, 1)
    SetScenarioFlags(0x9A, 1)

    #A0365
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1AB),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を供えた。\x02",
        )
    )


    label("loc_939F")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_93A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 2)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1AE, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_93F5")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_93EB")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x1AE, 1)
    SetScenarioFlags(0x9A, 2)

    #A0366
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1AE),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を供えた。\x02",
        )
    )


    label("loc_93EB")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_93F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 3)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1B1, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9441")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9437")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x1B1, 1)
    SetScenarioFlags(0x9A, 3)

    #A0367
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1B1),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を供えた。\x02",
        )
    )


    label("loc_9437")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9441")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 4)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1B4, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_948D")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9483")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x1B4, 1)
    SetScenarioFlags(0x9A, 4)

    #A0368
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1B4),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を供えた。\x02",
        )
    )


    label("loc_9483")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_948D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 5)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1B7, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_94D9")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_94CF")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x1B7, 1)
    SetScenarioFlags(0x9A, 5)

    #A0369
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1B7),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を供えた。\x02",
        )
    )


    label("loc_94CF")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_94D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 6)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1BA, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9525")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_951B")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x1BA, 1)
    SetScenarioFlags(0x9A, 6)

    #A0370
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1BA),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を供えた。\x02",
        )
    )


    label("loc_951B")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9525")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 7)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1BD, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9571")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9567")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x1BD, 1)
    SetScenarioFlags(0x9A, 7)

    #A0371
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1BD),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を供えた。\x02",
        )
    )


    label("loc_9567")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9571")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 0)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1C0, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_95BD")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_95B3")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x1C0, 1)
    SetScenarioFlags(0x9B, 0)

    #A0372
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1C0),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を供えた。\x02",
        )
    )


    label("loc_95B3")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_95BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 1)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1C3, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9609")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_95FF")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x1C3, 1)
    SetScenarioFlags(0x9B, 1)

    #A0373
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1C3),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を供えた。\x02",
        )
    )


    label("loc_95FF")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9609")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 2)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1C6, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9655")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_964B")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x1C6, 1)
    SetScenarioFlags(0x9B, 2)

    #A0374
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1C6),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を供えた。\x02",
        )
    )


    label("loc_964B")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9655")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 3)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1C9, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_96A1")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9697")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x1C9, 1)
    SetScenarioFlags(0x9B, 3)

    #A0375
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1C9),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を供えた。\x02",
        )
    )


    label("loc_9697")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_96A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 4)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1CC, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_96ED")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_96E3")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x1CC, 1)
    SetScenarioFlags(0x9B, 4)

    #A0376
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1CC),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を供えた。\x02",
        )
    )


    label("loc_96E3")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_96ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 5)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1CF, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9739")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_972F")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x1CF, 1)
    SetScenarioFlags(0x9B, 5)

    #A0377
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1CF),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を供えた。\x02",
        )
    )


    label("loc_972F")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9739")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 6)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1D2, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9785")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_977B")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x1D2, 1)
    SetScenarioFlags(0x9B, 6)

    #A0378
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1D2),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を供えた。\x02",
        )
    )


    label("loc_977B")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9785")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 7)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1D5, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_97D1")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_97C7")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x1D5, 1)
    SetScenarioFlags(0x9B, 7)

    #A0379
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1D5),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を供えた。\x02",
        )
    )


    label("loc_97C7")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_97D1")

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9994")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x98, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9991")

    #C0380
    ChrTalk(
        0x101,
        (
            "#0000Fこれでよし、と。\x01",
            "……また持ってきてみようかな。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9899")

    #C0381
    ChrTalk(
        0x102,
        (
            "#0100Fあまり同じ料理ばかりだと\x01",
            "失礼でしょうし、\x01",
            "一品一回くらいが良さそうね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9970")

    label("loc_9899")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9908")

    #C0382
    ChrTalk(
        0x103,
        (
            "#0200Fあまり同じ料理ばかりだと\x01",
            "失礼かもしれません。\x01",
            "一品一回くらいが良さそうですね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9970")

    label("loc_9908")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9970")

    #C0383
    ChrTalk(
        0x104,
        (
            "#0300Fあまり同じ料理ばかりだと\x01",
            "失礼なんじゃねえか？\x01",
            "一品一回くらいが良さそうだぜ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9970")


    #C0384
    ChrTalk(
        0x101,
        "#0000Fああ、そうするか。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x98, 1)

    label("loc_9991")

    SetScenarioFlags(0x1, 7)

    label("loc_9994")

    Jump("loc_8AFF")

    label("loc_9999")

    TalkEnd(0xFF)
    Return()

    # Function_46_7D37 end

    def Function_47_999D(): pass

    label("Function_47_999D")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 0)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x190, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_99C0")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_99C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 1)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x193, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_99D9")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_99D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 2)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x196, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_99F2")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_99F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 3)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x199, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9A0B")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9A0B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 4)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x19C, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9A24")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9A24")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 5)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x19F, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9A3D")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9A3D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 6)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1A2, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9A56")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9A56")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 7)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1A5, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9A6F")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9A6F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 0)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1A8, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9A88")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9A88")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 1)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1AB, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9AA1")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9AA1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 2)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1AE, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9ABA")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9ABA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 3)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1B1, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9AD3")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9AD3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 4)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1B4, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9AEC")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9AEC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 5)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1B7, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9B05")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9B05")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 6)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1BA, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9B1E")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9B1E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 7)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1BD, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9B37")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9B37")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 0)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1C0, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9B50")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9B50")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 1)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1C3, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9B69")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9B69")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 2)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1C6, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9B82")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9B82")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 3)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1C9, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9B9B")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9B9B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 4)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1CC, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9BB4")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9BB4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 5)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1CF, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9BCD")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9BCD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 6)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1D2, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9BE6")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9BE6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 7)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1D5, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9BFF")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9BFF")

    Return()

    # Function_47_999D end

    def Function_48_9C00(): pass

    label("Function_48_9C00")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 0)), scpexpr(EXPR_END)), "loc_9C1D")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9C1D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 1)), scpexpr(EXPR_END)), "loc_9C30")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9C30")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 2)), scpexpr(EXPR_END)), "loc_9C43")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9C43")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 3)), scpexpr(EXPR_END)), "loc_9C56")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9C56")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 4)), scpexpr(EXPR_END)), "loc_9C69")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9C69")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 5)), scpexpr(EXPR_END)), "loc_9C7C")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9C7C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 6)), scpexpr(EXPR_END)), "loc_9C8F")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9C8F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 7)), scpexpr(EXPR_END)), "loc_9CA2")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9CA2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 0)), scpexpr(EXPR_END)), "loc_9CB5")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9CB5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 1)), scpexpr(EXPR_END)), "loc_9CC8")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9CC8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 2)), scpexpr(EXPR_END)), "loc_9CDB")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9CDB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 3)), scpexpr(EXPR_END)), "loc_9CEE")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9CEE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 4)), scpexpr(EXPR_END)), "loc_9D01")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9D01")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 5)), scpexpr(EXPR_END)), "loc_9D14")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9D14")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 6)), scpexpr(EXPR_END)), "loc_9D27")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9D27")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 7)), scpexpr(EXPR_END)), "loc_9D3A")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9D3A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 0)), scpexpr(EXPR_END)), "loc_9D4D")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9D4D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 1)), scpexpr(EXPR_END)), "loc_9D60")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9D60")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 2)), scpexpr(EXPR_END)), "loc_9D73")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9D73")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 3)), scpexpr(EXPR_END)), "loc_9D86")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9D86")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 4)), scpexpr(EXPR_END)), "loc_9D99")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9D99")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 5)), scpexpr(EXPR_END)), "loc_9DAC")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9DAC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 6)), scpexpr(EXPR_END)), "loc_9DBF")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9DBF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 7)), scpexpr(EXPR_END)), "loc_9DD2")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9DD2")

    Return()

    # Function_48_9C00 end

    SaveToFile()

Try(main)
