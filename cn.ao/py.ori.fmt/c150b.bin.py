from ScenarioHelper import *

def main():
    CreateScenaFile(
        "c150b.bin",                # FileName
        "c150b",                    # MapName
        "c150b",                    # Location
        0x00AA,                     # MapIndex
        "ed7150",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x1E,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 170, 0, 0, 0, 1],
    )

    BuildStringList((
        "c150b",                  # 0
        "亚里欧斯",               # 1
        "达德利搜查官",           # 2
        "警队成员",               # 3
        "警队成员",               # 4
        "警队成员",               # 5
        "警队成员",               # 6
        "警队成员",               # 7
        "警队成员",               # 8
        "警队成员",               # 9
        "警队成员",               # 10
        "猎兵",                   # 11
        "猎兵",                   # 12
        "猎兵",                   # 13
        "猎兵",                   # 14
        "猎兵",                   # 15
        "猎兵",                   # 16
        "猎兵",                   # 17
        "猎兵",                   # 18
        "猎兵",                   # 19
        "猎兵",                   # 20
        "猎兵",                   # 21
        "达德利的车",             # 22
        "警车",                   # 23
        "警车",                   # 24
        "警车",                   # 25
        "警车",                   # 26
        "警车",                   # 27
        "SE控制",                 # 28
        "中央广场",               # 29
        "西街",                   # 30
        "行政区",                 # 31
        "住宅街",                 # 32
        "欢乐街",                 # 33
        "东街",                   # 34
        "旧城区",                 # 35
        "港湾区",                 # 36
        "ＩＢＣ",                 # 37
        "站前街道",               # 38
        "后巷",                   # 39
        "乌尔斯拉间道",           # 40
        "东克洛斯贝尔街道",       # 41
        "西克洛斯贝尔街道",       # 42
        "玛因兹山道",             # 43
        "兰花塔",                 # 44
    ))

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
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    PlaceName(-20.690000534057617, 0.0, -334.95001220703125, 0x0000, 0x0000, "中央广场")
    PlaceName(-176.4499969482422, 0.0, -343.79998779296875, 0x0000, 0x0000, "西街")
    PlaceName(21.639999389648438, 0.0, -191.3000030517578, 0x0000, 0x0000, "行政区")
    PlaceName(-276.45001220703125, 0.0, -223.8000030517578, 0x0000, 0x0000, "住宅街")
    PlaceName(-142.5, 0.0, -222.60000610351562, 0x0000, 0x0000, "欢乐街")
    PlaceName(113.25, 0.0, -400.5, 0x0000, 0x0000, "东街")
    PlaceName(183.5800018310547, 0.0, -513.25, 0x0000, 0x0000, "旧城区")
    PlaceName(154.9499969482422, 0.0, -274.3999938964844, 0x0000, 0x0000, "港湾区")
    PlaceName(126.94999694824219, 0.0, -96.5, 0x0000, 0x0000, "ＩＢＣ")
    PlaceName(-17.75, 0.0, -493.6000061035156, 0x0000, 0x0000, "站前街道")
    PlaceName(-101.80000305175781, 0.0, -283.20001220703125, 0x0000, 0x0000, "后巷")
    PlaceName(-21.200000762939453, 0.0, -548.0499877929688, 0x0000, 0x0000, "乌尔斯拉间道")
    PlaceName(234.85000610351562, 0.0, -384.6000061035156, 0x0000, 0x0000, "东克洛斯贝尔街道")
    PlaceName(-264.95001220703125, 0.0, -340.3999938964844, 0x0000, 0x0000, "西克洛斯贝尔街道")
    PlaceName(-254.0500030517578, 0.0, -165.39999389648438, 0x0000, 0x0000, "玛因兹山道")
    PlaceName(0.0, 0.0, 55.5, 0x0000, 0x0000, "兰花塔")
    PlaceName(-75.98999786376953, 0.0, -390.8500061035156, 0x0000, 0x0051, "")
    PlaceName(26.18000030517578, 0.0, -340.75, 0x0000, 0x0054, "")
    PlaceName(-30.809999465942383, 0.0, -400.6499938964844, 0x0000, 0x0057, "")
    PlaceName(-76.8499984741211, 0.0, -336.20001220703125, 0x0000, 0x0053, "")
    PlaceName(-33.279998779296875, 0.0, -289.79998779296875, 0x0000, 0x0053, "")
    PlaceName(-155.63999938964844, 0.0, -302.45001220703125, 0x0000, 0x0053, "")
    PlaceName(-99.7300033569336, 0.0, -266.6000061035156, 0x0000, 0x0053, "")
    PlaceName(-110.25, 0.0, -240.39999389648438, 0x0000, 0x0052, "")
    PlaceName(128.3000030517578, 0.0, -543.5800170898438, 0x0000, 0x0053, "")
    PlaceName(-85.7300033569336, 0.0, -280.67999267578125, 0x0000, 0x0053, "")
    PlaceName(-26.950000762939453, 0.0, -144.3300018310547, 0x0000, 0x0051, "")
    PlaceName(181.85000610351562, 0.0, -410.5, 0x0000, 0x0052, "")
    PlaceName(128.3000030517578, 0.0, -543.5800170898438, 0x0000, 0x0053, "")
    PlaceName(158.64999389648438, 0.0, -582.2999877929688, 0x0000, 0x0053, "")

    ChipFrameInfo(1656, 0)                                       # 0

    ScpFunction((
        "Function_0_678",          # 00, 0
        "Function_1_69C",          # 01, 1
        "Function_2_69D",          # 02, 2
        "Function_3_7BC",          # 03, 3
        "Function_4_165C",         # 04, 4
        "Function_5_16B0",         # 05, 5
        "Function_6_170A",         # 06, 6
        "Function_7_173E",         # 07, 7
        "Function_8_19BF",         # 08, 8
        "Function_9_1E44",         # 09, 9
        "Function_10_1FF9",        # 0A, 10
        "Function_11_2062",        # 0B, 11
        "Function_12_20CC",        # 0C, 12
        "Function_13_212A",        # 0D, 13
        "Function_14_2188",        # 0E, 14
        "Function_15_222B",        # 0F, 15
        "Function_16_22CE",        # 10, 16
        "Function_17_236B",        # 11, 17
        "Function_18_23FC",        # 12, 18
        "Function_19_2499",        # 13, 19
        "Function_20_253C",        # 14, 20
        "Function_21_257C",        # 15, 21
        "Function_22_25BC",        # 16, 22
        "Function_23_25FC",        # 17, 23
        "Function_24_2624",        # 18, 24
        "Function_25_264C",        # 19, 25
        "Function_26_26AF",        # 1A, 26
        "Function_27_2850",        # 1B, 27
        "Function_28_287C",        # 1C, 28
        "Function_29_28BC",        # 1D, 29
        "Function_30_28FC",        # 1E, 30
    ))


    def Function_0_678(): pass

    label("Function_0_678")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_68C")
    ClearScenarioFlags(0x22, 0)
    Event(0, 2)
    Jump("loc_69B")

    label("loc_68C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_69B")
    ClearScenarioFlags(0x22, 1)
    Event(0, 3)

    label("loc_69B")

    Return()

    # Function_0_678 end

    def Function_1_69C(): pass

    label("Function_1_69C")

    Return()

    # Function_1_69C end

    def Function_2_69D(): pass

    label("Function_2_69D")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(0, 25000, 40000, 0)
    MoveCamera(335, -20, 0, 0)
    OP_6E(1100, 0)
    SetCameraDistance(70000, 0)
    OP_F0(0x0, 0x1)
    SetChrPos(0x0, 0, 0, 50000, 0)
    SetChrPos(0x1, 0, 0, 50000, 0)
    SetChrPos(0x2, 0, 0, 50000, 0)
    SetChrPos(0x3, 0, 0, 50000, 0)
    OP_68(0, 65000, 45000, 10000)
    MoveCamera(20, -35, 0, 10000)
    SetCameraDistance(120000, 10000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)
    Fade(1000)
    OP_68(0, 170000, 45000, 0)
    MoveCamera(30, -45, 0, 0)
    OP_6E(1100, 0)
    SetCameraDistance(80000, 0)
    OP_68(0, 175000, 45000, 5000)
    SetCameraDistance(60000, 5000)
    Sleep(3000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_F0(0x0, 0xA)
    SetScenarioFlags(0x22, 0)
    NewScene("c153B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_2_69D end

    def Function_3_7BC(): pass

    label("Function_3_7BC")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    LoadChrToIndex("chr/ch00900.itc", 0x23)
    LoadChrToIndex("chr/ch00950.itc", 0x24)
    LoadChrToIndex("chr/ch00951.itc", 0x25)
    LoadChrToIndex("chr/ch00952.itc", 0x26)
    LoadChrToIndex("chr/ch02400.itc", 0x28)
    LoadChrToIndex("chr/ch02450.itc", 0x29)
    LoadChrToIndex("chr/ch02451.itc", 0x2A)
    LoadChrToIndex("chr/ch02452.itc", 0x2B)
    LoadChrToIndex("chr/ch02456.itc", 0x2C)
    LoadChrToIndex("apl/ch51236.itc", 0x2D)
    LoadChrToIndex("apl/ch51262.itc", 0x2E)
    LoadChrToIndex("apl/ch51263.itc", 0x2F)
    LoadChrToIndex("chr/ch41950.itc", 0x32)
    LoadChrToIndex("chr/ch41951.itc", 0x33)
    LoadChrToIndex("chr/ch41952.itc", 0x34)
    LoadChrToIndex("chr/ch41953.itc", 0x35)
    LoadChrToIndex("chr/ch42050.itc", 0x37)
    LoadChrToIndex("chr/ch42051.itc", 0x38)
    LoadChrToIndex("chr/ch42052.itc", 0x39)
    LoadChrToIndex("chr/ch42053.itc", 0x3A)
    LoadChrToIndex("chr/ch42057.itc", 0x3B)
    LoadChrToIndex("chr/ch42056.itc", 0x3C)
    LoadEffect(0x0, "battle/btgun00.eff")
    LoadEffect(0x1, "event/ev606_00.eff")
    LoadEffect(0x2, "battle/sp003000.eff")
    LoadEffect(0x3, "battle/ms00001.eff")
    LoadEffect(0x4, "event/ev15027.eff")
    LoadEffect(0x5, "battle/cr024100.eff")
    LoadEffect(0x6, "event/ev15042.eff")
    LoadEffect(0x7, "battle/cr024401.eff")
    LoadEffect(0x8, "battle/cr024000.eff")
    SoundLoad(868)
    SoundLoad(865)
    SoundLoad(861)
    SoundLoad(863)
    SetChrChipByIndex(0x9, 0x23)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    SetChrChipByIndex(0x8, 0x28)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrChipByIndex(0xA, 0x2D)
    SetChrSubChip(0xA, 0x0)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)
    SetChrChipByIndex(0xB, 0x2D)
    SetChrSubChip(0xB, 0x0)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8000)
    SetChrChipByIndex(0xC, 0x2D)
    SetChrSubChip(0xC, 0x0)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8000)
    SetChrChipByIndex(0xD, 0x2D)
    SetChrSubChip(0xD, 0x0)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x8000)
    SetChrChipByIndex(0xE, 0x2D)
    SetChrSubChip(0xE, 0x0)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x8000)
    SetChrChipByIndex(0xF, 0x2D)
    SetChrSubChip(0xF, 0x0)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x8000)
    SetChrChipByIndex(0x10, 0x2D)
    SetChrSubChip(0x10, 0x0)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x8000)
    SetChrChipByIndex(0x11, 0x2D)
    SetChrSubChip(0x11, 0x0)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x8000)
    SetChrChipByIndex(0x12, 0x34)
    SetChrSubChip(0x12, 0x1)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x12, 0x8000)
    SetChrChipByIndex(0x13, 0x34)
    SetChrSubChip(0x13, 0x1)
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x13, 0x8000)
    SetChrChipByIndex(0x14, 0x34)
    SetChrSubChip(0x14, 0x1)
    ClearChrFlags(0x14, 0x80)
    SetChrFlags(0x14, 0x8000)
    SetChrChipByIndex(0x15, 0x38)
    SetChrSubChip(0x15, 0x0)
    ClearChrFlags(0x15, 0x80)
    SetChrFlags(0x15, 0x8000)
    SetChrChipByIndex(0x16, 0x38)
    SetChrSubChip(0x16, 0x0)
    ClearChrFlags(0x16, 0x80)
    SetChrFlags(0x16, 0x8000)
    SetChrChipByIndex(0x17, 0x38)
    SetChrSubChip(0x17, 0x0)
    ClearChrFlags(0x17, 0x80)
    SetChrFlags(0x17, 0x8000)
    SetChrChipByIndex(0x18, 0x33)
    SetChrSubChip(0x18, 0x0)
    SetChrFlags(0x18, 0x8000)
    SetChrChipByIndex(0x19, 0x33)
    SetChrSubChip(0x19, 0x0)
    SetChrFlags(0x19, 0x8000)
    SetChrChipByIndex(0x1A, 0x33)
    SetChrSubChip(0x1A, 0x0)
    SetChrFlags(0x1A, 0x8000)
    SetChrChipByIndex(0x1B, 0x34)
    SetChrSubChip(0x1B, 0x1)
    ClearChrFlags(0x1B, 0x80)
    SetChrFlags(0x1B, 0x8000)
    SetChrChipByIndex(0x1C, 0x34)
    SetChrSubChip(0x1C, 0x1)
    ClearChrFlags(0x1C, 0x80)
    SetChrFlags(0x1C, 0x8000)
    ClearChrFlags(0x1D, 0x80)
    OP_78(0x9, 0x1D)
    OP_49()
    ClearMapObjFlags(0x9, 0x4)
    SetMapObjFlags(0x9, 0x1000)
    ClearChrFlags(0x1E, 0x80)
    OP_78(0xA, 0x1E)
    OP_49()
    ClearMapObjFlags(0xA, 0x4)
    SetMapObjFlags(0xA, 0x1000)
    SetMapObjFrame(0xA, "light", 0x0, 0x1)
    SetMapObjFrame(0xA, "patlight", 0x2, "highspd")
    ClearChrFlags(0x1F, 0x80)
    OP_78(0xB, 0x1F)
    OP_49()
    ClearMapObjFlags(0xB, 0x4)
    SetMapObjFlags(0xB, 0x1000)
    SetMapObjFrame(0xB, "light", 0x0, 0x1)
    SetMapObjFrame(0xB, "patlight", 0x2, "highspd")
    ClearChrFlags(0x20, 0x80)
    OP_78(0xC, 0x20)
    OP_49()
    ClearMapObjFlags(0xC, 0x4)
    SetMapObjFlags(0xC, 0x1000)
    SetMapObjFrame(0xC, "light", 0x0, 0x1)
    SetMapObjFrame(0xC, "patlight", 0x2, "highspd")
    ClearChrFlags(0x21, 0x80)
    OP_78(0xD, 0x21)
    OP_49()
    ClearMapObjFlags(0xD, 0x4)
    SetMapObjFlags(0xD, 0x1000)
    SetMapObjFrame(0xD, "light", 0x0, 0x1)
    SetMapObjFrame(0xD, "patlight", 0x2, "highspd")
    ClearChrFlags(0x22, 0x80)
    OP_78(0xE, 0x22)
    OP_49()
    SetMapObjFlags(0xE, 0x1000)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    SetChrPos(0x9, 750, 100, 9000, 180)
    SetChrPos(0x8, -750, 100, 8500, 180)
    SetChrPos(0xA, -10900, 0, -1900, 135)
    SetChrPos(0xB, -8950, 0, 1100, 135)
    SetChrPos(0xC, -7500, 250, 1850, 135)
    SetChrPos(0xD, -3000, 100, 4150, 180)
    SetChrPos(0xE, 3150, 110, 4450, 180)
    SetChrPos(0xF, 7500, 140, 1300, 225)
    SetChrPos(0x10, 9250, 0, 1100, 225)
    SetChrPos(0x11, 11100, 0, -3050, 225)
    SetChrPos(0x1D, 0, 0, 3800, 90)
    OP_D5(0x1D, 0x0, 0x15F90, 0x0, 0x0)
    SetChrPos(0x1E, -8800, 0, -1800, 30)
    OP_D5(0x1E, 0x0, 0x7530, 0x0, 0x0)
    SetChrPos(0x1F, -5100, 0, 2200, 60)
    OP_D5(0x1F, 0x0, 0xEA60, 0x0, 0x0)
    SetChrPos(0x20, 8800, 0, -1800, 330)
    OP_D5(0x20, 0x0, 0x50910, 0x0, 0x0)
    SetChrPos(0x21, 5100, 0, 2200, 300)
    OP_D5(0x21, 0x0, 0x493E0, 0x0, 0x0)
    SetChrPos(0x22, 8800, 0, -1800, 330)
    OP_D5(0x22, 0x0, 0x50910, 0x0, 0x0)
    SetChrPos(0x12, -2300, 0, -4500, 315)
    SetChrPos(0x13, 0, 0, -4000, 0)
    SetChrPos(0x14, 2300, 0, -4500, 45)
    SetChrPos(0x1B, -3300, 0, -6500, 315)
    SetChrPos(0x1C, 3300, 0, -6500, 45)
    SetChrPos(0x15, 0, 0, -28000, 0)
    SetChrPos(0x16, 900, 0, -29000, 0)
    SetChrPos(0x17, -900, 0, -29500, 0)
    OP_68(0, 3600, -20000, 0)
    MoveCamera(25, -15, 0, 0)
    OP_6E(750, 0)
    SetCameraDistance(15000, 0)
    OP_F0(0x0, 0x1)
    OP_68(0, 600, -5000, 6500)
    MoveCamera(45, 30, 0, 6500)
    OP_6E(750, 6500)
    SetCameraDistance(17000, 6500)
    ClearChrFlags(0x15, 0x4)
    ClearChrFlags(0x16, 0x4)
    ClearChrFlags(0x17, 0x4)

    def lambda_E1F():
        OP_9B(0x0, 0xFE, 0x0, 0x53FC, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_E1F)
    Sleep(100)

    def lambda_E37():
        OP_9B(0x0, 0xFE, 0x0, 0x53FC, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_E37)
    Sleep(100)

    def lambda_E4F():
        OP_9B(0x0, 0xFE, 0x0, 0x53FC, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_E4F)
    Sound(868, 2, 50, 0)
    BeginChrThread(0x23, 1, 0, 30)
    FadeToBright(1000, 0)
    OP_0D()
    BeginChrThread(0x12, 0, 0, 4)
    BeginChrThread(0x12, 3, 0, 6)
    BeginChrThread(0x13, 0, 0, 4)
    BeginChrThread(0x13, 3, 0, 6)
    BeginChrThread(0x14, 0, 0, 4)
    BeginChrThread(0x14, 3, 0, 6)
    BeginChrThread(0x1B, 0, 0, 4)
    BeginChrThread(0x1B, 3, 0, 6)
    BeginChrThread(0x1C, 0, 0, 4)
    BeginChrThread(0x1C, 3, 0, 6)
    BeginChrThread(0xA, 0, 0, 5)
    BeginChrThread(0xA, 3, 0, 6)
    BeginChrThread(0xB, 0, 0, 5)
    BeginChrThread(0xB, 3, 0, 6)
    BeginChrThread(0xC, 0, 0, 5)
    BeginChrThread(0xC, 3, 0, 6)
    BeginChrThread(0xD, 0, 0, 5)
    BeginChrThread(0xD, 3, 0, 6)
    BeginChrThread(0xE, 0, 0, 5)
    BeginChrThread(0xE, 3, 0, 6)
    BeginChrThread(0xF, 0, 0, 5)
    BeginChrThread(0xF, 3, 0, 6)
    BeginChrThread(0x10, 0, 0, 5)
    BeginChrThread(0x10, 3, 0, 6)
    BeginChrThread(0x11, 0, 0, 5)
    BeginChrThread(0x11, 3, 0, 6)
    PlayEffect(0x2, 0x0, 0xFF, 0x0, -5000, 250, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0x1, 0xFF, 0x0, 5000, 250, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    WaitChrThread(0x15, 1)
    Sound(540, 0, 50, 0)
    SetChrChipByIndex(0x15, 0x37)
    SetChrSubChip(0x15, 0x0)
    WaitChrThread(0x16, 1)
    SetChrChipByIndex(0x16, 0x37)
    SetChrSubChip(0x16, 0x0)
    WaitChrThread(0x17, 1)
    SetChrChipByIndex(0x17, 0x37)
    SetChrSubChip(0x17, 0x0)
    SetChrFlags(0x15, 0x4)
    SetChrFlags(0x16, 0x4)
    SetChrFlags(0x17, 0x4)
    OP_6F(0x79)
    Fade(500)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    SetChrPos(0x18, -2300, 0, -20000, 0)
    SetChrPos(0x19, 0, 0, -21000, 0)
    SetChrPos(0x1A, 2300, 0, -20000, 0)
    OP_68(0, 600, 0, 0)
    MoveCamera(0, 15, -2, 0)
    OP_6E(750, 0)
    SetCameraDistance(15750, 0)
    MoveCamera(0, 10, 2, 5000)
    SetCameraDistance(20750, 5000)
    ClearChrFlags(0x18, 0x4)
    ClearChrFlags(0x19, 0x4)
    ClearChrFlags(0x1A, 0x4)

    def lambda_1057():
        OP_9B(0x0, 0xFE, 0x0, 0x2904, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_1057)
    Sleep(100)

    def lambda_106F():
        OP_9B(0x0, 0xFE, 0x0, 0x2904, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_106F)
    Sleep(100)

    def lambda_1087():
        OP_9B(0x0, 0xFE, 0x0, 0x2904, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_1087)
    WaitChrThread(0x18, 1)
    Sound(540, 0, 50, 0)
    SetChrChipByIndex(0x18, 0x34)
    SetChrSubChip(0x18, 0x1)
    WaitChrThread(0x19, 1)
    SetChrChipByIndex(0x19, 0x34)
    SetChrSubChip(0x19, 0x1)
    WaitChrThread(0x1A, 1)
    SetChrChipByIndex(0x1A, 0x34)
    SetChrSubChip(0x1A, 0x1)
    SetChrFlags(0x18, 0x4)
    SetChrFlags(0x19, 0x4)
    SetChrFlags(0x1A, 0x4)
    OP_0D()
    OP_6F(0x79)
    StopSound(865, 1000, 40)
    StopSound(861, 1000, 40)
    OP_25(0x35F, 0x3C)
    EndChrThread(0x12, 0x0)
    EndChrThread(0x12, 0x3)
    EndChrThread(0x13, 0x0)
    EndChrThread(0x13, 0x3)
    EndChrThread(0x14, 0x0)
    EndChrThread(0x14, 0x3)
    EndChrThread(0x1B, 0x0)
    EndChrThread(0x1B, 0x3)
    EndChrThread(0x1C, 0x0)
    EndChrThread(0x1C, 0x3)
    Fade(500)
    OP_68(0, 1000, 8750, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(750, 0)
    SetCameraDistance(15000, 0)
    SetCameraDistance(14000, 2000)
    OP_0D()
    OP_6F(0x79)

    #C0001
    ChrTalk(
        0x9,
        (
            "#00607F#5P啧……！\x01",
            "为何突然间就攻到了这里……\x02\x03",

            "他们究竟是从哪里出现的！？\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x8,
        (
            "#01410F#5P很可能是驾驶\x01",
            "飞艇过来的……\x02\x03",

            "袭击玛因兹的部队在山道中突然消失，\x01",
            "恐怕也是因为乘上了飞艇。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x9, 0xE1, 0x1F4)
    Sleep(100)

    #C0003
    ChrTalk(
        0x9,
        (
            "#00610F#11P怎么可能……！\x01",
            "如果真是那样，对空雷达网\x01",
            "应该会有反应的！\x02\x03",

            "想避开雷达的探测，驾驶飞艇\x01",
            "进入自治州是不可能——\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0004
    ChrTalk(
        0x9,
        (
            "#00607F#11P啊！难道说……是『结社』\x01",
            "在利贝尔异变中所使用的……！？\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x8,
        (
            "#01403F#5P嗯……\x01",
            "也许他们配备了拥有\x01",
            "『隐形机能』的飞艇。\x02\x03",

            "#01407F但是，\x01",
            "我们现在没时间去确认这些了！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    Sound(531, 0, 60, 0)
    Sound(540, 0, 50, 0)
    Sound(859, 0, 70, 0)
    SetChrChipByIndex(0x8, 0x29)
    SetChrSubChip(0x8, 0x0)
    OP_0D()
    OP_93(0x9, 0xB4, 0x1F4)

    #C0006
    ChrTalk(
        0x9,
        "#00610F#5P唔……说的没错！\x02",
    )

    CloseMessageWindow()
    Fade(250)
    Sound(531, 0, 100, 0)
    SetChrChipByIndex(0x9, 0x24)
    SetChrSubChip(0x9, 0x0)
    OP_0D()
    OP_68(0, 1000, 7750, 750)
    Sleep(500)
    OP_25(0x35F, 0x50)
    Fade(500)
    EndChrThread(0xA, 0x0)
    EndChrThread(0xA, 0x3)
    EndChrThread(0xB, 0x0)
    EndChrThread(0xB, 0x3)
    EndChrThread(0xC, 0x0)
    EndChrThread(0xC, 0x3)
    EndChrThread(0xD, 0x0)
    EndChrThread(0xD, 0x3)
    SetChrSubChip(0xA, 0x0)

    def lambda_13F8():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0x1388)
        ExitThread()

    QueueWorkItem(0xA, 3, lambda_13F8)
    SetChrSubChip(0xB, 0x0)

    def lambda_1415():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0x1388)
        ExitThread()

    QueueWorkItem(0xB, 3, lambda_1415)
    SetChrSubChip(0xC, 0x0)

    def lambda_1432():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0x1388)
        ExitThread()

    QueueWorkItem(0xC, 3, lambda_1432)
    SetChrSubChip(0xD, 0x0)

    def lambda_144F():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0x1388)
        ExitThread()

    QueueWorkItem(0xD, 3, lambda_144F)
    OP_68(2300, 1000, -9500, 0)
    MoveCamera(180, 35, 0, 0)
    OP_6E(750, 0)
    SetCameraDistance(12250, 0)
    Sound(865, 2, 50, 0)
    Sound(861, 2, 50, 0)
    StopSound(863, 1000, 90)
    BeginChrThread(0x12, 0, 0, 4)
    BeginChrThread(0x12, 3, 0, 6)
    BeginChrThread(0x13, 0, 0, 4)
    BeginChrThread(0x13, 3, 0, 6)
    BeginChrThread(0x14, 0, 0, 4)
    BeginChrThread(0x14, 3, 0, 6)
    BeginChrThread(0x1B, 0, 0, 4)
    BeginChrThread(0x1B, 3, 0, 6)
    BeginChrThread(0x1C, 0, 0, 4)
    BeginChrThread(0x1C, 3, 0, 6)
    BeginChrThread(0x1A, 1, 0, 26)
    OP_0D()
    WaitChrThread(0x1A, 1)
    Fade(500)
    OP_68(-2300, 1000, -9500, 0)
    MoveCamera(220, 35, 0, 0)
    OP_6E(750, 0)
    SetCameraDistance(12250, 0)
    SetChrChipByIndex(0x1A, 0x32)
    SetChrSubChip(0x1A, 0x0)
    SetChrPos(0x8, -6450, 1250, 1400, 135)
    BeginChrThread(0x8, 1, 0, 7)
    OP_0D()
    WaitChrThread(0x8, 1)
    Fade(500)
    SetChrPos(0x9, 2750, 100, 4950, 180)
    SetChrPos(0xE, 3650, 110, 4450, 180)
    SetChrPos(0x21, 5600, 0, 2200, 300)
    OP_D5(0x21, 0x0, 0x493E0, 0x0, 0x0)
    SetChrPos(0x15, -650, -10, -7400, 225)
    SetChrPos(0x16, -70, -10, -10060, 270)
    SetChrPos(0x17, 250, 0, -8700, 270)
    SetChrPos(0x18, 900, -10, -12800, 315)
    OP_68(2750, 1000, 750, 0)
    MoveCamera(345, 35, 5, 0)
    OP_6E(750, 0)
    SetCameraDistance(13000, 0)
    OP_68(-2500, 1000, -8650, 3000)
    MoveCamera(325, 30, 8, 3000)
    SetCameraDistance(18500, 12000)
    BeginChrThread(0x9, 1, 0, 9)
    Sleep(2500)
    BeginChrThread(0x8, 1, 0, 8)
    Sleep(5500)
    StopSound(865, 2000, 40)
    StopSound(861, 2000, 40)
    OP_24(0x364)
    FadeToDark(2000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 0)
    NewScene("e3800", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_3_7BC end

    def Function_4_165C(): pass

    label("Function_4_165C")

    SetChrChipByIndex(0xFE, 0x34)

    label("loc_1660")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_16AF")
    PlayEffect(0x0, 0xFF, 0xFE, 0x3, 100, 950, 1700, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    OP_A1(0xFE, 0xBB8, 0x2, 0x2, 0x1)
    Jump("loc_1660")

    label("loc_16AF")

    Return()

    # Function_4_165C end

    def Function_5_16B0(): pass

    label("Function_5_16B0")

    SetChrChipByIndex(0xFE, 0x2D)

    label("loc_16B4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1709")
    PlayEffect(0x0, 0xFF, 0xFE, 0x3, 0, 1100, 1100, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0xFE, 0x1)
    Sleep(500)
    SetChrSubChip(0xFE, 0x0)
    Sleep(700)
    Jump("loc_16B4")

    label("loc_1709")

    Return()

    # Function_5_16B0 end

    def Function_6_170A(): pass

    label("Function_6_170A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_173D")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x50), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1731")
    OP_4C(0xFE, 0x0)
    Jump("loc_1735")

    label("loc_1731")

    OP_4B(0xFE, 0x0)

    label("loc_1735")

    Sleep(500)
    Jump("Function_6_170A")

    label("loc_173D")

    Return()

    # Function_6_170A end

    def Function_7_173E(): pass

    label("Function_7_173E")

    OP_68(-2300, 1000, -9500, 750)
    MoveCamera(230, 35, 5, 750)
    SetCameraDistance(11250, 750)
    Fade(250)
    OP_93(0x18, 0x13B, 0x0)
    SetCameraDistance(12750, 300)
    Sound(531, 0, 100, 0)
    Sound(358, 0, 60, 0)
    SetChrChipByIndex(0x18, 0x3B)
    OP_A0(0x18, 1000, 0x0, 0x1)
    OP_0D()
    Sleep(300)
    OP_6F(0x79)
    Fade(500)
    OP_68(-5100, 1500, -2750, 0)
    MoveCamera(210, 35, 5, 0)
    SetCameraDistance(11750, 0)
    OP_68(-2600, 1000, -9200, 500)
    MoveCamera(200, 35, 5, 500)
    Sound(540, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x2B)
    SetChrSubChip(0xFE, 0x2)
    Sound(551, 0, 100, 0)
    PlayEffect(0x6, 0x2, 0xFE, 0x3, 250, 1000, 1000, 90, -45, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sound(809, 0, 100, 0)
    OP_9D(0xFE, 0xFFFFF5BA, 0x0, 0xFFFFDE04, 0x5DC, 0x7D0)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    StopEffect(0x2, 0x0)
    SetChrChipByIndex(0xFE, 0x2C)
    SetChrSubChip(0xFE, 0x4)
    OP_82(0x64, 0x64, 0xBB8, 0x1F4)
    Sound(833, 0, 100, 0)
    SetCameraDistance(13750, 500)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0x1)
    CancelBlur(1000)
    Sound(264, 0, 100, 0)
    PlayEffect(0x5, 0xFF, 0xFE, 0x5, 0, 0, 1000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    BeginChrThread(0x18, 1, 0, 18)
    Sleep(500)
    SetChrSubChip(0xFE, 0x3)
    EndChrThread(0x12, 0x0)
    EndChrThread(0x12, 0x3)
    EndChrThread(0x13, 0x0)
    EndChrThread(0x13, 0x3)
    EndChrThread(0x14, 0x0)
    EndChrThread(0x14, 0x3)
    EndChrThread(0x1B, 0x0)
    EndChrThread(0x1B, 0x3)
    EndChrThread(0x1C, 0x0)
    EndChrThread(0x1C, 0x3)
    StopEffect(0x0, 0x2)
    StopEffect(0x1, 0x2)

    def lambda_1912():
        TurnDirection(0xFE, 0x8, 1000)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_1912)

    def lambda_191F():
        TurnDirection(0xFE, 0x8, 1000)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_191F)

    def lambda_192C():
        TurnDirection(0xFE, 0x8, 1000)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_192C)

    def lambda_1939():
        TurnDirection(0xFE, 0x8, 1000)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_1939)

    def lambda_1946():
        TurnDirection(0xFE, 0x8, 1000)
        ExitThread()

    QueueWorkItem(0x16, 2, lambda_1946)

    def lambda_1953():
        TurnDirection(0xFE, 0x8, 1000)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_1953)

    def lambda_1960():
        TurnDirection(0xFE, 0x8, 1000)
        ExitThread()

    QueueWorkItem(0x19, 2, lambda_1960)

    def lambda_196D():
        TurnDirection(0xFE, 0x8, 1000)
        ExitThread()

    QueueWorkItem(0x1A, 2, lambda_196D)

    def lambda_197A():
        TurnDirection(0xFE, 0x8, 1000)
        ExitThread()

    QueueWorkItem(0x1B, 2, lambda_197A)

    def lambda_1987():
        TurnDirection(0xFE, 0x8, 1000)
        ExitThread()

    QueueWorkItem(0x1C, 2, lambda_1987)
    WaitChrThread(0x12, 2)
    WaitChrThread(0x13, 2)
    WaitChrThread(0x14, 2)
    WaitChrThread(0x15, 2)
    WaitChrThread(0x16, 2)
    WaitChrThread(0x17, 2)
    WaitChrThread(0x19, 2)
    WaitChrThread(0x1A, 2)
    WaitChrThread(0x1B, 2)
    WaitChrThread(0x1C, 2)
    WaitChrThread(0x18, 1)
    Sleep(500)
    Return()

    # Function_7_173E end

    def Function_8_19BF(): pass

    label("Function_8_19BF")

    SetChrFlags(0x8, 0x20)
    SetChrFlags(0x15, 0x20)
    SetChrFlags(0x16, 0x20)
    SetChrFlags(0x17, 0x20)
    WaitChrThread(0x15, 1)
    WaitChrThread(0x16, 1)
    SetChrChipByIndex(0x15, 0x39)
    SetChrSubChip(0x15, 0x2)
    OP_52(0x15, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sound(809, 0, 100, 0)
    OP_9D(0x15, 0xFFFFF5E2, 0x0, 0xFFFFE08E, 0x7D0, 0x1388)
    Sound(538, 0, 100, 0)
    OP_52(0x15, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TurnDirection(0xFE, 0x15, 0)
    Sound(250, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x2B)

    def lambda_1A32():
        OP_A0(0xFE, 1500, 0x0, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 0, lambda_1A32)

    def lambda_1A3F():
        OP_9B(0x1, 0xFE, 0x5A, 0xFFFFFC18, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_1A3F)
    Sound(533, 0, 50, 0)
    SetChrSubChip(0x15, 0x3)
    Sleep(50)
    SetChrSubChip(0x15, 0x4)
    WaitChrThread(0xFE, 0)
    WaitChrThread(0xFE, 3)
    Sleep(500)
    TurnDirection(0xFE, 0x15, 0)

    def lambda_1A77():
        OP_A0(0xFE, 1500, 0x2, 0x3)
        ExitThread()

    QueueWorkItem(0xFE, 0, lambda_1A77)

    def lambda_1A84():
        OP_9B(0x1, 0xFE, 0x0, 0x3E8, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_1A84)
    Sound(551, 0, 100, 0)
    Sound(540, 0, 100, 0)
    PlayEffect(0x8, 0xFF, 0xFE, 0x3, 0, 850, 0, 0, 0, 0, 900, 900, 900, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0x15, 0x0)

    def lambda_1AE0():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0x1388)
        ExitThread()

    QueueWorkItem(0x15, 0, lambda_1AE0)

    def lambda_1AF9():
        OP_96(0xFE, 0xFFFFFA24, 0x0, 0xFFFFE66A, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 3, lambda_1AF9)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0x0)
    CancelBlur(500)
    Sleep(300)
    Sound(538, 0, 60, 0)
    SetChrChipByIndex(0x16, 0x3C)
    OP_A0(0x16, 1000, 0x0, 0x1)
    Sleep(500)

    def lambda_1B3B():
        OP_A0(0xFE, 1500, 0x2, 0x3)
        ExitThread()

    QueueWorkItem(0x16, 0, lambda_1B3B)

    def lambda_1B48():
        OP_9A(0xFE, 0x8, 0x3E8, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 3, lambda_1B48)
    SetChrChipByIndex(0x15, 0x37)
    SetChrSubChip(0x15, 0x0)
    Sound(264, 0, 100, 0)
    PlayEffect(0x7, 0xFF, 0xFE, 0x5, 0, 0, 0, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    SetChrChipByIndex(0xFE, 0x2C)

    def lambda_1BA5():
        TurnDirection(0xFE, 0x16, 3000)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1BA5)
    OP_A0(0xFE, 1500, 0x0, 0x1)
    EndChrThread(0x16, 0x0)
    EndChrThread(0x16, 0x3)
    BeginChrThread(0x16, 0, 0, 16)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0x0)
    CancelBlur(500)
    Sleep(500)
    Sound(538, 0, 70, 0)
    SetChrChipByIndex(0x15, 0x39)

    def lambda_1BE5():
        OP_9A(0xFE, 0x8, 0x2EE, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_1BE5)

    def lambda_1BF9():
        OP_A0(0xFE, 1500, 0x1, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 0, lambda_1BF9)
    Sleep(50)
    SetChrChipByIndex(0x17, 0x39)

    def lambda_1C0D():
        OP_9A(0xFE, 0x8, 0x2EE, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_1C0D)

    def lambda_1C21():
        OP_A0(0xFE, 1500, 0x1, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 0, lambda_1C21)
    OP_93(0xFE, 0x2D, 0x0)
    Sound(566, 0, 50, 0)
    Sound(540, 0, 50, 0)
    SetChrChipByIndex(0xFE, 0x2B)
    SetChrSubChip(0xFE, 0x1)

    def lambda_1C49():
        OP_A6(0xFE, 0xA, 0xA, 0x0, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1C49)

    def lambda_1C62():
        OP_A6(0xFE, 0xA, 0xA, 0x0, 0xBB8)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_1C62)

    def lambda_1C7B():
        OP_A6(0xFE, 0xA, 0xA, 0x0, 0xBB8)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_1C7B)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0x0)
    CancelBlur(500)
    Sleep(500)
    WaitChrThread(0x16, 0)
    OP_A6(0x16, 0x0, 0x32, 0x1F4, 0xBB8)
    Sound(802, 0, 100, 0)
    SetChrChipByIndex(0x16, 0x37)
    SetChrSubChip(0x16, 0x0)
    Sleep(300)
    SetChrChipByIndex(0x16, 0x38)
    ClearChrFlags(0x16, 0x20)
    OP_96(0x16, 0xFFFFF6A0, 0x0, 0xFFFFD3DC, 0xFA0, 0x0)
    SetChrFlags(0x16, 0x20)
    SetChrChipByIndex(0x16, 0x37)
    SetChrSubChip(0x16, 0x0)
    EndChrThread(0xFE, 0x2)
    EndChrThread(0x16, 0x2)
    EndChrThread(0x17, 0x2)
    SetChrSubChip(0xFE, 0x0)
    SetChrChip(0x0, 0xFE, 0x1E, 0xC8)

    def lambda_1D12():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFA24, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1D12)
    Sound(533, 0, 50, 0)

    def lambda_1D2D():
        OP_A0(0xFE, 1500, 0x3, 0x4)
        ExitThread()

    QueueWorkItem(0x15, 0, lambda_1D2D)

    def lambda_1D3A():
        OP_A0(0xFE, 1500, 0x3, 0x4)
        ExitThread()

    QueueWorkItem(0x17, 0, lambda_1D3A)
    WaitChrThread(0x15, 0)
    WaitChrThread(0x17, 0)
    WaitChrThread(0xFE, 2)
    Sleep(500)
    SetChrSubChip(0xFE, 0x2)
    Sound(289, 0, 100, 0)
    PlayEffect(0x6, 0x2, 0xFE, 0x3, 250, 1000, 1000, 90, -45, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sound(809, 0, 100, 0)
    OP_9D(0xFE, 0xFFFFF3B2, 0x0, 0xFFFFE05C, 0xBB8, 0x1388)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    StopEffect(0x2, 0x0)
    SetChrChipByIndex(0xFE, 0x2C)
    SetChrSubChip(0xFE, 0x4)
    OP_82(0x64, 0x64, 0xBB8, 0x1F4)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0x1)
    CancelBlur(1000)
    Sound(264, 0, 100, 0)
    PlayEffect(0x5, 0xFF, 0xFE, 0x5, 0, 0, 500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    BeginChrThread(0x15, 0, 0, 15)
    BeginChrThread(0x17, 0, 0, 17)
    Return()

    # Function_8_19BF end

    def Function_9_1E44(): pass

    label("Function_9_1E44")

    SetChrChipByIndex(0x9, 0x25)
    OP_95(0x9, 2600, 100, 3200, 4000, 0x0)
    OP_93(0x9, 0xB4, 0x3E8)
    SetChrChipByIndex(0x9, 0x26)
    SetChrSubChip(0x9, 0x0)
    Sleep(300)
    Sound(567, 0, 100, 0)
    PlayEffect(0x0, 0xFF, 0xFE, 0x3, 100, 950, 1000, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    OP_A1(0x9, 0x1388, 0x2, 0x1, 0x2)
    BeginChrThread(0x12, 1, 0, 14)

    def lambda_1EBE():
        OP_93(0xFE, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_1EBE)

    def lambda_1ECB():
        OP_93(0xFE, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_1ECB)

    def lambda_1ED8():
        OP_93(0xFE, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x19, 2, lambda_1ED8)

    def lambda_1EE5():
        OP_93(0xFE, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x1A, 2, lambda_1EE5)

    def lambda_1EF2():
        OP_93(0xFE, 0x2D, 0x3E8)
        ExitThread()

    QueueWorkItem(0x1B, 2, lambda_1EF2)

    def lambda_1EFF():
        OP_93(0xFE, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x1C, 2, lambda_1EFF)
    WaitChrThread(0x13, 2)
    WaitChrThread(0x14, 2)
    WaitChrThread(0x19, 2)
    WaitChrThread(0x1A, 2)
    WaitChrThread(0x1B, 2)
    WaitChrThread(0x1C, 2)
    Sleep(300)
    Sound(567, 0, 100, 0)
    PlayEffect(0x0, 0xFF, 0xFE, 0x3, 100, 950, 1000, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    OP_A1(0x9, 0x1388, 0x2, 0x1, 0x2)
    BeginChrThread(0x1B, 1, 0, 19)
    Sleep(500)
    BeginChrThread(0x13, 0, 0, 4)
    BeginChrThread(0x13, 3, 0, 6)
    BeginChrThread(0x14, 0, 0, 4)
    BeginChrThread(0x14, 3, 0, 6)
    BeginChrThread(0x1C, 0, 0, 4)
    BeginChrThread(0x1C, 3, 0, 6)
    BeginChrThread(0x15, 1, 0, 23)
    Sleep(50)
    BeginChrThread(0x16, 1, 0, 24)
    Sleep(50)
    BeginChrThread(0x19, 1, 0, 25)
    Sleep(50)
    BeginChrThread(0x1A, 1, 0, 27)
    PlayEffect(0x2, 0x1, 0xFF, 0x0, 5000, 250, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    BeginChrThread(0xFE, 0, 0, 10)
    BeginChrThread(0xFE, 3, 0, 6)
    Return()

    # Function_9_1E44 end

    def Function_10_1FF9(): pass

    label("Function_10_1FF9")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2061")
    SetChrChipByIndex(0x9, 0x26)
    OP_A1(0x9, 0x1388, 0x3, 0x3, 0x4, 0x0)
    Sleep(300)
    Sound(567, 0, 70, 0)
    PlayEffect(0x0, 0xFF, 0xFE, 0x3, 100, 950, 1000, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    OP_A1(0x9, 0x1388, 0x2, 0x1, 0x2)
    Sleep(700)
    Jump("Function_10_1FF9")

    label("loc_2061")

    Return()

    # Function_10_1FF9 end

    def Function_11_2062(): pass

    label("Function_11_2062")

    OP_93(0xFE, 0xB4, 0x0)
    SetChrChipByIndex(0xFE, 0x2E)
    SetChrSubChip(0xFE, 0x0)

    def lambda_2076():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_2076)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sound(251, 0, 70, 0)
    OP_9D(0xFE, 0x222E, 0xB4, 0x1356, 0x3E8, 0x1388)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xFE, 0x2F)
    SetChrSubChip(0xFE, 0x0)
    Sound(514, 0, 100, 0)
    Return()

    # Function_11_2062 end

    def Function_12_20CC(): pass

    label("Function_12_20CC")

    OP_93(0xFE, 0xE1, 0x0)
    SetChrChipByIndex(0xFE, 0x2E)
    SetChrSubChip(0xFE, 0x0)

    def lambda_20E0():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_20E0)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_9D(0xFE, 0x2EAE, 0x0, 0xC4E, 0x3E8, 0x1388)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xFE, 0x2F)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_12_20CC end

    def Function_13_212A(): pass

    label("Function_13_212A")

    OP_93(0xFE, 0x10E, 0x0)
    SetChrChipByIndex(0xFE, 0x2E)
    SetChrSubChip(0xFE, 0x0)

    def lambda_213E():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_213E)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_9D(0xFE, 0x399E, 0x0, 0xFFFFF0F6, 0x3E8, 0x1388)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xFE, 0x2F)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_13_212A end

    def Function_14_2188(): pass

    label("Function_14_2188")

    OP_93(0xFE, 0x2D, 0x0)
    SetChrChipByIndex(0xFE, 0x35)
    SetChrSubChip(0xFE, 0x0)
    Sound(501, 0, 100, 0)
    PlayEffect(0x3, 0xFF, 0xFE, 0x1, 0, 1000, 0, 0, 0, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)

    def lambda_21D9():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_21D9)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sound(251, 0, 50, 0)
    OP_9D(0xFE, 0xFFFFEE3A, 0x0, 0xFFFFEB1A, 0x3E8, 0xBB8)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrSubChip(0xFE, 0x3)
    Sound(514, 0, 100, 0)
    Return()

    # Function_14_2188 end

    def Function_15_222B(): pass

    label("Function_15_222B")

    OP_93(0xFE, 0xE1, 0x0)
    SetChrChipByIndex(0xFE, 0x3A)
    SetChrSubChip(0xFE, 0x0)
    Sound(501, 0, 100, 0)
    PlayEffect(0x3, 0xFF, 0xFE, 0x1, 0, 1000, 0, 0, 0, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)

    def lambda_227C():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_227C)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sound(251, 0, 50, 0)
    OP_9D(0xFE, 0xFFFFFA24, 0x0, 0xFFFFE85E, 0x3E8, 0x7D0)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrSubChip(0xFE, 0x3)
    Sound(514, 0, 100, 0)
    Return()

    # Function_15_222B end

    def Function_16_22CE(): pass

    label("Function_16_22CE")

    OP_93(0xFE, 0x0, 0x0)
    SetChrChipByIndex(0xFE, 0x3A)
    SetChrSubChip(0xFE, 0x0)
    PlayEffect(0x3, 0xFF, 0xFE, 0x1, 0, 1000, 0, 0, 0, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)

    def lambda_2319():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_2319)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sound(251, 0, 50, 0)
    OP_9D(0xFE, 0xFFFFF704, 0x0, 0xFFFFD472, 0x3E8, 0x7D0)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrSubChip(0xFE, 0x3)
    Sound(514, 0, 100, 0)
    Return()

    # Function_16_22CE end

    def Function_17_236B(): pass

    label("Function_17_236B")

    OP_93(0xFE, 0x10E, 0x0)
    SetChrChipByIndex(0xFE, 0x3A)
    SetChrSubChip(0xFE, 0x0)
    PlayEffect(0x3, 0xFF, 0xFE, 0x1, 0, 1000, 0, 0, 0, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)

    def lambda_23B6():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_23B6)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_9D(0xFE, 0x0, 0x0, 0xFFFFDF94, 0x3E8, 0x7D0)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrSubChip(0xFE, 0x3)
    Return()

    # Function_17_236B end

    def Function_18_23FC(): pass

    label("Function_18_23FC")

    OP_93(0xFE, 0x13B, 0x0)
    SetChrChipByIndex(0xFE, 0x35)
    SetChrSubChip(0xFE, 0x0)
    PlayEffect(0x3, 0xFF, 0xFE, 0x1, 0, 1000, 0, 0, 0, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)

    def lambda_2447():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_2447)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sound(251, 0, 60, 0)
    OP_9D(0xFE, 0xFFFFFD12, 0x0, 0xFFFFD120, 0x3E8, 0xBB8)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrSubChip(0xFE, 0x3)
    Sound(514, 0, 100, 0)
    Return()

    # Function_18_23FC end

    def Function_19_2499(): pass

    label("Function_19_2499")

    OP_93(0xFE, 0x2D, 0x0)
    SetChrChipByIndex(0xFE, 0x35)
    SetChrSubChip(0xFE, 0x0)
    Sound(501, 0, 100, 0)
    PlayEffect(0x3, 0xFF, 0xFE, 0x1, 0, 1000, 0, 0, 0, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)

    def lambda_24EA():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_24EA)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sound(251, 0, 50, 0)
    OP_9D(0xFE, 0xFFFFEBB0, 0x0, 0xFFFFE318, 0x3E8, 0xBB8)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrSubChip(0xFE, 0x3)
    Sound(514, 0, 100, 0)
    Return()

    # Function_19_2499 end

    def Function_20_253C(): pass

    label("Function_20_253C")

    SetChrChipByIndex(0xFE, 0x33)
    OP_95(0xFE, -9400, 0, -6500, 4000, 0x0)
    OP_95(0xFE, -14000, 0, -4950, 4000, 0x0)
    OP_93(0xFE, 0x2D, 0x3E8)
    BeginChrThread(0xFE, 0, 0, 4)
    BeginChrThread(0xFE, 3, 0, 6)
    Return()

    # Function_20_253C end

    def Function_21_257C(): pass

    label("Function_21_257C")

    SetChrChipByIndex(0xFE, 0x33)
    OP_95(0xFE, 10500, 0, -4810, 5000, 0x0)
    OP_95(0xFE, 11100, 0, -3750, 5000, 0x0)
    OP_93(0xFE, 0x159, 0x3E8)
    BeginChrThread(0xFE, 0, 0, 4)
    BeginChrThread(0xFE, 3, 0, 6)
    Return()

    # Function_21_257C end

    def Function_22_25BC(): pass

    label("Function_22_25BC")

    SetChrChipByIndex(0xFE, 0x33)
    OP_95(0xFE, 10500, 0, -4810, 5000, 0x0)
    OP_95(0xFE, 13350, 0, -3150, 5000, 0x0)
    OP_93(0xFE, 0x159, 0x3E8)
    BeginChrThread(0xFE, 0, 0, 4)
    BeginChrThread(0xFE, 3, 0, 6)
    Return()

    # Function_22_25BC end

    def Function_23_25FC(): pass

    label("Function_23_25FC")

    SetChrChipByIndex(0xFE, 0x38)
    OP_96(0xFE, 0xFFFFF66E, 0x0, 0xFFFFE926, 0x1388, 0x0)
    OP_93(0xFE, 0xB4, 0x3E8)
    SetChrChipByIndex(0xFE, 0x37)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_23_25FC end

    def Function_24_2624(): pass

    label("Function_24_2624")

    SetChrChipByIndex(0xFE, 0x38)
    OP_96(0xFE, 0xFFFFF6A0, 0x0, 0xFFFFD3DC, 0x1388, 0x0)
    OP_93(0xFE, 0x0, 0x3E8)
    SetChrChipByIndex(0xFE, 0x37)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_24_2624 end

    def Function_25_264C(): pass

    label("Function_25_264C")

    SetChrChipByIndex(0xFE, 0x33)
    OP_95(0xFE, 250, -10, -11350, 4000, 0x0)
    OP_93(0xFE, 0x13B, 0x3E8)
    PlayEffect(0x2, 0x0, 0xFF, 0x0, -2800, 250, -8700, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    BeginChrThread(0xFE, 0, 0, 4)
    BeginChrThread(0xFE, 3, 0, 6)
    Return()

    # Function_25_264C end

    def Function_26_26AF(): pass

    label("Function_26_26AF")

    OP_68(2300, 1000, -9500, 750)
    MoveCamera(165, 35, 5, 750)
    SetCameraDistance(11250, 750)
    OP_93(0xFE, 0x2D, 0x0)
    Sound(531, 0, 100, 0)
    Sound(358, 0, 60, 0)
    SetChrChipByIndex(0xFE, 0x3B)
    OP_A0(0xFE, 1000, 0x0, 0x1)
    OP_0D()
    Sleep(300)
    OP_6F(0x79)
    OP_68(8800, 1250, -1800, 500)
    MoveCamera(125, 35, 5, 500)

    def lambda_2719():
        OP_A0(0xFE, 1500, 0x2, 0x4)
        ExitThread()

    QueueWorkItem(0xFE, 0, lambda_2719)
    Sound(545, 0, 100, 0)
    PlayEffect(0x4, 0x2, 0xFE, 0x5, 0, 800, 500, 0, 0, 0, 1000, 1000, 1000, 0x20, 0, 0, 0, 0)
    Sleep(500)
    Fade(250)
    SetMapObjFlags(0xC, 0x4)
    ClearMapObjFlags(0xE, 0x4)
    OP_82(0x3E8, 0x0, 0xBB8, 0x3E8)
    Sound(200, 0, 100, 0)
    SetCameraDistance(17000, 500)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0x1)
    CancelBlur(1000)
    EndChrThread(0xF, 0x0)
    EndChrThread(0xF, 0x3)
    EndChrThread(0x10, 0x0)
    EndChrThread(0x10, 0x3)
    EndChrThread(0x11, 0x0)
    EndChrThread(0x11, 0x3)
    BeginChrThread(0xF, 1, 0, 11)
    BeginChrThread(0x10, 1, 0, 12)
    BeginChrThread(0x11, 1, 0, 13)
    OP_71(0xE, 0x1, 0x3C, 0x0, 0x8)
    OP_79(0xE)
    OP_71(0xE, 0x3D, 0x78, 0x0, 0x20)
    OP_0D()
    OP_63(0xA, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0xB, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0xC, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0xD, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0xE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    WaitChrThread(0xF, 1)
    WaitChrThread(0x10, 1)
    WaitChrThread(0x11, 1)
    Return()

    # Function_26_26AF end

    def Function_27_2850(): pass

    label("Function_27_2850")

    SetChrChipByIndex(0xFE, 0x33)
    OP_95(0xFE, 1300, -10, -5600, 4000, 0x0)
    OP_93(0xFE, 0xE1, 0x3E8)
    BeginChrThread(0xFE, 0, 0, 4)
    BeginChrThread(0xFE, 3, 0, 6)
    Return()

    # Function_27_2850 end

    def Function_28_287C(): pass

    label("Function_28_287C")

    SetChrChipByIndex(0xFE, 0x33)
    OP_95(0xFE, -10200, 0, -5750, 4000, 0x0)
    OP_95(0xFE, -14450, 0, -3850, 4000, 0x0)
    OP_93(0xFE, 0x2D, 0x3E8)
    BeginChrThread(0xFE, 0, 0, 4)
    BeginChrThread(0xFE, 3, 0, 6)
    Return()

    # Function_28_287C end

    def Function_29_28BC(): pass

    label("Function_29_28BC")

    SetChrChipByIndex(0xFE, 0x33)
    OP_95(0xFE, 11340, 0, -4800, 5000, 0x0)
    OP_95(0xFE, 15200, 0, -1800, 5000, 0x0)
    OP_93(0xFE, 0x159, 0x3E8)
    BeginChrThread(0xFE, 0, 0, 4)
    BeginChrThread(0xFE, 3, 0, 6)
    Return()

    # Function_29_28BC end

    def Function_30_28FC(): pass

    label("Function_30_28FC")

    Sound(865, 2, 0, 0)
    Sound(861, 2, 0, 0)
    Sound(863, 2, 0, 0)
    Sleep(200)
    OP_25(0x35F, 0xA)
    OP_25(0x361, 0xA)
    OP_25(0x35D, 0xA)
    Sleep(200)
    OP_25(0x35F, 0xF)
    OP_25(0x361, 0xF)
    OP_25(0x35D, 0xF)
    Sleep(200)
    OP_25(0x35F, 0x14)
    OP_25(0x361, 0x14)
    OP_25(0x35D, 0x14)
    Sleep(200)
    OP_25(0x35F, 0x19)
    OP_25(0x361, 0x19)
    OP_25(0x35D, 0x19)
    Sleep(200)
    OP_25(0x35F, 0x1E)
    OP_25(0x361, 0x1E)
    OP_25(0x35D, 0x1E)
    Sleep(200)
    OP_25(0x35F, 0x23)
    OP_25(0x361, 0x23)
    OP_25(0x35D, 0x23)
    Sleep(200)
    OP_25(0x35F, 0x28)
    OP_25(0x361, 0x28)
    OP_25(0x35D, 0x28)
    Sleep(200)
    OP_25(0x35F, 0x2D)
    OP_25(0x361, 0x2D)
    OP_25(0x35D, 0x2D)
    Sleep(200)
    OP_25(0x35F, 0x32)
    OP_25(0x361, 0x32)
    OP_25(0x35D, 0x32)
    Sleep(200)
    OP_25(0x35F, 0x3C)
    Sleep(400)
    OP_25(0x35F, 0x46)
    Sleep(200)
    OP_25(0x35F, 0x50)
    Return()

    # Function_30_28FC end

    SaveToFile()

Try(main)
