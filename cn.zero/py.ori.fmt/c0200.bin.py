from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "c0200.bin",                # FileName
        "c0200",                    # MapName
        "c0200",                    # Location
        0x000A,                     # MapIndex
        "ed7100",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x1E,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 10, 0, 9, 0, 10],
    )

    BuildStringList((
        "c0200",                  # 0
        "隆",                     # 1
        "亨利",                   # 2
        "庞斯",                   # 3
        "布利克",                 # 4
        "小桃",                   # 5
        "贝奈特",                 # 6
        "卢威克老人",             # 7
        "爱尔莎",                 # 8
        "蔡特",                   # 9
        "达德利搜查官",           # 10
        "蔡特",                   # 11
        "车１",                   # 12
        "民众１",                 # 13
        "民众２",                 # 14
        "民众３",                 # 15
        "民众４",                 # 16
        "民众５",                 # 17
        "奥斯卡",                 # 18
        "中央广场",               # 19
        "西街",                   # 20
        "行政区",                 # 21
        "住宅街",                 # 22
        "欢乐街",                 # 23
        "东街",                   # 24
        "旧城区",                 # 25
        "港湾区",                 # 26
        "ＩＢＣ",                 # 27
        "站前街道",               # 28
        "后巷",                   # 29
        "乌尔斯拉间道",           # 30
        "东克洛斯贝尔街道",       # 31
        "西克洛斯贝尔街道",       # 32
        "玛因兹山道",             # 33
    ))

    AddCharChip((
        "chr/ch20600.itc",                   # 00
        "chr/ch22200.itc",                   # 01
        "chr/ch20200.itc",                   # 02
        "chr/ch20402.itc",                   # 03
        "chr/ch20700.itc",                   # 04
        "chr/ch34300.itc",                   # 05
        "chr/ch21600.itc",                   # 06
        "chr/ch10400.itc",                   # 07
        "chr/ch02707.itc",                   # 08
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
        "chr/ch00000.itc",                   # 1C
        "chr/ch00000.itc",                   # 1D
    ))

    DeclNpc(449,     0,       610,     90,   257,  0x0, 0,   0,   0,   0,   1,   0,   13,  255,  0)
    DeclNpc(-1000,   0,       610,     90,   257,  0x0, 0,   1,   0,   0,   1,   0,   16,  255,  0)
    DeclNpc(-15119,  0,       5829,    270,  261,  0x0, 0,   2,   0,   0,   2,   0,   17,  255,  0)
    DeclNpc(6570,    -150,    5119,    90,   341,  0x0, 0,   3,   0,   255, 255, 0,   18,  255,  0)
    DeclNpc(5360,    3000,    17690,   0,    257,  0x0, 0,   4,   0,   0,   0,   0,   19,  255,  0)
    DeclNpc(3240,    -300,    4559,    270,  389,  0x0, 0,   5,   0,   0,   0,   0,   20,  255,  0)
    DeclNpc(-14420,  0,       4199,    0,    389,  0x0, 0,   6,   0,   0,   0,   0,   21,  255,  0)
    DeclNpc(5360,    3000,    17690,   0,    261,  0x0, 0,   7,   0,   0,   0,   0,   22,  255,  0)
    DeclNpc(29809,   -4000,   -18139,  225,  404,  0x0, 0,   8,   0,   0,   0,   0,   23,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       180,  453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 24,  11.5,                  15.5,                  2.0,                   49.0,                  [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.1428571492433548,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -5.75,                 -2.2142858505249023,   -0.4000000059604645,   1.0])
    DeclEvent(0x0000, 0, 32,  39.5,                  -19.0,                 -4.5,                  4.0,                   [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -19.75,                9.5,                   0.9000000357627869,    1.0])

    DeclActor(14410,   -6500,   -13590,  1200,    14410,   -5500,   -13590,  0x007C, 0,  11, 0x0000)
    DeclActor(-32070,  -1000,   11050,   1200,    -32070,  0,       11050,   0x007C, 0,  12, 0x0000)

    PlaceName(70.75, 0.0, -7.0, 0x0000, 0x0000, "中央广场")
    PlaceName(5.0, 0.0, -2.5, 0x0000, 0x0000, "西街")
    PlaceName(97.75, 0.0, 82.0, 0x0000, 0x0000, "行政区")
    PlaceName(-56.0, 0.0, 72.0, 0x0000, 0x0000, "住宅街")
    PlaceName(17.0, 0.0, 64.0, 0x0000, 0x0000, "欢乐街")
    PlaceName(152.0, 0.0, -30.0, 0x0000, 0x0000, "东街")
    PlaceName(187.5, 0.0, -85.0, 0x0000, 0x0000, "旧城区")
    PlaceName(180.0, 0.0, 36.0, 0x0000, 0x0000, "港湾区")
    PlaceName(154.0, 0.0, 130.0, 0x0000, 0x0000, "ＩＢＣ")
    PlaceName(82.0, 0.0, -76.0, 0x0000, 0x0000, "站前街道")
    PlaceName(35.0, 0.0, 28.0, 0x0000, 0x0000, "后巷")
    PlaceName(79.0, 0.0, -107.0, 0x0000, 0x0000, "乌尔斯拉间道")
    PlaceName(206.0, 0.0, -16.0, 0x0000, 0x0000, "东克洛斯贝尔街道")
    PlaceName(-46.0, 0.0, -4.0, 0x0000, 0x0000, "西克洛斯贝尔街道")
    PlaceName(-40.0, 0.0, 96.0, 0x0000, 0x0000, "玛因兹山道")
    PlaceName(48.75, 0.0, -21.0, 0x0000, 0x0051, "")
    PlaceName(102.5, 0.0, 5.0, 0x0000, 0x0054, "")
    PlaceName(73.25, 0.0, -29.0, 0x0000, 0x0057, "")
    PlaceName(48.0, 0.0, 8.0, 0x0000, 0x0053, "")
    PlaceName(68.5, 0.0, 32.0, 0x0000, 0x0053, "")
    PlaceName(17.75, 0.0, 3.0, 0x0000, 0x0053, "")
    PlaceName(8.0, 0.0, 24.0, 0x0000, 0x0053, "")
    PlaceName(32.0, 0.0, 56.0, 0x0000, 0x0052, "")
    PlaceName(36.75, 0.0, 43.0, 0x0000, 0x0053, "")
    PlaceName(45.5, 0.0, 34.5, 0x0000, 0x0053, "")
    PlaceName(74.0, 0.0, 105.5, 0x0000, 0x0051, "")
    PlaceName(186.0, 0.0, -30.0, 0x0000, 0x0052, "")
    PlaceName(169.0, 0.0, -120.5, 0x0000, 0x0053, "")
    PlaceName(156.0, 0.0, -102.0, 0x0000, 0x0053, "")
    PlaceName(82.0, 0.0, -19.0, 0x0000, 0x0056, "")

    ScpFunction((
        "Function_0_6EC",          # 00, 0
        "Function_1_7A4",          # 01, 1
        "Function_2_805",          # 02, 2
        "Function_3_866",          # 03, 3
        "Function_4_891",          # 04, 4
        "Function_5_965",          # 05, 5
        "Function_6_A39",          # 06, 6
        "Function_7_B0D",          # 07, 7
        "Function_8_BE1",          # 08, 8
        "Function_9_CB5",          # 09, 9
        "Function_10_11C3",        # 0A, 10
        "Function_11_13EE",        # 0B, 11
        "Function_12_1543",        # 0C, 12
        "Function_13_1679",        # 0D, 13
        "Function_14_1E47",        # 0E, 14
        "Function_15_2345",        # 0F, 15
        "Function_16_2460",        # 10, 16
        "Function_17_2C8B",        # 11, 17
        "Function_18_3921",        # 12, 18
        "Function_19_46D6",        # 13, 19
        "Function_20_4C17",        # 14, 20
        "Function_21_4D9A",        # 15, 21
        "Function_22_4E66",        # 16, 22
        "Function_23_513E",        # 17, 23
        "Function_24_5253",        # 18, 24
        "Function_25_5DF6",        # 19, 25
        "Function_26_6DFE",        # 1A, 26
        "Function_27_7118",        # 1B, 27
        "Function_28_7520",        # 1C, 28
        "Function_29_7A5B",        # 1D, 29
        "Function_30_7E53",        # 1E, 30
        "Function_31_7EEF",        # 1F, 31
        "Function_32_7F0B",        # 20, 32
        "Function_33_7F27",        # 21, 33
    ))


    def Function_0_6EC(): pass

    label("Function_0_6EC")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_72C"),
        (1, "loc_738"),
        (2, "loc_744"),
        (3, "loc_750"),
        (4, "loc_75C"),
        (5, "loc_768"),
        (6, "loc_774"),
        (SWITCH_DEFAULT, "loc_780"),
    )


    label("loc_72C")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_78C")

    label("loc_738")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_78C")

    label("loc_744")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_78C")

    label("loc_750")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_78C")

    label("loc_75C")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_78C")

    label("loc_768")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_78C")

    label("loc_774")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_78C")

    label("loc_780")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_78C")

    label("loc_78C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7A3")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_78C")

    label("loc_7A3")

    Return()

    # Function_0_6EC end

    def Function_1_7A4(): pass

    label("Function_1_7A4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_804")
    OP_95(0xFE, 7000, -300, 610, 6000, 0x0)
    OP_95(0xFE, 7000, 0, -9140, 6000, 0x0)
    OP_95(0xFE, -1000, -10, -9140, 6000, 0x0)
    OP_95(0xFE, -1000, 0, 610, 6000, 0x0)
    Jump("Function_1_7A4")

    label("loc_804")

    Return()

    # Function_1_7A4 end

    def Function_2_805(): pass

    label("Function_2_805")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_865")
    OP_95(0xFE, -5160, 0, 5750, 800, 0x0)
    OP_95(0xFE, -5160, 0, 2280, 800, 0x0)
    OP_95(0xFE, -27380, 0, 2280, 800, 0x0)
    OP_95(0xFE, -27380, 0, 5750, 800, 0x0)
    Jump("Function_2_805")

    label("loc_865")

    Return()

    # Function_2_805 end

    def Function_3_866(): pass

    label("Function_3_866")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_890")
    OP_94(0xFE, 0xFFFF8F3A, 0x9EC, 0xFFFFAD9E, 0x18EC, 0x3E8)
    Sleep(300)
    Jump("Function_3_866")

    label("loc_890")

    Return()

    # Function_3_866 end

    def Function_4_891(): pass

    label("Function_4_891")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_964")
    RunExpression(0x3, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_8D0")
    OP_96(0xFE, 0x1004, 0x0, 0xFFFFF40C, 0x12C, 0x0)
    Jump("loc_95C")

    label("loc_8D0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x28), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_8F8")
    OP_96(0xFE, 0x1004, 0x0, 0xFFFFF3A8, 0x12C, 0x0)
    Jump("loc_95C")

    label("loc_8F8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x3C), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_920")
    OP_96(0xFE, 0x1004, 0x0, 0xFFFFF344, 0x12C, 0x0)
    Jump("loc_95C")

    label("loc_920")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x50), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_948")
    OP_96(0xFE, 0x1004, 0x0, 0xFFFFF2E0, 0x12C, 0x0)
    Jump("loc_95C")

    label("loc_948")

    OP_96(0xFE, 0x1004, 0x0, 0xFFFFF27C, 0x12C, 0x0)

    label("loc_95C")

    Sleep(500)
    Jump("Function_4_891")

    label("loc_964")

    Return()

    # Function_4_891 end

    def Function_5_965(): pass

    label("Function_5_965")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A38")
    RunExpression(0x3, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_9A4")
    OP_96(0xFE, 0xA14, 0x0, 0xFFFFF40C, 0xC8, 0x0)
    Jump("loc_A30")

    label("loc_9A4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x28), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_9CC")
    OP_96(0xFE, 0xA14, 0x0, 0xFFFFF3A8, 0xC8, 0x0)
    Jump("loc_A30")

    label("loc_9CC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x3C), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_9F4")
    OP_96(0xFE, 0xA14, 0x0, 0xFFFFF344, 0xC8, 0x0)
    Jump("loc_A30")

    label("loc_9F4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x50), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_A1C")
    OP_96(0xFE, 0xA14, 0x0, 0xFFFFF2E0, 0xC8, 0x0)
    Jump("loc_A30")

    label("loc_A1C")

    OP_96(0xFE, 0xA14, 0x0, 0xFFFFF27C, 0xC8, 0x0)

    label("loc_A30")

    Sleep(600)
    Jump("Function_5_965")

    label("loc_A38")

    Return()

    # Function_5_965 end

    def Function_6_A39(): pass

    label("Function_6_A39")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_B0C")
    RunExpression(0x3, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_A78")
    OP_96(0xFE, 0x11A8, 0x0, 0xFFFFF1AA, 0x12C, 0x0)
    Jump("loc_B04")

    label("loc_A78")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x28), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_AA0")
    OP_96(0xFE, 0x11DA, 0x0, 0xFFFFF1DC, 0x12C, 0x0)
    Jump("loc_B04")

    label("loc_AA0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x3C), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_AC8")
    OP_96(0xFE, 0x120C, 0x0, 0xFFFFF20E, 0x12C, 0x0)
    Jump("loc_B04")

    label("loc_AC8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x50), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_AF0")
    OP_96(0xFE, 0x123E, 0x0, 0xFFFFF240, 0x12C, 0x0)
    Jump("loc_B04")

    label("loc_AF0")

    OP_96(0xFE, 0x1270, 0x0, 0xFFFFF272, 0x12C, 0x0)

    label("loc_B04")

    Sleep(500)
    Jump("Function_6_A39")

    label("loc_B0C")

    Return()

    # Function_6_A39 end

    def Function_7_B0D(): pass

    label("Function_7_B0D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_BE0")
    RunExpression(0x3, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_B4C")
    OP_96(0xFE, 0xE24, 0x0, 0xFFFFF92A, 0xFA, 0x0)
    Jump("loc_BD8")

    label("loc_B4C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x28), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_B74")
    OP_96(0xFE, 0xDF2, 0x0, 0xFFFFF92A, 0xFA, 0x0)
    Jump("loc_BD8")

    label("loc_B74")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x3C), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_B9C")
    OP_96(0xFE, 0xDC0, 0x0, 0xFFFFF92A, 0xFA, 0x0)
    Jump("loc_BD8")

    label("loc_B9C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x50), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_BC4")
    OP_96(0xFE, 0xD8E, 0x0, 0xFFFFF92A, 0xFA, 0x0)
    Jump("loc_BD8")

    label("loc_BC4")

    OP_96(0xFE, 0xD5C, 0x0, 0xFFFFF92A, 0xFA, 0x0)

    label("loc_BD8")

    Sleep(550)
    Jump("Function_7_B0D")

    label("loc_BE0")

    Return()

    # Function_7_B0D end

    def Function_8_BE1(): pass

    label("Function_8_BE1")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_CB4")
    RunExpression(0x3, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_C20")
    OP_96(0xFE, 0x910, 0x0, 0xFFFFF272, 0xC8, 0x0)
    Jump("loc_CAC")

    label("loc_C20")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x28), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_C48")
    OP_96(0xFE, 0x942, 0x0, 0xFFFFF240, 0xC8, 0x0)
    Jump("loc_CAC")

    label("loc_C48")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x3C), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_C70")
    OP_96(0xFE, 0x974, 0x0, 0xFFFFF20E, 0xC8, 0x0)
    Jump("loc_CAC")

    label("loc_C70")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x50), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_C98")
    OP_96(0xFE, 0x9A6, 0x0, 0xFFFFF1DC, 0xC8, 0x0)
    Jump("loc_CAC")

    label("loc_C98")

    OP_96(0xFE, 0x9D8, 0x0, 0xFFFFF1AA, 0xC8, 0x0)

    label("loc_CAC")

    Sleep(600)
    Jump("Function_8_BE1")

    label("loc_CB4")

    Return()

    # Function_8_BE1 end

    def Function_9_CB5(): pass

    label("Function_9_CB5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6F), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E21")
    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_D80")
    SetChrPos(0x0, 110, 3000, 22760, 180)
    SetChrPos(0x1, 110, 3000, 22760, 180)
    SetChrPos(0x2, 110, 3000, 22760, 180)
    SetChrPos(0x3, 110, 3000, 22760, 180)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D53")
    SetChrPos(0x4, 110, 3000, 22760, 180)
    SetChrPos(0x5, 110, 3000, 22760, 180)
    Jump("loc_D72")

    label("loc_D53")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D72")
    SetChrPos(0x4, 110, 3000, 22760, 180)

    label("loc_D72")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_E21")

    label("loc_D80")

    SetChrPos(0x0, 24460, 0, -8180, 270)
    SetChrPos(0x1, 24460, 0, -8180, 270)
    SetChrPos(0x2, 24460, 0, -8180, 270)
    SetChrPos(0x3, 24460, 0, -8180, 270)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_DF9")
    SetChrPos(0x4, 24460, 0, -8180, 270)
    SetChrPos(0x5, 24460, 0, -8180, 270)
    Jump("loc_E18")

    label("loc_DF9")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E18")
    SetChrPos(0x4, 24460, 0, -8180, 270)

    label("loc_E18")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_E21")

    OP_D0(0x7, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_E91")
    SetChrPos(0x8, 4100, 0, -3260, 270)
    BeginChrThread(0x8, 0, 0, 0)
    SetChrPos(0x9, 2580, 0, -3260, 90)
    BeginChrThread(0x9, 0, 0, 0)
    SetChrPos(0xA, -25120, 0, 4140, 180)
    BeginChrThread(0xA, 0, 0, 3)
    SetChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    Jump("loc_1177")

    label("loc_E91")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_EE3")
    SetChrPos(0x9, 8670, 0, -5340, 270)
    BeginChrThread(0x9, 0, 0, 0)
    SetChrPos(0x8, -1000, 0, 610, 90)
    SetChrPos(0xC, 450, 0, 610, 90)
    BeginChrThread(0xC, 0, 0, 1)
    SetChrFlags(0xF, 0x80)
    Jump("loc_1177")

    label("loc_EE3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_F3B")
    SetChrPos(0x8, 4620, 0, -3570, 315)
    BeginChrThread(0x8, 0, 0, 6)
    SetChrPos(0x9, 3520, 0, -1750, 180)
    BeginChrThread(0x9, 0, 0, 7)
    SetChrPos(0xC, 2420, 0, -3570, 45)
    BeginChrThread(0xC, 0, 0, 8)
    SetChrFlags(0xF, 0x80)
    Jump("loc_1177")

    label("loc_F3B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_F81")
    SetChrPos(0x8, 4100, 0, -3260, 270)
    BeginChrThread(0x8, 0, 0, 4)
    SetChrPos(0xC, 2580, 0, -3260, 90)
    BeginChrThread(0xC, 0, 0, 5)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xF, 0x80)
    Jump("loc_1177")

    label("loc_F81")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_FDA")
    SetChrFlags(0xC, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBD, 2)), scpexpr(EXPR_END)), "loc_FA7")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    Jump("loc_FD5")

    label("loc_FA7")

    SetChrPos(0x8, 4100, 0, -3260, 270)
    BeginChrThread(0x8, 0, 0, 0)
    SetChrPos(0x9, 2580, 0, -3260, 90)
    BeginChrThread(0x9, 0, 0, 0)

    label("loc_FD5")

    Jump("loc_1177")

    label("loc_FDA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_1020")
    SetChrPos(0x8, 4100, 0, -3260, 270)
    BeginChrThread(0x8, 0, 0, 0)
    SetChrPos(0x9, 2580, 0, -3260, 90)
    BeginChrThread(0x9, 0, 0, 0)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xF, 0x80)
    Jump("loc_1177")

    label("loc_1020")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_1038")
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xF, 0x80)
    Jump("loc_1177")

    label("loc_1038")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_1083")
    SetChrPos(0x8, 29770, -4000, -19580, 0)
    BeginChrThread(0x8, 0, 0, 0)
    SetChrPos(0x9, 27640, -4000, -18980, 90)
    BeginChrThread(0x9, 0, 0, 0)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    Jump("loc_1177")

    label("loc_1083")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_10CE")
    SetChrPos(0x8, 29770, -4000, -19580, 0)
    BeginChrThread(0x8, 0, 0, 0)
    SetChrPos(0x9, 27640, -4000, -18980, 90)
    BeginChrThread(0x9, 0, 0, 0)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    Jump("loc_1177")

    label("loc_10CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_111C")
    SetChrFlags(0xF, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1117")
    SetChrPos(0x8, 4100, 0, -3260, 270)
    BeginChrThread(0x8, 0, 0, 0)
    SetChrPos(0x9, 2580, 0, -3260, 90)
    BeginChrThread(0x9, 0, 0, 0)

    label("loc_1117")

    Jump("loc_1177")

    label("loc_111C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_1139")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xF, 0x80)
    Jump("loc_1177")

    label("loc_1139")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_1156")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xF, 0x80)
    Jump("loc_1177")

    label("loc_1156")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_1169")
    SetChrFlags(0xC, 0x80)
    Jump("loc_1177")

    label("loc_1169")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_1177")
    SetChrFlags(0xC, 0x80)

    label("loc_1177")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1188")
    Event(0, 27)

    label("loc_1188")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_119C")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 25)
    Jump("loc_11AB")

    label("loc_119C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 1)), scpexpr(EXPR_END)), "loc_11AB")
    ClearScenarioFlags(0x5C, 1)
    Event(0, 26)

    label("loc_11AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x44, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_11C2")
    SetMapFlags(0x10000000)
    Event(0, 28)

    label("loc_11C2")

    Return()

    # Function_9_CB5 end

    def Function_10_11C3(): pass

    label("Function_10_11C3")

    OP_52(0x10, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapObjFlags(0xD, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_11F9")
    ClearMapObjFlags(0xD, 0x4)

    label("loc_11F9")

    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1211")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_1211")

    SetMapObjFrame(0xFF, "br02", 0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_126E")
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    OP_11(0xFF, 0xCF, 0xB5, 0x23, 0x96, 0x0)
    SetMapObjFrame(0xFF, "sky", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sd_mul", 0x0, 0x1)
    Jump("loc_12DF")

    label("loc_126E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_12BA")
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    OP_11(0xFF, 0xCF, 0xB5, 0x23, 0x96, 0x0)
    SetMapObjFrame(0xFF, "sky", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sd_mul", 0x0, 0x1)
    Jump("loc_12DF")

    label("loc_12BA")

    SetMapObjFrame(0xFF, "sky", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sd_mul", 0x1, 0x1)

    label("loc_12DF")

    ClearMapObjFlags(0x9, 0x10)
    OP_70(0x9, 0x1E)
    OP_1B(0x8, 0xFF, 0xFFFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1301")
    OP_1B(0x8, 0x0, 0x1D)

    label("loc_1301")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1314")
    OP_1B(0x8, 0x0, 0x1D)

    label("loc_1314")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1327")
    OP_1B(0x8, 0x0, 0x1D)

    label("loc_1327")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_133A")
    OP_1B(0x8, 0x0, 0x1D)

    label("loc_133A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_1348")
    OP_1B(0x8, 0x0, 0x1D)

    label("loc_1348")

    OP_1B(0x0, 0xFF, 0xFFFF)
    OP_1B(0x1, 0xFF, 0xFFFF)
    ModifyEventFlags(0, 1, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x43, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x46, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1374")
    OP_1B(0x0, 0x0, 0x1E)
    OP_1B(0x1, 0x0, 0x1F)
    ModifyEventFlags(1, 1, 0x80)

    label("loc_1374")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x1, 0x1)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x1, 0x2)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_139E")
    OP_1B(0x0, 0x0, 0x1E)

    label("loc_139E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x110, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13B1")
    OP_70(0x7, 0x0)
    Jump("loc_13B5")

    label("loc_13B1")

    OP_70(0x7, 0x1E)

    label("loc_13B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x110, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13C8")
    OP_70(0x8, 0x0)
    Jump("loc_13CC")

    label("loc_13C8")

    OP_70(0x8, 0x1E)

    label("loc_13CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_23, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_13E8")
    Jump("loc_13ED")

    label("loc_13E8")

    OP_16(0x3, 0x1D, 0x1, 0x0)

    label("loc_13ED")

    Return()

    # Function_10_11C3 end

    def Function_11_13EE(): pass

    label("Function_11_13EE")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x110, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1514")
    Sound(14, 0, 100, 0)
    OP_71(0x7, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    OP_70(0x7, 0x1E)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    AddSepith(0x0, 80)
    AddSepith(0x1, 80)
    AddSepith(0x2, 80)
    AddSepith(0x3, 80)
    AddSepith(0x4, 80)
    AddSepith(0x5, 80)
    AddSepith(0x6, 80)

    #A0001
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#56I地之耀晶片×８０\x01\x07\x02",

            "#57I水之耀晶片×８０\x01\x07\x02",

            "#58I火之耀晶片×８０\x01\x07\x02",

            "#59I风之耀晶片×８０\x01\x07\x02",

            "#60I时之耀晶片×８０\x01\x07\x02",

            "#61I空之耀晶片×８０\x01\x07\x02",

            "#62I幻之耀晶片×８０\x01\x07\x00",
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x110, 0)
    OP_DE(0x6, 0x0)
    Jump("loc_1531")

    label("loc_1514")


    #A0002
    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "宝箱里什么都没有。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_1531")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_11_13EE end

    def Function_12_1543(): pass

    label("Function_12_1543")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x110, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1630")
    Sound(14, 0, 100, 0)
    OP_71(0x8, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0xA7, 1)"), scpexpr(EXPR_END)), "loc_15C2")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0003
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0xA7),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x110, 1)
    OP_DE(0x6, 0x0)
    Jump("loc_162B")

    label("loc_15C2")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0004
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, 0xA7),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多,",
            scpstr(SCPSTR_CODE_ITEM, 0xA7),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x8, 0x1E, 0x0, 0x0, 0x0)

    label("loc_162B")

    Jump("loc_166D")

    label("loc_1630")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0005
    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "宝箱里什么都没有。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_166D")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_12_1543 end

    def Function_13_1679(): pass

    label("Function_13_1679")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_16EA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1697")
    Call(0, 14)
    Jump("loc_16E5")

    label("loc_1697")


    #C0006
    ChrTalk(
        0xFE,
        (
            "我只是吓了小桃一下，\x01",
            "她就哭着逃走了。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0xFE,
        (
            "嘁，和女孩子玩\x01",
            "果然很麻烦啊～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16E5")

    Jump("loc_1E43")

    label("loc_16EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1737")

    #C0008
    ChrTalk(
        0xFE,
        "噢啦噢啦～喔……！\x02",
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0xFE,
        (
            "慢吞吞的话，\x01",
            "我就要追上来了啊～！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E43")

    label("loc_1737")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_1748")
    Call(0, 15)
    Jump("loc_1E43")

    label("loc_1748")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_185B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1803")
    OP_4B(0xC, 0xFF)

    #C0010
    ChrTalk(
        0xFE,
        (
            "嘿，跳房子可是\x01",
            "我最擅长的啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xFE, 0x10E, 0x1F4)
    Sleep(300)
    OP_9C(0xFE, 0x0, 0x0, 0x0, 0x190, 0xBB8)
    Sleep(300)

    #C0011
    ChrTalk(
        0xFE,
        (
            "嘿，小桃，到你那边啦！\x01",
            "好好跳啊！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xC)

    #C0012
    ChrTalk(
        0xC,
        "……嗯……！\x02",
    )

    CloseMessageWindow()
    OP_4C(0xC, 0xFF)
    SetScenarioFlags(0x0, 0)
    Jump("loc_1856")

    label("loc_1803")


    #C0013
    ChrTalk(
        0xFE,
        "亨利那家伙，今天真是好慢啊～\x02",
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0xFE,
        (
            "嘁，真没办法啊，\x01",
            "只能暂时先和小桃玩一会了～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1856")

    Jump("loc_1E43")

    label("loc_185B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_18C2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1876")
    Call(0, 14)
    Jump("loc_18BD")

    label("loc_1876")


    #C0015
    ChrTalk(
        0xFE,
        "哈～学习什么的太无聊了。\x02",
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0xFE,
        (
            "真羡慕亨利～\x01",
            "修女都不会对他生气呢～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18BD")

    Jump("loc_1E43")

    label("loc_18C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_1976")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18DD")
    Call(0, 14)
    Jump("loc_1971")

    label("loc_18DD")


    #C0017
    ChrTalk(
        0xFE,
        (
            "可恶～不过只是支援科而已，\x01",
            "竟然这么嚣张～！\x02",
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

    label("loc_1971")

    Jump("loc_1E43")

    label("loc_1976")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_19A7")

    #C0018
    ChrTalk(
        0xFE,
        (
            "嘿嘿，今天要去\x01",
            "哪里玩好呢～！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E43")

    label("loc_19A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_1ABA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A7E")
    OP_93(0x8, 0x0, 0x0)

    #C0019
    ChrTalk(
        0xFE,
        (
            "蔡特经常在\x01",
            "这一带巡逻吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0xFE,
        (
            "嘿嘿，不错嘛。\x01",
            "今天也带着我一起吧～！\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x12,
        "#1200F呜噜噜噜噜……\x02",
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x103,
        (
            "#0200F（看我心情吧，\x01",
            "  它这样说。）\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x101,
        "#0000F（简直就是立场颠倒了啊……）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1AB5")

    label("loc_1A7E")


    #C0024
    ChrTalk(
        0xFE,
        (
            "蔡特经常在这一带\x01",
            "巡逻啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0xFE,
        "警犬吗～好帅啊～！\x02",
    )

    CloseMessageWindow()

    label("loc_1AB5")

    Jump("loc_1E43")

    label("loc_1ABA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_1BCB")
    SetScenarioFlags(0x90, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B6E")

    #C0026
    ChrTalk(
        0xFE,
        (
            "蔡特真是又大\x01",
            "又帅气～！\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0xFE,
        "那种从容不迫的态度真让人着迷呢～！\x02",
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x101,
        "#0000F蔡特完全被当成英雄了呢……\x02",
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x102,
        (
            "#0100F对男孩子来说，\x01",
            "也许是那样的吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1BC6")

    label("loc_1B6E")

    OP_93(0x8, 0x0, 0x0)

    #C0030
    ChrTalk(
        0xFE,
        "蔡特～看这边啊～！\x02",
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0xFE,
        "哇噢噢，锋利的獠牙啊～！\x02",
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 1700, 0x8, 0x9, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Sleep(1000)

    label("loc_1BC6")

    Jump("loc_1E43")

    label("loc_1BCB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_1CDC")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C31")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1BF3")
    Call(0, 14)
    Jump("loc_1C2C")

    label("loc_1BF3")


    #C0032
    ChrTalk(
        0xFE,
        (
            "警察什么的\x01",
            "果然没用啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0xFE,
        "要说可靠，还属游击士！\x02",
    )

    CloseMessageWindow()

    label("loc_1C2C")

    Jump("loc_1CD7")

    label("loc_1C31")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CAC")

    #C0034
    ChrTalk(
        0xFE,
        "啊，是支援科的哥哥姐姐。\x02",
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0xFE,
        "……哼，工作加油啊！\x02",
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x101,
        (
            "#0000F哈哈……\x01",
            "（似乎稍微被认可了一点呢。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1CD7")

    label("loc_1CAC")


    #C0037
    ChrTalk(
        0xFE,
        (
            "支援科的哥哥姐姐，\x01",
            "……工作要加油啊！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1CD7")

    Jump("loc_1E43")

    label("loc_1CDC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_1CEA")
    Jump("loc_1E43")

    label("loc_1CEA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_1CF8")
    Jump("loc_1E43")

    label("loc_1CF8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_1D2F")

    #C0038
    ChrTalk(
        0xFE,
        (
            "喝啊～喝啊～！\x01",
            "最强的游击士登场～！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E43")

    label("loc_1D2F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_1E43")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E14")

    #C0039
    ChrTalk(
        0xFE,
        "啊，是那时的哥哥！\x02",
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0xFE,
        (
            "什么啊～你这么快\x01",
            "就开始巡逻了啊～？\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x101,
        (
            "#0006F……我说，\x01",
            "警察可是很忙的。\x02\x03",

            "#0000F先不说这个，你以后\x01",
            "可别再做那么莽撞的事啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0xFE,
        "呜……\x02",
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0xFE,
        (
            "哼、哼。\x01",
            "那种事～不用你管～！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1E43")

    label("loc_1E14")


    #C0044
    ChrTalk(
        0xFE,
        (
            "看着看着～我可是\x01",
            "亚里欧斯·马克莱因啊～！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E43")

    TalkEnd(0xFE)
    Return()

    # Function_13_1679 end

    def Function_14_1E47(): pass

    label("Function_14_1E47")

    OP_4B(0x8, 0xFF)
    OP_4B(0x9, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_1ED8")
    TurnDirection(0x8, 0x9, 0)
    TurnDirection(0x9, 0x8, 0)

    #C0045
    ChrTalk(
        0x8,
        (
            "什么嘛～\x01",
            "只不过是捉迷藏而已啊～\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x9,
        (
            "所以说，是隆\x01",
            "做得太过分了啊～！\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x9,
        (
            "明天可要好好\x01",
            "去向人家道歉哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2336")

    label("loc_1ED8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_1F6D")
    TurnDirection(0x8, 0x9, 0)
    TurnDirection(0x9, 0x8, 0)

    #C0048
    ChrTalk(
        0x8,
        (
            "今天要去主日学校啊～\x01",
            "嘁，不如逃课好了～\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x9,
        (
            "不行啊，隆。\x01",
            "必须认真去上课啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x9,
        (
            "好啦，我们叫上小桃，\x01",
            "赶快走吧！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2336")

    label("loc_1F6D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_20CB")
    TurnDirection(0x8, 0x9, 0)
    TurnDirection(0x9, 0x8, 0)

    #C0051
    ChrTalk(
        0x8,
        (
            "我说，亨利～\x01",
            "我们去市外看看吧～\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x8,
        (
            "嘿嘿，爸爸最近\x01",
            "很忙呢。\x01",
            "所以现在溜出去完全不用担心会被发现！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0053
    ChrTalk(
        0x9,
        "那、那个，隆～\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0054
    ChrTalk(
        0x8,
        "嗯～怎么了～……\x02",
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x101,
        (
            "#0001F你·们·两·个～……\x01",
            "小孩子怎么可以自己\x01",
            "跑到市外去呢！？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x0, 500)

    #C0056
    ChrTalk(
        0x8,
        (
            "呜哇，是支援科的哥哥！\x01",
            "不好～……！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x9, 0)
    Jump("loc_2336")

    label("loc_20CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_20D9")
    Jump("loc_2336")

    label("loc_20D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_2336")
    TurnDirection(0x8, 0x0, 0)
    TurnDirection(0x9, 0x0, 0)

    #C0057
    ChrTalk(
        0x8,
        "啊，是支援科的大哥哥。\x02",
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x8,
        "嘘嘘嘘～你们落后了啊～！\x02",
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

    #C0059
    ChrTalk(
        0x101,
        "#0005F哎……？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_21E0")

    #C0060
    ChrTalk(
        0x9,
        (
            "其实，我们昨天\x01",
            "捡到了一只迷路的小猫……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2211")

    label("loc_21E0")


    #C0061
    ChrTalk(
        0x9,
        (
            "其实，昨天和你们说过的\x01",
            "迷路小猫的那件事……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2211")


    #C0062
    ChrTalk(
        0x9,
        (
            "之后，由偶然路过的\x01",
            "游击士大姐姐\x01",
            "帮我们找到了它的主人！\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x8,
        (
            "她和一个黑发的哥哥共同行动，\x01",
            "转眼之间就把事情解决了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x8,
        (
            "嘿嘿嘿，不愧是游击士。\x01",
            "虽然是女生，但也那么厉害！\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x102,
        "#0105F那、那两个人……\x02",
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x103,
        (
            "#0200F是艾丝蒂尔\x01",
            "和约修亚呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x104,
        "#0303F被、被他们抢先了一步吗……\x02",
    )

    CloseMessageWindow()
    OP_93(0x8, 0x10E, 0x0)
    OP_93(0x9, 0x5A, 0x0)

    label("loc_2336")

    SetScenarioFlags(0x0, 0)
    SetScenarioFlags(0x0, 1)
    OP_4C(0x8, 0xFF)
    OP_4C(0x9, 0xFF)
    Return()

    # Function_14_1E47 end

    def Function_15_2345(): pass

    label("Function_15_2345")

    OP_4B(0x8, 0xFF)
    OP_4B(0xC, 0xFF)
    TurnDirection(0x8, 0xC, 0)
    TurnDirection(0xC, 0x8, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_23F3")

    #C0068
    ChrTalk(
        0x8,
        (
            "果然还是三个人\x01",
            "一起玩比较有趣啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x8,
        (
            "好，小桃，从今以后，\x01",
            "你就来和我们一起玩吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0xC,
        "……………………！\x02",
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0xC,
        "嗯！一起玩……！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2446")

    label("loc_23F3")


    #C0072
    ChrTalk(
        0x8,
        (
            "嘿，小桃，我要传给你了啊！\x01",
            "好好接住哦！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xC)

    #C0073
    ChrTalk(
        0xC,
        "嗯……！\x02",
    )

    CloseMessageWindow()

    label("loc_2446")

    OP_93(0x8, 0x13B, 0x0)
    OP_93(0xC, 0x2D, 0x0)
    SetScenarioFlags(0x0, 0)
    OP_4C(0x8, 0xFF)
    OP_4C(0xC, 0xFF)
    Return()

    # Function_15_2345 end

    def Function_16_2460(): pass

    label("Function_16_2460")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_24A4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_247E")
    Call(0, 14)
    Jump("loc_249F")

    label("loc_247E")


    #C0074
    ChrTalk(
        0xFE,
        (
            "隆，明天一定要\x01",
            "好好道歉啊～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_249F")

    Jump("loc_2C87")

    label("loc_24A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_24F9")
    OP_93(0xFE, 0x10E, 0x0)

    #C0075
    ChrTalk(
        0xFE,
        "等、等一下啦，隆～！\x02",
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0xFE,
        "那样追赶的话，小桃太可怜了啊～！\x02",
    )

    CloseMessageWindow()
    Jump("loc_2C87")

    label("loc_24F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_255A")

    #C0077
    ChrTalk(
        0xFE,
        "我们今天三个人在一起玩。\x02",
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0xFE,
        (
            "嘿嘿嘿……\x01",
            "比起两个人，还是三个人一起玩更开心。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C87")

    label("loc_255A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_2568")
    Jump("loc_2C87")

    label("loc_2568")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_25CD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2583")
    Call(0, 14)
    Jump("loc_25C8")

    label("loc_2583")


    #C0079
    ChrTalk(
        0xFE,
        "今天我们要去主日学校。\x02",
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0xFE,
        (
            "隆总是想偷懒逃课，\x01",
            "真是令人头疼啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_25C8")

    Jump("loc_2C87")

    label("loc_25CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_2645")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_25E8")
    Call(0, 14)
    Jump("loc_2640")

    label("loc_25E8")


    #C0081
    ChrTalk(
        0xFE,
        (
            "对、对不起，之前明明\x01",
            "在危机时刻被你们所救……\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0xFE,
        (
            "我一定会好好\x01",
            "说说隆这家伙的～！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2640")

    Jump("loc_2C87")

    label("loc_2645")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_2733")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2707")

    #C0083
    ChrTalk(
        0xFE,
        (
            "呼，因为逃课没去主日学校，\x01",
            "我被爸爸狠狠教训了一顿。\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0xFE,
        (
            "之前偷跑进地下空间的时候，\x01",
            "他也对我发了很大的脾气……\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0xFE,
        (
            "因为总和隆在一起玩，\x01",
            "所以经常把爸爸给惹怒呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_272E")

    label("loc_2707")


    #C0086
    ChrTalk(
        0xFE,
        (
            "隆，你也必须\x01",
            "稍微反省一下啊……！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_272E")

    Jump("loc_2C87")

    label("loc_2733")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_282A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_27CD")

    #C0087
    ChrTalk(
        0xFE,
        (
            "隆虽然总在嘴上\x01",
            "说看不起警察……\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0xFE,
        "但心里其实是有些憧憬的。\x02",
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0xFE,
        (
            "嘿嘿嘿……因为在警察\x01",
            "之中，也有像各位这么\x01",
            "帅气的人啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2825")

    label("loc_27CD")


    #C0090
    ChrTalk(
        0xFE,
        (
            "隆他其实是\x01",
            "有点憧憬警察这个职业的。\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0xFE,
        (
            "但因为性格太过固执，\x01",
            "所以嘴上绝对不认输。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2825")

    Jump("loc_2C87")

    label("loc_282A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_2A3A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2937")

    #C0092
    ChrTalk(
        0xFE,
        (
            "各位，之前多亏\x01",
            "你们的蔡特救了隆……\x01",
            "真是十分感谢！\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0xFE,
        (
            "话说回来，蔡特\x01",
            "真是太帅了啊！\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0xFE,
        (
            "竟然能饲养这种警犬，\x01",
            "各位真是太厉害了！\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0x104,
        (
            "#0300F哈哈，要说是饲养的话，\x01",
            "好像稍微有些不妥呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0x103,
        (
            "#0200F因为留在支援科\x01",
            "完全都是蔡特自己的意志。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2A35")

    label("loc_2937")

    OP_93(0xFE, 0x5A, 0x0)

    #C0097
    ChrTalk(
        0xFE,
        "是这样啊……\x02",
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    #C0098
    ChrTalk(
        0xFE,
        (
            "啊，对了！隆～不赶快去大圣堂没问题吗～？\x01",
            "主日学校的课已经开始了哦～！\x02",
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

    #C0099
    ChrTalk(
        0x101,
        "#0012F逃课可是不行的哦……！\x02",
    )

    CloseMessageWindow()

    label("loc_2A35")

    Jump("loc_2C87")

    label("loc_2A3A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_2B3A")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2AE7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A62")
    Call(0, 14)
    Jump("loc_2AE2")

    label("loc_2A62")


    #C0100
    ChrTalk(
        0xFE,
        "游击士大姐姐真是太厉害了！\x02",
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0xFE,
        (
            "『和猫有关的委托我早就习惯啦』\x01",
            "——她是这么说的！\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x102,
        (
            "#0100F是、是吗。\x01",
            "不愧是游击士啊……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2AE2")

    Jump("loc_2B35")

    label("loc_2AE7")


    #C0103
    ChrTalk(
        0xFE,
        (
            "各位，昨天真是\x01",
            "太感谢了。\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0xFE,
        (
            "如果以后有什么事情，\x01",
            "还会再和各位联络哦！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B35")

    Jump("loc_2C87")

    label("loc_2B3A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_2B48")
    Jump("loc_2C87")

    label("loc_2B48")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_2B56")
    Jump("loc_2C87")

    label("loc_2B56")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_2B99")

    #C0105
    ChrTalk(
        0xFE,
        "呼、呼……\x02",
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0xFE,
        (
            "真是的～隆总是\x01",
            "这么不守规则～！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C87")

    label("loc_2B99")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_2C87")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C66")

    #C0107
    ChrTalk(
        0xFE,
        (
            "啊，支援科的各位……\x01",
            "之前真是太感谢了。\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0xFE,
        (
            "我们之后都被爸爸\x01",
            "狠狠训斥了一顿呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0x101,
        (
            "#0000F哈哈哈，是吗？\x01",
            "不过，你们能平安无事就好啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0xFE,
        (
            "嘿嘿嘿……各位工作\x01",
            "要加油啊！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2C87")

    label("loc_2C66")


    #C0111
    ChrTalk(
        0xFE,
        (
            "等一下啊，隆～\x01",
            "你犯规啦～！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C87")

    TalkEnd(0xFE)
    Return()

    # Function_16_2460 end

    def Function_17_2C8B(): pass

    label("Function_17_2C8B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_2D90")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D38")

    #C0112
    ChrTalk(
        0xFE,
        (
            "嗯～今天的夕阳\x01",
            "格外引人哀愁啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0xFE,
        (
            "克洛斯贝尔大圣堂的\x01",
            "钟声差不多也该响起了……\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0xFE,
        (
            "以夕阳为背景，拍摄\x01",
            "一张大圣堂的照片或许也不错呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2D8B")

    label("loc_2D38")


    #C0115
    ChrTalk(
        0xFE,
        "今天的夕阳很特别呢。\x02",
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0xFE,
        (
            "在黄昏中耸立的大圣堂，\x01",
            "我觉得这种照片应该会很不错。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D8B")

    Jump("loc_391D")

    label("loc_2D90")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_2DEE")

    #C0117
    ChrTalk(
        0xFE,
        (
            "昨天在港湾区那边\x01",
            "发生了枪战吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0xFE,
        (
            "真恐怖啊，竟然在\x01",
            "那种办公地区发生……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_391D")

    label("loc_2DEE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_2EC2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E63")

    #C0119
    ChrTalk(
        0xFE,
        (
            "阿尔摩利卡村那边\x01",
            "也有个遗迹哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0xFE,
        (
            "我最近迷上了拍摄风景照片，\x01",
            "下次准备去那里看看。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2EBD")

    label("loc_2E63")


    #C0121
    ChrTalk(
        0xFE,
        (
            "克洛斯贝尔地区\x01",
            "还有很多不为人知的遗迹呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0xFE,
        (
            "只在城市中生活，\x01",
            "就不会知道这些呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2EBD")

    Jump("loc_391D")

    label("loc_2EC2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_302E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2FB9")

    #C0123
    ChrTalk(
        0xFE,
        (
            "玛因兹山道中段的那个遗迹\x01",
            "是非常不错的摄影场所呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0xFE,
        (
            "我为了拍摄风景照片，\x01",
            "经常去各处游走……\x01",
            "但还是感觉那里是最棒的地方。\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0xFE,
        (
            "在弥漫着寂静氛围的环境下，\x01",
            "一片庄严肃穆的废墟映入眼帘。\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0xFE,
        "……可惜就是没能进去啊。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3029")

    label("loc_2FB9")


    #C0127
    ChrTalk(
        0xFE,
        (
            "位于玛因兹山道中段的那片遗迹\x01",
            "静谧祥和，实在是个世外桃源啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0xFE,
        (
            "可惜警备队设置了防护措施，\x01",
            "所以没能进去。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3029")

    Jump("loc_391D")

    label("loc_302E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_30FF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_30B9")

    #C0129
    ChrTalk(
        0xFE,
        (
            "在纪念庆典期间，\x01",
            "我拍了很多好照片哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0xFE,
        (
            "到处都是热热闹闹的欢声笑语……\x01",
            "哎呀～明年的庆典也很让人期待啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_30FA")

    label("loc_30B9")


    #C0131
    ChrTalk(
        0xFE,
        (
            "明年的纪念庆典\x01",
            "能拍到怎样的照片呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0xFE,
        "哎呀～真是期待啊。\x02",
    )

    CloseMessageWindow()

    label("loc_30FA")

    Jump("loc_391D")

    label("loc_30FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_320E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_31BE")

    #C0133
    ChrTalk(
        0xFE,
        (
            "在克洛斯贝尔地区中残存着\x01",
            "好几处中世纪的遗迹。\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0xFE,
        (
            "但大多数都没有记录在\x01",
            "旅游指南中，\x01",
            "所以几乎都没人知道。\x02",
        )
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0xFE,
        (
            "……呵，不过正因如此，\x01",
            "探索它们才是一件乐事啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3209")

    label("loc_31BE")


    #C0136
    ChrTalk(
        0xFE,
        (
            "克洛斯贝尔地区中残存着\x01",
            "好几处中世纪的遗迹。\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0xFE,
        "不过几乎都无人知晓。\x02",
    )

    CloseMessageWindow()

    label("loc_3209")

    Jump("loc_391D")

    label("loc_320E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_3274")

    #C0138
    ChrTalk(
        0xFE,
        (
            "今天也是个好天气啊，\x01",
            "是绝佳的游玩日呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0xFE,
        (
            "好～！带上相机，\x01",
            "找个地方去转转好了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_391D")

    label("loc_3274")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_32CE")

    #C0140
    ChrTalk(
        0xFE,
        (
            "伊安律师最近一段时间\x01",
            "好像特别忙呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0xFE,
        (
            "他说最近的骚乱\x01",
            "好像增多了呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_391D")

    label("loc_32CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_3402")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_336E")

    #C0142
    ChrTalk(
        0xFE,
        (
            "顺着这条路一直走下去，\x01",
            "就是西克洛斯贝尔街道了。\x02",
        )
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0xFE,
        (
            "那里是通往帝国的国境门，\x01",
            "贝尔加德门。\x02",
        )
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0xFE,
        (
            "运输卡车之类的\x01",
            "经常从那里走呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_33FD")

    label("loc_336E")


    #C0145
    ChrTalk(
        0xFE,
        (
            "顺着这条路一直走下去，\x01",
            "就是西克洛斯贝尔街道了。\x02",
        )
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0xFE,
        (
            "不过那边除了贝尔加德门之外，\x01",
            "也就只剩警察学校了……\x01",
            "只有一些运输卡车才会走那条路呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_33FD")

    Jump("loc_391D")

    label("loc_3402")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_3542")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_34BC")

    #C0147
    ChrTalk(
        0xFE,
        (
            "导力相机之中，\x01",
            "也分各种品牌与规格哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0xFE,
        (
            "我比较中意的是\x01",
            "ＺＣＦ制造的系列相机。\x02",
        )
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0xFE,
        (
            "并没有什么标新立异的复杂构造，\x01",
            "不管是初学者还是高手，都能轻松使用。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_353D")

    label("loc_34BC")


    #C0150
    ChrTalk(
        0xFE,
        (
            "我比较中意的是\x01",
            "ＺＣＦ制造的系列相机。\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0xFE,
        (
            "这个系列的相机\x01",
            "从１１８０年时期一直延续到现在，\x01",
            "至今仍有很多专门收藏它们的人呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_353D")

    Jump("loc_391D")

    label("loc_3542")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_3649")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_35DA")

    #C0152
    ChrTalk(
        0xFE,
        (
            "你知道吗？\x01",
            "在乌尔斯拉间道的中段部分\x01",
            "有个遗迹呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0xFE,
        "好像是在中世纪时期建造的塔。\x02",
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0xFE,
        (
            "嗯～一定要用相机\x01",
            "把它拍下来啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3644")

    label("loc_35DA")


    #C0155
    ChrTalk(
        0xFE,
        (
            "在乌尔斯拉间道的中段部分\x01",
            "有一座中世纪时期建造的塔。\x02",
        )
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0xFE,
        (
            "对喜欢摄影的人来说，\x01",
            "绝对是个必拍的场所啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3644")

    Jump("loc_391D")

    label("loc_3649")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_3755")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_36EA")

    #C0157
    ChrTalk(
        0xFE,
        (
            "旧城区在不久前发生的那个事件，\x01",
            "连警察都介入进来了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0xFE,
        "……真是少见呢。\x02",
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0xFE,
        (
            "旧城区那种地方，\x01",
            "平时都不会有警察去那里巡逻的。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3750")

    label("loc_36EA")


    #C0160
    ChrTalk(
        0xFE,
        (
            "最近这段时间，在警察局里\x01",
            "好像也出现了一些行动奇特的人呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0xFE,
        (
            "身为一名市民，\x01",
            "稍微有点感兴趣啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3750")

    Jump("loc_391D")

    label("loc_3755")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_384E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_37EF")

    #C0162
    ChrTalk(
        0xFE,
        (
            "刚才有个穿西装、戴眼镜的人\x01",
            "经过那里了。\x02",
        )
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0xFE,
        (
            "他好像还佩戴着警察\x01",
            "的徽章呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0xFE,
        (
            "警察来这种安静平和\x01",
            "的地方能有什么事啊？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3849")

    label("loc_37EF")


    #C0165
    ChrTalk(
        0xFE,
        (
            "说起来，我最近好像\x01",
            "经常能见到那个人呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0xFE,
        (
            "警察来西街这种地方\x01",
            "究竟能有什么事呢？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3849")

    Jump("loc_391D")

    label("loc_384E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_391D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_38EC")

    #C0167
    ChrTalk(
        0xFE,
        (
            "最近，拥有导力车的人\x01",
            "好像也增多了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0xFE,
        (
            "对我这种爱好拍照的人来说，\x01",
            "开着车就能够轻松前往郊外这点，\x01",
            "真是有着很大的吸引力呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_391D")

    label("loc_38EC")


    #C0169
    ChrTalk(
        0xFE,
        (
            "真想有辆导力车啊……\x01",
            "要是能再便宜点就好了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_391D")

    TalkEnd(0xFE)
    Return()

    # Function_17_2C8B end

    def Function_18_3921(): pass

    label("Function_18_3921")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_39B5")
    Jump("loc_39FF")

    label("loc_39B5")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_39D5")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_39FF")

    label("loc_39D5")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_39F5")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_39FF")

    label("loc_39F5")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_39FF")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_3B14")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3AB1")

    #C0170
    ChrTalk(
        0xFE,
        (
            "噢，太阳都已经下山了啊……\x01",
            "差不多也该回去了。\x02",
        )
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0xFE,
        (
            "自治州议会\x01",
            "总算是结束了。\x02",
        )
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0xFE,
        "暂时应该会平静一阵子了吧。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3B0F")

    label("loc_3AB1")


    #C0173
    ChrTalk(
        0xFE,
        "自治州议会还是像以往一样啊。\x02",
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0xFE,
        (
            "真是的，无话可说了。\x01",
            "克洛斯贝尔最后\x01",
            "还是什么都没有变。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3B0F")

    Jump("loc_46CE")

    label("loc_3B14")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_3BF2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3BA4")

    #C0175
    ChrTalk(
        0xFE,
        (
            "最近这段时间，市内的\x01",
            "失踪人口好像增多了？\x02",
        )
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0xFE,
        (
            "黑手党仍然在\x01",
            "不断引发事端……\x01",
            "怎么全都是一堆令人不愉快的事情啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3BED")

    label("loc_3BA4")


    #C0177
    ChrTalk(
        0xFE,
        "经济景气虽然是好事……\x02",
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0xFE,
        (
            "但最近的治安好差啊，\x01",
            "到底是怎么回事呢？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3BED")

    Jump("loc_46CE")

    label("loc_3BF2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_3CD4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3C88")

    #C0179
    ChrTalk(
        0xFE,
        "克洛斯贝尔时代周刊临时休刊！？\x02",
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0xFE,
        "怎么会……我的早餐伴侣啊……\x02",
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0xFE,
        (
            "这样的话，岂不是连议会的情况\x01",
            "都无法了解了吗！？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3CCF")

    label("loc_3C88")


    #C0182
    ChrTalk(
        0xFE,
        (
            "克洛斯贝尔时代周刊\x01",
            "竟然会临时休刊……\x02",
        )
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0xFE,
        "究竟发生什么事了啊……\x02",
    )

    CloseMessageWindow()

    label("loc_3CCF")

    Jump("loc_46CE")

    label("loc_3CD4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_3DB5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D65")

    #C0184
    ChrTalk(
        0xFE,
        (
            "听说，现在正在市政厅召开的预算会议\x01",
            "好像又出现大争吵了。\x02",
        )
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0xFE,
        (
            "每年都会出现如此状况，\x01",
            "就不能想个办法解决一下吗……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3DB0")

    label("loc_3D65")


    #C0186
    ChrTalk(
        0xFE,
        (
            "预算会议和往常一样，好像又开始吵起来了。\x01",
            "但这也是没办法避免的事情吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3DB0")

    Jump("loc_46CE")

    label("loc_3DB5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_3F67")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3EE3")

    #C0187
    ChrTalk(
        0xFE,
        (
            "自治州议会的\x01",
            "预算审议会议终于开始了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0xFE,
        (
            "预算审议会议将会对克洛斯贝尔\x01",
            "一年的预算进行决断。\x02",
        )
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0xFE,
        (
            "是直接关系到米拉的会议哦……\x01",
            "由于议题涉及到派系、专权乃至于议员的\x01",
            "虚荣心等问题，所以每次都会有激烈的争执。\x02",
        )
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0xFE,
        "今年将会怎么样呢……\x02",
    )

    CloseMessageWindow()

    #C0191
    ChrTalk(
        0xFE,
        (
            "算啦，反正我们也只能\x01",
            "随它去啦。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3F62")

    label("loc_3EE3")


    #C0192
    ChrTalk(
        0xFE,
        (
            "预算会议每年都会\x01",
            "出现激烈的争吵。\x02",
        )
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0xFE,
        (
            "算啦，说到底那都是议员们的派系争斗，\x01",
            "身为普通市民，所能做的\x01",
            "也只是站在远处观望啦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3F62")

    Jump("loc_46CE")

    label("loc_3F67")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_400C")

    #C0194
    ChrTalk(
        0xFE,
        (
            "麦克道尔市长要在\x01",
            "本任期之后退休，是真的吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0xFE,
        (
            "他可是担任市长一职\x01",
            "长达十年以上的人啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0xFE,
        (
            "他是个很有见识的明智之人，\x01",
            "所以真不希望他退休啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_46CE")

    label("loc_400C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_4185")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4102")

    #C0197
    ChrTalk(
        0xFE,
        (
            "爱普斯泰恩财团推行的\x01",
            "那个导力网络计划，\x01",
            "ＩＢＣ好像也进行了相当大额的投资呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0xFE,
        (
            "听说ＩＢＣ正在推行一个项目，\x01",
            "其内容是通过导力网络\x01",
            "将他们在大陆的各个分行相连接。\x02",
        )
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0xFE,
        (
            "不愧是ＩＢＣ……\x01",
            "事业的规模真是让人望尘莫及。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4180")

    label("loc_4102")


    #C0200
    ChrTalk(
        0xFE,
        (
            "听说，推行导力网络计划，\x01",
            "需要使用相当庞大的资金……\x02",
        )
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0xFE,
        (
            "为了将来考虑，而不惜花费如此巨资，\x01",
            "ＩＢＣ的行事风格就是大气啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4180")

    Jump("loc_46CE")

    label("loc_4185")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_428A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4215")

    #C0202
    ChrTalk(
        0xFE,
        (
            "说起来，最近都\x01",
            "看不到克洛斯贝尔时代周刊\x01",
            "的那个记者小姐了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0203
    ChrTalk(
        0xFE,
        (
            "那个人原来经常为收集新闻素材\x01",
            "而来到这一带呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4285")

    label("loc_4215")


    #C0204
    ChrTalk(
        0xFE,
        (
            "克洛斯贝尔时代周刊的那位记者小姐\x01",
            "以前经常会来这一带呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0205
    ChrTalk(
        0xFE,
        (
            "据说她跟踪了警察，\x01",
            "从而掌握了不少独家新闻呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4285")

    Jump("loc_46CE")

    label("loc_428A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_4339")

    #C0206
    ChrTalk(
        0xFE,
        (
            "每年，当纪念庆典临近时，\x01",
            "街上都会这么繁华热闹呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0207
    ChrTalk(
        0xFE,
        (
            "而且……你知道吗？\x01",
            "今年可是自治州创立的七十周年哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0208
    ChrTalk(
        0xFE,
        (
            "所以今年的庆典一定会比往年\x01",
            "更加华丽盛大啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_46CE")

    label("loc_4339")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_43C1")

    #C0209
    ChrTalk(
        0xFE,
        (
            "听说警备队因为什么\x01",
            "事情而出动了……\x02",
        )
    )

    CloseMessageWindow()

    #C0210
    ChrTalk(
        0xFE,
        "国境那边出了什么事吗……\x02",
    )

    CloseMessageWindow()

    #C0211
    ChrTalk(
        0xFE,
        (
            "但却没有听说过相关新闻，\x01",
            "这点让人有些在意呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_46CE")

    label("loc_43C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_442F")

    #C0212
    ChrTalk(
        0xFE,
        (
            "嗯，这里的牛角面包\x01",
            "真是美味绝品呀～\x02",
        )
    )

    CloseMessageWindow()

    #C0213
    ChrTalk(
        0xFE,
        (
            "如果和超浓咖啡一起享用的话，\x01",
            "那就更是回味无穷了～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_46CE")

    label("loc_442F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_4508")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_44C9")

    #C0214
    ChrTalk(
        0xFE,
        (
            "对了，我听说游击士协会那里\x01",
            "好像有新人到任了哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0215
    ChrTalk(
        0xFE,
        (
            "会是怎么样的人呢？\x01",
            "游击士全都是一些很厉害的家伙，\x01",
            "所以我很感兴趣呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4503")

    label("loc_44C9")


    #C0216
    ChrTalk(
        0xFE,
        (
            "刚刚来克洛斯贝尔赴任\x01",
            "的游击士……\x01",
            "到底是怎样的人呢？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4503")

    Jump("loc_46CE")

    label("loc_4508")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_4583")

    #C0217
    ChrTalk(
        0xFE,
        (
            "克洛斯贝尔时代周刊社\x01",
            "有个很能干的女记者。\x02",
        )
    )

    CloseMessageWindow()

    #C0218
    ChrTalk(
        0xFE,
        (
            "时常能挖掘到一些\x01",
            "惊人的爆炸性独家消息。\x01",
            "也算是个名人了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_46CE")

    label("loc_4583")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_46CE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_464B")

    #C0219
    ChrTalk(
        0xFE,
        "游击士协会，又立下了功劳吗……\x02",
    )

    CloseMessageWindow()

    #C0220
    ChrTalk(
        0xFE,
        (
            "将小孩子救出来，\x01",
            "真不愧是游击士啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0xFE,
        (
            "不过……市里这种薄弱的\x01",
            "管理体制实在是让人无法原谅啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0222
    ChrTalk(
        0xFE,
        (
            "希望有关人员能\x01",
            "好好想些对策啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_46CE")

    label("loc_464B")


    #C0223
    ChrTalk(
        0xFE,
        (
            "不知为何，克洛斯贝尔市\x01",
            "总是有很多事件和事故呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0224
    ChrTalk(
        0xFE,
        (
            "虽然游击士协会的人\x01",
            "基本都能解决……\x01",
            "但希望市里的管理人员也能反省一下啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_46CE")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_18_3921 end

    def Function_19_46D6(): pass

    label("Function_19_46D6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x1, 0x1)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x1, 0x2)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_490D")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x1, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4878")

    #C0225
    ChrTalk(
        0x101,
        (
            "#0000F可以稍微打扰一下吗？\x02\x03",

            "请问你有没有\x01",
            "养猫呢？\x01",
            "是一只很小的幼猫。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0226
    ChrTalk(
        0xFE,
        "不太明白……\x02",
    )

    CloseMessageWindow()

    #C0227
    ChrTalk(
        0xFE,
        (
            "你们要送我小猫吗？\x01",
            "……虽然也很想养……\x02",
        )
    )

    CloseMessageWindow()

    #C0228
    ChrTalk(
        0xFE,
        (
            "啊，不过我家\x01",
            "还要做买卖，\x01",
            "应该不行啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0229
    ChrTalk(
        0x101,
        (
            "#0006F抱歉……\x01",
            "我是正在带小猫\x01",
            "寻找主人呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0230
    ChrTalk(
        0xFE,
        "是吗……\x02",
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0xFE,
        (
            "嗯，那很不错啊。\x01",
            "赶快帮它找到主人吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0232
    ChrTalk(
        0x102,
        "#0100F这次看来是白跑了一趟呢。\x02",
    )

    CloseMessageWindow()
    OP_29(0x8, 0x1, 0x4)
    Jump("loc_4908")

    label("loc_4878")


    #C0233
    ChrTalk(
        0xFE,
        "我虽然不知道这只小猫的主人是谁……\x02",
    )

    CloseMessageWindow()

    #C0234
    ChrTalk(
        0xFE,
        (
            "不过说起来，隆和亨利\x01",
            "好像是说过捡到了一只小猫……\x02",
        )
    )

    CloseMessageWindow()

    #C0235
    ChrTalk(
        0xFE,
        (
            "真羡慕隆他们，\x01",
            "小桃也好想帮忙一起照顾啊……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4908")

    Jump("loc_4C13")

    label("loc_490D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_491B")
    Jump("loc_4C13")

    label("loc_491B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_49C7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_499B")
    OP_63(0xFE, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xFE)

    #C0236
    ChrTalk(
        0xFE,
        "哇～……！\x02",
    )

    CloseMessageWindow()

    #C0237
    ChrTalk(
        0xFE,
        "隆跑得好快～！\x02",
    )

    CloseMessageWindow()

    #C0238
    ChrTalk(
        0x101,
        (
            "#0012F闭着眼睛跑\x01",
            "可是很危险的啊……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_49C2")

    label("loc_499B")


    #C0239
    ChrTalk(
        0xFE,
        (
            "隆，好可怕～！\x01",
            "跑得好快啊～……！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_49C2")

    Jump("loc_4C13")

    label("loc_49C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_49D8")
    Call(0, 15)
    Jump("loc_4C13")

    label("loc_49D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_4A3B")

    #C0240
    ChrTalk(
        0xFE,
        (
            "隆说……我也可以\x01",
            "和他们一起玩哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xFE)

    #C0241
    ChrTalk(
        0xFE,
        "太、太好了……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_4C13")

    label("loc_4A3B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_4A49")
    Jump("loc_4C13")

    label("loc_4A49")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_4A57")
    Jump("loc_4C13")

    label("loc_4A57")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_4A65")
    Jump("loc_4C13")

    label("loc_4A65")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_4A73")
    Jump("loc_4C13")

    label("loc_4A73")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_4A81")
    Jump("loc_4C13")

    label("loc_4A81")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_4A8F")
    Jump("loc_4C13")

    label("loc_4A8F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_4AE3")

    #C0242
    ChrTalk(
        0xFE,
        (
            "隆和亨利，\x01",
            "今天也很有精神啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0243
    ChrTalk(
        0xFE,
        (
            "小桃不能和\x01",
            "他们一起玩吗……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4C13")

    label("loc_4AE3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_4B50")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4B31")

    #C0244
    ChrTalk(
        0xFE,
        (
            "隆和亨利最近\x01",
            "都不来玩了。\x02",
        )
    )

    CloseMessageWindow()

    #C0245
    ChrTalk(
        0xFE,
        "在做什么呢……\x02",
    )

    CloseMessageWindow()
    Jump("loc_4B4B")

    label("loc_4B31")


    #C0246
    ChrTalk(
        0xFE,
        "小桃也想养小猫啊……\x02",
    )

    CloseMessageWindow()

    label("loc_4B4B")

    Jump("loc_4C13")

    label("loc_4B50")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_4BFC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4BD0")

    #C0247
    ChrTalk(
        0xFE,
        (
            "最近都看不到\x01",
            "隆和亨利了。\x02",
        )
    )

    CloseMessageWindow()

    #C0248
    ChrTalk(
        0xFE,
        (
            "他们好像有\x01",
            "什么秘密呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0249
    ChrTalk(
        0xFE,
        (
            "真羡慕呢……小桃也想\x01",
            "加入他们啊……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4BF7")

    label("loc_4BD0")


    #C0250
    ChrTalk(
        0xFE,
        (
            "呜，可是他们什么都不\x01",
            "告诉小桃……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4BF7")

    Jump("loc_4C13")

    label("loc_4BFC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_4C0A")
    Jump("loc_4C13")

    label("loc_4C0A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_4C13")

    label("loc_4C13")

    TalkEnd(0xFE)
    Return()

    # Function_19_46D6 end

    def Function_20_4C17(): pass

    label("Function_20_4C17")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4CF8")

    #C0251
    ChrTalk(
        0xFE,
        (
            "我将烤制的最高杰作\x01",
            "给奥斯卡尝过了。\x02",
        )
    )

    CloseMessageWindow()

    #C0252
    ChrTalk(
        0xFE,
        (
            "他看上去很开心地说：\x01",
            "『哈哈，这真是很美味啊！』\x01",
            "……就是这样。\x02",
        )
    )

    CloseMessageWindow()

    #C0253
    ChrTalk(
        0xFE,
        (
            "呜呜……\x01",
            "他怎么会赞赏\x01",
            "对手做的面包啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0254
    ChrTalk(
        0xFE,
        "奥斯卡那家伙……骗不了我的……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xED, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4CF0")
    SetScenarioFlags(0xED, 1)

    label("loc_4CF0")

    SetScenarioFlags(0x0, 7)
    Jump("loc_4D96")

    label("loc_4CF8")


    #C0255
    ChrTalk(
        0xFE,
        (
            "如果真的觉得很好吃，\x01",
            "应该会更加吃惊才对呢……\x01",
            "嗯，肯定是那样没错。\x02",
        )
    )

    CloseMessageWindow()

    #C0256
    ChrTalk(
        0xFE,
        (
            "可恶，奥斯卡那臭家伙……！\x01",
            "我一定要修行修行再修行，\x01",
            "绝对要让他再也无话可说……！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4D96")

    TalkEnd(0xFE)
    Return()

    # Function_20_4C17 end

    def Function_21_4D9A(): pass

    label("Function_21_4D9A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4E18")

    #C0257
    ChrTalk(
        0xFE,
        (
            "我终于买下了\x01",
            "导力车。\x02",
        )
    )

    CloseMessageWindow()

    #C0258
    ChrTalk(
        0xFE,
        (
            "呵呵呵，明天就去兜上一圈，\x01",
            "好好享受期待已久的初次上路吧。\x01",
            "真是很期待啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_4E62")

    label("loc_4E18")


    #C0259
    ChrTalk(
        0xFE,
        (
            "我终于买下了\x01",
            "导力车。\x02",
        )
    )

    CloseMessageWindow()

    #C0260
    ChrTalk(
        0xFE,
        (
            "呵呵，年老以后\x01",
            "就要最大限度地享受人生啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4E62")

    TalkEnd(0xFE)
    Return()

    # Function_21_4D9A end

    def Function_22_4E66(): pass

    label("Function_22_4E66")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_4F66")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4F1A")

    #C0261
    ChrTalk(
        0xFE,
        (
            "欢迎光临～\x01",
            "欢迎光顾塔利兹商店～\x02",
        )
    )

    CloseMessageWindow()

    #C0262
    ChrTalk(
        0xFE,
        "啊呀，好可爱的孩子。\x02",
    )

    CloseMessageWindow()

    #C0263
    ChrTalk(
        0xFE,
        (
            "和我家的小桃\x01",
            "做个好朋友如何呢～？\x02",
        )
    )

    CloseMessageWindow()

    #C0264
    ChrTalk(
        0x153,
        "#1110F嗯，知道啦～！\x02",
    )

    CloseMessageWindow()

    #C0265
    ChrTalk(
        0x101,
        "#0000F哈哈哈……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_4F61")

    label("loc_4F1A")


    #C0266
    ChrTalk(
        0xFE,
        (
            "我家的小桃稍微\x01",
            "有些内向害羞呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0267
    ChrTalk(
        0xFE,
        "你能和她做朋友，我很高兴啊～\x02",
    )

    CloseMessageWindow()

    label("loc_4F61")

    Jump("loc_513A")

    label("loc_4F66")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_4F74")
    Jump("loc_513A")

    label("loc_4F74")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_507C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 6)), scpexpr(EXPR_END)), "loc_4FFD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4FD3")

    #C0268
    ChrTalk(
        0xFE,
        (
            "皮特来了哦。\x01",
            "说是要给律师做午饭，\x02",
        )
    )

    CloseMessageWindow()

    #C0269
    ChrTalk(
        0xFE,
        "真是很能干啊。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_4FF8")

    label("loc_4FD3")


    #C0270
    ChrTalk(
        0xFE,
        (
            "希望我家的小桃\x01",
            "也能稍微学着点。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4FF8")

    Jump("loc_5077")

    label("loc_4FFD")


    #C0271
    ChrTalk(
        0xFE,
        (
            "听说不良团伙好像经常在旧城区那边\x01",
            "进行斗殴？\x02",
        )
    )

    CloseMessageWindow()

    #C0272
    ChrTalk(
        0xFE,
        (
            "虽然只是听了传闻，但还是觉得很恐怖啊～\x01",
            "希望我家的小桃不要靠近那边。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5077")

    Jump("loc_513A")

    label("loc_507C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_513A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_50FD")

    #C0273
    ChrTalk(
        0xFE,
        (
            "啊，早上好，\x01",
            "欢迎光临『塔利兹商店』～\x02",
        )
    )

    CloseMessageWindow()

    #C0274
    ChrTalk(
        0xFE,
        (
            "托您的福，我们已经开店十周年啦，\x01",
            "总是承蒙您的关照啊～\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_513A")

    label("loc_50FD")


    #C0275
    ChrTalk(
        0xFE,
        (
            "我们也终于迎来开店十周年了哦。\x01",
            "这都是托了各位街坊的福。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_513A")

    TalkEnd(0xFE)
    Return()

    # Function_22_4E66 end

    def Function_23_513E(): pass

    label("Function_23_513E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8E, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5231")

    #C0276
    ChrTalk(
        0x10,
        "#1200F呜噜噜噜噜…………\x02",
    )

    CloseMessageWindow()

    #C0277
    ChrTalk(
        0x101,
        "#0000F缇欧，它在说什么？\x02",
    )

    CloseMessageWindow()

    #C0278
    ChrTalk(
        0x103,
        (
            "#0200F『好舒服的阳光』\x01",
            "……它这么说。\x02",
        )
    )

    CloseMessageWindow()

    #C0279
    ChrTalk(
        0x104,
        (
            "#0300F什么嘛……\x01",
            "还以为它想说老被烦人的小鬼纠缠，\x01",
            "心情很不爽呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0280
    ChrTalk(
        0x102,
        (
            "#0100F呵呵，蔡特好像\x01",
            "还算是挺放松享受的呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x8E, 3)
    Jump("loc_524F")

    label("loc_5231")


    #C0281
    ChrTalk(
        0x10,
        "#1200F呜噜噜噜噜…………\x02",
    )

    CloseMessageWindow()

    label("loc_524F")

    TalkEnd(0xFE)
    Return()

    # Function_23_513E end

    def Function_24_5253(): pass

    label("Function_24_5253")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    LoadChrToIndex("chr/ch00900.itc", 0x1E)
    OP_4B(0xF, 0xFF)
    SetChrFlags(0xF, 0x80)
    OP_68(16500, 6000, 15500, 0)
    MoveCamera(66, 2, 0, 0)
    OP_6E(760, 0)
    SetCameraDistance(15500, 0)
    SetChrPos(0x101, 10500, 3000, 14800, 90)
    SetChrPos(0x102, 10500, 3000, 16200, 90)
    SetChrPos(0x103, 9300, 3000, 14800, 90)
    SetChrPos(0x104, 9300, 3000, 16200, 90)
    SetChrChipByIndex(0x11, 0x1E)
    SetChrSubChip(0x11, 0x0)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x8000)
    OP_A7(0x11, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x11, 21000, 3000, 15500, 270)
    OP_52(0x11, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu00600.itp")
    OP_68(14500, 6000, 15500, 6000)
    MoveCamera(56, 2, 0, 6000)
    SetCameraDistance(18500, 6000)
    FadeToBright(1000, 0)
    OP_6F(0x1)
    OP_6F(0x40)
    OP_6F(0x10)
    Sleep(500)

    #C0282
    ChrTalk(
        0x102,
        (
            "#0100F格里姆伍德法律事务所……\x02\x03",

            "嗯，看来就是这里了哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0283
    ChrTalk(
        0x101,
        (
            "#5P#0000F那位律师，我以前也曾\x01",
            "见过好几次哦。\x02\x03",

            "但并没有想到他是\x01",
            "那么了不起的人呢……\x02",
        )
    )

    CloseMessageWindow()
    ClearMapObjFlags(0x3, 0x10)
    OP_71(0x3, 0x0, 0xA, 0x0, 0x0)
    Sound(103, 0, 100, 0)
    OP_79(0x3)
    Sleep(300)

    #N0284
    NpcTalk(
        0x11,
        "男人的声音",
        (
            "#1P#2S……那么，律师。\x01",
            "今后也请您多关照了。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    #N0285
    NpcTalk(
        0x11,
        "男性的声音",
        (
            "#11P#2S啊，那是没问题……\x02\x03",

            "#2S不过，你们那里是不是\x01",
            "也应该稍微做点什么呢？\x02\x03",

            "#2S至少也应该\x01",
            "考虑到市民们的心情啊……\x02",
        )
    )

    CloseMessageWindow()

    #N0286
    NpcTalk(
        0x11,
        "男人的声音",
        (
            "#1P#2S……讨好市民并不是\x01",
            "我的工作内容。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    Sound(1553, 255, 90, 0)    #voice#Dudley
    Sleep(1000)
    Fade(500)
    OP_68(13070, 3700, 15860, 0)
    MoveCamera(55, 17, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(23790, 0)
    OP_0D()

    def lambda_55E7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_55E7)

    def lambda_55F8():
        OP_95(0xFE, 14000, 3000, 15500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_55F8)
    WaitChrThread(0x11, 2)
    Sleep(800)
    OP_71(0x3, 0xA, 0x0, 0x0, 0x0)
    Sound(104, 0, 100, 0)
    OP_79(0x3)
    SetMapObjFlags(0x3, 0x10)
    WaitChrThread(0x11, 1)
    OP_63(0x11, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    #Sound(1554, 255, 100, 0)    #voice#Dudley
    SetChrName("戴眼镜的男性")

    #A0287
    AnonymousTalk(
        0xFF,
        (
            "你们是……\x02\x03",

            "………………………………………\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)

    #C0288
    ChrTalk(
        0x101,
        "#6P#0005F怎、怎么了……？\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Sound(1555, 255, 100, 0)    #voice#Dudley
    Sleep(500)

    #N0289
    NpcTalk(
        0x11,
        "戴眼镜的男性",
        (
            "#0604F#11P……原来如此。\x02\x03",

            "#0602F是赛尔盖长官\x01",
            "最近刚养的那几只小狗啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0290
    ChrTalk(
        0x101,
        "#6P#0011F哎……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0291
    ChrTalk(
        0x101,
        (
            "#6P#0001F那徽章……\x01",
            "您也在克洛斯贝尔警察局工作吗？\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Sound(1556, 255, 100, 0)    #voice#Dudley
    Sleep(500)

    #N0292
    NpcTalk(
        0x11,
        "戴眼镜的男性",
        (
            "#0603F#11P我是什么人并不重要。\x02\x03",

            "#0601F看来，你们似乎是想\x01",
            "拜访伊安律师啊……\x02\x03",

            "但我奉劝你们，注意不要\x01",
            "浪费人家的宝贵时间。\x02\x03",

            "和你们这种没用的家伙不同，\x01",
            "他可是个十分忙碌的人。\x02",
        )
    )

    CloseMessageWindow()

    #C0293
    ChrTalk(
        0x101,
        "#6P#0013F什么……！？\x02",
    )

    CloseMessageWindow()

    def lambda_5928():

        label("loc_5928")

        TurnDirection(0xFE, 0x11, 500)
        Yield()
        Jump("loc_5928")

    QueueWorkItem2(0x101, 2, lambda_5928)

    def lambda_593A():

        label("loc_593A")

        TurnDirection(0xFE, 0x11, 500)
        Yield()
        Jump("loc_593A")

    QueueWorkItem2(0x102, 2, lambda_593A)

    def lambda_594C():

        label("loc_594C")

        TurnDirection(0xFE, 0x11, 500)
        Yield()
        Jump("loc_594C")

    QueueWorkItem2(0x103, 2, lambda_594C)

    def lambda_595E():

        label("loc_595E")

        TurnDirection(0xFE, 0x11, 500)
        Yield()
        Jump("loc_595E")

    QueueWorkItem2(0x104, 2, lambda_595E)

    def lambda_5970():
        OP_95(0xFE, 2100, 3000, 15500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_5970)
    Sleep(600)
    OP_68(11850, 3700, 16440, 3000)

    def lambda_599E():
        OP_96(0xFE, 0x2904, 0xBB8, 0x3840, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_599E)
    Sleep(400)

    def lambda_59BB():
        OP_96(0xFE, 0x2454, 0xBB8, 0x3840, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_59BB)
    Sleep(2500)

    def lambda_59D8():
        OP_96(0xFE, 0x2904, 0xBB8, 0x39D0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_59D8)
    Sleep(400)

    def lambda_59F5():
        OP_96(0xFE, 0x2454, 0xBB8, 0x39D0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_59F5)
    WaitChrThread(0x11, 1)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x103, 1)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x103, 0x2)
    EndChrThread(0x104, 0x2)
    ClearChrFlags(0x11, 0x8000)
    SetChrFlags(0x11, 0x80)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)

    #C0294
    ChrTalk(
        0x101,
        "#11P#0007F刚、刚才那些话到底是什么意思啊！？\x02",
    )

    CloseMessageWindow()

    #C0295
    ChrTalk(
        0x102,
        (
            "#11P#0101F看样子，那人好像是\x01",
            "总部的搜查官呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0296
    ChrTalk(
        0x103,
        "#12P#0211F……态度十分居高临下啊。\x02",
    )

    CloseMessageWindow()

    #C0297
    ChrTalk(
        0x104,
        (
            "#0303F#5P不过，那个眼镜男……\x01",
            "似乎是个相当厉害的家伙呢。\x02\x03",

            "#0301F左肋部位还挂着\x01",
            "一个不小的武器。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0x101, 0x104, 500)

    #C0298
    ChrTalk(
        0x101,
        "#11P#0005F有、有这种事吗？\x02",
    )

    CloseMessageWindow()

    #C0299
    ChrTalk(
        0x102,
        "#11P#0105F你竟然能察觉到呢……\x02",
    )

    CloseMessageWindow()

    #C0300
    ChrTalk(
        0x103,
        (
            "#12P#0203F我也用传感器\x01",
            "感知到了。\x02\x03",

            "#0200F大型的军用手枪……\x01",
            "似乎就是那种东西吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0301
    ChrTalk(
        0x104,
        "#0300F#5P是啊，多半如此。\x02",
    )

    CloseMessageWindow()

    #C0302
    ChrTalk(
        0x101,
        "#11P#0000F呼～……\x02",
    )

    CloseMessageWindow()

    #C0303
    ChrTalk(
        0x102,
        "#11P#0100F你们两人都好厉害啊……\x02",
    )

    CloseMessageWindow()

    def lambda_5CB4():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_5CB4)
    Sleep(50)

    def lambda_5CC4():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_5CC4)
    Sleep(300)

    #C0304
    ChrTalk(
        0x104,
        "#0304F#6P哈哈，碰巧注意到而已啦。\x02",
    )

    CloseMessageWindow()

    #C0305
    ChrTalk(
        0x103,
        (
            "#6P#0200F比起那个来，我们\x01",
            "是不是该去拜访那位律师了呢？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 500)

    #C0306
    ChrTalk(
        0x101,
        "#11P#0005F嗯……\x02",
    )

    CloseMessageWindow()

    def lambda_5D54():
        OP_93(0xFE, 0x59, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5D54)
    Sleep(100)

    def lambda_5D64():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_5D64)
    Sleep(500)

    #C0307
    ChrTalk(
        0x101,
        (
            "#6P#0001F虽然在他百忙之中还前去打扰有些不好意思，\x01",
            "但还是进去打个招呼吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_CA(0x1, 0xFF, 0x0)
    OP_D5(0x1E)
    OP_4C(0xF, 0xFF)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0x0, 10200, 3000, 15500, 90)
    ModifyEventFlags(0, 0, 0x80)
    SetScenarioFlags(0x42, 7)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_24_5253 end

    def Function_25_5DF6(): pass

    label("Function_25_5DF6")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(17100, 4000, 15500, 0)
    MoveCamera(57, 27, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(21500, 0)
    OP_4B(0xF, 0xFF)
    SetChrFlags(0xF, 0x80)
    SetChrPos(0x101, 20500, 3000, 15500, 270)
    SetChrPos(0x102, 20500, 3000, 15500, 270)
    SetChrPos(0x103, 20500, 3000, 15500, 270)
    SetChrPos(0x104, 20500, 3000, 15500, 270)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearMapObjFlags(0x3, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x46, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5EED")
    LoadChrToIndex("chr/ch07000.itc", 0x1E)
    SetChrChipByIndex(0x19, 0x1E)
    SetChrSubChip(0x19, 0x0)
    SetChrPos(0x19, 8000, 3300, 21000, 180)
    ClearChrFlags(0x19, 0x80)
    ClearChrBattleFlags(0x19, 0x8000)
    OP_A7(0x19, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    label("loc_5EED")

    FadeToBright(1000, 0)
    Sleep(500)
    OP_71(0x3, 0x0, 0xA, 0x0, 0x0)
    Sound(103, 0, 100, 0)
    OP_79(0x3)
    OP_68(11900, 4000, 15500, 5500)
    MoveCamera(45, 27, 0, 5500)
    SetCameraDistance(20500, 5500)

    def lambda_5F38():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5F38)

    def lambda_5F49():
        OP_95(0xFE, 15000, 3000, 15500, 2500, 0x1)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5F49)
    Sleep(700)

    def lambda_5F66():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_5F66)

    def lambda_5F77():
        OP_95(0xFE, 15000, 3000, 15500, 2500, 0x1)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5F77)
    Sleep(700)

    def lambda_5F94():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_5F94)

    def lambda_5FA5():
        OP_95(0xFE, 15000, 3000, 15500, 2500, 0x1)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5FA5)
    Sleep(700)

    def lambda_5FC2():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_5FC2)

    def lambda_5FD3():
        OP_95(0xFE, 15000, 3000, 15500, 2500, 0x1)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_5FD3)
    WaitChrThread(0x101, 1)

    def lambda_5FF1():
        OP_95(0xFE, 11200, 3000, 14800, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5FF1)
    WaitChrThread(0x102, 1)

    def lambda_600F():
        OP_95(0xFE, 11200, 3000, 16200, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_600F)
    WaitChrThread(0x103, 1)

    def lambda_602D():
        OP_95(0xFE, 12600, 3000, 14800, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_602D)
    WaitChrThread(0x104, 1)

    def lambda_604B():
        OP_95(0xFE, 12600, 3000, 16200, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_604B)
    OP_71(0x3, 0xA, 0x0, 0x0, 0x0)
    Sound(104, 0, 100, 0)
    WaitChrThread(0x101, 1)

    def lambda_607B():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_607B)
    WaitChrThread(0x102, 1)

    def lambda_608C():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_608C)
    WaitChrThread(0x103, 1)

    def lambda_609D():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_609D)
    WaitChrThread(0x104, 1)

    def lambda_60AE():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_60AE)
    WaitChrThread(0x104, 2)
    OP_79(0x3)
    OP_6F(0x79)

    #C0308
    ChrTalk(
        0x102,
        (
            "#0100F那么，接下来该怎么办？\x02\x03",

            "为了整理思路，\x01",
            "是不是应该回一趟支援科？\x02",
        )
    )

    CloseMessageWindow()

    #C0309
    ChrTalk(
        0x101,
        (
            "#6P#0008F也是啊……\x02\x03",

            "#0003F在那之前，如果还有其它\x01",
            "事情需要处理，就先去办完吧。\x02\x03",

            "#0001F如果我的想法就是\x01",
            "事件的真相……\x01",
            "那事情就真是变得相当棘手了。\x02",
        )
    )

    CloseMessageWindow()

    #C0310
    ChrTalk(
        0x104,
        (
            "#5P#0309F嘿嘿，虽然嘴上说得很谦虚，\x01",
            "但其实好像非常有自信嘛。\x02\x03",

            "#0300F既然如此，\x01",
            "那就赶快把其它事情解决，\x01",
            "然后返回支援科吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0311
    ChrTalk(
        0x103,
        (
            "#0202F……嗯，\x01",
            "尽快解决吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x46, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6DB9")
    OP_68(11050, 4000, 15990, 3000)
    MoveCamera(45, 27, 0, 3000)
    OP_6E(500, 3000)
    SetCameraDistance(20500, 3000)
    OP_71(0x2, 0x0, 0x5, 0x0, 0x0)
    Sound(103, 0, 100, 0)
    OP_79(0x2)
    Sleep(500)

    def lambda_629B():
        OP_95(0xFE, 8000, 3000, 15500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_629B)

    def lambda_62B5():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0x19, 2, lambda_62B5)
    Sleep(1000)
    OP_71(0x2, 0x5, 0x0, 0x0, 0x0)
    Sound(104, 0, 100, 0)
    OP_79(0x2)
    Sleep(500)
    WaitChrThread(0x19, 1)
    OP_63(0x19, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    def lambda_62F7():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_62F7)
    Sleep(1000)

    #N0312
    NpcTalk(
        0x19,
        "青年",
        (
            "哎……？\x01",
            "……这不是罗伊德嘛。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_632F():
        OP_95(0xFE, 9500, 3000, 15500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_632F)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    def lambda_6391():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6391)
    Sleep(60)

    def lambda_63A1():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_63A1)
    Sleep(60)

    def lambda_63B1():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_63B1)
    Sleep(60)

    def lambda_63C1():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_63C1)
    Sleep(60)
    WaitChrThread(0x19, 1)

    #C0313
    ChrTalk(
        0x101,
        "#0005F#11P奥斯卡……！？\x02",
    )

    CloseMessageWindow()

    #C0314
    ChrTalk(
        0x19,
        (
            "哇哈哈，真是好久不见了啊！\x01",
            "你是什么时候回来的？\x02",
        )
    )

    CloseMessageWindow()

    #C0315
    ChrTalk(
        0x19,
        (
            "这三年来，你连一次面都没有露过，\x01",
            "我可是很担心的哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0316
    ChrTalk(
        0x101,
        (
            "#0004F#11P哈哈哈……抱歉。\x01",
            "本来早就想去\x01",
            "和你打个招呼……\x02\x03",

            "#0002F但工作上稍微遇到了一些事情，\x01",
            "一直难以脱身啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0317
    ChrTalk(
        0x19,
        (
            "是吗，看来你现在也在工作呢……\x01",
            "那个……是在和同事一起进行调查吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0318
    ChrTalk(
        0x101,
        (
            "#0005F#11P哎、是啊，确实如此。\x02\x03",

            "#0006F……你怎么连这个都知道啊。\x01",
            "你还是和以前一样，\x01",
            "让人搞不清到底是敏锐还是粗神经……\x02",
        )
    )

    CloseMessageWindow()

    #C0319
    ChrTalk(
        0x19,
        (
            "哇哈哈，看你的表情好像有些沉重，\x01",
            "所以才这么猜啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0320
    ChrTalk(
        0x19,
        (
            "……对了，罗伊德。\x01",
            "要不，你就把这个拿去吧。\x01",
            "就当作是再会的纪念。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_6614():
        OP_98(0xFE, 0x1F4, 0x0, 0xFFFFFE0C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_6614)
    WaitChrThread(0x19, 1)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0321
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x2),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    AddItemNumber(0x2, 1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B0(0xD)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_67A9")
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0322
    AnonymousTalk(
        0xFF,
        (
            "手册中",
            scpstr(SCPSTR_CODE_ITEM, 0x1B5),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "的做法已经记下了。\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    #A0323
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1B5),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "的做法已经学会了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    OP_B0(0xD)

    def lambda_66D4():
        OP_98(0xFE, 0xFFFFFE0C, 0x0, 0x1F4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_66D4)
    WaitChrThread(0x19, 1)

    #C0324
    ChrTalk(
        0x19,
        "罗伊德，你很擅长做料理吧？\x02",
    )

    CloseMessageWindow()

    #C0325
    ChrTalk(
        0x19,
        (
            "使用这个东西，可以将食谱的每一个细节\x01",
            "和变化都记录下来，还能供多个人一起使用。\x02",
        )
    )

    CloseMessageWindow()

    #C0326
    ChrTalk(
        0x19,
        (
            "不过，现在只记录着\x01",
            "三明治的菜谱啦。\x01",
            "不嫌弃的话，请你多加活用。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_684D")

    label("loc_67A9")

    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()

    def lambda_67C1():
        OP_98(0xFE, 0xFFFFFE0C, 0x0, 0x1F4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_67C1)
    WaitChrThread(0x19, 1)

    #C0327
    ChrTalk(
        0x19,
        "罗伊德，你很擅长做料理吧？\x02",
    )

    CloseMessageWindow()

    #C0328
    ChrTalk(
        0x19,
        (
            "使用这个东西，可以将食谱的每一个细节\x01",
            "和变化都记录下来，还能供多个人一起使用。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_684D")


    #C0329
    ChrTalk(
        0x101,
        (
            "#0002F#11P嘿，那可真是相当方便啊……\x02\x03",

            "#0009F多谢啦，奥斯卡。\x01",
            "我一定会好好使用它的。\x02",
        )
    )

    CloseMessageWindow()

    #C0330
    ChrTalk(
        0x19,
        "噢，那么就先说再见吧。\x02",
    )

    CloseMessageWindow()

    def lambda_68C7():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_68C7)
    WaitChrThread(0x19, 1)
    Sleep(300)

    #C0331
    ChrTalk(
        0x19,
        (
            "我已经开始在那边那家\x01",
            "叫做摩尔吉的面包店工作了。\x01",
            "如果以后有空的话，可以再来找我啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0332
    ChrTalk(
        0x101,
        (
            "#0004F#11P面包店吗……说起来，\x01",
            "在信里确实写到过呢。\x02\x03",

            "#0000F知道啦，下次再去拜访你。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_698C():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_698C)
    WaitChrThread(0x19, 1)

    #C0333
    ChrTalk(
        0x19,
        "哈哈，要是没时间的话，也不用太过勉强哦。\x02",
    )

    CloseMessageWindow()

    def lambda_69CB():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_69CB)
    WaitChrThread(0x19, 1)

    def lambda_69DC():
        OP_95(0xFE, 1000, 3000, 15500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_69DC)
    Sleep(3000)

    #C0334
    ChrTalk(
        0x103,
        (
            "#0202F#11P看起来好像是\x01",
            "罗伊德前辈的熟人吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0335
    ChrTalk(
        0x101,
        (
            "#0004F#11P嗯，他叫奥斯卡，\x01",
            "是我的童年玩伴。\x02\x03",

            "#0002F我们一直都在通信，\x01",
            "但那家伙还真是一点都没有变啊……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_6A96():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6A96)
    WaitChrThread(0x102, 1)

    #C0336
    ChrTalk(
        0x102,
        (
            "#0100F罗伊德……如果需要的话，\x01",
            "你们不妨再聊一会啊。\x02\x03",

            "已经很久没见过面了吧？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_6AF8():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6AF8)
    WaitChrThread(0x101, 1)

    #C0337
    ChrTalk(
        0x101,
        (
            "#0006F不了，现在还是应该尽早思考一下\x01",
            "从伊安律师那里听来的情报……\x02\x03",

            "#0000F好啦，反正以后还要经常在市内奔波，\x01",
            "到时再去那间面包屋拜访他吧。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_6B97():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_6B97)
    WaitChrThread(0x104, 1)

    #C0338
    ChrTalk(
        0x104,
        (
            "#0304F#5P嗯，那样也好啊。\x02\x03",

            "#0302F如果该办的事都办完了，\x01",
            "就赶快回支援科吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Sleep(150)
    SetChrFlags(0x19, 0x80)
    SetChrBattleFlags(0x19, 0x8000)
    OP_49()
    OP_D5(0x1E)
    FadeToDark(300, 0, 100)
    Sound(828, 0, 100, 0)
    SetChrName("")

    #A0339
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※和不同的人交谈，或调查一些特定的场所，\x01",
            "  就有机会得到各种『食谱』。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #A0340
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※『食谱』会被记录在『料理手册』中。\x01",
            "  只要使用『料理手册』，随时都可以\x01",
            "  制作各种效果不同的料理。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #A0341
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※此外，做出的料理还有一定的概率会成为\x01",
            "  『大成功』料理或『预想外』料理。\x01",
            "  （同时，料理也有『制作失败』的可能。）\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #A0342
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※制作料理所需要的『食材』，\x01",
            "  可以在杂货店之类的商店中购得。\x01",
            "  此外，一些魔兽有时也会掉落。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x46, 1)
    SetScenarioFlags(0x4A, 7)

    label("loc_6DB9")

    SetChrPos(0x0, 11500, 3000, 15500, 270)
    OP_4C(0xF, 0xFF)
    ClearChrFlags(0xF, 0x80)
    SetMapObjFlags(0x3, 0x10)
    SetScenarioFlags(0x43, 0)
    OP_29(0x3E, 0x1, 0x7)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x46, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6DFB")
    OP_1B(0x0, 0x0, 0x1E)
    OP_1B(0x1, 0x0, 0x1F)
    ModifyEventFlags(1, 1, 0x80)

    label("loc_6DFB")

    EventEnd(0x5)
    Return()

    # Function_25_5DF6 end

    def Function_26_6DFE(): pass

    label("Function_26_6DFE")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch02702.itc", 0x1E)
    LoadChrToIndex("chr/ch05900.itc", 0x1F)
    LoadChrToIndex("chr/ch07000.itc", 0x20)
    LoadChrToIndex("chr/ch24500.itc", 0x21)
    LoadChrToIndex("chr/ch20700.itc", 0x22)
    LoadChrToIndex("chr/ch25000.itc", 0x23)
    OP_68(6600, 1400, -11300, 0)
    MoveCamera(27, 21, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(14500, 0)
    SetChrPos(0x101, 11700, 0, -9200, 270)
    SetChrPos(0x102, 11900, 0, -10200, 270)
    SetChrPos(0x103, 13300, 0, -10200, 270)
    SetChrPos(0x104, 13100, 0, -9200, 270)
    ClearChrFlags(0x12, 0x4)
    SetChrFlags(0x12, 0x8000)
    SetChrChipByIndex(0x12, 0x1E)
    SetChrSubChip(0x12, 0x0)
    SetChrPos(0x12, 8200, 0, -9400, 270)
    ClearChrFlags(0x12, 0x80)
    ClearChrBattleFlags(0x12, 0x8000)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    OP_4B(0x8, 0xFF)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 6800, 0, -9900, 90)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    OP_4B(0x9, 0xFF)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, 6600, 0, -8800, 125)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    OP_4B(0xA, 0xFF)
    SetChrFlags(0xA, 0x8000)
    SetChrPos(0xA, 10510, 0, -7890, 243)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    OP_4B(0xC, 0xFF)
    SetChrFlags(0xC, 0x8000)
    SetChrPos(0xC, 8940, 0, -4080, 210)
    SetChrChipByIndex(0x14, 0x1F)
    SetChrSubChip(0x14, 0x0)
    ClearChrFlags(0x14, 0x80)
    ClearChrBattleFlags(0x14, 0x8000)
    SetChrFlags(0x14, 0x8000)
    SetChrPos(0x14, 7260, 0, -5600, 157)
    SetChrChipByIndex(0x15, 0x20)
    SetChrSubChip(0x15, 0x0)
    ClearChrFlags(0x15, 0x80)
    ClearChrBattleFlags(0x15, 0x8000)
    SetChrFlags(0x15, 0x8000)
    SetChrPos(0x15, 8900, 0, -6230, 217)
    SetChrChipByIndex(0x16, 0x21)
    SetChrSubChip(0x16, 0x0)
    ClearChrFlags(0x16, 0x80)
    ClearChrBattleFlags(0x16, 0x8000)
    SetChrFlags(0x16, 0x8000)
    SetChrPos(0x16, 4310, 0, -7050, 127)
    SetChrChipByIndex(0x17, 0x22)
    SetChrSubChip(0x17, 0x0)
    ClearChrFlags(0x17, 0x80)
    ClearChrBattleFlags(0x17, 0x8000)
    SetChrFlags(0x17, 0x8000)
    SetChrPos(0x17, 12470, 0, -6780, 240)
    SetChrChipByIndex(0x18, 0x23)
    SetChrSubChip(0x18, 0x0)
    ClearChrFlags(0x18, 0x80)
    ClearChrBattleFlags(0x18, 0x8000)
    SetChrFlags(0x18, 0x8000)
    SetChrPos(0x18, 5760, 0, -4940, 178)
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x13, 0x8000)
    SetMapObjFlags(0xC, 0x1000)
    ClearMapObjFlags(0xC, 0x4)
    OP_78(0xC, 0x13)
    SetMapObjFrame(0xC, "light", 0x0, 0x1)
    OP_49()
    SetChrPos(0x13, 1500, 0, -13500, 0)
    OP_D3(0x13, 0x0, 0x29810, 0x4E20, 0x0)
    OP_70(0xC, 0x0)
    SetMapObjFrame(0xFF, "br02", 0x1, 0x1)
    SetMapObjFrame(0xFF, "br00", 0x0, 0x1)
    SetMapObjFrame(0xFF, "br01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "br_mul", 0x0, 0x1)
    FadeToBright(1000, 0)
    OP_0D()
    SetChrName("")

    #A0343
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "◆未输入。\x01",
            "西街的单色回忆剧情。\x01",
            "蔡特解救了遭遇事故的孩子。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    VolumeBGM(0x64, 0x3E8)
    SetScenarioFlags(0x5C, 7)
    NewScene("c0110", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_26_6DFE end

    def Function_27_7118(): pass

    label("Function_27_7118")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(17100, 4000, 15500, 0)
    MoveCamera(57, 27, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(21500, 0)
    SetChrPos(0x101, 20500, 3000, 15500, 270)
    SetChrPos(0x102, 20500, 3000, 15500, 270)
    SetChrPos(0x103, 20500, 3000, 15500, 270)
    SetChrPos(0x104, 20500, 3000, 15500, 270)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearMapObjFlags(0x3, 0x10)
    FadeToBright(1000, 0)
    OP_0D()
    OP_71(0x3, 0x0, 0xA, 0x0, 0x0)
    Sound(103, 0, 100, 0)
    OP_79(0x3)
    OP_68(11900, 4000, 15500, 5500)
    MoveCamera(45, 27, 0, 5500)
    SetCameraDistance(20500, 5500)

    def lambda_7211():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_7211)

    def lambda_7222():
        OP_95(0xFE, 15000, 3000, 15500, 2500, 0x1)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7222)
    Sleep(700)

    def lambda_723F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_723F)

    def lambda_7250():
        OP_95(0xFE, 15000, 3000, 15500, 2500, 0x1)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7250)
    Sleep(700)

    def lambda_726D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_726D)

    def lambda_727E():
        OP_95(0xFE, 15000, 3000, 15500, 2500, 0x1)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_727E)
    Sleep(700)

    def lambda_729B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_729B)

    def lambda_72AC():
        OP_95(0xFE, 15000, 3000, 15500, 2500, 0x1)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_72AC)
    WaitChrThread(0x101, 1)

    def lambda_72CA():
        OP_95(0xFE, 11200, 3000, 14800, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_72CA)
    WaitChrThread(0x102, 1)

    def lambda_72E8():
        OP_95(0xFE, 11200, 3000, 16200, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_72E8)
    WaitChrThread(0x103, 1)

    def lambda_7306():
        OP_95(0xFE, 12600, 3000, 14800, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_7306)
    WaitChrThread(0x104, 1)

    def lambda_7324():
        OP_95(0xFE, 12600, 3000, 16200, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_7324)
    OP_71(0x3, 0xA, 0x0, 0x0, 0x0)
    Sound(104, 0, 100, 0)
    WaitChrThread(0x101, 1)

    def lambda_7354():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_7354)
    WaitChrThread(0x102, 1)

    def lambda_7365():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_7365)
    WaitChrThread(0x103, 1)

    def lambda_7376():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_7376)
    WaitChrThread(0x104, 1)

    def lambda_7387():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_7387)
    WaitChrThread(0x104, 2)
    OP_79(0x3)
    OP_6F(0x79)

    #C0344
    ChrTalk(
        0x101,
        (
            "#6P#0003F那么……\x01",
            "我们这就去『黑月贸易公司』吧。\x02\x03",

            "#0000F记得应该是在港湾区……\x02",
        )
    )

    CloseMessageWindow()

    #C0345
    ChrTalk(
        0x103,
        (
            "#0203F……至于具体地点，\x01",
            "应该是港湾区东北部的外围吧。\x02\x03",

            "#0200F似乎是面朝河边呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0346
    ChrTalk(
        0x104,
        (
            "#5P#0300F啊，就是那个红颜色\x01",
            "的东方式建筑物吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0347
    ChrTalk(
        0x102,
        (
            "#0106F它的周边就坐落着ＩＢＣ、\x01",
            "克洛斯贝尔时代周刊社等建筑，\x01",
            "应该是个比较安全的正常街区啊……\x02\x03",

            "#0101F好啦。\x01",
            "总之，过去找找看吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, 11500, 3000, 15500, 270)
    SetMapObjFlags(0x3, 0x10)
    SetScenarioFlags(0x81, 1)
    OP_29(0x42, 0x1, 0x7)
    EventEnd(0x5)
    Return()

    # Function_27_7118 end

    def Function_28_7520(): pass

    label("Function_28_7520")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearMapFlags(0x10000000)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_68(8000, 5000, 15590, 0)
    MoveCamera(37, 20, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(15560, 0)
    OP_68(16710, 5000, 15520, 4000)
    MoveCamera(70, 18, 0, 4000)
    OP_6E(700, 4000)
    SetCameraDistance(18910, 4000)
    FadeToBright(1000, 0)
    OP_6F(0x79)
    Sleep(500)
    Fade(500)
    OP_68(-14910, 2400, -11820, 0)
    MoveCamera(29, 26, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(7830, 0)
    OP_68(-9970, 3700, 9790, 5000)
    MoveCamera(23, 15, 0, 5000)
    OP_6E(700, 5000)
    SetCameraDistance(16270, 5000)
    OP_6F(0x79)
    Sleep(500)
    Fade(500)
    OP_68(10660, 3700, 2040, 0)
    MoveCamera(59, 21, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(18420, 0)
    OP_68(6220, 1660, 5470, 5000)
    MoveCamera(45, 37, 0, 5000)
    OP_6E(700, 5000)
    SetCameraDistance(44100, 5000)
    PlaceName2(340, 200, "c_plac03", 0x0, 1000)
    OP_6F(0x79)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7858")

    #A0348
    AnonymousTalk(
        0x103,
        (
            "#0205F这里是……\x01",
            "克洛斯贝尔市的西街哦。\x02",
        )
    )

    CloseMessageWindow()

    #A0349
    AnonymousTalk(
        0x101,
        (
            "#0004F嗯，到处都是出租公寓，\x01",
            "有种住宅区的感觉呢。\x02\x03",

            "#0000F这里有不少我认识的人……\x01",
            "可能需要花时间去寒暄一下，\x01",
            "没关系吧？\x02",
        )
    )

    CloseMessageWindow()

    #A0350
    AnonymousTalk(
        0x104,
        (
            "#0300F对了，你就是出生在这里的呢。\x02\x03",

            "#0304F哈，这不是很好吗？\x01",
            "轻松愉快地出发吧。\x02",
        )
    )

    CloseMessageWindow()

    #A0351
    AnonymousTalk(
        0x102,
        (
            "#0102F是啊，毕竟都很久不见了，\x01",
            "我们也陪你一起去吧。\x02",
        )
    )

    CloseMessageWindow()

    #A0352
    AnonymousTalk(
        0x101,
        (
            "#0002F多谢了。\x02\x03",

            "#0004F（居住在贝尔海姆的阿姨一家，\x01",
            "  ……还有奥斯卡。\x01",
            "  不过他现在应该还在面包店里工作……）\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_7858")

    FadeToDark(300, 0, 100)
    OP_0D()
    Sound(828, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0353
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "西街是位于城市西侧的住宅区。\x02",
        )
    )

    CloseMessageWindow()

    #A0354
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "这里并行建立着不少住宅和公寓，同时也零星\x01",
            "分布着一些咖啡店、杂货店之类的店铺。\x02",
        )
    )

    CloseMessageWindow()

    #A0355
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "主人公之一的罗伊德\x01",
            "就是出生并成长在这个街区的。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 7)), scpexpr(EXPR_END)), "loc_79ED")
    FadeToBright(300, 0)
    OP_0D()

    #A0356
    AnonymousTalk(
        0x101,
        (
            "#0005F（说起来……\x01",
            "  还没去和阿姨还有\x01",
            "  奥斯卡打个招呼呢。）\x02\x03",

            "#0008F（阿姨应该是住在贝尔海姆，\x01",
            "  奥斯卡应该正在面包店里工作……）\x02\x03",

            "#0000F（有时间的话就过去看看吧。）\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_79ED")

    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7A55")
    OP_68(110, 5000, 22760, 0)
    MoveCamera(45, 28, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(17500, 0)

    label("loc_7A55")

    SetScenarioFlags(0x44, 6)
    EventEnd(0x5)
    Return()

    # Function_28_7520 end

    def Function_29_7A5B(): pass

    label("Function_29_7A5B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x1, 0x1)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x1, 0x2)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7ADB")
    EventBegin(0x1)
    Sound(823, 0, 100, 0)
    Sleep(500)

    #C0357
    ChrTalk(
        0x101,
        (
            "#0000F喔……\x02\x03",

            "我们还带着小猫呢。\x01",
            "还是不要走太远了。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, -34230, 0, 4210, 90)
    EventEnd(0x4)
    Return()

    label("loc_7ADB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7B89")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7B4C")

    #C0358
    ChrTalk(
        0x101,
        (
            "#0000F这边是城市的西出口啊。\x02\x03",

            "现在没必要去外面……\x01",
            "专心处理市内的工作吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_7B73")

    label("loc_7B4C")

    SetChrName("")

    #A0359
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "现在好像没有必要去市外呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_7B73")

    Sleep(50)
    SetChrPos(0x0, -34230, 0, 4210, 90)
    EventEnd(0x4)

    label("loc_7B89")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7C46")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7C0D")

    #C0360
    ChrTalk(
        0x101,
        (
            "#0000F这边是城市的西出口啊。\x01",
            "前面就是西克洛斯贝尔街道了……\x02\x03",

            "但这次的调查\x01",
            "好像并不需要过去。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_7C30")

    label("loc_7C0D")

    SetChrName("")

    #A0361
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "好像没有必要去市外吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_7C30")

    Sleep(50)
    SetChrPos(0x0, -34230, 0, 4210, 90)
    EventEnd(0x4)

    label("loc_7C46")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7CEB")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7CB2")

    #C0362
    ChrTalk(
        0x101,
        (
            "#0000F嗯，这边是西出口。\x02\x03",

            "不想让琪雅遭遇\x01",
            "到危险啊，\x01",
            "还是不要出去了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_7CD5")

    label("loc_7CB2")

    SetChrName("")

    #A0363
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "好像没有必要去市外吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_7CD5")

    Sleep(50)
    SetChrPos(0x0, -34230, 0, 4210, 90)
    EventEnd(0x4)

    label("loc_7CEB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7DAF")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7D6E")

    #C0364
    ChrTalk(
        0x101,
        (
            "#0003F这边是城市的西出口啊。\x02\x03",

            "还有黑月的事情需要解决……\x01",
            "……现在还是集中精力在市内调查吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_7D99")

    label("loc_7D6E")

    SetChrName("")

    #A0365
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "现在还是集中精力在市内调查吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_7D99")

    Sleep(50)
    SetChrPos(0x0, -34230, 0, 4210, 90)
    EventEnd(0x4)

    label("loc_7DAF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_7E52")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7E0F")

    #C0366
    ChrTalk(
        0x101,
        (
            "#0000F这边是城市的西出口啊。\x01",
            "……现在赶快前往乌尔斯拉医院吧！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_7E3C")

    label("loc_7E0F")

    SetChrName("")

    #A0367
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "似乎没有必要去西克洛斯贝尔街道。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_7E3C")

    Sleep(50)
    SetChrPos(0x0, -34230, 0, 4210, 90)
    EventEnd(0x4)

    label("loc_7E52")

    Return()

    # Function_29_7A5B end

    def Function_30_7E53(): pass

    label("Function_30_7E53")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x1, 0x1)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x1, 0x2)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7ED3")
    EventBegin(0x1)
    Sound(823, 0, 100, 0)
    Sleep(500)

    #C0368
    ChrTalk(
        0x101,
        (
            "#0000F啊……\x02\x03",

            "我们还带着小猫呢。\x01",
            "还是不要走太远了。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, 24460, 0, -8180, 270)
    EventEnd(0x4)
    Return()

    label("loc_7ED3")

    EventBegin(0x1)
    Call(0, 33)
    Sleep(50)
    SetChrPos(0x0, 24460, 0, -8180, 270)
    EventEnd(0x4)
    Return()

    # Function_30_7E53 end

    def Function_31_7EEF(): pass

    label("Function_31_7EEF")

    EventBegin(0x1)
    Sleep(50)
    Call(0, 33)
    SetChrPos(0x0, 110, 3000, 22760, 180)
    EventEnd(0x4)
    Return()

    # Function_31_7EEF end

    def Function_32_7F0B(): pass

    label("Function_32_7F0B")

    EventBegin(0x1)
    Sleep(50)
    Call(0, 33)
    SetChrPos(0x0, 36500, -4000, -19000, 270)
    EventEnd(0x4)
    Return()

    # Function_32_7F0B end

    def Function_33_7F27(): pass

    label("Function_33_7F27")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_809A")

    #C0369
    ChrTalk(
        0x101,
        "#0000F啊，对了……\x02",
    )

    CloseMessageWindow()

    #C0370
    ChrTalk(
        0x104,
        "#0300F嗯，怎么了？\x02",
    )

    CloseMessageWindow()

    #C0371
    ChrTalk(
        0x101,
        (
            "#0000F哦，其实我有个名叫奥斯卡\x01",
            "的童年玩伴就住在西街，\x01",
            "我们约好要见一面的。\x02\x03",

            "我想顺便过去\x01",
            "见见他，可以吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0372
    ChrTalk(
        0x102,
        (
            "#0100F嗯，这也用不了多少时间的，\x01",
            "过去看看也可以吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0373
    ChrTalk(
        0x103,
        "#0200F是在这附近吗？\x02",
    )

    CloseMessageWindow()

    #C0374
    ChrTalk(
        0x101,
        (
            "#0000F嗯，他应该是在一家名叫\x01",
            "摩尔吉的面包店里工作。\x02\x03",

            "虽然和我说过是\x01",
            "一家面朝大街的店……\x01",
            "但究竟在哪里呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_80ED")

    label("loc_809A")


    #C0375
    ChrTalk(
        0x101,
        (
            "#0000F我的一位童年玩伴应该在\x01",
            "一家名叫摩尔吉的面包店里工作。\x02\x03",

            "顺便过去看看吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_80ED")

    Return()

    # Function_33_7F27 end

    SaveToFile()

Try(main)
