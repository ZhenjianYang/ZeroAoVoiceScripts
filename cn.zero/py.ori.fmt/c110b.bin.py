from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "c110b.bin",                # FileName
        "c110b",                    # MapName
        "c110b",                    # Location
        0x0016,                     # MapIndex
        "ed7100",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x1D,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 22, 0, 2, 0, 3],
    )

    BuildStringList((
        "c110b",                  # 0
        "阿奈斯特秘书",           # 1
        "格蕾丝",                 # 2
        "达德利搜查官",           # 3
        "蔡特",                   # 4
        "赛尔盖科长",             # 5
        "麦克道尔市长",           # 6
        "哈尔特曼议长",           # 7
        "市职员",                 # 8
        "市职员",                 # 9
        "共和国派议员",           # 10
        "帝国派议员",             # 11
        "警备队员",               # 12
        "警备队员",               # 13
        "警备队员",               # 14
        "警备队员",               # 15
        "警备队员",               # 16
        "警备队员",               # 17
        "警备队员",               # 18
        "警备队员",               # 19
        "警备队员",               # 20
        "车１",                   # 21
        "车２",                   # 22
        "车３",                   # 23
        "SE控制",                 # 24
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
    ))

    AddCharChip((
        "chr/ch00000.itc",                   # 00
        "chr/ch00000.itc",                   # 01
        "chr/ch00000.itc",                   # 02
        "chr/ch00000.itc",                   # 03
        "chr/ch00000.itc",                   # 04
        "chr/ch00000.itc",                   # 05
        "chr/ch00000.itc",                   # 06
        "chr/ch00000.itc",                   # 07
        "chr/ch00000.itc",                   # 08
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

    PlaceName(-31.530000686645508, 0.0, -107.9000015258789, 0x0000, 0x0000, "中央广场")
    PlaceName(-117.0, 0.0, -102.05000305175781, 0x0000, 0x0000, "西街")
    PlaceName(3.5799999237060547, 0.0, 7.800000190734863, 0x0000, 0x0000, "行政区")
    PlaceName(-196.3000030517578, 0.0, -5.199999809265137, 0x0000, 0x0000, "住宅街")
    PlaceName(-101.4000015258789, 0.0, -15.600000381469727, 0x0000, 0x0000, "欢乐街")
    PlaceName(74.0999984741211, 0.0, -137.8000030517578, 0x0000, 0x0000, "东街")
    PlaceName(120.25, 0.0, -209.3000030517578, 0x0000, 0x0000, "旧城区")
    PlaceName(110.5, 0.0, -52.0, 0x0000, 0x0000, "港湾区")
    PlaceName(76.69999694824219, 0.0, 70.19999694824219, 0x0000, 0x0000, "ＩＢＣ")
    PlaceName(-16.899999618530273, 0.0, -197.60000610351562, 0x0000, 0x0000, "站前街道")
    PlaceName(-78.0, 0.0, -62.400001525878906, 0x0000, 0x0000, "后巷")
    PlaceName(-20.799999237060547, 0.0, -237.89999389648438, 0x0000, 0x0000, "乌尔斯拉间道")
    PlaceName(144.3000030517578, 0.0, -119.5999984741211, 0x0000, 0x0000, "东克洛斯贝尔街道")
    PlaceName(-183.3000030517578, 0.0, -104.0, 0x0000, 0x0000, "西克洛斯贝尔街道")
    PlaceName(-175.5, 0.0, 26.0, 0x0000, 0x0000, "玛因兹山道")
    PlaceName(-60.130001068115234, 0.0, -126.0999984741211, 0x0000, 0x0051, "")
    PlaceName(9.75, 0.0, -92.30000305175781, 0x0000, 0x0054, "")
    PlaceName(-28.280000686645508, 0.0, -136.5, 0x0000, 0x0057, "")
    PlaceName(-61.099998474121094, 0.0, -88.4000015258789, 0x0000, 0x0053, "")
    PlaceName(-34.45000076293945, 0.0, -57.20000076293945, 0x0000, 0x0053, "")
    PlaceName(-100.43000030517578, 0.0, -94.9000015258789, 0x0000, 0x0053, "")
    PlaceName(-113.0999984741211, 0.0, -67.5999984741211, 0x0000, 0x0053, "")
    PlaceName(-81.9000015258789, 0.0, -26.0, 0x0000, 0x0052, "")
    PlaceName(-75.7300033569336, 0.0, -42.900001525878906, 0x0000, 0x0053, "")
    PlaceName(-64.3499984741211, 0.0, -53.95000076293945, 0x0000, 0x0053, "")
    PlaceName(-27.299999237060547, 0.0, 38.349998474121094, 0x0000, 0x0051, "")
    PlaceName(118.30000305175781, 0.0, -137.8000030517578, 0x0000, 0x0052, "")
    PlaceName(96.19999694824219, 0.0, -255.4499969482422, 0x0000, 0x0053, "")
    PlaceName(79.30000305175781, 0.0, -231.39999389648438, 0x0000, 0x0053, "")

    ScpFunction((
        "Function_0_660",          # 00, 0
        "Function_1_67C",          # 01, 1
        "Function_2_69B",          # 02, 2
        "Function_3_6BF",          # 03, 3
        "Function_4_6C0",          # 04, 4
        "Function_5_6FD",          # 05, 5
        "Function_6_7B6",          # 06, 6
        "Function_7_F7E",          # 07, 7
        "Function_8_1F8C",         # 08, 8
        "Function_9_2022",         # 09, 9
        "Function_10_20B8",        # 0A, 10
        "Function_11_2185",        # 0B, 11
        "Function_12_21C2",        # 0C, 12
        "Function_13_21FF",        # 0D, 13
        "Function_14_222F",        # 0E, 14
        "Function_15_226C",        # 0F, 15
        "Function_16_229C",        # 10, 16
        "Function_17_22DC",        # 11, 17
        "Function_18_2347",        # 12, 18
        "Function_19_2384",        # 13, 19
        "Function_20_23C1",        # 14, 20
        "Function_21_23FE",        # 15, 21
        "Function_22_243B",        # 16, 22
        "Function_23_2478",        # 17, 23
        "Function_24_24B5",        # 18, 24
        "Function_25_24FA",        # 19, 25
        "Function_26_2561",        # 1A, 26
        "Function_27_2653",        # 1B, 27
    ))


    def Function_0_660(): pass

    label("Function_0_660")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_67B")
    OP_A1(0xFE, 0x5DC, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Jump("Function_0_660")

    label("loc_67B")

    Return()

    # Function_0_660 end

    def Function_1_67C(): pass

    label("Function_1_67C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_69A")
    OP_A1(0xFE, 0x5DC, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    Jump("Function_1_67C")

    label("loc_69A")

    Return()

    # Function_1_67C end

    def Function_2_69B(): pass

    label("Function_2_69B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_6AF")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 6)
    Jump("loc_6BE")

    label("loc_6AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 1)), scpexpr(EXPR_END)), "loc_6BE")
    ClearScenarioFlags(0x5C, 1)
    Event(0, 7)

    label("loc_6BE")

    Return()

    # Function_2_69B end

    def Function_3_6BF(): pass

    label("Function_3_6BF")

    Return()

    # Function_3_6BF end

    def Function_4_6C0(): pass

    label("Function_4_6C0")

    OP_95(0x8, -28130, 2460, 23580, 5700, 0x0)
    OP_95(0x8, -6100, 2500, 21500, 5700, 0x0)
    OP_95(0x8, 4520, 2500, 9280, 5700, 0x0)
    Return()

    # Function_4_6C0 end

    def Function_5_6FD(): pass

    label("Function_5_6FD")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7B5")
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_72B")
    Sleep(500)
    Jump("loc_773")

    label("loc_72B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x28), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_742")
    Sleep(200)
    Jump("loc_773")

    label("loc_742")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3C), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_759")
    Sleep(300)
    Jump("loc_773")

    label("loc_759")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x50), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_770")
    Sleep(400)
    Jump("loc_773")

    label("loc_770")

    Sleep(600)

    label("loc_773")

    PlayEffect(0x0, 0xFF, 0x9, 0xC0, 0, 1200, 400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(817, 0, 100, 0)
    Jump("Function_5_6FD")

    label("loc_7B5")

    Return()

    # Function_5_6FD end

    def Function_6_7B6(): pass

    label("Function_6_7B6")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00900.itc", 0x1E)
    LoadChrToIndex("apl/ch50229.itc", 0x1F)
    LoadChrToIndex("chr/ch02702.itc", 0x20)
    LoadChrToIndex("chr/ch06000.itc", 0x21)
    LoadChrToIndex("apl/ch50232.itc", 0x22)
    LoadChrToIndex("apl/ch50233.itc", 0x23)
    LoadChrToIndex("chr/ch02751.itc", 0x24)
    LoadChrToIndex("chr/ch02750.itc", 0x25)
    LoadChrToIndex("apl/ch50010.itc", 0x26)
    OP_68(4000, 4740, 8700, 0)
    MoveCamera(45, 17, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(17500, 0)
    SetChrFlags(0xA, 0x8000)
    SetChrChipByIndex(0xA, 0x1E)
    SetChrSubChip(0xA, 0x0)
    SetChrFlags(0x8, 0x8000)
    SetChrChipByIndex(0x8, 0x1F)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    SetChrFlags(0xB, 0x8000)
    SetChrChipByIndex(0xB, 0x24)
    SetChrSubChip(0xB, 0x0)
    SetChrFlags(0x9, 0x8000)
    SetChrChipByIndex(0x9, 0x21)
    SetChrSubChip(0x9, 0x0)
    SetChrPos(0x8, -36970, 10, 23640, 90)
    LoadEffect(0x0, "event\\eva02_00.eff")
    LoadEffect(0x1, "event\\eva04_00.eff")

    SetMessageWindowPos(-1, -1, -1, -1)
    AnonymousTalk(    #talk#5000
        0x8,
        (
            "#5P#8A#60W#2613F呵呵……\x01",
            "怎能就此结束…#3000W…#30W \x02\x03",
        )
    )
    Sleep(4000)
    CloseMessageWindow()

    FadeToBright(1000, 0)
    OP_6B(0x8)
    OP_68(-36520, 2770, 23050, 0)
    MoveCamera(354, 40, 0, 0)
    OP_6E(780, 0)
    SetCameraDistance(12000, 0)
    MoveCamera(90, 10, 0, 8000)
    OP_6E(780, 8000)
    SetCameraDistance(12000, 8000)
    SetChrFlags(0xB, 0x8000)
    SetChrFlags(0xB, 0x4)
    SetChrPos(0xB, 14310, 17110, 10280, 78)
    BeginChrThread(0x8, 0, 0, 4)
    OP_0D()

    #C0001
    ChrTalk(
        0x8,
        (
            # "#5P#8A#60W#2613F呵呵……\x01",
            # "怎能就此结束…#4000W…30W# \x02\x03",

            "#32A#30W#2610F我……\x01",
            "我要成为下任市长……！\x02\x03",

            "#25A#20W#2610F只要有哈尔特曼议长做后盾，\x01",
            "我就一定能在下一届市长选举中……！\x02",
        )
    )
    #Auto

    Sleep(5000)
    OP_52(0xB, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    OP_93(0xB, 0x10E, 0x0)
    SetChrChip(0x0, 0xB, 0x32, 0x12C)
    SetChrSubChip(0xB, 0x0)
    OP_9D(0xB, 0x2314, 0x9C4, 0x1C34, 0xBB8, 0xFA0)
    PlayEffect(0x1, 0xFF, 0xB, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(814, 0, 100, 0)
    Fade(500)
    OP_6B(0xFF)
    OP_68(4520, 3540, 9280, 0)
    MoveCamera(46, 25, 0, 0)
    OP_6E(780, 0)
    SetCameraDistance(12000, 0)

    def lambda_A78():
        OP_93(0xFE, 0x0, 0x64)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_A78)
    Sound(43, 0, 100, 0)
    Sound(46, 0, 100, 0)
    OP_9D(0xB, 0x1590, 0x9C4, 0x17E8, 0x3E8, 0x1770)
    PlayEffect(0x1, 0xFF, 0xB, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(854, 0, 100, 0)
    SetChrSubChip(0xB, 0x2)
    Sleep(100)
    SetChrSubChip(0xB, 0x0)
    Sound(2049, 255, 100, 0)    #voice#Zeit
    OP_9D(0xB, 0x1202, 0x9C4, 0x2238, 0x7D0, 0x1770)
    Sound(814, 0, 100, 0)
    SetChrChip(0x1, 0xB, 0x0, 0x0)
    SetChrChipByIndex(0xB, 0x25)
    SetChrSubChip(0xB, 0x0)
    BeginChrThread(0xB, 0, 0, 1)
    Sound(43, 0, 100, 0)
    Sound(46, 0, 100, 0)
    Sound(1876, 255, 100, 1)    #voice#Earnest
    OP_82(0x0, 0x12C, 0xBB8, 0x1F4)
    SetChrChipByIndex(0x8, 0x22)
    SetChrSubChip(0x8, 0x0)
    Sound(819, 0, 100, 0)
    Sound(804, 0, 100, 0)
    Sleep(60)
    SetChrChipByIndex(0x8, 0x23)
    SetChrSubChip(0x8, 0x0)
    SetChrPos(0x8, 4520, 2300, 9280, 321)
    Sound(514, 0, 100, 0)

    #C0002
    ChrTalk(
        0x8,
        "#2615F呜哇……！？\x02",
    )

    CloseMessageWindow()
    #Sound(2058, 255, 100, 0)    #voice#Zeit

    #C0003
    ChrTalk(
        0xB,
        "#1201F#11P呜噜噜噜噜……\x02",
    )

    CloseMessageWindow()
    OP_68(3990, 3750, 10640, 5000)
    MoveCamera(30, 28, 0, 5000)
    OP_6E(780, 5000)
    SetCameraDistance(12000, 5000)
    SetChrPos(0x101, -3290, 2500, 18180, 316)
    SetChrPos(0xA, -4530, 2500, 17470, 316)
    SetChrPos(0x104, -3130, 2500, 19300, 316)
    SetChrPos(0x103, -5020, 2500, 19570, 316)
    SetChrPos(0x9, -600, 2500, 16700, 120)

    def lambda_C41():
        OP_95(0xFE, 3240, 2500, 11490, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_C41)
    Sleep(500)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)

    def lambda_C68():
        OP_95(0xFE, 1810, 2500, 10970, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_C68)
    Sleep(500)

    def lambda_C85():
        OP_95(0xFE, 3400, 2500, 12610, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_C85)

    def lambda_C9F():
        OP_95(0xFE, 1910, 2500, 12470, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_C9F)
    WaitChrThread(0x101, 0)

    #C0004
    ChrTalk(
        0x101,
        "#0002F#5P蔡特……！\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0xA, 0)

    #C0005
    ChrTalk(
        0xA,
        "#0610F#5P唔……是那只狼吗……！\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x103, 0)

    #C0006
    ChrTalk(
        0x103,
        "#0204F#5P……干得好。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    SetChrChipByIndex(0xB, 0x20)
    SetChrSubChip(0xB, 0x0)

    def lambda_D2E():

        label("loc_D2E")

        OP_A0(0xFE, 1500, 0x0, 0xFB)
        Yield()
        Jump("loc_D2E")

    QueueWorkItem2(0xB, 0, lambda_D2E)
    OP_0D()
    WaitChrThread(0x104, 0)

    #C0007
    ChrTalk(
        0x104,
        (
            "#0302F#5P哎呀呀……\x01",
            "还真是独占功劳啊。\x02",
        )
    )

    CloseMessageWindow()

    #N0008
    NpcTalk(
        0x9,
        "女性的声音",
        "不，独占功劳的是我才对！\x02",
    )

    CloseMessageWindow()
    Fade(500)
    OP_68(4740, 3400, 11080, 0)
    MoveCamera(76, 34, 0, 0)
    OP_6E(620, 0)
    SetCameraDistance(15000, 0)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    OP_95(0x9, 4320, 2410, 15000, 5000, 0x0)
    OP_95(0x9, 5920, 2500, 10050, 5000, 0x0)
    TurnDirection(0x9, 0x8, 500)
    SetChrChipByIndex(0x9, 0x26)
    SetChrSubChip(0x9, 0x0)
    BeginChrThread(0x9, 0, 0, 5)
    Sleep(2000)

    #C0009
    ChrTalk(
        0x101,
        "#0012F#6P什、什么时候……\x02",
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x103,
        "#0211F#6P#N真会见缝插针啊……\x02",
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1200)

    #C0011
    ChrTalk(
        0xA,
        (
            "#0606F#6P#N你、你们……\x01",
            "给我适可而止吧……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)

    #C0012
    ChrTalk(
        0x8,
        (
            "#2614F#5P#40W唔唔唔……放开我……\x02\x03",

            "#40W我、我……我一定要……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    BlurSwitch(0xBB8, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    SetCameraDistance(36000, 4000)
    OP_82(0xC8, 0x0, 0x7D0, 0x5DC)

    #C0013
    ChrTalk(
        0x8,
        "#2615F#4S#5P#22A#70W一定要成为下任市长啊！\x02",
    )
    #Auto

    Sleep(1000)
    FadeToDark(3000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    CancelBlur(0)
    EndChrThread(0x9, 0x0)
    Sound(879, 0, 100, 0)
    StopBGM(0xFA0)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x5E, 1)
    NewScene("e3400", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_6_7B6 end

    def Function_7_F7E(): pass

    label("Function_7_F7E")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50539.itc", 0x1E)
    LoadChrToIndex("apl/ch50506.itc", 0x1F)
    LoadChrToIndex("chr/ch02750.itc", 0x20)
    LoadChrToIndex("chr/ch02751.itc", 0x21)
    LoadChrToIndex("chr/ch02702.itc", 0x22)
    LoadChrToIndex("chr/ch31250.itc", 0x23)
    LoadChrToIndex("chr/ch31251.itc", 0x24)
    LoadChrToIndex("chr/ch31350.itc", 0x25)
    LoadChrToIndex("chr/ch31351.itc", 0x26)
    LoadChrToIndex("chr/ch05800.itc", 0x27)
    LoadChrToIndex("chr/ch06500.itc", 0x28)
    LoadChrToIndex("chr/ch28000.itc", 0x29)
    LoadChrToIndex("chr/ch34600.itc", 0x2A)
    LoadChrToIndex("chr/ch27700.itc", 0x2B)
    LoadChrToIndex("chr/ch27400.itc", 0x2C)
    LoadChrToIndex("chr/ch00150.itc", 0x2D)
    LoadChrToIndex("chr/ch00151.itc", 0x2E)
    LoadChrToIndex("chr/ch00250.itc", 0x2F)
    LoadChrToIndex("chr/ch00251.itc", 0x30)
    LoadChrToIndex("chr/ch00950.itc", 0x31)
    LoadChrToIndex("chr/ch00951.itc", 0x32)
    LoadChrToIndex("chr/ch00952.itc", 0x33)
    LoadChrToIndex("apl/ch50509.itc", 0x34)
    LoadChrToIndex("chr/ch00152.itc", 0x35)
    LoadChrToIndex("chr/ch31352.itc", 0x36)
    OP_68(7000, 3500, 11500, 0)
    MoveCamera(45, 23, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(18500, 0)
    SetChrPos(0x101, -42500, 0, 24400, 90)
    SetChrChipByIndex(0x102, 0x2D)
    SetChrSubChip(0x102, 0x0)
    SetChrPos(0x102, -43400, 0, 25100, 90)
    SetChrChipByIndex(0x103, 0x2F)
    SetChrSubChip(0x103, 0x0)
    SetChrPos(0x103, -43900, 0, 23600, 90)
    SetChrPos(0x104, -42700, 0, 23100, 90)
    SetChrChipByIndex(0x10A, 0x31)
    SetChrSubChip(0x10A, 0x0)
    SetChrPos(0x10A, -44800, 0, 24200, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrChipByIndex(0xC, 0x1E)
    SetChrSubChip(0xC, 0x0)
    SetChrFlags(0xC, 0x8000)
    ClearChrFlags(0xC, 0x4)
    SetChrPos(0xC, -44000, 0, 22200, 90)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    SetChrChipByIndex(0xB, 0x20)
    SetChrSubChip(0xB, 0x0)
    SetChrFlags(0xB, 0x8000)
    SetChrFlags(0xB, 0x20)
    ClearChrFlags(0xB, 0x4)
    SetChrPos(0xB, -45300, 0, 22800, 90)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    SetChrChipByIndex(0x13, 0x23)
    SetChrSubChip(0x13, 0x0)
    SetChrChipByIndex(0x14, 0x23)
    SetChrSubChip(0x14, 0x0)
    SetChrChipByIndex(0x15, 0x23)
    SetChrSubChip(0x15, 0x0)
    SetChrChipByIndex(0x16, 0x23)
    SetChrSubChip(0x16, 0x0)
    SetChrChipByIndex(0x17, 0x23)
    SetChrSubChip(0x17, 0x0)
    SetChrChipByIndex(0x18, 0x23)
    SetChrSubChip(0x18, 0x0)
    SetChrChipByIndex(0x19, 0x25)
    SetChrSubChip(0x19, 0x0)
    SetChrChipByIndex(0x1A, 0x25)
    SetChrSubChip(0x1A, 0x0)
    SetChrChipByIndex(0x1B, 0x25)
    SetChrSubChip(0x1B, 0x0)
    SetChrFlags(0x13, 0x8000)
    SetChrFlags(0x14, 0x8000)
    SetChrFlags(0x15, 0x8000)
    SetChrFlags(0x16, 0x8000)
    SetChrFlags(0x17, 0x8000)
    SetChrFlags(0x18, 0x8000)
    SetChrFlags(0x19, 0x8000)
    SetChrFlags(0x1A, 0x8000)
    SetChrFlags(0x1B, 0x8000)
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
    ClearChrFlags(0x19, 0x80)
    ClearChrBattleFlags(0x19, 0x8000)
    ClearChrFlags(0x1A, 0x80)
    ClearChrBattleFlags(0x1A, 0x8000)
    ClearChrFlags(0x1B, 0x80)
    ClearChrBattleFlags(0x1B, 0x8000)
    SetChrPos(0x13, 4300, 2500, 9900, 45)
    SetChrPos(0x14, 5500, 2500, 8900, 45)
    SetChrPos(0x15, 3700, 2500, 11700, 90)
    SetChrPos(0x16, 7200, 2500, 8100, 0)
    SetChrPos(0x17, -18900, 2500, 24200, 0)
    SetChrPos(0x18, -17700, 2500, 24200, 0)
    SetChrPos(0x19, -18300, 2500, 28000, 0)
    SetChrPos(0x1A, -18900, 2500, 25400, 0)
    SetChrPos(0x1B, -17700, 2500, 25400, 0)
    SetChrChipByIndex(0xD, 0x27)
    SetChrSubChip(0xD, 0x0)
    SetChrFlags(0xD, 0x8000)
    SetChrPos(0xD, 7500, 2500, 12000, 225)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    SetChrChipByIndex(0xE, 0x28)
    SetChrSubChip(0xE, 0x0)
    SetChrFlags(0xE, 0x8000)
    SetChrPos(0xE, 10200, 2500, 12700, 225)
    ClearChrFlags(0xE, 0x80)
    ClearChrBattleFlags(0xE, 0x8000)
    SetChrChipByIndex(0xF, 0x29)
    SetChrSubChip(0xF, 0x0)
    SetChrFlags(0xF, 0x8000)
    SetChrPos(0xF, 7500, 2500, 13100, 225)
    ClearChrFlags(0xF, 0x80)
    ClearChrBattleFlags(0xF, 0x8000)
    SetChrChipByIndex(0x10, 0x2A)
    SetChrSubChip(0x10, 0x0)
    SetChrFlags(0x10, 0x8000)
    SetChrPos(0x10, 8600, 2500, 12000, 225)
    ClearChrFlags(0x10, 0x80)
    ClearChrBattleFlags(0x10, 0x8000)
    SetChrChipByIndex(0x11, 0x2B)
    SetChrSubChip(0x11, 0x0)
    SetChrFlags(0x11, 0x8000)
    SetChrPos(0x11, 6700, 2500, 13600, 225)
    ClearChrFlags(0x11, 0x80)
    ClearChrBattleFlags(0x11, 0x8000)
    SetChrChipByIndex(0x12, 0x2C)
    SetChrSubChip(0x12, 0x0)
    SetChrFlags(0x12, 0x8000)
    SetChrPos(0x12, 10200, 2500, 13800, 225)
    ClearChrFlags(0x12, 0x80)
    ClearChrBattleFlags(0x12, 0x8000)
    OP_78(0x12, 0x1C)
    SetMapObjFlags(0x12, 0x1000)
    ClearMapObjFlags(0x12, 0x4)
    SetChrFlags(0x1C, 0x8000)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1C, 0x4)
    OP_49()
    SetChrPos(0x1C, 700, 2500, 13000, 0)
    OP_D3(0x1C, 0x0, 0x2710, 0x0, 0x0)
    OP_74(0x12, 0x1E)
    OP_70(0x12, 0x0)
    OP_78(0x13, 0x1D)
    SetMapObjFlags(0x13, 0x1000)
    ClearMapObjFlags(0x13, 0x4)
    SetChrFlags(0x1D, 0x8000)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x1D, 0x4)
    OP_49()
    SetChrPos(0x1D, 9000, 2500, 4700, 0)
    OP_D3(0x1D, 0x0, 0x13880, 0x0, 0x0)
    OP_74(0x13, 0x1E)
    OP_70(0x13, 0x0)
    OP_78(0x14, 0x1E)
    SetMapObjFlags(0x14, 0x1000)
    ClearMapObjFlags(0x14, 0x4)
    SetChrFlags(0x1E, 0x8000)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x1E, 0x4)
    OP_49()
    SetChrPos(0x1E, -14500, 2500, 21500, 0)
    OP_D3(0x1E, 0x0, 0x41EB0, 0x0, 0x0)
    OP_74(0x14, 0x1E)
    OP_70(0x14, 0x0)
    LoadEffect(0x0, "battle\\ms00001.eff")
    LoadEffect(0x1, "battle\\btgun00.eff")
    SetCameraDistance(16500, 3000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x10)

    #C0014
    ChrTalk(
        0xD,
        (
            "#2507F#5P你们到底要做什么！\x02\x03",

            "这是警备队司令的命令吗！？\x01",
            "做出这种事，可别妄想轻易了结啊！？\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x15,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#6P#30W………………………………\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#6P#35W………………………………\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0xD,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#2501F#5P唔……\x01",
            "（这毫无生气的眼神……！？）\x02",
        )
    )

    CloseMessageWindow()
    Sound(532, 0, 100, 0)
    Sleep(200)
    Sound(958, 0, 100, 0)
    Sleep(1000)
    Sound(532, 0, 100, 0)
    Sleep(200)
    Sound(958, 0, 100, 0)
    OP_63(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x12, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(50)
    OP_63(0xF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(50)
    OP_63(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_63(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    ClearChrFlags(0x19, 0x4)
    BeginChrThread(0x19, 3, 0, 26)
    OP_68(-18300, 3500, 28000, 3000)
    SetCameraDistance(17500, 3000)

    def lambda_1653():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_1653)

    def lambda_1660():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_1660)
    Sleep(50)

    def lambda_1670():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF, 2, lambda_1670)

    def lambda_167D():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_167D)
    Sleep(50)

    def lambda_168D():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_168D)

    def lambda_169A():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_169A)
    OP_6F(0x11)
    Sleep(3700)

    def lambda_16AC():
        OP_98(0xFE, 0x2710, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_16AC)
    Sleep(50)

    def lambda_16C9():
        OP_98(0xFE, 0x2710, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_16C9)
    Sleep(50)

    def lambda_16E6():
        OP_98(0xFE, 0x2710, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_16E6)
    Sleep(50)

    def lambda_1703():
        OP_98(0xFE, 0x2710, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1703)
    Sleep(50)

    def lambda_1720():
        OP_98(0xFE, 0x2710, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_1720)
    Sleep(50)
    SetChrChipByIndex(0xC, 0x1F)
    SetChrSubChip(0xC, 0x0)

    def lambda_1745():
        OP_98(0xFE, 0x2710, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_1745)
    Sleep(50)
    SetChrChipByIndex(0xB, 0x21)
    SetChrSubChip(0xB, 0x0)
    BeginChrThread(0xB, 0, 0, 0)
    BeginChrThread(0x1F, 1, 0, 27)

    def lambda_1776():
        OP_98(0xFE, 0x2710, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1776)
    Fade(500)
    OP_68(-34000, 2000, 23600, 0)
    MoveCamera(53, 15, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(18000, 0)
    OP_68(-32000, 2000, 23600, 2000)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x10A, 1)
    WaitChrThread(0xC, 1)
    SetChrChipByIndex(0xC, 0x1E)
    SetChrSubChip(0xC, 0x0)
    WaitChrThread(0xB, 1)
    EndChrThread(0xB, 0x0)
    EndChrThread(0x1F, 0x1)
    SetChrChipByIndex(0xB, 0x22)
    SetChrSubChip(0xB, 0x0)
    OP_6F(0x1)

    #C0018
    ChrTalk(
        0x103,
        "#6P#0201F（啊……）\x02",
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x10A,
        "#6P#0610F（难道总部……！？）\x02",
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x102,
        "#0107F#6P（市、市政厅也……！）\x02",
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0xC,
        (
            "#6P#1003F（……那道铁门没那么容易破坏，\x01",
            "　应该能坚持一段时间吧。）\x02\x03",

            "#1001F（追兵来了……\x01",
            "　绕过喷泉，然后返回中央广场吧！）\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x104,
        "#0301F#5P（遵命！）\x02",
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x101,
        (
            "#0010F#5P（芙兰……大家……\x01",
            "　一定要平安无事啊……！）\x02",
        )
    )

    CloseMessageWindow()
    OP_68(-25000, 2500, 23600, 2000)
    MoveCamera(45, 25, 0, 2000)
    SetCameraDistance(19000, 2000)
    BeginChrThread(0x104, 3, 0, 20)
    Sleep(100)
    BeginChrThread(0x101, 3, 0, 19)
    Sleep(50)
    BeginChrThread(0x103, 3, 0, 22)
    Sleep(50)
    BeginChrThread(0x102, 3, 0, 21)
    Sleep(250)
    BeginChrThread(0x10A, 3, 0, 23)
    Sleep(150)
    BeginChrThread(0xC, 3, 0, 24)
    Sleep(50)
    BeginChrThread(0xB, 3, 0, 25)
    OP_6F(0x79)
    Sleep(500)
    OP_63(0x18, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_19BF():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x18, 2, lambda_19BF)
    Sleep(50)
    OP_63(0x17, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_19E7():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_19E7)
    Sleep(50)
    OP_63(0x1A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_1A0F():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1A, 2, lambda_1A0F)
    Sleep(1000)
    SetChrChipByIndex(0x18, 0x24)
    SetChrSubChip(0x18, 0x0)
    BeginChrThread(0x18, 3, 0, 18)
    Sleep(100)
    SetChrChipByIndex(0x17, 0x24)
    SetChrSubChip(0x17, 0x0)
    BeginChrThread(0x17, 3, 0, 18)
    Sleep(50)
    SetChrChipByIndex(0x1A, 0x26)
    SetChrSubChip(0x1A, 0x0)
    BeginChrThread(0x1A, 3, 0, 18)
    Sleep(2500)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x104, 3)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x103, 3)
    WaitChrThread(0x10A, 3)
    WaitChrThread(0xC, 3)
    WaitChrThread(0xB, 3)
    SetChrPos(0x101, 9000, 2400, -14300, 135)
    SetChrPos(0x102, 8300, 2400, -12100, 135)
    SetChrPos(0x103, 7700, 2500, -13700, 135)
    SetChrPos(0x104, 9300, 2500, -13000, 135)
    SetChrPos(0x10A, 6700, 2500, -12500, 135)
    SetChrPos(0xC, 6500, 2500, -13500, 135)
    SetChrPos(0xB, 8700, 2400, -11200, 135)
    ClearScenarioFlags(0x0, 0)
    Fade(500)
    OP_68(19300, 3500, -22100, 0)
    MoveCamera(85, 20, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(18500, 0)
    MoveCamera(95, 20, 0, 4000)
    SetCameraDistance(16500, 4000)
    BeginChrThread(0x101, 3, 0, 11)
    Sleep(50)
    BeginChrThread(0x104, 3, 0, 12)
    Sleep(100)
    BeginChrThread(0x103, 3, 0, 14)
    Sleep(50)
    BeginChrThread(0x102, 3, 0, 13)
    Sleep(150)
    BeginChrThread(0xC, 3, 0, 16)
    Sleep(50)
    BeginChrThread(0x10A, 3, 0, 15)
    Sleep(150)
    BeginChrThread(0xB, 3, 0, 17)
    OP_0D()
    EndChrThread(0x18, 0x3)
    EndChrThread(0x18, 0x3)
    EndChrThread(0x1A, 0x3)
    EndChrThread(0x19, 0x3)
    OP_6F(0x50)
    Sleep(3000)

    #C0024
    ChrTalk(
        0x102,
        "#11P#0108F（外公……保重……！）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    WaitChrThread(0x102, 3)
    SetChrChipByIndex(0x102, 0x2D)
    SetChrSubChip(0x102, 0x0)
    OP_93(0x102, 0xB4, 0x1F4)

    def lambda_1BBD():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFD508, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1BBD)
    WaitChrThread(0xC, 3)
    SetChrChipByIndex(0xC, 0x1E)
    SetChrSubChip(0xC, 0x0)
    OP_93(0xC, 0xB4, 0x1F4)
    SetChrChipByIndex(0xC, 0x1F)
    SetChrSubChip(0xC, 0x0)

    def lambda_1BF2():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFD508, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_1BF2)
    WaitChrThread(0x10A, 3)
    SetChrChipByIndex(0x10A, 0x31)
    SetChrSubChip(0x10A, 0x0)
    OP_93(0x10A, 0xB4, 0x1F4)

    def lambda_1C1F():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFD508, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_1C1F)
    WaitChrThread(0x102, 1)

    def lambda_1C3D():
        OP_93(0xFE, 0xB4, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_1C3D)

    def lambda_1C4A():
        OP_93(0xFE, 0xB4, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_1C4A)

    def lambda_1C57():
        OP_93(0xFE, 0xB4, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 2, lambda_1C57)

    def lambda_1C64():
        OP_93(0xFE, 0xB4, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_1C64)

    def lambda_1C71():
        OP_93(0xFE, 0xB4, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_1C71)

    def lambda_1C7E():
        OP_93(0xFE, 0xB4, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_1C7E)
    Fade(500)
    OP_68(7000, 3500, 11500, 0)
    MoveCamera(45, 23, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16500, 0)
    OP_0D()
    EndChrThread(0xC, 0x1)
    EndChrThread(0x10A, 0x1)

    #C0025
    ChrTalk(
        0xD,
        "#2501F#5P艾、艾莉……！？\x02",
    )

    CloseMessageWindow()
    OP_93(0xD, 0xE1, 0x1F4)

    def lambda_1CED():
        OP_9B(0x1, 0xFE, 0x0, 0x384, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_1CED)
    WaitChrThread(0xD, 1)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0026
    ChrTalk(
        0xD,
        (
            "#2507F#5P啊，给我闪开！\x02\x03",

            "你们想对\x01",
            "我的孙女做什么！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xF, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)

    def lambda_1D61():
        OP_93(0xFE, 0xDC, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF, 2, lambda_1D61)
    Sleep(50)
    OP_63(0x10, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)

    def lambda_1D83():
        OP_93(0xFE, 0xE6, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_1D83)
    WaitChrThread(0xF, 2)

    def lambda_1D94():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_1D94)
    WaitChrThread(0x10, 2)

    def lambda_1DAD():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_1DAD)
    WaitChrThread(0xF, 1)

    def lambda_1DC6():
        TurnDirection(0xFE, 0xD, 500)
        ExitThread()

    QueueWorkItem(0xF, 2, lambda_1DC6)
    WaitChrThread(0x10, 1)

    def lambda_1DD7():
        TurnDirection(0xFE, 0xD, 500)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_1DD7)
    WaitChrThread(0xF, 2)
    WaitChrThread(0x10, 2)

    #N0027
    NpcTalk(
        0xF,
        "库利普主任",
        (
            "#3P市、市长……\x01",
            "请您冷静点！\x02",
        )
    )

    CloseMessageWindow()

    #N0028
    NpcTalk(
        0x10,
        "接待小姐希恩",
        (
            "#4P危险！\x01",
            "请您退后！\x02",
        )
    )

    CloseMessageWindow()
    OP_68(8770, 3500, 13270, 2000)
    SetCameraDistance(16500, 2000)
    OP_6F(0x79)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x1, 0x1)"), scpexpr(EXPR_END)), "loc_1E95")

    #N0029
    NpcTalk(
        0x11,
        "坎贝尔议员",
        "#5P到、到底发生了什么事！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_1EB6")

    label("loc_1E95")


    #C0030
    ChrTalk(
        0x11,
        "#5P到、到底发生了什么事！？\x02",
    )

    CloseMessageWindow()

    label("loc_1EB6")


    #C0031
    ChrTalk(
        0x12,
        (
            "#5P议、议长……！\x01",
            "您现在还是先进去避难为好……\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0xE,
        (
            "#2705F#5P啊，好……\x02\x03",

            "#2703F（不、不可能……\x01",
            "　为什么会变成这样……）\x02\x03",

            "#2701F（难道……！？\x01",
            "　这都是『他』干的好事吗！？）\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(17000, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    SetScenarioFlags(0x5C, 7)
    NewScene("c010B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_7_F7E end

    def Function_8_1F8C(): pass

    label("Function_8_1F8C")

    SetChrChipByIndex(0x102, 0x35)
    SetChrSubChip(0x102, 0x0)
    Sleep(50)
    SetChrSubChip(0x102, 0x1)
    Sleep(50)
    SetChrSubChip(0x102, 0x2)
    Sleep(400)

    label("loc_1FA5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2021")
    PlayEffect(0x1, 0xFF, 0xFE, 0x140, 0, 1100, 1000, 0, 0, 0, 900, 900, 900, 0xFF, 0, 0, 0, 0)
    Sound(530, 0, 100, 0)
    OP_82(0x32, 0x0, 0xBB8, 0x96)
    SetChrSubChip(0x102, 0x3)
    Sleep(150)
    SetChrSubChip(0x102, 0x4)
    Sleep(100)
    SetChrSubChip(0x102, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_201C")
    Sleep(1100)

    label("loc_201C")

    Jump("loc_1FA5")

    label("loc_2021")

    Return()

    # Function_8_1F8C end

    def Function_9_2022(): pass

    label("Function_9_2022")

    SetChrChipByIndex(0x10A, 0x33)
    SetChrSubChip(0x10A, 0x0)
    Sleep(700)

    label("loc_202D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_20B7")
    OP_82(0x32, 0x0, 0xBB8, 0x96)
    PlayEffect(0x1, 0xFF, 0xFE, 0x140, 0, 1300, 1100, 0, 0, 0, 900, 900, 900, 0xFF, 0, 0, 0, 0)
    Sound(567, 0, 90, 0)
    SetChrSubChip(0x10A, 0x1)
    Sleep(50)
    SetChrSubChip(0x10A, 0x2)
    Sleep(50)
    SetChrSubChip(0x10A, 0x3)
    Sleep(50)
    SetChrSubChip(0x10A, 0x4)
    Sleep(50)
    SetChrSubChip(0x10A, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_20B2")
    Sleep(1100)

    label("loc_20B2")

    Jump("loc_202D")

    label("loc_20B7")

    Return()

    # Function_9_2022 end

    def Function_10_20B8(): pass

    label("Function_10_20B8")

    SetChrChipByIndex(0xC, 0x34)
    SetChrSubChip(0xC, 0x4)
    Sleep(600)

    label("loc_20C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2184")
    OP_82(0x64, 0x0, 0xBB8, 0x96)
    PlayEffect(0x1, 0xFF, 0xFE, 0x140, 0, 1100, 1200, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)
    Sound(845, 0, 90, 0)
    SetChrSubChip(0xC, 0x5)
    Sleep(150)
    SetChrSubChip(0xC, 0x6)
    Sleep(100)
    SetChrSubChip(0xC, 0x7)
    Sleep(100)
    SetChrSubChip(0xC, 0x4)
    Sleep(100)
    SetChrSubChip(0xC, 0x3)
    Sleep(70)
    SetChrSubChip(0xC, 0x2)
    Sleep(70)
    SetChrSubChip(0xC, 0x1)
    Sleep(70)
    SetChrSubChip(0xC, 0x0)
    Sound(531, 0, 100, 0)
    Sleep(70)
    SetChrSubChip(0xC, 0x1)
    Sleep(70)
    SetChrSubChip(0xC, 0x2)
    Sleep(70)
    SetChrSubChip(0xC, 0x3)
    Sleep(70)
    SetChrSubChip(0xC, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_217F")
    Sleep(700)

    label("loc_217F")

    Jump("loc_20C3")

    label("loc_2184")

    Return()

    # Function_10_20B8 end

    def Function_11_2185(): pass

    label("Function_11_2185")


    def lambda_218A():
        OP_97(0xFE, 0x2AF8, 0x0, 0xFFFFD8F0, 0x1388, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_218A)
    WaitChrThread(0xFE, 1)

    def lambda_21A8():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFC568, 0x1388, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_21A8)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_11_2185 end

    def Function_12_21C2(): pass

    label("Function_12_21C2")


    def lambda_21C7():
        OP_97(0xFE, 0x2AF8, 0x0, 0xFFFFD8F0, 0x1388, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_21C7)
    WaitChrThread(0xFE, 1)

    def lambda_21E5():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFC568, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_21E5)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_12_21C2 end

    def Function_13_21FF(): pass

    label("Function_13_21FF")


    def lambda_2204():
        OP_97(0xFE, 0x2AF8, 0x0, 0xFFFFD8F0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2204)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x13B, 0x1F4)
    BeginChrThread(0x102, 0, 0, 8)
    WaitChrThread(0x102, 0)
    Return()

    # Function_13_21FF end

    def Function_14_222F(): pass

    label("Function_14_222F")


    def lambda_2234():
        OP_97(0xFE, 0x2AF8, 0x0, 0xFFFFD8F0, 0x1388, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2234)
    WaitChrThread(0xFE, 1)

    def lambda_2252():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFC568, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2252)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_14_222F end

    def Function_15_226C(): pass

    label("Function_15_226C")


    def lambda_2271():
        OP_97(0xFE, 0x2AF8, 0x0, 0xFFFFD8F0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2271)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x13B, 0x1F4)
    BeginChrThread(0x10A, 0, 0, 9)
    WaitChrThread(0x10A, 0)
    Return()

    # Function_15_226C end

    def Function_16_229C(): pass

    label("Function_16_229C")

    SetChrChipByIndex(0xC, 0x1F)
    SetChrSubChip(0xC, 0x0)

    def lambda_22A9():
        OP_97(0xFE, 0x2AF8, 0x0, 0xFFFFD8F0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_22A9)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0xC, 0x1E)
    SetChrSubChip(0xC, 0x0)
    OP_93(0xFE, 0x13B, 0x1F4)
    BeginChrThread(0xC, 0, 0, 10)
    WaitChrThread(0xC, 0)
    Return()

    # Function_16_229C end

    def Function_17_22DC(): pass

    label("Function_17_22DC")

    SetChrChipByIndex(0xB, 0x21)
    SetChrSubChip(0xB, 0x0)
    OP_52(0xB, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xB, 0, 0, 0)
    BeginChrThread(0x1F, 1, 0, 27)

    def lambda_230B():
        OP_97(0xFE, 0x2AF8, 0x0, 0xFFFFD8F0, 0x1388, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_230B)
    WaitChrThread(0xFE, 1)

    def lambda_2329():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFC568, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2329)
    WaitChrThread(0xFE, 1)
    EndChrThread(0x1F, 0x1)
    Return()

    # Function_17_22DC end

    def Function_18_2347(): pass

    label("Function_18_2347")


    def lambda_234C():
        OP_97(0xFE, 0xFFFFF060, 0x0, 0xFFFFEA84, 0x1388, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_234C)
    WaitChrThread(0xFE, 1)

    def lambda_236A():
        OP_97(0xFE, 0x1B58, 0x0, 0xFFFFE4A8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_236A)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_18_2347 end

    def Function_19_2384(): pass

    label("Function_19_2384")


    def lambda_2389():
        OP_97(0xFE, 0x157C, 0x0, 0x0, 0x1388, 0x1)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2389)
    WaitChrThread(0x101, 1)

    def lambda_23A7():
        OP_97(0xFE, 0x2710, 0x0, 0xFFFFD8F0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_23A7)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_19_2384 end

    def Function_20_23C1(): pass

    label("Function_20_23C1")


    def lambda_23C6():
        OP_97(0xFE, 0x157C, 0x0, 0x0, 0x1388, 0x1)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_23C6)
    WaitChrThread(0x104, 1)

    def lambda_23E4():
        OP_97(0xFE, 0x2710, 0x0, 0xFFFFD8F0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_23E4)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_20_23C1 end

    def Function_21_23FE(): pass

    label("Function_21_23FE")


    def lambda_2403():
        OP_97(0xFE, 0x1770, 0x0, 0x0, 0x1388, 0x1)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2403)
    WaitChrThread(0x102, 1)

    def lambda_2421():
        OP_97(0xFE, 0x2710, 0x0, 0xFFFFD8F0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2421)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_21_23FE end

    def Function_22_243B(): pass

    label("Function_22_243B")


    def lambda_2440():
        OP_97(0xFE, 0x1964, 0x0, 0x0, 0x1388, 0x1)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2440)
    WaitChrThread(0x103, 1)

    def lambda_245E():
        OP_97(0xFE, 0x2710, 0x0, 0xFFFFD8F0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_245E)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_22_243B end

    def Function_23_2478(): pass

    label("Function_23_2478")


    def lambda_247D():
        OP_97(0xFE, 0x1D4C, 0x0, 0x0, 0x1388, 0x1)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_247D)
    WaitChrThread(0x10A, 1)

    def lambda_249B():
        OP_97(0xFE, 0x2710, 0x0, 0xFFFFD8F0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_249B)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_23_2478 end

    def Function_24_24B5(): pass

    label("Function_24_24B5")

    SetChrChipByIndex(0xC, 0x1F)
    SetChrSubChip(0xC, 0x0)

    def lambda_24C2():
        OP_97(0xFE, 0x1B58, 0x0, 0x0, 0x1388, 0x1)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_24C2)
    WaitChrThread(0xC, 1)

    def lambda_24E0():
        OP_97(0xFE, 0x2710, 0x0, 0xFFFFD8F0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_24E0)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_24_24B5 end

    def Function_25_24FA(): pass

    label("Function_25_24FA")

    SetChrChipByIndex(0xB, 0x21)
    SetChrSubChip(0xB, 0x0)
    OP_52(0xB, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xB, 0, 0, 0)
    BeginChrThread(0x1F, 1, 0, 27)

    def lambda_2529():
        OP_97(0xFE, 0x1F40, 0x0, 0x0, 0x1388, 0x1)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_2529)
    WaitChrThread(0xB, 1)

    def lambda_2547():
        OP_97(0xFE, 0x2710, 0x0, 0xFFFFD8F0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2547)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_25_24FA end

    def Function_26_2561(): pass

    label("Function_26_2561")

    SetChrChipByIndex(0xFE, 0x36)

    label("loc_2565")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2652")
    SetChrSubChip(0xFE, 0x5)
    Sleep(100)
    SetChrSubChip(0xFE, 0x0)
    Sleep(100)
    SetChrSubChip(0xFE, 0x1)
    Sleep(600)
    SetChrFlags(0xFE, 0x20)

    def lambda_258F():
        OP_9B(0x1, 0xFE, 0x0, 0x384, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_258F)
    SetChrSubChip(0xFE, 0x2)
    Sound(532, 0, 100, 0)
    Sleep(50)
    SetChrSubChip(0xFE, 0x3)
    Sleep(50)
    SetChrSubChip(0xFE, 0x4)
    PlayEffect(0x0, 0xFF, 0x19, 0x0, 0, 1500, 1500, 0, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)
    Sound(958, 0, 100, 0)
    OP_82(0xC8, 0xC8, 0xBB8, 0xC8)
    Sleep(900)
    WaitChrThread(0xFE, 1)
    SetChrSubChip(0xFE, 0x5)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sound(804, 0, 100, 0)

    def lambda_2626():
        OP_9C(0xFE, 0x0, 0x0, 0xFFFFFC7C, 0xC8, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2626)
    WaitChrThread(0xFE, 1)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2565")

    label("loc_2652")

    Return()

    # Function_26_2561 end

    def Function_27_2653(): pass

    label("Function_27_2653")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_266C")
    Sound(925, 0, 100, 0)
    Sleep(500)
    Jump("Function_27_2653")

    label("loc_266C")

    Return()

    # Function_27_2653 end

    SaveToFile()

Try(main)
