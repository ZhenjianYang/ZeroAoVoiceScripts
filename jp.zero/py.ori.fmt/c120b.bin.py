from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "警備隊員",               # 1
        "警備隊員",               # 2
        "警備隊員",               # 3
        "警備隊員",               # 4
        "警備隊員",               # 5
        "ワジ",                   # 6
        "ヴァルド",               # 7
        "アッバス",               # 8
        "青装束の青年",           # 9
        "青装束の青年",           # 10
        "青装束の青年",           # 11
        "青装束の青年",           # 12
        "赤ジャージの青年",       # 13
        "赤ジャージの青年",       # 14
        "赤ジャージの青年",       # 15
        "赤ジャージの青年",       # 16
        "赤ジャージの青年",       # 17
        "車１",                   # 18
        "ダミー",                 # 19
        "ダミー",                 # 20
        "ダミー",                 # 21
        "中央広場",               # 22
        "西通り",                 # 23
        "行政区",                 # 24
        "住宅街",                 # 25
        "歓楽街",                 # 26
        "東通り",                 # 27
        "旧市街",                 # 28
        "港湾区",                 # 29
        "ＩＢＣ",                 # 30
        "駅前通り",               # 31
        "裏通り",                 # 32
        "ウルスラ間道",           # 33
        "東クロスベル街道",       # 34
        "西クロスベル街道",       # 35
        "マインツ山道",           # 36
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

    PlaceName(-123.13999938964844, 0.0, -85.1500015258789, 0x0000, 0x0000, "中央広場")
    PlaceName(-209.27000427246094, 0.0, -79.26000213623047, 0x0000, 0x0000, "西通り")
    PlaceName(-87.7699966430664, 0.0, 31.440000534057617, 0x0000, 0x0000, "行政区")
    PlaceName(-289.17999267578125, 0.0, 18.34000015258789, 0x0000, 0x0000, "住宅街")
    PlaceName(-193.5500030517578, 0.0, 7.860000133514404, 0x0000, 0x0000, "歓楽街")
    PlaceName(-16.700000762939453, 0.0, -115.27999877929688, 0x0000, 0x0000, "東通り")
    PlaceName(29.799999237060547, 0.0, -187.3300018310547, 0x0000, 0x0000, "旧市街")
    PlaceName(19.979999542236328, 0.0, -28.81999969482422, 0x0000, 0x0000, "港湾区")
    PlaceName(-14.079999923706055, 0.0, 94.31999969482422, 0x0000, 0x0000, "ＩＢＣ")
    PlaceName(-108.4000015258789, 0.0, -175.5399932861328, 0x0000, 0x0000, "駅前通り")
    PlaceName(-169.97000122070312, 0.0, -39.29999923706055, 0x0000, 0x0000, "裏通り")
    PlaceName(-112.33000183105469, 0.0, -216.14999389648438, 0x0000, 0x0000, "ウルスラ間道")
    PlaceName(54.040000915527344, 0.0, -96.94000244140625, 0x0000, 0x0000, "東クロスベル街道")
    PlaceName(-276.0799865722656, 0.0, -81.22000122070312, 0x0000, 0x0000, "西クロスベル街道")
    PlaceName(-268.2200012207031, 0.0, 49.779998779296875, 0x0000, 0x0000, "マインツ山道")
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
        "Function_5_149B",         # 05, 5
        "Function_6_1BB3",         # 06, 6
        "Function_7_217A",         # 07, 7
        "Function_8_29D9",         # 08, 8
        "Function_9_2B54",         # 09, 9
        "Function_10_2C15",        # 0A, 10
        "Function_11_2DAA",        # 0B, 11
        "Function_12_2E82",        # 0C, 12
        "Function_13_2F23",        # 0D, 13
        "Function_14_31D6",        # 0E, 14
        "Function_15_3366",        # 0F, 15
        "Function_16_33B4",        # 10, 16
        "Function_17_350A",        # 11, 17
        "Function_18_36B2",        # 12, 18
        "Function_19_3954",        # 13, 19
        "Function_20_3B73",        # 14, 20
        "Function_21_3CBC",        # 15, 21
        "Function_22_3DC2",        # 16, 22
        "Function_23_3E70",        # 17, 23
        "Function_24_3F18",        # 18, 24
        "Function_25_3FBE",        # 19, 25
        "Function_26_4064",        # 1A, 26
        "Function_27_410A",        # 1B, 27
        "Function_28_41B0",        # 1C, 28
        "Function_29_4256",        # 1D, 29
        "Function_30_427C",        # 1E, 30
        "Function_31_42AB",        # 1F, 31
        "Function_32_42DD",        # 20, 32
        "Function_33_4316",        # 21, 33
        "Function_34_434F",        # 22, 34
        "Function_35_4387",        # 23, 35
        "Function_36_43B6",        # 24, 36
        "Function_37_43EF",        # 25, 37
        "Function_38_4428",        # 26, 38
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
            "#5P#0404F……やれやれ。\x01",
            "完全に操られてるみたいだね。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_82(0xC8, 0x0, 0xBB8, 0x1F4)

    #C0002
    ChrTalk(
        0xE,
        "#5P#1607F#4S#Nオラアアアアッ！\x02",
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
            "#5P#1602Fハッ……\x01",
            "大したことねえじゃねえか！\x02\x03",

            "#1609Fこのヴァルド様の力にかかりゃあ、\x01",
            "警備隊なんざ──\x02",
        )
    )

    CloseMessageWindow()

    def lambda_E81():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_E81)

    def lambda_E9A():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_E9A)
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
        "#5P#1605Fな、なんだコイツら！？\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xD, 0x4)
    SetChrChipByIndex(0xD, 0x28)
    SetChrSubChip(0xD, 0x0)
    OP_68(4590, 1700, 16770, 600)

    def lambda_FA1():
        OP_98(0xFE, 0x0, 0x0, 0xFFFFFBB4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_FA1)
    WaitChrThread(0xD, 1)
    SetChrChipByIndex(0xD, 0x29)
    SetChrSubChip(0xD, 0x0)
    OP_6F(0x1)

    #C0007
    ChrTalk(
        0xD,
        (
            "#5P#0406Fだから言っただろう？\x01",
            "薬をキメてタフになってるって。\x02\x03",

            "#0400F行方不明になった\x01",
            "君の所のディーノ君と同じさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0xE,
        (
            "#5P#1603Fチッ……そういう事か。\x02\x03",

            "#1601Fどうやら落とし前を\x01",
            "付ける必要がありそうだな……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_82(0xC8, 0x0, 0xBB8, 0x1F4)

    #C0009
    ChrTalk(
        0xE,
        "#5P#1607F#4Sてめえら、始めるぞ！\x02",
    )

    CloseMessageWindow()
    Sleep(150)
    SetMessageWindowPos(340, 100, -1, -1)
    SetChrName("青年たちの声")
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #A0010
    AnonymousTalk(
        0xFF,
        "#4Sウーッス！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0011
    ChrTalk(
        0xD,
        (
            "#5P#0400Fフフ……\x01",
            "こちらも聖戦の準備を！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    SetMessageWindowPos(80, 170, -1, -1)
    SetChrName("青年たちの声")
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #A0012
    AnonymousTalk(
        0xFF,
        "#4S了解#4Rヤー#！\x02",
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

    def lambda_127D():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_127D)
    Sleep(100)

    def lambda_128D():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_128D)
    Sleep(100)

    def lambda_129D():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_129D)
    Sleep(100)

    def lambda_12AD():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_12AD)
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
            "準備完了──\x01",
            "いつでもいいぞ、ワジ。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0xD,
        (
            "#0402Fフフ……\x01",
            "それでは聖戦を始めよう。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0xE,
        (
            "#1604F#6P暴れるには丁度良い夜だ……\x02\x03",

            "#1607Fてめえら、一人残らず\x01",
            "叩きのめしてふん縛#2Rじば#れ！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("バイパー＆テスタメンツ")
    OP_82(0xC8, 0x0, 0xBB8, 0x1F4)

    #A0016
    AnonymousTalk(
        0xFF,
        "#5Sおおっ！！\x02",
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

    def Function_5_149B(): pass

    label("Function_5_149B")

    Sleep(300)
    SetChrChipByIndex(0xFE, 0x16)
    SetChrSubChip(0xFE, 0x0)
    Sleep(70)
    SetChrSubChip(0xFE, 0x1)
    Sleep(70)
    SetChrSubChip(0xFE, 0x2)
    BeginChrThread(0x11, 3, 0, 11)

    def lambda_14BF():
        OP_A6(0xFE, 0x0, 0x1E, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_14BF)
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

    def lambda_171E():
        OP_A6(0xFE, 0x0, 0x1E, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_171E)
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

    def lambda_197D():
        OP_A6(0xFE, 0x0, 0x1E, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_197D)
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

    def lambda_1B81():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_1B81)

    def lambda_1B8E():
        OP_9D(0xFE, 0xA28, 0x0, 0x3908, 0x384, 0x9C4)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1B8E)
    WaitChrThread(0x8, 1)
    SetChrChipByIndex(0x8, 0x14)
    SetChrSubChip(0x8, 0x0)
    Return()

    # Function_5_149B end

    def Function_6_1BB3(): pass

    label("Function_6_1BB3")

    OP_52(0x9, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_NOT), scpexpr(EXPR_AND_SAVE), scpexpr(EXPR_END)))
    SetChrFlags(0x9, 0x4)
    SetChrChipByIndex(0x9, 0x15)
    SetChrSubChip(0x9, 0x1)

    def lambda_1BD1():
        OP_93(0xFE, 0x82, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_1BD1)

    def lambda_1BDE():
        OP_9D(0xFE, 0x170C, 0x0, 0x3B60, 0x2BC, 0x9C4)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1BDE)
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

    def lambda_1C20():
        OP_A6(0xFE, 0x0, 0x1E, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1C20)
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

    def lambda_1E7F():
        OP_A6(0xFE, 0x0, 0x1E, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1E7F)
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

    def lambda_20E6():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_20E6)

    def lambda_20F3():
        OP_9D(0xFE, 0x16A8, 0x0, 0x332C, 0x2BC, 0x9C4)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_20F3)
    WaitChrThread(0x9, 1)
    SetChrChipByIndex(0x9, 0x14)
    SetChrSubChip(0x9, 0x0)
    Sleep(100)
    SetChrChipByIndex(0x9, 0x17)
    SetChrSubChip(0x9, 0x0)

    def lambda_2127():
        OP_A6(0xFE, 0x64, 0x64, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_2127)

    def lambda_2140():
        OP_9D(0xFE, 0xDAC, 0x0, 0x3264, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2140)
    WaitChrThread(0x9, 1)

    def lambda_2161():
        OP_A6(0xFE, 0x32, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_2161)
    SetChrSubChip(0x9, 0x3)
    Return()

    # Function_6_1BB3 end

    def Function_7_217A(): pass

    label("Function_7_217A")

    SetChrChipByIndex(0xA, 0x16)
    SetChrSubChip(0xA, 0x2)
    OP_93(0xA, 0x82, 0x1F4)
    Sleep(100)
    BeginChrThread(0x14, 3, 0, 14)

    def lambda_2197():
        OP_A6(0xFE, 0x0, 0x1E, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2197)
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

    def lambda_2318():
        OP_A6(0xFE, 0x0, 0x1E, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2318)
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

    def lambda_2499():
        OP_A6(0xFE, 0x0, 0x1E, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2499)
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

    def lambda_2610():
        OP_A6(0xFE, 0x0, 0x1E, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2610)
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

    def lambda_27F5():
        OP_A6(0xFE, 0x0, 0x1E, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_27F5)
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

    # Function_7_217A end

    def Function_8_29D9(): pass

    label("Function_8_29D9")

    OP_52(0xB, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_NOT), scpexpr(EXPR_AND_SAVE), scpexpr(EXPR_END)))

    def lambda_29EA():

        label("loc_29EA")

        TurnDirection(0xFE, 0x13, 0)
        Yield()
        Jump("loc_29EA")

    QueueWorkItem2(0xB, 2, lambda_29EA)
    SetChrFlags(0xB, 0x4)
    SetChrChipByIndex(0xB, 0x19)
    SetChrSubChip(0xB, 0x1)
    Sound(854, 0, 100, 0)

    def lambda_2A0F():
        OP_9D(0xFE, 0x1068, 0x384, 0x1FA4, 0x76C, 0x9C4)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_2A0F)
    WaitChrThread(0xB, 1)
    Sleep(1000)
    Sound(854, 0, 100, 0)

    def lambda_2A39():
        OP_9D(0xFE, 0xCE4, 0x0, 0x2A30, 0x384, 0x9C4)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_2A39)
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

    def lambda_2A7F():
        OP_A6(0xFE, 0x32, 0x0, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_2A7F)
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

    def lambda_2AEF():
        OP_A6(0xFE, 0x64, 0x64, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_2AEF)

    def lambda_2B08():
        OP_9D(0xFE, 0xED8, 0x0, 0x2E18, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_2B08)
    WaitChrThread(0xB, 1)

    def lambda_2B29():
        OP_A6(0xFE, 0x32, 0x32, 0x2BC, 0xBB8)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_2B29)
    SetChrSubChip(0xB, 0x3)
    Sleep(500)
    SetChrSubChip(0xB, 0x2)
    Sleep(100)
    SetChrChipByIndex(0xB, 0x18)
    SetChrSubChip(0xB, 0x0)
    Return()

    # Function_8_29D9 end

    def Function_9_2B54(): pass

    label("Function_9_2B54")


    def lambda_2B59():
        OP_A6(0xFE, 0x32, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_2B59)
    SetChrChipByIndex(0xC, 0x17)
    SetChrSubChip(0xC, 0x1)
    Sleep(110)
    SetChrSubChip(0xC, 0x2)
    Sleep(110)
    SetChrSubChip(0xC, 0x3)
    Sleep(700)

    def lambda_2B8B():
        OP_A6(0xFE, 0x32, 0x32, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_2B8B)
    SetChrSubChip(0xC, 0x3)
    Sleep(200)
    SetChrSubChip(0xC, 0x2)
    Sleep(100)
    SetChrChipByIndex(0xC, 0x19)
    SetChrSubChip(0xC, 0x0)

    def lambda_2BBA():
        OP_9D(0xFE, 0xF3C, 0x0, 0x2E7C, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_2BBA)
    WaitChrThread(0xC, 1)
    Sleep(150)
    SetChrChipByIndex(0xC, 0x1A)
    SetChrSubChip(0xC, 0x1)

    def lambda_2BE6():
        OP_9D(0xFE, 0x13EC, 0x0, 0x2DB4, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_2BE6)
    Sleep(70)
    SetChrSubChip(0xC, 0x2)
    Sleep(70)
    SetChrSubChip(0xC, 0x3)
    WaitChrThread(0xC, 1)
    SetChrSubChip(0xC, 0x4)
    Return()

    # Function_9_2B54 end

    def Function_10_2C15(): pass

    label("Function_10_2C15")

    SetChrChipByIndex(0x10, 0x21)
    SetChrSubChip(0x10, 0x0)
    OP_52(0x10, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_NOT), scpexpr(EXPR_AND_SAVE), scpexpr(EXPR_END)))
    Sleep(110)
    Sound(814, 0, 100, 0)

    def lambda_2C37():
        OP_9C(0xFE, 0x0, 0x0, 0x0, 0x44C, 0xBB8)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_2C37)
    Sleep(150)
    SetChrSubChip(0x10, 0x1)
    Sleep(250)
    SetChrSubChip(0x10, 0x2)
    WaitChrThread(0x10, 1)
    PlayEffect(0x7, 0xFF, 0x10, 0x100, 0, 100, 300, 0, 0, 0, 350, 350, 350, 0xFF, 0, 0, 0, 0)
    Sound(332, 0, 100, 0)

    def lambda_2CA3():
        OP_A6(0xFE, 0x32, 0x0, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_2CA3)
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

    def lambda_2D09():
        OP_9C(0xFE, 0x0, 0x0, 0x0, 0x44C, 0xBB8)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_2D09)
    Sleep(150)
    SetChrSubChip(0x10, 0x1)
    Sleep(250)
    SetChrSubChip(0x10, 0x2)
    WaitChrThread(0x10, 1)
    PlayEffect(0x7, 0xFF, 0x10, 0x100, 0, 100, 300, 0, 0, 0, 350, 350, 350, 0xFF, 0, 0, 0, 0)
    Sound(332, 0, 100, 0)

    def lambda_2D75():
        OP_A6(0xFE, 0x32, 0x0, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_2D75)
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

    # Function_10_2C15 end

    def Function_11_2DAA(): pass

    label("Function_11_2DAA")

    Sleep(500)
    SetChrChipByIndex(0x11, 0x20)
    SetChrSubChip(0x11, 0x0)

    def lambda_2DBA():
        OP_96(0xFE, 0xFFFFF830, 0x0, 0x1FA4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_2DBA)
    WaitChrThread(0x11, 1)
    SetChrChipByIndex(0x11, 0x1F)
    SetChrSubChip(0x11, 0x0)
    Sleep(500)
    SetChrChipByIndex(0x11, 0x20)
    SetChrSubChip(0x11, 0x0)

    def lambda_2DEB():
        OP_96(0xFE, 0x4B0, 0x0, 0x2CEC, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_2DEB)
    WaitChrThread(0x11, 1)
    OP_52(0x11, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_NOT), scpexpr(EXPR_AND_SAVE), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x11, 0x34)
    SetChrSubChip(0x11, 0x0)

    def lambda_2E1D():
        OP_A6(0xFE, 0x64, 0x64, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_2E1D)

    def lambda_2E36():
        OP_9D(0xFE, 0xFFFFFE0C, 0x0, 0x24B8, 0x2BC, 0xBB8)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_2E36)
    WaitChrThread(0x11, 1)

    def lambda_2E57():
        OP_A6(0xFE, 0x32, 0x32, 0x5DC, 0xBB8)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_2E57)
    SetChrSubChip(0x11, 0x3)
    Sleep(1400)
    SetChrSubChip(0x11, 0x2)
    Sleep(100)
    SetChrChipByIndex(0x11, 0x1F)
    SetChrSubChip(0x11, 0x0)
    Return()

    # Function_11_2DAA end

    def Function_12_2E82(): pass

    label("Function_12_2E82")

    EndChrThread(0x12, 0x2)
    OP_93(0x12, 0x28, 0x0)
    SetChrFlags(0x12, 0x4)
    SetChrChipByIndex(0x12, 0x21)
    SetChrSubChip(0x12, 0x0)
    OP_52(0x12, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_NOT), scpexpr(EXPR_AND_SAVE), scpexpr(EXPR_END)))

    def lambda_2EAB():
        OP_9D(0xFE, 0xA28, 0x0, 0x27D8, 0x2BC, 0x9C4)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_2EAB)
    Sleep(150)
    SetChrSubChip(0x12, 0x1)
    Sleep(250)
    SetChrSubChip(0x12, 0x2)
    WaitChrThread(0x12, 1)

    def lambda_2EDA():
        OP_A6(0xFE, 0x32, 0x0, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_2EDA)
    Sleep(1100)
    SetChrChipByIndex(0x12, 0x20)
    SetChrSubChip(0x12, 0x1)

    def lambda_2EFE():
        OP_9D(0xFE, 0xC8, 0x0, 0x206C, 0x2BC, 0x9C4)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_2EFE)
    WaitChrThread(0x12, 1)
    SetChrChipByIndex(0x12, 0x1F)
    SetChrSubChip(0x12, 0x1)
    Return()

    # Function_12_2E82 end

    def Function_13_2F23(): pass

    label("Function_13_2F23")


    def lambda_2F28():

        label("loc_2F28")

        TurnDirection(0xFE, 0xB, 300)
        Yield()
        Jump("loc_2F28")

    QueueWorkItem2(0x12, 2, lambda_2F28)
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

    def lambda_2F79():
        OP_A6(0xFE, 0x32, 0x0, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_2F79)
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

    def lambda_3056():
        OP_A6(0xFE, 0x32, 0x0, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_3056)
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

    def lambda_3139():
        OP_A6(0xFE, 0x32, 0x0, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_3139)
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

    # Function_13_2F23 end

    def Function_14_31D6(): pass

    label("Function_14_31D6")

    SetChrChipByIndex(0x14, 0x1D)
    SetChrSubChip(0x14, 0x0)

    def lambda_31E3():
        OP_96(0xFE, 0x2B5C, 0x0, 0x3778, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_31E3)
    WaitChrThread(0x14, 1)
    SetChrChipByIndex(0x14, 0x1C)
    SetChrSubChip(0x14, 0x0)
    Sleep(700)
    SetChrChipByIndex(0x14, 0x1D)
    SetChrSubChip(0x14, 0x3)
    Sound(814, 0, 100, 0)

    def lambda_321A():
        OP_9D(0xFE, 0x33F4, 0x0, 0x3840, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_321A)
    WaitChrThread(0x14, 1)
    SetChrChipByIndex(0x14, 0x1C)
    SetChrSubChip(0x14, 0x0)
    Sleep(300)
    SetChrChipByIndex(0x14, 0x1D)
    SetChrSubChip(0x14, 0x0)

    def lambda_324E():
        OP_96(0xFE, 0x2580, 0x0, 0x3778, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_324E)
    WaitChrThread(0x14, 1)
    SetChrChipByIndex(0x14, 0x1E)
    SetChrSubChip(0x14, 0x1)
    Sound(814, 0, 100, 0)

    def lambda_327A():
        OP_9D(0xFE, 0x1AF4, 0x0, 0x3520, 0x44C, 0xBB8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_327A)
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

    def lambda_32F3():
        OP_A6(0xFE, 0x64, 0x64, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_32F3)
    SetChrChipByIndex(0x14, 0x35)
    SetChrSubChip(0x14, 0x0)

    def lambda_3314():
        OP_9D(0xFE, 0x24B8, 0x0, 0x38A4, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_3314)
    WaitChrThread(0x14, 1)
    Sleep(300)

    def lambda_3338():
        OP_A6(0xFE, 0x32, 0x32, 0x2BC, 0xBB8)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_3338)
    SetChrSubChip(0x14, 0x3)
    Sleep(200)
    SetChrSubChip(0x14, 0x2)
    Sleep(200)
    SetChrChipByIndex(0x14, 0x1C)
    SetChrSubChip(0x14, 0x0)
    Sleep(300)
    Return()

    # Function_14_31D6 end

    def Function_15_3366(): pass

    label("Function_15_3366")

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

    # Function_15_3366 end

    def Function_16_33B4(): pass

    label("Function_16_33B4")

    Sleep(100)
    SetChrChipByIndex(0x15, 0x23)
    SetChrSubChip(0x15, 0x0)

    def lambda_33C4():
        OP_96(0xFE, 0x1DB0, 0x0, 0x3264, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_33C4)
    WaitChrThread(0x15, 1)
    SetChrSubChip(0x15, 0x3)
    OP_52(0x15, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_NOT), scpexpr(EXPR_AND_SAVE), scpexpr(EXPR_END)))

    def lambda_33F2():
        OP_9D(0xFE, 0x2968, 0x0, 0x319C, 0x2BC, 0x9C4)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_33F2)
    WaitChrThread(0x15, 1)
    SetChrChipByIndex(0x15, 0x22)
    SetChrSubChip(0x15, 0x0)
    Sleep(100)

    def lambda_341E():
        OP_A6(0xFE, 0x32, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_341E)
    SetChrChipByIndex(0x15, 0x36)
    SetChrSubChip(0x15, 0x2)
    Sleep(200)
    SetChrSubChip(0x15, 0x3)
    Sleep(1300)

    def lambda_3449():
        OP_A6(0xFE, 0x32, 0x32, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_3449)
    SetChrSubChip(0x15, 0x2)
    Sleep(200)
    SetChrChipByIndex(0x15, 0x22)
    SetChrSubChip(0x15, 0x0)
    Sleep(100)
    SetChrChipByIndex(0x15, 0x23)
    SetChrSubChip(0x15, 0x0)

    def lambda_347C():
        OP_96(0xFE, 0x1DB0, 0x0, 0x3264, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_347C)
    WaitChrThread(0x15, 1)
    SetChrChipByIndex(0x15, 0x36)
    SetChrSubChip(0x15, 0x0)

    def lambda_34A2():
        OP_A6(0xFE, 0x64, 0x64, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_34A2)

    def lambda_34BB():
        OP_9D(0xFE, 0x2968, 0x0, 0x319C, 0x2BC, 0x9C4)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_34BB)
    WaitChrThread(0x15, 1)
    SetChrSubChip(0x15, 0x3)
    Sleep(300)

    def lambda_34E3():
        OP_A6(0xFE, 0x32, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_34E3)
    SetChrSubChip(0x15, 0x2)
    Sleep(200)
    SetChrChipByIndex(0x15, 0x24)
    SetChrSubChip(0x15, 0x0)
    Sleep(300)
    Return()

    # Function_16_33B4 end

    def Function_17_350A(): pass

    label("Function_17_350A")

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

    def lambda_358A():
        OP_A6(0xFE, 0x32, 0x0, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0x16, 2, lambda_358A)
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

    def lambda_35E7():
        OP_9D(0xFE, 0x1A2C, 0x0, 0x2BC0, 0x44C, 0xBB8)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_35E7)
    Sleep(250)
    SetChrSubChip(0x16, 0x2)
    WaitChrThread(0x16, 1)
    SetChrSubChip(0x16, 0x3)
    Sleep(500)

    def lambda_3616():
        OP_A6(0xFE, 0x64, 0x64, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0x16, 2, lambda_3616)
    PlayEffect(0x5, 0xFF, 0x16, 0x140, 0, 700, 500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrChipByIndex(0x16, 0x35)
    SetChrSubChip(0x16, 0x0)

    def lambda_366E():
        OP_9D(0xFE, 0x2198, 0x0, 0x2C88, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_366E)
    WaitChrThread(0x16, 1)

    def lambda_368F():
        OP_A6(0xFE, 0x32, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x16, 2, lambda_368F)
    SetChrSubChip(0x16, 0x2)
    Sleep(200)
    SetChrSubChip(0x16, 0x3)
    Sleep(300)
    Return()

    # Function_17_350A end

    def Function_18_36B2(): pass

    label("Function_18_36B2")

    OP_52(0x17, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_NOT), scpexpr(EXPR_AND_SAVE), scpexpr(EXPR_END)))
    SetChrFlags(0x17, 0x20)
    SetChrChipByIndex(0x17, 0x24)
    SetChrSubChip(0x17, 0x0)
    Sleep(70)
    SetChrSubChip(0x17, 0x1)
    Sleep(130)
    SetChrSubChip(0x17, 0x2)

    def lambda_36DE():
        OP_96(0xFE, 0x1838, 0x0, 0x2968, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_36DE)
    BeginChrThread(0x18, 3, 0, 19)
    Sleep(200)
    SetChrSubChip(0x17, 0x3)
    WaitChrThread(0x17, 1)
    SetChrChipByIndex(0xC, 0x1A)
    SetChrSubChip(0xC, 0x2)
    PlayEffect(0x5, 0xFF, 0x17, 0x140, 0, 900, 1000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_3748():
        OP_A6(0xFE, 0x32, 0x0, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_3748)

    def lambda_3761():
        OP_A6(0xFE, 0x32, 0x0, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_3761)
    Sleep(700)
    BeginChrThread(0x10, 3, 0, 10)
    Sleep(300)
    SetChrChipByIndex(0x17, 0x23)
    SetChrSubChip(0x17, 0x3)

    def lambda_378E():
        OP_9D(0xFE, 0x1EDC, 0x0, 0x25E4, 0x3E8, 0x9C4)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_378E)
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

    def lambda_37DA():

        label("loc_37DA")

        TurnDirection(0xFE, 0xC, 0)
        Yield()
        Jump("loc_37DA")

    QueueWorkItem2(0x17, 2, lambda_37DA)
    SetChrChipByIndex(0x17, 0x23)
    SetChrSubChip(0x17, 0x1)

    def lambda_37F4():
        OP_9D(0xFE, 0x15E0, 0x0, 0x238C, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_37F4)
    WaitChrThread(0x17, 1)
    SetChrChipByIndex(0x17, 0x22)
    SetChrSubChip(0x17, 0x0)
    Sleep(150)
    SetChrChipByIndex(0x17, 0x23)
    SetChrSubChip(0x17, 0x3)

    def lambda_3828():
        OP_9D(0xFE, 0x1EDC, 0x0, 0x25E4, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_3828)
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

    def lambda_386E():
        OP_96(0xFE, 0x1838, 0x0, 0x2968, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_386E)
    Sleep(200)
    SetChrSubChip(0x17, 0x3)
    WaitChrThread(0x17, 1)
    SetChrChipByIndex(0xC, 0x1A)
    SetChrSubChip(0xC, 0x2)
    PlayEffect(0x5, 0xFF, 0x17, 0x140, 0, 900, 1000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_38D2():
        OP_A6(0xFE, 0x32, 0x0, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_38D2)

    def lambda_38EB():
        OP_A6(0xFE, 0x32, 0x0, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_38EB)
    Sleep(1000)
    SetChrChipByIndex(0x17, 0x23)
    SetChrSubChip(0x17, 0x3)

    def lambda_390F():
        OP_9D(0xFE, 0x1EDC, 0x0, 0x25E4, 0x3E8, 0x9C4)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_390F)
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

    # Function_18_36B2 end

    def Function_19_3954(): pass

    label("Function_19_3954")

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

    def lambda_39D1():
        OP_A6(0xFE, 0x32, 0x0, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0x18, 2, lambda_39D1)
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

    def lambda_3A87():
        OP_A6(0xFE, 0x32, 0x0, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0x18, 2, lambda_3A87)
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

    def lambda_3B37():
        OP_A6(0xFE, 0x32, 0x0, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0x18, 2, lambda_3B37)
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

    # Function_19_3954 end

    def Function_20_3B73(): pass

    label("Function_20_3B73")

    Sleep(400)
    SetChrChipByIndex(0xD, 0x2A)
    SetChrSubChip(0xD, 0x0)

    def lambda_3B83():
        OP_95(0xFE, 3500, 2000, 22200, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_3B83)
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

    def lambda_3BD3():
        OP_9D(0xFE, 0xDAC, 0x3E8, 0x4718, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_3BD3)
    WaitChrThread(0xD, 1)
    SetChrChipByIndex(0xD, 0x2C)
    SetChrSubChip(0xD, 0x0)
    Sleep(100)
    Sound(2092, 255, 100, 0)    #voice#Lazy
    OP_52(0xD, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    PlayEffect(0x1, 0xFF, 0xD, 0x0, 0, 1700, 0, 180, 0, 0, 900, 900, 900, 0xFF, 0, 0, 0, 0)
    Sound(324, 0, 100, 0)
    Sound(625, 0, 100, 0)

    def lambda_3C53():
        OP_9D(0xFE, 0xDAC, 0x6A4, 0x4C2C, 0x708, 0x7D0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_3C53)
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

    # Function_20_3B73 end

    def Function_21_3CBC(): pass

    label("Function_21_3CBC")

    SetChrChipByIndex(0xE, 0x2F)
    SetChrSubChip(0xE, 0x0)

    def lambda_3CC9():
        OP_95(0xFE, 5500, 2000, 22200, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_3CC9)
    WaitChrThread(0xE, 1)
    SetChrChipByIndex(0xE, 0x31)
    SetChrSubChip(0xE, 0x1)
    SetChrChip(0x0, 0xE, 0x1E, 0x12C)
    OP_52(0xE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sound(814, 0, 100, 0)
    Sound(1793, 255, 100, 1)    #voice#Wald

    def lambda_3D0E():
        OP_9D(0xFE, 0x157C, 0x3E8, 0x4718, 0x190, 0xBB8)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_3D0E)
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

    # Function_21_3CBC end

    def Function_22_3DC2(): pass

    label("Function_22_3DC2")

    OP_82(0x0, 0x12C, 0xBB8, 0x1F4)
    SetChrChipByIndex(0xFE, 0x17)
    SetChrSubChip(0xFE, 0x0)
    PlayEffect(0x0, 0xFF, 0xFE, 0x0, 0, 1000, 0, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sound(501, 0, 100, 0)
    Sound(246, 0, 100, 0)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x4)

    def lambda_3E2C():
        OP_A6(0xFE, 0x0, 0x32, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_3E2C)

    def lambda_3E45():
        OP_9D(0xFE, 0xAF0, 0x0, 0x3390, 0x2BC, 0x7D0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_3E45)
    WaitChrThread(0x8, 1)
    SetChrSubChip(0xFE, 0x3)
    Sound(514, 0, 100, 0)
    WaitChrThread(0x8, 2)
    Return()

    # Function_22_3DC2 end

    def Function_23_3E70(): pass

    label("Function_23_3E70")

    OP_82(0x0, 0x12C, 0xBB8, 0x1F4)
    SetChrChipByIndex(0xFE, 0x17)
    SetChrSubChip(0xFE, 0x0)
    PlayEffect(0x0, 0xFF, 0xFE, 0x0, 0, 1000, 0, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sound(501, 0, 100, 0)
    Sound(246, 0, 100, 0)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x4)

    def lambda_3EDA():
        OP_A6(0xFE, 0x0, 0x32, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_3EDA)

    def lambda_3EF3():
        OP_9D(0xFE, 0x1838, 0x0, 0x3390, 0xC8, 0x7D0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_3EF3)
    WaitChrThread(0x9, 1)
    SetChrSubChip(0xFE, 0x3)
    WaitChrThread(0x9, 2)
    Return()

    # Function_23_3E70 end

    def Function_24_3F18(): pass

    label("Function_24_3F18")

    SetChrChipByIndex(0xFE, 0x15)
    SetChrSubChip(0xFE, 0x0)

    def lambda_3F25():
        OP_95(0xFE, -2200, 0, 11000, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3F25)

    def lambda_3F3F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3F3F)
    WaitChrThread(0xFE, 1)

    def lambda_3F54():
        OP_95(0xFE, 1200, 0, 11000, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3F54)
    WaitChrThread(0xFE, 1)
    ClearChrFlags(0xFE, 0x4)

    def lambda_3F77():
        OP_95(0xFE, 1200, 0, 11000, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3F77)
    WaitChrThread(0xFE, 1)

    def lambda_3F95():
        OP_95(0xFE, 3500, 600, 17200, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_3F95)
    WaitChrThread(0x8, 1)
    OP_93(0x8, 0x0, 0x1F4)
    SetChrChipByIndex(0xFE, 0x14)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_24_3F18 end

    def Function_25_3FBE(): pass

    label("Function_25_3FBE")

    SetChrChipByIndex(0xFE, 0x15)
    SetChrSubChip(0xFE, 0x0)

    def lambda_3FCB():
        OP_95(0xFE, -2200, 0, 11000, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3FCB)

    def lambda_3FE5():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3FE5)
    WaitChrThread(0xFE, 1)

    def lambda_3FFA():
        OP_95(0xFE, 1200, 0, 11000, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3FFA)
    WaitChrThread(0xFE, 1)
    ClearChrFlags(0xFE, 0x4)

    def lambda_401D():
        OP_95(0xFE, 1200, 0, 11000, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_401D)
    WaitChrThread(0xFE, 1)

    def lambda_403B():
        OP_95(0xFE, 5500, 600, 17200, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_403B)
    WaitChrThread(0x9, 1)
    OP_93(0x9, 0x0, 0x1F4)
    SetChrChipByIndex(0xFE, 0x14)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_25_3FBE end

    def Function_26_4064(): pass

    label("Function_26_4064")

    SetChrChipByIndex(0xFE, 0x15)
    SetChrSubChip(0xFE, 0x0)

    def lambda_4071():
        OP_95(0xFE, -2200, 0, 11000, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4071)

    def lambda_408B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_408B)
    WaitChrThread(0xFE, 1)

    def lambda_40A0():
        OP_95(0xFE, 1200, 0, 11000, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_40A0)
    WaitChrThread(0xFE, 1)
    ClearChrFlags(0xFE, 0x4)

    def lambda_40C3():
        OP_95(0xFE, 1200, 0, 11000, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_40C3)
    WaitChrThread(0xFE, 1)

    def lambda_40E1():
        OP_95(0xFE, 4500, 0, 14300, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_40E1)
    WaitChrThread(0xA, 1)
    OP_93(0xA, 0x0, 0x1F4)
    SetChrChipByIndex(0xFE, 0x14)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_26_4064 end

    def Function_27_410A(): pass

    label("Function_27_410A")

    SetChrChipByIndex(0xFE, 0x19)
    SetChrSubChip(0xFE, 0x0)

    def lambda_4117():
        OP_95(0xFE, -2200, 0, 11000, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4117)

    def lambda_4131():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4131)
    WaitChrThread(0xFE, 1)

    def lambda_4146():
        OP_95(0xFE, 1200, 0, 11000, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4146)
    WaitChrThread(0xFE, 1)
    ClearChrFlags(0xFE, 0x4)

    def lambda_4169():
        OP_95(0xFE, 1200, 0, 11000, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4169)
    WaitChrThread(0xFE, 1)

    def lambda_4187():
        OP_95(0xFE, 3000, 0, 11500, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_4187)
    WaitChrThread(0xB, 1)
    OP_93(0xB, 0x0, 0x1F4)
    SetChrChipByIndex(0xFE, 0x18)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_27_410A end

    def Function_28_41B0(): pass

    label("Function_28_41B0")

    SetChrChipByIndex(0xFE, 0x19)
    SetChrSubChip(0xFE, 0x0)

    def lambda_41BD():
        OP_95(0xFE, -2200, 0, 11000, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_41BD)

    def lambda_41D7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_41D7)
    WaitChrThread(0xFE, 1)

    def lambda_41EC():
        OP_95(0xFE, 1200, 0, 11000, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_41EC)
    WaitChrThread(0xFE, 1)
    ClearChrFlags(0xFE, 0x4)

    def lambda_420F():
        OP_95(0xFE, 1200, 0, 11000, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_420F)
    WaitChrThread(0xFE, 1)

    def lambda_422D():
        OP_95(0xFE, 5000, 0, 11500, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_422D)
    WaitChrThread(0xC, 1)
    OP_93(0xC, 0x0, 0x1F4)
    SetChrChipByIndex(0xFE, 0x18)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_28_41B0 end

    def Function_29_4256(): pass

    label("Function_29_4256")


    def lambda_425B():
        OP_96(0xFE, 0x9C4, 0x7D0, 0x5140, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_425B)
    WaitChrThread(0xF, 1)
    OP_93(0xF, 0xB4, 0x1F4)
    Return()

    # Function_29_4256 end

    def Function_30_427C(): pass

    label("Function_30_427C")

    SetChrChipByIndex(0x14, 0x1D)
    SetChrSubChip(0x14, 0x0)

    def lambda_4289():
        OP_96(0xFE, 0x2648, 0x0, 0x36B0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_4289)
    WaitChrThread(0x14, 1)
    SetChrChipByIndex(0x14, 0x1C)
    SetChrSubChip(0x14, 0x0)
    Return()

    # Function_30_427C end

    def Function_31_42AB(): pass

    label("Function_31_42AB")

    Sleep(100)
    SetChrChipByIndex(0x15, 0x23)
    SetChrSubChip(0x15, 0x0)

    def lambda_42BB():
        OP_96(0xFE, 0x29CC, 0x0, 0x3200, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_42BB)
    WaitChrThread(0x15, 1)
    SetChrChipByIndex(0x15, 0x22)
    SetChrSubChip(0x15, 0x0)
    Return()

    # Function_31_42AB end

    def Function_32_42DD(): pass

    label("Function_32_42DD")

    Sleep(50)
    SetChrChipByIndex(0x16, 0x1D)
    SetChrSubChip(0x16, 0x0)

    def lambda_42ED():
        OP_96(0xFE, 0x2648, 0x0, 0x28A0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_42ED)
    WaitChrThread(0x16, 1)
    SetChrChipByIndex(0x16, 0x1C)
    SetChrSubChip(0x16, 0x0)
    OP_93(0x16, 0x13B, 0x1F4)
    Return()

    # Function_32_42DD end

    def Function_33_4316(): pass

    label("Function_33_4316")

    Sleep(150)
    SetChrChipByIndex(0x17, 0x23)
    SetChrSubChip(0x17, 0x0)

    def lambda_4326():
        OP_96(0xFE, 0x1EDC, 0x0, 0x25E4, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_4326)
    WaitChrThread(0x17, 1)
    SetChrChipByIndex(0x17, 0x22)
    SetChrSubChip(0x17, 0x0)
    OP_93(0x17, 0x13B, 0x1F4)
    Return()

    # Function_33_4316 end

    def Function_34_434F(): pass

    label("Function_34_434F")

    Sleep(150)
    SetChrChipByIndex(0x18, 0x1D)
    SetChrSubChip(0x18, 0x0)

    def lambda_435F():
        OP_96(0xFE, 0x30D4, 0x0, 0x3200, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_435F)
    WaitChrThread(0x18, 1)
    SetChrChipByIndex(0x18, 0x1C)
    SetChrSubChip(0x18, 0x0)
    Sound(808, 0, 100, 0)
    Return()

    # Function_34_434F end

    def Function_35_4387(): pass

    label("Function_35_4387")

    SetChrChipByIndex(0x10, 0x20)
    SetChrSubChip(0x10, 0x0)

    def lambda_4394():
        OP_96(0xFE, 0xFFFFFBB4, 0x0, 0x2BC0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_4394)
    WaitChrThread(0x10, 1)
    SetChrChipByIndex(0x10, 0x1F)
    SetChrSubChip(0x10, 0x0)
    Return()

    # Function_35_4387 end

    def Function_36_43B6(): pass

    label("Function_36_43B6")

    Sleep(100)
    SetChrChipByIndex(0x11, 0x20)
    SetChrSubChip(0x11, 0x0)

    def lambda_43C6():
        OP_96(0xFE, 0xFFFFFAEC, 0x0, 0x23F0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_43C6)
    WaitChrThread(0x11, 1)
    SetChrChipByIndex(0x11, 0x1F)
    SetChrSubChip(0x11, 0x0)
    OP_93(0x11, 0x2D, 0x1F4)
    Return()

    # Function_36_43B6 end

    def Function_37_43EF(): pass

    label("Function_37_43EF")

    Sleep(50)
    SetChrChipByIndex(0x12, 0x20)
    SetChrSubChip(0x12, 0x0)

    def lambda_43FF():
        OP_96(0xFE, 0x2BC, 0x0, 0x2328, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_43FF)
    WaitChrThread(0x12, 1)
    SetChrChipByIndex(0x12, 0x1F)
    SetChrSubChip(0x12, 0x0)
    OP_93(0x12, 0x2D, 0x1F4)
    Return()

    # Function_37_43EF end

    def Function_38_4428(): pass

    label("Function_38_4428")

    Sleep(150)
    SetChrChipByIndex(0x13, 0x26)
    SetChrSubChip(0x13, 0x0)

    def lambda_4438():
        OP_96(0xFE, 0x578, 0x0, 0x1E78, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_4438)
    WaitChrThread(0x13, 1)
    SetChrChipByIndex(0x13, 0x25)
    SetChrSubChip(0x13, 0x0)
    Sound(531, 0, 100, 0)
    OP_93(0x13, 0x2D, 0x1F4)
    Return()

    # Function_38_4428 end

    SaveToFile()

Try(main)
