from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "c040b.bin",                # FileName
        "c040b",                    # MapName
        "c040b",                    # Location
        0x0022,                     # MapIndex
        "ed7113",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x1D,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 34, 0, 4, 0, 5],
    )

    BuildStringList((
        "c040b",                  # 0
        "索菲尤",                 # 1
        "揽客员皮姆",             # 2
        "珀利塞",                 # 3
        "塔普",                   # 4
        "拉曼达",                 # 5
        "缇乔",                   # 6
        "兔女郎",                 # 7
        "游客",                   # 8
        "游客",                   # 9
        "游客",                   # 10
        "麦克道尔市长",           # 11
        "阿奈斯特秘书",           # 12
        "蔡特",                   # 13
        "达德利搜查官",           # 14
        "赛尔盖科长",             # 15
        "伊莉娅",                 # 16
        "莉夏",                   # 17
        "警备队员",               # 18
        "警备队员",               # 19
        "警备队员",               # 20
        "警备队员",               # 21
        "车１",                   # 22
        "车２",                   # 23
        "客人",                   # 24
        "客人",                   # 25
        "客人",                   # 26
        "客人",                   # 27
        "客人",                   # 28
        "客人",                   # 29
        "客人",                   # 30
        "客人",                   # 31
        "客人",                   # 32
        "客人",                   # 33
        "SE控制",                 # 34
        "中央广场",               # 35
        "西街",                   # 36
        "行政区",                 # 37
        "住宅街",                 # 38
        "欢乐街",                 # 39
        "东街",                   # 40
        "旧城区",                 # 41
        "港湾区",                 # 42
        "ＩＢＣ",                 # 43
        "站前街道",               # 44
        "后巷",                   # 45
        "乌尔斯拉间道",           # 46
        "东克洛斯贝尔街道",       # 47
        "西克洛斯贝尔街道",       # 48
        "玛因兹山道",             # 49
    ))

    AddCharChip((
        "chr/ch20400.itc",                   # 00
        "chr/ch36300.itc",                   # 01
        "chr/ch21900.itc",                   # 02
        "chr/ch34500.itc",                   # 03
        "chr/ch25900.itc",                   # 04
        "chr/ch27100.itc",                   # 05
        "chr/ch32200.itc",                   # 06
        "chr/ch32300.itc",                   # 07
        "chr/ch24400.itc",                   # 08
        "chr/ch33100.itc",                   # 09
    ))

    DeclNpc(-10750,  1759,    24469,   175,  261,  0x0, 0,   3,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(230,     0,       -1830,   175,  277,  0x0, 0,   4,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(379,     1769,    28049,   315,  261,  0x0, 0,   1,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(1830,    1769,    27899,   315,  261,  0x0, 0,   8,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(-50000,  9,       12069,   220,  257,  0x0, 0,   2,   0,   0,   1,   0,   11,  255,  0)
    DeclNpc(15439,   0,       10340,   45,   261,  0x0, 0,   0,   0,   0,   2,   0,   12,  255,  0)
    DeclNpc(-22049,  0,       12489,   175,  261,  0x0, 0,   5,   0,   0,   0,   0,   13,  255,  0)
    DeclNpc(300,     0,       -3799,   355,  277,  0x0, 0,   6,   0,   0,   0,   0,   14,  255,  0)
    DeclNpc(1149,    0,       -4409,   310,  277,  0x0, 0,   7,   0,   0,   0,   0,   15,  255,  0)
    DeclNpc(14829,   0,       2670,    90,   261,  0x0, 0,   9,   0,   0,   0,   0,   16,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 58,  -2.0,                  35.0,                  1.0,                   25.0,                  [0.19999998807907104,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.19999998807907104,   0.0,                   0.3999999761581421,    -17.5,                 -0.19999998807907104,  1.0])

    PlaceName(90.5999984741211, 0.0, -111.88999938964844, 0x0000, 0x0000, "中央广场")
    PlaceName(-19.209999084472656, 0.0, -104.37999725341797, 0x0000, 0x0000, "西街")
    PlaceName(135.69000244140625, 0.0, 36.7400016784668, 0x0000, 0x0000, "行政区")
    PlaceName(-121.08000183105469, 0.0, 20.040000915527344, 0x0000, 0x0000, "住宅街")
    PlaceName(0.8399999737739563, 0.0, 6.679999828338623, 0x0000, 0x0000, "欢乐街")
    PlaceName(226.2899932861328, 0.0, -150.3000030517578, 0x0000, 0x0000, "东街")
    PlaceName(285.57000732421875, 0.0, -242.14999389648438, 0x0000, 0x0000, "旧城区")
    PlaceName(273.04998779296875, 0.0, -40.08000183105469, 0x0000, 0x0000, "港湾区")
    PlaceName(229.6300048828125, 0.0, 116.9000015258789, 0x0000, 0x0000, "ＩＢＣ")
    PlaceName(109.38999938964844, 0.0, -227.1199951171875, 0x0000, 0x0000, "站前街道")
    PlaceName(30.899999618530273, 0.0, -53.439998626708984, 0x0000, 0x0000, "后巷")
    PlaceName(104.37999725341797, 0.0, -278.8900146484375, 0x0000, 0x0000, "乌尔斯拉间道")
    PlaceName(316.4700012207031, 0.0, -126.91999816894531, 0x0000, 0x0000, "东克洛斯贝尔街道")
    PlaceName(-104.37999725341797, 0.0, -106.87999725341797, 0x0000, 0x0000, "西克洛斯贝尔街道")
    PlaceName(-94.36000061035156, 0.0, 60.119998931884766, 0x0000, 0x0000, "玛因兹山道")
    PlaceName(53.86000061035156, 0.0, -135.27000427246094, 0x0000, 0x0051, "")
    PlaceName(143.6199951171875, 0.0, -91.8499984741211, 0x0000, 0x0054, "")
    PlaceName(94.7699966430664, 0.0, -148.6300048828125, 0x0000, 0x0057, "")
    PlaceName(52.61000061035156, 0.0, -86.83999633789062, 0x0000, 0x0053, "")
    PlaceName(86.83999633789062, 0.0, -46.7599983215332, 0x0000, 0x0053, "")
    PlaceName(2.0899999141693115, 0.0, -95.19000244140625, 0x0000, 0x0053, "")
    PlaceName(-14.199999809265137, 0.0, -60.119998931884766, 0x0000, 0x0053, "")
    PlaceName(25.889999389648438, 0.0, -6.679999828338623, 0x0000, 0x0052, "")
    PlaceName(33.81999969482422, 0.0, -28.389999389648438, 0x0000, 0x0053, "")
    PlaceName(48.43000030517578, 0.0, -42.59000015258789, 0x0000, 0x0053, "")
    PlaceName(96.02999877929688, 0.0, 75.98999786376953, 0x0000, 0x0051, "")
    PlaceName(283.07000732421875, 0.0, -150.3000030517578, 0x0000, 0x0052, "")
    PlaceName(254.67999267578125, 0.0, -301.44000244140625, 0x0000, 0x0053, "")
    PlaceName(232.97000122070312, 0.0, -270.5400085449219, 0x0000, 0x0053, "")

    ScpFunction((
        "Function_0_814",          # 00, 0
        "Function_1_8CC",          # 01, 1
        "Function_2_A59",          # 02, 2
        "Function_3_B60",          # 03, 3
        "Function_4_B7C",          # 04, 4
        "Function_5_DF8",          # 05, 5
        "Function_6_E89",          # 06, 6
        "Function_7_FC5",          # 07, 7
        "Function_8_1058",         # 08, 8
        "Function_9_10FE",         # 09, 9
        "Function_10_1136",        # 0A, 10
        "Function_11_11A5",        # 0B, 11
        "Function_12_11CD",        # 0C, 12
        "Function_13_1217",        # 0D, 13
        "Function_14_125F",        # 0E, 14
        "Function_15_129D",        # 0F, 15
        "Function_16_12F6",        # 10, 16
        "Function_17_1353",        # 11, 17
        "Function_18_13A8",        # 12, 18
        "Function_19_13FD",        # 13, 19
        "Function_20_1466",        # 14, 20
        "Function_21_14CF",        # 15, 21
        "Function_22_1538",        # 16, 22
        "Function_23_15A1",        # 17, 23
        "Function_24_160A",        # 18, 24
        "Function_25_1673",        # 19, 25
        "Function_26_16DC",        # 1A, 26
        "Function_27_1745",        # 1B, 27
        "Function_28_17A2",        # 1C, 28
        "Function_29_17DF",        # 1D, 29
        "Function_30_1817",        # 1E, 30
        "Function_31_183D",        # 1F, 31
        "Function_32_1863",        # 20, 32
        "Function_33_1889",        # 21, 33
        "Function_34_18AF",        # 22, 34
        "Function_35_18E9",        # 23, 35
        "Function_36_1923",        # 24, 36
        "Function_37_1E2D",        # 25, 37
        "Function_38_1E6C",        # 26, 38
        "Function_39_1EA1",        # 27, 39
        "Function_40_1F4C",        # 28, 40
        "Function_41_1F86",        # 29, 41
        "Function_42_1FD2",        # 2A, 42
        "Function_43_273D",        # 2B, 43
        "Function_44_2ACE",        # 2C, 44
        "Function_45_3AA0",        # 2D, 45
        "Function_46_3B09",        # 2E, 46
        "Function_47_3C08",        # 2F, 47
        "Function_48_3C97",        # 30, 48
        "Function_49_3CE1",        # 31, 49
        "Function_50_3D2E",        # 32, 50
        "Function_51_3D95",        # 33, 51
        "Function_52_3DEE",        # 34, 52
        "Function_53_3F3E",        # 35, 53
        "Function_54_3F8B",        # 36, 54
        "Function_55_3FE0",        # 37, 55
        "Function_56_4036",        # 38, 56
        "Function_57_4099",        # 39, 57
        "Function_58_40B3",        # 3A, 58
        "Function_59_41AA",        # 3B, 59
        "Function_60_41C6",        # 3C, 60
        "Function_61_41E2",        # 3D, 61
        "Function_62_41FE",        # 3E, 62
    ))


    def Function_0_814(): pass

    label("Function_0_814")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_854"),
        (1, "loc_860"),
        (2, "loc_86C"),
        (3, "loc_878"),
        (4, "loc_884"),
        (5, "loc_890"),
        (6, "loc_89C"),
        (SWITCH_DEFAULT, "loc_8A8"),
    )


    label("loc_854")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_8B4")

    label("loc_860")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_8B4")

    label("loc_86C")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_8B4")

    label("loc_878")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_8B4")

    label("loc_884")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_8B4")

    label("loc_890")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_8B4")

    label("loc_89C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_8B4")

    label("loc_8A8")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_8B4")

    label("loc_8B4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_8CB")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_8B4")

    label("loc_8CB")

    Return()

    # Function_0_814 end

    def Function_1_8CC(): pass

    label("Function_1_8CC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A58")
    SetChrPos(0xFE, -50000, 10, 12070, 220)
    OP_95(0xFE, -18740, 10, 10280, 1500, 0x0)
    OP_95(0xFE, -2040, 1770, 9880, 1500, 0x0)
    OP_95(0xFE, 30970, 0, 12150, 1500, 0x0)
    Sleep(1500)
    SetChrPos(0xFE, 30210, 0, 8600, 270)
    OP_95(0xFE, 17210, 0, 8600, 1500, 0x0)
    OP_95(0xFE, 15010, 0, 6790, 1500, 0x0)
    OP_95(0xFE, 10210, 0, -960, 1500, 0x0)
    OP_95(0xFE, 8450, 0, -7690, 1500, 0x0)
    OP_95(0xFE, 10100, 0, -11960, 1500, 0x0)
    OP_95(0xFE, 28170, 0, -38880, 1500, 0x0)
    Sleep(1500)
    SetChrPos(0xFE, 28170, 0, -38880, 315)
    OP_95(0xFE, 9370, 0, -17000, 1500, 0x0)
    OP_95(0xFE, 4280, 0, -11560, 1500, 0x0)
    OP_95(0xFE, -4810, 0, -3900, 1500, 0x0)
    OP_95(0xFE, -13140, 0, 1410, 1500, 0x0)
    OP_95(0xFE, -21060, 0, 5360, 1500, 0x0)
    OP_95(0xFE, -26790, 0, 8090, 1500, 0x0)
    OP_95(0xFE, -50000, 10, 12070, 1500, 0x0)
    Sleep(1500)
    Jump("Function_1_8CC")

    label("loc_A58")

    Return()

    # Function_1_8CC end

    def Function_2_A59(): pass

    label("Function_2_A59")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_B5F")
    OP_95(0xFE, 8780, 0, 6460, 1000, 0x0)
    OP_95(0xFE, 2270, 0, 3060, 1000, 0x0)
    OP_95(0xFE, -5460, 0, 2360, 1000, 0x0)
    OP_95(0xFE, -14070, 0, 5650, 1000, 0x0)
    OP_95(0xFE, -19800, 0, 8020, 1000, 0x0)
    OP_95(0xFE, -26870, 0, 10100, 1000, 0x0)
    Sleep(1500)
    OP_95(0xFE, -19800, 0, 8020, 1000, 0x0)
    OP_95(0xFE, -14070, 0, 5650, 1000, 0x0)
    OP_95(0xFE, -5460, 0, 2360, 1000, 0x0)
    OP_95(0xFE, 2270, 0, 3060, 1000, 0x0)
    OP_95(0xFE, 8780, 0, 6460, 1000, 0x0)
    OP_95(0xFE, 11400, 0, 7650, 1000, 0x0)
    Sleep(1500)
    Jump("Function_2_A59")

    label("loc_B5F")

    Return()

    # Function_2_A59 end

    def Function_3_B60(): pass

    label("Function_3_B60")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_B7B")
    OP_A1(0xFE, 0x5DC, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Jump("Function_3_B60")

    label("loc_B7B")

    Return()

    # Function_3_B60 end

    def Function_4_B7C(): pass

    label("Function_4_B7C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6B), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D93")
    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_C47")
    SetChrPos(0x0, 21040, 0, 11840, 270)
    SetChrPos(0x1, 21040, 0, 11840, 270)
    SetChrPos(0x2, 21040, 0, 11840, 270)
    SetChrPos(0x3, 21040, 0, 11840, 270)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C23")
    SetChrPos(0x4, 21040, 0, 11840, 270)
    SetChrPos(0x5, 21040, 0, 11840, 270)
    Jump("loc_C42")

    label("loc_C23")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C42")
    SetChrPos(0x4, 21040, 0, 11840, 270)

    label("loc_C42")

    Jump("loc_D93")

    label("loc_C47")

    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_CFB")
    SetChrPos(0x0, -39280, 0, 12420, 90)
    SetChrPos(0x1, -39280, 0, 12420, 90)
    SetChrPos(0x2, -39280, 0, 12420, 90)
    SetChrPos(0x3, -39280, 0, 12420, 90)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CD7")
    SetChrPos(0x4, -39280, 0, 12420, 90)
    SetChrPos(0x5, -39280, 0, 12420, 90)
    Jump("loc_CF6")

    label("loc_CD7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CF6")
    SetChrPos(0x4, -39280, 0, 12420, 90)

    label("loc_CF6")

    Jump("loc_D93")

    label("loc_CFB")

    SetChrPos(0x0, 13270, 0, -19100, 315)
    SetChrPos(0x1, 13270, 0, -19100, 315)
    SetChrPos(0x2, 13270, 0, -19100, 315)
    SetChrPos(0x3, 13270, 0, -19100, 315)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D74")
    SetChrPos(0x4, 13270, 0, -19100, 315)
    SetChrPos(0x5, 13270, 0, -19100, 315)
    Jump("loc_D93")

    label("loc_D74")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D93")
    SetChrPos(0x4, 13270, 0, -19100, 315)

    label("loc_D93")

    OP_D0(0x7, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_DAD")
    Event(0, 43)

    label("loc_DAD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_DC1")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 36)
    Jump("loc_DE4")

    label("loc_DC1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 1)), scpexpr(EXPR_END)), "loc_DD5")
    ClearScenarioFlags(0x5C, 1)
    Event(0, 42)
    Jump("loc_DE4")

    label("loc_DD5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 2)), scpexpr(EXPR_END)), "loc_DE4")
    ClearScenarioFlags(0x5C, 2)
    Event(0, 44)

    label("loc_DE4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_DF7")
    ClearChrFlags(0x9, 0x10)
    ClearChrFlags(0xF, 0x10)

    label("loc_DF7")

    Return()

    # Function_4_B7C end

    def Function_5_DF8(): pass

    label("Function_5_DF8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x84, 4)), scpexpr(EXPR_END)), "loc_E1E")
    SetMapObjFrame(0xFF, "ka01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "ka02", 0x1, 0x1)
    Jump("loc_E36")

    label("loc_E1E")

    SetMapObjFrame(0xFF, "ka01", 0x1, 0x1)
    SetMapObjFrame(0xFF, "ka02", 0x0, 0x1)

    label("loc_E36")

    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E4E")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_E4E")

    OP_1B(0x1, 0xFF, 0xFFFF)
    OP_1B(0x2, 0xFF, 0xFFFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E70")
    OP_1B(0x1, 0x0, 0x3B)
    OP_1B(0x2, 0x0, 0x3C)

    label("loc_E70")

    OP_1B(0x0, 0xFF, 0xFFFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E88")
    OP_1B(0x0, 0x0, 0x3D)

    label("loc_E88")

    Return()

    # Function_5_DF8 end

    def Function_6_E89(): pass

    label("Function_6_E89")

    TalkBegin(0xFE)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_E96")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FC1")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "对话\x01",      # 0
            "购物\x01",      # 1
            "放弃\x01",      # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_EE6")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_EE6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F06")
    OP_AF(0x7E)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_FBC")

    label("loc_F06")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F1A")
    Jump("loc_FBC")

    label("loc_F1A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FBC")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_F6C")

    #C0001
    ChrTalk(
        0x8,
        (
            "做生意真辛苦啊～\x01",
            "这就是所谓的命运吗～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FBC")

    label("loc_F6C")


    #C0002
    ChrTalk(
        0x8,
        "夜晚的克洛斯贝尔真美啊～\x02",
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0x8,
        (
            "要是我不用做生意的话，\x01",
            "就可以到处去玩了～\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_FBC")

    Jump("loc_E96")

    label("loc_FC1")

    TalkEnd(0xFE)
    Return()

    # Function_6_E89 end

    def Function_7_FC5(): pass

    label("Function_7_FC5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1051")

    #C0004
    ChrTalk(
        0xFE,
        (
            "啊，你们也是出来玩的吗？\x01",
            "在我们这里可以喝到美酒哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0xFE,
        (
            "嘿嘿，四个人的话，\x01",
            "还可以打个团体折呢。\x01",
            "怎么样？考虑考虑吧！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1054")

    label("loc_1051")

    Call(0, 8)

    label("loc_1054")

    TalkEnd(0xFE)
    Return()

    # Function_7_FC5 end

    def Function_8_1058(): pass

    label("Function_8_1058")

    OP_4B(0x9, 0xFF)
    OP_4B(0xF, 0xFF)

    #C0006
    ChrTalk(
        0xF,
        "真、真的没问题吗？\x02",
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0xF,
        (
            "那个，虽然我有点兴趣，\x01",
            "不过好像有点可怕呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x9,
        "啊哈哈哈哈哈哈……！\x02",
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x9,
        (
            "没关系啦，\x01",
            "我可不是什么坏人。\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x9, 0x10)
    ClearChrFlags(0xF, 0x10)
    SetScenarioFlags(0x0, 1)
    OP_4C(0x9, 0xFF)
    OP_4C(0xF, 0xFF)
    Return()

    # Function_8_1058 end

    def Function_9_10FE(): pass

    label("Function_9_10FE")

    TalkBegin(0xFE)

    #C0010
    ChrTalk(
        0xA,
        (
            "呀，就快到公演时间了呢！\x01",
            "心跳得好厉害哦～！\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_9_10FE end

    def Function_10_1136(): pass

    label("Function_10_1136")

    TalkBegin(0xFE)

    #C0011
    ChrTalk(
        0xB,
        "夜晚的欢乐街真令人紧张兴奋啊……\x02",
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0xB,
        (
            "可恶，要是有票的话，\x01",
            "就可以尽情欣赏\x01",
            "彩虹剧团的舞台表演了……\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_10_1136 end

    def Function_11_11A5(): pass

    label("Function_11_11A5")

    TalkBegin(0xFE)

    #C0013
    ChrTalk(
        0xC,
        (
            "呵呵，今晚\x01",
            "要去哪里玩呢……\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_11_11A5 end

    def Function_12_11CD(): pass

    label("Function_12_11CD")

    TalkBegin(0xFE)

    #C0014
    ChrTalk(
        0xD,
        "好，今晚也要玩个痛快！\x02",
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0xD,
        (
            "先去『巴鲁卡』\x01",
            "试试今天的运气吧！\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_12_11CD end

    def Function_13_1217(): pass

    label("Function_13_1217")

    TalkBegin(0xFE)

    #C0016
    ChrTalk(
        0xE,
        "Ｈｅｌｌｏ～怎么样～☆\x02",
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0xE,
        (
            "『巴鲁卡』\x01",
            "今天也生意兴隆哦～！\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_13_1217 end

    def Function_14_125F(): pass

    label("Function_14_125F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1296")

    #C0018
    ChrTalk(
        0xF,
        (
            "咳、咳咳……\x01",
            "不要告诉\x01",
            "我太太哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1299")

    label("loc_1296")

    Call(0, 8)

    label("loc_1299")

    TalkEnd(0xFE)
    Return()

    # Function_14_125F end

    def Function_15_129D(): pass

    label("Function_15_129D")

    TalkBegin(0xFE)
    OP_4B(0x9, 0xFF)
    OP_4B(0xF, 0xFF)

    #C0019
    ChrTalk(
        0x10,
        (
            "哦，前辈，\x01",
            "你要去吗～？\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x10,
        (
            "嘿嘿嘿……我也\x01",
            "开始有点兴趣了～\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x9, 0xFF)
    OP_4C(0xF, 0xFF)
    TalkEnd(0xFE)
    Return()

    # Function_15_129D end

    def Function_16_12F6(): pass

    label("Function_16_12F6")

    TalkBegin(0xFE)

    #C0021
    ChrTalk(
        0xFE,
        (
            "我太太和女儿去购物以后，\x01",
            "就一直没回来啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0xFE,
        (
            "唉，没办法。\x01",
            "只能先回旅馆了吗……\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_16_12F6 end

    def Function_17_1353(): pass

    label("Function_17_1353")

    ClearChrFlags(0xFE, 0x80)
    ClearChrBattleFlags(0xFE, 0x8000)
    SetChrPos(0xFE, -2550, 1860, 25760, 0)
    OP_95(0xFE, -2550, 2660, 35120, 1000, 0x0)

    def lambda_1387():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1387)
    OP_97(0xFE, 0x0, 0x0, 0x5DC, 0x5DC, 0x0)
    Return()

    # Function_17_1353 end

    def Function_18_13A8(): pass

    label("Function_18_13A8")

    ClearChrFlags(0xFE, 0x80)
    ClearChrBattleFlags(0xFE, 0x8000)
    SetChrPos(0xFE, -1280, 1990, 24700, 0)
    OP_95(0xFE, -1390, 2660, 35120, 1000, 0x0)

    def lambda_13DC():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_13DC)
    OP_97(0xFE, 0x0, 0x0, 0x5DC, 0x5DC, 0x0)
    Return()

    # Function_18_13A8 end

    def Function_19_13FD(): pass

    label("Function_19_13FD")

    ClearChrFlags(0xFE, 0x80)
    ClearChrBattleFlags(0xFE, 0x8000)
    SetChrPos(0xFE, 4520, 1890, 19530, 333)
    OP_95(0xFE, -1330, 2150, 30540, 1000, 0x0)
    OP_95(0xFE, -1390, 2660, 35120, 1000, 0x0)

    def lambda_1445():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1445)
    OP_97(0xFE, 0x0, 0x0, 0x5DC, 0x5DC, 0x0)
    Return()

    # Function_19_13FD end

    def Function_20_1466(): pass

    label("Function_20_1466")

    ClearChrFlags(0xFE, 0x80)
    ClearChrBattleFlags(0xFE, 0x8000)
    SetChrPos(0xFE, 4040, 1950, 18100, 333)
    OP_95(0xFE, -2660, 2430, 31010, 1000, 0x0)
    OP_95(0xFE, -1390, 2660, 35120, 1000, 0x0)

    def lambda_14AE():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_14AE)
    OP_97(0xFE, 0x0, 0x0, 0x5DC, 0x5DC, 0x0)
    Return()

    # Function_20_1466 end

    def Function_21_14CF(): pass

    label("Function_21_14CF")

    ClearChrFlags(0xFE, 0x80)
    ClearChrBattleFlags(0xFE, 0x8000)
    SetChrPos(0xFE, -7760, 1920, 21240, 26)
    OP_95(0xFE, -2950, 1760, 29310, 1000, 0x0)
    OP_95(0xFE, -2800, 2660, 35080, 1000, 0x0)

    def lambda_1517():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1517)
    OP_97(0xFE, 0x0, 0x0, 0x5DC, 0x5DC, 0x0)
    Return()

    # Function_21_14CF end

    def Function_22_1538(): pass

    label("Function_22_1538")

    ClearChrFlags(0xFE, 0x80)
    ClearChrBattleFlags(0xFE, 0x8000)
    SetChrPos(0xFE, -7210, 1990, 19830, 26)
    OP_95(0xFE, -1240, 1760, 29900, 1000, 0x0)
    OP_95(0xFE, -1600, 2660, 35120, 1000, 0x0)

    def lambda_1580():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1580)
    OP_97(0xFE, 0x0, 0x0, 0x5DC, 0x5DC, 0x0)
    Return()

    # Function_22_1538 end

    def Function_23_15A1(): pass

    label("Function_23_15A1")

    ClearChrFlags(0xFE, 0x80)
    ClearChrBattleFlags(0xFE, 0x8000)
    SetChrPos(0xFE, -30, 1810, 12140, 341)
    OP_95(0xFE, -2950, 1760, 29310, 1000, 0x0)
    OP_95(0xFE, -2800, 2660, 35080, 1000, 0x0)

    def lambda_15E9():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_15E9)
    OP_97(0xFE, 0x0, 0x0, 0x5DC, 0x5DC, 0x0)
    Return()

    # Function_23_15A1 end

    def Function_24_160A(): pass

    label("Function_24_160A")

    ClearChrFlags(0xFE, 0x80)
    ClearChrBattleFlags(0xFE, 0x8000)
    SetChrPos(0xFE, 1150, 1760, 11990, 341)
    OP_95(0xFE, -1240, 1760, 29900, 1000, 0x0)
    OP_95(0xFE, -1600, 2660, 35120, 1000, 0x0)

    def lambda_1652():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1652)
    OP_97(0xFE, 0x0, 0x0, 0x5DC, 0x5DC, 0x0)
    Return()

    # Function_24_160A end

    def Function_25_1673(): pass

    label("Function_25_1673")

    ClearChrFlags(0xFE, 0x80)
    ClearChrBattleFlags(0xFE, 0x8000)
    SetChrPos(0xFE, -5550, 1990, 15680, 26)
    OP_95(0xFE, -2950, 1760, 29310, 1000, 0x0)
    OP_95(0xFE, -2800, 2660, 35080, 1000, 0x0)

    def lambda_16BB():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_16BB)
    OP_97(0xFE, 0x0, 0x0, 0x5DC, 0x5DC, 0x0)
    Return()

    # Function_25_1673 end

    def Function_26_16DC(): pass

    label("Function_26_16DC")

    ClearChrFlags(0xFE, 0x80)
    ClearChrBattleFlags(0xFE, 0x8000)
    SetChrPos(0xFE, -4270, 1990, 16100, 26)
    OP_95(0xFE, -1240, 1760, 29900, 1000, 0x0)
    OP_95(0xFE, -1600, 2660, 35120, 1000, 0x0)

    def lambda_1724():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1724)
    OP_97(0xFE, 0x0, 0x0, 0x5DC, 0x5DC, 0x0)
    Return()

    # Function_26_16DC end

    def Function_27_1745(): pass

    label("Function_27_1745")

    OP_95(0xFE, -8970, 330, 5920, 2000, 0x0)
    OP_93(0xFE, 0x109, 0x1F4)

    def lambda_1765():

        label("loc_1765")

        TurnDirection(0xFE, 0x12, 500)
        Yield()
        Jump("loc_1765")

    QueueWorkItem2(0xFE, 2, lambda_1765)
    Sleep(2500)
    EndChrThread(0xFE, 0x2)
    OP_95(0xFE, -7220, 1770, 9000, 1200, 0x0)
    OP_95(0xFE, -2350, 1990, 19350, 1200, 0x0)
    Return()

    # Function_27_1745 end

    def Function_28_17A2(): pass

    label("Function_28_17A2")

    OP_95(0xFE, -10140, 250, 6390, 1200, 0x0)
    OP_95(0xFE, -8109, 1770, 9690, 1200, 0x0)
    OP_95(0xFE, -3180, 1990, 19840, 1200, 0x0)
    Return()

    # Function_28_17A2 end

    def Function_29_17DF(): pass

    label("Function_29_17DF")

    OP_9F(0x0, 0x1D)
    OP_9F(0x1, -28630, 0, 10380)
    OP_9F(0x1, -19800, 0, 9100)
    OP_9F(0x1, -11600, 0, 3800)
    OP_9F(0x2, 0x1D, 5000, 0x6)
    Return()

    # Function_29_17DF end

    def Function_30_1817(): pass

    label("Function_30_1817")

    SetChrPos(0xFE, 470, 1770, 10040, 45)
    OP_95(0xFE, -3140, 1760, 29500, 1500, 0x0)
    Return()

    # Function_30_1817 end

    def Function_31_183D(): pass

    label("Function_31_183D")

    SetChrPos(0xFE, 1910, 1770, 10160, 45)
    OP_95(0xFE, -1330, 1760, 29360, 1500, 0x0)
    Return()

    # Function_31_183D end

    def Function_32_1863(): pass

    label("Function_32_1863")

    SetChrPos(0xFE, -6160, 1590, 7540, 315)
    OP_95(0xFE, -3140, 1760, 29500, 1500, 0x0)
    Return()

    # Function_32_1863 end

    def Function_33_1889(): pass

    label("Function_33_1889")

    SetChrPos(0xFE, -5150, 1640, 7470, 314)
    OP_95(0xFE, -1330, 1760, 29360, 1500, 0x0)
    Return()

    # Function_33_1889 end

    def Function_34_18AF(): pass

    label("Function_34_18AF")

    SetChrPos(0xFE, -7000, 690, 5700, 314)
    OP_95(0xFE, -6030, 1770, 9130, 1200, 0x0)
    OP_95(0xFE, -3140, 1760, 29500, 1200, 0x0)
    Return()

    # Function_34_18AF end

    def Function_35_18E9(): pass

    label("Function_35_18E9")

    SetChrPos(0xFE, -5600, 740, 5500, 44)
    OP_95(0xFE, -4950, 1770, 8820, 1200, 0x0)
    OP_95(0xFE, -1330, 1760, 29360, 1200, 0x0)
    Return()

    # Function_35_18E9 end

    def Function_36_1923(): pass

    label("Function_36_1923")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SoundLoad(803)
    LoadChrToIndex("chr/ch05800.itc", 0x1E)
    LoadChrToIndex("chr/ch02300.itc", 0x1F)
    LoadChrToIndex("chr/ch02700.itc", 0x20)
    LoadChrToIndex("chr/ch33000.itc", 0x28)
    LoadChrToIndex("chr/ch33300.itc", 0x29)
    LoadChrToIndex("chr/ch27700.itc", 0x2A)
    LoadChrToIndex("chr/ch27600.itc", 0x2B)
    LoadChrToIndex("chr/ch33100.itc", 0x2C)
    LoadChrToIndex("chr/ch32400.itc", 0x2D)
    LoadChrToIndex("chr/ch22000.itc", 0x2E)
    LoadChrToIndex("chr/ch33200.itc", 0x2F)
    LoadChrToIndex("chr/ch27800.itc", 0x30)
    LoadChrToIndex("chr/ch27900.itc", 0x31)
    SetChrChipByIndex(0x1F, 0x28)
    SetChrChipByIndex(0x20, 0x29)
    SetChrChipByIndex(0x21, 0x2A)
    SetChrChipByIndex(0x22, 0x2B)
    SetChrChipByIndex(0x23, 0x2C)
    SetChrChipByIndex(0x24, 0x2D)
    SetChrChipByIndex(0x25, 0x2E)
    SetChrChipByIndex(0x26, 0x2F)
    SetChrChipByIndex(0x27, 0x30)
    SetChrChipByIndex(0x28, 0x31)
    SetChrFlags(0x1F, 0x8000)
    SetChrFlags(0x20, 0x8000)
    SetChrFlags(0x21, 0x8000)
    SetChrFlags(0x22, 0x8000)
    SetChrFlags(0x23, 0x8000)
    SetChrFlags(0x24, 0x8000)
    SetChrFlags(0x25, 0x8000)
    SetChrFlags(0x26, 0x8000)
    SetChrFlags(0x27, 0x8000)
    SetChrFlags(0x28, 0x8000)
    ClearChrFlags(0x1F, 0x4)
    ClearChrFlags(0x20, 0x4)
    ClearChrFlags(0x21, 0x4)
    ClearChrFlags(0x22, 0x4)
    ClearChrFlags(0x23, 0x4)
    ClearChrFlags(0x24, 0x4)
    ClearChrFlags(0x25, 0x4)
    ClearChrFlags(0x26, 0x4)
    ClearChrFlags(0x27, 0x4)
    ClearChrFlags(0x28, 0x4)
    SetChrFlags(0x12, 0x8000)
    SetChrFlags(0x13, 0x8000)
    ClearChrFlags(0x12, 0x4)
    ClearChrFlags(0x13, 0x4)
    OP_68(-14500, 1950, 7000, 0)
    MoveCamera(40, 8, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(16500, 0)
    SetChrChipByIndex(0x12, 0x1E)
    SetChrSubChip(0x12, 0x0)
    SetChrPos(0x12, -3000, 1990, 20500, 180)
    SetChrChipByIndex(0x13, 0x1F)
    SetChrSubChip(0x13, 0x0)
    SetChrPos(0x13, -3000, 1990, 21500, 180)
    ClearChrFlags(0x1D, 0x80)
    OP_78(0x4, 0x1D)
    SetMapObjFrame(0x4, "light", 0x0, 0x1)
    OP_49()
    SetChrPos(0x1D, -28630, 0, 10380, 130)
    SetMapObjFlags(0x4, 0x1000)
    OP_74(0x4, 0x1E)
    OP_71(0x4, 0x79, 0xB4, 0x0, 0x20)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)
    SetChrFlags(0xE, 0x80)
    SetChrBattleFlags(0xE, 0x8000)
    SetChrFlags(0xF, 0x80)
    SetChrBattleFlags(0xF, 0x8000)
    SetChrFlags(0x10, 0x80)
    SetChrBattleFlags(0x10, 0x8000)
    SetChrFlags(0x11, 0x80)
    SetChrBattleFlags(0x11, 0x8000)
    OP_71(0x3, 0xA, 0x0, 0x0, 0x0)
    ClearMapObjFlags(0x3, 0x10)
    SetMapObjFrame(0xFF, "ka01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "ka02", 0x1, 0x1)
    BeginChrThread(0x29, 0, 0, 37)
    FadeToBright(3000, 0)
    OP_68(-2580, 10570, 29050, 0)
    MoveCamera(20, 3, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(36500, 0)
    OP_68(-2580, 10570, 29050, 14000)
    MoveCamera(345, -13, 0, 14000)
    OP_6E(800, 14000)
    SetCameraDistance(36500, 14000)
    BeginChrThread(0x1F, 0, 0, 17)
    BeginChrThread(0x20, 0, 0, 18)
    BeginChrThread(0x21, 0, 0, 19)
    BeginChrThread(0x22, 0, 0, 20)
    BeginChrThread(0x23, 0, 0, 21)
    BeginChrThread(0x24, 0, 0, 22)
    BeginChrThread(0x25, 0, 0, 23)
    BeginChrThread(0x26, 0, 0, 24)
    BeginChrThread(0x27, 0, 0, 25)
    BeginChrThread(0x28, 0, 0, 26)
    Sleep(6000)
    BeginChrThread(0x1D, 0, 0, 29)
    Sleep(2000)
    Fade(500)
    Fade(500)
    Sound(459, 0, 100, 0)
    EndChrThread(0x29, 0x0)
    BeginChrThread(0x1F, 0, 0, 30)
    BeginChrThread(0x20, 0, 0, 31)
    BeginChrThread(0x21, 0, 0, 32)
    BeginChrThread(0x22, 0, 0, 33)
    BeginChrThread(0x23, 0, 0, 34)
    BeginChrThread(0x24, 0, 0, 35)
    OP_68(-10140, 2050, 6000, 0)
    MoveCamera(12, 26, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(22500, 0)
    OP_6E(600, 10000)
    WaitChrThread(0x1D, 0)
    OP_71(0x4, 0x5B, 0x78, 0x0, 0x0)
    OP_79(0x4)
    OP_71(0x4, 0xF1, 0x10E, 0x0, 0x0)
    Sound(462, 0, 100, 0)
    OP_79(0x4)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x12, -10990, 0, 4660, 208)
    SetChrPos(0x13, -10990, 0, 4660, 208)
    BeginChrThread(0x13, 0, 0, 27)
    Sleep(1500)
    BeginChrThread(0x12, 0, 0, 28)
    Sleep(1600)
    OP_71(0x4, 0x10F, 0x12C, 0x0, 0x0)
    Sound(461, 0, 100, 0)
    OP_79(0x4)
    Sleep(1500)
    Fade(500)
    OP_68(10490, 2380, 14240, 0)
    MoveCamera(359, 11, 0, 0)
    OP_6E(580, 0)
    SetCameraDistance(17000, 0)
    OP_68(10490, 2380, 14240, 6000)
    MoveCamera(19, 19, 0, 6000)
    OP_6E(580, 6000)
    SetCameraDistance(17000, 6000)
    SetChrPos(0x104, 13520, 0, 14590, 270)

    def lambda_1D63():
        OP_95(0xFE, 8590, 1770, 14770, 1300, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_1D63)
    SetChrPos(0x103, 15170, 0, 14690, 270)

    def lambda_1D8E():
        OP_95(0xFE, 9760, 1400, 14890, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_1D8E)
    SetChrChipByIndex(0x14, 0x20)
    SetChrSubChip(0x14, 0x0)
    SetChrFlags(0x14, 0x8000)
    ClearChrFlags(0x14, 0x4)
    SetChrPos(0x14, 15760, 0, 13260, 272)
    ClearChrFlags(0x14, 0x80)
    ClearChrBattleFlags(0x14, 0x8000)

    def lambda_1DD5():
        OP_95(0xFE, 9320, 1410, 13720, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_1DD5)
    OP_71(0x3, 0x0, 0xA, 0x0, 0x0)
    Sleep(3000)
    BeginChrThread(0x29, 0, 0, 38)
    FadeToDark(1000, 0, -1)
    OP_0D()
    WaitChrThread(0x29, 1)
    RemoveParty(0x2, 0x0)
    RemoveParty(0x3, 0x0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x71), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_24(0x323)
    SetScenarioFlags(0x5C, 1)
    NewScene("e3400", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_36_1923 end

    def Function_37_1E2D(): pass

    label("Function_37_1E2D")

    Sound(803, 2, 0, 0)
    Sleep(100)
    OP_25(0x323, 0xA)
    Sleep(100)
    OP_25(0x323, 0x14)
    Sleep(100)
    OP_25(0x323, 0x1E)
    Sleep(100)
    OP_25(0x323, 0x28)
    Sleep(100)
    OP_25(0x323, 0x32)
    Sleep(100)
    OP_25(0x323, 0x3C)
    Sleep(100)
    OP_25(0x323, 0x46)
    Sleep(100)
    OP_25(0x323, 0x50)
    Return()

    # Function_37_1E2D end

    def Function_38_1E6C(): pass

    label("Function_38_1E6C")

    OP_25(0x323, 0x46)
    Sleep(100)
    OP_25(0x323, 0x3C)
    Sleep(100)
    OP_25(0x323, 0x32)
    Sleep(100)
    OP_25(0x323, 0x28)
    Sleep(100)
    OP_25(0x323, 0x1E)
    Sleep(100)
    OP_25(0x323, 0x14)
    Sleep(100)
    OP_25(0x323, 0xA)
    Sleep(100)
    OP_24(0x323)
    Return()

    # Function_38_1E6C end

    def Function_39_1EA1(): pass

    label("Function_39_1EA1")

    SetChrChipByIndex(0x13, 0x20)
    SetChrSubChip(0x13, 0x0)

    def lambda_1EAE():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1EAE)
    OP_95(0xFE, -2210, 2660, 31430, 5000, 0x0)
    OP_95(0xFE, -2210, 1760, 27140, 5000, 0x0)
    PlayEffect(0x1, 0xFF, 0xFE, 0x0, 0, 1000, 0, 0, 0, 0, 500, 500, 500, 0xFF, 0, 1000, 0, 0)
    OP_82(0x0, 0xC8, 0xBB8, 0x1F4)
    SetChrFlags(0x13, 0x20)
    SetChrChipByIndex(0x13, 0x21)
    SetChrSubChip(0x13, 0x0)
    OP_95(0xFE, -2360, 1940, 25100, 5000, 0x0)
    Return()

    # Function_39_1EA1 end

    def Function_40_1F4C(): pass

    label("Function_40_1F4C")


    def lambda_1F51():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1F51)
    OP_95(0xFE, -2720, 2660, 31430, 5000, 0x0)
    OP_95(0xFE, -2720, 1760, 29040, 5000, 0x0)
    Return()

    # Function_40_1F4C end

    def Function_41_1F86(): pass

    label("Function_41_1F86")

    ClearChrFlags(0xFE, 0x80)
    ClearChrBattleFlags(0xFE, 0x8000)
    SetChrChipByIndex(0xFE, 0x29)

    def lambda_1F99():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1F99)
    OP_95(0xFE, -1310, 2580, 31270, 5000, 0x0)
    OP_95(0xFE, -1170, 1760, 29010, 5000, 0x0)
    SetChrChipByIndex(0xFE, 0x28)
    Return()

    # Function_41_1F86 end

    def Function_42_1FD2(): pass

    label("Function_42_1FD2")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00900.itc", 0x1E)
    LoadChrToIndex("chr/ch02300.itc", 0x1F)
    LoadChrToIndex("apl/ch50229.itc", 0x20)
    LoadChrToIndex("apl/ch50230.itc", 0x21)
    LoadChrToIndex("apl/ch50232.itc", 0x22)
    LoadChrToIndex("apl/ch50233.itc", 0x23)
    LoadChrToIndex("chr/ch00950.itc", 0x28)
    LoadChrToIndex("chr/ch00951.itc", 0x29)
    LoadChrToIndex("chr/ch00050.itc", 0x2A)
    LoadChrToIndex("chr/ch00051.itc", 0x2B)
    LoadChrToIndex("chr/ch00350.itc", 0x2D)
    LoadChrToIndex("chr/ch00356.itc", 0x2E)
    LoadChrToIndex("chr/ch00351.itc", 0x2F)
    LoadChrToIndex("chr/ch00250.itc", 0x30)
    LoadChrToIndex("chr/ch00251.itc", 0x31)
    LoadChrToIndex("chr/ch00252.itc", 0x32)
    LoadChrToIndex("apl/ch50231.itc", 0x33)
    ClearMapObjFlags(0x3, 0x10)
    OP_70(0x3, 0xA)
    SetChrChipByIndex(0x103, 0x30)
    SetChrFlags(0x15, 0x8000)
    SetChrChipByIndex(0x15, 0x28)
    SetChrSubChip(0x15, 0x0)
    SetChrFlags(0x13, 0x8000)
    SetChrChipByIndex(0x13, 0x1F)
    SetChrSubChip(0x13, 0x0)
    ClearChrFlags(0x13, 0x80)
    ClearChrBattleFlags(0x13, 0x8000)
    OP_A7(0x13, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x101, 0x2A)
    SetChrChipByIndex(0x104, 0x2D)
    SetChrPos(0x101, -2160, 2660, 36390, 180)
    SetChrPos(0x15, -2160, 2660, 36390, 180)
    SetChrPos(0x13, -2160, 2660, 36390, 180)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x15, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x13, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x104, -2660, 1990, 18290, 0)
    SetChrPos(0x103, 3680, 1960, 17210, 135)
    LoadEffect(0x0, "event\\ev201_00.eff")
    LoadEffect(0x1, "battle\\ms00004.eff")
    OP_68(-2160, 4600, 35160, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(480, 0)
    SetCameraDistance(21500, 0)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)
    SetChrFlags(0xE, 0x80)
    SetChrBattleFlags(0xE, 0x8000)
    SetChrFlags(0xF, 0x80)
    SetChrBattleFlags(0xF, 0x8000)
    SetChrFlags(0x10, 0x80)
    SetChrBattleFlags(0x10, 0x8000)
    SetChrFlags(0x11, 0x80)
    SetChrBattleFlags(0x11, 0x8000)
    FadeToBright(1000, 0)
    BeginChrThread(0x13, 0, 0, 39)
    OP_68(-2040, 2800, 25190, 3000)
    MoveCamera(45, 25, 0, 3000)
    OP_6E(480, 3000)
    SetCameraDistance(21500, 3000)
    Sleep(1000)
    Sound(1221, 255, 100, 0)    #voice#Tio
    Sleep(500)
    SetChrPos(0x1D, -2210, 1760, 25140, 0)
    PlayEffect(0x0, 0xFF, 0x103, 0x0, 0, 1600, 0, 0, 0, 0, 1000, 1000, 1000, 0x1D, 0, 1000, 0, 0)
    Sound(255, 0, 100, 0)
    Sleep(250)
    Sound(1876, 255, 100, 2)    #voice#Earnest
    Sound(251, 0, 100, 0)
    WaitChrThread(0x13, 0)
    Sleep(500)

    def lambda_226D():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_226D)
    SetChrChipByIndex(0x13, 0x33)
    SetChrSubChip(0x13, 0x0)
    SetChrFlags(0x13, 0x2)
    Sound(1320, 255, 100, 1)    #voice#Randy
    SetChrFlags(0x104, 0x20)
    SetChrFlags(0x104, 0x1000)
    SetChrChipByIndex(0x104, 0x2E)
    SetChrSubChip(0x104, 0x0)
    Sound(250, 0, 100, 0)
    Sleep(100)
    SetChrChip(0x0, 0x104, 0x32, 0x12C)
    SetChrSubChip(0x104, 0x1)
    OP_99(0x104, 0x13, 0x1F4, 0x2328, 0x0)
    SetChrChipByIndex(0x13, 0x22)
    SetChrSubChip(0x13, 0x0)
    ClearChrFlags(0x13, 0x2)
    OP_82(0x0, 0xC8, 0xBB8, 0x1F4)
    Sound(1877, 255, 100, 2)    #voice#Earnest
    SetChrSubChip(0x104, 0x2)
    Sound(814, 0, 100, 0)
    Sound(819, 0, 100, 0)
    Sound(830, 0, 100, 0)
    SetChrChip(0x1, 0x104, 0x0, 0x0)
    OP_9D(0x104, 0xFFFFF682, 0x7C6, 0x59EC, 0x3E8, 0x7D0)
    SetChrChipByIndex(0x13, 0x21)
    SetChrSubChip(0x13, 0x0)
    Sound(514, 0, 100, 0)
    SetChrSubChip(0x104, 0x0)
    Sound(31, 0, 100, 0)
    Sleep(100)
    SetChrChipByIndex(0x104, 0x2D)
    SetChrSubChip(0x104, 0x0)
    Sound(30, 0, 100, 0)
    Sleep(1000)
    SetChrChipByIndex(0x104, 0x2F)
    ClearChrFlags(0x104, 0x20)
    OP_95(0x104, -2280, 1990, 24350, 5000, 0x0)
    SetChrChipByIndex(0x104, 0x2D)
    Sound(808, 0, 100, 0)
    Sleep(500)

    #C0023
    ChrTalk(
        0x104,
        "#0301F#11P呼……怎么回事啊。\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x103, 0x30)
    OP_95(0x103, -840, 1990, 23150, 5000, 0x0)
    TurnDirection(0x103, 0x13, 500)
    Sleep(300)

    #C0024
    ChrTalk(
        0x103,
        (
            "#0201F#11P看来他就是一连串事件的\x01",
            "真正犯人……\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x101,
        "兰迪、缇欧！\x02",
    )

    CloseMessageWindow()
    OP_68(-2120, 2810, 27360, 3000)
    BeginChrThread(0x101, 0, 0, 40)
    Sleep(1000)
    BeginChrThread(0x15, 0, 0, 41)
    WaitChrThread(0x101, 0)
    Sleep(1500)
    Fade(500)
    SetChrChipByIndex(0x101, 0xFF)
    Sound(804, 0, 100, 0)
    Sleep(500)

    #C0026
    ChrTalk(
        0x101,
        (
            "#0002F#5P太好了……\x01",
            "你们抓到他了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x104,
        (
            "#0301F#12P嗯，因为他拿着手枪，\x01",
            "所以我不假思索地就把他打晕了哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x101,
        "#0004F#5P嗯，没关系。\x02",
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x103,
        (
            "#0205F#12P对了，为什么罗伊德前辈\x01",
            "会和一科的四眼西装先生在一起……？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0030
    ChrTalk(
        0x15,
        (
            "#0607F#5P谁、谁是四眼西装啊！\x02\x03",

            "#0603F你们几个……\x01",
            "这到底是怎么回事？\x02\x03",

            "#0601F竟然连后援人员都安排好了，\x01",
            "到底在搞什么……！？\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x101,
        "#0008F#5P这个……\x02",
    )

    CloseMessageWindow()

    def lambda_25C5():

        label("loc_25C5")

        TurnDirection(0xFE, 0x13, 500)
        Yield()
        Jump("loc_25C5")

    QueueWorkItem2(0x101, 2, lambda_25C5)

    def lambda_25D7():

        label("loc_25D7")

        TurnDirection(0xFE, 0x13, 500)
        Yield()
        Jump("loc_25D7")

    QueueWorkItem2(0x104, 2, lambda_25D7)

    def lambda_25E9():

        label("loc_25E9")

        TurnDirection(0xFE, 0x13, 500)
        Yield()
        Jump("loc_25E9")

    QueueWorkItem2(0x103, 2, lambda_25E9)

    def lambda_25FB():

        label("loc_25FB")

        TurnDirection(0xFE, 0x13, 500)
        Yield()
        Jump("loc_25FB")

    QueueWorkItem2(0x15, 2, lambda_25FB)
    Sound(1901, 255, 100, 0)    #voice#Earnest
    SetChrChipByIndex(0x13, 0x1F)
    OP_82(0x0, 0xC8, 0xBB8, 0x1F4)
    Sound(804, 0, 100, 0)
    SetChrFlags(0x104, 0x20)
    SetChrChipByIndex(0x104, 0x2E)
    SetChrSubChip(0x104, 0x2)
    OP_96(0x104, 0xFFFFF6AA, 0x7C6, 0x5B04, 0x1770, 0x0)
    SetChrChipByIndex(0x104, 0x2D)
    Sound(819, 0, 100, 0)
    Sound(808, 0, 100, 0)
    Sleep(1000)
    SetChrChip(0x0, 0x13, 0x32, 0x12C)
    SetChrChipByIndex(0x13, 0x20)
    ClearChrFlags(0x13, 0x20)

    def lambda_2673():
        OP_95(0xFE, 8780, 1760, 24750, 8000, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_2673)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x15, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0032
    ChrTalk(
        0x104,
        "#0307F#5P什么……！？\x02",
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x101,
        "#0007F#5P还能动吗……！？\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x5C, 0)
    NewScene("c110B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_42_1FD2 end

    def Function_43_273D(): pass

    label("Function_43_273D")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-21000, 6500, 7000, 0)
    MoveCamera(45, 5, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(30000, 0)
    SetChrPos(0x101, -26500, 300, 17500, 180)
    SetChrPos(0x102, -25800, 300, 17500, 180)
    SetChrPos(0x103, -27200, 300, 17500, 180)
    SetChrPos(0x104, -26500, 300, 17500, 180)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_4B(0xC, 0xFF)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    OP_4B(0xD, 0xFF)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)
    OP_68(-21000, 5000, 7000, 6000)
    FadeToBright(2000, 0)
    OP_0D()
    Sound(107, 0, 100, 0)
    ClearMapObjFlags(0x1, 0x10)
    OP_71(0x1, 0x0, 0x5, 0x0, 0x0)
    OP_79(0x1)

    def lambda_283E():
        OP_96(0xFE, 0xFFFF987C, 0x0, 0x2A94, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_283E)

    def lambda_2858():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2858)
    Sleep(700)

    def lambda_286C():
        OP_96(0xFE, 0xFFFF94F8, 0x0, 0x2E7C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_286C)

    def lambda_2886():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_2886)
    Sleep(700)

    def lambda_289A():
        OP_96(0xFE, 0xFFFF9C00, 0x0, 0x2F44, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_289A)

    def lambda_28B4():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_28B4)
    Sleep(700)

    def lambda_28C8():
        OP_96(0xFE, 0xFFFF987C, 0x0, 0x332C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_28C8)

    def lambda_28E2():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_28E2)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    Sound(107, 0, 100, 0)
    OP_71(0x1, 0x5, 0x0, 0x0, 0x0)
    OP_79(0x1)
    SetMapObjFlags(0x1, 0x10)
    OP_6F(0x1)
    Fade(1000)
    OP_68(-26500, 1000, 12000, 0)
    MoveCamera(50, 23, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19500, 0)
    OP_0D()

    #C0034
    ChrTalk(
        0x101,
        "#5P#0001F已经天黑了吗……\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0x0, 0x1F4)

    #C0035
    ChrTalk(
        0x101,
        (
            "#12P#0000F总之，得找冈兹先生\x01",
            "谈谈才行。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_29A7():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_29A7)
    Sleep(50)
    TurnDirection(0x103, 0x101, 500)
    Sleep(100)

    #C0036
    ChrTalk(
        0x102,
        (
            "#5P#0104F嗯，去对面的\x01",
            "酒店看看吧。\x02\x03",

            "#0100F豪华客房应该\x01",
            "是在顶层。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x104,
        (
            "#5P#0306F在『巴鲁卡』大把赢取米拉，\x01",
            "然后优雅地住在酒店啊……\x02\x03",

            "#0301F可恶，羡慕死我了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x104, 500)

    #C0038
    ChrTalk(
        0x103,
        (
            "#6P#0211F兰迪前辈，\x01",
            "问题的重点并不在这里……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, -26500, 0, 12000, 180)
    OP_4C(0xC, 0xFF)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    OP_4C(0xD, 0xFF)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    SetScenarioFlags(0xC1, 7)
    EventEnd(0x5)
    Return()

    # Function_43_273D end

    def Function_44_2ACE(): pass

    label("Function_44_2ACE")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50539.itc", 0x1E)
    LoadChrToIndex("apl/ch50506.itc", 0x1F)
    LoadChrToIndex("chr/ch02750.itc", 0x20)
    LoadChrToIndex("chr/ch02751.itc", 0x21)
    LoadChrToIndex("chr/ch02752.itc", 0x22)
    LoadChrToIndex("chr/ch31250.itc", 0x23)
    LoadChrToIndex("chr/ch31251.itc", 0x24)
    LoadChrToIndex("chr/ch31350.itc", 0x25)
    LoadChrToIndex("chr/ch31351.itc", 0x26)
    LoadChrToIndex("chr/ch05100.itc", 0x27)
    LoadChrToIndex("chr/ch05200.itc", 0x28)
    LoadChrToIndex("chr/ch00150.itc", 0x29)
    LoadChrToIndex("chr/ch00151.itc", 0x2A)
    LoadChrToIndex("chr/ch00250.itc", 0x2B)
    LoadChrToIndex("chr/ch00251.itc", 0x2C)
    LoadChrToIndex("chr/ch00950.itc", 0x2D)
    LoadChrToIndex("chr/ch00951.itc", 0x2E)
    LoadChrToIndex("chr/ch00952.itc", 0x2F)
    LoadChrToIndex("apl/ch50509.itc", 0x30)
    LoadChrToIndex("chr/ch00152.itc", 0x31)
    LoadChrToIndex("chr/ch00254.itc", 0x32)
    OP_68(6100, 1000, -6300, 0)
    MoveCamera(35, 31, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(20500, 0)
    SetChrPos(0x101, 9000, 0, -13700, 0)
    SetChrChipByIndex(0x102, 0x29)
    SetChrSubChip(0x102, 0x0)
    SetChrPos(0x102, 8600, 0, -15200, 0)
    SetChrChipByIndex(0x103, 0x2B)
    SetChrSubChip(0x103, 0x0)
    SetChrPos(0x103, 9800, 0, -15700, 0)
    SetChrPos(0x104, 10200, 0, -14200, 0)
    SetChrChipByIndex(0x10A, 0x2D)
    SetChrSubChip(0x10A, 0x0)
    SetChrPos(0x10A, 11000, 0, -13700, 0)
    SetChrChipByIndex(0x16, 0x1F)
    SetChrSubChip(0x16, 0x0)
    SetChrFlags(0x16, 0x8000)
    SetChrPos(0x16, 9900, 0, -15000, 0)
    SetChrChipByIndex(0x14, 0x20)
    SetChrSubChip(0x14, 0x0)
    SetChrFlags(0x14, 0x8000)
    ClearChrFlags(0x14, 0x4)
    SetChrPos(0x14, 5000, 0, -14500, 0)
    ClearChrFlags(0x14, 0x80)
    ClearChrBattleFlags(0x14, 0x8000)
    OP_52(0x14, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x19, 0x25)
    SetChrSubChip(0x19, 0x0)
    SetChrChipByIndex(0x1A, 0x25)
    SetChrSubChip(0x1A, 0x0)
    SetChrChipByIndex(0x1B, 0x25)
    SetChrSubChip(0x1B, 0x0)
    SetChrChipByIndex(0x1C, 0x25)
    SetChrSubChip(0x1C, 0x0)
    SetChrFlags(0x19, 0x8000)
    SetChrFlags(0x1A, 0x8000)
    SetChrFlags(0x1B, 0x8000)
    SetChrFlags(0x1C, 0x8000)
    OP_A7(0x19, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x1A, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x1B, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x1C, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x19, -22600, 500, 9200, 180)
    SetChrPos(0x1A, -22600, 500, 9200, 180)
    SetChrPos(0x1B, -22600, 500, 9200, 180)
    SetChrPos(0x1C, -22600, 500, 9200, 180)
    SetChrChipByIndex(0x17, 0x27)
    SetChrSubChip(0x17, 0x0)
    SetChrFlags(0x17, 0x8000)
    ClearChrFlags(0x17, 0x4)
    OP_90(0x17, 1600, 1770, 13000, 180)
    SetChrChipByIndex(0x18, 0x28)
    SetChrSubChip(0x18, 0x0)
    SetChrFlags(0x18, 0x8000)
    ClearChrFlags(0x18, 0x4)
    OP_90(0x18, 600, 1770, 13400, 180)
    OP_78(0x8, 0x1D)
    SetMapObjFlags(0x8, 0x1000)
    SetMapObjFlags(0x8, 0x4)
    SetChrFlags(0x1D, 0x8000)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x1D, 0x4)
    OP_49()
    SetChrPos(0x1D, -22000, 0, 10000, 0)
    OP_D3(0x1D, 0x0, 0x186A0, 0x0, 0x0)
    OP_74(0x8, 0x1E)
    OP_70(0x8, 0x0)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)
    SetChrFlags(0xE, 0x80)
    SetChrBattleFlags(0xE, 0x8000)
    SetChrFlags(0xF, 0x80)
    SetChrBattleFlags(0xF, 0x8000)
    SetChrFlags(0x10, 0x80)
    SetChrBattleFlags(0x10, 0x8000)
    SetChrFlags(0x11, 0x80)
    SetChrBattleFlags(0x11, 0x8000)
    LoadEffect(0x0, "battle\\mgaria0.eff")
    LoadEffect(0x1, "battle\\mgaria1.eff")
    LoadEffect(0x2, "battle\\mg030_00.eff")
    LoadEffect(0x4, "battle\\btgun00.eff")

    def lambda_2E48():
        OP_96(0xFE, 0xBB8, 0x0, 0xFFFFFD44, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2E48)
    Sleep(50)

    def lambda_2E65():
        OP_96(0xFE, 0x1068, 0x0, 0xFFFFFB50, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2E65)
    Sleep(50)

    def lambda_2E82():
        OP_96(0xFE, 0xA28, 0x0, 0xFFFFF768, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2E82)
    Sleep(50)

    def lambda_2E9F():
        OP_96(0xFE, 0xED8, 0x0, 0xFFFFF574, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2E9F)
    SetChrChipByIndex(0x14, 0x21)
    SetChrSubChip(0x14, 0x0)
    OP_52(0x14, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x14, 3, 0, 3)

    def lambda_2EDD():
        OP_96(0xFE, 0x3E8, 0x0, 0xFFFFFA24, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_2EDD)
    OP_68(3100, 1000, -1700, 3000)
    MoveCamera(45, 21, 0, 3000)
    OP_6E(600, 3000)
    SetCameraDistance(15500, 3000)
    FadeToBright(2000, 0)
    BeginChrThread(0x29, 1, 0, 57)
    WaitChrThread(0x101, 1)

    def lambda_2F38():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2F38)
    WaitChrThread(0x104, 1)

    def lambda_2F49():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_2F49)
    WaitChrThread(0x102, 1)

    def lambda_2F5A():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_2F5A)
    WaitChrThread(0x103, 1)

    def lambda_2F6B():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_2F6B)
    WaitChrThread(0x14, 1)
    EndChrThread(0x29, 0x1)
    EndChrThread(0x14, 0x3)
    SetChrChipByIndex(0x14, 0x20)
    SetChrSubChip(0x14, 0x0)
    OP_52(0x14, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_2FA2():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_2FA2)
    WaitChrThread(0x103, 2)
    OP_6F(0x79)

    #C0039
    ChrTalk(
        0x101,
        "#0006F#5P呼、呼……\x02",
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x104,
        "#0306F#5P还真是够累人的啊……\x02",
    )

    CloseMessageWindow()

    #N0041
    NpcTalk(
        0x101,
        "琪雅",
        "#6P#1112F罗伊德～没事吧？\x02",
    )

    CloseMessageWindow()

    #N0042
    NpcTalk(
        0x104,
        "滴",
        "#6P#6001F我、我还是下来比较好吧……！\x02",
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x101,
        "#0000F#5P不，没关系……！\x02",
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x104,
        (
            "#0309F#5P哈哈……\x01",
            "这点小事交给我们吧。\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0x17, 0x8)
    ClearChrFlags(0x17, 0x80)
    ClearChrBattleFlags(0x17, 0x8000)

    #N0045
    NpcTalk(
        0x17,
        "女性的声音",
        "#4P哎呀，这不是警察弟弟嘛。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_3135():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3135)

    def lambda_3142():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_3142)

    def lambda_314F():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_314F)

    def lambda_315C():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_315C)

    def lambda_3169():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_3169)
    ClearChrFlags(0x17, 0x8)
    ClearChrFlags(0x18, 0x80)
    ClearChrBattleFlags(0x18, 0x8000)
    OP_68(3100, 1000, 200, 4000)

    def lambda_3196():
        OP_96(0xFE, 0xE10, 0x0, 0x7D0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_3196)
    Sleep(100)

    def lambda_31B3():
        OP_96(0xFE, 0xA28, 0xA, 0x960, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_31B3)
    WaitChrThread(0x17, 1)
    WaitChrThread(0x18, 1)
    OP_6F(0x1)

    #C0046
    ChrTalk(
        0x101,
        "#12P#0011F伊莉娅小姐、莉夏！？\x02",
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x18,
        "#1808F#5P各、各位……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB3, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBF, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_32D8")

    #N0048
    NpcTalk(
        0x101,
        "琪雅",
        (
            "#1105F#11P啊，是莉夏\x01",
            "和呼呼大睡的人～！\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x17,
        (
            "#5P#1705F呼呼大睡……？\x02\x03",

            "#1702F话说回来，\x01",
            "你们怎么带着这么可爱的孩子啊。\x02\x03",

            "#1709F还有这么大的狗，\x01",
            "这组合看上去真是令人愉快啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_348F")

    label("loc_32D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB3, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBF, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_336E")

    #N0050
    NpcTalk(
        0x101,
        "琪雅",
        "#1110F#11P啊，是莉夏～！\x02",
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x17,
        (
            "#5P#1705F嘿，还带着这么可爱的孩子呢。\x02\x03",

            "#1709F还有这么大的狗，\x01",
            "这组合看上去真是令人愉快啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_348F")

    label("loc_336E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB3, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBF, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_342F")

    #N0052
    NpcTalk(
        0x101,
        "琪雅",
        "#1105F#11P啊，是呼呼大睡的人～！\x02",
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x17,
        (
            "#5P#1705F呼呼大睡……？\x02\x03",

            "#1702F话说回来，\x01",
            "你们怎么带着这么可爱的孩子啊。\x02\x03",

            "#1709F还有这么大的狗，\x01",
            "这组合看上去真是令人愉快啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_348F")

    label("loc_342F")


    #C0054
    ChrTalk(
        0x17,
        (
            "#5P#1705F嘿，还带着这么可爱的孩子呢。\x02\x03",

            "#1709F还有这么大的狗，\x01",
            "这组合看上去真是令人愉快啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_348F")


    #C0055
    ChrTalk(
        0x101,
        (
            "#12P#0007F请你们两位赶快\x01",
            "到剧场里避难吧！\x02\x03",

            "他们很快就会──\x02",
        )
    )

    CloseMessageWindow()
    Sound(489, 0, 100, 0)
    Sleep(1000)
    Sound(495, 0, 100, 0)
    Sleep(200)
    OP_24(0x1E9)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    ClearMapObjFlags(0x8, 0x4)
    OP_68(-22000, 1000, 10000, 2000)
    MoveCamera(345, 27, 0, 2000)
    SetCameraDistance(18500, 2000)

    def lambda_3581():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3581)
    Sleep(50)

    def lambda_3591():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_3591)

    def lambda_359E():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_359E)
    Sleep(50)

    def lambda_35AE():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_35AE)

    def lambda_35BB():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_35BB)
    Sleep(50)

    def lambda_35CB():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_35CB)

    def lambda_35D8():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x18, 2, lambda_35D8)
    OP_6F(0x79)
    OP_71(0x8, 0xF1, 0x10E, 0x0, 0x0)
    Sound(464, 0, 100, 0)
    OP_79(0x8)
    ClearChrFlags(0x19, 0x80)
    ClearChrBattleFlags(0x19, 0x8000)
    ClearChrFlags(0x1A, 0x80)
    ClearChrBattleFlags(0x1A, 0x8000)
    ClearChrFlags(0x1B, 0x80)
    ClearChrBattleFlags(0x1B, 0x8000)
    ClearChrFlags(0x1C, 0x80)
    ClearChrBattleFlags(0x1C, 0x8000)
    BeginChrThread(0x19, 3, 0, 55)
    Sleep(500)
    BeginChrThread(0x1A, 3, 0, 55)
    Sleep(500)
    BeginChrThread(0x1B, 3, 0, 55)
    Sleep(500)
    BeginChrThread(0x1C, 3, 0, 55)
    WaitChrThread(0x19, 3)
    Fade(500)
    OP_68(3100, 1000, 200, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15500, 0)
    ClearScenarioFlags(0x0, 2)

    def lambda_367F():
        OP_A6(0xFE, 0x0, 0x1E, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_367F)
    SetChrChipByIndex(0x14, 0x22)
    SetChrSubChip(0x14, 0x3)
    OP_52(0x14, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x102, 3, 0, 47)
    BeginChrThread(0x103, 3, 0, 46)
    OP_0D()
    EndChrThread(0x19, 0xFF)
    EndChrThread(0x19, 0xFF)
    EndChrThread(0x1B, 0xFF)
    EndChrThread(0x1C, 0xFF)

    #C0056
    ChrTalk(
        0x104,
        (
            "#0307F#11P嘁……\x01",
            "到底开了几辆出来啊～！\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x17,
        (
            "#11P#1705F哎、哎……\x01",
            "这是什么游乐设施吗！？\x02\x03",

            "#1709F好像制作得很精良啊！？\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x102,
        "#12P#0107F总之，请快点进去避难吧！\x02",
    )

    CloseMessageWindow()
    OP_68(5600, 1000, -4800, 2000)
    MoveCamera(55, 21, 0, 2000)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x16, 0x80)
    ClearChrBattleFlags(0x16, 0x8000)

    def lambda_37A7():
        OP_95(0xFE, 7000, 0, -5700, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_37A7)
    Sleep(100)

    def lambda_37C4():
        OP_95(0xFE, 5900, 0, -7000, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_37C4)
    WaitChrThread(0x10A, 1)

    def lambda_37E2():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10A, 2, lambda_37E2)
    WaitChrThread(0x16, 1)
    SetChrChipByIndex(0x16, 0x1E)
    SetChrSubChip(0x16, 0x0)

    def lambda_37FB():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x16, 2, lambda_37FB)
    WaitChrThread(0x16, 2)

    def lambda_380C():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_380C)
    OP_6F(0x41)

    #C0059
    ChrTalk(
        0x10A,
        "#11P#0607F喂，在干什么呢！\x02",
    )

    CloseMessageWindow()

    def lambda_383B():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_383B)
    Sleep(50)

    def lambda_384B():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_384B)
    SetScenarioFlags(0x0, 2)

    #C0060
    ChrTalk(
        0x16,
        "#11P#1007F快点去警察局总部！\x02",
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x101,
        "#3P#0007F是……！\x02",
    )

    CloseMessageWindow()
    OP_AD(0x3)
    OP_AD(0x4)
    OP_68(15500, 1000, 9700, 5000)
    MoveCamera(30, 21, 0, 5000)
    BeginChrThread(0x101, 3, 0, 48)
    BeginChrThread(0x104, 3, 0, 49)
    BeginChrThread(0x102, 3, 0, 50)
    BeginChrThread(0x103, 3, 0, 51)
    BeginChrThread(0x10A, 3, 0, 53)
    BeginChrThread(0x16, 3, 0, 54)
    BeginChrThread(0x14, 3, 0, 52)
    Sleep(1000)

    def lambda_38E3():

        label("loc_38E3")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_38E3")

    QueueWorkItem2(0x17, 2, lambda_38E3)

    def lambda_38F5():

        label("loc_38F5")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_38F5")

    QueueWorkItem2(0x18, 2, lambda_38F5)
    WaitChrThread(0x16, 3)
    EndChrThread(0x17, 0x2)
    EndChrThread(0x18, 0x2)
    OP_6F(0x41)
    EndChrThread(0x29, 0x1)
    Fade(500)
    OP_68(3100, 1000, 2200, 0)
    MoveCamera(10, 21, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15500, 0)
    SetCameraDistance(14500, 1000)
    OP_0D()
    Sleep(500)

    #C0062
    ChrTalk(
        0x17,
        (
            "#5P#1709F哇哦！\x01",
            "好强的临场感啊！？\x02\x03",

            "#1702F好～既然如此，我也来……！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_39A3():
        OP_95(0xFE, 3200, 0, 2600, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_39A3)
    WaitChrThread(0x18, 1)
    TurnDirection(0x18, 0x17, 500)

    #C0063
    ChrTalk(
        0x18,
        (
            "#1801F#5P伊莉娅小姐！\x01",
            "拜托快去避难吧！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_39F4():
        OP_98(0xFE, 0xFFFFEC78, 0x0, 0x3A98, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_39F4)
    OP_63(0x17, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)

    def lambda_3A20():
        OP_98(0xFE, 0xFFFFEC78, 0x0, 0x3A98, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_3A20)
    Sleep(500)
    BeginChrThread(0x17, 3, 0, 45)
    SetCameraDistance(17000, 5000)

    #C0064
    ChrTalk(
        0x17,
        (
            "#6P#1705F#28A喂，莉夏！\x01",
            "不要拽我啦──\x02",
        )
    )
    #Auto

    CloseMessageWindow()
    Sleep(1000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x103, 0x2)
    EndChrThread(0x104, 0x2)
    SetScenarioFlags(0x5C, 1)
    NewScene("c110B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_44_2ACE end

    def Function_45_3AA0(): pass

    label("Function_45_3AA0")

    SetChrPos(0x19, -7000, 0, 1500, 90)
    SetChrPos(0x1A, -7000, 0, 1500, 90)
    SetChrPos(0x1B, -7000, 0, 1500, 90)
    SetChrPos(0x1C, -7000, 0, 1500, 90)
    Sleep(500)
    BeginChrThread(0x19, 3, 0, 56)
    Sleep(500)
    BeginChrThread(0x1A, 3, 0, 56)
    Sleep(500)
    BeginChrThread(0x1B, 3, 0, 56)
    Sleep(500)
    BeginChrThread(0x1C, 3, 0, 56)
    Return()

    # Function_45_3AA0 end

    def Function_46_3B09(): pass

    label("Function_46_3B09")

    ClearScenarioFlags(0x0, 4)
    SetChrChipByIndex(0x103, 0x32)
    SetChrSubChip(0x103, 0x0)

    label("loc_3B14")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3C04")
    PlayEffect(0x0, 0x0, 0x103, 0x40, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(831, 0, 100, 0)
    OP_A1(0x103, 0x5DC, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x1, 0x2, 0x1)
    OP_A1(0x103, 0x5DC, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x1, 0x2, 0x1)
    StopEffect(0x0, 0x2)
    Sound(280, 0, 80, 0)
    PlayEffect(0x1, 0x1, 0x103, 0x140, 0, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0x103, 0x3)
    Sleep(500)
    PlayEffect(0x2, 0x2, 0x103, 0x140, 0, 1000, 1000, 0, 0, 0, 1000, 1000, 1000, 0x19, 0, 0, 0, 0)
    SetChrSubChip(0x103, 0x4)
    Sleep(2000)
    StopEffect(0x2, 0x2)
    Jump("loc_3B14")

    label("loc_3C04")

    SetScenarioFlags(0x0, 4)
    Return()

    # Function_46_3B09 end

    def Function_47_3C08(): pass

    label("Function_47_3C08")

    ClearScenarioFlags(0x0, 3)
    SetChrChipByIndex(0x102, 0x31)
    SetChrSubChip(0x102, 0x0)
    Sleep(50)
    SetChrSubChip(0x102, 0x1)
    Sleep(50)
    SetChrSubChip(0x102, 0x2)

    label("loc_3C21")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3C93")
    Sleep(1500)
    OP_82(0x32, 0x0, 0xBB8, 0x96)
    PlayEffect(0x4, 0xFF, 0xFE, 0x140, 0, 1100, 900, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(530, 0, 100, 0)
    SetChrSubChip(0x102, 0x3)
    Sleep(150)
    SetChrSubChip(0x102, 0x4)
    Sleep(100)
    SetChrSubChip(0x102, 0x2)
    Jump("loc_3C21")

    label("loc_3C93")

    SetScenarioFlags(0x0, 3)
    Return()

    # Function_47_3C08 end

    def Function_48_3C97(): pass

    label("Function_48_3C97")

    OP_92(0x101, 0x34BC, 0x25E4, 0x1F4)

    def lambda_3CA9():
        OP_95(0xFE, 13500, 0, 9700, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3CA9)
    WaitChrThread(0x101, 1)

    def lambda_3CC7():
        OP_97(0xFE, 0x3A98, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3CC7)
    WaitChrThread(0x101, 1)
    Return()

    # Function_48_3C97 end

    def Function_49_3CE1(): pass

    label("Function_49_3CE1")

    Sleep(600)
    OP_92(0x104, 0x396C, 0x21FC, 0x1F4)

    def lambda_3CF6():
        OP_95(0xFE, 14700, 0, 8700, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3CF6)
    WaitChrThread(0x104, 1)

    def lambda_3D14():
        OP_97(0xFE, 0x2710, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3D14)
    WaitChrThread(0x104, 1)
    Return()

    # Function_49_3CE1 end

    def Function_50_3D2E(): pass

    label("Function_50_3D2E")

    SetChrSubChip(0x102, 0x2)
    Sleep(400)
    SetChrSubChip(0x102, 0x1)
    Sleep(100)
    SetChrSubChip(0x102, 0x0)
    Sleep(100)
    SetChrChipByIndex(0x102, 0x29)
    SetChrSubChip(0x102, 0x0)
    OP_92(0x102, 0x34BC, 0x25E4, 0x1F4)

    def lambda_3D5D():
        OP_95(0xFE, 13500, 0, 9700, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3D5D)
    WaitChrThread(0x102, 1)

    def lambda_3D7B():
        OP_97(0xFE, 0x2710, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3D7B)
    WaitChrThread(0x102, 1)
    Return()

    # Function_50_3D2E end

    def Function_51_3D95(): pass

    label("Function_51_3D95")

    SetChrSubChip(0x103, 0x3)
    Sleep(1200)
    SetChrChipByIndex(0x103, 0x2B)
    SetChrSubChip(0x103, 0x0)
    OP_92(0x103, 0x396C, 0x21FC, 0x1F4)

    def lambda_3DB6():
        OP_95(0xFE, 14700, 0, 8700, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_3DB6)
    WaitChrThread(0x103, 1)

    def lambda_3DD4():
        OP_97(0xFE, 0x2710, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_3DD4)
    WaitChrThread(0x103, 1)
    Return()

    # Function_51_3D95 end

    def Function_52_3DEE(): pass

    label("Function_52_3DEE")


    def lambda_3DF3():
        OP_A6(0xFE, 0x0, 0x1E, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_3DF3)
    WaitChrThread(0x14, 2)
    OP_92(0x14, 0x332C, 0x21FC, 0x1F4)
    SetChrChipByIndex(0x14, 0x21)
    SetChrSubChip(0x14, 0x0)
    OP_52(0x14, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x14, 0, 0, 3)
    BeginChrThread(0x29, 1, 0, 57)

    def lambda_3E47():
        OP_96(0xFE, 0x3E8, 0x6EA, 0x25E4, 0x1964, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_3E47)
    WaitChrThread(0x14, 1)

    def lambda_3E65():
        OP_96(0xFE, 0x157C, 0x6EA, 0x319C, 0x1964, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_3E65)
    WaitChrThread(0x14, 1)
    EndChrThread(0x14, 0x0)
    EndChrThread(0x29, 0x1)

    def lambda_3E8B():
        OP_92(0xFE, 0x34BC, 0x319C, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_3E8B)
    SetChrSubChip(0x14, 0x2)
    OP_52(0x14, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(50)
    SetChrSubChip(0x14, 0x3)
    Sleep(50)
    SetChrSubChip(0x14, 0x0)
    Sound(854, 0, 100, 0)

    def lambda_3ECC():
        OP_9D(0xFE, 0x34BC, 0x0, 0x319C, 0x2BC, 0xBB8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_3ECC)
    Sleep(600)
    SetChrSubChip(0x14, 0x1)
    Sleep(50)
    SetChrSubChip(0x14, 0x2)
    WaitChrThread(0x14, 1)
    SetChrSubChip(0x14, 0x3)
    OP_52(0x14, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xAA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(50)
    BeginChrThread(0x14, 0, 0, 3)
    BeginChrThread(0x29, 1, 0, 57)

    def lambda_3F24():
        OP_97(0xFE, 0x4E20, 0x0, 0x0, 0x1964, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_3F24)
    WaitChrThread(0x14, 1)
    Return()

    # Function_52_3DEE end

    def Function_53_3F3E(): pass

    label("Function_53_3F3E")

    Sleep(2500)
    OP_92(0x10A, 0x4268, 0x21FC, 0x1F4)

    def lambda_3F53():
        OP_95(0xFE, 17000, 0, 8700, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_3F53)
    WaitChrThread(0x10A, 1)

    def lambda_3F71():
        OP_97(0xFE, 0x1B58, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_3F71)
    WaitChrThread(0x10A, 1)
    Return()

    # Function_53_3F3E end

    def Function_54_3F8B(): pass

    label("Function_54_3F8B")

    Sleep(2800)
    SetChrChipByIndex(0x16, 0x1F)
    SetChrSubChip(0x16, 0x0)
    OP_92(0x16, 0x4268, 0x21FC, 0x1F4)

    def lambda_3FA8():
        OP_95(0xFE, 17000, 0, 8700, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_3FA8)
    WaitChrThread(0x16, 1)

    def lambda_3FC6():
        OP_97(0xFE, 0x1B58, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_3FC6)
    WaitChrThread(0x16, 1)
    Return()

    # Function_54_3F8B end

    def Function_55_3FE0(): pass

    label("Function_55_3FE0")

    SetChrChipByIndex(0xFE, 0x26)
    SetChrSubChip(0xFE, 0x0)

    def lambda_3FED():
        OP_95(0xFE, -22800, 0, 7200, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3FED)

    def lambda_4007():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4007)
    WaitChrThread(0xFE, 1)

    def lambda_401C():
        OP_95(0xFE, -13800, 0, 3200, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_401C)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_55_3FE0 end

    def Function_56_4036(): pass

    label("Function_56_4036")

    SetChrChipByIndex(0xFE, 0x26)
    SetChrSubChip(0xFE, 0x0)

    def lambda_4043():
        OP_95(0xFE, 3000, 0, 1500, 6000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4043)
    WaitChrThread(0xFE, 1)

    def lambda_4061():
        OP_95(0xFE, 13000, 0, 9500, 6000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4061)
    WaitChrThread(0xFE, 1)

    def lambda_407F():
        OP_95(0xFE, 23000, 0, 9500, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_407F)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_56_4036 end

    def Function_57_4099(): pass

    label("Function_57_4099")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_40B2")
    Sound(925, 0, 100, 0)
    Sleep(500)
    Jump("Function_57_4099")

    label("loc_40B2")

    Return()

    # Function_57_4099 end

    def Function_58_40B3(): pass

    label("Function_58_40B3")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_415B")

    #C0065
    ChrTalk(
        0x104,
        (
            "#0300F彩虹剧团的公演时间\x01",
            "似乎快到了。\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x101,
        (
            "#0003F虽然好像还可以进去……\x02\x03",

            "#0001F不过，现在还是先去看看冈兹先生的情况吧，\x01",
            "应该就在那边的酒店里。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_4193")

    label("loc_415B")

    SetChrName("")

    #A0067
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "今晚的公演似乎还没有开始呢，\x01",
            "稍后再过来吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_4193")

    Sleep(50)
    SetChrPos(0x0, -2040, 2660, 31410, 180)
    EventEnd(0x4)
    Return()

    # Function_58_40B3 end

    def Function_59_41AA(): pass

    label("Function_59_41AA")

    EventBegin(0x1)
    Call(0, 62)
    Sleep(50)
    SetChrPos(0x0, 20770, 0, 12930, 270)
    EventEnd(0x4)
    Return()

    # Function_59_41AA end

    def Function_60_41C6(): pass

    label("Function_60_41C6")

    EventBegin(0x1)
    Call(0, 62)
    Sleep(50)
    SetChrPos(0x0, -39280, 0, 12420, 90)
    EventEnd(0x4)
    Return()

    # Function_60_41C6 end

    def Function_61_41E2(): pass

    label("Function_61_41E2")

    EventBegin(0x1)
    Call(0, 62)
    Sleep(50)
    SetChrPos(0x0, 13270, 0, -19100, 315)
    EventEnd(0x4)
    Return()

    # Function_61_41E2 end

    def Function_62_41FE(): pass

    label("Function_62_41FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_425C")

    #C0068
    ChrTalk(
        0x101,
        (
            "#0001F冈兹先生似乎\x01",
            "就住在这附近的\x01",
            "高级酒店里……\x02\x03",

            "现在还是先去那边看看吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_425C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_435D")

    #C0069
    ChrTalk(
        0x101,
        (
            "#0000F太阳都下山了啊……\x02\x03",

            "琪雅还在等我们，\x01",
            "就不要绕道了，赶快回去吧。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_42F3")

    #C0070
    ChrTalk(
        0x102,
        (
            "#0100F是呀，工作\x01",
            "差不多也告一段落了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_435D")

    label("loc_42F3")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4320")

    #C0071
    ChrTalk(
        0x103,
        "#0200F是啊，回去吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_435D")

    label("loc_4320")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_435D")

    #C0072
    ChrTalk(
        0x104,
        (
            "#0300F是啊，赶紧回去，\x01",
            "看看阿琪的小脸吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_435D")

    Return()

    # Function_62_41FE end

    SaveToFile()

Try(main)
