from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c040b.bin",                # FileName
        "c040b",                    # MapName
        "c040b",                    # Location
        0x0022,                     # MapIndex
        "ed7113",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x1E,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 34, 0, 0, 0, 1],
    )

    BuildStringList((
        "c040b",                  # 0
        "警官隊",                 # 1
        "警官隊",                 # 2
        "警官隊",                 # 3
        "警官隊",                 # 4
        "警官隊",                 # 5
        "警官隊",                 # 6
        "猟兵",                   # 7
        "猟兵",                   # 8
        "猟兵",                   # 9
        "猟兵",                   # 10
        "猟兵",                   # 11
        "猟兵",                   # 12
        "猟兵",                   # 13
        "猟兵",                   # 14
        "猟兵",                   # 15
        "猟兵",                   # 16
        "猟兵",                   # 17
        "猟兵",                   # 18
        "軍用魔獣",               # 19
        "軍用魔獣",               # 20
        "パトカー",               # 21
        "パトカー",               # 22
        "パトカー",               # 23
        "パトカー",               # 24
        "SE制御",                 # 25
        "中央広場",               # 26
        "西通り",                 # 27
        "行政区",                 # 28
        "住宅街",                 # 29
        "歓楽街",                 # 30
        "東通り",                 # 31
        "旧市街",                 # 32
        "港湾区",                 # 33
        "ＩＢＣ",                 # 34
        "駅前通り",               # 35
        "裏通り",                 # 36
        "ウルスラ間道",           # 37
        "東クロスベル街道",       # 38
        "西クロスベル街道",       # 39
        "マインツ山道",           # 40
        "オルキスタワー",         # 41
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
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    PlaceName(90.5999984741211, 0.0, -111.88999938964844, 0x0000, 0x0000, "中央広場")
    PlaceName(-19.209999084472656, 0.0, -104.37999725341797, 0x0000, 0x0000, "西通り")
    PlaceName(135.69000244140625, 0.0, 36.7400016784668, 0x0000, 0x0000, "行政区")
    PlaceName(-121.08000183105469, 0.0, 20.040000915527344, 0x0000, 0x0000, "住宅街")
    PlaceName(0.8399999737739563, 0.0, 6.679999828338623, 0x0000, 0x0000, "歓楽街")
    PlaceName(226.2899932861328, 0.0, -150.3000030517578, 0x0000, 0x0000, "東通り")
    PlaceName(285.57000732421875, 0.0, -242.14999389648438, 0x0000, 0x0000, "旧市街")
    PlaceName(273.04998779296875, 0.0, -40.08000183105469, 0x0000, 0x0000, "港湾区")
    PlaceName(229.6300048828125, 0.0, 116.9000015258789, 0x0000, 0x0000, "ＩＢＣ")
    PlaceName(109.38999938964844, 0.0, -227.1199951171875, 0x0000, 0x0000, "駅前通り")
    PlaceName(30.899999618530273, 0.0, -53.439998626708984, 0x0000, 0x0000, "裏通り")
    PlaceName(104.37999725341797, 0.0, -278.8900146484375, 0x0000, 0x0000, "ウルスラ間道")
    PlaceName(316.4700012207031, 0.0, -126.91999816894531, 0x0000, 0x0000, "東クロスベル街道")
    PlaceName(-104.37999725341797, 0.0, -106.87999725341797, 0x0000, 0x0000, "西クロスベル街道")
    PlaceName(-94.36000061035156, 0.0, 60.119998931884766, 0x0000, 0x0000, "マインツ山道")
    PlaceName(124.0, 0.0, 255.0, 0x0000, 0x0000, "オルキスタワー")
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

    ChipFrameInfo(1532, 0)                                       # 0

    ScpFunction((
        "Function_0_5FC",          # 00, 0
        "Function_1_60C",          # 01, 1
        "Function_2_60D",          # 02, 2
        "Function_3_13EE",         # 03, 3
        "Function_4_143E",         # 04, 4
        "Function_5_1497",         # 05, 5
        "Function_6_14CB",         # 06, 6
        "Function_7_1726",         # 07, 7
        "Function_8_17F0",         # 08, 8
        "Function_9_1822",         # 09, 9
        "Function_10_1A5F",        # 0A, 10
        "Function_11_1B39",        # 0B, 11
        "Function_12_1D28",        # 0C, 12
        "Function_13_1DB3",        # 0D, 13
        "Function_14_1E1C",        # 0E, 14
        "Function_15_1E73",        # 0F, 15
        "Function_16_1ED1",        # 10, 16
        "Function_17_1F0E",        # 11, 17
        "Function_18_1F4B",        # 12, 18
        "Function_19_1F9A",        # 13, 19
        "Function_20_1FB4",        # 14, 20
    ))


    def Function_0_5FC(): pass

    label("Function_0_5FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_60B")
    ClearScenarioFlags(0x22, 0)
    Event(0, 2)

    label("loc_60B")

    Return()

    # Function_0_5FC end

    def Function_1_60C(): pass

    label("Function_1_60C")

    Return()

    # Function_1_60C end

    def Function_2_60D(): pass

    label("Function_2_60D")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    LoadChrToIndex("monster/ch82050.itc", 0x1E)
    LoadChrToIndex("monster/ch82051.itc", 0x1F)
    LoadChrToIndex("monster/ch82052.itc", 0x20)
    LoadChrToIndex("apl/ch51236.itc", 0x23)
    LoadChrToIndex("apl/ch51262.itc", 0x24)
    LoadChrToIndex("apl/ch51263.itc", 0x25)
    LoadChrToIndex("chr/ch41950.itc", 0x28)
    LoadChrToIndex("chr/ch41951.itc", 0x29)
    LoadChrToIndex("chr/ch41952.itc", 0x2A)
    LoadChrToIndex("chr/ch41954.itc", 0x2B)
    LoadChrToIndex("chr/ch42050.itc", 0x2D)
    LoadChrToIndex("chr/ch42051.itc", 0x2E)
    LoadChrToIndex("chr/ch42052.itc", 0x2F)
    LoadChrToIndex("chr/ch42056.itc", 0x30)
    LoadChrToIndex("chr/ch42057.itc", 0x31)
    LoadEffect(0x0, "battle/btgun00.eff")
    LoadEffect(0x1, "event/ev606_00.eff")
    LoadEffect(0x2, "battle/sp003000.eff")
    LoadEffect(0x3, "battle/ms00001.eff")
    LoadEffect(0x4, "event/ev15027.eff")
    LoadEffect(0x9, "event/ev15021.eff")
    PlayEffect(0x9, 0x7, 0xFF, 0x0, 200000, 300000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SoundLoad(868)
    SoundLoad(865)
    SoundLoad(861)
    SetChrChipByIndex(0x8, 0x23)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0x8, 0x20)
    SetChrChipByIndex(0x9, 0x23)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    SetChrFlags(0x9, 0x20)
    SetChrChipByIndex(0xA, 0x23)
    SetChrSubChip(0xA, 0x0)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)
    SetChrFlags(0xA, 0x20)
    SetChrChipByIndex(0xB, 0x23)
    SetChrSubChip(0xB, 0x0)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8000)
    SetChrFlags(0xB, 0x20)
    SetChrChipByIndex(0xC, 0x23)
    SetChrSubChip(0xC, 0x0)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8000)
    SetChrFlags(0xC, 0x20)
    SetChrChipByIndex(0xE, 0x2A)
    SetChrSubChip(0xE, 0x1)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x8000)
    SetChrChipByIndex(0xF, 0x2A)
    SetChrSubChip(0xF, 0x1)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x8000)
    SetChrChipByIndex(0x10, 0x2A)
    SetChrSubChip(0x10, 0x1)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x8000)
    SetChrChipByIndex(0x11, 0x2E)
    SetChrSubChip(0x11, 0x0)
    SetChrFlags(0x11, 0x8000)
    SetChrChipByIndex(0x12, 0x2E)
    SetChrSubChip(0x12, 0x0)
    SetChrFlags(0x12, 0x8000)
    SetChrChipByIndex(0x13, 0x2E)
    SetChrSubChip(0x13, 0x0)
    SetChrFlags(0x13, 0x8000)
    SetChrChipByIndex(0x14, 0x2E)
    SetChrSubChip(0x14, 0x0)
    SetChrFlags(0x14, 0x8000)
    SetChrChipByIndex(0x15, 0x2E)
    SetChrSubChip(0x15, 0x0)
    SetChrFlags(0x15, 0x8000)
    SetChrChipByIndex(0x16, 0x29)
    SetChrSubChip(0x16, 0x0)
    SetChrFlags(0x16, 0x8000)
    SetChrChipByIndex(0x17, 0x29)
    SetChrSubChip(0x17, 0x0)
    SetChrFlags(0x17, 0x8000)
    SetChrChipByIndex(0x18, 0x29)
    SetChrSubChip(0x18, 0x0)
    SetChrFlags(0x18, 0x8000)
    SetChrChipByIndex(0x19, 0x29)
    SetChrSubChip(0x19, 0x0)
    SetChrFlags(0x19, 0x8000)
    SetChrChipByIndex(0x1A, 0x1F)
    SetChrSubChip(0x1A, 0x0)
    SetChrFlags(0x1A, 0x20)
    SetChrFlags(0x1A, 0x8000)
    SetChrChipByIndex(0x1B, 0x1F)
    SetChrSubChip(0x1B, 0x0)
    SetChrFlags(0x1B, 0x20)
    SetChrFlags(0x1B, 0x8000)
    ClearChrFlags(0x1C, 0x80)
    OP_78(0x8, 0x1C)
    OP_49()
    ClearMapObjFlags(0x8, 0x4)
    SetMapObjFlags(0x8, 0x1000)
    SetMapObjFrame(0x8, "light", 0x0, 0x1)
    SetMapObjFrame(0x8, "patlight", 0x2, "highspd")
    ClearChrFlags(0x1D, 0x80)
    OP_78(0x9, 0x1D)
    OP_49()
    ClearMapObjFlags(0x9, 0x4)
    SetMapObjFlags(0x9, 0x1000)
    SetMapObjFrame(0x9, "light", 0x0, 0x1)
    SetMapObjFrame(0x9, "patlight", 0x2, "highspd")
    ClearChrFlags(0x1E, 0x80)
    OP_78(0xA, 0x1E)
    OP_49()
    SetMapObjFlags(0xA, 0x1000)
    ClearChrFlags(0x1F, 0x80)
    OP_78(0xB, 0x1F)
    OP_49()
    SetMapObjFlags(0xB, 0x1000)
    ClearMapObjFlags(0xD, 0x4)
    SetMapObjFlags(0xD, 0x1000)
    ClearMapObjFlags(0xE, 0x4)
    SetMapObjFlags(0xE, 0x1000)
    ClearMapObjFlags(0xF, 0x4)
    SetMapObjFlags(0xF, 0x1000)
    ClearMapObjFlags(0x10, 0x4)
    SetMapObjFlags(0x10, 0x1000)
    ClearMapObjFlags(0x11, 0x4)
    SetMapObjFlags(0x11, 0x1000)
    ClearMapObjFlags(0x12, 0x4)
    SetMapObjFlags(0x12, 0x1000)
    ClearMapObjFlags(0x13, 0x4)
    SetMapObjFlags(0x13, 0x1000)
    SetMapObjFlags(0x4, 0x4)
    SetMapObjFlags(0x5, 0x4)
    SetMapObjFlags(0x6, 0x4)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    SetChrPos(0x8, 16750, 0, 15050, 270)
    SetChrPos(0x9, 16450, 0, 12050, 270)
    SetChrPos(0xA, 16600, 0, 10800, 225)
    SetChrPos(0xB, 18250, 0, 8200, 225)
    SetChrPos(0xC, 18400, 0, 6900, 270)
    SetChrPos(0xE, 6200, 1770, 13150, 90)
    SetChrPos(0xF, 5850, 1120, 8350, 90)
    SetChrPos(0x10, 9350, 0, 3350, 45)
    SetChrPos(0x1C, 14750, 0, 13150, 190)
    OP_D5(0x1C, 0x0, 0x2E630, 0x0, 0x0)
    SetChrPos(0x1D, 15800, 0, 8150, 145)
    OP_D5(0x1D, 0x0, 0x4F588, 0x0, 0x0)
    SetChrPos(0x1E, 14750, 0, 12650, 200)
    OP_D5(0x1E, 0x0, 0x30D40, 0x0, 0x0)
    SetChrPos(0x1F, 15800, 0, 8150, 145)
    OP_D5(0x1F, 0x0, 0x4F588, 0x0, 0x0)
    OP_68(-2350, 9650, 32800, 0)
    MoveCamera(0, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(64000, 0)
    MoveCamera(10, 30, 0, 5000)
    SetCameraDistance(68000, 5000)
    Sound(868, 2, 50, 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    Fade(500)
    OP_82(0x32, 0x32, 0xBB8, 0x2710)
    Sound(865, 2, 80, 0)
    Sound(861, 2, 80, 0)
    BeginChrThread(0xE, 0, 0, 3)
    BeginChrThread(0xE, 3, 0, 5)
    BeginChrThread(0xF, 0, 0, 3)
    BeginChrThread(0xF, 3, 0, 5)
    BeginChrThread(0x10, 0, 0, 3)
    BeginChrThread(0x10, 3, 0, 5)
    BeginChrThread(0x8, 0, 0, 4)
    BeginChrThread(0x8, 3, 0, 5)
    BeginChrThread(0x9, 0, 0, 4)
    BeginChrThread(0x9, 3, 0, 5)
    BeginChrThread(0xA, 0, 0, 4)
    BeginChrThread(0xA, 3, 0, 5)
    BeginChrThread(0xB, 0, 0, 4)
    BeginChrThread(0xB, 3, 0, 5)
    BeginChrThread(0xC, 0, 0, 4)
    BeginChrThread(0xC, 3, 0, 5)
    BeginChrThread(0x20, 0, 0, 20)
    BeginChrThread(0x20, 3, 0, 5)
    PlayEffect(0x2, 0x0, 0xFF, 0x0, 16250, 0, 10550, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_68(10570, 1050, 8180, 0)
    MoveCamera(40, 30, 5, 0)
    OP_6E(800, 0)
    SetCameraDistance(14450, 0)
    SetCameraDistance(17500, 5000)
    OP_0D()
    OP_6F(0x79)
    OP_25(0x361, 0x14)
    OP_25(0x35D, 0x14)
    EndChrThread(0xE, 0x0)
    EndChrThread(0xE, 0x3)
    EndChrThread(0xF, 0x0)
    EndChrThread(0xF, 0x3)
    EndChrThread(0x10, 0x0)
    EndChrThread(0x10, 0x3)
    EndChrThread(0x8, 0x0)
    EndChrThread(0x8, 0x3)
    EndChrThread(0x9, 0x0)
    EndChrThread(0x9, 0x3)
    EndChrThread(0xA, 0x0)
    EndChrThread(0xA, 0x3)
    EndChrThread(0xB, 0x0)
    EndChrThread(0xB, 0x3)
    EndChrThread(0xC, 0x0)
    EndChrThread(0xC, 0x3)
    EndChrThread(0x20, 0x0)
    EndChrThread(0x20, 0x3)
    Fade(500)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    SetChrPos(0x11, -37250, 0, 11000, 90)
    SetChrPos(0x12, -38500, 0, 10000, 90)
    SetChrPos(0x13, -38750, 0, 12000, 90)
    SetChrPos(0x14, -39750, 0, 10000, 90)
    SetChrPos(0x15, -40000, 0, 12000, 90)
    SetChrPos(0x16, -42500, 0, 10000, 90)
    SetChrPos(0x17, -42750, 0, 12000, 90)
    SetChrPos(0x18, -43750, 0, 10000, 90)
    SetChrPos(0x19, -44000, 0, 12000, 90)
    SetChrPos(0x1A, -34250, 0, 12000, 90)
    SetChrPos(0x1B, -34750, 0, 10000, 90)
    OP_68(-30600, 1000, 11000, 0)
    MoveCamera(315, 35, 5, 0)
    OP_6E(500, 0)
    SetCameraDistance(16000, 0)
    OP_68(-20600, 1000, 11000, 3000)
    MoveCamera(325, 20, 5, 3000)
    OP_6E(500, 3000)
    SetCameraDistance(17000, 3000)
    BeginChrThread(0x20, 1, 0, 19)
    BeginChrThread(0x1A, 3, 0, 7)

    def lambda_D9D():
        OP_9B(0x0, 0xFE, 0x0, 0x61A8, 0x1BBC, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_D9D)
    Sleep(50)
    BeginChrThread(0x1B, 3, 0, 7)

    def lambda_DBB():
        OP_9B(0x0, 0xFE, 0x0, 0x61A8, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_DBB)

    def lambda_DD0():
        OP_9B(0x0, 0xFE, 0x0, 0x61A8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_DD0)
    Sleep(50)

    def lambda_DE8():
        OP_9B(0x0, 0xFE, 0x0, 0x61A8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_DE8)
    Sleep(50)

    def lambda_E00():
        OP_9B(0x0, 0xFE, 0x0, 0x61A8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_E00)
    Sleep(50)

    def lambda_E18():
        OP_9B(0x0, 0xFE, 0x0, 0x61A8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_E18)
    Sleep(50)

    def lambda_E30():
        OP_9B(0x0, 0xFE, 0x0, 0x61A8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_E30)
    Sleep(50)

    def lambda_E48():
        OP_9B(0x0, 0xFE, 0x0, 0x61A8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_E48)
    Sleep(50)

    def lambda_E60():
        OP_9B(0x0, 0xFE, 0x0, 0x61A8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_E60)
    Sleep(50)

    def lambda_E78():
        OP_9B(0x0, 0xFE, 0x0, 0x61A8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_E78)
    Sleep(50)

    def lambda_E90():
        OP_9B(0x0, 0xFE, 0x0, 0x61A8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_E90)
    OP_0D()
    OP_6F(0x79)
    EndChrThread(0x11, 0x1)
    EndChrThread(0x12, 0x1)
    EndChrThread(0x13, 0x1)
    EndChrThread(0x14, 0x1)
    EndChrThread(0x15, 0x1)
    EndChrThread(0x16, 0x1)
    EndChrThread(0x17, 0x1)
    EndChrThread(0x18, 0x1)
    EndChrThread(0x19, 0x1)
    EndChrThread(0x20, 0x1)
    EndChrThread(0x1A, 0x1)
    EndChrThread(0x1A, 0x3)
    EndChrThread(0x1B, 0x1)
    EndChrThread(0x1B, 0x3)
    Fade(500)
    SetChrPos(0x1A, 4950, 1770, 11400, 90)
    SetChrPos(0x1B, 10100, 0, 1050, 45)
    OP_25(0x361, 0x32)
    OP_25(0x35D, 0x32)
    BeginChrThread(0xE, 0, 0, 3)
    BeginChrThread(0xE, 3, 0, 5)
    BeginChrThread(0xF, 0, 0, 3)
    BeginChrThread(0xF, 3, 0, 5)
    BeginChrThread(0x10, 0, 0, 3)
    BeginChrThread(0x10, 3, 0, 5)
    BeginChrThread(0x8, 0, 0, 4)
    BeginChrThread(0x8, 3, 0, 5)
    BeginChrThread(0x9, 0, 0, 4)
    BeginChrThread(0x9, 3, 0, 5)
    BeginChrThread(0xA, 0, 0, 4)
    BeginChrThread(0xA, 3, 0, 5)
    BeginChrThread(0xB, 0, 0, 4)
    BeginChrThread(0xB, 3, 0, 5)
    BeginChrThread(0xC, 0, 0, 4)
    BeginChrThread(0xC, 3, 0, 5)
    BeginChrThread(0x20, 0, 0, 20)
    BeginChrThread(0x20, 3, 0, 5)
    OP_68(10000, 1000, 7350, 0)
    MoveCamera(50, 25, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(15000, 0)
    OP_68(17300, 1000, 10600, 2500)
    MoveCamera(45, 30, -5, 2500)
    SetCameraDistance(13750, 3500)
    OP_25(0x361, 0x28)
    OP_25(0x35D, 0x1E)
    BeginChrThread(0x1A, 1, 0, 9)
    BeginChrThread(0x1B, 1, 0, 11)
    Sleep(300)
    StopSound(865, 1000, 20)
    StopSound(861, 1000, 20)
    StopEffect(0x0, 0x2)
    EndChrThread(0xE, 0x0)
    EndChrThread(0xE, 0x3)
    EndChrThread(0xF, 0x0)
    EndChrThread(0xF, 0x3)
    EndChrThread(0x10, 0x0)
    EndChrThread(0x10, 0x3)
    WaitChrThread(0x1A, 1)
    WaitChrThread(0x1B, 1)
    Sleep(500)
    OP_0D()
    OP_6F(0x79)
    Fade(500)
    SetChrChipByIndex(0xE, 0x2A)
    SetChrSubChip(0xE, 0x0)
    SetChrChipByIndex(0x10, 0x31)
    SetChrSubChip(0x10, 0x1)
    SetChrChipByIndex(0x11, 0x31)
    SetChrSubChip(0x11, 0x1)
    SetChrPos(0x10, 0, 1760, 12150, 90)
    SetChrPos(0x11, -2250, 1760, 10150, 90)
    SetChrPos(0x12, 9560, 0, 2160, 45)
    SetChrPos(0x13, 9040, 0, 2420, 45)
    SetChrPos(0x14, 9560, 0, 2160, 45)
    SetChrPos(0x15, 9040, 0, 2420, 45)
    SetChrPos(0x16, 9560, 0, 2160, 45)
    SetChrPos(0x17, 9040, 0, 2420, 45)
    SetChrPos(0x18, 9560, 0, 2160, 45)
    SetChrPos(0x19, 9040, 0, 2420, 45)
    OP_68(10920, 1150, 11900, 0)
    MoveCamera(34, 31, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(20050, 0)
    OP_0D()
    Sound(947, 0, 100, 0)
    SetChrChipByIndex(0xE, 0x2B)
    SetChrSubChip(0xE, 0x0)
    Sleep(300)
    BeginChrThread(0x1A, 1, 0, 10)
    BeginChrThread(0x1B, 1, 0, 12)
    Sleep(500)

    def lambda_1130():
        TurnDirection(0xFE, 0xE, 1000)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_1130)
    OP_64(0x8)
    OP_63(0x8, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)

    def lambda_115B():
        TurnDirection(0xFE, 0xE, 1000)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_115B)
    OP_64(0x9)
    OP_63(0x9, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_68(-1300, 2700, 10950, 3000)
    MoveCamera(60, 38, 5, 3000)
    SetCameraDistance(15000, 3000)
    Sleep(2700)
    Sleep(50)
    Sleep(500)

    def lambda_11B1():
        OP_A0(0xFE, 1500, 0x2, 0x4)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_11B1)
    Sound(545, 0, 100, 0)
    PlayEffect(0x4, 0x0, 0x10, 0x3, 0, 800, 500, 0, 0, 0, 1000, 1000, 1000, 0x1C, 500, 0, 500, 0)
    Sleep(50)

    def lambda_11FE():
        OP_A0(0xFE, 1500, 0x2, 0x4)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_11FE)
    PlayEffect(0x4, 0x1, 0x11, 0x3, 0, 800, 500, 0, 0, 0, 1000, 1000, 1000, 0x1D, -500, 0, -500, 0)
    OP_68(14550, 1550, 10350, 500)
    MoveCamera(60, 30, 5, 500)
    Sleep(500)
    Fade(250)
    SetMapObjFlags(0x8, 0x4)
    ClearMapObjFlags(0xA, 0x4)
    OP_71(0xA, 0x1, 0x3C, 0x0, 0x8)
    OP_82(0x3E8, 0x0, 0xBB8, 0x3E8)
    Sound(200, 0, 100, 0)
    Sound(196, 0, 50, 0)
    MoveCamera(64, 30, 0, 500)
    SetCameraDistance(23050, 500)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0xA)
    CancelBlur(1000)
    BeginChrThread(0x8, 1, 0, 13)
    BeginChrThread(0x9, 1, 0, 14)
    BeginChrThread(0xA, 1, 0, 15)
    Sleep(50)
    Fade(250)
    SetMapObjFlags(0x9, 0x4)
    ClearMapObjFlags(0xB, 0x4)
    OP_71(0xB, 0x1, 0x3C, 0x0, 0x8)

    def lambda_12F2():
        OP_96(0xFE, 0x3FAC, 0x0, 0x19FA, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_12F2)

    def lambda_130C():
        OP_D5(0xFE, 0x0, 0x445C0, 0x0, 0x32)
        ExitThread()

    QueueWorkItem(0x1F, 2, lambda_130C)
    OP_79(0xA)
    OP_71(0xA, 0x3D, 0x78, 0x0, 0x20)
    OP_79(0xB)
    OP_71(0xB, 0x3D, 0x78, 0x0, 0x20)
    OP_0D()
    WaitChrThread(0x1D, 1)
    WaitChrThread(0x1D, 2)
    WaitChrThread(0x8, 1)
    WaitChrThread(0x9, 1)
    WaitChrThread(0xA, 1)
    OP_68(12110, 1550, 11560, 1500)
    MoveCamera(67, 31, 0, 1500)
    SetCameraDistance(23050, 1500)
    OP_6F(0x79)
    Sound(802, 0, 100, 0)
    SetChrChipByIndex(0xE, 0x2B)
    SetChrSubChip(0xE, 0x3)
    Sleep(300)
    SetChrSubChip(0xE, 0x4)
    OP_68(14600, 1150, 11240, 5000)
    MoveCamera(67, 25, 0, 5000)
    SetChrPos(0x11, 9040, 0, 2420, 45)
    SetChrChipByIndex(0x11, 0x2E)
    SetChrSubChip(0x11, 0x0)
    BeginChrThread(0xE, 0, 0, 18)
    Sleep(2000)
    FadeToDark(2000, 0, -1)
    Sleep(1000)
    StopSound(868, 1000, 40)
    OP_0D()
    SetScenarioFlags(0x22, 0)
    NewScene("c110B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_2_60D end

    def Function_3_13EE(): pass

    label("Function_3_13EE")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_143D")
    PlayEffect(0x0, 0xFF, 0xFE, 0x3, 100, 950, 1700, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    OP_A1(0xFE, 0xBB8, 0x2, 0x2, 0x1)
    Jump("Function_3_13EE")

    label("loc_143D")

    Return()

    # Function_3_13EE end

    def Function_4_143E(): pass

    label("Function_4_143E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1496")
    PlayEffect(0x0, 0xFF, 0xFE, 0x3, 0, 1100, 1100, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0xFE, 0x1)
    Sleep(500)
    SetChrSubChip(0xFE, 0x0)
    Sleep(700)
    Call(0, 6)
    Jump("Function_4_143E")

    label("loc_1496")

    Return()

    # Function_4_143E end

    def Function_5_1497(): pass

    label("Function_5_1497")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_14CA")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x50), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_14BE")
    OP_4C(0xFE, 0x0)
    Jump("loc_14C2")

    label("loc_14BE")

    OP_4B(0xFE, 0x0)

    label("loc_14C2")

    Sleep(500)
    Jump("Function_5_1497")

    label("loc_14CA")

    Return()

    # Function_5_1497 end

    def Function_6_14CB(): pass

    label("Function_6_14CB")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_1509"),
        (1, "loc_1545"),
        (2, "loc_1581"),
        (3, "loc_15BD"),
        (4, "loc_15F9"),
        (5, "loc_1635"),
        (6, "loc_1671"),
        (7, "loc_16AD"),
        (SWITCH_DEFAULT, "loc_16E9"),
    )


    label("loc_1509")

    PlayEffect(0x1, 0xFF, 0xE, 0x3, 0, 0, 800, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Jump("loc_1725")

    label("loc_1545")

    PlayEffect(0x1, 0xFF, 0xE, 0x3, 800, 0, -800, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Jump("loc_1725")

    label("loc_1581")

    PlayEffect(0x1, 0xFF, 0xE, 0x3, -800, 0, -800, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Jump("loc_1725")

    label("loc_15BD")

    PlayEffect(0x1, 0xFF, 0xF, 0x3, 0, 0, 800, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Jump("loc_1725")

    label("loc_15F9")

    PlayEffect(0x1, 0xFF, 0xF, 0x3, 800, 0, -800, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Jump("loc_1725")

    label("loc_1635")

    PlayEffect(0x1, 0xFF, 0xF, 0x3, -800, 0, -800, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Jump("loc_1725")

    label("loc_1671")

    PlayEffect(0x1, 0xFF, 0x10, 0x3, 0, 0, 800, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Jump("loc_1725")

    label("loc_16AD")

    PlayEffect(0x1, 0xFF, 0x10, 0x3, 800, 0, -800, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Jump("loc_1725")

    label("loc_16E9")

    PlayEffect(0x1, 0xFF, 0x10, 0x3, -800, 0, -800, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Jump("loc_1725")

    label("loc_1725")

    Return()

    # Function_6_14CB end

    def Function_7_1726(): pass

    label("Function_7_1726")

    SetChrChipByIndex(0xFE, 0x1F)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_1778"),
        (1, "loc_1784"),
        (2, "loc_1790"),
        (3, "loc_179C"),
        (4, "loc_17A8"),
        (5, "loc_17B4"),
        (6, "loc_17C0"),
        (SWITCH_DEFAULT, "loc_17CC"),
    )


    label("loc_1778")

    OP_A0(0xFE, 1200, 0x0, 0x7)
    Jump("loc_17D8")

    label("loc_1784")

    OP_A0(0xFE, 1300, 0x0, 0x7)
    Jump("loc_17D8")

    label("loc_1790")

    OP_A0(0xFE, 1400, 0x0, 0x7)
    Jump("loc_17D8")

    label("loc_179C")

    OP_A0(0xFE, 1500, 0x0, 0x7)
    Jump("loc_17D8")

    label("loc_17A8")

    OP_A0(0xFE, 1600, 0x0, 0x7)
    Jump("loc_17D8")

    label("loc_17B4")

    OP_A0(0xFE, 1700, 0x0, 0x7)
    Jump("loc_17D8")

    label("loc_17C0")

    OP_A0(0xFE, 1800, 0x0, 0x7)
    Jump("loc_17D8")

    label("loc_17CC")

    OP_A0(0xFE, 1500, 0x0, 0x7)
    Jump("loc_17D8")

    label("loc_17D8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_17EF")
    OP_A0(0xFE, 1500, 0x0, 0x7)
    Jump("loc_17D8")

    label("loc_17EF")

    Return()

    # Function_7_1726 end

    def Function_8_17F0(): pass

    label("Function_8_17F0")

    SetChrChipByIndex(0xFE, 0x1E)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_180A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1821")
    OP_A0(0xFE, 1500, 0x0, 0x7)
    Jump("loc_180A")

    label("loc_1821")

    Return()

    # Function_8_17F0 end

    def Function_9_1822(): pass

    label("Function_9_1822")

    BeginChrThread(0x20, 1, 0, 19)
    BeginChrThread(0xFE, 0, 0, 7)
    ClearChrFlags(0xFE, 0x4)
    OP_95(0xFE, 11400, 0, 9450, 7000, 0x0)
    SetChrFlags(0xFE, 0x4)
    EndChrThread(0xFE, 0x0)
    EndChrThread(0x20, 0x1)
    SetChrSubChip(0xFE, 0x5)
    Sound(809, 0, 100, 0)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_9D(0xFE, 0x3A98, 0x3E8, 0x251C, 0x4E2, 0x1B58)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrSubChip(0xFE, 0x1)
    Sleep(50)
    SetChrSubChip(0xFE, 0x5)
    Sound(809, 0, 100, 0)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_9D(0xFE, 0x4C2C, 0x0, 0x2B8E, 0x1F4, 0x1B58)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrSubChip(0xFE, 0x1)
    OP_93(0xFE, 0x10E, 0x1F4)
    BeginChrThread(0xFE, 0, 0, 8)
    EndChrThread(0x8, 0x0)
    EndChrThread(0x8, 0x3)
    EndChrThread(0x9, 0x0)
    EndChrThread(0x9, 0x3)
    EndChrThread(0xA, 0x0)
    EndChrThread(0xA, 0x3)
    EndChrThread(0x20, 0x0)
    EndChrThread(0x20, 0x3)

    def lambda_18FF():
        TurnDirection(0x8, 0x1A, 1500)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_18FF)
    Sleep(50)

    def lambda_190F():
        TurnDirection(0x9, 0x1A, 1500)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_190F)
    Sleep(50)

    def lambda_191F():
        TurnDirection(0xA, 0x1A, 1500)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_191F)
    Sleep(50)
    WaitChrThread(0x8, 0)
    WaitChrThread(0x9, 0)
    WaitChrThread(0xA, 0)
    OP_63(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sound(948, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x20)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_197F():
        OP_A0(0xFE, 2000, 0x0, 0x5)
        ExitThread()

    QueueWorkItem(0xFE, 0, lambda_197F)
    OP_9B(0x1, 0xFE, 0x0, 0x7D0, 0x2710, 0x0)
    OP_82(0x64, 0x0, 0xBB8, 0x1F4)
    Sound(501, 0, 100, 0)
    PlayEffect(0x3, 0xFF, 0xA, 0x1, 0, 1000, 0, 0, 0, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)
    SetChrChipByIndex(0xA, 0x24)
    SetChrSubChip(0xA, 0x0)

    def lambda_19F1():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0x1388)
        ExitThread()

    QueueWorkItem(0xA, 3, lambda_19F1)
    OP_9B(0x1, 0xA, 0x0, 0xFFFFFE0C, 0x2710, 0x0)
    Sound(514, 0, 100, 0)
    SetChrChipByIndex(0xA, 0x25)
    SetChrSubChip(0xA, 0x0)
    Sleep(500)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sound(809, 0, 100, 0)
    OP_9D(0xFE, 0x4C2C, 0x0, 0x2B8E, 0x1F4, 0x1B58)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xFE, 0, 0, 8)
    Return()

    # Function_9_1822 end

    def Function_10_1A5F(): pass

    label("Function_10_1A5F")

    BeginChrThread(0x20, 1, 0, 19)
    BeginChrThread(0xFE, 0, 0, 7)
    OP_95(0xFE, 17750, 0, 11650, 7000, 0x0)
    EndChrThread(0xFE, 0x0)
    EndChrThread(0x20, 0x1)
    SetChrSubChip(0xFE, 0x5)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sound(809, 0, 100, 0)
    OP_9D(0xFE, 0x37DC, 0x3E8, 0x2C24, 0x4E2, 0x1B58)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrSubChip(0xFE, 0x1)
    SetChrSubChip(0xFE, 0x5)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sound(809, 0, 100, 0)
    OP_9D(0xFE, 0x29FE, 0x2D0, 0x32FA, 0x4E2, 0x1B58)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrSubChip(0xFE, 0x1)
    BeginChrThread(0xFE, 0, 0, 8)
    Sleep(300)
    BeginChrThread(0x20, 1, 0, 19)
    BeginChrThread(0xFE, 0, 0, 7)
    ClearChrFlags(0xFE, 0x4)
    OP_95(0xFE, -12200, 1990, 19850, 7000, 0x0)
    SetChrFlags(0xFE, 0x4)
    EndChrThread(0xFE, 0x0)
    EndChrThread(0x20, 0x1)
    Return()

    # Function_10_1A5F end

    def Function_11_1B39(): pass

    label("Function_11_1B39")

    BeginChrThread(0xFE, 0, 0, 7)
    OP_95(0xFE, 13450, 0, 4350, 7000, 0x0)
    EndChrThread(0xFE, 0x0)
    SetChrSubChip(0xFE, 0x5)
    Sound(809, 0, 100, 0)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_9D(0xFE, 0x410A, 0x3E8, 0x1932, 0x4E2, 0x1B58)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrSubChip(0xFE, 0x1)
    EndChrThread(0xB, 0x0)
    EndChrThread(0xB, 0x3)
    EndChrThread(0xC, 0x0)
    EndChrThread(0xC, 0x3)

    def lambda_1BA7():
        TurnDirection(0xB, 0x1B, 500)
        ExitThread()

    QueueWorkItem(0xB, 0, lambda_1BA7)
    Sleep(50)

    def lambda_1BB7():
        TurnDirection(0xC, 0x1B, 500)
        ExitThread()

    QueueWorkItem(0xC, 0, lambda_1BB7)
    Sleep(50)
    WaitChrThread(0xB, 0)
    WaitChrThread(0xC, 0)
    SetChrChipByIndex(0xFE, 0x20)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_1BE9():
        OP_A0(0xFE, 2000, 0x0, 0x5)
        ExitThread()

    QueueWorkItem(0xFE, 0, lambda_1BE9)
    OP_9B(0x1, 0xFE, 0x0, 0x3E8, 0x2710, 0x0)
    OP_82(0x64, 0x0, 0xBB8, 0x1F4)
    Sound(501, 0, 100, 0)
    PlayEffect(0x3, 0xFF, 0xB, 0x1, 0, 1000, 0, 0, 0, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0xFF, 0xC, 0x1, 0, 1000, 0, 0, 0, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)
    SetChrChipByIndex(0xB, 0x24)
    SetChrSubChip(0xB, 0x0)
    SetChrChipByIndex(0xC, 0x24)
    SetChrSubChip(0xC, 0x0)

    def lambda_1C9A():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0x1388)
        ExitThread()

    QueueWorkItem(0xB, 3, lambda_1C9A)

    def lambda_1CB3():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0x1388)
        ExitThread()

    QueueWorkItem(0xC, 3, lambda_1CB3)

    def lambda_1CCC():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFA24, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1CCC)

    def lambda_1CE1():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFA24, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_1CE1)
    WaitChrThread(0xB, 1)
    Sound(514, 0, 100, 0)
    SetChrChipByIndex(0xB, 0x25)
    SetChrSubChip(0xB, 0x0)
    WaitChrThread(0xC, 1)
    SetChrChipByIndex(0xC, 0x25)
    SetChrSubChip(0xC, 0x0)
    Sleep(500)
    OP_9B(0x1, 0xFE, 0x0, 0xFFFFFC18, 0x2710, 0x0)
    BeginChrThread(0xFE, 0, 0, 8)
    Return()

    # Function_11_1B39 end

    def Function_12_1D28(): pass

    label("Function_12_1D28")

    BeginChrThread(0xFE, 0, 0, 7)
    OP_95(0xFE, 15600, 1250, 7900, 7000, 0x0)
    EndChrThread(0xFE, 0x0)
    SetChrSubChip(0xFE, 0x5)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sound(809, 0, 100, 0)
    OP_9D(0xFE, 0x2FDA, 0x0, 0x251C, 0x4E2, 0x1B58)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrSubChip(0xFE, 0x1)
    BeginChrThread(0xFE, 0, 0, 8)
    Sleep(300)
    BeginChrThread(0xFE, 0, 0, 7)
    ClearChrFlags(0xFE, 0x4)
    OP_95(0xFE, -12300, 1850, 17450, 7000, 0x0)
    SetChrFlags(0xFE, 0x4)
    EndChrThread(0xFE, 0x0)
    Return()

    # Function_12_1D28 end

    def Function_13_1DB3(): pass

    label("Function_13_1DB3")

    SetChrChipByIndex(0xFE, 0x24)
    SetChrSubChip(0xFE, 0x0)

    def lambda_1DC0():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_1DC0)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sound(251, 0, 100, 0)
    Sound(871, 0, 60, 0)
    OP_9D(0xFE, 0x4DBC, 0x0, 0x380E, 0x3E8, 0x1388)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sound(514, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x25)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_13_1DB3 end

    def Function_14_1E1C(): pass

    label("Function_14_1E1C")

    SetChrChipByIndex(0xFE, 0x24)
    SetChrSubChip(0xFE, 0x0)

    def lambda_1E29():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_1E29)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_9D(0xFE, 0x4E52, 0x0, 0x2F12, 0x3E8, 0x1388)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xFE, 0x25)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_14_1E1C end

    def Function_15_1E73(): pass

    label("Function_15_1E73")

    OP_93(0xFE, 0x10E, 0x0)
    SetChrChipByIndex(0xFE, 0x24)
    SetChrSubChip(0xFE, 0x0)

    def lambda_1E87():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_1E87)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_9D(0xFE, 0x461E, 0x0, 0x2292, 0x3E8, 0x1388)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xFE, 0x25)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_15_1E73 end

    def Function_16_1ED1(): pass

    label("Function_16_1ED1")

    OP_95(0xFE, 14400, 0, 9890, 5000, 0x0)
    OP_95(0xFE, 18230, 0, 11270, 5000, 0x0)
    OP_95(0xFE, 31300, 0, 11050, 5000, 0x0)
    Return()

    # Function_16_1ED1 end

    def Function_17_1F0E(): pass

    label("Function_17_1F0E")

    OP_95(0xFE, 14940, 0, 9340, 5000, 0x0)
    OP_95(0xFE, 17860, 0, 10450, 5000, 0x0)
    OP_95(0xFE, 35020, 0, 9440, 5000, 0x0)
    Return()

    # Function_17_1F0E end

    def Function_18_1F4B(): pass

    label("Function_18_1F4B")

    BeginChrThread(0x11, 1, 0, 16)
    Sleep(500)
    BeginChrThread(0x12, 1, 0, 17)
    Sleep(500)
    BeginChrThread(0x13, 1, 0, 16)
    Sleep(500)
    BeginChrThread(0x14, 1, 0, 17)
    Sleep(500)
    BeginChrThread(0x15, 1, 0, 16)
    Sleep(500)
    BeginChrThread(0x16, 1, 0, 17)
    Sleep(500)
    BeginChrThread(0x17, 1, 0, 16)
    Sleep(500)
    BeginChrThread(0x18, 1, 0, 17)
    Sleep(500)
    BeginChrThread(0x19, 1, 0, 16)
    Return()

    # Function_18_1F4B end

    def Function_19_1F9A(): pass

    label("Function_19_1F9A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1FB3")
    Sound(845, 0, 100, 0)
    Sleep(440)
    Jump("Function_19_1F9A")

    label("loc_1FB3")

    Return()

    # Function_19_1F9A end

    def Function_20_1FB4(): pass

    label("Function_20_1FB4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1FD0")
    Sound(530, 0, 50, 0)
    Sleep(500)
    Sleep(700)
    Jump("Function_20_1FB4")

    label("loc_1FD0")

    Return()

    # Function_20_1FB4 end

    SaveToFile()

Try(main)
