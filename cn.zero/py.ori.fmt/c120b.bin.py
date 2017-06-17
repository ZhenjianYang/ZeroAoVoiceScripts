from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "c120b.bin",                # FileName
        "c120b",                    # MapName
        "c120b",                    # Location
        0x001A,                     # MapIndex
        "ed7100",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x1D,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 26, 0, 0, 0, 1],
    )

    BuildStringList((
        "c120b",                  # 0
        "警备队员",               # 1
        "警备队员",               # 2
        "警备队员",               # 3
        "警备队员",               # 4
        "警备队员",               # 5
        "瓦吉",                   # 6
        "瓦鲁多",                 # 7
        "阿巴斯",                 # 8
        "蓝衣青年",               # 9
        "蓝衣青年",               # 10
        "蓝衣青年",               # 11
        "蓝衣青年",               # 12
        "红衣青年",               # 13
        "红衣青年",               # 14
        "红衣青年",               # 15
        "红衣青年",               # 16
        "红衣青年",               # 17
        "车１",                   # 18
        "假",                     # 19
        "假",                     # 20
        "假",                     # 21
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
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    PlaceName(-123.13999938964844, 0.0, -85.1500015258789, 0x0000, 0x0000, "中央广场")
    PlaceName(-209.27000427246094, 0.0, -79.26000213623047, 0x0000, 0x0000, "西街")
    PlaceName(-87.7699966430664, 0.0, 31.440000534057617, 0x0000, 0x0000, "行政区")
    PlaceName(-289.17999267578125, 0.0, 18.34000015258789, 0x0000, 0x0000, "住宅街")
    PlaceName(-193.5500030517578, 0.0, 7.860000133514404, 0x0000, 0x0000, "欢乐街")
    PlaceName(-16.700000762939453, 0.0, -115.27999877929688, 0x0000, 0x0000, "东街")
    PlaceName(29.799999237060547, 0.0, -187.3300018310547, 0x0000, 0x0000, "旧城区")
    PlaceName(19.979999542236328, 0.0, -28.81999969482422, 0x0000, 0x0000, "港湾区")
    PlaceName(-14.079999923706055, 0.0, 94.31999969482422, 0x0000, 0x0000, "ＩＢＣ")
    PlaceName(-108.4000015258789, 0.0, -175.5399932861328, 0x0000, 0x0000, "站前街道")
    PlaceName(-169.97000122070312, 0.0, -39.29999923706055, 0x0000, 0x0000, "后巷")
    PlaceName(-112.33000183105469, 0.0, -216.14999389648438, 0x0000, 0x0000, "乌尔斯拉间道")
    PlaceName(54.040000915527344, 0.0, -96.94000244140625, 0x0000, 0x0000, "东克洛斯贝尔街道")
    PlaceName(-276.0799865722656, 0.0, -81.22000122070312, 0x0000, 0x0000, "西克洛斯贝尔街道")
    PlaceName(-268.2200012207031, 0.0, 49.779998779296875, 0x0000, 0x0000, "玛因兹山道")
    PlaceName(-151.9600067138672, 0.0, -103.48999786376953, 0x0000, 0x0051, "")
    PlaceName(-81.55000305175781, 0.0, -69.43000030517578, 0x0000, 0x0054, "")
    PlaceName(-119.87000274658203, 0.0, -113.97000122070312, 0x0000, 0x0057, "")
    PlaceName(-152.94000244140625, 0.0, -65.5, 0x0000, 0x0053, "")
    PlaceName(-126.08999633789062, 0.0, -34.060001373291016, 0x0000, 0x0053, "")
    PlaceName(-192.57000732421875, 0.0, -72.05000305175781, 0x0000, 0x0053, "")
    PlaceName(-205.33999633789062, 0.0, -44.540000915527344, 0x0000, 0x0053, "")
    PlaceName(-173.89999389648438, 0.0, -2.619999885559082, 0x0000, 0x0052, "")
    PlaceName(-167.67999267578125, 0.0, -19.649999618530273, 0x0000, 0x0053, "")
    PlaceName(-156.22000122070312, 0.0, -30.790000915527344, 0x0000, 0x0053, "")
    PlaceName(-118.87999725341797, 0.0, 62.22999954223633, 0x0000, 0x0051, "")
    PlaceName(27.84000015258789, 0.0, -115.27999877929688, 0x0000, 0x0052, "")
    PlaceName(5.570000171661377, 0.0, -233.83999633789062, 0x0000, 0x0053, "")
    PlaceName(-11.460000038146973, 0.0, -209.60000610351562, 0x0000, 0x0053, "")

    ScpFunction((
        "Function_0_5C0",          # 00, 0
        "Function_1_5F8",          # 01, 1
        "Function_2_5F9",          # 02, 2
        "Function_3_6ED",          # 03, 3
        "Function_4_7E1",          # 04, 4
        "Function_5_143F",         # 05, 5
        "Function_6_1B57",         # 06, 6
        "Function_7_211E",         # 07, 7
        "Function_8_297D",         # 08, 8
        "Function_9_2AF8",         # 09, 9
        "Function_10_2BB9",        # 0A, 10
        "Function_11_2D4E",        # 0B, 11
        "Function_12_2E26",        # 0C, 12
        "Function_13_2EC7",        # 0D, 13
        "Function_14_317A",        # 0E, 14
        "Function_15_330A",        # 0F, 15
        "Function_16_3358",        # 10, 16
        "Function_17_34AE",        # 11, 17
        "Function_18_3656",        # 12, 18
        "Function_19_38F8",        # 13, 19
        "Function_20_3B17",        # 14, 20
        "Function_21_3C60",        # 15, 21
        "Function_22_3D66",        # 16, 22
        "Function_23_3E14",        # 17, 23
        "Function_24_3EBC",        # 18, 24
        "Function_25_3F62",        # 19, 25
        "Function_26_4008",        # 1A, 26
        "Function_27_40AE",        # 1B, 27
        "Function_28_4154",        # 1C, 28
        "Function_29_41FA",        # 1D, 29
        "Function_30_4220",        # 1E, 30
        "Function_31_424F",        # 1F, 31
        "Function_32_4281",        # 20, 32
        "Function_33_42BA",        # 21, 33
        "Function_34_42F3",        # 22, 34
        "Function_35_432B",        # 23, 35
        "Function_36_435A",        # 24, 36
        "Function_37_4393",        # 25, 37
        "Function_38_43CC",        # 26, 38
    ))


    def Function_0_5C0(): pass

    label("Function_0_5C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_5D4")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 2)
    Jump("loc_5F7")

    label("loc_5D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 1)), scpexpr(EXPR_END)), "loc_5E8")
    ClearScenarioFlags(0x5C, 1)
    Event(0, 3)
    Jump("loc_5F7")

    label("loc_5E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 2)), scpexpr(EXPR_END)), "loc_5F7")
    ClearScenarioFlags(0x5C, 2)
    Event(0, 4)

    label("loc_5F7")

    Return()

    # Function_0_5C0 end

    def Function_1_5F8(): pass

    label("Function_1_5F8")

    Return()

    # Function_1_5F8 end

    def Function_2_5F9(): pass

    label("Function_2_5F9")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-1600, 2500, 5600, 0)
    MoveCamera(55, 5, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(29000, 0)
    SetChrPos(0x0, -19600, 0, -28000, 0)
    SetChrPos(0x1, -19600, 0, -28000, 0)
    SetChrPos(0x2, -19600, 0, -28000, 0)
    SetChrPos(0x3, -19600, 0, -28000, 0)
    OP_68(-1600, 1500, 5600, 5000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x1)
    Fade(1000)
    OP_68(22140, 2500, 20700, 0)
    MoveCamera(35, 20, 0, 0)
    OP_6E(660, 0)
    SetCameraDistance(25000, 0)
    SetCameraDistance(21000, 4000)
    Sleep(3000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    SetScenarioFlags(0x5C, 0)
    NewScene("c121B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_2_5F9 end

    def Function_3_6ED(): pass

    label("Function_3_6ED")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-1600, 2500, 5600, 0)
    MoveCamera(55, 5, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(29000, 0)
    SetChrPos(0x0, -19600, 0, -28000, 0)
    SetChrPos(0x1, -19600, 0, -28000, 0)
    SetChrPos(0x2, -19600, 0, -28000, 0)
    SetChrPos(0x3, -19600, 0, -28000, 0)
    OP_68(-1600, 1500, 5600, 5000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x1)
    Fade(1000)
    OP_68(22140, 2500, 20700, 0)
    MoveCamera(35, 20, 0, 0)
    OP_6E(660, 0)
    SetCameraDistance(25000, 0)
    SetCameraDistance(21000, 4000)
    Sleep(3000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    SetScenarioFlags(0x5C, 1)
    NewScene("c121B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_3_6ED end

    def Function_4_7E1(): pass

    label("Function_4_7E1")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch31250.itc", 0x14)
    LoadChrToIndex("chr/ch31251.itc", 0x15)
    LoadChrToIndex("chr/ch31252.itc", 0x16)
    LoadChrToIndex("chr/ch31253.itc", 0x17)
    LoadChrToIndex("chr/ch31350.itc", 0x18)
    LoadChrToIndex("chr/ch31351.itc", 0x19)
    LoadChrToIndex("chr/ch31352.itc", 0x1A)
    LoadChrToIndex("chr/ch31353.itc", 0x1B)
    LoadChrToIndex("chr/ch30850.itc", 0x1C)
    LoadChrToIndex("chr/ch30851.itc", 0x1D)
    LoadChrToIndex("chr/ch30852.itc", 0x1E)
    LoadChrToIndex("chr/ch30950.itc", 0x1F)
    LoadChrToIndex("chr/ch30951.itc", 0x20)
    LoadChrToIndex("chr/ch30952.itc", 0x21)
    LoadChrToIndex("chr/ch31750.itc", 0x22)
    LoadChrToIndex("chr/ch31751.itc", 0x23)
    LoadChrToIndex("chr/ch31752.itc", 0x24)
    LoadChrToIndex("chr/ch31850.itc", 0x25)
    LoadChrToIndex("chr/ch31851.itc", 0x26)
    LoadChrToIndex("chr/ch31852.itc", 0x27)
    LoadChrToIndex("chr/ch00400.itc", 0x28)
    LoadChrToIndex("chr/ch00450.itc", 0x29)
    LoadChrToIndex("chr/ch00451.itc", 0x2A)
    LoadChrToIndex("chr/ch00452.itc", 0x2B)
    LoadChrToIndex("chr/ch00456.itc", 0x2C)
    LoadChrToIndex("chr/ch00457.itc", 0x2D)
    LoadChrToIndex("chr/ch02150.itc", 0x2E)
    LoadChrToIndex("chr/ch02151.itc", 0x2F)
    LoadChrToIndex("chr/ch02151.itc", 0x30)
    LoadChrToIndex("chr/ch02152.itc", 0x31)
    LoadChrToIndex("chr/ch02154.itc", 0x32)
    LoadChrToIndex("chr/ch06700.itc", 0x33)
    LoadChrToIndex("chr/ch30953.itc", 0x34)
    LoadChrToIndex("chr/ch30853.itc", 0x35)
    LoadChrToIndex("chr/ch31753.itc", 0x36)
    OP_68(-7000, 1000, 14000, 0)
    MoveCamera(30, 35, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(23000, 0)
    SetChrFlags(0x101, 0x8)
    SetChrFlags(0x102, 0x8)
    SetChrFlags(0x103, 0x8)
    SetChrFlags(0x104, 0x8)
    SetChrChipByIndex(0x8, 0x14)
    SetChrSubChip(0x8, 0x0)
    SetChrChipByIndex(0x9, 0x14)
    SetChrSubChip(0x9, 0x0)
    SetChrChipByIndex(0xA, 0x14)
    SetChrSubChip(0xA, 0x0)
    SetChrChipByIndex(0xB, 0x18)
    SetChrSubChip(0xB, 0x0)
    SetChrChipByIndex(0xC, 0x18)
    SetChrSubChip(0xC, 0x0)
    OP_90(0x8, -2200, 500, 13000, 180)
    OP_90(0x9, -2200, 500, 13000, 180)
    OP_90(0xA, -2200, 500, 13000, 180)
    OP_90(0xB, -2200, 500, 13000, 180)
    OP_90(0xC, -2200, 500, 13000, 180)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x8000)
    SetChrFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x8000)
    SetChrFlags(0xC, 0x8000)
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xB, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xC, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    SetChrChipByIndex(0xD, 0x29)
    SetChrSubChip(0xD, 0x0)
    SetChrChipByIndex(0xE, 0x2E)
    SetChrSubChip(0xE, 0x0)
    SetChrChipByIndex(0xF, 0x33)
    SetChrSubChip(0xF, 0x0)
    SetChrChipByIndex(0x14, 0x1C)
    SetChrSubChip(0x14, 0x0)
    SetChrChipByIndex(0x15, 0x22)
    SetChrSubChip(0x15, 0x0)
    SetChrChipByIndex(0x16, 0x1C)
    SetChrSubChip(0x16, 0x0)
    SetChrChipByIndex(0x17, 0x22)
    SetChrSubChip(0x17, 0x0)
    SetChrChipByIndex(0x18, 0x1C)
    SetChrSubChip(0x18, 0x0)
    SetChrChipByIndex(0x10, 0x1F)
    SetChrSubChip(0x10, 0x0)
    SetChrChipByIndex(0x11, 0x1F)
    SetChrSubChip(0x11, 0x0)
    SetChrChipByIndex(0x12, 0x1F)
    SetChrSubChip(0x12, 0x0)
    SetChrChipByIndex(0x13, 0x25)
    SetChrSubChip(0x13, 0x0)
    OP_90(0xD, 3500, 2000, 25000, 180)
    OP_90(0xE, 5500, 2000, 26000, 180)
    OP_90(0xF, -5500, 2000, 20800, 90)
    OP_90(0x10, -6100, 0, 11200, 90)
    OP_90(0x11, -6300, 0, 9200, 45)
    OP_90(0x12, 700, 0, 4000, 0)
    OP_90(0x13, 1400, 0, 2800, 0)
    OP_90(0x14, 14800, 0, 14000, 270)
    OP_90(0x15, 15700, 0, 12800, 270)
    OP_90(0x16, 15800, 0, 10400, 315)
    OP_90(0x17, 13900, 0, 9700, 315)
    OP_90(0x18, 17500, 0, 12800, 270)
    SetChrFlags(0xD, 0x8000)
    SetChrFlags(0xE, 0x8000)
    SetChrFlags(0xF, 0x8000)
    SetChrFlags(0x14, 0x8000)
    SetChrFlags(0x15, 0x8000)
    SetChrFlags(0x16, 0x8000)
    SetChrFlags(0x17, 0x8000)
    SetChrFlags(0x18, 0x8000)
    SetChrFlags(0x10, 0x8000)
    SetChrFlags(0x11, 0x8000)
    SetChrFlags(0x12, 0x8000)
    SetChrFlags(0x13, 0x8000)
    OP_78(0x12, 0x19)
    SetMapObjFlags(0x12, 0x1000)
    SetChrFlags(0x19, 0x8000)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x19, 0x4)
    OP_49()
    SetChrPos(0x19, -27000, 0, 14000, 0)
    OP_D3(0x19, 0x0, 0x15F90, 0x0, 0x0)
    OP_74(0x12, 0x1E)
    OP_71(0x12, 0xB5, 0xF0, 0x0, 0x20)
    LoadEffect(0x0, "battle\\ms00001.eff")
    LoadEffect(0x1, "battle\\cr004001.eff")
    LoadEffect(0x2, "battle\\cr313100.eff")
    LoadEffect(0x3, "event\\ev606_00.eff")
    LoadEffect(0x4, "battle\\btgun00.eff")
    LoadEffect(0x5, "event\\eva01_00.eff")
    LoadEffect(0x6, "battle\\cr318000.eff")
    LoadEffect(0x7, "battle\\cr309000.eff")
    SetCameraDistance(19000, 4000)
    OP_68(-2000, 1000, 14000, 4000)
    FadeToBright(2000, 0)
    Sound(485, 0, 100, 0)

    def lambda_C90():
        OP_96(0xFE, 0xFFFFF830, 0x0, 0x36B0, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_C90)
    Sleep(3000)
    Sound(495, 0, 80, 0)
    WaitChrThread(0x19, 1)
    SetMapObjFlags(0x12, 0x20)
    OP_24(0x1E5)
    OP_71(0x12, 0x5B, 0x78, 0x0, 0x0)
    OP_79(0x12)
    OP_71(0x12, 0xF1, 0x10E, 0x0, 0x0)
    Sound(464, 0, 100, 0)
    OP_79(0x12)
    OP_6F(0x79)
    BeginChrThread(0x9, 3, 0, 25)
    Sleep(500)
    BeginChrThread(0x8, 3, 0, 24)
    Sleep(500)
    BeginChrThread(0xA, 3, 0, 26)
    Sleep(500)
    BeginChrThread(0xC, 3, 0, 28)
    Sleep(500)
    BeginChrThread(0xB, 3, 0, 27)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    ClearChrFlags(0xE, 0x80)
    ClearChrBattleFlags(0xE, 0x8000)
    OP_68(4500, 3000, 22500, 1500)
    MoveCamera(48, 19, 0, 1500)
    SetCameraDistance(14000, 1500)
    OP_6F(0x79)
    OP_70(0x12, 0x0)

    #C0001
    ChrTalk(
        0xD,
        (
            "#5P#0404F……哎呀呀，\x01",
            "好像完全被操纵了呢。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_82(0xC8, 0x0, 0xBB8, 0x1F4)

    #C0002
    ChrTalk(
        0xE,
        "#5P#1607F#4S#N哇啊啊啊啊！\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0xD, 3, 0, 20)
    BeginChrThread(0xE, 3, 0, 21)
    Sleep(700)
    OP_68(4500, 1700, 17000, 1000)
    MoveCamera(32, 9, 0, 1000)
    SetCameraDistance(16000, 1000)
    OP_6F(0x79)
    WaitChrThread(0x8, 3)
    WaitChrThread(0x9, 3)
    WaitChrThread(0xA, 3)
    WaitChrThread(0xB, 3)
    WaitChrThread(0xC, 3)
    WaitChrThread(0xE, 3)
    WaitChrThread(0xD, 3)
    Sleep(500)

    #C0003
    ChrTalk(
        0xE,
        (
            "#5P#1602F哈……\x01",
            "没什么了不起的嘛！\x02\x03",

            "#1609F只要有我瓦鲁多大人的力量，\x01",
            "警备队的这些家伙根本就──\x02",
        )
    )

    CloseMessageWindow()

    def lambda_E6D():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_E6D)

    def lambda_E86():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_E86)
    SetChrSubChip(0x8, 0x2)
    SetChrSubChip(0x9, 0x2)
    Sound(804, 0, 100, 0)
    Sleep(150)
    SetChrSubChip(0x8, 0x1)
    SetChrSubChip(0x9, 0x1)
    Sleep(150)
    Fade(500)
    SetChrChipByIndex(0x8, 0x14)
    SetChrSubChip(0x8, 0x0)
    SetChrChipByIndex(0x9, 0x14)
    SetChrSubChip(0x9, 0x0)
    Sound(531, 0, 100, 0)
    OP_0D()
    OP_63(0xE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0004
    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#12P#30W…………………………………\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#11P#35W…………………………………\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0xE,
        "#5P#1605F这、这些家伙是怎么回事！？\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xD, 0x4)
    SetChrChipByIndex(0xD, 0x28)
    SetChrSubChip(0xD, 0x0)
    OP_68(4590, 1700, 16770, 600)

    def lambda_F91():
        OP_98(0xFE, 0x0, 0x0, 0xFFFFFBB4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_F91)
    WaitChrThread(0xD, 1)
    SetChrChipByIndex(0xD, 0x29)
    SetChrSubChip(0xD, 0x0)
    OP_6F(0x1)

    #C0007
    ChrTalk(
        0xD,
        (
            "#5P#0406F不是和你说过吗？\x01",
            "他们通过服用药物，能力得到了很大程度的强化。\x02\x03",

            "#0400F就像你们那个\x01",
            "行踪不明的迪诺一样。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0xE,
        (
            "#5P#1603F嘁……是这样啊。\x02\x03",

            "#1601F看来有必要\x01",
            "把总账算清啊……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_82(0xC8, 0x0, 0xBB8, 0x1F4)

    #C0009
    ChrTalk(
        0xE,
        "#5P#1607F#4S兄弟们，要上啦！\x02",
    )

    CloseMessageWindow()
    Sleep(150)
    SetMessageWindowPos(340, 100, -1, -1)
    SetChrName("青年们的声音")
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #A0010
    AnonymousTalk(
        0xFF,
        "#4S收到！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0011
    ChrTalk(
        0xD,
        (
            "#5P#0400F呵呵……\x01",
            "我们也要开始准备圣战了！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    SetMessageWindowPos(80, 170, -1, -1)
    SetChrName("青年们的声音")
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #A0012
    AnonymousTalk(
        0xFF,
        "#4S明白！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Fade(500)
    OP_68(4000, 1000, 13000, 0)
    MoveCamera(37, 23, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(13000, 0)
    MoveCamera(37, 18, 0, 3000)
    SetCameraDistance(17000, 3000)
    ClearChrFlags(0xF, 0x80)
    ClearChrBattleFlags(0xF, 0x8000)
    ClearChrFlags(0x10, 0x80)
    ClearChrBattleFlags(0x10, 0x8000)
    ClearChrFlags(0x11, 0x80)
    ClearChrBattleFlags(0x11, 0x8000)
    ClearChrFlags(0x12, 0x80)
    ClearChrBattleFlags(0x12, 0x8000)
    ClearChrFlags(0x13, 0x80)
    ClearChrBattleFlags(0x13, 0x8000)
    ClearChrFlags(0x14, 0x80)
    ClearChrBattleFlags(0x14, 0x8000)
    ClearChrFlags(0x15, 0x80)
    ClearChrBattleFlags(0x15, 0x8000)
    ClearChrFlags(0x16, 0x80)
    ClearChrBattleFlags(0x16, 0x8000)
    ClearChrFlags(0x17, 0x80)
    ClearChrBattleFlags(0x17, 0x8000)
    ClearChrFlags(0x18, 0x80)
    ClearChrBattleFlags(0x18, 0x8000)
    BeginChrThread(0x14, 3, 0, 30)
    BeginChrThread(0x15, 3, 0, 31)
    BeginChrThread(0x16, 3, 0, 32)
    BeginChrThread(0x17, 3, 0, 33)
    BeginChrThread(0x18, 3, 0, 34)
    BeginChrThread(0x10, 3, 0, 35)
    BeginChrThread(0x11, 3, 0, 36)
    BeginChrThread(0x12, 3, 0, 37)
    BeginChrThread(0x13, 3, 0, 38)
    BeginChrThread(0xF, 3, 0, 29)
    Sleep(300)

    def lambda_1243():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_1243)
    Sleep(100)

    def lambda_1253():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_1253)
    Sleep(100)

    def lambda_1263():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_1263)
    Sleep(100)

    def lambda_1273():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_1273)
    WaitChrThread(0x14, 3)
    WaitChrThread(0x15, 3)
    WaitChrThread(0x16, 3)
    WaitChrThread(0x17, 3)
    WaitChrThread(0x18, 3)
    WaitChrThread(0x10, 3)
    WaitChrThread(0x11, 3)
    WaitChrThread(0x12, 3)
    WaitChrThread(0x13, 3)
    WaitChrThread(0xF, 3)
    OP_6F(0x79)
    Sleep(300)

    #C0013
    ChrTalk(
        0xF,
        (
            "准备完毕──\x01",
            "随时听候差遣，瓦吉。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0xD,
        (
            "#0402F呵呵……\x01",
            "那么，圣战开始。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0xE,
        (
            "#1604F#6P今夜正适合大闹一场……\x02\x03",

            "#1607F兄弟们，尽情蹂躏吧，\x01",
            "一个不留地击溃他们！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("剑蛇帮＆圣书会")
    OP_82(0xC8, 0x0, 0xBB8, 0x1F4)

    #A0016
    AnonymousTalk(
        0xFF,
        "#5S噢噢！！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    LoadEffect(0x0, "battle\\cr308200.eff")
    LoadEffect(0x1, "battle\\cr308100.eff")
    LoadEffect(0x2, "battle\\cr317000.eff")
    MoveCamera(31, 21, 0, 6000)
    SetCameraDistance(18000, 6000)
    BeginChrThread(0x8, 3, 0, 5)
    BeginChrThread(0xA, 3, 0, 7)
    BeginChrThread(0x13, 3, 0, 13)
    BeginChrThread(0x15, 3, 0, 16)
    BeginChrThread(0x16, 3, 0, 17)
    BeginChrThread(0x17, 3, 0, 18)
    Sleep(4000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    ClearChrFlags(0x101, 0x8)
    ClearChrFlags(0x102, 0x8)
    ClearChrFlags(0x103, 0x8)
    ClearChrFlags(0x104, 0x8)
    SetScenarioFlags(0x5C, 3)
    NewScene("c130B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_4_7E1 end

    def Function_5_143F(): pass

    label("Function_5_143F")

    Sleep(300)
    SetChrChipByIndex(0xFE, 0x16)
    SetChrSubChip(0xFE, 0x0)
    Sleep(70)
    SetChrSubChip(0xFE, 0x1)
    Sleep(70)
    SetChrSubChip(0xFE, 0x2)
    BeginChrThread(0x11, 3, 0, 11)

    def lambda_1463():
        OP_A6(0xFE, 0x0, 0x1E, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1463)
    SetChrSubChip(0xFE, 0x3)
    Sound(957, 0, 100, 0)
    PlayEffect(0x4, 0xFF, 0xFE, 0x140, 0, 900, 700, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 1300, 0, 10600, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x4, 0xFF, 0xFE, 0x140, 0, 900, 700, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 200, 0, 11000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x4, 0xFF, 0xFE, 0x140, 0, 900, 700, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 200, 0, 9500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x4, 0xFF, 0xFE, 0x140, 0, 900, 700, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 1000, 0, 10100, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x4, 0xFF, 0xFE, 0x140, 0, 900, 700, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, -800, 0, 8300, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    SetChrSubChip(0xFE, 0x2)
    Sleep(500)

    def lambda_16C2():
        OP_A6(0xFE, 0x0, 0x1E, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_16C2)
    SetChrSubChip(0xFE, 0x3)
    Sound(957, 0, 100, 0)
    PlayEffect(0x4, 0xFF, 0xFE, 0x140, 0, 900, 700, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 1300, 0, 10600, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x4, 0xFF, 0xFE, 0x140, 0, 900, 700, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 200, 0, 11000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x4, 0xFF, 0xFE, 0x140, 0, 900, 700, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 200, 0, 9500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x4, 0xFF, 0xFE, 0x140, 0, 900, 700, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 1000, 0, 10100, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x4, 0xFF, 0xFE, 0x140, 0, 900, 700, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, -800, 0, 8300, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    SetChrSubChip(0xFE, 0x2)
    Sleep(1500)

    def lambda_1921():
        OP_A6(0xFE, 0x0, 0x1E, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1921)
    SetChrSubChip(0xFE, 0x3)
    Sound(957, 0, 100, 0)
    PlayEffect(0x4, 0xFF, 0xFE, 0x140, 0, 900, 700, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0xFF, 0x11, 0x40, 300, 300, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x4, 0xFF, 0xFE, 0x140, 0, 900, 700, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0xFF, 0x11, 0x40, -300, 300, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x4, 0xFF, 0xFE, 0x140, 0, 900, 700, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0xFF, 0x11, 0x40, 300, 300, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x4, 0xFF, 0xFE, 0x140, 0, 900, 700, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0xFF, 0x11, 0x40, 300, 300, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0xFE, 0x2)
    Sleep(1000)
    OP_52(0x8, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_NOT), scpexpr(EXPR_AND_SAVE), scpexpr(EXPR_END)))
    SetChrFlags(0x8, 0x4)
    SetChrChipByIndex(0x8, 0x15)
    SetChrSubChip(0x8, 0x1)

    def lambda_1B25():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_1B25)

    def lambda_1B32():
        OP_9D(0xFE, 0xA28, 0x0, 0x3908, 0x384, 0x9C4)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1B32)
    WaitChrThread(0x8, 1)
    SetChrChipByIndex(0x8, 0x14)
    SetChrSubChip(0x8, 0x0)
    Return()

    # Function_5_143F end

    def Function_6_1B57(): pass

    label("Function_6_1B57")

    OP_52(0x9, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_NOT), scpexpr(EXPR_AND_SAVE), scpexpr(EXPR_END)))
    SetChrFlags(0x9, 0x4)
    SetChrChipByIndex(0x9, 0x15)
    SetChrSubChip(0x9, 0x1)

    def lambda_1B75():
        OP_93(0xFE, 0x82, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_1B75)

    def lambda_1B82():
        OP_9D(0xFE, 0x170C, 0x0, 0x3B60, 0x2BC, 0x9C4)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1B82)
    WaitChrThread(0x9, 1)
    SetChrChipByIndex(0x9, 0x14)
    SetChrSubChip(0x9, 0x0)
    Sleep(50)
    SetChrChipByIndex(0x9, 0x16)
    SetChrSubChip(0x9, 0x0)
    Sleep(70)
    SetChrSubChip(0x9, 0x1)
    Sleep(70)
    SetChrSubChip(0x9, 0x2)

    def lambda_1BC4():
        OP_A6(0xFE, 0x0, 0x1E, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1BC4)
    SetChrSubChip(0xFE, 0x3)
    Sound(356, 0, 100, 0)
    PlayEffect(0x4, 0xFF, 0xFE, 0x140, 0, 900, 700, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 8400, 0, 14500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x4, 0xFF, 0xFE, 0x140, 0, 900, 700, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 8100, 0, 13000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x4, 0xFF, 0xFE, 0x140, 0, 900, 700, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 9300, 0, 13000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x4, 0xFF, 0xFE, 0x140, 0, 900, 700, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 11100, 0, 14100, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x4, 0xFF, 0xFE, 0x140, 0, 900, 700, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 9300, 0, 11600, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    SetChrSubChip(0xFE, 0x2)
    Sleep(500)

    def lambda_1E23():
        OP_A6(0xFE, 0x0, 0x1E, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1E23)
    SetChrSubChip(0xFE, 0x3)
    Sound(356, 0, 100, 0)
    PlayEffect(0x4, 0xFF, 0xFE, 0x140, 0, 900, 700, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 8400, 0, 14500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x4, 0xFF, 0xFE, 0x140, 0, 900, 700, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 8100, 0, 13000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x4, 0xFF, 0xFE, 0x140, 0, 900, 700, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 9300, 0, 13000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x4, 0xFF, 0xFE, 0x140, 0, 900, 700, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 11100, 0, 14100, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x4, 0xFF, 0xFE, 0x140, 0, 900, 700, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 9300, 0, 11600, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    SetChrSubChip(0xFE, 0x2)
    Sleep(300)
    SetChrChipByIndex(0x9, 0x15)
    SetChrSubChip(0x9, 0x1)

    def lambda_208A():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_208A)

    def lambda_2097():
        OP_9D(0xFE, 0x16A8, 0x0, 0x332C, 0x2BC, 0x9C4)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2097)
    WaitChrThread(0x9, 1)
    SetChrChipByIndex(0x9, 0x14)
    SetChrSubChip(0x9, 0x0)
    Sleep(100)
    SetChrChipByIndex(0x9, 0x17)
    SetChrSubChip(0x9, 0x0)

    def lambda_20CB():
        OP_A6(0xFE, 0x64, 0x64, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_20CB)

    def lambda_20E4():
        OP_9D(0xFE, 0xDAC, 0x0, 0x3264, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_20E4)
    WaitChrThread(0x9, 1)

    def lambda_2105():
        OP_A6(0xFE, 0x32, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_2105)
    SetChrSubChip(0x9, 0x3)
    Return()

    # Function_6_1B57 end

    def Function_7_211E(): pass

    label("Function_7_211E")

    SetChrChipByIndex(0xA, 0x16)
    SetChrSubChip(0xA, 0x2)
    OP_93(0xA, 0x82, 0x1F4)
    Sleep(100)
    BeginChrThread(0x14, 3, 0, 14)

    def lambda_213B():
        OP_A6(0xFE, 0x0, 0x1E, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_213B)
    SetChrSubChip(0xFE, 0x3)
    PlayEffect(0x4, 0xFF, 0xFE, 0x140, 0, 900, 700, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 7200, 0, 13800, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x4, 0xFF, 0xFE, 0x140, 0, 900, 700, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 8700, 0, 14700, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x4, 0xFF, 0xFE, 0x140, 0, 900, 700, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 8600, 0, 12800, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    SetChrSubChip(0xFE, 0x2)
    Sleep(500)
    OP_93(0xA, 0xDC, 0x1F4)
    Sleep(100)

    def lambda_22BC():
        OP_A6(0xFE, 0x0, 0x1E, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_22BC)
    SetChrSubChip(0xFE, 0x3)
    PlayEffect(0x4, 0xFF, 0xFE, 0x140, 0, 900, 700, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 1900, 0, 11100, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x4, 0xFF, 0xFE, 0x140, 0, 900, 700, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 1900, 0, 9800, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x4, 0xFF, 0xFE, 0x140, 0, 900, 700, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 700, 0, 9500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    SetChrSubChip(0xFE, 0x2)
    Sleep(700)
    OP_93(0xA, 0x82, 0x1F4)
    Sleep(100)

    def lambda_243D():
        OP_A6(0xFE, 0x0, 0x1E, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_243D)
    SetChrSubChip(0xFE, 0x3)
    PlayEffect(0x4, 0xFF, 0xFE, 0x140, 0, 900, 700, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 7200, 0, 13800, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x4, 0xFF, 0xFE, 0x140, 0, 900, 700, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 8700, 0, 14700, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x4, 0xFF, 0xFE, 0x140, 0, 900, 700, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 8600, 0, 12800, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    SetChrSubChip(0xFE, 0x2)
    Sleep(700)

    def lambda_25B4():
        OP_A6(0xFE, 0x0, 0x1E, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_25B4)
    SetChrSubChip(0xFE, 0x3)
    PlayEffect(0x4, 0xFF, 0xFE, 0x140, 0, 900, 700, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0xFF, 0x15, 0x40, 300, 300, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x4, 0xFF, 0xFE, 0x140, 0, 900, 700, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0xFF, 0x15, 0x40, -300, 300, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x4, 0xFF, 0xFE, 0x140, 0, 900, 700, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0xFF, 0x15, 0x40, 300, 300, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x4, 0xFF, 0xFE, 0x140, 0, 900, 700, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0xFF, 0x15, 0x40, 300, 300, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0xFE, 0x2)
    Sleep(700)

    def lambda_2799():
        OP_A6(0xFE, 0x0, 0x1E, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2799)
    SetChrSubChip(0xFE, 0x3)
    Sound(356, 0, 100, 0)
    PlayEffect(0x4, 0xFF, 0xFE, 0x140, 0, 900, 700, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0xFF, 0x14, 0x40, 300, 300, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x4, 0xFF, 0xFE, 0x140, 0, 900, 700, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0xFF, 0x14, 0x40, -300, 300, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x4, 0xFF, 0xFE, 0x140, 0, 900, 700, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0xFF, 0x14, 0x40, 300, 300, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x4, 0xFF, 0xFE, 0x140, 0, 900, 700, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0xFF, 0x14, 0x40, 300, 300, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0xFE, 0x2)
    Return()

    # Function_7_211E end

    def Function_8_297D(): pass

    label("Function_8_297D")

    OP_52(0xB, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_NOT), scpexpr(EXPR_AND_SAVE), scpexpr(EXPR_END)))

    def lambda_298E():

        label("loc_298E")

        TurnDirection(0xFE, 0x13, 0)
        Yield()
        Jump("loc_298E")

    QueueWorkItem2(0xB, 2, lambda_298E)
    SetChrFlags(0xB, 0x4)
    SetChrChipByIndex(0xB, 0x19)
    SetChrSubChip(0xB, 0x1)
    Sound(854, 0, 100, 0)

    def lambda_29B3():
        OP_9D(0xFE, 0x1068, 0x384, 0x1FA4, 0x76C, 0x9C4)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_29B3)
    WaitChrThread(0xB, 1)
    Sleep(1000)
    Sound(854, 0, 100, 0)

    def lambda_29DD():
        OP_9D(0xFE, 0xCE4, 0x0, 0x2A30, 0x384, 0x9C4)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_29DD)
    WaitChrThread(0xB, 1)
    SetChrChipByIndex(0xB, 0x18)
    SetChrSubChip(0xB, 0x0)
    EndChrThread(0xB, 0x2)
    Sleep(70)
    SetChrChipByIndex(0xB, 0x1A)
    SetChrSubChip(0xB, 0x0)
    Sleep(70)
    SetChrSubChip(0xB, 0x1)
    Sleep(70)
    SetChrSubChip(0xB, 0x2)

    def lambda_2A23():
        OP_A6(0xFE, 0x32, 0x0, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_2A23)
    PlayEffect(0x5, 0xFF, 0x12, 0x140, 500, 1500, 300, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1100)
    SetChrSubChip(0xB, 0x3)
    Sleep(350)
    SetChrSubChip(0xB, 0x4)
    Sleep(100)
    SetChrSubChip(0xB, 0x5)
    Sleep(100)
    SetChrChipByIndex(0xB, 0x1B)
    SetChrSubChip(0xB, 0x0)

    def lambda_2A93():
        OP_A6(0xFE, 0x64, 0x64, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_2A93)

    def lambda_2AAC():
        OP_9D(0xFE, 0xED8, 0x0, 0x2E18, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_2AAC)
    WaitChrThread(0xB, 1)

    def lambda_2ACD():
        OP_A6(0xFE, 0x32, 0x32, 0x2BC, 0xBB8)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_2ACD)
    SetChrSubChip(0xB, 0x3)
    Sleep(500)
    SetChrSubChip(0xB, 0x2)
    Sleep(100)
    SetChrChipByIndex(0xB, 0x18)
    SetChrSubChip(0xB, 0x0)
    Return()

    # Function_8_297D end

    def Function_9_2AF8(): pass

    label("Function_9_2AF8")


    def lambda_2AFD():
        OP_A6(0xFE, 0x32, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_2AFD)
    SetChrChipByIndex(0xC, 0x17)
    SetChrSubChip(0xC, 0x1)
    Sleep(110)
    SetChrSubChip(0xC, 0x2)
    Sleep(110)
    SetChrSubChip(0xC, 0x3)
    Sleep(700)

    def lambda_2B2F():
        OP_A6(0xFE, 0x32, 0x32, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_2B2F)
    SetChrSubChip(0xC, 0x3)
    Sleep(200)
    SetChrSubChip(0xC, 0x2)
    Sleep(100)
    SetChrChipByIndex(0xC, 0x19)
    SetChrSubChip(0xC, 0x0)

    def lambda_2B5E():
        OP_9D(0xFE, 0xF3C, 0x0, 0x2E7C, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_2B5E)
    WaitChrThread(0xC, 1)
    Sleep(150)
    SetChrChipByIndex(0xC, 0x1A)
    SetChrSubChip(0xC, 0x1)

    def lambda_2B8A():
        OP_9D(0xFE, 0x13EC, 0x0, 0x2DB4, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_2B8A)
    Sleep(70)
    SetChrSubChip(0xC, 0x2)
    Sleep(70)
    SetChrSubChip(0xC, 0x3)
    WaitChrThread(0xC, 1)
    SetChrSubChip(0xC, 0x4)
    Return()

    # Function_9_2AF8 end

    def Function_10_2BB9(): pass

    label("Function_10_2BB9")

    SetChrChipByIndex(0x10, 0x21)
    SetChrSubChip(0x10, 0x0)
    OP_52(0x10, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_NOT), scpexpr(EXPR_AND_SAVE), scpexpr(EXPR_END)))
    Sleep(110)
    Sound(814, 0, 100, 0)

    def lambda_2BDB():
        OP_9C(0xFE, 0x0, 0x0, 0x0, 0x44C, 0xBB8)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_2BDB)
    Sleep(150)
    SetChrSubChip(0x10, 0x1)
    Sleep(250)
    SetChrSubChip(0x10, 0x2)
    WaitChrThread(0x10, 1)
    PlayEffect(0x7, 0xFF, 0x10, 0x100, 0, 100, 300, 0, 0, 0, 350, 350, 350, 0xFF, 0, 0, 0, 0)
    Sound(332, 0, 100, 0)

    def lambda_2C47():
        OP_A6(0xFE, 0x32, 0x0, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_2C47)
    SetChrSubChip(0x10, 0x3)
    Sleep(500)
    BeginChrThread(0xC, 3, 0, 9)
    Sleep(500)
    SetChrSubChip(0x10, 0x4)
    Sleep(130)
    SetChrSubChip(0x10, 0x5)
    Sleep(130)
    SetChrChipByIndex(0x10, 0x1F)
    SetChrSubChip(0x10, 0x0)
    Sleep(750)
    TurnDirection(0x10, 0x8, 500)
    SetChrChipByIndex(0x10, 0x21)
    SetChrSubChip(0x10, 0x0)
    OP_52(0x10, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_NOT), scpexpr(EXPR_AND_SAVE), scpexpr(EXPR_END)))
    Sleep(110)
    Sound(814, 0, 100, 0)

    def lambda_2CAD():
        OP_9C(0xFE, 0x0, 0x0, 0x0, 0x44C, 0xBB8)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_2CAD)
    Sleep(150)
    SetChrSubChip(0x10, 0x1)
    Sleep(250)
    SetChrSubChip(0x10, 0x2)
    WaitChrThread(0x10, 1)
    PlayEffect(0x7, 0xFF, 0x10, 0x100, 0, 100, 300, 0, 0, 0, 350, 350, 350, 0xFF, 0, 0, 0, 0)
    Sound(332, 0, 100, 0)

    def lambda_2D19():
        OP_A6(0xFE, 0x32, 0x0, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_2D19)
    SetChrSubChip(0x10, 0x3)
    Sleep(1000)
    SetChrSubChip(0x10, 0x4)
    Sleep(130)
    SetChrSubChip(0x10, 0x5)
    Sleep(130)
    SetChrChipByIndex(0x10, 0x1F)
    SetChrSubChip(0x10, 0x0)
    Sleep(600)
    Return()

    # Function_10_2BB9 end

    def Function_11_2D4E(): pass

    label("Function_11_2D4E")

    Sleep(500)
    SetChrChipByIndex(0x11, 0x20)
    SetChrSubChip(0x11, 0x0)

    def lambda_2D5E():
        OP_96(0xFE, 0xFFFFF830, 0x0, 0x1FA4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_2D5E)
    WaitChrThread(0x11, 1)
    SetChrChipByIndex(0x11, 0x1F)
    SetChrSubChip(0x11, 0x0)
    Sleep(500)
    SetChrChipByIndex(0x11, 0x20)
    SetChrSubChip(0x11, 0x0)

    def lambda_2D8F():
        OP_96(0xFE, 0x4B0, 0x0, 0x2CEC, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_2D8F)
    WaitChrThread(0x11, 1)
    OP_52(0x11, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_NOT), scpexpr(EXPR_AND_SAVE), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x11, 0x34)
    SetChrSubChip(0x11, 0x0)

    def lambda_2DC1():
        OP_A6(0xFE, 0x64, 0x64, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_2DC1)

    def lambda_2DDA():
        OP_9D(0xFE, 0xFFFFFE0C, 0x0, 0x24B8, 0x2BC, 0xBB8)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_2DDA)
    WaitChrThread(0x11, 1)

    def lambda_2DFB():
        OP_A6(0xFE, 0x32, 0x32, 0x5DC, 0xBB8)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_2DFB)
    SetChrSubChip(0x11, 0x3)
    Sleep(1400)
    SetChrSubChip(0x11, 0x2)
    Sleep(100)
    SetChrChipByIndex(0x11, 0x1F)
    SetChrSubChip(0x11, 0x0)
    Return()

    # Function_11_2D4E end

    def Function_12_2E26(): pass

    label("Function_12_2E26")

    EndChrThread(0x12, 0x2)
    OP_93(0x12, 0x28, 0x0)
    SetChrFlags(0x12, 0x4)
    SetChrChipByIndex(0x12, 0x21)
    SetChrSubChip(0x12, 0x0)
    OP_52(0x12, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_NOT), scpexpr(EXPR_AND_SAVE), scpexpr(EXPR_END)))

    def lambda_2E4F():
        OP_9D(0xFE, 0xA28, 0x0, 0x27D8, 0x2BC, 0x9C4)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_2E4F)
    Sleep(150)
    SetChrSubChip(0x12, 0x1)
    Sleep(250)
    SetChrSubChip(0x12, 0x2)
    WaitChrThread(0x12, 1)

    def lambda_2E7E():
        OP_A6(0xFE, 0x32, 0x0, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_2E7E)
    Sleep(1100)
    SetChrChipByIndex(0x12, 0x20)
    SetChrSubChip(0x12, 0x1)

    def lambda_2EA2():
        OP_9D(0xFE, 0xC8, 0x0, 0x206C, 0x2BC, 0x9C4)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_2EA2)
    WaitChrThread(0x12, 1)
    SetChrChipByIndex(0x12, 0x1F)
    SetChrSubChip(0x12, 0x1)
    Return()

    # Function_12_2E26 end

    def Function_13_2EC7(): pass

    label("Function_13_2EC7")


    def lambda_2ECC():

        label("loc_2ECC")

        TurnDirection(0xFE, 0xB, 300)
        Yield()
        Jump("loc_2ECC")

    QueueWorkItem2(0x12, 2, lambda_2ECC)
    SetChrPos(0x1A, 3500, 500, 12600, 0)
    OP_A7(0x1A, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x1A, 0x14)
    SetChrSubChip(0x1A, 0x0)
    ClearChrFlags(0x1A, 0x80)
    SetChrChipByIndex(0x13, 0x27)
    SetChrSubChip(0x13, 0x0)
    Sleep(110)
    SetChrSubChip(0x13, 0x1)
    Sleep(110)
    SetChrSubChip(0x13, 0x2)

    def lambda_2F1D():
        OP_A6(0xFE, 0x32, 0x0, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_2F1D)
    Sleep(500)
    BeginChrThread(0xB, 3, 0, 8)
    PlayEffect(0x6, 0xFF, 0x13, 0x140, 0, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 0x1A, 0, 0, 0, 0)
    SetChrSubChip(0x13, 0x3)
    Sleep(70)
    SetChrSubChip(0x13, 0x4)
    Sleep(80)
    PlayEffect(0x3, 0x0, 0x1A, 0x0, 0, -100, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(337, 0, 100, 0)
    Sleep(620)
    SetChrPos(0x1A, 4200, 900, 8100, 0)
    SetChrChipByIndex(0x13, 0x25)
    SetChrSubChip(0x13, 0x0)
    TurnDirection(0x13, 0x1A, 500)
    SetChrChipByIndex(0x13, 0x27)
    SetChrSubChip(0x13, 0x0)
    Sleep(110)
    SetChrSubChip(0x13, 0x1)
    Sleep(110)
    SetChrSubChip(0x13, 0x2)

    def lambda_2FFA():
        OP_A6(0xFE, 0x32, 0x0, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_2FFA)
    Sleep(500)
    PlayEffect(0x6, 0xFF, 0x13, 0x140, 0, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 0x1A, 0, 0, 0, 0)
    SetChrSubChip(0x13, 0x3)
    Sleep(70)
    SetChrSubChip(0x13, 0x4)
    Sleep(80)
    PlayEffect(0x3, 0x0, 0x1A, 0x0, 0, -100, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(337, 0, 100, 0)
    Sleep(300)
    BeginChrThread(0x12, 3, 0, 12)
    Sleep(320)
    Sleep(700)
    SetChrPos(0x1A, 3300, 500, 10800, 0)
    SetChrChipByIndex(0x13, 0x25)
    SetChrSubChip(0x13, 0x0)
    TurnDirection(0x13, 0x1A, 500)
    SetChrChipByIndex(0x13, 0x27)
    SetChrSubChip(0x13, 0x0)
    Sleep(110)
    SetChrSubChip(0x13, 0x1)
    Sleep(110)
    SetChrSubChip(0x13, 0x2)

    def lambda_30DD():
        OP_A6(0xFE, 0x32, 0x0, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_30DD)
    Sleep(500)
    PlayEffect(0x6, 0xFF, 0x13, 0x140, 0, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 0x1A, 0, 0, 0, 0)
    SetChrSubChip(0x13, 0x3)
    Sleep(70)
    SetChrSubChip(0x13, 0x4)
    Sleep(80)
    PlayEffect(0x3, 0x0, 0x1A, 0x0, 0, -100, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(337, 0, 100, 0)
    Sleep(620)
    Return()

    # Function_13_2EC7 end

    def Function_14_317A(): pass

    label("Function_14_317A")

    SetChrChipByIndex(0x14, 0x1D)
    SetChrSubChip(0x14, 0x0)

    def lambda_3187():
        OP_96(0xFE, 0x2B5C, 0x0, 0x3778, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_3187)
    WaitChrThread(0x14, 1)
    SetChrChipByIndex(0x14, 0x1C)
    SetChrSubChip(0x14, 0x0)
    Sleep(700)
    SetChrChipByIndex(0x14, 0x1D)
    SetChrSubChip(0x14, 0x3)
    Sound(814, 0, 100, 0)

    def lambda_31BE():
        OP_9D(0xFE, 0x33F4, 0x0, 0x3840, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_31BE)
    WaitChrThread(0x14, 1)
    SetChrChipByIndex(0x14, 0x1C)
    SetChrSubChip(0x14, 0x0)
    Sleep(300)
    SetChrChipByIndex(0x14, 0x1D)
    SetChrSubChip(0x14, 0x0)

    def lambda_31F2():
        OP_96(0xFE, 0x2580, 0x0, 0x3778, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_31F2)
    WaitChrThread(0x14, 1)
    SetChrChipByIndex(0x14, 0x1E)
    SetChrSubChip(0x14, 0x1)
    Sound(814, 0, 100, 0)

    def lambda_321E():
        OP_9D(0xFE, 0x1AF4, 0x0, 0x3520, 0x44C, 0xBB8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_321E)
    Sleep(150)
    SetChrSubChip(0x14, 0x2)
    BeginChrThread(0x14, 2, 0, 15)
    Sleep(150)
    PlayEffect(0x0, 0xFF, 0x14, 0x140, 0, 700, 0, 0, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)
    Sound(534, 0, 100, 0)
    WaitChrThread(0x14, 1)
    SetChrSubChip(0x14, 0x3)
    WaitChrThread(0x14, 2)
    Sleep(300)

    def lambda_3297():
        OP_A6(0xFE, 0x64, 0x64, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_3297)
    SetChrChipByIndex(0x14, 0x35)
    SetChrSubChip(0x14, 0x0)

    def lambda_32B8():
        OP_9D(0xFE, 0x24B8, 0x0, 0x38A4, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_32B8)
    WaitChrThread(0x14, 1)
    Sleep(300)

    def lambda_32DC():
        OP_A6(0xFE, 0x32, 0x32, 0x2BC, 0xBB8)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_32DC)
    SetChrSubChip(0x14, 0x3)
    Sleep(200)
    SetChrSubChip(0x14, 0x2)
    Sleep(200)
    SetChrChipByIndex(0x14, 0x1C)
    SetChrSubChip(0x14, 0x0)
    Sleep(300)
    Return()

    # Function_14_317A end

    def Function_15_330A(): pass

    label("Function_15_330A")

    OP_93(0x14, 0xE1, 0x0)
    Sleep(40)
    OP_93(0x14, 0xB4, 0x0)
    Sleep(40)
    OP_93(0x14, 0x87, 0x0)
    Sleep(40)
    OP_93(0x14, 0x5A, 0x0)
    Sleep(40)
    OP_93(0x14, 0x2D, 0x0)
    Sleep(40)
    OP_93(0x14, 0x0, 0x0)
    Sleep(40)
    OP_93(0x14, 0x13B, 0x0)
    Sleep(40)
    OP_93(0x14, 0x10E, 0x0)
    Return()

    # Function_15_330A end

    def Function_16_3358(): pass

    label("Function_16_3358")

    Sleep(100)
    SetChrChipByIndex(0x15, 0x23)
    SetChrSubChip(0x15, 0x0)

    def lambda_3368():
        OP_96(0xFE, 0x1DB0, 0x0, 0x3264, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_3368)
    WaitChrThread(0x15, 1)
    SetChrSubChip(0x15, 0x3)
    OP_52(0x15, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_NOT), scpexpr(EXPR_AND_SAVE), scpexpr(EXPR_END)))

    def lambda_3396():
        OP_9D(0xFE, 0x2968, 0x0, 0x319C, 0x2BC, 0x9C4)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_3396)
    WaitChrThread(0x15, 1)
    SetChrChipByIndex(0x15, 0x22)
    SetChrSubChip(0x15, 0x0)
    Sleep(100)

    def lambda_33C2():
        OP_A6(0xFE, 0x32, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_33C2)
    SetChrChipByIndex(0x15, 0x36)
    SetChrSubChip(0x15, 0x2)
    Sleep(200)
    SetChrSubChip(0x15, 0x3)
    Sleep(1300)

    def lambda_33ED():
        OP_A6(0xFE, 0x32, 0x32, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_33ED)
    SetChrSubChip(0x15, 0x2)
    Sleep(200)
    SetChrChipByIndex(0x15, 0x22)
    SetChrSubChip(0x15, 0x0)
    Sleep(100)
    SetChrChipByIndex(0x15, 0x23)
    SetChrSubChip(0x15, 0x0)

    def lambda_3420():
        OP_96(0xFE, 0x1DB0, 0x0, 0x3264, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_3420)
    WaitChrThread(0x15, 1)
    SetChrChipByIndex(0x15, 0x36)
    SetChrSubChip(0x15, 0x0)

    def lambda_3446():
        OP_A6(0xFE, 0x64, 0x64, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_3446)

    def lambda_345F():
        OP_9D(0xFE, 0x2968, 0x0, 0x319C, 0x2BC, 0x9C4)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_345F)
    WaitChrThread(0x15, 1)
    SetChrSubChip(0x15, 0x3)
    Sleep(300)

    def lambda_3487():
        OP_A6(0xFE, 0x32, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_3487)
    SetChrSubChip(0x15, 0x2)
    Sleep(200)
    SetChrChipByIndex(0x15, 0x24)
    SetChrSubChip(0x15, 0x0)
    Sleep(300)
    Return()

    # Function_16_3358 end

    def Function_17_34AE(): pass

    label("Function_17_34AE")

    Sleep(900)
    SetChrPos(0x1C, 4300, 0, 14100, 0)
    OP_A7(0x1C, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x1C, 0x14)
    SetChrSubChip(0x1C, 0x0)
    ClearChrFlags(0x1C, 0x80)
    SetChrChipByIndex(0x16, 0x1E)
    SetChrSubChip(0x16, 0x0)
    Sleep(110)
    SetChrSubChip(0x16, 0x1)
    PlayEffect(0x1, 0xFF, 0x16, 0x140, 0, 100, 0, 0, 0, 0, 1000, 1000, 1000, 0x1C, 0, 0, 0, 0)
    Sound(241, 0, 100, 0)
    Sleep(300)

    def lambda_352E():
        OP_A6(0xFE, 0x32, 0x0, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0x16, 2, lambda_352E)
    Sleep(300)
    Sound(195, 0, 100, 0)
    SetChrSubChip(0x16, 0x2)
    Sleep(70)
    SetChrSubChip(0x16, 0x3)
    Sleep(700)
    SetChrSubChip(0x16, 0x4)
    Sleep(130)
    SetChrSubChip(0x16, 0x5)
    Sleep(130)
    SetChrChipByIndex(0x16, 0x1C)
    SetChrSubChip(0x16, 0x0)
    Sleep(700)
    OP_52(0x16, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_NOT), scpexpr(EXPR_AND_SAVE), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x16, 0x1E)
    SetChrSubChip(0x16, 0x1)

    def lambda_358B():
        OP_9D(0xFE, 0x1A2C, 0x0, 0x2BC0, 0x44C, 0xBB8)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_358B)
    Sleep(250)
    SetChrSubChip(0x16, 0x2)
    WaitChrThread(0x16, 1)
    SetChrSubChip(0x16, 0x3)
    Sleep(500)

    def lambda_35BA():
        OP_A6(0xFE, 0x64, 0x64, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0x16, 2, lambda_35BA)
    PlayEffect(0x5, 0xFF, 0x16, 0x140, 0, 700, 500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrChipByIndex(0x16, 0x35)
    SetChrSubChip(0x16, 0x0)

    def lambda_3612():
        OP_9D(0xFE, 0x2198, 0x0, 0x2C88, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_3612)
    WaitChrThread(0x16, 1)

    def lambda_3633():
        OP_A6(0xFE, 0x32, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x16, 2, lambda_3633)
    SetChrSubChip(0x16, 0x2)
    Sleep(200)
    SetChrSubChip(0x16, 0x3)
    Sleep(300)
    Return()

    # Function_17_34AE end

    def Function_18_3656(): pass

    label("Function_18_3656")

    OP_52(0x17, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_NOT), scpexpr(EXPR_AND_SAVE), scpexpr(EXPR_END)))
    SetChrFlags(0x17, 0x20)
    SetChrChipByIndex(0x17, 0x24)
    SetChrSubChip(0x17, 0x0)
    Sleep(70)
    SetChrSubChip(0x17, 0x1)
    Sleep(130)
    SetChrSubChip(0x17, 0x2)

    def lambda_3682():
        OP_96(0xFE, 0x1838, 0x0, 0x2968, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_3682)
    BeginChrThread(0x18, 3, 0, 19)
    Sleep(200)
    SetChrSubChip(0x17, 0x3)
    WaitChrThread(0x17, 1)
    SetChrChipByIndex(0xC, 0x1A)
    SetChrSubChip(0xC, 0x2)
    PlayEffect(0x5, 0xFF, 0x17, 0x140, 0, 900, 1000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_36EC():
        OP_A6(0xFE, 0x32, 0x0, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_36EC)

    def lambda_3705():
        OP_A6(0xFE, 0x32, 0x0, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_3705)
    Sleep(700)
    BeginChrThread(0x10, 3, 0, 10)
    Sleep(300)
    SetChrChipByIndex(0x17, 0x23)
    SetChrSubChip(0x17, 0x3)

    def lambda_3732():
        OP_9D(0xFE, 0x1EDC, 0x0, 0x25E4, 0x3E8, 0x9C4)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_3732)
    Sleep(70)
    SetChrSubChip(0xC, 0x3)
    Sleep(100)
    SetChrSubChip(0xC, 0x4)
    Sleep(100)
    SetChrSubChip(0xC, 0x5)
    Sleep(100)
    SetChrChipByIndex(0xC, 0x18)
    SetChrSubChip(0xC, 0x0)
    WaitChrThread(0x17, 1)
    SetChrChipByIndex(0x17, 0x22)
    SetChrSubChip(0x17, 0x0)
    Sleep(700)

    def lambda_377E():

        label("loc_377E")

        TurnDirection(0xFE, 0xC, 0)
        Yield()
        Jump("loc_377E")

    QueueWorkItem2(0x17, 2, lambda_377E)
    SetChrChipByIndex(0x17, 0x23)
    SetChrSubChip(0x17, 0x1)

    def lambda_3798():
        OP_9D(0xFE, 0x15E0, 0x0, 0x238C, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_3798)
    WaitChrThread(0x17, 1)
    SetChrChipByIndex(0x17, 0x22)
    SetChrSubChip(0x17, 0x0)
    Sleep(150)
    SetChrChipByIndex(0x17, 0x23)
    SetChrSubChip(0x17, 0x3)

    def lambda_37CC():
        OP_9D(0xFE, 0x1EDC, 0x0, 0x25E4, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_37CC)
    WaitChrThread(0x17, 1)
    EndChrThread(0x17, 0x2)
    SetChrChipByIndex(0x17, 0x22)
    SetChrSubChip(0x17, 0x0)
    Sleep(700)
    SetChrChipByIndex(0x17, 0x24)
    SetChrSubChip(0x17, 0x0)
    Sleep(70)
    SetChrSubChip(0x17, 0x1)
    Sleep(130)
    SetChrSubChip(0x17, 0x2)

    def lambda_3812():
        OP_96(0xFE, 0x1838, 0x0, 0x2968, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_3812)
    Sleep(200)
    SetChrSubChip(0x17, 0x3)
    WaitChrThread(0x17, 1)
    SetChrChipByIndex(0xC, 0x1A)
    SetChrSubChip(0xC, 0x2)
    PlayEffect(0x5, 0xFF, 0x17, 0x140, 0, 900, 1000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_3876():
        OP_A6(0xFE, 0x32, 0x0, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_3876)

    def lambda_388F():
        OP_A6(0xFE, 0x32, 0x0, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_388F)
    Sleep(1000)
    SetChrChipByIndex(0x17, 0x23)
    SetChrSubChip(0x17, 0x3)

    def lambda_38B3():
        OP_9D(0xFE, 0x1EDC, 0x0, 0x25E4, 0x3E8, 0x9C4)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_38B3)
    Sleep(70)
    SetChrSubChip(0xC, 0x3)
    Sleep(100)
    SetChrSubChip(0xC, 0x4)
    Sleep(100)
    SetChrSubChip(0xC, 0x5)
    Sleep(100)
    SetChrChipByIndex(0xC, 0x18)
    SetChrSubChip(0xC, 0x0)
    WaitChrThread(0x17, 1)
    SetChrChipByIndex(0x17, 0x22)
    SetChrSubChip(0x17, 0x0)
    Return()

    # Function_18_3656 end

    def Function_19_38F8(): pass

    label("Function_19_38F8")

    SetChrPos(0x1B, 5800, 0, 13200, 0)
    OP_A7(0x1B, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x1B, 0x14)
    SetChrSubChip(0x1B, 0x0)
    ClearChrFlags(0x1B, 0x80)
    SetChrChipByIndex(0x18, 0x1E)
    SetChrSubChip(0x18, 0x0)
    Sleep(110)
    SetChrSubChip(0x18, 0x1)
    PlayEffect(0x1, 0xFF, 0x18, 0x140, 0, 100, 0, 0, 0, 0, 1000, 1000, 1000, 0x1B, 0, 0, 0, 0)
    Sound(241, 0, 100, 0)
    Sleep(300)

    def lambda_3975():
        OP_A6(0xFE, 0x32, 0x0, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0x18, 2, lambda_3975)
    Sleep(300)
    Sound(195, 0, 100, 0)
    BeginChrThread(0x9, 3, 0, 6)
    SetChrSubChip(0x18, 0x2)
    Sleep(70)
    SetChrSubChip(0x18, 0x3)
    Sleep(700)
    SetChrSubChip(0x18, 0x4)
    Sleep(130)
    SetChrSubChip(0x18, 0x5)
    Sleep(130)
    SetChrChipByIndex(0x18, 0x1C)
    SetChrSubChip(0x18, 0x0)
    Sleep(700)
    SetChrPos(0x1B, 6000, 0, 15100, 0)
    TurnDirection(0x18, 0x1B, 500)
    SetChrChipByIndex(0x18, 0x1E)
    SetChrSubChip(0x18, 0x0)
    Sleep(110)
    SetChrSubChip(0x18, 0x1)
    PlayEffect(0x1, 0xFF, 0x18, 0x140, 0, 100, 0, 0, 0, 0, 1000, 1000, 1000, 0x1B, 0, 0, 0, 0)
    Sound(241, 0, 100, 0)
    Sleep(300)

    def lambda_3A2B():
        OP_A6(0xFE, 0x32, 0x0, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0x18, 2, lambda_3A2B)
    Sleep(300)
    Sound(195, 0, 100, 0)
    SetChrSubChip(0x18, 0x2)
    Sleep(70)
    SetChrSubChip(0x18, 0x3)
    Sleep(700)
    SetChrSubChip(0x18, 0x4)
    Sleep(130)
    SetChrSubChip(0x18, 0x5)
    Sleep(130)
    SetChrChipByIndex(0x18, 0x1C)
    SetChrSubChip(0x18, 0x0)
    Sleep(500)
    SetChrPos(0x1B, 6340, 0, 11800, 0)
    TurnDirection(0x18, 0x1B, 500)
    SetChrChipByIndex(0x18, 0x1E)
    SetChrSubChip(0x18, 0x0)
    Sleep(110)
    SetChrSubChip(0x18, 0x1)
    PlayEffect(0x1, 0xFF, 0x18, 0x140, 0, 100, 0, 0, 0, 0, 1000, 1000, 1000, 0x1B, 0, 0, 0, 0)
    Sound(241, 0, 100, 0)
    Sleep(300)

    def lambda_3ADB():
        OP_A6(0xFE, 0x32, 0x0, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0x18, 2, lambda_3ADB)
    Sleep(300)
    SetChrSubChip(0x18, 0x2)
    Sleep(70)
    SetChrSubChip(0x18, 0x3)
    Sleep(700)
    SetChrSubChip(0x18, 0x4)
    Sleep(130)
    SetChrSubChip(0x18, 0x5)
    Sleep(130)
    SetChrChipByIndex(0x18, 0x1C)
    SetChrSubChip(0x18, 0x0)
    Return()

    # Function_19_38F8 end

    def Function_20_3B17(): pass

    label("Function_20_3B17")

    Sleep(400)
    SetChrChipByIndex(0xD, 0x2A)
    SetChrSubChip(0xD, 0x0)

    def lambda_3B27():
        OP_95(0xFE, 3500, 2000, 22200, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_3B27)
    WaitChrThread(0xD, 1)
    SetChrChipByIndex(0xD, 0x2C)
    SetChrSubChip(0xD, 0x0)
    Sleep(150)
    SetChrChipByIndex(0xD, 0x2A)
    SetChrSubChip(0xD, 0x1)
    SetChrChip(0x0, 0xD, 0x1E, 0x12C)
    OP_52(0xD, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sound(250, 0, 100, 0)
    Sound(814, 0, 100, 0)

    def lambda_3B77():
        OP_9D(0xFE, 0xDAC, 0x3E8, 0x4718, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_3B77)
    WaitChrThread(0xD, 1)
    SetChrChipByIndex(0xD, 0x2C)
    SetChrSubChip(0xD, 0x0)
    Sleep(100)
    Sound(2092, 255, 100, 0)    #voice#Lazy
    OP_52(0xD, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    PlayEffect(0x1, 0xFF, 0xD, 0x0, 0, 1700, 0, 180, 0, 0, 900, 900, 900, 0xFF, 0, 0, 0, 0)
    Sound(324, 0, 100, 0)
    Sound(625, 0, 100, 0)

    def lambda_3BF7():
        OP_9D(0xFE, 0xDAC, 0x6A4, 0x4C2C, 0x708, 0x7D0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_3BF7)
    SetChrSubChip(0xD, 0x1)
    Sleep(50)
    BeginChrThread(0x8, 3, 0, 22)
    Sound(834, 0, 100, 0)
    Sleep(150)
    SetChrSubChip(0xD, 0x2)
    Sleep(100)
    SetChrSubChip(0xD, 0x3)
    Sleep(100)
    WaitChrThread(0xD, 1)
    OP_52(0xD, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrSubChip(0xD, 0x0)
    SetChrChip(0x1, 0xD, 0x0, 0x0)
    Sleep(500)
    Fade(250)
    SetChrChipByIndex(0xD, 0x29)
    SetChrSubChip(0xD, 0x0)
    OP_0D()
    Return()

    # Function_20_3B17 end

    def Function_21_3C60(): pass

    label("Function_21_3C60")

    SetChrChipByIndex(0xE, 0x2F)
    SetChrSubChip(0xE, 0x0)

    def lambda_3C6D():
        OP_95(0xFE, 5500, 2000, 22200, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_3C6D)
    WaitChrThread(0xE, 1)
    SetChrChipByIndex(0xE, 0x31)
    SetChrSubChip(0xE, 0x1)
    SetChrChip(0x0, 0xE, 0x1E, 0x12C)
    OP_52(0xE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sound(814, 0, 100, 0)
    Sound(1793, 255, 100, 1)    #voice#Wald

    def lambda_3CB2():
        OP_9D(0xFE, 0x157C, 0x3E8, 0x4718, 0x190, 0xBB8)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_3CB2)
    Sleep(100)
    SetChrSubChip(0xE, 0x2)
    Sleep(100)
    Sound(532, 0, 100, 0)
    SetChrSubChip(0xE, 0x3)
    Sleep(100)
    SetChrSubChip(0xE, 0x4)
    Sleep(50)
    WaitChrThread(0xE, 1)
    PlayEffect(0x2, 0xFF, 0xE, 0x0, 0, 100, -1700, 0, 0, 0, 400, 400, 400, 0xFF, 0, 0, 0, 0)
    Sound(834, 0, 100, 0)
    BeginChrThread(0x9, 3, 0, 23)
    SetChrSubChip(0xE, 0x5)
    SetChrChip(0x1, 0xE, 0x0, 0x0)
    OP_52(0xE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(700)
    SetChrSubChip(0xE, 0x6)
    Sleep(150)
    SetChrSubChip(0xE, 0x7)
    Sleep(150)
    Fade(250)
    SetChrChipByIndex(0xE, 0x2E)
    SetChrSubChip(0xE, 0x0)
    OP_0D()
    Return()

    # Function_21_3C60 end

    def Function_22_3D66(): pass

    label("Function_22_3D66")

    OP_82(0x0, 0x12C, 0xBB8, 0x1F4)
    SetChrChipByIndex(0xFE, 0x17)
    SetChrSubChip(0xFE, 0x0)
    PlayEffect(0x0, 0xFF, 0xFE, 0x0, 0, 1000, 0, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sound(501, 0, 100, 0)
    Sound(246, 0, 100, 0)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x4)

    def lambda_3DD0():
        OP_A6(0xFE, 0x0, 0x32, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_3DD0)

    def lambda_3DE9():
        OP_9D(0xFE, 0xAF0, 0x0, 0x3390, 0x2BC, 0x7D0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_3DE9)
    WaitChrThread(0x8, 1)
    SetChrSubChip(0xFE, 0x3)
    Sound(514, 0, 100, 0)
    WaitChrThread(0x8, 2)
    Return()

    # Function_22_3D66 end

    def Function_23_3E14(): pass

    label("Function_23_3E14")

    OP_82(0x0, 0x12C, 0xBB8, 0x1F4)
    SetChrChipByIndex(0xFE, 0x17)
    SetChrSubChip(0xFE, 0x0)
    PlayEffect(0x0, 0xFF, 0xFE, 0x0, 0, 1000, 0, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sound(501, 0, 100, 0)
    Sound(246, 0, 100, 0)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x4)

    def lambda_3E7E():
        OP_A6(0xFE, 0x0, 0x32, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_3E7E)

    def lambda_3E97():
        OP_9D(0xFE, 0x1838, 0x0, 0x3390, 0xC8, 0x7D0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_3E97)
    WaitChrThread(0x9, 1)
    SetChrSubChip(0xFE, 0x3)
    WaitChrThread(0x9, 2)
    Return()

    # Function_23_3E14 end

    def Function_24_3EBC(): pass

    label("Function_24_3EBC")

    SetChrChipByIndex(0xFE, 0x15)
    SetChrSubChip(0xFE, 0x0)

    def lambda_3EC9():
        OP_95(0xFE, -2200, 0, 11000, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3EC9)

    def lambda_3EE3():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3EE3)
    WaitChrThread(0xFE, 1)

    def lambda_3EF8():
        OP_95(0xFE, 1200, 0, 11000, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3EF8)
    WaitChrThread(0xFE, 1)
    ClearChrFlags(0xFE, 0x4)

    def lambda_3F1B():
        OP_95(0xFE, 1200, 0, 11000, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3F1B)
    WaitChrThread(0xFE, 1)

    def lambda_3F39():
        OP_95(0xFE, 3500, 600, 17200, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_3F39)
    WaitChrThread(0x8, 1)
    OP_93(0x8, 0x0, 0x1F4)
    SetChrChipByIndex(0xFE, 0x14)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_24_3EBC end

    def Function_25_3F62(): pass

    label("Function_25_3F62")

    SetChrChipByIndex(0xFE, 0x15)
    SetChrSubChip(0xFE, 0x0)

    def lambda_3F6F():
        OP_95(0xFE, -2200, 0, 11000, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3F6F)

    def lambda_3F89():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3F89)
    WaitChrThread(0xFE, 1)

    def lambda_3F9E():
        OP_95(0xFE, 1200, 0, 11000, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3F9E)
    WaitChrThread(0xFE, 1)
    ClearChrFlags(0xFE, 0x4)

    def lambda_3FC1():
        OP_95(0xFE, 1200, 0, 11000, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3FC1)
    WaitChrThread(0xFE, 1)

    def lambda_3FDF():
        OP_95(0xFE, 5500, 600, 17200, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_3FDF)
    WaitChrThread(0x9, 1)
    OP_93(0x9, 0x0, 0x1F4)
    SetChrChipByIndex(0xFE, 0x14)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_25_3F62 end

    def Function_26_4008(): pass

    label("Function_26_4008")

    SetChrChipByIndex(0xFE, 0x15)
    SetChrSubChip(0xFE, 0x0)

    def lambda_4015():
        OP_95(0xFE, -2200, 0, 11000, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4015)

    def lambda_402F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_402F)
    WaitChrThread(0xFE, 1)

    def lambda_4044():
        OP_95(0xFE, 1200, 0, 11000, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4044)
    WaitChrThread(0xFE, 1)
    ClearChrFlags(0xFE, 0x4)

    def lambda_4067():
        OP_95(0xFE, 1200, 0, 11000, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4067)
    WaitChrThread(0xFE, 1)

    def lambda_4085():
        OP_95(0xFE, 4500, 0, 14300, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_4085)
    WaitChrThread(0xA, 1)
    OP_93(0xA, 0x0, 0x1F4)
    SetChrChipByIndex(0xFE, 0x14)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_26_4008 end

    def Function_27_40AE(): pass

    label("Function_27_40AE")

    SetChrChipByIndex(0xFE, 0x19)
    SetChrSubChip(0xFE, 0x0)

    def lambda_40BB():
        OP_95(0xFE, -2200, 0, 11000, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_40BB)

    def lambda_40D5():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_40D5)
    WaitChrThread(0xFE, 1)

    def lambda_40EA():
        OP_95(0xFE, 1200, 0, 11000, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_40EA)
    WaitChrThread(0xFE, 1)
    ClearChrFlags(0xFE, 0x4)

    def lambda_410D():
        OP_95(0xFE, 1200, 0, 11000, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_410D)
    WaitChrThread(0xFE, 1)

    def lambda_412B():
        OP_95(0xFE, 3000, 0, 11500, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_412B)
    WaitChrThread(0xB, 1)
    OP_93(0xB, 0x0, 0x1F4)
    SetChrChipByIndex(0xFE, 0x18)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_27_40AE end

    def Function_28_4154(): pass

    label("Function_28_4154")

    SetChrChipByIndex(0xFE, 0x19)
    SetChrSubChip(0xFE, 0x0)

    def lambda_4161():
        OP_95(0xFE, -2200, 0, 11000, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4161)

    def lambda_417B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_417B)
    WaitChrThread(0xFE, 1)

    def lambda_4190():
        OP_95(0xFE, 1200, 0, 11000, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4190)
    WaitChrThread(0xFE, 1)
    ClearChrFlags(0xFE, 0x4)

    def lambda_41B3():
        OP_95(0xFE, 1200, 0, 11000, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_41B3)
    WaitChrThread(0xFE, 1)

    def lambda_41D1():
        OP_95(0xFE, 5000, 0, 11500, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_41D1)
    WaitChrThread(0xC, 1)
    OP_93(0xC, 0x0, 0x1F4)
    SetChrChipByIndex(0xFE, 0x18)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_28_4154 end

    def Function_29_41FA(): pass

    label("Function_29_41FA")


    def lambda_41FF():
        OP_96(0xFE, 0x9C4, 0x7D0, 0x5140, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_41FF)
    WaitChrThread(0xF, 1)
    OP_93(0xF, 0xB4, 0x1F4)
    Return()

    # Function_29_41FA end

    def Function_30_4220(): pass

    label("Function_30_4220")

    SetChrChipByIndex(0x14, 0x1D)
    SetChrSubChip(0x14, 0x0)

    def lambda_422D():
        OP_96(0xFE, 0x2648, 0x0, 0x36B0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_422D)
    WaitChrThread(0x14, 1)
    SetChrChipByIndex(0x14, 0x1C)
    SetChrSubChip(0x14, 0x0)
    Return()

    # Function_30_4220 end

    def Function_31_424F(): pass

    label("Function_31_424F")

    Sleep(100)
    SetChrChipByIndex(0x15, 0x23)
    SetChrSubChip(0x15, 0x0)

    def lambda_425F():
        OP_96(0xFE, 0x29CC, 0x0, 0x3200, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_425F)
    WaitChrThread(0x15, 1)
    SetChrChipByIndex(0x15, 0x22)
    SetChrSubChip(0x15, 0x0)
    Return()

    # Function_31_424F end

    def Function_32_4281(): pass

    label("Function_32_4281")

    Sleep(50)
    SetChrChipByIndex(0x16, 0x1D)
    SetChrSubChip(0x16, 0x0)

    def lambda_4291():
        OP_96(0xFE, 0x2648, 0x0, 0x28A0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_4291)
    WaitChrThread(0x16, 1)
    SetChrChipByIndex(0x16, 0x1C)
    SetChrSubChip(0x16, 0x0)
    OP_93(0x16, 0x13B, 0x1F4)
    Return()

    # Function_32_4281 end

    def Function_33_42BA(): pass

    label("Function_33_42BA")

    Sleep(150)
    SetChrChipByIndex(0x17, 0x23)
    SetChrSubChip(0x17, 0x0)

    def lambda_42CA():
        OP_96(0xFE, 0x1EDC, 0x0, 0x25E4, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_42CA)
    WaitChrThread(0x17, 1)
    SetChrChipByIndex(0x17, 0x22)
    SetChrSubChip(0x17, 0x0)
    OP_93(0x17, 0x13B, 0x1F4)
    Return()

    # Function_33_42BA end

    def Function_34_42F3(): pass

    label("Function_34_42F3")

    Sleep(150)
    SetChrChipByIndex(0x18, 0x1D)
    SetChrSubChip(0x18, 0x0)

    def lambda_4303():
        OP_96(0xFE, 0x30D4, 0x0, 0x3200, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_4303)
    WaitChrThread(0x18, 1)
    SetChrChipByIndex(0x18, 0x1C)
    SetChrSubChip(0x18, 0x0)
    Sound(808, 0, 100, 0)
    Return()

    # Function_34_42F3 end

    def Function_35_432B(): pass

    label("Function_35_432B")

    SetChrChipByIndex(0x10, 0x20)
    SetChrSubChip(0x10, 0x0)

    def lambda_4338():
        OP_96(0xFE, 0xFFFFFBB4, 0x0, 0x2BC0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_4338)
    WaitChrThread(0x10, 1)
    SetChrChipByIndex(0x10, 0x1F)
    SetChrSubChip(0x10, 0x0)
    Return()

    # Function_35_432B end

    def Function_36_435A(): pass

    label("Function_36_435A")

    Sleep(100)
    SetChrChipByIndex(0x11, 0x20)
    SetChrSubChip(0x11, 0x0)

    def lambda_436A():
        OP_96(0xFE, 0xFFFFFAEC, 0x0, 0x23F0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_436A)
    WaitChrThread(0x11, 1)
    SetChrChipByIndex(0x11, 0x1F)
    SetChrSubChip(0x11, 0x0)
    OP_93(0x11, 0x2D, 0x1F4)
    Return()

    # Function_36_435A end

    def Function_37_4393(): pass

    label("Function_37_4393")

    Sleep(50)
    SetChrChipByIndex(0x12, 0x20)
    SetChrSubChip(0x12, 0x0)

    def lambda_43A3():
        OP_96(0xFE, 0x2BC, 0x0, 0x2328, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_43A3)
    WaitChrThread(0x12, 1)
    SetChrChipByIndex(0x12, 0x1F)
    SetChrSubChip(0x12, 0x0)
    OP_93(0x12, 0x2D, 0x1F4)
    Return()

    # Function_37_4393 end

    def Function_38_43CC(): pass

    label("Function_38_43CC")

    Sleep(150)
    SetChrChipByIndex(0x13, 0x26)
    SetChrSubChip(0x13, 0x0)

    def lambda_43DC():
        OP_96(0xFE, 0x578, 0x0, 0x1E78, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_43DC)
    WaitChrThread(0x13, 1)
    SetChrChipByIndex(0x13, 0x25)
    SetChrSubChip(0x13, 0x0)
    Sound(531, 0, 100, 0)
    OP_93(0x13, 0x2D, 0x1F4)
    Return()

    # Function_38_43CC end

    SaveToFile()

Try(main)
