from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c1000.bin",                # FileName
        "c1000",                    # MapName
        "c1000",                    # Location
        0x0010,                     # MapIndex
        "ed7100",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x1E,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 16, 0, 8, 0, 9],
    )

    BuildStringList((
        "c1000",                  # 0
        "クロンク",               # 1
        "ディンズ",               # 2
        "リリィ",                 # 3
        "マルテ",                 # 4
        "アンネ",                 # 5
        "ルノー爺さん",           # 6
        "ロイ",                   # 7
        "ルース",                 # 8
        "メイリン",               # 9
        "スーザン",               # 10
        "ジレ",                   # 11
        "クータ",                 # 12
        "観光客",                 # 13
        "エステル",               # 14
        "ヨシュア",               # 15
        "シズク",                 # 16
        "列車",                   # 17
        "中央広場",               # 18
        "西通り",                 # 19
        "行政区",                 # 20
        "住宅街",                 # 21
        "歓楽街",                 # 22
        "東通り",                 # 23
        "旧市街",                 # 24
        "港湾区",                 # 25
        "ＩＢＣ",                 # 26
        "駅前通り",               # 27
        "裏通り",                 # 28
        "ウルスラ間道",           # 29
        "東クロスベル街道",       # 30
        "西クロスベル街道",       # 31
        "マインツ山道",           # 32
    ))

    AddCharChip((
        "chr/ch20400.itc",                   # 00
        "chr/ch24800.itc",                   # 01
        "chr/ch24900.itc",                   # 02
        "chr/ch23500.itc",                   # 03
        "chr/ch21100.itc",                   # 04
        "chr/ch24000.itc",                   # 05
        "chr/ch21200.itc",                   # 06
        "chr/ch21500.itc",                   # 07
        "chr/ch10300.itc",                   # 08
        "chr/ch26200.itc",                   # 09
        "chr/ch21400.itc",                   # 0A
        "chr/ch00600.itc",                   # 0B
        "chr/ch00700.itc",                   # 0C
        "chr/ch08700.itc",                   # 0D
        "chr/ch22800.itc",                   # 0E
    ))

    DeclNpc(-24409,  -3000,   5239,    180,  261,  0x0, 0,   14,  0,   0,   0,   0,   10,  255,  0)
    DeclNpc(-13039,  -3000,   -810,    225,  261,  0x0, 0,   1,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(-16500,  -3000,   2920,    45,   261,  0x0, 0,   2,   0,   0,   6,   0,   12,  255,  0)
    DeclNpc(-4559,   -3000,   -8949,   180,  261,  0x0, 0,   3,   0,   0,   0,   0,   13,  255,  0)
    DeclNpc(26200,   -300,    -1049,   270,  261,  0x0, 0,   4,   0,   0,   1,   0,   17,  255,  0)
    DeclNpc(-40490,  -300,    15850,   90,   261,  0x0, 0,   5,   0,   0,   5,   0,   18,  255,  0)
    DeclNpc(-18200,  -300,    18139,   270,  261,  0x0, 0,   6,   0,   0,   0,   0,   19,  255,  0)
    DeclNpc(5300,    -3000,   -13220,  270,  389,  0x0, 0,   6,   0,   0,   0,   0,   25,  255,  0)
    DeclNpc(-22280,  -300,    18370,   225,  261,  0x0, 0,   7,   0,   0,   2,   0,   20,  255,  0)
    DeclNpc(-8470,   -3000,   -7349,   45,   261,  0x0, 0,   8,   0,   0,   0,   0,   21,  255,  0)
    DeclNpc(-8470,   -3000,   -7349,   45,   389,  0x0, 0,   9,   0,   0,   0,   0,   22,  255,  0)
    DeclNpc(-15939,  -3000,   -600,    45,   261,  0x0, 0,   10,  0,   0,   3,   0,   23,  255,  0)
    DeclNpc(-4190,   -300,    -1210,   225,  389,  0x0, 0,   0,   0,   0,   0,   0,   24,  255,  0)
    DeclNpc(-23690,  -3000,   3190,    270,  405,  0x0, 0,   11,  0,   0,   0,   0,   27,  255,  0)
    DeclNpc(-25129,  -3000,   3630,    90,   405,  0x0, 0,   12,  0,   0,   0,   0,   27,  255,  0)
    DeclNpc(-23530,  -3000,   4090,    270,  405,  0x0, 0,   13,  0,   0,   0,   0,   27,  255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 36,  -7.920000076293945,    13.430000305175781,    -0.5,                  4.0,                   [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   3.9600000381469727,    -6.715000152587891,    0.10000000149011612,   1.0])
    DeclEvent(0x0000, 0, 37,  -7.789999961853027,    -7.980000019073486,    -3.0,                  25.0,                  [0.35355326533317566,  0.1414213925600052,    -0.0,                  0.0,                   -0.35355350375175476,  0.14142130315303802,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.19999998807907104,   0.0,                   -0.06717704236507416,  2.2302145957946777,    0.5999999642372131,    1.0])
    DeclEvent(0x0000, 0, 38,  2.200000047683716,     -2.2300000190734863,   -0.30000001192092896,  25.0,                  [0.19999998807907104,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.19999998807907104,   0.0,                   -0.4399999976158142,   1.1150000095367432,    0.05999999865889549,   1.0])

    DeclActor(17360,   -300,    4630,    1200,    17530,   1500,    5120,    0x007C, 0,  39, 0x0000)

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
    PlaceName(-98.33000183105469, 0.0, 1.440000057220459, 0x0000, 0x0056, "")

    ScpFunction((
        "Function_0_6F0",          # 00, 0
        "Function_1_7A8",          # 01, 1
        "Function_2_841",          # 02, 2
        "Function_3_86C",          # 03, 3
        "Function_4_8E1",          # 04, 4
        "Function_5_92E",          # 05, 5
        "Function_6_9EF",          # 06, 6
        "Function_7_A3C",          # 07, 7
        "Function_8_AAC",          # 08, 8
        "Function_9_F19",          # 09, 9
        "Function_10_10A5",        # 0A, 10
        "Function_11_211F",        # 0B, 11
        "Function_12_3374",        # 0C, 12
        "Function_13_4451",        # 0D, 13
        "Function_14_6123",        # 0E, 14
        "Function_15_7232",        # 0F, 15
        "Function_16_7375",        # 10, 16
        "Function_17_753E",        # 11, 17
        "Function_18_827F",        # 12, 18
        "Function_19_9436",        # 13, 19
        "Function_20_A1C1",        # 14, 20
        "Function_21_A9AC",        # 15, 21
        "Function_22_B401",        # 16, 22
        "Function_23_B4B3",        # 17, 23
        "Function_24_C0C8",        # 18, 24
        "Function_25_C235",        # 19, 25
        "Function_26_C32C",        # 1A, 26
        "Function_27_C416",        # 1B, 27
        "Function_28_C505",        # 1C, 28
        "Function_29_C88A",        # 1D, 29
        "Function_30_CD5F",        # 1E, 30
        "Function_31_CF74",        # 1F, 31
        "Function_32_DD7E",        # 20, 32
        "Function_33_DDDB",        # 21, 33
        "Function_34_E5F6",        # 22, 34
        "Function_35_EA8F",        # 23, 35
        "Function_36_EE02",        # 24, 36
        "Function_37_F096",        # 25, 37
        "Function_38_F180",        # 26, 38
        "Function_39_F26A",        # 27, 39
        "Function_40_1118C",       # 28, 40
        "Function_41_113EF",       # 29, 41
    ))


    def Function_0_6F0(): pass

    label("Function_0_6F0")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_730"),
        (1, "loc_73C"),
        (2, "loc_748"),
        (3, "loc_754"),
        (4, "loc_760"),
        (5, "loc_76C"),
        (6, "loc_778"),
        (SWITCH_DEFAULT, "loc_784"),
    )


    label("loc_730")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_790")

    label("loc_73C")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_790")

    label("loc_748")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_790")

    label("loc_754")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_790")

    label("loc_760")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_790")

    label("loc_76C")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_790")

    label("loc_778")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_790")

    label("loc_784")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_790")

    label("loc_790")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7A7")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_790")

    label("loc_7A7")

    Return()

    # Function_0_6F0 end

    def Function_1_7A8(): pass

    label("Function_1_7A8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_840")
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
    Jump("Function_1_7A8")

    label("loc_840")

    Return()

    # Function_1_7A8 end

    def Function_2_841(): pass

    label("Function_2_841")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_86B")
    OP_94(0xFE, 0xFFFFB000, 0x4ECA, 0xFFFFA8EE, 0x3F01, 0x3E8)
    Sleep(300)
    Jump("Function_2_841")

    label("loc_86B")

    Return()

    # Function_2_841 end

    def Function_3_86C(): pass

    label("Function_3_86C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_8E0")
    OP_95(0xFE, -19740, -3000, 3190, 1000, 0x0)
    OP_95(0xFE, -22610, -3000, 3390, 1000, 0x0)
    OP_93(0xFE, 0x0, 0x12C)
    Sleep(1500)
    OP_95(0xFE, -19740, -3000, 3190, 1000, 0x0)
    OP_95(0xFE, -15940, -3000, -600, 1000, 0x0)
    OP_93(0xFE, 0x2D, 0x12C)
    Sleep(1500)
    Jump("Function_3_86C")

    label("loc_8E0")

    Return()

    # Function_3_86C end

    def Function_4_8E1(): pass

    label("Function_4_8E1")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_92D")
    OP_95(0xFE, -15940, -3000, -600, 1000, 0x0)
    OP_93(0xFE, 0x2D, 0x12C)
    Sleep(1500)
    OP_95(0xFE, -9950, -3000, -6670, 1000, 0x0)
    OP_93(0xFE, 0x2D, 0x12C)
    Sleep(1500)
    Jump("Function_4_8E1")

    label("loc_92D")

    Return()

    # Function_4_8E1 end

    def Function_5_92E(): pass

    label("Function_5_92E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_9EE")
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
    Jump("Function_5_92E")

    label("loc_9EE")

    Return()

    # Function_5_92E end

    def Function_6_9EF(): pass

    label("Function_6_9EF")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A3B")
    OP_95(0xFE, -15130, -3000, 1420, 1000, 0x0)
    OP_93(0xFE, 0x2D, 0x12C)
    Sleep(3000)
    OP_95(0xFE, -16500, -3000, 2920, 1000, 0x0)
    OP_93(0xFE, 0x2D, 0x12C)
    Sleep(3000)
    Jump("Function_6_9EF")

    label("loc_A3B")

    Return()

    # Function_6_9EF end

    def Function_7_A3C(): pass

    label("Function_7_A3C")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AAB")
    SetChrPos(0x18, 70000, -27500, -17600, 0)
    ClearChrFlags(0x18, 0x80)
    OP_78(0x0, 0x18)
    OP_49()
    OP_D3(0x18, 0x0, 0x41EB0, 0x0, 0x0)
    ClearMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x0, 0x1000)
    OP_9B(0x0, 0x18, 0x10E, 0x30D40, 0x4E20, 0x0)
    SetChrFlags(0x18, 0x80)
    SetMapObjFlags(0x0, 0x4)

    label("loc_AAB")

    Return()

    # Function_7_A3C end

    def Function_8_AAC(): pass

    label("Function_8_AAC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6E), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CCC")
    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_B77")
    SetChrPos(0x0, -20760, -310, 33300, 180)
    SetChrPos(0x1, -20760, -310, 33300, 180)
    SetChrPos(0x2, -20760, -310, 33300, 180)
    SetChrPos(0x3, -20760, -310, 33300, 180)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B4A")
    SetChrPos(0x4, -20760, -310, 33300, 180)
    SetChrPos(0x5, -20760, -310, 33300, 180)
    Jump("loc_B69")

    label("loc_B4A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B69")
    SetChrPos(0x4, -20760, -310, 33300, 180)

    label("loc_B69")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_CCC")

    label("loc_B77")

    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C2B")
    SetChrPos(0x0, 1910, -3000, -35980, 0)
    SetChrPos(0x1, 1910, -3000, -35980, 0)
    SetChrPos(0x2, 1910, -3000, -35980, 0)
    SetChrPos(0x3, 1910, -3000, -35980, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BFE")
    SetChrPos(0x4, 1910, -3000, -35980, 0)
    SetChrPos(0x5, 1910, -3000, -35980, 0)
    Jump("loc_C1D")

    label("loc_BFE")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C1D")
    SetChrPos(0x4, 1910, -3000, -35980, 0)

    label("loc_C1D")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_CCC")

    label("loc_C2B")

    SetChrPos(0x0, -29790, -330, 13830, 90)
    SetChrPos(0x1, -29790, -330, 13830, 90)
    SetChrPos(0x2, -29790, -330, 13830, 90)
    SetChrPos(0x3, -29790, -330, 13830, 90)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CA4")
    SetChrPos(0x4, -29790, -330, 13830, 90)
    SetChrPos(0x5, -29790, -330, 13830, 90)
    Jump("loc_CC3")

    label("loc_CA4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CC3")
    SetChrPos(0x4, -29790, -330, 13830, 90)

    label("loc_CC3")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_CCC")

    OP_D0(0x7, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xD, 0x0, 0x10)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CEE")
    SetMapFlags(0x10000000)
    Event(0, 33)

    label("loc_CEE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_D05")
    ClearScenarioFlags(0x5C, 0)
    SetScenarioFlags(0x2, 4)
    Event(0, 30)
    Jump("loc_D14")

    label("loc_D05")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 1)), scpexpr(EXPR_END)), "loc_D14")
    ClearScenarioFlags(0x5C, 1)
    Event(0, 31)

    label("loc_D14")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_D6D")
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0xE, -18200, -300, 18140, 0)
    SetChrPos(0x10, -18360, -310, 19590, 180)
    BeginChrThread(0x10, 0, 0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xEE, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D68")
    SetChrFlags(0xE, 0x10)
    SetChrFlags(0x10, 0x10)

    label("loc_D68")

    Jump("loc_F01")

    label("loc_D6D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_D90")
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    BeginChrThread(0x13, 0, 0, 4)
    Jump("loc_F01")

    label("loc_D90")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_D9E")
    Jump("loc_F01")

    label("loc_D9E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_DAC")
    Jump("loc_F01")

    label("loc_DAC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_DDB")
    SetChrFlags(0x13, 0x80)
    SetChrPos(0x10, -18360, -310, 19590, 180)
    BeginChrThread(0x10, 0, 0, 0)
    SetChrFlags(0x10, 0x10)
    Jump("loc_F01")

    label("loc_DDB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_DE9")
    Jump("loc_F01")

    label("loc_DE9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_DF7")
    Jump("loc_F01")

    label("loc_DF7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_E32")
    SetChrPos(0xE, -18820, -320, 21060, 0)
    SetChrPos(0x10, -18680, -310, 19940, 0)
    BeginChrThread(0x10, 0, 0, 0)
    SetChrFlags(0x10, 0x10)
    Jump("loc_F01")

    label("loc_E32")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_E6D")
    SetChrPos(0xE, -18200, -300, 18140, 135)
    SetChrPos(0x10, -18690, -320, 19040, 180)
    BeginChrThread(0x10, 0, 0, 0)
    SetChrFlags(0x10, 0x10)
    Jump("loc_F01")

    label("loc_E6D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_E7B")
    Jump("loc_F01")

    label("loc_E7B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_E89")
    Jump("loc_F01")

    label("loc_E89")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_E97")
    Jump("loc_F01")

    label("loc_E97")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_EA5")
    Jump("loc_F01")

    label("loc_EA5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_EB3")
    Jump("loc_F01")

    label("loc_EB3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_EC6")
    ClearChrFlags(0x14, 0x80)
    Jump("loc_F01")

    label("loc_EC6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_F01")
    SetChrPos(0xE, -18200, -300, 18140, 0)
    SetChrPos(0x10, -18360, -310, 19590, 180)
    BeginChrThread(0x10, 0, 0, 0)
    SetChrFlags(0x10, 0x10)
    ClearChrFlags(0x14, 0x80)

    label("loc_F01")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x44, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F18")
    SetMapFlags(0x10000000)
    Event(0, 29)

    label("loc_F18")

    Return()

    # Function_8_AAC end

    def Function_9_F19(): pass

    label("Function_9_F19")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 4)), scpexpr(EXPR_END)), "loc_F2B")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_F2B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F6C")
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    SetMapObjFrame(0xFF, "sky", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sd_mul", 0x0, 0x1)
    Jump("loc_FCD")

    label("loc_F6C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_FA8")
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    SetMapObjFrame(0xFF, "sky", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sd_mul", 0x0, 0x1)
    Jump("loc_FCD")

    label("loc_FA8")

    SetMapObjFrame(0xFF, "sky", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sd_mul", 0x1, 0x1)

    label("loc_FCD")

    ClearMapObjFlags(0x6, 0x10)
    OP_70(0x6, 0x1E)
    OP_1B(0x8, 0xFF, 0xFFFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_FEF")
    OP_1B(0x8, 0x0, 0x23)

    label("loc_FEF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1002")
    OP_1B(0x8, 0x0, 0x23)

    label("loc_1002")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1015")
    OP_1B(0x8, 0x0, 0x23)

    label("loc_1015")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1028")
    OP_1B(0x8, 0x0, 0x23)

    label("loc_1028")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_103B")
    OP_1B(0x8, 0x0, 0x23)

    label("loc_103B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_1049")
    OP_1B(0x8, 0x0, 0x23)

    label("loc_1049")

    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1061")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_1061")

    ModifyEventFlags(0, 1, 0x80)
    ModifyEventFlags(0, 2, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1083")
    ModifyEventFlags(1, 1, 0x80)
    ModifyEventFlags(1, 2, 0x80)

    label("loc_1083")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_23, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_109F")
    Jump("loc_10A4")

    label("loc_109F")

    OP_16(0x3, 0x1D, 0x1, 0x0)

    label("loc_10A4")

    Return()

    # Function_9_F19 end

    def Function_10_10A5(): pass

    label("Function_10_10A5")

    TalkBegin(0xFE)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_10B2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_211B")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1110")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_1110")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1130")
    OP_AF(0x39)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2116")

    label("loc_1130")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1144")
    Jump("loc_2116")

    label("loc_1144")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2116")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2, 0x1, 0x0)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2, 0x1, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1342")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12C8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11EA")

    #C0001
    ChrTalk(
        0x101,
        (
            "#0003F（東通りの市場……\x01",
            "  落し物をしたトロントさんが\x01",
            "  立ち寄っていた場所だな。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 1)

    label("loc_11EA")


    #C0002
    ChrTalk(
        0x101,
        (
            "#0000Fすみません、この辺りで\x01",
            "落し物を見かけませんでしたか？\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0xFE,
        "落し物ッスか……？\x02",
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0xFE,
        "いんや、見てないッスね。\x02",
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0xFE,
        (
            "店の前は毎日掃除するッスから\x01",
            "間違いないッスよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x102,
        "#0106F（このお店は空振りみたいね。）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_133D")

    label("loc_12C8")


    #C0007
    ChrTalk(
        0xFE,
        (
            "落し物……自分は\x01",
            "心当たりがないッスね。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0xFE,
        (
            "他の露店の人にも\x01",
            "聞いてみたらどうッスか？\x01",
            "みんないい人たちッスよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_133D")

    Jump("loc_2116")

    label("loc_1342")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_1403")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13B4")

    #C0009
    ChrTalk(
        0xFE,
        (
            "さっき遊撃士さんたちが\x01",
            "一斉に出ていったッスよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0xFE,
        "どこかにお出掛けッスかねえ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_13FE")

    label("loc_13B4")


    #C0011
    ChrTalk(
        0xFE,
        (
            "みんな方角が\x01",
            "バラバラだったッスけど……\x01",
            "どこかにお出掛けッスかねえ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13FE")

    Jump("loc_2116")

    label("loc_1403")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_149F")

    #C0012
    ChrTalk(
        0xFE,
        (
            "ヘイ、いらっしゃいッスぅ！\x01",
            "工芸屋クロンクの新作ッスよ！\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0xFE,
        (
            "お手製のストラップで\x01",
            "土産にも最適ッスよ！\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0xFE,
        "ぜひ見ていってくださいッス！\x02",
    )

    CloseMessageWindow()
    Jump("loc_2116")

    label("loc_149F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_1592")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1529")

    #C0015
    ChrTalk(
        0xFE,
        (
            "昨晩、港湾公園の方で\x01",
            "撃ち合いがあったそうッスね。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0xFE,
        (
            "やっぱり……\x01",
            "クロスベルはどことなく\x01",
            "怖い街ッスよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_158D")

    label("loc_1529")


    #C0017
    ChrTalk(
        0xFE,
        (
            "この辺りはギルドが近いんで\x01",
            "平気ッスけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0xFE,
        (
            "やっぱりクロスベルは\x01",
            "どことなく怖い街ッスよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_158D")

    Jump("loc_2116")

    label("loc_1592")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_16A8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1662")

    #C0019
    ChrTalk(
        0xFE,
        (
            "先週、黒い服の人たちが\x01",
            "この辺りを占領してったッス。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0xFE,
        (
            "みかじめ料を払えとか\x01",
            "散々脅されたッスよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0xFE,
        (
            "あれがクロスベルのマフィアっスか。\x01",
            "……噂は聞いてたけど、恐ろしいッス。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_16A3")

    label("loc_1662")


    #C0022
    ChrTalk(
        0xFE,
        (
            "クロスベルのマフィア……\x01",
            "噂は聞いてたけど、恐ろしいッスよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16A3")

    Jump("loc_2116")

    label("loc_16A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_17E8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1787")

    #C0023
    ChrTalk(
        0xFE,
        (
            "記念祭では沢山売れたんで、\x01",
            "工芸品の種類を増やしてみたんスよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0xFE,
        (
            "お陰で工作中の怪我も\x01",
            "増えてしまったッスけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0xFE,
        (
            "ふふ、心配は無用ッス。\x01",
            "クロスベルには\x01",
            "立派な病院があるッスからねェ～。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_17E3")

    label("loc_1787")


    #C0026
    ChrTalk(
        0xFE,
        (
            "午後からは\x01",
            "ウルスラ病院に行くッスよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0xFE,
        (
            "病院があると\x01",
            "安心して怪我できるッスねェ～。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17E3")

    Jump("loc_2116")

    label("loc_17E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_18ED")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18AF")

    #C0028
    ChrTalk(
        0xFE,
        (
            "工芸品を作る楽しみ……\x01",
            "それはお客さんの反応ッスね。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0xFE,
        (
            "精工な細工物をみて\x01",
            "ビックリしてもらえると\x01",
            "最高に嬉しいんスよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0xFE,
        (
            "ふふ、数々の怪我も\x01",
            "報われるってものッス。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_18E8")

    label("loc_18AF")


    #C0031
    ChrTalk(
        0xFE,
        (
            "自治州７０周年の記念品も\x01",
            "いい物を作りたいッスね～。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18E8")

    Jump("loc_2116")

    label("loc_18ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_1952")

    #C0032
    ChrTalk(
        0xFE,
        (
            "いらっしゃいッス！\x01",
            "今日は新作が入ってるッスよ！\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0xFE,
        "ぜひ眺めていって下さいッス！\x02",
    )

    CloseMessageWindow()
    Jump("loc_2116")

    label("loc_1952")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_1A46")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19F4")

    #C0034
    ChrTalk(
        0xFE,
        "らっしゃいッス～！\x02",
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0xFE,
        (
            "……工作機械を使っていたら\x01",
            "手の甲をズバッとやってしまったッスよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0xFE,
        "考え事をしてるといけないッスねー。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_1A41")

    label("loc_19F4")


    #C0037
    ChrTalk(
        0xFE,
        "やれやれ、また怪我が増えたッス。\x02",
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0xFE,
        (
            "早く治ってくれると\x01",
            "いいんスけど。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A41")

    Jump("loc_2116")

    label("loc_1A46")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_1B1A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1AD8")

    #C0039
    ChrTalk(
        0xFE,
        "ヘイ、らっしゃいッス！\x02",
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0xFE,
        "来月は創立記念祭ッスねえ。\x02",
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0xFE,
        (
            "今年は７０周年ッスし、\x01",
            "何か記念品を作りたい所ッスよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_1B15")

    label("loc_1AD8")


    #C0042
    ChrTalk(
        0xFE,
        (
            "今のうちに記念祭の準備を\x01",
            "考えておかなきゃいけないッス。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B15")

    Jump("loc_2116")

    label("loc_1B1A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_1C18")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1BB1")

    #C0043
    ChrTalk(
        0xFE,
        "さっき木箱を運んでいたら……\x02",
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0xFE,
        (
            "そこの階段で\x01",
            "足をぶつけてしまったッス。\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0xFE,
        (
            "ふ……これしき。\x01",
            "負けてられないッスよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_1C13")

    label("loc_1BB1")


    #C0046
    ChrTalk(
        0xFE,
        (
            "ふ……工芸屋は\x01",
            "常に怪我と隣り合わせの職業ッス。\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0xFE,
        (
            "これしきの痛みに\x01",
            "負けてられないッスよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C13")

    Jump("loc_2116")

    label("loc_1C18")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_1CAA")

    #C0048
    ChrTalk(
        0xFE,
        (
            "最近売り上げが\x01",
            "伸びてきてるんスよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0xFE,
        "ふ……嬉しい話ッスねえ。\x02",
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0xFE,
        (
            "両手に傷をこさえながら\x01",
            "作ってきたかいがあったッスよ～。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2116")

    label("loc_1CAA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_1E05")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1DA7")

    #C0051
    ChrTalk(
        0xFE,
        (
            "いてて……\x01",
            "また指先を怪我してしまったッス。\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0xFE,
        (
            "工芸品を作ってると\x01",
            "怪我が絶えないんスよねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0xFE,
        "………………………………\x02",
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0xFE,
        (
            "け、決して自分が\x01",
            "不器用なわけではないッスよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0xFE,
        (
            "ベテランでも\x01",
            "怪我してしまうものなんス。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_1E00")

    label("loc_1DA7")


    #C0056
    ChrTalk(
        0xFE,
        "ヘイ、らっしゃいッス～！\x02",
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0xFE,
        (
            "怪我なんていつものことッス。\x01",
            "気にしてられないッスよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E00")

    Jump("loc_2116")

    label("loc_1E05")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_1F24")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1EA1")

    #C0058
    ChrTalk(
        0xFE,
        (
            "旧市街の不良たちには\x01",
            "よく絡まれたりするんスよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0xFE,
        (
            "うちは物珍しい品を\x01",
            "置いてるっスからねー……\x01",
            "うー、腹の立つ話ッスよ……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_1F1F")

    label("loc_1EA1")


    #C0060
    ChrTalk(
        0xFE,
        (
            "旧市街の不良たちは\x01",
            "時々やってきて絡んでいくんスよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0xFE,
        (
            "そんな時は売り上げが落ち込むッス。\x01",
            "まったく腹の立つ話ッスよ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F1F")

    Jump("loc_2116")

    label("loc_1F24")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_2116")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_20A8")

    #C0062
    ChrTalk(
        0xFE,
        "ヘイ、らっしゃいッス！\x02",
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0xFE,
        (
            "うちは手作りの\x01",
            "工芸品を扱ってるッスよ！\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x101,
        "#0005Fへえ、こんな店もあるのか……\x02",
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x103,
        (
            "#0200Fあの、このくるくる\x01",
            "回っている物は……？\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0xFE,
        (
            "ふっふ、よくぞ\x01",
            "聞いてくれたッスね。\x01",
            "これは『風車』という物ッスよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0xFE,
        (
            "東方では魔除けのほか\x01",
            "運気をよぶとも言われてるんス。\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0xFE,
        (
            "どうスか、お一つ。\x01",
            "幸運を呼び込んでくれるかも\x01",
            "しれないッスよ！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_2116")

    label("loc_20A8")


    #C0069
    ChrTalk(
        0xFE,
        (
            "うちは風車の他にも\x01",
            "細工物や工芸品を扱ってるッス。\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0xFE,
        (
            "すべて手作りっスよ。\x01",
            "ぜひ見ていってくださいッス！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2116")

    Jump("loc_10B2")

    label("loc_211B")

    TalkEnd(0xFE)
    Return()

    # Function_10_10A5 end

    def Function_11_211F(): pass

    label("Function_11_211F")

    TalkBegin(0xFE)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_212C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3370")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_218A")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_218A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_21AA")
    OP_AF(0x38)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_336B")

    label("loc_21AA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_21BE")
    Jump("loc_336B")

    label("loc_21BE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_336B")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2, 0x1, 0x0)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2, 0x1, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2441")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_23E7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2264")

    #C0071
    ChrTalk(
        0x101,
        (
            "#0003F（東通りの市場……\x01",
            "  落し物をしたトロントさんが\x01",
            "  立ち寄っていた場所だな。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 1)

    label("loc_2264")


    #C0072
    ChrTalk(
        0x101,
        (
            "#0000Fすみません、この辺りで\x01",
            "落し物を見かけませんでしたか？\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0xFE,
        (
            "へい、らっしゃいらっしゃ～い！\x01",
            "……ってなんだい、落し物！？\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0xFE,
        "ちょいと見てないねぇ。\x02",
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0xFE,
        (
            "うちは朝が早いから\x01",
            "そんな物があれば気付く筈なんだが。\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0xFE,
        (
            "もし大事なものなら\x01",
            "一応警察に届けてみちゃあどうだい？\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0x101,
        "#0006F（いや、警察なんですけど……）\x02",
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0x103,
        (
            "#0203F（さすがクロスベル警察、\x01",
            "  認知度が低いですね。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_243C")

    label("loc_23E7")


    #C0079
    ChrTalk(
        0xFE,
        (
            "落し物か……\x01",
            "うちの辺りじゃ見てないねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0xFE,
        "悪いな、力にはなれそうにねえや。\x02",
    )

    CloseMessageWindow()

    label("loc_243C")

    Jump("loc_336B")

    label("loc_2441")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_24BE")

    #C0081
    ChrTalk(
        0xFE,
        (
            "おっとお客さん、\x01",
            "もたもたしてると\x01",
            "日が暮れちまうぜ！\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0xFE,
        (
            "さあ買った買ったぁ！\x01",
            "本日ラストの叩き売りだぁ！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_336B")

    label("loc_24BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_260C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_259F")

    #C0083
    ChrTalk(
        0xFE,
        (
            "商工会のじーさまたちの事は\x01",
            "俺も心底尊敬してるぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0xFE,
        (
            "なんてったって\x01",
            "露店街の伝統を\x01",
            "守ってきた人たちだからな。\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0xFE,
        (
            "だが……オレには\x01",
            "難しい事はわからねえ！\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0xFE,
        "役員なんて柄じゃないって事よ！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_2607")

    label("loc_259F")


    #C0087
    ChrTalk(
        0xFE,
        (
            "へいらっしゃい！\x01",
            "見ていってくんな～っ！\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0xFE,
        (
            "……やっぱオレはこうして\x01",
            "商売してる方が向いてるぜい。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2607")

    Jump("loc_336B")

    label("loc_260C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_2699")

    #C0089
    ChrTalk(
        0xFE,
        (
            "へいらしゃ～い！\x01",
            "毎度フレッシュ・ディンズだよ！\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0xFE,
        (
            "今日も朝から大放出、\x01",
            "大特価でご奉仕中だぜい！\x01",
            "見ていってくれよなっ！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_336B")

    label("loc_2699")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_2758")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2722")

    #C0091
    ChrTalk(
        0xFE,
        (
            "くそっ、あの連中\x01",
            "乱暴をしやがって……！\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0xFE,
        (
            "俺を殴るだけならともかく、\x01",
            "客に迷惑掛けるなんて許せないぜ！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_2753")

    label("loc_2722")


    #C0093
    ChrTalk(
        0xFE,
        (
            "ルバーチェの連中め……\x01",
            "くそっ、許せないぜ！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2753")

    Jump("loc_336B")

    label("loc_2758")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_28A4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_283E")

    #C0094
    ChrTalk(
        0xFE,
        (
            "最近商工会のじーさまたちに\x01",
            "呼ばれることが多いんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0xFE,
        (
            "なんだか気に\x01",
            "入られちまったみたいでな。\x01",
            "食事に誘われたりすんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0xFE,
        (
            "へへっ、みんな\x01",
            "生え抜きの商人ばっかだ。\x01",
            "昔話を聞くだけでも面白いぜ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_289F")

    label("loc_283E")


    #C0097
    ChrTalk(
        0xFE,
        (
            "最近商工会のじーさまたちと\x01",
            "食事に行ったりするんだよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0xFE,
        "みんな親切でいい人たちだぜい。\x02",
    )

    CloseMessageWindow()

    label("loc_289F")

    Jump("loc_336B")

    label("loc_28A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_29E8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2975")

    #C0099
    ChrTalk(
        0xFE,
        (
            "商工会の会長さんに\x01",
            "いつも誠実な商売だって\x01",
            "褒めてもらったんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0xFE,
        (
            "へっへー、嬉しいねぇ。\x01",
            "オレの商売が認められるなんてさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0xFE,
        (
            "おまけに今度飲まないかって\x01",
            "誘われちまったよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_29E3")

    label("loc_2975")


    #C0102
    ChrTalk(
        0xFE,
        (
            "商工会の会長さんに\x01",
            "商売を褒めてもらったんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0xFE,
        (
            "へっへー、露天売りとして\x01",
            "これ以上嬉しいことはねえよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_29E3")

    Jump("loc_336B")

    label("loc_29E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_2B2D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2AD1")

    #C0104
    ChrTalk(
        0xFE,
        (
            "記念祭の間の仕入れは\x01",
            "毎年予想するのが難しいんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0xFE,
        (
            "なんと言っても\x01",
            "野菜は鮮度が命だからな。\x01",
            "仕入れすぎはご法度なんだぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0xFE,
        (
            "だが売り切れちまっても\x01",
            "お客に迷惑がかかる……\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0xFE,
        "悩みどころだなぁ……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_2B28")

    label("loc_2AD1")


    #C0108
    ChrTalk(
        0xFE,
        (
            "記念祭の間の仕入れは\x01",
            "毎年予想するのが難しいんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0xFE,
        "やれやれ、悩みどころだな。\x02",
    )

    CloseMessageWindow()

    label("loc_2B28")

    Jump("loc_336B")

    label("loc_2B2D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_2BAE")

    #C0110
    ChrTalk(
        0xFE,
        "らっしゃい、らっしゃ～い！\x02",
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0xFE,
        (
            "うちはお得意さんには\x01",
            "おまけを付けてるよっ！\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0xFE,
        "ガツーンと買っていってくれ！\x02",
    )

    CloseMessageWindow()
    Jump("loc_336B")

    label("loc_2BAE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_2D02")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C9B")

    #C0113
    ChrTalk(
        0xFE,
        (
            "アルモリカ村からの仕入れは\x01",
            "導力トラックで\x01",
            "届けてもらってるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0xFE,
        (
            "商売を始めた頃は\x01",
            "まだまだそんなモンは\x01",
            "なかったみたいだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0xFE,
        (
            "お陰で新鮮野菜が\x01",
            "早く届くようになった！\x01",
            "世の中便利になったもんだな！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_2CFD")

    label("loc_2C9B")


    #C0116
    ChrTalk(
        0xFE,
        (
            "最近はどこの店も\x01",
            "導力トラックを使ってるらしいぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0xFE,
        (
            "いやあ、世の中\x01",
            "便利になったもんだな！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2CFD")

    Jump("loc_336B")

    label("loc_2D02")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_2E22")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2DC2")

    #C0118
    ChrTalk(
        0xFE,
        (
            "朝の市で商工会の\x01",
            "会長さんに挨拶されちまったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0xFE,
        (
            "やれやれ、照れちまうなぁ。\x01",
            "会長に顔を覚えられてるなんてさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0xFE,
        (
            "……うっし、今日も\x01",
            "頑張って声を出すかぁ！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_2E1D")

    label("loc_2DC2")


    #C0121
    ChrTalk(
        0xFE,
        "らっしゃい、らっしゃ～い！\x02",
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0xFE,
        (
            "つやつや新鮮、お買い得の\x01",
            "フレッシュ・ディンズだよっ！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E1D")

    Jump("loc_336B")

    label("loc_2E22")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_2F51")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2EFC")

    #C0123
    ChrTalk(
        0xFE,
        (
            "らっしゃい、らっしゃい！\x01",
            "今日もフレッシュ・ディンズは\x01",
            "絶好調だ！\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0xFE,
        (
            "自慢じゃねえが、\x01",
            "こちとら店を始めてから\x01",
            "一度も休んだ事はねえのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0xFE,
        (
            "大事なお客さんが\x01",
            "店先で待ってんだからよっ！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_2F4C")

    label("loc_2EFC")


    #C0126
    ChrTalk(
        0xFE,
        (
            "らっしゃい、らっしゃい！\x01",
            "フレッシュ・ディンズは\x01",
            "年中無休、毎日開店だよっ！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F4C")

    Jump("loc_336B")

    label("loc_2F51")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_30B0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_302A")

    #C0127
    ChrTalk(
        0xFE,
        "らっしゃい、らっしゃ～い！\x02",
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0xFE,
        (
            "今朝は元気な娘さんが\x01",
            "立ち寄ってくれてねえ。\x01",
            "世間話に花を咲かせちまったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0xFE,
        (
            "でも栗髪のツインテールで\x01",
            "見かけねえ子だったな。\x01",
            "最近越してきた子かねえ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_30AB")

    label("loc_302A")


    #C0130
    ChrTalk(
        0xFE,
        (
            "今朝は元気な娘さんが\x01",
            "立ち寄ってくれてねえ。\x01",
            "こっちも元気貰っちまったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0xFE,
        (
            "見かけねえ子だったが\x01",
            "最近越してきた人かねえ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_30AB")

    Jump("loc_336B")

    label("loc_30B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_31A7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3144")

    #C0132
    ChrTalk(
        0xFE,
        "らっしゃい、らっしゃ～い！\x02",
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0xFE,
        (
            "うちの野菜は採れたて新鮮、\x01",
            "お手ごろ値段でお買い得だ！\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0xFE,
        "買って損はさせないよっ！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_31A2")

    label("loc_3144")


    #C0135
    ChrTalk(
        0xFE,
        (
            "うちの新鮮な野菜を\x01",
            "超お買い得価格で提供してるぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0xFE,
        (
            "さあさあ\x01",
            "買って損はさせないよっ！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_31A2")

    Jump("loc_336B")

    label("loc_31A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_336B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_331C")

    #C0137
    ChrTalk(
        0xFE,
        (
            "へい、らっしゃい\x01",
            "らっしゃ～い！\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0xFE,
        (
            "おっ、お兄さん達見かけない顔だね！\x01",
            "今なら１つおまけしとくよっ！\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0x104,
        (
            "#0300Fひゅー、野菜だって\x01",
            "これだけ並んでると壮観だなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0x102,
        (
            "#0100F露店の商品って\x01",
            "なぜだか欲しくなっちゃうわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0xFE,
        (
            "おっ、お客さんたち\x01",
            "嬉しい事言ってくれるねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0xFE,
        (
            "こいつはアルモリカ村からの直送品だ。\x01",
            "好きなだけ選んでってくれよ！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_336B")

    label("loc_331C")


    #C0143
    ChrTalk(
        0xFE,
        (
            "うちはアルモリカ村からの\x01",
            "直送品も扱ってるよっ！\x02",
        )
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0xFE,
        "さあ買った買ったあ！\x02",
    )

    CloseMessageWindow()

    label("loc_336B")

    Jump("loc_212C")

    label("loc_3370")

    TalkEnd(0xFE)
    Return()

    # Function_11_211F end

    def Function_12_3374(): pass

    label("Function_12_3374")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2, 0x1, 0x0)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2, 0x1, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3544")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_34EC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3404")

    #C0145
    ChrTalk(
        0x101,
        (
            "#0003F（東通りの市場……\x01",
            "  落し物をしたトロントさんが\x01",
            "  立ち寄っていた場所だな。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 1)

    label("loc_3404")


    #C0146
    ChrTalk(
        0x101,
        (
            "#0000Fすみません、この辺りで\x01",
            "落し物を見かけませんでしたか？\x02",
        )
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0xFE,
        (
            "落し物～？\x01",
            "さあ、あたしは見てないな～。\x02",
        )
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0xFE,
        (
            "でも市場に来る人は多いし\x01",
            "落し物とかは珍しくないわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0xFE,
        (
            "誰かに聞いてみたら？\x01",
            "拾ってくれてる人がいるかも。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_353F")

    label("loc_34EC")


    #C0150
    ChrTalk(
        0xFE,
        (
            "落し物を探してるなら\x01",
            "誰かに聞いてみたら？\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0xFE,
        "拾ってくれてる人がいるかもよ。\x02",
    )

    CloseMessageWindow()

    label("loc_353F")

    Jump("loc_444D")

    label("loc_3544")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_3693")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3607")

    #C0152
    ChrTalk(
        0xFE,
        (
            "ディンズったら……\x01",
            "いい気なもんねぇ……\x02",
        )
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0xFE,
        (
            "商工会への誘いを\x01",
            "あっさり断っちゃって\x01",
            "今日も地道なお商売よ。\x02",
        )
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0xFE,
        (
            "ほんっと商売一筋っていうか……\x01",
            "馬鹿正直なのよねぇ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_368E")

    label("loc_3607")


    #C0155
    ChrTalk(
        0xFE,
        (
            "馬鹿正直でお商売一筋……\x01",
            "これじゃ悪い人に騙されても\x01",
            "絶対に気付かないわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0xFE,
        (
            "やれやれ、やっぱり私が\x01",
            "ついてなくちゃ駄目みたいね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_368E")

    Jump("loc_444D")

    label("loc_3693")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_37F1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_376C")

    #C0157
    ChrTalk(
        0xFE,
        (
            "商工会の会長さんから\x01",
            "正式な話があったみたいなの。\x02",
        )
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0xFE,
        (
            "ディンズにしちゃ\x01",
            "珍しく悩んでるみたいよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0xFE,
        (
            "んもう……ちゃっちゃと\x01",
            "受けちゃいなさいよね。\x01",
            "商人としてのステップアップじゃない。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_37EC")

    label("loc_376C")


    #C0160
    ChrTalk(
        0xFE,
        (
            "商工会に入れば\x01",
            "じーさまたちの援助も受けられるわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0xFE,
        (
            "勉強になることも沢山あるだろうし\x01",
            "商人としてステップアップじゃない。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_37EC")

    Jump("loc_444D")

    label("loc_37F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_38FD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3888")

    #C0162
    ChrTalk(
        0xFE,
        "いらっしゃ～い！\x02",
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0xFE,
        (
            "何だか事件があったそうだけど\x01",
            "ウチは平常営業よ。\x02",
        )
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0xFE,
        (
            "ま、あんまり気にしないで\x01",
            "買って行って頂戴。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_38F8")

    label("loc_3888")


    #C0165
    ChrTalk(
        0xFE,
        (
            "にしても……\x01",
            "ディンズはホントいつも通りね。\x02",
        )
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0xFE,
        (
            "噂を気にしてないっていうか\x01",
            "気付いてないんじゃないかしら。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_38F8")

    Jump("loc_444D")

    label("loc_38FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_39E8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_39A4")

    #C0167
    ChrTalk(
        0xFE,
        (
            "ディンズのやつ、連中に殴られて\x01",
            "昨日は病院に行っていたのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0xFE,
        "ったく、あったまくるわ～。\x02",
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0xFE,
        (
            "もちろん滅多な事は\x01",
            "できないけどさぁ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_39E3")

    label("loc_39A4")


    #C0170
    ChrTalk(
        0xFE,
        (
            "くぅ、あたしにも力があれば\x01",
            "ぶん殴ってやる所なんだけど……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_39E3")

    Jump("loc_444D")

    label("loc_39E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_3AE3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3AC2")

    #C0171
    ChrTalk(
        0xFE,
        (
            "商工会のじーさまたち、\x01",
            "ディンズを役員に誘おうとしてるのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0xFE,
        (
            "いつも誠実な商売だから\x01",
            "すっかり認めてくれたみたいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0xFE,
        (
            "でもディンズは鈍いから……\x01",
            "そういうトコ全然気付かないのよね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_3ADE")

    label("loc_3AC2")


    #C0174
    ChrTalk(
        0xFE,
        "ふう、駄目だわこりゃ。\x02",
    )

    CloseMessageWindow()

    label("loc_3ADE")

    Jump("loc_444D")

    label("loc_3AE3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_3C0F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3BA8")

    #C0175
    ChrTalk(
        0xFE,
        (
            "やれやれ……\x01",
            "ディンズったら鈍いわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0xFE,
        (
            "商工会に入らないかって\x01",
            "誘われてるんじゃない。\x02",
        )
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0xFE,
        (
            "商工会のじーさま達に\x01",
            "優良な店として認められるなんて\x01",
            "とても名誉な事よ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_3C0A")

    label("loc_3BA8")


    #C0178
    ChrTalk(
        0xFE,
        (
            "商工会に入れるなんて\x01",
            "とても名誉な事よ。\x02",
        )
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0xFE,
        (
            "でも、本人が判ってないんじゃ\x01",
            "仕方ないわよねぇ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3C0A")

    Jump("loc_444D")

    label("loc_3C0F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_3C9D")

    #C0180
    ChrTalk(
        0xFE,
        "いらっしゃ～い！\x02",
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0xFE,
        (
            "記念祭の間は\x01",
            "あちこちで安売りをするのよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0xFE,
        (
            "うちも売り出すつもりだから\x01",
            "ばっちり期待していてね！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_444D")

    label("loc_3C9D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_3DC4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D57")

    #C0183
    ChrTalk(
        0xFE,
        (
            "アルカンシェルの話題の新人に\x01",
            "リーシャって人がいるじゃない。\x02",
        )
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0xFE,
        (
            "あの人……\x01",
            "ときどき見かけるのよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0xFE,
        (
            "もしかしてこの近くに\x01",
            "住んでるんじゃないかしら。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_3DBF")

    label("loc_3D57")


    #C0186
    ChrTalk(
        0xFE,
        (
            "リーシャさん、時々\x01",
            "露店街で買い物してるわよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0xFE,
        (
            "もしかしてこの近くに\x01",
            "住んでるんじゃないかしら。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3DBF")

    Jump("loc_444D")

    label("loc_3DC4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_3F1E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3EC1")

    #C0188
    ChrTalk(
        0xFE,
        (
            "アルカンシェルの\x01",
            "チケット、欲しかったな～。\x02",
        )
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0xFE,
        (
            "公演を観た後は\x01",
            "百貨店でショッピングしてぇ……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0190
    ChrTalk(
        0xFE,
        "……って、そうじゃなくって！\x02",
    )

    CloseMessageWindow()

    #C0191
    ChrTalk(
        0xFE,
        (
            "い、いらっしゃいませ～。\x01",
            "フレッシュ・ディンズへようこそ～。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_3F19")

    label("loc_3EC1")


    #C0192
    ChrTalk(
        0xFE,
        (
            "いけないいけない。\x01",
            "陽気のせいかしら……\x02",
        )
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0xFE,
        (
            "つい物欲が\x01",
            "ほとばしってしまったわね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3F19")

    Jump("loc_444D")

    label("loc_3F1E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_3FE3")

    #C0194
    ChrTalk(
        0xFE,
        (
            "いらっしゃ～い！\x01",
            "フレッシュ・ディンズへようこそ！\x02",
        )
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0xFE,
        (
            "店主がちょっとお人よしだけど\x01",
            "ま、誠実な店には違いないわよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0xFE,
        (
            "お野菜ならフレッシュ・ディンズ！\x01",
            "バッチリ見て行って頂戴！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_444D")

    label("loc_3FE3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_40F1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_408E")

    #C0197
    ChrTalk(
        0xFE,
        (
            "ディンズのお商売は\x01",
            "誠実っていうか、何ていうか……\x02",
        )
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0xFE,
        (
            "売れ残りのお野菜なんて\x01",
            "ご近所に配っちゃうのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0xFE,
        "これじゃただのお人よしよねぇ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_40EC")

    label("loc_408E")


    #C0200
    ChrTalk(
        0xFE,
        (
            "ディンズは誠実を通り越して\x01",
            "馬鹿正直なのよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0xFE,
        (
            "……幼馴染としちゃ\x01",
            "やっぱり心配だわ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_40EC")

    Jump("loc_444D")

    label("loc_40F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_42B5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_421E")

    #C0202
    ChrTalk(
        0xFE,
        (
            "東通りには『商工会』って\x01",
            "組織があるのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0203
    ChrTalk(
        0xFE,
        (
            "もともと露店街の\x01",
            "商人たちのまとめ役だったけど、\x01",
            "今じゃ地域の代表みたいなものね。\x02",
        )
    )

    CloseMessageWindow()

    #C0204
    ChrTalk(
        0xFE,
        (
            "クロスベルには\x01",
            "貿易や先物取り引きなんかで\x01",
            "荒稼ぎする商人も多いけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0205
    ChrTalk(
        0xFE,
        (
            "少なくとも東通りの露店じゃ\x01",
            "そういう人は認められてないのよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_42B0")

    label("loc_421E")


    #C0206
    ChrTalk(
        0xFE,
        (
            "商工会のじーさま達は\x01",
            "みんな露天商上がりの人たちよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0207
    ChrTalk(
        0xFE,
        (
            "荒稼ぎする商売なんかも\x01",
            "団結して認めていないの。\x02",
        )
    )

    CloseMessageWindow()

    #C0208
    ChrTalk(
        0xFE,
        "まさに東通りの纏め役って所ね。\x02",
    )

    CloseMessageWindow()

    label("loc_42B0")

    Jump("loc_444D")

    label("loc_42B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_43F1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4386")

    #C0209
    ChrTalk(
        0xFE,
        (
            "ディンズって思い込んだら\x01",
            "一直線なのよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0210
    ChrTalk(
        0xFE,
        (
            "おまけに馬鹿正直で\x01",
            "人を疑うってことを知らないの。\x02",
        )
    )

    CloseMessageWindow()

    #C0211
    ChrTalk(
        0xFE,
        (
            "なのに商売を始めるだなんて\x01",
            "言い出しちゃって……\x01",
            "幼馴染としては心配だわね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_43EC")

    label("loc_4386")


    #C0212
    ChrTalk(
        0xFE,
        (
            "ディンズって思い込んだら\x01",
            "一直線な所があるのよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0213
    ChrTalk(
        0xFE,
        (
            "お客さんには\x01",
            "好かれてるからいいんだけど。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_43EC")

    Jump("loc_444D")

    label("loc_43F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_444D")

    #C0214
    ChrTalk(
        0xFE,
        "あ、いらっしゃい！\x02",
    )

    CloseMessageWindow()

    #C0215
    ChrTalk(
        0xFE,
        (
            "うちのお野菜はぴっかぴかよ！\x01",
            "バッチリ買って行ってね！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_444D")

    TalkEnd(0xFE)
    Return()

    # Function_12_3374 end

    def Function_13_4451(): pass

    label("Function_13_4451")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2, 0x1, 0x0)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2, 0x1, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_447E")
    TurnDirection(0x0, 0xB, 0)
    OP_4B(0xB, 0xFF)
    Call(0, 34)
    Return()

    label("loc_447E")

    TalkBegin(0xFE)
    ClearScenarioFlags(0x2, 3)
    Call(0, 15)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_45CB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 3)), scpexpr(EXPR_END)), "loc_45C3")

    #C0216
    ChrTalk(
        0xFE,
        (
            "あらあんたたち。\x01",
            "活きのイイ魚を持ってるみたいだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0217
    ChrTalk(
        0xFE,
        (
            "あんた達で釣り上げたのかい？\x01",
            "傷も付いてないし……そのまま店に\x01",
            "並べたって良さそうじゃないか。\x02",
        )
    )

    CloseMessageWindow()

    #C0218
    ChrTalk(
        0xFE,
        (
            "ふむ、どうだい。\x01",
            "その魚をあたしの店に\x01",
            "卸しちゃくれないかい？\x02",
        )
    )

    CloseMessageWindow()

    #C0219
    ChrTalk(
        0xFE,
        (
            "クロスベル産の魚も人気があるんだ。\x01",
            "多少のお礼はするよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x51, 7)
    SetScenarioFlags(0x2, 2)
    TalkEnd(0xFE)
    Return()

    label("loc_45C3")

    Call(0, 14)
    Jump("loc_611F")

    label("loc_45CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 3)), scpexpr(EXPR_END)), "loc_611C")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_45DE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6117")
    FadeToDark(300, 0, 100)
    MenuCmd(0, 1)
    MenuCmd(1, 1, "話をする")
    MenuCmd(1, 1, "魚を渡す")
    MenuCmd(1, 1, "やめる")
    ClearScenarioFlags(0x2, 3)
    Call(0, 15)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4630")
    MenuCmd(3, 1, 0x1)

    label("loc_4630")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuCmd(2, 1, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x1)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4662")
    FadeToBright(300, 0)
    OP_0D()

    label("loc_4662")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_60E2")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_467B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_60D3")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuCmd(0, 1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x15E, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_46EC")
    MenuCmd(1, 1, "スノーシュラブ　　　地 × 10")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x15E, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_46E2")
    Call(0, 16)

    label("loc_46E2")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_46EC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x15F, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4741")
    MenuCmd(1, 1, "アルモリカブナ　　　水 × 10")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x15F, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4737")
    Call(0, 16)

    label("loc_4737")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4741")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x2, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x160, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4796")
    MenuCmd(1, 1, "オロショ　　　　　　火 × 10")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x160, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_478C")
    Call(0, 16)

    label("loc_478C")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4796")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x3, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x161, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_47EB")
    MenuCmd(1, 1, "ロック　　　　　　　風 × 10")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x161, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_47E1")
    Call(0, 16)

    label("loc_47E1")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_47EB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x4, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x162, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4840")
    MenuCmd(1, 1, "カルプ　　　　　　　時 × 10")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x162, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4836")
    Call(0, 16)

    label("loc_4836")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4840")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x5, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x163, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4895")
    MenuCmd(1, 1, "レイニー　　　　　　幻 × 10")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x163, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_488B")
    Call(0, 16)

    label("loc_488B")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4895")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x6, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x164, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_48EA")
    MenuCmd(1, 1, "エーゼル　　　　　　地 × 20")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x164, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_48E0")
    Call(0, 16)

    label("loc_48E0")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_48EA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x7, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x165, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_493F")
    MenuCmd(1, 1, "カサギン　　　　　　水 × 20")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x165, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4935")
    Call(0, 16)

    label("loc_4935")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_493F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x8, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x166, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4994")
    MenuCmd(1, 1, "レインボウ　　　　　火 × 20")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x166, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_498A")
    Call(0, 16)

    label("loc_498A")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4994")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x9, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x167, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_49E9")
    MenuCmd(1, 1, "トラード　　　　　　風 × 20")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x167, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_49DF")
    Call(0, 16)

    label("loc_49DF")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_49E9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0xA, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x168, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4A3E")
    MenuCmd(1, 1, "サモーナ　　　　　　時 × 20")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x168, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4A34")
    Call(0, 16)

    label("loc_4A34")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4A3E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0xB, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x169, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4A93")
    MenuCmd(1, 1, "イール　　　　　　　幻 × 20")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x169, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4A89")
    Call(0, 16)

    label("loc_4A89")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4A93")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0xC, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16A, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4AE8")
    MenuCmd(1, 1, "パールグラス　　　　空 × 20")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16A, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4ADE")
    Call(0, 16)

    label("loc_4ADE")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4AE8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0xD, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16B, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4B3D")
    MenuCmd(1, 1, "グラトンバス　　　　地 × 40")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16B, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4B33")
    Call(0, 16)

    label("loc_4B33")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4B3D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0xE, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16C, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4B92")
    MenuCmd(1, 1, "バイパーヘッド　　　水 × 40")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16C, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4B88")
    Call(0, 16)

    label("loc_4B88")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4B92")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0xF, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16D, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4BE7")
    MenuCmd(1, 1, "パイソンヘッド　　　火 × 40")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4BDD")
    Call(0, 16)

    label("loc_4BDD")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4BE7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x10, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16E, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4C3C")
    MenuCmd(1, 1, "タイタン　　　　　　風 × 40")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16E, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4C32")
    Call(0, 16)

    label("loc_4C32")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4C3C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x11, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16F, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4C91")
    MenuCmd(1, 1, "クインシザー　　　　時 × 50")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16F, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4C87")
    Call(0, 16)

    label("loc_4C87")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4C91")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x12, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x170, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4CE6")
    MenuCmd(1, 1, "エレキイール　　　　幻 × 50")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x170, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4CDC")
    Call(0, 16)

    label("loc_4CDC")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4CE6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x13, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x171, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4D3B")
    MenuCmd(1, 1, "デモンタイタン　　　時 × 50")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x171, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4D31")
    Call(0, 16)

    label("loc_4D31")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4D3B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x14, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x172, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4D90")
    MenuCmd(1, 1, "アークシュラブ　　　空 × 50")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x172, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4D86")
    Call(0, 16)

    label("loc_4D86")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4D90")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x15, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x173, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4DE6")
    MenuCmd(1, 1, "ゴルドサモーナ　　　時 × 100")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x173, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4DDC")
    Call(0, 16)

    label("loc_4DDC")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4DE6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x16, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x174, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4E3C")
    MenuCmd(1, 1, "ノーブルカルプ　　　空 × 100")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x174, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4E32")
    Call(0, 16)

    label("loc_4E32")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4E3C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x17, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x175, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4E92")
    MenuCmd(1, 1, "サーペントヘッド　　幻 × 100")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x175, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4E88")
    Call(0, 16)

    label("loc_4E88")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4E92")

    MenuCmd(1, 1, "やめる")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuCmd(2, 1, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x1)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4ED3")
    Jump("loc_60CE")

    label("loc_4ED3")

    FadeToBright(300, 0)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x15E, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4F60")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4F56")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0220
    ChrTalk(
        0xFE,
        (
            "この魚を\x07\x02",

            "#56I地のセピス10個\x07\x00",
            "で\x01",
            "渡してくれるかい？\x02",
        )
    )


    label("loc_4F56")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4F60")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x15F, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4FD0")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4FC6")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0221
    ChrTalk(
        0xFE,
        (
            "この魚を\x07\x02",

            "#57I水のセピス10個\x07\x00",
            "で\x01",
            "渡してくれるかい？\x02",
        )
    )


    label("loc_4FC6")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4FD0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x2, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x160, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5040")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5036")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0222
    ChrTalk(
        0xFE,
        (
            "この魚を\x07\x02",

            "#58I火のセピス10個\x07\x00",
            "で\x01",
            "渡してくれるかい？\x02",
        )
    )


    label("loc_5036")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_5040")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x3, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x161, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_50B0")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_50A6")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0223
    ChrTalk(
        0xFE,
        (
            "この魚を\x07\x02",

            "#59I風のセピス10個\x07\x00",
            "で\x01",
            "渡してくれるかい？\x02",
        )
    )


    label("loc_50A6")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_50B0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x4, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x162, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5120")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5116")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0224
    ChrTalk(
        0xFE,
        (
            "この魚を\x07\x02",

            "#60I時のセピス10個\x07\x00",
            "で\x01",
            "渡してくれるかい？\x02",
        )
    )


    label("loc_5116")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_5120")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x5, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x163, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5190")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5186")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0225
    ChrTalk(
        0xFE,
        (
            "この魚を\x07\x02",

            "#62I幻のセピス10個\x07\x00",
            "で\x01",
            "渡してくれるかい？\x02",
        )
    )


    label("loc_5186")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_5190")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x6, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x164, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5200")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_51F6")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0226
    ChrTalk(
        0xFE,
        (
            "この魚を\x07\x02",

            "#56I地のセピス20個\x07\x00",
            "で\x01",
            "渡してくれるかい？\x02",
        )
    )


    label("loc_51F6")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_5200")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x7, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x165, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5270")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5266")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0227
    ChrTalk(
        0xFE,
        (
            "この魚を\x07\x02",

            "#57I水のセピス20個\x07\x00",
            "で\x01",
            "渡してくれるかい？\x02",
        )
    )


    label("loc_5266")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_5270")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x8, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x166, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_52E0")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_52D6")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0228
    ChrTalk(
        0xFE,
        (
            "この魚を\x07\x02",

            "#58I火のセピス20個\x07\x00",
            "で\x01",
            "渡してくれるかい？\x02",
        )
    )


    label("loc_52D6")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_52E0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x9, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x167, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5350")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5346")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0229
    ChrTalk(
        0xFE,
        (
            "この魚を\x07\x02",

            "#59I風のセピス20個\x07\x00",
            "で\x01",
            "渡してくれるかい？\x02",
        )
    )


    label("loc_5346")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_5350")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0xA, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x168, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_53C0")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_53B6")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0230
    ChrTalk(
        0xFE,
        (
            "この魚を\x07\x02",

            "#60I時のセピス20個\x07\x00",
            "で\x01",
            "渡してくれるかい？\x02",
        )
    )


    label("loc_53B6")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_53C0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0xB, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x169, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5430")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5426")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0231
    ChrTalk(
        0xFE,
        (
            "この魚を\x07\x02",

            "#62I幻のセピス20個\x07\x00",
            "で\x01",
            "渡してくれるかい？\x02",
        )
    )


    label("loc_5426")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_5430")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0xC, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16A, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_54A0")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5496")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0232
    ChrTalk(
        0xFE,
        (
            "この魚を\x07\x02",

            "#61I空のセピス20個\x07\x00",
            "で\x01",
            "渡してくれるかい？\x02",
        )
    )


    label("loc_5496")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_54A0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0xD, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16B, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5510")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5506")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0233
    ChrTalk(
        0xFE,
        (
            "この魚を\x07\x02",

            "#56I地のセピス40個\x07\x00",
            "で\x01",
            "渡してくれるかい？\x02",
        )
    )


    label("loc_5506")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_5510")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0xE, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16C, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5580")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5576")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0234
    ChrTalk(
        0xFE,
        (
            "この魚を\x07\x02",

            "#57I水のセピス40個\x07\x00",
            "で\x01",
            "渡してくれるかい？\x02",
        )
    )


    label("loc_5576")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_5580")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0xF, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16D, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_55F0")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_55E6")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0235
    ChrTalk(
        0xFE,
        (
            "この魚を\x07\x02",

            "#58I火のセピス40個\x07\x00",
            "で\x01",
            "渡してくれるかい？\x02",
        )
    )


    label("loc_55E6")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_55F0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x10, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16E, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5660")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5656")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0236
    ChrTalk(
        0xFE,
        (
            "この魚を\x07\x02",

            "#59I風のセピス40個\x07\x00",
            "で\x01",
            "渡してくれるかい？\x02",
        )
    )


    label("loc_5656")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_5660")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x11, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16F, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_56D0")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_56C6")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x11), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0237
    ChrTalk(
        0xFE,
        (
            "この魚を\x07\x02",

            "#60I時のセピス50個\x07\x00",
            "で\x01",
            "渡してくれるかい？\x02",
        )
    )


    label("loc_56C6")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_56D0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x12, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x170, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5740")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5736")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x12), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0238
    ChrTalk(
        0xFE,
        (
            "この魚を\x07\x02",

            "#62I幻のセピス50個\x07\x00",
            "で\x01",
            "渡してくれるかい？\x02",
        )
    )


    label("loc_5736")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_5740")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x13, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x171, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_57B0")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_57A6")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x13), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0239
    ChrTalk(
        0xFE,
        (
            "この魚を\x07\x02",

            "#60I時のセピス50個\x07\x00",
            "で\x01",
            "渡してくれるかい？\x02",
        )
    )


    label("loc_57A6")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_57B0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x14, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x172, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5820")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5816")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0240
    ChrTalk(
        0xFE,
        (
            "この魚を\x07\x02",

            "#61I空のセピス50個\x07\x00",
            "で\x01",
            "渡してくれるかい？\x02",
        )
    )


    label("loc_5816")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_5820")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x15, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x173, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5891")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5887")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x15), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0241
    ChrTalk(
        0xFE,
        (
            "この魚を\x07\x02",

            "#60I時のセピス100個\x07\x00",
            "で\x01",
            "渡してくれるかい？\x02",
        )
    )


    label("loc_5887")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_5891")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x16, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x174, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5902")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_58F8")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x16), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0242
    ChrTalk(
        0xFE,
        (
            "この魚を\x07\x02",

            "#61I空のセピス100個\x07\x00",
            "で\x01",
            "渡してくれるかい？\x02",
        )
    )


    label("loc_58F8")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_5902")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x17, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x175, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5973")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5969")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x17), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0243
    ChrTalk(
        0xFE,
        (
            "この魚を\x07\x02",

            "#62I幻のセピス100個\x07\x00",
            "で\x01",
            "渡してくれるかい？\x02",
        )
    )


    label("loc_5969")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_5973")

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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_60CE")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x15), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x16), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x17), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5A83")

    #C0244
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5A83")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5A83")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_60C4")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sleep(300)
    Sound(17, 0, 100, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_5B4A"),
        (1, "loc_5B83"),
        (2, "loc_5BBC"),
        (3, "loc_5BF5"),
        (4, "loc_5C2E"),
        (5, "loc_5C67"),
        (6, "loc_5CA0"),
        (7, "loc_5CD9"),
        (8, "loc_5D12"),
        (9, "loc_5D4B"),
        (10, "loc_5D84"),
        (11, "loc_5DBD"),
        (12, "loc_5DF6"),
        (13, "loc_5E2F"),
        (14, "loc_5E68"),
        (15, "loc_5EA1"),
        (16, "loc_5EDA"),
        (17, "loc_5F13"),
        (18, "loc_5F4C"),
        (19, "loc_5F85"),
        (20, "loc_5FBE"),
        (21, "loc_5FF7"),
        (22, "loc_6032"),
        (23, "loc_606D"),
        (SWITCH_DEFAULT, "loc_60A8"),
    )


    label("loc_5B4A")


    #A0245
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
    Jump("loc_60A8")

    label("loc_5B83")


    #A0246
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
    Jump("loc_60A8")

    label("loc_5BBC")


    #A0247
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
    Jump("loc_60A8")

    label("loc_5BF5")


    #A0248
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
    Jump("loc_60A8")

    label("loc_5C2E")


    #A0249
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
    Jump("loc_60A8")

    label("loc_5C67")


    #A0250
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
    Jump("loc_60A8")

    label("loc_5CA0")


    #A0251
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
    Jump("loc_60A8")

    label("loc_5CD9")


    #A0252
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
    Jump("loc_60A8")

    label("loc_5D12")


    #A0253
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
    Jump("loc_60A8")

    label("loc_5D4B")


    #A0254
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
    Jump("loc_60A8")

    label("loc_5D84")


    #A0255
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
    Jump("loc_60A8")

    label("loc_5DBD")


    #A0256
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
    Jump("loc_60A8")

    label("loc_5DF6")


    #A0257
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
    Jump("loc_60A8")

    label("loc_5E2F")


    #A0258
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
    Jump("loc_60A8")

    label("loc_5E68")


    #A0259
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
    Jump("loc_60A8")

    label("loc_5EA1")


    #A0260
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
    Jump("loc_60A8")

    label("loc_5EDA")


    #A0261
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
    Jump("loc_60A8")

    label("loc_5F13")


    #A0262
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
    Jump("loc_60A8")

    label("loc_5F4C")


    #A0263
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
    Jump("loc_60A8")

    label("loc_5F85")


    #A0264
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
    Jump("loc_60A8")

    label("loc_5FBE")


    #A0265
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
    Jump("loc_60A8")

    label("loc_5FF7")


    #A0266
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
    Jump("loc_60A8")

    label("loc_6032")


    #A0267
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
    Jump("loc_60A8")

    label("loc_606D")


    #A0268
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
    Jump("loc_60A8")

    label("loc_60A8")

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_60CE")

    label("loc_60C4")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_60CE")

    Jump("loc_467B")

    label("loc_60D3")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6112")

    label("loc_60E2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_60F6")
    Jump("loc_6112")

    label("loc_60F6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6112")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 14)

    label("loc_6112")

    Jump("loc_45DE")

    label("loc_6117")

    Jump("loc_611F")

    label("loc_611C")

    Call(0, 14)

    label("loc_611F")

    TalkEnd(0xB)
    Return()

    # Function_13_4451 end

    def Function_14_6123(): pass

    label("Function_14_6123")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_END)), "loc_61F9")

    #C0269
    ChrTalk(
        0xB,
        (
            "クロスベル産の魚も人気があるんだが\x01",
            "仕入れ先が少なくてね。\x01",
            "いつも品薄気味なんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0270
    ChrTalk(
        0xB,
        (
            "あんた達の持ってる魚は\x01",
            "中々質が良さそうだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0271
    ChrTalk(
        0xB,
        (
            "良ければあたしの店に卸しておくれよ。\x01",
            "多少のお礼はするよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7231")

    label("loc_61F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_END)), "loc_62C1")

    #C0272
    ChrTalk(
        0xB,
        (
            "警察の人が直接\x01",
            "引き取りに来るなんて珍しいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0273
    ChrTalk(
        0xB,
        (
            "まあいいや、あんたらで\x01",
            "あの子に届けてやってくんなよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0274
    ChrTalk(
        0x101,
        "#0000Fええ、お任せください。\x02",
    )

    CloseMessageWindow()

    #C0275
    ChrTalk(
        0x102,
        "#0100Fご協力ありがとうございました。\x02",
    )

    CloseMessageWindow()
    Jump("loc_7231")

    label("loc_62C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_63C2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6378")

    #C0276
    ChrTalk(
        0xB,
        (
            "朝からクロスベルタイムズの人が\x01",
            "ウロウロしてるみたいだねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0277
    ChrTalk(
        0xB,
        "遊撃士の人も慌しそうだし……\x02",
    )

    CloseMessageWindow()

    #C0278
    ChrTalk(
        0xB,
        (
            "みんなして何をしてるんだろう。\x01",
            "気になっちまうねえ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_63BD")

    label("loc_6378")


    #C0279
    ChrTalk(
        0xB,
        (
            "今日は街が慌しい気がするよ。\x01",
            "みんなして何をしてるんだろうねぇ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_63BD")

    Jump("loc_7231")

    label("loc_63C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_64B3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6471")

    #C0280
    ChrTalk(
        0xB,
        (
            "今朝旧市街の不良が\x01",
            "心配そうな顔で訪ねてきたんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0281
    ChrTalk(
        0xB,
        "仲間を知らないかってねぇ……\x02",
    )

    CloseMessageWindow()

    #C0282
    ChrTalk(
        0xB,
        (
            "さあ、見てないけど……\x01",
            "喧嘩でもしちゃったのかねえ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_64AE")

    label("loc_6471")


    #C0283
    ChrTalk(
        0xB,
        (
            "旧市街の不良たち、仲間内で\x01",
            "喧嘩でもしちゃったのかねえ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_64AE")

    Jump("loc_7231")

    label("loc_64B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_65B5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6562")

    #C0284
    ChrTalk(
        0xB,
        "何か事件があったって噂だけど……\x02",
    )

    CloseMessageWindow()

    #C0285
    ChrTalk(
        0xB,
        (
            "その程度で店を\x01",
            "閉めたりなんかはしないよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0286
    ChrTalk(
        0xB,
        (
            "昔のクロスベル商人なんて\x01",
            "戦争中でも営業してたんだからね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_65B0")

    label("loc_6562")


    #C0287
    ChrTalk(
        0xB,
        (
            "あたしもクロスベル商人の端くれだ。\x01",
            "何があっても\x01",
            "店を閉める気はないよっ！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_65B0")

    Jump("loc_7231")

    label("loc_65B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_66FB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6694")

    #C0288
    ChrTalk(
        0xB,
        (
            "まったくルバーチェの\x01",
            "連中と来たら……\x02",
        )
    )

    CloseMessageWindow()

    #C0289
    ChrTalk(
        0xB,
        (
            "最近は共和国から\x01",
            "別のマフィアが入ってきたそうだけど\x01",
            "そっちの方がマシなんじゃないのかい？\x02",
        )
    )

    CloseMessageWindow()

    #C0290
    ChrTalk(
        0xB,
        (
            "まあ……マフィアに\x01",
            "良いも悪いもないとは思うけどねえ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_66F6")

    label("loc_6694")


    #C0291
    ChrTalk(
        0xB,
        (
            "そういえば物騒な事件も\x01",
            "増えてるそうじゃないか。\x02",
        )
    )

    CloseMessageWindow()

    #C0292
    ChrTalk(
        0xB,
        (
            "あんたたちも\x01",
            "気をつけないといけないよ？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_66F6")

    Jump("loc_7231")

    label("loc_66FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_679C")

    #C0293
    ChrTalk(
        0xB,
        "はいよ、いらっしゃい。\x02",
    )

    CloseMessageWindow()

    #C0294
    ChrTalk(
        0xB,
        (
            "記念祭が終わっても\x01",
            "まだ滞在してる\x01",
            "観光客がいるみたいだねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0295
    ChrTalk(
        0xB,
        (
            "もう１週間になるってのに\x01",
            "売り上げは悪くないよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7231")

    label("loc_679C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_68E3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6868")

    #C0296
    ChrTalk(
        0xFE,
        (
            "ようやく共和国方面の街道が\x01",
            "復旧したらしいわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0297
    ChrTalk(
        0xFE,
        (
            "ただのトラック事故にしちゃあ\x01",
            "随分時間が掛かったわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0298
    ChrTalk(
        0xFE,
        (
            "……まあいいわ、仕入れの魚さえ\x01",
            "届いてくれば文句はいわないさ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_68DE")

    label("loc_6868")


    #C0299
    ChrTalk(
        0xFE,
        (
            "最近おかしな事故が\x01",
            "増えているみたいだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0300
    ChrTalk(
        0xFE,
        (
            "……まあいいわ、仕入れの魚さえ\x01",
            "届いてくれば文句はいわないさ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_68DE")

    Jump("loc_7231")

    label("loc_68E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_6A1C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_69B1")

    #C0301
    ChrTalk(
        0xFE,
        "はいよ、いらっしゃ～い！\x02",
    )

    CloseMessageWindow()

    #C0302
    ChrTalk(
        0xFE,
        (
            "しばらく釣公師団の人から\x01",
            "魚を買い上げることにしてね。\x01",
            "一応新鮮なのも入ってるよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0303
    ChrTalk(
        0xFE,
        (
            "トラック便が遅れてるのが痛いけど\x01",
            "何とか凌がなくちゃねぇ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_6A17")

    label("loc_69B1")


    #C0304
    ChrTalk(
        0xFE,
        (
            "例のトラック事故のせいで\x01",
            "仕入れが滞りがちなんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0305
    ChrTalk(
        0xFE,
        (
            "何とか工夫して\x01",
            "乗り切らなくっちゃ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6A17")

    Jump("loc_7231")

    label("loc_6A1C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_6AE5")

    #C0306
    ChrTalk(
        0xFE,
        (
            "悪いけど今日の魚は\x01",
            "品揃えがいまいちなんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0307
    ChrTalk(
        0xFE,
        (
            "共和国であったトラック事故、\x01",
            "まだ街道を塞いじゃってるみたいでね。\x02",
        )
    )

    CloseMessageWindow()

    #C0308
    ChrTalk(
        0xFE,
        (
            "向こうからのトラック便が\x01",
            "ほとんどストップしちまってるのさ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7231")

    label("loc_6AE5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_6C1E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6BA4")

    #C0309
    ChrTalk(
        0xFE,
        (
            "近頃、共和国の方で\x01",
            "トラックの事故が増えてるらしくてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0310
    ChrTalk(
        0xFE,
        (
            "そのたびに街道が塞がっちまって、\x01",
            "仕入れの魚が遅れたりするんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0311
    ChrTalk(
        0xFE,
        "ふう、全く困ったものだわ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_6C16")

    label("loc_6BA4")


    #C0312
    ChrTalk(
        0xFE,
        (
            "近頃、共和国の方で\x01",
            "トラックの事故が増えてるんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0313
    ChrTalk(
        0xFE,
        (
            "つい先週も立て続けにあって。\x01",
            "……どうした事かねえ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6C16")

    SetScenarioFlags(0x95, 1)
    Jump("loc_7231")

    label("loc_6C1E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_6D36")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6CE8")

    #C0314
    ChrTalk(
        0xB,
        (
            "亭主は仕入れで忙しくてねぇ、\x01",
            "中々会えないんだよ……\x02",
        )
    )

    CloseMessageWindow()

    #C0315
    ChrTalk(
        0xB,
        (
            "……おっといけない、\x01",
            "湿っぽいことを言っちゃったね。\x02",
        )
    )

    CloseMessageWindow()

    #C0316
    ChrTalk(
        0xB,
        (
            "はい、自慢のお魚はいかが～？\x01",
            "どれも味は保証するよ～っ！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_6D31")

    label("loc_6CE8")


    #C0317
    ChrTalk(
        0xB,
        (
            "亭主も仕入れに忙しくて\x01",
            "中々会えないんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0318
    ChrTalk(
        0xB,
        "ちょっと寂しいわ。\x02",
    )

    CloseMessageWindow()

    label("loc_6D31")

    Jump("loc_7231")

    label("loc_6D36")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_6E30")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6DE1")

    #C0319
    ChrTalk(
        0xB,
        (
            "そこの通りに釣公師団って\x01",
            "人たちがいるでしょ？\x02",
        )
    )

    CloseMessageWindow()

    #C0320
    ChrTalk(
        0xB,
        (
            "あの人たち、通りがかるたびに\x01",
            "ウチのお魚をじろじろ見ていくのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0321
    ChrTalk(
        0xB,
        "一体何なのかねえ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_6E2B")

    label("loc_6DE1")


    #C0322
    ChrTalk(
        0xB,
        (
            "釣公師団の人たち、\x01",
            "真剣な顔でお魚を見ていくのよ。\x01",
            "一体何なのかねえ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6E2B")

    Jump("loc_7231")

    label("loc_6E30")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_703C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6FCD")

    #C0323
    ChrTalk(
        0xB,
        (
            "赤ジャージの不良たち、\x01",
            "最近は見なくなったねえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0324
    ChrTalk(
        0xB,
        (
            "店前で喧嘩されなくなったのは\x01",
            "嬉しいけど……静かすぎて\x01",
            "逆に心配になっちゃうわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0325
    ChrTalk(
        0xB,
        (
            "みんなして食あたりにでも\x01",
            "なっちゃったのかねえ。\x02",
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
    Sleep(500)

    #C0326
    ChrTalk(
        0x104,
        (
            "#0300F（次に連中が騒ぎ出したら\x01",
            "  この手でいくか？）\x02",
        )
    )

    CloseMessageWindow()

    #C0327
    ChrTalk(
        0x101,
        "#0006F（流石にそれはちょっと……）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_7037")

    label("loc_6FCD")


    #C0328
    ChrTalk(
        0xB,
        (
            "赤ジャージの不良たち、\x01",
            "最近は見なくなったねえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0329
    ChrTalk(
        0xB,
        (
            "みんなして食あたりにでも\x01",
            "なっちゃったのかねえ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7037")

    Jump("loc_7231")

    label("loc_703C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_70CF")

    #C0330
    ChrTalk(
        0xB,
        (
            "最近じゃ輸送トラックの\x01",
            "便数も増えてね。\x01",
            "仕入れが楽になったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0331
    ChrTalk(
        0xB,
        (
            "さあさあ、お一つどうだい？\x01",
            "こっちのは朝の採れたてだよ～っ！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7231")

    label("loc_70CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_7231")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_71E6")

    #C0332
    ChrTalk(
        0xB,
        (
            "お魚はいかが～！\x01",
            "新鮮なお魚だよ～っ！\x02",
        )
    )

    CloseMessageWindow()

    #C0333
    ChrTalk(
        0x103,
        "#0200F……お魚がたくさんです。\x02",
    )

    CloseMessageWindow()

    #C0334
    ChrTalk(
        0x101,
        (
            "#0003Fうーん、見たことの無い\x01",
            "魚ばっかりだな……\x02",
        )
    )

    CloseMessageWindow()

    #C0335
    ChrTalk(
        0xB,
        (
            "ふふ、そっちのは共和国から\x01",
            "塩漬けにして輸送した海魚なのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0336
    ChrTalk(
        0xB,
        (
            "焼いても蒸してもイケるんだ。\x01",
            "どうだい、おひとつ！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_7231")

    label("loc_71E6")


    #C0337
    ChrTalk(
        0xB,
        "お魚はいかが～！\x02",
    )

    CloseMessageWindow()

    #C0338
    ChrTalk(
        0xB,
        (
            "さっき届いたばかり、\x01",
            "新鮮なお魚ばかりだよ～っ！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7231")

    Return()

    # Function_14_6123 end

    def Function_15_7232(): pass

    label("Function_15_7232")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x15E, 0x0)"), scpexpr(EXPR_END)), "loc_7240")
    SetScenarioFlags(0x2, 3)

    label("loc_7240")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x15F, 0x0)"), scpexpr(EXPR_END)), "loc_724E")
    SetScenarioFlags(0x2, 3)

    label("loc_724E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x160, 0x0)"), scpexpr(EXPR_END)), "loc_725C")
    SetScenarioFlags(0x2, 3)

    label("loc_725C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x161, 0x0)"), scpexpr(EXPR_END)), "loc_726A")
    SetScenarioFlags(0x2, 3)

    label("loc_726A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x162, 0x0)"), scpexpr(EXPR_END)), "loc_7278")
    SetScenarioFlags(0x2, 3)

    label("loc_7278")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x163, 0x0)"), scpexpr(EXPR_END)), "loc_7286")
    SetScenarioFlags(0x2, 3)

    label("loc_7286")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x164, 0x0)"), scpexpr(EXPR_END)), "loc_7294")
    SetScenarioFlags(0x2, 3)

    label("loc_7294")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x165, 0x0)"), scpexpr(EXPR_END)), "loc_72A2")
    SetScenarioFlags(0x2, 3)

    label("loc_72A2")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x166, 0x0)"), scpexpr(EXPR_END)), "loc_72B0")
    SetScenarioFlags(0x2, 3)

    label("loc_72B0")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x167, 0x0)"), scpexpr(EXPR_END)), "loc_72BE")
    SetScenarioFlags(0x2, 3)

    label("loc_72BE")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x168, 0x0)"), scpexpr(EXPR_END)), "loc_72CC")
    SetScenarioFlags(0x2, 3)

    label("loc_72CC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x169, 0x0)"), scpexpr(EXPR_END)), "loc_72DA")
    SetScenarioFlags(0x2, 3)

    label("loc_72DA")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16A, 0x0)"), scpexpr(EXPR_END)), "loc_72E8")
    SetScenarioFlags(0x2, 3)

    label("loc_72E8")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16B, 0x0)"), scpexpr(EXPR_END)), "loc_72F6")
    SetScenarioFlags(0x2, 3)

    label("loc_72F6")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16C, 0x0)"), scpexpr(EXPR_END)), "loc_7304")
    SetScenarioFlags(0x2, 3)

    label("loc_7304")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16D, 0x0)"), scpexpr(EXPR_END)), "loc_7312")
    SetScenarioFlags(0x2, 3)

    label("loc_7312")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16E, 0x0)"), scpexpr(EXPR_END)), "loc_7320")
    SetScenarioFlags(0x2, 3)

    label("loc_7320")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16F, 0x0)"), scpexpr(EXPR_END)), "loc_732E")
    SetScenarioFlags(0x2, 3)

    label("loc_732E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x170, 0x0)"), scpexpr(EXPR_END)), "loc_733C")
    SetScenarioFlags(0x2, 3)

    label("loc_733C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x171, 0x0)"), scpexpr(EXPR_END)), "loc_734A")
    SetScenarioFlags(0x2, 3)

    label("loc_734A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x172, 0x0)"), scpexpr(EXPR_END)), "loc_7358")
    SetScenarioFlags(0x2, 3)

    label("loc_7358")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x173, 0x0)"), scpexpr(EXPR_END)), "loc_7366")
    SetScenarioFlags(0x2, 3)

    label("loc_7366")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x174, 0x0)"), scpexpr(EXPR_END)), "loc_7374")
    SetScenarioFlags(0x2, 3)

    label("loc_7374")

    Return()

    # Function_15_7232 end

    def Function_16_7375(): pass

    label("Function_16_7375")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7388")
    MenuCmd(3, 1, 0x0)

    label("loc_7388")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_739B")
    MenuCmd(3, 1, 0x1)

    label("loc_739B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_73AE")
    MenuCmd(3, 1, 0x2)

    label("loc_73AE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_73C1")
    MenuCmd(3, 1, 0x3)

    label("loc_73C1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_73D4")
    MenuCmd(3, 1, 0x4)

    label("loc_73D4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_73E7")
    MenuCmd(3, 1, 0x5)

    label("loc_73E7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_73FA")
    MenuCmd(3, 1, 0x6)

    label("loc_73FA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_740D")
    MenuCmd(3, 1, 0x7)

    label("loc_740D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7420")
    MenuCmd(3, 1, 0x8)

    label("loc_7420")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7433")
    MenuCmd(3, 1, 0x9)

    label("loc_7433")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7446")
    MenuCmd(3, 1, 0xA)

    label("loc_7446")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7459")
    MenuCmd(3, 1, 0xB)

    label("loc_7459")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_746C")
    MenuCmd(3, 1, 0xC)

    label("loc_746C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_747F")
    MenuCmd(3, 1, 0xD)

    label("loc_747F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7492")
    MenuCmd(3, 1, 0xE)

    label("loc_7492")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_74A5")
    MenuCmd(3, 1, 0xF)

    label("loc_74A5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_74B8")
    MenuCmd(3, 1, 0x10)

    label("loc_74B8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x11), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_74CB")
    MenuCmd(3, 1, 0x11)

    label("loc_74CB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x12), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_74DE")
    MenuCmd(3, 1, 0x12)

    label("loc_74DE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x13), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_74F1")
    MenuCmd(3, 1, 0x13)

    label("loc_74F1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7504")
    MenuCmd(3, 1, 0x14)

    label("loc_7504")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x15), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7517")
    MenuCmd(3, 1, 0x15)

    label("loc_7517")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x16), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_752A")
    MenuCmd(3, 1, 0x16)

    label("loc_752A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x17), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_753D")
    MenuCmd(3, 1, 0x17)

    label("loc_753D")

    Return()

    # Function_16_7375 end

    def Function_17_753E(): pass

    label("Function_17_753E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_7612")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_75AF")

    #C0339
    ChrTalk(
        0xFE,
        "あら、もうこんな時間ね。\x02",
    )

    CloseMessageWindow()

    #C0340
    ChrTalk(
        0xFE,
        (
            "露店でお買い物を済ませて\x01",
            "急いで帰らなくっちゃ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_760D")

    label("loc_75AF")


    #C0341
    ChrTalk(
        0xFE,
        (
            "丁度今の時間だと\x01",
            "安売りをやっているはずね。\x02",
        )
    )

    CloseMessageWindow()

    #C0342
    ChrTalk(
        0xFE,
        (
            "さっさと済ませて\x01",
            "急いで帰らなくっちゃ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_760D")

    Jump("loc_827B")

    label("loc_7612")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_76AF")

    #C0343
    ChrTalk(
        0xFE,
        (
            "今日はバス点検があるから\x01",
            "アルモリカ方面のバスは\x01",
            "お昼から運休するんですって。\x02",
        )
    )

    CloseMessageWindow()

    #C0344
    ChrTalk(
        0xFE,
        (
            "アルモリカ村に用事があるなら\x01",
            "早めに行った方がいいわよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_827B")

    label("loc_76AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_77BB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_773E")

    #C0345
    ChrTalk(
        0xFE,
        (
            "商工会の会長さん、\x01",
            "議会の方に呼ばれてるそうね。\x02",
        )
    )

    CloseMessageWindow()

    #C0346
    ChrTalk(
        0xFE,
        (
            "がんばれ～、私達の代表～！\x01",
            "見事予算を勝ち取って頂戴よ～！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_77B6")

    label("loc_773E")


    #C0347
    ChrTalk(
        0xFE,
        (
            "クロスベル商工会の会長は\x01",
            "この東通りの代表みたいなものよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0348
    ChrTalk(
        0xFE,
        (
            "今じゃ市内の商工業全体を\x01",
            "取りまとめているけれどね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_77B6")

    Jump("loc_827B")

    label("loc_77BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_78E7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_788A")

    #C0349
    ChrTalk(
        0xFE,
        (
            "クロスベルタイムズによると\x01",
            "１年後には更に景気がよくなるそうよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0350
    ChrTalk(
        0xFE,
        (
            "景気が良くなるっていうのはね、\x01",
            "つまり主人のお給料が上がるって事。\x02",
        )
    )

    CloseMessageWindow()

    #C0351
    ChrTalk(
        0xFE,
        "これでブランド服も買えるかしら～。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_78E2")

    label("loc_788A")


    #C0352
    ChrTalk(
        0xFE,
        (
            "お給料が上がるほど\x01",
            "嬉しい事はないわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0353
    ChrTalk(
        0xFE,
        (
            "これであの\x01",
            "ブランド服も買えるかしら。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_78E2")

    Jump("loc_827B")

    label("loc_78E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_79E4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7989")

    #C0354
    ChrTalk(
        0xFE,
        (
            "記念祭が終わって\x01",
            "街も静かになったわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0355
    ChrTalk(
        0xFE,
        (
            "マフィア達も随分\x01",
            "大人しくなったんじゃない？\x02",
        )
    )

    CloseMessageWindow()

    #C0356
    ChrTalk(
        0xFE,
        (
            "ここのところ\x01",
            "全く噂を聞かないけど。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_79DF")

    label("loc_7989")


    #C0357
    ChrTalk(
        0xFE,
        (
            "ルバーチェの噂も\x01",
            "さっぱり聞かないわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0358
    ChrTalk(
        0xFE,
        (
            "大人しくなったみたいで\x01",
            "一安心だわ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_79DF")

    Jump("loc_827B")

    label("loc_79E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_7A43")

    #C0359
    ChrTalk(
        0xFE,
        (
            "創立記念祭では\x01",
            "毎年商工会で催し物をやるのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0360
    ChrTalk(
        0xFE,
        "今年は何をするのかしら。\x02",
    )

    CloseMessageWindow()
    Jump("loc_827B")

    label("loc_7A43")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_7AB8")

    #C0361
    ChrTalk(
        0xFE,
        "いよいよ来月は創立記念祭ね。\x02",
    )

    CloseMessageWindow()

    #C0362
    ChrTalk(
        0xFE,
        (
            "やっぱり記念祭は楽しみたいし\x01",
            "今から出費を抑えておかなくちゃね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_827B")

    label("loc_7AB8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_7C05")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7B8E")

    #C0363
    ChrTalk(
        0xFE,
        (
            "７、８年くらい前にも\x01",
            "マフィア同士の撃ち合いが\x01",
            "あったわよねぇ……\x02",
        )
    )

    CloseMessageWindow()

    #C0364
    ChrTalk(
        0xFE,
        (
            "あの時はたしか\x01",
            "ルバーチェの内紛だって\x01",
            "噂されてたっけ。\x02",
        )
    )

    CloseMessageWindow()

    #C0365
    ChrTalk(
        0xFE,
        (
            "ふう、警察も何もしてくれないし\x01",
            "怖いことばかりだわ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_7C00")

    label("loc_7B8E")


    #C0366
    ChrTalk(
        0xFE,
        (
            "最近も倉庫街の辺りで\x01",
            "撃ち合いがあったそうだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0367
    ChrTalk(
        0xFE,
        (
            "また内紛でも始まったのかしら。\x01",
            "本当に怖い話よねぇ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7C00")

    Jump("loc_827B")

    label("loc_7C05")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_7D71")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7CDE")

    #C0368
    ChrTalk(
        0xFE,
        (
            "……ねえ聞いた？\x01",
            "昨晩、倉庫街の方で\x01",
            "発砲事件があったそうよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0369
    ChrTalk(
        0xFE,
        (
            "遊撃士の人も駆けつけたけど\x01",
            "犯人達は早々に逃げちゃったらしいわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0370
    ChrTalk(
        0xFE,
        (
            "まったく……いつになっても\x01",
            "平和にならないわねぇ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_7D69")

    label("loc_7CDE")


    #C0371
    ChrTalk(
        0xFE,
        (
            "なんでも倉庫街の辺りで\x01",
            "発砲事件があったそうじゃない。\x02",
        )
    )

    CloseMessageWindow()

    #C0372
    ChrTalk(
        0xFE,
        (
            "また例の人たちかしら……\x01",
            "……この街はいつになっても\x01",
            "平和にならないわねぇ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7D69")

    SetScenarioFlags(0x95, 1)
    Jump("loc_827B")

    label("loc_7D71")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_7E9B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7E4A")

    #C0373
    ChrTalk(
        0xFE,
        (
            "クロスベルタイムズの記事で\x01",
            "知ったんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0374
    ChrTalk(
        0xFE,
        (
            "ソーニャって名前からして、\x01",
            "警備隊の副司令さんって\x01",
            "女性の方なのね。\x02",
        )
    )

    CloseMessageWindow()

    #C0375
    ChrTalk(
        0xFE,
        (
            "警備隊の車なら時々見かけるけど\x01",
            "ちょっと親近感を持っちゃうわ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_7E96")

    label("loc_7E4A")


    #C0376
    ChrTalk(
        0xFE,
        (
            "警備隊の副司令さんって\x01",
            "女性の方なのね。\x01",
            "ちょっと親近感を持っちゃうわ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7E96")

    Jump("loc_827B")

    label("loc_7E9B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_7FC9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7F6C")

    #C0377
    ChrTalk(
        0xFE,
        (
            "東通りに住んでいると\x01",
            "一通りの物は何でも揃うのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0378
    ChrTalk(
        0xFE,
        (
            "少し歩けば露店があるし\x01",
            "特別な物なら、知り合いの\x01",
            "商人さんに頼めばいいもの。\x02",
        )
    )

    CloseMessageWindow()

    #C0379
    ChrTalk(
        0xFE,
        (
            "この辺りって\x01",
            "実は一番住みやすいのかもね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_7FC4")

    label("loc_7F6C")


    #C0380
    ChrTalk(
        0xFE,
        (
            "東通りに住んでいると\x01",
            "一通りの物は何でも揃うのよ。\x01",
            "実は一番住みやすい所なのかもね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7FC4")

    Jump("loc_827B")

    label("loc_7FC9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_80C3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8062")

    #C0381
    ChrTalk(
        0xFE,
        "あら、アルモリカ村に行くの？\x02",
    )

    CloseMessageWindow()

    #C0382
    ChrTalk(
        0xFE,
        (
            "それならそこの\x01",
            "東の出口から出るといいわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0383
    ChrTalk(
        0xFE,
        (
            "バスに乗れば\x01",
            "割と楽に行き来できるわよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_80BE")

    label("loc_8062")


    #C0384
    ChrTalk(
        0xFE,
        (
            "そこの東の出口から\x01",
            "出るとバス停があるわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0385
    ChrTalk(
        0xFE,
        (
            "バスに乗れば\x01",
            "アルモリカ村まではすぐよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_80BE")

    Jump("loc_827B")

    label("loc_80C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_8143")

    #C0386
    ChrTalk(
        0xFE,
        (
            "また旧市街の方で\x01",
            "騒ぎがあったそうね。\x02",
        )
    )

    CloseMessageWindow()

    #C0387
    ChrTalk(
        0xFE,
        (
            "もう、あそこの不良たちときたら……\x01",
            "警察も何とかできないのかしら。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_827B")

    label("loc_8143")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_827B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_820D")

    #C0388
    ChrTalk(
        0xFE,
        "あら、観光客の人？\x02",
    )

    CloseMessageWindow()

    #C0389
    ChrTalk(
        0xFE,
        (
            "気をつけなさいよ、\x01",
            "この辺りは旧市街に近くって\x01",
            "あまり治安が良くないから。\x02",
        )
    )

    CloseMessageWindow()

    #C0390
    ChrTalk(
        0xFE,
        (
            "困ったら遊撃士協会に行きなさいね。\x01",
            "きっと助けてくれるでしょうから。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_827B")

    label("loc_820D")


    #C0391
    ChrTalk(
        0xFE,
        (
            "この辺りは\x01",
            "治安が良くないのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0392
    ChrTalk(
        0xFE,
        (
            "困ったら遊撃士協会に行きなさいね。\x01",
            "きっと助けてくれるでしょうから。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_827B")

    TalkEnd(0xFE)
    Return()

    # Function_17_753E end

    def Function_18_827F(): pass

    label("Function_18_827F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_83FB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_836E")

    #C0393
    ChrTalk(
        0xFE,
        (
            "ルバーチェの会長といえば\x01",
            "いままで一度も検挙されずに\x01",
            "狡猾に生きてきた男じゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0394
    ChrTalk(
        0xFE,
        (
            "まともに裁かれれば\x01",
            "懲役二百年は固いじゃろうに……\x02",
        )
    )

    CloseMessageWindow()

    #C0395
    ChrTalk(
        0xFE,
        "いつまで経っても捕まらん。\x02",
    )

    CloseMessageWindow()

    #C0396
    ChrTalk(
        0xFE,
        "この世はそう出来ておるのかのう……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_83F6")

    label("loc_836E")


    #C0397
    ChrTalk(
        0xFE,
        (
            "ルバーチェの会長が捕まれば\x01",
            "懲役二百年は固いじゃろうに……\x02",
        )
    )

    CloseMessageWindow()

    #C0398
    ChrTalk(
        0xFE,
        (
            "警察はいまだ検挙できぬままじゃ。\x01",
            "世の中、そう出来ておるのかのう……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_83F6")

    Jump("loc_9432")

    label("loc_83FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_8496")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_846B")

    #C0399
    ChrTalk(
        0xFE,
        (
            "今朝から国際定期便が\x01",
            "止まっておるそうじゃな。\x02",
        )
    )

    CloseMessageWindow()

    #C0400
    ChrTalk(
        0xFE,
        "はて……また事件じゃろうか。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_8491")

    label("loc_846B")


    #C0401
    ChrTalk(
        0xFE,
        "近頃よくわからん事件が多いのう。\x02",
    )

    CloseMessageWindow()

    label("loc_8491")

    Jump("loc_9432")

    label("loc_8496")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_8595")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8559")

    #C0402
    ChrTalk(
        0xFE,
        (
            "昨晩、黒い導力車が\x01",
            "港湾公園の方に\x01",
            "突っ込んでいったそうじゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0403
    ChrTalk(
        0xFE,
        (
            "そういえば夜中に\x01",
            "銃声が何度も音が聞こえたのう。\x02",
        )
    )

    CloseMessageWindow()

    #C0404
    ChrTalk(
        0xFE,
        (
            "ふむ、やはり\x01",
            "ルバーチェの連中じゃろうか……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_8590")

    label("loc_8559")


    #C0405
    ChrTalk(
        0xFE,
        (
            "またルバーチェの連中かの……\x01",
            "やれやれ怖い話じゃ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8590")

    Jump("loc_9432")

    label("loc_8595")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_8734")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_86B9")

    #C0406
    ChrTalk(
        0xFE,
        "まったく、ルバーチェの連中め……\x02",
    )

    CloseMessageWindow()

    #C0407
    ChrTalk(
        0xFE,
        (
            "先日は導力運搬車で\x01",
            "露店街に乗りつけてきおってな。\x02",
        )
    )

    CloseMessageWindow()

    #C0408
    ChrTalk(
        0xFE,
        (
            "辺りを占拠したかと思うと\x01",
            "デカイ態度でみかじめ料を\x01",
            "要求してきおったんじゃ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 1900, 0x2C, 0x2F, 0x96, 0x1)
    Sound(25, 0, 100, 0)
    Sleep(1000)

    #C0409
    ChrTalk(
        0xFE,
        (
            "すぐに遊撃士が追っ払ってくれたが\x01",
            "どうにも腹の立つ話じゃよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_872F")

    label("loc_86B9")


    #C0410
    ChrTalk(
        0xFE,
        (
            "ルバーチェの連中め、\x01",
            "わしら商人が代々引き継いできた\x01",
            "露店街を踏みにじりおって……\x02",
        )
    )

    CloseMessageWindow()

    #C0411
    ChrTalk(
        0xFE,
        "どうにも腹の立つ話じゃよ。\x02",
    )

    CloseMessageWindow()

    label("loc_872F")

    Jump("loc_9432")

    label("loc_8734")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_8876")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_880B")

    #C0412
    ChrTalk(
        0xFE,
        (
            "記念祭からこちら、\x01",
            "クロスベルに居残っておる\x01",
            "観光客も多いそうじゃな。\x02",
        )
    )

    CloseMessageWindow()

    #C0413
    ChrTalk(
        0xFE,
        (
            "中には商売を始めようと\x01",
            "考えておる者もいるようじゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0414
    ChrTalk(
        0xFE,
        (
            "ほっほ、またこの通りに\x01",
            "新米商人が集まりそうじゃな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_8871")

    label("loc_880B")


    #C0415
    ChrTalk(
        0xFE,
        (
            "商人たちが集う場所、\x01",
            "それが東通りじゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0416
    ChrTalk(
        0xFE,
        (
            "ほっほ、人生の先輩として\x01",
            "温かく迎え入れてやるかの。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8871")

    Jump("loc_9432")

    label("loc_8876")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_89C5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8958")

    #C0417
    ChrTalk(
        0xFE,
        (
            "クロイス総裁の娘御も\x01",
            "なかなか優秀だと聞くのう。\x02",
        )
    )

    CloseMessageWindow()

    #C0418
    ChrTalk(
        0xFE,
        (
            "若くしてＩＢＣグループの\x01",
            "取締役の１人に就いておるとか。\x02",
        )
    )

    CloseMessageWindow()

    #C0419
    ChrTalk(
        0xFE,
        (
            "ほっほ、まるで\x01",
            "若い頃の父親そっくりじゃわい。\x02",
        )
    )

    CloseMessageWindow()

    #C0420
    ChrTalk(
        0xFE,
        "いや、それ以上かもしれんな。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_89C0")

    label("loc_8958")


    #C0421
    ChrTalk(
        0xFE,
        (
            "クロイス父娘は\x01",
            "揃いも揃って優秀じゃのう。\x02",
        )
    )

    CloseMessageWindow()

    #C0422
    ChrTalk(
        0xFE,
        (
            "今でも十分大物じゃが、\x01",
            "この先将来も楽しみじゃわい。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_89C0")

    Jump("loc_9432")

    label("loc_89C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_8B4E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8AC6")

    #C0423
    ChrTalk(
        0xFE,
        (
            "ＩＢＣのクロイス総裁は\x01",
            "若くして重役を歴任した\x01",
            "やり手の男じゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0424
    ChrTalk(
        0xFE,
        (
            "当初からずば抜けた\x01",
            "ビジネスセンスを持っておったが、\x01",
            "今や財界の雄まで駆け上りおった。\x02",
        )
    )

    CloseMessageWindow()

    #C0425
    ChrTalk(
        0xFE,
        (
            "それでいて\x01",
            "成功が嫌味にならんのは……\x01",
            "やはりあの人徳のせいかのう。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_8B49")

    label("loc_8AC6")


    #C0426
    ChrTalk(
        0xFE,
        (
            "ＩＢＣのクロイス総裁は\x01",
            "かなりのやり手じゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0427
    ChrTalk(
        0xFE,
        (
            "しかし、ま、人徳のある男でな。\x01",
            "わしら商人の中でも\x01",
            "尊敬する者は多いんじゃよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8B49")

    Jump("loc_9432")

    label("loc_8B4E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_8CCC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8C6A")

    #C0428
    ChrTalk(
        0xFE,
        (
            "近頃、暴力事件だの何だのと\x01",
            "物騒な話を耳にするのう……\x02",
        )
    )

    CloseMessageWindow()

    #C0429
    ChrTalk(
        0xFE,
        (
            "しかし警察の捜査は\x01",
            "イマイチ成果を挙げておらんそうじゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0430
    ChrTalk(
        0xFE,
        (
            "やれやれ、相変わらずじゃな……\x01",
            "やはりいざと言うときは\x01",
            "ギルドが一番頼りになるわい。\x02",
        )
    )

    CloseMessageWindow()

    #C0431
    ChrTalk(
        0x101,
        (
            "#0006F（ううっ、やっぱり\x01",
            "  耳が痛いな……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_8CC7")

    label("loc_8C6A")


    #C0432
    ChrTalk(
        0xFE,
        "警察の捜査はいつもパッとせんのう。\x02",
    )

    CloseMessageWindow()

    #C0433
    ChrTalk(
        0xFE,
        (
            "やはりいざと言うときは\x01",
            "ブレイサーギルドじゃよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8CC7")

    Jump("loc_9432")

    label("loc_8CCC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_8DD7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8D82")

    #C0434
    ChrTalk(
        0xFE,
        (
            "クロスベル商工会では\x01",
            "毎年創立記念祭に\x01",
            "催し物を開くんじゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0435
    ChrTalk(
        0xFE,
        (
            "今年は市民も参加できる\x01",
            "イベントを考えておるそうじゃよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0436
    ChrTalk(
        0xFE,
        "ほっほ、楽しみじゃのう。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_8DD2")

    label("loc_8D82")


    #C0437
    ChrTalk(
        0xFE,
        (
            "クロスベル商工会は\x01",
            "創立記念祭に催し物を開くんじゃ。\x01",
            "今から楽しみじゃのう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8DD2")

    Jump("loc_9432")

    label("loc_8DD7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_8EFF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8E87")

    #C0438
    ChrTalk(
        0xFE,
        (
            "わしも東通りでは\x01",
            "長いこと店を持っておってな。\x02",
        )
    )

    CloseMessageWindow()

    #C0439
    ChrTalk(
        0xFE,
        (
            "商工会の会長にも\x01",
            "よくお世話になったもんじゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0440
    ChrTalk(
        0xFE,
        (
            "ほっほ、昔培った絆は\x01",
            "まさに財産じゃのう。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_8EFA")

    label("loc_8E87")


    #C0441
    ChrTalk(
        0xFE,
        (
            "商工会の会長は\x01",
            "今でも露店街に\x01",
            "顔を出しておるようじゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0442
    ChrTalk(
        0xFE,
        (
            "ほっほ、若い商人達の\x01",
            "様子が気になるんじゃろうな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8EFA")

    Jump("loc_9432")

    label("loc_8EFF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_9061")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8FEC")

    #C0443
    ChrTalk(
        0xFE,
        (
            "ここ３、４年で\x01",
            "導力車も随分と普及したのう。\x02",
        )
    )

    CloseMessageWindow()

    #C0444
    ChrTalk(
        0xFE,
        (
            "共和国からの仕入れにも\x01",
            "導力トラックを使ったりするらしい。\x02",
        )
    )

    CloseMessageWindow()

    #C0445
    ChrTalk(
        0xFE,
        (
            "トラック便は鉄道よりも\x01",
            "融通が効くからのう。\x02",
        )
    )

    CloseMessageWindow()

    #C0446
    ChrTalk(
        0xFE,
        (
            "……お前さんらも\x01",
            "車には気を付けるんじゃよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_905C")

    label("loc_8FEC")


    #C0447
    ChrTalk(
        0xFE,
        (
            "最近ではトラック便を使う\x01",
            "業者も増えておるらしいな。\x02",
        )
    )

    CloseMessageWindow()

    #C0448
    ChrTalk(
        0xFE,
        (
            "わしが商売しておった頃とは\x01",
            "随分様変わりしたわい。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_905C")

    Jump("loc_9432")

    label("loc_9061")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_91C8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_914F")

    #C0449
    ChrTalk(
        0xFE,
        "クロスベルは昔からの貿易都市じゃ。\x02",
    )

    CloseMessageWindow()

    #C0450
    ChrTalk(
        0xFE,
        (
            "東西に伸びる街道は\x01",
            "重要な交易路だったんじゃよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0451
    ChrTalk(
        0xFE,
        (
            "外国の様々な作物や織物、\x01",
            "また人々の口を介して行きかう噂……\x02",
        )
    )

    CloseMessageWindow()

    #C0452
    ChrTalk(
        0xFE,
        (
            "そういった物が\x01",
            "クロスベルを形作ったといえるな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_91C3")

    label("loc_914F")


    #C0453
    ChrTalk(
        0xFE,
        (
            "クロスベルは中世の頃から\x01",
            "貿易都市として発達してきたんじゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0454
    ChrTalk(
        0xFE,
        (
            "今では『文明の十字路』とも\x01",
            "呼ばれるんじゃよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_91C3")

    Jump("loc_9432")

    label("loc_91C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_92CF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9263")

    #C0455
    ChrTalk(
        0xFE,
        (
            "先ほど、例の女記者が\x01",
            "ここを通っていったワイ。\x02",
        )
    )

    CloseMessageWindow()

    #C0456
    ChrTalk(
        0xFE,
        "あの記者もマメじゃのぉ……\x02",
    )

    CloseMessageWindow()

    #C0457
    ChrTalk(
        0xFE,
        (
            "この辺りでは\x01",
            "しょっちゅう見かけるわい。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_92CA")

    label("loc_9263")


    #C0458
    ChrTalk(
        0xFE,
        (
            "あの記者は\x01",
            "よう取材に来ておるんじゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0459
    ChrTalk(
        0xFE,
        (
            "最近は熱心に\x01",
            "遊撃士なんかを\x01",
            "追いかけておるようじゃよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_92CA")

    Jump("loc_9432")

    label("loc_92CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_9432")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_93BE")

    #C0460
    ChrTalk(
        0xFE,
        (
            "おや、見かけん顔じゃ。\x01",
            "東通りは初めてかの？\x02",
        )
    )

    CloseMessageWindow()

    #C0461
    ChrTalk(
        0xFE,
        (
            "この辺りは商売が盛んでな、\x01",
            "外国からの移民も多いんじゃよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0462
    ChrTalk(
        0xFE,
        (
            "ほっほ、昔からのことなのでな、\x01",
            "すっかりよそ者を受け入れる\x01",
            "気風ちゅうもんが出来上がっておるよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_9432")

    label("loc_93BE")


    #C0463
    ChrTalk(
        0xFE,
        (
            "東通りはちぃと騒がしいが、\x01",
            "みなあれで心暖かい連中ばかりじゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0464
    ChrTalk(
        0xFE,
        (
            "慣れんからといって\x01",
            "物怖じすることはないぞ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9432")

    TalkEnd(0xFE)
    Return()

    # Function_18_827F end

    def Function_19_9436(): pass

    label("Function_19_9436")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_95AB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xEE, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_954F")
    OP_4B(0xE, 0xFF)
    OP_4B(0x10, 0xFF)

    #C0465
    ChrTalk(
        0xE,
        (
            "なあメイリ～ン……\x01",
            "オレ、どうするべきかなー……\x02",
        )
    )

    CloseMessageWindow()

    #C0466
    ChrTalk(
        0x10,
        (
            "兄たんは兄たんでいいの。\x01",
            "メイリンと遊んでほしいの。\x02",
        )
    )

    CloseMessageWindow()

    #C0467
    ChrTalk(
        0xE,
        (
            "あはははは……\x01",
            "そっか、そうだよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0468
    ChrTalk(
        0xE,
        (
            "よーし、今日は\x01",
            "手ぇつないで帰るか！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x10, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1500)

    #C0469
    ChrTalk(
        0x10,
        "あい！\x02",
    )

    CloseMessageWindow()
    OP_4C(0xE, 0xFF)
    OP_4C(0x10, 0xFF)
    ClearChrFlags(0xE, 0x10)
    ClearChrFlags(0x10, 0x10)
    SetScenarioFlags(0xEE, 0)
    Jump("loc_95A6")

    label("loc_954F")


    #C0470
    ChrTalk(
        0xFE,
        "やっぱオレ、仕事探そっかな。\x02",
    )

    CloseMessageWindow()

    #C0471
    ChrTalk(
        0xFE,
        (
            "毎日ぼーっとしてるだけってのも\x01",
            "つまんねえしな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_95A6")

    Jump("loc_A1BD")

    label("loc_95AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_967F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9645")

    #C0472
    ChrTalk(
        0xFE,
        (
            "さっきアリオスさんが\x01",
            "ギルドから出ていったぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0473
    ChrTalk(
        0xFE,
        (
            "他の遊撃士の人も\x01",
            "忙しくしてるみたいだし……\x01",
            "遊撃士の人も忙しいよなー。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_967A")

    label("loc_9645")


    #C0474
    ChrTalk(
        0xFE,
        (
            "あー……オレだけ\x01",
            "ダラダラしてていいのかなー……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_967A")

    Jump("loc_A1BD")

    label("loc_967F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_97B8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9737")

    #C0475
    ChrTalk(
        0xFE,
        (
            "今朝爺ちゃんが通りがかってさ、\x01",
            "メイリンから目を離さないようにって\x01",
            "声を掛けてくれたぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0476
    ChrTalk(
        0xFE,
        (
            "ま、なんか事件があったらしいしな。\x01",
            "オレも気をつけとくかー。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_97B3")

    label("loc_9737")


    #C0477
    ChrTalk(
        0xFE,
        (
            "爺ちゃんはクロスベル議事堂に\x01",
            "行ってるみたいだぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0478
    ChrTalk(
        0xFE,
        (
            "議会の参考人に呼ばれてるんだ。\x01",
            "あっちもなんか大変そうだよなー。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_97B3")

    Jump("loc_A1BD")

    label("loc_97B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_98BA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9853")

    #C0479
    ChrTalk(
        0xFE,
        (
            "オレ、記念祭でちょっとだけ\x01",
            "バイトしたんだよなー。\x02",
        )
    )

    CloseMessageWindow()

    #C0480
    ChrTalk(
        0xFE,
        "………………………………\x02",
    )

    CloseMessageWindow()

    #C0481
    ChrTalk(
        0xFE,
        (
            "やっぱオレも\x01",
            "働いた方がいいのかなー。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_98B5")

    label("loc_9853")


    #C0482
    ChrTalk(
        0xFE,
        (
            "ヒマだし働くってのも\x01",
            "悪くない気がするけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0483
    ChrTalk(
        0xFE,
        (
            "ああ～、でもまた\x01",
            "流されてる気がすんな～。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_98B5")

    Jump("loc_A1BD")

    label("loc_98BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_99CB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9993")

    #C0484
    ChrTalk(
        0xFE,
        (
            "くそー、記念祭の後は\x01",
            "片づけまで手伝わされたぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0485
    ChrTalk(
        0xFE,
        (
            "おまけに役員の人が\x01",
            "会長のお孫さんなら才能があるはず、\x01",
            "とかすげー褒めてきてさぁ……\x02",
        )
    )

    CloseMessageWindow()

    #C0486
    ChrTalk(
        0xFE,
        (
            "はあ……結局バイト料まで\x01",
            "渡されちまったぜ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_99C6")

    label("loc_9993")


    #C0487
    ChrTalk(
        0xFE,
        (
            "はあ、オレは商売なんて\x01",
            "全然興味ねえのになー。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_99C6")

    Jump("loc_A1BD")

    label("loc_99CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_9ADD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9A7C")

    #C0488
    ChrTalk(
        0xFE,
        (
            "い、いま親父が\x01",
            "そこの通りを歩いてたんだよ……\x02",
        )
    )

    CloseMessageWindow()

    #C0489
    ChrTalk(
        0xFE,
        (
            "爺ちゃんちに\x01",
            "用事でもあったのかな。\x02",
        )
    )

    CloseMessageWindow()

    #C0490
    ChrTalk(
        0xFE,
        (
            "危ない危ない……\x01",
            "見つかったら\x01",
            "また小言を言われるぜ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_9AD8")

    label("loc_9A7C")


    #C0491
    ChrTalk(
        0xFE,
        (
            "親父は仕事につけって\x01",
            "いつもうるさいんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0492
    ChrTalk(
        0xFE,
        (
            "見つかったら\x01",
            "また小言を言われちまうぜ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9AD8")

    Jump("loc_A1BD")

    label("loc_9ADD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_9C06")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9B9C")

    #C0493
    ChrTalk(
        0xFE,
        (
            "メイリンしつけ計画は\x01",
            "失敗に終わったぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0494
    ChrTalk(
        0xFE,
        "はあ、甘えん坊で困ったもんだ。\x02",
    )

    CloseMessageWindow()

    #C0495
    ChrTalk(
        0xFE,
        (
            "でもこんなに泣きじゃくるなんて……\x01",
            "やっぱ悪いことしちまったかな。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xE, 0x87, 0x0)
    SetChrFlags(0xE, 0x10)
    SetScenarioFlags(0x1, 1)
    Jump("loc_9C01")

    label("loc_9B9C")


    #C0496
    ChrTalk(
        0xFE,
        (
            "その……置いていった\x01",
            "兄ちゃんが悪かった。\x02",
        )
    )

    CloseMessageWindow()

    #C0497
    ChrTalk(
        0xFE,
        (
            "今日はなんでも\x01",
            "奢ってやるからさ。\x01",
            "機嫌直せよ～。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9C01")

    Jump("loc_A1BD")

    label("loc_9C06")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_9D59")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9CDF")

    #C0498
    ChrTalk(
        0xFE,
        (
            "メイリンの奴を\x01",
            "しつけてやろうかと思ってるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0499
    ChrTalk(
        0xFE,
        (
            "毎日オレやお袋にべったりで\x01",
            "ちょっと甘えん坊すぎるからなぁ……\x02",
        )
    )

    CloseMessageWindow()

    #C0500
    ChrTalk(
        0xFE,
        (
            "来年からは日曜学校だし、\x01",
            "もちっとしゃっきり\x01",
            "させてやらないとな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_9D54")

    label("loc_9CDF")


    #C0501
    ChrTalk(
        0xFE,
        (
            "プータローのオレが\x01",
            "言うのもなんだが……\x01",
            "このままじゃ将来苦労するぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0502
    ChrTalk(
        0xFE,
        (
            "兄として少し\x01",
            "しつけてやらないとな……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9D54")

    Jump("loc_A1BD")

    label("loc_9D59")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_9E4D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9DF3")

    #C0503
    ChrTalk(
        0xFE,
        (
            "……メイリンは\x01",
            "少し甘えん坊すぎだよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0504
    ChrTalk(
        0xFE,
        (
            "来年からは日曜学校なんだ。\x01",
            "もちっとしっかりしないと\x01",
            "苦労するんじゃねえかな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_9E48")

    label("loc_9DF3")


    #C0505
    ChrTalk(
        0xFE,
        "メイリンは甘えん坊なんだ。\x02",
    )

    CloseMessageWindow()

    #C0506
    ChrTalk(
        0xFE,
        (
            "もちっとしっかりしないと\x01",
            "将来きっと苦労するぜ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9E48")

    Jump("loc_A1BD")

    label("loc_9E4D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_9F64")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9EFF")

    #C0507
    ChrTalk(
        0xFE,
        (
            "親父もお袋も\x01",
            "仕事につけってうるさいんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0508
    ChrTalk(
        0xFE,
        (
            "ちぇっ、少しくらい\x01",
            "自由にさせてくれてもいいのにな。\x02",
        )
    )

    CloseMessageWindow()

    #C0509
    ChrTalk(
        0xFE,
        (
            "オレだって\x01",
            "働きたくなったら働くっての。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_9F5F")

    label("loc_9EFF")


    #C0510
    ChrTalk(
        0xFE,
        (
            "親父もお袋もうるさくて\x01",
            "家には居づらいぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0511
    ChrTalk(
        0xFE,
        (
            "ちぇっ、自由に\x01",
            "させてくれてもいいのになぁ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9F5F")

    Jump("loc_A1BD")

    label("loc_9F64")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_9FB0")

    #C0512
    ChrTalk(
        0xFE,
        "あー、腹へったなー。\x02",
    )

    CloseMessageWindow()

    #C0513
    ChrTalk(
        0xFE,
        "今日は龍老飯店で食うとするか。\x02",
    )

    CloseMessageWindow()
    Jump("loc_A1BD")

    label("loc_9FB0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_A0B5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A074")

    #C0514
    ChrTalk(
        0xFE,
        (
            "うちの家系ってさ、\x01",
            "代々商売人なんだよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0515
    ChrTalk(
        0xFE,
        (
            "親父は貿易会社をやってるし\x01",
            "爺ちゃんは商工会の会長なんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0516
    ChrTalk(
        0xFE,
        (
            "でもな～、オレはそういうのに\x01",
            "興味持てないんだよな～。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_A0B0")

    label("loc_A074")


    #C0517
    ChrTalk(
        0xFE,
        "あー、だるいな～……\x02",
    )

    CloseMessageWindow()

    #C0518
    ChrTalk(
        0xFE,
        "今日も適当に時間を潰すか～。\x02",
    )

    CloseMessageWindow()

    label("loc_A0B0")

    Jump("loc_A1BD")

    label("loc_A0B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_A15D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A13C")

    #C0519
    ChrTalk(
        0xFE,
        "あー、それにしても暇だな～。\x02",
    )

    CloseMessageWindow()

    #C0520
    ChrTalk(
        0xFE,
        (
            "オトナに指示されんのは\x01",
            "嫌なんだけど、\x01",
            "１人でいるのも暇なんだよな～。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_A158")

    label("loc_A13C")


    #C0521
    ChrTalk(
        0xFE,
        "あー、なんか暇だな～。\x02",
    )

    CloseMessageWindow()

    label("loc_A158")

    Jump("loc_A1BD")

    label("loc_A15D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_A1BD")

    #C0522
    ChrTalk(
        0xFE,
        (
            "親父もお袋も\x01",
            "妹の世話を押し付けやがって……\x02",
        )
    )

    CloseMessageWindow()

    #C0523
    ChrTalk(
        0xFE,
        "ちぇっ、１人にさせてくれよな～。\x02",
    )

    CloseMessageWindow()

    label("loc_A1BD")

    TalkEnd(0xFE)
    Return()

    # Function_19_9436 end

    def Function_20_A1C1(): pass

    label("Function_20_A1C1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_A20B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xEE, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A1DF")
    Call(0, 19)
    Jump("loc_A206")

    label("loc_A1DF")


    #C0524
    ChrTalk(
        0xFE,
        (
            "兄たん、げんきに\x01",
            "なってくれたの！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A206")

    Jump("loc_A9A8")

    label("loc_A20B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_A288")

    #C0525
    ChrTalk(
        0xFE,
        (
            "兄たん、さいきん\x01",
            "とおりがかる人を\x01",
            "ジロジロみてるの。\x02",
        )
    )

    CloseMessageWindow()

    #C0526
    ChrTalk(
        0xFE,
        (
            "兄たん、いつもとちがうの……\x01",
            "どうしたのかなー。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A9A8")

    label("loc_A288")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_A362")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A330")

    #C0527
    ChrTalk(
        0xFE,
        (
            "きょうね、兄たんが\x01",
            "そばにいるようにっていったの。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1200)

    #C0528
    ChrTalk(
        0xFE,
        "わーい……！\x02",
    )

    CloseMessageWindow()

    #C0529
    ChrTalk(
        0xFE,
        (
            "メイリン、ずっと\x01",
            "兄たんといっしょなのー！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_A35D")

    label("loc_A330")


    #C0530
    ChrTalk(
        0xFE,
        (
            "メイリン、兄たんと\x01",
            "たくさんあそぶのー！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A35D")

    Jump("loc_A9A8")

    label("loc_A362")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_A47C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A427")
    OP_4B(0xE, 0xFF)

    #C0531
    ChrTalk(
        0xFE,
        "兄たん、あのねー！\x02",
    )

    CloseMessageWindow()

    #C0532
    ChrTalk(
        0xFE,
        (
            "きょうのあさ\x01",
            "おっきなお犬をみたのー！\x02",
        )
    )

    CloseMessageWindow()

    #C0533
    ChrTalk(
        0xFE,
        (
            "白くってねー、\x01",
            "こーんなおおきくてねー！\x02",
        )
    )

    CloseMessageWindow()

    #C0534
    ChrTalk(
        0xE,
        (
            "ふーん、そっか～。\x01",
            "そりゃよかったなぁ。\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xE, 0xFF)
    ClearChrFlags(0x10, 0x10)
    SetScenarioFlags(0x1, 2)
    Jump("loc_A477")

    label("loc_A427")


    #C0535
    ChrTalk(
        0xFE,
        (
            "兄たん、さいきん\x01",
            "ぼぉっとしてるの。\x02",
        )
    )

    CloseMessageWindow()

    #C0536
    ChrTalk(
        0xFE,
        (
            "メイリンの話\x01",
            "きいてくれないの……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A477")

    Jump("loc_A9A8")

    label("loc_A47C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_A4DD")

    #C0537
    ChrTalk(
        0xFE,
        "きねんさい、たのちかたねー！\x02",
    )

    CloseMessageWindow()

    #C0538
    ChrTalk(
        0xFE,
        (
            "メイリン、兄たんと\x01",
            "２人でお店したんだよー。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A9A8")

    label("loc_A4DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_A52E")

    #C0539
    ChrTalk(
        0xFE,
        "兄たん……どこいくの？\x02",
    )

    CloseMessageWindow()

    #C0540
    ChrTalk(
        0xFE,
        (
            "メイリンを\x01",
            "おいていかないでっ！！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A9A8")

    label("loc_A52E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_A591")

    #C0541
    ChrTalk(
        0xFE,
        "兄たん、おいてかないで～！\x02",
    )

    CloseMessageWindow()

    #C0542
    ChrTalk(
        0xFE,
        (
            "兄たんといるようにって、\x01",
            "ママ、言ってたのっ！！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A9A8")

    label("loc_A591")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_A604")

    #C0543
    ChrTalk(
        0xFE,
        "たらんらんらん……♪\x02",
    )

    CloseMessageWindow()

    #C0544
    ChrTalk(
        0xFE,
        "今日も兄たんと遊ぶのー。\x02",
    )

    CloseMessageWindow()

    #C0545
    ChrTalk(
        0xFE,
        (
            "兄たん、たくさん\x01",
            "遊んでくれるんだよー！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A9A8")

    label("loc_A604")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_A65E")

    #C0546
    ChrTalk(
        0xFE,
        (
            "兄たんにおかし\x01",
            "買ってもらったのー。\x02",
        )
    )

    CloseMessageWindow()

    #C0547
    ChrTalk(
        0xFE,
        (
            "もぐもぐ……\x01",
            "んー、おいしー！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A9A8")

    label("loc_A65E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_A6C9")

    #C0548
    ChrTalk(
        0xFE,
        (
            "兄たんねー、きょうもパパに\x01",
            "いろいろ言われちゃったの。\x02",
        )
    )

    CloseMessageWindow()

    #C0549
    ChrTalk(
        0xFE,
        "……兄たん、げんきだすのー！\x02",
    )

    CloseMessageWindow()
    Jump("loc_A9A8")

    label("loc_A6C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_A73B")

    #C0550
    ChrTalk(
        0xFE,
        (
            "兄たんはねー、\x01",
            "お商売したくないんだって～。\x02",
        )
    )

    CloseMessageWindow()

    #C0551
    ChrTalk(
        0xFE,
        (
            "今はじんせーの\x01",
            "じゅーでんきかんなんだってー。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A9A8")

    label("loc_A73B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_A82F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A7DC")

    #C0552
    ChrTalk(
        0xFE,
        "パパはね、えらい人なんだよー。\x02",
    )

    CloseMessageWindow()

    #C0553
    ChrTalk(
        0xFE,
        (
            "おっきなぼーえき会社の\x01",
            "しゃちょーさんなのー。\x02",
        )
    )

    CloseMessageWindow()

    #C0554
    ChrTalk(
        0xFE,
        (
            "でも……兄たんは\x01",
            "パパのことキライなの……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_A82A")

    label("loc_A7DC")


    #C0555
    ChrTalk(
        0xFE,
        (
            "兄たんは\x01",
            "パパのことキライなの……\x02",
        )
    )

    CloseMessageWindow()

    #C0556
    ChrTalk(
        0xFE,
        (
            "くすん……\x01",
            "メイリンかなしいの……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A82A")

    Jump("loc_A9A8")

    label("loc_A82F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_A8C7")

    #C0557
    ChrTalk(
        0xFE,
        "たらんたらん……♪\x02",
    )

    CloseMessageWindow()

    #C0558
    ChrTalk(
        0xFE,
        (
            "そこの赤いおうち、\x01",
            "ゆーげきしきょーかいなんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0559
    ChrTalk(
        0xFE,
        (
            "よくゆーげきしさんがきてね、\x01",
            "あいさつしてくれるのー。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A9A8")

    label("loc_A8C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_A9A8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A981")
    OP_4B(0xE, 0xFF)

    #C0560
    ChrTalk(
        0xE,
        "いいかメイリン、よく聞けよ～。\x02",
    )

    CloseMessageWindow()

    #C0561
    ChrTalk(
        0xE,
        (
            "兄ちゃんは今日は\x01",
            "ぼーっとしたい気分なんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0562
    ChrTalk(
        0xE,
        (
            "ついてくるのはいいけど\x01",
            "ワガママは言うなよ？\x02",
        )
    )

    CloseMessageWindow()

    #C0563
    ChrTalk(
        0xFE,
        "あい！\x02",
    )

    CloseMessageWindow()
    OP_4C(0xE, 0xFF)
    ClearChrFlags(0x10, 0x10)
    SetScenarioFlags(0x1, 2)
    Jump("loc_A9A8")

    label("loc_A981")


    #C0564
    ChrTalk(
        0xFE,
        (
            "兄たんとおでかけ、\x01",
            "たのしいな～♪\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A9A8")

    TalkEnd(0xFE)
    Return()

    # Function_20_A1C1 end

    def Function_21_A9AC(): pass

    label("Function_21_A9AC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_A9BD")
    Jump("loc_B3FD")

    label("loc_A9BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_AAF3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AA92")

    #C0565
    ChrTalk(
        0xFE,
        (
            "昨日はせっかく\x01",
            "晩御飯を作ったってのに……\x02",
        )
    )

    CloseMessageWindow()

    #C0566
    ChrTalk(
        0xFE,
        (
            "うちの男ども、夜中になるまで\x01",
            "帰ってこなかったのよ！\x02",
        )
    )

    CloseMessageWindow()

    #C0567
    ChrTalk(
        0xFE,
        (
            "現場主任が居なくなったとか\x01",
            "言い訳してたけど、\x01",
            "そんなの理由になるもんですか！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    Jump("loc_AAEE")

    label("loc_AA92")


    #C0568
    ChrTalk(
        0xFE,
        (
            "……もう怒った！\x01",
            "もう絶対家事をしないから！\x02",
        )
    )

    CloseMessageWindow()

    #C0569
    ChrTalk(
        0xFE,
        (
            "これからは全部\x01",
            "男どもにやらせるから！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AAEE")

    Jump("loc_B3FD")

    label("loc_AAF3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_AB8D")

    #C0570
    ChrTalk(
        0xFE,
        "ウチの男どもときたら……\x02",
    )

    CloseMessageWindow()

    #C0571
    ChrTalk(
        0xFE,
        (
            "昨日は一斉に帰ってきて\x01",
            "食事はまだかって急かすのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0572
    ChrTalk(
        0xFE,
        (
            "もう、ブーイングの時だけ\x01",
            "息ピッタリなんだから！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B3FD")

    label("loc_AB8D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_AC3B")

    #C0573
    ChrTalk(
        0xFE,
        (
            "なんでも……\x01",
            "アリオス・マクレインは\x01",
            "長期出張に行ってるそうじゃない。\x02",
        )
    )

    CloseMessageWindow()

    #C0574
    ChrTalk(
        0xFE,
        (
            "あの人がいないと\x01",
            "ちょっと不安よねえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0575
    ChrTalk(
        0xFE,
        (
            "なるべく自治州に\x01",
            "居て欲しいものだわ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B3FD")

    label("loc_AC3B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_AD08")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_ACD2")

    #C0576
    ChrTalk(
        0xFE,
        (
            "うちの男ども、今日は\x01",
            "家でゴロゴロしているわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0577
    ChrTalk(
        0xFE,
        "仕事が休みなんですって。\x02",
    )

    CloseMessageWindow()

    #C0578
    ChrTalk(
        0xFE,
        (
            "主婦は休みが無いっての。\x01",
            "まったく……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    Jump("loc_AD03")

    label("loc_ACD2")


    #C0579
    ChrTalk(
        0xFE,
        (
            "休みなら休みで\x01",
            "家事を手伝ってほしいものね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AD03")

    Jump("loc_B3FD")

    label("loc_AD08")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_ADB9")

    #C0580
    ChrTalk(
        0xFE,
        (
            "あら、もうお昼……？\x01",
            "帰って洗い物を\x01",
            "しなくちゃいけないわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0581
    ChrTalk(
        0xFE,
        (
            "お掃除、洗濯、料理に買い物……\x01",
            "まったく毎日毎日忙しいわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0582
    ChrTalk(
        0xFE,
        "誰か手伝ってくれないかしら。\x02",
    )

    CloseMessageWindow()
    Jump("loc_B3FD")

    label("loc_ADB9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_AEA0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AE59")

    #C0583
    ChrTalk(
        0xFE,
        (
            "ウチの男どもは\x01",
            "建設現場で働いているのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0584
    ChrTalk(
        0xFE,
        (
            "最近仕事がハードだって\x01",
            "文句ばかり言っているけど……\x01",
            "家じゃダラけてばかりなのよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    Jump("loc_AE9B")

    label("loc_AE59")


    #C0585
    ChrTalk(
        0xFE,
        (
            "毎日山ほど\x01",
            "家事をこなしてる私の方が\x01",
            "きっとハードワークだわ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AE9B")

    Jump("loc_B3FD")

    label("loc_AEA0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_AEF9")

    #C0586
    ChrTalk(
        0xFE,
        (
            "あら、なんだか\x01",
            "お魚の品揃えが悪いわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0587
    ChrTalk(
        0xFE,
        "どうしちゃったのかしら。\x02",
    )

    CloseMessageWindow()
    Jump("loc_B3FD")

    label("loc_AEF9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_B015")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AFC0")

    #C0588
    ChrTalk(
        0xFE,
        (
            "アルカンシェルのチケット、\x01",
            "もう売り切れちゃったんですって？\x02",
        )
    )

    CloseMessageWindow()

    #C0589
    ChrTalk(
        0xFE,
        (
            "くぅ～、私だって\x01",
            "家事さえなければ\x01",
            "買いに行きたかったのに……\x02",
        )
    )

    CloseMessageWindow()

    #C0590
    ChrTalk(
        0xFE,
        (
            "うちの家族には\x01",
            "まったく腹が立つわ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    Jump("loc_B010")

    label("loc_AFC0")


    #C0591
    ChrTalk(
        0xFE,
        (
            "うちの男どもが家事を\x01",
            "手伝ってくれればよかったのに……\x01",
            "まったく腹が立つわ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B010")

    Jump("loc_B3FD")

    label("loc_B015")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_B0D4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B098")

    #C0592
    ChrTalk(
        0xFE,
        (
            "さてと、帰ったら\x01",
            "山ほど溜まってる洗濯物を\x01",
            "片付けなくっちゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0593
    ChrTalk(
        0xFE,
        "家族が多いと色々と大変なのよね。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    Jump("loc_B0CF")

    label("loc_B098")


    #C0594
    ChrTalk(
        0xFE,
        (
            "はあ、うちの男どもも\x01",
            "手伝ってくれればいいのに……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B0CF")

    Jump("loc_B3FD")

    label("loc_B0D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_B16F")

    #C0595
    ChrTalk(
        0xFE,
        (
            "露店のいい所は\x01",
            "お店の人とお喋りできる事よね。\x02",
        )
    )

    CloseMessageWindow()

    #C0596
    ChrTalk(
        0xFE,
        (
            "ここのおばさんは\x01",
            "魚の楽な捌き方を教えてくれるのよ。\x01",
            "時間がないときは助かっちゃうわ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B3FD")

    label("loc_B16F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_B284")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B21B")

    #C0597
    ChrTalk(
        0xFE,
        (
            "うちには大きな男が\x01",
            "５人もいるのよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0598
    ChrTalk(
        0xFE,
        (
            "図体ばかりでかくて\x01",
            "役に立ちゃしないんだから。\x02",
        )
    )

    CloseMessageWindow()

    #C0599
    ChrTalk(
        0xFE,
        (
            "せめて家事を手伝って\x01",
            "くれりゃあいいんだけど。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    Jump("loc_B27F")

    label("loc_B21B")


    #C0600
    ChrTalk(
        0xFE,
        (
            "うちには図体ばかり\x01",
            "でかい男が５人もいるのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0601
    ChrTalk(
        0xFE,
        (
            "まったく……どうして\x01",
            "男ばかりなのかしらね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B27F")

    Jump("loc_B3FD")

    label("loc_B284")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_B382")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B319")

    #C0602
    ChrTalk(
        0xFE,
        (
            "ニンジン８個に玉葱１２玉、\x01",
            "サモーナは１５匹で……\x02",
        )
    )

    CloseMessageWindow()

    #C0603
    ChrTalk(
        0xFE,
        (
            "えーっと、それからそれから……\x01",
            "何を買いに来たんだったかしら。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    Jump("loc_B37D")

    label("loc_B319")


    #C0604
    ChrTalk(
        0xFE,
        (
            "露店を回っていると\x01",
            "ついつい忘れちゃうのよねえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0605
    ChrTalk(
        0xFE,
        (
            "えーっと、何を買いに\x01",
            "来たんだったかしら。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B37D")

    Jump("loc_B3FD")

    label("loc_B382")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_B3FD")

    #C0606
    ChrTalk(
        0xFE,
        "えーっと、お魚お魚……\x02",
    )

    CloseMessageWindow()

    #C0607
    ChrTalk(
        0xFE,
        (
            "うちの男どもは\x01",
            "みんな大食いなのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0608
    ChrTalk(
        0xFE,
        (
            "やれやれ、食事を\x01",
            "用意するのも大変だわ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B3FD")

    TalkEnd(0xFE)
    Return()

    # Function_21_A9AC end

    def Function_22_B401(): pass

    label("Function_22_B401")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_B4AF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B47E")

    #C0609
    ChrTalk(
        0xFE,
        (
            "母ちゃんが面倒だっていうから\x01",
            "代わりに買い物に来たんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0610
    ChrTalk(
        0xFE,
        "母ちゃんは家でダラケてるぜ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_B4AF")

    label("loc_B47E")


    #C0611
    ChrTalk(
        0xFE,
        (
            "うちの母ちゃん、\x01",
            "面倒くさがりなんだよなぁ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B4AF")

    TalkEnd(0xFE)
    Return()

    # Function_22_B401 end

    def Function_23_B4B3(): pass

    label("Function_23_B4B3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_B591")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B52A")

    #C0612
    ChrTalk(
        0xFE,
        (
            "一番安い買い物ルートを\x01",
            "見つけたと思ったのに……\x02",
        )
    )

    CloseMessageWindow()

    #C0613
    ChrTalk(
        0xFE,
        "世の中判らないことばかりだね。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 5)
    Jump("loc_B58C")

    label("loc_B52A")


    #C0614
    ChrTalk(
        0xFE,
        (
            "もうお買い物は\x01",
            "カンペキだと思ったのになぁ……\x02",
        )
    )

    CloseMessageWindow()

    #C0615
    ChrTalk(
        0xFE,
        (
            "また一からお店のくせを\x01",
            "覚える事にするよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B58C")

    Jump("loc_C0C4")

    label("loc_B591")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_B687")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B615")

    #C0616
    ChrTalk(
        0xFE,
        (
            "あれ、なんだか\x01",
            "お野菜が値上がりしている……\x02",
        )
    )

    CloseMessageWindow()

    #C0617
    ChrTalk(
        0xFE,
        "なんでだろ。\x02",
    )

    CloseMessageWindow()

    #C0618
    ChrTalk(
        0xFE,
        "こんなはずはないんだけどなぁ……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 5)
    Jump("loc_B682")

    label("loc_B615")


    #C0619
    ChrTalk(
        0xFE,
        (
            "なんだかお野菜が\x01",
            "値上がりしてるんだ……\x01",
            "それにお魚も……\x02",
        )
    )

    CloseMessageWindow()

    #C0620
    ChrTalk(
        0xFE,
        (
            "おかしいな、\x01",
            "こんなはずはないんだけど……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B682")

    Jump("loc_C0C4")

    label("loc_B687")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_B7E3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B751")

    #C0621
    ChrTalk(
        0xFE,
        (
            "最近ようやく一番安い\x01",
            "買い物ルートを見つけたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0622
    ChrTalk(
        0xFE,
        (
            "これも毎日お買い物して\x01",
            "お店のくせを覚えちゃったお陰だよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0623
    ChrTalk(
        0xFE,
        (
            "ふふ……一番安いお買い物。\x01",
            "なんだか気持ちがいいな♪\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 5)
    Jump("loc_B7DE")

    label("loc_B751")


    #C0624
    ChrTalk(
        0xFE,
        (
            "お店のくせを全部覚えて\x01",
            "一番安い買い物ルートを見つけたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0625
    ChrTalk(
        0xFE,
        (
            "ふう……難しい算術の問題が\x01",
            "解けたキブンだよ。\x01",
            "なんだか気持ちがいいや。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B7DE")

    Jump("loc_C0C4")

    label("loc_B7E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_B7F1")
    Jump("loc_C0C4")

    label("loc_B7F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_B8F7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B89A")

    #C0626
    ChrTalk(
        0xFE,
        (
            "記念祭が５日間もあって\x01",
            "すっかり忘れてたよ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1200)

    #C0627
    ChrTalk(
        0xFE,
        "日曜学校の宿題をやらなくちゃ。\x02",
    )

    CloseMessageWindow()

    #C0628
    ChrTalk(
        0xFE,
        "シスターに怒られちゃう。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 5)
    Jump("loc_B8F2")

    label("loc_B89A")


    #C0629
    ChrTalk(
        0xFE,
        (
            "記念祭の前に\x01",
            "たくさん宿題が出たんだよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0630
    ChrTalk(
        0xFE,
        (
            "家に帰ったら\x01",
            "大急ぎでやらなくちゃ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B8F2")

    Jump("loc_C0C4")

    label("loc_B8F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_BA36")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B9C3")

    #C0631
    ChrTalk(
        0xFE,
        (
            "クロスベル商工会の会長さんは\x01",
            "市長とも面識のある偉い人なんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0632
    ChrTalk(
        0xFE,
        (
            "でも、まとめ役なだけで\x01",
            "元々は普通の露店商さんなんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0633
    ChrTalk(
        0xFE,
        (
            "僕にも挨拶してくれる\x01",
            "気のいいお爺さんだよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 5)
    Jump("loc_BA31")

    label("loc_B9C3")


    #C0634
    ChrTalk(
        0xFE,
        (
            "クロスベル商工会の会長さんは\x01",
            "気のいいお爺さんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0635
    ChrTalk(
        0xFE,
        (
            "さっきも通りがかって\x01",
            "かるく挨拶してくれたんだ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BA31")

    Jump("loc_C0C4")

    label("loc_BA36")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_BAE3")

    #C0636
    ChrTalk(
        0xFE,
        (
            "今日は思ったより安く\x01",
            "買い物ができたんだ♪\x02",
        )
    )

    CloseMessageWindow()

    #C0637
    ChrTalk(
        0xFE,
        (
            "……でも、ここで気を緩めると\x01",
            "つい余計な物を買っちゃうんだよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0638
    ChrTalk(
        0xFE,
        (
            "お小遣いとして\x01",
            "きちんと貯金しないと。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C0C4")

    label("loc_BAE3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_BB63")

    #C0639
    ChrTalk(
        0xFE,
        (
            "そこのお店のクロンクさん、\x01",
            "いつも手に包帯してるよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0640
    ChrTalk(
        0xFE,
        (
            "……大丈夫なのかな。\x01",
            "ちょっと心配になっちゃうよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C0C4")

    label("loc_BB63")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_BC7B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BC2B")

    #C0641
    ChrTalk(
        0xFE,
        (
            "ママはお買い物リストと一緒に\x01",
            "ミラを多めに渡してくれるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0642
    ChrTalk(
        0xFE,
        (
            "だから節約すると\x01",
            "手元にお小遣いが残るってわけ。\x02",
        )
    )

    CloseMessageWindow()

    #C0643
    ChrTalk(
        0xFE,
        (
            "……今日もがんばって\x01",
            "一番安い買い物をしないとね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 5)
    Jump("loc_BC76")

    label("loc_BC2B")


    #C0644
    ChrTalk(
        0xFE,
        (
            "うーん、お魚は\x01",
            "日によって値段が変わるんだよね……\x02",
        )
    )

    CloseMessageWindow()

    #C0645
    ChrTalk(
        0xFE,
        "難しいなぁ……\x02",
    )

    CloseMessageWindow()

    label("loc_BC76")

    Jump("loc_C0C4")

    label("loc_BC7B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_BCD4")

    #C0646
    ChrTalk(
        0xFE,
        "あ、今日は日曜学校の日だ。\x02",
    )

    CloseMessageWindow()

    #C0647
    ChrTalk(
        0xFE,
        (
            "お買い物を済ませたら\x01",
            "急がなくっちゃ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C0C4")

    label("loc_BCD4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_BDE3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BDA5")

    #C0648
    ChrTalk(
        0xFE,
        (
            "この時間帯なら\x01",
            "フレッシュ・ディンズの\x01",
            "纏め買いが一番安いかな。\x02",
        )
    )

    CloseMessageWindow()

    #C0649
    ChrTalk(
        0xFE,
        (
            "うーん、でも\x01",
            "お野菜は鮮度が大切だし……\x01",
            "纏め買いはしたくないかも……\x02",
        )
    )

    CloseMessageWindow()

    #C0650
    ChrTalk(
        0xFE,
        "他のお店も回ってから考えようかな。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 5)
    Jump("loc_BDDE")

    label("loc_BDA5")


    #C0651
    ChrTalk(
        0xFE,
        (
            "一番安く買い物しようと思うと\x01",
            "色々大変なんだよね……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BDDE")

    Jump("loc_C0C4")

    label("loc_BDE3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_BF07")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BE9A")

    #C0652
    ChrTalk(
        0xFE,
        (
            "今朝、遊撃士の人が\x01",
            "露店を見に来ていたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0653
    ChrTalk(
        0xFE,
        "……遊撃士の人って忙しそうだよね。\x02",
    )

    CloseMessageWindow()

    #C0654
    ChrTalk(
        0xFE,
        (
            "この通りでトラブルがあると\x01",
            "みんなギルド支部に駆け込むもんね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 5)
    Jump("loc_BF02")

    label("loc_BE9A")


    #C0655
    ChrTalk(
        0xFE,
        (
            "でも、今朝の遊撃士さんは\x01",
            "のんびりしてたなぁ……\x02",
        )
    )

    CloseMessageWindow()

    #C0656
    ChrTalk(
        0xFE,
        (
            "ディンズさんのお店で\x01",
            "お野菜を買っていったよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BF02")

    Jump("loc_C0C4")

    label("loc_BF07")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_BFDF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BFA7")

    #C0657
    ChrTalk(
        0xFE,
        (
            "安売りしてると、つい\x01",
            "たくさん買っちゃうんだよね。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0658
    ChrTalk(
        0xFE,
        (
            "安上がりのつもりだったのに\x01",
            "……どうしてだろ？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 5)
    Jump("loc_BFDA")

    label("loc_BFA7")


    #C0659
    ChrTalk(
        0xFE,
        (
            "お商売は奥が深いね。\x01",
            "お買い物も楽じゃないよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BFDA")

    Jump("loc_C0C4")

    label("loc_BFDF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_C0C4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C05E")

    #C0660
    ChrTalk(
        0xFE,
        (
            "うーん、こっちの\x01",
            "お店の方が少しだけ安い……\x02",
        )
    )

    CloseMessageWindow()

    #C0661
    ChrTalk(
        0xFE,
        (
            "いやいや、あっちの\x01",
            "お店は値切りがきくから……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 5)
    Jump("loc_C0C4")

    label("loc_C05E")


    #C0662
    ChrTalk(
        0xFE,
        (
            "ここの青果店は夕方に\x01",
            "タイムセールをするんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0663
    ChrTalk(
        0xFE,
        (
            "やっぱりもう少し待ってから\x01",
            "買いにこようかな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C0C4")

    TalkEnd(0xFE)
    Return()

    # Function_23_B4B3 end

    def Function_24_C0C8(): pass

    label("Function_24_C0C8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_C12A")

    #C0664
    ChrTalk(
        0xFE,
        (
            "あれ、鉄橋のあちら側が\x01",
            "騒がしかったみたいだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0665
    ChrTalk(
        0xFE,
        "何かあったのかな。\x02",
    )

    CloseMessageWindow()
    Jump("loc_C231")

    label("loc_C12A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_C231")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C1C2")

    #C0666
    ChrTalk(
        0xFE,
        (
            "旅先で困ったときは\x01",
            "やっぱり遊撃士協会だよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0667
    ChrTalk(
        0xFE,
        (
            "いつ何時、どの国にいても\x01",
            "市民の味方をしてくれるんだ。\x01",
            "実に心強いよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 6)
    Jump("loc_C231")

    label("loc_C1C2")


    #C0668
    ChrTalk(
        0xFE,
        (
            "旅先で困ったときは\x01",
            "やはり遊撃士協会だよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0669
    ChrTalk(
        0xFE,
        (
            "特にクロスベルには\x01",
            "優秀な遊撃士が多いと聞くし\x01",
            "心強いよね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C231")

    TalkEnd(0xFE)
    Return()

    # Function_24_C0C8 end

    def Function_25_C235(): pass

    label("Function_25_C235")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_C328")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B0(0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C254")
    Call(0, 26)
    Jump("loc_C328")

    label("loc_C254")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C2C9")

    #C0670
    ChrTalk(
        0xFE,
        "いらっしゃいませ～……\x02",
    )

    CloseMessageWindow()

    #C0671
    ChrTalk(
        0xFE,
        (
            "お願いだから寄って行ってくれ。\x01",
            "でないとマスターにどやされるんだ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 7)
    Jump("loc_C328")

    label("loc_C2C9")


    #C0672
    ChrTalk(
        0xFE,
        "ここのマスター、怖いんだよなぁ。\x02",
    )

    CloseMessageWindow()

    #C0673
    ChrTalk(
        0xFE,
        (
            "ううっ、バイトするにも\x01",
            "別の店を探せばよかったぜ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C328")

    TalkEnd(0xFE)
    Return()

    # Function_25_C235 end

    def Function_26_C32C(): pass

    label("Function_26_C32C")


    #C0674
    ChrTalk(
        0xFE,
        (
            "ここでバイトしているときに\x01",
            "うまいマーボー豆腐の\x01",
            "レシピを思いついたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0675
    ChrTalk(
        0xFE,
        "あんたら、俺の話を聞いてくかい？\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0676
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x194),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "のレシピを教えてもらった。\x02",
        )
    )

    CloseMessageWindow()

    #A0677
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x194),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "のレシピを覚えた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    OP_B0(0x2)
    Return()

    # Function_26_C32C end

    def Function_27_C416(): pass

    label("Function_27_C416")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_C501")
    OP_4B(0x15, 0xFF)
    OP_4B(0x16, 0xFF)
    OP_4B(0x17, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C440")
    Call(0, 28)
    Jump("loc_C4F5")

    label("loc_C440")


    #C0678
    ChrTalk(
        0x17,
        (
            "#6002F風の音……すごく感じます。\x02\x03",

            "ありがとう……！\x01",
            "エステルさん、ヨシュアさん！\x02",
        )
    )

    CloseMessageWindow()

    #C0679
    ChrTalk(
        0x15,
        "#0809Fえへへ……\x02",
    )

    CloseMessageWindow()

    #C0680
    ChrTalk(
        0x16,
        "#0902F喜んでもらえて何よりだよ。\x02",
    )

    CloseMessageWindow()

    #C0681
    ChrTalk(
        0x101,
        "#0004F（ちょっと妬けるな……）\x02",
    )

    CloseMessageWindow()

    label("loc_C4F5")

    OP_4C(0x15, 0xFF)
    OP_4C(0x16, 0xFF)
    OP_4C(0x17, 0xFF)

    label("loc_C501")

    TalkEnd(0xFE)
    Return()

    # Function_27_C416 end

    def Function_28_C505(): pass

    label("Function_28_C505")

    EventBegin(0x0)
    Fade(500)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_4B(0x8, 0xFF)
    OP_68(-24130, -1400, 4220, 0)
    MoveCamera(45, 19, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(18500, 0)
    SetChrPos(0x101, -19520, -3000, 5040, 270)
    SetChrPos(0x102, -19520, -3000, 3780, 270)
    SetChrPos(0x103, -18270, -3000, 3780, 270)
    SetChrPos(0x104, -18270, -3000, 5040, 270)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C5AD")
    SetChrPos(0x10A, -18500, -3000, 2490, 270)

    label("loc_C5AD")

    OP_0D()
    Sleep(250)

    #C0682
    ChrTalk(
        0x17,
        (
            "#6000Fふふっ……\x01",
            "風車って面白いですね。\x02\x03",

            "見えないですけど……\x01",
            "確かに回ってるのが分かります。\x02",
        )
    )

    CloseMessageWindow()

    #C0683
    ChrTalk(
        0x15,
        (
            "#0800Fそっか……風の音とか\x01",
            "流れが感じられるもんね。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x16, 0x8, 500)

    #C0684
    ChrTalk(
        0x16,
        (
            "#0900Fすみません。\x01",
            "ピンクのを一つください。\x02\x03",

            "プレゼント用に\x01",
            "包装もお願いします。\x02",
        )
    )

    CloseMessageWindow()

    #C0685
    ChrTalk(
        0x8,
        "まいどっす！\x02",
    )

    CloseMessageWindow()
    OP_63(0x17, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x17)

    #C0686
    ChrTalk(
        0x17,
        "#6008Fヨ、ヨシュアさん……？\x02",
    )

    CloseMessageWindow()
    OP_93(0x16, 0x5A, 0x1F4)

    #C0687
    ChrTalk(
        0x15,
        (
            "#0800Fいいのいいの。\x01",
            "このくらい大した事ないから。\x02",
        )
    )

    CloseMessageWindow()

    #C0688
    ChrTalk(
        0x16,
        (
            "#0904Fアリオスさんには日頃から\x01",
            "お世話になってるからね。\x02\x03",

            "#0902Fだからという訳じゃないけど\x01",
            "受け取ってくれると嬉しいな。\x02",
        )
    )

    CloseMessageWindow()

    #C0689
    ChrTalk(
        0x17,
        "#6002Fあ、ありがとうございます……\x02",
    )

    CloseMessageWindow()
    Fade(500)
    OP_68(-19140, -1400, 3950, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15000, 0)
    OP_0D()
    Sleep(100)

    #C0690
    ChrTalk(
        0x104,
        (
            "#0300F（はは……\x01",
            "  結構楽しそうじゃねぇか。）\x02",
        )
    )

    CloseMessageWindow()

    #C0691
    ChrTalk(
        0x101,
        (
            "#0000F（ああ……\x01",
            "  邪魔するのは止めておこう。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xD0, 1)
    OP_4C(0x8, 0xFF)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_28_C505 end

    def Function_29_C88A(): pass

    label("Function_29_C88A")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearMapFlags(0x10000000)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_68(-16810, 1440, 25050, 0)
    MoveCamera(49, 28, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(26970, 0)
    OP_68(-1670, 1440, 2470, 7000)
    MoveCamera(25, 17, 0, 7000)
    OP_6E(600, 7000)
    SetCameraDistance(21920, 7000)
    FadeToBright(1000, 0)
    Sleep(500)
    OP_6F(0x79)
    Sleep(500)
    Fade(500)
    OP_68(5230, -200, -13420, 0)
    MoveCamera(54, 14, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(18000, 0)
    OP_68(-26250, 1500, -2620, 6000)
    MoveCamera(22, 22, 0, 6000)
    OP_6E(600, 6000)
    SetCameraDistance(14290, 6000)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0x13, 0x8000)
    SetChrFlags(0xA, 0x8000)
    SetChrFlags(0x9, 0x8000)
    SetChrFlags(0x11, 0x8000)
    SetChrFlags(0xB, 0x8000)
    OP_6F(0x79)
    Sleep(500)
    Fade(500)
    OP_68(-6850, 1440, -820, 0)
    MoveCamera(35, 29, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(31810, 0)
    SetCameraDistance(37810, 5000)
    OP_0D()
    PlaceName2(340, 40, "c_plac04", 0x0, 0)
    OP_6F(0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CB86")

    #A0692
    AnonymousTalk(
        0x104,
        (
            "#0305Fひゅー、随分と\x01",
            "エキゾチックな街並みだな。\x02",
        )
    )

    CloseMessageWindow()

    #A0693
    AnonymousTalk(
        0x103,
        (
            "#0202F東方風ですね……\x01",
            "話には聞いていましたが少し驚きです。\x02",
        )
    )

    CloseMessageWindow()

    #A0694
    AnonymousTalk(
        0x102,
        (
            "#0102F東通りの露店街……\x01",
            "私もあんまり来た事がないわね。\x02",
        )
    )

    CloseMessageWindow()

    #A0695
    AnonymousTalk(
        0x104,
        (
            "#0309Fお、んじゃあ\x01",
            "適当にぶらぶらしてみるか。\x02",
        )
    )

    CloseMessageWindow()

    #A0696
    AnonymousTalk(
        0x101,
        (
            "#0006Fあのな……\x01",
            "買い物目的じゃないんだけど。\x02\x03",

            "#0008F（それに……確か東通りには\x01",
            "  遊撃士協会#10Rブレイサーギルド#があったはずだな。）\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_CB86")

    FadeToDark(300, 0, 100)
    OP_0D()
    Sound(828, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0697
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "東通りは、街の東側にある東方風の街区です。\x02",
        )
    )

    CloseMessageWindow()

    #A0698
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "市場には露店が軒を連ね、\x01",
            "多くの市民や買い物客が行き交います。\x02",
        )
    )

    CloseMessageWindow()

    #A0699
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "また、市民から絶大な支持を得ている\x01",
            "《遊撃士協会#10Rブレイサーギルド#》の支部もあります。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    ClearChrFlags(0x8, 0x8000)
    ClearChrFlags(0x13, 0x8000)
    ClearChrFlags(0xA, 0x8000)
    ClearChrFlags(0x9, 0x8000)
    ClearChrFlags(0x11, 0x8000)
    ClearChrFlags(0xB, 0x8000)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CD0C")
    OP_68(-29790, 1420, 13830, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(22500, 0)
    Jump("loc_CD59")

    label("loc_CD0C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CD59")
    SetChrPos(0x0, -20550, -310, 29980, 180)
    OP_68(-20550, 1440, 29980, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(22500, 0)

    label("loc_CD59")

    SetScenarioFlags(0x44, 5)
    EventEnd(0x5)
    Return()

    # Function_29_C88A end

    def Function_30_CD5F(): pass

    label("Function_30_CD5F")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-10500, 2000, -1000, 0)
    MoveCamera(65, 3, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(30000, 0)
    SetChrPos(0x0, 27600, -300, -2700, 0)
    SetChrPos(0x1, 27600, -300, -2700, 0)
    SetChrPos(0x2, 27600, -300, -2700, 0)
    SetChrPos(0x3, 27600, -300, -2700, 0)
    SetChrFlags(0xA, 0x8000)
    SetChrFlags(0x9, 0x8000)
    SetChrFlags(0x11, 0x8000)
    SetChrFlags(0xB, 0x8000)
    SetChrFlags(0x13, 0x8000)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0xE, 0x8000)
    ClearChrFlags(0x10, 0x80)
    ClearChrBattleFlags(0x10, 0x8000)
    OP_4B(0x10, 0xFF)
    BeginChrThread(0x10, 0, 0, 0)
    SetChrPos(0x10, -19900, -320, 18140, 90)
    SetChrFlags(0x10, 0x8000)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    OP_4B(0xC, 0xFF)
    SetChrPos(0xC, -16300, -300, 12700, 135)
    SetChrFlags(0xC, 0x8000)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    OP_4B(0xD, 0xFF)
    SetChrPos(0xD, -4900, -300, 4000, 315)
    SetChrFlags(0xD, 0x8000)
    Sleep(1000)
    OP_C7(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0700
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#1K同日、１５：００──\x02",
        )
    )

    Sleep(2500)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C7(0x1, 0x800)
    PlayBGM("ed7103", 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_CECC():
        OP_98(0xFE, 0x32C8, 0x0, 0xFFFFCD38, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_CECC)

    def lambda_CEE6():
        OP_98(0xFE, 0xFFFFCD38, 0x0, 0x32C8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_CEE6)
    OP_68(-10500, 1000, -1000, 5000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x1)
    Fade(1000)
    OP_68(-7500, 2100, 14100, 0)
    MoveCamera(75, 23, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(21500, 0)
    SetCameraDistance(17500, 4000)
    Sleep(3000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    ClearScenarioFlags(0x2, 4)
    SetScenarioFlags(0x5C, 1)
    NewScene("c1010", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_30_CD5F end

    def Function_31_CF74(): pass

    label("Function_31_CF74")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-7800, 1300, 13600, 0)
    MoveCamera(0, 21, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17150, 0)
    SetChrPos(0x101, -7000, 300, 14400, 225)
    SetChrPos(0x102, -7000, 300, 14400, 225)
    SetChrPos(0x103, -7000, 300, 14400, 225)
    SetChrPos(0x104, -7000, 300, 14400, 225)
    OP_4B(0x17, 0xFF)
    ClearChrFlags(0x17, 0x80)
    ClearChrBattleFlags(0x17, 0x8000)
    SetChrPos(0x17, -7000, 300, 14400, 225)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x17, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_4B(0xD, 0xFF)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)
    OP_4B(0xC, 0xFF)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    ClearChrFlags(0x10, 0x80)
    ClearChrBattleFlags(0x10, 0x8000)
    OP_4B(0x10, 0xFF)
    BeginChrThread(0x10, 0, 0, 0)
    SetChrPos(0x10, -19900, -320, 18140, 90)
    SetChrFlags(0x10, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()
    Sound(103, 0, 100, 0)
    ClearMapObjFlags(0x2, 0x10)
    OP_71(0x2, 0x0, 0x5, 0x0, 0x0)
    OP_79(0x2)
    OP_68(-11000, 700, 10250, 4500)

    def lambda_D0C9():
        OP_95(0xFE, -12000, -300, 9400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_D0C9)

    def lambda_D0E3():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_D0E3)
    Sleep(500)

    def lambda_D0F7():
        OP_95(0xFE, -10600, -300, 10800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_D0F7)

    def lambda_D111():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_D111)
    Sleep(500)

    def lambda_D125():
        OP_95(0xFE, -10600, -300, 10800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_D125)

    def lambda_D13F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_D13F)
    Sleep(500)

    def lambda_D153():
        OP_95(0xFE, -10600, -300, 10800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_D153)

    def lambda_D16D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_D16D)
    Sleep(700)

    def lambda_D181():
        OP_95(0xFE, -9600, -300, 11800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_D181)

    def lambda_D19B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_D19B)
    WaitChrThread(0x103, 1)

    def lambda_D1B0():
        OP_95(0xFE, -11000, -300, 9000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_D1B0)

    def lambda_D1CA():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_D1CA)
    WaitChrThread(0x102, 1)

    def lambda_D1DF():
        OP_95(0xFE, -11600, -300, 11200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_D1DF)

    def lambda_D1F9():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_D1F9)
    WaitChrThread(0x104, 1)

    def lambda_D20E():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_D20E)
    WaitChrThread(0x103, 1)

    def lambda_D21F():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_D21F)
    WaitChrThread(0x102, 1)

    def lambda_D230():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_D230)
    WaitChrThread(0x101, 1)
    Sound(104, 0, 100, 0)
    OP_71(0x2, 0x5, 0x0, 0x0, 0x0)
    OP_79(0x2)
    SetMapObjFlags(0x2, 0x10)
    WaitChrThread(0x17, 1)
    WaitChrThread(0x104, 2)
    WaitChrThread(0x103, 2)
    WaitChrThread(0x102, 2)
    Sleep(300)

    #C0701
    ChrTalk(
        0x101,
        (
            "#0006F#11Pいや……\x01",
            "何ていうか、圧倒されたな。\x02",
        )
    )

    CloseMessageWindow()

    #C0702
    ChrTalk(
        0x103,
        (
            "#6P#0204Fアリオスさんは勿論ですが、\x01",
            "ホープのエステルさんたち……\x02\x03",

            "#0202Fそれ以外の人たちも全員、\x01",
            "かなり腕が立ちそうでしたね。\x02",
        )
    )

    CloseMessageWindow()

    #C0703
    ChrTalk(
        0x104,
        (
            "#6P#0300Fどうやら全員、Ｂ級以上の\x01",
            "ランクを持ってるみてぇだが……\x02\x03",

            "若手の実力者が\x01",
            "あれだけ集まっている支部も\x01",
            "珍しいんじゃねぇか？\x02",
        )
    )

    CloseMessageWindow()

    #C0704
    ChrTalk(
        0x102,
        (
            "#5P#0102Fそれだけギルドも\x01",
            "クロスベルという場所を\x01",
            "重視しているんでしょうね。\x02\x03",

            "#0106F裏を返せば、警察が動けない状況を\x01",
            "見透かされてるんでしょうけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0705
    ChrTalk(
        0x101,
        (
            "#0006F#11Pああ……\x01",
            "こちらもしっかりしないとな。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_68(-10100, 700, 11300, 1200)

    def lambda_D4A0():
        TurnDirection(0xFE, 0x17, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_D4A0)
    Sleep(150)

    def lambda_D4B0():
        TurnDirection(0xFE, 0x17, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_D4B0)
    Sleep(50)
    TurnDirection(0x102, 0x17, 500)
    OP_6F(0x1)

    #C0706
    ChrTalk(
        0x101,
        (
            "#6P#0012Fっと、ゴメン。\x01",
            "いきなり変なことを言って。\x02",
        )
    )

    CloseMessageWindow()

    #C0707
    ChrTalk(
        0x17,
        (
            "#6002F#11Pふふ、気にしないでください。\x02\x03",

            "#6008Fお父さんが昔、警察にいたのは\x01",
            "わたしも聞いていますし……\x02\x03",

            "いろいろ複雑で難しい問題が\x01",
            "あるみたいですけど……\x02\x03",

            "#6000Fでも、今回はいっしょに\x01",
            "協力してお仕事するんですよね？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2C, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D68A")

    #C0708
    ChrTalk(
        0x101,
        (
            "#6P#0004Fああ、どちらかというと\x01",
            "俺たちが助けてもらうんだけどね。\x02\x03",

            "#0002F──さてと、それじゃあ\x01",
            "支援課に案内させてもらうよ。\x02\x03",

            "手を引かせてもらっていいかい？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D999")

    label("loc_D68A")


    #C0709
    ChrTalk(
        0x101,
        (
            "#6P#0004Fああ、どちらかというと\x01",
            "俺たちが助けてもらうんだけどね。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0710
    ChrTalk(
        0x101,
        (
            "#6P#0000Fそういえば、おととい作った\x01",
            "手作りのペンダント……\x02\x03",

            "お父さんには渡せたのかい？\x02",
        )
    )

    CloseMessageWindow()

    #C0711
    ChrTalk(
        0x17,
        (
            "#6005F#11Pあ……はい。\x02\x03",

            "#6000Fえへへ……実は昨晩\x01",
            "お父さんがお見舞いに来てくれて。\x02\x03",

            "#6010F無事に渡せたんですけど……\x01",
            "お父さん、どんな顔をしてたのかな。\x02\x03",

            "しばらく黙ってて……\x01",
            "その後、ちょっとぶっきらぼうに\x01",
            "お礼を言われたんですけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0712
    ChrTalk(
        0x104,
        (
            "#6P#0302Fハハ……\x01",
            "『……受け取っておく』ってか？\x02",
        )
    )

    CloseMessageWindow()

    #C0713
    ChrTalk(
        0x17,
        "#6002F#11Pはい、ちょうどそんな感じです。\x02",
    )

    CloseMessageWindow()

    #C0714
    ChrTalk(
        0x103,
        "#6P#0204F容易に想像できますね……\x02",
    )

    CloseMessageWindow()

    #C0715
    ChrTalk(
        0x102,
        (
            "#6P#0109Fふふ、シズクちゃんの前では\x01",
            "アリオスさんも形無しね。\x02",
        )
    )

    CloseMessageWindow()

    #C0716
    ChrTalk(
        0x101,
        (
            "#6P#0004Fそれだけシズクちゃんの事を\x01",
            "大事にしてるんだろうな……\x02\x03",

            "#0002F──さてと、それじゃあ\x01",
            "支援課に案内させてもらうよ。\x02\x03",

            "手を引かせてもらっていいかい？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D999")


    #C0717
    ChrTalk(
        0x17,
        (
            "#6000F#11Pあ、ありがとうございます。\x02\x03",

            "#6005Fそういえば……\x01",
            "キーアちゃん、いるんですよね？\x02",
        )
    )

    CloseMessageWindow()

    #C0718
    ChrTalk(
        0x102,
        (
            "#0102Fええ、例のツァイトと\x01",
            "一緒にいるんじゃないかしら。\x02",
        )
    )

    CloseMessageWindow()

    #C0719
    ChrTalk(
        0x103,
        (
            "#6P#0202Fシズクさんが遊びに来たら\x01",
            "飛び上がって喜びそうですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0720
    ChrTalk(
        0x17,
        "#6002F#11Pえへへ……嬉しいな。\x02",
    )

    CloseMessageWindow()

    #C0721
    ChrTalk(
        0x104,
        (
            "#6P#0302Fよーし、そんじゃあ姫を\x01",
            "エスコートして帰るとするか！\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(16650, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    SetChrPos(0x101, -17500, -300, 14300, 270)
    SetChrPos(0x102, -17400, -300, 13000, 270)
    SetChrPos(0x103, -16000, -300, 13200, 270)
    SetChrPos(0x104, -15800, -300, 14500, 270)
    SetChrPos(0x17, -17500, -300, 13700, 270)
    OP_68(-22000, 500, 13700, 0)
    MoveCamera(54, 26, 0, 0)
    OP_6E(620, 0)
    SetCameraDistance(15500, 0)

    def lambda_DB7D():
        OP_97(0xFE, 0xFFFFB1E0, 0x0, 0x0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_DB7D)
    Sleep(15)

    def lambda_DB9A():
        OP_97(0xFE, 0xFFFFB1E0, 0x0, 0x0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_DB9A)
    Sleep(15)

    def lambda_DBB7():
        OP_97(0xFE, 0xFFFFB1E0, 0x0, 0x0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_DBB7)
    Sleep(15)

    def lambda_DBD4():
        OP_97(0xFE, 0xFFFFB1E0, 0x0, 0x0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_DBD4)
    Sleep(15)

    def lambda_DBF1():
        OP_97(0xFE, 0xFFFFB1E0, 0x0, 0x0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_DBF1)
    BeginChrThread(0x101, 3, 0, 32)
    OP_68(-27000, 500, 13700, 10000)
    MoveCamera(54, 18, 0, 10000)
    SetCameraDistance(19500, 10000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_63(0x102, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(700)
    OP_63(0x101, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(500)
    OP_63(0x104, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(800)
    OP_63(0x17, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(500)
    OP_63(0x103, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1500)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    SetChrPos(0xD, -40000, -340, 16000, 90)
    SetChrFlags(0xD, 0x8000)

    def lambda_DCC9():
        OP_97(0xFE, 0x4E20, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_DCC9)
    OP_63(0x102, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(700)
    OP_63(0x101, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(500)
    OP_63(0x104, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(800)
    OP_63(0x17, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(500)
    OP_63(0x103, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x101, 0xFF)
    EndChrThread(0x102, 0xFF)
    EndChrThread(0x103, 0xFF)
    EndChrThread(0x104, 0xFF)
    StopBGM(0xFA0)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x5D, 7)
    NewScene("c0100", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_31_CF74 end

    def Function_32_DD7E(): pass

    label("Function_32_DD7E")

    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    SetChrPos(0xC, -10000, -300, 6500, 315)
    SetChrFlags(0xC, 0x8000)

    def lambda_DDA3():
        OP_95(0xFE, -16000, -300, 12500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_DDA3)
    WaitChrThread(0xC, 1)

    def lambda_DDC1():
        OP_95(0xFE, -36000, -300, 12500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_DDC1)
    WaitChrThread(0xC, 1)
    Return()

    # Function_32_DD7E end

    def Function_33_DDDB(): pass

    label("Function_33_DDDB")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50011.itc", 0x1E)
    SoundLoad(806)
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
    CreatePortrait(0, 180, 0, 436, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis007.itp")

    def lambda_DEAF():
        OP_98(0xFE, 0xFFFFEC78, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_DEAF)
    Sleep(50)

    def lambda_DECC():
        OP_98(0xFE, 0xFFFFEC78, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_DECC)
    Sleep(50)

    def lambda_DEE9():
        OP_98(0xFE, 0xFFFFEC78, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_DEE9)
    Sleep(50)

    def lambda_DF06():
        OP_98(0xFE, 0xFFFFEC78, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_DF06)
    SetCameraDistance(20500, 2500)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x101, 1)
    Sound(806, 2, 100, 0)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    OP_6F(0x10)
    Sleep(250)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_DF69():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_DF69)
    Sleep(50)

    def lambda_DF79():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_DF79)
    Fade(250)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    Sound(804, 0, 100, 0)
    Sleep(500)
    SetChrSubChip(0x101, 0x1)
    OP_24(0x326)
    Sound(807, 0, 100, 0)
    Sleep(300)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    FadeToDark(500, 0, 100)
    OP_0D()
    OP_CA(0x0, 0x0, 0x3)
    #Sound(1084, 255, 90, 0)    #voice#Lloyd
    SetMessageWindowPos(90, 130, -1, -1)

    #A0722
    AnonymousTalk(
        0x101,
        (
            "#0001Fはい、特務支援課、\x01",
            "バニングスです。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(150)
    #Sound(2083, 255, 100, 0)    #voice#Fran
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("フランの声")

    #A0723
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "あ、ロイドさん～！\x02\x03",

            "よかった。\x01",
            "繋がったみたいですね～。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0724
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0005Fフラン……？\x01",
            "直接連絡なんて珍しいな。\x02\x03",

            "#0000F何かあったのか？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("フランの声")

    #A0725
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "えっと、それが……\x02\x03",

            "実は支援課に相談があるという\x01",
            "市民の方がいるんですけど……\x02\x03",

            "直接そちらに回してもいいですか？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0726
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0001Fああ……\x01",
            "大丈夫だと思うけど。\x02\x03",

            "いつものように端末で\x01",
            "回せる話じゃないってことか？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("フランの声")

    #A0727
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "はい……\x01",
            "ちょっと深刻そうな話なので。\x02\x03",

            "それにロイドさんたちを是非にと\x01",
            "指名される方も珍しいですから。\x02\x03",

            "どうせだったらと思いまして～。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    SetMessageWindowPos(90, 130, -1, -1)

    #A0728
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0012Fそ、そうか……\x02\x03",

            "#0000F事情は分かったよ。\x01",
            "支援課の方に戻ればいいのかな？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("フランの声")

    #A0729
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "はい、相談者の方にも\x01",
            "そちらに向かうように伝えます。\x02\x03",

            "どのくらいでお戻りになりますか？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0730
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0003Fそうだな……\x02\x03",

            "#0000F少し遅れるかもしれないから\x01",
            "早く着いたら中で待っているように\x01",
            "相談者に伝えておいてくれ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("フランの声")

    #A0731
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "はい、分かりましたー。\x02\x03",

            "それではロイドさん。\x01",
            "よろしくお願いしますね～。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sound(825, 0, 100, 0)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    OP_CA(0x0, 0x0, 0x3)
    SetChrSubChip(0x101, 0x0)
    Sleep(300)

    #C0732
    ChrTalk(
        0x102,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0105F#5P緊急の要請が入ったの？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    ClearChrFlags(0x101, 0x20)
    ClearChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    Sound(807, 0, 100, 0)
    OP_0D()
    Sleep(150)
    TurnDirection(0x101, 0x104, 500)

    #C0733
    ChrTalk(
        0x101,
        (
            "#6P#0003Fああ……\x01",
            "ちょっと深刻な話みたいだ。\x02\x03",

            "#0000F他の支援要請は切り上げて\x01",
            "いったん支援課の方に戻ろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0734
    ChrTalk(
        0x103,
        "#0202F#11P……了解です。\x02",
    )

    CloseMessageWindow()

    #C0735
    ChrTalk(
        0x104,
        "#5P#0309Fで、相談者ってのは美人なのか？\x02",
    )

    CloseMessageWindow()

    #C0736
    ChrTalk(
        0x101,
        "#6P#0006Fいや、知らないって。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_CA(0x1, 0xFF, 0x0)
    OP_D5(0x1E)
    OP_4C(0xC, 0xFF)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    OP_4C(0xD, 0xFF)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    SetChrPos(0x0, 24700, -300, 500, 270)
    ClearMapFlags(0x10000000)
    SetScenarioFlags(0x80, 1)
    OP_29(0x41, 0x1, 0x2)
    OP_24(0x326)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_33_DDDB end

    def Function_34_E5F6(): pass

    label("Function_34_E5F6")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-5890, -1400, -10830, 0)
    MoveCamera(53, 23, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(14300, 0)
    SetChrPos(0x101, -5200, -3000, -10840, 0)
    SetChrPos(0x102, -3950, -3000, -12150, 0)
    SetChrPos(0x103, -5040, -3000, -11950, 0)
    SetChrPos(0x104, -3970, -3000, -10800, 0)
    SetChrFlags(0x11, 0x80)
    SetChrBattleFlags(0x11, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E6F1")

    #C0737
    ChrTalk(
        0x101,
        (
            "#6P#0003F（東通りの市場……\x01",
            "  落し物をしたトロントさんが\x01",
            "  立ち寄っていた場所だな。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 1)

    label("loc_E6F1")


    #C0738
    ChrTalk(
        0x101,
        (
            "#6P#0000Fすみません、この辺りで\x01",
            "落し物を見かけませんでしたか？\x02",
        )
    )

    CloseMessageWindow()

    #C0739
    ChrTalk(
        0xB,
        "#5P落し物かい……？\x02",
    )

    CloseMessageWindow()

    #C0740
    ChrTalk(
        0xB,
        (
            "#5Pああ、そういえば……\x01",
            "昨日能天気な青年が\x01",
            "１つ落し物をしたよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0741
    ChrTalk(
        0xB,
        (
            "#5Pウチの露店を見て\x01",
            "下らない冗談を飛ばしてたけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0742
    ChrTalk(
        0xB,
        (
            "#5Pカバンにデッカイ穴が空いててねぇ、\x01",
            "ぽろっと小包を落として\x01",
            "そのままどこかに行っちまったんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0743
    ChrTalk(
        0xB,
        (
            "#5Pあたしもすぐに\x01",
            "追いかけたんだけどね。\x02",
        )
    )

    CloseMessageWindow()

    #C0744
    ChrTalk(
        0x104,
        "#11P#0300Fはは……間違いねえみたいだな。\x02",
    )

    CloseMessageWindow()

    #C0745
    ChrTalk(
        0xB,
        (
            "#5Pなんだい、警察の人が\x01",
            "引き取りに来たのかい？\x02",
        )
    )

    CloseMessageWindow()

    #C0746
    ChrTalk(
        0xB,
        "#5Pそいじゃあんたらに渡しとくよ。\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0747
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x338),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を預かった。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x338, 1)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x337, 0x0)"), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x338, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x339, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E9D2")

    #C0748
    ChrTalk(
        0x101,
        (
            "#0006Fふう……ともかくこれで\x01",
            "全部見つかったみたいだ。\x02\x03",

            "#0000Fトロントさんに報告しよう。\x02",
        )
    )

    CloseMessageWindow()

    #C0749
    ChrTalk(
        0x102,
        "#0100Fええ、届けてあげましょう。\x02",
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_E9D2")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-4630, -1400, -10720, 0)
    MoveCamera(45, 13, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(21000, 0)
    SetChrPos(0x0, -4630, -3000, -10720, 0)
    SetChrPos(0x1, -4630, -3000, -10720, 0)
    SetChrPos(0x2, -4630, -3000, -10720, 0)
    SetChrPos(0x3, -4630, -3000, -10720, 0)
    OP_4C(0xB, 0xFF)
    ClearChrFlags(0x11, 0x80)
    ClearChrBattleFlags(0x11, 0x8000)
    OP_29(0x2, 0x1, 0x2)
    SetScenarioFlags(0x2, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2, 0x1, 0x1)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2, 0x1, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2, 0x1, 0x4)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_EA89")
    OP_29(0x2, 0x1, 0x1F)

    label("loc_EA89")

    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_34_E5F6 end

    def Function_35_EA8F(): pass

    label("Function_35_EA8F")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_EB33")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EB08")

    #C0750
    ChrTalk(
        0x101,
        (
            "#0000Fこっちは街の東口だな。\x02\x03",

            "今は外に出る必要はない……\x01",
            "市内の仕事に専念しよう。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_EB33")

    label("loc_EB08")

    SetChrName("")

    #A0751
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "街の外に出る必要はなさそうだ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_EB33")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_EBA7")

    #C0752
    ChrTalk(
        0x101,
        (
            "#0000Fウルスラ病院に行くには\x01",
            "街の南口から出ないとな。\x02\x03",

            "中央広場から駅前通りの方へ\x01",
            "回ってみよう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EBA7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_EC08")

    #C0753
    ChrTalk(
        0x101,
        (
            "#0000Fマインツに行くには\x01",
            "街の北口から出ないとな。\x02\x03",

            "住宅街の方に回ってみよう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EC08")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_ECBB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EC92")

    #C0754
    ChrTalk(
        0x101,
        (
            "#0005Fっと、こっちは東口だ。\x02\x03",

            "#0000Fキーアを危険な目に\x01",
            "遭わせたくないし、\x01",
            "外に出るのは止めておこう。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_ECBB")

    label("loc_EC92")

    SetChrName("")

    #A0755
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "街道に出る必要はなさそうだ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_ECBB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_ED5D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_ED34")

    #C0756
    ChrTalk(
        0x101,
        (
            "#0003Fこっちは街の東口だな。\x02\x03",

            "黒月のこともある……\x01",
            "……今は市内の捜査に集中しよう。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_ED5D")

    label("loc_ED34")

    SetChrName("")

    #A0757
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "今は市内の捜査に集中しよう。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_ED5D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_EDEE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EDB9")

    #C0758
    ChrTalk(
        0x101,
        (
            "#0000Fこっちは街の東口だな。\x01",
            "……今はウルスラ病院に急ごう！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_EDEE")

    label("loc_EDB9")

    SetChrName("")

    #A0759
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "東クロスベル街道に出る必要はなさそうだ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_EDEE")

    SetChrPos(0x0, 29390, -300, 500, 270)
    EventEnd(0x4)
    Return()

    # Function_35_EA8F end

    def Function_36_EE02(): pass

    label("Function_36_EE02")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EFB4")

    #C0760
    ChrTalk(
        0x10A,
        "#0603F………………………………\x02",
    )

    CloseMessageWindow()

    #C0761
    ChrTalk(
        0x101,
        (
            "#0005Fダドリーさん、\x01",
            "どうかしたんですか？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EE94")

    #C0762
    ChrTalk(
        0x10A,
        "#0601Fフン、ギルドか……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_EEBE")

    label("loc_EE94")


    #C0763
    ChrTalk(
        0x10A,
        "#0601Fお前たち、まさか……（ギロッ）\x02",
    )

    CloseMessageWindow()

    label("loc_EEBE")

    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0764
    ChrTalk(
        0x101,
        (
            "#0005F（うっ、そうだった……\x01",
            "  ダドリーさんは筋金入りの\x01",
            "  遊撃士嫌い……）\x02",
        )
    )

    CloseMessageWindow()

    #C0765
    ChrTalk(
        0x104,
        (
            "#0306F（こりゃあ中には\x01",
            "  入らねえ方が良さそうだな。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x47, 6)
    Jump("loc_F07F")

    label("loc_EFB4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F016")

    #C0766
    ChrTalk(
        0x10A,
        (
            "#0603F………………………………\x02\x03",

            "#0600F特に用はない。\x01",
            "……さっさと行くぞ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F07F")

    label("loc_F016")


    #C0767
    ChrTalk(
        0x10A,
        "#0600F………………………………\x02",
    )

    CloseMessageWindow()

    #C0768
    ChrTalk(
        0x101,
        (
            "#0006F（ダドリーさんが睨んでいる……\x01",
            "  今は入らないでおこう。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F07F")

    Sleep(50)
    SetChrPos(0x0, -9300, -300, 12060, 225)
    EventEnd(0x4)
    Return()

    # Function_36_EE02 end

    def Function_37_F096(): pass

    label("Function_37_F096")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F12A")

    #C0769
    ChrTalk(
        0x101,
        (
            "#0005Fおっと……\x02\x03",

            "あの記者の人が言っていた店は\x01",
            "すぐそこみたいだ。\x02\x03",

            "#0003F今は情報がほしい。\x01",
            "ともかく一度話を聞いてみよう。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_F169")

    label("loc_F12A")


    #C0770
    ChrTalk(
        0x101,
        (
            "#0003F今は情報がほしい……\x01",
            "一度話を聞くだけ聞いてみよう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F169")

    Sleep(50)
    SetChrPos(0x0, -6210, -3000, -9790, 135)
    EventEnd(0x4)
    Return()

    # Function_37_F096 end

    def Function_38_F180(): pass

    label("Function_38_F180")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F214")

    #C0771
    ChrTalk(
        0x101,
        (
            "#0005Fおっと……\x02\x03",

            "あの記者の人が言っていた店は\x01",
            "すぐそこみたいだ。\x02\x03",

            "#0003F今は情報がほしい。\x01",
            "ともかく一度話を聞いてみよう。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_F253")

    label("loc_F214")


    #C0772
    ChrTalk(
        0x101,
        (
            "#0003F今は情報がほしい……\x01",
            "一度話を聞くだけ聞いてみよう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F253")

    Sleep(50)
    SetChrPos(0x0, 2100, -1350, -5490, 180)
    EventEnd(0x4)
    Return()

    # Function_38_F180 end

    def Function_39_F26A(): pass

    label("Function_39_F26A")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x98, 7)), scpexpr(EXPR_END)), "loc_F2A4")
    SetChrName("")

    #A0773
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
    Jump("loc_11188")

    label("loc_F2A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x98, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F72A")
    SetChrName("")

    #A0774
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F51C")

    #C0775
    ChrTalk(
        0x153,
        (
            "#1110F……あ！\x01",
            "ねぇ、なんかあるよ？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_F365")

    #C0776
    ChrTalk(
        0x102,
        (
            "#0105Fこんな所にお地蔵様が……\x01",
            "何度か通ったけど気づかなかったわね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F406")

    label("loc_F365")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_F3B8")

    #C0777
    ChrTalk(
        0x103,
        (
            "#0205F地蔵……大きいお顔ですね。\x01",
            "見るのは初めてかもしれません。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F406")

    label("loc_F3B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_F406")

    #C0778
    ChrTalk(
        0x104,
        (
            "#0305Fへえ、地蔵まで奉られてたのかよ。\x01",
            "何となく見落としてたな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F406")


    #C0779
    ChrTalk(
        0x153,
        "#1111F……じぞ？\x02",
    )

    CloseMessageWindow()
    OP_63(0x153, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0780
    ChrTalk(
        0x153,
        (
            "#1105Fねーねー、\x01",
            "なんか置けそうな台があるよ。\x02\x03",

            "#1110Fおなかすいてるかもしれないし、\x01",
            "なんか持ってきてあげよーよ！\x02",
        )
    )

    CloseMessageWindow()

    #C0781
    ChrTalk(
        0x101,
        (
            "#0000Fきっと、お供えするための台座だな。\x02\x03",

            "#0000Fそうだな、\x01",
            "上手にできた料理があれば\x01",
            "今度持ってきてみよう。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F722")

    label("loc_F51C")


    #C0782
    ChrTalk(
        0x104,
        (
            "#0305Fへえ、東方風の\x01",
            "街並みだとは思ってたが。\x01",
            "地蔵まで奉られてんのかよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0783
    ChrTalk(
        0x103,
        (
            "#0200F見るのは初めてかもしれません。\x01",
            "……大きいお顔ですね。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F5CE")
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    label("loc_F5CE")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F5F1")
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    label("loc_F5F1")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F614")
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    label("loc_F614")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F637")
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    label("loc_F637")


    #C0784
    ChrTalk(
        0x103,
        "#0205Fこの地蔵の前の台座は……？\x02",
    )

    CloseMessageWindow()

    #C0785
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

    #C0786
    ChrTalk(
        0x101,
        (
            "#0000Fそうだな、支援課は基本自炊だし。\x02\x03",

            "うまくできた料理があれば\x01",
            "今度持ってきてみよう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F722")

    SetScenarioFlags(0x98, 0)
    Jump("loc_11188")

    label("loc_F72A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 5)), scpexpr(EXPR_END)), "loc_F761")
    SetChrName("")

    #A0787
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
    Jump("loc_11188")

    label("loc_F761")

    Call(0, 40)
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F7EF")
    SetChrName("")

    #A0788
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

    #C0789
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

    label("loc_F7EF")

    Call(0, 41)
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x98, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_FA4E")
    SetChrName("")

    #A0790
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

    #A0791
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

    #A0792
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

    #A0793
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
    Jump("loc_11188")

    label("loc_FA4E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x16), scpexpr(EXPR_GE), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x98, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_FC63")
    SetChrName("")

    #A0794
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

    #A0795
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

    #A0796
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

    #A0797
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
    Jump("loc_11188")

    label("loc_FC63")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_GE), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x98, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_FE75")
    SetChrName("")

    #A0798
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

    #A0799
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

    #A0800
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

    #A0801
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
    Jump("loc_11188")

    label("loc_FE75")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_GE), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x98, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1001F")
    SetChrName("")

    #A0802
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

    #A0803
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

    #A0804
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

    #A0805
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
    Jump("loc_11188")

    label("loc_1001F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x98, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_10180")
    SetChrName("")

    #A0806
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

    #A0807
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

    #A0808
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
    Jump("loc_11188")

    label("loc_10180")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x98, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1029B")
    SetChrName("")

    #A0809
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

    #A0810
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

    #A0811
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
    Jump("loc_11188")

    label("loc_1029B")

    SetChrName("")

    #A0812
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

    label("loc_102EE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11188")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuCmd(0, 1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 0)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x190, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_10339")
    MenuCmd(1, 1, "覇王麺")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 0)), scpexpr(EXPR_END)), "loc_1032F")
    Call(0, 16)

    label("loc_1032F")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_10339")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 1)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x193, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_10372")
    MenuCmd(1, 1, "薬膳麻婆≪黄龍≫")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 1)), scpexpr(EXPR_END)), "loc_10368")
    Call(0, 16)

    label("loc_10368")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_10372")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 2)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x196, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_103A3")
    MenuCmd(1, 1, "白虎炒飯")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 2)), scpexpr(EXPR_END)), "loc_10399")
    Call(0, 16)

    label("loc_10399")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_103A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 3)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x199, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_103DE")
    MenuCmd(1, 1, "極上ステーキ≪雅≫")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 3)), scpexpr(EXPR_END)), "loc_103D4")
    Call(0, 16)

    label("loc_103D4")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_103DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 4)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x19C, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_10419")
    MenuCmd(1, 1, "極上シチュー≪薫≫")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 4)), scpexpr(EXPR_END)), "loc_1040F")
    Call(0, 16)

    label("loc_1040F")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_10419")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 5)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x19F, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_10450")
    MenuCmd(1, 1, "鉄人鍋≪絢爛≫")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 5)), scpexpr(EXPR_END)), "loc_10446")
    Call(0, 16)

    label("loc_10446")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_10450")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 6)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1A2, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_10487")
    MenuCmd(1, 1, "賢人鍋≪繚乱≫")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 6)), scpexpr(EXPR_END)), "loc_1047D")
    Call(0, 16)

    label("loc_1047D")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_10487")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 7)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1A5, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_104C0")
    MenuCmd(1, 1, "リザレクトフライ")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 7)), scpexpr(EXPR_END)), "loc_104B6")
    Call(0, 16)

    label("loc_104B6")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_104C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 0)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1A8, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_104F9")
    MenuCmd(1, 1, "黄金卵飯≪輝き≫")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 0)), scpexpr(EXPR_END)), "loc_104EF")
    Call(0, 16)

    label("loc_104EF")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_104F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 1)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1AB, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_10532")
    MenuCmd(1, 1, "黄金卵麺≪煌き≫")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 1)), scpexpr(EXPR_END)), "loc_10528")
    Call(0, 16)

    label("loc_10528")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_10532")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 2)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1AE, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_10569")
    MenuCmd(1, 1, "キングバーガー")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 2)), scpexpr(EXPR_END)), "loc_1055F")
    Call(0, 16)

    label("loc_1055F")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_10569")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 3)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1B1, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1059E")
    MenuCmd(1, 1, "クイーンピザ")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 3)), scpexpr(EXPR_END)), "loc_10594")
    Call(0, 16)

    label("loc_10594")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_1059E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 4)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1B4, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_105D9")
    MenuCmd(1, 1, "行楽サンド≪相棒≫")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 4)), scpexpr(EXPR_END)), "loc_105CF")
    Call(0, 16)

    label("loc_105CF")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_105D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 5)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1B7, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_10614")
    MenuCmd(1, 1, "愛情凝縮箱≪お袋≫")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 5)), scpexpr(EXPR_END)), "loc_1060A")
    Call(0, 16)

    label("loc_1060A")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_10614")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 6)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1BA, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1064D")
    MenuCmd(1, 1, "フルムーンスープ")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 6)), scpexpr(EXPR_END)), "loc_10643")
    Call(0, 16)

    label("loc_10643")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_1064D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 7)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1BD, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_10686")
    MenuCmd(1, 1, "クレセントスープ")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 7)), scpexpr(EXPR_END)), "loc_1067C")
    Call(0, 16)

    label("loc_1067C")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_10686")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 0)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1C0, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_106BD")
    MenuCmd(1, 1, "絶菓≪白無垢≫")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 0)), scpexpr(EXPR_END)), "loc_106B3")
    Call(0, 16)

    label("loc_106B3")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_106BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 1)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1C3, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_106F2")
    MenuCmd(1, 1, "絶菓≪黄熟≫")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 1)), scpexpr(EXPR_END)), "loc_106E8")
    Call(0, 16)

    label("loc_106E8")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_106F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 2)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1C6, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_10727")
    MenuCmd(1, 1, "絶菓≪粉雪≫")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 2)), scpexpr(EXPR_END)), "loc_1071D")
    Call(0, 16)

    label("loc_1071D")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_10727")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 3)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1C9, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1075C")
    MenuCmd(1, 1, "絶菓≪浮雲≫")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 3)), scpexpr(EXPR_END)), "loc_10752")
    Call(0, 16)

    label("loc_10752")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_1075C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 4)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1CC, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_10795")
    MenuCmd(1, 1, "シュプリームラテ")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 4)), scpexpr(EXPR_END)), "loc_1078B")
    Call(0, 16)

    label("loc_1078B")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_10795")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 5)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1CF, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_107D0")
    MenuCmd(1, 1, "アルティマミックス")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 5)), scpexpr(EXPR_END)), "loc_107C6")
    Call(0, 16)

    label("loc_107C6")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_107D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 6)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1D2, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_10809")
    MenuCmd(1, 1, "キル・ナイトメア")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 6)), scpexpr(EXPR_END)), "loc_107FF")
    Call(0, 16)

    label("loc_107FF")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_10809")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 7)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1D5, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_10840")
    MenuCmd(1, 1, "秘水≪月光蝶≫")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 7)), scpexpr(EXPR_END)), "loc_10836")
    Call(0, 16)

    label("loc_10836")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_10840")

    MenuCmd(1, 1, "やめる")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuCmd(2, 1, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x1)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_10881")
    Jump("loc_11183")

    label("loc_10881")

    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 0)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x190, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_108EC")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_108E2")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x190, 1)
    SetScenarioFlags(0x99, 0)

    #A0813
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x190),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を供えた。\x02",
        )
    )


    label("loc_108E2")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_108EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 1)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x193, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_10938")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1092E")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x193, 1)
    SetScenarioFlags(0x99, 1)

    #A0814
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x193),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を供えた。\x02",
        )
    )


    label("loc_1092E")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_10938")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 2)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x196, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_10984")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1097A")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x196, 1)
    SetScenarioFlags(0x99, 2)

    #A0815
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x196),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を供えた。\x02",
        )
    )


    label("loc_1097A")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_10984")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 3)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x199, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_109D0")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_109C6")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x199, 1)
    SetScenarioFlags(0x99, 3)

    #A0816
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x199),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を供えた。\x02",
        )
    )


    label("loc_109C6")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_109D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 4)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x19C, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_10A1C")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10A12")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x19C, 1)
    SetScenarioFlags(0x99, 4)

    #A0817
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x19C),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を供えた。\x02",
        )
    )


    label("loc_10A12")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_10A1C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 5)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x19F, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_10A68")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10A5E")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x19F, 1)
    SetScenarioFlags(0x99, 5)

    #A0818
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x19F),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を供えた。\x02",
        )
    )


    label("loc_10A5E")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_10A68")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 6)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1A2, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_10AB4")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10AAA")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x1A2, 1)
    SetScenarioFlags(0x99, 6)

    #A0819
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1A2),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を供えた。\x02",
        )
    )


    label("loc_10AAA")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_10AB4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 7)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1A5, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_10B00")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10AF6")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x1A5, 1)
    SetScenarioFlags(0x99, 7)

    #A0820
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1A5),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を供えた。\x02",
        )
    )


    label("loc_10AF6")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_10B00")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 0)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1A8, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_10B4C")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10B42")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x1A8, 1)
    SetScenarioFlags(0x9A, 0)

    #A0821
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1A8),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を供えた。\x02",
        )
    )


    label("loc_10B42")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_10B4C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 1)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1AB, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_10B98")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10B8E")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x1AB, 1)
    SetScenarioFlags(0x9A, 1)

    #A0822
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1AB),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を供えた。\x02",
        )
    )


    label("loc_10B8E")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_10B98")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 2)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1AE, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_10BE4")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10BDA")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x1AE, 1)
    SetScenarioFlags(0x9A, 2)

    #A0823
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1AE),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を供えた。\x02",
        )
    )


    label("loc_10BDA")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_10BE4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 3)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1B1, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_10C30")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10C26")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x1B1, 1)
    SetScenarioFlags(0x9A, 3)

    #A0824
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1B1),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を供えた。\x02",
        )
    )


    label("loc_10C26")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_10C30")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 4)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1B4, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_10C7C")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10C72")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x1B4, 1)
    SetScenarioFlags(0x9A, 4)

    #A0825
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1B4),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を供えた。\x02",
        )
    )


    label("loc_10C72")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_10C7C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 5)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1B7, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_10CC8")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10CBE")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x1B7, 1)
    SetScenarioFlags(0x9A, 5)

    #A0826
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1B7),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を供えた。\x02",
        )
    )


    label("loc_10CBE")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_10CC8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 6)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1BA, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_10D14")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10D0A")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x1BA, 1)
    SetScenarioFlags(0x9A, 6)

    #A0827
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1BA),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を供えた。\x02",
        )
    )


    label("loc_10D0A")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_10D14")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 7)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1BD, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_10D60")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10D56")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x1BD, 1)
    SetScenarioFlags(0x9A, 7)

    #A0828
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1BD),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を供えた。\x02",
        )
    )


    label("loc_10D56")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_10D60")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 0)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1C0, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_10DAC")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10DA2")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x1C0, 1)
    SetScenarioFlags(0x9B, 0)

    #A0829
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1C0),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を供えた。\x02",
        )
    )


    label("loc_10DA2")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_10DAC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 1)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1C3, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_10DF8")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10DEE")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x1C3, 1)
    SetScenarioFlags(0x9B, 1)

    #A0830
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1C3),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を供えた。\x02",
        )
    )


    label("loc_10DEE")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_10DF8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 2)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1C6, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_10E44")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10E3A")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x1C6, 1)
    SetScenarioFlags(0x9B, 2)

    #A0831
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1C6),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を供えた。\x02",
        )
    )


    label("loc_10E3A")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_10E44")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 3)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1C9, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_10E90")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10E86")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x1C9, 1)
    SetScenarioFlags(0x9B, 3)

    #A0832
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1C9),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を供えた。\x02",
        )
    )


    label("loc_10E86")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_10E90")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 4)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1CC, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_10EDC")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10ED2")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x1CC, 1)
    SetScenarioFlags(0x9B, 4)

    #A0833
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1CC),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を供えた。\x02",
        )
    )


    label("loc_10ED2")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_10EDC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 5)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1CF, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_10F28")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10F1E")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x1CF, 1)
    SetScenarioFlags(0x9B, 5)

    #A0834
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1CF),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を供えた。\x02",
        )
    )


    label("loc_10F1E")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_10F28")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 6)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1D2, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_10F74")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10F6A")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x1D2, 1)
    SetScenarioFlags(0x9B, 6)

    #A0835
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1D2),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を供えた。\x02",
        )
    )


    label("loc_10F6A")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_10F74")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 7)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1D5, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_10FC0")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10FB6")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x1D5, 1)
    SetScenarioFlags(0x9B, 7)

    #A0836
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1D5),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を供えた。\x02",
        )
    )


    label("loc_10FB6")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_10FC0")

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11183")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x98, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11180")

    #C0837
    ChrTalk(
        0x101,
        (
            "#0000Fこれでよし、と。\x01",
            "……また持ってきてみようかな。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_11088")

    #C0838
    ChrTalk(
        0x102,
        (
            "#0100Fあまり同じ料理ばかりだと\x01",
            "失礼でしょうし、\x01",
            "一品一回くらいが良さそうね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1115F")

    label("loc_11088")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_110F7")

    #C0839
    ChrTalk(
        0x103,
        (
            "#0200Fあまり同じ料理ばかりだと\x01",
            "失礼かもしれません。\x01",
            "一品一回くらいが良さそうですね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1115F")

    label("loc_110F7")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1115F")

    #C0840
    ChrTalk(
        0x104,
        (
            "#0300Fあまり同じ料理ばかりだと\x01",
            "失礼なんじゃねえか？\x01",
            "一品一回くらいが良さそうだぜ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1115F")


    #C0841
    ChrTalk(
        0x101,
        "#0000Fああ、そうするか。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x98, 1)

    label("loc_11180")

    SetScenarioFlags(0x2, 5)

    label("loc_11183")

    Jump("loc_102EE")

    label("loc_11188")

    TalkEnd(0xFF)
    Return()

    # Function_39_F26A end

    def Function_40_1118C(): pass

    label("Function_40_1118C")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 0)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x190, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_111AF")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_111AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 1)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x193, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_111C8")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_111C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 2)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x196, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_111E1")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_111E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 3)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x199, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_111FA")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_111FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 4)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x19C, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_11213")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_11213")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 5)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x19F, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1122C")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_1122C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 6)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1A2, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_11245")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_11245")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 7)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1A5, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1125E")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_1125E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 0)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1A8, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_11277")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_11277")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 1)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1AB, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_11290")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_11290")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 2)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1AE, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_112A9")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_112A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 3)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1B1, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_112C2")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_112C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 4)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1B4, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_112DB")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_112DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 5)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1B7, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_112F4")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_112F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 6)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1BA, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1130D")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_1130D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 7)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1BD, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_11326")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_11326")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 0)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1C0, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1133F")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_1133F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 1)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1C3, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_11358")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_11358")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 2)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1C6, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_11371")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_11371")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 3)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1C9, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1138A")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_1138A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 4)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1CC, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_113A3")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_113A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 5)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1CF, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_113BC")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_113BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 6)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1D2, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_113D5")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_113D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 7)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1D5, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_113EE")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_113EE")

    Return()

    # Function_40_1118C end

    def Function_41_113EF(): pass

    label("Function_41_113EF")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 0)), scpexpr(EXPR_END)), "loc_1140C")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_1140C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 1)), scpexpr(EXPR_END)), "loc_1141F")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_1141F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 2)), scpexpr(EXPR_END)), "loc_11432")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_11432")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 3)), scpexpr(EXPR_END)), "loc_11445")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_11445")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 4)), scpexpr(EXPR_END)), "loc_11458")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_11458")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 5)), scpexpr(EXPR_END)), "loc_1146B")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_1146B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 6)), scpexpr(EXPR_END)), "loc_1147E")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_1147E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 7)), scpexpr(EXPR_END)), "loc_11491")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_11491")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 0)), scpexpr(EXPR_END)), "loc_114A4")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_114A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 1)), scpexpr(EXPR_END)), "loc_114B7")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_114B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 2)), scpexpr(EXPR_END)), "loc_114CA")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_114CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 3)), scpexpr(EXPR_END)), "loc_114DD")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_114DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 4)), scpexpr(EXPR_END)), "loc_114F0")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_114F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 5)), scpexpr(EXPR_END)), "loc_11503")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_11503")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 6)), scpexpr(EXPR_END)), "loc_11516")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_11516")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9A, 7)), scpexpr(EXPR_END)), "loc_11529")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_11529")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 0)), scpexpr(EXPR_END)), "loc_1153C")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_1153C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 1)), scpexpr(EXPR_END)), "loc_1154F")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_1154F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 2)), scpexpr(EXPR_END)), "loc_11562")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_11562")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 3)), scpexpr(EXPR_END)), "loc_11575")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_11575")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 4)), scpexpr(EXPR_END)), "loc_11588")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_11588")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 5)), scpexpr(EXPR_END)), "loc_1159B")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_1159B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 6)), scpexpr(EXPR_END)), "loc_115AE")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_115AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9B, 7)), scpexpr(EXPR_END)), "loc_115C1")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_115C1")

    Return()

    # Function_41_113EF end

    SaveToFile()

Try(main)
